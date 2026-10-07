"""
(a) DEFORMATION THREAD — step 1: reproduce Romik's Meixner-Pollaczek expansion coefficients of Xi by
direct projection, and validate against his two theorems (alternating-sign positivity + asymptotic
c_2n ~ A sqrt(n) e^{-4 sqrt(pi) sqrt(n)}).  This confirms the MP machinery before we build the new
deformation and test real-zero preservation.

Symmetric Meixner-Pollaczek P_n^{(3/4)}(x; pi/2): recurrence (Koekoek-Swarttouw, phi=pi/2, lambda=3/4)
   (n+1)P_{n+1}(x) = 2x P_n(x) - (n + 2*lambda - 1) P_{n-1}(x),   P_0=1, P_1=2x,  leading coeff 2^n/n!.
Orthogonal w.r.t. w(x)=|Gamma(3/4+ix)|^2 with CLOSED-FORM norm (Koekoek):
   h_n = int P_n^2 w dx = 2*pi * Gamma(n+3/2) / (n! * 2^{3/2}).
Expansion of Xi(t)=Xi(2x) in this basis:  gamma_n = (1/h_n) int_{-inf}^{inf} Xi(2x) P_n(x) w(x) dx.
(Romik writes Xi=sum (-1)^n c_2n f_2n(t/2) with f_2n=(-i)^{2n} P_2n=(-1)^n P_2n, so the coefficient of the
real polynomial P_2n is exactly c_2n>0 — i.e. gamma_2n should be POSITIVE, all n.)

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 22
LAM = mp.mpf(3)/4

def xi(s): return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def Xi(t): return mp.re(xi(mp.mpf(1)/2 + 1j*mp.mpf(t)))
def Pmp(n, x):                              # symmetric MP P_n^{(3/4)}(x;pi/2)
    if n == 0: return mp.mpf(1)
    p0, p1 = mp.mpf(1), 2*x
    for k in range(1, n):
        p0, p1 = p1, (2*x*p1 - (k + 2*LAM - 1)*p0)/(k+1)
    return p1
def wmp(x): return mp.re(mp.gamma(LAM + 1j*x)*mp.gamma(LAM - 1j*x))   # |Gamma(3/4+ix)|^2
def hnorm(n): return 2*mp.pi*mp.gamma(n + 2*LAM)/(mp.factorial(n)*2**(2*LAM))

print("=" * 82)
print("Reproducing Romik's Meixner-Pollaczek coefficients of Xi (validate before deforming)")
print("=" * 82)

# sanity: h_0 closed form vs direct integral of the weight
h0_int = mp.quad(wmp, [-12, -2, 0, 2, 12])
print(f"\n  norm check: h_0 (closed form) = {mp.nstr(hnorm(0),8)} ;  ∫|Γ(3/4+ix)|^2 dx = {mp.nstr(h0_int,8)} ;  "
      f"{'MATCH' if abs(hnorm(0)-h0_int)<mp.mpf(10)**(-6) else 'MISMATCH'}")

print(f"\n  {'n':>3} {'gamma_n = coeff of P_n':>24} {'>0?':>5} {'|gamma_n|/(sqrt(n)e^{-4sqrtpi sqrtn})':>38}")
A_pred = None
rows = []
for n in range(0, 16, 2):                   # even n only (Xi even)
    num = mp.quad(lambda x: Xi(2*x)*Pmp(n, x)*wmp(x), [-14, -5, -1, 0, 1, 5, 14])
    g = num/hnorm(n)
    # Romik asymptotic shape for c_2n (n here = 2*(our index)); use n directly as Romik's 2n index:
    k = n//2                                # Romik's c_{2k}; asymptotic in k: ~ sqrt(k) e^{-4 sqrt(pi) sqrt(k)}
    shape = mp.sqrt(k)*mp.e**(-4*mp.sqrt(mp.pi)*mp.sqrt(k)) if k >= 1 else mp.mpf('nan')
    ratio = abs(g)/shape if k >= 1 else mp.mpf('nan')
    rows.append((n, g, ratio))
    print(f"   {n:>3} {mp.nstr(g,9):>24} {str(g>0):>5} {mp.nstr(ratio,6):>38}")

allpos = all(g > 0 for _, g, _ in rows)
ratios = [r for _, _, r in rows if not mp.isnan(r)]
stable = (max(ratios)/min(ratios) < 5) if len(ratios) >= 3 else False
print(f"\n  all gamma_n > 0 (Romik alternating-sign positivity, our normalization): {allpos}")
print(f"  |gamma_n| / (sqrt(k) e^{{-4 sqrt(pi) sqrt(k)}}) ~ const (ratio spread {mp.nstr(max(ratios)/min(ratios),3)}): "
      f"{'YES -> asymptotic shape confirmed' if stable else 'rough (need larger n / A constant)'}")
print("""
  => If positivity holds and the e^{-4 sqrt(pi) sqrt(n)} shape is reproduced, the MP machinery is correct
     and we have Romik's c_2n. NEXT (step 2): build the deformation Xi_alpha(t)=sum gamma_n alpha^n P_n(t/2)
     (Poisson kernel) and test whether its zeros stay real as alpha varies — with the Hermite/de Bruijn-
     Newman case as the validated control.""")
print("=" * 82)
