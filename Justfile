[private]
default:
    @just --list --unsorted

config := absolute_path('config')
build := absolute_path('.build')
out := absolute_path('firmware')
draw := absolute_path('draw')

build_matrix := "build.yaml"

# parse build.yaml and filter targets by expression
_parse_targets $expr: _check_yq_version
    #!/usr/bin/env bash
    attrs="[.board, .shield, .snippet, .\"artifact-name\", .\"cmake-args\"]"
    filter="(($attrs | map(. // [.]) | combinations), ((.include // {})[] | $attrs)) | join(\",\")"
    echo "$(yq -r "$filter" {{build_matrix}} | grep -v "^," | grep -i "${expr/#all/.*}")"

# build firmware for single board & shield combination
_build_single $board $shield $snippet $artifact cmake_args *west_args:
    #!/usr/bin/env bash
    set -euo pipefail
    artifact="${artifact:-${shield:+${shield// /+}-}${board//\//_}}"
    build_dir="{{ build / '$artifact' }}"

    echo "Building firmware for $artifact..."
    west build -s zmk/app -d "$build_dir" -b $board {{ west_args }} ${snippet:+-S "$snippet"} -- \
        -DZMK_CONFIG="{{ config }}" ${shield:+-DSHIELD="$shield"} -DCMAKE_EXPORT_COMPILE_COMMANDS=ON {{ cmake_args }}

    if [[ -f "$build_dir/compile_commands.json" ]]; then
        ln -sf "$build_dir/compile_commands.json" "{{ justfile_directory() }}/compile_commands.json"
    fi

    if [[ -f "$build_dir/zephyr/zmk.uf2" ]]; then
        mkdir -p "{{ out }}" && cp "$build_dir/zephyr/zmk.uf2" "{{ out }}/$artifact.uf2"
    else
        mkdir -p "{{ out }}" && cp "$build_dir/zephyr/zmk.bin" "{{ out }}/$artifact.bin"
    fi

# flash firmware for single board & shield combination
# only needed for boards which do not support UF2
_flash_single $board $shield $artifact:
    #!/usr/bin/env bash
    set -euo pipefail
    artifact="${artifact:-${shield:+${shield// /+}-}${board//\//_}}"
    build_dir="{{ build / '$artifact' }}"

    echo "Flashing firmware for $artifact..."
    west flash -d "$build_dir"

# List build targets. The sed chain removes version and build variants,
# and prints the shield (if given) or otherwise the board name.
[group('build & draw')]
[doc('list build targets')]
list:
    @just build_matrix={{build_matrix}} _parse_targets all \
        | sed 's|[@/][^,]*,|,|' \
        | sed 's|\([^,]*\),\([^,]\+\),.*|\2|' \
        | sed 's|\([^,]*\),,.*|\1|' \
        | sort \
        | column

# build firmware for targets matching <expr>
[group('build & draw')]
build expr *west_args:
    #!/usr/bin/env bash
    set -euo pipefail
    targets=$(just build_matrix={{build_matrix}} _parse_targets {{ expr }})

    [[ -z $targets ]] && echo "No matching targets found. Aborting..." >&2 && exit 1
    echo "$targets" | while IFS=, read -r board shield snippet artifact cmake_args; do
        just _build_single "$board" "$shield" "$snippet" "$artifact" "$cmake_args" {{ west_args }}
    done

# flash firmware for targets matching <expr>
[group('build & draw')]
flash expr: (build expr)
    #!/usr/bin/env bash
    set -euo pipefail
    targets=$(just build_matrix={{build_matrix}} _parse_targets {{ expr }})

    [[ -z $targets ]] && echo "No matching targets found. Aborting..." >&2 && exit 1
    echo "$targets" | while IFS=, read -r board shield snippet artifact cmake_args; do
        just _flash_single "$board" "$shield" "$artifact"
    done

# fail if the generated chords, the drawing or the practice drifted from the keymap
check-keymap:
    python3 draw/gen_symbols.py --check
    python3 -m unittest tests.test_chord_consistency

# the keymap as a self-contained HTML page (layers, chords by family, search)
[group('build & draw')]
keymap-html:
    python3 "{{ draw }}/make_keymap_html.py"
    xdg-open "{{ draw }}/twonr9_keymap.html"

# the keymap as an SVG, layer by layer, without the chord overlay
[group('build & draw')]
keymap-svg:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{ draw }}"
    keymap="$(command -v keymap || echo "$HOME/Projects/layer-hud-niri/.venv/bin/keymap")"
    tmp="$(mktemp -t twonr9-layers.XXXXXX.yaml)"
    python3 -c "import sys, yaml; d = yaml.safe_load(open('twonr9_srht.yaml')); d.pop('combos', None); d['layers'] = {n: k for n, k in d['layers'].items() if not all((x if isinstance(x, dict) else {'t': str(x)}).get('t') == '▽' for x in k)}; yaml.safe_dump(d, open(sys.argv[1], 'w'), sort_keys=False, allow_unicode=True)" "$tmp"
    "$keymap" -c twonr9_config.yaml draw "$tmp" -o twonr9_srht_current.svg
    rm -f "$tmp"
    xdg-open twonr9_srht_current.svg

# LEGACY: the old morph-era generator (pre-dates the chord layout; bugwind only)
# parse & plot twonr9 keymap
# no args: the default (bugwind) variant only; pass "srht" or "all" for others
[group('build & draw')]
draw-twonr9 *variants:
    #!/usr/bin/env bash
    set -euo pipefail
    python3 "{{ draw }}/draw_twonr9.py" {{ variants }}

# Check generated drawings against the current keymaps without modifying files.
[group('build & draw')]
draw-check *variants:
    #!/usr/bin/env bash
    set -euo pipefail
    python3 "{{ draw }}/draw_twonr9.py" --check {{ variants }}

# initialize the west workspace
[group('workspace')]
init:
    west init -l config
    west update --fetch-opt=--filter=blob:none
    west zephyr-export

# synchronize the west workspace (after manifest changes)
[group('workspace')]
sync:
    west update --fetch-opt=--filter=blob:none

# bump west manifest and re-sync the workspace
[group('workspace')]
bump-west: && sync
    pin-west bump

# bump nix toolchain (flake.lock)
[group('workspace')]
bump-nix:
    nix flake update --flake .

# clear build cache and artifacts
[group('cleanup')]
clean:
    rm -rf {{ build }} {{ out }}

# garbage-collect the nix store (system-wide)
[group('cleanup')]
nix-gc:
    nix-collect-garbage --delete-old

# format devicetree files, or a single directory recursively
[group('dev')]
[no-cd]
format *paths:
    #!/usr/bin/env bash
    set -euo pipefail
    paths=({{ paths }})

    if [[ ${#paths[@]} -eq 0 ]]; then
        echo "Usage: just format <file>... | <dir>" >&2
        exit 1
    fi

    for path in "${paths[@]}"; do
        if [[ -d "$path" ]]; then
            if [[ ${#paths[@]} -gt 1 ]]; then
                echo "A directory must be the only argument. Aborting..." >&2
                exit 1
            fi
            cd "$path"
            dts-format --fix
            exit 0
        fi
    done

    dts-format --fix "${paths[@]}"

# run test suites (--auto-accept updates the snapshot)
[group('dev')]
[no-cd]
test $testpath *FLAGS:
    #!/usr/bin/env bash
    set -euo pipefail
    testcase=$(basename "$testpath")
    build_dir="{{ build / "tests" / '$testcase' }}"
    config_dir=$(realpath "$testpath")
    cd {{ justfile_directory() }}

    if [[ "{{ FLAGS }}" != *"--no-build"* ]]; then
        echo "Running $testcase..."
        rm -rf "$build_dir"
        west build -s zmk/app -d "$build_dir" -b native_sim//zmk_test_mock -- \
            -DCONFIG_ASSERT=y -DZMK_CONFIG="$config_dir"
    fi

    ${build_dir}/zephyr/zmk.exe | sed -e "s/.*> //" |
        tee ${build_dir}/keycode_events.full.log |
        sed -n -f ${config_dir}/events.patterns > ${build_dir}/keycode_events.log
    if [[ "{{ FLAGS }}" == *"--verbose"* ]]; then
        cat ${build_dir}/keycode_events.log
    fi

    if [[ "{{ FLAGS }}" == *"--auto-accept"* ]]; then
        cp ${build_dir}/keycode_events.log ${config_dir}/keycode_events.snapshot
    fi
    diff -auZ ${config_dir}/keycode_events.snapshot ${build_dir}/keycode_events.log

# warn user if they are using golang-yq and not python-yq
[no-exit-message]
_check_yq_version:
    #!/usr/bin/env bash
    if yq --help 2>&1 | grep -qi 'eval'; then
        echo "This script requires python-yq, but PATH contains golang-yq" >&2
        echo "Please install python-yq or use the included nix shell" >&2
        exit 1
    fi

# start the layout trainer web app
[group('trainer')]
[doc('start layout trainer web app')]
trainer:
    cd trainer && npm run dev

