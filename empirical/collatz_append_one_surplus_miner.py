"""Mine near-failures of the append-one surplus inequality.

The append-one block recurrence gives, for a contracting anchor w and a
contracting child w1^k,

    q_{w,1^k} = q_w
        + (D_{w,k} b - (3^k - 2^k) alpha) / 2^k,

where

    alpha = (y_w + 1) / 2,
    b == -alpha * (3^m)^-1 mod 2^k, 0 <= b < 2^k,
    D_{w,k}=2^(S+k)-3^(m+k).

Equivalently, append-one positivity is the exact integer inequality

    2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha.

This script ranks the reduced append-one channel by the scaled surplus

    Sigma(w,k) = 2^k q_{w,1^k}

which is exactly the difference between the two sides above.  The smallest
positive surpluses are the theorem-facing examples: they show which arithmetic
mechanism must be proved, not merely which chains have large drops.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from collatz_append_one_chain_miner import (
    block_data,
    bounded_compositions,
    trailing_ones,
)
from collatz_margin_theorem_candidate import LOG2_3, margin_data


@dataclass
class BucketStats:
    count: int = 0
    min_scaled_surplus: int | None = None
    min_example: dict[str, Any] | None = None


@dataclass
class RunStats:
    blocks: int = 0
    negative_q: int = 0
    zero_q: int = 0
    positive_q: int = 0
    b_zero: int = 0
    b_positive: int = 0
    q_support_sufficient: int = 0
    lift_needed: int = 0
    lift_needed_but_zero: int = 0
    min_scaled_surplus: int | None = None
    min_scaled_surplus_example: dict[str, Any] | None = None
    min_child_q: int | None = None
    min_child_q_example: dict[str, Any] | None = None
    max_drop: int | None = None
    max_drop_example: dict[str, Any] | None = None
    min_q_support_gap: int | None = None
    min_q_support_gap_example: dict[str, Any] | None = None
    max_q_support_deficit: int | None = None
    max_q_support_deficit_example: dict[str, Any] | None = None
    bucket_stats: dict[str, BucketStats] = field(default_factory=dict)
    bit_patterns: Counter[str] = field(default_factory=Counter)


def update_top_min(
    examples: list[dict[str, Any]],
    example: dict[str, Any],
    limit: int,
    key: str = "scaled_surplus",
) -> None:
    examples.append(example)
    examples.sort(key=lambda row: (int(row[key]), int(row["run"]), row["child_signature"]))
    del examples[limit:]


def update_bucket(bucket: BucketStats, example: dict[str, Any]) -> None:
    sigma = int(example["scaled_surplus"])
    bucket.count += 1
    if bucket.min_scaled_surplus is None or sigma < bucket.min_scaled_surplus:
        bucket.min_scaled_surplus = sigma
        bucket.min_example = example


def b_bucket(run: int, b: int) -> str:
    modulus = 1 << run
    if b == 0:
        return "zero"
    if b == modulus - 1:
        return "all_ones"
    if run == 1:
        return "one"
    if b * 4 < modulus:
        return "low_quarter"
    if b * 2 < modulus:
        return "lower_middle"
    if b * 4 < 3 * modulus:
        return "upper_middle"
    return "high_quarter"


def surplus_example(block: dict[str, Any]) -> dict[str, Any]:
    run = int(block["run"])
    q_support = (1 << run) * int(block["anchor_q"])
    lift_support = int(block["block_denominator"]) * int(block["block_lift_b"])
    obstruction = (3**run - (1 << run)) * int(block["alpha"])
    scaled_surplus = int(block["scaled_surplus"])
    if q_support + lift_support - obstruction != scaled_surplus:
        raise AssertionError("surplus decomposition failed")
    q_support_gap = q_support - obstruction
    bucket = b_bucket(run, int(block["block_lift_b"]))
    return {
        "anchor": block["anchor"],
        "anchor_signature": block["anchor_signature"],
        "child": block["child"],
        "child_signature": block["child_signature"],
        "run": run,
        "anchor_m": block["anchor_m"],
        "anchor_S": block["anchor_S"],
        "child_m": block["child_m"],
        "child_S": block["child_S"],
        "anchor_q": block["anchor_q"],
        "child_q": block["child_q"],
        "drop_from_anchor": block["drop_from_anchor"],
        "scaled_surplus": scaled_surplus,
        "q_support": q_support,
        "lift_support": lift_support,
        "obstruction": obstruction,
        "q_support_gap": q_support_gap,
        "support_mode": "q_support_sufficient"
        if q_support_gap >= 0
        else "lift_needed",
        "anchor_y": block["anchor_y"],
        "alpha": block["alpha"],
        "block_lift_b": block["block_lift_b"],
        "block_lift_bucket": bucket,
        "block_lift_bits_low_to_high": block["block_lift_bits_low_to_high"],
        "h": block["h"],
        "block_denominator": block["block_denominator"],
    }


def update_run_stats(stats: RunStats, example: dict[str, Any]) -> None:
    child_q = int(example["child_q"])
    sigma = int(example["scaled_surplus"])
    drop = int(example["drop_from_anchor"])
    q_gap = int(example["q_support_gap"])
    stats.blocks += 1
    if child_q < 0:
        stats.negative_q += 1
    elif child_q == 0:
        stats.zero_q += 1
    else:
        stats.positive_q += 1

    if int(example["block_lift_b"]) == 0:
        stats.b_zero += 1
    else:
        stats.b_positive += 1

    if q_gap >= 0:
        stats.q_support_sufficient += 1
        if stats.min_q_support_gap is None or q_gap < stats.min_q_support_gap:
            stats.min_q_support_gap = q_gap
            stats.min_q_support_gap_example = example
    else:
        stats.lift_needed += 1
        if int(example["block_lift_b"]) == 0:
            stats.lift_needed_but_zero += 1
        deficit = -q_gap
        if stats.max_q_support_deficit is None or deficit > stats.max_q_support_deficit:
            stats.max_q_support_deficit = deficit
            stats.max_q_support_deficit_example = example

    if stats.min_scaled_surplus is None or sigma < stats.min_scaled_surplus:
        stats.min_scaled_surplus = sigma
        stats.min_scaled_surplus_example = example
    if stats.min_child_q is None or child_q < stats.min_child_q:
        stats.min_child_q = child_q
        stats.min_child_q_example = example
    if stats.max_drop is None or drop > stats.max_drop:
        stats.max_drop = drop
        stats.max_drop_example = example

    bucket = stats.bucket_stats.setdefault(example["block_lift_bucket"], BucketStats())
    update_bucket(bucket, example)
    stats.bit_patterns[str(example["block_lift_bits_low_to_high"])] += 1


def bucket_stats_json(stats: BucketStats) -> dict[str, Any]:
    return {
        "count": stats.count,
        "min_scaled_surplus": stats.min_scaled_surplus,
        "min_example": stats.min_example,
    }


def run_stats_json(stats: RunStats, top_patterns: int) -> dict[str, Any]:
    return {
        "blocks": stats.blocks,
        "negative_q": stats.negative_q,
        "zero_q": stats.zero_q,
        "positive_q": stats.positive_q,
        "b_zero": stats.b_zero,
        "b_positive": stats.b_positive,
        "q_support_sufficient": stats.q_support_sufficient,
        "lift_needed": stats.lift_needed,
        "lift_needed_but_zero": stats.lift_needed_but_zero,
        "min_scaled_surplus": stats.min_scaled_surplus,
        "min_scaled_surplus_example": stats.min_scaled_surplus_example,
        "min_child_q": stats.min_child_q,
        "min_child_q_example": stats.min_child_q_example,
        "max_drop": stats.max_drop,
        "max_drop_example": stats.max_drop_example,
        "min_q_support_gap": stats.min_q_support_gap,
        "min_q_support_gap_example": stats.min_q_support_gap_example,
        "max_q_support_deficit": stats.max_q_support_deficit,
        "max_q_support_deficit_example": stats.max_q_support_deficit_example,
        "bucket_stats": {
            bucket: bucket_stats_json(bucket_stats)
            for bucket, bucket_stats in sorted(stats.bucket_stats.items())
        },
        "top_bit_patterns": [
            {"pattern": pattern, "count": count}
            for pattern, count in stats.bit_patterns.most_common(top_patterns)
        ],
    }


def enumerate_surpluses(
    *,
    max_length: int,
    max_total_depth: int,
    max_carry: int,
    top_examples: int,
    top_patterns: int,
) -> dict[str, Any]:
    data_by_word: dict[tuple[int, ...], dict[str, Any] | None] = {}
    by_run: dict[int, RunStats] = {}
    global_min_surpluses: list[dict[str, Any]] = []
    global_lift_needed_min_surpluses: list[dict[str, Any]] = []
    global_b_zero_min_surpluses: list[dict[str, Any]] = []
    totals = {
        "words": 0,
        "contracting_words": 0,
        "append_one_blocks": 0,
        "negative_q_words": 0,
        "zero_q_words": 0,
        "trivial_zero_words": 0,
        "positive_q_words": 0,
        "decomposition_failures": 0,
    }

    for length in range(1, max_length + 1):
        for total_depth in range(length, max_total_depth + 1):
            if total_depth > length * max_carry:
                continue
            for word in bounded_compositions(total_depth, length, max_carry):
                totals["words"] += 1
                data = margin_data(word)
                data_by_word[word] = data
                if data is None:
                    continue

                totals["contracting_words"] += 1
                q = int(data["q_int"])
                if q < 0:
                    totals["negative_q_words"] += 1
                elif q == 0:
                    totals["zero_q_words"] += 1
                    if all(carry == 2 for carry in word):
                        totals["trivial_zero_words"] += 1
                else:
                    totals["positive_q_words"] += 1

                run = trailing_ones(word)
                if not run or len(word) == run:
                    continue
                anchor = word[:-run]
                anchor_data = data_by_word.get(anchor)
                if anchor_data is None:
                    continue

                block = block_data(anchor, run, word, anchor_data, data)
                if not block["ok"]:
                    totals["decomposition_failures"] += 1
                    continue
                example = surplus_example(block)
                stats = by_run.setdefault(run, RunStats())
                update_run_stats(stats, example)
                totals["append_one_blocks"] += 1
                update_top_min(global_min_surpluses, example, top_examples)
                if example["support_mode"] == "lift_needed":
                    update_top_min(
                        global_lift_needed_min_surpluses,
                        example,
                        top_examples,
                    )
                if int(example["block_lift_b"]) == 0:
                    update_top_min(
                        global_b_zero_min_surpluses,
                        example,
                        top_examples,
                    )

    return {
        "totals": totals,
        "by_run": {
            str(run): run_stats_json(stats, top_patterns)
            for run, stats in sorted(by_run.items())
        },
        "global_min_surpluses": global_min_surpluses,
        "global_lift_needed_min_surpluses": global_lift_needed_min_surpluses,
        "global_b_zero_min_surpluses": global_b_zero_min_surpluses,
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


def number_or_dash(value: object) -> str:
    return "-" if value is None else str(value)


def make_run_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| k | blocks | q < 0 | b=0 | lift needed | q support enough | min Sigma | min child q | max drop | min-Sigma word |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for run in sorted(rows, key=lambda item: int(item)):
        row = rows[run]
        example = row["min_scaled_surplus_example"]
        signature = "-" if example is None else f"`{example['child_signature']}`"
        lines.append(
            f"| {run} | {row['blocks']} | {row['negative_q']} | "
            f"{row['b_zero']} | {row['lift_needed']} | "
            f"{row['q_support_sufficient']} | "
            f"{number_or_dash(row['min_scaled_surplus'])} | "
            f"{number_or_dash(row['min_child_q'])} | "
            f"{number_or_dash(row['max_drop'])} | {signature} |"
        )
    return lines


def make_near_failure_table(title: str, examples: list[dict[str, Any]]) -> list[str]:
    lines = [
        title,
        "",
        "| Sigma | k | child q | child | anchor q | drop | b | bits | mode | q gap | lift | obstruction |",
        "|---:|---:|---:|---|---:|---:|---:|---|---|---:|---:|---:|",
    ]
    if not examples:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - | - |")
        return lines
    for example in examples:
        lines.append(
            f"| {example['scaled_surplus']} | {example['run']} | "
            f"{example['child_q']} | `{example['child_signature']}` | "
            f"{example['anchor_q']} | {example['drop_from_anchor']} | "
            f"{example['block_lift_b']} | `{example['block_lift_bits_low_to_high']}` | "
            f"{example['support_mode']} | {example['q_support_gap']} | "
            f"{example['lift_support']} | {example['obstruction']} |"
        )
    return lines


def make_bucket_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| k | bucket | count | min Sigma | min-Sigma word |",
        "|---:|---|---:|---:|---|",
    ]
    for run in sorted(rows, key=lambda item: int(item)):
        bucket_rows = rows[run]["bucket_stats"]
        for bucket in sorted(bucket_rows):
            row = bucket_rows[bucket]
            example = row["min_example"]
            signature = "-" if example is None else f"`{example['child_signature']}`"
            lines.append(
                f"| {run} | `{bucket}` | {row['count']} | "
                f"{number_or_dash(row['min_scaled_surplus'])} | {signature} |"
            )
    return lines


def make_pattern_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| k | most common lift-bit patterns |",
        "|---:|---|",
    ]
    for run in sorted(rows, key=lambda item: int(item)):
        patterns = rows[run]["top_bit_patterns"]
        if not patterns:
            text = "-"
        else:
            text = ", ".join(
                f"`{row['pattern']}` ({row['count']})" for row in patterns
            )
        lines.append(f"| {run} | {text} |")
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    results = payload["results"]
    totals = results["totals"]
    lines = [
        "# Collatz Append-One Surplus Miner",
        "",
        "## Meaning",
        "",
        "The append-one block recurrence reduces the remaining suffix channel to the exact inequality",
        "",
        "```text",
        "2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha.",
        "```",
        "",
        "This report ranks append-one blocks by the scaled surplus",
        "",
        "```text",
        "Sigma(w,k) = 2^k q_{w,1^k}",
        "```",
        "",
        "which is exactly the difference between the two sides of the inequality.  Small `Sigma` examples are the near-failures that a proof has to explain.",
        "",
        "## Settings",
        "",
        f"- max length: `{settings['max_length']}`",
        f"- max total carry depth: `{settings['max_total_depth']}`",
        f"- carry alphabet: `1..{settings['max_carry']}`",
        f"- retained examples per list: `{settings['top_examples']}`",
        "",
        "## Verification",
        "",
        f"- words scanned: `{totals['words']}`",
        f"- contracting words: `{totals['contracting_words']}`",
        f"- append-one blocks: `{totals['append_one_blocks']}`",
        f"- decomposition failures: `{totals['decomposition_failures']}`",
        f"- negative q words: `{totals['negative_q_words']}`",
        f"- zero q words: `{totals['zero_q_words']}`",
        f"- trivial zero words: `{totals['trivial_zero_words']}`",
        f"- positive q words: `{totals['positive_q_words']}`",
        "",
        "## Surplus Ledger By Run Length",
        "",
        *make_run_table(results["by_run"]),
        "",
        *make_near_failure_table(
            "Smallest global scaled surpluses:",
            results["global_min_surpluses"],
        ),
        "",
        *make_near_failure_table(
            "Smallest surpluses where lift support is needed:",
            results["global_lift_needed_min_surpluses"],
        ),
        "",
        *make_near_failure_table(
            "Smallest surpluses with zero block lift `b=0`:",
            results["global_b_zero_min_surpluses"],
        ),
        "",
        "## Lift Residue Buckets",
        "",
        "Buckets are only descriptive: `zero`, `all_ones`, and quartiles of `0 < b < 2^k-1`.  They help separate no-lift drops from cases where `D_{w,k} b` supplies the missing positivity.",
        "",
        *make_bucket_table(results["by_run"]),
        "",
        "## Common Lift-Bit Patterns",
        "",
        "The bit strings are low-to-high, so the first character is the first appended-one lift digit.",
        "",
        *make_pattern_table(results["by_run"]),
        "",
        "## Proof-Facing Read",
        "",
        "The support decomposition is",
        "",
        "```text",
        "Sigma = 2^k q_w + D_{w,k} b - (3^k - 2^k) alpha.",
        "```",
        "",
        "If `2^k q_w >= (3^k - 2^k) alpha`, positivity is already supplied by the anchor margin.  Otherwise the proof must use the forced lift residue `b`; those are the `lift_needed` rows.  The `b=0` rows are the opposite extreme: no lift support is available, so their positivity must come entirely from prior margin.",
        "",
        "This is still not a proof of Collatz.  It isolates the append-one channel into exact near-failure families for the next local lemma.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_append_one_surplus_miner.py "
        f"--max-length {settings['max_length']} "
        f"--max-total-depth {settings['max_total_depth']} "
        f"--max-carry {settings['max_carry']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, max_total_depth: int, max_carry: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_append_one_surplus_L{max_length}_S{max_total_depth}_K{max_carry}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_append_one_surplus_L{max_length}_S{max_total_depth}_K{max_carry}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=8)
    parser.add_argument("--max-total-depth", type=int, default=21)
    parser.add_argument("--max-carry", type=int, default=8)
    parser.add_argument("--top-examples", type=int, default=12)
    parser.add_argument("--top-patterns", type=int, default=6)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 2:
        raise ValueError("--max-length must be at least 2")
    if args.max_total_depth < args.max_length:
        raise ValueError("--max-total-depth must be at least max-length")
    if args.max_carry < 2:
        raise ValueError("--max-carry must be at least 2")
    if args.top_examples < 1:
        raise ValueError("--top-examples must be positive")
    if args.top_patterns < 1:
        raise ValueError("--top-patterns must be positive")

    results = enumerate_surpluses(
        max_length=args.max_length,
        max_total_depth=args.max_total_depth,
        max_carry=args.max_carry,
        top_examples=args.top_examples,
        top_patterns=args.top_patterns,
    )
    payload = {
        "settings": {
            "max_length": args.max_length,
            "max_total_depth": args.max_total_depth,
            "max_carry": args.max_carry,
            "top_examples": args.top_examples,
            "top_patterns": args.top_patterns,
            "height_threshold": LOG2_3,
        },
        "results": results,
    }

    report_path = args.report or default_report_path(
        args.max_length,
        args.max_total_depth,
        args.max_carry,
    )
    json_path = args.json or default_json_path(
        args.max_length,
        args.max_total_depth,
        args.max_carry,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(results["global_min_surpluses"]), indent=2))


if __name__ == "__main__":
    main()
