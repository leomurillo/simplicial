"""Smoke test for the hyper-adjacency operadic composition law (Paper 11, Theorem 9.5).

This script verifies, on the F_4[u]/(u^2) row:

  1. Partial composition f circ_i g is well-defined (closure preserved, all legs nonzero).
  2. Associativity: (f circ_i g) circ_j h == f circ_i (g circ_{j-i} h) when j falls in
     the inserted g-range.
  3. Hayes-Frobenius equivariance: gamma . (f circ_i g) == (gamma . f) circ_i (gamma . g).
  4. Binary identities: f circ_i (a, -a) == f when (a, -a) is the unit at f's i-th label.

The convention is: each closed cell is rooted at its *last* leg, which serves as the
operadic output.  The remaining n-1 legs are inputs, indexed 0, ..., n-2.

Composition matching at slot i requires
    f[i] + g[n-1] == 0   (in additive notation),
in which case
    (f circ_i g) = (f[0], ..., f[i-1], g[0], ..., g[n-2], f[i+1], ..., f[m-1]).

Run from the empirical/ directory:

    python operadic_composition_check.py

Exit status 0 on success; nonzero on any failure.
"""

from __future__ import annotations

import itertools
import sys
from typing import Iterable

from local_adjacency_constructor import (
    FiniteLocalRing,
    LocalAdjacencyConstructor,
    make_f4_u2_ring,
)


Label = tuple[int, int]
Cell = tuple[Label, ...]


def compose(ring: FiniteLocalRing, f: Cell, g: Cell, i: int) -> Cell | None:
    """Return f circ_i g if the matching condition holds; otherwise None.

    Both f and g are closed cells rooted at their last leg.  Slot i runs
    over the n-1 input legs of f, i.e., i in {0, ..., len(f) - 2}.
    """

    m = len(f)
    n = len(g)
    if not (0 <= i < m - 1):
        raise IndexError(f"slot {i} out of input range for arity-{m} cell")

    # matching: f[i] + g[n-1] == 0
    if ring.add(f[i], g[n - 1]) != ring.zero:
        return None

    # build composite: replace f[i] with g[0..n-2]
    composite: list[Label] = list(f[:i]) + list(g[: n - 1]) + list(f[i + 1 :])
    return tuple(composite)


def check_closed(ring: FiniteLocalRing, cell: Cell) -> bool:
    if any(label == ring.zero for label in cell):
        return False
    return ring.add_many(cell) == ring.zero


def gather_cells(ctor: LocalAdjacencyConstructor, arity: int) -> tuple[Cell, ...]:
    return ctor.closed_cells(arity)


def apply_normalizer(ring: FiniteLocalRing, action, cell: Cell) -> Cell:
    return tuple(ring.apply(action, label) for label in cell)


# ---------------------------------------------------------------------------
# checks


def check_composition_well_defined(
    ring: FiniteLocalRing, cells_m: Iterable[Cell], cells_n: Iterable[Cell]
) -> dict[str, int]:
    """Verify that every successful composition produces a valid closed cell."""

    cells_m = tuple(cells_m)
    cells_n = tuple(cells_n)
    candidates = 0
    matched = 0
    failures = 0

    for f in cells_m:
        for g in cells_n:
            for i in range(len(f) - 1):
                candidates += 1
                composite = compose(ring, f, g, i)
                if composite is None:
                    continue
                matched += 1
                if not check_closed(ring, composite):
                    failures += 1
                if len(composite) != len(f) + len(g) - 2:
                    failures += 1

    return {
        "candidates": candidates,
        "matched": matched,
        "failures": failures,
    }


def check_associativity(
    ring: FiniteLocalRing,
    cells_m: Iterable[Cell],
    cells_n: Iterable[Cell],
    cells_p: Iterable[Cell],
    sample_cap: int | None = None,
) -> dict[str, int]:
    """Test the inserted-range associativity case.

    For each (f, g, h) and each i, j with j in the inserted g-range:
      (f circ_i g) circ_j h  ==  f circ_i (g circ_{j-i} h).
    """

    cells_m = tuple(cells_m)
    cells_n = tuple(cells_n)
    cells_p = tuple(cells_p)
    tested = 0
    matched = 0
    failures = 0

    triples = itertools.product(cells_m, cells_n, cells_p)
    if sample_cap is not None:
        triples = itertools.islice(triples, sample_cap)

    for f, g, h in triples:
        m = len(f)
        n = len(g)
        for i in range(m - 1):
            fg = compose(ring, f, g, i)
            if fg is None:
                continue
            # j in g's inserted range is positions i, i+1, ..., i+n-2 in fg
            for j_prime in range(n - 1):
                j = i + j_prime
                tested += 1
                # left: (f circ_i g) circ_j h
                left = compose(ring, fg, h, j)
                # right: f circ_i (g circ_{j_prime} h)
                gh = compose(ring, g, h, j_prime)
                right = compose(ring, f, gh, i) if gh is not None else None
                if left is None and right is None:
                    continue
                matched += 1
                if left != right:
                    failures += 1

    return {
        "tested": tested,
        "both_defined": matched,
        "failures": failures,
    }


def check_equivariance(
    ring: FiniteLocalRing,
    cells_m: Iterable[Cell],
    cells_n: Iterable[Cell],
    actions,
    sample_cap: int | None = None,
) -> dict[str, int]:
    """Verify gamma . (f circ_i g) == (gamma . f) circ_i (gamma . g)."""

    cells_m = tuple(cells_m)
    cells_n = tuple(cells_n)
    tested = 0
    failures = 0

    pairs = list(itertools.product(cells_m, cells_n))
    if sample_cap is not None:
        pairs = pairs[:sample_cap]

    for f, g in pairs:
        for i in range(len(f) - 1):
            composite = compose(ring, f, g, i)
            if composite is None:
                continue
            for action in actions:
                tested += 1
                acted_composite = apply_normalizer(ring, action, composite)
                acted_f = apply_normalizer(ring, action, f)
                acted_g = apply_normalizer(ring, action, g)
                composed_acted = compose(ring, acted_f, acted_g, i)
                if composed_acted != acted_composite:
                    failures += 1

    return {"tested": tested, "failures": failures}


def check_binary_identity(
    ring: FiniteLocalRing, cells_m: Iterable[Cell]
) -> dict[str, int]:
    """Verify that the unit cell (a, -a) is a right identity for slot i with label a."""

    tested = 0
    failures = 0

    for f in cells_m:
        for i in range(len(f) - 1):
            a = f[i]
            neg_a = next(
                (label for label in ring.labels if ring.add(a, label) == ring.zero),
                None,
            )
            if neg_a is None or neg_a == ring.zero:
                continue
            unit = (a, neg_a)
            # matching: f[i] + unit[-1] = f[i] + neg_a = 0  -- ok
            composite = compose(ring, f, unit, i)
            tested += 1
            if composite != f:
                failures += 1

    return {"tested": tested, "failures": failures}


# ---------------------------------------------------------------------------
# main


def main() -> int:
    ring = make_f4_u2_ring()
    ctor = LocalAdjacencyConstructor(ring)

    cells_2 = gather_cells(ctor, 2)
    cells_3 = gather_cells(ctor, 3)

    print(f"ring: {ring.name}")
    print(f"|cells_2| = {len(cells_2)}")
    print(f"|cells_3| = {len(cells_3)}")
    print()

    failures_total = 0

    # 1. composition well-defined
    print("[1] composition well-defined ...")
    stats = check_composition_well_defined(ring, cells_3, cells_3)
    print(f"    candidates={stats['candidates']}  matched={stats['matched']}  failures={stats['failures']}")
    failures_total += stats["failures"]

    # 2. associativity (sample-capped to keep runtime moderate)
    print("[2] associativity (inserted-range case, sample-capped) ...")
    stats = check_associativity(ring, cells_3, cells_3, cells_3, sample_cap=20000)
    print(f"    tested={stats['tested']}  both_defined={stats['both_defined']}  failures={stats['failures']}")
    failures_total += stats["failures"]

    # 3. Hayes-Frobenius equivariance (sample-capped)
    print("[3] Hayes-Frobenius equivariance ...")
    stats = check_equivariance(ring, cells_3, cells_3, ring.normalizer_actions, sample_cap=200)
    print(f"    tested={stats['tested']}  failures={stats['failures']}")
    failures_total += stats["failures"]

    # 4. binary identities
    print("[4] binary identity at each slot ...")
    stats = check_binary_identity(ring, cells_3)
    print(f"    tested={stats['tested']}  failures={stats['failures']}")
    failures_total += stats["failures"]

    print()
    if failures_total == 0:
        print("PASS  (operadic composition law verified on F_4[u]/(u^2) arity-3 floor)")
        return 0
    else:
        print(f"FAIL  total failures = {failures_total}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
