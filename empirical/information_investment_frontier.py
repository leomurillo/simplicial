"""Held-out frontier audit for the B0 information-investment functional.

The single-row B0 prototype asks whether a candidate support wins on one
hand-picked finite task.  This script moves one step toward A0: sample many
finite behavior tasks, learn aggregate low-rank supports on train tasks, and
compare those learned baselines against descent/conductor closures on held-out
tasks under the same support budget.
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
    allowed_reciprocal_modes,
    build_rows,
    conductor_packet_support,
    cyclic_descent_closure,
    dft,
    local_descent_closure,
    normalizer_saturation,
    random_support,
    reciprocal_density_from_support,
    score_candidate,
)


Mode = Hashable
DEFAULT_JSON = Path("empirical/reports/information_investment_frontier.json")
DEFAULT_REPORT = Path("empirical/reports/information_investment_frontier.md")


def descent_closure(row: FiniteRow, support: set[Mode]) -> set[Mode]:
    if row.key.startswith("c"):
        return cyclic_descent_closure(row, support)
    return local_descent_closure(row, support)


def random_task_support(row: FiniteRow, rng: random.Random) -> set[Mode]:
    nonzero = list(row.nonzero_modes)
    if row.key.startswith("c"):
        n = len(row.labels)
        base = int(rng.choice(nonzero))
        partner = (-base) % n
        return {base} if partner == base else {base, partner}

    conductors = sorted({row.conductor(mode) for mode in nonzero})
    conductor = rng.choice(conductors)
    packet = [mode for mode in nonzero if row.conductor(mode) == conductor]
    if len(packet) <= 3 or rng.random() < 0.5:
        return set(packet)
    size = rng.randint(1, min(3, len(packet)))
    return set(rng.sample(packet, size))


def task_coefficients(
    row: FiniteRow,
    support: set[Mode],
    amplitude: float,
) -> tuple[dict[Mode, complex], dict[Mode, complex]]:
    reciprocal, probability = reciprocal_density_from_support(row, support, amplitude)
    uniform = 1.0 / len(row.labels)
    tangent = {label: probability[label] - uniform for label in row.labels}
    return dft(row, tangent), dft(row, reciprocal)


def train_energy_ranking(
    row: FiniteRow,
    task_supports: list[set[Mode]],
    amplitudes: list[float],
) -> list[Mode]:
    aggregate: dict[Mode, float] = defaultdict(float)
    for support, amplitude in zip(task_supports, amplitudes):
        h_hat, _ = task_coefficients(row, support, amplitude)
        for mode in row.nonzero_modes:
            aggregate[mode] += abs(h_hat[mode]) ** 2
    return sorted(row.nonzero_modes, key=lambda mode: (-aggregate[mode], row.label_name(mode)))


def learned_support(ranking: list[Mode], size: int) -> set[Mode]:
    return set(ranking[:size])


def summarize_policy(records: list[dict[str, float]]) -> dict[str, float]:
    count = len(records)
    out: dict[str, float] = {"count": float(count)}
    for key in [
        "J",
        "fisher_projection_error",
        "reciprocal_projection_error",
        "closure_leakage",
        "descent_balance_cost",
        "resource_cost",
        "support_size",
    ]:
        out[f"mean_{key}"] = sum(record[key] for record in records) / count
    return out


def run_row(
    row: FiniteRow,
    *,
    train_tasks: int,
    test_tasks: int,
    amplitude_min: float,
    amplitude_max: float,
    resource_weight: float,
    seed: int,
) -> dict[str, Any]:
    rng = random.Random(seed)
    train_supports = [random_task_support(row, rng) for _ in range(train_tasks)]
    train_amplitudes = [rng.uniform(amplitude_min, amplitude_max) for _ in range(train_tasks)]
    ranking = train_energy_ranking(row, train_supports, train_amplitudes)

    policy_records: dict[str, list[dict[str, float]]] = defaultdict(list)
    wins: dict[str, int] = defaultdict(int)
    examples: list[dict[str, Any]] = []

    for index in range(test_tasks):
        support = random_task_support(row, rng)
        amplitude = rng.uniform(amplitude_min, amplitude_max)
        h_hat, m_hat = task_coefficients(row, support, amplitude)
        raw_size = len(support)
        descent = descent_closure(row, support)
        descent_size = len(descent)

        policies = {
            "raw_support": support,
            "descent_closure": descent,
            "normalizer_saturation": normalizer_saturation(row, support),
            "conductor_packet": conductor_packet_support(row, support),
            "allowed_reciprocal": allowed_reciprocal_modes(row),
            "learned_top_raw_k": learned_support(ranking, raw_size),
            "learned_top_descent_k": learned_support(ranking, descent_size),
            "random_raw_k": random_support(row, raw_size, seed + 1000 + index),
            "random_descent_k": random_support(row, descent_size, seed + 2000 + index),
            "full": set(row.nonzero_modes),
        }

        scored: list[dict[str, Any]] = []
        for name, candidate_support in policies.items():
            score = score_candidate(row, candidate_support, h_hat, m_hat, resource_weight)
            record = {**score, "support_size": float(len(candidate_support))}
            policy_records[name].append(record)
            scored.append({"name": name, **record})

        scored.sort(key=lambda item: (item["J"], item["resource_cost"], item["name"]))
        wins[scored[0]["name"]] += 1
        if len(examples) < 5:
            examples.append(
                {
                    "active_support": [
                        row.label_name(mode) for mode in sorted(support, key=row.label_name)
                    ],
                    "descent_closure": [
                        row.label_name(mode) for mode in sorted(descent, key=row.label_name)
                    ],
                    "winner": scored[0]["name"],
                    "winner_J": scored[0]["J"],
                    "learned_top_descent_k": [
                        row.label_name(mode)
                        for mode in sorted(policies["learned_top_descent_k"], key=row.label_name)
                    ],
                }
            )

    policies = {
        name: {
            **summarize_policy(records),
            "wins": wins.get(name, 0),
        }
        for name, records in policy_records.items()
    }
    ordered = sorted(policies.items(), key=lambda item: (item[1]["mean_J"], item[0]))
    return {
        "key": row.key,
        "row": row.name,
        "label_count": len(row.labels),
        "train_tasks": train_tasks,
        "test_tasks": test_tasks,
        "learned_energy_ranking_prefix": [
            row.label_name(mode) for mode in ranking[: min(8, len(ranking))]
        ],
        "policies": {name: summary for name, summary in ordered},
        "winner_by_mean_J": ordered[0][0],
        "examples": examples,
    }


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    row_keys = [key.strip() for key in args.rows.split(",") if key.strip()]
    rows = []
    for offset, row in enumerate(build_rows(row_keys)):
        rows.append(
            run_row(
                row,
                train_tasks=args.train_tasks,
                test_tasks=args.test_tasks,
                amplitude_min=args.amplitude_min,
                amplitude_max=args.amplitude_max,
                resource_weight=args.resource_weight,
                seed=args.seed + 100 * offset,
            )
        )
    return {
        "purpose": (
            "Held-out frontier audit for B0: compare descent/conductor supports "
            "against learned aggregate low-rank supports on exact finite tasks."
        ),
        "config": {
            "rows": row_keys,
            "train_tasks": args.train_tasks,
            "test_tasks": args.test_tasks,
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
        "# B0 Information-Investment Frontier Audit",
        "",
        "This report tests B0 beyond one hand-picked task.  For each finite row,",
        "it samples train tasks, learns aggregate top-energy supports, then",
        "scores policies on held-out tasks under the same information-investment",
        "functional.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    for row in payload["rows"]:
        lines += [
            "",
            f"## {row['row']}",
            "",
            f"Winner by mean J: `{row['winner_by_mean_J']}`.",
            f"Learned energy ranking prefix: `{', '.join(row['learned_energy_ranking_prefix'])}`.",
            "",
            "| policy | mean J | wins | support | Fisher | reciprocal | closure | balance | resource |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for name, summary in row["policies"].items():
            lines.append(
                "| {name} | {J:.6f} | {wins} | {support:.3f} | {fisher:.6f} | "
                "{reciprocal:.6f} | {closure:.6f} | {balance:.6f} | {resource:.6f} |".format(
                    name=name,
                    J=summary["mean_J"],
                    wins=summary["wins"],
                    support=summary["mean_support_size"],
                    fisher=summary["mean_fisher_projection_error"],
                    reciprocal=summary["mean_reciprocal_projection_error"],
                    closure=summary["mean_closure_leakage"],
                    balance=summary["mean_descent_balance_cost"],
                    resource=summary["mean_resource_cost"],
                )
            )

        lines += ["", "### Example Held-Out Tasks", ""]
        for example in row["examples"]:
            lines.append(
                "- active `{active}` -> descent `{descent}`; winner `{winner}`; "
                "learned-top-descent `{learned}`".format(
                    active=", ".join(example["active_support"]),
                    descent=", ".join(example["descent_closure"]),
                    winner=example["winner"],
                    learned=", ".join(example["learned_top_descent_k"]),
                )
            )

    lines += [
        "",
        "## Reading",
        "",
        "`learned_top_descent_k` is the key baseline: it receives the same support",
        "budget as `descent_closure`, but chooses modes from aggregate train-task",
        "Fisher energy.  When descent closure wins, B0 is detecting a structural",
        "balance-transfer mode that energy ranking alone can miss.",
        "`normalizer_saturation` is the symmetry-complete policy: it may be worth",
        "buying when equivariance matters, but B3 tracks that extra cost",
        "separately from minimal subgroup descent.",
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
    parser.add_argument("--rows", default="c7,c8,c12,f4-u2")
    parser.add_argument("--train-tasks", type=int, default=48)
    parser.add_argument("--test-tasks", type=int, default=48)
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
