"""
Is the literal bridge (i) available? — i.e. does Romik's orthogonal basis diagonalize OUR Weil energy
metric A?  Decided by whether Romik's orthogonality MEASURE equals our Weil archimedean WEIGHT.

  - OUR Weil archimedean weight (the explicit-formula density, what A is built from):
        Omega_inf(r) = Re psi(1/4 + i r/2) - log pi          [the Gamma-factor LOG-DERIVATIVE, param 1/4]
  - ROMIK's Meixner-Pollaczek measure (param 3/4, phi=pi/2, from the abstract P_n^{(3/4)}(x;pi/2)):
        m(r) = |Gamma(3/4 + i r/2)|^2                          [the Gamma-factor MODULUS, param 3/4]
    continuous Hahn p_n(x;3/4,3/4,3/4,3/4):  |Gamma(3/4 + i r/2)|^4.

If Omega_inf is NOT a function of m (different functional AND different parameter), Romik's basis does
NOT diagonalize A, so the literal (i) (substitute his diagonal weights into rho_E) is not available.

We tabulate Omega_inf(r), log m(r), and d/dr log m(r) = -Im psi(3/4+ir/2)*(...) and show they are three
different functions. (And recall the program-established Sylvester fact: any basis change of the Weil
form is a CONGRUENCE -> preserves inertia/marginality -> no basis can be a conditioning lever anyway.)

No torch. mpmath. Deterministic, fast (digamma/gamma only).
"""
import mpmath as mp
mp.mp.dps = 25

def Omega_inf(r):                       # Weil archimedean density (what our metric A carries)
    return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)
def logm(r):                            # log of Romik's MP measure |Gamma(3/4+ir/2)|^2
    return 2*mp.re(mp.loggamma(mp.mpf(3)/4 + 1j*r/2))
def dlogm(r):                           # d/dr log m = -Im psi(3/4+ir/2)
    return mp.re(-1j*mp.digamma(mp.mpf(3)/4 + 1j*r/2))   # = derivative wrt r of 2 Re logGamma(3/4+ir/2)

print("=" * 82)
print("Does Romik's basis diagonalize our Weil energy metric A?  (decides if literal (i) is available)")
print("=" * 82)
print(f"\n  {'r':>6} {'Omega_inf(r) [Weil A]':>22} {'log m(r) [Romik |G(3/4)|^2]':>28} {'d/dr log m(r)':>16}")
for r in [0.5, 2.0, 6.283, 14.135, 30.0, 60.0]:
    r = mp.mpf(r)
    print(f"  {mp.nstr(r,5):>6} {mp.nstr(Omega_inf(r),8):>22} {mp.nstr(logm(r),8):>28} {mp.nstr(dlogm(r),8):>16}")

# are they functionally equal / proportional? check correlation of Omega_inf vs the two m-derived fns
import statistics
rs = [mp.mpf(x) for x in (1,2,3,5,8,12,18,25,35,50)]
O  = [Omega_inf(r) for r in rs]
Lm = [logm(r) for r in rs]
Dm = [dlogm(r) for r in rs]
def corr(a, b):
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    num = sum((x-ma)*(y-mb) for x,y in zip(a,b))
    da = mp.sqrt(sum((x-ma)**2 for x in a)); db = mp.sqrt(sum((y-mb)**2 for y in b))
    return num/(da*db)
print(f"\n  Pearson corr(Omega_inf, log m)      = {mp.nstr(corr(O,Lm),5)}")
print(f"  Pearson corr(Omega_inf, d/dr log m) = {mp.nstr(corr(O,Dm),5)}")
print(f"  Omega_inf grows ~ log(r/2pi) (=arch density); log m ~ -(pi/2)r + (3/2-... ) log r (Stirling, decays).")

print("\n" + "=" * 82)
print("""VERDICT on (i) — the literal bridge is NOT available, for two independent reasons:
  1. DIFFERENT ARCHIMEDEAN FUNCTIONALS. Our Weil metric A is weighted by Omega_inf = Re psi(1/4+ir/2)
     - log pi (the Gamma-factor LOG-DERIVATIVE, density, param 1/4); it GROWS like log(r/2pi). Romik's
     basis is orthogonal w.r.t. m = |Gamma(3/4+ir/2)|^2 (the Gamma-factor MODULUS, param 3/4); log m
     DECAYS like -(pi/2)|r|. They are not the same function (corr above), not proportional, different
     parameter (1/4 vs 3/4). So Romik's orthogonal polynomials do NOT diagonalize A — there is no
     explicit diagonal of A to substitute his c_2n/d_2n into. (The abstract confirms Romik connects to
     real-rootedness + de Bruijn-Newman, NOT the Weil form / any quadratic-form positivity.)
  2. EVEN IF IT DID: a basis change of the Weil form is a CONGRUENCE, which by Sylvester's law preserves
     inertia (the RH content) and cannot cure the marginal conditioning — the program already established
     this (master-state: marginality is gauge/encoding-invariant; the signature is the invariant). So no
     basis is a lever for the energy contraction.
  => (i) is a DEAD direction, and that is a useful negative: Romik's contribution to our program is NOT a
     basis trick for the energy form. It is (a) the free/location confirmation (positivity from Phi>0,
     already done), and (b) the genuinely forward item — his NEW de Bruijn-Newman-type DEFORMATIONS of Xi
     (Poisson kernel on the MP/cH expansions), whose real-zero-preservation the abstract leaves OPEN.
""")
print("=" * 82)
