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
* **Row-Split Hold Model**: On both alpha layers, the **top row is layer-taps** (`fn` / `nav` / `sym`) and the **home row is modifiers** (`CTRL` / `ALT` / `GUI` / `SHIFT`), mirrored across the two halves. See [§5](#5-twonr9-keymap--layer-reference).
* **Dual GUI & Notification Support**:
  * **ZMK Studio**: Real-time on-keyboard layer/keymap remapping via USB RPC.
  * **KeyPeek**: Real-time active layer visualizer via `zmk-raw-hid` and `zmk-keypeek-layer-notifier`.
* **Adaptive Thumb Engine** (both alpha layers share the same thumb cluster):
  * Left Outer (14): `SMART_NUM` (Tap: `num_word`, Hold: momentary `num`).
  * Left Inner (15): `A2_DUAL` (Tap: single `a2`, Hold: continuous `a2` words like *BMW*, *Quiz*, *Pflanze*).
  * Right Inner (16): `SPC_NAV` (Tap: `Space` with sentence `. ` morph, Hold: `nav` layer).
  * Right Outer (17): `SYM_DUAL` (Tap: single `sym`, Hold: continuous `sym`).
  * *Note*: `MAGIC_SHIFT` is not on the thumbs — it is reached via the `shiftl` (8+9) and `shiftr` (10+11) combos on every layer.
* **Complete 14-Pair Mod-Morph Symbol System**: All brackets, quotes, slashes, and punctuation mapped without combo clutter.
* **Nine Adaptive Keys**: Context-aware bigram-swap keys (eliminate same-finger rolls like `rhl`, `uo`, `qi`) wired through their own hold-taps. See [§4.E](#e-adaptive-key-swaps--symbol-auto-repeat) and [`config/twonr9_adaptive_keys.h`](twonr9_adaptive_keys.h).
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
  * `config/twonr9_keys.h`: Mod-morph pairs, nav long-taps, `MAGIC_SHIFT`, `A2_DUAL`/`SYM_DUAL`, `SPC_NAV`, `SMART_NUM`, `swapper`.
  * `config/twonr9_adaptive_keys.h`: Adaptive swap rules (`AK`/`AK2`/`AK_PAIR`), their hold-taps (`MAKE_AK_HM`/`MAKE_AK_LT`), and the nine grid aliases (`FN_L`, `GL_H`, …).
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

### 6. Adaptive Keys Split Into Their Own Module (2026-10-11, `config/twonr9_adaptive_keys.h`)
* **Change**: Moved all nine adaptive keys out of `twonr9_keys.h` into a new `config/twonr9_adaptive_keys.h`.
  * *Reason*: Each key's swap rule, hold wiring and grid name now sit in one contiguous group, so reworking a single adaptive key touches one block instead of scattering across `twonr9_keys.h`. `twonr9_keys.h` dropped from 256 to 182 lines.
  * *Structure*: `AK_TRIG`/`AK`/`AK2`/`AK_PAIR` generate the adaptive nodes; `MAKE_AK_HM`/`MAKE_AK_LT` wire each into a hold-tap; a trailing `#define` gives it its grid alias.
  * *Verified*: Devicetree diff showed all `ak_*` nodes and all 6 layer bindings byte-identical to before the split — only file layout changed.

### 7. Grid Row-Swap: Layers to Top Row, Mods to Home Row (2026-10-11, `config/twonr9.keymap`)
* **Change**: On both `a1` and `a2`, the **top row became layer-taps** (`L_FN` / `L_NAV` / `L_SYM`) and the **home row became modifiers** (`LCTRL` / `LALT` / `LGUI` / `LSHFT`), mirrored on the right half with right-hand modifiers (`RCTRL` / `RALT` / `RGUI` / `RSHFT`). Alpha letters did not move — only each key's hold behavior changed.
  * *Reason*: Consolidates holds by role — every layer access is on the top row, every modifier on the home row — and removes a pre-existing handedness inconsistency (`&hmr LCTRL DE_Y`, a right-hand key holding left Ctrl).
  * *Adaptive keys*: 7 of the 9 keys flipped generator (`MAKE_AK_HM` ↔ `MAKE_AK_LT`) and were renamed to match their new hold (e.g. `AL_L`→`FN_L`, `NV_H`→`GL_H`, `FN_I`→`AR_I`).
  * *Trigger sets*: `TRIG_L`/`TRIG_R` are hand-based, not row-based, so no trigger positions needed changing.
  * *Combos*: All position-based and unaffected — no letter moved, so every combo still finds its keys in place.
  * *Verified*: Devicetree diff showed only the 9 adaptive hold-taps and 4 grid lines changed; all combo nodes and `ak_*` nodes byte-identical. Left 34.07% FLASH / 28.84% RAM, right 23.42% / 13.86% — matching baseline.

### 8. quick-tap-ms Removed From Gated Hold-Taps (2026-10-11, `config/twonr9.keymap` + `twonr9_adaptive_keys.h`)
* **Change**: Omitted `quick-tap-ms` from `MAKE_HRM`, the `&lt` override, `MAKE_AK_HM` and `MAKE_AK_LT`. Kept `QUICK_TAP_MS` (175) on `lt_spc`, `lt_dual`, `magic_shift` and `smart_num`.
  * *Reason*: In ZMK's `is_quick_tap()`, the same-key quick-tap branch is only evaluated **after** the `require-prior-idle-ms` gate has already failed. Since `HRM_IDLE`/`LT_IDLE` are both 300, any `quick-tap-ms` value ≤ 300 is unreachable on those behaviors — the property was dead. `require-prior-idle-ms = <300>` remains the sole gate, which also matches urob's timeless HRM (his config sets no `quick-tap-ms` at all).
  * *Why some remain*: The four thumb behaviors that keep it have **no** `require-prior-idle-ms`, so their `quick-tap-ms` is genuinely live; removing it there would change behavior.
  * *Verified*: Devicetree diff showed exactly 12 `quick-tap-ms` lines removed and nothing added; the four live sites and ZMK's built-in `mt` behaviors retained theirs.

### 9. Teenspirit Target Removed (2026-10-11, `build.yaml`)
* **Change**: Dropped the Teenspirit (xiao_rp2040) target entirely — the two `build.yaml` entries (teenspirit + its `settings_reset`), the `config/boards/shields/teenspirit/` shield definition, and both `.uf2` artifacts.
  * *Reason*: The teenspirit shield ships no keymap, so the build failed with `Failed to locate keymap file!` → `#error "Keymap node not found"`. The target was unused. The four remaining targets all build.
  * *Verified*: `git grep teenspirit` returns nothing; `just build all` produces all four artifacts (`twonr9_left`, `twonr9_left_with_studio`, `twonr9_right`, `settings_reset`), and the push CI workflow (`build.yml`, zmkfirmware's action) passes on all four.
* **Note on the two CI workflows**: Pushes/PRs are built by **`build.yml`**, which passes on every target. The **`build-nix.yml`** workflow (urob's nix action) is **manual-dispatch only** — its push triggers were already commented out before this session and are deliberately left that way, and the workflow file is unchanged here. It has never passed in this repo: urob's `setup-sdk` builds its own environment (it ignores this repo's `flake.nix`), and its `zephyr` toolchain ships no `protoc`, which the ZMK Studio target needs because nanopb regenerates its protobuf bindings by shelling out to it. Setting `toolchain: zephyr-full` is not a workaround — that path fails to build `spsdk` on an upstream `hidapi` conflict, taking every job down. Local builds are unaffected: the nix dev environment in this repo ships `protoc`, which is why `just build` succeeds on all targets.

### 10. Diagram Regeneration & Draw-Parser Fixes (2026-10-11, `draw/`)
* **Change**: Regenerated all tracked diagrams with `just draw-twonr9` (they were 10 days stale and still showed the pre-swap layout), and fixed three bugs in `draw/draw_twonr9.py` that made the parser misread the current keymap:
  * *`&lt` recognition*: The layer-tap branch only matched the **legacy** node names (`&lt_r4`, `&lt_h`, `&lt_i`, `&lt_v`). The current plain `&lt` override fell through with **no hold label at all**. It now matches `&lt` too and derives the label from the layer argument — accepting both the `L_NAV` form and the numeric index the `keymap` CLI emits (`nav`=2, `sym`=3, `fn`=4, `num`=5).
  * *Shift detection*: The mod label used `"SHI" in mod_raw`, which is **false** for `LSHFT`/`RSHFT` (no "SHI" substring) — so every Shift key was drawn as Ctrl (⌃). Now tests `"SHFT"`/`"SHIFT"`, so `T`, `C`, `K`, `G` correctly show ⇧.
  * *Right-hand modifiers*: `hold_abbr_map` had no entries for `RIGHT ALT`/`RIGHT GUI`, leaving raw text on the adaptive keys. Added `RALT`/`RGUI`/`RSHFT`/`RCTRL` and their long forms.
  * *Reason*: Two of these (the `&lt` gap and Shift mislabel) were **pre-existing** — the old diagrams had already been wrong; the row-swap simply moved far more keys onto `&lt`/mod holds and made it obvious.
  * *Verified*: All 36 hold labels across `a1`/`a2` now match `config/twonr9.keymap` binding-for-binding (`a1`: L→fn N→nav D→sym Y→sym O→nav U→fn / S→⌃ R→⌥ H→⌘ T→⇧ C→⇧ E→⌘ I→⌥ A→⌃). All four alpha-layer modifier glyphs render with the `hold-mod` color class, and no raw `RIGHT …` text remains in the SVGs.

---

## 3. The Power of Urob's ZMK Architecture

Urob's configuration is widely recognized as the gold standard for minimal-key ergonomic keyboards. Key architectural concepts include:

### 1. "Timeless" Homerow Mod Tuning
* `flavor = "balanced"`: Activates as a hold only if another key is pressed and released while held.
* `require-prior-idle-ms = <300>`: Holds only trigger if you pause typing for 300ms before pressing the key. During fast typing streams, keys *always* output as letters even if fingers overlap.
  * *Note*: urob's reference config uses `150`. This config deliberately doubles it to `300` — a stricter gate, so accidental mods during continuous typing are rarer, but intentional mods right after a word need a slightly longer pause. `HRM_IDLE` and `LT_IDLE` are independent constants; either can be tuned without touching the other.
* `hold-trigger-key-positions`: A left-hand modifier will *never* activate if you press another left-hand key.
* **No `quick-tap-ms`**: It is deliberately omitted here. ZMK's `is_quick_tap()` only evaluates its same-key quick-tap branch *after* the `require-prior-idle-ms` gate has failed, so with a 300ms idle window any `quick-tap-ms` value ≤ 300 is unreachable. Omitting it also matches urob, whose config sets none.

### 2. Micro-Module Ecosystem
* `zmk-helpers`: Standardized key positions, hold-taps, morphs, and macros.
* `zmk-auto-layer`: Auto-terminating layers (`num_word`).
* `zmk-adaptive-key`: Dynamic context-aware keys (`magic_shift`, auto-repeat).
* `zmk-tri-state`: Conditional state toggles (`swapper`).

---

## 4. Advanced Behaviors & Smart Engine

### Tuning Constants (single source of truth)

Defined at the top of `config/twonr9.keymap`, shared by every hold-tap:

| Constant | Value | Meaning |
|----------|-------|---------|
| `QUICK_TAP_MS` | 175 | Same-key quick-tap window — **only** on the ungated thumb behaviors (`lt_spc`, `lt_dual`, `magic_shift`, `smart_num`) |
| `HRM_TERM` | 280 | Homerow-mod tapping term (`hml`/`hmr`, `MAKE_AK_HM`) |
| `HRM_IDLE` | 300 | Homerow-mod require-prior-idle |
| `LT_TERM` | 200 | Layer-tap tapping term (`&lt`, `MAKE_AK_LT`) |
| `LT_IDLE` | 300 | Layer-tap require-prior-idle |
| `AK_MS` | 300 | Adaptive-key swap window (max prior idle for triggers) |

### A. Adaptive `magic_shift` (`MAGIC_SHIFT`)
* **Reachability**: Not bound to any thumb key. Reached only via two home-row combos, active on every layer (`ALL`):
  * **`shiftl`** — home row 8+9 (left hand inner pair)
  * **`shiftr`** — home row 10+11 (right hand inner pair)
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

### E. Adaptive Key Swaps & Symbol Auto-Repeat
* **Adaptive Key Swaps (SFB Elimination)**:
  * **`r hl`** (After `R`): Pressing `H` outputs `L` (fast `rl` roll), pressing `L` outputs `H`.
  * **`u oi`** (After `U`): Pressing `O` outputs `I` (fast `ui` roll), pressing `I` outputs `O`.
  * **`q iu`** (After `Q`): Pressing `I` outputs `U` (fast `qu` roll for *Quelle*, *Quiz*), pressing `U` outputs `I`.
  * **`r mv`** (After `R`): Pressing `M` outputs `V` (fast `rv` roll), pressing `V` outputs `M`.
  * **`n bx`** (After `N`): Pressing `B` outputs `X` (fast `nx` roll), pressing `X` outputs `B`.
  * *Where these live*: The swap rules, hold wiring, and grid aliases for all nine adaptive keys are defined in [`config/twonr9_adaptive_keys.h`](twonr9_adaptive_keys.h). Each key's rule, hold-tap, and `#define` sit together in one group, so reworking a single adaptive key touches one contiguous block.
* **Expanded Symbol & Number Auto-Repeat**: Tapping Magic Shift immediately after typing any symbol or number (`==`, `++`, `::`, `//`, `!=`, `->`, `**`, `11`, `00`) instantly repeats that character.

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

Top row = layer-taps · Home row = modifiers (mirrored on the right half).

```c
ZMK_LAYER(a1,
//                         ╭─────────────────┬─────────────────┬─────────────────╮      ╭─────────────────┬─────────────────┬─────────────────╮
                            FN_L              &lt L_NAV DE_N    &lt L_SYM DE_D           &lt L_SYM DE_Y    NV_O              FN_U
//       ╭─────────────────┼─────────────────┼─────────────────┼─────────────────┤      ├─────────────────┼─────────────────┼─────────────────┼─────────────────┤
          &hml LCTRL DE_S   &hml LALT DE_R    GL_H              &hml LSHFT DE_T          &hmr RSHFT DE_C   &hmr RGUI DE_E    AR_I              &hmr RCTRL DE_A
//       ╰─────────────────┴─────────────────┴─────────────────┴─────────────────╯      ╰─────────────────┴─────────────────┴─────────────────┴─────────────────╯
                                              SMART_NUM         A2_DUAL                  SPC_NAV           SYM_DUAL
//                                           ╰─────────────────┴─────────────────╯      ╰─────────────────┴─────────────────╯
)
```

| Pos | Key | Hold | Pos | Key | Hold |
|-----|-----|------|-----|-----|------|
| 0 | L *(adaptive)* | `FN_L` (fn) | 3 | Y | `&lt L_SYM` |
| 1 | N | `&lt L_NAV` (nav) | 4 | O *(adaptive)* | `NV_O` (nav) |
| 2 | D | `&lt L_SYM` (sym) | 5 | U *(adaptive)* | `FN_U` (fn) |
| 6 | S | `&hml LCTRL` | 10 | C | `&hmr RSHFT` |
| 7 | R | `&hml LALT` | 11 | E | `&hmr RGUI` |
| 8 | H *(adaptive)* | `GL_H` (GUI) | 12 | I *(adaptive)* | `AR_I` (RALT) |
| 9 | T | `&hml LSHFT` | 13 | A | `&hmr RCTRL` |

#### Layer 1: `a2` (Secondary Alphas)

Same row-split: top row = layer-taps, home row = modifiers.

```c
ZMK_LAYER(a2,
//                            ╭────────────────────┬────────────────────┬────────────────────╮      ╭────────────────────┬────────────────────┬────────────────────╮
                               FN_X                 NV_B                 SY_V                        &lt L_SYM DE_W       &lt L_NAV DE_Q       &lt L_FN DE_COMMA
//       ╭────────────────────┼────────────────────┼────────────────────┼────────────────────┤      ├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
          &hml LCTRL DE_F      AL_M                 &hml LGUI DE_P       &hml LSHFT DE_K             &hmr RSHFT DE_G      &hmr RGUI DE_J       &hmr RALT DE_DOT     &hmr RCTRL DE_Z
//       ╰────────────────────┴────────────────────┴────────────────────┴────────────────────╯      ╰────────────────────┴────────────────────┴────────────────────┴────────────────────╯
                                                    SMART_NUM            &to L_A1                    SPC_NAV              SYM_DUAL
//                                                 ╰────────────────────┴────────────────────╯      ╰────────────────────┴────────────────────╯
)
```

| Pos | Key | Hold | Pos | Key | Hold |
|-----|-----|------|-----|-----|------|
| 0 | X *(adaptive)* | `FN_X` (fn) | 3 | W | `&lt L_SYM` |
| 1 | B *(adaptive)* | `NV_B` (nav) | 4 | Q | `&lt L_NAV` |
| 2 | V *(adaptive)* | `SY_V` (sym) | 5 | `,` | `&lt L_FN` |
| 6 | F | `&hml LCTRL` | 10 | G | `&hmr RSHFT` |
| 7 | M *(adaptive)* | `AL_M` (LALT) | 11 | J | `&hmr RGUI` |
| 8 | P | `&hml LGUI` | 12 | `.` | `&hmr RALT` |
| 9 | K | `&hml LSHFT` | 13 | Z | `&hmr RCTRL` |

> **Adaptive keys** (marked *adaptive*) additionally rewrite their own output based on the preceding bigram — see [§4.E](#e-adaptive-key-swaps--symbol-auto-repeat). Their hold wiring lives in [`config/twonr9_adaptive_keys.h`](twonr9_adaptive_keys.h).

#### Layer 2: `nav` (Navigation & Niri Suite)
```c
ZMK_LAYER(nav,
//              ╭────────┬────────┬────────╮      ╭────────┬────────┬────────╮
                  &sk LALT &sk LGUI &sk LSHFT       NAV_LEFT NAV_DOWN NAV_UP
//       ╭──────┼────────┼────────┼────────┤      ├────────┼────────┼────────┼────────╮
           &sk LCTRL &kp LG(DE_Q) &kp LG(TAB) &niri_adjust &swapper NAV_PGDN NAV_PGUP NAV_RIGHT
//       ╰──────┴────────┼────────┼────────┤      ├────────┼────────┼────────┴────────╯
               SMART_NUM  &to L_A1           SPC_NAV   SYM_DUAL
//                     ╰─────────┴─────────╯      ╰───────────┴─────────╯
)
```

#### Layer 3: `sym` (Morphing Brackets & Symbols)
```c
ZMK_LAYER(sym,
//              ╭───────────┬───────────┬───────────╮      ╭────────┬────────┬────────────╮
                  &excl_qmark &hash_tilde &dllr_euro         &lpar_rpar &lbkt_rbkt &semi_sqt
//       ╭──────┼───────────┼───────────┼───────────┤      ├────────┼────────┼────────────┼──────────╮
            &grave_caret &under_minus &amps_at &equal_pipe  &lbrc_rbrc &lt_gt &colon_dqt &fslh_bslh
//       ╰──────┴───────────┼───────────┼───────────┤      ├────────┼────────┼────────────┴──────────╯
                         SMART_NUM  &to L_A1           SPC_NAV   SYM_DUAL
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
                         SMART_NUM  &to L_A1           SPC_NAV   SYM_DUAL
//                     ╰───────────┴──────────╯      ╰───────────┴─────────╯
)
```

#### Layer 5: `num` (3x3 Calculator Numpad & Math)
```c
ZMK_LAYER(num,
//              ╭────────────┬────────────┬────────────╮      ╭────────┬────────┬────────╮
                  &kp DE_MINUS &kp DE_ASTRK &kp DE_EQUAL        &kp DE_N4 &kp DE_N5 &kp DE_N6
//       ╭──────┼────────────┼────────────┼────────────┤      ├────────┼────────┼────────┼──────╮
           &kp DE_PLUS &kp DE_PRCNT &kp DE_FSLH &dot_comma      &kp DE_N1 &kp DE_N2 &kp DE_N3 &kp DE_N0
//       ╰──────┴────────────┼────────────┼────────────┤      ├────────┼────────┼────────┴──────╯
                             SMART_NUM  &to L_A1           SPC_NAV   SYM_DUAL
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
