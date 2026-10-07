"""
Quantify rho(s)=f(p_{s+2})/f(p_s) and find a RIGOROUS sufficient condition for (*).

(*) is  g_{s+1}^2 > rho(s) g_s g_{s+2},  rho(s)=c_{s+2}/c_s = f(p_{s+2})/f(p_s).

Strategy for a clean SUFFICIENT condition:
  g_l = f(p_{l+1})-f(p_l). For monic f deg d>=1 with f increasing on [2,oo) (true for large p;
  handle small p separately), g_l>0.

  UPPER bound rho(s): f(p_{s+2})/f(p_s). Since f monic deg d, for p>=2,
     f(p_{s+2})/f(p_s) <= (p_{s+2}/p_s)^d * (1+small)? Not exactly monotone in general coeffs.
  Better: we don't need asymptotics. We need, at a SPECIFIC good window, a clean bound.

KEY ALTERNATIVE — exploit a SINGLE explicit prime configuration that recurs:
  Consider three consecutive prime gaps (d_s, d_{s+1}, d_{s+2}) = (2, k, 2) with k>=4
  ('isolated' structure: p, p+2 twin... no). Actually we want the MIDDLE gap big, outer small.

Let me instead directly bound, for the SPECIFIC f and using exact integer arithmetic, the
quantity  g_{s+1}^2 - rho(s) g_s g_{s+2} and show >0. But that's per-f.

For a UNIFORM proof we need: inf over monic f of [sup over s of (R(s)-rho(s))] > 0, basically.

Let me test the cleanest LEMMA candidate:
  LEMMA?: For every monic f (deg>=1, eventually increasing), there are infinitely many s with
     g_{s+1}^2 >= 4 g_s g_{s+2}  AND  rho(s) < 4    simultaneously?
  If gaps (d_s,d_{s+1},d_{s+2})=(2,4,2)-like recur with bounded primes ratio... but as p->oo
  rho(s)->1 so rho<4 eventually always. So really need: infinitely many s with R(s)>=1+eps
  for some fixed eps, OR even R(s) bounded below by something and rho->1.

Let me measure: liminf and limsup of R(s) over the (2,k,2)-type windows, and confirm
rho(s)->1, so eventually R(s)>rho(s) at every (small,big,small) window.
"""
from sympy import primerange
from fractions import Fraction

P = list(primerange(2, 2000000))
NP=len(P)

def test_f(ff, name, smax=2000):
    # find windows where gap pattern is 'local max in middle': d_{s+1}>d_s and d_{s+1}>d_{s+2}
    d=[P[l]-P[l-1] for l in range(1,smax+5)]  # d[k]=p_{k+1}-p_k, 1-indexed prime gap d_k for k=1.. ; here d[0]=p2-p1
    # careful indexing: d[i] = P[i+1]-P[i] = gap after p_{i+1}. Let's define gap(l)=P[l]-P[l-1] for l>=1 (gap between p_l and p_{l+1})
    def gap(l): return P[l]-P[l-1]   # = p_{l+1}-p_l, l from 1
    def c(l): return ff(P[l-1])
    cnt_fire=0; cnt_localmax=0; first=None
    Rvals_at_localmax=[]
    for s in range(1, smax+1):
        gs=gap(s); gs1=gap(s+1); gs2=gap(s+2)  # prime gaps
        ggs = c(s+1)-c(s); ggs1=c(s+2)-c(s+1); ggs2=c(s+3)-c(s+2)  # f-gaps g
        R = Fraction(int(ggs1)**2, int(ggs*ggs2))
        rho = Fraction(int(c(s+2)), int(c(s)))
        if R>rho:
            cnt_fire+=1
            if first is None: first=s
        if gs1>gs and gs1>gs2:
            cnt_localmax+=1
            Rvals_at_localmax.append(float(R))
    print(f"{name:12s}: first fire s={first}, #fires in [1,{smax}]={cnt_fire}, "
          f"#gap-local-max windows={cnt_localmax}, R at localmax: min={min(Rvals_at_localmax):.3f} "
          f"max={max(Rvals_at_localmax):.3f} mean={sum(Rvals_at_localmax)/len(Rvals_at_localmax):.3f}")

for nm,ff in [("p",lambda p:p),("p^2+1",lambda p:p**2+1),("p^3+1",lambda p:p**3+1),
              ("p^5+1",lambda p:p**5+1),("p^10+1",lambda p:p**10+1)]:
    test_f(ff,nm,2000)
