#!/usr/bin/env python3
"""Write the symbol chords and their drawing entries from one layout table.

The table below is the single source: each pair of keys, and the output of each
of the eight states. It writes

  config/twonr9_symbol_chords.dtsi   the combos and their macros
  draw/twonr9_srht.yaml             the symbol chord entries (other combos kept)

State order: plain, shift, cmd, shift+cmd, alt, shift+alt, ctrl, shift+ctrl.
A state's mod comes from the hand opposite its pair: a left-hand pair takes the
right-hand mods (shift C, cmd E, alt I, ctrl A), a right-hand pair the left-hand
ones (shift T, cmd H, alt R, ctrl S). Every "second" state is its mod plus shift.

    python3 draw/gen_symbols.py            # rewrite both files
    python3 draw/gen_symbols.py --check    # fail if they are out of date
"""
import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DTSI = ROOT / "config/twonr9_symbol_chords.dtsi"
DRAWING = ROOT / "draw/twonr9_srht.yaml"
# The layers a symbol chord is live on, in the firmware's ids and the drawing's
# names: every layer but mouse. ZMK matches a combo against the *highest* active
# layer (combo_active_on_layer in zmk/app/src/combo.c), so the vim layers have to
# be named even though they are transparent -- in normal/visual a symbol chord is
# the only way to type a bare ( or " there, which is what ci( and r; need.
SYMBOL_LAYERS = ("L_A1 L_A2 L_NAV L_SYM L_FN L_NUM "
                 "L_VIM_NORMAL L_VIM_VISUAL L_VIM_INSERT L_VIM_CMDLINE")
SYMBOL_DRAW = ["a1", "a2", "nav", "sym", "fn", "num",
               "vim_normal", "vim_visual", "vim_insert", "vim_cmdline"]
# Where the base alphabet is what you type: the hand-written typing combos belong
# here, not on normal/visual where those keys are motions. Mouse stays out too.
TYPING_DRAW = ["a1", "a2", "nav", "sym", "fn", "num", "vim_insert", "vim_cmdline"]
# An empty layer list means every layer (how host/keymap.py reads it).
ALL_DRAW = []

# A two-key chord only fires after this long without a key, so a fast roll of two
# motions (ci, di, jk) types them instead of firing one. Mirrored by `combo_idle_ms`
# in the HUD's config.yaml.
CHORD_IDLE_MS = 40
DOCS = ROOT / "docs/SYMBOLS.md"
# The letters printed on a1, by ZMK position (0-13).
LETTERS = ["L", "N", "D", "Y", "O", "U", "S", "R", "H", "T", "C", "E", "I", "A"]
FINGER = ["ring", "middle", "index", "index", "middle", "ring",
          "pinky", "ring", "middle", "index", "index", "middle", "ring", "pinky"]
POS = LETTERS + ["Shift", "a2", "Spc", "Num"]
# Families, by the first character of a pair's plain token.
GROUPS = [("Brackets & comparisons", "([{<"),
          ("Arithmetic", "-=*%/"),
          ("Punctuation", ",;"),
          ("Logic & symbols", "&$@!"),
          ("Quoting & LaTeX", '`"\\')]


STATE_ORDER = ["plain", "shift", "cmd", "shiftcmd", "alt", "shiftalt", "ctrl", "shiftctrl"]
LEFT_MODS = {"shift": 10, "cmd": 11, "alt": 12, "ctrl": 13}
RIGHT_MODS = {"shift": 9, "cmd": 8, "alt": 7, "ctrl": 6}
LEFT_KEYS = {0, 1, 2, 6, 7, 8, 9}

# token letter -> the German keycode that types it
KEY = {"(": "DE_LPAR", ")": "DE_RPAR", "[": "DE_LBKT", "]": "DE_RBKT", "{": "DE_LBRC",
       "}": "DE_RBRC", "<": "DE_LT", ">": "DE_GT", "=": "DE_EQUAL", "+": "DE_PLUS",
       "-": "DE_MINUS", "_": "DE_UNDER", "/": "DE_FSLH", "\\": "DE_BSLH", "&": "DE_AMPS",
       "|": "DE_PIPE", "$": "DE_DOLLAR", "^": "DE_CARET", '"': "DE_DQT", "'": "DE_SQT",
       ";": "DE_SEMI", ":": "DE_COLON", ",": "DE_COMMA", ".": "DE_DOT", "*": "DE_ASTRK",
       "#": "DE_HASH", "!": "DE_EXCL", "?": "DE_QMARK", "@": "DE_AT", "~": "DE_TILDE",
       "`": "DE_GRAVE", "%": "DE_PRCNT", "\u20ac": "DE_EURO"}
LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# `{}` and friends are typed as the pair with the cursor left in the middle.
CURSOR_INSIDE = {"()", "[]", "{}"}

# pair (ZMK positions) -> {state: token or None}
TABLE = {
    (1, 9): {"plain": "(", "shift": ")", "cmd": "==", "shiftcmd": "!=", "alt": "=>", "ctrl": "()"},
    (2, 8): {"plain": "<", "shift": ">", "cmd": "<=", "shiftcmd": ">=", "alt": "<<",
             "shiftalt": ">>", "ctrl": "->", "shiftctrl": "<-"},
    (1, 6): {"plain": "[", "shift": "]", "cmd": "\\[", "shiftcmd": "\\]", "alt": "[[",
             "shiftalt": "]]", "ctrl": "[]", "shiftctrl": "[^]"},
    (1, 7): {"plain": "{", "shift": "}", "cmd": "\\{", "shiftcmd": "\\}", "alt": "{{",
             "shiftalt": "}}", "ctrl": "{}"},
    (0, 6): {"plain": "/", "shift": "./", "cmd": "/*", "shiftcmd": "*/", "ctrl": "//",
             "shiftctrl": "///"},
    (0, 8): {"plain": "-", "shift": "_", "cmd": "--", "shiftcmd": "__", "alt": "---",
             "shiftalt": "++", "ctrl": "\\_"},
    (0, 9): {"plain": "&", "shift": "|", "cmd": "&&", "shiftcmd": "||", "alt": "&=",
             "shiftalt": "|=", "ctrl": "\\&"},
    (2, 6): {"plain": "$", "shift": "^", "cmd": "\\$", "shiftcmd": "\\^", "alt": "$$"},
    (2, 7): {"plain": '"', "shift": "'", "cmd": '""', "shiftcmd": "''", "alt": "'''",
             "shiftalt": '"""'},
    (4, 10): {"plain": ";", "shift": ":", "cmd": "::", "alt": ";;"},
    (3, 11): {"plain": ",", "shift": ".", "cmd": "..", "shiftcmd": "..<", "alt": "..."},
    (3, 12): {"plain": "!", "shift": "?", "cmd": "?.", "shiftcmd": "?:", "alt": "!!",
              "shiftalt": "!?"},
    (4, 12): {"plain": "*", "shift": "#", "cmd": "**", "shiftcmd": "##", "alt": "###",
              "ctrl": "\\#"},
    (3, 13): {"plain": "`", "cmd": "```", "alt": "~~~", "ctrl": "``"},
    (4, 13): {"plain": "@", "shift": "~", "alt": "\u20ac", "ctrl": "~~"},
    (5, 11): {"plain": "=", "shift": "+", "cmd": "-=", "shiftcmd": "+=", "alt": "|=",
              "shiftalt": "&=", "ctrl": "^="},
    (5, 13): {"plain": "\\", "shift": "\\(", "cmd": "\\)", "alt": "\\n", "shiftalt": "\\t",
              "ctrl": "\\\\"},
    (5, 10): {"plain": "%", "shift": "%s", "alt": "%%", "ctrl": "\\%"},
}


# Every chord that is not a symbol pair, with the legend the drawing shows. The
# firmware defines them in its combo files; test_chord_consistency compares the
# two so a missing or stale entry fails.
OTHER = [
    ((0, 1), "\u21e5", ALL_DRAW, "util"),
    ((1, 2), "\u23ce", ALL_DRAW, "util"),
    ((3, 4), {"t": "\u232b", "s": "\u2326"}, ALL_DRAW, "util"),
    ((4, 5), "\u2303\u232b", ALL_DRAW, "util"),
    ((3, 4, 5), "\u238b", ALL_DRAW, "util"),
    ((7, 9), "_", SYMBOL_DRAW, "symbol"),
    ((7, 8), "-", SYMBOL_DRAW, "symbol"),
    ((11, 12), ":", SYMBOL_DRAW, "symbol"),
    ((10, 12), ";", SYMBOL_DRAW, "symbol"),
    ((6, 7, 8, 9), "\U0001f513", ["sym"], "sym"),
    ((8, 9), {"t": "\u21e7 repeat", "h": "\u21e7", "s": "\u21aa"}, TYPING_DRAW, "util"),
    ((10, 11), {"t": "\u21e7 repeat", "h": "\u21e7", "s": "\u21aa"}, TYPING_DRAW, "util"),
    ((3, 10), "7", ["num"], "num"),
    ((4, 11), "8", ["num"], "num"),
    ((5, 12), "9", ["num"], "num"),
    ((0, 7), "RL", ["a1"], "bigram"),
    ((1, 8), "HN", ["a1"], "bigram"),
    ((2, 9), "DT", ["a1"], "bigram"),
    ((3, 10), "CY", ["a1"], "bigram"),
    ((4, 11), "EO", ["a1"], "bigram"),
    ((5, 12), "UI", ["a1"], "bigram"),
    ((0, 7), "RM", ["a2"], "bigram"),
    ((1, 8), "NB", ["a2"], "bigram"),
    ((2, 9), "KT", ["a2"], "bigram"),
    ((3, 10), "GY", ["a2"], "bigram"),
    ((4, 11), "OE", ["a2"], "bigram"),
    ((5, 12), "IU", ["a2"], "bigram"),
    ((6, 7), {"t": "\u00b4", "s": "`"}, ["a1", "a2"], "util"),
    ((10, 16), {"t": "\u00df", "s": "\u00df"}, ["a1", "a2"], "symbol"),
    ((13, 16), {"t": "\u00e4", "s": "\u00e4"}, ["a1", "a2"], "util"),
    ((4, 16), {"t": "\u00f6", "s": "\u00f6"}, ["a1", "a2"], "util"),
    ((5, 16), {"t": "\u00fc", "s": "\u00fc"}, ["a1", "a2"], "util"),
    ((14, 15), "a2 + \u21e7", ALL_DRAW, "layer"),
    ((16, 17), "mouse", ["a1", "a2"], "layer"),
    ((0, 1), "BT prev", ["fn"], "util"),
    ((1, 2), "BT next", ["fn"], "util"),
    ((0, 2), "BT clear", ["fn"], "util"),
]


def states_of(table=TABLE):
    """(pair, state, positions, token) for every defined state."""
    out = []
    for pair, states in table.items():
        left = all(p in LEFT_KEYS for p in pair)
        mods = LEFT_MODS if left else RIGHT_MODS
        for state in STATE_ORDER:
            token = states.get(state)
            if not token:
                continue
            if state == "plain":
                pos = tuple(pair)
            elif state in ("shift", "cmd", "alt", "ctrl"):
                pos = tuple(sorted(pair + (mods[state],)))
            elif state == "shiftcmd":
                pos = tuple(sorted(pair + (mods["shift"], mods["cmd"])))
            elif state == "shiftalt":
                pos = tuple(sorted(pair + (mods["shift"], mods["alt"])))
            elif state == "shiftctrl":
                pos = tuple(sorted(pair + (mods["shift"], mods["ctrl"])))
            else:
                raise ValueError(state)
            out.append((pair, state, pos, token))
    return out


def keys_of(token):
    """The &kp arguments a token needs, backslash by backslash."""
    out, i = [], 0
    while i < len(token):
        ch = token[i]
        if ch == "\\":
            out.append(KEY["\\"])
            i += 1
            if i < len(token):
                nxt = token[i]
                out.append(KEY.get(nxt, f"DE_{nxt.upper()}" if nxt.isalpha() else None))
                i += 1
            continue
        if ch in KEY:
            out.append(KEY[ch])
        elif ch.isalpha() and ch.upper() in LETTER:
            out.append(f"DE_{ch.upper()}")
        else:
            raise ValueError(f"token {token!r}: no key for {ch!r}")
        i += 1
    if token in CURSOR_INSIDE:
        out.append("LEFT")
    return out


def macros_and_combos():
    names, macros, combos = set(), [], []
    for pair, state, pos, token in states_of():
        keys = keys_of(token)
        tag = "_".join(str(p) for p in pair) + "_" + state
        if len(keys) == 1:
            binding = f"&kp {keys[0]}"
        else:
            name = f"sym_{tag}"
            macros.append("ZMK_MACRO(%s,\n    bindings = <%s>;\n    wait-ms = <0>;\n    tap-ms = <5>;\n)"
                          % (name, " ".join(f"&kp {k}" for k in keys)))
            binding = f"&{name}"
        idle = f", COMBO_TERM, {CHORD_IDLE_MS}" if len(pos) == 2 else ""
        combos.append(f"ZMK_COMBO(sym_{tag}, {binding}, {' '.join(map(str, pos))}, "
                      f"{SYMBOL_LAYERS}{idle})")
    return macros, combos


def dtsi_text():
    macros, combos = macros_and_combos()
    head = ("/* Symbol chords, generated by draw/gen_symbols.py from its TABLE.\n"
            " * State order: plain, Shift, Cmd, Shift+Cmd, Alt, Shift+Alt, Ctrl, Shift+Ctrl;\n"
            " * the mod comes from the hand opposite the pair. Do not edit by hand. */\n\n")
    return head + "\n".join(macros) + "\n\n" + "\n".join(combos) + "\n"


def drawing_text():
    """The drawing with its layer pictures kept and every chord generated."""
    text = DRAWING.read_text(encoding="utf-8")
    lines = text.split("\n")
    start = lines.index("combos:")
    head = "\n".join(lines[:start + 1])

    def legend(value):
        if isinstance(value, dict):
            return yaml.safe_dump(value, default_flow_style=True, allow_unicode=True,
                                  width=10**9, sort_keys=False).strip()
        return yaml.safe_dump(value, default_style='"', allow_unicode=True, width=10**9).strip()

    blocks = []
    for _pair, _state, pos, token in states_of():
        blocks.append(["- p:"] + [f"  - {p}" for p in pos]
                      + [f"  k: {legend(token)}", "  l:"]
                      + [f"  - {name}" for name in SYMBOL_DRAW] + ["  type: symbol"])
    for pos, key, layers, kind in OTHER:
        block = ["- p:"] + [f"  - {p}" for p in pos] + [f"  k: {legend(key)}"]
        if layers:
            block += ["  l:"] + [f"  - {name}" for name in layers]
        blocks.append(block + [f"  type: {kind}"])
    return head + "\n" + "\n".join("\n".join(b) for b in blocks) + "\n"


def docs_text():
    """The symbol sheet: one source with the firmware and the drawing."""
    pair_rows = {}
    for (pair, states) in TABLE.items():
        pair_rows[pair] = states
    out = ["# Symbol reference", "",
           "_Generated by `draw/gen_symbols.py`; `just check-keymap` fails when it drifts._", "",
           "## How to press a state", "",
           "A state is the pair plus one mod from the other hand, and the Shift variants add Shift.",
           "Left-hand pairs use `⇧C ⌘E ⌥I ⌃A`; right-hand pairs use `⇧T ⌘H ⌥R ⌃S`.",
           "",
           "| state | mod | reads as |", "| --- | --- | --- |",
           "| Plain | — | the opener |",
           "| Shift | ⇧ | the closer |",
           "| Cmd | ⌘ / H | escaped opener |",
           "| Shift+Cmd | ⇧⌘ / ⇧H | escaped closer |",
           "| Alt | ⌥ / R | doubled opener |",
           "| Shift+Alt | ⇧⌥ / ⇧R | doubled closer |",
           "| Ctrl | ⌃ / S | the remaining pair, opener |",
           "| Shift+Ctrl | ⇧⌃ / ⇧S | its closer |",
           "",
           "## Remembering it", "",
           "- **Mods by finger, other hand:** Shift = index, Cmd = middle, Alt = ring, Ctrl = pinky.",
           "- **Every mod has a pair:** mod alone, then mod + Shift — the second one closes.",
           "- **Plain opens, Shift closes:** `(` / `)`, `[` / `]`, `{` / `}`, `<` / `>`.",
           "- **Mirrored hands:** a family sits on the same finger class both sides "
           "(`- _` ↔ `= +`, quotes ↔ backtick, `/` ↔ `\\`).",
           "- **Escapes ride with their character:** `\\_` with `_`, `\\#` with `#`, `\\&` with `&`.",
           ""]

    def legend(token):
        return f"`{token}`"

    def row(pair, states, hint):
        cells = []
        for state in STATE_ORDER:
            token = states.get(state)
            cells.append(legend(token) if token else "—")
        keys = " + ".join(LETTERS[p] for p in pair)
        fingers = " + ".join(FINGER[p] for p in pair)
        return f"| `{keys}` | {fingers} | {hint} | " + " | ".join(cells) + " |"

    def hint_for(pair):
        left = all(p in LEFT_KEYS for p in pair)
        mods = LEFT_MODS if left else RIGHT_MODS
        glyphs = {"shift": "⇧", "cmd": "⌘", "alt": "⌥", "ctrl": "⌃"}
        return " ".join(f"{glyphs[s]}{LETTERS[p]}" for s, p in sorted(mods.items(), key=lambda kv: STATE_ORDER.index(kv[0])))

    for title, chars in GROUPS:
        rows = [row(pair, states, hint_for(pair)) for pair, states in sorted(TABLE.items(), key=lambda kv: kv[0])
                if (states.get("plain") or "")[:1] in chars]
        if not rows:
            continue
        out += [f"## {title}", "",
                "| keys | fingers | mods | " + " | ".join(STATE_ORDER) + " |",
                "| --- | --- | --- | " + " | ".join("---" for _ in STATE_ORDER) + " |"]
        out += rows + [""]

    def other(kind, title):
        items = [(pos, key, layers) for pos, key, layers, k in OTHER if k == kind]
        if not items:
            return
        out.extend([f"## {title}", ""])
        for pos, key, layers in items:
            def code(text):
                return f"`` {text} ``" if "`" in str(text) else f"`{text}`"

            if isinstance(key, dict):
                label = code(key.get("t", ""))
                if key.get("s") and key["s"] != key.get("t"):
                    label += f" (shift {code(key['s'])})"
            else:
                label = code(key)
            keys = " + ".join(POS[p] for p in pos)
            if not layers:
                where = " (every layer)"
            elif layers == ["a1", "a2"]:
                where = ""
            else:
                where = f" ({', '.join(layers)})"
            out.append(f"- `{keys}` → {label}{where}")
        out.append("")

    other("bigram", "Bigrams")
    other("symbol", "Home-row chords")
    other("util", "Utilities")
    other("num", "Numpad")
    other("layer", "Layer access")
    other("sym", "System")
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="do not write; fail if out of date")
    args = ap.parse_args()
    dtsi, drawing, docs = dtsi_text(), drawing_text(), docs_text()
    stale = []
    if DTSI.read_text(encoding="utf-8") != dtsi:
        stale.append(DTSI)
    if DRAWING.read_text(encoding="utf-8") != drawing:
        stale.append(DRAWING)
    if not DOCS.is_file() or DOCS.read_text(encoding="utf-8") != docs:
        stale.append(DOCS)
    if args.check:
        for path in stale:
            print(f"out of date: {path}")
        return 1 if stale else 0
    for path, text in ((DTSI, dtsi), (DRAWING, drawing), (DOCS, docs)):
        path.write_text(text, encoding="utf-8")
    states = states_of()
    print(f"{DTSI.name}: {len(states)} states; {DRAWING.name}: symbol chords replaced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
