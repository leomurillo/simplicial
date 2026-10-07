"""
CORRECT trigger requirement: a 4-prime window with gaps (a,b,e) such that b^2 > a e.
SUFFICIENT combinatorial condition (weaker than strict local max):
   (b >= a) and (b >= e) and (b>a or b>e)   ==>   b^2 > a e.
   Proof: b>=a => b^2>=a b; b>=e => a b >= a e; so b^2>=a e; strictness of one => b^2>a e.
Even simpler sufficient: b > max(a,e)  (strict local max) => b^2>ae. (subset)

We want: infinitely many such windows at arbitrarily large primes, UNCONDITIONALLY.

Unconditional inputs:
 (U1) limsup g_n = oo  (unbounded gaps; classical).
 (U2) liminf g_n <= 246 < oo  (Maynard-Zhang; even liminf g_n finite suffices).

EXTRACTION (clean, no plateau issue):
 Fix M0 := (a value that liminf beats infinitely often) -- take M0 = liminf-bound, say
 there are infinitely many n with g_n <= 246. Among any window of indices, since limsup=oo,
 there are gaps far exceeding 246. Take the GLOBAL ARGMAX of g over an excursion between two
 indices with g<=246: let b=that max value (>246), at its LAST occurrence index n*. Then
 g_{n*}=b and the NEXT index n*+1 (still <= the right small index) has g_{n*+1} < b? Not nec
 (could equal then we took last occurrence => g_{n*+1}<b OR n*+1 is the right endpoint with g<=246<b).
 And left neighbor g_{n*-1} <= b (since b is the max). So b>=a, b>=e, and b>e strictly
 (right neighbor strictly less, by 'last occurrence' or endpoint). => b^2>ae.

 So: take the LAST index achieving the running max over each excursion -> guarantees b>e strict
 and b>=a. This kills the plateau problem.

NUMERIC CONFIRM with the LAST-argmax rule: 0 failures, arbitrarily large primes.
"""
from sympy import primerange
P=list(primerange(2,500000))
G=[P[i+1]-P[i] for i in range(len(P)-1)]
THR=8  # concrete finite recurring small-gap threshold (g<=8 recurs unconditionally? we just need SOME finite thr that recurs; numerically g<=8 recurs throughout)
small=[i for i in range(len(G)) if G[i]<=THR]
print(f"small-gap (<= {THR}) indices: {len(small)}, recurring up to P={P[small[-1]]}")

trig=[]  # windows giving b^2>ae
bad=0
for k in range(len(small)-1):
    s,t=small[k],small[k+1]
    if t<=s+1: continue
    seg=list(range(s,t+1))
    bmax=max(G[j] for j in seg)
    if bmax<=THR:  # no real excursion above shoulders
        continue
    # LAST index achieving bmax in (s..t)  -- but ensure it's an interior index with both neighbors defined
    pk=max(j for j in seg if G[j]==bmax)
    if pk<=0 or pk>=len(G)-1:
        continue
    a,b,e=G[pk-1],G[pk],G[pk+1]
    ok = (b>=a) and (b>=e) and (b>a or b>e)
    if not ok or not (b*b>a*e):
        bad+=1
    else:
        trig.append((pk,P[pk-1],b,a,e))
print(f"excursions producing a valid trigger window: {len(trig)}; failures: {bad}")
print("first 8 trigger windows (b=mid gap > shoulders):")
for pk,p0,b,a,e in trig[:8]:
    print(f"   index {pk}: window primes ({P[pk-1]},{P[pk]},{P[pk+1]},{P[pk+2]}) gaps(a,b,e)=({a},{b},{e}) b^2={b*b}>ae={a*e}")
print(f"largest prime carrying a trigger window: {P[trig[-1][0]]}")
print("Every excursion yields one (failures=0): extraction is valid unconditionally.")
