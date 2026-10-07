"""
PIN DOWN the unconditional core for (G').

We need: infinitely many l with  d_{l+1}^2 / (d_l d_{l+2}) >= K, for a FIXED K>1.
(Then at large such l, since rho(s)->1 and f'-bracket->1, criterion (*) fires.)

Candidate unconditional inputs (all classical, no RH):
 (U1) limsup_{l} d_l/log p_l = +oo  (Westzynthius 1931, Erdos). UNCONDITIONAL.
      Even stronger Rankin/Maier-Pomerance/Ford-Green-Konyagin-Tao. But basic limsup=oo
      version: there are gaps >= c log p * (loglog) ... i.o. Elementary version: limsup d_l=oo.
 (U2) For ANY M, infinitely many l with d_l > M (gaps unbounded). ELEMENTARY (factorials).
 (U3) liminf_l d_l <= 246 (Maynard-Tao-Zhang) UNCONDITIONAL but deep. Gives d_l<=246 i.o.

CLEAN ARGUMENT using (U2)+(U3):
   By (U3) there is a bounded value v<=246 attained by d_l infinitely often? Not quite: Zhang
   gives liminf<=246, i.e. SOME even value <=246 attained i.o. Call it v* (d_l=v* i.o.).
   By (U2) gaps are unbounded.
   Hmm, to get a LOCAL MAX with big ratio: take a HUGE gap d_{l+1}=D (from U2, D->oo). Its
   neighbors d_l, d_{l+2} are SOME gaps. We can't directly bound them small.

 BETTER CLEAN ARGUMENT (the right one) — strict local maxima with diverging ratio:
   Define A_l = d_l (positive even integers for l>=2). Since limsup A_l=+oo (U2) and the sequence
   does NOT diverge to +oo (because liminf A_l<=246<oo by U3, OR even elementarily liminf<=
   something finite: there are infinitely many l with d_l = d_{l+... } small? Actually we need
   liminf finite, which U3 gives, or the ELEMENTARY observation that consecutive gaps can't all
   grow: sum of first l gaps = p_{l+1}-2 ~ l log l, so AVERAGE gap ~ log l, so liminf d_l <=
   average ~ log l along a subsequence -> but that ->oo. So elementary average only gives
   liminf d_l = O(log l), not bounded. For BOUNDED liminf we DO need Zhang/Maynard (U3).)

   With limsup A_l=+oo and liminf A_l <= 246 (U3): the sequence has infinitely many "ascents to
   a record then descent". Precisely: pick a strictly increasing sequence of record positions
   n_1<n_2<... with A_{n_k}=record ->oo. Between consecutive records, the sequence comes back
   DOWN to <=246 infinitely often (by U3) BEFORE the next record region...
   This is getting delicate. Let me check the CLEANEST sufficient claim NUMERICALLY and see
   which classical theorem it maps to:

   CLAIM (G''): limsup_l d_{l+1}^2/(d_l d_{l+2}) = +oo.   [strongest, clearly true numerically]

Let me also test a fully different, ROBUST sufficient condition that may be elementary:
   At a STRICT one-sided record that is followed by a return to a small gap.
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,20000000))
def gap(l): return P[l]-P[l-1]
N=len(P)-3
# limsup of the centered ratio
mx=0; arg=0
for l in range(2,N):
    r=Fraction(gap(l+1)**2, gap(l)*gap(l+2))
    if r>mx: mx=r; arg=l
print(f"max d_{{l+1}}^2/(d_l d_{{l+2}}) over l<{N}: {float(mx):.1f} at l={arg}, primes near {P[arg]}")
print(f"  gaps there: d_l={gap(arg)} d_{{l+1}}={gap(arg+1)} d_{{l+2}}={gap(arg+2)}")
# growth of this max with cutoff -> shows limsup=+oo
for cut in [1000,10000,100000,1000000,N]:
    m=0
    for l in range(2,min(cut,N)):
        r=gap(l+1)**2/(gap(l)*gap(l+2))
        if r>m: m=r
    print(f"  cutoff {cut:>8}: running max ratio = {m:.1f}")
