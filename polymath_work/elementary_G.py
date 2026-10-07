"""
Can (G') be made ELEMENTARY (no deep ANT)?

Need: infinitely many l with d_{l+1}^2 >= K d_l d_{l+2}, K>1 FIXED (any K>1 works since
threshold (1+o(1))->1; even K=1+delta for tiny delta is fine but must be a FIXED constant
and the witnessing l -> infinity).

ELEMENTARY FACTS available (no PNT, no RH):
 (a) limsup d_l = +oo. ELEMENTARY: n!+2,...,n!+n are composite => some gap >= n near n!.
 (b) liminf d_l = 2 conjecturally (twin primes, OPEN). But liminf d_l is BOUNDED:
     d_l = 2 infinitely often is the twin prime conjecture (OPEN). However we do NOT need
     d_l=2 i.o.; we need d_l SMALL relative to a neighbor.
 (c) Zhang/Maynard: liminf d_l <= 246 (bounded gaps) -- DEEP but published & unconditional.

CLEAN ELEMENTARY ARGUMENT for (G') via (a)+(b-elementary):
 Consider any l where d_l achieves a "record relative to recent history". Actually simplest:
 Take the sequence of MAXIMAL gaps. Let G_k be record gaps (d at record positions n_k).
 At a record, d_{n_k} > d_j for all j<n_k, in particular d_{n_k} > d_{n_k -1}. That's a LEFT
 local max but says nothing about the RIGHT neighbor d_{n_k+1}.

 Try: the gap sequence d_l is NOT eventually monotone and has limsup=oo, liminf finite.
 A sequence of positive integers with limsup=oo must have infinitely many STRICT local maxima
 (l with d_l>d_{l-1} and d_l>=d_{l+1}, or >). At a strict local max, d_l>d_{l-1} and d_l>d_{l+1}
 (if strict both sides). Then d_l^2 > d_{l-1} d_{l+1}? Only if d_l^2 > d_{l-1}d_{l+1}; with
 d_l>d_{l-1},d_l>d_{l+1} we get d_l^2 > d_{l-1} d_{l+1} ALWAYS (product of two smaller). YES!
   If d_l > d_{l-1} and d_l > d_{l+1} (strict local max), then d_l^2 > d_{l-1} d_{l+1}.
 So every strict local max l of the gap sequence gives ratio (centered at l) d_l^2/(d_{l-1}d_{l+1})>1.
 That's the plain version => ratio>1 but maybe ->1. For a FIXED margin need d_l >= (1+c)max(nb).

 The integers help: gaps are EVEN for l>=2 (all primes >2 odd => gaps even), and >=2. If d_l is a
 strict local max among EVEN integers, d_l >= d_{l-1}+2 and d_l>=d_{l+1}+2. Then
   d_l^2/(d_{l-1}d_{l+1}) >= (m+2)^2/(m * m) for m=max(d_{l-1},d_{l+1})? Not bounded away from 1
   if m large. So margin ->1 if the local max is only +2 above large neighbors. NOT enough alone.

 NEED: local max where d_l >= 2*max(neighbors) (strong). Does limsup d_l=oo FORCE strong local
 maxima i.o.? Consider record gaps: at a record n_k, d_{n_k}=G_k. The NEXT gap d_{n_k+1} could
 be anything <=G_k. The PREVIOUS gap d_{n_k -1}<G_k. If both neighbors <= G_k/2 we win.
 Numerically check: at RECORD gaps, are both neighbors <= half the record? And is there a clean
 unconditional reason? Let me check record gaps and their neighbors.
"""
from sympy import primerange
P=list(primerange(2,20000000))
def gap(l): return P[l]-P[l-1]
# record gaps
rec=[]; mx=0
for l in range(1,len(P)-2):
    g=gap(l)
    if g>mx:
        mx=g; rec.append(l)
print("Record-gap positions l, gap, left neighbor d_{l-1}, right neighbor d_{l+1}, max(nb), ratio g^2/(nb_l*nb_r):")
from fractions import Fraction
strong_rec=0
for l in rec:
    if l<2: continue
    dl=gap(l); dm=gap(l-1); dp=gap(l+1)
    ratio=float(Fraction(dl**2,dm*dp))
    strong = dl>=2*max(dm,dp)
    strong_rec += strong
    print(f"  l={l:>8} d_l={dl:>4} d_{{l-1}}={dm:>4} d_{{l+1}}={dp:>4} max_nb={max(dm,dp):>4} ratio={ratio:>8.2f} strong={strong}")
print(f"\n# record gaps with d_l>=2max(neighbors): {strong_rec}/{len([l for l in rec if l>=2])}")
