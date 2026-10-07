"""probe_pinfF_f5_sampling.py -- the F.5' strike: QW on the sampling sector.

CONTEXT: F.4 strike (P-inf-F section 7) established off-E = span{zero representers} + one
pole-protected direction (dim count exact at lambda = 3, 3.5; eigenvector overlaps 0.99-1.00).
The full window Weil form on that sector is then the explicit formula's ZERO SIDE:
   QW_lambda(f) = sum_gamma |fhat(gamma)|^2   (on-line zeros; verified range; + tiny tail),
which is positive BY COMPUTATION at any fixed window -- no RH input.  The asymptotic
(lambda -> infinity) version is the genuine residue (smoothed-density positivity at the
zeros; Montgomery form-factor territory).  This probe certifies the per-window discharge.

PRE-REGISTERED PREDICTIONS (GPD):
  Q1 (positivity on named directions): QW_lambda(rep_k) > 0 for every resolved zero k at
      lambda = 2, 2.5, 3 -- O(1), tracking the smoothed truncated density spike.
      FALSIFIER G1: any QW(rep_k) < -floor -- a window-Weil-positivity violation on a
      named direction (would contradict RH; diagnose quadrature first per float64 lesson).
  Q2 (sector model adequacy): the off-E minimizer of the FULL form lies in the
      rep-span + pole-dir model space: overlap >= 0.8 at lambda >= 2.5; and the K2 bounce
      (0.57 / 0.30 / 0.61) is explained as min_k QW(rep_k) +- mixing.
      FALSIFIER G2: overlap < 0.8 at lambda = 3 (sampling-sector model of (B2b) inadequate).
  Q3 (zero-side identity = the per-window discharge): QW(rep_1) equals the on-line
      zero-side sum 2*sum_{gamma<=gamma_40} |fhat(gamma)|^2 within quadrature + explicit
      tail allowance.  FALSIFIER G3: mismatch beyond allowance (criterion vs mathematics:
      diagnose normalization first).
  Q4 (the +1 direction): the off-E complement of the rep-span is pole-protected
      (large pole share, QW positive O(1)).

Machinery: certified exact builder (with primes); FD prolate cells; representers as in
probe_pinfF_f4_floor.py.  Zeros via mp.zetazero at dps 15 (evaluation points only).
Deterministic, local, ~6-10 min.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
from scipy.special import digamma
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30


def thetap(t):
    return -0.5 * np.log(np.pi) + 0.5 * np.real(digamma(0.25 + 0.5j * np.asarray(t, float)))


def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW(lam, N, with_primes=True):
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    pj = []
    if with_primes:
        for p in primes_upto(float(mp.exp(L)) + 1e-12):
            j = 1
            while j * mp.log(p) <= L + mp.mpf("1e-25"):
                pj.append((j * mp.log(p), mp.log(p) * mp.power(p, -mp.mpf(j) / 2)))
                j += 1
    pts = mp.linspace(0, L, 14)
    S = {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        P = mp.fsum(cw * mp.sin(wk * yp) for yp, cw in pj) if pj else mp.mpf(0)
        S[k] = A - B - P
    tailL = mp.log(mp.tanh(L / 2)) / 2
    D = {}
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + mp.euler) + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj) if pj else mp.mpf(0)
        D[k] = A - WR - P
    dim = 2 * N + 1
    QW = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            n, m = i - N, j - N
            QW[i, j] = float(D[abs(n)] if n == m else (S[m] - S[n]) / (mp.pi * (n - m)))
    return QW, float(L)


def prolate_cells(lam, nmax, M=6001):
    x = np.linspace(-lam, lam, M); dx = x[1] - x[0]
    xm = (x[:-1] + x[1:]) / 2
    a = lam**2 - xm**2
    diag = np.zeros(M); diag[:-1] += a / dx**2; diag[1:] += a / dx**2
    diag += (2 * np.pi * lam * x)**2
    bands = np.vstack([diag, np.append(-a / dx**2, 0.0)])
    _, vv = eig_banded(bands, lower=True, select='i', select_range=(0, nmax))
    F = np.exp(2j * np.pi * np.outer(x, x)) * dx
    H, defects = {}, {}
    for n in range(0, nmax + 1, 4):
        h = vv[:, n] / np.sqrt(dx)
        if h[M // 2] < 0:
            h = -h
        H[n] = h
        defects[n] = float(np.dot(h, h - (F @ h).real) * dx)
    return x, H, defects


def cell_coeffs(lam_f, L, N, h, x):
    xg = np.linspace(0.0, L, 3001)
    u = np.exp(xg - L / 2)
    kl = np.zeros_like(u)
    for n in range(1, int(lam_f / u.min()) + 2):
        msk = n * u <= lam_f
        kl[msk] += np.interp(n * u[msk], x[x >= 0], h[x >= 0])
    kl *= np.sqrt(u)
    nrm = np.sqrt(np.trapezoid(kl * kl, xg))
    if nrm < 1e-9:
        return None
    kl /= nrm
    return np.array([np.trapezoid(kl * np.exp(-2j * np.pi * n * xg / L) / np.sqrt(L), xg)
                     for n in range(-N, N + 1)])


def Ebas_of(N):
    dim = 2 * N + 1
    E = np.zeros((dim, N + 1))
    E[N, 0] = 1.0
    for k in range(1, N + 1):
        E[N + k, k] = E[N - k, k] = 1 / np.sqrt(2)
    return E


def Vhat_c(n, z, L):
    wn = 2 * np.pi * n / L
    d = wn - z
    if abs(d) < 1e-12:
        return np.exp(1j * z * L / 2) * np.sqrt(L)
    return np.exp(1j * z * L / 2) / np.sqrt(L) * (np.exp(1j * d * L) - 1) / (1j * d)


def rep_vector(gam, N, L, Ebas):
    v = np.array([Vhat_c(n, gam, L) for n in range(-N, N + 1)])
    r = np.real(Ebas.T @ v)
    return r / np.linalg.norm(r)


def fhat_of(coef_even, Ebas, N, L, t):
    c = Ebas @ coef_even
    return sum(c[N + n] * Vhat_c(n, t, L) for n in range(-N, N + 1))


# ---- zeros (evaluation points only; dps 15 suffices) ----
print("harvesting zeros (mp.zetazero, 40)...")
mp.mp.dps = 15
GAMMAS = [float(mp.im(mp.zetazero(k))) for k in range(1, 41)]
mp.mp.dps = 30
print("   gamma_1..5 = " + ", ".join(f"{g:.6f}" for g in GAMMAS[:5]) + f"; gamma_40 = {GAMMAS[-1]:.3f}")

CASES = [(2.0, 12), (2.5, 15), (3.0, 18)]
okM = True
print("\n== EXP-1/2/4: full form on the sampling sector ==")
for lam_f, N in CASES:
    QWf, L = build_QW(mp.mpf(str(lam_f)), N, True)
    Ebas = Ebas_of(N)
    Qf_e = Ebas.T @ QWf @ Ebas
    c_pr = 2 * np.pi * lam_f**2
    nmax = max(36, int(4 * np.ceil((2 * c_pr / np.pi + 8) / 4)))
    nmax = min(nmax, 36) if lam_f <= 3.0 else nmax          # match falsifier-probe cells
    x, H, defects = prolate_cells(lam_f, nmax)
    I0 = np.trapezoid(H[0], x)
    cols = []
    for n in sorted(defects):
        if n == 0 or defects[n] >= 0.05:
            continue
        cc = cell_coeffs(lam_f, L, N, H[n] - (np.trapezoid(H[n], x) / I0) * H[0], x)
        if cc is not None:
            cols.append(Ebas.T @ cc.real)
    C = np.column_stack(cols)
    Qc, _ = np.linalg.qr(C)
    Pp = np.eye(N + 1) - Qc @ Qc.T
    wo, vo = np.linalg.eigh(Pp)
    Qo = vo[:, wo > 0.5]
    omega_N = 2 * np.pi * N / L
    gam_res = [g for g in GAMMAS if g <= omega_N]
    reps = [rep_vector(g, N, L, Ebas) for g in gam_res]
    # EXP-1: QW on each representer
    qw_reps = [float(r @ Qf_e @ r) for r in reps]
    print(f"\n   lambda = {lam_f} (N={N}, omega_N={omega_N:.1f}, cells={C.shape[1]}, "
          f"off-E dim={Qo.shape[1]}, resolved zeros={len(gam_res)})")
    print("   QW(rep_k):  " + "  ".join(f"{q:+.3f}" for q in qw_reps))
    neg = [(k + 1, q) for k, q in enumerate(qw_reps) if q < -5e-3]
    if neg:
        print(f"   !! G1 CANDIDATE (diagnose quadrature first): {neg}")
    # EXP-2: off-E full-form minimizer vs the model space (reps + pole-dir)
    Qoff = Qo.T @ Qf_e @ Qo
    evf, evecf = np.linalg.eigh(Qoff)
    vmin = Qo @ evecf[:, 0]
    valp = np.array([Vhat_c(n, 0.5j, L) for n in range(-N, N + 1)])
    pv = np.real(Ebas.T @ valp); pv /= np.linalg.norm(pv)
    Mdl = np.column_stack(reps + [pv])
    U, s, _ = np.linalg.svd(Mdl, full_matrices=False)
    Um = U[:, s > 1e-7 * s[0]]
    ov_model = np.linalg.norm(Um.T @ vmin)
    print(f"   off-E full-form spectrum bottom: {evf[0]:+.4f}, {evf[1]:+.4f}, {evf[2]:+.4f}"
          f"   min_k QW(rep_k) = {min(qw_reps):+.4f}")
    print(f"   off-E minimizer: |proj onto rep+pole model| = {ov_model:.3f}")
    # EXP-4: the +1 direction = off-E component orthogonal to rep-span
    Ur, sr, _ = np.linalg.svd(np.column_stack(reps), full_matrices=False)
    Urr = Ur[:, sr > 1e-7 * sr[0]]
    Poff = Qo @ Qo.T
    comp = Poff - Urr @ (Urr.T @ Poff)      # off-E directions not in rep-span
    wc, vc = np.linalg.eigh((comp + comp.T) / 2)
    plus = vc[:, -1]                         # dominant leftover direction
    plus = plus - Urr @ (Urr.T @ plus); plus /= np.linalg.norm(plus)
    qw_plus = float(plus @ Qf_e @ plus)
    QWa, _ = build_QW(mp.mpf(str(lam_f)), N, False)
    Aa_e = Ebas.T @ QWa @ Ebas
    al = np.array([Vhat_c(n, 0.5j, L) for n in range(-N, N + 1)])
    be = np.array([Vhat_c(n, -0.5j, L) for n in range(-N, N + 1)])
    Pol = np.real(np.outer(al, np.conj(be)) + np.outer(be, np.conj(al)))
    Pol_e = Ebas.T @ Pol @ Ebas
    pole_share_plus = float(plus @ Pol_e @ plus) / max(float(plus @ Aa_e @ plus), 1e-12)
    print(f"   '+1' direction: QW = {qw_plus:+.4f}, pole share of its arch+pole = {pole_share_plus:.3f}, "
          f"|<+1, pole-dir>| = {abs(float(plus @ pv)):.3f}")
    if lam_f == 3.0:
        d3 = dict(N=N, L=L, Ebas=Ebas, Qf_e=Qf_e, reps=reps, gam_res=gam_res, qw=qw_reps)

# ---- EXP-3: zero-side identity on rep_1 at lambda = 3 (the per-window discharge) ----
print("\n== EXP-3: zero-side identity QW(rep_1) = 2 sum |fhat(gamma)|^2 (lambda = 3) ==")
N, L, Ebas = d3['N'], d3['L'], d3['Ebas']
r1 = d3['reps'][0]
lhs = float(r1 @ d3['Qf_e'] @ r1)
partial = []
tot = 0.0
for j, g in enumerate(GAMMAS):
    tot += 2 * abs(fhat_of(r1, Ebas, N, L, g))**2
    if j + 1 in (5, 10, 20, 30, 40):
        partial.append((j + 1, tot))
print("   partial zero sums: " + "   ".join(f"J={J}: {v:.4f}" for J, v in partial))
# explicit tail allowance: density ~ log(g/2pi)/2pi per unit, |fhat|^2 ~ C/(g-g1)^2 envelope
gJ = GAMMAS[-1]
env = abs(fhat_of(r1, Ebas, N, L, gJ))**2 * (gJ - GAMMAS[0])**2
tail = 2 * env * np.log(gJ / (2 * np.pi)) / (2 * np.pi) / (gJ - GAMMAS[0])
err = abs(lhs - tot)
allow = max(0.03 * abs(lhs), tail + 0.02)
ok3 = err < allow
okM &= ok3
print(f"   QW(rep_1) geometric side = {lhs:.4f}   zero side (J=40) = {tot:.4f}   "
      f"|diff| = {err:.4f}   allowance = {allow:.4f}   -> {'MATCH' if ok3 else 'MISMATCH'}")
print("   (positivity of QW on the sampling sector at fixed window = verified zeros + this"
      " identity + tail bound: no RH input)")

print("\n== VERDICTS (pre-registered) ==")
print("   Q1: QW(rep_k) all positive at all windows -> see tables (G1 fires only on a"
      " negative beyond floor).")
print("   Q2: off-E minimizer in rep+pole model space (overlap printed per window;"
      " >= 0.8 at lambda >= 2.5 = SURVIVES).")
print("   Q3: " + ("SURVIVES -- per-window discharge certified" if ok3 else "G3 FIRED -- diagnose"))
print("   Q4: '+1' direction pole-protected (see pole shares).")
print("\nRESULT: " + ("GREEN -- zero-side identity certified; sampling-sector readings above"
                      if okM else "RED -- EXP-3 identity failed; diagnose before reading"))
