"""Audit a three-gap carry grammar on squarefree CRT cyclic faces.

This is a Paper 25 diagnostic, not a proof of a conductor/CRT carry law.

For a squarefree row R = Z/nZ, a CRT divisor face is obtained by fixing the
coordinates outside a squarefree divisor d and varying the coordinates over
the primes p | d.  A primitive one-generator cyclic face is the orbit

    x_j = j * gamma  (mod n),  j = 0, ..., ord(gamma)-1,

where gamma has nonzero CRT coordinate at every p | d and zero coordinate at
every p not dividing d.  The rotation shadow sorts the prefix
{x_j / n : 0 <= j < M}; the classical three-gap theorem applies to this
finite rational rotation after repeated points are quotiented.

The conductor-specific test here is intentionally narrower and falsifiable.
For the same prefix, we measure the global integer carry of adding gamma,

    C_n(j) = floor((rep(x_j) + rep(gamma)) / n),

and quotient split/flat terms by projecting away from the span of the constant
vector and the local prime-axis carries

    C_p(j) = floor((x_j mod p + gamma mod p) / p),  p | d.

The residual is a toy non-split carry observable.  The audit sorts residual
support and residual jumps by the same circle order and checks whether the
primitive adjacent gap sizes are bounded by three, with largest = sum of the
two smaller in the genuine three-gap regime.

Failures should be read as falsifiers of this raw carry observable, not of the
larger target principle.  The manuscript-facing question is whether the actual
PSL-boundary/Hayes-Mobius leakage observable, after split and flat quotienting,
is a rotation cocycle with the same low-complexity gap grammar.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Any, Iterable

import numpy as np


DEFAULT_JSON = Path("empirical/reports/three_gap_carry_audit.json")
DEFAULT_REPORT = Path("empirical/reports/three_gap_carry_audit.md")
DEFAULT_ROWS = "6,10,15,30,210"
DEFAULT_PREFIX_FRACTIONS = "1/3,1/2,2/3,1"


@dataclass(frozen=True)
class PrimitiveGapCheck:
    primitive_count: int
    primitive_sizes: list[str]
    largest_sum_relation: bool | None
    three_gap_ok: bool


def parse_int_csv(text: str) -> list[int]:
    return [int(item.strip()) for item in text.split(",") if item.strip()]


def parse_fraction_csv(text: str) -> list[Fraction]:
    out: list[Fraction] = []
    for item in text.split(","):
        item = item.strip()
        if not item:
            continue
        out.append(Fraction(item))
    return out


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


def is_squarefree(n: int) -> bool:
    return all(n % (p * p) != 0 for p in prime_factors(n))


def omega(n: int) -> int:
    return len(prime_factors(n))


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


def crt_from_residues(residues: dict[int, int], n: int) -> int:
    total = 0
    for p, residue in residues.items():
        modulus_part = n // p
        inverse = pow(modulus_part, -1, p)
        total += residue * modulus_part * inverse
    return total % n


def primitive_generators_for_face(n: int, face_primes: tuple[int, ...]) -> list[dict[str, Any]]:
    all_primes = prime_factors(n)
    generators: list[dict[str, Any]] = []
    local_ranges = [range(1, p) for p in face_primes]
    for local_values in product(*local_ranges):
        residues = {p: 0 for p in all_primes}
        residues.update({p: value for p, value in zip(face_primes, local_values)})
        gamma = crt_from_residues(residues, n)
        generators.append(
            {
                "gamma": gamma,
                "local_residues": {str(p): residues[p] for p in all_primes},
            }
        )
    return generators


def prefix_lengths(order: int, fractions: list[Fraction]) -> list[int]:
    lengths = {order}
    if order >= 2:
        lengths.add(2)
    if order >= 3:
        lengths.add(3)
    for frac in fractions:
        value = math.ceil(order * frac.numerator / frac.denominator)
        value = max(2, min(order, value))
        lengths.add(value)
    return sorted(lengths)


def circle_points(n: int, gamma: int, prefix: int) -> list[Fraction]:
    return [Fraction((j * gamma) % n, n) for j in range(prefix)]


def cyclic_gaps(points: list[Fraction]) -> list[Fraction]:
    unique = sorted(set(points))
    if len(unique) <= 1:
        return []
    gaps = [unique[i + 1] - unique[i] for i in range(len(unique) - 1)]
    gaps.append(Fraction(1, 1) + unique[0] - unique[-1])
    return gaps


def check_fraction_gaps(gaps: list[Fraction]) -> PrimitiveGapCheck:
    positive = sorted({gap for gap in gaps if gap > 0})
    relation: bool | None = None
    if len(positive) == 3:
        relation = positive[2] == positive[0] + positive[1]
    ok = len(positive) <= 3 and (relation is not False)
    return PrimitiveGapCheck(
        primitive_count=len(positive),
        primitive_sizes=[format_fraction(value) for value in positive],
        largest_sum_relation=relation,
        three_gap_ok=ok,
    )


def check_float_gaps(values: list[float], tolerance: float) -> dict[str, Any]:
    positive = sorted(value for value in values if value > tolerance)
    primitive: list[float] = []
    for value in positive:
        if not primitive or abs(value - primitive[-1]) > tolerance:
            primitive.append(value)
    relation: bool | None = None
    if len(primitive) == 3:
        relation = abs(primitive[2] - primitive[0] - primitive[1]) <= 10 * tolerance
    return {
        "primitive_count": len(primitive),
        "primitive_sizes": [float(value) for value in primitive],
        "largest_sum_relation": relation,
        "three_gap_ok": len(primitive) <= 3 and relation is not False,
    }


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def split_quotient_residual(
    *,
    n: int,
    gamma: int,
    face_primes: tuple[int, ...],
    prefix: int,
    tolerance: float,
) -> dict[str, Any]:
    x_values = np.array([(j * gamma) % n for j in range(prefix)], dtype=float)
    global_carry = np.floor((x_values + gamma) / n)
    columns = [np.ones(prefix, dtype=float)]
    local_carries: dict[str, list[int]] = {}
    for p in face_primes:
        gamma_p = gamma % p
        carry = np.floor(((x_values % p) + gamma_p) / p)
        columns.append(carry)
        local_carries[str(p)] = [int(value) for value in carry]
    design = np.column_stack(columns)
    projection, *_ = np.linalg.lstsq(design, global_carry, rcond=None)
    fitted = design @ projection
    residual = global_carry - fitted
    residual_norm = float(np.linalg.norm(residual))
    support = [int(i) for i, value in enumerate(residual) if abs(value) > tolerance]

    ordered_indices = sorted(range(prefix), key=lambda j: Fraction((j * gamma) % n, n))
    jump_values: list[float] = []
    for i, current in enumerate(ordered_indices):
        following = ordered_indices[(i + 1) % len(ordered_indices)]
        jump_values.append(abs(float(residual[following] - residual[current])))

    support_points = [Fraction((j * gamma) % n, n) for j in support]
    support_gap_check = check_fraction_gaps(cyclic_gaps(support_points))
    jump_gap_check = check_float_gaps(jump_values, tolerance)
    value_gap_check = check_float_gaps(
        [
            b - a
            for a, b in zip(
                sorted(float(value) for value in residual),
                sorted(float(value) for value in residual)[1:],
            )
        ],
        tolerance,
    )

    rank = int(np.linalg.matrix_rank(design, tol=tolerance))
    return {
        "global_carry": [int(value) for value in global_carry],
        "local_carries": local_carries,
        "split_coefficients": [float(value) for value in projection],
        "split_rank": rank,
        "residual_norm": residual_norm,
        "residual_support_count": len(support),
        "residual_support_indices": support[:20],
        "residual_min": float(np.min(residual)) if len(residual) else 0.0,
        "residual_max": float(np.max(residual)) if len(residual) else 0.0,
        "support_gap_check": support_gap_check.__dict__,
        "jump_gap_check": jump_gap_check,
        "value_gap_check": value_gap_check,
    }


def run_audit(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    fractions = parse_fraction_csv(args.prefix_fractions)
    records: list[dict[str, Any]] = []
    for n in rows:
        if not is_squarefree(n):
            raise ValueError(f"row {n} is not squarefree")
        primes = prime_factors(n)
        for d in divisors_from_primes(primes, args.min_face_omega):
            face_primes = prime_factors(d)
            generators = primitive_generators_for_face(n, face_primes)
            if args.max_generators_per_face > 0:
                generators = generators[: args.max_generators_per_face]
            for generator in generators:
                gamma = int(generator["gamma"])
                order = d
                for prefix in prefix_lengths(order, fractions):
                    points = circle_points(n, gamma, prefix)
                    rotation_check = check_fraction_gaps(cyclic_gaps(points))
                    residual = split_quotient_residual(
                        n=n,
                        gamma=gamma,
                        face_primes=face_primes,
                        prefix=prefix,
                        tolerance=args.tolerance,
                    )
                    records.append(
                        {
                            "row": n,
                            "face": d,
                            "face_primes": list(face_primes),
                            "gamma": gamma,
                            "local_residues": generator["local_residues"],
                            "order": order,
                            "prefix": prefix,
                            "rotation_gap_check": rotation_check.__dict__,
                            "raw_carry_residual": residual,
                            "checks": {
                                "rotation_three_gap_ok": rotation_check.three_gap_ok,
                                "residual_support_three_gap_ok": residual[
                                    "support_gap_check"
                                ]["three_gap_ok"],
                                "residual_jump_three_gap_ok": residual[
                                    "jump_gap_check"
                                ]["three_gap_ok"],
                                "residual_value_three_gap_ok": residual[
                                    "value_gap_check"
                                ]["three_gap_ok"],
                            },
                        }
                    )
    summary = summarize(records)
    return {
        "config": {
            "rows": rows,
            "min_face_omega": args.min_face_omega,
            "prefix_fractions": [str(frac) for frac in fractions],
            "max_generators_per_face": args.max_generators_per_face,
            "tolerance": args.tolerance,
            "observable": "raw global-addition carry residual after constant/local-carry quotient",
            "claim_hygiene": (
                "rotation gaps are classical three-gap shadows; residual carry "
                "checks are conductor/CRT diagnostics only"
            ),
        },
        "summary": summary,
        "records": records,
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_row: dict[int, list[dict[str, Any]]] = {}
    by_face: dict[tuple[int, int], list[dict[str, Any]]] = {}
    for record in records:
        by_row.setdefault(record["row"], []).append(record)
        by_face.setdefault((record["row"], record["face"]), []).append(record)

    def aggregate(items: list[dict[str, Any]]) -> dict[str, Any]:
        count = len(items)
        support_failures = [
            item for item in items if not item["checks"]["residual_support_three_gap_ok"]
        ]
        jump_failures = [
            item for item in items if not item["checks"]["residual_jump_three_gap_ok"]
        ]
        value_failures = [
            item for item in items if not item["checks"]["residual_value_three_gap_ok"]
        ]
        nonflat = [
            item
            for item in items
            if item["raw_carry_residual"]["residual_norm"] > 1e-10
        ]
        return {
            "records": count,
            "rotation_ok": sum(
                1 for item in items if item["checks"]["rotation_three_gap_ok"]
            ),
            "support_ok": count - len(support_failures),
            "jump_ok": count - len(jump_failures),
            "value_ok": count - len(value_failures),
            "support_failures": len(support_failures),
            "jump_failures": len(jump_failures),
            "value_failures": len(value_failures),
            "nonflat_residuals": len(nonflat),
            "max_support_primitive_count": max(
                (
                    item["raw_carry_residual"]["support_gap_check"]["primitive_count"]
                    for item in items
                ),
                default=0,
            ),
            "max_jump_primitive_count": max(
                (
                    item["raw_carry_residual"]["jump_gap_check"]["primitive_count"]
                    for item in items
                ),
                default=0,
            ),
            "max_value_primitive_count": max(
                (
                    item["raw_carry_residual"]["value_gap_check"]["primitive_count"]
                    for item in items
                ),
                default=0,
            ),
            "max_residual_norm": max(
                (item["raw_carry_residual"]["residual_norm"] for item in items),
                default=0.0,
            ),
        }

    row_summary = {
        str(row): aggregate(items) for row, items in sorted(by_row.items())
    }
    face_summary = {
        f"{row}:{face}": aggregate(items)
        for (row, face), items in sorted(by_face.items())
    }
    return {
        "records": len(records),
        "all": aggregate(records),
        "by_row": row_summary,
        "by_face": face_summary,
        "first_support_failures": compact_failures(
            records, "residual_support_three_gap_ok"
        ),
        "first_jump_failures": compact_failures(
            records, "residual_jump_three_gap_ok"
        ),
        "first_value_failures": compact_failures(
            records, "residual_value_three_gap_ok"
        ),
    }


def compact_failures(records: list[dict[str, Any]], key: str, limit: int = 8) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for record in records:
        if record["checks"][key]:
            continue
        residual = record["raw_carry_residual"]
        out.append(
            {
                "row": record["row"],
                "face": record["face"],
                "gamma": record["gamma"],
                "prefix": record["prefix"],
                "local_residues": record["local_residues"],
                "residual_norm": residual["residual_norm"],
                "support_gap_check": residual["support_gap_check"],
                "jump_gap_check": residual["jump_gap_check"],
                "value_gap_check": residual["value_gap_check"],
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
        "# Three-Gap Carry Audit",
        "",
        "This is a diagnostic for Paper 25 Target Principle 1.1A, not a proof.",
        "The rotation-shadow column is the part controlled by the classical",
        "three-gap theorem.  The residual columns use a toy conductor observable:",
        "global integer-addition carry after quotienting the constant vector and",
        "the local prime-axis carry bits.  A failure there falsifies that raw",
        "observable, not the intended PSL-boundary/Hayes-Mobius carry law.",
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
        "| check | pass | total | rate | max primitive gaps | failures |",
        "|---|---:|---:|---:|---:|---:|",
        "| rotation shadow | {ok} | {total} | {rate} | <=3 | {fail} |".format(
            ok=aggregate["rotation_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["rotation_ok"], aggregate["records"]),
            fail=aggregate["records"] - aggregate["rotation_ok"],
        ),
        "| residual support gaps | {ok} | {total} | {rate} | {maxgap} | {fail} |".format(
            ok=aggregate["support_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["support_ok"], aggregate["records"]),
            maxgap=aggregate["max_support_primitive_count"],
            fail=aggregate["support_failures"],
        ),
        "| residual phase jumps | {ok} | {total} | {rate} | {maxgap} | {fail} |".format(
            ok=aggregate["jump_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["jump_ok"], aggregate["records"]),
            maxgap=aggregate["max_jump_primitive_count"],
            fail=aggregate["jump_failures"],
        ),
        "| residual value gaps | {ok} | {total} | {rate} | {maxgap} | {fail} |".format(
            ok=aggregate["value_ok"],
            total=aggregate["records"],
            rate=pct(aggregate["value_ok"], aggregate["records"]),
            maxgap=aggregate["max_value_primitive_count"],
            fail=aggregate["value_failures"],
        ),
        "",
        f"- nonflat residuals: `{aggregate['nonflat_residuals']}`",
        f"- max residual norm: `{render_float(aggregate['max_residual_norm'])}`",
        "",
        "## By Row",
        "",
        "| row | records | rotation | support | jumps | values | nonflat | max residual |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row, item in summary["by_row"].items():
        lines.append(
            "| {row} | {records} | {rot} | {support} | {jump} | {value} | {nonflat} | {resid} |".format(
                row=row,
                records=item["records"],
                rot=f"{item['rotation_ok']}/{item['records']}",
                support=f"{item['support_ok']}/{item['records']}",
                jump=f"{item['jump_ok']}/{item['records']}",
                value=f"{item['value_ok']}/{item['records']}",
                nonflat=item["nonflat_residuals"],
                resid=render_float(item["max_residual_norm"]),
            )
        )
    lines += [
        "",
        "## By Face",
        "",
        "| row:face | records | support | jumps | values | nonflat | max support gaps | max jump gaps | max value gaps |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for face, item in summary["by_face"].items():
        lines.append(
            "| {face} | {records} | {support} | {jump} | {value} | {nonflat} | {sgap} | {jgap} | {vgap} |".format(
                face=face,
                records=item["records"],
                support=f"{item['support_ok']}/{item['records']}",
                jump=f"{item['jump_ok']}/{item['records']}",
                value=f"{item['value_ok']}/{item['records']}",
                nonflat=item["nonflat_residuals"],
                sgap=item["max_support_primitive_count"],
                jgap=item["max_jump_primitive_count"],
                vgap=item["max_value_primitive_count"],
            )
        )
    lines += [
        "",
        "## First Falsifiers",
        "",
        "These are falsifiers for the raw global-addition residual observable.",
        "They say the actual theorem, if true, must use the filtered PSL-boundary",
        "or Hayes-Mobius leakage observable rather than this naive integer carry.",
        "",
    ]
    for label, failures in [
        ("Residual support gaps", summary["first_support_failures"]),
        ("Residual phase jumps", summary["first_jump_failures"]),
        ("Residual value gaps", summary["first_value_failures"]),
    ]:
        lines += [f"### {label}", ""]
        if not failures:
            lines += ["No failures in this run.", ""]
            continue
        lines += [
            "| row | face | gamma | prefix | residual norm | support gaps | jump gaps | value gaps |",
            "|---:|---:|---:|---:|---:|---|---|---|",
        ]
        for failure in failures:
            lines.append(
                "| {row} | {face} | {gamma} | {prefix} | {norm} | {support} | {jump} | {value} |".format(
                    row=failure["row"],
                    face=failure["face"],
                    gamma=failure["gamma"],
                    prefix=failure["prefix"],
                    norm=render_float(failure["residual_norm"]),
                    support=failure["support_gap_check"]["primitive_sizes"],
                    jump=[render_float(v) for v in failure["jump_gap_check"]["primitive_sizes"]],
                    value=[render_float(v) for v in failure["value_gap_check"]["primitive_sizes"]],
                )
            )
        lines.append("")
    lines += [
        "## Reading",
        "",
        "The rotation shadow passes because it is exactly the finite rational",
        "rotation case governed by the classical three-gap theorem.  That part",
        "does not prove any conductor/CRT carry law.",
        "",
        "The residual tests are the new diagnostic.  Passing rows identify",
        "places where the raw split-quotiented carry already has a small gap",
        "grammar.  Failing rows identify the extra structure still needed:",
        "the observable must be the non-split PSL-boundary/Hayes-Mobius leakage",
        "class after flat and split terms are killed, and the proof must show",
        "that this class is represented by a rotation or interval cocycle.",
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
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run_audit(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    aggregate = payload["summary"]["all"]
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    print(
        "records={records} rotation={rotation}/{records} support={support}/{records} "
        "jumps={jumps}/{records} values={values}/{records}".format(
            records=aggregate["records"],
            rotation=aggregate["rotation_ok"],
            support=aggregate["support_ok"],
            jumps=aggregate["jump_ok"],
            values=aggregate["value_ok"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
