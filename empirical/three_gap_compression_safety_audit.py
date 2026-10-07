"""Audit which PSL-boundary compressions preserve the three-gap grammar.

Paper 25 Section 3.17 proves that the non-split PSL-boundary phase vector has
support gaps and jump classes lifted from the finite rotation gaps.  The next
question is whether a Hayes-Mobius/current-level compression preserves that
grammar.

This script tests a sharp finite criterion:

* eta-diagonal compressions preserve the grammar, because the squared jump
  norm is a weighted sum of terms depending only on the adjacent rotation gap.
* lossy conductor-only compressions can mix distinct character phases.  Then
  the jump norm may depend on the starting point inside the same rotation gap,
  so the lifted three-gap grammar can fail.

The squarefree rows here are diagnostic models for the primorial CRT tower.
The unsafe modes are not claimed to be the actual Paper 22 Hayes-Mobius map;
they are falsifiers showing what the current-level quotient must avoid or
control.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from three_gap_psl_boundary_audit import (
    DEFAULT_PREFIX_FRACTIONS,
    DEFAULT_ROWS,
    check_fraction_gaps,
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


DEFAULT_JSON = Path("empirical/reports/three_gap_compression_safety_audit.json")
DEFAULT_REPORT = Path("empirical/reports/three_gap_compression_safety_audit.md")
DEFAULT_MODES = "eta_diagonal,boundary_eta_diagonal,eta_conductor,boundary_eta_conductor,mobius_total,boundary_mobius_total"


def mobius_squarefree(value: int) -> int:
    return -1 if omega(value) % 2 else 1


def group_weights(entries: list[dict[str, int]], mode: str) -> dict[str, dict[int, complex]]:
    grouped: dict[str, dict[int, complex]] = defaultdict(lambda: defaultdict(complex))
    for entry in entries:
        eta = entry["eta"]
        eta_conductor = entry["eta_conductor"]
        src = entry["src"]
        tgt = entry["tgt"]
        if mode == "eta_diagonal":
            key = f"eta:{eta}"
            weight = 1.0
        elif mode == "boundary_eta_diagonal":
            key = f"{src}->{tgt}:eta:{eta}"
            weight = 1.0
        elif mode == "eta_conductor":
            key = f"cond:{eta_conductor}"
            weight = 1.0
        elif mode == "boundary_eta_conductor":
            key = f"{src}->{tgt}:cond:{eta_conductor}"
            weight = 1.0
        elif mode == "mobius_total":
            key = "mobius_total"
            weight = mobius_squarefree(eta_conductor)
        elif mode == "boundary_mobius_total":
            key = f"{src}->{tgt}:mobius_total"
            weight = mobius_squarefree(eta_conductor)
        else:
            raise ValueError(f"unknown compression mode: {mode}")
        grouped[key][eta] += weight
    return {key: dict(weights) for key, weights in grouped.items()}


def compressed_matrix(
    *,
    n: int,
    gamma: int,
    prefix: int,
    grouped: dict[str, dict[int, complex]],
) -> np.ndarray:
    keys = sorted(grouped)
    if not keys:
        return np.zeros((prefix, 0), dtype=np.complex128)
    x_values = np.array([(j * gamma) % n for j in range(prefix)], dtype=float)
    matrix = np.zeros((prefix, len(keys)), dtype=np.complex128)
    for col, key in enumerate(keys):
        for eta, multiplicity in grouped[key].items():
            step = np.exp(2j * np.pi * eta * gamma / n) - 1.0
            phase = np.exp(2j * np.pi * x_values * eta / n)
            matrix[:, col] += multiplicity * step * phase
    return matrix - matrix.mean(axis=0, keepdims=True)


def float_classes(values: list[float], tolerance: float) -> list[float]:
    positive = sorted(value for value in values if value > tolerance)
    classes: list[float] = []
    for value in positive:
        if not classes or abs(value - classes[-1]) > tolerance:
            classes.append(value)
    return classes


def audit_mode_record(
    *,
    n: int,
    face: int,
    gamma: int,
    prefix: int,
    mode: str,
    entries: list[dict[str, int]],
    tolerance: float,
) -> dict[str, Any]:
    points = [Fraction((j * gamma) % n, n) for j in range(prefix)]
    rotation = check_fraction_gaps(cyclic_gaps(points))
    grouped = group_weights(entries, mode)
    matrix = compressed_matrix(n=n, gamma=gamma, prefix=prefix, grouped=grouped)
    norms = np.linalg.norm(matrix, axis=1) if matrix.shape[1] else np.zeros(prefix)
    support = [j for j, value in enumerate(norms) if value > tolerance]
    support_check = check_fraction_gaps(
        cyclic_gaps([Fraction((j * gamma) % n, n) for j in support])
    )

    ordered = sorted(range(prefix), key=lambda j: Fraction((j * gamma) % n, n))
    jump_by_gap: dict[str, list[float]] = defaultdict(list)
    all_jumps: list[float] = []
    for index, current in enumerate(ordered):
        following = ordered[(index + 1) % len(ordered)]
        current_point = Fraction((current * gamma) % n, n)
        next_point = Fraction((following * gamma) % n, n)
        gap = (next_point - current_point) % 1
        jump = float(np.linalg.norm(matrix[following] - matrix[current]))
        all_jumps.append(jump)
        jump_by_gap[format_fraction(gap)].append(jump)

    per_gap_classes = {
        gap: [float(value) for value in float_classes(values, tolerance)]
        for gap, values in sorted(jump_by_gap.items(), key=lambda item: Fraction(item[0]))
    }
    jump_classes = float_classes(all_jumps, tolerance)
    lift_ok = all(len(classes) <= 1 for classes in per_gap_classes.values())
    count_ok = len(jump_classes) <= rotation.primitive_count
    eta_diagonal = mode in {"eta_diagonal", "boundary_eta_diagonal"}
    return {
        "row": n,
        "face": face,
        "gamma": gamma,
        "prefix": prefix,
        "mode": mode,
        "eta_diagonal": eta_diagonal,
        "entry_count": len(entries),
        "compressed_dimension": len(grouped),
        "zero_observable": bool(float(np.max(norms)) <= tolerance) if len(norms) else True,
        "rotation_gap_check": rotation.__dict__,
        "support_gap_check": support_check.__dict__,
        "jump_class_check": {
            "primitive_count": len(jump_classes),
            "primitive_sizes": [float(value) for value in jump_classes],
            "classes_lift_from_rotation_gaps": lift_ok,
            "class_count_at_most_rotation_count": count_ok,
            "per_rotation_gap_classes": per_gap_classes,
        },
        "checks": {
            "support_three_gap_ok": support_check.three_gap_ok,
            "jump_lift_ok": lift_ok,
            "jump_count_ok": count_ok,
        },
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    fractions = parse_fraction_csv(args.prefix_fractions)
    modes = [item.strip() for item in args.modes.split(",") if item.strip()]
    records: list[dict[str, Any]] = []
    for n in rows:
        if not is_squarefree(n):
            raise ValueError(f"row {n} is not squarefree")
        primes = prime_factors(n)
        for face in divisors_from_primes(primes, args.min_face_omega):
            face_primes = prime_factors(face)
            entries = non_split_boundary_etas(n, face)
            generators = primitive_generators(n, face_primes)
            if args.max_generators_per_face > 0:
                generators = generators[: args.max_generators_per_face]
            for generator in generators:
                gamma = generator["gamma"]
                for prefix in prefix_lengths(face, fractions):
                    for mode in modes:
                        records.append(
                            audit_mode_record(
                                n=n,
                                face=face,
                                gamma=gamma,
                                prefix=prefix,
                                mode=mode,
                                entries=entries,
                                tolerance=args.tolerance,
                            )
                        )
    return {
        "config": {
            "rows": rows,
            "min_face_omega": args.min_face_omega,
            "prefix_fractions": [str(frac) for frac in fractions],
            "max_generators_per_face": args.max_generators_per_face,
            "modes": modes,
            "tolerance": args.tolerance,
            "claim_hygiene": (
                "eta-diagonal compression is theorem-safe; lossy conductor "
                "compression is a falsifier class, not the asserted Paper 22 map"
            ),
        },
        "summary": summarize(records),
        "records": records,
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_mode: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_row_mode: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_mode[record["mode"]].append(record)
        by_row_mode[(record["row"], record["mode"])].append(record)

    def aggregate(items: list[dict[str, Any]]) -> dict[str, Any]:
        total = len(items)
        return {
            "records": total,
            "support_ok": sum(item["checks"]["support_three_gap_ok"] for item in items),
            "jump_lift_ok": sum(item["checks"]["jump_lift_ok"] for item in items),
            "jump_count_ok": sum(item["checks"]["jump_count_ok"] for item in items),
            "zero_observable": sum(item["zero_observable"] for item in items),
            "max_compressed_dimension": max(
                (item["compressed_dimension"] for item in items), default=0
            ),
            "max_jump_class_count": max(
                (item["jump_class_check"]["primitive_count"] for item in items),
                default=0,
            ),
            "max_support_gap_count": max(
                (item["support_gap_check"]["primitive_count"] for item in items),
                default=0,
            ),
        }

    return {
        "records": len(records),
        "by_mode": {mode: aggregate(items) for mode, items in sorted(by_mode.items())},
        "by_row_mode": {
            f"{row}:{mode}": aggregate(items)
            for (row, mode), items in sorted(by_row_mode.items())
        },
        "first_failures": first_failures(records),
    }


def first_failures(records: list[dict[str, Any]], limit: int = 12) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for record in records:
        if record["checks"]["jump_lift_ok"] and record["checks"]["jump_count_ok"]:
            continue
        out.append(
            {
                "row": record["row"],
                "face": record["face"],
                "gamma": record["gamma"],
                "prefix": record["prefix"],
                "mode": record["mode"],
                "compressed_dimension": record["compressed_dimension"],
                "rotation_gaps": record["rotation_gap_check"]["primitive_sizes"],
                "jump_classes": record["jump_class_check"]["primitive_sizes"],
                "per_rotation_gap_classes": record["jump_class_check"][
                    "per_rotation_gap_classes"
                ],
            }
        )
        if len(out) >= limit:
            break
    return out


def pct(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "0.00%"
    return f"{100.0 * numerator / denominator:.2f}%"


def render_float(value: float) -> str:
    return f"{value:.7g}"


def render_report(payload: dict[str, Any]) -> str:
    config = payload["config"]
    summary = payload["summary"]
    lines = [
        "# Three-Gap Compression Safety Audit",
        "",
        "This audit tests which current-level compressions preserve the",
        "PSL-boundary three-gap grammar.  The positive theorem-safe class is",
        "eta-diagonal compression.  The lossy conductor modes are falsifiers:",
        "they show what a Hayes-Mobius quotient must not do without adding a",
        "correction term.",
        "",
        "## Config",
        "",
        f"- `rows`: `{config['rows']}`",
        f"- `min_face_omega`: `{config['min_face_omega']}`",
        f"- `prefix_fractions`: `{config['prefix_fractions']}`",
        f"- `max_generators_per_face`: `{config['max_generators_per_face']}`",
        f"- `modes`: `{config['modes']}`",
        f"- `tolerance`: `{config['tolerance']}`",
        "",
        "## By Compression Mode",
        "",
        "| mode | records | support | jump lift | jump count | zero obs | max dim | max jump classes |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for mode, item in summary["by_mode"].items():
        lines.append(
            "| {mode} | {records} | {support} | {lift} | {count} | {zero} | {dim} | {classes} |".format(
                mode=mode,
                records=item["records"],
                support=f"{item['support_ok']}/{item['records']}",
                lift=f"{item['jump_lift_ok']}/{item['records']}",
                count=f"{item['jump_count_ok']}/{item['records']}",
                zero=item["zero_observable"],
                dim=item["max_compressed_dimension"],
                classes=item["max_jump_class_count"],
            )
        )
    lines += [
        "",
        "## First Unsafe-Compression Falsifiers",
        "",
    ]
    failures = summary["first_failures"]
    if not failures:
        lines += ["No jump-lift or jump-count failures in this run.", ""]
    else:
        lines += [
            "| row | face | gamma | prefix | mode | dim | rotation gaps | jump classes |",
            "|---:|---:|---:|---:|---|---:|---|---|",
        ]
        for failure in failures:
            lines.append(
                "| {row} | {face} | {gamma} | {prefix} | {mode} | {dim} | {rot} | {jump} |".format(
                    row=failure["row"],
                    face=failure["face"],
                    gamma=failure["gamma"],
                    prefix=failure["prefix"],
                    mode=failure["mode"],
                    dim=failure["compressed_dimension"],
                    rot=failure["rotation_gaps"],
                    jump=[render_float(value) for value in failure["jump_classes"]],
                )
            )
        lines.append("")
    lines += [
        "## Reading",
        "",
        "Eta-diagonal compression preserves the three-gap jump grammar because",
        "the compressed squared jump norm is a weighted sum of independent",
        "character terms indexed by `eta`; each term depends only on the",
        "adjacent rotation difference.  Conductor-only compression mixes",
        "different character phases into the same coordinate.  Then the norm",
        "can depend on the starting point as well as the gap, which is exactly",
        "the failure mode recorded above.",
        "",
        "The Paper 22 bridge is now sharper: prove the Hayes-Mobius leakage",
        "quotient is eta-diagonal after the functorial split/flat quotient, or",
        "is eta-diagonal plus a controlled correction whose gap-price is",
        "accounted for separately.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default=DEFAULT_ROWS)
    parser.add_argument("--min-face-omega", type=int, default=2)
    parser.add_argument("--prefix-fractions", default=DEFAULT_PREFIX_FRACTIONS)
    parser.add_argument("--modes", default=DEFAULT_MODES)
    parser.add_argument("--max-generators-per-face", type=int, default=0)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for mode, item in payload["summary"]["by_mode"].items():
        print(
            "{mode}: jump_lift={lift}/{records}, jump_count={count}/{records}".format(
                mode=mode,
                lift=item["jump_lift_ok"],
                count=item["jump_count_ok"],
                records=item["records"],
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
