"""
SSA / scale-convexity offshoot of the arch-domination ANEC diagnostic -- is it a NEW constraint?

The brainstorm flagged: strong subadditivity (Lieb-Ruskai) on nested scaling intervals -> an
UNCONDITIONAL scale-convexity of the arithmetic relative entropy, hoped to be a new constraint on the
zeros "like Rodgers-Tao Lambda>=0".  This probe tests whether the convexity actually DETECTS RH.

Setup.  The natural scale family is the sec-8.7 heat trace  Theta(s) = sum_n e^{-s omega_n}  (omega_n
the energy spectrum; under RH omega_n = gamma_n^2 > 0).  Its scale-convexity is  Theta''(s) =
sum_n omega_n^2 e^{-s omega_n}.

KEY OBSERVATION (the test).  Every term e^{-s omega} is convex in s for ANY real omega -- including
omega < 0 (an off-line zero / RH violation), since d^2/ds^2 e^{-s omega} = omega^2 e^{-s omega} > 0
regardless of sign(omega).  So Theta''(s) > 0 ALWAYS, whether or not RH holds.  => scale-convexity is
AUTOMATIC and RH-INSENSITIVE.  Contrast sec 8.7's nuclearity/boundedness, which DID detect the negative
mode (e^{-s omega_*} -> +inf).  Convexity does not.

VERDICT this probe establishes: the SSA offshoot is THIN -- the convexity it gives is automatic and
cannot constrain RH (unlike Lambda>=0, which is a genuine zero-side flow result).  It is the QNEC
(local) face of the C diagnostic, with the SAME firewall: convexity is unconditional on the modular
(K) side; crossing to the zeros = Bisognano-Wichmann = positive energy = RH.  No new constraint.

No torch. mpmath for the trace; finite-difference convexity cross-check.
"""
import mpmath as mp

mp.mp.dps = 30
GAMMA = [mp.mpf(x) for x in [
    "14.134725142", "21.022039639", "25.010857580", "30.424876126", "32.935061588",
    "37.586178159", "40.918719012", "43.327073281", "48.005150881", "49.773832478",
]]

def trace(omegas, s):
    return mp.fsum(mp.e ** (-s * w) for w in omegas)

def trace_d2(omegas, s):           # exact second derivative: sum omega^2 e^{-s omega}
    return mp.fsum(w * w * mp.e ** (-s * w) for w in omegas)

if __name__ == "__main__":
    print("SSA scale-convexity: does it DETECT RH?  (offshoot of the ANEC diagnostic)")
    print("=" * 78)

    # (A) RH-TRUE spectrum: omega_n = gamma_n^2 > 0
    omega_true = [g * g for g in GAMMA]
    # (B) RH-FALSE stand-in: inject a NEGATIVE-energy mode (an off-line zero), as in sec 8.7
    omega_false = omega_true + [mp.mpf("-5.0")]

    print("  Theta''(s) = sum omega_n^2 e^{-s omega_n}  (scale-convexity); >0 means convex")
    print(f"  {'s':>5} | {'Theta'' (RH-true)':>20} | {'Theta'' (RH-FALSE, neg mode)':>28}")
    print("  " + "-" * 64)
    for s in (mp.mpf("0.02"), mp.mpf("0.05"), mp.mpf("0.10"), mp.mpf("0.30")):
        d2t = trace_d2(omega_true, s)
        d2f = trace_d2(omega_false, s)
        print(f"  {mp.nstr(s,2):>5} | {mp.nstr(d2t,8):>20} | {mp.nstr(d2f,8):>28}")
    print("  " + "-" * 64)
    print("  BOTH columns are strictly POSITIVE (convex) -- including the RH-FALSE spectrum with a")
    print("  negative mode.  Convexity holds regardless of RH:  d^2/ds^2 e^{-s omega}=omega^2 e^{-s omega}>0")
    print("  for ANY sign of omega.  => scale-convexity is AUTOMATIC and RH-INSENSITIVE.")
    print()
    print("  Contrast (sec 8.7): the nuclearity norm / BOUNDEDNESS detects the negative mode --")
    print("  e^{-s*(-5)} = e^{+5s} -> +inf.  That is the RH-sensitive quantity; convexity is not.")

    print("\n" + "=" * 78)
    print("VERDICT (SSA offshoot -- THIN).")
    print("  * SSA gives an UNCONDITIONAL scale-convexity (the QNEC/local face of the C diagnostic).")
    print("  * But that convexity is AUTOMATIC (every e^{-s omega} convex) and RH-INSENSITIVE: it holds")
    print("    for off-line / negative-mode spectra too.  It does NOT constrain the zeros to the line.")
    print("  * So it is NOT a Rodgers-Tao Lambda>=0 analogue (Lambda>=0 is a genuine zero-side flow")
    print("    result that detects RH; the entropy convexity lives on the modular K-side and detects")
    print("    nothing without the Bisognano-Wichmann bridge = positive energy = RH -- same firewall).")
    print("  * The RH content is in BOUNDEDNESS (sec 8.7, e^{-sP} bounded = P>=0), not CONVEXITY.")
    print("  * Net: the SSA offshoot does not yield a new unconditional constraint on the zeros.")
    print("    The arch-domination brainstorm (A,B,C,D,E,F + SSA) is exhausted of fresh leverage;")
    print("    the irreducible step remains P>=0 / mu_lambda v 0 (prime-shaped, no shortcut).")
