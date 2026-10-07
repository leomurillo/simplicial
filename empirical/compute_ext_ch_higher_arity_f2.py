"""Compute dim Ext_CH^(n)(R) for n = 3, 4 via the chain complex (H_R^(•), d)
of Paper 11 Corollary 9.5.11, working over F_2.

Paper 11 Definition 9.5.1 says H_R^(n) is the "free R-module on closed n-cells";
since R = F_4[u]/(u^2) has characteristic 2, the natural ground ring is F_2
(or any characteristic-2 field), and the (-1)^(i+j) signs of d_{i,j} collapse
to +1. Under this reading d^2 = 0 holds, the cohomology is well-defined, and
the dimensions count F_2-vector-space cohomology.

The chain complex only uses additive structure of R, so as a vector space
Ext_CH^(n) depends only on the abelian group (Z/2)^4 (which is the additive
group of F_4[u]/(u^2), F_16, F_2^4, F_2[u]/(u^4)).

Strategy: build d_3, d_4, d_5 as 0/1 matrices over F_2 (reducing mod 2 the
multiplicities from oriented signs); verify d^2 = 0; compute F_2-rank.
"""

from __future__ import annotations

import numpy as np
from itertools import product

# Ground ring of cells = F_2; coefficients = F_2.
ORDER = 16


def add(x: int, y: int) -> int:
    return x ^ y


def enumerate_cells(arity: int) -> list[tuple[int, ...]]:
    if arity < 2:
        return []
    nonzero = list(range(1, ORDER))
    cells: list[tuple[int, ...]] = []
    for prefix in product(nonzero, repeat=arity - 1):
        s = 0
        for x in prefix:
            s = add(s, x)
        if s != 0:
            cells.append((*prefix, s))
    return cells


def build_differential_f2(arity: int,
                          cells_n: list[tuple[int, ...]],
                          index_nm1: dict[tuple[int, ...], int]) -> np.ndarray:
    """Build d_n: H^(n) -> H^(n-1) over F_2.
    Each (i,j) merge contributes +1 to the (output, input) entry; multiplicities
    sum mod 2."""
    nrows = len(index_nm1)
    ncols = len(cells_n)
    M = np.zeros((nrows, ncols), dtype=np.uint8)
    for col, cell in enumerate(cells_n):
        for i in range(arity):
            for j in range(i + 1, arity):
                merged = add(cell[i], cell[j])
                if merged == 0:
                    continue
                rest = tuple(cell[k] for k in range(arity) if k != i and k != j)
                out_cell = rest + (merged,)
                row = index_nm1[out_cell]
                M[row, col] ^= 1  # XOR for F_2 addition
    return M


def f2_rank(M: np.ndarray) -> int:
    """Rank of an F_2 matrix via Gaussian elimination."""
    A = M.copy()
    nrows, ncols = A.shape
    rank = 0
    row = 0
    for col in range(ncols):
        if row >= nrows:
            break
        pivot = -1
        for r in range(row, nrows):
            if A[r, col]:
                pivot = r
                break
        if pivot == -1:
            continue
        if pivot != row:
            A[[row, pivot]] = A[[pivot, row]]
        for r in range(nrows):
            if r != row and A[r, col]:
                A[r] ^= A[row]
        rank += 1
        row += 1
    return rank


def f2_matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Matrix multiplication over F_2 using bitwise operations."""
    # A: m x k, B: k x n; result is m x n.
    return ((A.astype(np.int32) @ B.astype(np.int32)) & 1).astype(np.uint8)


def main():
    print("=" * 70)
    print("Ext_CH^(n)(R) over F_2 for additive group (Z/2)^4")
    print("(applies to F_4[u]/(u^2) and other rings of order 16, char 2)")
    print("=" * 70)
    print()

    arities = [2, 3, 4, 5]
    cells = {}
    indices = {}
    for n in arities:
        cells[n] = enumerate_cells(n)
        indices[n] = {c: i for i, c in enumerate(cells[n])}
        expected = ((ORDER - 1) ** n + (ORDER - 1) * (-1) ** n) // ORDER
        print(f"  dim H^({n}) = {len(cells[n]):>6}   (expected {expected})  "
              f"{'OK' if len(cells[n]) == expected else 'MISMATCH'}")
    print()

    print("Building differentials over F_2 (signs collapse; +1 per merge)...")
    D = {}
    for n in [3, 4, 5]:
        D[n] = build_differential_f2(n, cells[n], indices[n - 1])
        nnz = int((D[n] != 0).sum())
        print(f"  d_{n}: {D[n].shape[0]:>6} x {D[n].shape[1]:>6}, nnz = {nnz}")
    print()

    print("Verifying d^2 = 0 over F_2:")
    for (n_low, n_high) in [(3, 4), (4, 5)]:
        prod = f2_matmul(D[n_low], D[n_high])
        nnz = int((prod != 0).sum())
        status = "OK" if nnz == 0 else f"FAIL: {nnz} nonzeros"
        print(f"  d_{n_low} o d_{n_high} = 0: {status}")
    print()

    print("Computing F_2-ranks...")
    ranks = {}
    for n in [3, 4]:
        ranks[n] = f2_rank(D[n])
        print(f"  rank d_{n} = {ranks[n]}")
    print(f"  rank d_5 (this is the expensive one, may take a few minutes)...")
    ranks[5] = f2_rank(D[5])
    print(f"  rank d_5 = {ranks[5]}")
    print()

    print("Cohomology dimensions over F_2:")
    for n in [3, 4]:
        ker_dim = len(cells[n]) - ranks[n]
        im_dim = ranks[n + 1]
        ext = ker_dim - im_dim
        print(f"  dim_F2 Ext_CH^({n}) = ({len(cells[n])} - {ranks[n]}) - {ranks[n+1]} "
              f"= {ker_dim} - {im_dim} = {ext}")
    print()

    # Also compute Ext_CH^(2) (which is dim H^(2) - rank d_3, since H^(1) = 0
    # implies ker d_2 = H^(2)):
    ker2_dim = len(cells[2])  # all of H^(2) is in the kernel of d_2 = 0
    im_to_2 = ranks[3]
    ext2 = ker2_dim - im_to_2
    print(f"  dim_F2 Ext_CH^(2) = {ker2_dim} - {im_to_2} = {ext2}  "
          f"(for consistency with Paper 11's binary case)")
    print()

    print("Euler-characteristic sanity:")
    # Since the truncated complex is finite, Sum (-1)^n dim H^(n) = Sum (-1)^n dim Ext^(n)
    # restricted to the same range — but we don't have Ext^(5).
    chi_chains = sum((-1) ** n * len(cells[n]) for n in arities)
    print(f"  Sum (-1)^n dim H^(n) (n=2..5) = {chi_chains}")


if __name__ == "__main__":
    main()
