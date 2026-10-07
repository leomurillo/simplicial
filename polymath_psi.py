"""
M234 = -12 * [prod of f(p_k), k=1..6, with multiplicities] * Psi(B,C),
Psi = 9B^3 + B^2 C + 605 B^2 + 60 B C + 12204 B + 912 C + 61968.
On valid region all f(p_k)>0, so sign(M234) = -sign(Psi). M234<0 <=> Psi>0.
We need M234<0 on the Phi<=0 sliver, i.e. Psi>0 there. Analyze Psi.
Psi is LINEAR in C: Psi = (B^2+60B+912) C + (9B^3+605B^2+12204B+61968).
"""
from sympy import symbols, factor, expand, Poly, solve, S, Rational, primerange, lambdify, simplify
import sympy as sp
import numpy as np

B,C=symbols('B C', real=True)
Psi = 9*B**3 + B**2*C + 605*B**2 + 60*B*C + 12204*B + 912*C + 61968
pC=Poly(Psi,C)
coeffC = Psi.diff(C); constC = expand(Psi - coeffC*C)
print("Psi linear in C:")
print("  coeff of C:", factor(coeffC))        # B^2+60B+912
print("  const term:", factor(constC))        # 9B^3+605B^2+12204B+61968
print("  disc(B^2+60B+912) =", 60**2-4*912, "(<0 => coeffC>0 for all B)")
# coeffC>0 always => Psi increasing in C. Psi>0 <=> C > C2*(B) := -constC/coeffC.
C2star = simplify(-constC/coeffC)
print("\n  Psi>0 <=> C > C2*(B),  C2*(B) = -(9B^3+605B^2+12204B+61968)/(B^2+60B+912)")
print("  factor numerator 9B^3+605B^2+12204B+61968:", factor(9*B**3+605*B**2+12204*B+61968))

# We need Psi>0 on the sliver. Sliver lower edge is C = -2B-4 (f(2)=0+). Check Psi at C=-2B-4:
Psi_edge = factor(Psi.subs(C, -2*B-4))
print("\n  Psi at C = -2B-4 (f(2)=0 edge):", Psi_edge)
print("   -> if >0 on the relevant B-range, the WHOLE sliver (which is just above this edge... ")
print("      but Psi increasing in C, so Psi(edge) is the MINIMUM over C>=edge) is Psi>0. KEY.")

# Evaluate Psi_edge sign for B in (-5, ~7) (sliver B-range) and beyond:
Psi_edge_f=lambdify(B,Psi.subs(C,-2*B-4),'numpy')
print("\n  Psi(C=-2B-4) at sample B:")
for Bv in [-5,-4.9,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,10,20]:
    print(f"    B={Bv}: Psi_edge={Psi_edge_f(Bv):.3f}")
print("\n  roots of Psi_edge:", [sp.nsimplify(r) for r in solve(sp.Eq(Psi.subs(C,-2*B-4),0),B) if r.is_real])
