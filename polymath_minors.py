"""
On the Phi<=0 sliver (where leading D_3 fails), look for a NON-leading principal minor that is
negative and might factor more cleanly than D_4. Candidates: 3x3 principal minors on index sets
like {0,1,3},{0,2,3},{1,2,3},{0,1,4}, etc. Also 2x2 minors {i,j}: det = b_{2i}b_{2j}-b_{i+j}^2.
A 2x2 principal minor on rows {i,j}: b_{2i} b_{2j} - b_{i+j}^2.  For Hankel PSD need all >=0.
Note 2x2 {0,j}: b_0 b_{2j} - b_j^2 = b_{2j} - b_j^2. With b's products, maybe a clean one fails.

Test at exact sliver points which principal minors (all sizes) are negative; tally which index
sets are 'universally negative' across the sliver.
"""
from sympy import primerange, Matrix, Integer, Rational, lambdify, symbols
import sympy as sp
import numpy as np, itertools

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
def valid(Bv,Cv):
    return all(P[i]**2+Bv*P[i]+Cv>0 for i in range(80))

# gather sliver points
pts=[]
for Bnum in range(-49,71):
    Bv=Rational(Bnum,10); Bvf=float(Bv); Clo=-2*Bvf-4
    Cs=np.linspace(Clo,Clo+3,4000); ph=Phif(Bvf,Cs); mask=ph<=0
    if not mask.any(): continue
    Cw=Cs[mask]; hi=Cw.max()
    if hi<=Clo+1e-9: continue
    for frac in [0.3,0.6]:
        Cval=Clo+frac*(hi-Clo); Cv=Rational(round(Cval*100),100)
        if valid(Bv,Cv) and Phi.subs({B:Bv,C:Cv})<=0:
            pts.append((Bv,Cv))

print(f"{len(pts)} sliver points.")
Nmax=4
idx=list(range(Nmax+1))
subsets=[]
for r in range(2,Nmax+2):
    subsets += [list(s) for s in itertools.combinations(idx,r)]

# For each subset, is its principal minor <0 at ALL sliver points?
always_neg={tuple(s):True for s in subsets}
for (Bv,Cv) in pts:
    b=bn_num(Bv,Cv,2*Nmax+2)
    H=Matrix(Nmax+1,Nmax+1,lambda i,j:b[i+j])
    for s in subsets:
        d=H[s,s].det()
        if d>=0:
            always_neg[tuple(s)]=False
univ=[s for s,v in always_neg.items() if v]
print("Principal-minor index sets that are NEGATIVE at EVERY sliver point:")
for s in sorted(univ,key=lambda x:(len(x),x)):
    print("   ",s)
print("(smallest such sets are the cleanest candidates to prove symbolically)")
