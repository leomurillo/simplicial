"""Numerical verification of Theorem 3.10 (Packet-local invariance of mu*).

Theorem 3.10 of Paper 25 proves that for q = 2^r and k >= s,

    mu*_{F_q[u]/(u^k)}(u^s, alpha) = mu*_{F_q[u]/(u^s)}(u^s, alpha).

The proof goes through Lemma 3.10.C: the off-centroid Fisher Gram
G_h^{R_k} restricted to V_{<=s} equals G_h^{R_s}, and the cross-prefix
entries G_h^{R_k}[V_{<=s}, V_{>s}] are exactly zero.

This script checks both Lemma 3.10.C numerically across the supported
F_2[u]/(u^k) rows for k = 2, 3, 4, 5 and reports the maximum within-prefix
Fisher Gram difference and the maximum cross-prefix Fisher Gram entry.
A successful check has both quantities at machine-precision noise levels.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from helmert_first_order_mu_atlas import evaluate_mu_case, ledger_weights  # noqa: E402
from helmert_local_rotation_obstruction import setup_case  # noqa: E402


DEFAULT_JSON = Path("empirical/reports/helmert_theorem_3_10_verification.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_theorem_3_10_verification.md")


def parse_float_csv(text: str) -> list[float]:
    return [float(item.strip()) for item in text.split(",") if item.strip()]


def verify_packet_for_amplitude(
    *,
    packet_index: int,
    amplitude_fraction: float,
    weights: dict[str, float],
) -> dict[str, Any]:
    """Verify Lemma 3.10.C and Theorem 3.10 for one (packet, amplitude) pair."""
    s = packet_index
    target_packet = f"u^{s}"
    # Reference: R_s = F_2[u]/(u^s), packet u^s is the top packet of R_s
    reference_key = f"f2-u{s}"
    reference_ctx = setup_case(reference_key, target_packet, amplitude_fraction)
    reference_gram = reference_ctx["gram"]
    reference_dim = reference_gram.shape[0]
    reference_mu = evaluate_mu_case(
        row_key=reference_key,
        target_packet=target_packet,
        amplitude_fraction=amplitude_fraction,
        epsilon=1e-6,
        weights=weights,
    )["max_mu_star"]

    embedded_results: list[dict[str, Any]] = []
    max_within_prefix_diff = 0.0
    max_cross_prefix_entry = 0.0
    max_mu_diff = 0.0
    for k in range(s + 1, 6):
        embedded_key = f"f2-u{k}"
        try:
            embedded_ctx = setup_case(embedded_key, target_packet, amplitude_fraction)
        except (ValueError, KeyError):
            continue
        embedded_gram = embedded_ctx["gram"]
        prefix_dim = sum(embedded_ctx["sizes"][: packet_index])
        within = embedded_gram[:prefix_dim, :prefix_dim]
        cross_right = embedded_gram[:prefix_dim, prefix_dim:]
        within_diff = float(np.max(np.abs(within - reference_gram)))
        cross_max = float(np.max(np.abs(cross_right))) if cross_right.size else 0.0
        embedded_mu = evaluate_mu_case(
            row_key=embedded_key,
            target_packet=target_packet,
            amplitude_fraction=amplitude_fraction,
            epsilon=1e-6,
            weights=weights,
        )["max_mu_star"]
        mu_diff = abs(embedded_mu - reference_mu)
        max_within_prefix_diff = max(max_within_prefix_diff, within_diff)
        max_cross_prefix_entry = max(max_cross_prefix_entry, cross_max)
        max_mu_diff = max(max_mu_diff, mu_diff)
        embedded_results.append(
            {
                "k": k,
                "row": embedded_ctx["spec"].display,
                "total_dim": embedded_gram.shape[0],
                "prefix_dim": prefix_dim,
                "within_prefix_block_diff": within_diff,
                "cross_prefix_block_max_abs": cross_max,
                "embedded_mu_star": embedded_mu,
                "mu_diff_vs_reference": mu_diff,
            }
        )

    return {
        "packet_index_s": s,
        "target_packet": target_packet,
        "amplitude_fraction": amplitude_fraction,
        "reference_row": reference_ctx["spec"].display,
        "reference_total_dim": reference_dim,
        "reference_mu_star": reference_mu,
        "max_within_prefix_block_diff": max_within_prefix_diff,
        "max_cross_prefix_block_entry": max_cross_prefix_entry,
        "max_mu_diff_vs_reference": max_mu_diff,
        "embedded_rows": embedded_results,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    amplitudes = parse_float_csv(args.amplitudes)
    weights = ledger_weights(args)
    results: list[dict[str, Any]] = []
    for s in range(2, 5):
        for amplitude in amplitudes:
            results.append(
                verify_packet_for_amplitude(
                    packet_index=s,
                    amplitude_fraction=amplitude,
                    weights=weights,
                )
            )
    return {
        "purpose": (
            "Numerical check of Theorem 3.10 (paper 25): for q=2 and k>=s, "
            "the within-prefix Fisher Gram is identical across F_2[u]/(u^k) "
            "and cross-prefix Fisher entries are zero, hence mu* is invariant."
        ),
        "config": {
            "amplitudes": amplitudes,
            "ledger_weights": weights,
        },
        "results": results,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Theorem 3.10 Numerical Verification",
        "",
        "This script verifies the structural content of Theorem 3.10 of Paper 25",
        "across the F_2[u]/(u^k) wild tower for k = 2, ..., 5.",
        "",
        "For each (target packet u^s, amplitude alpha), we compare:",
        "",
        "1. **Within-prefix Fisher Gram equality** (Lemma 3.10.C(i)):",
        "   max |G_h^{R_k}[V_{<=s}] - G_h^{R_s}| should be 0 (machine precision).",
        "2. **Cross-prefix Fisher Gram vanishing** (Lemma 3.10.C(ii)):",
        "   max |G_h^{R_k}[V_{<=s}, V_{>s}]| should be 0 (machine precision).",
        "3. **mu* invariance** (Theorem 3.10):",
        "   |mu*_{R_k} - mu*_{R_s}| should be 0 (machine precision).",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Verification table",
        "",
        "| target packet | amp | reference row | reference mu* | max within-prefix diff | max cross-prefix entry | max mu* diff |",
        "|---|---:|---|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        lines.append(
            "| {pkt} | {amp:.6g} | {ref} | {mu:.6g} | {within:.3e} | {cross:.3e} | {mudiff:.3e} |".format(
                pkt=result["target_packet"],
                amp=result["amplitude_fraction"],
                ref=result["reference_row"],
                mu=result["reference_mu_star"],
                within=result["max_within_prefix_block_diff"],
                cross=result["max_cross_prefix_block_entry"],
                mudiff=result["max_mu_diff_vs_reference"],
            )
        )

    lines += [
        "",
        "## Per-embedding details",
        "",
    ]
    for result in payload["results"]:
        lines.append(
            f"### Target {result['target_packet']} at amp={result['amplitude_fraction']}"
        )
        lines.append("")
        lines.append(
            "| k | row | total dim | prefix dim | within diff | cross max | embedded mu* | mu* diff |"
        )
        lines.append(
            "|---:|---|---:|---:|---:|---:|---:|---:|"
        )
        for row in result["embedded_rows"]:
            lines.append(
                "| {k} | {row} | {td} | {pd} | {w:.3e} | {c:.3e} | {mu:.6g} | {d:.3e} |".format(
                    k=row["k"],
                    row=row["row"],
                    td=row["total_dim"],
                    pd=row["prefix_dim"],
                    w=row["within_prefix_block_diff"],
                    c=row["cross_prefix_block_max_abs"],
                    mu=row["embedded_mu_star"],
                    d=row["mu_diff_vs_reference"],
                )
            )
        lines.append("")

    lines += [
        "## Pass criterion",
        "",
        "Theorem 3.10 is verified if all within-prefix diffs, cross-prefix",
        "entries, and mu* differences are at floating-point noise levels",
        "(< 1e-10).  See `helmert_theorem_3_10_verification.json` for full",
        "precision.",
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
    all_passed = True
    for result in payload["results"]:
        passed = (
            result["max_within_prefix_block_diff"] < 1e-10
            and result["max_cross_prefix_block_entry"] < 1e-10
            and result["max_mu_diff_vs_reference"] < 1e-10
        )
        status = "PASS" if passed else "FAIL"
        all_passed = all_passed and passed
        print(
            f"{status}  {result['target_packet']} amp={result['amplitude_fraction']}: "
            f"within={result['max_within_prefix_block_diff']:.3e} "
            f"cross={result['max_cross_prefix_block_entry']:.3e} "
            f"mu_diff={result['max_mu_diff_vs_reference']:.3e}"
        )
    print("ALL PASSED" if all_passed else "SOME FAILED")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
