# TwoNr9 (18-Key Split) Keyboard Cheatsheet & Usability Guide

> **Visual Infographic:** View [`draw/twonr9_cheatsheet.svg`](../draw/twonr9_cheatsheet.svg) for the all-in-one visual card reference (bugwind). For the srht backup: [`draw/twonr9_srht_cheatsheet.svg`](../draw/twonr9_srht_cheatsheet.svg).

> **Which variant am I looking at?** This cheatsheet documents **bugwind**, the default keymap (`config/twonr9.keymap`) — every letter bound directly. The optional **srht** backup (`config/twonr9_srht.keymap`) differs in the alpha grids, bigram chords and ß chord, and adds nine adaptive keys; see [§9](#9-adaptive-key-swaps--symbol-repeat-srht-only). Other layers and shared combos are common.

---

## 1. Combined Layout & Combo Map

<img src="./draw/twonr9_combined_overview.svg" alt="TwoNr9 Combined Keymap & Combos (bugwind)" width="100%" />

---

## 2. Four-Corner Sub-Layer Legends

Each finger key on the overview diagram displays 4 color-coded sub-legends — one per sub-layer, read by corner rather than by position:

```text
                  ╭──────────────────────────╮
   Top-Left (Cyan)│  tl: sym       tr: nav   │Top-Right (Yellow)
                  │          tap             │
                  │                          │
Bottom-Left(Orange│  bl: num       br: fn    │Bottom-Right (Green)
                  │          hold            │(Layer Activation / Mod)
                  ╰──────────────────────────╯
```

| Corner | Color | Layer | Core Functionality |
| :--- | :--- | :--- | :--- |
| **Top-Left (`tl`)** | **Cyan (`#458588`)** | **`sym`** | Legacy mod-morph symbol pairs; the current symbol chords are listed in §7 |
| **Top-Right (`tr`)** | **Yellow (`#d79921`)** | **`nav`** | One-shot mods `⌥ ⌘ ⇧ ⌃`, Niri ops `⌘Q ⌘⇥ ⌘R`, clustered arrows `← ↓ ↑ →`, workspaces `⌘⇟ ⌘⇞` |
| **Bottom-Left (`bl`)** | **Orange (`#d65d0e`)** | **`num`** | 3x3 Calculator Numpad (`4 5 6` top, `1 2 3 0` home, `.` / `,` decimal morph, `7 8 9` chords) |
| **Bottom-Right (`br`)** | **Green (`#689d6a`)** | **`fn`** | Function Keys `F1`–`F12` & Volume Controls `V-`, `V+` |

---

## 3. Row-Split Hold Model (Base `a1`, bugwind)

The **top row is layer-taps** and the **home row is modifiers**, mirrored across the two halves:

```text
                  LEFT HAND                                     RIGHT HAND
        ╭──────┬──────┬──────┬──────╮                 ╭──────┬──────┬──────┬──────╮
Key     │  6   │  7   │  8   │  9   │                 │  10  │  11  │  12  │  13  │
Letter  │  N   │  R   │  T   │  H   │                 │  S   │  E   │  I   │  A   │
        ├──────┼──────┼──────┼──────┤                 ├──────┼──────┼──────┼──────┤
Hold    │  ⌃   │  ⌥   │  ⌘   │  ⇧   │                 │  ⇧   │  ⌘   │  ⌥   │  ⌃   │
        ╰──────┴──────┴──────┴──────╯                 ╰──────┴──────┴──────┴──────╯
        Pinky   Ring  Middle  Index                   Index  Middle  Ring   Pinky

        ╭──────┬──────┬──────╮                       ╭──────┬──────┬──────╮
Key     │  0   │  1   │  2   │                       │  3   │  4   │  5   │
Letter  │  L   │  M   │  D   │                       │  Y   │  O   │  U   │
        ├──────┼──────┼──────┤                       ├──────┼──────┼──────┤
Hold    │  fn  │ nav  │ sym  │                       │ sym  │ nav  │  fn  │
        ╰──────┴──────┴──────╯                       ╰──────┴──────┴──────╯
```

* **Index (`H` on 9, `S` on 10)**: Hold $\rightarrow$ **`⇧` (Shift)** on the home row, **`sym` layer** on the top row.
* **Symmetric fan**: mods read `⌃ ⌥ ⌘ ⇧` outwards on the left and `⇧ ⌘ ⌥ ⌃` outwards on the right.
* **Homerow mods are "timeless"** (`balanced` flavor + `require-prior-idle-ms = 300`) — see [`config/DOCUMENTATION.md`](../config/DOCUMENTATION.md) §3.1.

### Secondary Alphas (`a2`)

Same row-split. Tap the **Left Outer Thumb (14)** for one letter, hold it to stay in `a2` for whole words (*BMW*, *Quiz*, *Pflanze*). On bugwind, the right pinky key (position 13) is `Z`:

| Pos | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Key** | X | V | B | G | J | `,` | P | W | K | F | C | Q | `.` | Z |
| **Hold** | fn | nav | sym | sym | nav | fn | ⌃ | ⌥ | ⌘ | ⇧ | ⇧ | ⌘ | ⌥ | ⌃ |

---

## 4. Symmetrical Adaptive Thumb Engine

```text
                  LEFT THUMBS                                 RIGHT THUMBS
          ╭──────────────┬──────────────╮             ╭──────────────┬──────────────╮
          │   Thumb 14   │   Thumb 15   │             │   Thumb 16   │   Thumb 17   │
          │   (Outer)    │   (Inner)    │             │   (Inner)    │   (Outer)    │
          ├──────────────┼──────────────┤             ├──────────────┼──────────────┤
          │  SMART_NUM   │   A2 DUAL    │             │ SPACE / NAV  │  SYM DUAL    │
          ╰──────────────┴──────────────╯             ╰──────────────┴──────────────╯
```

| Thumb Key | Position | Single Tap | Hold Action | Context / Special Feature |
| :--- | :---: | :--- | :--- | :--- |
| **Left Outer (14)** | `14` | **`num_word`** | **Momentary `num`** | Auto-exits number mode on Space, Enter, or alphas |
| **Left Inner (15)** | `15` | **Sticky `a2`** (1 letter) | **Continuous `a2`** | Hold to type secondary words (*BMW*, *Quiz*, *Pflanze*) |
| **Right Inner (16)** | `16` | **`Space`** | **`nav` Layer** | Shift + Tap outputs `. ` (period + space) & arms Sticky Shift |
| **Right Outer (17)** | `17` | **Sticky `sym`** (1 symbol) | **Continuous `sym`** | Hold to chain bracket/symbol pairs without releasing |

> **`MAGIC_SHIFT` is not on the thumbs.** It is reached via the **`shiftl` (8+9)** and **`shiftr` (10+11)** combos on every layer, and quadruples as *Repeat* / *Sticky Shift* / *Shift* / *Caps Word* — see [§8](#8-speed--flow-patterns).

---

## 5. Layer 2: Navigation & Niri Suite (`nav`)

Access via **Right Inner Thumb (16)**, or by holding **`H` (9)** / **`S` (10)** on the top row's mirror (`M` on 1 / `O` on 4):

### Left Hand: Niri Window Controls & Sticky Mods
| Key | Action | Technical Function in Niri / OS |
| :---: | :--- | :--- |
| **`0` `1` `2` `6`** | **`⌥` `⌘` `⇧` `⌃`** | One-shot sticky modifiers for effortless chording |
| **`7`** | **`⌘Q`** (`Super + Q`) | **Close active Niri window** |
| **`8`** | **`⌘⇥`** (`Super + Tab`) | **Toggle Niri window overview** |
| **`9`** | **`&niri_adjust`** | Tap: **`⌘R`** (Cycle Column Width 33%/50%/66%) \| Shift+Tap: **`⌘⌃C`** (Center & Balance Columns) |

### Right Hand: Clustered Arrows, Workspaces & Jumps
| Key | Action | Tap | Hold Action |
| :---: | :--- | :---: | :--- |
| **`3`** | **`NAV_LEFT`** | **`←`** | **`↖`** (Jump to first column) |
| **`4`** | **`NAV_DOWN`** | **`↓`** | **`Ctl + ↘`** (Bottom of document / buffer) |
| **`5`** | **`NAV_UP`** | **`↑`** | **`Ctl + ↖`** (Top of document / buffer) |
| **`13`** | **`NAV_RIGHT`** | **`→`** | **`↘`** (Jump to last column) |
| **`10`** | **`&swapper` (`⇹`)** | **Alt+Tab** | Smooth window cycling in Niri |
| **`11`** | **`NAV_PGDN`** | **`⇟`** (`PgDn`) | **`⌘⇟`** (`Super + PgDn`) $\rightarrow$ **Next Niri Workspace** |
| **`12`** | **`NAV_PGUP`** | **`⇞`** (`PgUp`) | **`⌘⇞`** (`Super + PgUp`) $\rightarrow$ **Previous Niri Workspace** |

---

## 6. Combo Quick Lookup & Practical Benefits

### Top Row: Code Editing & Navigation
| Combo | Keys | Output | Why it's useful / Benefits |
| :--- | :---: | :---: | :--- |
| `combo_tab` | `0 + 1` | **`⇥`** (Tab) | Indentation & autocompletion with Left Hand |
| `combo_rtn` | `1 + 2` | **`⏎`** (Enter) | Newline insertion & command execution with Left Hand |
| `combo_bspc` | `3 + 4` | **`⌫ / ⌦`** (Bspc / Del) | **Morphing Backspace / Delete**: Tap for Backspace, Shift+Tap for Delete |
| `combo_cbspc` | `4 + 5` | **`⌃⌫`** (Word Del) | Delete entire previous word in IDEs and terminal in one pinch |
| `combo_esc` | `3 + 4 + 5` | **`⎋`** (Esc) | **Instant Modal Exit** for Helix / Vim normal mode & dialogs (offset top) |

### Home Row: Coding Symbols & German Orthography
| Combo | Keys | Output | Why it's useful / Benefits |
| :--- | :---: | :---: | :--- |
| `combo_sz` | `6 + 7` | **`ß`** (Eszett) | Fast pinch on base for German words (*Straße*, *groß*, *weiß*) — **`N + R`** on bugwind, **`S + R`** on srht |
| `combo_under` | `7 + 9` | **`_`** (Underscore) | Instant typing of `snake_case` variables and function names |
| `combo_minus` | `7 + 8` | **`-`** (Minus) | Hyphenation, negative values, and CLI flags (`--flag`, `-v`) |
| `combo_colon` | `11 + 12` | **`:`** (Colon) | Rust `::` namespace pathing, Python defs & JSON key-value pairs |
| `combo_semi` | `10 + 12` | **`;`** (Semicolon) | Statement terminator for C, Rust, TypeScript, Java |

### System & Numpad Shortcuts
| Combo | Keys | Output | Why it's useful / Benefits |
| :--- | :---: | :---: | :--- |
| `combo_caps` | `14 + 15` | **`⇪`** (Caps Word) | Type `UPPERCASE_CONSTANTS` (automatically turns off on Space/Enter) |
| `combo_shiftl` | `8 + 9` | **`&shift_repeat`** | Magic Shift (left hand) — see [§8](#8-speed--flow-patterns) |
| `combo_shiftr` | `10 + 11` | **`&shift_repeat`** | Magic Shift (right hand) |
| `combo_stdio` | `7 + 8 + 9` | **`🔓`** (Studio Unlock) | Unlocks live ZMK Studio key remapping (on `sym` layer, offset bottom) |
| `combo_7, 8, 9` | `3+10`, `4+11`, `5+12` | **`7` `8` `9`** | Vertical chords on `num` layer to hit top-row calculator digits |

---

## 7. Symbol chords and legacy `sym` layer

Most programming symbols are now on diagonal alpha-layer combos in `config/symbol_work.dtsi`. Each chord uses plain/Shift for symbols and Ctrl/Ctrl+Shift for its operator pair. These combos work on `a1` and `a2`.

| Family | Chords (Plain / Shift; Ctrl / Ctrl+Shift) |
| :--- | :--- |
| Brackets | `L+N ( / )`; `Y+E ) / (`; `M+R [ / ]`; `O+I ] / [`; `D+T { / }`; `U+A } / {` |
| Bitwise, logic, arrows | `M+N & / *; && / ||`; `O+A $ / €; ?? / ?.`; `D+R ~ / ^; -> / =>`; `Y+I = / +; << / >>`; `D+N < / >; <= / <=`; `Y+A > / <; >= / >=` |
| Sentence, comments | `L+T ! / ?; // / ...`; `M+H - / _; ++ / --`; `U+E ; / :; /* / */`; `O+S ' / "; = / |` |
| Other | `L+H : / "; :: / :=`; `U+S / / \\; + / @` |

The dedicated `sym` layer remains available during the transition and still has its original mod-morph pairs. Access it by holding **Top-Left** on the top row (`D` on position 2 or `Y` on position 3); the layer grid is visible in the diagrams. The alpha chords above are the current reference for the migrated symbol assignments.

---

## 8. Speed & Flow Patterns

1. **Noun Capitalization (*"Das Haus"*)**:
   $$\text{Space (16)} \longrightarrow \text{Sticky Shift (combo 10+11)} \longrightarrow \text{H (Letter)}$$
   *Shift arms for 1 letter and auto-disarms instantly.*

2. **Double Letters (*"Schifffahrt", "Bitte"*)**:
   $$\text{Letter (t)} \longrightarrow \text{Magic Shift (8+9 / 10+11)} \longrightarrow \text{Instant second 't'}$$

3. **German Eszett (*"Straße", "gross"*)**:
   $$\text{Pinch Keys 6 + 7} \longrightarrow \text{Instant 'ß'}$$

4. **Secondary Alphas (*"BMW", "Quiz"*)**:
   $$\text{Tap 14 (1 letter)} \quad\text{or}\quad \text{Hold 14 (continuous words)}$$

5. **Niri Window Management**:
   $$\text{Hold 16 / M / O} \longrightarrow \text{⌘Q (Close), ⌘⇥ (Overview), ⌘R (Width), ⇹ (Swapper), ⌘⇞/⌘⇟ (Workspaces)}$$

6. **Symbol & Number Auto-Repeat (`MAGIC_SHIFT`)**:
   Tapping Magic Shift immediately after typing **any symbol or number** (`==`, `++`, `::`, `//`, `!=`, `->`, `**`, `11`, `00`) instantly repeats that character.

---

## 9. Adaptive Key Swaps & Symbol Repeat (`srht` only)

> **Not part of bugwind.** The default keymap binds every alpha directly, so it has no adaptive keys — what you see on the grid is what you type. This section applies only to the optional **srht** backup (`config/twonr9_srht.keymap`), whose swap rules live in [`config/twonr9_adaptive_keys_srht.h`](../config/twonr9_adaptive_keys_srht.h). See [`config/DOCUMENTATION.md`](../config/DOCUMENTATION.md) §4.E.

1. **Adaptive Key Swaps (SFB Elimination)**:
   * **`r hl`** (After `R`): Pressing `H` outputs **`L`** (fast `rl` roll), pressing `L` outputs **`H`**.
   * **`u oi`** (After `U`): Pressing `O` outputs **`I`** (fast `ui` roll), pressing `I` outputs **`O`**.
   * **`q iu`** (After `Q`): Pressing `I` outputs **`U`** (fast `qu` roll for *Quelle*, *Quiz*), pressing `U` outputs **`I`**.
   * **`r mv`** (After `R`): Pressing `M` outputs **`V`** (fast `rv` roll), pressing `V` outputs **`M`**.
   * **`n bx`** (After `N`): Pressing `B` outputs **`X`** (fast `nx` roll), pressing `X` outputs **`B`**.

2. **Bigram Chords (srht)**:
   * `a1`: `RL` · `HN` · `DT` · `CY` · `EO` · `UI`
   * `a2`: `RM` · `NB` · `KT` · `GY` · `OE` · `IU`

### Bigram Chords (bugwind)

   * `a1`: `RL` · `KT` · `MB` · `YS` · `EO` · `UI`
   * `a2`: `RW` · `MT` · `SCH` · `GS` · `OE` · `IU`

Each chord is a **vertical pair across the same column** (e.g. `0 + 7`, `1 + 8`, …), so they land under the finger that would otherwise produce the awkward roll.
