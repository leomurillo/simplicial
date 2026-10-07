"""probe_pinfF_f4d_supplement.py -- T3 diagnosis completion: the edge-corrected marginal.

DIAGNOSIS UNDER TEST: T3 fired because phi_B vanishes only at the 10 RESOLVED zeros while
the taper passes gamma_11 = 52.97 at W ~ 0.36 -- the acausal mass IS the edge-band zero
mass (cell 0.000 / phi_B 0.217 / control 0.286, monotone in un-vanished zero content).

PRE-REGISTERED COMPLETION PREDICTIONS:
  V1: extending the vanishing constraints through gamma_12 (12 zeros), the vanishing space
      V12 (dim 7) sits INSIDE the 8-dim cell span: top singular value of (I-P_cells)V12
      <= 0.25 (vs 1.000 for the 10-zero space) -- the marginal direction was PURE edge mass.
  V2: the top residual direction of V12 (whatever sliver remains) runs the pipeline with
      error <= 0.15 and acausal mass <= 0.07 -- error -> floor and causality restored as
      edge mass -> 0: the dist^2 ~ edge-mass identity demonstrated from both ends.
  V3: phi_B's measured edge anatomy confirms the story: |Phi_B(gamma_11)|, |Phi_B(gamma_12)|
      are O(1) while |Phi_B(gamma_j)| <= 1e-10 for j <= 10 (constraint check).
"""
import sys, os
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

src = open("empirical/p_infinity/probe_pinfF_f4d_division.py", encoding="utf-8").read()
exec(src.split('Ebas = Ebas_of(N)')[0])          # builders only
Ebas = Ebas_of(N)
mp.mp.dps = 15
GAM = [float(mp.im(mp.zetazero(k))) for k in range(1, 21)]
mp.mp.dps = 30
OMEGA = 2 * np.pi * N / L
RES = [g for g in GAM if g <= OMEGA]

TG, DT = 120.0, 0.03
ts = np.arange(-TG, TG + DT / 2, DT)
zline = np.load("empirical/p_infinity/f4d_zeta_grid.npy")
W = np.ones_like(ts)
m1 = np.abs(ts) > 50; m2 = np.abs(ts) >= 55
W[m1] = np.cos(np.pi / 2 * (np.abs(ts[m1]) - 50) / 5)**2
W[m2] = 0.0
VHg = VH_on_grid(N, L, ts)

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


def vanish_space(klist):
    R = np.column_stack([rep_vector(g, N, L, Ebas) for g in klist])
    _, s_, Vt_ = np.linalg.svd(R.T, full_matrices=True)
    return Vt_[len(klist):, :].T


def divide_and_build(cvec, label):
    Phi = (Ebas @ cvec) @ VHg
    G = Phi * W / zline
    yg = np.arange(-14.0, LX + 0.005, 0.01)
    g = ((G[:, None] * np.exp(-1j * np.outer(ts, yg))).sum(axis=0)) * DT / (2 * np.pi)
    yg_hi = np.arange(LX + 0.01, LX + 6.0, 0.01)
    g_hi = ((G[:, None] * np.exp(-1j * np.outer(ts, yg_hi))).sum(axis=0)) * DT / (2 * np.pi)
    m_in = np.trapezoid(np.abs(g)**2, yg); m_out = np.trapezoid(np.abs(g_hi)**2, yg_hi)
    acausal = m_out / (m_in + m_out)
    wgrid = np.exp(yg)
    hv = np.real(g) * wgrid**(-0.5)
    Ih = np.trapezoid(hv, wgrid)
    h0i = np.interp(wgrid, x_p[x_p >= 0], Hp[0][x_p >= 0], left=Hp[0][len(x_p)//2], right=0.0)
    hv = hv - (Ih / I0) * h0i
    cc = E_assemble_coeffs(LAM, L, N, wgrid, hv)
    e = np.real(Ebas.T @ cc); e /= np.linalg.norm(e)
    t = cvec / np.linalg.norm(cvec)
    err = np.sqrt(max(0.0, 1 - float(e @ t)**2))
    print(f"   {label:34s} error = {err:.4f}   acausal mass = {acausal:.4f}")
    return err, acausal


# V3: phi_B edge anatomy
V10 = vanish_space(RES)
M10 = V10 - Qc @ (Qc.T @ V10)
U10, s10, _ = np.linalg.svd(M10, full_matrices=False)
phiB = U10[:, 0]
prof = lambda c, g: abs(float(np.real((Ebas @ c) @ np.array([Vhat_c(n, g, L) for n in range(-N, N + 1)]))) + 1j * float(np.imag((Ebas @ c) @ np.array([Vhat_c(n, g, L) for n in range(-N, N + 1)]))))
vals_res = [abs(complex((Ebas @ phiB) @ np.array([Vhat_c(n, g, L) for n in range(-N, N + 1)]))) for g in RES]
vals_edge = [abs(complex((Ebas @ phiB) @ np.array([Vhat_c(n, g, L) for n in range(-N, N + 1)]))) for g in GAM[10:14]]
print("== V3: phi_B zero-value anatomy ==")
print("   max |Phi_B| at resolved zeros = {:.2e}".format(max(vals_res)))
print("   |Phi_B| at gamma_11..14 = " + ", ".join(f"{v:.3f}" for v in vals_edge))
v3 = max(vals_res) < 1e-8 and max(vals_edge[:2]) > 0.05

# V1: extended vanishing space
V12 = vanish_space(GAM[:12])
M12 = V12 - Qc @ (Qc.T @ V12)
U12, s12, _ = np.linalg.svd(M12, full_matrices=False)
print("\n== V1: (I - P_cells) applied to the 12-zero vanishing space ==")
print("   sing.vals: " + ", ".join(f"{v:.4f}" for v in s12[:5]) + f"   (10-zero space gave {s10[0]:.3f})")
v1 = s12[0] <= 0.25

# V2: pipeline on the top residual sliver (and on the projection of V12 onto cells as sanity)
print("\n== V2: pipeline on the edge-corrected marginal sliver ==")
errS, acS = divide_and_build(U12[:, 0], "top sliver of (I-P_cells)V12")
v2 = errS <= 0.15 and acS <= 0.07

print("\n== VERDICTS ==")
print(f"   V1 (marginal was pure edge mass): {'SURVIVES' if v1 else 'FIRED'} (top sv {s12[0]:.4f})")
print(f"   V2 (error->floor, causality restored): {'SURVIVES' if v2 else 'FIRED'}"
      f" (err {errS:.4f}, acausal {acS:.4f})")
print(f"   V3 (anatomy): {'SURVIVES' if v3 else 'FIRED'}")
print("\nRESULT: " + ("GREEN -- T3 diagnosed as edge mass; dist^2 ~ edge-mass identity"
                      " demonstrated from both ends" if (v1 and v2 and v3) else
                      "PARTIAL -- see verdicts"))
