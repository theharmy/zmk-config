/*
 * ==============================================================================
 * TwoNr9 Key Definition Macros & Advanced Behaviors
 * ==============================================================================
 *
 * Provides:
 * 1. Parameterized Homerow Modifiers: AL(), GL(), SL(), CL(), SR(), GR(), AR(), CR()
 * 2. Parameterized Fast Layer-Taps: S1() [Sym], FN() [Fn/Media], NM() [Num]
 * 3. 14 Complete Mod-Morph Symbol & Enclosure Pairs on `sym`:
 *      ( / < · ) / > · [ / { · ] / } · : / " · ; / ' · / / \
 *      ! / ? · # / ~ · $ / € · ` / ^ · _ / - · & / @ · | / =
 * 4. Smart Sentence Space with Nav Hold (SPC_NAV):
 *      Tap: Space | Shift+Tap: ". " + Sticky Shift | Hold: Nav layer
 * 5. Dual a2 Thumb (A2_DUAL):
 *      Tap: Single a2 letter | Hold: Continuous a2 words (BMW, Quiz, Pflanze)
 * 6. Adaptive Magic Shift (MAGIC_SHIFT):
 *      After letter: Instant Repeat (&key_repeat) | On pause: Sticky Shift | Hold: Shift
 * 7. Auto-Terminating Number Word (SMART_NUM via zmk-auto-layer):
 *      Tap: num_word | Double-tap: Sticky Num | Hold: Momentary Num
 * 8. One-Key App Switcher (swapper via zmk-tri-state):
 *      Cycles open windows on Alt+Tab and releases Alt when another key is pressed
 * ==============================================================================
 */

#pragma once

#include <behaviors/num_word.dtsi>

/* --- Homerow Modifiers on Left Hand --- */
#define AL(k)    &hml LEFT_ALT k
#define GL(k)    &hml LEFT_GUI k
#define SL(k)    &hml LEFT_SHIFT k
#define CL(k)    &hml LCTRL k

/* --- Homerow Modifiers on Right Hand --- */
#define SR(k)    &hmr RIGHT_SHIFT k
#define GR(k)    &hmr RIGHT_GUI k
#define AR(k)    &hmr RIGHT_ALT k
#define CR(k)    &hmr LCTRL k

/* --- Fast Layer-Taps on Home Row Keys --- */
#define S1(k)    &lt_r4 L_SYM k    // Hold: Primary Symbols Layer
#define FN(k)    &lt_r4 L_FN k     // Hold: Function & Media Layer
#define NM(k)    &lt_r4 L_NUM k    // Hold: Numpad / Arithmetic Layer

/* --- Morphing Symbol & Enclosure Pairs --- */
ZMK_MOD_MORPH(excl_qmark,
    bindings = <&kp DE_EXCL>, <&kp DE_QMARK>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(hash_tilde,
    bindings = <&kp DE_HASH>, <&kp DE_TILDE>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(dllr_euro,
    bindings = <&kp DE_DLLR>, <&kp DE_EURO>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(grave_caret,
    bindings = <&kp DE_GRAVE>, <&kp DE_CARET>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(under_minus,
    bindings = <&kp DE_UNDER>, <&kp DE_MINUS>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(amps_at,
    bindings = <&kp DE_AMPS>, <&kp DE_AT>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(pipe_equal,
    bindings = <&kp DE_PIPE>, <&kp DE_EQUAL>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(lpar_lt,
    bindings = <&kp DE_LPAR>, <&kp DE_LT>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(rpar_gt,
    bindings = <&kp DE_RPAR>, <&kp DE_GT>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(colon_dqt,
    bindings = <&kp DE_COLON>, <&kp DE_DQT>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(lbkt_lbrc,
    bindings = <&kp DE_LBKT>, <&kp DE_LBRC>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(rbkt_rbrc,
    bindings = <&kp DE_RBKT>, <&kp DE_RBRC>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(semi_sqt,
    bindings = <&kp DE_SEMI>, <&kp DE_SQT>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_MOD_MORPH(fslh_bslh,
    bindings = <&kp DE_FSLH>, <&kp DE_BSLH>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

/* --- Morphing Backspace / Delete --- */
ZMK_MOD_MORPH(bs_del,
    bindings = <&kp BSPC>, <&kp DEL>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

/* --- Smart Sentence Space with Nav Hold --- */
ZMK_MACRO(dot_spc,
    bindings = <&kp DE_DOT &kp SPACE &sk LEFT_SHIFT>;
    wait-ms = <0>;
    tap-ms = <5>;
)

ZMK_MOD_MORPH(spc_morph,
    bindings = <&kp SPACE>, <&dot_spc>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_HOLD_TAP(lt_spc,
    flavor = "balanced";
    tapping-term-ms = <200>;
    quick-tap-ms = <QUICK_TAP_MS>;
    bindings = <&mo>, <&spc_morph>;
)

#define SPC_NAV &lt_spc L_NAV 0

/* --- Dual a2 Thumb (Tap: Single a2, Hold: Continuous a2) --- */
ZMK_HOLD_TAP(lt_a2,
    flavor = "balanced";
    tapping-term-ms = <200>;
    quick-tap-ms = <QUICK_TAP_MS>;
    bindings = <&mo>, <&sl>;
)

#define A2_DUAL &lt_a2 L_A2 L_A2

/* --- Magic Shift (Adaptive Repeat / Sticky Shift / Hold Shift) --- */
#define MAGIC_SHIFT &magic_shift LSHFT 0

ZMK_HOLD_TAP(magic_shift,
    bindings = <&kp>, <&magic_shift_tap>;
    flavor = "balanced";
    tapping-term-ms = <200>;
    quick-tap-ms = <QUICK_TAP_MS>;
)

ZMK_MOD_MORPH(magic_shift_tap,
    bindings = <&shift_repeat>, <&caps_word>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

ZMK_ADAPTIVE_KEY(shift_repeat,
    bindings = <&sk LSHFT>;
    repeat {
        trigger-keys = <A B C D E F G H I J K L M N O P Q R S T U V W X Y Z>;
        bindings = <&key_repeat>;
        max-prior-idle-ms = <1200>;
        strict-modifiers;
    };
)

/* --- Auto-Terminating Number Word (smart_num) --- */
ZMK_TAP_DANCE(num_dance,
    tapping-term-ms = <200>;
    bindings = <&num_word L_NUM>, <&sl L_NUM>;
)

ZMK_HOLD_TAP(smart_num,
    flavor = "balanced";
    tapping-term-ms = <200>;
    quick-tap-ms = <QUICK_TAP_MS>;
    bindings = <&mo>, <&num_dance>;
)

#define SMART_NUM &smart_num L_NUM 0

/* --- One-Key App Switcher (swapper) --- */
ZMK_TRI_STATE(swapper,
    bindings = <&kt LALT>, <&kp TAB>, <&kt LALT>;
    ignored-key-positions = <0 1 2 3 4 5>;
)
