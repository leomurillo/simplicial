"""Collatz arithmetic skeleton probe on finite quotient simplices.

This script treats a Collatz orbit as a sequence of labels in a finite
arithmetic quotient instead of as a smoothed scalar path.  The default report
tracks

* the raw orbit projected to (n mod 2^a, n mod 3^b);
* the odd-step carry depths v_2(3n+1);
* the finite-quotient closure deficit of the raw Collatz map; and
* the sampled relation of the accelerated odd map on hidden 2-adic lift bits.

It is a computational microscope, not a proof of the conjecture.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


Label = tuple[int, int]
TransitionCounts = Counter[tuple[Label, Label]]


@dataclass(frozen=True)
class OrbitSummary:
    start: int
    raw_steps: int
    ended_at_one: bool
    end_value: int
    max_value: int
    odd_bursts: int
    initial_halving_depth: int
    max_odd_carry_depth: int
    mean_odd_carry_depth: float
    mean_odd_log2_gain: float


def vp(n: int, prime: int) -> int:
    """Return the p-adic valuation of a positive integer."""

    if n <= 0:
        raise ValueError("vp is defined here only for positive integers")
    depth = 0
    while n % prime == 0:
        n //= prime
        depth += 1
    return depth


def collatz_step(n: int) -> int:
    if n <= 0:
        raise ValueError("Collatz is computed here only for positive integers")
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def accelerated_odd_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("accelerated odd step requires a positive odd integer")
    raised = 3 * n + 1
    depth = vp(raised, 2)
    return raised >> depth, depth


def raw_trajectory(start: int, max_steps: int) -> list[int]:
    if start <= 0:
        raise ValueError("start must be positive")
    values = [start]
    for _ in range(max_steps):
        if values[-1] == 1:
            break
        values.append(collatz_step(values[-1]))
    return values


def odd_trajectory(start: int, max_bursts: int) -> tuple[list[int], list[int], int]:
    """Return odd-only accelerated orbit, carry depths, and initial halving."""

    if start <= 0:
        raise ValueError("start must be positive")
    initial_halving = vp(start, 2) if start % 2 == 0 else 0
    n = start >> initial_halving
    odds = [n]
    carries: list[int] = []
    for _ in range(max_bursts):
        if n == 1:
            break
        n, depth = accelerated_odd_step(n)
        carries.append(depth)
        odds.append(n)
    return odds, carries, initial_halving


def label(n: int, two_bits: int, three_pow: int) -> Label:
    return n % (1 << two_bits), n % (3**three_pow)


def label_name(item: Label, two_bits: int) -> str:
    two, three = item
    return f"2:{two:0{two_bits}b}|3:{three}"


def all_labels(two_bits: int, three_pow: int) -> list[Label]:
    return [
        (two, three)
        for two in range(1 << two_bits)
        for three in range(3**three_pow)
    ]


def transition_counts(values: list[int], two_bits: int, three_pow: int) -> TransitionCounts:
    counts: TransitionCounts = Counter()
    for left, right in zip(values, values[1:]):
        counts[(label(left, two_bits, three_pow), label(right, two_bits, three_pow))] += 1
    return counts


def labels_seen(values: Iterable[int], two_bits: int, three_pow: int) -> Counter[Label]:
    counts: Counter[Label] = Counter()
    for n in values:
        counts[label(n, two_bits, three_pow)] += 1
    return counts


def entropy(counter: Counter[object]) -> float:
    total = sum(counter.values())
    if total == 0:
        return 0.0
    out = 0.0
    for count in counter.values():
        p = count / total
        out -= p * math.log2(p)
    return out


def matrix_rows(
    counts: TransitionCounts,
    labels: list[Label],
    two_bits: int,
    *,
    max_labels: int,
) -> list[str]:
    if len(labels) > max_labels:
        return [f"matrix omitted: {len(labels)} labels exceeds display limit {max_labels}"]

    active = sorted(
        {source for source, _target in counts} | {target for _source, target in counts},
        key=lambda item: (item[0], item[1]),
    )
    if not active:
        return ["(no transitions)"]

    short_names = {item: f"{item[0]}:{item[1]}" for item in active}
    first_col = max(len(short_names[item]) for item in active)
    cell_width = max(3, max(len(short_names[item]) for item in active))
    header = " " * (first_col + 1) + " ".join(
        short_names[item].rjust(cell_width) for item in active
    )
    rows = [header]
    for source in active:
        entries = []
        for target in active:
            value = counts.get((source, target), 0)
            entries.append(("." if value == 0 else str(value)).rjust(cell_width))
        rows.append(short_names[source].rjust(first_col) + " " + " ".join(entries))
    rows.append("")
    rows.append("Legend: row/column labels are residue2:residue3.")
    rows.append(
        "Full labels: "
        + ", ".join(f"{short_names[item]}={label_name(item, two_bits)}" for item in active)
    )
    return rows


def top_transitions(counts: TransitionCounts, two_bits: int, limit: int) -> list[str]:
    rows = []
    for (source, target), count in counts.most_common(limit):
        rows.append(
            f"- `{label_name(source, two_bits)} -> {label_name(target, two_bits)}`: `{count}`"
        )
    return rows or ["- none"]


def transition_row_entropies(counts: TransitionCounts) -> dict[str, float]:
    by_source: dict[Label, Counter[Label]] = defaultdict(Counter)
    for (source, target), count in counts.items():
        by_source[source][target] += count
    return {
        str(source): entropy(targets)
        for source, targets in sorted(by_source.items(), key=lambda item: item[0])
    }


def raw_quotient_relation(two_bits: int, three_pow: int, lift_bits: int) -> dict[int, Counter[int]]:
    """Formal one-step relation on Z/MZ, sampled over hidden lift bits."""

    modulus = (1 << two_bits) * (3**three_pow)
    lift_count = 1 << lift_bits
    relation: dict[int, Counter[int]] = {}
    for residue in range(modulus):
        targets: Counter[int] = Counter()
        for lift in range(lift_count):
            n = residue + lift * modulus
            if n == 0:
                n = lift_count * modulus
            targets[collatz_step(n) % modulus] += 1
        relation[residue] = targets
    return relation


def accelerated_odd_relation(
    two_bits: int,
    three_pow: int,
    lift_bits: int,
) -> tuple[dict[int, Counter[int]], dict[int, Counter[int]]]:
    """Odd accelerated relation on Z/MZ, sampled over hidden lift bits."""

    modulus = (1 << two_bits) * (3**three_pow)
    lift_count = 1 << lift_bits
    relation: dict[int, Counter[int]] = {}
    carries: dict[int, Counter[int]] = {}
    for residue in range(1, modulus, 2):
        targets: Counter[int] = Counter()
        carry_counts: Counter[int] = Counter()
        for lift in range(lift_count):
            n = residue + lift * modulus
            target, depth = accelerated_odd_step(n)
            targets[target % modulus] += 1
            carry_counts[depth] += 1
        relation[residue] = targets
        carries[residue] = carry_counts
    return relation, carries


def relation_summary(relation: dict[int, Counter[int]]) -> dict[str, object]:
    outdegrees = Counter(len(targets) for targets in relation.values())
    entropies = [entropy(targets) for targets in relation.values()]
    ambiguous = [
        (source, targets)
        for source, targets in relation.items()
        if len(targets) > 1
    ]
    ambiguous.sort(key=lambda item: (-len(item[1]), item[0]))
    return {
        "sources": len(relation),
        "deterministic_sources": outdegrees.get(1, 0),
        "ambiguous_sources": len(relation) - outdegrees.get(1, 0),
        "closure_deficit": sum(max(0, degree - 1) * count for degree, count in outdegrees.items()),
        "outdegree_distribution": dict(sorted(outdegrees.items())),
        "max_outdegree": max(outdegrees) if outdegrees else 0,
        "mean_row_entropy_bits": sum(entropies) / len(entropies) if entropies else 0.0,
        "max_row_entropy_bits": max(entropies) if entropies else 0.0,
        "sample_ambiguous_sources": [
            {
                "source": source,
                "targets": dict(sorted(targets.items())),
                "entropy_bits": entropy(targets),
            }
            for source, targets in ambiguous[:8]
        ],
    }


def summarize_orbit(start: int, values: list[int], carries: list[int], initial_halving: int) -> OrbitSummary:
    odd_log_gains = []
    n = start >> initial_halving
    for depth in carries:
        target = (3 * n + 1) >> depth
        odd_log_gains.append(math.log2(target) - math.log2(n))
        n = target

    return OrbitSummary(
        start=start,
        raw_steps=len(values) - 1,
        ended_at_one=values[-1] == 1,
        end_value=values[-1],
        max_value=max(values),
        odd_bursts=len(carries),
        initial_halving_depth=initial_halving,
        max_odd_carry_depth=max(carries) if carries else 0,
        mean_odd_carry_depth=sum(carries) / len(carries) if carries else 0.0,
        mean_odd_log2_gain=sum(odd_log_gains) / len(odd_log_gains) if odd_log_gains else 0.0,
    )


def range_payload(
    limit: int,
    max_steps: int,
    two_bits: int,
    three_pow: int,
) -> dict[str, object]:
    if limit <= 0:
        return {}

    total_raw_steps = 0
    ended = 0
    global_max = 0
    transition_total: TransitionCounts = Counter()
    carry_total: Counter[int] = Counter()
    stopping_times: list[int] = []
    for start in range(1, limit + 1):
        values = raw_trajectory(start, max_steps)
        odds, carries, _initial_halving = odd_trajectory(start, max_steps)
        del odds
        transition_total.update(transition_counts(values, two_bits, three_pow))
        carry_total.update(carries)
        total_raw_steps += len(values) - 1
        global_max = max(global_max, max(values))
        if values[-1] == 1:
            ended += 1
            stopping_times.append(len(values) - 1)

    return {
        "limit": limit,
        "ended_at_one": ended,
        "not_ended_within_budget": limit - ended,
        "total_raw_steps": total_raw_steps,
        "max_value_seen": global_max,
        "mean_stopping_time_ended": (
            sum(stopping_times) / len(stopping_times) if stopping_times else 0.0
        ),
        "max_stopping_time_ended": max(stopping_times) if stopping_times else 0,
        "carry_distribution": dict(sorted(carry_total.items())),
        "top_projected_transitions": [
            {
                "source": source,
                "target": target,
                "count": count,
            }
            for (source, target), count in transition_total.most_common(12)
        ],
    }


def rounded(value: object) -> object:
    if isinstance(value, float):
        return round(value, 8)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    if isinstance(value, tuple):
        return [rounded(inner) for inner in value]
    return value


def make_report(
    *,
    summary: OrbitSummary,
    values: list[int],
    odd_values: list[int],
    carries: list[int],
    transition_total: TransitionCounts,
    seen: Counter[Label],
    raw_relation_report: dict[str, object],
    odd_relation_report: dict[str, object],
    odd_relation_carries: dict[int, Counter[int]],
    range_report: dict[str, object],
    two_bits: int,
    three_pow: int,
    lift_bits: int,
    matrix_limit: int,
) -> str:
    modulus = (1 << two_bits) * (3**three_pow)
    carry_distribution = Counter(carries)
    carry_by_mod3: dict[int, Counter[int]] = defaultdict(Counter)
    for odd, depth in zip(odd_values, carries):
        carry_by_mod3[odd % (3**three_pow)][depth] += 1

    lines = [
        f"# Collatz Arithmetic Skeleton: start {summary.start}",
        "",
        "## Status",
        "",
        "This is a finite arithmetic projection of one Collatz orbit.  It is meant to expose the discrete carry structure; it is not evidence of a proof by itself.",
        "",
        f"- raw stopping steps: `{summary.raw_steps}`",
        f"- ended at one within budget: `{summary.ended_at_one}`",
        f"- end value: `{summary.end_value}`",
        f"- max value: `{summary.max_value}`",
        f"- accelerated odd bursts: `{summary.odd_bursts}`",
        f"- initial halving depth: `{summary.initial_halving_depth}`",
        f"- max odd carry depth v2(3n+1): `{summary.max_odd_carry_depth}`",
        f"- mean odd carry depth: `{summary.mean_odd_carry_depth:.6f}`",
        f"- mean odd log2 gain after full odd burst: `{summary.mean_odd_log2_gain:.6f}`",
        "",
        "## Quotient Simplex",
        "",
        f"- label: `(n mod 2^{two_bits}, n mod 3^{three_pow})`",
        f"- combined modulus: `{modulus}`",
        f"- occupied labels on this orbit: `{len(seen)}` of `{(1 << two_bits) * (3**three_pow)}`",
        f"- projected transition edges used: `{len(transition_total)}`",
        "",
        "Top projected transitions:",
        "",
        *top_transitions(transition_total, two_bits, 16),
        "",
        "Transition matrix on occupied labels:",
        "",
        "```text",
        *matrix_rows(transition_total, all_labels(two_bits, three_pow), two_bits, max_labels=matrix_limit),
        "```",
        "",
        "## Odd Carry Depths",
        "",
        "The odd operation is recorded as `n -> (3n+1)/2^s`, where `s=v2(3n+1)`.  This is the local 2-adic carry packet that a smooth interpolation tends to hide.",
        "",
        "| carry depth s | count |",
        "|---:|---:|",
    ]
    for depth, count in sorted(carry_distribution.items()):
        lines.append(f"| {depth} | {count} |")

    lines += [
        "",
        f"Carry depth split by `n mod 3^{three_pow}`:",
        "",
        "| residue | depth counts |",
        "|---:|---|",
    ]
    for residue, counts in sorted(carry_by_mod3.items()):
        text = ", ".join(f"{depth}:{count}" for depth, count in sorted(counts.items()))
        lines.append(f"| {residue} | `{text}` |")

    lines += [
        "",
        "## Finite-Quotient Closure Deficit",
        "",
        "A finite 2-adic quotient does not make the raw Collatz map closed: for an even residue, division by 2 needs one hidden lift bit.  The count below measures that missing lift information as a relation rather than forcing a false function.",
        "",
        f"- raw relation sources: `{raw_relation_report['sources']}`",
        f"- deterministic sources: `{raw_relation_report['deterministic_sources']}`",
        f"- ambiguous sources: `{raw_relation_report['ambiguous_sources']}`",
        f"- closure deficit: `{raw_relation_report['closure_deficit']}`",
        f"- outdegree distribution: `{raw_relation_report['outdegree_distribution']}`",
        f"- mean row entropy: `{raw_relation_report['mean_row_entropy_bits']:.6f}` bits",
        "",
        f"For the accelerated odd map, the script samples all lifts modulo `2^{lift_bits}` hidden lift bits over the same quotient.",
        "",
        f"- odd relation sources: `{odd_relation_report['sources']}`",
        f"- deterministic odd sources: `{odd_relation_report['deterministic_sources']}`",
        f"- ambiguous odd sources: `{odd_relation_report['ambiguous_sources']}`",
        f"- accelerated closure deficit: `{odd_relation_report['closure_deficit']}`",
        f"- odd outdegree distribution: `{odd_relation_report['outdegree_distribution']}`",
        f"- mean odd row entropy: `{odd_relation_report['mean_row_entropy_bits']:.6f}` bits",
        f"- max odd row entropy: `{odd_relation_report['max_row_entropy_bits']:.6f}` bits",
        "",
        "Most ambiguous accelerated sources:",
        "",
    ]
    for row in odd_relation_report["sample_ambiguous_sources"]:
        source = row["source"]
        target_text = ", ".join(f"{target}:{count}" for target, count in row["targets"].items())
        carry_text = ", ".join(
            f"{depth}:{count}" for depth, count in sorted(odd_relation_carries[int(source)].items())
        )
        lines.append(
            f"- source `{source}`: targets `{target_text}`, carry depths `{carry_text}`, entropy `{row['entropy_bits']:.6f}`"
        )

    if range_report:
        lines += [
            "",
            "## Range Sweep",
            "",
            f"- starts swept: `1..{range_report['limit']}`",
            f"- ended at one within budget: `{range_report['ended_at_one']}`",
            f"- not ended within budget: `{range_report['not_ended_within_budget']}`",
            f"- total raw steps: `{range_report['total_raw_steps']}`",
            f"- max value seen: `{range_report['max_value_seen']}`",
            f"- mean stopping time among ended starts: `{range_report['mean_stopping_time_ended']:.6f}`",
            f"- max stopping time among ended starts: `{range_report['max_stopping_time_ended']}`",
            f"- carry distribution: `{range_report['carry_distribution']}`",
        ]

    lines += [
        "",
        "## Interpretation",
        "",
        "The low-dimensional mod-2/mod-3 picture is the entrance ramp, but the nontrivial object is the lift-sensitive relation.  The raw map exposes a predictable division-by-2 ambiguity, while the accelerated odd map records the variable carry depth created by `3n+1`.  That is the Collatz version of a discrete skeleton: finite categorical labels, transition operators, and explicit carry data instead of a smoothed curve.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_arithmetic_skeleton.py --start {summary.start} --two-bits {two_bits} --three-pow {three_pow} --lift-bits {lift_bits}",
        "python empirical/collatz_arithmetic_skeleton.py --start 27 --two-bits 4 --three-pow 1 --range-limit 10000",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(start: int, two_bits: int, three_pow: int) -> Path:
    return Path("empirical/reports") / f"collatz_skeleton_start_{start}_2p{two_bits}_3p{three_pow}.md"


def default_json_path(start: int, two_bits: int, three_pow: int) -> Path:
    return Path("empirical/reports") / f"collatz_skeleton_start_{start}_2p{two_bits}_3p{three_pow}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=27)
    parser.add_argument("--two-bits", type=int, default=4)
    parser.add_argument("--three-pow", type=int, default=1)
    parser.add_argument("--lift-bits", type=int, default=8)
    parser.add_argument("--max-steps", type=int, default=10000)
    parser.add_argument("--range-limit", type=int, default=0)
    parser.add_argument("--matrix-limit", type=int, default=64)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.two_bits < 1:
        raise ValueError("--two-bits must be at least 1 so parity is visible")
    if args.three_pow < 1:
        raise ValueError("--three-pow must be at least 1")
    if args.lift_bits < 1:
        raise ValueError("--lift-bits must be at least 1")

    values = raw_trajectory(args.start, args.max_steps)
    odd_values, carries, initial_halving = odd_trajectory(args.start, args.max_steps)
    summary = summarize_orbit(args.start, values, carries, initial_halving)
    transitions = transition_counts(values, args.two_bits, args.three_pow)
    seen = labels_seen(values, args.two_bits, args.three_pow)

    raw_relation = raw_quotient_relation(args.two_bits, args.three_pow, 1)
    raw_relation_report = relation_summary(raw_relation)
    odd_relation, odd_relation_carries = accelerated_odd_relation(
        args.two_bits,
        args.three_pow,
        args.lift_bits,
    )
    odd_relation_report = relation_summary(odd_relation)
    sweep = range_payload(
        args.range_limit,
        args.max_steps,
        args.two_bits,
        args.three_pow,
    )

    report_path = args.report or default_report_path(args.start, args.two_bits, args.three_pow)
    json_path = args.json or default_json_path(args.start, args.two_bits, args.three_pow)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report = make_report(
        summary=summary,
        values=values,
        odd_values=odd_values,
        carries=carries,
        transition_total=transitions,
        seen=seen,
        raw_relation_report=raw_relation_report,
        odd_relation_report=odd_relation_report,
        odd_relation_carries=odd_relation_carries,
        range_report=sweep,
        two_bits=args.two_bits,
        three_pow=args.three_pow,
        lift_bits=args.lift_bits,
        matrix_limit=args.matrix_limit,
    )
    report_path.write_text(report, encoding="utf-8")

    payload = {
        "summary": summary.__dict__,
        "settings": {
            "two_bits": args.two_bits,
            "three_pow": args.three_pow,
            "lift_bits": args.lift_bits,
            "max_steps": args.max_steps,
            "range_limit": args.range_limit,
        },
        "raw_trajectory": values,
        "odd_trajectory": odd_values,
        "odd_carry_depths": carries,
        "projected_label_counts": dict(seen),
        "projected_transition_counts": {
            f"{source}->{target}": count
            for (source, target), count in sorted(transitions.items())
        },
        "projected_row_entropies": transition_row_entropies(transitions),
        "raw_quotient_relation_summary": raw_relation_report,
        "accelerated_odd_relation_summary": odd_relation_report,
        "range_sweep": sweep,
    }
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(summary.__dict__), indent=2))


if __name__ == "__main__":
    main()
