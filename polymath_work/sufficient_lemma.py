"""
SUFFICIENT LEMMA (make rigorous & EXACT).

We want, for s large: g_{s+1}^2 > rho(s) g_s g_{s+2}, rho(s)=f(p_{s+2})/f(p_s).

Bound each piece for monic f, deg d>=1, increasing on [p_1,oo) (true eventually; here we work s large).
Let a=p_s<b=p_{s+1}<c=p_{s+2}<e=p_{s+3}. gaps d_s=b-a, d_{s+1}=c-b, d_{s+2}=e-c.
g_s=f(b)-f(a), g_{s+1}=f(c)-f(b), g_{s+2}=f(e)-f(c).

By MVT: g_s=f'(x1)(b-a), g_{s+1}=f'(x2)(c-b), g_{s+2}=f'(x3)(e-c),
  a<x1<b<x2<c<x3<e. Since f' increasing (f convex for large x, deg>=2; for deg1 f'=const):
  f'(a)<=f'(x1)<=f'(b), etc.
So g_{s+1}^2/(g_s g_{s+2}) = [f'(x2)^2/(f'(x1)f'(x3))] * [d_{s+1}^2/(d_s d_{s+2})].
The bracket [f'(x2)^2/(f'(x1)f'(x3))]: since a<x1<x2<x3<e and f' increasing,
   f'(x2)^2/(f'(x1)f'(x3)) >= f'(x2)^2/(f'(x2)f'(e)) ... let me bound BELOW:
   f'(x1)<=f'(c), f'(x3)<=f'(e). So bracket >= f'(b)^2/(f'(c) f'(e))? No: x2>b => f'(x2)>=f'(b).
   bracket >= f'(b)^2/(f'(c) f'(e)).  And rho(s)=f(c)/f(a).

This is getting messy with general coefficients. Let me instead PROVE a clean uniform bound
using the degree only, valid for large p, then the recurrence of strong gap-local-maxima.

KEY UNIFORM BOUND (large p): for monic f deg d, and a<b<c<e all in [p_s, p_s+O(log^2 p_s)]
(consecutive primes, gaps = O(log^2) by any standard bound, even O(p^{0.6}) Ingham suffices):
  f'(x2)/f'(x1) = 1+O((x2-x1)/x1 * d) = 1 + O(d * log^2(p)/p) -> 1.  Likewise all f' ratios ->1.
  rho(s)=f(c)/f(a) = 1 + O(d*(c-a)/a) = 1 + O(d log^2 p / p) -> 1.
So for s large: bracket >= 1-eps and rho<=1+eps for any eps>0.
Then g_{s+1}^2 > rho g_s g_{s+2}  is implied by  (1-eps) d_{s+1}^2/(d_s d_{s+2}) > (1+eps),
i.e. d_{s+1}^2/(d_s d_{s+2}) > (1+eps)/(1-eps).
Choosing the gap-local-max windows where d_{s+1} >= 2 max(d_s,d_{s+2}):
  d_{s+1}^2/(d_s d_{s+2}) >= 4 max(d_s,d_{s+2})^2/(d_s d_{s+2}) >= 4. And 4 > (1+eps)/(1-eps)
  for eps<3/5. So for s large enough (eps<3/5), EVERY such window fires.  <-- RIGOROUS modulo
  "strong gap-local-max windows occur for arbitrarily large s".

REMAINING UNCONDITIONAL FACT NEEDED:
  (G) There are infinitely many s with d_{s+1} >= 2 max(d_s, d_{s+2})
      (a prime gap at least double both neighbors).
  Actually we can RELAX: for s large, eps is tiny, so we just need
  d_{s+1}^2 > (1+eps')/(1-eps') d_s d_{s+2} with eps'->0, i.e. essentially d_{s+1}^2 > d_s d_{s+2}
  infinitely often (gap NOT log-convex i.o.) -- which we PROVED in Claim B applied to f=p? NO,
  Claim B was for g_l (f-gaps). For the PURE prime gaps d_l we need the same: prime gaps not
  eventually log-convex. Same proof: if d_{l+1}^2<=d_l d_{l+2} eventually => d_l geometric or
  nonincreasing; nonincreasing impossible (limsup d_l=oo, Westzynthius); geometric impossible
  (d_l=O(log^2 p_l)=O(log^2 l) sub-polynomial, can't be geometric). => d_{l+1}^2>d_l d_{l+2} i.o.

  BUT "d_{l+1}^2>d_l d_{l+2} i.o." gives ratio>1, and we need ratio>(1+eps')/(1-eps')->1.
  Since at such l the ratio is >1 by an INTEGER-driven amount? d's are even integers (>=2 except
  first). If d_{l+1}^2>d_l d_{l+2} then since all are positive even integers, the ratio
  d_{l+1}^2/(d_l d_{l+2}) > 1 but could be 1+tiny (e.g. d_{l+1}=6,d_l=4,d_{l+2}=8: 36/32=1.125).
  As eps'->0 we need ratio bounded away from 1 i.o. -> need limsup of the gap-ratio >1 strictly,
  which holds since it's >=1.125>1 type values, but must EXCEED the s-dependent (1+eps')/(1-eps').
  Since eps'(s)->0, ANY fixed ratio>1 occurring i.o. with the SAME lower bound works:
  e.g. if ratio>=1.1 i.o. then for s large enough that (1+eps')/(1-eps')<1.1, those fire.

Let me CHECK: limsup_l d_{l+1}^2/(d_l d_{l+2}) -- is it bounded below away from 1 i.o.?
And does ratio>=1.1 occur for arbitrarily large l? (essentially yes, strong-local-max gives>=4).
"""
from sympy import primerange
P=list(primerange(2,5000000))
def gap(l): return P[l]-P[l-1]
from fractions import Fraction
# Among large l, do strong-local-max (d_{l+1}>=2max) occur? and ratio>=1.1?
smax=300000
strong=[]; mild=[]
for l in range(1,smax):
    dl,dl1,dl2=gap(l),gap(l+1),gap(l+2)
    if dl1>=2*max(dl,dl2): strong.append(l)
    r=Fraction(dl1**2,dl*dl2)
    if r>=Fraction(11,10): mild.append(l)
print(f"strong-local-max windows (d_{{l+1}}>=2max) in [1,{smax}]: count={len(strong)}, "
      f"max index={max(strong)}, e.g. last few: {strong[-3:]}")
print(f"  at those l, primes around p_{{l+1}}: ", [(l,P[l],gap(l),gap(l+1),gap(l+2)) for l in strong[-2:]])
print(f"ratio>=1.1 windows in [1,{smax}]: count={len(mild)}, max index={max(mild)}")
# arbitrarily large => max index near smax confirms recurrence at scale.
