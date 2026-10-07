"""Gauge holonomy for the mixed 2/3 inverse Collatz path algebra.

The one-step mixed inverse audit shows that

    D(x) = 2x
    U(x) = (x - 1) / 3

is not same-level closed on a quotient M = 2^a 3^b.  A U step consumes one
extra 3-adic digit, so a word W with u occurrences of U is naturally a
filtered arrow

    R / (3^u M)  ->  R / M.

If the word has d occurrences of D, changing the initial lift digit
q in Z/(3^u) changes the final target phase by

    q |-> 2^d q mod 3^u.

This script verifies that law on finite quotients, records which support
words fail the honest parity gate, and compares the resulting signatures with
the known integer cycles and the existing primitive carry-necklace sieve.

This is a proof-facing audit, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any


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


@dataclass(frozen=True)
class CycleCarry:
    start_odd: int
    carry: int
    target_odd: int
    verified: bool


def collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def count_letters(word: str) -> tuple[int, int]:
    d_count = word.count("D")
    u_count = word.count("U")
    return d_count, u_count


def word_label(word: str) -> str:
    if len(word) <= 18:
        return word
    pieces: list[str] = []
    run_char = word[0]
    run_length = 0
    for char in word:
        if char == run_char:
            run_length += 1
            continue
        pieces.append(run_char if run_length == 1 else f"{run_char}^{run_length}")
        run_char = char
        run_length = 1
    pieces.append(run_char if run_length == 1 else f"{run_char}^{run_length}")
    return " ".join(pieces)


def carry_word_text(word: list[int] | tuple[int, ...]) -> str:
    return "(" + ",".join(str(item) for item in word) + ")"


def inverse_word_from_carry(carries: list[int] | tuple[int, ...]) -> str:
    return "".join("D" * carry + "U" for carry in carries)


def multiplicative_order(value: int, modulus: int) -> int | None:
    if modulus <= 1 or math.gcd(value, modulus) != 1:
        return None
    current = 1
    for order in range(1, modulus + 1):
        current = (current * value) % modulus
        if current == 1:
            return order
    raise AssertionError("multiplicative order search failed")


def apply_branch_word(word: str, residue: int, modulus: int) -> int | None:
    current_modulus = modulus
    current = residue % current_modulus
    for branch in word:
        if branch == "D":
            current = (2 * current) % current_modulus
            continue
        if branch != "U":
            raise ValueError(f"unknown branch {branch!r}")
        if current_modulus % 3:
            raise ValueError("U branch requires a 3-refined source modulus")
        if current % 6 != 4:
            return None
        current_modulus //= 3
        current = ((current - 1) // 3) % current_modulus
    return current


def audit_branch_word(
    word: str,
    *,
    two_bits: int,
    three_depth: int,
    sample_limit: int,
) -> dict[str, Any]:
    d_count, u_count = count_letters(word)
    if u_count > three_depth:
        raise ValueError("three_depth must be at least the number of U branches")
    base_modulus = (1 << two_bits) * (3**three_depth)
    lift_count = 3**u_count
    source_modulus = base_modulus * lift_count
    gauge_modulus = base_modulus // lift_count if u_count else None
    phase_multiplier = pow(2, d_count, lift_count) if u_count else None
    phase_order = (
        multiplicative_order(phase_multiplier, lift_count)
        if phase_multiplier is not None
        else None
    )

    legal_coarse_sources = 0
    full_lift_arrows = 0
    target_widths: Counter[int] = Counter()
    gauge_orbit_violations = 0
    phase_law_violations = 0
    phase_offsets: Counter[int] = Counter()
    samples: list[dict[str, Any]] = []

    for coarse_residue in range(base_modulus):
        q_targets: list[tuple[int, int]] = []
        for lift_digit in range(lift_count):
            source = coarse_residue + lift_digit * base_modulus
            target = apply_branch_word(word, source, source_modulus)
            if target is not None:
                q_targets.append((lift_digit, target))

        if not q_targets:
            continue

        legal_coarse_sources += 1
        full_lift_arrows += len(q_targets)
        target_set = {target for _lift_digit, target in q_targets}
        target_widths[len(target_set)] += 1

        if u_count == 0:
            continue

        if gauge_modulus is None:
            raise AssertionError("gauge modulus missing for a U word")
        orbit_bases = {target % gauge_modulus for _lift_digit, target in q_targets}
        if len(orbit_bases) != 1:
            gauge_orbit_violations += 1
            continue
        orbit_base = next(iter(orbit_bases))
        phase_by_lift = {
            lift_digit: ((target - orbit_base) // gauge_modulus) % lift_count
            for lift_digit, target in q_targets
        }
        phase_zero = phase_by_lift.get(0)
        if phase_zero is None:
            phase_law_violations += 1
            continue
        phase_offset = phase_zero
        phase_offsets[phase_offset] += 1
        for lift_digit, phase in phase_by_lift.items():
            expected = (phase_offset + phase_multiplier * lift_digit) % lift_count
            if phase != expected:
                phase_law_violations += 1
                break

        if len(samples) < sample_limit:
            sample_pairs = [
                {
                    "lift_digit": lift_digit,
                    "target": target,
                    "phase": phase_by_lift[lift_digit],
                }
                for lift_digit, target in q_targets[: min(lift_count, 12)]
            ]
            samples.append(
                {
                    "coarse_source": coarse_residue,
                    "orbit_base": orbit_base,
                    "phase_offset": phase_offset,
                    "lift_to_phase_sample": sample_pairs,
                }
            )

    raw_closure_deficit = (
        None
        if full_lift_arrows == 0
        else 1.0 - legal_coarse_sources / full_lift_arrows
    )
    expected_width = lift_count
    width_law_holds = (
        u_count == 0
        or full_lift_arrows == 0
        or target_widths == Counter({expected_width: legal_coarse_sources})
    )
    gauge_law_holds = (
        u_count == 0
        or full_lift_arrows == 0
        or (
            gauge_orbit_violations == 0
            and phase_law_violations == 0
            and width_law_holds
            and full_lift_arrows == legal_coarse_sources * lift_count
        )
    )

    return {
        "word": word,
        "word_label": word_label(word),
        "length": len(word),
        "D_count": d_count,
        "U_count": u_count,
        "base_modulus": base_modulus,
        "source_modulus": source_modulus,
        "lift_count": lift_count,
        "gauge_modulus": gauge_modulus,
        "legal_coarse_sources": legal_coarse_sources,
        "legal_source_fraction": legal_coarse_sources / base_modulus,
        "full_lift_arrows": full_lift_arrows,
        "target_width_distribution": {
            str(width): target_widths[width] for width in sorted(target_widths)
        },
        "raw_closure_deficit": raw_closure_deficit,
        "gauge_reduced_closure_deficit": (
            None if full_lift_arrows == 0 or u_count == 0 else 0.0
        ),
        "phase_modulus": lift_count if u_count else None,
        "phase_multiplier": phase_multiplier,
        "phase_identity": (
            None if phase_multiplier is None else phase_multiplier % lift_count == 1
        ),
        "phase_order": phase_order,
        "phase_offsets": {
            str(offset): phase_offsets[offset] for offset in sorted(phase_offsets)
        },
        "gauge_orbit_violations": gauge_orbit_violations,
        "phase_law_violations": phase_law_violations,
        "width_law_holds": width_law_holds,
        "gauge_law_holds": gauge_law_holds,
        "honest_possible": legal_coarse_sources > 0,
        "samples": samples,
    }


def generate_words(max_word_length: int, three_depth: int) -> list[str]:
    words: list[str] = []
    for length in range(1, max_word_length + 1):
        for letters in product(("D", "U"), repeat=length):
            word = "".join(letters)
            if word.count("U") <= three_depth:
                words.append(word)
    return words


def audit_words(
    *,
    max_word_length: int,
    two_bits: int,
    three_depth: int,
    sample_limit: int,
) -> list[dict[str, Any]]:
    return [
        audit_branch_word(
            word,
            two_bits=two_bits,
            three_depth=three_depth,
            sample_limit=sample_limit,
        )
        for word in generate_words(max_word_length, three_depth)
    ]


def group_audits(audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[int, int, int], dict[str, Any]] = {}
    for audit in audits:
        key = (audit["length"], audit["D_count"], audit["U_count"])
        row = grouped.setdefault(
            key,
            {
                "length": audit["length"],
                "D_count": audit["D_count"],
                "U_count": audit["U_count"],
                "words": 0,
                "honest_possible_words": 0,
                "parity_defect_words": 0,
                "min_legal_source_fraction": None,
                "max_legal_source_fraction": None,
                "phase_multiplier": audit["phase_multiplier"],
                "phase_modulus": audit["phase_modulus"],
                "phase_identity_words": 0,
                "gauge_law_failures": 0,
            },
        )
        row["words"] += 1
        if audit["honest_possible"]:
            row["honest_possible_words"] += 1
            fraction = audit["legal_source_fraction"]
            row["min_legal_source_fraction"] = (
                fraction
                if row["min_legal_source_fraction"] is None
                else min(row["min_legal_source_fraction"], fraction)
            )
            row["max_legal_source_fraction"] = (
                fraction
                if row["max_legal_source_fraction"] is None
                else max(row["max_legal_source_fraction"], fraction)
            )
        else:
            row["parity_defect_words"] += 1
        if audit["phase_identity"] is True:
            row["phase_identity_words"] += 1
        if not audit["gauge_law_holds"]:
            row["gauge_law_failures"] += 1
    return [grouped[key] for key in sorted(grouped)]


def accelerated_cycle_carries(cycle: tuple[int, ...]) -> list[CycleCarry]:
    odd_positions = [index for index, value in enumerate(cycle) if value % 2]
    if not odd_positions:
        return []
    records: list[CycleCarry] = []
    for local_index, position in enumerate(odd_positions):
        start = cycle[position]
        raised = 3 * start + 1
        carry = 0
        target = raised
        while target and target % 2 == 0:
            target //= 2
            carry += 1
        expected = cycle[odd_positions[(local_index + 1) % len(odd_positions)]]
        records.append(
            CycleCarry(
                start_odd=start,
                carry=carry,
                target_odd=target,
                verified=target == expected,
            )
        )
    return records


def cycle_component(cycle: tuple[int, ...]) -> str:
    if all(value == 0 for value in cycle):
        return "zero"
    if all(value > 0 for value in cycle):
        return "positive"
    if all(value < 0 for value in cycle):
        return "negative"
    return "mixed"


def cycle_holonomy_records() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for cycle in CYCLES_ALL_Z:
        carries = accelerated_cycle_carries(cycle)
        carry_word = [record.carry for record in carries]
        m = len(carry_word)
        total_depth = sum(carry_word)
        phase_modulus = 3**m if m else None
        phase_multiplier = pow(2, total_depth, phase_modulus) if m else None
        rows.append(
            {
                "cycle": list(cycle),
                "component": cycle_component(cycle),
                "verified_full_cycle": tuple(collatz_step(n) for n in cycle)
                == cycle[1:] + cycle[:1],
                "accelerated_verified": all(record.verified for record in carries),
                "carry_word": carry_word,
                "m": m,
                "S": total_depth,
                "inverse_word": inverse_word_from_carry(carry_word),
                "phase_modulus": phase_modulus,
                "phase_multiplier": phase_multiplier,
                "phase_identity": (
                    None
                    if phase_multiplier is None
                    else phase_multiplier % phase_modulus == 1
                ),
                "phase_order": (
                    None
                    if phase_multiplier is None
                    else multiplicative_order(phase_multiplier, phase_modulus)
                ),
            }
        )
    return rows


def sieve_record_holonomy(record: dict[str, Any], section: str) -> dict[str, Any]:
    m = int(record["length"])
    total_depth = int(record["total_depth"])
    phase_modulus = 3**m
    phase_multiplier = pow(2, total_depth, phase_modulus)
    best = record["best_rotation"]
    return {
        "section": section,
        "representative": record["representative"],
        "best_rotation": best["word"],
        "m": m,
        "S": total_depth,
        "phase_modulus": phase_modulus,
        "phase_multiplier": phase_multiplier,
        "phase_identity": phase_multiplier == 1,
        "phase_order": multiplicative_order(phase_multiplier, phase_modulus),
        "best_reduced_denominator": record["best_reduced_denominator"],
        "best_modular_residue": record["best_modular_residue"],
        "exact": record["exact_rotation"] is not None,
        "candidate": (
            None
            if record["exact_rotation"] is None
            else record["exact_rotation"]["cycle_candidate"]
        ),
    }


def load_sieve_comparison(path: Path | None, limit: int) -> dict[str, Any] | None:
    if path is None or not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    for section in (
        "exact_records",
        "closest_divisibility",
        "closest_modular",
        "near_resonant",
    ):
        for record in data.get(section, [])[:limit]:
            rows.append(sieve_record_holonomy(record, section))
    identity_misses = [
        row
        for row in rows
        if row["phase_identity"] and not row["exact"] and row["section"] != "exact_records"
    ]
    return {
        "path": str(path),
        "settings": data.get("settings", {}),
        "totals": data.get("totals", {}),
        "rows": rows,
        "identity_miss_count": len(identity_misses),
        "identity_miss_examples": identity_misses[:limit],
    }


def choose_example_audits(audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_word = {audit["word"]: audit for audit in audits}
    preferred = [
        "U",
        "DU",
        "DDU",
        "UDD",
        "UU",
        "DUU",
        "UDU",
        "DUDU",
        "DDUDU",
    ]
    examples = [by_word[word] for word in preferred if word in by_word]
    seen = {audit["word"] for audit in examples}
    for audit in audits:
        if len(examples) >= 12:
            break
        if audit["word"] in seen:
            continue
        if not audit["honest_possible"] or audit["phase_identity"] is False:
            examples.append(audit)
            seen.add(audit["word"])
    return examples


def verification_summary(audits: list[dict[str, Any]]) -> dict[str, Any]:
    gauge_words = [
        audit for audit in audits if audit["U_count"] > 0 and audit["honest_possible"]
    ]
    return {
        "audited_words": len(audits),
        "honest_possible_words": sum(1 for audit in audits if audit["honest_possible"]),
        "parity_defect_words": sum(1 for audit in audits if not audit["honest_possible"]),
        "gauge_words_with_sources": len(gauge_words),
        "gauge_orbit_violations": sum(
            audit["gauge_orbit_violations"] for audit in gauge_words
        ),
        "phase_law_violations": sum(
            audit["phase_law_violations"] for audit in gauge_words
        ),
        "width_law_failures": sum(
            1 for audit in gauge_words if not audit["width_law_holds"]
        ),
        "gauge_law_failures": sum(
            1 for audit in gauge_words if not audit["gauge_law_holds"]
        ),
    }


def rounded(value: object) -> object:
    if isinstance(value, float):
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
        return f"{value:.12f}"
    return str(value)


def make_example_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| word | d | u | legal sources | source fraction | target width | raw deficit | phase | order | identity |",
        "|---|---:|---:|---:|---:|---|---:|---|---:|---|",
    ]
    for row in rows:
        width = ", ".join(
            f"{width}:{count}" for width, count in row["target_width_distribution"].items()
        )
        phase = (
            "-"
            if row["phase_multiplier"] is None
            else f"{row['phase_multiplier']} mod {row['phase_modulus']}"
        )
        lines.append(
            f"| `{row['word_label']}` | {row['D_count']} | {row['U_count']} | "
            f"{row['legal_coarse_sources']} | "
            f"{row['legal_source_fraction']:.12f} | "
            f"{width or '-'} | {number_or_dash(row['raw_closure_deficit'])} | "
            f"{phase} | {number_or_dash(row['phase_order'])} | "
            f"{number_or_dash(row['phase_identity'])} |"
        )
    return lines


def make_group_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| L | d | u | words | honest possible | parity defects | source fraction range | phase | identity words | law failures |",
        "|---:|---:|---:|---:|---:|---:|---|---|---:|---:|",
    ]
    for row in rows:
        if row["min_legal_source_fraction"] is None:
            fraction_range = "-"
        else:
            fraction_range = (
                f"{row['min_legal_source_fraction']:.6f}"
                f"..{row['max_legal_source_fraction']:.6f}"
            )
        phase = (
            "-"
            if row["phase_multiplier"] is None
            else f"{row['phase_multiplier']} mod {row['phase_modulus']}"
        )
        lines.append(
            f"| {row['length']} | {row['D_count']} | {row['U_count']} | "
            f"{row['words']} | {row['honest_possible_words']} | "
            f"{row['parity_defect_words']} | {fraction_range} | {phase} | "
            f"{row['phase_identity_words']} | {row['gauge_law_failures']} |"
        )
    return lines


def make_cycle_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| component | cycle | carries | m | S | phase | order | identity | verified |",
        "|---|---|---|---:|---:|---|---:|---|---|",
    ]
    for row in rows:
        cycle = ", ".join(str(value) for value in row["cycle"])
        phase = (
            "-"
            if row["phase_multiplier"] is None
            else f"{row['phase_multiplier']} mod {row['phase_modulus']}"
        )
        lines.append(
            f"| {row['component']} | `{cycle}` | "
            f"`{carry_word_text(row['carry_word'])}` | {row['m']} | {row['S']} | "
            f"{phase} | {number_or_dash(row['phase_order'])} | "
            f"{number_or_dash(row['phase_identity'])} | "
            f"{row['verified_full_cycle'] and row['accelerated_verified']} |"
        )
    return lines


def make_sieve_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| section | necklace | m | S | phase | order | identity | reduced denom | mod residue | exact |",
        "|---|---|---:|---:|---|---:|---|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['section']} | `{carry_word_text(row['representative'])}` | "
            f"{row['m']} | {row['S']} | "
            f"{row['phase_multiplier']} mod {row['phase_modulus']} | "
            f"{number_or_dash(row['phase_order'])} | {row['phase_identity']} | "
            f"{number_or_dash(row['best_reduced_denominator'])} | "
            f"{number_or_dash(row['best_modular_residue'])} | {row['exact']} |"
        )
    return lines


def make_sample_phase_table(example: dict[str, Any]) -> list[str]:
    if not example["samples"]:
        return ["_No honest source sample for this word._"]
    sample = example["samples"][0]
    lines = [
        f"Sample for word `{example['word_label']}`, coarse source `{sample['coarse_source']}`, orbit base `{sample['orbit_base']}`:",
        "",
        "| lift digit q | target | final phase |",
        "|---:|---:|---:|",
    ]
    for item in sample["lift_to_phase_sample"]:
        lines.append(
            f"| {item['lift_digit']} | {item['target']} | {item['phase']} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    verification = payload["verification"]
    examples = payload["examples"]
    sample_example = next(
        (
            example
            for example in examples
            if example["word"] == "UDU" and example["samples"]
        ),
        next((example for example in examples if example["samples"]), examples[0]),
    )
    lines = [
        "# Collatz Gauge Holonomy Audit",
        "",
        "## Meaning",
        "",
        "A branch word `W` in the inverse alphabet `D(x)=2x`, `U(x)=(x-1)/3` is not merely a support word.  If `W` has `u` uses of `U`, then the honest finite quotient arrow is",
        "",
        "```text",
        "R / (3^u M) -> R / M,    M = 2^a 3^b.",
        "```",
        "",
        "The lift digit `q mod 3^u` is the gauge coordinate.  If `W` has `d` uses of `D`, changing that digit changes the final phase by",
        "",
        "```text",
        "q -> phi_0(r) + 2^d q mod 3^u.",
        "```",
        "",
        "The offset `phi_0(r)` depends on the coarse source.  The multiplier `2^d mod 3^u` is the gauge holonomy of the support word.",
        "",
        "## Settings",
        "",
        f"- base quotient: `M = 2^{settings['two_bits']} 3^{settings['three_depth']} = {settings['base_modulus']}`",
        f"- audited branch-word length: `1..{settings['max_word_length']}`",
        f"- imported cycle sieve: `{settings['cycle_sieve_json']}`",
        "",
        "## Verification",
        "",
        f"- audited words: `{verification['audited_words']}`",
        f"- words with honest sources: `{verification['honest_possible_words']}`",
        f"- finite parity-defect words: `{verification['parity_defect_words']}`",
        f"- gauge words with sources: `{verification['gauge_words_with_sources']}`",
        f"- gauge orbit violations: `{verification['gauge_orbit_violations']}`",
        f"- phase-law violations: `{verification['phase_law_violations']}`",
        f"- target-width law failures: `{verification['width_law_failures']}`",
        f"- gauge-law failures: `{verification['gauge_law_failures']}`",
        "",
        "For every audited word with honest sources, the raw same-level multivaluedness is exactly one `Z/3^u` gauge orbit.  The gauge-reduced closure deficit is zero.  Words with no honest source have already developed a finite 2-adic parity defect.",
        "",
        "## Branch Examples",
        "",
        *make_example_table(examples),
        "",
        *make_sample_phase_table(sample_example),
        "",
        "## Support Ledger",
        "",
        *make_group_table(payload["groups"]),
        "",
        "## Integer Cycle Calibration",
        "",
        "The all-`Z` calibration cycles remain separate components.  The positive `1 -> 4 -> 2 -> 1` component has identity gauge holonomy; the negative components carry nontrivial phase holonomy.",
        "",
        *make_cycle_table(payload["cycle_holonomy"]),
        "",
    ]
    sieve = payload["sieve_comparison"]
    if sieve is not None:
        lines.extend(
            [
                "## Forward Cycle-Sieve Comparison",
                "",
                f"- source: `{sieve['path']}`",
                f"- exact cycle necklaces: `{sieve['totals'].get('exact_cycle_necklaces')}`",
                f"- nontrivial exact cycle necklaces: `{sieve['totals'].get('nontrivial_exact_cycle_necklaces')}`",
                f"- identity-holonomy misses in displayed comparison rows: `{sieve['identity_miss_count']}`",
                "",
                *make_sieve_table(sieve["rows"]),
                "",
                "Holonomy identity is not the same as the cycle equation: displayed misses such as `(4)`, `(6)`, `(8)`, or `(1,5)` can have identity phase but still fail divisibility.  The cycle obstruction is still the exact affine fixed-point equation; holonomy is the filtered bookkeeping that prevents us from mistaking same-level multivaluedness for dynamics.",
                "",
            ]
        )
    lines.extend(
        [
            "## Theorem Candidate After The Audit",
            "",
            "The clean local statement is now:",
            "",
            "```text",
            "For M = 2^a 3^b and every inverse branch word W with u <= b,",
            "the honest finite quotient relation is either empty because a",
            "U parity gate fails, or it is a principal Z/(3^u) gauge orbit",
            "over each legal coarse source.  Its holonomy multiplier is",
            "2^d mod 3^u, where d is the number of D branches in W.",
            "```",
            "",
            "The global Collatz-facing target therefore splits cleanly:",
            "",
            "```text",
            "Local closure: handled by the mixed 2/3 filtered path algebra.",
            "Cycle obstructions: the primitive carry-necklace divisibility problem.",
            "Escape/descent: the q_w >= 0 margin problem on contracting carry words.",
            "```",
            "",
            "So the mission does not end in a proof claim.  It ends in a sharper skeleton: same-level U closure deficits are gauge artifacts; impossible inverse support words are finite parity defects; remaining positive periodic obstructions reduce to the carry-cycle equation and the descent-margin lemma.",
            "",
            "## Reproduction",
            "",
            "```powershell",
            "python empirical/collatz_gauge_holonomy.py "
            f"--max-word-length {settings['max_word_length']} "
            f"--two-bits {settings['two_bits']} "
            f"--three-depth {settings['three_depth']} "
            f"--cycle-sieve-json {settings['cycle_sieve_json']}",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def default_report_path(max_word_length: int, two_bits: int, three_depth: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_gauge_holonomy_L{max_word_length}_2p{two_bits}_3p{three_depth}.md"
    )


def default_json_path(max_word_length: int, two_bits: int, three_depth: int) -> Path:
    return (
        Path("empirical/reports")
        / f"collatz_gauge_holonomy_L{max_word_length}_2p{two_bits}_3p{three_depth}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-word-length", type=int, default=8)
    parser.add_argument("--two-bits", type=int, default=4)
    parser.add_argument("--three-depth", type=int, default=4)
    parser.add_argument("--sample-limit", type=int, default=2)
    parser.add_argument(
        "--cycle-sieve-json",
        type=Path,
        default=Path("empirical/reports/collatz_cycle_sieve_L12_S24_K8.json"),
    )
    parser.add_argument("--sieve-row-limit", type=int, default=8)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_word_length < 1:
        raise ValueError("--max-word-length must be at least 1")
    if args.two_bits < 1:
        raise ValueError("--two-bits must be at least 1")
    if args.three_depth < 1:
        raise ValueError("--three-depth must be at least 1")

    audits = audit_words(
        max_word_length=args.max_word_length,
        two_bits=args.two_bits,
        three_depth=args.three_depth,
        sample_limit=args.sample_limit,
    )
    base_modulus = (1 << args.two_bits) * (3**args.three_depth)
    payload = {
        "settings": {
            "max_word_length": args.max_word_length,
            "two_bits": args.two_bits,
            "three_depth": args.three_depth,
            "base_modulus": base_modulus,
            "cycle_sieve_json": str(args.cycle_sieve_json),
            "sieve_row_limit": args.sieve_row_limit,
        },
        "verification": verification_summary(audits),
        "groups": group_audits(audits),
        "examples": choose_example_audits(audits),
        "cycle_holonomy": cycle_holonomy_records(),
        "sieve_comparison": load_sieve_comparison(
            args.cycle_sieve_json,
            args.sieve_row_limit,
        ),
        "audits": audits,
    }

    report_path = args.report or default_report_path(
        args.max_word_length,
        args.two_bits,
        args.three_depth,
    )
    json_path = args.json or default_json_path(
        args.max_word_length,
        args.two_bits,
        args.three_depth,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["verification"]), indent=2))


if __name__ == "__main__":
    main()
