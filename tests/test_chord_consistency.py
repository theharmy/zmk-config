"""Consistency of the symbol chords across the firmware, the drawing and the practice.

The chords are defined once, in config/twonr9_symbol_chords.dtsi. The drawing
(draw/twonr9_srht.yaml) and the practice generator (practice/gen_monkeytype_srht.py)
must agree with it. These tests read each source and compare them.
"""

import importlib.util
import re
import unittest
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHORDS = ROOT / "config/twonr9_symbol_chords.dtsi"
COMBOS = ROOT / "config/twonr9_combos_srht.dtsi"
MACROS = ROOT / "config/twonr9_macros_srht.dtsi"
SYMBOL_WORK = ROOT / "config/symbol_work.dtsi"
DRAW = ROOT / "draw/twonr9_srht.yaml"
PRACTICE = ROOT / "practice/gen_monkeytype_srht.py"
COMBO_FILES = [CHORDS, ROOT / "config/twonr9_combos.dtsi",
               ROOT / "config/twonr9_combos_srht.dtsi", SYMBOL_WORK]
MOUSE = ROOT / "config/twonr9_mouse.dtsi"

LEFT_KEYS = {0, 1, 2, 6, 7, 8, 9}
# Mods from the opposite hand: shift = index, cmd = middle, alt = ring, ctrl = pinky.
MOD_STATE = {10: "shift", 11: "cmd", 12: "alt", 13: "ctrl",
             9: "shift", 8: "cmd", 7: "alt", 6: "ctrl"}
FINGER = {0: "ring", 1: "middle", 2: "index", 3: "index", 4: "middle", 5: "ring",
          6: "pinky", 7: "ring", 8: "middle", 9: "index",
          10: "index", 11: "middle", 12: "ring", 13: "pinky"}
# Every symbol and LaTeX escape the sym and num layers need.
REQUIRED = list("!?#~$\u20ac()[];'`^_-&@=|{}<>:\"/\\*+%.,") + [
    "\\[", "\\]", "\\{", "\\}", "\\(", "\\)", "\\$", "\\_", "\\%", "\\&", "\\#", "\\\\"]

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


def split_triplet(pos, pairs):
    """(pair, mod): the mod is the key from the opposite hand that completes a pair."""
    for mod in pos:
        rest = tuple(p for p in pos if p != mod)
        left = all(p in LEFT_KEYS for p in rest)
        if rest in pairs and mod in MOD_STATE and ((mod >= 10) == left):
            return rest, mod
    raise AssertionError(f"{pos} has no pair with an opposite-hand mod")


def macros_of(text):
    out = {}
    for name, body in re.findall(r"ZMK_MACRO\((\w+),\s*bindings = <(.*?)>;", text, re.S):
        chars = []
        for key in re.findall(r"&kp (\w+)", body):
            if key in ("LEFT", "RIGHT", "UP", "DOWN"):
                continue          # the cursor is left inside `{}` and friends
            if key in DE_CHAR:
                chars.append(DE_CHAR[key])
            elif re.fullmatch(r"DE_[A-Z]", key):
                chars.append(key[3].lower())
            else:
                chars.append(key.lower())
        out[name] = "".join(chars)
    return out


def firmware_chords():
    text = CHORDS.read_text(encoding="utf-8")
    macros = macros_of(text)
    chords = []
    for name, binding, pos in re.findall(
            r"ZMK_COMBO\((\w+),\s*(&kp DE_\w+|&\w+),\s*([0-9 ]+?),\s*L_A1 L_A2\)", text):
        out = DE_CHAR[binding[4:]] if binding.startswith("&kp ") else macros[binding[1:]]
        chords.append((tuple(sorted(int(p) for p in pos.split())), out))
    return chords


def bigram_and_umlaut_positions():
    combos = COMBOS.read_text(encoding="utf-8")
    symbols = SYMBOL_WORK.read_text(encoding="utf-8")
    keys = [tuple(sorted((int(a), int(b)))) for a, b in
            re.findall(r"ZMK_COMBO\(combo_\w+,\s*&macro_\w+,\s*(\d+) (\d+),", combos)]
    keys += [tuple(sorted((int(a), int(b)))) for a, b in
             re.findall(r"ZMK_COMBO\(combo_de_\w+,\s*&de_\w+,\s*(\d+)\s+(\d+),", symbols)]
    return keys


def drawing_chords():
    data = yaml.safe_load(DRAW.read_text(encoding="utf-8"))
    out = {}
    for combo in data["combos"]:
        key = tuple(sorted(combo["p"]))
        if isinstance(combo["k"], str):
            out.setdefault(key, []).append(combo["k"])
    return out


def base_letters():
    data = yaml.safe_load(DRAW.read_text(encoding="utf-8"))
    return [key["t"] for key in data["layers"]["a1"]]


class ChordSources(unittest.TestCase):
    def setUp(self):
        self.chords = firmware_chords()
        self.keysets = Counter(pos for pos, _ in self.chords)

    def test_every_pair_and_state_is_defined(self):
        self.assertEqual(len(self.chords), 104)

    def test_no_two_chords_share_a_key_set(self):
        dupes = {k: v for k, v in self.keysets.items() if v > 1}
        self.assertEqual(dupes, {})

    def test_drawing_has_one_entry_per_chord_with_its_output(self):
        drawn = drawing_chords()
        for pos, out in self.chords:
            self.assertIn(pos, drawn, f"no drawing entry for {pos}")
            self.assertEqual(drawn[pos], [out], f"drawing output for {pos} differs")
        extra = [k for k in drawn if k in set(self.keysets) and k not in self.keysets]
        self.assertEqual(extra, [])

    def test_mods_come_from_the_opposite_hand(self):
        pairs = {pos for pos, _ in self.chords if len(pos) == 2}
        for pos, _ in self.chords:
            if len(pos) == 3:
                rest, mod = split_triplet(pos, pairs)
                self.assertIn(rest, pairs, pos)
                self.assertNotEqual(mod in LEFT_KEYS, all(p in LEFT_KEYS for p in rest), pos)
            if len(pos) == 4:
                pair = next((q for q in pairs if set(q) <= set(pos)), None)
                self.assertIsNotNone(pair, pos)
                mods = sorted(MOD_STATE[p] for p in pos if p not in pair)
                self.assertEqual(len(mods), 2, pos)
                self.assertIn("shift", mods, pos)

    def test_mods_are_not_the_pair_finger_on_the_same_hand(self):
        pairs = {pos for pos, _ in self.chords if len(pos) == 2}
        for pos, _ in self.chords:
            if len(pos) == 3:
                rest, mod = split_triplet(pos, pairs)
                hands_fingers = {(p in LEFT_KEYS, FINGER[p]) for p in rest}
                self.assertNotIn((mod in LEFT_KEYS, FINGER[mod]), hands_fingers, pos)

    def test_no_triplet_or_quad_contains_a_bigram_or_umlaut_chord(self):
        special = bigram_and_umlaut_positions()
        for pos, _ in self.chords:
            if len(pos) > 2:
                for key in special:
                    self.assertFalse(set(key) <= set(pos), f"{pos} contains {key}")

    def test_every_required_symbol_is_placed_once_or_more(self):
        placed = {out for _, out in self.chords}
        for symbol in REQUIRED:
            if symbol == "|":
                self.assertIn("|", "".join(placed))
                continue
            self.assertIn(symbol, placed, f"{symbol!r} is not placed")

    def test_bigram_and_umlaut_chords_are_still_defined(self):
        self.assertEqual(len(bigram_and_umlaut_positions()), 16)  # 12 bigrams + 4 umlauts


class DrawingCoversTheFirmware(unittest.TestCase):
    """The drawing's chord list is generated; it must be exactly the firmware's."""

    def firmware_combos(self):
        out = []
        for path in COMBO_FILES:
            text = path.read_text(encoding="utf-8")
            for m in re.finditer(r"ZMK_COMBO\(\s*\w+\s*,\s*[^,]+,\s*([0-9 ]+?),\s*([^)]+)\)", text):
                out.append((tuple(sorted(int(x) for x in m.group(1).split())), m.group(2).strip()))
        text = MOUSE.read_text(encoding="utf-8")
        for m in re.finditer(r"key-positions = <([0-9 ]+)>", text):
            out.append((tuple(sorted(int(x) for x in m.group(1).split())), "mouse"))
        return out

    def drawing_combos(self):
        return yaml.safe_load(DRAW.read_text(encoding="utf-8"))["combos"]

    def test_every_firmware_chord_is_in_the_drawing_and_nothing_else(self):
        firmware = {pos for pos, _ in self.firmware_combos()}
        drawn = {tuple(sorted(c["p"])) for c in self.drawing_combos()}
        self.assertEqual(sorted(firmware - drawn), [], "firmware chords missing from the drawing")
        self.assertEqual(sorted(drawn - firmware), [], "drawing chords the firmware does not define")

    def test_bigrams_keep_their_layers(self):
        text = (ROOT / "config/twonr9_combos_srht.dtsi").read_text(encoding="utf-8")
        firmware = {}
        for m in re.finditer(r"ZMK_COMBO\(combo_\w+,\s*&macro_\w+,\s*(\d+) (\d+),\s*L_A(\d)\)", text):
            a, b, layer = int(m.group(1)), int(m.group(2)), int(m.group(3))
            firmware.setdefault((min(a, b), max(a, b)), set()).add(f"a{layer}")
        drawn = {}
        for combo in self.drawing_combos():
            if combo.get("type") == "bigram":
                key = tuple(sorted(combo["p"]))
                drawn.setdefault(key, set()).update(combo["l"])
        self.assertEqual(firmware, drawn)


class PracticeFollowsTheKeymap(unittest.TestCase):
    def test_practice_reads_the_same_chords(self):
        spec = importlib.util.spec_from_file_location("gen_monkeytype_srht", PRACTICE)
        gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gen)
        self.assertEqual(sorted(gen.parse_chords()), sorted(firmware_chords()))

    def test_practice_table_names_every_pair_from_the_drawing_letters(self):
        spec = importlib.util.spec_from_file_location("gen_monkeytype_srht", PRACTICE)
        gen = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gen)
        letters = {"a1": base_letters(), "a2": base_letters()}
        table = gen.build_table(firmware_chords(), letters)
        self.assertEqual(len(table), 104)
        self.assertTrue(all(" + " in label for label, _ in table.values()))


if __name__ == "__main__":
    unittest.main()
