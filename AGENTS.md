# Customization guide

Instructions for working on this ZMK config — written for coding agents, but equally usable by
humans adapting this repo. For background on the keymap and the build pipeline, see the
[README](README.md).

## Ground rules

- **Building needs no local setup.** Pushing builds every target in `build.yaml` through
  GitHub Actions (`.github/workflows/build-nix.yml`); the firmware is downloaded from the
  Actions tab. A fresh fork has Actions disabled — enable them once from the fork's Actions tab.
- **Building locally** requires the nix-based dev environment (nix + direnv, see the
  [README](README.md#local-build-environment)) plus a one-time `just init`, which turns the
  repository into a west workspace by pulling in ZMK, Zephyr and the modules. Then verify keymap
  changes with `just build <target>` (`just list` shows valid targets, `just build all` builds
  everything); compiled firmware lands in `firmware/`. If `just` or `west` are missing, the
  environment isn't active — run commands through `nix develop --command <cmd>` or activate with
  `direnv allow`.
- `config/west.yml` is maintained by [pin-west](https://github.com/urob/pin-west): never hand-edit
  pinned revisions, run `pin-west bump` instead. Adding or removing a module is fine — edit the
  entry itself and re-run `pin-west pin` to (re)pin.
- `dts-format` (packaged in the dev environment) formats devicetree files. It does not reformat
  C-preprocessor macros, so on the keymaps it is close to a no-op — the hand-aligned grids inside
  `ZMK_LAYER` are safe and need no guarding. It earns its keep on plain devicetree, i.e. when
  developing modules or board definitions. Without arguments it recurses over the working
  directory; pass files explicitly to narrow it.
- After keymap changes that affect the layout, regenerate the diagrams with
  `just draw-twonr9 all` (renders the TwoNr9 overviews into `draw/`).
- `just test` is a snapshot-test harness for developing the ZMK **modules** checked out under
  `modules/zmk/`. It does not test this repo's keymap; the keymap is validated by building.

## The TwoNr9 (this repo's keyboard)

The TwoNr9 is an 18-key split. Its hardware is defined **once**, in
`config/boards/shields/twonr9/`, built by the `twonr9_left` / `twonr9_right` shields (ZMK resolves
`config/twonr9.keymap` by shield name, so `just build` and CI need no `cmake-args`):

| Target | Firmware |
| --- | --- |
| `twonr9_left` | left half, no serial signal |
| `twonr9_left_with_snippets` | left half with `layer-hud-usb-uart` — **the one to flash** |
| `twonr9_right` | right half |
| `settings_reset` | reset |

There is a **second physical build of the same board, smol2nr9** (`smol2nr9_left` /
`smol2nr9_right`), wired to different pins. It reuses everything: `config/smol2nr9.keymap` includes
`twonr9.keymap`, `config/smol2nr9.conf` mirrors `twonr9.conf`, and
`config/boards/shields/smol2nr9/smol2nr9.dtsi` includes `../twonr9/twonr9.dtsi` for the matrix
transform and physical layout. Only the kscan pin lists in `smol2nr9_left.overlay` /
`smol2nr9_right.overlay` are different (taken from the Shield Wizard output). Both boards also get
a `*_left_with_snippets` target.

```bash
just build all        # both boards (left + HUD variant + right) and settings_reset -- what CI builds
just build smol       # only the smol2nr9 targets
just keymap-html      # the interactive keymap page
just keymap-svg       # every layer as an SVG
```

**When editing the keymap**, these are the files that matter:

| Change | File(s) |
| --- | --- |
| Alpha grids, HRM holds, thumbs | `config/twonr9.keymap` |
| Shared behaviors (magic shift, thumbs, smart layers) | `config/twonr9_keys.h` |
| Bigram chords / their macro bodies | `config/twonr9_combos_srht.dtsi` / `config/twonr9_macros_srht.dtsi` |
| Coding & utility combos | `config/twonr9_combos.dtsi` |
| Symbol chords (all eight states) | `draw/gen_symbols.py` → `config/twonr9_symbol_chords.dtsi` + the drawing |
| German keycodes, umlaut chords | `config/keys_de.h`, `config/symbol_work.dtsi` |
| Adaptive swap rules | `config/twonr9_adaptive_keys_srht.h` (generators: `config/twonr9_adaptive.h`) |
| Physical grid, split/BT settings, keyboard name | `config/boards/shields/twonr9/` |
| smol2nr9 pin wiring (same keymap/layout) | `config/boards/shields/smol2nr9/*.overlay` |
| Hardware/power settings (both boards) | `config/twonr9.conf` **and** `config/smol2nr9.conf` |
| Build targets | `build.yaml` |

The `_srht` suffix on a few files names the layout family, not a second variant — there is one
keymap.

Traps worth knowing:

- **Never edit the chords by hand.** `draw/gen_symbols.py` owns the symbol table and the non-symbol
  chord list, and writes both the dtsi and every chord entry in the drawing; `just check-keymap`
  fails when the firmware, the drawing or the practice drift apart. Only the layer pictures in
  `draw/twonr9_srht.yaml` are still hand-written.
- **Keep the adaptive set deliberate.** Nine swaps are active (`u oi`, `y us`, plus the srht seven);
  adding one costs a chord-path risk and should come with a reason.
- **The drawing and the page are generated.** `just keymap-svg` and `just keymap-html` read
  `draw/twonr9_srht.yaml`; the legacy `draw_twonr9.py` still draws the retired morph model, so
  `just draw-twonr9` is not a source of truth.

## Where to change what

| Change | File |
| --- | --- |
| Layers, HRMs, thumb keys | `config/twonr9.keymap` |
| Shared behaviors (magic shift, morphs, smart layers) | `config/twonr9_keys.h` |
| Combos (layout / shared) | `config/twonr9_combos_srht.dtsi` / `config/twonr9_combos.dtsi` |
| Board settings (BT, sleep, power) | `config/twonr9.conf` |
| Build targets | `build.yaml` |
| ZMK/module versions | `config/west.yml` (via `pin-west bump` only) |
| Dev environment | `flake.nix`, `nix/` (test with `nix develop`) |

Removing a feature: delete its `#include` from the keymap (and its bindings/combo references),
and if it was the only consumer of a module, drop the module's entry from `config/west.yml`. The
modules used per feature are commented at the top of the keymap.
