"""Bounded carry-pair one-split atlas for FC1 on F4[u]/(u^2).

This script closes the first declared FC1 Noether-atlas delivery layer after
the base skeleton, aggregate tuple baseline, and selected moving-coordinate
charts.  It assesses every canonical carry-pair orbit in the F4[u]/(u^2)
row.  For each orbit that can form a 14-Hamiltonian tuple together with the
four fixed macro/residual coordinates, it computes exact support-orbit,
stabilizer, determinant-character, and residual-label distributions.

The delivered object is bounded on purpose:

    one carry-pair orbit split at a time
    four fixed macro/residual coordinates
    tuple size Q-2 = 14

It is not the simultaneous 637-coordinate tuple atlas.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import math
from pathlib import Path
from typing import Any

from compute_f4_u2_ext_ch import ACTIONS
from fc1_noether_moving_tuple_census_f4_u2 import (
    BASE_JSON,
    EXT_JSON,
    FIXED_COORDINATES,
    HAMILTONIAN_COUNT,
    ROW_KEY,
    build_coordinates,
    determinant_sign_for_stabilizer,
    load_json,
    mask_from_indices,
    source_path,
    support_summary,
    transform_mask,
)
from fc1_noether_moving_tuple_census_f4_u2_size24 import (
    cycle_lengths,
    moving_permutations,
)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"
OUT_JSON = REPORTS / "fc1_noether_carry_pair_atlas_f4_u2.json"
OUT_MD = REPORTS / "fc1_noether_carry_pair_atlas_f4_u2.md"
SIZE24_JSON = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_size24.json"


def counter_dict(counter: Counter[Any]) -> dict[str, int]:
    return {str(key): value for key, value in sorted(counter.items())}


def canonical_pair_with_index(index: int, row: dict[str, Any]) -> dict[str, Any]:
    return {"source_index": index, **row}


def permutation_cycle_profile(permutations: list[list[int]]) -> dict[str, int]:
    profile: Counter[str] = Counter()
    for permutation in permutations:
        profile[",".join(str(length) for length in cycle_lengths(permutation))] += 1
    return dict(sorted(profile.items()))


def direct_one_split_census(
    selected: dict[str, Any],
) -> dict[str, Any]:
    coordinates, permutations, _action_rows = build_coordinates(selected)
    coordinate_count = len(coordinates)
    all_masks = {
        mask_from_indices(indices)
        for indices in combinations(range(coordinate_count), HAMILTONIAN_COUNT)
    }
    unvisited = set(all_masks)
    orbit_size_distribution: Counter[int] = Counter()
    stabilizer_distribution: Counter[int] = Counter()
    determinant_distribution: Counter[str] = Counter()
    fixed_coverage_distribution: Counter[str] = Counter()
    sample_orbits: list[dict[str, Any]] = []

    while unvisited:
        seed = min(unvisited)
        orbit = {transform_mask(seed, permutation) for permutation in permutations}
        present_orbit = orbit & all_masks
        representative = min(present_orbit)
        stabilizer_actions = [
            index
            for index, permutation in enumerate(permutations)
            if transform_mask(representative, permutation) == representative
        ]
        determinant_values = [
            determinant_sign_for_stabilizer(representative, permutations[index])
            for index in stabilizer_actions
        ]
        summary = support_summary(representative, coordinates)
        determinant_character = (
            "trivial" if set(determinant_values) == {1} else "sign-nontrivial"
        )
        orbit_size_distribution[len(present_orbit)] += 1
        stabilizer_distribution[len(stabilizer_actions)] += 1
        determinant_distribution[determinant_character] += 1
        fixed_coverage_distribution[",".join(summary["fixed_ids"]) or "(none)"] += 1
        if len(sample_orbits) < 12:
            sample_orbits.append(
                {
                    "orbit_size": len(present_orbit),
                    "stabilizer_order": len(stabilizer_actions),
                    "determinant_character": determinant_character,
                    "support_summary": summary,
                }
            )
        unvisited -= present_orbit

    return {
        "status": "enumerated",
        "coordinate_count": coordinate_count,
        "support_count": len(all_masks),
        "normalizer_orbit_count": sum(orbit_size_distribution.values()),
        "orbit_size_distribution": counter_dict(orbit_size_distribution),
        "stabilizer_order_distribution": counter_dict(stabilizer_distribution),
        "determinant_character_distribution": counter_dict(determinant_distribution),
        "fixed_coverage_distribution": dict(sorted(fixed_coverage_distribution.items())),
        "sample_orbits": sample_orbits,
    }


def size24_profile_for_pair(
    selected: dict[str, Any],
    *,
    reference_profile: dict[str, Any],
    reference_cycle_profile: dict[str, int],
) -> dict[str, Any]:
    coordinates, permutations, _action_rows = build_coordinates(selected)
    cycle_profile = permutation_cycle_profile(moving_permutations(permutations))
    verified_regular_profile = cycle_profile == reference_cycle_profile
    census = reference_profile["tuple_census"]
    return {
        "status": "enumerated_by_regular_size24_profile",
        "coordinate_count": len(coordinates),
        "support_count": census["support_count"],
        "normalizer_orbit_count": census["normalizer_orbit_count"],
        "orbit_size_distribution": census["orbit_size_distribution"],
        "stabilizer_order_distribution": census["stabilizer_order_distribution"],
        "determinant_character_distribution": census[
            "determinant_character_distribution"
        ],
        "by_fixed_coordinate_count": census["by_fixed_coordinate_count"],
        "cycle_profile": cycle_profile,
        "regular_profile_verified": verified_regular_profile,
        "profile_source": source_path(
            REPORTS / "fc1_noether_moving_tuple_census_f4_u2_size24.json"
        ),
    }


def tuple_label(selected: dict[str, Any], base: dict[str, Any]) -> dict[str, Any]:
    row = base["row_summary"]
    return {
        "closure_defect_label": f"filtered_carry_pair_path:{selected['path']}",
        "kappa_source": "FC2 filtered section class [kappa]",
        "support_projection_residual": row["support_projection_residual"],
        "full_filtered_residual": row["full_filtered_residual"],
        "h4_visible_atoms": row["h4_visible_atoms"],
        "h3_contraction_visible_from_h4_invisible": row[
            "h3_contraction_visible_from_h4_invisible"
        ],
        "remaining_invisible_atoms": row["remaining_invisible_atoms"],
        "hygiene": [
            "support residual 0 is not full filtered closure",
            "K_CH is a Fisher-shadow channel, not a standalone Ext_CH detector",
            "quotient sufficiency is relative to the declared finite skeleton",
        ],
    }


def build_report() -> dict[str, Any]:
    base = load_json(BASE_JSON)
    ext = load_json(EXT_JSON)
    reference_size24 = load_json(SIZE24_JSON)
    reference_selected = reference_size24["scope"]["selected_pair_orbit"]
    ref_coordinates, ref_permutations, _rows = build_coordinates(reference_selected)
    _ = ref_coordinates
    reference_cycle_profile = permutation_cycle_profile(
        moving_permutations(ref_permutations)
    )

    orbit_rows: list[dict[str, Any]] = []
    status_distribution: Counter[str] = Counter()
    determinant_distribution: Counter[str] = Counter()
    support_chart_total = 0
    orbit_chart_total = 0
    tuple_capable_count = 0
    too_small_count = 0

    for index, row in enumerate(ext["canonical_pair_orbits"]):
        selected = canonical_pair_with_index(index, row)
        moving_size = int(selected["size"])
        coordinate_count = moving_size + len(FIXED_COORDINATES)
        if coordinate_count < HAMILTONIAN_COUNT:
            chart = {
                "status": "requires_companion_coordinates",
                "coordinate_count": coordinate_count,
                "support_count": 0,
                "normalizer_orbit_count": 0,
                "reason": (
                    "moving orbit plus four fixed macro/residual coordinates "
                    f"has only {coordinate_count} coordinates, below tuple size "
                    f"{HAMILTONIAN_COUNT}"
                ),
            }
            too_small_count += 1
        elif moving_size == 24:
            chart = size24_profile_for_pair(
                selected,
                reference_profile=reference_size24,
                reference_cycle_profile=reference_cycle_profile,
            )
            tuple_capable_count += 1
        else:
            chart = direct_one_split_census(selected)
            tuple_capable_count += 1

        status_distribution[chart["status"]] += 1
        support_chart_total += int(chart.get("support_count", 0))
        orbit_chart_total += int(chart.get("normalizer_orbit_count", 0))
        for key, count in chart.get("determinant_character_distribution", {}).items():
            determinant_distribution[key] += int(count)

        orbit_rows.append(
            {
                "source_index": index,
                "path": selected["path"],
                "size": moving_size,
                "representative": selected["representative"],
                "tuple_label": tuple_label(selected, base),
                **chart,
            }
        )

    checks: list[dict[str, Any]] = []

    def add_check(name: str, observed: Any, expected: Any, note: str = "") -> None:
        checks.append(
            {
                "name": name,
                "observed": observed,
                "expected": expected,
                "pass": observed == expected,
                "note": note,
            }
        )

    add_check("canonical carry-pair orbit count", len(orbit_rows), 20)
    add_check(
        "carry-pair orbit-size sum",
        sum(int(row["size"]) for row in orbit_rows),
        int(ext["raw_pair_count"]),
    )
    add_check(
        "tuple-capable one-split chart count",
        tuple_capable_count,
        sum(1 for row in ext["canonical_pair_orbits"] if int(row["size"]) + 4 >= 14),
    )
    add_check(
        "too-small chart count",
        too_small_count,
        sum(1 for row in ext["canonical_pair_orbits"] if int(row["size"]) + 4 < 14),
    )
    add_check(
        "all size-24 regular profiles verified",
        all(
            row.get("regular_profile_verified", True)
            for row in orbit_rows
            if int(row["size"]) == 24
        ),
        True,
    )
    add_check(
        "size-12 direct support counts",
        [
            row["support_count"]
            for row in orbit_rows
            if int(row["size"]) == 12 and row["status"] == "enumerated"
        ],
        [math.comb(16, 14)] * 6,
    )
    add_check(
        "support/full residual inherited separately",
        [
            base["row_summary"]["full_filtered_residual"],
            base["row_summary"]["support_projection_residual"],
        ],
        [1569, 0],
    )

    return {
        "schema": "fc1_noether_carry_pair_atlas_f4_u2.v1",
        "row_key": ROW_KEY,
        "ring": base["ring"],
        "status": "bounded one-split carry-pair Noether atlas certificate",
        "certificate_pass": all(check["pass"] for check in checks),
        "sources": {
            "base_census": source_path(BASE_JSON),
            "ext_cocycle": source_path(EXT_JSON),
            "size24_profile": source_path(
                SIZE24_JSON
            ),
        },
        "scope": {
            "hamiltonian_tuple_size": HAMILTONIAN_COUNT,
            "fixed_coordinates": len(FIXED_COORDINATES),
            "canonical_carry_pair_orbits": len(orbit_rows),
            "tuple_capable_one_split_charts": tuple_capable_count,
            "requires_companion_coordinates": too_small_count,
            "not_claimed": [
                "simultaneous split of all carry-pair orbits",
                "all K_CH commutator orbit coordinates split",
                "full 637-coordinate tuple census",
                "arbitrary smooth invariant functions",
                "all Fisher-volume-preserving currents",
            ],
        },
        "summary": {
            "status_distribution": counter_dict(status_distribution),
            "chart_support_count_total_not_simultaneous": support_chart_total,
            "chart_orbit_count_total_not_simultaneous": orbit_chart_total,
            "determinant_character_distribution_across_charts_not_simultaneous": counter_dict(
                determinant_distribution
            ),
            "full_filtered_residual": base["row_summary"][
                "full_filtered_residual"
            ],
            "support_projection_residual": base["row_summary"][
                "support_projection_residual"
            ],
            "h4_visible_atoms": base["row_summary"]["h4_visible_atoms"],
            "h3_contraction_visible_from_h4_invisible": base["row_summary"][
                "h3_contraction_visible_from_h4_invisible"
            ],
            "remaining_invisible_atoms": base["row_summary"][
                "remaining_invisible_atoms"
            ],
        },
        "orbit_charts": orbit_rows,
        "count_checks": checks,
        "delivery_statement": (
            "This finishes the bounded carry-pair one-split atlas layer for "
            "F4[u]/(u^2).  It complements the analytic FC1 theorem with exact "
            "finite charts; it does not claim the simultaneous 637-coordinate "
            "atlas."
        ),
    }


def md_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return lines


def dist_text(mapping: dict[str, Any]) -> str:
    return ", ".join(f"{key}:{value}" for key, value in mapping.items())


def write_markdown(payload: dict[str, Any]) -> None:
    summary = payload["summary"]
    lines: list[str] = [
        "# FC1 Noether Carry-Pair Atlas: F4[u]/(u^2)",
        "",
        "This is the bounded carry-pair one-split atlas certificate.  It",
        "assesses every canonical carry-pair orbit and enumerates the exact",
        "tuple charts whenever that one moving orbit plus the four fixed",
        "macro/residual coordinates can support a 14-Hamiltonian tuple.",
        "",
        "## Scope",
        "",
        f"- row: `{payload['row_key']}`",
        f"- ring: `{payload['ring']}`",
        f"- status: `{payload['status']}`",
        f"- certificate pass: `{payload['certificate_pass']}`",
        f"- tuple size: `{payload['scope']['hamiltonian_tuple_size']}`",
        f"- fixed coordinates per chart: `{payload['scope']['fixed_coordinates']}`",
        f"- canonical carry-pair orbits assessed: `{payload['scope']['canonical_carry_pair_orbits']}`",
        f"- tuple-capable one-split charts: `{payload['scope']['tuple_capable_one_split_charts']}`",
        f"- charts requiring companion coordinates: `{payload['scope']['requires_companion_coordinates']}`",
        "- this is not the simultaneous 637-coordinate tuple atlas.",
        "- support residual `0` is not full filtered closure.",
        "- `K_CH` is not used as a standalone `Ext_CH` detector.",
        "",
        "## Summary",
        "",
    ]
    lines.extend(
        md_table(
            ["field", "value"],
            [
                ["status distribution", dist_text(summary["status_distribution"])],
                [
                    "chart support total, not simultaneous",
                    summary["chart_support_count_total_not_simultaneous"],
                ],
                [
                    "chart orbit total, not simultaneous",
                    summary["chart_orbit_count_total_not_simultaneous"],
                ],
                [
                    "determinants across charts, not simultaneous",
                    dist_text(
                        summary[
                            "determinant_character_distribution_across_charts_not_simultaneous"
                        ]
                    ),
                ],
                ["full filtered residual", summary["full_filtered_residual"]],
                ["support projection residual", summary["support_projection_residual"]],
                ["H4-visible atoms", summary["h4_visible_atoms"]],
                [
                    "H3-contraction visible from H4-invisible",
                    summary["h3_contraction_visible_from_h4_invisible"],
                ],
                ["remaining invisible atoms", summary["remaining_invisible_atoms"]],
            ],
        )
    )
    lines.extend(["", "## Orbit Charts", ""])
    lines.extend(
        md_table(
            [
                "index",
                "path",
                "size",
                "status",
                "supports",
                "orbits",
                "stabilizers",
                "determinants",
            ],
            [
                [
                    row["source_index"],
                    row["path"],
                    row["size"],
                    row["status"],
                    row.get("support_count", 0),
                    row.get("normalizer_orbit_count", 0),
                    dist_text(row.get("stabilizer_order_distribution", {})),
                    dist_text(row.get("determinant_character_distribution", {})),
                ]
                for row in payload["orbit_charts"]
            ],
        )
    )
    lines.extend(["", "## Count Checks", ""])
    lines.extend(
        md_table(
            ["check", "observed", "expected", "pass"],
            [
                [
                    check["name"],
                    json.dumps(check["observed"], sort_keys=True),
                    json.dumps(check["expected"], sort_keys=True),
                    check["pass"],
                ]
                for check in payload["count_checks"]
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Reading",
            "",
            payload["delivery_statement"],
            "",
            "Each enumerated chart carries the same tuple-level residual label:",
            "the FC2 filtered section class `[kappa]` is the source, support",
            "projection residual is `0`, full filtered residual is `1569`,",
            "H4-visible mass is `72`, H3-contraction-visible mass is `1470`,",
            "and `27` atoms remain invisible to the tested H4/H3 channels.",
            "",
            "The two tiny carry-pair orbits of sizes `3` and `6` are not omitted;",
            "they are marked as requiring companion coordinates because the",
            "declared one-split chart has fewer than 14 coordinates.",
            "",
        ]
    )
    for label, path in payload["sources"].items():
        lines.append(f"- `{label}`: `{path}`")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    payload = build_report()
    OUT_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"certificate_pass={payload['certificate_pass']}")


if __name__ == "__main__":
    main()
