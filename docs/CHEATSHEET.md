# TwoNr9 (18-Key Split) Keyboard Cheatsheet & Usability Guide

> **Visual references:** [`draw/twonr9_keymap.html`](../draw/twonr9_keymap.html) (interactive:
> layers, all eight chord states, any chord previewed on its keys) and
> [`draw/twonr9_srht_current.svg`](../draw/twonr9_srht_current.svg) (every layer as one SVG).

> **One keymap.** This cheatsheet describes the only keymap, `config/twonr9.keymap`, built by the
> `twonr9_left` / `twonr9_right` shields. The `_srht` suffixes on some files name the layout
> family, not a second variant. Nine adaptive swaps are active (see [§9](#9-adaptive-key-swaps--symbol-repeat)).

---

## 1. Combined Layout & Combo Map

<img src="./draw/twonr9_srht_current.svg" alt="TwoNr9 keymap, every layer" width="100%" />

---

## 2. What the layers are

Seven layers, all drawn in [`draw/twonr9_srht_current.svg`](../draw/twonr9_srht_current.svg) and
clickable in [`draw/twonr9_keymap.html`](../draw/twonr9_keymap.html):

| Layer | Reached by | Holds |
| --- | --- | --- |
| `a1` | base | alphas, thumbs `⇧` (smart shift) `a2` `Spc` `Num` |
| `a2` | thumb `a2` (or `14+15` for a2 + Shift) | second alpha grid |
| `nav` | hold `Spc` | arrows, one-shot mods, niri window controls |
| `sym` | hold `D` or `Y` (legacy) | the original mod-morph pairs |
| `fn` | hold `L` or `U` | F1–F12, volume, BT prev/next/clear |
| `num` | tap or double-tap `Num` | digits, arithmetic, `7 8 9` column chords |
| `mouse` | `16+17` (`Spc`+`Num`) | pointer, buttons, scroll; leave with `14+15` |

The left thumb is **smart shift**: hold for Shift, tap straight after a letter to repeat it, tap
on a pause for a one-shot Shift, and Shift+tap for caps word (same behaviour as the `8+9` /
`10+11` magic-shift chords).

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

> **`MAGIC_SHIFT` is not on the thumbs.** It is reached via the **`shiftl` (8+9)** and **`shiftr` (10+11)** combos on the typing layers (not vim normal/visual, where those pairs are motions), and quadruples as *Repeat* / *Sticky Shift* / *Shift* / *Caps Word* — see [§8](#8-speed--flow-patterns).

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
| `combo_de_sz` | `10 + 16` | **`ß`** (Eszett) | Fast pinch on base for German words (*Straße*, *groß*, *weiß*) — `S + Space` on bugwind, `C + Space` on srht |
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

## 7. Symbols

Every symbol chord, with its eight states and the mod key each needs, is in the generated
[`SYMBOLS.md`](SYMBOLS.md). Do not copy it here; `just check-keymap` keeps it honest.

How to remember the system:

* **Mods by finger, opposite hand:** Shift = index, Cmd = middle, Alt = ring, Ctrl = pinky.
* **Every mod has a pair:** the mod alone, and the same mod + Shift.
* **Plain opens, Shift closes:** `( )`, `[ ]`, `{ }`, `< >`.
* **Mirrored hands:** a family sits on the same finger class on both sides — `- _` mirrors `= +`,
  `" '` mirrors the backtick, `/` mirrors `\`.
* **Escapes ride with their character:** `\_` with `_`, `\#` with `#`, `\&` with `&`.
* **Doubles live on the Ctrl side:** `//`, `&&`, `**`, ``` ``` ```, `""`, `''`.

German letters (same positions on both layers): `ß` = `C`+`Space`, `ä`/`ö`/`ü` = vowel+`Space`,
`´` (Shift ``` ` ```) = `S`+`R`.

---

## 8. Speed & Flow Patterns

1. **Noun Capitalization (*"Das Haus"*)**:
   $$\text{Space (16)} \longrightarrow \text{Sticky Shift (combo 10+11)} \longrightarrow \text{H (Letter)}$$
   *Shift arms for 1 letter and auto-disarms instantly.*

2. **Double Letters (*"Schifffahrt", "Bitte"*)**:
   $$\text{Letter (t)} \longrightarrow \text{Magic Shift (8+9 / 10+11)} \longrightarrow \text{Instant second 't'}$$

3. **German Eszett (*"Straße", "gross"*)**:
   $$\text{Pinch Keys 10 + 16} \longrightarrow \text{Instant 'ß'} \quad (S + \text{Space})$$

4. **Secondary Alphas (*"BMW", "Quiz"*)**:
   $$\text{Tap 14 (1 letter)} \quad\text{or}\quad \text{Hold 14 (continuous words)}$$

5. **Niri Window Management**:
   $$\text{Hold 16 / M / O} \longrightarrow \text{⌘Q (Close), ⌘⇥ (Overview), ⌘R (Width), ⇹ (Swapper), ⌘⇞/⌘⇟ (Workspaces)}$$

6. **Symbol & Number Auto-Repeat (`MAGIC_SHIFT`)**:
   Tapping Magic Shift immediately after typing **any symbol or number** (`==`, `++`, `::`, `//`, `!=`, `->`, `**`, `11`, `00`) instantly repeats that character.

---

## 9. Adaptive Key Swaps & Symbol Repeat

Both variants correct the most common fast-typing (SFB) mistypes: within **300 ms** of its trigger key, an adaptive key outputs its swap partner. The chord path (both keys pressed together) and everything outside the window are unaffected. srht carries the full set of nine keys; bugwind only the two most frequent swaps.

1. **Adaptive Key Swaps (SFB Elimination)**:
   * **`u oi`** (After `U`): Pressing `O` outputs **`I`** (fast `ui` roll), pressing `I` outputs **`O`**. — *both variants*
   * **`y us`** (After `Y`): Pressing `U` outputs **`S`** (fast `ys` roll), pressing `S` outputs **`U`**. — *bugwind only*
   * **`r hl`** (After `R`): Pressing `H` outputs **`L`** (fast `rl` roll), pressing `L` outputs **`H`**. — *srht only*
   * **`q iu`** (After `Q`): Pressing `I` outputs **`U`** (fast `qu` roll for *Quelle*, *Quiz*), pressing `U` outputs **`I`**. — *srht only*
   * **`r mv`** (After `R`): Pressing `M` outputs **`V`** (fast `rv` roll), pressing `V` outputs **`M`**. — *srht only*
   * **`n bx`** (After `N`): Pressing `B` outputs **`X`** (fast `nx` roll), pressing `X` outputs **`B`**. — *srht only*

   The swap rules and hold wiring live in [`config/twonr9_adaptive_keys_bugwind.h`](../config/twonr9_adaptive_keys_bugwind.h) and [`config/twonr9_adaptive_keys_srht.h`](../config/twonr9_adaptive_keys_srht.h) (shared generators in `config/twonr9_adaptive.h`). See [`config/DOCUMENTATION.md`](../config/DOCUMENTATION.md) §4.E.

2. **Bigram Chords (srht)**:
   * `a1`: `RL` · `HN` · `DT` · `CY` · `EO` · `UI`
   * `a2`: `RM` · `NB` · `KT` · `GY` · `OE` · `IU`

### Bigram Chords (bugwind)

   * `a1`: `RL` · `KT` · `MB` · `YS` · `EO` · `UI`
   * `a2`: `RW` · `MT` · `SCH` · `GS` · `OE` · `IU`

Each chord is a **vertical pair across the same column** (e.g. `0 + 7`, `1 + 8`, …), so they land under the finger that would otherwise produce the awkward roll.
