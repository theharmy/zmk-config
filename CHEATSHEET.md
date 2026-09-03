# TwoNr9 (18-Key Split) Keyboard Cheatsheet & Usability Guide

> **Visual Infographic:** View [`draw/twonr9_cheatsheet.svg`](draw/twonr9_cheatsheet.svg) for the all-in-one visual card reference.

---

## 1. Combined Layout & Combo Map

<img src="./draw/twonr9_combined_overview.svg" alt="TwoNr9 Combined Keymap & Combos" width="100%" />

---

## 2. Four-Corner Sub-Layer Legends

Each finger key on the overview diagram displays 4 color-coded sub-legends corresponding to sub-layers:

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
| **Top-Left (`tl`)** | **Cyan (`#458588`)** | **`sym`** | 14 Dual Mod-Morph Symbol Pairs (`( <`, `) >`, `[ {`, `] }`, `; '`, `: "`, `/ \`, etc.) |
| **Top-Right (`tr`)** | **Yellow (`#d79921`)** | **`nav`** | Clustered Arrows `← ↓ ↑ →`, Niri Ops `⌘Q ⌘⇥ ⌘R ⇹`, Workspaces `⌘⇞ ⌘⇟`, Jumps `↖ ↘` |
| **Bottom-Left (`bl`)** | **Orange (`#d65d0e`)** | **`num`** | 3x3 Calculator Numpad (`4 5 6` top, `1 2 3 0` home, `. / ,` decimal morph, `7 8 9` chords) |
| **Bottom-Right (`br`)** | **Green (`#689d6a`)** | **`fn`** | Function Keys `F1`–`F12` & Volume Controls `V-`, `V+` |

---

## 3. Symmetrical Home-Row Layer Access (Base `a1`)

```text
                  LEFT HAND                                   RIGHT HAND
        ╭──────┬──────┬──────┬──────╮               ╭──────┬──────┬──────┬──────╮
Key     │  6   │  7   │  8   │  9   │               │  10  │  11  │  12  │  13  │
Letter  │  S   │  R   │  H   │  T   │               │  C   │  E   │  I   │  A   │
        ├──────┼──────┼──────┼──────┤               ├──────┼──────┼──────┼──────┤
Hold    │  ⌃   │  fn  │ nav  │ sym  │               │ sym  │ nav  │  fn  │  ⌃   │
        ╰──────┴──────┴──────┴──────╯               ╰──────┴──────┴──────┴──────╯
        Pinky   Ring  Middle  Index                 Index  Middle  Ring   Pinky
```

* **Index (`T` on 9, `C` on 10)**: Hold $\rightarrow$ **`sym` layer** (14 mod-morph brackets, quotes, slashes, logic).
* **Middle (`H` on 8, `E` on 11)**: Hold $\rightarrow$ **`nav` layer** (Niri window controls, clustered arrows, workspaces).
* **Ring (`R` on 7, `I` on 12)**: Hold $\rightarrow$ **`fn` layer** (`F1`–`F12`, volume controls).
* **Pinky (`S` on 6, `A` on 13)**: Hold $\rightarrow$ **`⌃` (Control)**.

---

## 4. Symmetrical Adaptive Thumb Engine

```text
                  LEFT THUMBS                                 RIGHT THUMBS
          ╭──────────────┬──────────────╮             ╭──────────────┬──────────────╮
          │   Thumb 14   │   Thumb 15   │             │   Thumb 16   │   Thumb 17   │
          │   (Outer)    │   (Inner)    │             │   (Inner)    │   (Outer)    │
          ├──────────────┼──────────────┤             ├──────────────┼──────────────┤
          │    A2 DUAL   │  SPACE / NAV │             │ MAGIC_SHIFT  │  SMART_NUM   │
          ╰──────────────┴──────────────╯             ╰──────────────┴──────────────╯
```

| Thumb Key | Position | Single Tap | Hold Action | Context / Special Feature |
| :--- | :---: | :--- | :--- | :--- |
| **Left Outer (14)** | `14` | **Sticky `a2`** (1 letter) | **Continuous `a2`** | Hold to type secondary words (*BMW*, *Quiz*, *Pflanze*) |
| **Left Inner (15)** | `15` | **`Space`** | **`nav` Layer** | Shift + Tap outputs `. ` (period + space) & arms Sticky Shift |
| **Right Inner (16)** | `16` | **`Repeat` / `Sticky Shift`** | **Continuous Shift** | After char = **Repeat** (*tt, ee, ll*); On pause = **Sticky Shift**; S-Tap = **`⇪` Caps** |
| **Right Outer (17)** | `17` | **`num_word`** | **Momentary `num`** | Auto-exits number mode when pressing Space, Enter, or alphas |

---

## 5. Layer 2: Navigation & Niri Suite (`nav`)

Access via Left Inner Thumb (15) or Home Middle Fingers (`H` / `E`):

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
| **`3`** | **`NAV_LEFT`** | **`←`** | **`Home`** (Start of line / First Column) |
| **`4`** | **`NAV_DOWN`** | **`↓`** | **`Ctrl + End`** (Bottom of document / buffer) |
| **`5`** | **`NAV_UP`** | **`↑`** | **`Ctrl + Home`** (Top of document / buffer) |
| **`13`** | **`NAV_RIGHT`** | **`→`** | **`End`** (End of line / Last Column) |
| **`10`** | **`&swapper` (`⇹`)** | **Alt+Tab** | Smooth window cycling in Niri |
| **`11`** | **`NAV_PGDN`** | **`PgDn` (`⇟`)** | **`⌘⇟` (`Super + PgDn`)** $\rightarrow$ **Next Niri Workspace** |
| **`12`** | **`NAV_PGUP`** | **`PgUp` (`⇞`)** | **`⌘⇞` (`Super + PgUp`)** $\rightarrow$ **Previous Niri Workspace** |

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
| `combo_sz` | `6 + 7` | **`ß`** (Eszett) | Fast `S + R` pinch on base for German words (*Straße*, *groß*, *weiß*) |
| `combo_under` | `7 + 8` | **`_`** (Underscore) | Instant typing of `snake_case` variables and function names |
| `combo_minus` | `8 + 9` | **`-`** (Minus) | Hyphenation, negative values, and CLI flags (`--flag`, `-v`) |
| `combo_colon` | `10 + 11` | **`:`** (Colon) | Rust `::` namespace pathing, Python defs & JSON key-value pairs |
| `combo_semi` | `11 + 12` | **`;`** (Semicolon) | Statement terminator for C, Rust, TypeScript, Java |

### System & Numpad Shortcuts
| Combo | Keys | Output | Why it's useful / Benefits |
| :--- | :---: | :---: | :--- |
| `combo_caps` | `14 + 15` | **`⇪`** (Caps Word) | Type `UPPERCASE_CONSTANTS` (automatically turns off on Space/Enter) |
| `combo_stdio` | `7 + 8 + 9` | **`🔓`** (Studio Unlock) | Unlocks live ZMK Studio key remapping (on `sym` layer, offset bottom) |
| `combo_7, 8, 9` | `3+10`, `4+11`, `5+12` | **`7` `8` `9`** | Vertical chords on `num` layer to hit top-row calculator digits |

---

## 7. Complete 14-Pair Mod-Morph Symbol System (`sym` Layer)

Access `sym` by holding Left Index **`T`** (Key 9) or Right Index **`C`** (Key 10):

| Key Position | Primary (Tap) | Shift + Tap (Morph) | Category & Coding Relevance |
| :--- | :---: | :---: | :--- |
| **Key 3** (Right Col 1 Top) | **`(`** | **`<`** | Function calls `foo()`, generics `<T>`, HTML tags |
| **Key 4** (Right Col 2 Top) | **`)`** | **`>`** | Closing parentheses & angle brackets |
| **Key 10** (Right Col 1 Home) | **`[`** | **`{`** | Array indices `arr[0]`, JSON & code blocks `{` |
| **Key 11** (Right Col 2 Home) | **`]`** | **`}`** | Closing array brackets & code blocks `}` |
| **Key 5** (Right Col 3 Top) | **`;`** | **`'`** | Statement terminators `;`, character literals `'c'` (matches `,` on `a2`) |
| **Key 12** (Right Col 3 Home) | **`:`** | **`"`** | Dict keys, Python defs, string literals `"..."` (matches `.` on `a2`) |
| **Key 13** (Right Pinky) | **`/`** | **`\`** | File paths `a/b`, comments `//`, escape codes `\n`, regex |
| **Key 0** (Left Col 1 Top) | **`!`** | **`?`** | Logical NOT `!`, ternary `? :`, nullable types `T?` |
| **Key 1** (Left Col 2 Top) | **`#`** | **`~`** | Preprocessor `#define`, home directory `~/` |
| **Key 2** (Left Col 3 Top) | **`$`** | **`€`** | Shell variables `$VAR`, Euro currency `€` |
| **Key 6** (Left Pinky) | **`` ` ``** | **`^`** | Code fences ``` `...` ```, regex line-start `^`, XOR |
| **Key 7** (Left Col 1 Home) | **`_`** | **`-`** | `snake_case` identifiers, subtraction `-`, CLI flags |
| **Key 8** (Left Col 2 Home) | **`&`** | **`@`** | References `&var`, logical AND `&&`, Python `@decorators` |
| **Key 9** (Left Col 3 Home) | **`\|`** | **`=`** | Shell pipes `a \| b`, logical OR `\|\|`, assignment `=` |

---

## 8. Speed & Flow Patterns

1. **Noun Capitalization (*"Das Haus"*)**:
   $$\text{Space (15)} \longrightarrow \text{Sticky Shift (16)} \longrightarrow \text{H (Letter)}$$
   *Shift arms for 1 letter and auto-disarms instantly.*

2. **Double Letters (*"Schifffahrt", "Bitte"*)**:
   $$\text{Letter (t)} \longrightarrow \text{Thumb 16 (Repeat)} \longrightarrow \text{Instant second 't'}$$

3. **German Eszett (*"Straße", "groß"*)**:
   $$\text{Pinch Keys 6 + 7 (S + R on base)} \longrightarrow \text{Instant 'ß'}$$

4. **Secondary Alphas (*"BMW", "Quiz"*)**:
   $$\text{Tap 14 (1 letter)} \quad\text{or}\quad \text{Hold 14 (continuous words)}$$

5. **Niri Window Management**:
   $$\text{Hold 15 / H / E} \longrightarrow \text{⌘Q (Close), ⌘⇥ (Overview), ⌘R (Width), ⇹ (Swapper), ⌘⇞/⌘⇟ (Workspaces)}$$
