"""Domain-constrained transfer audit for Collatz carry corridors.

The two-cocycle pressure audit showed the blindspot: low-height carry
corridors are small in 2-adic mass, but the normalized affine intercept can
have a large tail.  This script forces that tail to pay the exact arithmetic
domain cost.

For a carry word w of length m and total carry depth S,

    U_w(n) = (3^m n + C_w) / 2^S.

The exact domain of that word is a single odd residue class

    n = r_w mod 2^(S+1),

where

    3^m r_w + C_w == 2^S mod 2^(S+1).

This audit records the first positive integer in that cylinder, its image,
the exact finite nondecrease exceptions for contracting words, and witness
corridors at long length.  It is a finite arithmetic transfer ledger, not a
proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)


def log2_int(value: int) -> float:
    if value <= 0:
        return float("-inf")
    return math.log2(value)


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


def cocycle_for_word(word: tuple[int, ...]) -> tuple[int, int]:
    total_depth = 0
    cocycle = 0
    for carry in word:
        cocycle = 3 * cocycle + (1 << total_depth)
        total_depth += carry
    return total_depth, cocycle


def exact_domain_residue(length: int, total_depth: int, cocycle: int) -> tuple[int, int]:
    modulus = 1 << (total_depth + 1)
    multiplier = pow(3, length, modulus)
    inverse = pow(multiplier, -1, modulus)
    residue = ((1 << total_depth) - cocycle) * inverse
    return residue % modulus, modulus


def domain_metrics(word: tuple[int, ...], total_depth: int, cocycle: int) -> dict[str, Any]:
    length = len(word)
    three_power = 3**length
    residue, modulus = exact_domain_residue(length, total_depth, cocycle)
    first_n = residue if residue > 0 else modulus
    numerator = three_power * first_n + cocycle
    denominator_power = 1 << total_depth
    if numerator % denominator_power != 0:
        raise AssertionError("domain residue failed divisibility check")
    image = numerator // denominator_power

    height = total_depth - length * LOG2_3
    denominator = denominator_power - three_power
    intercept_log2 = log2_int(cocycle) - total_depth
    first_n_log2 = log2_int(first_n)
    image_log2 = log2_int(image)
    gain_log2 = image_log2 - first_n_log2
    domain_charge_log2 = first_n_log2 - intercept_log2

    if denominator > 0:
        max_nondecreasing_n = cocycle // denominator
        if max_nondecreasing_n >= first_n:
            nondecreasing_count: int | str = (
                (max_nondecreasing_n - first_n) // modulus
            ) + 1
        else:
            nondecreasing_count = 0
        cap_log2: float | None = log2_int(cocycle) - log2_int(denominator)
        max_nondecreasing_log2: float | None = log2_int(max_nondecreasing_n)
        contraction_type = "contracting"
    else:
        nondecreasing_count = "infinite"
        cap_log2 = None
        max_nondecreasing_log2 = None
        contraction_type = "expanding"

    return {
        "word": list(word),
        "signature": word_signature(word),
        "length": length,
        "total_depth": total_depth,
        "height": height,
        "cocycle_log2": log2_int(cocycle),
        "intercept_log2": intercept_log2,
        "domain_residue": str(residue),
        "domain_modulus_log2": total_depth + 1,
        "first_n": str(first_n),
        "first_n_log2": first_n_log2,
        "image_first_n": str(image),
        "image_first_n_log2": image_log2,
        "gain_at_first_n_log2": gain_log2,
        "domain_charge_log2": domain_charge_log2,
        "denominator_sign": 1 if denominator > 0 else -1 if denominator < 0 else 0,
        "contraction_type": contraction_type,
        "cap_log2": cap_log2,
        "max_nondecreasing_n_log2": max_nondecreasing_log2,
        "nondecreasing_representatives": nondecreasing_count,
        "all_large_representatives_decrease": denominator > 0,
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


def record_for_metric(metrics: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "signature",
        "length",
        "total_depth",
        "height",
        "intercept_log2",
        "first_n_log2",
        "image_first_n_log2",
        "gain_at_first_n_log2",
        "domain_charge_log2",
        "cap_log2",
        "nondecreasing_representatives",
        "domain_modulus_log2",
        "word",
    ]
    return {key: metrics.get(key) for key in keys}


@dataclass
class WindowStats:
    label: str
    barrier: float
    length: int
    words: int = 0
    mass: float = 0.0
    expanding_words: int = 0
    expanding_mass: float = 0.0
    contracting_words: int = 0
    contracting_mass: float = 0.0
    all_decrease_words: int = 0
    finite_exception_words: int = 0
    finite_exception_representatives: int = 0
    records: dict[str, dict[str, Any]] = field(default_factory=dict)

    def update_record(
        self,
        name: str,
        metrics: dict[str, Any],
        score: float,
        lower_is_better: bool = False,
    ) -> None:
        old = self.records.get(name)
        if old is None:
            self.records[name] = {
                "score": score,
                "metrics": record_for_metric(metrics),
            }
            return
        old_score = float(old["score"])
        better = score < old_score if lower_is_better else score > old_score
        if better:
            self.records[name] = {
                "score": score,
                "metrics": record_for_metric(metrics),
            }

    def update(self, metrics: dict[str, Any]) -> None:
        total_depth = int(metrics["total_depth"])
        branch_mass = 2.0 ** (-total_depth)
        self.words += 1
        self.mass += branch_mass

        if metrics["contraction_type"] == "expanding":
            self.expanding_words += 1
            self.expanding_mass += branch_mass
        else:
            self.contracting_words += 1
            self.contracting_mass += branch_mass
            count = metrics["nondecreasing_representatives"]
            if isinstance(count, int) and count > 0:
                self.finite_exception_words += 1
                self.finite_exception_representatives += count
            else:
                self.all_decrease_words += 1

        self.update_record(
            "max_gain_at_first_n",
            metrics,
            float(metrics["gain_at_first_n_log2"]),
        )
        self.update_record(
            "max_intercept",
            metrics,
            float(metrics["intercept_log2"]),
        )
        self.update_record(
            "max_first_n",
            metrics,
            float(metrics["first_n_log2"]),
        )
        self.update_record(
            "min_domain_charge",
            metrics,
            float(metrics["domain_charge_log2"]),
            lower_is_better=True,
        )
        cap_log2 = metrics.get("cap_log2")
        if cap_log2 is not None:
            self.update_record("max_contracting_cap", metrics, float(cap_log2))
        count = metrics["nondecreasing_representatives"]
        if isinstance(count, int):
            self.update_record("max_finite_exceptions", metrics, float(count))

    def to_json(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "barrier": self.barrier,
            "length": self.length,
            "words": self.words,
            "mass": self.mass,
            "log2_mass": math.log2(self.mass) if self.mass > 0.0 else float("-inf"),
            "expanding_words": self.expanding_words,
            "expanding_mass": self.expanding_mass,
            "expanding_mass_fraction": self.expanding_mass / self.mass
            if self.mass > 0.0
            else 0.0,
            "contracting_words": self.contracting_words,
            "contracting_mass": self.contracting_mass,
            "all_decrease_words": self.all_decrease_words,
            "finite_exception_words": self.finite_exception_words,
            "finite_exception_representatives": self.finite_exception_representatives,
            "records": self.records,
        }


def parse_barriers(text: str) -> list[float]:
    barriers = []
    for part in text.split(","):
        stripped = part.strip()
        if stripped:
            barriers.append(float(stripped))
    if not barriers:
        raise ValueError("--barriers must contain at least one value")
    return barriers


def enumerate_final_windows(length: int, barriers: list[float]) -> list[WindowStats]:
    max_allowed = math.floor(length * LOG2_3 + max(barriers))
    allowed_by_barrier = {
        barrier: math.floor(length * LOG2_3 + barrier)
        for barrier in barriers
    }
    stats = {
        barrier: WindowStats("exact-final-window", barrier, length)
        for barrier in barriers
    }

    def visit(position: int, total_depth: int, cocycle: int, word: tuple[int, ...]) -> None:
        if position == length:
            metrics = domain_metrics(word, total_depth, cocycle)
            for barrier, allowed in allowed_by_barrier.items():
                if total_depth <= allowed:
                    stats[barrier].update(metrics)
            return

        remaining_after = length - position - 1
        max_carry = max_allowed - total_depth - remaining_after
        for carry in range(1, max_carry + 1):
            visit(
                position + 1,
                total_depth + carry,
                3 * cocycle + (1 << total_depth),
                word + (carry,),
            )

    visit(0, 0, 0, ())
    return [stats[barrier] for barrier in barriers]


def enumerate_prefix_windows(length: int, barriers: list[float]) -> list[WindowStats]:
    out = []
    for barrier in barriers:
        stats = WindowStats("exact-prefix-window", barrier, length)

        def visit(position: int, total_depth: int, cocycle: int, word: tuple[int, ...]) -> None:
            if position == length:
                stats.update(domain_metrics(word, total_depth, cocycle))
                return
            prefix_position = position + 1
            prefix_cap = math.floor(prefix_position * LOG2_3 + barrier)
            remaining_after = length - prefix_position
            final_cap = math.floor(length * LOG2_3 + barrier)
            max_carry = min(
                prefix_cap - total_depth,
                final_cap - total_depth - remaining_after,
            )
            for carry in range(1, max_carry + 1):
                visit(
                    position + 1,
                    total_depth + carry,
                    3 * cocycle + (1 << total_depth),
                    word + (carry,),
                )

        visit(0, 0, 0, ())
        out.append(stats)
    return out


def all_ones_word(length: int) -> tuple[int, ...]:
    return (1,) * length


def early_depth_word(length: int, total_depth: int) -> tuple[int, ...] | None:
    first = total_depth - (length - 1)
    if first < 1:
        return None
    return (first,) + ((1,) * (length - 1))


def greedy_prefix_word(
    length: int,
    barrier: float,
    total_depth: int,
) -> tuple[int, ...] | None:
    word: list[int] = []
    current_depth = 0
    for position in range(1, length + 1):
        remaining = length - position
        prefix_cap = math.floor(position * LOG2_3 + barrier)
        max_by_prefix = prefix_cap - current_depth
        max_by_total = total_depth - current_depth - remaining
        carry = min(max_by_prefix, max_by_total)
        if carry < 1:
            return None
        word.append(carry)
        current_depth += carry
    if current_depth != total_depth:
        return None
    return tuple(word)


def corridor_record(
    label: str,
    barrier: float,
    word: tuple[int, ...],
) -> dict[str, Any]:
    total_depth, cocycle = cocycle_for_word(word)
    metrics = domain_metrics(word, total_depth, cocycle)
    metrics["label"] = label
    metrics["barrier"] = barrier
    return metrics


def long_corridors(length: int, barriers: list[float]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    positive_depth = math.floor(length * LOG2_3) + 1
    ones = all_ones_word(length)
    for barrier in barriers:
        rows.append(corridor_record("all-ones expansion corridor", barrier, ones))
        allowed_depth = math.floor(length * LOG2_3 + barrier)
        if positive_depth <= allowed_depth:
            final_word = early_depth_word(length, positive_depth)
            if final_word is not None:
                rows.append(
                    corridor_record(
                        "final-window earliest contracting cap",
                        barrier,
                        final_word,
                    )
                )
            prefix_word = greedy_prefix_word(length, barrier, positive_depth)
            if prefix_word is not None:
                rows.append(
                    corridor_record(
                        "prefix-barrier earliest contracting cap",
                        barrier,
                        prefix_word,
                    )
                )
    return rows


def validation_rows(
    exact_length: int,
    barriers: list[float],
    final_stats: list[WindowStats],
    prefix_stats: list[WindowStats],
) -> list[dict[str, Any]]:
    positive_depth = math.floor(exact_length * LOG2_3) + 1
    rows = []
    final_by_barrier = {stats.barrier: stats for stats in final_stats}
    prefix_by_barrier = {stats.barrier: stats for stats in prefix_stats}
    for barrier in barriers:
        allowed_depth = math.floor(exact_length * LOG2_3 + barrier)
        if positive_depth > allowed_depth:
            rows.append(
                {
                    "barrier": barrier,
                    "positive_depth": positive_depth,
                    "has_contracting_window": False,
                }
            )
            continue
        predicted_final = early_depth_word(exact_length, positive_depth)
        predicted_prefix = greedy_prefix_word(exact_length, barrier, positive_depth)
        exact_final_word = (
            final_by_barrier[barrier]
            .records.get("max_contracting_cap", {})
            .get("metrics", {})
            .get("word")
        )
        exact_prefix_word = (
            prefix_by_barrier[barrier]
            .records.get("max_contracting_cap", {})
            .get("metrics", {})
            .get("word")
        )
        rows.append(
            {
                "barrier": barrier,
                "positive_depth": positive_depth,
                "has_contracting_window": True,
                "final_greedy_matches_exact": list(predicted_final or ())
                == exact_final_word,
                "prefix_greedy_matches_exact": list(predicted_prefix or ())
                == exact_prefix_word,
                "predicted_final_signature": word_signature(predicted_final or ()),
                "exact_final_signature": word_signature(tuple(exact_final_word or ())),
                "predicted_prefix_signature": word_signature(predicted_prefix or ()),
                "exact_prefix_signature": word_signature(tuple(exact_prefix_word or ())),
            }
        )
    return rows


def make_stats_table(stats_rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| barrier | words | mass | log2 mass | expanding % | contracting words | all-decrease words | finite exception reps |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in stats_rows:
        lines.append(
            f"| {row['barrier']} | {row['words']} | {row['mass']:.12g} | "
            f"{row['log2_mass']:.6f} | {100.0 * row['expanding_mass_fraction']:.4f} | "
            f"{row['contracting_words']} | {row['all_decrease_words']} | "
            f"{row['finite_exception_representatives']} |"
        )
    return lines


def make_corridor_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| barrier | corridor | S | H | log2 B | log2 n0 | log2 U(n0) | log2 gain | log2 cap | nondec reps | word |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        cap = row.get("cap_log2")
        cap_text = "-" if cap is None else f"{float(cap):.6f}"
        reps = row["nondecreasing_representatives"]
        lines.append(
            f"| {row['barrier']} | {row['label']} | {row['total_depth']} | "
            f"{row['height']:.6f} | {row['intercept_log2']:.6f} | "
            f"{row['first_n_log2']:.6f} | {row['image_first_n_log2']:.6f} | "
            f"{row['gain_at_first_n_log2']:.6f} | {cap_text} | {reps} | "
            f"`{row['signature']}` |"
        )
    return lines


def make_record_table(stats_rows: list[dict[str, Any]], record_name: str) -> list[str]:
    lines = [
        "| window | barrier | score | S | H | log2 B | log2 n0 | log2 gain | reps | word |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in stats_rows:
        record = row["records"].get(record_name)
        if record is None:
            lines.append(f"| {row['label']} | {row['barrier']} | - | - | - | - | - | - | - | - |")
            continue
        metrics = record["metrics"]
        lines.append(
            f"| {row['label']} | {row['barrier']} | {float(record['score']):.6f} | "
            f"{metrics['total_depth']} | {metrics['height']:.6f} | "
            f"{metrics['intercept_log2']:.6f} | {metrics['first_n_log2']:.6f} | "
            f"{metrics['gain_at_first_n_log2']:.6f} | "
            f"{metrics['nondecreasing_representatives']} | "
            f"`{metrics['signature']}` |"
        )
    return lines


def make_validation_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| barrier | positive S | final witness exact? | prefix witness exact? | final signatures | prefix signatures |",
        "|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        if not row.get("has_contracting_window"):
            lines.append(
                f"| {row['barrier']} | {row['positive_depth']} | no contracting S | no contracting S | - | - |"
            )
            continue
        lines.append(
            f"| {row['barrier']} | {row['positive_depth']} | "
            f"{row['final_greedy_matches_exact']} | {row['prefix_greedy_matches_exact']} | "
            f"`{row['predicted_final_signature']}` / `{row['exact_final_signature']}` | "
            f"`{row['predicted_prefix_signature']}` / `{row['exact_prefix_signature']}` |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    lines = [
        "# Collatz Domain-Constrained Transfer",
        "",
        "## Status",
        "",
        "This report couples the two-cocycle `(H(w), B_w)` to the exact carry-domain cylinder `n = r_w mod 2^(S+1)`.  The goal is to test whether rare high-intercept corridors line up with actual positive integers cheaply enough to matter.",
        "",
        f"- long corridor length: `{settings['long_length']}`",
        f"- exact validation length: `{settings['exact_length']}`",
        f"- barriers: `{settings['barriers']}`",
        f"- log2(3): `{LOG2_3:.12f}`",
        "",
        "## Exact Domain Formula",
        "",
        "```text",
        "U_w(n) = (3^m n + C_w) / 2^S",
        "3^m r_w + C_w == 2^S mod 2^(S+1)",
        "n = r_w + t 2^(S+1)",
        "```",
        "",
        "If `2^S > 3^m`, the word is contracting for all sufficiently large representatives in its cylinder.  The exact finite nondecrease exceptions are the `t` for which",
        "",
        "```text",
        "r_w + t 2^(S+1) <= floor(C_w / (2^S - 3^m)).",
        "```",
        "",
        "## Long Witness Corridors",
        "",
        *make_corridor_table(payload["long_corridors"]),
        "",
        "The all-ones corridor creates the largest visible intercept tail, but its first admissible positive integer is also enormous because the exact cylinder is `-1 mod 2^(m+1)`.  The contracting-cap corridors sit just past the height boundary; they are the finite words where additive lift has the best chance to delay descent.",
        "",
        "## Exact Final-Window Validation",
        "",
        "These exact rows enumerate every carry word at the validation length whose final height satisfies `H(w) <= barrier`.",
        "",
        *make_stats_table(payload["exact_final_windows"]),
        "",
        "### Final-Window Max Contracting Caps",
        "",
        *make_record_table(payload["exact_final_windows"], "max_contracting_cap"),
        "",
        "### Final-Window Smallest Domain Charge",
        "",
        "`domain charge = log2(first admissible n) - log2(B_w)`.  Smaller means the intercept tail is cheaper in actual integer size.",
        "",
        *make_record_table(payload["exact_final_windows"], "min_domain_charge"),
        "",
        "## Exact Prefix-Barrier Validation",
        "",
        "These exact rows enumerate every validation-length word whose every prefix stays under the same height barrier.",
        "",
        *make_stats_table(payload["exact_prefix_windows"]),
        "",
        "### Prefix-Barrier Max Contracting Caps",
        "",
        *make_record_table(payload["exact_prefix_windows"], "max_contracting_cap"),
        "",
        "### Prefix-Barrier Smallest Domain Charge",
        "",
        *make_record_table(payload["exact_prefix_windows"], "min_domain_charge"),
        "",
        "## Witness Validation",
        "",
        "The long witnesses are generated by an early-depth rule: put the extra carry depth as early as the constraints allow.  This table checks that rule against the exact validation window.",
        "",
        *make_validation_table(payload["validation_rows"]),
        "",
        "## Interpretation",
        "",
        "This is the arithmetic version of the blindspot.  Height pressure sees contraction, and intercept pressure sees a large rare tail.  The exact domain cylinder adds the missing cost: high-intercept words usually demand very large first admissible integers, and contracting words have an exact finite exception budget.",
        "",
        "The next proof-facing object is therefore a domain-constrained transfer operator: states should carry `(H, log2 B, log2 r_w or cylinder scale, exception budget)`, with exact residue updates rather than source-blind averaging.  In deep-learning language, this is the conductor packet layer that the quadratic metric averages away.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_domain_constrained_transfer.py --long-length {settings['long_length']} --exact-length {settings['exact_length']} --barriers \"{','.join(str(x) for x in settings['barriers'])}\"",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(long_length: int, exact_length: int) -> Path:
    return Path("empirical/reports") / (
        f"collatz_domain_constrained_transfer_L{long_length}_E{exact_length}.md"
    )


def default_json_path(long_length: int, exact_length: int) -> Path:
    return Path("empirical/reports") / (
        f"collatz_domain_constrained_transfer_L{long_length}_E{exact_length}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--long-length", type=int, default=120)
    parser.add_argument("--exact-length", type=int, default=10)
    parser.add_argument("--barriers", type=str, default="0,2,4,8")
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.long_length < 1:
        raise ValueError("--long-length must be at least 1")
    if args.exact_length < 1:
        raise ValueError("--exact-length must be at least 1")

    barriers = parse_barriers(args.barriers)
    final_stats = enumerate_final_windows(args.exact_length, barriers)
    prefix_stats = enumerate_prefix_windows(args.exact_length, barriers)

    payload = {
        "settings": {
            "long_length": args.long_length,
            "exact_length": args.exact_length,
            "barriers": barriers,
        },
        "long_corridors": long_corridors(args.long_length, barriers),
        "exact_final_windows": [stats.to_json() for stats in final_stats],
        "exact_prefix_windows": [stats.to_json() for stats in prefix_stats],
        "validation_rows": validation_rows(
            args.exact_length,
            barriers,
            final_stats,
            prefix_stats,
        ),
    }

    report_path = args.report or default_report_path(args.long_length, args.exact_length)
    json_path = args.json or default_json_path(args.long_length, args.exact_length)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    summary = {
        "long_corridors": len(payload["long_corridors"]),
        "exact_final_words_max_barrier": payload["exact_final_windows"][-1]["words"],
        "exact_prefix_words_max_barrier": payload["exact_prefix_windows"][-1]["words"],
    }
    print(json.dumps(rounded(summary), indent=2))


if __name__ == "__main__":
    main()
