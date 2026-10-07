"""Audit convolutional current layers for the three-gap grammar.

This is the next bridge after ``three_gap_compression_safety_audit.py``.
The PSL-boundary phase vector has coordinates

    f_j(eta) = a_eta * chi_eta(x_j),

after the edge factor chi_eta(gamma)-1 and any fixed boundary/Hayes-Mobius
weights are absorbed into a_eta.  The k-fold cyclic convolution satisfies

    (f_j^{*k})(zeta) = D_k(zeta) * chi_zeta(x_j),

so the convolutional current layer is still diagonal by output character
label zeta.  Therefore it should preserve the three-gap support and jump-class
grammar before any non-diagonal current compression is applied.

The audit tests this finite statement on the same squarefree cyclic faces used
by the earlier Paper 25 three-gap audits.  It is not a proof that the Paper 22
Hayes-Mobius leakage norm is already diagonal; it certifies that the
convolutional coefficient layer is safe if the subsequent leakage quotient is
zeta-diagonal, or if any non-diagonal correction is priced separately.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from three_gap_psl_boundary_audit import (
    DEFAULT_PREFIX_FRACTIONS,
    DEFAULT_ROWS,
    check_fraction_gaps,
    conductor,
    cyclic_gaps,
    divisors_from_primes,
    format_fraction,
    is_squarefree,
    non_split_boundary_etas,
    omega,
    prefix_lengths,
    prime_factors,
    primitive_generators,
    parse_fraction_csv,
    parse_int_csv,
)


DEFAULT_JSON = Path("empirical/reports/three_gap_convolutional_current_audit.json")
DEFAULT_REPORT = Path("empirical/reports/three_gap_convolutional_current_audit.md")
DEFAULT_SEED_MODES = "plain_count,mobius,oriented_boundary"
DEFAULT_ORDERS = "1,2,3,4"


def mobius_squarefree(value: int) -> int:
    return -1 if omega(value) % 2 else 1


def seed_vector(
    *,
    n: int,
    gamma: int,
    entries: list[dict[str, int]],
    mode: str,
) -> np.ndarray:
    seed = np.zeros(n, dtype=np.complex128)
    for entry in entries:
        eta = entry["eta"]
        if mode == "plain_count":
            weight = 1.0
        elif mode == "mobius":
            weight = mobius_squarefree(entry["eta_conductor"])
        elif mode == "oriented_boundary":
            weight = 1.0 if omega(entry["tgt"]) > omega(entry["src"]) else -1.0
        else:
            raise ValueError(f"unknown seed mode: {mode}")
        seed[eta] += weight
    edge = np.exp(2j * np.pi * np.arange(n) * gamma / n) - 1.0
    seed *= edge
    seed[0] = 0.0
    return seed


def convolution_base(seed: np.ndarray, order: int) -> np.ndarray:
    if order < 1:
        raise ValueError("convolution order must be positive")
    return np.fft.ifft(np.fft.fft(seed) ** order)


def output_labels(n: int) -> list[int]:
    labels: list[int] = []
    for label in range(1, n):
        if omega(conductor(label, n)) >= 2:
            labels.append(label)
    return labels


def current_matrix(
    *,
    n: int,
    gamma: int,
    prefix: int,
    base: np.ndarray,
    outputs: list[int],
) -> np.ndarray:
    if not outputs:
        return np.zeros((prefix, 0), dtype=np.complex128)
    x_values = np.array([(j * gamma) % n for j in range(prefix)], dtype=float)
    labels = np.array(outputs, dtype=float)
    phase = np.exp(2j * np.pi * np.outer(x_values, labels) / n)
    matrix = phase * base[outputs][None, :]
    return matrix - matrix.mean(axis=0, keepdims=True)


def float_classes(values: list[float], tolerance: float) -> list[float]:
    positive = sorted(value for value in values if value > tolerance)
    classes: list[float] = []
    for value in positive:
        scale = max(1.0, abs(value), abs(classes[-1]) if classes else 0.0)
        if not classes or abs(value - classes[-1]) > tolerance * scale:
            classes.append(value)
    return classes


def audit_record(
    *,
    n: int,
    face: int,
    gamma: int,
    prefix: int,
    seed_mode: str,
    order: int,
    entries: list[dict[str, int]],
    tolerance: float,
) -> dict[str, Any]:
    seed = seed_vector(n=n, gamma=gamma, entries=entries, mode=seed_mode)
    base = convolution_base(seed, order)
    outputs = [
        label for label in output_labels(n) if abs(base[label]) > tolerance
    ]
    matrix = current_matrix(n=n, gamma=gamma, prefix=prefix, base=base, outputs=outputs)

    points = [Fraction((j * gamma) % n, n) for j in range(prefix)]
    rotation = check_fraction_gaps(cyclic_gaps(points))
    norms = np.linalg.norm(matrix, axis=1) if matrix.shape[1] else np.zeros(prefix)
    support = [j for j, value in enumerate(norms) if value > tolerance]
    support_check = check_fraction_gaps(
        cyclic_gaps([Fraction((j * gamma) % n, n) for j in support])
    )

    ordered = sorted(range(prefix), key=lambda j: Fraction((j * gamma) % n, n))
    jumps: list[float] = []
    by_gap: dict[str, list[float]] = defaultdict(list)
    for index, current in enumerate(ordered):
        following = ordered[(index + 1) % len(ordered)]
        current_point = Fraction((current * gamma) % n, n)
        next_point = Fraction((following * gamma) % n, n)
        gap = (next_point - current_point) % 1
        value = float(np.linalg.norm(matrix[following] - matrix[current]))
        jumps.append(value)
        by_gap[format_fraction(gap)].append(value)

    per_gap_classes = {
        gap: [float(value) for value in float_classes(values, tolerance)]
        for gap, values in sorted(by_gap.items(), key=lambda item: Fraction(item[0]))
    }
    jump_classes = float_classes(jumps, tolerance)
    lift_ok = all(len(classes) <= 1 for classes in per_gap_classes.values())
    count_ok = len(jump_classes) <= rotation.primitive_count
    return {
        "row": n,
        "face": face,
        "gamma": gamma,
        "prefix": prefix,
        "seed_mode": seed_mode,
        "order": order,
        "entry_count": len(entries),
        "output_count": len(outputs),
        "zero_current": len(outputs) == 0 or bool(float(np.max(norms)) <= tolerance),
        "rotation_gap_count": rotation.primitive_count,
        "support_gap_count": support_check.primitive_count,
        "jump_class_count": len(jump_classes),
        "support_three_gap_ok": support_check.three_gap_ok,
        "jump_lift_ok": lift_ok,
        "jump_count_ok": count_ok,
        "first_gap_classes": dict(list(per_gap_classes.items())[:4]),
        "jump_classes": [float(value) for value in jump_classes[:8]],
    }


def audit_record_from_base(
    *,
    n: int,
    face: int,
    gamma: int,
    prefix: int,
    seed_mode: str,
    order: int,
    base: np.ndarray,
    outputs: list[int],
    entry_count: int,
    tolerance: float,
) -> dict[str, Any]:
    matrix = current_matrix(n=n, gamma=gamma, prefix=prefix, base=base, outputs=outputs)

    points = [Fraction((j * gamma) % n, n) for j in range(prefix)]
    rotation = check_fraction_gaps(cyclic_gaps(points))
    norms = np.linalg.norm(matrix, axis=1) if matrix.shape[1] else np.zeros(prefix)
    support = [j for j, value in enumerate(norms) if value > tolerance]
    support_check = check_fraction_gaps(
        cyclic_gaps([Fraction((j * gamma) % n, n) for j in support])
    )

    ordered = sorted(range(prefix), key=lambda j: Fraction((j * gamma) % n, n))
    jumps: list[float] = []
    by_gap: dict[str, list[float]] = defaultdict(list)
    for index, current in enumerate(ordered):
        following = ordered[(index + 1) % len(ordered)]
        current_point = Fraction((current * gamma) % n, n)
        next_point = Fraction((following * gamma) % n, n)
        gap = (next_point - current_point) % 1
        value = float(np.linalg.norm(matrix[following] - matrix[current]))
        jumps.append(value)
        by_gap[format_fraction(gap)].append(value)

    per_gap_classes = {
        gap: [float(value) for value in float_classes(values, tolerance)]
        for gap, values in sorted(by_gap.items(), key=lambda item: Fraction(item[0]))
    }
    jump_classes = float_classes(jumps, tolerance)
    lift_ok = all(len(classes) <= 1 for classes in per_gap_classes.values())
    count_ok = len(jump_classes) <= rotation.primitive_count
    return {
        "row": n,
        "face": face,
        "gamma": gamma,
        "prefix": prefix,
        "seed_mode": seed_mode,
        "order": order,
        "entry_count": entry_count,
        "output_count": len(outputs),
        "zero_current": len(outputs) == 0 or bool(float(np.max(norms)) <= tolerance),
        "rotation_gap_count": rotation.primitive_count,
        "support_gap_count": support_check.primitive_count,
        "jump_class_count": len(jump_classes),
        "support_three_gap_ok": support_check.three_gap_ok,
        "jump_lift_ok": lift_ok,
        "jump_count_ok": count_ok,
        "first_gap_classes": dict(list(per_gap_classes.items())[:4]),
        "jump_classes": [float(value) for value in jump_classes[:8]],
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    fractions = parse_fraction_csv(args.prefix_fractions)
    seed_modes = [item.strip() for item in args.seed_modes.split(",") if item.strip()]
    orders = parse_int_csv(args.orders)
    records: list[dict[str, Any]] = []
    for n in rows:
        if not is_squarefree(n):
            raise ValueError(f"row {n} is not squarefree")
        primes = prime_factors(n)
        all_outputs = output_labels(n)
        for face in divisors_from_primes(primes, args.min_face_omega):
            face_primes = prime_factors(face)
            entries = non_split_boundary_etas(n, face)
            generators = primitive_generators(n, face_primes)
            if args.max_generators_per_face > 0:
                generators = generators[: args.max_generators_per_face]
            for generator in generators:
                gamma = generator["gamma"]
                bases: dict[tuple[str, int], tuple[np.ndarray, list[int]]] = {}
                for seed_mode in seed_modes:
                    seed = seed_vector(n=n, gamma=gamma, entries=entries, mode=seed_mode)
                    for order in orders:
                        base = convolution_base(seed, order)
                        outputs = [
                            label for label in all_outputs if abs(base[label]) > args.tolerance
                        ]
                        bases[(seed_mode, order)] = (base, outputs)
                for prefix in prefix_lengths(face, fractions):
                    for seed_mode in seed_modes:
                        for order in orders:
                            base, outputs = bases[(seed_mode, order)]
                            records.append(
                                audit_record_from_base(
                                    n=n,
                                    face=face,
                                    gamma=gamma,
                                    prefix=prefix,
                                    seed_mode=seed_mode,
                                    order=order,
                                    base=base,
                                    outputs=outputs,
                                    entry_count=len(entries),
                                    tolerance=args.tolerance,
                                )
                            )
    return {
        "config": {
            "rows": rows,
            "min_face_omega": args.min_face_omega,
            "prefix_fractions": [str(frac) for frac in fractions],
            "max_generators_per_face": args.max_generators_per_face,
            "seed_modes": seed_modes,
            "orders": orders,
            "tolerance": args.tolerance,
            "claim_hygiene": (
                "the convolutional coefficient layer is zeta-diagonal-safe; "
                "the actual leakage norm still needs a diagonal or corrected "
                "compression proof"
            ),
        },
        "summary": summarize(records),
        "first_failures": first_failures(records),
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_seed_order: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    by_order: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_seed_order[(record["seed_mode"], record["order"])].append(record)
        by_order[record["order"]].append(record)

    def aggregate(items: list[dict[str, Any]]) -> dict[str, Any]:
        total = len(items)
        return {
            "records": total,
            "support_ok": sum(item["support_three_gap_ok"] for item in items),
            "jump_lift_ok": sum(item["jump_lift_ok"] for item in items),
            "jump_count_ok": sum(item["jump_count_ok"] for item in items),
            "zero_current": sum(item["zero_current"] for item in items),
            "max_output_count": max((item["output_count"] for item in items), default=0),
            "max_support_gap_count": max(
                (item["support_gap_count"] for item in items), default=0
            ),
            "max_jump_class_count": max(
                (item["jump_class_count"] for item in items), default=0
            ),
        }

    return {
        "records": len(records),
        "all": aggregate(records),
        "by_order": {str(order): aggregate(items) for order, items in sorted(by_order.items())},
        "by_seed_order": {
            f"{seed}:k{order}": aggregate(items)
            for (seed, order), items in sorted(by_seed_order.items())
        },
    }


def first_failures(records: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for record in records:
        if record["support_three_gap_ok"] and record["jump_lift_ok"] and record["jump_count_ok"]:
            continue
        out.append(record)
        if len(out) >= limit:
            break
    return out


def pct(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "0.00%"
    return f"{100.0 * numerator / denominator:.2f}%"


def render_report(payload: dict[str, Any]) -> str:
    config = payload["config"]
    summary = payload["summary"]
    all_summary = summary["all"]
    lines = [
        "# Three-Gap Convolutional Current Audit",
        "",
        "This audit tests the all-order convolutional coefficient layer used by",
        "Hayes-Mobius-style currents.  The theorem-safe statement is that",
        "k-fold cyclic convolution of fixed character-phase data remains",
        "diagonal by the output character label `zeta`.",
        "",
        "## Config",
        "",
        f"- `rows`: `{config['rows']}`",
        f"- `min_face_omega`: `{config['min_face_omega']}`",
        f"- `prefix_fractions`: `{config['prefix_fractions']}`",
        f"- `max_generators_per_face`: `{config['max_generators_per_face']}`",
        f"- `seed_modes`: `{config['seed_modes']}`",
        f"- `orders`: `{config['orders']}`",
        f"- `tolerance`: `{config['tolerance']}`",
        "",
        "## Aggregate",
        "",
        "| check | pass | total | rate | max classes |",
        "|---|---:|---:|---:|---:|",
        "| support gaps | {ok} | {total} | {rate} | {maxc} |".format(
            ok=all_summary["support_ok"],
            total=all_summary["records"],
            rate=pct(all_summary["support_ok"], all_summary["records"]),
            maxc=all_summary["max_support_gap_count"],
        ),
        "| jump lift | {ok} | {total} | {rate} | {maxc} |".format(
            ok=all_summary["jump_lift_ok"],
            total=all_summary["records"],
            rate=pct(all_summary["jump_lift_ok"], all_summary["records"]),
            maxc=all_summary["max_jump_class_count"],
        ),
        "| jump count <= rotation count | {ok} | {total} | {rate} | {maxc} |".format(
            ok=all_summary["jump_count_ok"],
            total=all_summary["records"],
            rate=pct(all_summary["jump_count_ok"], all_summary["records"]),
            maxc=all_summary["max_jump_class_count"],
        ),
        "",
        f"- zero current records after split quotient: `{all_summary['zero_current']}`",
        f"- max output character count: `{all_summary['max_output_count']}`",
        "",
        "## By Seed And Order",
        "",
        "| seed/order | records | support | jump lift | jump count | zero current | max outputs |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for key, item in summary["by_seed_order"].items():
        lines.append(
            "| {key} | {records} | {support} | {lift} | {count} | {zero} | {outputs} |".format(
                key=key,
                records=item["records"],
                support=f"{item['support_ok']}/{item['records']}",
                lift=f"{item['jump_lift_ok']}/{item['records']}",
                count=f"{item['jump_count_ok']}/{item['records']}",
                zero=item["zero_current"],
                outputs=item["max_output_count"],
            )
        )
    lines += [
        "",
        "## First Failures",
        "",
    ]
    failures = payload["first_failures"]
    if not failures:
        lines += ["No support, jump-lift, or jump-count failures in this run.", ""]
    else:
        lines += [
            "| row | face | gamma | prefix | seed | order | output count | jump classes |",
            "|---:|---:|---:|---:|---|---:|---:|---|",
        ]
        for record in failures:
            lines.append(
                "| {row} | {face} | {gamma} | {prefix} | {seed} | {order} | {outputs} | {classes} |".format(
                    row=record["row"],
                    face=record["face"],
                    gamma=record["gamma"],
                    prefix=record["prefix"],
                    seed=record["seed_mode"],
                    order=record["order"],
                    outputs=record["output_count"],
                    classes=record["jump_classes"],
                )
            )
        lines.append("")
    lines += [
        "## Reading",
        "",
        "For fixed boundary/Hayes-Mobius seed weights, convolution itself does",
        "not mix starting phases.  The output coefficient at label `zeta` is",
        "again a fixed coefficient times `chi_zeta(x_j)`.  Thus all tested",
        "orders inherit the same three-gap support and jump-class grammar.",
        "",
        "The remaining Paper 22 bridge is therefore not the convolutional",
        "coefficient layer.  It is the leakage norm or compression applied",
        "after this layer: it must be zeta-diagonal after split/flat quotienting",
        "or have an explicit non-diagonal correction that is priced separately.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default=DEFAULT_ROWS)
    parser.add_argument("--min-face-omega", type=int, default=2)
    parser.add_argument("--prefix-fractions", default=DEFAULT_PREFIX_FRACTIONS)
    parser.add_argument("--seed-modes", default=DEFAULT_SEED_MODES)
    parser.add_argument("--orders", default=DEFAULT_ORDERS)
    parser.add_argument("--max-generators-per-face", type=int, default=0)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    all_summary = payload["summary"]["all"]
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    print(
        "records={records} support={support}/{records} jump_lift={lift}/{records} "
        "jump_count={count}/{records}".format(
            records=all_summary["records"],
            support=all_summary["support_ok"],
            lift=all_summary["jump_lift_ok"],
            count=all_summary["jump_count_ok"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
