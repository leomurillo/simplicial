"""
Q in ratio variables. Let u=x/w, v=y/x, s=z/y (consecutive ratios >1 for increasing f).
Q = w*x^2 - 2 w x y + w y z + x y^2 - x y z.
Substitute x=w u, y=w u v, z=w u v s. Factor Q / (lowest power of w).
"""
from sympy import symbols, factor, simplify, expand, collect, Poly

w,u,v,s = symbols('w u v s', positive=True)
x=w*u; y=w*u*v; z=w*u*v*s
Q = w*x**2 - 2*w*x*y + w*y*z + x*y**2 - x*y*z
Qs = expand(Q)
print("Q in (w,u,v,s):", factor(Qs))

# divide by w^2 u  (lowest monomial)
import sympy
g = simplify(Qs / (w**2 * u))
print("\nQ/(w^2 u) =", factor(g))
print("expanded:", expand(g))

# This should be independent of w now? check
print("\nfree symbols of Q/(w^2 u):", g.free_symbols)

# Express as polynomial; analyze sign. Q>0 <=> g>0 (since w^2 u>0).
# collect in s
gs = collect(expand(g), s)
print("\ncollected in s:", gs)
# coefficient of s and constant
from sympy import Symbol
gpoly = Poly(expand(g), s)
print("as poly in s, coeffs (high->low):", gpoly.all_coeffs())
# So g = A*s + B with:
A = gpoly.all_coeffs()[0]
B = gpoly.all_coeffs()[1]
print("A (coeff of s) =", factor(A))
print("B (constant)   =", factor(B))
print("=> g>0  <=>  A*s + B > 0")
print("   A = u*v^2*(1 - v)  [check]:", factor(A - u*v**2*(1-v))==0)
print("   B = u + u v^2 - 2 u v ... [check]:")
print("   B factored:", factor(B))
