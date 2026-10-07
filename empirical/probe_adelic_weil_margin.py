"""
PULL LINK 5: the adelic apex Weil form and its margin.

The Weil quadratic form (Bombieri): for real even test g, compact support in
u=log x, with FT  ghat(r)=int g(u)e^{iru}du,

  Q(g) = sum_zeros |ghat(gamma)|^2                                    (spectral side)
       = (1/2pi) int |ghat(r)|^2 * 2 theta'(r) dr      [ARCHIMEDEAN = apex edge/N5]
         + 2 ( int g cosh(u/2) du )^2                  [POLE at s=1]
         - 2 sum_n Lambda(n)/sqrt(n) (g*g~)(log n)     [PRIMES = conductor blocks]   (arithmetic side)

where 2 theta'(r) = Re psi(1/4+ir/2) - log pi  is exactly the apex archimedean
phase-clock velocity (N5).  RH  <=>  Q(g) >= 0 for all such g  (Weil's criterion):
on the spectral side, if every zero is on the line gamma is real and |ghat(gamma)|^2>=0;
an off-line zero pairs ghat(rho)ghat(1-rho) and can be made negative.

On a finite basis {g_k} of support-[-L,L] functions, Q = c^T M c with
  M_jk = (1/2pi) int ghat_j ghat_k 2 theta' dr  +  2 G_j G_k  -  2 sum_n Lam(n)/sqrt n (g_j*g_k)(log n).
The margin = lambda_min(M).  As L grows, primes with log n <= 2L enter (the eroding
term); the archimedean apex floor (+pole) holds it up.  We:
  (1) VERIFY  c^T M c == sum_gamma |ghat(gamma)|^2  on the true zeros (calibration),
  (2) report lambda_min(M) (the margin) as L = 1,1.5,2,2.5,3 (primes come in).

Deterministic: numpy + mpmath (zeros, digamma).
"""

import numpy as np
import mpmath as mp
mp.mp.dps = 20

# 2 theta'(r) = Re psi(1/4 + i r/2) - log pi   (apex archimedean density, N5)
def two_theta_prime(rvals):
    out = np.empty_like(rvals, dtype=float)
    lp = float(mp.log(mp.pi))
    for i, r in enumerate(rvals):
        out[i] = float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.mpf(r)/2))) - lp
    return out

def vonmangoldt_upto(Nmax):
    """list of (n, Lambda(n)) for 2<=n<=Nmax with Lambda(n)!=0."""
    out = []
    for n in range(2, Nmax + 1):
        m, p = n, 0
        d = 2; pp = None; ok = True
        # factor n; prime power iff single prime
        temp = n; primes = set()
        dd = 2
        while dd * dd <= temp:
            while temp % dd == 0:
                primes.add(dd); temp //= dd
            dd += 1
        if temp > 1:
            primes.add(temp)
        if len(primes) == 1:
            out.append((n, float(mp.log(next(iter(primes))))))
    return out

def basis_funcs(u, L, m):
    """smooth even compactly-supported basis on [-L,L]: bump * cos(k pi u/L)."""
    env = np.where(np.abs(u) <= L, (1 + np.cos(np.pi * u / L)) / 2, 0.0)
    G = np.zeros((m, len(u)))
    for k in range(m):
        G[k] = env * np.cos(k * np.pi * u / L)
    return G

def run(L, m=14):
    # grids
    du = 2 * L / 4000
    u = np.arange(-L, L + du/2, du)
    g = basis_funcs(u, L, m)                       # m x len(u)
    # FT ghat_k(r) = int g_k(u) e^{i r u} du = int g_k cos(r u) du  (g even, real)
    R, dr = 260.0, 0.05
    r = np.arange(-R, R + dr/2, dr)
    cosru = np.cos(np.outer(r, u))                 # len(r) x len(u)
    ghat = (g @ cosru.T) * du                      # m x len(r)   (real, even in r)
    # archimedean matrix A_jk = (1/2pi) int ghat_j ghat_k 2theta' dr
    ttp = two_theta_prime(r)
    A = np.zeros((m, m))
    for j in range(m):
        wj = ghat[j] * ttp * dr / (2 * np.pi)
        for k in range(j, m):
            A[j, k] = A[k, j] = np.sum(wj * ghat[k])
    # pole G_k = int g_k cosh(u/2) du  -> rank-1 term 2 G G^T
    coshu = np.cosh(u / 2)
    Gk = (g * coshu) @ np.ones_like(u) * du
    POLE = 2 * np.outer(Gk, Gk)
    # prime matrix P_jk = 2 sum_n Lam(n)/sqrt(n) (g_j * g_k)(log n),  log n <= 2L
    Nmax = int(np.floor(np.exp(2 * L)))
    vm = [(n, lam) for (n, lam) in vonmangoldt_upto(Nmax) if np.log(n) <= 2 * L + 1e-9]
    P = np.zeros((m, m))
    for (n, lam) in vm:
        w = np.log(n)
        # (g_j * g_k)(w) = int g_j(v) g_k(v-w) dv
        gk_shift = np.array([np.interp(u - w, u, g[k], left=0.0, right=0.0) for k in range(m)])
        corr = (g @ gk_shift.T) * du               # m x m, corr[j,k]=(g_j*g_k)(w)
        P += 2 * lam / np.sqrt(n) * corr
    M = A + POLE - P
    M = (M + M.T) / 2
    return M, ghat, r, vm

# ---- (1) calibration: c^T M c == sum_gamma |ghat(gamma)|^2 on true zeros -----
print("=" * 74)
print("(1) CALIBRATION: arithmetic Weil form == spectral side over true zeros")
print("=" * 74)
L0, m0 = 2.0, 14
M, ghat, r, vm = run(L0, m0)
# true zeros
NZ = 200
gammas = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)])
def ghat_at(gam, c):
    # interpolate sum_k c_k ghat_k at r=gam
    gh = c @ np.array([np.interp(gam, r, ghat[k]) for k in range(len(c))])
    return gh
rng = np.random.default_rng(0)
print(f"  L={L0}, basis m={m0}, primes used (log n<=2L): {len(vm)} (up to n={vm[-1][0]})")
print(f"  {'trial':>6} {'arithmetic cMc':>16} {'spectral sum|ghat|^2':>22} {'rel.err':>10}")
maxerr = 0.0
for trial in range(4):
    c = rng.standard_normal(m0)
    arith = float(c @ M @ c)
    spec = 2 * np.sum([ (c @ np.array([np.interp(gm, r, ghat[k]) for k in range(m0)]))**2
                        for gm in gammas ])
    e = abs(arith - spec) / (abs(spec) + 1e-30)
    maxerr = max(maxerr, e)
    print(f"  {trial:>6} {arith:>16.6f} {spec:>22.6f} {e:>10.2e}")
print(f"  >>> max rel.err = {maxerr:.2e}  [{'CALIBRATED' if maxerr<5e-2 else 'CHECK conventions'}]")

# ---- (2) the margin as primes come in ----------------------------------------
print()
print("=" * 74)
print("(2) THE MARGIN  lambda_min(M)  as L grows (primes log n <= 2L enter)")
print("=" * 74)
print(f"  {'L':>5} {'#primes/ppowers':>16} {'max n':>7} {'lambda_min (margin)':>20} {'lambda_max':>12}")
for L in [1.0, 1.5, 2.0, 2.5, 3.0]:
    M, ghat, r, vm = run(L, m=14)
    ev = np.linalg.eigvalsh(M)
    maxn = vm[-1][0] if vm else 0
    print(f"  {L:>5} {len(vm):>16} {maxn:>7} {ev[0]:>20.6e} {ev[-1]:>12.4e}")

print()
print("=" * 74)
print("READING")
print("=" * 74)
print("""  If (1) calibrates: the matrix M IS the genuine Weil quadratic form -- the
  arithmetic side (apex archimedean 2theta' + pole - primes) reproduces the
  spectral side sum over the actual zeros.  Then lambda_min(M) in (2) is the
  true Weil margin on support-[-L,L] test functions.
  RH <=> M stays positive semidefinite as L -> infinity (all primes in).
  The apex contribution: the archimedean floor (2theta', N5) + the pole rank-1
  are PSD; the primes erode.  The thread closes iff the floor holds the margin
  >= 0 in the limit -- the squared-norm/Gram structure (P0 Prop 4.3) is the
  lever, since each place's energy is a squared norm.""")
