"""The a priori factorial bound at unlimited complexity, E*(x) = E*(x, x/2) (Paper 53 §4.12), certificate K10(d).

On J(x) the column of every k with the same m = floor(x/k) is the same vector (floor(floor(x/n)/k) = floor(m/n)),
so all k <= x/2 collapse to ~2 sqrt(x) column groups m.  Within a group, Stirling's bracket is tightest at the group's ends:
    F(m) <= S(y) + b(y)  at y = x/floor(x/m)         (cost of a positive coefficient)
   -F(m) <= -S(y) + b(y) at y = x/(floor(x/(m+1))+1)  (cost of a negative coefficient)
E*(x) = min sum_m (cp_m (S+b)(y_m^-) + cm_m (-S+b)(y_m^+))  s.t.  G(j) = sum_m (cp_m - cm_m) A(j,m) >= [j = 1] on J.
Rigorous for every x:  psi(x) - psi(x/2) <= E*(x).  No prime, no exact factorial, no zero enters.
Usage: python p53_apriori_full.py x1 x2 ...
"""
import math
import sys
import time
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from p53_chebyshev_lp import J_of, psi_table
from p53_apriori_lp import S, b


def groups(x):
    ms = sorted({x // k for k in range(1, x // 2 + 1)} if x <= 10**6 else
                set(range(2, math.isqrt(x) + 2)) | {x // k for k in range(1, math.isqrt(x) + 2)})
    ms = [m for m in ms if m >= 2]
    out = []
    for m in ms:
        kmax = x // m
        kmin = x // (m + 1) + 1
        if kmin > kmax or x // kmax != m:
            continue
        out.append((m, kmax, x / kmax, x / kmin))
    return out


def solve_full(x):
    J = J_of(x)
    G = groups(x)
    rows, cols, vals = [], [], []
    for c, (m, kmax, ylo, yhi) in enumerate(G):
        k = kmax
        idx = np.nonzero(J >= k)[0]
        v = J[idx] // k - J[idx] // (2 * k)
        nz = v != 0
        rows.append(idx[nz]); cols.append(np.full(int(nz.sum()), c)); vals.append(v[nz].astype(float))
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    A = sp.csr_matrix((vals, (rows, cols)), shape=(len(J), len(G)))
    cp = np.array([S(g[2]) + b(g[2]) for g in G]); cm = np.array([-S(g[3]) + b(g[3]) for g in G])
    rhs = (J == 1).astype(float)
    t0 = time.time()
    res = linprog(np.concatenate([cp, cm]), A_ub=-sp.hstack([A, -A]).tocsr(), b_ub=-rhs,
                  bounds=[(0, None)] * (2 * len(G)), method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    c = res.x[:len(G)] - res.x[len(G):]
    return res.fun, c, G, J, A, time.time() - t0


if __name__ == "__main__":
    psi, _ = psi_table(10**7)
    for x in [int(float(a)) for a in sys.argv[1:]]:
        E, c, G, J, A, dt = solve_full(x)
        s = math.sqrt(x); L = math.log(x)
        win = psi[x] - psi[x // 2] if x <= 10**7 else float("nan")
        l1 = float(np.sum(np.abs(c)))
        print(f"x = {x:.2e}: groups {len(G)}, |J| = {len(J)}, nnz = {A.nnz}:  E* - x/2 = {E - x/2:11.2f} = {(E - x/2)/s:6.3f} sqrt x"
              f" = {(E - x/2)/(s*L):6.4f} sqrt x log x = {(E - x/2)/(s*L*L):7.5f} sqrt x log^2 x;   window - x/2 = {win - x/2:9.2f};"
              f"  l1 = {l1:9.1f} = {l1/(s*L):.4f} sqrt x log x   [{dt:.0f}s]", flush=True)
