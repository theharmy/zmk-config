/*
 * ==============================================================================
 * TwoNr9 Adaptive Keys -- "bugwind" (the default)
 * ==============================================================================
 *
 * Bugwind binds every alpha directly (the a1/a2 grids are self-describing),
 * so the only adaptive behavior is a small set of same-finger swap rules that
 * let one finger's repeated press be reached by rolling a different finger
 * instead. Each rule is a symmetric swap: after TRIG, the two involved keys
 * exchange outputs, so both spellings stay reachable (the inverse covers the
 * rarer direction and the edge cases).
 *
 *   rule   trigger  effect          why
 *   ----   -------  --------------  -------------------------------------------
 *   1      U        O <-> I         "uo" is usually "ui"; "ui" is common, "uo"
 *                                   is rarer -- the inverse keeps "uo" safe.
 *   2      Y        U <-> S         "yu" is usually "ys"; "ys" is common, "yu"
 *                                   is rarer -- the inverse keeps "yu" safe.
 *
 * An adaptive key rewrites its own output within AK_MS of the trigger key;
 * outside the window it emits its default. Triggers match regardless of active
 * modifiers (e.g. "UO" -> "UI"). Add `strict-modifiers;` to AK_TRIG if that
 * ever gets in the way.
 *
 * The node generators (AK / AK_PAIR / AK_TRIG / MAKE_AK_HM / MAKE_AK_LT) are
 * shared with the srht variant in twonr9_adaptive.h; this file only declares
 * the rules and wires them into the grid.
 *
 * --- The four adaptive keys ---------------------------------------------------
 *
 *   key  layer  pos  hand  hold            name    swap
 *   ---  -----  ---  ----  --------------  ------  --------------------------
 *   o    a1      4   right Nav layer       NV_O    -> I after U
 *   i    a1     12   right RIGHT_ALT       AR_I    -> O after U
 *   u    a1      5   right Fn layer        FN_U    -> S after Y
 *   s    a1     10   right RIGHT_SHIFT     SH_S    -> U after Y
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
 *   swap rule      edit the AK_PAIR / AK call in its group below
 *   hold behavior  edit the MAKE_AK_HM / MAKE_AK_LT line in the same group
 *   grid binding   edit the #define name below (e.g. NV_O) where it is used
 *                  in the layer grids of twonr9.keymap
 *   timing         AK_MS (swap window), HRM_* / LT_* (holds)
 *
 * Each key's rule, wiring and name sit together in one group below, so a
 * rework touches one contiguous block.
 * ==============================================================================
 */

#pragma once

#include "twonr9_adaptive.h"

/* ==============================================================================
 * Adaptive keys -- one group per key: swap rule, hold wiring, grid name
 * ============================================================================== */

/* --- 1. u oi: after U, O<->I ------------------------------------------------ */
AK(o, DE_O, AK_TRIG(t, DE_U, DE_I)) // defines ak_o

MAKE_AK_LT(o, &ak_o) // a1: Nav hold, o (swaps with i after u)
#define NV_O &lt_o L_NAV 0

AK(i, DE_I, AK_TRIG(t, DE_U, DE_O)) // defines ak_i

MAKE_AK_HM(i, &ak_i, TRIG_R) // a1: Alt hold, i (swaps with o after u)
#define AR_I &hm_i RIGHT_ALT 0

/* --- 2. y us: after Y, U<->S ------------------------------------------------ */
AK(u, DE_U, AK_TRIG(t, DE_Y, DE_S)) // defines ak_u

MAKE_AK_LT(u, &ak_u) // a1: Fn hold, u (swaps with s after y)
#define FN_U &lt_u L_FN 0

AK(s, DE_S, AK_TRIG(t, DE_Y, DE_U)) // defines ak_s

MAKE_AK_HM(s, &ak_s, TRIG_R) // a1: Shift hold, s (swaps with u after y)
#define SH_S &hm_s RIGHT_SHIFT 0
