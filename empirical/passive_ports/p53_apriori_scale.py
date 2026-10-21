"""Scaling of the a priori (Stepanov-type) factorial bound (Paper 53 §4.12), certificate K10(d).

E*(x,K) = min over c in R^K of  sum_k c_k S(x/k) + sum_k |c_k| b(x/k)
          subject to  G_c(1) >= 1,  G_c(j) >= 0  (j in J(x)),   G_c(j) = sum_k c_k (floor(j/k) - floor(j/2k)).
No prime and no exact factorial enters.  For every x:  psi(x) - psi(x/2) <= E*(x,K)  (rigorous, given b, checked to 1e7
in p53_apriori_lp.py).  Sparse constraint matrix (nonzeros ~ x/2 + K |J ∩ (K, x/2]|).  Usage: python p53_apriori_scale.py x r1 r2 ...
"""
import math
import sys
import time
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from p53_chebyshev_lp import J_of
from p53_apriori_lp import S, b


def apriori_sparse(x, K, J):
    rows, cols, vals = [], [], []
    for i, j in enumerate(J):
        kmax = min(int(j), K)
        ks = np.arange(1, kmax + 1, dtype=np.int64)
        v = j // ks - j // (2 * ks)
        nz = np.nonzero(v)[0]
        rows.append(np.full(len(nz), i)); cols.append(ks[nz] - 1); vals.append(v[nz].astype(float))
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    A = sp.csr_matrix((vals, (rows, cols)), shape=(len(J), K))
    rhs = (J == 1).astype(float)
    ks = np.arange(1, K + 1)
    s = np.array([S(x / k) for k in ks]); bb = np.array([b(x / k) for k in ks])
    cost = np.concatenate([s + bb, -s + bb])
    res = linprog(cost, A_ub=-sp.hstack([A, -A]).tocsr(), b_ub=-rhs, bounds=[(0, None)] * (2 * K), method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    c = res.x[:K] - res.x[K:]
    return res.fun, c, A.nnz


if __name__ == "__main__":
    x = int(float(sys.argv[1]))
    J = J_of(x); s = math.isqrt(x)
    for r in [float(a) for a in sys.argv[2:]]:
        K = int(r * s)
        t0 = time.time()
        E, c, nnz = apriori_sparse(x, K, J)
        L = math.log(x)
        print(f"x = {x:.0e}  K = {K:6d} ({r:4.2f} sqrt x)  |J| = {len(J)}  nnz = {nnz}:  E* - x/2 = {E - x/2:12.2f}"
              f"  = {(E - x/2)/s:7.3f} sqrt x = {(E - x/2)/(s*L*L):7.4f} sqrt x log^2 x   l1 = {np.sum(np.abs(c)):9.2f}"
              f" = {np.sum(np.abs(c))/(s*L):6.4f} sqrt x log x   [{time.time()-t0:.0f}s]", flush=True)
