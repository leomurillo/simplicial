"""Audit PSL-boundary carry phases on squarefree CRT cyclic faces.

This is the second Paper 25 three-gap diagnostic.  The previous
``three_gap_carry_audit.py`` deliberately used raw integer-addition carry and
found many falsifiers.  This script replaces that toy scalar with a
character-level PSL-boundary carry observable.

For R = Z/nZ and a primitive cyclic face x_j = j * gamma, the edge
displacement has Fourier coefficient

    Delta_hat_j(eta) = chi_eta(x_j + gamma) - chi_eta(x_j).

For a PSL cover boundary e < ep inside a CRT face, the carry operator has
entries indexed by a in X_e and b in X_ep with eta = b - a.  This audit keeps
only non-split entries, i.e. eta with support on at least two prime axes, and
then removes flat constants by centering the resulting vector sequence over
the tested prefix.

The key point is structural: after split-coordinate deletion, the observable
is still a finite character vector L(x_j).  Therefore phase-ordered jump
norms are functions of the adjacent rotation gap, not arbitrary high-rank
noise.  The audit checks that support gaps obey the classical three-gap law
and that PSL jump classes are lifted from the primitive rotation-gap classes.
It does not claim that the full conductor/CRT carry law is proved.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Any, Iterable

import numpy as np


DEFAULT_JSON = Path("empirical/reports/three_gap_psl_boundary_audit.json")
DEFAULT_REPORT = Path("empirical/reports/three_gap_psl_boundary_audit.md")
DEFAULT_ROWS = "6,10,15,30,210"
DEFAULT_PREFIX_FRACTIONS = "1/3,1/2,2/3,1"


@dataclass(frozen=True)
class GapCheck:
    primitive_count: int
    primitive_sizes: list[str]
    largest_sum_relation: bool | None
    three_gap_ok: bool


def parse_int_csv(text: str) -> list[int]:
    return [int(item.strip()) for item in text.split(",") if item.strip()]


def parse_fraction_csv(text: str) -> list[Fraction]:
    return [Fraction(item.strip()) for item in text.split(",") if item.strip()]


def prime_factors(n: int) -> tuple[int, ...]:
    out: list[int] = []
    value = n
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            out.append(factor)
            while value % factor == 0:
                value //= factor
        factor += 1 if factor == 2 else 2
    if value > 1:
        out.append(value)
    return tuple(out)


def omega(n: int) -> int:
    return len(prime_factors(n))


def is_squarefree(n: int) -> bool:
    return all(n % (p * p) != 0 for p in prime_factors(n))


def product_int(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def divisors_from_primes(primes: tuple[int, ...], min_omega: int) -> list[int]:
    out: list[int] = []
    for size in range(min_omega, len(primes) + 1):
        for subset in combinations(primes, size):
            out.append(product_int(subset))
    return sorted(out, key=lambda d: (omega(d), d))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conductor(label: int, n: int) -> int:
    label %= n
    if label == 0:
        return 1
    return n // math.gcd(label, n)


def packet_labels(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {d: [] for d in divisors(n) if d > 1}
    for label in range(1, n):
        packets[conductor(label, n)].append(label)
    return {d: labels for d, labels in packets.items() if labels}


def crt_from_residues(residues: dict[int, int], n: int) -> int:
    total = 0
    for p, residue in residues.items():
        modulus_part = n // p
        inverse = pow(modulus_part, -1, p)
        total += residue * modulus_part * inverse
    return total % n


def primitive_generators(n: int, face_primes: tuple[int, ...]) -> list[dict[str, Any]]:
    all_primes = prime_factors(n)
    out: list[dict[str, Any]] = []
    for local_values in product(*[range(1, p) for p in face_primes]):
        residues = {p: 0 for p in all_primes}
        residues.update({p: value for p, value in zip(face_primes, local_values)})
        gamma = crt_from_residues(residues, n)
        out.append(
            {
                "gamma": gamma,
                "local_residues": {str(p): residues[p] for p in all_primes},
            }
        )
    return out


def prefix_lengths(order: int, fractions: list[Fraction]) -> list[int]:
    lengths = {order}
    if order >= 2:
        lengths.add(2)
    if order >= 3:
        lengths.add(3)
    for frac in fractions:
        lengths.add(max(2, min(order, math.ceil(order * frac.numerator / frac.denominator))))
    return sorted(lengths)


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def cyclic_gaps(points: list[Fraction]) -> list[Fraction]:
    unique = sorted(set(points))
    if len(unique) <= 1:
        return []
    gaps = [unique[i + 1] - unique[i] for i in range(len(unique) - 1)]
    gaps.append(Fraction(1, 1) + unique[0] - unique[-1])
    return gaps


def check_fraction_gaps(gaps: list[Fraction]) -> GapCheck:
    primitive = sorted({gap for gap in gaps if gap > 0})
    relation: bool | None = None
    if len(primitive) == 3:
        relation = primitive[2] == primitive[0] + primitive[1]
    return GapCheck(
        primitive_count=len(primitive),
        primitive_sizes=[format_fraction(value) for value in primitive],
        largest_sum_relation=relation,
        three_gap_ok=len(primitive) <= 3 and relation is not False,
    )


def float_classes(values: list[float], tolerance: float) -> list[float]:
    positive = sorted(value for value in values if value > tolerance)
    classes: list[float] = []
    for value in positive:
        if not classes or abs(value - classes[-1]) > tolerance:
            classes.append(value)
    return classes


def check_float_three_gap(values: list[float], tolerance: float) -> dict[str, Any]:
    classes = float_classes(values, tolerance)
    relation: bool | None = None
    if len(classes) == 3:
        relation = abs(classes[2] - classes[0] - classes[1]) <= 20 * tolerance
    return {
        "primitive_count": len(classes),
        "primitive_sizes": [float(value) for value in classes],
        "largest_sum_relation": relation,
        "three_gap_ok": len(classes) <= 3 and relation is not False,
    }


def cover_boundaries(face: int) -> list[tuple[int, int]]:
    face_primes = prime_factors(face)
    active = [d for d in divisors(face) if d > 1]
    boundaries: list[tuple[int, int]] = []
    for src in active:
        for p in face_primes:
            if src % p != 0:
                tgt = src * p
                if tgt <= face and face % tgt == 0:
                    boundaries.append((src, tgt))
                    boundaries.append((tgt, src))
    return boundaries


def non_split_boundary_etas(n: int, face: int) -> list[dict[str, int]]:
    packets = packet_labels(n)
    entries: list[dict[str, int]] = []
    seen: set[tuple[int, int, int, int, int]] = set()
    for src, tgt in cover_boundaries(face):
        for a in packets[src]:
            for b in packets[tgt]:
                eta = (b - a) % n
                eta_conductor = conductor(eta, n)
                if omega(eta_conductor) < 2:
                    continue
                key = (src, tgt, a, b, eta)
                if key in seen:
                    continue
                seen.add(key)
                entries.append(
                    {
                        "src": src,
                        "tgt": tgt,
                        "src_label": a,
                        "tgt_label": b,
                        "eta": eta,
                        "eta_conductor": eta_conductor,
                    }
                )
    return entries


def psl_observable_matrix(
    *,
    n: int,
    gamma: int,
    prefix: int,
    entries: list[dict[str, int]],
) -> np.ndarray:
    if not entries:
        return np.zeros((prefix, 0), dtype=np.complex128)
    x_values = np.array([(j * gamma) % n for j in range(prefix)], dtype=float)
    etas = np.array([entry["eta"] for entry in entries], dtype=float)
    step = np.exp(2j * np.pi * etas * gamma / n) - 1.0
    phase = np.exp(2j * np.pi * np.outer(x_values, etas) / n)
    matrix = phase * step[None, :]
    return matrix - matrix.mean(axis=0, keepdims=True)


def audit_record(
    *,
    n: int,
    face: int,
    gamma: int,
    local_residues: dict[str, int],
    prefix: int,
    tolerance: float,
) -> dict[str, Any]:
    points = [Fraction((j * gamma) % n, n) for j in range(prefix)]
    rotation = check_fraction_gaps(cyclic_gaps(points))
    entries = non_split_boundary_etas(n, face)
    matrix = psl_observable_matrix(n=n, gamma=gamma, prefix=prefix, entries=entries)
    norms = np.linalg.norm(matrix, axis=1) if matrix.shape[1] else np.zeros(prefix)
    support = [j for j, value in enumerate(norms) if value > tolerance]
    support_points = [Fraction((j * gamma) % n, n) for j in support]
    support_check = check_fraction_gaps(cyclic_gaps(support_points))

    ordered = sorted(range(prefix), key=lambda j: Fraction((j * gamma) % n, n))
    jump_norms: list[float] = []
    jump_by_gap: dict[str, list[float]] = defaultdict(list)
    for index, current in enumerate(ordered):
        following = ordered[(index + 1) % len(ordered)]
        gap = (Fraction((following * gamma) % n, n) - Fraction((current * gamma) % n, n)) % 1
        value = float(np.linalg.norm(matrix[following] - matrix[current]))
        jump_norms.append(value)
        jump_by_gap[format_fraction(gap)].append(value)

    jump_classes = float_classes(jump_norms, tolerance)
    per_gap_classes = {
        gap: [float(value) for value in float_classes(values, tolerance)]
        for gap, values in sorted(jump_by_gap.items(), key=lambda item: Fraction(item[0]))
    }
    lift_ok = all(len(classes) <= 1 for classes in per_gap_classes.values())
    jump_count_ok = len(jump_classes) <= rotation.primitive_count
    jump_additive = check_float_three_gap(jump_norms, tolerance)

    eta_conductors = sorted({entry["eta_conductor"] for entry in entries})
    return {
        "row": n,
        "face": face,
        "gamma": gamma,
        "local_residues": local_residues,
        "prefix": prefix,
        "entry_count": len(entries),
        "eta_conductors": eta_conductors,
        "rotation_gap_check": rotation.__dict__,
        "support_gap_check": support_check.__dict__,
        "jump_class_check": {
            "primitive_count": len(jump_classes),
            "primitive_sizes": [float(value) for value in jump_classes],
            "classes_lift_from_rotation_gaps": lift_ok,
            "class_count_at_most_rotation_count": jump_count_ok,
            "per_rotation_gap_classes": per_gap_classes,
        },
        "jump_additive_check": jump_additive,
        "checks": {
            "rotation_three_gap_ok": rotation.three_gap_ok,
            "support_three_gap_ok": support_check.three_gap_ok,
            "jump_lift_ok": lift_ok,
            "jump_count_ok": jump_count_ok,
        },
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    fractions = parse_fraction_csv(args.prefix_fractions)
    records: list[dict[str, Any]] = []
    for n in rows:
        if not is_squarefree(n):
            raise ValueError(f"row {n} is not squarefree")
        primes = prime_factors(n)
        for face in divisors_from_primes(primes, args.min_face_omega):
            face_primes = prime_factors(face)
            generators = primitive_generators(n, face_primes)
            if args.max_generators_per_face > 0:
                generators = generators[: args.max_generators_per_face]
            for generator in generators:
                for prefix in prefix_lengths(face, fractions):
                    records.append(
                        audit_record(
                            n=n,
                            face=face,
                            gamma=generator["gamma"],
                            local_residues=generator["local_residues"],
                            prefix=prefix,
                            tolerance=args.tolerance,
                        )
                    )
    return {
        "config": {
            "rows": rows,
            "min_face_omega": args.min_face_omega,
            "prefix_fractions": [str(frac) for frac in fractions],
            "max_generators_per_face": args.max_generators_per_face,
            "tolerance": args.tolerance,
            "observable": (
                "non-split PSL cover-boundary edge Fourier coefficients, "
                "centered modulo flat constants"
            ),
            "claim_hygiene": (
                "support and jump-class lift are finite character-vector facts; "
                "the full conductor/CRT carry law remains a target"
            ),
        },
        "summary": summarize(records),
        "records": records,
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_row: dict[int, list[dict[str, Any]]] = defaultdict(list)
    by_face: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_row[record["row"]].append(record)
        by_face[(record["row"], record["face"])].append(record)

    def aggregate(items: list[dict[str, Any]]) -> dict[str, Any]:
        count = len(items)
        return {
            "records": count,
            "rotation_ok": sum(item["checks"]["rotation_three_gap_ok"] for item in items),
            "support_ok": sum(item["checks"]["support_three_gap_ok"] for item in items),
            "jump_lift_ok": sum(item["checks"]["jump_lift_ok"] for item in items),
            "jump_count_ok": sum(item["checks"]["jump_count_ok"] for item in items),
            "jump_additive_ok": sum(
                item["jump_additive_check"]["three_gap_ok"] for item in items
            ),
            "max_entries": max((item["entry_count"] for item in items), default=0),
            "max_rotation_gap_count": max(
                (item["rotation_gap_check"]["primitive_count"] for item in items),
                default=0,
            ),
            "max_support_gap_count": max(
                (item["support_gap_check"]["primitive_count"] for item in items),
                default=0,
            ),
            "max_jump_class_count": max(
                (item["jump_class_check"]["primitive_count"] for item in items),
                default=0,
            ),
            "max_jump_additive_gap_count": max(
                (item["jump_additive_check"]["primitive_count"] for item in items),
                default=0,
            ),
        }

    return {
        "records": len(records),
        "all": aggregate(records),
        "by_row": {str(row): aggregate(items) for row, items in sorted(by_row.items())},
        "by_face": {
            f"{row}:{face}": aggregate(items)
            for (row, face), items in sorted(by_face.items())
        },
        "first_failures": first_failures(records),
    }


def first_failures(records: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for record in records:
        if (
            record["checks"]["support_three_gap_ok"]
            and record["checks"]["jump_lift_ok"]
            and record["checks"]["jump_count_ok"]
        ):
            continue
        out.append(
            {
                "row": record["row"],
                "face": record["face"],
                "gamma": record["gamma"],
                "prefix": record["prefix"],
                "entry_count": record["entry_count"],
                "rotation": record["rotation_gap_check"],
                "support": record["support_gap_check"],
                "jump": record["jump_class_check"],
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
    aggregate = summary["all"]
    lines = [
        "# Three-Gap PSL-Boundary Audit",
        "",
        "This is the second Paper 25 three-gap diagnostic.  It replaces the",
        "raw integer carry from `three_gap_carry_audit.py` with a non-split",
        "PSL cover-boundary character observable.  The result is a finite",
        "character-vector rigidity check, not a proof of the full conductor/CRT",
        "carry law.",
        "",
        "## Config",
        "",
        f"- `rows`: `{config['rows']}`",
        f"- `min_face_omega`: `{config['min_face_omega']}`",
        f"- `prefix_fractions`: `{config['prefix_fractions']}`",
        f"- `max_generators_per_face`: `{config['max_generators_per_face']}`",
        f"- `tolerance`: `{config['tolerance']}`",
        f"- `observable`: `{config['observable']}`",
        "",
        "## Aggregate",
        "",
        "| check | pass | total | rate | max primitive classes | failures |",
        "|---|---:|---:|---:|---:|---:|",
        "| rotation shadow | {ok} | {total} | {rate} | {maxc} | {fail} |".format(
            ok=aggregate["rotation_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["rotation_ok"], aggregate["records"]),
            maxc=aggregate["max_rotation_gap_count"],
            fail=aggregate["records"] - aggregate["rotation_ok"],
        ),
        "| PSL support gaps | {ok} | {total} | {rate} | {maxc} | {fail} |".format(
            ok=aggregate["support_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["support_ok"], aggregate["records"]),
            maxc=aggregate["max_support_gap_count"],
            fail=aggregate["records"] - aggregate["support_ok"],
        ),
        "| PSL jump classes lift from rotation gaps | {ok} | {total} | {rate} | {maxc} | {fail} |".format(
            ok=aggregate["jump_lift_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["jump_lift_ok"], aggregate["records"]),
            maxc=aggregate["max_jump_class_count"],
            fail=aggregate["records"] - aggregate["jump_lift_ok"],
        ),
        "| PSL jump class count <= rotation count | {ok} | {total} | {rate} | {maxc} | {fail} |".format(
            ok=aggregate["jump_count_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["jump_count_ok"], aggregate["records"]),
            maxc=aggregate["max_jump_class_count"],
            fail=aggregate["records"] - aggregate["jump_count_ok"],
        ),
        "| PSL jump additive three-gap law | {ok} | {total} | {rate} | {maxc} | {fail} |".format(
            ok=aggregate["jump_additive_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["jump_additive_ok"], aggregate["records"]),
            maxc=aggregate["max_jump_additive_gap_count"],
            fail=aggregate["records"] - aggregate["jump_additive_ok"],
        ),
        "",
        "The first four rows are the intended finite rigidity checks.  The",
        "last row is intentionally stronger: it asks the nonlinear jump norms",
        "themselves to satisfy the additive largest=sum law.  That stronger",
        "amplitude statement is not expected from the classical theorem.",
        "",
        "## By Row",
        "",
        "| row | records | support | jump lift | jump count | additive jumps | max entries |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row, item in summary["by_row"].items():
        lines.append(
            "| {row} | {records} | {support} | {lift} | {count} | {add} | {entries} |".format(
                row=row,
                records=item["records"],
                support=f"{item['support_ok']}/{item['records']}",
                lift=f"{item['jump_lift_ok']}/{item['records']}",
                count=f"{item['jump_count_ok']}/{item['records']}",
                add=f"{item['jump_additive_ok']}/{item['records']}",
                entries=item["max_entries"],
            )
        )
    lines += [
        "",
        "## By Face",
        "",
        "| row:face | records | support | jump lift | jump count | additive jumps | max jump classes | max entries |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for face, item in summary["by_face"].items():
        lines.append(
            "| {face} | {records} | {support} | {lift} | {count} | {add} | {jmax} | {entries} |".format(
                face=face,
                records=item["records"],
                support=f"{item['support_ok']}/{item['records']}",
                lift=f"{item['jump_lift_ok']}/{item['records']}",
                count=f"{item['jump_count_ok']}/{item['records']}",
                add=f"{item['jump_additive_ok']}/{item['records']}",
                jmax=item["max_jump_class_count"],
                entries=item["max_entries"],
            )
        )
    lines += [
        "",
        "## First Rigidity Failures",
        "",
    ]
    failures = summary["first_failures"]
    if not failures:
        lines += [
            "No failures for support gaps, jump lift, or jump class-count checks.",
            "",
        ]
    else:
        lines += [
            "| row | face | gamma | prefix | entries | rotation gaps | support gaps | jump classes |",
            "|---:|---:|---:|---:|---:|---|---|---|",
        ]
        for failure in failures:
            lines.append(
                "| {row} | {face} | {gamma} | {prefix} | {entries} | {rot} | {sup} | {jump} |".format(
                    row=failure["row"],
                    face=failure["face"],
                    gamma=failure["gamma"],
                    prefix=failure["prefix"],
                    entries=failure["entry_count"],
                    rot=failure["rotation"]["primitive_sizes"],
                    sup=failure["support"]["primitive_sizes"],
                    jump=[render_float(v) for v in failure["jump"]["primitive_sizes"]],
                )
            )
        lines.append("")
    lines += [
        "## Reading",
        "",
        "The raw integer carry audit failed because integer carry is not the",
        "filtered conductor observable.  This PSL-boundary audit keeps the",
        "character-translation structure.  After deleting split prime-axis",
        "entries and centering flat constants, support gaps and jump classes",
        "are controlled by the same primitive rotation-gap classes on every",
        "tested cyclic face.",
        "",
        "This supports a precise next theorem: finite character-vector PSL",
        "carry phases have a three-gap support grammar and a jump-class grammar",
        "lifted from the rotation gaps.  It still does not prove that the",
        "current-level Hayes-Mobius leakage quotient is exactly this vector",
        "observable, nor that projective CRT products preserve the grammar.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default=DEFAULT_ROWS)
    parser.add_argument("--min-face-omega", type=int, default=2)
    parser.add_argument("--prefix-fractions", default=DEFAULT_PREFIX_FRACTIONS)
    parser.add_argument(
        "--max-generators-per-face",
        type=int,
        default=0,
        help="0 means all primitive CRT generators on each face.",
    )
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    aggregate = payload["summary"]["all"]
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    print(
        "records={records} support={support}/{records} jump_lift={lift}/{records} "
        "jump_count={count}/{records}".format(
            records=aggregate["records"],
            support=aggregate["support_ok"],
            lift=aggregate["jump_lift_ok"],
            count=aggregate["jump_count_ok"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
