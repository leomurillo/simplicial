"""Closed-form residue-degree top-packet decay for F_q[u]/(u^k), q > 2.

Theorem 3.12 of Paper 25 proves that for F = 2^r with r >= 2 and k >= 2,
the low-amplitude / top-coupling branch is

    mu*^top_{F,k}(alpha)
    =
    2 rho^2 |(F-1) rho - F(F-2)|
    /
    (F^k (1 + rho(F-1))^2 (1 - rho)^2),
    rho = 0.95 alpha.

The maximizing coordinate plane connects packet u^{k-1} to top packet u^k.
In particular F^k * mu*^top_{F,k} is exactly constant in k for F > 2.

At larger amplitudes and k >= 3, a non-top cross-packet plane can dominate.
The full coordinate-plane envelope is the maximum of the top-coupling branch
and the largest non-top/non-top branch.

This script:
  * compares the formula against the finite-difference atlas for the
    supported rows (F_4 at k=2,3 and F_8 at k=2),
  * extends the prediction to unsupported rows (F_4 at k=4..6, F_8 at k=3..4,
    F_16 at k=2..3, F_32 at k=2),
  * tabulates the residue-degree profile at fixed k=2 and amp=0.35
    to make the F=4 peak transparent.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from helmert_first_order_mu_atlas import evaluate_mu_case, ledger_weights  # noqa: E402


DEFAULT_JSON = Path("empirical/reports/helmert_residue_top_packet_decay_formula.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_residue_top_packet_decay_formula.md")


def gram_constants(F: int, k: int, alpha: float) -> dict[str, float]:
    rho = 0.95 * alpha
    n = F**k
    D = (1.0 + rho * (F - 1)) * (1.0 - rho)
    c0_abs = F * rho / (D * n)
    c1 = F * (F - 1) * rho * rho / (D * n)
    tau = (F - 1) * rho
    return {"rho": rho, "n": n, "D": D, "c0_abs": c0_abs, "c1": c1, "tau": tau}


def predict_top_branch(F: int, k: int, alpha: float) -> float:
    """Closed-form top-coupling branch for F_q[u]/(u^k), q = 2^r.

    Dispatches to Theorem 3.11 for F = 2 (maximizing plane u -> top, j=1)
    and Theorem 3.12 for F > 2 (maximizing plane u^{k-1} -> top, j=k-1).
    """
    if F == 2:
        rho = 0.95 * alpha
        # Theorem 3.11: mu*^top_{2,k} = 8(2^{k-1} - 1)/4^k * rho^3 / (1 - rho^2)^2
        return 8.0 * (2 ** (k - 1) - 1) / (4**k) * rho**3 / (1.0 - rho * rho) ** 2
    # Theorem 3.12: mu*^top_{F,k} = 2 rho^2 |(F-1)rho - F(F-2)|
    #                              / (F^k * (1 + rho(F-1))^2 (1 - rho)^2)
    constants = gram_constants(F, k, alpha)
    rho = constants["rho"]
    D = constants["D"]
    numerator = 2.0 * rho * rho * abs((F - 1) * rho - F * (F - 2))
    return numerator / (F**k * D * D)


def predict_non_top_branch(F: int, k: int, alpha: float) -> float:
    """Largest non-top/non-top coordinate-plane branch.

    The winning non-top plane, when this branch is active, connects the
    smallest packet u to the highest non-top packet u^{k-1}.  It is zero for
    k=2 because there is only one non-top packet.
    """
    if k < 3:
        return 0.0
    constants = gram_constants(F, k, alpha)
    c1 = constants["c1"]
    max_size_gap = (F - 1) * (F ** (k - 2) - 1)
    return 2.0 * max_size_gap * c1 * c1


def predict_mu_top(F: int, k: int, alpha: float) -> float:
    """Full coordinate-plane envelope for top-packet mu*."""
    return max(predict_top_branch(F, k, alpha), predict_non_top_branch(F, k, alpha))


def winning_branch(F: int, k: int, alpha: float) -> str:
    top = predict_top_branch(F, k, alpha)
    non_top = predict_non_top_branch(F, k, alpha)
    if top >= non_top:
        return "top" if F > 2 else "top-f2"
    return "non-top"


def top_branch_alpha_threshold(F: int, k: int) -> float | None:
    """Return alpha threshold below which the top branch dominates.

    For F>2 and k>=3, write tau=(F-1)rho.  Top branch dominates the largest
    non-top branch exactly when

        (F-1)(F^{k-2}-1) tau^2 + F^{k-2} tau - F^{k-2}F(F-2) <= 0.

    The positive root gives the switching threshold.  k=2 has no non-top
    branch, so the threshold is unbounded.
    """
    if F <= 2 or k < 3:
        return None
    A = (F - 1) * (F ** (k - 2) - 1)
    B = F ** (k - 2)
    C = -B * F * (F - 2)
    tau_star = (-B + (B * B - 4 * A * C) ** 0.5) / (2 * A)
    rho_star = tau_star / (F - 1)
    return rho_star / 0.95


def supported_row_key(F: int, k: int) -> str | None:
    """Return helmert_conductor_flag_baseline key if supported, else None."""
    if F == 2 and 2 <= k <= 5:
        return f"f2-u{k}"
    if F == 4 and 2 <= k <= 3:
        return f"f4-u{k}"
    if F == 8 and k == 2:
        return f"f8-u{k}"
    return None


def measured_mu_top(
    F: int,
    k: int,
    alpha: float,
    weights: dict[str, float],
) -> float | None:
    row = supported_row_key(F, k)
    if row is None:
        return None
    top_packet = f"u^{k}"
    result = evaluate_mu_case(
        row_key=row,
        target_packet=top_packet,
        amplitude_fraction=alpha,
        epsilon=1e-6,
        weights=weights,
    )
    return result["max_mu_star"]


def collect(
    F_values: list[int],
    k_values_per_F: dict[int, list[int]],
    alphas: list[float],
    weights: dict[str, float],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for F in F_values:
        for k in k_values_per_F.get(F, []):
            for alpha in alphas:
                predicted = predict_mu_top(F, k, alpha)
                top_branch = predict_top_branch(F, k, alpha)
                non_top_branch = predict_non_top_branch(F, k, alpha)
                measured = measured_mu_top(F, k, alpha, weights)
                rel_err = (
                    abs(predicted - measured) / measured
                    if measured is not None and measured > 0.0
                    else None
                )
                results.append(
                    {
                        "F": F,
                        "k": k,
                        "amplitude_fraction": alpha,
                        "predicted_mu_top": predicted,
                        "top_branch_mu": top_branch,
                        "non_top_branch_mu": non_top_branch,
                        "winning_branch": winning_branch(F, k, alpha),
                        "top_branch_alpha_threshold": top_branch_alpha_threshold(F, k),
                        "atlas_mu_top": measured,
                        "relative_error": rel_err,
                        "F_k_times_mu_top": (F**k) * predicted,
                        "F_k_times_top_branch": (F**k) * top_branch,
                    }
                )
    return results


def residue_profile(k: int, alpha: float) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for F in [2, 4, 8, 16, 32, 64, 128]:
        mu = predict_mu_top(F, k, alpha)
        out.append(
            {
                "F": F,
                "k": k,
                "amplitude_fraction": alpha,
                "predicted_mu_top": mu,
                "F_k_times_mu_top": (F**k) * mu,
            }
        )
    return out


def run(args: argparse.Namespace) -> dict[str, Any]:
    weights = ledger_weights(args)
    alphas = [float(a) for a in args.amplitudes.split(",") if a.strip()]
    F_values = [2, 4, 8, 16, 32]
    k_values_per_F = {
        2: [2, 3, 4, 5, 6, 7, 8],
        4: [2, 3, 4, 5, 6],
        8: [2, 3, 4],
        16: [2, 3],
        32: [2],
    }
    results = collect(F_values, k_values_per_F, alphas, weights)
    residue_at_k2 = residue_profile(k=2, alpha=0.35)
    return {
        "purpose": (
            "Theorem 3.12 closed-form residue-degree top-packet decay for "
            "F_q[u]/(u^k) with q = 2^r, r >= 2.  The default paper amplitudes "
            "sit on the top-coupling branch.  The script also reports the "
            "full coordinate-plane envelope when the non-top branch dominates."
        ),
        "config": {
            "amplitudes": alphas,
            "ledger_weights": weights,
            "F_values": F_values,
            "k_values_per_F": k_values_per_F,
        },
        "results": results,
        "residue_profile_k2_amp035": residue_at_k2,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Residue Top Packet Decay Formula",
        "",
        "This report verifies Theorem 3.12 of Paper 25: the closed-form",
        "top-coupling branch of the top-packet first-order frame price for",
        "F_q[u]/(u^k) with q = 2^r, r >= 2.  The branch formula is",
        "",
        "    mu*^top_{F,k}(alpha) = 2 rho^2 |(F-1)rho - F(F-2)|",
        "                          / (F^k * (1 + rho(F-1))^2 (1 - rho)^2),",
        "",
        "with rho = 0.95 * alpha.  On this branch, the maximizing plane connects",
        "packet u^{k-1} to the top packet u^k.  At higher amplitudes and k >= 3,",
        "the full coordinate-plane envelope can instead be controlled by the",
        "largest non-top/non-top plane.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Verification table (predicted vs atlas)",
        "",
        "Rows where the atlas has a measurement are marked with the relative error",
        "between predicted and measured mu*; unsupported rows have only the",
        "extrapolated prediction.",
        "",
        "| F | k | amp | envelope mu* | top branch | non-top branch | winner | atlas mu* | rel err | F^k * mu* |",
        "|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for item in payload["results"]:
        atlas = item["atlas_mu_top"]
        rel = item["relative_error"]
        atlas_str = f"{atlas:.7f}" if atlas is not None else "--"
        rel_str = f"{rel:.2e}" if rel is not None else "--"
        lines.append(
            (
                "| {F} | {k} | {amp:.4g} | {pred:.7f} | {top:.7f} | "
                "{non_top:.7f} | {winner} | {atlas} | {rel} | {prod:.6f} |"
            ).format(
                F=item["F"],
                k=item["k"],
                amp=item["amplitude_fraction"],
                pred=item["predicted_mu_top"],
                top=item["top_branch_mu"],
                non_top=item["non_top_branch_mu"],
                winner=item["winning_branch"],
                atlas=atlas_str,
                rel=rel_str,
                prod=item["F_k_times_mu_top"],
            )
        )

    lines += [
        "",
        "## Residue-degree profile at k=2, amp=0.35",
        "",
        "This shows the non-monotone residue-degree peak at F=4 explicitly.",
        "F^k mu* is monotone increasing in F (and bounded by 2/(1-rho)^2 as",
        "F -> infinity), but mu* itself decays as F^{-k}, so the product peaks",
        "at finite F.",
        "",
        "| F | k | predicted mu* | F^k * mu* |",
        "|---:|---:|---:|---:|",
    ]
    for item in payload["residue_profile_k2_amp035"]:
        lines.append(
            "| {F} | {k} | {mu:.7f} | {prod:.6f} |".format(
                F=item["F"],
                k=item["k"],
                mu=item["predicted_mu_top"],
                prod=item["F_k_times_mu_top"],
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "Theorem 3.12 supplies a closed form for the diagonal mu*^top in the F_q",
        "wild tower (q = 2^r, r >= 2).  Two structural features distinguish it",
        "from the F=2 case (Theorem 3.11):",
        "",
        "1. On the low-amplitude/top-coupling branch, the maximizing plane connects",
        "   u^{k-1} (highest non-top packet) to u^k (top packet), not u to u^k as",
        "   in F=2.  This is because the F^{k-1}(F-2) term in the descent rate is",
        "   zero for F=2 but nonzero for F>2.",
        "2. On that branch, F^k mu*^top is *exactly* constant in k for F>2.  For",
        "   F=2, only an asymptotic limit holds (with leading (2^{k-1}-1) factor).",
        "3. Above the amplitude threshold, the envelope switches to a non-top",
        "   branch connecting u to u^{k-1}.  The default paper amplitudes",
        "   0.1, 0.35, and 0.5 remain on the top-coupling branch for the",
        "   supported F>2 rows.",
        "",
        "The residue-degree profile at fixed k peaks at finite F (here F=4 for",
        "k=2 and amp=0.35), reconciling the apparent non-monotonicity that",
        "Computation 3.9 flagged as the next open question.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--amplitudes", default="0.1,0.35,0.5")
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
    max_rel = 0.0
    for item in payload["results"]:
        if item["relative_error"] is not None:
            tag = "ATLAS"
            max_rel = max(max_rel, item["relative_error"])
            err = f"rel_err={item['relative_error']:.2e}"
        else:
            tag = "PRED "
            err = "(predicted only)"
        print(
            f"{tag} F={item['F']} k={item['k']} amp={item['amplitude_fraction']:.2f}: "
            f"mu*={item['predicted_mu_top']:.7f}, winner={item['winning_branch']}, "
            f"F^k*mu*={item['F_k_times_mu_top']:.4f}, {err}"
        )
    print(f"max atlas relative error: {max_rel:.2e}")
    return 0 if max_rel < 5e-5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
