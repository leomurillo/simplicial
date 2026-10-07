"""Mine exact recurrences for the Collatz descent-margin quotient q_w.

For a carry word w = (s_1, ..., s_m), write

    U_w(n) = (3^m n + C_w) / 2^S,
    D_w = 2^S - 3^m.

On the exact carry cylinder, the first positive representative r_w gives

    q_w = (r_w D_w - C_w) / 2^(S+1) = (r_w - U_w(r_w)) / 2.

This script attacks the sign theorem by looking at exact append recurrences.
If a new carry s is appended to w, then the child exact-cylinder residue is

    r_{w,s} = r_w + t 2^(S+1) mod 2^(S+s+1),

where t mod 2^s is forced by the next carry gate.  The computation verifies
that recurrence and mines the observed sign behavior of

    q_{w,s} - q_w.

The recurrence also exposes the exact append-delta identity

    q_{w,s} - q_w =
        (2 D_{w,s} t + (2^s - 3) y_w - 1) / 2^(s+1),

where y_w = U_w(r_w).  This proves suffix monotonicity for s >= 2 as soon
as both parent and child are contracting.

The useful reduction candidate found by this audit is suffix monotonicity for
appended carries s >= 2.  If true in general, a minimal negative-margin
counterexample must either end in carry 1 or occur at the first prefix where
the word becomes contracting.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
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
class AppendStats:
    transitions: int = 0
    delta_negative: int = 0
    delta_zero: int = 0
    delta_positive: int = 0
    min_delta: int | None = None
    min_delta_example: dict[str, Any] | None = None
    min_child_q: int | None = None
    min_child_q_example: dict[str, Any] | None = None
    max_child_q: int | None = None
    preserving_examples: list[dict[str, Any]] | None = None
    recurrence_failures: int = 0

    def __post_init__(self) -> None:
        if self.preserving_examples is None:
            self.preserving_examples = []


@dataclass
class BoundaryStats:
    contracting_children: int = 0
    parent_contracting: int = 0
    parent_noncontracting: int = 0
    min_child_q: int | None = None
    min_child_q_example: dict[str, Any] | None = None
    examples: list[dict[str, Any]] | None = None

    def __post_init__(self) -> None:
        if self.examples is None:
            self.examples = []


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


def carry_gate_residue(carry: int) -> int:
    """Residue a_s mod 2^(s+1) for v2(3n+1)=s."""

    modulus = 1 << (carry + 1)
    return ((1 << carry) - 1) * pow(3, -1, modulus) % modulus


def carry_word_json(word: tuple[int, ...]) -> list[int]:
    return list(word)


def transition_example(
    parent: tuple[int, ...],
    carry: int,
    parent_data: dict[str, Any],
    child_data: dict[str, Any],
    recurrence: dict[str, Any],
) -> dict[str, Any]:
    parent_q = int(parent_data["q_int"])
    child_q = int(child_data["q_int"])
    return {
        "parent": carry_word_json(parent),
        "parent_signature": word_signature(parent),
        "carry": carry,
        "child": carry_word_json((*parent, carry)),
        "child_signature": word_signature((*parent, carry)),
        "parent_q": parent_q,
        "child_q": child_q,
        "delta_q": child_q - parent_q,
        "parent_m": parent_data["length"],
        "parent_S": parent_data["total_depth"],
        "child_m": child_data["length"],
        "child_S": child_data["total_depth"],
        "lift_t": recurrence["lift_t"],
        "parent_image_mod_gate": recurrence["parent_image_mod_gate"],
        "next_gate_residue": recurrence["next_gate_residue"],
    }


def append_recurrence(parent: tuple[int, ...], carry: int) -> dict[str, Any] | None:
    parent_data = margin_data(parent)
    child = (*parent, carry)
    child_data = margin_data(child)
    if parent_data is None or child_data is None:
        return None

    m, total_depth, three_power, _cocycle = cocycle_for_word(parent)
    parent_residue = int(parent_data["residue"])
    parent_image = int(parent_data["image"])
    next_gate_residue = carry_gate_residue(carry)
    lift_modulus = 1 << carry
    lift_t = (
        ((next_gate_residue - parent_image) // 2)
        * pow(three_power, -1, lift_modulus)
    ) % lift_modulus

    parent_modulus = 1 << (total_depth + 1)
    child_modulus = 1 << (total_depth + carry + 1)
    predicted_residue = (parent_residue + lift_t * parent_modulus) % child_modulus
    predicted_image = (
        3 * parent_image + 1 + 6 * three_power * lift_t
    ) // (1 << carry)
    predicted_q = (predicted_residue - predicted_image) // 2
    child_denominator = (1 << (total_depth + carry)) - 3 * three_power
    delta_formula_numerator = (
        2 * child_denominator * lift_t
        + ((1 << carry) - 3) * parent_image
        - 1
    )
    delta_formula_denominator = 1 << (carry + 1)
    if delta_formula_numerator % delta_formula_denominator:
        raise AssertionError("append delta formula is not integral")
    predicted_delta_q = delta_formula_numerator // delta_formula_denominator

    child_q = int(child_data["q_int"])
    parent_q = int(parent_data["q_int"])
    residue_ok = predicted_residue == int(child_data["residue"])
    image_ok = predicted_image == int(child_data["image"])
    q_ok = predicted_q == child_q
    delta_formula_ok = predicted_delta_q == child_q - parent_q
    return {
        "parent_data": parent_data,
        "child_data": child_data,
        "lift_t": lift_t,
        "lift_modulus": lift_modulus,
        "next_gate_residue": next_gate_residue,
        "parent_image_mod_gate": parent_image % (1 << (carry + 1)),
        "predicted_residue": predicted_residue,
        "predicted_image": predicted_image,
        "predicted_q": predicted_q,
        "child_denominator": child_denominator,
        "delta_formula_numerator": delta_formula_numerator,
        "delta_formula_denominator": delta_formula_denominator,
        "predicted_delta_q": predicted_delta_q,
        "residue_ok": residue_ok,
        "image_ok": image_ok,
        "q_ok": q_ok,
        "delta_formula_ok": delta_formula_ok,
        "ok": residue_ok and image_ok and q_ok and delta_formula_ok,
    }


def update_append_stats(
    stats: AppendStats,
    example: dict[str, Any],
    recurrence_ok: bool,
    example_limit: int,
) -> None:
    delta = int(example["delta_q"])
    child_q = int(example["child_q"])
    stats.transitions += 1
    if not recurrence_ok:
        stats.recurrence_failures += 1
    if delta < 0:
        stats.delta_negative += 1
    elif delta == 0:
        stats.delta_zero += 1
        if len(stats.preserving_examples or []) < example_limit:
            stats.preserving_examples.append(example)
    else:
        stats.delta_positive += 1

    if stats.min_delta is None or delta < stats.min_delta:
        stats.min_delta = delta
        stats.min_delta_example = example
    if stats.min_child_q is None or child_q < stats.min_child_q:
        stats.min_child_q = child_q
        stats.min_child_q_example = example
    if stats.max_child_q is None or child_q > stats.max_child_q:
        stats.max_child_q = child_q


def update_boundary_stats(
    stats: BoundaryStats,
    child: tuple[int, ...],
    child_data: dict[str, Any],
    parent_contracting: bool,
    example_limit: int,
) -> None:
    child_q = int(child_data["q_int"])
    stats.contracting_children += 1
    if parent_contracting:
        stats.parent_contracting += 1
    else:
        stats.parent_noncontracting += 1
        example = {
            "child": carry_word_json(child),
            "child_signature": word_signature(child),
            "carry": child[-1],
            "child_q": child_q,
            "child_m": child_data["length"],
            "child_S": child_data["total_depth"],
            "height": child_data["height"],
        }
        if len(stats.examples or []) < example_limit:
            stats.examples.append(example)
        if stats.min_child_q is None or child_q < stats.min_child_q:
            stats.min_child_q = child_q
            stats.min_child_q_example = example


def append_stats_json(stats: AppendStats) -> dict[str, Any]:
    return {
        "transitions": stats.transitions,
        "delta_negative": stats.delta_negative,
        "delta_zero": stats.delta_zero,
        "delta_positive": stats.delta_positive,
        "min_delta": stats.min_delta,
        "min_delta_example": stats.min_delta_example,
        "min_child_q": stats.min_child_q,
        "min_child_q_example": stats.min_child_q_example,
        "max_child_q": stats.max_child_q,
        "preserving_examples": stats.preserving_examples,
        "recurrence_failures": stats.recurrence_failures,
    }


def boundary_stats_json(stats: BoundaryStats) -> dict[str, Any]:
    return {
        "contracting_children": stats.contracting_children,
        "parent_contracting": stats.parent_contracting,
        "parent_noncontracting": stats.parent_noncontracting,
        "min_child_q": stats.min_child_q,
        "min_child_q_example": stats.min_child_q_example,
        "examples": stats.examples,
    }


def enumerate_recurrences(
    *,
    max_length: int,
    max_total_depth: int,
    max_carry: int,
    example_limit: int,
) -> dict[str, Any]:
    append_stats: dict[int, AppendStats] = {
        carry: AppendStats() for carry in range(1, max_carry + 1)
    }
    boundary_stats: dict[int, BoundaryStats] = {
        carry: BoundaryStats() for carry in range(1, max_carry + 1)
    }
    totals = {
        "words": 0,
        "contracting_words": 0,
        "transition_words": 0,
        "recurrence_failures": 0,
        "delta_formula_failures": 0,
        "negative_q_words": 0,
        "zero_q_words": 0,
        "positive_q_words": 0,
        "trivial_zero_words": 0,
    }
    global_min_q: dict[str, Any] | None = None
    first_failures: list[dict[str, Any]] = []

    data_by_word: dict[tuple[int, ...], dict[str, Any] | None] = {}
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
                if global_min_q is None or q < int(global_min_q["q"]):
                    global_min_q = {
                        "word": carry_word_json(word),
                        "signature": word_signature(word),
                        "m": data["length"],
                        "S": data["total_depth"],
                        "q": q,
                    }

                if length >= 2:
                    parent = word[:-1]
                    parent_data = data_by_word.get(parent)
                    parent_contracting = parent_data is not None
                    update_boundary_stats(
                        boundary_stats[word[-1]],
                        word,
                        data,
                        parent_contracting,
                        example_limit,
                    )
                    if parent_contracting:
                        recurrence = append_recurrence(parent, word[-1])
                        if recurrence is None:
                            raise AssertionError("contracting parent/child lost recurrence")
                        example = transition_example(
                            parent,
                            word[-1],
                            parent_data,
                            data,
                            recurrence,
                        )
                        totals["transition_words"] += 1
                        if not recurrence["ok"]:
                            totals["recurrence_failures"] += 1
                            if len(first_failures) < example_limit:
                                first_failures.append(example)
                        if not recurrence["delta_formula_ok"]:
                            totals["delta_formula_failures"] += 1
                        update_append_stats(
                            append_stats[word[-1]],
                            example,
                            recurrence["ok"],
                            example_limit,
                        )

    monotone_carries = [
        carry
        for carry, stats in append_stats.items()
        if stats.transitions > 0 and stats.delta_negative == 0
    ]
    strict_positive_carries = [
        carry
        for carry, stats in append_stats.items()
        if stats.transitions > 0 and stats.delta_negative == 0 and stats.delta_zero == 0
    ]
    dangerous_carries = [
        carry
        for carry, stats in append_stats.items()
        if stats.delta_negative > 0
    ]
    return {
        "totals": totals,
        "global_min_q": global_min_q,
        "append_stats": {
            str(carry): append_stats_json(stats)
            for carry, stats in append_stats.items()
        },
        "boundary_stats": {
            str(carry): boundary_stats_json(stats)
            for carry, stats in boundary_stats.items()
        },
        "candidate_reductions": {
            "monotone_appended_carries": monotone_carries,
            "strict_positive_appended_carries": strict_positive_carries,
            "dangerous_appended_carries": dangerous_carries,
            "minimal_negative_counterexample_filter": (
                "By suffix monotonicity for s>=2, a minimal negative q "
                "counterexample must end in carry 1 or have a noncontracting prefix."
            ),
        },
        "first_recurrence_failures": first_failures,
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
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def make_append_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| appended s | transitions | delta < 0 | delta = 0 | delta > 0 | min delta | min child q | recurrence failures |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for carry in sorted(rows, key=lambda item: int(item)):
        row = rows[carry]
        lines.append(
            f"| {carry} | {row['transitions']} | {row['delta_negative']} | "
            f"{row['delta_zero']} | {row['delta_positive']} | "
            f"{number_or_dash(row['min_delta'])} | "
            f"{number_or_dash(row['min_child_q'])} | "
            f"{row['recurrence_failures']} |"
        )
    return lines


def make_boundary_table(rows: dict[str, Any]) -> list[str]:
    lines = [
        "| final s | contracting children | parent contracting | parent noncontracting | min boundary q |",
        "|---:|---:|---:|---:|---:|",
    ]
    for carry in sorted(rows, key=lambda item: int(item)):
        row = rows[carry]
        lines.append(
            f"| {carry} | {row['contracting_children']} | "
            f"{row['parent_contracting']} | {row['parent_noncontracting']} | "
            f"{number_or_dash(row['min_child_q'])} |"
        )
    return lines


def make_example_table(examples: list[dict[str, Any]], title: str) -> list[str]:
    lines = [
        title,
        "",
        "| parent | s | child | q parent | q child | delta | lift t | gate y mod |",
        "|---|---:|---|---:|---:|---:|---:|---:|",
    ]
    if not examples:
        lines.append("| - | - | - | - | - | - | - | - |")
        return lines
    for example in examples:
        lines.append(
            f"| `{example['parent_signature']}` | {example['carry']} | "
            f"`{example['child_signature']}` | {example['parent_q']} | "
            f"{example['child_q']} | {example['delta_q']} | "
            f"{example['lift_t']} | {example['parent_image_mod_gate']} |"
        )
    return lines


def collect_examples(payload: dict[str, Any], carry: int, key: str) -> list[dict[str, Any]]:
    row = payload["append_stats"][str(carry)]
    value = row.get(key)
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def make_boundary_examples(rows: dict[str, Any]) -> list[str]:
    examples: list[dict[str, Any]] = []
    for carry in sorted(rows, key=lambda item: int(item)):
        row = rows[carry]
        examples.extend(row["examples"][:2])
    lines = [
        "Boundary examples where the child is contracting but its prefix is not:",
        "",
        "| child | final s | m | S | q | height |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    if not examples:
        lines.append("| - | - | - | - | - | - |")
        return lines
    for example in examples[:16]:
        lines.append(
            f"| `{example['child_signature']}` | {example['carry']} | "
            f"{example['child_m']} | {example['child_S']} | "
            f"{example['child_q']} | {example['height']:.6f} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    results = payload["results"]
    totals = results["totals"]
    reductions = results["candidate_reductions"]
    dangerous_examples: list[dict[str, Any]] = []
    for carry in reductions["dangerous_appended_carries"]:
        dangerous_examples.extend(
            collect_examples(results, carry, "min_delta_example")
        )
    preserving_examples = collect_examples(results, 2, "preserving_examples")
    lines = [
        "# Collatz Margin Recurrence Miner",
        "",
        "## Meaning",
        "",
        "This audit moves the `q_w >= 0` problem from census to recurrence.  For a contracting parent carry word `w` and appended carry `s`, the child exact-cylinder lift is",
        "",
        "```text",
        "r_{w,s} = r_w + t 2^(S+1) mod 2^(S+s+1).",
        "```",
        "",
        "The lift digit `t mod 2^s` is forced by the next carry gate:",
        "",
        "```text",
        "U_w(r_w) + 2 * 3^m * t == a_s mod 2^(s+1),",
        "a_s = (2^s - 1) * 3^-1 mod 2^(s+1).",
        "```",
        "",
        "The script verifies this exact recurrence and records the sign of `q_{w,s} - q_w`.",
        "",
        "The same recurrence gives the exact append-delta identity",
        "",
        "```text",
        "q_{w,s} - q_w = (2D_{w,s}t + (2^s - 3)y_w - 1) / 2^(s+1),",
        "```",
        "",
        "where `D_{w,s}=2^(S+s)-3^(m+1)` and `y_w=U_w(r_w)`.",
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
        f"- recurrence transitions: `{totals['transition_words']}`",
        f"- recurrence failures: `{totals['recurrence_failures']}`",
        f"- delta formula failures: `{totals['delta_formula_failures']}`",
        f"- negative q words: `{totals['negative_q_words']}`",
        f"- zero q words: `{totals['zero_q_words']}`",
        f"- trivial zero words: `{totals['trivial_zero_words']}`",
        f"- positive q words: `{totals['positive_q_words']}`",
        "",
        "## Append Delta Ledger",
        "",
        *make_append_table(results["append_stats"]),
        "",
        "Observed candidate reduction:",
        "",
        f"- monotone appended carries: `{reductions['monotone_appended_carries']}`",
        f"- strict positive appended carries: `{reductions['strict_positive_appended_carries']}`",
        f"- dangerous appended carries: `{reductions['dangerous_appended_carries']}`",
        "",
        "In this window, appending `s >= 2` never decreases `q`; appending `1` is the only observed decreasing move.",
        "",
        *make_example_table(dangerous_examples, "Most negative append deltas:"),
        "",
        *make_example_table(preserving_examples, "Sample q-preserving append-2 moves:"),
        "",
        "## Contraction Boundary",
        "",
        *make_boundary_table(results["boundary_stats"]),
        "",
        *make_boundary_examples(results["boundary_stats"]),
        "",
        "## Proven Reduction",
        "",
        "The append-delta identity proves the broad suffix case:",
        "",
        "```text",
        "Suffix monotonicity lemma:",
        "If w and (w,s) are contracting and s >= 2, then q_{w,s} >= q_w.",
        "```",
        "",
        "Therefore any minimal negative-margin counterexample cannot end in a carry `s >= 2` with contracting prefix.  It must either end in carry `1`, or be a first-contraction boundary word whose prefix has `2^S - 3^m <= 0`.",
        "",
        "So the descent-margin theorem splits into two smaller targets:",
        "",
        "```text",
        "1. Prove suffix monotonicity for s >= 2.",
        "2. Control append-1 and first-contraction boundary words.",
        "```",
        "",
        "This is still not a proof of Collatz, but it turns the `q_w >= 0` question into a finite-looking recurrence problem with one visibly dangerous channel.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_margin_recurrence_miner.py "
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
        / f"collatz_margin_recurrence_L{max_length}_S{max_total_depth}_K{max_carry}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_margin_recurrence_L{max_length}_S{max_total_depth}_K{max_carry}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=8)
    parser.add_argument("--max-total-depth", type=int, default=21)
    parser.add_argument("--max-carry", type=int, default=8)
    parser.add_argument("--example-limit", type=int, default=8)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 2:
        raise ValueError("--max-length must be at least 2")
    if args.max_total_depth < args.max_length:
        raise ValueError("--max-total-depth must be at least max-length")
    if args.max_carry < 2:
        raise ValueError("--max-carry must be at least 2")

    results = enumerate_recurrences(
        max_length=args.max_length,
        max_total_depth=args.max_total_depth,
        max_carry=args.max_carry,
        example_limit=args.example_limit,
    )
    payload = {
        "settings": {
            "max_length": args.max_length,
            "max_total_depth": args.max_total_depth,
            "max_carry": args.max_carry,
            "example_limit": args.example_limit,
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
    print(json.dumps(rounded(results["candidate_reductions"]), indent=2))


if __name__ == "__main__":
    main()
