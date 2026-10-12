/*
 * ==============================================================================
 * TwoNr9 Adaptive Keys
 * ==============================================================================
 *
 * Everything about the adaptive keys lives in this one file:
 *   1. the swap rules          -> AK / AK2 / AK_PAIR + AK_TRIG
 *   2. the hold-tap wiring     -> MAKE_AK_HM / MAKE_AK_LT
 *   3. the grid names          -> FN_L, GL_H, ... (used by twonr9.keymap)
 *
 * An adaptive key rewrites its own output depending on what was typed just
 * before it: within AK_MS of the trigger key it emits the swap output instead
 * of its default key. Typing "rh" within the window comes out as "rl"; outside
 * it, as "rh". Nothing changes for untimed or non-matching input.
 *
 * German bigram frequency is what the rules encode -- the swaps correct the
 * most common mistypes on this layout:
 *
 *   rule   trigger  effect                why
 *   ----   -------  --------------------  ------------------------------------
 *   1      R        H <-> L               "rhl" is almost always meant "rll"
 *   2      U        O -> I,  I -> O       "uo" is usually "ui"
 *   3      Q        I -> U,  U -> I       "qi" is usually "qu"
 *   4      R        M <-> V               "rmv" is almost always meant "rmr"
 *   5      N        B <-> X               "nbx" is almost always meant "nxx"
 *
 * Note: triggers match regardless of active modifiers (e.g. "RH" -> "RL").
 * Add `strict-modifiers;` to AK_TRIG if that ever gets in the way.
 *
 * --- The nine adaptive keys ---------------------------------------------------
 *
 *   key  layer  pos  hand  hold            name    swap
 *   ---  -----  ---  ----  --------------  ------  --------------------------
 *   l    a1      0   left  Fn layer        FN_L    -> h after R
 *   h    a1      8   left  LEFT_GUI        GL_H    -> l after R
 *   o    a1      4   right Nav layer       NV_O    -> I after U
 *   i    a1     12   right RIGHT_ALT       AR_I    -> O after U, U after Q
 *   u    a1      5   right Fn layer        FN_U    -> I after Q
 *   x    a2      0   left  Fn layer        FN_X    -> b after N
 *   b    a2      1   left  Nav layer       NV_B    -> x after N
 *   v    a2      2   left  Sym layer       SY_V    -> m after R
 *   m    a2      7   left  LEFT_ALT        AL_M    -> v after R
 *
 * HM keys hold a modifier, LT keys hold a momentary layer. Both use the same
 * feel as the plain homerow mods / layer-taps (see MAKE_HRM / &lt in
 * twonr9.keymap) -- flavour, tapping term and prior-idle all come from the
 * shared tuning constants, so they stay in step automatically.
 *
 * HM keys sit on the home row, LT keys on the top row, matching the plain
 * &hml/&hmr and &lt keys around them. So the adaptive keys inherit the same
 * hold-trigger sets and tapping terms as their row.
 *
 * Trigger sets are hand-based, not row-based: a key on the left hand holds
 * when chording the right hand (and vice versa). Moving an adaptive key to
 * another row therefore needs no change here -- only a different hand does.
 *
 * --- To change one adaptive key ----------------------------------------------
 *
 *   swap rule      edit the AK_PAIR / AK / AK2 call in its group below
 *   hold behavior  edit the MAKE_AK_HM / MAKE_AK_LT line in the same group
 *   grid binding   edit the #define name below (e.g. FN_L) where it is used
 *                  in the layer grids of twonr9.keymap
 *   timing         AK_MS (swap window), HRM_* / LT_* (holds)
 *
 * Each key's rule, wiring and name sit together in one group below, so a
 * rework touches one contiguous block.
 * ==============================================================================
 */

#pragma once

/* --- Generators: adaptive-key nodes ---------------------------------------- */

// One adaptive-key behavior with one trigger rule: after TRIG (within AK_MS),
// NAME outputs OUT instead of its default key. (Devicetree subnodes need the
// trailing ';', and are ';'-separated, never ','-separated.)
#define AK_TRIG(NAME, TRIG, OUT)                                               \
    NAME { trigger-keys = <TRIG>; max-prior-idle-ms = <AK_MS>;                 \
           bindings = <&kp OUT>; };

#define AK(NAME, DEFAULT, TRIG)                                                \
    ZMK_ADAPTIVE_KEY(ak_##NAME, bindings = <&kp DEFAULT>; TRIG)

// Like AK, but with two trigger rules.
#define AK2(NAME, DEFAULT, TRIG1, TRIG2)                                       \
    ZMK_ADAPTIVE_KEY(ak_##NAME, bindings = <&kp DEFAULT>; TRIG1 TRIG2)

// Symmetric swap: "after T, A->B and B->A".
#define AK_PAIR(NA, A, NB, B, T)                                               \
    AK(NA, A, AK_TRIG(t, T, B))                                                \
    AK(NB, B, AK_TRIG(t, T, A))

/* --- Generators: hold-taps wiring the adaptive keys into the grid ----------- */

// HM: hold = modifier (param), tap = adaptive key, same feel as hml/hmr.
// TRIG_L / TRIG_R are the trigger set for a key on that hand.
// quick-tap-ms omitted to match MAKE_HRM / urob: inert below HRM_IDLE, see
// the reasoning in twonr9.keymap.
#define MAKE_AK_HM(NAME, TAP, TRIGGER_POS)                                     \
    ZMK_HOLD_TAP(hm_##NAME, flavor = "balanced";                               \
                 tapping-term-ms = <HRM_TERM>;                                 \
                 require-prior-idle-ms = <HRM_IDLE>; hold-trigger-on-release;  \
                 hold-trigger-key-positions = <TRIGGER_POS>;                   \
                 bindings = <&kp>, <TAP>;)

// LT: hold = momentary layer (param), tap = adaptive key, same feel as &lt.
// quick-tap-ms omitted likewise (inert below LT_IDLE).
#define MAKE_AK_LT(NAME, TAP)                                                  \
    ZMK_HOLD_TAP(lt_##NAME, flavor = "balanced";                               \
                 tapping-term-ms = <LT_TERM>;                                  \
                 require-prior-idle-ms = <LT_IDLE>;                            \
                 bindings = <&mo>, <TAP>;)

/* ==============================================================================
 * Adaptive keys -- one group per key: swap rule, hold wiring, grid name
 * ============================================================================== */

/* --- 1. r hl: after R, H<->L ------------------------------------------------ */
AK_PAIR(h, DE_H, l, DE_L, DE_R) // defines ak_h + ak_l

MAKE_AK_HM(h, &ak_h, TRIG_L) // a1: GUI hold, h (swaps with l after r)
#define GL_H &hm_h LEFT_GUI 0

MAKE_AK_LT(l, &ak_l) // a1: Fn hold, l (swaps with h after r)
#define FN_L &lt_l L_FN 0

/* --- 2. u oi: after U, O<->I ----------------------------------------------- */
AK(o, DE_O, AK_TRIG(t, DE_U, DE_I)) // defines ak_o

MAKE_AK_LT(o, &ak_o) // a1: Nav hold, o (swaps with i after u)
#define NV_O &lt_o L_NAV 0

/* --- 3. q iu: after Q, I<->U ----------------------------------------------- */
AK2(i, DE_I, AK_TRIG(t_u, DE_U, DE_O), // defines ak_i (two rules: U and Q)
    AK_TRIG(t_q, DE_Q, DE_U))

MAKE_AK_HM(i, &ak_i, TRIG_R) // a1: Alt hold, i (swaps with o after u / u after q)
#define AR_I &hm_i RIGHT_ALT 0

AK(u, DE_U, AK_TRIG(t, DE_Q, DE_I)) // defines ak_u

MAKE_AK_LT(u, &ak_u) // a1: Fn hold, u (swaps with i after q)
#define FN_U &lt_u L_FN 0

/* --- 4. r mv: after R, M<->V ----------------------------------------------- */
AK_PAIR(m, DE_M, v, DE_V, DE_R) // defines ak_m + ak_v

MAKE_AK_HM(m, &ak_m, TRIG_L) // a2: Alt hold, m (swaps with v after r)
#define AL_M &hm_m LEFT_ALT 0

MAKE_AK_LT(v, &ak_v) // a2: Sym hold, v (swaps with m after r)
#define SY_V &lt_v L_SYM 0

/* --- 5. n bx: after N, B<->X ----------------------------------------------- */
AK_PAIR(b, DE_B, x, DE_X, DE_N) // defines ak_b + ak_x

MAKE_AK_LT(b, &ak_b) // a2: Nav hold, b (swaps with x after n)
#define NV_B &lt_b L_NAV 0

MAKE_AK_LT(x, &ak_x) // a2: Fn hold, x (swaps with b after n)
#define FN_X &lt_x L_FN 0
