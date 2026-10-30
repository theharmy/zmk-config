# TwoNr9 Keyboard & Urob ZMK Workspace Technical Guide

Comprehensive technical documentation for the **TwoNr9 (18-Key Split)** keyboard integrated into the **Urob ZMK Workspace**.

> ⚡ **Quick Reference & Visual Infographic:** View [`docs/CHEATSHEET.md`](../docs/CHEATSHEET.md) or [`draw/twonr9_cheatsheet.svg`](../draw/twonr9_cheatsheet.svg) for an all-in-one visual layout and combo usability reference.

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
* **Two Keymap Variants, One Shield Definition**: The hardware lives in `config/boards/shields/twonr9/`; ZMK resolves the keymap by shield name, so no cmake-args or manual steps are needed. See [§6](#6-hardware-shields--build-targets).
  * **`bugwind`** (default): `twonr9_left` / `twonr9_right` → `config/twonr9.keymap`. No adaptive keys — every letter is bound directly, so the grids are self-describing.
  * **`srht`** (backup): `twonr9_srht_left` / `twonr9_srht_right` → `config/twonr9_srht.keymap`. Keeps the nine adaptive keys.
  * Bluetooth names differ (`TwoNr9` vs `TwoNr9 SRHT`) so both can be paired side by side without re-bonding.
* **Automated Visualizations**: all-layer, overview, combined overview and cheatsheet drawings are retained in their original form; the bugwind diagonal symbol mod-morph list is additionally available at `draw/twonr9_mod_morph_overview.svg`.

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
  * *(Since renamed for the two-variant split — see [§2.11](#11-two-keymap-variants-as-two-shields-2026-10-12-config--buildyaml--draw). Today the adaptive module is `twonr9_adaptive_keys_srht.h`, and the macros/combos come in `*_bugwind` and `*_srht` variants plus the shared `twonr9_combos.dtsi`.)*

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

### 11. Two Keymap Variants as Two Shields (2026-10-12, `config/` + `build.yaml` + `draw/`)
* **Change**: Split the single keymap into **two real shields** so `just build <variant>` and CI both resolve the right keymap **by shield name** — no `cmake-args`, no manual steps, identical behaviour locally and in GitHub Actions.
  * **`bugwind` (default)**: `twonr9_left` / `twonr9_right` → `config/twonr9.keymap` + `config/twonr9.conf`. No adaptive keys — every alpha is bound directly, so the grids are self-describing.
  * **`srht` (optional backup)**: `twonr9_srht_left` / `twonr9_srht_right` → `config/twonr9_srht.keymap` + `config/twonr9_srht.conf`. Keeps the nine adaptive keys.
  * `config/boards/shields/twonr9/` is now the **only** place the physical grid is defined (dtsi, both half overlays, and its `Kconfig.*`). `twonr9_srht/` holds nothing but thin overlays that `#include "../twonr9/twonr9_left.overlay"`, plus its own `Kconfig.shield`/`Kconfig.defconfig` — so there is no duplicated hardware definition to drift.
  * **Why shields rather than `-DKEYMAP_FILE=`**: a keymap path passed to `west build` must be absolute (so it breaks on any other machine), and `KEYMAP_FILE` is a **CMake cache variable** — reusing a build directory with a different keymap silently keeps the old one unless the define is repeated or the build is pristine. Shield-name resolution has neither problem, and it is what ZMK already does natively.
  * **Bluetooth names differ on purpose**: bugwind keeps `"TwoNr9"` so existing bonds survive; srht is `"TwoNr9 SRHT"`, so both halves can sit paired to the same host side by side without re-bonding.
* **`.conf` split**: `twonr9.conf` + `twonr9_srht.conf`. ZMK resolves `.conf` by *shield directory name* and its search loop **appends every match rather than breaking on the first**, and there is no include mechanism for `.conf` files — so the two files necessarily duplicate the hardware/power settings. They must be edited in sync; this is called out in both file headers and in §6.
* **Build matrices split**: `build.yaml` keeps only the default targets (bugwind left / left-with-studio / right / settings_reset) — i.e. what CI builds, so the matrix stays lean and `firmware/` is not cluttered with a backup. The srht targets moved to **`build-srht.yaml`** with a new **`just build-srht`** recipe that overrides the Justfile's existing `build_matrix` variable (`just build_matrix=build-srht.yaml build all` is the underlying form). srht is therefore fully buildable but never built by accident.
* **Two keymap bugs fixed** (both unambiguous defects, not taste):
  * `a2` top row, position 4: bound `DE_P`, which **duplicated `P`** (already at `a1` pos 6) and left **`Q` missing entirely** → now `DE_Q`.
  * `a1` home row, position 12: `&hmr RGUI DE_I` **duplicated `RGUI`** (already at pos 11) → now `&hmr RALT DE_I`, restoring the symmetric `⌃ ⌥ ⌘ ⇧ / ⇧ ⌘ ⌥ ⌃` mod fan.
  * The srht keymap was also **missing `#include "twonr9_combos.dtsi"`**, silently dropping 18 shared utility combos (tab, enter, bspc, cbspc, esc, ß, under, minus, colon, semi, caps, stdio, shiftl, shiftr, numpad 7/8/9) — restored.
* **Dead files removed**: `config/twonr9_adaptive_keys_bugwind.h` (bugwind has no adaptive keys) and `config/twonr9_keys.h.bak`. The surviving adaptive module was renamed to `config/twonr9_adaptive_keys_srht.h` to make its ownership explicit.
* **Draw system made variant-aware** (`draw/draw_twonr9.py`): a `VARIANTS` table drives everything — per-variant keymap path, title, a1/a2 bigram lists, adaptive rules (or `None`), and the ß chord text. `main()` takes optional variant names (`just draw-twonr9 [bugwind|srht|all]`, default **bugwind only**, so every existing doc link keeps resolving).
  * Derived, not duplicated: `combined_bigram_map()` builds the a1/a2 chord pairs from the bigram lists, and `combo_symbol()` resolves `&macro_<bigram>` bindings from the same lists — so the grids in the diagrams **cannot** drift from the keymap. (The previous hardcoded `combo_symbol_map` only knew the srht macro names, which is why the bugwind diagrams silently lost the `MB`/`YS`/`RW`/`MT`/`SCH`/`GS` chords.)
  * The adaptive legend card, the PIP reference card, and the cheatsheet prose now read from the variant table; bugwind renders an explicit *"none — every letter is bound directly"* in place of the swap rules.
  * Output names: bugwind keeps the canonical `twonr9*.svg` names; srht writes `twonr9_srht_*.svg`.
* *Verified*: `just build all` produces all four default artifacts; `just build-srht` produces both srht halves. The compiled `zephyr.dts` was decoded for both variants and confirmed all 26 letters appear **exactly once** across `a1`+`a2`, `I` is `RALT`, `A` is `GUI`, and `Q` is present with `P` appearing once. All 12 bigrams render on both variants' diagrams, and the adaptive legend/dashes appear on srht only.
* *Note*: `config/twonr9_adaptive_keys_bugwind.h` was deleted but `config/twonr9_adaptive_keys_srht.h` is now the sole adaptive module, included only by the srht keymap.

### 12. Diagonal Chord Regrouping & German Space Chords (2026-10-27, `config/` + `draw/` + `practice/`)
* **Change**: The bugwind diagonal symbol chords were regrouped from 15 ad-hoc assignments into **16 chords in four geometry families** (mirrored across the split), all in `config/symbol_work.dtsi`:
  * **Inner-1 (brackets)**: `L+N ( )` · `Y+E ) (` · `M+R [ ]` · `U+A ] [` · `D+T { }` · `O+I } {` — openers plain on the left hand, closers plain on the right, so every bracket type is available with both hands.
  * **Inner-2 (bitwise/logic/arrows)**: `M+N & *` · `O+A $ €` · `D+R ~ ^` · `Y+I < >`.
  * **Outer-1 (sentence/comments)**: `L+T ! ?` · `M+H _ -` · `U+E ; '` · `O+S # %`.
  * **Outer-2**: `L+H : "` · `U+S / \`.
  * The dedicated `##`/`###` states were dropped (repeat `#` instead) in exchange for the bilateral `U+A ] [` chord; every Ctrl/ctrl+Shift operator output is unchanged, only re-homed.
* **German letter chords**: `ß` moved off `N+R` to **`S + Space`** (`10 16`), and the umlauts became **letter + Space** chords — `A+Space ä`, `O+Space ö`, `U+Space ü` (all `a1`/`a2`; uppercase via the shifted state on the German host layout). The shared `combo_sz` in `twonr9_combos.dtsi` was removed; srht got its own `S+R` (6+7) `ß` combo in `twonr9_combos_srht.dtsi` (its 6+7 position is S+R). The freed bugwind `N+R` (6+7) is now `´` with shift → `DE_GRAVE` (backtick on a nodeadkeys host).
* **Draw system**: `DIAGONAL_CHORDS` in `draw/draw_twonr9.py` mirrors the new 16-chord table, now with a `family` field + `FAMILY_ORDER` (the single source for both references). Both the **mod-morph overview** (`twonr9_mod_morph_overview.svg`, replacing the old physical-position grid) and the **symbol-layer reference card** (`twonr9_symbol_layer.svg`) now group the chords into the four family tables (Inner-1 Brackets / Inner-2 Bitwise / Outer-1 Sentence / Outer-2), each chord one row with a `SYMBOL-PAIR` header over Plain/Shift and a `PROGRAMMING-OPERATOR PAIR` header over Ctrl/Ctrl+Shift; rows are ordered by top-row key, then home-row key, both left-to-right. The symbol-layer card renders the families in two columns (inner left, outer right) with a dashed left-hand (L/M/D) vs right-hand (Y/O/U) divider per family, so it stays compact below the board. `extra_combos` and the new `diag_macro_{equal,pipe,plus,at}` labels keep the layer drawings in step. The ß-chord cheatsheet text is now variant-driven (`S + Space` / `S + R` + position). The companion `twonr9_mod_morph_overview.yaml` mirrors the same structure as `families:`.
* **Practice**: `practice/twonr9_chords_monkeytype.md` is a **7-stage progressive curriculum** (quality over quantity) over the full token set (16 chords × 4 states = 64 outputs + 5 German letters + 12 bigrams = 81 tokens; `( ) [ ] { }` are the only duplicates, once per hand): Plain → Plain+Ctrl+erste Wörter → +a1-bigrams+Layer-1-Wörter → all symbols (Shift states) → +a2-bigrams+alle Wörter → Wörter → Vollpass (all 174 tokens once). From stage 2 on the German word pool trains the alpha grid in parallel with the chords: first 20 untagged plain words + the umlaut words (no bigram pairs), then the a1-bigram words, then the a2-bigram words (tiers are derived from the word tags and asserted to partition the pool); `sch`/`gs`/`oe`/`iu` words deliberately force the a2 layer switch mid-word. Every block is self-contained, ~3–4k chars, and round-robined so each random Monkeytype slice is uniform (each token exactly once per round). Generated by `practice/gen_monkeytype.py` (re-run with `python3 practice/gen_monkeytype.py`), which asserts per-block pool purity and exact per-token counts.
* **Combo window → 35ms**: both keymaps now `#define COMBO_TERM 35` before the `zmk-helpers/helper.h` include, so every `ZMK_COMBO` without an explicit timeout uses 35ms instead of the helper default of 30. `combo_stdio` keeps its deliberate 50ms (the slow "Studio Unlock" idle). Verified in the generated devicetree: 48 combos at `timeout-ms = <35>`, 1 at `<50>`.
* *Verified*: `keymap … parse` lists all 21 new chord positions and nothing stale; `just draw-twonr9 all` regenerates both bugwind overviews (checked-in `*_overview.yaml`/cheatsheet artifacts untouched by design); `just build twonr9` and `just build-srht` both succeed (FLASH 23.42% / 31.14%).

### 13. Repo Trimmed to the TwoNr9 (2026-10-30, repo-wide)
* **Change**: Removed everything that belonged to the upstream 34-key layout and is not needed by any TwoNr9 build target:
  * `config/base.keymap` and its private includes `config/combos.dtsi`, `config/leader.dtsi`, `config/mouse.dtsi` (the TwoNr9's combos/symbols live in `twonr9_combos*.dtsi` / `symbol_work.dtsi`).
  * The root `boards/` directory — a byte-identical copy of `config/boards/shields/twonr9/`; `config/boards/` is the live shield root (the only place `twonr9_srht/` exists, and the one the build log resolves).
  * `draw/base.svg`, `draw/overview.svg`, `draw/config.yaml` and the `draw` Justfile recipe that rendered the 34-key layout (`just draw-twonr9` is unaffected).
  * `.github/workflows/build.yml` (redundant with `build-nix.yml`).
* **Docs**: `AGENTS.md` dropped the multi-board/`base.keymap` sections; `README.md` and `docs/build-env.md` replaced their 34-key examples with the TwoNr9's actual HRM setup and targets.
* *Verified*: `just list`, `just build all` (4 targets) and `just build-srht` all succeed after the trim.

### 14. Dropped the PiP Cards & Stray Prettier Config (2026-10-30, `draw/` + repo root)
* **Change**: Removed the picture-in-picture quick-ref cards — `draw/twonr9_pip.{svg,png}` and `draw/twonr9_srht_pip.{svg,png}` — which were referenced by nothing, and the now-dead `build_pip_svg()` generator in `draw/draw_twonr9.py`. Also removed the unreferenced `.prettierrc` (a fork leftover; no tool, recipe or workflow in this repo runs Prettier).
* *Verified*: `draw/draw_twonr9.py` still parses and `just draw-twonr9 all` still runs clean.

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
* **Adaptive Key Swaps (SFB Elimination)** — *`srht` variant only*. The default `bugwind` keymap has no adaptive keys: every alpha is bound directly, so what you see on the grid is what you type.
  * **`r hl`** (After `R`): Pressing `H` outputs `L` (fast `rl` roll), pressing `L` outputs `H`.
  * **`u oi`** (After `U`): Pressing `O` outputs `I` (fast `ui` roll), pressing `I` outputs `O`.
  * **`q iu`** (After `Q`): Pressing `I` outputs `U` (fast `qu` roll for *Quelle*, *Quiz*), pressing `U` outputs `I`.
  * **`r mv`** (After `R`): Pressing `M` outputs `V` (fast `rv` roll), pressing `V` outputs `M`.
  * **`n bx`** (After `N`): Pressing `B` outputs `X` (fast `nx` roll), pressing `X` outputs `B`.
  * *Where these live*: The swap rules, hold wiring, and grid aliases for all nine adaptive keys are defined in [`config/twonr9_adaptive_keys_srht.h`](twonr9_adaptive_keys_srht.h), included only by [`config/twonr9_srht.keymap`](twonr9_srht.keymap). Each key's rule, hold-tap, and `#define` sit together in one group, so reworking a single adaptive key touches one contiguous block.
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

#### Layer 0: `a1` (Base QWERTZ Alphas) — bugwind

Top row = layer-taps · Home row = modifiers (mirrored on the right half).

Every alpha is bound directly, so the grid is self-describing.

```c
ZMK_LAYER(a1,
//                         ╭─────────────────┬─────────────────┬─────────────────╮      ╭─────────────────┬─────────────────┬─────────────────╮
                            &lt L_FN DE_L    &lt L_NAV DE_M    &lt L_SYM DE_D           &lt L_SYM DE_Y    &lt L_NAV DE_O    &lt L_FN DE_U
//       ╭─────────────────┼─────────────────┼─────────────────┼─────────────────┤      ├─────────────────┼─────────────────┼─────────────────┼─────────────────┤
          &hml LCTRL DE_N   &hml LALT DE_R     &hml LGUI DE_T   &hml LSHFT DE_H          &hmr RSHFT DE_S   &hmr RGUI DE_A     &hmr RALT DE_I    &hmr RCTRL DE_E
//       ╰─────────────────┴─────────────────┴─────────────────┴─────────────────╯      ╰─────────────────┴─────────────────┴─────────────────┴─────────────────╯
                                              SMART_NUM         A2_DUAL                  SPC_NAV           SYM_DUAL
//                                           ╰─────────────────┴─────────────────╯      ╰─────────────────┴─────────────────╯
)
```

| Pos | Key | Hold | Pos | Key | Hold |
|-----|-----|------|-----|-----|------|
| 0 | L | `&lt L_FN` (fn) | 3 | Y | `&lt L_SYM` |
| 1 | M | `&lt L_NAV` (nav) | 4 | O | `&lt L_NAV` (nav) |
| 2 | D | `&lt L_SYM` (sym) | 5 | U | `&lt L_FN` (fn) |
| 6 | N | `&hml LCTRL` | 10 | S | `&hmr RSHFT` |
| 7 | R | `&hml LALT` | 11 | A | `&hmr RGUI` |
| 8 | T | `&hml LGUI` | 12 | I | `&hmr RALT` |
| 9 | H | `&hml LSHFT` | 13 | E | `&hmr RCTRL` |

#### Layer 0: `a1` (Base QWERTZ Alphas) — srht

Same row-split and identical *structure*, but nine of the alphas are adaptive: they rewrite their own output based on the preceding bigram (see [§4.E](#e-adaptive-key-swaps--symbol-auto-repeat)), so their binding aliases (`FN_L`, `GL_H`, `AR_I`, …) live in [`config/twonr9_adaptive_keys_srht.h`](twonr9_adaptive_keys_srht.h).

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

#### Layer 1: `a2` (Secondary Alphas) — bugwind

Same row-split: top row = layer-taps, home row = modifiers. Note the thumb at pos 15 toggles back to `a1`.

```c
ZMK_LAYER(a2,
//                            ╭────────────────────┬────────────────────┬────────────────────╮      ╭────────────────────┬────────────────────┬────────────────────╮
                                &lt L_FN DE_X           &lt L_NAV DE_V      &lt L_SYM DE_B             &lt L_SYM DE_G         &lt L_NAV DE_Q       &lt L_FN DE_COMMA
//       ╭────────────────────┼────────────────────┼────────────────────┼────────────────────┤      ├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
          &hml LCTRL DE_P       &hml LALT DE_W         &hml LGUI DE_K       &hml LSHFT DE_F            &hmr RSHFT DE_C      &hmr RGUI DE_Z        &hmr RALT DE_DOT      &hmr RCTRL DE_J
//       ╰────────────────────┴────────────────────┴────────────────────┴────────────────────╯      ╰────────────────────┴────────────────────┴────────────────────┴────────────────────╯
                                                    SMART_NUM            &to L_A1                    SPC_NAV              SYM_DUAL
//                                                 ╰────────────────────┴────────────────────╯      ╰────────────────────┴────────────────────╯
)
```

| Pos | Key | Hold | Pos | Key | Hold |
|-----|-----|------|-----|-----|------|
| 0 | X | `&lt L_FN` (fn) | 3 | G | `&lt L_SYM` |
| 1 | V | `&lt L_NAV` (nav) | 4 | Q | `&lt L_NAV` (nav) |
| 2 | B | `&lt L_SYM` (sym) | 5 | `,` | `&lt L_FN` (fn) |
| 6 | P | `&hml LCTRL` | 10 | C | `&hmr RSHFT` |
| 7 | W | `&hml LALT` | 11 | Z | `&hmr RGUI` |
| 8 | K | `&hml LGUI` | 12 | `.` | `&hmr RALT` |
| 9 | F | `&hml LSHFT` | 13 | J | `&hmr RCTRL` |

#### Layer 1: `a2` (Secondary Alphas) — srht

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

> **Adaptive keys** (marked *adaptive*, `srht` only) additionally rewrite their own output based on the preceding bigram — see [§4.E](#e-adaptive-key-swaps--symbol-auto-repeat). Their hold wiring lives in [`config/twonr9_adaptive_keys_srht.h`](twonr9_adaptive_keys_srht.h).

Layers 2–5 (`nav`, `sym`, `fn`, `num`) and the thumb cluster are **identical in both variants**.

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

### Shield Layout

The physical board is defined **once**; the two keymap variants are thin shields that include it and differ only by which keymap/conf ZMK resolves for them:

```text
config/boards/shields/
├── twonr9/                 # shared hardware: the only place the physical grid is defined
│   ├── twonr9.dtsi
│   ├── twonr9-layouts.dtsi
│   ├── twonr9_left.overlay
│   ├── twonr9_right.overlay
│   ├── Kconfig.shield      # SHIELD_TWONR9_LEFT / SHIELD_TWONR9_RIGHT
│   └── Kconfig.defconfig
└── twonr9_srht/            # optional backup variant -- no hardware of its own
    ├── twonr9_srht_left.overlay   # #include "../twonr9/twonr9_left.overlay"
    ├── twonr9_srht_right.overlay  # #include "../twonr9/twonr9_right.overlay"
    ├── Kconfig.shield      # SHIELD_TWONR9_SRHT_LEFT / SHIELD_TWONR9_SRHT_RIGHT
    └── Kconfig.defconfig
```

### Keymap & Config Resolution

ZMK derives candidate names from the shield, so each variant picks up its own files automatically — no `cmake-args`, no manual steps, identical behaviour locally and in CI:

| Shield | Candidate names | Keymap | Config |
| --- | --- | --- | --- |
| `twonr9_left` | `twonr9`, `twonr9_left` | `config/twonr9.keymap` | `config/twonr9.conf` |
| `twonr9_srht_left` | `twonr9_srht`, `twonr9_srht_left` | `config/twonr9_srht.keymap` | `config/twonr9_srht.conf` |

> **`.conf` files have no include mechanism in ZMK**, so `twonr9.conf` and `twonr9_srht.conf` duplicate the same hardware/power settings. Keep them in sync when editing either.

Bluetooth names intentionally differ — **`TwoNr9`** (bugwind, preserves existing bonds) vs **`TwoNr9 SRHT`** — so both halves can be paired to the same host side by side without re-bonding.

### Build Target Matrix (`build.yaml` — default, built by CI)

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

### Optional Build Target Matrix (`build-srht.yaml` — on demand)

The srht variant is kept as a backup rather than a daily driver, so it is deliberately **not** in `build.yaml` and is **not built by CI**. Build it explicitly:

```bash
just build-srht                       # both halves
just build-srht twonr9_srht_left      # one half only
```

```yaml
include:
  - board: nice_nano@2.0.0//zmk
    shield: twonr9_srht_left

  - board: nice_nano@2.0.0//zmk
    shield: twonr9_srht_right
```

### Generated Firmware Artifacts (`firmware/`)

From `just build all` (the default matrix):

1. **`twonr9_left_with_studio.uf2`**: Central (Left) half with ZMK Studio RPC and KeyPeek Raw HID streaming.
2. **`twonr9_left-nice_nano@2.0.0__zmk.uf2`**: Central (Left) half (standard lightweight build).
3. **`twonr9_right-nice_nano@2.0.0__zmk.uf2`**: Peripheral (Right) half.
4. **`settings_reset-nice_nano@2.0.0__zmk.uf2`**: Diagnostic firmware to clear corrupted BLE bond storage.

From `just build-srht`:

5. **`twonr9_srht_left-nice_nano@2.0.0__zmk.uf2`** / 6. **`twonr9_srht_right-nice_nano@2.0.0__zmk.uf2`**: the backup variant.

---

## 7. Step-by-Step User Workflow

### A. Flashing the Keyboard (bugwind — the default)

1. **Left Half (Central)**:
   * Double-press the physical reset button on the left nice!nano.
   * Drag & drop `firmware/twonr9_left_with_studio.uf2` onto the `NICENANO` USB drive.
2. **Right Half (Peripheral)**:
   * Double-press the physical reset button on the right nice!nano.
   * Drag & drop `firmware/twonr9_right-nice_nano@2.0.0__zmk.uf2` onto the `NICENANO` drive.

For the srht backup, build with `just build-srht` and flash the `twonr9_srht_*` artifacts instead.

### B. Daily Development Commands

```bash
# 1. Generate the bugwind diagrams & cheatsheet infographic
just draw-twonr9

# 1b. Same, but for the srht backup (or `all` for both variants)
just draw-twonr9 srht

# 2. Build every default firmware target (bugwind + settings_reset; what CI builds)
just build all

# 3. Build only the central half with Studio + KeyPeek
just build twonr9_left_with_studio

# 4. Build the optional srht backup variant
just build-srht

# 5. Check west dependencies integrity
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
