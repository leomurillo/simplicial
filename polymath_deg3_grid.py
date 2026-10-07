"""
Degree 3 GRID: search valid monic cubics for ANY counterexample (no negative principal minor),
and record max N* (first negative leading minor) and which minor closes. Use slogdet (float).
Validity: f(p)=p^3+Bp^2+Cp+E>0 for all primes p (check enough primes).
Sample (B,C,E) widely, including large additive E, negative B, etc.
"""
from sympy import primerange
import numpy as np, itertools

P=list(primerange(2,3000))

def valid(Bv,Cv,Ev,nchk=150):
    for i in range(nchk):
        pp=P[i]
        if pp**3+Bv*pp**2+Cv*pp+Ev<=0: return False
    return True

def first_neg_leading(Bv,Cv,Ev,Nmax=9):
    L=2*Nmax+2
    b=[1.0];a=1.0
    for i in range(1,L):
        pp=P[i-1]; a*=(pp**3+Bv*pp**2+Cv*pp+Ev)
        if not np.isfinite(a) or abs(a)>1e290: return ('OF',None)
        b.append(a)
    for N in range(1,Nmax+1):
        M=np.array([[b[i+j] for j in range(N+1)] for i in range(N+1)],float)
        sgn,_=np.linalg.slogdet(M)
        if sgn<0: return (N,None)
    return (None,None)

# To sample VALID cubics, parametrize by requiring f(p)>0. Easiest: pick B,C, set E large enough.
# We'll sample B in wide range, C in wide range, and E from just above the validity threshold up.
def Emin(Bv,Cv):
    return max(-(P[i]**3+Bv*P[i]**2+Cv*P[i]) for i in range(150))

rng=np.random.default_rng(0)
hist={}; nofail=[]; maxN=0; whereMax=None; total=0
# structured sweep
for Bv in np.linspace(-30,30,40):
    for Cv in np.linspace(-200,200,40):
        em=Emin(Bv,Cv)
        for dE in [0.01,0.1,0.5,1,3,10,30,100,300,1000,1e4,1e5]:
            Ev=em+dE
            r=first_neg_leading(Bv,Cv,Ev,9)
            if r[0]=='OF': continue
            total+=1
            if r[0] is None:
                if valid(Bv,Cv,Ev):
                    nofail.append((round(Bv,2),round(Cv,2),round(Ev,3)))
            else:
                hist[r[0]]=hist.get(r[0],0)+1
                if r[0]>maxN: maxN=r[0]; whereMax=(round(Bv,2),round(Cv,2),round(Ev,3))
# random sweep too
for _ in range(20000):
    Bv=rng.uniform(-50,50); Cv=rng.uniform(-500,500)
    em=Emin(Bv,Cv); Ev=em+10**rng.uniform(-2,6)
    r=first_neg_leading(Bv,Cv,Ev,9)
    if r[0]=='OF': continue
    total+=1
    if r[0] is None:
        if valid(Bv,Cv,Ev): nofail.append((round(Bv,2),round(Cv,2),round(Ev,3)))
    else:
        hist[r[0]]=hist.get(r[0],0)+1
        if r[0]>maxN: maxN=r[0]; whereMax=(round(Bv,2),round(Cv,2),round(Ev,3))

print(f"Degree-3 grid: {total} valid cubics tested.")
print("Histogram of first-negative leading-minor N*:", dict(sorted(hist.items())))
print("Max N*:", maxN, "at (B,C,E)=", whereMax)
print("Candidate counterexamples (no neg leading minor up to N=9):", len(nofail))
print("  sample:", nofail[:20])
