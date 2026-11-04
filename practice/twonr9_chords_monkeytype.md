# TwoNr9 — Chord-Praxis (Monkeytype)

Diese Datei enthält ein **Stufen-Übungssystem** für die TwoNr9-Keymap (bugwind) — Qualität vor Quantität: 7 aufeinander aufbauende Blöcke, die in der Schwierigkeit steigen (Plain → +Ctrl/+erste Wörter → +a1-Bigrams/+Layer-1-Wörter → +Shift → +a2-Bigrams/+alle Wörter → Wörter → Vollpass). Die Wörter drillen ab Stufe 2 auch das Alpha-Grid: zuerst Wörter ohne Bigram-Paare, dann die, die a1- bzw. a2-Chords brauchen — so wachsen die Wörter mit den Layer-Kenntnissen mit. Jeder Block ist selbstständig (nur sein eigener Pool) und wird Round-Robin gezogen: pro voller Runde kommt jeder Token genau einmal vor, egal an welcher Stelle Monkeytype zufällig ansetzt — jeder Ausschnitt ist gleichmäßig.

## Nutzung in Monkeytype

1. Den Block der aktuellen Stufe kopieren (Code-Block, < 10.000 Zeichen).
2. Monkeytype → Test Type **Custom** → Text einfügen.
3. Test-Länge z. B. auf 25–75 Wörter stellen; Monkeytype wählt aus dem Block einen zufälligen Ausschnitt.
4. Erst zur nächsten Stufe wechseln, wenn die aktuelle sauber läuft. Stufe 7 (Vollpass) ist die Abschlussprüfung: jeder Token genau einmal.

Beim Üben auf der TwoNr9 zeigt die Legende unten, welcher Token welchen Chord + Modifier-Zustand triggert.

## Legende

### Stufen

| Stufe | Block | Was er übt | Pool |
| --- | --- | --- | --- |
| 1 | **Plain** | reines Chord-Gefühl: 18 Plain-Outputs, keine Modifier | 18 Tokens |
| 2 | **Plain + Ctrl + erste Wörter** | Operatoren dazu + allgemeine deutsche Wörter ohne Bigrams (Alpha-Grid übt mit) — immer noch kein Shift | 72 Tokens |
| 3 | **+ a1-Bigrams + Layer-1-Wörter** | a1 komplett: Bigrams + die Wörter, die nur a1-Chords brauchen | 109 Tokens |
| 4 | **Alle Symbole** | Shift-Zustände kommen dazu (+ ´ aus N + R) | 140 Tokens |
| 5 | **+ a2-Bigrams + alle Wörter** | die komplette Keymap: a2-Bigrams (Layerwechsel mitten im Wort) + alle Wörter | 182 Tokens |
| 6 | **Wörter** | alles im echten Tipp-Kontext (93 Wörter) | 93 Tokens |
| 7 | **Vollpass (Abschluss)** | alles in einem Durchgang | 182 Tokens |

### Diagonale Symbol-Chords (16 Chords × 4 Modifier-Zustände = 64 Outputs)

| Chord | Plain | Shift | Ctrl | Ctrl + Shift |
| --- | --- | --- | --- | --- |
| L + N | `(` | `)` | `==` | `!=` |
| Y + E | `}` | `{` | `<=` | `>=` |
| M + R | `[` | `]` | `+=` | `-=` |
| U + A | `)` | `(` | `&=` | `|=` |
| D + T | `{` | `}` | `<<=` | `>>=` |
| O + I | `]` | `[` | `^=` | `*=` |
| M + N | `&` | `*` | `&&` | `||` |
| O + A | `$` | `€` | `??` | `?.` |
| D + R | `~` | `^` | `->` | `=>` |
| Y + I | `=` | `+` | `<<` | `>>` |
| D + N | `<` | `>` | `<=` | `<=` |
| Y + A | `>` | `<` | `>=` | `>=` |
| L + T | `!` | `?` | `//` | `...` |
| M + H | `-` | `_` | `++` | `--` |
| U + E | `;` | `:` | `/*` | `*/` |
| O + S | `'` | `"` | `=` | `|` |
| L + H | `#` | `%` | `::` | `:=` |
| U + S | `/` | `\` | `+` | `@` |

### Deutsche Buchstaben (Buchstabe + Space, a1/a2)

| Chord | Output (Shift = Grossbuchstabe) |
| --- | --- |
| S + Space | ß / ẞ |
| A + Space | ä / Ä |
| O + Space | ö / Ö |
| U + Space | ü / Ü |
| N + R | ´ (Shift: `) |

### Bigrams (12)

| Layer | Chords |
| --- | --- |
| a1 | RL · KT · MB · YS · EO · UI |
| a2 | RW · MT · SCH · GS · OE · IU |

### Wörter (ab Stufe 2, kumulativ)

**Stufe 2** — ohne Bigram-Paare: Haus, Maus, Hund, Kind, Wind, Hand, Nacht, Licht, Wasser, Baum, Apfel, Vogel, Wolke, Fenster, Buch, Bett, Morgen, Glas, Wiese, Tanne + ß/ä/ö/ü-Wörter: Straße, größer, heiß, Küsse, grüßen, während, Mädchen, Käse, Hände, Höfe, Höhlen, Vögel, Müde, Hütte, Küche, Hüpfen

**Stufe 3** — a1-Bigram-Wörter: erleben, erlöst, erlitten, erlaubt, Erlösung, aktuell, Diktat, Diktatur, Kontakt, Kaktus, Symbol, Kombi, Amboss, Kombination, umbringt, System, Systeme, Analyse, Geometrie, beobachten, Beobachtung, Geometer, eons, eosin, Ruine, Ruinen, build, suit, suitable, juice, guide

**Stufe 5** — a2-Bigram-Wörter (Layerwechsel mitten im Wort): erwartet, erwartung, erwachsene, erwache, Amt, Amtsstube, Amtsblatt, amtieren, Schule, schön, Maschine, schreiben, Schrift, Schritt, bags, dogs, tags, flags, mugs, bugs, Koeffizient, Koexistenz, Koeln, Iulius, Iunius, equinoctium

### Wörter-Drill: Buchstabenpaar → Chord → Wörter

| Paar | Chord | Wörter |
| --- | --- | --- |
| `rl` | L+R | erleben, erlöst, erlitten, erlaubt, Erlösung |
| `kt` | M+T | aktuell, Diktat, Diktatur, Kontakt, Kaktus |
| `mb` | D+H | Symbol, Kombi, Amboss, Kombination, umbringt |
| `ys` | Y+S | System, Systeme, Analyse |
| `eo` | O+E | Geometrie, beobachten, Beobachtung, Geometer, eons, eosin |
| `ui` | U+I | Ruine, Ruinen, build, suit, suitable, juice, guide |
| `rw` | X+W | erwartet, erwartung, erwachsene, erwache |
| `mt` | V+K | Amt, Amtsstube, Amtsblatt, amtieren |
| `sch` | B+F (a2) | Schule, schön, Maschine, schreiben, Schrift, Schritt |
| `gs` | G+C (a2) | bags, dogs, tags, flags, mugs, bugs |
| `oe` | J+Q (a2) | Koeffizient, Koexistenz, Koeln |
| `iu` | ,+. (a2) | Iulius, Iunius, equinoctium |
| `ß` | S+Space | Straße, größer, heiß, grüßen |
| `ä` | A+Space | während, Mädchen, Käse, Hände |
| `ö` | O+Space | größer, Höfe, Höhlen, Vögel |
| `ü` | U+Space | Küsse, grüßen, Müde, Hütte, Küche, Hüpfen |

> Wörter mit `sch`/`gs`/`oe`/`iu` erzwingen einen a2-Layerwechsel mitten im Wort (das ist der Punkt des Drills). Bei den seltenen Paaren `gs` und `iu` fehlen häufige deutsche Wörter, daher englische bzw. Lehnformen.

### Home-Row-Symbol-Combos (alle Alpha-Layer)

| Chord | Output |
| --- | --- |
| R + H | _ (auch M + H · Shift) |
| R + T | - (auch M + H · Plain) |
| E + I | : (auch U + E · Shift) |
| S + I | ; (auch U + E · Plain) |

> `_ - : ;` kommen im Pool nur einmal pro Runde vor (Chord-Pfad); beide Wege liefern das gleiche Zeichen.

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

## Stufe 2 — Plain + Ctrl + erste Wörter (13 Runden · 936 Tokens · 3951 Zeichen)

```
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
Wasser Kind :: ! / Buch größer Bett ( ??
Mädchen Tanne Hütte < Hände Straße == Baum = Höhlen
# Maus /* ] << Müde Vögel grüßen Wiese während
&& $ Haus <<= > { Licht ' Fenster heiß
&= Küsse ; Vogel Wolke <= Küche Nacht Käse &
<= - ^= -> Morgen Wind ~ Glas + [
Apfel Hüpfen += // Hund ) = Höfe >= Hand
++ }
```

## Stufe 3 — + a1-Bigrams + Layer-1-Wörter (7 Runden · 763 Tokens · 3947 Zeichen)

```
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
Hand Symbol Maus Diktat << Amboss > ++ Kontakt Tanne
beobachten build Wolke Buch Kind ' aktuell Käse Systeme größer
<= Küsse erlitten Ruinen & Diktatur umbringt guide / !
eosin juice # Wasser Vögel Erlösung System Kaktus Straße ::
erlöst Geometer Geometrie += Hütte EO ~ Hüpfen Höfe &=
heiß = <= KT MB ?? Glas Baum ( <
Hund <<= während Analyse suit + Licht == - ;
Mädchen Fenster Morgen ^= } Nacht ] erlaubt grüßen suitable
Bett RL Kombination /* && eons Beobachtung Wind { YS
Höhlen $ = Kombi -> erleben Haus // Ruine >=
Hände Küche Müde Wiese UI Apfel [ Vogel )
```

## Stufe 4 — Alle Symbole (6 Runden · 840 Tokens · 3827 Zeichen)

```
>>= Beobachtung Vögel Symbol eons Ruine < $ { Küche
Kombi :: ] _ Diktat -= erleben Tanne suitable ->
== */ : } grüßen @ ; ( >= >>
€ ++ \ Küsse Käse größer > Wiese ? Bett
aktuell Ruinen + juice = Hund Wolke <<= # --
eosin Nacht ] | := * Vogel erlitten % ~
/ erlöst Maus während Geometer suit umbringt >= Hüpfen ||
+= ) Kontakt < Müde |= ! = Kind Straße
*= Baum >= ?. Amboss erlaubt } + Geometrie "
Haus { ( Erlösung ?? > Hand Höfe << &=
^ != // - Kombination Mädchen Glas Diktatur [ <=
guide ´ [ Hände && Buch <= Apfel Wind beobachten
& Morgen Analyse Systeme build ' ^= /* <= )
=> Fenster Wasser ... System Kaktus heiß Höhlen Hütte Licht
>>= Beobachtung Vögel Symbol eons Ruine < $ { Küche
Kombi :: ] _ Diktat -= erleben Tanne suitable ->
== */ : } grüßen @ ; ( >= >>
€ ++ \ Küsse Käse größer > Wiese ? Bett
aktuell Ruinen + juice = Hund Wolke <<= # --
eosin Nacht ] | := * Vogel erlitten % ~
/ erlöst Maus während Geometer suit umbringt >= Hüpfen ||
+= ) Kontakt < Müde |= ! = Kind Straße
*= Baum >= ?. Amboss erlaubt } + Geometrie "
Haus { ( Erlösung ?? > Hand Höfe << &=
^ != // - Kombination Mädchen Glas Diktatur [ <=
guide ´ [ Hände && Buch <= Apfel Wind beobachten
& Morgen Analyse Systeme build ' ^= /* <= )
=> Fenster Wasser ... System Kaktus heiß Höhlen Hütte Licht
>>= Beobachtung Vögel Symbol eons Ruine < $ { Küche
Kombi :: ] _ Diktat -= erleben Tanne suitable ->
== */ : } grüßen @ ; ( >= >>
€ ++ \ Küsse Käse größer > Wiese ? Bett
aktuell Ruinen + juice = Hund Wolke <<= # --
eosin Nacht ] | := * Vogel erlitten % ~
/ erlöst Maus während Geometer suit umbringt >= Hüpfen ||
+= ) Kontakt < Müde |= ! = Kind Straße
*= Baum >= ?. Amboss erlaubt } + Geometrie "
Haus { ( Erlösung ?? > Hand Höfe << &=
^ != // - Kombination Mädchen Glas Diktatur [ <=
guide ´ [ Hände && Buch <= Apfel Wind beobachten
& Morgen Analyse Systeme build ' ^= /* <= )
=> Fenster Wasser ... System Kaktus heiß Höhlen Hütte Licht
>>= Beobachtung Vögel Symbol eons Ruine < $ { Küche
Kombi :: ] _ Diktat -= erleben Tanne suitable ->
== */ : } grüßen @ ; ( >= >>
€ ++ \ Küsse Käse größer > Wiese ? Bett
aktuell Ruinen + juice = Hund Wolke <<= # --
eosin Nacht ] | := * Vogel erlitten % ~
/ erlöst Maus während Geometer suit umbringt >= Hüpfen ||
+= ) Kontakt < Müde |= ! = Kind Straße
*= Baum >= ?. Amboss erlaubt } + Geometrie "
Haus { ( Erlösung ?? > Hand Höfe << &=
^ != // - Kombination Mädchen Glas Diktatur [ <=
guide ´ [ Hände && Buch <= Apfel Wind beobachten
& Morgen Analyse Systeme build ' ^= /* <= )
=> Fenster Wasser ... System Kaktus heiß Höhlen Hütte Licht
>>= Beobachtung Vögel Symbol eons Ruine < $ { Küche
Kombi :: ] _ Diktat -= erleben Tanne suitable ->
== */ : } grüßen @ ; ( >= >>
€ ++ \ Küsse Käse größer > Wiese ? Bett
aktuell Ruinen + juice = Hund Wolke <<= # --
eosin Nacht ] | := * Vogel erlitten % ~
/ erlöst Maus während Geometer suit umbringt >= Hüpfen ||
+= ) Kontakt < Müde |= ! = Kind Straße
*= Baum >= ?. Amboss erlaubt } + Geometrie "
Haus { ( Erlösung ?? > Hand Höfe << &=
^ != // - Kombination Mädchen Glas Diktatur [ <=
guide ´ [ Hände && Buch <= Apfel Wind beobachten
& Morgen Analyse Systeme build ' ^= /* <= )
=> Fenster Wasser ... System Kaktus heiß Höhlen Hütte Licht
>>= Beobachtung Vögel Symbol eons Ruine < $ { Küche
Kombi :: ] _ Diktat -= erleben Tanne suitable ->
== */ : } grüßen @ ; ( >= >>
€ ++ \ Küsse Käse größer > Wiese ? Bett
aktuell Ruinen + juice = Hund Wolke <<= # --
eosin Nacht ] | := * Vogel erlitten % ~
/ erlöst Maus während Geometer suit umbringt >= Hüpfen ||
+= ) Kontakt < Müde |= ! = Kind Straße
*= Baum >= ?. Amboss erlaubt } + Geometrie "
Haus { ( Erlösung ?? > Hand Höfe << &=
^ != // - Kombination Mädchen Glas Diktatur [ <=
guide ´ [ Hände && Buch <= Apfel Wind beobachten
& Morgen Analyse Systeme build ' ^= /* <= )
=> Fenster Wasser ... System Kaktus heiß Höhlen Hütte Licht
```

## Stufe 5 — + a2-Bigrams + alle Wörter (4 Runden · 728 Tokens · 3551 Zeichen)

```
// " ?. Höhlen build = Haus Hütte Koexistenz Vogel
Buch beobachten Hund >> Maschine ... $ erwartung } *
|= << RW -= >= Nacht *= RL ++ Diktat
_ IU % MB eosin &= Licht Amtsstube Analyse umbringt
! SCH Maus erlitten ß bugs guide Diktatur ( ->
Kaktus Schritt = := @ ö equinoctium größer != Tanne
+ <= Küche Ruine Wiese erwache > erlaubt */ erwachsene
YS >>= ~ Küsse } <<= -- Wasser Höfe Iunius
UI tags Hand Amtsblatt || erleben += { :: Koeln
erlöst { schön bags Systeme suitable # >= Ruinen (
dogs schreiben Mädchen + : mugs <= € Geometer System
- Käse Straße == && OE ) < EO ]
? Müde Hände | < heiß [ grüßen Symbol KT
Kombination ' juice suit eons Baum erwartet Kind [ /*
?? GS Glas Schrift Geometrie Vögel ] ü / Fenster
Koeffizient MT => \ <= flags > Hüpfen Wolke )
Erlösung Schule ´ Iulius Morgen Kombi Apfel Beobachtung & Wind
amtieren während Amboss aktuell ä Amt ^= Kontakt ^ >=
Bett ;
// " ?. Höhlen build = Haus Hütte Koexistenz Vogel
Buch beobachten Hund >> Maschine ... $ erwartung } *
|= << RW -= >= Nacht *= RL ++ Diktat
_ IU % MB eosin &= Licht Amtsstube Analyse umbringt
! SCH Maus erlitten ß bugs guide Diktatur ( ->
Kaktus Schritt = := @ ö equinoctium größer != Tanne
+ <= Küche Ruine Wiese erwache > erlaubt */ erwachsene
YS >>= ~ Küsse } <<= -- Wasser Höfe Iunius
UI tags Hand Amtsblatt || erleben += { :: Koeln
erlöst { schön bags Systeme suitable # >= Ruinen (
dogs schreiben Mädchen + : mugs <= € Geometer System
- Käse Straße == && OE ) < EO ]
? Müde Hände | < heiß [ grüßen Symbol KT
Kombination ' juice suit eons Baum erwartet Kind [ /*
?? GS Glas Schrift Geometrie Vögel ] ü / Fenster
Koeffizient MT => \ <= flags > Hüpfen Wolke )
Erlösung Schule ´ Iulius Morgen Kombi Apfel Beobachtung & Wind
amtieren während Amboss aktuell ä Amt ^= Kontakt ^ >=
Bett ;
// " ?. Höhlen build = Haus Hütte Koexistenz Vogel
Buch beobachten Hund >> Maschine ... $ erwartung } *
|= << RW -= >= Nacht *= RL ++ Diktat
_ IU % MB eosin &= Licht Amtsstube Analyse umbringt
! SCH Maus erlitten ß bugs guide Diktatur ( ->
Kaktus Schritt = := @ ö equinoctium größer != Tanne
+ <= Küche Ruine Wiese erwache > erlaubt */ erwachsene
YS >>= ~ Küsse } <<= -- Wasser Höfe Iunius
UI tags Hand Amtsblatt || erleben += { :: Koeln
erlöst { schön bags Systeme suitable # >= Ruinen (
dogs schreiben Mädchen + : mugs <= € Geometer System
- Käse Straße == && OE ) < EO ]
? Müde Hände | < heiß [ grüßen Symbol KT
Kombination ' juice suit eons Baum erwartet Kind [ /*
?? GS Glas Schrift Geometrie Vögel ] ü / Fenster
Koeffizient MT => \ <= flags > Hüpfen Wolke )
Erlösung Schule ´ Iulius Morgen Kombi Apfel Beobachtung & Wind
amtieren während Amboss aktuell ä Amt ^= Kontakt ^ >=
Bett ;
// " ?. Höhlen build = Haus Hütte Koexistenz Vogel
Buch beobachten Hund >> Maschine ... $ erwartung } *
|= << RW -= >= Nacht *= RL ++ Diktat
_ IU % MB eosin &= Licht Amtsstube Analyse umbringt
! SCH Maus erlitten ß bugs guide Diktatur ( ->
Kaktus Schritt = := @ ö equinoctium größer != Tanne
+ <= Küche Ruine Wiese erwache > erlaubt */ erwachsene
YS >>= ~ Küsse } <<= -- Wasser Höfe Iunius
UI tags Hand Amtsblatt || erleben += { :: Koeln
erlöst { schön bags Systeme suitable # >= Ruinen (
dogs schreiben Mädchen + : mugs <= € Geometer System
- Käse Straße == && OE ) < EO ]
? Müde Hände | < heiß [ grüßen Symbol KT
Kombination ' juice suit eons Baum erwartet Kind [ /*
?? GS Glas Schrift Geometrie Vögel ] ü / Fenster
Koeffizient MT => \ <= flags > Hüpfen Wolke )
Erlösung Schule ´ Iulius Morgen Kombi Apfel Beobachtung & Wind
amtieren während Amboss aktuell ä Amt ^= Kontakt ^ >=
Bett ;
```

## Stufe 6 — Wörter (6 Runden · 558 Tokens · 3971 Zeichen)

```
Licht equinoctium Schule Ruine schreiben Mädchen Tanne Küche suit Diktatur
Morgen Hund Bett Vogel Glas Schritt Wind erwache juice Beobachtung
Vögel Müde Käse Amboss bugs Hände grüßen Amt Maus Systeme
Buch dogs suitable Geometer während eons größer tags Analyse Wolke
heiß aktuell Ruinen Schrift erlöst build eosin Hüpfen Haus Amtsblatt
Kaktus Koexistenz Erlösung Koeffizient Kontakt Amtsstube erwartung bags beobachten Koeln
Maschine Iulius amtieren Straße Apfel erwachsene schön Hütte Kind System
Diktat Höfe guide erlaubt erleben Iunius Symbol Geometrie Küsse erlitten
Fenster erwartet Hand Baum mugs Wasser Wiese flags Nacht Höhlen
Kombi Kombination umbringt
Licht equinoctium Schule Ruine schreiben Mädchen Tanne Küche suit Diktatur
Morgen Hund Bett Vogel Glas Schritt Wind erwache juice Beobachtung
Vögel Müde Käse Amboss bugs Hände grüßen Amt Maus Systeme
Buch dogs suitable Geometer während eons größer tags Analyse Wolke
heiß aktuell Ruinen Schrift erlöst build eosin Hüpfen Haus Amtsblatt
Kaktus Koexistenz Erlösung Koeffizient Kontakt Amtsstube erwartung bags beobachten Koeln
Maschine Iulius amtieren Straße Apfel erwachsene schön Hütte Kind System
Diktat Höfe guide erlaubt erleben Iunius Symbol Geometrie Küsse erlitten
Fenster erwartet Hand Baum mugs Wasser Wiese flags Nacht Höhlen
Kombi Kombination umbringt
Licht equinoctium Schule Ruine schreiben Mädchen Tanne Küche suit Diktatur
Morgen Hund Bett Vogel Glas Schritt Wind erwache juice Beobachtung
Vögel Müde Käse Amboss bugs Hände grüßen Amt Maus Systeme
Buch dogs suitable Geometer während eons größer tags Analyse Wolke
heiß aktuell Ruinen Schrift erlöst build eosin Hüpfen Haus Amtsblatt
Kaktus Koexistenz Erlösung Koeffizient Kontakt Amtsstube erwartung bags beobachten Koeln
Maschine Iulius amtieren Straße Apfel erwachsene schön Hütte Kind System
Diktat Höfe guide erlaubt erleben Iunius Symbol Geometrie Küsse erlitten
Fenster erwartet Hand Baum mugs Wasser Wiese flags Nacht Höhlen
Kombi Kombination umbringt
Licht equinoctium Schule Ruine schreiben Mädchen Tanne Küche suit Diktatur
Morgen Hund Bett Vogel Glas Schritt Wind erwache juice Beobachtung
Vögel Müde Käse Amboss bugs Hände grüßen Amt Maus Systeme
Buch dogs suitable Geometer während eons größer tags Analyse Wolke
heiß aktuell Ruinen Schrift erlöst build eosin Hüpfen Haus Amtsblatt
Kaktus Koexistenz Erlösung Koeffizient Kontakt Amtsstube erwartung bags beobachten Koeln
Maschine Iulius amtieren Straße Apfel erwachsene schön Hütte Kind System
Diktat Höfe guide erlaubt erleben Iunius Symbol Geometrie Küsse erlitten
Fenster erwartet Hand Baum mugs Wasser Wiese flags Nacht Höhlen
Kombi Kombination umbringt
Licht equinoctium Schule Ruine schreiben Mädchen Tanne Küche suit Diktatur
Morgen Hund Bett Vogel Glas Schritt Wind erwache juice Beobachtung
Vögel Müde Käse Amboss bugs Hände grüßen Amt Maus Systeme
Buch dogs suitable Geometer während eons größer tags Analyse Wolke
heiß aktuell Ruinen Schrift erlöst build eosin Hüpfen Haus Amtsblatt
Kaktus Koexistenz Erlösung Koeffizient Kontakt Amtsstube erwartung bags beobachten Koeln
Maschine Iulius amtieren Straße Apfel erwachsene schön Hütte Kind System
Diktat Höfe guide erlaubt erleben Iunius Symbol Geometrie Küsse erlitten
Fenster erwartet Hand Baum mugs Wasser Wiese flags Nacht Höhlen
Kombi Kombination umbringt
Licht equinoctium Schule Ruine schreiben Mädchen Tanne Küche suit Diktatur
Morgen Hund Bett Vogel Glas Schritt Wind erwache juice Beobachtung
Vögel Müde Käse Amboss bugs Hände grüßen Amt Maus Systeme
Buch dogs suitable Geometer während eons größer tags Analyse Wolke
heiß aktuell Ruinen Schrift erlöst build eosin Hüpfen Haus Amtsblatt
Kaktus Koexistenz Erlösung Koeffizient Kontakt Amtsstube erwartung bags beobachten Koeln
Maschine Iulius amtieren Straße Apfel erwachsene schön Hütte Kind System
Diktat Höfe guide erlaubt erleben Iunius Symbol Geometrie Küsse erlitten
Fenster erwartet Hand Baum mugs Wasser Wiese flags Nacht Höhlen
Kombi Kombination umbringt
```

## Stufe 7 — Vollpass (Abschluss) (1 Runde · 182 Tokens · 887 Zeichen)

```
Küche erwache &= } EO Diktatur - Höhlen == amtieren
Geometrie | || OE [ erwartet Maus Haus erleben ...
< Straße guide bags / beobachten % ´ Beobachtung "
* Hand + Schule >= |= ) ?. Geometer &&
Vogel ö ! eons aktuell & Müde ; // +=
< Hütte Iulius Buch Wiese Morgen @ Wind Hände /*
MB Wolke : + ++ größer eosin KT heiß umbringt
schreiben Ruinen ' <= ] Licht ?? Küsse Kontakt Koexistenz
= Fenster ( :: grüßen erlaubt Vögel erlöst build )
!= Iunius Apfel Bett Amboss >> -- UI <= {
( erwachsene */ Symbol \ Ruine > € Kind Amt
Amtsblatt ^= erlitten System *= # >= flags YS _
GS Maschine Kombi := ^ bugs ~ Mädchen <= ->
equinoctium Hüpfen = dogs Koeffizient SCH Käse Wasser -= Schrift
juice Kaktus Kombination >>= Nacht RW > Analyse => Systeme
Schritt tags Amtsstube << $ Koeln Höfe während RL ß
] [ schön Glas Baum IU ü ä { suit
suitable } Erlösung mugs MT ? Diktat <<= >= erwartung
Hund Tanne
```
