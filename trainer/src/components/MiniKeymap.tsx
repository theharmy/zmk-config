import React from 'react';
import type { Layer } from '../types';

interface MiniKeymapProps {
  activeLayer: Layer;
  highlightedKeyIds: number[];
  actionLabel?: string;
}

export const MiniKeymap: React.FC<MiniKeymapProps> = ({
  activeLayer,
  highlightedKeyIds,
  actionLabel
}) => {
  const getLayerColor = (layer: Layer) => {
    switch (layer) {
      case 'sym':
        return 'bg-purple-600 shadow-lg shadow-purple-900/60 ring-2 ring-purple-400 scale-105';
      case 'nav':
        return 'bg-blue-600 shadow-lg shadow-blue-900/60 ring-2 ring-blue-400 scale-105';
      case 'a2':
        return 'bg-emerald-600 shadow-lg shadow-emerald-900/60 ring-2 ring-emerald-400 scale-105';
      case 'num':
        return 'bg-amber-600 shadow-lg shadow-amber-900/60 ring-2 ring-amber-400 scale-105';
      default:
        return 'bg-zinc-800 border border-zinc-700';
    }
  };

  const renderKey = (id: number) => {
    const isHighlighted = highlightedKeyIds.includes(id);
    const colorClass = isHighlighted ? getLayerColor(activeLayer) : 'bg-zinc-900/60 border border-zinc-800/80';

    return (
      <div
        key={id}
        className={`w-10 h-10 sm:w-12 sm:h-12 rounded-xl transition-all duration-150 ${colorClass}`}
      />
    );
  };

  return (
    <div className="flex flex-col items-center gap-4 bg-zinc-900/80 border border-zinc-800 p-6 rounded-2xl shadow-xl backdrop-blur-md">
      <div className="flex items-center justify-between w-full max-w-md px-2 text-xs font-mono">
        <span className="text-zinc-400">
          Layer: <strong className="uppercase text-purple-400">{activeLayer}</strong>
        </span>
        {actionLabel && (
          <span className="px-2.5 py-1 rounded-full bg-purple-950/80 text-purple-300 border border-purple-800/60 font-semibold">
            {actionLabel}
          </span>
        )}
      </div>

      {/* Columnar Split Layout */}
      <div className="flex flex-col sm:flex-row gap-12 items-center justify-center py-2">
        {/* Left Half (Columnar: Pinky -> Ring -> Middle -> Index/Inner) */}
        <div className="flex flex-col items-end gap-2">
          {/* Top Row */}
          <div className="flex gap-2">
            {renderKey(0)}
            {renderKey(1)}
            {renderKey(2)}
          </div>
          {/* Home Row */}
          <div className="flex gap-2">
            {renderKey(6)}
            {renderKey(7)}
            {renderKey(8)}
            {renderKey(9)}
          </div>
          {/* Left Thumbs shifted ~1.5u to the right (pl-12) below innermost keys */}
          <div className="flex gap-2 pt-2 pl-12">
            {renderKey(14)}
            {renderKey(15)}
          </div>
        </div>

        {/* Center Divider */}
        <div className="hidden sm:block w-px h-36 bg-zinc-800" />

        {/* Right Half (Columnar: Inner/Index -> Middle -> Ring -> Pinky) */}
        <div className="flex flex-col items-start gap-2">
          {/* Top Row */}
          <div className="flex gap-2">
            {renderKey(3)}
            {renderKey(4)}
            {renderKey(5)}
          </div>
          {/* Home Row */}
          <div className="flex gap-2">
            {renderKey(10)}
            {renderKey(11)}
            {renderKey(12)}
            {renderKey(13)}
          </div>
          {/* Right Thumbs shifted ~1.5u to the left (pr-12) below innermost keys */}
          <div className="flex gap-2 pt-2 pr-12">
            {renderKey(16)}
            {renderKey(17)}
          </div>
        </div>
      </div>
    </div>
  );
};
