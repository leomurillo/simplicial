"""
Derive the gap-form of det W_3, analogous to det W_2 = c3 g1 g3 - c1 g2^2.
det W_3 in c1..c6. Substitute gaps g_l=c_{l+1}-c_l and look for clean structure.
"""
from sympy import symbols, simplify, factor, expand, collect, Integer

c1,c2,c3,c4,c5,c6 = symbols('c1 c2 c3 c4 c5 c6', positive=True)
d3 = (c1*c2**2*c3**3 - 3*c1*c2**2*c3**2*c4 + c1*c2**2*c3*c4**2 + 2*c1*c2**2*c3*c4*c5
      - c1*c2**2*c4*c5*c6 + 2*c1*c2*c3**2*c4**2 - 2*c1*c2*c3**2*c4*c5
      - 2*c1*c2*c3*c4**2*c5 + 2*c1*c2*c3*c4*c5*c6 + c1*c3*c4**2*c5**2
      - c1*c3*c4**2*c5*c6 - c2*c3**2*c4**3 + 2*c2*c3**2*c4**2*c5
      - c2*c3**2*c4*c5*c6 - c2*c3*c4**2*c5**2 + c2*c3*c4**2*c5*c6)

g1,g2,g3,g4,g5 = symbols('g1 g2 g3 g4 g5')
sub = {c2: c1+g1, c3: c1+g1+g2, c4: c1+g1+g2+g3, c5: c1+g1+g2+g3+g4, c6: c1+g1+g2+g3+g4+g5}
d3g = expand(d3.subs(sub))
d3g_c = collect(d3g, c1)
print("det W_3 in (c1, g1..g5), collected by c1:")
print(d3g_c)
print()
# Get coefficient of each power of c1
from sympy import Poly
pol = Poly(d3g, c1)
for (deg,), coef in pol.terms():
    print(f"  c1^{deg} coeff:", factor(coef))
