"""
(a) DEFORMATION THREAD — the decisive test: track the ACTUAL zero positions of Romik's MP deformation
Xi_alpha(t) = sum_{k=0}^{K} gamma_2k alpha^{2k} P_2k(t/2)  through a fine alpha-sweep, and decide:

  - if two adjacent real zeros' gap closes to ~0 and the real-root count drops by 2 while the merge point
    is INTERIOR -> a COLLISION -> the pair goes COMPLEX -> real-rootedness BROKEN (a de Bruijn-Newman-type
    flow with its own constant);
  - if a root simply leaves the window (reaches a boundary) -> window-exit, NOT a collision (inconclusive
    for that root, real-rootedness not broken there).

At any alpha where the count drops via a suspected collision, we directly chase the COMPLEX root (findroot
with a complex start near the merge) and report its imaginary part.

K=12 resolves Xi's first 3 zeros (14.13, 21.02, 25.01). No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25
LAM = mp.mpf(3)/4; K = 12

def xi(s): return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def Xi(t): return mp.re(xi(mp.mpf(1)/2 + 1j*mp.mpf(t)))
def Pmp(n, x):                               # MP P_n^{(3/4)}(x;pi/2), complex-capable
    if n == 0: return mp.mpf(1)
    p0, p1 = mp.mpf(1), 2*x
    for k in range(1, n): p0, p1 = p1, (2*x*p1 - (k + 2*LAM - 1)*p0)/(k+1)
    return p1
def wmp(x): return mp.re(mp.gamma(LAM + 1j*x)*mp.gamma(LAM - 1j*x))
def hnorm(n): return 2*mp.pi*mp.gamma(n + 2*LAM)/(mp.factorial(n)*2**(2*LAM))

print("computing MP coefficients gamma_2k, k=0..%d ..." % K)
gamma = [mp.quad(lambda x: Xi(2*x)*Pmp(2*k, x)*wmp(x), [-12,-5,-1,0,1,5,12])/hnorm(2*k) for k in range(K+1)]
print("  gamma_2k = " + ", ".join(mp.nstr(g,5) for g in gamma))

def Xa(alpha, t):                            # MP-deformed Xi (complex-capable in t)
    return mp.fsum(gamma[k]*alpha**(2*k)*Pmp(2*k, t/2) for k in range(K+1))

def real_roots(alpha, lo=mp.mpf(9), hi=mp.mpf(29), step=mp.mpf('0.1')):
    roots = []; pt = lo; pv = Xa(alpha, lo); t = lo+step
    while t <= hi:
        v = Xa(alpha, t)
        if pv*v < 0:
            try: roots.append(mp.findroot(lambda x: Xa(alpha, x), (pt+t)/2))
            except Exception: pass
        pt, pv = t, v; t += step
    return sorted(mp.re(r) for r in roots)

print("\n" + "=" * 82)
print("Zero positions of the MP-deformed Xi_alpha(t) in [9,29] vs alpha (true Xi: 14.13, 21.02, 25.01)")
print("=" * 82)
print(f"  {'alpha':>6} {'# real':>7}  real zeros")
prev = None
alphas = [mp.mpf(s) for s in ('1.4','1.3','1.2','1.1','1.05','1.0','0.95','0.9','0.85','0.8','0.75','0.7','0.6')]
data = {}
for al in alphas:
    rr = real_roots(al); data[al] = rr
    print(f"  {mp.nstr(al,3):>6} {len(rr):>7}  " + ", ".join(mp.nstr(r,6) for r in rr))

print("\n  COLLISION ANALYSIS (interior gap closing => complex pair):")
# look for the smallest-gap adjacent pair as alpha decreases, and where count drops
for al in alphas:
    rr = data[al]
    if len(rr) >= 2:
        gaps = [(rr[i+1]-rr[i], (rr[i]+rr[i+1])/2) for i in range(len(rr)-1)]
        g, mid = min(gaps)
        if g < mp.mpf('2.5'):
            print(f"   alpha={mp.nstr(al,3)}: tightest interior gap {mp.nstr(g,3)} near t={mp.nstr(mid,4)} (closing?)")

# at a drop, chase the complex pair: pick an alpha with fewer than 3 roots, start near a plausible merge
print("\n  complex-root chase at reduced-count alphas (Im != 0 confirms a real pair went complex):")
for al in alphas:
    if len(data[al]) < 3:
        for guess in (14+2j, 18+2j, 23+2j, 17+3j):
            try:
                r = mp.findroot(lambda x: Xa(al, x), guess)
                if abs(mp.im(r)) > mp.mpf('0.05') and 8 < mp.re(r) < 30:
                    print(f"   alpha={mp.nstr(al,3)}: COMPLEX root at {mp.nstr(r,6)}  (Im={mp.nstr(mp.im(r),4)})")
                    break
            except Exception: pass
        else:
            print(f"   alpha={mp.nstr(al,3)}: no interior complex root found near guesses (likely window-exit)")
print("=" * 82)
