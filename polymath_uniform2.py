"""
Make the large-q positivity fully rigorous with explicit constants.

N_q(-2q + s q) = A4(s) q^4 + A3(s) q^3 + A2(s) q^2 + A1(s) q + A0
  A4 = (2-s)^2 (1-s)        [ = -(s-2)^2(s-1) ]
  A3 = -(s-2)(s^2+11s-11) = (2-s)(s^2+11s-11)
  A2 = -2(19 s^2 - 42 s + 42)
  A1 = -341(s-2) = 341(2-s)
  A0 = -988
We want N >= 0 on the binding window. The binding window in s is
  s in [1 - q'/q, 1 - q''/q],  q'' < q < q' consecutive primes.
By Bertrand, q' < 2q => 1 - q'/q > -1, and q'' >= 2 => 1 - q''/q < 1.  So s in (-1, 1).
We will prove N_q(-2q+sq) >= 0 for ALL real s in [-1, 1 - eps] ... but at s->1 (i.e. B->-(q''+q)
corner with q''->? ) need care. Actually the UPPER corner s = 1 - q''/q can approach 1 only if
q'' / q -> 0, impossible for consecutive primes (q'' = prevprime(q) ~ q). For q large, q''/q -> 1
so upper s -> 0+. And lower s = 1 - q'/q -> 0- . So the REAL window shrinks to {0}!
The window [1-q'/q, 1-q''/q] has width (q'-q'')/q = (gap)/q -> 0.
=> For large q, s stays in a TINY nbhd of 0, where A4(0)=4>0 dominates.

Rigorous plan:
(1) Pick s0 = 1/2. Show: for ALL s in [-1, 1/2] and ALL q >= Q0, N_q(-2q+sq) > 0.
    On s in [-1,1/2], A4(s) = (2-s)^2(1-s) >= (2-1/2)^2*(1-1/2) = (3/2)^2*(1/2)=9/8 >0,
    and is bounded; A3,A2,A1,A0 bounded on compact s-range. So for q large enough the q^4 term wins.
    Get explicit Q0 by bounding |A3|,|A2|,|A1|,|A0| on [-1,1/2] and requiring
       A4_min q^4 > |A3|_max q^3 + |A2|_max q^2 + |A1|_max q + |A0|_max.
(2) For q < Q0: the binding window has s in [1-q'/q, 1-q''/q] ⊆ (-1,1). We separately verified
    (exact, primes up to 7927) that N_q>=0 on each actual piece. As long as Q0 <= 7927 we are done
    for all q (small q by finite exact check, large q by (1)), PROVIDED for q>=Q0 the actual window
    s in [1-q'/q, 1-q''/q] ⊆ [-1, 1/2]. Upper end 1-q''/q <= 1/2  <=>  q'' >= q/2, true by Bertrand
    (prevprime(q) > q/2). Lower end 1-q'/q >= -1 <=> q' <= 2q, true by Bertrand. GOOD.
So we need Q0 with: (a) Q0 <= 7927, (b) for q>=Q0, q^4 term dominates on s in[-1,1/2].
"""
from sympy import symbols, Rational, Poly, expand, factor, S, nsimplify, diff, solve, Abs
import sympy as sp

s = symbols('s', real=True)
A4 = (2-s)**2*(1-s)
A3 = (2-s)*(s**2+11*s-11)
A2 = -2*(19*s**2-42*s+42)
A1 = 341*(2-s)
A0 = S(-988)

# On s in [-1, 1/2]: bound each coefficient.
lo, hi = S(-1), Rational(1,2)
def extremes(expr):
    # min and max of polynomial expr on [lo,hi]: endpoints + interior crit pts
    cps = solve(sp.Eq(diff(expr,s),0), s)
    cand=[lo,hi]+[c for c in cps if c.is_real and lo<=c<=hi]
    vals=[expr.subs(s,c) for c in cand]
    return min(vals), max(vals)

A4min,A4max = extremes(A4)
A3min,A3max = extremes(A3)
A2min,A2max = extremes(A2)
A1min,A1max = extremes(A1)
print("On s in [-1, 1/2]:")
print(f"  A4 in [{A4min},{A4max}]   (need A4min>0): A4min={A4min}={float(A4min):.4f}")
print(f"  A3 in [{A3min},{A3max}]")
print(f"  A2 in [{A2min},{A2max}]")
print(f"  A1 in [{A1min},{A1max}]")
print(f"  A0 = {A0}")
A3abs = max(abs(A3min),abs(A3max))
A2abs = max(abs(A2min),abs(A2max))
A1abs = max(abs(A1min),abs(A1max))
A0abs = abs(A0)
print(f"\n  |A3|<= {A3abs}, |A2|<= {A2abs}, |A1|<= {A1abs}, |A0|<= {A0abs}, A4>= {A4min}")
# Need A4min q^4 - A3abs q^3 - A2abs q^2 - A1abs q - A0abs > 0.
q = symbols('q', positive=True)
G = A4min*q**4 - A3abs*q**3 - A2abs*q**2 - A1abs*q - A0abs
print("\n  Dominance polynomial G(q) =", expand(G))
# find largest real root
rr = solve(sp.Eq(G,0), q)
rrr = [r for r in rr if r.is_real]
print("  real roots of G:", [float(r) for r in rrr])
Q0_needed = max([float(r) for r in rrr])
print(f"  => G(q)>0 for q > {Q0_needed:.4f}. Take Q0 = {int(Q0_needed)+1}.")
print(f"  Q0 <= 7927 ? {int(Q0_needed)+1 <= 7927}")
# sanity: G at a few q
for qq in [10, 15, 20, 30, 50]:
    print(f"    G({qq}) = {G.subs(q,qq)}")
