"""
Confirm (exact arithmetic) that D_4 < 0 everywhere on the Phi<=0 sliver.
Sliver: B in (-5, ~7), C in (Cmin(B)=-2B-4 , Cupper(B)] where Cupper is the root of Phi(B,.)=0
(the upper edge of Phi<=0). Sample many rational (B,C) strictly inside the sliver & valid,
compute exact D_2, D_3, D_4, confirm D_4<0 (and that indeed D_2>=0,D_3>=0 there as expected,
showing D_4 is the one doing the work).
"""
from sympy import primerange, Matrix, Integer, Rational, lambdify, symbols
import sympy as sp
import numpy as np

P=list(primerange(2,3000))
B,C=symbols('B C')
Phi = (547*B**6 + 297*B**5*C + 32888*B**5 + 21*B**4*C**2 + 17727*B**4*C + 749230*B**4
       - B**3*C**3 + 1302*B**3*C**2 + 385779*B**3*C + 8211596*B**3 - 29*B**2*C**3
       + 24885*B**2*C**2 + 3860625*B**2*C + 45675199*B**2 - 340*B*C**3 + 177108*B*C**2
       + 18423204*B*C + 118856828*B - 2256*C**3 + 445968*C**2 + 34380432*C + 99623856)
Phif=lambdify((B,C),Phi,'numpy')

def bn_num(Bv,Cv,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L):
        a*=(P[i-1]**2+Bv*P[i-1]+Cv); b.append(a)
    return b
def Dn(Bv,Cv,N):
    b=bn_num(Bv,Cv,2*N+2)
    return Matrix(N+1,N+1,lambda i,j:b[i+j]).det()
def valid(Bv,Cv):
    return all(P[i]**2+Bv*P[i]+Cv>0 for i in range(80))

worst_d4=None; bad=[]; checked=0; d3pos=0; d2pos=0
# sweep B rationally in (-5,7), for each find Phi<=0 C-window numerically then pick exact rationals inside
for Bnum in range(-49, 71):    # B = Bnum/10
    Bv=Rational(Bnum,10)
    Bvf=float(Bv)
    Clo=-2*Bvf-4
    Cs=np.linspace(Clo, Clo+3, 6000)
    ph=Phif(Bvf,Cs)
    mask=ph<=0
    if not mask.any(): continue
    Cw=Cs[mask]
    lo,hi=Cw.min(),Cw.max()
    if hi<=Clo+1e-9: continue
    # pick a few exact rationals strictly inside (Clo, hi) and valid
    for frac in [0.2,0.5,0.8]:
        Cval=Clo + frac*(hi-Clo)
        Cv=Rational(round(Cval*100),100)
        if not valid(Bv,Cv): continue
        # confirm Phi<=0 exactly
        ph_exact=Phi.subs({B:Bv,C:Cv})
        if ph_exact>0:   # outside sliver after rounding
            continue
        checked+=1
        d2=Dn(Bv,Cv,2); d3=Dn(Bv,Cv,3); d4=Dn(Bv,Cv,4)
        if d2>=0: d2pos+=1
        if d3>=0: d3pos+=1
        if d4>=0:
            bad.append((Bv,Cv,d4))
        if worst_d4 is None or float(d4)>float(worst_d4[2]):  # closest to 0 from below
            worst_d4=(Bv,Cv,d4)

print(f"Checked {checked} exact rational points strictly inside the Phi<=0 sliver (valid).")
print(f"  of these, D_2>=0 count={d2pos}, D_3>=0 count={d3pos} (expected ~all: D2,D3 don't close here)")
print(f"  D_4>=0 occurrences (would be a problem): {len(bad)}  sample:{bad[:5]}")
print(f"  worst (largest, closest-to-0) D_4: {worst_d4[2]} at B={worst_d4[0]}, C={worst_d4[1]}")
print("  => if D_4>=0 count is 0, D_4<0 closes the entire D_3-failure sliver.")
