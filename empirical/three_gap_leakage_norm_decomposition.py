"""Decompose current-layer leakage norms into diagonal and correction parts.

This is the finite resolution of the post-convolution leakage question in
Paper 25.  On the convolutional current layer, a cyclic-face current has the
form

    J_j(zeta) = D(zeta) * chi_zeta(x_j).

A leakage norm with Gram matrix G is three-gap safe exactly when G is diagonal
by the output character label zeta, equivalently when it commutes with the
additive translation representation.  For an arbitrary Hermitian positive
Gram matrix, the canonical safe part is its translation average, which is just
diag(G) in the zeta basis.  The remaining off-diagonal part is the priced
correction.

This audit computes that decomposition for several finite compression models:

* zeta_identity: identity norm, safe;
* mobius_weight_diagonal: diagonal Mobius-weight norm, safe;
* conductor_weight_diagonal: diagonal conductor-depth norm, safe;
* crt_face_restriction: diagonal restriction/projector to CRT divisor faces,
  safe and functorial;
* conductor_sum and mobius_total: lossy phase-mixing compressions, unsafe.

The unsafe modes are falsifiers, not claims about the Paper 22 leakage form.
They measure exactly the correction that must be absent or separately priced.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from three_gap_psl_boundary_audit import (
    DEFAULT_ROWS,
    conductor,
    divisors_from_primes,
    is_squarefree,
    omega,
    parse_int_csv,
    prime_factors,
)


DEFAULT_JSON = Path("empirical/reports/three_gap_leakage_norm_decomposition.json")
DEFAULT_REPORT = Path("empirical/reports/three_gap_leakage_norm_decomposition.md")
DEFAULT_MODES = (
    "zeta_identity,mobius_weight_diagonal,conductor_weight_diagonal,"
    "conductor_sum,mobius_total"
)


def mobius_squarefree(value: int) -> int:
    return -1 if omega(value) % 2 else 1


def non_split_labels(n: int) -> list[int]:
    return [label for label in range(1, n) if omega(conductor(label, n)) >= 2]


def label_support(label: int, n: int) -> set[int]:
    return {p for p in prime_factors(n) if label % p != 0}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def product_int(values: Iterable[int]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def compression_matrix(n: int, labels: list[int], mode: str) -> tuple[np.ndarray, list[str]]:
    if mode == "zeta_identity":
        return np.eye(len(labels), dtype=np.complex128), [f"zeta:{z}" for z in labels]

    if mode == "mobius_weight_diagonal":
        diagonal = [mobius_squarefree(conductor(z, n)) for z in labels]
        return np.diag(diagonal).astype(np.complex128), [f"mu*zeta:{z}" for z in labels]

    if mode == "conductor_weight_diagonal":
        diagonal = [omega(conductor(z, n)) for z in labels]
        return np.diag(diagonal).astype(np.complex128), [f"depth*zeta:{z}" for z in labels]

    if mode == "conductor_sum":
        conductors = sorted({conductor(z, n) for z in labels}, key=lambda d: (omega(d), d))
        rows = np.zeros((len(conductors), len(labels)), dtype=np.complex128)
        for row, cond in enumerate(conductors):
            for col, zeta in enumerate(labels):
                if conductor(zeta, n) == cond:
                    rows[row, col] = 1.0
        return rows, [f"cond:{cond}" for cond in conductors]

    if mode == "mobius_total":
        rows = np.zeros((1, len(labels)), dtype=np.complex128)
        for col, zeta in enumerate(labels):
            rows[0, col] = mobius_squarefree(conductor(zeta, n))
        return rows, ["mobius_total"]

    raise ValueError(f"unknown mode: {mode}")


def restriction_matrix(n: int, labels: list[int], face: int) -> tuple[np.ndarray, list[str]]:
    face_primes = set(prime_factors(face))
    rows: list[np.ndarray] = []
    names: list[str] = []
    for col, zeta in enumerate(labels):
        if label_support(zeta, n) <= face_primes:
            row = np.zeros(len(labels), dtype=np.complex128)
            row[col] = 1.0
            rows.append(row)
            names.append(f"face:{face}:zeta:{zeta}")
    if not rows:
        return np.zeros((0, len(labels)), dtype=np.complex128), []
    return np.vstack(rows), names


def gram_decomposition(compression: np.ndarray, tolerance: float) -> dict[str, Any]:
    gram = compression.conj().T @ compression
    diagonal = np.diag(np.diag(gram))
    correction = gram - diagonal
    gram_norm = float(np.linalg.norm(gram, ord=2)) if gram.size else 0.0
    diagonal_norm = float(np.linalg.norm(diagonal, ord=2)) if diagonal.size else 0.0
    correction_norm = float(np.linalg.norm(correction, ord=2)) if correction.size else 0.0
    fro_correction = float(np.linalg.norm(correction, ord="fro")) if correction.size else 0.0
    return {
        "compressed_dimension": int(compression.shape[0]),
        "label_dimension": int(compression.shape[1]),
        "gram_operator_norm": gram_norm,
        "diagonal_operator_norm": diagonal_norm,
        "off_diagonal_operator_norm": correction_norm,
        "off_diagonal_frobenius_norm": fro_correction,
        "relative_off_diagonal_operator_norm": (
            correction_norm / gram_norm if gram_norm > tolerance else 0.0
        ),
        "is_zeta_diagonal_safe": correction_norm <= tolerance * max(1.0, gram_norm),
        "correction_rank": int(np.linalg.matrix_rank(correction, tol=tolerance))
        if correction.size
        else 0,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    modes = [item.strip() for item in args.modes.split(",") if item.strip()]
    records: list[dict[str, Any]] = []
    restriction_records: list[dict[str, Any]] = []
    for n in rows:
        if not is_squarefree(n):
            raise ValueError(f"row {n} is not squarefree")
        labels = non_split_labels(n)
        for mode in modes:
            matrix, names = compression_matrix(n, labels, mode)
            item = gram_decomposition(matrix, args.tolerance)
            item.update(
                {
                    "row": n,
                    "mode": mode,
                    "coordinate_count": len(names),
                    "non_split_label_count": len(labels),
                }
            )
            records.append(item)

        primes = prime_factors(n)
        for face in divisors_from_primes(primes, args.min_face_omega):
            matrix, names = restriction_matrix(n, labels, face)
            item = gram_decomposition(matrix, args.tolerance)
            item.update(
                {
                    "row": n,
                    "face": face,
                    "mode": "crt_face_restriction",
                    "coordinate_count": len(names),
                    "non_split_label_count": len(labels),
                }
            )
            restriction_records.append(item)

    return {
        "config": {
            "rows": rows,
            "modes": modes,
            "min_face_omega": args.min_face_omega,
            "tolerance": args.tolerance,
            "claim_hygiene": (
                "diagonal-safe leakage norms preserve the three-gap grammar; "
                "off-diagonal correction is a priced residual, not a proof of "
                "projective closure"
            ),
        },
        "summary": summarize(records, restriction_records),
        "records": records,
        "restriction_records": restriction_records,
    }


def summarize(records: list[dict[str, Any]], restriction_records: list[dict[str, Any]]) -> dict[str, Any]:
    by_mode: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        by_mode.setdefault(record["mode"], []).append(record)

    def aggregate(items: list[dict[str, Any]]) -> dict[str, Any]:
        return {
            "records": len(items),
            "safe": sum(item["is_zeta_diagonal_safe"] for item in items),
            "max_off_diagonal_operator_norm": max(
                (item["off_diagonal_operator_norm"] for item in items), default=0.0
            ),
            "max_relative_off_diagonal_operator_norm": max(
                (item["relative_off_diagonal_operator_norm"] for item in items),
                default=0.0,
            ),
            "max_correction_rank": max(
                (item["correction_rank"] for item in items), default=0
            ),
            "max_compressed_dimension": max(
                (item["compressed_dimension"] for item in items), default=0
            ),
        }

    return {
        "by_mode": {mode: aggregate(items) for mode, items in sorted(by_mode.items())},
        "crt_restrictions": aggregate(restriction_records),
        "unsafe_examples": [
            item
            for item in records
            if not item["is_zeta_diagonal_safe"]
        ][:10],
    }


def render_float(value: float) -> str:
    return f"{value:.7g}"


def render_report(payload: dict[str, Any]) -> str:
    summary = payload["summary"]
    lines = [
        "# Three-Gap Leakage Norm Decomposition",
        "",
        "This report resolves the post-convolution leakage-norm question at the",
        "finite linear-algebra level.  A leakage Gram form is three-gap safe",
        "exactly when its off-diagonal part in the output-character basis",
        "vanishes.  Otherwise it splits canonically into a diagonal safe part",
        "plus a priced non-diagonal correction.",
        "",
        "## By Compression / Leakage Model",
        "",
        "| mode | rows | safe | max offdiag op | max relative offdiag | max correction rank | max compressed dim |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for mode, item in summary["by_mode"].items():
        lines.append(
            "| {mode} | {records} | {safe}/{records} | {op} | {rel} | {rank} | {dim} |".format(
                mode=mode,
                records=item["records"],
                safe=item["safe"],
                op=render_float(item["max_off_diagonal_operator_norm"]),
                rel=render_float(item["max_relative_off_diagonal_operator_norm"]),
                rank=item["max_correction_rank"],
                dim=item["max_compressed_dimension"],
            )
        )
    restriction = summary["crt_restrictions"]
    lines += [
        "| crt_face_restriction | {records} | {safe}/{records} | {op} | {rel} | {rank} | {dim} |".format(
            records=restriction["records"],
            safe=restriction["safe"],
            op=render_float(restriction["max_off_diagonal_operator_norm"]),
            rel=render_float(restriction["max_relative_off_diagonal_operator_norm"]),
            rank=restriction["max_correction_rank"],
            dim=restriction["max_compressed_dimension"],
        ),
        "",
        "## First Unsafe Examples",
        "",
        "| row | mode | labels | compressed dim | offdiag op | relative offdiag | correction rank |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ]
    for item in summary["unsafe_examples"]:
        lines.append(
            "| {row} | {mode} | {labels} | {dim} | {op} | {rel} | {rank} |".format(
                row=item["row"],
                mode=item["mode"],
                labels=item["non_split_label_count"],
                dim=item["compressed_dimension"],
                op=render_float(item["off_diagonal_operator_norm"]),
                rel=render_float(item["relative_off_diagonal_operator_norm"]),
                rank=item["correction_rank"],
            )
        )
    lines += [
        "",
        "## Reading",
        "",
        "Identity, diagonal Mobius weights, diagonal conductor-depth weights, and",
        "CRT face restrictions are zeta-diagonal.  They preserve the three-gap",
        "grammar after the convolutional current layer.  Conductor-sum and",
        "Mobius-total compressions are unsafe because their Gram matrices contain",
        "cross-terms between distinct output characters.",
        "",
        "Thus the leakage norm/current compression is solved as a dichotomy:",
        "prove the Paper 22 leakage form is translation-equivariant, hence",
        "zeta-diagonal, or split it into its canonical diagonal Reynolds part",
        "plus the explicit off-diagonal correction priced by the operator norm",
        "recorded here.",
        "",
    ]
    return "\n".join(lines)


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
    for mode, item in payload["summary"]["by_mode"].items():
        print(
            "{mode}: safe={safe}/{records}, max_offdiag={op:.6g}".format(
                mode=mode,
                safe=item["safe"],
                records=item["records"],
                op=item["max_off_diagonal_operator_norm"],
            )
        )
    restriction = payload["summary"]["crt_restrictions"]
    print(
        "crt_face_restriction: safe={safe}/{records}, max_offdiag={op:.6g}".format(
            safe=restriction["safe"],
            records=restriction["records"],
            op=restriction["max_off_diagonal_operator_norm"],
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
