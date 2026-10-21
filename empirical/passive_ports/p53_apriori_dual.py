"""The a priori polytope from the dual side: the extremal fake prime measure (Paper 53 §4.12(c)), certificate K10d'.

E*(x) = max z_1  over  z >= 0 on J(x)  with  -cm_m <= sum_j z_j A(j,m) <= cp_m  for every column group m
(cp, cm: Stirling bracket ends, as in p53_apriori_full.py).  Two-sided rows, no duplicated matrix, so x = 1e7 fits.
Also reports how the extremal fake measure z* differs from the true prime masses z^Lambda.
Usage: python p53_apriori_dual.py x1 x2 ...
"""
import math
import sys
import time
import numpy as np
import scipy.sparse as sp
from scipy.optimize import milp, LinearConstraint, Bounds
from p53_chebyshev_lp import J_of, psi_table
from p53_apriori_lp import S, b
from p53_apriori_full import groups


def dual(x):
    J = J_of(x)
    G = groups(x)
    rows, cols, vals = [], [], []
    for r, (m, kmax, ylo, yhi) in enumerate(G):
        idx = np.nonzero(J >= kmax)[0]
        v = J[idx] // kmax - J[idx] // (2 * kmax)
        nz = v != 0
        rows.append(np.full(int(nz.sum()), r)); cols.append(idx[nz]); vals.append(v[nz].astype(float))
    AT = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(len(G), len(J)))
    up = np.array([S(g[2]) + b(g[2]) for g in G]); lo = np.array([S(g[3]) - b(g[3]) for g in G])
    obj = -(J == 1).astype(float)
    t0 = time.time()
    res = milp(obj, constraints=LinearConstraint(AT, lo, up), bounds=Bounds(0, np.inf), integrality=np.zeros(len(J)))
    if not res.success:
        raise RuntimeError(res.message)
    return -res.fun, res.x, J, AT.nnz, time.time() - t0


if __name__ == "__main__":
    xs = [int(float(a)) for a in sys.argv[1:]]
    psi, _ = psi_table(max(xs))
    for x in xs:
        E, z, J, nnz, dt = dual(x)
        s = math.sqrt(x); L = math.log(x)
        zt = np.array([psi[x // j] - psi[x // (j + 1)] for j in J])      # true masses on each class
        big = J > math.isqrt(x)                                           # single-n classes (n < sqrt x)
        win = psi[x] - psi[x // 2]
        print(f"x = {x:.2e}: |J| = {len(J)}, nnz = {nnz}:  E* - x/2 = {E - x/2:11.2f} = {(E - x/2)/s:6.3f} sqrt x"
              f" = {(E - x/2)/(s*L):6.4f} sqrt x log x;  window - x/2 = {win - x/2:9.2f};"
              f"  fake vs true: sum|z*-z^Lambda| on n<sqrt x = {np.sum(np.abs(z - zt)[big]):.1f},"
              f" on n>=sqrt x = {np.sum(np.abs(z - zt)[~big]):.1f};  fake mass on composite n<sqrt x = {np.sum(z[big & (zt == 0)]):.1f}"
              f"   [{dt:.0f}s]", flush=True)
