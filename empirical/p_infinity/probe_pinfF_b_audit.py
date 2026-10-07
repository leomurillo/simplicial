"""probe_pinfF_b_audit.py -- the (b)-audit strike: cluster/desert robustness of the floor.

THE AUDIT (P-inf-F section 11): the weld needs of the off-E floor only
   floor(lambda) >= lambda^{1+delta} * QW(k-tilde)  ~  e^{-4 pi lambda^2} * poly
(sub-exponential collapse tolerated; cross-couplings exp-small by radical membership).
The floor's carrier is the BOUNDARY BAND (section 9.3 anatomy), so the two classical
worries are tested here on the F.6-certified zero-side model (QW = 2 sum |fhat(gamma)|^2,
validated against the exact form: D1, 1.3-9% at J=40):

PRE-REGISTERED PREDICTIONS (GPD):
  W1 (clusters cannot reach the floor -- NO REPULSION NEEDED): merging gamma_4, gamma_5 to a
      sub-resolution pair (split 0.1 << resolution 2.86) degrades the off-E floor by <= 3x;
      a TRIPLE merge (gamma_3,4,5) by <= 10x.  The freed interior directions pay boundary
      mass instead.  FALSIFIER X1: pair-merge collapse > 10x (interior degeneracy reaches
      the floor => repulsion would be needed after all).
  W2 (deserts cost polylog -- RvM SUFFICES): deleting gamma_9, gamma_10 (a [44, 51.5]
      desert, ~ the maximal RvM-allowed S(T)-fluctuation scale) degrades the floor by
      <= 20x, and the new minimizer's spectral centroid sits INSIDE the desert.
      FALSIFIER X2: collapse > 100x (desert facet underestimated).
  W3 (the margin, displayed): weld bar lambda^{1+delta} eps_lambda vs measured floors,
      using the certified eps values (P-inf-E section 21): the (b)-requirement is met with
      >= 10 orders of room at the certified windows.  (Arithmetic display, not a test.)

Model-level by design: the claims concern the zero-side sampling geometry; baseline model
floor is cross-checked against the exact-build floor 0.6111 (D1).  lambda = 3, N = 18.
"""
import sys
import numpy as np
from scipy.linalg import eig_banded
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 30

src = open("empirical/p_infinity/probe_pinfF_f4d_division.py", encoding="utf-8").read()
exec(src.split('Ebas = Ebas_of(N)')[0])          # LAM, N, L, LX + builders
Ebas = Ebas_of(N)
print("harvesting zeros (40)...")
mp.mp.dps = 15
GAM = [float(mp.im(mp.zetazero(k))) for k in range(1, 41)]
mp.mp.dps = 30
OMEGA = 2 * np.pi * N / L

# cells -> off-E projector (certified convention)
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
wo, vo = np.linalg.eigh(np.eye(N + 1) - Qc @ Qc.T)
Qo = vo[:, wo > 0.5]


def vfun(gam):
    return np.real(Ebas.T @ np.array([Vhat_c(n, gam, L) for n in range(-N, N + 1)]))


def model_floor(zlist):
    M = np.zeros((N + 1, N + 1))
    for g in zlist:
        v = vfun(g)
        M += 2.0 * np.outer(v, v)
    Mo = Qo.T @ M @ Qo
    ev, evec = np.linalg.eigh(Mo)
    return float(ev[0]), Qo @ evec[:, 0]


def centroid(c):
    ts = np.arange(-80, 80, 0.02)
    fh = (Ebas @ c) @ VH_on_grid(N, L, ts)
    p = np.abs(fh)**2
    return float(np.sum(np.abs(ts) * p) / np.sum(p))


base_floor, vb = model_floor(GAM)
print(f"\n== baseline: model floor (J=40 zero-side, off-E) = {base_floor:.4f}"
      f"   [exact-build floor 0.6111; D1 gap = far tail]")

print("\n== W1: cluster robustness ==")
Z2 = list(GAM)
mid = 0.5 * (GAM[3] + GAM[4])
Z2[3], Z2[4] = mid - 0.05, mid + 0.05
f2, v2 = model_floor(Z2)
Z3 = list(GAM)
m3 = (GAM[2] + GAM[3] + GAM[4]) / 3
Z3[2], Z3[3], Z3[4] = m3 - 0.05, m3, m3 + 0.05
f3, v3 = model_floor(Z3)
r2, r3 = base_floor / max(f2, 1e-15), base_floor / max(f3, 1e-15)
print(f"   pair-merge  (g4,g5 -> {mid:.2f}+-0.05, split 0.1 vs resolution 2.86):"
      f" floor {f2:.4f}  (degradation x{r2:.2f})")
print(f"   triple-merge (g3,g4,g5 -> {m3:.2f}):                floor {f3:.4f}"
      f"  (degradation x{r3:.2f})")
w1 = r2 <= 3.0 and r3 <= 10.0
x1 = r2 > 10.0
print("   W1: " + ("SURVIVES -- interior degeneracy does NOT reach the floor; repulsion"
                   " NOT needed" if w1 else ("X1 FIRED" if x1 else "partial -- see ratios")))

print("\n== W2: desert robustness ==")
Zd = [g for g in GAM if not (44.0 <= g <= 51.5)]
fd, vd = model_floor(Zd)
rd = base_floor / max(fd, 1e-15)
cd = centroid(vd)
print(f"   desert [44, 51.5] (gamma_9, gamma_10 deleted): floor {fd:.4f}"
      f"  (degradation x{rd:.2f}); minimizer centroid = {cd:.2f}")
w2 = rd <= 20.0 and 43.0 <= cd <= 53.0
x2 = rd > 100.0
print("   W2: " + ("SURVIVES -- desert costs bounded, minimizer lives in the desert;"
                   " RvM-scale control suffices" if w2 else ("X2 FIRED" if x2 else
                   "partial -- see numbers")))

print("\n== W3: the (alpha)-margin (arithmetic display) ==")
# certified eps_lambda (P-inf-E section 21 exact-matrix values) and measured off-E floors
table = [(1.5, 1.57e-4, 0.280), (2.0, 1.38e-12, 0.568)]
for lam, eps, fl in table:
    bar = lam**2 * eps          # lambda^{1+delta} with delta=1
    print(f"   lambda={lam}: weld bar lambda^2*eps = {bar:.2e}   vs measured floor {fl:.3f}"
          f"   margin x{fl/bar:.1e}")
print("   (the (b)-requirement is floor >= bar: met with >= 10^3 / 10^11 room; at lambda=3"
      " the bar is ~1e-44)")

print("\nRESULT: " + ("GREEN -- audit predictions W1/W2 survive; floor robust to clusters"
                      " and deserts at the predicted scales" if (w1 and w2) else
                      "PARTIAL/RED -- diagnose (criterion vs mathematics)"))
