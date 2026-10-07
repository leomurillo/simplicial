"""First-order packet-respect price atlas for Paper 25.

The local-rotation obstruction shows that a quadratic packet-impurity price
cannot control a nonstationary one-point objective: the break-even lambda
diverges like 1/|theta|.  Theorem 3.5 proposes the first-order cure

    N(Q) = sum_{a != b} ||P_a Q P_b||_F,

with local required price mu* = sup_A |a(A)| / nu(A).  This atlas computes the
plane-rotation version of that finite price across the supported local rows.

It is intentionally narrower and faster than
helmert_local_rotation_obstruction.py: it does not sample a theta grid or
store every rotation trace.  It only estimates the local one-sided descent
rate of J0 at the conductor flag and divides by nu(A_ij)=2 for cross-packet
coordinate planes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from helmert_conductor_flag_baseline import ROW_SPECS, LocalAdjacencyConstructor, summarize  # noqa: E402
from helmert_local_rotation_obstruction import (  # noqa: E402
    cross_packet_pairs,
    first_order_packet_norm_for_plane,
    j0,
    ledger_at,
    plane_rotation,
    setup_case,
)


DEFAULT_JSON = Path("empirical/reports/helmert_first_order_mu_atlas.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_first_order_mu_atlas.md")


def parse_csv(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def parse_float_csv(text: str) -> list[float]:
    return [float(item.strip()) for item in text.split(",") if item.strip()]


def ledger_weights(args: argparse.Namespace) -> dict[str, float]:
    return {
        "block": args.block_weight,
        "mix": args.impurity_weight,
        "fisher_projection": args.fisher_projection_weight,
        "reciprocal_projection": args.reciprocal_projection_weight,
        "closure": args.closure_weight,
        "resource": args.resource_weight,
        "depth": args.depth_weight,
    }


def positive_summary(values: list[float]) -> dict[str, float]:
    positives = [value for value in values if value > 0.0]
    if not positives:
        return {key: 0.0 for key in ["min", "p05", "median", "mean", "p95", "max"]}
    return summarize(positives)


def evaluate_mu_case(
    *,
    row_key: str,
    target_packet: str,
    amplitude_fraction: float,
    epsilon: float,
    weights: dict[str, float],
) -> dict[str, Any]:
    context = setup_case(row_key, target_packet, amplitude_fraction)
    dim = context["gram"].shape[0]
    base = ledger_at(context, np.eye(dim), weights)
    base_j0 = j0(base, weights)
    pairs = cross_packet_pairs(context["sizes"])

    pair_records: list[dict[str, Any]] = []
    mu_values: list[float] = []
    for i, j in pairs:
        plus = ledger_at(context, plane_rotation(dim, i, j, epsilon), weights)
        minus = ledger_at(context, plane_rotation(dim, i, j, -epsilon), weights)
        plus_j0 = j0(plus, weights)
        minus_j0 = j0(minus, weights)
        d_j0 = (plus_j0 - minus_j0) / (2.0 * epsilon)
        one_sided_descent_rate = max(
            (base_j0 - plus_j0) / epsilon,
            (base_j0 - minus_j0) / epsilon,
            0.0,
        )
        observed_c = (
            plus["mix_impurity"] + minus["mix_impurity"] - 2.0 * base["mix_impurity"]
        ) / (2.0 * epsilon * epsilon)
        nu = first_order_packet_norm_for_plane(i, j, context["sizes"])
        mu = one_sided_descent_rate / nu if nu > 0.0 else 0.0
        mu_values.append(mu)
        pair_records.append(
            {
                "pair": [i, j],
                "d_J0_at_zero": d_j0,
                "one_sided_descent_rate": one_sided_descent_rate,
                "observed_quadratic_impurity_c": observed_c,
                "nu": nu,
                "mu": mu,
            }
        )

    best = max(pair_records, key=lambda item: item["mu"], default=None)
    positive_mu = [item["mu"] for item in pair_records if item["mu"] > 0.0]
    singular_count = sum(abs(item["d_J0_at_zero"]) > 1e-8 for item in pair_records)
    descent_count = sum(item["one_sided_descent_rate"] > 0.0 for item in pair_records)
    c_formula = 8.0 / dim
    c_errors = [
        abs(item["observed_quadratic_impurity_c"] - c_formula)
        for item in pair_records
    ]
    return {
        "row_key": row_key,
        "row": context["spec"].display,
        "target_packet": target_packet,
        "target_depth": context["target_index"] + 1,
        "packet_sizes": dict(zip(context["cond_order"], context["sizes"])),
        "active_prefix_dimension": sum(context["sizes"][: context["target_index"] + 1]),
        "total_dimension": dim,
        "amplitude_fraction": amplitude_fraction,
        "actual_amplitude": context["actual_amplitude"],
        "probability_min": context["probability_min"],
        "probability_max": context["probability_max"],
        "base_J0": base_j0,
        "base_J": base["J"],
        "base_block_coupling": base["block_coupling"],
        "cross_pair_count": len(pair_records),
        "singular_pair_count": singular_count,
        "descent_pair_count": descent_count,
        "positive_mu_summary": positive_summary(mu_values),
        "all_mu_summary": summarize(mu_values) if mu_values else positive_summary([]),
        "max_mu_star": best["mu"] if best else 0.0,
        "best_pair": best["pair"] if best else None,
        "best_d_J0_at_zero": best["d_J0_at_zero"] if best else 0.0,
        "best_one_sided_descent_rate": (
            best["one_sided_descent_rate"] if best else 0.0
        ),
        "quadratic_impurity_c_formula": c_formula,
        "quadratic_impurity_c_error_max": max(c_errors) if c_errors else 0.0,
        "top_pairs": sorted(pair_records, key=lambda item: item["mu"], reverse=True)[:10],
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_csv(args.rows)
    amplitudes = parse_float_csv(args.amplitudes)
    weights = ledger_weights(args)
    results: list[dict[str, Any]] = []
    for row_key in rows:
        if row_key not in ROW_SPECS:
            raise ValueError(f"unknown row key {row_key!r}; choose from {sorted(ROW_SPECS)}")
        spec = ROW_SPECS[row_key]
        ring = spec.factory()
        constructor = LocalAdjacencyConstructor(ring)
        cond_order = tuple(c for c in ring.conductor_order if c in constructor.packets)
        for packet_offset, target_packet in enumerate(cond_order):
            if args.skip_lowest and packet_offset == 0:
                continue
            for amplitude in amplitudes:
                results.append(
                    evaluate_mu_case(
                        row_key=row_key,
                        target_packet=target_packet,
                        amplitude_fraction=amplitude,
                        epsilon=args.epsilon,
                        weights=weights,
                    )
                )
    return {
        "purpose": (
            "First-order packet-respect price atlas: compute the plane-rotation "
            "mu* required by Theorem 3.5 of Paper 25 across supported rows."
        ),
        "config": {
            "rows": rows,
            "amplitudes": amplitudes,
            "epsilon": args.epsilon,
            "skip_lowest": args.skip_lowest,
            "ledger_weights": weights,
        },
        "results": results,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert First-Order Mu Atlas",
        "",
        "This atlas computes the plane-rotation first-order packet-respect price",
        "`mu*` from Paper 25 Theorem 3.5.  Unlike the quadratic impurity",
        "break-even price, this number remains finite as the cross-packet angle",
        "goes to zero.",
        "",
        "For a cross-packet coordinate plane `A_ij`, the first-order packet norm",
        "is `nu(A_ij)=2`, so the reported local price is the maximum one-sided",
        "descent rate of the unpriced ledger `J0` divided by `2`.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Mu Atlas",
        "",
        "| row | packet | amp | active dim | total dim | pairs | descent pairs | max mu* | p95 positive mu | median positive mu | best pair | c formula | max c error |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|",
    ]
    for result in payload["results"]:
        pos = result["positive_mu_summary"]
        lines.append(
            "| {row} | {packet} | {amp:.6g} | {active} | {total} | {pairs} | "
            "{descent} | {mu:.6g} | {p95:.6g} | {median:.6g} | {best} | "
            "{c:.6g} | {cerr:.3e} |".format(
                row=result["row"],
                packet=result["target_packet"],
                amp=result["amplitude_fraction"],
                active=result["active_prefix_dimension"],
                total=result["total_dimension"],
                pairs=result["cross_pair_count"],
                descent=result["descent_pair_count"],
                mu=result["max_mu_star"],
                p95=pos["p95"],
                median=pos["median"],
                best=result["best_pair"],
                c=result["quadratic_impurity_c_formula"],
                cerr=result["quadratic_impurity_c_error_max"],
            )
        )

    reference_amp = 0.35
    reference = [
        result for result in payload["results"]
        if abs(result["amplitude_fraction"] - reference_amp) < 1e-12
    ]
    if reference:
        lines += [
            "",
            f"## Tower Profiles at amplitude {reference_amp}",
            "",
            "### Wild-depth top packets",
            "",
            "| row | top packet | total dim | max mu* | descent pairs |",
            "|---|---|---:|---:|---:|",
        ]
        wild = [
            result for result in reference
            if result["row_key"].startswith("f2-u")
            and result["target_depth"] == len(result["packet_sizes"])
        ]
        wild.sort(key=lambda item: item["total_dimension"])
        for result in wild:
            lines.append(
                "| {row} | {packet} | {dim} | {mu:.6g} | {descent}/{pairs} |".format(
                    row=result["row"],
                    packet=result["target_packet"],
                    dim=result["total_dimension"],
                    mu=result["max_mu_star"],
                    descent=result["descent_pair_count"],
                    pairs=result["cross_pair_count"],
                )
            )

        lines += [
            "",
            "### Residue-degree dual-number packets",
            "",
            "| row | packet | total dim | max mu* | descent pairs |",
            "|---|---|---:|---:|---:|",
        ]
        residue = [
            result for result in reference
            if result["row_key"] in {"f2-u2", "f4-u2", "f8-u2"}
            and result["target_depth"] == len(result["packet_sizes"])
        ]
        residue.sort(key=lambda item: item["total_dimension"])
        for result in residue:
            lines.append(
                "| {row} | {packet} | {dim} | {mu:.6g} | {descent}/{pairs} |".format(
                    row=result["row"],
                    packet=result["target_packet"],
                    dim=result["total_dimension"],
                    mu=result["max_mu_star"],
                    descent=result["descent_pair_count"],
                    pairs=result["cross_pair_count"],
                )
            )

    lines += [
        "",
        "## Reading",
        "",
        "The `max mu*` column is the finite first-order price required to make",
        "the conductor flag locally resistant to cross-packet coordinate-plane",
        "escapes for the tested one-point ledger.  The `c formula` column checks",
        "Theorem 3.3's packet-impurity expansion for plane rotations:",
        "`c(A_ij)=8/dim(H_R)`.  Small `max c error` confirms that the numerical",
        "diagnostic is measuring the theorem's local expansion, not a sampling",
        "artifact.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rows",
        default="f2-u2,f2-u3,f2-u4,f2-u5,f4-u2,f4-u3,f8-u2",
    )
    parser.add_argument("--amplitudes", default="0.1,0.35,0.5")
    parser.add_argument("--epsilon", type=float, default=1e-6)
    parser.add_argument("--impurity-weight", type=float, default=1.0)
    parser.add_argument("--block-weight", type=float, default=1.0)
    parser.add_argument("--fisher-projection-weight", type=float, default=1.0)
    parser.add_argument("--reciprocal-projection-weight", type=float, default=1.0)
    parser.add_argument("--closure-weight", type=float, default=1.0)
    parser.add_argument("--resource-weight", type=float, default=0.1)
    parser.add_argument("--depth-weight", type=float, default=0.1)
    parser.add_argument("--skip-lowest", action="store_true", default=True)
    parser.add_argument("--include-lowest", dest="skip_lowest", action="store_false")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for result in payload["results"]:
        print(
            f"{result['row']} {result['target_packet']} amp={result['amplitude_fraction']}: "
            f"mu*={result['max_mu_star']:.6g}, "
            f"descent={result['descent_pair_count']}/{result['cross_pair_count']}, "
            f"c_error={result['quadratic_impurity_c_error_max']:.3e}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
