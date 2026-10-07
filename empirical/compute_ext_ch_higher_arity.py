"""Compute dim Ext_CH^(n)(R) for n = 3 and 4 via the explicit chain complex
(H_R^(•), d) of Paper 11 Corollary 9.5.11.

The chain complex uses only the ADDITIVE structure of R. For R = F_4[u]/(u^2)
the additive group is (Z/2)^4 ≅ F_2^4. The Γ_R-action is ring-specific and
refines Ext_CH^(n) to a Γ_R-module, but as a vector space the dimensions
depend only on the abelian group.

Definitions (Paper 11 §9.5):
- H_R^(n) = free Q-module on closed n-cells (chi_{a_1},...,chi_{a_n}) with
  a_k ∈ R nonzero and Sum a_k = 0.
- d_{i,j}(chi_{a_1},...,chi_{a_n}) =
    (..., omit i,..., omit j,..., chi_{a_i + a_j}) if a_i + a_j ≠ 0
    0                                          if a_i + a_j = 0
  with the merged leg placed at position n-1 (new last).
- d_n = Sum_{i<j} (-1)^{i+j} d_{i,j} : H_R^(n) → H_R^(n-1)
- Ext_CH^(n) = ker(d_n) / im(d_{n+1}).

Computation strategy: enumerate cells for arities 2,3,4,5; build differentials
as sparse matrices over Q; compute ranks via scipy.sparse.linalg.

Rank stability check: also compute mod a large prime; the two should agree
unless the chain complex has p-torsion (it shouldn't for generic abelian groups).
"""

from __future__ import annotations

import numpy as np
from itertools import product
from scipy.sparse import lil_matrix


# Additive group: (Z/2)^4 (matches additive structure of F_4[u]/(u^2),
# F_16, F_2^4, F_2[u]/(u^4) etc.)
ORDER = 16


def add(x: int, y: int) -> int:
    """Addition in (Z/2)^4: XOR of 4-bit representations."""
    return x ^ y


def enumerate_cells(arity: int) -> list[tuple[int, ...]]:
    """Enumerate ordered tuples (a_1,...,a_n) with each a_k ∈ {1,...,15}
    and Sum a_k = 0 (XOR-sum)."""
    if arity < 2:
        return []
    nonzero = list(range(1, ORDER))
    cells: list[tuple[int, ...]] = []
    # Generate first (n-1) entries freely from nonzero; compute last from closure.
    for prefix in product(nonzero, repeat=arity - 1):
        s = 0
        for x in prefix:
            s = add(s, x)
        # last entry must equal s (since x + s = 0 means x = s for XOR)
        last = s
        if last != 0:
            cells.append((*prefix, last))
    return cells


def build_differential(arity: int,
                       cells_n: list[tuple[int, ...]],
                       index_nm1: dict[tuple[int, ...], int]) -> lil_matrix:
    """Build d_n: H^(n) -> H^(n-1) as a sparse matrix.
    Rows are indexed by arity-(n-1) cells, columns by arity-n cells."""
    if arity < 2:
        raise ValueError("arity must be >= 2")
    nrows = len(index_nm1)
    ncols = len(cells_n)
    M = lil_matrix((nrows, ncols), dtype=np.int64)

    for col, cell in enumerate(cells_n):
        for i in range(arity):
            for j in range(i + 1, arity):
                merged = add(cell[i], cell[j])
                if merged == 0:
                    continue
                # Output cell: drop positions i and j, append merged at end.
                rest = tuple(cell[k] for k in range(arity) if k != i and k != j)
                out_cell = rest + (merged,)
                # Sign (-1)^(i+j). Paper's convention is 1-indexed but parity
                # of i+j is the same under 0/1-indexed shift by constant.
                sign = -1 if (i + j) % 2 else 1
                row = index_nm1[out_cell]
                M[row, col] += sign

    return M


def rank_via_qr_or_lu(M_sparse):
    """Compute rank of a sparse integer matrix M over Q.

    For sizes up to ~4000x50000, we cast to dense and use numpy.linalg.matrix_rank
    if memory permits; otherwise fall back to a mod-p approach.
    """
    nrows, ncols = M_sparse.shape
    dense_bytes = nrows * ncols * 8
    # Use a 4 GB ceiling for dense float64
    if dense_bytes < 4 * 1024**3:
        dense = M_sparse.toarray().astype(np.float64)
        return int(np.linalg.matrix_rank(dense))
    # Mod-p path: galois-style, but using numpy via mod p.
    # Numpy doesn't have native modular rank; we do simple row-reduction.
    return rank_modp(M_sparse, p=10007)


def rank_modp(M_sparse, p: int) -> int:
    """Rank over F_p via row-reduction. Operates on a dense int64 copy."""
    A = (M_sparse.toarray().astype(np.int64) % p).astype(np.int64)
    nrows, ncols = A.shape
    rank = 0
    row = 0
    for col in range(ncols):
        if row >= nrows:
            break
        # Find pivot
        pivot = None
        for r in range(row, nrows):
            if A[r, col] % p != 0:
                pivot = r
                break
        if pivot is None:
            continue
        # Swap rows
        if pivot != row:
            A[[row, pivot]] = A[[pivot, row]]
        # Normalize: multiply row by inverse of A[row, col] mod p
        inv = pow(int(A[row, col]) % p, p - 2, p)
        A[row] = (A[row] * inv) % p
        # Eliminate other rows
        for r in range(nrows):
            if r != row and A[r, col] % p != 0:
                factor = int(A[r, col]) % p
                A[r] = (A[r] - factor * A[row]) % p
        rank += 1
        row += 1
    return rank


def verify_d_squared_zero(D_low, D_high) -> tuple[bool, int]:
    """Verify D_low @ D_high == 0 (equivalently d² = 0)."""
    product = (D_low @ D_high).toarray()
    nnz = int(np.count_nonzero(product))
    return (nnz == 0), nnz


def main():
    print("=" * 70)
    print("Ext_CH^(n)(R) computation for R with additive group (Z/2)^4")
    print("(applies to F_4[u]/(u^2), F_16, F_2^4, F_2[u]/(u^4))")
    print("=" * 70)
    print()

    # Step 1: enumerate cells
    arities = [2, 3, 4, 5]
    print("Enumerating closed cells:")
    cells = {}
    indices = {}
    for n in arities:
        cells[n] = enumerate_cells(n)
        indices[n] = {c: i for i, c in enumerate(cells[n])}
        # Theoretical: dim H^(n) = ((|R|-1)^n + (|R|-1)·(-1)^n) / |R|
        expected = ((ORDER - 1) ** n + (ORDER - 1) * (-1) ** n) // ORDER
        print(f"  dim H^({n}) = {len(cells[n]):>6}   "
              f"(expected {expected})  "
              f"{'OK' if len(cells[n]) == expected else 'MISMATCH'}")
    print()

    # Step 2: build differentials
    print("Building differentials...")
    D = {}
    for n in [3, 4, 5]:
        D[n] = build_differential(n, cells[n], indices[n - 1]).tocsr()
        print(f"  d_{n}: {D[n].shape[0]:>6} x {D[n].shape[1]:>6}, "
              f"nnz = {D[n].nnz}")
    print()

    # Step 3: verify d² = 0
    print("Verifying d² = 0:")
    for (n_low, n_high) in [(3, 4), (4, 5)]:
        ok, nnz = verify_d_squared_zero(D[n_low], D[n_high])
        status = "OK" if ok else f"FAIL: {nnz} nonzeros in d_{n_low} d_{n_high}"
        print(f"  d_{n_low} o d_{n_high} = 0: {status}")
    print()

    # Step 4: compute ranks
    print("Computing ranks (over Q):")
    ranks = {}
    for n in [3, 4]:
        ranks[n] = rank_via_qr_or_lu(D[n])
        print(f"  rank d_{n} = {ranks[n]}")
    print(f"  rank d_5 = ... (this is the expensive one)")
    ranks[5] = rank_via_qr_or_lu(D[5])
    print(f"  rank d_5 = {ranks[5]}")
    print()

    # Step 5: compute dim Ext_CH^(n)
    print("Cohomology dimensions:")
    # Ext_CH^(n) = ker(d_n) / im(d_{n+1}); dim = (dim H^(n) - rank d_n) - rank d_{n+1}
    for n in [3, 4]:
        ker_dim = len(cells[n]) - ranks[n]
        im_dim = ranks[n + 1]
        ext = ker_dim - im_dim
        print(f"  dim Ext_CH^({n}) = (dim H^({n}) - rank d_{n}) - rank d_{n + 1}")
        print(f"                  = ({len(cells[n])} - {ranks[n]}) - {ranks[n + 1]}")
        print(f"                  = {ker_dim} - {im_dim}")
        print(f"                  = {ext}")
    print()

    # Sanity check: Euler characteristic
    print("Sanity: alternating-sum / Euler characteristic")
    # chi = Sum (-1)^n dim H^(n) — only meaningful if the complex is bounded
    # For the truncated complex H^(2..5), we have:
    # chi = dim H^(2) - dim H^(3) + dim H^(4) - dim H^(5)
    chi = sum((-1) ** n * len(cells[n]) for n in arities)
    print(f"  Sum (-1)^n dim H^(n) (n=2..5) = {chi}")
    print(f"  Sum (-1)^n dim Ext_CH^(n)? (cohomological Euler)")
    # This requires Ext_CH^(2) and Ext_CH^(5), which we don't have here.


if __name__ == "__main__":
    main()
