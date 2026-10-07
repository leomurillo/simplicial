"""
(a) DEFORMATION THREAD — step 2: build Romik's Poisson-kernel deformation of Xi in each basis and test
whether the zeros stay REAL as the deformation parameter alpha varies.

Poisson deformation in basis {B_2k}:  Xi_alpha(t) = sum_k w_k alpha^{2k} B_2k(t).   alpha=1 gives Xi.
  - TAYLOR  (B_2k = t^2k):  Xi_alpha = sum (-1)^k a_2k alpha^2k t^2k = Xi(alpha t)  -- pure SCALING,
    trivially real-zero-preserving (control #1: must show ALL real for all alpha).
  - HERMITE (B_2k = H_2k):  the Poisson/Mehler kernel = the de Bruijn-Newman HEAT FLOW (control #2:
    must show the known behaviour -- smoothing keeps real, the backward direction creates complex pairs
    since Lambda >= 0).
  - MEIXNER-POLLACZEK (B_2k = P_2k(t/2), Romik's NEW expansion): the open question -- does its Poisson
    deformation preserve real zeros, and is there a tractable monotone?

We truncate at k<=K (degree 2K poly), find all roots, and report: # real roots, and the imaginary part
of the lowest off-real root (the 'physical' low roots approximate Xi's first zeros). The Taylor & Hermite
controls calibrate the truncation; the MP row is the result.

Coefficients: a_2k via the Phi-moment integral; b_2k (Hermite) via the monomial->Hermite connection;
gamma_2k (= coeff of P_2k, validated in probe_romik_mp_coeffs) hardcoded. No torch. mpmath.
"""
import mpmath as mp
mp.mp.dps = 30
K = 7                                        # k = 0..7  -> degree 14 polynomials

# ---- coefficients ----
def Phi(u):
    tot = mp.mpf(0); e2u = mp.e**(2*u); e92 = mp.e**(mp.mpf(9)*u/2); e52 = mp.e**(mp.mpf(5)*u/2)
    for n in range(1, 30):
        ex = mp.pi*n*n*e2u
        if ex > 60: break
        tot += (2*mp.pi**2*n**4*e92 - 3*mp.pi*n**2*e52)*mp.e**(-ex)
    return tot
a = [2*mp.quad(lambda u: Phi(u)*u**(2*k), [0, 1, 2, 3])/mp.factorial(2*k) for k in range(K+1)]   # a_2k>0
# Hermite b_2j via connection b_2j = (-1)^j sum_{m>=j} (-1)^m a_2m (2m)!/(2^2m (m-j)!(2j)!)
b = [(-1)**j*mp.fsum((-1)**m*a[m]*mp.factorial(2*m)/(2**(2*m)*mp.factorial(m-j)*mp.factorial(2*j))
                     for m in range(j, K+1)) for j in range(K+1)]
# MP coeff of P_2k (validated in probe_romik_mp_coeffs): gamma_2k = (-1)^k c_2k
gamma = [mp.mpf(s) for s in ['0.480990006','-0.0194182172','0.00203194489','-0.000314086649',
         '6.13031011e-5','-1.40530715e-5','3.6321932e-6','-1.03143947e-6']]

# ---- polynomial basis coefficient arrays (index = power of t) ----
def pad(c, deg): return c + [mp.mpf(0)]*(deg+1-len(c))
def herm(n):                                 # H_n(t) coeffs
    H = [[mp.mpf(1)], [mp.mpf(0), mp.mpf(2)]]
    for k in range(1, n):
        nx = [mp.mpf(0)] + [2*x for x in H[k]]                       # 2t H_k
        nx = pad(nx, k+1)
        for i,x in enumerate(H[k-1]): nx[i] -= 2*k*x                 # -2k H_{k-1}
        H.append(nx)
    return H[n]
def mp_poly(n):                              # P_n^{(3/4)}(t/2) coeffs in t: P_{n+1}=(t P_n-(n+1/2)P_{n-1})/(n+1)
    P = [[mp.mpf(1)], [mp.mpf(0), mp.mpf(1)]]                        # P_0=1, P_1 = t (=2*(t/2))
    for k in range(1, n):
        tP = [mp.mpf(0)] + P[k]                                      # t * P_k
        tP = pad(tP, k+1)
        for i,x in enumerate(P[k-1]): tP[i] -= (k + mp.mpf(1)/2)*x
        P.append([x/(k+1) for x in tP])
    return P[n]

def build(coeffs, basis):                    # Xi_alpha(t)=sum_k coeffs[k] alpha^2k basis(2k)(t)
    def poly(alpha):
        deg = 2*K; arr = [mp.mpf(0)]*(deg+1)
        for k in range(K+1):
            bc = pad(basis(2*k), deg)
            w = coeffs[k]*alpha**(2*k)
            for i in range(deg+1): arr[i] += w*bc[i]
        return arr
    return poly

taylor_sign = [(-1)**k*a[k] for k in range(K+1)]      # coeff of t^2k in Xi
herm_sign   = [(-1)**k*b[k] for k in range(K+1)]      # coeff of H_2k in Xi
mp_sign     = gamma                                   # coeff of P_2k(t/2) in Xi
builders = {
    'Taylor (=scaling, control)':  build(taylor_sign, lambda n: [mp.mpf(1) if i==n else mp.mpf(0) for i in range(n+1)]),
    'Hermite (=de Bruijn-Newman)': build(herm_sign, herm),
    'Meixner-Pollaczek (NEW)':     build(mp_sign, mp_poly),
}

print("=" * 88)
print("Romik's Poisson deformations of Xi: do the zeros stay real as alpha varies?")
print("=" * 88)
print("  (alpha=1 is Xi; we report # real roots / total, and Im of the lowest |t|<30 off-real root)")
for name, poly in builders.items():
    print(f"\n  {name}:")
    print(f"    {'alpha':>7} {'#real/total':>14} {'lowest |t|<30 |Im|':>20}")
    for alpha in [mp.mpf(s) for s in ('0.7','0.85','1.0','1.15','1.3')]:
        arr = poly(alpha)
        roots = mp.polyroots(arr[::-1], maxsteps=200, extraprec=80)
        nreal = sum(1 for r in roots if abs(mp.im(r)) < mp.mpf(10)**(-6))
        low = [r for r in roots if abs(mp.re(r)) < 30 and abs(mp.im(r)) >= mp.mpf(10)**(-6)]
        loIm = min((abs(mp.im(r)) for r in low), default=mp.mpf(0))
        print(f"    {mp.nstr(alpha,3):>7} {f'{nreal}/{len(roots)}':>14} {mp.nstr(loIm,5):>20}")

print("\n" + "=" * 88)
print("""READING:
  * Taylor row = pure scaling Xi(alpha t): all roots real for every alpha (sanity: truncation is benign).
  * Hermite row = de Bruijn-Newman: calibrates how the truncated test renders the known heat-flow
    behaviour (real on the smoothing side; complex pairs appear on the backward side, Lambda>=0).
  * Meixner-Pollaczek row = Romik's NEW deformation: compare to the Hermite control. If the low (physical)
    roots stay real on the same side and go complex on the other, it is a de Bruijn-Newman-type flow with
    its OWN constant; if it stays real on BOTH sides or breaks differently, it is a genuinely different
    object -- the thing worth a monotone hunt.
""")
print("=" * 88)
