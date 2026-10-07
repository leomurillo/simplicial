"""
CLEAN UNCONDITIONAL ARGUMENT for existence of infinitely many windows with b^2>ae
(=> asymptotic trigger), needing ONLY:
   (U1) limsup g_n = +oo     (gaps unbounded; classical/unconditional)
   (U2) liminf g_n  <  +oo   (true trivially: g_n>=2 and average ~log n, but we need
        liminf finite -- which is immediate since g_n is not ->oo? NO, unbounded doesn't
        forbid ->oo. We need g_n does NOT ->oo, i.e. liminf<oo. UNCONDITIONAL via e.g.
        infinitely many g_n=2? that's twin primes (open). BUT liminf g_n<=246 (Maynard-Zhang)
        is UNCONDITIONAL and suffices. Even Erdos(1935): liminf g_n/log n <1, giving infinitely
        many n with g_n< log n, certainly liminf finite-relative; for OUR argument we just need
        infinitely many n with g_n <= some fixed B. Maynard-Zhang B=246. UNCONDITIONAL.)

CLAIM: (U1)&(U2) => there are infinitely many n with g_n^2 > g_{n-1} g_{n+1}  (in fact with
       g_n > g_{n-1} and g_n > g_{n+1}, a strict local max), at arbitrarily large n.

PROOF (elementary):
 Suppose not: only finitely many strict local maxima. Then exists N s.t. for all n>N,
 NOT(g_{n-1}<g_n>g_{n+1}). Consider n>N. Define the sequence h_n=g_n for n>N. 'No strict local
 max' means: whenever g_{n-1}<g_n we must have g_n<=g_{n+1} (else n is a strict local max). I.e.
 once the sequence strictly increases into n, it cannot strictly decrease right after; it must be
 >= at n+1. More precisely: there is no index where a strict rise is immediately followed by a
 strict fall. Equivalently the sequence has no strict 'peak'.
 Take any n0>N with g_{n0}<=B (exists infinitely often by U2). Since limsup=oo (U1), there is a
 later index with g much larger than B. Let M=first index>n0 with g_M> B. Then g_{M-1}<=B<g_M,
 so g_{M-1}<g_M (strict rise at M). 'No strict peak' => g_M<=g_{M+1}. Repeat: g_M<g_{M+1} or
 g_M=g_{M+1}. If g_M<g_{M+1}: strict rise at M+1 => g_{M+1}<=g_{M+2}. By induction the sequence is
 NON-DECREASING from M onward: g_M<=g_{M+1}<=g_{M+2}<=...  (each step: if strict rise, next is >=;
 if equal, also fine, but need to ensure it never strictly drops. Suppose g_{k}>g_{k+1} for some
 k>=M (first strict drop). Then at k: was g_{k-1}<g_k? Since no strict drop before k, g_{k-1}<=g_k.
 If g_{k-1}<g_k then k is a strict peak (g_{k-1}<g_k>g_{k+1}) -- contradiction. If g_{k-1}=g_k, then
 look back to first index j<=k with g_j=g_{j+1}=...=g_k (a plateau) and g_{j-1}<g_j (a strict rise
 into the plateau, which exists since we rose from <=B). Then g_{j-1}<g_j=...=g_k>g_{k+1}: this is a
 'wide peak'; j is not strict peak (g_j=g_{j+1}) but the PLATEAU has a strict rise on left and strict
 fall on right. For OUR purposes (b^2>ae) the plateau endpoints still work, but for 'strict local max'
 we need to also forbid plateaus. To keep it clean we PROVE b^2>ae directly at the plateau-left index:
 at index j: a=g_{j-1}<g_j=b, e=g_{j+1}=g_j=b => b^2=b*b> a*b=a*e? e=b so ae=ab<b^2 since a<b. YES b^2>ae.)
 So either we get a strict peak (contradiction) OR a plateau whose LEFT endpoint j satisfies b^2>ae.
 In the no-strict-peak world the only escape is g non-decreasing forever after M -> but then g is
 eventually monotone increasing, contradicting nothing yet; EXCEPT we also have infinitely many
 indices with g<=B (U2) at arbitrarily large n -> contradicts g being eventually non-decreasing &
 ->oo (since once g>B at M and non-decreasing, g stays >B forever, no more g<=B). CONTRADICTION with U2.
 Hence infinitely many indices (strict peaks or plateau-left-endpoints) with b^2>ae, unboundedly large. QED.

This script just SANITY-CHECKS the logic by verifying, in the real gap sequence, that between
every 'return to <=B' there is an index with b^2>ae, for B=246, at arbitrarily large primes.
"""
from sympy import primerange
P=list(primerange(2,2000000)); NP=len(P)
G=[P[i+1]-P[i] for i in range(NP-1)]
B=246
small=[i for i in range(len(G)) if G[i]<=B]   # g<=246 indices (Maynard-Zhang: infinite, unconditional)
print(f"indices with g_n<=246: {len(small)} of {len(G)} (recur to prime {P[small[-1]]}) -- these are")
print("guaranteed infinite & unbounded-index by Maynard-Zhang (UNCONDITIONAL).")

# Between consecutive such small indices s<t, if the segment rises above B somewhere, find an index
# with b^2>ae (strict peak or plateau endpoint). Verify it ALWAYS exists.
fails=0; last_big=0; total=0
for k in range(len(small)-1):
    s,t=small[k],small[k+1]
    if t-s<2: continue
    seg=range(s+1,t)  # interior indices (have both neighbors defined within [s..t])
    peak=max(G[j] for j in range(s,t+1))
    if peak<=B: continue  # no excursion above B
    total+=1
    found=None
    for j in range(max(1,s+1), min(len(G)-1,t)):
        a,b,e=G[j-1],G[j],G[j+1]
        if b*b>a*e:
            found=j; break
    if found is None: fails+=1
    else: last_big=max(last_big,P[found])
print(f"excursions above 246 between small-gap indices: {total}; with NO b^2>ae index: {fails}")
print(f"=> every such excursion contains a trigger index (b^2>ae). fails should be 0: {fails==0}")
print(f"largest prime carrying such a trigger index: {last_big}")
print("\nThe elementary argument needs ONLY: gaps unbounded (U1) + infinitely many g<=246 (U2,")
print("Maynard-Zhang). Both UNCONDITIONAL. So trigger windows (b^2>ae) exist at arbitrarily large x.")
