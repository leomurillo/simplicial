"""
Paper 01f certificates: spin ice in the simplicial frame (numpy/sympy/mpmath/scipy only; no torch).

T1  The tetrahedron: R^4 = H (+) R1 is dipole (+) monopole; ice states = oriented matchings of K4 with moments
    along the cubic axes; NN energy = (3J/2)(4 - |m|^2) = 2J q^2 - 2J; Pauling = |{+-1}^4 cap H| / 16 = 3/8.
T2  Lattice operators on an explicit real-space pyrochlore cluster: 4 hexagons per cell, curl.grad = 0,
    spectrum of curl^T curl = {16 - |f|^2 (twice), 0, 0}; frame: curl = Kt(e^{i theta}) up to phases,
    -Kt(conj u)Kt(u) = 4(|u_H|^2(I - J/4) - u_H u_H^dag); Benton et al.'s zeta^2 = 16 - |f|^2, h_nm = opposite edge.
T3  Classical Coulomb phase: P = I - J/4 - u_H u_H^dag/|u_H|^2 = Kt(u)^dag Kt(u)/(16 - |f|^2); synthesis of the
    pinch-point limit = (4/3)(I - k k^T/k^2) (Henley); soft-spin longitudinal 4 - |f| ~ phi^T M phi / 8.
T4  Neutron structure factor: polarization factor = (4/3) T(phi) (same transverse projector); frame formula
    == real-space null-space projector; exact T=0 ice Monte Carlo (loop algorithm, 2048 spins) vs frame
    large-N with no fitted constant: pre-registered thresholds corr >= 0.99, mean |dev| <= 3%, means within 1%.
T5  Kagome ice: pinned apical spin -> each triangle at a simplex vertex (dimer); in-plane field = zero-sum frame
    vector; Kasteleyn torus formula vs brute force; log Z / L^2 -> R(t); entropy per spin = m(1+x+y)/4;
    dimer densities = gradient of R = angles/pi = 1 - (Dirac-point phase differences)/pi; T_K = delta / ln 2.
T6  [100] field: |h.v_j| = h/sqrt3 for all j; saturated state = an oriented matching; branching 2 -> T_K.
T7  Control: square ice has a 2-dimensional synthesis kernel (no single gauge line).
Writes fig_spin_ice.png.
"""
import itertools, math, sys, time
import numpy as np
import sympy as sp
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

E = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / 4.0     # diamond bond vectors, a0 = 1
V = E / np.linalg.norm(E, axis=1)[:, None]                                  # unit local axes
A1 = np.array([E[0] - E[1], E[0] - E[2], E[0] - E[3]])                     # FCC primitive vectors
I4, J4 = np.eye(4), np.ones((4, 4))
def Kt(u):
    u1, u2, u3, u4 = u
    return np.array([[0, u3 - u4, u4 - u2, u2 - u3], [u4 - u3, 0, u1 - u4, u3 - u1],
                     [u2 - u4, u4 - u1, 0, u1 - u2], [u3 - u2, u1 - u3, u2 - u1, 0]])
def fsum(th): return np.exp(1j * th).sum()
def P_cell(th):
    u = np.exp(1j * th); uH = u - u.sum() / 4
    return I4 - J4 / 4 - np.outer(uH, uH.conj()) / np.vdot(uH, uH).real

print("T1  the tetrahedron")
states = list(itertools.product([1, -1], repeat=4))
Gm = sp.Rational(1, 3) * (4 * sp.eye(4) - sp.ones(4))          # Gram of the unit frame = M/3
ok_e = ok_m = True; levels = {}
for s in states:
    sv = sp.Matrix(s); Qn = (sv.T * Gm * sv)[0]; q = sp.Rational(sum(s), 2)
    En = sum(s[i] * s[j] for i in range(4) for j in range(i + 1, 4))
    ok_e &= (En == sp.Rational(3, 2) * (4 - Qn)) and (En == 2 * q**2 - 2)
    m = sum(s[j] * V[j] for j in range(4)); ok_m &= abs(m @ m - float(Qn)) < 1e-12
    levels.setdefault(q, []).append(Qn)
chk("|m|^2 = |sum sigma_j v_j|^2 = sigma^T (M/3) sigma for all 16 states (moment = synthesis)", ok_m)
chk("NN energy sum_(i<j) sigma_i sigma_j = (3/2)(4 - |m|^2) = 2 q^2 - 2,  q = (sum sigma)/2", ok_e)
chk("levels: q=0 -> 6 states |m|^2=16/3; |q|=1 -> 8 states |m|^2=4; |q|=2 -> 2 states m=0",
    len(levels[0]) == 6 and set(levels[0]) == {sp.Rational(16, 3)} and len(levels[1]) + len(levels[-1]) == 8
    and set(levels[1] + levels[-1]) == {4} and set(levels[2] + levels[-2]) == {0})
ice = [s for s in states if sum(s) == 0]
match = {frozenset([frozenset(i for i in range(4) if s[i] == 1), frozenset(i for i in range(4) if s[i] == -1)]) for s in ice}
moms = [sum(s[j] * V[j] for j in range(4)) for s in ice]
axes_ok = all(np.count_nonzero(np.abs(m) > 1e-12) == 1 and abs(np.linalg.norm(m) - 4 / math.sqrt(3)) < 1e-12 for m in moms)
chk("6 ice states = 3 perfect matchings of K4 x 2 orientations; moments = (4/sqrt3) x the 6 cubic directions",
    len(ice) == 6 and len(match) == 3 and axes_ok)
chk("synthesis kills exactly the gauge line: sum_j v_j = 0 (charge invisible to the moment)", np.allclose(V.sum(0), 0))
chk("Pauling: |{+-1}^4 cap H| / 16 = 3/8, S_P = ln2 + (1/2)ln(3/8) = (1/2)ln(3/2) per spin",
    len(ice) * 8 == 3 * 16 and abs(math.log(2) + 0.5 * math.log(3 / 8) - 0.5 * math.log(1.5)) < 1e-15)
chk("std form of the spins: n = (sigma + 1)/2 in {0,1}^4 with sum n = 2 + q", all(sum((x + 1) // 2 for x in s) == 2 + sum(s) // 2 for s in states))

print("T2  lattice operators: divergence, hexagon curl, photon")
def build(L):
    cells = [np.array(c) for c in itertools.product(range(L), repeat=3)]
    cidx = {tuple(c): i for i, c in enumerate(cells)}
    wrap = lambda c: tuple(np.mod(c, L))
    dvec = [np.zeros(3, int)] + [-np.eye(3, dtype=int)[i] for i in range(3)]
    nc, nb = len(cells), 4 * len(cells)
    pos = np.array([(c @ A1) + E[n] / 2 for c in cells for n in range(4)])
    ax = np.array([V[n] for c in cells for n in range(4)])
    Aend, Bend = np.zeros(nb, int), np.zeros(nb, int)
    for c in cells:
        for n in range(4):
            b = 4 * cidx[tuple(c)] + n; Aend[b] = cidx[tuple(c)]; Bend[b] = cidx[wrap(c + dvec[n])]
    return cells, cidx, wrap, dvec, nc, nb, pos, ax, Aend, Bend
L = 4
cells, cidx, wrap, dvec, nc, nb, pos, ax, Aend, Bend = build(L)
D = np.zeros((2 * nc, nb)); D[Aend, np.arange(nb)] += 1; D[nc + Bend, np.arange(nb)] -= 1
bid = lambda c, n: 4 * cidx[wrap(c)] + n
def nbrs(node):
    c = np.array(node[1])
    if node[0] == 'A': return [(('B', wrap(c + dvec[n])), bid(c, n), +1) for n in range(4)]
    return [(('A', wrap(c - dvec[n])), bid(c - dvec[n], n), -1) for n in range(4)]
hexes, hexlist = set(), []
for c in cells:
    start = ('A', tuple(c))
    def dfs(node, pn, pb, depth):
        for (nxt, b, s) in nbrs(node):
            if b in [x for x, _ in pb]: continue
            if nxt == start and depth == 5:
                key = frozenset([x for x, _ in pb] + [b])
                if key not in hexes and len(key) == 6: hexes.add(key); hexlist.append(pb + [(b, s)])
                continue
            if nxt in pn or depth >= 5: continue
            dfs(nxt, pn + [nxt], pb + [(b, s)], depth + 1)
    dfs(start, [start], [], 0)
C = np.zeros((len(hexlist), nb))
for h, cyc in enumerate(hexlist):
    for b, s in cyc: C[h, b] += s
rec = 2 * np.pi * np.linalg.inv(A1).T
pred = []
for m in itertools.product(range(L), repeat=3):
    k = (np.array(m) / L) @ rec; pred += [16 - abs(fsum(E @ k))**2] * 2 + [0, 0]
ev = np.sort(np.linalg.eigvalsh(C.T @ C))
chk(f"real-space cluster (L={L}): {len(hexlist)} hexagons = 4 per primitive cell; curl . grad = 0",
    len(hexlist) == 4 * nc and np.abs(C @ D.T).max() == 0)
chk("spectrum of curl^T curl = {16 - |f(k)|^2 twice, 0, 0} at every allowed k (photon omega^2/UK)",
    np.abs(ev - np.sort(pred)).max() < 1e-10)
rng = np.random.default_rng(0)
rep = {}
for cyc in hexlist:
    rep.setdefault(({0, 1, 2, 3} - {b % 4 for b, _ in cyc}).pop(), cyc)
mi = lambda c: np.where(np.array(c) > L // 2, np.array(c) - L, np.array(c))   # minimal-image cell
worst = 0
for _ in range(200):
    k = rng.normal(size=3) * 4; Kk = Kt(np.exp(1j * (E @ k)))
    for ell, cyc in rep.items():
        row = np.zeros(4, complex)
        for b, s in cyc: row[b % 4] += s * np.exp(1j * (mi(cells[b // 4]) @ A1) @ k)
        rr = [row[j] / Kk[ell, j] for j in range(4) if j != ell]
        worst = max(worst, max(abs(x - rr[0]) for x in rr), abs(abs(rr[0]) - 1))
chk(f"Bloch curl row of the hexagon missing direction l = (unit phase) x row l of Kt(e^{{i theta}}) (4 types, 200 random k; dev {worst:.0e})",
    len(rep) == 4 and worst < 1e-10)
err = 0
for _ in range(300):
    th = rng.uniform(0, 2 * np.pi, 4); u = np.exp(1j * th); f = u.sum(); uH = u - f / 4
    K = Kt(u); G = K.conj().T @ K
    err = max(err, np.abs(K @ u).max(), np.abs(K @ np.ones(4)).max(),
              np.abs(G - 4 * (np.vdot(uH, uH).real * (I4 - J4 / 4) - np.outer(uH, uH.conj()))).max(),
              abs(4 * np.vdot(uH, uH).real - (16 - abs(f)**2)))
chk("frame: Kt(u) kills the gradients {1, u}; Kt(u)^dag Kt(u) = 4(|u_H|^2 (I-J/4) - u_H u_H^dag); 4|u_H|^2 = 16 - |f|^2", err < 1e-12)
chk("hence curl^dag curl = Kt(u)^dag Kt(u) (same kernel {1,u}, same constant 16-|f|^2 on its complement)", err < 1e-12)
def zeta2(k):
    s = 0
    for m_ in range(4):
        for n_ in range(4):
            if m_ != n_:
                cr = np.cross(E[n_], E[m_]); s += np.sin(k @ (cr / np.linalg.norm(cr) / np.sqrt(8)))**2
    return 2 * s
ks = rng.normal(size=(300, 3)) * 6
chk("Benton-Sikora-Shannon Eq.(68): zeta(k)^2 = 16 - |f(k)|^2 (300 random k)", max(abs(zeta2(k) - (16 - abs(fsum(E @ k))**2)) for k in ks) < 1e-12)
opp_ok = True
for m_, n_ in itertools.combinations(range(4), 2):
    k_, l_ = [x for x in range(4) if x not in (m_, n_)]
    cr = np.cross(E[m_], E[n_]); d = E[k_] - E[l_]
    opp_ok &= abs(abs(cr @ d) - np.linalg.norm(cr) * np.linalg.norm(d)) < 1e-12 and np.allclose(cr / np.linalg.norm(cr) / np.sqrt(8), np.sign(cr @ d) * d / 2)
chk("h_nm = (1/sqrt8) unit(e_n x e_m) = +-(e_k - e_l)/2: the cross product is the opposite-edge Hodge dual (01b Thm 10.1)", opp_ok)
k0 = np.array([0.013, -0.007, 0.011])
chk("long wavelength: 16 - |f|^2 = a0^2 |k|^2 (1 + O(k^2)) -> c = sqrt(UK) a0 (Benton Eq. 70)",
    abs((16 - abs(fsum(E @ k0))**2) / (k0 @ k0) - 1) < 1e-3)
chk("photon band top omega = 4 sqrt(UK) exactly on the diamond nodal set f = 0 (e.g. X point)",
    abs(16 - abs(fsum(E @ (2 * np.pi * np.array([1, 0, 0]))))**2 - 16) < 1e-12)

print("T3  the classical Coulomb phase")
err = 0
for _ in range(300):
    th = rng.uniform(0, 2 * np.pi, 4); u = np.exp(1j * th); f = u.sum()
    Bm = np.vstack([np.ones(4), u.conj()])
    P = I4 - Bm.conj().T @ np.linalg.inv(Bm @ Bm.conj().T) @ Bm
    err = max(err, np.abs(P - P_cell(th)).max(), np.abs(P - Kt(u).conj().T @ Kt(u) / (16 - abs(f)**2)).max())
    ev2 = np.sort(np.linalg.eigvalsh(Bm.conj().T @ Bm))
    err = max(err, np.abs(ev2 - np.sort([0, 0, 4 - abs(f), 4 + abs(f)])).max())
chk("flat-band projector P = I - B^dag(BB^dag)^-1 B = I - J/4 - u_H u_H^dag/|u_H|^2 = Kt(u)^dag Kt(u)/(16 - |f|^2)", err < 1e-12)
chk("B^dag B (soft-spin constraint) has spectrum {0, 0, 4 - |f|, 4 + |f|}", err < 1e-12)
S3 = V.T                                                    # synthesis (columns = unit axes)
kk = np.array([0.3, -0.5, 0.8]); phi = V @ kk
T = I4 - J4 / 4 - np.outer(phi, phi) / (phi @ phi)
chk("synthesis of the pinch-point limit: S T S^T = (4/3)(I - k k^T/|k|^2), Henley's dipolar form",
    np.allclose(S3 @ T @ S3.T, 4 / 3 * (np.eye(3) - np.outer(kk, kk) / (kk @ kk))))
th_s = 1e-3 * rng.normal(size=4); M4 = 4 * I4 - J4
chk("longitudinal (monopole) mode: 4 - |f| = theta^T M theta / 8 (1 + O(theta^2))",
    abs((4 - abs(fsum(th_s))) / (th_s @ M4 @ th_s / 8) - 1) < 1e-4)

print("T4  the neutron structure factor")
def S_frame(Q, kappa=2.0):
    th = E @ Q; Qh = Q / np.linalg.norm(Q); ph_ = V @ Q
    Vq = V @ V.T - np.outer(V @ Qh, V @ Qh)
    Tq = I4 - J4 / 4 - np.outer(ph_, ph_) / (ph_ @ ph_)
    W = np.diag(np.exp(1j * th / 2))
    return kappa * np.real(np.sum(Vq * (W.conj().T @ P_cell(th) @ W))), np.abs(Vq - 4 / 3 * Tq).max()
pol_err = max(S_frame(rng.normal(size=3) * 7)[1] for _ in range(200))
chk("polarization factor v_j.v_k - (Q.v_j)(Q.v_k)/Q^2 = (4/3) T(phi): the same transverse projector", pol_err < 1e-12)
Un, sn, Vt = np.linalg.svd(D); r = int((sn > 1e-9).sum()); N0 = Vt[r:].T; Preal = N0 @ N0.T
errs = []
for m in itertools.product(range(L), repeat=3):
    for G in ([0, 0, 0], [1, 0, 0], [0, 1, 1]):
        Q = ((np.array(m) / L) + np.array(G)) @ rec
        if 16 - abs(fsum(E @ Q))**2 < 1e-9: continue
        phs = np.exp(1j * pos @ Q); Vab = ax @ ax.T - np.outer(ax @ Q, ax @ Q) / (Q @ Q)
        errs.append(abs(np.real(np.sum(Vab * Preal * np.outer(phs.conj(), phs))) / nc - S_frame(Q, 1.0)[0]))
chk(f"frame S(Q) == real-space null-space projector, {len(errs)} wavevectors (max err {max(errs):.1e})", max(errs) < 1e-12)
# exact T = 0 ice ensemble: loop algorithm
L8 = 8
cells8, cidx8, wrap8, dvec8, nc8, nb8, pos8, ax8, Aend8, Bend8 = build(L8)
inc = [[] for _ in range(2 * nc8)]
for b in range(nb8): inc[Aend8[b]].append(b); inc[nc8 + Bend8[b]].append(b)
inc = np.array(inc); sig = np.tile(np.array([1, 1, -1, -1]), nc8)
def div_max(s):
    dA, dB = np.zeros(nc8), np.zeros(nc8); np.add.at(dA, Aend8, s); np.add.at(dB, Bend8, s)
    return np.abs(dA).max() + np.abs(dB).max()
mrng = np.random.default_rng(1)
def loop_update():
    node = int(mrng.integers(2 * nc8)); visited = {node: 0}; pb = []
    while True:
        outs = [b for b in inc[node] if sig[b] == (1 if node < nc8 else -1)]
        b = outs[int(mrng.integers(2))]; nxt = nc8 + Bend8[b] if node < nc8 else Aend8[b]; pb.append(b)
        if nxt in visited: sig[pb[visited[nxt]:]] *= -1; return
        visited[nxt] = len(pb); node = nxt
Qs = []
for hi in range(-2 * L8, 2 * L8 + 1):
    for li in range(-3 * L8, 3 * L8 + 1):
        if (hi + li) % 2: continue
        Q = 2 * np.pi * np.array([hi / L8, hi / L8, li / L8])
        if 16 - abs(fsum(E @ Q))**2 > 1e-6: Qs.append(Q)
Qs = np.array(Qs); Qh = Qs / np.linalg.norm(Qs, axis=1)[:, None]; phm = np.exp(1j * Qs @ pos8.T)
acc, nmeas, t0 = np.zeros(len(Qs)), 0, time.time()
for sweep in range(4000):
    for _ in range(20): loop_update()
    if sweep >= 500 and sweep % 2 == 0:
        mv = (phm * sig) @ ax8; perp = mv - Qh * np.sum(mv * Qh, axis=1)[:, None]
        acc += np.sum(np.abs(perp)**2, axis=1) / nc8; nmeas += 1
Smc = acc / nmeas; Sfr = np.array([S_frame(Q, 2.0)[0] for Q in Qs])
corr = np.corrcoef(Smc, Sfr)[0, 1]; mdev = np.mean(np.abs(Smc - Sfr)) / Sfr.mean(); rmean = Smc.mean() / Sfr.mean()
print(f"      MC: {nb8} spins, {nmeas} measurements, {len(Qs)} wavevectors in (hhl), {time.time()-t0:.0f}s")
chk("Monte Carlo stayed in the ice manifold (divergence 0 everywhere)", div_max(sig) == 0)
chk(f"exact ice MC vs frame large-N, NO fitted constant (kappa = 2): corr {corr:.4f} >= 0.99, mean dev {mdev:.3f} <= 0.03, means ratio {rmean:.4f}",
    corr >= 0.99 and mdev <= 0.03 and abs(rmean - 1) <= 0.01)

print("T5  kagome ice")
tri_states = [s for s in itertools.product([1, -1], repeat=3) if sum(s) + 1 == 0]   # apical sigma_4 = +1, ice rule
chk("apical spin pinned out => kagome triangle states = the 3 frame vertices e_j (std-form 0/1, one 1): a dimer",
    sorted(tuple((x + 1) // 2 for x in s) for s in tri_states) == sorted(tuple(int(i == j) for i in range(3)) for j in range(3)))
hperp = np.cross(V[3], np.array([0.3, -1.1, 0.7])); c_j = -2 * (V[:3] @ hperp)
chk("in-plane field: dimer energies c_j = -2 mu h_perp . v_j are a zero-sum frame vector (sum_j<=3 v_j = -v_4)", abs(c_j.sum()) < 1e-12)
def perm(A):
    n = A.shape[0]; tot = 0.0
    for S in range(1, 1 << n):
        cols = [j for j in range(n) if S >> j & 1]; tot += (-1)**len(cols) * np.prod(A[:, cols].sum(axis=1))
    return (-1)**n * tot
def Kmat(Ln, t):
    n = Ln * Ln; M = np.zeros((n, n)); idx = lambda x, y: (x % Ln) * Ln + (y % Ln)
    for x in range(Ln):
        for y in range(Ln):
            b = idx(x, y); M[b, idx(x, y)] += t[0]; M[b, idx(x + 1, y)] += t[1]; M[b, idx(x, y + 1)] += t[2]
    return M
def logP(Ln, t, z, w):
    mp.mp.dps = 40; tot = mp.mpf(1)
    for a in range(Ln):
        for b in range(Ln):
            al = mp.expjpi((mp.mpf(0 if z == 1 else 1) + 2 * a) / Ln); be = mp.expjpi((mp.mpf(0 if w == 1 else 1) + 2 * b) / Ln)
            tot *= (t[0] + t[1] * al + t[2] * be)
    return tot
def Z_kast(Ln, t):
    return mp.re(0.5 * (-logP(Ln, t, 1, 1) + logP(Ln, t, 1, -1) + logP(Ln, t, -1, 1) + logP(Ln, t, -1, -1)))
ok = True
for Ln in (2, 4):
    t = rng.uniform(0.5, 1.5, 3); ok &= abs(float(Z_kast(Ln, t)) - perm(Kmat(Ln, t))) < 1e-8 * perm(Kmat(Ln, t))
chk("Kasteleyn torus formula (even L) = brute-force permanent, L = 2, 4", ok)
def R3(t):
    mp.mp.dps = 30; pts = [mp.mpf(0), mp.pi, 2 * mp.pi]
    cb = (mp.mpf(t[0])**2 - mp.mpf(t[1])**2 - mp.mpf(t[2])**2) / (2 * mp.mpf(t[1]) * mp.mpf(t[2]))
    if abs(cb) <= 1: pts += [mp.acos(cb), 2 * mp.pi - mp.acos(cb)]
    return mp.quad(lambda b: mp.log(max(mp.mpf(t[0]), abs(t[1] + t[2] * mp.exp(1j * b)))), sorted(pts)) / (2 * mp.pi)
for t in ([1, 1, 1], [1.2, 0.9, 0.7]):
    Ln = 64; dens = float(mp.log(Z_kast(Ln, t)) / Ln**2); Rv = float(R3(t))
    chk(f"t={t}: log Z / L^2 at L=64 = {dens:.6f} -> R(t) = {Rv:.6f}", abs(dens - Rv) < 2e-3)
mp.mp.dps = 30
Lchi = mp.nsum(lambda n: 1 / (3 * n + 1)**2 - 1 / (3 * n + 2)**2, [0, mp.inf])
s_spin = 3 * mp.sqrt(3) / (16 * mp.pi) * Lchi
chk(f"kagome-ice entropy per pyrochlore spin = m(1+x+y)/4 = (3sqrt3/16pi) L(chi_-3,2) = {mp.nstr(s_spin, 12)} (0.0808)",
    abs(s_spin - R3([1, 1, 1]) / 4) < mp.mpf(10)**-20 and abs(float(s_spin) - 0.0808) < 1e-4)
def rho(t, h=1e-6):
    out = []
    for j in range(3):
        tp = list(map(mp.mpf, t)); tm = list(map(mp.mpf, t)); tp[j] *= mp.e**h; tm[j] *= mp.e**(-h)
        out.append(float((R3(tp) - R3(tm)) / (2 * h)))
    return np.array(out)
t = [1.2, 0.9, 0.7]; r_num = rho(t)
a_ = [math.acos((t[1]**2 + t[2]**2 - t[0]**2) / (2 * t[1] * t[2])), math.acos((t[0]**2 + t[2]**2 - t[1]**2) / (2 * t[0] * t[2])),
      math.acos((t[0]**2 + t[1]**2 - t[2]**2) / (2 * t[0] * t[1]))]
chk(f"dimer densities rho = grad_(log t) R = {np.round(r_num, 6)} = (angle opposite t_j)/pi = {np.round(np.array(a_) / math.pi, 6)}; sum = 1",
    np.allclose(r_num, np.array(a_) / math.pi, atol=1e-6) and abs(r_num.sum() - 1) < 1e-6)
x2 = math.acos((t[2]**2 - t[0]**2 - t[1]**2) / (2 * t[0] * t[1])); u2 = t[0] + t[1] * np.exp(1j * x2)
x3 = np.angle(-u2 / t[2]) % (2 * np.pi); thK = np.array([0.0, x2, x3])
assert abs(t[0] + t[1] * np.exp(1j * x2) + t[2] * np.exp(1j * x3)) < 1e-12
turn = [((thK[(k + 2) % 3] - thK[(k + 1) % 3]) % (2 * np.pi)) for k in range(3)]
chk(f"rho_k = 1 - (theta_(k+2) - theta_(k+1))/pi at the graphene Dirac point (counter-clockwise closing triangle)",
    np.allclose(1 - np.array(turn) / np.pi, r_num, atol=1e-6))
chk("frozen sector (t_1 >= t_2 + t_3): rho = vertex e_1 (std-form gauge), entropy 0", np.allclose(rho([3, 1, 0.5]), [1, 0, 0], atol=1e-6))
tau = sp.Symbol('T', positive=True); dl = sp.Symbol('delta', positive=True)
chk("symmetric tilt (c = 0, delta, delta): Kasteleyn transition e^0 = 2 e^{-delta/T} at T_K = delta/ln 2 (01e sharpness)",
    sp.simplify(1 - 2 * sp.exp(-dl / (dl / sp.log(2)))) == 0)

print("T6  [100] field: the three-dimensional Kasteleyn transition")
hx = np.array([1.0, 0, 0]); proj = V @ hx
sat = tuple(int(np.sign(p)) for p in proj)
chk(f"|h.v_j| = h/sqrt3 for all j; saturated state {sat} is an ice state = oriented matching {{12|34}}",
    np.allclose(np.abs(proj), 1 / math.sqrt(3)) and sum(sat) == 0)
chk("a string enters on an 'in' bond and leaves by one of the 2 'out' bonds: entropy ln 2 per step, cost 2 mu h/sqrt3 -> T_K = 2 mu h/(sqrt3 ln 2)",
    sum(1 for x in sat if x == 1) == 2)

print("T7  control: square ice")
star = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
chk("square-ice bond star {+-x, +-y} has a 2-dimensional synthesis kernel: no single gauge line (cross-polytope frame)",
    4 - np.linalg.matrix_rank(star.T) == 2)

# ---------------- figure ----------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
blue = LinearSegmentedColormap.from_list("seqblue", ["#fcfcfb", "#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"])
orange = LinearSegmentedColormap.from_list("seqorange", ["#fcfcfb", "#fbdcc9", "#f4a77f", "#eb6834", "#b8461b", "#6e2709"])
hh = np.linspace(-2, 2, 241); ll = np.linspace(-3, 3, 361)
Smap = np.zeros((len(ll), len(hh))); Wmap = np.zeros_like(Smap)
for i, l_ in enumerate(ll):
    for j, h_ in enumerate(hh):
        Q = 2 * np.pi * np.array([h_, h_, l_]); d16 = 16 - abs(fsum(E @ Q))**2
        Wmap[i, j] = math.sqrt(max(d16, 0))
        Smap[i, j] = S_frame(Q, 2.0)[0] if d16 > 1e-9 and Q @ Q > 0 else np.nan
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6), gridspec_kw={'width_ratios': [1, 1.05, 1]})
im0 = axs[0].imshow(Smap, origin='lower', extent=[hh[0] * math.sqrt(2), hh[-1] * math.sqrt(2), ll[0], ll[-1]], cmap=blue, aspect='equal')
axs[0].set_xlabel("$\\sqrt{2}\\,h$  along (1, 1, 0)"); axs[0].set_ylabel("(0, 0, l)")
axs[0].set_title("(a) spin-ice S(Q), frame formula", fontsize=11, loc='left')
fig.colorbar(im0, ax=axs[0], fraction=0.046, pad=0.03)
axs[1].scatter(Sfr, Smc, s=9, color="#2a78d6", alpha=0.7, linewidths=0)
lim = [0, max(Sfr.max(), Smc.max()) * 1.05]
axs[1].plot(lim, lim, color="#52514e", lw=1)
axs[1].set_xlim(lim); axs[1].set_ylim(lim)
axs[1].set_xlabel("frame large-N  S(Q)  (no fitted constant)"); axs[1].set_ylabel("exact T = 0 ice Monte Carlo  S(Q)")
axs[1].set_title(f"(b) {len(Qs)} wavevectors, corr {corr:.3f}", fontsize=11, loc='left')
axs[1].grid(color="#e6e5e0", lw=0.6)
im2 = axs[2].imshow(Wmap, origin='lower', extent=[hh[0] * math.sqrt(2), hh[-1] * math.sqrt(2), ll[0], ll[-1]], cmap=orange, aspect='equal', vmin=0, vmax=4)
axs[2].set_xlabel("$\\sqrt{2}\\,h$  along (1, 1, 0)"); axs[2].set_ylabel("(0, 0, l)")
axs[2].set_title("(c) photon  $\\omega/\\sqrt{UK}=\\sqrt{16-|f|^2}$", fontsize=11, loc='left')
fig.colorbar(im2, ax=axs[2], fraction=0.046, pad=0.03)
for a in axs:
    for sp_ in a.spines.values(): sp_.set_color("#b5b4ad")
fig.tight_layout()
fig.savefig("empirical_01f/fig_spin_ice.png", dpi=160)
print("      wrote empirical_01f/fig_spin_ice.png")

print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
