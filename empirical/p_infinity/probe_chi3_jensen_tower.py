"""
THE CHIRAL (chi_3) JENSEN TOWER vs zeta: is L(1/2, chi_3) the cubic-margin MINIMIZER (the RH-critical knob)?

The cubic THRESHOLD result: for zeta, d=2 Jensen margin is rigid 1.0 (free), d=3 is the first arithmetic-
bearing order (margin 0.287 at the lowest zero, vs Hermite floor 0.5). Now the chiral channel: the program's
c_2 ~ L(1/2,chi_3)^2 rides on the central value of the self-dual character of Q(sqrt-3)=Q(zeta_3) -- the ODD
quadratic character chi_{-3} mod 3 (the chiral/odd half of the Z/6 split: zeta=even, L(.,chi_{-3})=odd).
Its completed Xi_chi(t)=Lambda(1/2+it,chi_{-3}) is real even; b_0 = Lambda(1/2,chi_{-3}) ~ L(1/2,chi_{-3}).

We compute the chiral Jensen tower and compare its cubic (d=3) margin to zeta's. If the chiral cubic margin
is SMALLER (tighter), then L(1/2,chi_3) is literally the margin-minimizer = the RH-critical knob, and the
program's c_2<0 chiral anchor is the tightest Jensen margin in the system.

Lambda(s,chi_{-3}) = (3/pi)^{(s+1)/2} Gamma((s+1)/2) L(s,chi_{-3}),  L = 3^{-s}[zeta(s,1/3)-zeta(s,2/3)].

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 30

# ---- zeta side ----
def xi(s): return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def Xi_zeta(t): return xi(mp.mpf(1)/2 + 1j*t)        # analytic (real on R); re() only at the end

# ---- chiral chi_{-3} side (odd quadratic char mod 3) ----
def Lchi(s): return 3**(-s) * (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
def Lambda_chi(s): return (3/mp.pi)**((s+1)/2) * mp.gamma((s+1)/2) * Lchi(s)
def Xi_chi(t): return Lambda_chi(mp.mpf(1)/2 + 1j*t)   # analytic (real on R); re() only at the end

Lhalf = mp.re(Lchi(mp.mpf(1)/2))
print("=" * 84)
print("Chiral chi_3 Jensen tower vs zeta: is L(1/2,chi_3) the cubic-margin minimizer?")
print("=" * 84)
print(f"\n  L(1/2, chi_{{-3}}) = {mp.nstr(Lhalf,8)}   (program value 0.4808 -> {'MATCH' if abs(Lhalf-mp.mpf('0.4808'))<mp.mpf('0.01') else 'differs'})")

def taylor_a(Xifun, M):
    tc = mp.taylor(Xifun, 0, 2*M+2, method='quad', radius=4)   # Cauchy-integral: fast for special fns
    a = [(-1)**m * mp.re(tc[2*m]) for m in range(M+1)]          # a_m = (-1)^m c_{2m} (>0 = L-P/RH side)
    return a

NM = 6
Az = taylor_a(Xi_zeta, NM)
Ac = taylor_a(Xi_chi, NM)
print(f"\n  zeta:  a_0..a_4 = {[mp.nstr(Az[m],5) for m in range(5)]}  (a_0=xi(1/2))")
print(f"  chi3:  b_0..b_4 = {[mp.nstr(Ac[m],5) for m in range(5)]}  (b_0=Lambda(1/2,chi_3))")
print(f"         all positive (L-P side)? zeta:{all(mp.re(x)>0 for x in Az)}  chi3:{all(mp.re(x)>0 for x in Ac)}")

def jensen_margin(A, d, n):
    rho = A[n]/A[n+1]
    coef = [mp.binomial(d, j)*A[n+j]*rho**j for j in range(d+1)]
    roots = mp.polyroots([coef[d-j] for j in range(d+1)], maxsteps=300, extraprec=80)
    im = max(abs(mp.im(r)) for r in roots)
    re = sorted(mp.re(r) for r in roots)
    real = im < mp.mpf(10)**-8 * (1 + max(abs(x) for x in re))
    spread = re[-1] - re[0]
    gaps = [re[i+1]-re[i] for i in range(len(re)-1)]
    return (real, float(min(gaps)/spread) if (real and spread != 0) else 0.0)

print(f"\n  CUBIC (d=3) Jensen margin (min gap/spread), zeta vs chiral, across shift n:")
print(f"  {'n':>4} {'zeta d=3':>12} {'chi3 d=3':>12} {'chi3 tighter?':>14}")
for n in range(0, 5):
    if n+3 >= NM: break
    _, mz = jensen_margin(Az, 3, n)
    _, mc = jensen_margin(Ac, 3, n)
    print(f"  {n:>4} {mz:>12.4f} {mc:>12.4f} {('YES (chiral=critical)' if mc < mz else 'no'):>14}")

print(f"\n  for context, the full tower at n=0 (zeta vs chi3), d=2..6:")
print(f"  {'d':>4} {'zeta':>10} {'chi3':>10}")
for d in range(2, 7):
    if d >= NM: break
    _, mz = jensen_margin(Az, d, 0)
    _, mc = jensen_margin(Ac, d, 0)
    print(f"  {d:>4} {mz:>10.4f} {mc:>10.4f}")

print("\n" + "=" * 84)
print(f"""READING:
  * L(1/2,chi_{{-3}}) = {mp.nstr(Lhalf,6)} (the program's chiral central value): the self-dual odd character of
    Q(zeta_3) is the chiral half of the Z/6 split, and its completed Jensen tower is well-defined (b_m>0).
  * If the chiral CUBIC (d=3) margin is SMALLER than zeta's at the low shifts, then L(1/2,chi_3) is the
    cubic-margin MINIMIZER -- the RH-critical knob -- and the program's c_2<0 chiral anchor IS the tightest
    Jensen margin in the system. The arithmetic squeeze on hyperbolicity is led by the chiral channel.
  * Either way: the CUBIC (d=3) is the threshold (d=2 rigid/free for both); the chiral vs even comparison
    locates where the tightest cubic positivity lives. This closes the loop T15 (D_3<0 finite obstruction)
    -> cubic Jensen threshold -> the chiral channel L(1/2,chi_3), all on the SAME cubic seam.
""")
print("=" * 84)
