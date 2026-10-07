"""
For the consecutive 3x3 minor at base r:
   minor < 0  <=>  Q(w,x,y,z) > 0,  (w,x,y,z)=(f(p_{2r+1}),f(p_{2r+2}),f(p_{2r+3}),f(p_{2r+4}))
   Q = w*x^2 - 2*w*x*y + w*y*z + x*y^2 - x*y*z

QUESTION: For EVERY monic non-constant f (f>0 on primes), is there SOME r with Q>0
(equivalently some consecutive 3x3 minor negative)?  Test broadly; record min r that works,
and whether r=0 (leading D_2) already works.
"""
from sympy import primerange, Integer
import itertools, random

P = list(primerange(2, 200000))  # need lots for higher-degree growth and windows

def poly(coeffs):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    return f

def Qval(f, r):
    w=f(P[2*r]); x=f(P[2*r+1]); y=f(P[2*r+2]); z=f(P[2*r+3])
    return w*x*x - 2*w*x*y + w*y*z + x*y*y - x*y*z

def first_neg_consecutive_minor(coeffs, RMAX=60):
    f=poly(coeffs)
    for r in range(RMAX):
        if Qval(f,r) > 0:
            return r
    return None

# Big bank
bank=[]
for cc in range(-1,15): bank.append([Integer(1),Integer(cc)])
for a in range(-4,7):
    for bb in range(-4,15):
        bank.append([Integer(1),Integer(a),Integer(bb)])
for a in range(-3,5):
    for bb in range(-3,5):
        for d in range(-3,8):
            bank.append([Integer(1),Integer(a),Integer(bb),Integer(d)])
random.seed(1)
for deg in (4,5,6,7,8):
    for _ in range(60):
        bank.append([Integer(1)]+[Integer(random.randint(-5,9)) for _ in range(deg)])
for K in (50,100,1000,10**4,10**6,10**9):
    bank.append([Integer(1),Integer(K)])
    bank.append([Integer(1),Integer(0),Integer(K)])
    bank.append([Integer(1),Integer(1),Integer(K)])
    bank.append([Integer(1),Integer(-1),Integer(K)])
    bank.append([Integer(1),Integer(0),Integer(0),Integer(K)])

# positivity filter on first 200 primes
def ok(coeffs):
    f=poly(coeffs)
    return all(f(P[i])>0 for i in range(200))

results={}
r0works=0; never=0; tested=0
maxr=0
never_list=[]
hist={}
for coeffs in bank:
    if not ok(coeffs): continue
    tested+=1
    r=first_neg_consecutive_minor(coeffs)
    if r is None:
        never+=1; never_list.append(coeffs)
    else:
        hist[r]=hist.get(r,0)+1
        if r==0: r0works+=1
        maxr=max(maxr,r)

print(f"Tested (positive) polynomials: {tested}")
print(f"Leading D_2 (r=0) already gives negative minor: {r0works}/{tested}")
print(f"Some consecutive 3x3 minor negative: {tested-never}/{tested}")
print(f"NO consecutive 3x3 minor negative up to r=60: {never}")
print(f"Max r needed: {maxr}")
print("Histogram of first-working r:")
for r in sorted(hist): print(f"   r={r}: {hist[r]}")
if never_list:
    print("\nPolynomials with NO negative consecutive 3x3 minor (potential counterexamples!):")
    for coeffs in never_list[:30]:
        print("   ", coeffs)
