"""
Per-piece interior check: for each prime q = p_k (k>=1), N_q(B) >= 0 for ALL real B in
the closed corner-interval [-(q+q'), -(q''+q)]  (q''=prev prime, q'=next prime).
N_q is a cubic in B. We check it has NO root in the OPEN interval and is >=0 at endpoints
(endpoints already shown >=0). Equivalent: min of N_q over the closed interval >= 0.
Since N_q is a real cubic, its min on a closed interval is at an endpoint or a critical point
inside. We compute critical points (N_q'(B)=0) exactly and evaluate N_q there if inside.
Do this for k=1..1000 (primes up to ~8000) with EXACT arithmetic.
"""
from sympy import symbols, primerange, diff, solve, Rational, expand, S, nsimplify, re, im
import sympy as sp

B = symbols('B', real=True)
P = list(primerange(2, 9000))

def Nq_expr(q):
    return expand((-q*B - q**2)*(B**2+15*B+68) - (B**3+38*B**2+341*B+988))

worst = None
fails = []
import math
for k in range(1, 1001):
    q = P[k]; qprev = P[k-1]; qnext = P[k+1]
    lo = -(q+qnext)   # lower B end
    hi = -(qprev+q)   # upper B end
    N = Nq_expr(q)
    Np = sp.diff(N, B)
    # exact critical points
    crits = sp.solve(sp.Eq(Np, 0), B)
    cand = [S(lo), S(hi)]
    for c in crits:
        if c.is_real and (lo < c) and (c < hi):
            cand.append(c)
    vals = [N.subs(B, c) for c in cand]
    mn = min(vals)
    mnf = float(mn)
    if worst is None or mnf < worst[0]:
        worst = (mnf, q, [(str(c), float(N.subs(B,c))) for c in cand])
    if mn < 0:
        fails.append((q, lo, hi, mnf))

print(f"Checked k=1..1000 (primes 3..{P[1000]}). Interior+endpoint min of N_q over each corner-interval.")
print("FAILS (min<0):", fails[:20], "(empty => N_q>=0 on every piece => detW2<0 on all valid B<=-5)")
print("Worst (smallest) min over all pieces:", worst[0], "at q=", worst[1])
print("   candidates at worst piece:", worst[2])
