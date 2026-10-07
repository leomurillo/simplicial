"""Support/orbit atlas for the pure-wild row F_2[u]/(u^4).

Labels are encoded as 4-bit integers

    c0 + c1*u + c2*u^2 + c3*u^3,

with addition given by xor and multiplication reduced modulo u^4.  The
conductor convention matches the existing F_2[u]/(u^2) control: the first
nonzero coefficient determines the conductor exponent.  Thus u^3-labels have
conductor u, u^2-labels have conductor u^2, u-labels have conductor u^3, and
labels with nonzero constant coefficient have conductor u^4.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import permutations, product
from pathlib import Path
from typing import Iterable


Label = int
Cell = tuple[Label, ...]
Action = tuple[Label, ...]

MODULUS_DEGREE = 4
LABELS: tuple[Label, ...] = tuple(range(1 << MODULUS_DEGREE))
NONTRIVIAL: tuple[Label, ...] = tuple(label for label in LABELS if label)
ZERO: Label = 0


def add_label(x: Label, y: Label) -> Label:
    return x ^ y


def add_many(labels: Iterable[Label]) -> Label:
    out = ZERO
    for label in labels:
        out ^= label
    return out


def mul_label(x: Label, y: Label) -> Label:
    out = 0
    for i in range(MODULUS_DEGREE):
        if not (x & (1 << i)):
            continue
        for j in range(MODULUS_DEGREE - i):
            if y & (1 << j):
                out ^= 1 << (i + j)
    return out


def pow_label(x: Label, exponent: int) -> Label:
    out = 1
    for _ in range(exponent):
        out = mul_label(out, x)
    return out


def substitute_u(label: Label, image_u: Label) -> Label:
    out = 0
    for degree in range(MODULUS_DEGREE):
        if label & (1 << degree):
            out ^= pow_label(image_u, degree)
    return out


def label_coefficients(label: Label) -> list[int]:
    return [(label >> degree) & 1 for degree in range(MODULUS_DEGREE)]


def label_name(label: Label) -> str:
    if label == ZERO:
        return "0"
    parts = []
    for degree, coefficient in enumerate(label_coefficients(label)):
        if not coefficient:
            continue
        if degree == 0:
            parts.append("1")
        elif degree == 1:
            parts.append("u")
        else:
            parts.append(f"u^{degree}")
    return "+".join(parts)


def conductor_exponent(label: Label) -> int:
    if label == ZERO:
        return 0
    for degree in range(MODULUS_DEGREE):
        if label & (1 << degree):
            return MODULUS_DEGREE - degree
    raise AssertionError("unreachable")


def conductor_name(label: Label) -> str:
    exponent = conductor_exponent(label)
    if exponent == 0:
        return "1"
    if exponent == 1:
        return "u"
    return f"u^{exponent}"


def conductor_word(cell: Cell) -> str:
    return "".join(str(conductor_exponent(label)) for label in cell)


def conductor_family(cell: Cell) -> str:
    return "".join(sorted(conductor_word(cell)))


def closed_cells(arity: int) -> list[Cell]:
    cells: list[Cell] = []
    for prefix in product(NONTRIVIAL, repeat=arity - 1):
        final = add_many(prefix)
        if final != ZERO:
            cells.append((*prefix, final))
    return cells


def direct_closed_count(arity: int) -> int:
    return sum(
        1
        for cell in product(NONTRIVIAL, repeat=arity)
        if add_many(cell) == ZERO
    )


def units() -> list[Label]:
    return [label for label in LABELS if label & 1]


def unit_action(unit: Label) -> Action:
    return tuple(mul_label(unit, label) for label in LABELS)


def automorphism_specs() -> list[dict[str, Label]]:
    # Every F_2-algebra automorphism of F_2[u]/(u^4) of this restricted form:
    # u |-> u + a*u^2 + b*u^3.
    return [{"a": a, "b": b, "image_u": 0b0010 ^ (a << 2) ^ (b << 3)} for a in [0, 1] for b in [0, 1]]


def automorphism_action(spec: dict[str, Label]) -> Action:
    return tuple(substitute_u(label, spec["image_u"]) for label in LABELS)


def compose_actions(first: Action, second: Action) -> Action:
    return tuple(second[first[label]] for label in LABELS)


def unique_actions(actions: Iterable[Action]) -> list[Action]:
    seen: set[Action] = set()
    out: list[Action] = []
    for action in actions:
        if action in seen:
            continue
        seen.add(action)
        out.append(action)
    return out


def transform_cell(cell: Cell, action: Action, permutation: tuple[int, ...]) -> Cell:
    acted = tuple(action[label] for label in cell)
    return tuple(acted[index] for index in permutation)


def orbit_decomposition(
    cells: list[Cell],
    actions: list[Action],
    coordinate_permutations: list[tuple[int, ...]],
) -> list[set[Cell]]:
    remaining = set(cells)
    orbits: list[set[Cell]] = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {
            transform_cell(seed, action, coordinate_permutation)
            for action in actions
            for coordinate_permutation in coordinate_permutations
        }
        orbits.append(orbit)
        remaining -= orbit
    return orbits


def counter_dict(counter: Counter[object]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter)}


def cell_str(cell: Cell) -> list[str]:
    return [label_name(label) for label in cell]


def orbit_summary(
    cells: list[Cell],
    actions: list[Action],
    coordinate_permutations: list[tuple[int, ...]],
) -> dict[str, object]:
    orbits = orbit_decomposition(cells, actions, coordinate_permutations)
    sizes = [len(orbit) for orbit in orbits]
    family_orbit_counts = Counter(conductor_family(next(iter(orbit))) for orbit in orbits)
    family_size_distributions: dict[str, Counter[int]] = {}
    for orbit in orbits:
        family = conductor_family(next(iter(orbit)))
        family_size_distributions.setdefault(family, Counter())[len(orbit)] += 1

    return {
        "orbit_count": len(orbits),
        "orbit_size_distribution": counter_dict(Counter(sizes)),
        "family_orbit_counts": counter_dict(family_orbit_counts),
        "family_orbit_size_distributions": {
            family: counter_dict(distribution)
            for family, distribution in sorted(family_size_distributions.items())
        },
    }


def arity_summary(
    arity: int,
    unit_actions: list[Action],
    unit_automorphism_actions: list[Action],
) -> dict[str, object]:
    cells = closed_cells(arity)
    direct_count = direct_closed_count(arity)
    if direct_count != len(cells):
        raise AssertionError(
            f"arity {arity}: last-leg enumeration has {len(cells)} cells, "
            f"direct enumeration has {direct_count}"
        )

    symmetric_group = list(permutations(range(arity)))
    return {
        "arity": arity,
        "closed_nontrivial_ordered_cells": len(cells),
        "direct_closed_nontrivial_ordered_cells": direct_count,
        "validated_by_direct_enumeration": True,
        "conductor_word_counts": counter_dict(Counter(conductor_word(cell) for cell in cells)),
        "conductor_family_counts": counter_dict(Counter(conductor_family(cell) for cell in cells)),
        "unit_times_symmetric": orbit_summary(cells, unit_actions, symmetric_group),
        "unit_automorphism_times_symmetric": orbit_summary(
            cells,
            unit_automorphism_actions,
            symmetric_group,
        ),
    }


def build_summary() -> dict[str, object]:
    unit_values = units()
    unit_actions = unique_actions(unit_action(unit) for unit in unit_values)
    automorphism_values = automorphism_specs()
    automorphism_actions = unique_actions(
        automorphism_action(spec) for spec in automorphism_values
    )
    unit_automorphism_actions = unique_actions(
        compose_actions(unit_action(unit), automorphism_action(spec))
        for unit in unit_values
        for spec in automorphism_values
    )

    return {
        "ring": "F_2[u]/(u^4)",
        "label_encoding": "bit i is the coefficient of u^i in c0+c1*u+c2*u^2+c3*u^3",
        "conductor_word_alphabet": {
            "1": "u",
            "2": "u^2",
            "3": "u^3",
            "4": "u^4",
        },
        "labels": {
            "total": len(LABELS),
            "nontrivial": len(NONTRIVIAL),
            "by_conductor": counter_dict(Counter(conductor_name(label) for label in NONTRIVIAL)),
        },
        "units": {
            "count": len(unit_values),
            "action_count": len(unit_actions),
            "elements": [label_name(unit) for unit in unit_values],
        },
        "automorphisms": {
            "included": True,
            "count": len(automorphism_values),
            "action_count": len(automorphism_actions),
            "maps": [
                {
                    "a": spec["a"],
                    "b": spec["b"],
                    "u_maps_to": label_name(spec["image_u"]),
                }
                for spec in automorphism_values
            ],
        },
        "unit_automorphism_actions": {
            "action_count": len(unit_automorphism_actions),
        },
        "arities": {
            str(arity): arity_summary(
                arity,
                unit_actions,
                unit_automorphism_actions,
            )
            for arity in [3, 4]
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="also write empirical/reports/f2_u4_atlas.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary = build_summary()
    text = json.dumps(summary, sort_keys=True, separators=(",", ":"))
    print(text)
    if args.write_report:
        report_path = Path(__file__).with_name("reports") / "f2_u4_atlas.json"
        report_path.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
