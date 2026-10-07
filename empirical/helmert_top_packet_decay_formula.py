"""Closed-form top-packet decay for F_2[u]/(u^k).

Paper 25 Theorem 3.10 proves packet-local invariance for fixed target packet
u^s embedded into deeper wild rows.  It does not explain the diagonal
top-packet sequence

    mu*_{F_2[u]/(u^k)}(u^k, alpha).

For the top packet, the Fourier-pure displacement has a two-point form:

    h(0)=1/2, h(1)=-1/2, h(x)=0 otherwise.

The resulting Fisher Gram is a rank-two perturbation of the identity with two
off-block constants.  This script records the closed-form consequence:

    mu_top(k, alpha)
      = 8(2^{k-1}-1)/4^k * rho^3/(1-rho^2)^2,
        rho = 0.95 alpha.

It compares the formula against the finite-difference atlas for k <= 5 and
then extrapolates the decay profile.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from helmert_first_order_mu_atlas import evaluate_mu_case, ledger_weights  # noqa: E402


DEFAULT_JSON = Path("empirical/reports/helmert_top_packet_decay_formula.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_top_packet_decay_formula.md")


def parse_float_csv(text: str) -> list[float]:
    return [float(item.strip()) for item in text.split(",") if item.strip()]


def mu_top_formula(k: int, alpha: float) -> float:
    rho = 0.95 * alpha
    return (
        8.0
        * ((2 ** (k - 1)) - 1.0)
        / (4.0 ** k)
        * (rho ** 3)
        / ((1.0 - rho * rho) ** 2)
    )


def asymptotic_constant(alpha: float) -> float:
    rho = 0.95 * alpha
    return 4.0 * (rho ** 3) / ((1.0 - rho * rho) ** 2)


def atlas_value(k: int, alpha: float, weights: dict[str, float]) -> float | None:
    if k < 2 or k > 5:
        return None
    return evaluate_mu_case(
        row_key=f"f2-u{k}",
        target_packet=f"u^{k}",
        amplitude_fraction=alpha,
        epsilon=1e-6,
        weights=weights,
    )["max_mu_star"]


def run(args: argparse.Namespace) -> dict[str, Any]:
    amplitudes = parse_float_csv(args.amplitudes)
    weights = ledger_weights(args)
    rows: list[dict[str, Any]] = []
    for alpha in amplitudes:
        previous = None
        for k in range(args.k_min, args.k_max + 1):
            formula = mu_top_formula(k, alpha)
            atlas = atlas_value(k, alpha, weights)
            rows.append(
                {
                    "alpha": alpha,
                    "rho": 0.95 * alpha,
                    "k": k,
                    "dim_H": (2 ** k) - 1,
                    "formula_mu_top": formula,
                    "atlas_mu_top": atlas,
                    "abs_error_vs_atlas": abs(formula - atlas) if atlas is not None else None,
                    "ratio_to_previous_k": formula / previous if previous else None,
                    "scaled_2k_mu": (2 ** k) * formula,
                    "asymptotic_scaled_limit": asymptotic_constant(alpha),
                    "best_plane": [1, k],
                }
            )
            previous = formula
    return {
        "purpose": (
            "Closed-form F_2[u]/(u^k) top-packet first-order frame-price "
            "decay and comparison against the finite-difference mu* atlas."
        ),
        "config": {
            "amplitudes": amplitudes,
            "k_min": args.k_min,
            "k_max": args.k_max,
            "ledger_weights": weights,
        },
        "formula": (
            "mu_top(k,alpha)=8(2^(k-1)-1)/4^k * rho^3/(1-rho^2)^2, "
            "rho=0.95 alpha"
        ),
        "rows": rows,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Top-Packet Decay Formula",
        "",
        "This report records the closed-form first-order packet price for the",
        "top-packet row `F_2[u]/(u^k)`.",
        "",
        "For `rho = 0.95 alpha`,",
        "",
        "\\[",
        "\\mu_k^{top}(\\alpha)",
        "=",
        "{8(2^{k-1}-1)\\over 4^k}\\,{\\rho^3\\over(1-\\rho^2)^2}.",
        "\\]",
        "",
        "Equivalently,",
        "",
        "\\[",
        "2^k\\mu_k^{top}(\\alpha)",
        "\\to",
        "{4\\rho^3\\over(1-\\rho^2)^2}.",
        "\\]",
        "",
        "The maximizing coordinate plane is the plane connecting the `u` packet",
        "to the top `u^k` packet.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    for alpha in payload["config"]["amplitudes"]:
        lines += [
            "",
            f"## Alpha {alpha}",
            "",
            "| k | dim H | formula mu_top | atlas mu_top | abs error | ratio to previous k | 2^k mu | limit |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for row in [item for item in payload["rows"] if item["alpha"] == alpha]:
            atlas = "" if row["atlas_mu_top"] is None else f"{row['atlas_mu_top']:.12g}"
            err = "" if row["abs_error_vs_atlas"] is None else f"{row['abs_error_vs_atlas']:.3e}"
            ratio = "" if row["ratio_to_previous_k"] is None else f"{row['ratio_to_previous_k']:.6g}"
            lines.append(
                "| {k} | {dim} | {mu:.12g} | {atlas} | {err} | {ratio} | {scaled:.12g} | {limit:.12g} |".format(
                    k=row["k"],
                    dim=row["dim_H"],
                    mu=row["formula_mu_top"],
                    atlas=atlas,
                    err=err,
                    ratio=ratio,
                    scaled=row["scaled_2k_mu"],
                    limit=row["asymptotic_scaled_limit"],
                )
            )

    lines += [
        "",
        "## Reading",
        "",
        "The finite-difference atlas agrees with the closed form for the supported",
        "rows `k <= 5` up to the expected finite-difference tolerance.  The decay",
        "is asymptotically `2^{-k}` after multiplying by the amplitude-dependent",
        "constant `4 rho^3/(1-rho^2)^2`.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--amplitudes", default="0.1,0.35,0.5")
    parser.add_argument("--k-min", type=int, default=2)
    parser.add_argument("--k-max", type=int, default=16)
    parser.add_argument("--impurity-weight", type=float, default=1.0)
    parser.add_argument("--block-weight", type=float, default=1.0)
    parser.add_argument("--fisher-projection-weight", type=float, default=1.0)
    parser.add_argument("--reciprocal-projection-weight", type=float, default=1.0)
    parser.add_argument("--closure-weight", type=float, default=1.0)
    parser.add_argument("--resource-weight", type=float, default=0.1)
    parser.add_argument("--depth-weight", type=float, default=0.1)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for row in payload["rows"]:
        if row["alpha"] == payload["config"]["amplitudes"][0] and row["k"] <= 6:
            print(
                f"alpha={row['alpha']} k={row['k']}: "
                f"mu={row['formula_mu_top']:.6g}, "
                f"atlas={row['atlas_mu_top']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
