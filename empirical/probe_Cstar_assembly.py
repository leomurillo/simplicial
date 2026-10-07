"""
Assembling C* explicitly: does the current ANT machinery reach the primorial-BV level
theta_0(p_n) = 1 - C*/n with C* <= 2.80 (the diez Thm 3.3 / ocho S7.1 V/M crossover)?

Ingredients (all literature except the CRT-compounding hypothesis, which is the program's
open step):
  - Heath-Brown identity, K=5: Lambda decomposed into Type I (one smooth variable <= x^{1/5})
    + Type II (two middle variables). Type II is the BINDING constraint.
  - Type I / large sieve over d | P_n: benefits from the EXTREME sparsity of divisors
    (sum_{d|P_n} phi(d) = P_n exactly, vs ~Q^2 for all q<=Q). High level, NOT binding.
  - Type II / bilinear: Cauchy-Schwarz + complete sum mod d. Per prime, Weil |Kl(p)|<=2 sqrt p
    gives the 1/2 barrier (level 1/2). BEYOND-Weil (the only way past 1/2):
       * Wright 2026 (trilinear Kloosterman, arXiv:2604.25177): level 1/2 + 1/66 ~ 0.5152.
       * Polymath-8 (smooth moduli, Type-III/Deligne): varpi = 7/300, level 1/2 + 2varpi
         = 1/2 + 7/150 ~ 0.5467.
    KEY FACT: a UNIFORM per-prime beyond-Weil exponent gives a FIXED level (the complete
    sum mod d = prod_i p_i factors as prod p_i^{1/2-varpi} = d^{1/2-varpi}; same exponent,
    same level, regardless of #factors). So fixed per-prime savings -> FIXED theta_0.
  - Mertens: prod_{i<=n}(1-1/p_i)^{-1} ~ e^gamma log p_n -- a log-loss to absorb.

The target theta_0 = 1 - C*/n -> 1 (Elliott-Halberstam regime) as n -> infinity. A FIXED
level theta_bW corresponds to C*_achieved(n) = n(1 - theta_bW), which GROWS. So C* <= 2.80
can hold only up to a crossover n*, unless the per-prime savings COMPOUND (level grows with
n) -- the program's open hypothesis. This probe computes the crossover and the growth.

Deterministic. No torch.
"""

import sympy

# ---- primorial data ------------------------------------------------------------------
def first_primes(n):
    out = []; p = 2
    while len(out) < n:
        out.append(p); p = sympy.nextprime(p)
    return out

NMAX = 16
PR = first_primes(NMAX)

import math
def primorial_data(n):
    ps = PR[:n]
    logP = sum(math.log(p) for p in ps)               # log P_n = theta(p_n)
    mertens = 1.0
    for p in ps:
        mertens *= 1 / (1 - 1/p)                       # prod (1-1/p)^{-1}
    return ps[-1], logP, mertens

# ---- the achieved Type II (beyond-Weil) levels, FIXED -------------------------------
THETA_WEIL    = 0.5
THETA_WRIGHT  = 0.5 + 1/66          # arXiv:2604.25177  ~ 0.51515
THETA_POLY8   = 0.5 + 7/150         # Polymath-8 varpi=7/300, 1/2+2varpi ~ 0.54667

C_TARGET = 2.80                     # ocho S7.1 V/M crossover (diez Thm 3.3 required rate)

print("=" * 86)
print("PART 1 - the target 1 - C*/n vs the FIXED beyond-Weil Type II levels")
print("=" * 86)
print(f"  target C* = {C_TARGET};  Weil level {THETA_WEIL:.4f},  Wright {THETA_WRIGHT:.4f},"
      f"  Polymath-8 {THETA_POLY8:.4f}")
print()
print(f"  {'n':>3} {'p_n':>5} {'logP_n':>8} {'target 1-2.8/n':>15} {'Wright lvl':>11}"
      f" {'Poly8 lvl':>10} {'meets?':>8}")
for n in range(2, NMAX + 1):
    pn, logP, mert = primorial_data(n)
    tgt = 1 - C_TARGET / n
    meets_w = THETA_WRIGHT >= tgt
    meets_p = THETA_POLY8 >= tgt
    tag = "BOTH" if meets_p and meets_w else ("Poly8" if meets_p else ("Wright" if meets_w else "NEITHER"))
    print(f"  {n:>3} {pn:>5} {logP:>8.2f} {tgt:>15.4f} {THETA_WRIGHT:>11.4f}"
          f" {THETA_POLY8:>10.4f} {tag:>8}")

# ---- crossover: where fixed level can no longer meet the (rising) target -------------
print()
print("=" * 86)
print("PART 2 - the crossover n*: fixed beyond-Weil meets 1-C*/n only for small n")
print("=" * 86)
n_star_w = C_TARGET / (1 - THETA_WRIGHT)
n_star_p = C_TARGET / (1 - THETA_POLY8)
print(f"  target level 1-2.8/n = theta_bW  =>  n* = 2.8/(1-theta_bW)")
print(f"    Wright  (0.5152): n* = {n_star_w:.2f}   -> C*<=2.80 holds for n <= {int(n_star_w)}")
print(f"    Poly8   (0.5467): n* = {n_star_p:.2f}   -> C*<=2.80 holds for n <= {int(n_star_p)}")
print(f"  (matches the program ledger 'n <= 6 discharged')")

# ---- the achieved C*(n) GROWS with a fixed level ------------------------------------
print()
print("=" * 86)
print("PART 3 - C*_achieved(n) = n(1 - theta_bW): FIXED level => C* GROWS, blows past 2.80")
print("=" * 86)
print(f"  {'n':>3} {'C*_ach (Weil)':>14} {'C*_ach (Wright)':>16} {'C*_ach (Poly8)':>15} {'<=2.80?':>8}")
for n in range(2, NMAX + 1):
    c_weil  = n * (1 - THETA_WEIL)
    c_wright= n * (1 - THETA_WRIGHT)
    c_poly  = n * (1 - THETA_POLY8)
    ok = "yes" if c_poly <= C_TARGET else "NO"
    print(f"  {n:>3} {c_weil:>14.2f} {c_wright:>16.2f} {c_poly:>15.2f} {ok:>8}")

# ---- what rate would CLOSE it, and does known iteration give it ----------------------
print()
print("=" * 86)
print("PART 4 - the deficit RATE: what the bridge needs vs what fixed savings give")
print("=" * 86)
print("""  target deficit  1 - theta_0 = C*/n          -> O(1/n),   -> 0   (EH regime)
  fixed beyond-Weil deficit  1 - theta_bW ~ 0.45-0.48 -> O(1),   does NOT -> 0
  large-sieve-only deficit (ledger) ~ 2 log2 / log n   -> O(1/log n), -> 0 but too slow
       (C*_LS(n) = n * 2 log2 / log n -> infinity)

  To reach C*<=2.80 for ALL n, the per-prime saving must COMPOUND so the LEVEL itself
  rises with n: theta_0(n) = 1 - C*/n -> 1. Known mechanisms do NOT deliver this:
    - uniform per-prime beyond-Weil  -> level fixed (d^{1/2-varpi}, exponent unchanged).
    - iterated q-van der Corput / exponent pairs -> converge to a POSITIVE fixed point
      (kappa_infty ~ 0.16), NOT to level 1.
    - large-sieve sparsity helps Type I, but Type II (binding) stays Weil-capped.
  So level -> 1 (= primorial Elliott-Halberstam) is the genuine requirement, and it is NOT
  produced by assembling Wright + Burgess + Polymath-8 + large sieve.""")

# ---- verdict -------------------------------------------------------------------------
print("=" * 86)
print("VERDICT")
print("=" * 86)
print(f"""  * SMALL n (<= {int(n_star_p)}): target 1-2.8/n <= {THETA_POLY8:.3f} IS reached by beyond-Weil
    (Wright / Polymath-8). C*<=2.80 holds. Matches 'n<=6 discharged'.
  * LARGE n: target 1-2.8/n -> 1 EXCEEDS the fixed Type-II cap ~0.55. C*_achieved(n)
    = n(1-theta_bW) ~ 0.45 n GROWS, blowing past 2.80 at n~6-7. NOT reached.
  * The bridge (diez Thm 4.3) needs the level for ALL n -> infinity, i.e. theta_0 -> 1 =
    primorial Elliott-Halberstam. The assembled machinery gives a FIXED level ~0.55, not
    -> 1. The gap is the deficit RATE (fixed/O(1/log n) vs needed O(1/n)) -- a Type-II Weil
    barrier, NOT a constant to tune.

  HONEST: C*<=2.80 is NOT delivered by assembling current unconditional tools. diez's own
  label ('conjectural calibration', 'specialist verification') is right, and the assembly
  pins WHY: the binding Type-II beyond-Weil level is fixed (~0.51-0.55), while the bridge
  needs it -> 1. The terminus is in the Elliott-Halberstam difficulty class for primorial
  moduli -- conservation of difficulty: RH-hard -> primorial-EH-hard. Small primorials
  (n<=6) genuinely discharge; the large-n asymptotic is the wall, and it is the SAME wall
  (EH/GRH-strength), not a Polymath-8 constant chase.""")
