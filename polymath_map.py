"""
Map first-negative leading minor N* over the FULL valid region for monic quadratic.
We expect N* in {2,3,4,5,...}. Find the MAX N* needed (the grid hint said N* in {2,3,4,5}).
Scan (B,C) with B in wide range, C from just above Cmin(B) upward, mark N*.
Use float for speed; spot-verify with exact at boundaries.
"""
from sympy import primerange
import numpy as np

P = list(primerange(2, 5000))
Pf = np.array(P, dtype=float)

def first_neg_leading(Bv,Cv,Nmax=8):
    # build b_n in float (log to avoid overflow? values get huge; use python big ints via floats ok up to ~1e308)
    # Use logs for ratio, but determinants need actual values. Use float128? Just use Fraction-free with floats and watch overflow.
    L=2*Nmax+2
    b=[1.0]; a=1.0; overflow=False
    for i in range(1,L):
        a*= (P[i-1]**2 + Bv*P[i-1] + Cv)
        b.append(a)
        if abs(a)>1e290: overflow=True; break
    if overflow:
        return ('OF',None)
    import numpy as np
    for N in range(1,Nmax+1):
        M=np.array([[b[i+j] for j in range(N+1)] for i in range(N+1)],dtype=float)
        # scale rows to avoid det overflow: det sign via slogdet
        sign,logdet=np.linalg.slogdet(M)
        if sign<0:
            return (N, None)
    return (None,None)

def Cmin(Bv):
    # max over primes of -(p^2+Bp)
    return max(-(q*q+Bv*q) for q in P[:200])

Bs = np.linspace(-4.9, 60, 140)
maxNstar=0; whereMax=None
nofail=[]  # points with no negative minor up to Nmax (potential counterexamples!)
hist={}
for Bv in Bs:
    cmn=Cmin(Bv)
    Cs=np.linspace(cmn+0.05, cmn+200, 90)
    for Cv in Cs:
        ns,_=first_neg_leading(Bv,Cv,8)
        if ns=='OF':
            continue
        if ns is None:
            nofail.append((round(Bv,3),round(Cv,3)))
        else:
            hist[ns]=hist.get(ns,0)+1
            if ns>maxNstar:
                maxNstar=ns; whereMax=(round(Bv,3),round(Cv,3))

print("Histogram of first-negative leading-minor index N* over valid B in [-4.9,60]:")
for k in sorted(hist): print(f"   N*={k}: {hist[k]} points")
print("Max N* seen:", maxNstar, "at", whereMax)
print("Points with NO negative leading minor up to N=8 (candidate counterexamples):", len(nofail))
print("   sample:", nofail[:20])
