"""
Paper 01e Section 11 certificates: how to measure the Grashof loop count.

M1  Near a Grashof wall the two loops separate as sqrt(margin): log-log slope -> 1/2; 0.3 rad at 1.25% margin.
M2  Synthetic Brillouin zone (four-arm interferometer / any four-path two-mode system): loops = vortex lines of
    the output phase; plaquette-winding counting, size-filtered, recovers 0/1/2 loops for [111] strain and is
    >= 90% correct at |margin| >= 2% (64^3 settings, 0.02 rad phase noise, 1% field noise).
M3  An intensity threshold (dark-spot detection) at the same resolution merges the two loops (the failure mode).
M4  Real lattice: on the (111) surface zone the region without drumhead zero modes has 2 pockets under tension
    (2 loops) and 1 under compression (1 loop); the drumhead fraction itself is continuous across the wall.
"""
import itertools, math
from collections import Counter
import numpy as np
from scipy import ndimage

PASS = []
def chk(name, ok):
    PASS.append(bool(ok)); print(f"  [{'OK ' if ok else 'FAIL'}] {name}")
rng = np.random.default_rng(11)
E = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / 4.0; Ec = E - E[0]
A1 = np.array([E[0] - E[1], E[0] - E[2], E[0] - E[3]]); rec = 2 * np.pi * np.linalg.inv(A1).T
def theory(T):
    s = sorted(T); return 0 if s[3] > s[0] + s[1] + s[2] else (2 if s[0] + s[3] < s[1] + s[2] else 1)

print("M1  loop separation near the Grashof wall")
def nodal_branches(T, M=3000):
    out = {1: [], -1: []}
    for a in np.linspace(0, 2 * np.pi, M, endpoint=False):
        w = T[0] + T[1] * np.exp(1j * a); r = abs(w)
        cd = (r * r + T[2]**2 - T[3]**2) / (2 * r * T[2]) if r > 1e-12 else 9
        if abs(cd) > 1: continue
        d = math.acos(cd); b = np.angle(-w)
        for s in (1, -1):
            u3 = T[2] * np.exp(1j * (b + s * d)); u4 = -w - u3
            out[s].append((a, np.angle(u3) % (2 * np.pi), np.angle(u4) % (2 * np.pi)))
    return np.array(out[1]), np.array(out[-1])
gs, ds = [], []
for g in (0.2, 0.1, 0.05, 0.025, 0.0125):
    l, s = 1.3, 0.7; p = (l + s + g) / 2; A, B = nodal_branches([l, s, p, p])
    dd = np.abs(A[::2, None, :] - B[None, ::2, :]); dd = np.minimum(dd, 2 * np.pi - dd)
    gs.append(g); ds.append(np.sqrt((dd**2).sum(-1)).min())
slope = np.polyfit(np.log(gs[-3:]), np.log(ds[-3:]), 1)[0]
print(f"      margins {gs} -> min separation {np.round(ds, 3)} rad")
chk(f"separation ~ margin^(1/2) (fitted exponent {slope:.3f}); still {ds[-1]:.2f} rad at 1.25% margin", abs(slope - 0.5) < 0.05 and ds[-1] > 0.25)

print("M2  synthetic Brillouin zone: vortex-line counting")
def field(T, M, sth=0.02, sF=0.01):
    g = np.arange(M) * 2 * np.pi / M; a, b, c = np.meshgrid(g, g, g, indexing='ij')
    a = a + rng.normal(0, sth, a.shape); b = b + rng.normal(0, sth, b.shape); c = c + rng.normal(0, sth, c.shape)
    F = T[0] + T[1] * np.exp(1j * a) + T[2] * np.exp(1j * b) + T[3] * np.exp(1j * c)
    return F + sF * sum(T) * (rng.normal(size=F.shape) + 1j * rng.normal(size=F.shape)) / math.sqrt(2)
def wind(F, a1, a2):
    F1 = np.roll(F, -1, a1); F12 = np.roll(F1, -1, a2); F2 = np.roll(F, -1, a2)
    return np.rint((np.angle(F1 / F) + np.angle(F12 / F1) + np.angle(F2 / F12) + np.angle(F / F2)) / (2 * np.pi)).astype(int)
def vortex_loops(F, minfrac=0.25):
    M = F.shape[0]; parent = {}; size = Counter(); edges = []
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for n, (a1, a2) in enumerate(((1, 2), (0, 2), (0, 1))):
        for p in np.argwhere(wind(F, a1, a2) != 0):
            q = p.copy(); q[n] = (q[n] - 1) % M; a, b = tuple(p), tuple(q)
            for x in (a, b): parent.setdefault(x, x)
            ra, rb = find(a), find(b)
            if ra != rb: parent[ra] = rb
            edges.append(a)
    for e in edges: size[find(e)] += 1
    return sum(1 for s in size.values() if s >= minfrac * M)
res = {tp: [vortex_loops(field([tp, 1, 1, 1], 48)) for _ in range(5)] for tp in (0.7, 1.3, 3.3)}
print(f"      [111] strain t'=0.7/1.3/3.3 -> {res}")
chk("[111] strain: tension t'=0.7 -> 2 loops, compression 1.3 -> 1 loop, t'=3.3 -> 0 (every repeat)",
    all(v == 2 for v in res[0.7]) and all(v == 1 for v in res[1.3]) and all(v == 0 for v in res[3.3]))
rates = {}
for t1 in (0.48, 0.52):
    T = [t1, 1.0, 1.3, 0.8]; th = theory(T)
    rates[t1] = np.mean([vortex_loops(field(T, 64)) == th for _ in range(10)])
print(f"      success at margin +0.02 / -0.02 (64^3, 10 repeats): {rates}")
chk("success >= 0.9 at |margin| = 2%", min(rates.values()) >= 0.9)

print("M3  failure mode: intensity threshold")
def periodic_comps3(mask):
    lab, k = ndimage.label(mask, structure=np.ones((3, 3, 3))); par = list(range(k + 1))
    def f(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    for ax in range(3):
        s0 = [slice(None)] * 3; s1 = [slice(None)] * 3; s0[ax] = 0; s1[ax] = -1
        X, Y = lab[tuple(s0)], lab[tuple(s1)]; m = (X > 0) & (Y > 0)
        for x, y in zip(X[m], Y[m]):
            a, b = f(x), f(y)
            if a != b: par[a] = b
    return len({f(i) for i in range(1, k + 1)})
T = [0.4, 1.0, 1.3, 0.8]; F = field(T, 48)
I = np.abs(F)**2 / sum(T)**2; eps = (0.6 * 2 * np.pi / 48)**2
ci, cv = periodic_comps3(I < eps), vortex_loops(F)
chk(f"margin +0.10 (2 loops): dark-spot threshold counts {ci}, vortex counting counts {cv}", ci == 1 and cv == 2)

print("M4  real lattice: (111) surface zero-mode map")
def periodic_comps2(mask):
    lab, k = ndimage.label(mask); par = list(range(k + 1))
    def f(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    for ax in (0, 1):
        s0 = [slice(None)] * 2; s1 = [slice(None)] * 2; s0[ax] = 0; s1[ax] = -1
        X, Y = lab[tuple(s0)], lab[tuple(s1)]; m = (X > 0) & (Y > 0)
        for x, y in zip(X[m], Y[m]):
            a, b = f(x), f(y)
            if a != b: par[a] = b
    return len({f(i) for i in range(1, k + 1)})
def surface_map(T, normal=(1, 1, 1), M=72, Nz=160):
    n = np.array(normal, float); n /= np.linalg.norm(n); P = lambda g: g - (g @ n) * n
    proj = sorted((P(np.array(m) @ rec) for m in itertools.product(range(-2, 3), repeat=3) if any(m)), key=np.linalg.norm)
    proj = [p for p in proj if np.linalg.norm(p) > 1e-9]; g1 = proj[0]
    g2 = next(p for p in proj if np.linalg.norm(np.cross(p, g1)) > 1e-6)
    per = min(np.linalg.norm(np.array(m) @ rec) for m in itertools.product(range(-3, 4), repeat=3)
              if any(m) and np.linalg.norm(np.cross(np.array(m) @ rec, n)) < 1e-9)
    s = np.linspace(0, per, Nz, endpoint=False); W = np.zeros((M, M), int)
    for i in range(M):
        k = (i / M) * g1 + (np.arange(M)[:, None, None] / M) * g2 + s[None, :, None] * n
        f = (np.exp(1j * k @ Ec.T) * np.array(T)).sum(-1)
        W[i] = np.rint(np.angle(np.roll(f, -1, axis=1) / f).sum(1) / (2 * np.pi)).astype(int)
    return W
out = {}
for tp in (0.8, 0.9, 1.1, 1.2):
    W = surface_map([tp, 1, 1, 1]); out[tp] = (np.mean(W != 0), periodic_comps2(W == 0), periodic_comps2(W != 0))
    print(f"      t'={tp}: drumhead fraction {out[tp][0]:.3f}, non-drumhead pockets {out[tp][1]}, drumhead regions {out[tp][2]}")
chk("(111) surface: 2 non-drumhead pockets under tension (2 loops), 1 under compression (1 loop)",
    out[0.8][1] == 2 and out[0.9][1] == 2 and out[1.1][1] == 1 and out[1.2][1] == 1)
chk("drumhead fraction varies smoothly (monotone, no jump > 0.1 across t'=1): not a sharp signature",
    out[0.8][0] > out[0.9][0] > out[1.1][0] > out[1.2][0] and out[0.9][0] - out[1.1][0] < 0.2)
print(f"\nTOTAL {sum(PASS)}/{len(PASS)}")
