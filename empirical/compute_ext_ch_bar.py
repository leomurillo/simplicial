"""Resolved chain complex of Paper 11 §9.5: bar / Hochschild differential.

Differential:
  partial(a_1,...,a_n) = sum_{i=1}^{n-1} (-1)^{i-1} (a_1,...,a_i+a_{i+1},...,a_n)
where the merged element replaces position i (deleting position i+1).

This is the standard reduced bar complex of the augmentation ideal of Z[hat R],
intersected with the subcomplex of closed cells (sum of labels = 0). Both the
closure constraint and the bar relations are preserved, so partial^2 = 0 by the
classical bar-complex theorem.

Computes Ext_CH^(n) := H^n(H_R^(.), partial) for R with additive group (Z/2)^4
(applies to F_4[u]/(u^2), F_16, F_2^4, F_2[u]/(u^4)).
"""

from __future__ import annotations

import numpy as np
from itertools import product

ORDER = 16  # |R| for additive group (Z/2)^4


def add(x, y):
    return x ^ y


def enumerate_closed_cells(arity):
    if arity < 1:
        return []
    nonzero = list(range(1, ORDER))
    if arity == 1:
        # Closed 1-cells require a_1 = 0, but a_1 != 0; so empty.
        return []
    cells = []
    for prefix in product(nonzero, repeat=arity - 1):
        s = 0
        for x in prefix:
            s = add(s, x)
        if s != 0:
            cells.append((*prefix, s))
    return cells


def bar_differential(arity, cells_n, index_nm1):
    """Bar differential: adjacent-merge only, sign (-1)^(i-1) for 1-indexed i.
    Output is a Q-rank dense matrix (sparse storage if needed)."""
    nrows = len(index_nm1)
    ncols = len(cells_n)
    # Use dense int64; for n=5 we have nrows=3165, ncols=47460, ~150M entries
    # but int64 is 1.2 GB. Use int8 since entries are in {-1, 0, 1}.
    # Actually each column has at most n-1 nonzero entries.
    M = np.zeros((nrows, ncols), dtype=np.int64)
    for col, cell in enumerate(cells_n):
        for i in range(arity - 1):  # 0-indexed: i = 0..n-2 corresponds to 1-indexed 1..n-1
            merged = cell[i] ^ cell[i + 1]
            if merged == 0:
                continue
            out_cell = (
                tuple(cell[k] for k in range(i))
                + (merged,)
                + tuple(cell[k] for k in range(i + 2, arity))
            )
            sign = -1 if (i % 2 == 1) else 1  # (-1)^(i-1) with 1-indexed i = (-1)^i' with 0-indexed i'... wait
            # 1-indexed i runs 1..n-1, sign (-1)^(i-1). 0-indexed i' = i-1 runs 0..n-2, sign (-1)^i'.
            # So sign = +1 when i' even, -1 when i' odd.
            row = index_nm1[out_cell]
            M[row, col] += sign
    return M


def main():
    print("=" * 70)
    print("Resolved chain complex (bar differential)")
    print("R additive = (Z/2)^4 (applies to F_4[u]/(u^2), F_16, F_2^4, ...)")
    print("=" * 70)

    arities = [2, 3, 4, 5]
    cells = {}
    indices = {}
    for n in arities:
        cells[n] = enumerate_closed_cells(n)
        indices[n] = {c: i for i, c in enumerate(cells[n])}
        print(f"  dim H^({n}) = {len(cells[n])}")
    print()

    print("Building bar differentials...")
    D = {}
    for n in [3, 4, 5]:
        D[n] = bar_differential(n, cells[n], indices[n - 1])
        nnz = int((D[n] != 0).sum())
        print(f"  d_{n}: {D[n].shape[0]:>6} x {D[n].shape[1]:>6}, nnz = {nnz}")
    print()

    print("Verifying d^2 = 0 over Q:")
    for (low, high) in [(3, 4), (4, 5)]:
        prod = D[low] @ D[high]
        nnz = int((prod != 0).sum())
        status = "OK (d^2 = 0)" if nnz == 0 else f"FAIL: {nnz} nonzero entries in d_{low} d_{high}"
        print(f"  d_{low} . d_{high} : {status}")
    print()

    print("Computing Q-ranks via numpy.linalg.matrix_rank...")
    ranks = {}
    for n in [3, 4]:
        ranks[n] = int(np.linalg.matrix_rank(D[n].astype(np.float64)))
        print(f"  rank d_{n} = {ranks[n]}")
    # d_5 is 3165 x 47460, may be large. Try.
    print(f"  rank d_5 (this matrix is {D[5].shape[0]} x {D[5].shape[1]} = {D[5].shape[0]*D[5].shape[1]} entries)...")
    ranks[5] = int(np.linalg.matrix_rank(D[5].astype(np.float64)))
    print(f"  rank d_5 = {ranks[5]}")
    print()

    print("Cohomology dimensions Ext_CH^(n)(R) := H^n(H_R^(.), d_bar):")
    # Ext^(2) = ker(d_2) / im(d_3) = H^(2) / im(d_3)
    ext2 = len(cells[2]) - ranks[3]
    print(f"  dim Ext_CH^(2) = dim H^(2) - rank d_3 = {len(cells[2])} - {ranks[3]} = {ext2}")
    # Ext^(3) = ker(d_3) / im(d_4) = (dim H^(3) - rank d_3) - rank d_4
    ext3 = len(cells[3]) - ranks[3] - ranks[4]
    print(f"  dim Ext_CH^(3) = (dim H^(3) - rank d_3) - rank d_4 = ({len(cells[3])} - {ranks[3]}) - {ranks[4]} = {ext3}")
    # Ext^(4) = ker(d_4) / im(d_5)
    ext4 = len(cells[4]) - ranks[4] - ranks[5]
    print(f"  dim Ext_CH^(4) = (dim H^(4) - rank d_4) - rank d_5 = ({len(cells[4])} - {ranks[4]}) - {ranks[5]} = {ext4}")


if __name__ == "__main__":
    main()
