"""Mine the rare lift-supported append-one channel.

The append-one surplus split is

    Sigma = 2^k q_w + D_k b - (3^k - 2^k) alpha,

where Sigma = 2^k q_{w,1^k}.  Most append-one blocks are already handled by
anchor support:

    2^k q_w >= (3^k - 2^k) alpha.

This script isolates the complementary lift-supported channel, where the
deficit

    E = (3^k - 2^k) alpha - 2^k q_w

is positive and must be covered by the forced lift term D_k b.  The useful
integer is the lift-copy demand

    N = ceil(E / D_k).

In the lift-supported channel, append-one positivity is equivalent to

    N <= b.

The point of this miner is not to prove that inequality, but to identify how
large N gets, which small-b patterns are genuinely dangerous, and whether the
rare channel collapses to a small set of arithmetic families.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from collatz_append_one_chain_miner import (
    block_data,
    bounded_compositions,
    trailing_ones,
)
from collatz_append_one_surplus_miner import surplus_example
from collatz_margin_theorem_candidate import LOG2_3, margin_data


@dataclass
class LiftRunStats:
    total_lift_cases: int = 0
    alpha_one: int = 0
    alpha_gt_one: int = 0
    one_copy_covers: int = 0
    multi_copy_needed: int = 0
    forced_cover_failures: int = 0
    min_scaled_surplus: int | None = None
    min_scaled_surplus_example: dict[str, Any] | None = None
    min_spare_copies: int | None = None
    min_spare_copies_example: dict[str, Any] | None = None
    max_needed_copies: int | None = None
    max_needed_copies_example: dict[str, Any] | None = None
    max_deficit: int | None = None
    max_deficit_example: dict[str, Any] | None = None
    b_counter: Counter[int] = field(default_factory=Counter)
    needed_counter: Counter[int] = field(default_factory=Counter)
    alpha_counter: Counter[int] = field(default_factory=Counter)
    bit_counter: Counter[str] = field(default_factory=Counter)


def ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return (numerator + denominator - 1) // denominator


def update_top_min(
    rows: list[dict[str, Any]],
    example: dict[str, Any],
    limit: int,
    key: str,
) -> None:
    rows.append(example)
    rows.sort(
        key=lambda row: (
            int(row[key]),
            int(row["run"]),
            int(row["block_lift_b"]),
            row["child_signature"],
        )
    )
    del rows[limit:]


def lift_example(block: dict[str, Any]) -> dict[str, Any]:
    base = surplus_example(block)
    if base["support_mode"] != "lift_needed":
        raise ValueError("not a lift-supported example")
    deficit = -int(base["q_support_gap"])
    block_denominator = int(base["block_denominator"])
    lift_copies_needed = ceil_div(deficit, block_denominator)
    block_lift_b = int(base["block_lift_b"])
    spare_copies = block_lift_b - lift_copies_needed
    copy_cover_surplus = block_lift_b * block_denominator - deficit
    if copy_cover_surplus != int(base["scaled_surplus"]):
        raise AssertionError("copy cover surplus mismatch")
    if block_lift_b <= 0:
        raise AssertionError("lift-supported case cannot have b=0")

    row = dict(base)
    row.update(
        {
            "deficit": deficit,
            "lift_copies_needed": lift_copies_needed,
            "spare_lift_copies": spare_copies,
            "one_copy_covers": lift_copies_needed == 1,
            "copy_cover_surplus": copy_cover_surplus,
            "forced_cover_ok": spare_copies >= 0,
            "small_b": block_lift_b <= 8,
            "alpha_one": int(base["alpha"]) == 1,
        }
    )
    return row


def update_lift_run_stats(stats: LiftRunStats, example: dict[str, Any]) -> None:
    sigma = int(example["scaled_surplus"])
    deficit = int(example["deficit"])
    needed = int(example["lift_copies_needed"])
    spare = int(example["spare_lift_copies"])
    alpha = int(example["alpha"])
    b = int(example["block_lift_b"])
    bits = str(example["block_lift_bits_low_to_high"])

    stats.total_lift_cases += 1
    if alpha == 1:
        stats.alpha_one += 1
    else:
        stats.alpha_gt_one += 1
    if needed == 1:
        stats.one_copy_covers += 1
    else:
        stats.multi_copy_needed += 1
    if spare < 0:
        stats.forced_cover_failures += 1

    stats.b_counter[b] += 1
    stats.needed_counter[needed] += 1
    stats.alpha_counter[alpha] += 1
    stats.bit_counter[bits] += 1

    if stats.min_scaled_surplus is None or sigma < stats.min_scaled_surplus:
        stats.min_scaled_surplus = sigma
        stats.min_scaled_surplus_example = example
    if stats.min_spare_copies is None or spare < stats.min_spare_copies:
        stats.min_spare_copies = spare
        stats.min_spare_copies_example = example
    if stats.max_needed_copies is None or needed > stats.max_needed_copies:
        stats.max_needed_copies = needed
        stats.max_needed_copies_example = example
    if stats.max_deficit is None or deficit > stats.max_deficit:
        stats.max_deficit = deficit
        stats.max_deficit_example = example


def counter_json(counter: Counter[int | str], limit: int | None = None) -> list[dict[str, Any]]:
    items = counter.most_common(limit)
    return [{"value": value, "count": count} for value, count in items]


def lift_run_stats_json(stats: LiftRunStats, top_patterns: int) -> dict[str, Any]:
    return {
        "total_lift_cases": stats.total_lift_cases,
        "alpha_one": stats.alpha_one,
        "alpha_gt_one": stats.alpha_gt_one,
        "one_copy_covers": stats.one_copy_covers,
        "multi_copy_needed": stats.multi_copy_needed,
        "forced_cover_failures": stats.forced_cover_failures,
        "min_scaled_surplus": stats.min_scaled_surplus,
        "min_scaled_surplus_example": stats.min_scaled_surplus_example,
        "min_spare_copies": stats.min_spare_copies,
        "min_spare_copies_example": stats.min_spare_copies_example,
        "max_needed_copies": stats.max_needed_copies,
        "max_needed_copies_example": stats.max_needed_copies_example,
        "max_deficit": stats.max_deficit,
        "max_deficit_example": stats.max_deficit_example,
        "b_counter": counter_json(stats.b_counter),
        "needed_counter": counter_json(stats.needed_counter),
        "alpha_counter": counter_json(stats.alpha_counter),
        "top_bit_patterns": counter_json(stats.bit_counter, top_patterns),
    }


def enumerate_lift_channel(
    *,
    max_length: int,
    max_total_depth: int,
    max_carry: int,
    top_examples: int,
    top_patterns: int,
) -> dict[str, Any]:
    data_by_word: dict[tuple[int, ...], dict[str, Any] | None] = {}
    by_run: dict[int, LiftRunStats] = {}
    all_lift_examples: list[dict[str, Any]] = []
    min_sigma_examples: list[dict[str, Any]] = []
    min_spare_examples: list[dict[str, Any]] = []
    max_needed_examples: list[dict[str, Any]] = []
    alpha_gt_one_examples: list[dict[str, Any]] = []
    small_b_examples: list[dict[str, Any]] = []
    totals = {
        "words": 0,
        "contracting_words": 0,
        "append_one_blocks": 0,
        "lift_supported_blocks": 0,
        "anchor_supported_blocks": 0,
        "negative_q_words": 0,
        "zero_q_words": 0,
        "trivial_zero_words": 0,
        "positive_q_words": 0,
        "decomposition_failures": 0,
        "forced_cover_failures": 0,
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

                totals["append_one_blocks"] += 1
                surplus = surplus_example(block)
                if surplus["support_mode"] != "lift_needed":
                    totals["anchor_supported_blocks"] += 1
                    continue

                example = lift_example(block)
                totals["lift_supported_blocks"] += 1
                if not example["forced_cover_ok"]:
                    totals["forced_cover_failures"] += 1

                stats = by_run.setdefault(int(example["run"]), LiftRunStats())
                update_lift_run_stats(stats, example)
                all_lift_examples.append(example)
                update_top_min(
                    min_sigma_examples,
                    example,
                    top_examples,
                    "scaled_surplus",
                )
                update_top_min(
                    min_spare_examples,
                    example,
                    top_examples,
                    "spare_lift_copies",
                )
                if int(example["alpha"]) > 1:
                    update_top_min(
                        alpha_gt_one_examples,
                        example,
                        top_examples,
                        "scaled_surplus",
                    )
                if bool(example["small_b"]):
                    update_top_min(
                        small_b_examples,
                        example,
                        top_examples,
                        "scaled_surplus",
                    )

    max_needed_examples = sorted(
        all_lift_examples,
        key=lambda row: (
            -int(row["lift_copies_needed"]),
            int(row["spare_lift_copies"]),
            int(row["scaled_surplus"]),
            row["child_signature"],
        ),
    )[:top_examples]

    global_counters = {
        "by_run": Counter(int(row["run"]) for row in all_lift_examples),
        "by_b": Counter(int(row["block_lift_b"]) for row in all_lift_examples),
        "by_needed_copies": Counter(
            int(row["lift_copies_needed"]) for row in all_lift_examples
        ),
        "by_alpha": Counter(int(row["alpha"]) for row in all_lift_examples),
    }

    return {
        "totals": totals,
        "by_run": {
            str(run): lift_run_stats_json(stats, top_patterns)
            for run, stats in sorted(by_run.items())
        },
        "global_counters": {
            key: counter_json(counter)
            for key, counter in global_counters.items()
        },
        "min_sigma_examples": min_sigma_examples,
        "min_spare_examples": min_spare_examples,
        "max_needed_examples": max_needed_examples,
        "alpha_gt_one_examples": alpha_gt_one_examples,
        "small_b_examples": small_b_examples,
        "all_lift_examples": sorted(
            all_lift_examples,
            key=lambda row: (
                int(row["run"]),
                int(row["block_lift_b"]),
                int(row["scaled_surplus"]),
                row["child_signature"],
            ),
        ),
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
        "| k | lift cases | alpha=1 | alpha>1 | one-copy | multi-copy | max N | min spare | min Sigma | cover failures |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for run in sorted(rows, key=lambda item: int(item)):
        row = rows[run]
        lines.append(
            f"| {run} | {row['total_lift_cases']} | {row['alpha_one']} | "
            f"{row['alpha_gt_one']} | {row['one_copy_covers']} | "
            f"{row['multi_copy_needed']} | "
            f"{number_or_dash(row['max_needed_copies'])} | "
            f"{number_or_dash(row['min_spare_copies'])} | "
            f"{number_or_dash(row['min_scaled_surplus'])} | "
            f"{row['forced_cover_failures']} |"
        )
    return lines


def make_example_table(title: str, examples: list[dict[str, Any]]) -> list[str]:
    lines = [
        title,
        "",
        "| child | k | b | N | spare | Sigma | deficit | D_k | alpha | q anchor | bits |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    if not examples:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - |")
        return lines
    for example in examples:
        lines.append(
            f"| `{example['child_signature']}` | {example['run']} | "
            f"{example['block_lift_b']} | {example['lift_copies_needed']} | "
            f"{example['spare_lift_copies']} | {example['scaled_surplus']} | "
            f"{example['deficit']} | {example['block_denominator']} | "
            f"{example['alpha']} | {example['anchor_q']} | "
            f"`{example['block_lift_bits_low_to_high']}` |"
        )
    return lines


def make_counter_table(title: str, rows: list[dict[str, Any]]) -> list[str]:
    lines = [title, "", "| value | count |", "|---:|---:|"]
    if not rows:
        lines.append("| - | - |")
        return lines
    for row in rows:
        lines.append(f"| {row['value']} | {row['count']} |")
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    results = payload["results"]
    totals = results["totals"]
    lines = [
        "# Collatz Append-One Lift Channel Miner",
        "",
        "## Meaning",
        "",
        "This report isolates the rare append-one blocks where anchor support is not enough:",
        "",
        "```text",
        "2^k q_w < (3^k - 2^k) alpha.",
        "```",
        "",
        "For those blocks, define the positive deficit",
        "",
        "```text",
        "E = (3^k - 2^k) alpha - 2^k q_w",
        "```",
        "",
        "and the lift-copy demand",
        "",
        "```text",
        "N = ceil(E / D_k).",
        "```",
        "",
        "Since the forced lift contribution is `D_k b`, append-one positivity in this subchannel is equivalent to",
        "",
        "```text",
        "N <= b.",
        "```",
        "",
        "The miner records how close that inequality comes to failing.",
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
        f"- anchor-supported blocks: `{totals['anchor_supported_blocks']}`",
        f"- lift-supported blocks: `{totals['lift_supported_blocks']}`",
        f"- decomposition failures: `{totals['decomposition_failures']}`",
        f"- forced-cover failures: `{totals['forced_cover_failures']}`",
        f"- negative q words: `{totals['negative_q_words']}`",
        f"- zero q words: `{totals['zero_q_words']}`",
        f"- trivial zero words: `{totals['trivial_zero_words']}`",
        "",
        "## Lift Ledger By Run Length",
        "",
        *make_run_table(results["by_run"]),
        "",
        *make_example_table(
            "Smallest lift-supported scaled surpluses:",
            results["min_sigma_examples"],
        ),
        "",
        *make_example_table(
            "Smallest spare-copy margins:",
            results["min_spare_examples"],
        ),
        "",
        *make_example_table(
            "Largest lift-copy demands:",
            results["max_needed_examples"],
        ),
        "",
        *make_example_table(
            "Non-unit-alpha lift cases:",
            results["alpha_gt_one_examples"],
        ),
        "",
        *make_example_table(
            "Small-b lift cases:",
            results["small_b_examples"],
        ),
        "",
        "## Global Counters",
        "",
        *make_counter_table(
            "Lift cases by run length:",
            results["global_counters"]["by_run"],
        ),
        "",
        *make_counter_table(
            "Lift cases by required copy count N:",
            results["global_counters"]["by_needed_copies"],
        ),
        "",
        *make_counter_table(
            "Lift cases by forced lift b:",
            results["global_counters"]["by_b"],
        ),
        "",
        *make_counter_table(
            "Lift cases by alpha:",
            results["global_counters"]["by_alpha"],
        ),
        "",
        "## Proof-Facing Read",
        "",
        "The rare channel now has a minimal exact form:",
        "",
        "```text",
        "E = (3^k - 2^k) alpha - 2^k q_w > 0",
        "N = ceil(E / D_k)",
        "prove N <= b, where b == -alpha * (3^m)^-1 mod 2^k.",
        "```",
        "",
        "Thus the small-`b` cases are dangerous only when the copy demand `N` approaches `b`.  The table `Smallest spare-copy margins` is the finite-window list of nearest misses.",
        "",
        "This is not a proof of append-one positivity; it is a sharper local formulation of the lift-supported obligation.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_append_one_lift_channel_miner.py "
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
        / f"collatz_append_one_lift_channel_L{max_length}_S{max_total_depth}_K{max_carry}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_append_one_lift_channel_L{max_length}_S{max_total_depth}_K{max_carry}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=8)
    parser.add_argument("--max-total-depth", type=int, default=21)
    parser.add_argument("--max-carry", type=int, default=8)
    parser.add_argument("--top-examples", type=int, default=16)
    parser.add_argument("--top-patterns", type=int, default=8)
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

    results = enumerate_lift_channel(
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
    print(json.dumps(rounded(results["global_counters"]), indent=2))


if __name__ == "__main__":
    main()
