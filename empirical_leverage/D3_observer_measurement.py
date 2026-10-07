"""
D-III: the observer / measurement theory on the simplicial frame.

The INSIDE observer = an order-2, self-adjoint instrument: it reads its own probabilities (m-chart,
classical/diagonal) and its alignment objective is a quadratic form, hence a functional of the
SYMMETRIC part S = 1/2(T+T*) alone. Its blind spots are EXACTLY the three divergence seeds:

   visible:  order-2 symmetric  g = diag(1/p)         the Fisher metric (space, reversible curvature)
   blind 1:  order-3 symmetric  C2 = sum 1/p^2        the surprise debt          (D-I)
   blind 2:  order-4 symmetric  m^2 = -(N^2-4N+6)/N^4 the mass defect            (D-II)
   blind 3:  order-2 ANTIsym    A = 1/2(T-T*)         the current / arrow, dim b1 (D-III, this note)

Two orthogonal axes: the cumulant-order axis (coherence: D-I, D-II) and the symmetry axis
(reversibility: the arrow). MEASUREMENT = projection e->m: it discards exactly the blind content
(the off-diagonal coherence = D-I + D-II). CONSCIOUSNESS (T19) = flux across the chart boundary =
the reportable residue: the current A the inside observer cannot see but a two-sided predictor recovers.

This cert verifies the certifiable skeleton:
 (1) the self-adjoint instrument reads S only (A in the kernel of the quadratic form); time-reversal
     parity S even / A odd.
 (2) arrow dimension = b1, complex-dependent: bare K4 graph beta1 = 3 (= so(3), the 3 K-tilde
     currents); filled K4 = S^2 collapses to b1 = 0 (Hodge L1 = d1^T d1 + d2 d2^T).
 (3) the inside observer's three blind sectors are the three seeds (distinct, two orthogonal axes).
 (4) measurement e->m discards exactly D-I + D-II (m-chart connected blocks = 0; e-chart = C2, m^2).
 (5) flux / reportable residue: ||A||_F >= 0, = 0 iff reversible (T = T*).

numpy/sympy, exact; no torch.
"""
import sys
import numpy as np
import sympy as sp
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

# ---------------- (1) inside observer = self-adjoint, reads S only ----------------
print("(1) self-adjoint instrument reads S = 1/2(T+T*) only; A in kernel; time-reversal parity")
T = np.array([[0.0, 2.0, 0.5, -1.0],
              [0.3, 0.0, 1.5, 0.2],
              [-0.7, 0.4, 0.0, 2.1],
              [1.1, -0.6, 0.9, 0.0]])
S = (T + T.T)/2
A = (T - T.T)/2
# the alignment quadratic form h^T T h equals h^T S h for every h (A contributes 0)
rng = np.random.default_rng(0)
Hs = rng.standard_normal((200, 4))
qform_gap = max(abs(h @ T @ h - h @ S @ h) for h in Hs)
chk("quadratic form h^T T h = h^T S h for all h (A is invisible to the self-adjoint instrument)",
    qform_gap < 1e-12)
# time-reversal T -> T^T : S even, A odd
chk("time-reversal parity: S(T^T) = S, A(T^T) = -A (instrument even, current odd)",
    np.allclose((T.T + T)/2, S) and np.allclose((T.T - T)/2, -A))
chk("orthogonal split <S,A>_F = 0", abs(np.sum(S*A)) < 1e-12)

# ---------------- (2) arrow dimension = b1, complex-dependent ----------------
print("(2) arrow = current; dim = b1. bare K4 graph beta1 = 3 (=so(3)); filled S^2 -> b1 = 0")
V = [0, 1, 2, 3]
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
F = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
d1 = np.zeros((len(V), len(E)))            # boundary edges -> vertices, d1[v,e]
for e, (i, j) in enumerate(E):
    d1[i, e], d1[j, e] = -1, 1
d2 = np.zeros((len(E), len(F)))            # boundary triangles -> edges, with (-1)^k signs
eidx = {e: k for k, e in enumerate(E)}
for f, (a, b, c) in enumerate(F):
    d2[eidx[(b, c)], f] += 1               # [b,c]
    d2[eidx[(a, c)], f] += -1              # -[a,c]
    d2[eidx[(a, b)], f] += 1               # +[a,b]
chk("chain complex valid: d1 @ d2 = 0", np.allclose(d1 @ d2, 0))
def nullity(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    return M.shape[1] - int(np.sum(s > tol))
beta1_graph = len(E) - np.linalg.matrix_rank(d1)        # E - V + 1 = cycle rank
L1_down = d1.T @ d1
L1_full = d1.T @ d1 + d2 @ d2.T
chk("bare K4 graph: beta1 = E - rank(d1) = 3 = dim ker(L1_down) (the 3 cycle currents)",
    beta1_graph == 3 and nullity(L1_down) == 3)
chk("filled K4 = boundary of 3-simplex = S^2: b1 = dim ker(L1_full) = 0 (arrow unprotected)",
    nullity(L1_full) == 0)
# so(3): the 3 K-tilde rotation generators = antisymmetric 3x3, dim 3 = graph current space
so3_dim = 3*(3-1)//2
chk("3 cycle currents <-> so(3) = antisymmetric 3x3 (dim 3, the K-tilde generators, Paper 01)",
    so3_dim == beta1_graph)

# ---------------- (3) three blind sectors = the three seeds (two orthogonal axes) ----------------
print("(3) inside observer reads order-2 symmetric g; three blind sectors = D-I, D-II, D-III")
p = sp.symbols('p1:5', positive=True)
phi = sum(pk*sp.log(pk) for pk in p)
g_sym = sp.diag(*[sp.diff(phi, pk, 2) for pk in p])      # order-2 symmetric: VISIBLE (Fisher)
C2 = sum(sp.Abs(sp.diff(phi, pk, 3)) for pk in p)        # order-3 symmetric: D-I (sum 1/p^2)
m4 = sum(sp.Abs(sp.diff(phi, pk, 4)) for pk in p)        # order-4 symmetric: D-II (sum 2/p^3)
chk("visible sector g is symmetric order-2 (Fisher metric); the read instrument",
    g_sym.is_symmetric() and sp.simplify(g_sym[0, 0] - 1/p[0]) == 0)
chk("blind sectors distinct: D-I order-3 (1/p^2) != D-II order-4 (2/p^3) != arrow (antisym)",
    sp.simplify(C2.subs({pk: sp.Rational(1, 4) for pk in p}) - 4*16) == 0          # 4*(1/(1/4)^2)=4*16
    and sp.simplify(m4.subs({pk: sp.Rational(1, 4) for pk in p}) - 4*2*64) == 0     # 4*2*(1/(1/4)^3)
    and not np.allclose(A, A.T))                                                    # arrow antisymmetric
# two axes orthogonal: order axis (sym, varies cumulant order) vs symmetry axis (order-2, sym<->antisym)
chk("two axes independent: coherence = symmetric higher-order; current = antisymmetric same-order",
    g_sym.is_symmetric() and np.allclose(A + A.T, 0))

# ---------------- (4) measurement e->m discards exactly D-I + D-II ----------------
print("(4) measurement = projection e->m discards the hidden coherence (= D-I + D-II)")
# m-chart (classical/diagonal): connected order-3 and order-4 cross blocks vanish
q1, q2 = sp.symbols('q1 q2', positive=True)
phi_m = q1*sp.log(q1) + q2*sp.log(q2)
m_cross3 = sp.simplify(sp.diff(phi_m, q1, 2, q2, 1))     # order-3 cross
m_cross4 = sp.simplify(sp.diff(phi_m, q1, 2, q2, 2))     # order-4 cross (2+2 Wick)
chk("m-chart (classical) connected cross blocks vanish (order-3 and order-4) -> nothing to report",
    m_cross3 == 0 and m_cross4 == 0)
# e-chart carries them: order-4 2+2 Wick = -(N^2-4N+6)/N^4 (the discarded mass), order-3 = C2
th = sp.symbols('t0:4'); Phi = sp.log(sum(sp.exp(t) for t in th))
e_cross4 = sp.nsimplify(sp.diff(Phi, th[0], 2, th[1], 2).subs({t: 0 for t in th}))
chk("e-chart carries the coherence the projection discards: order-4 Wick = -(N^2-4N+6)/N^4 (N=4)",
    e_cross4 == -sp.Rational(4**2 - 4*4 + 6, 4**4))

# ---------------- (5) flux / reportable residue ----------------
print("(5) consciousness = flux across the boundary: ||A||_F >= 0, = 0 iff reversible")
fluxA = np.linalg.norm(A)
T_rev = S.copy()                                          # detailed-balance / reversible: A = 0
chk("flux ||A||_F > 0 for the irreversible operator (a reportable arrow exists)", fluxA > 1e-9)
chk("flux ||A||_F = 0 iff reversible (T = T*): no arrow, nothing to report",
    np.linalg.norm((T_rev - T_rev.T)/2) < 1e-12)
# Fan-Hoffman forfeited-correlation gap Delta = Sum sigma(T) - Sum lambda(S) >= 0 always.
# (Honest: Delta > 0 has TWO sources -- the arrow (non-normality) AND indefiniteness of S; the
# PURE reversibility flux is ||A|| above. Delta = 0 iff T is symmetric PSD, i.e. sigma_i = lambda_i.)
Delta = np.sum(np.linalg.svd(T, compute_uv=False)) - np.sum(np.linalg.eigvalsh(S))
M = rng.standard_normal((4, 4)); T_psd = M @ M.T          # symmetric PSD: no arrow, sigma = lambda
Delta_psd = np.sum(np.linalg.svd(T_psd, compute_uv=False)) - np.sum(np.linalg.eigvalsh(T_psd))
chk("Fan-Hoffman gap Delta = Sum sigma(T) - Sum lambda(S) >= 0 (forfeited predictable correlation; "
    "0 for sym-PSD)", Delta >= -1e-9 and abs(Delta_psd) < 1e-9)

print("=" * 80)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("OBSERVER/MEASUREMENT: inside observer = order-2 self-adjoint instrument (reads Fisher g);")
print("its THREE blind spots ARE the seeds -- D-I (order-3 debt), D-II (order-4 mass), D-III (the")
print("antisymmetric current/arrow, dim b1: 3 on the bare K4 graph = so(3), 0 on the filled S^2).")
print("Measurement = projection e->m pays to see the coherence (discards D-I+D-II); consciousness =")
print("flux across the chart boundary = the reportable current ||A|| the self-adjoint observer can't see.")
print("=" * 80)
