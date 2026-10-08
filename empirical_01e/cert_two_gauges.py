"""
Paper 01e, Part I certificates: the two gauges of the simplicial frame (exact; sympy + small numerics).

G1  One metric: ||sum c_i v_i||^2 = (1/(N-1)) c^T (N I - J) c for EVERY representative (N=3..6);
    the genesis circle/sphere equations are the N=3,4 cases; the genesis two-zero limit formula is refuted.
G2  Linear gauges = points w with w.1 = 1 (projector I - 1 w^T); zero-sum = barycentre, std form = vertex gauge.
G3  Temperature bridge F_tau = -tau log((1/N) sum e^{-c/tau}): equivariance, grad = Gibbs state,
    sandwich min <= F_tau <= min + tau log N, cumulant expansion, leading correction -(N-1)/(2N^2 tau) ||x||^2,
    tau = 1 section = -log(N p).
G4  Std-form regions: N cones {c_i = min}, every pair adjacent (codim-1 overlap); Cartesian orthants are not.
G5  Tropical (range) ball = Voronoi cell of the root lattice A_{N-1}; its vertices = the 2^N - 2 std-form 0/1 vectors.
G6  Integer std form = SU(N) weights: Z^N/Z1 -> min-normalized N^N; N-ality invariant; dominant = Young diagrams;
    Dynkin labels = consecutive differences; Weyl dimension for N=3.
"""
import itertools, math, random
import sympy as sp

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

def frame(N):
    """Unit regular-simplex frame vectors v_i = sqrt(N/(N-1)) (e_i - 1/N), living in H subset R^N."""
    s = sp.sqrt(sp.Rational(N, N - 1))
    return [s * (sp.Matrix([1 if j == i else 0 for j in range(N)]) - sp.ones(N, 1) / N) for i in range(N)]

print("G1  one quotient, one metric")
for N in range(3, 7):
    c = sp.symbols(f'c1:{N+1}', real=True); k = sp.Symbol('k', real=True)
    V = frame(N); x = sum((c[i] * V[i] for i in range(N)), sp.zeros(N, 1))
    M = N * sp.eye(N) - sp.ones(N); cv = sp.Matrix(c)
    Q = (cv.T * M * cv)[0] / (N - 1)
    chk(f"N={N}: ||sum c_i v_i||^2 = c^T(NI-J)c/(N-1)", sp.expand((x.T * x)[0] - Q) == 0)
    chk(f"N={N}: gauge invariant (c -> c + k1)", sp.expand(Q.subs({ci: ci + k for ci in c}, simultaneous=True) - Q) == 0)
    Qg = sum(ci**2 for ci in c) - sp.Rational(2, N - 1) * sum(c[i] * c[j] for i in range(N) for j in range(i + 1, N))
    chk(f"N={N}: = sum c_i^2 - 2/(N-1) sum_(i<j) c_i c_j  (genesis form)", sp.expand(Q - Qg) == 0)
l, n, m, p = sp.symbols('l n m p', real=True)
chk("N=3 genesis circle r^2 = l^2+n^2+m^2-ln-lm-nm",
    sp.expand(sp.Rational(1, 2) * (sp.Matrix([l, n, m]).T * (3 * sp.eye(3) - sp.ones(3)) * sp.Matrix([l, n, m]))[0]
              - (l**2 + n**2 + m**2 - l*n - l*m - n*m)) == 0)
Q4 = lambda a: sp.expand((sp.Matrix(a).T * (4 * sp.eye(4) - sp.ones(4)) * sp.Matrix(a))[0] / 3)
chk("N=4 two-zero point (l,0,0,p): r^2 = l^2 + p^2 - (2/3) l p (same single formula)",
    sp.expand(Q4([l, 0, 0, p]) - (l**2 + p**2 - sp.Rational(2, 3) * l * p)) == 0)
genesis_p15 = l**2 + sp.Rational(4, 3) * p**2 - sp.Rational(4, 3) * l * p
chk("genesis p.15 two-zero formula is refuted: at (0,0,0,p) it gives 4p^2/3, true value p^2",
    sp.simplify(genesis_p15.subs(l, 0) - Q4([0, 0, 0, p])) != 0 and Q4([0, 0, 0, p]) == p**2)

print("G2  linear gauges are points of the simplex")
N = 4; w = sp.Matrix(sp.symbols('w1:5'))
P = sp.eye(N) - sp.ones(N, 1) * w.T
cond = {w[3]: 1 - w[0] - w[1] - w[2]}
chk("w.1=1 => pi_w = I - 1 w^T is idempotent", sp.simplify((P * P - P).subs(cond)) == sp.zeros(N))
chk("pi_w kills the gauge line: pi_w 1 = 0", sp.simplify((P * sp.ones(N, 1)).subs(cond)) == sp.zeros(N, 1))
chk("image of pi_w = ker w^T (w^T pi_w = 0)", sp.simplify((w.T * P).subs(cond)) == sp.zeros(1, N))
Pzs = sp.eye(N) - sp.ones(N) / N
chk("w = barycentre 1/N  -> zero-sum projector I - J/N (orthogonal)", P.subs({w[i]: sp.Rational(1, N) for i in range(N)}) == Pzs)
cc = sp.Matrix([5, 2, 7, 3]); istar = 1
Pv = P.subs({w[i]: (1 if i == istar else 0) for i in range(N)})
chk("w = vertex e_argmin -> std form: pi(c) = c - min(c) 1 (nonnegative, one zero)",
    Pv * cc == cc - min(cc) * sp.ones(N, 1) and min(Pv * cc) == 0)

print("G3  the temperature bridge F_tau")
N = 3; c = sp.symbols('c1:4', real=True); tau, k = sp.symbols('tau k', positive=True)
F = -tau * sp.log(sum(sp.exp(-ci / tau) for ci in c) / N)
Fk = F.subs({ci: ci + k for ci in c}, simultaneous=True)
chk("equivariance F_tau(c + k1) = F_tau(c) + k", sp.simplify(sp.exp(-(Fk - k) / tau) - sp.exp(-F / tau)) == 0)
Z = sum(sp.exp(-ci / tau) for ci in c)
chk("grad F_tau = Gibbs state p_i = e^{-c_i/tau}/Z (sums to 1)",
    all(sp.simplify(sp.diff(F, c[i]) - sp.exp(-c[i] / tau) / Z) == 0 for i in range(3)))
chk("tau = 1 section: c_i - F_1(c) = -log(N p_i)",
    all(sp.simplify(sp.expand_log((c[i] - F + sp.log(N * sp.exp(-c[i] / tau) / Z)).subs(tau, 1), force=True)) == 0 for i in range(3)))
eps = sp.Symbol('eps', positive=True)
Fe = sp.series((-sp.log(sum(sp.exp(-eps * ci) for ci in c) / N) / eps), eps, 0, 3).removeO()
cb = sum(c) / N; d = [ci - cb for ci in c]
k2 = sum(di**2 for di in d) / N; k3 = sum(di**3 for di in d) / N
chk("cumulant expansion F = k1 - k2/(2tau) + k3/(6tau^2) + O(tau^-3)  (eps = 1/tau)",
    sp.simplify(sp.expand(Fe - (cb - k2 * eps / 2 + k3 * eps**2 / 6))) == 0)
Qc = sp.Rational(1, 2) * (sp.Matrix(c).T * (3 * sp.eye(3) - sp.ones(3)) * sp.Matrix(c))[0]
chk("leading correction is the metric: k2/2 = (N-1)/(2N^2) ||x||^2",
    sp.simplify(k2 / 2 - sp.Rational(N - 1, 2 * N**2) * Qc) == 0)
random.seed(1); ok = True
for _ in range(2000):
    NN = random.randint(2, 7); cv = [random.uniform(-5, 5) for _ in range(NN)]; t = 10 ** random.uniform(-3, 2)
    mn = min(cv); Ft = mn - t * math.log(sum(math.exp(-(x - mn) / t) for x in cv) / NN)
    ok &= (mn - 1e-12 <= Ft <= mn + t * math.log(NN) + 1e-12)
chk("sandwich min(c) <= F_tau(c) <= min(c) + tau log N  (2000 random cases, N=2..7)", ok)

print("G4  std-form regions: the normal fan of the simplex")
def wall_dim(N, i, j, samples=12):   # dim (mod gauge) of the shared wall {c_i = c_j = min} of regions i, j
    random.seed(100 * N + 10 * i + j); pts = []
    for _ in range(samples):
        cvec = [random.randint(1, 9) for _ in range(N)]; cvec[i] = cvec[j] = 0
        g = random.randint(-5, 5); pts.append([a + g for a in cvec])
        assert min(pts[-1]) == pts[-1][i] == pts[-1][j]          # lies in both regions
    span = sp.Matrix([sp.Matrix(pt).T * (sp.eye(N) - sp.ones(N) / N) for pt in pts])
    return span.rank()
for N in (3, 4, 5):
    chk(f"N={N}: N regions, every pair shares a codim-1 wall (dim N-2 in the (N-1)-dim quotient)",
        all(wall_dim(N, i, j) == N - 2 for i, j in itertools.combinations(range(N), 2)))
for d in (2, 3, 4):
    orth = list(itertools.product([1, -1], repeat=d))
    adj = sum(1 for a, b in itertools.combinations(orth, 2) if sum(x != y for x, y in zip(a, b)) == 1)
    chk(f"d={d}: Cartesian has 2^d={2**d} orthants, only {adj} of {math.comb(2**d, 2)} pairs adjacent; simplex fan: {d+1} regions, all {math.comb(d+1, 2)} pairs adjacent",
        adj == d * 2**(d - 1) and adj < math.comb(2**d, 2))

print("G5  tropical ball = Voronoi cell of A_{N-1}; vertices = std-form 0/1 vectors")
for N in (3, 4, 5):
    cube01 = [v for v in itertools.product([0, 1], repeat=N) if 0 < sum(v) < N]
    roots = [tuple((1 if t == i else -1 if t == j else 0) for t in range(N)) for i in range(N) for j in range(N) if i != j]
    rng = lambda x: max(x) - min(x)
    proj = lambda v: [sp.Rational(x) - sp.Rational(sum(v), N) for x in v]
    is_vertex = True
    for v in cube01:
        xv = proj(v); active = [r for r in roots if sum(a * b for a, b in zip(r, xv)) == 1]
        is_vertex &= (rng(xv) == 1) and (sp.Matrix(active).rank() == N - 1)
    chk(f"N={N}: the {2**N - 2} 0/1 std-form vectors are vertices of {{x in H : max x - min x <= 1}}", is_vertex and len(cube01) == 2**N - 2)
    lat = [v for v in itertools.product(range(-2, 3), repeat=N) if sum(v) == 0 and any(v)]
    random.seed(N); agree = 0; trials = 3000
    for _ in range(trials):
        y = [random.uniform(-1, 1) for _ in range(N)]; mu = sum(y) / N; y = [a - mu for a in y]
        in_trop = rng(y) <= 1
        n0 = sum(a * a for a in y)
        in_vor = all(n0 <= sum((a - b)**2 for a, b in zip(y, L)) for L in lat)
        agree += (in_trop == in_vor)
    chk(f"N={N}: Voronoi cell of A_{N-1} (brute force) == range ball, {agree}/{trials} random points", agree == trials)

print("G6  integer std form = SU(N) weights and Young diagrams")
N = 3; box = list(itertools.product(range(-3, 4), repeat=N))
std = lambda v: tuple(a - min(v) for a in v)
classes = {}
for v in box:
    classes.setdefault(std(v), set()).add(sum(v) % N)
chk("N=3: std form is constant on gauge classes and N-ality (sum mod N) is well defined on it",
    all(len(s) == 1 for s in classes.values()) and all(std(tuple(a + 5 for a in v)) == std(v) for v in box))
dom = sorted({tuple(sorted(s, reverse=True)) for s in classes})
chk("N=3: dominant std forms = partitions with <= N-1 rows (last row 0)", all(s[-1] == 0 and list(s) == sorted(s, reverse=True) for s in dom))
lam = (7, 4, 2)   # a GL(3) weight; massaction = 2 = number of full columns of height 3
chk("massaction = number of height-N columns removed: (7,4,2) -> (5,2,0), det^2", std(lam) == (5, 2, 0) and min(lam) == 2)
def dim_su3(s):
    a, b = s[0] - s[1], s[1] - s[2]          # Dynkin labels = consecutive differences (gauge invariant)
    return (a + 1) * (b + 1) * (a + b + 2) // 2
chk("Weyl dims from std forms: (0,0,0)->1, (1,0,0)->3, (1,1,0)->3bar, (2,1,0)->8, (3,0,0)->10",
    [dim_su3(s) for s in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 0, 0)]] == [1, 3, 3, 8, 10])

print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
