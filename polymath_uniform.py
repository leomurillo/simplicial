"""
UNIFORM (large-q) rigor for N_q(B) >= 0 on the binding piece.

We had  N_q(-2q+t) = (-q-1) t^3 + (q+2)(5q-19) t^2 + (-8q^3+33q^2+84q-341) t
                      + 2(2q^4 - 11 q^3 - 42 q^2 + 341 q - 494).

On the q-piece, B in [-(q+q'), -(q''+q)] so t=B+2q in [q-q', q-q''].
With q'',q' the neighboring primes. Half-gaps: q'-q and q-q''.
By a classical explicit gap bound (e.g. q' - q < q for q>=2, Bertrand; in fact gap=o(q)),
t lies in a small window around 0. We will prove N_q(-2q+t) >= 0 for ALL t in a GENEROUS
symmetric window |t| <= W(q). If the actual piece-window [q-q', q-q''] ⊆ [-W,W], done.

Take W = q (very generous; Bertrand guarantees q' < 2q so q-q' > -q, and q-q'' < q since q''>=2,
actually q-q'' <= q-2 < q). So the piece ⊆ (-q, q). We prove N_q(-2q+t) >= 0 for |t| <= q?
Let's TEST whether that holds; if not, tighten W. We need the true window only, which is
[q-q', q-q'']. For an elementary uniform bound we use q' - q <= c (won't work, gaps grow).
Better: use t in [q-q', q-q'']; bound |t| by the max prime gap g(q). We KNOW (proved, Baker-
Harman-Pintz, but even Cramer-heuristic-free) g(q) = o(q). For a SELF-CONTAINED bound we can use
the explicit result g(q) < q^{0.6} for all q (holds; even g(q)<3 sqrt(q) log q etc). To keep it
elementary, let's just find the LARGEST window W (as a function of q, e.g. W=alpha*q) on which
N_q(-2q+t)>=0, by analyzing the cubic. Then note any sub-quadratic gap bound puts the piece
well inside for large q, and the finite check covers small q.
"""
from sympy import symbols, expand, factor, Poly, Rational, S, sqrt, simplify, limit, oo
import sympy as sp

q, t, s = symbols('q t s', positive=True)

N = (-q-1)*t**3 + (q+2)*(5*q-19)*t**2 + (-8*q**3+33*q**2+84*q-341)*t \
    + 2*(2*q**4 - 11*q**3 - 42*q**2 + 341*q - 494)

# Idea: write t = s*q (s = t/q = (B+2q)/q, the RELATIVE deviation). Piece window in s:
#   s in [ (q-q')/q, (q-q'')/q ] = [ 1 - q'/q, 1 - q''/q ]. As q->oo with gaps o(q), s->0.
Ns = expand(N.subs(t, s*q))
print("N_q(-2q + s q) expanded:")
Ns_poly = Poly(Ns, q)
print("  As polynomial in q (coeffs in s):")
for deg, coeff in zip(range(Ns_poly.degree(), -1, -1), Ns_poly.all_coeffs()):
    print(f"    q^{deg}: {factor(coeff)}")

# Leading term in q (q^4) coefficient as function of s -> dominates for large q.
lead = Ns_poly.all_coeffs()[0]
print("\nLeading q^4 coefficient (function of s):", factor(lead))
print("  -> This must be >0 for the window where large-q positivity holds.")
print("  roots in s of leading coeff:", sp.solve(sp.Eq(lead,0), s))
