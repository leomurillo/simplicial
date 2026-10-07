"""Enumerate the pure tame F_16 field row for Paper 11.

Field model:

    F_16 = F_2[a] / (a^4 + a + 1).

Elements are encoded as four-bit integers whose bits are coefficients of
1, a, a^2, a^3.  The quotient-size-16 tame actions are the semilinear maps

    x |-> u * x^(2^k),  u in F_16^*,  k = 0,1,2,3,

and orbit quotients use this Gamma action together with all leg permutations.

The cells enumerated here are ordered nontrivial closed n-tuples:

    (x_1, ..., x_n), x_i != 0, sum_i x_i = 0.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import permutations, product
from pathlib import Path
from typing import Iterable


MODULUS = 0b10011  # a^4 + a + 1
DEGREE = 4
FIELD_SIZE = 16
ZERO = 0
NONZERO = tuple(range(1, FIELD_SIZE))


Cell = tuple[int, ...]
Action = tuple[int, ...]


def gf_add(x: int, y: int) -> int:
    return x ^ y


def gf_mul(x: int, y: int, modulus: int = MODULUS, degree: int = DEGREE) -> int:
    product_bits = 0
    left = x
    right = y
    while right:
        if right & 1:
            product_bits ^= left
        right >>= 1
        left <<= 1

    for product_degree in range(2 * degree - 2, degree - 1, -1):
        if product_bits & (1 << product_degree):
            product_bits ^= modulus << (product_degree - degree)
    return product_bits & ((1 << degree) - 1)


def gf_pow(
    x: int,
    exponent: int,
    modulus: int = MODULUS,
    degree: int = DEGREE,
) -> int:
    result = 1
    base = x
    while exponent:
        if exponent & 1:
            result = gf_mul(result, base, modulus=modulus, degree=degree)
        base = gf_mul(base, base, modulus=modulus, degree=degree)
        exponent >>= 1
    return result


def gf_square(x: int, modulus: int = MODULUS, degree: int = DEGREE) -> int:
    return gf_mul(x, x, modulus=modulus, degree=degree)


def gf_frobenius(
    x: int,
    power: int,
    modulus: int = MODULUS,
    degree: int = DEGREE,
) -> int:
    out = x
    for _ in range(power % degree):
        out = gf_square(out, modulus=modulus, degree=degree)
    return out


def gf_sum(values: Iterable[int]) -> int:
    out = ZERO
    for value in values:
        out ^= value
    return out


def element_name(x: int, symbol: str = "a") -> str:
    if x == 0:
        return "0"

    parts: list[str] = []
    if x & 1:
        parts.append("1")
    if x & 2:
        parts.append(symbol)
    if x & 4:
        parts.append(f"{symbol}^2")
    if x & 8:
        parts.append(f"{symbol}^3")
    return "+".join(parts)


def cell_names(cell: Cell, symbol: str = "a") -> list[str]:
    return [element_name(value, symbol=symbol) for value in cell]


def semilinear_actions(
    field_size: int,
    modulus: int = MODULUS,
    degree: int = DEGREE,
) -> list[Action]:
    nonzero = range(1, field_size)
    actions: list[Action] = []
    seen: set[Action] = set()

    for unit in nonzero:
        for frob_power in range(degree):
            images = [0] * field_size
            for value in range(field_size):
                image = gf_mul(
                    unit,
                    gf_frobenius(value, frob_power, modulus=modulus, degree=degree),
                    modulus=modulus,
                    degree=degree,
                )
                images[value] = image
            action = tuple(images)
            if action not in seen:
                seen.add(action)
                actions.append(action)

    return actions


def closed_cells(arity: int, field_size: int = FIELD_SIZE) -> list[Cell]:
    nonzero = tuple(range(1, field_size))
    cells: list[Cell] = []

    for prefix in product(nonzero, repeat=arity - 1):
        last = gf_sum(prefix)
        if last != ZERO:
            cells.append(tuple(prefix) + (last,))

    return cells


def transform_cell(cell: Cell, action: Action, permutation: tuple[int, ...]) -> Cell:
    acted = tuple(action[value] for value in cell)
    return tuple(acted[index] for index in permutation)


def orbit_decomposition(
    cells: list[Cell],
    actions: list[Action],
    permutations_to_use: list[tuple[int, ...]],
) -> list[set[Cell]]:
    remaining = set(cells)
    orbits: list[set[Cell]] = []

    while remaining:
        seed = next(iter(remaining))
        orbit = {
            transform_cell(seed, action, permutation)
            for action in actions
            for permutation in permutations_to_use
        }
        orbits.append(orbit)
        remaining -= orbit

    return orbits


def canonical_cell(cells: Iterable[Cell], symbol: str = "a") -> Cell:
    return min(cells, key=lambda cell: (cell_names(cell, symbol=symbol), cell))


def multiplicity_partition(cell: Cell) -> str:
    counts = sorted(Counter(cell).values(), reverse=True)
    return "+".join(str(count) for count in counts)


def orbit_rows(
    orbits: list[set[Cell]],
    joint_group_size: int,
    symbol: str = "a",
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for orbit in orbits:
        representative = canonical_cell(orbit, symbol=symbol)
        support = tuple(sorted(set(representative), key=lambda value: element_name(value, symbol=symbol)))
        rows.append(
            {
                "representative": cell_names(representative, symbol=symbol),
                "support": [element_name(value, symbol=symbol) for value in support],
                "ordered_size": len(orbit),
                "stabilizer_size": joint_group_size // len(orbit),
                "support_size": len(set(representative)),
                "multiplicity_partition": multiplicity_partition(representative),
            }
        )

    return sorted(
        rows,
        key=lambda row: (
            int(row["support_size"]),
            str(row["multiplicity_partition"]),
            int(row["ordered_size"]),
            row["representative"],
        ),
    )


def counter_to_plain(counter: Counter[object]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter, key=str)}


def arity_payload(
    arity: int,
    field_size: int = FIELD_SIZE,
    modulus: int = MODULUS,
    degree: int = DEGREE,
    symbol: str = "a",
) -> dict[str, object]:
    cells = closed_cells(arity, field_size=field_size)
    actions = semilinear_actions(field_size, modulus=modulus, degree=degree)
    perms = list(permutations(range(arity)))
    orbits = orbit_decomposition(cells, actions, perms)
    joint_group_size = len(actions) * len(perms)
    rows = orbit_rows(orbits, joint_group_size, symbol=symbol)

    support_counter = Counter(len(set(cell)) for cell in cells)
    partition_counter = Counter(multiplicity_partition(cell) for cell in cells)
    orbit_size_counter = Counter(len(orbit) for orbit in orbits)
    stabilizer_counter = Counter(joint_group_size // len(orbit) for orbit in orbits)

    payload: dict[str, object] = {
        "arity": arity,
        "ordered_cells": len(cells),
        "all_distinct_ordered_cells": sum(1 for cell in cells if len(set(cell)) == arity),
        "gamma_size": len(actions),
        "joint_group_size": joint_group_size,
        "orbit_count": len(orbits),
        "orbit_size_distribution": counter_to_plain(orbit_size_counter),
        "stabilizer_size_distribution": counter_to_plain(stabilizer_counter),
        "cell_support_size_distribution": counter_to_plain(support_counter),
        "cell_multiplicity_partition_distribution": counter_to_plain(partition_counter),
        "orbits": rows,
    }
    return payload


def f4_control_payload() -> dict[str, object]:
    return {
        "field_model": "F_4 = F_2[w]/(w^2+w+1), embedded via the same bit arithmetic",
        "arities": {
            str(arity): arity_payload(
                arity,
                field_size=4,
                modulus=0b111,
                degree=2,
                symbol="w",
            )
            for arity in (3, 4)
        },
    }


def build_payload() -> dict[str, object]:
    return {
        "field_model": "F_16 = F_2[a]/(a^4+a+1)",
        "element_encoding": "integer bits are coefficients of 1,a,a^2,a^3",
        "action_model": "Gamma = F_16^* semidirect <x -> x^2>; quotient by Gamma x S_n",
        "irreducible_polynomial_bits": bin(MODULUS),
        "arities": {
            str(arity): arity_payload(arity)
            for arity in (3, 4)
        },
        "controls": {
            "pure_tame_f4": f4_control_payload(),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Enumerate the F16 pure tame support/orbit atlas."
    )
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="Also write empirical/reports/f16_atlas.json.",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=None,
        help="Pretty-print JSON with this indentation level.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload()

    if args.write_report:
        report_path = Path(__file__).with_name("reports") / "f16_atlas.json"
        report_path.write_text(
            json.dumps(payload, sort_keys=True, separators=(",", ":")),
            encoding="utf-8",
        )

    print(json.dumps(payload, sort_keys=True, indent=args.indent, separators=(",", ":")))


if __name__ == "__main__":
    main()
