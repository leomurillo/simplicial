"""
Refined leading criterion using LOG-gaps. Define for window q1<q2<q3<q4:
   l1=log(q2/q1), l2=log(q3/q2), l3=log(q4/q3)  (positive 'log-gaps').
Claim: minor M_{r,r+1,r+2}<0  for monic deg-d f, q large,  is governed by
   sign( l1*l3 - l2^2 ):  if l1*l3 < l2^2 (middle log-gap spike), then R<0 for q>>d.
Verify:
 (1) For x^d at gap-spike windows, sign(R) == sign(l1 l3 - l2^2)  (large primes).
 (2) The DEGREE cancels: same sign threshold for all d (at fixed large window).
 (3) Existence: among primes, l1 l3 < l2^2 happens infinitely often & with margin.
     Simplest guaranteed instance: q1,q2 twin (l1=log((q1+2)/q1)~2/q1 small),
        q3,q4 twin (l3 small), middle gap big (l2 not small) => l1 l3 << l2^2. EASY.
"""
from sympy import primerange, Integer, Rational, log, N
import math

P = list(primerange(2, 50_000_000))

def loggaps(q1,q2,q3,q4):
    l1=math.log(q2/q1); l2=math.log(q3/q2); l3=math.log(q4/q3)
    return l1,l2,l3

def Rxd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

# (1)+(2): sign agreement across windows and degrees
print("=== sign(R(x^d)) vs sign(l1 l3 - l2^2), large-prime windows, d=1..50 ===")
# choose windows in a large-prime range r in [2000,2400] to ensure q large
mismatch=0; total=0; spike_windows=0
for r in range(2000, 2600):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    l1,l2,l3=loggaps(q1,q2,q3,q4)
    crit = l1*l3 - l2*l2   # <0 => predict R<0
    for d in [1,2,3,5,10,20,50]:
        R=Rxd(d,q1,q2,q3,q4)
        total+=1
        if (R<0) != (crit<0):
            mismatch+=1
print(f"  windows r in [2000,2600), d in 7 values: total={total}, sign mismatches={mismatch}")
print(f"  (mismatches expected ~0 since q ~ 1.7e4 >> d<=50)")

# (3) Existence with margin via twin-spike: scan for q1,q2 twin & q3,q4 twin & middle gap big
print("\n=== Twin-spike windows (q1,q2 twin; q3,q4 twin; big middle gap) ===")
cnt=0
examples=[]
for r in range(0, 4000):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    if q2-q1==2 and q4-q3==2 and (q3-q2)>=8:
        cnt+=1
        l1,l2,l3=loggaps(q1,q2,q3,q4)
        if len(examples)<12:
            examples.append((r,q1,q2,q3,q4,q3-q2, l1*l3, l2*l2))
print(f"  count of twin-spike windows in first 4000 r: {cnt}")
for (r,q1,q2,q3,q4,mg,lhs,rhs) in examples:
    print(f"   r={r}: ({q1},{q2},{q3},{q4}) midgap={mg}  l1*l3={lhs:.3e}  l2^2={rhs:.3e}  spike={lhs<rhs}")

# For a twin-spike window, verify R(x^d)<0 for a big d-range (q must beat d)
r,q1,q2,q3,q4,mg,lhs,rhs=examples[0]
print(f"\nR(x^d)<0 at twin-spike window ({q1},{q2},{q3},{q4}):")
maxgood=0
for d in range(1,4000):
    if Rxd(d,q1,q2,q3,q4)>=0:
        break
    maxgood=d
print(f"  R<0 for all d in 1..{maxgood}; fails at d={maxgood+1}  (q~{q1}, so threshold scales with q)")
