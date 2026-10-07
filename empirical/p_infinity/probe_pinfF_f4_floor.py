"""probe_pinfF_f4_floor.py -- the F.4 strike: the flat archimedean floor at mechanism level.

PRE-REGISTERED PREDICTIONS (written before running; GPD, Paper 35):
  P1 (floor law): the off-E arch+pole floor equals 2*theta'(gamma_1) = 0.811 up to width
      corrections, lambda-FLAT including lambda=3.5 -- the floor is the archimedean energy
      of the FIRST ZERO's sampling representer; it is positive because gamma_1 = 14.13 > 2*pi
      (the first zero lies outside the light cone where the first integer enters).
      FALSIFIER KF1: floor at lambda=3.5 outside [0.75, 0.95], or floor tracking the
      cell-count band law 2*theta'(pi*k/(L/2)) instead of the constant.
  P2 (fingerprint): the off-E minimizer IS the gamma_1 representer:
      |<v0, rep_1>|^2 >= 0.5 at lambda >= 2.5; spectral centroid in [13.5, 15.5];
      second off-E eigenvalue closer to 2*theta'(gamma_2) = 1.208 than to the band-edge
      alternative 2*theta'(17.58) = 1.029 (zero-ladder, not band-continuum).
      FALSIFIER KF2: overlap^2 < 0.5 at lambda = 3.
  P3 (coverage saturation): the E-sector covers sub-gamma_1 band content (T <= 11 Slepian
      modes: residual to the cell span < 0.15 at lambda = 3) and saturates near gamma_1:
      T = 17, 21 Slepians keep O(1) residual even against the FULL even-n E-image cone
      (enrichment-stable), and the residual aligns with the zero representers.
      FALSIFIER KF3: full-cone residual for T > gamma_1 Slepians < 0.05 enrichment-stable
      (then coverage does NOT saturate at gamma_1 and the mechanism must be cell-specific).

THEOREM F.4.A (band-split floor; proven; verified numerically here as a convention check):
  for even real phi supported in the window, ||phi|| = 1, and any T > 0:
     arch(phi) >= 2*theta'(T) - 2*(theta'(T) - theta'(0)) * mu_T(phi),
  where mu_T = in-band spectral mass fraction (theta' even, strictly increasing in |t|),
  and pole(phi) = 2*m(phi)^2 >= 0 on the real even sector.

Machinery: exact mpmath matrix builder (certified, probe_ccm_exact_matrix lineage) for
lambda <= 3; multiplier-grid arch matrix for lambda = 3.5 with cross-validation at 3.0;
FD prolates via eig_banded (never scipy prolates).  Deterministic, local, ~10 min.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
from scipy.special import digamma
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

ZEROS = [14.134725141734693, 21.022039638771555, 25.010857580145688,
         30.424876125859513, 32.935061587739190]
G1, G2, G3 = ZEROS[0], ZEROS[1], ZEROS[2]


def thetap(t):
    return -0.5 * np.log(np.pi) + 0.5 * np.real(digamma(0.25 + 0.5j * np.asarray(t, float)))

TH0 = float(thetap(0.0))                       # -2.6861
REF1, REF2, REF3 = 2 * float(thetap(G1)), 2 * float(thetap(G2)), 2 * float(thetap(G3))
REFMID = 2 * float(thetap(0.5 * (G1 + G2)))    # band-edge alternative for e1


def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW(lam, N, with_primes=True):
    """Exact window Weil matrix (V_n basis), certified lineage. arch+pole if not with_primes."""
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
    """FD prolates on [-lam, lam], c = 2*pi*lam^2; returns all even-n modes + defects."""
    x = np.linspace(-lam, lam, M); dx = x[1] - x[0]
    xm = (x[:-1] + x[1:]) / 2
    a = lam**2 - xm**2
    diag = np.zeros(M); diag[:-1] += a / dx**2; diag[1:] += a / dx**2
    diag += (2 * np.pi * lam * x)**2
    bands = np.vstack([diag, np.append(-a / dx**2, 0.0)])
    _, vv = eig_banded(bands, lower=True, select='i', select_range=(0, nmax))
    F = np.exp(2j * np.pi * np.outer(x, x)) * dx
    H, defects = {}, {}
    for n in range(0, nmax + 1, 2):
        h = vv[:, n] / np.sqrt(dx)
        if h[M // 2] < 0 and n % 4 == 0:
            h = -h
        H[n] = h
        Fh = (F @ h)
        defects[n] = float(np.dot(h, h - (Fh.real if n % 4 == 0 else -Fh.real)) * dx)
    return x, H, defects


def cell_coeffs(lam_f, L, N, h, x):
    """Window restriction of E(h), normalized, as V_n coefficients (complex)."""
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


def VH_on_grid(N, L, ts):
    wn = (2 * np.pi / L) * np.arange(-N, N + 1)[:, None]
    d = wn - ts[None, :]
    small = np.abs(d) < 1e-12
    dd = np.where(small, 1.0, d)
    out = np.where(small, L, (np.exp(1j * dd * L) - 1) / (1j * dd))
    return np.exp(1j * ts[None, :] * L / 2) / np.sqrt(L) * out


def pole_matrix(N, L):
    al = np.array([Vhat_c(n, 0.5j, L) for n in range(-N, N + 1)])
    be = np.array([Vhat_c(n, -0.5j, L) for n in range(-N, N + 1)])
    return np.real(np.outer(al, np.conj(be)) + np.outer(be, np.conj(al)))


def arch_matrix_multiplier(N, L, Tmax=4000.0, step=0.02, chunk=20000):
    """QWa = (1/pi) int |.|^2 theta' dt + pole, on the V_n basis, chunked t-grid."""
    dim = 2 * N + 1
    M = np.zeros((dim, dim), dtype=complex)
    tgrid = np.arange(-Tmax, Tmax, step)
    for i0 in range(0, len(tgrid), chunk):
        ts = tgrid[i0:i0 + chunk]
        VH = VH_on_grid(N, L, ts)
        Wt = thetap(ts)
        M += (VH * Wt[None, :]) @ np.conj(VH).T * step
    return np.real(M) / np.pi + pole_matrix(N, L)


def band_matrix_even(N, L, T, Ebas, step=0.004):
    ts = np.arange(-T, T, step)
    VH = VH_on_grid(N, L, ts)
    Q = (VH @ np.conj(VH).T) * step / (2 * np.pi)
    return Ebas.T @ np.real(Q) @ Ebas


def rep_vector(gam, N, L, Ebas):
    v = np.array([Vhat_c(n, gam, L) for n in range(-N, N + 1)])
    r = Ebas.T @ v
    assert np.max(np.abs(r.imag)) < 1e-8 * np.max(np.abs(r.real)) + 1e-12, "rep not real"
    r = np.real(r)
    return r / np.linalg.norm(r)


def span_orth(cols, tol=2e-7):
    Mt = np.column_stack(cols)
    U, s, _ = np.linalg.svd(Mt, full_matrices=False)
    return U[:, s > tol * s[0]]


def resid_to(vec, U):
    r = vec - U @ (U.T @ vec)
    return np.linalg.norm(r), r


# =====================================================================================
print("== F.4 STRIKE: flat archimedean floor -- mechanism measurements ==")
print(f"   references: 2*theta'(gamma_1) = {REF1:.4f}   2*theta'(gamma_2) = {REF2:.4f}   "
      f"2*theta'(gamma_3) = {REF3:.4f}   band-edge alt 2*theta'({0.5*(G1+G2):.2f}) = {REFMID:.4f}")
print(f"   theta'(0) = {TH0:.4f}; cone edge 2*pi = {2*np.pi:.4f}; gamma_1/2pi = {G1/(2*np.pi):.4f}")

CASES = [(1.5, 10), (2.0, 12), (2.5, 15), (3.0, 18), (3.5, 21)]
data = {}
ok_machinery = True

print("\n== EXP-A: off-E arch+pole spectrum, minimizer anatomy ==")
print("   lam   cells  e0(floor)  e1      e2      tbar(v0)  2th'(tbar)  |<v0,rep1>|  "
      "mass(|t|<11)  pole-share")
for lam_f, N in CASES:
    c_pr = 2 * np.pi * lam_f**2
    nmax = max(36, int(4 * np.ceil((2 * c_pr / np.pi + 8) / 4)))
    use_mult = lam_f > 3.0
    if use_mult:
        L = float(2 * np.log(lam_f))
        QWa = arch_matrix_multiplier(N, L)
    else:
        QWa, L = build_QW(mp.mpf(str(lam_f)), N, with_primes=False)
    Ebas = Ebas_of(N)
    x, H, defects = prolate_cells(lam_f, nmax)
    I0 = np.trapezoid(H[0], x)
    cols, used = [], []
    for n in sorted(defects):
        if n == 0 or n % 4 != 0 or defects[n] >= 0.05:
            continue
        cc = cell_coeffs(lam_f, L, N, H[n] - (np.trapezoid(H[n], x) / I0) * H[0], x)
        if cc is not None:
            cols.append(Ebas.T @ cc.real)
            used.append(n)
    C = np.column_stack(cols)
    Qc, _ = np.linalg.qr(C)
    Pp = np.eye(N + 1) - Qc @ Qc.T
    wo, vo = np.linalg.eigh(Pp)
    Qo = vo[:, wo > 0.5]
    Ae = Ebas.T @ QWa @ Ebas
    Ao = Qo.T @ Ae @ Qo
    ev, evec = np.linalg.eigh(Ao)
    v0 = Qo @ evec[:, 0]
    v1 = Qo @ evec[:, 1] if Ao.shape[0] > 1 else None
    # spectral profile of v0
    ts = np.arange(-80, 80, 0.01)
    fh = (Ebas @ v0) @ VH_on_grid(N, L, ts)
    prof = np.abs(fh)**2
    tbar = float(np.sum(np.abs(ts) * prof) / np.sum(prof))
    Q11 = band_matrix_even(N, L, 11.0, Ebas)
    m11 = float(v0 @ Q11 @ v0)
    Pol_e = Ebas.T @ pole_matrix(N, L) @ Ebas
    pole_share = float(v0 @ Pol_e @ v0) / float(v0 @ Ae @ v0)
    r1 = rep_vector(G1, N, L, Ebas)
    ov1 = abs(float(v0 @ r1))
    data[lam_f] = dict(N=N, L=L, Ebas=Ebas, Ae=Ae, Qo=Qo, Qc=Qc, C=C, ev=ev, v0=v0, v1=v1,
                       Pol_e=Pol_e, x=x, H=H, defects=defects, I0=I0, used=used)
    th_tb = 2 * float(thetap(tbar))
    print(f"   {lam_f:3}   {len(used):^5}  {ev[0]:8.4f}  {ev[1]:6.3f}  {ev[2]:6.3f}  "
          f"{tbar:7.2f}  {th_tb:9.4f}  {abs(ov1):^11.3f}  {m11:^12.4f}  {pole_share:^10.4f}"
          + ("   [multiplier build]" if use_mult else ""))

# cross-validation of the multiplier build at lambda = 3.0
d3 = data[3.0]
QWa_m = arch_matrix_multiplier(d3['N'], d3['L'])
Ae_m = d3['Ebas'].T @ QWa_m @ d3['Ebas']
e0_m = float(np.min(np.linalg.eigvalsh(d3['Qo'].T @ Ae_m @ d3['Qo'])))
e0_x = float(data[3.0]['ev'][0])
dx_val = abs(e0_m - e0_x)
ok_machinery &= dx_val < 0.02
print(f"\n   cross-validation lambda=3.0: off-E floor exact {e0_x:.4f} vs multiplier {e0_m:.4f}"
      f"  (|diff| = {dx_val:.4f}, require < 0.02)")

# ---------------- EXP-B: representer ladder ----------------
print("\n== EXP-B: zero-representer ladder (A-energy of rep_k; cell-span component) ==")
print("   lam    A(rep1)  A(rep2)  A(rep3)   ref1    ref2    ref3   in-cell(rep1)  |<v1,rep2>|")
for lam_f, N in CASES:
    d = data[lam_f]
    row = []
    incell = None
    for k, g in enumerate([G1, G2, G3]):
        r = rep_vector(g, N, d['L'], d['Ebas'])
        row.append(float(r @ d['Ae'] @ r))
        if k == 0:
            incell = np.linalg.norm(d['Qc'].T @ r)
    ov2 = abs(float(d['v1'] @ rep_vector(G2, N, d['L'], d['Ebas']))) if d['v1'] is not None else np.nan
    print(f"   {lam_f:3}   {row[0]:7.4f}  {row[1]:7.4f}  {row[2]:7.4f}   "
          f"{REF1:.3f}   {REF2:.3f}   {REF3:.3f}   {incell:^12.3f}  {ov2:^9.3f}")

# ---------------- EXP-C: coverage geometry ----------------
print("\n== EXP-C: band-Slepian coverage by the E-sector (cells vs full even-n cone) ==")
TLIST = [8.0, 11.0, G1, 17.0, 21.0]
for lam_f in (2.5, 3.0):
    N = data[lam_f]['N']; d = data[lam_f]
    L, Ebas = d['L'], d['Ebas']
    # full-cone dictionary: all even n >= 2, vanishing-integral combos, enrichment tiers
    tiers = {}
    for cap in (12, 24, 40):
        cols = []
        for n in sorted(d['defects']):
            if n == 0 or n > cap:
                continue
            cc = cell_coeffs(lam_f, L, N, d['H'][n] - (np.trapezoid(d['H'][n], d['x']) / d['I0']) * d['H'][0], d['x'])
            if cc is not None:
                cols.append(Ebas.T @ cc.real)
        tiers[cap] = cols
    pole_dir = None
    valp = np.array([Vhat_c(n, 0.5j, L) for n in range(-N, N + 1)])
    pv = np.real(Ebas.T @ valp)
    pole_dir = pv / np.linalg.norm(pv)
    U_cell = span_orth([d['C'][:, j] for j in range(d['C'].shape[1])] + [pole_dir])
    r1 = rep_vector(G1, N, L, Ebas); r2 = rep_vector(G2, N, L, Ebas)
    print(f"   lambda = {lam_f} (cells = {d['C'].shape[1]}, +pole dir; dict tiers n<=12/24/40):")
    print("    T      slep-chi   resid(cells)  resid(d12)  resid(d24)  resid(d40)  "
          "align(rep1)  align(rep2)")
    for T in TLIST:
        QT = band_matrix_even(N, L, T, Ebas)
        wq, vq = np.linalg.eigh(QT)
        idx = np.where(wq > 0.5)[0]
        if len(idx) == 0:
            continue
        s = vq[:, idx[-1]]                     # top Slepian mode
        chi = wq[idx[-1]]
        rc, _ = resid_to(s, U_cell)
        rr = []
        rvec = None
        for cap in (12, 24, 40):
            U_t = span_orth(tiers[cap] + [pole_dir])
            rt, rv = resid_to(s, U_t)
            rr.append(rt)
            if cap == 40:
                rvec = rv
        a1 = abs(float(rvec @ r1)) / (np.linalg.norm(rvec) + 1e-30)
        a2 = abs(float(rvec @ r2)) / (np.linalg.norm(rvec) + 1e-30)
        print(f"   {T:6.2f}  {chi:8.3f}   {rc:^12.4f}  {rr[0]:^10.4f}  {rr[1]:^10.4f}  "
              f"{rr[2]:^10.4f}  {a1:^10.3f}  {a2:^10.3f}")

# ---------------- F.4.A inequality verification (convention check of the theorem) ----------------
print("\n== THEOREM F.4.A check: arch(phi) >= 2th'(T) - 2(th'(T)-th'(0))*mu_T, random draws ==")
rng = np.random.default_rng(11)
okA = True
for lam_f in (2.0, 3.0):
    d = data[lam_f]; N = d['N']; L = d['L']; Ebas = d['Ebas']
    arch_e = d['Ae'] - d['Pol_e']
    worst = np.inf
    for T in (8.0, G1, 20.0):
        QT = band_matrix_even(N, L, T, Ebas)
        thT = float(thetap(T))
        for _ in range(20):
            c = rng.normal(size=N + 1); c /= np.linalg.norm(c)
            lhs = float(c @ arch_e @ c)
            mu = float(c @ QT @ c)
            bound = 2 * thT - 2 * (thT - TH0) * mu
            worst = min(worst, lhs - bound)
    okA &= worst > -0.02
    print(f"   lambda={lam_f}: min[arch - bound] over 60 draws x 3 bands = {worst:+.4f}  "
          f"(require > -0.02; theorem says >= 0, tolerance = quadrature)")
ok_machinery &= okA

# ---------------- verdicts ----------------
print("\n== VERDICTS (pre-registered) ==")
floors = {lf: float(data[lf]['ev'][0]) for lf, _ in CASES}
flat_ok = all(0.75 <= floors[lf] <= 0.95 for lf in (2.0, 2.5, 3.0, 3.5))
print(f"   P1 floor law: floors = " + ", ".join(f"{lf}:{floors[lf]:.3f}" for lf, _ in CASES)
      + f"  -> lambda>=2 all in [0.75,0.95]: {flat_ok}"
      + ("  [P1 SURVIVES: flat at ~2th'(gamma_1)]" if flat_ok else "  [KF1 FIRED]"))
d30 = data[3.0]
ov30 = abs(float(d30['v0'] @ rep_vector(G1, d30['N'], d30['L'], d30['Ebas'])))
e1_30 = float(d30['ev'][1])
zl = abs(e1_30 - REF2) < abs(e1_30 - REFMID)
p2_ok = ov30**2 >= 0.5
print(f"   P2 fingerprint: |<v0,rep1>|^2 at lambda=3: {ov30**2:.3f} (>=0.5: {p2_ok}); "
      f"e1 = {e1_30:.3f} vs ref2 {REF2:.3f} / band-alt {REFMID:.3f} -> zero-ladder: {zl}"
      + ("  [P2 SURVIVES]" if (p2_ok and zl) else "  [KF2 FIRED or partial]"))
print("   P3 coverage: read EXP-C table -- sub-gamma_1 residuals small + T>gamma_1 residuals"
      " O(1) enrichment-stable = SURVIVES; T>gamma_1 residual <0.05 at d40 = KF3 FIRED.")
print("\nRESULT: " + ("GREEN -- machinery validated (cross-val + F.4.A inequality); "
                      "verdicts above are the measurement" if ok_machinery else
                      "RED -- machinery check failed; fix before reading verdicts"))
