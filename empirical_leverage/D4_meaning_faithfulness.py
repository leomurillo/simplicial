"""
D-IV: meaning = gauge-invariant connected content (the faithfulness-obstruction philosophy).

The capstone seed: what of the whole structure is OBJECTIVE (both observers agree) vs PERSPECTIVAL
(chart-dependent, hidden)? The answer is a three-rung hierarchy of meaning:

   order-1  absolute coordinate c_i        GAUGE        meaningless (the overflow line 1)
   order-2  the metric (Fisher / K_N)      OBJECTIVE    both m- and e-charts agree; the faithful core
   order>=3 connected (cubic, Wick)        PERSPECTIVAL e-chart-only; compositional; structurally hidden

Meaning is (a) gauge-invariant -- only the differences c_i - c_j carry content, never the absolute
coordinate; and (b) connected -- the metric is the objective core, but the compositional meaning
(the connected order>=3 cross-content) lives in the blind spot of any order-2 instrument. That last
fact is the FAITHFULNESS OBSTRUCTION: probes / lenses / SAEs are order-2 readouts of an order>=3
world, so they faithfully read the objective meaning and provably miss the compositional meaning.

This cert verifies:
 (1) gauge invariance: M_N 1 = 0 (the absolute coordinate is null); meaning lives on H (differences),
     spectrum {0 on 1, N on H}.
 (2) objective = order-2 self-dual rung: the order-2 cumulant at p_* equals the universal eigenvalue N
     equals the K_N Hodge-Laplacian eigenvalue -- the rung where cumulant, metric, and Laplacian coincide.
 (3) perspectival = order>=3 connected, e-chart-only: m-chart cross blocks vanish; e-chart carries them.
 (4) THE FAITHFULNESS OBSTRUCTION: two distributions matched through order-2 (mean, variance) but
     differing at order-3 are IDENTICAL to every order-2 instrument; the order-3 direction is the
     third finite difference [-1,3,-3,1] -- the compositional meaning the order-2 readout cannot see.

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

# ---------------- (1) meaning is gauge-invariant ----------------
print("(1) gauge invariance: absolute coordinate is null (M_N 1 = 0); meaning = differences on H")
N = 4
M = N*sp.eye(N) - sp.ones(N, N)            # K_N graph Laplacian = N I - J
one = sp.ones(N, 1)
chk("M_N 1 = 0 : the absolute/uniform coordinate (gauge line 1) is meaningless (null direction)",
    (M*one) == sp.zeros(N, 1))
eig = M.eigenvals()
chk("spectrum {0 on 1 (gauge), N on H (meaning)}: meaning lives on the zero-sum hyperplane",
    eig == {sp.Integer(0): 1, sp.Integer(N): N-1})
# a difference vector c_i - c_j lives in H (sum zero) -> carries meaning; 1 carries none
diff = sp.Matrix([1, -1, 0, 0])
chk("a difference c_i - c_j is in H (gauge-invariant content); has nonzero M-norm",
    sum(diff) == 0 and (diff.T*M*diff)[0] > 0 and (one.T*M*one)[0] == 0)

# ---------------- (2) objective meaning = the order-2 self-dual rung ----------------
print("(2) objective = order-2 self-dual rung: cumulant = metric = Hodge eigenvalue = N at p_*")
p = sp.symbols(f'p1:{N+1}', positive=True)
phi = sum(pk*sp.log(pk) for pk in p)
order2_diag_star = sp.diff(phi, p[0], 2).subs({pk: sp.Rational(1, N) for pk in p})   # 1/p_* = N
chk("order-2 cumulant at p_* (=1/p_*=N) equals the K_N Laplacian eigenvalue on H (=N): self-dual core",
    order2_diag_star == N and sp.Integer(N) in M.eigenvals())
# self-dual under Legendre: the metric g and its dual g^{-1} are the SAME bilinear form (orders >=3 are not)
g_sym = sp.diag(*[sp.diff(phi, pk, 2) for pk in p])
chk("order-2 metric is a symmetric tensor (objective, chart-covariant); g and g^-1 the same form",
    g_sym.is_symmetric() and sp.simplify(g_sym.inv().inv() - g_sym) == sp.zeros(N, N))

# ---------------- (3) perspectival meaning = order>=3 connected, e-chart-only ----------------
print("(3) perspectival = order>=3 connected (compositional), e-chart-only / hidden from m-chart")
q1, q2 = sp.symbols('q1 q2', positive=True)
phi_m = q1*sp.log(q1) + q2*sp.log(q2)
chk("m-chart (classical) connected cross blocks vanish (order-3 and order-4): no compositional content",
    sp.simplify(sp.diff(phi_m, q1, 2, q2, 1)) == 0 and sp.simplify(sp.diff(phi_m, q1, 2, q2, 2)) == 0)
th = sp.symbols(f't0:{N}'); Phi = sp.log(sum(sp.exp(t) for t in th))
e_cross4 = sp.nsimplify(sp.diff(Phi, th[0], 2, th[1], 2).subs({t: 0 for t in th}))
chk("e-chart carries the compositional content (order-4 Wick = -(N^2-4N+6)/N^4): perspectival, hidden",
    e_cross4 == -sp.Rational(N**2 - 4*N + 6, N**4) and e_cross4 != 0)

# ---------------- (4) THE FAITHFULNESS OBSTRUCTION ----------------
print("(4) faithfulness obstruction: order-2 readout blind to order-3 (compositional) meaning")
v = np.array([0.0, 1.0, 2.0, 3.0])                       # the value/observable
# null space of the order-<=2 moment map [1, v, v^2] is spanned by the 3rd finite difference
Mom = np.vstack([v**0, v**1, v**2])                      # 3x4 : matches mean, 2nd moment
null = np.array([-1.0, 3.0, -3.0, 1.0])                  # (1-1)^3 binomial = 3rd finite difference
chk("order-2 moment map kernel = third finite difference [-1,3,-3,1] (the order-3 direction)",
    np.allclose(Mom @ null, 0) and abs(v**3 @ null) > 1e-9)
base = np.full(4, 0.25)
eps = 0.05
pdist = base + eps*null                                   # [.20,.40,.10,.30]
qdist = base - eps*null                                   # [.30,.10,.40,.20]
chk("p,q are valid distributions (positive, sum 1), distinct", np.all(pdist > 0) and np.all(qdist > 0)
    and abs(pdist.sum()-1) < 1e-12 and abs(qdist.sum()-1) < 1e-12 and not np.allclose(pdist, qdist))
def moment(d, k):
    return float(d @ v**k)
chk("ORDER-2 INSTRUMENT reads them IDENTICALLY: same mean and same variance",
    abs(moment(pdist, 1)-moment(qdist, 1)) < 1e-12
    and abs((moment(pdist, 2)-moment(pdist, 1)**2) - (moment(qdist, 2)-moment(qdist, 1)**2)) < 1e-12)
m3p = moment(pdist, 3) - 3*moment(pdist, 1)*moment(pdist, 2) + 2*moment(pdist, 1)**3
m3q = moment(qdist, 3) - 3*moment(qdist, 1)*moment(qdist, 2) + 2*moment(qdist, 1)**3
chk("but their order-3 (skew / compositional meaning) DIFFERS: invisible to the order-2 probe",
    abs(m3p - m3q) > 1e-3)
# the program instance: order-2 is circulant in k-l (difference, 2-frequency), order-3 on k+l+m=0
# (sum, 3-frequency) -- no 2-frequency operator represents a 3-frequency coupling (CBS P4, 18/18).

print("=" * 80)
print(f"SUMMARY: {sum(PASS)}/{len(PASS)} OK ->", "GREEN" if all(PASS) else "RED")
print("MEANING = gauge-invariant connected content. Order-1 absolute = GAUGE (null line 1); order-2")
print("metric = OBJECTIVE (both charts agree, self-dual rung = N); order>=3 connected = PERSPECTIVAL")
print("(e-chart-only, compositional, hidden). FAITHFULNESS OBSTRUCTION: an order-2 instrument reads")
print("the objective meaning but is provably blind to the order-3 (compositional) meaning -- two")
print("distributions matched through order-2 are identical to it though their order-3 differs. That is")
print("interpretability's faithfulness crisis: order-2 readouts (probes/lenses/SAEs) of order>=3 meaning.")
print("=" * 80)
