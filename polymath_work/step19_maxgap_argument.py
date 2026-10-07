"""
Unconditional existence of gap-spike windows via MAXIMAL GAP in a dyadic block.

Claim: Let M(X) = the maximal prime gap g_n among primes p_n in [X, 2X]. Let p_m be where
it is attained (g_m = M(X)). Then its NEIGHBOR gaps g_{m-1}, g_{m+1} are gaps between primes
that lie in (about) the same block, hence <= M(X). So g_m >= g_{m-1} and g_m >= g_{m+1}.
Thus  g_m^2 >= g_{m-1} g_{m+1}  ALWAYS (the spike condition, non-strict).

For the STRICT spike with growing margin (g_m^2 >> g_{m-1}g_{m+1}), we use:
  M(X) -> infinity faster than typical gaps: M(X) >= (1+o(1)) log X grows, and along a
  subsequence M(X) / (max neighbor) -> infinity (record gaps are isolated).
Here we just MEASURE: for the maximal gap in [X,2X], what is ratio g_m^2/(g_{m-1} g_{m+1}),
and the implied dmax. Show dmax -> infinity using ONLY the maximal-gap window.
"""
from sympy import primerange, Rational

P = list(primerange(2, 50_000_000))
Pidx = {p:i for i,p in enumerate(P)}

def Rxd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

def dmax(q1,q2,q3,q4, cap=2_000_000):
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

print("Maximal-gap window in [X,2X]: report gaps, spike ratio, dmax")
print(f"{'X':>10} {'maxgap':>7} {'nbr gaps':>14} {'g2^2/(g1g3)':>12} {'dmax':>8}")
X=1000
while X < 5_000_000:
    # find primes in [X,2X]; locate max gap
    loI = None
    # binary-ish: scan index range
    import bisect
    i0 = bisect.bisect_left(P, X)
    i1 = bisect.bisect_right(P, 2*X)
    best=-1; bi=None
    for i in range(i0, min(i1, len(P)-2)):
        g = P[i+1]-P[i]
        if g>best:
            best=g; bi=i
    # window q1=P[bi-1].. q4=P[bi+2] so middle gap is g_bi
    q1,q2,q3,q4 = P[bi-1],P[bi],P[bi+1],P[bi+2]
    g1=q2-q1; g2=q3-q2; g3=q4-q3
    ratio = (g2*g2)/(g1*g3)
    dm = dmax(q1,q2,q3,q4)
    print(f"{X:>10} {g2:>7} {str((g1,g3)):>14} {ratio:>12.2f} {dm:>8}")
    X*=2
