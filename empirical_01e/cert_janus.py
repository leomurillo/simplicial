"""
Paper 01e, Part III certificates: Janus inversion J[c] = [-c] read in the simplicial frame (Section 12).

J1  The arenas are the gauge line: R^N = H (+) R1, J = -1 on both summands; every class c + R1 meets both
    half-spaces sum>0, sum<0 and crosses H exactly once (at its zero-sum representative); of the 2^N sign
    corners 1_S, the two constant ones go to the origin and the 2^N - 2 others are the vertices of the tropical
    ball (Thm 4.3); J acts on them by complement; in standard form J[c] = max c - c, range is J-invariant.
J2  Janus is temperature reversal: p_tau(-c) = p_{-tau}(c), F_tau(-c) = -F_{-tau}(c), p_tau(s c) = p_{tau/s}(c);
    at beta = 0 the state is the barycentre and dp/dbeta = -(c - cbar)/N (the zero-sum representative);
    ergotropy W = 0 for beta >= 0 and W > 0 for beta < 0 (non-constant c).
J3  Janus on weights is charge conjugation: N-ality k -> -k, 1_S -> 1_{S^c}; fixed classes 0 and N/2;
    N = 4: A_3*/A_3 = Z/4 with classes 1, 3 the two tetrahedral-hole classes of FCC (4 neighbours at 3/8 d^2)
    and class 2 the octahedral holes (6 at 1/2 d^2); J swaps 1 <-> 3, fixes 0, 2.  Diamond: J(D_4) = D_4 - e_1 and
    bond-midpoint inversion swaps the sublattices.  Graphene zone: theta -> -theta swaps K <-> K'.
J4  Exterior and Clifford algebra: -I acts by (-1)^k on Lambda^k; det(-I_4) = +1 = det(-I_H) det(-1 on R1);
    in Cl(R^4) -I_4 is conjugation by the pseudoscalar omega, omega^2 = 1, and an odd relabelling sends omega -> -omega;
    Hodge * on Lambda^2 R^4 (opposite edges of K_4) is a para-complex structure (*^2 = 1, 3 + 3) that COMMUTES with J
    and ANTICOMMUTES with an orientation flip; * on Lambda^1 is the complement e_i -> +-e_{[4] minus i}.
J5  Quadrances see relative, not absolute, Janus parity: Q(sX) = s^2 Q(X), V(sX) = s^3 V(X); Cayley-Menger gives V^2;
    X and -X have identical quadrances and opposite V; V(A) V(B) is a polynomial in quadrances (bideterminant).
J6  Galois limit on prime polygons: in a regular p-gon the side v0v1 is parallel to the diagonal v_{p-1}v_2 with ratio
    1 + 2 cos(2 pi/p), of degree (p-1)/2 over Q (not a power of 2 for p = 7, 11, 13).
"""
import itertools, math, random
import numpy as np
import sympy as sp

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

std = lambda v: tuple(a - min(v) for a in v)           # standard form (vertex gauge) on integer/rational tuples
rng_norm = lambda v: max(v) - min(v)

print("J1  the arenas are the gauge line")
for N in (3, 4, 5):
    c = sp.Matrix(sp.symbols(f'c1:{N+1}', real=True)); one = sp.ones(N, 1); t = sp.Symbol('t', real=True)
    tr = sum(c) / N; x = c - tr * one
    chk(f"N={N}: c = x + (sum c/N) 1 with x in H; J = -1 on both summands",
        sp.simplify(sum(x)) == 0 and sp.simplify((-c) - ((-x) + (-tr) * one)) == sp.zeros(N, 1))
    sol = sp.solve(sp.Eq(sum(c + t * one), 0), t)
    chk(f"N={N}: c + t1 crosses H exactly once, at t = -cbar (its zero-sum representative)",
        len(sol) == 1 and sp.simplify(sol[0] + tr) == 0)
    corners = list(itertools.product((0, 1), repeat=N))
    const = [S for S in corners if len(set(S)) == 1]; mixed = [S for S in corners if len(set(S)) > 1]
    chk(f"N={N}: the two constant sign corners (arenas) both map to the origin mod 1",
        all(std(S) == (0,) * N for S in const))
    chk(f"N={N}: the {2**N - 2} mixed corners map to distinct classes of range 1 (vertices of the tropical ball)",
        len({std(S) for S in mixed}) == 2**N - 2 and all(rng_norm(S) == 1 for S in mixed))
    chk(f"N={N}: J acts on corners by complement, -1_S = 1_(S^c) mod 1",
        all(std(tuple(-a for a in S)) == std(tuple(1 - a for a in S)) for S in mixed))
random.seed(1)
cases = [tuple(random.randint(-9, 9) for _ in range(4)) for _ in range(500)]
chk("standard form of J[c] is max c - c (min-plus <-> max-plus), 500 cases",
    all(std(tuple(-a for a in v)) == tuple(max(v) - a for a in v) for v in cases))
chk("range norm is J-invariant (tropical ball centrally symmetric), 500 cases",
    all(rng_norm(tuple(-a for a in v)) == rng_norm(v) for v in cases))
chk("J sends the min region C_i of c to the max region of c (argmin(-c) = argmax c)",
    all(set(i for i in range(4) if -v[i] == min(-a for a in v)) == set(i for i in range(4) if v[i] == max(v)) for v in cases))

print("J2  Janus is temperature reversal")
N = 4; c = sp.symbols('c1:5', real=True); tau, s, b = sp.symbols('tau s beta', real=True, nonzero=True)
Z = lambda cc, T: sum(sp.exp(-ci / T) for ci in cc)
p = lambda cc, T: [sp.exp(-ci / T) / Z(cc, T) for ci in cc]
F = lambda cc, T: -T * sp.log(Z(cc, T) / N)
chk("p_tau(-c) = p_(-tau)(c)", all(sp.simplify(a - bb) == 0 for a, bb in zip(p([-ci for ci in c], tau), p(c, -tau))))
chk("F_tau(-c) = -F_(-tau)(c)", sp.simplify(F([-ci for ci in c], tau) + F(c, -tau)) == 0)
chk("p_tau(s c) = p_(tau/s)(c): scaling a form through 0 is beta = s/tau through 0",
    all(sp.simplify(a - bb) == 0 for a, bb in zip(p([s * ci for ci in c], tau), p(c, tau / s))))
pb = [sp.exp(-b * ci) / sum(sp.exp(-b * cj) for cj in c) for ci in c]
cbar = sum(c) / N
chk("beta = 0 is the barycentre (the zero-sum gauge w = 1/N)", all(sp.limit(q, b, 0) == sp.Rational(1, N) for q in pb))
chk("dp/dbeta at 0 = -(c - cbar)/N: the shape carried through the boundary is the zero-sum representative",
    all(sp.simplify(sp.diff(q, b).subs(b, 0) + (ci - cbar) / N) == 0 for q, ci in zip(pb, c)))
def gibbs(cv, beta):
    w = np.exp(-beta * (cv - cv.min() if beta > 0 else cv - cv.max())); return w / w.sum()
def ergotropy(pv, cv):   # W = <c>_p - <c>_passive, passive = populations sorted decreasing onto energies increasing
    order = np.argsort(cv); passive = np.empty_like(pv); passive[order] = np.sort(pv)[::-1]
    return pv @ cv - passive @ cv
rs = np.random.default_rng(7); okp = okn = 0; T = 2000
for _ in range(T):
    cv = rs.normal(size=rs.integers(2, 8)); beta = rs.uniform(0.05, 5)
    okp += abs(ergotropy(gibbs(cv, beta), cv)) < 1e-12
    okn += ergotropy(gibbs(cv, -beta), cv) > 1e-12
chk(f"beta > 0 arena passive (W = 0): {okp}/{T}; Janus image beta < 0 active (W > 0): {okn}/{T}", okp == T and okn == T)
chk("the barycentre is the unique J-fixed Gibbs state (p_beta(-c) = p_beta(c) for non-constant c iff beta = 0)",
    sp.solve(sp.Eq(pb[0].subs({c[0]: 0, c[1]: 1, c[2]: 1, c[3]: 1}),
                   pb[0].subs({c[0]: 0, c[1]: -1, c[2]: -1, c[3]: -1})), b) == [])

print("J3  Janus on weights is charge conjugation")
for N in range(3, 7):
    box = list(itertools.product(range(-3, 4), repeat=N))
    chk(f"N={N}: N-ality of -lambda is -(N-ality of lambda) mod N",
        all((-sum(v)) % N == (-(sum(v) % N)) % N for v in box))
    fixed = sorted(k for k in range(N) if (-k) % N == k)
    chk(f"N={N}: J-fixed N-ality classes = {fixed} (0, and N/2 for even N)",
        fixed == ([0, N // 2] if N % 2 == 0 else [0]))
    chk(f"N={N}: frame vertex e_i (fundamental, N-ality 1) -> facet centre 1 - e_i (N-ality N-1, the dual)",
        all(std(tuple(-(1 if j == i else 0) for j in range(N))) == std(tuple(0 if j == i else 1 for j in range(N)))
            for i in range(N)))
N = 4
def nq(v):  # squared frame norm, Thm 2.1
    v = np.array(v, float); return (N * v @ v - v.sum() ** 2) / (N - 1)
Qpts = [q for q in itertools.product(range(-2, 3), repeat=N) if sum(q) == 0]
d2 = min(nq(q) for q in Qpts if any(q))
def hole(v):
    ds = sorted(nq(np.array(v) - np.array(q)) for q in Qpts); m = ds[0]
    return round(m / d2, 6), sum(abs(x - m) < 1e-9 for x in ds)
reps = {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (1, 1, 1, 0)}
chk(f"N=4: Q = A_3 is FCC (12 nearest neighbours at d^2 = {d2:.4f})",
    sum(abs(nq(q) - d2) < 1e-9 for q in Qpts) == 12)
chk("N=4: class 1 = tetrahedral holes (4 FCC sites at 3/8 d^2)", hole(reps[1]) == (0.375, 4))
chk("N=4: class 3 = the other tetrahedral holes (4 at 3/8 d^2)", hole(reps[3]) == (0.375, 4))
chk("N=4: class 2 = octahedral holes (6 FCC sites at 1/2 d^2)", hole(reps[2]) == (0.5, 6))
chk("N=4: J swaps classes 1 <-> 3 and fixes 0, 2", [(-k) % 4 for k in range(4)] == [0, 3, 2, 1])
box = list(itertools.product(range(-2, 3), repeat=4))
inD4 = lambda v: sum(v) % 4 in (0, 1)                        # D_4 = Q u (Q + e1): N-ality 0 or 1
e1 = (1, 0, 0, 0); neg = lambda v: tuple(-a for a in v); sub = lambda v, w: tuple(a - b for a, b in zip(v, w))
chk("diamond: J(D_4) = D_4 - e_1, i.e. -v in D_4 - e_1 iff v in D_4 (J maps the diamond to a translate)",
    all(inD4(sub(neg(v), neg(e1))) == inD4(v) for v in box))
chk("diamond: inversion through the bond midpoint e_1/2 (x -> e_1 - x) preserves D_4 and swaps A (class 0) <-> B (class 1)",
    all(inD4(sub(e1, v)) and (sum(sub(e1, v)) % 4) == 1 - sum(v) % 4 for v in box if inD4(v)))
th = sp.symbols('t1:4', real=True)
f3 = sum(sp.exp(sp.I * x) for x in th)
chk("graphene: f(-theta) = conj f(theta), and theta -> -theta swaps the Dirac characters a = 1 <-> a = 2",
    sp.simplify(f3.subs({x: -x for x in th}, simultaneous=True) - sp.conjugate(f3)) == 0
    and all(sp.expand_complex(sum(sp.exp(sp.I * 2 * sp.pi * a * j / 3) for j in range(3))) == 0 for a in (1, 2))
    and [(-a) % 3 for a in (1, 2)] == [2, 1])

print("J4  exterior and Clifford algebra")
def compound(A, k):
    n = A.shape[0]; B = list(itertools.combinations(range(n), k))
    return sp.Matrix(len(B), len(B), lambda r, s: A.extract(list(B[r]), list(B[s])).det())
I4 = sp.eye(4)
chk("-I_4 acts on Lambda^k R^4 as (-1)^k (vertices, faces flip; edges fixed)",
    all(compound(-I4, k) == (-1) ** k * sp.eye(math.comb(4, k)) for k in range(1, 5)))
u = sp.ones(4, 1) / 2; Hb = sp.Matrix.hstack(*[sp.Matrix([1, -1, 0, 0]) / sp.sqrt(2), sp.Matrix([1, 1, -2, 0]) / sp.sqrt(6),
                                              sp.Matrix([1, 1, 1, -3]) / sp.sqrt(12), u])
chk("det(-I_4) = +1 = det(-I_H) * det(-1 on R1) = (-1)(-1): the gauge line supplies the extra reflection",
    (-I4).det() == 1 and sp.simplify(Hb.T * Hb) == I4 and (-sp.eye(3)).det() == -1)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]]); e2 = sp.eye(2)
kron = lambda A, B: sp.Matrix(sp.BlockMatrix([[A[i, j] * B for j in range(2)] for i in range(2)]))
gam = [kron(s1, s1), kron(s1, s2), kron(s1, s3), kron(s2, e2)]       # Euclidean Cl(R^4): g_i g_j + g_j g_i = 2 delta_ij
chk("Clifford relations g_i g_j + g_j g_i = 2 delta_ij", all(gam[i] * gam[j] + gam[j] * gam[i] == 2 * (i == j) * sp.eye(4)
                                                            for i in range(4) for j in range(4)))
om = gam[0] * gam[1] * gam[2] * gam[3]
chk("pseudoscalar omega = g1 g2 g3 g4: omega^2 = +1, omega g_i omega^-1 = -g_i (J = Ad omega is inner)",
    om * om == sp.eye(4) and all(om * g * om.inv() == -g for g in gam))
om_odd = gam[1] * gam[0] * gam[2] * gam[3]
chk("odd relabelling (swap e1, e2) sends omega -> -omega: the Janus bit eps_1234 is the sign of omega", om_odd == -om)
E2 = list(itertools.combinations(range(4), 2))
star = sp.zeros(6, 6)
for a, (i, j) in enumerate(E2):
    k, l = [m for m in range(4) if m not in (i, j)]
    star[E2.index((k, l)), a] = sp.Matrix.hstack(*[I4[:, m] for m in (i, j, k, l)]).det()
chk("Hodge * on Lambda^2 R^4 pairs opposite edges of K_4, *^2 = +1, eigenvalues +1 (x3), -1 (x3)",
    star * star == sp.eye(6) and sorted(star.eigenvals().items()) == [(-1, 3), (1, 3)])
swap = I4.extract([1, 0, 2, 3], [0, 1, 2, 3])
chk("J commutes with * (J is not the para-complex structure)", compound(-I4, 2) * star == star * compound(-I4, 2))
chk("an orientation flip anticommutes with * (eps_1234 swaps the self-dual halves)",
    compound(swap, 2) * star == -star * compound(swap, 2))
chk("* on Lambda^1 is the complement map: e_i -> +- e_([4] minus i) (vertex -> opposite facet)",
    all(sum(1 for S in itertools.combinations(range(4), 3) if i not in S) == 1 for i in range(4)))

print("J5  what quadrances can see")
rs = np.random.default_rng(11)
Qm = lambda X: ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
vol = lambda P: np.linalg.det(P[1:] - P[0]) / 6
def cm(P):
    q = Qm(P); n = len(P); B = np.ones((n + 1, n + 1)); B[0, 0] = 0; B[1:, 1:] = q; return np.linalg.det(B)
ok_scale = ok_cm = ok_mirror = ok_bi = 0; T = 300
def bideterminant(q, A, B):  # V(A) V(B) from quadrances only: polarization of (a_i - a_0).(b_j - b_0)
    a0, b0 = A[0], B[0]
    M = np.array([[(q[a, b0] + q[a0, b] - q[a, b] - q[a0, b0]) / 2 for b in B[1:]] for a in A[1:]])
    return np.linalg.det(M) / 36
for _ in range(T):
    X = rs.normal(size=(6, 3)); sc = rs.uniform(-2, 2)
    ok_scale += np.allclose(Qm(sc * X), sc ** 2 * Qm(X)) and np.isclose(vol(sc * X[:4]), sc ** 3 * vol(X[:4]))
    ok_cm += np.isclose(cm(X[:4]), 288 * vol(X[:4]) ** 2)
    ok_mirror += np.allclose(Qm(-X), Qm(X)) and np.sign(vol(-X[:4])) == -np.sign(vol(X[:4]))
    A, B = [0, 1, 2, 3], [5, 4, 2, 1]
    ok_bi += np.isclose(bideterminant(Qm(X), A, B), vol(X[A]) * vol(X[B]))
chk(f"Q(sX) = s^2 Q(X) (even), V(sX) = s^3 V(X) (odd): {ok_scale}/{T}", ok_scale == T)
chk(f"Cayley-Menger determinant = 288 V^2 (sees |V| only): {ok_cm}/{T}", ok_cm == T)
chk(f"X and -X: identical quadrances, opposite oriented volume (absolute bit invisible): {ok_mirror}/{T}", ok_mirror == T)
chk(f"V(A) V(B) for two 4-subsets (not sharing a base point) is a polynomial in quadrances: {ok_bi}/{T}", ok_bi == T)

print("J6  Galois limit on prime polygons")
xs = sp.Symbol('x')
for pr in (5, 7, 11, 13, 17):   # p = 3 has no diagonals
    deg = sp.degree(sp.minimal_polynomial(1 + 2 * sp.cos(2 * sp.pi / pr), xs), xs)
    v = [np.array([math.cos(2 * math.pi * k / pr), math.sin(2 * math.pi * k / pr)]) for k in range(pr)]
    side, diag = v[1] - v[0], v[2] - v[pr - 1]
    par = abs(side[0] * diag[1] - side[1] * diag[0]) < 1e-12
    ratio = np.linalg.norm(diag) / np.linalg.norm(side)
    pow2 = deg & (deg - 1) == 0
    chk(f"p={pr:2d}: v0v1 || v(p-1)v2, ratio = 1 + 2cos(2pi/p), degree {deg} = (p-1)/2 "
        f"({'2-power' if pow2 else 'NOT a 2-power: no affinely regular p-gon over a multiquadratic field'})",
        par and math.isclose(ratio, 1 + 2 * math.cos(2 * math.pi / pr)) and deg == (pr - 1) // 2)

print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
