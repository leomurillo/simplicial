import sys
from sympy import primerange, Integer, Rational
import bisect, math
def pr(*a): print(*a); sys.stdout.flush()
P=list(primerange(2,30_000_000))

def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f
def Rf(f,q1,q2,q3,q4):
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e
def maxgap_window(X):
    i0=bisect.bisect_left(P,X); i1=bisect.bisect_right(P,2*X)
    best=-1;bi=None
    for i in range(i0,min(i1,len(P)-2)):
        g=P[i+1]-P[i]
        if g>best:best=g;bi=i
    return P[bi-1],P[bi],P[bi+1],P[bi+2]

# Claim: at maxgap window with primes >> |coeffs|, R(f) and R(x^deg) have the SAME sign (<0).
# Test f = x^d + c x^{d-1} for LARGE c, and compare to x^d, across growing X.
pr("Compare sign(R(x^d + c x^{d-1})) to sign(R(x^d)) at maxgap windows, growing X.")
for (d,c) in [(2,10**6),(3,10**6),(2,-10**6+ Integer(0)),(3,10**9),(5,10**4),(4,-50)]:
    co=[Integer(1),Integer(c)]+[Integer(0)]*(d-1)
    f=poly(co); f0=poly([Integer(1)]+[Integer(0)]*d)
    # smallest X where both R<0 and they agree
    line=f"  f=x^{d}+({c})x^{d-1}: "
    agree_from=None
    for k in range(6,24):
        X=2**k
        if X>=10_000_000: break
        q1,q2,q3,q4=maxgap_window(X)
        if not (f(q1)>0 and f(q1)<f(q2)<f(q3)<f(q4)): continue
        Rfull=Rf(f,q1,q2,q3,q4); Rbase=Rf(f0,q1,q2,q3,q4)
        same=(Rfull<0)==(Rbase<0)
        if same and Rfull<0 and agree_from is None:
            agree_from=X
    pr(line+f"sign(R) agrees with x^{d} and both<0 from X={agree_from}")

# Also: explicitly show |R(f)-R(x^d)| / |R(x^d)| -> 0 as X grows (correction negligible)
pr("\nRelative correction |R(f)-R(x^d)|/|R(x^d)| at maxgap windows (f=x^3+10^6 x^2):")
f=poly([Integer(1),Integer(10**6),Integer(0),Integer(0)]); f0=poly([Integer(1),0,0,0])
for k in range(8,24):
    X=2**k
    if X>=10_000_000: break
    q1,q2,q3,q4=maxgap_window(X)
    if not (f(q1)>0 and f(q1)<f(q2)<f(q3)<f(q4)): continue
    Rfull=Rf(f,q1,q2,q3,q4); Rbase=Rf(f0,q1,q2,q3,q4)
    rel=abs(float(Rfull-Rbase))/abs(float(Rbase)) if Rbase!=0 else float('inf')
    pr(f"  X={X:>9}: Rfull<0={Rfull<0}, Rbase<0={Rbase<0}, rel.corr={rel:.3e}")
