import type { DrillItem } from './types';

export const DRILL_ITEMS: DrillItem[] = [
  {
    id: 'de_base_1',
    title: 'German Base Alphas (A1 - Extended Pool)',
    category: 'alphas',
    description: 'Practice high-frequency German letters and simple roots randomly sampled from a large pool.',
    text: 'und der die das ist in den von mit auf fuer von als auch an nach wie aus',
    wordPool: [
      'und', 'der', 'die', 'das', 'ist', 'in', 'den', 'von', 'mit', 'auf', 'fuer',
      'als', 'auch', 'an', 'nach', 'wie', 'aus', 'ein', 'zu', 'es', 'sich', 'nicht',
      'auch', 'nach', 'werden', 'aus', 'er', 'bei', 'hat', 'dass', 'sie', 'wird',
      'sagen', 'sehen', 'kommen', 'gehen', 'wissen', 'machen', 'geben', 'lassen'
    ]
  },
  {
    id: 'de_base_2',
    title: 'German Common Words (Extended Pool)',
    category: 'alphas',
    description: 'Frequently used German words to build muscle memory on home-row mods and key positions.',
    text: 'wird aber auch nicht noch sich nur dass er es sie wir sie ein eine einen einem',
    wordPool: [
      'wird', 'aber', 'auch', 'nicht', 'noch', 'sich', 'nur', 'dass', 'er', 'es',
      'sie', 'wir', 'ein', 'eine', 'einen', 'einem', 'wieder', 'sagen', 'sehen',
      'jahr', 'mensch', 'tag', 'kind', 'zeit', 'frau', 'mann', 'kind', 'werk',
      'hand', 'auge', 'kopf', 'stadt', 'land', 'haus', 'wasser', 'welt', 'leben'
    ]
  },
  {
    id: 'bigram_combos_drill',
    title: 'Dedicated Bigram Combos (Layer A1 & A2 Chords)',
    category: 'combos',
    description: 'Drill vertical bigram combos (rl, hn, dt, cy, eo, ui, lr, nb, mt, gy, oe, iu).',
    text: 'rl hn dt cy eo ui lr nb mt gy oe iu under colon semi rl hn dt cy eo ui',
    wordPool: [
      'Urlaub', 'Erlebnis', 'natuerlich', 'Kerl', 'erlauben', 'Bahn', 'Ihnen', 'ohne', 'Wohnen', 'ahnen', 'Stadt', 'laedt', 'verwandt', 'Schmidt', 'Sandtorte', 'Cyber', 'Recycling', 'Cyan', 'Cyborg', 'Cyberspace', 'Theorie', 'Video', 'Geometrie', 'Leopard', 'Geografie', 'Ruine', 'intuitiv', 'pfui', 'Duisburg', 'Fluid', 'Walross', 'Spielraum', 'Zielrichtung', 'Edelrost', 'Alraune', 'unbekannt', 'Einbau', 'anbieten', 'unbedingt', 'Einblick', 'kommt', 'bestimmt', 'Amt', 'nimmt', 'verdammt', 'Gymnasium', 'Aegypten', 'Gyros', 'Gynaekologe', 'androgyn', 'Goethe', 'Poesie', 'Koexistenz', 'Aloe', 'Koeffizient', 'Studium', 'Medium', 'Stadium', 'Aquarium', 'Premium'    ]
  },
  {
    id: 'magic_keys_a2',
    title: 'Magic Keys & Secondary Alphas (A2 Layer)',
    category: 'alphas',
    description: 'Practice secondary alpha layer keys (BMW, Quiz, Pflanze, Zeus, Fax, Joghurt).',
    text: 'BMW Quiz Pflanze Zeus Fax Joghurt Matrix Quantum Vector Pixel Backup Plugin',
    wordPool: [
      'BMW', 'Quiz', 'Pflanze', 'Zeus', 'Fax', 'Joghurt', 'Matrix', 'Quantum',
      'Vector', 'Pixel', 'Backup', 'Plugin', 'Zephyr', 'ZMQ', 'Xylophon', 'Broker',
      'Proxy', 'Kernel', 'Thread', 'Buffer', 'Pointer', 'Reference', 'Stream'
    ]
  },
  {
    id: 'cpp_basics',
    title: 'C++ Basics & I/O (std::cout, namespaces)',
    category: 'custom',
    description: 'Drill C++ syntax including scope resolution (::), standard streams, and semicolons.',
    text: '#include <iostream>\n#include <string>\n\nint main() {\n    std::string name = "TwoNr9";\n    std::cout << "Hello C++ on " << name << std::endl;\n    return 0;\n}',
    learningNote: 'Used for standard console input/output streaming, preprocessor includes, and namespace qualification (::).',
    wordPool: [
      '#include <iostream>\nint main() {\n    std::cout << "Hello" << std::endl;\n    return 0;\n}',
      '#include <string>\nnamespace App {\n    std::string version = "1.0";\n}',
      '#include <iostream>\nint main() {\n    int x = 42;\n    std::cout << x << std::endl;\n}'
    ]
  },
  {
    id: 'cpp_templates_stl',
    title: 'C++ Templates & STL (vector, unique_ptr)',
    category: 'custom',
    description: 'Practice angle brackets (< >), templates, smart pointers, and vector iterators in C++.',
    text: 'std::vector<std::unique_ptr<Widget>> widgets;\nwidgets.push_back(std::make_unique<Widget>(42));\nfor (const auto& w : widgets) {\n    w->process();\n}',
    learningNote: 'Used for dynamic memory management with smart pointers and generic type containers in the STL.',
    wordPool: [
      'std::vector<std::unique_ptr<Widget>> widgets;\nwidgets.push_back(std::make_unique<Widget>(42));',
      'std::vector<int> numbers;\nnumbers.push_back(100);',
      'std::unique_ptr<Config> cfg = std::make_unique<Config>();'
    ]
  },
  {
    id: 'cpp_classes',
    title: 'C++ Classes & Methods (const, references)',
    category: 'custom',
    description: 'Drill C++ class declarations, constructor initializers, references (&), and const correctness.',
    text: 'class Buffer {\nprivate:\n    char* data_ptr;\n    size_t capacity;\npublic:\n    explicit Buffer(size_t cap) : capacity(cap) {}\n    const char* data() const {\n        return data_ptr;\n    }\n};',
    learningNote: 'Used for encapsulation, member initialization lists, and const-correct read-only accessor methods.',
    wordPool: [
      'class Buffer {\nprivate:\n    size_t cap;\npublic:\n    explicit Buffer(size_t c) : cap(c) {}\n};',
      'class Point {\nprivate:\n    int x, y;\npublic:\n    Point(int px, int py) : x(px), y(py) {}\n};'
    ]
  },
  {
    id: 'cpp_algorithms',
    title: 'C++ Algorithms & Lambdas (std::sort, auto)',
    category: 'custom',
    description: 'Drill C++ lambda expressions, algorithms, and container operations.',
    text: 'std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {\n    return a.id < b.id;\n});',
    learningNote: 'Used for inline anonymous predicates and efficient sorting algorithms over container ranges.',
    wordPool: [
      'std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {\n    return a.id < b.id;\n});',
      'auto it = std::find_if(v.begin(), v.end(), [](int x) {\n    return x > 10;\n});'
    ]
  },
  {
    id: 'cpp_exceptions',
    title: 'C++ Exceptions & Smart Pointers (std::shared_ptr, try/catch)',
    category: 'custom',
    description: 'Drill exception handling, try/catch blocks, and shared pointers in modern C++.',
    text: 'try {\n    auto resource = std::make_shared<Resource>();\n    resource->initialize();\n} catch (const std::exception& e) {\n    std::cerr << "Error: " << e.what() << std::endl;\n}',
    learningNote: 'Used for robust error handling and shared ownership resource management.',
    wordPool: [
      'try {\n    auto res = std::make_shared<Resource>();\n} catch (const std::exception& e) {\n    std::cerr << e.what() << std::endl;\n}'
    ]
  },
  {
    id: 'sym_morphs_brackets',
    title: 'Mod-Morph Brackets & Parentheses',
    category: 'sym_morphs',
    description: 'Drill the 14 dual-morph symbol pairs on the SYM layer (Tap vs Shift + Tap).',
    text: '() [] {} <> "" \'\' /\\ _- &= |='
  },
  {
    id: 'de_natural_flow',
    title: 'Natural German Writing (Caps & Double Letters)',
    category: 'natural_flow',
    description: 'Practice noun capitalization (Space + Sticky Shift thumb) and double letters (Thumb Repeat).',
    text: 'Das Haus hat ein grosses Dach. Die Schiffahrt im Hafen war wunderschoen. Bitte trinken Sie Kaffee.',
    wordPool: [
      'Das Haus hat ein grosses Dach.',
      'Die Schiffahrt im Hafen war wunderschoen.',
      'Bitte trinken Sie eine Tasse Kaffee.',
      'Der fruehe Vogel faengt den Wurm.',
      'Guter Rat ist teuer im Leben.',
      'Wer zuletzt laecht, laecht am besten.'
    ]
  }
];
