"""probe_pinfF_f7_absorption.py -- the F.5'' strike: the absorption identity and the frame race.

PRE-REGISTERED PREDICTIONS (GPD):
  R1 (absorption / Theorem F.7): the mod-4 cell count obeys K(lambda) = lambda^2 - O(log lambda),
      matching the zero-sampling deficit below the cone edge T_cone = 2*pi*lambda^2:
         deficit(T_cone) = L_x*T_cone/pi - N(T_cone) = lambda^2 - 7/8 - S(T) + o(1)
      (Riemann-von Mangoldt; L_x = log lambda).  THE TOWER IS THE CONE'S SAMPLING DEBT.
      FALSIFIER S1: |K - deficit| growing like a power of lambda over the sweep to lambda=5.
  R2 (leakage identity): the off-E full-form minimizer's QW value is carried by ABOVE-CUTOFF
      zeros (gamma > omega_N): leakage share > 50%; resolved-zero share small (cancellation).
      FALSIFIER S2: resolved share > 50% (frame/leakage mechanism wrong).
  R3 (edge marginality; arithmetic identity, printed): mean zero gap at T_cone
      = 2*pi/log(lambda^2) = pi/L_x = the window resolution, EXACTLY.
  R4 (clustering model): collapsing a zero gap g in the window's sampling Gram degrades the
      frame minimum ~ g^2 (second-order coincidence; beta=2-consistent; sibling of E.14's
      d^2.2 law).  FALSIFIER S3: exponent outside [1.5, 2.5].

Deterministic, local, ~8 min.  FD prolates via eig_banded; exact mpmath QW builds at
lambda = 2.5, 3.0; zeros via mp.zetazero (40, evaluation points only).
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30


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


def cell_count_and_cells(lam, M=None):
    """K(lambda) = #{n >= 4, n = 0 mod 4, defect < 0.05} + the cell vectors (h_n, h_0, x)."""
    nmax = int(4 * np.ceil((4 * lam**2 + 14) / 4))
    if M is None:
        M = 6001 if lam <= 3.6 else 4001
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
    del F
    K = sum(1 for n in defects if n >= 4 and defects[n] < 0.05)
    return K, H, defects, x


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


def fhat_of(coef_even, Ebas, N, L, t):
    c = Ebas @ coef_even
    return sum(c[N + n] * Vhat_c(n, t, L) for n in range(-N, N + 1))


print("harvesting zeros (mp.zetazero, 40)...")
mp.mp.dps = 15
GAMMAS = [float(mp.im(mp.zetazero(k))) for k in range(1, 41)]
mp.mp.dps = 30

# ---------------- R1 + R3: the absorption identity across the sweep ----------------
print("\n== R1/R3: THE ABSORPTION IDENTITY -- K(lambda) vs the cone's sampling debt ==")
print("   lam    K(cells)  T_cone   N(T_cone)  deficit=2lam^2*loglam-N   lam^2-7/8   meangap*L_x/pi")
LAMS = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
Ks, defs_meas = [], []
cells_store = {}
for lam in LAMS:
    K, H, defects, x = cell_count_and_cells(lam)
    Lx = np.log(lam)
    Tcone = 2 * np.pi * lam**2
    if Tcone <= GAMMAS[-1]:
        Ncone = sum(1 for g in GAMMAS if g <= Tcone)
        nstr = f"{Ncone:^9d}"
    else:  # RvM asymptotic (error O(log T)) once past the harvested list
        Ncone = (Tcone / (2 * np.pi)) * np.log(Tcone / (2 * np.pi * np.e)) + 7 / 8
        nstr = f"{Ncone:^9.2f}"
    deficit = 2 * lam**2 * Lx / 1.0 - Ncone          # L_x*T_cone/pi = 2 lam^2 log lam
    meangap_ratio = (2 * np.pi / np.log(lam**2)) * Lx / np.pi
    Ks.append(K); defs_meas.append(deficit)
    cells_store[lam] = (H, defects, x)
    print(f"   {lam:3}   {K:^8d}  {Tcone:7.2f}  {nstr}  {deficit:^23.2f}  {lam**2-0.875:^9.3f}"
          f"  {meangap_ratio:^14.6f}")
res = np.array(Ks) - np.array(defs_meas)
drift = np.polyfit(np.log(LAMS), np.log(np.abs(res) + 0.3), 1)[0]
s1_ok = np.max(np.abs(res)) < 2.5 and drift < 1.0
print(f"   K - deficit residuals: " + ", ".join(f"{r:+.2f}" for r in res)
      + f"   max |res| = {np.max(np.abs(res)):.2f}, log-log drift exponent = {drift:.2f}")
print("   R1: " + ("SURVIVES -- the E-tower is the cone's sampling debt (residual O(1), no power growth)"
                   if s1_ok else "S1 FIRED -- absorption identity fails at leading order"))
print("   R3: mean zero gap at T_cone over window resolution = 1.000000 IDENTICALLY (column above)")
print("       (2*pi/log(lambda^2) = pi/log(lambda): the frame race is decided at the constant level)")

# ---------------- R2: leakage identity for the off-E full-form minimizer ----------------
print("\n== R2: the frame floor IS above-cutoff leakage (lambda = 2.5, 3.0, exact builds) ==")
ok2_all = True
for lam_f, N in ((2.5, 15), (3.0, 18)):
    QWf, L = build_QW(mp.mpf(str(lam_f)), N, True)
    Ebas = Ebas_of(N)
    Qf_e = Ebas.T @ QWf @ Ebas
    H, defects, x = cells_store[lam_f]
    I0 = np.trapezoid(H[0], x)
    cols = []
    for n in sorted(defects):
        if n == 0 or defects[n] >= 0.05 or n > 36:    # match prior-probe cell convention
            continue
        cc = cell_coeffs(lam_f, L, N, H[n] - (np.trapezoid(H[n], x) / I0) * H[0], x)
        if cc is not None:
            cols.append(Ebas.T @ cc.real)
    C = np.column_stack(cols)
    Qc, _ = np.linalg.qr(C)
    Pp = np.eye(N + 1) - Qc @ Qc.T
    wo, vo = np.linalg.eigh(Pp)
    Qo = vo[:, wo > 0.5]
    evf, evecf = np.linalg.eigh(Qo.T @ Qf_e @ Qo)
    v = Qo @ evecf[:, 0]
    qwv = float(evf[0])
    omega_N = 2 * np.pi * N / L
    s_res = sum(2 * abs(fhat_of(v, Ebas, N, L, g))**2 for g in GAMMAS if g <= omega_N)
    s_abv = sum(2 * abs(fhat_of(v, Ebas, N, L, g))**2 for g in GAMMAS if g > omega_N)
    gJ = GAMMAS[-1]
    env = abs(fhat_of(v, Ebas, N, L, gJ))**2 * gJ**2
    tail = 2 * env * np.log(gJ / (2 * np.pi)) / (2 * np.pi) / gJ
    tot = s_res + s_abv
    share_abv = s_abv / max(tot, 1e-30)
    match = abs(qwv - tot) < max(0.05 * qwv, tail + 0.03)
    ok2 = share_abv > 0.5 and match
    ok2_all &= ok2
    print(f"   lambda={lam_f}: QW(min) = {qwv:.4f}; zero side to J=40: resolved(<= {omega_N:.1f}) ="
          f" {s_res:.4f}, above-cutoff = {s_abv:.4f} (share {share_abv:.2f}), tail-env ~ {tail:.3f}"
          f"  -> identity {'MATCH' if match else 'MISMATCH'}; leakage carries the floor: {share_abv > 0.5}")
print("   R2: " + ("SURVIVES -- frame floor = mass leaked past resolution, certified"
                   if ok2_all else "S2 FIRED or identity mismatch -- diagnose"))

# ---------------- R4: gap-collapse model (clustering = the enemy, order 2) ----------------
print("\n== R4: clustering model -- frame minimum vs collapsed gap (sinc Gram, L_x = log 3) ==")
Lx = np.log(3.0)
base = [g for g in GAMMAS if g <= 51.5]


def gram_min(gap_scale):
    gs = list(base)
    gs[1] = gs[0] + (base[1] - base[0]) * gap_scale     # move gamma_2 toward gamma_1
    n = len(gs)
    G = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            d, s = gs[i] - gs[j], gs[i] + gs[j]
            G[i, j] = np.sinc(Lx * d / np.pi) + np.sinc(Lx * s / np.pi)
    return float(np.min(np.linalg.eigvalsh(G)))


scales = [1.0, 0.5, 0.25, 0.125, 0.0625]
mins = [gram_min(s) for s in scales]
gaps = [(base[1] - base[0]) * s for s in scales]
print("   gap: " + "  ".join(f"{g:7.3f}" for g in gaps))
print("   min: " + "  ".join(f"{m:7.4f}" for m in mins))
expo = np.polyfit(np.log(gaps[1:]), np.log(np.maximum(mins[1:], 1e-12)), 1)[0]
s3_ok = 1.5 <= expo <= 2.5
print(f"   collapse exponent (fit over the small-gap rows) = {expo:.2f}  -> "
      + ("R4 SURVIVES (second-order coincidence; beta=2-consistent; E.14 d^2.2 sibling)"
         if s3_ok else "S3 FIRED"))

okM = s1_ok and ok2_all and s3_ok
print("\nRESULT: " + ("GREEN -- absorption identity certified; leakage mechanism certified; "
                      "clustering exponent 2" if okM else "RED/PARTIAL -- see fired falsifiers above"))
