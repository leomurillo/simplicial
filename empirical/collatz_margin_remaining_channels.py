"""Audit the two remaining channels after suffix monotonicity.

The append-delta identity proves that a minimal negative-margin counterexample
cannot end with carry s >= 2 when its prefix is already contracting.  This
leaves two channels:

1. append-1 chains after a contracting prefix;
2. first-contraction boundary words, whose prefix is not contracting.

This script mines those channels directly.  It is still empirical, but it is
aimed at the reduced proof obligations rather than the full carry language.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from collatz_margin_theorem_candidate import LOG2_3, margin_data, word_signature


@dataclass
class ChannelStats:
    count: int = 0
    negative_q: int = 0
    zero_q: int = 0
    positive_q: int = 0
    min_q: int | None = None
    min_q_example: dict[str, Any] | None = None
    max_drop: int | None = None
    max_drop_example: dict[str, Any] | None = None


def bounded_compositions(
    total: int,
    parts: int,
    max_part: int,
) -> Iterable[tuple[int, ...]]:
    if parts == 1:
        if 1 <= total <= max_part:
            yield (total,)
        return

    lower = max(1, total - max_part * (parts - 1))
    upper = min(max_part, total - (parts - 1))
    for first in range(lower, upper + 1):
        for rest in bounded_compositions(total - first, parts - 1, max_part):
            yield (first, *rest)


def trailing_ones(word: tuple[int, ...]) -> int:
    count = 0
    for carry in reversed(word):
        if carry != 1:
            break
        count += 1
    return count


def example_for_word(
    word: tuple[int, ...],
    data: dict[str, Any],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    row = {
        "word": list(word),
        "signature": word_signature(word),
        "m": data["length"],
        "S": data["total_depth"],
        "height": data["height"],
        "q": int(data["q_int"]),
        "first_n": int(data["first_n"]),
        "image": int(data["image"]),
    }
    if extra:
        row.update(extra)
    return row


def update_q_stats(
    stats: ChannelStats,
    word: tuple[int, ...],
    data: dict[str, Any],
    extra: dict[str, Any] | None = None,
) -> None:
    q = int(data["q_int"])
    stats.count += 1
    if q < 0:
        stats.negative_q += 1
    elif q == 0:
        stats.zero_q += 1
    else:
        stats.positive_q += 1
    if stats.min_q is None or q < stats.min_q:
        stats.min_q = q
        stats.min_q_example = example_for_word(word, data, extra)


def update_drop_stats(
    stats: ChannelStats,
    word: tuple[int, ...],
    data: dict[str, Any],
    drop: int,
    extra: dict[str, Any],
) -> None:
    if stats.max_drop is None or drop > stats.max_drop:
        stats.max_drop = drop
        stats.max_drop_example = example_for_word(word, data, extra)


def enumerate_channels(
    *,
    max_length: int,
    max_total_depth: int,
    max_carry: int,
) -> dict[str, Any]:
    data_by_word: dict[tuple[int, ...], dict[str, Any] | None] = {}
    totals = {
        "words": 0,
        "contracting_words": 0,
        "negative_q_words": 0,
        "zero_q_words": 0,
        "trivial_zero_words": 0,
        "positive_q_words": 0,
    }
    append_one_by_run: dict[int, ChannelStats] = {}
    boundary_by_final: dict[int, ChannelStats] = {
        carry: ChannelStats() for carry in range(2, max_carry + 1)
    }
    irreducible_stats = ChannelStats()

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

                prefix = word[:-1]
                prefix_data = data_by_word.get(prefix)
                if prefix and prefix_data is None:
                    stats = boundary_by_final.setdefault(word[-1], ChannelStats())
                    update_q_stats(
                        stats,
                        word,
                        data,
                        {"prefix": list(prefix), "prefix_signature": word_signature(prefix)},
                    )

                run = trailing_ones(word)
                if run:
                    anchor = word[:-run]
                    anchor_data = data_by_word.get(anchor)
                    if anchor_data is not None:
                        stats = append_one_by_run.setdefault(run, ChannelStats())
                        anchor_q = int(anchor_data["q_int"])
                        drop = anchor_q - q
                        extra = {
                            "anchor": list(anchor),
                            "anchor_signature": word_signature(anchor),
                            "anchor_q": anchor_q,
                            "drop_from_anchor": drop,
                        }
                        update_q_stats(stats, word, data, extra)
                        update_drop_stats(stats, word, data, drop, extra)

                if (
                    not prefix
                    or prefix_data is None
                    or word[-1] == 1
                ):
                    update_q_stats(
                        irreducible_stats,
                        word,
                        data,
                        {
                            "reason": "boundary"
                            if prefix and prefix_data is None
                            else ("append-one" if word[-1] == 1 else "root")
                        },
                    )

    return {
        "totals": totals,
        "append_one_by_run": {
            str(run): channel_stats_json(stats)
            for run, stats in sorted(append_one_by_run.items())
        },
        "boundary_by_final": {
            str(carry): channel_stats_json(stats)
            for carry, stats in sorted(boundary_by_final.items())
        },
        "irreducible_stats": channel_stats_json(irreducible_stats),
    }


def channel_stats_json(stats: ChannelStats) -> dict[str, Any]:
    return {
        "count": stats.count,
        "negative_q": stats.negative_q,
        "zero_q": stats.zero_q,
        "positive_q": stats.positive_q,
        "min_q": stats.min_q,
        "min_q_example": stats.min_q_example,
        "max_drop": stats.max_drop,
        "max_drop_example": stats.max_drop_example,
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


def make_append_one_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| trailing ones | words | negative q | zero q | positive q | min q | max drop from anchor | min-q word |",
        "|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for run in sorted(rows, key=lambda item: int(item)):
        row = rows[run]
        example = row["min_q_example"]
        signature = "-" if example is None else f"`{example['signature']}`"
        lines.append(
            f"| {run} | {row['count']} | {row['negative_q']} | "
            f"{row['zero_q']} | {row['positive_q']} | "
            f"{number_or_dash(row['min_q'])} | {number_or_dash(row['max_drop'])} | "
            f"{signature} |"
        )
    return lines


def make_boundary_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| final carry | boundary words | negative q | zero q | positive q | min q | min-q word |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for carry in sorted(rows, key=lambda item: int(item)):
        row = rows[carry]
        example = row["min_q_example"]
        signature = "-" if example is None else f"`{example['signature']}`"
        lines.append(
            f"| {carry} | {row['count']} | {row['negative_q']} | "
            f"{row['zero_q']} | {row['positive_q']} | "
            f"{number_or_dash(row['min_q'])} | {signature} |"
        )
    return lines


def make_example_block(title: str, example: dict[str, Any] | None) -> list[str]:
    lines = [title, ""]
    if example is None:
        lines.append("_None._")
        return lines
    lines.extend(
        [
            f"- word: `{example['signature']}`",
            f"- m, S: `{example['m']}, {example['S']}`",
            f"- q: `{example['q']}`",
            f"- height: `{example['height']:.6f}`",
        ]
    )
    if "anchor_signature" in example:
        lines.extend(
            [
                f"- anchor: `{example['anchor_signature']}`",
                f"- anchor q: `{example['anchor_q']}`",
                f"- drop from anchor: `{example['drop_from_anchor']}`",
            ]
        )
    if "prefix_signature" in example:
        lines.append(f"- noncontracting prefix: `{example['prefix_signature']}`")
    if "reason" in example:
        lines.append(f"- reason: `{example['reason']}`")
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    results = payload["results"]
    totals = results["totals"]
    irreducible = results["irreducible_stats"]
    lines = [
        "# Collatz Remaining Margin Channels",
        "",
        "## Meaning",
        "",
        "Suffix monotonicity handles every appended carry `s >= 2` after a contracting prefix.  This report audits the two channels still capable of containing a minimal negative-margin word: trailing append-1 chains and first-contraction boundary words.",
        "",
        "## Settings",
        "",
        f"- max length: `{settings['max_length']}`",
        f"- max total carry depth: `{settings['max_total_depth']}`",
        f"- carry alphabet: `1..{settings['max_carry']}`",
        "",
        "## Totals",
        "",
        f"- words scanned: `{totals['words']}`",
        f"- contracting words: `{totals['contracting_words']}`",
        f"- negative q words: `{totals['negative_q_words']}`",
        f"- zero q words: `{totals['zero_q_words']}`",
        f"- trivial zero words: `{totals['trivial_zero_words']}`",
        f"- positive q words: `{totals['positive_q_words']}`",
        "",
        "## Append-One Chains",
        "",
        *make_append_one_table(results["append_one_by_run"]),
        "",
        *make_example_block(
            "Largest observed q drop along a trailing-one chain:",
            max(
                (
                    row["max_drop_example"]
                    for row in results["append_one_by_run"].values()
                    if row["max_drop_example"] is not None
                ),
                key=lambda item: item["drop_from_anchor"],
                default=None,
            ),
        ),
        "",
        "## First-Contraction Boundary",
        "",
        *make_boundary_table(results["boundary_by_final"]),
        "",
        *make_example_block(
            "Smallest observed boundary q:",
            min(
                (
                    row["min_q_example"]
                    for row in results["boundary_by_final"].values()
                    if row["min_q_example"] is not None
                ),
                key=lambda item: item["q"],
                default=None,
            ),
        ),
        "",
        "## Irreducible After Suffix Monotonicity",
        "",
        "An irreducible word here means: root, append-1 final carry, or first-contraction boundary.  Any minimal counterexample must appear in this reduced list.",
        "",
        f"- irreducible words: `{irreducible['count']}`",
        f"- negative q: `{irreducible['negative_q']}`",
        f"- zero q: `{irreducible['zero_q']}`",
        f"- positive q: `{irreducible['positive_q']}`",
        f"- min q: `{irreducible['min_q']}`",
        "",
        *make_example_block(
            "Smallest irreducible q:",
            irreducible["min_q_example"],
        ),
        "",
        "## Next Proof Targets",
        "",
        "The remaining theorem work is now concentrated in two statements:",
        "",
        "```text",
        "Append-one positivity:",
        "A contracting append-1 chain cannot push q below zero.",
        "",
        "Boundary positivity:",
        "Every first-contraction boundary word has q >= 0.",
        "```",
        "",
        "The finite window shows no negative q in either channel.  This is not yet a proof; it is the narrowed target list after the suffix-monotonicity lemma.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_margin_remaining_channels.py "
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
        / f"collatz_margin_remaining_channels_L{max_length}_S{max_total_depth}_K{max_carry}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_margin_remaining_channels_L{max_length}_S{max_total_depth}_K{max_carry}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=8)
    parser.add_argument("--max-total-depth", type=int, default=21)
    parser.add_argument("--max-carry", type=int, default=8)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 2:
        raise ValueError("--max-length must be at least 2")
    if args.max_total_depth < args.max_length:
        raise ValueError("--max-total-depth must be at least max-length")
    if args.max_carry < 2:
        raise ValueError("--max-carry must be at least 2")

    results = enumerate_channels(
        max_length=args.max_length,
        max_total_depth=args.max_total_depth,
        max_carry=args.max_carry,
    )
    payload = {
        "settings": {
            "max_length": args.max_length,
            "max_total_depth": args.max_total_depth,
            "max_carry": args.max_carry,
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
    print(json.dumps(rounded(results["irreducible_stats"]), indent=2))


if __name__ == "__main__":
    main()
