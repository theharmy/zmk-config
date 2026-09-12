import { useState, useEffect } from 'react';
import type { DrillItem, SessionStats } from './types';
import { DRILL_ITEMS } from './drills';
import { TrainingArea } from './components/TrainingArea';
import { StatsAndHeatmap } from './components/StatsAndHeatmap';
import { Keyboard, BarChart3, BookOpen, Sparkles } from 'lucide-react';

export function App() {
  const [selectedDrill, setSelectedDrill] = useState<DrillItem>(DRILL_ITEMS[0]);
  const [currentView, setCurrentView] = useState<'drill' | 'stats' | 'select'>('select');
  const [statsHistory, setStatsHistory] = useState<SessionStats[]>([]);
  const [keyErrors] = useState<Record<number, number>>({});
  const [keyPresses] = useState<Record<number, number>>({});

  useEffect(() => {
    const saved = localStorage.getItem('twonr9_stats');
    if (saved) {
      try {
        setStatsHistory(JSON.parse(saved));
      } catch (e) {
        console.error(e);
      }
    }
  }, []);

  const handleFinishSession = (stats: SessionStats) => {
    const updated = [stats, ...statsHistory];
    setStatsHistory(updated);
    localStorage.setItem('twonr9_stats', JSON.stringify(updated));
  };

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 flex flex-col items-center selection:bg-purple-600 selection:text-white">
      <header className="w-full max-w-5xl px-6 py-4 flex items-center justify-between border-b border-zinc-800/80 bg-zinc-900/50 backdrop-blur-md sticky top-0 z-50">
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => setCurrentView('select')}>
          <div className="p-2 bg-purple-600/20 border border-purple-500/30 rounded-xl text-purple-400">
            <Keyboard className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-lg font-bold tracking-tight">TwoNr9 Trainer</h1>
            <p className="text-xs text-zinc-400 font-mono">18-Key Split ZMK • German & C++ Drill</p>
          </div>
        </div>

        <div className="flex items-center gap-2 font-mono text-sm">
          <button
            onClick={() => setCurrentView('select')}
            className={`px-3 py-1.5 rounded-lg border transition flex items-center gap-2 ${
              currentView === 'select'
                ? 'bg-purple-600 border-purple-500 text-white'
                : 'bg-zinc-900 border-zinc-800 text-zinc-300 hover:bg-zinc-800'
            }`}
          >
            <BookOpen className="w-4 h-4" /> Drills
          </button>
          <button
            onClick={() => setCurrentView('stats')}
            className={`px-3 py-1.5 rounded-lg border transition flex items-center gap-2 ${
              currentView === 'stats'
                ? 'bg-purple-600 border-purple-500 text-white'
                : 'bg-zinc-900 border-zinc-800 text-zinc-300 hover:bg-zinc-800'
            }`}
          >
            <BarChart3 className="w-4 h-4" /> Analytics & Heatmap
          </button>
        </div>
      </header>

      <main className="w-full max-w-5xl flex-1 p-6 flex flex-col items-center justify-center">
        {currentView === 'select' && (
          <div className="w-full max-w-3xl flex flex-col gap-6 text-left">
            <div className="bg-gradient-to-r from-purple-950/40 via-zinc-900 to-zinc-900 border border-purple-800/40 p-8 rounded-3xl shadow-xl">
              <div className="flex items-center gap-2 text-purple-400 font-mono text-xs uppercase tracking-wider mb-2">
                <Sparkles className="w-4 h-4" /> ZMK Layout Mastery
              </div>
              <h2 className="text-3xl font-bold tracking-tight text-zinc-100 mb-3">
                Drill Your 18-Key TwoNr9 Layout
              </h2>
              <p className="text-sm text-zinc-300 leading-relaxed mb-6">
                Master homorow mods, vertical/horizontal combos (`ß`, `_`, `:`), mod-morph brackets, German orthography, and C++ coding patterns seamlessly synchronized with Keypeek.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {DRILL_ITEMS.map((drill) => (
                <div
                  key={drill.id}
                  onClick={() => {
                    setSelectedDrill(drill);
                    setCurrentView('drill');
                  }}
                  className="group bg-zinc-900/80 hover:bg-zinc-900 border border-zinc-800 hover:border-purple-500/50 p-6 rounded-2xl cursor-pointer transition-all duration-200 shadow-lg flex flex-col justify-between"
                >
                  <div>
                    <span className="text-[10px] font-mono uppercase px-2.5 py-1 rounded-full bg-purple-950/80 text-purple-300 border border-purple-800/60 inline-block mb-3">
                      {drill.category}
                    </span>
                    <h3 className="text-lg font-bold text-zinc-100 group-hover:text-purple-400 transition">
                      {drill.title}
                    </h3>
                    <p className="text-xs text-zinc-400 mt-1 leading-normal">{drill.description}</p>
                  </div>
                  <div className="mt-4 pt-4 border-t border-zinc-800/80 flex items-center justify-between text-xs font-mono text-zinc-500 group-hover:text-zinc-300">
                    <span className="truncate max-w-[220px]">{drill.text}</span>
                    <span className="text-purple-400 font-semibold">Start →</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {currentView === 'drill' && (
          <TrainingArea
            drill={selectedDrill}
            onFinishSession={handleFinishSession}
            onSelectDrill={() => setCurrentView('select')}
          />
        )}

        {currentView === 'stats' && (
          <StatsAndHeatmap
            statsHistory={statsHistory}
            keyErrors={keyErrors}
            keyPresses={keyPresses}
            onBackToTraining={() => setCurrentView('select')}
          />
        )}
      </main>

      <footer className="w-full max-w-5xl px-6 py-4 border-t border-zinc-800/80 text-center text-xs font-mono text-zinc-500">
        TwoNr9 Layout Trainer • Integrated with ZMK & Keypeek
      </footer>
    </div>
  );
}

export default App;
