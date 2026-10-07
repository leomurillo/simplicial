"""
Paper 55 — The Network of Ports: Space, Light Cones, and Area Laws from Passive Composition.  Certificate.

numpy / sympy / mpmath only (no torch: torch never runs on this machine).
Exact rational / symbolic arithmetic decides every vanishing, sign and membership claim tagged [exact].
Floating point appears only in checks tagged [numerics] or [witness], with stated tolerances.
Pseudo-random instances come from one fixed deterministic stream (random.Random(551001)).

PRE-REGISTERED FALSIFIERS (written 2026-10-01, before the first run; every branch is reportable)

K1 [exact] Composition (H1).
  K1a  Three random networks (6 nodes, 8-9 edges) of random passive two-ports Y_e(s) = G_e + s C_e + Gamma_e / s
       (G, C, Gamma = A^T A, rational): the assembled admittance Y(s) = sum_e P_e^T Y_e(s) P_e has a positive
       semidefinite Hermitian part at 5 sample points of Re s > 0, and so does its Kron reduction (Schur complement)
       onto the boundary nodes {0, 1}.  L-control: replacing one G_e by an indefinite matrix (an active two-port with
       a negative conductance) is flagged (non-PSD) at >= 1 sample point.
  K1b  One-port edges y_e(s) = g + c s + 1/(l s): Y = d0^T diag(y) d0 equals the stamped weighted Laplacian exactly;
       d0 1 = 0 and 1^T Y = 0 (Kirchhoff's current law = the Noether identity of the potential shift phi -> phi + c 1);
       Tellegen <d0 phi, i> = <phi, d0^T i>.
  K1c  The unit-conductance complete network K_N has admittance N I - J for N = 3..7 (N = 4: 4I - J, the frame metric
       of Paper 01); the effective resistance between any two vertices is 2/N.
  K1d  Pick matrix P_jk = (Y(s_j) + conj Y(s_k)) / (s_j + conj s_k) of the Kron-reduced driving-point admittance at
       node 0 of network #1 at 6 points of Re s > 0 is PSD.  L-control: a shunt conductance -100 at node 0 makes it
       non-PSD.
K2 [exact + 50-digit] Light cones (H2).  Lattice units, c = 1/sqrt(LC), D = 1/(RC), gamma = R/L.
  K2a  LC chain Bloch dispersion omega^2 = (4/LC) sin^2(k/2); group velocity cos(k/2)/sqrt(LC) <= c, equality only at
       k = 0.  RC chain: s(k) = -(4/RC) sin^2(k/2), real and <= 0 (no propagating mode).
  K2b  Exact mean-square displacement of the impulse response sum_n n^2 G_n(t):  LC  c^2 t^2;  RC  2 D t;  series-RLC
       links (telegraph)  (2c^2/gamma)(t - (1 - e^{-gamma t})/gamma) = c^2 t^2 + O(t^3) and = 2Dt - 2D/gamma + o(1).
  K2c  Discrete time, exact rationals: leapfrog LC (lambda^2 in {1, 1/4}) AND explicit-Euler RC (mu in {1/2, 1/4})
       both vanish exactly outside |n| <= m.  PRE-REGISTERED EXPECTATION: the strict discrete cone is a stencil
       property and does NOT discriminate.  The discriminators are: MSD = lambda^2 m^2 (ballistic) versus 2 mu m
       (diffusive), exactly; at lambda^2 = 1 (magic step) phi^m = (delta_m + delta_{-m})/2 (dispersionless); the
       continuum cone speed dx/dt is c/lambda (finite) versus D/(mu dx) -> infinity.
  K2d  Continuous time (50 digits).  G_LC(n,t) = J_{2|n|}(2ct) solves the chain ODE (residual < 1e-25) with generating
       function cos(2ct sin(k/2)) (residual < 1e-25); |G_LC| <= (ct)^{2|n|}/(2|n|)! on a grid (Lieb-Robinson-type
       bound).  PRE-REGISTERED: continuous time has NO strict cone: G_LC(60, t=50) != 0 (v = 1.2c).  Rate
       r(t) = -ln max_{|n - vt| <= 3} |G| / t:  at v = 1.2c it approaches the Debye rate 2v acosh v - 2 sqrt(v^2-1)
       = 0.16702: |r(t) - 0.16702| decreases over t in {50, 100, 200, 400} and is < 0.03 at t = 400;  at v = 0.8c,
       r(400) < 0.02 (inside the cone: algebraic decay).  RC: G_RC = e^{-2Dt} I_n(2Dt) > 0 for all |n| <= 100 at
       t = 1 (no front), and at v = 0.8 its rate at t = 400 is within 0.03 of 2 - sqrt(v^2+4) + v asinh(v/2) = 0.15796.
       Zero-rate velocity set: [-c, c] (LC) versus {0} (RC).
  K2e  Cauer: Z(s) = sum_{a in {1,2,3}} 2s/(s^2+a^2) (Paper 53's three-tank Foster port) has a Cauer ladder of 6
       positive rational elements reproducing Z exactly: the port is the end of a one-dimensional LC chain.
       L-control: replacing s^2+4 by s^2-4 yields some non-positive element or a broken expansion.
  K2f  Signature of the second-order symbol (exact, Sylvester / Descartes): square-lattice LC network
       sigma2 = diag(C, -w_x, -w_y) -> (n+, n0, n-) = (1, 0, 2) (Lorentzian); series-RLC: identical (loss is first
       order); RC: (0, 1, 2) (no time direction); isolated node: (1, 2, 0) (no space); one active link w_y < 0:
       (2, 0, 1) with omega^2(k = (0, pi/2)) < 0 (growth).  Comparison instance (Pinf-WhatIsMultiplicative §2 form,
       q = 7): M = [[-14, -a], [-a, -2]] is negative definite at a = 5 and indefinite at a = 6.
K3 [exact + numerics with exact covariance formulas] Area law (H3).
  K3a  [exact] Port-Hamiltonian FDT: for random rational J (skew), R >= 0, Q > 0 (4 storage variables),
       Sigma = T Q^{-1} solves (J-R)Q Sigma + Sigma Q (J-R)^T + 2 T R = 0 (Gibbs on the stored energy, independent of
       R and J).  L: resistors in two groups at T1 != T2: the unique stationary covariance is not c Q^{-1} for any c.
  K3b  [40-digit] Slack identity I(A:B) + D(rho_A x rho_B || rho) = beta sum_cut w_ij X_ij on a 6-node harmonic
       network, residual < 1e-30, with D >= 0, where S(AB) is computed from symplectic eigenvalues and
       beta<H> + ln Z from normal modes (two routes).
  K3c  [numerics] Thermal Gaussian states, beta = 1, w = 1, m^2 = 1: chain N = 240 (blocks l = 4..64), square 24^2
       (l = 2..10), cubic 10^3 (l = 2..5), diamond 6^3 conventional cells (l = 1..4 cells).  For each lattice:
       (i) I <= beta sum_cut w X + 1e-9 for every block;  (ii) band: max/min of I/|dA| <= 2.0 (square, cubic,
       diamond); chain: max/min of I <= 1.5;  (iii) volume: (I/|A|) at the largest block / at the smallest <= 0.6
       (square, cubic, diamond), <= 0.1 (chain);  (iv) fitted slope of ln I vs ln|dA| in [0.8, 1.2] and of ln I vs
       ln|A| <= 0.85 (square, cubic, diamond).  |dA| = number of cut edges.
  K3d  Controls on 576 nodes with square-lattice block geometry.  (C1) long-range random 4-regular multigraph (two
       fixed permutations): I/|dA|_geo grows (last/first >= 2.0) -- the GEOMETRIC area law is violated -- while
       I/cut stays in a band (max/min <= 2.0) and the cut bound holds.  (C2) all-to-all, w = 1/N: I <= 1 nat for every
       block, (I/cut)_last / (I/cut)_first <= 0.1, and the cut bound holds.
K4 [exact] Cut capacity (H4).
  K4a  40 random directed networks (7 nodes, rational capacities): Edmonds-Karp max flow = brute-force min cut
       exactly, and every s-t cut >= the flow.
  K4b  Independent ports (k = 4, rational amplitude gains g_e in (0,1), hidden-port noise theta_e (1 - g_e^2)): for 20
       random correlated input covariances, det Sigma_Y / det Sigma_N <= prod_e (Sigma_Y)_ee / (Sigma_N)_ee (Hadamard,
       i.e. I(X;Y) <= sum_e I(X_e;Y_e)), with equality for diagonal inputs.  L-control (correlated hidden ports,
       Sigma_N = 2(I - W), W = [[1/2, -1/4], [-1/4, 1/2]], signal eps W, eps = 1/10): per-port additivity FAILS, exact.
  K4c  ln(1+x) <= x (energy-per-bit form); Pendry-Bekenstein single channel (hbar = k_B = 1): P = pi T^2/12,
       S_dot = pi T/6, hence S_dot^2 = pi P / 3, exactly.
  K4d  Butterfly: min cut 2 to each sink; XOR at the bottleneck delivers both bits to both sinks for all 4 inputs;
       each of the 2 pure-forwarding choices leaves one sink unable to decode.
K5 [exact] The arrow on the cycle space (H5).
  K5a  10 random Markov networks (5-7 nodes, rational rates): d0^T J = 0; dim ker d0^T = |E| - |V| + 1 = b1;
       J = sum_f J_f z_f over fundamental cycles exactly.
  K5b  20 random trees: J = 0 exactly.
  K5c  Kolmogorov rates (k_ij / k_ji = a_j / a_i) on graphs with cycles: J = 0; perturbing one rate: J != 0;
       entropy production via edges (with pi) equals the cycle-affinity form exactly (log algebra); sigma > 0.
  K5d  [30-digit witness] Lossless LC ring of 5 nodes: frequency ratio 2 cos(pi/5) = golden ratio (exact); return
       amplitude G0(t) = (1 + 2 cos w1 t + 2 cos w2 t)/5 reaches >= 0.95 at some t <= 2000, at t = 2 pi F / w1 with
       F a Fibonacci number; lossy ring (gamma = 0.05): |G0(t) - 1/5| <= 0.01 on [400, 2000].
K6 [exact sympy] Which network (H6).
  K6   (the claim as handed to this session) tetrahedral first shell omega^2 = Omega^2 sum_n (1 - cos k.delta_n),
       |delta_n| = l: omega^2 = c^2 k^2 (1 - l^2 k^2/36 + O(k^4)), ISOTROPIC at that order, eta~ = 1/72.
       L: the k^4 term is anisotropic.
  K6'  (written from a hand expansion done BEFORE the first run) the k^4 term is -(c^2 l^2/36)(k^4 + 4P),
       P = sum_{i<j} k_i^2 k_j^2: coefficient 1/36 along <100>, 1/18 along <110>, 7/108 along <111> (ratio 7/3), so
       K6 holds only along the cube axes and its isotropy fails; c^2 = (2/3) Omega^2 l^2 is isotropic; the diamond
       acoustic branch Omega^2 (4 - |f|) agrees with the single-shell formula through O(k^4) and differs at O(k^6) by
       -(2/27) Omega^2 l^6 (k1 k2 k3)^2.
  K6b  Tetrahedral star: sum delta = 0, sum delta delta^T = (4 l^2/3) I, Gram = (l^2/3)(4I - J) (the frame metric).
  K6c  Fourth-moment ratio sum (k.delta)^4 / (sum (k.delta)^2)^2 differs between <100> and <111> for the sc, bcc, fcc
       and tetrahedral shells, and is equal for the icosahedral 12-star (a non-crystallographic 5-design).
  K6d  Maxwell: periodic bar frameworks.  Diamond 2x2x2 conventional cells: rank <= 128 < 189 (floppy);
       sc 4^3: rank 144 < 189 (floppy despite z = 6); fcc 2x2x2 conventional cells: rank 93 = 96 - 3 (rigid).
  K6e  Closed tetrahedral complexes: boundary of the 4-simplex gives B3 B3^T = 5I - J; the Kuhn-triangulated 3-torus
       (3^3 cubes, 162 tetrahedra) gives B3 B3^T = 4I - A (Laplacian of the 4-regular dual graph); every triangle lies
       in exactly two tetrahedra.
K7 [exact, fenced H7] Gauge.  Cycle holonomies of a random edge connection are invariant under A -> A + d0 chi and
  number b1; on a triangulated annulus a flat (d1 A = 0) connection with holonomy 1 around the hole exists and is not
  exact.

L (global): any FAIL above is retained in the RUN LOG below and reported in Paper 55 §8; post-diagnosis checks, if
any, are labelled NOT BLIND.

RUN LOG
  Run 1 (2026-10-01, p55_run1.log): 25/29 PASS.  Four pre-registered failures, all RETAINED:
   - K1a: composition passed (full and Kron-reduced Hermitian parts PSD at all 5 points), but the L-control was
     flagged at 0/5 points: the active two-port G = diag(1, -3) was MASKED by the passive ports around it, so the
     composite stayed passive.  Diagnosis: passivity of a composite does not certify its components (the converse of
     composition fails; this is the Port Principle's boundary rule seen from inside).  Control-design failure.
   - K2d: every sub-claim held except the pre-registered MONOTONE decrease of |rate - Debye|: deviations
     0.0103, 0.0027, 0.00013, 0.00087 at t = 50, 100, 200, 400.  Diagnosis: the +-3 window lowers the rate by
     ~ 2 acosh(v) * 3/t while the Debye prefactor raises it by ~ ln sqrt(2 pi nu tanh a)/t; the two cross between
     t = 200 and 400.  The limit (|dev| = 0.00087 < 0.03 at t = 400) holds.  Same lesson as Port P7: no pointwise
     finite-size monotonicity in pre-registrations.
   - K3d: C1 passed (expander: I/|dA|_geo grows x4.20, I/cut band 1.03).  C2 failed: all-to-all MI is O(1) (max
     0.035 nat) but (I/cut)_last/(I/cut)_first = 0.967, not <= 0.1.  Diagnosis: the pre-registered expectation was
     wrong -- mean-field MI is a function of f_A = |A|/N that is linear for small f_A, MI ~ f_A f_B, i.e. it tracks
     the weighted cut |A||B|/N, so all-to-all also obeys the CUT law and violates the GEOMETRIC area law.
   - K6: the isotropy claim fails exactly as K6' predicted: k^4 coefficient 1/36 (<100>), 1/18 (<110>), 7/108 (<111>).
  Post-diagnosis checks added for run 2 (NOT BLIND; criteria written here before run 2):
   - K1a' (NOT BLIND): masking witness: with G = diag(1, -3) the composite is passive at all 5 points while that
     two-port alone is not passive at s = 1; with G = diag(1, -100) the composite is flagged at >= 1 point.
   - K2d' (NOT BLIND): at n = 1.2 t exactly (no window), the ratio |J_{2n}(2t)| / Debye-leading
     e^{nu(tanh a - a)}/sqrt(2 pi nu tanh a) (nu = 2n, cosh a = 1.2) has |ratio - 1| decreasing over
     t in {100, 200, 400, 800}, < 0.01 at t = 800, and |ratio - 1 - u1(coth a)/nu| < 10/nu^2, u1(p) = (3p - 5p^3)/24.  (Bound first drafted as 5/nu^2; corrected
     BEFORE run 2 after computing the next Debye coefficient u2(coth a) = 7.65 by hand.)
   - K3d' (NOT BLIND): all-to-all: numeric MI equals the mean-field closed form
     s(nu(f)) + s(nu(1-f)) - s(nu_1) - s(nu_2) to relative 1e-8; I/|dA|_geo grows (last/first >= 2: geometric area
     law violated); I/(weighted cut |A||B|/N) has max/min <= 2; I <= 1 nat.
  Run 2 (2026-10-01, p55_run2.log): the 29 pre-registered lines are identical to run 1 (25/29, deterministic);
  post-diagnosis (NOT BLIND) 3/3: K1a' composite passive at 5/5 with the masked element, strong element flagged
  5/5; K2d' |ratio-1| = 0.0041, 0.0021, 0.0010, 0.00052 (halving with t, first Debye correction confirmed);
  K3d' all-to-all MI = mean-field closed form to 9.8e-10, I/|dA|_geo grows x4.02, I/weighted-cut band 1.034.
  Run 3 (2026-10-01, p55_run3.log): checker hygiene only -- K1d's helper called sp.nsimplify on exact Schur-
  complement rationals (a known exactness hazard, Paper 54 K3d / Port P4.R10); replaced by an is_Rational assertion.
  Results must be unchanged; see p55_run3.log.
"""
import sys
import math
import random
import itertools
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


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


RNG = random.Random(551001)
def rq(lo, hi, den=4):
    return sp.Rational(RNG.randint(int(lo * den), int(hi * den)), den)

def psd(Msym):
    """Exact PSD test for a real symmetric rational sympy matrix."""
    return signature(sp.Matrix(Msym))[2] == 0

def realify(X, Y):
    """Complex matrix X + iY  ->  real 2n x 2n matrix [[X, -Y], [Y, X]] (an algebra homomorphism)."""
    return sp.BlockMatrix([[X, -Y], [Y, X]]).as_explicit()

def herm_psd_realified(Rm):
    return psd((Rm + Rm.T) / 2)

def schur(Rm, keep, elim):
    A = Rm.extract(keep, keep); B = Rm.extract(keep, elim)
    C = Rm.extract(elim, keep); D = Rm.extract(elim, elim)
    return A - B * D.inv() * C

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


# =========================================================================== K1 composition
print("== K1 composition (H1) ==")
def rand_psd2():
    A = sp.Matrix(2, 2, lambda i, j: rq(-2, 2, 2))
    return A.T * A

S_PTS = [(sp.Integer(1), sp.Integer(0)), (sp.Rational(1, 2), sp.Integer(3)), (sp.Integer(2), sp.Rational(-5, 2)),
         (sp.Rational(1, 10), sp.Integer(1)), (sp.Integer(3), sp.Integer(7))]

def assemble_two_ports(n, edges, ports, s_pt):
    a, b = s_pt
    X = sp.zeros(n, n); Y = sp.zeros(n, n)
    for (i, j), (G, Cm, Gm) in zip(edges, ports):
        ReY = G + a * Cm + (a / (a**2 + b**2)) * Gm
        ImY = b * Cm - (b / (a**2 + b**2)) * Gm
        idx = [i, j]
        for p_ in range(2):
            for q_ in range(2):
                X[idx[p_], idx[q_]] += ReY[p_, q_]; Y[idx[p_], idx[q_]] += ImY[p_, q_]
    return X, Y

nets = []
for t in range(3):
    n = 6
    edges = random_connected_graph(n, 3 if t < 2 else 2)
    ports = [(rand_psd2(), rand_psd2(), rand_psd2()) for _ in edges]
    nets.append((n, edges, ports))

ok_full, ok_red = True, True
for (n, edges, ports) in nets:
    for s_pt in S_PTS:
        X, Y = assemble_two_ports(n, edges, ports, s_pt)
        Rm = realify(X, Y)
        ok_full &= herm_psd_realified(Rm)
        keep = [0, 1, n + 0, n + 1]; elim = [i for i in range(2 * n) if i not in keep]
        ok_red &= herm_psd_realified(schur(Rm, keep, elim))
# L-control: one active two-port
n, edges, ports = nets[0]
bad_ports = list(ports)
G0, C0, Gm0 = bad_ports[0]
bad_ports[0] = (sp.Matrix([[1, 0], [0, -3]]), C0, Gm0)
flagged = 0
for s_pt in S_PTS:
    X, Y = assemble_two_ports(n, edges, bad_ports, s_pt)
    if not herm_psd_realified(realify(X, Y)):
        flagged += 1
check("K1a [exact] random passive two-port networks: Hermitian part of Y(s) PSD at 5 RHP points; Kron reduction "
      "onto {0,1} PSD; active control flagged", ok_full and ok_red and flagged >= 1,
      f"full={ok_full}, Kron={ok_red}, control flagged at {flagged}/5 points")

# K1b one-port edges: Laplacian, Noether/KCL, Tellegen
s = sp.symbols('s')
n = 5
edges = random_connected_graph(n, 3)
ys = [rq(0, 2) + rq(0, 2) * s + 1 / (rq(1, 3) * s) for _ in edges]
d0 = incidence(n, edges)
Ylap = d0.T * sp.diag(*ys) * d0
Lstamp = sp.zeros(n, n)
for (i, j), y in zip(edges, ys):
    Lstamp[i, i] += y; Lstamp[j, j] += y; Lstamp[i, j] -= y; Lstamp[j, i] -= y
one = sp.ones(n, 1)
lap_ok = sp.simplify(Ylap - Lstamp) == sp.zeros(n, n)
noether_ok = (d0 * one == sp.zeros(len(edges), 1)) and sp.simplify(one.T * Ylap) == sp.zeros(1, n)
phi = sp.Matrix([rq(-3, 3) for _ in range(n)]); cur = sp.Matrix([rq(-3, 3) for _ in edges])
tellegen_ok = ((d0 * phi).T * cur)[0] == (phi.T * (d0.T * cur))[0]
check("K1b [exact] Y = d0^T diag(y) d0 = stamped Laplacian; d0 1 = 0, 1^T Y = 0 (KCL = Noether identity of the "
      "potential shift); Tellegen", lap_ok and noether_ok and tellegen_ok,
      f"Laplacian={lap_ok}, Noether/KCL={noether_ok}, Tellegen={tellegen_ok}")

# K1c complete network
kn_ok = True; reff_ok = True
for N in range(3, 8):
    edgesN = list(itertools.combinations(range(N), 2))
    dN = incidence(N, edgesN)
    L = dN.T * dN
    kn_ok &= (L == N * sp.eye(N) - sp.ones(N, N))
    Lplus = (L + sp.ones(N, N) / N).inv() - sp.ones(N, N) / N
    for (i, j) in edgesN:
        e = sp.zeros(N, 1); e[i] = 1; e[j] = -1
        reff_ok &= ((e.T * Lplus * e)[0] == sp.Rational(2, N))
check("K1c [exact] complete network K_N: admittance = N I - J (K4: 4I - J = frame metric), R_eff = 2/N, N = 3..7",
      kn_ok and reff_ok, f"Laplacian={kn_ok}, R_eff={reff_ok}")

# K1d Pick matrix of the driving-point admittance at node 0
def gmul(z, w): return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])
def gdiv(z, w):
    d = w[0]**2 + w[1]**2
    return ((z[0] * w[0] + z[1] * w[1]) / d, (z[1] * w[0] - z[0] * w[1]) / d)
P_PTS = [(sp.Integer(1), sp.Integer(0)), (sp.Rational(1, 2), sp.Integer(1)), (sp.Rational(1, 2), sp.Integer(-1)),
         (sp.Integer(2), sp.Integer(3)), (sp.Rational(1, 4), sp.Integer(2)), (sp.Integer(1), sp.Rational(-7, 2))]
def driving_point(n, edges, ports, s_pt, extra_shunt=0):
    X, Y = assemble_two_ports(n, edges, ports, s_pt)
    X = X.copy(); X[0, 0] += extra_shunt
    Rm = realify(X, Y)
    keep = [0, n]; elim = [i for i in range(2 * n) if i not in keep]
    Sm = schur(Rm, keep, elim)
    x_, y_ = sp.Rational(Sm[0, 0]), sp.Rational(Sm[1, 0])
    assert x_.is_Rational and y_.is_Rational and x_ == Sm[0, 0] and y_ == Sm[1, 0]
    return (x_, y_)
def pick_psd(vals, pts_):
    m = len(pts_)
    Pr = sp.zeros(m, m); Pi = sp.zeros(m, m)
    for j in range(m):
        for k in range(m):
            num = (vals[j][0] + vals[k][0], vals[j][1] - vals[k][1])
            den = (pts_[j][0] + pts_[k][0], pts_[j][1] - pts_[k][1])
            q = gdiv(num, den)
            Pr[j, k] = q[0]; Pi[j, k] = q[1]
    return psd(realify(Pr, Pi))
n, edges, ports = nets[0]
vals = [driving_point(n, edges, ports, p) for p in P_PTS]
vals_bad = [driving_point(n, edges, ports, p, extra_shunt=-100) for p in P_PTS]
pk_good, pk_bad = pick_psd(vals, P_PTS), pick_psd(vals_bad, P_PTS)
check("K1d [exact] Pick (defect-Gram) matrix of the Kron-reduced driving-point admittance PSD; active shunt control "
      "non-PSD", pk_good and not pk_bad, f"good PSD={pk_good}, control PSD={pk_bad}")


# =========================================================================== K2 light cones
print("== K2 light cones (H2) ==")
k, t, Lp, Cp, Rp, gam, cc, DD = sp.symbols('k t L C R gamma c D', positive=True)
w2_LC = (2 / (Lp * Cp)) * (1 - sp.cos(k))
disp_ok = sp.simplify(w2_LC - (4 / (Lp * Cp)) * sp.sin(k / 2)**2) == 0
omega = 2 / sp.sqrt(Lp * Cp) * sp.sin(k / 2)
vg = sp.diff(omega, k)
vg_ok = sp.simplify(vg - sp.cos(k / 2) / sp.sqrt(Lp * Cp)) == 0 and sp.simplify(vg.subs(k, 0) - 1 / sp.sqrt(Lp * Cp)) == 0
s_RC = (1 / (Rp * Cp)) * (2 * sp.cos(k) - 2)
rc_ok = sp.simplify(s_RC + (4 / (Rp * Cp)) * sp.sin(k / 2)**2) == 0
check("K2a [exact] LC: omega^2 = (4/LC) sin^2(k/2), v_g = cos(k/2)/sqrt(LC) <= c (max at k=0); RC: s = -(4/RC) "
      "sin^2(k/2) <= 0 (no propagation)", disp_ok and vg_ok and rc_ok, f"LC={disp_ok}, v_g={vg_ok}, RC={rc_ok}")

F_LC = sp.cos(2 * cc * t * sp.sin(k / 2))
ode_LC = sp.simplify(sp.diff(F_LC, t, 2) + 4 * cc**2 * sp.sin(k / 2)**2 * F_LC) == 0
msd_LC = sp.simplify(-sp.diff(F_LC, k, 2).subs(k, 0))
F_RC = sp.exp(-2 * DD * t * (1 - sp.cos(k)))
ode_RC = sp.simplify(sp.diff(F_RC, t) + 4 * DD * sp.sin(k / 2)**2 * F_RC) == 0
msd_RC = sp.simplify(-sp.diff(F_RC, k, 2).subs(k, 0))
m_tel = (2 * cc**2 / gam) * (t - (1 - sp.exp(-gam * t)) / gam)
tel_ode = sp.simplify(sp.diff(m_tel, t, 2) + gam * sp.diff(m_tel, t) - 2 * cc**2) == 0
tel_init = m_tel.subs(t, 0) == 0 and sp.simplify(sp.diff(m_tel, t).subs(t, 0)) == 0
tel_short = sp.simplify(sp.series(m_tel, t, 0, 3).removeO() - cc**2 * t**2) == 0
tel_long = sp.simplify(sp.limit(m_tel - (2 * cc**2 / gam) * t, t, sp.oo) + 2 * cc**2 / gam**2) == 0
check("K2b [exact] MSD: LC c^2 t^2 (ballistic); RC 2Dt (diffusive); RLC telegraph (2c^2/g)(t-(1-e^{-gt})/g): "
      "c^2 t^2 short, 2Dt - 2D/g long",
      ode_LC and msd_LC == cc**2 * t**2 and ode_RC and msd_RC == 2 * DD * t and tel_ode and tel_init and tel_short
      and tel_long, f"LC MSD={msd_LC}, RC MSD={msd_RC}, telegraph ode={tel_ode} short={tel_short} long={tel_long}")

def run_discrete(kind, par, M):
    size = 2 * M + 5; c0 = M + 2
    def lap(p): return [(p[i - 1] if i > 0 else 0) - 2 * p[i] + (p[i + 1] if i < size - 1 else 0) for i in range(size)]
    phi0 = [Fr(0)] * size; phi0[c0] = Fr(1)
    supp_ok, msd = True, []
    if kind == 'LC':
        l0 = lap(phi0)
        phi1 = [phi0[i] + Fr(1, 2) * par * l0[i] for i in range(size)]
        prev, cur = phi0, phi1
        hist = [phi0, phi1]
        for m_ in range(1, M):
            lc = lap(cur)
            nxt = [2 * cur[i] - prev[i] + par * lc[i] for i in range(size)]
            prev, cur = cur, nxt; hist.append(cur)
    else:
        hist = [phi0]; cur = phi0
        for m_ in range(M):
            lc = lap(cur)
            cur = [cur[i] + par * lc[i] for i in range(size)]; hist.append(cur)
    for m_, ph in enumerate(hist):
        supp_ok &= all(ph[i] == 0 for i in range(size) if abs(i - c0) > m_)
        msd.append(sum((i - c0)**2 * ph[i] for i in range(size)))
    return supp_ok, msd, hist, c0
M = 12
cone_all, msd_ok = True, True
for l2 in (Fr(1), Fr(1, 4)):
    sok, msd, hist, c0 = run_discrete('LC', l2, M)
    cone_all &= sok; msd_ok &= all(msd[m_] == l2 * m_**2 for m_ in range(M + 1))
    if l2 == 1:
        magic = all(hist[m_][c0 + m_] == Fr(1, 2) and hist[m_][c0 - m_] == Fr(1, 2) and
                    sum(abs(x) for x in hist[m_]) == 1 for m_ in range(1, M + 1))
for mu in (Fr(1, 2), Fr(1, 4)):
    sok, msd, hist, c0 = run_discrete('RC', mu, M)
    cone_all &= sok; msd_ok &= all(msd[m_] == 2 * mu * m_ for m_ in range(M + 1))
dx, lam_, mu_ = sp.symbols('dx lambda mu', positive=True)
speed_LC = cc / lam_
speed_RC = sp.limit(DD / (mu_ * dx), dx, 0)
check("K2c [exact] discrete time: BOTH leapfrog-LC and Euler-RC vanish outside |n|<=m (stencil cone, not a "
      "discriminator); MSD lambda^2 m^2 vs 2 mu m; magic step dispersionless; continuum cone speed c/lambda vs oo",
      cone_all and msd_ok and magic and speed_RC == sp.oo,
      f"strict cones={cone_all}, MSD laws={msd_ok}, magic step={magic}, RC continuum speed={speed_RC}")

mp.mp.dps = 50
def G_LC(n_, t_): return mp.besselj(2 * abs(n_), 2 * t_)
def G_RC(n_, t_): return mp.exp(-2 * t_) * mp.besseli(abs(n_), 2 * t_)
res_ode = max(abs(mp.diff(lambda tt: G_LC(n_, tt), t_, 2) - (G_LC(n_ + 1, t_) - 2 * G_LC(n_, t_) + G_LC(n_ - 1, t_)))
              for n_ in (0, 1, 3, 7) for t_ in (mp.mpf('0.7'), mp.mpf(3), mp.mpf(11)))
kk, tt0 = mp.mpf('0.7'), mp.mpf(3)
gen = mp.fsum(G_LC(n_, tt0) * mp.cos(kk * n_) for n_ in range(-80, 81))
res_gen = abs(gen - mp.cos(2 * tt0 * mp.sin(kk / 2)))
lr_ok = all(abs(G_LC(n_, t_)) <= mp.mpf(t_)**(2 * n_) / mp.factorial(2 * n_)
            for n_ in range(1, 41) for t_ in (0.5, 1, 2, 5, 10, 20))
outside = abs(G_LC(60, 50))
def rate(Gf, v, t_):
    n0 = int(mp.floor(v * t_))
    mx = max(abs(Gf(n_, t_)) for n_ in range(n0 - 3, n0 + 4))
    return -mp.log(mx) / t_
r_star = 2 * 1.2 * mp.acosh(1.2) - 2 * mp.sqrt(1.2**2 - 1)
rates12 = [rate(G_LC, mp.mpf('1.2'), T) for T in (50, 100, 200, 400)]
dev12 = [abs(r - r_star) for r in rates12]
r08 = rate(G_LC, mp.mpf('0.8'), 400)
rc_pos = all(G_RC(n_, 1) > 0 for n_ in range(0, 101))
r_rc_star = 2 - mp.sqrt(mp.mpf('0.64') + 4) + mp.mpf('0.8') * mp.asinh(mp.mpf('0.4'))
r_rc = rate(G_RC, mp.mpf('0.8'), 400)
k2d = (res_ode < mp.mpf('1e-25') and res_gen < mp.mpf('1e-25') and lr_ok and outside > 0 and
       all(dev12[i + 1] < dev12[i] for i in range(3)) and dev12[-1] < 0.03 and r08 < 0.02 and rc_pos and
       abs(r_rc - r_rc_star) < 0.03)
check("K2d [50-digit] continuous time: J_{2n}(2ct) solves the chain; LR bound; NO strict cone (tails); front rate "
      "-> Debye 0.16702 at v=1.2c; ~0 at v=0.8c; RC has no front and rate 0.158 at v=0.8", k2d,
      f"ODE res={mp.nstr(res_ode, 3)}, gen res={mp.nstr(res_gen, 3)}, LR={lr_ok}, |G(60,50)|={mp.nstr(outside, 4)}, "
      f"rates(1.2c)={[mp.nstr(r, 5) for r in rates12]} vs {mp.nstr(r_star, 5)}, rate(0.8c)={mp.nstr(r08, 3)}, "
      f"RC>0={rc_pos}, RC rate={mp.nstr(r_rc, 5)} vs {mp.nstr(r_rc_star, 5)}")

def cauer(Z):
    elems = []
    f = sp.cancel(1 / Z); kind = 'C'
    for _ in range(40):
        N_, D_ = sp.fraction(sp.cancel(f))
        pN, pD = sp.Poly(N_, s), sp.Poly(D_, s)
        if pN.degree() != pD.degree() + 1:
            return elems, False
        a_ = pN.LC() / pD.LC()
        elems.append((kind, a_))
        rem = sp.cancel(f - a_ * s)
        if rem == 0:
            return elems, True
        f = sp.cancel(1 / rem); kind = 'L' if kind == 'C' else 'C'
    return elems, False
def rebuild(elems):
    f = sp.Integer(0)
    for kind, a_ in reversed(elems):
        f = a_ * s + (1 / f if f != 0 else 0)
    return sp.cancel(1 / f)
Zg = sum(2 * s / (s**2 + a_**2) for a_ in (1, 2, 3))
el_g, fin_g = cauer(Zg)
pos_g = fin_g and len(el_g) == 6 and all(a_ > 0 for _, a_ in el_g) and sp.simplify(rebuild(el_g) - Zg) == 0
Zb = 2 * s / (s**2 + 1) + 2 * s / (s**2 - 4) + 2 * s / (s**2 + 9)
el_b, fin_b = cauer(Zb)
flag_b = (not fin_b) or any(a_ <= 0 for _, a_ in el_b)
check("K2e [exact] Cauer ladder of the three-tank Foster port: 6 positive elements, exact reconstruction (the port "
      "is the end of a 1D LC chain); non-reactance control flagged", pos_g and flag_b,
      f"good elements={[(k_, str(a_)) for k_, a_ in el_g]}, control elements={[(k_, str(a_)) for k_, a_ in el_b]} "
      f"finished={fin_b}")

C1, wx, wy = 1, 1, 2
sig_LC = signature(sp.diag(C1, -wx, -wy))
sig_RC = signature(sp.diag(0, -wx, -wy))
sig_node = signature(sp.diag(C1, 0, 0))
sig_act = signature(sp.diag(C1, -wx, 1))
w2_act = (2 * wx * (1 - sp.cos(0)) + 2 * (-1) * (1 - sp.cos(sp.pi / 2))) / C1
sig_P7a5 = signature(sp.Matrix([[-14, -5], [-5, -2]]))
sig_P7a6 = signature(sp.Matrix([[-14, -6], [-6, -2]]))
check("K2f [exact] second-order symbol: LC/RLC (1,0,2) Lorentzian; RC (0,1,2); isolated node (1,2,0); active link "
      "(2,0,1) with omega^2<0; Pinf q=7 form: a=5 neg-def, a=6 indefinite",
      sig_LC == (1, 0, 2) and sig_RC == (0, 1, 2) and sig_node == (1, 2, 0) and sig_act == (2, 0, 1) and w2_act < 0
      and sig_P7a5 == (0, 0, 2) and sig_P7a6 == (1, 0, 1),
      f"LC={sig_LC}, RC={sig_RC}, node={sig_node}, active={sig_act} (omega^2={w2_act}), Pinf a=5 {sig_P7a5}, "
      f"a=6 {sig_P7a6}")


# =========================================================================== K3 area law
print("== K3 area law (H3) ==")
# K3a port-Hamiltonian FDT (exact)
nst = 4
A_ = sp.Matrix(nst, nst, lambda i, j: rq(-2, 2, 2))
Qm = A_.T * A_ + sp.eye(nst)
Bj = sp.Matrix(nst, nst, lambda i, j: rq(-2, 2, 2)); Jm = Bj - Bj.T
Br = sp.Matrix(2, nst, lambda i, j: rq(-2, 2, 2)); Rm_ = Br.T * Br
T_ = sp.Rational(3, 2)
Sig = T_ * Qm.inv()
lyap = (Jm - Rm_) * Qm * Sig + Sig * Qm * (Jm - Rm_).T + 2 * T_ * Rm_
fdt_ok = sp.simplify(lyap) == sp.zeros(nst, nst)
# two temperatures, full-rank damping, unique solution
Br1 = sp.Matrix(nst, nst, lambda i, j: rq(-2, 2, 2)); R1 = Br1.T * Br1 + sp.eye(nst) / 2
Br2 = sp.Matrix(nst, nst, lambda i, j: rq(-2, 2, 2)); R2 = Br2.T * Br2
T1, T2 = sp.Integer(1), sp.Integer(3)
Rt = R1 + R2
syms = sp.symbols('x0:%d' % (nst * (nst + 1) // 2))
Sg = sp.zeros(nst, nst); idx = 0
for i in range(nst):
    for j in range(i, nst):
        Sg[i, j] = syms[idx]; Sg[j, i] = syms[idx]; idx += 1
eqs = (Jm - Rt) * Qm * Sg + Sg * Qm * (Jm - Rt).T + 2 * (T1 * R1 + T2 * R2)
sol = sp.solve(list(eqs), syms, dict=True)
Sg_sol = Sg.subs(sol[0]) if len(sol) == 1 else None
cand = Sg_sol * Qm if Sg_sol is not None else None
two_T_noneq = (Sg_sol is not None) and not all(cand[i, j] == (cand[0, 0] if i == j else 0)
                                               for i in range(nst) for j in range(nst))
check("K3a [exact] port-Hamiltonian FDT: Sigma = T Q^{-1} (Gibbs on stored energy) solves the Lyapunov equation for "
      "any J, R; two resistor temperatures: unique Sigma not proportional to Q^{-1}", fdt_ok and two_T_noneq,
      f"FDT={fdt_ok}, unique two-T solution found={Sg_sol is not None}, non-Gibbs={two_T_noneq}")

# K3b slack identity at 40 digits
mp.mp.dps = 40
def mp_thermal(Kmat, beta):
    E, U = mp.eigsy(Kmat)
    nn = Kmat.rows
    w = [mp.sqrt(E[i]) for i in range(nn)]
    cx = [mp.coth(beta * w[i] / 2) / (2 * w[i]) for i in range(nn)]
    cp = [w[i] * mp.coth(beta * w[i] / 2) / 2 for i in range(nn)]
    X = U * mp.diag(cx) * U.T; P = U * mp.diag(cp) * U.T
    return X, P, w
def mp_sub(Mm, ids):
    return mp.matrix([[Mm[i, j] for j in ids] for i in ids])
def mp_entropy(X, P, ids):
    XA, PA = mp_sub(X, ids), mp_sub(P, ids)
    E, U = mp.eigsy(XA)
    sq = U * mp.diag([mp.sqrt(E[i]) for i in range(len(ids))]) * U.T
    E2, _ = mp.eigsy(sq * PA * sq)
    S_ = mp.mpf(0)
    for i in range(len(ids)):
        nu = mp.sqrt(E2[i])
        S_ += (nu + mp.mpf(1) / 2) * mp.log(nu + mp.mpf(1) / 2)
        if nu - mp.mpf(1) / 2 > mp.mpf('1e-35'):
            S_ -= (nu - mp.mpf(1) / 2) * mp.log(nu - mp.mpf(1) / 2)
    return S_
nn = 6
edges6 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3), (1, 4)]
wts6 = [mp.mpf(1), mp.mpf('0.5'), mp.mpf(2), mp.mpf(1), mp.mpf('1.5'), mp.mpf(1), mp.mpf('0.7'), mp.mpf('0.3')]
K6m = mp.matrix(nn, nn)
for (i, j), w_ in zip(edges6, wts6):
    K6m[i, i] += w_; K6m[j, j] += w_; K6m[i, j] -= w_; K6m[j, i] -= w_
for i in range(nn): K6m[i, i] += mp.mpf('0.8')
beta = mp.mpf('1.3')
X6, P6, w6 = mp_thermal(K6m, beta)
Aset, Bset = [0, 1, 2], [3, 4, 5]
SA, SB, SAB = mp_entropy(X6, P6, Aset), mp_entropy(X6, P6, Bset), mp_entropy(X6, P6, list(range(nn)))
MI = SA + SB - SAB
cut = mp.fsum(w_ * X6[i, j] for (i, j), w_ in zip(edges6, wts6) if (i in Aset) != (j in Aset))
lnZ = -mp.fsum(mp.log(2 * mp.sinh(beta * w_ / 2)) for w_ in w6)
E_rho = mp.fsum(P6[i, i] for i in range(nn)) / 2 + mp.fsum(K6m[i, j] * X6[j, i] for i in range(nn) for j in range(nn)) / 2
E_sig = E_rho + cut
D_rel = -(SA + SB) + beta * E_sig + lnZ
slack_res = abs(MI + D_rel - beta * cut)
check("K3b [40-digit] slack identity I(A:B) + D(rho_A x rho_B || rho) = beta sum_cut w X (symplectic entropy vs "
      "normal-mode thermodynamics); D >= 0", slack_res < mp.mpf('1e-30') and D_rel >= 0,
      f"I={mp.nstr(MI, 8)}, D={mp.nstr(D_rel, 8)}, beta*cut={mp.nstr(beta * cut, 8)}, residual={mp.nstr(slack_res, 3)}")

# K3c lattices (float64, exact covariance formulas)
BETA, MSQ = 1.0, 1.0
def thermal_np(Kmat, beta=BETA):
    E, U = np.linalg.eigh(Kmat)
    w = np.sqrt(E)
    cth = 1.0 / np.tanh(beta * w / 2)
    X = (U * (cth / (2 * w))) @ U.T
    P = (U * (w * cth / 2)) @ U.T
    return X, P
def S_np(X, P, ids):
    ids = np.asarray(ids)
    XA = X[np.ix_(ids, ids)]; PA = P[np.ix_(ids, ids)]
    E, U = np.linalg.eigh(XA)
    sq = (U * np.sqrt(E)) @ U.T
    nu = np.sqrt(np.clip(np.linalg.eigvalsh(sq @ PA @ sq), 0.25, None))
    a_ = nu + 0.5; b_ = nu - 0.5
    return float(np.sum(a_ * np.log(a_)) - np.sum(np.where(b_ > 1e-14, b_ * np.log(np.where(b_ > 1e-14, b_, 1.0)), 0.0)))
def build_K(N, edge_w, msq=MSQ):
    Kmat = np.zeros((N, N))
    for (i, j), w_ in edge_w.items():
        Kmat[i, i] += w_; Kmat[j, j] += w_; Kmat[i, j] -= w_; Kmat[j, i] -= w_
    Kmat += msq * np.eye(N)
    return Kmat
def block_stats(N, edge_w, blocks, X=None, P=None):
    Kmat = build_K(N, edge_w)
    if X is None:
        X, P = thermal_np(Kmat)
    Sall = S_np(X, P, range(N))
    out = []
    for Aids in blocks:
        Aset_ = set(Aids); Bids = [i for i in range(N) if i not in Aset_]
        I_ = S_np(X, P, Aids) + S_np(X, P, Bids) - Sall
        cutc = sum(w_ for (i, j), w_ in edge_w.items() if (i in Aset_) != (j in Aset_))
        ncut = sum(1 for (i, j), w_ in edge_w.items() if (i in Aset_) != (j in Aset_))
        bnd = BETA * sum(w_ * X[i, j] for (i, j), w_ in edge_w.items() if (i in Aset_) != (j in Aset_))
        out.append(dict(I=I_, cut=ncut, cutw=cutc, vol=len(Aids), bound=bnd))
    return out
def slope(xs, ys):
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0])

lat = {}
Nch = 240
e_ch = {(i, (i + 1) % Nch) if i < (i + 1) % Nch else ((i + 1) % Nch, i): 1.0 for i in range(Nch)}
lat['chain'] = block_stats(Nch, e_ch, [list(range(l)) for l in (4, 8, 16, 32, 64)])
Lsq = 24
def sqid(x, y): return (x % Lsq) * Lsq + (y % Lsq)
e_sq = {}
for x in range(Lsq):
    for y in range(Lsq):
        for (u, v) in ((sqid(x, y), sqid(x + 1, y)), (sqid(x, y), sqid(x, y + 1))):
            e_sq[(min(u, v), max(u, v))] = 1.0
sq_blocks = [[sqid(x, y) for x in range(l) for y in range(l)] for l in (2, 3, 4, 6, 8, 10)]
lat['square'] = block_stats(Lsq * Lsq, e_sq, sq_blocks)
Lc = 10
def cid(x, y, z): return ((x % Lc) * Lc + (y % Lc)) * Lc + (z % Lc)
e_cu = {}
for x in range(Lc):
    for y in range(Lc):
        for z in range(Lc):
            for (u, v) in ((cid(x, y, z), cid(x + 1, y, z)), (cid(x, y, z), cid(x, y + 1, z)), (cid(x, y, z), cid(x, y, z + 1))):
                e_cu[(min(u, v), max(u, v))] = 1.0
lat['cubic'] = block_stats(Lc**3, e_cu, [[cid(x, y, z) for x in range(l) for y in range(l) for z in range(l)]
                                         for l in (2, 3, 4, 5)])
Ld = 6; side = 4 * Ld
base = [(0, 0, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0)]
pos = []
for cx in range(Ld):
    for cy in range(Ld):
        for cz in range(Ld):
            for b in base:
                pa = (4 * cx + b[0], 4 * cy + b[1], 4 * cz + b[2])
                pos.append(pa); pos.append(((pa[0] + 1) % side, (pa[1] + 1) % side, (pa[2] + 1) % side))
pid = {p_: i for i, p_ in enumerate(pos)}
e_di = {}
for i, p_ in enumerate(pos):
    if i % 2 == 0:
        for d_ in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)):
            q_ = ((p_[0] + d_[0]) % side, (p_[1] + d_[1]) % side, (p_[2] + d_[2]) % side)
            j = pid[q_]; e_di[(min(i, j), max(i, j))] = 1.0
di_blocks = [[i for i, p_ in enumerate(pos) if all(c_ < 4 * l for c_ in p_)] for l in (1, 2, 3, 4)]
lat['diamond'] = block_stats(len(pos), e_di, di_blocks)

k3c_detail = []
k3c_ok = True
for name, st in lat.items():
    Is = np.array([d['I'] for d in st]); cuts = np.array([d['cut'] for d in st]); vols = np.array([d['vol'] for d in st])
    bnd_ok = all(d['I'] <= d['bound'] + 1e-9 for d in st)
    vol_ratio = (Is[-1] / vols[-1]) / (Is[0] / vols[0])
    if name == 'chain':
        band = Is.max() / Is.min(); ok_ = bnd_ok and band <= 1.5 and vol_ratio <= 0.1
        k3c_detail.append(f"{name}: I={np.round(Is, 4).tolist()}, max/min I={band:.3f}, vol ratio={vol_ratio:.4f}, bound={bnd_ok}")
    else:
        band = (Is / cuts).max() / (Is / cuts).min()
        sl_c, sl_v = slope(cuts, Is), slope(vols, Is)
        ok_ = bnd_ok and band <= 2.0 and vol_ratio <= 0.6 and 0.8 <= sl_c <= 1.2 and sl_v <= 0.85
        k3c_detail.append(f"{name}: I/|dA|={np.round(Is / cuts, 5).tolist()}, band={band:.3f}, vol ratio={vol_ratio:.3f}, "
                          f"slope(cut)={sl_c:.3f}, slope(vol)={sl_v:.3f}, I/bound={np.round(Is / np.array([d['bound'] for d in st]), 3).tolist()}, bound={bnd_ok}")
    k3c_ok &= ok_
for line in k3c_detail: print("   ", line)
check("K3c [numerics, exact covariance] thermal MI on chain/square/cubic/diamond: cut bound, area band, not volume",
      k3c_ok, "see lines above")

# K3d controls
N576 = Lsq * Lsq
perm1 = list(range(N576)); RNG.shuffle(perm1)
perm2 = list(range(N576)); RNG.shuffle(perm2)
e_ex = {}
for pm in (perm1, perm2):
    for i in range(N576):
        j = pm[i]
        if i != j:
            key = (min(i, j), max(i, j)); e_ex[key] = e_ex.get(key, 0.0) + 1.0
ex = block_stats(N576, e_ex, sq_blocks)
geo = np.array([4 * l for l in (2, 3, 4, 6, 8, 10)], dtype=float)
Iex = np.array([d['I'] for d in ex]); cex = np.array([d['cutw'] for d in ex])
c1_geo = (Iex[-1] / geo[-1]) / (Iex[0] / geo[0])
c1_band = (Iex / cex).max() / (Iex / cex).min()
c1_bnd = all(d['I'] <= d['bound'] + 1e-9 for d in ex)
# all-to-all, w = 1/N: K = (1 + m^2) I - J/N
Kall = (1 + MSQ) * np.eye(N576) - np.ones((N576, N576)) / N576
Xa, Pa = thermal_np(Kall)
Sall_a = S_np(Xa, Pa, range(N576))
Ia, cuta, bnda = [], [], []
for Aids in sq_blocks:
    Bids = [i for i in range(N576) if i not in set(Aids)]
    Ia.append(S_np(Xa, Pa, Aids) + S_np(Xa, Pa, Bids) - Sall_a)
    cuta.append(len(Aids) * len(Bids))
    bnda.append(BETA * (1.0 / N576) * Xa[np.ix_(Aids, Bids)].sum())
Ia, cuta = np.array(Ia), np.array(cuta, dtype=float)
c2_ok = Ia.max() <= 1.0 and ((Ia[-1] / cuta[-1]) / (Ia[0] / cuta[0])) <= 0.1 and all(Ia[i] <= bnda[i] + 1e-9 for i in range(len(Ia)))
print(f"    expander: I={np.round(Iex, 3).tolist()}, I/geo last/first={c1_geo:.3f}, I/cut band={c1_band:.3f}, bound={c1_bnd}")
print(f"    all-to-all: I={np.round(Ia, 6).tolist()}, (I/cut) last/first={(Ia[-1] / cuta[-1]) / (Ia[0] / cuta[0]):.4f}")
check("K3d [numerics] controls: long-range expander violates the GEOMETRIC area law but obeys the cut law; "
      "all-to-all MI stays O(1)", c1_geo >= 2.0 and c1_band <= 2.0 and c1_bnd and c2_ok,
      f"C1 geo growth={c1_geo:.2f}, C1 cut band={c1_band:.2f}, C2 ok={c2_ok}")


# =========================================================================== K4 cut capacity
print("== K4 cut capacity (H4) ==")
def maxflow(nv, cap, s_, t_):
    flow = {e: Fr(0) for e in cap}
    def resid(u, v):
        return cap.get((u, v), Fr(0)) - flow.get((u, v), Fr(0)) + flow.get((v, u), Fr(0))
    total = Fr(0)
    while True:
        par = {s_: None}; queue = [s_]
        while queue and t_ not in par:
            u = queue.pop(0)
            for v in range(nv):
                if v not in par and resid(u, v) > 0:
                    par[v] = u; queue.append(v)
        if t_ not in par:
            return total
        path = []; v = t_
        while par[v] is not None:
            path.append((par[v], v)); v = par[v]
        bott = min(resid(u, v) for u, v in path)
        for u, v in path:
            back = min(bott, flow.get((v, u), Fr(0)))
            if back > 0:
                flow[(v, u)] -= back
            if bott - back > 0:
                flow[(u, v)] = flow.get((u, v), Fr(0)) + (bott - back)
        total += bott
def mincut(nv, cap, s_, t_):
    best = None; mids = [v for v in range(nv) if v not in (s_, t_)]
    allcuts = []
    for r in range(len(mids) + 1):
        for sub in itertools.combinations(mids, r):
            S_ = set(sub) | {s_}
            c_ = sum((cv for (u, v), cv in cap.items() if u in S_ and v not in S_), Fr(0))
            allcuts.append(c_)
            best = c_ if best is None or c_ < best else best
    return best, allcuts
mf_ok = True
for _ in range(40):
    cap = {}
    for u in range(7):
        for v in range(7):
            if u != v and RNG.random() < 0.4:
                cap[(u, v)] = Fr(RNG.randint(1, 20), RNG.randint(1, 4))
    f_ = maxflow(7, cap, 0, 6)
    mc, allc = mincut(7, cap, 0, 6)
    mf_ok &= (f_ == mc) and all(c_ >= f_ for c_ in allc)
check("K4a [exact] max flow = min cut on 40 random rational networks; every cut >= flow", mf_ok)

had_ok, eq_ok = True, True
kp = 4
for trial in range(20):
    g = [Fr(RNG.randint(1, 9), 10) for _ in range(kp)]
    th = [Fr(RNG.randint(1, 8), 2) for _ in range(kp)]
    Am = sp.Matrix(kp, kp, lambda i, j: rq(-2, 2, 2))
    SX = Am * Am.T + sp.eye(kp) / 10
    if trial % 5 == 0:
        SX = sp.diag(*[SX[i, i] for i in range(kp)])
    Gd = sp.diag(*[sp.Rational(x.numerator, x.denominator) for x in g])
    SN = sp.diag(*[sp.Rational(th[i].numerator, th[i].denominator) * (1 - sp.Rational(g[i].numerator, g[i].denominator)**2)
                   for i in range(kp)])
    SY = Gd * SX * Gd + SN
    lhs = SY.det() / SN.det()
    rhs = sp.prod([SY[i, i] / SN[i, i] for i in range(kp)])
    had_ok &= (lhs <= rhs)
    if trial % 5 == 0:
        eq_ok &= (lhs == rhs)
Wm = sp.Matrix([[sp.Rational(1, 2), sp.Rational(-1, 4)], [sp.Rational(-1, 4), sp.Rational(1, 2)]])
SNc = 2 * (sp.eye(2) - Wm); eps_ = sp.Rational(1, 10)
SYc = SNc + eps_ * Wm
joint = SYc.det() / SNc.det(); perport = sp.prod([SYc[i, i] / SNc[i, i] for i in range(2)])
check("K4b [exact] independent ports: I(X;Y) <= sum_e I(X_e;Y_e) (Hadamard), equality for diagonal inputs; "
      "correlated hidden ports break per-port additivity", had_ok and eq_ok and joint > perport,
      f"Hadamard={had_ok}, equality={eq_ok}, correlated-noise control: joint ratio {joint} > per-port {perport}")

xx = sp.symbols('x', nonnegative=True)
ln_ok = sp.simplify(sp.diff(xx - sp.log(1 + xx), xx) - xx / (1 + xx)) == 0
Tt = sp.symbols('T', positive=True); uu = sp.symbols('u', positive=True); nn_ = sp.symbols('n', integer=True, positive=True)
# substitute omega = T u; expand 1/(e^u - 1) = sum e^{-nu} and -ln(1 - e^{-u}) = sum e^{-nu}/n (monotone convergence)
I1 = sp.summation(sp.integrate(uu * sp.exp(-nn_ * uu), (uu, 0, sp.oo)), (nn_, 1, sp.oo))        # int u/(e^u-1) du
I2 = sp.summation(sp.integrate(sp.exp(-nn_ * uu) / nn_, (uu, 0, sp.oo)), (nn_, 1, sp.oo))       # int -ln(1-e^{-u}) du
P_int = Tt**2 * I1 / (2 * sp.pi)
S_int = Tt * (I1 + I2) / (2 * sp.pi)
mp.mp.dps = 30
I2_num = mp.quad(lambda u_: -mp.log(1 - mp.exp(-u_)), [0, 1, mp.inf])
pend = sp.simplify(P_int - sp.pi * Tt**2 / 12) == 0 and sp.simplify(S_int - sp.pi * Tt / 6) == 0 and \
    sp.simplify(S_int**2 - sp.pi * P_int / 3) == 0 and abs(I2_num - mp.pi**2 / 6) < mp.mpf('1e-25')
check("K4c [exact] ln(1+x) <= x (energy-per-bit form); Pendry-Bekenstein: P = pi T^2/12, S_dot = pi T/6, "
      "S_dot^2 = pi P/3", ln_ok and pend, f"P={sp.simplify(P_int)}, S_dot={sp.simplify(S_int)}, quad witness "
      f"|I2 - pi^2/6|={mp.nstr(abs(I2_num - mp.pi**2 / 6), 3)}")

# butterfly: 0=S, 1=A, 2=B, 3=C, 4=D, 5=T1, 6=T2
bf = {(0, 1): Fr(1), (0, 2): Fr(1), (1, 3): Fr(1), (2, 3): Fr(1), (3, 4): Fr(1), (1, 5): Fr(1), (2, 6): Fr(1),
      (4, 5): Fr(1), (4, 6): Fr(1)}
mc1, mc2 = maxflow(7, bf, 0, 5), maxflow(7, bf, 0, 6)
xor_ok = True
for x1, x2 in itertools.product((0, 1), repeat=2):
    c_ = x1 ^ x2
    t1 = (x1, x1 ^ c_); t2 = (x2 ^ c_, x2)
    xor_ok &= (t1 == (x1, x2)) and (t2 == (x1, x2))
route_fail = True
for choice in ('x1', 'x2'):
    t1_bits = {'x1'} | {choice}; t2_bits = {'x2'} | {choice}
    route_fail &= not (t1_bits == {'x1', 'x2'} and t2_bits == {'x1', 'x2'})
check("K4d [exact] butterfly: min cut 2 to each sink; XOR coding delivers both bits; pure forwarding cannot",
      mc1 == 2 and mc2 == 2 and xor_ok and route_fail, f"min cuts=({mc1},{mc2}), XOR={xor_ok}, routing fails={route_fail}")


# =========================================================================== K5 arrow on the cycle space
print("== K5 arrow = cycle space (H5) ==")
def markov(n, edges, rates):
    Q = sp.zeros(n, n)
    for (i, j), (kij, kji) in zip(edges, rates):
        Q[i, j] += kij; Q[j, i] += kji
    for i in range(n):
        Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
    ns_ = Q.T.nullspace()
    pi_ = ns_[0] / sum(ns_[0])
    J = sp.Matrix([pi_[i] * kij - pi_[j] * kji for (i, j), (kij, kji) in zip(edges, rates)])
    return pi_, J
def fundamental_cycles(n, edges):
    adj = {v: [] for v in range(n)}
    for e, (i, j) in enumerate(edges):
        adj[i].append((j, e)); adj[j].append((i, e))
    par = {0: (None, None)}; order = [0]
    for u in order:
        for v, e in adj[u]:
            if v not in par:
                par[v] = (u, e); order.append(v)
    tree = {par[v][1] for v in par if par[v][1] is not None}
    def path_to_root(v):
        p_ = []
        while par[v][0] is not None:
            u, e = par[v]; p_.append((u, v, e)); v = u
        return p_
    cyc = []
    for f, (i, j) in enumerate(edges):
        if f in tree: continue
        z = [0] * len(edges); z[f] = 1
        for (u, v, e) in path_to_root(j):          # walk j -> root: traverse edge from v to u
            z[e] += 1 if edges[e] == (v, u) else -1
        for (u, v, e) in path_to_root(i):          # walk root -> i: traverse edge from u to v
            z[e] += 1 if edges[e] == (u, v) else -1
        cyc.append((f, sp.Matrix(z)))
    return cyc
k5a_ok = True
for _ in range(10):
    n = RNG.randint(5, 7)
    edges = random_connected_graph(n, RNG.randint(1, 4))
    rates = [(rq(1, 3), rq(1, 3)) for _ in edges]
    pi_, J = markov(n, edges, rates)
    d0 = incidence(n, edges)
    b1 = len(edges) - n + 1
    cyc = fundamental_cycles(n, edges)
    recon = sum((J[f] * z for f, z in cyc), sp.zeros(len(edges), 1))
    zs_ok = all(d0.T * z == sp.zeros(n, 1) for _, z in cyc) and \
        (sp.Matrix.hstack(*[z for _, z in cyc]).rank() == b1 if cyc else b1 == 0)
    k5a_ok &= (d0.T * J == sp.zeros(n, 1)) and (len(edges) - d0.rank() == b1) and (len(cyc) == b1) and zs_ok and recon == J
check("K5a [exact] stationary currents: d0^T J = 0; dim ker d0^T = |E|-|V|+1 = b1; J = sum_f J_f z_f", k5a_ok)
k5b_ok = True
for _ in range(20):
    n = RNG.randint(4, 8)
    edges = random_connected_graph(n, 0)
    rates = [(rq(1, 3), rq(1, 3)) for _ in edges]
    _, J = markov(n, edges, rates)
    k5b_ok &= (J == sp.zeros(len(edges), 1))
check("K5b [exact] trees carry no stationary current (detailed balance automatic)", k5b_ok)
n = 6
edges = random_connected_graph(n, 3)
a_pot = [rq(1, 3) for _ in range(n)]
sym = [rq(1, 2) for _ in edges]
rates_db = [(sym[e] * a_pot[j], sym[e] * a_pot[i]) for e, (i, j) in enumerate(edges)]
pi_db, J_db = markov(n, edges, rates_db)
cyc = fundamental_cycles(n, edges)
f0 = cyc[0][0]
rates_nd = list(rates_db); rates_nd[f0] = (rates_db[f0][0] * 2, rates_db[f0][1])
pi_nd, J_nd = markov(n, edges, rates_nd)
sig_edge = sum(J_nd[e] * sp.log(pi_nd[i] * rates_nd[e][0] / (pi_nd[j] * rates_nd[e][1])) for e, (i, j) in enumerate(edges))
sig_cyc = sum(J_nd[f] * sum(z[e] * sp.log(rates_nd[e][0] / rates_nd[e][1]) for e in range(len(edges)) if z[e] != 0)
              for f, z in cyc)
diff_sig = sp.simplify(sp.expand_log(sig_edge - sig_cyc, force=True))
check("K5c [exact] Kolmogorov rates: J = 0; perturbed: J != 0; sigma(edges, with pi) = sigma(cycle affinities); sigma>0",
      J_db == sp.zeros(len(edges), 1) and J_nd != sp.zeros(len(edges), 1) and diff_sig == 0 and sp.N(sig_cyc) > 0,
      f"sigma = {sp.N(sig_cyc, 8)}, difference = {diff_sig}")

mp.mp.dps = 30
xg = sp.symbols('x')
golden_ok = sp.simplify(sp.sin(2 * xg) / sp.sin(xg) - 2 * sp.cos(xg)) == 0 and \
    sp.simplify(2 * sp.cos(sp.pi / 5) - (1 + sp.sqrt(5)) / 2) == 0
w1, w2 = 2 * mp.sin(mp.pi / 5), 2 * mp.sin(2 * mp.pi / 5)
def G0(t_): return (1 + 2 * mp.cos(w1 * t_) + 2 * mp.cos(w2 * t_)) / 5
fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
fib_t = [2 * mp.pi * F / w1 for F in fibs if 2 * mp.pi * F / w1 <= 2000]
best_fib = max((G0(t_), t_) for t_ in fib_t)
grid_best = max(G0(mp.mpf(i) / 4) for i in range(4, 8001))
gam5 = mp.mpf('0.05')
def G0_lossy(t_):
    out = mp.mpf(1) / 5
    for wk, mult in ((w1, 2), (w2, 2)):
        wd = mp.sqrt(wk**2 - gam5**2 / 4)
        out += mult * mp.exp(-gam5 * t_ / 2) * (mp.cos(wd * t_) + gam5 / (2 * wd) * mp.sin(wd * t_)) / 5
    return out
lossy_dev = max(abs(G0_lossy(mp.mpf(t_)) - mp.mpf(1) / 5) for t_ in range(400, 2001, 7))
check("K5d [witness] LC 5-ring: frequency ratio = golden; near-perfect echo at Fibonacci times; lossy ring forgets "
      "all but the conserved charge 1/5", golden_ok and best_fib[0] >= 0.95 and lossy_dev <= 0.01,
      f"golden={golden_ok}, best echo {mp.nstr(best_fib[0], 6)} at t={mp.nstr(best_fib[1], 6)} "
      f"(grid max {mp.nstr(grid_best, 6)}), lossy max dev={mp.nstr(lossy_dev, 3)}")


# =========================================================================== K6 which network
print("== K6 which network (H6) ==")
k1, k2, k3, ell, Om, eps = sp.symbols('k1 k2 k3 ell Omega epsilon', positive=True)
kv = sp.Matrix([k1, k2, k3])
tet = [sp.Matrix(v_) * ell / sp.sqrt(3) for v_ in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
xs_ = [eps * (kv.T * d_)[0] for d_ in tet]
w2_shell = sp.expand(Om**2 * sum(x_**2 / 2 - x_**4 / 24 + x_**6 / 720 for x_ in xs_))
c2_ = sp.Rational(2, 3) * Om**2 * ell**2
ksq = k1**2 + k2**2 + k3**2
Pq = k1**2 * k2**2 + k1**2 * k3**2 + k2**2 * k3**2
coef2 = w2_shell.coeff(eps, 2); coef4 = w2_shell.coeff(eps, 4)
c2_ok = sp.simplify(coef2 - c2_ * ksq) == 0
iso_claim = sp.simplify(coef4 + c2_ * ell**2 * ksq**2 / 36) == 0
check("K6 [exact] (as handed over) tetrahedral shell: omega^2 = c^2 k^2 (1 - l^2 k^2/36 + ...) ISOTROPIC, eta = 1/72",
      c2_ok and iso_claim, f"c^2 isotropic={c2_ok}, isotropic k^4 term={iso_claim}; k^4 term = {sp.factor(coef4)}")
pred4 = -c2_ * ell**2 / 36 * (ksq**2 + 4 * Pq)
k4_ok = sp.simplify(coef4 - pred4) == 0
def dir_coef(nv_):
    sub = {k1: nv_[0], k2: nv_[1], k3: nv_[2]}
    return sp.simplify(-coef4.subs(sub) / (c2_ * ell**2 * (ksq**2).subs(sub)))
dirs = {'100': (1, 0, 0), '110': (1, 1, 0), '111': (1, 1, 1)}
dc = {kk_: dir_coef(v_) for kk_, v_ in dirs.items()}
ratio = sp.simplify(dc['111'] / dc['100'])
re_f = sum(1 - x_**2 / 2 + x_**4 / 24 - x_**6 / 720 for x_ in xs_)
im_f = sum(x_ - x_**3 / 6 + x_**5 / 120 for x_ in xs_)
a_ = sp.expand(4 - re_f); b_ = sp.expand(im_f)
w2_ac = sp.expand(Om**2 * (a_ - b_**2 / 8))
diff6 = sp.expand((w2_ac - w2_shell).coeff(eps, 6))
diff_low = [sp.expand((w2_ac - w2_shell).coeff(eps, p_)) for p_ in (2, 4)]
pred6 = -sp.Rational(2, 27) * Om**2 * ell**6 * (k1 * k2 * k3)**2
mp.mp.dps = 60
tet_mp = [[mp.mpf(sg) / mp.sqrt(3) for sg in v_] for v_ in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
kdir = (mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('0.8'))
ratios_num = []
for sc_ in (mp.mpf('1e-2'), mp.mpf('5e-3')):
    kk3 = [sc_ * x for x in kdir]
    xs_mp = [mp.fsum(kk3[i] * tv[i] for i in range(3)) for tv in tet_mp]
    a_mp = mp.fsum(x**2 / 2 - x**4 / 24 + x**6 / 720 for x in xs_mp)
    b_mp = mp.fsum(x - x**3 / 6 + x**5 / 120 for x in xs_mp)
    exact_ac = 4 - abs(mp.fsum(mp.expj(x) for x in xs_mp))
    ratios_num.append(abs(exact_ac - (a_mp - b_mp**2 / 8)))
order8 = ratios_num[0] / ratios_num[1] if ratios_num[1] > 0 else mp.inf
k6p = (c2_ok and k4_ok and dc['100'] == sp.Rational(1, 36) and dc['110'] == sp.Rational(1, 18) and
       dc['111'] == sp.Rational(7, 108) and ratio == sp.Rational(7, 3) and all(d_ == 0 for d_ in diff_low) and
       sp.simplify(diff6 - pred6) == 0)
check("K6' [exact] (hand prediction) k^4 term = -(c^2 l^2/36)(k^4 + 4P): 1/36 <100>, 1/18 <110>, 7/108 <111> "
      "(ratio 7/3); diamond acoustic = shell through O(k^4), differs at O(k^6) by -(2/27) Omega^2 l^6 (k1k2k3)^2", k6p,
      f"dir coefs={dc}, ratio={ratio}, k^6 diff={sp.factor(diff6)}, numeric truncation-error ratio (k halved)="
      f"{mp.nstr(order8, 4)} (expect ~2^8=256 if float exact; witness only)")

S3 = sum((d_ * d_.T for d_ in tet), sp.zeros(3, 3))
Gram = sp.Matrix(4, 4, lambda i, j: (tet[i].T * tet[j])[0])
k6b = (sum(tet, sp.zeros(3, 1)) == sp.zeros(3, 1) and sp.simplify(S3 - sp.Rational(4, 3) * ell**2 * sp.eye(3)) == sp.zeros(3, 3)
       and sp.simplify(Gram - ell**2 / 3 * (4 * sp.eye(4) - sp.ones(4, 4))) == sp.zeros(4, 4))
check("K6b [exact] tetrahedral star: sum = 0, second moment (4l^2/3) I (isotropic c), Gram = (l^2/3)(4I - J) = "
      "frame metric", k6b)

phi_ = (1 + sp.sqrt(5)) / 2
shells = {
    'sc': [v_ for v_ in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in v_) == 1],
    'bcc': list(itertools.product((-1, 1), repeat=3)),
    'fcc': [v_ for v_ in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in v_) == 2],
    'tet': [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],
    'ico': [p_ for a1 in (-1, 1) for a2 in (-1, 1) for p_ in ((0, a1, a2 * phi_), (a1, a2 * phi_, 0), (a2 * phi_, 0, a1))],
}
def m4ratio(vecs, dvec):
    dv = sp.Matrix(dvec); x2 = sum(((sp.Matrix(v_).T * dv)[0])**2 for v_ in vecs)
    x4 = sum(((sp.Matrix(v_).T * dv)[0])**4 for v_ in vecs)
    return sp.radsimp(sp.simplify(x4 / x2**2))
aniso = {}
for nm, vecs in shells.items():
    r100 = sp.simplify(m4ratio(vecs, (1, 0, 0))); r111 = sp.simplify(m4ratio(vecs, (1, 1, 1)))
    aniso[nm] = (r100, r111, sp.simplify(r100 - r111) == 0)
k6c = all(not aniso[nm][2] for nm in ('sc', 'bcc', 'fcc', 'tet')) and aniso['ico'][2] and len(shells['ico']) == 12
check("K6c [exact] fourth-moment anisotropy: sc, bcc, fcc, tetrahedral shells anisotropic; icosahedral 12-star "
      "isotropic", k6c, "; ".join(f"{nm}: <100> {a_[0]}, <111> {a_[1]}" for nm, a_ in aniso.items()))

def rank_exact(rows, ncol):
    Mx = [list(map(Fr, r)) for r in rows]
    rk = 0; col = 0
    nr = len(Mx)
    while rk < nr and col < ncol:
        piv = next((r for r in range(rk, nr) if Mx[r][col] != 0), None)
        if piv is None:
            col += 1; continue
        Mx[rk], Mx[piv] = Mx[piv], Mx[rk]
        pv = Mx[rk][col]
        for r in range(rk + 1, nr):
            if Mx[r][col] != 0:
                f_ = Mx[r][col] / pv
                Mx[r] = [a - f_ * b for a, b in zip(Mx[r], Mx[rk])]
        rk += 1; col += 1
    return rk
def rigidity_rank(positions, bonds):
    idx_ = {p_: i for i, p_ in enumerate(positions)}
    rows = []
    for (p_, dvec) in bonds:
        row = [0] * (3 * len(positions))
        i = idx_[p_]; j = idx_[tuple(dvec[1])]
        for a in range(3):
            row[3 * i + a] -= dvec[0][a]; row[3 * j + a] += dvec[0][a]
        rows.append(row)
    return rank_exact(rows, 3 * len(positions)), len(rows), 3 * len(positions)
# diamond 2x2x2 conventional cells, side 8
sd = 8
dpos = []
for cx in range(2):
    for cy in range(2):
        for cz in range(2):
            for b in base:
                pa = (4 * cx + b[0], 4 * cy + b[1], 4 * cz + b[2])
                dpos.append(pa); dpos.append(((pa[0] + 1) % sd, (pa[1] + 1) % sd, (pa[2] + 1) % sd))
dbonds = []
for i, p_ in enumerate(dpos):
    if i % 2 == 0:
        for d_ in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)):
            q_ = ((p_[0] + d_[0]) % sd, (p_[1] + d_[1]) % sd, (p_[2] + d_[2]) % sd)
            dbonds.append((p_, (d_, q_)))
rk_d, nb_d, nd_d = rigidity_rank(dpos, dbonds)
# sc 4^3
ss = 4
scpos = [(x, y, z) for x in range(ss) for y in range(ss) for z in range(ss)]
scb = [(p_, (d_, ((p_[0] + d_[0]) % ss, (p_[1] + d_[1]) % ss, (p_[2] + d_[2]) % ss)))
       for p_ in scpos for d_ in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
rk_s, nb_s, nd_s = rigidity_rank(scpos, scb)
# fcc 2x2x2 conventional cells: integer points mod 4 with even coordinate sum
sf = 4
fpos = [(x, y, z) for x in range(sf) for y in range(sf) for z in range(sf) if (x + y + z) % 2 == 0]
half = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
fb = [(p_, (d_, ((p_[0] + d_[0]) % sf, (p_[1] + d_[1]) % sf, (p_[2] + d_[2]) % sf))) for p_ in fpos for d_ in half]
rk_f, nb_f, nd_f = rigidity_rank(fpos, fb)
k6d = rk_d <= 128 and rk_d < nd_d - 3 and rk_s == 144 and rk_f == nd_f - 3
check("K6d [exact] Maxwell: diamond floppy (rank << 3n-3), sc floppy (z=6 necessary, not sufficient), fcc rigid",
      k6d, f"diamond rank {rk_d}/{nd_d - 3} ({nb_d} bonds), sc rank {rk_s}/{nd_s - 3}, fcc rank {rk_f}/{nd_f - 3}")

def perm_sign(seq):
    seq = list(seq); sgn = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]: sgn = -sgn
    return sgn
def B3_matrix(oriented_tets):
    faces = {}
    rows = []
    for sgn, tv in oriented_tets:
        row = {}
        for i in range(4):
            fv = tv[:i] + tv[i + 1:]
            key = tuple(sorted(fv))
            ssign = sgn * (-1)**i * perm_sign([sorted(fv).index(x) for x in fv])
            if key not in faces: faces[key] = len(faces)
            row[faces[key]] = row.get(faces[key], 0) + ssign
        rows.append(row)
    Bm = np.zeros((len(rows), len(faces)), dtype=np.int64)
    for r, row in enumerate(rows):
        for c_, v_ in row.items(): Bm[r, c_] = v_
    return Bm
tets5 = []
for i in range(5):
    tv = tuple(x for x in range(5) if x != i)
    tets5.append(((-1)**i, tv))
B5 = B3_matrix(tets5)
L5 = B5 @ B5.T
ok5 = np.array_equal(L5, 5 * np.eye(5, dtype=np.int64) - np.ones((5, 5), dtype=np.int64))
nk = 3
def vid(x, y, z): return ((x % nk) * nk + (y % nk)) * nk + (z % nk)
tets_k = []
for x in range(nk):
    for y in range(nk):
        for z in range(nk):
            for sig_ in itertools.permutations(range(3)):
                p_ = [x, y, z]; vs = [vid(*p_)]
                for ax in sig_:
                    p_[ax] += 1; vs.append(vid(*p_))
                tets_k.append((perm_sign(sig_), tuple(vs)))
Bk = B3_matrix(tets_k)
Lk = Bk @ Bk.T
deg_ok = np.all(np.diag(Lk) == 4)
off = Lk - np.diag(np.diag(Lk))
off_ok = set(np.unique(off).tolist()) <= {0, -1} and np.all(off.sum(axis=1) == -4)
two_ok = np.all(np.abs(Bk).sum(axis=0) == 2)
check("K6e [exact] closed tetrahedral complexes: boundary of 4-simplex B3B3^T = 5I - J; Kuhn 3-torus B3B3^T = "
      "4I - A (4-regular dual graph Laplacian); each triangle in exactly two tetrahedra",
      ok5 and deg_ok and off_ok and two_ok, f"d4-boundary={ok5}, torus tets={len(tets_k)}, faces={Bk.shape[1]}, "
      f"diag 4={deg_ok}, off-diag in {{0,-1}} & row sum -4={off_ok}, two per face={two_ok}")


# =========================================================================== K7 gauge (fenced)
print("== K7 gauge (H7, fenced) ==")
n = 6
edges = random_connected_graph(n, 3)
d0 = incidence(n, edges)
Acon = sp.Matrix([rq(-3, 3) for _ in edges]); chi = sp.Matrix([rq(-3, 3) for _ in range(n)])
cyc = fundamental_cycles(n, edges)
hol = [(z.T * Acon)[0] for _, z in cyc]; hol2 = [(z.T * (Acon + d0 * chi))[0] for _, z in cyc]
ann_edges = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (0, 3), (1, 4), (2, 5), (0, 4), (1, 5), (2, 3)]
ann_tris = [(0, 1, 4), (0, 3, 4), (1, 2, 5), (1, 4, 5), (0, 2, 3), (2, 3, 5)]
eidx = {e: i for i, e in enumerate(ann_edges)}
def ed(u, v):
    return (eidx[(u, v)], 1) if (u, v) in eidx else (eidx[(v, u)], -1)
d1 = sp.zeros(len(ann_tris), len(ann_edges))
for r, (a, b, c) in enumerate(ann_tris):
    for (u, v) in ((a, b), (b, c), (c, a)):
        e, sg = ed(u, v); d1[r, e] += sg
d0a = incidence(6, ann_edges)
inner = sp.zeros(1, len(ann_edges))
for (u, v) in ((0, 1), (1, 2), (2, 0)):
    e, sg = ed(u, v); inner[0, e] += sg
Avar = sp.Matrix(sp.symbols('a0:%d' % len(ann_edges)))
solA = sp.solve(list(d1 * Avar) + [(inner * Avar)[0] - 1], list(Avar), dict=True)
Aflat = Avar.subs(solA[0]).subs({v_: 0 for v_ in Avar})
flat_ok = d1 * Aflat == sp.zeros(len(ann_tris), 1) and (inner * Aflat)[0] == 1
not_exact = sp.Matrix.hstack(d0a, Aflat).rank() > d0a.rank()
b1_ann = len(ann_edges) - d0a.rank() - d1.rank()
check("K7 [exact, fenced] cycle holonomies gauge-invariant, count b1; annulus (b1=1): flat connection with holonomy 1, "
      "not exact", hol == hol2 and len(hol) == len(edges) - n + 1 and flat_ok and not_exact and b1_ann == 1,
      f"holonomies invariant={hol == hol2}, count={len(hol)}, annulus b1={b1_ann}, flat={flat_ok}, non-exact={not_exact}")


# =========================================================================== summary (pre-registered)
print()
n_pre = len(res)
print(f"TOTAL (pre-registered): {sum(res)}/{n_pre} PASS")


# =========================================================================== POST-DIAGNOSIS (NOT BLIND)
print()
print("== POST-DIAGNOSIS checks (NOT BLIND; criteria fixed in the RUN LOG before run 2) ==")
# K1a' masking witness
n, edges, ports = nets[0]
alone = signature(sp.Matrix([[1, 0], [0, -3]]))[2] > 0
masked_pass = True
for s_pt in S_PTS:
    X, Y = assemble_two_ports(n, edges, bad_ports, s_pt)
    masked_pass &= herm_psd_realified(realify(X, Y))
strong_ports = list(ports); strong_ports[0] = (sp.Matrix([[1, 0], [0, -100]]), C0, Gm0)
strong_flag = 0
for s_pt in S_PTS:
    X, Y = assemble_two_ports(n, edges, strong_ports, s_pt)
    if not herm_psd_realified(realify(X, Y)):
        strong_flag += 1
check("K1a' [exact, NOT BLIND] masking: an active two-port (alone non-passive) inside a passive network leaves the "
      "composite passive; a strong active element is flagged", alone and masked_pass and strong_flag >= 1,
      f"element alone active={alone}, composite passive at 5/5={masked_pass}, strong control flagged {strong_flag}/5")

# K2d' Debye ratio without window
mp.mp.dps = 50
al = mp.acosh(mp.mpf('1.2')); th_ = mp.tanh(al); p_ = 1 / th_
u1 = (3 * p_ - 5 * p_**3) / 24
devs, corr_ok = [], True
for T in (100, 200, 400, 800):
    nu = 2 * (6 * T // 5)
    deb = mp.exp(nu * (th_ - al)) / mp.sqrt(2 * mp.pi * nu * th_)
    ratio = mp.besselj(nu, 2 * T) / deb
    devs.append(abs(ratio - 1))
    corr_ok &= abs(ratio - 1 - u1 / nu) < mp.mpf(10) / nu**2
check("K2d' [50-digit, NOT BLIND] at n = 1.2t the LC response is the Debye front: |ratio-1| decreasing, < 0.01 at "
      "t=800, first correction u1/nu", all(devs[i + 1] < devs[i] for i in range(3)) and devs[-1] < 0.01 and corr_ok,
      f"|ratio-1| = {[mp.nstr(d_, 4) for d_ in devs]}, first-correction residual within 10/nu^2: {corr_ok}")

# K3d' all-to-all closed form
def s_nu(nu):
    return (nu + 0.5) * math.log(nu + 0.5) - ((nu - 0.5) * math.log(nu - 0.5) if nu - 0.5 > 1e-14 else 0.0)
lam1, lam2 = MSQ, 1 + MSQ
gx = lambda lam: 1 / math.tanh(BETA * math.sqrt(lam) / 2) / (2 * math.sqrt(lam))
hp = lambda lam: math.sqrt(lam) / math.tanh(BETA * math.sqrt(lam) / 2) / 2
def nu_f(f):
    return math.sqrt((gx(lam2) + (gx(lam1) - gx(lam2)) * f) * (hp(lam2) + (hp(lam1) - hp(lam2)) * f))
mf = []
for Aids in sq_blocks:
    f = len(Aids) / N576
    mf.append(s_nu(nu_f(f)) + s_nu(nu_f(1 - f)) - s_nu(math.sqrt(gx(lam1) * hp(lam1))) - s_nu(math.sqrt(gx(lam2) * hp(lam2))))
mf = np.array(mf)
rel_mf = float(np.max(np.abs(Ia - mf) / np.abs(mf)))
wcut = cuta / N576
geo_growth_c2 = (Ia[-1] / geo[-1]) / (Ia[0] / geo[0])
band_c2 = (Ia / wcut).max() / (Ia / wcut).min()
check("K3d' [numerics, NOT BLIND] all-to-all: MI = mean-field closed form; geometric area law violated; cut law "
      "holds (band); I <= 1 nat", rel_mf < 1e-8 and geo_growth_c2 >= 2.0 and band_c2 <= 2.0 and Ia.max() <= 1.0,
      f"max rel dev from closed form={rel_mf:.2e}, I/|dA|_geo growth={geo_growth_c2:.2f}, I/weighted-cut band={band_c2:.3f}")

print()
print(f"TOTAL (post-diagnosis, NOT BLIND): {sum(res[n_pre:])}/{len(res) - n_pre} PASS")
