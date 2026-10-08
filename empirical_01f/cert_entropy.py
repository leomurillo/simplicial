"""
Paper 01f Section 11 certificates: the residual entropy of spin ice as an exact frame loop expansion.

E1  Frame projector: delta(sum sigma = 0) = (3/8)(1 + sum_(i<j) G_ij s_i s_j + s1 s2 s3 s4), G_ij = v_i.v_j = -1/3.
E2  Loop expansion is exact: periodic diamond tori L = 1, 2 give 6 and 2970 ice states from both sides;
    all loop weights are positive (bipartite) so Pauling is a lower bound.
E3  The cluster engine (loopgas.py) is validated exactly: (a) on a finite diamond fragment, cluster sum ==
    log of the exact cycle-space generating function through order 18 (rational arithmetic, incl. 3-clusters);
    (b) on square ice, cluster series == exact transfer-matrix ln Z(x) coefficients of a 10x10 torus, orders 4-8.
E4  Lattice series per spin through order K (default 18; pass 20 to recompute order 20).
E5  Debye-Hueckel asymptotics a_n ~ C k^-5/2 (k = n/2) from the dilute monopole plasma; tail and S.
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
from collections import Counter, deque, defaultdict
import numpy as np
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0])
from loopgas import Lattice, nbrs_dia, cluster_series, verts, edge, weight

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")
K = int(sys.argv[1]) if len(sys.argv) > 1 else 18

print("E1  the frame projector")
G = -Fr(1, 3); ok = True
for s in itertools.product([1, -1], repeat=4):
    ok &= Fr(1 if sum(s) == 0 else 0) == Fr(3, 8) * (1 + sum(G * s[i] * s[j] for i in range(4) for j in range(i + 1, 4)) + s[0] * s[1] * s[2] * s[3])
chk("delta(sum sigma=0) = 3/8 (1 + sum G_ij s_i s_j + prod s) with G_ij = cos(tetrahedral angle) = -1/3 (all 16 states)", ok)

print("E2  exact loop expansion on periodic tori")
def torus(L):
    cells = list(itertools.product(range(L), repeat=3)); cid = {c: i for i, c in enumerate(cells)}
    dvec = [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    return len(cells), [(cid[c], cid[tuple((c[k] + dvec[n][k]) % L for k in range(3))]) for c in cells for n in range(4)]
def exact_count(nv, bonds):
    ice = [s for s in itertools.product([1, -1], repeat=4) if sum(s) == 0]
    states = {tuple([0] * nv): 1}; left = [4] * nv
    for a in range(nv):
        mine = [(n, bonds[4 * a + n][1]) for n in range(4)]
        for n, b in mine: left[b] -= 1
        new = defaultdict(int)
        for st, w in states.items():
            for s in ice:
                lst = list(st)
                for (n, b), x in zip(mine, s): lst[b] += x
                if any(abs(lst[b]) > left[b] for b in range(nv)): continue
                new[tuple(lst)] += w
        states = new
    return sum(states.values())
def loop_sum(nv, bonds):
    V = 2 * nv; E = [(a, nv + b) for a, b in bonds]; ne = len(E)
    adj = defaultdict(list)
    for i, (u, v) in enumerate(E): adj[u].append((v, i)); adj[v].append((u, i))
    par = {0: None}; pe = {}; dq = deque([0]); tree = set()
    while dq:
        u = dq.popleft()
        for v, i in adj[u]:
            if v not in par: par[v] = u; pe[v] = i; tree.add(i); dq.append(v)
    def path(v):
        m = 0
        while par[v] is not None: m ^= 1 << pe[v]; v = par[v]
        return m
    basis = [(1 << i) ^ path(E[i][0]) ^ path(E[i][1]) for i in range(ne) if i not in tree]
    tot, allpos = Fr(0), True
    for k in range(1 << len(basis)):
        m = 0; kk = k; j = 0
        while kk:
            if kk & 1: m ^= basis[j]
            kk >>= 1; j += 1
        deg = [0] * V
        for i in range(ne):
            if m >> i & 1: u, v = E[i]; deg[u] += 1; deg[v] += 1
        n2 = sum(1 for x in deg if x == 2); w = Fr(-1, 3)**n2; allpos &= w > 0; tot += w
    return tot, allpos
for L, expect in ((1, 6), (2, 2970)):
    nv, bonds = torus(L); c = exact_count(nv, bonds); s, allpos = loop_sum(nv, bonds)
    pref = Fr(2)**len(bonds) * Fr(3, 8)**(2 * nv)
    chk(f"L={L} torus ({len(bonds)} spins): exact count {c} = loop expansion {pref * s}; every loop weight (-1/3)^n2 > 0; Pauling {float(pref):.2f} <= count",
        c == expect and pref * s == c and allpos and pref <= c)

print("E3  validation of the cluster engine")
O = (0, 0, 0, 0); base = Lattice(nbrs_dia); Gf = set()
for h in base.cycles_through(O, 6): Gf |= h
for u in nbrs_dia(O)[:2]:
    for h in base.cycles_through(u, 6): Gf |= h
Vf = verts(Gf); Eind = sorted({edge(v, w) for v in Vf for w in nbrs_dia(v) if w in Vf})
idx = {e: i for i, e in enumerate(Eind)}; adj = {v: [] for v in Vf}
for (a, b) in Eind: adj[a].append(b); adj[b].append(a)
root = min(Vf); par = {root: None}; dq = deque([root]); tree = set()
while dq:
    v = dq.popleft()
    for w in adj[v]:
        if w not in par: par[w] = v; tree.add(edge(v, w)); dq.append(w)
def ptr(v):
    m = 0
    while par[v] is not None: m ^= 1 << idx[edge(v, par[v])]; v = par[v]
    return m
basis = [(1 << idx[e]) ^ ptr(e[0]) ^ ptr(e[1]) for e in Eind if e not in tree]
Kf = 18; poly = Counter()
for mask in range(1 << len(basis)):
    m = 0; mm = mask; i = 0
    while mm:
        if mm & 1: m ^= basis[i]
        mm >>= 1; i += 1
    es = [Eind[j] for j in range(len(Eind)) if m >> j & 1]
    if len(es) <= Kf: poly[len(es)] += weight(frozenset(es))
cc = [poly.get(k, Fr(0)) for k in range(Kf + 1)]; Lg = [Fr(0)] * (Kf + 1)
for n in range(1, Kf + 1): Lg[n] = cc[n] - sum(Fr(k, n) * Lg[k] * cc[n - k] for k in range(1, n))
cl = cluster_series(Lattice(nbrs_dia, allowed=Vf), [(v, Fr(1)) for v in Vf], Kf, Kf)
chk(f"finite fragment (V={len(Vf)}, cycle space 2^{len(basis)}): cluster sum = log of exact generating function, orders 6..18, exact rationals",
    all(Lg[n] == cl.get(n, 0) for n in range(Kf + 1)))
def lnZ_sq(x, L=10):
    sp = np.array([1, -1]); W = np.zeros((2, 2, 2, 2), complex)
    for a, b, c, d in itertools.product(range(2), repeat=4):
        s = [sp[a], sp[b], sp[c], sp[d]]
        W[a, b, c, d] = (1 - (x / 3) * sum(s[i] * s[j] for i in range(4) for j in range(i + 1, 4)) + x * x * np.prod(s)) / 4
    st = np.array(list(itertools.product(range(2), repeat=L))); n = len(st)
    P = np.broadcast_to(np.eye(2, dtype=complex), (n, n, 2, 2)).copy()
    for j in range(L): P = P @ W[st[:, j][:, None], st[:, j][None, :]]
    return np.log(np.sum(np.linalg.eigvals(np.trace(P, axis1=2, axis2=3))**L))
M, r, Ls = 64, 0.35, 10
vals = np.array([lnZ_sq(r * np.exp(2j * np.pi * m / M)) for m in range(M)]); co = np.fft.fft(vals) / M
torus_c = [(co[k] / r**k).real / (2 * Ls * Ls) for k in range(9)]
def nbrs_sq(v): i, j = v[0], v[1]; return [(i + 1, j, 0, 0), (i - 1, j, 0, 0), (i, j + 1, 0, 0), (i, j - 1, 0, 0)]
sq = cluster_series(Lattice(nbrs_sq, girth=4), [((0, 0, 0, 0), Fr(1))], 8, 8)
chk(f"square ice: cluster series per edge {[round(float(sq[k]) / 2, 10) for k in (4, 6, 8)]} = exact torus {[round(torus_c[k], 10) for k in (4, 6, 8)]}",
    all(abs(float(sq[k]) / 2 - torus_c[k]) < 1e-9 for k in (4, 6, 8)))

print(f"E4  the diamond series through order {K}")
t0 = time.time(); B0 = (1, 0, 0, 0); lat = Lattice(nbrs_dia); CS = K - 6
res = cluster_series(lat, [(O, Fr(1, 2)), (B0, Fr(1, 2))], K, CS)
for rt in (O, B0):
    cnt = Counter(); lat.cycles_through(rt, K, store=False, counts=cnt)
    for l, c in cnt.items():
        if l > CS: res[l] += Fr(1, 2) * c / Fr(3)**l / l
terms = {k: float(res[k]) / 2 for k in sorted(res)}
S = 0.5 * math.log(1.5)
for k, t in terms.items():
    S += t; print(f"      order {k:2d}: {t:.6e}   S = {S:.8f}")
print(f"      ({time.time()-t0:.0f}s)")
known = {6: 1.3717421124828532e-03, 8: 2.2862368541380887e-04, 10: 2.0322105370116343e-04, 12: 1.5523834e-04, 14: 9.0948e-05, 16: 7.0336e-05, 18: 5.3088e-05}
chk("series terms reproduce the recorded values (orders 6..18) and every term is positive",
    all(abs(terms[k] - v) / v < 1e-4 for k, v in known.items() if k <= K) and all(t > 0 for t in terms.values()))
chk("order 6 = hexagons: exactly one per spin, weight 3^-6", terms[6] == float(Fr(1, 729)))

print("E5  Debye-Hueckel tail")
from mpmath import mp, zeta
mp.dps = 30
N = max(terms); ks = [N // 2 - 1, N // 2]
Mx = np.array([[k**-2.5, k**-3.5] for k in ks]); cs = np.linalg.solve(Mx, [terms[2 * k] for k in ks])
tail2 = float(cs[0] * zeta(mp.mpf(2.5), N // 2 + 1) + cs[1] * zeta(mp.mpf(3.5), N // 2 + 1))
C1 = terms[N] * (N // 2)**2.5; tail1 = float(C1 * zeta(mp.mpf(2.5), N // 2 + 1))
S1, S2 = S + tail1, S + tail2
kol = 0.5 * math.log(1.5074660)
print(f"      partial {S:.7f}; DH 1-term tail {tail1:.3e} -> S = {S1:.6f}; DH 2-term tail {tail2:.3e} -> S = {S2:.6f}")
print(f"      references: Kolafa 2014 (Ic) {kol:.6f}; Nagle 1966 {0.5*math.log(1.50685):.6f}; Singh-Oitmaa NLC 0.205507")
chk("DH-extrapolated S lies within 2e-5 of Kolafa's Monte Carlo value and excludes Nagle (low) and the NLC value (high)",
    abs(S2 - kol) < 2e-5 and abs(S1 - kol) < 2e-5 and S2 - 0.5 * math.log(1.50685) > 1e-4 and 0.205507 - S2 > 2e-4)
if K >= 20:
    pred2 = 4.1220e-05      # recorded in entropy_prediction_a20.txt before the order-20 run
    chk(f"pre-registered order-20 prediction: 2-term DH {pred2:.4e} vs computed {terms[20]:.4e} (within 1%)", abs(terms[20] - pred2) / terms[20] < 0.01)

print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
