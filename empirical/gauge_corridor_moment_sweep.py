#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gauge_corridor_moment_sweep.py

T0 frame: "what is additive?"  The moment (Hankel) problem is the r=2 (quadratic/Born)
gauge.  Sweep the power-mean gauge exponent rho and ask: for which rho is the gauged
primorial a Hamburger moment sequence?

  f(p) = p^rho   =>   b_n = prod_{i<=n} p_i^rho = P_n^rho   (rho-th power of the primorial).

  rho = 0  : b_n = 1            (delta_1; trivially MOMENT)          [geometric gauge limit]
  rho = 1  : b_n = P_n          (the primorial; NON-moment, D_3<0)   [arithmetic]
  rho = 2  : b_n = P_n^2        (RMS/energy gauge)
  rho < 0  : b_n = P_n^rho      decreasing (harmonic side; Hausdorff-like?)

A single Hankel D_N < 0 proves NON-moment at that gauge.  N*(rho) = first failure index
(None = moment through N=NMAX).  Sign read at high precision and re-checked at higher
precision for robustness.  We ALSO record log-convexity (the r=0 regularity), which the
primorial passes for ALL rho>0.

Deterministic; mpmath.  Run: python gauge_corridor_moment_sweep.py
"""
import sys
import mpmath as mp
from sympy import primerange

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PRIMES = list(primerange(2, 300))
def primorials(M):
    P = [1]; a = 1
    for i in range(1, M):
        a *= PRIMES[i-1]; P.append(a)
    return P                      # P[n] = n-th primorial (exact int)

def first_neg_Hankel(rho, NMAX, dps):
    """b_n = P_n^rho ; return first N with Hankel det < 0 (None if all >0 thru NMAX)."""
    mp.mp.dps = dps
    P = primorials(2*NMAX + 2)
    Pr = [mp.mpf(p) ** mp.mpf(rho) for p in P]     # P_n^rho at precision dps
    for N in range(NMAX + 1):
        H = mp.matrix(N+1, N+1)
        for i in range(N+1):
            for j in range(N+1):
                H[i, j] = Pr[i+j]
        d = mp.det(H)
        if d < 0:
            return N, d
    return None, None

def robust_first_neg(rho, NMAX):
    """Read N* at two precisions; agree => robust."""
    a = first_neg_Hankel(rho, NMAX, 80)[0]
    b = first_neg_Hankel(rho, NMAX, 160)[0]
    return a, (a == b)

def hr(): print("=" * 84)

NMAX = 10
hr()
print("GAUGE-CORRIDOR MOMENT SWEEP   b_n = P_n^rho   (N* = first Hankel D_N<0; None=moment)")
print(f"   Hankel tested through N={NMAX}; sign re-checked at dps 80 vs 160 (robust=agree)")
hr()
print("    rho        N*(rho)     verdict                         robust?")
print("    " + "-" * 70)
rhos = [-2.0, -1.0, -0.5, -0.25, -0.1, 0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]
data = []
for rho in rhos:
    Ns, robust = robust_first_neg(rho, NMAX)
    verdict = f"MOMENT (thru N={NMAX})" if Ns is None else f"NON-moment (D_{Ns}<0)"
    data.append((rho, Ns))
    print(f"    {rho:>6.2f}     {str(Ns):>5}       {verdict:<30}  {'yes' if robust else 'NO(!)'}")
hr()

# log-convexity (the r=0 / geometric-gauge regularity): b_n^2 <= b_{n-1} b_{n+1}
# <=> p_n^rho <= p_{n+1}^rho <=> (rho>0: p_n<=p_{n+1} TRUE; rho<0: reversed)
print("LOG-CONVEXITY CHECK (the r=0 geometric-gauge regularity, b_n^2 <= b_{n-1}b_{n+1}):")
print("   For rho>0: ratios p_i^rho are increasing  => b_n LOG-CONVEX (passes) for ALL rho>0.")
print("   For rho<0: ratios p_i^rho are decreasing  => b_n LOG-CONCAVE.")
P = primorials(12)
for rho in (1.0, 0.5, 2.0):
    lc = all((P[n]**rho)**2 <= (P[n-1]**rho)*(P[n+1]**rho) for n in range(1, 10))
    print(f"     rho={rho}:  log-convex on n=1..9 ?  {lc}")
hr()
print("READING printed after run.")
hr()
