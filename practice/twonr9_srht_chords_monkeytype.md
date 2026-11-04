# TwoNr9 srht — Chord-Praxis (Monkeytype)

Diese Datei enthält ein **Stufen-Übungssystem** für die srht-Keymap — Qualität vor Quantität: 7 aufeinander aufbauende Blöcke, die in der Schwierigkeit steigen (Plain → +Ctrl/+erste Wörter → +a1-Bigrams/+Layer-1-Wörter → +Shift → +a2-Bigrams/+alle Wörter → Wörter → Vollpass). Die Wörter drillen ab Stufe 2 auch das Alpha-Grid: zuerst Wörter ohne Bigram-Paare, dann die, die a1- bzw. a2-Chords brauchen — so wachsen die Wörter mit den Layer-Kenntnissen mit. Jeder Block ist selbstständig (nur sein eigener Pool) und wird Round-Robin gezogen: pro voller Runde kommt jeder Token genau einmal vor, egal an welcher Stelle Monkeytype zufällig ansetzt — jeder Ausschnitt ist gleichmäßig.

Die Chord-Namen folgen dem **srht**-Grid (obere Reihe `L N D Y O U`, Home `S R H T | C E I A`); die Outputs sind identisch mit bugwind, nur die gedrückten Buchstaben wechseln. Zehn der achtzehn Diagonal-Chords heißen daher anders als im bugwind-Praxisblatt.

## Nutzung in Monkeytype

1. Den Block der aktuellen Stufe kopieren (Code-Block, < 10.000 Zeichen).
2. Monkeytype → Test Type **Custom** → Text einfügen.
3. Test-Länge z. B. auf 25–75 Wörter stellen; Monkeytype wählt aus dem Block einen zufälligen Ausschnitt.
4. Erst zur nächsten Stufe wechseln, wenn die aktuelle sauber läuft. Stufe 7 (Vollpass) ist die Abschlussprüfung: jeder Token genau einmal.

Beim Üben auf der TwoNr9 zeigt die Legende unten, welcher Token welchen Chord + Modifier-Zustand triggert. Achtung: die neun adaptiven Keys tauschen bei schnellem Tippen innerhalb von 300 ms Buchstaben — die Legende am Ende erklärt, wann.

## Legende

### Stufen

| Stufe | Block | Was er übt | Pool |
| --- | --- | --- | --- |
| 1 | **Plain** | reines Chord-Gefühl: 18 Plain-Outputs, keine Modifier | 18 Tokens |
| 2 | **Plain + Ctrl + erste Wörter** | Operatoren dazu + allgemeine deutsche Wörter ohne Bigrams (Alpha-Grid übt mit) — immer noch kein Shift | 100 Tokens |
| 3 | **+ a1-Bigrams + Layer-1-Wörter** | a1 komplett: Bigrams + die Wörter, die nur a1-Chords brauchen | 135 Tokens |
| 4 | **Alle Symbole** | Shift-Zustände kommen dazu (+ ´ aus S + R, ß aus C + Space) | 166 Tokens |
| 5 | **+ a2-Bigrams + alle Wörter** | die komplette Keymap: a2-Bigrams (Layerwechsel mitten im Wort) + alle Wörter | 203 Tokens |
| 6 | **Wörter** | alles im echten Tipp-Kontext (114 Wörter) | 114 Tokens |
| 7 | **Vollpass (Abschluss)** | alles in einem Durchgang | 203 Tokens |

### Diagonale Symbol-Chords (16 Chords × 4 Modifier-Zustände = 64 Outputs)

| Chord | Plain | Shift | Ctrl | Ctrl + Shift |
| --- | --- | --- | --- | --- |
| L + S | `(` | `)` | `==` | `!=` |
| Y + E | `}` | `{` | `<=` | `>=` |
| N + R | `[` | `]` | `+=` | `-=` |
| U + A | `)` | `(` | `&=` | `|=` |
| D + H | `{` | `}` | `<<=` | `>>=` |
| O + I | `]` | `[` | `^=` | `*=` |
| N + S | `&` | `*` | `&&` | `||` |
| O + A | `$` | `€` | `??` | `?.` |
| D + R | `~` | `^` | `->` | `=>` |
| Y + I | `=` | `+` | `<<` | `>>` |
| D + S | `<` | `>` | `<=` | `<=` |
| Y + A | `>` | `<` | `>=` | `>=` |
| L + H | `!` | `?` | `//` | `...` |
| N + T | `-` | `_` | `++` | `--` |
| U + E | `;` | `:` | `/*` | `*/` |
| O + C | `'` | `"` | `=` | `|` |
| L + T | `#` | `%` | `::` | `:=` |
| U + C | `/` | `\` | `+` | `@` |

### Deutsche Buchstaben (srht)

| Chord | Output (Shift = Grossbuchstabe) |
| --- | --- |
| C + Space | ß / ẞ |
| A + Space | ä / Ä |
| O + Space | ö / Ö |
| U + Space | ü / Ü |
| S + R | ´ (Shift: `) |

> Die deutschen Buchstaben liegen auf srht an denselben Chord-Positionen wie auf bugwind — nur die gedrückten Buchstaben wechseln mit dem Grid: `ß` ist **C + Space** (10+16; auf bugwind S + Space) und der Akzent `´` steht allein auf **S + R** (6+7; auf bugwind N + R). Die Umlaute (Vokal + Space) sind identisch. Der frühere 6+7-Konflikt zwischen ß und ´ ist damit aufgelöst.

### Bigrams (12)

| Layer | Chords |
| --- | --- |
| a1 | RL · HN · DT · CY · EO · UI |
| a2 | RM · NB · KT · GY · OE · IU |

### Wörter (ab Stufe 2, kumulativ)

**Stufe 2** — ohne Bigram-Paare: Haus, Maus, Hund, Kind, Wind, Hand, Nacht, Licht, Wasser, Baum, Apfel, Vogel, Wolke, Fenster, Buch, Bett, Morgen, Glas, Wiese, Tanne, Symbol, Kombi, Amboss, Kombination, umbringt, System, Systeme, Analyse, erwartet, erwartung, erwachsene, erwache, Amt, Amtsstube, Amtsblatt, amtieren, Schule, Maschine, schreiben, Schrift, Schritt, bags, dogs, tags, flags, mugs, bugs + ß/ä/ö/ü-Wörter: Straße, größer, heiß, Küsse, grüßen, während, Mädchen, Käse, Hände, schön, Höfe, Höhlen, Vögel, Müde, Hütte, Küche, Hüpfen

**Stufe 3** — a1-Bigram-Wörter: erleben, erlöst, erlitten, erlaubt, Erlösung, Sohn, Kahn, Hahn, Mohn, wohnen, Landtag, verwandt, Handtuch, Bicycle, Cyclist, Cyber, Geometrie, beobachten, Beobachtung, Geometer, eons, eosin, Ruine, Ruinen, build, suit, suitable, juice, guide

**Stufe 5** — a2-Bigram-Wörter (Layerwechsel mitten im Wort): Norm, Formel, warm, Wärme, Anbau, Einbau, anbei, aktuell, Diktat, Diktatur, Kontakt, Kaktus, Gymnasium, Biology, Energy, Koeffizient, Koexistenz, Koeln, Iulius, Iunius, equinoctium

### Wörter-Drill: Buchstabenpaar → Chord → Wörter

| Paar | Chord | Wörter |
| --- | --- | --- |
| `rl` | L+R | erleben, erlöst, erlitten, erlaubt, Erlösung |
| `hn` | N+H | Sohn, Kahn, Hahn, Mohn, wohnen |
| `dt` | D+T | Landtag, verwandt, Handtuch |
| `cy` | Y+C | Bicycle, Cyclist, Cyber |
| `eo` | O+E | Geometrie, beobachten, Beobachtung, Geometer, eons, eosin |
| `ui` | U+I | Ruine, Ruinen, build, suit, suitable, juice, guide |
| `rm` | X+M | Norm, Formel, warm, Wärme |
| `nb` | B+P | Anbau, Einbau, anbei |
| `kt` | V+K | aktuell, Diktat, Diktatur, Kontakt, Kaktus |
| `gy` | W+G | Gymnasium, Biology, Energy |
| `oe` | Q+J | Koeffizient, Koexistenz, Koeln |
| `iu` | ,+. | Iulius, Iunius, equinoctium |
| `ß` | C+Space | Straße, größer, heiß, grüßen |
| `ä` | A+Space | während, Mädchen, Käse, Hände |
| `ö` | O+Space | größer, schön, Höfe, Höhlen, Vögel |
| `ü` | U+Space | Küsse, grüßen, Müde, Hütte, Küche, Hüpfen |

> Wörter mit `rm`/`nb`/`kt`/`gy`/`oe`/`iu` erzwingen einen a2-Layerwechsel mitten im Wort (das ist der Punkt des Drills). Bei den seltenen Paaren `cy`, `nb` und `gy` fehlen häufige deutsche Wörter, daher englische bzw. Lehnformen.

### Home-Row-Symbol-Combos (alle Alpha-Layer)

| Chord | Output |
| --- | --- |
| R + T | _ (auch N + T · Shift) |
| R + H | - (auch N + T · Plain) |
| E + I | : (auch U + E · Shift) |
| C + I | ; (auch U + E · Plain) |

> `_ - : ;` kommen im Pool nur einmal pro Runde vor (Chord-Pfad); beide Wege liefern das gleiche Zeichen.

### Adaptive Keys (9, nur srht)

| Nach | Swap | Keys |
| --- | --- | --- |
| R | H ↔ L · M ↔ V | H L M V |
| U | O ↔ I | O I |
| Q | I ↔ U | I U |
| N | B ↔ X | B X |

> 9 adaptive Keys (`l h o i u` auf a1, `x b v m` auf a2): innerhalb von 300 ms nach dem Trigger gibt der Key den Partner aus — z. B. kommt schnelles `rh` als `rl` heraus, `ui` als `uo`. Die Bigram-Chords (beide Tasten gleichzeitig) und alles außerhalb des Fensters sind nicht betroffen — der Drill nutzt deshalb bewusst den Chord-Pfad.

## Stufe 1 — Plain (116 Runden · 2088 Tokens · 4175 Zeichen)

```
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
] / { < & $ ' # ) (
! [ > } - ; ~ =
```

## Stufe 2 — Plain + Ctrl + erste Wörter (8 Runden · 800 Tokens · 4143 Zeichen)

```
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
Schrift ( Höfe mugs heiß - Baum Maus -> erwache
umbringt Symbol Systeme erwachsene bugs :: <= während Wind Morgen
&= = / Kombination Buch Mädchen erwartet Amboss Licht ^=
schreiben tags Küsse += Höhlen ?? && $ Hüpfen Schule
Haus + Tanne amtieren Straße größer Wolke > == Kind
Wiese /* Bett Amtsstube schön < Schritt Hände & '
Apfel Hütte Fenster ; Amt Wasser <<= ~ Vögel Küche
dogs Nacht { <= bags Kombi Analyse System ! Käse
<< Vogel Glas flags # Amtsblatt ] [ Müde //
Hund ) Maschine = erwartung >= Hand grüßen ++ }
```

## Stufe 3 — + a1-Bigrams + Layer-1-Wörter (5 Runden · 675 Tokens · 3749 Zeichen)

```
Wolke Kombi DT Ruinen ?? Symbol grüßen verwandt beobachten flags
Schritt Amtsblatt Geometer erlaubt tags = ) Buch > &=
Landtag Käse ' Cyclist <<= mugs Kombination Ruine ++ Höhlen
// <= Amboss ! << Hand guide Beobachtung Sohn <
Vogel HN Maus Tanne # <= juice Mädchen UI wohnen
Maschine erlitten bugs ~ Analyse :: Vögel eosin Amtsstube >=
Erlösung System Kind EO Wasser / erwartung eons Kahn Müde
Hütte Baum Hahn ( += Hund schön build Apfel +
Licht == - schreiben ; erwache Systeme dogs Fenster Morgen
amtieren ^= Mohn } Geometrie Nacht ] suit Hüpfen Küsse
umbringt [ Schrift Bett RL Hände heiß während Bicycle /*
Höfe && erwartet Amt größer Wind suitable CY erwachsene $
erlöst = Straße -> Schule Handtuch Haus Wiese Glas Cyber
bags Küche { erleben &
Wolke Kombi DT Ruinen ?? Symbol grüßen verwandt beobachten flags
Schritt Amtsblatt Geometer erlaubt tags = ) Buch > &=
Landtag Käse ' Cyclist <<= mugs Kombination Ruine ++ Höhlen
// <= Amboss ! << Hand guide Beobachtung Sohn <
Vogel HN Maus Tanne # <= juice Mädchen UI wohnen
Maschine erlitten bugs ~ Analyse :: Vögel eosin Amtsstube >=
Erlösung System Kind EO Wasser / erwartung eons Kahn Müde
Hütte Baum Hahn ( += Hund schön build Apfel +
Licht == - schreiben ; erwache Systeme dogs Fenster Morgen
amtieren ^= Mohn } Geometrie Nacht ] suit Hüpfen Küsse
umbringt [ Schrift Bett RL Hände heiß während Bicycle /*
Höfe && erwartet Amt größer Wind suitable CY erwachsene $
erlöst = Straße -> Schule Handtuch Haus Wiese Glas Cyber
bags Küche { erleben &
Wolke Kombi DT Ruinen ?? Symbol grüßen verwandt beobachten flags
Schritt Amtsblatt Geometer erlaubt tags = ) Buch > &=
Landtag Käse ' Cyclist <<= mugs Kombination Ruine ++ Höhlen
// <= Amboss ! << Hand guide Beobachtung Sohn <
Vogel HN Maus Tanne # <= juice Mädchen UI wohnen
Maschine erlitten bugs ~ Analyse :: Vögel eosin Amtsstube >=
Erlösung System Kind EO Wasser / erwartung eons Kahn Müde
Hütte Baum Hahn ( += Hund schön build Apfel +
Licht == - schreiben ; erwache Systeme dogs Fenster Morgen
amtieren ^= Mohn } Geometrie Nacht ] suit Hüpfen Küsse
umbringt [ Schrift Bett RL Hände heiß während Bicycle /*
Höfe && erwartet Amt größer Wind suitable CY erwachsene $
erlöst = Straße -> Schule Handtuch Haus Wiese Glas Cyber
bags Küche { erleben &
Wolke Kombi DT Ruinen ?? Symbol grüßen verwandt beobachten flags
Schritt Amtsblatt Geometer erlaubt tags = ) Buch > &=
Landtag Käse ' Cyclist <<= mugs Kombination Ruine ++ Höhlen
// <= Amboss ! << Hand guide Beobachtung Sohn <
Vogel HN Maus Tanne # <= juice Mädchen UI wohnen
Maschine erlitten bugs ~ Analyse :: Vögel eosin Amtsstube >=
Erlösung System Kind EO Wasser / erwartung eons Kahn Müde
Hütte Baum Hahn ( += Hund schön build Apfel +
Licht == - schreiben ; erwache Systeme dogs Fenster Morgen
amtieren ^= Mohn } Geometrie Nacht ] suit Hüpfen Küsse
umbringt [ Schrift Bett RL Hände heiß während Bicycle /*
Höfe && erwartet Amt größer Wind suitable CY erwachsene $
erlöst = Straße -> Schule Handtuch Haus Wiese Glas Cyber
bags Küche { erleben &
Wolke Kombi DT Ruinen ?? Symbol grüßen verwandt beobachten flags
Schritt Amtsblatt Geometer erlaubt tags = ) Buch > &=
Landtag Käse ' Cyclist <<= mugs Kombination Ruine ++ Höhlen
// <= Amboss ! << Hand guide Beobachtung Sohn <
Vogel HN Maus Tanne # <= juice Mädchen UI wohnen
Maschine erlitten bugs ~ Analyse :: Vögel eosin Amtsstube >=
Erlösung System Kind EO Wasser / erwartung eons Kahn Müde
Hütte Baum Hahn ( += Hund schön build Apfel +
Licht == - schreiben ; erwache Systeme dogs Fenster Morgen
amtieren ^= Mohn } Geometrie Nacht ] suit Hüpfen Küsse
umbringt [ Schrift Bett RL Hände heiß während Bicycle /*
Höfe && erwartet Amt größer Wind suitable CY erwachsene $
erlöst = Straße -> Schule Handtuch Haus Wiese Glas Cyber
bags Küche { erleben &
```

## Stufe 4 — Alle Symbole (5 Runden · 830 Tokens · 4119 Zeichen)

```
: Handtuch erwache Beobachtung eons Schritt bags <<= erlaubt suitable
- erlöst < Cyber System Bett > während bugs ~
; == $ * Küsse guide >>= Hahn heiß ^
Landtag Höfe Hütte Schrift Käse Morgen ] */ Mohn >>
] ( größer Geometrie && -> Straße Ruinen build Systeme
Maschine & Hand ?? ++ Maus Küche Erlösung >= erwartet
suit <= eosin € + ´ Höhlen = schreiben %
@ juice ( { Tanne Mädchen flags Amtsblatt Geometer ^=
erlitten Wind // -- / | # \ Müde <<
:= beobachten Vogel > ' >= [ || += )
tags erwartung Analyse < &= |= wohnen Amt Glas =
Kind umbringt != *= dogs >= ?. Ruine [ Kombi
} erleben Vögel Cyclist " Haus Sohn } amtieren Buch
-= Hüpfen Wiese Nacht :: Schule Kombination + Bicycle schön
<= Symbol { Wolke Hände Hund ! Baum ? _
Apfel /* <= ) => Fenster Wasser ... Kahn grüßen
mugs Amboss erwachsene Amtsstube Licht verwandt
: Handtuch erwache Beobachtung eons Schritt bags <<= erlaubt suitable
- erlöst < Cyber System Bett > während bugs ~
; == $ * Küsse guide >>= Hahn heiß ^
Landtag Höfe Hütte Schrift Käse Morgen ] */ Mohn >>
] ( größer Geometrie && -> Straße Ruinen build Systeme
Maschine & Hand ?? ++ Maus Küche Erlösung >= erwartet
suit <= eosin € + ´ Höhlen = schreiben %
@ juice ( { Tanne Mädchen flags Amtsblatt Geometer ^=
erlitten Wind // -- / | # \ Müde <<
:= beobachten Vogel > ' >= [ || += )
tags erwartung Analyse < &= |= wohnen Amt Glas =
Kind umbringt != *= dogs >= ?. Ruine [ Kombi
} erleben Vögel Cyclist " Haus Sohn } amtieren Buch
-= Hüpfen Wiese Nacht :: Schule Kombination + Bicycle schön
<= Symbol { Wolke Hände Hund ! Baum ? _
Apfel /* <= ) => Fenster Wasser ... Kahn grüßen
mugs Amboss erwachsene Amtsstube Licht verwandt
: Handtuch erwache Beobachtung eons Schritt bags <<= erlaubt suitable
- erlöst < Cyber System Bett > während bugs ~
; == $ * Küsse guide >>= Hahn heiß ^
Landtag Höfe Hütte Schrift Käse Morgen ] */ Mohn >>
] ( größer Geometrie && -> Straße Ruinen build Systeme
Maschine & Hand ?? ++ Maus Küche Erlösung >= erwartet
suit <= eosin € + ´ Höhlen = schreiben %
@ juice ( { Tanne Mädchen flags Amtsblatt Geometer ^=
erlitten Wind // -- / | # \ Müde <<
:= beobachten Vogel > ' >= [ || += )
tags erwartung Analyse < &= |= wohnen Amt Glas =
Kind umbringt != *= dogs >= ?. Ruine [ Kombi
} erleben Vögel Cyclist " Haus Sohn } amtieren Buch
-= Hüpfen Wiese Nacht :: Schule Kombination + Bicycle schön
<= Symbol { Wolke Hände Hund ! Baum ? _
Apfel /* <= ) => Fenster Wasser ... Kahn grüßen
mugs Amboss erwachsene Amtsstube Licht verwandt
: Handtuch erwache Beobachtung eons Schritt bags <<= erlaubt suitable
- erlöst < Cyber System Bett > während bugs ~
; == $ * Küsse guide >>= Hahn heiß ^
Landtag Höfe Hütte Schrift Käse Morgen ] */ Mohn >>
] ( größer Geometrie && -> Straße Ruinen build Systeme
Maschine & Hand ?? ++ Maus Küche Erlösung >= erwartet
suit <= eosin € + ´ Höhlen = schreiben %
@ juice ( { Tanne Mädchen flags Amtsblatt Geometer ^=
erlitten Wind // -- / | # \ Müde <<
:= beobachten Vogel > ' >= [ || += )
tags erwartung Analyse < &= |= wohnen Amt Glas =
Kind umbringt != *= dogs >= ?. Ruine [ Kombi
} erleben Vögel Cyclist " Haus Sohn } amtieren Buch
-= Hüpfen Wiese Nacht :: Schule Kombination + Bicycle schön
<= Symbol { Wolke Hände Hund ! Baum ? _
Apfel /* <= ) => Fenster Wasser ... Kahn grüßen
mugs Amboss erwachsene Amtsstube Licht verwandt
: Handtuch erwache Beobachtung eons Schritt bags <<= erlaubt suitable
- erlöst < Cyber System Bett > während bugs ~
; == $ * Küsse guide >>= Hahn heiß ^
Landtag Höfe Hütte Schrift Käse Morgen ] */ Mohn >>
] ( größer Geometrie && -> Straße Ruinen build Systeme
Maschine & Hand ?? ++ Maus Küche Erlösung >= erwartet
suit <= eosin € + ´ Höhlen = schreiben %
@ juice ( { Tanne Mädchen flags Amtsblatt Geometer ^=
erlitten Wind // -- / | # \ Müde <<
:= beobachten Vogel > ' >= [ || += )
tags erwartung Analyse < &= |= wohnen Amt Glas =
Kind umbringt != *= dogs >= ?. Ruine [ Kombi
} erleben Vögel Cyclist " Haus Sohn } amtieren Buch
-= Hüpfen Wiese Nacht :: Schule Kombination + Bicycle schön
<= Symbol { Wolke Hände Hund ! Baum ? _
Apfel /* <= ) => Fenster Wasser ... Kahn grüßen
mugs Amboss erwachsene Amtsstube Licht verwandt
```

## Stufe 5 — + a2-Bigrams + alle Wörter (4 Runden · 812 Tokens · 4115 Zeichen)

```
< Buch Sohn Systeme erlöst ö Tanne Anbau >= grüßen
== Gymnasium Kombi erwachsene Schule Maus UI RL ß ->
IU Licht Geometrie Kombination _ // Bicycle *= = $
= Amtsstube ... Diktat eons Höhlen ?. Iunius Ruine RM
erwartung Schrift Wiese >> ++ mugs Küche ! KT |
wohnen &= anbei tags @ DT Haus Symbol != EO
Nacht Ruinen := <= Mädchen % } Iulius ( +
|= < << ] Höfe Hüpfen Vögel -= Erlösung Maschine
build Handtuch > erwartet */ Cyber Wasser >>= ~ erlitten
dogs bugs -- Analyse Hände Amtsblatt Amt Vogel Hand Amboss
suit juice || heiß ) += { :: Koexistenz [
{ Diktatur Norm erlaubt Beobachtung # >= Cyclist ( &&
? OE + : Kaktus Küsse € Kahn " suitable
Koeffizient } - * CY <<= Wärme schreiben Hund <=
umbringt Müde HN erleben warm ' Geometer beobachten verwandt Baum
eosin Kind während [ /* ?? GY Glas Einbau Biology
Käse erwache ] Hütte ü / Fenster Energy Mohn NB
=> \ <= equinoctium > amtieren Wolke ) Schritt Formel
´ guide Koeln Morgen Straße Apfel schön & Wind Landtag
System größer bags ä Hahn aktuell ^= flags ^ >=
Bett ; Kontakt
< Buch Sohn Systeme erlöst ö Tanne Anbau >= grüßen
== Gymnasium Kombi erwachsene Schule Maus UI RL ß ->
IU Licht Geometrie Kombination _ // Bicycle *= = $
= Amtsstube ... Diktat eons Höhlen ?. Iunius Ruine RM
erwartung Schrift Wiese >> ++ mugs Küche ! KT |
wohnen &= anbei tags @ DT Haus Symbol != EO
Nacht Ruinen := <= Mädchen % } Iulius ( +
|= < << ] Höfe Hüpfen Vögel -= Erlösung Maschine
build Handtuch > erwartet */ Cyber Wasser >>= ~ erlitten
dogs bugs -- Analyse Hände Amtsblatt Amt Vogel Hand Amboss
suit juice || heiß ) += { :: Koexistenz [
{ Diktatur Norm erlaubt Beobachtung # >= Cyclist ( &&
? OE + : Kaktus Küsse € Kahn " suitable
Koeffizient } - * CY <<= Wärme schreiben Hund <=
umbringt Müde HN erleben warm ' Geometer beobachten verwandt Baum
eosin Kind während [ /* ?? GY Glas Einbau Biology
Käse erwache ] Hütte ü / Fenster Energy Mohn NB
=> \ <= equinoctium > amtieren Wolke ) Schritt Formel
´ guide Koeln Morgen Straße Apfel schön & Wind Landtag
System größer bags ä Hahn aktuell ^= flags ^ >=
Bett ; Kontakt
< Buch Sohn Systeme erlöst ö Tanne Anbau >= grüßen
== Gymnasium Kombi erwachsene Schule Maus UI RL ß ->
IU Licht Geometrie Kombination _ // Bicycle *= = $
= Amtsstube ... Diktat eons Höhlen ?. Iunius Ruine RM
erwartung Schrift Wiese >> ++ mugs Küche ! KT |
wohnen &= anbei tags @ DT Haus Symbol != EO
Nacht Ruinen := <= Mädchen % } Iulius ( +
|= < << ] Höfe Hüpfen Vögel -= Erlösung Maschine
build Handtuch > erwartet */ Cyber Wasser >>= ~ erlitten
dogs bugs -- Analyse Hände Amtsblatt Amt Vogel Hand Amboss
suit juice || heiß ) += { :: Koexistenz [
{ Diktatur Norm erlaubt Beobachtung # >= Cyclist ( &&
? OE + : Kaktus Küsse € Kahn " suitable
Koeffizient } - * CY <<= Wärme schreiben Hund <=
umbringt Müde HN erleben warm ' Geometer beobachten verwandt Baum
eosin Kind während [ /* ?? GY Glas Einbau Biology
Käse erwache ] Hütte ü / Fenster Energy Mohn NB
=> \ <= equinoctium > amtieren Wolke ) Schritt Formel
´ guide Koeln Morgen Straße Apfel schön & Wind Landtag
System größer bags ä Hahn aktuell ^= flags ^ >=
Bett ; Kontakt
< Buch Sohn Systeme erlöst ö Tanne Anbau >= grüßen
== Gymnasium Kombi erwachsene Schule Maus UI RL ß ->
IU Licht Geometrie Kombination _ // Bicycle *= = $
= Amtsstube ... Diktat eons Höhlen ?. Iunius Ruine RM
erwartung Schrift Wiese >> ++ mugs Küche ! KT |
wohnen &= anbei tags @ DT Haus Symbol != EO
Nacht Ruinen := <= Mädchen % } Iulius ( +
|= < << ] Höfe Hüpfen Vögel -= Erlösung Maschine
build Handtuch > erwartet */ Cyber Wasser >>= ~ erlitten
dogs bugs -- Analyse Hände Amtsblatt Amt Vogel Hand Amboss
suit juice || heiß ) += { :: Koexistenz [
{ Diktatur Norm erlaubt Beobachtung # >= Cyclist ( &&
? OE + : Kaktus Küsse € Kahn " suitable
Koeffizient } - * CY <<= Wärme schreiben Hund <=
umbringt Müde HN erleben warm ' Geometer beobachten verwandt Baum
eosin Kind während [ /* ?? GY Glas Einbau Biology
Käse erwache ] Hütte ü / Fenster Energy Mohn NB
=> \ <= equinoctium > amtieren Wolke ) Schritt Formel
´ guide Koeln Morgen Straße Apfel schön & Wind Landtag
System größer bags ä Hahn aktuell ^= flags ^ >=
Bett ; Kontakt
```

## Stufe 6 — Wörter (5 Runden · 570 Tokens · 4019 Zeichen)

```
Vogel Diktat beobachten Ruine Koexistenz Höfe aktuell Vögel Koeln Schritt
Anbau suitable amtieren Maus Maschine Mohn Biology Landtag Mädchen equinoctium
Hüpfen Cyclist Wärme erlöst guide erleben warm Amtsblatt erwache Erlösung
während Bett Buch schön Hände System Systeme Wind Küche bags
Amboss Amt Morgen Kaktus Analyse Kontakt build Wolke Koeffizient Kahn
Kombi Höhlen Hahn juice Hund größer Sohn Geometer mugs erwartet
Diktatur Cyber Iunius Geometrie Müde tags Tanne Ruinen umbringt flags
Handtuch Haus anbei Glas Licht suit Hütte wohnen Symbol Apfel
Energy Norm Amtsstube Kind grüßen verwandt dogs Bicycle erwartung erlitten
Schrift Schule Iulius bugs Käse Kombination schreiben Formel Beobachtung Fenster
erlaubt eosin Hand Baum Gymnasium Wasser Wiese eons Nacht erwachsene
Straße heiß Einbau Küsse
Vogel Diktat beobachten Ruine Koexistenz Höfe aktuell Vögel Koeln Schritt
Anbau suitable amtieren Maus Maschine Mohn Biology Landtag Mädchen equinoctium
Hüpfen Cyclist Wärme erlöst guide erleben warm Amtsblatt erwache Erlösung
während Bett Buch schön Hände System Systeme Wind Küche bags
Amboss Amt Morgen Kaktus Analyse Kontakt build Wolke Koeffizient Kahn
Kombi Höhlen Hahn juice Hund größer Sohn Geometer mugs erwartet
Diktatur Cyber Iunius Geometrie Müde tags Tanne Ruinen umbringt flags
Handtuch Haus anbei Glas Licht suit Hütte wohnen Symbol Apfel
Energy Norm Amtsstube Kind grüßen verwandt dogs Bicycle erwartung erlitten
Schrift Schule Iulius bugs Käse Kombination schreiben Formel Beobachtung Fenster
erlaubt eosin Hand Baum Gymnasium Wasser Wiese eons Nacht erwachsene
Straße heiß Einbau Küsse
Vogel Diktat beobachten Ruine Koexistenz Höfe aktuell Vögel Koeln Schritt
Anbau suitable amtieren Maus Maschine Mohn Biology Landtag Mädchen equinoctium
Hüpfen Cyclist Wärme erlöst guide erleben warm Amtsblatt erwache Erlösung
während Bett Buch schön Hände System Systeme Wind Küche bags
Amboss Amt Morgen Kaktus Analyse Kontakt build Wolke Koeffizient Kahn
Kombi Höhlen Hahn juice Hund größer Sohn Geometer mugs erwartet
Diktatur Cyber Iunius Geometrie Müde tags Tanne Ruinen umbringt flags
Handtuch Haus anbei Glas Licht suit Hütte wohnen Symbol Apfel
Energy Norm Amtsstube Kind grüßen verwandt dogs Bicycle erwartung erlitten
Schrift Schule Iulius bugs Käse Kombination schreiben Formel Beobachtung Fenster
erlaubt eosin Hand Baum Gymnasium Wasser Wiese eons Nacht erwachsene
Straße heiß Einbau Küsse
Vogel Diktat beobachten Ruine Koexistenz Höfe aktuell Vögel Koeln Schritt
Anbau suitable amtieren Maus Maschine Mohn Biology Landtag Mädchen equinoctium
Hüpfen Cyclist Wärme erlöst guide erleben warm Amtsblatt erwache Erlösung
während Bett Buch schön Hände System Systeme Wind Küche bags
Amboss Amt Morgen Kaktus Analyse Kontakt build Wolke Koeffizient Kahn
Kombi Höhlen Hahn juice Hund größer Sohn Geometer mugs erwartet
Diktatur Cyber Iunius Geometrie Müde tags Tanne Ruinen umbringt flags
Handtuch Haus anbei Glas Licht suit Hütte wohnen Symbol Apfel
Energy Norm Amtsstube Kind grüßen verwandt dogs Bicycle erwartung erlitten
Schrift Schule Iulius bugs Käse Kombination schreiben Formel Beobachtung Fenster
erlaubt eosin Hand Baum Gymnasium Wasser Wiese eons Nacht erwachsene
Straße heiß Einbau Küsse
Vogel Diktat beobachten Ruine Koexistenz Höfe aktuell Vögel Koeln Schritt
Anbau suitable amtieren Maus Maschine Mohn Biology Landtag Mädchen equinoctium
Hüpfen Cyclist Wärme erlöst guide erleben warm Amtsblatt erwache Erlösung
während Bett Buch schön Hände System Systeme Wind Küche bags
Amboss Amt Morgen Kaktus Analyse Kontakt build Wolke Koeffizient Kahn
Kombi Höhlen Hahn juice Hund größer Sohn Geometer mugs erwartet
Diktatur Cyber Iunius Geometrie Müde tags Tanne Ruinen umbringt flags
Handtuch Haus anbei Glas Licht suit Hütte wohnen Symbol Apfel
Energy Norm Amtsstube Kind grüßen verwandt dogs Bicycle erwartung erlitten
Schrift Schule Iulius bugs Käse Kombination schreiben Formel Beobachtung Fenster
erlaubt eosin Hand Baum Gymnasium Wasser Wiese eons Nacht erwachsene
Straße heiß Einbau Küsse
```

## Stufe 7 — Vollpass (Abschluss) (1 Runde · 203 Tokens · 1028 Zeichen)

```
€ erwachsene < } Kind | anbei * build guide
Wolke Schrift == >= Hand Ruinen + Bett &= <
Geometrie Amboss Symbol Fenster ! DT - + Kombi Anbau
Norm += schön % || HN Straße ´ ... Sohn
Maus ; Kahn // bags _ CY Geometer Diktat ö
suit Höfe Handtuch flags Amtsstube / ) ?. " &&
erwartet schreiben & *= Diktatur Energy EO [ bugs >=
Licht Apfel Mohn Schule tags Hahn Gymnasium ++ Morgen verwandt
@ Küsse ^= erlitten OE Bicycle ' <= Buch ]
umbringt ?? erlöst Höhlen Vögel = Amt ( Vogel ::
Wind erlaubt Müde GY ~ Käse ) != Iunius Küche
Amtsblatt warm >> -- UI <= { ( Hände eosin
Maschine */ Hütte \ erwache ^ Kombination Haus /* Koexistenz
> größer : Beobachtung Cyclist |= Wiese Iulius := Formel
# Systeme <= -> equinoctium amtieren = Kontakt Koeffizient Landtag
KT Analyse Wasser -= grüßen aktuell beobachten mugs heiß >>=
Nacht RM > Mädchen => während Cyber Kaktus Einbau <<
$ Koeln erwartung System RL wohnen ß ] Ruine suitable
[ Wärme Glas Baum eons IU ü juice ä {
Hüpfen erleben } Schritt Biology NB ? dogs <<= >=
Erlösung Hund Tanne
```
