"""
Paper 58 certificate: an arrow of time from growing capacity, and entropy carried by defects (port networks).
numpy / scipy / fractions only.  Usage: python p58_cert.py

PRE-REGISTERED FALSIFIERS (written 2026-10-02 before the first run; every branch reportable)

TEST 1 -- CAPACITY GROWTH.  A chain of harmonic nodes between two walls, springs k, temperature T = 1, overdamped
port dynamics dx = -gamma K x dt + sqrt(2 gamma T) dW (gamma = 1); thermal state Sigma_eq = T K^-1.  The network GROWS by
splitting the stiffest bond (k -> two bonds of 2k: Kron reduction, so the old nodes' thermal marginal is unchanged and
the proper length is unchanged -- a finer network, more capacity).  The new node is inserted at the midpoint of its
neighbours with variance eps (eps < s = T/(4k): colder than thermal, "incepted from a lighter phase").  Arrow resource:
D(t) = D(rho_t || Sigma_eq(t)) = beta (F - F_eq), the work available against the current thermal state.
  K1a [exact identity] thermal insertion (eps = s) leaves D unchanged (|dD| < 1e-10), from any state.
  K1b [exact identity] cold insertion raises D by exactly J = (1/2)(eps/s - 1 - ln(eps/s)), independent of the prior
      state (chain rule + Kron), checked at every one of 64 insertions to relative 1e-8, starting from D = 0.
  K1c [theorem check] with relaxation of duration tau between insertions, D_final(tau) <= N_ins J for every tau
      (relaxation toward the current thermal state cannot increase D).
  K1d [numerics] freeze-out: the retained fraction f(tau) = D_final / (N_ins J) exceeds 0.5 at tau = 1e-3 and is below
      0.05 at tau = 10.                                                      L1: either branch fails.
  L1-global: if cold insertion did not raise D (K1b), capacity growth would produce no arrow in this model.
  Report: entropy gap S_eq(N) - S(rho) at the end, and f(tau) on the grid tau in {0, 1e-4, ..., 10}.

TEST 2 -- DEFECTS CARRY ENTROPY.  Periodic triangular network (torus L x L, unit bonds).  An edge flip (Pachner 2-2 move)
removes bond (u,v) and adds (w,z), creating a 5-5-7-7 disclination quadrupole at fixed node count N and bond count E
(zero net curvature).  For the massless classical field at fixed T, S = const - (1/2) ln tau(G), tau = number of spanning
trees (matrix-tree theorem; det' K = N tau).  Hypothesis (Penrose link): the defect-free network is the stiffest, so it
has the LOWEST field entropy.
  K2a [exact, integers] one flip strictly lowers tau (Delta S > 0) for L = 6, 8, 10.
  K2b [exact, integers] for L = 8, every one of 30 random networks with k = 1..6 disjoint flips (5 per k) has
      tau < tau(perfect).                                                    L2: some defected network has tau >= tau(perfect).
  Report: mean Delta S versus k; the quantum thermal entropy change at T = 1 with mass m^2 = 0.1 for one flip.

RUN LOG
  Run 1 (2026-10-02, p58_run1.log): 3/6.  K1a, K2a, K2b PASS.  K1b, K1c, K1d FAILED on a PRE-REGISTRATION DESIGN ERROR:
  the growth rule "split the stiffest bond" re-splits the bond it just created (two bonds of 2k are the new maximum), so
  one segment is refined without end, its stiffness reaches ~2^64, and the relaxation step overflows (D -> -1e25, nan).
  The tau = 0 branch, which never relaxes, already matched N_ins J exactly.  The intended rule -- uniform refinement,
  the analogue of expansion -- splits the SOFTEST (longest) bond.  Failure retained.  Run 2 uses the softest-bond rule
  with K1b-K1d unchanged; it is POST-DIAGNOSIS, NOT BLIND.
"""
import math, random
import numpy as np
from scipy.linalg import expm

res = []
def check(name, ok, detail=""):
    res.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

# ============================================================== TEST 1
T = 1.0; gamma = 1.0

class Chain:
    def __init__(self, n0, k0):
        self.order = list(range(n0))          # node ids along the chain
        self.k = [k0] * (n0 + 1)              # bond stiffness: wall-0, 0-1, ..., (n-1)-wall
        self.n = n0
    def K(self):
        n = self.n; M = np.zeros((n, n))
        o = self.order
        for b, kb in enumerate(self.k):
            left = o[b - 1] if b >= 1 else None
            right = o[b] if b < len(o) else None
            for x in (left, right):
                if x is not None:
                    M[x, x] += kb
            if left is not None and right is not None:
                M[left, right] -= kb; M[right, left] -= kb
        return M

def kl(Sig, Seq):
    n = Sig.shape[0]
    A = np.linalg.solve(Seq, Sig)
    sign, ld = np.linalg.slogdet(A)
    return 0.5 * (np.trace(A) - n - ld)

def insert(ch, Sig, eps_rel):
    b = int(np.argmin(ch.k))          # run 2: softest (longest) bond -- uniform refinement (run 1 used argmax)
    kb = ch.k[b]
    o = ch.order
    left = o[b - 1] if b >= 1 else None
    right = o[b] if b < len(o) else None
    new = ch.n
    c = np.zeros(ch.n)
    for x in (left, right):
        if x is not None:
            c[x] += 0.5
    s = T / (4 * kb)
    eps = eps_rel * s
    A = np.vstack([np.eye(ch.n), c])
    Sn = A @ Sig @ A.T
    Sn[new, new] += eps
    o.insert(b, new)
    ch.k[b:b + 1] = [2 * kb, 2 * kb]
    ch.n += 1
    return Sn, s, eps

def relax(ch, Sig, tau):
    if tau == 0:
        return Sig
    K = ch.K(); Seq = T * np.linalg.inv(K)
    E = expm(-gamma * K * tau)
    return E @ Sig @ E.T + Seq - E @ Seq @ E.T

def run_growth(eps_rel, tau, n_ins=64, n0=8, check_jumps=False):
    ch = Chain(n0, 1.0)
    Sig = T * np.linalg.inv(ch.K())
    D = kl(Sig, T * np.linalg.inv(ch.K()))
    worst = 0.0; Jsum = 0.0; Jlast = None
    for _ in range(n_ins):
        Sig = relax(ch, Sig, tau)
        Dpre = kl(Sig, T * np.linalg.inv(ch.K()))
        Sig, s, eps = insert(ch, Sig, eps_rel)
        Dpost = kl(Sig, T * np.linalg.inv(ch.K()))
        J = 0.5 * (eps / s - 1 - math.log(eps / s))
        Jsum += J; Jlast = J
        if J > 0:
            worst = max(worst, abs((Dpost - Dpre) - J) / J)
        else:
            worst = max(worst, abs(Dpost - Dpre))
    Seq = T * np.linalg.inv(ch.K())
    Dfin = kl(Sig, Seq)
    S = 0.5 * np.linalg.slogdet(2 * math.pi * math.e * Sig)[1]
    Seqent = 0.5 * np.linalg.slogdet(2 * math.pi * math.e * Seq)[1]
    return dict(D=Dfin, Jsum=Jsum, worst=worst, gap=Seqent - S, n=ch.n)

r_th = run_growth(1.0, 0.0)
r_th2 = run_growth(1.0, 0.1)
check("K1a [exact] thermal insertion leaves D unchanged", r_th['worst'] < 1e-10 and r_th2['worst'] < 1e-10,
      f"max |dD| = {max(r_th['worst'], r_th2['worst']):.2e}")
r0 = run_growth(0.01, 0.0)
r1 = run_growth(0.01, 0.1)
check("K1b [exact] cold insertion raises D by exactly J (chain rule + Kron), 64 insertions, any prior state",
      r0['worst'] < 1e-8 and r1['worst'] < 1e-8 and abs(r0['D'] / r0['Jsum'] - 1) < 1e-8,
      f"max rel error {max(r0['worst'], r1['worst']):.2e}; J = {r0['Jsum'] / 64:.6f} per insertion; D_final(tau=0) = {r0['D']:.6f}")
taus = [0.0, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0]
fr = {}
ok_c = True
for tau in taus:
    r = run_growth(0.01, tau)
    fr[tau] = r['D'] / r['Jsum']
    ok_c &= r['D'] <= r['Jsum'] * (1 + 1e-9)
    print(f"   tau={tau:g}: D_final={r['D']:.6f}, f={fr[tau]:.5f}, entropy gap S_eq - S = {r['gap']:.6f}, N={r['n']}", flush=True)
check("K1c [theorem check] relaxation never increases the arrow: D_final(tau) <= N_ins J", ok_c)
check("K1d [numerics] freeze-out: f(1e-3) > 0.5 and f(10) < 0.05", fr[1e-3] > 0.5 and fr[10.0] < 0.05,
      f"f(1e-3) = {fr[1e-3]:.4f}, f(10) = {fr[10.0]:.5f}")

# ============================================================== TEST 2
def tri_torus(L):
    E = set()
    for i in range(L):
        for j in range(L):
            u = i * L + j
            for di, dj in ((1, 0), (0, 1), (1, -1)):
                v = ((i + di) % L) * L + (j + dj) % L
                E.add((min(u, v), max(u, v)))
    return L * L, E

def adj(N, E):
    A = [set() for _ in range(N)]
    for u, v in E:
        A[u].add(v); A[v].add(u)
    return A

def flip(N, E, rng, used):
    A = adj(N, E)
    edges = sorted(E)
    rng.shuffle(edges)
    for (u, v) in edges:
        if u in used or v in used:
            continue
        cn = sorted(A[u] & A[v])
        if len(cn) != 2:
            continue
        w, z = cn
        if w in used or z in used or z in A[w]:
            continue
        E2 = set(E); E2.remove((u, v)); E2.add((min(w, z), max(w, z)))
        used |= {u, v, w, z}
        return E2
    return None

def spanning_trees(N, E):
    """exact integer count: Bareiss determinant of the reduced Laplacian."""
    M = [[0] * N for _ in range(N)]
    for u, v in E:
        M[u][u] += 1; M[v][v] += 1; M[u][v] -= 1; M[v][u] -= 1
    M = [row[:N - 1] for row in M[:N - 1]]
    n = N - 1; prev = 1
    for k in range(n - 1):
        piv = M[k][k]
        if piv <= 0:
            raise ValueError("reduced Laplacian is positive definite: pivots must be positive")
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * piv - M[i][k] * M[k][j]) // prev
        prev = piv
    return M[n - 1][n - 1]

def count_trees(N, E):
    t = spanning_trees(N, E)
    return abs(t)

rng = random.Random(580001)
ok_a = True; det_a = []
for L in (6, 8, 10):
    N, E = tri_torus(L)
    t0 = count_trees(N, E)
    E1 = flip(N, E, rng, set())
    t1 = count_trees(N, E1)
    dS = -0.5 * (math.log(t1) - math.log(t0))
    ok_a &= t1 < t0
    det_a.append(f"L={L}: tau ratio {t1 / t0:.6f}, Delta S = {dS:+.6f}")
check("K2a [exact] one edge flip (5-5-7-7 quadrupole) lowers the spanning-tree count: Delta S > 0", ok_a, "; ".join(det_a))
N, E = tri_torus(8)
t0 = count_trees(N, E)
ok_b = True; means = []
for k in range(1, 7):
    dss = []
    for rep in range(5):
        Ek = set(E); used = set()
        for _ in range(k):
            Ek2 = flip(N, Ek, rng, used)
            if Ek2 is None:
                break
            Ek = Ek2
        tk = count_trees(N, Ek)
        ok_b &= tk < t0
        dss.append(-0.5 * (math.log(tk) - math.log(t0)))
    means.append((k, float(np.mean(dss)), float(np.min(dss))))
check("K2b [exact] every defected network (k = 1..6 flips, 30 samples, L=8) has fewer spanning trees than the perfect one",
      ok_b, "; ".join(f"k={k}: mean dS={m:+.5f} (min {mn:+.5f})" for k, m, mn in means))

# report: quantum thermal entropy, massive, one flip, L = 8
def lap(N, E):
    M = np.zeros((N, N))
    for u, v in E:
        M[u, u] += 1; M[v, v] += 1; M[u, v] -= 1; M[v, u] -= 1
    return M
def S_quantum(N, E, m2=0.1, Tq=1.0):
    w = np.sqrt(np.linalg.eigvalsh(lap(N, E)) + m2)
    nb = 1 / np.expm1(w / Tq)
    return float(np.sum((nb + 1) * np.log1p(nb) - nb * np.log(nb)))
E1 = flip(N, E, random.Random(7), set())
print(f"   report: quantum thermal entropy (T=1, m^2=0.1), one flip on L=8: dS = {S_quantum(N, E1) - S_quantum(N, E):+.6f}", flush=True)
print(f"\nTOTAL: {sum(res)}/{len(res)} PASS")
