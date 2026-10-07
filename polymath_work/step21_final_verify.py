import sys
from sympy import primerange, Integer, Rational
import bisect, math

P = list(primerange(2, 30_000_000))
def pr(*a): print(*a); sys.stdout.flush()

pr("primes loaded:", len(P), "max", P[-1])

# ---- exact R for f via rationals ----
def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f
def Rgen(f,q1,q2,q3,q4):
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e
def Rxd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

# dmax via float sign (fast); cap modest
def dmax_float(q1,q2,q3,q4, cap=200000):
    r1=q2/q1; r2=q3/q2; r3=q4/q3
    L1=math.log(r1); L2=math.log(r2); L3=math.log(r3)
    def Rf(d):
        # use log to avoid overflow: a=exp(d L1)-1 etc. but for moderate d fine
        a=math.expm1(d*L1); b=math.expm1(d*L2); e=math.expm1(d*L3)
        return a*e-b*b+a*b*e*(2+b)
    if Rf(1)>=0: return 0
    lo=1;hi=2
    while hi<cap and Rf(hi)<0: lo=hi;hi*=2
    if Rf(min(hi,cap))<0: return min(hi,cap)
    while hi-lo>1:
        mid=(lo+hi)//2
        if Rf(mid)<0: lo=mid
        else: hi=mid
    return lo

def maxgap_window(X):
    i0=bisect.bisect_left(P,X); i1=bisect.bisect_right(P,2*X)
    best=-1; bi=None
    for i in range(i0,min(i1,len(P)-2)):
        g=P[i+1]-P[i]
        if g>best: best=g; bi=i
    return P[bi-1],P[bi],P[bi+1],P[bi+2], best

pr("\n=== (A) MAXIMAL-GAP window in [X,2X]: spike property + dmax growth ===")
pr(f"{'X':>9} {'window gaps(g1,g2,g3)':>22} {'g2^2/(g1g3)':>12} {'dmax':>8}")
X=128
while X<10_000_000:
    q1,q2,q3,q4,mg=maxgap_window(X)
    g1=q2-q1;g2=q3-q2;g3=q4-q3
    ratio=(g2*g2)/(g1*g3)
    dm=dmax_float(q1,q2,q3,q4)
    pr(f"{X:>9} {str((g1,g2,g3)):>22} {ratio:>12.2f} {dm:>8}")
    X*=2

pr("\n=== (B) GENERAL monic f: maximal-gap window gives R<0 at large enough X ===")
fams = {
 "x^3":[1,0,0,0],
 "x^3-2x^2":[1,-2,0,0],
 "x^5-3x^4":[1,-3,0,0,0,0],
 "x^8-5x^7":[1,-5]+[0]*7,
 "x^4-3x^3+2":[1,-3,0,0,2],
 "x^6-6x^5+1":[1,-6,0,0,0,0,1],
 "x^2+10^6":[1,0,10**6],
 "x^3+10^9":[1,0,0,10**9],
 "x^10":[1]+[0]*10,
}
for name,co in fams.items():
    co=[Integer(c) for c in co]
    f=poly(co)
    if not all(f(P[i])>0 for i in range(500)):
        pr(f"  {name}: not positive on small primes, skip"); continue
    found=None
    X=64
    while X<10_000_000:
        q1,q2,q3,q4,mg=maxgap_window(X)
        if f(q1)>0 and f(q1)<f(q2)<f(q3)<f(q4):
            if Rgen(f,q1,q2,q3,q4)<0:
                found=(X,(q1,q2,q3,q4)); break
        X*=2
    pr(f"  {name:14s}: first maxgap-window with R<0 at X={found[0] if found else 'NONE'}, window={found[1] if found else None}")

pr("\n=== (C) EXACT sanity: leading consecutive 3x3 minor negative, exact ints ===")
from sympy import Matrix
def bn(f,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(P[i-1]); b.append(a)
    return b
def minor(f,S):
    b=bn(f,2*max(S)+2); n=len(S)
    return Matrix(n,n,lambda i,j:b[S[i]+S[j]]).det()
# For f=x, the window (5,7,11,13) is r=1 -> minor on {1,2,3}
for name,co,S in [("f=x",[1,0],(1,2,3)),("f=x^2",[1,0,0],(2,3,4)),("f=x^3+10^9",[1,0,0,10**9],None)]:
    f=poly([Integer(c) for c in co])
    if S is None:
        # find first r with exact R<0
        r=None
        for rr in range(0,200):
            q1,q2,q3,q4=P[2*rr],P[2*rr+1],P[2*rr+2],P[2*rr+3]
            if Rgen(f,q1,q2,q3,q4)<0: r=rr;break
        S=(r,r+1,r+2)
    pr(f"  {name}: minor on {S} = {minor(f,S)}  (negative => non-moment certificate)")
