"""
Port Principle — settlement certificates (numpy/scipy only, local-safe).

C1  Causal parity: causality => symmetric and antisymmetric parts of a response
    kernel carry EQUAL energy; the only excess is the instantaneous diagonal.
    (finite grid: exact rationals; continuum: damped oscillator, Plancherel)
C2  Quantum FDT = the T24 Petz fork: one dissipation spectrum chi''(w), four
    weights (coth, 1/x, tanh, x). Watched variance >= T * pushed susceptibility;
    SLD (Bures) Fisher <= Kubo-Mori Fisher = beta * f-sum rule; per-mode ratio tanh(u)/u.
C3  Arrow = FDT violation: overdamped Langevin with a skew (circulating) force has an
    EXACTLY Gibbs stationary density (static/symmetric instrument sees equilibrium),
    yet the Harada-Sasa FDT-violation integral equals the hidden heat 2 k T w^2.
C4  Dilation: decay is dephasing of a finite ledger of pure rotations
    (Wigner-Weisskopf); resistance Gamma comes with KK reactance (Lamb shift);
    finite capacity => recurrence at t_rec = 2 pi / delta.
"""
import numpy as np
from fractions import Fraction
from scipy.linalg import expm, eigh, solve_sylvester, solve_continuous_lyapunov
from scipy.integrate import quad

rng = np.random.default_rng(20260929)
checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


# ---------------------------------------------------------------- C1 causal parity
print("\n== C1 causal parity ==")
for trial in range(6):
    n = 9
    L = [[Fraction(int(rng.integers(-9, 10)), int(rng.integers(1, 8))) if i > j else Fraction(0)
          for j in range(n)] for i in range(n)]
    d = [Fraction(int(rng.integers(-5, 6)), int(rng.integers(1, 4))) for _ in range(n)]
    S2 = sum(((L[i][j] + L[j][i]) / 2) ** 2 for i in range(n) for j in range(n))
    A2 = sum(((L[i][j] - L[j][i]) / 2) ** 2 for i in range(n) for j in range(n))
    Ld = [[L[i][j] + (d[i] if i == j else 0) for j in range(n)] for i in range(n)]
    S2d = sum(((Ld[i][j] + Ld[j][i]) / 2) ** 2 for i in range(n) for j in range(n))
    A2d = sum(((Ld[i][j] - Ld[j][i]) / 2) ** 2 for i in range(n) for j in range(n))
    ok = (S2 == A2) and (S2d - A2d == sum(x * x for x in d))
    check(f"C1.{trial} strictly causal |S|^2==|A|^2 exactly; excess == |diag|^2", ok,
          f"|S|^2={S2}  |A|^2={A2}")

g, w1 = 0.3, 1.7  # f(t) = e^{-g t} sin(w1 t) theta(t)
chi = lambda w: w1 / ((g - 1j * w) ** 2 + w1 ** 2)
re2 = quad(lambda w: chi(w).real ** 2, -np.inf, np.inf, limit=400)[0]
im2 = quad(lambda w: chi(w).imag ** 2, -np.inf, np.inf, limit=400)[0]
exact = np.pi * w1 ** 2 / (4 * g * (g ** 2 + w1 ** 2))  # pi * int f^2 dt
check("C1.cont damped oscillator: int (Re chi)^2 == int (Im chi)^2 == pi int f^2",
      abs(re2 - exact) < 1e-7 and abs(im2 - exact) < 1e-7,
      f"Re:{re2:.10f} Im:{im2:.10f} exact:{exact:.10f}")

# ---------------------------------------------------------------- C2 quantum FDT / Petz fork
print("\n== C2 quantum FDT = Petz fork (Bures vs Kubo-Mori) ==")
n, beta = 6, 1.3
X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); H = (X + X.conj().T) / 2
Y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); A = (Y + Y.conj().T) / 2
rho = expm(-beta * H); rho /= np.trace(rho).real
E, U = eigh(H); p = np.exp(-beta * E); p /= p.sum()
Ae = U.conj().T @ A @ U
dA = Ae - np.trace(np.diag(p) @ Ae).real * np.eye(n)

# spectral lines of chi''(w): weight pi (p_i - p_j)|A_ij|^2 at w = E_j - E_i  (hbar = 1)
lines = [(E[j] - E[i], np.pi * (p[i] - p[j]) * abs(Ae[i, j]) ** 2)
         for i in range(n) for j in range(n) if E[j] - E[i] > 1e-12]
x = lambda w: beta * w / 2

# (a) watched: symmetrized variance, direct
var_direct = (np.trace(rho @ A @ A) - np.trace(rho @ A) ** 2).real
# (b) pushed: isothermal static susceptibility by finite-difference push  rho_h ~ exp(-beta(H - hA))
def meanA(h):
    r = expm(-beta * (H - h * A)); r /= np.trace(r).real
    return np.trace(r @ A).real
hh = 1e-4
chi_iso = (-meanA(2 * hh) + 8 * meanA(hh) - 8 * meanA(-hh) + meanA(-2 * hh)) / (12 * hh)
# spectral forms (elastic w=0 part identical in both: sum_i p_i |dA_ii|^2 over degenerate blocks)
elastic = sum(p[i] * abs(dA[i, j]) ** 2 for i in range(n) for j in range(n) if abs(E[i] - E[j]) < 1e-12)
var_spec = elastic + sum(wt / np.pi * (1 / np.tanh(x(w))) for w, wt in lines)   # coth weight
kubo_spec = elastic + sum(wt / np.pi * (1 / x(w)) for w, wt in lines)            # 1/x weight
check("C2.a watched variance == (1/pi) int coth(x) chi''  (+elastic)", abs(var_direct - var_spec) < 1e-12,
      f"{var_direct:.12f} vs {var_spec:.12f}")
check("C2.b pushed chi_iso == beta * Kubo variance == (1/pi) int (1/x) chi'' * beta", abs(chi_iso - beta * kubo_spec) < 1e-8,
      f"{chi_iso:.10f} vs {beta*kubo_spec:.10f}")
check("C2.c quantum FDT inequality: Var >= T chi_iso (x coth x >= 1)", var_direct >= chi_iso / beta,
      f"Var={var_direct:.6f}  T*chi={chi_iso/beta:.6f}  gap={var_direct-chi_iso/beta:.3e}")
# classical limit: A commuting with H => gap 0
Ac = U @ np.diag(rng.normal(size=n)) @ U.conj().T
var_c = (np.trace(rho @ Ac @ Ac) - np.trace(rho @ Ac) ** 2).real
r0 = lambda h: (lambda r: np.trace(r @ Ac).real / np.trace(r).real)(expm(-beta * (H - h * Ac)))
chi_c = (r0(hh) - r0(-hh)) / (2 * hh)
check("C2.d fork closes when [A,H]=0: Var == T chi_iso", abs(var_c - chi_c / beta) < 1e-7,
      f"{var_c:.10f} vs {chi_c/beta:.10f}")

# Fisher side: rotation family rho_th = e^{-iA th} rho e^{iA th}; tangent Xd = -i[A, rho]
Xd = -1j * (A @ rho - rho @ A)
Lsld = solve_sylvester(rho, rho, 2 * Xd)                 # rho L + L rho = 2 d rho
F_sld = np.trace(rho @ Lsld @ Lsld).real
F_sld_resp = sum(4 / np.pi * np.tanh(x(w)) * wt for w, wt in lines)   # Hauke et al. (tanh weight)
check("C2.e SLD/Bures QFI (Sylvester) == (4/pi) int tanh(x) chi''", abs(F_sld - F_sld_resp) < 1e-10,
      f"{F_sld:.12f} vs {F_sld_resp:.12f}")
# Kubo-Mori metric via its own integral formula  g = int_0^inf Tr[X (rho+s)^-1 X (rho+s)^-1] ds
def km_integrand(s):
    R = np.linalg.inv(rho + s * np.eye(n))
    return np.trace(Xd @ R @ Xd @ R).real
F_km = quad(km_integrand, 0, np.inf, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
fsum = (beta * np.trace(rho @ (A @ (H @ A - A @ H) - (H @ A - A @ H) @ A))).real  # beta <[A,[H,A]]>
F_km_resp = sum(4 / np.pi * x(w) * wt for w, wt in lines)            # x weight
check("C2.f Kubo-Mori metric (integral) == beta <[A,[H,A]]> (f-sum rule) == (4/pi) int x chi''",
      abs(F_km - fsum) < 1e-8 and abs(fsum - F_km_resp) < 1e-10,
      f"{F_km:.10f} | {fsum:.10f} | {F_km_resp:.10f}")
check("C2.g Petz ordering g_SLD <= g_KM (tanh x <= x)", F_sld <= F_km, f"{F_sld:.6f} <= {F_km:.6f}")
# relative entropy of rotated Gibbs = beta * work  (passivity)
th = 0.2
rth = expm(-1j * A * th) @ rho @ expm(1j * A * th)
ev, evec = eigh(rth); ev = np.clip(ev, 1e-300, None)
log_rth = evec @ np.diag(np.log(ev)) @ evec.conj().T
ev0, evec0 = eigh(rho); log_r = evec0 @ np.diag(np.log(ev0)) @ evec0.conj().T
D = np.trace(rth @ (log_rth - log_r)).real
W = np.trace((rth - rho) @ H).real
check("C2.h D(U rho U* || rho) == beta * W  (Gibbs passive: every rotation costs work)", abs(D - beta * W) < 1e-10 and W > 0,
      f"D={D:.12f}  beta*W={beta*W:.12f}")

# ---------------------------------------------------------------- C3 arrow = FDT violation
print("\n== C3 hidden current: Gibbs density, violated FDT, Harada-Sasa heat ==")
k, T, om = 1.4, 0.7, 0.9
J = np.array([[0, om], [-om, 0]])
M = k * (np.eye(2) - J)                       # dx = -M x dt + sqrt(2T) dW
Sig = solve_continuous_lyapunov(M, 2 * T * np.eye(2))    # M S + S M^T = 2T I
check("C3.a stationary density is EXACTLY Gibbs (T/k) I despite the circulation", np.allclose(Sig, T / k * np.eye(2), atol=1e-14),
      f"Sigma={np.round(Sig,12).tolist()}")
def hs_integrand(w, i, Mm, Tv):
    Rm = np.linalg.inv(Mm - 1j * w * np.eye(2))           # x response, convention x^(w)=int x e^{iwt}
    C = Rm @ np.diag(2 * Tv) @ Rm.conj().T                 # x-x spectral density
    Cvv = w ** 2 * C[i, i].real
    Rv = (-1j * w * Rm)[i, i].real
    return (Cvv - 2 * Tv[i] * Rv) / (2 * np.pi)
Tv = np.array([T, T])
heat_HS = sum(quad(hs_integrand, -np.inf, np.inf, args=(i, M, Tv), limit=400)[0] for i in range(2))
heat_exact = 2 * k * T * om ** 2
check("C3.b Harada-Sasa FDT-violation integral == hidden heat 2 k T w^2", abs(heat_HS - heat_exact) < 1e-7,
      f"HS={heat_HS:.10f}  exact={heat_exact:.10f}")
M0 = k * np.eye(2)
viol0 = max(abs(hs_integrand(w, i, M0, Tv)) for w in np.linspace(-20, 20, 81) for i in range(2))
check("C3.c no circulation (w=0): FDT holds pointwise, integrand == 0", viol0 < 1e-12, f"max|integrand|={viol0:.2e}")

# ---------------------------------------------------------------- C4 dilation / finite ledger
print("\n== C4 decay = dephasing of rotations; resistance + reactance; recurrence ==")
def ww(N, delta, gc, E0):
    Ek = (np.arange(N) - (N - 1) / 2) * delta
    Hm = np.zeros((N + 1, N + 1)); Hm[0, 0] = E0; Hm[0, 1:] = gc; Hm[1:, 0] = gc
    Hm[1:, 1:] = np.diag(Ek)
    lam, V = eigh(Hm)
    wts = V[0, :] ** 2                                   # spectral measure of the port |0>
    amp = lambda t: np.sum(wts * np.exp(-1j * lam * t))  # pure sum of rotations
    return amp, Ek
N, delta, gc, E0 = 801, 0.025, 0.035, 3.0
amp, Ek = ww(N, delta, gc, E0)
Gam = 2 * np.pi * gc ** 2 / delta
Wh = Ek[-1] + delta / 2
lamb_KK = (gc ** 2 / delta) * np.log((Wh + E0) / (Wh - E0))   # KK partner of flat Gamma, finite band
trec = 2 * np.pi / delta
ts = np.linspace(2, 0.5 * trec, 1500)
a = np.array([amp(t) for t in ts])
P = np.abs(a) ** 2
mask = ts < 6 / Gam
rel = np.max(np.abs(P[mask] - np.exp(-Gam * ts[mask])) / np.exp(-Gam * ts[mask]))
check("C4.a |<0|e^{-iHt}|0>|^2 (finite sum of rotations) == e^{-Gamma t}, Gamma=2pi g^2/delta (to 6 lifetimes)", rel < 0.02,
      f"Gamma={Gam:.4f}  max rel dev={rel:.3e}")
ph = np.unwrap(np.angle(a[mask]))
slope = np.polyfit(ts[mask], ph, 1)[0]
shift = -slope - E0
check("C4.b reactance (Lamb shift) measured from phase == KK partner (g^2/delta) ln((W+E0)/(W-E0))",
      abs(shift - lamb_KK) < 0.1 * abs(lamb_KK), f"measured={shift:.5f}  KK={lamb_KK:.5f}")
tr = np.linspace(0.9 * trec, 1.2 * trec, 3000)
Prev = np.max(np.abs([amp(t) for t in tr]) ** 2)
Pmid = np.exp(-Gam * trec)
check("C4.c finite ledger => revival near t_rec = 2pi/delta (record not durable)", Prev > 1e6 * Pmid,
      f"t_rec={trec:.1f}  revival P={Prev:.3e}  vs e^(-Gamma t_rec)={Pmid:.1e}")

print(f"\n{sum(ok for _, ok in checks)}/{len(checks)} GREEN")

# C4.a' — the miss in C4.a is the reactance feeding back: Z = 1/(1 - Re Sigma'(E0))
dSig = (gc ** 2 / delta) * (1 / (Wh + E0) + 1 / (Wh - E0))
Z = 1 / (1 - dSig)
relZ = np.max(np.abs(P[mask] - Z ** 2 * np.exp(-Z * Gam * ts[mask])) / (Z ** 2 * np.exp(-Z * Gam * ts[mask])))
check("C4.a' with reactance renormalization P = Z^2 e^{-Z Gamma t}, Z=1/(1-Re Sigma')", relZ < 5e-3,
      f"Z={Z:.5f}  max rel dev={relZ:.3e} (was {rel:.3e} without Z)")
print(f"\n{sum(ok for _, ok in checks)}/{len(checks)} checks; C4.a superseded by C4.a'")
