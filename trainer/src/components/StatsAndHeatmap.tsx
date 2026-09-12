import React, { useState } from 'react';
import type { SessionStats, Layer } from '../types';
import { TWO_NR9_KEYS } from '../keyboardMap';
import { Trophy, Activity, Target, Layers, Grid } from 'lucide-react';

interface StatsAndHeatmapProps {
  statsHistory: SessionStats[];
  keyErrors: Record<number, number>;
  keyPresses: Record<number, number>;
  onBackToTraining: () => void;
}

export const StatsAndHeatmap: React.FC<StatsAndHeatmapProps> = ({
  statsHistory,
  keyErrors,
  keyPresses,
  onBackToTraining
}) => {
  const [activeLayerRef, setActiveLayerRef] = useState<Layer>('a1');

  const avgWpm =
    statsHistory.length > 0
      ? Math.round(statsHistory.reduce((acc, s) => acc + s.wpm, 0) / statsHistory.length)
      : 0;

  const avgAcc =
    statsHistory.length > 0
      ? Math.round(statsHistory.reduce((acc, s) => acc + s.accuracy, 0) / statsHistory.length)
      : 100;

  return (
    <div className="flex flex-col gap-8 w-full max-w-6xl mx-auto p-6 text-left">
      {/* Top Bar */}
      <div className="flex items-center justify-between bg-zinc-900/80 border border-zinc-800 p-6 rounded-3xl shadow-xl">
        <div>
          <h2 className="text-2xl font-bold text-zinc-100">Performance Analytics, Heatmap & Layer Reference</h2>
          <p className="text-sm text-zinc-400">Explore TwoNr9 layer mappings, bigram chords, and error distributions.</p>
        </div>
        <button
          onClick={onBackToTraining}
          className="px-5 py-2.5 bg-purple-600 hover:bg-purple-500 text-white rounded-xl font-medium transition"
        >
          Back to Training
        </button>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <div className="bg-zinc-900/80 border border-zinc-800 p-6 rounded-3xl flex items-center gap-4 shadow-lg">
          <div className="p-3 bg-purple-950/60 border border-purple-800/60 rounded-2xl text-purple-400">
            <Activity className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs font-mono text-zinc-400 uppercase">Average Speed</p>
            <p className="text-3xl font-bold text-zinc-100 font-mono">{avgWpm} <span className="text-sm font-normal text-zinc-400">WPM</span></p>
          </div>
        </div>

        <div className="bg-zinc-900/80 border border-zinc-800 p-6 rounded-3xl flex items-center gap-4 shadow-lg">
          <div className="p-3 bg-emerald-950/60 border border-emerald-800/60 rounded-2xl text-emerald-400">
            <Target className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs font-mono text-zinc-400 uppercase">Average Accuracy</p>
            <p className="text-3xl font-bold text-zinc-100 font-mono">{avgAcc}%</p>
          </div>
        </div>

        <div className="bg-zinc-900/80 border border-zinc-800 p-6 rounded-3xl flex items-center gap-4 shadow-lg">
          <div className="p-3 bg-amber-950/60 border border-amber-800/60 rounded-2xl text-amber-400">
            <Trophy className="w-6 h-6" />
          </div>
          <div>
            <p className="text-xs font-mono text-zinc-400 uppercase">Sessions Completed</p>
            <p className="text-3xl font-bold text-zinc-100 font-mono">{statsHistory.length}</p>
          </div>
        </div>
      </div>

      {/* Layers & Bigrams Reference Section */}
      <div className="bg-zinc-900/80 border border-zinc-800 p-8 rounded-3xl flex flex-col gap-6 shadow-xl">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <h3 className="text-xl font-semibold text-zinc-200 flex items-center gap-2">
              <Layers className="w-5 h-5 text-purple-400" /> TwoNr9 Layer & Key Reference
            </h3>
            <p className="text-sm text-zinc-400 mt-1">Select any layer to inspect its exact key bindings on the 18-key split layout.</p>
          </div>
          <div className="flex flex-wrap gap-2 font-mono text-xs">
            {(['a1', 'a2', 'sym', 'nav', 'fn', 'num'] as Layer[]).map((l) => (
              <button
                key={l}
                onClick={() => setActiveLayerRef(l)}
                className={`px-3 py-1.5 rounded-xl border uppercase transition font-semibold ${
                  activeLayerRef === l
                    ? 'bg-purple-600 border-purple-500 text-white shadow-md'
                    : 'bg-zinc-800 border-zinc-700 text-zinc-300 hover:bg-zinc-700'
                }`}
              >
                {l}
              </button>
            ))}
          </div>
        </div>

        {/* Layer Keymap Visualizer */}
        <div className="flex flex-col sm:flex-row gap-12 justify-center items-center py-8 bg-zinc-950/70 rounded-2xl border border-zinc-800 shadow-inner">
          <div className="flex flex-col items-end gap-2">
            <div className="flex gap-2">
              {[0, 1, 2].map((id) => renderLayerKey(id, activeLayerRef))}
            </div>
            <div className="flex gap-2">
              {[6, 7, 8, 9].map((id) => renderLayerKey(id, activeLayerRef))}
            </div>
            <div className="flex gap-2 pt-2 pl-12">
              {[14, 15].map((id) => renderLayerKey(id, activeLayerRef))}
            </div>
          </div>

          <div className="hidden sm:block w-px h-36 bg-zinc-800" />

          <div className="flex flex-col items-start gap-2">
            <div className="flex gap-2">
              {[3, 4, 5].map((id) => renderLayerKey(id, activeLayerRef))}
            </div>
            <div className="flex gap-2">
              {[10, 11, 12, 13].map((id) => renderLayerKey(id, activeLayerRef))}
            </div>
            <div className="flex gap-2 pt-2 pr-12">
              {[16, 17].map((id) => renderLayerKey(id, activeLayerRef))}
            </div>
          </div>
        </div>

        {/* Bigrams Reference Table */}
        <div className="mt-4 pt-6 border-t border-zinc-800 flex flex-col gap-4">
          <h4 className="text-base font-semibold text-zinc-200">Vertical Bigram Chords Reference</h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 font-mono text-sm">
            <div className="bg-zinc-950/70 border border-zinc-800 p-4 rounded-2xl">
              <span className="text-purple-400 font-bold">Layer 1 (A1) Bigrams:</span>
              <div className="grid grid-cols-3 gap-2 mt-2 text-zinc-300">
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">rl (0 + 7)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">hn (1 + 8)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">dt (2 + 9)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">cy (3 + 10)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">eo (4 + 11)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">ui (5 + 12)</span>
              </div>
            </div>

            <div className="bg-zinc-950/70 border border-zinc-800 p-4 rounded-2xl">
              <span className="text-emerald-400 font-bold">Layer 2 (A2) Bigrams:</span>
              <div className="grid grid-cols-3 gap-2 mt-2 text-zinc-300">
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">lr (0 + 7)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">nb (1 + 8)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">mt (2 + 9)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">gy (3 + 10)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">oe (4 + 11)</span>
                <span className="bg-zinc-900 p-2 rounded-lg border border-zinc-800 text-center">iu (5 + 12)</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Heatmap Section */}
      <div className="bg-zinc-900/80 border border-zinc-800 p-8 rounded-3xl flex flex-col gap-6 shadow-xl">
        <div>
          <h3 className="text-xl font-semibold text-zinc-200 flex items-center gap-2">
            <Grid className="w-5 h-5 text-amber-400" /> Key Error Heatmap
          </h3>
          <p className="text-sm text-zinc-400 mt-1">
            Keys highlighted in red or amber indicate frequent typos during drills. Focus your practice on these positions.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-12 justify-center items-center py-8 bg-zinc-950/70 rounded-2xl border border-zinc-800 shadow-inner">
          <div className="flex flex-col items-end gap-2">
            <div className="flex gap-2">
              {[0, 1, 2].map((id) => renderHeatmapKey(id, keyErrors, keyPresses))}
            </div>
            <div className="flex gap-2">
              {[6, 7, 8, 9].map((id) => renderHeatmapKey(id, keyErrors, keyPresses))}
            </div>
            <div className="flex gap-2 pt-2 pl-12">
              {[14, 15].map((id) => renderHeatmapKey(id, keyErrors, keyPresses))}
            </div>
          </div>

          <div className="hidden sm:block w-px h-36 bg-zinc-800" />

          <div className="flex flex-col items-start gap-2">
            <div className="flex gap-2">
              {[3, 4, 5].map((id) => renderHeatmapKey(id, keyErrors, keyPresses))}
            </div>
            <div className="flex gap-2">
              {[10, 11, 12, 13].map((id) => renderHeatmapKey(id, keyErrors, keyPresses))}
            </div>
            <div className="flex gap-2 pt-2 pr-12">
              {[16, 17].map((id) => renderHeatmapKey(id, keyErrors, keyPresses))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

function renderLayerKey(id: number, layer: Layer) {
  const keyDef = TWO_NR9_KEYS.find((k) => k.id === id);
  const val = keyDef?.defaultLayerKey[layer] || keyDef?.label || '';
  return (
    <div
      key={id}
      className="relative flex flex-col items-center justify-center rounded-xl border border-zinc-700 bg-zinc-900 text-zinc-200 w-12 h-12 font-mono text-xs shadow-md"
    >
      <span className="text-[9px] opacity-50 absolute top-1 left-1.5">{id}</span>
      <span className="font-bold text-sm truncate max-w-[40px]">{val === '___' ? keyDef?.label : val}</span>
    </div>
  );
}

function renderHeatmapKey(
  id: number,
  keyErrors: Record<number, number>,
  keyPresses: Record<number, number>
) {
  const keyDef = TWO_NR9_KEYS.find((k) => k.id === id);
  const errors = keyErrors[id] || 0;
  const presses = keyPresses[id] || 0;

  let bgClass = 'bg-zinc-900 text-zinc-300 border-zinc-700';
  if (presses > 0) {
    const ratio = errors / presses;
    if (ratio > 0.3) bgClass = 'bg-red-950/80 text-red-200 border-red-500';
    else if (ratio > 0.1) bgClass = 'bg-amber-950/80 text-amber-200 border-amber-500';
    else bgClass = 'bg-emerald-950/80 text-emerald-200 border-emerald-500';
  }

  return (
    <div
      key={id}
      className={`relative flex flex-col items-center justify-center rounded-xl border p-2 w-12 h-12 font-mono text-xs ${bgClass}`}
    >
      <span className="text-[9px] opacity-60 absolute top-1 left-1.5">{id}</span>
      <span className="font-bold">{keyDef?.defaultLayerKey.a1 || keyDef?.label}</span>
      <span className="text-[8px] opacity-75">{errors}e</span>
    </div>
  );
}
