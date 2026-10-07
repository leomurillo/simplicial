"""
Confirm: at a FIXED 'universal' window (e.g. r=21, primes 191,193,197,199 gaps 2,4,2),
high enough degree f=x^d makes R>=0 (minor NOT negative), breaking universality.
Then: for such high-degree f, find the window r that DOES work (should be larger),
confirming max-r grows with degree (so no finite window set is universal).
"""
from sympy import primerange, Integer, Rational

P = list(primerange(2, 50_000_000))
print("primes available:", len(P), "max prime ~", P[-1])

def Rval_xd(d,r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

# r=21 window
print("\n=== r=21 window (191,193,197,199), f=x^d, R sign vs d ===")
for d in [1,5,10,20,40,60,80,95,100,120,150,200]:
    R=Rval_xd(d,21)
    print(f"  d={d:3d}: R<0? {R<0}   (sign {'-' if R<0 else '+'})")

# Find threshold d where r=21 flips from R<0 to R>=0
lo,hi=1,500
# find first d with R>=0
firstbad=None
for d in range(1,500):
    if Rval_xd(d,21)>=0:
        firstbad=d; break
print(f"\nfirst degree d making r=21 FAIL (R>=0): {firstbad}")

# For a high degree (say d=200), find the first window r that works
def first_r_xd(d, RMAX=2000):
    for r in range(RMAX):
        if Rval_xd(d,r)<0:
            return r
    return None
for d in [60,100,150,200,300,400]:
    fr=first_r_xd(d)
    if fr is not None:
        q1,q2,q3,q4=P[2*fr],P[2*fr+1],P[2*fr+2],P[2*fr+3]
        print(f"  d={d}: first working r={fr}, primes=({q1},{q2},{q3},{q4}) gaps=({q2-q1},{q3-q2},{q4-q3})")
    else:
        print(f"  d={d}: NO working r up to 2000 (!!)")
