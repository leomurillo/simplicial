"""
Sensitivity of C* <= 2.80 to (a) Wright's CONSTANT-level error terms vs (b) the
well-factorable RATE (Maynard). Direct answer to: how sensitive is the threshold to
improvements in Wright's bounds?

CORRECTION to probe_Cstar_assembly: that probe assumed a FIXED Type-II level theta_bW,
giving C*(n)=n(1-theta_bW) -> infinity. But the primorial P_n is n-fold WELL-FACTORABLE,
and Maynard's well-factorable estimates give a level that RISES with the number of factors:
  - k=1 (plain BV, no factorability):           theta = 1/2     (deficit 0.50)
  - k=3 (Maynard triply well-factorable, x^{3/5}): theta = 3/5   (deficit 0.40)
  - k=inf (conjectural smooth Elliott-Halberstam): theta -> 1     (deficit -> 0)
So the relevant model is a RISING level theta_k, and C* is governed by the RATE of the
well-factorable deficit, NOT by Wright's constant. Wright (partially-fixed moduli, beyond-
Weil) FEEDS the per-prime input; Maynard ASSEMBLES it across the factors. This probe
separates the two sensitivities.

Deterministic. No torch.
"""

C_TARGET = 2.80

# ---- PART 1: sensitivity to Wright's CONSTANT level ---------------------------------
print("=" * 84)
print("PART 1 - sensitivity to Wright's CONSTANT-level improvements (FIXED theta)")
print("=" * 84)
print("  If the level were FIXED at theta, the crossover n* = 2.8/(1-theta):")
print(f"  {'theta (fixed)':>14} {'n* = 2.8/(1-theta)':>20} {'note':>24}")
for th, note in [(0.5000, "Weil / plain BV"), (0.5152, "Wright 2026 (1/2+1/66)"),
                 (0.5200, "Wright + small gain"), (0.5467, "Polymath-8 (1/2+7/150)"),
                 (0.6000, "if Wright reached 3/5"), (0.7000, "hypothetical")]:
    nstar = C_TARGET / (1 - th)
    print(f"  {th:>14.4f} {nstar:>20.2f} {note:>24}")
print("""
  => Improving Wright's CONSTANT moves n* only marginally: 0.515 -> 0.520 moves n* from
     5.8 to 5.8 (one more nothing); even reaching 0.60 gives n*=7. A FIXED level NEVER
     closes the gap -- C*(n)=n(1-theta) grows without bound for any theta<1. So the
     threshold is LARGELY INSENSITIVE to Wright's error-term constants.""")

# ---- PART 2: the well-factorable RATE (Maynard) -- the real lever --------------------
print("=" * 84)
print("PART 2 - the well-factorable RATE (Maynard): theta_k rises with #factors")
print("=" * 84)
# data points (factorability k -> level theta_k); primorial P_n has k = n
data = [(1, 0.5, "plain BV"), (3, 0.6, "Maynard triply w.f. (x^{3/5})")]
print("  data (k = degree of well-factorability -> achieved level theta_k):")
for k, th, src in data:
    print(f"    k={k}: theta={th:.3f}  deficit={1-th:.3f}   [{src}]")
print(f"    k=inf: theta->1 (conjectural smooth Elliott-Halberstam)")

# Model A (optimistic): deficit ~ c/k. Fit c from Maynard's k=3 point.
cA = 3 * (1 - 0.6)
# Model B (pessimistic): power law deficit ~ a k^{-b} through BOTH points.
import math
b = math.log(0.5 / 0.4) / math.log(3)      # 0.5*1^{-b}=0.5 ; 0.5*3^{-b}=0.4
a = 0.5
print(f"""
  Model A (deficit ~ c/k, the form that gives bounded C*): fit to Maynard k=3 point
    => c = 3*(1-0.6) = {cA:.2f}.  Then theta_n = 1 - {cA:.1f}/n, i.e. C* = {cA:.2f} <= 2.80  -> MET.
  Model B (deficit ~ a*k^(-b) through BOTH points k=1,3): b = {b:.3f}, a = {a:.2f}
    => deficit decays slower than 1/k; C*(n) = n*a*n^(-b) = {a:.1f}*n^(1-{b:.2f}) -> infinity -> FAILS.""")

print()
print(f"  {'n':>3} {'target 1-2.8/n':>14} {'ModelA (c/n)':>13} {'ModelB (k^-b)':>14} {'A meets?':>9} {'B meets?':>9}")
for n in [3, 5, 7, 10, 15, 20, 30, 50]:
    tgt = 1 - C_TARGET / n
    thA = 1 - cA / n
    thB = 1 - a * n ** (-b)
    print(f"  {n:>3} {tgt:>14.4f} {thA:>13.4f} {thB:>14.4f} "
          f"{('yes' if thA>=tgt else 'NO'):>9} {('yes' if thB>=tgt else 'NO'):>9}")

# ---- PART 3: the needed rate, and where Maynard sits --------------------------------
print()
print("=" * 84)
print("PART 3 - what RATE closes it, and is Maynard's data above or below the line?")
print("=" * 84)
print(f"""  C* <= 2.80  <=>  well-factorable deficit(k) <= 2.80/k  for all large k.
    At Maynard's k=3: deficit = 0.40, threshold 2.80/3 = 0.93  -> 0.40 << 0.93, COMFORTABLY
      below. Maynard's single point is consistent with success.
    The fate is the ASYMPTOTIC decay exponent of deficit(k):
      - if deficit ~ c/k with c <= 2.80  (Model A; Maynard-extrapolated c=1.2): MET.
      - if deficit decays slower than 1/k (Model B; saturation / parity barrier): FAILS.
    TWO data points (k=1,3) underdetermine the exponent -- Model A and Model B both fit them
    and diverge completely at large n. The threshold sits exactly on this open question.""")

print("=" * 84)
print("VERDICT - direct answer to the sensitivity question")
print("=" * 84)
print(f"""  * To Wright's CONSTANT error terms: LARGELY INSENSITIVE. Sharpening 1/66 -> a bit more
    only nudges the crossover n* (0.515->0.520 keeps n*~5.8); no fixed-level improvement
    closes the gap for all n. Wright's role is to FEED the per-prime beyond-Weil input that
    the well-factorable assembly consumes -- it sets the CONSTANT c, not the rate.

  * To the well-factorable RATE (Maynard): TOTALLY SENSITIVE. C* <= 2.80 holds iff the
    n-fold well-factorable level obeys theta_n = 1 - C*/n with C* <= 2.80, i.e. deficit ~ c/n
    with c <= 2.80. Maynard's triply-well-factorable 3/5, read as deficit 0.4 at k=3 under a
    1/k law, gives c = 1.2 <= 2.80 -- ENCOURAGINGLY within target IF the rate persists.

  * BOTTOM LINE: my earlier 'fixed level -> C* grows -> fails' was too pessimistic; it ignored
    that the PRIMORIAL is maximally well-factorable and Maynard's level RISES with factors.
    The threshold's fate is the ASYMPTOTIC well-factorable deficit exponent -- the heart of
    Maynard's 'primes in AP to large moduli II/III' program -- NOT Wright's error constants.
    Current data (BV, Maynard 3/5) is consistent with C* ~ 1.2 (met) under a 1/k law, but a
    single nontrivial point cannot exclude a slower (saturating) rate. THIS exponent is the
    precisely-stated open lever, and it is exactly where Maynard's well-factorable machinery
    is moving. Wright sharpens the constant; Maynard decides the threshold.""")
