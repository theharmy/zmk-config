# TwoNr9 srht — Chord-Praxis (Monkeytype)

Stufen nach Modifier-Zuständen: erst die Paare, dann je ein Zustand dazu, dann die Bigramme und Wörter. Jede Stufe enthält alles aus den vorigen; die Remixe mischen Zustände und Wörter neu. Die Chords werden aus Firmware und Zeichnung gelesen, nicht von Hand gepflegt.

## Nutzung in Monkeytype

1. Den Block der Stufe kopieren (Code-Block, unter 10.000 Zeichen).
2. Monkeytype → Test Type **Custom** → Text einfügen.
3. Erst zur nächsten Stufe, wenn die aktuelle sauber läuft. Die Remixe gehen nach Stufe 10.

## Legende

### Stufen

| Stufe | Name | Was er übt | Tokens |
| --- | --- | --- | --- |
| 1 | Plain | 18 Paare ohne Modifier | 18 |
| 2 | + Shift | Shift-Zustände (gegenüberliegender Zeigefinger) | 33 |
| 3 | + Ctrl | Ctrl-Zustände (gegenüberliegender kleiner Finger) | 51 |
| 4 | + Cmd | Cmd-Zustände (gegenüberliegender Mittelfinger) | 69 |
| 5 | + Alt | Alt-Zustände (gegenüberliegender Ringfinger) | 81 |
| 6 | + Quad | Shift + Cmd, vier Tasten | 82 |
| 7 | + a1-Bigramme | a1-Bigramme, Umlaute, ´, Wörter ohne Bigram-Paare | 157 |
| 8 | + a2-Bigramme | a2-Bigramme (Layerwechsel mitten im Wort), a1-Wörter | 256 |
| 9 | Wörter | alles im Tipp-Kontext (114 Wörter) | 114 |
| 10 | Vollpass | jeder Token einmal (Abschluss) | 213 |
| R1 | Remix Operatoren | Ctrl-, Cmd-, Alt- und Quad-Zustände mit Wörtern gemischt | 113 |
| R2 | Remix Symbole | Einzel-Chords und Bigramme, ohne Wörter | 50 |

### Chords nach Paar

| Paar | Plain | + Shift | + Ctrl | + Cmd | + Alt | Quad |
| --- | --- | --- | --- | --- | --- | --- |
| L + S | `/` | — | `//` | `/*` | `*/` | — |
| L + H | `-` | `_` | `--` | `++` | — | — |
| L + T | `&` | `\|` | `&&` | `\|\|` | `&=` | — |
| N + S | `[` | `]` | `\[` | `\]` | `[[` | — |
| N + R | `{` | `}` | `\{` | `\}` | `->` | — |
| N + T | `(` | `)` | `==` | `!=` | — | — |
| D + S | `$` | `^` | `$$` | `\_` | `\$` | — |
| D + R | `"` | `'` | `""` | `''` | — | — |
| D + H | `<` | `>` | `<<` | `>>` | `<=` | `>=` |
| Y + E | `,` | `.` | `...` | `..` | `..<` | — |
| Y + I | `=` | `+` | `+=` | `-=` | `\|=` | — |
| Y + A | `!` | `?` | `?.` | `!!` | `!?` | — |
| O + C | `;` | `:` | `::` | `?:` | `;;` | — |
| O + I | `*` | `#` | `**` | `##` | `^=` | — |
| O + A | `@` | `~` | `~~` | `\#` | `€` | — |
| U + C | `\` | `\(` | `\\` | `\)` | — | — |
| U + E | `` ` `` | — | `` `` `` | `` ``` `` | — | — |
| U + A | `%` | — | `\%` | `\&` | — | — |

### Bigramme

| Layer | Chords |
| --- | --- |
| a1 | rl · hn · dt · cy · eo · ui |
| a2 | rm · nb · kt · gy · oe · iu |

### Deutsche Buchstaben

| Chord | Output |
| --- | --- |
| C + Spc | `ß` |
| A + Spc | `ä` |
| O + Spc | `ö` |
| U + Spc | `ü` |
| S + R | `´` |

### Wörter

**Stufe 7**, ohne Bigram-Paare: Haus, Maus, Hund, Kind, Wind, Hand, Nacht, Licht, Wasser, Baum, Apfel, Vogel, Wolke, Fenster, Buch, Bett, Morgen, Glas, Wiese, Tanne, Symbol, Kombi, Amboss, Kombination, umbringt, System, Systeme, Analyse, erwartet, erwartung, erwachsene, erwache, Amt, Amtsstube, Amtsblatt, amtieren, Schule, Maschine, schreiben, Schrift, Schritt, bags, dogs, tags, flags, mugs, bugs

**Stufe 8**, a1-Bigramme: erleben, erlöst, erlitten, erlaubt, Erlösung, Sohn, Kahn, Hahn, Mohn, wohnen, Landtag, verwandt, Handtuch, Bicycle, Cyclist, Cyber, Geometrie, beobachten, Beobachtung, Geometer, eons, eosin, Ruine, Ruinen, build, suit, suitable, juice, guide

**Stufe 9**, a2-Bigramme (Layerwechsel): Norm, Formel, warm, Wärme, Anbau, Einbau, anbei, aktuell, Diktat, Diktatur, Kontakt, Kaktus, Gymnasium, Biology, Energy, Koeffizient, Koexistenz, Koeln, Iulius, Iunius, equinoctium

### Adaptive Keys (9, nur srht)

Innerhalb von 300 ms nach dem Trigger gibt ein adaptiver Key den Partner aus — schnelles `rh` kann als `rl` herauskommen. Die Chords (beide Tasten gleichzeitig) sind nicht betroffen.

## Stufe 1 — Plain (116 Runden · 2088 Tokens · 4175 Zeichen)

```
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
- \ / , & $ ` % { (
* [ = < ! @ " ;
```

## Stufe 2 — + Shift (62 Runden · 2046 Tokens · 4153 Zeichen)

```
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
& . @ [ ] * - : | ~
? _ > ' { = ! / \ <
^ # + ; \( ) " % $ ,
} ` (
```

## Stufe 3 — + Ctrl (34 Runden · 1734 Tokens · 4147 Zeichen)

```
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
~~ / \ && == :: $$ = ) .
# , & $ << - ... ~ + '
\{ ( ?. "" ; ** _ \( `` "
^ * | [ > { % ! } `
+= @ \[ -- // ? ] \% \\ :
<
```

## Stufe 4 — + Cmd (23 Runden · 1587 Tokens · 4070 Zeichen)

```
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
/* : .. ' \# \ [ \_ !! ?
\} + == @ _ ++ :: << - ##
# " ?. `` ( // , \\ ~ \&
** > ! . ^ & \% ... = |
\{ < || \( "" -- ) { += >>
``` $ ?: * ; / ` } \) &&
] % \[ -= '' ~~ != \] $$
```

## Stufe 5 — + Alt (19 Runden · 1539 Tokens · 4046 Zeichen)

```
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
# << :: € ... == / "" ** _
> ~~ |= . ! ## += ..< \$ &&
!! .. ;; `` \} <= ; '' &= ]
!= ` \_ ++ \\ ^ ?: | [[ [
@ $ /* : & */ \[ ? \] //
) -> -= - $$ } " \ < \(
, ~ ' ( \& -- ^= !? \% *
?. || \) \# \{ = ``` % { >>
+
```

## Stufe 6 — + Quad (19 Runden · 1558 Tokens · 4103 Zeichen)

```
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
~ [[ ] \] > \ \( : / =
"" ^ $ . # += != \_ :: ..<
'' ++ << .. [ -> /* >> + `
\# &= ... * _ ?: `` ``` \[ (
## |= $$ \$ { -= ^= !? !! ,
*/ || ** \) >= % < ' // }
<= @ == && \{ € ?. \} | --
! \& - ; ;; " ) & ? ~~
\% \\
```

## Stufe 7 — + a1-Bigramme (6 Runden · 942 Tokens · 4037 Zeichen)

```
>= erwache : != Amt eo < ^= Analyse \)
! Apfel > umbringt erwachsene [ !? ^ ' ```
Nacht // ?: flags heiß $$ \{ Hund \\ Buch
schön erwartung ** ## größer Amtsblatt Vögel = Wiese während
/ ? Baum .. , . ` Wind Systeme Wasser
tags Müde ..< & ++ \$ Schritt dogs ´ >>
Wolke ... Mädchen << * { Morgen && /* Vogel
Hüpfen ( '' Kombination Straße += # bags _ rl
Schrift | !! $ Maus \] grüßen Amboss == Höhlen
\( || } hn Symbol Küche Käse \} -= ~
ui erwartet \# Amtsstube :: \_ Kind `` - [[
amtieren ä Licht € @ \& <= cy mugs ö
Haus Glas Tanne ~~ "" ] -> \[ Maschine Hände
bugs -- + Hütte System Kombi |= */ ; "
Küsse Fenster Hand ß ;; &= % \ Schule Höfe
dt \% schreiben ) ?. ü Bett
>= erwache : != Amt eo < ^= Analyse \)
! Apfel > umbringt erwachsene [ !? ^ ' ```
Nacht // ?: flags heiß $$ \{ Hund \\ Buch
schön erwartung ** ## größer Amtsblatt Vögel = Wiese während
/ ? Baum .. , . ` Wind Systeme Wasser
tags Müde ..< & ++ \$ Schritt dogs ´ >>
Wolke ... Mädchen << * { Morgen && /* Vogel
Hüpfen ( '' Kombination Straße += # bags _ rl
Schrift | !! $ Maus \] grüßen Amboss == Höhlen
\( || } hn Symbol Küche Käse \} -= ~
ui erwartet \# Amtsstube :: \_ Kind `` - [[
amtieren ä Licht € @ \& <= cy mugs ö
Haus Glas Tanne ~~ "" ] -> \[ Maschine Hände
bugs -- + Hütte System Kombi |= */ ; "
Küsse Fenster Hand ß ;; &= % \ Schule Höfe
dt \% schreiben ) ?. ü Bett
>= erwache : != Amt eo < ^= Analyse \)
! Apfel > umbringt erwachsene [ !? ^ ' ```
Nacht // ?: flags heiß $$ \{ Hund \\ Buch
schön erwartung ** ## größer Amtsblatt Vögel = Wiese während
/ ? Baum .. , . ` Wind Systeme Wasser
tags Müde ..< & ++ \$ Schritt dogs ´ >>
Wolke ... Mädchen << * { Morgen && /* Vogel
Hüpfen ( '' Kombination Straße += # bags _ rl
Schrift | !! $ Maus \] grüßen Amboss == Höhlen
\( || } hn Symbol Küche Käse \} -= ~
ui erwartet \# Amtsstube :: \_ Kind `` - [[
amtieren ä Licht € @ \& <= cy mugs ö
Haus Glas Tanne ~~ "" ] -> \[ Maschine Hände
bugs -- + Hütte System Kombi |= */ ; "
Küsse Fenster Hand ß ;; &= % \ Schule Höfe
dt \% schreiben ) ?. ü Bett
>= erwache : != Amt eo < ^= Analyse \)
! Apfel > umbringt erwachsene [ !? ^ ' ```
Nacht // ?: flags heiß $$ \{ Hund \\ Buch
schön erwartung ** ## größer Amtsblatt Vögel = Wiese während
/ ? Baum .. , . ` Wind Systeme Wasser
tags Müde ..< & ++ \$ Schritt dogs ´ >>
Wolke ... Mädchen << * { Morgen && /* Vogel
Hüpfen ( '' Kombination Straße += # bags _ rl
Schrift | !! $ Maus \] grüßen Amboss == Höhlen
\( || } hn Symbol Küche Käse \} -= ~
ui erwartet \# Amtsstube :: \_ Kind `` - [[
amtieren ä Licht € @ \& <= cy mugs ö
Haus Glas Tanne ~~ "" ] -> \[ Maschine Hände
bugs -- + Hütte System Kombi |= */ ; "
Küsse Fenster Hand ß ;; &= % \ Schule Höfe
dt \% schreiben ) ?. ü Bett
>= erwache : != Amt eo < ^= Analyse \)
! Apfel > umbringt erwachsene [ !? ^ ' ```
Nacht // ?: flags heiß $$ \{ Hund \\ Buch
schön erwartung ** ## größer Amtsblatt Vögel = Wiese während
/ ? Baum .. , . ` Wind Systeme Wasser
tags Müde ..< & ++ \$ Schritt dogs ´ >>
Wolke ... Mädchen << * { Morgen && /* Vogel
Hüpfen ( '' Kombination Straße += # bags _ rl
Schrift | !! $ Maus \] grüßen Amboss == Höhlen
\( || } hn Symbol Küche Käse \} -= ~
ui erwartet \# Amtsstube :: \_ Kind `` - [[
amtieren ä Licht € @ \& <= cy mugs ö
Haus Glas Tanne ~~ "" ] -> \[ Maschine Hände
bugs -- + Hütte System Kombi |= */ ; "
Küsse Fenster Hand ß ;; &= % \ Schule Höfe
dt \% schreiben ) ?. ü Bett
>= erwache : != Amt eo < ^= Analyse \)
! Apfel > umbringt erwachsene [ !? ^ ' ```
Nacht // ?: flags heiß $$ \{ Hund \\ Buch
schön erwartung ** ## größer Amtsblatt Vögel = Wiese während
/ ? Baum .. , . ` Wind Systeme Wasser
tags Müde ..< & ++ \$ Schritt dogs ´ >>
Wolke ... Mädchen << * { Morgen && /* Vogel
Hüpfen ( '' Kombination Straße += # bags _ rl
Schrift | !! $ Maus \] grüßen Amboss == Höhlen
\( || } hn Symbol Küche Käse \} -= ~
ui erwartet \# Amtsstube :: \_ Kind `` - [[
amtieren ä Licht € @ \& <= cy mugs ö
Haus Glas Tanne ~~ "" ] -> \[ Maschine Hände
bugs -- + Hütte System Kombi |= */ ; "
Küsse Fenster Hand ß ;; &= % \ Schule Höfe
dt \% schreiben ) ?. ü Bett
```

## Stufe 8 — + a2-Bigramme (3 Runden · 768 Tokens · 4001 Zeichen)

```
Glas Küche Wasser Schule Müde Mohn Symbol gy erwartet Systeme
/ Nacht Bett Morgen nb heiß Straße heiß ^= Höfe
€ ü [ dogs eosin bugs beobachten Mädchen Erlösung Amtsblatt
Haus Hände verwandt Nacht /* eo Küsse juice ``` Hüpfen
Amtsblatt Höhlen , Maschine schön ? Amboss Amboss Hund ...
größer umbringt \# Wolke ] ö Schrift Apfel \ \}
Kind wohnen Kombi erwache Höhlen Tanne Cyclist \) :: ->
bags Kombination grüßen Kombi suit Maschine ~~ > build Höfe
!? Ruinen += Wiese ` Bett ~ @ \\ mugs
erwache Beobachtung flags ; == " Buch Wind Schrift ##
Käse Küsse System mugs Bicycle >= .. Haus schön Vögel
Analyse rl erleben \_ & erlaubt $$ Schritt Hahn Vogel
[[ \{ \& Fenster * ' flags Sohn ) >>
oe Tanne \[ amtieren bugs : !! Ruine Geometrie erwachsene
;; ** Licht iu Amt \% kt Mädchen Wind erlöst
Cyber Licht -- Straße Hand = -= erwartung Handtuch amtieren
Hände { Wolke ++ != ^ Baum ! Vogel _
|= Amtsstube \( Systeme ?. // schreiben <= `` .
Hund ui # umbringt ?: Hütte Hütte Geometer eons Amtsstube
+ während Maus Vögel Buch << tags guide erwartet Maus
- \] rm */ Küche Käse bags &= Wiese ä
( Morgen Fenster Landtag dogs erlitten Glas Hand < grüßen
Kind Wasser ´ ß '' erwachsene % Kahn hn $
\$ Baum ..< Symbol während && Hüpfen dt Schule Analyse
| Amt tags cy Müde "" Apfel Kombination || suitable
Schritt } erwartung größer schreiben System
Glas Küche Wasser Schule Müde Mohn Symbol gy erwartet Systeme
/ Nacht Bett Morgen nb heiß Straße heiß ^= Höfe
€ ü [ dogs eosin bugs beobachten Mädchen Erlösung Amtsblatt
Haus Hände verwandt Nacht /* eo Küsse juice ``` Hüpfen
Amtsblatt Höhlen , Maschine schön ? Amboss Amboss Hund ...
größer umbringt \# Wolke ] ö Schrift Apfel \ \}
Kind wohnen Kombi erwache Höhlen Tanne Cyclist \) :: ->
bags Kombination grüßen Kombi suit Maschine ~~ > build Höfe
!? Ruinen += Wiese ` Bett ~ @ \\ mugs
erwache Beobachtung flags ; == " Buch Wind Schrift ##
Käse Küsse System mugs Bicycle >= .. Haus schön Vögel
Analyse rl erleben \_ & erlaubt $$ Schritt Hahn Vogel
[[ \{ \& Fenster * ' flags Sohn ) >>
oe Tanne \[ amtieren bugs : !! Ruine Geometrie erwachsene
;; ** Licht iu Amt \% kt Mädchen Wind erlöst
Cyber Licht -- Straße Hand = -= erwartung Handtuch amtieren
Hände { Wolke ++ != ^ Baum ! Vogel _
|= Amtsstube \( Systeme ?. // schreiben <= `` .
Hund ui # umbringt ?: Hütte Hütte Geometer eons Amtsstube
+ während Maus Vögel Buch << tags guide erwartet Maus
- \] rm */ Küche Käse bags &= Wiese ä
( Morgen Fenster Landtag dogs erlitten Glas Hand < grüßen
Kind Wasser ´ ß '' erwachsene % Kahn hn $
\$ Baum ..< Symbol während && Hüpfen dt Schule Analyse
| Amt tags cy Müde "" Apfel Kombination || suitable
Schritt } erwartung größer schreiben System
Glas Küche Wasser Schule Müde Mohn Symbol gy erwartet Systeme
/ Nacht Bett Morgen nb heiß Straße heiß ^= Höfe
€ ü [ dogs eosin bugs beobachten Mädchen Erlösung Amtsblatt
Haus Hände verwandt Nacht /* eo Küsse juice ``` Hüpfen
Amtsblatt Höhlen , Maschine schön ? Amboss Amboss Hund ...
größer umbringt \# Wolke ] ö Schrift Apfel \ \}
Kind wohnen Kombi erwache Höhlen Tanne Cyclist \) :: ->
bags Kombination grüßen Kombi suit Maschine ~~ > build Höfe
!? Ruinen += Wiese ` Bett ~ @ \\ mugs
erwache Beobachtung flags ; == " Buch Wind Schrift ##
Käse Küsse System mugs Bicycle >= .. Haus schön Vögel
Analyse rl erleben \_ & erlaubt $$ Schritt Hahn Vogel
[[ \{ \& Fenster * ' flags Sohn ) >>
oe Tanne \[ amtieren bugs : !! Ruine Geometrie erwachsene
;; ** Licht iu Amt \% kt Mädchen Wind erlöst
Cyber Licht -- Straße Hand = -= erwartung Handtuch amtieren
Hände { Wolke ++ != ^ Baum ! Vogel _
|= Amtsstube \( Systeme ?. // schreiben <= `` .
Hund ui # umbringt ?: Hütte Hütte Geometer eons Amtsstube
+ während Maus Vögel Buch << tags guide erwartet Maus
- \] rm */ Küche Käse bags &= Wiese ä
( Morgen Fenster Landtag dogs erlitten Glas Hand < grüßen
Kind Wasser ´ ß '' erwachsene % Kahn hn $
\$ Baum ..< Symbol während && Hüpfen dt Schule Analyse
| Amt tags cy Müde "" Apfel Kombination || suitable
Schritt } erwartung größer schreiben System
```

## Stufe 9 — Wörter (5 Runden · 570 Tokens · 4019 Zeichen)

```
Anbau Bicycle Cyber Schritt anbei Iulius Ruinen amtieren Hände Amtsstube
Schule erwartung Analyse schreiben Apfel erwachsene während Symbol Kombi Koeln
bugs Hand mugs bags Nacht Gymnasium Hüpfen erleben Energy Wärme
Licht wohnen suitable suit Vogel Morgen Diktatur Formel Schrift Amt
heiß Haus Mohn Geometrie beobachten Ruine Cyclist Käse Kontakt Geometer
erlaubt Wolke Kind Wiese flags Müde Mädchen verwandt Koeffizient Kombination
Biology System Amtsblatt Iunius Maus Straße Systeme build Fenster Einbau
Beobachtung Buch eosin Glas dogs Hütte warm Höfe erwartet größer
tags erlöst Baum Kaktus Amboss Landtag Handtuch Küche Maschine Hund
eons Diktat Norm Höhlen Tanne guide Erlösung Wasser Bett umbringt
Vögel Wind erlitten Koexistenz Sohn grüßen schön equinoctium Kahn aktuell
erwache Hahn Küsse juice
Anbau Bicycle Cyber Schritt anbei Iulius Ruinen amtieren Hände Amtsstube
Schule erwartung Analyse schreiben Apfel erwachsene während Symbol Kombi Koeln
bugs Hand mugs bags Nacht Gymnasium Hüpfen erleben Energy Wärme
Licht wohnen suitable suit Vogel Morgen Diktatur Formel Schrift Amt
heiß Haus Mohn Geometrie beobachten Ruine Cyclist Käse Kontakt Geometer
erlaubt Wolke Kind Wiese flags Müde Mädchen verwandt Koeffizient Kombination
Biology System Amtsblatt Iunius Maus Straße Systeme build Fenster Einbau
Beobachtung Buch eosin Glas dogs Hütte warm Höfe erwartet größer
tags erlöst Baum Kaktus Amboss Landtag Handtuch Küche Maschine Hund
eons Diktat Norm Höhlen Tanne guide Erlösung Wasser Bett umbringt
Vögel Wind erlitten Koexistenz Sohn grüßen schön equinoctium Kahn aktuell
erwache Hahn Küsse juice
Anbau Bicycle Cyber Schritt anbei Iulius Ruinen amtieren Hände Amtsstube
Schule erwartung Analyse schreiben Apfel erwachsene während Symbol Kombi Koeln
bugs Hand mugs bags Nacht Gymnasium Hüpfen erleben Energy Wärme
Licht wohnen suitable suit Vogel Morgen Diktatur Formel Schrift Amt
heiß Haus Mohn Geometrie beobachten Ruine Cyclist Käse Kontakt Geometer
erlaubt Wolke Kind Wiese flags Müde Mädchen verwandt Koeffizient Kombination
Biology System Amtsblatt Iunius Maus Straße Systeme build Fenster Einbau
Beobachtung Buch eosin Glas dogs Hütte warm Höfe erwartet größer
tags erlöst Baum Kaktus Amboss Landtag Handtuch Küche Maschine Hund
eons Diktat Norm Höhlen Tanne guide Erlösung Wasser Bett umbringt
Vögel Wind erlitten Koexistenz Sohn grüßen schön equinoctium Kahn aktuell
erwache Hahn Küsse juice
Anbau Bicycle Cyber Schritt anbei Iulius Ruinen amtieren Hände Amtsstube
Schule erwartung Analyse schreiben Apfel erwachsene während Symbol Kombi Koeln
bugs Hand mugs bags Nacht Gymnasium Hüpfen erleben Energy Wärme
Licht wohnen suitable suit Vogel Morgen Diktatur Formel Schrift Amt
heiß Haus Mohn Geometrie beobachten Ruine Cyclist Käse Kontakt Geometer
erlaubt Wolke Kind Wiese flags Müde Mädchen verwandt Koeffizient Kombination
Biology System Amtsblatt Iunius Maus Straße Systeme build Fenster Einbau
Beobachtung Buch eosin Glas dogs Hütte warm Höfe erwartet größer
tags erlöst Baum Kaktus Amboss Landtag Handtuch Küche Maschine Hund
eons Diktat Norm Höhlen Tanne guide Erlösung Wasser Bett umbringt
Vögel Wind erlitten Koexistenz Sohn grüßen schön equinoctium Kahn aktuell
erwache Hahn Küsse juice
Anbau Bicycle Cyber Schritt anbei Iulius Ruinen amtieren Hände Amtsstube
Schule erwartung Analyse schreiben Apfel erwachsene während Symbol Kombi Koeln
bugs Hand mugs bags Nacht Gymnasium Hüpfen erleben Energy Wärme
Licht wohnen suitable suit Vogel Morgen Diktatur Formel Schrift Amt
heiß Haus Mohn Geometrie beobachten Ruine Cyclist Käse Kontakt Geometer
erlaubt Wolke Kind Wiese flags Müde Mädchen verwandt Koeffizient Kombination
Biology System Amtsblatt Iunius Maus Straße Systeme build Fenster Einbau
Beobachtung Buch eosin Glas dogs Hütte warm Höfe erwartet größer
tags erlöst Baum Kaktus Amboss Landtag Handtuch Küche Maschine Hund
eons Diktat Norm Höhlen Tanne guide Erlösung Wasser Bett umbringt
Vögel Wind erlitten Koexistenz Sohn grüßen schön equinoctium Kahn aktuell
erwache Hahn Küsse juice
```

## Stufe 10 — Vollpass (3 Runden · 639 Tokens · 3197 Zeichen)

```
rl += ^ \) Licht Nacht & ``` Wiese beobachten
( Baum \ erleben Küche Landtag <= ´ juice Beobachtung
Kombi build Fenster .. \% && -> iu Käse oe
?: Anbau ; */ schön tags / Koeffizient !? ~~
* ~ \{ # ` "" größer gy Cyber ü
= Symbol + Amtsblatt ** Iulius Müde @ Schrift rm
amtieren Ruine Biology -- erwartung Mädchen Maschine :: Einbau suitable
Haus Formel \[ $ -= erwache ui bags Kaktus ##
|= Hund [ umbringt < Schule Wind System Mohn wohnen
Norm Analyse nb Hand Amboss " << eons . eosin
Hände % // während \$ Tanne guide hn Koexistenz ``
\} [[ Iunius ö ß == aktuell erlöst erwachsene Ruinen
Energy Wasser Morgen ' Hütte ) Küsse \# Koeln ?
Apfel kt Kontakt Handtuch Hahn equinoctium Höfe Systeme /* \(
Hüpfen eo _ Cyclist > ;; Erlösung heiß Glas |
Bicycle Vögel mugs Kombination anbei Maus ä \_ Straße grüßen
: cy \\ Höhlen ?. !! Kahn Amt Diktatur erlaubt
\& erwartet schreiben Gymnasium Geometer Wolke erlitten '' Bett {
suit Buch ] Vogel || warm >> } >= \]
€ , Diktat Kind $$ &= ... Schritt Sohn !
Amtsstube verwandt flags Wärme bugs ..< dt != - ^=
Geometrie dogs ++
rl += ^ \) Licht Nacht & ``` Wiese beobachten
( Baum \ erleben Küche Landtag <= ´ juice Beobachtung
Kombi build Fenster .. \% && -> iu Käse oe
?: Anbau ; */ schön tags / Koeffizient !? ~~
* ~ \{ # ` "" größer gy Cyber ü
= Symbol + Amtsblatt ** Iulius Müde @ Schrift rm
amtieren Ruine Biology -- erwartung Mädchen Maschine :: Einbau suitable
Haus Formel \[ $ -= erwache ui bags Kaktus ##
|= Hund [ umbringt < Schule Wind System Mohn wohnen
Norm Analyse nb Hand Amboss " << eons . eosin
Hände % // während \$ Tanne guide hn Koexistenz ``
\} [[ Iunius ö ß == aktuell erlöst erwachsene Ruinen
Energy Wasser Morgen ' Hütte ) Küsse \# Koeln ?
Apfel kt Kontakt Handtuch Hahn equinoctium Höfe Systeme /* \(
Hüpfen eo _ Cyclist > ;; Erlösung heiß Glas |
Bicycle Vögel mugs Kombination anbei Maus ä \_ Straße grüßen
: cy \\ Höhlen ?. !! Kahn Amt Diktatur erlaubt
\& erwartet schreiben Gymnasium Geometer Wolke erlitten '' Bett {
suit Buch ] Vogel || warm >> } >= \]
€ , Diktat Kind $$ &= ... Schritt Sohn !
Amtsstube verwandt flags Wärme bugs ..< dt != - ^=
Geometrie dogs ++
rl += ^ \) Licht Nacht & ``` Wiese beobachten
( Baum \ erleben Küche Landtag <= ´ juice Beobachtung
Kombi build Fenster .. \% && -> iu Käse oe
?: Anbau ; */ schön tags / Koeffizient !? ~~
* ~ \{ # ` "" größer gy Cyber ü
= Symbol + Amtsblatt ** Iulius Müde @ Schrift rm
amtieren Ruine Biology -- erwartung Mädchen Maschine :: Einbau suitable
Haus Formel \[ $ -= erwache ui bags Kaktus ##
|= Hund [ umbringt < Schule Wind System Mohn wohnen
Norm Analyse nb Hand Amboss " << eons . eosin
Hände % // während \$ Tanne guide hn Koexistenz ``
\} [[ Iunius ö ß == aktuell erlöst erwachsene Ruinen
Energy Wasser Morgen ' Hütte ) Küsse \# Koeln ?
Apfel kt Kontakt Handtuch Hahn equinoctium Höfe Systeme /* \(
Hüpfen eo _ Cyclist > ;; Erlösung heiß Glas |
Bicycle Vögel mugs Kombination anbei Maus ä \_ Straße grüßen
: cy \\ Höhlen ?. !! Kahn Amt Diktatur erlaubt
\& erwartet schreiben Gymnasium Geometer Wolke erlitten '' Bett {
suit Buch ] Vogel || warm >> } >= \]
€ , Diktat Kind $$ &= ... Schritt Sohn !
Amtsstube verwandt flags Wärme bugs ..< dt != - ^=
Geometrie dogs ++
```

## Stufe R1 — Remix Operatoren (7 Runden · 791 Tokens · 4045 Zeichen)

```
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
\$ Schule Wolke \& !? \} Straße Küsse \) Vogel
Mädchen >= Kind -- \[ \{ Haus grüßen schreiben amtieren
?: Höhlen Schritt -= Wiese "" :: erwartung Schrift Glas
>> Nacht ^= erwache '' Morgen <= ~~ Symbol Wind
Apfel &= während ..< Kombi << `` Analyse ++ ...
Müde Bett Küche \_ bags Hüpfen \# ** Buch [[
Maus // -> .. && dogs System || $$ Systeme
\] ?. /* Wasser bugs Amtsstube Hand Tanne mugs größer
Amtsblatt schön Maschine !! € erwachsene == Licht Amboss ;;
Hütte |= Hände \% Amt */ Vögel ``` != +=
erwartet Höfe Käse Hund flags ## tags heiß Kombination Fenster
umbringt \\ Baum
```

## Stufe R2 — Remix Symbole (37 Runden · 1850 Tokens · 4180 Zeichen)

```
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
\ % [ cy ? ´ iu + nb }
| & @ ` rm ~ * # $ .
kt \( > / rl " ! ' = hn
^ ; eo ä ö ui _ oe , ü
gy ] ( < - ß dt : ) {
```
