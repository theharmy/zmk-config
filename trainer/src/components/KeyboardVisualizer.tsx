import React from 'react';
import { TWO_NR9_KEYS } from '../keyboardMap';
import type { Layer } from '../types';

interface KeyboardVisualizerProps {
  activeLayer: Layer;
  highlightedKeyIds?: number[];
  keyErrors?: Record<number, number>;
  keyPresses?: Record<number, number>;
}

export const KeyboardVisualizer: React.FC<KeyboardVisualizerProps> = ({
  activeLayer,
  highlightedKeyIds = [],
  keyErrors = {},
  keyPresses = {}
}) => {
  const getKeyColor = (id: number) => {
    if (highlightedKeyIds.includes(id)) {
      return 'bg-purple-600 text-white border-purple-400 ring-4 ring-purple-400/30 scale-105';
    }

    const errors = keyErrors[id] || 0;
    const presses = keyPresses[id] || 0;
    if (presses > 0 && errors > 0) {
      const errorRatio = errors / presses;
      if (errorRatio > 0.3) return 'bg-red-900/60 text-red-200 border-red-500';
      if (errorRatio > 0.1) return 'bg-amber-900/60 text-amber-200 border-amber-500';
    }

    switch (activeLayer) {
      case 'sym':
        return 'bg-cyan-950/40 text-cyan-300 border-cyan-800';
      case 'nav':
        return 'bg-yellow-950/40 text-yellow-300 border-yellow-800';
      case 'num':
        return 'bg-orange-950/40 text-orange-300 border-orange-800';
      case 'fn':
        return 'bg-emerald-950/40 text-emerald-300 border-emerald-800';
      case 'a2':
        return 'bg-blue-950/40 text-blue-300 border-blue-800';
      default:
        return 'bg-zinc-900/90 text-zinc-200 border-zinc-700 hover:border-zinc-500';
    }
  };

  const renderKey = (id: number) => {
    const keyDef = TWO_NR9_KEYS.find((k) => k.id === id);
    if (!keyDef) return null;

    let displayLabel = keyDef.defaultLayerKey[activeLayer] || keyDef.label;
    if (displayLabel === '___') displayLabel = keyDef.label;

    return (
      <div
        key={id}
        className={`relative flex flex-col items-center justify-center rounded-xl border p-2 transition-all duration-150 shadow-md select-none font-mono text-sm font-semibold w-14 h-14 sm:w-16 sm:h-16 ${getKeyColor(
          id
        )}`}
      >
        <span className="text-xs opacity-60 absolute top-1 left-1.5">{id}</span>
        <span className="text-base sm:text-lg">{displayLabel}</span>
        {keyDef.defaultLayerKey.subLabel && (
          <span className="text-[10px] opacity-75 absolute bottom-1 right-1.5">
            {keyDef.defaultLayerKey.subLabel}
          </span>
        )}
      </div>
    );
  };

  return (
    <div className="flex flex-col items-center justify-center gap-4 p-6 bg-zinc-950/60 rounded-2xl border border-zinc-800/80 shadow-2xl backdrop-blur-md my-4">
      <div className="flex items-center justify-between w-full max-w-2xl px-4 text-xs font-mono text-zinc-400">
        <span>Active Layer: <strong className="text-purple-400 uppercase">{activeLayer}</strong></span>
        <span>Keypeek & ZMK Synchronized View</span>
      </div>

      <div className="flex flex-col sm:flex-row gap-8 lg:gap-16 items-center justify-center">
        {/* Left Split */}
        <div className="flex flex-col gap-2 items-center">
          <div className="flex gap-2">
            {renderKey(0)}
            {renderKey(1)}
            {renderKey(2)}
          </div>
          <div className="flex gap-2">
            {renderKey(6)}
            {renderKey(7)}
            {renderKey(8)}
            {renderKey(9)}
          </div>
          <div className="flex gap-2 pt-2 border-t border-zinc-800">
            {renderKey(14)}
            {renderKey(15)}
          </div>
        </div>

        {/* Divider */}
        <div className="hidden sm:block w-px h-32 bg-zinc-800/80" />

        {/* Right Split */}
        <div className="flex flex-col gap-2 items-center">
          <div className="flex gap-2">
            {renderKey(3)}
            {renderKey(4)}
            {renderKey(5)}
          </div>
          <div className="flex gap-2">
            {renderKey(10)}
            {renderKey(11)}
            {renderKey(12)}
            {renderKey(13)}
          </div>
          <div className="flex gap-2 pt-2 border-t border-zinc-800">
            {renderKey(16)}
            {renderKey(17)}
          </div>
        </div>
      </div>
    </div>
  );
};
