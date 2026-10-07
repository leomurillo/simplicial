"""
Goal: a CLEAN, PROVABLE sufficient condition for R<0 (minor negative) for ALL monic f of
degree d simultaneously, tied to an explicit prime configuration.

Configuration idea ('double-twin around a gap'):
  q1=p, q2=p+2, q3, q4=q3+2  with q3 - q2 = G large (a big prime gap), and q1,q2 twin, q3,q4 twin.
Then for monic f deg d:
  u=f(q2)/f(q1)=f(p+2)/f(p),  a=u-1  ~ d* (2/p) ... SMALL
  s=f(q4)/f(q3)=f(q3+2)/f(q3), e=s-1 ~ d*(2/q3) ... SMALL
  v=f(q3)/f(q2)=f(q3)/f(p+2), b=v-1 ~ (q3/p)^d - 1 ... LARGE (since q3>p+2 by gap G)
We want R = a e - b^2 + a b e (2+b) < 0.
Since b is large and a,e small, -b^2 dominates? But a*b*e*(2+b) ~ a e b^3 ... could be large.
Compare b^2 vs a e b^3 (2+b ~ b for large b): need b^2 > a e b^3, i.e. 1 > a e b, i.e. a e b < 1.
With a~2d/p, e~2d/q3, b~(q3/p)^d: a e b ~ (4 d^2 / (p q3)) (q3/p)^d. For FIXED gap this BLOWS UP in d.
=> 'double twin with bounded gap' FAILS for high d. Need q3/p -> 1 too, i.e. gap/p -> 0.

REAL config: ALL four primes close together (gaps all = O(log p)), but MIDDLE gap > geometric
mean of outer gaps. This keeps b small (like a,e) and uses the quadratic ae-b^2<0.
Let me just verify the precise sufficient condition numerically across a wide d-range, using
the actual prime windows that ARE gap-spikes, and confirm R<0 holds for ALL d up to large.
"""
from sympy import primerange, Integer, Rational, log as slog

P = list(primerange(2, 50_000_000))

def Rval_xd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

# For a gap-spike window (g1,g2,g3) with g2^2 > g1 g3 (normalized), test R<0 for ALL d=1..D
# using x^d (worst case among monic? we will test general monic separately).
# Pick windows from the data: scan primes, find windows with g2 large vs g1,g3, test all-d robustness.

def gaps(r):
    q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
    return q1,q2,q3,q4,(q2-q1,q3-q2,q4-q3)

# Find windows where R<0 for x^d for ALL d in 1..Dmax, and report the gap normalized ratio.
Dmax=2000
def works_all_d(q1,q2,q3,q4,Dtest):
    # test a geometric set of d plus check monotone trend; R(d) for large d ~ ab^2e d^4 sign?
    # We test all d in Dtest list; if all R<0, accept.
    for d in Dtest:
        if Rval_xd(d,q1,q2,q3,q4)>=0:
            return False,d
    return True,None

Dtest=[1,2,3,5,8,13,21,34,55,89,144,233,377,610,1000,1500,2000]

print("Scan for windows where x^d gives R<0 for ALL tested d up to 2000:")
found=[]
for r in range(0, 4000):
    q1,q2,q3,q4,g=gaps(r)
    g1,g2,g3=g
    # only bother with gap-spike candidates: g2^2 q1 q3 > g1 g3 q2^2
    if g2*g2*q1*q3 > g1*g3*q2*q2:
        ok,bad=works_all_d(q1,q2,q3,q4,Dtest)
        if ok:
            found.append((r,q1,q2,q3,q4,g))
            if len(found)<=20:
                # normalized spike ratio
                ratio = float(g2*g2*q1*q3)/(g1*g3*q2*q2)
                print(f"  r={r} primes=({q1},{q2},{q3},{q4}) gaps={g} spike-ratio={ratio:.2f}")
    if len(found)>=20:
        break
print(f"\nTotal all-d-robust gap-spike windows found in first 4000 r: {len(found)} (showed up to 20)")
if found:
    r,q1,q2,q3,q4,g=found[0]
    print(f"\nFirst all-d-robust window: r={r}, primes ({q1},{q2},{q3},{q4}), gaps {g}")
    print("R(x^d) for that window, sampled d:")
    for d in [1,10,100,1000,2000,5000]:
        R=Rval_xd(d,q1,q2,q3,q4)
        print(f"   d={d}: R<0? {R<0}")
