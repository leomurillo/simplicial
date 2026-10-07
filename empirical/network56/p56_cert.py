"""
Paper 56 — The Dynamic Network: Entanglement Equilibrium on Networks of Ports.  Certificate.

numpy / scipy.fft / sympy / mpmath only (no torch on this machine).  Exact (sympy / Fraction) arithmetic decides
every claim tagged [exact].  Claims tagged [numerics] use exact covariance formulas (no sampling) evaluated in
float64 through discrete sine transforms and a trapezoid rule in u = ln t (exponentially convergent); they carry
stated tolerances and are validated by an independent dense route (V-block).  Pseudo-random instances come from
one fixed deterministic stream (random.Random(560001)).  Usage: python p56_cert.py [E|V|J2|J3|D|all].

QUESTION.  Paper 55 (O1): let the network's own weights respond to what it stores.  Jacobson (2016): if the
entanglement of every small ball is stationary at fixed volume when geometry and state vary together (MVEH),
then G_ab = 8 pi G T_ab with 1/(4G) = eta, the entanglement per unit area.  On a network of ports, does
"weights = geometry" support this, and with the same G as the area law?  If not, what must the network do?

SETUP.  Static metric g = -N^2 dt^2 + Omega^2 dx^2 in d space dimensions, scalar with curvature coupling xi.
Network dictionary (discretized action): node inertia M_v = Omega^d / N, link weight w_e = N Omega^(d-2),
node mass mu_v = xi N Omega^d R.  Canonical variables y = M^(1/2) x: entanglement depends only on
Kt = M^(-1/2) (L_w + diag mu) M^(-1/2).  Weak field Omega = 1 - Psi (spatial curvature; N = 1), or N = Omega
(spacetime Weyl rescaling).  Lattice Laplacian Delta (Neumann mirror at walls).  Dirichlet cube, massless,
ground state.  Ball A = sites with |x - c| <= R; R_eff = (n_A / V_d)^(1/d).  Curvature profile:
Psi = r^2/2 (r <= R_c = R + 1.5), Psi = 3 R_c^2/2 - R_c^3/r outside (harmonic), so Delta Psi = d inside R_c.
Linear response: delta S_A = tr(delta Kt . W), W = (1/pi) int_0^oo G_t[:,A] (t^2 D_P - D_X) G_t[A,:] dt,
G_t = (L + t^2)^(-1), D_X = dS/dX_A, D_P = dS/dP_A (= half the modular-Hamiltonian kernels).

THEORY TARGETS (fixed before any run).
  Jacobson area deficit at fixed volume for uniform curvature Delta Psi = d:  3D  delta A|_V = -(8 pi/5) R^4;
  2D  delta C|_V = -(pi/2) R^3.  So MVEH-consistency predicts delta S_geom = -J_d eta R^(d+1) + lower,
  J_3 = 8 pi/5, J_2 = pi/2.  Bisognano-Wichmann matter weight sum_x beta(x) (c = 1): 3D (8 pi^2/15) R^4,
  2D (pi^2/2) R^3.  Equilibrium c_top R^(d+1) alpha + m_top R^(d+1) eps = 0 gives Delta Psi = d alpha:
  3D 4 pi G_net = -3 m_top / c_top;  2D 8 pi G_net = -2 m_top / c_top.  Heat-kernel induced gravity:
  1/G_ind proportional to (1/6 - xi).

PRE-REGISTERED FALSIFIERS (written 2026-10-01, before the first run; every branch reportable)

E [exact]
  E1  Classical Gaussian network (random rational K = L_w + diag m^2, 7 nodes, A = 3 nodes): the marginal on A is
      Gibbs for the Kron-reduced stiffness, (Sigma_AA)^(-1) = K_AA - K_AB K_BB^(-1) K_BA (modular Hamiltonian =
      beta x Kron reduction), and det Sigma_AA det Sigma_BB / det Sigma = det K_AA det K_BB / det K > 1
      (classical mutual information = (1/2) ln of a ratio of spanning-forest polynomials).
  E2  Random 6-node graph with symbolic weights: det of the reduced Laplacian = spanning-tree polynomial
      (Kirchhoff, enumerated); d ln det / d w_e = R_eff(e) (Hellmann-Feynman); sum_e w_e R_eff(e) = n - 1
      (Foster = equipartition); Hessian of ln det, H_ef = -(b_e^T L_red^(-1) b_f)^2, negative semidefinite
      (the induced free energy is concave: matter softens geometry).
  E3  Metric dictionary to first order (symbolic Psi, xi; 2D 4x4 and 3D 3x3x3 Dirichlet lattices):
      spatial (N = 1):  delta Kt = (Psi L + L Psi) + kappa_xi diag(Delta Psi),  kappa_xi = 2(d-1) xi - (d-2)/2;
      spacetime Weyl (N = Omega):  delta Kt = (2 d xi - (d-1)/2) diag(Delta Psi), which vanishes identically iff
      xi = (d-1)/(4d) (conformal coupling): the lattice is exactly Weyl invariant to first order there.
  E4  Vacuum stationarity: int_0^oo (t^2 - lam)/(lam + t^2)^2 dt = 0, hence for every first-order Hamiltonian
      perturbation of a Gaussian ground state <H_old> changes only at second order.
  E5  Second order of relative entropy is Fisher: D(N(0, S + e Dl) || N(0, S)) = (e^2/4) tr((S^-1 Dl)^2) + O(e^3)
      (random rational 3x3), and the e^1 term vanishes (first law).
V [numerics; validation gates for J]
  V1  Quadrature: X_A from (1/pi) int G_t dt equals the direct DST formula to relative 1e-8 (2D L=81, R=4; 3D L=33, R=3).
  V2  Linear response tr(delta Kt W) (DST + quadrature + D_X, D_P) equals a dense central finite difference of S_A
      under Kt + e delta Kt (independent eigh route) to relative 1e-5, for xi = 0 and for a pure mass term;
      2D L=14, R=3 and 3D L=8, R=2 (region = whole lattice).  The diag+nearest-neighbour profile formula
      2 sum (Psi - Psi_oo)(L W)_vv + kappa sum Delta Psi W_vv equals tr(delta Kt W) to 1e-10.
  V3  Uniform rescaling is invisible: |sum_v (L W)_vv| <= 1e-7 sum_v |(L W)_vv| on the whole small lattice.
  V5  Truncation gate (per dimension, largest R): relative change of y_s and of y_m between the two largest
      truncation radii <= 10%.  If V5 fails, the J-block of that dimension is reported INCONCLUSIVE.
J [numerics; the Jacobson test on fixed graphs, weights = geometry]  2D: L = 81, R = 4..16; 3D: L = 33,
  R = 3, 3.5, ..., 6.  y_s = response of S_A to the (Psi L + L Psi) part, y_m = response to diag(Delta Psi);
  delta S(xi) = y_s + kappa_xi y_m.  Fits: y = c_top R^(d+1) + c R^d + c' R^(d-1) (least squares in R_eff);
  eta from S = a R^(d-1) (+ lower: 3D a R^2 + b R + c; 2D a R + b, R >= 6): eta = a / Omega_(d-1).
  Minimal coupling xi = 0 (kappa_0 = -(d-2)/2):
  K_J   (Jacobson-consistent network gravity): (i) c_top(0) < 0; (ii) dominance |c_top| R_max^(d+1) >= 0.5 |y(R_max)|;
        (iii) r_J = -c_top / (J_d eta) in [0.5, 2.0].
  L_J0  no volume-order response: dominance fails.   L_J1  c_top > 0 with dominance (repulsive).
  L_J2  dominance and sign hold but r_J outside [0.5, 2.0] (induced G differs from the area-law G).
  K_xi  the zero xi_0 of c_top(xi) = c_s + kappa_xi c_m lies in [0.08, 0.30] (heat-kernel 1/6); L_xi otherwise.
M [numerics; matter side]  K_M: m_kin(R) / BW(R) in [0.6, 1.6] for the three largest R in each dimension, where
  m_kin = sum_{x in A} 2 D_P(x,x) (kinetic modular inverse temperature); also reported: m_pot = sum D_X(x,x)/d.
  If K_J and K_M both hold, G_net (formula above) is reported with 4 eta G_net.
D [numerics, dense; combinatorial curvature in 2+1]  Triangulated cones: k triangular sectors glued around an apex
  (k = 6 flat, 5 positive deficit pi/3, 7 negative), unit weights, Dirichlet ring at R_max = 26, ground state.
  Graph balls = rings 0..R.  cut(R) = number of links from ring R outward.
  D1  bond-count area law universal: fits S = eta_b cut + s_0 over R in [4, 12] give eta_b(5), eta_b(7) within 5% of
      eta_b(6).
  D2  Jacobson deficit at fixed node count: (S_k - S_6)|_n / (eta_b(6) (cut_k - cut_6)|_n) in [0.8, 1.25] for
      R in {8, ..., 12}, k = 5 and 7 (S_6, cut_6 interpolated to the cone's node count).
  D3  Bisognano-Wichmann at the apex of the flat lattice: 2 D_P(0,0) / (pi R_eff / c) in [0.6, 1.6] for R in [6, 12],
      c = sqrt(3/2), R_eff = (n sqrt(3)/(2 pi))^(1/2).
  D4  A point mass is a disclination: M_1(R) = -(S_5 - S_6)|_n / (2 D_P^(k=5)(0,0)) is positive, with
      max/min <= 1.3 over R in [6, 12] (R-independent), and the k = 7 analogue is negative.
  D5  Consistency with the area law: M_1 2 pi / (eta_len delta c) in [0.5, 2] (mean over R in [6, 12]), delta = pi/3,
      eta_len = dS_6/d(2 pi R_eff) from the flat fit.

L (global): any FAIL is retained in the RUN LOG below and reported in Paper 56; post-diagnosis checks, if any,
are labelled NOT BLIND.

RUN LOG
  Run 1 (2026-10-01): stage E 5/5 (p56_run1_E.log).  Stage V 4/6 (p56_run1_V.log): V1 (1e-9), V2 (xi=0: 6.0e-6 and
    2.2e-6; mass 3e-8) passed; V3 FAILED, retained: |sum (LW)_vv| / sum |(LW)_vv| = 5.0e-7 (2D), 1.0e-6 (3D) > 1e-7.
    Diagnosis (checker artifact, numerical method): D_X, D_P satisfy tr(D_X X_A) = tr(D_P P_A) algebraically, so
    exact invisibility can only be broken by the quadrature; the P-channel integrand decays only as e^{-u} at large
    t and the trapezoid sum stopped at u = 22 (similarly e^{+u} at small t).  Fix: exact geometric-sum end
    corrections from the asymptotic forms (upper: D_P e^{-u}/pi on A x A; lower: -(t/pi) G_0 D_X G_0), applied to
    W and to V1's X_A.  Criteria unchanged.  No J- or D-stage had been run.
  Run 2 (2026-10-01): V 6/6 (p56_run2_V.log; V1 2e-13, V3 2.5e-9 / 9.1e-10).
    J2 (p56_run2_J2.log) 1/4: V5 FAILED (y_s changes 25% between the two largest truncations; y_m 2%) => by the
      pre-registered rule the 2D J-block is INCONCLUSIVE; J2 printed branch L_J2 (r_J = 0.044) and J2xi PASS (0.256)
      are therefore not evidence.  M2 FAILED: m_kin/BW falls 1.03 -> 0.56 for R = 4 -> 16 at L = 81.
      PRE-REGISTRATION ERROR found after the run (retained): the "harmonic exterior" 3R_c^2/2 - R_c^3/r is harmonic
      only in 3D; in 2D it adds curvature Delta Psi = R_c^3/r^3 outside R_c (the 2D harmonic exterior is
      logarithmic).  The 2D J-block tested a different profile than the prose says.
    J3 (p56_run2_J3.log) 2/4: V5 FAILED at the margin (y_s 0.100 > 0.10; y_m 0.000) => formally INCONCLUSIVE.
      Printed branch L_J0: c_top(0) = -0.0090 +- 0.0056 (consistent with 0), dominance 0.469, r_J = 0.091; the mass
      channel is truncation-independent and area-like (y_m ~ -R^2).  J3xi PASS (xi_0 = 0.166, but c_m has a 70% error).
      M3 PASS (m_kin/BW 0.90-1.04).
    D (p56_run2_D.log) 3/5: D1 PASS (eta_b 0.03669 / 0.03654 / 0.03679), D2 PASS (0.93 -> 0.999), D3 FAILED (apex
      beta / BW 0.82 -> 0.48 for R = 6 -> 12 at R_max = 26), D4 FAILED (M_1 0.0151 -> 0.0280, follows from D3),
      D5 PASS (1.36).
  Post-diagnosis P-block (NOT BLIND; criteria fixed here before its first run):
    P1  2D J with the correct (logarithmic) harmonic exterior, full-lattice sums (no truncation), L = 161,
        R = 4..12; IR gate: y_s at R in {4, 8} changes <= 10% between L = 121 and L = 161.  Verdict with the
        pre-registered K_J / L_J criteria (eta refit on these balls, R >= 6).
    P2  3D J, full-lattice sums, L = 25, R in {3, 3.5, 4, 4.5, 5}; IR gate: y = y_s - y_m/2 at R in {3, 4} changes
        <= 10% between L = 21 and L = 25.  Verdict with K_J / L_J (eta from S = aR^2 + bR + c on these balls).
    P3  Box-size check of Bisognano-Wichmann (2D square): m_kin/BW at R in {8, 12} for L in {81, 161, 241};
        K: at L = 241 both ratios in [0.8, 1.25] and each ratio moves toward 1 as L grows.
    P4  Cones with sparse solvers (independent of the dense route): P4a at R_max = 26 reproduces the dense D-run
        S and 2 D_P(0,0) to relative 1e-8; P4b at R_max = 78: D3 ratios in [0.6, 1.6] for R in [6, 12] and closer
        to 1 than at R_max = 26; D4 at R_max = 78: M_1 > 0, max/min <= 1.3 over R in [6, 12], k = 7 negative;
        D2 at R_max = 78 within [0.8, 1.25].
  Run 3 (2026-10-01, p56_run3_P*.log, NOT BLIND): P3 FAILED: the 2D BW deficit is box-independent (m_kin/BW = 0.849 /
    0.848 / 0.848 at R = 8 and 0.685 / 0.683 / 0.683 at R = 12 for L = 81 / 161 / 241) => intrinsic, not IR.
    P1: gate FAILED narrowly (0.067, 0.102: the logarithmic 2D exterior reaches the box); verdict L_J0
      (c_top = -0.0036 +- 0.0012 vs Jacobson -0.130; r_J = 0.028; dominance 0.27; |y| ~ R^1.52).
    P2: gate PASS (0.026, 0.034); verdict L_J0 (c_top = -0.0078 +- 0.0026; r_J = 0.043 with this fit's eta = 0.036,
      0.079 with J3's eta = 0.0197; dominance 0.30; |y| ~ R^2.18); xi_0 = 0.164 +- 0.017; BW 0.94-1.04.
    P4: P4a FAILED (worst 0.36): CHECKER ARTIFACT -- P was computed as (1/pi) int (I - t^2 G_t) dt, whose large-t
      cancellation limits P to ~2e-8 relative (debug: X 5e-13, P 2.3e-8 on a 6-ring cone), and D_P amplifies this
      through nearly pure modes.  P4b, P4c from that run are void.  Fix: P = K X exactly (no cancellation).  P4 rerun
      as run 4 with unchanged criteria.
  Run 4 (2026-10-01, p56_run4_P4.log, NOT BLIND): P4a FAILED again (worst 3.1e-2), P4b FAILED (apex BW ratio 0.79 -> 0.46
    at R_max = 78, unchanged from 26), P4c FAILED (M_1 0.0153 -> 0.0286; D2 0.87-0.93 at R_max = 78).
    DIAGNOSIS (to be tested by P5): the modular kernels D_X, D_P are dominated by modes of large modular energy
    eps = ln((nu+1/2)/(nu-1/2)); Bisognano-Wichmann predicts eps up to ~beta(0) omega_max (~107 at R = 12 in 2D), but
    float64 resolves nu - 1/2 only to ~1e-13 (the clip), i.e. eps <~ 30.  The clip under-estimates the modular weight
    where beta omega > 30: the 2D apex saturates near 30/omega, the deficit grows with R, it is box-independent (P3), it
    is mild in 3D (the volume sum is less centre-weighted), and it makes the sparse and dense routes differ.  Entropy-
    level quantities (all J verdicts, D1, D2) are insensitive (V2 validated them).  If confirmed, M2, P3, D3, D4, P4
    are precision artifacts of the estimator, not physics.
  P5 (NOT BLIND; criteria fixed here): 2D square lattice L = 31, disk R = 6, reduced covariances computed exactly from
    the mode sum at 60 digits (mpmath) and in float64.  K: the 60-digit entanglement spectrum has modes with eps > 35;
    the 60-digit 2 D_P(c,c) exceeds the float64 value by >= 10%; and its ratio to pi R_eff is closer to 1 than the
    float64 ratio.  L: otherwise (the BW deficit would then not be a precision artifact).
  Run 5 (2026-10-01, p56_run5_P5.log, NOT BLIND): P5 PASS.  60-digit eps_max = 49.3 (24 modes above 30);
    2 D_P(c,c): float64 15.84 -> 60-digit 20.87 (+32%); BW pi R_eff = 18.84; ratio 0.84 -> 1.11.  S identical
    (3.0375353300 in both).  CONCLUSION: M2, P3, D3, D4 and P4 (a, b, c) are precision artifacts of the float64
    modular-kernel estimator (clip of the entanglement spectrum at eps ~ 30), NOT physics; the lattice 2+1 BW holds
    to ~11% at R = 6 once resolved.  Entropy-level results (all J verdicts, D1, D2) are unaffected.  The 2+1
    point-mass law of disclinations is UNTESTED at the required precision (needs X_A, P_A to ~e^{-eps_max}), not failed.
"""
import sys
import math
import time
import random
import itertools
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
import mpmath as mp
from scipy.fft import dstn
from scipy.interpolate import CubicSpline

sys.stdout.reconfigure(encoding="utf-8")
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)


# ---------- exact signature via charpoly + Descartes (valid: symmetric => all real eigenvalues) ----------
# (copied verbatim from empirical/p_infinity/probe_toy_lorentzian_intersection.py)
def signature(Mat):
    """Return (n_plus, n_zero, n_minus) exactly for a symmetric sympy integer/rational matrix."""
    n = Mat.shape[0]
    lam = sp.symbols('lam')
    p = Mat.charpoly(lam)                  # monic, exact integer/rational coeffs
    coeffs = p.all_coeffs()                # highest degree first, length n+1
    # multiplicity of zero root = number of trailing zero coeffs
    nz = 0
    while coeffs and coeffs[-1] == 0:
        nz += 1; coeffs = coeffs[:-1]
    # strip to the nonzero-root polynomial q(lam) of degree (n - nz); all its roots real & nonzero
    def sign_changes(seq):
        s = [c for c in seq if c != 0]
        return sum(1 for i in range(len(s)-1) if s[i]*s[i+1] < 0)
    n_plus = sign_changes(coeffs)                                   # Descartes on q(lam): # positive roots
    alt = [c*(-1)**i for i, c in enumerate(coeffs)]                 # q(-lam) coeffs (coeffs high->low)
    n_minus = sign_changes(alt)                                     # # negative roots
    assert n_plus + n_minus + nz == n, (n_plus, n_minus, nz, n)
    return n_plus, nz, n_minus


RNG = random.Random(560001)
# (rq, random_connected_graph, incidence copied verbatim from empirical/network55/p55_cert.py)
def rq(lo, hi, den=4):
    return sp.Rational(RNG.randint(int(lo * den), int(hi * den)), den)

def random_connected_graph(n, extra):
    edges = set()
    for v in range(1, n):
        u = RNG.randrange(v); edges.add((u, v))
    while len(edges) < n - 1 + extra:
        u, v = sorted(RNG.sample(range(n), 2)); edges.add((u, v))
    return sorted(edges)

def incidence(n, edges):
    d0 = sp.zeros(len(edges), n)
    for e, (i, j) in enumerate(edges):
        d0[e, i] = -1; d0[e, j] = 1
    return d0

STAGE = sys.argv[1] if len(sys.argv) > 1 else "all"
def run(tag):
    return STAGE == "all" or STAGE == tag


# =========================================================================== E: exact backbone
if run("E"):
    print("== E exact backbone ==", flush=True)
    # E1
    n = 7
    edges = random_connected_graph(n, 4)
    d0 = incidence(n, edges)
    K = d0.T * sp.diag(*[rq(1, 3) for _ in edges]) * d0 + sp.diag(*[rq(1, 2) for _ in range(n)])
    A_, B_ = [0, 1, 2], [3, 4, 5, 6]
    Sig = K.inv()
    kron = K.extract(A_, A_) - K.extract(A_, B_) * K.extract(B_, B_).inv() * K.extract(B_, A_)
    e1a = sp.simplify(Sig.extract(A_, A_).inv() - kron) == sp.zeros(3, 3)
    lhs = Sig.extract(A_, A_).det() * Sig.extract(B_, B_).det() / Sig.det()
    rhs = K.extract(A_, A_).det() * K.extract(B_, B_).det() / K.det()
    e1b = sp.simplify(lhs - rhs) == 0 and rhs > 1
    check("E1 [exact] classical modular Hamiltonian = beta x Kron reduction; MI = (1/2) ln(detK_AA detK_BB / detK)",
          e1a and e1b, f"Kron={e1a}, MI identity={e1b}, MI = {float(sp.log(rhs) / 2):.6f}")

    # E2
    n = 6
    edges = random_connected_graph(n, 4)
    ws = sp.symbols('w0:%d' % len(edges), positive=True)
    d0 = incidence(n, edges)
    Lw = d0.T * sp.diag(*ws) * d0
    detred = sp.expand(Lw[1:, 1:].det())
    trees = sp.Integer(0)
    for sub in itertools.combinations(range(len(edges)), n - 1):
        par = list(range(n))
        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]; a = par[a]
            return a
        ok = True
        for e in sub:
            a, b = find(edges[e][0]), find(edges[e][1])
            if a == b:
                ok = False; break
            par[a] = b
        if ok:
            trees += sp.prod([ws[e] for e in sub])
    mt = sp.expand(detred - trees) == 0
    vals = {w: rq(1, 3) for w in ws}
    Ln = Lw.subs(vals)
    Lplus = (Ln + sp.ones(n, n) / n).inv() - sp.ones(n, n) / n
    bvec = [d0.row(e).T for e in range(len(edges))]
    Reff = [(b.T * Lplus * b)[0] for b in bvec]
    hf = all(sp.simplify(sp.diff(sp.log(detred), ws[e]).subs(vals) - Reff[e]) == 0 for e in range(len(edges)))
    foster = sp.simplify(sum(vals[ws[e]] * Reff[e] for e in range(len(edges))) - (n - 1)) == 0
    Lri = Ln[1:, 1:].inv()
    br = [b[1:, 0] for b in bvec]
    Hm = sp.Matrix(len(edges), len(edges), lambda e, f: -((br[e].T * Lri * br[f])[0]) ** 2)
    Hchk = sp.simplify(sp.diff(sp.log(detred), ws[0], ws[1]).subs(vals) - Hm[0, 1]) == 0
    sigH = signature(Hm)
    check("E2 [exact] Kirchhoff matrix-tree; dlndet/dw_e = R_eff (Hellmann-Feynman); Foster sum w R_eff = n-1 "
          "(equipartition); Hessian = -(transfer current)^2 is NSD (matter softens geometry)",
          mt and hf and foster and Hchk and sigH[0] == 0,
          f"matrix-tree={mt}, HF={hf}, Foster={foster}, Hessian formula={Hchk}, signature={sigH}")

    # E3
    def first_order_Kt(d, Ls, mode):
        sites = list(itertools.product(range(1, Ls + 1), repeat=d))
        idx = {s: i for i, s in enumerate(sites)}
        nn_ = len(sites)
        eps, xi = sp.symbols('epsilon xi')
        Psi = sp.symbols('P0:%d' % nn_)
        Om = [1 - eps * Psi[i] for i in range(nn_)]
        Nl = [sp.Integer(1)] * nn_ if mode == 'spatial' else Om
        Kw = sp.zeros(nn_, nn_)
        DPsi = [sp.Integer(0)] * nn_
        for s in sites:
            i = idx[s]
            for ax in range(d):
                for sg in (1, -1):
                    t_ = list(s); t_[ax] += sg; t_ = tuple(t_)
                    if t_ in idx:
                        j = idx[t_]
                        DPsi[i] += Psi[j] - Psi[i]
                        if sg == 1:
                            Pe = (Psi[i] + Psi[j]) / 2
                            Ome = 1 - eps * Pe
                            Ne = sp.Integer(1) if mode == 'spatial' else Ome
                            w = Ne * Ome ** (d - 2)
                            Kw[i, i] += w; Kw[j, j] += w; Kw[i, j] -= w; Kw[j, i] -= w
                    else:
                        Ome = 1 - eps * Psi[i]
                        Ne = sp.Integer(1) if mode == 'spatial' else Ome
                        Kw[i, i] += Ne * Ome ** (d - 2)
        Rfac = 2 * (d - 1) if mode == 'spatial' else 2 * d
        M = [Om[i] ** d / Nl[i] for i in range(nn_)]
        first = sp.zeros(nn_, nn_)
        for i in range(nn_):
            for j in range(nn_):
                base = Kw[i, j]
                if i == j:
                    base = base + xi * Nl[i] * Om[i] ** d * Rfac * eps * DPsi[i]
                if base == 0:
                    continue
                expr = base / sp.sqrt(M[i] * M[j])
                first[i, j] = sp.expand(sp.diff(expr, eps).subs(eps, 0))
        L0 = Kw.subs(eps, 0)
        P = sp.diag(*Psi)
        if mode == 'spatial':
            kap = 2 * (d - 1) * xi - sp.Rational(d - 2, 2)
            pred = P * L0 + L0 * P + kap * sp.diag(*DPsi)
        else:
            pred = (2 * d * xi - sp.Rational(d - 1, 2)) * sp.diag(*DPsi)
        ok = sp.expand(first - pred) == sp.zeros(nn_, nn_)
        xic = sp.Rational(d - 1, 4 * d)
        weyl0 = (mode == 'weyl') and (sp.expand(first.subs(xi, xic)) == sp.zeros(nn_, nn_)) and \
            (sp.expand(first.subs(xi, 0)) != sp.zeros(nn_, nn_))
        return ok, weyl0
    e3 = []
    for d_, Ls in ((2, 4), (3, 3)):
        a1, _ = first_order_Kt(d_, Ls, 'spatial')
        a2, w0 = first_order_Kt(d_, Ls, 'weyl')
        e3.append((d_, a1, a2, w0))
    check("E3 [exact] metric dictionary: spatial dKt = (Psi L + L Psi) + kappa_xi DeltaPsi; spacetime Weyl dKt = "
          "(2d xi - (d-1)/2) DeltaPsi, vanishing iff xi = (d-1)/(4d) (exact first-order Weyl invariance)",
          all(a1 and a2 and w0 for _, a1, a2, w0 in e3), f"{e3}")

    # E4
    lam_, tt = sp.symbols('lambda t', positive=True)
    e4 = sp.simplify(sp.integrate((tt ** 2 - lam_) / (lam_ + tt ** 2) ** 2, (tt, 0, sp.oo))) == 0
    check("E4 [exact] vacuum stationarity: int_0^oo (t^2 - lam)/(lam+t^2)^2 dt = 0 (no first-order change of <H_old>)", e4)

    # E5
    ee = sp.symbols('e')
    Am = sp.Matrix(3, 3, lambda i, j: rq(-2, 2, 2))
    S0 = Am * Am.T + sp.eye(3)
    Dl = sp.Matrix(3, 3, lambda i, j: rq(-2, 2, 2)); Dl = Dl + Dl.T
    S1 = S0 + ee * Dl
    Dkl = (( S0.inv() * S1).trace() - 3 - sp.log((S0.inv() * S1).det())) / 2
    ser = sp.series(Dkl, ee, 0, 3).removeO()
    c1 = sp.simplify(ser.coeff(ee, 1)); c2 = sp.simplify(ser.coeff(ee, 2))
    fisher = sp.simplify(c2 - ((S0.inv() * Dl) ** 2).trace() / 4) == 0
    check("E5 [exact] relative entropy: first order vanishes (first law), second order = Fisher/4 >= 0",
          c1 == 0 and fisher and c2 > 0, f"e^1 coeff={c1}, e^2 coeff={c2}")


# =========================================================================== numerics machinery
class Lat:
    def __init__(self, d, L):
        self.d, self.L, self.N = d, L, L ** d
        k = np.arange(1, L + 1)
        lam1 = 2.0 - 2.0 * np.cos(np.pi * k / (L + 1))
        lam = np.zeros((L,) * d)
        for ax in range(d):
            sh = [1] * d; sh[ax] = L
            lam = lam + lam1.reshape(sh)
        self.lam = lam
        self.S1 = np.sqrt(2.0 / (L + 1)) * np.sin(np.pi * np.outer(k, k) / (L + 1))
        self.c = (L + 1) // 2

    def flat(self, coords):
        return np.ravel_multi_index(tuple((np.asarray(coords) - 1).T), (self.L,) * self.d)

    def Ue(self, coords):
        coords = np.asarray(coords); n_ = len(coords)
        out = np.ones((n_,) + (self.L,) * self.d)
        for ax in range(self.d):
            v = self.S1[coords[:, ax] - 1, :]
            sh = [n_] + [1] * self.d; sh[ax + 1] = self.L
            out = out * v.reshape(sh)
        return out

    def block(self, cols, f, rows_flat, bs=48):
        cols = np.asarray(cols)
        out = np.empty((len(rows_flat), len(cols)))
        axes = tuple(range(1, self.d + 1))
        for s0 in range(0, len(cols), bs):
            ue = self.Ue(cols[s0:s0 + bs])
            ue *= f
            z = dstn(ue, type=1, norm='ortho', axes=axes, workers=-1)
            out[:, s0:s0 + bs] = z.reshape(len(ue), -1)[:, rows_flat].T
        return out

    def ball(self, R):
        rng = np.arange(1, self.L + 1)
        grid = np.array(list(itertools.product(rng, repeat=self.d)))
        r2 = ((grid - self.c) ** 2).sum(1)
        sel = grid[r2 <= R * R + 1e-9]
        r2s = ((sel - self.c) ** 2).sum(1)
        order = np.lexsort(tuple(sel[:, ax] for ax in reversed(range(self.d))) + (r2s,))
        return sel[order]

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

def quad_nodes(lat, h=0.35, umax=22.0):
    umin = 0.5 * math.log(lat.lam.min()) - 18.0
    return np.arange(umin, umax + 1e-12, h), h

def tail_factor(h):
    # sum_{k>=1} e^{-k h} = e^{-h} / (1 - e^{-h})  (geometric continuation of the trapezoid sum beyond an end node)
    return math.exp(-h) / (1.0 - math.exp(-h))

def W_entries(lat, Ac, Rgc, DX, DP, pairs):
    us, h = quad_nodes(lat)
    Rg_flat = lat.flat(Rgc)
    nA = len(Ac)
    wd = np.zeros(len(Rgc)); wp = np.zeros(len(pairs))
    for u in us:
        t = math.exp(u)
        Ga = lat.block(Ac, 1.0 / (lat.lam + t * t), Rg_flat)
        H = Ga @ (t * t * DP - DX)
        wq = h * t / math.pi
        wd += wq * np.einsum('ij,ij->i', H, Ga)
        for c0 in range(0, len(pairs), 4000):
            pc = pairs[c0:c0 + 4000]
            wp[c0:c0 + 4000] += wq * np.einsum('ij,ij->i', H[pc[:, 0]], Ga[pc[:, 1]])
    # end corrections (added after run 1, V3 checker artifact): small t, f ~ -(t/pi) G0 DX G0;
    # large t, f ~ (1/pi) DP e^{-u} on A x A.
    G0 = lat.block(Ac, 1.0 / lat.lam, Rg_flat)
    H0 = G0 @ (-DX)
    lo = (h / math.pi) * math.exp(us[0]) * tail_factor(h)
    wd += lo * np.einsum('ij,ij->i', H0, G0)
    for c0 in range(0, len(pairs), 4000):
        pc = pairs[c0:c0 + 4000]
        wp[c0:c0 + 4000] += lo * np.einsum('ij,ij->i', H0[pc[:, 0]], G0[pc[:, 1]])
    hi = (h / math.pi) * math.exp(-us[-1]) * tail_factor(h)
    wd[:nA] += hi * np.diag(DP)
    if len(pairs):
        inA = (pairs[:, 0] < nA) & (pairs[:, 1] < nA)
        wp[inA] += hi * DP[pairs[inA, 0], pairs[inA, 1]]
    return wd, wp

def W_full(lat, Ac, DX, DP):
    us, h = quad_nodes(lat)
    allc = np.array(list(itertools.product(range(1, lat.L + 1), repeat=lat.d)))
    fl = lat.flat(allc)
    W = np.zeros((lat.N, lat.N))
    for u in us:
        t = math.exp(u)
        Ga = np.zeros((lat.N, len(Ac)))
        Ga[fl, :] = lat.block(Ac, 1.0 / (lat.lam + t * t), fl)
        W += (h * t / math.pi) * (Ga @ (t * t * DP - DX) @ Ga.T)
    G0 = np.zeros((lat.N, len(Ac))); G0[fl, :] = lat.block(Ac, 1.0 / lat.lam, fl)
    W += (h / math.pi) * math.exp(us[0]) * tail_factor(h) * (G0 @ (-DX) @ G0.T)
    Af = lat.flat(Ac)
    W[np.ix_(Af, Af)] += (h / math.pi) * math.exp(-us[-1]) * tail_factor(h) * DP
    return W

def profile(coords, c, R):
    Rc = R + 1.5
    r = np.sqrt(((np.asarray(coords) - c) ** 2).sum(1))
    psi = np.where(r <= Rc, 0.5 * r ** 2, 1.5 * Rc ** 2 - Rc ** 3 / np.maximum(r, 1e-12))
    return psi - 1.5 * Rc ** 2

def lattice_DeltaPsi(lat, coords, R):
    coords = np.asarray(coords)
    base = profile(coords, lat.c, R)
    out = np.zeros(len(coords))
    for ax in range(lat.d):
        for sg in (1, -1):
            nb = coords.copy(); nb[:, ax] += sg
            inside = (nb[:, ax] >= 1) & (nb[:, ax] <= lat.L)
            pv = profile(nb, lat.c, R)
            out += np.where(inside, pv - base, 0.0)
    return out

def neighbour_structure(lat, Rgc):
    pos = {tuple(x): i for i, x in enumerate(Rgc)}
    pairs = []
    complete = np.ones(len(Rgc), bool)
    for i, x in enumerate(Rgc):
        for ax in range(lat.d):
            for sg in (1, -1):
                y = x.copy(); y[ax] += sg
                if y[ax] < 1 or y[ax] > lat.L:
                    continue
                j = pos.get(tuple(y))
                if j is None:
                    complete[i] = False
                elif sg == 1:
                    pairs.append((i, j))
    return np.array(pairs, dtype=int).reshape(-1, 2), complete

def LW_diag(lat, wd, wp, pairs):
    LW = 2 * lat.d * wd.copy()
    np.subtract.at(LW, pairs[:, 0], wp)
    np.subtract.at(LW, pairs[:, 1], wp)
    return LW

def kappa(d, xi):
    return 2 * (d - 1) * xi - (d - 2) / 2

def dense_S(Kt, Aflat):
    lam_, V = np.linalg.eigh(Kt)
    X = (V * (0.5 / np.sqrt(lam_))) @ V.T
    P = (V * (0.5 * np.sqrt(lam_))) @ V.T
    S, _, _ = gauss_stuff(X[np.ix_(Aflat, Aflat)], P[np.ix_(Aflat, Aflat)])
    return S

def dense_L(lat):
    allc = np.array(list(itertools.product(range(1, lat.L + 1), repeat=lat.d)))
    fl = lat.flat(allc)
    Lm = np.zeros((lat.N, lat.N))
    Lm[fl, fl] = 2 * lat.d
    for ax in range(lat.d):
        nb = allc.copy(); nb[:, ax] += 1
        ok = nb[:, ax] <= lat.L
        a = fl[ok]; b = lat.flat(nb[ok])
        Lm[a, b] = -1; Lm[b, a] = -1
    return Lm, allc, fl


# =========================================================================== V: validation gates
if run("V"):
    print("== V validation ==", flush=True)
    for (d, L, R) in ((2, 81, 4), (3, 33, 3)):
        lat = Lat(d, L)
        Ac = lat.ball(R); Af = lat.flat(Ac)
        XA = lat.block(Ac, 0.5 / np.sqrt(lat.lam), Af)
        us, h = quad_nodes(lat)
        Xq = np.zeros_like(XA)
        for u in us:
            t = math.exp(u)
            Xq += (h * t / math.pi) * lat.block(Ac, 1.0 / (lat.lam + t * t), Af)
        Xq += (h / math.pi) * math.exp(us[0]) * tail_factor(h) * lat.block(Ac, 1.0 / lat.lam, Af)
        Xq += (h / math.pi) * math.exp(-us[-1]) * tail_factor(h) * np.eye(len(Ac))
        rel = np.abs(Xq - XA).max() / np.abs(XA).max()
        check(f"V1 [numerics] quadrature reproduces X_A ({d}D, L={L}, R={R})", rel < 1e-8, f"max rel err {rel:.2e}")
    for (d, L, R) in ((2, 14, 3), (3, 8, 2)):
        lat = Lat(d, L)
        Ac = lat.ball(R); Af = lat.flat(Ac)
        XA = lat.block(Ac, 0.5 / np.sqrt(lat.lam), Af); PA = lat.block(Ac, 0.5 * np.sqrt(lat.lam), Af)
        S0, DX, DP = gauss_stuff((XA + XA.T) / 2, (PA + PA.T) / 2)
        W = W_full(lat, Ac, DX, DP)
        Lm, allc, fl = dense_L(lat)
        S_dense0 = dense_S(Lm, Af)
        psi = np.zeros(lat.N); psi[fl] = profile(allc, lat.c, R)
        dps = np.zeros(lat.N); dps[fl] = lattice_DeltaPsi(lat, allc, R)
        ok_all = True; dets = []
        for label, dK in (("xi=0", np.diag(psi) @ Lm + Lm @ np.diag(psi) + kappa(d, 0.0) * np.diag(dps)),
                          ("mass", np.diag(dps))):
            lin = float(np.sum(dK * W))
            e = 1e-5 / max(1.0, np.abs(dK).max())
            fd = (dense_S(Lm + e * dK, Af) - dense_S(Lm - e * dK, Af)) / (2 * e)
            relr = abs(lin - fd) / max(abs(fd), 1e-300)
            ok_all &= relr < 1e-5
            dets.append(f"{label}: lin={lin:.8e} fd={fd:.8e} rel={relr:.1e}")
        pairs, complete = neighbour_structure(lat, allc)
        wd = np.array([W[f, f] for f in fl]); wp = np.array([W[fl[a], fl[b]] for a, b in pairs])
        LW = LW_diag(lat, wd, wp, pairs)
        prof = 2 * np.sum(profile(allc, lat.c, R) * LW) + kappa(d, 0.0) * np.sum(lattice_DeltaPsi(lat, allc, R) * wd)
        dK0 = np.diag(psi) @ Lm + Lm @ np.diag(psi) + kappa(d, 0.0) * np.diag(dps)
        tr0 = float(np.sum(dK0 * W))
        relp = abs(prof - tr0) / abs(tr0)
        check(f"V2 [numerics] linear response = dense finite difference; profile formula = trace ({d}D, L={L}, R={R})",
              ok_all and relp < 1e-10 and abs(S0 - S_dense0) < 1e-9,
              "; ".join(dets) + f"; profile vs trace rel={relp:.1e}; S route diff={abs(S0 - S_dense0):.1e}")
        v3 = abs(LW.sum()) / np.abs(LW).sum()
        check(f"V3 [numerics] uniform rescaling invisible ({d}D): |sum (LW)_vv| / sum |(LW)_vv|", v3 < 1e-7, f"{v3:.2e}")


# =========================================================================== J: the Jacobson test
def jacobson_block(d, L, Rs, regfac, regoff):
    lat = Lat(d, L)
    rows = []
    t0 = time.time()
    for R in Rs:
        Ac = lat.ball(R); nA = len(Ac); Af = lat.flat(Ac)
        Reff = (nA / (math.pi if d == 2 else 4 * math.pi / 3)) ** (1 / d)
        XA = lat.block(Ac, 0.5 / np.sqrt(lat.lam), Af); PA = lat.block(Ac, 0.5 * np.sqrt(lat.lam), Af)
        S, DX, DP = gauss_stuff((XA + XA.T) / 2, (PA + PA.T) / 2)
        rreg = min(regfac * R + regoff, lat.c - 2)
        big = lat.ball(rreg)
        inA = set(map(tuple, Ac))
        shell = np.array([x for x in big if tuple(x) not in inA])
        Rgc = np.vstack([Ac, shell])
        pairs, complete = neighbour_structure(lat, Rgc)
        wd, wp = W_entries(lat, Ac, Rgc, DX, DP, pairs)
        LW = LW_diag(lat, wd, wp, pairs)
        r = np.sqrt(((Rgc - lat.c) ** 2).sum(1))
        dev = profile(Rgc, lat.c, R)
        dps = lattice_DeltaPsi(lat, Rgc, R)
        Rc = R + 1.5
        trs = [Rc + 1.5, 0.5 * (Rc + 1.5 + rreg - 1), rreg - 1]
        ys, ym = [], []
        for rt in trs:
            sel = complete & (r <= rt + 1e-9)
            ys.append(2 * float(np.sum(dev[sel] * LW[sel])))
            selm = r <= rt + 1e-9
            ym.append(float(np.sum(dps[selm] * wd[selm])))
        mkin = float(np.sum(2 * np.diag(DP)))
        mpot = float(np.sum(np.diag(DX)) / d)
        rows.append(dict(R=R, nA=nA, Reff=Reff, S=S, ys=ys, ym=ym, mkin=mkin, mpot=mpot, rreg=rreg))
        print(f"   {d}D R={R:5.2f} nA={nA:5d} Reff={Reff:6.3f} S={S:10.5f} y_s={ys[-1]: .6e} y_m={ym[-1]: .6e} "
              f"(trunc ys {[f'{v:.4e}' for v in ys]}, ym {[f'{v:.4e}' for v in ym]}) m_kin={mkin:.5e} m_pot={mpot:.5e} "
              f"[{time.time() - t0:.0f}s]", flush=True)
    return rows

def fit(xs, ys, powers):
    X = np.vstack([xs ** p for p in powers]).T
    coef, *_ = np.linalg.lstsq(X, ys, rcond=None)
    resid = ys - X @ coef
    dof = max(len(xs) - len(powers), 1)
    cov = np.linalg.inv(X.T @ X) * float(resid @ resid) / dof
    return coef, np.sqrt(np.diag(cov))

def analyse_J(d, rows):
    Re = np.array([q['Reff'] for q in rows]); S = np.array([q['S'] for q in rows])
    ys = np.array([q['ys'][-1] for q in rows]); ym = np.array([q['ym'][-1] for q in rows])
    J = 8 * math.pi / 5 if d == 3 else math.pi / 2
    Om = 4 * math.pi if d == 3 else 2 * math.pi
    BW = (8 * math.pi ** 2 / 15) * Re ** 4 if d == 3 else (math.pi ** 2 / 2) * Re ** 3
    v5s = abs(rows[-1]['ys'][-1] - rows[-1]['ys'][-2]) / abs(rows[-1]['ys'][-1])
    v5m = abs(rows[-1]['ym'][-1] - rows[-1]['ym'][-2]) / abs(rows[-1]['ym'][-1])
    check(f"V5 [numerics] {d}D truncation gate (largest R): relative change of y_s, y_m <= 10%",
          v5s <= 0.1 and v5m <= 0.1, f"y_s {v5s:.3f}, y_m {v5m:.3f}")
    if d == 3:
        ce, _ = fit(Re, S, [2, 1, 0]); eta = ce[0] / Om
    else:
        sel = Re >= 6
        ce, _ = fit(Re[sel], S[sel], [1, 0]); eta = ce[0] / Om
    pw = [d + 1, d, d - 1]
    cs, es = fit(Re, ys, pw); cm, em = fit(Re, ym, pw)
    k0 = kappa(d, 0.0)
    y0 = ys + k0 * ym
    c0, e0 = fit(Re, y0, pw)
    ctop = c0[0]
    dom = abs(ctop) * Re[-1] ** (d + 1) / abs(y0[-1])
    rJ = -ctop / (J * eta)
    xi0 = ((d - 2) / 2 - cs[0] / cm[0]) / (2 * (d - 1)) if cm[0] != 0 else float('nan')
    mk, _ = fit(Re, np.array([q['mkin'] for q in rows]), pw)
    ratios = np.array([q['mkin'] for q in rows]) / BW
    ratios_p = np.array([q['mpot'] for q in rows]) / BW
    print(f"   {d}D eta={eta:.6f}  fit S coeffs={ce}")
    print(f"   {d}D y_s top={cs[0]:.5e}+-{es[0]:.1e}  y_m top={cm[0]:.5e}+-{em[0]:.1e}  "
          f"xi=0: c_top={ctop:.5e}+-{e0[0]:.1e} (full {c0}), dominance={dom:.3f}, r_J={rJ:.4f}, xi_0={xi0:.4f}")
    print(f"   {d}D matter m_kin/BW per R={np.round(ratios, 4).tolist()}  m_pot/BW={np.round(ratios_p, 4).tolist()}  "
          f"m_top={mk[0]:.5e} (BW {8 * math.pi ** 2 / 15 if d == 3 else math.pi ** 2 / 2:.5e})")
    kj = ctop < 0 and dom >= 0.5 and 0.5 <= rJ <= 2.0
    branch = ("K_J" if kj else ("L_J0 (no volume-order response)" if dom < 0.5 else
              ("L_J1 (repulsive)" if ctop > 0 else "L_J2 (induced G != area-law G)")))
    check(f"J{d} [numerics] Jacobson test, minimal coupling: c_top<0, dominance>=0.5, r_J in [0.5,2]", kj,
          f"branch {branch}: c_top={ctop:.4e}, dominance={dom:.3f}, r_J={rJ:.3f}, eta={eta:.5f}")
    check(f"J{d}xi [numerics] zero of c_top(xi) in [0.08, 0.30] (heat-kernel 1/6)", 0.08 <= xi0 <= 0.30,
          f"xi_0={xi0:.4f}")
    km = all(0.6 <= q <= 1.6 for q in ratios[-3:])
    check(f"M{d} [numerics] kinetic modular weight / Bisognano-Wichmann in [0.6,1.6] (three largest R)", km,
          f"{np.round(ratios[-3:], 4).tolist()}")
    if kj and km:
        Gnet = (-3 * mk[0] / (4 * math.pi * ctop)) if d == 3 else (-mk[0] / (4 * math.pi * ctop))
        print(f"   {d}D G_net={Gnet:.5e}, 4 eta G_net={4 * eta * Gnet:.4f}")
    return dict(eta=eta, cs=cs, cm=cm, c0=c0, dom=dom, rJ=rJ, xi0=xi0, ratios=ratios)

if run("J2"):
    print("== J2 Jacobson test, 2+1 ==", flush=True)
    rows2 = jacobson_block(2, 81, list(range(4, 17)), 2.0, 3.0)
    analyse_J(2, rows2)
if run("J3"):
    print("== J3 Jacobson test, 3+1 ==", flush=True)
    rows3 = jacobson_block(3, 33, [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0], 1.5, 3.0)
    analyse_J(3, rows3)


# =========================================================================== D: disclinations in 2+1
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

if run("D"):
    print("== D disclinations ==", flush=True)
    Rmax = 26
    Rs = list(range(1, 14))
    data = {}
    for k in (6, 5, 7):
        K, ring, cut = cone_graph(k, Rmax)
        deg = np.diag(K).copy()
        degok = deg[0] == k and np.all(deg[1:] == 6)
        lam_, V = np.linalg.eigh(K); del K
        X = (V * (0.5 / np.sqrt(lam_))) @ V.T
        P = (V * (0.5 * np.sqrt(lam_))) @ V.T
        del V
        rowsk = []
        for R in Rs:
            Af = np.where(ring <= R)[0]
            S, DX, DP = gauss_stuff(X[np.ix_(Af, Af)], P[np.ix_(Af, Af)])
            rowsk.append(dict(R=R, n=len(Af), S=S, cut=cut[R], b0=2 * DP[0, 0]))
        del X, P
        data[k] = rowsk
        print(f"   k={k}: degrees ok={degok}; " + "; ".join(f"R={q['R']} n={q['n']} S={q['S']:.5f} cut={q['cut']} "
                                                            f"beta0={q['b0']:.4f}" for q in rowsk), flush=True)
    def arr(k, key):
        return np.array([q[key] for q in data[k]], dtype=float)
    selR = (np.array(Rs) >= 4) & (np.array(Rs) <= 12)
    etab = {}
    for k in (6, 5, 7):
        cf, _ = fit(arr(k, 'cut')[selR], arr(k, 'S')[selR], [1, 0]); etab[k] = cf[0]
    d1 = abs(etab[5] / etab[6] - 1) <= 0.05 and abs(etab[7] / etab[6] - 1) <= 0.05
    check("D1 [numerics] bond-count area law universal across k = 5, 6, 7", d1,
          f"eta_b: {', '.join(f'k={k}: {etab[k]:.6f}' for k in (6, 5, 7))}")
    Rf = np.array(Rs, dtype=float)
    spl = CubicSpline(Rf, arr(6, 'S'))
    def flat_at(nv):
        Rx = (-1 + math.sqrt(1 + 4 * (nv - 1) / 3)) / 2
        return float(spl(Rx)), 6 * (2 * Rx + 1)
    d2ok = True; d2txt = []
    dS = {}
    for k in (5, 7):
        dS[k] = []
        for q in data[k]:
            S6, c6 = flat_at(q['n'])
            dS[k].append(q['S'] - S6)
            if 8 <= q['R'] <= 12:
                rat = (q['S'] - S6) / (etab[6] * (q['cut'] - c6))
                d2ok &= 0.8 <= rat <= 1.25
                d2txt.append(f"k={k} R={q['R']}: {rat:.4f}")
    check("D2 [numerics] Jacobson deficit at fixed node count = eta_b x cut deficit", d2ok, "; ".join(d2txt))
    cl = math.sqrt(1.5)
    Reff6 = np.sqrt(arr(6, 'n') * math.sqrt(3) / (2 * math.pi))
    d3 = arr(6, 'b0') / (math.pi * Reff6 / cl)
    sel3 = (np.array(Rs) >= 6) & (np.array(Rs) <= 12)
    check("D3 [numerics] Bisognano-Wichmann at the apex (flat): 2 D_P(0,0) / (pi R_eff / c) in [0.6,1.6]",
          bool(np.all((d3[sel3] >= 0.6) & (d3[sel3] <= 1.6))), f"{np.round(d3[sel3], 4).tolist()}")
    M1 = -np.array(dS[5]) / arr(5, 'b0'); M7 = -np.array(dS[7]) / arr(7, 'b0')
    m1s = M1[sel3]
    d4 = bool(np.all(m1s > 0) and m1s.max() / m1s.min() <= 1.3 and np.all(M7[sel3] < 0))
    check("D4 [numerics] point mass = disclination: M_1(R) > 0, R-independent (max/min <= 1.3); k=7 negative", d4,
          f"M_1={np.round(m1s, 6).tolist()}, M_(k=7)={np.round(M7[sel3], 6).tolist()}")
    cf, _ = fit(Reff6[selR], arr(6, 'S')[selR], [1, 0])
    eta_len = cf[0] / (2 * math.pi)
    d5r = float(np.mean(m1s)) * 2 * math.pi / (eta_len * (math.pi / 3) * cl)
    check("D5 [numerics] M_1 consistent with the area law: M_1 2pi/(eta_len delta c) in [0.5, 2]", 0.5 <= d5r <= 2.0,
          f"ratio={d5r:.4f}, eta_len={eta_len:.6f}, mean M_1={float(np.mean(m1s)):.6f}")


# =========================================================================== P: post-diagnosis (NOT BLIND)
def run_p(tag):
    return STAGE == tag or STAGE == "P"

def profile_h(coords, c, R, d):
    Rc = R + 1.5
    r = np.sqrt(((np.asarray(coords) - c) ** 2).sum(1))
    rr = np.maximum(r, 1e-12)
    if d == 3:
        ext, ref = 1.5 * Rc ** 2 - Rc ** 3 / rr, 1.5 * Rc ** 2
    else:
        ext, ref = 0.5 * Rc ** 2 + Rc ** 2 * np.log(rr / Rc), 0.5 * Rc ** 2
    return np.where(r <= Rc, 0.5 * r ** 2, ext) - ref

def lattice_DeltaPsi_h(lat, coords, R):
    coords = np.asarray(coords)
    base = profile_h(coords, lat.c, R, lat.d)
    out = np.zeros(len(coords))
    for ax in range(lat.d):
        for sg in (1, -1):
            nb = coords.copy(); nb[:, ax] += sg
            inside = (nb[:, ax] >= 1) & (nb[:, ax] <= lat.L)
            out += np.where(inside, profile_h(nb, lat.c, R, lat.d) - base, 0.0)
    return out

def full_responses(d, L, R):
    lat = Lat(d, L)
    allc = np.array(list(itertools.product(range(1, L + 1), repeat=d)))
    Ac = lat.ball(R); Af = lat.flat(Ac); nA = len(Ac)
    inA = np.zeros(lat.N, bool); inA[Af] = True
    Rgc = np.vstack([Ac, allc[~inA[lat.flat(allc)]]])
    XA = lat.block(Ac, 0.5 / np.sqrt(lat.lam), Af); PA = lat.block(Ac, 0.5 * np.sqrt(lat.lam), Af)
    S, DX, DP = gauss_stuff((XA + XA.T) / 2, (PA + PA.T) / 2)
    pairs, complete = neighbour_structure(lat, Rgc)
    wd, wp = W_entries(lat, Ac, Rgc, DX, DP, pairs)
    LW = LW_diag(lat, wd, wp, pairs)
    ys = 2 * float(np.sum(profile_h(Rgc, lat.c, R, d) * LW))
    ym = float(np.sum(lattice_DeltaPsi_h(lat, Rgc, R) * wd))
    v3 = abs(LW.sum()) / np.abs(LW).sum()
    Reff = (nA / (math.pi if d == 2 else 4 * math.pi / 3)) ** (1 / d)
    q = dict(R=R, nA=nA, Reff=Reff, S=S, ys=ys, ym=ym, mkin=float(np.sum(2 * np.diag(DP))), v3=v3,
             all=bool(complete.all()))
    print(f"   {d}D L={L} R={R} nA={nA} Reff={Reff:.3f} S={S:.6f} y_s={ys:.6e} y_m={ym:.6e} m_kin={q['mkin']:.5e} "
          f"v3={v3:.1e} all-complete={q['all']}", flush=True)
    return q

def verdict(d, rows, label):
    Re = np.array([q['Reff'] for q in rows]); S = np.array([q['S'] for q in rows])
    J = 8 * math.pi / 5 if d == 3 else math.pi / 2
    Om = 4 * math.pi if d == 3 else 2 * math.pi
    if d == 3:
        ce, _ = fit(Re, S, [2, 1, 0])
    else:
        sel = Re >= 6
        ce, _ = fit(Re[sel], S[sel], [1, 0])
    eta = ce[0] / Om
    ys = np.array([q['ys'] for q in rows]); ym = np.array([q['ym'] for q in rows])
    pw = [d + 1, d, d - 1]
    y0 = ys + kappa(d, 0.0) * ym
    c0, e0 = fit(Re, y0, pw); cs, es = fit(Re, ys, pw); cm, em = fit(Re, ym, pw)
    ctop = c0[0]; dom = abs(ctop) * Re[-1] ** (d + 1) / abs(y0[-1]); rJ = -ctop / (J * eta)
    xi0 = ((d - 2) / 2 - cs[0] / cm[0]) / (2 * (d - 1))
    pl = float(np.polyfit(np.log(Re), np.log(np.abs(y0)), 1)[0])
    BW = (8 * math.pi ** 2 / 15) * Re ** 4 if d == 3 else (math.pi ** 2 / 2) * Re ** 3
    mr = np.array([q['mkin'] for q in rows]) / BW
    kj = ctop < 0 and dom >= 0.5 and 0.5 <= rJ <= 2.0
    branch = ("K_J" if kj else ("L_J0 (no volume-order response)" if dom < 0.5 else
              ("L_J1 (repulsive)" if ctop > 0 else "L_J2 (induced G != area-law G)")))
    print(f"   {label}: eta={eta:.6f}; minimal-coupling y fit {c0} (+- {e0}); c_top={ctop:.4e}+-{e0[0]:.1e}; "
          f"dominance={dom:.3f}; r_J={rJ:.4f}; log-log slope of |y| vs R_eff = {pl:.3f}; y_s top {cs[0]:.3e}+-{es[0]:.1e}, "
          f"y_m top {cm[0]:.3e}+-{em[0]:.1e}, xi_0={xi0:.3f}; m_kin/BW={np.round(mr, 3).tolist()}", flush=True)
    return kj, branch, dict(eta=round(eta, 6), ctop=float(ctop), ectop=float(e0[0]), dom=round(dom, 4),
                            rJ=round(rJ, 4), slope=round(pl, 3), xi0=round(xi0, 4))

if run_p("P1"):
    print("== P1 (NOT BLIND) 2D, harmonic (log) exterior, full-lattice sums ==", flush=True)
    rows = [full_responses(2, 161, R) for R in range(4, 13)]
    ir = [full_responses(2, 121, R) for R in (4, 8)]
    g = [abs(a['ys'] - b['ys']) / abs(b['ys']) for a, b in zip(ir, [q for q in rows if q['R'] in (4, 8)])]
    check("P1-gate [numerics, NOT BLIND] 2D IR: y_s changes <= 10% between L=121 and L=161 (R = 4, 8)",
          all(x <= 0.10 for x in g), f"{np.round(g, 4).tolist()}")
    kj, br, info = verdict(2, rows, "P1 2D L=161")
    check("P1 [numerics, NOT BLIND] 2D Jacobson test (minimal coupling), pre-registered K_J criteria", kj,
          f"branch {br}: {info}")

if run_p("P2"):
    print("== P2 (NOT BLIND) 3D, full-lattice sums ==", flush=True)
    rows = [full_responses(3, 25, R) for R in (3.0, 3.5, 4.0, 4.5, 5.0)]
    ir = [full_responses(3, 21, R) for R in (3.0, 4.0)]
    yy = lambda q: q['ys'] - 0.5 * q['ym']
    g = [abs(yy(a) - yy(b)) / abs(yy(b)) for a, b in zip(ir, [q for q in rows if q['R'] in (3.0, 4.0)])]
    check("P2-gate [numerics, NOT BLIND] 3D IR: y_s - y_m/2 changes <= 10% between L=21 and L=25 (R = 3, 4)",
          all(x <= 0.10 for x in g), f"{np.round(g, 4).tolist()}")
    kj, br, info = verdict(3, rows, "P2 3D L=25")
    check("P2 [numerics, NOT BLIND] 3D Jacobson test (minimal coupling), pre-registered K_J criteria", kj,
          f"branch {br}: {info}")

if run_p("P3"):
    print("== P3 (NOT BLIND) box-size check of Bisognano-Wichmann, 2D ==", flush=True)
    tab = {}
    for L in (81, 161, 241):
        lat = Lat(2, L)
        for R in (8, 12):
            Ac = lat.ball(R); Af = lat.flat(Ac)
            XA = lat.block(Ac, 0.5 / np.sqrt(lat.lam), Af); PA = lat.block(Ac, 0.5 * np.sqrt(lat.lam), Af)
            S, DX, DP = gauss_stuff((XA + XA.T) / 2, (PA + PA.T) / 2)
            Reff = (len(Ac) / math.pi) ** 0.5
            tab[(L, R)] = float(np.sum(2 * np.diag(DP))) / ((math.pi ** 2 / 2) * Reff ** 3)
    print("   m_kin/BW:", {f"L={L},R={R}": round(v, 4) for (L, R), v in tab.items()}, flush=True)
    ok = all(0.8 <= tab[(241, R)] <= 1.25 for R in (8, 12)) and all(
        abs(tab[(241, R)] - 1) < abs(tab[(161, R)] - 1) < abs(tab[(81, R)] - 1) for R in (8, 12))
    check("P3 [numerics, NOT BLIND] BW restored as the box grows (2D)", ok,
          f"{ {f'{L},{R}': round(v, 4) for (L, R), v in tab.items()} }")

def cone_sparse(k, Rmax):
    from scipy.sparse import lil_matrix
    def vid(r, m):
        return 0 if r == 0 else 1 + k * (r - 1) * r // 2 + m
    N = 1 + k * Rmax * (Rmax + 1) // 2
    K = lil_matrix((N, N)); ring = np.zeros(N, int)
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
            s_, j = divmod(m, r)
            tg = [s_ * (r + 1) + j, s_ * (r + 1) + j + 1] + ([s_ * (r + 1) - 1] if j == 0 else [])
            for tm in tg:
                ups += 1
                if r < Rmax:
                    add(vid(r, m), vid(r + 1, tm % (k * (r + 1))))
                else:
                    K[vid(r, m), vid(r, m)] += 1
        cut[r] = ups
    return K.tocsc(), ring, cut

def cone_balls_sparse(k, Rmax, Rs):
    from scipy.sparse import identity
    from scipy.sparse.linalg import splu
    K, ring, cut = cone_sparse(k, Rmax)
    N = K.shape[0]
    Abig = np.where(ring <= max(Rs))[0]
    E = np.zeros((N, len(Abig))); E[Abig, np.arange(len(Abig))] = 1.0
    h = 0.35
    us = np.arange(-26.0, 22.0 + 1e-12, h)
    Xc = np.zeros((N, len(Abig)))
    Id = identity(N, format='csc')
    for u in us:
        t = math.exp(u)
        Xc += (h * t / math.pi) * splu((K + (t * t) * Id).tocsc()).solve(E)
    tf = tail_factor(h)
    Xc += (h / math.pi) * math.exp(us[0]) * tf * splu(K).solve(E) + (h / math.pi) * math.exp(-us[-1]) * tf * E
    X = Xc[Abig, :]
    P = (K @ Xc)[Abig, :]          # P = K X exactly (run-4 fix: no I - t^2 G cancellation)
    out = []
    for R in Rs:
        sub = np.where(ring[Abig] <= R)[0]
        Xs = X[np.ix_(sub, sub)]; Ps = P[np.ix_(sub, sub)]
        S, DX, DP = gauss_stuff((Xs + Xs.T) / 2, (Ps + Ps.T) / 2)
        out.append(dict(R=R, n=len(sub), S=S, cut=cut[R], b0=2 * DP[0, 0]))
    return out

if run_p("P4"):
    print("== P4 (NOT BLIND) cones with sparse solvers ==", flush=True)
    Rs = list(range(1, 14))
    res26 = {k: cone_balls_sparse(k, 26, Rs) for k in (6, 5)}
    worst = 0.0
    for k in (6, 5):
        Kd, ring, cut = cone_graph(k, 26)
        lam_, V = np.linalg.eigh(Kd); del Kd
        Xd = (V * (0.5 / np.sqrt(lam_))) @ V.T; Pd = (V * (0.5 * np.sqrt(lam_))) @ V.T; del V
        for q in res26[k]:
            Af = np.where(ring <= q['R'])[0]
            S, DX, DP = gauss_stuff(Xd[np.ix_(Af, Af)], Pd[np.ix_(Af, Af)])
            worst = max(worst, abs(S - q['S']) / S, abs(2 * DP[0, 0] - q['b0']) / (2 * DP[0, 0]))
        del Xd, Pd
    check("P4a [numerics, NOT BLIND] sparse route reproduces the dense cone results (R_max = 26)", worst < 1e-8,
          f"worst relative difference {worst:.2e}")
    res78 = {k: cone_balls_sparse(k, 78, Rs) for k in (6, 5, 7)}
    for k in (6, 5, 7):
        print(f"   R_max=78 k={k}: " + "; ".join(f"R={q['R']} n={q['n']} S={q['S']:.5f} cut={q['cut']} beta0={q['b0']:.4f}"
                                                for q in res78[k]), flush=True)
    cl = math.sqrt(1.5)
    def ratio_bw(rows):
        n = np.array([q['n'] for q in rows], float); b0 = np.array([q['b0'] for q in rows])
        return b0 / (math.pi * np.sqrt(n * math.sqrt(3) / (2 * math.pi)) / cl)
    r26 = ratio_bw(res26[6]); r78 = ratio_bw(res78[6])
    sel = (np.array(Rs) >= 6) & (np.array(Rs) <= 12)
    p4b = bool(np.all((r78[sel] >= 0.6) & (r78[sel] <= 1.6)) and np.all(np.abs(r78[sel] - 1) < np.abs(r26[sel] - 1)))
    check("P4b [numerics, NOT BLIND] apex BW restored as the cone grows (R_max 26 -> 78)", p4b,
          f"R_max=26: {np.round(r26[sel], 4).tolist()}; R_max=78: {np.round(r78[sel], 4).tolist()}")
    spl = CubicSpline(np.array(Rs, float), np.array([q['S'] for q in res78[6]]))
    cf, _ = fit(np.array([q['cut'] for q in res78[6]], float)[sel], np.array([q['S'] for q in res78[6]])[sel], [1, 0])
    eb6 = cf[0]
    M = {}; d2 = []
    for k in (5, 7):
        dS = []
        for q in res78[k]:
            Rx = (-1 + math.sqrt(1 + 4 * (q['n'] - 1) / 3)) / 2
            dS.append(q['S'] - float(spl(Rx)))
            if 8 <= q['R'] <= 12:
                d2.append((q['S'] - float(spl(Rx))) / (eb6 * (q['cut'] - 6 * (2 * Rx + 1))))
        M[k] = -np.array(dS) / np.array([q['b0'] for q in res78[k]])
    m1 = M[5][sel]
    p4c = bool(np.all(m1 > 0) and m1.max() / m1.min() <= 1.3 and np.all(M[7][sel] < 0)
               and all(0.8 <= x <= 1.25 for x in d2))
    check("P4c [numerics, NOT BLIND] at R_max = 78: point mass = disclination (M_1 > 0, R-independent), k=7 negative, "
          "D2 holds", p4c, f"M_1={np.round(m1, 6).tolist()}; M_7={np.round(M[7][sel], 6).tolist()}; "
          f"D2={np.round(d2, 4).tolist()}; eta_b(6)={eb6:.6f}")
    Reff6 = np.sqrt(np.array([q['n'] for q in res78[6]], float) * math.sqrt(3) / (2 * math.pi))
    cfl, _ = fit(Reff6[sel], np.array([q['S'] for q in res78[6]])[sel], [1, 0])
    eta_len = cfl[0] / (2 * math.pi)
    print(f"   P4 summary: eta_len={eta_len:.6f}; mean M_1={float(np.mean(m1)):.6f}; "
          f"M_1 2pi/(eta_len (pi/3) c) = {float(np.mean(m1)) * 2 * math.pi / (eta_len * math.pi / 3 * cl):.4f}",
          flush=True)


if run_p("P5"):
    print("== P5 (NOT BLIND) precision diagnosis of the modular kernel (2D, L=31, R=6) ==", flush=True)
    mp.mp.dps = 60
    L5, R5 = 31, 6
    lat5 = Lat(2, L5)
    Ac5 = lat5.ball(R5); Af5 = lat5.flat(Ac5); nA5 = len(Ac5)
    ci = int(np.where((Ac5 == lat5.c).all(1))[0][0])
    # float64 route (exact mode sums via DST)
    XA = lat5.block(Ac5, 0.5 / np.sqrt(lat5.lam), Af5); PA = lat5.block(Ac5, 0.5 * np.sqrt(lat5.lam), Af5)
    S64, DX64, DP64 = gauss_stuff((XA + XA.T) / 2, (PA + PA.T) / 2)
    b64 = 2 * DP64[ci, ci]
    # 60-digit route: X_A, P_A from the separable mode sum
    sv = [[mp.sqrt(mp.mpf(2) / (L5 + 1)) * mp.sin(mp.pi * kk * xx / (L5 + 1)) for xx in range(1, L5 + 1)]
          for kk in range(1, L5 + 1)]
    lam1 = [2 - 2 * mp.cos(mp.pi * kk / (L5 + 1)) for kk in range(1, L5 + 1)]
    Xl = [[mp.mpf(0)] * nA5 for _ in range(nA5)]; Pl = [[mp.mpf(0)] * nA5 for _ in range(nA5)]
    for k1 in range(L5):
        for k2 in range(L5):
            lam = lam1[k1] + lam1[k2]
            fx = 1 / (2 * mp.sqrt(lam)); fp = mp.sqrt(lam) / 2
            u = [sv[k1][a[0] - 1] * sv[k2][a[1] - 1] for a in Ac5]
            ux = [ui * fx for ui in u]; up = [ui * fp for ui in u]
            for i in range(nA5):
                Xi = Xl[i]; Pi = Pl[i]; uxi = ux[i]; upi = up[i]
                for j in range(i, nA5):
                    Xi[j] += uxi * u[j]; Pi[j] += upi * u[j]
    Xm = mp.matrix(nA5, nA5); Pm = mp.matrix(nA5, nA5)
    for i in range(nA5):
        for j in range(i, nA5):
            Xm[i, j] = Xm[j, i] = Xl[i][j]; Pm[i, j] = Pm[j, i] = Pl[i][j]
    E, V = mp.eigsy(Xm)
    Xh = V * mp.diag([mp.sqrt(E[i]) for i in range(nA5)]) * V.T
    C = Xh * Pm * Xh
    mu, Q = mp.eigsy(C)
    nus = [mp.sqrt(mu[i]) for i in range(nA5)]
    eps = [mp.log((n_ + mp.mpf(1) / 2) / (n_ - mp.mpf(1) / 2)) for n_ in nus]
    B = Xh * Q
    bmp = 2 * mp.fsum(B[ci, n] ** 2 * eps[n] / (2 * nus[n]) for n in range(nA5))
    Smp = mp.fsum((n_ + mp.mpf(1) / 2) * mp.log(n_ + mp.mpf(1) / 2) - (n_ - mp.mpf(1) / 2) * mp.log(n_ - mp.mpf(1) / 2)
                  for n_ in nus)
    Reff5 = (nA5 / math.pi) ** 0.5
    bw = math.pi * Reff5
    epsmax = max(eps)
    gain = float(bmp) / b64 - 1
    k5 = float(epsmax) > 35 and gain >= 0.10 and abs(float(bmp) / bw - 1) < abs(b64 / bw - 1)
    print(f"   n_A={nA5}, S float64={S64:.12f}, S 60-digit={mp.nstr(Smp, 15)}; eps_max (60-digit)={mp.nstr(epsmax, 6)}; "
          f"#modes with eps>30: {sum(1 for e in eps if e > 30)}", flush=True)
    check("P5 [numerics, NOT BLIND] modular-kernel clip: 60-digit eps_max > 35, 2D_P(c,c) gains >= 10%, closer to BW",
          k5, f"2D_P(c,c): float64={b64:.5f}, 60-digit={mp.nstr(bmp, 8)} (gain {gain:+.3f}); BW pi R_eff={bw:.5f}; "
          f"ratios {b64 / bw:.4f} -> {float(bmp) / bw:.4f}")


# =========================================================================== summary
print()
print(f"TOTAL: {sum(res)}/{len(res)} PASS (stage {STAGE})")
