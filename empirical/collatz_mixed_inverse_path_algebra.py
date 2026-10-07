"""Mixed 2/3 filtered inverse path algebra for Collatz.

The support inverse tree has two formal branches

    D(x) = 2x,
    U(x) = (x - 1) / 3.

Every binary word is defined in Z[1/3].  Honest inverse-Collatz paths are
much thinner:

* 3-adic closure: U may land in Z only when the current integer is 1 mod 3.
* 2-adic parity closure: U is an odd preimage only when the current integer
  is 4 mod 6.

The finite quotient algebra makes the mixed filtration visible.  At modulus
M = 2^a 3^b, D is a single-valued operator on residues.  U is not closed as
a same-level operator: to compute (x - 1) / 3 modulo M, the source must be
known modulo 3M.  Thus U is naturally a filtered arrow

    R/(2^a 3^(b+1))  ->  R/(2^a 3^b).

This script records both the path counts and the quotient-adjacency closure
deficit.  It also records the natural Z/3 gauge: choosing one of the three
source lifts modulo 3M.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass
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
class PathState:
    numerator: int
    denominator_exponent: int
    integer_path: bool
    honest_path: bool


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
    denominator = 3**denominator_exponent
    if numerator % denominator:
        return None
    return numerator // denominator


def state_integer_value(state: PathState) -> int | None:
    return exact_integer_value(state.numerator, state.denominator_exponent)


def selected_lengths(max_length: int) -> list[int]:
    candidates = [1, 2, 3, 4, 5, 8, 10, 12, 14, 16, 18, 20, 24]
    out = [length for length in candidates if length <= max_length]
    if max_length not in out:
        out.append(max_length)
    return sorted(set(out))


def transition_states(
    states: list[PathState],
    powers3: list[int],
) -> tuple[list[PathState], dict[str, int]]:
    next_states: list[PathState] = []
    gates: Counter[str] = Counter()

    for state in states:
        parent_value = state_integer_value(state)
        parent_is_integer = parent_value is not None

        # D(x) = 2x. This is always a support arrow. If the parent path is
        # honest, D is an honest even-preimage arrow.
        d_state = PathState(
            numerator=2 * state.numerator,
            denominator_exponent=state.denominator_exponent,
            integer_path=state.integer_path and parent_is_integer,
            honest_path=state.honest_path,
        )
        next_states.append(d_state)
        gates["D_support"] += 1
        if parent_is_integer:
            gates["D_from_integer"] += 1
        if state.honest_path:
            gates["D_honest"] += 1

        # U(x) = (x - 1) / 3. This is always a support arrow in Z[1/3],
        # but it is an integer arrow only at x = 1 mod 3 and an honest odd
        # inverse-Collatz arrow only at x = 4 mod 6.
        denominator = powers3[state.denominator_exponent]
        u_numerator = state.numerator - denominator
        u_exponent = state.denominator_exponent + 1
        u_defect = reduced_denominator_exponent(u_numerator, u_exponent)
        u_is_integer = u_defect == 0

        gates["U_support"] += 1
        if parent_is_integer:
            gates["U_from_integer"] += 1
            if parent_value % 3 == 1:
                gates["U_3adic_pass"] += 1
            else:
                gates["U_3adic_fail"] += 1
            if parent_value % 6 == 4:
                gates["U_honest_pass"] += 1
            elif parent_value % 3 == 1:
                gates["U_parity_fail"] += 1
        else:
            gates["U_from_noninteger"] += 1

        u_state = PathState(
            numerator=u_numerator,
            denominator_exponent=u_exponent,
            integer_path=state.integer_path and u_is_integer,
            honest_path=state.honest_path and parent_is_integer and parent_value % 6 == 4,
        )
        next_states.append(u_state)

    return next_states, dict(gates)


def residue_counter(values: list[int], modulus: int) -> dict[str, int]:
    counts = Counter(value % modulus for value in values)
    return {str(key): counts[key] for key in sorted(counts)}


def endpoint_row(
    states: list[PathState],
    length: int,
    gates: dict[str, int],
) -> dict[str, Any]:
    denominator_defects: Counter[int] = Counter()
    integer_values: list[int] = []
    honest_values: list[int] = []
    integer_path_count = 0
    honest_path_count = 0

    for state in states:
        defect = reduced_denominator_exponent(
            state.numerator,
            state.denominator_exponent,
        )
        denominator_defects[defect] += 1
        value = state_integer_value(state)
        if value is not None:
            integer_values.append(value)
        if state.integer_path:
            integer_path_count += 1
        if state.honest_path:
            honest_path_count += 1
            honest_value = state_integer_value(state)
            if honest_value is None:
                raise AssertionError("honest path left the integers")
            honest_values.append(honest_value)

    total = len(states)
    integer_endpoint_count = len(integer_values)
    if integer_endpoint_count != integer_path_count:
        raise AssertionError("integer endpoint returned after denominator defect")
    return {
        "length": length,
        "support_words": total,
        "integer_words": integer_path_count,
        "integer_density": integer_path_count / total,
        "honest_inverse_words": honest_path_count,
        "honest_density": honest_path_count / total,
        "integer_but_not_honest": integer_path_count - honest_path_count,
        "distinct_integer_endpoints": len(set(integer_values)),
        "distinct_honest_endpoints": len(set(honest_values)),
        "integer_residue_mod6": residue_counter(integer_values, 6),
        "honest_residue_mod6": residue_counter(honest_values, 6),
        "top_denominator_defects": [
            {"defect": defect, "count": count}
            for defect, count in denominator_defects.most_common(8)
        ],
        "edge_gates": gates,
    }


def path_audit(seed: int, max_length: int) -> dict[str, Any]:
    powers3 = [1]
    for _index in range(max_length + 2):
        powers3.append(powers3[-1] * 3)

    states = [PathState(seed, 0, True, True)]
    rows: list[dict[str, Any]] = []
    selected = set(selected_lengths(max_length))
    selected_rows: list[dict[str, Any]] = []
    final_honest_values: list[int] = []

    for length in range(1, max_length + 1):
        states, gates = transition_states(states, powers3)
        row = endpoint_row(states, length, gates)
        rows.append(row)
        if length in selected:
            selected_rows.append(row)

    for state in states:
        if state.honest_path:
            value = state_integer_value(state)
            if value is not None:
                final_honest_values.append(value)

    return {
        "seed": seed,
        "max_length": max_length,
        "selected_rows": selected_rows,
        "final": rows[-1],
        "final_honest_endpoint_sample": sorted(set(final_honest_values))[:40],
        "final_honest_endpoint_tail_sample": sorted(set(final_honest_values))[-40:],
    }


def quotient_adjacency(two_bits: int, three_depth: int) -> dict[str, Any]:
    if two_bits < 1 or three_depth < 1:
        raise ValueError("two_bits and three_depth must both be at least 1")

    modulus = (1 << two_bits) * (3**three_depth)
    refined_source_modulus = 3 * modulus
    d_targets = {(2 * residue) % modulus for residue in range(modulus)}

    u_rows: list[dict[str, Any]] = []
    gauge_rows: list[dict[str, Any]] = []
    target_widths: Counter[int] = Counter()
    full_u_arrows = 0
    target_union: set[int] = set()
    legal_source_count = 0
    gauge_shift = modulus // 3

    for residue in range(modulus):
        targets: set[int] = set()
        gauge_targets: list[int | None] = []
        legal_lifts = 0
        for lift in range(3):
            refined_residue = residue + lift * modulus
            if refined_residue % 6 != 4:
                gauge_targets.append(None)
                continue
            legal_lifts += 1
            target = ((refined_residue - 1) // 3) % modulus
            targets.add(target)
            gauge_targets.append(target)

        if legal_lifts:
            legal_source_count += 1
            full_u_arrows += legal_lifts
            target_union.update(targets)
            target_widths[len(targets)] += 1
            if len(u_rows) < 12:
                u_rows.append(
                    {
                        "source_residue": residue,
                        "legal_lifts": legal_lifts,
                        "target_residues": sorted(targets),
                    }
                )
            if len(gauge_rows) < 12:
                gauge_rows.append(
                    {
                        "source_residue": residue,
                        "gauge_0_target": gauge_targets[0],
                        "gauge_1_target": gauge_targets[1],
                        "gauge_2_target": gauge_targets[2],
                        "target_orbit_mod_gauge": min(targets) % gauge_shift,
                    }
                )

    refined_legal_sources = [
        residue for residue in range(refined_source_modulus) if residue % 6 == 4
    ]
    refined_targets = {
        ((residue - 1) // 3) % modulus for residue in refined_legal_sources
    }
    same_level_closed = all(width <= 1 for width in target_widths)

    return {
        "two_bits": two_bits,
        "three_depth": three_depth,
        "modulus": modulus,
        "refined_source_modulus": refined_source_modulus,
        "vertex_count": modulus,
        "D": {
            "support_arrows": modulus,
            "target_count": len(d_targets),
            "target_reading": "even residues modulo M",
        },
        "U": {
            "coarse_legal_source_count": legal_source_count,
            "coarse_support_arrows": legal_source_count,
            "full_lift_arrows": full_u_arrows,
            "target_count": len(target_union),
            "target_reading": "odd residues modulo M",
            "target_width_distribution": {
                str(width): target_widths[width] for width in sorted(target_widths)
            },
            "same_level_closed_as_function": same_level_closed,
            "closure_deficit": 0.0
            if full_u_arrows == 0
            else 1.0 - legal_source_count / full_u_arrows,
            "sample_multivalued_sources": u_rows,
            "gauge": {
                "gauge_group": "Z/3",
                "section_lifts": [0, 1, 2],
                "target_shift_between_adjacent_sections": gauge_shift,
                "target_orbit_modulus": gauge_shift,
                "gauge_orbit_count": legal_source_count,
                "gauge_reduced_target_count": len({target % gauge_shift for target in target_union}),
                "gauge_reduced_closure_deficit": 0.0,
                "section_change_rule": "U_{t+delta}(r) = U_t(r) + delta*M/3 mod M",
                "sample_section_targets": gauge_rows,
            },
            "refined_source_legal_count": len(refined_legal_sources),
            "refined_target_count": len(refined_targets),
            "refined_arrow_is_function_to_coarse_target": True,
        },
    }


def verify_cycles() -> list[dict[str, Any]]:
    records = []
    for cycle in CYCLES_ALL_Z:
        image = tuple(collatz_step(n) for n in cycle)
        records.append(
            {
                "cycle": list(cycle),
                "length": len(cycle),
                "verified": image == cycle[1:] + cycle[:1],
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


def make_path_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| L | support words | integer words | honest words | integer density | honest density | distinct honest endpoints |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['length']} | {row['support_words']} | "
            f"{row['integer_words']} | {row['honest_inverse_words']} | "
            f"{row['integer_density']:.12f} | {row['honest_density']:.12f} | "
            f"{row['distinct_honest_endpoints']} |"
        )
    return lines


def make_gate_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| L | U from integer | U 3-adic pass | U parity fail | U honest pass | U from noninteger |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        gates = row["edge_gates"]
        lines.append(
            f"| {row['length']} | {gates.get('U_from_integer', 0)} | "
            f"{gates.get('U_3adic_pass', 0)} | "
            f"{gates.get('U_parity_fail', 0)} | "
            f"{gates.get('U_honest_pass', 0)} | "
            f"{gates.get('U_from_noninteger', 0)} |"
        )
    return lines


def make_quotient_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| 2^a | 3^b | M | U sources | U full lift arrows | U target width | closure deficit | U targets |",
        "|---:|---:|---:|---:|---:|---|---:|---:|",
    ]
    for row in rows:
        u = row["U"]
        widths = ", ".join(
            f"{width}:{count}"
            for width, count in u["target_width_distribution"].items()
        )
        lines.append(
            f"| {row['two_bits']} | {row['three_depth']} | {row['modulus']} | "
            f"{u['coarse_legal_source_count']} | {u['full_lift_arrows']} | "
            f"{widths} | {u['closure_deficit']:.6f} | {u['target_count']} |"
        )
    return lines


def make_gauge_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| M | gauge group | target shift | gauge orbits | gauge-reduced targets | gauge-reduced deficit |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        gauge = row["U"]["gauge"]
        lines.append(
            f"| {row['modulus']} | {gauge['gauge_group']} | "
            f"{gauge['target_shift_between_adjacent_sections']} | "
            f"{gauge['gauge_orbit_count']} | "
            f"{gauge['gauge_reduced_target_count']} | "
            f"{gauge['gauge_reduced_closure_deficit']:.6f} |"
        )
    return lines


def make_gauge_sample_table(row: dict[str, Any]) -> list[str]:
    lines = [
        f"| source mod {row['modulus']} | gauge 0 | gauge 1 | gauge 2 | orbit mod {row['U']['gauge']['target_orbit_modulus']} |",
        "|---:|---:|---:|---:|---:|",
    ]
    for sample in row["U"]["gauge"]["sample_section_targets"]:
        lines.append(
            f"| {sample['source_residue']} | {sample['gauge_0_target']} | "
            f"{sample['gauge_1_target']} | {sample['gauge_2_target']} | "
            f"{sample['target_orbit_mod_gauge']} |"
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
    path = payload["path_audit"]
    final = path["final"]
    lines = [
        "# Collatz Mixed 2/3 Inverse Path Algebra",
        "",
        "## Meaning",
        "",
        "This is the flipped object.  Binary support paths are cheap because both formal branches are defined in `Z[1/3]`.  Honest integer inverse paths require two filters at every `U` branch:",
        "",
        "```text",
        "3-adic: x = 1 mod 3 so (x - 1)/3 is an integer.",
        "2-adic: x = 4 mod 6 so that integer is odd.",
        "```",
        "",
        "Thus the algebra is mixed: `D` is a 2-adic even-preimage lift, while `U` is a 3-adic filtered division with a 2-adic parity gate.",
        "",
        "## Path Ledger",
        "",
        f"- seed: `{path['seed']}`",
        f"- max length: `{path['max_length']}`",
        f"- final support words: `{final['support_words']}`",
        f"- final integer words: `{final['integer_words']}`",
        f"- final honest inverse words: `{final['honest_inverse_words']}`",
        f"- final honest density: `{final['honest_density']:.12f}`",
        "",
        *make_path_table(path["selected_rows"]),
        "",
        "## U-Branch Gate Ledger",
        "",
        "The `U` branch is where the mixed closure lives.  `U 3-adic pass` counts integer parents with `x = 1 mod 3`; `U honest pass` is the stricter `x = 4 mod 6`; `U parity fail` is the integer-but-not-Collatz branch.",
        "",
        *make_gate_table(path["selected_rows"]),
        "",
        "## Finite Quotient Adjacency",
        "",
        "At `M = 2^a 3^b`, `D` is same-level and single-valued.  `U` is not: a source residue modulo `M` has three lifts modulo `3M`, and those lifts can land in three different target residues modulo `M`.  The filtered closed arrow is `R/(3M) -> R/M`.",
        "",
        *make_quotient_table(payload["quotient_audits"]),
        "",
        "## Gauge Sections",
        "",
        "A gauge is a section choice for the filtered `U` source lift.  For a legal coarse source `r mod M`, the three lifts `r`, `r+M`, and `r+2M` give targets separated by `M/3`.  Choosing one lift turns `U` into a deterministic representative; changing the section adds the constant `Z/3` phase.",
        "",
        *make_gauge_table(payload["quotient_audits"]),
        "",
        "Sample section targets for the largest quotient audit:",
        "",
        *make_gauge_sample_table(payload["quotient_audits"][-1]),
        "",
        "## Integer Cycles In All Z",
        "",
        "These are the calibration components for the global integer dynamics.",
        "",
        *make_cycle_table(payload["cycles_all_z"]),
        "",
        "## Interpretation",
        "",
        "This is the paper-style closure deficit in Collatz clothing.  If we keep only binary support, every word exists.  If we keep `Z[1/3]`, most words acquire a 3-denominator defect.  If we keep integers, many remaining words are still parity-wrong.  If we keep honest inverse-Collatz paths, the tree is governed by a filtered quotient algebra where `U` consumes one extra 3-adic digit and checks one 2-adic parity bit.",
        "",
        "The next theorem candidate becomes:",
        "",
        "```text",
        "In the mixed inverse path algebra, every infinite honest integer path",
        "is contained in the inverse basin of one of the five integer cycles;",
        "all other binary support paths acquire a finite 3-adic denominator",
        "defect or a 2-adic parity defect.",
        "```",
        "",
        "This is stronger and cleaner than a purely 2-adic no-descent statement: it makes the missing prime part of the state space.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/collatz_mixed_inverse_path_algebra.py "
        f"--seed {path['seed']} --max-length {settings['max_length']} "
        f"--quotient-pairs {' '.join(settings['quotient_pair_args'])}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int, seed: int) -> Path:
    return Path("empirical/reports") / f"collatz_mixed_inverse_path_seed_{seed}_L{max_length}.md"


def default_json_path(max_length: int, seed: int) -> Path:
    return Path("empirical/reports") / f"collatz_mixed_inverse_path_seed_{seed}_L{max_length}.json"


def parse_quotient_pairs(raw_pairs: list[str]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    for raw in raw_pairs:
        if "," in raw:
            left, right = raw.split(",", 1)
        elif ":" in raw:
            left, right = raw.split(":", 1)
        else:
            raise ValueError(f"quotient pair must be a,b or a:b, got {raw!r}")
        pairs.append((int(left), int(right)))
    return pairs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--max-length", type=int, default=20)
    parser.add_argument(
        "--quotient-pairs",
        nargs="+",
        default=["1:1", "2:1", "3:2", "4:3", "5:3"],
        help="pairs a,b for moduli 2^a 3^b",
    )
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_length > 24:
        raise ValueError("max length above 24 enumerates too many support words")

    quotient_pairs = parse_quotient_pairs(args.quotient_pairs)
    path = path_audit(args.seed, args.max_length)
    quotient_audits = [
        quotient_adjacency(two_bits, three_depth)
        for two_bits, three_depth in quotient_pairs
    ]
    payload = {
        "settings": {
            "max_length": args.max_length,
            "quotient_pairs": quotient_pairs,
            "quotient_pair_args": args.quotient_pairs,
        },
        "path_audit": path,
        "quotient_audits": quotient_audits,
        "cycles_all_z": verify_cycles(),
    }

    report_path = args.report or default_report_path(args.max_length, args.seed)
    json_path = args.json or default_json_path(args.max_length, args.seed)
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
                    "path_final": path["final"],
                    "quotient_U": [
                        {
                            "two_bits": row["two_bits"],
                            "three_depth": row["three_depth"],
                            "modulus": row["modulus"],
                            "closure_deficit": row["U"]["closure_deficit"],
                            "gauge": row["U"]["gauge"],
                        }
                        for row in quotient_audits
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
