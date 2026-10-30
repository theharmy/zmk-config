#!/usr/bin/env python3
import sys
import subprocess
import shutil
import yaml
import re
import html
import json
from pathlib import Path

raw_code_map = {
    "KEYBOARD_COMMA_AND_LESS_THAN": ",",
    "KEYBOARD_PERIOD_AND_GREATER_THAN": ".",
    "KEYBOARD_SLASH_AND_QUESTION_MARK": "-",
    "KEYBOARD_NON_US_BACKSLASH_AND_PIPE": "<",
    "KEYBOARD_GRAVE_ACCENT_AND_TILDE": "^",
    "KEYBOARD_EQUAL_AND_PLUS": "`",
    "KEYBOARD_RIGHT_BRACKET_AND_RIGHT_BRACE": "+",
    "KEYBOARD_BACKSLASH_AND_PIPE": "#",
    "KEYBOARD_MINUS_AND_UNDERSCORE": "ß",
    "KEYBOARD_1_AND_EXCLAMATION": "1",
    "KEYBOARD_2_AND_AT": "2",
    "KEYBOARD_3_AND_HASH": "3",
    "KEYBOARD_4_AND_DOLLAR": "4",
    "KEYBOARD_5_AND_PERCENT": "5",
    "KEYBOARD_6_AND_CARET": "6",
    "KEYBOARD_7_AND_AMPERSAND": "7",
    "KEYBOARD_8_AND_ASTERISK": "8",
    "KEYBOARD_9_AND_LEFT_PARENTHESIS": "9",
    "KEYBOARD_0_AND_RIGHT_PARENTHESIS": "0",
    "KEYBOARD_A": "A", "KEYBOARD_B": "B", "KEYBOARD_C": "C", "KEYBOARD_D": "D",
    "KEYBOARD_E": "E", "KEYBOARD_F": "F", "KEYBOARD_G": "G", "KEYBOARD_H": "H",
    "KEYBOARD_I": "I", "KEYBOARD_J": "J", "KEYBOARD_K": "K", "KEYBOARD_L": "L",
    "KEYBOARD_M": "M", "KEYBOARD_N": "N", "KEYBOARD_O": "O", "KEYBOARD_P": "P",
    "KEYBOARD_Q": "Q", "KEYBOARD_R": "R", "KEYBOARD_S": "S", "KEYBOARD_T": "T",
    "KEYBOARD_U": "U", "KEYBOARD_V": "V", "KEYBOARD_W": "W", "KEYBOARD_X": "X",
    "KEYBOARD_Y": "Z", "KEYBOARD_Z": "Y", # German QWERTZ swap
}

sorted_raw_codes = sorted(raw_code_map.items(), key=lambda x: len(x[0]), reverse=True)

# ==============================================================================
# Keymap variants
#
# The TwoNr9 ships as two shields sharing one hardware definition:
#   config/twonr9.keymap       (shield twonr9_*)        -- default, no adaptive keys
#   config/twonr9_srht.keymap  (shield twonr9_srht_*)   -- optional backup, 9 adaptive keys
#
# Only the alpha grids, their bigram chords, and the adaptive-key engine differ;
# every other layer is shared. Each entry below mirrors its keymap file, so edit
# the two together.
# ==============================================================================
VARIANTS = {
    "bugwind": {
        "keymap": "twonr9.keymap",
        "title": "BUGWIND",
        # Bigram chords, positionally paired across the six column pairs.
        "a1_bigrams": ["RL", "KT", "MB", "YS", "EO", "UI"],
        "a2_bigrams": ["RW", "MT", "SCH", "GS", "OE", "IU"],
        # Adaptive-key engine: bugwind binds every letter directly, so there are
        # no swap rules, no dashed keycaps and no legend card.
        "adaptive": None,
        # German Eszett chord (S + Space, see symbol_work.dtsi) plus the
        # vowel + Space umlaut chords.
        "sz_chord": "S + Space",
        "sz_pos": "10 + 16",
        "combo_labels": {
            "diag_macro_slashslash": "//",
            "diag_macro_ellipsis": "...",
            "diag_macro_comment_open": "/*",
            "diag_macro_comment_close": "*/",
            "diag_macro_nullish": "??",
            "diag_macro_optional_chain": "?.",
            "diag_macro_le": "<=",
            "diag_macro_ge": ">=",
            "diag_macro_increment": "++",
            "diag_macro_decrement": "--",
            "diag_macro_arrow": "->",
            "diag_macro_fat_arrow": "=>",
            "diag_macro_add_assign": "+=",
            "diag_macro_sub_assign": "-=",
            "diag_macro_equal_equal": "==",
            "diag_macro_not_equal": "!=",
            "diag_macro_and_and": "&&",
            "diag_macro_or_or": "||",
            "diag_macro_scope": "::",
            "diag_macro_colon_equal": ":=",
            "diag_macro_equal": "=",
            "diag_macro_pipe": "|",
            "diag_macro_plus": "+",
            "diag_macro_at": "@",
        },
        # Position-bound chords whose nested mod-morphs/macros are not
        # meaningfully decoded by keymap-drawer. The main drawings use concise
        # normal/Shift labels; the dedicated overview shows all modifier states.
        "extra_combos": [
            {"p": [0, 6], "k": "( / )", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [3, 11], "k": ") / (", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [1, 7], "k": "[ / ]", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [5, 13], "k": "] / [", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [2, 8], "k": "{ / }", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [4, 12], "k": "} / {", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [1, 6], "k": "& / *", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [4, 13], "k": "$ / €", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [2, 7], "k": "~ / ^", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [3, 12], "k": "< / >", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [0, 8], "k": "! / ?", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [1, 9], "k": "_ / -", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [5, 11], "k": "; / '", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [4, 10], "k": "# / %", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [0, 9], "k": ": / \\\"", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [5, 10], "k": "/ / \\\\", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [6, 7], "k": "´ / `", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [10, 16], "k": "ß / ẞ", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [13, 16], "k": "ä / Ä", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [4, 16], "k": "ö / Ö", "l": ["a1", "a2"], "type": "symbol"},
            {"p": [5, 16], "k": "ü / Ü", "l": ["a1", "a2"], "type": "symbol"},
        ],
    },
    "srht": {
        "keymap": "twonr9_srht.keymap",
        "title": "SRHT",
        "a1_bigrams": ["RL", "HN", "DT", "CY", "EO", "UI"],
        "a2_bigrams": ["RM", "NB", "KT", "GY", "OE", "IU"],
        # zmk-adaptive-key letters by board and keypos, colored by trigger set:
        #   R-set (pink):  L H (a1, long-dash 5 3) + M V (a2, dotted 2 3)
        #   U-set (blue):  O    Q-set (red): U    N-set (aqua): B X
        #   key I serves both U and Q -> U-colored letter, interleaved U/Q dashes
        "adaptive": {
            "a1_keys": {
                0: ("ak-r", "ak-r"),   # L after R
                4: ("ak-u", "ak-u"),   # O after U
                5: ("ak-q", "ak-q"),   # U after Q
                8: ("ak-r", "ak-r"),   # H after R
                12: ("ak-i", "ak-u"),  # I after U and Q
            },
            "a2_keys": {
                0: ("ak-n", "ak-n"),   # X after N
                1: ("ak-n", "ak-n"),   # B after N
                2: ("ak-mv", "ak-r"),  # V after R
                7: ("ak-mv", "ak-r"),  # M after R
            },
            "rows": [
                ("after R", "#d3869b", "H &#8644; L  &#183;  M &#8644; V"),
                ("after U", "#83a598", "O &#8644; I"),
                ("after Q", "#fb4934", "I &#8644; U"),
                ("after N", "#8ec07c", "B &#8644; X"),
            ],
            "letters_line": "adaptive letters &#8212; a1: L H O I U  &#183;  a2: X B M V",
            # Cheatsheet prose describing the swaps.
            "swaps_line": "r hl, u oi, q iu, r mv, n bx swap letters on roll to eliminate SFBs",
        },
        "sz_chord": "S + R",
        "sz_pos": "6 + 7",
        "extra_combos": [],
        "combo_labels": {},
    },
}

# Which variant this run renders. `main()` sets it from argv[1] (default: all).
ACTIVE = None
_DIAGONAL_COMBOS = []

# The diagonal symbol chords (bugwind): positions on the 18-key grid plus
# their four modifier states -- plain, shift, ctrl, ctrl+shift. Mirrors the
# DIAG_SYMBOL assignments in config/symbol_work.dtsi. Shared by the dedicated
# mod-morph grid (build_mod_morph_overview) and the compact table on the
# symbol-layer reference (build_symbol_layer_overview).
DIAGONAL_CHORDS = [
    # 16 chords in four geometry families (mirrored across the split), ordered
    # like the layout: top-row letters left to right (L M D | Y O U), and
    # within each letter its home-row partners in home-row order
    # (N R T H | S E I A).
    # Inner-1: brackets (openers plain on the left, closers plain on the right).
    {"positions": [0, 6], "family": "inner1", "normal_shift": ("(", ")"), "ctrl": "==", "ctrl_shift": "!="},
    {"positions": [3, 11], "family": "inner1", "normal_shift": (")", "("), "ctrl": "<=", "ctrl_shift": ">="},
    {"positions": [1, 7], "family": "inner1", "normal_shift": ("[", "]"), "ctrl": "+=", "ctrl_shift": "-="},
    {"positions": [5, 13], "family": "inner1", "normal_shift": ("]", "["), "ctrl": "&=", "ctrl_shift": "|="},
    {"positions": [2, 8], "family": "inner1", "normal_shift": ("{", "}"), "ctrl": "<<=", "ctrl_shift": ">>="},
    {"positions": [4, 12], "family": "inner1", "normal_shift": ("}", "{"), "ctrl": "^=", "ctrl_shift": "*="},
    # Inner-2: bitwise / logic / arrows.
    {"positions": [1, 6], "family": "inner2", "normal_shift": ("&", "*"), "ctrl": "&&", "ctrl_shift": "||"},
    {"positions": [4, 13], "family": "inner2", "normal_shift": ("$", "€"), "ctrl": "??", "ctrl_shift": "?."},
    {"positions": [2, 7], "family": "inner2", "normal_shift": ("~", "^"), "ctrl": "->", "ctrl_shift": "=>"},
    {"positions": [3, 12], "family": "inner2", "normal_shift": ("<", ">"), "ctrl": "<<", "ctrl_shift": ">>"},
    # Outer-1: sentence, markdown, comments.
    {"positions": [0, 8], "family": "outer1", "normal_shift": ("!", "?"), "ctrl": "//", "ctrl_shift": "..."},
    {"positions": [1, 9], "family": "outer1", "normal_shift": ("_", "-"), "ctrl": "++", "ctrl_shift": "--"},
    {"positions": [5, 11], "family": "outer1", "normal_shift": (";", "'"), "ctrl": "/*", "ctrl_shift": "*/"},
    {"positions": [4, 10], "family": "outer1", "normal_shift": ("#", "%"), "ctrl": "=", "ctrl_shift": "|"},
    # Outer-2: the two remaining diagonals.
    {"positions": [0, 9], "family": "outer2", "normal_shift": (":", '"'), "ctrl": "::", "ctrl_shift": ":="},
    {"positions": [5, 10], "family": "outer2", "normal_shift": ("/", "\\"), "ctrl": "+", "ctrl_shift": "@"},
]

# Display order of the four geometry families in the mod-morph overview.
FAMILY_ORDER = [
    ("inner1", "Inner-1 (Brackets)"),
    ("inner2", "Inner-2 (Bitwise)"),
    ("outer1", "Outer-1 (Sentence)"),
    ("outer2", "Outer-2"),
]




def variant():
    """The variant table for the current render pass."""
    return VARIANTS[ACTIVE]


def all_bigrams(v):
    """Every bigram label of a variant, in a1-then-a2 order."""
    return v["a1_bigrams"] + v["a2_bigrams"]


def combined_bigram_map(v):
    """{column-pair positions: "a1 / a2"} -- derived so the grids can't drift."""
    return {
        pos: f"{a1} / {a2}"
        for pos, a1, a2 in zip(
            [(0, 7), (1, 8), (2, 9), (3, 10), (4, 11), (5, 12)],
            v["a1_bigrams"],
            v["a2_bigrams"],
        )
    }

def decode_hid_code(s):
    if not isinstance(s, str):
        return s
    
    s_clean = s.replace(" ", "_").upper()
    
    # 1. AltGr (RA) combinations
    if "RA(" in s_clean or "RA_" in s_clean or "RIGHT_ALT" in s_clean:
        if "KEYBOARD_E" in s_clean: return "€"
        if "KEYBOARD_Q" in s_clean: return "@"
        if "NON_US_BACKSLASH" in s_clean: return "|"
        if "MINUS_AND_UNDERSCORE" in s_clean: return "\\"
        if "8_AND_ASTERISK" in s_clean: return "["
        if "9_AND_LEFT_PARENTHESIS" in s_clean: return "]"
        if "7_AND_AMPERSAND" in s_clean: return "{"
        if "0_AND_RIGHT_PARENTHESIS" in s_clean: return "}"
        if "RIGHT_BRACKET" in s_clean: return "~"
        if "KEYBOARD_M" in s_clean: return "µ"
        if "2_AND_AT" in s_clean: return "²"
        if "3_AND_HASH" in s_clean: return "³"

    # 2. Shift (LS) combinations
    if "LS(" in s_clean or "LS_" in s_clean or "LEFT_SHIFT" in s_clean or "LSHIFT" in s_clean:
        if "NON_US_BACKSLASH" in s_clean: return ">"
        if "BACKSLASH_AND_PIPE" in s_clean: return "'"
        if "1_AND_EXCLAMATION" in s_clean: return "!"
        if "2_AND_AT" in s_clean: return '"'
        if "3_AND_HASH" in s_clean: return "§"
        if "4_AND_DOLLAR" in s_clean: return "$"
        if "5_AND_PERCENT" in s_clean: return "%"
        if "6_AND_CARET" in s_clean: return "&"
        if "7_AND_AMPERSAND" in s_clean: return "/"
        if "8_AND_ASTERISK" in s_clean: return "("
        if "9_AND_LEFT_PARENTHESIS" in s_clean: return ")"
        if "0_AND_RIGHT_PARENTHESIS" in s_clean: return "="
        if "SLASH_AND_QUESTION_MARK" in s_clean: return "_"
        if "RIGHT_BRACKET" in s_clean: return "*"
        if "PERIOD_AND_GREATER_THAN" in s_clean: return ":"
        if "COMMA_AND_LESS_THAN" in s_clean: return ";"
        if "MINUS_AND_UNDERSCORE" in s_clean: return "?"
        if "EQUAL_AND_PLUS" in s_clean: return "`"
        if "GRAVE_ACCENT" in s_clean: return "°"

    # 3. Plain unshifted keys
    if "NON_US_BACKSLASH" in s_clean: return "<"
    if "BACKSLASH_AND_PIPE" in s_clean: return "#"
    if "RIGHT_BRACKET_AND_RIGHT_BRACE" in s_clean: return "+"
    if "SLASH_AND_QUESTION_MARK" in s_clean: return "-"
    if "PERIOD_AND_GREATER_THAN" in s_clean: return "."
    if "COMMA_AND_LESS_THAN" in s_clean: return ","
    if "GRAVE_ACCENT" in s_clean: return "^"
    if "EQUAL_AND_PLUS" in s_clean: return "´"
    if "MINUS_AND_UNDERSCORE" in s_clean: return "ß"
    if "APOSTROPHE_AND_QUOTE" in s_clean: return "ä"
    if "SEMICOLON_AND_COLON" in s_clean: return "ö"
    if "LEFT_BRACKET_AND_LEFT_BRACE" in s_clean: return "ü"

    # Digits
    if "0_AND_RIGHT_PARENTHESIS" in s_clean: return "0"
    if "1_AND_EXCLAMATION" in s_clean: return "1"
    if "2_AND_AT" in s_clean: return "2"
    if "3_AND_HASH" in s_clean: return "3"
    if "4_AND_DOLLAR" in s_clean: return "4"
    if "5_AND_PERCENT" in s_clean: return "5"
    if "6_AND_CARET" in s_clean: return "6"
    if "7_AND_AMPERSAND" in s_clean: return "7"
    if "8_AND_ASTERISK" in s_clean: return "8"
    if "9_AND_LEFT_PARENTHESIS" in s_clean: return "9"

    # Direct letters
    for k, v in sorted_raw_codes:
        if k in s_clean:
            return v

    return s

hold_abbr_map = {
    "Shift": "⇧",
    "LEFT_SHIFT": "⇧",
    "LSHFT": "⇧",
    "Sft": "⇧",
    "Control": "⌃",
    "Ctrl": "⌃",
    "Ctl": "⌃",
    "LEFT_CONTROL": "⌃",
    "LCTRL": "⌃",
    "Alt": "⌥",
    "LEFT_ALT": "⌥",
    "LALT": "⌥",
    "RALT": "⌥",
    "RIGHT_ALT": "⌥",
    "RIGHT ALT": "⌥",
    "Gui": "⌘",
    "LEFT_GUI": "⌘",
    "LGUI": "⌘",
    "RGUI": "⌘",
    "RIGHT_GUI": "⌘",
    "RIGHT GUI": "⌘",
    "RSHFT": "⇧",
    "RIGHT_SHIFT": "⇧",
    "RIGHT SHIFT": "⇧",
    "RCTRL": "⌃",
    "RIGHT_CONTROL": "⌃",
    "RIGHT CONTROL": "⌃",
    "sym": "sym",
    "fn": "fn",
    "num": "num",
    "num_word": "num"
}

def decode_binding(s):
    if isinstance(s, dict):
        res = dict(s)
        if "t" in res:
            res["t"] = decode_binding(res["t"])
            if isinstance(res["t"], dict):
                inner = res.pop("t")
                res.update(inner)
        if "s" in res:
            res["s"] = decode_hid_code(res["s"])
            if res["s"] in ["&dot_spc", "dot_spc"]:
                del res["s"]
        if "h" in res:
            res["h"] = hold_abbr_map.get(res["h"], res["h"])
            if res["h"] == "sticky":
                del res["h"]
        return res

    if not isinstance(s, str):
        return s

    if s in ["A2_DUAL", "&lt_a2"]:
        return {"t": "a2", "h": "a2"}
    if s in ["SPC_NAV", "&lt_spc", "&spc_morph", "SPC_SFT"]:
        return {"t": "Spc", "h": "nav"}
    if s in ["MAGIC_SHIFT", "&magic_shift", "&shift_repeat", "shift_repeat"]:
        return {"t": "⇧", "h": "Repeat", "s": "⇪"}
    if s in ["&smart_num", "SMART_NUM", "&num_dance"]:
        return {"t": "Num", "h": "num"}

    # Mod-Morph Symbol Pairs
    if s in ["&excl_qmark", "excl_qmark"]:
        return {"t": "!", "s": "?"}
    if s in ["&hash_tilde", "hash_tilde"]:
        return {"t": "#", "s": "~"}
    if s in ["&dllr_euro", "dllr_euro"]:
        return {"t": "$", "s": "€"}
    if s in ["&grave_caret", "grave_caret"]:
        return {"t": "`", "s": "^"}
    if s in ["&under_minus", "under_minus"]:
        return {"t": "_", "s": "-"}
    if s in ["&amps_at", "amps_at"]:
        return {"t": "&", "s": "@"}
    if s in ["&pipe_equal", "pipe_equal"]:
        return {"t": "|", "s": "="}
    if s in ["&lpar_lt", "lpar_lt"]:
        return {"t": "(", "s": "<"}
    if s in ["&rpar_gt", "rpar_gt"]:
        return {"t": ")", "s": ">"}
    if s in ["&colon_dqt", "colon_dqt"]:
        return {"t": ":", "s": '"'}
    if s in ["&lbkt_lbrc", "lbkt_lbrc"]:
        return {"t": "[", "s": "{"}
    if s in ["&rbkt_rbrc", "rbkt_rbrc"]:
        return {"t": "]", "s": "}"}
    if s in ["&semi_sqt", "semi_sqt"]:
        return {"t": ";", "s": "'"}
    if s in ["&fslh_bslh", "fslh_bslh"]:
        return {"t": "/", "s": "\\"}

    if s in ["&bs_del", "bs_del"]:
        return {"t": "⌫", "s": "⌦"}
    if s in ["&swapper", "swapper"]:
        return "⇹"
    if s in ["&caps_word", "caps_word"]:
        return "⇪"

    # Clustered Nav & Niri Bindings
    if "mt_home" in s or "NAV_LEFT" in s:
        return {"t": "←", "h": "Hm"}
    if "mt_end" in s or "NAV_RIGHT" in s:
        return {"t": "→", "h": "End"}
    if "mt_up" in s or "NAV_UP" in s:
        return {"t": "↑", "h": "D-Top"}
    if "mt_down" in s or "NAV_DOWN" in s:
        return {"t": "↓", "h": "D-End"}
    if "NAV_PGDN" in s or "LG(PG_DN)" in s and "PG_DN" in s:
        return {"t": "⇟", "h": "⌘⇟"}
    if "NAV_PGUP" in s or "LG(PG_UP)" in s and "PG_UP" in s:
        return {"t": "⇞", "h": "⌘⇞"}
    if "mt_bspc" in s or "NAV_BSPC" in s:
        return {"t": "⌫", "h": "W-Del"}
    if "niri_adjust" in s:
        return {"t": "⌘R", "s": "⌘⌃C"}
    if "dot_comma" in s:
        return {"t": ".", "s": ","}
    if "LG(DE_Q)" in s or "LG(Q)" in s or "KEYBOARD_Q" in s and "LG" in s:
        return "⌘Q"
    if "LG(TAB)" in s or "KEYBOARD_TAB" in s and "LG" in s:
        return "⌘⇥"

    # Hold-taps: &hml / &hmr / &hml_* / &hmr_*
    m = re.search(r"&(?:hml|hmr)(?:_[a-z])?\s+([A-Z_]+)\s+(.+)", s)
    if m:
        mod_raw, key_part = m.group(1), m.group(2)
        if "ALT" in mod_raw:
            mod_label = "⌥"
        elif "GUI" in mod_raw:
            mod_label = "⌘"
        elif "SHFT" in mod_raw or "SHIFT" in mod_raw:
            mod_label = "⇧"
        else:
            mod_label = "⌃"
        return {"t": decode_hid_code(key_part), "h": mod_label}

    # Layer-taps: legacy named nodes (&lt_r4 / &lt_h / &lt_i / &lt_v) and the
    # current plain &lt override. The `keymap` CLI resolves the layer argument
    # to its numeric index, so accept both "L_NAV" and "2".
    m = re.search(r"&(lt_r4|lt_[hinv]|lt)\s+(L_[A-Z]+|\d+)\s+(.+)", s)
    if m:
        node, layer, key_part = m.group(1), m.group(2), m.group(3)
        if node == "lt_h":
            layer_label = "nav"
        elif node in ("lt_i", "lt_v"):
            layer_label = "fn"
        elif node == "lt_r4":
            layer_label = "sym"
        else:
            layer_label = {
                "L_A1": "a1", "L_A2": "a2", "L_NAV": "nav",
                "L_SYM": "sym", "L_FN": "fn", "L_NUM": "num",
                "0": "a1", "1": "a2", "2": "nav", "3": "sym",
                "4": "fn", "5": "num",
            }.get(layer, "sym")
        return {"t": decode_hid_code(key_part), "h": layer_label}

    # Adaptive keys: &ak_l, &ak_h, etc.
    if s.startswith("&ak_") or ("ak_" in s and not "adaptive" in s):
        parts = s.split("ak_")
        if len(parts) > 1:
            letter = parts[-1].strip()[0].upper()
            return letter

    # If it contains HID USAGE
    if "HID_USAGE" in s.upper() or "ZMK_HID" in s.upper() or "ZMK HID" in s:
        return decode_hid_code(s)

    return s

def combo_symbol(s):
    """Resolve ``&macro_<bigram>`` bindings to their two/three-letter label.

    Derived from the active variant's bigram lists, so a chord whose macro
    name follows the ``&macro_XX`` convention always matches -- whether it is
    one of the plain two-letter ones or something like ``&macro_sch``.
    """
    if ACTIVE is None or not isinstance(s, str) or not s.startswith("&macro_"):
        return None
    suffix = s[len("&macro_"):]
    for b in all_bigrams(variant()):
        if suffix == b.lower():
            return b
    return variant().get("combo_labels", {}).get(suffix)


# Variant-independent symbol substitutions (macros are handled by combo_symbol).
combo_symbol_map = {
    "&studio_unlock": "🔓",
    "&caps_word": "⇪",
    "&swapper": "⇹",
    "&bs_del": "⌫ / ⌦",
    "bs_del": "⌫ / ⌦",
    "RETURN": "⏎",
    "Enter": "⏎",
    "TAB": "⇥",
    "Tab": "⇥",
    "BSPC": "⌫",
    "Bspc": "⌫",
    "DEL": "⌦",
    "Del": "⌦",
    "ESC": "⎋",
    "Esc": "⎋",
    "Ctl+Bspc": "⌃⌫",
    "Ctl+⌫": "⌃⌫",
    "LC(BSPC)": "⌃⌫",
    "Shift": "⇧",
    "Sft": "⇧",
    "LEFT_SHIFT": "⇧",
    "&sl L_SYM": "sym",
    "&macro_shift_sym": "sym+⇧",
}

def decode_combo_key(s):
    if isinstance(s, dict):
        res = dict(s)
        if "t" in res:
            res["t"] = decode_combo_key(res["t"])
        if "s" in res:
            res["s"] = decode_combo_key(res["s"])
        return res
    if not isinstance(s, str):
        return s
    if s in combo_symbol_map:
        return combo_symbol_map[s]
    macro = combo_symbol(s)
    if macro is not None:
        return macro
    decoded = decode_hid_code(s)
    if decoded in combo_symbol_map:
        return combo_symbol_map[decoded]
    return decoded

def classify_combo_type(c):
    k = c.get("k")
    layers = c.get("l", [])
    bigrams = all_bigrams(variant())

    if c.get("type"):
        return c["type"]
    
    # 1. Bigrams (combined labels look like "RL / RM")
    if isinstance(k, str) and (k in bigrams or ("/" in k and " · Ctrl:" not in k)):
        return "bigram"
    if isinstance(k, dict) and "t" in k and "/" in str(k.get("t")):
        return "bigram"

    # 2. Number Combos (7, 8, 9 or unique to num layer) -> Orange
    if isinstance(k, str) and k in ["7", "8", "9"]:
        return "num"
    if len(layers) == 1 and "num" in str(layers[0]).lower():
        return "num"

    # 3. Check if combo is unique to a single sublayer
    if len(layers) == 1:
        l0 = str(layers[0]).lower()
        if "sym" in l0: return "sym"
        if "nav" in l0: return "nav"
        if "fn" in l0: return "fn"
        if "a2" in l0: return "a2"
        if "a1" in l0: return "a1"

    # 4. Multi-layer combos categorized by type
    if isinstance(k, dict):
        k = k.get("t")
    if isinstance(k, str):
        if k in ["{", "}", "[", "]", "(", ")", "?", "<", ">", "/", "\\", "-", ";", ":", "_", "ß"]:
            return "symbol"
        if k in ["⇥", "⏎", "⌫", "⌃⌫", "⎋", "⇧", "Tab", "Enter", "Bspc", "Ctl+Bspc", "Esc", "Shift", "Sft", "NWin", "⇹"]:
            return "util"
        if k in ["🔓", "⇪", "Unlock", "Boot", "Reset", "Caps Word"]:
            return "system"
    return "util"

def apply_combo_alignment(combos):
    # Keep bigrams on their established alignment. Spread every other chord,
    # including two-key combos, away from the key centers for readability.
    for c in combos:
        p = set(c.get("p", []))
        c_type = classify_combo_type(c)
        c["type"] = c_type

        if c_type == "bigram":
            c.setdefault("align", "mid")
            c.setdefault("offset", 0.0)
            continue
        
        if c.get("k") == "⌫ / ⌦":
            c["width"] = 46.0

        if len(p) > 2:
            c["align"] = "top" if max(p) <= 5 else "bottom" if min(p) >= 6 else "mid"
            c["offset"] = 0.18
        else:
            c["align"] = "mid"
            c["offset"] = 0.16

def extract_label(key):
    if isinstance(key, dict):
        if key.get("type") in ["trans", "held"]:
            return None
        lbl = key.get("t")
    elif isinstance(key, str):
        if key in ["___", "", "None", "&trans", "&none"]:
            return None
        lbl = key
    else:
        return None

    if lbl in ["VOL DN", "Vol-", "&kp C_VOL_DN", "C_VOL_DN"]: return "V-"
    if lbl in ["VOL UP", "Vol+", "&kp C_VOL_UP", "C_VOL_UP"]: return "V+"
    if lbl in ["PgUp", "PG_UP", "PgU", "⇞"]: return "⇞"
    if lbl in ["PgDn", "PG_DN", "PgD", "⇟"]: return "⇟"
    if lbl in ["Home", "HOME", "Hm", "↖"]: return "↖"
    if lbl in ["End", "END", "↘"]: return "↘"
    if lbl in ["Alt", "LALT", "LEFT_ALT", "⌥"]: return "⌥"
    if lbl in ["Gui", "LGUI", "LEFT_GUI", "⌘"]: return "⌘"
    if lbl in ["Shift", "Sft", "LSHFT", "LEFT_SHIFT", "⇧"]: return "⇧"
    if lbl in ["Ctrl", "Ctl", "LCTRL", "LEFT_CONTROL", "⌃"]: return "⌃"
    if lbl in ["niri_adjust", "&niri_adjust"]: return "⌘R"
    if lbl in ["dot_comma", "&dot_comma"]: return ". ,"
    return lbl

def extract_sym_label(key):
    if isinstance(key, dict):
        if key.get("type") in ["trans", "held"]:
            return None
        t = key.get("t")
        s = key.get("s")
        if t and s:
            return f"{t} {s}"
        return t
    return extract_label(key)

def build_overview_layer(layers, base_layer_name="a1"):
    base_l = layers.get(base_layer_name, [])
    nav_l  = layers.get("nav", [])
    sym_l  = layers.get("sym", [])
    num_l  = layers.get("num", [])
    fn_l   = layers.get("fn", [])

    overview = []
    for i in range(len(base_l)):
        b = base_l[i]
        base_item = dict(b) if isinstance(b, dict) else {"t": b}
        
        # Only add 4-corner legends for finger keys (0..13)
        if i < 14:
            # Corner 1: Top-Right (Nav -> Yellow)
            nav_lbl = extract_label(nav_l[i]) if i < len(nav_l) else None
            if nav_lbl and nav_lbl != base_item.get("t"):
                base_item["tr"] = nav_lbl

            # Corner 2: Top-Left (Sym -> Cyan)
            sym_lbl = extract_sym_label(sym_l[i]) if i < len(sym_l) else None
            if sym_lbl and sym_lbl != base_item.get("t"):
                base_item["tl"] = sym_lbl

            # Corner 3: Bottom-Left (Num -> Orange)
            num_lbl = extract_label(num_l[i]) if i < len(num_l) else None
            if num_lbl and num_lbl != base_item.get("t"):
                base_item["bl"] = num_lbl

            # Corner 4: Bottom-Right (Fn -> Green)
            fn_lbl = extract_label(fn_l[i]) if i < len(fn_l) else None
            if fn_lbl and fn_lbl != base_item.get("t"):
                base_item["br"] = fn_lbl

        overview.append(base_item)
    return overview

def build_symbol_overview_layer(layers):
    """Render the actual symbol-layer outputs, including shift morphs and thumbs."""
    return [dict(key) if isinstance(key, dict) else {"t": key} for key in layers.get("sym", [])]

def build_combined_alpha_layer(layers, corners=True):
    """Combine the a1/a2 grids into one board ("t1 / t2" per finger key).

    With corners=True the 4-corner sub-layer legends (nav/sym/num/fn) are
    added like in the combined overview; without them the board shows only
    the dual alpha, its hold label and the thumbs -- used by the symbol
    layer reference, where the corners would be noise.
    """
    a1_l = layers.get("a1", [])
    a2_l = layers.get("a2", [])
    nav_l  = layers.get("nav", [])
    sym_l  = layers.get("sym", [])
    num_l  = layers.get("num", [])
    fn_l   = layers.get("fn", [])

    combined = []
    for i in range(len(a1_l)):
        b1 = a1_l[i]
        b2 = a2_l[i] if i < len(a2_l) else {}

        t1 = b1.get("t") if isinstance(b1, dict) else b1
        t2 = b2.get("t") if isinstance(b2, dict) else b2

        # For fingers (0..13): format as "t1 / t2"
        if i < 14 and t1 and t2:
            item = {"t": f"{t1} / {t2}"}
        else:
            item = dict(b1) if isinstance(b1, dict) else {"t": b1}

        # Add hold function abbreviation
        h_lbl = b1.get("h") if isinstance(b1, dict) else None
        if h_lbl:
            item["h"] = hold_abbr_map.get(h_lbl, h_lbl)

        # Only add 4-corner legends for finger keys (0..13)
        if corners and i < 14:
            # Corner 1: Top-Right (Nav -> Yellow)
            nav_lbl = extract_label(nav_l[i]) if i < len(nav_l) else None
            if nav_lbl and nav_lbl != t1:
                item["tr"] = nav_lbl

            # Corner 2: Top-Left (Sym -> Cyan)
            sym_lbl = extract_sym_label(sym_l[i]) if i < len(sym_l) else None
            if sym_lbl and sym_lbl != t1:
                item["tl"] = sym_lbl

            # Corner 3: Bottom-Left (Num -> Orange)
            num_lbl = extract_label(num_l[i]) if i < len(num_l) else None
            if num_lbl and num_lbl != t1:
                item["bl"] = num_lbl

            # Corner 4: Bottom-Right (Fn -> Green)
            fn_lbl = extract_label(fn_l[i]) if i < len(fn_l) else None
            if fn_lbl and fn_lbl != t1:
                item["br"] = fn_lbl

        combined.append(item)
    return combined

def post_process_svg_colors(svg_path):
    with open(svg_path) as f:
        svg = f.read()

    # 1. Colorize 4-Corner Legends directly
    svg = re.sub(r'(<text[^>]*class="[^"]*\btl\b[^"]*")', r'\1 style="fill: #458588 !important; font-weight: 700;"', svg)
    svg = re.sub(r'(<text[^>]*class="[^"]*\btr\b[^"]*")', r'\1 style="fill: #d79921 !important; font-weight: 700;"', svg)
    svg = re.sub(r'(<text[^>]*class="[^"]*\bbl\b[^"]*")', r'\1 style="fill: #d65d0e !important; font-weight: 700;"', svg)
    svg = re.sub(r'(<text[^>]*class="[^"]*\bbr\b[^"]*")', r'\1 style="fill: #689d6a !important; font-weight: 700;"', svg)

    # 2. Colorize hold / bottom labels based on their layer target or modifier
    svg = re.sub(
        r'(<text[^>]*class="[^"]*hold[^"]*"[^>]*>)\s*sym\s*(</text>)',
        r'\1<tspan class="hold-sym">sym</tspan>\2',
        svg
    )
    svg = re.sub(
        r'(<text[^>]*class="[^"]*hold[^"]*"[^>]*>)\s*(?:sym2|fn)\s*(</text>)',
        r'\1<tspan class="hold-fn">fn</tspan>\2',
        svg
    )
    svg = re.sub(
        r'(<text[^>]*class="[^"]*hold[^"]*"[^>]*>)\s*(?:num|num_word)\s*(</text>)',
        r'\1<tspan class="hold-num">num</tspan>\2',
        svg
    )
    svg = re.sub(
        r'(<text[^>]*class="[^"]*hold[^"]*"[^>]*>)\s*nav\s*(</text>)',
        r'\1<tspan class="hold-nav">nav</tspan>\2',
        svg
    )
    svg = re.sub(
        r'(<text[^>]*class="[^"]*hold[^"]*"[^>]*>)\s*(⌥|⌘|⇧|⌃|Repeat|Alt|Gui|Sft|Ctl)\s*(</text>)',
        r'\1<tspan class="hold-mod">\2</tspan>\3',
        svg
    )

    # 3. Style horizontal dual tap text on the same baseline (class-based, theme responsive)
    svg = re.sub(
        r'<text([^>]*)>\s*<tspan[^>]*>([A-Za-z0-9,\.\+\-\*\/])</tspan>\s*<tspan[^>]*>/</tspan>\s*<tspan[^>]*>([A-Za-z0-9,\.\+\-\*\/])</tspan>\s*</text>',
        r'<text\1><tspan class="a1-tap">\2</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-tap">\3</tspan></text>',
        svg
    )

    svg = re.sub(
        r'(<text[^>]*class="[^"]*tap[^"]*"[^>]*>)([A-Za-z0-9,\.\+\-\*\/])(\s*/\s*)([A-Za-z0-9,\.\+\-\*\/])(</text>)',
        r'\1<tspan class="a1-tap">\2</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-tap">\4</tspan>\5',
        svg
    )

    # 4. Style bigram dual text on the same horizontal baseline: RL / RM
    v = variant()
    for (b1, b2) in zip(v["a1_bigrams"], v["a2_bigrams"]):
        svg = re.sub(
            rf'<text([^>]*)>\s*<tspan[^>]*>{b1}</tspan><tspan[^>]*>[^<]*</tspan>\s*</text>',
            rf'<text\1><tspan class="a1-bigram">{b1}</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-bigram">{b2}</tspan></text>',
            svg
        )
        svg = re.sub(
            rf'(<text[^>]*class="[^"]*combo[^"]*"[^>]*>){b1}\s*/\s*{b2}(</text>)',
            rf'\1<tspan class="a1-bigram">{b1}</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-bigram">{b2}</tspan>\2',
            svg
        )

    # 5. Style ⌫ / ⌦ combo text
    svg = re.sub(
        r'(<text[^>]*class="[^"]*combo[^"]*"[^>]*>)\s*⌫\s*/\s*⌦\s*(</text>)',
        r'\1<tspan class="a1-tap">⌫</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-tap">⌦</tspan>\2',
        svg
    )

    with open(svg_path, "w") as f:
        f.write(svg)

def add_adaptive_overview(svg_path):
    # Decorates the overview with the adaptive-key engine: dashed keycaps on the
    # letters that swap, plus a legend card. Variants without adaptive keys
    # (bugwind) pass through untouched -- there is nothing to mark.
    ak = variant().get("adaptive")
    if not ak:
        return
    a1_keys = ak["a1_keys"]
    a2_keys = ak["a2_keys"]

    with open(svg_path) as f:
        svg = f.read()

    # Segment by layer group: keypos indices are only unique per board, and
    # a2's thumb key uses class "key held keypos-15" (shifting global order).
    def layer_start(marker):
        i = svg.index(marker)
        return svg.rindex("<g ", 0, i)

    a1_start = layer_start('class="layer-a1 (Base)"')
    a2_start = layer_start('class="layer-a2 (Alphas 2)"')
    sym_start = layer_start('class="layer-Symbols')

    key_re = re.compile(
        r'(<g transform="[^"]*" class="[^"]*keypos-(\d+)">)(.*?)(</g>)', re.S
    )

    def mark_segment(segment, keys):
        def mark(m):
            pos = int(m.group(2))
            if pos not in keys:
                return m.group(0)
            rect_cls, text_cls = keys[pos]
            body = m.group(3)
            # Dashed accent outline on the keycap (class-driven so the
            # colors resolve from the stylesheet's CSS variables)
            def rect_sub(rm):
                full = rm.group(0)
                if rect_cls == "ak-i":
                    # twin rects: U-colored dashes interleaved with Q-colored
                    # ones (stroke-dashoffset shifts the pattern by one dash)
                    t1 = re.sub(r'class="([^"]*)"',
                                lambda c: 'class="{} ak-i1"'.format(c.group(1)),
                                full, count=1)
                    t2 = re.sub(r'class="([^"]*)"',
                                lambda c: 'class="{} ak-i2"'.format(c.group(1)),
                                full, count=1)
                    return t1 + t2
                return re.sub(r'class="([^"]*)"',
                              lambda c: 'class="{} {}"'.format(c.group(1), rect_cls),
                              full, count=1)

            body = re.sub(r'<rect[^>]*class="key[^"]*"[^>]*?/>', rect_sub,
                          body, count=1)
            # Accent tap letter
            body = re.sub(
                r'(<text[^>]*class=")([^"]*)("[^>]*?)(>)',
                r'\1\2 ' + text_cls + r'\3\4',
                body,
                count=1,
            )
            return m.group(1) + body + m.group(4)

        return key_re.sub(mark, segment)

    svg = (
        svg[:a1_start]
        + mark_segment(svg[a1_start:a2_start], a1_keys)
        + mark_segment(svg[a2_start:sym_start], a2_keys)
        + svg[sym_start:]
    )

    # Extend canvas by 150px and shift the layers below a1 down by the same
    # amount, opening a slot for the legend card right after the first keymap
    svg = re.sub(
        r'width="(\d+)" height="(\d+)" viewBox="0 0 (\d+) (\d+)"',
        lambda m: 'width="{}" height="{}" viewBox="0 0 {} {}"'.format(
            m.group(1),
            int(m.group(2)) + 150,
            m.group(3),
            int(m.group(4)) + 150,
        ),
        svg,
        count=1,
    )

    for marker in ('class="layer-a2 (Alphas 2)"', 'class="layer-Symbols'):
        i = svg.index(marker)
        gs = svg.rindex("<g ", 0, i)
        ge = svg.index(">", gs)
        svg = (
            svg[:gs]
            + re.sub(
                r"(translate\([^,]+,\s*)(-?\d+)(\))",
                lambda m: m.group(1) + str(int(m.group(2)) + 150) + m.group(3),
                svg[gs:ge],
                count=1,
            )
            + svg[ge:]
        )

    svg = re.sub(
        r'(<text[^>]*\by=")(\d+(?:\.\d+)?)("[^>]*class="footer")',
        lambda m: m.group(1) + "{:.1f}".format(float(m.group(2)) + 150) + m.group(3),
        svg,
        count=1,
    )

    ak_body = 'text-anchor: start; font-size: 13px;'
    # Layout: first row spans the card alone, the rest sit side by side.
    # Trigger/letter colors come from the stylesheet's ak-tr-*/ak-lt-* classes;
    # the suffix is the trigger letter (e.g. "after R" -> r).
    def legend_row(x, y, trigger, letters):
        sfx = trigger.split()[-1].lower()
        return (
            f'    <text x="{x}" y="{y}" class="ak-body" style="{ak_body}">'
            f'<tspan class="ak-tr-{sfx}">{trigger}</tspan>'
            f'<tspan>&#160;&#8594;&#160;</tspan>'
            f'<tspan class="ak-lt-{sfx}">{letters}</tspan></text>'
        )

    rows = ak["rows"]  # (trigger, color, letters); color lives in the CSS class
    legend_rows = [legend_row(24, 62, rows[0][0], rows[0][2])]
    legend_rows += [
        legend_row(24 + i * 240, 92, row[0], row[2]) for i, row in enumerate(rows[1:])
    ]
    legend = f'''
  <!-- ADAPTIVE KEYS LEGEND -->
  <g transform="translate(10, 352)">
    <rect x="0" y="0" width="754" height="130" rx="8" class="ak-card"/>
    <text x="24" y="30" class="ak-title" style="text-anchor: start; font-size: 14px; font-weight: bold; letter-spacing: 0.5px;">ADAPTIVE KEYS &#8635;</text>
    <text x="230" y="30" class="ak-body" style="text-anchor: start; font-size: 11.5px; opacity: 0.85;">dashed keys swap partners within 300 ms of the trigger letter</text>

{chr(10).join(legend_rows)}

    <text x="24" y="118" class="ak-body" style="text-anchor: start; font-size: 12px; opacity: 0.85;">{ak["letters_line"]}</text>
  </g>
'''

    # Place the legend immediately before the (shifted) second keymap
    i = svg.index('class="layer-a2 (Alphas 2)"')
    a2_start = svg.rindex("<g ", 0, i)
    svg = svg[:a2_start] + legend + "\n  " + svg[a2_start:]
    with open(svg_path, "w") as f:
        f.write(svg)


def _chord_row_order(chord, key_labels, a1_order):
    """(top-row key, home-row key) as grid indices: top first, then bottom,
    both most-to-the-left (within a row, grid index == left-to-right order)."""
    ordered = sorted(
        chord["positions"],
        key=lambda position: a1_order.get(key_labels[position], position),
    )
    return ordered[0], ordered[1]


def build_mod_morph_overview(draw_dir, config_dir, cfg_overview_path, source_data):
    """Render the diagonal symbol chords as four family tables.

    One table per geometry family (FAMILY_ORDER), each chord a row showing
    all four modifier states: a Symbol-Pair band over Plain/Shift and a
    Programming-Operator-Pair band over Ctrl/Ctrl+Shift. Within a family the
    rows are ordered by top-row key, then home-row key, both left to right.
    """
    if ACTIVE != "bugwind":
        return None

    overview_svg = draw_dir / "twonr9_mod_morph_overview.svg"
    overview_yaml = draw_dir / "twonr9_mod_morph_overview.yaml"
    key_labels = [extract_label(key) for key in source_data.get("layers", {}).get("a1", [])]
    key_labels.extend(str(index) for index in range(len(key_labels), 18))
    a1_order = {label: index for index, label in enumerate(key_labels)}

    def state_text(value):
        return " / ".join(value) if isinstance(value, tuple) else value

    families = []
    for fam_key, fam_title in FAMILY_ORDER:
        chords = sorted(
            (c for c in DIAGONAL_CHORDS if c["family"] == fam_key),
            key=lambda c: _chord_row_order(c, key_labels, a1_order),
        )
        rows = [
            (
                f"{key_labels[top]} + {key_labels[home]}",
                state_text(chord["normal_shift"][0]),
                state_text(chord["normal_shift"][1]),
                state_text(chord["ctrl"]),
                state_text(chord["ctrl_shift"]),
            )
            for chord in chords
            for top, home in [_chord_row_order(chord, key_labels, a1_order)]
        ]
        families.append((fam_title, chords, rows))

    # Table geometry
    margin = 42
    chord_col_x = 24
    col_cx = [chord_col_x + 80, 260, 400, 540, 680]  # chord, plain, shift, ctrl, ctrl+shift
    mid = (col_cx[2] + col_cx[3]) // 2                    # between shift and ctrl
    symbol_band = (col_cx[1] - 80, mid)                   # spans plain + shift
    operator_band = (mid, col_cx[4] + 80)                 # spans ctrl + ctrl+shift
    table_w = 764
    row_h = 34
    title_h = 34
    section_gap = 28
    # Table body: band (24) + header gap (40) + rows + bottom padding.
    body_h = lambda nrows: 40 + nrows * row_h + 8
    width = margin * 2 + table_w
    height = margin * 2 + sum(title_h + body_h(len(rows)) for _, _, rows in families) \
        + (len(families) - 1) * section_gap

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<style>svg { font-family:Calibri,system-ui,sans-serif; }',
        '.title { fill:#fbf1c7; font-size:22px; font-weight:700; }',
        '.fam { fill:#ebdbb2; font-size:16px; font-weight:700; letter-spacing:0.5px; }',
        '.band { fill:#fbf1c7; font-size:12px; font-weight:700; letter-spacing:1px; }',
        '.hdr { fill:#a89984; font-size:11px; font-weight:700; }',
        '.card { fill:#ebdbb2; stroke:#d5c4a1; stroke-width:1; }',
        '.out { fill:#282828; font-size:18px; font-weight:700; text-anchor:middle; dominant-baseline:middle; }',
        '.pos { fill:#282828; font-size:14px; font-weight:700; text-anchor:start; dominant-baseline:middle; }',
        '.sepline { stroke:#a89984; stroke-width:1; }</style>',
        '<rect width="100%" height="100%" fill="#7c6f64"/>',
    ]
    y = margin
    for fam_title, chords, rows in families:
        parts.append(f'<text x="{margin}" y="{y + 24}" class="fam">{html.escape(fam_title)}</text>')
        band_y = y + title_h + 2
        parts.append(f'<rect x="{margin + symbol_band[0]}" y="{band_y}" width="{symbol_band[1] - symbol_band[0]}" height="24" rx="4" fill="#665c54" stroke="#a89984" stroke-width="1"/>')
        parts.append(f'<text x="{(margin + symbol_band[0] + margin + symbol_band[1]) / 2}" y="{band_y + 12}" class="band" style="text-anchor:middle; dominant-baseline:middle;">SYMBOL-PAIR</text>')
        parts.append(f'<rect x="{margin + operator_band[0]}" y="{band_y}" width="{operator_band[1] - operator_band[0]}" height="24" rx="4" fill="#665c54" stroke="#a89984" stroke-width="1"/>')
        parts.append(f'<text x="{(margin + operator_band[0] + margin + operator_band[1]) / 2}" y="{band_y + 12}" class="band" style="text-anchor:middle; dominant-baseline:middle;">PROGRAMMING-OPERATOR PAIR</text>')
        hdr_y = band_y + 40
        for x, t in zip(col_cx, ["CHORD", "PLAIN", "SHIFT", "CTRL", "CTRL+SHIFT"]):
            anchor = 'start' if t == "CHORD" else 'middle'
            parts.append(f'<text x="{margin + x}" y="{hdr_y}" class="hdr" style="text-anchor:{anchor};">{t}</text>')
        parts.append(f'<line x1="{margin + 130}" y1="{band_y - 6}" x2="{margin + 130}" y2="{hdr_y + 4}" class="sepline"/>')
        row_y0 = hdr_y + 14
        for i, row in enumerate(rows):
            ry = row_y0 + i * row_h
            parts.append(f'<rect x="{margin + 8}" y="{ry}" width="{table_w - 16}" height="{row_h - 6}" rx="5" class="card"/>')
            cy = ry + (row_h - 6) / 2
            parts.append(f'<text x="{margin + col_cx[0]}" y="{cy}" class="pos">{html.escape(row[0])}</text>')
            for j, value in enumerate(row[1:]):
                parts.append(f'<text x="{margin + col_cx[j + 1]}" y="{cy}" class="out">{html.escape(value)}</text>')
        y += title_h + body_h(len(rows)) + section_gap
    parts.append('</svg>')
    overview_svg.write_text("\n".join(parts) + "\n")
    with overview_yaml.open("w") as f:
        yaml.dump({
            "families": [
                {"name": fam_title, "chords": [
                    {
                        "label": f"{key_labels[top]} + {key_labels[home]}",
                        "positions": chord["positions"],
                        "plain": chord["normal_shift"][0],
                        "shift": chord["normal_shift"][1],
                        "ctrl": chord["ctrl"],
                        "ctrl_shift": chord["ctrl_shift"],
                    }
                    for chord in chords
                    for top, home in [_chord_row_order(chord, key_labels, a1_order)]
                ]}
                for fam_title, chords, _rows in families
            ],
        }, f, sort_keys=False, allow_unicode=True)
    return [overview_svg]


def build_symbol_layer_overview(draw_dir, config_dir, source_data):
    """Render the combined a1/a2 board plus a compact mod-morph reference.

    Intended as a second-screen learning aid: the combined alpha board
    (dual alpha "t1 / t2" without sub-layer legends, thumbs, bigram chords)
    on top, below it a compact table of the ten diagonal chords in all four
    modifier states and the non-diagonal morphs, and the thumb/symbol-chord
    reference. Bugwind only -- the diagonal chords live in the bugwind
    combo set.
    """
    if ACTIVE != "bugwind":
        return None

    v = variant()
    out_svg = draw_dir / "twonr9_symbol_layer.svg"
    out_yaml = draw_dir / "twonr9_symbol_layer.yaml"

    # --- Step A: render the combined a1/a2 board (same style as the others) ---
    # Dual alpha without the 4-corner sub-layer legends ("subscripts"), plus
    # the six bigram chords. The diagonal symbol chords live on a1/a2 too,
    # but their chips would cover the alpha keys -- they are listed in the
    # table below instead.
    sym_yaml = {
        "layout": {"zmk_keyboard": "twonr9"},
        "layers": {"Combined (a1 / a2)": build_combined_alpha_layer(source_data["layers"], corners=False)},
        "combos": [
            {
                "p": list(pos),
                "k": label,
                "l": ["Combined (a1 / a2)"],
                "type": "bigram",
                "align": "mid",
                "offset": 0.0,
                "width": 54.0,
            }
            for pos, label in combined_bigram_map(v).items()
        ],
    }
    with out_yaml.open("w") as f:
        yaml.dump(sym_yaml, f, sort_keys=False, allow_unicode=True)

    res = subprocess.run(
        ["keymap", "-c", str(draw_dir / "twonr9_config.yaml"), "draw",
         str(out_yaml), "-j", str(config_dir / "twonr9.json")],
        capture_output=True, text=True, check=True
    )
    svg = res.stdout

    # --- Step B: derive chord rows per family from the parsed a1 layer ---
    key_labels = [extract_label(key) for key in source_data.get("layers", {}).get("a1", [])]
    key_labels.extend(str(index) for index in range(len(key_labels), 18))
    a1_order = {label: index for index, label in enumerate(key_labels)}

    def state_text(value):
        return " / ".join(value) if isinstance(value, tuple) else value

    # One row per chord, split by hand: the top key decides (0-2 = left, 3-5 =
    # right; each diagonal's home key is always on the same side).
    family_blocks = []
    for fam_key, fam_title in FAMILY_ORDER:
        chords = sorted(
            (c for c in DIAGONAL_CHORDS if c["family"] == fam_key),
            key=lambda c: _chord_row_order(c, key_labels, a1_order),
        )
        left_rows, right_rows = [], []
        for chord in chords:
            top, home = _chord_row_order(chord, key_labels, a1_order)
            row = (
                f"{key_labels[top]} + {key_labels[home]}",
                state_text(chord["normal_shift"][0]),
                state_text(chord["normal_shift"][1]),
                state_text(chord["ctrl"]),
                state_text(chord["ctrl_shift"]),
            )
            (left_rows if top < 3 else right_rows).append(row)
        family_blocks.append((fam_title, left_rows, right_rows))

    # Two columns so the table sits compactly below the board: inner families
    # left, outer families right.
    col_groups = [family_blocks[:2], family_blocks[2:]]

    # --- Step C: append the reference cards (below the footer at y=345) ---
    # Cards follow the cheatsheet card conventions: CSS-variable driven so the
    # dark-mode media query in twonr9_config.yaml keeps applying.
    card_w = 736
    x0 = 20
    y0 = 370

    def esc(s):
        return html.escape(s, quote=False)

    def card_frame(title, y, height, body):
        return (
            f'  <g transform="translate({x0}, {y})" class="symov-card">\n'
            f'    <rect x="0" y="0" width="{card_w}" height="{height}" rx="8" '
            f'style="fill: var(--color-held); fill-opacity: 0.25; stroke: var(--color-dendron); stroke-width: 1.5;"/>\n'
            f'    <text x="24" y="28" style="text-anchor: start; font-size: 14px; font-weight: bold; '
            f'fill: var(--color-text); letter-spacing: 0.5px;">{title}</text>\n'
            f'{body}\n  </g>\n'
        )

    # Card A: the diagonal chords grouped by family, in two columns (inner
    # families left, outer families right) so the card stays short enough to
    # sit below the board. Within each family, a dashed divider separates the
    # left-hand chords (top key L/M/D) from the right-hand chords (Y/O/U).
    fam_gap = 26
    row_h = 24
    fam_title_h = 22
    sub_hdr_h = 16
    col_gap = 16
    hand_gap = 4
    f_width = 344
    f_col0 = 18                                # chord label (start-anchored)
    f_col_cx = [128, 190, 250, 318]            # plain, shift, ctrl, ctrl+shift centers

    def fam_block(title, left_rows, right_rows, x, y):
        b = f'    <text x="{x}" y="{y}" style="text-anchor: start; font-size: 12.5px; font-weight: bold; ' \
            f'fill: #a89984;">{esc(title)}</text>\n'
        y += fam_title_h
        hdr = ''.join(
            f'<text x="{x + (f_col0 if i == 0 else f_col_cx[i - 1])}" y="{y}" '
            f'style="text-anchor: {"start" if i == 0 else "middle"}; font-size: 10px; '
            f'font-weight: bold; fill: #a89984;">{t}</text>'
            for i, t in enumerate(["CHORD", "PLAIN", "SHIFT", "CTRL", "CTRL+SHIFT"])
        )
        b += f'    {hdr}\n'
        y += sub_hdr_h

        def rows_at(rows, top_y, hand, color):
            if not rows:
                return ""
            s = (f'    <text x="{x + 6}" y="{top_y + 4}" style="text-anchor: middle; '
                 f'font-size: 10px; font-weight: bold; fill: {color};">{hand}</text>\n')
            for i, row in enumerate(rows):
                ry = top_y + i * row_h
                s += ''.join(
                    f'<text x="{x + (f_col0 if j == 0 else f_col_cx[j - 1])}" y="{ry}" '
                    f'style="text-anchor: {"start" if j == 0 else "middle"}; font-size: 12px; '
                    f'font-weight: {700 if j == 0 else 600}; fill: var(--color-text);">{esc(val)}</text>'
                    for j, val in enumerate(row)
                ) + '\n'
            return s

        top_y = y
        b += rows_at(left_rows, top_y, "L", "var(--color-sym)")
        div_y = top_y + len(left_rows) * row_h - row_h // 2
        if left_rows and right_rows:
            b += (f'    <line x1="{x + 2}" y1="{div_y + 2}" x2="{x + f_width - 2}" y2="{div_y + 2}" '
                  f'style="stroke: #a89984; stroke-width: 1; stroke-dasharray: 3,3; opacity: 0.7;"/>\n')
        # First right-hand baseline = end of left block + small gap.
        right_top = top_y + len(left_rows) * row_h + 2 + hand_gap
        b += rows_at(right_rows, right_top, "R", "#d79921")
        body_h = (sub_hdr_h + len(left_rows) * row_h + hand_gap
                  + (len(right_rows) if right_rows else 0) * row_h)
        return b, fam_title_h + body_h

    body = ""
    col_heights = []
    for x_off, groups in enumerate(col_groups):
        gx = x_off * (f_width + col_gap)
        gy = 44
        for title, left_rows, right_rows in groups:
            blk, bh = fam_block(title, left_rows, right_rows, x0 + 16 + gx, gy)
            body += blk
            gy += bh + fam_gap
        col_heights.append(gy - 44 + 4)
    card_a_h = 44 + max(col_heights) + 10
    card_a = card_frame("MOD MORPHS &#8212; DIAGONAL CHORDS (A1 / A2) &#8212; grouped by family",
                        y0, card_a_h, body)

    # Card B: non-diagonal morphs + thumbs + symbol entries
    b_y = y0 + card_a_h + 20
    b = ""
    b += '    <text x="30" y="52" style="text-anchor: start; font-size: 11px; font-weight: bold; fill: #a89984;">OTHER SHIFT MORPHS</text>\n'
    other_morphs = [
        (". \u2192 ,", "num layer: . / , decimal morph (dot_comma)", "#d65d0e"),
        ("\u232B \u2192 \u2326", "top row 3+4: backspace / delete (bs_del)", "#b16286"),
        ("\u2318R \u2192 \u2318\u2303C", "nav layer T: niri column width / center (niri_adjust)", "#d79921"),
    ]
    for i, (label, desc, color) in enumerate(other_morphs):
        y = 74 + i * 22
        b += f'    <text x="30" y="{y}" style="text-anchor: start; font-size: 12px; font-weight: 700; fill: {color};">{esc(label)}</text>\n'
        b += f'    <text x="190" y="{y}" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">{esc(desc)}</text>\n'

    b += '    <text x="30" y="142" style="text-anchor: start; font-size: 11px; font-weight: bold; fill: #a89984;">THUMB CLUSTER</text>\n'
    thumbs = [
        ("14 (L-Out)", "#b16286", "a2 dual: tap momentary a2 \u00b7 hold sticky a2"),
        ("15 (L-In)", "#d79921", "space \u00b7 shift-tap \u201c. \u201d \u00b7 hold nav"),
        ("16 (R-In)", "#b57614", "magic shift: tap \u21e7/repeat \u00b7 on pause sticky \u21e7 \u00b7 hold \u21e7"),
        ("17 (R-Out)", "#d65d0e", "smart num: tap num_word (drops on space) \u00b7 hold num"),
    ]
    for i, (label, color, desc) in enumerate(thumbs):
        y = 164 + i * 22
        b += f'    <text x="30" y="{y}" style="text-anchor: start; font-size: 12px; font-weight: 700; fill: {color};">{esc(label)}</text>\n'
        b += f'    <text x="190" y="{y}" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">{esc(desc)}</text>\n'

    b += '    <text x="30" y="258" style="text-anchor: start; font-size: 11px; font-weight: bold; fill: #a89984;">SYMBOL LAYER ENTRIES</text>\n'
    entries = [
        ("17 (R-Out)", "tap sym \u00b7 hold sticky sym (only sym entry \u2014 all sym symbols now have diagonal chords)"),
        (v["sz_chord"], "Eszett \u00df chord on a1/a2 (not on sym)"),
    ]
    for i, (label, desc) in enumerate(entries):
        y = 280 + i * 22
        b += f'    <text x="30" y="{y}" style="text-anchor: start; font-size: 12px; font-weight: 700; fill: var(--color-text);">{esc(label)}</text>\n'
        b += f'    <text x="190" y="{y}" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">{esc(desc)}</text>\n'
    # Card B bottom content sits at 280 + 4*22 - ~5 = 363; leave 20px padding.
    card_b_h = 280 + len(entries) * 22 + 20
    card_b = card_frame("MORPHS, THUMBS &amp; SYMBOL ENTRIES", b_y, card_b_h, b)

    total_h = b_y + card_b_h + 20
    svg = re.sub(
        r'width="(\d+)" height="(\d+)" viewBox="0 0 (\d+) (\d+)"',
        lambda m: 'width="{}" height="{}" viewBox="0 0 {} {}"'.format(
            m.group(1), total_h, m.group(3), total_h),
        svg,
        count=1,
    )

    svg = svg.replace("</svg>", card_a + card_b + "\n</svg>")
    out_svg.write_text(svg)
    post_process_svg_colors(out_svg)
    return [out_svg]


def build_cheatsheet_svg(cfg_2col_path, combined_yaml_path, cheatsheet_svg_path, config_dir):
    # Step A: Render the 2-column wide combined layout
    res = subprocess.run(
        ["keymap", "-c", str(cfg_2col_path), "draw", str(combined_yaml_path), "-j", str(config_dir / "twonr9.json")],
        capture_output=True, text=True, check=True
    )
    svg = res.stdout

    # Step B: Expand height and viewBox to 1533 x 1020
    svg = re.sub(
        r'width="(\d+)" height="(\d+)" viewBox="0 0 (\d+) (\d+)"',
        r'width="1533" height="1020" viewBox="0 0 1533 1020"',
        svg
    )

    # Step C: Append spacious 2-column cheatsheet cards below the boards
    cheatsheet_cards = '''
  <!-- LEFT COLUMN CARD (x=20, width=736, height=580) -->
  <g transform="translate(20, 410)" class="cheatsheet-left">
    <rect x="0" y="0" width="736" height="580" rx="8" class="cs-card-bg" style="fill: var(--color-held); fill-opacity: 0.25; stroke: var(--color-dendron); stroke-width: 1.5;"/>
    
    <!-- 4-Corner Sub-Layer Legends Key -->
    <text x="24" y="28" style="text-anchor: start; font-size: 14px; font-weight: bold; fill: var(--color-text); letter-spacing: 0.5px;">FOUR-CORNER SUB-LAYER LEGENDS</text>
    
    <g transform="translate(24, 42)">
      <rect x="0" y="0" width="14" height="14" rx="3" style="fill: #458588;"/>
      <text x="22" y="11" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #458588;">Top-Left (Cyan):</text>
      <text x="130" y="11" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">sym — 14 Morphs: ( &lt; ) &gt; [ { ] } ; \' : " / \\ ! ? # ~ $ € ` ^ &amp; @ | =</text>
    </g>
    
    <g transform="translate(24, 64)">
      <rect x="0" y="0" width="14" height="14" rx="3" style="fill: #d79921;"/>
      <text x="22" y="11" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #d79921;">Top-Right (Yellow):</text>
      <text x="142" y="11" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">nav — Arrows ← ↓ ↑ →, Niri Ops ⌘Q ⌘⇥ ⌘R ⇹, Workspace ⌘⇞ ⌘⇟</text>
    </g>
    
    <g transform="translate(24, 86)">
      <rect x="0" y="0" width="14" height="14" rx="3" style="fill: #d65d0e;"/>
      <text x="22" y="11" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #d65d0e;">Bottom-Left (Orange):</text>
      <text x="160" y="11" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">num — 4 5 6 Top, 1 2 3 0 Home, . , Decimal Morph, 7 8 9 Chords</text>
    </g>
    
    <g transform="translate(24, 108)">
      <rect x="0" y="0" width="14" height="14" rx="3" style="fill: #689d6a;"/>
      <text x="22" y="11" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #689d6a;">Bottom-Right (Green):</text>
      <text x="160" y="11" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">fn — Function F1-F12 &amp; Volume Controls V- V+</text>
    </g>

    <!-- Thumb cluster reference -->
    <text x="24" y="152" style="text-anchor: start; font-size: 14px; font-weight: bold; fill: var(--color-text); letter-spacing: 0.5px;">THUMB CLUSTER</text>

    <!-- Thumb 14 -->
    <rect x="24" y="168" width="162" height="110" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="105" y="188" style="font-size: 12px; font-weight: bold; fill: var(--color-text);">Thumb 14 (L-Out)</text>
    <text x="105" y="206" style="font-size: 11.5px; font-weight: bold; fill: #b16286;">a2 Dual Mode</text>
    <text x="105" y="228" style="font-size: 11px; fill: var(--color-text);">Tap: 1 Sticky a2</text>
    <text x="105" y="246" style="font-size: 11px; fill: var(--color-text);">Hold: Continuous a2</text>
    <text x="105" y="264" style="font-size: 10px; fill: #7c6f64;">(BMW, Quiz, Pflanze)</text>

    <!-- Thumb 15 -->
    <rect x="198" y="168" width="162" height="110" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="279" y="188" style="font-size: 12px; font-weight: bold; fill: var(--color-text);">Thumb 15 (L-In)</text>
    <text x="279" y="206" style="font-size: 11.5px; font-weight: bold; fill: #d79921;">Space / Nav</text>
    <text x="279" y="228" style="font-size: 11px; fill: var(--color-text);">Tap: Spacebar</text>
    <text x="279" y="246" style="font-size: 11px; fill: var(--color-text);">Shift+Tap: ". " Morph</text>
    <text x="279" y="264" style="font-size: 10px; fill: #7c6f64;">Hold: nav Layer</text>

    <!-- Thumb 16 -->
    <rect x="372" y="168" width="162" height="110" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="453" y="188" style="font-size: 12px; font-weight: bold; fill: var(--color-text);">Thumb 16 (R-In)</text>
    <text x="453" y="206" style="font-size: 11.5px; font-weight: bold; fill: #b57614;">Magic Shift</text>
    <text x="453" y="228" style="font-size: 11px; fill: var(--color-text);">After char: Repeat (tt)</text>
    <text x="453" y="246" style="font-size: 11px; fill: var(--color-text);">On pause: Sticky Shift</text>
    <text x="453" y="264" style="font-size: 10px; fill: #7c6f64;">Hold: Shift | S-Tap: ⇪</text>

    <!-- Thumb 17 -->
    <rect x="546" y="168" width="162" height="110" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="627" y="188" style="font-size: 12px; font-weight: bold; fill: var(--color-text);">Thumb 17 (R-Out)</text>
    <text x="627" y="206" style="font-size: 11.5px; font-weight: bold; fill: #d65d0e;">Smart Num</text>
    <text x="627" y="228" style="font-size: 11px; fill: var(--color-text);">Tap: num_word entry</text>
    <text x="627" y="246" style="font-size: 11px; fill: var(--color-text);">(Auto-drops on space)</text>
    <text x="627" y="264" style="font-size: 10px; fill: #7c6f64;">Hold: Momentary Num</text>

    <!-- German Typing Rhythm Box -->
    <rect x="24" y="285" width="684" height="275" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="44" y="308" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: var(--color-text); letter-spacing: 0.5px;">SPEED, FLOW &amp; SYMBOL CHORDS</text>
    
    <text x="44" y="332" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #d79921;">• Noun Capitalization:</text>
    <text x="180" y="332" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Space (16) → Sticky Shift (17) → Letter</text>
    
    <text x="44" y="356" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #b57614;">• Symbol &amp; Double Repeat:</text>
    <text x="195" y="356" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Thumb 16 after char repeats letters, numbers &amp; symbols (==, ++, ::)</text>
    
    <text x="44" y="380" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #458588;">• German Eszett (ß):</text>
    <text x="175" y="380" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Pinch {sz_chord} ({sz_pos}) on base (Straße, groß, weiß)</text>

    <text x="44" y="404" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #b16286;">• Diagonal Symbols:</text>
    <text x="180" y="404" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">See the modifier-state overview for normal, Shift, Ctrl and Ctrl+Shift</text>

    <text x="44" y="428" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #b16286;">• Symbol Layer:</text>
    <text x="175" y="428" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Thumb 17 (R-Out) \u2014 all sym symbols are also reachable as diagonal chords</text>

    <text x="44" y="452" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #d79921;">• Niri Window Suite:</text>
    <text x="175" y="452" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Hold 15 / H / E → ⌘Q (Close), ⌘⇥ (Overview), ⌘R (Width), ⇹ (Swapper)</text>

    <text x="44" y="476" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #689d6a;">• Workspace Navigation:</text>
    <text x="195" y="476" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Hold 15 / H / E → NAV_PGDN (⌘⇟ Next), NAV_PGUP (⌘⇞ Prev)</text>

    <text x="44" y="500" style="text-anchor: start; font-size: 11.5px; font-weight: bold; fill: #d65d0e;">• Document Jumps:</text>
    <text x="165" y="500" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Long-press ← (Home), → (End), ↑ (Doc Top), ↓ (Doc End)</text>
  </g>

  <!-- RIGHT COLUMN CARD (x=776, width=736, height=580) -->
  <g transform="translate(776, 410)" class="cheatsheet-right">
    <rect x="0" y="0" width="736" height="580" rx="8" class="cs-card-bg" style="fill: var(--color-held); fill-opacity: 0.25; stroke: var(--color-dendron); stroke-width: 1.5;"/>
    <text x="24" y="28" style="text-anchor: start; font-size: 14px; font-weight: bold; fill: var(--color-text); letter-spacing: 0.5px;">COMBO QUICK LOOKUP &amp; SHORTCUTS</text>

    <!-- Top Row Combos -->
    <text x="24" y="52" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #fe8019;">EDITING &amp; NAVIGATION (TOP ROW)</text>
    
    <rect x="24" y="62" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="76" style="font-size: 12px; font-weight: bold; fill: #282828;">⇥</text>
    <text x="62" y="76" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Tab (0+1):</text>
    <text x="130" y="76" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Indent &amp; autocomplete (Left Hand)</text>

    <rect x="24" y="88" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="102" style="font-size: 12px; font-weight: bold; fill: #282828;">⏎</text>
    <text x="62" y="102" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Enter (1+2):</text>
    <text x="140" y="102" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Newline &amp; execute command (Left Hand)</text>

    <rect x="24" y="114" width="46" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="47" y="128" style="font-size: 11px; font-weight: bold; fill: #282828;">⌫/⌦</text>
    <text x="78" y="128" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Bspc / Del (3+4):</text>
    <text x="185" y="128" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Tap: Backspace | Shift+Tap: Delete</text>

    <rect x="24" y="140" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="154" style="font-size: 11px; font-weight: bold; fill: #282828;">⌃⌫</text>
    <text x="62" y="154" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Word Del (4+5):</text>
    <text x="170" y="154" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Delete entire previous word in IDE / shell</text>

    <rect x="24" y="166" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="180" style="font-size: 12px; font-weight: bold; fill: #282828;">⎋</text>
    <text x="62" y="180" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Esc (3+4+5):</text>
    <text x="140" y="180" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Helix / Vim normal mode &amp; dialog exit (Offset Top)</text>

    <!-- Home Row Combos -->
    <text x="24" y="212" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #458588;">CODING SYMBOLS &amp; ORTHOGRAPHY (HOME ROW)</text>

    <rect x="24" y="222" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="236" style="font-size: 12px; font-weight: bold; fill: #282828;">ß</text>
    <text x="62" y="236" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Eszett ({sz_pos}):</text>
    <text x="142" y="236" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">{sz_chord} chord on base (Straße, groß, weiß)</text>

    <rect x="24" y="248" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="262" style="font-size: 12px; font-weight: bold; fill: #282828;">_</text>
    <text x="62" y="262" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Underscore (7+9):</text>
    <text x="175" y="262" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Instant snake_case identifier naming</text>

    <rect x="24" y="274" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="288" style="font-size: 12px; font-weight: bold; fill: #282828;">-</text>
    <text x="62" y="288" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Minus (7+8):</text>
    <text x="142" y="288" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Hyphens, subtraction, CLI flags (--opt)</text>

    <rect x="24" y="300" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="314" style="font-size: 12px; font-weight: bold; fill: #282828;">:</text>
    <text x="62" y="314" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Colon (11+12):</text>
    <text x="150" y="314" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Rust :: namespace paths, Python defs &amp; JSON pairs</text>

    <rect x="24" y="326" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="340" style="font-size: 12px; font-weight: bold; fill: #282828;">;</text>
    <text x="62" y="340" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Semicolon (10+12):</text>
    <text x="180" y="340" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Statement terminators for C, Rust, TS, Java</text>

    <!-- System, symbols, and numbers -->
    <text x="24" y="372" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #d3869b;">SYSTEM, SYMBOLS &amp; NUMPAD</text>

    <rect x="24" y="382" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="396" style="font-size: 12px; font-weight: bold; fill: #282828;">⇪</text>
    <text x="62" y="396" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Caps Word (14+15):</text>
    <text x="185" y="396" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">UPPERCASE_CONSTANTS (Auto-exits on space/enter)</text>

    <rect x="24" y="408" width="30" height="20" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="39" y="422" style="font-size: 12px; font-weight: bold; fill: #282828;">🔓</text>
    <text x="62" y="422" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Studio Unlock (6+7+8+9):</text>
    <text x="230" y="422" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Live ZMK Studio key remapping (on sym)</text>

    <rect x="24" y="434" width="30" height="20" rx="4" style="fill: #d65d0e; stroke: #af3a03; stroke-width: 1.5;"/>
    <text x="39" y="448" style="font-size: 10.5px; font-weight: bold; fill: #fbf1c7;">7 8 9</text>
    <text x="62" y="448" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #d65d0e;">Num Chords (3+10, 4+11, 5+12):</text>
    <text x="275" y="448" style="text-anchor: start; font-size: 11.5px; fill: var(--color-text);">Vertical chords on num for calculator top row</text>
  </g>
'''
    v = variant()
    ak = v.get("adaptive")
    cheatsheet_cards = cheatsheet_cards.replace("{sz_chord}", v["sz_chord"]).replace("{sz_pos}", v["sz_pos"]).replace(
        "{adaptive_line}",
        ak["swaps_line"] if ak else "None — every letter is bound directly on the grid",
    )

    svg = svg.replace("</svg>", cheatsheet_cards + "\n</svg>")
    with open(cheatsheet_svg_path, "w") as f:
        f.write(svg)
    post_process_svg_colors(cheatsheet_svg_path)

def render_variant(name, config_dir, draw_dir):
    """Render the additional mod-morph list without touching saved drawings."""
    global ACTIVE
    global _DIAGONAL_COMBOS
    ACTIVE = name
    v = variant()
    # This repository keeps the established drawings as checked-in artifacts.
    # Generate only the additional bugwind modifier-state list here.
    if name != "bugwind":
        print(f"[{v['title']}] No additional drawing for this variant")
        return []

    res = subprocess.run(
        ["keymap", "-c", str(draw_dir / "twonr9_config.yaml"), "parse", "-z",
         str(config_dir / v["keymap"])],
        capture_output=True, text=True, check=True
    )
    d = yaml.safe_load(res.stdout)
    for keys in d.get("layers", {}).values():
        for index, key in enumerate(keys):
            keys[index] = decode_binding(key)

    parsed_positions = set()
    for combo in d.get("combos", []):
        combo["k"] = decode_combo_key(combo["k"])
        parsed_positions.add(tuple(combo.get("p", [])))
    for extra in v.get("extra_combos", []):
        if tuple(extra["p"]) not in parsed_positions:
            d.setdefault("combos", []).append(dict(extra))

    built = build_mod_morph_overview(draw_dir, config_dir, draw_dir / "twonr9_config.yaml", d)
    built += build_symbol_layer_overview(draw_dir, config_dir, d)
    return built


def main(argv=None):
    """Render diagrams.

    With no arguments only the default (bugwind) variant is drawn, so
    ``just draw-twonr9`` keeps producing the filenames the docs link to.
    Pass variant names (``bugwind``, ``srht``, ``all``) to render others.
    """
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv == ["all"]:
        names = [n for n in VARIANTS if n == "bugwind"] if not argv else list(VARIANTS)
    else:
        unknown = [a for a in argv if a not in VARIANTS]
        if unknown:
            sys.exit(f"unknown variant(s): {', '.join(unknown)} "
                     f"(choose from: {', '.join(VARIANTS)}, all)")
        names = list(dict.fromkeys(argv))

    root = Path(__file__).resolve().parent.parent
    config_dir = root / "config"
    draw_dir = root / "draw"
    for name in names:
        render_variant(name, config_dir, draw_dir)

if __name__ == "__main__":
    main()
