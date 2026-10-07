"""
Port Principle — SPINE settlement: "one inequality (no port gives more than it takes)":
base = every input (contraction -> ledger), lifts = every instant (causality) and every copy
(temperature); see PortPrinciple.md §1.1 / Prop 3.1.  Exact arithmetic only
(Fractions, integer energies); no float enters any pass/fail decision.

PRE-REGISTERED FALSIFIERS (written before the run; both branches reportable)
S1  every-instant passivity => causality
    K1: every rational kernel with an anticausal entry admits an exact violating input
        u = e_i + lam e_j at truncation t = i (constructive).
    L1: some anticausal kernel passes truncated passivity at every t  -> spine (i) FALSE.
    K1b (expected): NET passivity (only t = n) does NOT force causality — a symmetric PSD
        kernel with anticausal entries is net-passive yet fails at some instant.
    L1b: net passivity already forces causality -> the 'every instant' clause is idle.
S2  every-input passivity (contraction) => finite lossless ledger up to a horizon (Egervary)
    K2: U ((N+1)d x (N+1)d, rational) is exactly orthogonal and P U^k P = T^k for 0<=k<=N.
    L2: either identity fails for some k<=N -> construction/spine (ii) wrong.
    K2b (expected): the identity FAILS at k = N+1 (finite ledger => finite horizon).
    L2b: it still holds at k = N+1 -> 'horizon is sharp' claim is wrong for this ledger.
S3  every-copy passivity => temperature (Pusz-Woronowicz / Lenard, finite form)
    K3: non-Gibbs passive p=(1/2,2/5,1/10), E=(0,1,2) first becomes ACTIVE at n* = 3 copies
        (predicted from (1,1,1)[E=3] vs (0,0,2)[E=2]); ergotropy exact rational > 0.
    L3: n* != 3.
    K3b (zeroth law): two individually Gibbs ports at DIFFERENT temperatures,
        A: E=(0,1), w=2^-E ; B: E=(0,2), w=2^(-E/2), are jointly passive at n=1 but
        jointly ACTIVE at n* = 3 (predicted: A:111,B:000 [E=3] vs A:000,B:110 [E=4]).
    L3b: equal-temperature joint (B: w=2^-E) becomes active for some n <= 5.
S4  Shannon + Nyquist => Landauer:  lim_{W->oo} E_b / N0 = ln 2  (sympy exact limit).
    K4: limit == ln 2.   L4: anything else.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

# deterministic rational generator (no RNG seeds)
def rat(a, b): return F(a, b)
def kernel(n, shift):
    return [[F(((3*i + 5*j + shift) % 11) - 5, 1 + (i*j + shift) % 4) for j in range(n)] for i in range(n)]

# ---------------------------------------------------------------- S1
print("== S1 every-instant passivity => causality ==")
n = 6
found_all = True
for shift in range(12):
    K = kernel(n, shift)
    anti = [(i, j) for i in range(n) for j in range(n) if j > i and K[i][j] != 0]
    for (i, j) in anti:
        lam = -(K[i][i] + 1) / K[i][j]
        u = [F(0)] * n; u[i] = F(1); u[j] = lam
        y = [sum(K[s][r] * u[r] for r in range(n)) for s in range(n)]
        val = sum(u[s] * y[s] for s in range(i + 1))   # energy absorbed up to instant t=i
        if val != -1: found_all = False
check("S1.K1 every anticausal entry -> exact violating input (absorbed energy = -1 at t=i)", found_all,
      "12 kernels, all anticausal entries")
# K1b: symmetric PSD kernel (net passive) with anticausal entries fails at an instant
Kp = [[F(2), F(1), F(0)], [F(1), F(2), F(1)], [F(0), F(1), F(2)]]   # PSD (eigs 2, 2+-sqrt2)
net_ok = all(sum(u[s] * sum(Kp[s][r] * u[r] for r in range(3)) for s in range(3)) >= 0
             for u in product([F(-2), F(-1), F(0), F(1), F(2)], repeat=3))
u = [F(1), F(-3), F(0)]
inst = u[0] * sum(Kp[0][r] * u[r] for r in range(3))                  # truncation t=0
check("S1.K1b net-passive (PSD) anticausal kernel still violates at an instant (precognition)",
      net_ok and inst < 0, f"net passive on grid={net_ok}; absorbed up to t=0: {inst}")

# ---------------------------------------------------------------- S2
print("== S2 contraction => finite lossless ledger with sharp horizon (Egervary) ==")
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(r) for r in zip(*A)]
def eye(d): return [[F(int(i == j)) for j in range(d)] for i in range(d)]
def cayley(S):  # rational orthogonal (I-S)(I+S)^-1 for skew S
    d = len(S); I = eye(d)
    M = sp.Matrix([[I[i][j] + S[i][j] for j in range(d)] for i in range(d)]).inv()
    Mi = [[F(int(sp.fraction(M[i, j])[0]), int(sp.fraction(M[i, j])[1])) for j in range(d)] for i in range(d)]
    return mm([[I[i][j] - S[i][j] for j in range(d)] for i in range(d)], Mi)
V = cayley([[F(0), F(1, 2), F(-1, 3)], [F(-1, 2), F(0), F(1, 4)], [F(1, 3), F(-1, 4), F(0)]])
W = cayley([[F(0), F(-2, 5), F(1, 7)], [F(2, 5), F(0), F(3, 8)], [F(-1, 7), F(-3, 8), F(0)]])
sig = [F(3, 5), F(5, 13), F(8, 17)]; dsg = [F(4, 5), F(12, 13), F(15, 17)]   # Pythagorean defects
diag = lambda v: [[v[i] if i == j else F(0) for j in range(3)] for i in range(3)]
T = mm(mm(V, diag(sig)), W)
DT = mm(mm(tr(W), diag(dsg)), W)        # (I - T^T T)^(1/2)
DTs = mm(mm(V, diag(dsg)), tr(V))       # (I - T T^T)^(1/2)
d, N = 3, 4
D = (N + 1) * d
U = [[F(0)] * D for _ in range(D)]
def put(bi, bj, B):
    for i in range(d):
        for j in range(d): U[bi * d + i][bj * d + j] = B[i][j]
put(0, 0, T); put(0, N, DTs); put(1, 0, DT); put(1, N, [[-x for x in r] for r in tr(T)])
for k in range(2, N + 1): put(k, k - 1, eye(d))
orth = mm(tr(U), U) == eye(D)
check("S2.K2a ledger U (15x15, exact rationals) is orthogonal: lossless", orth)
Uk = eye(D); Tk = eye(d); horizon_ok = True; fail_next = None
for k in range(1, N + 2):
    Uk = mm(Uk, U); Tk = mm(Tk, T)
    corner = [row[:d] for row in Uk[:d]]
    if k <= N and corner != Tk: horizon_ok = False
    if k == N + 1: fail_next = (corner != Tk)
check("S2.K2 corner of U^k == T^k exactly for k = 1..N (lossy port = corner of lossless ledger)", horizon_ok, f"N={N}")
check("S2.K2b identity FAILS at k = N+1 (finite ledger => finite horizon; echo returns)", fail_next)

# ---------------------------------------------------------------- S3
print("== S3 every-copy passivity => temperature; zeroth law ==")
def ergotropy(levels):   # levels: list of (E, p); passive iff 0
    Es = sorted(E for E, _ in levels); ps = sorted((p for _, p in levels), reverse=True)
    return sum(p * E for E, p in levels) - sum(p * E for p, E in zip(ps, Es))
def copies(levels, n):
    out = []
    for combo in product(levels, repeat=n):
        E = sum(c[0] for c in combo); p = F(1)
        for c in combo: p *= c[1]
        out.append((E, p))
    return out
def first_active(levels, nmax):
    for m in range(1, nmax + 1):
        w = ergotropy(copies(levels, m))
        if w > 0: return m, w
    return None, F(0)
pas = [(0, F(1, 2)), (1, F(2, 5)), (2, F(1, 10))]
m, w = first_active(pas, 5)
check("S3.K3 non-Gibbs passive state first turns ACTIVE at exactly n*=3 copies", m == 3,
      f"n*={m}, extractable work={w}")
Z = F(1) + F(1, 3) + F(1, 9)
gibbs = [(0, 1 / Z), (1, F(1, 3) / Z), (2, F(1, 9) / Z)]
check("S3.K3' Gibbs state stays passive for n=1..6", first_active(gibbs, 6)[0] is None)
A = [(0, F(2, 3)), (1, F(1, 3))]                         # w = 2^-E
B_hot = [(0, F(2, 3)), (2, F(1, 3))]                     # w = 2^(-E/2): hotter
B_eq = [(0, F(4, 5)), (2, F(1, 5))]                      # w = 2^-E: same temperature
joint = lambda X, Y: [(ex + ey, px * py) for (ex, px), (ey, py) in product(X, Y)]
mh, wh = first_active(joint(A, B_hot), 4)
check("S3.K3b zeroth law: two Gibbs ports at different T are jointly ACTIVE, first at n*=3", mh == 3,
      f"n*={mh}, extractable work={wh}")
check("S3.L3b equal-temperature joint stays passive for n=1..5", first_active(joint(A, B_eq), 5)[0] is None)

# ---------------------------------------------------------------- S4
print("== S4 Shannon + Nyquist => Landauer ==")
P, N0, Wb = sp.symbols('P N0 W', positive=True)
C = Wb * sp.log(1 + P / (N0 * Wb)) / sp.log(2)
Eb_over_N0 = sp.limit(P / C / N0, Wb, sp.oo)
check("S4.K4 lim_{W->oo} E_b/N0 == ln 2  (with N0 = kT: E_b >= kT ln 2)", sp.simplify(Eb_over_N0 - sp.log(2)) == 0,
      f"limit = {Eb_over_N0}")

print(f"\n{sum(res)}/{len(res)} GREEN")
