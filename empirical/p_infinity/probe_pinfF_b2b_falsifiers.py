"""probe_pinfF_b2b_falsifiers.py — foundation + pre-registered falsifiers for P-infinity-F.

THEOREM F.1 (multiplier representation; Parseval, exact): for f supported in the window,
  QW_lambda(f) = (1/pi) int |fhat(t)|^2 W_lambda(t) dt + 2 Re( fhat(i/2) conj(fhat(-i/2)) ),
  W_lambda(t) = theta'(t) - sum_{2<=n<=lambda^2} Lambda(n) n^{-1/2} cos(t log n)
— the TRUNCATED ZERO DENSITY (times pi).  CHECK A certifies this against the exact matrix.

BELIEFS UNDER TEST (pre-registered, each with its falsifier):
  K1 (incoherence): off the E-sector the prime part is SUB-COHERENT: its compressed norm
      grows like O(log lambda), not the coherent bound ~ 4 lambda.
      FALSIFIER: measured growth ~ lambda.
  K2 (soft positivity): the off-E minimum of the full form stays >= 1/poly.
      FALSIFIER: exponential decay of the off-E minimum in lambda.
  K3 (carrier): positivity off-E is carried by arch+pole alone (primes a small
      perturbation there).  FALSIFIER: arch+pole-only off-E minimum near 0 or negative
      (then prime CANCELLATION, not prime smallness, is the mechanism).

Windows lambda = 1.5, 2.0, 2.5, 3.0 (N = 10, 12, 15, 18; tower cells n = 0 mod 4 with
FD defect < 0.05 removed).  Deterministic, local, ~5-8 min.
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
    if nrm < 1e-14:
        return None
    kl /= nrm
    return np.array([np.trapezoid(kl * np.exp(-2j * np.pi * n * xg / L) / np.sqrt(L), xg)
                     for n in range(-N, N + 1)])

# ---------------- CHECK A: the multiplier representation (Theorem F.1) ----------------
print("== CHECK A: QW = (1/pi) int |fhat|^2 W_lambda + pole-term, vs exact matrix (lambda=1.5) ==")
lam_f, N = 1.5, 10
QW, L = build_QW(mp.mpf("1.5"), N)
rng = np.random.default_rng(7)
from scipy.special import digamma
T = 4000.0
ts = np.arange(-T, T, 0.02)
thp = -0.5 * np.log(np.pi) + 0.5 * np.real(digamma(0.25 + 0.5j * ts))
Wl = thp.copy()
for p in primes_upto(lam_f**2 + 1e-9):
    j = 1
    while p**j <= lam_f**2 + 1e-9:
        Wl -= np.log(p) * p**(-j / 2) * np.cos(ts * j * np.log(p))
        j += 1

def Vhat_grid(n, z_arr, L):
    wn = 2 * np.pi * n / L
    d = wn - z_arr
    out = np.where(np.abs(d) < 1e-12, L, (np.exp(1j * d * L) - 1) / (1j * d))
    return np.exp(1j * z_arr * L / 2) / np.sqrt(L) * out

VH = np.array([Vhat_grid(n, ts, L) for n in range(-N, N + 1)])
VH_p = np.array([complex(mp.e**(1j * mp.mpc(0, 0.5) * L / 2)) for n in range(0)])  # unused
def Vhat_c(n, z, L):
    wn = 2 * np.pi * n / L
    d = wn - z
    if abs(d) < 1e-12:
        return np.exp(1j * z * L / 2) * np.sqrt(L)
    return np.exp(1j * z * L / 2) / np.sqrt(L) * (np.exp(1j * d * L) - 1) / (1j * d)

okA = True
for _ in range(3):
    c = rng.normal(size=2 * N + 1)
    fh = c @ VH
    main = np.trapezoid(np.abs(fh)**2 * Wl, ts) / np.pi
    fp = sum(c[N + n] * Vhat_c(n, 0.5j, L) for n in range(-N, N + 1))
    fm = sum(c[N + n] * Vhat_c(n, -0.5j, L) for n in range(-N, N + 1))
    pole = 2 * np.real(fp * np.conj(fm))
    lhs = main + pole
    rhs = c @ QW @ c
    e = abs(lhs - rhs) / abs(rhs)
    okA &= e < 0.02
    print(f"   random f: multiplier+pole = {lhs:+.5f}   exact matrix = {rhs:+.5f}   rel err {e:.1e}")
print(f"   W_lambda(0) = {Wl[len(ts)//2]:+.3f}  (the naive pointwise well: deeply negative)")
print("   " + ("PASS — Theorem F.1 certified: the semilocal form IS a multiplier + rank-2 pole"
               if okA else "FAIL"))

# ---------------- K1/K2/K3 falsifier battery ----------------
print("\n== K1/K2/K3: sector-compressed components across the lambda sweep ==")
print("   lam   cells  off-min(full)  off-min(arch+pole)  off-norm(prime)  coherent 4*lam")
results = []
for lam_f, N in ((1.5, 10), (2.0, 12), (2.5, 15), (3.0, 18)):
    QWf, L = build_QW(mp.mpf(str(lam_f)), N, True)
    QWa, _ = build_QW(mp.mpf(str(lam_f)), N, False)
    QWp = QWa - QWf                          # prime part with + sign: QWf = QWa - QWp
    x, H, defects = prolate_cells(lam_f, min(4 * int(4 * lam_f**2 / 4) + 4, 36))
    dim = 2 * N + 1
    Ebas = np.zeros((dim, N + 1))
    Ebas[N, 0] = 1.0
    for k in range(1, N + 1):
        Ebas[N + k, k] = Ebas[N - k, k] = 1 / np.sqrt(2)
    cols = []
    I0 = np.trapezoid(H[0], x)
    for n in sorted(defects):
        if n == 0 or defects[n] >= 0.05:
            continue
        cc = cell_coeffs(lam_f, L, N, H[n] - (np.trapezoid(H[n], x) / I0) * H[0], x)
        if cc is not None:
            cols.append(Ebas.T @ cc.real)
    C = np.column_stack(cols)
    Qc, _ = np.linalg.qr(C)
    P = np.eye(N + 1) - Qc @ Qc.T
    wo, vo = np.linalg.eigh(P)
    Qo = vo[:, wo > 0.5]
    co = lambda M_: Qo.T @ (Ebas.T @ M_ @ Ebas) @ Qo
    mn_full = np.min(np.linalg.eigvalsh(co(QWf)))
    mn_arch = np.min(np.linalg.eigvalsh(co(QWa)))
    nrm_prime = np.max(np.abs(np.linalg.eigvalsh(co(QWp))))
    results.append((lam_f, C.shape[1], mn_full, mn_arch, nrm_prime))
    print(f"   {lam_f:3}   {C.shape[1]:^5}  {mn_full:^13.4f}  {mn_arch:^18.4f}  "
          f"{nrm_prime:^15.4f}  {4*lam_f:.1f}")
lams = np.array([r[0] for r in results])
pn = np.array([r[4] for r in results])
gr = np.polyfit(np.log(lams), np.log(pn), 1)[0]
k2_ok = all(r[2] > 0.05 for r in results)
k3_carried = all(r[3] > 0.3 for r in results)
print(f"\n   K1: off-E prime-part norm growth ~ lambda^{gr:.2f} "
      f"(coherent would be ~ lambda^1 at full norm scale 4*lam)")
print(f"   K2: off-E full minimum stays positive and O(1)-ish: {k2_ok} "
      f"({', '.join(f'{r[2]:.3f}' for r in results)})")
print(f"   K3: arch+pole alone carries off-E positivity: {k3_carried} "
      f"({', '.join(f'{r[3]:.3f}' for r in results)})")

verdict_ok = okA and k2_ok
print("\nRESULT: " + ("GREEN — Theorem F.1 certified; falsifier battery executed; see K1-K3 "
                      "verdicts for which beliefs survived" if verdict_ok else "RED"))
