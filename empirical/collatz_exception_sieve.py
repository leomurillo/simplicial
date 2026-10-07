"""Finite exception sieve for domain-constrained Collatz carry words.

For a carry word w of length m and total carry depth S, the accelerated odd
Collatz branch is

    U_w(n) = (3^m n + C_w) / 2^S.

If 2^S <= 3^m, the word is expanding in its linear part.  If 2^S > 3^m,
then the word is eventually decreasing on its exact domain cylinder

    n = r_w mod 2^(S+1).

The exact nondecrease exceptions are finite and satisfy

    r_w + t 2^(S+1) <= floor(C_w / (2^S - 3^m)).

Equivalently, the first representative is already decreasing when

    r_w (2^S - 3^m) - C_w > 0.

This script enumerates a bounded carry-word window and classifies every word
as expanding, contracting-all-decrease, trivial-cycle exception, certified
descent exception, verified-trivial-basin exception, or unknown exception.
It is a finite proof-facing sieve, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


LOG2_3 = math.log2(3.0)


def vp2(n: int) -> int:
    if n <= 0:
        raise ValueError("vp2 expects a positive integer")
    return (n & -n).bit_length() - 1


def accelerated_odd_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("accelerated odd step requires a positive odd integer")
    raised = 3 * n + 1
    depth = vp2(raised)
    return raised >> depth, depth


def log2_int(value: int) -> float:
    if value <= 0:
        return float("-inf")
    return math.log2(value)


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period != 0:
            continue
        root = word[:period]
        if root * (len(word) // period) == word:
            return period
    return len(word)


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
    runs = word_runs(word)
    parts = [
        str(carry) if count == 1 else f"{carry}^{count}"
        for carry, count in runs
    ]
    if len(parts) <= limit:
        return "(" + " ".join(parts) + ")"
    head = " ".join(parts[: limit // 2])
    tail = " ".join(parts[-(limit // 2) :])
    return f"({head} ... {tail})"


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


def cocycle_for_word(word: tuple[int, ...]) -> int:
    total_depth = 0
    cocycle = 0
    for carry in word:
        cocycle = 3 * cocycle + (1 << total_depth)
        total_depth += carry
    return cocycle


def classify_exception_orbit(
    n0: int,
    image: int,
    word: tuple[int, ...],
    max_tail_steps: int,
) -> tuple[str, int, int]:
    """Classify one finite nondecrease representative after applying w."""

    if n0 == 1 and image == 1 and all(carry == 2 for carry in word):
        return "trivial-cycle", 0, 1

    n = image
    max_seen = max(n0, image)
    for step in range(max_tail_steps + 1):
        if n == 1:
            return "trivial-basin", step, max_seen
        if n < n0:
            return "descent", step, max_seen
        n, _carry = accelerated_odd_step(n)
        max_seen = max(max_seen, n)
    return "unknown", max_tail_steps, max_seen


@dataclass(frozen=True)
class WordClassification:
    word: tuple[int, ...]
    length: int
    total_depth: int
    primitive: bool
    period: int
    category: str
    height: float
    cocycle: int
    denominator: int
    residue: int | None
    modulus: int | None
    first_n: int | None
    cap: int | None
    margin: int | None
    exception_count: int | str
    exception_status: str | None
    certified_exception_count: int
    unknown_exception_count: int
    first_exception_image: int | None
    max_exception_image: int | None
    max_tail_value: int | None
    max_tail_steps_used: int | None


def classify_word(
    word: tuple[int, ...],
    length: int,
    total_depth: int,
    cocycle: int,
    three_power: int,
    denominator_power: int,
    denominator: int,
    inverse: int | None,
    max_exception_reps: int,
    max_tail_steps: int,
) -> WordClassification:
    period = primitive_period(word)
    primitive = period == length
    height = total_depth - length * LOG2_3

    if denominator <= 0:
        return WordClassification(
            word=word,
            length=length,
            total_depth=total_depth,
            primitive=primitive,
            period=period,
            category="expanding",
            height=height,
            cocycle=cocycle,
            denominator=denominator,
            residue=None,
            modulus=None,
            first_n=None,
            cap=None,
            margin=None,
            exception_count="infinite",
            exception_status=None,
            certified_exception_count=0,
            unknown_exception_count=0,
            first_exception_image=None,
            max_exception_image=None,
            max_tail_value=None,
            max_tail_steps_used=None,
        )

    modulus = denominator_power << 1
    if inverse is None:
        raise ValueError("contracting word requires an inverse modulo 2^(S+1)")
    residue = ((denominator_power - cocycle) * inverse) % modulus
    first_n = residue if residue > 0 else modulus
    cap = cocycle // denominator
    margin = first_n * denominator - cocycle

    if first_n > cap:
        return WordClassification(
            word=word,
            length=length,
            total_depth=total_depth,
            primitive=primitive,
            period=period,
            category="contracting-all-decrease",
            height=height,
            cocycle=cocycle,
            denominator=denominator,
            residue=residue,
            modulus=modulus,
            first_n=first_n,
            cap=cap,
            margin=margin,
            exception_count=0,
            exception_status=None,
            certified_exception_count=0,
            unknown_exception_count=0,
            first_exception_image=None,
            max_exception_image=None,
            max_tail_value=None,
            max_tail_steps_used=None,
        )

    exception_count = ((cap - first_n) // modulus) + 1
    if exception_count > max_exception_reps:
        return WordClassification(
            word=word,
            length=length,
            total_depth=total_depth,
            primitive=primitive,
            period=period,
            category="unknown-exception",
            height=height,
            cocycle=cocycle,
            denominator=denominator,
            residue=residue,
            modulus=modulus,
            first_n=first_n,
            cap=cap,
            margin=margin,
            exception_count=exception_count,
            exception_status="too-many-representatives",
            certified_exception_count=0,
            unknown_exception_count=exception_count,
            first_exception_image=None,
            max_exception_image=None,
            max_tail_value=None,
            max_tail_steps_used=None,
        )

    statuses: list[str] = []
    first_image: int | None = None
    max_image: int | None = None
    max_tail_value: int | None = None
    max_steps_used = 0
    unknown_count = 0
    certified_count = 0
    for index in range(exception_count):
        n0 = first_n + index * modulus
        image_num = three_power * n0 + cocycle
        if image_num % denominator_power != 0:
            raise AssertionError("domain residue failed exact divisibility")
        image = image_num // denominator_power
        first_image = image if first_image is None else first_image
        max_image = image if max_image is None else max(max_image, image)
        status, steps_used, tail_value = classify_exception_orbit(
            n0,
            image,
            word,
            max_tail_steps,
        )
        statuses.append(status)
        max_steps_used = max(max_steps_used, steps_used)
        max_tail_value = tail_value if max_tail_value is None else max(max_tail_value, tail_value)
        if status == "unknown":
            unknown_count += 1
        else:
            certified_count += 1

    status_set = set(statuses)
    if status_set == {"trivial-cycle"}:
        category = "trivial-cycle-exception"
        status_summary = "trivial-cycle"
    elif "unknown" in status_set:
        category = "unknown-exception"
        status_summary = ",".join(sorted(status_set))
    elif status_set <= {"trivial-basin", "trivial-cycle"}:
        category = "trivial-basin-exception"
        status_summary = ",".join(sorted(status_set))
    else:
        category = "descent-certified-exception"
        status_summary = ",".join(sorted(status_set))

    return WordClassification(
        word=word,
        length=length,
        total_depth=total_depth,
        primitive=primitive,
        period=period,
        category=category,
        height=height,
        cocycle=cocycle,
        denominator=denominator,
        residue=residue,
        modulus=modulus,
        first_n=first_n,
        cap=cap,
        margin=margin,
        exception_count=exception_count,
        exception_status=status_summary,
        certified_exception_count=certified_count,
        unknown_exception_count=unknown_count,
        first_exception_image=first_image,
        max_exception_image=max_image,
        max_tail_value=max_tail_value,
        max_tail_steps_used=max_steps_used,
    )


def classification_record(item: WordClassification) -> dict[str, Any]:
    return {
        "word": list(item.word),
        "signature": word_signature(item.word),
        "length": item.length,
        "total_depth": item.total_depth,
        "height": item.height,
        "primitive": item.primitive,
        "period": item.period,
        "category": item.category,
        "intercept_log2": log2_int(item.cocycle) - item.total_depth,
        "first_n_log2": log2_int(item.first_n or 0),
        "cap_log2": log2_int(item.cap or 0),
        "margin_log2": log2_int(abs(item.margin or 0)),
        "margin_sign": 1 if (item.margin or 0) > 0 else -1 if (item.margin or 0) < 0 else 0,
        "exception_count": item.exception_count,
        "exception_status": item.exception_status,
        "certified_exception_count": item.certified_exception_count,
        "unknown_exception_count": item.unknown_exception_count,
        "first_exception_image_log2": log2_int(item.first_exception_image or 0),
        "max_exception_image_log2": log2_int(item.max_exception_image or 0),
        "max_tail_value_log2": log2_int(item.max_tail_value or 0),
        "max_tail_steps_used": item.max_tail_steps_used,
    }


class RecordKeeper:
    def __init__(self, limit: int, lower_is_better: bool = False) -> None:
        self.limit = limit
        self.lower_is_better = lower_is_better
        self.serial = 0
        self.heap: list[tuple[float, int, WordClassification]] = []

    def push(self, score: float, item: WordClassification) -> None:
        if self.limit <= 0:
            return
        rank = -score if self.lower_is_better else score
        entry = (rank, self.serial, item)
        self.serial += 1
        if len(self.heap) < self.limit:
            heapq.heappush(self.heap, entry)
            return
        if rank > self.heap[0][0]:
            heapq.heapreplace(self.heap, entry)

    def records(self) -> list[dict[str, Any]]:
        rows = sorted(self.heap, key=lambda entry: entry[0], reverse=True)
        return [
            {
                "score": -rank if self.lower_is_better else rank,
                "classification": classification_record(item),
            }
            for rank, _serial, item in rows
        ]


@dataclass
class SieveStats:
    words: int = 0
    primitive_words: int = 0
    categories: dict[str, int] = field(default_factory=dict)
    primitive_categories: dict[str, int] = field(default_factory=dict)
    finite_exception_representatives: int = 0
    primitive_finite_exception_representatives: int = 0
    unknown_exception_representatives: int = 0
    primitive_unknown_exception_representatives: int = 0

    def update(self, item: WordClassification) -> None:
        self.words += 1
        self.categories[item.category] = self.categories.get(item.category, 0) + 1
        if isinstance(item.exception_count, int):
            if item.exception_count > 0:
                self.finite_exception_representatives += item.exception_count
        self.unknown_exception_representatives += item.unknown_exception_count
        if item.primitive:
            self.primitive_words += 1
            self.primitive_categories[item.category] = (
                self.primitive_categories.get(item.category, 0) + 1
            )
            if isinstance(item.exception_count, int):
                if item.exception_count > 0:
                    self.primitive_finite_exception_representatives += item.exception_count
            self.primitive_unknown_exception_representatives += item.unknown_exception_count

    def as_json(self) -> dict[str, Any]:
        return {
            "words": self.words,
            "primitive_words": self.primitive_words,
            "categories": dict(sorted(self.categories.items())),
            "primitive_categories": dict(sorted(self.primitive_categories.items())),
            "finite_exception_representatives": self.finite_exception_representatives,
            "primitive_finite_exception_representatives": (
                self.primitive_finite_exception_representatives
            ),
            "unknown_exception_representatives": self.unknown_exception_representatives,
            "primitive_unknown_exception_representatives": (
                self.primitive_unknown_exception_representatives
            ),
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


def enumerate_sieve(
    max_length: int,
    max_total_depth: int,
    max_carry: int | None,
    top_limit: int,
    max_exception_reps: int,
    max_tail_steps: int,
) -> dict[str, Any]:
    totals = SieveStats()
    pair_stats: dict[tuple[int, int], SieveStats] = {}
    records = {
        "unknown_exceptions": RecordKeeper(top_limit),
        "largest_exception_count": RecordKeeper(top_limit),
        "closest_all_decrease_margin": RecordKeeper(top_limit, lower_is_better=True),
        "largest_contracting_cap": RecordKeeper(top_limit),
        "largest_tail_value": RecordKeeper(top_limit),
        "primitive_unknown_exceptions": RecordKeeper(top_limit),
    }

    for length in range(1, max_length + 1):
        three_power = 3**length
        for total_depth in range(length, max_total_depth + 1):
            denominator_power = 1 << total_depth
            denominator = denominator_power - three_power
            modulus = denominator_power << 1
            inverse = pow(three_power, -1, modulus) if denominator > 0 else None
            pair = (length, total_depth)
            pair_stat = pair_stats.setdefault(pair, SieveStats())
            for word in bounded_compositions(total_depth, length, max_carry):
                cocycle = cocycle_for_word(word)
                item = classify_word(
                    word=word,
                    length=length,
                    total_depth=total_depth,
                    cocycle=cocycle,
                    three_power=three_power,
                    denominator_power=denominator_power,
                    denominator=denominator,
                    inverse=inverse,
                    max_exception_reps=max_exception_reps,
                    max_tail_steps=max_tail_steps,
                )
                totals.update(item)
                pair_stat.update(item)

                if item.category == "unknown-exception":
                    records["unknown_exceptions"].push(
                        float(item.unknown_exception_count),
                        item,
                    )
                    if item.primitive:
                        records["primitive_unknown_exceptions"].push(
                            float(item.unknown_exception_count),
                            item,
                        )
                if isinstance(item.exception_count, int) and item.exception_count > 0:
                    records["largest_exception_count"].push(
                        float(item.exception_count),
                        item,
                    )
                if item.category == "contracting-all-decrease" and item.margin:
                    records["closest_all_decrease_margin"].push(
                        log2_int(item.margin),
                        item,
                    )
                if item.denominator > 0 and item.cap is not None:
                    records["largest_contracting_cap"].push(log2_int(item.cap), item)
                if item.max_tail_value is not None:
                    records["largest_tail_value"].push(log2_int(item.max_tail_value), item)

    return {
        "settings": {
            "max_length": max_length,
            "max_total_depth": max_total_depth,
            "max_carry": max_carry,
            "top_limit": top_limit,
            "max_exception_reps": max_exception_reps,
            "max_tail_steps": max_tail_steps,
        },
        "totals": totals.as_json(),
        "pair_stats": {
            f"{length},{total_depth}": stats.as_json()
            for (length, total_depth), stats in sorted(pair_stats.items())
            if stats.words
        },
        "records": {
            name: keeper.records()
            for name, keeper in records.items()
        },
    }


def category_count(stats: dict[str, Any], category: str) -> int:
    return int(stats["categories"].get(category, 0))


def primitive_category_count(stats: dict[str, Any], category: str) -> int:
    return int(stats["primitive_categories"].get(category, 0))


def make_totals_table(totals: dict[str, Any]) -> list[str]:
    categories = [
        "expanding",
        "contracting-all-decrease",
        "trivial-cycle-exception",
        "trivial-basin-exception",
        "descent-certified-exception",
        "unknown-exception",
    ]
    lines = [
        "| category | all words | primitive words |",
        "|---|---:|---:|",
    ]
    for category in categories:
        lines.append(
            f"| {category} | {category_count(totals, category)} | "
            f"{primitive_category_count(totals, category)} |"
        )
    return lines


def make_record_table(records: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| score | category | m | S | H | primitive | exceptions | status | log2 cap | log2 n0 | word |",
        "|---:|---|---:|---:|---:|---|---:|---|---:|---:|---|",
    ]
    if not records:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - |")
        return lines
    for record in records:
        item = record["classification"]
        exceptions = item["exception_count"]
        lines.append(
            f"| {float(record['score']):.6f} | {item['category']} | "
            f"{item['length']} | {item['total_depth']} | {item['height']:.6f} | "
            f"{item['primitive']} | {exceptions} | {item['exception_status']} | "
            f"{item['cap_log2']:.6f} | {item['first_n_log2']:.6f} | "
            f"`{item['signature']}` |"
        )
    return lines


def top_pair_rows(pair_stats: dict[str, Any], limit: int = 20) -> list[tuple[str, dict[str, Any]]]:
    rows = sorted(
        pair_stats.items(),
        key=lambda item: (
            item[1]["unknown_exception_representatives"],
            item[1]["finite_exception_representatives"],
            item[1]["words"],
        ),
        reverse=True,
    )
    return rows[:limit]


def make_pair_table(pair_stats: dict[str, Any]) -> list[str]:
    lines = [
        "| m,S | words | all-decrease | finite-exception reps | unknown reps | primitive unknown reps |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for key, stats in top_pair_rows(pair_stats):
        lines.append(
            f"| {key} | {stats['words']} | "
            f"{stats['categories'].get('contracting-all-decrease', 0)} | "
            f"{stats['finite_exception_representatives']} | "
            f"{stats['unknown_exception_representatives']} | "
            f"{stats['primitive_unknown_exception_representatives']} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    totals = payload["totals"]
    suffix = "unbounded" if settings["max_carry"] is None else str(settings["max_carry"])
    lines = [
        "# Collatz Contracting Exception Sieve",
        "",
        "## Status",
        "",
        "This report enumerates bounded carry words and classifies the exact finite nondecrease exceptions in each contracting domain cylinder.",
        "",
        f"- max length: `{settings['max_length']}`",
        f"- max total carry depth: `{settings['max_total_depth']}`",
        f"- max carry per step: `{suffix}`",
        f"- max exception representatives certified per word: `{settings['max_exception_reps']}`",
        f"- max tail steps per representative: `{settings['max_tail_steps']}`",
        "",
        "## Decision Rule",
        "",
        "For `2^S > 3^m`, the whole cylinder is decreasing after the word when",
        "",
        "```text",
        "r_w (2^S - 3^m) - C_w > 0.",
        "```",
        "",
        "If the margin is nonpositive, the sieve lists the finite representatives and tries to certify each one by hitting the `1` cycle or descending below its starting value.",
        "",
        "## Totals",
        "",
        *make_totals_table(totals),
        "",
        f"- total words: `{totals['words']}`",
        f"- primitive words: `{totals['primitive_words']}`",
        f"- finite exception representatives: `{totals['finite_exception_representatives']}`",
        f"- unknown exception representatives: `{totals['unknown_exception_representatives']}`",
        f"- primitive unknown exception representatives: `{totals['primitive_unknown_exception_representatives']}`",
        "",
        "## Pair Hotspots",
        "",
        *make_pair_table(payload["pair_stats"]),
        "",
        "## Unknown Exceptions",
        "",
        *make_record_table(payload["records"]["unknown_exceptions"]),
        "",
        "## Primitive Unknown Exceptions",
        "",
        *make_record_table(payload["records"]["primitive_unknown_exceptions"]),
        "",
        "## Largest Exception Counts",
        "",
        *make_record_table(payload["records"]["largest_exception_count"]),
        "",
        "## Closest All-Decrease Margins",
        "",
        "Small score means the first admissible representative barely clears the nondecrease cap.",
        "",
        *make_record_table(payload["records"]["closest_all_decrease_margin"]),
        "",
        "## Largest Contracting Caps",
        "",
        *make_record_table(payload["records"]["largest_contracting_cap"]),
        "",
        "## Largest Certified Tail Values",
        "",
        *make_record_table(payload["records"]["largest_tail_value"]),
        "",
        "## Interpretation",
        "",
        "This is the proof-shaped blindspot audit.  The average contraction and the intercept tail are no longer separate summaries: every contracting word is forced through its exact residue cylinder, and every surviving exception representative is either certified by descent, certified into the trivial basin, or left in the unknown bucket.",
        "",
        "An empty primitive-unknown bucket in a bounded window does not prove Collatz.  It does, however, identify the algebra that a proof must control: the integer margin `r_w(2^S-3^m)-C_w` plus a descent certificate for the finite representatives when that margin is nonpositive.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_exception_sieve.py --max-length {settings['max_length']} --max-total-depth {settings['max_total_depth']}"
        + ("" if settings["max_carry"] is None else f" --max-carry {settings['max_carry']}")
        + f" --max-exception-reps {settings['max_exception_reps']} --max-tail-steps {settings['max_tail_steps']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, max_total_depth: int, max_carry: int | None) -> Path:
    suffix = "unbounded" if max_carry is None else f"K{max_carry}"
    return Path("empirical/reports") / (
        f"collatz_exception_sieve_L{max_length}_S{max_total_depth}_{suffix}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int | None) -> Path:
    suffix = "unbounded" if max_carry is None else f"K{max_carry}"
    return Path("empirical/reports") / (
        f"collatz_exception_sieve_L{max_length}_S{max_total_depth}_{suffix}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=12)
    parser.add_argument("--max-total-depth", type=int, default=22)
    parser.add_argument("--max-carry", type=int, default=0)
    parser.add_argument("--top-limit", type=int, default=12)
    parser.add_argument("--max-exception-reps", type=int, default=128)
    parser.add_argument("--max-tail-steps", type=int, default=10000)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_total_depth < args.max_length:
        raise ValueError("--max-total-depth must be at least --max-length")
    if args.max_carry < 0:
        raise ValueError("--max-carry must be nonnegative; use 0 for no bound")
    if args.max_exception_reps < 1:
        raise ValueError("--max-exception-reps must be at least 1")
    if args.max_tail_steps < 0:
        raise ValueError("--max-tail-steps must be nonnegative")

    max_carry = args.max_carry or None
    payload = enumerate_sieve(
        max_length=args.max_length,
        max_total_depth=args.max_total_depth,
        max_carry=max_carry,
        top_limit=args.top_limit,
        max_exception_reps=args.max_exception_reps,
        max_tail_steps=args.max_tail_steps,
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
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["totals"]), indent=2))


if __name__ == "__main__":
    main()
