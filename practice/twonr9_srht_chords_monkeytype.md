# TwoNr9 srht — Chord-Praxis (Monkeytype)

Stufen nach Häufigkeit: erst echte Wörter mit den täglichen Symbolen, dann Bigramme, die zweite Ebene, und die Symbol-Zustände in zunehmender Seltenheit. Jede Stufe enthält alles aus den vorigen; die Remixe mischen Symbole und Wörter neu. Die Chords werden aus Firmware und Zeichnung gelesen, nicht von Hand gepflegt.

## Nutzung in Monkeytype

1. Den Block der Stufe kopieren (Code-Block, unter 10.000 Zeichen).
2. Monkeytype → Test Type **Custom** → Text einfügen.
3. Erst zur nächsten Stufe, wenn die aktuelle sauber läuft. Die Remixe gehen nach Stufe 8.

## Legende

### Stufen

| Stufe | Name | Was er übt | Tokens |
| --- | --- | --- | --- |
| 1 | Erste Wörter | a1-Wörter ohne Bigramme (47) und die häufigsten Symbole | 57 |
| 2 | + Grundsymbole | Klammern, Anführungszeichen und die restlichen Paare | 69 |
| 3 | + a1-Bigramme | a1-Bigramme, Umlaute, ´ und die Wörter mit ihnen | 126 |
| 4 | + Layer 2 | a2-Bigramme und -Wörter, Layerwechsel mitten im Wort | 153 |
| 5 | + Operatoren | Cmd-Zustände: && ‖ == != += <= >= -> => | 169 |
| 6 | + Escapes | Shift+Cmd: \( \) \[ \] \{ \} \$ \^ \_ | 182 |
| 7 | + Alt (Doppelte) | Alt-Zustände: ** -- :: ~~ !! und die Wortpaare | 208 |
| 8 | Vollpass | die restlichen Symbole, Ctrl-Escapes und die Vier-Tasten-Zustände | 237 |
| R1 | Symbole kompakt | jedes Symbol und jeder Bigramm ohne Wörter | 123 |
| R2 | Operatoren | Cmd-, Alt- und Quad-Zustände mit Wörtern gemischt | 148 |
| W | Wörter | nur Wörter (114), kein Symbol | 114 |

### Chords nach Paar

| Paar | Plain | + Shift | + Ctrl | + Cmd | + Alt | Quad |
| --- | --- | --- | --- | --- | --- | --- |
| L + S | `/` | `./` | `//` | `/*` | — | `*/` |
| L + H | `-` | `_` | `\_` | `--` | `---` | `__` |
| L + T | `&` | `\|` | `\&` | `&&` | `&=` | `\|\|` |
| N + S | `[` | `]` | `[]` | `\[` | `[[` | `\]` |
| N + R | `{` | `}` | `{}` | `\{` | `{{` | `\}` |
| N + T | `(` | `)` | `()` | `==` | `=>` | `!=` |
| D + S | `$` | `^` | — | `\$` | `$$` | `\^` |
| D + R | `"` | `'` | — | `""` | `'''` | `''` |
| D + H | `<` | `>` | `->` | `<=` | `<<` | `>=` |
| Y + E | `,` | `.` | — | `..` | `...` | `..<` |
| Y + I | `!` | `?` | — | `?.` | `!!` | `?:` |
| Y + A | `` ` `` | — | `` `` `` | `` ``` `` | `~~~` | — |
| O + C | `;` | `:` | — | `::` | `;;` | — |
| O + I | `*` | `#` | `\#` | `**` | `###` | `##` |
| O + A | `@` | `~` | `~~` | — | `€` | — |
| U + C | `%` | `%s` | `\%` | — | `%%` | — |
| U + E | `=` | `+` | `^=` | `-=` | `\|=` | `+=` |
| U + A | `\` | `\(` | `\\` | `\)` | `\n` | — |

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

**Stufe 1**, ohne Bigram-Paare: Haus, Maus, Hund, Kind, Wind, Hand, Nacht, Licht, Wasser, Baum, Apfel, Vogel, Wolke, Fenster, Buch, Bett, Morgen, Glas, Wiese, Tanne, Symbol, Kombi, Amboss, Kombination, umbringt, System, Systeme, Analyse, erwartet, erwartung, erwachsene, erwache, Amt, Amtsstube, Amtsblatt, amtieren, Schule, Maschine, schreiben, Schrift, Schritt, bags, dogs, tags, flags, mugs, bugs

**Stufe 3**, a1-Bigramme: erleben, erlöst, erlitten, erlaubt, Erlösung, Sohn, Kahn, Hahn, Mohn, wohnen, Landtag, verwandt, Handtuch, Bicycle, Cyclist, Cyber, Geometrie, beobachten, Beobachtung, Geometer, eons, eosin, Ruine, Ruinen, build, suit, suitable, juice, guide

**Stufe 4**, a2-Bigramme (Layerwechsel): Norm, Formel, warm, Wärme, Anbau, Einbau, anbei, aktuell, Diktat, Diktatur, Kontakt, Kaktus, Gymnasium, Biology, Energy, Koeffizient, Koexistenz, Koeln, Iulius, Iunius, equinoctium

### Adaptive Keys (Wörter, nur srht)

Innerhalb von 300 ms nach dem Trigger gibt ein adaptiver Key den Partner aus — schnelles `rh` kann als `rl` herauskommen. Die Chords (beide Tasten gleichzeitig) sind nicht betroffen.

## Stufe 1 — Erste Wörter (12 Runden · 684 Tokens · 4103 Zeichen)

```
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
Symbol Amtsstube Kombi Amtsblatt flags Apfel Wiese Maus Amt System
= Wolke bags Wind Kombination ( Schritt ; Kind Haus
Analyse Licht Bett tags dogs . erwachsene erwartung Maschine Schrift
amtieren Hand Amboss ) schreiben erwache - Schule Systeme /
Morgen _ : umbringt Baum Fenster Buch Hund Vogel mugs
Wasser bugs Nacht erwartet Glas , Tanne
```

## Stufe 2 — + Grundsymbole (11 Runden · 759 Tokens · 4025 Zeichen)

```
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
/ Wiese Amt Wolke tags Glas Haus , _ :
Apfel Maschine - Amtsblatt ] Schrift Baum " Morgen Schule
flags Hand mugs Analyse } Licht ; { umbringt >
System schreiben Amboss Vogel Wind ' ! ( . Kombi
< Buch [ erwartet ? dogs erwachsene Nacht * Fenster
Kombination Systeme = Schritt Wasser ) amtieren Hund bugs +
Symbol Bett Tanne Kind Amtsstube erwartung bags erwache Maus
```

## Stufe 3 — + a1-Bigramme (5 Runden · 630 Tokens · 3574 Zeichen)

```
tags erwache Küsse Erlösung ! Mädchen ( Kombi ] Handtuch
beobachten Cyclist rl erlöst heiß guide ; Vogel . Hahn
Hände Bett schreiben Amboss ´ Glas Mohn Tanne ? Baum
Cyber Wolke Analyse Nacht erlitten Apfel Kahn Maschine Morgen erwartet
während _ build ß erleben Käse Ruinen } Amtsblatt Küche
juice dt Geometer Straße > mugs Vögel * Schritt Wasser
{ wohnen System Geometrie Sohn grüßen Müde , erlaubt Haus
Symbol flags Bicycle eosin suit amtieren - Wiese Fenster Buch
eo + : [ ö Kombination Maus / Hand Hüpfen
' suitable größer < Schule Höhlen Hütte verwandt Amt umbringt
eons Beobachtung Höfe bugs Wind Schrift cy Licht Landtag Amtsstube
schön Systeme ü dogs erwachsene Ruine erwartung hn ä ui
" bags = Hund ) Kind
tags erwache Küsse Erlösung ! Mädchen ( Kombi ] Handtuch
beobachten Cyclist rl erlöst heiß guide ; Vogel . Hahn
Hände Bett schreiben Amboss ´ Glas Mohn Tanne ? Baum
Cyber Wolke Analyse Nacht erlitten Apfel Kahn Maschine Morgen erwartet
während _ build ß erleben Käse Ruinen } Amtsblatt Küche
juice dt Geometer Straße > mugs Vögel * Schritt Wasser
{ wohnen System Geometrie Sohn grüßen Müde , erlaubt Haus
Symbol flags Bicycle eosin suit amtieren - Wiese Fenster Buch
eo + : [ ö Kombination Maus / Hand Hüpfen
' suitable größer < Schule Höhlen Hütte verwandt Amt umbringt
eons Beobachtung Höfe bugs Wind Schrift cy Licht Landtag Amtsstube
schön Systeme ü dogs erwachsene Ruine erwartung hn ä ui
" bags = Hund ) Kind
tags erwache Küsse Erlösung ! Mädchen ( Kombi ] Handtuch
beobachten Cyclist rl erlöst heiß guide ; Vogel . Hahn
Hände Bett schreiben Amboss ´ Glas Mohn Tanne ? Baum
Cyber Wolke Analyse Nacht erlitten Apfel Kahn Maschine Morgen erwartet
während _ build ß erleben Käse Ruinen } Amtsblatt Küche
juice dt Geometer Straße > mugs Vögel * Schritt Wasser
{ wohnen System Geometrie Sohn grüßen Müde , erlaubt Haus
Symbol flags Bicycle eosin suit amtieren - Wiese Fenster Buch
eo + : [ ö Kombination Maus / Hand Hüpfen
' suitable größer < Schule Höhlen Hütte verwandt Amt umbringt
eons Beobachtung Höfe bugs Wind Schrift cy Licht Landtag Amtsstube
schön Systeme ü dogs erwachsene Ruine erwartung hn ä ui
" bags = Hund ) Kind
tags erwache Küsse Erlösung ! Mädchen ( Kombi ] Handtuch
beobachten Cyclist rl erlöst heiß guide ; Vogel . Hahn
Hände Bett schreiben Amboss ´ Glas Mohn Tanne ? Baum
Cyber Wolke Analyse Nacht erlitten Apfel Kahn Maschine Morgen erwartet
während _ build ß erleben Käse Ruinen } Amtsblatt Küche
juice dt Geometer Straße > mugs Vögel * Schritt Wasser
{ wohnen System Geometrie Sohn grüßen Müde , erlaubt Haus
Symbol flags Bicycle eosin suit amtieren - Wiese Fenster Buch
eo + : [ ö Kombination Maus / Hand Hüpfen
' suitable größer < Schule Höhlen Hütte verwandt Amt umbringt
eons Beobachtung Höfe bugs Wind Schrift cy Licht Landtag Amtsstube
schön Systeme ü dogs erwachsene Ruine erwartung hn ä ui
" bags = Hund ) Kind
tags erwache Küsse Erlösung ! Mädchen ( Kombi ] Handtuch
beobachten Cyclist rl erlöst heiß guide ; Vogel . Hahn
Hände Bett schreiben Amboss ´ Glas Mohn Tanne ? Baum
Cyber Wolke Analyse Nacht erlitten Apfel Kahn Maschine Morgen erwartet
während _ build ß erleben Käse Ruinen } Amtsblatt Küche
juice dt Geometer Straße > mugs Vögel * Schritt Wasser
{ wohnen System Geometrie Sohn grüßen Müde , erlaubt Haus
Symbol flags Bicycle eosin suit amtieren - Wiese Fenster Buch
eo + : [ ö Kombination Maus / Hand Hüpfen
' suitable größer < Schule Höhlen Hütte verwandt Amt umbringt
eons Beobachtung Höfe bugs Wind Schrift cy Licht Landtag Amtsstube
schön Systeme ü dogs erwachsene Ruine erwartung hn ä ui
" bags = Hund ) Kind
```

## Stufe 4 — + Layer 2 (4 Runden · 612 Tokens · 3575 Zeichen)

```
Amt Einbau grüßen Koeln flags Schritt erwartung = Baum equinoctium
[ Beobachtung . > nb warm Wasser ) Licht Anbau
Landtag umbringt erlöst aktuell Hände dogs Buch Maus Schule suit
iu Symbol - Norm System Hand Cyclist Mohn Diktat Hahn
Sohn rm Käse + Nacht cy Geometrie erleben Biology :
Amtsblatt Vögel Hüpfen Ruine Iunius schön Vogel Handtuch Wärme oe
Gymnasium ´ Kontakt dt Kombi Tanne ui Bicycle Erlösung Iulius
suitable ö Geometer ? Glas rl Morgen amtieren eons hn
Diktatur beobachten Bett } Kombination " schreiben Kind erlaubt Apfel
Koeffizient < Formel guide , ä Cyber { Energy (
! verwandt Hund Hütte Amboss Analyse Höhlen anbei Amtsstube eo
gy Haus Ruinen tags erwartet ü build mugs Schrift Systeme
_ / Fenster bags erlitten Höfe ] bugs Müde Wind
während kt ß Wolke heiß erwachsene erwache Küsse ; Maschine
Wiese * Mädchen größer ' Kaktus juice eosin Küche Kahn
wohnen Straße Koexistenz
Amt Einbau grüßen Koeln flags Schritt erwartung = Baum equinoctium
[ Beobachtung . > nb warm Wasser ) Licht Anbau
Landtag umbringt erlöst aktuell Hände dogs Buch Maus Schule suit
iu Symbol - Norm System Hand Cyclist Mohn Diktat Hahn
Sohn rm Käse + Nacht cy Geometrie erleben Biology :
Amtsblatt Vögel Hüpfen Ruine Iunius schön Vogel Handtuch Wärme oe
Gymnasium ´ Kontakt dt Kombi Tanne ui Bicycle Erlösung Iulius
suitable ö Geometer ? Glas rl Morgen amtieren eons hn
Diktatur beobachten Bett } Kombination " schreiben Kind erlaubt Apfel
Koeffizient < Formel guide , ä Cyber { Energy (
! verwandt Hund Hütte Amboss Analyse Höhlen anbei Amtsstube eo
gy Haus Ruinen tags erwartet ü build mugs Schrift Systeme
_ / Fenster bags erlitten Höfe ] bugs Müde Wind
während kt ß Wolke heiß erwachsene erwache Küsse ; Maschine
Wiese * Mädchen größer ' Kaktus juice eosin Küche Kahn
wohnen Straße Koexistenz
Amt Einbau grüßen Koeln flags Schritt erwartung = Baum equinoctium
[ Beobachtung . > nb warm Wasser ) Licht Anbau
Landtag umbringt erlöst aktuell Hände dogs Buch Maus Schule suit
iu Symbol - Norm System Hand Cyclist Mohn Diktat Hahn
Sohn rm Käse + Nacht cy Geometrie erleben Biology :
Amtsblatt Vögel Hüpfen Ruine Iunius schön Vogel Handtuch Wärme oe
Gymnasium ´ Kontakt dt Kombi Tanne ui Bicycle Erlösung Iulius
suitable ö Geometer ? Glas rl Morgen amtieren eons hn
Diktatur beobachten Bett } Kombination " schreiben Kind erlaubt Apfel
Koeffizient < Formel guide , ä Cyber { Energy (
! verwandt Hund Hütte Amboss Analyse Höhlen anbei Amtsstube eo
gy Haus Ruinen tags erwartet ü build mugs Schrift Systeme
_ / Fenster bags erlitten Höfe ] bugs Müde Wind
während kt ß Wolke heiß erwachsene erwache Küsse ; Maschine
Wiese * Mädchen größer ' Kaktus juice eosin Küche Kahn
wohnen Straße Koexistenz
Amt Einbau grüßen Koeln flags Schritt erwartung = Baum equinoctium
[ Beobachtung . > nb warm Wasser ) Licht Anbau
Landtag umbringt erlöst aktuell Hände dogs Buch Maus Schule suit
iu Symbol - Norm System Hand Cyclist Mohn Diktat Hahn
Sohn rm Käse + Nacht cy Geometrie erleben Biology :
Amtsblatt Vögel Hüpfen Ruine Iunius schön Vogel Handtuch Wärme oe
Gymnasium ´ Kontakt dt Kombi Tanne ui Bicycle Erlösung Iulius
suitable ö Geometer ? Glas rl Morgen amtieren eons hn
Diktatur beobachten Bett } Kombination " schreiben Kind erlaubt Apfel
Koeffizient < Formel guide , ä Cyber { Energy (
! verwandt Hund Hütte Amboss Analyse Höhlen anbei Amtsstube eo
gy Haus Ruinen tags erwartet ü build mugs Schrift Systeme
_ / Fenster bags erlitten Höfe ] bugs Müde Wind
während kt ß Wolke heiß erwachsene erwache Küsse ; Maschine
Wiese * Mädchen größer ' Kaktus juice eosin Küche Kahn
wohnen Straße Koexistenz
```

## Stufe 5 — + Operatoren (4 Runden · 676 Tokens · 3771 Zeichen)

```
Geometrie verwandt flags erlöst schön /* ! erwache * build
System Kombination schreiben Höfe Ruine Geometer eons Diktat / kt
{ Hände -= Hütte , Bett Höhlen Koeffizient ö erwartet
? ui ´ ; Amt nb Kontakt ) _ }
heiß Schule Cyclist Tanne aktuell ?. Hüpfen suit tags "
erlaubt Buch Handtuch Haus Amtsblatt ( Kaktus Vogel Küche Norm
Iulius iu Straße Beobachtung -- Wiese : während dt Vögel
cy Koeln Wärme Analyse <= Apfel Hand ' ** Bicycle
Morgen Gymnasium Iunius Diktatur ] guide anbei Fenster Energy Landtag
&& rm < "" dogs erwartung \[ eosin = Kahn
Hund Systeme Käse Wolke Schritt größer Baum Cyber > mugs
Kombi \) suitable Schrift Wind erleben Küsse == Koexistenz ü
Kind Glas Maschine - warm bugs hn Wasser [ erwachsene
Mädchen wohnen \{ Ruinen Symbol ß + Sohn .. grüßen
amtieren rl Nacht :: bags juice Erlösung Maus gy equinoctium
ä ``` Mohn Anbau erlitten Biology umbringt Müde beobachten Einbau
oe eo \$ Amboss Formel Amtsstube Licht Hahn .
Geometrie verwandt flags erlöst schön /* ! erwache * build
System Kombination schreiben Höfe Ruine Geometer eons Diktat / kt
{ Hände -= Hütte , Bett Höhlen Koeffizient ö erwartet
? ui ´ ; Amt nb Kontakt ) _ }
heiß Schule Cyclist Tanne aktuell ?. Hüpfen suit tags "
erlaubt Buch Handtuch Haus Amtsblatt ( Kaktus Vogel Küche Norm
Iulius iu Straße Beobachtung -- Wiese : während dt Vögel
cy Koeln Wärme Analyse <= Apfel Hand ' ** Bicycle
Morgen Gymnasium Iunius Diktatur ] guide anbei Fenster Energy Landtag
&& rm < "" dogs erwartung \[ eosin = Kahn
Hund Systeme Käse Wolke Schritt größer Baum Cyber > mugs
Kombi \) suitable Schrift Wind erleben Küsse == Koexistenz ü
Kind Glas Maschine - warm bugs hn Wasser [ erwachsene
Mädchen wohnen \{ Ruinen Symbol ß + Sohn .. grüßen
amtieren rl Nacht :: bags juice Erlösung Maus gy equinoctium
ä ``` Mohn Anbau erlitten Biology umbringt Müde beobachten Einbau
oe eo \$ Amboss Formel Amtsstube Licht Hahn .
Geometrie verwandt flags erlöst schön /* ! erwache * build
System Kombination schreiben Höfe Ruine Geometer eons Diktat / kt
{ Hände -= Hütte , Bett Höhlen Koeffizient ö erwartet
? ui ´ ; Amt nb Kontakt ) _ }
heiß Schule Cyclist Tanne aktuell ?. Hüpfen suit tags "
erlaubt Buch Handtuch Haus Amtsblatt ( Kaktus Vogel Küche Norm
Iulius iu Straße Beobachtung -- Wiese : während dt Vögel
cy Koeln Wärme Analyse <= Apfel Hand ' ** Bicycle
Morgen Gymnasium Iunius Diktatur ] guide anbei Fenster Energy Landtag
&& rm < "" dogs erwartung \[ eosin = Kahn
Hund Systeme Käse Wolke Schritt größer Baum Cyber > mugs
Kombi \) suitable Schrift Wind erleben Küsse == Koexistenz ü
Kind Glas Maschine - warm bugs hn Wasser [ erwachsene
Mädchen wohnen \{ Ruinen Symbol ß + Sohn .. grüßen
amtieren rl Nacht :: bags juice Erlösung Maus gy equinoctium
ä ``` Mohn Anbau erlitten Biology umbringt Müde beobachten Einbau
oe eo \$ Amboss Formel Amtsstube Licht Hahn .
Geometrie verwandt flags erlöst schön /* ! erwache * build
System Kombination schreiben Höfe Ruine Geometer eons Diktat / kt
{ Hände -= Hütte , Bett Höhlen Koeffizient ö erwartet
? ui ´ ; Amt nb Kontakt ) _ }
heiß Schule Cyclist Tanne aktuell ?. Hüpfen suit tags "
erlaubt Buch Handtuch Haus Amtsblatt ( Kaktus Vogel Küche Norm
Iulius iu Straße Beobachtung -- Wiese : während dt Vögel
cy Koeln Wärme Analyse <= Apfel Hand ' ** Bicycle
Morgen Gymnasium Iunius Diktatur ] guide anbei Fenster Energy Landtag
&& rm < "" dogs erwartung \[ eosin = Kahn
Hund Systeme Käse Wolke Schritt größer Baum Cyber > mugs
Kombi \) suitable Schrift Wind erleben Küsse == Koexistenz ü
Kind Glas Maschine - warm bugs hn Wasser [ erwachsene
Mädchen wohnen \{ Ruinen Symbol ß + Sohn .. grüßen
amtieren rl Nacht :: bags juice Erlösung Maus gy equinoctium
ä ``` Mohn Anbau erlitten Biology umbringt Müde beobachten Einbau
oe eo \$ Amboss Formel Amtsstube Licht Hahn .
```

## Stufe 6 — + Escapes (4 Runden · 728 Tokens · 3931 Zeichen)

```
..< erwartet System Hand Cyber * Straße += < Formel
Amtsstube bags "" Diktatur ' ( wohnen :: eons ?:
hn ! \} guide ´ build Mohn Käse Symbol Haus
juice ui eo \] ] <= Schrift Kombination mugs aktuell
rl anbei Maschine heiß Landtag Hände Kind Diktat . Bicycle
eosin verwandt Apfel suitable Amboss { Kaktus Biology Wind =
+ dt nb .. -= Nacht */ kt Cyclist ä
, Wasser / erwachsene Buch dogs erlaubt Geometer Gymnasium ```
Hahn Küsse >= Beobachtung erleben Höfe Einbau || erlöst equinoctium
iu Koeln rm \^ > Hund erwache erwartung größer ß
: oe ; ) gy /* == \) flags }
Hüpfen Hütte warm während Amt Ruine Glas Vögel Höhlen Geometrie
_ Tanne && Sohn umbringt '' Koexistenz Anbau Kontakt Baum
Wolke beobachten Iulius tags \{ Ruinen Mädchen schreiben amtieren -
schön Koeffizient Maus Systeme Amtsblatt Bett \$ suit Energy Schritt
Kombi -- ?. ? Licht Kahn Iunius grüßen \[ [
Norm ü cy ## Müde Handtuch bugs ö ** Analyse
Wärme Vogel Wiese __ Morgen Schule != Fenster " Küche
erlitten Erlösung
..< erwartet System Hand Cyber * Straße += < Formel
Amtsstube bags "" Diktatur ' ( wohnen :: eons ?:
hn ! \} guide ´ build Mohn Käse Symbol Haus
juice ui eo \] ] <= Schrift Kombination mugs aktuell
rl anbei Maschine heiß Landtag Hände Kind Diktat . Bicycle
eosin verwandt Apfel suitable Amboss { Kaktus Biology Wind =
+ dt nb .. -= Nacht */ kt Cyclist ä
, Wasser / erwachsene Buch dogs erlaubt Geometer Gymnasium ```
Hahn Küsse >= Beobachtung erleben Höfe Einbau || erlöst equinoctium
iu Koeln rm \^ > Hund erwache erwartung größer ß
: oe ; ) gy /* == \) flags }
Hüpfen Hütte warm während Amt Ruine Glas Vögel Höhlen Geometrie
_ Tanne && Sohn umbringt '' Koexistenz Anbau Kontakt Baum
Wolke beobachten Iulius tags \{ Ruinen Mädchen schreiben amtieren -
schön Koeffizient Maus Systeme Amtsblatt Bett \$ suit Energy Schritt
Kombi -- ?. ? Licht Kahn Iunius grüßen \[ [
Norm ü cy ## Müde Handtuch bugs ö ** Analyse
Wärme Vogel Wiese __ Morgen Schule != Fenster " Küche
erlitten Erlösung
..< erwartet System Hand Cyber * Straße += < Formel
Amtsstube bags "" Diktatur ' ( wohnen :: eons ?:
hn ! \} guide ´ build Mohn Käse Symbol Haus
juice ui eo \] ] <= Schrift Kombination mugs aktuell
rl anbei Maschine heiß Landtag Hände Kind Diktat . Bicycle
eosin verwandt Apfel suitable Amboss { Kaktus Biology Wind =
+ dt nb .. -= Nacht */ kt Cyclist ä
, Wasser / erwachsene Buch dogs erlaubt Geometer Gymnasium ```
Hahn Küsse >= Beobachtung erleben Höfe Einbau || erlöst equinoctium
iu Koeln rm \^ > Hund erwache erwartung größer ß
: oe ; ) gy /* == \) flags }
Hüpfen Hütte warm während Amt Ruine Glas Vögel Höhlen Geometrie
_ Tanne && Sohn umbringt '' Koexistenz Anbau Kontakt Baum
Wolke beobachten Iulius tags \{ Ruinen Mädchen schreiben amtieren -
schön Koeffizient Maus Systeme Amtsblatt Bett \$ suit Energy Schritt
Kombi -- ?. ? Licht Kahn Iunius grüßen \[ [
Norm ü cy ## Müde Handtuch bugs ö ** Analyse
Wärme Vogel Wiese __ Morgen Schule != Fenster " Küche
erlitten Erlösung
..< erwartet System Hand Cyber * Straße += < Formel
Amtsstube bags "" Diktatur ' ( wohnen :: eons ?:
hn ! \} guide ´ build Mohn Käse Symbol Haus
juice ui eo \] ] <= Schrift Kombination mugs aktuell
rl anbei Maschine heiß Landtag Hände Kind Diktat . Bicycle
eosin verwandt Apfel suitable Amboss { Kaktus Biology Wind =
+ dt nb .. -= Nacht */ kt Cyclist ä
, Wasser / erwachsene Buch dogs erlaubt Geometer Gymnasium ```
Hahn Küsse >= Beobachtung erleben Höfe Einbau || erlöst equinoctium
iu Koeln rm \^ > Hund erwache erwartung größer ß
: oe ; ) gy /* == \) flags }
Hüpfen Hütte warm während Amt Ruine Glas Vögel Höhlen Geometrie
_ Tanne && Sohn umbringt '' Koexistenz Anbau Kontakt Baum
Wolke beobachten Iulius tags \{ Ruinen Mädchen schreiben amtieren -
schön Koeffizient Maus Systeme Amtsblatt Bett \$ suit Energy Schritt
Kombi -- ?. ? Licht Kahn Iunius grüßen \[ [
Norm ü cy ## Müde Handtuch bugs ö ** Analyse
Wärme Vogel Wiese __ Morgen Schule != Fenster " Küche
erlitten Erlösung
```

## Stufe 7 — + Alt (Doppelte) (3 Runden · 624 Tokens · 3197 Zeichen)

```
ä Maschine => __ >> Sohn Biology Wind größer ´
Haus Cyclist build Licht Hund Straße Hüpfen Hahn € Buch
Käse System + Ruinen Cyber = Systeme erwartung mugs **
eons suitable Schritt nb Norm ``` Analyse <= '' suit
. ### Koexistenz ! ?. ... Erlösung >= hn +=
erlaubt , -- ; Iulius > umbringt rm Einbau erlitten
ui } erwache [[ ) kt -= / Kombination !?
}} oe --- Kombi aktuell ( &= Handtuch Höfe Amtsstube
Anbau Geometrie Wärme _ ü \[ != dt Kahn Amboss
&& Hütte \] " Nacht ..< Symbol Koeln erwachsene Vögel
Kaktus \{ Gymnasium Iunius Formel Schule { Fenster Bicycle '
Müde "" Energy Mohn Mädchen Amt Koeffizient Wolke Kind &=
Hand rl guide Schrift : heiß dogs Apfel Maus Ruine
|= schön [ |= flags .. < \^ \} Bett
Landtag !! ? $$ ] Beobachtung tags Amtsblatt \t juice
* \n ++ \) während Geometer erleben Vogel Diktat ~~~
\$ << warm anbei Tanne Küche Küsse bags Kontakt amtieren
Diktatur ''' %% {{ schreiben erwartet """ eosin beobachten ö
:: cy Baum || ?: Wasser ;; wohnen erlöst */
Hände ß ## eo Morgen equinoctium == Glas gy ]]
grüßen - iu Wiese bugs /* Höhlen verwandt
ä Maschine => __ >> Sohn Biology Wind größer ´
Haus Cyclist build Licht Hund Straße Hüpfen Hahn € Buch
Käse System + Ruinen Cyber = Systeme erwartung mugs **
eons suitable Schritt nb Norm ``` Analyse <= '' suit
. ### Koexistenz ! ?. ... Erlösung >= hn +=
erlaubt , -- ; Iulius > umbringt rm Einbau erlitten
ui } erwache [[ ) kt -= / Kombination !?
}} oe --- Kombi aktuell ( &= Handtuch Höfe Amtsstube
Anbau Geometrie Wärme _ ü \[ != dt Kahn Amboss
&& Hütte \] " Nacht ..< Symbol Koeln erwachsene Vögel
Kaktus \{ Gymnasium Iunius Formel Schule { Fenster Bicycle '
Müde "" Energy Mohn Mädchen Amt Koeffizient Wolke Kind &=
Hand rl guide Schrift : heiß dogs Apfel Maus Ruine
|= schön [ |= flags .. < \^ \} Bett
Landtag !! ? $$ ] Beobachtung tags Amtsblatt \t juice
* \n ++ \) während Geometer erleben Vogel Diktat ~~~
\$ << warm anbei Tanne Küche Küsse bags Kontakt amtieren
Diktatur ''' %% {{ schreiben erwartet """ eosin beobachten ö
:: cy Baum || ?: Wasser ;; wohnen erlöst */
Hände ß ## eo Morgen equinoctium == Glas gy ]]
grüßen - iu Wiese bugs /* Höhlen verwandt
ä Maschine => __ >> Sohn Biology Wind größer ´
Haus Cyclist build Licht Hund Straße Hüpfen Hahn € Buch
Käse System + Ruinen Cyber = Systeme erwartung mugs **
eons suitable Schritt nb Norm ``` Analyse <= '' suit
. ### Koexistenz ! ?. ... Erlösung >= hn +=
erlaubt , -- ; Iulius > umbringt rm Einbau erlitten
ui } erwache [[ ) kt -= / Kombination !?
}} oe --- Kombi aktuell ( &= Handtuch Höfe Amtsstube
Anbau Geometrie Wärme _ ü \[ != dt Kahn Amboss
&& Hütte \] " Nacht ..< Symbol Koeln erwachsene Vögel
Kaktus \{ Gymnasium Iunius Formel Schule { Fenster Bicycle '
Müde "" Energy Mohn Mädchen Amt Koeffizient Wolke Kind &=
Hand rl guide Schrift : heiß dogs Apfel Maus Ruine
|= schön [ |= flags .. < \^ \} Bett
Landtag !! ? $$ ] Beobachtung tags Amtsblatt \t juice
* \n ++ \) während Geometer erleben Vogel Diktat ~~~
\$ << warm anbei Tanne Küche Küsse bags Kontakt amtieren
Diktatur ''' %% {{ schreiben erwartet """ eosin beobachten ö
:: cy Baum || ?: Wasser ;; wohnen erlöst */
Hände ß ## eo Morgen equinoctium == Glas gy ]]
grüßen - iu Wiese bugs /* Höhlen verwandt
```

## Stufe 8 — Vollpass (3 Runden · 711 Tokens · 3434 Zeichen)

```
Iulius ... [[ ' Hund Beobachtung tags ?: Höhlen Wind
`` ^= \t Kontakt Tanne ^ || ´ ;; ->
+ suitable Wiese oe \( ..< Kaktus ``` : #
[] << erlitten Geometer \) % Diktatur juice ] ~~~
!! amtieren ( Straße dt \ != Cyber Norm \\
= erwachsene Symbol Landtag \% Koexistenz nb warm Mädchen Höfe
beobachten // Apfel Erlösung [^] flags Küche Bett -= erwache
''' ; %% \_ Kahn Amtsstube Wasser -- ]] >
Müde () größer eons \& __ verwandt """ [ Nacht
+= Schritt \# |= "" hn Schule ? Wolke System
$$ Einbau } Baum Systeme & ü \$ heiß |=
&= Buch Glas => >= {} wohnen .. ++ anbei
&& ~~ _ Mohn dogs ! eosin ß mugs erlaubt
Koeln guide - Energy \n erleben $ aktuell {{ schreiben
Diktat \[ Vogel * Iunius %s kt >> Kind ::
. , umbringt Sohn Fenster Hahn Amboss ö rm Amt
Ruine bugs Maschine iu rl / Analyse ** Käse erwartung
" <= !? ## erwartet Biology ?. equinoctium '' Amtsblatt
Anbau build /// Hand ) /* cy Koeffizient eo Cyclist
schön Haus Handtuch \^ ~ Wärme ` Bicycle erlöst Maus
Gymnasium Hüpfen \] Vögel Hände { ### Morgen ./ Küsse
Licht ui \} ä Geometrie | Schrift \{ grüßen gy
Ruinen Kombination € &= während == bags */ --- <
<- Formel Kombi suit @ }} Hütte
Iulius ... [[ ' Hund Beobachtung tags ?: Höhlen Wind
`` ^= \t Kontakt Tanne ^ || ´ ;; ->
+ suitable Wiese oe \( ..< Kaktus ``` : #
[] << erlitten Geometer \) % Diktatur juice ] ~~~
!! amtieren ( Straße dt \ != Cyber Norm \\
= erwachsene Symbol Landtag \% Koexistenz nb warm Mädchen Höfe
beobachten // Apfel Erlösung [^] flags Küche Bett -= erwache
''' ; %% \_ Kahn Amtsstube Wasser -- ]] >
Müde () größer eons \& __ verwandt """ [ Nacht
+= Schritt \# |= "" hn Schule ? Wolke System
$$ Einbau } Baum Systeme & ü \$ heiß |=
&= Buch Glas => >= {} wohnen .. ++ anbei
&& ~~ _ Mohn dogs ! eosin ß mugs erlaubt
Koeln guide - Energy \n erleben $ aktuell {{ schreiben
Diktat \[ Vogel * Iunius %s kt >> Kind ::
. , umbringt Sohn Fenster Hahn Amboss ö rm Amt
Ruine bugs Maschine iu rl / Analyse ** Käse erwartung
" <= !? ## erwartet Biology ?. equinoctium '' Amtsblatt
Anbau build /// Hand ) /* cy Koeffizient eo Cyclist
schön Haus Handtuch \^ ~ Wärme ` Bicycle erlöst Maus
Gymnasium Hüpfen \] Vögel Hände { ### Morgen ./ Küsse
Licht ui \} ä Geometrie | Schrift \{ grüßen gy
Ruinen Kombination € &= während == bags */ --- <
<- Formel Kombi suit @ }} Hütte
Iulius ... [[ ' Hund Beobachtung tags ?: Höhlen Wind
`` ^= \t Kontakt Tanne ^ || ´ ;; ->
+ suitable Wiese oe \( ..< Kaktus ``` : #
[] << erlitten Geometer \) % Diktatur juice ] ~~~
!! amtieren ( Straße dt \ != Cyber Norm \\
= erwachsene Symbol Landtag \% Koexistenz nb warm Mädchen Höfe
beobachten // Apfel Erlösung [^] flags Küche Bett -= erwache
''' ; %% \_ Kahn Amtsstube Wasser -- ]] >
Müde () größer eons \& __ verwandt """ [ Nacht
+= Schritt \# |= "" hn Schule ? Wolke System
$$ Einbau } Baum Systeme & ü \$ heiß |=
&= Buch Glas => >= {} wohnen .. ++ anbei
&& ~~ _ Mohn dogs ! eosin ß mugs erlaubt
Koeln guide - Energy \n erleben $ aktuell {{ schreiben
Diktat \[ Vogel * Iunius %s kt >> Kind ::
. , umbringt Sohn Fenster Hahn Amboss ö rm Amt
Ruine bugs Maschine iu rl / Analyse ** Käse erwartung
" <= !? ## erwartet Biology ?. equinoctium '' Amtsblatt
Anbau build /// Hand ) /* cy Koeffizient eo Cyclist
schön Haus Handtuch \^ ~ Wärme ` Bicycle erlöst Maus
Gymnasium Hüpfen \] Vögel Hände { ### Morgen ./ Küsse
Licht ui \} ä Geometrie | Schrift \{ grüßen gy
Ruinen Kombination € &= während == bags */ --- <
<- Formel Kombi suit @ }} Hütte
```

## Stufe R1 — Symbole kompakt (12 Runden · 1476 Tokens · 4091 Zeichen)

```
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
<- ``` } ? eo &= [ [[ ä =>
&& ..< ~~ /// ; hn - \) %% """
kt ?. */ nb / { ´ ### == %s
'' .. \_ += > : $$ + ++ &=
' ?: <= @ ~~~ {{ \[ iu -- -=
>= \\ "" |= < = * _ , \{
\# \] ü ui !! |= << ^ \& "
. & ^= ]] | $ }} ] cy `
./ || [^] () \} --- \t rl -> gy
// ~ ** \n ( !? __ ''' \$ ö
:: \% \ >> /* ß \( ) ! €
oe rm != dt {} # [] `` ;; ##
... % \^
```

## Stufe R2 — Operatoren (6 Runden · 888 Tokens · 4079 Zeichen)

```
bags @ ## Hütte \^ --- % Hund mugs \]
Wasser schreiben Vögel flags () größer Hand Käse */ Haus
\\ tags Kind ^= erwache Hüpfen \# -= <= ?.
-> Apfel Baum ''' >> !! ;; /// Systeme /*
Amt \} € :: %s << Vogel => Analyse ~~
Schritt .. \ Hände dogs [^] Wiese Wolke Symbol {}
"" ?: ** Glas == // während $$ ./ &
Licht Küsse \n Tanne != Schule | # Amtsblatt !?
erwartet ^ Fenster || """ |= \_ ]] '' Amtsstube
..< %% += \( Straße heiß erwartung erwachsene }} \{
Maus ``` grüßen &= &= $ Schrift ` bugs ++
<- Kombination umbringt Buch Morgen [] \t [[ {{ amtieren
Müde -- Maschine `` Bett >= ~~~ ~ System Nacht
... \$ Mädchen Amboss ### Wind Höhlen |= Küche Höfe
\% \[ && __ schön Kombi \& \)
bags @ ## Hütte \^ --- % Hund mugs \]
Wasser schreiben Vögel flags () größer Hand Käse */ Haus
\\ tags Kind ^= erwache Hüpfen \# -= <= ?.
-> Apfel Baum ''' >> !! ;; /// Systeme /*
Amt \} € :: %s << Vogel => Analyse ~~
Schritt .. \ Hände dogs [^] Wiese Wolke Symbol {}
"" ?: ** Glas == // während $$ ./ &
Licht Küsse \n Tanne != Schule | # Amtsblatt !?
erwartet ^ Fenster || """ |= \_ ]] '' Amtsstube
..< %% += \( Straße heiß erwartung erwachsene }} \{
Maus ``` grüßen &= &= $ Schrift ` bugs ++
<- Kombination umbringt Buch Morgen [] \t [[ {{ amtieren
Müde -- Maschine `` Bett >= ~~~ ~ System Nacht
... \$ Mädchen Amboss ### Wind Höhlen |= Küche Höfe
\% \[ && __ schön Kombi \& \)
bags @ ## Hütte \^ --- % Hund mugs \]
Wasser schreiben Vögel flags () größer Hand Käse */ Haus
\\ tags Kind ^= erwache Hüpfen \# -= <= ?.
-> Apfel Baum ''' >> !! ;; /// Systeme /*
Amt \} € :: %s << Vogel => Analyse ~~
Schritt .. \ Hände dogs [^] Wiese Wolke Symbol {}
"" ?: ** Glas == // während $$ ./ &
Licht Küsse \n Tanne != Schule | # Amtsblatt !?
erwartet ^ Fenster || """ |= \_ ]] '' Amtsstube
..< %% += \( Straße heiß erwartung erwachsene }} \{
Maus ``` grüßen &= &= $ Schrift ` bugs ++
<- Kombination umbringt Buch Morgen [] \t [[ {{ amtieren
Müde -- Maschine `` Bett >= ~~~ ~ System Nacht
... \$ Mädchen Amboss ### Wind Höhlen |= Küche Höfe
\% \[ && __ schön Kombi \& \)
bags @ ## Hütte \^ --- % Hund mugs \]
Wasser schreiben Vögel flags () größer Hand Käse */ Haus
\\ tags Kind ^= erwache Hüpfen \# -= <= ?.
-> Apfel Baum ''' >> !! ;; /// Systeme /*
Amt \} € :: %s << Vogel => Analyse ~~
Schritt .. \ Hände dogs [^] Wiese Wolke Symbol {}
"" ?: ** Glas == // während $$ ./ &
Licht Küsse \n Tanne != Schule | # Amtsblatt !?
erwartet ^ Fenster || """ |= \_ ]] '' Amtsstube
..< %% += \( Straße heiß erwartung erwachsene }} \{
Maus ``` grüßen &= &= $ Schrift ` bugs ++
<- Kombination umbringt Buch Morgen [] \t [[ {{ amtieren
Müde -- Maschine `` Bett >= ~~~ ~ System Nacht
... \$ Mädchen Amboss ### Wind Höhlen |= Küche Höfe
\% \[ && __ schön Kombi \& \)
bags @ ## Hütte \^ --- % Hund mugs \]
Wasser schreiben Vögel flags () größer Hand Käse */ Haus
\\ tags Kind ^= erwache Hüpfen \# -= <= ?.
-> Apfel Baum ''' >> !! ;; /// Systeme /*
Amt \} € :: %s << Vogel => Analyse ~~
Schritt .. \ Hände dogs [^] Wiese Wolke Symbol {}
"" ?: ** Glas == // während $$ ./ &
Licht Küsse \n Tanne != Schule | # Amtsblatt !?
erwartet ^ Fenster || """ |= \_ ]] '' Amtsstube
..< %% += \( Straße heiß erwartung erwachsene }} \{
Maus ``` grüßen &= &= $ Schrift ` bugs ++
<- Kombination umbringt Buch Morgen [] \t [[ {{ amtieren
Müde -- Maschine `` Bett >= ~~~ ~ System Nacht
... \$ Mädchen Amboss ### Wind Höhlen |= Küche Höfe
\% \[ && __ schön Kombi \& \)
bags @ ## Hütte \^ --- % Hund mugs \]
Wasser schreiben Vögel flags () größer Hand Käse */ Haus
\\ tags Kind ^= erwache Hüpfen \# -= <= ?.
-> Apfel Baum ''' >> !! ;; /// Systeme /*
Amt \} € :: %s << Vogel => Analyse ~~
Schritt .. \ Hände dogs [^] Wiese Wolke Symbol {}
"" ?: ** Glas == // während $$ ./ &
Licht Küsse \n Tanne != Schule | # Amtsblatt !?
erwartet ^ Fenster || """ |= \_ ]] '' Amtsstube
..< %% += \( Straße heiß erwartung erwachsene }} \{
Maus ``` grüßen &= &= $ Schrift ` bugs ++
<- Kombination umbringt Buch Morgen [] \t [[ {{ amtieren
Müde -- Maschine `` Bett >= ~~~ ~ System Nacht
... \$ Mädchen Amboss ### Wind Höhlen |= Küche Höfe
\% \[ && __ schön Kombi \& \)
```

## Stufe W — Wörter (5 Runden · 570 Tokens · 4019 Zeichen)

```
Maschine Diktatur Koeffizient Bett erwartet Kahn erlitten Wind Mädchen equinoctium
Iulius eosin bags erwartung Hund Höfe Hand Kontakt Norm Symbol
Licht Erlösung Formel umbringt Handtuch Kombination Iunius bugs Hände aktuell
amtieren Ruine tags Wärme Vögel Wiese Biology Sohn System Apfel
Straße Nacht heiß Küche Landtag flags Kombi Amtsblatt suit Koexistenz
Hahn grüßen Energy erwachsene Käse Geometer Müde verwandt Anbau Amboss
Küsse Schule Höhlen Hüpfen Buch juice wohnen Schrift Baum schön
schreiben erlöst Kaktus erwache Morgen Beobachtung anbei beobachten Fenster erleben
Glas Einbau Hütte Analyse build Geometrie Gymnasium Cyclist warm Maus
Diktat eons mugs dogs Mohn Haus Systeme Schritt während Wolke
Cyber Bicycle Tanne Ruinen erlaubt Amt Vogel größer Amtsstube Wasser
Koeln guide Kind suitable
Maschine Diktatur Koeffizient Bett erwartet Kahn erlitten Wind Mädchen equinoctium
Iulius eosin bags erwartung Hund Höfe Hand Kontakt Norm Symbol
Licht Erlösung Formel umbringt Handtuch Kombination Iunius bugs Hände aktuell
amtieren Ruine tags Wärme Vögel Wiese Biology Sohn System Apfel
Straße Nacht heiß Küche Landtag flags Kombi Amtsblatt suit Koexistenz
Hahn grüßen Energy erwachsene Käse Geometer Müde verwandt Anbau Amboss
Küsse Schule Höhlen Hüpfen Buch juice wohnen Schrift Baum schön
schreiben erlöst Kaktus erwache Morgen Beobachtung anbei beobachten Fenster erleben
Glas Einbau Hütte Analyse build Geometrie Gymnasium Cyclist warm Maus
Diktat eons mugs dogs Mohn Haus Systeme Schritt während Wolke
Cyber Bicycle Tanne Ruinen erlaubt Amt Vogel größer Amtsstube Wasser
Koeln guide Kind suitable
Maschine Diktatur Koeffizient Bett erwartet Kahn erlitten Wind Mädchen equinoctium
Iulius eosin bags erwartung Hund Höfe Hand Kontakt Norm Symbol
Licht Erlösung Formel umbringt Handtuch Kombination Iunius bugs Hände aktuell
amtieren Ruine tags Wärme Vögel Wiese Biology Sohn System Apfel
Straße Nacht heiß Küche Landtag flags Kombi Amtsblatt suit Koexistenz
Hahn grüßen Energy erwachsene Käse Geometer Müde verwandt Anbau Amboss
Küsse Schule Höhlen Hüpfen Buch juice wohnen Schrift Baum schön
schreiben erlöst Kaktus erwache Morgen Beobachtung anbei beobachten Fenster erleben
Glas Einbau Hütte Analyse build Geometrie Gymnasium Cyclist warm Maus
Diktat eons mugs dogs Mohn Haus Systeme Schritt während Wolke
Cyber Bicycle Tanne Ruinen erlaubt Amt Vogel größer Amtsstube Wasser
Koeln guide Kind suitable
Maschine Diktatur Koeffizient Bett erwartet Kahn erlitten Wind Mädchen equinoctium
Iulius eosin bags erwartung Hund Höfe Hand Kontakt Norm Symbol
Licht Erlösung Formel umbringt Handtuch Kombination Iunius bugs Hände aktuell
amtieren Ruine tags Wärme Vögel Wiese Biology Sohn System Apfel
Straße Nacht heiß Küche Landtag flags Kombi Amtsblatt suit Koexistenz
Hahn grüßen Energy erwachsene Käse Geometer Müde verwandt Anbau Amboss
Küsse Schule Höhlen Hüpfen Buch juice wohnen Schrift Baum schön
schreiben erlöst Kaktus erwache Morgen Beobachtung anbei beobachten Fenster erleben
Glas Einbau Hütte Analyse build Geometrie Gymnasium Cyclist warm Maus
Diktat eons mugs dogs Mohn Haus Systeme Schritt während Wolke
Cyber Bicycle Tanne Ruinen erlaubt Amt Vogel größer Amtsstube Wasser
Koeln guide Kind suitable
Maschine Diktatur Koeffizient Bett erwartet Kahn erlitten Wind Mädchen equinoctium
Iulius eosin bags erwartung Hund Höfe Hand Kontakt Norm Symbol
Licht Erlösung Formel umbringt Handtuch Kombination Iunius bugs Hände aktuell
amtieren Ruine tags Wärme Vögel Wiese Biology Sohn System Apfel
Straße Nacht heiß Küche Landtag flags Kombi Amtsblatt suit Koexistenz
Hahn grüßen Energy erwachsene Käse Geometer Müde verwandt Anbau Amboss
Küsse Schule Höhlen Hüpfen Buch juice wohnen Schrift Baum schön
schreiben erlöst Kaktus erwache Morgen Beobachtung anbei beobachten Fenster erleben
Glas Einbau Hütte Analyse build Geometrie Gymnasium Cyclist warm Maus
Diktat eons mugs dogs Mohn Haus Systeme Schritt während Wolke
Cyber Bicycle Tanne Ruinen erlaubt Amt Vogel größer Amtsstube Wasser
Koeln guide Kind suitable
```
