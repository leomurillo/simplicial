"""
Degree 3 analysis:
(a) Is coeffE = 912B^2+60BC+41340B+C^2+1342C+474285 > 0 for all (B,C)? (quadratic form + linear)
(b) On the binding-2 region (Q_3=5B+C+19>0, and B>-8), is Psi3_edge>0 ? If yes => M234<0 there.
(c) Where does the cubic's overall first-failure live? Sample the (B,C,E) valid region.
"""
import os; os.makedirs(r"C:\Projects\simplicial\polymath_certs",exist_ok=True)
from sympy import symbols, factor, expand, Poly, simplify, solve, S, primerange, Matrix, Integer, Rational, hessian
import sympy as sp
import numpy as np

B,C,E=symbols('B C E', real=True)

# (a) coeffE positivity
coeffE = 912*B**2 + 60*B*C + 41340*B + C**2 + 1342*C + 474285
# It's quadratic in (B,C). Min over all (B,C): solve grad=0.
gB=coeffE.diff(B); gC=coeffE.diff(C)
sol=solve([gB,gC],[B,C],dict=True)
print("(a) coeffE critical point:", sol)
for so in sol:
    val=coeffE.subs(so)
    print("    coeffE at crit =", val, "=", float(val))
# Hessian
H=hessian(coeffE,[B,C])
print("    Hessian:",H.tolist()," det=",H.det()," (>0 & H11>0 => convex => min is global)")
print("    => coeffE_min =", float(coeffE.subs(sol[0])), "(>0 => coeffE>0 everywhere => Psi3 incr in E)")

# (b) Psi3_edge on binding region. Psi3_edge is cubic in (B,C).
Psi3_edge = (58320*B**3 + 10140*B**2*C + 2831100*B**2 + 481*B*C**2 + 380198*B*C
             + 40096501*B + 7*C**3 + 9395*C**2 + 3522649*C + 124436109)
# binding-2 region (for B>-8): Q_3=5B+C+19>0 i.e. C>-5B-19. Also need f(2)>0 which is the edge (E side).
# Sample (B,C) with C>-5B-19 (binding region) and check Psi3_edge>0.
Pe=sp.lambdify((B,C),Psi3_edge,'numpy')
bad=[]; mn=None
for Bv in np.linspace(-8,200,500):
    Clo=-5*Bv-19
    for Cv in np.linspace(Clo+1e-3, Clo+3000, 200):
        v=Pe(Bv,Cv)
        if mn is None or v<mn: mn=v; mnat=(Bv,Cv)
        if v<=0: bad.append((round(Bv,2),round(Cv,2),v))
print("\n(b) Psi3_edge on binding-2 region (B in[-8,200], C>-5B-19):")
print("    min Psi3_edge =",mn," at",mnat)
print("    Psi3_edge<=0 occurrences:",len(bad)," sample:",bad[:6])
print("    => if 0 occurrences, M234<0 on binding-2 region.")
