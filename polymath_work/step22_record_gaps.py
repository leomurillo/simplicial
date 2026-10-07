import sys
from sympy import primerange, Integer, Rational
import math
def pr(*a): print(*a); sys.stdout.flush()

P = list(primerange(2, 30_000_000))
pr("primes:", len(P))

def Rgen(f,q1,q2,q3,q4):
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e
def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f
def dmax_float(q1,q2,q3,q4, cap=500000):
    L1=math.log(q2/q1);L2=math.log(q3/q2);L3=math.log(q4/q3)
    def Rf(d):
        a=math.expm1(d*L1);b=math.expm1(d*L2);e=math.expm1(d*L3)
        return a*e-b*b+a*b*e*(2+b)
    if Rf(1)>=0: return 0
    lo,hi=1,2
    while hi<cap and Rf(hi)<0: lo=hi;hi*=2
    if Rf(min(hi,cap))<0: return min(hi,cap)
    while hi-lo>1:
        m=(lo+hi)//2
        if Rf(m)<0: lo=m
        else: hi=m
    return lo

# ---- RECORD gaps: g_n strictly greater than all previous gaps. Record neighbor ratio. ----
pr("\n=== RECORD MAXIMAL GAPS: g_m > all previous gaps. Neighbors g_{m-1},g_{m+1}, ratio, dmax ===")
pr(f"{'prime q2':>12} {'(g1,g2,g3)':>16} {'g2/max(g1,g3)':>13} {'g2^2/(g1g3)':>12} {'dmax':>8}")
record=0
rows=0
for i in range(2, len(P)-2):
    g=P[i]-P[i-1]   # gap ending at P[i]; treat as middle gap g2 with q2=P[i-1],q3=P[i]
    if g>record:
        record=g
        q1,q2,q3,q4=P[i-2],P[i-1],P[i],P[i+1]
        g1=q2-q1;g2=q3-q2;g3=q4-q3
        ratio_geom=(g2*g2)/(g1*g3)
        ratio_min=g2/max(g1,g3)
        dm=dmax_float(q1,q2,q3,q4)
        if rows<40:
            pr(f"{q2:>12} {str((g1,g2,g3)):>16} {ratio_min:>13.2f} {ratio_geom:>12.2f} {dm:>8}")
        rows+=1
pr(f"total record gaps found: {rows}")

# ---- SLOW-GROWER valid monic polys (negative coeffs but f>0 on ALL primes) ----
pr("\n=== Slow growers valid on all primes: first maxgap-window with R<0 ===")
import bisect
def maxgap_window(X):
    i0=bisect.bisect_left(P,X); i1=bisect.bisect_right(P,2*X)
    best=-1;bi=None
    for i in range(i0,min(i1,len(P)-2)):
        gg=P[i+1]-P[i]
        if gg>best: best=gg;bi=i
    return P[bi-1],P[bi],P[bi+1],P[bi+2]
fams={
 "x^2-x+1":[1,-1,1],          # f(2)=3>0, slow
 "x^3-2x^2+2":[1,-2,0,2],     # f(2)=2>0
 "x^3-3x^2+3":[1,-3,0,3],     # f(2)=-1<0? check
 "x^4-2x^3+2":[1,-2,0,0,2],
 "x^5-x^4-x+3":[1,-1,0,0,-1,3],
 "x^2-2x+2":[1,-2,2],         # f(2)=2,f(3)=5 slow start
 "x^3-x^2-x+3":[1,-1,-1,3],
}
for name,co in fams.items():
    f=poly([Integer(c) for c in co])
    pos=all(f(P[i])>0 for i in range(2000))
    if not pos:
        pr(f"  {name}: NOT positive on all primes (invalid), skip"); continue
    found=None; X=64
    while X<10_000_000:
        q1,q2,q3,q4=maxgap_window(X)
        if f(q1)>0 and f(q1)<f(q2)<f(q3)<f(q4) and Rgen(f,q1,q2,q3,q4)<0:
            found=(X,(q1,q2,q3,q4)); break
        X*=2
    pr(f"  {name:16s}: R<0 first at X={found[0] if found else 'NONE'}, window={found[1] if found else None}")
