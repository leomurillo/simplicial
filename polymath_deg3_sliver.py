"""
Degree-3 sliver (where M234 fails, i.e. Psi3_edge<=0 region near Q_3=0 boundary):
find which principal minor is negative there. Test exact points on the sliver.
The sliver: binding-2 region boundary, C just above Cmin_bind, where Psi3_edge<=0.
Take points with f(2) small (E just above -(4B+2C+8)) and C near the Q_3=0 line.
"""
from sympy import primerange, Matrix, Integer, Rational
import sympy as sp
import numpy as np, itertools

P=list(primerange(2,3000))
def valid(Bv,Cv,Ev):
    return all(P[i]**3+Bv*P[i]**2+Cv*P[i]+Ev>0 for i in range(150))
def bn_num(Bv,Cv,Ev,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L):
        pp=P[i-1]; a*=(pp**3+Bv*pp**2+Cv*pp+Ev); b.append(a)
    return b

# Build sliver points: pick B in [-8,-3], C just above the Q_3=0 line (C = -5B-19 + small),
# and E just above f(2)=0 (E=-(4B+2C+8)+eps). Confirm M234>=0 (D_3 fails) and find neg minor.
Nmax=5
idx=list(range(Nmax+1))
subsets=[list(s) for r in range(2,Nmax+2) for s in itertools.combinations(idx,r)]
always_neg={tuple(s):True for s in subsets}
pts=[]
for Bnum in range(-79,-29,5):       # B=-7.9..-3.4
    Bv=Rational(Bnum,10)
    Cline=-5*Bv-19
    for dC in [Rational(1,10),Rational(5,10),Rational(15,10)]:
        Cv=Cline+dC
        Eedge=-(4*Bv+2*Cv+8)
        for dE in [Rational(1,10),Rational(1,2),Rational(2,1)]:
            Ev=Eedge+dE
            if not valid(Bv,Cv,Ev): continue
            # check M234 sign (3x3 on {2,3,4})
            b=bn_num(Bv,Cv,Ev,2*Nmax+2)
            H=Matrix(Nmax+1,Nmax+1,lambda i,j:b[i+j])
            m234=H[[2,3,4],[2,3,4]].det()
            if m234<0:   # M234 already closes; not a sliver point
                continue
            pts.append((Bv,Cv,Ev))
            for s in subsets:
                if H[s,s].det()>=0: always_neg[tuple(s)]=False
print(f"Collected {len(pts)} sliver points (M234>=0, i.e. M234 fails).")
univ=[s for s,v in always_neg.items() if v]
print("Principal-minor index sets negative at EVERY sliver point:")
for s in sorted(univ,key=lambda x:(len(x),x)): print("   ",s)
if not pts:
    print("No sliver points found in this sample (M234 may close more than expected here).")
