import type { KeyDefinition } from './types';

export const TWO_NR9_KEYS: KeyDefinition[] = [
  // Left Top Row (0, 1, 2)
  { id: 0, label: '0', hand: 'left', row: 'top', defaultLayerKey: { a1: 'L', a2: 'X', subLabel: '!', nav: 'LALT', sym: '!', fn: 'F1', num: '-' } },
  { id: 1, label: '1', hand: 'left', row: 'top', defaultLayerKey: { a1: 'N', a2: 'B', subLabel: '#', nav: 'LGUI', sym: '#', fn: 'F2', num: '*' } },
  { id: 2, label: '2', hand: 'left', row: 'top', defaultLayerKey: { a1: 'D', a2: 'M', subLabel: '$', nav: 'LSHFT', sym: '$', fn: 'F3', num: '=' } },

  // Right Top Row (3, 4, 5)
  { id: 3, label: '3', hand: 'right', row: 'top', defaultLayerKey: { a1: 'Y', a2: 'W', subLabel: '(', nav: '←', sym: '(', fn: 'F8', num: '4' } },
  { id: 4, label: '4', hand: 'right', row: 'top', defaultLayerKey: { a1: 'O', a2: 'Q', subLabel: ')', nav: '↓', sym: ')', fn: 'F9', num: '5' } },
  { id: 5, label: '5', hand: 'right', row: 'top', defaultLayerKey: { a1: 'U', a2: ',', subLabel: ';', nav: '↑', sym: ';', fn: 'F10', num: '6' } },

  // Left Home Row (6, 7, 8, 9)
  { id: 6, label: '6', hand: 'left', row: 'home', defaultLayerKey: { a1: 'S', a2: 'F', subLabel: '`', nav: 'LCTRL', sym: '`', fn: 'F4', num: '+' } },
  { id: 7, label: '7', hand: 'left', row: 'home', defaultLayerKey: { a1: 'R', a2: 'V', subLabel: '_', nav: '⌘Q', sym: '_', fn: 'F5', num: '%' } },
  { id: 8, label: '8', hand: 'left', row: 'home', defaultLayerKey: { a1: 'H', a2: 'P', subLabel: '&', nav: '⌘⇥', sym: '&', fn: 'F6', num: '/' } },
  { id: 9, label: '9', hand: 'left', row: 'home', defaultLayerKey: { a1: 'T', a2: 'K', subLabel: '|', nav: '⇹', sym: '|', fn: 'F7', num: 'comma' } },

  // Right Home Row (10, 11, 12, 13)
  { id: 10, label: '10', hand: 'right', row: 'home', defaultLayerKey: { a1: 'C', a2: 'G', subLabel: '[', nav: 'niri', sym: '[', fn: 'F11', num: '1' } },
  { id: 11, label: '11', hand: 'right', row: 'home', defaultLayerKey: { a1: 'E', a2: 'J', subLabel: ']', nav: 'PgDn', sym: ']', fn: 'F12', num: '2' } },
  { id: 12, label: '12', hand: 'right', row: 'home', defaultLayerKey: { a1: 'I', a2: '.', subLabel: ':', nav: 'PgUp', sym: ':', fn: 'Vol-', num: '3' } },
  { id: 13, label: '13', hand: 'right', row: 'home', defaultLayerKey: { a1: 'A', a2: 'Z', subLabel: '"', nav: '→', sym: '"', fn: 'Vol+', num: '0' } },

  // Left Thumbs (14, 15)
  { id: 14, label: '14', hand: 'left', row: 'thumb', defaultLayerKey: { a1: 'A2', a2: 'to A1', subLabel: 'a2', nav: '___', sym: '___', fn: '___', num: '___' } },
  { id: 15, label: '15', hand: 'left', row: 'thumb', defaultLayerKey: { a1: 'SPC/NAV', a2: 'SPC/NAV', subLabel: 'nav', nav: 'to A1', sym: 'to A1', fn: 'to A1', num: 'to A1' } },

  // Right Thumbs (16, 17)
  { id: 16, label: '16', hand: 'right', row: 'thumb', defaultLayerKey: { a1: 'SHIFT', a2: 'SHIFT', subLabel: 'shift', nav: 'SHIFT', sym: 'SHIFT', fn: 'SHIFT', num: 'SHIFT' } },
  { id: 17, label: '17', hand: 'right', row: 'thumb', defaultLayerKey: { a1: 'NUM', a2: 'NUM', subLabel: 'num', nav: 'NUM', sym: 'NUM', fn: 'NUM', num: 'NUM' } },
];

export interface ComboInfo {
  id: string;
  keys: number[];
  output: string;
  name: string;
  category: 'ortho' | 'symbol' | 'nav';
}

export const COMBOS: ComboInfo[] = [
  { id: 'combo_sz', keys: [6, 7], output: 'ß', name: 'Eszett (S + R)', category: 'ortho' },
  { id: 'combo_under', keys: [7, 8], output: '_', name: 'Underscore', category: 'symbol' },
  { id: 'combo_minus', keys: [8, 9], output: '-', name: 'Hyphen / Minus', category: 'symbol' },
  { id: 'combo_colon', keys: [10, 11], output: ':', name: 'Colon', category: 'symbol' },
  { id: 'combo_semi', keys: [11, 12], output: ';', name: 'Semicolon', category: 'symbol' },
  { id: 'combo_tab', keys: [0, 1], output: '\t', name: 'Tab', category: 'nav' },
  { id: 'combo_rtn', keys: [1, 2], output: '\n', name: 'Enter', category: 'nav' },
  { id: 'combo_bspc', keys: [3, 4], output: '⌫', name: 'Backspace / Delete', category: 'nav' },
  { id: 'combo_esc', keys: [3, 4, 5], output: '⎋', name: 'Escape', category: 'nav' },
];
