import React, { useState, useEffect, useRef } from 'react';
import type { DrillItem, SessionStats } from '../types';
import { RefreshCw, Award, Zap, Code, BookOpen } from 'lucide-react';

interface TrainingAreaProps {
  drill: DrillItem;
  onFinishSession: (stats: SessionStats) => void;
  onSelectDrill: () => void;
}

export const TrainingArea: React.FC<TrainingAreaProps> = ({
  drill,
  onFinishSession,
  onSelectDrill
}) => {
  const [targetText, setTargetText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [startTime, setStartTime] = useState<number | null>(null);
  const [errors, setErrors] = useState(0);
  const [completed, setCompleted] = useState(false);
  const [wpm, setWpm] = useState(0);
  const [accuracy, setAccuracy] = useState(100);

  const inputRef = useRef<HTMLInputElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const initDrillText = (item: DrillItem) => {
    if (item.wordPool && item.wordPool.length > 0) {
      const shuffled = [...item.wordPool].sort(() => 0.5 - Math.random());
      const isCpp = item.id.startsWith('cpp_');
      if (isCpp) {
        return shuffled[0];
      }
      const selected = shuffled.slice(0, 18);
      return selected.join(' ');
    }
    return item.text;
  };

  useEffect(() => {
    setTargetText(initDrillText(drill));
    setCurrentIndex(0);
    setStartTime(null);
    setErrors(0);
    setCompleted(false);
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, [drill]);

  useEffect(() => {
    if (containerRef.current) {
      const scrollRatio = targetText.length > 0 ? currentIndex / targetText.length : 0;
      containerRef.current.scrollLeft = containerRef.current.scrollWidth * scrollRatio - 120;
    }
  }, [currentIndex, targetText]);

  const currentChar = targetText[currentIndex] || '';
  const prevChar = currentIndex > 0 ? targetText[currentIndex - 1] : '';
  const isCppDrill = drill.id.startsWith('cpp_');

  const getAnnouncement = (text: string, idx: number, char: string, prev: string, drillId: string, category: string) => {
    if (char === ' ') {
      return {
        title: 'SMART SPACE & SHIFT + SPACE',
        action: 'Space / Dot-Space Morph',
        instruction: 'Tap for Space | Shift + Tap for ". " + Sticky Shift',
        bgStyle: 'bg-gradient-to-r from-sky-950/90 via-zinc-900 to-zinc-900 border-sky-500/80 text-sky-200',
        underlineStyle: 'decoration-sky-400',
        colorClass: 'text-sky-300'
      };
    }

    const morphHints: Record<string, string> = {
      '(': 'Tap (Primary)',
      '<': 'Shift + Tap (Mod-Morph)',
      ')': 'Tap (Primary)',
      '>': 'Shift + Tap (Mod-Morph)',
      '[': 'Tap (Primary)',
      '{': 'Shift + Tap (Mod-Morph)',
      ']': 'Tap (Primary)',
      '}': 'Shift + Tap (Mod-Morph)',
      ';': 'Tap (Primary)',
      '\'': 'Shift + Tap (Mod-Morph)',
      ':': 'Tap (Primary)',
      '"': 'Shift + Tap (Mod-Morph)',
      '!': 'Tap (Primary)',
      '?': 'Shift + Tap (Mod-Morph)',
      '#': 'Tap (Primary)',
      '~': 'Shift + Tap (Mod-Morph)',
      '$': 'Tap (Primary)',
      '€': 'Shift + Tap (Mod-Morph)',
      '`': 'Tap (Primary)',
      '^': 'Shift + Tap (Mod-Morph)',
      '_': 'Tap (Primary)',
      '-': 'Shift + Tap (Mod-Morph)',
      '&': 'Tap (Primary)',
      '@': 'Shift + Tap (Mod-Morph)',
      '|': 'Tap (Primary)',
      '=': 'Shift + Tap (Mod-Morph)'
    };

    if (morphHints[char]) {
      return {
        title: 'MOD-MORPH SYMBOL',
        action: `Symbol '${char}'`,
        instruction: morphHints[char],
        bgStyle: 'bg-gradient-to-r from-purple-950/90 via-zinc-900 to-zinc-900 border-purple-500/80 text-purple-200',
        underlineStyle: 'decoration-purple-400',
        colorClass: 'text-purple-300'
      };
    }

    if (drillId === 'magic_keys_a2' && char) {
      return {
        title: 'MAGIC KEYS — LAYER 2 (A2)',
        action: `Alpha 2 (${char})`,
        instruction: 'Hold Left Outer Thumb (Key 14) + Alpha Key',
        bgStyle: 'bg-gradient-to-r from-emerald-950/90 via-zinc-900 to-zinc-900 border-emerald-500/80 text-emerald-200',
        underlineStyle: 'decoration-emerald-400',
        colorClass: 'text-emerald-300'
      };
    }

    if (drillId === 'bigram_combos_drill') {
      const words = text.split(' ');
      let charCount = 0;
      let currentWord = words[0] || '';
      for (const w of words) {
        if (idx >= charCount && idx <= charCount + w.length) {
          currentWord = w;
          break;
        }
        charCount += w.length + 1;
      }

      const a2Bigrams = ['lr', 'nb', 'mt', 'gy', 'oe', 'iu'];
      const isA2 = a2Bigrams.some(b => currentWord.includes(b));
      const layerNum = isA2 ? '2' : '1';

      const knownBigrams = ['rl', 'hn', 'dt', 'cy', 'eo', 'ui', 'lr', 'nb', 'mt', 'gy', 'oe', 'iu'];
      const foundBigram = knownBigrams.find(b => currentWord.includes(b)) || currentWord;

      return {
        title: `BIGRAM CHORD — LAYER ${layerNum}`,
        action: `${foundBigram} (Layer ${layerNum})`,
        instruction: `Vertical Bigram Chord`,
        bgStyle: isA2
          ? 'bg-gradient-to-r from-emerald-950/90 via-zinc-900 to-zinc-900 border-emerald-500/80 text-emerald-200'
          : 'bg-gradient-to-r from-violet-950/90 via-zinc-900 to-zinc-900 border-violet-500/80 text-violet-200',
        underlineStyle: isA2 ? 'decoration-emerald-400' : 'decoration-violet-400',
        colorClass: isA2 ? 'text-emerald-300' : 'text-violet-300'
      };
    }

    if (category === 'natural_flow' || drillId === 'de_natural_flow') {
      if (char && char === char.toUpperCase() && char !== ' ' && char !== '.' && (prev === ' ' || prev === '.' || idx === 0)) {
        return {
          title: 'NOUN CAPITALIZATION (STICKY SHIFT)',
          action: `Sticky Shift + '${char}'`,
          instruction: 'Use Right Inner Thumb (Key 16) Sticky Shift for Noun',
          bgStyle: 'bg-gradient-to-r from-blue-950/90 via-zinc-900 to-zinc-900 border-blue-500/80 text-blue-200',
          underlineStyle: 'decoration-blue-400',
          colorClass: 'text-blue-300'
        };
      }
      if (prev && char && prev.toLowerCase() === char.toLowerCase()) {
        return {
          title: 'ADAPTIVE KEY REPEAT',
          action: `Repeat Key '${char}${char}'`,
          instruction: 'Use Right Inner Thumb (Key 16) Repeat Key after Alpha',
          bgStyle: 'bg-gradient-to-r from-amber-950/90 via-zinc-900 to-zinc-900 border-amber-500/80 text-amber-200',
          underlineStyle: 'decoration-amber-400',
          colorClass: 'text-amber-300'
        };
      }
    }

    return null;
  };

  const announcement = getAnnouncement(targetText, currentIndex, currentChar, prevChar, drill.id, drill.category);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (completed) return;

    if (!startTime) {
      setStartTime(Date.now());
    }

    if (e.key === 'Backspace') {
      e.preventDefault();
      if (currentIndex > 0) {
        if (e.ctrlKey) {
          const textUpToNow = targetText.slice(0, currentIndex);
          const lastSpace = textUpToNow.trimEnd().lastIndexOf(' ');
          const newIdx = lastSpace === -1 ? 0 : lastSpace + 1;
          setCurrentIndex(newIdx);
        } else {
          setCurrentIndex((prev) => Math.max(0, prev - 1));
        }
      }
      return;
    }

    let charTyped = '';
    if (e.key === 'Enter') {
      charTyped = '\n';
    } else if (e.key.length === 1) {
      charTyped = e.key;
    } else {
      return;
    }

    if (charTyped === currentChar) {
      const nextIdx = currentIndex + 1;
      setCurrentIndex(nextIdx);

      const elapsedMin = (Date.now() - (startTime || Date.now())) / 60000;
      if (elapsedMin > 0) {
        const currentWpm = Math.round(nextIdx / 5 / elapsedMin);
        setWpm(currentWpm);
      }

      const currentAcc = Math.round(((nextIdx - errors) / nextIdx) * 100);
      setAccuracy(Math.max(0, currentAcc));

      if (nextIdx >= targetText.length) {
        setCompleted(true);
        const duration = Math.round((Date.now() - (startTime || Date.now())) / 1000);
        onFinishSession({
          wpm: wpm || 25,
          accuracy: accuracy,
          charsTyped: targetText.length,
          errors,
          durationSeconds: duration,
          timestamp: Date.now()
        });
      }
    } else {
      setErrors((prev) => {
        const newErrors = prev + 1;
        const currentAcc = Math.round(((currentIndex - newErrors) / (currentIndex + 1)) * 100);
        setAccuracy(Math.max(0, currentAcc));
        return newErrors;
      });
    }
  };

  const restartDrill = () => {
    setTargetText(initDrillText(drill));
    setCurrentIndex(0);
    setStartTime(null);
    setErrors(0);
    setCompleted(false);
    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  const underlineClass = announcement ? announcement.underlineStyle : 'decoration-purple-500';
  const charColorClass = announcement ? announcement.colorClass : 'text-zinc-400';

  return (
    <div className="flex flex-col gap-6 w-full max-w-none flex-1 px-8 py-8 items-center">
      {/* Header Info */}
      <div className="flex flex-col lg:flex-row items-center justify-between bg-zinc-900/80 border border-zinc-800 p-8 rounded-3xl gap-6 shadow-xl w-full">
        <div className="text-left">
          <div className="flex items-center gap-2 text-purple-400 font-mono text-xs uppercase font-bold tracking-wider mb-1">
            {isCppDrill && <Code className="w-4 h-4" />} {drill.category} drill
          </div>
          <h2 className="text-3xl font-bold text-zinc-100">{drill.title}</h2>
          <p className="text-base text-zinc-400">{drill.description}</p>
        </div>
        <div className="flex items-center gap-4 font-mono text-base">
          <div className="bg-zinc-800/80 px-5 py-2.5 rounded-xl border border-zinc-700">
            WPM: <strong className="text-purple-400">{wpm}</strong>
          </div>
          <div className="bg-zinc-800/80 px-5 py-2.5 rounded-xl border border-zinc-700">
            Acc: <strong className="text-emerald-400">{accuracy}%</strong>
          </div>
          <button
            onClick={restartDrill}
            className="px-5 py-2.5 bg-zinc-800 hover:bg-zinc-700 text-zinc-200 rounded-xl border border-zinc-700 transition font-medium flex items-center gap-2"
          >
            <RefreshCw className="w-4 h-4" /> New Set
          </button>
          <button
            onClick={onSelectDrill}
            className="px-5 py-2.5 bg-zinc-800 hover:bg-zinc-700 text-zinc-200 rounded-xl border border-zinc-700 transition font-medium"
          >
            Switch Drill
          </button>
        </div>
      </div>

      {/* C++ Learning Context Banner Above Typing Line */}
      {isCppDrill && drill.learningNote && (
        <div className="bg-blue-950/40 border border-blue-500/40 px-8 py-4 rounded-2xl shadow-md flex items-center gap-4 text-left w-full">
          <BookOpen className="w-6 h-6 text-blue-400 shrink-0" />
          <p className="text-base font-mono text-blue-200">
            <strong className="text-blue-300">C++ Concept Note:</strong> {drill.learningNote}
          </p>
        </div>
      )}

      {/* Typing Prompt Display */}
      <div
        className="relative bg-zinc-900/95 border border-zinc-800/90 rounded-3xl p-16 min-h-[380px] flex flex-col items-center justify-center cursor-pointer shadow-2xl backdrop-blur-md w-full flex-1 overflow-hidden"
        onClick={() => inputRef.current?.focus()}
      >
        <input
          ref={inputRef}
          type="text"
          className="absolute opacity-0 pointer-events-none"
          onKeyDown={handleKeyDown}
          autoFocus
        />

        {completed ? (
          <div className="flex flex-col items-center gap-4 text-center w-full">
            <Award className="w-20 h-20 text-emerald-400 animate-bounce mx-auto" />
            <h3 className="text-4xl font-bold text-zinc-100">Drill Completed Successfully!</h3>
            <p className="text-lg text-zinc-400 font-mono">
              Speed: {wpm} WPM | Accuracy: {accuracy}% | Errors: {errors}
            </p>
            <button
              onClick={restartDrill}
              className="mt-4 px-10 py-4 bg-purple-600 hover:bg-purple-500 text-white rounded-2xl font-medium shadow-lg transition flex items-center gap-2 text-lg mx-auto"
            >
              <RefreshCw className="w-6 h-6" /> Practice Again
            </button>
          </div>
        ) : (
          <div className="w-full flex flex-col items-center gap-6">
            <div ref={containerRef} className="w-full text-left overflow-x-auto whitespace-pre py-2 scroll-smooth px-8">
              <span className="font-mono text-xl sm:text-3xl tracking-wide leading-relaxed">
                <span className="text-purple-400 font-bold bg-purple-950/40 px-2 py-1 rounded opacity-90">
                  {targetText.slice(0, currentIndex)}
                </span>
                {/* Color-coded underline matching the active announcement / behavior */}
                <span className={`text-amber-300 underline decoration-3 underline-offset-8 bg-zinc-800 px-2 py-1 rounded font-bold ${underlineClass}`}>
                  {currentChar === ' ' ? '␣' : currentChar === '\n' ? '↵' : currentChar}
                </span>
                <span className={charColorClass}>
                  {targetText.slice(currentIndex + 1)}
                </span>
              </span>
            </div>

            {/* Universal Announcement Banner */}
            {!completed && announcement && (
              <div className={`border px-6 py-3 rounded-2xl shadow-2xl flex items-center gap-4 text-left max-w-md mx-auto backdrop-blur-md ${announcement.bgStyle}`}>
                <Zap className="w-5 h-5 text-yellow-400 animate-pulse shrink-0" />
                <div>
                  <p className="text-xs font-mono uppercase tracking-widest opacity-80 font-bold">{announcement.title}</p>
                  <p className="text-2xl sm:text-3xl font-black tracking-tight mt-0.5">{announcement.action}</p>
                  <p className="text-xs font-mono opacity-90 mt-1">{announcement.instruction}</p>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
