"""probe_pinfF_f4d_division.py -- the F.4.D strike: the zero-constrained division REALIZED.

THEOREM STRUCTURE UNDER TEST (P-inf-F section 10):
  E-cone full-line profiles = zeta(1/2+it) * (shifted Hardy class e^{i L_x t} H^2_-).
  zeta(1/2+it) = B * O, O outer, B = Blaschke of off-line zeros (lower half t-plane):
  division by O is causality-preserving; B == 1 <=> RH; per-window B ~ 1 (verified strip +
  density theorems).  Coverage construction: taper -> divide -> Hardy-truncate -> assemble.
  Predicted error law: dist(phi, E-cone)^2 ~ edge-band zero mass (the F.5'' quantity):
  THE TWO RESIDUES ARE ONE IDENTITY (approximate Plancherel for the E-cone).

PRE-REGISTERED PREDICTIONS (GPD):
  U1 (coverage contrast): the marginal zero-vanishing direction phi_B (vanishes at the 10
      resolved zeros, orthogonal to the 8 cells -- the direction the cell span does NOT
      reach) is covered by the PURE division construction: error <= 0.25 raw (pipeline
      floors included), <= 2x the pipeline floor measured on a cell (target A).  CONTROL:
      the same pipeline on rep_gamma1 (NOT zero-vanishing) fails: error >= 0.7.
      FALSIFIER T1: phi_B error > max(0.35, 3x floor) -- a missing obstruction.
  U2 (the ~ law): injecting edge mass (alpha * rep at gamma_12 = 56.446 > omega_N) makes the
      error grow linearly in alpha, correlation >= 0.97.
      FALSIFIER T2: nonlinearity / no alpha-dependence.
  U3 (causality diagnostic = the inner factor at window scale): out-of-support mass of g
      (beyond y = L_x) <= 5% for zero-vanishing targets; LARGE (>= 25%) for the rep_gamma1
      control (a real-line pole of the quotient dumps half its transform acausally).
      FALSIFIER T3: large acausal mass for vanishing targets (causality obstruction live
      at window scale -- would measure a nontrivial inner factor: escalate immediately).

lambda = 3 (N = 18, L_x = log 3).  Deterministic, local; zeta grid cached. ~4-8 min.
"""
import sys, os
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

LAM, N = 3.0, 18
LX = np.log(LAM)          # half-window in centered x
L = 2 * LX                # probe-convention window length
EBD = None

# ---------- shared machinery (certified lineage) ----------


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


def rep_vector(gam, N, L, Ebas):
    v = np.array([Vhat_c(n, gam, L) for n in range(-N, N + 1)])
    r = np.real(Ebas.T @ v)
    return r / np.linalg.norm(r)


def prolate_modes(lam, nmax, M=6001):
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
    return x, H, defects


def E_assemble_coeffs(lam_f, L, N, wgrid, hvals):
    """E(h) restricted to the window, as even-space coefficients (normalized)."""
    xg = np.linspace(0.0, L, 3001)
    u = np.exp(xg - L / 2)
    kl = np.zeros_like(u)
    nmaxsum = int(lam_f / u.min()) + 2
    for n in range(1, nmaxsum):
        msk = n * u <= lam_f
        kl[msk] += np.interp(n * u[msk], wgrid, hvals, left=0.0, right=0.0)
    kl *= np.sqrt(u)
    nrm = np.sqrt(np.trapezoid(kl * kl, xg))
    if nrm < 1e-12:
        return None
    kl /= nrm
    cc = np.array([np.trapezoid(kl * np.exp(-2j * np.pi * n * xg / L) / np.sqrt(L), xg)
                   for n in range(-N, N + 1)])
    return cc


Ebas = Ebas_of(N)
print("harvesting zeros (20)...")
mp.mp.dps = 15
GAM = [float(mp.im(mp.zetazero(k))) for k in range(1, 21)]
mp.mp.dps = 30
OMEGA = 2 * np.pi * N / L
RES = [g for g in GAM if g <= OMEGA]          # 10 resolved zeros
print(f"   omega_N = {OMEGA:.2f}; resolved = {len(RES)}; gamma_11 = {GAM[10]:.3f}, gamma_12 = {GAM[11]:.3f}")

# ---------- zeta on the t-grid (cached) ----------
TG, DT = 120.0, 0.03
ts = np.arange(-TG, TG + DT / 2, DT)
cache = "empirical/p_infinity/f4d_zeta_grid.npy"
if os.path.exists(cache):
    zline = np.load(cache)
else:
    print(f"computing zeta(1/2+it) on {len(ts)} grid points (dps 10)...")
    mp.mp.dps = 10
    zline = np.array([complex(mp.zeta(mp.mpc(0.5, t))) for t in ts])
    mp.mp.dps = 30
    np.save(cache, zline)

# taper: 1 on |t|<=50, cos^2 roll to 0 on [50,55]
W = np.ones_like(ts)
m1 = np.abs(ts) > 50; m2 = np.abs(ts) >= 55
W[m1] = np.cos(np.pi / 2 * (np.abs(ts[m1]) - 50) / 5)**2
W[m2] = 0.0

VHg = VH_on_grid(N, L, ts)

# ---------- targets ----------
x_p, Hp, defp = prolate_modes(LAM, 36)
I0 = np.trapezoid(Hp[0], x_p)
cells = []
for n in sorted(defp):
    if n == 0 or defp[n] >= 0.05:
        continue
    wg = x_p[x_p >= 0]
    hv = (Hp[n] - (np.trapezoid(Hp[n], x_p) / I0) * Hp[0])[x_p >= 0]
    cc = E_assemble_coeffs(LAM, L, N, wg, hv)
    cells.append(np.real(Ebas.T @ cc))
C = np.column_stack([c / np.linalg.norm(c) for c in cells])
Qc, _ = np.linalg.qr(C)

R = np.column_stack([rep_vector(g, N, L, Ebas) for g in RES])     # constraint rows
U_, s_, Vt_ = np.linalg.svd(R.T, full_matrices=True)
V0 = Vt_[len(RES):, :].T                                          # zero-vanishing subspace (dim 9)
M_perp = V0 - Qc @ (Qc.T @ V0)
Uu, ss, _ = np.linalg.svd(M_perp, full_matrices=False)
phiB = Uu[:, 0]
print(f"   vanishing-subspace dim = {V0.shape[1]}; sing.vals of (I-P_cells)V0: "
      + ", ".join(f"{v:.3f}" for v in ss[:4]) + "  -> marginal directions beyond cells")
repE = rep_vector(GAM[11], N, L, Ebas)                            # gamma_12 edge injector
rep1 = rep_vector(GAM[0], N, L, Ebas)                             # control target


def divide_and_build(cvec, label):
    """The construction: profile -> taper -> /zeta -> g(y) -> Hardy truncate -> h -> E h."""
    Phi = (Ebas @ cvec) @ VHg                                     # profile on grid
    G = Phi * W / zline
    yg = np.arange(-14.0, LX + 0.005, 0.01)
    ph = np.exp(-1j * np.outer(ts, yg))
    g = (G[:, None] * ph).sum(axis=0) * DT / (2 * np.pi)          # g(y) on y <= L_x
    # causality diagnostic: mass beyond y = L_x (extend grid upward)
    yg_hi = np.arange(LX + 0.01, LX + 6.0, 0.01)
    ph2 = np.exp(-1j * np.outer(ts, yg_hi))
    g_hi = (G[:, None] * ph2).sum(axis=0) * DT / (2 * np.pi)
    m_in = np.trapezoid(np.abs(g)**2, yg)
    m_out = np.trapezoid(np.abs(g_hi)**2, yg_hi)
    acausal = m_out / (m_in + m_out)
    # h(w) = g(log w) w^{-1/2}, real part; vanishing-integral correction with FD h0
    wgrid = np.exp(yg)
    hv = np.real(g) * wgrid**(-0.5)
    Ih = np.trapezoid(hv, wgrid)
    h0i = np.interp(wgrid, x_p[x_p >= 0], Hp[0][x_p >= 0], left=Hp[0][len(x_p)//2], right=0.0)
    hv = hv - (Ih / I0) * h0i
    cc = E_assemble_coeffs(LAM, L, N, wgrid, hv)
    if cc is None:
        return 1.0, acausal
    e = np.real(Ebas.T @ cc); e /= np.linalg.norm(e)
    t = cvec / np.linalg.norm(cvec)
    err = np.sqrt(max(0.0, 1 - float(e @ t)**2))                  # sine of the angle
    print(f"   {label:34s} error = {err:.4f}   acausal mass of g = {acausal:.4f}")
    return err, acausal


print("\n== U1/U3: the construction on the four targets ==")
errA, acA = divide_and_build(Qc[:, 0], "A: first cell (pipeline floor)")
errB, acB = divide_and_build(phiB, "B: marginal vanishing direction")
err1, ac1 = divide_and_build(rep1, "CONTROL: rep_gamma1 (no vanishing)")
print(f"   contrast: phi_B {errB:.3f} vs control {err1:.3f}; floor {errA:.3f}")
u1 = errB <= max(0.35, 3 * errA) and err1 >= 0.7
u3 = acB <= 0.05 and acA <= 0.05 and ac1 >= 0.25

print("\n== U2: error vs injected edge mass (alpha * rep_gamma12) ==")
alphas = [0.0, 0.1, 0.2, 0.4]
errs = []
for a in alphas:
    cv = phiB + a * repE
    cv /= np.linalg.norm(cv)
    e, _ = divide_and_build(cv, f"B + {a:.1f}*edge(gamma_12)")
    errs.append(e)
de = np.array(errs) - errs[0]
fit = np.polyfit(alphas[1:], de[1:], 1)
corr = np.corrcoef(alphas[1:], de[1:])[0, 1] if np.std(de[1:]) > 1e-9 else 0.0
u2 = corr >= 0.97 and fit[0] > 0
print(f"   slope = {fit[0]:.3f}, corr = {corr:.4f}")

print("\n== VERDICTS (pre-registered) ==")
print(f"   U1 coverage contrast: {'SURVIVES' if u1 else 'T1 FIRED'}"
      f"  (B err {errB:.3f} vs floor {errA:.3f} vs control {err1:.3f})")
print(f"   U2 edge-mass linearity: {'SURVIVES' if u2 else 'T2 FIRED'} (corr {corr:.3f})")
print(f"   U3 causality diagnostic: {'SURVIVES' if u3 else 'T3 FIRED'}"
      f"  (acausal: cell {acA:.3f}, B {acB:.3f}, control {ac1:.3f})")
print("\nRESULT: " + ("GREEN -- division construction realized; error law and causality as"
                      " predicted" if (u1 and u2 and u3) else
                      "PARTIAL/RED -- diagnose fired falsifiers (criterion vs mathematics)"))
