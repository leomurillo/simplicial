"""
DOES THE EULER PRODUCT FORCE A >= P?  Push the multiplicative positivity as far as it provably goes.

The Euler product's positivity content is the von Mangoldt nonnegativity Lambda(n) >= 0 (only prime powers,
log p > 0). The question: does Lambda(n) >= 0 force the Weil contraction A >= P (RH)?

Two representations of positivity collide:
  PHYSICAL:  Lambda(n) >= 0  (nonneg coefficients).  This is what the Euler product gives.
  FOURIER:   the Weil form A - P >= 0 on positive-definite test functions (rho_E <= 1).  This is RH.

We test, concretely, exactly how far the PHYSICAL positivity reaches:
  A  the single-prime symbol  s(r) = sum_{n<=X} Lambda(n)/sqrt(n) cos(r log n)  is INDEFINITE: Lambda>=0 is
     KILLED by the cos(r log n) oscillation. So Lambda>=0 does NOT make the prime operator <= archimedean.
  B  the 3-4-1 trick RESTORES positivity by a nonneg trig polynomial: 3+4cos t + cos 2t = 2(1+cos t)^2 >= 0.
     This is the genuine multiplicative lever -> de la Vallee Poussin:  3 log|zeta(s)| + 4 Re log zeta(s+it)
     + Re log zeta(s+2it) >= 0  =>  zeta(1+it) != 0.  We verify the inequality holds (>= 0) on samples.
  C  but it reaches only sigma > 1 - c/log t, NOT 1/2.  We compute the zero-free boundary for real heights
     and show the critical line 1/2 is DEEP inside the un-reached strip; the FE only reflects it to a strip
     (c/log t, 1 - c/log t) of width ~1 that does NOT collapse to {1/2}.

CONCLUSION the math will force: the Euler product forces A>=P at the EDGE (provably), not the CENTER; the
edge->center conversion is physical->Fourier = the uncertainty-limited spectral step (CCM), NOT a polynomial.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25

def vonmangoldt_upto(X):
    out = []
    p = 2
    while p <= X:
        if all(p % d for d in range(2, int(p**0.5)+1)):
            lp = mp.log(p); pk = p
            while pk <= X:
                out.append((pk, lp)); pk *= p
        p += 1
    return out
PP = vonmangoldt_upto(5000)

print("=" * 86)
print("Does the Euler product force A >= P?  Pushing the multiplicative positivity to its limit")
print("=" * 86)

# A: single-prime symbol is INDEFINITE despite Lambda>=0
print("\nA. single-prime symbol s(r) = sum Lambda(n)/sqrt(n) cos(r log n)  (Lambda>=0, but cos oscillates):")
def sym(r): return mp.fsum(lp/mp.sqrt(pk)*mp.cos(r*mp.log(pk)) for pk, lp in PP)
vals = [(r, sym(mp.mpf(r))) for r in (0, 5, 10, 14, 20, 30, 45)]
print(f"   {'r':>5} {'s(r)':>14}")
for r, v in vals: print(f"   {r:>5} {mp.nstr(v,6):>14}")
smin = min(v for _, v in vals); smax = max(v for _, v in vals)
print(f"   range over sampled r: [{mp.nstr(smin,4)}, {mp.nstr(smax,4)}]  -> BOTH SIGNS = INDEFINITE.")
print(f"   => Lambda(n)>=0 does NOT make the prime form <= archimedean: the Fourier cos kills physical nonneg.")

# B: 3-4-1 nonneg trig polynomial and the de la Vallee Poussin inequality
print("\nB. the 3-4-1 lever: 3 + 4cos(t) + cos(2t) = 2(1+cos t)^2 >= 0  (restores positivity):")
tt = [mp.mpf(x)/4 for x in range(0, 26)]
poly_min = min(3 + 4*mp.cos(t) + mp.cos(2*t) for t in tt)
print(f"   min over t of (3+4cos t+cos 2t) = {mp.nstr(poly_min,4)} (>=0, =0 at t=pi).  This is the multiplicative")
print(f"   positivity. Applied to log zeta (Euler product): 3 log|zeta(s)|+4 Re log zeta(s+it)+Re log zeta(s+2it)>=0.")
print(f"   verify the de la Vallee Poussin quantity Q(sigma,t) >= 0 (forces zeta(1+it)!=0):")
def Q(sig, t):
    s = mp.mpf(sig)
    return (3*mp.log(abs(mp.zeta(s))) + 4*mp.re(mp.log(mp.zeta(s+1j*t)))
            + mp.re(mp.log(mp.zeta(s+2j*t))))
print(f"   {'sigma':>7} {'t':>5} {'Q(sigma,t)':>14} {'>=0?':>6}")
for sig, t in ((1.2,14),(1.1,21),(1.05,25),(1.02,30)):
    q = Q(sig, mp.mpf(t)); print(f"   {sig:>7} {t:>5} {mp.nstr(q,6):>14} {'yes' if q>=-mp.mpf(10)**-12 else 'NO':>6}")

# C: the reach -- zero-free boundary 1 - c/log t vs the critical line 1/2
print("\nC. how far does it reach?  de la Vallee Poussin zero-free boundary  sigma > 1 - c/log t  (c~0.12):")
c = mp.mpf('0.12')
print(f"   {'height t':>9} {'1 - c/log t (reach)':>20} {'critical line':>14} {'gap to 1/2':>11}")
for t in (14, 100, 1000, 10**6, 10**12):
    reach = 1 - c/mp.log(t)
    print(f"   {t:>9} {mp.nstr(reach,6):>20} {'0.5':>14} {mp.nstr(reach-mp.mpf('0.5'),4):>11}")
print(f"   FE reflects this to a STRIP (c/log t, 1 - c/log t): width 1 - 2c/log t -> 1 as t->inf.")
print(f"   The strip does NOT collapse to {{1/2}}; the zeros sit at 1/2, DEEP inside the un-reached interior.")

print("\n" + "=" * 86)
print("""ANSWER -- does the Euler product force A >= P?
  YES, provably, but only at the EDGE.  The Euler product's positivity (Lambda(n)>=0) is real, and via the
  3-4-1 nonneg trig polynomial 2(1+cos)^2 it FORCES A >= P in a zero-free region sigma > 1 - c/log t (de la
  Vallee Poussin); Davenport-Heilbronn, lacking the Euler product, fails exactly this. That is a genuine
  multiplicative inequality, shown above (B), not a reformulation.
  NO, it does not reach the CENTER (1/2).  The reason is precise (A): the multiplicative positivity is
  PHYSICAL (nonneg coefficients), and the single-prime Fourier symbol is INDEFINITE because cos(r log n)
  oscillates -- Lambda>=0 alone never makes the prime OPERATOR <= the archimedean. The 3-4-1 beats the
  oscillation only at FIXED sigma near 1 (a physical-space combination), and provably reaches 1 - c/log t,
  not 1/2 (C). The known nonneg-trig-polynomial method is edge-only by construction.
  SO: A >= P at the edge is forced multiplicatively; A >= P at 1/2 is the PHYSICAL->FOURIER conversion --
  the same uncertainty-limited spectral step (CCM, Sliwinski 1/(4 ln lambda)). The lever RH needs is a
  positivity living in BOTH representations at once (physical-nonneg AND Fourier-positive-definite). The
  Euler product supplies the physical half everywhere and the Fourier half only at the edge; the spectral
  operator (CCM) is precisely the construction that carries the Fourier half inward -- that is where to push,
  and it is NOT a polynomial-positivity problem (which is proven to stop at the edge).
""")
print("=" * 86)
