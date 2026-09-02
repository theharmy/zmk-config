# TwoNr9 Keyboard & Urob ZMK Workspace Technical Guide

Comprehensive documentation for your **TwoNr9 (18-Key Split)** keyboard integrated into the **Urob ZMK Workspace**.

---

## Table of Contents
1. [Executive Summary & Setup Overview](#1-executive-summary--setup-overview)
2. [What Changed & Architecture Comparison](#2-what-changed--architecture-comparison)
3. [The Power of Urob's ZMK Architecture](#3-the-power-of-urobs-zmk-architecture)
4. [Advanced Features You Can Adapt to TwoNr9](#4-advanced-features-you-can-adapt-to-twonr9)
5. [TwoNr9 Keymap & Layer Reference](#5-twonr9-keymap--layer-reference)
6. [Hardware, Shields & Build Targets](#6-hardware-shields--build-targets)
7. [Step-by-Step User Workflow (Flashing & Customization)](#7-step-by-step-user-workflow)

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
* **Automated Visualization**: 2-column keymap diagram generator (`just draw-twonr9` $\rightarrow$ `draw/twonr9.svg`).

---

## 2. What Changed & Architecture Comparison

| Area | Old Setup (`zmk-config-twonr9-`) | New Setup (`zmk-workspace`) | Benefit |
| :--- | :--- | :--- | :--- |
| **Dev Environment** | Standalone repo, unpinned modules | Nix devshell + `Justfile` + `pin-west` | 100% reproducible builds locally & in CI |
| **Keymap Syntax** | Raw, verbose Devicetree syntax | `zmk-helpers` macros + compact 4–6 char tokens | Clean, readable, hand-aligned ASCII grid |
| **HRM Triggers** | Out-of-bounds positions (`18`, `19`), mixed hands | Exact hand isolation (`KEYS_R THUMBS` & `KEYS_L THUMBS`) | Zero false mod activations during rolls |
| **ZMK Studio** | Deprecated experimental shield | Modern USB-UART RPC snippet (`studio-rpc-usb-uart`) | Seamless connection with official ZMK Studio |
| **KeyPeek Support** | Module unpinned, manual setup | Pinned `zmk-raw-hid` + `zmk-keypeek-layer-notifier` | Layer changes stream directly to desktop UI |
| **Diagrams** | Generic or manual SVG | Automated `keymap-drawer` 2-column rendering | High-res Gruvbox SVG with decoded German keys |

---

## 3. The Power of Urob's ZMK Architecture

Urob's configuration is widely recognized as the gold standard for minimal-key ergonomic keyboards (34-key, 18-key, etc.). Here is why it stands out:

### 1. "Timeless" Homerow Mod Tuning
Standard hold-taps rely purely on `tapping-term-ms`, causing misfires if you type too fast or delays if you hold too long. Urob's configuration uses:
* `flavor = "balanced"`: Key activates as a hold if another key is pressed and released while held.
* `require-prior-idle-ms = <150>`: Holds only trigger if you pause typing for 150ms before pressing the key. During fast typing streams, keys *always* output as letters even if fingers overlap.
* `hold-trigger-key-positions`: A left-hand modifier will *never* activate if you press another left-hand key, completely eliminating intra-hand typing roll errors.

### 2. Micro-Module Ecosystem
Instead of a single monolithic fork, features are isolated into clean, maintained upstream ZMK modules:
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

You can easily pull in any of Urob's advanced behaviors from `config/base.keymap` into your `twonr9.keymap`:

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

### Key Shorthand Reference:
* `al_*` (Left Alt) | `gl_*` (Left Gui) | `sl_*` (Left Shift) | `cl_*` (Left Ctrl)
* `ar_*` (Right Alt) | `gr_*` (Right Gui) | `sr_*` (Right Shift) | `cr_*` (Right Ctrl)
* `s1_*` (Sym Layer 3) | `s2_*` (Sym2 Layer 4) | `num_*` (Num Layer 5)
* `sl_NAV` (Sticky Nav) | `sl_A2` (Sticky a2) | `spc_SFT` (Space/Shift) | `sl_NUM` (Sticky Num) | `to_BASE` (To Layer 0)

---

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
just build twonr9

# 3. Build only the central half with Studio + KeyPeek
just build twonr9_left_with_studio

# 4. Generate the visual keymap diagram (draw/twonr9.svg)
just draw-twonr9

# 5. Check dependencies integrity
pin-west check

# 6. Format devicetree / C headers
just format config/twonr9.keymap
```

### C. Where to Make Changes

* **Keybindings, Layers, Combos**: Edit `config/twonr9.keymap`.
* **Hardware Timers, Bluetooth Power, Sleep**: Edit `config/twonr9.conf`.
* **Pin Assignments / GPIO Wiring**: Edit `boards/shields/twonr9/twonr9_left.overlay` or `twonr9_right.overlay`.
* **Visual Diagram Styling**: Edit `draw/twonr9_config.yaml`.
