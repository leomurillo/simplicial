"""Full audit: check d^2 = 0 over F_2 on every arity-4 cell in (Z/2)^4."""

from __future__ import annotations
from itertools import product


def add(x, y):
    return x ^ y


def enumerate_cells(arity, order):
    if arity < 2:
        return []
    nonzero = list(range(1, order))
    cells = []
    for prefix in product(nonzero, repeat=arity - 1):
        s = 0
        for x in prefix:
            s = add(s, x)
        if s != 0:
            cells.append((*prefix, s))
    return cells


def diff_paper(cell):
    """Paper literal: merged at end, sign (-1)^(i+j)."""
    n = len(cell)
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            merged = add(cell[i], cell[j])
            if merged == 0:
                continue
            rest = tuple(cell[k] for k in range(n) if k != i and k != j)
            out_cell = rest + (merged,)
            sign = -1 if (i + j) % 2 else 1
            out.append((sign, out_cell))
    return out


def apply_d(coefs):
    result: dict = {}
    for cell, coef in coefs.items():
        for sign, out_cell in diff_paper(cell):
            result[out_cell] = result.get(out_cell, 0) + sign * coef
    return {c: v for c, v in result.items() if v != 0}


def main():
    order = 16  # (Z/2)^4
    cells_4 = enumerate_cells(4, order)
    print(f"Auditing d^2 = 0 over Q and F_2 on all {len(cells_4)} arity-4 cells of (Z/2)^4")

    fail_Q = 0
    fail_F2 = 0
    cells_with_zero_d4 = 0
    sample_failures = []

    for c in cells_4:
        d1 = apply_d({c: 1})
        if not d1:
            cells_with_zero_d4 += 1
            continue
        d2 = apply_d(d1)
        d2_F2 = {k: v % 2 for k, v in d2.items() if v % 2 != 0}
        if d2:
            fail_Q += 1
        if d2_F2:
            fail_F2 += 1
            if len(sample_failures) < 3:
                sample_failures.append((c, d2_F2))

    print(f"  Cells with d_4 = 0 (trivially d^2=0): {cells_with_zero_d4}")
    print(f"  Cells with d^2 != 0 over Q:           {fail_Q}/{len(cells_4)}")
    print(f"  Cells with d^2 != 0 over F_2:         {fail_F2}/{len(cells_4)}")
    print()
    print(f"  Sample F_2 failures:")
    for c, d2 in sample_failures:
        print(f"    cell {c}:")
        print(f"      d_3 d_4(c) mod 2 = {d2}")


if __name__ == "__main__":
    main()
