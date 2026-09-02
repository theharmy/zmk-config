# TwoNr9 Keyboard & Urob ZMK Workspace Technical Guide

Comprehensive documentation for your **TwoNr9 (18-Key Split)** keyboard integrated into the **Urob ZMK Workspace**.

---

## Table of Contents
1. [Executive Summary & Setup Overview](#1-executive-summary--setup-overview)
2. [Retroactive Log of All Changes & Technical Reasoning](#2-retroactive-log-of-all-changes--technical-reasoning)
3. [The Power of Urob's ZMK Architecture](#3-the-power-of-urobs-zmk-architecture)
4. [Advanced Features You Can Adapt to TwoNr9](#4-advanced-features-you-can-adapt-to-twonr9)
5. [TwoNr9 Keymap & Layer Reference](#5-twonr9-keymap--layer-reference)
6. [Hardware, Shields & Build Targets](#6-hardware-shields--build-targets)
7. [Step-by-Step User Workflow (Flashing & Customization)](#7-step-by-step-user-workflow)
8. [External References & Useful Links](#8-external-references--useful-links)

---

## 1. Executive Summary & Setup Overview

Your TwoNr9 keyboard configuration is fully integrated into a nix-managed ZMK devicetree workspace.

### Key Capabilities Now Enabled:
* **Hardware Model v2**: Targets `nice_nano@2.0.0//zmk` on Zephyr 4.1.
* **German Layout Integration**: Native `keys_de.h` keycodes with correct German modifier handling.
* **Ergonomic Homerow Mods (HRM)**: Positional triggers isolating left hand from right hand to eliminate typing roll misfires.
* **Dual GUI & Notification Support**:
  * **ZMK Studio**: Real-time on-keyboard layer/keymap remapping via USB RPC.
  * **KeyPeek**: Real-time active layer visualizer via `zmk-raw-hid` and `zmk-keypeek-layer-notifier`.
* **Automated Visualizations**:
  * All 6 Layers detailed view: `draw/twonr9.svg`
  * Single-board unified overview with 4-corner layer sub-legends: `draw/twonr9_overview.svg`

---

## 2. Retroactive Log of All Changes & Technical Reasoning

Below is an exhaustive log of every change made across the workspace, including the technical reasons and upstream references.

### 1. Keymap Architecture (`config/twonr9.keymap`)
* **Change**: Converted raw devicetree syntax to `zmk-helpers` macros (`ZMK_HOLD_TAP`, `ZMK_MACRO`, `ZMK_COMBO`, `ZMK_LAYER`).
  * *Reason*: `zmk-helpers` generates clean nodes, standardizes naming, and prevents syntax errors when chording modifiers.
* **Change**: Corrected `hold-trigger-key-positions` for `hml` and `hmr`.
  * *Reason*: The old configuration contained out-of-bounds indices (`18`, `19`) and mixed left/right fingers in the same trigger list. In the new keymap, `hml` triggers exclusively on right-hand keys + thumbs (`KEYS_R THUMBS`), and `hmr` triggers on left-hand keys + thumbs (`KEYS_L THUMBS`).
  * *Reference*: [ZMK Positional Hold-Tap Documentation](https://zmk.dev/docs/behaviors/hold-tap#positional-hold-tap-and-hold-trigger-key-positions)
* **Change**: Defined `#define ALL 0 1 2 3 4 5`.
  * *Reason*: In C preprocessors, `ALL` was undefined, causing devicetree syntax parse errors. Defining `ALL` allows multi-layer combos (`Tab`, `Enter`, `Esc`, `Bspc`, `Ctrl+Bspc`, `Minus`, `Shift repeat`) to apply across all 6 layers.
* **Change**: Introduced compact 4–6 character token shorthands (`al_*`, `gl_*`, `sl_*`, `cl_*`, `s1_*`, `s2_*`, `num_*`, `sl_NAV`, `spc_SFT`, etc.).
  * *Reason*: Replaces sprawling line definitions with a clean, hand-aligned ASCII box art grid that matches physical key placements.

### 2. Shield & Module Setup (`boards/shields/twonr9/` & `config/zephyr/module.yml`)
* **Change**: Added shield overlays, layout metadata, and Kconfigs into `boards/shields/twonr9/` and `config/boards/shields/twonr9/`.
* **Change**: Added `config/zephyr/module.yml` declaring `board_root: .`.
  * *Reason*: Under Zephyr Hardware Model v2, user configs must declare a module root so that ZMK and Zephyr discover custom shields both in local CLI builds and inside GitHub Actions CI containers without throwing deprecation warnings.
  * *Reference*: [ZMK New Shield Integration Guide](https://zmk.dev/docs/hardware-integration/new-shield)

### 3. Build Matrix & CI Configuration (`build.yaml` & `.github/workflows/build-nix.yml`)
* **Change**: Updated board target names from `nice_nano_v2` to `nice_nano@2.0.0//zmk`.
  * *Reason*: Conforms to ZMK's modern hardware qualifier syntax (`<board>@<revision>//zmk`).
* **Change**: Removed unused sample keyboards (Planck, Corne-ish Zen, Glove80) from `build.yaml` and deleted their config files from `config/`.
  * *Reason*: Keeps the build matrix dedicated exclusively to TwoNr9 and reduces GitHub Actions build time.
* **Change**: Configured ZMK Studio target with snippet `studio-rpc-usb-uart` and raw HID adapter (`shield: twonr9_left raw_hid_adapter`).
  * *Reason*: Enables native ZMK Studio RPC over USB UART while simultaneously streaming layer notifications over raw HID for KeyPeek.
* **Change**: Set `toolchain: zephyr-full` in `.github/workflows/build-nix.yml`.
  * *Reason*: ZMK Studio RPC requires Protobuf compilers (`nanopb_generator.py` and `grpcio-tools`), which are packaged inside `zephyr-full`.

### 4. Dependency Locking (`config/west.yml` & `flake.nix`)
* **Change**: Added `zzeneg/zmk-raw-hid` and `srwi/zmk-keypeek-layer-notifier` to `config/west.yml` and pinned them with `pin-west`.
  * *Reason*: Required for KeyPeek desktop layer visualization.
* **Change**: Added `nanopb` to the Zephyr module allowlist in `config/west.yml`.
  * *Reason*: ZMK Studio RPC uses Google Protobuf serialization via Nanopb to communicate with the ZMK Studio GUI.
* **Change**: Added Python `protobuf` and `grpcio-tools` to `flake.nix`.
  * *Reason*: Allows the local Nix environment to compile Protobuf definitions during local `just build` runs.

### 5. Automated Drawing System (`draw/draw_twonr9.py` & `draw/twonr9_config.yaml`)
* **Change**: Created custom parser and decoder script `draw/draw_twonr9.py`.
  * *Reason*: Standard `keymap-drawer` cannot natively parse raw HID usage numbers from localized headers like `keys_de.h`. The script translates all raw codes into clean German legends and hold-tap labels.
* **Change**: Added 2-column layer layout (`draw/twonr9.svg`) and single-board overview diagram (`draw/twonr9_overview.svg`).
  * *Reason*: Produces high-resolution, Gruvbox-themed SVGs with zero text collisions and 4-corner multi-layer legends matching Urob's style.

---

## 3. The Power of Urob's ZMK Architecture

Urob's configuration is widely recognized as the gold standard for minimal-key ergonomic keyboards. Key architectural concepts include:

### 1. "Timeless" Homerow Mod Tuning
Standard hold-taps rely purely on `tapping-term-ms`, causing misfires if you type too fast or delays if you hold too long. Urob's configuration uses:
* `flavor = "balanced"`: Activates as a hold only if another key is pressed and released while held.
* `require-prior-idle-ms = <150>`: Holds only trigger if you pause typing for 150ms before pressing the key. During fast typing streams, keys *always* output as letters even if fingers overlap.
* `hold-trigger-key-positions`: A left-hand modifier will *never* activate if you press another left-hand key, completely eliminating intra-hand typing roll errors.

### 2. Micro-Module Ecosystem
Features are isolated into clean upstream ZMK modules:
* `zmk-helpers`: Standardized key positions, hold-taps, morphs, and macros.
* `zmk-auto-layer`: Auto-terminating layers (like `num_word`).
* `zmk-adaptive-key`: Dynamic context-aware keys (auto-repeat, intelligent shifting).
* `zmk-tri-state`: Conditional state toggles (`smart_mouse`, `swapper`).
* `zmk-leader-key`: Sequences of keystrokes triggering complex commands.
* `zmk-unicode`: Cross-platform unicode symbols.

### 3. Pin-West Deterministic Dependency Management
Standard ZMK configs track floating Git branches (`main`), which can break unexpectedly when dependencies update. `pin-west` locks every module and Zephyr dependency to exact commit SHAs. You can update safely at any time using:
```bash
just bump-west
```

---

## 4. Advanced Features You Can Adapt to TwoNr9

You can pull in any of Urob's advanced behaviors from `config/base.keymap` into your `twonr9.keymap`:

### A. Sentence Capitalization (`spc_morph`)
Makes Space automatically output a period + space + sticky shift when tapped with Shift held:
```c
// In config/twonr9.keymap:
ZMK_MACRO(dot_spc, bindings = <&kp DE_DOT &kp SPACE &sk LEFT_SHIFT>;)
ZMK_MOD_MORPH(spc_morph, bindings = <&kp SPACE>, <&dot_spc>; mods = <(MOD_LSFT|MOD_RSFT)>;)
```

### B. Auto-Terminating Number Mode (`num_word`)
Instead of locking or holding a number layer, `num_word` keeps the number layer active as long as you type numbers, math operators, or backspace, and automatically drops back to base when you press Space, Enter, or any other key.
```c
// Enable in twonr9.keymap:
#include <behaviors/num_word.dtsi>
// Use &num_word L_NUM on a thumb or combo!
```

### C. Magic Shift & Key Repeat (`magic_shift`)
Tapping shift after a letter repeats the previous letter (great for double letters like *tt*, *ll*, *ee*). Double-tapping shift activates Caps Word. Holding shift acts as standard Shift:
```c
#include <behaviors/adaptive_key.dtsi>
// Uses Urob's magic_shift behavior on thumb or combo
```

### D. Alt+Tab / App Swapper (`swapper`)
Press a single key to cycle through open windows (Alt+Tab). It holds Alt open until you press another key, giving you clean, one-key app switching:
```c
#include <behaviors/tri_state.dtsi>
ZMK_TRI_STATE(swapper, bindings = <&kt LALT>, <&kp TAB>, <&kt LALT>;)
```

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

### Layer Overview

#### Layer 0: `a1` (Base QWERTZ Alphas)
```c
ZMK_LAYER(a1,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  al_L   gl_N   sl_D          sr_Y   gr_O   ar_U
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           cl_S   s2_R   s1_H   num_T         num_C  s1_E   s2_I   cr_A
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         sl_NAV sl_A2         spc_SFT sl_NUM
//                     ╰──────┴──────╯      ╰──────┴──────╯
)
```

#### Layer 1: `a2` (Secondary Alphas)
```c
ZMK_LAYER(a2,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  al_X   gl_B   sl_M          sr_W   gr_Q   ar_CMA
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           cl_F   s2_V   s1_P   num_K         num_G  s1_J   s2_DOT cr_Z
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         ___    to_BASE       ___    ___
//                     ╰──────┴──────╯      ╰──────┴──────╯
)
```

#### Layer 2: `nav` (Navigation & Movement)
```c
ZMK_LAYER(nav,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  sk_ALT sk_GUI sk_SFT        sr_LFT gr_DWN ar_UP
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           sk_CTL ___    s1_PGUP ___          num_HOM s1_PGDN s2_END cr_RGT
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         ___    to_BASE       ___    ___
//                     ╰──────┴──────╯      ╰──────┴──────╯
)
```

#### Layer 3: `sym` (Primary Symbols & Enclosures)
```c
ZMK_LAYER(sym,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  al_EUR gl_HSH sl_DLR        sr_LT  gr_GT  ar_CRT
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           cl_GRV s2_UND s1_MIN num_AMP       num_LBK s1_RBK s2_PIP cr_SLH
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         ___    to_BASE       ___    ___
//                     ╰──────┴──────╯      ╰──────┴──────╯
)
```

#### Layer 4: `sym2` (Secondary Symbols & Punctuations)
```c
ZMK_LAYER(sym2,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  al_AT  gl_SQT sl_DQT        sr_LPR gr_RPR ar_CLN
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           cl_AST s2_TLD s1_EXC num_QMK       num_LBC s1_RBC s2_SMI cr_BSL
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         ___    to_BASE       ___    ___
//                     ╰──────┴──────╯      ╰──────┴──────╯
)
```

#### Layer 5: `num` (Numpad & Arithmetic)
```c
ZMK_LAYER(num,
//              ╭──────┬──────┬──────╮      ╭──────┬──────┬──────╮
                  al_MIN gl_AST sl_EQL        sr_N4  gr_N5  ar_N6
//       ╭──────┼──────┼──────┼──────┤      ├──────┼──────┼──────┼──────╮
           cl_PLS s2_PCT s1_PIP num_SLH       num_N1 s1_N2  s2_N3  cr_N0
//       ╰──────┴──────┼──────┼──────┤      ├──────┼──────┼──────┴──────╯
                         ___    to_BASE       ___    ___
//                     ╰──────┴──────╯      ╰──────┴──────╯
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
# 1. List available targets
just list

# 2. Build all TwoNr9 firmware
just build all

# 3. Build only the central half with Studio + KeyPeek
just build twonr9_left_with_studio

# 4. Generate both visual keymap diagrams (draw/twonr9.svg & draw/twonr9_overview.svg)
just draw-twonr9

# 5. Check dependencies integrity
pin-west check

# 6. Format devicetree / C headers
just format config/twonr9.keymap
```

---

## 8. External References & Useful Links

* **Urob ZMK Config**: [https://github.com/urob/zmk-config](https://github.com/urob/zmk-config)
* **ZMK Helpers**: [https://github.com/urob/zmk-helpers](https://github.com/urob/zmk-helpers)
* **ZMK Official Documentation**: [https://zmk.dev/docs](https://zmk.dev/docs)
* **ZMK Studio Features**: [https://zmk.dev/docs/features/studio](https://zmk.dev/docs/features/studio)
* **KeyPeek Layer Notifier**: [https://github.com/srwi/keypeek](https://github.com/srwi/keypeek)
* **ZMK Raw HID Module**: [https://github.com/zzeneg/zmk-raw-hid](https://github.com/zzeneg/zmk-raw-hid)
* **Pin-West Tool**: [https://github.com/urob/pin-west](https://github.com/urob/pin-west)
* **Keymap-Drawer**: [https://github.com/caksoylar/keymap-drawer](https://github.com/caksoylar/keymap-drawer)
