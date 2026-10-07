"""Audit the projective leakage correction budget for Paper 25.

Theorem 3.20 decomposes every post-convolution leakage Gram form as

    G = G_diag + E,

where ``G_diag`` is the translation/Reynolds average in the output-character
basis and ``E`` is the off-diagonal correction.  Paper 22 projective closure
can use the three-gap grammar only for the diagonal part.  Any nonzero ``E``
must either vanish after split/flat quotienting or be paid for separately.

This audit estimates the finite correction coefficients on the squarefree
rows 6, 10, 15, 30, and 210.  It records full-row models, the same models
restricted to CRT divisor faces, and the normalized CRT face restrictions
themselves.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from three_gap_leakage_norm_decomposition import (
    DEFAULT_MODES,
    DEFAULT_ROWS,
    compression_matrix,
    gram_decomposition,
    label_support,
    non_split_labels,
    restriction_matrix,
)
from three_gap_psl_boundary_audit import (
    divisors_from_primes,
    is_squarefree,
    omega,
    parse_int_csv,
    prime_factors,
)


DEFAULT_JSON = Path("empirical/reports/projective_leakage_correction_budget.json")
DEFAULT_REPORT = Path("empirical/reports/projective_leakage_correction_budget.md")


def face_supported_labels(n: int, labels: list[int], face: int) -> list[int]:
    face_primes = set(prime_factors(face))
    return [label for label in labels if label_support(label, n) <= face_primes]


def enrich_record(
    *,
    item: dict[str, Any],
    row: int,
    mode: str,
    scope: str,
    face: int | None,
    source_label_count: int,
    coordinate_count: int,
) -> dict[str, Any]:
    item.update(
        {
            "row": row,
            "mode": mode,
            "scope": scope,
            "face": face,
            "face_omega": omega(face) if face else omega(row),
            "source_label_count": source_label_count,
            "coordinate_count": coordinate_count,
            "budget_coefficient": item["off_diagonal_operator_norm"],
        }
    )
    return item


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    modes = [item.strip() for item in args.modes.split(",") if item.strip()]
    records: list[dict[str, Any]] = []

    for row in rows:
        if not is_squarefree(row):
            raise ValueError(f"row {row} is not squarefree")

        row_labels = non_split_labels(row)
        for mode in modes:
            matrix, names = compression_matrix(row, row_labels, mode)
            records.append(
                enrich_record(
                    item=gram_decomposition(matrix, args.tolerance),
                    row=row,
                    mode=mode,
                    scope="full_row_model",
                    face=None,
                    source_label_count=len(row_labels),
                    coordinate_count=len(names),
                )
            )

        primes = prime_factors(row)
        for face in divisors_from_primes(primes, args.min_face_omega):
            face_labels = face_supported_labels(row, row_labels, face)

            restriction, restriction_names = restriction_matrix(row, row_labels, face)
            records.append(
                enrich_record(
                    item=gram_decomposition(restriction, args.tolerance),
                    row=row,
                    mode="crt_face_restriction",
                    scope="restriction_operator",
                    face=face,
                    source_label_count=len(row_labels),
                    coordinate_count=len(restriction_names),
                )
            )

            for mode in modes:
                matrix, names = compression_matrix(row, face_labels, mode)
                records.append(
                    enrich_record(
                        item=gram_decomposition(matrix, args.tolerance),
                        row=row,
                        mode=mode,
                        scope="face_model",
                        face=face,
                        source_label_count=len(face_labels),
                        coordinate_count=len(names),
                    )
                )

    return {
        "config": {
            "rows": rows,
            "modes": modes,
            "min_face_omega": args.min_face_omega,
            "tolerance": args.tolerance,
            "correction_budget": (
                "sum_k w_k ||E_{S,k}||_op ||J_{S,k}||^2, with the "
                "per-model coefficient recorded as budget_coefficient"
            ),
            "claim_hygiene": (
                "diagonal records are finite zeta-diagonal safety checks; "
                "unsafe records are falsifier/comparison models; Paper 22 "
                "projective closure still requires functorial restriction, "
                "lower semicontinuity, and correction-budget extinction"
            ),
        },
        "summary": summarize(records),
        "records": records,
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_scope_mode: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    by_row_mode: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    by_face_omega_mode: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    restrictions: list[dict[str, Any]] = []

    for record in records:
        by_scope_mode[(record["scope"], record["mode"])].append(record)
        if record["scope"] == "full_row_model":
            by_row_mode[(record["row"], record["mode"])].append(record)
        if record["scope"] == "face_model":
            by_face_omega_mode[(record["face_omega"], record["mode"])].append(record)
        if record["scope"] == "restriction_operator":
            restrictions.append(record)

    return {
        "by_scope_mode": {
            f"{scope}:{mode}": aggregate(items)
            for (scope, mode), items in sorted(by_scope_mode.items())
        },
        "full_row_models": {
            f"{row}:{mode}": aggregate(items)
            for (row, mode), items in sorted(by_row_mode.items())
        },
        "face_models_by_omega": {
            f"{face_omega}:{mode}": aggregate(items)
            for (face_omega, mode), items in sorted(by_face_omega_mode.items())
        },
        "restriction_operators": aggregate(restrictions),
        "unsafe_examples": [
            record
            for record in records
            if not record["is_zeta_diagonal_safe"]
        ][:16],
    }


def aggregate(items: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "records": len(items),
        "safe": sum(item["is_zeta_diagonal_safe"] for item in items),
        "max_source_labels": max((item["source_label_count"] for item in items), default=0),
        "max_coordinate_count": max((item["coordinate_count"] for item in items), default=0),
        "max_off_diagonal_operator_norm": max(
            (item["off_diagonal_operator_norm"] for item in items), default=0.0
        ),
        "max_relative_off_diagonal_operator_norm": max(
            (item["relative_off_diagonal_operator_norm"] for item in items), default=0.0
        ),
        "max_correction_rank": max((item["correction_rank"] for item in items), default=0),
    }


def render_float(value: float) -> str:
    return f"{value:.7g}"


def render_report(payload: dict[str, Any]) -> str:
    config = payload["config"]
    summary = payload["summary"]
    lines = [
        "# Projective Leakage Correction Budget",
        "",
        "This audit turns Theorem 3.20 into the finite correction-budget ledger",
        "needed for the Paper 22 projective-closure package.  The diagonal",
        "part of a leakage Gram form is three-gap safe; the off-diagonal",
        "correction is priced by its operator norm.",
        "",
        "## Config",
        "",
        f"- `rows`: `{config['rows']}`",
        f"- `modes`: `{config['modes']}`",
        f"- `min_face_omega`: `{config['min_face_omega']}`",
        f"- `tolerance`: `{config['tolerance']}`",
        "",
        "## Scope / Model Summary",
        "",
        "| scope:model | records | safe | max labels | max coordinates | max ||E||_op | max relative offdiag | max rank(E) |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, item in summary["by_scope_mode"].items():
        lines.append(summary_row(key, item))

    lines += [
        "",
        "## Full Row Scaling",
        "",
        "| row:model | safe | labels | coordinates | ||E||_op | relative offdiag | rank(E) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for key, item in summary["full_row_models"].items():
        lines.append(compact_row(key, item))

    lines += [
        "",
        "## CRT Face Scaling",
        "",
        "| omega(face):model | records | safe | max labels | max coordinates | max ||E||_op | max relative offdiag | max rank(E) |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, item in summary["face_models_by_omega"].items():
        lines.append(summary_row(key, item))

    restriction = summary["restriction_operators"]
    lines += [
        "",
        "## Restriction Operators",
        "",
        "| records | safe | max labels | max coordinates | max ||E||_op | max relative offdiag | max rank(E) |",
        "|---:|---:|---:|---:|---:|---:|---:|",
        "| {records} | {safe}/{records} | {labels} | {coords} | {op} | {rel} | {rank} |".format(
            records=restriction["records"],
            safe=restriction["safe"],
            labels=restriction["max_source_labels"],
            coords=restriction["max_coordinate_count"],
            op=render_float(restriction["max_off_diagonal_operator_norm"]),
            rel=render_float(restriction["max_relative_off_diagonal_operator_norm"]),
            rank=restriction["max_correction_rank"],
        ),
        "",
        "## First Unsafe Examples",
        "",
        "| row | face | scope | mode | labels | coordinates | ||E||_op | relative offdiag | rank(E) |",
        "|---:|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    for item in summary["unsafe_examples"]:
        face = "" if item["face"] is None else item["face"]
        lines.append(
            "| {row} | {face} | {scope} | {mode} | {labels} | {coords} | {op} | {rel} | {rank} |".format(
                row=item["row"],
                face=face,
                scope=item["scope"],
                mode=item["mode"],
                labels=item["source_label_count"],
                coords=item["coordinate_count"],
                op=render_float(item["off_diagonal_operator_norm"]),
                rel=render_float(item["relative_off_diagonal_operator_norm"]),
                rank=item["correction_rank"],
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "The diagonal identity, Mobius-weight, and conductor-depth norms have",
        "`E=0` on every row and CRT face tested.  The normalized CRT face",
        "restriction operators are also diagonal-safe.  The conductor-sum and",
        "Mobius-total models are deliberately unsafe phase-mixing comparisons:",
        "their correction rank and relative off-diagonal mass grow with the",
        "available non-split character labels.",
        "",
        "For Paper 22, this says the projective closure theorem can use the",
        "three-gap grammar only after the actual leakage form is proved",
        "zeta-diagonal on the split/flat quotient, or after the correction",
        "budget is shown to vanish along the tower.",
        "",
    ]
    return "\n".join(lines)


def summary_row(key: str, item: dict[str, Any]) -> str:
    return "| {key} | {records} | {safe}/{records} | {labels} | {coords} | {op} | {rel} | {rank} |".format(
        key=key,
        records=item["records"],
        safe=item["safe"],
        labels=item["max_source_labels"],
        coords=item["max_coordinate_count"],
        op=render_float(item["max_off_diagonal_operator_norm"]),
        rel=render_float(item["max_relative_off_diagonal_operator_norm"]),
        rank=item["max_correction_rank"],
    )


def compact_row(key: str, item: dict[str, Any]) -> str:
    return "| {key} | {safe}/{records} | {labels} | {coords} | {op} | {rel} | {rank} |".format(
        key=key,
        records=item["records"],
        safe=item["safe"],
        labels=item["max_source_labels"],
        coords=item["max_coordinate_count"],
        op=render_float(item["max_off_diagonal_operator_norm"]),
        rel=render_float(item["max_relative_off_diagonal_operator_norm"]),
        rank=item["max_correction_rank"],
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default=DEFAULT_ROWS)
    parser.add_argument("--modes", default=DEFAULT_MODES)
    parser.add_argument("--min-face-omega", type=int, default=2)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for key, item in payload["summary"]["by_scope_mode"].items():
        print(
            "{key}: safe={safe}/{records}, max_offdiag={op:.6g}".format(
                key=key,
                safe=item["safe"],
                records=item["records"],
                op=item["max_off_diagonal_operator_norm"],
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
