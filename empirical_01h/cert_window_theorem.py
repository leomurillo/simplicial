"""Paper 01h (Windows of the Hermite-Pade solid) -- certificate.
Criteria declared before first execution. 2026-10-18.
Author certificate after analytic derivation. Exploratory probes (scratchpad,
same session) preceded these checks; every claim is re-derived here.

Object. Series f_0=1, f_1..f_N; for n in N^{N+1}, tau(n) = det M(n), where M(n) is
|n| x |n|, rows k=0..|n|-1, columns (i,j) block-ordered (i, then j<n_i), entry
[z^k] z^j f_i. Generator a (primitive deficient vector): d(a)_i = deg a_i + 1,
w(a) = ord(sum a_i f_i), s = w - |d|, S = supp(a). Elementary window
W(a) = { n >= d : |n-d| - min_{i in S}(n-d)_i <= s }.

W1  Hirota-Miwa over Q (exact Fractions): tau_i tau_jk - tau_j tau_ik + tau_k tau_ij
    = 0 at every base point and every triple i<j<k, for N=2 (B=4) and N=3 (B=3),
    random rational series and the exp examples. Zero failures.
W2  Hirota-Miwa over F_p, p in {2,3,5,7}: N=2 (B=7), N=3 (B=4). Zero failures.
W3  Union theorem: Z(tau) = union of W(a) over generators read off kernels, exact
    set equality inside the box, N=1,2,3, p in {2,3,5,7}, 3 seeds each.
W4  Depth formula: at every zero covered by exactly one elementary window,
    corank M(n) = 1 + min(mu, s - (|k| - mu)), k = n - d, mu = min_S k.
W5  Planted windows over F_101 (N=1,2,3; full and partial supports): W(a) is
    contained in Z; |W(a)| equals the slice count sum_r #slice(r), where the order-r
    slice is the simplex of side r (r<=s) and (|S|)s-(|S|-1)r afterwards
    (|S|>=2); every order slice of W(a) equals that translated simplex.
W6  N=1 (number walls): no unit square n+{0,1}^2 meets two distinct PRIMITIVE generators
    (=> windows are disjoint squares, separated in all 8 directions). p in
    {2,3,5}, 5 seeds each, B=14. [run2 addition, declared before run3: the
    depth formula of W4 holds at EVERY zero when N=1.]
W7  Local rank bound: for every unit cube n+{0,1}^{N+1}, the kernel vectors of its
    2^{N+1} points span a K(z)-space of dimension <= N (every (N+1)-minor of the
    polynomial matrix vanishes), N=2 (p=2,3, B=6) and N=3 (p=2, B=3). Sharpness:
    for N=2 some cube attains rank exactly 2.
W8  Touching and overlap for N=2 (exact over Q). (a) f1=exp(z^2), f2=exp(z^2+z^3):
    the zeros (1,1,0) [generator (1,-1,0)] and (1,1,1) [generator (0,1,-1)] are
    e_2-adjacent and belong to distinct generators; W((0,1,-1)) is the 5-point
    square pyramid {(0,1,1),(1,1,1),(0,2,1),(0,1,2),(0,2,2)}. (b) f1=exp(z^3),
    f2=exp(z^3+z^4): corank M(1,1,1) = 2 although every single elementary window
    through (1,1,1) predicts depth 1 (overlap). (c) Over F_5, N=2, 6 seeds, B=8:
    pairs of distinct-generator zeros occur in all 26 king directions.
W10 [declared before run3] Number-wall cross rule as Hirota-Miwa. For a random
    bi-infinite integer sequence c, the three-family solid (unit columns e_k;
    right shifts v_j=(c_{k-j})_k, j=0,1,..; left shifts v_{-1},v_{-2},.. appended
    in that order) satisfies tau(n) = (-1)^{n1 n2 + C(n2,2)} S(n1+n2, n0+n2) with
    S(m,q) = det[c_{q+i-j}]_{i,j<m}; it satisfies Hirota-Miwa; and S satisfies
    S(m+2,q+1)S(m,q+1) = S(m+1,q+1)^2 - S(m+1,q+2)S(m+1,q) (Lunnon). Exact.
W9  Frame observation (reported, not a theorem): planted N=1 windows have
    geometric facet layers (all checks pass); planted N=2 windows do not
    (report failure counts).
"""
import sys, itertools, random, json, time
from fractions import Fraction as Fr
from collections import Counter
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
RESULTS = {}
T0 = time.time()

def report(key, ok, info):
    RESULTS[key] = {"pass": bool(ok), "info": info}
    print(f"{key}: {'PASS' if ok else 'FAIL'}  {info}", flush=True)

# ---------------------------------------------------------------- F_p engine
def build_M(F, n, p=None):
    N = sum(n)
    M = np.zeros((N, N), dtype=np.int64) if p is not None else [[Fr(0)] * N for _ in range(N)]
    c = 0
    for i, ni in enumerate(n):
        fi = F[i]
        for j in range(ni):
            for k in range(j, N):
                if p is not None:
                    M[k, c] = fi[k - j]
                else:
                    M[k][c] = fi[k - j]
            c += 1
    return M

def det_rank_p(M, p):
    A = M.copy() % p
    N = A.shape[0]; det = 1; r = 0
    for col in range(N):
        piv = next((rr for rr in range(r, N) if A[rr, col]), None)
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]; det = -det
        det = det * int(A[r, col]) % p
        A[r] = A[r] * pow(int(A[r, col]), p - 2, p) % p
        f = A[:, col].copy(); f[r] = 0
        A = (A - np.outer(f, A[r])) % p
        r += 1
    return (det % p if r == N else 0), r

def nullspace_p(M, p):
    A = M.copy() % p
    R, C = A.shape; piv = []; r = 0
    for col in range(C):
        q = next((rr for rr in range(r, R) if A[rr, col]), None)
        if q is None:
            continue
        A[[r, q]] = A[[q, r]]
        A[r] = A[r] * pow(int(A[r, col]), p - 2, p) % p
        f = A[:, col].copy(); f[r] = 0
        A = (A - np.outer(f, A[r])) % p
        piv.append(col); r += 1
        if r == R:
            break
    out = []
    for fc in (c for c in range(C) if c not in piv):
        v = np.zeros(C, dtype=np.int64); v[fc] = 1
        for ri, pc in enumerate(piv):
            v[pc] = (-A[ri, fc]) % p
        out.append(v)
    return out

def det_rank_q(M):
    A = [row[:] for row in M]; N = len(A); det = Fr(1); r = 0
    for col in range(N):
        piv = next((i for i in range(r, N) if A[i][col] != 0), None)
        if piv is None:
            continue
        if piv != r:
            A[r], A[piv] = A[piv], A[r]; det = -det
        det *= A[r][col]
        for i in range(N):
            if i != r and A[i][col] != 0:
                f = A[i][col] / A[r][col]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
    return (det if r == N else Fr(0)), r

def split(v, n):
    out = []; c = 0
    for ni in n:
        out.append([int(x) for x in v[c:c + ni]]); c += ni
    return out

def dvec(a):
    return tuple((max(j for j, x in enumerate(ai) if x) + 1) if any(ai) else 0 for ai in a)

def omega_p(F, a, L, p):
    tot = [0] * L
    for ai, fi in zip(a, F):
        for j, x in enumerate(ai):
            if x:
                for k in range(L - j):
                    tot[j + k] = (tot[j + k] + x * fi[k]) % p
    return next((k for k, x in enumerate(tot) if x), 10 ** 9)

def strip_z(a):
    t = min(next((j for j, x in enumerate(ai) if x), 10 ** 9) for ai in a)
    return [ai[t:] for ai in a]

def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a

def pdivmod(a, b, p):
    a = ptrim(a); b = ptrim(b)
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % p; sh = len(a) - len(b)
        q[sh] = c
        for i, y in enumerate(b):
            a[sh + i] = (a[sh + i] - c * y) % p
        a = ptrim(a)
    return ptrim(q), a

def pgcd(a, b, p):
    a = ptrim(a); b = ptrim(b)
    while b:
        a, b = b, pdivmod(a, b, p)[1]
    return a

def primitive(a, p):
    """strip z, divide by the polynomial gcd of the components, normalize."""
    a = [ptrim(ai) for ai in strip_z(a)]
    g = []
    for ai in a:
        if ai:
            g = pgcd(g, ai, p) if g else ai
    a = [pdivmod(ai, g, p)[0] if ai else [] for ai in a]
    lead = next(ai[-1] for ai in a if ai)
    inv = pow(lead, p - 2, p)
    return [[x * inv % p for x in ai] for ai in a]

def in_window(n, d, s, S, *_):
    k = [x - y for x, y in zip(n, d)]
    if min(k) < 0:
        return False
    if not S:
        return False
    mu = min(k[i] for i in S)
    return sum(k) - mu <= s

def rand_series(N1, L, p, rng):
    return [[1] + [0] * (L - 1)] + [[rng.randrange(p) for _ in range(L)] for _ in range(N1 - 1)]

def solid_p(F, B, p, N1):
    tau, rank = {}, {}
    for n in itertools.product(range(B + 1), repeat=N1):
        if sum(n) == 0:
            tau[n], rank[n] = 1, 0
            continue
        tau[n], rank[n] = det_rank_p(build_M(F, n, p), p)
    return tau, rank

def generators_p(F, Z, p, L, N1):
    gens = {}
    kers = {}
    for n in Z:
        kers[n] = []
        for v in nullspace_p(build_M(F, n, p), p):
            a = primitive(split(v, n), p)
            kers[n].append(split(v, n))
            d = dvec(a); w = omega_p(F, a, L, p)
            S = tuple(i for i in range(N1) if d[i] > 0)
            gens.setdefault((d, w - sum(d), S, tuple(tuple(x) for x in a)), a)
    return gens, kers

def hirota_fail(tau, N1, zero):
    E = [tuple(int(t == i) for t in range(N1)) for i in range(N1)]
    add = lambda *v: tuple(map(sum, zip(*v)))
    bad = tot = 0
    for n in list(tau):
        for i, j, k in itertools.combinations(range(N1), 3):
            q = [add(n, E[i]), add(n, E[j], E[k]), add(n, E[j]), add(n, E[i], E[k]), add(n, E[k]), add(n, E[i], E[j])]
            if all(x in tau for x in q):
                tot += 1
                v = tau[q[0]] * tau[q[1]] - tau[q[2]] * tau[q[3]] + tau[q[4]] * tau[q[5]]
                bad += not zero(v)
    return bad, tot

# ---------------------------------------------------------------- Q series
def exp_series(c, L):
    out = [Fr(0)] * L; out[0] = Fr(1)
    g1 = [Fr(0)] * L
    for k, v in c.items():
        g1[k - 1] += k * Fr(v)
    for n in range(1, L):
        out[n] = sum(g1[j] * out[n - 1 - j] for j in range(n)) / n
    return out

def solid_q(F, B, N1):
    tau, rank = {}, {}
    for n in itertools.product(range(B + 1), repeat=N1):
        if sum(n) == 0:
            tau[n], rank[n] = Fr(1), 0
            continue
        tau[n], rank[n] = det_rank_q(build_M(F, n))
    return tau, rank

# ======================================================================= W1
rng = random.Random(20261018)
bad_all = tot_all = 0
cases = []
L = 20
F2 = [[Fr(1)] + [Fr(0)] * (L - 1)] + [[Fr(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(L)] for _ in range(2)]
cases.append(("rand N=2", F2, 4, 3))
F3 = [[Fr(1)] + [Fr(0)] * (L - 1)] + [[Fr(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(L)] for _ in range(3)]
cases.append(("rand N=3", F3, 3, 4))
cases.append(("exp(z^2),exp(z^2+z^3)", [[Fr(1)] + [Fr(0)] * (L - 1), exp_series({2: 1}, L), exp_series({2: 1, 3: 1}, L)], 4, 3))
QSOL = {}
for name, F, B, N1 in cases:
    tau, rank = solid_q(F, B, N1)
    QSOL[name] = (tau, rank)
    b, t = hirota_fail(tau, N1, lambda v: v == 0)
    bad_all += b; tot_all += t
report("W1", bad_all == 0, f"{tot_all} exact Hirota-Miwa checks over Q, {bad_all} failures")

# ======================================================================= W2..W4
bad_all = tot_all = 0
w3_ok = True; w3_info = []
w4_ok = w4_bad = 0
for p in (2, 3, 5, 7):
    for (N1, B) in ((2, 9), (3, 7), (4, 4)):
        for seed in range(3):
            rng = random.Random(1000 * p + 10 * N1 + seed)
            L = N1 * B + 60
            F = rand_series(N1, L, p, rng)
            tau, rank = solid_p(F, B, p, N1)
            if N1 >= 3:
                b, t = hirota_fail(tau, N1, lambda v: v % p == 0)
                bad_all += b; tot_all += t
            Z = [n for n in tau if tau[n] == 0]
            gens, _ = generators_p(F, Z, p, L, N1)
            pred = set(n for n in tau if any(in_window(n, *g) for g in gens))
            eq = pred == set(Z)
            w3_ok &= eq
            w3_info.append((p, N1 - 1, seed, len(Z), len(gens), eq))
            for n in Z:
                cover = [g for g in gens if in_window(n, *g)]
                if len(cover) == 1:
                    d, s, S = cover[0][:3]
                    k = [x - y for x, y in zip(n, d)]
                    mu = min(k[i] for i in S)
                    if 1 + min(mu, s - (sum(k) - mu)) == sum(n) - rank[n]:
                        w4_ok += 1
                    else:
                        w4_bad += 1
report("W2", bad_all == 0, f"{tot_all} Hirota-Miwa checks over F_p (N=2,3), {bad_all} failures")
report("W3", w3_ok, f"{len(w3_info)} solids (p,N,seed,|Z|,#gens,eq) e.g. {w3_info[:3]} ... all equal: {w3_ok}")
report("W4", w4_bad == 0 and w4_ok > 0, f"depth formula: {w4_ok} single-cover zeros agree, {w4_bad} disagree")

# ======================================================================= W5
def inv_series(a, L, p):
    out = [0] * L; i0 = pow(a[0], p - 2, p); out[0] = i0
    for k in range(1, L):
        s = sum(a[j] * out[k - j] for j in range(1, min(k, len(a) - 1) + 1))
        out[k] = (-s * i0) % p
    return out

def mul(a, b, L, p):
    out = [0] * L
    for i, x in enumerate(a[:L]):
        if x:
            for j, y in enumerate(b[:L - i]):
                out[i + j] = (out[i + j] + x * y) % p
    return out

def plant(p, d, s, L, rng):
    """f_0 = 1; a has support S = {i: d_i > 0}, last index in S solved for."""
    N1 = len(d)
    S = [i for i in range(N1) if d[i] > 0]
    a = []
    for di in d:
        if di == 0:
            a.append([])
        else:
            c = [rng.randrange(p) for _ in range(di)]
            c[0] = rng.randrange(1, p); c[-1] = rng.randrange(1, p)
            a.append(c)
    F = [[1] + [0] * (L - 1)] + [[rng.randrange(1, p)] + [rng.randrange(p) for _ in range(L - 1)] for _ in range(N1 - 1)]
    last = S[-1]
    w = sum(d) + s
    acc = [0] * L
    for i in S[:-1]:
        acc = [(x + y) % p for x, y in zip(acc, mul(a[i], F[i], L, p))]
    r = [0] * w + [rng.randrange(1, p)] + [rng.randrange(p) for _ in range(L - w - 1)]
    num = [(-x + y) % p for x, y in zip(acc, r)]
    F[last] = mul(num, inv_series(a[last], L, p), L, p)
    return F, a, tuple(S)

def slice_side(r, s, k):
    return r if r <= s else (k + 1) * s - k * r

from math import comb
w5_ok = True; w5_info = []
p = 101
for (d, s) in [((3, 3), 5), ((2, 4), 3), ((3, 3, 3), 4), ((2, 3, 4), 3), ((2, 2, 0), 3), ((2, 0, 3), 4), ((2, 2, 2, 2), 2), ((2, 0, 2, 2), 2)]:
    rng = random.Random(hash((d, s)) & 0xffff)
    N1 = len(d)
    B = max(d) + s + 2
    L = N1 * B + 40
    F, a, S = plant(p, d, s, L, rng)
    assert omega_p(F, a, L, p) == sum(d) + s
    tau, rank = solid_p(F, B, p, N1)
    W = [n for n in tau if in_window(n, d, s, S)]
    sub = all(tau[n] == 0 for n in W)
    k = len(S) - 1
    rmax = (k + 1) * s // k
    count = sum(comb(slice_side(r, s, k) + N1 - 1, N1 - 1) for r in range(rmax + 1))
    # slice shapes
    shapes = True
    for r in range(rmax + 1):
        sl = set(n for n in W if sum(n) - sum(d) == r)
        Lr = slice_side(r, s, k)
        base = [max(0, r - s) if i in S else 0 for i in range(N1)]
        pred = set(tuple(d[i] + base[i] + y[i] for i in range(N1)) for y in itertools.product(range(Lr + 1), repeat=N1) if sum(y) == Lr)
        # points with coordinates beyond box excluded
        pred = set(x for x in pred if all(c <= B for c in x))
        shapes &= sl == pred
    ok = sub and count == len(W) and shapes
    w5_ok &= ok
    w5_info.append((d, s, S, len(W), count, sub, shapes))
report("W5", w5_ok, f"planted (d,s,S,|W|,count,W<=Z,slices): {w5_info}")

# ======================================================================= W6
w6_bad = 0; w6_sq = 0; w6_dep = 0; w6_depbad = 0
for p in (2, 3, 5):
    for seed in range(5):
        rng = random.Random(7000 + 100 * p + seed)
        B = 14; L = 2 * B + 60
        F = rand_series(2, L, p, rng)
        tau, rank = solid_p(F, B, p, 2)
        Z = [n for n in tau if tau[n] == 0]
        gens, _ = generators_p(F, Z, p, L, 2)
        for n in itertools.product(range(B), repeat=2):
            G = set()
            for v in itertools.product((0, 1), repeat=2):
                m = (n[0] + v[0], n[1] + v[1])
                G |= set(g for g in gens if in_window(m, *g))
            w6_sq += 1
            w6_bad += len(G) > 1
        for n in Z:
            cover = [g for g in gens if in_window(n, *g)]
            d, s, S = cover[0][:3]
            k = [x - y for x, y in zip(n, d)]
            mu = min(k[i] for i in S)
            w6_dep += 1
            w6_depbad += (1 + min(mu, s - (sum(k) - mu))) != sum(n) - rank[n]
report("W6", w6_bad == 0 and w6_depbad == 0, f"N=1: {w6_sq} unit squares checked, {w6_bad} meet two generators; depth formula at all {w6_dep} zeros, {w6_depbad} failures")

# ======================================================================= W10
def S_wall(c, m, q):
    if m == 0:
        return Fr(1)
    return det_rank_q([[Fr(c[q + i - j]) for j in range(m)] for i in range(m)])[0]

def tau3(c, n0, n1, n2):
    N = n0 + n1 + n2
    if N == 0:
        return Fr(1)
    cols = [[Fr(int(k == j)) for k in range(N)] for j in range(n0)]
    cols += [[Fr(c[k - j]) for k in range(N)] for j in range(n1)]
    cols += [[Fr(c[k + j]) for k in range(N)] for j in range(1, n2 + 1)]
    return det_rank_q([[cols[col][row] for col in range(N)] for row in range(N)])[0]

rng = random.Random(31)
c = {k: rng.randint(-4, 4) for k in range(-40, 41)}
w10_map = w10_hir = w10_cross = 0; w10_tot = 0
for n in itertools.product(range(4), repeat=3):
    eps = (-1) ** (n[1] * n[2] + n[2] * (n[2] - 1) // 2)
    w10_tot += 1
    w10_map += tau3(c, *n) != eps * S_wall(c, n[1] + n[2], n[0] + n[2])
for n in itertools.product(range(3), repeat=3):
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    ad = lambda *v: tuple(map(sum, zip(*v)))
    T = lambda x: tau3(c, *x)
    v = T(ad(n, e[0])) * T(ad(n, e[1], e[2])) - T(ad(n, e[1])) * T(ad(n, e[0], e[2])) + T(ad(n, e[2])) * T(ad(n, e[0], e[1]))
    w10_hir += v != 0
for m in range(5):
    for q in range(-6, 6):
        w10_cross += S_wall(c, m + 2, q + 1) * S_wall(c, m, q + 1) != S_wall(c, m + 1, q + 1) ** 2 - S_wall(c, m + 1, q + 2) * S_wall(c, m + 1, q)
report("W10", w10_map == 0 and w10_hir == 0 and w10_cross == 0, f"three-family solid = signed number wall ({w10_tot} pts, {w10_map} fail); Hirota fails {w10_hir}; cross rule fails {w10_cross}")

# ======================================================================= W7
def pmul(a, b, p):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return out

def padd(a, b, p):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)]

def pdet(rows, p):
    n = len(rows)
    tot = []
    for perm in itertools.permutations(range(n)):
        sgn = 1
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    sgn = -sgn
        term = [1]
        for i in range(n):
            term = pmul(term, rows[i][perm[i]], p)
        if sgn < 0:
            term = [(-x) % p for x in term]
        tot = padd(tot, term, p)
    return any(tot)

w7_bad = 0; w7_cubes = 0; w7_sharp = 0
for (p, N1, B) in ((2, 3, 6), (3, 3, 6), (2, 4, 3)):
    for seed in range(2):
        rng = random.Random(9000 + 10 * p + N1 + seed)
        L = N1 * B + 60
        F = rand_series(N1, L, p, rng)
        tau, rank = solid_p(F, B, p, N1)
        Z = [n for n in tau if tau[n] == 0]
        _, kers = generators_p(F, Z, p, L, N1)
        for n in itertools.product(range(B), repeat=N1):
            vecs = []
            for v in itertools.product((0, 1), repeat=N1):
                m = tuple(x + y for x, y in zip(n, v))
                vecs += kers.get(m, [])
            if not vecs:
                continue
            w7_cubes += 1
            # dedupe
            uniq = []
            for a in vecs:
                key = tuple(tuple(x) for x in a)
                if key not in [tuple(tuple(x) for x in b) for b in uniq]:
                    uniq.append(a)
            if len(uniq) > 12:
                uniq = uniq[:12]
            full = any(pdet([u for u in sub], p) for sub in itertools.combinations(uniq, N1)) if len(uniq) >= N1 else False
            w7_bad += full
            if N1 == 3 and len(uniq) >= 2:
                if any(pdet([[a[i] for i in cols] for a in sub], p) for sub in itertools.combinations(uniq, 2) for cols in itertools.combinations(range(3), 2)):
                    w7_sharp += 1
report("W7", w7_bad == 0 and w7_sharp > 0, f"{w7_cubes} unit cubes with kernels; rank N+1 found in {w7_bad}; N=2 cubes attaining rank 2: {w7_sharp}")

# ======================================================================= W8
tau, rank = QSOL["exp(z^2),exp(z^2+z^3)"]
pyr = {(0, 1, 1), (1, 1, 1), (0, 2, 1), (0, 1, 2), (0, 2, 2)}
win_c = set(n for n in tau if in_window(n, (0, 1, 1), 1, (1, 2)))
a_ok = tau[(1, 1, 0)] == 0 and tau[(1, 1, 1)] == 0 and win_c == pyr and all(tau[n] == 0 for n in pyr) \
    and not in_window((1, 1, 1), (1, 1, 0), 0, (0, 1)) and not in_window((1, 1, 0), (0, 1, 1), 1, (1, 2))
L = 16
Fb = [[Fr(1)] + [Fr(0)] * (L - 1), exp_series({3: 1}, L), exp_series({3: 1, 4: 1}, L)]
t, r = det_rank_q(build_M(Fb, (1, 1, 1)))
b_ok = t == 0 and 3 - r == 2
dirs = Counter()
for seed in range(6):
    rng = random.Random(500 + seed)
    p = 5; B = 8; L = 3 * B + 60
    F = [[1] + [0] * (L - 1)] + [[rng.randrange(1, p)] + [rng.randrange(p) for _ in range(L - 1)] for _ in range(2)]
    tau5, rank5 = solid_p(F, B, p, 3)
    Z = [n for n in tau5 if tau5[n] == 0]
    gens, _ = generators_p(F, Z, p, L, 3)
    cov = {n: set(g for g in gens if in_window(n, *g)) for n in Z}
    for n in Z:
        for dl in itertools.product((-1, 0, 1), repeat=3):
            m = tuple(x + y for x, y in zip(n, dl))
            if any(dl) and m in cov and cov[n].isdisjoint(cov[m]):
                dirs[dl] += 1
c_ok = len(dirs) == 26
report("W8", a_ok and b_ok and c_ok, f"(a) touching pyramid example {a_ok}; (b) corank M(1,1,1)={3 - r} overlap {b_ok}; (c) king directions realized {len(dirs)}/26")

# ======================================================================= W9
def facet_geometric(N1, d, s, S, tau, p):
    add = lambda x, y: tuple(i + j for i, j in zip(x, y))
    E = [tuple(int(t == i) for t in range(N1)) for i in range(N1)]
    ok = bad = 0
    for i in S:
        lay = set(n for n in tau if n[i] == d[i] - 1 and in_window(add(n, E[i]), d, s, S))
        for u in E:
            if u[i]:
                continue
            for n in lay:
                q = [n, add(n, u), add(add(n, u), u)]
                if all(x in lay for x in q):
                    if tau[q[0]] * tau[q[2]] % p == tau[q[1]] ** 2 % p:
                        ok += 1
                    else:
                        bad += 1
    return ok, bad

out9 = {}
p = 101
for (d, s) in [((3, 3), 5), ((3, 3, 3), 4), ((2, 3, 4), 3)]:
    rng = random.Random(hash((d, s, 9)) & 0xffff)
    N1 = len(d); B = max(d) + s + 2; L = N1 * B + 40
    F, a, S = plant(p, d, s, L, rng)
    tau, rank = solid_p(F, B, p, N1)
    out9[str(d)] = facet_geometric(N1, d, s, S, tau, p)
n1 = out9[str((3, 3))]
n2 = [out9[str((3, 3, 3))], out9[str((2, 3, 4))]]
report("W9", n1[1] == 0 and all(b > 0 for _, b in n2), f"lower facet layers geometric (ok,bad): N=1 {n1}; N=2 {n2} (observation)")

print(f"\nTotal time {time.time() - T0:.1f}s; {sum(v['pass'] for v in RESULTS.values())}/{len(RESULTS)} PASS")
json.dump(RESULTS, open(__file__.replace(".py", "_results.json"), "w"), indent=1, default=str)
