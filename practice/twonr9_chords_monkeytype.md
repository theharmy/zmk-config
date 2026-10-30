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
| 1 | **Plain** | reines Chord-Gefühl: 16 Plain-Outputs, keine Modifier | 16 Tokens |
| 2 | **Plain + Ctrl + erste Wörter** | Operatoren dazu + allgemeine deutsche Wörter ohne Bigrams (Alpha-Grid übt mit) — immer noch kein Shift | 68 Tokens |
| 3 | **+ a1-Bigrams + Layer-1-Wörter** | a1 komplett: Bigrams + die Wörter, die nur a1-Chords brauchen | 105 Tokens |
| 4 | **Alle Symbole** | Shift-Zustände kommen dazu (+ ´ aus N + R) | 132 Tokens |
| 5 | **+ a2-Bigrams + alle Wörter** | die komplette Keymap: a2-Bigrams (Layerwechsel mitten im Wort) + alle Wörter | 174 Tokens |
| 6 | **Wörter** | alles im echten Tipp-Kontext (93 Wörter) | 93 Tokens |
| 7 | **Vollpass (Abschluss)** | alles in einem Durchgang | 174 Tokens |

### Diagonale Symbol-Chords (16 Chords × 4 Modifier-Zustände = 64 Outputs)

| Chord | Plain | Shift | Ctrl | Ctrl + Shift |
| --- | --- | --- | --- | --- |
| L + N | `(` | `)` | `==` | `!=` |
| Y + E | `)` | `(` | `<=` | `>=` |
| M + R | `[` | `]` | `+=` | `-=` |
| U + A | `]` | `[` | `&=` | `|=` |
| D + T | `{` | `}` | `<<=` | `>>=` |
| O + I | `}` | `{` | `^=` | `*=` |
| M + N | `&` | `*` | `&&` | `||` |
| O + A | `$` | `€` | `??` | `?.` |
| D + R | `~` | `^` | `->` | `=>` |
| Y + I | `<` | `>` | `<<` | `>>` |
| L + T | `!` | `?` | `//` | `...` |
| M + H | `_` | `-` | `++` | `--` |
| U + E | `;` | `'` | `/*` | `*/` |
| O + S | `#` | `%` | `=` | `|` |
| L + H | `:` | `"` | `::` | `:=` |
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
| R + H | _ (auch M + H · Plain) |
| R + T | - (auch M + H · Shift) |
| E + I | : (auch L + H · Plain) |
| S + I | ; (auch U + E · Plain) |

> `_ - : ;` kommen im Pool nur einmal pro Runde vor (Chord-Pfad); beide Wege liefern das gleiche Zeichen.

## Stufe 1 — Plain (131 Runden · 2096 Tokens · 4191 Zeichen)

```
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
/ # ~ : & _ } ] ( !
[ ) $ { ; <
```

## Stufe 2 — Plain + Ctrl + erste Wörter (14 Runden · 952 Tokens · 4115 Zeichen)

```
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
grüßen Hand && heiß ( Tanne <= Hände Höfe !
Bett Nacht Haus ; < += == Hund Vögel }
Glas Hütte ++ Müde Morgen Küsse -> ] << $
Vogel _ { Licht während Fenster Straße ^= größer :
Wolke /* Küche Apfel :: & Mädchen # ?? //
Wasser ~ Kind [ Buch Käse <<= / &= Hüpfen
Wiese Wind Höhlen Maus = Baum + )
```

## Stufe 3 — + a1-Bigrams + Layer-1-Wörter (7 Runden · 735 Tokens · 3877 Zeichen)

```
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
Geometrie juice suit == beobachten Küsse Diktatur _ aktuell Hütte
&= Kaktus + Kombi / & Käse guide Ruinen ;
Amboss Symbol Wiese YS ++ größer Höfe Höhlen Licht umbringt
Kontakt Vögel Analyse build eosin MB erlöst Geometer <<= Hand
Hund ~ Hüpfen grüßen ^= Baum < /* UI Haus
<< Morgen Fenster ( ! Nacht && Mädchen Diktat Systeme
<= während Wolke Vogel += # : Glas Straße ??
) Apfel } erlaubt Hände suitable Tanne EO Kombination RL
-> eons Beobachtung Wasser { Maus Küche $ KT System
// Erlösung Wind :: Ruine = Müde erlitten erleben heiß
Kind Buch [ Bett ]
```

## Stufe 4 — Alle Symbole (6 Runden · 792 Tokens · 3707 Zeichen)

```
=> Hütte <<= ] % { Kombination Hund umbringt Morgen
Kontakt Wind Kind ?. Maus Vogel >>= Vögel Küche Diktatur
*= Käse Haus Hände } >= Symbol Diktat /* Beobachtung
... Hand @ System Erlösung Baum ) Tanne } Müde
&& ^ Buch suitable += ~ ( suit Apfel &=
Systeme erlöst : größer $ == _ */ [ )
" eosin juice ! Ruinen >> ; |= Glas --
eons + | Straße Hüpfen * - -= Geometer Wasser
{ ( Höfe build ' beobachten Mädchen = ?? ?
|| != # Kaktus während erlaubt € :: Geometrie Licht
[ erleben // heiß ´ Wiese Wolke ^= & grüßen
Amboss Ruine / << > ] < \ ++ guide
Fenster -> <= Nacht := Kombi Küsse Analyse Höhlen erlitten
aktuell Bett
=> Hütte <<= ] % { Kombination Hund umbringt Morgen
Kontakt Wind Kind ?. Maus Vogel >>= Vögel Küche Diktatur
*= Käse Haus Hände } >= Symbol Diktat /* Beobachtung
... Hand @ System Erlösung Baum ) Tanne } Müde
&& ^ Buch suitable += ~ ( suit Apfel &=
Systeme erlöst : größer $ == _ */ [ )
" eosin juice ! Ruinen >> ; |= Glas --
eons + | Straße Hüpfen * - -= Geometer Wasser
{ ( Höfe build ' beobachten Mädchen = ?? ?
|| != # Kaktus während erlaubt € :: Geometrie Licht
[ erleben // heiß ´ Wiese Wolke ^= & grüßen
Amboss Ruine / << > ] < \ ++ guide
Fenster -> <= Nacht := Kombi Küsse Analyse Höhlen erlitten
aktuell Bett
=> Hütte <<= ] % { Kombination Hund umbringt Morgen
Kontakt Wind Kind ?. Maus Vogel >>= Vögel Küche Diktatur
*= Käse Haus Hände } >= Symbol Diktat /* Beobachtung
... Hand @ System Erlösung Baum ) Tanne } Müde
&& ^ Buch suitable += ~ ( suit Apfel &=
Systeme erlöst : größer $ == _ */ [ )
" eosin juice ! Ruinen >> ; |= Glas --
eons + | Straße Hüpfen * - -= Geometer Wasser
{ ( Höfe build ' beobachten Mädchen = ?? ?
|| != # Kaktus während erlaubt € :: Geometrie Licht
[ erleben // heiß ´ Wiese Wolke ^= & grüßen
Amboss Ruine / << > ] < \ ++ guide
Fenster -> <= Nacht := Kombi Küsse Analyse Höhlen erlitten
aktuell Bett
=> Hütte <<= ] % { Kombination Hund umbringt Morgen
Kontakt Wind Kind ?. Maus Vogel >>= Vögel Küche Diktatur
*= Käse Haus Hände } >= Symbol Diktat /* Beobachtung
... Hand @ System Erlösung Baum ) Tanne } Müde
&& ^ Buch suitable += ~ ( suit Apfel &=
Systeme erlöst : größer $ == _ */ [ )
" eosin juice ! Ruinen >> ; |= Glas --
eons + | Straße Hüpfen * - -= Geometer Wasser
{ ( Höfe build ' beobachten Mädchen = ?? ?
|| != # Kaktus während erlaubt € :: Geometrie Licht
[ erleben // heiß ´ Wiese Wolke ^= & grüßen
Amboss Ruine / << > ] < \ ++ guide
Fenster -> <= Nacht := Kombi Küsse Analyse Höhlen erlitten
aktuell Bett
=> Hütte <<= ] % { Kombination Hund umbringt Morgen
Kontakt Wind Kind ?. Maus Vogel >>= Vögel Küche Diktatur
*= Käse Haus Hände } >= Symbol Diktat /* Beobachtung
... Hand @ System Erlösung Baum ) Tanne } Müde
&& ^ Buch suitable += ~ ( suit Apfel &=
Systeme erlöst : größer $ == _ */ [ )
" eosin juice ! Ruinen >> ; |= Glas --
eons + | Straße Hüpfen * - -= Geometer Wasser
{ ( Höfe build ' beobachten Mädchen = ?? ?
|| != # Kaktus während erlaubt € :: Geometrie Licht
[ erleben // heiß ´ Wiese Wolke ^= & grüßen
Amboss Ruine / << > ] < \ ++ guide
Fenster -> <= Nacht := Kombi Küsse Analyse Höhlen erlitten
aktuell Bett
=> Hütte <<= ] % { Kombination Hund umbringt Morgen
Kontakt Wind Kind ?. Maus Vogel >>= Vögel Küche Diktatur
*= Käse Haus Hände } >= Symbol Diktat /* Beobachtung
... Hand @ System Erlösung Baum ) Tanne } Müde
&& ^ Buch suitable += ~ ( suit Apfel &=
Systeme erlöst : größer $ == _ */ [ )
" eosin juice ! Ruinen >> ; |= Glas --
eons + | Straße Hüpfen * - -= Geometer Wasser
{ ( Höfe build ' beobachten Mädchen = ?? ?
|| != # Kaktus während erlaubt € :: Geometrie Licht
[ erleben // heiß ´ Wiese Wolke ^= & grüßen
Amboss Ruine / << > ] < \ ++ guide
Fenster -> <= Nacht := Kombi Küsse Analyse Höhlen erlitten
aktuell Bett
```

## Stufe 5 — + a2-Bigrams + alle Wörter (4 Runden · 696 Tokens · 3471 Zeichen)

```
MB ; Bett ?. */ Amt Küche Maus suit }
\ + * umbringt Symbol / << Fenster = /*
$ SCH Hände Höfe schreiben *= bags _ % |=
Müde YS erlitten Kontakt aktuell heiß ä System guide Licht
erleben Diktat Buch < Koexistenz Wasser ü Kaktus erwache >
... IU Amtsblatt &= dogs ( -> -- Apfel -=
:= Tanne tags Amtsstube >>= ~ Ruinen Geometer <<= |
Baum UI Erlösung Kombi Wind OE amtieren || Iunius +=
( ö Koeln Hüpfen { erwartet Schule Geometrie juice ß
++ build [ Maschine Vögel Mädchen KT " mugs //
€ eons erwachsene # Käse == && Nacht ] !
Haus ] erlöst @ - Höhlen { equinoctium ' >>
) Morgen Hund Ruine Analyse GS != bugs eosin Glas
erwartung Vogel [ :: ?? Hand während Schritt erlaubt }
RW ´ größer Koeffizient Kind => RL <= flags ?
Diktatur Straße ) Amboss schön MT Iulius grüßen beobachten Wiese
suitable & Wolke Hütte Beobachtung Kombination EO Schrift ^= Systeme
^ >= Küsse :
MB ; Bett ?. */ Amt Küche Maus suit }
\ + * umbringt Symbol / << Fenster = /*
$ SCH Hände Höfe schreiben *= bags _ % |=
Müde YS erlitten Kontakt aktuell heiß ä System guide Licht
erleben Diktat Buch < Koexistenz Wasser ü Kaktus erwache >
... IU Amtsblatt &= dogs ( -> -- Apfel -=
:= Tanne tags Amtsstube >>= ~ Ruinen Geometer <<= |
Baum UI Erlösung Kombi Wind OE amtieren || Iunius +=
( ö Koeln Hüpfen { erwartet Schule Geometrie juice ß
++ build [ Maschine Vögel Mädchen KT " mugs //
€ eons erwachsene # Käse == && Nacht ] !
Haus ] erlöst @ - Höhlen { equinoctium ' >>
) Morgen Hund Ruine Analyse GS != bugs eosin Glas
erwartung Vogel [ :: ?? Hand während Schritt erlaubt }
RW ´ größer Koeffizient Kind => RL <= flags ?
Diktatur Straße ) Amboss schön MT Iulius grüßen beobachten Wiese
suitable & Wolke Hütte Beobachtung Kombination EO Schrift ^= Systeme
^ >= Küsse :
MB ; Bett ?. */ Amt Küche Maus suit }
\ + * umbringt Symbol / << Fenster = /*
$ SCH Hände Höfe schreiben *= bags _ % |=
Müde YS erlitten Kontakt aktuell heiß ä System guide Licht
erleben Diktat Buch < Koexistenz Wasser ü Kaktus erwache >
... IU Amtsblatt &= dogs ( -> -- Apfel -=
:= Tanne tags Amtsstube >>= ~ Ruinen Geometer <<= |
Baum UI Erlösung Kombi Wind OE amtieren || Iunius +=
( ö Koeln Hüpfen { erwartet Schule Geometrie juice ß
++ build [ Maschine Vögel Mädchen KT " mugs //
€ eons erwachsene # Käse == && Nacht ] !
Haus ] erlöst @ - Höhlen { equinoctium ' >>
) Morgen Hund Ruine Analyse GS != bugs eosin Glas
erwartung Vogel [ :: ?? Hand während Schritt erlaubt }
RW ´ größer Koeffizient Kind => RL <= flags ?
Diktatur Straße ) Amboss schön MT Iulius grüßen beobachten Wiese
suitable & Wolke Hütte Beobachtung Kombination EO Schrift ^= Systeme
^ >= Küsse :
MB ; Bett ?. */ Amt Küche Maus suit }
\ + * umbringt Symbol / << Fenster = /*
$ SCH Hände Höfe schreiben *= bags _ % |=
Müde YS erlitten Kontakt aktuell heiß ä System guide Licht
erleben Diktat Buch < Koexistenz Wasser ü Kaktus erwache >
... IU Amtsblatt &= dogs ( -> -- Apfel -=
:= Tanne tags Amtsstube >>= ~ Ruinen Geometer <<= |
Baum UI Erlösung Kombi Wind OE amtieren || Iunius +=
( ö Koeln Hüpfen { erwartet Schule Geometrie juice ß
++ build [ Maschine Vögel Mädchen KT " mugs //
€ eons erwachsene # Käse == && Nacht ] !
Haus ] erlöst @ - Höhlen { equinoctium ' >>
) Morgen Hund Ruine Analyse GS != bugs eosin Glas
erwartung Vogel [ :: ?? Hand während Schritt erlaubt }
RW ´ größer Koeffizient Kind => RL <= flags ?
Diktatur Straße ) Amboss schön MT Iulius grüßen beobachten Wiese
suitable & Wolke Hütte Beobachtung Kombination EO Schrift ^= Systeme
^ >= Küsse :
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

## Stufe 7 — Vollpass (Abschluss) (1 Runde · 174 Tokens · 867 Zeichen)

```
KT : ; &= */ MT Kontakt == ! ::
suitable # beobachten erlitten Höfe Beobachtung erwartet - UI Straße
Wolke heiß -- * MB Baum Haus Vögel erlaubt guide
) |= ) ?. > && Tanne ´ eons Kaktus
Hände & Kombination /* += equinoctium amtieren OE Wiese Koeffizient
\ @ GS schreiben Erlösung || Nacht Schule Müde erwache
eosin ä System Systeme erwartung Ruinen / <= } größer
?? Küsse Diktatur Koexistenz < Fenster [ ö grüßen ...
erleben -> ] != Diktat Bett Wasser >> | Maus
// ( ( erwachsene := build RL Küche _ €
Vogel Schritt Amtsblatt ^= Mädchen Geometrie *= ß >= flags
aktuell % Hand Maschine ü ^ bugs ~ " Höhlen
{ Geometer IU Iunius Kombi = Symbol + dogs Wind
Hüpfen Morgen -= Schrift juice Analyse >>= Buch Hund ?
=> Ruine suit tags bags << $ Koeln erlöst Hütte
SCH YS ] [ Iulius während Glas Licht RW EO
{ Amt Amtsstube } Amboss mugs Kind ' umbringt <<=
++ schön Apfel Käse
```
