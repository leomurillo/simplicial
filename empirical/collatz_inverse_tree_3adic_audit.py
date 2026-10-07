"""3-adic audit for the flipped Collatz inverse tree.

The forward Collatz map hides the prime 3 in the odd step.  The inverse tree
puts it in the open:

    D(x) = 2x,
    U(x) = (x - 1) / 3.

If the branches are applied without integrality restrictions, every binary
word lands in Z[1/3].  Landing back in Z is exactly a 3-adic divisibility
condition on the accumulated numerator.  This is the missing companion to the
2-adic carry-depth audits.

The shifted form mentioned in the notes is also audited:

    A(x) = 2x - 1,
    B(x) = 2x / 3.

These unrestricted trees are support objects.  The true integer inverse
Collatz tree is obtained by imposing extra congruence/parity constraints on
the U branch.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


CYCLES_ALL_Z = [
    (0,),
    (1, 4, 2),
    (-1, -2),
    (-5, -14, -7, -20, -10),
    (
        -17,
        -50,
        -25,
        -74,
        -37,
        -110,
        -55,
        -164,
        -82,
        -41,
        -122,
        -61,
        -182,
        -91,
        -272,
        -136,
        -68,
        -34,
    ),
]


def collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def v3(value: int) -> int:
    value = abs(value)
    if value == 0:
        return 10**9
    count = 0
    while value % 3 == 0:
        count += 1
        value //= 3
    return count


def reduced_denominator_exponent(numerator: int, denominator_exponent: int) -> int:
    return max(0, denominator_exponent - v3(numerator))


def exact_integer_value(numerator: int, denominator_exponent: int) -> int | None:
    power = 3**denominator_exponent
    if numerator % power:
        return None
    return numerator // power


def branch_states(
    states: Iterable[tuple[int, int]],
    powers3: list[int],
    system: str,
) -> list[tuple[int, int]]:
    next_states: list[tuple[int, int]] = []
    for numerator, exponent in states:
        denominator = powers3[exponent]
        if system == "inverse":
            next_states.append((2 * numerator, exponent))
            next_states.append((numerator - denominator, exponent + 1))
        elif system == "shifted":
            next_states.append((2 * numerator - denominator, exponent))
            next_states.append((2 * numerator, exponent + 1))
        else:
            raise ValueError(f"unknown branch system: {system}")
    return next_states


def top_denominator_distribution(
    denominator_counts: Counter[int],
    limit: int = 8,
) -> list[dict[str, Any]]:
    return [
        {"denominator_exponent": exponent, "count": count}
        for exponent, count in denominator_counts.most_common(limit)
    ]


def selected_lengths(max_length: int) -> list[int]:
    candidates = [1, 2, 3, 4, 5, 8, 10, 12, 14, 16, 18, 20, 24]
    out = [length for length in candidates if length <= max_length]
    if max_length not in out:
        out.append(max_length)
    return sorted(set(out))


def audit_branch_system(
    *,
    label: str,
    system: str,
    seed: int,
    max_length: int,
) -> dict[str, Any]:
    powers3 = [1]
    for _index in range(max_length + 2):
        powers3.append(powers3[-1] * 3)

    states: list[tuple[int, int]] = [(seed, 0)]
    rows: list[dict[str, Any]] = []
    selected = set(selected_lengths(max_length))
    selected_rows: list[dict[str, Any]] = []
    final_integer_values: list[int] = []

    for length in range(1, max_length + 1):
        states = branch_states(states, powers3, system)
        denominator_counts: Counter[int] = Counter()
        integer_values: list[int] = []

        for numerator, exponent in states:
            reduced_exponent = reduced_denominator_exponent(numerator, exponent)
            denominator_counts[reduced_exponent] += 1
            if reduced_exponent == 0:
                value = exact_integer_value(numerator, exponent)
                if value is None:
                    raise AssertionError("reduced denominator says integer but division failed")
                integer_values.append(value)

        total = len(states)
        integer_count = len(integer_values)
        row = {
            "length": length,
            "total_words": total,
            "integer_word_count": integer_count,
            "integer_word_density": integer_count / total,
            "noninteger_word_count": total - integer_count,
            "distinct_integer_endpoints": len(set(integer_values)),
            "top_denominator_exponents": top_denominator_distribution(denominator_counts),
        }
        rows.append(row)
        if length in selected:
            selected_rows.append(row)
        if length == max_length:
            final_integer_values = integer_values

    return {
        "label": label,
        "system": system,
        "seed": seed,
        "max_length": max_length,
        "selected_rows": selected_rows,
        "final": rows[-1],
        "final_integer_sample": sorted(set(final_integer_values))[:40],
        "final_integer_tail_sample": sorted(set(final_integer_values))[-40:],
    }


def verify_cycles() -> list[dict[str, Any]]:
    records = []
    for cycle in CYCLES_ALL_Z:
        image = tuple(collatz_step(n) for n in cycle)
        rotated_target = cycle[1:] + cycle[:1]
        records.append(
            {
                "cycle": list(cycle),
                "length": len(cycle),
                "verified": image == rotated_target,
            }
        )
    return records


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


def make_branch_table(audit: dict[str, Any]) -> list[str]:
    lines = [
        f"| L | words | integer words | integer density | distinct integer endpoints | dominant reduced denominator exponents ({audit['label']}) |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in audit["selected_rows"]:
        top = ", ".join(
            f"3^-{item['denominator_exponent']}:{item['count']}"
            for item in row["top_denominator_exponents"][:5]
        )
        lines.append(
            f"| {row['length']} | {row['total_words']} | "
            f"{row['integer_word_count']} | {row['integer_word_density']:.12f} | "
            f"{row['distinct_integer_endpoints']} | {top} |"
        )
    return lines


def make_cycle_table(cycles: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| cycle | length | verified |",
        "|---|---:|---|",
    ]
    for record in cycles:
        cycle = ", ".join(str(n) for n in record["cycle"])
        lines.append(f"| `{cycle}` | {record['length']} | {record['verified']} |")
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    lines = [
        "# Collatz Inverse Tree 3-Adic Audit",
        "",
        "## Meaning",
        "",
        "The forward carry audits were mostly 2-adic because the accelerated map divides by powers of 2.  The flipped inverse tree exposes the missing prime: unrestricted inverse words live in `Z[1/3]`, and returning to `Z` is a 3-adic divisibility condition.",
        "",
        "For the unrestricted inverse branches",
        "",
        "```text",
        "D(x) = 2x",
        "U(x) = (x - 1)/3",
        "```",
        "",
        "a binary word with `k` uses of `U` lands at `N / 3^k`.  It is an integer exactly when `v_3(N) >= k`.  That is the 3-adic closure test.",
        "",
        "The shifted branch system is also audited:",
        "",
        "```text",
        "A(x) = 2x - 1",
        "B(x) = 2x/3",
        "```",
        "",
        "## Branch Audits",
        "",
    ]
    for audit in payload["branch_audits"]:
        lines.extend(
            [
                f"### {audit['label']}",
                "",
                f"- seed: `{audit['seed']}`",
                f"- max length: `{audit['max_length']}`",
                f"- final integer words: `{audit['final']['integer_word_count']}` / `{audit['final']['total_words']}`",
                f"- final integer density: `{audit['final']['integer_word_density']:.12f}`",
                "",
                *make_branch_table(audit),
                "",
            ]
        )

    lines.extend(
        [
            "## Integer Cycles In All Z",
            "",
            "These are included as a calibration row for the flipped picture.  A correct global story has to keep the positive, zero, and negative basins separate.",
            "",
            *make_cycle_table(payload["cycles_all_z"]),
            "",
            "## Interpretation",
            "",
            "The flip is worth doing.  The binary branch support is huge, but integrality is a thin 3-adic condition.  That means our previous 2-adic residue/carry ledger was only half of the filtered algebra.  The natural object is a mixed `2`/`3` path algebra:",
            "",
            "- `2`-adic data controls forward carry depth and descent margins.",
            "- `3`-adic data controls which inverse binary words are honest integer nodes rather than `Z[1/3]` shadows.",
            "- the five integer cycles are boundary components of the all-`Z` dynamics, not noise.",
            "",
            "The next useful theorem form is therefore not purely 2-adic:",
            "",
            "```text",
            "Every infinite support path in the inverse 2/3 branch algebra either",
            "falls into one of the five integer cycle components or has a",
            "nonzero 3-adic denominator defect at some finite stage.",
            "```",
            "",
            "That is the flipped version of the closure-deficit question: support paths are easy; integer paths require simultaneous 2-adic and 3-adic closure.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            f"python empirical/collatz_inverse_tree_3adic_audit.py --max-length {settings['max_length']}",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def default_report_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_inverse_tree_3adic_L{max_length}.md"


def default_json_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_inverse_tree_3adic_L{max_length}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=20)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_length > 24:
        raise ValueError("max length above 24 enumerates too many binary words")

    branch_audits = [
        audit_branch_system(
            label="inverse D/U from seed 1",
            system="inverse",
            seed=1,
            max_length=args.max_length,
        ),
        audit_branch_system(
            label="inverse D/U from seed 2",
            system="inverse",
            seed=2,
            max_length=args.max_length,
        ),
        audit_branch_system(
            label="shifted A/B from seed 2",
            system="shifted",
            seed=2,
            max_length=args.max_length,
        ),
    ]
    payload = {
        "settings": {"max_length": args.max_length},
        "branch_audits": branch_audits,
        "cycles_all_z": verify_cycles(),
    }

    report_path = args.report or default_report_path(args.max_length)
    json_path = args.json or default_json_path(args.max_length)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(
        json.dumps(
            rounded(
                {
                    "finals": [
                        {
                            "label": audit["label"],
                            **audit["final"],
                        }
                        for audit in branch_audits
                    ],
                    "cycles_verified": all(
                        record["verified"] for record in payload["cycles_all_z"]
                    ),
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
