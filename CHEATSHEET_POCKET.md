# 2nr9 · pocket card

*18 keys · DE QWERTZ · Niri · bugwind (the default keymap)*

> srht backup differs in the grids, bigrams & ß chord and adds adaptive keys — see [`CHEATSHEET.md`](CHEATSHEET.md) §9.

## Base `a1` — top row = layer-taps, home row = mods

```text
              ╭────────┬────────┬────────╮      ╭────────┬────────┬────────╮
              │ L  fn  │ M  nav │ D  sym │      │ Y  sym │ O  nav │ U  fn  │
       ╭──────┼────────┼────────┼────────┤      ├────────┼────────┼────────┼──────╮
       │ N  ⌃ │ R  ⌥   │ T  ⌘   │ H  ⇧   │      │ S  ⇧   │ A  ⌘   │ I  ⌥   │ E  ⌃  │
       ╰──────┴────────┼────────┼────────┤      ├────────┼────────┼────────┴──────╯
                       │  num   │  a2 ⇄  │      │  spc   │  sym   │
                       ╰────────┴────────╯      ╰────────┴────────╯
```
*home row reads `⌃ ⌥ ⌘ ⇧` outwards on the left, `⇧ ⌘ ⌥ ⌃` outwards on the right*

## `a2` — the other 12 letters (tap or hold thumb 15)

```text
              │ X  fn  │ V  nav │ B  sym │      │ G  sym │ Q  nav │  ,  fn │
       │ P  ⌃ │ W  ⌥   │ K  ⌘   │ F  ⇧   │      │ C  ⇧   │ Z  ⌘   │  .  ⌥  │ J  ⌃  │
```
*BMW · Quiz · Pflanze · Kaffee — hold 15 and type like normal*

## Thumbs

| | tap | hold | special |
|---|---|---|---|
| **14** | `num_word` (auto-exits!) | `num` layer | — |
| **15** | 1 letter of `a2` | stay in `a2` | — |
| **16** | space | `nav` | shift+tap → `. ` + auto-shift |
| **17** | 1 symbol of `sym` | stay in `sym` | — |

**Magic shift** is *not* a thumb — it is the `8+9` (left) or `10+11` (right) combo, on every layer:
just typed something → **repeat it** (`ee`, `ll`, `::`, `==`, `11`); paused a moment → **sticky shift** for the next letter (*Das Haus*); hold → ⇧; shift+tap → `⇪` Caps Word.

## Bigrams — one vertical pinch = one digraph

Chords run down a **column pair**, so they land under the finger that would otherwise make the awkward roll.

```text
 a1:  0+7 RL   1+8 KT   2+9 MB   3+10 YS   4+11 EO   5+12 UI
 a2:  0+7 RW   1+8 MT   2+9 SCH  3+10 GS   4+11 OE   5+12 IU
```

## Combos worth memorizing

```text
 0+1 ⇥        1+2 ⏎        3+4 ⌫/⌦ (⇧=del)   4+5 ⌃⌫ word-del   3+4+5 ⎋
 6+7 ß        7+9 _        7+8 -             11+12 :           10+12 ;
14+15 ⇪ caps-word    8+9 / 10+11 magic-shift    7+8+9 🔓 studio unlock (on sym)
```

## `nav` in one breath

`←↓↑→` clustered (long-press = jump to first/last column, top/bottom of document) · `⌘Q` close · `⌘⇥` overview · `⌘R` cycles column width · `⇹` window swapper · hold `⇞⇟` = next/prev workspace · `⌥ ⌘ ⇧ ⌃` one-shot mods.
