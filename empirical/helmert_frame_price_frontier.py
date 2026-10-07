"""Amplitude frontier for arithmetic frame price in Helmert/NZSBTL audits.

This driver turns the one-amplitude mixed-frame baseline into a small frontier
experiment.  For each row, conductor packet, and amplitude fraction, it samples
Haar-random mixed flags and records the largest packet-respect price needed
for the conductor prefix to beat every sampled mixed flag under the full
subspace J ledger.

The output is meant to feed Paper 25 directly:

    curvature linearization = Fisher coupling + arithmetic frame cost.

If the critical price is stable across amplitudes, it is a candidate finite
observable rather than a one-point artifact.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from helmert_conductor_flag_baseline import (  # noqa: E402
    ROW_SPECS,
    LocalAdjacencyConstructor,
    evaluate_packet,
    summarize,
)


DEFAULT_JSON = Path("empirical/reports/helmert_frame_price_frontier.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_frame_price_frontier.md")


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


def frontier_record(result: dict[str, Any]) -> dict[str, Any]:
    full_break_even = result["full_J_break_even_mix_weight"]
    raw_break_even = result["break_even_mix_weight"]
    return {
        "row_key": result["row_key"],
        "row": result["row"],
        "target_packet": result["target_packet"],
        "target_depth": result["target_depth"],
        "active_prefix_dimension": result["active_prefix_dimension"],
        "amplitude_fraction": result["amplitude_fraction"],
        "actual_amplitude": result["actual_amplitude"],
        "lambda_full_crit": full_break_even["max"],
        "lambda_full_median": full_break_even["median"],
        "lambda_raw_crit": raw_break_even["max"],
        "random_better_full_J_count": result["random_mixed_better_J_count"],
        "random_better_raw_count": result["random_mixed_better_count"],
        "samples": result["samples"],
        "conductor_J": result["conductor_full_ledger"]["J"],
        "random_J_median": result["random_mixed_J"]["median"],
        "conductor_block_coupling": result["conductor_block_coupling"],
        "random_block_median": result["random_mixed_block_coupling"]["median"],
        "oracle_block_coupling": result["oracle_eigenbasis_block_coupling"],
    }


def group_key(record: dict[str, Any]) -> tuple[str, str]:
    return (record["row_key"], record["target_packet"])


def summarize_frontier(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in records:
        grouped.setdefault(group_key(record), []).append(record)

    summaries: list[dict[str, Any]] = []
    for (_row_key, _packet), items in grouped.items():
        items = sorted(items, key=lambda item: item["amplitude_fraction"])
        lambda_full = [item["lambda_full_crit"] for item in items]
        lambda_raw = [item["lambda_raw_crit"] for item in items]
        better_full = [item["random_better_full_J_count"] for item in items]
        better_raw = [item["random_better_raw_count"] for item in items]
        summaries.append(
            {
                "row_key": items[0]["row_key"],
                "row": items[0]["row"],
                "target_packet": items[0]["target_packet"],
                "target_depth": items[0]["target_depth"],
                "active_prefix_dimension": items[0]["active_prefix_dimension"],
                "amplitudes": [item["amplitude_fraction"] for item in items],
                "lambda_full_crit": summarize(lambda_full),
                "lambda_raw_crit": summarize(lambda_raw),
                "max_random_better_full_J_count": max(better_full),
                "max_random_better_raw_count": max(better_raw),
                "samples": items[0]["samples"],
                "records": items,
            }
        )
    summaries.sort(
        key=lambda item: (
            item["lambda_full_crit"]["max"],
            item["max_random_better_full_J_count"],
            item["lambda_raw_crit"]["max"],
        ),
        reverse=True,
    )
    return summaries


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_csv(args.rows)
    amplitudes = parse_float_csv(args.amplitudes)
    weights = ledger_weights(args)
    records: list[dict[str, Any]] = []
    details: list[dict[str, Any]] = []

    for row_offset, key in enumerate(rows):
        if key not in ROW_SPECS:
            raise ValueError(f"unknown row key {key!r}; choose from {sorted(ROW_SPECS)}")
        spec = ROW_SPECS[key]
        ring = spec.factory()
        constructor = LocalAdjacencyConstructor(ring)
        cond_order = tuple(c for c in ring.conductor_order if c in constructor.packets)
        for packet_offset, target_packet in enumerate(cond_order):
            if args.skip_lowest and packet_offset == 0:
                continue
            for amplitude_offset, amplitude in enumerate(amplitudes):
                result = evaluate_packet(
                    ring=ring,
                    row_key=spec.key,
                    row_display=spec.display,
                    field_width=spec.field_width,
                    target_packet=target_packet,
                    samples=args.samples,
                    seed=(
                        args.seed
                        + 100000 * row_offset
                        + 1000 * packet_offset
                        + 37 * amplitude_offset
                    ),
                    amplitude_fraction=amplitude,
                    impurity_weight=args.impurity_weight,
                    weights=weights,
                )
                records.append(frontier_record(result))
                if args.keep_details:
                    details.append(result)

    summaries = summarize_frontier(records)
    return {
        "purpose": (
            "Amplitude frontier for Helmert/NZSBTL arithmetic frame price: "
            "sweep off-centroid displacement amplitude and estimate the "
            "largest packet-respect price needed for conductor prefixes to "
            "beat sampled mixed flags under the full J ledger."
        ),
        "config": {
            "rows": rows,
            "amplitudes": amplitudes,
            "samples": args.samples,
            "seed": args.seed,
            "ledger_weights": weights,
            "skip_lowest": args.skip_lowest,
            "keep_details": args.keep_details,
        },
        "summaries": summaries,
        "records": records,
        "details": details,
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Frame-Price Frontier",
        "",
        "This sweep estimates the arithmetic frame price needed to prefer",
        "conductor-respecting gauge cascades over Haar-random mixed flags.",
        "Each row/packet is evaluated at several off-centroid amplitudes.",
        "",
        "The main number is `lambda_full_crit`: the maximum sampled",
        "packet-commutator impurity weight needed for the conductor prefix to",
        "beat every sampled mixed flag under the full subspace J ledger.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Frontier Summary",
        "",
        "| row | packet | depth | active dim | lambda_full max | lambda_full median | lambda_raw max | max better full J | max better raw |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in payload["summaries"]:
        lines.append(
            "| {row} | {packet} | {depth} | {dim} | {lfmax:.6g} | {lfmed:.6g} | "
            "{lrmax:.6g} | {better_full}/{samples} | {better_raw}/{samples} |".format(
                row=item["row"],
                packet=item["target_packet"],
                depth=item["target_depth"],
                dim=item["active_prefix_dimension"],
                lfmax=item["lambda_full_crit"]["max"],
                lfmed=item["lambda_full_crit"]["median"],
                lrmax=item["lambda_raw_crit"]["max"],
                better_full=item["max_random_better_full_J_count"],
                better_raw=item["max_random_better_raw_count"],
                samples=item["samples"],
            )
        )

    lines += [
        "",
        "## Amplitude Traces",
        "",
    ]
    for item in payload["summaries"]:
        lines += [
            f"### {item['row']} target `{item['target_packet']}`",
            "",
            "| amplitude | lambda_full | better full J | lambda_raw | better raw | conductor J | random J median | conductor coupling | random coupling median |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for record in item["records"]:
            lines.append(
                "| {amp:.6g} | {lf:.6g} | {bf}/{samples} | {lr:.6g} | {br}/{samples} | "
                "{cj:.6g} | {rj:.6g} | {cc:.6g} | {rc:.6g} |".format(
                    amp=record["amplitude_fraction"],
                    lf=record["lambda_full_crit"],
                    bf=record["random_better_full_J_count"],
                    samples=record["samples"],
                    lr=record["lambda_raw_crit"],
                    br=record["random_better_raw_count"],
                    cj=record["conductor_J"],
                    rj=record["random_J_median"],
                    cc=record["conductor_block_coupling"],
                    rc=record["random_block_median"],
                )
            )
        lines.append("")

    lines += [
        "## Reading",
        "",
        "A high raw critical price says that random mixed frames can diagonalize",
        "the single tested Fisher matrix better than the conductor frame.  A",
        "low full critical price says that this advantage disappears once packet",
        "respect, projection, closure, resource, and depth are priced.  The",
        "interesting pressure points are therefore not the rows where raw mixed",
        "flags win, but the rows where `lambda_full_crit` remains high across",
        "amplitudes.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rows",
        default="f2-u2,f2-u3,f2-u4,f2-u5,f4-u2,f4-u3,f8-u2",
    )
    parser.add_argument("--amplitudes", default="0.1,0.2,0.35,0.5,0.7")
    parser.add_argument("--samples", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20260515)
    parser.add_argument("--impurity-weight", type=float, default=1.0)
    parser.add_argument("--block-weight", type=float, default=1.0)
    parser.add_argument("--fisher-projection-weight", type=float, default=1.0)
    parser.add_argument("--reciprocal-projection-weight", type=float, default=1.0)
    parser.add_argument("--closure-weight", type=float, default=1.0)
    parser.add_argument("--resource-weight", type=float, default=0.1)
    parser.add_argument("--depth-weight", type=float, default=0.1)
    parser.add_argument("--skip-lowest", action="store_true", default=True)
    parser.add_argument("--include-lowest", dest="skip_lowest", action="store_false")
    parser.add_argument("--keep-details", action="store_true")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for item in payload["summaries"][:8]:
        print(
            f"{item['row']} {item['target_packet']}: "
            f"lambda_full_max={item['lambda_full_crit']['max']:.6g}, "
            f"lambda_raw_max={item['lambda_raw_crit']['max']:.6g}, "
            f"better_full_max={item['max_random_better_full_J_count']}/{item['samples']}, "
            f"better_raw_max={item['max_random_better_raw_count']}/{item['samples']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
