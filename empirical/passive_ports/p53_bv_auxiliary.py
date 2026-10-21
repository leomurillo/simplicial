"""Explicit mollified-Mobius auxiliary plus minimal repair (Paper 53 §4.12, target), certificate K10f.

Base: Barban–Vehov weights  c0_k = mu(k) for k <= z1,  mu(k) log(z2/k)/log(z2/z1) for z1 < k <= z2,  0 beyond,
with z1 = a x^{1/4}, z2 = sqrt(x).  Measured: how far G_{c0} is from positivity on J(x), its Stirling moments, and the
cheapest repair d (a priori LP over d with c = c0 + d, all k <= x/2 grouped as in p53_apriori_full.py) against E*(x).
"""
import math
import sys
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from p53_chebyshev_lp import J_of, mobius
from p53_apriori_lp import S, b
from p53_apriori_full import groups

if __name__ == "__main__":
    mu = mobius(4 * 10**6)
    for x in [int(float(a)) for a in sys.argv[1:]]:
        J = J_of(x); G = groups(x); s = math.sqrt(x); L = math.log(x)
        for a in (1.0, 3.0):
            z1, z2 = a * x**0.25, s
            # base vector on k (k <= z2 < sqrt x  => every k is its own group m = floor(x/k))
            kk = np.arange(1, int(z2) + 1)
            w = np.where(kk <= z1, 1.0, np.clip(np.log(z2 / kk) / math.log(z2 / z1), 0, 1))
            c0k = mu[kk] * w
            A0 = (J[:, None] // kk[None, :] - J[:, None] // (2 * kk[None, :])).astype(float)
            g0 = A0 @ c0k - (J == 1)
            C1 = float(np.sum(c0k / kk)); dC = float(-np.sum(c0k * np.log(kk) / kk))
            E0 = 0.5 * x * (C1 * (L + math.log(2) - 1) + dC) + float(np.sum(np.abs(c0k) * np.array([b(x / k) for k in kk])))
            # repair LP over all groups: c = c0 + d, minimize E(c) exactly (|c| split), subject to G_c >= [j=1]
            rows, cols, vals = [], [], []
            for col, (m, kmax, ylo, yhi) in enumerate(G):
                idx = np.nonzero(J >= kmax)[0]
                v = J[idx] // kmax - J[idx] // (2 * kmax)
                nz = v != 0
                rows.append(idx[nz]); cols.append(np.full(int(nz.sum()), col)); vals.append(v[nz].astype(float))
            A = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(len(J), len(G)))
            base = np.zeros(len(G))
            col_of_k = {g[1]: i for i, g in enumerate(G)}
            for k, v in zip(kk, c0k):
                base[col_of_k[x // (x // k)] if (x // (x // k)) in col_of_k else col_of_k[k]] += v
            cp = np.array([S(g[2]) + b(g[2]) for g in G]); cm = np.array([-S(g[3]) + b(g[3]) for g in G])
            # variables: c = p - q (p,q >= 0); minimize cp.p + cm.q ; constraints A(p - q) >= rhs.  Repair size = |c - c0|.
            res = linprog(np.concatenate([cp, cm]), A_ub=-sp.hstack([A, -A]).tocsr(), b_ub=-(J == 1).astype(float),
                          bounds=[(0, None)] * (2 * len(G)), method="highs")
            cstar = res.x[:len(G)] - res.x[len(G):]
            print(f"x = {x:.0e}, z1 = {a:.0f} x^(1/4): base BV: min_J (G - [j=1]) = {g0.min():+.2f} on {int(np.sum(g0 < -1e-9))}/{len(J)} scales;"
                  f"  C(1) = {C1:+.2e}, C'(1)-1 = {dC - 1:+.2e};  E(c0)-x/2 = {E0 - x/2:+.1f} (infeasible base)."
                  f"  Optimum E*-x/2 = {res.fun - x/2:.1f};  |c* - c0|_1 = {np.sum(np.abs(cstar - base)):.1f}, |c0|_1 = {np.sum(np.abs(c0k)):.1f}", flush=True)


def l1_split(x):
    """l1 mass of the unlimited-complexity a priori optimum on k <= sqrt x versus the groups k > sqrt x."""
    from p53_apriori_full import solve_full
    E, c, G, J, A, dt = solve_full(x)
    head = np.array([g[1] <= math.isqrt(x) for g in G])
    return float(np.sum(np.abs(c[head]))), float(np.sum(np.abs(c[~head])))
