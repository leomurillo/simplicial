"""
Analyze the valid region for monic quadratic f(p)=p^2+Bp+C > 0 for all primes p,
and the sign of det W_2 = 2*(B^3 - B^2 C + 38 B^2 - 15 B C + 341 B - 68 C + 988).
"""
from sympy import symbols, factor, expand, simplify, solve, Poly, Rational, oo, S
import sympy as sp

B, C, p = symbols('B C p', real=True)

# det W_2 inner factor
g2 = B**3 - B**2*C + 38*B**2 - 15*B*C + 341*B - 68*C + 988
# Solve det W_2 = 0 for C (it's linear in C):
g2_C = sp.collect(expand(g2), C)
print("det W_2 inner factor, collected in C:")
print("  g2 =", g2_C)
# coefficient of C and constant:
coeffC = g2.diff(C)
const = (g2 - coeffC*C)
coeffC = simplify(coeffC); const = simplify(const)
print("  coeff of C:", coeffC)             # = -(B^2+15B+68)
print("  const (C=0):", expand(const))     # = B^3+38B^2+341B+988
print("  factor coeffC:", factor(coeffC))
print("  factor const:", factor(const))

# So g2 = const + coeffC * C = (B^3+38B^2+341B+988) - (B^2+15B+68) C
# det W_2 = 0  <=>  C = (B^3+38B^2+341B+988)/(B^2+15B+68)
Cstar = simplify(const/(-coeffC))   # value of C making det W_2 = 0
print("\n  C* (root, where detW2=0):  C =", factor(Cstar))
print("  i.e. C* =", expand(Cstar))

# sign: coeffC = -(B^2+15B+68).  Discriminant of B^2+15B+68:
disc = 15**2 - 4*68
print("\n  disc(B^2+15B+68) =", disc, "(<0 => always positive) => coeffC < 0 for ALL real B")
print("  => det W_2 is a DECREASING linear function of C.")
print("  => det W_2 < 0  <=>  C > C*(B).")

print("\n  factor(B^2+15B+68):", factor(B**2+15*B+68))   # irreducible over reals
