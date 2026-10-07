import sys
from sympy import primerange
import bisect, math
def pr(*a): print(*a); sys.stdout.flush()
P=list(primerange(2,30_000_000))
pr("primes:",len(P))

# For MANY dyadic blocks [2^k, 2^{k+1}], find the maximal-gap window and its neighbor
# geometric ratio g2^2/(g1 g3). Report the MIN over all blocks (is it bounded away from 1?).
# Also report g2 / log(q2) (Westzynthius growth) to confirm spike magnitude grows.
pr(f"\n{'k':>3} {'q2~':>10} {'g2':>5} {'(g1,g3)':>10} {'geomratio':>9} {'g2/ln q2':>9}")
mins=1e9; mn_k=None
for k in range(8,25):
    X=2**k
    if 2*X>P[-1]: break
    i0=bisect.bisect_left(P,X); i1=bisect.bisect_right(P,2*X)
    best=-1;bi=None
    for i in range(i0,min(i1,len(P)-2)):
        g=P[i+1]-P[i]
        if g>best:best=g;bi=i
    q1,q2,q3,q4=P[bi-1],P[bi],P[bi+1],P[bi+2]
    g1=q2-q1;g2=q3-q2;g3=q4-q3
    gr=(g2*g2)/(g1*g3)
    glog=g2/math.log(q2)
    if gr<mins: mins=gr; mn_k=k
    pr(f"{k:>3} {q2:>10} {g2:>5} {str((g1,g3)):>10} {gr:>9.2f} {glog:>9.2f}")
pr(f"\nMIN geometric ratio over blocks k=8..24: {mins:.2f} (at k={mn_k})")

# Stronger: scan ALL local-max gaps (g_m>g_{m-1},g_m>g_{m+1}) with g_m>=4 log q, count and
# report distribution of geom ratio -- to argue ratio>=K windows are ABUNDANT, not rare.
pr("\nAmong local-max gaps with g_m >= c*log(q), fraction with geom ratio>=K:")
for c in (2,3,4):
    tot=0; ge2=0; ge3=0; ge4=0; ge8=0
    for i in range(2,len(P)-2):
        g2=P[i]-P[i-1]
        if g2 < c*math.log(P[i]): continue
        g1=P[i-1]-P[i-2]; g3=P[i+1]-P[i]
        if not (g2>g1 and g2>g3): continue
        tot+=1
        gr=(g2*g2)/(g1*g3)
        if gr>=2: ge2+=1
        if gr>=3: ge3+=1
        if gr>=4: ge4+=1
        if gr>=8: ge8+=1
    if tot:
        pr(f"  c={c}: count={tot}  ratio>=2:{ge2/tot:.2%}  >=3:{ge3/tot:.2%}  >=4:{ge4/tot:.2%}  >=8:{ge8/tot:.2%}")
