"""
det W_2 = c1 (g1 g3 - g2^2) + g1 g3 (g1 + g2),  g_l = c_{l+1}-c_l.

For MONIC f and primes: c_l = f(p_l). g_l = f(p_{l+1}) - f(p_l).
We need det W_2 < 0.

Rewrite: det W_2 = c1 g1 g3 - c1 g2^2 + g1^2 g3 + g1 g2 g3
                 = g1 g3 (c1 + g1 + g2) - c1 g2^2
                 = g1 g3 * c3   -  c1 g2^2      [since c1+g1+g2 = c3]
Wait check: c1 + g1 + g2 = c1 + (c2-c1) + (c3-c2) = c3. YES.
So:
    det W_2 = c3 * g1 * g3  -  c1 * g2^2.

CLEAN!  det W_2 = c3 g1 g3 - c1 g2^2.
=> det W_2 < 0  <=>  c1 g2^2 > c3 g1 g3
=> non-moment-at-N=2  <=>  (g2^2)/(g1 g3) > c3/c1.

Let me VERIFY this clean identity, then test discriminating power.
"""
from sympy import symbols, simplify, factor, expand

c1,c2,c3,c4 = symbols('c1 c2 c3 c4', positive=True)
g1,g2,g3 = symbols('g1 g2 g3')
d2 = -c1*c2**2 + 2*c1*c2*c3 - c1*c3*c4 - c2*c3**2 + c2*c3*c4

clean = c3*g1*g3 - c1*g2**2
sub = {g1: c2-c1, g2: c3-c2, g3: c4-c3}
print("VERIFY det W_2 == c3 g1 g3 - c1 g2^2 :", expand(clean.subs(sub) - d2))
# should be 0

# So the N=2 non-moment criterion:
#   c1 * (c3-c2)^2  >  c3 * (c2-c1) * (c4-c3)         ... (INEQ-2)
print()
print("INEQ-2 (det W_2<0):  c1 (c3-c2)^2 > c3 (c2-c1)(c4-c3)")
print("Equivalently:  (c3-c2)^2 / [(c2-c1)(c4-c3)]  >  c3/c1")
