"""
(A) Confirm d^2-cancellation: for monic deg-d f, a=u-1 ~ d*g1/q1, etc., so
    ae - b^2 ~ d^2[g1 g3/(q1 q3) - g2^2/q2^2]. The SIGN is degree-independent to leading order.
    Verify: sign(ae-b^2) for f=x^d matches the pure gap G across many r and d.
(B) Margin: R = (ae - b^2) + abe(2+b).  Need R<0.  Since abe(2+b)>0, need
    b^2 - ae > abe(2+b).  Check magnitudes: with a,b,e=O(log q / q),
    quadratic ~ (log q/q)^2, cubic ~ (log q/q)^3 -> ratio cubic/quad = O(log q/q) -> 0.
    So once b^2 - ae > 0 with the RIGHT order, R<0 for large enough primes.
    Quantify: for windows where G>0 (gap spike), compute R and check R<0 for q not too small.
"""
from sympy import primerange, Integer, Rational

P = list(primerange(2, 5_000_000))

def poly_xd(d):
    def f(x): return x**d
    return f

def ratios(f,r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    return (u-1,v-1,s-1,(q1,q2,q3,q4))

def gapG(r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    g1=q2-q1;g2=q3-q2;g3=q4-q3
    return g2*g2*q1*q3 - g1*g3*q2*q2  # >0 means middle gap spike (predict ae-b^2<0)

# (A) degree independence of sign(ae-b^2) vs G
print("=== (A) sign(ae - b^2) vs gap G, for d=1,2,3,5, r=0..200 ===")
for d in (1,2,3,5):
    f=poly_xd(d)
    mismatch=0; checked=0
    for r in range(0,200):
        a,b,e,qs=ratios(f,r)
        lead = a*e-b**2
        G=gapG(r)
        checked+=1
        if (lead<0) != (G>0):
            mismatch+=1
    print(f"  d={d}: sign(ae-b^2)!=sign(G) in {mismatch}/{checked} windows")

# (B) For f=x: among windows with G>0, how often is the EXACT R<0, by prime size bucket
print("\n=== (B) f=x: of windows with gap spike G>0, fraction with exact R<0, vs q2 size ===")
f=poly_xd(1)
buckets={}
firstRneg=None
for r in range(0,5000):
    a,b,e,qs=ratios(f,r)
    G=gapG(r)
    Rfull=a*e-b**2+2*a*b*e+a*b**2*e
    if Rfull<0 and firstRneg is None: firstRneg=r
    if G>0:
        q2=qs[1]
        key = len(str(q2))  # digit bucket ~ size
        d=buckets.setdefault(key,[0,0])
        d[1]+=1
        if Rfull<0: d[0]+=1
print(" digits(q2): R<0count / G>0count")
for k in sorted(buckets):
    z=buckets[k]; print(f"   {k}: {z[0]}/{z[1]}")
print("first r with exact R<0 for f=x:", firstRneg)

# (B') The crux: is there a window where G>0 with margin big enough that R<0, for SMALL r?
print("\n=== (B') smallest r with exact R<0 for f=x^d, d=1..6 ===")
for d in range(1,7):
    f=poly_xd(d)
    fr=None
    for r in range(0,2000):
        a,b,e,qs=ratios(f,r)
        Rfull=a*e-b**2+2*a*b*e+a*b**2*e
        if Rfull<0: fr=r; break
    print(f"   d={d}: first r with R<0 = {fr}  (window {ratios(f,fr)[3] if fr is not None else None})")
