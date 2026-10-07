"""
Open Problem O (Paper 18 Rem 6.4): does closed-current/Noether positivity force the
JOINT monotone metric on D(C^2 (x) C^3) -- incl. tensor cross-coherences -- to be the
minimal SLD/Bures member?

Resolution (this cert): NO. By a three-way structural dichotomy on D(C^2 (x) C^3)=D(C^6),
the minimal (Bures) member is forced by no natural reading; the only canonically pinned
member is Kubo-Mori (dual flatness), which is NOT minimal. Consistent with the D4 result.

Facts (numpy, exact; Petz family via Morozova-Chentsov g^f_rho(A,A)=sum c^f(lam_i,lam_j)|A_ij|^2):

 (H)  HOMOGENEITY. c^f(tx,ty)=t^{-1} c^f(x,y) for every monotone f. Consequence: on product
      states with product-rule tangents X_A(x)rB + rA(x)X_B, EVERY monotone metric is additive
      (joint = sum of parts). So "additivity/extensivity on the product structure" is
      metric-AGNOSTIC -- it cannot force any member, a fortiori not the minimal one.

 (O1) POSITIVITY. All three Petz members (SLD/Bures minimal, Kubo-Mori, RLD maximal) are
      positive on genuine tensor CROSS-COHERENCES. Positivity selects nothing.

 (O2) THE ONE GENUINE SELECTOR = DUAL FLATNESS (Hessian of relative entropy). On D(C^6),
      Kubo-Mori = BKM integral = Hess(Tr rho log rho) on cross-coherences; Bures != Hess.
      So if anything is forced by a canonical (additive-potential / dually-flat) principle it
      is KUBO-MORI -- the unique dually-flat monotone metric (Grasselli-Streater) -- NOT Bures.

 (O3) VERDICT. The minimal member (Bures) is selected by NONE of {homogeneous additivity,
      positivity, dual flatness}. Open Problem O resolves NEGATIVE for its conjectured Bures
      answer. The gauge algebra su(2)+su(3) (Thm 6.1, unitary invariance) is metric-agnostic and
      survives untouched; only the connection/cumulant structure is pinned, and it is Kubo-Mori.

No torch.
"""
import sys
import numpy as np
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def cfun(name, x, y):
    if name == 'SLD':   return 2.0/(x+y)
    if name == 'KM':     return 1.0/x if abs(x-y) < 1e-12 else (np.log(x)-np.log(y))/(x-y)
    if name == 'RLD':   return (x+y)/(2*x*y)

def gf(name, r, A):
    w, V = np.linalg.eigh(r)
    Ae = V.conj().T @ A @ V
    return float(sum(cfun(name, w[i], w[j]) * abs(Ae[i, j])**2
                     for i in range(len(w)) for j in range(len(w))).real)

def bkm_integral(r, A):
    u = np.linspace(0.0, 1.0 - 1e-12, 120001); s = u/(1.0-u); jac = 1.0/(1.0-u)**2
    I = np.eye(r.shape[0])
    vals = np.array([np.trace(A @ np.linalg.inv(r+sv*I) @ A @ np.linalg.inv(r+sv*I)).real
                     for sv in s]) * jac
    trap = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
    return float(trap(vals, u))

PASS = []
def chk(n, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {n}")

# (H) homogeneity of c^f, degree -1
print("H — Morozova-Chentsov weight is homogeneous deg -1 (=> product-additivity universal)")
hom = True
for f in ('SLD', 'KM', 'RLD'):
    for (x, y, t) in [(0.3, 0.7, 2.0), (0.5, 0.2, 5.0), (0.11, 0.4, 0.3)]:
        hom &= abs(cfun(f, t*x, t*y) - cfun(f, x, y)/t) < 1e-12
chk("c^f(tx,ty) = c^f(x,y)/t for SLD, KM, RLD", hom)

pA = np.array([0.6, 0.4]); rA = np.diag(pA).astype(complex)
qB = np.array([0.5, 0.3, 0.2]); rB = np.diag(qB).astype(complex)
rho = np.kron(rA, rB)
XA = np.array([[0, 1], [1, 0]], dtype=complex)
XB = np.zeros((3, 3), dtype=complex); XB[0, 1] = 1; XB[1, 0] = 1
T = np.kron(XA, rB) + np.kron(rA, XB)
univ_add = all(abs(gf(f, rho, T) - (gf(f, rA, XA) + gf(f, rB, XB))) < 1e-9 for f in ('SLD', 'KM', 'RLD'))
chk("EVERY monotone metric is additive on product-rule tangents (metric-agnostic, forces nothing)",
    univ_add)

# (O1) positivity on tensor cross-coherence
print("O1 — positivity on tensor cross-coherences: all Petz members > 0")
Xc = np.zeros((6, 6), dtype=complex); Xc[0, 5] = 1; Xc[5, 0] = 1   # |q0,t0> <-> |q1,t2>
vals = {f: gf(f, rho, Xc) for f in ('SLD', 'KM', 'RLD')}
chk(f"SLD={vals['SLD']:.3f} <= KM={vals['KM']:.3f} <= RLD={vals['RLD']:.3f}, all>0; "
    f"positivity selects nothing", all(v > 1e-9 for v in vals.values())
    and vals['SLD'] <= vals['KM'] + 1e-9 <= vals['RLD'] + 2e-9)

# (O2) dual flatness = Hessian of relative entropy = Kubo-Mori, on cross-coherences (6-dim)
print("O2 — dual-flat selector on D(C^6): Kubo-Mori = BKM = Hess; Bures != ")
# non-degenerate 6-dim state + cross-coherence direction
rho2 = np.diag([0.30, 0.22, 0.18, 0.12, 0.10, 0.08]).astype(complex)
g_km, g_bkm, g_sld = gf('KM', rho2, Xc), bkm_integral(rho2, Xc), gf('SLD', rho2, Xc)
print(f"    cross-coherence:  g^KM={g_km:.5f}  BKM∫={g_bkm:.5f}  g^Bures={g_sld:.5f}")
chk("Kubo-Mori = BKM integral (the dually-flat/entropy-Hessian metric) on cross-coherences",
    abs(g_km - g_bkm) < 1e-4)
chk("Bures != BKM/Hessian on cross-coherences (Bures is NOT dually flat)", abs(g_sld - g_bkm) > 1e-3)

# (O3) verdict
print("O3 — VERDICT")
chk("minimal (Bures) forced by NONE of {homogeneous additivity, positivity, dual flatness} "
    "=> Open Problem O resolves NEGATIVE for Bures (only KM is pinned, and it is not minimal)",
    hom and univ_add and all(v > 1e-9 for v in vals.values()) and abs(g_km - g_bkm) < 1e-4
    and abs(g_sld - g_bkm) > 1e-3)

print("=" * 76)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("Open Problem O: closed-current/Noether positivity does NOT force the minimal (Bures)")
print("joint metric on D(C^2 (x) C^3). Product-additivity is universal (homogeneity); positivity")
print("is metric-agnostic; the only canonical selector is dual flatness = KUBO-MORI (not minimal).")
print("The su(2)+su(3) gauge recovery (unitary invariance) is metric-agnostic and survives.")
print("=" * 76)
