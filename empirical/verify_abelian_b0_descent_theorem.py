"""Exact verifier for the finite-abelian B0 subgroup descent theorem.

B1 says that cyclic balance-transfer descent is lcm-of-conductors closure.
B2 is the finite-abelian generalization: the minimal B0 descent closure of an
active reciprocal support is the nonzero part of the subgroup it generates.

This matters because lcm/order data is insufficient in noncyclic groups.  For
example, one nonzero mode in C_2 x C_2 has order 2, but the lcm-order closure
would buy all three nonzero modes.  B2 buys only the generated line unless a
separate symmetry/normalizer policy is requested.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import sys
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Hashable


sys.path.insert(0, str(Path(__file__).resolve().parent))

from local_adjacency_constructor import make_f2_u4_ring, make_f4_u2_ring


Label = Hashable
DEFAULT_JSON = Path("empirical/reports/abelian_b0_descent_theorem.json")
DEFAULT_REPORT = Path("empirical/reports/abelian_b0_descent_theorem.md")


@dataclass(frozen=True)
class AdditiveRow:
    key: str
    name: str
    labels: tuple[Label, ...]
    zero: Label
    add: Callable[[Label, Label], Label]
    label_name: Callable[[Label], str]
    order: Callable[[Label], int]
    conductor: Callable[[Label], str] | None = None
    conductor_rank: Callable[[str], int] | None = None

    @property
    def nonzero(self) -> tuple[Label, ...]:
        return tuple(label for label in self.labels if label != self.zero)


def element_order_in_product(moduli: tuple[int, ...], label: tuple[int, ...]) -> int:
    orders = []
    for modulus, coordinate in zip(moduli, label):
        coordinate %= modulus
        if coordinate == 0:
            orders.append(1)
        else:
            orders.append(modulus // math.gcd(modulus, coordinate))
    return math.lcm(*orders)


def product_row(moduli: tuple[int, ...]) -> AdditiveRow:
    labels = tuple(itertools.product(*(range(modulus) for modulus in moduli)))
    zero = tuple(0 for _ in moduli)

    def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((a + b) % modulus for a, b, modulus in zip(left, right, moduli))

    key = "x".join(f"c{modulus}" for modulus in moduli)
    name = " x ".join(f"C_{modulus}" for modulus in moduli)
    return AdditiveRow(
        key=key,
        name=name,
        labels=labels,
        zero=zero,
        add=add,
        label_name=lambda label: "(" + ",".join(str(x) for x in label) + ")",
        order=lambda label: element_order_in_product(moduli, label),
    )


def local_row(key: str) -> AdditiveRow:
    if key == "f4-u2":
        ring = make_f4_u2_ring()
    elif key == "f2-u4":
        ring = make_f2_u4_ring()
    else:
        raise ValueError(f"unknown local row {key}")
    conductor_order = {name: index + 1 for index, name in enumerate(ring.conductor_order)}
    return AdditiveRow(
        key=key,
        name=f"{ring.name} additive",
        labels=ring.labels,
        zero=ring.zero,
        add=ring.add,
        label_name=ring.label_name,
        order=lambda label: 1 if label == ring.zero else 2,
        conductor=ring.conductor,
        conductor_rank=lambda conductor: conductor_order[conductor],
    )


def generated_subgroup(row: AdditiveRow, support: set[Label]) -> set[Label]:
    generators = [label for label in support if label != row.zero]
    if not generators:
        return set()
    closure = {row.zero}
    frontier = [row.zero]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = row.add(current, generator)
            if candidate in closure:
                continue
            closure.add(candidate)
            frontier.append(candidate)
    closure.discard(row.zero)
    return closure


def is_closed(row: AdditiveRow, support: set[Label]) -> bool:
    with_zero = set(support)
    with_zero.add(row.zero)
    for left in with_zero:
        for right in with_zero:
            if row.add(left, right) not in with_zero:
                return False
    return True


def order_lcm_closure(row: AdditiveRow, support: set[Label]) -> set[Label]:
    if not support:
        return set()
    combined_order = math.lcm(*(row.order(label) for label in support))
    return {
        label
        for label in row.nonzero
        if combined_order % row.order(label) == 0
    }


def conductor_rank_saturation(row: AdditiveRow, support: set[Label]) -> set[Label]:
    if row.conductor is None or row.conductor_rank is None or not support:
        return set()
    max_rank = max(row.conductor_rank(row.conductor(label)) for label in support)
    return {
        label
        for label in row.nonzero
        if row.conductor_rank(row.conductor(label)) <= max_rank
    }


def all_supports(row: AdditiveRow, exhaustive_max_nonzero: int, sample_count: int, seed: int) -> tuple[list[set[Label]], str]:
    nonzero = list(row.nonzero)
    if len(nonzero) <= exhaustive_max_nonzero:
        supports: list[set[Label]] = []
        for size in range(1, len(nonzero) + 1):
            for combo in itertools.combinations(nonzero, size):
                supports.append(set(combo))
        return supports, "exhaustive"

    rng = random.Random(seed)
    supports = []
    for _ in range(sample_count):
        size = rng.randint(1, min(len(nonzero), max(1, exhaustive_max_nonzero)))
        supports.append(set(rng.sample(nonzero, size)))
    return supports, "sampled"


def format_support(row: AdditiveRow, support: Iterable[Label], max_items: int = 8) -> list[str]:
    labels = sorted(support, key=row.label_name)
    names = [row.label_name(label) for label in labels[:max_items]]
    if len(labels) > max_items:
        names.append(f"...(+{len(labels) - max_items})")
    return names


def first_lcm_overbuy(row: AdditiveRow, supports: list[set[Label]]) -> dict[str, Any] | None:
    for support in supports:
        generated = generated_subgroup(row, support)
        by_order = order_lcm_closure(row, support)
        if len(by_order) > len(generated):
            return {
                "support": format_support(row, support),
                "generated_size": len(generated),
                "order_lcm_size": len(by_order),
                "generated": format_support(row, generated),
                "order_lcm_extra": format_support(row, by_order - generated),
            }
    return None


def first_conductor_overbuy(row: AdditiveRow, supports: list[set[Label]]) -> dict[str, Any] | None:
    if row.conductor is None:
        return None
    for support in supports:
        generated = generated_subgroup(row, support)
        saturated = conductor_rank_saturation(row, support)
        if len(saturated) > len(generated):
            return {
                "support": format_support(row, support),
                "generated_size": len(generated),
                "conductor_saturation_size": len(saturated),
                "generated": format_support(row, generated),
                "saturation_extra": format_support(row, saturated - generated),
            }
    return None


def verify_row(
    row: AdditiveRow,
    *,
    exhaustive_max_nonzero: int,
    sample_count: int,
    seed: int,
) -> dict[str, Any]:
    supports, mode = all_supports(row, exhaustive_max_nonzero, sample_count, seed)
    closure_sizes: list[int] = []
    order_overbuy_count = 0
    conductor_overbuy_count = 0

    for support in supports:
        closure = generated_subgroup(row, support)
        closure_sizes.append(len(closure))
        if not support <= closure:
            raise AssertionError(f"{row.key}: generated closure does not contain support")
        if not is_closed(row, closure):
            raise AssertionError(f"{row.key}: generated closure is not additively closed")
        if generated_subgroup(row, closure) != closure:
            raise AssertionError(f"{row.key}: generated closure is not idempotent")

        by_order = order_lcm_closure(row, support)
        if len(by_order) > len(closure):
            order_overbuy_count += 1
        if row.conductor is not None:
            saturated = conductor_rank_saturation(row, support)
            if len(saturated) > len(closure):
                conductor_overbuy_count += 1

    first_order_overbuy = first_lcm_overbuy(row, supports)
    first_rank_overbuy = first_conductor_overbuy(row, supports)
    nonzero_count = len(row.nonzero)
    return {
        "key": row.key,
        "row": row.name,
        "label_count": len(row.labels),
        "nonzero_count": nonzero_count,
        "verification_mode": mode,
        "support_checks": len(supports),
        "mean_generated_resource_ratio": (
            sum(size / nonzero_count for size in closure_sizes) / len(closure_sizes)
        ),
        "max_generated_size": max(closure_sizes),
        "order_lcm_overbuy_count": order_overbuy_count,
        "conductor_rank_overbuy_count": conductor_overbuy_count,
        "first_order_lcm_overbuy": first_order_overbuy,
        "first_conductor_rank_overbuy": first_rank_overbuy,
    }


def build_rows() -> list[AdditiveRow]:
    return [
        product_row((2, 2)),
        product_row((2, 4)),
        product_row((3, 3)),
        product_row((2, 6)),
        product_row((4, 4)),
        product_row((2, 2, 2)),
        product_row((3, 6)),
        local_row("f4-u2"),
        local_row("f2-u4"),
    ]


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    rows = [
        verify_row(
            row,
            exhaustive_max_nonzero=args.exhaustive_max_nonzero,
            sample_count=args.sample_count,
            seed=args.seed + index * 1000,
        )
        for index, row in enumerate(build_rows())
    ]
    return {
        "theorem": (
            "For a finite abelian character group G and nonempty reciprocal "
            "support S, the B0 balance-transfer descent closure is "
            "D_G(S)=<S>\\{0}.  It is the unique minimum-resource support with "
            "zero projection, closure, and descent-balance costs."
        ),
        "caveat": (
            "In noncyclic groups, lcm/order data is insufficient.  The subgroup "
            "generated by S is the invariant; conductor or order saturation is "
            "a stronger symmetry policy and can overbuy."
        ),
        "config": {
            "exhaustive_max_nonzero": args.exhaustive_max_nonzero,
            "sample_count": args.sample_count,
            "seed": args.seed,
        },
        "rows": rows,
    }


def write_json(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def render_overbuy(example: dict[str, Any] | None) -> str:
    if example is None:
        return "none"
    return (
        f"{', '.join(example['support'])} -> "
        f"{example['generated_size']} vs {example.get('order_lcm_size', example.get('conductor_saturation_size'))}"
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Finite Abelian B0 Subgroup Descent Theorem",
        "",
        "## Theorem",
        "",
        payload["theorem"],
        "",
        "## Caveat",
        "",
        payload["caveat"],
        "",
        "## Certified Rows",
        "",
        "| row | mode | support checks | mean resource | max closure | order-lcm overbuy | conductor overbuy | first order-lcm overbuy | first conductor overbuy |",
        "|---|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in payload["rows"]:
        lines.append(
            "| {row} | {mode} | {checks} | {mean:.6f} | {max_size} | {order_overbuy} | "
            "{conductor_overbuy} | {first_order} | {first_conductor} |".format(
                row=row["row"],
                mode=row["verification_mode"],
                checks=row["support_checks"],
                mean=row["mean_generated_resource_ratio"],
                max_size=row["max_generated_size"],
                order_overbuy=row["order_lcm_overbuy_count"],
                conductor_overbuy=row["conductor_rank_overbuy_count"],
                first_order=render_overbuy(row["first_order_lcm_overbuy"]),
                first_conductor=render_overbuy(row["first_conductor_rank_overbuy"]),
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "B1's cyclic lcm formula survives as a special case because cyclic groups",
        "have one subgroup for each divisor.  B2 replaces lcm closure by generated",
        "subgroup closure.  In product and local additive rows, order or conductor",
        "saturation can be a useful symmetry policy, but it is not the minimal B0",
        "information investment.",
    ]
    return "\n".join(lines) + "\n"


def write_report(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(payload), encoding="utf-8")


def check_payload(payload: dict[str, Any], path: Path) -> None:
    recorded = json.loads(path.read_text(encoding="utf-8"))
    if recorded != payload:
        raise AssertionError(f"payload differs from {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive-max-nonzero", type=int, default=15)
    parser.add_argument("--sample-count", type=int, default=2048)
    parser.add_argument("--seed", type=int, default=20260514)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", type=Path, default=None)
    args = parser.parse_args()

    payload = build_payload(args)
    if args.check is not None:
        check_payload(payload, args.check)
        print(f"checked {args.check}")
        return

    write_json(payload, args.json)
    write_report(payload, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
