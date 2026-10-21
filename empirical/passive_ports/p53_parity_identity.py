"""The parity identity in exact forms (Paper 53 §4.12), certificate K10(e).

(i)   Prime-2 cone.  Delta_n = complex of squarefree k <= n (faces = prime sets).  Delta_n = Delta^odd_n  U  cone_2(Delta^odd_{n/2}),
      so Delta_n ~ Delta^odd_n / Delta^odd_{n/2} = wedge of spheres S^{omega(k)-1}, one for each odd squarefree k in (n/2, n]
      (every proper face of such k is k/p <= n/3).  Check: reduced Betti numbers over GF(p) by exact rank, n <= 90.
(ii)  M(n) = sum over odd squarefree k in (n/2, n] of mu(k)  (= -reduced Euler characteristic), n <= 10^6.
(iii) Squares: sum_{d<=x} lambda(d) floor(x/d) = floor(sqrt x), and v_p( prod_d floor(x/d)!^lambda(d) ) = sum_r floor(sqrt(x/p^r)).
(iv)  F_q[T]: window Mobius sums  sum_{deg f = n, T not | f} mu(f) = 1 - q  for every n >= 1 (the structural identity 1/Z = 1 - qT).
"""
import itertools
import math
import numpy as np
from sympy import factorint, Poly, GF, symbols, primerange
from sympy.polys.galoistools import gf_sqf_p, gf_factor_sqf

PR = 1_000_003


def rank_mod(M, p=PR):
    M = [list(r) for r in M]
    if not M or not M[0]:
        return 0
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(v * inv) % p for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r


def squarefree_faces(n):
    faces = {}
    for k in range(1, n + 1):
        f = factorint(k)
        if all(e == 1 for e in f.values()):
            faces[k] = tuple(sorted(f))
    return faces


def reduced_betti(n):
    faces = squarefree_faces(n)
    by_dim = {}
    for k, ps in faces.items():
        by_dim.setdefault(len(ps) - 1, []).append(ps)
    dims = sorted(by_dim)
    idx = {d: {s: i for i, s in enumerate(by_dim[d])} for d in dims}
    rk = {}
    for d in dims:
        if d - 1 not in by_dim:
            continue
        M = [[0] * len(by_dim[d]) for _ in by_dim[d - 1]]
        for j, s in enumerate(by_dim[d]):
            for t in range(len(s)):
                M[idx[d - 1][s[:t] + s[t + 1:]]][j] = (-1) ** t
        rk[d] = rank_mod(M)
    return {d: len(by_dim[d]) - rk.get(d, 0) - rk.get(d + 1, 0) for d in dims}   # includes the empty face at d=-1


if __name__ == "__main__":
    print("(i) prime-2 cone: reduced Betti numbers of Delta_n vs odd squarefree k in (n/2, n] by omega(k)")
    ok = True
    for n in list(range(2, 61)) + [72, 90]:
        b = reduced_betti(n)
        pred = {}
        for k in range(n // 2 + 1, n + 1):
            f = factorint(k)
            if k % 2 and all(e == 1 for e in f.values()):
                pred[len(f) - 1] = pred.get(len(f) - 1, 0) + 1
        got = {d: v for d, v in b.items() if v}
        ok &= got == pred
        if n in (10, 30, 60, 90):
            print(f"   n = {n}: reduced Betti {got}  predicted {pred}")
    print(f"   all n in [2,60] and 72, 90 agree: {ok}")

    N = 10**6
    mu = np.ones(N + 1, dtype=np.int64); mu[0] = 0
    lam = np.ones(N + 1, dtype=np.int64); lam[0] = 0
    isp = np.ones(N + 1, bool); isp[:2] = False
    for p in range(2, N + 1):
        if isp[p]:
            isp[p * p::p] = False
            mu[p::p] *= -1; mu[p * p::p * p] = 0
            pk = p
            while pk <= N:
                lam[pk::pk] *= -1; pk *= p
    M = np.cumsum(mu)
    oddmu = np.where(np.arange(N + 1) % 2 == 1, mu, 0); Co = np.cumsum(oddmu)
    ns = np.arange(2, N + 1)
    print(f"\n(ii) M(n) = sum_(odd sqfree k in (n/2,n]) mu(k) for all 2 <= n <= 10^6: {bool(np.all(M[ns] == Co[ns] - Co[ns // 2]))}")

    print("\n(iii) squares: sum_(d<=x) lambda(d) floor(x/d) = floor(sqrt x)")
    allok = True
    for x in list(range(1, 3001)) + [10**5, 999_999, 10**6]:
        d = np.arange(1, x + 1)
        allok &= int(np.sum(lam[1:x + 1] * (x // d))) == math.isqrt(x)
    print(f"   x in [1,3000] and 1e5, 999999, 1e6: {allok}")
    x = 5000
    vals = []
    md = x // np.arange(1, x + 1)
    for p in primerange(2, x + 1):
        vfac = np.zeros(x, dtype=np.int64); pr = p
        while pr <= x:
            vfac += md // pr; pr *= p
        v_left = int(np.sum(lam[1:x + 1] * vfac))
        v_right = sum(math.isqrt(x // p**r) for r in range(1, 40) if p**r <= x)
        vals.append(v_left == v_right)
    print(f"   v_p(prod_d floor(x/d)!^lambda(d)) = sum_r floor(sqrt(x/p^r)) for all p <= x = {x}: {all(vals)}"
          f"  (an integer with multiplicity floor(sqrt(x/p)) at p)")

    print("\n(iv) F_q[T]: window Mobius sums over squarefree f, deg f = n, T not dividing f")
    for q, nmax in ((3, 7), (5, 5)):
        dom = GF(q)
        out = []
        for n in range(1, nmax + 1):
            tot = 0
            for coeffs in itertools.product(range(q), repeat=n):
                if coeffs[-1] == 0:          # constant term 0 <=> T | f
                    continue
                f = [1] + list(coeffs)
                if not gf_sqf_p(f, q, dom):
                    continue
                tot += (-1) ** len(gf_factor_sqf(f, q, dom)[1])
            out.append(tot)
        print(f"   q = {q}: n = 1..{nmax}: {out}   (predicted 1 - q = {1 - q} for every n)")
