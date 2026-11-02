/*
 * ==============================================================================
 * TwoNr9 Adaptive Keys -- shared generators
 * ==============================================================================
 *
 * The devicetree node generators shared by every TwoNr9 adaptive-key file
 * (twonr9_adaptive_keys_bugwind.h, twonr9_adaptive_keys_srht.h):
 *
 *   1. the swap rules          -> AK / AK2 / AK_PAIR + AK_TRIG
 *   2. the hold-tap wiring     -> MAKE_AK_HM / MAKE_AK_LT
 *
 * An adaptive key rewrites its own output depending on what was typed just
 * before it: within AK_MS of the trigger key it emits the swap output instead
 * of its default key. Typing "uo" within the window comes out as "ui"; outside
 * it, as "uo". Nothing changes for untimed or non-matching input.
 *
 * The generators are pure macro definitions; they reference the per-keymap
 * tuning constants (AK_MS, HRM_*, LT_*) and the hand-based trigger sets
 * (TRIG_L / TRIG_R) by name, so the including keymap must have #define'd those
 * before it pulls in an adaptive-key file (both twonr9.keymap and
 * twonr9_srht.keymap already do).
 *
 * Each variant file includes this header and then calls the generators to
 * build its own rules, hold-taps and grid aliases.
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
