"""
UNCONDITIONAL configuration (no twins). We need windows q1<q2<q3<q4 (consecutive primes)
with l1 l3 < l2^2 (middle log-gap spike) at arbitrarily large q, with margin giving
dmax -> infinity.

Relaxed criterion: just require g2^2 > K * g1 * g3 for some fixed K>1 (with q-normalization
negligible across a 4-window). I.e. the MIDDLE gap dominates the geometric mean of its
neighbors by a factor sqrt(K).  This is an unconditional 'local-max gap' statement.

Test: scan ALL windows (not just twin), pick those with g2^2 >= 3*g1*g3, of increasing q,
and report dmax (largest d with R(x^d)<0). Does dmax -> infinity? What K gives clean growth?

ALSO: the truly unconditional existence claim we can cite:
  (Erdos / classical) limsup g_n/log n = infinity  AND  there are infinitely many n with
  g_n a strict local maximum exceeding neighbors by any fixed factor (because gaps are not
  eventually monotone). We just need K=O(1).  Verify K=3 and K=2 both give dmax->inf.
"""
from sympy import primerange, Rational
import math

P = list(primerange(2, 50_000_000))

def Rxd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

def dmax(q1,q2,q3,q4, cap=300000):
    if Rxd(1,q1,q2,q3,q4)>=0: return 0
    lo=1; hi=2
    while hi<cap and Rxd(hi,q1,q2,q3,q4)<0:
        lo=hi; hi*=2
    if Rxd(min(hi,cap),q1,q2,q3,q4)<0: return min(hi,cap)
    while hi-lo>1:
        mid=(lo+hi)//2
        if Rxd(mid,q1,q2,q3,q4)<0: lo=mid
        else: hi=mid
    return lo

for K in (2,3):
    print(f"\n===== Relaxed spike  g2^2 >= {K} * g1*g3  (NO twin requirement) =====")
    seen=0
    last_q=0
    rows=[]
    for r in range(0, 300000):
        q1,q2,q3,q4=P[2*r],P[2*r+1],P[2*r+2],P[2*r+3]
        g1=q2-q1;g2=q3-q2;g3=q4-q3
        if g2*g2 >= K*g1*g3 and q1 > last_q*1.4:  # take a geometric subsample of growing q
            dm=dmax(q1,q2,q3,q4)
            rows.append((q1,(g1,g2,g3),dm))
            last_q=q1
            seen+=1
        if seen>=22: break
    for (q1,g,dm) in rows:
        print(f"  q1={q1:9d} gaps={g} dmax={dm}")
    print(f"  -> dmax grows with q? first dmax={rows[0][2]}, last dmax={rows[-1][2]}")
