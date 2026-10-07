"""Primitive carry-necklace sieve for Collatz cycle candidates.

This is the cycle-facing companion to ``collatz_carry_word_algebra.py``.  It
works by total word length ``m`` and total carry depth ``S`` rather than by a
rectangular carry alphabet alone.

For a carry word w = (s_1, ..., s_m), the accelerated odd map has

    U_w(n) = (3^m n + C_w) / 2^S.

Any cycle with this carry word must satisfy

    n = C_w / (2^S - 3^m).

Since cyclic rotations of a word describe the same periodic orbit from
different base points, this script tests primitive necklaces: one canonical
representative per cyclic rotation class, excluding powers of shorter words.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from collatz_carry_word_algebra import (
    LOG2_3,
    WordItem,
    exact_domain_residue,
    is_trivial_one_cycle_power,
    item_json,
    make_word_item,
    primitive_period,
    verify_cycle_candidate,
    word_text,
)


@dataclass
class PairStats:
    compositions: int = 0
    necklaces: int = 0
    imprimitive_necklaces: int = 0
    primitive_necklaces: int = 0
    positive_denominator: int = 0
    integer_candidate_necklaces: int = 0
    exact_cycle_necklaces: int = 0
    nontrivial_exact_cycle_necklaces: int = 0
    min_reduced_denominator: int | None = None
    min_nonzero_modular_residue: int | None = None


@dataclass(frozen=True)
class NecklaceRecord:
    representative: tuple[int, ...]
    length: int
    total_depth: int
    denominator: int
    drift: float
    best_rotation: WordItem
    best_reduced_denominator: int | None
    best_modular_residue: int | None
    integer_rotation: WordItem | None
    exact_rotation: WordItem | None
    nontrivial_exact: bool


class SmallestKeeper:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.serial = 0
        self.heap: list[tuple[float, int, NecklaceRecord]] = []

    def push(self, score: float, record: NecklaceRecord) -> None:
        if self.limit <= 0:
            return
        entry = (-score, self.serial, record)
        self.serial += 1
        if len(self.heap) < self.limit:
            heapq.heappush(self.heap, entry)
            return
        if score < -self.heap[0][0]:
            heapq.heapreplace(self.heap, entry)

    def records(self) -> list[NecklaceRecord]:
        return [
            record
            for _score, _serial, record in sorted(
                self.heap,
                key=lambda entry: (-entry[0], entry[1]),
            )
        ]


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def word_cocycle(word: tuple[int, ...]) -> tuple[int, int]:
    total_depth = 0
    cocycle = 0
    for carry in word:
        cocycle = 3 * cocycle + (1 << total_depth)
        total_depth += carry
    return total_depth, cocycle


def bounded_compositions(
    total: int,
    parts: int,
    max_part: int | None,
) -> Iterable[tuple[int, ...]]:
    if parts == 0:
        if total == 0:
            yield ()
        return
    if parts == 1:
        if total >= 1 and (max_part is None or total <= max_part):
            yield (total,)
        return

    upper = total - parts + 1
    if max_part is not None:
        upper = min(upper, max_part)
    for first in range(1, upper + 1):
        remaining = total - first
        if max_part is not None and remaining > max_part * (parts - 1):
            continue
        for suffix in bounded_compositions(remaining, parts - 1, max_part):
            yield (first, *suffix)


def modular_residue(item: WordItem) -> int | None:
    if item.denominator <= 0:
        return None
    residue = item.cocycle % item.denominator
    if residue == 0:
        return 0
    return min(residue, item.denominator - residue)


def analyze_necklace(word: tuple[int, ...]) -> NecklaceRecord:
    length = len(word)
    total_depth = sum(word)
    denominator = (1 << total_depth) - (3**length)
    drift = total_depth - length * LOG2_3

    best_rotation: WordItem | None = None
    best_reduced_denominator: int | None = None
    best_modular_residue: int | None = None
    integer_rotation: WordItem | None = None
    exact_rotation: WordItem | None = None

    for rotation in rotations(word):
        rotation_depth, cocycle = word_cocycle(rotation)
        item = make_word_item(rotation, rotation_depth, cocycle)
        residue = modular_residue(item)
        if item.reduced_denominator is not None and item.reduced_denominator > 1:
            if (
                best_reduced_denominator is None
                or item.reduced_denominator < best_reduced_denominator
            ):
                best_reduced_denominator = item.reduced_denominator
                best_rotation = item
        if residue is not None and residue > 0:
            if best_modular_residue is None or residue < best_modular_residue:
                best_modular_residue = residue
                if best_rotation is None:
                    best_rotation = item
        if item.cycle_candidate is not None:
            integer_rotation = item
            if item.exact_cycle:
                exact_rotation = item

    if best_rotation is None:
        rotation_depth, cocycle = word_cocycle(word)
        best_rotation = make_word_item(word, rotation_depth, cocycle)

    nontrivial = (
        exact_rotation is not None
        and not is_trivial_one_cycle_power(
            exact_rotation.word,
            exact_rotation.cycle_candidate,
        )
    )
    return NecklaceRecord(
        representative=word,
        length=length,
        total_depth=total_depth,
        denominator=denominator,
        drift=drift,
        best_rotation=best_rotation,
        best_reduced_denominator=best_reduced_denominator,
        best_modular_residue=best_modular_residue,
        integer_rotation=integer_rotation,
        exact_rotation=exact_rotation,
        nontrivial_exact=nontrivial,
    )


def update_pair_stats(stats: PairStats, record: NecklaceRecord) -> None:
    if record.denominator > 0:
        stats.positive_denominator += 1
    if record.integer_rotation is not None:
        stats.integer_candidate_necklaces += 1
    if record.exact_rotation is not None:
        stats.exact_cycle_necklaces += 1
    if record.nontrivial_exact:
        stats.nontrivial_exact_cycle_necklaces += 1
    if record.best_reduced_denominator is not None:
        stats.min_reduced_denominator = (
            record.best_reduced_denominator
            if stats.min_reduced_denominator is None
            else min(stats.min_reduced_denominator, record.best_reduced_denominator)
        )
    if record.best_modular_residue is not None:
        stats.min_nonzero_modular_residue = (
            record.best_modular_residue
            if stats.min_nonzero_modular_residue is None
            else min(stats.min_nonzero_modular_residue, record.best_modular_residue)
        )


def enumerate_sieve(
    *,
    max_length: int,
    max_total_depth: int,
    max_carry: int | None,
    top_limit: int,
) -> dict[str, Any]:
    pair_stats: defaultdict[tuple[int, int], PairStats] = defaultdict(PairStats)
    exact_records: list[NecklaceRecord] = []
    nontrivial_exact_records: list[NecklaceRecord] = []
    closest_divisibility = SmallestKeeper(top_limit)
    closest_modular = SmallestKeeper(top_limit)
    near_resonant = SmallestKeeper(top_limit)

    totals = {
        "compositions": 0,
        "necklaces": 0,
        "imprimitive_necklaces": 0,
        "primitive_necklaces": 0,
        "positive_denominator_primitive_necklaces": 0,
        "integer_candidate_necklaces": 0,
        "exact_cycle_necklaces": 0,
        "nontrivial_exact_cycle_necklaces": 0,
    }

    for length in range(1, max_length + 1):
        for total_depth in range(length, max_total_depth + 1):
            if max_carry is not None and total_depth > length * max_carry:
                continue
            key = (length, total_depth)
            stats = pair_stats[key]
            for word in bounded_compositions(total_depth, length, max_carry):
                stats.compositions += 1
                totals["compositions"] += 1
                if word != canonical_rotation(word):
                    continue
                stats.necklaces += 1
                totals["necklaces"] += 1
                if primitive_period(word) != length:
                    stats.imprimitive_necklaces += 1
                    totals["imprimitive_necklaces"] += 1
                    continue
                stats.primitive_necklaces += 1
                totals["primitive_necklaces"] += 1

                record = analyze_necklace(word)
                update_pair_stats(stats, record)

                if record.denominator > 0:
                    totals["positive_denominator_primitive_necklaces"] += 1
                    near_resonant.push(record.drift, record)
                if record.integer_rotation is not None:
                    totals["integer_candidate_necklaces"] += 1
                if record.exact_rotation is not None:
                    totals["exact_cycle_necklaces"] += 1
                    exact_records.append(record)
                if record.nontrivial_exact:
                    totals["nontrivial_exact_cycle_necklaces"] += 1
                    nontrivial_exact_records.append(record)
                if record.best_reduced_denominator is not None:
                    closest_divisibility.push(float(record.best_reduced_denominator), record)
                if record.best_modular_residue is not None:
                    closest_modular.push(float(record.best_modular_residue), record)

    return {
        "settings": {
            "max_length": max_length,
            "max_total_depth": max_total_depth,
            "max_carry": max_carry,
            "top_limit": top_limit,
        },
        "totals": totals,
        "pair_stats": {
            key: value
            for key, value in sorted(pair_stats.items())
            if value.compositions > 0
        },
        "exact_records": sorted(
            exact_records,
            key=lambda record: (
                record.exact_rotation.cycle_candidate if record.exact_rotation else 0,
                record.length,
                record.representative,
            ),
        ),
        "nontrivial_exact_records": sorted(
            nontrivial_exact_records,
            key=lambda record: (
                record.exact_rotation.cycle_candidate if record.exact_rotation else 0,
                record.length,
                record.representative,
            ),
        ),
        "closest_divisibility": closest_divisibility.records(),
        "closest_modular": closest_modular.records(),
        "near_resonant": near_resonant.records(),
    }


def record_json(record: NecklaceRecord) -> dict[str, Any]:
    exact = record.exact_rotation
    integer = record.integer_rotation
    best = record.best_rotation
    residue, modulus = exact_domain_residue(best)
    return {
        "representative": list(record.representative),
        "length": record.length,
        "total_depth": record.total_depth,
        "denominator": record.denominator,
        "drift": record.drift,
        "best_rotation": item_json(best),
        "best_reduced_denominator": record.best_reduced_denominator,
        "best_modular_residue": record.best_modular_residue,
        "integer_rotation": item_json(integer) if integer is not None else None,
        "exact_rotation": item_json(exact) if exact is not None else None,
        "nontrivial_exact": record.nontrivial_exact,
        "best_rotation_domain_residue": residue,
        "best_rotation_domain_modulus": modulus,
    }


def pair_stats_json(stats: PairStats) -> dict[str, Any]:
    return {
        "compositions": stats.compositions,
        "necklaces": stats.necklaces,
        "imprimitive_necklaces": stats.imprimitive_necklaces,
        "primitive_necklaces": stats.primitive_necklaces,
        "positive_denominator": stats.positive_denominator,
        "integer_candidate_necklaces": stats.integer_candidate_necklaces,
        "exact_cycle_necklaces": stats.exact_cycle_necklaces,
        "nontrivial_exact_cycle_necklaces": stats.nontrivial_exact_cycle_necklaces,
        "min_reduced_denominator": stats.min_reduced_denominator,
        "min_nonzero_modular_residue": stats.min_nonzero_modular_residue,
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


def make_record_table(records: list[NecklaceRecord], *, reason: str) -> list[str]:
    if not records:
        return ["_None in this finite window._"]
    lines = [
        "| necklace | m | S | drift | selected rotation | C_w | D | reduced denom | mod residue | candidate | exact | cylinder |",
        "|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for record in records:
        if reason == "exact" and record.exact_rotation is not None:
            item = record.exact_rotation
        elif reason == "integer" and record.integer_rotation is not None:
            item = record.integer_rotation
        else:
            item = record.best_rotation
        residue, modulus = exact_domain_residue(item)
        candidate = item.cycle_candidate if item.cycle_candidate is not None else "-"
        reduced = item.reduced_denominator if item.reduced_denominator is not None else "-"
        mod_residue = modular_residue(item)
        mod_text = "-" if mod_residue is None else str(mod_residue)
        lines.append(
            f"| `{word_text(record.representative)}` | {record.length} | "
            f"{record.total_depth} | {record.drift:.6f} | `{word_text(item.word)}` | "
            f"{item.cocycle} | {item.denominator} | {reduced} | {mod_text} | "
            f"{candidate} | {item.exact_cycle} | `n = {residue} mod {modulus}` |"
        )
    return lines


def make_pair_summary_table(pair_stats: dict[tuple[int, int], PairStats]) -> list[str]:
    active = [
        (key, stats)
        for key, stats in pair_stats.items()
        if stats.primitive_necklaces > 0 and stats.positive_denominator > 0
    ]
    if not active:
        return ["_No positive-denominator primitive necklaces in this window._"]
    lines = [
        "| m | S | drift | primitive necklaces | integer hits | exact hits | nontrivial hits | min reduced denom | min mod residue |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for (length, total_depth), stats in active:
        drift = total_depth - length * LOG2_3
        min_reduced = "-" if stats.min_reduced_denominator is None else str(stats.min_reduced_denominator)
        min_residue = "-" if stats.min_nonzero_modular_residue is None else str(stats.min_nonzero_modular_residue)
        lines.append(
            f"| {length} | {total_depth} | {drift:.6f} | "
            f"{stats.primitive_necklaces} | {stats.integer_candidate_necklaces} | "
            f"{stats.exact_cycle_necklaces} | {stats.nontrivial_exact_cycle_necklaces} | "
            f"{min_reduced} | {min_residue} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    totals = payload["totals"]
    max_carry = settings["max_carry"]
    carry_text = "unbounded by part size" if max_carry is None else f"1..{max_carry}"
    lines = [
        "# Collatz Primitive Cycle Sieve",
        "",
        "## Status",
        "",
        "This report works directly against the cycle equation on primitive carry necklaces.  A necklace is one cyclic rotation class of carry words; primitive necklaces exclude powers of shorter words.",
        "",
        f"- max word length: `{settings['max_length']}`",
        f"- max total carry depth: `{settings['max_total_depth']}`",
        f"- carry part bound: `{carry_text}`",
        f"- compositions tested: `{totals['compositions']}`",
        f"- necklaces seen: `{totals['necklaces']}`",
        f"- primitive necklaces tested: `{totals['primitive_necklaces']}`",
        f"- positive-denominator primitive necklaces: `{totals['positive_denominator_primitive_necklaces']}`",
        f"- integer candidate necklaces: `{totals['integer_candidate_necklaces']}`",
        f"- exact cycle necklaces: `{totals['exact_cycle_necklaces']}`",
        f"- nontrivial exact cycle necklaces: `{totals['nontrivial_exact_cycle_necklaces']}`",
        "",
        "## Cycle Equation",
        "",
        "For a primitive carry necklace with length `m` and total carry depth `S`, every rotation is tested against",
        "",
        "```text",
        "n = C_w / (2^S - 3^m)",
        "```",
        "",
        "A positive cycle requires `S > m log2(3)` and divisibility `C_w == 0 mod (2^S - 3^m)` for one rotation, followed by exact carry simulation.",
        "",
        "## Pair Summary",
        "",
        *make_pair_summary_table(payload["pair_stats"]),
        "",
        "## Exact Cycle Necklaces",
        "",
        *make_record_table(payload["exact_records"], reason="exact"),
        "",
        "## Nontrivial Exact Cycle Necklaces",
        "",
        *make_record_table(payload["nontrivial_exact_records"], reason="exact"),
        "",
        "## Closest Divisibility Misses",
        "",
        *make_record_table(payload["closest_divisibility"], reason="best"),
        "",
        "## Closest Modular Misses",
        "",
        *make_record_table(payload["closest_modular"], reason="best"),
        "",
        "## Near-Resonant Necklaces",
        "",
        *make_record_table(payload["near_resonant"], reason="best"),
        "",
        "## Interpretation",
        "",
        "This is the finite cycle sieve suggested by the carry-word algebra.  The proof-facing target is now crisp: show that every primitive necklace other than `(2)` fails the divisibility condition or fails the exact carry simulation.  This report verifies that statement only inside the bounded `(m,S)` window.",
        "",
        "The escape-facing target remains separate: control the height cocycle `S - m log2(3)` along infinite admissible carry words.  The cycle sieve is not an escape proof; it is the exact algebraic filter for periodic obstructions.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_cycle_sieve.py --max-length {settings['max_length']} --max-total-depth {settings['max_total_depth']}"
        + ("" if max_carry is None else f" --max-carry {max_carry}"),
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, max_total_depth: int, max_carry: int | None) -> Path:
    suffix = "unbounded" if max_carry is None else f"K{max_carry}"
    return Path("empirical/reports") / (
        f"collatz_cycle_sieve_L{max_length}_S{max_total_depth}_{suffix}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int | None) -> Path:
    suffix = "unbounded" if max_carry is None else f"K{max_carry}"
    return Path("empirical/reports") / (
        f"collatz_cycle_sieve_L{max_length}_S{max_total_depth}_{suffix}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=12)
    parser.add_argument("--max-total-depth", type=int, default=22)
    parser.add_argument("--max-carry", type=int, default=0)
    parser.add_argument("--top-limit", type=int, default=16)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_total_depth < args.max_length:
        raise ValueError("--max-total-depth must be at least --max-length")
    if args.max_carry < 0:
        raise ValueError("--max-carry must be nonnegative; use 0 for no part bound")

    max_carry = args.max_carry or None
    payload = enumerate_sieve(
        max_length=args.max_length,
        max_total_depth=args.max_total_depth,
        max_carry=max_carry,
        top_limit=args.top_limit,
    )

    report_path = args.report or default_report_path(
        args.max_length,
        args.max_total_depth,
        max_carry,
    )
    json_path = args.json or default_json_path(
        args.max_length,
        args.max_total_depth,
        max_carry,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(make_report(payload), encoding="utf-8")

    json_payload = {
        "settings": payload["settings"],
        "totals": payload["totals"],
        "pair_stats": {
            f"{length},{total_depth}": pair_stats_json(stats)
            for (length, total_depth), stats in payload["pair_stats"].items()
        },
        "exact_records": [record_json(record) for record in payload["exact_records"]],
        "nontrivial_exact_records": [
            record_json(record) for record in payload["nontrivial_exact_records"]
        ],
        "closest_divisibility": [
            record_json(record) for record in payload["closest_divisibility"]
        ],
        "closest_modular": [
            record_json(record) for record in payload["closest_modular"]
        ],
        "near_resonant": [
            record_json(record) for record in payload["near_resonant"]
        ],
    }
    json_path.write_text(json.dumps(rounded(json_payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["totals"]), indent=2))


if __name__ == "__main__":
    main()
