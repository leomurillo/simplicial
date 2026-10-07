"""Odd-prime top-packet frame-price formula for F_p[u]/(u^k).

Paper 25 Theorem 3.12 gives the top-packet coordinate-plane envelope for
the real characteristic-two character basis.  For odd residue fields the
additive characters are complex and the real tangent basis is obtained by
realifying conjugate character pairs into cosine/sine coordinates.

The branch geometry is the same as Theorem 3.12 after replacing F by p, but
the real coordinate-plane price is twice the complex-character envelope:

    mu_real_odd(p,k,alpha) = 2 * max(mu_top_plus, mu_non_top).

This script verifies that factor directly for prime fields by building the
real cosine/sine character basis of F_p[u]/(u^k), computing the off-centroid
Fisher Gram, and finite-differencing all cross-packet coordinate planes for
small prime rows.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path
from typing import Any

import numpy as np


DEFAULT_JSON = Path("empirical/reports/helmert_odd_residue_top_packet_formula.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_odd_residue_top_packet_formula.md")


Label = tuple[int, ...]


def parse_float_csv(text: str) -> list[float]:
    return [float(item.strip()) for item in text.split(",") if item.strip()]


def labels(p: int, k: int) -> list[Label]:
    return list(product(range(p), repeat=k))


def neg(label: Label, p: int) -> Label:
    return tuple((-value) % p for value in label)


def mul(left: Label, right: Label, p: int) -> Label:
    k = len(left)
    out = [0] * k
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j < k:
                out[i + j] = (out[i + j] + a * b) % p
    return tuple(out)


def phase(character: Label, point: Label, p: int) -> float:
    """Local trace-pairing phase: coefficient of u^(k-1) in character*point."""
    return 2.0 * np.pi * mul(character, point, p)[-1] / p


def packet_index(label: Label, p: int) -> int | None:
    if all(value == 0 for value in label):
        return None
    valuation = next(i for i, value in enumerate(label) if value % p)
    return len(label) - valuation


def real_modes(p: int, k: int) -> tuple[list[Label], list[tuple[str, Label, int]], list[int]]:
    all_labels = labels(p, k)
    seen: set[Label] = set()
    packets: dict[int, list[Label]] = {index: [] for index in range(1, k + 1)}
    for label in all_labels:
        if all(value == 0 for value in label) or label in seen:
            continue
        partner = neg(label, p)
        seen.add(label)
        seen.add(partner)
        packet = packet_index(label, p)
        if packet is None:
            continue
        packets[packet].append(min(label, partner))

    columns: list[tuple[str, Label, int]] = []
    sizes: list[int] = []
    for packet in range(1, k + 1):
        packets[packet].sort()
        sizes.append(2 * len(packets[packet]))
        for character in packets[packet]:
            columns.append(("cos", character, packet))
            columns.append(("sin", character, packet))
    return all_labels, columns, sizes


def top_probability(p: int, k: int, alpha: float) -> np.ndarray:
    """safe_probability for the top-packet displacement."""
    n = p**k
    rho = 0.95 * alpha
    probabilities: list[float] = []
    for point in labels(p, k):
        if all(value == 0 for value in point):
            probabilities.append((1.0 + rho * (p - 1)) / n)
        elif all(point[index] == 0 for index in range(k - 1)) and point[-1] != 0:
            probabilities.append((1.0 - rho) / n)
        else:
            probabilities.append(1.0 / n)
    return np.array(probabilities, dtype=float)


def fisher_gram_real(p: int, k: int, alpha: float) -> tuple[np.ndarray, list[int], list[tuple[str, Label, int]]]:
    all_labels, columns, sizes = real_modes(p, k)
    n = p**k
    basis = np.empty((n, len(columns)), dtype=float)
    scale = np.sqrt(2.0 / n)
    for row, point in enumerate(all_labels):
        for col, (kind, character, _) in enumerate(columns):
            theta = phase(character, point, p)
            basis[row, col] = scale * (np.cos(theta) if kind == "cos" else np.sin(theta))
    probability = top_probability(p, k, alpha)
    gram = basis.T @ (basis / probability[:, None]) / n
    return 0.5 * (gram + gram.T), sizes, columns


def block_slices(sizes: list[int]) -> list[slice]:
    out: list[slice] = []
    start = 0
    for size in sizes:
        out.append(slice(start, start + size))
        start += size
    return out


def off_block_energy(matrix: np.ndarray, sizes: list[int]) -> float:
    total = 0.0
    slices = block_slices(sizes)
    for i, rows in enumerate(slices):
        for j, cols in enumerate(slices):
            if i != j:
                block = matrix[rows, cols]
                total += float(np.sum(block * block))
    return total


def plane_rotation(dim: int, i: int, j: int, theta: float) -> np.ndarray:
    rotation = np.eye(dim)
    c = np.cos(theta)
    s = np.sin(theta)
    rotation[i, i] = c
    rotation[j, j] = c
    rotation[i, j] = -s
    rotation[j, i] = s
    return rotation


def branch_values(field_size: int, k: int, alpha: float) -> dict[str, float | str | None]:
    rho = 0.95 * alpha
    d = (1.0 + rho * (field_size - 1)) * (1.0 - rho)
    top = (
        2.0
        * rho
        * rho
        * abs((field_size - 1) * rho - field_size * (field_size - 2))
        / (field_size**k * d * d)
    )
    non_top = 0.0
    threshold = None
    if k >= 3:
        non_top = (
            2.0
            * (field_size - 1) ** 3
            * rho**4
            * (field_size ** (k - 2) - 1)
            / (d * d * field_size ** (2 * k - 2))
        )
        a = (field_size - 1) * (field_size ** (k - 2) - 1)
        b = field_size ** (k - 2)
        c = -b * field_size * (field_size - 2)
        tau_star = (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
        threshold = tau_star / (0.95 * (field_size - 1))
    complex_envelope = max(top, non_top)
    return {
        "rho": rho,
        "complex_top_branch": top,
        "complex_non_top_branch": non_top,
        "complex_envelope": complex_envelope,
        "real_top_branch": 2.0 * top,
        "real_non_top_branch": 2.0 * non_top,
        "real_envelope": 2.0 * complex_envelope,
        "winning_branch": "top" if top >= non_top else "non-top",
        "alpha_threshold": threshold,
    }


def finite_difference_mu(p: int, k: int, alpha: float, epsilon: float) -> dict[str, Any]:
    gram, sizes, columns = fisher_gram_real(p, k, alpha)
    dim = gram.shape[0]
    base = off_block_energy(gram, sizes)
    starts = np.cumsum([0] + sizes[:-1])
    best: dict[str, Any] | None = None
    for block_i, start_i in enumerate(starts):
        for block_j, start_j in enumerate(starts):
            if block_j <= block_i:
                continue
            for i in range(start_i, start_i + sizes[block_i]):
                for j in range(start_j, start_j + sizes[block_j]):
                    plus_q = plane_rotation(dim, i, j, epsilon)
                    minus_q = plane_rotation(dim, i, j, -epsilon)
                    plus = off_block_energy(plus_q.T @ gram @ plus_q, sizes)
                    minus = off_block_energy(minus_q.T @ gram @ minus_q, sizes)
                    descent = max((base - plus) / epsilon, (base - minus) / epsilon, 0.0)
                    mu = descent / 2.0
                    if best is None or mu > best["numeric_mu"]:
                        best = {
                            "numeric_mu": mu,
                            "packet_pair": [block_i + 1, block_j + 1],
                            "coordinate_pair": [columns[i], columns[j]],
                            "plus_energy": plus,
                            "minus_energy": minus,
                        }
    assert best is not None
    formula = branch_values(p, k, alpha)
    best["formula_mu"] = formula["real_envelope"]
    best["relative_error"] = abs(best["numeric_mu"] - best["formula_mu"]) / max(best["numeric_mu"], 1e-15)
    best["winning_branch_formula"] = formula["winning_branch"]
    return best


def verification_cases(alphas: list[float], epsilon: float) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for p, k in [(3, 2), (3, 3), (5, 2), (7, 2)]:
        for alpha in alphas:
            record = {
                "p": p,
                "k": k,
                "alpha": alpha,
                **finite_difference_mu(p, k, alpha, epsilon),
            }
            out.append(record)
    return out


def formula_table(alphas: list[float]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for p in [3, 5, 7, 11, 13]:
        for k in [2, 3, 4]:
            for alpha in alphas:
                values = branch_values(p, k, alpha)
                out.append({"p": p, "k": k, "alpha": alpha, **values})
    return out


def run(args: argparse.Namespace) -> dict[str, Any]:
    alphas = parse_float_csv(args.alphas)
    checks = verification_cases(alphas, args.epsilon)
    return {
        "purpose": (
            "Odd-prime real-basis verification of the top-packet frame-price "
            "formula.  The branch envelope is the Theorem 3.12 complex formula "
            "with F=p, multiplied by 2 because odd-prime characters realify "
            "into cosine/sine conjugate-pair coordinates."
        ),
        "config": {"alphas": alphas, "epsilon": args.epsilon},
        "verification": checks,
        "formula_table": formula_table(alphas),
    }


def format_float(value: Any) -> str:
    if value is None:
        return "--"
    if isinstance(value, str):
        return value
    return f"{float(value):.7g}"


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Odd-Residue Top-Packet Formula",
        "",
        "This report tests the odd-prime analogue of Paper 25 Theorem 3.12 in the",
        "real tangent basis.  For odd `p`, additive characters come in conjugate",
        "pairs, so the real cosine/sine coordinate-plane price is twice the",
        "complex-character branch envelope:",
        "",
        "\\[",
        "\\mu^{\\mathrm{real}}_{p,k}(\\alpha)",
        "=",
        "2\\max\\{\\mu^{\\mathrm{top},+}_{p,k}(\\alpha),\\mu^{\\mathrm{nt}}_{p,k}(\\alpha)\\}.",
        "\\]",
        "",
        "The branch formulas inside the maximum are the same as Theorem 3.12 with",
        "`F=p`.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Finite-Difference Verification",
        "",
        "| p | k | alpha | numeric mu | formula mu | rel err | numeric packet pair | formula branch |",
        "|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in payload["verification"]:
        lines.append(
            "| {p} | {k} | {alpha:.4g} | {numeric:.7g} | {formula:.7g} | {err:.3e} | {pair} | {branch} |".format(
                p=row["p"],
                k=row["k"],
                alpha=row["alpha"],
                numeric=row["numeric_mu"],
                formula=row["formula_mu"],
                err=row["relative_error"],
                pair=row["packet_pair"],
                branch=row["winning_branch_formula"],
            )
        )

    lines += [
        "",
        "## Formula Table",
        "",
        "| p | k | alpha | real envelope | real top | real non-top | branch | alpha threshold |",
        "|---:|---:|---:|---:|---:|---:|---|---:|",
    ]
    for row in payload["formula_table"]:
        lines.append(
            "| {p} | {k} | {alpha:.4g} | {env} | {top} | {nt} | {branch} | {thr} |".format(
                p=row["p"],
                k=row["k"],
                alpha=row["alpha"],
                env=format_float(row["real_envelope"]),
                top=format_float(row["real_top_branch"]),
                nt=format_float(row["real_non_top_branch"]),
                branch=row["winning_branch"],
                thr=format_float(row["alpha_threshold"]),
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "The odd-prime top-packet law is not a new branch formula; it is a",
        "realification of the same finite-field character-sum envelope.  The",
        "new arithmetic feature is the factor of two: characteristic-two",
        "characters are already real, while odd-prime characters split into",
        "cosine/sine conjugate-pair coordinates in the real tangent space.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alphas", default="0.35,0.75")
    parser.add_argument("--epsilon", type=float, default=1e-6)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    max_error = max(row["relative_error"] for row in payload["verification"])
    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    print(f"max verification relative error: {max_error:.3e}")
    for row in payload["verification"]:
        print(
            "p={p} k={k} alpha={alpha:.2f}: numeric={numeric:.7g}, "
            "formula={formula:.7g}, branch={branch}, rel_err={err:.3e}".format(
                p=row["p"],
                k=row["k"],
                alpha=row["alpha"],
                numeric=row["numeric_mu"],
                formula=row["formula_mu"],
                branch=row["winning_branch_formula"],
                err=row["relative_error"],
            )
        )
    return 0 if max_error < 1e-5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
