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
LAYERS = "L_A1 L_A2"

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
    (0, 8): {"plain": "-", "shift": "_", "cmd": "++", "alt": "--", "shiftalt": "__",
             "ctrl": "---", "shiftctrl": "\\_"},
    (0, 9): {"plain": "&", "shift": "|", "cmd": "&&", "shiftcmd": "||", "alt": "\\&"},
    (2, 6): {"plain": "$", "shift": "^", "cmd": "$$", "shiftcmd": "\\$", "alt": "\\^"},
    (2, 7): {"plain": '"', "shift": "'", "cmd": '""', "shiftcmd": "''", "alt": "'''",
             "shiftalt": '"""'},
    (4, 10): {"plain": ";", "shift": ":", "cmd": "::", "alt": ";;"},
    (3, 11): {"plain": ",", "shift": ".", "cmd": "..", "shiftcmd": "..<", "alt": "..."},
    (3, 12): {"plain": "!", "shift": "?", "cmd": "?.", "shiftcmd": "?:", "alt": "!!",
              "shiftalt": "!?"},
    (4, 12): {"plain": "*", "shift": "#", "cmd": "**", "shiftcmd": "##", "alt": "###",
              "shiftalt": "\\#", "ctrl": "^="},
    (3, 13): {"plain": "`", "cmd": "```", "alt": "~~~", "ctrl": "``"},
    (4, 13): {"plain": "@", "shift": "~", "alt": "\u20ac", "ctrl": "~~"},
    (5, 11): {"plain": "=", "shift": "+", "cmd": "-=", "shiftcmd": "+=", "alt": "|=",
              "shiftalt": "&="},
    (5, 13): {"plain": "\\", "shift": "\\(", "cmd": "\\)", "alt": "\\n", "shiftalt": "\\t",
              "ctrl": "\\\\"},
    (5, 10): {"plain": "%", "shift": "%s", "cmd": "\\%", "alt": "%%"},
}


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
        combos.append(f"ZMK_COMBO(sym_{tag}, {binding}, {' '.join(map(str, pos))}, {LAYERS})")
    return macros, combos


def dtsi_text():
    macros, combos = macros_and_combos()
    head = ("/* Symbol chords, generated by draw/gen_symbols.py from its TABLE.\n"
            " * State order: plain, Shift, Cmd, Shift+Cmd, Alt, Shift+Alt, Ctrl, Shift+Ctrl;\n"
            " * the mod comes from the hand opposite the pair. Do not edit by hand. */\n\n")
    return head + "\n".join(macros) + "\n\n" + "\n".join(combos) + "\n"


def is_symbol_chord(combo):
    """A drawing combo the generator owns: one of its pairs plus only mods."""
    pos = set(combo.get("p") or [])
    for pair in TABLE:
        if set(pair) <= pos and pos - set(pair) <= set(LEFT_MODS.values()) | set(RIGHT_MODS.values()):
            return True
    return False


def drawing_text():
    text = DRAWING.read_text(encoding="utf-8")
    lines = text.split("\n")
    start = lines.index("combos:")
    data = yaml.safe_load(text)
    blocks, cur = [], None
    for ln in lines[start + 1:]:
        if ln.startswith("- p:"):
            if cur is not None:
                blocks.append(cur)
            cur = [ln]
        elif cur is not None:
            cur.append(ln)
    if cur is not None:
        blocks.append(cur)
    assert len(blocks) == len(data["combos"]), (len(blocks), len(data["combos"]))
    kept = [b for b, c in zip(blocks, data["combos"]) if not is_symbol_chord(c)]

    new = []
    for _pair, _state, pos, token in states_of():
        new.append(["- p:"] + [f"  - {p}" for p in pos]
                   + [f"  k: {yaml.safe_dump(token, default_style='\"', width=10**9).strip()}",
                      "  l:", "  - a1", "  - a2", "  type: symbol"])
    head = "\n".join(lines[:start + 1])
    body = "\n".join("\n".join(b).rstrip("\n") for b in kept)
    tail = "\n".join("\n".join(b) for b in new)
    return head + "\n" + body + "\n" + tail + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="do not write; fail if out of date")
    args = ap.parse_args()
    dtsi, drawing = dtsi_text(), drawing_text()
    stale = []
    if DTSI.read_text(encoding="utf-8") != dtsi:
        stale.append(DTSI)
    if DRAWING.read_text(encoding="utf-8") != drawing:
        stale.append(DRAWING)
    if args.check:
        for path in stale:
            print(f"out of date: {path}")
        return 1 if stale else 0
    for path, text in ((DTSI, dtsi), (DRAWING, drawing)):
        path.write_text(text, encoding="utf-8")
    states = states_of()
    print(f"{DTSI.name}: {len(states)} states; {DRAWING.name}: symbol chords replaced")
    return 0


if __name__ == "__main__":
    sys.exit(main())
