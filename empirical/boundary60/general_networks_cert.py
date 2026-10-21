"""Paper 60, Sections 9-11 and Proposition 7.3: author certificate for general thermal networks,
the canonical-correlation identification, visibility truncation, and the quantum effective oscillator.

Criteria and tolerances below were written on 2026-10-09 BEFORE the first execution of this script,
after exploratory scratch computations. This is an author check, not an independent review.
Brute-force comparisons never use the reduced observation model: they sample the FULL network's
exact Gaussian transitions and compute the KL of the sampled boundary record directly.

G1  Overdamped, arbitrary friction (Prop. 9.3): closed form with effective (C~,B~) agrees with the
    correlated-noise Riccati to 1e-9, and with second-order Richardson extrapolation of the
    full-network sampled KL (n=200,400,800) to relative 1e-6.
G2  Inertial, block-diagonal friction (Thm. 9.2): Riccati + (8.2) vs first-order Richardson of the
    full-network sampled KL (n=100,200,400), relative 1e-6.
G3  Inertial, cross friction (Thm. 9.2, correlated noise): same comparison, relative 1e-6.
G4  Undamped boundary direction (Thm. 9.5): Bryson-Johansen formula vs 45-digit brute force
    (n=20,40,80), two-step Richardson, relative 2e-5; mean shift on the predicted exactly visible
    direction has D/J errors shrinking by >= 6x per halving, final error < 1e-5.
G5  Private-bath principle (Thm. 9.4, Cor. 9.6): scalar common bath lambda(1000) > 0.997 and lambda
    increasing on tau=1,10,100,1000; matching private baths |lambda(1000)-lambda(100)| < 1e-6;
    an undamped DARK hidden mode keeps |lambda(400)-lambda(100)| < 1e-8; making that mode visible
    raises lambda(400) above lambda(100)+0.1.
G6  Approach rate (Prop. 9.7): (1-lambda_tau)tau extrapolated in 1/tau matches
    4 w^2/((B phi)^T Phi(i w)^{-1} (B phi)) to relative 3e-3, for Gamma_II = 0 and for Gamma_II != 0.
G7  Scalar inertial closed form (Prop. 9.8) vs numerical ARE to 1e-12 (4 random cases); overdamped
    limit |Pi_yy(gamma=100) - tan^2(theta/2)| < 1e-4, Pi_yy decreasing along the friction grid.
G8  Noncommuting inertial gauge (Prop. 9.9): O orthogonal to 1e-10 with rotation angle > 0.1 deg;
    commuting example angle < 1e-8 deg.
C1  Canonical correlations, overdamped (Thm. 10.1): two-step Richardson of exact increment-covariance
    canonical correlations (dt=0.02,0.01,0.005) matches eig(Pi_inf) to relative 1e-3, two networks.
C2  Canonical correlations, inertial: first-order Richardson (dt=0.02,0.01) matches
    sv(Pi^{1/2} eps Pi^{1/2}) to relative 2e-3; and sigma_1 < lambda_max(Pi).
C3  Riccati Hamiltonian eigenvalues are zeros of det[Z_B(s)+Z_B(-s)^T] (Prop. 10.3): |det Phi|/||Phi||^b < 1e-11.
C4  Tracking (Prop. 10.4): forward Kalman steady state equals eps (S^-1 + I_inf)^-1 eps to 1e-10 (inertial),
    and 2T (C+F)^-1 to 1e-12 (overdamped).
C5  Information budget (Rem. 10.5) for the Section 8.7 witness: stored - transmitted = (1/2) sum log(1+pi) to 1e-14.
R1  Visibility truncation (Thm. 11.1): over 200 random truncations, reduced-network visibilities equal the kept
    ones to 1e-10, K_r > 0, and the boundary Schur complement equals K_B to 1e-12.
R2  Error law (Obs. 11.2): over 500 random truncations, max err/[prod((1+pi)/(1-pi))^2 - 1] <= 1.01 and median >= 0.9;
    visibility truncation has smaller sup error than the best of two modal truncations in >= 90% of cases.
R3  Chain spectrum (Obs. 11.3): m=k=1, consecutive ratios of the top 6 visibilities agree to 1%, and top 6 agree
    between n=20 and n=30 to relative 1e-3.
Q1  Effective quantum oscillator (Prop. 7.3): 2 sqrt(X P) > 1, k_eff < K_B for the Prop. 7.1 witness;
    at T=100, |m_eff - 1| < 1e-3 and |k_eff - K_B| < 1e-3.
"""
import json, sys, time, platform
import numpy as np, scipy, mpmath as mp
from scipy.linalg import expm, sqrtm, solve_sylvester, solve_continuous_are, eig
from scipy.integrate import solve_ivp
sys.stdout.reconfigure(encoding="utf-8")
t_start = time.time()
results = []
def check(name, ok, detail):
    results.append({"check": name, "pass": bool(ok), "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)

def rsq(M): return np.real(sqrtm(M))
def klg(m1, S1, m0, S0):
    d = m1 - m0; c0 = np.linalg.cholesky(S0)
    A = np.linalg.solve(c0, S1); A = np.linalg.solve(c0, A.T).T; e = np.linalg.solve(c0, d)
    return 0.5 * (np.trace(A) + e @ e - len(d) - np.linalg.slogdet(A)[1])
def Dform(Pi, al, W):
    n = len(al); Ph = rsq(Pi); Om = np.eye(n) + Ph @ (W - np.eye(n)) @ Ph
    return 0.5 * (al @ Pi @ al + np.trace(Pi @ (W - np.eye(n))) - np.linalg.slogdet(Om)[1])
def Jform(al, W): return 0.5 * (al @ al + np.trace(W) - len(al) - np.linalg.slogdet(W)[1])
def vis(I, S):
    Sh = rsq(S); X = Sh @ I @ Sh; return X @ np.linalg.inv(np.eye(len(X)) + X)
def ric(HRH, F, Q, tau, method="LSODA"):
    n = len(F)
    f = lambda t, v: (lambda I: (HRH + F.T @ I + I @ F - I @ Q @ I).ravel())(v.reshape(n, n))
    I = solve_ivp(f, (0, tau), np.zeros(n * n), rtol=1e-11, atol=1e-13, method=method).y[:, -1].reshape(n, n)
    return (I + I.T) / 2
def pi_overdamped(C, B):
    F = rsq(C @ C + B.T @ B); X = solve_sylvester(C, F, B.T @ B); X = (X + X.T) / 2
    Ci = np.linalg.inv(rsq(C)); Xi = 0.5 * Ci @ X @ Ci; return Xi @ np.linalg.inv(np.eye(len(C)) + Xi)

def inertial_model(A, B, C, G, T):
    """unit mass, full friction G; returns HRH, F', Q', S (correlated-noise decorrelated)."""
    b, h = len(A), len(C); GBB, GBI, GIB, GII = G[:b, :b], G[:b, b:], G[b:, :b], G[b:, b:]
    F = np.block([[np.zeros((h, h)), np.eye(h)], [-C, -GII]])
    H = -np.hstack([B, GBI]); R = 2 * T * GBB; N = np.zeros((2 * h, b)); N[h:] = 2 * T * GIB
    Q = np.zeros((2 * h, 2 * h)); Q[h:, h:] = 2 * T * GII
    Fp = F - N @ np.linalg.solve(R, H); Qp = Q - N @ np.linalg.solve(R, N.T); HRH = H.T @ np.linalg.solve(R, H)
    S = T * np.block([[np.linalg.inv(C), np.zeros((h, h))], [np.zeros((h, h)), np.eye(h)]])
    return HRH, Fp, Qp, S

def sampled_stack(Fz, Sinf, O, m0, S0, dt, n):
    Phi = expm(Fz * dt); Ps = [np.eye(len(Fz))]
    for _ in range(n): Ps.append(Phi @ Ps[-1])
    SO = [(P @ S0 @ P.T + Sinf - P @ Sinf @ P.T) @ O.T for P in Ps]; OP = [O @ P for P in Ps]
    b = O.shape[0]; M = np.concatenate([OP[k] @ m0 for k in range(n + 1)]); Cv = np.zeros((b * (n + 1),) * 2)
    for k in range(n + 1):
        for j in range(k + 1):
            blk = OP[k - j] @ SO[j]; Cv[k*b:(k+1)*b, j*b:(j+1)*b] = blk; Cv[j*b:(j+1)*b, k*b:(k+1)*b] = blk.T
    return M, Cv

def brute_inertial(A, B, C, G, T, tau, a, V, n):
    b, h = len(A), len(C); N = b + h; K = np.block([[A, B], [B.T, C]])
    Fz = np.block([[np.zeros((N, N)), np.eye(N)], [-K, -G]])
    Sinf = np.block([[T * np.linalg.inv(K), np.zeros((N, N))], [np.zeros((N, N)), T * np.eye(N)]])
    L = -np.linalg.solve(C, B.T); KB = A - B @ np.linalg.solve(C, B.T)
    U = np.zeros((2*N, 2*N)); U[0:b, 0:b] = np.eye(b); U[b:N, 0:b] = L; U[b:N, 2*b:2*b+h] = np.eye(h)
    U[N:N+b, b:2*b] = np.eye(b); U[N+b:, 2*b+h:] = np.eye(h)
    mu = np.block([[T * np.linalg.inv(KB), np.zeros((b, b))], [np.zeros((b, b)), T * np.eye(b)]])
    Sref = T * np.block([[np.linalg.inv(C), np.zeros((h, h))], [np.zeros((h, h)), np.eye(h)]])
    def law(m, Vz):
        return U @ np.concatenate([np.zeros(2*b), m]), U @ np.block([[mu, np.zeros((2*b, 2*h))], [np.zeros((2*h, 2*b)), Vz]]) @ U.T
    O = np.zeros((b, 2*N)); O[:, :b] = np.eye(b)
    return klg(*sampled_stack(Fz, Sinf, O, *law(a, V), tau/n, n), *sampled_stack(Fz, Sinf, O, *law(np.zeros(2*h), Sref), tau/n, n))

rng = np.random.default_rng(20261009)

# ---------------- G1 overdamped arbitrary friction ----------------
T, tau = 0.8, 1.2
A = np.array([[4., -1], [-1, 5]]); B = np.array([[-1., 0.3], [-0.7, -1.2]]); C = np.array([[3., -1], [-1, 2.5]])
K = np.block([[A, B], [B.T, C]]); b = h = 2
Gm = rng.normal(size=(4, 4)); G = Gm @ Gm.T / 3 + 0.4 * np.eye(4); Mo = np.linalg.inv(G)
MBB, MBI, MIB, MII = Mo[:b, :b], Mo[:b, b:], Mo[b:, :b], Mo[b:, b:]; GII = G[b:, b:]; GIh = rsq(GII)
Ct = np.linalg.inv(GIh) @ C @ np.linalg.inv(GIh); Bt = np.linalg.inv(rsq(MBB)) @ (MBB @ B + MBI @ C) @ np.linalg.inv(GIh)
f = lambda t, v: (lambda R: (Ct @ Ct + Bt.T @ Bt - R @ R).ravel())(v.reshape(h, h))
R_ = solve_ivp(f, (0, tau), Ct.ravel(), rtol=1e-12, atol=1e-14, method="DOP853").y[:, -1].reshape(h, h); R_ = (R_ + R_.T) / 2
Cth = rsq(Ct); Xi = 0.5 * np.linalg.inv(Cth) @ (R_ - Ct) @ np.linalg.inv(Cth); Pi_c = Xi @ np.linalg.inv(np.eye(h) + Xi)
S = T * np.linalg.inv(C); a = np.array([0.5, -0.8]); V = rsq(S) @ np.diag([0.4, 2.0]) @ rsq(S)
Sp = T * np.linalg.inv(Ct); Sph = rsq(Sp); ap = GIh @ a; Vp = GIh @ V @ GIh.T
al = np.linalg.solve(Sph, ap); W = np.linalg.solve(Sph, np.linalg.solve(Sph, Vp).T).T
D_closed = Dform(Pi_c, al, W)
# correlated-noise Riccati in physical coordinates
H = -(MBB @ B + MBI @ C); Rn = 2 * T * MBB; Nn = 2 * T * MIB; Qn = 2 * T * MII; F0 = -(MIB @ B + MII @ C)
Fp = F0 - Nn @ np.linalg.solve(Rn, H); Qp = Qn - Nn @ np.linalg.solve(Rn, Nn.T)
Pi_r = vis(ric(H.T @ np.linalg.solve(Rn, H), Fp, Qp, tau), S); Sh = rsq(S)
D_ric = Dform(Pi_r, np.linalg.solve(Sh, a), np.linalg.solve(Sh, np.linalg.solve(Sh, V).T).T)
def brute_od(n):
    Sinf = T * np.linalg.inv(K); L = -np.linalg.solve(C, B.T); KB = A - B @ np.linalg.solve(C, B.T)
    U = np.zeros((4, 4)); U[:2, :2] = np.eye(2); U[2:, :2] = L; U[2:, 2:] = np.eye(2)
    def law(m, Vz): return U @ np.concatenate([np.zeros(2), m]), U @ np.block([[T*np.linalg.inv(KB), np.zeros((2, 2))], [np.zeros((2, 2)), Vz]]) @ U.T
    O = np.zeros((2, 4)); O[:, :2] = np.eye(2)
    return klg(*sampled_stack(-Mo @ K, Sinf, O, *law(a, V), tau/n, n), *sampled_stack(-Mo @ K, Sinf, O, *law(np.zeros(2), S), tau/n, n))
d1, d2, d3 = brute_od(200), brute_od(400), brute_od(800)
rich = d3 + (d3 - d2) / 3
check("G1 overdamped arbitrary friction", abs(D_closed - D_ric) < 1e-9 and abs(rich - D_closed) / D_closed < 1e-6,
      f"closed (C~,B~) {D_closed:.10f}; correlated Riccati {D_ric:.10f}; brute n=200/400/800 {d1:.9f}/{d2:.9f}/{d3:.9f}, Richardson {rich:.10f}")

# ---------------- G2/G3 inertial ----------------
T, tau = 0.9, 1.5
A = np.array([[4., -1], [-1, 5]]); B = np.array([[-1., 0.3], [-0.7, -1.2]]); C = np.array([[3., -1], [-1, 2.5]])
GB = np.array([[0.8, 0.2], [0.2, 0.6]]); GI = np.array([[1.1, -0.3], [-0.3, 0.7]])
S4 = T * np.block([[np.linalg.inv(C), np.zeros((2, 2))], [np.zeros((2, 2)), np.eye(2)]]); S4h = rsq(S4)
al4 = np.array([0.7, -0.4, 0.5, 0.9]); Qr, _ = np.linalg.qr(rng.normal(size=(4, 4))); W4 = Qr @ np.diag([0.5, 1.8, 0.3, 2.2]) @ Qr.T
for name, G in (("G2 inertial block-diagonal friction", np.block([[GB, np.zeros((2, 2))], [np.zeros((2, 2)), GI]])),
                ("G3 inertial cross friction", (lambda Gh: Gh @ Gh.T / 4 + 0.2 * np.eye(4))(rng.normal(size=(4, 4))))):
    HRH, Fp, Qp, S_ = inertial_model(A, B, C, G, T); Pi = vis(ric(HRH, Fp, Qp, tau), S_)
    Df = Dform(Pi, al4, W4); bs = [brute_inertial(A, B, C, G, T, tau, S4h @ al4, S4h @ W4 @ S4h, n) for n in (100, 200, 400)]
    rich = 2 * bs[2] - bs[1]
    check(name, abs(rich - Df) / Df < 1e-6, f"formula {Df:.9f}; brute {bs[0]:.8f}/{bs[1]:.8f}/{bs[2]:.8f}; Richardson {rich:.9f}; Gamma_BI={np.round(G[:2,2:],3).tolist()}")

# ---------------- G4 Bryson-Johansen vs 45-digit brute ----------------
mp.mp.dps = 45
gd = 0.8; Bd, Bu = B[:1], B[1:]
Fh = np.block([[np.zeros((2, 2)), np.eye(2)], [-C, -GI]])
Hh = -np.vstack([np.hstack([Bd, np.zeros((1, 2))]), np.hstack([Bu @ C, Bu @ GI])])
Rh = np.diag([2 * T * gd, (2 * T * Bu @ GI @ Bu.T).item()]); Nh = np.zeros((4, 2)); Nh[2:, 1:] = 2 * T * GI @ Bu.T
Qh = np.zeros((4, 4)); Qh[2:, 2:] = 2 * T * GI
Fhp = Fh - Nh @ np.linalg.solve(Rh, Hh); Qhp = Qh - Nh @ np.linalg.solve(Rh, Nh.T)
Ic = ric(Hh.T @ np.linalg.solve(Rh, Hh), Fhp, Qhp, tau, "DOP853"); Ich = rsq(Ic)
E = np.block([[Bu, np.zeros((1, 2))], [np.zeros((1, 2)), Bu]])
def datalaw(m, P):
    Gd = np.vstack([E, Ich]); M = Gd @ m; Cv = Gd @ P @ Gd.T; Cv[2:, 2:] += np.eye(4); return M, Cv
a4, V4 = S4h @ al4, S4h @ np.diag([0.5, 1.8, 0.3, 2.2]) @ S4h
D_BJ = klg(*datalaw(a4, V4), *datalaw(np.zeros(4), S4))
vdir = S4h @ E.T[:, 0]; vdir /= np.linalg.norm(vdir); am = 1.3 * vdir
def mpm(M): return mp.matrix([[mp.mpf(float(x)) for x in row] for row in np.atleast_2d(M)])
def chol(Mx, n):
    L = [[mp.mpf(0)] * n for _ in range(n)]
    for j in range(n):
        L[j][j] = mp.sqrt(Mx[j][j] - mp.fsum(L[j][k] ** 2 for k in range(j)))
        for i in range(j + 1, n): L[i][j] = (Mx[i][j] - mp.fsum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]
    return L
def fsub(L, col, n):
    x = [mp.mpf(0)] * n
    for i in range(n): x[i] = (col[i] - mp.fsum(L[i][k] * x[k] for k in range(i))) / L[i][i]
    return x
def brute_mp(a, Vz, n):
    N = 4; K = np.block([[A, B], [B.T, C]]); G = np.zeros((4, 4)); G[0, 0] = gd; G[2:, 2:] = GI
    Fz = mpm(np.block([[np.zeros((N, N)), np.eye(N)], [-K, -G]]))
    Sinf = mpm(np.block([[T * np.linalg.inv(K), np.zeros((N, N))], [np.zeros((N, N)), T * np.eye(N)]]))
    L = -np.linalg.solve(C, B.T); KB = A - B @ np.linalg.solve(C, B.T)
    U = np.zeros((8, 8)); U[0:2, 0:2] = np.eye(2); U[2:4, 0:2] = L; U[2:4, 4:6] = np.eye(2); U[4:6, 2:4] = np.eye(2); U[6:8, 6:8] = np.eye(2)
    mu = np.block([[T * np.linalg.inv(KB), np.zeros((2, 2))], [np.zeros((2, 2)), T * np.eye(2)]])
    def law(m, Vv):
        return mpm(U @ np.concatenate([np.zeros(4), m]).reshape(-1, 1)), mpm(U @ np.block([[mu, np.zeros((4, 4))], [np.zeros((4, 4)), Vv]]) @ U.T)
    dt = mp.mpf(tau) / n; Phi = mp.expm(Fz * dt); O = mp.zeros(2, 8); O[0, 0] = O[1, 1] = 1
    OP = [O]; P = mp.eye(8); Ps = [P]
    for _ in range(n): P = Phi * P; Ps.append(P); OP.append(O * P)
    def stack(m0, S0):
        SO = [(Pk * S0 * Pk.T + Sinf - Pk * Sinf * Pk.T) * O.T for Pk in Ps]
        dim = 2 * (n + 1); Cv = [[mp.mpf(0)] * dim for _ in range(dim)]; M = [mp.mpf(0)] * dim
        for k in range(n + 1):
            mk = OP[k] * m0; M[2*k] = mk[0]; M[2*k+1] = mk[1]
            for j in range(k + 1):
                blk = OP[k - j] * SO[j]
                for r in range(2):
                    for c in range(2): Cv[2*k+r][2*j+c] = blk[r, c]; Cv[2*j+c][2*k+r] = blk[r, c]
        return M, Cv, dim
    M1, C1, dim = stack(*law(a, Vz)); M0, C0, _ = stack(*law(np.zeros(4), S4))
    L0 = chol(C0, dim); L1 = chol(C1, dim); tr = mp.mpf(0)
    for c in range(dim):
        col = fsub(L0, [L1[i][c] for i in range(dim)], dim); tr += mp.fsum(x * x for x in col)
    e = fsub(L0, [M1[i] - M0[i] for i in range(dim)], dim)
    ld = 2 * mp.fsum(mp.log(L1[i][i]) for i in range(dim)) - 2 * mp.fsum(mp.log(L0[i][i]) for i in range(dim))
    return float(0.5 * (tr + mp.fsum(x * x for x in e) - dim - ld))
bD = [brute_mp(a4, V4, n) for n in (20, 40, 80)]; r1 = [2 * bD[1] - bD[0], 2 * bD[2] - bD[1]]; r2 = (4 * r1[1] - r1[0]) / 3
Jm = Jform(am, np.eye(4)); eD = [1 - brute_mp(S4h @ am, S4, n) / Jm for n in (20, 40, 80)]
check("G4 degenerate boundary damping (Bryson-Johansen)", abs(r2 - D_BJ) / D_BJ < 2e-5 and eD[0] / eD[1] >= 6 and eD[1] / eD[2] >= 6 and eD[2] < 1e-5,
      f"BJ {D_BJ:.9f}; 45-digit brute {bD[0]:.8f}/{bD[1]:.8f}/{bD[2]:.8f}, two-step Richardson {r2:.9f}; exact-direction 1-D/J {eD[0]:.2e}/{eD[1]:.2e}/{eD[2]:.2e}")

# ---------------- G5 private-bath principle ----------------
A1 = np.array([[3.]]); B1 = np.array([[-1.2]]); C1 = np.array([[2.]]); g = np.array([0.9, 0.7])
def lam_seq(G, taus, A_=A1, B_=B1, C_=C1):
    HRH, Fp, Qp, S_ = inertial_model(A_, B_, C_, G, T)
    return [np.linalg.eigvalsh(vis(ric(HRH, Fp, Qp, t), S_)).max() for t in taus]
lc = lam_seq(np.outer(g, g), (1, 10, 100, 1000)); lp = lam_seq(np.diag(g ** 2), (1, 10, 100, 1000))
C2 = np.diag([2., 3.]); GI2 = np.diag([0., 1.]); GBm = np.array([[0.8, 0.2], [0.2, 0.6]])
def lam_blk(B_, taus):
    G = np.zeros((4, 4)); G[:2, :2] = GBm; G[2:, 2:] = GI2; return lam_seq(G, taus, A, B_, C2)
ld = lam_blk(np.array([[0., 1.], [0., -0.5]]), (100, 400)); lv = lam_blk(np.array([[0.4, 1.], [0., -0.5]]), (100, 400))
ok = lc[-1] > 0.997 and all(np.diff(lc) > 0) and abs(lp[-1] - lp[-2]) < 1e-6 and abs(ld[1] - ld[0]) < 1e-8 and lv[1] > lv[0] + 0.1
check("G5 private-bath principle", ok, f"common bath lambda {np.round(lc,6).tolist()}; private baths {np.round(lp,6).tolist()}; dark undamped {np.round(ld,10).tolist()}; visible undamped {np.round(lv,6).tolist()}")

# ---------------- G6 approach rate ----------------
def rate_pred(B_, C_, GI_, GB_, j):
    w2, Ph = np.linalg.eigh(C_); w = np.sqrt(w2[j]); phi = Ph[:, j]; s = 1j * (w + 1e-7)
    Pp = s*s*np.eye(len(C_)) + s*GI_ + C_; Pm = s*s*np.eye(len(C_)) - s*GI_ + C_
    Phi = GB_ + B_ @ np.linalg.solve(Pp, GI_) @ np.linalg.solve(Pm, B_.T); Phi = np.real((Phi + Phi.conj().T) / 2)
    return 4 * w * w / ((B_ @ phi) @ np.linalg.solve(Phi, B_ @ phi))
G0 = np.zeros((4, 4)); G0[:2, :2] = GBm
k0 = min(rate_pred(B, C, np.zeros((2, 2)), GBm, j) for j in range(2))
l0 = lam_seq(G0, (1000, 4000), A, B, C); e0 = [(1 - l0[0]) * 1000, (1 - l0[1]) * 4000]; x0 = (4 * e0[1] - e0[0]) / 3
B3 = np.array([[0.4, 1.], [0., -0.5]]); k1 = rate_pred(B3, C2, GI2, GBm, 0)
G1m = np.zeros((4, 4)); G1m[:2, :2] = GBm; G1m[2:, 2:] = GI2
l1 = lam_seq(G1m, (2000, 8000), A, B3, C2); e1 = [(1 - l1[0]) * 2000, (1 - l1[1]) * 8000]; x1 = (4 * e1[1] - e1[0]) / 3
check("G6 approach rate to unit visibility", abs(x0 - k0) / k0 < 3e-3 and abs(x1 - k1) / k1 < 3e-3,
      f"Gamma_II=0: predicted {k0:.5f}, extrapolated {x0:.5f}; Gamma_II!=0: predicted {k1:.5f}, extrapolated {x1:.5f}")

# ---------------- G7 scalar inertial closed form ----------------
def closed_scalar(c, b_, gb, gi):
    s = np.sqrt(c); rho = np.sqrt(c + gi * b_ * b_ / (gb * c)); lam_ = np.sqrt(gi ** 2 + 2 * s * (rho - s))
    return np.array([[(rho * lam_ - s * gi) / (2 * s * gi), (rho - s) / (2 * gi)], [(rho - s) / (2 * gi), (lam_ - gi) / (2 * gi)]])
errs = []
for _ in range(4):
    c, b_, gb, gi = rng.uniform(0.3, 4, 4)
    Ft = np.array([[0, np.sqrt(c)], [-np.sqrt(c), -gi]]); Qt = np.diag([0, 2 * gi]); Hh_ = np.diag([b_ * b_ / (2 * gb * c), 0])
    X = ric(Hh_, Ft, Qt, 400., "Radau"); errs.append(np.abs(X - closed_scalar(c, b_, gb, gi)).max())
c, b_ = 3., 4.; th = np.arctan(b_ / c * np.sqrt(2.)); grid = (0.1, 0.5, 1, 3, 10, 100)
pyy = [(lambda X: (X @ np.linalg.inv(np.eye(2) + X))[0, 0])(closed_scalar(c, b_, gm, 2 * gm)) for gm in grid]
check("G7 scalar inertial closed form and overdamped limit", max(errs) < 1e-12 and abs(pyy[-1] - np.tan(th / 2) ** 2) < 1e-4 and all(np.diff(pyy) < 0),
      f"max ARE mismatch {max(errs):.1e}; Pi_yy over gamma {np.round(pyy,6).tolist()} -> tan^2(theta/2)={np.tan(th/2)**2:.6f}")

# ---------------- G8 gauge ----------------
def gauge(B_, C_, GB_, GI_):
    G = np.zeros((4, 4)); G[:2, :2] = GB_; G[2:, 2:] = GI_; HRH, Fp, Qp, S_ = inertial_model(A, B_, C_, G, T)
    I = ric(HRH, Fp, Qp, 80.); Sh_ = rsq(S_); Xi = Sh_ @ I @ Sh_; Y = Xi + np.eye(4) / 2; X = Y[:2, 2:]
    Sg = rsq(C_); GIh_ = rsq(GI_); P = np.sqrt(2) * X @ GIh_; Kk = Sg @ np.linalg.inv(GIh_) / np.sqrt(2)
    HB = 0.5 * np.linalg.inv(Sg) @ B_.T @ np.linalg.solve(GB_, B_) @ np.linalg.inv(Sg); N_ = HB + Kk @ Kk.T
    O = np.linalg.inv(rsq(N_)) @ (P + Kk); return np.abs(O @ O.T - np.eye(2)).max(), np.degrees(np.arctan2(O[1, 0], O[0, 0]))
o1, a1 = gauge(B, C, GB, GI); o2, a2 = gauge(np.diag([1.2, 0.8]), np.diag([3., 2.]), np.diag([0.8, 0.6]), np.diag([1.1, 0.7]))
check("G8 noncommuting inertial gauge", o1 < 1e-10 and abs(a1) > 0.1 and o2 < 1e-10 and abs(a2) < 1e-8,
      f"noncommuting |OO^T-I|={o1:.1e}, angle {a1:.4f} deg; commuting |OO^T-I|={o2:.1e}, angle {a2:.1e} deg")

# ---------------- C1/C2 canonical correlations ----------------
def canon(F, S_, Hy, Rw, dt, n):
    m = len(F); Fi = np.linalg.inv(F); E1 = Fi @ (expm(F * dt) - np.eye(m)); Em1 = -Fi @ (expm(-F * dt) - np.eye(m))
    Dg = -dt * Fi + Fi @ Fi @ (expm(F * dt) - np.eye(m)); diag = Hy @ (Dg @ S_ + S_ @ Dg.T) @ Hy.T + Rw * dt
    bb = Hy.shape[0]; Nn = 2 * n; Cv = np.zeros((bb * Nn, bb * Nn)); Phi = expm(F * dt); P = np.eye(m); blocks = [diag]
    for k in range(1, Nn): blocks.append(Hy @ P @ E1 @ Em1 @ S_ @ Hy.T); P = Phi @ P
    for i in range(Nn):
        for j in range(i + 1):
            blk = blocks[i - j]; Cv[i*bb:(i+1)*bb, j*bb:(j+1)*bb] = blk; Cv[j*bb:(j+1)*bb, i*bb:(i+1)*bb] = blk.T
    Lp = np.linalg.cholesky(Cv[:bb*n, :bb*n]); Lf = np.linalg.cholesky(Cv[bb*n:, bb*n:])
    Kc = np.linalg.solve(Lf, np.linalg.solve(Lp, Cv[bb*n:, :bb*n].T).T); return np.linalg.svd(Kc, compute_uv=False)[:m]
T = 1.5; rows = []; okc = True
for Bc, Cc, nn in ((np.array([[-1., 0], [-1, -2]]), np.array([[5., -1], [-1, 5]]), 150), (np.array([[2., 1], [-1, 3]]), np.array([[1., 0.4], [0.4, 2]]), 300)):
    ev = np.sort(np.linalg.eigvalsh(pi_overdamped(Cc, Bc)))[::-1]
    cs = [canon(-Cc, T * np.linalg.inv(Cc), -Bc, 2 * T * np.eye(2), dt, int(nn * f)) for dt, f in ((0.02, 1), (0.01, 2), (0.005, 4))]
    q1 = [2 * cs[1] - cs[0], 2 * cs[2] - cs[1]]; q2 = (4 * q1[1] - q1[0]) / 3
    okc &= np.max(np.abs(q2 - ev) / ev) < 1e-3; rows.append(f"eig Pi {np.round(ev,7).tolist()} vs extrapolated {np.round(q2,7).tolist()}")
check("C1 canonical correlations = visibilities (overdamped)", okc, "; ".join(rows))
Fi_ = np.block([[np.zeros((2, 2)), np.eye(2)], [-C, -GI]]); Hy = np.hstack([-B, np.zeros((2, 2))])
Si = T * np.block([[np.linalg.inv(C), np.zeros((2, 2))], [np.zeros((2, 2)), np.eye(2)]]); Qi = np.zeros((4, 4)); Qi[2:, 2:] = 2 * T * GI
Pi_i = vis(ric(Hy.T @ np.linalg.solve(2 * T * GB, Hy), Fi_, Qi, 60.), Si); eps = np.diag([1, 1, -1, -1.]); Ph = rsq(Pi_i)
svp = np.linalg.svd(Ph @ eps @ Ph, compute_uv=False)
cs = [canon(Fi_, Si, Hy, 2 * T * GB, dt, n) for dt, n in ((0.02, 600), (0.01, 1200))]; q1 = 2 * cs[1] - cs[0]
check("C2 canonical correlations (inertial) = sv(Pi^1/2 eps Pi^1/2)", np.max(np.abs(q1 - svp) / svp) < 2e-3 and svp[0] < np.linalg.eigvalsh(Pi_i).max(),
      f"sv {np.round(svp,6).tolist()} vs extrapolated {np.round(q1,6).tolist()}; lambda_max(Pi)={np.linalg.eigvalsh(Pi_i).max():.6f}")

# ---------------- C3 Hamiltonian spectrum = impedance zeros ----------------
T = 0.9; G = np.zeros((4, 4)); G[:2, :2] = GB; G[2:, 2:] = GI
HRH, Fp, Qp, S_ = inertial_model(A, B, C, G, T); I_inf = ric(HRH, Fp, Qp, 80.)
evH = eig(np.block([[Fp, -Qp], [-HRH, -Fp.T]]))[0]
def PhiZ(s):
    Pp = s*s*np.eye(2) + s*GI + C; Pm = s*s*np.eye(2) - s*GI + C
    return GB + B @ np.linalg.solve(Pp, GI) @ np.linalg.solve(Pm, B.T)
zr = max(abs(np.linalg.det(PhiZ(s))) / np.linalg.norm(PhiZ(s)) ** 2 for s in evH)
check("C3 Hamiltonian eigenvalues = zeros of det[Z_B(s)+Z_B(-s)^T]", zr < 1e-11, f"{len(evH)} eigenvalues, max normalized |det| {zr:.1e}; closed-loop poles {np.round(np.sort_complex(np.linalg.eigvals(Fp - Qp @ I_inf)),5).tolist()}")

# ---------------- C4 tracking ----------------
Pf = solve_continuous_are(Fp.T, np.hstack([B, np.zeros((2, 2))]).T, Qp + 1e-300 * np.eye(4), 2 * T * GB)
d_in = np.abs(Pf - eps @ np.linalg.inv(np.linalg.inv(S_) + I_inf) @ eps).max()
Cw = np.array([[5., -1], [-1, 5]]); Bw = np.array([[-1., 0], [-1, -2]]); Tw = 1.5; Fw = rsq(Cw @ Cw + Bw.T @ Bw)
Pfo = solve_continuous_are(-Cw.T, Bw.T, 2 * Tw * np.eye(2), 2 * Tw * np.eye(2)); d_od = np.abs(Pfo - 2 * Tw * np.linalg.inv(Cw + Fw)).max()
check("C4 boundary tracking bound (detailed balance)", d_in < 1e-10 and d_od < 1e-12, f"inertial {d_in:.1e}; overdamped witness {d_od:.1e}")

# ---------------- C5 information budget ----------------
pw = np.sort(np.linalg.eigvalsh(pi_overdamped(Cw, Bw)))[::-1]
stored = -0.5 * np.sum(np.log1p(-pw)); trans = -0.5 * np.sum(np.log1p(-pw ** 2)); cryp = 0.5 * np.sum(np.log1p(pw))
check("C5 information budget (Section 8.7 witness)", abs(stored - trans - cryp) < 1e-14,
      f"stored {stored:.10f} nats; past-future {trans:.10f} nats; crypticity {cryp:.10f} nats; visibilities {pw.tolist()}")

# ---------------- R1/R2 truncation ----------------
def Qs(B_, C_, w): return np.eye(len(B_)) + B_ @ np.linalg.inv(C_ @ C_ + w * w * np.eye(len(C_))) @ B_.T
ws = np.concatenate([[0], np.logspace(-4, 4, 800)])
def sup_err(B_, C_, Br, Cr):
    return max(np.abs(np.linalg.eigvalsh((lambda Qh_: Qh_ @ (Qs(Br, Cr, w) - Qs(B_, C_, w)) @ Qh_)(np.linalg.inv(rsq(Qs(B_, C_, w)))))).max() for w in ws)
def trunc(B_, C_, Vr): Hu = B_ @ np.linalg.inv(rsq(C_)); Cr = Vr.T @ C_ @ Vr; return Hu @ Vr @ rsq(Cr), Cr
dev = 0; schur = 0; posdef = True
for _ in range(200):
    bb = rng.integers(1, 4); hh = rng.integers(2, 7); Cm = rng.normal(size=(hh, hh)); Cm = Cm @ Cm.T + rng.uniform(0.05, 2) * np.eye(hh)
    Bm = rng.normal(size=(bb, hh)) * 10 ** rng.uniform(-1, 0.7); Am = rng.normal(size=(bb, bb)); KBm = Am @ Am.T + 0.5 * np.eye(bb)
    ev, Vv = np.linalg.eigh(pi_overdamped(Cm, Bm)); o = np.argsort(ev)[::-1]; ev, Vv = ev[o], Vv[:, o]; r = rng.integers(1, hh)
    Br, Cr = trunc(Bm, Cm, Vv[:, :r]); Ar = KBm + Br @ np.linalg.solve(Cr, Br.T); Kr = np.block([[Ar, Br], [Br.T, Cr]])
    posdef &= np.linalg.eigvalsh(Kr).min() > 0; schur = max(schur, np.abs(Ar - Br @ np.linalg.solve(Cr, Br.T) - KBm).max())
    dev = max(dev, np.abs(np.sort(np.linalg.eigvalsh(pi_overdamped(Cr, Br)))[::-1] - ev[:r]).max())
check("R1 visibility truncation is hereditary and physical", dev < 1e-10 and posdef and schur < 1e-12,
      f"max retained-visibility deviation {dev:.1e}; K_r > 0 in all; Schur-complement deviation {schur:.1e}")
ratios = []; wins = 0; NT = 500
for _ in range(NT):
    bb = rng.integers(1, 4); hh = rng.integers(3, 7); Cm = rng.normal(size=(hh, hh)); Cm = Cm @ Cm.T + rng.uniform(0.05, 2) * np.eye(hh)
    Bm = rng.normal(size=(bb, hh)) * 10 ** rng.uniform(-1, 0.7)
    ev, Vv = np.linalg.eigh(pi_overdamped(Cm, Bm)); o = np.argsort(ev)[::-1]; ev, Vv = ev[o], Vv[:, o]; r = rng.integers(1, hh)
    e_v = sup_err(Bm, Cm, *trunc(Bm, Cm, Vv[:, :r])); bnd = np.prod(((1 + ev[r:]) / (1 - ev[r:])) ** 2) - 1; ratios.append(e_v / bnd)
    cw, cv = np.linalg.eigh(Cm); Hu = Bm @ np.linalg.inv(rsq(Cm)); wt = np.sum((Hu @ cv) ** 2, axis=0) / cw
    e_m = min(sup_err(Bm, Cm, *trunc(Bm, Cm, cv[:, np.argsort(-wt)[:r]])), sup_err(Bm, Cm, *trunc(Bm, Cm, cv[:, :r])))
    wins += e_v < e_m
check("R2 truncation error law (numerical)", max(ratios) <= 1.01 and np.median(ratios) >= 0.9 and wins / NT >= 0.9,
      f"{NT} truncations: max err/bound {max(ratios):.5f}, median {np.median(ratios):.4f}; visibility beats modal in {100*wins/NT:.1f}%")

# ---------------- R3 chain spectrum ----------------
spec = {}
for n in (10, 20, 30):
    a_ = 3.; Cn = np.diag([a_] * n) + np.diag([-1.] * (n - 1), 1) + np.diag([-1.] * (n - 1), -1); Bn = np.zeros((1, n)); Bn[0, 0] = -1.
    spec[n] = np.sort(np.linalg.eigvalsh(pi_overdamped(Cn, Bn)))[::-1][:7]
rat = spec[30][1:7] / spec[30][:6]
check("R3 pinned-chain visibility spectrum is geometric", np.max(np.abs(rat / rat.mean() - 1)) < 0.01 and np.max(np.abs(spec[20][:6] / spec[30][:6] - 1)) < 1e-3,
      f"n=30 top: {['%.4e' % x for x in spec[30][:6]]}; ratios {np.round(rat,5).tolist()}")

# ---------------- Q1 effective quantum oscillator ----------------
def eff(Tq):
    Kq = np.array([[2.5, -1.5], [-1.5, 2.5]]); w2, U_ = np.linalg.eigh(Kq); Om = np.sqrt(w2)
    X = (U_ @ np.diag(0.5 / Om / np.tanh(Om / (2 * Tq))) @ U_.T)[0, 0]; P = (U_ @ np.diag(0.5 * Om / np.tanh(Om / (2 * Tq))) @ U_.T)[0, 0]
    co = 2 * np.sqrt(X * P); weff = 2 * Tq * np.arctanh(1 / co); meff = np.sqrt(P / X) / weff; return X, P, co, weff, meff, meff * weff ** 2
X, P, co, weff, meff, keff = eff(1 / (2 * np.log(2))); _, _, _, _, m100, k100 = eff(100.)
check("Q1 effective quantum oscillator", co > 1 and keff < 1.6 and abs(m100 - 1) < 1e-3 and abs(k100 - 1.6) < 1e-3,
      f"X_B={X:.10f} (67/120), P_B={P:.10f} (59/60), coth={co:.10f}, w_eff={weff:.10f}, m_eff={meff:.10f}, k_eff={keff:.10f}; T=100: m_eff={m100:.6f}, k_eff={k100:.6f}")

npass = sum(r["pass"] for r in results)
print(f"RESULT {npass}/{len(results)} in {time.time()-t_start:.1f}s", flush=True)
json.dump({"criteria_written": "2026-10-09", "status": "author verification, not independent review",
           "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__, "mpmath": mp.__version__,
           "results": results, "passed": npass, "total": len(results)},
          open(__file__.replace("general_networks_cert.py", "general_networks_cert_results.json"), "w"), indent=1)
