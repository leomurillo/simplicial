"""
Adversarial sweep: confirm the theorem (some negative principal minor) for a broad family,
using BOTH the leading Hankel determinants D_N (first-failure N*) AND, independently, the
record-gap principal-minor witness. Cross-check they agree that b_n is non-moment.
Includes the strategy's noted hard cases: large additive constant, high degree, deg 1-6.
"""
import sys; sys.set_int_max_str_digits(5000000)
from sympy import primerange, Integer, Matrix
P=list(primerange(2,200000))

def bn(f,L):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1,L): a*=f(P[i-1]); b.append(a)
    return b
def D(f,N):
    b=bn(f,2*N+2); return Matrix(N+1,N+1,lambda i,j:b[i+j]).det()
def firstfail_leading(f,Nmax=12):
    for N in range(1,Nmax+1):
        if D(f,N)<0: return N
    return None

G=[P[k+1]-P[k] for k in range(len(P)-1)]
def record_witness(f):
    """return (window primes, det of 3x3 principal minor<0) using first large-enough record gap."""
    cur=0
    for i in range(1,len(G)-1):
        if G[i]>cur:
            cur=G[i]
            if P[i]>2000:
                a,b,e=G[i-1],G[i],G[i+1]
                if b*b>a*e:
                    bb=bn(f,2*(i+2)+3)
                    Mm=Matrix(3,3,lambda r,c: bb[[i,i+1,i+2][r]+[i,i+1,i+2][c]])
                    det=Mm.det()
                    if det<0:
                        return (P[i-1],P[i],P[i+1],P[i+2]),N if False else det
    return None,None

cases=[]
for d in [1,2,3,4,5,6]:
    cases.append((f"p^{d}", lambda p,d=d: p**d))
for C in [1,5,100,10000,10**6]:
    cases.append((f"p+{C}", lambda p,C=C: p+C))
    cases.append((f"p^2+{C}", lambda p,C=C: p**2+C))
    cases.append((f"p^3+{C}", lambda p,C=C: p**3+C))
cases.append(("p^4+10^6 p", lambda p: p**4+10**6*p))
cases.append(("p^2-p+1", lambda p: p**2-p+1))
cases.append(("p^5-1000p^4+1", lambda p: p**5-1000*p**4+1))

print(f"{'f':18s} {'N*(leading D_N<0)':18s} {'record-minor<0?':16s}")
allgood=True
for name,f in cases:
    Ns=firstfail_leading(f)
    win,det=record_witness(f)
    rec_ok = det is not None and det<0
    print(f"{name:18s} {str(Ns):18s} {('YES @'+str(win)) if rec_ok else 'NO':16s}")
    if Ns is None and not rec_ok:
        allgood=False
        print("   !!! NO failure found -- potential counterexample, investigate", name)
print("\nEvery case fails (non-moment) by SOME principal minor:", allgood)
