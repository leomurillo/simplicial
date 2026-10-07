"""
ROBUSTNESS: push degrees up to 12, coefficients up to +-large and +10^9, and find the
TRUE max r needed.  Characterize the r in {7,8} cluster.  Also: which window r is the
'safest' uniform single choice (test if r=2 alone works for nearly all; what fails it).
"""
from sympy import primerange, Integer
import random

P = list(primerange(2, 2_000_000))
print("num primes available:", len(P))

def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f

def Qval(f, r):
    w=f(P[2*r]); x=f(P[2*r+1]); y=f(P[2*r+2]); z=f(P[2*r+3])
    return w*x*x - 2*w*x*y + w*y*z + x*y*y - x*y*z

def first_r(coeffs, RMAX=200):
    f=poly(coeffs)
    for r in range(RMAX):
        if Qval(f,r) > 0:
            return r
    return None

def ok(coeffs, npr=300):
    f=poly(coeffs)
    return all(f(P[i])>0 for i in range(npr))

random.seed(7)
bank=[]
# wide degree-1..12 random, plus structured slow-growers x^d - k x^{d-1} + ...
for deg in range(1,13):
    for _ in range(120):
        bank.append([Integer(1)]+[Integer(random.randint(-6,12)) for _ in range(deg)])
# slow growers: large negative subleading coeff (these pushed r high before)
for deg in range(2,13):
    for a in range(-1,-8,-1):
        for d in range(0,6):
            coeffs=[Integer(1),Integer(a)]+[Integer(0)]*(deg-2)+[Integer(d)]
            # ensure deg correct length deg+1
            coeffs=[Integer(1),Integer(a)]+[Integer(0)]*(deg-2)
            coeffs[-1]=Integer(d) if deg>=2 else coeffs[-1]
            bank.append(coeffs)
# huge constants with various degrees
for deg in range(1,8):
    for K in (10**3,10**6,10**9):
        coeffs=[Integer(1)]+[Integer(0)]*(deg-1)+[Integer(K)]
        bank.append(coeffs)
# near-root-at-small: f with f(2) tiny positive (slowest possible start)
for deg in range(1,9):
    # f(x) = (x-2)*x^{deg-1} + 1  -> f(2)=1 minimal
    # build via expand
    from sympy import symbols, Poly, expand
    X=symbols('X')
    expr=expand((X-2)*X**(deg-1)+1)
    pc=Poly(expr,X).all_coeffs()
    bank.append([Integer(int(t)) for t in pc])
    expr2=expand((X-2)*(X-3)*X**(max(deg-2,0))+1)
    pc2=Poly(expr2,X).all_coeffs()
    bank.append([Integer(int(t)) for t in pc2])

tested=0; never=[]; maxr=0; hist={}; rcluster={}
for coeffs in bank:
    if not ok(coeffs): continue
    tested+=1
    r=first_r(coeffs)
    if r is None:
        never.append(coeffs)
    else:
        hist[r]=hist.get(r,0)+1
        maxr=max(maxr,r)

print(f"tested positive polys: {tested}")
print(f"max r needed: {maxr}")
print(f"NEVER (no neg consecutive 3x3 minor up to r=200): {len(never)}")
print("histogram first-working r:")
for r in sorted(hist): print(f"   r={r}: {hist[r]}")
if never:
    print("NEVER list (potential counterexamples):")
    for c in never[:40]: print("   ",c)

# Does a single fixed r work for all? check coverage of each r value
print("\nSingle-window coverage (how many of tested have Q(r)>0):")
covr={}
for coeffs in bank:
    if not ok(coeffs): continue
    f=poly(coeffs)
    for r in range(0,12):
        if Qval(f,r)>0:
            covr[r]=covr.get(r,0)+1
for r in sorted(covr): print(f"   r={r}: {covr[r]}/{tested}")
