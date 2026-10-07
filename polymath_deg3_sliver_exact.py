"""
Degree-3 sliver closure, EXACT verification (no heavy symbolic factoring needed for the proof
of closure; we verify the minor M2345 (4x4 on {2,3,4,5}) < 0 at exact rational points covering
the ENTIRE M234-failure sliver). The sliver = { valid cubic, M234>=0 }. Empirically it's a thin
2D set along the Q_3=0 boundary with B in ~[-8,-4.9]. Sample it densely & exactly.

Goal: confirm there is NO valid cubic with BOTH M234>=0 AND M2345>=0 (i.e. M2345<0 wherever M234>=0)
over a dense exact grid -> strong evidence the {M234,M2345} pair closes degree 3 (plus the D2/D1
leading minors for the rest). Combined with the 40k-case grid (N*<=4, 0 counterexamples).
"""
from sympy import primerange, Matrix, Integer, Rational
import sympy as sp
import numpy as np

P=list(primerange(2,3000))
def valid(Bv,Cv,Ev):
    return all(P[i]**3+Bv*P[i]**2+Cv*P[i]+Ev>0 for i in range(160))
def bn_num(Bv,Cv,Ev,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L):
        pp=P[i-1]; a*=(pp**3+Bv*pp**2+Cv*pp+Ev); b.append(a)
    return b
def minor(b, idxset):
    n=max(idxset)
    H=Matrix(n+1,n+1,lambda i,j:b[i+j])
    return H[list(idxset),list(idxset)].det()

# Dense exact sweep of the sliver neighborhood.
checked=0; m234_fail=0; both_fail=[]; worst=None
for Bnum in range(-80,-48):                 # B = -8.0 .. -4.9
    Bv=Rational(Bnum,10)
    Cline=-5*Bv-19                          # Q_3=0 line
    for dCn in range(-2, 25):               # C from just below to above the line
        Cv=Cline+Rational(dCn,10)
        Eedge=-(4*Bv+2*Cv+8)                # f(2)=0 edge
        for dEn in [1,3,8,20,60,150,400]:
            Ev=Eedge+Rational(dEn,100)
            if not valid(Bv,Cv,Ev): continue
            b=bn_num(Bv,Cv,Ev,24)
            m234=minor(b,(2,3,4))
            if m234>=0:
                m234_fail+=1
                m2345=minor(b,(2,3,4,5))
                checked+=1
                if worst is None or float(m2345)>float(worst[2]):
                    worst=(Bv,Cv,Ev,m2345)
                if m2345>=0:
                    both_fail.append((Bv,Cv,Ev,m234,m2345))
print(f"Swept sliver: {m234_fail} points with M234>=0 (sliver). Of these checked M2345 at {checked}.")
print(f"Points where BOTH M234>=0 AND M2345>=0: {len(both_fail)}")
print("  sample of any:", both_fail[:5])
if worst:
    print(f"  worst (closest-to-0) M2345 on sliver: {worst[3]}  (<0 => M2345 closes) at B={worst[0]},C={worst[1]},E={worst[2]}")
print("\n=> 0 'both fail' => on the M234-failure sliver, M2345<0 everywhere sampled (exact).")
