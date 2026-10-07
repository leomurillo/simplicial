"""Investigate sign/placement corrections that would make d^2 = 0 for the
Paper 11 §9.5 contraction differential.

We try several variant differentials on R = (Z/2)^2 and (Z/2)^4 and check
whether d^2 = 0 either over Q or over F_2.

Variants tried:
  A. Paper literal: merged at end, sign (-1)^(i+j), 0-indexed.
  B. Same but 1-indexed sign (-1)^(i+j) -- parity is the same as A, so no change.
  C. Merged at position min(i,j); rest preserves order modulo deletion of j.
     Sign (-1)^(i+j).
  D. Merged at position min(i,j); sign (-1)^(j-1) (a la simplicial face map).
  E. Sign (-1)^(j-i-1) (length of arc skipped).
  F. Antisymmetrize: replace each cell by its alternating sum over S_n
     (sign(sigma) (a_{sigma(1)},...,a_{sigma(n)})). Compute d on antisymmetrized
     basis vectors.
  G. Quotient by symmetric action (S_n - coinvariants): treat (a_1,...,a_n)
     as unordered multisets. Sum d_{i,j} over unordered position pairs with
     no signs (only the merged-leg multiplicity matters).
"""

from __future__ import annotations
from itertools import product, permutations
import numpy as np


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


def diff_variant(cell, variant):
    """Return list of (sign, output_cell) for given variant."""
    n = len(cell)
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            merged = add(cell[i], cell[j])
            if merged == 0:
                continue
            # Construct output cell per variant
            if variant in ("A", "B"):
                # Merged at end
                rest = tuple(cell[k] for k in range(n) if k != i and k != j)
                out_cell = rest + (merged,)
                sign = -1 if (i + j) % 2 else 1
            elif variant == "C":
                # Merged at position i (replace pos i, delete pos j)
                out_cell = tuple(
                    merged if k == i else cell[k]
                    for k in range(n) if k != j
                )
                sign = -1 if (i + j) % 2 else 1
            elif variant == "D":
                out_cell = tuple(
                    merged if k == i else cell[k]
                    for k in range(n) if k != j
                )
                sign = -1 if (j) % 2 else 1
            elif variant == "E":
                rest = tuple(cell[k] for k in range(n) if k != i and k != j)
                out_cell = rest + (merged,)
                sign = -1 if ((j - i - 1) % 2) else 1
            else:
                raise ValueError(f"Unknown variant {variant}")
            out.append((sign, out_cell))
    return out


def apply_d(coefs, variant):
    result: dict = {}
    for cell, coef in coefs.items():
        for sign, out_cell in diff_variant(cell, variant):
            result[out_cell] = result.get(out_cell, 0) + sign * coef
    return {c: v for c, v in result.items() if v != 0}


def check_d_squared(arity, order, variant, mod=None):
    """Compute d ∘ d on every arity-n cell; return set of cells with nonzero d²."""
    cells = enumerate_cells(arity, order)
    failures = []
    for c in cells:
        d1 = apply_d({c: 1}, variant)
        d2 = apply_d(d1, variant)
        if mod is not None:
            d2 = {k: v % mod for k, v in d2.items() if v % mod != 0}
        if d2:
            failures.append((c, d2))
    return failures


def main():
    print("Variant audit: which sign convention gives d^2 = 0 on the merge complex?")
    print()

    for order, name in [(4, "(Z/2)^2"), (16, "(Z/2)^4 = F_4[u]/(u^2) additive")]:
        print(f"=== Ground group: {name} (|R| = {order}) ===")
        for variant in ["A", "C", "D", "E"]:
            for arity in [3, 4]:
                cells = enumerate_cells(arity, order)
                if not cells:
                    continue
                # Check d^2 on first 5 cells over Q and F_2
                failures_Q = []
                failures_F2 = []
                sample = cells[:5]
                for c in sample:
                    d1 = apply_d({c: 1}, variant)
                    d2 = apply_d(d1, variant)
                    if d2:
                        failures_Q.append(c)
                    d2_F2 = {k: v % 2 for k, v in d2.items() if v % 2 != 0}
                    if d2_F2:
                        failures_F2.append(c)
                Q_status = "vanishes" if not failures_Q else f"FAILS ({len(failures_Q)}/5)"
                F2_status = "vanishes" if not failures_F2 else f"FAILS ({len(failures_F2)}/5)"
                print(f"  variant {variant}, arity {arity}: Q d^2: {Q_status:>20}    F_2 d^2: {F2_status}")
        print()


if __name__ == "__main__":
    main()
