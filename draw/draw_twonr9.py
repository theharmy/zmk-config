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

def decode_binding(s):
    if not isinstance(s, str):
        return s

    # Hold-taps: &hml / &hmr
    m = re.search(r"&(?:hml|hmr)\s+([A-Z_]+)\s+(.+)", s)
    if m:
        mod_raw, key_part = m.group(1), m.group(2)
        mod_label = "Alt" if "ALT" in mod_raw else ("Gui" if "GUI" in mod_raw else ("Shift" if "SHI" in mod_raw or "SFT" in mod_raw else "Ctrl"))
        
        # Check direct special symbols
        if "KEYBOARD_E" in key_part and "RA" in key_part: return {"t": "€", "h": mod_label}
        if "KEYBOARD_Q" in key_part and "RA" in key_part: return {"t": "@", "h": mod_label}
        if "KEYBOARD_BACKSLASH_AND_PIPE" in key_part:
            if "LS" in key_part: return {"t": "'", "h": mod_label}
            return {"t": "#", "h": mod_label}
        if "KEYBOARD_4_AND_DOLLAR" in key_part: return {"t": "$", "h": mod_label}
        if "KEYBOARD_2_AND_AT" in key_part and "LS" in key_part: return {"t": '"', "h": mod_label}
        if "KEYBOARD_8_AND_ASTERISK" in key_part and "LS" in key_part: return {"t": "(", "h": mod_label}
        if "KEYBOARD_9_AND_LEFT_PARENTHESIS" in key_part and "LS" in key_part: return {"t": ")", "h": mod_label}
        if "KEYBOARD_PERIOD_AND_GREATER_THAN" in key_part and "LS" in key_part: return {"t": ":", "h": mod_label}
        if "KEYBOARD_RIGHT_BRACKET_AND_RIGHT_BRACE" in key_part:
            if "LS" in key_part: return {"t": "*", "h": mod_label}
            return {"t": "+", "h": mod_label}
        if "KEYBOARD_GRAVE_ACCENT_AND_TILDE" in key_part: return {"t": "^", "h": mod_label}
        if "KEYBOARD_EQUAL_AND_PLUS" in key_part:
            if "LS" in key_part: return {"t": "`", "h": mod_label}
            return {"t": "`", "h": mod_label}
        if "KEYBOARD_NON_US_BACKSLASH_AND_PIPE" in key_part:
            if "LS" in key_part: return {"t": ">", "h": mod_label}
            if "RA" in key_part: return {"t": "|", "h": mod_label}
            return {"t": "<", "h": mod_label}
        if "KEYBOARD_SLASH_AND_QUESTION_MARK" in key_part:
            if "LS" in key_part: return {"t": "_", "h": mod_label}
            return {"t": "-", "h": mod_label}
        if "KEYBOARD_7_AND_AMPERSAND" in key_part and "LS" in key_part: return {"t": "/", "h": mod_label}
        if "KEYBOARD_MINUS_AND_UNDERSCORE" in key_part and "RA" in key_part: return {"t": "\\", "h": mod_label}

        for k, v in sorted_raw_codes:
            if k in key_part:
                return {"t": v, "h": mod_label}

    # Layer-taps: &lt_r4 <layer> <key>
    m = re.search(r"&lt_r4\s+(\d+)\s+(.+)", s)
    if m:
        layer_idx, key_part = int(m.group(1)), m.group(2)
        layer_names = {0: "a1", 1: "a2", 2: "nav", 3: "sym", 4: "sym2", 5: "num"}
        layer_label = layer_names.get(layer_idx, str(layer_idx))
        
        # Check special symbols
        if "KEYBOARD_SLASH_AND_QUESTION_MARK" in key_part:
            if "LS" in key_part: return {"t": "_", "h": layer_label}
            return {"t": "-", "h": layer_label}
        if "KEYBOARD_6_AND_CARET" in key_part and "LS" in key_part: return {"t": "&", "h": layer_label}
        if "KEYBOARD_8_AND_ASTERISK" in key_part and "RA" in key_part: return {"t": "[", "h": layer_label}
        if "KEYBOARD_9_AND_LEFT_PARENTHESIS" in key_part and "RA" in key_part: return {"t": "]", "h": layer_label}
        if "KEYBOARD_NON_US_BACKSLASH_AND_PIPE" in key_part and "RA" in key_part: return {"t": "|", "h": layer_label}
        if "KEYBOARD_RIGHT_BRACKET_AND_RIGHT_BRACE" in key_part and "RA" in key_part: return {"t": "~", "h": layer_label}
        if "KEYBOARD_1_AND_EXCLAMATION" in key_part and "LS" in key_part: return {"t": "!", "h": layer_label}
        if "KEYBOARD_MINUS_AND_UNDERSCORE" in key_part and "LS" in key_part: return {"t": "?", "h": layer_label}
        if "KEYBOARD_7_AND_AMPERSAND" in key_part:
            if "RA" in key_part: return {"t": "{", "h": layer_label}
            if "LS" in key_part: return {"t": "/", "h": layer_label}
        if "KEYBOARD_0_AND_RIGHT_PARENTHESIS" in key_part and "RA" in key_part: return {"t": "}", "h": layer_label}
        if "KEYBOARD_COMMA_AND_LESS_THAN" in key_part and "LS" in key_part: return {"t": ";", "h": layer_label}
        if "KEYBOARD_5_AND_PERCENT" in key_part and "LS" in key_part: return {"t": "%", "h": layer_label}

        for k, v in sorted_raw_codes:
            if k in key_part:
                return {"t": v, "h": layer_label}

    return s

combo_map = {
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
    "&studio_unlock": "Unlock",
    "RETURN": "Enter",
}

def decode_combo_key(s):
    if not isinstance(s, str):
        return s
    if s in combo_map:
        return combo_map[s]
    
    s_norm = s.replace(" ", "_")
    
    # Specific German combos
    if "KEYBOARD_7_AND_AMPERSAND" in s_norm:
        if "RA" in s_norm: return "{"
        if "LS" in s_norm: return "/"
        return "7"
    if "KEYBOARD_8_AND_ASTERISK" in s_norm:
        if "RA" in s_norm: return "["
        if "LS" in s_norm: return "("
        return "8"
    if "KEYBOARD_9_AND_LEFT_PARENTHESIS" in s_norm:
        if "RA" in s_norm: return "]"
        if "LS" in s_norm: return ")"
        return "9"
    if "KEYBOARD_0_AND_RIGHT_PARENTHESIS" in s_norm:
        if "RA" in s_norm: return "}"
        return "0"
    if "KEYBOARD_MINUS_AND_UNDERSCORE" in s_norm:
        if "RA" in s_norm: return "\\"
        if "LS" in s_norm: return "?"
        return "ß"
    if "KEYBOARD_NON_US_BACKSLASH_AND_PIPE" in s_norm:
        if "LS" in s_norm: return ">"
        if "RA" in s_norm: return "|"
        return "<"
    if "KEYBOARD_SLASH_AND_QUESTION_MARK" in s_norm:
        if "LS" in s_norm: return "_"
        return "-"
    if "KEYBOARD_E" in s_norm and "RA" in s_norm: return "€"
    if "KEYBOARD_Q" in s_norm and "RA" in s_norm: return "@"

    for k, v in sorted_raw_codes:
        if k in s_norm:
            return v
    return s

def classify_combo_type(k):
    if isinstance(k, str):
        if k in ["RL", "HN", "DT", "CY", "EO", "UI", "LR", "NB", "MT", "GY", "OE", "IU"] or "/" in k:
            return "bigram"
        if k in ["{", "}", "[", "]", "(", ")", "?", "<", ">", "/", "\\", "-"]:
            return "symbol"
        if k in ["Tab", "Enter", "Bspc", "Ctl+Bspc", "Esc", "Shift"]:
            return "util"
        if k in ["Unlock", "Boot", "Reset"]:
            return "system"
    return "symbol"

def apply_combo_alignment(combos):
    for c in combos:
        p = set(c["p"])
        k = c.get("k")
        c["type"] = classify_combo_type(k)
        
        # 1. Vertical Column Combos -> stay in the middle between top and home rows
        if p in [{0, 7}, {1, 8}, {2, 9}, {3, 10}, {4, 11}, {5, 12}]:
            c["align"] = "mid"
            c["offset"] = 0.0
            
        # 2. Horizontal Combos on Top Row (0..5) -> offset above the keys
        elif p.issubset({0, 1, 2, 3, 4, 5}):
            c["align"] = "top"
            if len(p) > 2:
                c["offset"] = 1.15  # Esc sits higher
            else:
                c["offset"] = 0.45  # Tab, Enter, Bspc, Ctrl+Bspc
                
        # 3. Horizontal Combos on Bottom Row (6..13) -> offset below the keys
        elif p.issubset({6, 7, 8, 9, 10, 11, 12, 13}):
            c["align"] = "bottom"
            if len(p) > 2:
                c["offset"] = 1.15  # Unlock sits lower
            elif p in [{12, 10}]:
                c["offset"] = 0.85  # Minus
            else:
                c["offset"] = 0.45  # Shift
                
        # 4. Diagonal / Cross Combos -> centered in middle
        else:
            c["align"] = "mid"
            c["offset"] = 0.0

def extract_label(key):
    if isinstance(key, dict):
        if key.get("type") in ["trans", "held"]:
            return None
        return key.get("t")
    if isinstance(key, str):
        if key in ["___", "", "None", "&trans", "&none"]:
            return None
        return key
    return None

def build_overview_layer(layers, base_layer_name="a1"):
    base_l = layers.get(base_layer_name, [])
    nav_l  = layers.get("nav", [])
    sym_l  = layers.get("sym", [])
    num_l  = layers.get("num", [])
    sym2_l = layers.get("sym2", [])

    overview = []
    for i in range(len(base_l)):
        b = base_l[i]
        base_item = dict(b) if isinstance(b, dict) else {"t": b}
        
        # Corner 1: Top-Right (Nav -> Yellow)
        nav_lbl = extract_label(nav_l[i]) if i < len(nav_l) else None
        if nav_lbl and nav_lbl != base_item.get("t"):
            base_item["tr"] = nav_lbl

        # Corner 2: Top-Left (Sym -> Cyan)
        sym_lbl = extract_label(sym_l[i]) if i < len(sym_l) else None
        if sym_lbl and sym_lbl != base_item.get("t"):
            base_item["tl"] = sym_lbl

        # Corner 3: Bottom-Left (Num -> Orange)
        num_lbl = extract_label(num_l[i]) if i < len(num_l) else None
        if num_lbl and num_lbl != base_item.get("t"):
            base_item["bl"] = num_lbl

        # Corner 4: Bottom-Right (Sym2 -> Green)
        sym2_lbl = extract_label(sym2_l[i]) if i < len(sym2_l) else None
        if sym2_lbl and sym2_lbl != base_item.get("t"):
            base_item["br"] = sym2_lbl

        overview.append(base_item)
    return overview

def build_combined_alpha_layer(layers):
    a1_l = layers.get("a1", [])
    a2_l = layers.get("a2", [])
    nav_l  = layers.get("nav", [])
    sym_l  = layers.get("sym", [])
    num_l  = layers.get("num", [])
    sym2_l = layers.get("sym2", [])

    hold_abbr_map = {
        "Shift": "Sft",
        "LEFT_SHIFT": "Sft",
        "Control": "Ctl",
        "Ctrl": "Ctl",
        "LEFT_CONTROL": "Ctl",
        "LCTRL": "Ctl",
        "Alt": "Alt",
        "LEFT_ALT": "Alt",
        "Gui": "Gui",
        "LEFT_GUI": "Gui",
        "sym": "sym",
        "sym2": "sym2",
        "num": "num"
    }

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

        # Corner 1: Top-Right (Nav -> Yellow)
        nav_lbl = extract_label(nav_l[i]) if i < len(nav_l) else None
        if nav_lbl and nav_lbl != t1:
            item["tr"] = nav_lbl

        # Corner 2: Top-Left (Sym -> Cyan)
        sym_lbl = extract_label(sym_l[i]) if i < len(sym_l) else None
        if sym_lbl and sym_lbl != t1:
            item["tl"] = sym_lbl

        # Corner 3: Bottom-Left (Num -> Orange)
        num_lbl = extract_label(num_l[i]) if i < len(num_l) else None
        if num_lbl and num_lbl != t1:
            item["bl"] = num_lbl

        # Corner 4: Bottom-Right (Sym2 -> Green)
        sym2_lbl = extract_label(sym2_l[i]) if i < len(sym2_l) else None
        if sym2_lbl and sym2_lbl != t1:
            item["br"] = sym2_lbl

        combined.append(item)
    return combined

def post_process_svg_colors(svg_path):
    with open(svg_path) as f:
        svg = f.read()

    # Style horizontal dual tap text on the same baseline (removes vertical dy stacking)
    svg = re.sub(
        r'<text([^>]*)>\s*<tspan[^>]*>([A-Za-z0-9,\.\+\-\*\/])</tspan>\s*<tspan[^>]*>/</tspan>\s*<tspan[^>]*>([A-Za-z0-9,\.\+\-\*\/])</tspan>\s*</text>',
        r'<text\1><tspan class="a1-tap">\2</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-tap">\3</tspan></text>',
        svg
    )

    # Style horizontal dual tap text if without tspans: A / B
    svg = re.sub(
        r'(<text[^>]*class="[^"]*tap[^"]*"[^>]*>)([A-Za-z0-9,\.\+\-\*\/])(\s*/\s*)([A-Za-z0-9,\.\+\-\*\/])(</text>)',
        r'\1<tspan class="a1-tap">\2</tspan><tspan class="slash-tap"> / </tspan><tspan class="a2-tap">\4</tspan>\5',
        svg
    )

    # Style bigram dual text on the same horizontal baseline: RL / LR
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

    with open(svg_path, "w") as f:
        f.write(svg)

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
            if isinstance(k, str):
                keys[i] = decode_binding(k)
            elif isinstance(k, dict) and "t" in k and isinstance(k["t"], str):
                decoded = decode_binding(k["t"])
                if isinstance(decoded, dict):
                    k.update(decoded)

    for c in d.get("combos", []):
        c["k"] = decode_combo_key(c["k"])

    # Apply vertical / horizontal combo offsets
    apply_combo_alignment(d.get("combos", []))

    yaml_out = draw_dir / "twonr9.yaml"
    with open(yaml_out, "w") as f:
        yaml.dump(d, f, sort_keys=False)

    # Step 3: Draw All-Layers SVG (2-column layout)
    svg_out = draw_dir / "twonr9.svg"
    with open(svg_out, "w") as f:
        subprocess.run(
            ["keymap", "-c", str(draw_dir / "twonr9_config.yaml"), "draw", str(yaml_out), "-j", str(config_dir / "twonr9.json")],
            stdout=f, check=True
        )

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
            ["keymap", "-c", str(draw_dir / "twonr9_config.yaml"), "draw", str(overview_yaml), "-j", str(config_dir / "twonr9.json")],
            stdout=f, check=True
        )

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
            ["keymap", "-c", str(draw_dir / "twonr9_config.yaml"), "draw", str(combined_yaml), "-j", str(config_dir / "twonr9.json")],
            stdout=f, check=True
        )
    post_process_svg_colors(combined_svg)

    print(f"Generated {svg_out}, {overview_svg}, and {combined_svg}")

if __name__ == "__main__":
    main()
