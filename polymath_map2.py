"""
Wider scan: confirm no counterexample (every valid monic quadratic fails some leading minor),
and find max N* over a BIG region. Also test large B, large C, and near-boundary slivers finely.
Use slogdet (float) for speed; the question is existence of a NEGATIVE leading minor.
"""
from sympy import primerange
import numpy as np

P = list(primerange(2, 5000))

def first_neg_leading(Bv,Cv,Nmax=10):
    L=2*Nmax+2
    b=[1.0]; a=1.0
    for i in range(1,L):
        a*= (P[i-1]**2 + Bv*P[i-1] + Cv)
        if not np.isfinite(a) or abs(a)>1e290:
            return ('OF',None)
        b.append(a)
    for N in range(1,Nmax+1):
        M=np.array([[b[i+j] for j in range(N+1)] for i in range(N+1)],dtype=float)
        sign,logdet=np.linalg.slogdet(M)
        if sign<0:
            return (N,logdet)
    return (None,None)

def Cmin(Bv):
    return max(-(q*q+Bv*q) for q in P[:300])

maxNstar=0; whereMax=None; nofail=[]; hist={}
# region 1: B in [-4.95, 5], fine C near boundary (slivers live here)
# region 2: B in [5, 500], C up to large
import itertools
configs=[
    (np.linspace(-4.95, 5, 200), lambda c: np.linspace(c+0.02, c+50, 200)),
    (np.linspace(5, 200, 120),   lambda c: np.linspace(c+0.1, c+2000, 120)),
    (np.linspace(200, 5000, 60), lambda c: np.linspace(c+1, c+50000, 60)),
]
total=0
for Bs, Cfun in configs:
    for Bv in Bs:
        cmn=Cmin(Bv)
        for Cv in Cfun(cmn):
            r=first_neg_leading(Bv,Cv,10)
            if r[0]=='OF': continue
            total+=1
            if r[0] is None:
                nofail.append((round(Bv,4),round(Cv,4)))
            else:
                hist[r[0]]=hist.get(r[0],0)+1
                if r[0]>maxNstar: maxNstar=r[0]; whereMax=(round(Bv,4),round(Cv,4))

print(f"Scanned {total} valid points across B in [-4.95, 5000].")
print("Histogram N*:", dict(sorted(hist.items())))
print("Max N*:", maxNstar, "at", whereMax)
print("Candidate counterexamples (no neg leading minor up to N=10):", len(nofail))
print("  sample:", nofail[:30])
