#!/usr/bin/env python3
"""Draw the current keymap as one self-contained HTML page.

Everything comes from the drawing (draw/twonr9_srht.yaml: layers, chords, the
layout it names), the layout geometry (config/twonr9.json) and the bigram chords
(config/twonr9_combos_srht.dtsi), so the page follows the keymap instead of
drifting from it.

    python3 draw/make_keymap_html.py            # writes draw/twonr9_keymap.html
    python3 draw/make_keymap_html.py -o /tmp/k.html

No dependencies beyond PyYAML, no network, no build step: open the file in a
browser.
"""
import argparse
import html
import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DRAWING = HERE / "twonr9_srht.yaml"
LAYOUT = ROOT / "config/twonr9.json"
BIGRAMS = ROOT / "config/twonr9_combos_srht.dtsi"
OUT = HERE / "twonr9_keymap.html"

BOX = 92          # key face, px
GAP = 4
SCALE = 100       # layout units -> px

# A chord's mod comes from the hand opposite its pair: a left-hand pair takes the
# right-hand mods (10-13), a right-hand pair the left-hand ones (6-9).
MOD_STATE = {10: "shift", 11: "cmd", 12: "alt", 13: "ctrl",
             9: "shift", 8: "cmd", 7: "alt", 6: "ctrl"}
STATES = ["plain", "shift", "ctrl", "cmd", "alt", "quad"]
STATE_LABEL = {"plain": "Plain", "shift": "\u21e7 Shift", "ctrl": "\u2303 Ctrl",
               "cmd": "\u2318 Cmd", "alt": "\u2325 Alt", "quad": "\u21e7\u2318 Shift+Cmd"}
UMlAUT_POSITIONS = {(4, 16), (5, 16), (10, 16), (13, 16)}
ACUTE = (6, 7)
LEFT_KEYS = {0, 1, 2, 6, 7, 8, 9}
# Pairs are grouped by the first character of their plain legend.
GROUPS = [("Brackets & comparisons", "([{<"),
          ("Arithmetic", "-=*%/"),
          ("Punctuation", ",;"),
          ("Logic & symbols", "&$@!"),
          ("Quoting & LaTeX", '"`\\')]


def load(drawing):
    d = yaml.safe_load(Path(drawing).read_text(encoding="utf-8"))
    layout_ref = (d.get("layout") or {}).get("qmk_info_json")
    if not layout_ref:
        raise SystemExit(f"{drawing}: no layout: qmk_info_json to take the geometry from")
    layout_path = (Path(drawing).resolve().parent / layout_ref).resolve()
    layout = json.loads(layout_path.read_text(encoding="utf-8"))
    geom = next(iter(layout["layouts"].values()))["layout"]
    return d, geom, layout_path


def geometry(geom):
    """Each key: (x, y, w, rotation, rot_center_x, rot_center_y), in px."""
    out = []
    for key in geom:
        out.append((round(float(key.get("x", 0)) * SCALE),
                    round(float(key.get("y", 0)) * SCALE),
                    round(float(key.get("w", 1)) * SCALE),
                    key.get("r"),
                    round(float(key.get("rx", 0)) * SCALE),
                    round(float(key.get("ry", 0)) * SCALE)))
    return out


def legends(drawing):
    layers = []
    for name, keys in drawing["layers"].items():
        # A key is a mapping of legends, or just a string for its tap legend.
        layers.append({"name": name,
                       "keys": [k if isinstance(k, dict) else {"t": str(k)} for k in keys]})
    return layers


def chords(drawing):
    out = []
    for combo in drawing.get("combos") or []:
        key = combo.get("k")
        if isinstance(key, dict):
            legend = {"tap": key.get("t", ""), "shifted": key.get("s", ""),
                      "hold": key.get("h", ""), "left": key.get("left", ""),
                      "right": key.get("right", "")}
        else:
            legend = {"tap": key or "", "shifted": "", "hold": "", "left": "", "right": ""}
        out.append({"p": sorted(combo.get("p") or []), "l": combo.get("l") or [],
                    "type": combo.get("type") or "", "k": legend})
    return out


def bigram_pairs():
    """The 12 bigram chords: positions -> the layer they fire on."""
    if not BIGRAMS.is_file():
        return {}
    text = BIGRAMS.read_text(encoding="utf-8")
    out = {}
    for a, b, layer in re.findall(r"ZMK_COMBO\(combo_\w+,\s*&macro_\w+,\s*(\d+)\s+(\d+),\s*L_A(\d)\)", text):
        out.setdefault((min(int(a), int(b)), max(int(a), int(b))), set()).add(int(layer))
    return out


def build_sections(chords_list, pairs, letters):
    """Group the drawing's chords the way the layout thinks about them."""
    bigrams = bigram_pairs()
    pair_set = set(pairs)
    symbol_rows, bigram_rows, german, utility, numpad = [], [], [], [], []

    for c in chords_list:
        p = tuple(c["p"])
        tap = c["k"]["tap"]
        label = tap or c["k"].get("shifted") or "\u2014"
        if len(p) == 1:
            utility.append({"label": label, "p": list(p), "state": "plain", "keys": ""})
            continue
        if 16 in p or p == ACUTE:
            german.append({"label": label, "p": list(p), "state": "plain", "keys": ""})
            continue
        if set(c["l"]) == {"num"}:
            numpad.append({"label": label, "p": list(p), "state": "plain", "keys": ""})
            continue
        if p in bigrams:
            where = " \u00b7 ".join(f"a{n}" for n in sorted(bigrams[p]))
            bigram_rows.append({"label": label, "p": list(p), "state": "plain", "keys": where})
            continue
        if c["type"] == "util":
            utility.append({"label": label, "p": list(p), "state": "plain", "keys": ""})
            continue
        if len(p) == 2 and p in pair_set:
            symbol_rows.append({"pair": p, "state": "plain", "label": label})
        elif len(p) == 3:
            pair = next((q for q in pairs if set(q) <= set(p)), None)
            mod = next((x for x in p if pair is None or x not in pair), None)
            if pair and mod in MOD_STATE:
                symbol_rows.append({"pair": pair, "state": MOD_STATE[mod], "label": label})
            else:
                utility.append({"label": label, "p": list(p), "state": "plain", "keys": ""})
        elif len(p) == 4 and {10, 11} <= set(p):
            pair = tuple(x for x in p if x not in (10, 11))
            symbol_rows.append({"pair": pair, "state": "quad", "label": label})
        else:
            utility.append({"label": label, "p": list(p), "state": "plain", "keys": ""})

    rows = {}
    for entry in symbol_rows:
        rows.setdefault(entry["pair"], {})[entry["state"]] = entry["label"]
    # A pair with a single state is not a family of chords but a utility chord
    # (the home-row `_ - : ;` pairs): list it with the utilities, not as a row.
    for pair in [q for q, states in rows.items() if list(states) == ["plain"]]:
        utility.append({"label": rows[pair]["plain"], "p": list(pair),
                        "state": "plain", "keys": ""})
        del rows[pair]

    pair_states = {}
    for pair, states in rows.items():
        key = ",".join(str(p) for p in pair)
        pair_states[key] = {st: {"label": lab, "p": list(pair)} for st, lab in states.items()}
        # The mod key for each state, as the letter printed on the a1 layer.
        left = all(p in LEFT_KEYS for p in pair)
        mods = {p: MOD_STATE[p] for p in (range(10, 14) if left else range(6, 10))}
        states_for = {MOD_STATE[p]: letters[p] for p in mods}
        states_for["quad"] = letters[10] + "+" + letters[11] if left else ""
        pair_states[key]["_mods"] = states_for

    sections = []
    for title, chars in GROUPS:
        group_rows = []
        for pair in sorted(rows, key=lambda q: (min(q), max(q))):
            plain = rows[pair].get("plain", "")
            if not plain or plain[0] not in chars:
                continue
            mods = pair_states[",".join(map(str, pair))]["_mods"]
            hint = " ".join(
                f"{glyph}{mods[state]}"
                for state, glyph in (("shift", "\u21e7"), ("ctrl", "\u2303"),
                                     ("cmd", "\u2318"), ("alt", "\u2325"))
                if mods.get(state))
            cells = [{"label": rows[pair].get(st, ""), "state": st, "p": list(pair)}
                     for st in STATES]
            group_rows.append({"pair": list(pair), "cells": cells, "hint": hint})
        if group_rows:
            sections.append({"name": title, "kind": "table", "states": STATES,
                             "rows": group_rows})

    sections += [
        {"name": "Bigrams", "kind": "chips", "chips": bigram_rows},
        {"name": "German", "kind": "chips", "chips": german},
        {"name": "Utilities & shifts", "kind": "chips", "chips": utility},
        {"name": "Numpad", "kind": "chips", "chips": numpad},
    ]
    return [s for s in sections if s.get("rows") or s.get("chips")], pair_states


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--bg:#faf9f5;--fg:#1f2421;--mut:#6c736e;--key:#fff;--bd:#d8d5ca;--acc:#2b7a68;
 --sel:#dff0ea;--hl:#ffeccb;--hlb:#c98a2b;--sh:#8a5a12;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#1a1d1b;--fg:#ecebe4;--mut:#9ca59e;--key:#272b28;
 --bd:#41463f;--acc:#62c6ab;--sel:#223d37;--hl:#463818;--hlb:#e0a35c;--sh:#d9a45c;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 ui-sans-serif,system-ui,"Segoe UI",Roboto,sans-serif}
main{max-width:1180px;margin:0 auto;padding:20px 16px 48px}
h1{font-size:22px;margin:0}
h2{font-size:13px;letter-spacing:.07em;text-transform:uppercase;color:var(--mut);margin:26px 0 8px}
.sub{color:var(--mut);margin:2px 0 12px;font-size:13px}
.bar{display:flex;flex-wrap:wrap;gap:8px 18px;margin-bottom:10px;align-items:center}
.seg{display:inline-flex;border:1px solid var(--bd);border-radius:10px;overflow:hidden;max-width:100%;overflow-x:auto}
.seg button{border:0;background:transparent;color:var(--fg);padding:7px 13px;font:inherit;cursor:pointer;white-space:nowrap}
.seg button[aria-pressed=true]{background:var(--acc);color:var(--bg)}
input[type=search]{font:inherit;color:var(--fg);background:var(--key);border:1px solid var(--bd);border-radius:10px;padding:7px 11px;min-width:240px}
.wrap{overflow-x:auto;border:1px solid var(--bd);border-radius:14px;padding:6px}
svg{display:block;min-width:760px;width:100%}
.key rect{fill:var(--key);stroke:var(--bd);stroke-width:2;cursor:pointer}
.key:hover rect{stroke:var(--acc)}
.key.sel rect{fill:var(--sel);stroke:var(--acc);stroke-width:4}
.key.hl rect{fill:var(--hl);stroke:var(--hlb);stroke-width:4}
.key text{text-anchor:middle;fill:var(--fg);pointer-events:none}
.key text.t{font-weight:600}
.key text.h{fill:var(--mut);font-size:20px}
.key text.s{fill:var(--sh);font-size:20px}
.key text.ix{fill:var(--mut);font-size:13px;opacity:.5}
#info{min-height:24px;margin:12px 0;padding:10px 14px;border:1px solid var(--bd);border-radius:12px;background:var(--key)}
#info .o{margin-left:12px;white-space:nowrap}
#info b,.cell b,.chip b{font-family:ui-monospace,Menlo,Consolas,monospace}
table.chords{border-collapse:collapse;width:100%;font-size:14px}
table.chords th{font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--mut);
 text-align:left;font-weight:600;padding:4px 6px;border-bottom:1px solid var(--bd)}
table.chords td{padding:2px 4px;border-bottom:1px solid var(--bd)}
table.chords td.keys{color:var(--mut);font-size:12px;white-space:nowrap}
.hint{font-size:11px;color:var(--mut);opacity:.8;margin-top:2px}
.cell{border:1px solid transparent;background:transparent;color:var(--fg);font:inherit;cursor:pointer;
 border-radius:8px;padding:4px 8px;min-width:52px;text-align:left}
.cell:hover{border-color:var(--hlb);background:var(--hl)}
.cell.on{border-color:var(--hlb);background:var(--hl)}
.cell.empty{color:var(--mut);cursor:default}
.cell.empty:hover{background:transparent;border-color:transparent}
.cs{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;gap:8px;align-items:baseline;border:1px solid var(--bd);background:var(--key);
 color:var(--fg);border-radius:10px;padding:6px 10px;font:inherit;cursor:pointer}
.chip:hover,.chip.on{border-color:var(--hlb);background:var(--hl)}
.chip .ks{color:var(--mut);font-size:12px}
.mut{color:var(--mut)}
</style>
</head>
<body>
<main>
<h1>__TITLE__</h1>
<p class="sub" id="meta"></p>
<div class="bar"><div class="seg" id="tabs"></div><div class="seg" id="sts"></div>
<input type="search" id="q" placeholder="search an output (e.g. ==, MB1, ß)"></div>
<p class="sub" id="ld"></p>
<div class="wrap"><svg id="bd" role="img" aria-label="keyboard"></svg></div>
<div id="info"></div>
<div id="sections"></div>
<p class="sub">Big legend = tap; small grey = hold; small amber = shifted. Faint number = key position.
The state buttons are the chord states: Shift, Ctrl, Cmd, Alt and Shift+Cmd. Click a chord cell (or a key)
to pick its pair: the pair's symbol for the state on screen sits above its two keys. Hover a cell to light its keys.</p>
</main>
<script>
const DATA = __DATA__;
const LAYERS = DATA.layers, GEOM = DATA.geom, SECTIONS = DATA.sections;
const BOX = DATA.box, GAP = DATA.gap, STATES = DATA.states, LABELS = DATA.state_labels;
const PAIRS = DATA.pair_states, LEFT = new Set(DATA.left_keys);
let ly = 0, st = 'plain', sel = null, pair = null, hov = null, pin = null, query = '';
const $ = id => document.getElementById(id);
const E = s => String(s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));

function keyLabel(i) { const k = LAYERS[ly].keys[i] || {}; return k.t || k.h || String(i); }
function keyInfo(i) {
  const k = LAYERS[ly].keys[i] || {};
  return [k.t ? 'Tap ' + k.t : '', k.h ? 'Hold ' + k.h : '', k.s ? 'Shift ' + k.s : '']
    .filter(Boolean).join(' · ') || 'unbound';
}
function onLayer(c) { return !c.l || c.l.includes(LAYERS[ly].name); }
function pairKey(p) { return p.join(','); }
function pairStates(p) { return PAIRS[pairKey(p)] || null; }
function pairOutput(p, state) {
  const s = pairStates(p); if (!s || !s[state]) return null;
  return s[state].label;
}
function output(c) {
  const k = c.k;
  if (st === 'shift') return k.shifted || k.tap;
  if (st === 'ctrl') return k.left || k.tap;
  if (st === 'quad') return k.right || k.left || k.tap;
  return k.tap;
}
function matches(text) { return !query || String(text).toLowerCase().includes(query.toLowerCase()); }

function tabs() {
  $('tabs').innerHTML = LAYERS.map((l, i) =>
    `<button data-i="${i}" aria-pressed="${i === ly}">${l.name}</button>`).join('');
  $('sts').innerHTML = STATES.map(s =>
    `<button data-s="${s}" aria-pressed="${s === st}">${LABELS[s]}</button>`).join('');
  $('ld').textContent = `${LAYERS[ly].keys.length} keys · ${LAYERS[ly].name} layer`;
}

function board() {
  const hk = new Set(hov ? hov.p : []);
  const part = {};
  if (sel !== null) {
    DATA.layer_chords.filter(c => onLayer(c) && c.p.includes(sel))
      .sort((a, b) => a.p.length - b.p.length)
      .forEach(c => c.p.forEach(p => { if (p !== sel && !(p in part)) part[p] = output(c); }));
  }
  let minX = 1e9, minY = 1e9, maxX = -1e9, maxY = -1e9, s = '';
  GEOM.forEach((g, i) => {
    const [x, y, w, rot, rx, ry] = g;
    const key = LAYERS[ly].keys[i] || {};
    let big = key.t || key.h || '', small = '', smallCls = 'h';
    if (key.s) { small = key.s; smallCls = 's'; } else if (key.h && key.t) { small = key.h; }
    const pill = pair && pair.includes(i) ? pairOutput(pair, st) || part[i] : part[i];
    const fs = big.length > 4 ? 17 : big.length > 3 ? 19 : big.length > 2 ? 24 : big.length > 1 ? 28 : 34;
    minX = Math.min(minX, x); minY = Math.min(minY, y);
    maxX = Math.max(maxX, x + w); maxY = Math.max(maxY, y + BOX);
    s += `<g class="key${i === sel ? ' sel' : ''}${hk.has(i) ? ' hl' : ''}" data-k="${i}"`
       + (rot ? ` transform="rotate(${rot} ${rx} ${ry})"` : '') + '>';
    s += `<rect x="${x}" y="${y}" width="${w - GAP}" height="${BOX - GAP}" rx="13"/>`;
    s += `<text class="ix" x="${x + 13}" y="${y + 20}">${i}</text>`;
    if (pill) s += `<text class="s" x="${x + w / 2}" y="${y + 22}">${E(pill)}</text>`;
    s += `<text class="t" x="${x + w / 2}" y="${y + (small ? 58 : 66)}" font-size="${fs}">${E(big)}</text>`;
    if (small) s += `<text class="${smallCls}" x="${x + w / 2}" y="${y + 86}">${E(small)}</text>`;
    s += '</g>';
  });
  const pad = 14;
  $('bd').setAttribute('viewBox', `${minX - pad} ${minY - pad} ${maxX - minX + 2 * pad} ${maxY - minY + 2 * pad}`);
  $('bd').innerHTML = s;
}

function pairLabel(p) { return p.map(keyLabel).join(' + '); }

function cellButton(cell) {
  const p = JSON.stringify(cell.p);
  if (!cell.label || !matches(cell.label)) return '<td><span class="cell empty">—</span></td>';
  const on = pair && pairKey(cell.p) === pairKey(pair) && st === cell.state ? ' on' : '';
  return `<td><button class="cell${on}" data-p='${p}' data-l="${E(cell.label)}" data-st="${cell.state}"`
       + ` title="${E(pairLabel(cell.p))} · ${LABELS[cell.state]}">${E(cell.label)}</button></td>`;
}

function sections() {
  let out = '';
  SECTIONS.forEach(section => {
    if (section.kind === 'table') {
      const rows = section.rows.filter(row => row.cells.some(c => c.label && matches(c.label)));
      if (!rows.length) return;
      out += `<h2>${E(section.name)} · ${rows.length}</h2><table class="chords"><thead><tr><th>keys</th>`
        + section.states.map(s => `<th>${E(LABELS[s])}</th>`).join('') + '</tr></thead><tbody>';
      rows.forEach(row => {
        out += `<tr><td class="keys">${E(pairLabel(row.pair))}`
          + (row.hint ? `<div class="hint">${E(row.hint)}</div>` : '') + '</td>'
          + row.cells.map(cellButton).join('') + '</tr>';
      });
      out += '</tbody></table>';
    } else {
      const chips = section.chips.filter(c => matches(c.label));
      if (!chips.length) return;
      out += `<h2>${E(section.name)} · ${chips.length}</h2><div class="cs">`;
      chips.forEach(c => {
        out += `<button class="chip" data-p='${JSON.stringify(c.p)}' data-l="${E(c.label)}" data-st="plain">`
          + `<span class="ks">${E(c.p.map(keyLabel).join('+'))}</span><b>${E(c.label)}</b></button>`;
      });
      out += '</div>';
    }
  });
  $('sections').innerHTML = out || '<p class="mut">Nothing matches.</p>';
}

function info() {
  let h = 'Click a key for its legends; click a chord cell to show that pair in that state.';
  if (sel !== null) h = `<b>Key ${sel}</b> · ${E(keyInfo(sel))}`;
  if (pair) {
    const out = pairOutput(pair, st);
    h = `<b>${E(pairLabel(pair))}</b><span class="o">${E(LABELS[st])}</span>`
      + (out ? `<span class="o">produces <b>${E(out)}</b></span>` : '<span class="mut"> · not defined in this state</span>');
  } else if (hov) {
    h = `<b>${E(hov.label)}</b><span class="o">${E(LABELS[hov.st])}</span>`
      + `<span class="o">keys ${E(hov.p.map(keyLabel).join(' + '))}</span>`;
  }
  $('info').innerHTML = h;
}

function meta() {
  $('meta').textContent = `${DATA.title} · ${LAYERS.length} layers · ${DATA.layer_chords.length} chords · `
    + `combo window ${DATA.combo_term} ms · drawn from ${DATA.source}`;
}

function hash() {
  location.hash = 'L' + ly + (pair ? '&p=' + pairKey(pair) + '&s=' + st : '');
}

function render() { tabs(); board(); sections(); info(); meta(); }

$('tabs').onclick = e => { const b = e.target.closest('[data-i]'); if (b) { ly = +b.dataset.i; sel = pair = hov = pin = null; hash(); render(); } };
$('sts').onclick = e => { const b = e.target.closest('[data-s]'); if (b) { st = b.dataset.s; hash(); render(); } };
$('q').oninput = e => { query = e.target.value; sections(); };
$('bd').onclick = e => {
  const g = e.target.closest('[data-k]'); if (!g) return;
  const k = +g.dataset.k; sel = sel === k ? null : k;
  if (sel === null) { pair = null; }
  else {
    const found = Object.keys(PAIRS).map(s => s.split(',').map(Number)).find(p => p.includes(k));
    pair = found || null;
  }
  hash(); render();
};
$('sections').onmouseover = e => {
  const b = e.target.closest('[data-p]'); if (!b) return;
  hov = {p: JSON.parse(b.dataset.p), label: b.dataset.l, st: b.dataset.st}; board(); info();
};
$('sections').onmouseout = e => { if (e.target.closest('[data-p]')) { hov = null; board(); info(); } };
$('sections').onclick = e => {
  const b = e.target.closest('[data-p]'); if (!b) return;
  const p = JSON.parse(b.dataset.p);
  if (pair && pairKey(p) === pairKey(pair) && st === b.dataset.st) { pair = null; }
  else { pair = p; st = b.dataset.st; sel = null; }
  hash(); render();
};
// #L3&p=1,9&s=ctrl opens on a layer with a pair and state selected.
{
  const m = location.hash.match(/^#L([0-9]+)(?:&p=([0-9,]+))?(?:&s=([a-z]+))?$/);
  if (m) {
    ly = Math.min(+m[1], LAYERS.length - 1);
    if (m[2]) pair = m[2].split(',').map(Number);
    if (m[3] && STATES.includes(m[3])) st = m[3];
  }
}
render();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--drawing", default=str(DRAWING), help="the drawing YAML to read")
    ap.add_argument("-o", "--output", default=str(OUT), help="the HTML file to write")
    args = ap.parse_args()

    drawing, geom, layout_path = load(args.drawing)
    layer_list = legends(drawing)
    chord_list = chords(drawing)
    pairs = [tuple(c["p"]) for c in chord_list
             if len(c["p"]) == 2 and 16 not in c["p"] and tuple(c["p"]) != ACUTE]
    letters = [k.get("t", "") for k in layer_list[0]["keys"]]
    sections, pair_states = build_sections(chord_list, pairs, letters)
    data = {
        "title": drawing.get("title") or Path(args.drawing).stem,
        "source": f"{Path(args.drawing).name} + {Path(layout_path).name}",
        "combo_term": 0,
        "layers": layer_list,
        "geom": geometry(geom),
        "layer_chords": chord_list,
        "sections": sections,
        "pair_states": pair_states,
        "left_keys": sorted(LEFT_KEYS),
        "states": STATES,
        "state_labels": STATE_LABEL,
        "box": BOX,
        "gap": GAP,
    }
    cfg = Path.home() / ".config/zmk-layer-hud/config.yaml"
    if cfg.is_file():
        hud = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
        data["combo_term"] = int(hud.get("combo_term_ms") or 0)

    keys = len(data["geom"])
    for layer in data["layers"]:
        if len(layer["keys"]) != keys:
            raise SystemExit(f"layer {layer['name']} has {len(layer['keys'])} keys, the layout {keys}")
    for chord in data["layer_chords"]:
        for p in chord["p"]:
            if not 0 <= p < keys:
                raise SystemExit(f"chord {chord['p']} names key {p}, the layout has {keys}")

    page = PAGE.replace("__TITLE__", html.escape(data["title"]))
    page = page.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    Path(args.output).write_text(page, encoding="utf-8")
    symbol_pairs = sum(len(s["rows"]) for s in data["sections"] if s["kind"] == "table")
    print(f"{args.output}: {len(data['layers'])} layers, {len(data['layer_chords'])} chords, "
          f"{symbol_pairs} symbol pairs in {sum(1 for s in data['sections'] if s['kind'] == 'table')} groups, {keys} keys")


if __name__ == "__main__":
    main()
