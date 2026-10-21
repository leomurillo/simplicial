"""Port harvest equals port visibility: checks declared before first execution.

2026-10-13. Author verification after analytic derivation (Paper 60, Section
8.10), not blind discovery. Retain all run logs and report failures. Do not
overwrite earlier certificates or their results.

Claim under test (Theorem 8.9). Unit-friction overdamped network, deterministic
(open-loop) additive force f(t) on the boundary only, f(0-)=0 and f=0 eventually.
Mean extracted work W = int m_x . df. Then
  sup W = 1/2 m_x^T K_B m_x + 1/2 z^T C^{1/2} Pi_inf C^{1/2} z,  z = m_y - L m_x,
i.e. minimal dissipation V = (Cz)^T (C+F)^{-1} (Cz), and for thermal-covariance
mean shifts sup W = T [D(rho_B||sigma_B) + D_inf], loss = T (J - D_inf).

H1 exact (SymPy): scalar symbolic c,b: G=1/(c+f) solves 1-G b^2 G-2cG=0;
   closed-loop rate b^2 G + c = f; harvest fraction 1-2c/(c+f) = pi_inf (8.10).
   c=3,b=4: stabilizing PSD Riccati solution of the (x,y) control problem is
   P = w w^T/8 with w=(4,3); harvest fraction exactly 1/4.
H2 matrix identities, Paper 60 witness + 200 random networks with boundary and
   hidden dimensions in {1,2,3,4} (non-square B, noncommuting C, B^T B):
   Riccati residual and closed-loop identity B^T B G + C = (C+F) F (C+F)^{-1}
   both < 1e-11
   (relative). INDEPENDENT value: backward integration of the free-end LQ
   Riccati ODE to convergence gives P with |P - [B;C] G [B;C]^T| < 1e-7
   (relative), and harvest matrix I - 2 C^{-1/2} P_yy C^{-1/2} agrees with
   Pi_inf computed from the information Riccati limit (8.8) to < 1e-7.
H3 time-domain Sekimoto work along the explicit protocol (closed-loop phase on
   the means, then linear return of x over tau_r, then f switched off):
   (a) Sekimoto work equals E0 - dissipation - final energy to 1e-8;
   (b) W(tau_r) <= W* + 1e-10 for tau_r in {25,50,100,200,400}, increasing;
   (c) Richardson 2W(400)-W(200) within 1e-4 (relative) of W*.
H4 stochastic: exact Gaussian transitions of the FULL network, 20000 paths,
   piecewise-constant version of the H3 protocol (tau_r=50, dt=0.01), with a
   NONthermal covariance preparation V=S/3 and nonthermal boundary variance.
   Mean extracted work agrees with the exact mean-only prediction within
   4 standard errors; that prediction is within 1% of the continuous W(50).
H5 no admissible protocol beats W*: 400 random piecewise-constant protocols
   (random bumps, and perturbations of the optimal protocol) evaluated exactly
   with discrete transitions: every W <= W* + 1e-10. f == 0 gives W = 0.
H6 strictness: for thermal-covariance mean shifts W*/(T D_inf(mean)) = 1 to
   1e-10 (D_inf from (8.2)); for Paper 60 witness (a, V=S/3) W* < T D_inf and
   both are reported.
H7 ignorance corollary: binary preparation (prior 1/2) between mean residual z
   and 0, common m_x. Average Sekimoto work of the protocol built for the prior
   mean equals T D_inf(mean of alpha) (Richardson, 1e-4 rel). Penalty equals
   (T/2) tr(Pi Cov alpha) to 1e-4 rel and exceeds T I(theta; record) computed
   by quadrature.
C1 controls: a protocol built with the wrong gain G'=(2C)^{-1} harvests
   strictly less than W*; full actuation (force on every coordinate) has zero
   minimal dissipation in the same backward-Riccati solver (fraction 1).

Run 1 (harvest_run1.log): 5/8. Repairs before run 2, criteria otherwise unchanged:
 - H2: the declared identity B^T B G + C = F is false for noncommuting C, B^T B
   (error 0.19). Correct: B^T B G + C = X F X^{-1}, X = C+F, since
   X C X^{-1} != C. It is similar to F, so w still decays at the rates of F and
   the theorem's proof is unaffected. The paper states the corrected identity.
 - H7: quadrature integrand underflowed (0*log 0 -> nan); rewritten in
   log-sum-exp form.
 - C1: full actuation was mis-specified (hidden actuation added to, rather than
   replacing, the hidden relaxation velocity in the cost). Correct form: every
   velocity is a control, cost |v|^2, no state cost; solver must return P=0.
"""

from pathlib import Path
import json
import platform
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
from scipy.linalg import expm, cholesky
import sympy as sp

rows, details = [], {}
start = time.perf_counter()
HERE = Path(__file__).resolve().parent


def check(name, ok, detail=""):
    rows.append({"name": name, "pass": bool(ok), "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def sym(X):
    return (X + X.T) / 2


def fn(X, f):
    lam, U = np.linalg.eigh(sym(X))
    return (U * f(lam)) @ U.T


def sqrtm_psd(X):
    return fn(X, lambda l: np.sqrt(np.clip(l, 0, None)))


def blocks(K, b):
    return K[:b, :b], K[:b, b:], K[b:, b:]


def visibility(B, C, T):
    """Pi_inf from the information Riccati limit (8.8), as in Section 8."""
    F = sqrtm_psd(C @ C + B.T @ B)
    Iinf = (F - C) / (2 * T)
    S = T * np.linalg.inv(C)
    Sh = sqrtm_psd(S)
    Xi = Sh @ Iinf @ Sh
    return sym(Xi @ np.linalg.inv(np.eye(len(C)) + Xi))


def gain(B, C):
    F = sqrtm_psd(C @ C + B.T @ B)
    return F, np.linalg.inv(C + F)


def D_inf_gauss(Pi, alpha, W):
    h = len(Pi)
    Ph = sqrtm_psd(Pi)
    Om = np.eye(h) + Ph @ (W - np.eye(h)) @ Ph
    return 0.5 * (alpha @ Pi @ alpha + np.trace(Pi @ (W - np.eye(h)))
                  - np.linalg.slogdet(Om)[1])


def lq_backward(B, C, E, horizon=None):
    """Free-end LQ: minimise int |v|^2 + |w|^2, xdot=v (on actuated coords),
    ydot=-B^T x - C y. Returns P with value s^T P s. Independent of the
    closed form: integrates the Riccati ODE backward from P=0."""
    b, h = B.shape
    n = b + h
    M = np.zeros((n, n))
    M[b:, :b] = -B.T
    M[b:, b:] = -C
    Wm = np.hstack([B.T, C])
    Q = Wm.T @ Wm
    lmin = np.linalg.eigvalsh(C).min()
    if horizon is None:
        horizon = 60.0 / lmin

    def rhs(t, p):
        P = p.reshape(n, n)
        dP = M.T @ P + P @ M - P @ E @ E.T @ P + Q
        return dP.ravel()
    sol = solve_ivp(rhs, (0, horizon), np.zeros(n * n), method="LSODA",
                    rtol=1e-12, atol=1e-14)
    return sym(sol.y[:, -1].reshape(n, n))


# ---------------------------------------------------------------- H1
c, bb = sp.symbols("c b", positive=True)
f = sp.sqrt(c**2 + bb**2)
G = 1 / (c + f)
r1 = sp.simplify(1 - G * bb**2 * G - 2 * c * G)
r2 = sp.simplify(bb**2 * G + c - f)
frac = sp.simplify(1 - 2 * c**2 * G / c - (f - c) / (f + c))
p11, p12, p22 = sp.symbols("p11 p12 p22", real=True)
P = sp.Matrix([[p11, p12], [p12, p22]])
Mm = sp.Matrix([[0, 0], [-4, -3]])
Ee = sp.Matrix([1, 0])
w = sp.Matrix([4, 3])
R = Mm.T * P + P * Mm - P * Ee * Ee.T * P + w * w.T
sols = sp.solve([R[0, 0], R[0, 1], R[1, 1]], [p11, p12, p22], dict=True)
psd = [s for s in sols if all(sp.N(e) >= -1e-30 for e in P.subs(s).eigenvals())]
ok = (r1 == 0 and r2 == 0 and frac == 0 and len(psd) == 1
      and sp.simplify(P.subs(psd[0]) - w * w.T / 8) == sp.zeros(2)
      and 1 - 2 * psd[0][p22] / 3 == sp.Rational(1, 4))
check("H1 scalar exact", ok,
      f"Riccati residual {r1}, closed loop {r2}, fraction-pi {frac}; P={psd[0] if psd else None}")

# ---------------------------------------------------------------- witness
Aw = np.array([[5., -1], [-1, 6]])
Bw = np.array([[-1., 0], [-1, -2]])
Cw = np.array([[5., -1], [-1, 5]])
Tw = 1.5


def h2_case(B, C, T):
    b, h = B.shape
    F, G = gain(B, C)
    res = np.linalg.norm(np.eye(h) - G @ B.T @ B @ G - G @ C - C @ G)
    X = C + F
    cl = np.linalg.norm(B.T @ B @ G + C - X @ F @ np.linalg.inv(X)) / np.linalg.norm(F)
    P = lq_backward(B, C, np.vstack([np.eye(b), np.zeros((h, b))]))
    Wm = np.vstack([B, C])
    Pc = Wm @ G @ Wm.T
    perr = np.linalg.norm(P - Pc) / np.linalg.norm(Pc)
    Cmh = fn(C, lambda l: l**-0.5)
    H = sym(np.eye(h) - 2 * Cmh @ P[b:, b:] @ Cmh)
    Pi = visibility(B, C, T)
    herr = np.linalg.norm(H - Pi) / max(np.linalg.norm(Pi), 1e-300)
    return res, cl, perr, herr


rng = np.random.default_rng(20261013)
worst = np.zeros(4)
cases = [h2_case(Bw, Cw, Tw)]
for k in range(200):
    b, h = rng.integers(1, 5, size=2)
    X = rng.normal(size=(b + h, b + h))
    K = X @ X.T + 0.3 * np.eye(b + h)
    _, B, C = blocks(K, b)
    cases.append(h2_case(B, C, rng.uniform(0.1, 5)))
worst = np.max(np.array(cases), axis=0)
w0 = cases[0]
check("H2 matrix identities + independent LQ", worst[0] < 1e-11 and worst[1] < 1e-11
      and worst[2] < 1e-7 and worst[3] < 1e-7,
      f"worst over 201: Riccati {worst[0]:.2e}, closed loop {worst[1]:.2e}, "
      f"P vs closed form {worst[2]:.2e}, harvest vs Pi_inf {worst[3]:.2e}; "
      f"witness harvest-vs-Pi {w0[3]:.2e}")
details["H2"] = {"worst": worst.tolist()}

# ---------------------------------------------------------------- strong witness for H3-H5
A = np.array([[6., 1], [1, 5]])
B = np.array([[-2., 1], [-1, -3]])
C = np.array([[4., -1], [-1, 3]])
K = np.block([[A, B], [B.T, C]])
assert np.linalg.eigvalsh(K).min() > 0
T = 0.2
b, h = 2, 2
L = -np.linalg.solve(C, B.T)
KB = A - B @ np.linalg.solve(C, B.T)
mx0 = np.array([0.3, -0.2])
z0 = np.array([1.0, -0.7])
my0 = L @ mx0 + z0
F, G = gain(B, C)
Pi = visibility(B, C, T)
S = T * np.linalg.inv(C)
Smh = fn(S, lambda l: l**-0.5)
alpha = Smh @ z0
E0 = 0.5 * mx0 @ KB @ mx0 + 0.5 * z0 @ C @ z0
Vmin = (C @ z0) @ G @ (C @ z0)
Wstar = E0 - Vmin
Wpred = 0.5 * mx0 @ KB @ mx0 + 0.5 * T * alpha @ Pi @ alpha
details["strong"] = {"E0": E0, "Vmin": Vmin, "Wstar": Wstar, "Wpred": Wpred,
                     "Pi_eigs": np.linalg.eigvalsh(Pi).tolist()}
tau1 = 30.0 / np.linalg.eigvalsh(F).min()


def protocol_path(mx, my, Gp, tau_r, dense=False):
    """Means under the explicit protocol; returns Sekimoto work and dissipation."""
    Fp = B.T @ B @ Gp + C   # closed-loop matrix for w

    def ph1(t, s):
        x, y = s[:b], s[b:b + h]
        wv = B.T @ x + C @ y
        xd = -B @ Gp @ wv
        yd = -wv
        wd = B.T @ xd + C @ yd
        fd = -B @ Gp @ wd + A @ xd + B @ yd   # d/dt (xd + A x + B y)
        return np.concatenate([xd, yd, [x @ fd, xd @ xd + yd @ yd]])
    s0 = np.concatenate([mx, my, [0.0, 0.0]])
    wv0 = B.T @ mx + C @ my
    f0 = -B @ Gp @ wv0 + A @ mx + B @ my
    W = mx @ f0                              # jump at t=0
    s1 = solve_ivp(ph1, (0, tau1), s0, rtol=1e-12, atol=1e-14,
                   dense_output=dense)
    x1, y1 = s1.y[:b, -1], s1.y[b:b + h, -1]
    W += s1.y[-2, -1]
    diss = s1.y[-1, -1]
    xd_before = -B @ Gp @ (B.T @ x1 + C @ y1)
    xd_after = -x1 / tau_r
    W += x1 @ (xd_after - xd_before)         # jump at tau1

    def ph2(t, s):
        x, y = s[:b], s[b:b + h]
        xd = xd_after
        yd = -B.T @ x - C @ y
        fd = A @ xd + B @ yd
        return np.concatenate([xd, yd, [x @ fd, xd @ xd + yd @ yd]])
    s2 = solve_ivp(ph2, (0, tau_r), np.concatenate([x1, y1, [0.0, 0.0]]),
                   rtol=1e-12, atol=1e-14, dense_output=dense)
    W += s2.y[-2, -1]
    diss += s2.y[-1, -1]
    y2 = s2.y[b:b + h, -1]
    Efin = 0.5 * y2 @ C @ y2                 # x=0: jump work zero, then free decay
    return W, diss, Efin, (s1, s2, xd_after)


taus = [25, 50, 100, 200, 400]
Ws = []
bal = 0
for tr in taus:
    Wv, dv, ef, _ = protocol_path(mx0, my0, G, tr)
    Ws.append(Wv)
    bal = max(bal, abs(Wv - (E0 - dv - ef)))
rich = 2 * Ws[-1] - Ws[-2]
ok = (bal < 1e-8 and all(x <= Wstar + 1e-10 for x in Ws)
      and all(np.diff(Ws) > 0) and abs(rich - Wstar) / Wstar < 1e-4
      and abs(Wstar - Wpred) < 1e-12)
check("H3 Sekimoto work approaches W*", ok,
      f"energy balance {bal:.1e}; W(tau_r)={['%.9f' % x for x in Ws]}; "
      f"Richardson {rich:.9f} vs W*={Wstar:.9f} (closed form {Wpred:.9f})")
details["H3"] = {"taus": taus, "W": Ws, "richardson": rich}

# ---------------------------------------------------------------- H4 stochastic, piecewise-constant protocol
dt = 0.01
tr = 50.0
_, _, _, (s1, s2, xd_after) = protocol_path(mx0, my0, G, tr, dense=True)
n1 = int(round(tau1 / dt))
n2 = int(round(tr / dt))
t1 = np.arange(n1) * dt
t2 = np.arange(n2) * dt
X1 = s1.sol(t1)
X2 = s2.sol(t2)
f1 = (-B @ G @ (B.T @ X1[:b] + C @ X1[b:b + h])) + A @ X1[:b] + B @ X1[b:b + h]
f2 = xd_after[:, None] + A @ X2[:b] + B @ X2[b:b + h]
fs = np.hstack([f1, f2]).T                    # f_k on [t_k, t_k+dt)
nrel = int(round(10.0 / dt))
fs = np.vstack([fs, np.zeros((nrel, b))])
Ph = expm(-K * dt)
Kinv = np.linalg.inv(K)
Psi = (np.eye(4) - Ph) @ Kinv                 # commutes with K
Sig = T * Kinv @ (np.eye(4) - Ph @ Ph)
Lc = cholesky(sym(Sig), lower=True)


def pc_mean_work(m0, fseq):
    m = m0.copy()
    W = 0.0
    fprev = np.zeros(b)
    for fk in fseq:
        W += m[:b] @ (fk - fprev)
        fprev = fk
        m = Ph @ m + Psi[:, :b] @ fk
    W += m[:b] @ (0 - fprev)
    return W


m0 = np.concatenate([mx0, my0])
Wpc = pc_mean_work(m0, fs)
N = 20000
V = S / 3
xcov = 2.0 * T * np.linalg.inv(KB)
x0s = mx0 + rng.multivariate_normal(np.zeros(b), xcov, size=N)
zs = z0 + rng.multivariate_normal(np.zeros(h), V, size=N)
q = np.hstack([x0s, x0s @ L.T + zs])
Wmc = np.zeros(N)
fprev = np.zeros(b)
PhT, PsiE = Ph.T, Psi[:, :b]
for fk in fs:
    Wmc += q[:, :b] @ (fk - fprev)
    fprev = fk
    q = q @ PhT + (PsiE @ fk)[None, :] + rng.standard_normal((N, 4)) @ Lc.T
Wmc += q[:, :b] @ (0 - fprev)
mc, se = Wmc.mean(), Wmc.std(ddof=1) / np.sqrt(N)
ok = abs(mc - Wpc) <= 4 * se and abs(Wpc - Ws[1]) / Ws[1] < 0.01
check("H4 full-network Monte Carlo, nonthermal covariance", ok,
      f"MC {mc:.5f} +/- {se:.5f}; exact pc mean prediction {Wpc:.5f}; "
      f"continuous W(50) {Ws[1]:.5f}; z-score {(mc - Wpc) / se:.2f}")
details["H4"] = {"mc": mc, "se": se, "Wpc": Wpc, "N": N, "dt": dt}

# ---------------------------------------------------------------- H5 no protocol beats W*
best = -np.inf
tgrid = np.arange(len(fs)) * dt
for k in range(400):
    if k % 2 == 0:
        fr = np.zeros_like(fs)
        for _ in range(rng.integers(1, 6)):
            c0, wd = rng.uniform(0, 40), rng.uniform(0.3, 8)
            fr += np.exp(-0.5 * ((tgrid - c0) / wd)**2)[:, None] * rng.normal(0, 3, size=b)
        fr[-nrel:] = 0
    else:
        eps = 10**rng.uniform(-4, -0.5)
        fr = fs + eps * np.cumsum(rng.normal(size=fs.shape), axis=0) * np.sqrt(dt)
        fr[-nrel:] = 0
    best = max(best, pc_mean_work(m0, fr))
Wzero = pc_mean_work(m0, np.zeros_like(fs))
check("H5 no admissible protocol exceeds W*", best <= Wstar + 1e-10 and abs(Wzero) < 1e-15,
      f"best random {best:.9f} <= W* {Wstar:.9f}; optimal pc {Wpc:.9f}; f=0 gives {Wzero:.1e}")
details["H5"] = {"best": best, "Wstar": Wstar}

# ---------------------------------------------------------------- H6 strictness
Dmean = D_inf_gauss(Pi, alpha, np.eye(h))
ratio = Wstar_hidden = 0.5 * T * alpha @ Pi @ alpha
r_mean = Wstar_hidden / (T * Dmean)
Pw = visibility(Bw, Cw, Tw)
Sw = Tw * np.linalg.inv(Cw)
aw = fn(Sw, lambda l: l**-0.5) @ np.array([0.4, -0.6])
Dw = D_inf_gauss(Pw, aw, np.eye(2) / 3)
Jw = 0.5 * (aw @ aw + np.trace(np.eye(2) / 3 - np.eye(2)) - np.log(1 / 9))
Hw = 0.5 * Tw * aw @ Pw @ aw
ok = abs(r_mean - 1) < 1e-10 and Hw < Tw * Dw and abs(Dw - 0.011954085736) < 1e-9
check("H6 equality for mean shifts, strict for covariance preparations", ok,
      f"mean shift W/(T D)={r_mean:.12f}; witness: harvest {Hw:.9f}, T*D_inf {Tw * Dw:.9f}, "
      f"T*J {Tw * Jw:.9f}; harvest/(T D_inf)={Hw / (Tw * Dw):.6f}, harvest/(T J)={Hw / (Tw * Jw):.6f}")
details["H6"] = {"witness_harvest": Hw, "witness_TD": Tw * Dw, "witness_TJ": Tw * Jw}

# ---------------------------------------------------------------- H7 ignorance
zbar = z0 / 2
mybar = L @ mx0 + zbar
Wi = []
for tr7 in (200, 400):
    Wbar, _, _, _ = protocol_path(mx0, mybar, G, tr7)
    Wi.append(Wbar)
# work of hypothesis theta under protocol f: W_theta = W_bar + int dev_x(t) . df(t);
# check the cross term averages to zero numerically on the discrete protocol.
_, _, _, (p1, p2, xa) = protocol_path(mx0, mybar, G, 50.0, dense=True)
Y1 = p1.sol(t1)
Y2 = p2.sol(np.arange(int(round(50.0 / dt))) * dt)
g1 = (-B @ G @ (B.T @ Y1[:b] + C @ Y1[b:b + h])) + A @ Y1[:b] + B @ Y1[b:b + h]
g2 = xa[:, None] + A @ Y2[:b] + B @ Y2[b:b + h]
gs = np.vstack([np.hstack([g1, g2]).T, np.zeros((nrel, b))])
Wth = [pc_mean_work(np.concatenate([mx0, L @ mx0 + zt]), gs) for zt in (z0, np.zeros(h))]
Wbar_pc = pc_mean_work(np.concatenate([mx0, mybar]), gs)
avg_identity = abs(0.5 * sum(Wth) - Wbar_pc)
rich_i = 2 * Wi[1] - Wi[0]
abar = Smh @ zbar
Wign_pred = 0.5 * mx0 @ KB @ mx0 + 0.5 * T * abar @ Pi @ abar
Wknown = 0.5 * (Wstar + (0.5 * mx0 @ KB @ mx0))
penalty = Wknown - Wign_pred
Sig_a = np.outer(alpha, alpha) / 4
pen_pred = 0.5 * T * np.trace(Pi @ Sig_a)
delta = np.sqrt(alpha @ Pi @ alpha)            # record statistic: N(0 or delta e, I)


def mi_binary(d):
    def integrand(u):
        l0, l1 = -0.5 * u**2, -0.5 * (u - d)**2
        lm = np.logaddexp(l0, l1) - np.log(2)
        return 0.5 * (np.exp(l0) * (l0 - lm) + np.exp(l1) * (l1 - lm)) / np.sqrt(2 * np.pi)
    return quad(integrand, -40, 40 + d, limit=400, epsabs=1e-14)[0]


Irec = mi_binary(delta)
ok = (avg_identity < 1e-10 and abs(rich_i - Wign_pred) / Wign_pred < 1e-4
      and abs(penalty - pen_pred) / pen_pred < 1e-10 and penalty > T * Irec)
check("H7 ignorance penalty and record information", ok,
      f"averaging identity {avg_identity:.1e}; W_ign Richardson {rich_i:.9f} vs {Wign_pred:.9f}; "
      f"penalty {penalty:.6f} = (T/2)tr(Pi Cov a) {pen_pred:.6f} > T*I(theta;record) {T * Irec:.6f} "
      f"(I={Irec:.6f} nats, Gaussian bound {0.5 * np.log(1 + delta**2 / 4):.6f})")
details["H7"] = {"penalty": penalty, "T_I": T * Irec, "I": Irec}

# ---------------------------------------------------------------- C1 controls
Gwrong = np.linalg.inv(2 * C)
Ww = [protocol_path(mx0, my0, Gwrong, tr)[0] for tr in (200, 400)]
rich_w = 2 * Ww[1] - Ww[0]
def lq_full(n, horizon=20.0):
    sol = solve_ivp(lambda t, p: -(p.reshape(n, n) @ p.reshape(n, n)).ravel(),
                    (0, horizon), np.zeros(n * n), rtol=1e-12, atol=1e-14)
    return sol.y[:, -1].reshape(n, n)


Pfull = lq_full(4)
ok = rich_w < Wstar - 1e-6 and np.linalg.norm(Pfull) < 1e-6
check("C1 controls", ok,
      f"wrong-gain harvest {rich_w:.9f} < W* {Wstar:.9f}; full-actuation minimal dissipation norm {np.linalg.norm(Pfull):.1e}")

elapsed = time.perf_counter() - start
npass = sum(r["pass"] for r in rows)
print(f"\n{npass}/{len(rows)} passed in {elapsed:.2f} s "
      f"(Python {platform.python_version()}, NumPy {np.__version__}, SciPy {scipy.__version__}, SymPy {sp.__version__})")
(HERE / "harvest_cert_results.json").write_text(json.dumps(
    {"rows": rows, "details": details, "elapsed_s": elapsed,
     "versions": {"python": platform.python_version(), "numpy": np.__version__,
                  "scipy": scipy.__version__, "sympy": sp.__version__}},
    indent=2, default=float))
sys.exit(0 if npass == len(rows) else 1)
