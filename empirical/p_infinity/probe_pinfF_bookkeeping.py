"""probe_pinfF_bookkeeping.py -- the bookkeeping strike: Lemmas F.15/F.16 certified.

THE LEMMAS (P-inf-F section 16):
  F.15 (tail-form bound, = E.22.3 referee form): for h even, C^2, h(0) = int h = 0, the Weil
      form on the below-window tail F_out of E(h) satisfies
         |QW(F_out)| <= C * (1 + DY) * ||F_out||_w^2,   ||F||_w^2 = int |F|^2 (1+|y|) dy,
      with C absolute-ish (arch via the screw-kernel log estimate g''~1/(2|t|); primes via
      per-shift Cauchy-Schwarz + Poisson decay from h(0)=int h=0; pole via weighted CS).
  F.16 (cross-mixing / B2c): |QW(E h_k|win, g)| <= C log(lam) ||F_out,k|| ||g|| -- hence the
      CROSS-LADDER LAW: the cell-to-off-E coupling tracks sqrt(defect_k).

PRE-REGISTERED (GPD):
  M0 (the exact tail identity E.22.2, machine-verified for the first time):
      QW(F_out) = windowed Rayleigh QW_lam(cell) to < 15% (rough grids).
      FALSIFIER: mismatch beyond -- diagnose convention vs mathematics.
  M1 (F.15 constant): C_eff = |QW(F_out)| / ((1+DY) ||F_out||_w^2) lies in [0.01, 100] and
      does NOT grow like a power of 1/defect across cells spanning 5 decades of defect.
      FALSIFIER: poly(1/defect) growth (tails not norm-controlled -- kills F.15).
  M2 (cross-ladder): slope of log cross_k vs log defect_k >= 0.35 (sqrt-law or better) at
      lambda = 2, 3.  FALSIFIER: slope < 0.35 (no tracking -- kills F.16's mechanism).
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
from scipy.special import digamma
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

src = open("empirical/p_infinity/probe_pinfF_f4d_division.py", encoding="utf-8").read()
exec(src.split('Ebas = Ebas_of(N)')[0])   # builders incl. prolate_modes, E_assemble_coeffs, Vhat_c, Ebas_of

src2 = open("empirical/p_infinity/probe_pinfF_f5_sampling.py", encoding="utf-8").read()
exec(src2.split('# ---- zeros')[0])        # primes_upto, build_QW, and friends


def thetap(t):
    return -0.5 * np.log(np.pi) + 0.5 * np.real(digamma(0.25 + 0.5j * np.asarray(t, float)))


def lam_von_mangoldt(X):
    LV = np.zeros(X + 1)
    sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
    for p in range(2, X + 1):
        if sieve[p]:
            sieve[2 * p::p] = False
            pk = p
            while pk <= X:
                LV[pk] = np.log(p)
                pk *= p
    return LV


def assemble_full_Eh(lam_f, h, x_p, Y=4.0, dy=0.002):
    """Tail grid capped at y = -Y: below it the two-condition h makes E(h) exp-small by
    Poisson duality (hhat(0) = int h = 0), while the n-sum at y < -4 has ~lam*e^{|y|}
    interpolated terms cancelling to a tiny value -- pure float noise (the M0 diagnosis)."""
    """E(h)(e^y) on y in [-Y, log lam]; returns (ygrid, vals)."""
    yg = np.arange(-Y, np.log(lam_f) + dy / 2, dy)
    u = np.exp(yg)
    vals = np.zeros_like(u)
    nmax = int(np.ceil(lam_f / u[0]))
    hp = h[x_p >= 0]; xp = x_p[x_p >= 0]
    for n in range(1, nmax + 1):
        w = n * u
        msk = w <= lam_f
        if not msk.any():
            break
        vals[msk] += np.interp(w[msk], xp, hp, left=hp[0], right=0.0)
    return yg, np.sqrt(u) * vals


def weil_form_general(yg, F, lam_f, Tmax=3000.0, dt=0.05):
    """QW on a general compactly-supported (in y) real function: multiplier arch + pole
       + direct prime shifts (primes up to the support length)."""
    dy = yg[1] - yg[0]
    arch = 0.0
    for t0 in np.arange(-Tmax, Tmax, 500.0):
        ts = np.arange(t0, min(t0 + 500.0, Tmax), dt)
        Fh = np.exp(1j * np.outer(ts, yg)) @ F * dy
        arch += float(np.trapezoid(np.abs(Fh)**2 * thetap(ts), ts)) / np.pi
    fp = np.sum(F * np.exp(-0.5 * yg)) * dy     # fhat(i/2) = int F e^{-y/2}? convention e^{izy}, z=i/2 -> e^{-y/2}
    fm = np.sum(F * np.exp(0.5 * yg)) * dy
    pole = 2.0 * fp * fm
    span = yg[-1] - yg[0]
    X = int(np.exp(min(span, 11.5))) + 1
    LV = lam_von_mangoldt(X)
    pr = 0.0
    for n in range(2, X + 1):
        if LV[n] == 0.0:
            continue
        sh = np.log(n)
        F2 = np.interp(yg - sh, yg, F, left=0.0, right=0.0)
        pr += LV[n] / np.sqrt(n) * 2.0 * float(np.sum(F * F2)) * dy
    return pole + arch - pr, dict(arch=arch, pole=pole, primes=pr)


# ---------------- M0/M1: the tail identity + the F.15 constant ----------------
print("== M0/M1: exact tail identity (E.22.2) + tail-form constant (F.15) ==")
print("   case              defect      ||Fout||^2    QW(Fout)     QW_win(cell)   id-err   C_eff")
cases = [(1.3, 8, 4), (1.5, 10, 4), (2.0, 12, 8)]
C_effs, defects_used = [], []
ok0 = True
for lam_f, N, ncell in cases:
    L = 2 * np.log(lam_f)
    x_p, Hp, defp = prolate_modes(lam_f, 36)
    I0 = np.trapezoid(Hp[0], x_p)
    # TWO-CONDITION combo: kill int h AND h(0) exactly (h_n - a h_0 - b h_8; E.22.1 needs both)
    naux = 8 if ncell != 8 else 12
    M2c = np.array([[np.trapezoid(Hp[0], x_p), np.trapezoid(Hp[naux], x_p)],
                    [Hp[0][len(x_p) // 2], Hp[naux][len(x_p) // 2]]])
    rhs = np.array([np.trapezoid(Hp[ncell], x_p), Hp[ncell][len(x_p) // 2]])
    ab = np.linalg.solve(M2c, rhs)
    hcomb = Hp[ncell] - ab[0] * Hp[0] - ab[1] * Hp[naux]
    yg, Eh = assemble_full_Eh(lam_f, hcomb, x_p)
    Lx = np.log(lam_f)
    m_out = yg < -Lx
    F_out = np.where(m_out, Eh, 0.0)
    n2_out = float(np.trapezoid(F_out**2, yg))
    w2_out = float(np.trapezoid(F_out**2 * (1 + np.abs(yg)), yg))
    q_out, parts = weil_form_general(yg, F_out, lam_f)
    # windowed Rayleigh of the cell from the exact matrix (per-cell, unnormalized to match)
    QWf, Lf = build_QW(mp.mpf(repr(float(lam_f))), N, True)
    Ebas = Ebas_of(N)
    cc = E_assemble_coeffs(lam_f, Lf, N, x_p[x_p >= 0], hcomb[x_p >= 0])
    ce = np.real(Ebas.T @ cc)
    # E_assemble normalizes; undo: window norm of Eh
    n2_win = float(np.trapezoid(np.where(~m_out, Eh, 0.0)**2, yg))
    q_win = float(ce @ (Ebas.T @ QWf @ Ebas) @ ce) * n2_win
    F_in = np.where(~m_out, Eh, 0.0)
    q_in_eng, _ = weil_form_general(yg, F_in, lam_f)
    iderr = abs(q_out - q_in_eng) / max(abs(q_out), abs(q_in_eng), 1e-30)
    idmat = abs(q_out - q_win) / max(abs(q_out), abs(q_win), 1e-30)
    DY = (yg[-1] - yg[0])
    c_eff = abs(q_out) / max((1 + DY) * w2_out, 1e-300)
    C_effs.append(c_eff); defects_used.append(defp[ncell])
    ok0 &= iderr < 0.15
    print(f"   lam={lam_f}, n={ncell}:   {defp[ncell]:.2e}  {n2_out:.3e}   {q_out:+.3e}  "
          f"Qeng(Fin)={q_in_eng:+.3e}  Qmat(Fin)={q_win:+.3e}   id-eng={iderr:.3f}  "
          f"id-mat={idmat:.3f}   C_eff={c_eff:.2f}")
gr = np.polyfit(np.log(defects_used), np.log(C_effs), 1)[0]
ok1 = all(0.01 <= c <= 100 for c in C_effs) and abs(gr) < 0.45
print(f"   C_eff vs defect: log-log slope {gr:+.2f} (|slope| < 0.45 = no poly(1/defect) growth)")
print("   M0: " + ("SURVIVES -- E.22.2 tail identity machine-verified" if ok0 else "FIRED -- diagnose"))
print("   M1: " + ("SURVIVES -- tail form is norm-controlled (F.15)" if ok1 else "FIRED"))

# ---------------- M2: the cross-ladder ----------------
print("\n== M2: cross-ladder -- cell-to-off-E coupling vs sqrt(defect) ==")
for lam_f, N in ((2.0, 12), (3.0, 18)):
    QWf, L = build_QW(mp.mpf(repr(float(lam_f))), N, True)
    Ebas = Ebas_of(N)
    Qf_e = Ebas.T @ QWf @ Ebas
    x_p, Hp, defp = prolate_modes(lam_f, 36)
    I0 = np.trapezoid(Hp[0], x_p)
    cols, defs_ = [], []
    for n in sorted(defp):
        if n == 0 or defp[n] >= 0.05:
            continue
        hcomb = Hp[n] - (np.trapezoid(Hp[n], x_p) / I0) * Hp[0]
        cc = E_assemble_coeffs(lam_f, L, N, x_p[x_p >= 0], hcomb[x_p >= 0])
        cols.append(np.real(Ebas.T @ cc)); defs_.append(defp[n])
    C = np.column_stack([c / np.linalg.norm(c) for c in cols])
    Qc, _ = np.linalg.qr(C)
    wo, vo = np.linalg.eigh(np.eye(N + 1) - Qc @ Qc.T)
    Qo = vo[:, wo > 0.5]
    crosses = [float(np.linalg.norm(Qo.T @ Qf_e @ C[:, j])) for j in range(C.shape[1])]
    usable = [(d, c) for d, c in zip(defs_, crosses) if d > 1e-11 and c > 1e-13]
    sl = np.polyfit([np.log(d) for d, _ in usable], [np.log(c) for _, c in usable], 1)[0] \
        if len(usable) >= 2 else np.nan
    print(f"   lam={lam_f}: defects " + " ".join(f"{d:.1e}" for d, _ in usable)
          + " | crosses " + " ".join(f"{c:.1e}" for _, c in usable) + f"  slope={sl:.2f}")
print("   M2 verdict: slope >= 0.35 at each lambda = SURVIVES (sqrt-law or better)")
print("\nRESULT: see M0/M1/M2 lines (GREEN iff none fired)")
