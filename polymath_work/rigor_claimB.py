"""
RIGOROUS Claim B:  g_{l+1}^2 > g_l g_{l+2}  for infinitely many l.
(i.e., the f-gap sequence g_l = f(p_{l+1})-f(p_l) is NOT eventually log-convex.)

PROOF (clean):
 Suppose, for contradiction, that there is L with g_{l+1}^2 <= g_l g_{l+2} for ALL l>=L.
 Equivalently t_l := g_{l+1}/g_l satisfies t_{l+1} >= t_l for all l>=L  (ratios nondecreasing),
   because g_{l+1}^2 <= g_l g_{l+2}  <=>  g_{l+1}/g_l <= g_{l+2}/g_{l+1}  <=> t_l <= t_{l+1}.
 So (t_l)_{l>=L} is nondecreasing, hence has a limit T in (0, +oo].

 FACT 1: g_l -> +oo. Indeed for monic f of degree d>=1, f is increasing for x>=X0, and
   g_l = f(p_{l+1})-f(p_l) >= (p_{l+1}-p_l) * min_{[p_l,p_{l+1}]} f'  >= 1 * f'(p_l) -> +oo,
   since f'(x) -> +oo (deg d-1>=0; if d=1, f'=1>0 constant and g_l=f(p_{l+1})-f(p_l)=
   p_{l+1}-p_l which has limsup +oo by prime gaps -> need care for d=1; see FACT 1').
   For d>=2: f'(p_l) ~ d p_l^{d-1} -> oo so g_l -> oo.
 FACT 1' (d=1, f=p+c): g_l = p_{l+1}-p_l = prime gap; limsup = +oo (Westzynthius), and more
   simply g_l is unbounded. (We only need limsup g_l=+oo, which is classical & unconditional.)

 CASE T>1: then t_l>=t_L'>1 for large l, so g_l grows at least geometrically:
   g_{l} >= g_{L'} * (t_{L'})^{l-L'} >= C * r^l, r>1. Then f(p_{l+1}) >= g_l + ... >= C r^l,
   exponential in l. But f(p_{l+1}) <= 2 p_{l+1}^d (for large p, monic) and p_{l+1} = O(l log l)
   (PNT / Chebyshev), so f(p_{l+1}) = O((l log l)^d) = polynomial in l. Exponential <= polynomial
   is false for large l. CONTRADICTION.

 CASE T<=1: t_l nondecreasing with limit <=1 => t_l<=1 for all l>=L => g_{l+1}<=g_l for l>=L
   => (g_l) eventually nonincreasing => bounded above => contradicts g_l -> +oo (FACT 1/1').
   CONTRADICTION.

 Both cases contradict. Hence no such L: g_{l+1}^2 > g_l g_{l+2} infinitely often.  QED Claim B (R(s)>1 i.o.)

NOTE: This gives R(s)>1 i.o. We separately need R(s)>rho(s). Since rho(s)->1, "R>1 i.o." is
NOT immediately enough (could have R=1.0001<rho=1.0002). The QUANTITATIVE upgrade is below.

Let me NUMERICALLY CONFIRM the proof's mechanism:
 (i) g_l -> oo,  (ii) ratios t_l NOT eventually nondecreasing (drops happen i.o.),
 (iii) at the drops, R(s)=1/( (t_s)(... )) ... let me just confirm g_{l+1}^2>g_l g_{l+2} i.o.
"""
from sympy import primerange
from fractions import Fraction

P=list(primerange(2,3000000))
def test(ff,name,smax=50000):
    def c(l): return ff(P[l-1])
    g=[c(l+1)-c(l) for l in range(1,smax+5)]  # g[0]=g_1
    # count l with g_{l+1}^2 > g_l g_{l+2}, i.e. index i: g[i]^2>g[i-1]*g[i+1] (1-indexed g_l=g[l-1])
    cntlc=0; last=None
    for i in range(1,smax):  # g_l with l=i+1 in middle: g[i]^2 > g[i-1]*g[i+1]
        if g[i]**2 > g[i-1]*g[i+1]:
            cntlc+=1; last=i+1
    print(f"{name:10s}: g_l grows {int(g[0])}->{int(g[smax])} ; "
          f"#{{l<= {smax}: g_l^2>g_{{l-1}}g_{{l+1}}}}={cntlc} (frac {cntlc/smax:.3f}); last such l={last}")

for nm,ff in [("p",lambda p:p),("p+10^6",lambda p:p+10**6),("p^2+1",lambda p:p**2+1),
              ("p^5+1",lambda p:p**5+1),("p^12+1",lambda p:p**12+1)]:
    test(ff,nm,50000)
