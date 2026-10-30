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
`config/boards/shields/twonr9/`; two thin shields wrap it and differ only in which keymap ZMK
resolves for them **by shield name** (so `just build` and CI need no `cmake-args`):

| Variant | Shield | Keymap | Config | Built by |
| --- | --- | --- | --- | --- |
| **bugwind** (default) | `twonr9_left` / `twonr9_right` | `config/twonr9.keymap` | `config/twonr9.conf` | `build.yaml` (CI) |
| **srht** (backup) | `twonr9_srht_left` / `twonr9_srht_right` | `config/twonr9_srht.keymap` | `config/twonr9_srht.conf` | `build-srht.yaml` |

```bash
just build all        # bugwind + settings_reset -- what CI builds
just build-srht       # the optional srht backup (overrides build_matrix)
just draw-twonr9      # diagrams for bugwind; pass `srht` or `all` for the other
```

**When editing a TwoNr9 keymap**, the rule is: keep the shared layers shared, and change only the
variant-specific files. `nav`, `sym`, `fn`, `num`, the thumb cluster and `config/twonr9_keys.h` are
common to both variants. What differs is the alpha grid, its bigram chords, and the adaptive-key
engine (srht only).

| Change | File(s) |
| --- | --- |
| Alpha grids, HRM holds, thumbs (bugwind) | `config/twonr9.keymap` |
| Alpha grids, HRM holds, thumbs (srht) | `config/twonr9_srht.keymap` |
| Behaviors shared by both (magic shift, morphs, thumbs) | `config/twonr9_keys.h` |
| Bigram chords (bugwind / srht) | `config/twonr9_combos_bugwind.dtsi` / `..._srht.dtsi` |
| Bigram macro bodies (e.g. `SCH`) | `config/twonr9_macros_bugwind.dtsi` / `..._srht.dtsi` |
| Coding & utility combos (shared) | `config/twonr9_combos.dtsi` |
| Adaptive swap rules (srht only) | `config/twonr9_adaptive_keys_srht.h` |
| Symbols, German keycodes | `config/keys_de.h` |
| Physical grid, split/BT settings, keyboard name | `config/boards/shields/twonr9/` (`*.dtsi`, `*.overlay`, `Kconfig.defconfig`) |
| Build targets | `build.yaml` (default) · `build-srht.yaml` (backup) |

Three traps worth knowing:

- **`.conf` files have no include mechanism in ZMK**, so `twonr9.conf` and `twonr9_srht.conf`
  duplicate the same hardware/power settings. Edit both, or the srht backup drifts silently.
- **Do not add adaptive keys to `bugwind`.** Its whole point is that every alpha is bound directly,
  so the grid is self-describing. Adaptive rules live in `twonr9_adaptive_keys_srht.h`, included
  only by the srht keymap.
- **After changing a keymap, regenerate the diagrams** with `just draw-twonr9 all`. The draw
  script's `VARIANTS` table (`draw/draw_twonr9.py`) mirrors the keymap's bigram lists and adaptive
  rules by hand — it does not read them out of the keymap, so it must be updated together with it.

## Where to change what

| Change | File |
| --- | --- |
| Layers, HRMs, thumb keys (per variant) | `config/twonr9.keymap` / `config/twonr9_srht.keymap` |
| Shared behaviors (magic shift, morphs, smart layers) | `config/twonr9_keys.h` |
| Combos (per variant / shared) | `config/twonr9_combos*.dtsi` |
| Board settings (BT, sleep, power) | `config/twonr9.conf` / `config/twonr9_srht.conf` |
| Build targets | `build.yaml` · `build-srht.yaml` |
| ZMK/module versions | `config/west.yml` (via `pin-west bump` only) |
| Dev environment | `flake.nix`, `nix/` (test with `nix develop`) |

Removing a feature: delete its `#include` from the keymap (and its bindings/combo references),
and if it was the only consumer of a module, drop the module's entry from `config/west.yml`. The
modules used per feature are commented at the top of the keymap.
