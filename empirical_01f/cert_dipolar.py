"""
Paper 01f Section 10 certificates: dipolar spin ice in the frame (numpy only; no Ewald needed).

D1  Exact decomposition on an open cluster: E_dip = U_Coulomb(tetrahedron charges) + nn on-site term
    + sum_(non-nn) delta_ij sigma_i sigma_j + const, with delta = point dipole - dumbbell; nn coupling = 5D/3.
D2  The nn remainder has ONE coefficient c' for all nn pairs, so (01f Prop 2.3) it is 2c' q_t^2 - 2c' per
    tetrahedron: an on-site charge term. Nearest-neighbour exchange J is likewise pure gauge.
D3  The residual delta decays as r^-5 (absolutely convergent; no Ewald sum required).
D4  Projected onto the ice sector (the flat bands), delta has its minimum exactly at the X point, doubly
    degenerate; converged in the cutoff; band width ~0.178 D.
D5  The X-point ground states are ice on every tetrahedron, carry zero net moment, and are built from the two
    matchings whose diamond nodal circles cross at that X point; the third matching is not ice.
"""
import itertools, math
import numpy as np

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")

E = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / 4.0
V = E / np.linalg.norm(E, axis=1)[:, None]
A1 = np.array([E[0] - E[1], E[0] - E[2], E[0] - E[3]])
ad = np.linalg.norm(E[0]); rnn = np.linalg.norm(E[0] - E[1]) / 2; q = 1 / ad    # mu = 1, mu0/4pi = 1
Dunit = 1 / rnn**3
dvec = [np.zeros(3, int)] + [-np.eye(3, dtype=int)[i] for i in range(3)]

def Tpt(ri, vi, rj, vj):
    r = rj - ri; d = np.linalg.norm(r); rh = r / d
    return (vi @ vj - 3 * (vi @ rh) * (vj @ rh)) / d**3
def Tdb(ri, ei, rj, ej):          # dumbbell: +q at the head (B end), -q at the tail (A end); skip coincident charges
    s = 0
    for pi, qi in ((ri + ei / 2, q), (ri - ei / 2, -q)):
        for pj, qj in ((rj + ej / 2, q), (rj - ej / 2, -q)):
            d = np.linalg.norm(pi - pj)
            if d > 1e-9: s += qi * qj / d
    return s

print("D1  exact decomposition (open cluster, L = 3, 108 spins)")
L = 3; cells = [np.array(c) for c in itertools.product(range(L), repeat=3)]
pos, ax, bv = [], [], []
for c in cells:
    for n in range(4): pos.append(c @ A1 + E[n] / 2); ax.append(V[n]); bv.append(E[n])
pos, ax, bv = map(np.array, (pos, ax, bv)); ns = len(pos)
isnn = lambda i, j: abs(np.linalg.norm(pos[i] - pos[j]) - rnn) < 1e-9
sites = {}
for i in range(ns):
    for p, s in ((pos[i] + bv[i] / 2, 1), (pos[i] - bv[i] / 2, -1)):
        sites.setdefault(tuple(np.round(p, 9)), []).append((i, s))
skeys = list(sites); spos = np.array(skeys)
pairs = [(i, j) for i in range(ns) for j in range(i + 1, ns)]
Tp = {pr: Tpt(pos[pr[0]], ax[pr[0]], pos[pr[1]], ax[pr[1]]) for pr in pairs}
Td = {pr: Tdb(pos[pr[0]], bv[pr[0]], pos[pr[1]], bv[pr[1]]) for pr in pairs}
rng = np.random.default_rng(0); worst = 0
for _ in range(5):
    sg = rng.choice([-1, 1], ns)
    Edip = sum(Tp[pr] * sg[pr[0]] * sg[pr[1]] for pr in pairs)
    Q = np.array([q * sum(s * sg[i] for i, s in sites[k]) for k in skeys])
    U = sum(Q[a] * Q[b] / np.linalg.norm(spos[a] - spos[b]) for a in range(len(Q)) for b in range(a + 1, len(Q)))
    nnpart = sum((Tp[pr] - Td[pr]) * sg[pr[0]] * sg[pr[1]] for pr in pairs if isnn(*pr))
    res = sum((Tp[pr] - Td[pr]) * sg[pr[0]] * sg[pr[1]] for pr in pairs if not isnn(*pr))
    worst = max(worst, abs(Edip - (U + nnpart + res + q * q / ad * ns)))
chk(f"E_dip = U(site charges) + nn remainder + residual + const, exactly (5 random configurations; err {worst:.1e})", worst < 1e-9)
cnn = [Tp[pr] for pr in pairs if isnn(*pr)]
chk("nearest-neighbour dipolar coupling = (5/3) D (den Hertog-Gingras)", np.allclose(np.array(cnn) / Dunit, 5 / 3))

print("D2  the nearest-neighbour remainder is an on-site charge term")
cprime = np.array([(Tp[pr] - Td[pr]) / Dunit for pr in pairs if isnn(*pr)])
chk(f"all nn pairs share one coefficient c' = {cprime[0]:.8f} D  ->  per tetrahedron c'(2q^2 - 2): pure gauge", np.ptp(cprime) < 1e-9)
states = list(itertools.product([1, -1], repeat=4))
chk("any nn coupling K: K sum_(i<j) sigma_i sigma_j = K(2q^2 - 2) for all 16 states: exchange J never touches the ice sector",
    all(sum(s[i] * s[j] for i in range(4) for j in range(i + 1, 4)) == 2 * (sum(s) / 2)**2 - 2 for s in states))

print("D3  the residual is short-ranged (r^-5)")
r0 = np.array([0, 0, 0.]); shells = {}
for c in itertools.product(range(-8, 9), repeat=3):
    R = np.array(c) @ A1
    for k in range(4):
        rk = R + E[k] / 2 - E[0] / 2; d = np.linalg.norm(rk)
        if d < 1e-9 or abs(d - rnn) < 1e-9 or d > 3.5: continue
        dl = abs(Tpt(r0, V[0], rk, V[k]) - Tdb(r0, E[0], rk, E[k]))
        key = round(d, 6); shells[key] = max(shells.get(key, 0), dl)
ds = np.array(sorted(shells)); mx = np.array([shells[d] for d in ds])
far = ds > 1.5
slope = np.polyfit(np.log(ds[far]), np.log(mx[far]), 1)[0]
chk(f"shell maxima of |delta| decay with log-log slope {slope:.2f} (multipole theory: -5)", -5.6 < slope < -4.6)

print("D4  the residual on the ice sector selects the X point")
def residual_terms(Rc):
    T = []
    for j in range(4):
        rj = E[j] / 2
        for c in itertools.product(range(-Rc, Rc + 1), repeat=3):
            R = np.array(c) @ A1
            if np.linalg.norm(R) > Rc * 0.5 + 1e-9: continue
            for k in range(4):
                rk = R + E[k] / 2; d = np.linalg.norm(rk - rj)
                if d < 1e-9 or abs(d - rnn) < 1e-9: continue
                T.append((j, k, rk - rj, Tpt(rj, V[j], rk, V[k]) - Tdb(rj, E[j], rk, E[k])))
    J = np.array([t[0] for t in T]); K = np.array([t[1] for t in T]); Dp = np.array([t[2] for t in T]); dl = np.array([t[3] for t in T])
    def delta(kv):
        M = np.zeros((4, 4), complex); np.add.at(M, (J, K), dl * np.exp(1j * Dp @ kv)); return M / Dunit
    return delta
def flat_basis(kv):
    th = E @ kv; u = np.exp(1j * th); uH = u - u.mean()
    P = np.eye(4) - np.ones((4, 4)) / 4 - np.outer(uH, uH.conj()) / np.vdot(uH, uH).real
    W = np.diag(np.exp(1j * th / 2)); Pp = W.conj().T @ P @ W
    w, U = np.linalg.eigh(Pp); return U[:, w > 0.5]
rec = 2 * np.pi * np.linalg.inv(A1).T
res = {}
for Rc in (6, 8):
    delta = residual_terms(Rc); best = (1e9, None); lo, hi = 1e9, -1e9; n = 16
    for m in itertools.product(range(n), repeat=3):
        kv = (np.array(m) / n) @ rec
        if 16 - abs(np.exp(1j * (E @ kv)).sum())**2 < 1e-8: continue
        B = flat_basis(kv); h = B.conj().T @ delta(kv) @ B; e2 = np.linalg.eigvalsh((h + h.conj().T) / 2)
        lo, hi = min(lo, e2[0]), max(hi, e2[-1])
        if e2[0] < best[0] - 1e-12: best = (e2[0], kv)
    kX = best[1] / (2 * np.pi)
    isX = sorted(np.abs(np.round(kX, 6))) == [0, 0, 1]
    res[Rc] = (lo, hi, isX)
    print(f"      Rc={Rc}: ice-sector band [{lo:.5f}, {hi:.5f}] D, argmin k = {np.round(kX, 4)} (2pi/a0)")
    if Rc == 8: deltaX = delta
chk("argmin of the ice-sector residual is an X point (k = 2pi/a0 * unit cubic vector), at both cutoffs", res[6][2] and res[8][2])
chk(f"converged in the cutoff: min {res[8][0]:.4f} D, width {res[8][1]-res[8][0]:.4f} D (Rc 6 vs 8 agree to 1e-3)",
    abs(res[6][0] - res[8][0]) < 1e-3 and abs((res[6][1] - res[6][0]) - (res[8][1] - res[8][0])) < 1e-3)
kXv = 2 * np.pi * np.array([0, 1, 0.]); B = flat_basis(kXv); h = B.conj().T @ deltaX(kXv) @ B
eX = np.linalg.eigvalsh((h + h.conj().T) / 2)
chk(f"at X the minimum is doubly degenerate ({eX[0]:.5f}, {eX[1]:.5f})", abs(eX[0] - eX[1]) < 1e-9)
chk(f"scale: ice-sector width / nn coupling = {(res[8][1]-res[8][0])/(5/3):.3f}; / on-site monopole cost 2c' = {(res[8][1]-res[8][0])/(2*cprime[0]):.3f}",
    (res[8][1] - res[8][0]) / (2 * cprime[0]) < 0.05)

print("D5  the ordered state")
th = E @ kXv; u = np.exp(1j * th); Bdiv = np.vstack([np.ones(4), u.conj()])
chk(f"at X, u = {np.round(u, 6)} and f = 0: X lies on the diamond nodal network (crossing of two matching circles)", abs(u.sum()) < 1e-12)
Lc = 2; cl = [np.array(m) for m in itertools.product(range(Lc), repeat=3)]
out = {}
for name, cc in (("{12|34}", np.array([1, 1, -1, -1.])), ("{14|23}", np.array([1, -1, -1, 1.])), ("{13|24}", np.array([1, -1, 1, -1.]))):
    sig = {(tuple(m), nn): int(np.sign(np.real(cc[nn] * np.exp(1j * kXv @ (m @ A1))))) for m in cl for nn in range(4)}
    okA = all(sum(sig[(tuple(m), nn)] for nn in range(4)) == 0 for m in cl)
    okB = all(sum(sig[(tuple(np.mod(m - dvec[nn], Lc)), nn)] for nn in range(4)) == 0 for m in cl)
    mom = sum(sig[(tuple(m), nn)] * V[nn] for m in cl for nn in range(4))
    cph = np.diag(np.exp(-1j * th / 2)) @ cc / 2
    out[name] = (np.abs(Bdiv @ cc).max() < 1e-12, okA and okB, np.allclose(mom, 0), float(np.real(cph.conj() @ deltaX(kXv) @ cph)))
    print(f"      matching {name}: flat {out[name][0]}, ice on all tetrahedra {out[name][1]}, zero moment {out[name][2]}, residual energy {out[name][3]:.5f}")
chk("the X ground states (energy = band minimum) are the staggered ice states of matchings {12|34} and {14|23}, zero net moment",
    all(out[k][0] and out[k][1] and out[k][2] and abs(out[k][3] - eX[0]) < 1e-9 for k in ("{12|34}", "{14|23}")))
chk("the third matching {13|24} is not in the flat space and violates the ice rule on down tetrahedra",
    (not out["{13|24}"][0]) and (not out["{13|24}"][1]))

print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
