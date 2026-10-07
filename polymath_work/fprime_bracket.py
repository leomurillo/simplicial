"""
RIGOROUS control of the f'-bracket and rho, completing the reduction
R(s) > rho(s)  <==  a_{s+1}^2 > (1+delta) a_s a_{s+2}  (for s large, suitable delta).

Setup: f monic real poly, deg d>=1. There is X0 with f, f' >0 and f' nondecreasing on [X0,oo)
(true: f'(x)=d x^{d-1}+... ~ d x^{d-1}>0 increasing for large x). Work with s large so
p_s>=X0. a_l:=d_l=p_{l+1}-p_l. Let a=p_s<b=p_{s+1}<c=p_{s+2}<e=p_{s+3}.

g_s=f(b)-f(a)=f'(x1)(b-a)=f'(x1)a_s,  x1 in (a,b).
g_{s+1}=f'(x2)a_{s+1}, x2 in (b,c).  g_{s+2}=f'(x3)a_{s+2}, x3 in (c,e).
x1<x2<x3, all in [a,e], e-a = a_s+a_{s+1}+a_{s+2} =: W (the window width).

R(s) = g_{s+1}^2/(g_s g_{s+2}) = [f'(x2)^2/(f'(x1)f'(x3))] * a_{s+1}^2/(a_s a_{s+2}).
Bracket B := f'(x2)^2/(f'(x1)f'(x3)).
Since f' nondecreasing and x1<x2<x3: f'(x1)<=f'(x2)<=f'(x3). So
   B = f'(x2)/f'(x1) * f'(x2)/f'(x3) ; first factor>=1, second<=1.
Lower bound B: f'(x2)/f'(x3) >= f'(a)/f'(e) (since x2>=a, x3<=e, f' incr => f'(x2)>=f'(a),
   f'(x3)<=f'(e)). And f'(x2)/f'(x1)>=1. So B >= f'(a)/f'(e).
Now f'(e)/f'(a): e=a+W, W=o(a) (gaps tiny vs a). f' monic-ish deg d-1:
   f'(e)/f'(a) = (e/a)^{d-1}(1+o(1)) = (1+W/a)^{d-1}(1+o(1)) = 1 + O((d-1)W/a) -> 1.
So B >= 1 - O(W/a) -> 1.    [B>=1-eps for s large]

rho(s)=f(c)/f(a). f(c)-f(a)=f'(y)(c-a), y in (a,c), c-a=a_s+a_{s+1}<=W.
   rho(s)-1 = f'(y)(c-a)/f(a) <= f'(e) W / f(a).
   f'(e)/f(a): f'~d x^{d-1}, f~x^d => f'(e)/f(a) ~ d e^{d-1}/a^d ~ d/a (since e~a). So
   rho(s)-1 <= 2 d W/a (for s large).    [rho<=1+O(W/a) -> 1]

So for s large: R(s) >= (1-eps) a_{s+1}^2/(a_s a_{s+2}) and rho(s) <= 1+eps, eps=O(W/a)->0.
If a_{s+1}^2 > (1+delta) a_s a_{s+2} with delta FIXED, then
   R(s) >= (1-eps)(1+delta) and we need this > 1+eps, i.e. (1-eps)(1+delta)>1+eps,
   i.e. delta > 2eps/(1-eps) -> 0. So for s large enough (eps< delta/4, say), R(s)>rho(s). FIRES.

The ONLY thing to ensure: the i.o. windows from (TwoSidedWeak) have eps=O(W_s/p_s)->0 along them.
W_s = a_s+a_{s+1}+a_{s+2} = sum of three prime gaps near p_s = O(log^2 p_s) (or even o(p_s) by
trivial p_{n+1}-p_n=o(p_n)). So eps->0 along ALL large s. GOOD. So every large (TwoSidedWeak)
window fires.   <<< PROOF COMPLETE for general monic f >>>

NUMERICAL CONFIRMATION: pick the (TwoSidedWeak, delta=1) windows at LARGE s and verify ALL fire,
for several f incl high degree and big constant. (delta=1 => ratio>2, eps tiny at large s.)
"""
from sympy import primerange
from fractions import Fraction
P=list(primerange(2,5000000))
def a(m): return P[m]-P[m-1]
def fires(ff,s):
    def c(l): return ff(P[l-1])
    g0=c(s+1)-c(s); g1=c(s+2)-c(s+1); g2=c(s+3)-c(s+2)
    return c(s)*int(g1)**2 > c(s+2)*g0*g2

tests=[("p",lambda p:p),("p+10^6",lambda p:p+10**6),("p^2+1",lambda p:p**2+1),
       ("p^3-p+5",lambda p:p**3-p+5),("p^6+1",lambda p:p**6+1),("p^10+1",lambda p:p**10+1),
       ("p^15+7",lambda p:p**15+7)]
S_LO=10000; S_HI=len(P)-100
for name,ff in tests:
    tot=0; bad=0; firstbad=None
    for s in range(S_LO,S_HI):
        if a(s+1)**2 > 2*a(s)*a(s+2):   # delta=1
            tot+=1
            if not fires(ff,s):
                bad+=1
                if firstbad is None: firstbad=(s,(a(s),a(s+1),a(s+2)))
    print(f"{name:12s}: delta=1 windows in [{S_LO},{S_HI}): total={tot}, NON-firing={bad}"
          + (f"  firstbad={firstbad}" if bad else "  -> ALL FIRE"))
