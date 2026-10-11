/*
 * ==============================================================================
 * TwoNr9 Key Definition Macros & Advanced Behaviors
 * ==============================================================================
 *
 * Provides:
 * 1. 14 Complete Mod-Morph Symbol & Enclosure Pairs on `sym`:
 *      ( / < · ) / > · [ / { · ] / } · : / " · ; / ' · / / \
 *      ! / ? · # / ~ · $ / € · ` / ^ · _ / - · & / @ · | / =
 * 2. Smart Sentence Space with Nav Hold (SPC_NAV):
 *      Tap: Space | Shift+Tap: ". " + Sticky Shift | Hold: Nav layer
 * 3. Dual Thumbs (A2_DUAL / SYM_DUAL, shared lt_dual):
 *      Tap: Momentary layer | Hold: Sticky layer
 * 4. Adaptive Magic Shift (MAGIC_SHIFT):
 *      After letter: Instant Repeat (&key_repeat) | On pause: Sticky Shift | Hold: Shift
 * 5. Auto-Terminating Number Word (SMART_NUM via zmk-auto-layer):
 *      Tap: num_word | Double-tap: Sticky Num | Hold: Momentary Num
 * 6. One-Key App Switcher (swapper via zmk-tri-state):
 *      Cycles open windows on Alt+Tab and releases Alt when another key is pressed
 *
 * Adaptive keys (swap rules, their hold-taps and grid names) live separately in
 * config/twonr9_adaptive_keys.h.
 * ==============================================================================
 */

#pragma once

#include <behaviors/num_word.dtsi>

/* --- Clustered Navigation & Long-Tap Jumps (Urob Nav Pattern) --- */
#define MT_CORE \
    flavor = "tap-preferred"; \
    tapping-term-ms = <220>; \
    quick-tap-ms = <220>; \
    hold-trigger-key-positions = <0>;

&mt { MT_CORE }; // Trigger tap-action on all interrupts for plain &mt keys too.

#define MASK_MODS(NAME, MODS, BINDING) \
    ZMK_MOD_MORPH(NAME, bindings = <BINDING>, <BINDING>; mods = <MODS>;)

MASK_MODS(masked_home, (MOD_LCTL), &kp HOME)
MASK_MODS(masked_end,  (MOD_LCTL), &kp END)

ZMK_HOLD_TAP(mt_home, bindings = <&masked_home>, <&kp>; MT_CORE)
ZMK_HOLD_TAP(mt_end,  bindings = <&masked_end>,  <&kp>; MT_CORE)

#define NAV_LEFT  &mt_home 0   LEFT   // Tap: Left arrow  | Long-press: Home (Start of line / First Col)
#define NAV_RIGHT &mt_end 0    RIGHT  // Tap: Right arrow | Long-press: End (End of line / Last Col)
#define NAV_UP    &mt LC(HOME) UP     // Tap: Up arrow    | Long-press: Top of Document (Ctrl+Home)
#define NAV_DOWN  &mt LC(END)  DOWN   // Tap: Down arrow  | Long-press: Bottom of Document (Ctrl+End)
#define NAV_PGDN  &mt LG(PG_DN) PG_DN // Tap: PgDn (⇟)    | Hold: Super+PgDn (Next Niri Workspace)
#define NAV_PGUP  &mt LG(PG_UP) PG_UP // Tap: PgUp (⇞)    | Hold: Super+PgUp (Prev Niri Workspace)
#define NAV_BSPC  &mt LC(BSPC) BSPC   // Tap: Backspace   | Long-press: Word delete backwards
#define NAV_DEL   &mt LC(DEL)  DEL    // Tap: Delete      | Long-press: Word delete forward

/* --- Niri Smart Layout Morph --- */
// Tap: Super+R (Cycle Column Width 33%/50%/66%) | Shift+Tap: Super+Ctrl+C (Center & Balance Columns)
ZMK_MOD_MORPH(niri_adjust,
    bindings = <&kp LG(DE_R)>, <&kp LG(LC(DE_C))>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
)

/* --- Shift-Morph Pairs: Tap = PLAIN, Shift+Tap = SHIFTED --- */
#define SHIFT_PAIR(NAME, PLAIN, SHIFTED) \
    ZMK_MOD_MORPH(NAME, bindings = <&kp PLAIN>, <&kp SHIFTED>; mods = <(MOD_LSFT|MOD_RSFT)>;)

/* --- Numpad Decimal Morph --- */
// Tap: Dot (Code/International) | Shift+Tap: Comma (German Accounting)
SHIFT_PAIR(dot_comma,   DE_DOT,    DE_COMMA)

/* --- Morphing Symbol & Enclosure Pairs --- */
SHIFT_PAIR(excl_qmark,  DE_EXCL,   DE_QMARK)
SHIFT_PAIR(hash_tilde,  DE_HASH,   DE_TILDE)
SHIFT_PAIR(dllr_euro,   DE_DLLR,   DE_EURO)
SHIFT_PAIR(grave_caret, DE_GRAVE,  DE_CARET)
SHIFT_PAIR(under_minus, DE_UNDER,  DE_MINUS)
SHIFT_PAIR(amps_at,     DE_AMPS,   DE_AT)
SHIFT_PAIR(equal_pipe,  DE_EQUAL,  DE_PIPE)
SHIFT_PAIR(lpar_rpar,   DE_LPAR,   DE_RPAR)
SHIFT_PAIR(lbkt_rbkt,   DE_LBKT,   DE_RBKT)
SHIFT_PAIR(lbrc_rbrc,   DE_LBRC,   DE_RBRC)
SHIFT_PAIR(lt_gt,       DE_LT,     DE_GT)
SHIFT_PAIR(colon_dqt,   DE_COLON,  DE_DQT)
SHIFT_PAIR(semi_sqt,    DE_SEMI,   DE_SQT)
SHIFT_PAIR(fslh_bslh,   DE_FSLH,   DE_BSLH)

/* --- Morphing Backspace / Delete --- */
// Tap: Backspace | Shift+Tap: Shift+Delete (keeps shift, cf. urob)
ZMK_MOD_MORPH(bs_del,
    bindings = <&kp BSPC>, <&kp DEL>;
    mods = <(MOD_LSFT|MOD_RSFT)>;
    keep-mods = <MOD_RSFT>;
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

/* --- Dual Thumbs (Tap: Single Momentary, Hold: Sticky Layer) --- */
ZMK_HOLD_TAP(lt_dual,
    flavor = "balanced";
    tapping-term-ms = <LT_TERM>;
    quick-tap-ms = <QUICK_TAP_MS>;
    bindings = <&mo>, <&sl>;
)

#define A2_DUAL  &lt_dual L_A2 L_A2
#define SYM_DUAL &lt_dual L_SYM L_SYM


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
        trigger-keys = <
            A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
            DE_SZ DE_A_UMLAUT DE_O_UMLAUT DE_U_UMLAUT
            DE_N1 DE_N2 DE_N3 DE_N4 DE_N5 DE_N6 DE_N7 DE_N8 DE_N9 DE_N0
            DE_LPAR DE_RPAR DE_LT DE_GT DE_LBKT DE_RBKT DE_LBRC DE_RBRC
            DE_COLON DE_DQT DE_SEMI DE_SQT DE_DOT DE_COMMA
            DE_PLUS DE_MINUS DE_ASTRK DE_FSLH DE_BSLH DE_EQUAL DE_PRCNT
            DE_PIPE DE_AMPS DE_UNDER DE_EXCL DE_QMARK DE_HASH DE_TILDE
            DE_DLLR DE_EURO DE_GRAVE DE_CARET DE_AT
        >;
        bindings = <&key_repeat>;
        max-prior-idle-ms = <500>;
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
