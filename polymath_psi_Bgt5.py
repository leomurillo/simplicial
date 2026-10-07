"""
GOAL: Prove Psi(B,C) > 0 on the valid region with B > -5 (where binding prime is 2, Cmin=-2B-4).
Then M234 = -12*[f(p_k)>0 products]*Psi < 0 there, closing B>-5.

Psi = (B^2+60B+912) C + (9B^3+605B^2+12204B+61968), coeff of C is B^2+60B+912>0 (disc=-48<0).
=> Psi increasing in C. On B>-5 valid, C>-2B-4, so
   Psi(B,C) > Psi(B,-2B-4) = E2(B) := 7B^3+481B^2+10140B+58320.
Need E2(B) >= 0 for all B >= -5 (then Psi>0 strictly for C>-2B-4).
Prove: E2(B) = 7B^3+481B^2+10140B+58320.
  - E2 is a cubic with positive leading coeff.
  - Show E2(B) > 0 for all B >= -5  by: E2(-5)=?, and E2 increasing for B>=-5 (E2'>=0)? or min>0.
"""
from sympy import symbols, factor, expand, diff, solve, S, Rational, sqrt, Poly, re, im, nsimplify
import sympy as sp

B=symbols('B', real=True)
E2 = 7*B**3 + 481*B**2 + 10140*B + 58320
print("E2(B) =", E2)
print("E2(-5) =", E2.subs(B,-5))
print("E2 factored:", factor(E2))
# real roots
roots=solve(sp.Eq(E2,0),B)
realroots=[r for r in roots if r.is_real]
print("real roots of E2:", [float(r) for r in realroots], " exact:", [nsimplify(r) for r in realroots])
print("# real roots:", len(realroots))
# E2' :
E2p=diff(E2,B)
print("\nE2'(B) =", expand(E2p), " = ", factor(E2p))
disc_E2p = 962**2 - 4*21*10140   # for 21B^2+962B+10140
print("disc(E2') = disc(21B^2+962B+10140) =", disc_E2p)
crits=solve(sp.Eq(E2p,0),B)
print("critical points of E2:", [float(c) for c in crits if c.is_real])
# Determine min of E2 on [-5, inf):
# if E2 monotincreasing on [-5,inf) (E2'>=0 there) then min at B=-5.
for c in crits:
    if c.is_real:
        print(f"  E2 at crit {float(c):.4f}: {float(E2.subs(B,c)):.3f}")
# Sign of E2' at B=-5 and large B:
print("E2'(-5) =", E2p.subs(B,-5), " E2'(0)=", E2p.subs(B,0))
print("\nConclusion check: is E2(B)>0 for ALL B>=-5?")
# Evaluate E2 on a sweep
import numpy as np
E2f=sp.lambdify(B,E2,'numpy')
xs=np.linspace(-5,1000,200000)
print("  min E2 on [-5,1000]:", E2f(xs).min(), "at B=", xs[np.argmin(E2f(xs))])
print("  E2 large-B leading term 7B^3>0 => +inf. So global min on [-5,inf) is in the sweep.")
