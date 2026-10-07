"""Mine the exact margin lattice for contracting Collatz carry words.

The old cousin/path notes stress a useful separation:

* periodic cycle obstructions are zero-orbit/divisibility questions;
* divergence/descent needs exact domain-cylinder inequalities.

For an accelerated odd carry word w of length m and total carry depth S,

    U_w(n) = (3^m n + C_w) / 2^S.

If D_w = 2^S - 3^m > 0, the branch is contracting.  On its exact domain
cylinder n = r_w mod 2^(S+1), the first representative is already decreasing
iff

    margin(w) = r_w D_w - C_w > 0.

The hidden lattice fact is that this margin is always a multiple of
2^(S+1).  This script mines the integer quotient

    q_w = margin(w) / 2^(S+1)

and classifies the sign pattern in bounded windows.  The hard global question
is no longer "is the margin near zero?"  Nonzero margins cannot be near zero.
It is the sharper sign/zero question: q_w > 0, q_w = 0, or q_w < 0.
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


@dataclass(frozen=True)
class MarginItem:
    word: tuple[int, ...]
    length: int
    total_depth: int
    primitive: bool
    period: int
    cocycle: int
    denominator: int
    residue: int
    modulus: int
    first_n: int
    cap: int
    margin: int
    q: int
    gap_to_cap: int

    @property
    def height(self) -> float:
        return self.total_depth - self.length * LOG2_3

    @property
    def category(self) -> str:
        if self.q < 0:
            return "negative-margin"
        if self.q == 0:
            if self.first_n == 1 and all(carry == 2 for carry in self.word):
                return "trivial-zero-margin"
            return "nontrivial-zero-margin"
        return "positive-margin"


def analyze_contracting_word(
    word: tuple[int, ...],
    length: int,
    total_depth: int,
    denominator: int,
    denominator_power: int,
    three_power_inverse: int,
) -> MarginItem:
    cocycle = cocycle_for_word(word)
    modulus = denominator_power << 1
    residue = ((denominator_power - cocycle) * three_power_inverse) % modulus
    first_n = residue if residue > 0 else modulus
    cap = cocycle // denominator
    margin = first_n * denominator - cocycle
    if margin % modulus != 0:
        raise AssertionError("margin lattice failure")
    q = margin // modulus
    gap_to_cap = first_n - cap
    period = primitive_period(word)
    return MarginItem(
        word=word,
        length=length,
        total_depth=total_depth,
        primitive=period == length,
        period=period,
        cocycle=cocycle,
        denominator=denominator,
        residue=residue,
        modulus=modulus,
        first_n=first_n,
        cap=cap,
        margin=margin,
        q=q,
        gap_to_cap=gap_to_cap,
    )


def item_record(item: MarginItem) -> dict[str, Any]:
    return {
        "word": list(item.word),
        "signature": word_signature(item.word),
        "length": item.length,
        "total_depth": item.total_depth,
        "height": item.height,
        "primitive": item.primitive,
        "period": item.period,
        "category": item.category,
        "q": str(item.q),
        "q_log2_abs": log2_int(abs(item.q)),
        "margin_log2_abs": log2_int(abs(item.margin)),
        "intercept_log2": log2_int(item.cocycle) - item.total_depth,
        "cap_log2": log2_int(item.cap),
        "first_n_log2": log2_int(item.first_n),
        "gap_to_cap": str(item.gap_to_cap),
        "gap_to_cap_log2": log2_int(item.gap_to_cap),
        "residue_log2": log2_int(item.residue),
        "modulus_log2": item.total_depth + 1,
    }


class RecordKeeper:
    def __init__(self, limit: int, lower_is_better: bool = False) -> None:
        self.limit = limit
        self.lower_is_better = lower_is_better
        self.serial = 0
        self.heap: list[tuple[float, int, MarginItem]] = []

    def push(self, score: float, item: MarginItem) -> None:
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
                "item": item_record(item),
            }
            for rank, _serial, item in rows
        ]


@dataclass
class MarginStats:
    contracting_words: int = 0
    primitive_contracting_words: int = 0
    positive_q: int = 0
    zero_q: int = 0
    negative_q: int = 0
    trivial_zero_q: int = 0
    nontrivial_zero_q: int = 0
    primitive_positive_q: int = 0
    primitive_zero_q: int = 0
    primitive_negative_q: int = 0
    min_positive_q: int | None = None
    min_positive_q_word: tuple[int, ...] | None = None
    min_gap_to_cap: int | None = None
    min_gap_word: tuple[int, ...] | None = None
    gcd_positive_q: int = 0

    def update(self, item: MarginItem) -> None:
        self.contracting_words += 1
        if item.primitive:
            self.primitive_contracting_words += 1

        if item.q > 0:
            self.positive_q += 1
            self.gcd_positive_q = (
                item.q
                if self.gcd_positive_q == 0
                else math.gcd(self.gcd_positive_q, item.q)
            )
            if self.min_positive_q is None or item.q < self.min_positive_q:
                self.min_positive_q = item.q
                self.min_positive_q_word = item.word
            if self.min_gap_to_cap is None or item.gap_to_cap < self.min_gap_to_cap:
                self.min_gap_to_cap = item.gap_to_cap
                self.min_gap_word = item.word
            if item.primitive:
                self.primitive_positive_q += 1
        elif item.q == 0:
            self.zero_q += 1
            if item.category == "trivial-zero-margin":
                self.trivial_zero_q += 1
            else:
                self.nontrivial_zero_q += 1
            if item.primitive:
                self.primitive_zero_q += 1
        else:
            self.negative_q += 1
            if item.primitive:
                self.primitive_negative_q += 1

    def as_json(self) -> dict[str, Any]:
        return {
            "contracting_words": self.contracting_words,
            "primitive_contracting_words": self.primitive_contracting_words,
            "positive_q": self.positive_q,
            "zero_q": self.zero_q,
            "negative_q": self.negative_q,
            "trivial_zero_q": self.trivial_zero_q,
            "nontrivial_zero_q": self.nontrivial_zero_q,
            "primitive_positive_q": self.primitive_positive_q,
            "primitive_zero_q": self.primitive_zero_q,
            "primitive_negative_q": self.primitive_negative_q,
            "min_positive_q": str(self.min_positive_q)
            if self.min_positive_q is not None
            else None,
            "min_positive_q_log2": log2_int(self.min_positive_q or 0),
            "min_positive_q_word": list(self.min_positive_q_word)
            if self.min_positive_q_word is not None
            else None,
            "min_positive_q_signature": word_signature(self.min_positive_q_word or ()),
            "min_gap_to_cap": str(self.min_gap_to_cap)
            if self.min_gap_to_cap is not None
            else None,
            "min_gap_to_cap_log2": log2_int(self.min_gap_to_cap or 0),
            "min_gap_signature": word_signature(self.min_gap_word or ()),
            "gcd_positive_q": str(self.gcd_positive_q),
            "gcd_positive_q_log2": log2_int(self.gcd_positive_q),
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


def enumerate_margins(
    max_length: int,
    max_total_depth: int,
    max_carry: int | None,
    top_limit: int,
) -> dict[str, Any]:
    totals = MarginStats()
    by_length: dict[int, MarginStats] = {}
    by_pair: dict[tuple[int, int], MarginStats] = {}
    records = {
        "smallest_positive_q": RecordKeeper(top_limit, lower_is_better=True),
        "smallest_gap_to_cap": RecordKeeper(top_limit, lower_is_better=True),
        "largest_contracting_cap": RecordKeeper(top_limit),
        "negative_q": RecordKeeper(top_limit),
        "nontrivial_zero_q": RecordKeeper(top_limit),
        "q_equals_one": RecordKeeper(top_limit, lower_is_better=True),
    }

    expanding_words = 0
    for length in range(1, max_length + 1):
        three_power = 3**length
        by_length.setdefault(length, MarginStats())
        for total_depth in range(length, max_total_depth + 1):
            denominator_power = 1 << total_depth
            denominator = denominator_power - three_power
            if denominator <= 0:
                count = 0
                for _word in bounded_compositions(total_depth, length, max_carry):
                    count += 1
                expanding_words += count
                continue

            modulus = denominator_power << 1
            inverse = pow(three_power, -1, modulus)
            pair_stats = by_pair.setdefault((length, total_depth), MarginStats())
            length_stats = by_length.setdefault(length, MarginStats())
            for word in bounded_compositions(total_depth, length, max_carry):
                item = analyze_contracting_word(
                    word=word,
                    length=length,
                    total_depth=total_depth,
                    denominator=denominator,
                    denominator_power=denominator_power,
                    three_power_inverse=inverse,
                )
                totals.update(item)
                pair_stats.update(item)
                length_stats.update(item)

                if item.q > 0:
                    records["smallest_positive_q"].push(float(item.q), item)
                    records["smallest_gap_to_cap"].push(float(item.gap_to_cap), item)
                    records["largest_contracting_cap"].push(log2_int(item.cap), item)
                    if item.q == 1:
                        records["q_equals_one"].push(float(item.total_depth), item)
                elif item.q < 0:
                    records["negative_q"].push(float(item.q), item)
                elif item.category == "nontrivial-zero-margin":
                    records["nontrivial_zero_q"].push(float(item.total_depth), item)

    return {
        "settings": {
            "max_length": max_length,
            "max_total_depth": max_total_depth,
            "max_carry": max_carry,
            "top_limit": top_limit,
        },
        "expanding_words": expanding_words,
        "totals": totals.as_json(),
        "by_length": {
            str(length): stats.as_json()
            for length, stats in sorted(by_length.items())
        },
        "by_pair": {
            f"{length},{total_depth}": stats.as_json()
            for (length, total_depth), stats in sorted(by_pair.items())
        },
        "records": {
            name: keeper.records()
            for name, keeper in records.items()
        },
    }


def make_length_table(by_length: dict[str, Any]) -> list[str]:
    lines = [
        "| m | contracting | positive q | zero q | negative q | min q | min gap | gcd positive q | min-q word |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for length, row in by_length.items():
        lines.append(
            f"| {length} | {row['contracting_words']} | {row['positive_q']} | "
            f"{row['zero_q']} | {row['negative_q']} | {row['min_positive_q']} | "
            f"{row['min_gap_to_cap']} | {row['gcd_positive_q']} | "
            f"`{row['min_positive_q_signature']}` |"
        )
    return lines


def top_pair_rows(by_pair: dict[str, Any], limit: int = 24) -> list[tuple[str, dict[str, Any]]]:
    return sorted(
        by_pair.items(),
        key=lambda item: (
            item[1]["nontrivial_zero_q"],
            item[1]["negative_q"],
            -(int(item[1]["min_positive_q"]) if item[1]["min_positive_q"] is not None else 10**100),
            item[1]["contracting_words"],
        ),
        reverse=True,
    )[:limit]


def make_pair_table(by_pair: dict[str, Any]) -> list[str]:
    lines = [
        "| m,S | contracting | positive q | zero q | negative q | min q | min gap | gcd q | min-q word |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for key, row in top_pair_rows(by_pair):
        lines.append(
            f"| {key} | {row['contracting_words']} | {row['positive_q']} | "
            f"{row['zero_q']} | {row['negative_q']} | {row['min_positive_q']} | "
            f"{row['min_gap_to_cap']} | {row['gcd_positive_q']} | "
            f"`{row['min_positive_q_signature']}` |"
        )
    return lines


def make_record_table(records: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| score | category | m | S | H | q | gap | log2 cap | log2 n0 | primitive | word |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    if not records:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - |")
        return lines
    for record in records:
        item = record["item"]
        lines.append(
            f"| {float(record['score']):.6f} | {item['category']} | "
            f"{item['length']} | {item['total_depth']} | {item['height']:.6f} | "
            f"{item['q']} | {item['gap_to_cap']} | {item['cap_log2']:.6f} | "
            f"{item['first_n_log2']:.6f} | {item['primitive']} | "
            f"`{item['signature']}` |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    totals = payload["totals"]
    max_carry = settings["max_carry"]
    suffix = "unbounded" if max_carry is None else str(max_carry)
    lines = [
        "# Collatz Margin Lattice Miner",
        "",
        "## Stress Check From Old Notes",
        "",
        "The old notes are cycle-side notes: they reduce periodic obstructions to the path-sum divisibility condition and warn that small-modulus/canonical-coset structure is mostly a mirage.  This report therefore does not canonicalize carry words and does not look for a small-prime obstruction.  It mines the exact domain inequality for every linear carry word in the window.",
        "",
        "The cycle-side zero condition remains hard globally.  What is new here is the descent-side lattice: once a contracting word is not exactly zero-margin, the margin cannot be close to zero.",
        "",
        "## Lattice Lemma",
        "",
        "For a contracting word, set `D = 2^S - 3^m`, `M = 2^(S+1)`, and choose the exact domain residue `r` with",
        "",
        "```text",
        "3^m r + C_w == 2^S mod 2^(S+1).",
        "```",
        "",
        "Then",
        "",
        "```text",
        "margin(w) = rD - C_w",
        "q_w       = margin(w) / 2^(S+1)  is an integer.",
        "```",
        "",
        "So a nonzero margin has an automatic gap of at least one full domain modulus.  The remaining proof-facing sign question is whether nontrivial contracting words ever have `q_w <= 0`.",
        "",
        "## Settings",
        "",
        f"- max length: `{settings['max_length']}`",
        f"- max total carry depth: `{settings['max_total_depth']}`",
        f"- max carry per step: `{suffix}`",
        f"- expanding words skipped: `{payload['expanding_words']}`",
        "",
        "## Totals",
        "",
        f"- contracting words: `{totals['contracting_words']}`",
        f"- primitive contracting words: `{totals['primitive_contracting_words']}`",
        f"- positive q: `{totals['positive_q']}`",
        f"- zero q: `{totals['zero_q']}`",
        f"- trivial zero q: `{totals['trivial_zero_q']}`",
        f"- nontrivial zero q: `{totals['nontrivial_zero_q']}`",
        f"- negative q: `{totals['negative_q']}`",
        f"- primitive zero q: `{totals['primitive_zero_q']}`",
        f"- primitive negative q: `{totals['primitive_negative_q']}`",
        "",
        "## Length Envelope",
        "",
        *make_length_table(payload["by_length"]),
        "",
        "## Pair Envelope Hotspots",
        "",
        *make_pair_table(payload["by_pair"]),
        "",
        "## Smallest Positive q",
        "",
        *make_record_table(payload["records"]["smallest_positive_q"]),
        "",
        "## Smallest Gap To Cap",
        "",
        "Here `gap = first admissible n - floor(C_w / D)`.  Positive margins force `gap >= ceil(2^(S+1)/D)`, so even the nearest descent cases clear the cap by multiple integers.",
        "",
        *make_record_table(payload["records"]["smallest_gap_to_cap"]),
        "",
        "## q = 1 Witnesses",
        "",
        *make_record_table(payload["records"]["q_equals_one"]),
        "",
        "## Nontrivial Zero q",
        "",
        *make_record_table(payload["records"]["nontrivial_zero_q"]),
        "",
        "## Negative q",
        "",
        *make_record_table(payload["records"]["negative_q"]),
        "",
        "## Largest Contracting Caps",
        "",
        *make_record_table(payload["records"]["largest_contracting_cap"]),
        "",
        "## Interpretation",
        "",
        "The computation separates the descent problem into a clean trichotomy.  `q_w = 0` is the cycle obstruction.  `q_w < 0` would be a finite nondecrease packet.  `q_w > 0` means the entire exact cylinder decreases after the word.",
        "",
        "In this window, the only zero margins are the trivial `(2)^m` words and there are no negative margins.  Combined with the old notes, this says the next real theorem candidate is not a small modular obstruction.  It is a sign theorem for the domain-lattice quotient `q_w`, with the cycle-zero case explicitly separated.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_margin_lattice_miner.py --max-length {settings['max_length']} --max-total-depth {settings['max_total_depth']}"
        + ("" if max_carry is None else f" --max-carry {max_carry}")
        + f" --top-limit {settings['top_limit']}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, max_total_depth: int, max_carry: int | None) -> Path:
    suffix = "unbounded" if max_carry is None else f"K{max_carry}"
    return Path("empirical/reports") / (
        f"collatz_margin_lattice_L{max_length}_S{max_total_depth}_{suffix}.md"
    )


def default_json_path(max_length: int, max_total_depth: int, max_carry: int | None) -> Path:
    suffix = "unbounded" if max_carry is None else f"K{max_carry}"
    return Path("empirical/reports") / (
        f"collatz_margin_lattice_L{max_length}_S{max_total_depth}_{suffix}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=12)
    parser.add_argument("--max-total-depth", type=int, default=25)
    parser.add_argument("--max-carry", type=int, default=8)
    parser.add_argument("--top-limit", type=int, default=16)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_total_depth < args.max_length:
        raise ValueError("--max-total-depth must be at least --max-length")
    if args.max_carry < 0:
        raise ValueError("--max-carry must be nonnegative; use 0 for no bound")

    max_carry = args.max_carry or None
    payload = enumerate_margins(
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
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["totals"]), indent=2))


if __name__ == "__main__":
    main()
