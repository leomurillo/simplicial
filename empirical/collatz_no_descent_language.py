"""No-descent carry language for the second half of the Collatz program.

Assume the margin lemma:

    every contracting carry block has q_w >= 0,

with equality only harmless/trivial.  Then a positive odd integer can avoid
falling below its starting value for m accelerated odd steps only if every
prefix carry word stays noncontracting:

    S_j <= floor(j log_2 3)  for every prefix j <= m.

This script studies that avoidance language.  It is the finite shadow of the
second half of the program: prove that no positive integer can remain in this
language forever.  The computation shows what is accessible now:

* exact counts of avoiding carry words;
* exact 2-adic/Haar cylinder mass of the avoiding set;
* extremal symbolic corridors such as all-ones and balanced Sturmian-like
  prefixes;
* concrete residues for those corridors.

The result is an "almost all" statement, not a pointwise proof.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)


def log2sumexp(values: list[float]) -> float:
    if not values:
        return float("-inf")
    top = max(values)
    if top == float("-inf"):
        return top
    return top + math.log2(sum(2.0 ** (value - top) for value in values))


def word_runs(word: tuple[int, ...]) -> list[tuple[int, int]]:
    if not word:
        return []
    runs: list[tuple[int, int]] = []
    current = word[0]
    count = 1
    for carry in word[1:]:
        if carry == current:
            count += 1
            continue
        runs.append((current, count))
        current = carry
        count = 1
    runs.append((current, count))
    return runs


def word_signature(word: tuple[int, ...], limit: int = 14) -> str:
    parts = [
        str(carry) if count == 1 else f"{carry}^{count}"
        for carry, count in word_runs(word)
    ]
    if len(parts) <= limit:
        return "(" + " ".join(parts) + ")"
    head = " ".join(parts[: limit // 2])
    tail = " ".join(parts[-(limit // 2) :])
    return f"({head} ... {tail})"


def cocycle_for_word(word: tuple[int, ...]) -> tuple[int, int, int, int]:
    total_depth = 0
    cocycle = 0
    for carry in word:
        cocycle = 3 * cocycle + (1 << total_depth)
        total_depth += carry
    length = len(word)
    return length, total_depth, 3**length, cocycle


def branch_data(word: tuple[int, ...]) -> dict[str, Any]:
    length, total_depth, multiplier, cocycle = cocycle_for_word(word)
    denominator_power = 1 << total_depth
    modulus = denominator_power << 1
    residue = ((denominator_power - cocycle) * pow(multiplier, -1, modulus)) % modulus
    first_n = residue if residue > 0 else modulus
    image_num = multiplier * first_n + cocycle
    if image_num % denominator_power:
        raise AssertionError("domain residue failed divisibility")
    image = image_num // denominator_power
    height = total_depth - length * LOG2_3
    return {
        "signature": word_signature(word),
        "word": list(word),
        "length": length,
        "total_depth": total_depth,
        "height": height,
        "residue": str(residue),
        "modulus_log2": total_depth + 1,
        "first_n": str(first_n),
        "first_n_log2": math.log2(first_n),
        "image": str(image),
        "image_log2": math.log2(image),
        "gain_log2": math.log2(image) - math.log2(first_n),
    }


def all_ones_word(length: int) -> tuple[int, ...]:
    return (1,) * length


def balanced_word(length: int) -> tuple[int, ...]:
    """Maximal prefix under S_j <= floor(j log2 3)."""

    out = []
    previous = 0
    for index in range(1, length + 1):
        current = math.floor(index * LOG2_3)
        out.append(current - previous)
        previous = current
    return tuple(out)


def low_height_rows(max_length: int) -> list[dict[str, Any]]:
    state: dict[int, int] = {0: 1}
    rows = []
    for length in range(1, max_length + 1):
        cap = math.floor(length * LOG2_3)
        next_state: dict[int, int] = {}
        for total_depth, count in state.items():
            max_carry = cap - total_depth
            for carry in range(1, max_carry + 1):
                new_depth = total_depth + carry
                next_state[new_depth] = next_state.get(new_depth, 0) + count
        state = next_state
        count = sum(state.values())
        log_count = math.log2(count) if count else float("-inf")
        mass_log_terms = [
            math.log2(depth_count) - total_depth
            for total_depth, depth_count in state.items()
        ]
        log_mass = log2sumexp(mass_log_terms)
        rows.append(
            {
                "length": length,
                "max_total_depth": cap,
                "states": len(state),
                "word_count": count,
                "log2_word_count": log_count,
                "log2_count_per_step": log_count / length
                if count
                else float("-inf"),
                "cylinder_mass": 2.0**log_mass if log_mass > -1070 else 0.0,
                "log2_cylinder_mass": log_mass,
                "log2_mass_per_step": log_mass / length
                if log_mass != float("-inf")
                else float("-inf"),
                "min_total_depth": min(state) if state else None,
                "max_reached_depth": max(state) if state else None,
            }
        )
    return rows


def selected_lengths(max_length: int) -> list[int]:
    candidates = [
        1,
        2,
        3,
        4,
        5,
        8,
        10,
        12,
        16,
        20,
        24,
        30,
        40,
        60,
        80,
        100,
        120,
        160,
        200,
        240,
        300,
    ]
    out = [length for length in candidates if length <= max_length]
    if max_length not in out:
        out.append(max_length)
    return sorted(set(out))


def witness_rows(lengths: list[int]) -> list[dict[str, Any]]:
    rows = []
    for length in lengths:
        for label, word in [
            ("all-ones", all_ones_word(length)),
            ("balanced-boundary", balanced_word(length)),
        ]:
            data = branch_data(word)
            data["label"] = label
            rows.append(data)
    return rows


def summarize_tail(rows: list[dict[str, Any]]) -> dict[str, Any]:
    half = max(1, len(rows) // 2)
    tail = rows[half - 1 :]
    return {
        "final": rows[-1],
        "tail_mean_log2_count_per_step": sum(
            row["log2_count_per_step"] for row in tail
        )
        / len(tail),
        "tail_mean_log2_mass_per_step": sum(
            row["log2_mass_per_step"] for row in tail
        )
        / len(tail),
    }


def rounded(value: object) -> object:
    if isinstance(value, float):
        if math.isinf(value):
            return "inf" if value > 0 else "-inf"
        return round(value, 10)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    return value


def make_avoidance_table(rows: list[dict[str, Any]], max_length: int) -> list[str]:
    row_by_length = {row["length"]: row for row in rows}
    lines = [
        "| m | words | log2 words/m | mass | log2 mass | log2 mass/m | states |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for length in selected_lengths(max_length):
        row = row_by_length[length]
        lines.append(
            f"| {length} | {row['word_count']} | "
            f"{row['log2_count_per_step']:.6f} | "
            f"{row['cylinder_mass']:.12g} | "
            f"{row['log2_cylinder_mass']:.6f} | "
            f"{row['log2_mass_per_step']:.6f} | "
            f"{row['states']} |"
        )
    return lines


def make_witness_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| label | m | S | H | log2 n0 | log2 image | log2 gain | word |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['label']} | {row['length']} | {row['total_depth']} | "
            f"{row['height']:.6f} | {row['first_n_log2']:.6f} | "
            f"{row['image_log2']:.6f} | {row['gain_log2']:.6f} | "
            f"`{row['signature']}` |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    tail = payload["summary"]
    final = tail["final"]
    lines = [
        "# Collatz No-Descent Carry Language",
        "",
        "## Meaning",
        "",
        "Assume the margin theorem candidate is true: every contracting carry block decreases the first positive integer in its exact cylinder, and all larger representatives too.  Then an orbit can avoid descent below its current value for `m` accelerated odd steps only if every prefix is noncontracting:",
        "",
        "```text",
        "S_j <= floor(j log2(3))  for every j <= m.",
        "```",
        "",
        "This report studies that avoidance language.  It is the second half of the program in finite form.",
        "",
        "## What We Can Know",
        "",
        "The avoiding language is symbolically large but arithmetically small.  Its word count grows exponentially, while its exact cylinder mass decays exponentially.  Therefore the margin theorem would imply a density-one total stopping statement: the set of odd integers with no descent by step `m` has density at most the mass below.",
        "",
        f"- max length: `{settings['max_length']}`",
        f"- final word count: `{final['word_count']}`",
        f"- final log2 word count / step: `{final['log2_count_per_step']:.12f}`",
        f"- final cylinder mass: `{final['cylinder_mass']:.12g}`",
        f"- final log2 mass / step: `{final['log2_mass_per_step']:.12f}`",
        f"- tail mean log2 mass / step: `{tail['tail_mean_log2_mass_per_step']:.12f}`",
        "",
        "## Avoidance Counts And Mass",
        "",
        *make_avoidance_table(payload["rows"], settings["max_length"]),
        "",
        "## Extremal Corridors",
        "",
        "`all-ones` is the maximally expanding symbolic corridor; its infinite 2-adic limit is `-1`.  `balanced-boundary` is the maximal prefix that stays just under the height boundary.",
        "",
        *make_witness_table(payload["witnesses"]),
        "",
        "## Interpretation",
        "",
        "The second half is exactly the infinite-intersection problem.  The finite bad sets shrink in density, but the infinite symbolic language is nonempty in the 2-adics.  The all-ones corridor already shows why measure is not enough: it is a perfectly valid infinite 2-adic carry sequence, but it corresponds to `-1`, not a positive escaping integer.",
        "",
        "So the remaining pointwise theorem is:",
        "",
        "```text",
        "No positive odd integer has an infinite carry sequence with",
        "S_j <= floor(j log2(3)) for every prefix j.",
        "```",
        "",
        "Equivalently: every positive odd integer other than the trivial fixed point eventually has a positive-height prefix block, hence a descent block if the margin theorem holds.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_no_descent_language.py --max-length {settings['max_length']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_no_descent_language_L{max_length}.md"


def default_json_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_no_descent_language_L{max_length}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=300)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")

    rows = low_height_rows(args.max_length)
    witnesses = witness_rows(selected_lengths(min(args.max_length, 120)))
    payload = {
        "settings": {
            "max_length": args.max_length,
        },
        "rows": rows,
        "summary": summarize_tail(rows),
        "witnesses": witnesses,
    }

    report_path = args.report or default_report_path(args.max_length)
    json_path = args.json or default_json_path(args.max_length)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["summary"]), indent=2))


if __name__ == "__main__":
    main()
