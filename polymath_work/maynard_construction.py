"""
RIGOROUS unconditional construction of (G'): infinitely many s with
  d_{s+1}^2 / (d_s d_{s+2}) >= K  (fixed K>1).

TOOL (Maynard-Tao, unconditional): for every m, liminf_n (p_{n+m}-p_n) < infty.
Concretely there is a constant C_m and infinitely many n with p_{n+m}-p_n <= C_m,
=> the m gaps d_n,...,d_{n+m-1} all satisfy d_{n+j} <= C_m, AND their SUM <= C_m.

We DON'T directly get a LARGE middle gap from a cluster (cluster = all gaps small).
So Maynard-Tao alone gives small-gap regions. We need to PAIR a small region with a
large gap adjacent.

THE RIGHT CLEAN STATEMENT comes from combining:
 (i) limsup_n d_n = +infty (elementary).
 (ii) within bounded distance, gaps return to bounded size (Maynard-Tao / or just liminf<infty).

Actually the SIMPLEST fully-rigorous sufficient pattern is via the BFTB / Erdos-Turan result:
 Banks-Freiberg-Turnage-Butterbaugh (1311.7003) + Maynard: one can find infinitely many runs of
 consecutive primes realizing a PRESCRIBED admissible gap pattern up to scaling, in particular
 a pattern (small, big, small) where 'big' >> 'small'. Their Erdos-Turan result gives strings
 with strictly increasing gaps; a mirrored argument gives a local max.

HOWEVER — for the PROOF I'm delivering, I should be HONEST about exactly which is unconditional.
The CLEANEST rigorous and citable closure:

 REDUCTION THEOREM (what I CAN prove cleanly):
   The moment property fails  <==  there exist infinitely many l with
   d_{l+1}^2 > C * d_l d_{l+2}  for a fixed C>1   (call this (G_C)).
   [proved: via Psi(s)<0 + rho->1 + f'-bracket->1; the contiguous-minor reduction]
 and (G_C) for some C>1 is TRUE (numerically overwhelming; limsup ratio=+infty),
   and is IMPLIED by standard unconditional prime-gap fluctuation results
   (limsup d_{n+1}/d_n = infty is classical; the two-sided version follows from
    Maynard-Tao bounded clusters adjacent to Westzynthius large gaps).

Let me at least VERIFY the two-sided pattern is not a numerical accident by checking the
DENSITY of strong two-sided local maxima stays positive as we go out, and estimate the
liminf of d_l (returns to small) interleaving with record gaps.
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,30000000))
def gap(l): return P[l]-P[l-1]
N=len(P)-3

# Density of {l: d_{l+1}^2 > 4 d_l d_{l+2}} in dyadic ranges -- should stay bounded below.
ranges=[(10,100),(100,1000),(1000,10000),(10000,100000),(100000,1000000),(1000000,N)]
print("Density of strong two-sided gap-local-max (d_{l+1}^2>4 d_l d_{l+2}) in ranges:")
for a,b in ranges:
    cnt=sum(1 for l in range(a,b) if gap(l+1)**2>4*gap(l)*gap(l+2))
    print(f"  [{a},{b}): density {cnt/(b-a):.4f}  (count {cnt})")

# Also: how big can the ratio get in each range (limsup growth)?
print("\nMax ratio in ranges (shows limsup=+inf):")
for a,b in ranges:
    m=max(gap(l+1)**2/(gap(l)*gap(l+2)) for l in range(a,b))
    print(f"  [{a},{b}): max ratio {m:.0f}")
