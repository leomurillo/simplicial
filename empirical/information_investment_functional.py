"""Prototype B0 information-investment functional on finite behavior tables.

B0 is the bridge from the exact Fisher/conductor skeleton (F0) to the
information-investment attractor (A0).  This script keeps the first version
deliberately finite: build exact categorical rows, generate a nonuniform
probability from a reciprocal Fourier support, and score candidate
discretizations by

    J(D) = projection error + reciprocal error + closure leakage
           + descent-balance cost + resource_weight * resource cost.

The new descent-balance term encodes the nested zero-sum idea: a support that
uses a higher conductor level should pay for missing lower balance-transfer
levels in the conductor/divisor ladder.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
import random
import sys
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Hashable


sys.path.insert(0, str(Path(__file__).resolve().parent))

from local_adjacency_constructor import FiniteLocalRing, make_f2_u4_ring, make_f4_u2_ring


Mode = Hashable
DEFAULT_JSON = Path("empirical/reports/information_investment_functional.json")
DEFAULT_REPORT = Path("empirical/reports/information_investment_functional.md")


@dataclass(frozen=True)
class FiniteRow:
    key: str
    name: str
    labels: tuple[Mode, ...]
    modes: tuple[Mode, ...]
    zero: Mode
    add: Callable[[Mode, Mode], Mode]
    conductor: Callable[[Mode], str]
    conductor_rank: Callable[[str], int]
    label_name: Callable[[Mode], str]
    character: Callable[[Mode, Mode], complex]
    normalizer_actions: tuple[dict[Mode, Mode], ...] = ()

    @property
    def nonzero_modes(self) -> tuple[Mode, ...]:
        return tuple(mode for mode in self.modes if mode != self.zero)


def cyclic_conductor(n: int, k: int) -> int:
    k %= n
    if k == 0:
        return 1
    return n // math.gcd(n, k)


def cyclic_row(n: int) -> FiniteRow:
    labels = tuple(range(n))
    units = tuple(value for value in range(n) if math.gcd(value, n) == 1)

    def add(a: int, b: int) -> int:
        return (a + b) % n

    def character(mode: int, label: int) -> complex:
        return cmath.exp(-2j * math.pi * mode * label / n)

    return FiniteRow(
        key=f"c{n}",
        name=f"C_{n}",
        labels=labels,
        modes=labels,
        zero=0,
        add=add,
        conductor=lambda mode: str(cyclic_conductor(n, int(mode))),
        conductor_rank=lambda conductor: int(conductor),
        label_name=lambda mode: str(mode),
        character=character,
        normalizer_actions=tuple(
            {mode: (unit * mode) % n for mode in labels}
            for unit in units
        ),
    )


def _bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> index) & 1 for index in range(width))


def _local_bits(label: tuple[int, ...], field_width: int) -> tuple[int, ...]:
    out: list[int] = []
    for coefficient in label:
        out.extend(_bits(coefficient, field_width))
    return tuple(out)


def _normalizer_maps(ring: FiniteLocalRing) -> tuple[dict[Mode, Mode], ...]:
    return tuple(
        {label: ring.apply(action, label) for label in ring.labels}
        for action in ring.normalizer_actions
    )


def local_row_from_ring(key: str, ring: FiniteLocalRing, field_width: int) -> FiniteRow:
    total_width = max(1, (len(ring.labels) - 1).bit_length())
    bit_cache = {
        label: (
            _local_bits(label, field_width)
            if isinstance(label, tuple)
            else _bits(int(label), total_width)
        )
        for label in ring.labels
    }
    conductor_order = {name: index + 1 for index, name in enumerate(ring.conductor_order)}

    def character(mode: Mode, label: Mode) -> complex:
        mode_bits = bit_cache[mode]  # type: ignore[index]
        label_bits = bit_cache[label]  # type: ignore[index]
        dot = sum(a * b for a, b in zip(mode_bits, label_bits)) % 2
        return -1.0 if dot else 1.0

    return FiniteRow(
        key=key,
        name=ring.name,
        labels=ring.labels,
        modes=ring.labels,
        zero=ring.zero,
        add=ring.add,
        conductor=ring.conductor,
        conductor_rank=lambda conductor: conductor_order[conductor],
        label_name=ring.label_name,
        character=character,
        normalizer_actions=_normalizer_maps(ring),
    )


def local_row_f4_u2() -> FiniteRow:
    return local_row_from_ring("f4-u2", make_f4_u2_ring(), 2)


def local_row_f2_u4() -> FiniteRow:
    return local_row_from_ring("f2-u4", make_f2_u4_ring(), 1)


def dft(row: FiniteRow, values: dict[Mode, float]) -> dict[Mode, complex]:
    return {
        mode: sum(values[label] * row.character(mode, label) for label in row.labels)
        for mode in row.modes
    }


def energy(coefficients: dict[Mode, complex], modes: Iterable[Mode]) -> float:
    return sum(abs(coefficients[mode]) ** 2 for mode in modes)


def reciprocal_density_from_support(
    row: FiniteRow,
    support: set[Mode],
    amplitude: float,
) -> tuple[dict[Mode, float], dict[Mode, float]]:
    if not support:
        reciprocal = {label: 1.0 for label in row.labels}
    else:
        scale = amplitude / len(support)
        reciprocal = {}
        for label in row.labels:
            oscillation = sum(row.character(mode, label).real for mode in support)
            reciprocal[label] = 1.0 + scale * oscillation

    min_value = min(reciprocal.values())
    if min_value <= 0:
        raise ValueError(f"reciprocal density is not positive: min={min_value}")

    inverse_total = sum(1.0 / value for value in reciprocal.values())
    probability = {label: (1.0 / reciprocal[label]) / inverse_total for label in row.labels}
    return reciprocal, probability


def projection_error(coefficients: dict[Mode, complex], row: FiniteRow, support: set[Mode]) -> float:
    total = energy(coefficients, row.nonzero_modes)
    if total == 0:
        return 0.0
    outside = [mode for mode in row.nonzero_modes if mode not in support]
    return energy(coefficients, outside) / total


def closure_leakage(coefficients: dict[Mode, complex], row: FiniteRow, support: set[Mode]) -> float:
    active = [mode for mode in support if mode != row.zero and abs(coefficients[mode]) > 1e-10]
    denominator = 0.0
    numerator = 0.0
    for left in active:
        for right in active:
            weight = abs(coefficients[left]) ** 2 * abs(coefficients[right]) ** 2
            if weight == 0:
                continue
            target = row.add(left, right)
            denominator += weight
            if target != row.zero and target not in support:
                numerator += weight
    if denominator == 0:
        return 0.0
    return numerator / denominator


def descent_required_modes(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    return generated_subgroup(row, support)


def generated_subgroup(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    generators = [mode for mode in support if mode != row.zero]
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


def normalizer_saturation(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    if not row.normalizer_actions:
        return generated_subgroup(row, support)

    orbit_support: set[Mode] = set()
    for mode in support:
        if mode == row.zero:
            continue
        for action in row.normalizer_actions:
            orbit_support.add(action[mode])
    return generated_subgroup(row, orbit_support)


def descent_balance_cost(row: FiniteRow, support: set[Mode]) -> float:
    required = descent_required_modes(row, support)
    if not required:
        return 0.0
    return len(required - support) / len(required)


def resource_cost(row: FiniteRow, support: set[Mode]) -> float:
    if not row.nonzero_modes:
        return 0.0
    return len([mode for mode in support if mode != row.zero]) / len(row.nonzero_modes)


def score_candidate(
    row: FiniteRow,
    support: set[Mode],
    h_hat: dict[Mode, complex],
    m_hat: dict[Mode, complex],
    resource_weight: float,
) -> dict[str, float]:
    fisher_projection = projection_error(h_hat, row, support)
    reciprocal_projection = projection_error(m_hat, row, support)
    closure = closure_leakage(m_hat, row, support)
    balance = descent_balance_cost(row, support)
    resource = resource_cost(row, support)
    total = fisher_projection + reciprocal_projection + closure + balance + resource_weight * resource
    return {
        "J": total,
        "fisher_projection_error": fisher_projection,
        "reciprocal_projection_error": reciprocal_projection,
        "closure_leakage": closure,
        "descent_balance_cost": balance,
        "resource_cost": resource,
    }


def symmetrize_cyclic(n: int, modes: Iterable[int]) -> set[int]:
    out: set[int] = set()
    for mode in modes:
        mode %= n
        if mode == 0:
            continue
        out.add(mode)
        out.add((-mode) % n)
    return out


def cyclic_descent_closure(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    active_conductors = {
        int(row.conductor(mode))
        for mode in support
        if mode != row.zero
    }
    if not active_conductors:
        return set()
    combined_conductor = math.lcm(*active_conductors)
    return {
        mode
        for mode in row.nonzero_modes
        if combined_conductor % int(row.conductor(mode)) == 0
    }


def local_descent_closure(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    return generated_subgroup(row, support)


def allowed_reciprocal_modes(row: FiniteRow) -> set[Mode]:
    allowed: set[Mode] = set()
    for eta in row.modes:
        ok = True
        for source in row.nonzero_modes:
            target = row.add(eta, source)
            if target == row.zero:
                continue
            if row.conductor(source) != row.conductor(target):
                ok = False
                break
        if ok and eta != row.zero:
            allowed.add(eta)
    return allowed


def low_index_support(row: FiniteRow, size: int) -> set[Mode]:
    if row.key.startswith("c"):
        n = len(row.labels)
        ordered = sorted(row.nonzero_modes, key=lambda mode: (min(int(mode), n - int(mode)), int(mode)))
    else:
        ordered = sorted(row.nonzero_modes, key=row.label_name)
    return set(ordered[:size])


def random_support(row: FiniteRow, size: int, seed: int) -> set[Mode]:
    rng = random.Random(seed)
    return set(rng.sample(list(row.nonzero_modes), min(size, len(row.nonzero_modes))))


def top_energy_support(row: FiniteRow, coefficients: dict[Mode, complex], size: int) -> set[Mode]:
    ordered = sorted(
        row.nonzero_modes,
        key=lambda mode: (-abs(coefficients[mode]) ** 2, row.label_name(mode)),
    )
    return set(ordered[:size])


def conductor_packet_support(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    conductors = {row.conductor(mode) for mode in support if mode != row.zero}
    return {mode for mode in row.nonzero_modes if row.conductor(mode) in conductors}


def row_active_support(row: FiniteRow) -> set[Mode]:
    if row.key == "c7":
        return symmetrize_cyclic(7, [1])
    if row.key == "c8":
        return {4}
    if row.key == "c12":
        return symmetrize_cyclic(12, [3])
    if row.key == "f4-u2":
        return {mode for mode in row.nonzero_modes if row.conductor(mode) == "u"}
    raise ValueError(f"no active support configured for {row.key}")


def candidate_supports(row: FiniteRow, true_support: set[Mode], seed: int) -> dict[str, set[Mode]]:
    size = len(true_support)
    if row.key.startswith("c"):
        descent = cyclic_descent_closure(row, true_support)
    else:
        descent = local_descent_closure(row, true_support)
    candidates = {
        "zero": set(),
        "true_support": set(true_support),
        "descent_closure": descent,
        "normalizer_saturation": normalizer_saturation(row, true_support),
        "conductor_packet": conductor_packet_support(row, true_support),
        "allowed_reciprocal": allowed_reciprocal_modes(row),
        "low_index": low_index_support(row, size),
        "random_same_size": random_support(row, size, seed),
        "full": set(row.nonzero_modes),
    }
    return candidates


def run_row(row: FiniteRow, amplitude: float, resource_weight: float, seed: int) -> dict[str, Any]:
    true_support = row_active_support(row)
    reciprocal, probability = reciprocal_density_from_support(row, true_support, amplitude)
    uniform = 1.0 / len(row.labels)
    tangent = {label: probability[label] - uniform for label in row.labels}
    h_hat = dft(row, tangent)
    m_hat = dft(row, reciprocal)

    support_map = candidate_supports(row, true_support, seed)
    support_map["top_fisher_energy"] = top_energy_support(row, h_hat, len(true_support))

    candidates = []
    for name, support in support_map.items():
        scores = score_candidate(row, support, h_hat, m_hat, resource_weight)
        required = descent_required_modes(row, support)
        candidates.append(
            {
                "name": name,
                "support_size": len(support),
                "support": [row.label_name(mode) for mode in sorted(support, key=row.label_name)],
                "required_descent_size": len(required),
                **scores,
            }
        )
    candidates.sort(key=lambda item: (item["J"], item["resource_cost"], item["name"]))
    return {
        "key": row.key,
        "row": row.name,
        "label_count": len(row.labels),
        "active_reciprocal_support": [
            row.label_name(mode) for mode in sorted(true_support, key=row.label_name)
        ],
        "amplitude": amplitude,
        "resource_weight": resource_weight,
        "winner": candidates[0]["name"],
        "candidates": candidates,
    }


def build_rows(row_keys: Iterable[str]) -> list[FiniteRow]:
    rows: list[FiniteRow] = []
    for key in row_keys:
        normalized = key.strip().lower()
        if not normalized:
            continue
        if normalized.startswith("c") and normalized[1:].isdigit():
            rows.append(cyclic_row(int(normalized[1:])))
        elif normalized == "f4-u2":
            rows.append(local_row_f4_u2())
        elif normalized == "f2-u4":
            rows.append(local_row_f2_u4())
        else:
            raise ValueError(f"unknown row key: {key}")
    return rows


def build_payload(
    row_keys: list[str],
    amplitude: float,
    resource_weight: float,
    seed: int,
) -> dict[str, Any]:
    rows = [run_row(row, amplitude, resource_weight, seed) for row in build_rows(row_keys)]
    return {
        "purpose": "Prototype B0 information-investment functional on exact finite rows.",
        "functional": {
            "J": (
                "fisher_projection_error + reciprocal_projection_error + "
                "closure_leakage + descent_balance_cost + "
                "resource_weight * resource_cost"
            ),
            "resource_weight": resource_weight,
            "amplitude": amplitude,
            "seed": seed,
        },
        "rows": rows,
    }


def write_json(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# B0 Information-Investment Functional Prototype",
        "",
        "This report scores candidate finite discretizations on exact behavior",
        "tables.  It is the first computable bridge from F0 to A0.",
        "",
        "```text",
        payload["functional"]["J"],
        "```",
        "",
        f"Resource weight: `{payload['functional']['resource_weight']}`.",
        f"Reciprocal-density amplitude: `{payload['functional']['amplitude']}`.",
        "",
    ]

    for row in payload["rows"]:
        lines += [
            f"## {row['row']}",
            "",
            f"Active reciprocal support: `{', '.join(row['active_reciprocal_support'])}`.",
            f"Winner: `{row['winner']}`.",
            "",
            "| candidate | J | Fisher err | reciprocal err | closure | balance | resource | support |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for candidate in row["candidates"]:
            lines.append(
                "| {name} | {J:.6f} | {fisher:.6f} | {reciprocal:.6f} | "
                "{closure:.6f} | {balance:.6f} | {resource:.6f} | {support_size} |".format(
                    name=candidate["name"],
                    J=candidate["J"],
                    fisher=candidate["fisher_projection_error"],
                    reciprocal=candidate["reciprocal_projection_error"],
                    closure=candidate["closure_leakage"],
                    balance=candidate["descent_balance_cost"],
                    resource=candidate["resource_cost"],
                    support_size=candidate["support_size"],
                )
            )
        lines.append("")

    lines += [
        "## Reading",
        "",
        "`true_support` tests raw approximation.  `descent_closure` tests the",
        "nested zero-sum balance principle: if a support uses a conductor level,",
        "it should pay for the lower balance-transfer levels needed for closure.",
        "`normalizer_saturation` adds the smallest symmetry-complete subgroup",
        "generated by the normalizer orbit of the active support.",
        "`allowed_reciprocal` is the exact Paper 10 full-block orthogonality",
        "support.  `top_fisher_energy` is a PCA-style finite-table baseline.",
        "`low_index` and `random_same_size` are adversarial baselines.",
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
    parser.add_argument("--rows", default="c7,c8,c12,f4-u2")
    parser.add_argument("--amplitude", type=float, default=0.35)
    parser.add_argument("--resource-weight", type=float, default=0.25)
    parser.add_argument("--seed", type=int, default=20260514)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", type=Path, default=None)
    args = parser.parse_args()

    row_keys = [key.strip() for key in args.rows.split(",") if key.strip()]
    payload = build_payload(row_keys, args.amplitude, args.resource_weight, args.seed)
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
