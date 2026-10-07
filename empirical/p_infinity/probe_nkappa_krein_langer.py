"""probe_nkappa_krein_langer.py — certificate for P-infinity-E SS12 (the N_kappa correspondence).

Object: Xi(z) = xi(1/2 - iz), xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s) — real, entire,
even, pole-free.  Zero rho = beta + i gamma of zeta maps to z = -gamma + i(beta - 1/2):
on-line zero <=> real z.  Ntilde(z) := -Xi'/Xi(z) = i * (xi'/xi)(1/2 - iz).

CLASSICAL FACT (P-infinity-E Prop E.13): RH <=> Ntilde is Herglotz (class N_0) <=> the
Nevanlinna kernel  K(z,w) = (Ntilde(z) - conj(Ntilde(w))) / (z - conj(w))  is PSD on C+.
Off-line zeros = generalized poles of non-positive type; Krein-Langer: #negative squares
kappa = #zeros of Xi in C+ (an off-line quadruple contributes exactly 2).

CHECK A  (true zeta, kappa = 0 witness): K on 21 points of C+ is PSD at dps=30 —
         a genuine negative square here would DISPROVE RH.
CHECK B  (counting law, rational models from the first 12 true zeros):
         all-real model -> kappa = 0; imaginary pair +-i*delta -> kappa = 1 exactly;
         off-line quadruple +-w, +-conj(w) -> kappa = 2 exactly.
CHECK C  (displacement on the TRUE object): Xi_pert = Xi * (1 - z^2/w^2)(1 - z^2/wbar^2),
         w = 10 + 0.25i (a fake off-line quadruple grafted onto zeta): kappa jumps 0 -> 2.
CHECK D  (index = winding = S(T) grounding): (1/2pi i) contour-int Xi'/Xi dz over the
         rectangle [-20,20] x [0.1, 2] counts 0 (true) and 2 (perturbed) — the Pontryagin
         index IS the argument-principle / Backlund-Turing count.

Deterministic, local, ~2-4 min (mpmath).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 25

def xilogd(s):
    """xi'/xi(s)."""
    return (1/s + 1/(s - 1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2
            + mp.zeta(s, derivative=1) / mp.zeta(s))

def Nt_true(z):
    """Ntilde(z) = -Xi'/Xi(z) = i * xi'/xi(1/2 - i z)."""
    return 1j * xilogd(mp.mpf(0.5) - 1j*z)

def nev_kernel(Nfun, pts):
    M = len(pts)
    vals = [Nfun(z) for z in pts]
    K = mp.matrix(M, M)
    for i in range(M):
        for j in range(M):
            K[i, j] = (vals[i] - mp.conj(vals[j])) / (pts[i] - mp.conj(pts[j]))
    return K

def neg_squares(K, rel_tol=mp.mpf("1e-15")):
    E = mp.eighe(K, eigvals_only=True)
    E = [mp.re(e) for e in E]
    scale = max(abs(e) for e in E)
    neg = sum(1 for e in E if e < -rel_tol * scale)
    return neg, float(min(E)), float(scale)

PTS = [mp.mpc(x, y) for x in (-24, -16, -8, 0, 8, 16, 24) for y in (0.4, 1.2, 2.5)]

# ---------------- CHECK A: true zeta, kappa = 0 ----------------
print("== CHECK A: Nevanlinna kernel of -Xi'/Xi on 21 points of C+ (true zeta) ==")
herg = all(mp.im(Nt_true(z)) > 0 for z in [mp.mpc(3, 0.5), mp.mpc(-11, 1.0), mp.mpc(20, 2.0)])
print(f"   Herglotz sign spot-check Im Ntilde > 0 on C+: {herg}")
KA = nev_kernel(Nt_true, PTS)
negA, mnA, scA = neg_squares(KA)
okA = (negA == 0) and herg
print(f"   eigenvalues: min = {mnA:.3e}, scale = {scA:.3e}, negative squares = {negA}")
print("   " + ("PASS — kappa = 0 on this window (RH-consistent; a negative square here would "
               "DISPROVE RH)" if okA else "FAIL"))

# ---------------- CHECK B: counting law on rational models ----------------
print("\n== CHECK B: Krein-Langer counting law, rational models from first 12 zeros ==")
T = [mp.im(mp.zetazero(k)) for k in range(1, 13)]

def model(zeros_sq):
    """Ntilde for Xi_model = prod (1 - z^2/a): poles of -Xi'/Xi at z^2 = a."""
    def f(z):
        return -sum(2*z/(z*z - a) for a in zeros_sq)
    return f

base = [t*t for t in T]
delta = mp.mpf("0.3"); w = T[0] + 0.25j
cases = [
    ("all zeros real            ", base,                                    0),
    ("imaginary pair +-i*0.3    ", [-delta*delta] + base[1:],               1),
    ("off-line quadruple t1+-.25i", [w*w, mp.conj(w)*mp.conj(w)] + base[1:], 2),
]
okB = True
for name, zs, expect in cases:
    K = nev_kernel(model(zs), PTS)
    neg, mn, sc = neg_squares(K)
    ok = neg == expect
    okB &= ok
    print(f"   {name}: negative squares = {neg} (expect {expect}), min eig = {mn:.3e}   "
          + ("PASS" if ok else "FAIL"))
print("   " + ("PASS — kappa counts C+ zeros EXACTLY (quadruple -> 2, imaginary pair -> 1)"
               if okB else "FAIL"))

# ---------------- CHECK C: graft a fake off-line quadruple onto TRUE zeta ----------------
print("\n== CHECK C: true zeta with grafted quadruple w = 10 + 0.25i — kappa: 0 -> 2 ==")
wq = mp.mpc(10, 0.25)

def Nt_pert(z):
    return Nt_true(z) - (2*z/(z*z - wq*wq) + 2*z/(z*z - mp.conj(wq)*mp.conj(wq)))

KC = nev_kernel(Nt_pert, PTS)
negC, mnC, scC = neg_squares(KC)
okC = negC == 2
print(f"   negative squares = {negC} (expect 2), min eig = {mnC:.3e}")
print("   " + ("PASS — one off-line quadruple = exactly two negative squares, on the true object"
               if okC else "FAIL"))

# ---------------- CHECK D: kappa = argument-principle winding (= S(T) count) ----------------
print("\n== CHECK D: winding (1/2pi i) contour-int Xi'/Xi dz over [-20,20] x [0.1,2] ==")
mp.mp.dps = 15
corners = [mp.mpc(-20, 0.1), mp.mpc(20, 0.1), mp.mpc(20, 2), mp.mpc(-20, 2), mp.mpc(-20, 0.1)]

def winding(logd):
    tot = mp.mpc(0)
    for a, b in zip(corners[:-1], corners[1:]):
        tot += mp.quad(lambda t: logd(a + t*(b - a)) * (b - a), [0, 1], maxdegree=10)
    return tot / (2j * mp.pi)

W0 = winding(lambda z: -Nt_true(z))
W2 = winding(lambda z: -Nt_pert(z))
okD = abs(W0 - 0) < 1e-3 and abs(W2 - 2) < 1e-3
print(f"   true zeta:      winding = {complex(W0):.6f}  (expect 0)")
print(f"   grafted zeta:   winding = {complex(W2):.6f}  (expect 2)")
print("   " + ("PASS — Pontryagin index = argument-principle count (the S(T) object)" if okD
               else "FAIL"))

allok = okA and okB and okC and okD
print("\nRESULT: " + ("GREEN — RH <=> -Xi'/Xi in N_0 certified operational: kappa = #C+ zeros "
                      "exactly (Krein-Langer), detectable as negative squares AND as winding; "
                      "off-line quadruple <-> 2 negative squares on the true object"
                      if allok else "RED"))
