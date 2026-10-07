"""Arity-4 audit for F_4[u]/(u^2).

This script tests the arity-4 pre-registration proposed in the third epistle.
It deliberately reports both conventions that might explain the proposed
``2730`` count:

* all nontrivial closed ordered 4-tuples;
* all-distinct nontrivial closed ordered 4-tuples.

The stated hyper-adjacency convention only requires all labels to be
nontrivial, so the first count is the operative one.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations
from pathlib import Path

from compute_f4_u2_ext_ch import (
    NONTRIVIAL,
    add_label,
    conductor,
    f4_mul,
    f4_square,
    normalizer_actions,
)


Label = tuple[int, int]
Cell4 = tuple[Label, Label, Label, Label]
ZERO: Label = (0, 0)

S4 = list(permutations(range(4)))
C4 = [(0, 1, 2, 3), (1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)]
IDENTITY = [(0, 1, 2, 3)]
ACTIONS = normalizer_actions()


def add_many(labels: tuple[Label, ...]) -> Label:
    out = ZERO
    for label in labels:
        out = add_label(out, label)
    return out


def h4_cells(distinct: bool = False) -> list[Cell4]:
    cells: list[Cell4] = []
    for first in NONTRIVIAL:
        for second in NONTRIVIAL:
            for third in NONTRIVIAL:
                fourth = add_many((first, second, third))
                if fourth == ZERO:
                    continue
                cell = (first, second, third, fourth)
                if distinct and len(set(cell)) < 4:
                    continue
                cells.append(cell)
    return cells


def conductor_letter(label: Label) -> str:
    return "T" if conductor(label) == "u" else "W"


def conductor_word(cell: Cell4) -> str:
    return "".join(conductor_letter(label) for label in cell)


def conductor_family(cell: Cell4) -> str:
    return "".join(sorted(conductor_word(cell)))


def transform_cell(cell: Cell4, action: dict[Label, Label], permutation: tuple[int, ...]) -> Cell4:
    acted = tuple(action[label] for label in cell)
    return tuple(acted[index] for index in permutation)


def orbit_sizes(cells: list[Cell4], permutations_to_use: list[tuple[int, ...]]) -> list[int]:
    remaining = set(cells)
    sizes: list[int] = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {
            transform_cell(seed, action, permutation)
            for action in ACTIONS
            for permutation in permutations_to_use
        }
        sizes.append(len(orbit))
        remaining -= orbit
    return sorted(sizes)


def orbit_family_sizes(
    cells: list[Cell4],
    permutations_to_use: list[tuple[int, ...]],
) -> dict[str, list[int]]:
    remaining = set(cells)
    by_family: dict[str, list[int]] = {}
    while remaining:
        seed = next(iter(remaining))
        orbit = {
            transform_cell(seed, action, permutation)
            for action in ACTIONS
            for permutation in permutations_to_use
        }
        family = conductor_family(seed)
        by_family.setdefault(family, []).append(len(orbit))
        remaining -= orbit
    return {family: sorted(sizes) for family, sizes in by_family.items()}


def f4_control() -> dict[str, object]:
    labels = [0, 1, 2, 3]
    nonzero = [1, 2, 3]
    cells = []
    for first in nonzero:
        for second in nonzero:
            for third in nonzero:
                fourth = first ^ second ^ third
                if fourth:
                    cells.append((first, second, third, fourth))

    actions = []
    seen = set()
    for unit in nonzero:
        for use_frobenius in [False, True]:
            action = {}
            for label in labels:
                image = f4_mul(unit, label)
                if use_frobenius:
                    image = f4_square(image)
                action[label] = image
            signature = tuple(action[label] for label in labels)
            if signature not in seen:
                seen.add(signature)
                actions.append(action)

    remaining = set(cells)
    sizes = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {
            tuple(action[seed[index]] for index in permutation)
            for action in actions
            for permutation in S4
        }
        sizes.append(len(orbit))
        remaining -= orbit

    return {"cells": len(cells), "actions": len(actions), "orbit_sizes": sorted(sizes)}


def f2u2_control() -> dict[str, object]:
    labels = [(a, b) for a in [0, 1] for b in [0, 1]]
    nonzero = [label for label in labels if label != ZERO]

    def add2(x: Label, y: Label) -> Label:
        return (x[0] ^ y[0], x[1] ^ y[1])

    def mul_unit(unit: Label, x: Label) -> Label:
        return (unit[0] & x[0], (unit[0] & x[1]) ^ (unit[1] & x[0]))

    cells = []
    for first in nonzero:
        for second in nonzero:
            for third in nonzero:
                fourth = add2(add2(first, second), third)
                if fourth != ZERO:
                    cells.append((first, second, third, fourth))

    actions = [{label: mul_unit(unit, label) for label in labels} for unit in [(1, 0), (1, 1)]]
    remaining = set(cells)
    sizes = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {
            tuple(action[seed[index]] for index in permutation)
            for action in actions
            for permutation in S4
        }
        sizes.append(len(orbit))
        remaining -= orbit

    type_counts = Counter(
        "".join("T" if label[0] == 0 else "W" for label in cell)
        for cell in cells
    )
    return {
        "cells": len(cells),
        "actions": len(actions),
        "orbit_sizes": sorted(sizes),
        "type_counts": type_counts,
    }


def report() -> str:
    cells = h4_cells(distinct=False)
    distinct_cells = h4_cells(distinct=True)
    word_counts = Counter(conductor_word(cell) for cell in cells)
    family_counts = Counter(conductor_family(cell) for cell in cells)
    gamma_sizes = orbit_sizes(cells, IDENTITY)
    cyclic_sizes = orbit_sizes(cells, C4)
    symmetric_sizes = orbit_sizes(cells, S4)
    cyclic_family_sizes = orbit_family_sizes(cells, C4)
    symmetric_family_sizes = orbit_family_sizes(cells, S4)
    f4 = f4_control()
    f2u2 = f2u2_control()

    lines = [
        "# Arity-4 Audit for F4[u]/(u^2)",
        "",
        "This checks the third epistle's arity-4 preregistration before the",
        "curvature-lift computation is attempted.",
        "",
        "## Count Convention",
        "",
        f"- all nontrivial closed ordered 4-tuples: {len(cells)}",
        f"- all-distinct nontrivial closed ordered 4-tuples: {len(distinct_cells)}",
        "- proposed count in epistle: 2730",
        "",
        "The stated hyper-adjacency convention only excludes the trivial label, so",
        "the operative count is 3165.  The number 2730 is the count of ordered",
        "distinct choices for the first three legs before imposing that the fourth",
        "leg is nonzero; after imposing closure and nontriviality, the distinct",
        "count is 2520.",
        "",
        "## Conductor Stratification",
        "",
        "Ordered words:",
        "",
    ]

    for word in sorted(word_counts):
        lines.append(f"- {word}: {word_counts[word]}")

    lines += [
        "",
        "Unordered families:",
        "",
    ]
    for family in sorted(family_counts):
        lines.append(f"- {family}: {family_counts[family]}")

    lines += [
        "",
        "In particular, TTWW and TWWW families are nonzero.  The proposed parity",
        "claim that these vanish is false under the stated closure rule.",
        "",
        "## Orbit Counts",
        "",
        f"- Gamma_R-only orbits: {len(gamma_sizes)} with sizes {dict(Counter(gamma_sizes))}",
        f"- Gamma_R x C_4 orbits: {len(cyclic_sizes)} with sizes {dict(Counter(cyclic_sizes))}",
        f"- Gamma_R x S_4 orbits: {len(symmetric_sizes)} with sizes {dict(Counter(symmetric_sizes))}",
        "",
        "By family under Gamma_R x C_4:",
        "",
    ]

    for family in sorted(cyclic_family_sizes):
        sizes = cyclic_family_sizes[family]
        lines.append(f"- {family}: {len(sizes)} orbits, sizes {sizes}")

    lines += [
        "",
        "By family under Gamma_R x S_4:",
        "",
    ]

    for family in sorted(symmetric_family_sizes):
        sizes = symmetric_family_sizes[family]
        lines.append(f"- {family}: {len(sizes)} orbits, sizes {sizes}")

    lines += [
        "",
        "The cyclic and full symmetric quotients differ at arity 4: this is the",
        "first place where quotienting too aggressively can erase structure.",
        "The revised fourth-epistle family prediction is still not correct:",
        "measured S_4 family orbit counts are TTTT=2, TTWW=4, TWWW=3, WWWW=9,",
        "not TTTT=1, TTWW=3, TWWW=5, WWWW=9.",
        "",
        "## Controls",
        "",
        f"- pure tame F_4: {f4['cells']} closed arity-4 cells, normalizer actions {f4['actions']}, orbit sizes {f4['orbit_sizes']}",
        f"- pure wild F_2[u]/(u^2): {f2u2['cells']} closed arity-4 cells, unit actions {f2u2['actions']}, orbit sizes {f2u2['orbit_sizes']}, conductor words {dict(f2u2['type_counts'])}",
        "",
        "Unlike arity 3, the pure controls do not collapse to one orbit at arity 4.",
        "The fourth epistle corrected these pure-control counts, but the stronger",
        "claim that C_4-to-S_4 collapse occurs only on curvature-carrying lifts is",
        "false at the orbit-skeleton level: TTTT and WWWW families also collapse.",
        "",
        "## Status",
        "",
        "RED for both the original and revised arity-4 preregistrations as written.",
        "The selector may still be right, but the measurable orbit-family",
        "predictions need correction before the curvature-lift test can be trusted.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    text = report()
    report_path = Path(__file__).with_name("reports") / "h4_f4_u2_audit.md"
    report_path.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nWrote {report_path}")


if __name__ == "__main__":
    main()
