"""
Cleaner Region A: det W_2 = 2*g2, g2 decreasing in C. On piece with binding prime q,
validity => C > -qB-q^2, so g2(B,C) < g2(B,-qB-q^2). Want g2(B,-qB-q^2) <= 0 on the piece.
Compute g2 at C=-qB-q^2 symbolically in q,B and factor.
"""
from sympy import symbols, factor, expand, primerange, simplify, Poly, collect, S
import sympy as sp
B,C,q=symbols('B C q', real=True)
g2 = B**3 - B**2*C + 38*B**2 - 15*B*C + 341*B - 68*C + 988
g2_edge = expand(g2.subs(C, -q*B - q**2))
print("g2 at C=-qB-q^2 (binding-prime edge), as poly:")
print("  raw:", g2_edge)
print("  collected in B:", collect(g2_edge, B))
print("  factor:", factor(g2_edge))
# This equals -N_q (we defined N_q = (Cmin-Cstar)*den earlier, and detW_2=2*g2; let's relate)
# We want g2_edge <= 0 on the q-piece B-interval. Substitute B=-2q+t (t=B+2q):
g2_sub = expand(g2_edge.subs(B,-2*q+t if False else -2*q+symbols('t')))
t=symbols('t', real=True)
g2_sub=expand(g2_edge.subs(B,-2*q+t))
print("\n  g2_edge at B=-2q+t:")
print("   collected in t:", collect(g2_sub,t))
# in relative var s=t/q:
s=symbols('s', real=True)
g2_s=expand(g2_sub.subs(t,s*q))
print("\n  g2_edge at B=-2q+s q, as poly in q:")
pq=Poly(g2_s,q)
for d,co in zip(range(pq.degree(),-1,-1), pq.all_coeffs()):
    print(f"     q^{d}: {factor(co)}")
print("\n  leading q^3 coeff (function of s):", factor(pq.all_coeffs()[0]))
print("  roots in s of leading coeff:", sp.solve(sp.Eq(pq.all_coeffs()[0],0),s))
