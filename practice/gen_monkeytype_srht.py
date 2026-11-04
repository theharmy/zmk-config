#!/usr/bin/env python3
"""Generate practice text for the TwoNr9 chord keymap (srht) for Monkeytype.

Variant twin of `gen_monkeytype.py` (which covers the default bugwind layout):
same curriculum structure, same chord *outputs*, but every chord is named with
the **srht** letters that sit at its positions -- the diagonal/home-row/German
combos are position-based and shared (`symbol_work.dtsi`, `twonr9_combos.dtsi`),
only the srht grids differ:

    srht a1   top: L N D Y O U   home: S R H T | C E I A
    srht a2   top: X B V W Q ,   home: F M P K | G J . Z

Differences from the bugwind curriculum:

  * bigrams:   a1 RL HN DT CY EO UI · a2 RM NB KT GY OE IU
               (kt words drill an a2 layer switch; the bugwind-only pairs
               mb ys rw mt sch gs have no chord here and demote to plain)
  * German letters: ß is C+Space (10+16) on srht vs S+Space on bugwind, and the
    acute ´ sits alone at S+R (6+7) vs N+R on bugwind -- the umlauts (vowel +
    Space) are identical on both variants
  * home-row combos: _ = R+T, - = R+H, ; = C+I (letters moved vs bugwind)
  * srht's nine adaptive keys are documented in the legend: within 300 ms of
    its trigger an adaptive key emits the swap partner; the chord path used
    by this drill is not affected

A short, progressive curriculum (quality over quantity): 7 self-contained
blocks of ~3-4k chars each, increasing in difficulty:

    1  Plain                18 plain outputs, no modifiers
    2  Plain + Ctrl + erste Wörter  operators + general German words
                                   (no bigram pairs — alpha grid joins in)
    3  + a1 Bigrams + Layer-1-Wörter  a1 layer complete (positions + bigrams)
    4  All Symbols          Shift states unlock (+ ´ from S + R)
    5  + a2 Bigrams + alle Wörter     the full keymap
    6  Wörter               the full word pool in context
    7  Vollpass (Exam)      every token — 89 chord outputs + all words — once

Words accumulate: from stage 2 on, each block carries the earlier word tiers,
so the later blocks are realistic mixes. The word tiers are derived from the
pair tags: tier 2 = no bigram pairs (plain words + umlaut words), tier 3 =
a1-bigram words, tier 5 = a2-bigram words.

Each block is drawn round-robin from its own pool, so every fixed-size random
slice is uniform (each pool entry appears exactly once per full round). Words
with umlauts / Eszett also drill the letter + Space chords.

Run:  python3 practice/gen_monkeytype_srht.py
      (writes practice/twonr9_srht_chords_monkeytype.md)
"""
import random
import sys
from collections import Counter
from pathlib import Path

# Practice curriculum table for srht. Keep it aligned with
# `config/symbol_work.dtsi` (positions, outputs) and the srht grids in
# `config/twonr9_srht.keymap` (letters at those positions).
CHORDS = [
    ("L + S", ["(", ")", "==", "!="]),
    ("Y + E", ["}", "{", "<=", ">="]),
    ("N + R", ["[", "]", "+=", "-="]),
    ("U + A", [")", "(", "&=", "|="]),
    ("D + H", ["{", "}", "<<=", ">>="]),
    ("O + I", ["]", "[", "^=", "*="]),
    ("N + S", ["&", "*", "&&", "||"]),
    ("O + A", ["$", "\u20ac", "??", "?."]),
    ("D + R", ["~", "^", "->", "=>"]),
    ("Y + I", ["=", "+", "<<", ">>"]),
    ("D + S", ["<", ">", "<=", "<="]),
    ("Y + A", [">", "<", ">=", ">="]),
    ("L + H", ["!", "?", "//", "..."]),
    ("N + T", ["-", "_", "++", "--"]),
    ("U + E", [";", ":", "/*", "*/"]),
    ("O + C", ["'", '\"', "=", "|"]),
    ("L + T", ["#", "%", "::", ":="]),
    ("U + C", ["/", "\\", "+", "@"]),
]
# German letters (letter + Space chord, shared with bugwind via
# symbol_work.dtsi) and the acute at S + R (6+7).
GERMAN = [
    ("C + Space", "\u00df"),   # Eszett (combo_de_sz, positions 10+16)
    ("A + Space", "\u00e4"),   # a-umlaut
    ("O + Space", "\u00f6"),   # o-umlaut
    ("U + Space", "\u00fc"),   # u-umlaut
    ("S + R", "\u00b4"),       # acute (shift: backtick), positions 6+7
]
BIGRAMS = ["RL", "HN", "DT", "CY", "EO", "UI", "RM", "NB", "KT", "GY", "OE", "IU"]
A1 = BIGRAMS[:6]
A2 = BIGRAMS[6:]

TOKENS = []
for _, outs in CHORDS:
    TOKENS.extend(outs)
for _, tok in GERMAN:
    TOKENS.append(tok)
TOKENS.extend(BIGRAMS)
N_TOKENS = len(TOKENS)
assert N_TOKENS == 89, f"expected 89 chord states, got {N_TOKENS}"
# Some outputs intentionally occur on multiple chords (mirrored brackets,
# comparison operators and the shared = / + chord states). Assert the expected
# duplicate surface to catch accidental changes. The outputs are identical to
# bugwind's, so this surface is the same for both variants.
_dupes = {t: c for t, c in Counter(TOKENS).items() if c > 1}
_allowed_duplicates = set("()[]{}") | {"<", ">", "<=", ">=", "=", "+"}
assert set(_dupes) <= _allowed_duplicates, f"unexpected duplicate tokens: {_dupes}"
assert all(c == 2 for t, c in _dupes.items() if t not in {"<=", ">="}), \
    f"unexpected duplicate counts: {_dupes}"
assert _dupes.get("<=") == 3 and _dupes.get(">=") == 3, \
    f"comparison operators should each occur on three states: {_dupes}"
assert set(_dupes) == _allowed_duplicates, f"duplicate surface changed: {_dupes}"

# --- Words containing the bigram letter pairs (mostly German, some English) ---
# Each word is tagged with the bigram(s) / German letters it drills. Tags refer
# to the OUTPUT pair (which is identical across variants), not the chord keys.
# Words for pairs that only exist on bugwind (mb ys rw mt sch gs) are absent
# here and live in PLAIN_WORDS instead -- on srht they need no chord.
WORDS = [
    # rl (L+R)
    ("erleben", ["rl"]),
    ("erlöst", ["rl"]),
    ("erlitten", ["rl"]),
    ("erlaubt", ["rl"]),
    ("Erlösung", ["rl"]),
    # hn (N+H)
    ("Sohn", ["hn"]),
    ("Kahn", ["hn"]),
    ("Hahn", ["hn"]),
    ("Mohn", ["hn"]),
    ("wohnen", ["hn"]),
    # dt (D+T)
    ("Landtag", ["dt"]),
    ("verwandt", ["dt"]),
    ("Handtuch", ["dt"]),
    # cy (Y+C -- rare in German, English/loan words)
    ("Bicycle", ["cy"]),
    ("Cyclist", ["cy"]),
    ("Cyber", ["cy"]),
    # eo (O+E)
    ("Geometrie", ["eo"]),
    ("beobachten", ["eo"]),
    ("Beobachtung", ["eo"]),
    ("Geometer", ["eo"]),
    ("eons", ["eo"]),
    ("eosin", ["eo"]),
    # ui (U+I)
    ("Ruine", ["ui"]),
    ("Ruinen", ["ui"]),
    ("build", ["ui"]),
    ("suit", ["ui"]),
    ("suitable", ["ui"]),
    ("juice", ["ui"]),
    ("guide", ["ui"]),
    # rm (X+M, a2)
    ("Norm", ["rm"]),
    ("Formel", ["rm"]),
    ("warm", ["rm"]),
    ("Wärme", ["rm"]),
    # nb (B+P, a2 -- rare; German compounds)
    ("Anbau", ["nb"]),
    ("Einbau", ["nb"]),
    ("anbei", ["nb"]),
    # kt (V+K, a2 -- forces an a2 switch mid-word)
    ("aktuell", ["kt"]),
    ("Diktat", ["kt"]),
    ("Diktatur", ["kt"]),
    ("Kontakt", ["kt"]),
    ("Kaktus", ["kt"]),
    # gy (W+G, a2 -- rare; English/loan words)
    ("Gymnasium", ["gy"]),
    ("Biology", ["gy"]),
    ("Energy", ["gy"]),
    # oe (Q+J, a2)
    ("Koeffizient", ["oe"]),
    ("Koexistenz", ["oe"]),
    ("Koeln", ["oe"]),
    # iu (comma+dot, a2 -- rare pair; Latin/loan forms)
    ("Iulius", ["iu"]),
    ("Iunius", ["iu"]),
    ("equinoctium", ["iu"]),
    # German letter chords: ß (C+Space), ä (A+Space), ö (O+Space), ü (U+Space)
    ("Straße", ["\u00df"]),
    ("größer", ["\u00df", "\u00f6"]),
    ("heiß", ["\u00df"]),
    ("Küsse", ["\u00fc"]),
    ("grüßen", ["\u00fc", "\u00df"]),
    ("während", ["\u00e4"]),
    ("Mädchen", ["\u00e4"]),
    ("Käse", ["\u00e4"]),
    ("Hände", ["\u00e4"]),
    ("schön", ["\u00f6"]),
    ("Höfe", ["\u00f6"]),
    ("Höhlen", ["\u00f6"]),
    ("Vögel", ["\u00f6"]),
    ("Müde", ["\u00fc"]),
    ("Hütte", ["\u00fc"]),
    ("Küche", ["\u00fc"]),
    ("Hüpfen", ["\u00fc"]),
]

# General German words that contain NONE of the 12 srht bigram pair sequences —
# they only need plain letters (plus the umlaut chords in the tagged pool
# above), so they can join the curriculum early (stage 2) while the a1/a2
# bigram layers are still being learned. The first 20 are the shared core;
# the rest were bigram words on bugwind (mb ys rw mt sch gs pairs) whose
# chord does not exist on srht, so they demote to plain typing here.
PLAIN_WORDS = [
    "Haus", "Maus", "Hund", "Kind", "Wind",
    "Hand", "Nacht", "Licht", "Wasser", "Baum",
    "Apfel", "Vogel", "Wolke", "Fenster", "Buch",
    "Bett", "Morgen", "Glas", "Wiese", "Tanne",
    # demoted from the bugwind tagged pool (no srht chord for their pair):
    "Symbol", "Kombi", "Amboss", "Kombination", "umbringt",
    "System", "Systeme", "Analyse",
    "erwartet", "erwartung", "erwachsene", "erwache",
    "Amt", "Amtsstube", "Amtsblatt", "amtieren",
    "Schule", "Maschine", "schreiben", "Schrift", "Schritt",
    "bags", "dogs", "tags", "flags", "mugs", "bugs",
]

WORD_TAGS = {
    "rl": "L+R", "hn": "N+H", "dt": "D+T", "cy": "Y+C", "eo": "O+E", "ui": "U+I",
    "rm": "X+M", "nb": "B+P", "kt": "V+K", "gy": "W+G", "oe": "Q+J", "iu": ",+.",
    "\u00df": "C+Space", "\u00e4": "A+Space", "\u00f6": "O+Space", "\u00fc": "U+Space",
}

# Verify: every tag must actually occur in the word.
for _word, _tags in WORDS:
    for _t in _tags:
        assert _t in _word.lower(), f"word {_word!r} does not contain {_t!r}"
_word_names = [w for w, _ in WORDS]
assert len(set(_word_names)) == len(_word_names), "duplicate words!"
assert not set(PLAIN_WORDS) & set(_word_names), "plain words duplicate tagged words"
# Every bigram and every German letter must be drilled by at least one word.
_covered = {t for _, tags in WORDS for t in tags}
_needed = {b.lower() for b in BIGRAMS} | set("\u00df\u00e4\u00f6\u00fc")
_missing = _needed - _covered
assert not _missing, f"not drilled by any word: {_missing}"

# --- Word tiers for the curriculum, derived from the pair tags ---
_pairs = [b.lower() for b in BIGRAMS]
_umlauts = set("\u00df\u00e4\u00f6\u00fc")
# PLAIN_WORDS must not contain any bigram pair sequence and must not clash
# with the tagged pool.
for _w in PLAIN_WORDS:
    _wl = _w.lower()
    for _p in _pairs:
        assert _p not in _wl, f"plain word {_w!r} contains bigram pair {_p!r}"
# Tiers: a2 = word drills at least one a2 pair; a1 = at least one a1 pair
# (and no a2); umlaut = no pair at all. The three tiers partition WORDS.
_a1s, _a2s = {b.lower() for b in A1}, {b.lower() for b in A2}
_tier_a2 = [w for w, tags in WORDS if _a2s & set(tags)]
_tier_a1 = [w for w, tags in WORDS
            if _a1s & set(tags) and not (_a2s & set(tags))]
_tier_umlaut = [w for w, tags in WORDS
                if set(tags) and set(tags) <= _umlauts]
_tiered = _tier_a2 + _tier_a1 + _tier_umlaut
assert len(set(_tiered)) == len(_tiered) == len(_word_names), "word tiers must partition WORDS"
# Cumulative word pools for the stages:
WORDS_EARLY = PLAIN_WORDS + _tier_umlaut            # stage 2
WORDS_A1 = WORDS_EARLY + _tier_a1                   # stage 3
WORDS_ALL = WORDS_A1 + _tier_a2                     # stage 5
N_WORDS = len(WORDS_ALL)

# --- Curriculum: 7 progressive stages (quality over quantity) ---
# Each stage is self-contained (only its own pool appears) and round-robin
# shuffled, so every fixed-length slice is uniform: each pool entry appears
# exactly once per full round. Stages grow by adding one new ingredient.
PLAIN = [outs[0] for _, outs in CHORDS]
SHIFT = [outs[1] for _, outs in CHORDS]
CTRL = [outs[2] for _, outs in CHORDS]
CTRL_SHIFT = [outs[3] for _, outs in CHORDS]

STAGES = [
    ("1", "Plain",
     "reines Chord-Gef\u00fchl: 18 Plain-Outputs, keine Modifier",
     PLAIN),
    ("2", "Plain + Ctrl + erste W\u00f6rter",
     "Operatoren dazu + allgemeine deutsche W\u00f6rter ohne Bigrams "
     "(Alpha-Grid \u00fcbt mit) \u2014 immer noch kein Shift",
     PLAIN + CTRL + WORDS_EARLY),
    ("3", "+ a1-Bigrams + Layer-1-W\u00f6rter",
     "a1 komplett: Bigrams + die W\u00f6rter, die nur a1-Chords brauchen",
     PLAIN + CTRL + A1 + WORDS_A1),
    ("4", "Alle Symbole",
     "Shift-Zust\u00e4nde kommen dazu (+ \u00b4 aus S + R, \u00df aus C + Space)",
     PLAIN + SHIFT + CTRL + CTRL_SHIFT + [GERMAN[4][1]] + WORDS_A1),
    ("5", "+ a2-Bigrams + alle W\u00f6rter",
     "die komplette Keymap: a2-Bigrams (Layerwechsel mitten im Wort) + alle W\u00f6rter",
     TOKENS + WORDS_ALL),
    ("6", "W\u00f6rter",
     f"alles im echten Tipp-Kontext ({N_WORDS} W\u00f6rter)",
     WORDS_ALL),
]
# Final exam: every token \u2014 89 chord outputs + all words \u2014 exactly once.
EXAM = ("7", "Vollpass (Abschluss)", "alles in einem Durchgang", TOKENS + WORDS_ALL)

PER_LINE = 10
MIN_BLOCK_CHARS = 2800
MAX_BLOCK_CHARS = 4200  # stay well below Monkeytype's 10k custom-test limit
OUT = Path(__file__).resolve().parent / "twonr9_srht_chords_monkeytype.md"


def perm_for(tokens, seed, salt=0):
    rng = random.Random(1000 + (seed + salt) * 7919)
    perm = tokens[:]
    rng.shuffle(perm)
    return perm


def block_text(perm, rounds: int) -> str:
    lines = []
    for _ in range(rounds):
        for i in range(0, len(perm), PER_LINE):
            lines.append(" ".join(perm[i:i + PER_LINE]))
    return "\n".join(lines)


def fit_rounds(perm) -> int:
    """Largest round count that still fits the character budget."""
    rounds = 1
    while len(block_text(perm, rounds + 1)) <= MAX_BLOCK_CHARS:
        rounds += 1
    return rounds


def make_block(num, perm, rounds):
    """Assemble the block text and verify pool purity + uniform counts."""
    text = block_text(perm, rounds)
    # A block may contain nothing but its own pool, and every pool entry
    # must appear exactly `rounds` times (the round-robin guarantee; bracket
    # characters occur twice in the pool and thus 2*rounds times in the text).
    pool_count = Counter(perm)
    text_count = Counter(text.split())
    assert set(text_count) == set(pool_count), \
        f"stage {num}: unexpected tokens {set(text_count) - set(pool_count)}"
    for tok, n in pool_count.items():
        assert text_count[tok] == rounds * n, \
            f"stage {num}: token {tok!r} count {text_count[tok]} != {rounds * n}"
    return text


def legend():
    out = []
    out.append("## Legende\n")
    out.append("### Stufen\n")
    out.append("| Stufe | Block | Was er \u00fcbt | Pool |")
    out.append("| --- | --- | --- | --- |")
    for num, name, desc, pool in STAGES + [EXAM]:
        out.append(f"| {num} | **{name}** | {desc} | {len(pool)} Tokens |")
    out.append("")
    out.append(
        "### Diagonale Symbol-Chords (16 Chords \u00d7 4 Modifier-Zust\u00e4nde = 64 Outputs)\n")
    out.append("| Chord | Plain | Shift | Ctrl | Ctrl + Shift |")
    out.append("| --- | --- | --- | --- | --- |")
    for name, (p, s, c, cs) in CHORDS:
        out.append(f"| {name} | `{p}` | `{s}` | `{c}` | `{cs}` |")
    out.append("")
    out.append("### Deutsche Buchstaben (srht)\n")
    out.append("| Chord | Output (Shift = Grossbuchstabe) |")
    out.append("| --- | --- |")
    out.append("| C + Space | \u00df / \u1e9e |")
    out.append("| A + Space | \u00e4 / \u00c4 |")
    out.append("| O + Space | \u00f6 / \u00d6 |")
    out.append("| U + Space | \u00fc / \u00dc |")
    out.append("| S + R | \u00b4 (Shift: `) |")
    out.append("")
    out.append(
        "> Die deutschen Buchstaben liegen auf srht an denselben Chord-Positionen "
        "wie auf bugwind \u2014 nur die gedr\u00fcckten Buchstaben wechseln mit dem Grid: "
        "`\u00df` ist **C + Space** (10+16; auf bugwind S + Space) und der Akzent `´` "
        "steht allein auf **S + R** (6+7; auf bugwind N + R). Die Umlaute (Vokal + Space) "
        "sind identisch. Der fr\u00fchere 6+7-Konflikt zwischen \u00df und ´ ist damit "
        "aufgel\u00f6st.\n")
    out.append("### Bigrams (12)\n")
    out.append("| Layer | Chords |")
    out.append("| --- | --- |")
    out.append("| a1 | RL \u00b7 HN \u00b7 DT \u00b7 CY \u00b7 EO \u00b7 UI |")
    out.append("| a2 | RM \u00b7 NB \u00b7 KT \u00b7 GY \u00b7 OE \u00b7 IU |")
    out.append("")
    # Word tiers: which words join at which stage, then the pair -> words drill.
    out.append("### W\u00f6rter (ab Stufe 2, kumulativ)\n")
    out.append(f"**Stufe 2** \u2014 ohne Bigram-Paare: {', '.join(PLAIN_WORDS)} "
               f"+ \u00df/\u00e4/\u00f6/\u00fc-W\u00f6rter: {', '.join(_tier_umlaut)}")
    out.append(f"\n**Stufe 3** \u2014 a1-Bigram-W\u00f6rter: {', '.join(_tier_a1)}")
    out.append(f"\n**Stufe 5** \u2014 a2-Bigram-W\u00f6rter (Layerwechsel mitten im Wort): "
               f"{', '.join(_tier_a2)}\n")
    out.append("### W\u00f6rter-Drill: Buchstabenpaar \u2192 Chord \u2192 W\u00f6rter\n")
    out.append("| Paar | Chord | W\u00f6rter |")
    out.append("| --- | --- | --- |")
    for pair in [b.lower() for b in BIGRAMS] + ["\u00df", "\u00e4", "\u00f6", "\u00fc"]:
        ws = [w for w, tags in WORDS if pair in tags]
        out.append(f"| `{pair}` | {WORD_TAGS[pair]} | {', '.join(ws)} |")
    out.append("")
    out.append("> W\u00f6rter mit `rm`/`nb`/`kt`/`gy`/`oe`/`iu` erzwingen einen a2-Layerwechsel "
               "mitten im Wort (das ist der Punkt des Drills). Bei den seltenen Paaren `cy`, "
               "`nb` und `gy` fehlen h\u00e4ufige deutsche W\u00f6rter, daher englische bzw. "
               "Lehnformen.\n")
    out.append("### Home-Row-Symbol-Combos (alle Alpha-Layer)\n")
    out.append("| Chord | Output |")
    out.append("| --- | --- |")
    out.append("| R + T | _ (auch N + T \u00b7 Shift) |")
    out.append("| R + H | - (auch N + T \u00b7 Plain) |")
    out.append("| E + I | : (auch U + E \u00b7 Shift) |")
    out.append("| C + I | ; (auch U + E \u00b7 Plain) |")
    out.append("")
    out.append("> `_ - : ;` kommen im Pool nur einmal pro Runde vor (Chord-Pfad); "
               "beide Wege liefern das gleiche Zeichen.\n")
    out.append("### Adaptive Keys (9, nur srht)\n")
    out.append("| Nach | Swap | Keys |")
    out.append("| --- | --- | --- |")
    out.append("| R | H \u2194 L \u00b7 M \u2194 V | H L M V |")
    out.append("| U | O \u2194 I | O I |")
    out.append("| Q | I \u2194 U | I U |")
    out.append("| N | B \u2194 X | B X |")
    out.append("")
    out.append("> 9 adaptive Keys (`l h o i u` auf a1, `x b v m` auf a2): innerhalb von "
               "300 ms nach dem Trigger gibt der Key den Partner aus \u2014 z. B. kommt "
               "schnelles `rh` als `rl` heraus, `ui` als `uo`. Die Bigram-Chords "
               "(beide Tasten gleichzeitig) und alles au\u00dferhalb des Fensters sind "
               "nicht betroffen \u2014 der Drill nutzt deshalb bewusst den Chord-Pfad.\n")
    return "\n".join(out)


def main():
    parts = []
    parts.append("# TwoNr9 srht \u2014 Chord-Praxis (Monkeytype)\n")
    parts.append(
        "Diese Datei enth\u00e4lt ein **Stufen-\u00dcbungssystem** f\u00fcr die srht-Keymap "
        "\u2014 Qualit\u00e4t vor Quantit\u00e4t: "
        f"{len(STAGES) + 1} aufeinander aufbauende Bl\u00f6cke, die in der Schwierigkeit steigen "
        "(Plain \u2192 +Ctrl/+erste W\u00f6rter \u2192 +a1-Bigrams/+Layer-1-W\u00f6rter \u2192 +Shift "
        "\u2192 +a2-Bigrams/+alle W\u00f6rter \u2192 W\u00f6rter \u2192 Vollpass). Die W\u00f6rter drillen ab "
        "Stufe 2 auch das Alpha-Grid: zuerst W\u00f6rter ohne Bigram-Paare, dann die, die a1- bzw. "
        "a2-Chords brauchen \u2014 so wachsen die W\u00f6rter mit den Layer-Kenntnissen mit. "
        "Jeder Block ist selbstst\u00e4ndig (nur sein eigener Pool) und wird Round-Robin gezogen: "
        "pro voller Runde kommt jeder Token genau einmal vor, egal an welcher Stelle Monkeytype "
        "zuf\u00e4llig ansetzt \u2014 jeder Ausschnitt ist gleichm\u00e4\u00dfig.\n")
    parts.append(
        "Die Chord-Namen folgen dem **srht**-Grid (obere Reihe `L N D Y O U`, Home `S R H T | "
        "C E I A`); die Outputs sind identisch mit bugwind, nur die gedr\u00fcckten Buchstaben "
        "wechseln. Zehn der achtzehn Diagonal-Chords hei\u00dfen daher anders als im "
        "bugwind-Praxisblatt.\n")
    parts.append("## Nutzung in Monkeytype\n")
    parts.append("1. Den Block der aktuellen Stufe kopieren (Code-Block, < 10.000 Zeichen).")
    parts.append("2. Monkeytype \u2192 Test Type **Custom** \u2192 Text einf\u00fcgen.")
    parts.append("3. Test-L\u00e4nge z. B. auf 25\u201375 W\u00f6rter stellen; Monkeytype w\u00e4hlt aus dem "
                 "Block einen zuf\u00e4lligen Ausschnitt.")
    parts.append("4. Erst zur n\u00e4chsten Stufe wechseln, wenn die aktuelle sauber l\u00e4uft. "
                 "Stufe 7 (Vollpass) ist die Abschlusspr\u00fcfung: jeder Token genau einmal.\n")
    parts.append("Beim \u00dcben auf der TwoNr9 zeigt die Legende unten, welcher Token welchen "
                 "Chord + Modifier-Zustand triggert. Achtung: die neun adaptiven Keys "
                 "tauschen bei schnellem Tippen innerhalb von 300 ms Buchstaben \u2014 die "
                 "Legende am Ende erkl\u00e4rt, wann.\n")
    parts.append(legend())

    sizes = []
    for num, name, _desc, pool in STAGES:
        perm = perm_for(pool, int(num))
        rounds = fit_rounds(perm)
        text = make_block(num, perm, rounds)
        assert MIN_BLOCK_CHARS <= len(text) <= MAX_BLOCK_CHARS, \
            f"stage {num}: {len(text)} chars outside the " \
            f"{MIN_BLOCK_CHARS}\u2013{MAX_BLOCK_CHARS} band"
        parts.append(f"## Stufe {num} \u2014 {name} "
                     f"({rounds} Runden \u00b7 {rounds * len(perm)} Tokens \u00b7 "
                     f"{len(text)} Zeichen)\n")
        parts.append("```")
        parts.append(text)
        parts.append("```\n")
        sizes.append(len(text))

    num, name, _desc, pool = EXAM
    text = make_block(num, perm_for(pool, int(num)), 1)
    parts.append(f"## Stufe {num} \u2014 {name} "
                 f"(1 Runde \u00b7 {len(pool)} Tokens \u00b7 {len(text)} Zeichen)\n")
    parts.append("```")
    parts.append(text)
    parts.append("```\n")
    sizes.append(len(text))

    doc = "\n".join(parts)
    OUT.write_text(doc)
    print(f"stages: {len(sizes)}, block chars: {sizes}")
    print(f"total doc chars: {len(doc)}")


if __name__ == "__main__":
    sys.exit(main())
