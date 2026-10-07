"""Transfer audit for B3 normalizer-saturated information investment.

B2 buys the minimal generated subgroup for one active reciprocal support.
B3 buys the normalizer-saturated subgroup for all equivalent supports in the
normalizer orbit.  This audit tests when the B3 symmetry premium pays for
itself under held-out normalizer-transformed tasks.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Hashable


sys.path.insert(0, str(Path(__file__).resolve().parent))

from information_investment_functional import (
    FiniteRow,
    build_rows,
    conductor_packet_support,
    dft,
    generated_subgroup,
    normalizer_saturation,
    reciprocal_density_from_support,
    score_candidate,
)


Mode = Hashable
DEFAULT_JSON = Path("empirical/reports/normalizer_transfer_audit.json")
DEFAULT_REPORT = Path("empirical/reports/normalizer_transfer_audit.md")


def task_coefficients(
    row: FiniteRow,
    support: set[Mode],
    amplitude: float,
) -> tuple[dict[Mode, complex], dict[Mode, complex]]:
    reciprocal, probability = reciprocal_density_from_support(row, support, amplitude)
    uniform = 1.0 / len(row.labels)
    tangent = {label: probability[label] - uniform for label in row.labels}
    return dft(row, tangent), dft(row, reciprocal)


def random_source_support(row: FiniteRow, rng: random.Random, max_size: int) -> set[Mode]:
    nonzero = list(row.nonzero_modes)
    size = rng.randint(1, min(max_size, len(nonzero)))
    if row.key.startswith("c"):
        base = rng.choice(nonzero)
        partner = (-int(base)) % len(row.labels)
        support = {base}
        if partner != row.zero:
            support.add(partner)
        return support
    return set(rng.sample(nonzero, size))


def transform_support(row: FiniteRow, support: set[Mode], action: dict[Mode, Mode]) -> set[Mode]:
    return {action[mode] for mode in support if action[mode] != row.zero}


def structural_part(score: dict[str, float], resource_weight: float) -> float:
    return score["J"] - resource_weight * score["resource_cost"]


def summarize(records: list[dict[str, float]]) -> dict[str, float]:
    out: dict[str, float] = {"count": float(len(records))}
    for key in [
        "J",
        "fisher_projection_error",
        "reciprocal_projection_error",
        "closure_leakage",
        "descent_balance_cost",
        "resource_cost",
        "support_size",
        "structural_cost",
    ]:
        out[f"mean_{key}"] = sum(record[key] for record in records) / len(records)
    return out


def summarize_transfer_pairs(records: list[dict[str, float]]) -> dict[str, float]:
    return {
        "count": float(len(records)),
        "mean_premium": sum(record["premium"] for record in records) / len(records),
        "mean_structural_gain": sum(record["structural_gain"] for record in records)
        / len(records),
        "mean_net_gain": sum(record["net_gain"] for record in records) / len(records),
        "normalizer_beats_minimal_rate": sum(
            record["normalizer_beats_minimal"] for record in records
        )
        / len(records),
    }


def run_row(
    row: FiniteRow,
    *,
    source_tasks: int,
    transfers_per_source: int,
    max_source_size: int,
    amplitude_min: float,
    amplitude_max: float,
    resource_weight: float,
    seed: int,
) -> dict[str, Any]:
    rng = random.Random(seed)
    if not row.normalizer_actions:
        raise ValueError(f"{row.key}: row has no normalizer actions")

    policy_records: dict[str, list[dict[str, float]]] = defaultdict(list)
    wins: dict[str, int] = defaultdict(int)
    pair_records: list[dict[str, float]] = []
    examples: list[dict[str, Any]] = []

    for source_index in range(source_tasks):
        source = random_source_support(row, rng, max_source_size)
        source_minimal = generated_subgroup(row, source)
        source_normalizer = normalizer_saturation(row, source)
        source_conductor = conductor_packet_support(row, source)

        for transfer_index in range(transfers_per_source):
            action = rng.choice(row.normalizer_actions)
            target = transform_support(row, source, action)
            amplitude = rng.uniform(amplitude_min, amplitude_max)
            h_hat, m_hat = task_coefficients(row, target, amplitude)

            policies = {
                "source_raw": source,
                "source_minimal": source_minimal,
                "source_normalizer": source_normalizer,
                "source_conductor_packet": source_conductor,
                "full": set(row.nonzero_modes),
                "oracle_minimal": generated_subgroup(row, target),
            }

            scored: list[dict[str, Any]] = []
            for name, support in policies.items():
                score = score_candidate(row, support, h_hat, m_hat, resource_weight)
                record = {
                    **score,
                    "support_size": float(len(support)),
                    "structural_cost": structural_part(score, resource_weight),
                }
                policy_records[name].append(record)
                scored.append({"name": name, **record})

            scored.sort(key=lambda item: (item["J"], item["resource_cost"], item["name"]))
            wins[scored[0]["name"]] += 1

            minimal_score = scored[[item["name"] for item in scored].index("source_minimal")]
            normalizer_score = scored[[item["name"] for item in scored].index("source_normalizer")]
            premium = resource_weight * (
                normalizer_score["resource_cost"] - minimal_score["resource_cost"]
            )
            structural_gain = minimal_score["structural_cost"] - normalizer_score["structural_cost"]
            net_gain = minimal_score["J"] - normalizer_score["J"]
            pair_records.append(
                {
                    "premium": premium,
                    "structural_gain": structural_gain,
                    "net_gain": net_gain,
                    "normalizer_beats_minimal": 1.0 if net_gain > 1e-12 else 0.0,
                }
            )

            if len(examples) < 6 and (
                net_gain > 1e-12 or len(source_normalizer) > len(source_minimal)
            ):
                examples.append(
                    {
                        "source": [
                            row.label_name(mode) for mode in sorted(source, key=row.label_name)
                        ],
                        "target": [
                            row.label_name(mode) for mode in sorted(target, key=row.label_name)
                        ],
                        "source_minimal": [
                            row.label_name(mode)
                            for mode in sorted(source_minimal, key=row.label_name)
                        ],
                        "source_normalizer": [
                            row.label_name(mode)
                            for mode in sorted(source_normalizer, key=row.label_name)
                        ],
                        "minimal_J": minimal_score["J"],
                        "normalizer_J": normalizer_score["J"],
                        "premium": premium,
                        "structural_gain": structural_gain,
                    }
                )

    policies = {
        name: {
            **summarize(records),
            "wins": wins.get(name, 0),
        }
        for name, records in policy_records.items()
    }
    ordered = sorted(policies.items(), key=lambda item: (item[1]["mean_J"], item[0]))
    transfer_summary = summarize_transfer_pairs(pair_records)
    return {
        "key": row.key,
        "row": row.name,
        "label_count": len(row.labels),
        "normalizer_action_count": len(row.normalizer_actions),
        "source_tasks": source_tasks,
        "transfers_per_source": transfers_per_source,
        "winner_by_mean_J": ordered[0][0],
        "policies": {name: summary for name, summary in ordered},
        "transfer_summary": transfer_summary,
        "examples": examples,
    }


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    row_keys = [key.strip() for key in args.rows.split(",") if key.strip()]
    rows = []
    for index, row in enumerate(build_rows(row_keys)):
        rows.append(
            run_row(
                row,
                source_tasks=args.source_tasks,
                transfers_per_source=args.transfers_per_source,
                max_source_size=args.max_source_size,
                amplitude_min=args.amplitude_min,
                amplitude_max=args.amplitude_max,
                resource_weight=args.resource_weight,
                seed=args.seed + 1000 * index,
            )
        )
    return {
        "purpose": (
            "Transfer audit for B3: compare source-minimal subgroup descent "
            "against source normalizer saturation on held-out normalizer "
            "transforms of the source task."
        ),
        "config": {
            "rows": row_keys,
            "source_tasks": args.source_tasks,
            "transfers_per_source": args.transfers_per_source,
            "max_source_size": args.max_source_size,
            "amplitude_min": args.amplitude_min,
            "amplitude_max": args.amplitude_max,
            "resource_weight": args.resource_weight,
            "seed": args.seed,
        },
        "rows": rows,
    }


def write_json(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# B3 Normalizer Transfer Audit",
        "",
        "This report asks when the B3 symmetry premium earns itself back.  A",
        "source support is fixed, held-out tasks are normalizer transforms of it,",
        "and policies are scored without seeing the target transform.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    for row in payload["rows"]:
        transfer = row["transfer_summary"]
        lines += [
            "",
            f"## {row['row']}",
            "",
            f"Winner by mean J: `{row['winner_by_mean_J']}`.",
            (
                "Normalizer beats source-minimal rate: "
                f"`{transfer['normalizer_beats_minimal_rate']:.3f}`."
            ),
            (
                "Mean structural gain / premium / net gain: "
                f"`{transfer['mean_structural_gain']:.6f}` / "
                f"`{transfer['mean_premium']:.6f}` / "
                f"`{transfer['mean_net_gain']:.6f}`."
            ),
            "",
            "| policy | mean J | wins | support | structural | resource | Fisher | reciprocal | closure | balance |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for name, summary in row["policies"].items():
            lines.append(
                "| {name} | {J:.6f} | {wins} | {support:.3f} | {structural:.6f} | "
                "{resource:.6f} | {fisher:.6f} | {reciprocal:.6f} | "
                "{closure:.6f} | {balance:.6f} |".format(
                    name=name,
                    J=summary["mean_J"],
                    wins=summary["wins"],
                    support=summary["mean_support_size"],
                    structural=summary["mean_structural_cost"],
                    resource=summary["mean_resource_cost"],
                    fisher=summary["mean_fisher_projection_error"],
                    reciprocal=summary["mean_reciprocal_projection_error"],
                    closure=summary["mean_closure_leakage"],
                    balance=summary["mean_descent_balance_cost"],
                )
            )

        lines += ["", "### Payoff Examples", ""]
        if not row["examples"]:
            lines.append("- none")
        for example in row["examples"]:
            lines.append(
                "- source `{source}` -> target `{target}`; minimal `{minimal}`; "
                "normalizer `{normalizer}`; J `{minimal_J:.6f}` -> `{normalizer_J:.6f}`; "
                "gain/premium `{gain:.6f}`/`{premium:.6f}`".format(
                    source=", ".join(example["source"]),
                    target=", ".join(example["target"]),
                    minimal=", ".join(example["source_minimal"]),
                    normalizer=", ".join(example["source_normalizer"]),
                    minimal_J=example["minimal_J"],
                    normalizer_J=example["normalizer_J"],
                    gain=example["structural_gain"],
                    premium=example["premium"],
                )
            )

    lines += [
        "",
        "## Reading",
        "",
        "When the deployment task is fixed, B2 minimal descent is cheaper.  When",
        "the deployment task is only known up to normalizer symmetry, B3 can",
        "outperform B2 because it buys all equivalent supports at once.  The",
        "break-even condition is structural transfer gain greater than the",
        "resource-weighted symmetry premium.",
    ]
    return "\n".join(lines) + "\n"


def write_report(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(payload), encoding="utf-8")


def check_payload(payload: dict[str, Any], path: Path) -> None:
    recorded = json.loads(path.read_text(encoding="utf-8"))
    if recorded != payload:
        raise AssertionError(f"payload differs from {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", default="c7,c8,c12,f4-u2,f2-u4")
    parser.add_argument("--source-tasks", type=int, default=64)
    parser.add_argument("--transfers-per-source", type=int, default=8)
    parser.add_argument("--max-source-size", type=int, default=2)
    parser.add_argument("--amplitude-min", type=float, default=0.15)
    parser.add_argument("--amplitude-max", type=float, default=0.45)
    parser.add_argument("--resource-weight", type=float, default=0.25)
    parser.add_argument("--seed", type=int, default=20260514)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", type=Path, default=None)
    args = parser.parse_args()

    payload = build_payload(args)
    if args.check is not None:
        check_payload(payload, args.check)
        print(f"checked {args.check}")
        return

    write_json(payload, args.json)
    write_report(payload, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
