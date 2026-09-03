#!/usr/bin/env python3
import sys
import subprocess
import yaml
import re
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
    "Gui": "⌘",
    "LEFT_GUI": "⌘",
    "LGUI": "⌘",
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
    if "mt_bspc" in s or "NAV_BSPC" in s:
        return {"t": "⌫", "h": "W-Del"}
    if "LG(DE_Q)" in s or "LG(Q)" in s or "KEYBOARD_Q" in s and "LG" in s:
        return "⌘Q"
    if "LG(TAB)" in s or "KEYBOARD_TAB" in s and "LG" in s:
        return "⌘⇥"

    # Hold-taps: &hml / &hmr
    m = re.search(r"&(?:hml|hmr)\s+([A-Z_]+)\s+(.+)", s)
    if m:
        mod_raw, key_part = m.group(1), m.group(2)
        mod_label = "⌥" if "ALT" in mod_raw else ("⌘" if "GUI" in mod_raw else ("⇧" if "SHI" in mod_raw or "SFT" in mod_raw else "⌃"))
        return {"t": decode_hid_code(key_part), "h": mod_label}

    # Layer-taps: &lt_r4 <layer> <key>
    m = re.search(r"&lt_r4\s+(\d+)\s+(.+)", s)
    if m:
        layer_idx, key_part = int(m.group(1)), m.group(2)
        layer_names = {0: "a1", 1: "a2", 2: "nav", 3: "sym", 4: "fn", 5: "num"}
        layer_label = layer_names.get(layer_idx, str(layer_idx))
        return {"t": decode_hid_code(key_part), "h": layer_label}

    # If it contains HID USAGE
    if "HID_USAGE" in s.upper() or "ZMK_HID" in s.upper() or "ZMK HID" in s:
        return decode_hid_code(s)

    return s

combo_symbol_map = {
    "&macro_rl": "RL",
    "&macro_hn": "HN",
    "&macro_dt": "DT",
    "&macro_cy": "CY",
    "&macro_eo": "EO",
    "&macro_ui": "UI",
    "&macro_lr": "LR",
    "&macro_nb": "NB",
    "&macro_mt": "MT",
    "&macro_gy": "GY",
    "&macro_oe": "OE",
    "&macro_iu": "IU",
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
    decoded = decode_hid_code(s)
    if decoded in combo_symbol_map:
        return combo_symbol_map[decoded]
    return decoded

def classify_combo_type(c):
    k = c.get("k")
    layers = c.get("l", [])
    
    # 1. Bigrams
    if isinstance(k, str) and (k in ["RL", "HN", "DT", "CY", "EO", "UI", "LR", "NB", "MT", "GY", "OE", "IU"] or "RL / LR" in k or "/" in k):
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
    for c in combos:
        p = set(c.get("p", []))
        c_type = classify_combo_type(c)
        c["type"] = c_type
        
        if c.get("k") == "⌫ / ⌦":
            c["width"] = 46.0

        # Only offset combos if they share keys (e.g. 3-key chords sharing keys with 2-key combos)
        if len(p) > 2:
            is_top = p.issubset({0, 1, 2, 3, 4, 5})
            is_bottom = p.issubset({6, 7, 8, 9, 10, 11, 12, 13})
            if is_top:
                c["align"] = "top"
                c["offset"] = 0.12
            elif is_bottom:
                c["align"] = "bottom"
                c["offset"] = 0.07
            else:
                c["align"] = "mid"
                c["offset"] = 0.0
        else:
            # All 2-key combos stay in their natural spot between keys without offset
            c["align"] = "mid"
            c["offset"] = 0.0

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

def build_combined_alpha_layer(layers):
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
        if i < 14:
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

    # 4. Style bigram dual text on the same horizontal baseline: RL / LR
    for (b1, b2) in [("RL", "LR"), ("HN", "NB"), ("DT", "MT"), ("CY", "GY"), ("EO", "OE"), ("UI", "IU")]:
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
    <text x="24" y="28" style="text-anchor: start; font-size: 15px; font-weight: bold; fill: var(--color-text);">4-CORNER SUB-LAYER LEGENDS</text>
    
    <rect x="24" y="44" width="16" height="16" rx="3" style="fill: #458588;"/>
    <text x="48" y="56" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #458588;">Top-Left (Cyan):</text>
    <text x="165" y="56" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">sym (14 Morphs: ( &lt; ) &gt; [ { ] } : " ; \' / \\ ! ? # ~ $ € ` ^ &amp; @ | =)</text>
    
    <rect x="24" y="68" width="16" height="16" rx="3" style="fill: #d79921;"/>
    <text x="48" y="80" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #d79921;">Top-Right (Yellow):</text>
    <text x="165" y="80" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">nav (Arrows ← ↓ ↑ → &amp; Document Navigation ↖ ↘ ⇞ ⇟)</text>
    
    <rect x="24" y="92" width="16" height="16" rx="3" style="fill: #d65d0e;"/>
    <text x="48" y="104" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #d65d0e;">Bottom-Left (Orange):</text>
    <text x="185" y="104" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">num (3x3 Calculator: 4 5 6 Top, 1 2 3 0 Home, 7 8 9 Chords)</text>
    
    <rect x="24" y="116" width="16" height="16" rx="3" style="fill: #689d6a;"/>
    <text x="48" y="128" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #689d6a;">Bottom-Right (Green):</text>
    <text x="185" y="128" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">fn (F1-F12 Functions &amp; Volume Controls V- V+)</text>

    <!-- Symmetrical Adaptive Thumb Engine -->
    <text x="24" y="172" style="text-anchor: start; font-size: 15px; font-weight: bold; fill: var(--color-text);">SYMMETRICAL ADAPTIVE THUMB ENGINE</text>

    <!-- Thumb 14 -->
    <rect x="24" y="188" width="162" height="120" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="105" y="210" style="font-size: 13px; font-weight: bold; fill: var(--color-text);">Thumb 14 (Left Outer)</text>
    <text x="105" y="230" style="font-size: 12px; font-weight: bold; fill: #b16286;">a2 Dual Mode</text>
    <text x="105" y="252" style="font-size: 11px; fill: var(--color-text);">• Tap: 1 secondary alpha</text>
    <text x="105" y="270" style="font-size: 11px; fill: var(--color-text);">• Hold: continuous a2</text>
    <text x="105" y="290" style="font-size: 10px; fill: #7c6f64;">(BMW, Quiz, Pflanze)</text>

    <!-- Thumb 15 -->
    <rect x="198" y="188" width="162" height="120" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="279" y="210" style="font-size: 13px; font-weight: bold; fill: var(--color-text);">Thumb 15 (Left Inner)</text>
    <text x="279" y="230" style="font-size: 12px; font-weight: bold; fill: #d79921;">Space / Nav Hold</text>
    <text x="279" y="252" style="font-size: 11px; fill: var(--color-text);">• Tap: Spacebar</text>
    <text x="279" y="270" style="font-size: 11px; fill: var(--color-text);">• Shift+Tap: ". " morph</text>
    <text x="279" y="290" style="font-size: 10px; fill: #7c6f64;">• Hold: Nav layer</text>

    <!-- Thumb 16 -->
    <rect x="372" y="188" width="162" height="120" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="453" y="210" style="font-size: 13px; font-weight: bold; fill: var(--color-text);">Thumb 16 (Right Inner)</text>
    <text x="453" y="230" style="font-size: 12px; font-weight: bold; fill: #b57614;">Magic Shift</text>
    <text x="453" y="252" style="font-size: 11px; fill: var(--color-text);">• After letter: Repeat (tt,ll)</text>
    <text x="453" y="270" style="font-size: 11px; fill: var(--color-text);">• On pause: Sticky Shift</text>
    <text x="453" y="290" style="font-size: 10px; fill: #7c6f64;">• Hold: Continuous Shift</text>

    <!-- Thumb 17 -->
    <rect x="546" y="188" width="162" height="120" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="627" y="210" style="font-size: 13px; font-weight: bold; fill: var(--color-text);">Thumb 17 (Right Outer)</text>
    <text x="627" y="230" style="font-size: 12px; font-weight: bold; fill: #d65d0e;">Smart Num</text>
    <text x="627" y="252" style="font-size: 11px; fill: var(--color-text);">• Tap: num_word entry</text>
    <text x="627" y="270" style="font-size: 11px; fill: var(--color-text);">(Auto-drops on space/alpha)</text>
    <text x="627" y="290" style="font-size: 10px; fill: #7c6f64;">• Hold: Momentary Num</text>

    <!-- German Typing Rhythm Box -->
    <rect x="24" y="325" width="684" height="235" rx="6" style="fill: var(--color-key); stroke: var(--color-dendron); stroke-width: 1;"/>
    <text x="44" y="348" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: var(--color-text);">GERMAN TYPING FLOW &amp; SPEED TECHNIQUES</text>
    <text x="44" y="374" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">• <tspan font-weight="bold">German Noun Capitalization:</tspan> Left Thumb 15 (Space) → Right Thumb 16 (Sticky Shift) → Noun Letter</text>
    <text x="44" y="396" style="text-anchor: start; font-size: 12px; fill: #7c6f64;">  (Shift automatically arms for exactly 1 letter and disarms immediately after — no holding required)</text>
    
    <text x="44" y="426" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">• <tspan font-weight="bold">Double Letters (Schifffahrt, Bitte, Alles):</tspan> Type letter → Right Thumb 16 (Instant Repeat)</text>
    <text x="44" y="448" style="text-anchor: start; font-size: 12px; fill: #7c6f64;">  (Outputs repeated character instantly with zero finger movement or layer delay)</text>

    <text x="44" y="478" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">• <tspan font-weight="bold">German Eszett (Straße, groß, weiß):</tspan> Pinch Left Home Keys 6 + 7 (S + R) on base</text>
    <text x="44" y="500" style="text-anchor: start; font-size: 12px; fill: #7c6f64;">  (Outputs native ß instantly without switching to special symbol layers)</text>

    <text x="44" y="530" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">• <tspan font-weight="bold">Continuous Secondary Alphas (BMW, Quiz):</tspan> Hold Left Thumb 14 (a2 Dual) → Type letters</text>
  </g>

  <!-- RIGHT COLUMN CARD (x=776, width=736, height=580) -->
  <g transform="translate(776, 410)" class="cheatsheet-right">
    <rect x="0" y="0" width="736" height="580" rx="8" class="cs-card-bg" style="fill: var(--color-held); fill-opacity: 0.25; stroke: var(--color-dendron); stroke-width: 1.5;"/>
    <text x="24" y="28" style="text-anchor: start; font-size: 15px; font-weight: bold; fill: var(--color-text);">COMBO LOOKUP, USABILITY &amp; PRACTICAL BENEFITS</text>

    <!-- Top Row Combos -->
    <text x="24" y="54" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #fe8019;">TOP ROW: CODE EDITING &amp; NAVIGATION</text>
    
    <rect x="24" y="66" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="81" style="font-size: 13px; font-weight: bold; fill: #282828;">⇥</text>
    <text x="66" y="80" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Tab (0+1):</text>
    <text x="130" y="80" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Instant code indentation, autocomplete &amp; form navigation (Left hand)</text>

    <rect x="24" y="94" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="109" style="font-size: 13px; font-weight: bold; fill: #282828;">⏎</text>
    <text x="66" y="108" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Enter (1+2):</text>
    <text x="140" y="108" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Execute shell commands, insert newlines without moving right hand</text>

    <rect x="24" y="122" width="46" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="47" y="137" style="font-size: 12px; font-weight: bold; fill: #282828;">⌫ / ⌦</text>
    <text x="78" y="136" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Bspc / Del (3+4):</text>
    <text x="185" y="136" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Morph: Tap for Backspace, Shift+Tap for forward Delete</text>

    <rect x="24" y="150" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="165" style="font-size: 12px; font-weight: bold; fill: #282828;">⌃⌫</text>
    <text x="66" y="164" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Word Delete (4+5):</text>
    <text x="190" y="164" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Delete entire previous word in IDEs and terminal in one quick pinch</text>

    <rect x="24" y="178" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="193" style="font-size: 13px; font-weight: bold; fill: #282828;">⎋</text>
    <text x="66" y="192" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Esc (3+4+5):</text>
    <text x="140" y="192" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Instant modal exit for Helix / Vim normal mode &amp; dialogs (Offset Top)</text>

    <!-- Home Row Combos -->
    <text x="24" y="226" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #458588;">HOME ROW: CODING SYMBOLS &amp; GERMAN ORTHOGRAPHY</text>

    <rect x="24" y="238" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="253" style="font-size: 13px; font-weight: bold; fill: #282828;">ß</text>
    <text x="66" y="252" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Eszett (6+7):</text>
    <text x="146" y="252" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">S + R chord on base for native German words (Straße, groß, weiß)</text>

    <rect x="24" y="266" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="281" style="font-size: 13px; font-weight: bold; fill: #282828;">_</text>
    <text x="66" y="280" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Underscore (7+8):</text>
    <text x="180" y="280" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Single-chord snake_case variable &amp; function naming</text>

    <rect x="24" y="294" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="309" style="font-size: 13px; font-weight: bold; fill: #282828;">-</text>
    <text x="66" y="308" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Minus (8+9):</text>
    <text x="146" y="308" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Hyphenated words, negative values, and CLI flags (--flag)</text>

    <rect x="24" y="322" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="337" style="font-size: 13px; font-weight: bold; fill: #282828;">:</text>
    <text x="66" y="336" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Colon (10+11):</text>
    <text x="155" y="336" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Rust :: namespace paths, Python defs &amp; JSON key-value pairs</text>

    <rect x="24" y="350" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="365" style="font-size: 13px; font-weight: bold; fill: #282828;">;</text>
    <text x="66" y="364" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Semicolon (11+12):</text>
    <text x="185" y="364" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Statement terminators for C, Rust, TypeScript, Java</text>

    <!-- System & Numbers -->
    <text x="24" y="400" style="text-anchor: start; font-size: 13px; font-weight: bold; fill: #d3869b;">SYSTEM &amp; NUMPAD SHORTCUTS</text>

    <rect x="24" y="412" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="427" style="font-size: 13px; font-weight: bold; fill: #282828;">⇪</text>
    <text x="66" y="426" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Caps Word (14+15):</text>
    <text x="185" y="426" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Type UPPERCASE_CONSTANTS (auto-deactivates on space/enter)</text>

    <rect x="24" y="440" width="34" height="22" rx="4" style="fill: #ebdbb2; stroke: #d5c4a1; stroke-width: 1;"/>
    <text x="41" y="455" style="font-size: 13px; font-weight: bold; fill: #282828;">🔓</text>
    <text x="66" y="454" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: var(--color-text);">Studio Unlock (7+8+9):</text>
    <text x="210" y="454" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Unlocks live ZMK Studio key remapping (on Sym layer, Offset Bottom)</text>

    <rect x="24" y="468" width="34" height="22" rx="4" style="fill: #d65d0e; stroke: #af3a03; stroke-width: 1.5;"/>
    <text x="41" y="483" style="font-size: 12px; font-weight: bold; fill: #fbf1c7;">7 8 9</text>
    <text x="66" y="482" style="text-anchor: start; font-size: 12px; font-weight: bold; fill: #d65d0e;">Numpad Chords (3+10, 4+11, 5+12):</text>
    <text x="280" y="482" style="text-anchor: start; font-size: 12px; fill: var(--color-text);">Vertical chords on Num layer for upper digits</text>
  </g>
'''

    svg = svg.replace("</svg>", cheatsheet_cards + "\n</svg>")
    with open(cheatsheet_svg_path, "w") as f:
        f.write(svg)
    post_process_svg_colors(cheatsheet_svg_path)

def main():
    root = Path(__file__).resolve().parent.parent
    config_dir = root / "config"
    draw_dir = root / "draw"

    # Step 1: Parse keymap
    res = subprocess.run(
        ["keymap", "-c", str(draw_dir / "twonr9_config.yaml"), "parse", "-z", str(config_dir / "twonr9.keymap")],
        capture_output=True, text=True, check=True
    )
    d = yaml.safe_load(res.stdout)

    # Step 2: Clean up keys and combos
    for layer, keys in d.get("layers", {}).items():
        for i, k in enumerate(keys):
            keys[i] = decode_binding(k)

    for c in d.get("combos", []):
        c["k"] = decode_combo_key(c["k"])
        layers = c.get("l", [])
        # In the All-Layers diagram (twonr9.svg), only show universal combos on a1 and a2
        if len(layers) >= 5 or any("all" in str(x).lower() for x in layers) or set(layers) >= {"a1", "a2", "nav", "sym", "fn", "num"}:
            c["l"] = ["a1", "a2"]

    # Apply vertical / horizontal combo offsets
    apply_combo_alignment(d.get("combos", []))

    yaml_out = draw_dir / "twonr9.yaml"
    with open(yaml_out, "w") as f:
        yaml.dump(d, f, sort_keys=False)

    # Load base config for column split
    with open(draw_dir / "twonr9_config.yaml") as f:
        cfg = yaml.safe_load(f)

    # 2-column config for All-Layers (twonr9.svg)
    cfg_2col = dict(cfg)
    cfg_2col["draw_config"] = dict(cfg.get("draw_config", {}))
    cfg_2col["draw_config"]["n_columns"] = 2
    cfg_2col_path = draw_dir / "twonr9_config_2col.yaml"
    with open(cfg_2col_path, "w") as f:
        yaml.dump(cfg_2col, f, sort_keys=False)

    # 1-column config for General Overview (twonr9_overview.svg) - 10px outer pad, 19px tl
    cfg_overview = dict(cfg)
    cfg_overview["draw_config"] = dict(cfg.get("draw_config", {}))
    cfg_overview["draw_config"]["n_columns"] = 1
    cfg_overview["draw_config"]["outer_pad_w"] = 10
    cfg_overview["draw_config"]["outer_pad_h"] = 10
    cfg_overview_path = draw_dir / "twonr9_config_overview.yaml"
    with open(cfg_overview_path, "w") as f:
        yaml.dump(cfg_overview, f, sort_keys=False)

    # 1-column config for Combined Overview (twonr9_combined_overview.svg)
    cfg_combined = dict(cfg)
    cfg_combined["draw_config"] = dict(cfg.get("draw_config", {}))
    cfg_combined["draw_config"]["n_columns"] = 1
    cfg_combined_path = draw_dir / "twonr9_config_combined.yaml"
    with open(cfg_combined_path, "w") as f:
        yaml.dump(cfg_combined, f, sort_keys=False)

    # Step 3: Draw All-Layers SVG (2-column layout)
    svg_out = draw_dir / "twonr9.svg"
    with open(svg_out, "w") as f:
        subprocess.run(
            ["keymap", "-c", str(cfg_2col_path), "draw", str(yaml_out), "-j", str(config_dir / "twonr9.json")],
            stdout=f, check=True
        )
    post_process_svg_colors(svg_out)

    # Step 4: Build Overview YAML (a1 + a2 with their respective bigrams, and Symbols & Util ghost layer)
    overview_combos = []
    for c in d.get("combos", []):
        c_copy = dict(c)
        layers = c.get("l", [])
        k = c.get("k")
        if "a1" in layers and k in ["RL", "HN", "DT", "CY", "EO", "UI"]:
            c_copy["l"] = ["a1 (Base)"]
            overview_combos.append(c_copy)
        elif "a2" in layers and k in ["LR", "NB", "MT", "GY", "OE", "IU"]:
            c_copy["l"] = ["a2 (Alphas 2)"]
            overview_combos.append(c_copy)
        elif not (k in ["RL", "HN", "DT", "CY", "EO", "UI", "LR", "NB", "MT", "GY", "OE", "IU"]):
            c_copy["l"] = ["Symbols & Utilities"]
            overview_combos.append(c_copy)

    overview_data = {
        "layout": {"zmk_keyboard": "twonr9"},
        "layers": {
            "a1 (Base)": build_overview_layer(d.get("layers", {}), "a1"),
            "a2 (Alphas 2)": build_overview_layer(d.get("layers", {}), "a2"),
            "Symbols & Utilities": [""] * 18,
        },
        "combos": overview_combos
    }
    overview_yaml = draw_dir / "twonr9_overview.yaml"
    with open(overview_yaml, "w") as f:
        yaml.dump(overview_data, f, sort_keys=False)

    overview_svg = draw_dir / "twonr9_overview.svg"
    with open(overview_svg, "w") as f:
        subprocess.run(
            ["keymap", "-c", str(cfg_overview_path), "draw", str(overview_yaml), "-j", str(config_dir / "twonr9.json")],
            stdout=f, check=True
        )
    post_process_svg_colors(overview_svg)

    # Step 5: Build Combined Alpha Overview YAML (a1 / a2 merged with dual bigrams & 4-corner legends)
    combined_bigram_map = {
        (0, 7): "RL / LR",
        (1, 8): "HN / NB",
        (2, 9): "DT / MT",
        (3, 10): "CY / GY",
        (4, 11): "EO / OE",
        (5, 12): "UI / IU",
    }
    
    combined_combos = []
    for pos, label in combined_bigram_map.items():
        combined_combos.append({
            "p": list(pos),
            "k": label,
            "l": ["Combined (a1 / a2)"],
            "align": "mid",
            "offset": 0.0,
            "type": "bigram",
            "width": 54.0
        })

    for c in d.get("combos", []):
        k = c.get("k")
        if k not in ["RL", "HN", "DT", "CY", "EO", "UI", "LR", "NB", "MT", "GY", "OE", "IU"]:
            c_copy = dict(c)
            c_copy["l"] = ["Symbols & Utilities"]
            combined_combos.append(c_copy)

    combined_data = {
        "layout": {"zmk_keyboard": "twonr9"},
        "layers": {
            "Combined (a1 / a2)": build_combined_alpha_layer(d.get("layers", {})),
            "Symbols & Utilities": [""] * 18,
        },
        "combos": combined_combos
    }
    combined_yaml = draw_dir / "twonr9_combined_overview.yaml"
    with open(combined_yaml, "w") as f:
        yaml.dump(combined_data, f, sort_keys=False)

    combined_svg = draw_dir / "twonr9_combined_overview.svg"
    with open(combined_svg, "w") as f:
        subprocess.run(
            ["keymap", "-c", str(cfg_combined_path), "draw", str(combined_yaml), "-j", str(config_dir / "twonr9.json")],
            stdout=f, check=True
        )
    post_process_svg_colors(combined_svg)

    # Step 6: Build Full 2-Column Wide Infographic Cheatsheet SVG (width=1533)
    cheatsheet_svg = draw_dir / "twonr9_cheatsheet.svg"
    build_cheatsheet_svg(cfg_2col_path, combined_yaml, cheatsheet_svg, config_dir)

    # Clean up temp configs
    if cfg_2col_path.exists(): cfg_2col_path.unlink()
    if cfg_overview_path.exists(): cfg_overview_path.unlink()
    if cfg_combined_path.exists(): cfg_combined_path.unlink()

    print(f"Generated {svg_out}, {overview_svg}, {combined_svg}, and {cheatsheet_svg}")

if __name__ == "__main__":
    main()
