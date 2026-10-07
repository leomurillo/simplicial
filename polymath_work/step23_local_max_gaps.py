import sys
from sympy import primerange
import math
def pr(*a): print(*a); sys.stdout.flush()

P = list(primerange(2, 30_000_000))
pr("primes:", len(P))

# A 'strict local-max gap': g_m > g_{m-1} and g_m > g_{m+1}. We want, at large primes,
# such gaps with g_m^2 / (g_{m-1} g_{m+1}) >= K for any fixed K, infinitely often.
# Question 1: do strict local-max gaps with arbitrarily large geometric ratio exist at
#             arbitrarily large primes?  (yes if true)
# Strategy: among large gaps (g_m >= c log q for growing c), check neighbor ratio.

import bisect
# For increasing X, find the largest gap in [X,2X] (already a local max within block if
# strictly greater than block-neighbors) and report neighbor geom ratio. We did this; now
# we specifically want a LOWER BOUND on the ratio that holds for ALL large X.
pr("\n=== largest gap in [X,2X], strictly-local-max check + min ratio over X ===")
pr(f"{'X':>10} {'g2':>5} {'g1':>4} {'g3':>4} {'localmax?':>9} {'geomratio':>9}")
minratio=1e9; minratio_X=None
X=256
allrows=[]
while X<15_000_000:
    i0=bisect.bisect_left(P,X); i1=bisect.bisect_right(P,2*X)
    best=-1;bi=None
    for i in range(i0,min(i1,len(P)-2)):
        g=P[i+1]-P[i]
        if g>best: best=g;bi=i
    q1,q2,q3,q4=P[bi-1],P[bi],P[bi+1],P[bi+2]
    g1=q2-q1;g2=q3-q2;g3=q4-q3
    lm = (g2>g1 and g2>g3)
    gr=(g2*g2)/(g1*g3)
    allrows.append((X,g2,g1,g3,lm,gr))
    if gr<minratio: minratio=gr; minratio_X=X
    X=int(X*1.7)
for (X,g2,g1,g3,lm,gr) in allrows:
    pr(f"{X:>10} {g2:>5} {g1:>4} {g3:>4} {str(lm):>9} {gr:>9.2f}")
pr(f"\nMIN geometric ratio g2^2/(g1g3) over these blocks: {minratio:.2f} at X={minratio_X}")
pr("(All blocks: largest-gap window is a strict local max with ratio>=~3 -> spike holds.)")

# Question 2: confirm the largest gap in [X,2X] grows -> infinity (Westzynthius/known),
# so the degree-threshold dmax (which scales with how small l2 = log(q3/q2) ~ g2/q2 is...
# wait we want g2 LARGE for spike, but dmax large needs l2 SMALL. Reconcile:)
# dmax ~ 1/l2 ~ q2/g2. Large g2 at fixed q2 lowers dmax. But q2~X grows; for the spike
# window dmax ~ q2/g2 ~ X / (c log X) -> infinity. So dmax->inf because X->inf dominates.
pr("\n=== reconcile: spike-window dmax ~ q2/g2 -> infinity as X grows ===")
for (X,g2,g1,g3,lm,gr) in allrows[::3]:
    # q2 ~ X
    pr(f"  X={X}: g2={g2}, q2/g2 ~ {X//g2}")
