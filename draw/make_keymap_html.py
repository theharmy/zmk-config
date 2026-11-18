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
LEFT_MODS = {10: "shift", 11: "cmd", 12: "alt", 13: "ctrl"}
RIGHT_MODS = {9: "shift", 8: "cmd", 7: "alt", 6: "ctrl"}
MOD_STATE = {**LEFT_MODS, **RIGHT_MODS}
TWO_MODS = {frozenset(("shift", "cmd")): "shiftcmd",
            frozenset(("shift", "alt")): "shiftalt",
            frozenset(("shift", "ctrl")): "shiftctrl"}
STATES = ["plain", "shift", "cmd", "shiftcmd", "alt", "shiftalt", "ctrl", "shiftctrl"]
STATE_COLORS = {"plain": "#7d837d", "shift": "#3b82f6", "cmd": "#14b8a6",
                "shiftcmd": "#5fd0c0", "alt": "#f59e0b", "shiftalt": "#fbbf24",
                "ctrl": "#a855f7", "shiftctrl": "#c084fc"}
STATE_LABEL = {"plain": "Plain", "shift": "\u21e7 Shift", "cmd": "\u2318 Cmd",
               "shiftcmd": "\u21e7\u2318 Shift+Cmd", "alt": "\u2325 Alt",
               "shiftalt": "\u21e7\u2325 Shift+Alt", "ctrl": "\u2303 Ctrl",
               "shiftctrl": "\u21e7\u2303 Shift+Ctrl"}
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
        # A key is a mapping of legends, or just a string for its tap legend. A layer of nothing but
        # ▽ draws nothing -- the vim layers, transparent until they are designed -- so it is not a
        # column on the page.
        keys = [k if isinstance(k, dict) else {"t": str(k)} for k in keys]
        if all(k.get("t") == "▽" for k in keys):
            continue
        layers.append({"name": name, "keys": keys})
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


def pick_pair(pos, pairs):
    """The pair inside a chord: a two-key chord whose other keys are all mods.

    A chord can contain more than one two-key chord (10+11 is the magic-shift
    stand-in), so the first subset found is not necessarily the pair."""
    best = None
    for q in pairs:
        if set(q) <= set(pos):
            extras = [x for x in pos if x not in q]
            if len(extras) <= 2 and all(x in MOD_STATE for x in extras):
                if best is None or min(q) < min(best[0]):
                    best = (q, extras)
    return best if best else (None, [])


def build_sections(chords_list, pairs, letters):
    """Group the drawing's chords the way the layout thinks about them."""
    bigrams = bigram_pairs()
    pair_set = set(pairs)
    symbol_rows, bigram_rows, german, utility, numpad, layer_access = [], [], [], [], [], []

    for c in chords_list:
        p = tuple(c["p"])
        tap = c["k"]["tap"]
        label = tap or c["k"].get("shifted") or "\u2014"
        if c["type"] == "layer":
            layer_access.append({"label": label, "p": list(p), "state": "plain", "keys": ""})
            continue
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
        pair, extras = pick_pair(p, pairs)
        state = None
        if pair is not None:
            names = sorted(MOD_STATE[x] for x in extras)
            if not extras:
                state = "plain"
            elif len(extras) == 1 and names:
                state = names[0]
            elif len(extras) == 2 and frozenset(names) in TWO_MODS:
                state = TWO_MODS[frozenset(names)]
        if state is not None:
            symbol_rows.append({"pair": pair, "state": state, "label": label})
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
        mods = LEFT_MODS if left else RIGHT_MODS
        states_for = {state: letters[pos] for pos, state in mods.items()}
        states_for["shiftcmd"] = letters[10 if left else 9] + "+" + letters[11 if left else 8]
        states_for["shiftalt"] = letters[10 if left else 9] + "+" + letters[12 if left else 7]
        states_for["shiftctrl"] = letters[10 if left else 9] + "+" + letters[13 if left else 6]
        states_for["plain"] = ""
        pair_states[key]["_mods"] = states_for

    sections = []
    for title, chars in GROUPS:
        group_rows = []
        for pair in sorted(rows, key=lambda q: (min(q), max(q))):
            plain = rows[pair].get("plain", "")
            if not plain or plain[0] not in chars:
                continue
            mods = pair_states[",".join(map(str, pair))]["_mods"]
            hint = [{"g": glyph, "k": mods[state], "state": state}
                    for state, glyph in (("shift", "\u21e7"), ("cmd", "\u2318"),
                                         ("alt", "\u2325"), ("ctrl", "\u2303"))
                    if mods.get(state)]
            cells = [{"label": rows[pair].get(st, ""), "state": st, "p": list(pair)}
                     for st in STATES]
            group_rows.append({"pair": list(pair), "cells": cells, "hint": hint})
        if group_rows:
            sections.append({"name": title, "kind": "table", "states": STATES,
                             "rows": group_rows})

    sections += [
        {"name": "Layer access", "kind": "chips", "chips": layer_access},
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
.key.dim{opacity:.32}
.key .pilltext{text-anchor:middle;font-weight:700;font-size:15px;fill:var(--fg)}
.key .ix{fill:var(--mut);font-size:11px;opacity:.45}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:middle}
.seg button[data-s]{display:inline-flex;align-items:center}
.hint span{margin-right:4px}
.cell:hover{border-color:var(--c,var(--hlb))}
.cell.on{border-color:var(--c,var(--hlb));background:color-mix(in srgb, var(--c,#f59e0b) 18%, transparent)}
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
Each mod has a colour (Shift blue, Cmd teal, Alt amber, Ctrl purple); the Shift+mod states use a lighter shade of the same colour, and the hint beside each pair shows the key to hold. Click a chord cell (or a key)
to pick its pair: the pair's symbol for the state on screen sits above its two keys. Hover a cell to light its keys.</p>
</main>
<script>
const DATA = __DATA__;
const LAYERS = DATA.layers, GEOM = DATA.geom, SECTIONS = DATA.sections;
const BOX = DATA.box, GAP = DATA.gap, STATES = DATA.states, LABELS = DATA.state_labels;
const COLORS = DATA.state_colors, PAIRS = DATA.pair_states;
let ly = 0, st = 'plain', sel = null, pick = null, hov = null, query = '';
const $ = id => document.getElementById(id);
const E = s => String(s).replace(/[&<>"]/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));

function contrast(hex) {
  const n = parseInt(hex.slice(1), 16);
  const [r, g, b] = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map(v => {
    v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b > 0.45 ? '#1f2421' : '#ffffff';
}
function keyLabel(i) { const k = LAYERS[ly].keys[i] || {}; return k.t || k.h || String(i); }
function keyInfo(i) {
  const k = LAYERS[ly].keys[i] || {};
  return [k.t ? 'Tap ' + k.t : '', k.h ? 'Hold ' + k.h : '', k.s ? 'Shift ' + k.s : '']
    .filter(Boolean).join(' · ') || 'unbound';
}
function pairKey(p) { return p.join(','); }
const GLYPH_STATE = {'\u21e7': 'shift', '\u2318': 'cmd', '\u2325': 'alt', '\u2303': 'ctrl'};
const MODS_OF = {left: DATA.left_mods, right: DATA.right_mods};
function modPositions(p, state) {
  if (!p || state === 'plain') return [];
  const left = p.every(k => DATA.left_keys.includes(k));
  const mods = left ? MODS_OF.left : MODS_OF.right;
  if (state === 'shiftcmd') return [mods.shift, mods.cmd];
  if (state === 'shiftalt') return [mods.shift, mods.alt];
  if (state === 'shiftctrl') return [mods.shift, mods.ctrl];
  return mods[state] !== undefined ? [mods[state]] : [];
}
function pairOutput(p, state) {
  const s = PAIRS[pairKey(p)]; return s && s[state] ? s[state].label : null;
}
function output(c) {
  const k = c.k;
  if (st === 'shift') return k.shifted || k.tap;
  if (st === 'ctrl') return k.left || k.tap;
  if (st === 'quad') return k.right || k.left || k.tap;
  return k.tap;
}
function matches(text) { return !query || String(text).toLowerCase().includes(query.toLowerCase()); }
function pickSame(p, state) { return pick && pairKey(pick.p) === pairKey(p) && pick.st === state; }

function tabs() {
  $('tabs').innerHTML = LAYERS.map((l, i) =>
    `<button data-i="${i}" aria-pressed="${i === ly}">${l.name}</button>`).join('');
  $('sts').innerHTML = STATES.map(s =>
    `<button data-s="${s}" aria-pressed="${s === st}">`
    + `<span class="dot" style="background:${COLORS[s]}"></span>${LABELS[s]}</button>`).join('');
  $('ld').textContent = `${LAYERS[ly].keys.length} keys · ${LAYERS[ly].name} layer`;
}

function board() {
  const active = pick ? new Set(pick.p) : null;
  const hk = new Set(hov ? hov.p : []);
  const modKeys = new Set();
  if (pick) modPositions(pick.p, pick.st).forEach(k => modKeys.add(k));
  else if (sel !== null) {
    for (const key of Object.keys(PAIRS)) {
      const p = key.split(',').map(Number);
      if (p.includes(sel) && PAIRS[key][st] && PAIRS[key][st].label)
        modPositions(p, st).forEach(k => modKeys.add(k));
    }
  }
  const part = {};
  if (sel !== null && !pick) {
    for (const key of Object.keys(PAIRS)) {
      const p = key.split(',').map(Number);
      if (!p.includes(sel)) continue;
      const cell = PAIRS[key][st];
      if (!cell || !cell.label) continue;
      p.forEach(k => { if (k !== sel && !(k in part)) part[k] = cell.label; });
    }
  }
  let minX = 1e9, minY = 1e9, maxX = -1e9, maxY = -1e9, s = '';
  GEOM.forEach((g, i) => {
    const [x, y, w, rot, rx, ry] = g;
    const key = LAYERS[ly].keys[i] || {};
    let big = key.t || key.h || '', small = '', smallCls = 'h';
    if (key.s) { small = key.s; smallCls = 's'; } else if (key.h && key.t) { small = key.h; }
    const involved = active ? active.has(i) : false;
    const pill = involved ? pick.label : (!active && part[i]) ? part[i] : null;
    const fs = big.length > 4 ? 17 : big.length > 3 ? 19 : big.length > 2 ? 24 : big.length > 1 ? 28 : 34;
    minX = Math.min(minX, x); minY = Math.min(minY, y);
    maxX = Math.max(maxX, x + w); maxY = Math.max(maxY, y + BOX);
    s += `<g class="key${sel === i ? ' sel' : ''}${hk.has(i) ? ' hl' : ''}`
       + `${active && !involved ? ' dim' : ''}" data-k="${i}"`
       + (rot ? ` transform="rotate(${rot} ${rx} ${ry})"` : '') + '>';
    const isMod = modKeys.has(i);
    s += `<rect x="${x}" y="${y}" width="${w - GAP}" height="${BOX - GAP}" rx="13"`
       + (isMod ? ` style="stroke:${COLORS[st]};stroke-width:3.5;stroke-dasharray:8 5"` : '') + '/>';
    if (pill) {
      const tw = Math.min(w - 10, Math.max(22, pill.length * 9 + 12));
      const color = involved ? pick.color : COLORS[st];
      s += `<rect x="${x + (w - tw) / 2}" y="${y + 7}" width="${tw}" height="20" rx="10"`
         + ` style="fill:${color};opacity:0.92"/>`;
      s += `<text class="pilltext" x="${x + w / 2}" y="${y + 21}"`
         + ` style="fill:${contrast(color)}">${E(pill)}</text>`;
    }
    s += `<text class="t" x="${x + w / 2}" y="${y + (small ? 58 : 66)}" font-size="${fs}">${E(big)}</text>`;
    if (small) {
      const tint = GLYPH_STATE[small];
      s += `<text class="${smallCls}" x="${x + w / 2}" y="${y + 86}"`
        + (tint ? ` style="fill:${COLORS[tint]}"` : '') + `>${E(small)}</text>`;
    }
    s += `<text class="ix" x="${x + w - 13}" y="${y + BOX - 9}">${i}</text>`;
    s += '</g>';
  });
  const pad = 14;
  $('bd').setAttribute('viewBox', `${minX - pad} ${minY - pad} ${maxX - minX + 2 * pad} ${maxY - minY + 2 * pad}`);
  $('bd').innerHTML = s;
}

function pairLabel(p) { return p.map(keyLabel).join(' + '); }

function cellButton(cell) {
  if (!cell.label || !matches(cell.label)) return '<td><span class="cell empty">—</span></td>';
  const on = pickSame(cell.p, cell.state) ? ' on' : '';
  return `<td><button class="cell${on}" style="--c:${COLORS[cell.state]}"`
       + ` data-p='${JSON.stringify(cell.p)}' data-l="${E(cell.label)}" data-st="${cell.state}"`
       + ` title="${E(pairLabel(cell.p))} · ${LABELS[cell.state]}">${E(cell.label)}</button></td>`;
}

function sections() {
  let out = '';
  SECTIONS.forEach(section => {
    if (section.kind === 'table') {
      const rows = section.rows.filter(row => (sel === null || row.pair.includes(sel))
        && row.cells.some(c => c.label && matches(c.label)));
      if (!rows.length) return;
      out += `<h2>${E(section.name)} · ${rows.length}${sel !== null ? ' for key ' + sel : ''}</h2>`
        + '<table class="chords"><thead><tr><th>keys</th>'
        + section.states.map(s => `<th><span class="dot" style="background:${COLORS[s]}"></span>${E(LABELS[s])}</th>`).join('')
        + '</tr></thead><tbody>';
      rows.forEach(row => {
        const hint = (row.hint || []).map(h =>
          `<span style="color:${COLORS[h.state]}">${E(h.g)}${E(h.k)}</span>`).join('');
        out += `<tr><td class="keys">${E(pairLabel(row.pair))}`
          + (hint ? `<div class="hint">${hint}</div>` : '') + '</td>'
          + row.cells.map(cellButton).join('') + '</tr>';
      });
      out += '</tbody></table>';
    } else {
      const chips = section.chips.filter(c => (sel === null || c.p.includes(sel)) && matches(c.label));
      if (!chips.length) return;
      out += `<h2>${E(section.name)} · ${chips.length}${sel !== null ? ' for key ' + sel : ''}</h2><div class="cs">`;
      chips.forEach(c => {
        const on = pickSame(c.p, 'plain') ? ' on' : '';
        out += `<button class="chip${on}" style="--c:${COLORS.plain}"`
          + ` data-p='${JSON.stringify(c.p)}' data-l="${E(c.label)}" data-st="plain">`
          + `<span class="ks">${E(c.p.map(keyLabel).join('+'))}</span><b>${E(c.label)}</b></button>`;
      });
      out += '</div>';
    }
  });
  $('sections').innerHTML = out || '<p class="mut">Nothing matches.</p>';
}

function info() {
  let h = 'Click a key for its chords; click a chord cell or chip to show what that chord types.';
  if (pick) {
    h = `<b>${E(pick.label)}</b><span class="o">${E(LABELS[pick.st])}</span>`
      + `<span class="o">keys ${E(pairLabel(pick.p))}</span>`;
  } else if (sel !== null) {
    const n = Object.keys(PAIRS).filter(k => k.split(',').map(Number).includes(sel)
      && PAIRS[k][st] && PAIRS[k][st].label).length;
    h = `<b>Key ${sel}</b> · ${E(keyInfo(sel))}`
      + `<span class="o">${n} chord${n === 1 ? '' : 's'} in ${E(LABELS[st])}</span>`;
  }
  $('info').innerHTML = h;
}

function meta() {
  $('meta').textContent = `${DATA.title} · ${LAYERS.length} layers · ${DATA.layer_chords.length} chords · `
    + `combo window ${DATA.combo_term} ms · drawn from ${DATA.source}`;
}

function hash() {
  location.hash = 'L' + ly + (sel !== null && !pick ? '&k=' + sel : '')
    + (pick ? '&c=' + pairKey(pick.p) + '&s=' + pick.st : '');
}

function render() { tabs(); board(); sections(); info(); meta(); }

$('tabs').onclick = e => { const b = e.target.closest('[data-i]'); if (b) { ly = +b.dataset.i; sel = pick = hov = null; hash(); render(); } };
$('sts').onclick = e => { const b = e.target.closest('[data-s]'); if (b) { st = b.dataset.s; if (pick) { pick.st = st; pick.color = COLORS[st]; } hash(); render(); } };
$('q').oninput = e => { query = e.target.value; sections(); };
$('bd').onclick = e => {
  const g = e.target.closest('[data-k]'); if (!g) return;
  const k = +g.dataset.k;
  if (pick && pick.p.includes(k)) { pick = null; sel = null; }
  else { sel = sel === k ? null : k; pick = null; }
  hash(); render();
};
$('sections').onmouseover = e => {
  const b = e.target.closest('[data-p]'); if (!b) return;
  hov = {p: JSON.parse(b.dataset.p)}; board();
};
$('sections').onmouseout = e => { if (e.target.closest('[data-p]')) { hov = null; board(); } };
$('sections').onclick = e => {
  const b = e.target.closest('[data-p]'); if (!b) return;
  const p = JSON.parse(b.dataset.p), state = b.dataset.st || 'plain';
  if (pickSame(p, state)) pick = null;
  else pick = {p, st: state, label: b.dataset.l, color: COLORS[state]};
  sel = null;
  hash(); render();
};
// #L0&c=1,6&s=shiftalt picks a chord and state; #L0&k=6 picks a key.
{
  const m = location.hash.match(/^#L([0-9]+)(?:&k=([0-9]+))?(?:&c=([0-9,]+))?(?:&s=([a-z]+))?$/);
  if (m) {
    ly = Math.min(+m[1], LAYERS.length - 1);
    if (m[2]) sel = +m[2];
    if (m[4] && STATES.includes(m[4])) st = m[4];
    if (m[3]) {
      const p = m[3].split(',').map(Number), state = st;
      const label = state === 'plain'
        ? (LAYERS[ly].keys[p[0]] || {}).t && pairOutput(p, state)
        : pairOutput(p, state);
      pick = {p, st: state, label: pairOutput(p, state) || (DATA.layer_chords.find(c => pairKey(c.p) === pairKey(p)) || {}).k?.tap || '', color: COLORS[state]};
    }
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
        "left_mods": {state: pos for pos, state in LEFT_MODS.items()},
        "right_mods": {state: pos for pos, state in RIGHT_MODS.items()},
        "states": STATES,
        "state_labels": STATE_LABEL,
        "state_colors": STATE_COLORS,
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
