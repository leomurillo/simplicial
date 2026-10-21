"""Where the optimal factorial auxiliary becomes exact, and why (Paper 53 §4.12), certificate K10(b).

H*(x,K) = optimal value of the prime-free LP of p53_chebyshev_lp.py.  Duality: H*(x,K) = max z_1 over fake prime
masses z >= 0 on J reproducing the first K factorial identities.  Two thresholds are measured:
  K_LP(x)    : smallest K on a grid with H*(x,K) = psi(x) - psi(x/2) to 1e-6 (the auxiliary is exact);
  K_exact(x) : smallest K with an exact prime-free vector, G_c(j) = [j = 1] for EVERY j in J (least-squares residual).
At K_LP the optimal G* vanishes on the classes floor(x/n) that carry a prime power and may be positive elsewhere:
the LP solution is adapted to the primes below sqrt(x), i.e. it is the Legendre sieve.
"""
import math
import numpy as np
from scipy.optimize import linprog
from p53_chebyshev_lp import J_of, F, solve, psi_table, mobius


def lsq_residual(x, K, J):
    ks = np.arange(1, K + 1, dtype=np.int64)
    A = (J[:, None] // ks[None, :] - J[:, None] // (2 * ks[None, :])).astype(float)
    A, idx = np.unique(A, axis=1, return_index=True)        # identical columns (same floor(x/k) beyond sqrt x)
    b = (J == 1).astype(float)
    c, *_ = np.linalg.lstsq(A, b, rcond=None)
    return float(np.max(np.abs(A @ c - b))), int(np.linalg.matrix_rank(A)), A.shape[1]


if __name__ == "__main__":
    psi, sieve = psi_table(10**6)
    mu = mobius(10**5)
    is_pp = np.zeros(10**6 + 1, bool)
    for p in np.nonzero(sieve)[0]:
        pk = int(p)
        while pk <= 10**6:
            is_pp[pk] = True; pk *= int(p)
    for x in (1000, 10**4, 10**5):
        J = J_of(x); s = math.isqrt(x)
        win = psi[x] - psi[x // 2]
        print(f"x = {x}: |J| = {len(J)}, sqrt x = {s}, window = {win:.6f}")
        K_LP = None
        for r in (1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.5, 4.0):
            K = int(r * s)
            H, c, z, _, A = solve(x, K, J)
            res, rank, ncol = lsq_residual(x, K, J)
            tag = ""
            if K_LP is None and abs(H - win) < 1e-6:
                K_LP = K; tag = "  <- K_LP"
            print(f"   K = {K:6d} ({r:4.2f} sqrt x): H*-window = {H - win:12.6f}   rank(A_J,K) = {rank:5d}/{len(J)}"
                  f" ({ncol} distinct columns)   exact-on-J residual = {res:.2e}{tag}")
            if K_LP == K:
                G = A @ c
                n_of = {int(j): [] for j in J}
                for n in range(2, x + 1):
                    if x // n <= x // 2:
                        n_of[x // n].append(n)
                pp_cls = np.array([any(is_pp[n] for n in n_of[int(j)]) for j in J])
                print(f"      at K_LP: max G* on prime-power classes (j>=2) = {np.max(G[(J >= 2) & pp_cls]):.2e};"
                      f"  classes with no prime power: {int(np.sum(~pp_cls & (J >= 2)))}, of which G* > 1e-9 on "
                      f"{int(np.sum((G > 1e-9) & ~pp_cls & (J >= 2)))};  c* = mu on [1,sqrt x]: "
                      f"{bool(np.all(np.round(c[:s]) == mu[1:s + 1]))};  max|c*| = {np.max(np.abs(c)):.3f};"
                      f"  c* integral: {bool(np.max(np.abs(c - np.round(c))) < 1e-7)}")
        Kfull = x // 2
        res, rank, ncol = lsq_residual(x, Kfull, J)
        print(f"   K = x/2 = {Kfull}: rank = {rank}/{len(J)}, exact-on-J residual = {res:.2e} (full Mobius is exact)\n")
