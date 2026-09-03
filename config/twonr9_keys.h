/*
 * ==============================================================================
 * TwoNr9 Key Definition Macros (Modular Parameterized Wrappers)
 * ==============================================================================
 *
 * REASONING & BENEFITS:
 * - Eliminates static 1:1 key definitions (e.g. #define al_L, gl_N, etc.).
 * - To change any key in your keymap, you only edit the keycode directly inside
 *   the layer grid (e.g. `AL(DE_L)` -> `AL(DE_A)` to change L to A).
 * - You never have to touch this file or add new definitions when rearranging keys.
 *
 * CONVENTIONS:
 * - AL(k) / AR(k): Left / Right Alt  + key `k`
 * - GL(k) / GR(k): Left / Right Gui  + key `k`
 * - SL(k) / SR(k): Left / Right Shift + key `k`
 * - CL(k) / CR(k): Left / Right Ctrl  + key `k`
 * - S1(k): Primary Symbols Layer (L_SYM) on hold + key `k` on tap
 * - S2(k): Secondary Symbols Layer (L_SYM2) on hold + key `k` on tap
 * - NM(k): Numpad / Arithmetic Layer (L_NUM) on hold + key `k` on tap
 * ==============================================================================
 */

#pragma once

/* --- Homerow Modifiers on Left Hand --- */
#define AL(k)    &hml LEFT_ALT k
#define GL(k)    &hml LEFT_GUI k
#define SL(k)    &hml LEFT_SHIFT k
#define CL(k)    &hml LCTRL k

/* --- Homerow Modifiers on Right Hand --- */
#define SR(k)    &hmr LEFT_SHIFT k
#define GR(k)    &hmr LEFT_GUI k
#define AR(k)    &hmr LEFT_ALT k
#define CR(k)    &hmr LCTRL k

/* --- Fast Layer-Taps on Home Row Keys --- */
#define S1(k)    &lt_r4 L_SYM k    // Hold: Primary Symbols Layer (Layer 3)
#define S2(k)    &lt_r4 L_SYM2 k   // Hold: Secondary Symbols Layer (Layer 4)
#define NM(k)    &lt_r4 L_NUM k    // Hold: Numpad / Arithmetic Layer (Layer 5)
