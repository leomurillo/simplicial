"""Search for failures of the append-one one-copy bound.

The lift-channel note suggested the possible bound

    E <= D_k

inside the lift-supported channel.  That bound would make the copy demand
N=ceil(E/D_k) equal to 1.  It is false in general.

This script searches small anchors w and appended blocks 1^k for exact
counterexamples with N > 1.  These are not counterexamples to append-one
positivity: they still satisfy the true copy-cover inequality N <= b in the
checked examples.  They are counterexamples only to the proposed one-copy
shortcut.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from collatz_append_one_chain_miner import block_data, bounded_compositions
from collatz_append_one_lift_channel_miner import lift_example
from collatz_append_one_surplus_miner import surplus_example
from collatz_margin_theorem_candidate import LOG2_3, margin_data, word_signature


@dataclass
class CounterexampleStats:
    anchors_scanned: int = 0
    contracting_anchors: int = 0
    children_checked: int = 0
    lift_supported_children: int = 0
    one_copy_failures: int = 0
    forced_cover_failures: int = 0
    max_needed_copies: int | None = None
    max_needed_example: dict[str, Any] | None = None
    min_failure: dict[str, Any] | None = None
    smallest_surplus_failure: dict[str, Any] | None = None


def carry_word_json(word: tuple[int, ...]) -> list[int]:
    return list(word)


def update_top_failures(
    rows: list[dict[str, Any]],
    example: dict[str, Any],
    limit: int,
) -> None:
    rows.append(example)
    rows.sort(
        key=lambda row: (
            int(row["run"]),
            int(row["anchor_S"]),
            int(row["anchor_m"]),
            row["anchor_signature"],
        )
    )
    del rows[limit:]


def update_minima(stats: CounterexampleStats, example: dict[str, Any]) -> None:
    needed = int(example["lift_copies_needed"])
    if stats.max_needed_copies is None or needed > stats.max_needed_copies:
        stats.max_needed_copies = needed
        stats.max_needed_example = example
    if stats.min_failure is None or (
        int(example["run"]),
        int(example["anchor_S"]),
        int(example["anchor_m"]),
        example["anchor_signature"],
    ) < (
        int(stats.min_failure["run"]),
        int(stats.min_failure["anchor_S"]),
        int(stats.min_failure["anchor_m"]),
        stats.min_failure["anchor_signature"],
    ):
        stats.min_failure = example
    if stats.smallest_surplus_failure is None or int(
        example["scaled_surplus"]
    ) < int(stats.smallest_surplus_failure["scaled_surplus"]):
        stats.smallest_surplus_failure = example


def enumerate_anchor_words(
    *,
    max_anchor_length: int,
    max_anchor_total_depth: int,
    max_carry: int,
) -> Iterable[tuple[int, ...]]:
    for length in range(1, max_anchor_length + 1):
        for total_depth in range(length, max_anchor_total_depth + 1):
            if total_depth > length * max_carry:
                continue
            yield from bounded_compositions(total_depth, length, max_carry)


def counterexample_row(
    anchor: tuple[int, ...],
    run: int,
    child: tuple[int, ...],
    example: dict[str, Any],
) -> dict[str, Any]:
    row = dict(example)
    row["anchor"] = carry_word_json(anchor)
    row["child"] = carry_word_json(child)
    row["anchor_signature"] = word_signature(anchor)
    row["child_signature"] = word_signature(child)
    row["one_copy_bound_holds"] = int(row["deficit"]) <= int(row["block_denominator"])
    return row


def search_counterexamples(
    *,
    max_anchor_length: int,
    max_anchor_total_depth: int,
    max_carry: int,
    max_run: int,
    top_examples: int,
) -> dict[str, Any]:
    stats = CounterexampleStats()
    failures: list[dict[str, Any]] = []
    lift_examples: list[dict[str, Any]] = []

    for anchor in enumerate_anchor_words(
        max_anchor_length=max_anchor_length,
        max_anchor_total_depth=max_anchor_total_depth,
        max_carry=max_carry,
    ):
        stats.anchors_scanned += 1
        anchor_data = margin_data(anchor)
        if anchor_data is None:
            continue
        stats.contracting_anchors += 1
        for run in range(1, max_run + 1):
            child = anchor + ((1,) * run)
            child_data = margin_data(child)
            if child_data is None:
                continue
            stats.children_checked += 1
            block = block_data(anchor, run, child, anchor_data, child_data)
            if not block["ok"]:
                raise AssertionError("block recurrence failed")
            surplus = surplus_example(block)
            if surplus["support_mode"] != "lift_needed":
                continue
            stats.lift_supported_children += 1
            lift = lift_example(block)
            row = counterexample_row(anchor, run, child, lift)
            if len(lift_examples) < top_examples:
                lift_examples.append(row)
            if not row["forced_cover_ok"]:
                stats.forced_cover_failures += 1
            if int(row["lift_copies_needed"]) > 1:
                stats.one_copy_failures += 1
                update_minima(stats, row)
                update_top_failures(failures, row, top_examples)

    return {
        "totals": {
            "anchors_scanned": stats.anchors_scanned,
            "contracting_anchors": stats.contracting_anchors,
            "children_checked": stats.children_checked,
            "lift_supported_children": stats.lift_supported_children,
            "one_copy_failures": stats.one_copy_failures,
            "forced_cover_failures": stats.forced_cover_failures,
            "max_needed_copies": stats.max_needed_copies,
            "max_needed_example": stats.max_needed_example,
            "min_failure": stats.min_failure,
            "smallest_surplus_failure": stats.smallest_surplus_failure,
        },
        "one_copy_failures": failures,
        "sample_lift_supported_children": lift_examples,
    }


def rounded(value: object) -> object:
    if isinstance(value, float):
        if math.isinf(value):
            return "inf" if value > 0 else "-inf"
        return round(value, 12)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    return value


def make_example_table(title: str, examples: list[dict[str, Any]]) -> list[str]:
    lines = [
        title,
        "",
        "| child | anchor | k | b | N | spare | E | D_k | Sigma | alpha | q anchor |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    if not examples:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - |")
        return lines
    for example in examples:
        lines.append(
            f"| `{example['child_signature']}` | `{example['anchor_signature']}` | "
            f"{example['run']} | {example['block_lift_b']} | "
            f"{example['lift_copies_needed']} | {example['spare_lift_copies']} | "
            f"{example['deficit']} | {example['block_denominator']} | "
            f"{example['scaled_surplus']} | {example['alpha']} | "
            f"{example['anchor_q']} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    results = payload["results"]
    totals = results["totals"]
    lines = [
        "# Collatz Append-One One-Copy Counterexamples",
        "",
        "## Meaning",
        "",
        "This report tests the proposed one-copy bound in the lift-supported append-one channel:",
        "",
        "```text",
        "E <= D_k.",
        "```",
        "",
        "The bound is useful because it implies `N=ceil(E/D_k)=1`; since lift-supported cases have `b>0`, one copy of `D_k` would cover the deficit.  The search below shows that this shortcut is false in general.",
        "",
        "The true local condition remains",
        "",
        "```text",
        "N <= b.",
        "```",
        "",
        "## Settings",
        "",
        f"- max anchor length: `{settings['max_anchor_length']}`",
        f"- max anchor total depth: `{settings['max_anchor_total_depth']}`",
        f"- carry alphabet: `1..{settings['max_carry']}`",
        f"- max appended-one run: `{settings['max_run']}`",
        "",
        "## Verification",
        "",
        f"- anchors scanned: `{totals['anchors_scanned']}`",
        f"- contracting anchors: `{totals['contracting_anchors']}`",
        f"- children checked: `{totals['children_checked']}`",
        f"- lift-supported children: `{totals['lift_supported_children']}`",
        f"- one-copy failures: `{totals['one_copy_failures']}`",
        f"- forced-cover failures: `{totals['forced_cover_failures']}`",
        f"- max required copies: `{totals['max_needed_copies']}`",
        "",
        *make_example_table(
            "Earliest one-copy failures:",
            results["one_copy_failures"],
        ),
        "",
        "## Explicit Disproof",
        "",
        "The smallest failure is already",
        "",
        "```text",
        "anchor w = (4), appended block 1^4.",
        "```",
        "",
        "For this block:",
        "",
        "```text",
        "q_w = 2, alpha = 1, D_k = 13, b = 5,",
        "E = (3^4 - 2^4)alpha - 2^4 q_w = 65 - 32 = 33.",
        "```",
        "",
        "So `E=33 > 13=D_k`, and the one-copy bound fails.  The child still has positive surplus because",
        "",
        "```text",
        "D_k b - E = 13*5 - 33 = 32.",
        "```",
        "",
        "The right target is therefore not the universal one-copy bound.  It is the copy-cover inequality `N <= b`, possibly with a one-copy sublemma for the majority channel and a separate multi-copy channel.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_append_one_lift_counterexample_miner.py "
        f"--max-anchor-length {settings['max_anchor_length']} "
        f"--max-anchor-total-depth {settings['max_anchor_total_depth']} "
        f"--max-carry {settings['max_carry']} "
        f"--max-run {settings['max_run']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(
    max_anchor_length: int,
    max_anchor_total_depth: int,
    max_carry: int,
    max_run: int,
) -> Path:
    return (
        Path("empirical/reports")
        / (
            "collatz_append_one_lift_counterexamples_"
            f"A{max_anchor_length}_S{max_anchor_total_depth}_"
            f"K{max_carry}_R{max_run}.md"
        )
    )


def default_json_path(
    max_anchor_length: int,
    max_anchor_total_depth: int,
    max_carry: int,
    max_run: int,
) -> Path:
    return (
        Path("empirical/reports")
        / (
            "collatz_append_one_lift_counterexamples_"
            f"A{max_anchor_length}_S{max_anchor_total_depth}_"
            f"K{max_carry}_R{max_run}.json"
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-anchor-length", type=int, default=4)
    parser.add_argument("--max-anchor-total-depth", type=int, default=16)
    parser.add_argument("--max-carry", type=int, default=10)
    parser.add_argument("--max-run", type=int, default=30)
    parser.add_argument("--top-examples", type=int, default=20)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_anchor_length < 1:
        raise ValueError("--max-anchor-length must be positive")
    if args.max_anchor_total_depth < args.max_anchor_length:
        raise ValueError("--max-anchor-total-depth must be at least max anchor length")
    if args.max_carry < 2:
        raise ValueError("--max-carry must be at least 2")
    if args.max_run < 1:
        raise ValueError("--max-run must be positive")
    if args.top_examples < 1:
        raise ValueError("--top-examples must be positive")

    results = search_counterexamples(
        max_anchor_length=args.max_anchor_length,
        max_anchor_total_depth=args.max_anchor_total_depth,
        max_carry=args.max_carry,
        max_run=args.max_run,
        top_examples=args.top_examples,
    )
    payload = {
        "settings": {
            "max_anchor_length": args.max_anchor_length,
            "max_anchor_total_depth": args.max_anchor_total_depth,
            "max_carry": args.max_carry,
            "max_run": args.max_run,
            "top_examples": args.top_examples,
            "height_threshold": LOG2_3,
        },
        "results": results,
    }

    report_path = args.report or default_report_path(
        args.max_anchor_length,
        args.max_anchor_total_depth,
        args.max_carry,
        args.max_run,
    )
    json_path = args.json or default_json_path(
        args.max_anchor_length,
        args.max_anchor_total_depth,
        args.max_carry,
        args.max_run,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(results["totals"]), indent=2))


if __name__ == "__main__":
    main()
