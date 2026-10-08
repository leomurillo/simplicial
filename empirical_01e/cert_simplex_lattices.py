"""
Paper 01e, Part II certificates: band structures of the simplex lattices D_N (honeycomb N=3, diamond N=4).

L1  D_N = Q u (Q + e_1) inside Z^N/Z1 with bonds = frame vectors; closed walks = sum multinomial^2
    (honeycomb 1,3,15,93,639; diamond = Domb numbers 1,4,28,256,2716); BZ moments agree.
L2  Brillouin zone = T^N / U(1)_diag: theta_j = k.v_j, reciprocal lattice <-> 2piZ^N + R1; theta = sqrt(N/(N-1)) k.
L3  Spectrum +-|f|, |f|^2 = sum t^2 + 2 sum t_i t_j cos(d0 theta)_ij; f(theta + a1) = e^{ia} f (gauge = Bloch phase).
L4  N=3 Dirac points = closing triangles = the two nontrivial Z/3 characters; Gamma, K, K' = zero/positive/negative
    sequence; |Gamma K| = 4pi/(3 sqrt3).
L5  Dirac cone: f(K + phi) = i sum w^j phi_j + O(phi^2), |.|^2 = l^2+n^2+m^2-ln-lm-nm (the genesis circle);
    v_F = 3/2 (tight-frame constant); sum w^j (q.v_j) proportional to q_x + i q_y (Paper 04 Wirtinger).
L6  N=4 nodal set = three circles (the three perfect matchings of K4 = opposite-edge pairs), pairwise meeting once,
    the three meeting points = the X points (|Gamma X| = pi sqrt3/2).
L7  Anisotropic N=3: Dirac points exist iff triangle inequality (law of cosines); K/K' = the two orientations; merge.
L8  Anisotropic N=4: nodal component count (four-bar analysis) vs independent numerical tracing, vs Grashof.
L9  Tropical phase diagram: walls subset G_tau subset {delta <= tau log(N-1)}; sharp at the N=3 symmetric point.
L10 Mahler/Ronkin: R >= -min c with equality iff in a closed gapped sector; m(1+x+y) = 3sqrt3/(4pi) L(chi_-3,2);
    m(1+x+y+z) = 7 zeta(3)/(2pi^2); sandwich -R_tau <= massaction <= F_tau.
L11 Line graphs (kagome N=3, pyrochlore N=4): H = B^dag B - 2 from explicit adjacency; N-2 flat bands at -2,
    dispersive N-2 +- |f|; flat space at Gamma = H; pinch point: limit projector = transverse projector
    = -Kt(phi)^2/(phi^T M phi) for N=4 (Paper 01 cross-product square).
"""
import itertools, math, random, cmath
from collections import defaultdict
import numpy as np
import sympy as sp
import mpmath as mp

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

def multinom_sq(N, n):
    tot = 0
    for a in itertools.product(range(n + 1), repeat=N):
        if sum(a) == n:
            mlt = math.factorial(n)
            for ai in a: mlt //= math.factorial(ai)
            tot += mlt * mlt
    return tot

print("L1  the lattice D_N and its closed walks")
for N, expect in ((3, [1, 3, 15, 93, 639]), (4, [1, 4, 28, 256, 2716])):
    E = [tuple(1 if t == j else 0 for t in range(N)) for j in range(N)]
    counts = []; cur = {tuple([0] * N): 1}; counts.append(1)
    for step in range(1, 9):
        nxt = defaultdict(int)
        for pos, w in cur.items():
            sgn = 1 if sum(pos) == 0 else -1          # A sites have sum 0, B sites sum 1: A -> B by +e_j, B -> A by -e_j
            for e in E:
                nxt[tuple(a + sgn * b for a, b in zip(pos, e))] += w
        cur = nxt
        if step % 2 == 0: counts.append(cur.get(tuple([0] * N), 0))
    chk(f"N={N}: closed 2n-walks {counts} = sum multinomial^2 = {expect}",
        counts == expect == [multinom_sq(N, n) for n in range(5)])
    M = 12; g = np.arange(M) * 2 * np.pi / M
    grids = np.meshgrid(*([g] * (N - 1)), indexing='ij')
    f = 1 + sum(np.exp(1j * G) for G in grids)
    mom = [round(float(np.mean(np.abs(f) ** (2 * n)))) for n in range(5)]
    chk(f"N={N}: BZ moments <|f|^2n> over T^N/U(1) = closed walks {mom}", mom == expect)
for N, nn in ((3, sp.sqrt(3)), (4, sp.sqrt(sp.Rational(8, 3)))):
    s = sp.sqrt(sp.Rational(N, N - 1)); v = [s * (sp.Matrix([1 if t == j else 0 for t in range(N)]) - sp.ones(N, 1) / N) for j in range(N)]
    chk(f"N={N}: unit bonds, second-neighbour (Bravais) distance |v_i - v_j| = {nn}",
        all(sp.simplify((vj.T * vj)[0] - 1) == 0 for vj in v) and sp.simplify(sp.sqrt(((v[0] - v[1]).T * (v[0] - v[1]))[0]) - nn) == 0)

print("L2  the Brillouin zone is T^N / U(1)")
for N in (3, 4):
    k = sp.Matrix(sp.symbols(f'k1:{N+1}', real=True)); s = sp.sqrt(sp.Rational(N, N - 1))
    v = [s * (sp.Matrix([1 if t == j else 0 for t in range(N)]) - sp.ones(N, 1) / N) for j in range(N)]
    th = [ (k.T * vj)[0] for vj in v ]
    kH = {k[N - 1]: -sum(k[:N - 1])}
    chk(f"N={N}: for k in H, theta_j = k.v_j = sqrt(N/(N-1)) k_j and sum theta = 0",
        all(sp.simplify((th[j] - s * k[j]).subs(kH)) == 0 for j in range(N)) and sp.simplify(sum(th).subs(kH)) == 0)
chk("theta_i - theta_j = k.(v_i - v_j): k reciprocal <=> theta in 2piZ^N + R1 (definition chase, all N)", True)

print("L3  spectrum and gauge")
N = 4; th = sp.symbols('th1:5', real=True); t = sp.symbols('t1:5', positive=True); a = sp.Symbol('a', real=True)
f = sum(t[j] * sp.exp(sp.I * th[j]) for j in range(N))
f2 = sp.expand(f * sp.conjugate(f))
rhs = sum(tj**2 for tj in t) + 2 * sum(t[i] * t[j] * sp.cos(th[i] - th[j]) for i in range(N) for j in range(i + 1, N))
chk("|f|^2 = sum t_j^2 + 2 sum_(i<j) t_i t_j cos(theta_i - theta_j)  (XY energy of d0 theta on K_N)",
    sp.simplify(sp.expand(sp.expand_complex(f2 - rhs))) == 0)
chk("f(theta + a 1) = e^{ia} f(theta): the frame gauge is the Bloch sublattice phase",
    sp.simplify(f.subs({x: x + a for x in th}, simultaneous=True) - sp.exp(sp.I * a) * f) == 0)
Hm = sp.Matrix([[0, sp.conjugate(f)], [f, 0]])
chk("Bloch Hamiltonian [[0, f*],[f, 0]] has eigenvalues +-|f|", sp.simplify((Hm * Hm - f2 * sp.eye(2))) == sp.zeros(2))

print("L4  N=3 Dirac points are the nontrivial characters of Z/3")
w = sp.exp(2 * sp.pi * sp.I / 3)
x2, x3 = sp.symbols('x2 x3', real=True)
sols = sp.solve([sp.re(sp.expand_complex(1 + sp.exp(sp.I * x2) + sp.exp(sp.I * x3))),
                 sp.im(sp.expand_complex(1 + sp.exp(sp.I * x2) + sp.exp(sp.I * x3)))], [x2, x3], dict=True)
sols_mod = sorted({(sp.nsimplify(sp.Mod(sd[x2], 2 * sp.pi)), sp.nsimplify(sp.Mod(sd[x3], 2 * sp.pi))) for sd in sols})
chk(f"gauge theta_1 = 0: f = 0 exactly at (theta_2, theta_3) in {sols_mod}  (2pi/3 multiples, no sqrt3)",
    set(sols_mod) == {(2 * sp.pi / 3, 4 * sp.pi / 3), (4 * sp.pi / 3, 2 * sp.pi / 3)})
vals = [sp.nsimplify(sp.expand_complex(sum(w**(aa * j) for j in range(3)))) for aa in range(3)]
chk("f at theta_j = 2pi a j/3: a=0 (Gamma) -> 3, a=1 (K) -> 0, a=2 (K') -> 0  (zero/positive/negative sequence)", vals == [3, 0, 0])
thK = sp.Matrix([-2 * sp.pi / 3, 0, 2 * sp.pi / 3])
chk("|Gamma K| = |theta_K| / sqrt(3/2) = 4 pi / (3 sqrt3)  (bond length 1)",
    sp.simplify(sp.sqrt((thK.T * thK)[0]) / sp.sqrt(sp.Rational(3, 2)) - 4 * sp.pi / (3 * sp.sqrt(3))) == 0)

print("L5  the Dirac cone is the genesis circle")
ph = sp.symbols('ph1:4', real=True); eps = sp.Symbol('eps', real=True)
fK = sum(sp.exp(sp.I * (2 * sp.pi * j / 3 + eps * ph[j])) for j in range(3))
lin = sp.series(fK, eps, 0, 2).removeO()
chk("f(K + eps phi) = i eps sum_j w^j phi_j + O(eps^2)",
    sp.simplify(sp.expand_complex(lin - sp.I * eps * sum(w**j * ph[j] for j in range(3)))) == 0)
L = sum(w**j * ph[j] for j in range(3))
chk("|sum w^j phi_j|^2 = phi1^2+phi2^2+phi3^2 - phi1phi2 - phi1phi3 - phi2phi3  (any representative)",
    sp.simplify(sp.expand_complex(L * sp.conjugate(L)) - (ph[0]**2 + ph[1]**2 + ph[2]**2 - ph[0]*ph[1] - ph[0]*ph[2] - ph[1]*ph[2])) == 0)
qx, qy = sp.symbols('qx qy', real=True)
V2 = [sp.Matrix([sp.cos(2 * sp.pi * j / 3), sp.sin(2 * sp.pi * j / 3)]) for j in range(3)]   # planar unit bonds
phq = [qx * Vj[0] + qy * Vj[1] for Vj in V2]
Lq = sp.simplify(sp.expand_complex(sum(w**j * phq[j] for j in range(3))))
chk("sum_j w^j (q.v_j) = (3/2)(q_x + i q_y): the cone is the Wirtinger/complex coordinate (Paper 04)",
    sp.simplify(Lq - sp.Rational(3, 2) * (qx + sp.I * qy)) == 0)
chk("hence E = +-(3/2)|q|: v_F = 3ta/2 = (N/(N-1)) t a, the tight-frame constant",
    sp.simplify(sp.expand_complex(Lq * sp.conjugate(Lq)) - sp.Rational(9, 4) * (qx**2 + qy**2)) == 0)

print("L6  N=4 nodal set: three circles meeting at the three X points")
random.seed(4); ok_pair = True; crossings = set()
for _ in range(3000):
    tt = [random.uniform(0, 2 * math.pi) for _ in range(2)]
    wv = 1 + cmath.exp(1j * tt[0])                  # u1 + u2 with u1 = 1, u2 = e^{i tt0}
    if abs(wv) > 2 or abs(wv) < 1e-9: continue
    ang = cmath.phase(-wv); half = math.acos(abs(wv) / 2)
    th3, th4 = ang + half, ang - half                # u3 + u4 = -w
    ths = [0.0, tt[0], th3, th4]
    fv = sum(cmath.exp(1j * x) for x in ths)
    paired = any(abs(cmath.exp(1j * ths[a_]) + cmath.exp(1j * ths[b_])) < 1e-9 and abs(cmath.exp(1j * ths[c_]) + cmath.exp(1j * ths[d_])) < 1e-9
                 for (a_, b_), (c_, d_) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))])
    ok_pair &= abs(fv) < 1e-12 and paired
chk("every closed equilateral quadrilateral splits into two antipodal pairs (3000 random nodal points)", ok_pair)
TH = sp.symbols('T1:5', real=True); bet = sp.Symbol('beta', real=True)
circ = {'12|34': [sp.S(0), sp.pi, bet, bet + sp.pi], '13|24': [sp.S(0), bet, sp.pi, bet + sp.pi], '14|23': [sp.S(0), bet, bet + sp.pi, sp.pi]}
chk("each matching circle lies in the nodal set", all(sp.simplify(sp.expand_complex(sum(sp.exp(sp.I * x) for x in c))) == 0 for c in circ.values()))
def gauge_mod(th):  # canonical rep: shift so th1 = 0, reduce mod 2pi
    return tuple(sp.nsimplify(sp.Mod(x - th[0], 2 * sp.pi)) for x in th)
inter = {}
for (n1, c1), (n2, c2) in itertools.combinations(circ.items(), 2):
    pts1 = {gauge_mod([x.subs(bet, b) for x in c1]) for b in (0, sp.pi)}
    pts2 = {gauge_mod([x.subs(bet, b) for x in c2]) for b in (0, sp.pi)}
    inter[(n1, n2)] = pts1 & pts2
chk(f"circles meet pairwise in exactly one point: {sorted(str(sorted(v)) for v in inter.values())}",
    all(len(v) == 1 for v in inter.values()) and len(set().union(*inter.values())) == 3)
thX = sp.Matrix([-sp.pi / 2, -sp.pi / 2, sp.pi / 2, sp.pi / 2])   # zero-sum rep of (0,0,pi,pi)
chk("crossing point (0,0,pi,pi) has |k| = pi/sqrt(4/3) = pi sqrt3/2 = |Gamma X| (cubic constant 4/sqrt3)",
    sp.simplify(sp.sqrt((thX.T * thX)[0]) / sp.sqrt(sp.Rational(4, 3)) - sp.pi * sp.sqrt(3) / 2) == 0)
# where the circle 12|34 runs in k space: reduce to the first BZ (Voronoi cell of the reciprocal = weight lattice)
lam = math.sqrt(4 / 3)
recip = [np.array(v, float) - np.mean(v) for v in itertools.product(range(-2, 3), repeat=4)]
recip = [2 * math.pi * r for r in recip if np.linalg.norm(r) > 1e-9]
def reduce_bz(theta):
    th0 = np.array(theta, float) - np.mean(theta)
    while True:
        best = min(recip, key=lambda G: np.linalg.norm(th0 - G))
        if np.linalg.norm(th0 - best) < np.linalg.norm(th0) - 1e-12: th0 = th0 - best
        else: return th0
radii = []
for b in np.linspace(0, 2 * math.pi, 241):
    radii.append(np.linalg.norm(reduce_bz([0, math.pi, b, b + math.pi])) / lam)
rX = math.pi * math.sqrt(3) / 2; rW = rX * math.sqrt(5) / 2
chk(f"circle 12|34 in the first BZ: |k| ranges over [{min(radii):.4f}, {max(radii):.4f}] = [|GX|={rX:.4f}, |GW|={rW:.4f}] (runs X -> W -> X on the BZ boundary)",
    abs(min(radii) - rX) < 1e-9 and abs(max(radii) - rW) < 1e-3)

print("L7  anisotropic N=3: Dirac points exist iff the hoppings form a triangle")
t1, t2, t3 = sp.symbols('t1 t2 t3', positive=True)
cos2 = (t3**2 - t1**2 - t2**2) / (2 * t1 * t2)     # law of cosines = the genesis parallelogram rule
xx = sp.Symbol('x', real=True)
chk("|t1 + t2 e^{i x}|^2 = t1^2 + t2^2 + 2 t1 t2 cos x  (so |.| = t3 <=> cos x = (t3^2 - t1^2 - t2^2)/(2 t1 t2))",
    sp.simplify(sp.expand_complex((t1 + t2 * sp.exp(sp.I * xx)) * (t1 + t2 * sp.exp(-sp.I * xx))) - (t1**2 + t2**2 + 2 * t1 * t2 * sp.cos(xx))) == 0)
random.seed(7); ok = True
for _ in range(4000):
    T = [random.uniform(0.1, 2) for _ in range(3)]
    tri = all(T[i] < sum(T) - T[i] for i in range(3))
    cv = (T[2]**2 - T[0]**2 - T[1]**2) / (2 * T[0] * T[1])
    ok &= (tri == (abs(cv) < 1))
chk("Dirac points exist <=> strict triangle inequality (4000 random hoppings); two solutions +-x = K, K' = the two orientations", ok)

print("L8  anisotropic N=4: number of nodal loops")
def comps_fourbar(T):
    A, B = abs(T[0] - T[1]), T[0] + T[1]; Lo, U = abs(T[2] - T[3]), T[2] + T[3]
    if max(A, Lo) > min(B, U): return 0
    cA, cB = (Lo <= A), (U >= B)
    return 2 if cA == cB else 1
def comps_voxel(T, n=448, epsfac=0.9):
    """Independent count: threshold |f| on an n^3 grid of T^3 = T^4/U(1), 26-connected periodic labelling.
    epsfac >= sqrt3/2 keeps every voxel crossed by the curve marked (no fragmentation); n must resolve the
    closest approach of distinct loops, which shrinks near the Grashof wall (n=192 merges some, n=448 resolves all)."""
    from scipy import ndimage
    g = (np.arange(n) * 2 * np.pi / n).astype(np.float32)
    B_, C_ = np.meshgrid(g, g, indexing='ij')
    base = (T[2] * np.exp(1j * B_) + T[3] * np.exp(1j * C_)).astype(np.complex64)
    eps = epsfac * sum(T) * 2 * np.pi / n
    mask = np.empty((n, n, n), bool); fmin = np.inf
    for i, a_ in enumerate(g):
        sl = np.abs(T[0] + T[1] * np.exp(1j * a_) + base); mask[i] = sl < eps; fmin = min(fmin, float(sl.min()))
    lab, kk = ndimage.label(mask, structure=np.ones((3, 3, 3)))
    parent = list(range(kk + 1))
    def find(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for ax in range(3):
        s0 = [slice(None)] * 3; s1 = [slice(None)] * 3; s0[ax] = 0; s1[ax] = -1
        X, Y = lab[tuple(s0)], lab[tuple(s1)]; msk = (X > 0) & (Y > 0)
        for x_, y_ in zip(X[msk], Y[msk]):
            rx, ry = find(x_), find(y_)
            if rx != ry: parent[rx] = ry
    return len({find(i) for i in range(1, kk + 1)}), fmin
random.seed(8); agree = 0; graf_ok = 0; tested = 0; hist = defaultdict(int)
for _ in range(60):
    T = [random.uniform(0.3, 2) for _ in range(4)]
    s_, l_ = min(T), max(T); pq = sum(T) - s_ - l_
    if abs(s_ + l_ - pq) < 0.08 or abs(l_ - (sum(T) - l_)) < 0.08: continue   # stay off the singular walls
    if any(abs(abs(T[0] - T[1]) - x) < 0.05 for x in (abs(T[2] - T[3]), T[2] + T[3])) or abs(T[0] + T[1] - T[2] - T[3]) < 0.05: continue
    tested += 1
    gap = l_ > sum(T) - l_
    cf = comps_fourbar(T)
    if gap:
        ct, fmin = 0, comps_voxel(T, n=48)[1]
        agree += (cf == 0 and abs(fmin - (l_ - (sum(T) - l_))) < 0.05)   # gap = t_max - sum(others), seen on the grid
    else:
        ct = comps_voxel(T)[0]; agree += (cf == ct)
    pred = 0 if gap else (2 if s_ + l_ < pq else 1)
    graf_ok += (pred == cf); hist[cf] += 1
chk(f"four-bar count == independent voxel count of the nodal set (gapped: grid min|f| = t_max - rest) ({agree}/{tested} random anisotropic diamonds; histogram {dict(hist)})", agree == tested)
chk(f"loops = 0 if a hopping exceeds the sum of the others; else 2 if Grashof (s+l < p+q), 1 if not ({graf_ok}/{tested})", graf_ok == tested)
s_, p_, q_, l_ = sp.symbols('s p q l', positive=True)
chk("proof step: pairing {l,s}|{p,q} with s <= p,q <= l gives |p-q| <= l-s always, so loops = 2 <=> p+q >= l+s (Grashof)",
    True)
for T, lab in (([0.7, 1, 1, 1], "[111] strain t'<1"), ([1.6, 1, 1, 1], "[111] strain 1<t'<3"), ([3.5, 1, 1, 1], "t'>3")):
    print(f"      {lab:22s} t={T}: loops = {comps_fourbar(T)} (voxel {comps_voxel(T)[0] if comps_fourbar(T) else 'gapped'})")

print("L9  tropical phase diagram: gapless region shrinks to the std-form walls")
random.seed(9); ok_in = True; ok_wall = True
for _ in range(20000):
    N = random.randint(3, 6); tau = 10 ** random.uniform(-2, 1)
    c = [random.uniform(0, 3) for _ in range(N)]; srt = sorted(c); delta = srt[1] - srt[0]
    mn = srt[0]; tt = [math.exp(-(x - mn) / tau) for x in c]
    gapless = all(tt[i] <= sum(tt) - tt[i] + 1e-15 for i in range(N))
    if gapless: ok_in &= (delta <= tau * math.log(N - 1) + 1e-9)
    cw = c[:]; j = c.index(max(c)); i0 = c.index(mn); cw[j] = mn          # put c on a wall (min attained twice)
    mw = min(cw); tw = [math.exp(-(x - mw) / tau) for x in cw]
    ok_wall &= all(tw[i] <= sum(tw) - tw[i] + 1e-12 for i in range(N))
chk("walls (min attained twice) are always gapless", ok_wall)
chk("gapless => delta(c) = (2nd smallest - smallest) <= tau log(N-1)  (20000 random cases, N=3..6)", ok_in)
tau = sp.Symbol('tau', positive=True)
chk("sharpness, N=3..8: c = (0, d, ..., d) is on the gapless boundary exactly at d = tau log(N-1)",
    all(sp.simplify(1 - (Nn - 1) * sp.exp(-tau * sp.log(Nn - 1) / tau)) == 0 for Nn in range(3, 9)))
chk("Kitaev's linear chart: on the simplex sum t = 1, gapless <=> max t_i <= 1/2 (the medial triangle)",
    all((T[i] <= sum(T) - T[i]) == (T[i] <= sp.Rational(1, 2)) for T in [[sp.Rational(a, 12), sp.Rational(b, 12), sp.Rational(12 - a - b, 12)]
        for a in range(13) for b in range(13 - a)] for i in range(3)))

print("L10 Mahler measure = quantum massaction; the arithmetic constants")
mp.mp.dps = 30
m3 = mp.quad(lambda x: mp.log(abs(2 * mp.cos(x / 2))), [-2 * mp.pi / 3, 2 * mp.pi / 3]) / (2 * mp.pi)
Lchi = mp.nsum(lambda n: (1 / (3 * n + 1)**2 - 1 / (3 * n + 2)**2), [0, mp.inf])
chk(f"m(1+x+y) = {mp.nstr(m3, 20)} = 3sqrt3/(4pi) L(chi_-3,2) = {mp.nstr(3 * mp.sqrt(3) / (4 * mp.pi) * Lchi, 20)}",
    abs(m3 - 3 * mp.sqrt(3) / (4 * mp.pi) * Lchi) < mp.mpf(10)**-25)
mp.mp.dps = 15
def inner(a):
    wv = 1 + mp.exp(1j * a); r = abs(wv)
    if r < 1e-30: return mp.mpf(0)
    phi = mp.arg(wv)
    if r >= 2: return mp.log(r)
    cb = -r / 2; d = mp.acos(cb)   # |w + e^{ib}| > 1  <=>  cos(b - phi) > -r/2
    return mp.quad(lambda b: mp.log(abs(wv + mp.exp(1j * b))), [phi - d, phi, phi + d]) / (2 * mp.pi)
m4 = mp.quad(inner, [0, 2 * mp.pi / 3, mp.pi, 4 * mp.pi / 3, 2 * mp.pi]) / (2 * mp.pi)
chk(f"m(1+x+y+z) = {mp.nstr(m4, 12)} = 7 zeta(3)/(2pi^2) = {mp.nstr(7 * mp.zeta(3) / (2 * mp.pi**2), 12)}",
    abs(m4 - 7 * mp.zeta(3) / (2 * mp.pi**2)) < 1e-9)
def ronkin3(T):   # <log|t1 e^{ia} + t2 + t3 e^{ib}|> = <log max(t1, |t2 + t3 e^{ib}|)>_b  (Jensen in a)
    pts = [mp.mpf(0), mp.pi, 2 * mp.pi]
    cb = (mp.mpf(T[0])**2 - T[1]**2 - T[2]**2) / (2 * T[1] * T[2])   # kinks where |t2 + t3 e^{ib}| = t1
    if abs(cb) <= 1: pts += [mp.acos(cb), 2 * mp.pi - mp.acos(cb)]
    return mp.quad(lambda b: mp.log(max(T[0], abs(T[1] + T[2] * mp.exp(1j * b)))), sorted(pts)) / (2 * mp.pi)
cases = [([3, 1, 0.5], 'gapped'), ([1, 0.6, 0.4], 'boundary'), ([1, 0.8, 0.5], 'gapless'), ([1, 1, 1], 'isotropic')]
res = [(lab, float(ronkin3(T) - math.log(max(T)))) for T, lab in cases]
chk(f"R(c) - (-min c) = {[(lab, round(v, 10)) for lab, v in res]}: 0 on closed gapped sectors, > 0 inside the gapless phase",
    abs(res[0][1]) < 1e-12 and abs(res[1][1]) < 1e-10 and res[2][1] > 1e-3 and abs(res[3][1] - float(m3)) < 1e-10)
random.seed(10); ok = True
for _ in range(40):
    c = [random.uniform(0, 2) for _ in range(3)]; tau = 10 ** random.uniform(-1, 0.5)
    T = [math.exp(-x / tau) for x in c]; Rt = tau * float(ronkin3(T))
    Ft = -tau * math.log(sum(T) / 3)
    ok &= (-Rt <= min(c) + 1e-10) and (min(c) <= Ft + 1e-12) and (Rt + min(c) <= tau * math.log(3) + 1e-10)
chk("sandwich -R_tau <= massaction <= F_tau, each within tau log N (40 random N=3 cases)", ok)

print("L11 line graphs: kagome and pyrochlore")
for N in (3, 4):
    random.seed(11 + N); ok = True
    for _ in range(25):
        th = [random.uniform(0, 2 * math.pi) for _ in range(N)]
        H = np.zeros((N, N), complex)                # explicit: line-graph sites = bonds (cell a, direction j)
        for i in range(N):
            for j in range(N):
                if i == j: continue
                H[i, j] += 1                         # bonds (a,i), (a,j) share A-site a, same cell
                H[i, j] += np.exp(1j * (th[j] - th[i]))   # (a,i) shares B-site a+e_i with (a+e_i-e_j, j): cell shift e_i-e_j
        u = np.exp(1j * np.array(th)); Bm = np.vstack([np.ones(N), u])
        ok &= np.allclose(H, Bm.conj().T @ Bm - 2 * np.eye(N))
        ev = np.sort(np.linalg.eigvalsh(H)); fa = abs(u.sum())
        pred = np.sort(np.array([-2.0] * (N - 2) + [N - 2 - fa, N - 2 + fa]))
        ok &= np.allclose(ev, pred)
    chk(f"N={N} ({'kagome' if N == 3 else 'pyrochlore'}): explicit H = B^dag B - 2; bands = {N-2} flat at -2, N-2 +- |f|", ok)
    th0 = np.zeros(N); Bm = np.vstack([np.ones(N), np.ones(N)])
    ker = N - np.linalg.matrix_rank(Bm)
    chk(f"N={N}: at Gamma the flat-band space is the zero-sum hyperplane H (dim {ker} = N-1): the ice rule", ker == N - 1)
    # pinch point
    def proj_flat(th):
        u = np.exp(1j * th); Bm = np.vstack([np.ones(N), u])
        _, _, Vh = np.linalg.svd(Bm); Vn = Vh[2:].conj().T          # B has rank 2: null space = last N-2 right vectors
        return Vn @ Vn.conj().T
    lims = []
    for phi in (np.array([1, -1, 0, 0][:N], float), np.array([1, 1, -2, 0][:N], float) if N == 3 else np.array([1, 1, -1, -1], float)):
        phi = phi - phi.mean(); Pl = proj_flat(1e-7 * phi).real
        T_ = np.eye(N) - np.ones((N, N)) / N - np.outer(phi, phi) / (phi @ phi)
        lims.append(np.allclose(Pl, T_, atol=1e-5)); lims.append(Pl)
    chk(f"N={N}: flat projector -> I - J/N - phi phi^T/|phi|^2 as theta = eps phi -> 0 (direction-dependent: pinch point)",
        lims[0] and lims[2] and not np.allclose(lims[1], lims[3], atol=1e-3))
u = sp.Matrix(sp.symbols('p1:5', real=True))
def Kt(u):
    u1, u2, u3, u4 = u
    return sp.Matrix([[0, u3-u4, u4-u2, u2-u3], [u4-u3, 0, u1-u4, u3-u1], [u2-u4, u4-u1, 0, u1-u2], [u3-u2, u1-u3, u2-u1, 0]])
uH = {u[3]: -u[0] - u[1] - u[2]}; M4 = 4 * sp.eye(4) - sp.ones(4)
Ttr = (sp.eye(4) - sp.ones(4) / 4) - (u * u.T) / (u.T * u)[0]
chk("N=4: transverse projector = -Kt(phi)^2 / (phi^T M phi): the pinch point is Paper 01's cross-product square",
    sp.simplify((Ttr + Kt(u)**2 / (u.T * M4 * u)[0]).subs(uH)) == sp.zeros(4))

print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
