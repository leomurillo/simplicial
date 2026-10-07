"""
QUANTITATIVE closure: need R(s) > rho(s), rho(s)->1.

Two sub-results to make rigorous:
 (Q1) rho(s)=f(p_{s+2})/f(p_s) <= 1 + C_f/p_s  for large s, some constant C_f.  [easy, calculus]
      Actually rho(s)-1 = [f(p_{s+2})-f(p_s)]/f(p_s). Numerator <= f'(p_{s+2})(p_{s+2}-p_s)
      <= f'(p_{s+2}) * (d_s+d_{s+1}).  Hmm depends on gaps. Cleaner bound:
      rho(s) = f(p_{s+2})/f(p_s). For monic deg d, f(p_{s+2})/f(p_s) <= (p_{s+2}/p_s)^d * K
      for some K? Not uniform. Let's just bound rho(s) <= (p_{s+2}/p_s)^d * (1+o(1)). Since
      p_{s+2}/p_s = 1 + (d_s+d_{s+1})/p_s, and d_s+d_{s+1} = O(log^2 p_s) (or even just o(p_s)),
      rho(s) <= 1 + O(d * (d_s+d_{s+1})/p_s).

 (Q2) Need R(s) = g_{s+1}^2/(g_s g_{s+2}) to exceed rho(s). With g_l ~ f'(p_l) d_l,
      R(s) ~ (f'(p_{s+1})^2)/(f'(p_s)f'(p_{s+2})) * d_{s+1}^2/(d_s d_{s+2}).
      The f' factor -> 1. So R(s) ~ d_{s+1}^2/(d_s d_{s+2}) =: Rg(s) (pure gap ratio).

 THE CLEAN SUFFICIENT INEQUALITY (to be checked it FIRES infinitely / discriminates):
      Rg(s) = d_{s+1}^2/(d_s d_{s+2})  >  rho(s) [~1].
   Since rho(s)->1, suffices: limsup Rg(s) > 1. Even better, EXISTS s with d_{s+1}^2 > d_s d_{s+2}
   AND the f'-correction + rho all under control. Numerically rho->1 fast and Rg>=4 happens at
   every (2,>=4,2) gap window which recur (e.g. around primes with small-large-small gaps).

DISCRIMINATION CHECK (must FAIL for AP, HOLD for primes):
   AP gaps constant => Rg(s)=1 for all s, and rho(s)>1 => Rg<rho ALWAYS => never fires. GOOD.
   Primes: Rg(s)=d_{s+1}^2/(d_s d_{s+2}); compute limsup and the "margin" Rg(s)-rho(s).

Let me compute, for f=p and f=p^2+1, the actual margin g_{s+1}^2 - rho(s) g_s g_{s+2} (exact,
should be >0 at fired s), AND the pure prime-gap quantity d_{s+1}^2 - d_s d_{s+2}, to show the
prime-gap log-concavity is what drives it. Also measure rho(s)-1 vs (R(s)-1) scale.
"""
from sympy import primerange
from fractions import Fraction

P=list(primerange(2,5000000))
def gap(l): return P[l]-P[l-1]

def study(ff,name,smax=200000):
    def c(l): return ff(P[l-1])
    # find all fired s; among them record min over s>=1000 of (R(s)-rho(s)) and rho(s)-1
    minmargin=None; firecount=0; firecount_large_s=0
    # Also: does EVERY (small,large,small) gap window with d_{s+1}>=2 max(d_s,d_{s+2}) fire for s large?
    fire_at_strong_localmax=0; strong_localmax=0
    for s in range(1,smax):
        ds,ds1,ds2=gap(s),gap(s+1),gap(s+2)
        g0=c(s+1)-c(s); g1=c(s+2)-c(s+1); g2=c(s+3)-c(s+2)
        lhs=int(g1)**2; rhs_rho=Fraction(int(c(s+2)),int(c(s)))
        R=Fraction(lhs,int(g0*g2))
        fired = R>rho if (rho:=rhs_rho) else False
        if fired:
            firecount+=1
            if s>=1000: firecount_large_s+=1
        # strong gap local max: middle gap >= 2*max(neighbors)
        if ds1>=2*max(ds,ds2):
            strong_localmax+=1
            if fired: fire_at_strong_localmax+=1
    print(f"{name:10s}: fires={firecount} (of {smax}); fires with s>=1000: {firecount_large_s}")
    print(f"            strong gap-local-max windows (d_{{s+1}}>=2max(d_s,d_{{s+2}})): {strong_localmax}; "
          f"of those FIRED: {fire_at_strong_localmax}  (ratio {fire_at_strong_localmax/max(strong_localmax,1):.3f})")

study(lambda p:p,"p",200000)
study(lambda p:p**2+1,"p^2+1",200000)
study(lambda p:p**6+1,"p^6+1",200000)
