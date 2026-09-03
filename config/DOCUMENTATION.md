# TwoNr9 Keyboard & Urob ZMK Workspace Technical Guide

Comprehensive technical documentation for the **TwoNr9 (18-Key Split)** keyboard integrated into the **Urob ZMK Workspace**.

> ⚡ **Quick Reference & Visual Infographic:** View [`CHEATSHEET.md`](../CHEATSHEET.md) or [`draw/twonr9_cheatsheet.svg`](../draw/twonr9_cheatsheet.svg) for an all-in-one visual layout and combo usability reference.

---

## Table of Contents
1. [Executive Summary & Setup Overview](#1-executive-summary--setup-overview)
2. [Retroactive Log of All Changes & Technical Reasoning](#2-retroactive-log-of-all-changes--technical-reasoning)
3. [The Power of Urob's ZMK Architecture](#3-the-power-of-urobs-zmk-architecture)
4. [Advanced Behaviors & Smart Engine](#4-advanced-behaviors--smart-engine)
5. [TwoNr9 Keymap & Layer Reference](#5-twonr9-keymap--layer-reference)
6. [Hardware, Shields & Build Targets](#6-hardware-shields--build-targets)
7. [Step-by-Step User Workflow](#7-step-by-step-user-workflow)
8. [External References & Useful Links](#8-external-references--useful-links)

---

## 1. Executive Summary & Setup Overview

Your TwoNr9 keyboard configuration is fully integrated into a nix-managed ZMK devicetree workspace.

### Key Capabilities Enabled:
* **Hardware Model v2**: Targets `nice_nano@2.0.0//zmk` on Zephyr 4.1.
* **German Layout Integration**: Native `keys_de.h` keycodes with correct German modifier handling.
* **Ergonomic Homerow Mods (HRM)**: Positional triggers isolating left hand from right hand to eliminate typing roll misfires.
* **Dual GUI & Notification Support**:
  * **ZMK Studio**: Real-time on-keyboard layer/keymap remapping via USB RPC.
  * **KeyPeek**: Real-time active layer visualizer via `zmk-raw-hid` and `zmk-keypeek-layer-notifier`.
* **Symmetrical Adaptive Thumb Engine**:
  * Left Outer (14): `A2_DUAL` (Tap: single `a2`, Hold: continuous `a2` words like *BMW*, *Quiz*, *Pflanze*).
  * Left Inner (15): `SPC_NAV` (Tap: `Space` with sentence `. ` morph, Hold: `nav` layer).
  * Right Inner (16): `MAGIC_SHIFT` (Adaptive Repeat after letters, Sticky Shift on pause for German noun caps, Hold for continuous Shift).
  * Right Outer (17): `SMART_NUM` (Auto-terminating `num_word`).
* **Complete 14-Pair Mod-Morph Symbol System**: All brackets, quotes, slashes, and punctuation mapped without combo clutter.
* **Automated Visualizations**:
  * All 6 Layers detailed view: `draw/twonr9.svg`
  * Single-board unified overview with 4-corner layer sub-legends: `draw/twonr9_overview.svg`
  * Combined dual-alpha overview: `draw/twonr9_combined_overview.svg`
  * All-in-one visual infographic: `draw/twonr9_cheatsheet.svg`

---

## 2. Retroactive Log of All Changes & Technical Reasoning

### 1. Keymap Architecture & Modular Organization (`config/twonr9.keymap`)
* **Change**: Converted raw devicetree syntax to `zmk-helpers` macros (`ZMK_HOLD_TAP`, `ZMK_MACRO`, `ZMK_COMBO`, `ZMK_LAYER`, `ZMK_MOD_MORPH`, `ZMK_ADAPTIVE_KEY`).
  * *Reason*: `zmk-helpers` generates clean nodes, standardizes naming, and prevents syntax errors when chording modifiers.
* **Change**: Corrected `hold-trigger-key-positions` for `hml` and `hmr`.
  * *Reason*: In the new keymap, `hml` triggers exclusively on right-hand keys + thumbs (`KEYS_R THUMBS`), and `hmr` triggers on left-hand keys + thumbs (`KEYS_L THUMBS`), completely eliminating intra-hand typing roll misfires.
* **Change**: Defined `#define ALL 0 1 2 3 4 5`.
  * *Reason*: Allows universal coding combos (`⇥`, `⏎`, `⌫ / ⌦`, `⌃⌫`, `⎋`, `_`, `-`, `:`, `;`, `⇪`) to apply across all layers.
* **Change**: Extracted key definitions into modular components:
  * `config/twonr9_keys.h`: Parameterized function macros (`AL()`, `GL()`, `SL()`, `CL()`, `SR()`, `GR()`, `AR()`, `CR()`, `S1()`, `FN()`, `NM()`), `MAGIC_SHIFT`, `A2_DUAL`, `SPC_NAV`, and 14 mod-morph pairs.
  * `config/twonr9_macros.dtsi`: German bigram digraph macros.
  * `config/twonr9_combos.dtsi`: Categorized combo definitions.

### 2. Editor & LSP Integration for Helix (`.helix/languages.toml` & `flake.nix`)
* **Change**: Configured `.helix/languages.toml` with native `dts-lsp-server` for `.keymap`, `.dtsi`, and `.overlay` files, and `clangd` for C headers.
  * *Reason*: Packaged `dts-lsp-server` directly into the Nix development shell (`flake.nix`) for out-of-the-box autocomplete, hover documentation, and jump-to-definition in Helix.

### 3. Shield & Module Setup (`boards/shields/twonr9/` & `config/zephyr/module.yml`)
* **Change**: Added shield overlays, layout metadata, and Kconfigs into `boards/shields/twonr9/` and `config/boards/shields/twonr9/`.
* **Change**: Added `config/zephyr/module.yml` declaring `board_root: .`.
  * *Reason*: Under Zephyr Hardware Model v2, user configs must declare a module root so that ZMK and Zephyr discover custom shields both in local CLI builds and inside GitHub Actions CI containers without deprecation warnings.

### 4. Build Matrix & CI Configuration (`build.yaml`, `.github/workflows/build-nix.yml`, `.github/workflows/test-build-env.yml`)
* **Change**: Updated board target names to `nice_nano@2.0.0//zmk`.
* **Change**: Configured ZMK Studio target with snippet `studio-rpc-usb-uart` and raw HID adapter (`shield: twonr9_left raw_hid_adapter`).
* **Change**: Set `toolchain: zephyr-full` in `.github/workflows/build-nix.yml` for Protobuf compilation.
* **Change**: Updated `.github/workflows/test-build-env.yml` to target `just build twonr9_left` and `just draw-twonr9` (replacing legacy `planck` tests).

### 5. Automated Drawing System (`draw/draw_twonr9.py` & `draw/twonr9_config.yaml`)
* **Change**: Created custom parser and decoder script `draw/draw_twonr9.py`.
  * *Reason*: Standard `keymap-drawer` cannot natively parse raw HID usage numbers from localized headers like `keys_de.h`. The script translates all raw codes into clean German legends, unicode symbols, and hold-tap labels.
* **Change**: Added 2-column detailed layer layout (`draw/twonr9.svg`), single-board overview (`draw/twonr9_overview.svg`), combined dual-alpha diagram (`draw/twonr9_combined_overview.svg`), and visual infographic (`draw/twonr9_cheatsheet.svg`).

---

## 3. The Power of Urob's ZMK Architecture

Urob's configuration is widely recognized as the gold standard for minimal-key ergonomic keyboards. Key architectural concepts include:

### 1. "Timeless" Homerow Mod Tuning
* `flavor = "balanced"`: Activates as a hold only if another key is pressed and released while held.
* `require-prior-idle-ms = <150>`: Holds only trigger if you pause typing for 150ms before pressing the key. During fast typing streams, keys *always* output as letters even if fingers overlap.
* `hold-trigger-key-positions`: A left-hand modifier will *never* activate if you press another left-hand key.

### 2. Micro-Module Ecosystem
* `zmk-helpers`: Standardized key positions, hold-taps, morphs, and macros.
* `zmk-auto-layer`: Auto-terminating layers (`num_word`).
* `zmk-adaptive-key`: Dynamic context-aware keys (`magic_shift`, auto-repeat).
* `zmk-tri-state`: Conditional state toggles (`swapper`).

---

## 4. Advanced Behaviors & Smart Engine

### A. Adaptive `magic_shift` (`MAGIC_SHIFT`)
* **After typing a letter**: Acts immediately as **`&key_repeat`** (repeats the last character: *tt*, *ee*, *ll*, *ff*, *mm*, *ss* with zero delay).
* **After a pause / start of word**: Acts as **`&sk LSHFT` (Sticky Shift)** (arms Shift for German noun capitalization without holding).
* **Hold**: Acts as standard continuous **`&kp LSHFT`**.
* **Shift + Tap**: Activates **`&caps_word`**.

### B. Dual `a2` Thumb (`A2_DUAL`)
* **Tap**: **Sticky `a2`** (types 1 secondary alpha, then returns to base).
* **Hold**: **Momentary `a2`** (hold to type continuous secondary words like *BMW*, *Quiz*, *Pflanze*).

### C. Smart Sentence Space (`SPC_NAV`)
* **Tap**: Outputs `Space`.
* **Shift + Tap**: Outputs `. ` (period + space) and arms Sticky Shift for the next sentence.
* **Hold**: Activates momentary **`nav`** layer.

### D. Complete Mod-Morph Symbol System (14 Pairs on `sym`)
* `(` / `<` · `)` / `>` · `[` / `{` · `]` / `}`
* `;` / `'` · `:` / `"` · `/` / `\` · `_` / `-`
* `!` / `?` · `#` / `~` · `$` / `€` · `` ` `` / `^` · `&` / `@` · `|` / `=`

---

## 5. TwoNr9 Keymap & Layer Reference

### Physical Layout Matrix
```text
                     TwoNr9 KEY POSITIONS (18 Keys)

              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
              │  0   │  1   │  2   │      │  3   │  4   │  5   │
       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
       │  6   │  7   │  8   │  9   │      │  10  │  11  │  12  │  13  │
       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                     │  14  │  15  │      │  16  │  17  │
                     ╰──────┴──────╯      ╰──────┴──────╯
```

---

### Layer Overview

#### Layer 0: `a1` (Base QWERTZ Alphas)
```c
ZMK_LAYER(a1,
//              ╭────────┬────────┬────────╮      ╭────────┬────────┬────────╮
                  AL(DE_L) GL(DE_N) SL(DE_D)        SR(DE_Y) GR(DE_O) AR(DE_U)
//       ╭──────┼────────┼────────┼────────┤      ├────────┼────────┼────────┼──────╮
           CL(DE_S) FN(DE_R) NV(DE_H) S1(DE_T)      S1(DE_C) NV(DE_E) FN(DE_I) CR(DE_A)
//       ╰──────┴────────┼────────┼────────┤      ├────────┼────────┼────────┴──────╯
                         A2_DUAL   SPC_NAV          MAGIC_SHIFT SMART_NUM
//                     ╰─────────┴─────────╯      ╰───────────┴─────────╯
)
```

#### Layer 1: `a2` (Secondary Alphas)
```c
ZMK_LAYER(a2,
//              ╭────────┬────────┬────────╮      ╭────────┬────────┬────────╮
                  AL(DE_X) GL(DE_B) SL(DE_M)        SR(DE_W) GR(DE_Q) AR(DE_COMMA)
//       ╭──────┼────────┼────────┼────────┤      ├────────┼────────┼────────┼──────╮
           CL(DE_F) FN(DE_V) NV(DE_P) S1(DE_K)      S1(DE_G) NV(DE_J) FN(DE_DOT) CR(DE_Z)
//       ╰──────┴────────┼────────┼────────┤      ├────────┼────────┼────────┴──────╯
                         &to L_A1  SPC_NAV          MAGIC_SHIFT SMART_NUM
//                     ╰─────────┴─────────╯      ╰───────────┴─────────╯
)
```

#### Layer 2: `nav` (Navigation & Niri Suite)
```c
ZMK_LAYER(nav,
//              ╭────────┬────────┬────────╮      ╭────────┬────────┬────────╮
                  &sk LALT &sk LGUI &sk LSHFT       NAV_LEFT &kp DOWN &kp UP
//       ╭──────┼────────┼────────┼────────┤      ├────────┼────────┼────────┼────────╮
           &sk LCTRL &kp LG(DE_Q) &kp LG(TAB) NAV_BSPC &swapper &kp PG_DN &kp PG_UP NAV_RIGHT
//       ╰──────┴────────┼────────┼────────┤      ├────────┼────────┼────────┴────────╯
                         ___       &to L_A1         MAGIC_SHIFT SMART_NUM
//                     ╰─────────┴─────────╯      ╰───────────┴─────────╯
)
```

#### Layer 3: `sym` (Morphing Brackets & Symbols)
```c
ZMK_LAYER(sym,
//              ╭───────────┬───────────┬───────────╮      ╭────────┬────────┬────────────╮
                  &excl_qmark &hash_tilde &dllr_euro         &lpar_lt &rpar_gt &semi_sqt
//       ╭──────┼───────────┼───────────┼───────────┤      ├────────┼────────┼────────────┼──────────╮
            &grave_caret &under_minus &amps_at &pipe_equal  &lbkt_lbrc &rbkt_rbrc &colon_dqt &fslh_bslh
//       ╰──────┴───────────┼───────────┼───────────┤      ├────────┼────────┼────────────┴──────────╯
                            ___         &to L_A1           MAGIC_SHIFT SMART_NUM
//                        ╰───────────┴───────────╯      ╰───────────┴─────────╯
)
```

#### Layer 4: `fn` (Function Keys & Media Controls)
```c
ZMK_LAYER(fn,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  &kp F1 &kp F2 &kp F3        &kp F8 &kp F9 &kp F10
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           &kp F4 &kp F5 &kp F6 &kp F7        &kp F11 &kp F12 &kp C_VOL_DN &kp C_VOL_UP
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         ___    &to L_A1      MAGIC_SHIFT SMART_NUM
//                     ╰──────┴──────╯      ╰───────────┴─────────╯
)
```

#### Layer 5: `num` (3x3 Calculator Numpad & Math)
```c
ZMK_LAYER(num,
//              ╭────────────┬────────────┬────────────╮      ╭────────┬────────┬────────╮
                  &kp DE_MINUS &kp DE_ASTRK &kp DE_EQUAL        &kp DE_N4 &kp DE_N5 &kp DE_N6
//       ╭──────┼────────────┼────────────┼────────────┤      ├────────┼────────┼────────┼──────╮
           &kp DE_PLUS &kp DE_PRCNT &kp DE_FSLH &kp DE_DOT      &kp DE_N1 &kp DE_N2 &kp DE_N3 &kp DE_N0
//       ╰──────┴────────────┼────────────┼────────────┤      ├────────┼────────┼────────┴──────╯
                             ___          &to L_A1            MAGIC_SHIFT SMART_NUM
//                         ╰────────────┴────────────╯        ╰───────────┴─────────╯
)
```

---

## 6. Hardware, Shields & Build Targets

### Build Target Matrix (`build.yaml`)
```yaml
include:
  - board: nice_nano@2.0.0//zmk
    shield: twonr9_left

  - board: nice_nano@2.0.0//zmk
    shield: twonr9_left raw_hid_adapter
    snippet: studio-rpc-usb-uart
    cmake-args: -DCONFIG_ZMK_STUDIO=y
    artifact-name: twonr9_left_with_studio

  - board: nice_nano@2.0.0//zmk
    shield: twonr9_right

  - board: nice_nano@2.0.0//zmk
    shield: settings_reset
```

### Generated Firmware Artifacts (`firmware/`)
1. **`twonr9_left_with_studio.uf2`**: Central (Left) half with ZMK Studio RPC and KeyPeek Raw HID streaming.
2. **`twonr9_left-nice_nano@2.0.0__zmk.uf2`**: Central (Left) half (standard lightweight build).
3. **`twonr9_right-nice_nano@2.0.0__zmk.uf2`**: Peripheral (Right) half.
4. **`settings_reset-nice_nano@2.0.0__zmk.uf2`**: Diagnostic firmware to clear corrupted BLE bond storage.

---

## 7. Step-by-Step User Workflow

### A. Flashing the Keyboard
1. **Left Half (Central)**:
   * Double-press the physical reset button on the left nice!nano.
   * Drag & drop `firmware/twonr9_left_with_studio.uf2` onto the `NICENANO` USB drive.
2. **Right Half (Peripheral)**:
   * Double-press the physical reset button on the right nice!nano.
   * Drag & drop `firmware/twonr9_right-nice_nano@2.0.0__zmk.uf2` onto the `NICENANO` drive.

### B. Daily Development Commands

```bash
# 1. Generate all visual keymap diagrams & cheatsheet infographic
just draw-twonr9

# 2. Build all TwoNr9 firmware targets
just build all

# 3. Build only the central half with Studio + KeyPeek
just build twonr9_left_with_studio

# 4. Check west dependencies integrity
pin-west check
```

---

## 8. External References & Useful Links

* **Urob ZMK Config**: [https://github.com/urob/zmk-config](https://github.com/urob/zmk-config)
* **ZMK Helpers**: [https://github.com/urob/zmk-helpers](https://github.com/urob/zmk-helpers)
* **ZMK Official Documentation**: [https://zmk.dev/docs](https://zmk.dev/docs)
* **ZMK Studio Features**: [https://zmk.dev/docs/features/studio](https://zmk.dev/docs/features/studio)
* **KeyPeek Layer Notifier**: [https://github.com/srwi/keypeek](https://github.com/srwi/keypeek)
* **Pin-West Tool**: [https://github.com/urob/pin-west](https://github.com/urob/pin-west)
* **Keymap-Drawer**: [https://github.com/caksoylar/keymap-drawer](https://github.com/caksoylar/keymap-drawer)
