"""Closure-deficit audit for the second half of the Collatz program.

Papers 11 and 12 warn that support-level closure is not enough: a
macrovariable can look closed in the associated graded while leaking filtered
carry data in the full adjacency algebra.  For Collatz, the support-level
object is the no-descent carry language

    S_j <= floor(j log2(3)).

This script compares that visible language with the finite 2-adic residue
packets it actually occupies.  It also stress-checks positive odd integers
below finite bounds, because the infinite no-descent language is nonempty in
the 2-adics even when it may contain no positive integer.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 expects a positive integer")
    return (value & -value).bit_length() - 1


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


def project_states_to_residues(
    states: set[tuple[int, int]],
    length: int,
    bits: int,
) -> set[int]:
    """Project exact no-descent cylinders to odd residues modulo 2^bits.

    A prefix with total carry S determines the initial odd integer modulo
    2^(S+1).  If S+1 is below the requested bit depth, the cylinder expands
    to all compatible residues modulo 2^bits.
    """

    modulus = 1 << bits
    residues: set[int] = set()
    three_power = pow(3, length, modulus)
    full_inverse = pow(three_power, -1, modulus)

    for total_depth, cocycle_mod in states:
        exact_bits = total_depth + 1
        if exact_bits >= bits:
            residue = (((1 << total_depth) % modulus - cocycle_mod) * full_inverse) % modulus
            residues.add(residue)
            continue

        exact_modulus = 1 << exact_bits
        exact_inverse = pow(pow(3, length, exact_modulus), -1, exact_modulus)
        exact_residue = (
            ((1 << total_depth) % exact_modulus - cocycle_mod % exact_modulus)
            * exact_inverse
        ) % exact_modulus
        for lift in range(1 << (bits - exact_bits)):
            residues.add(exact_residue + lift * exact_modulus)

    return {residue for residue in residues if residue & 1}


def residue_stats(residues: set[int], bits: int) -> dict[str, Any]:
    modulus = 1 << bits
    odd_capacity = 1 << (bits - 1)
    if not residues:
        return {
            "odd_residue_count": 0,
            "residue_density": 0.0,
            "residue_deficit": 1.0,
            "negative_half_fraction": 0.0,
            "mean_v2_n_plus_1": 0.0,
            "max_v2_n_plus_1": 0,
            "contains_minus_one": False,
        }

    def clipped_v2_n_plus_1(residue: int) -> int:
        value = (residue + 1) % modulus
        return bits if value == 0 else v2(value)

    count = len(residues)
    negative_half = sum(1 for residue in residues if residue >= modulus // 2)
    valuations = [clipped_v2_n_plus_1(residue) for residue in residues]
    density = count / odd_capacity
    return {
        "odd_residue_count": count,
        "residue_density": density,
        "residue_deficit": 1.0 - density,
        "negative_half_fraction": negative_half / count,
        "mean_v2_n_plus_1": sum(valuations) / count,
        "max_v2_n_plus_1": max(valuations),
        "contains_minus_one": (modulus - 1) in residues,
    }


def projection_audit(max_length: int, bits: int) -> dict[str, Any]:
    modulus = 1 << bits
    states: set[tuple[int, int]] = {(0, 0)}
    rows: list[dict[str, Any]] = []
    residue_history: list[set[int]] = []

    for length in range(1, max_length + 1):
        cap = math.floor(length * LOG2_3)
        next_states: set[tuple[int, int]] = set()
        for total_depth, cocycle_mod in states:
            max_carry = cap - total_depth
            for carry in range(1, max_carry + 1):
                next_depth = total_depth + carry
                next_cocycle = (3 * cocycle_mod + (1 << total_depth)) % modulus
                next_states.add((next_depth, next_cocycle))
        states = next_states

        depths = {total_depth for total_depth, _cocycle in states}
        residues = project_states_to_residues(states, length, bits)
        residue_history.append(residues)
        stats = residue_stats(residues, bits)
        rows.append(
            {
                "length": length,
                "height_cap": cap,
                "support_depth_count": len(depths),
                "full_state_count": len(states),
                "state_density_per_depth": len(states) / (max(1, len(depths)) * modulus),
                **stats,
            }
        )

    final_residues = residue_history[-1] if residue_history else set()
    stable_from = max_length
    for index in range(len(residue_history) - 1, -1, -1):
        if residue_history[index] != final_residues:
            break
        stable_from = index + 1

    return {
        "bits": bits,
        "modulus": modulus,
        "stable_from_through_max": stable_from,
        "final": rows[-1],
        "selected_rows": [
            rows[length - 1] for length in selected_lengths(max_length)
        ],
        "final_residue_sample": sorted(final_residues)[:32],
        "final_residue_tail_sample": sorted(final_residues)[-32:],
    }


def no_descent_prefix_result(n: int, max_length: int) -> dict[str, Any]:
    total_depth = 0
    current = n
    for length in range(1, max_length + 1):
        next_value = 3 * current + 1
        carry = v2(next_value)
        total_depth += carry
        current = next_value >> carry
        cap = math.floor(length * LOG2_3)
        if total_depth > cap:
            return {
                "survives": False,
                "survived_prefixes": length - 1,
                "failure_length": length,
                "failure_total_depth": total_depth,
                "failure_cap": cap,
                "next_odd_after_failure": current,
            }
    return {
        "survives": True,
        "survived_prefixes": max_length,
        "failure_length": None,
        "failure_total_depth": total_depth,
        "failure_cap": math.floor(max_length * LOG2_3),
        "next_odd_after_failure": current,
    }


def positive_integer_audit(max_length: int, bits_values: list[int]) -> list[dict[str, Any]]:
    rows = []
    for bits in bits_values:
        upper = 1 << bits
        survivors: list[int] = []
        best_witness: dict[str, Any] | None = None
        tested = 0
        for n in range(3, upper, 2):
            tested += 1
            result = no_descent_prefix_result(n, max_length)
            if result["survives"]:
                survivors.append(n)
            if (
                best_witness is None
                or result["survived_prefixes"] > best_witness["survived_prefixes"]
            ):
                best_witness = {"n": n, **result}
        rows.append(
            {
                "bits": bits,
                "upper_bound_exclusive": upper,
                "positive_odd_tested_excluding_1": tested,
                "survivors_after_max_length": len(survivors),
                "survivor_sample": survivors[:16],
                "best_witness": best_witness,
            }
        )
    return rows


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


def make_projection_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| bits | stable from | final states | depths | residues | residue density | residue deficit | max v2(n+1) | contains -1 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        final = row["final"]
        lines.append(
            f"| {row['bits']} | {row['stable_from_through_max']} | "
            f"{final['full_state_count']} | {final['support_depth_count']} | "
            f"{final['odd_residue_count']} | {final['residue_density']:.6f} | "
            f"{final['residue_deficit']:.6f} | {final['max_v2_n_plus_1']} | "
            f"{final['contains_minus_one']} |"
        )
    return lines


def make_selected_table(audit: dict[str, Any]) -> list[str]:
    lines = [
        f"| m | states mod 2^{audit['bits']} | depths | residues | density | mean v2(n+1) |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in audit["selected_rows"]:
        lines.append(
            f"| {row['length']} | {row['full_state_count']} | "
            f"{row['support_depth_count']} | {row['odd_residue_count']} | "
            f"{row['residue_density']:.6f} | {row['mean_v2_n_plus_1']:.6f} |"
        )
    return lines


def make_positive_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| bits | odds tested | survivors to M | best n | survived prefixes | failure length | failure S/cap |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        witness = row["best_witness"] or {}
        lines.append(
            f"| {row['bits']} | {row['positive_odd_tested_excluding_1']} | "
            f"{row['survivors_after_max_length']} | {witness.get('n')} | "
            f"{witness.get('survived_prefixes')} | {witness.get('failure_length')} | "
            f"{witness.get('failure_total_depth')}/{witness.get('failure_cap')} |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    largest_projection = payload["projection_audits"][-1]
    lines = [
        "# Collatz Closure-Deficit Ledger",
        "",
        "## Meaning",
        "",
        "Papers 11 and 12 say that support closure is not enough: the visible conductor macrovariable can close while the full filtered adjacency algebra still carries hidden data.  This is the Collatz version of that audit.",
        "",
        "The visible macrovariable is the no-descent support language:",
        "",
        "```text",
        "S_j <= floor(j log2(3)) for every prefix j.",
        "```",
        "",
        "The filtered data is the exact 2-adic residue packet of the initial odd integer.  At finite depth this report projects those packets modulo `2^B` and compares them with the support-only language.",
        "",
        "## Projection Audit",
        "",
        *make_projection_table(payload["projection_audits"]),
        "",
        f"Selected rows for the largest quotient, `2^{largest_projection['bits']}`:",
        "",
        *make_selected_table(largest_projection),
        "",
        "## Positive Integer Stress",
        "",
        f"Directly tested positive odd integers below `2^B`, excluding the fixed point `1`, against the no-descent condition through `{settings['max_length']}` accelerated odd steps.",
        "",
        *make_positive_table(payload["positive_integer_audit"]),
        "",
        "## Interpretation",
        "",
        "This is the blindspot made concrete.  The support language remains alive and the finite residue projections stabilize to nonempty 2-adic survivor sets, including the all-ones class `-1`.  But bounded positive integers disappear in the direct stress test.  So the second-half theorem is not a mass/counting theorem; it is a closure theorem separating the inverse-limit 2-adic survivor set from the embedded positive odd integers.",
        "",
        "The next theorem target should therefore be:",
        "",
        "```text",
        "The infinite no-descent residue inverse limit contains no positive odd integer.",
        "```",
        "",
        "In the papers' language: height support is the associated graded; exact residue packets are the filtered block; the missing proof is that support-level closure does not lift to a positive-integer full-block path.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_closure_deficit_ledger.py "
        f"--max-length {settings['max_length']} "
        f"--projection-bits {' '.join(str(bit) for bit in settings['projection_bits'])} "
        f"--positive-bits {' '.join(str(bit) for bit in settings['positive_bits'])}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, max_bits: int) -> Path:
    return Path("empirical/reports") / f"collatz_closure_deficit_L{max_length}_B{max_bits}.md"


def default_json_path(max_length: int, max_bits: int) -> Path:
    return Path("empirical/reports") / f"collatz_closure_deficit_L{max_length}_B{max_bits}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=120)
    parser.add_argument("--projection-bits", type=int, nargs="+", default=[8, 10, 12, 14])
    parser.add_argument("--positive-bits", type=int, nargs="+", default=[8, 10, 12, 14, 16, 18, 20])
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if any(bit < 2 for bit in args.projection_bits + args.positive_bits):
        raise ValueError("bit depths must be at least 2")

    projection_bits = sorted(set(args.projection_bits))
    positive_bits = sorted(set(args.positive_bits))
    projection_audits = [
        projection_audit(args.max_length, bits) for bits in projection_bits
    ]
    positive_rows = positive_integer_audit(args.max_length, positive_bits)
    payload = {
        "settings": {
            "max_length": args.max_length,
            "projection_bits": projection_bits,
            "positive_bits": positive_bits,
        },
        "projection_audits": projection_audits,
        "positive_integer_audit": positive_rows,
    }

    max_bits = max(projection_bits)
    report_path = args.report or default_report_path(args.max_length, max_bits)
    json_path = args.json or default_json_path(args.max_length, max_bits)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded({
        "projection_final": [audit["final"] for audit in projection_audits],
        "positive_integer_audit": positive_rows,
    }), indent=2))


if __name__ == "__main__":
    main()
