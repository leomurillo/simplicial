"""Carry-word algebra for the accelerated odd Collatz map.

The accelerated odd map is the countable-branch system

    U_s(n) = (3n + 1) / 2^s,    s = v2(3n + 1), s >= 1.

For a carry word w = (s_1, ..., s_m), the composed branch has the exact
affine form

    U_w(n) = (3^m n + C_w) / 2^S,
    S = s_1 + ... + s_m.

The cocycle C_w obeys

    C_empty = 0,
    C_{w,s} = 3 C_w + 2^S.

This script enumerates a finite carry-word window, computes the affine
cocycle, the 2-adic exact-domain cylinder, and cycle candidates

    n = C_w / (2^S - 3^m).

It is a proof-facing algebraic audit, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)


@dataclass(frozen=True)
class WordItem:
    word: tuple[int, ...]
    length: int
    total_depth: int
    cocycle: int
    denominator: int
    drift: float
    gcd_cocycle_denominator: int
    reduced_denominator: int | None
    cycle_candidate: int | None
    exact_cycle: bool
    primitive_period: int


@dataclass
class LengthStats:
    words: int = 0
    positive_denominator: int = 0
    nonpositive_denominator: int = 0
    integer_candidates: int = 0
    exact_cycles: int = 0
    nontrivial_exact_cycles: int = 0
    primitive_exact_cycles: int = 0
    min_positive_drift: float | None = None
    max_positive_drift: float | None = None
    min_reduced_denominator: int | None = None
    min_noninteger_reduced_denominator: int | None = None
    haar_mass: float = 0.0


class SmallestKeeper:
    """Keep a bounded set of items with the smallest score."""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.serial = 0
        self.heap: list[tuple[float, int, WordItem]] = []

    def push(self, score: float, item: WordItem) -> None:
        if self.limit <= 0:
            return
        entry = (-score, self.serial, item)
        self.serial += 1
        if len(self.heap) < self.limit:
            heapq.heappush(self.heap, entry)
            return
        if score < -self.heap[0][0]:
            heapq.heapreplace(self.heap, entry)

    def items(self) -> list[WordItem]:
        return [
            item
            for _score, _serial, item in sorted(
                self.heap,
                key=lambda entry: (-entry[0], entry[1]),
            )
        ]


def vp(n: int, prime: int) -> int:
    if n <= 0:
        raise ValueError("vp is defined here only for positive integers")
    depth = 0
    while n % prime == 0:
        n //= prime
        depth += 1
    return depth


def accelerated_odd_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("accelerated odd step requires a positive odd integer")
    raised = 3 * n + 1
    depth = vp(raised, 2)
    return raised >> depth, depth


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period != 0:
            continue
        root = word[:period]
        if root * (len(word) // period) == word:
            return period
    return len(word)


def is_trivial_one_cycle_power(word: tuple[int, ...], candidate: int | None) -> bool:
    return candidate == 1 and bool(word) and all(depth == 2 for depth in word)


def verify_cycle_candidate(candidate: int, word: tuple[int, ...]) -> bool:
    if candidate <= 0 or candidate % 2 == 0:
        return False
    n = candidate
    carries: list[int] = []
    for _ in word:
        n, carry = accelerated_odd_step(n)
        carries.append(carry)
    return n == candidate and tuple(carries) == word


def make_word_item(word: tuple[int, ...], total_depth: int, cocycle: int) -> WordItem:
    length = len(word)
    denominator = (1 << total_depth) - (3**length)
    drift = total_depth - length * LOG2_3
    reduced_denominator: int | None = None
    gcd_value = 0
    candidate: int | None = None
    exact_cycle = False

    if denominator > 0:
        gcd_value = math.gcd(cocycle, denominator)
        reduced_denominator = denominator // gcd_value
        if reduced_denominator == 1:
            candidate = cocycle // denominator
            exact_cycle = verify_cycle_candidate(candidate, word)

    return WordItem(
        word=word,
        length=length,
        total_depth=total_depth,
        cocycle=cocycle,
        denominator=denominator,
        drift=drift,
        gcd_cocycle_denominator=gcd_value,
        reduced_denominator=reduced_denominator,
        cycle_candidate=candidate,
        exact_cycle=exact_cycle,
        primitive_period=primitive_period(word),
    )


def exact_domain_residue(item: WordItem) -> tuple[int, int]:
    """Return the exact carry-cylinder residue modulo 2^(S+1)."""

    modulus = 1 << (item.total_depth + 1)
    multiplier = pow(3, item.length, modulus)
    inverse = pow(multiplier, -1, modulus)
    residue = ((1 << item.total_depth) - item.cocycle) * inverse
    return residue % modulus, modulus


def word_text(word: tuple[int, ...]) -> str:
    return "(" + ",".join(str(depth) for depth in word) + ")"


def item_json(item: WordItem) -> dict[str, Any]:
    residue, modulus = exact_domain_residue(item)
    return {
        "word": list(item.word),
        "length": item.length,
        "total_depth": item.total_depth,
        "cocycle": item.cocycle,
        "denominator": item.denominator,
        "drift": item.drift,
        "gcd_cocycle_denominator": item.gcd_cocycle_denominator,
        "reduced_denominator": item.reduced_denominator,
        "cycle_candidate": item.cycle_candidate,
        "exact_cycle": item.exact_cycle,
        "primitive_period": item.primitive_period,
        "domain_residue": residue,
        "domain_modulus": modulus,
    }


def update_length_stats(stats: LengthStats, item: WordItem) -> None:
    stats.words += 1
    stats.haar_mass += 2.0 ** (-item.total_depth)
    if item.denominator > 0:
        stats.positive_denominator += 1
        stats.min_positive_drift = (
            item.drift
            if stats.min_positive_drift is None
            else min(stats.min_positive_drift, item.drift)
        )
        stats.max_positive_drift = (
            item.drift
            if stats.max_positive_drift is None
            else max(stats.max_positive_drift, item.drift)
        )
        if item.reduced_denominator is not None:
            stats.min_reduced_denominator = (
                item.reduced_denominator
                if stats.min_reduced_denominator is None
                else min(stats.min_reduced_denominator, item.reduced_denominator)
            )
            if item.reduced_denominator > 1:
                stats.min_noninteger_reduced_denominator = (
                    item.reduced_denominator
                    if stats.min_noninteger_reduced_denominator is None
                    else min(stats.min_noninteger_reduced_denominator, item.reduced_denominator)
                )
    else:
        stats.nonpositive_denominator += 1

    if item.cycle_candidate is not None:
        stats.integer_candidates += 1
    if item.exact_cycle:
        stats.exact_cycles += 1
        if item.primitive_period == item.length:
            stats.primitive_exact_cycles += 1
        if not is_trivial_one_cycle_power(item.word, item.cycle_candidate):
            stats.nontrivial_exact_cycles += 1


def enumerate_window(
    *,
    max_length: int,
    max_carry: int,
    top_limit: int,
) -> dict[str, Any]:
    length_stats: defaultdict[int, LengthStats] = defaultdict(LengthStats)
    total_words = 0
    total_positive = 0
    total_integer_candidates = 0
    total_exact_cycles = 0
    total_nontrivial_exact_cycles = 0
    total_haar_mass = 0.0
    carry_histogram: Counter[int] = Counter()
    total_depth_histogram: Counter[int] = Counter()
    exact_cycles: list[WordItem] = []
    nontrivial_exact_cycles: list[WordItem] = []
    near_positive_drift = SmallestKeeper(top_limit)
    best_divisibility_obstructions = SmallestKeeper(top_limit)

    def visit(word: tuple[int, ...], total_depth: int, cocycle: int) -> None:
        nonlocal total_words
        nonlocal total_positive
        nonlocal total_integer_candidates
        nonlocal total_exact_cycles
        nonlocal total_nontrivial_exact_cycles
        nonlocal total_haar_mass

        if word:
            item = make_word_item(word, total_depth, cocycle)
            stats = length_stats[item.length]
            update_length_stats(stats, item)
            total_words += 1
            total_haar_mass += 2.0 ** (-item.total_depth)
            carry_histogram.update(word)
            total_depth_histogram[item.total_depth] += 1
            if item.denominator > 0:
                total_positive += 1
                near_positive_drift.push(item.drift, item)
                if item.reduced_denominator and item.reduced_denominator > 1:
                    best_divisibility_obstructions.push(
                        float(item.reduced_denominator),
                        item,
                    )
            if item.cycle_candidate is not None:
                total_integer_candidates += 1
            if item.exact_cycle:
                total_exact_cycles += 1
                exact_cycles.append(item)
                if not is_trivial_one_cycle_power(item.word, item.cycle_candidate):
                    total_nontrivial_exact_cycles += 1
                    nontrivial_exact_cycles.append(item)

        if len(word) >= max_length:
            return

        for carry in range(1, max_carry + 1):
            next_word = (*word, carry)
            next_cocycle = 3 * cocycle + (1 << total_depth)
            visit(next_word, total_depth + carry, next_cocycle)

    visit((), 0, 0)

    captured_mass_by_length = {
        length: stats.haar_mass
        for length, stats in sorted(length_stats.items())
    }
    expected_captured_mass_by_length = {
        length: (1.0 - 2.0 ** (-max_carry)) ** length
        for length in sorted(length_stats)
    }

    return {
        "settings": {
            "max_length": max_length,
            "max_carry": max_carry,
            "top_limit": top_limit,
        },
        "totals": {
            "words": total_words,
            "positive_denominator_words": total_positive,
            "integer_candidates": total_integer_candidates,
            "exact_cycles": total_exact_cycles,
            "nontrivial_exact_cycles": total_nontrivial_exact_cycles,
            "haar_mass_in_window": total_haar_mass,
        },
        "length_stats": {
            length: stats
            for length, stats in sorted(length_stats.items())
        },
        "captured_mass_by_length": captured_mass_by_length,
        "expected_captured_mass_by_length": expected_captured_mass_by_length,
        "carry_histogram": dict(sorted(carry_histogram.items())),
        "total_depth_histogram": dict(sorted(total_depth_histogram.items())),
        "exact_cycles": sorted(
            exact_cycles,
            key=lambda item: (item.cycle_candidate or 0, item.length, item.word),
        ),
        "nontrivial_exact_cycles": sorted(
            nontrivial_exact_cycles,
            key=lambda item: (item.cycle_candidate or 0, item.length, item.word),
        ),
        "near_positive_drift": near_positive_drift.items(),
        "best_divisibility_obstructions": best_divisibility_obstructions.items(),
    }


def stats_json(stats: LengthStats) -> dict[str, Any]:
    return {
        "words": stats.words,
        "positive_denominator": stats.positive_denominator,
        "nonpositive_denominator": stats.nonpositive_denominator,
        "integer_candidates": stats.integer_candidates,
        "exact_cycles": stats.exact_cycles,
        "nontrivial_exact_cycles": stats.nontrivial_exact_cycles,
        "primitive_exact_cycles": stats.primitive_exact_cycles,
        "min_positive_drift": stats.min_positive_drift,
        "max_positive_drift": stats.max_positive_drift,
        "min_reduced_denominator": stats.min_reduced_denominator,
        "min_noninteger_reduced_denominator": stats.min_noninteger_reduced_denominator,
        "haar_mass": stats.haar_mass,
    }


def rounded(value: object) -> object:
    if isinstance(value, float):
        return round(value, 10)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    if isinstance(value, tuple):
        return [rounded(inner) for inner in value]
    return value


def make_item_table(items: list[WordItem], *, include_candidate: bool) -> list[str]:
    if not items:
        return ["_None in this finite window._"]

    header = (
        "| word | m | S | drift | C_w | 2^S-3^m | reduced denom | "
        "candidate | exact | domain cylinder |"
    )
    lines = [
        header,
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in items:
        residue, modulus = exact_domain_residue(item)
        candidate = (
            str(item.cycle_candidate)
            if include_candidate and item.cycle_candidate is not None
            else "-"
        )
        reduced = item.reduced_denominator if item.reduced_denominator is not None else "-"
        lines.append(
            f"| `{word_text(item.word)}` | {item.length} | {item.total_depth} | "
            f"{item.drift:.6f} | {item.cocycle} | {item.denominator} | "
            f"{reduced} | {candidate} | {item.exact_cycle} | "
            f"`n = {residue} mod {modulus}` |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    totals = payload["totals"]
    length_stats: dict[int, LengthStats] = payload["length_stats"]

    lines = [
        "# Collatz Carry-Word Algebra",
        "",
        "## Status",
        "",
        "This report enumerates a finite window in the carry-word algebra of the accelerated odd Collatz map.  The finite window is a diagnostic slice of an infinite pro-2 carry tower.",
        "",
        f"- carry alphabet: `1..{settings['max_carry']}`",
        f"- max word length: `{settings['max_length']}`",
        f"- words enumerated: `{totals['words']}`",
        f"- positive-denominator words: `{totals['positive_denominator_words']}`",
        f"- integer cycle candidates: `{totals['integer_candidates']}`",
        f"- exact cycles: `{totals['exact_cycles']}`",
        f"- nontrivial exact cycles: `{totals['nontrivial_exact_cycles']}`",
        f"- Haar mass represented by the truncated carry alphabet across all listed lengths: `{totals['haar_mass_in_window']:.10f}`",
        "",
        "## Algebra",
        "",
        "For a word `w=(s1,...,sm)`,",
        "",
        "```text",
        "U_w(n) = (3^m n + C_w) / 2^S",
        "S = s1 + ... + sm",
        "C_empty = 0",
        "C_{w,s} = 3 C_w + 2^S",
        "```",
        "",
        "Composition is a semigroup law:",
        "",
        "```text",
        "C_{uv} = 3^|v| C_u + 2^S(u) C_v",
        "S_{uv} = S_u + S_v",
        "```",
        "",
        "A cycle with carry word `w` would have to satisfy",
        "",
        "```text",
        "n = C_w / (2^S - 3^m)",
        "```",
        "",
        "and also pass the exact carry simulation test.",
        "",
        "## Length Summary",
        "",
        "| m | words | positive denom | nonpositive denom | integer candidates | exact cycles | nontrivial exact cycles | min positive drift | min noninteger reduced denom | Haar mass |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for length, stats in length_stats.items():
        min_drift = "-" if stats.min_positive_drift is None else f"{stats.min_positive_drift:.6f}"
        min_reduced = (
            "-"
            if stats.min_noninteger_reduced_denominator is None
            else str(stats.min_noninteger_reduced_denominator)
        )
        lines.append(
            f"| {length} | {stats.words} | {stats.positive_denominator} | "
            f"{stats.nonpositive_denominator} | {stats.integer_candidates} | "
            f"{stats.exact_cycles} | {stats.nontrivial_exact_cycles} | "
            f"{min_drift} | {min_reduced} | {stats.haar_mass:.10f} |"
        )

    lines += [
        "",
        "## Exact Cycle Candidates",
        "",
        "The expected trivial family is the one-cycle word `(2)` and its powers, all giving `n=1`.",
        "",
        *make_item_table(payload["exact_cycles"], include_candidate=True),
        "",
        "## Nontrivial Exact Cycles",
        "",
        *make_item_table(payload["nontrivial_exact_cycles"], include_candidate=True),
        "",
        "## Near-Resonant Positive-Drift Words",
        "",
        "These are the words with the smallest positive `S - m log2(3)` in the finite window.  Positive drift is required for a positive cycle denominator.",
        "",
        *make_item_table(payload["near_positive_drift"], include_candidate=False),
        "",
        "## Best Divisibility Obstructions",
        "",
        "For positive-denominator words that do not give integer candidates, the reduced denominator is `(2^S - 3^m)/gcd(C_w, 2^S - 3^m)`.  Small values are the closest algebraic misses.",
        "",
        *make_item_table(payload["best_divisibility_obstructions"], include_candidate=False),
        "",
        "## Backwards From The Goal",
        "",
        "To rule out nontrivial cycles, the algebraic task is: for every primitive carry word not generated by `(2)`, prove that either `2^S - 3^m` does not divide `C_w`, or the resulting integer fails the exact carry word.  The finite report performs that test only inside the enumerated window.",
        "",
        "To rule out escape, the algebraic task is different: control the height cocycle",
        "",
        "```text",
        "H(w) = S(w) - |w| log2(3)",
        "```",
        "",
        "along infinite admissible carry words.  Escape would require prefixes whose average carry depth fails to beat `log2(3)` often enough to overcome the affine constants.",
        "",
        "So the needed object is not a single finite matrix.  It is the filtered pro-2 carry-word groupoid: carry words, their exact domain cylinders `n = r_w mod 2^(S+1)`, the cocycle `C_w`, and the height cocycle `H(w)`.  Finite quotient adjacency matrices are representations of this algebra, not the algebra itself.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_carry_word_algebra.py --max-length {settings['max_length']} --max-carry {settings['max_carry']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, max_carry: int) -> Path:
    return Path("empirical/reports") / f"collatz_carry_word_algebra_L{max_length}_K{max_carry}.md"


def default_json_path(max_length: int, max_carry: int) -> Path:
    return Path("empirical/reports") / f"collatz_carry_word_algebra_L{max_length}_K{max_carry}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=8)
    parser.add_argument("--max-carry", type=int, default=6)
    parser.add_argument("--top-limit", type=int, default=16)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_carry < 1:
        raise ValueError("--max-carry must be at least 1")

    payload = enumerate_window(
        max_length=args.max_length,
        max_carry=args.max_carry,
        top_limit=args.top_limit,
    )

    report_path = args.report or default_report_path(args.max_length, args.max_carry)
    json_path = args.json or default_json_path(args.max_length, args.max_carry)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(make_report(payload), encoding="utf-8")

    json_payload = {
        "settings": payload["settings"],
        "totals": payload["totals"],
        "length_stats": {
            length: stats_json(stats)
            for length, stats in payload["length_stats"].items()
        },
        "captured_mass_by_length": payload["captured_mass_by_length"],
        "expected_captured_mass_by_length": payload["expected_captured_mass_by_length"],
        "carry_histogram": payload["carry_histogram"],
        "total_depth_histogram": payload["total_depth_histogram"],
        "exact_cycles": [item_json(item) for item in payload["exact_cycles"]],
        "nontrivial_exact_cycles": [
            item_json(item) for item in payload["nontrivial_exact_cycles"]
        ],
        "near_positive_drift": [
            item_json(item) for item in payload["near_positive_drift"]
        ],
        "best_divisibility_obstructions": [
            item_json(item) for item in payload["best_divisibility_obstructions"]
        ],
    }
    json_path.write_text(json.dumps(rounded(json_payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["totals"]), indent=2))


if __name__ == "__main__":
    main()
