export type Layer = 'a1' | 'a2' | 'nav' | 'sym' | 'fn' | 'num';

export interface LayerKeyMap {
  a1: string;
  a2: string;
  nav: string;
  sym: string;
  fn: string;
  num: string;
  subLabel?: string;
}

export interface KeyDefinition {
  id: number;
  label: string;
  hand: 'left' | 'right';
  row: 'top' | 'home' | 'thumb';
  defaultLayerKey: LayerKeyMap;
}

export type DrillCategory = 'alphas' | 'combos' | 'sym_morphs' | 'natural_flow' | 'custom';

export interface DrillItem {
  id: string;
  title: string;
  category: DrillCategory;
  text: string;
  description: string;
  wordPool?: string[];
  learningNote?: string;
}

export interface KeyStats {
  presses: number;
  errors: number;
  totalTimeMs: number;
}

export interface ComboStats {
  id: string;
  name: string;
  presses: number;
  errors: number;
}

export interface SessionStats {
  wpm: number;
  accuracy: number;
  charsTyped: number;
  errors: number;
  durationSeconds: number;
  timestamp: number;
}
