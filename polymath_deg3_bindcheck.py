"""
For degree 3, precisely characterize the binding-prime-2 region and test whether M234<0 there.
2 binds  <=>  f(2) <= f(p) for ALL primes p>=3  <=>  Q_p(B,C)=p^2+2p+4+B(p+2)+C >= 0 for all p>=3.
(The (p-2) factor is >0.) So binding-2 region in (B,C) = intersection over primes p>=3 of {Q_p>=0}.
Q_p is linear in (B,C): slope in B is (p+2). As p grows these are more constraints.
The region {Q_p>=0 all p>=3} = {(B,C): C >= -(p+2)B - (p^2+2p+4) for all p>=3}
 = upper envelope of lines C = -(p+2)B - (p^2+2p+4). (Like deg-2 Cmin but now in (B,C) for the bracket.)
For B>-8: p=3 line is the binding one? line_p slope -(p+2); steeper for larger p. They cross...
We just need: within the binding-2 region (all Q_p>=0) AND f(2)>0 (E side), is M234<0?
Since Psi3 increasing in E (coeffE>0 except tiny ellipse at B=-45), and validity in binding-2
region <=> f(2)>0 <=> E>-(4B+2C+8): Psi3 >= Psi3_edge. Need Psi3_edge>0 on binding-2 region.
TEST exactly: sample (B,C) in binding-2 region, compute Psi3_edge, check>0. Use the TRUE region
(all Q_p>=0), not just Q_3.
"""
from sympy import symbols, primerange, lambdify, Rational
import sympy as sp
import numpy as np
B,C=symbols('B C', real=True)
P=list(primerange(2,2000))

Psi3_edge = (58320*B**3 + 10140*B**2*C + 2831100*B**2 + 481*B*C**2 + 380198*B*C
             + 40096501*B + 7*C**3 + 9395*C**2 + 3522649*C + 124436109)
Pe=lambdify((B,C),Psi3_edge,'numpy')

def binding2(Bv,Cv):
    # all Q_p>=0 for primes p>=3
    for pp in P[1:200]:
        if pp**2+2*pp+4 + Bv*(pp+2)+Cv < 0:
            return False
    return True

bad=[]; mn=None; cnt=0
for Bv in np.linspace(-8,300,700):
    # find min C in binding-2 region: C >= max_p ( -(p+2)B-(p^2+2p+4) )
    Cmin_bind=max(-(pp+2)*Bv-(pp**2+2*pp+4) for pp in P[1:200])
    for Cv in np.linspace(Cmin_bind, Cmin_bind+5000, 200):
        if not binding2(Bv,Cv): continue
        cnt+=1
        v=Pe(Bv,Cv)
        if mn is None or v<mn: mn=v; mnat=(Bv,Cv,Cmin_bind)
        if v<=0: bad.append((round(Bv,3),round(Cv,3),v))
print(f"Tested {cnt} (B,C) strictly in binding-2 region (B in[-8,300]).")
print("min Psi3_edge on binding-2 region:", mn, "at (B,C,Cmin_bind)=", mnat)
print("Psi3_edge<=0 occurrences:", len(bad), " sample:", bad[:8])
print("=> if 0, then M234<0 on ALL binding-2 region (the deg-3 analog of deg-2 region B).")
