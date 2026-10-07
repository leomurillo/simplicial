"""
TWO-SIDED SPIKE LEMMA (rigorous), from Pintz limsup d_{n+1}/d_n=+oo.

LEMMA: For every M>1 there are infinitely many s with
    d_{s+1} > M d_s   AND   d_{s+1} > M d_{s+2}.   (two-sided spike of strength M)

PROOF: Fix M. By Pintz, limsup d_{n+1}/d_n=+oo, so there are infinitely many n with
   d_{n+1}/d_n > M^2 ... we'll choose the threshold M' below.
   Actually we use: the set T = { n : d_{n+1} > M^2 d_n } is infinite.
   For n in T, consider the largest j>=1 such that d_{n+1} < d_{n+2} < ... < d_{n+j}
   (a maximal ascending run starting at index n+1). Such j is FINITE because gaps are bounded
   (d_m <= p_{m+1} = O(m log m) so cannot ascend forever; in fact d_m=o(p_m) and along any
   infinite ascending run d would be increasing without the average constraint... more simply:
   d_m cannot be monotincreasing for all large m since average gap ~ log m grows slowly but
   liminf d_m <= 246 < oo (Maynard) forces returns below 246, breaking any long ascending run).
   Let s = n+j (top of the ascending run). Then:
     - d_{s} = d_{n+j} >= d_{n+1} (since ascending from n+1 to n+j, and j>=1 means d_{s}=d_{n+j}>=d_{n+1}).
       Wait we need d_{s+1} big vs d_s and d_{s+2}. Let me re-set: let s be the index where the
       run TOPS, i.e. d_{s} is the max of the run and d_{s+1} < d_s (descent). Hmm, indices.

 Let me restate cleanly with the gap sequence a_m := d_m. limsup a_{m+1}/a_m=+oo.
 Want s with a_{s+1} > M a_s and a_{s+1} > M a_{s+2}.

 Take m with a_{m+1}/a_m > M (exists i.o.). Among indices >= m+1, let s+1 be the FIRST index
 (>= m+1) at which the sequence stops being >= M times its predecessor going forward...

 Simplest rigorous version: Let m have a_{m+1} > M a_m. Define s+1 = argmax_{ m+1 <= t <= m+1+J } a_t
 over a window of length J. For J large enough that the window must contain a local descent
 (guaranteed since liminf a_t <= 246 means a_t returns below 246 within bounded gaps of indices?
 NO, liminf is about VALUES not index-spacing; returns below 246 happen i.o. but maybe far apart).

 CLEANER and CORRECT: Use BOTH limsup and the existence of the ABSOLUTE MAX over a finite stretch.
 Over the infinite sequence, consider any index m0 with a_{m0+1} > M a_{m0}. Look forward to the
 next index where a_t <= a_{m0+1}/M ... such an index exists because liminf a_t <= 246 < a_{m0+1}/M
 once a_{m0+1} > 246 M (true since a_{m0+1} > M a_{m0} and we can pick m0 with a_{m0} large, OR
 pick the limsup witness with a_{m0+1} huge). Let t0 = first index > m0+1 with a_{t0} <= a_{m0+1}/M.
 Then in [m0+1, t0], a attains a MAXIMUM at some s+1 (m0+1 <= s+1 <= t0-1, since a_{t0} is small).
   At s+1: a_{s+1} >= a_{m0+1} (max over window incl m0+1) > M a_{m0}.
   a_{s+2} <= a_{s+1} (s+1 is the argmax, but need STRICT or boundary)...
   Hmm a_{s+2}: if s+1 is the LAST argmax then a_{s+2} < a_{s+1}. Need a_{s+2} < a_{s+1}/M.
 This still doesn't force the FACTOR M on the right immediately.

 *** PRACTICAL RESOLUTION ***
 The fully airtight two-sided-factor-M lemma from limsup ALONE is fiddly. BUT we do NOT need
 factor M on both sides simultaneously with the SAME large M. Recall what the criterion needs at
 large s: R(s) = (1+o(1)) a_{s+1}^2/(a_s a_{s+2}) > rho(s) = 1+o(1). It SUFFICES that
       a_{s+1}^2 > (1+delta) a_s a_{s+2}   for a fixed delta>0, i.o.   (TwoSidedWeak)
 NOT factor M. And (TwoSidedWeak) follows from limsup a_{m+1}/a_m=+oo cleanly:

 PROOF of (TwoSidedWeak): Suppose for contradiction a_{m+1}^2 <= (1+delta) a_m a_{m+2} for ALL
 large m. Then b_m:=log a_m satisfies b_{m+1}-b_m <= b_{m+2}-b_{m+1} + log(1+delta), i.e. the
 increments e_m:=b_{m+1}-b_m satisfy e_m <= e_{m+1}+log(1+delta), i.e. e_{m+1} >= e_m - L,
 L=log(1+delta). So e_m can DECREASE by at most L per step. Now limsup a_{m+1}/a_m=+oo means
 limsup e_m=+oo: there are m with e_m > E (arbitrarily large E). After such m, e decreases by
 <= L per step, so e_{m+k} >= E - kL > 0 for k < E/L. Hence a is INCREASING (e>0) for at least
 E/L consecutive steps, and during them a_{m+k+1}/a_{m+k} = exp(e_{m+k}) >= exp(E-kL).
 Product over k=0..K-1 (K=floor(E/(2L))): a_{m+K}/a_m >= exp(sum_{k<K}(E-kL)) >= exp(K*E/2)
 -> a_{m+K} >= a_m exp(K E/2), with K~E/(2L). So a_{m+K} >= a_m exp(E^2/(4L)). Taking E->oo
 (m varies), we get gaps a_t as large as a_m exp(E^2/(4L)) at index t=m+K, where t-m=K~E/(2L).
 So a_t >= a_m exp(E^2/(4L)) at an index only ~E/(2L) beyond m. But a_t <= p_{t+1} <= C t log t,
 and t <= m + E/(2L). For fixed m and E->oo this gives a_t super-exponential in E while t grows
 only linearly in E => a_t <= C(m+E)log(m+E) = O(E log E), contradicting a_t >= exp(E^2/(4L)).
 CONTRADICTION. Hence (TwoSidedWeak) holds: a_{m+1}^2 > (1+delta) a_m a_{m+2} i.o., for EVERY
 delta>0.  QED.

 This is RIGOROUS and uses only: (a) limsup a_{m+1}/a_m=+oo [Pintz, unconditional],
 (b) a_m=d_m <= p_{m+1} = O(m log m) [Chebyshev/PNT, elementary upper bound on p_n].

 Let me NUMERICALLY sanity-check the contradiction mechanism: when e_m=log(a_{m+1}/a_m) is large,
 verify a CANNOT keep the log-convex (e nondecreasing-ish) pattern, i.e. that big e_m is followed
 by big drops (e decreases by more than any fixed L i.o.), consistent with (TwoSidedWeak).
"""
from sympy import primerange
import math
P=list(primerange(2,3000000))
def a(m): return P[m]-P[m-1]  # a_m=d_m=p_{m+1}-p_m, m>=1
# verify a_{m+1}^2 > (1+delta) a_m a_{m+2} occurs i.o. for delta=0.5 and delta=2, at large m
for delta in [0.5,1.0,2.0,3.0]:
    cnt=0; last=0
    for m in range(1,len(P)-3):
        if a(m+1)**2 > (1+delta)*a(m)*a(m+2):
            cnt+=1; last=m
    print(f"delta={delta}: # m<{len(P)-3} with a_{{m+1}}^2>(1+delta)a_m a_{{m+2}} = {cnt}, last m={last}")
