"""
(a) DEFORMATION THREAD — step 2 (valid test): the polyroots test was invalid (low-degree truncation
makes spurious complex roots — the Taylor control, = pure scaling Xi(alpha t), wrongly showed non-real
roots). FIX: count REAL-AXIS SIGN CHANGES of Xi_alpha(t) directly (immune to spurious complex roots),
with enough coefficients (k<=12) to resolve the first ~3 zeros (14.13, 21.02, 25.01).

Xi_alpha(t) = sum_{k=0}^{K} w_k alpha^{2k} B_2k(t),  alpha=1 -> Xi.
  Taylor  B=t^2k    -> Xi_trunc(alpha t)  (scaling; sign-change count must stay = #zeros in [0, 24] all real)
  Hermite B=H_2k    -> de Bruijn-Newman heat flow (control)
  MP      B=P_2k(t/2) (Romik NEW)
A deformation BREAKS real-rootedness when two real zeros COLLIDE -> the sign-change count DROPS by 2.

No torch. mpmath. MP coefficients computed by projection (closed-form norm). Deterministic.
"""
import mpmath as mp
mp.mp.dps = 25
LAM = mp.mpf(3)/4; K = 12

def xi(s): return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def Xi(t): return mp.re(xi(mp.mpf(1)/2 + 1j*mp.mpf(t)))
def Phi(u):
    tot = mp.mpf(0); e2u = mp.e**(2*u); e92 = mp.e**(mp.mpf(9)*u/2); e52 = mp.e**(mp.mpf(5)*u/2)
    for n in range(1, 30):
        ex = mp.pi*n*n*e2u
        if ex > 60: break
        tot += (2*mp.pi**2*n**4*e92 - 3*mp.pi*n**2*e52)*mp.e**(-ex)
    return tot
def Pmp(n, x):
    if n == 0: return mp.mpf(1)
    p0, p1 = mp.mpf(1), 2*x
    for k in range(1, n): p0, p1 = p1, (2*x*p1 - (k + 2*LAM - 1)*p0)/(k+1)
    return p1
def wmp(x): return mp.re(mp.gamma(LAM + 1j*x)*mp.gamma(LAM - 1j*x))
def hnorm(n): return 2*mp.pi*mp.gamma(n + 2*LAM)/(mp.factorial(n)*2**(2*LAM))
def Hev(n, t):                               # H_n(t)
    if n == 0: return mp.mpf(1)
    h0, h1 = mp.mpf(1), 2*t
    for k in range(1, n): h0, h1 = h1, 2*t*h1 - 2*k*h0
    return h1

print("computing coefficients (a, b, gamma) for k=0..%d ..." % K)
a = [2*mp.quad(lambda u: Phi(u)*u**(2*k), [0,1,2,3])/mp.factorial(2*k) for k in range(K+1)]
b = [(-1)**j*mp.fsum((-1)**m*a[m]*mp.factorial(2*m)/(2**(2*m)*mp.factorial(m-j)*mp.factorial(2*j))
                     for m in range(j, K+1)) for j in range(K+1)]
gamma = [mp.quad(lambda x: Xi(2*x)*Pmp(2*k, x)*wmp(x), [-16,-6,-1,0,1,6,16])/hnorm(2*k) for k in range(K+1)]

def Xi_alpha(coeffs, kind, alpha, t):
    s = mp.mpf(0)
    for k in range(K+1):
        if kind == 'taylor': B = t**(2*k)*(-1)**k
        elif kind == 'hermite': B = Hev(2*k, t)*(-1)**k
        else: B = Pmp(2*k, t/2)
        s += coeffs[k]*alpha**(2*k)*B
    return s
def sign_changes(coeffs, kind, alpha, lo, hi, step):
    ts = mp.arange(lo, hi, step); prev = None; cnt = 0; vals = []
    for t in ts:
        v = Xi_alpha(coeffs, kind, alpha, t); vals.append(v)
        if prev is not None and prev*v < 0: cnt += 1
        prev = v
    return cnt

bases = {'Taylor (=scaling, control)': (a, 'taylor'),
         'Hermite (=de Bruijn-Newman)': (b, 'hermite'),
         'Meixner-Pollaczek (NEW)': (gamma, 'mp')}
LO, HI, ST = mp.mpf('6'), mp.mpf('27'), mp.mpf('0.2')
print("=" * 80)
print(f"Sign changes of Xi_alpha(t) on [{LO},{HI}] (true Xi has zeros 14.13, 21.02, 25.01 -> 3 here)")
print("=" * 80)
print(f"\n  {'basis':<30} " + " ".join(f"a={mp.nstr(al,3):>5}" for al in ('0.7','0.85','1.0','1.15','1.3')))
for name,(co,kind) in bases.items():
    counts = [sign_changes(co, kind, mp.mpf(al), LO, HI, ST) for al in ('0.7','0.85','1.0','1.15','1.3')]
    print(f"  {name:<30} " + " ".join(f"{c:>7}" for c in counts))
print(f"\n  (alpha=1 column should read 3 for a faithful truncation; a DROP of 2 as alpha moves = a real")
print(f"   zero-pair COLLISION = real-rootedness broken on that side.)")
print("=" * 80)
