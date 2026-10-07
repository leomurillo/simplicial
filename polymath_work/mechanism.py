"""
MECHANISM of criterion (*): c_s g_{s+1}^2 > c_{s+2} g_s g_{s+2}.
<=> R(s):= g_{s+1}^2/(g_s g_{s+2})  >  rho(s):=c_{s+2}/c_s.

For monic f deg d: c_l=f(p_l). g_l=f(p_{l+1})-f(p_l).
rho(s)=f(p_{s+2})/f(p_s) -> 1 as s->oo (since p_{s+2}/p_s -> 1 and f~x^d => ratio->(p_{s+2}/p_s)^d ->1).
Actually p_{s+2}/p_s -> 1, so rho(s)->1.

So as s->oo, RHS->1. We need R(s)=g_{s+1}^2/(g_s g_{s+2}) to EXCEED ~1 infinitely often.
g_l ~ f'(p_l)*d_l (d_l=prime gap) to leading order, with correction.
R(s) ~ [f'(p_{s+1})^2 d_{s+1}^2] / [f'(p_s) f'(p_{s+2}) d_s d_{s+2}]
     ~ (d_{s+1}^2)/(d_s d_{s+2}) * [f' factors ->1].
So R(s) ~ d_{s+1}^2/(d_s d_{s+2}) = ratio measuring prime-gap LOG-CONCAVITY.

THE CRUX: we need d_{s+1}^2 > d_s d_{s+2} (gap log-concave) to beat rho(s) which ->1.
The prime gaps d_l are HIGHLY irregular. d_{s+1}^2/(d_s d_{s+2}) can be large
(e.g. a big gap flanked by small gaps: d_s=2,d_{s+1}=large,d_{s+2}=2 -> R huge).

KEY DISCRIMINATION vs AP: for AP, gaps constant => R(s)=1 EXACTLY, and rho(s)>1 strictly
=> (*) fails forever. For primes, gaps fluctuate => R(s)>1 happens, and the question is
whether it beats rho(s)-1 (which ->0). Since rho(s)-1 -> 0 but gap fluctuations do NOT die,
(*) should fire. Let me QUANTIFY.

Compute for f=p (worst case, smallest gaps relative): R(s), rho(s), and R-rho at each s,
find where R>rho, and confirm the GAP-RATIO d_{s+1}^2/(d_s d_{s+2}) drives it.
"""
from sympy import primerange, Integer, Rational
from fractions import Fraction

P = list(primerange(2, 100000))

def analyze(ff, name, smax=40):
    def c(l): return ff(P[l-1])
    cv=[None]+[c(l) for l in range(1,smax+5)]
    d =[None]+[P[l]-P[l-1] for l in range(1,smax+4)]  # prime gaps d_l=p_{l+1}-p_l
    g =[None]+[cv[l+1]-cv[l] for l in range(1,smax+4)]
    print(f"--- {name} ---")
    print(f"{'s':>3} {'gaps d_s,d_s+1,d_s+2':>22} {'R=g_{s+1}^2/(g_s g_{s+2})':>26} {'rho=c_{s+2}/c_s':>18} {'(*) fires':>10}")
    fired=False
    for s in range(1, smax+1):
        R = Fraction(int(g[s+1])**2, int(g[s]*g[s+2]))
        rho = Fraction(int(cv[s+2]), int(cv[s]))
        fire = R>rho
        if fire and not fired:
            mark="<== FIRST"
            fired=True
        else:
            mark="*" if fire else ""
        if s<=20 or fire:
            print(f"{s:>3} {str((d[s],d[s+1],d[s+2])):>22} {float(R):>26.6f} {float(rho):>18.6f} {mark:>10}")

analyze(lambda p:p, "f=p (degree 1, c=0)", 20)
print()
analyze(lambda p:p**5+1, "f=p^5+1", 20)
