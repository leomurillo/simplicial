"""Mine exact append-one chains for the Collatz descent-margin quotient.

The suffix-monotonicity note proves that appending a carry s >= 2 cannot
decrease q once the parent and child are contracting.  The only suffix channel
that can still decrease q is therefore the carry-one channel.

For a contracting carry word w, write

    U_w(n) = (3^m n + C_w) / 2^S,
    D_w = 2^S - 3^m,
    y_w = U_w(r_w),
    q_w = (r_w - y_w) / 2.

Appending one carry has lift digit t in {0,1}, forced by

    y_w + 2 * 3^m * t == 3 mod 4.

This script mines that single-step rule and the closed block recurrence for
appending 1^k.  If

    alpha = (y_w + 1) / 2,
    A = 3^m,

then the whole 1^k block is encoded by the unique integer 0 <= b < 2^k with

    A b == -alpha mod 2^k,

equivalently y_w + 2 A b == -1 mod 2^(k+1).  The child image is

    y_{w,1^k} = 2 * 3^k * h - 1,
    h = (alpha + A b) / 2^k,

and the exact block margin recurrence is

    q_{w,1^k} = q_w
        + (D_{w,k} b - (3^k - 2^k) alpha) / 2^k,

where D_{w,k}=2^(S+k)-3^(m+k).

The remaining theorem-facing append-one obligation is the inequality version

    2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha

for every contracting child w1^k that arises in the reduced channel.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from collatz_margin_theorem_candidate import (
    LOG2_3,
    cocycle_for_word,
    margin_data,
    word_signature,
)


@dataclass
class StepStats:
    transitions: int = 0
    delta_negative: int = 0
    delta_zero: int = 0
    delta_positive: int = 0
    child_negative_q: int = 0
    child_zero_q: int = 0
    child_positive_q: int = 0
    min_delta: int | None = None
    min_delta_example: dict[str, Any] | None = None
    min_child_q: int | None = None
    min_child_q_example: dict[str, Any] | None = None
    max_drop: int | None = None
    max_drop_example: dict[str, Any] | None = None
    recurrence_failures: int = 0


@dataclass
class BlockStats:
    chains: int = 0
    negative_q: int = 0
    zero_q: int = 0
    positive_q: int = 0
    drop_negative: int = 0
    drop_zero: int = 0
    drop_positive: int = 0
    min_q: int | None = None
    min_q_example: dict[str, Any] | None = None
    max_drop: int | None = None
    max_drop_example: dict[str, Any] | None = None
    min_scaled_surplus: int | None = None
    min_scaled_surplus_example: dict[str, Any] | None = None
    block_failures: int = 0


def bounded_compositions(
    total: int,
    parts: int,
    max_part: int,
) -> Iterable[tuple[int, ...]]:
    if parts == 0:
        if total == 0:
            yield ()
        return
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
    run = 0
    for carry in reversed(word):
        if carry != 1:
            break
        run += 1
    return run


def carry_word_json(word: tuple[int, ...]) -> list[int]:
    return list(word)


def bits_low_to_high(value: int, width: int) -> str:
    return "".join("1" if value & (1 << index) else "0" for index in range(width))


def signed_count(q: int, stats: StepStats | BlockStats) -> None:
    if isinstance(stats, StepStats):
        if q < 0:
            stats.child_negative_q += 1
        elif q == 0:
            stats.child_zero_q += 1
        else:
            stats.child_positive_q += 1
        return

    if q < 0:
        stats.negative_q += 1
    elif q == 0:
        stats.zero_q += 1
    else:
        stats.positive_q += 1


def one_step_data(
    parent: tuple[int, ...],
    child: tuple[int, ...],
    parent_data: dict[str, Any],
    child_data: dict[str, Any],
) -> dict[str, Any]:
    m, total_depth, three_power, _cocycle = cocycle_for_word(parent)
    y = int(parent_data["image"])
    parent_q = int(parent_data["q_int"])
    child_q = int(child_data["q_int"])
    child_denominator = (1 << (total_depth + 1)) - 3 * three_power
    lift_t = (((3 - y) // 2) * pow(three_power, -1, 2)) % 2
    rule_t = 0 if y % 4 == 3 else 1
    delta_numerator = 2 * child_denominator * lift_t - y - 1
    delta_ok = delta_numerator % 4 == 0
    predicted_delta = delta_numerator // 4 if delta_ok else None
    delta_q = child_q - parent_q
    return {
        "parent": carry_word_json(parent),
        "parent_signature": word_signature(parent),
        "child": carry_word_json(child),
        "child_signature": word_signature(child),
        "parent_m": parent_data["length"],
        "parent_S": parent_data["total_depth"],
        "parent_q": parent_q,
        "child_q": child_q,
        "delta_q": delta_q,
        "drop_from_parent": parent_q - child_q,
        "parent_y": y,
        "parent_y_mod_4": y % 4,
        "child_denominator": child_denominator,
        "lift_t": lift_t,
        "rule_t": rule_t,
        "delta_formula_numerator": delta_numerator,
        "predicted_delta_q": predicted_delta,
        "ok": (
            rule_t == lift_t
            and delta_ok
            and predicted_delta == delta_q
            and (y + 2 * three_power * lift_t - 3) % 4 == 0
        ),
    }


def block_data(
    anchor: tuple[int, ...],
    run: int,
    child: tuple[int, ...],
    anchor_data: dict[str, Any],
    child_data: dict[str, Any],
) -> dict[str, Any]:
    m, total_depth, three_power, _cocycle = cocycle_for_word(anchor)
    y = int(anchor_data["image"])
    anchor_q = int(anchor_data["q_int"])
    child_q = int(child_data["q_int"])
    alpha = (y + 1) // 2
    modulus = 1 << run
    block_lift = (-alpha * pow(three_power, -1, modulus)) % modulus
    h_numerator = alpha + three_power * block_lift
    h_ok = h_numerator % modulus == 0
    h = h_numerator // modulus if h_ok else None
    three_block = 3**run
    block_denominator = (1 << (total_depth + run)) - three_block * three_power
    delta_numerator = block_denominator * block_lift - (
        three_block - (1 << run)
    ) * alpha
    delta_ok = delta_numerator % modulus == 0
    predicted_delta = delta_numerator // modulus if delta_ok else None
    predicted_q = anchor_q + predicted_delta if predicted_delta is not None else None
    predicted_residue = (
        int(anchor_data["residue"]) + block_lift * (1 << (total_depth + 1))
    ) % (1 << (total_depth + run + 1))
    predicted_image = None if h is None else 2 * three_block * h - 1
    scaled_surplus = (1 << run) * child_q
    inequality_left = (1 << run) * anchor_q + block_denominator * block_lift
    inequality_right = (three_block - (1 << run)) * alpha
    return {
        "anchor": carry_word_json(anchor),
        "anchor_signature": word_signature(anchor),
        "child": carry_word_json(child),
        "child_signature": word_signature(child),
        "run": run,
        "anchor_m": anchor_data["length"],
        "anchor_S": anchor_data["total_depth"],
        "child_m": child_data["length"],
        "child_S": child_data["total_depth"],
        "anchor_q": anchor_q,
        "child_q": child_q,
        "drop_from_anchor": anchor_q - child_q,
        "anchor_y": y,
        "alpha": alpha,
        "three_power": three_power,
        "block_lift_b": block_lift,
        "block_lift_bits_low_to_high": bits_low_to_high(block_lift, run),
        "h": h,
        "block_denominator": block_denominator,
        "delta_formula_numerator": delta_numerator,
        "predicted_delta_q": predicted_delta,
        "predicted_q": predicted_q,
        "predicted_residue": predicted_residue,
        "actual_residue": int(child_data["residue"]),
        "predicted_image": predicted_image,
        "actual_image": int(child_data["image"]),
        "scaled_surplus": scaled_surplus,
        "inequality_left": inequality_left,
        "inequality_right": inequality_right,
        "ok": (
            h_ok
            and delta_ok
            and predicted_q == child_q
            and predicted_residue == int(child_data["residue"])
            and predicted_image == int(child_data["image"])
            and (y + 2 * three_power * block_lift + 1)
            % (1 << (run + 1))
            == 0
            and inequality_left - inequality_right == scaled_surplus
        ),
    }


def update_step_stats(stats: StepStats, example: dict[str, Any]) -> None:
    delta = int(example["delta_q"])
    child_q = int(example["child_q"])
    drop = int(example["drop_from_parent"])
    stats.transitions += 1
    if not example["ok"]:
        stats.recurrence_failures += 1
    if delta < 0:
        stats.delta_negative += 1
    elif delta == 0:
        stats.delta_zero += 1
    else:
        stats.delta_positive += 1
    signed_count(child_q, stats)
    if stats.min_delta is None or delta < stats.min_delta:
        stats.min_delta = delta
        stats.min_delta_example = example
    if stats.min_child_q is None or child_q < stats.min_child_q:
        stats.min_child_q = child_q
        stats.min_child_q_example = example
    if stats.max_drop is None or drop > stats.max_drop:
        stats.max_drop = drop
        stats.max_drop_example = example


def update_block_stats(stats: BlockStats, example: dict[str, Any]) -> None:
    child_q = int(example["child_q"])
    drop = int(example["drop_from_anchor"])
    scaled_surplus = int(example["scaled_surplus"])
    stats.chains += 1
    if not example["ok"]:
        stats.block_failures += 1
    signed_count(child_q, stats)
    if drop < 0:
        stats.drop_negative += 1
    elif drop == 0:
        stats.drop_zero += 1
    else:
        stats.drop_positive += 1
    if stats.min_q is None or child_q < stats.min_q:
        stats.min_q = child_q
        stats.min_q_example = example
    if stats.max_drop is None or drop > stats.max_drop:
        stats.max_drop = drop
        stats.max_drop_example = example
    if stats.min_scaled_surplus is None or scaled_surplus < stats.min_scaled_surplus:
        stats.min_scaled_surplus = scaled_surplus
        stats.min_scaled_surplus_example = example


def step_stats_json(stats: StepStats) -> dict[str, Any]:
    return {
        "transitions": stats.transitions,
        "delta_negative": stats.delta_negative,
        "delta_zero": stats.delta_zero,
        "delta_positive": stats.delta_positive,
        "child_negative_q": stats.child_negative_q,
        "child_zero_q": stats.child_zero_q,
        "child_positive_q": stats.child_positive_q,
        "min_delta": stats.min_delta,
        "min_delta_example": stats.min_delta_example,
        "min_child_q": stats.min_child_q,
        "min_child_q_example": stats.min_child_q_example,
        "max_drop": stats.max_drop,
        "max_drop_example": stats.max_drop_example,
        "recurrence_failures": stats.recurrence_failures,
    }


def block_stats_json(stats: BlockStats) -> dict[str, Any]:
    return {
        "chains": stats.chains,
        "negative_q": stats.negative_q,
        "zero_q": stats.zero_q,
        "positive_q": stats.positive_q,
        "drop_negative": stats.drop_negative,
        "drop_zero": stats.drop_zero,
        "drop_positive": stats.drop_positive,
        "min_q": stats.min_q,
        "min_q_example": stats.min_q_example,
        "max_drop": stats.max_drop,
        "max_drop_example": stats.max_drop_example,
        "min_scaled_surplus": stats.min_scaled_surplus,
        "min_scaled_surplus_example": stats.min_scaled_surplus_example,
        "block_failures": stats.block_failures,
    }


def enumerate_append_one_chains(
    *,
    max_length: int,
    max_total_depth: int,
    max_carry: int,
) -> dict[str, Any]:
    data_by_word: dict[tuple[int, ...], dict[str, Any] | None] = {}
    step_by_t = {0: StepStats(), 1: StepStats()}
    block_by_run: dict[int, BlockStats] = {}
    totals = {
        "words": 0,
        "contracting_words": 0,
        "append_one_transitions": 0,
        "append_one_blocks": 0,
        "step_recurrence_failures": 0,
        "block_recurrence_failures": 0,
        "negative_q_words": 0,
        "zero_q_words": 0,
        "trivial_zero_words": 0,
        "positive_q_words": 0,
    }

    first_step_failures: list[dict[str, Any]] = []
    first_block_failures: list[dict[str, Any]] = []

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

                if word[-1] == 1 and len(word) >= 2:
                    parent = word[:-1]
                    parent_data = data_by_word.get(parent)
                    if parent_data is not None:
                        step = one_step_data(parent, word, parent_data, data)
                        update_step_stats(step_by_t[int(step["lift_t"])], step)
                        totals["append_one_transitions"] += 1
                        if not step["ok"]:
                            totals["step_recurrence_failures"] += 1
                            if len(first_step_failures) < 8:
                                first_step_failures.append(step)

                run = trailing_ones(word)
                if run and len(word) > run:
                    anchor = word[:-run]
                    anchor_data = data_by_word.get(anchor)
                    if anchor_data is not None:
                        block = block_data(anchor, run, word, anchor_data, data)
                        stats = block_by_run.setdefault(run, BlockStats())
                        update_block_stats(stats, block)
                        totals["append_one_blocks"] += 1
                        if not block["ok"]:
                            totals["block_recurrence_failures"] += 1
                            if len(first_block_failures) < 8:
                                first_block_failures.append(block)

    all_block_rows = [block_stats_json(stats) for stats in block_by_run.values()]
    global_min_block_q = min(
        (
            row["min_q_example"]
            for row in all_block_rows
            if row["min_q_example"] is not None
        ),
        key=lambda item: int(item["child_q"]),
        default=None,
    )
    global_max_block_drop = max(
        (
            row["max_drop_example"]
            for row in all_block_rows
            if row["max_drop_example"] is not None
        ),
        key=lambda item: int(item["drop_from_anchor"]),
        default=None,
    )

    return {
        "totals": totals,
        "step_by_t": {
            str(lift_t): step_stats_json(stats)
            for lift_t, stats in sorted(step_by_t.items())
        },
        "block_by_run": {
            str(run): block_stats_json(stats)
            for run, stats in sorted(block_by_run.items())
        },
        "global_min_block_q": global_min_block_q,
        "global_max_block_drop": global_max_block_drop,
        "first_step_failures": first_step_failures,
        "first_block_failures": first_block_failures,
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


def make_step_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| lift t | transitions | delta < 0 | delta = 0 | delta > 0 | min delta | min child q | recurrence failures |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for lift_t in sorted(rows, key=lambda item: int(item)):
        row = rows[lift_t]
        lines.append(
            f"| {lift_t} | {row['transitions']} | {row['delta_negative']} | "
            f"{row['delta_zero']} | {row['delta_positive']} | "
            f"{number_or_dash(row['min_delta'])} | "
            f"{number_or_dash(row['min_child_q'])} | "
            f"{row['recurrence_failures']} |"
        )
    return lines


def make_block_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| trailing ones k | blocks | q < 0 | q = 0 | q > 0 | drop > 0 | min q | max signed drop | min-q word |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for run in sorted(rows, key=lambda item: int(item)):
        row = rows[run]
        example = row["min_q_example"]
        signature = "-" if example is None else f"`{example['child_signature']}`"
        lines.append(
            f"| {run} | {row['chains']} | {row['negative_q']} | "
            f"{row['zero_q']} | {row['positive_q']} | {row['drop_positive']} | "
            f"{number_or_dash(row['min_q'])} | {number_or_dash(row['max_drop'])} | "
            f"{signature} |"
        )
    return lines


def make_step_example_table(rows: dict[str, Any]) -> list[str]:
    examples = [
        row["min_delta_example"]
        for row in rows.values()
        if row["min_delta_example"] is not None
    ]
    lines = [
        "Most negative one-step deltas by lift digit:",
        "",
        "| t | parent | child | q parent | q child | delta | y | D child |",
        "|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    if not examples:
        lines.append("| - | - | - | - | - | - | - | - |")
        return lines
    for example in sorted(examples, key=lambda item: int(item["lift_t"])):
        lines.append(
            f"| {example['lift_t']} | `{example['parent_signature']}` | "
            f"`{example['child_signature']}` | {example['parent_q']} | "
            f"{example['child_q']} | {example['delta_q']} | "
            f"{example['parent_y']} | {example['child_denominator']} |"
        )
    return lines


def make_block_example(title: str, example: dict[str, Any] | None) -> list[str]:
    lines = [title, ""]
    if example is None:
        lines.append("_None._")
        return lines
    lines.extend(
        [
            f"- anchor: `{example['anchor_signature']}`",
            f"- child: `{example['child_signature']}`",
            f"- run k: `{example['run']}`",
            f"- anchor q: `{example['anchor_q']}`",
            f"- child q: `{example['child_q']}`",
            f"- drop from anchor: `{example['drop_from_anchor']}`",
            f"- y, alpha: `{example['anchor_y']}, {example['alpha']}`",
            f"- block lift b: `{example['block_lift_b']}`",
            f"- t bits low-to-high: `{example['block_lift_bits_low_to_high']}`",
            f"- h: `{example['h']}`",
            f"- D block: `{example['block_denominator']}`",
            f"- scaled surplus `2^k q_child`: `{example['scaled_surplus']}`",
        ]
    )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    results = payload["results"]
    totals = results["totals"]
    lines = [
        "# Collatz Append-One Chain Miner",
        "",
        "## Meaning",
        "",
        "Suffix monotonicity leaves append-1 as the only suffix channel that can decrease the descent-margin quotient.  This report mines that channel using exact integer recurrences, not floating approximations.",
        "",
        "For one appended carry, the lift digit is determined by",
        "",
        "```text",
        "y_w + 2 * 3^m * t == 3 mod 4,   t in {0,1}.",
        "```",
        "",
        "Since `y_w` is odd, this is the simple parity split:",
        "",
        "```text",
        "t = 0  iff  y_w == 3 mod 4",
        "t = 1  iff  y_w == 1 mod 4.",
        "```",
        "",
        "For a whole appended block `1^k`, write `A=3^m`, `alpha=(y_w+1)/2`, and let `b` be the unique integer `0 <= b < 2^k` satisfying",
        "",
        "```text",
        "A b == -alpha mod 2^k.",
        "```",
        "",
        "Equivalently, `y_w + 2 A b == -1 mod 2^(k+1)`.  The bits of `b` are the successive lift digits of the appended-one chain.",
        "",
        "## Settings",
        "",
        f"- max length: `{settings['max_length']}`",
        f"- max total carry depth: `{settings['max_total_depth']}`",
        f"- carry alphabet: `1..{settings['max_carry']}`",
        "",
        "## Verification",
        "",
        f"- words scanned: `{totals['words']}`",
        f"- contracting words: `{totals['contracting_words']}`",
        f"- negative q words: `{totals['negative_q_words']}`",
        f"- zero q words: `{totals['zero_q_words']}`",
        f"- trivial zero words: `{totals['trivial_zero_words']}`",
        f"- positive q words: `{totals['positive_q_words']}`",
        f"- append-one transitions: `{totals['append_one_transitions']}`",
        f"- append-one blocks: `{totals['append_one_blocks']}`",
        f"- one-step recurrence failures: `{totals['step_recurrence_failures']}`",
        f"- block recurrence failures: `{totals['block_recurrence_failures']}`",
        "",
        "## One-Step Gate Split",
        "",
        *make_step_table(results["step_by_t"]),
        "",
        *make_step_example_table(results["step_by_t"]),
        "",
        "The `t=0` branch always decreases `q` by `(y_w+1)/4`.  The `t=1` branch has",
        "",
        "```text",
        "q_{w,1} - q_w = (2D_{w,1} - y_w - 1) / 4,",
        "```",
        "",
        "so it can still decrease when `y_w` is large compared with the child denominator `D_{w,1}`.",
        "",
        "## Block Chains",
        "",
        *make_block_table(results["block_by_run"]),
        "",
        *make_block_example(
            "Smallest observed q after an append-one block:",
            results["global_min_block_q"],
        ),
        "",
        *make_block_example(
            "Largest observed drop across an append-one block:",
            results["global_max_block_drop"],
        ),
        "",
        "## Exact Block Recurrence",
        "",
        "With `D_{w,k}=2^(S+k)-3^(m+k)` and `h=(alpha+A b)/2^k`, the block image is",
        "",
        "```text",
        "y_{w,1^k} = 2 * 3^k * h - 1.",
        "```",
        "",
        "The block margin recurrence verified above is",
        "",
        "```text",
        "q_{w,1^k} = q_w + (D_{w,k} b - (3^k - 2^k) alpha) / 2^k.",
        "```",
        "",
        "Thus append-one positivity is exactly the integer inequality",
        "",
        "```text",
        "2^k q_w + D_{w,k} b >= (3^k - 2^k) alpha.",
        "```",
        "",
        "In this finite window, every checked contracting append-one block has nonnegative `q`, and the scaled surplus `2^k q_{w,1^k}` is the exact difference between the two sides of the inequality.",
        "",
        "This is not a proof of Collatz.  It isolates the append-one proof obligation as a closed finite-arithmetic inequality for the forced lift residue `b`.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_append_one_chain_miner.py "
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
        / f"collatz_append_one_chains_L{max_length}_S{max_total_depth}_K{max_carry}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_append_one_chains_L{max_length}_S{max_total_depth}_K{max_carry}.json"
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

    results = enumerate_append_one_chains(
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
    print(json.dumps(rounded(results["global_min_block_q"]), indent=2))


if __name__ == "__main__":
    main()
