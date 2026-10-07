import sys
from sympy import primerange, Integer, Rational, symbols, Poly, expand
import random
def pr(*a): print(*a); sys.stdout.flush()

P = list(primerange(2, 5_000_000))

def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f
def Rgen(f,r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e
def first_neg_minor_r(coeffs, RMAX=400):
    f=poly(coeffs)
    # need increasing & positive; primes large enough
    for r in range(RMAX):
        q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
        if f(q1)>0 and f(q1)<f(q2)<f(q3)<f(q4):
            if Rgen(f,r)<0:
                return r
    return None
def valid(coeffs, npr=300):
    f=poly(coeffs)
    return all(f(P[i])>0 for i in range(npr))

random.seed(2024)
N=0; fails=[]; maxr=0; rhist={}
X=symbols('X')

def add(coeffs):
    global N,maxr
    coeffs=[Integer(c) for c in coeffs]
    if coeffs[0]!=1: return
    if not valid(coeffs): return
    N+=1
    r=first_neg_minor_r(coeffs)
    if r is None: fails.append(coeffs)
    else:
        rhist[r]=rhist.get(r,0)+1
        if r>maxr: maxr=r

# 1) dense low-degree
for a in range(-6,8):
    for b in range(-6,15):
        add([1,a,b])
# 2) random deg 3..14
for deg in range(3,15):
    for _ in range(150):
        add([1]+[random.randint(-8,15) for _ in range(deg)])
# 3) slow growers near root at 2: (x-2)*prod + 1  (f(2)=1 minimal positive)
for deg in range(1,12):
    expr=expand((X-2)*X**(deg-1)+1)
    add([int(t) for t in Poly(expr,X).all_coeffs()])
    expr=expand((X-2)*(X-3)*X**max(deg-2,0)+7)  # f could dip; valid() filters
    add([int(t) for t in Poly(expr,X).all_coeffs()])
# 4) huge constants, various degrees
for deg in range(1,9):
    for K in (10**3,10**6,10**9,10**12):
        add([1]+[0]*(deg-1)+[K])
        add([1,-1]+[0]*(deg-2)+[K] if deg>=2 else [1,K])
# 5) negative-subleading slow growers with positive constant to stay valid
for deg in range(2,12):
    for a in range(-1,-9,-1):
        add([1,a]+[0]*(deg-2)+[max(1, -a*7)])  # constant chosen to keep positive-ish; valid() filters

pr(f"Total VALID monic non-constant polynomials tested: {N}")
pr(f"Polynomials with NO negative consecutive 3x3 minor (FAILS / COUNTEREXAMPLES): {len(fails)}")
pr(f"Max window r needed: {maxr}")
pr("Histogram of first-working r (top by count):")
for r in sorted(rhist):
    pr(f"   r={r}: {rhist[r]}")
if fails:
    pr("FAILURES:")
    for c in fails[:50]: pr("   ",c)
else:
    pr("\n*** NO COUNTEREXAMPLE FOUND. Every tested monic non-constant f has a negative")
    pr("    consecutive 3x3 principal minor of its Hankel matrix => NOT a moment sequence. ***")
