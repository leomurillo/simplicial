"""Odd-residue packet-local invariance verifier for F_p[u]/(u^k).

Paper 25 Theorem 3.10 proves packet-local invariance in characteristic two:

    mu*_{F_q[u]/(u^k)}(u^s, alpha)
      = mu*_{F_q[u]/(u^s)}(u^s, alpha).

For odd residue characteristic, additive characters are complex and the real
tangent chart uses cosine/sine coordinates on conjugate character pairs.  This
script tests the non-top odd-prime cases directly in that real basis.  It
checks:

1. the within-prefix real Fisher Gram in R_k equals the R_s Fisher Gram;
2. the real Fisher cross block between conductor <= s and conductor > s is
   zero;
3. cross-prefix and beyond-prefix coordinate-plane derivatives vanish; and
4. the embedded real coordinate-plane price equals the quotient price.

The reported quotient price is also compared with Theorem 3.13's top-packet
formula for R_s, so the odd realification factor of 2 is visible in the common
value rather than in the invariance comparison.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from helmert_odd_residue_top_packet_formula import (  # noqa: E402
    Label,
    branch_values,
    labels,
    phase,
    real_modes,
)


DEFAULT_JSON = Path("empirical/reports/helmert_odd_residue_packet_invariance.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_odd_residue_packet_invariance.md")


def parse_float_csv(text: str) -> list[float]:
    return [float(item.strip()) for item in text.split(",") if item.strip()]


def parse_case_csv(text: str) -> list[tuple[int, int, int]]:
    cases: list[tuple[int, int, int]] = []
    for item in text.split(","):
        item = item.strip()
        if not item:
            continue
        parts = item.split(":")
        if len(parts) != 3:
            raise ValueError(f"case {item!r} should have form p:k:s")
        p, k, s = (int(part) for part in parts)
        if p <= 2:
            raise ValueError("odd-residue verifier requires odd prime p")
        if not (1 < s < k):
            raise ValueError("non-top packet invariance cases require 1 < s < k")
        cases.append((p, k, s))
    return cases


def in_ideal(point: Label, depth: int) -> bool:
    """Return True when point lies in u^depth R."""
    return all(value == 0 for value in point[:depth])


def packet_probability(p: int, k: int, packet_s: int, alpha: float) -> np.ndarray:
    """safe_probability for the Fourier-pure packet u^packet_s.

    For R_k = F_p[u]/(u^k), the inverse transform of the packet with conductor
    depth s is supported on u^(s-1)R:

        +(p^(s-1)(p-1))/p^k on u^s R,
        -p^(s-1)/p^k on u^(s-1)R \\ u^s R,
        0 elsewhere.

    The safe_probability normalization therefore gives the same probability
    levels as the top-packet case, but on the shifted ideal shell.
    """
    n = p**k
    rho = 0.95 * alpha
    probabilities: list[float] = []
    for point in labels(p, k):
        if in_ideal(point, packet_s):
            probabilities.append((1.0 + rho * (p - 1)) / n)
        elif in_ideal(point, packet_s - 1):
            probabilities.append((1.0 - rho) / n)
        else:
            probabilities.append(1.0 / n)
    return np.array(probabilities, dtype=float)


def fisher_gram_real_packet(
    p: int,
    k: int,
    packet_s: int,
    alpha: float,
) -> tuple[np.ndarray, list[int], list[tuple[str, Label, int]]]:
    all_labels, columns, sizes = real_modes(p, k)
    n = p**k
    basis = np.empty((n, len(columns)), dtype=float)
    scale = np.sqrt(2.0 / n)
    for row, point in enumerate(all_labels):
        for col, (kind, character, _) in enumerate(columns):
            theta = phase(character, point, p)
            basis[row, col] = scale * (np.cos(theta) if kind == "cos" else np.sin(theta))
    probability = packet_probability(p, k, packet_s, alpha)
    gram = basis.T @ (basis / probability[:, None]) / n
    return 0.5 * (gram + gram.T), sizes, columns


def block_slices(sizes: list[int]) -> list[slice]:
    out: list[slice] = []
    start = 0
    for size in sizes:
        out.append(slice(start, start + size))
        start += size
    return out


def packet_of(index: int, sizes: list[int]) -> int:
    total = 0
    for packet, size in enumerate(sizes, start=1):
        total += size
        if index < total:
            return packet
    raise ValueError(f"index {index} outside block sizes {sizes}")


def off_block_mask(sizes: list[int]) -> np.ndarray:
    dim = sum(sizes)
    mask = np.ones((dim, dim), dtype=float)
    for span in block_slices(sizes):
        mask[span, span] = 0.0
    return mask


def plane_derivative_off_energy(
    gram: np.ndarray,
    mask: np.ndarray,
    i: int,
    j: int,
) -> float:
    """Derivative of off-block energy for exp(theta A_ij) at theta=0."""
    derivative = np.zeros_like(gram)
    derivative[:, i] += gram[:, j]
    derivative[:, j] -= gram[:, i]
    derivative[i, :] += gram[j, :]
    derivative[j, :] -= gram[i, :]
    return float(2.0 * np.sum(mask * gram * derivative))


def coordinate_plane_mu(
    gram: np.ndarray,
    sizes: list[int],
    prefix_dim: int | None = None,
) -> dict[str, Any]:
    mask = off_block_mask(sizes)
    dim = gram.shape[0]
    class_max = {"in": 0.0, "out": 0.0, "beyond": 0.0}
    class_best: dict[str, dict[str, Any] | None] = {
        "in": None,
        "out": None,
        "beyond": None,
    }
    best: dict[str, Any] | None = None
    for i in range(dim):
        packet_i = packet_of(i, sizes)
        for j in range(i + 1, dim):
            packet_j = packet_of(j, sizes)
            if packet_i == packet_j:
                continue
            derivative = plane_derivative_off_energy(gram, mask, i, j)
            descent = abs(derivative)
            mu = descent / 2.0
            if prefix_dim is None or (i < prefix_dim and j < prefix_dim):
                pair_class = "in"
            elif i < prefix_dim or j < prefix_dim:
                pair_class = "out"
            else:
                pair_class = "beyond"
            if descent > class_max[pair_class]:
                class_max[pair_class] = descent
                class_best[pair_class] = {
                    "pair": [i, j],
                    "packet_pair": [packet_i, packet_j],
                    "derivative": derivative,
                    "mu": mu,
                }
            if best is None or mu > best["mu"]:
                best = {
                    "pair": [i, j],
                    "packet_pair": [packet_i, packet_j],
                    "class": pair_class,
                    "derivative": derivative,
                    "mu": mu,
                }
    return {
        "max_mu": 0.0 if best is None else best["mu"],
        "best": best,
        "class_max_descent": class_max,
        "class_best": class_best,
    }


def compare_case(p: int, k: int, s: int, alpha: float) -> dict[str, Any]:
    embedded_gram, embedded_sizes, embedded_columns = fisher_gram_real_packet(p, k, s, alpha)
    reference_gram, reference_sizes, reference_columns = fisher_gram_real_packet(p, s, s, alpha)
    prefix_dim = sum(embedded_sizes[:s])

    if prefix_dim != reference_gram.shape[0]:
        raise AssertionError("prefix dimension does not match reference dimension")

    within = embedded_gram[:prefix_dim, :prefix_dim]
    cross = embedded_gram[:prefix_dim, prefix_dim:]
    within_diff = float(np.max(np.abs(within - reference_gram)))
    cross_max = float(np.max(np.abs(cross))) if cross.size else 0.0
    prefix_columns = embedded_columns[:prefix_dim]
    columns_match = [
        (kind, tuple(character[-s:]), packet)
        for kind, character, packet in prefix_columns
    ] == reference_columns

    reference_mu = coordinate_plane_mu(reference_gram, reference_sizes)
    embedded_mu = coordinate_plane_mu(embedded_gram, embedded_sizes, prefix_dim=prefix_dim)
    formula = branch_values(p, s, alpha)
    complex_formula = float(formula["complex_envelope"])
    real_formula = float(formula["real_envelope"])
    factor = reference_mu["max_mu"] / complex_formula if complex_formula > 0 else 0.0

    return {
        "p": p,
        "k": k,
        "packet_s": s,
        "alpha": alpha,
        "embedded_row": f"F_{p}[u]/(u^{k})",
        "reference_row": f"F_{p}[u]/(u^{s})",
        "target_packet": f"u^{s}",
        "embedded_dim": embedded_gram.shape[0],
        "reference_dim": reference_gram.shape[0],
        "prefix_dim": prefix_dim,
        "embedded_packet_sizes": embedded_sizes,
        "reference_packet_sizes": reference_sizes,
        "prefix_columns_match_reference": columns_match,
        "within_prefix_block_diff": within_diff,
        "cross_prefix_block_max_abs": cross_max,
        "reference_mu": reference_mu,
        "embedded_mu": embedded_mu,
        "mu_diff_vs_reference": abs(embedded_mu["max_mu"] - reference_mu["max_mu"]),
        "theorem_3_13_complex_envelope_for_reference": complex_formula,
        "theorem_3_13_real_envelope_for_reference": real_formula,
        "reference_mu_diff_vs_formula": abs(reference_mu["max_mu"] - real_formula),
        "real_to_complex_factor_observed": factor,
        "pass": (
            columns_match
            and within_diff < 1e-10
            and cross_max < 1e-10
            and embedded_mu["class_max_descent"]["out"] < 1e-10
            and embedded_mu["class_max_descent"]["beyond"] < 1e-10
            and abs(embedded_mu["max_mu"] - reference_mu["max_mu"]) < 1e-10
            and abs(reference_mu["max_mu"] - real_formula) < 1e-10
        ),
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    cases = parse_case_csv(args.cases)
    alphas = parse_float_csv(args.alphas)
    results: list[dict[str, Any]] = []
    for p, k, s in cases:
        for alpha in alphas:
            results.append(compare_case(p, k, s, alpha))
    return {
        "purpose": (
            "Odd-prime real-basis verification of packet-local invariance for "
            "non-top packets in F_p[u]/(u^k)."
        ),
        "config": {"cases": cases, "alphas": alphas},
        "results": results,
    }


def fmt(value: float) -> str:
    return f"{value:.7g}"


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Odd-Residue Packet Invariance",
        "",
        "This report tests the non-top odd-residue analogue of Paper 25 Theorem",
        "3.10 in the real cosine/sine tangent basis.",
        "",
        "For each case, the verifier compares the real Fisher Gram of",
        "`F_p[u]/(u^k)` at target packet `u^s` with the top-packet Gram of",
        "`F_p[u]/(u^s)`.  It also differentiates the real off-block Fisher",
        "coupling over all cross-packet coordinate planes and records whether",
        "the winning plane stays inside the conductor-`<=s` prefix.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Structural Checks",
        "",
        "| row | target | alpha | prefix dim | within diff | cross max | out descent | beyond descent | columns match | pass |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in payload["results"]:
        lines.append(
            "| {row_name} | {target} | {alpha:.4g} | {prefix_dim} | {within:.3e} | "
            "{cross:.3e} | {out:.3e} | {beyond:.3e} | {columns} | {passed} |".format(
                row_name=row["embedded_row"],
                target=row["target_packet"],
                alpha=row["alpha"],
                prefix_dim=row["prefix_dim"],
                within=row["within_prefix_block_diff"],
                cross=row["cross_prefix_block_max_abs"],
                out=row["embedded_mu"]["class_max_descent"]["out"],
                beyond=row["embedded_mu"]["class_max_descent"]["beyond"],
                columns="yes" if row["prefix_columns_match_reference"] else "no",
                passed="PASS" if row["pass"] else "FAIL",
            )
        )

    lines += [
        "",
        "## Mu Comparison",
        "",
        "| row | reference | alpha | embedded mu | reference mu | formula real | mu diff | formula diff | factor vs complex | best class | best packets |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in payload["results"]:
        best = row["embedded_mu"]["best"]
        lines.append(
            "| {row_name} | {ref} | {alpha:.4g} | {embedded} | {reference} | "
            "{formula} | {mudiff:.3e} | {fdiff:.3e} | {factor:.6g} | {klass} | {packets} |".format(
                row_name=row["embedded_row"],
                ref=row["reference_row"],
                alpha=row["alpha"],
                embedded=fmt(row["embedded_mu"]["max_mu"]),
                reference=fmt(row["reference_mu"]["max_mu"]),
                formula=fmt(row["theorem_3_13_real_envelope_for_reference"]),
                mudiff=row["mu_diff_vs_reference"],
                fdiff=row["reference_mu_diff_vs_formula"],
                factor=row["real_to_complex_factor_observed"],
                klass=best["class"] if best else "--",
                packets=best["packet_pair"] if best else "--",
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "The real cross-prefix block vanishes to numerical precision; it does not",
        "split into a nonzero conjugate-pair block.  Realification doubles the",
        "odd-prime price relative to the complex character envelope, but that",
        "same factor appears in both the embedded row and the quotient row, so",
        "it cancels in the packet-local invariance comparison.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", default="3:3:2,3:4:2,3:4:3,5:3:2")
    parser.add_argument("--alphas", default="0.35,0.75")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    all_passed = all(row["pass"] for row in payload["results"])
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for row in payload["results"]:
        status = "PASS" if row["pass"] else "FAIL"
        print(
            "{status} p={p} k={k} s={s} alpha={alpha:.2f}: "
            "within={within:.3e} cross={cross:.3e} "
            "out={out:.3e} beyond={beyond:.3e} "
            "mu={mu:.7g} ref={ref:.7g} factor={factor:.6g}".format(
                status=status,
                p=row["p"],
                k=row["k"],
                s=row["packet_s"],
                alpha=row["alpha"],
                within=row["within_prefix_block_diff"],
                cross=row["cross_prefix_block_max_abs"],
                out=row["embedded_mu"]["class_max_descent"]["out"],
                beyond=row["embedded_mu"]["class_max_descent"]["beyond"],
                mu=row["embedded_mu"]["max_mu"],
                ref=row["reference_mu"]["max_mu"],
                factor=row["real_to_complex_factor_observed"],
            )
        )
    print("ALL PASSED" if all_passed else "SOME FAILED")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
