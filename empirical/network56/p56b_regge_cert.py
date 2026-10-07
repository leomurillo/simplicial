"""
Paper 56, Section 4.4 — The 3+1 Regge hinge test.  Certificate.

numpy / sympy only (no torch on this machine).  Every claim is entropy-level (robust in float64: Paper 56, P5 and V2);
modular kernels are NOT used.  Integer counting is exact.  Deterministic (no randomness).

QUESTION.  In 3+1 dimensions Regge curvature lives on hinges (codimension 2).  Does a deficit hinge in a network of
ports change the entanglement of a ball by eta_b x (bond deficit), and does that bond deficit equal Jacobson's area
deficit, as the 2+1 disclination did (Paper 56, D1-D2)?

SETUP.  Prism networks: a triangulated cone of k triangular sectors (k = 6 flat, 5 deficit delta = pi/3, 7 deficit
-pi/3; the construction of p56_cert.py, cone_graph, verbatim) stacked in L_z = 41 layers along z.  In-plane links
weight 1; vertical links weight 3/2, so the long-wavelength light speed is isotropic (c^2 = 3/2 in-plane and vertical);
unit node inertia; massless; Dirichlet at the outer ring (R_max = 22) and at both z-ends.  The hinge is the vertical
line through the apex.  Intrinsic distance from the axis: rho^2 = r^2 - r j + j^2 for vertex j of ring r in its
sector (each sector is a flat 60-degree wedge).  Geodesic balls centred on the hinge at the middle layer z0:
A_R = {rho^2 + (z - z0)^2 <= R^2}, R = 3.0, 3.25, ..., 7.5.  Ground state from the exact product structure
K = K_cone (x) 1 + 1 (x) K_z: X = sum_j V diag(1/(2 sqrt(lam + mu_j))) V^T (x) s_j s_j^T, P likewise with sqrt/2.
Cut counts c_par (in-plane links) and c_perp (vertical links) leaving A.

THEORY (fixed before any run).  Cone x line, deficit delta: a geodesic ball of radius R has volume (1 - delta/2pi) V_0
and area (1 - delta/2pi) A_0, so at fixed volume  delta A|_V = 4 pi R^2 [(1 - delta/2pi)^{1/3} - 1] = -(2/3) delta R^2
+ O(delta^2).  Bisognano-Wichmann modular energy of a string of mass per length mu through the centre: (4 pi/3) mu R^2 / c.
Equilibrium eta (2/3) delta R^2 = (4 pi/3) mu R^2 gives delta = 2 pi mu / eta = 8 pi G mu with G = 1/(4 eta): the
general-relativistic cosmic-string deficit.  Both sides scale as R^2, so the balance is R-independent.

PRE-REGISTERED FALSIFIERS (written 2026-10-02, before the first run; every branch reportable)

V  [numerics, validation]
  Va  Product-structure X_A, P_A equal a dense diagonalization of the full prism Laplacian to 1e-11 (small cone
      R_max = 5, L_z = 7, k = 5, ball R = 2.5).
  Vb  Isotropy: in-plane and vertical long-wavelength c^2 are both 3/2 (exact, sympy).
  Vc  rho formula: for k = 6, rho^2 = r^2 - rj + j^2 equals the Euclidean distance^2 of the planar embedding (exact,
      all vertices of ring <= 6).
R  [numerics + exact counting]
  R1  Bond-count law on the flat prism (k = 6): S = eta_par c_par + eta_perp c_perp + s0 over R in [3, 7.5] fits with
      relative rms residual <= 1% (the bond-count law holds in 3+1).
  R2  Universality across the hinge: for k = 5 and k = 7, the residuals S_k - (eta_par c_par + eta_perp c_perp + s0)
      (k = 6 coefficients) have mean absolute value <= 25% of the mean |deficit signal| |S_k - S_6(n)| over R in [5, 7.5]
      (the entanglement per bond does not see the hinge).
  R3  Jacobson deficit in bond units: Q = (S_k - S_6(n)) / (eta_par dc_par + eta_perp dc_perp) in [0.8, 1.25] for every
      R in [5.5, 7.5], k = 5 and 7, where S_6(n), c_6(n) are least-squares fits of the k = 6 data in n^(2/3), n^(1/3), 1
      evaluated at the cone ball's node count n, and dc = c_k - c_6(n).
  R4  Geometry: the total bond deficit at fixed node count matches Jacobson's area deficit,
      (c_k - c_6(n))_total / (sigma_b (-(2/3) delta R^2)) in [0.7, 1.4] for R in [5.5, 7.5], sigma_b = c_6 / (4 pi R^2)
      (k = 6 bonds per unit area); delta = pi/3 (k = 5), -pi/3 (k = 7).
  R5  Headline (Jacobson in 3+1, combinatorial): (S_k - S_6(n)) / (eta (-(2/3) delta R^2)) in [0.7, 1.4] for R in
      [5.5, 7.5], k = 5 and 7, with eta = d S_6 / d(4 pi R^2) from the k = 6 fit S_6 = a R^2 + b R + c.
  Not tested (precision, Paper 56 P5): the string's modular energy; the reading mu = eta delta / (2 pi) stays [A].

L (global): any FAIL is retained in the RUN LOG below; post-diagnosis checks, if any, are labelled NOT BLIND.

RUN LOG
  Run 1 (2026-10-02, p56b_run1.log): 5/8.  Va (2e-15), Vb, Vc PASS.  R1 PASS (eta_par = 0.012828, eta_perp = 0.011425,
    s0 = 0.028, rms 0.94%).  R2 PASS (k = 5: mean|resid| 0.087 vs mean|deficit| 0.705; k = 7: 0.082 vs 0.781).
    R3, R4, R5 FAILED, retained: pointwise ratios mostly 0.90-1.04 (R3) and 0.73-0.98 (R5) but single digital balls give
    outliers (R3 1.64; R4 0.34-1.79; R5 0.52-1.29).  Diagnosis: the deficit (~5% of the cut count) is comparable to the
    digitization jitter of individual digital balls relative to the smooth k = 6 references; the pre-registration used
    POINTWISE ratios at finite size, against the program's own lesson (bands or fitted slopes).
  Post-diagnosis (NOT BLIND; criteria fixed here before computing; p56b_post.py, from the run-1 transcript):
    R3'  slope of dS on (eta_par dc_par + eta_perp dc_perp), through the origin, all R in [3, 7.5], k = 5 and 7 jointly:
         in [0.85, 1.15].
    R4'  slope of dc_total on sigma_b (-(2/3) delta R^2), same data: in [0.75, 1.3].
    R5'  HEADLINE slope of dS on eta (-(2/3) delta R^2), same data: in [0.75, 1.3]; per-k slopes and standard errors
         reported.
  Post run 1 (2026-10-02, p56b_post_run1.log, NOT BLIND): 3/3.  R3' slope 0.929 +- 0.022 (k=5 0.930, k=7 0.927);
    R4' slope 0.959 +- 0.057 (k=5 0.908, k=7 1.011); R5' slope 0.848 +- 0.033 (k=5 0.796 +- 0.038, k=7 0.899 +- 0.051).
    Reading: a 3+1 Regge hinge carries Jacobson's term at 85% of the continuum value at R <= 7.5; the shortfall
    factorizes as 0.93 (entropy per bond deficit; the 2+1 analogue rose 0.93 -> 0.999 with R) x 0.96 (digital geometry).
"""
import sys
import math
import time
import itertools

import numpy as np
import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

# (gauss_stuff, cone_graph, fit copied verbatim from empirical/network56/p56_cert.py)
def gauss_stuff(XA, PA):
    xe, V = np.linalg.eigh(XA)
    Xh = (V * np.sqrt(xe)) @ V.T
    Xmh = (V / np.sqrt(xe)) @ V.T
    C = Xh @ PA @ Xh; C = (C + C.T) / 2
    mu, Q = np.linalg.eigh(C)
    nu = np.maximum(np.sqrt(np.clip(mu, 0.25, None)), 0.5 + 1e-13)
    sp_ = np.log((nu + 0.5) / (nu - 0.5))
    S = float(np.sum((nu + 0.5) * np.log(nu + 0.5) - (nu - 0.5) * np.log(nu - 0.5)))
    B = Xh @ Q
    DP = (B * (sp_ / (2 * nu))) @ B.T
    Bm = Xmh @ Q
    DX = (Bm * (nu * sp_ / 2)) @ Bm.T
    return S, (DX + DX.T) / 2, (DP + DP.T) / 2

def entropy_only(XA, PA):
    # first lines of gauss_stuff (verbatim), returning S only (memory: the modular kernels are not needed here)
    xe, V = np.linalg.eigh(XA)
    Xh = (V * np.sqrt(xe)) @ V.T
    del V
    C = Xh @ PA @ Xh; C = (C + C.T) / 2
    del Xh
    mu = np.linalg.eigvalsh(C)
    nu = np.maximum(np.sqrt(np.clip(mu, 0.25, None)), 0.5 + 1e-13)
    S = float(np.sum((nu + 0.5) * np.log(nu + 0.5) - (nu - 0.5) * np.log(nu - 0.5)))
    return S

def cone_graph(k, Rmax):
    def vid(r, m):
        return 0 if r == 0 else 1 + k * (r - 1) * r // 2 + m
    N = 1 + k * Rmax * (Rmax + 1) // 2
    K = np.zeros((N, N)); ring = np.zeros(N, int)
    def add(a, b):
        K[a, a] += 1; K[b, b] += 1; K[a, b] -= 1; K[b, a] -= 1
    for m in range(k):
        add(0, vid(1, m))
    cut = {0: k}
    for r in range(1, Rmax + 1):
        nr = k * r
        for m in range(nr):
            ring[vid(r, m)] = r
            add(vid(r, m), vid(r, (m + 1) % nr))
        ups = 0
        for m in range(nr):
            s, j = divmod(m, r)
            tg = [s * (r + 1) + j, s * (r + 1) + j + 1] + ([s * (r + 1) - 1] if j == 0 else [])
            for tm in tg:
                ups += 1
                if r < Rmax:
                    add(vid(r, m), vid(r + 1, tm % (k * (r + 1))))
                else:
                    K[vid(r, m), vid(r, m)] += 1
        cut[r] = ups
    return K, ring, cut

def fit(xs, ys, powers):
    X = np.vstack([xs ** p for p in powers]).T
    coef, *_ = np.linalg.lstsq(X, ys, rcond=None)
    resid = ys - X @ coef
    dof = max(len(xs) - len(powers), 1)
    cov = np.linalg.inv(X.T @ X) * float(resid @ resid) / dof
    return coef, np.sqrt(np.diag(cov))


WZ = 1.5

def cone_rho2(k, Rmax):
    N = 1 + k * Rmax * (Rmax + 1) // 2
    rho2 = np.zeros(N)
    for r in range(1, Rmax + 1):
        base = 1 + k * (r - 1) * r // 2
        for m in range(k * r):
            s_, j = divmod(m, r)
            rho2[base + m] = r * r - r * j + j * j
    return rho2

def edges_from_K(K):
    iu = np.triu_indices(K.shape[0], 1)
    sel = K[iu] < 0
    return np.vstack([iu[0][sel], iu[1][sel]]).T

class Prism:
    def __init__(self, k, Rmax, Lz):
        K, ring, _ = cone_graph(k, Rmax)
        self.k, self.Rmax, self.Lz = k, Rmax, Lz
        self.edges = edges_from_K(K)
        self.rho2 = cone_rho2(k, Rmax)
        self.lam, self.V = np.linalg.eigh(K)
        del K
        jj = np.arange(1, Lz + 1)
        self.mu = WZ * (2 - 2 * np.cos(np.pi * jj / (Lz + 1)))
        self.sz = np.sqrt(2.0 / (Lz + 1)) * np.sin(np.pi * np.outer(jj, jj) / (Lz + 1))   # sz[j-1, z-1]
        self.z0 = (Lz + 1) // 2

    def footprint(self, Rmax_ball):
        return np.where(self.rho2 <= Rmax_ball ** 2 + 1e-9)[0]

    def blocks(self, foot):
        Vf = self.V[foot, :]
        FX = np.empty((self.Lz, len(foot), len(foot))); FP = np.empty_like(FX)
        for j in range(self.Lz):
            w = self.lam + self.mu[j]
            FX[j] = (Vf * (0.5 / np.sqrt(w))) @ Vf.T
            FP[j] = (Vf * (0.5 * np.sqrt(w))) @ Vf.T
        return FX, FP

    def ball(self, R, foot):
        sites = []
        for fi, a in enumerate(foot):
            for z in range(1, self.Lz + 1):
                if self.rho2[a] + (z - self.z0) ** 2 <= R * R + 1e-9:
                    sites.append((fi, a, z))
        return np.array(sites, dtype=int)

    def XP(self, sites, FX, FP):
        fi = sites[:, 0]; zi = sites[:, 2] - 1
        n = len(sites)
        X = np.zeros((n, n)); P = np.zeros((n, n))
        for j in range(self.Lz):
            sj = self.sz[j, zi]
            o = np.outer(sj, sj)
            X += FX[j][np.ix_(fi, fi)] * o
            P += FP[j][np.ix_(fi, fi)] * o
        return (X + X.T) / 2, (P + P.T) / 2

    def cuts(self, sites):
        inA = set((int(a), int(z)) for _, a, z in sites)
        cpar = 0
        for z in set(int(z) for _, _, z in sites):
            for a, b in self.edges:
                if ((int(a), z) in inA) != ((int(b), z) in inA):
                    cpar += 1
        cperp = 0
        for (a, z) in inA:
            for dz in (1, -1):
                z2 = z + dz
                if 1 <= z2 <= self.Lz and (a, z2) not in inA:
                    cperp += 1
        return cpar, cperp


# =========================================================================== V: validation
print("== V validation ==", flush=True)
pr = Prism(5, 5, 7)
foot = pr.footprint(2.5)
FX, FP = pr.blocks(foot)
sites = pr.ball(2.5, foot)
Xp, Pp = pr.XP(sites, FX, FP)
Kc, _, _ = cone_graph(5, 5)
N2 = Kc.shape[0]; Lz = 7
Tz = np.zeros((Lz, Lz))
for z in range(Lz):
    Tz[z, z] = 2 * WZ
    if z + 1 < Lz:
        Tz[z, z + 1] = Tz[z + 1, z] = -WZ
Kfull = np.kron(Kc, np.eye(Lz)) + np.kron(np.eye(N2), Tz)
lam_, U = np.linalg.eigh(Kfull)
Xf = (U * (0.5 / np.sqrt(lam_))) @ U.T; Pf = (U * (0.5 * np.sqrt(lam_))) @ U.T
idx = np.array([a * Lz + (z - 1) for _, a, z in sites])
eX = np.abs(Xf[np.ix_(idx, idx)] - Xp).max() / np.abs(Xp).max()
eP = np.abs(Pf[np.ix_(idx, idx)] - Pp).max() / np.abs(Pp).max()
check("Va [numerics] product-structure ground state = dense diagonalization of the full prism", max(eX, eP) < 1e-11,
      f"X {eX:.1e}, P {eP:.1e}, n_A={len(sites)}")
kx, ky, kz = sp.symbols('k_x k_y k_z', real=True)
e1 = sp.Matrix([1, 0]); e2 = sp.Matrix([sp.Rational(1, 2), sp.sqrt(3) / 2]); e3 = e2 - e1
kv = sp.Matrix([kx, ky])
w2_plane = sum(2 * (1 - sp.cos((kv.T * e)[0])) for e in (e1, e2, e3))
c2p = sp.simplify(sp.series(w2_plane.subs({kx: sp.Symbol('t') * kx, ky: sp.Symbol('t') * ky}), sp.Symbol('t'), 0, 3)
                  .removeO().coeff(sp.Symbol('t'), 2) - sp.Rational(3, 2) * (kx ** 2 + ky ** 2)) == 0
c2z = sp.simplify(sp.series(WZ * 2 * (1 - sp.cos(kz)), kz, 0, 3).removeO() - sp.Rational(3, 2) * kz ** 2) == 0
check("Vb [exact] isotropy: in-plane and vertical c^2 = 3/2", c2p and c2z, f"in-plane {c2p}, vertical {c2z}")
rho2 = cone_rho2(6, 6); ok = True
for r in range(1, 7):
    base = 1 + 6 * (r - 1) * r // 2
    for m in range(6 * r):
        s_, j = divmod(m, r)
        ang = s_ * math.pi / 3
        a1 = np.array([math.cos(ang), math.sin(ang)]); a2 = np.array([math.cos(ang + math.pi / 3), math.sin(ang + math.pi / 3)])
        p = (r - j) * a1 + j * a2
        ok &= abs(float(p @ p) - rho2[base + m]) < 1e-12
check("Vc [exact up to float embedding] rho^2 = r^2 - rj + j^2 is the Euclidean distance^2 for k = 6", ok)
del Kfull, U, Xf, Pf


# =========================================================================== R: the hinge test
print("== R hinge test ==", flush=True)
RMAX, LZ = 22, 41
Rs = np.arange(3.0, 7.5 + 1e-9, 0.25)
data = {}
t0 = time.time()
for k in (6, 5, 7):
    pr = Prism(k, RMAX, LZ)
    foot = pr.footprint(Rs[-1])
    FX, FP = pr.blocks(foot)
    rows = []
    for R in Rs:
        sites = pr.ball(R, foot)
        X, P = pr.XP(sites, FX, FP)
        S = entropy_only(X, P)
        del X, P
        cpar, cperp = pr.cuts(sites)
        rows.append(dict(R=R, n=len(sites), S=S, cpar=cpar, cperp=cperp))
        print(f"   k={k} R={R:.2f} n={len(sites):5d} S={S:.6f} c_par={cpar} c_perp={cperp} [{time.time() - t0:.0f}s]",
              flush=True)
    data[k] = rows
    del pr, FX, FP

def col(k, key):
    return np.array([q[key] for q in data[k]], dtype=float)

R6 = col(6, 'R'); S6 = col(6, 'S'); cp6 = col(6, 'cpar'); cq6 = col(6, 'cperp'); n6 = col(6, 'n')
A = np.vstack([cp6, cq6, np.ones_like(cp6)]).T
coef, *_ = np.linalg.lstsq(A, S6, rcond=None)
eta_par, eta_perp, s0 = coef
rms = float(np.sqrt(np.mean((A @ coef - S6) ** 2)) / np.mean(S6))
check("R1 [numerics] flat prism obeys the bond-count law S = eta_par c_par + eta_perp c_perp + s0 (rms <= 1%)",
      rms <= 0.01, f"eta_par={eta_par:.6f}, eta_perp={eta_perp:.6f}, s0={s0:.4f}, rel rms={rms:.4f}, "
      f"cond={np.linalg.cond(A):.1f}")
x13 = n6 ** (1 / 3)
fS, _ = fit(x13, S6, [2, 1, 0]); fp_, _ = fit(x13, cp6, [2, 1, 0]); fq_, _ = fit(x13, cq6, [2, 1, 0])
def ref(f, n):
    x = n ** (1 / 3)
    return f[0] * x ** 2 + f[1] * x + f[2]
aS, _ = fit(R6, S6, [2, 1, 0])
eta_c = aS[0] / (4 * math.pi)
sig_b = (cp6 + cq6) / (4 * math.pi * R6 ** 2)
sig_fit, _ = fit(R6, sig_b, [0])
r2txt, r3txt, r4txt, r5txt = [], [], [], []
r2ok = r3ok = r4ok = r5ok = True
for k, dl in ((5, math.pi / 3), (7, -math.pi / 3)):
    Rk = col(k, 'R'); Sk = col(k, 'S'); nk = col(k, 'n'); cpk = col(k, 'cpar'); cqk = col(k, 'cperp')
    dS = Sk - ref(fS, nk)
    dcp = cpk - ref(fp_, nk); dcq = cqk - ref(fq_, nk)
    resid = Sk - (eta_par * cpk + eta_perp * cqk + s0)
    sel2 = (Rk >= 5) & (Rk <= 7.5)
    m_res = float(np.mean(np.abs(resid[sel2]))); m_sig = float(np.mean(np.abs(dS[sel2])))
    r2ok &= m_res <= 0.25 * m_sig
    r2txt.append(f"k={k}: mean|resid|={m_res:.4f} vs mean|deficit|={m_sig:.4f}")
    sel = (Rk >= 5.5) & (Rk <= 7.5)
    Q = dS / (eta_par * dcp + eta_perp * dcq)
    geo = (dcp + dcq) / (sig_fit[0] * (-(2 / 3) * dl * Rk ** 2))
    J = dS / (eta_c * (-(2 / 3) * dl * Rk ** 2))
    r3ok &= bool(np.all((Q[sel] >= 0.8) & (Q[sel] <= 1.25)))
    r4ok &= bool(np.all((geo[sel] >= 0.7) & (geo[sel] <= 1.4)))
    r5ok &= bool(np.all((J[sel] >= 0.7) & (J[sel] <= 1.4)))
    r3txt.append(f"k={k}: {np.round(Q[sel], 3).tolist()}")
    r4txt.append(f"k={k}: {np.round(geo[sel], 3).tolist()}")
    r5txt.append(f"k={k}: {np.round(J[sel], 3).tolist()}")
    print(f"   k={k} deficit signal dS(R) = {np.round(dS, 4).tolist()}", flush=True)
check("R2 [numerics] entanglement per bond does not see the hinge (residuals <= 25% of the deficit signal)", r2ok,
      "; ".join(r2txt))
check("R3 [numerics] deficit in bond units: Q = dS / (eta dc) in [0.8, 1.25]", r3ok, "; ".join(r3txt))
check("R4 [exact counting + fit] bond deficit = sigma_b x Jacobson area deficit -(2/3) delta R^2, ratio in [0.7, 1.4]",
      r4ok, f"sigma_b={sig_fit[0]:.4f}; " + "; ".join(r4txt))
check("R5 [numerics] HEADLINE: dS|_n = eta x delta A|_V (3+1 Jacobson term from a Regge hinge), ratio in [0.7, 1.4]",
      r5ok, f"eta={eta_c:.6f}; " + "; ".join(r5txt))

print()
print(f"TOTAL: {sum(res)}/{len(res)} PASS")
