#!/usr/bin/env python3
"""Generate practice text for the TwoNr9 chord keymap (bugwind) for Monkeytype.

A short, progressive curriculum (quality over quantity): 7 self-contained
blocks of ~3–4k chars each, increasing in difficulty:

    1  Plain                16 plain outputs, no modifiers
    2  Plain + Ctrl + erste Wörter  operators + general German words
                                   (no bigram pairs — alpha grid joins in)
    3  + a1 Bigrams + Layer-1-Wörter  a1 layer complete (positions + bigrams)
    4  All Symbols          Shift states unlock (+ ´ from N + R)
    5  + a2 Bigrams + alle Wörter     the full keymap
    6  Wörter               the full word pool in context
    7  Vollpass (Exam)      every token — 81 chord outputs + all words — once

Words accumulate: from stage 2 on, each block carries the earlier word tiers,
so the later blocks are realistic mixes. The word tiers are derived from the
pair tags: tier 2 = no bigram pairs (plain words + umlaut words), tier 3 =
a1-bigram words, tier 5 = a2-bigram words.

Each block is drawn round-robin from its own pool, so every fixed-size random
slice is uniform (each pool entry appears exactly once per full round). Words
with umlauts / Eszett also drill the letter + Space chords.

Run:  python3 practice/gen_monkeytype.py   (writes practice/twonr9_chords_monkeytype.md)
"""
import random
import sys
from collections import Counter
from pathlib import Path

# Single update point: mirrors the DIAG_SYMBOL table in config/symbol_work.dtsi
# and the DIAGONAL_CHORDS table in draw/draw_twonr9.py.
CHORDS = [
    ("L + N", ["(", ")", "==", "!="]),
    ("Y + E", [")", "(", "<=", ">="]),
    ("M + R", ["[", "]", "+=", "-="]),
    ("U + A", ["]", "[", "&=", "|="]),
    ("D + T", ["{", "}", "<<=", ">>="]),
    ("O + I", ["}", "{", "^=", "*="]),
    ("M + N", ["&", "*", "&&", "||"]),
    ("O + A", ["$", "\u20ac", "??", "?."]),
    ("D + R", ["~", "^", "->", "=>"]),
    ("Y + I", ["<", ">", "<<", ">>"]),
    ("L + T", ["!", "?", "//", "..."]),
    ("M + H", ["_", "-", "++", "--"]),
    ("U + E", [";", "'", "/*", "*/"]),
    ("O + S", ["#", "%", "=", "|"]),
    ("L + H", [":", '"', "::", ":="]),
    ("U + S", ["/", "\\", "+", "@"]),
]
# German letters (letter + Space chord) and the freed N + R acute/backtick.
GERMAN = [
    ("S + Space", "\u00df"),   # Eszett
    ("A + Space", "\u00e4"),   # a-umlaut
    ("O + Space", "\u00f6"),   # o-umlaut
    ("U + Space", "\u00fc"),   # u-umlaut
    ("N + R", "\u00b4"),       # acute (shift: backtick)
]
BIGRAMS = ["RL", "KT", "MB", "YS", "EO", "UI", "RW", "MT", "SCH", "GS", "OE", "IU"]
A1 = BIGRAMS[:6]
A2 = BIGRAMS[6:]

TOKENS = []
for _, outs in CHORDS:
    TOKENS.extend(outs)
for _, tok in GERMAN:
    TOKENS.append(tok)
TOKENS.extend(BIGRAMS)
N_TOKENS = len(TOKENS)
assert N_TOKENS == 81, f"expected 81 chord states, got {N_TOKENS}"
# Bracket characters are produced by both hands (e.g. "(" is L+N plain and
# Y+E shift), so ( ) [ ] { } each legitimately appear twice. Everything else
# must be unique.
_dupes = {t: c for t, c in Counter(TOKENS).items() if c > 1}
assert set(_dupes) == set("()[]{}"), f"unexpected duplicate tokens: {_dupes}"
assert all(c == 2 for c in _dupes.values()), f"bracket dupes must be exactly x2: {_dupes}"

# --- Words containing the bigram letter pairs (mostly German, some English) ---
# Each word is tagged with the bigram(s) / German letters it drills. Every tag
# is asserted against the actual word at import time below.
WORDS = [
    # rl (L+R)
    ("erleben", ["rl"]),
    ("erlöst", ["rl"]),
    ("erlitten", ["rl"]),
    ("erlaubt", ["rl"]),
    ("Erlösung", ["rl"]),
    # kt (M+T)
    ("aktuell", ["kt"]),
    ("Diktat", ["kt"]),
    ("Diktatur", ["kt"]),
    ("Kontakt", ["kt"]),
    ("Kaktus", ["kt"]),
    # mb (D+H)
    ("Symbol", ["mb"]),
    ("Kombi", ["mb"]),
    ("Amboss", ["mb"]),
    ("Kombination", ["mb"]),
    ("umbringt", ["mb"]),
    # ys (Y+S)
    ("System", ["ys"]),
    ("Systeme", ["ys"]),
    ("Analyse", ["ys"]),
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
    # rw (X+W)
    ("erwartet", ["rw"]),
    ("erwartung", ["rw"]),
    ("erwachsene", ["rw"]),
    ("erwache", ["rw"]),
    # mt (V+K)
    ("Amt", ["mt"]),
    ("Amtsstube", ["mt"]),
    ("Amtsblatt", ["mt"]),
    ("amtieren", ["mt"]),
    # sch (B+F, a2 -- drills the a2 layer switch mid-word)
    ("Schule", ["sch"]),
    ("schön", ["sch"]),
    ("Maschine", ["sch"]),
    ("schreiben", ["sch"]),
    ("Schrift", ["sch"]),
    ("Schritt", ["sch"]),
    # gs (G+C, a2 -- the pair is rare in German, mostly English words)
    ("bags", ["gs"]),
    ("dogs", ["gs"]),
    ("tags", ["gs"]),
    ("flags", ["gs"]),
    ("mugs", ["gs"]),
    ("bugs", ["gs"]),
    # oe (J+Q, a2)
    ("Koeffizient", ["oe"]),
    ("Koexistenz", ["oe"]),
    ("Koeln", ["oe"]),
    # iu (comma+dot, a2 -- rare pair; Latin/loan forms)
    ("Iulius", ["iu"]),
    ("Iunius", ["iu"]),
    ("equinoctium", ["iu"]),
    # German letter chords: ß (S+Space), ä (A+Space), ö (O+Space), ü (U+Space)
    ("Straße", ["\u00df"]),
    ("größer", ["\u00df", "\u00f6"]),
    ("heiß", ["\u00df"]),
    ("Küsse", ["\u00fc"]),
    ("grüßen", ["\u00fc", "\u00df"]),
    ("während", ["\u00e4"]),
    ("Mädchen", ["\u00e4"]),
    ("Käse", ["\u00e4"]),
    ("Hände", ["\u00e4"]),
    ("Höfe", ["\u00f6"]),
    ("Höhlen", ["\u00f6"]),
    ("Vögel", ["\u00f6"]),
    ("Müde", ["\u00fc"]),
    ("Hütte", ["\u00fc"]),
    ("Küche", ["\u00fc"]),
    ("Hüpfen", ["\u00fc"]),
]

# General German words that contain NONE of the 12 bigram pair sequences —
# they only need plain letters (plus the umlaut chords in the tagged pool
# above), so they can join the curriculum early (stage 2) while the a1/a2
# bigram layers are still being learned.
PLAIN_WORDS = [
    "Haus", "Maus", "Hund", "Kind", "Wind",
    "Hand", "Nacht", "Licht", "Wasser", "Baum",
    "Apfel", "Vogel", "Wolke", "Fenster", "Buch",
    "Bett", "Morgen", "Glas", "Wiese", "Tanne",
]

WORD_TAGS = {
    "rl": "L+R", "kt": "M+T", "mb": "D+H", "ys": "Y+S", "eo": "O+E", "ui": "U+I",
    "rw": "X+W", "mt": "V+K", "sch": "B+F (a2)", "gs": "G+C (a2)",
    "oe": "J+Q (a2)", "iu": ",+. (a2)",
    "\u00df": "S+Space", "\u00e4": "A+Space", "\u00f6": "O+Space", "\u00fc": "U+Space",
}

# Verify: every tag must actually occur in the word.
for _word, _tags in WORDS:
    for _t in _tags:
        assert _t in _word.lower(), f"word {_word!r} does not contain {_t!r}"
_word_names = [w for w, _ in WORDS]
assert len(set(_word_names)) == len(_word_names), "duplicate words!"
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
assert not set(PLAIN_WORDS) & set(_word_names), "plain words duplicate tagged words"
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
     "reines Chord-Gef\u00fchl: 16 Plain-Outputs, keine Modifier",
     PLAIN),
    ("2", "Plain + Ctrl + erste W\u00f6rter",
     "Operatoren dazu + allgemeine deutsche W\u00f6rter ohne Bigrams "
     "(Alpha-Grid \u00fcbt mit) \u2014 immer noch kein Shift",
     PLAIN + CTRL + WORDS_EARLY),
    ("3", "+ a1-Bigrams + Layer-1-W\u00f6rter",
     "a1 komplett: Bigrams + die W\u00f6rter, die nur a1-Chords brauchen",
     PLAIN + CTRL + A1 + WORDS_A1),
    ("4", "Alle Symbole",
     "Shift-Zust\u00e4nde kommen dazu (+ \u00b4 aus N + R)",
     PLAIN + SHIFT + CTRL + CTRL_SHIFT + [GERMAN[4][1]] + WORDS_A1),
    ("5", "+ a2-Bigrams + alle W\u00f6rter",
     "die komplette Keymap: a2-Bigrams (Layerwechsel mitten im Wort) + alle W\u00f6rter",
     TOKENS + WORDS_ALL),
    ("6", "W\u00f6rter",
     f"alles im echten Tipp-Kontext ({N_WORDS} W\u00f6rter)",
     WORDS_ALL),
]
# Final exam: every token \u2014 81 chord outputs + all words \u2014 exactly once.
EXAM = ("7", "Vollpass (Abschluss)", "alles in einem Durchgang", TOKENS + WORDS_ALL)

PER_LINE = 10
MIN_BLOCK_CHARS = 2800
MAX_BLOCK_CHARS = 4200  # stay well below Monkeytype's 10k custom-test limit
OUT = Path(__file__).resolve().parent / "twonr9_chords_monkeytype.md"


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
    out.append("### Deutsche Buchstaben (Buchstabe + Space, a1/a2)\n")
    out.append("| Chord | Output (Shift = Grossbuchstabe) |")
    out.append("| --- | --- |")
    out.append("| S + Space | \u00df / \u1e9e |")
    out.append("| A + Space | \u00e4 / \u00c4 |")
    out.append("| O + Space | \u00f6 / \u00d6 |")
    out.append("| U + Space | \u00fc / \u00dc |")
    out.append("| N + R | \u00b4 (Shift: `) |")
    out.append("")
    out.append("### Bigrams (12)\n")
    out.append("| Layer | Chords |")
    out.append("| --- | --- |")
    out.append("| a1 | RL \u00b7 KT \u00b7 MB \u00b7 YS \u00b7 EO \u00b7 UI |")
    out.append("| a2 | RW \u00b7 MT \u00b7 SCH \u00b7 GS \u00b7 OE \u00b7 IU |")
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
    out.append("> W\u00f6rter mit `sch`/`gs`/`oe`/`iu` erzwingen einen a2-Layerwechsel mitten im Wort "
               "(das ist der Punkt des Drills). Bei den seltenen Paaren `gs` und `iu` fehlen "
               "h\u00e4ufige deutsche W\u00f6rter, daher englische bzw. Lehnformen.\n")
    out.append("### Home-Row-Symbol-Combos (alle Alpha-Layer)\n")
    out.append("| Chord | Output |")
    out.append("| --- | --- |")
    out.append("| R + H | _ (auch M + H \u00b7 Plain) |")
    out.append("| R + T | - (auch M + H \u00b7 Shift) |")
    out.append("| E + I | : (auch L + H \u00b7 Plain) |")
    out.append("| S + I | ; (auch U + E \u00b7 Plain) |")
    out.append("")
    out.append("> `_ - : ;` kommen im Pool nur einmal pro Runde vor (Chord-Pfad); "
               "beide Wege liefern das gleiche Zeichen.\n")
    return "\n".join(out)


def main():
    parts = []
    parts.append("# TwoNr9 \u2014 Chord-Praxis (Monkeytype)\n")
    parts.append(
        "Diese Datei enth\u00e4lt ein **Stufen-\u00dcbungssystem** f\u00fcr die TwoNr9-Keymap "
        "(bugwind) \u2014 Qualit\u00e4t vor Quantit\u00e4t: "
        f"{len(STAGES) + 1} aufeinander aufbauende Bl\u00f6cke, die in der Schwierigkeit steigen "
        "(Plain \u2192 +Ctrl/+erste W\u00f6rter \u2192 +a1-Bigrams/+Layer-1-W\u00f6rter \u2192 +Shift "
        "\u2192 +a2-Bigrams/+alle W\u00f6rter \u2192 W\u00f6rter \u2192 Vollpass). Die W\u00f6rter drillen ab "
        "Stufe 2 auch das Alpha-Grid: zuerst W\u00f6rter ohne Bigram-Paare, dann die, die a1- bzw. "
        "a2-Chords brauchen \u2014 so wachsen die W\u00f6rter mit den Layer-Kenntnissen mit. "
        "Jeder Block ist selbstst\u00e4ndig (nur sein eigener Pool) und wird Round-Robin gezogen: "
        "pro voller Runde kommt jeder Token genau einmal vor, egal an welcher Stelle Monkeytype "
        "zuf\u00e4llig ansetzt \u2014 jeder Ausschnitt ist gleichm\u00e4\u00dfig.\n")
    parts.append("## Nutzung in Monkeytype\n")
    parts.append("1. Den Block der aktuellen Stufe kopieren (Code-Block, < 10.000 Zeichen).")
    parts.append("2. Monkeytype \u2192 Test Type **Custom** \u2192 Text einf\u00fcgen.")
    parts.append("3. Test-L\u00e4nge z.\u00a0B. auf 25\u201375 W\u00f6rter stellen; Monkeytype w\u00e4hlt aus dem "
                 "Block einen zuf\u00e4lligen Ausschnitt.")
    parts.append("4. Erst zur n\u00e4chsten Stufe wechseln, wenn die aktuelle sauber l\u00e4uft. "
                 "Stufe 7 (Vollpass) ist die Abschlusspr\u00fcfung: jeder Token genau einmal.\n")
    parts.append("Beim \u00dcben auf der TwoNr9 zeigt die Legende unten, welcher Token welchen "
                 "Chord + Modifier-Zustand triggert.\n")
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
