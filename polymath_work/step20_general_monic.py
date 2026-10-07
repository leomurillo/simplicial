"""
FINAL piece: the existence argument must cover GENERAL monic f (any subleading coeffs),
not just x^d. Show: at a spike window chosen at large enough q, R<0 for general monic f.

We verify: take a fixed 'hostile' monic f (e.g. slow grower x^d - k x^{d-1} + ...), and show
that as we slide to spike windows at larger primes, R becomes negative (and stays) -- the
subleading terms wash out. Tabulate first spike-window (max gap in [X,2X]) where R<0, vs X.
"""
from sympy import primerange, Integer, Rational
import bisect

P = list(primerange(2, 50_000_000))

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

def maxgap_window(X):
    i0=bisect.bisect_left(P,X); i1=bisect.bisect_right(P,2*X)
    best=-1; bi=None
    for i in range(i0,min(i1,len(P)-2)):
        g=P[i+1]-P[i]
        if g>best: best=g; bi=i
    return P[bi-1],P[bi],P[bi+1],P[bi+2]

# hostile monic families
fams = {
 "x^3":[1,0,0,0],
 "x^3-2x^2":[1,-2,0,0],
 "x^5-3x^4":[1,-3,0,0,0,0],
 "x^8-5x^7":[1,-5,0,0,0,0,0,0,0],
 "x^4-3x^3+2":[1,-3,0,0,2],
 "x^6 - 6 x^5 + 1":[1,-6,0,0,0,0,1],
 "x^2 + 10^6":[1,0,10**6],
 "x^3 + 10^9":[1,0,0,10**9],
}
print("For each hostile monic f: smallest dyadic X whose MAXIMAL-GAP window gives R<0")
for name,co in fams.items():
    co=[Integer(c) for c in co]
    f=poly(co)
    # ensure positivity on first 500 primes
    if not all(f(P[i])>0 for i in range(500)):
        print(f"  {name}: not positive on small primes, skip"); continue
    found=None
    X=64
    while X<10_000_000:
        q1,q2,q3,q4=maxgap_window(X)
        if f(q1)>0 and f(q1)<f(q2)<f(q3)<f(q4):
            if Rgen(f,q1,q2,q3,q4)<0:
                found=(X,(q1,q2,q3,q4)); break
        X*=2
    print(f"  {name:22s}: first maxgap-window with R<0 at X={found[0] if found else None}, window={found[1] if found else None}")
