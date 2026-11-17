#!/usr/bin/env python3
"""Generate practice text for the TwoNr9 chord keymap (srht) for Monkeytype.

Nothing here is typed in by hand. The chords are read from the firmware
(config/twonr9_symbol_chords.dtsi: positions and the outputs of their macros),
the bigram and umlaut chords from config/twonr9_combos_srht.dtsi and
config/symbol_work.dtsi, and the letters at each position from the drawing
(draw/twonr9_srht.yaml). When the keymap changes, the practice follows.

The stages follow the modifier states of the chords, then two remixes:

    1  Plain            the pairs, no modifier
    2  + Shift          the shift states (opposite-hand index mod)
    3  + Ctrl           the ctrl states (opposite-hand pinky mod)
    4  + Cmd            the cmd states (opposite-hand middle mod)
    5  + Alt            the alt states (opposite-hand ring mod)
    6  + Quad           the quad (shift + cmd, four keys)
    7  + a1 Bigramme    a1 bigrams, umlauts, acute, plain words
    8  + a2 Bigramme    a2 bigrams, a1 words
    9  Wörter           the full word pool in context
    10 Vollpass         every chord output and every word, once
    R1 Remix Operatoren ctrl, cmd, alt and quad outputs mixed with words
    R2 Remix Symbole    single-chord outputs and bigrams, no words

Each stage is cumulative (except the remixes) and drawn round-robin, so every
fixed-length slice is uniform: each token appears once per full round.

Run:  python3 practice/gen_monkeytype_srht.py
      (writes practice/twonr9_srht_chords_monkeytype.md)
"""
import random
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from words import PLAIN_WORDS, WORD_TAGS, WORDS  # noqa: E402,F401

ROOT = Path(__file__).resolve().parents[1]
CHORDS_DTSI = ROOT / "config/twonr9_symbol_chords.dtsi"
SRHT_COMBOS = ROOT / "config/twonr9_combos_srht.dtsi"
SRHT_MACROS = ROOT / "config/twonr9_macros_srht.dtsi"
SYMBOL_WORK = ROOT / "config/symbol_work.dtsi"
DRAW = ROOT / "draw/twonr9_srht.yaml"
OUT = Path(__file__).resolve().parent / "twonr9_srht_chords_monkeytype.md"

# German keycode names (config/keys_de.h) -> the character they type.
DE_CHAR = {
    "DE_LPAR": "(", "DE_RPAR": ")", "DE_LBRC": "{", "DE_RBRC": "}",
    "DE_LBKT": "[", "DE_RBKT": "]", "DE_LT": "<", "DE_GT": ">",
    "DE_EQUAL": "=", "DE_PLUS": "+", "DE_MINUS": "-", "DE_UNDER": "_",
    "DE_FSLH": "/", "DE_BSLH": "\\", "DE_AMPS": "&", "DE_PIPE": "|",
    "DE_DOLLAR": "$", "DE_CARET": "^", "DE_DQT": '"', "DE_SQT": "'",
    "DE_SEMI": ";", "DE_COLON": ":", "DE_COMMA": ",", "DE_DOT": ".",
    "DE_ASTRK": "*", "DE_HASH": "#", "DE_EXCL": "!", "DE_QMARK": "?",
    "DE_AT": "@", "DE_TILDE": "~", "DE_GRAVE": "`", "DE_PRCNT": "%",
    "DE_EURO": "\u20ac",
}

# Mod keys (ZMK positions). Left-hand pairs take the right-hand mods, right-hand
# pairs the left-hand ones: shift is the opposite index, cmd the opposite middle,
# alt the opposite ring, ctrl the opposite pinky.
LEFT_MODS = {10: "shift", 11: "cmd", 12: "alt", 13: "ctrl"}
RIGHT_MODS = {9: "shift", 8: "cmd", 7: "alt", 6: "ctrl"}
MOD_STATE = {**LEFT_MODS, **RIGHT_MODS}
TWO_MODS = {frozenset(("shift", "cmd")): "shiftcmd",
            frozenset(("shift", "alt")): "shiftalt",
            frozenset(("shift", "ctrl")): "shiftctrl"}
STATES = ["plain", "shift", "cmd", "shiftcmd", "alt", "shiftalt", "ctrl", "shiftctrl"]
CURSOR_KEYS = {"LEFT", "RIGHT", "UP", "DOWN"}

PER_LINE = 10
MIN_BLOCK_CHARS = 2800
MAX_BLOCK_CHARS = 4200  # stay well below Monkeytype's 10k custom-test limit


def parse_macros(text):
    """Macro name -> the characters its bindings type (DE_ keys or plain letters)."""
    out = {}
    for name, body in re.findall(r"ZMK_MACRO\((\w+),\s*bindings = <(.*?)>;", text, re.S):
        chars = []
        for key in re.findall(r"&kp (\w+)", body):
            if key in CURSOR_KEYS:
                continue          # `{}` types the pair and leaves the cursor inside
            if key in DE_CHAR:
                chars.append(DE_CHAR[key])
            elif re.fullmatch(r"DE_[A-Z]", key):
                chars.append(key[3].lower())
            elif len(key) == 1:
                chars.append(key.lower())
            else:
                raise ValueError(f"macro {name}: unknown key {key}")
        out[name] = "".join(chars)
    return out


def parse_chords():
    """Every plain, triplet and quad chord: (positions, output)."""
    text = CHORDS_DTSI.read_text(encoding="utf-8")
    macros = parse_macros(text)
    chords = []
    pattern = r"ZMK_COMBO\((\w+),\s*(&kp DE_\w+|&\w+),\s*([0-9 ]+?),\s*L_A1 L_A2\)"
    for _name, binding, pos in re.findall(pattern, text):
        if binding.startswith("&kp "):
            out = DE_CHAR[binding[4:]]
        else:
            out = macros[binding[1:]]
        chords.append((tuple(sorted(int(p) for p in pos.split())), out))
    return chords


def parse_bigrams():
    """Bigram chords: (layer, positions, output)."""
    text = SRHT_COMBOS.read_text(encoding="utf-8")
    macros = parse_macros(SRHT_MACROS.read_text(encoding="utf-8"))
    out = []
    for _name, macro, a, b, layer in re.findall(
            r"ZMK_COMBO\(combo_(\w+),\s*&macro_(\w+),\s*(\d+) (\d+),\s*L_A(\d)\)", text):
        out.append((int(layer), (int(a), int(b)), macros[f"macro_{macro}"]))
    return out


def parse_umlauts():
    """The vowel and Eszett + Space chords, plus the acute (S + R)."""
    text = SYMBOL_WORK.read_text(encoding="utf-8")
    names = {"de_sz": "\u00df", "de_ae": "\u00e4", "de_oe": "\u00f6", "de_ue": "\u00fc"}
    out = []
    for name, a, b in re.findall(r"ZMK_COMBO\(combo_(de_\w+),\s*&de_\w+,\s*(\d+)\s+(\d+),", text):
        out.append(((int(a), int(b)), names[name]))
    out.append(((6, 7), "\u00b4"))  # acute, combo_diag_67, kept in symbol_work.dtsi
    return out


def letters():
    data = yaml.safe_load(DRAW.read_text(encoding="utf-8"))
    return {layer: [key["t"] for key in data["layers"][layer]] for layer in ("a1", "a2")}


def cell(tok):
    """A token as a Markdown table cell: pipes escaped, backticks fenced."""
    t = tok.replace("|", "\\|")
    return f"`` {t} ``" if "`" in t else f"`{t}`"


def label(positions, letter_map):
    return " + ".join(letter_map[p] for p in positions)


LEFT_KEYS = {0, 1, 2, 6, 7, 8, 9}


def build_table(chords, letter_map):
    """(pair, state) -> (label, output) for every chord that uses a pair.

    A chord's mod comes from the hand opposite its pair: a left-hand pair takes
    the right-hand mods (10-13), a right-hand pair the left-hand ones (6-9).
    """
    letter_map = letter_map["a1"]
    pairs = {pos for pos, _ in chords if len(pos) == 2}
    table = {}
    for pos, out in chords:
        pair = next((q for q in pairs if set(q) <= set(pos)), None)
        assert pair is not None, f"chord {pos} has no pair"
        extras = [p for p in pos if p not in pair]
        if not extras:
            table[(pair, "plain")] = (label(pair, letter_map), out)
            continue
        names = sorted(MOD_STATE[p] for p in extras)
        state = names[0] if len(names) == 1 else TWO_MODS.get(frozenset(names))
        assert state, f"chord {pos} has mods {names}"
        extra = " + ".join(letter_map[p] for p in extras)
        table[(pair, state)] = (f"{label(pair, letter_map)} + {extra}", out)
    return table


def perm_for(tokens, seed, salt=0):
    rng = random.Random(1000 + (seed + salt) * 7919)
    perm = tokens[:]
    rng.shuffle(perm)
    return perm


def block_text(perm, rounds):
    lines = []
    for _ in range(rounds):
        for i in range(0, len(perm), PER_LINE):
            lines.append(" ".join(perm[i:i + PER_LINE]))
    return "\n".join(lines)


def fit_rounds(perm):
    rounds = 1
    while len(block_text(perm, rounds + 1)) <= MAX_BLOCK_CHARS:
        rounds += 1
    return rounds


def make_block(num, perm, rounds):
    """Verify the block holds only its own pool, each token exactly `rounds` times."""
    text = block_text(perm, rounds)
    pool = Counter(perm)
    seen = Counter(text.split())
    assert set(seen) == set(pool), f"stage {num}: foreign tokens {set(seen) - set(pool)}"
    for tok, n in pool.items():
        assert seen[tok] == rounds * n, f"stage {num}: {tok!r} count {seen[tok]} != {rounds * n}"
    return text


def main():
    chords = parse_chords()
    letter_map = letters()
    a1, a2 = letter_map["a1"], letter_map["a2"]
    table = build_table(chords, letter_map)
    bigrams = parse_bigrams()
    umlauts = parse_umlauts()

    def state(s):
        return [out for (_pos, st), (_lbl, out) in table.items() if st == s]

    plain = state("plain")
    shift = state("shift")
    cmd = state("cmd")
    shiftcmd = state("shiftcmd")
    alt = state("alt")
    shiftalt = state("shiftalt")
    ctrl = state("ctrl")
    shiftctrl = state("shiftctrl")
    a1_bi = [out for layer, _, out in bigrams if layer == 1]
    a2_bi = [out for layer, _, out in bigrams if layer == 2]
    umlaut_out = [out for _, out in umlauts]

    # Word tiers from the tags: umlaut-only, a1, a2.
    umlaut_chars = set("\u00df\u00e4\u00f6\u00fc")
    a1_tags = {t.lower() for t in a1_bi}
    a2_tags = {t.lower() for t in a2_bi}
    tier_a2 = [w for w, tags in WORDS if a2_tags & set(tags)]
    tier_a1 = [w for w, tags in WORDS if a1_tags & set(tags) and not a2_tags & set(tags)]
    tier_umlaut = [w for w, tags in WORDS if set(tags) and set(tags) <= umlaut_chars]
    words_early = PLAIN_WORDS + tier_umlaut
    words_a1 = words_early + tier_a1
    words_all = words_a1 + tier_a2
    assert len(set(words_all)) == len(words_all) == len(WORDS) + len(PLAIN_WORDS), \
        "word tiers must partition the word pool"
    covered = {t for _, tags in WORDS for t in tags}
    missing = (a1_tags | a2_tags | umlaut_chars) - covered
    assert not missing, f"bigrams or umlauts without a word: {sorted(missing)}"

    s1 = plain
    s2 = s1 + shift
    s3 = s2 + cmd
    s4 = s3 + shiftcmd
    s5 = s4 + alt
    s6 = s5 + shiftalt
    s7 = s6 + ctrl
    s8 = s7 + shiftctrl
    s9 = s8 + a1_bi + umlaut_out + words_early
    s10 = s9 + a2_bi + words_a1
    s11 = words_all
    s12 = s8 + a1_bi + a2_bi + umlaut_out + words_all
    r1 = cmd + shiftcmd + alt + shiftalt + ctrl + shiftctrl + words_early
    r2 = plain + shift + a1_bi + a2_bi + umlaut_out

    stages = [
        ("1", "Plain", "18 Paare ohne Modifier", s1),
        ("2", "+ Shift", "Shift-Zust\u00e4nde (gegen\u00fcberliegender Zeigefinger)", s2),
        ("3", "+ Cmd", "Cmd-Zust\u00e4nde (gegen\u00fcberliegender Mittelfinger)", s3),
        ("4", "+ Shift+Cmd", "Shift + Cmd, vier Tasten", s4),
        ("5", "+ Alt", "Alt-Zust\u00e4nde (gegen\u00fcberliegender Ringfinger)", s5),
        ("6", "+ Shift+Alt", "Shift + Alt, vier Tasten", s6),
        ("7", "+ Ctrl", "Ctrl-Zust\u00e4nde (gegen\u00fcberliegender kleiner Finger)", s7),
        ("8", "+ Shift+Ctrl", "Shift + Ctrl, vier Tasten", s8),
        ("9", "+ a1-Bigramme", "a1-Bigramme, Umlaute, \u00b4, W\u00f6rter ohne Bigram-Paare", s9),
        ("10", "+ a2-Bigramme", "a2-Bigramme (Layerwechsel mitten im Wort), a1-W\u00f6rter", s10),
        ("11", "W\u00f6rter", f"alles im Tipp-Kontext ({len(words_all)} W\u00f6rter)", s11),
        ("12", "Vollpass", "jeder Token einmal (Abschluss)", s12),
        ("R1", "Remix Operatoren", "Ctrl-, Cmd-, Alt- und Quad-Zust\u00e4nde mit W\u00f6rtern gemischt", r1),
        ("R2", "Remix Symbole", "Einzel-Chords und Bigramme, ohne W\u00f6rter", r2),
    ]

    parts = [
        "# TwoNr9 srht \u2014 Chord-Praxis (Monkeytype)\n",
        "Stufen nach Modifier-Zust\u00e4nden: erst die Paare, dann je ein Zustand dazu, dann die "
        "Bigramme und W\u00f6rter. Jede Stufe enth\u00e4lt alles aus den vorigen; die Remixe mischen "
        "Zust\u00e4nde und W\u00f6rter neu. Die Chords werden aus Firmware und Zeichnung gelesen, "
        "nicht von Hand gepflegt.\n",
        "## Nutzung in Monkeytype\n",
        "1. Den Block der Stufe kopieren (Code-Block, unter 10.000 Zeichen).",
        "2. Monkeytype \u2192 Test Type **Custom** \u2192 Text einf\u00fcgen.",
        "3. Erst zur n\u00e4chsten Stufe, wenn die aktuelle sauber l\u00e4uft. Die Remixe "
        "gehen nach Stufe 10.\n",
        "## Legende\n",
        "### Stufen\n",
        "| Stufe | Name | Was er \u00fcbt | Tokens |",
        "| --- | --- | --- | --- |",
    ]
    for num, name, desc, pool in stages:
        parts.append(f"| {num} | {name} | {desc} | {len(pool)} |")
    parts.append("")
    parts.append("### Chords nach Paar\n")
    parts.append("| Paar | Plain | + Shift | + Ctrl | + Cmd | + Alt | Quad |")
    parts.append("| --- | --- | --- | --- | --- | --- | --- |")
    pair_positions = sorted({pos for pos, _ in table})
    for pos in pair_positions:
        cells = []
        for st in ("plain", "shift", "ctrl", "cmd", "alt", "shiftcmd"):
            entry = table.get((pos, st))
            cells.append(cell(entry[1]) if entry else "\u2014")
        pair_label = table[(pos, "plain")][0] if (pos, "plain") in table else label(pos, letter_map["a1"])
        parts.append(f"| {pair_label} | " + " | ".join(cells) + " |")
    parts.append("")
    parts.append("### Bigramme\n")
    parts.append("| Layer | Chords |")
    parts.append("| --- | --- |")
    parts.append(f"| a1 | {' \u00b7 '.join(a1_bi)} |")
    parts.append(f"| a2 | {' \u00b7 '.join(a2_bi)} |")
    parts.append("")
    parts.append("### Deutsche Buchstaben\n")
    parts.append("| Chord | Output |")
    parts.append("| --- | --- |")
    for (a, b), out in umlauts:
        parts.append(f"| {label((a, b), a1)} | {cell(out)} |")
    parts.append("")
    parts.append("### W\u00f6rter\n")
    parts.append(f"**Stufe 7**, ohne Bigram-Paare: {', '.join(PLAIN_WORDS)}")
    parts.append(f"\n**Stufe 8**, a1-Bigramme: {', '.join(tier_a1)}")
    parts.append(f"\n**Stufe 9**, a2-Bigramme (Layerwechsel): {', '.join(tier_a2)}\n")
    parts.append("### Adaptive Keys (9, nur srht)\n")
    parts.append("Innerhalb von 300 ms nach dem Trigger gibt ein adaptiver Key den Partner aus "
                 "\u2014 schnelles `rh` kann als `rl` herauskommen. Die Chords (beide Tasten "
                 "gleichzeitig) sind nicht betroffen.\n")

    sizes = []
    for num, name, _desc, pool in stages:
        perm = perm_for(pool, int(num.lstrip("R")) + (100 if num.startswith("R") else 0))
        rounds = fit_rounds(perm)
        body = make_block(num, perm, rounds)
        assert MIN_BLOCK_CHARS <= len(body) <= MAX_BLOCK_CHARS, \
            f"stage {num}: {len(body)} chars outside the band"
        parts.append(f"## Stufe {num} \u2014 {name} "
                     f"({rounds} Runden \u00b7 {rounds * len(pool)} Tokens \u00b7 {len(body)} Zeichen)\n")
        parts.append("```")
        parts.append(body)
        parts.append("```\n")
        sizes.append(len(body))

    doc = "\n".join(parts)
    OUT.write_text(doc, encoding="utf-8")
    print(f"stages: {len(stages)}, block chars: {sizes}")
    print(f"chord states: {len(table)} on {len(pair_positions)} pairs; bigrams: {len(bigrams)}; "
          f"umlauts: {len(umlauts)}; words: {len(words_all)}")


if __name__ == "__main__":
    sys.exit(main())
