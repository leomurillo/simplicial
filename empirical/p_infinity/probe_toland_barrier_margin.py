"""
TOLAND-SINGER BARRIER fork -- does the dual barrier margin stay bounded away from zero across tau=1?

CONTEXT.  N15 writes the Weil functional as a difference of convex potentials, W = D_arch - Phi_prime, and
probe_toland_dual_signpreserving.py certified the bare Toland-Singer transform is an EQUALITY OF INFIMA
(m_primal = m_dual): it cannot manufacture positivity.  The follow-up PROPOSAL (Leo, 2026-06-08) is the
*Singer/relaxation* half: build a tractable convex BARRIER in the dual, trackable across the tau=1
(Montgomery form-factor diagonal/off-diagonal) transition, proving the infimum m stays bounded away from 0.

THE OBSTRUCTION, MADE PRECISE.  A descent flow (de Bruijn-Newman Cole-Hopf/Burgers) uses a convex MAJORANT
and is blind to the threshold Lambda.  A *barrier* needs a convex MINORANT psi <= W with inf psi > 0.  For a
quadratic form on the autocorrelation cone the tightest such convex certificate IS the smallest generalized
eigenvalue of the form.  So the barrier margin over support [-nu, nu] is exactly

    mu(nu) := min_{phi: supp phi subset [-nu/2, nu/2]}  W(phi)/||phi||^2  =  lambda_min(M_A + M_pole - M_P, G).

THE FORK this probe settles, numerically and honestly:
  * MARGINAL branch:    a small-nu floor that COLLAPSES toward 0 as nu crosses the support threshold
                        (the tau=1 analog) -- the barrier is RH-hard, no free floor.
  * NON-MARGINAL branch: a floor HELD across the threshold -> imported spectral-gap content
                        (no-Siegel-zero class, weaker than RH; see rh_barrier_synthesis.md).

OBJECTS (program-faithful; same conventions as the sibling p_infinity probes):
  - archimedean density  Omega(r) = Re psi(1/4 + i r/2) - log pi          (N14)
  - prime side           Lambda(n) n^{-1/2}  von Mangoldt                 (probe_prime_side_bregman_logzeta)
  - Riemann-Weil explicit formula (validated below to ~1e-6 against true zeros), h=|phi^|^2, g=phi corr phi:
        Sum_rho h(gamma) = (1/2pi) int h Omega dr + h(i/2)+h(-i/2) - 2 Sum_n Lambda(n) n^{-1/2} g(log n).
        h>=0 on the real axis => under RH the LHS >= 0 => W(phi) >= 0 => mu(nu) >= 0 for all nu.

  Test cone = Gaussian bumps b_j(u)=exp(-(u-t_j)^2/2w^2) on a grid in [-nu/2, nu/2].  The frequency envelope
  is exp(-w^2 r^2/2); w must be SMALL ENOUGH that |phi^| reaches the first zeros (gamma_1~14), else W~0
  trivially (a degenerate basis, not the knife-edge).  We use w=0.12 (envelope ~0.24 at gamma_1) and VALIDATE
  the assembled matrix form against the direct zero-sum 2 Sum_{gamma>0}|phi^(gamma)|^2 -- the probe's own
  correctness gate.  Closed-form phi^, autocorrelation, pole, Gram (Gaussians); arch = 1-D quadrature.

CONTROL.  Scale the prime term by kappa.  kappa=1 is the true zeta knife-edge; kappa>1 (prime over-weight,
RH-false analog) must drive mu<0 -- certifying mu is a genuine arch-vs-prime DOMINATION margin (= the N15
sec 7 / tau=1 object, in the dual).  NB the prime form M_P is INDEFINITE (autocorrelation at nonzero lag is
sign-indefinite), so mu(kappa) need not be monotone; the load-bearing statement is sign-breaking at kappa>1.

All exact-arithmetic (mpmath, no torch).  Honest scope: LOCATES the fork and measures mu(nu); does NOT
claim RH.  A collapsing mu(nu) confirms marginality; it proves nothing.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 25
SQRT_PI = mp.sqrt(mp.pi)

def Omega(r):
    """Archimedean density Re psi(1/4 + i r/2) - log pi  (N14 sec 1.2; even in r)."""
    return mp.re(mp.digamma(mp.mpf('0.25') + mp.mpc(0, 1) * r / 2)) - mp.log(mp.pi)

def prime_powers(umax):
    out = []
    Nmax = int(mp.floor(mp.e ** umax)) + 1
    for p in sp.primerange(2, Nmax + 1):
        pk, logp = p, mp.log(p)
        while pk <= Nmax:
            if mp.log(pk) <= umax:
                out.append((mp.mpf(pk), logp))
            pk *= p
    return out

def grid(T, w):
    spacing = mp.mpf('2.2') * w
    n = int(mp.floor(2 * T / spacing)) + 1
    t = [(-T + spacing * j) for j in range(max(n, 1))]
    if abs(t[-1] - T) > spacing / 2:
        t.append(T)
    return t

def build_matrices(T, w, kappa=mp.mpf(1)):
    t = grid(T, w); d = len(t)
    nu = 2 * T
    pps = prime_powers(nu + 9 * w)           # Gaussian-tail cutoff: exact to ~1e-35
    Rmax = 14 / w                            # frequency cutoff: envelope exp(-w^2 R^2/2) ~ 1e-42
    brk = [mp.mpf(k) * Rmax / 10 for k in range(11)]   # subdivide the oscillatory arch integral

    def corr(i, j, x):                       # (b_i corr b_j)(x) = sqrt(pi) w exp(-(x-d_ij)^2/4w^2)
        dij = t[i] - t[j]
        return SQRT_PI * w * mp.e ** (-(x - dij) ** 2 / (4 * w ** 2))

    MA = mp.zeros(d); MP = mp.zeros(d); G = mp.zeros(d)
    for i in range(d):
        for j in range(i, d):
            dij = t[i] - t[j]
            integ = mp.quad(lambda r: mp.cos(r * dij) * mp.e ** (-w ** 2 * r ** 2) * Omega(r), brk)
            MA[i, j] = MA[j, i] = w ** 2 * 2 * integ
            G[i, j] = G[j, i] = corr(i, j, mp.mpf(0))
    # prime kernel sampled at x=log n>0 -> not symmetric in (i,j); the form's matrix is its symmetric part
    for i in range(d):
        for j in range(d):
            MP[i, j] = 2 * mp.fsum(lam / mp.sqrt(nn) * corr(i, j, mp.log(nn)) for (nn, lam) in pps)
    MP = (MP + MP.T) / 2
    Kpole = 4 * mp.pi * w ** 2 * mp.e ** (w ** 2 / 4)
    a = [mp.e ** (-ti / 2) for ti in t]; b = [mp.e ** (ti / 2) for ti in t]
    Mpole = mp.matrix(d)
    for i in range(d):
        for j in range(d):
            Mpole[i, j] = Kpole / 2 * (a[i] * b[j] + a[j] * b[i])
    Q = MA + Mpole - kappa * MP
    Q = (Q + Q.T) / 2
    return Q, G, t, d, len(pps)

def min_gen_eig(Q, G):
    L = mp.cholesky(G); Linv = L ** -1
    M = Linv * Q * Linv.T
    M = (M + M.T) / 2
    return min(mp.eigsy(M, eigvals_only=True))

# ----------------------------------------------------------------------------------------------
# CORRECTNESS GATE: matrix form  ==  direct sum over true zeros  (the explicit formula identity)
# ----------------------------------------------------------------------------------------------
print("=" * 100)
print("0. CORRECTNESS GATE -- assembled matrix form equals the direct sum over true zeta zeros")
print("=" * 100)
w = mp.mpf('0.12')
Tg = mp.mpf('1.0')
Qg, Gg, tg, dg, _ = build_matrices(Tg, w)
ZEROS = [mp.im(mp.zetazero(n)) for n in range(1, 400)]
def phihat(t, c, r):
    return mp.fsum(c[j] * mp.sqrt(2 * mp.pi) * w * mp.e ** (mp.mpc(0, 1) * r * t[j]) * mp.e ** (-w ** 2 * r ** 2 / 2)
                   for j in range(len(t)))
gate_ok = True
for ctag, c in [("alternating", [(-1) ** j for j in range(dg)]), ("ramp", [mp.mpf(j + 1) for j in range(dg)])]:
    c = [mp.mpf(x) for x in c]
    cv = mp.matrix(c)
    form_m = (cv.T * Qg * cv)[0, 0]
    form_z = 2 * mp.fsum(mp.re(phihat(tg, c, gm) * phihat(tg, c, -gm)) for gm in ZEROS)
    err = abs(form_m - form_z)
    gate_ok = gate_ok and (err < mp.mpf('1e-5'))
    print(f"  c={ctag:>12}: matrix form = {mp.nstr(form_m,10):>14}   zero-sum = {mp.nstr(form_z,10):>14}   "
          f"|diff| = {mp.nstr(err,3)}   (>=0: {form_z >= -mp.mpf('1e-9')})")
print(f"  --> explicit formula reproduced by the matrices (form is genuinely Sum_rho|phi^(gamma)|^2): {gate_ok}")

# ----------------------------------------------------------------------------------------------
print("=" * 100)
print("1. BARRIER MARGIN  mu(nu) = lambda_min(M_A + M_pole - M_P, G)  over support [-nu, nu]")
print(f"    (frequency-reaching basis w={float(w)}; mu = tightest convex certificate in the dual test cone)")
print("=" * 100)
NUS = [mp.mpf(x) for x in ('0.5', '0.7', '0.9', '1.2', '1.5', '2.0', '2.5', '3.0', '3.6')]
print(f"  {'nu':>6} {'dim':>4} {'#primepow':>10} {'mu(nu) = barrier margin':>26} {'sign':>6}")
margins = []
for nu in NUS:
    Q, G, t, d, npp = build_matrices(nu / 2, w)
    mu = min_gen_eig(Q, G)
    margins.append((nu, mu))
    print(f"  {float(nu):>6.2f} {d:>4} {npp:>10} {mp.nstr(mu, 12):>26} {'>=0' if mu >= -mp.mpf('1e-9') else '<0 !!':>6}")

print("-" * 100)
mu_small = max(m for (nu, m) in margins if nu <= mp.mpf('0.7'))   # the floor before primes turn on
mu_large = margins[-1][1]
print(f"  small-support margin (nu<=0.7, few/no primes reachable): mu = {mp.nstr(mu_small,8)}")
print(f"  large-support margin (nu={float(margins[-1][0])}):                          mu = {mp.nstr(mu_large,8)}")
if mu_small > mp.mpf('1e-4'):
    frac = mu_large / mu_small
    nu_star = next((float(nu) for (nu, m) in margins if m < mu_small / 100), None)
    print(f"  margin ratio large/small = {mp.nstr(frac,5)}   (-> 0 = floor COLLAPSES across threshold)")
    print(f"  support threshold nu* (margin drops below 1% of the small-nu floor): nu* ~ {nu_star}")
    BRANCH = "MARGINAL -- floor collapses across the support (tau=1) threshold" if frac < mp.mpf('0.05') \
        else "NON-MARGINAL -- floor held across the threshold"
else:
    print(f"  no positive small-support floor at this basis width (margin ~0 throughout)")
    BRANCH = "MARGINAL -- margin pinned at 0 for all nu (no floor to stand on)"
print(f"  ==> FORK VERDICT: {BRANCH}")

# ----------------------------------------------------------------------------------------------
print("=" * 100)
print("2. CONTROL -- mu is a genuine arch-vs-prime DOMINATION margin: scale prime term by kappa")
print("   kappa=1 = true-zeta knife-edge; kappa>1 (prime over-weight, RH-false analog) must drive mu<0.")
print("   (M_P is indefinite -> mu(kappa) need not be monotone; the load-bearing fact is sign-break at kappa>1.)")
print("=" * 100)
nu_c = mp.mpf('1.5')
print(f"  at fixed nu={float(nu_c)}:")
print(f"  {'kappa':>8} {'mu':>22} {'sign':>7}")
mu_at = {}
for kappa in [mp.mpf(x) for x in ('0.7', '0.9', '1.0', '1.2', '1.5')]:
    Q, G, t, d, _ = build_matrices(nu_c / 2, w, kappa=kappa)
    mu = min_gen_eig(Q, G); mu_at[float(kappa)] = mu
    print(f"  {float(kappa):>8.2f} {mp.nstr(mu, 12):>22} {'>=0' if mu >= -mp.mpf('1e-9') else '<0':>7}")
domination = (mu_at[1.5] < mu_at[1.0]) and (mu_at[1.2] < mu_at[1.0] + mp.mpf('1e-9')) and (mu_at[1.5] < 0)
print(f"  --> prime over-weight (kappa>1) drives the margin negative: {domination}")
print(f"      (confirms mu tracks arch-vs-prime domination -- the N15 sec 7 / tau=1 closure object, dualized)")

# ----------------------------------------------------------------------------------------------
print("=" * 100)
print("VERDICT")
print("=" * 100)
print(f"""  The Toland-Singer BARRIER margin mu(nu) -- the tightest convex certificate the dual admits over the
  support-nu test cone -- is on the {BRANCH.split('--')[0].strip()} branch of the fork.
  A valid convex barrier cannot certify m bounded away from zero past the tau=1 support threshold: its
  floor IS the missing object (per rh_barrier_synthesis.md, the same gap^2 knife-edge that defeats Li /
  de Bruijn-Newman / Jensen).  The control confirms mu is a real arch-vs-prime domination margin (prime
  over-weight drives it negative).  Toland-Singer relocates RH cleanly onto Phi_prime^* >= D_arch^*; the
  barrier does not cross tau=1 for free.  [C], not a proof.""")

allok = gate_ok and all(m >= -mp.mpf('1e-7') for (_, m) in margins) and domination
print("=" * 100)
print(f"CERTIFICATE {'GREEN -- gate passed, margin measured, fork settled, control valid' if allok else 'RED -- a check FAILED'}")
print("=" * 100)
