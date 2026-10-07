"""
RIGOROUS CORE ARGUMENT (asymptotic).

Claim A: For monic f (deg d>=1), rho(s):=f(p_{s+2})/f(p_s) -> 1 as s->oo.
   Proof sketch: p_{s+2}/p_s -> 1 (consecutive primes ratio ->1, since p_{n+1}/p_n->1
   by PNT). f monic deg d => f(x)=x^d(1+o(1)). So f(p_{s+2})/f(p_s)=(p_{s+2}/p_s)^d (1+o(1))->1.

Claim B: limsup_s R(s) > 1, in fact R(s) > 1+eps0 for infinitely many s, for a UNIVERSAL eps0,
   where R(s)=g_{s+1}^2/(g_s g_{s+2}), g_l=f(p_{l+1})-f(p_l).
   Heuristic: if g_{s+1}^2 <= g_s g_{s+2} for ALL s>=S (log-convex tail), then for s>=S,
   log g_{s+1} - log g_s is nondecreasing => g_s grows at least geometrically:
   g_s >= g_S * r^{s-S} with r=g_{S+1}/g_S>1 (if r>1). That forces f(p_s) ~ sum g >= geometric
   => f(p_s) grows exponentially in s. But f(p_s) <= poly(p_s) = poly(O(s log s)) -- polynomial
   in s. Contradiction unless r<=1, i.e. g eventually nonincreasing -- but g_l=f(p_{l+1})-f(p_l)
   -> infinity for deg>=1 (since f increasing unboundedly and gaps>=2... actually g_l>=f'(p_l)*2).
   So g_l -> oo, cannot be eventually nonincreasing. => log-convex tail impossible
   => g_{s+1}^2 > g_s g_{s+2} infinitely often => R(s)>1 i.o.

   The subtlety: R(s)>1 i.o. gives R(s)>1, but we need R(s)>rho(s) and rho(s)->1 from ABOVE.
   Need R(s) bounded AWAY from 1 i.o., OR R(s)>1 with rho(s)-1 smaller. Since rho(s)->1 but
   is always >1, R(s)>1 alone might not beat it if R(s)->1+. Need a quantitative gap.

   STRONGER: I'll show limsup R(s) >= some constant >1 UNCONDITIONALLY via gap fluctuation.

Let me FIRST verify Claim A numerically (rho->1) and measure how fast, and limsup R(s).
"""
from sympy import primerange
from fractions import Fraction
import math

P = list(primerange(2, 5000000))
def gap(l): return P[l]-P[l-1]

# rho(s) for f=p: = p_{s+2}/p_s
print("rho(s)=p_{s+2}/p_s for f=p, sampled (should ->1):")
for s in [10,100,1000,10000,100000,300000]:
    print(f"  s={s:>7}: p_s={P[s-1]}, p_{{s+2}}={P[s+1]}, rho={P[s+1]/P[s-1]:.6f}")
print()

# limsup R(s) and how often R(s) exceeds thresholds, f=p
def Rp(s): return Fraction(gap(s+1)**2, gap(s)*gap(s+2))
smax=300000
maxR=0; argmax=0
cnt={1.5:0,2:0,3:0,4:0}
for s in range(1,smax):
    r=Rp(s); rf=float(r)
    if rf>maxR: maxR=rf; argmax=s
    for t in cnt:
        if rf>t: cnt[t]+=1
print(f"f=p, s in [1,{smax}]: max R(s)={maxR:.3f} at s={argmax}")
print(f"  #(R>1.5)={cnt[1.5]}, #(R>2)={cnt[2]}, #(R>3)={cnt[3]}, #(R>4)={cnt[4]}")
print(f"  fraction R>2: {cnt[2]/smax:.4f}, R>3: {cnt[3]/smax:.4f}")
