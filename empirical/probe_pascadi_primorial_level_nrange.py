"""
N1 -- Pascadi handoff into Paper 43 primorial-BV: the EXACT level / n-range crossover.

Setup (Paper 43 obligation, ocho 7 V/M crossover):  primorial-BV at level theta_0(p_n) = 1 - C*/n,
C* = 2.80 = 14/5.  Classical BV gives theta = 1/2 (no Kloosterman).  Beyond 1/2 needs the dispersion
method with a Type-II bilinear-Kloosterman input.  After iterated completion (Paper 43 5), the Type-II
sum is Pascadi's object  sum a_k b_h S(a k, h; q)  over DUAL variables of length ~ q/M ~ X^{theta-1/2}
<< q^{1/2}  (theta<=1), i.e. Pascadi's regime.  On primorial divisors q | P_n (squarefree, divisor
d ~ sqrt(q)) Pascadi Ex 1.3 gives saving  q^{-1/12}  (eta = 1/12), with the 2^{omega(q)} = 2^n divisor
penalty ABSORBED into q^{o(1)} (removing Paper 43's r0=5 saturation).

Level translation (BFI/Polymath8):  theta = 1/2 + g,  gain g = kappa * eta,  kappa in (0,1] the
dispersion efficiency (NOT pinned here -- the standard Polymath8 bookkeeping).  CEILING: g <= eta
(reference kappa=1).  This script computes, EXACTLY, the required gain g_req(n) = theta_0(n) - 1/2 per
primorial row, and classifies each n as: classical (g_req<=0) / Pascadi-reachable (0<g_req<=eta, with
the needed efficiency kappa_min = g_req/eta) / out-of-reach (g_req>eta).

This is the EXACT arithmetic gate for the n-range; the level constant kappa is the honest open piece.
"""
import sympy as sp

C_star = sp.Rational(14, 5)     # 2.80, the V/M crossover constant (ocho 7)
eta = sp.Rational(1, 12)        # Pascadi Ex 1.3 saving exponent on primorial divisors (d ~ sqrt q)
half = sp.Rational(1, 2)

print("Pascadi -> primorial-BV: exact level / n-range crossover")
print(f"  C* = {C_star} = {float(C_star):.2f}   Pascadi saving eta = 1/12 = {float(eta):.4f}")
print(f"  theta_0(n) = 1 - C*/n ;  required gain g_req(n) = theta_0(n) - 1/2")
print("=" * 78)
print(f"  {'n':>2} | {'theta_0(n)':>12} | {'g_req':>10} | {'kappa_min':>10} | verdict")
print("  " + "-" * 74)

n_max_pascadi = None
for n in range(4, 13):
    theta0 = 1 - C_star / n
    g_req = theta0 - half
    if g_req <= 0:
        verdict = "classical BV (theta_0 <= 1/2), no Kloosterman needed"
        kmin = "-"
    elif g_req <= eta:
        kmin_val = g_req / eta
        kmin = f"{float(kmin_val):.3f}"
        verdict = f"PASCADI-REACHABLE if dispersion efficiency kappa >= {float(kmin_val):.2f}"
        n_max_pascadi = n
    else:
        kmin = f"{float(g_req/eta):.3f}"
        verdict = "OUT (needs gain > eta=1/12, beyond Pascadi even at kappa=1)"
    print(f"  {n:>2} | {str(theta0):>12} | {str(g_req):>10} | {kmin:>10} | {verdict}")
    if n in (6, 7):
        pass

print("  " + "-" * 74)
print(f"  exact crossover: g_req(n) <= eta  <=>  1/2 - C*/n <= 1/12  <=>  n <= "
      f"{sp.nsimplify(C_star/(half-eta))} = {float(C_star/(half-eta)):.3f}")
print(f"  => n_max reachable by Pascadi = {n_max_pascadi}  (n>=7 needs g_req >= 1/10 > 1/12)")
print("=" * 78)
print("VERDICT (N1).  Pascadi's completed-Type-II handoff secures the primorial-BV obligation up to")
print("n = 6 (provided the standard dispersion efficiency kappa >= 2/5 = 0.40 -- the Polymath8")
print("bookkeeping, the one open constant), and repairs Paper 43's flawed derivation + r0=5 saturation")
print("(2^n divisor penalty absorbed in q^{o(1)}).  n = 7 (theta_0 = 0.60) is OUT even at kappa=1")
print("(needs gain 1/10 > 1/12).  n <= 5 is classical BV.  The n -> infinity tail (theta_0 -> 1) is")
print("Elliott-Halberstam on smooth moduli -- open, untouched by Pascadi.")
print("  Net advance over classical BV: exactly the single row n = 6, on a CORRECT architecture.")
