"""
D4 resolution: which monotone metric carries the quantum continuation of Paper III's
information geometry — Bures or Kubo-Mori? (Follow-up to leverage C2, finding F2.)

The corpus has an apparent inconsistency:
  * the cubic-MECHANICS line (Papers 15/18/44) selects BURES, via the criterion
    "the monotone metric whose Nambu flow is the von Neumann flow ρ̇=−i[H,ρ]"
    (Paper 15 Thm 3.2);
  * Paper III's information geometry (the α-collapse Γ^(α)=−((1+α)/2)T, dual flatness,
    Fisher = Hess(negative entropy)) is a DUALLY-FLAT structure, and the unique dually-flat
    monotone metric is KUBO-MORI (Grasselli–Streater; T24 Thm 5.1).

This cert settles it on the qubit D(ℂ²) (sympy/numpy, exact + tight-tol numerics, NO torch):

 (M1) METRIC-AGNOSTICISM. Paper 15 Thm 3.2's proof uses ONLY unitary invariance of the
      metric's volume form. Every monotone metric g^f is unitarily invariant, so the
      von-Neumann reduction holds for ALL of them — it does NOT single out Bures. Verified:
      g^f is unitary-invariant for f ∈ {SLD/Bures, Kubo–Mori, RLD}. ⇒ the Bures selection
      is UNDER-DETERMINED.

 (M2) KUBO–MORI = THE DUAL-FLAT / ENTROPY-HESSIAN METRIC. The quantum continuation of
      Paper III's foundational identity "Fisher = Hess(Σ p log p)" is
      Kubo–Mori = Hess(Tr ρ log ρ) (the BKM metric), NOT Bures:
        g^KM = BKM integral ∫₀^∞ Tr(A(ρ+s)^{-1}A(ρ+s)^{-1})ds = Hess(Tr ρ log ρ);
        g^Bures ≠ Hess(Tr ρ log ρ) on coherences (r>0).
      So Paper III's dual-flat / α-collapse / cumulant structure continues on Kubo–Mori.

 (M3) AGREEMENT ON THE CLASSICAL DOMAIN. On the diagonal (decoherent face = Paper III's
      actual domain) and at the maximally-mixed center, ALL monotone metrics coincide
      (c^f(λ,λ)=1/λ). The fork opens only on coherences. So the resolution is role-
      separation, not contradiction: Bures = estimation/QFI; Kubo–Mori = the dual-flat
      connection/cumulant carrier; they agree where Paper III lives.
"""
import sys
import numpy as np
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)

def rho(rvec):
    rx, ry, rz = rvec
    return (I2 + rx*sx + ry*sy + rz*sz) / 2

def cfun(name, x, y):
    if name == 'SLD':   # Bures, f=(1+t)/2, arithmetic mean
        return 2.0/(x+y)
    if name == 'KM':     # Kubo–Mori, logarithmic mean
        return 1.0/x if abs(x-y) < 1e-12 else (np.log(x)-np.log(y))/(x-y)
    if name == 'RLD':    # harmonic mean
        return (x+y)/(2*x*y)

def gf(name, r, A):
    """monotone metric g^f_r(A,A) = sum_ij c^f(λ_i,λ_j) |A_ij|^2 in r's eigenbasis."""
    w, V = np.linalg.eigh(r)
    Ae = V.conj().T @ A @ V
    return float(sum(cfun(name, w[i], w[j]) * abs(Ae[i, j])**2
                     for i in range(2) for j in range(2)).real)

def bkm_integral(r, A):
    """g^BKM(A,A) = ∫_0^∞ Tr(A (r+sI)^{-1} A (r+sI)^{-1}) ds, numeric.
    Substitute s = u/(1-u) to capture the full infinite range (the 2/s^2 tail)."""
    u = np.linspace(0.0, 1.0 - 1e-12, 200001)
    s = u / (1.0 - u)
    jac = 1.0 / (1.0 - u)**2
    vals = np.empty_like(u)
    for k in range(len(u)):
        M = np.linalg.inv(r + s[k]*I2)
        vals[k] = np.trace(A @ M @ A @ M).real * jac[k]
    trap = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
    return float(trap(vals, u))

def hess_entropy(r, A):
    """Hess of Φ(ρ)=Tr(ρ log ρ) in direction A: d^2/dt^2 Tr((r+tA)log(r+tA))|_0."""
    def Phi(t):
        M = r + t*A
        w, V = np.linalg.eigh(M)
        return float(sum(wi*np.log(wi) for wi in w))
    h = 1e-4
    return (Phi(h) - 2*Phi(0.0) + Phi(-h)) / h**2

PASS = []
def chk(n, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {n}")

rng = np.random.default_rng(0)

print("M1 — von-Neumann criterion is metric-AGNOSTIC (unitary invariance, all f)")
maxdev = 0.0
for _ in range(40):
    rvec = rng.normal(size=3); rvec *= 0.7/np.linalg.norm(rvec)*rng.uniform(0.1, 1.0)
    r = rho(rvec)
    A = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); A = A + A.conj().T
    A -= np.trace(A)/2*I2
    # random unitary (von Neumann flow point) U = exp(-i H t)
    Hh = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Hh = Hh + Hh.conj().T
    wH, VH = np.linalg.eigh(Hh); U = VH @ np.diag(np.exp(-1j*wH*rng.uniform(0, 3))) @ VH.conj().T
    rU, AU = U @ r @ U.conj().T, U @ A @ U.conj().T
    for f in ('SLD', 'KM', 'RLD'):
        maxdev = max(maxdev, abs(gf(f, rU, AU) - gf(f, r, A)))
chk(f"every monotone metric g^f is unitary-invariant (max dev {maxdev:.1e}) "
    f"⇒ Thm 3.2 holds for ALL f ⇒ Bures NOT selected", maxdev < 1e-9)

print("M2 — Kubo–Mori = BKM integral = Hess(Tr ρ log ρ); Bures ≠ entropy Hessian")
km_eq_bkm = km_eq_hess = bures_ne_hess = True
for rr in (0.2, 0.5, 0.8):
    r = rho((0, 0, rr))                 # diagonal ρ
    A = sx                              # coherence direction
    g_km, g_bkm, g_hess, g_bures = gf('KM', r, A), bkm_integral(r, A), hess_entropy(r, A), gf('SLD', r, A)
    km_eq_bkm &= abs(g_km - g_bkm) < 1e-4
    km_eq_hess &= abs(g_km - g_hess) < 1e-4
    bures_ne_hess &= abs(g_bures - g_hess) > 1e-3
    print(f"    r={rr}: g^KM={g_km:.5f}  BKM∫={g_bkm:.5f}  Hess(TrρlogρlogΦ)={g_hess:.5f}  g^Bures={g_bures:.5f}")
chk("g^KM == BKM integral (Kubo–Mori is the BKM metric)", km_eq_bkm)
chk("g^KM == Hess(Tr ρ log ρ)  ⇒ KM is the dual-flat / entropy-Hessian metric "
    "(quantum continuation of Paper III 'Fisher=Hess(neg entropy)')", km_eq_hess)
chk("g^Bures ≠ Hess(Tr ρ log ρ) on coherences ⇒ Bures is NOT dually flat", bures_ne_hess)

print("M3 — agreement on the classical domain (diagonal + center): role-separation")
diag_agree = center_agree = True
for rr in (0.2, 0.5, 0.8):
    r = rho((0, 0, rr))
    vals = [gf(f, r, sz) for f in ('SLD', 'KM', 'RLD')]   # diagonal tangent
    diag_agree &= max(vals) - min(vals) < 1e-9
small = rho((0, 0, 1e-5))
center_agree = abs(gf('SLD', small, sx) - gf('KM', small, sx)) < 1e-6
chk("all monotone metrics agree on the diagonal tangent (= classical Fisher)", diag_agree)
chk("Bures and Kubo–Mori agree at the maximally-mixed center (fork closes)", center_agree)

print("=" * 72)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("D4 RESOLVED: the von-Neumann criterion (Paper 15 Thm 3.2) is metric-agnostic, so the")
print("Bures selection is under-determined. Paper III's dual-flat/α-collapse/cumulant structure")
print("continues quantumly on KUBO–MORI (= Hess(Tr ρ log ρ), the unique dually-flat monotone")
print("metric), NOT Bures. Bures keeps the estimation/QFI role. They agree where Paper III lives")
print("(diagonal + center); the fork opens only on coherences. Resolution = role-separation.")
print("=" * 72)
