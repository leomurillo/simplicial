"""
Characterize the set S3 = { (B,C) valid, B>-5, Phi(B,C) <= 0 } where D_3 FAILS to be negative
(D_3 = -4 Phi, so D_3 <= 0 <=> Phi>=0; we need D_3<0 i.e. Phi>0; the PROBLEM sliver is Phi<=0).
On this sliver we must show D_4 < 0.

Phi is cubic in C with NEGATIVE leading coeff in C? Check coeff of C^3:
  -B^3 -29 B^2 -340 B -2256  (from the expansion). For B>-5 sign?
Understand Phi(B, .) as cubic in C: where is Phi<=0?
"""
from sympy import symbols, factor, expand, Poly, solve, S, Rational, primerange, lambdify
import sympy as sp
import numpy as np

B,C=symbols('B C', real=True)
Phi = (547*B**6 + 297*B**5*C + 32888*B**5 + 21*B**4*C**2 + 17727*B**4*C + 749230*B**4
       - B**3*C**3 + 1302*B**3*C**2 + 385779*B**3*C + 8211596*B**3 - 29*B**2*C**3
       + 24885*B**2*C**2 + 3860625*B**2*C + 45675199*B**2 - 340*B*C**3 + 177108*B*C**2
       + 18423204*B*C + 118856828*B - 2256*C**3 + 445968*C**2 + 34380432*C + 99623856)

pC = Poly(Phi, C)
print("Phi as poly in C, coeffs (high->low):")
for d,co in zip(range(pC.degree(),-1,-1), pC.all_coeffs()):
    print(f"  C^{d}: {factor(co)}")

c3 = pC.all_coeffs()[0]
print("\nLeading C^3 coeff:", factor(c3))
print("  roots in B:", [sp.nsimplify(r) for r in solve(sp.Eq(c3,0),B) if r.is_real])
# sign of c3 for B>-5:
print("  c3 at B=0:", c3.subs(B,0), " at B=5:", c3.subs(B,5), " at B=-4:", c3.subs(B,-4))

# Numerically: for each B>-5, find the C-range where Phi<=0 AND valid (C>-2B-4), AND D_2>=0 (C<=Cstar).
Phif=lambdify((B,C),Phi,'numpy')
Cstar=lambdify(B,(B**3+38*B**2+341*B+988)/(B**2+15*B+68),'numpy')
print("\nFor sample B, the C-interval where Phi<=0 within (Cmin, Cstar]:")
for Bv in [-4.9,-4,-3,-2,-1,0,1,2,3,4,4.77,5,6,8,10,20,50,100]:
    Clo=-2*Bv-4
    cs=Cstar(Bv)
    if cs<=Clo:
        print(f"  B={Bv}: band empty (Cstar<=Cmin)"); continue
    Cs=np.linspace(Clo,cs,4000)
    ph=Phif(Bv,Cs)
    mask=ph<=0
    if mask.any():
        Csel=Cs[mask]
        print(f"  B={Bv}: Phi<=0 on C in [{Csel.min():.4f}, {Csel.max():.4f}]  (band (Cmin={Clo:.3f},Cstar={cs:.3f}])  width={Csel.max()-Csel.min():.4f}")
    else:
        print(f"  B={Bv}: Phi>0 on ALL of band (D_3 closes here)")
