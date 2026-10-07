"""Full size-24 moving-coordinate tuple census for FC1 on F4[u]/(u^2).

This is the next nontrivial FC1 Noether-atlas layer after the selected
size-12 carry-pair split.  It splits one full size-24 carry-pair orbit into
individual normalizer-moving coordinates and keeps the same four fixed
macro/residual coordinates:

    E_u, E_u^2, H4-visible residual bucket, remaining-invisible residual bucket.

The tuple size is Q-2 = 14 for |F4[u]/(u^2)| = 16.  The resulting finite
skeleton has 28 coordinates and C(28,14)=40,116,600 supports.  The report
therefore records exact aggregate orbit/stabilizer/determinant distributions
with samples, rather than emitting millions of orbit representatives.
"""

from __future__ import annotations

from collections import Counter, defaultdict
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
    indices_from_mask,
    load_json,
    mask_from_indices,
    source_path,
    transform_mask,
)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"
OUT_JSON = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_size24.json"
OUT_MD = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_size24.md"


def selected_size24_pair_orbit(ext: dict[str, Any]) -> dict[str, Any]:
    """Choose a full orbit on the mixed carry interface."""

    size_24 = [
        (index, row)
        for index, row in enumerate(ext["canonical_pair_orbits"])
        if int(row["size"]) == 24
    ]
    if not size_24:
        raise ValueError("no size-24 carry-pair orbit found")

    for index, row in size_24:
        if row["path"] in {"u->u->u^2", "u^2->u->u"}:
            return {"source_index": index, **row}
    index, row = size_24[0]
    return {"source_index": index, **row}


def moving_permutations(permutations: list[list[int]]) -> list[list[int]]:
    fixed_count = len(FIXED_COORDINATES)
    out: list[list[int]] = []
    for permutation in permutations:
        out.append([image - fixed_count for image in permutation[fixed_count:]])
    return out


def transform_moving_mask(mask: int, permutation: list[int]) -> int:
    out = 0
    bit = mask
    while bit:
        lsb = bit & -bit
        index = lsb.bit_length() - 1
        out |= 1 << permutation[index]
        bit ^= lsb
    return out


def determinant_sign_for_moving_stabilizer(mask: int, permutation: list[int]) -> int:
    support = indices_from_mask(mask)
    position = {coord: index for index, coord in enumerate(support)}
    induced = [position[permutation[coord]] for coord in support]
    inversions = 0
    for i, value in enumerate(induced):
        for other in induced[i + 1 :]:
            if value > other:
                inversions += 1
    return -1 if inversions % 2 else 1


def cycle_lengths(permutation: list[int]) -> list[int]:
    seen = [False] * len(permutation)
    lengths: list[int] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        lengths.append(length)
    return sorted(lengths)


def fixed_subset_counts_by_size(permutation: list[int]) -> dict[int, int]:
    counts: Counter[int] = Counter({0: 1})
    for length in cycle_lengths(permutation):
        updated = Counter(counts)
        for size, count in counts.items():
            updated[size + length] += count
        counts = updated
    return dict(counts)


def moving_mask_from_combination(indices: tuple[int, ...]) -> int:
    mask = 0
    for index in indices:
        mask |= 1 << index
    return mask


def full_mask_from_parts(fixed_indices: tuple[int, ...], moving_mask: int) -> int:
    fixed_count = len(FIXED_COORDINATES)
    mask = mask_from_indices(fixed_indices)
    bit = moving_mask
    while bit:
        lsb = bit & -bit
        index = lsb.bit_length() - 1
        mask |= 1 << (fixed_count + index)
        bit ^= lsb
    return mask


def orbit_sample(
    *,
    moving_mask: int,
    fixed_indices: tuple[int, ...],
    moving_perms: list[list[int]],
    full_perms: list[list[int]],
    coordinates: list[dict[str, Any]],
) -> dict[str, Any]:
    full_mask = full_mask_from_parts(fixed_indices, moving_mask)
    stabilizer_actions = [
        index
        for index, permutation in enumerate(full_perms)
        if transform_mask(full_mask, permutation) == full_mask
    ]
    determinant_values = [
        determinant_sign_for_stabilizer(full_mask, full_perms[index])
        for index in stabilizer_actions
    ]
    moving_stabilizer_actions = [
        index
        for index, permutation in enumerate(moving_perms)
        if transform_moving_mask(moving_mask, permutation) == moving_mask
    ]
    if stabilizer_actions != moving_stabilizer_actions:
        raise AssertionError("fixed-coordinate stabilizer mismatch")

    support = indices_from_mask(full_mask)
    fixed_ids = [coordinates[index]["id"] for index in support if index < len(FIXED_COORDINATES)]
    moving_ids = [coordinates[index]["id"] for index in support if index >= len(FIXED_COORDINATES)]
    return {
        "fixed_ids": fixed_ids,
        "moving_count": len(moving_ids),
        "moving_ids_sample": moving_ids[:10],
        "stabilizer_order": len(stabilizer_actions),
        "stabilizer_action_indices": stabilizer_actions,
        "determinant_distribution": {
            str(key): value for key, value in sorted(Counter(determinant_values).items())
        },
        "determinant_character": (
            "trivial" if set(determinant_values) == {1} else "sign-nontrivial"
        ),
    }


def enumerate_moving_orbits(
    moving_perms: list[list[int]],
    *,
    moving_size: int,
) -> tuple[list[dict[str, Any]], dict[int, int]]:
    """Enumerate k-subset orbits of the 24 moving coordinates."""

    seen: set[int] = set()
    rows: list[dict[str, Any]] = []
    sample_reps_by_stabilizer: dict[int, int] = {}

    for indices in combinations(range(24), moving_size):
        mask = moving_mask_from_combination(indices)
        if mask in seen:
            continue
        orbit = {transform_moving_mask(mask, permutation) for permutation in moving_perms}
        representative = min(orbit)
        stabilizer_actions = [
            index
            for index, permutation in enumerate(moving_perms)
            if transform_moving_mask(representative, permutation) == representative
        ]
        determinant_values = [
            determinant_sign_for_moving_stabilizer(representative, moving_perms[index])
            for index in stabilizer_actions
        ]
        stabilizer_order = len(stabilizer_actions)
        rows.append(
            {
                "representative_mask": representative,
                "orbit_size": len(orbit),
                "stabilizer_order": stabilizer_order,
                "determinant_character": (
                    "trivial"
                    if set(determinant_values) == {1}
                    else "sign-nontrivial"
                ),
            }
        )
        sample_reps_by_stabilizer.setdefault(stabilizer_order, representative)
        seen.update(orbit)

    return rows, sample_reps_by_stabilizer


def build_report() -> dict[str, Any]:
    base = load_json(BASE_JSON)
    ext = load_json(EXT_JSON)
    selected = selected_size24_pair_orbit(ext)
    coordinates, permutations, action_rows = build_coordinates(selected)
    moving_perms = moving_permutations(permutations)
    coordinate_count = len(coordinates)

    fixed_count = len(FIXED_COORDINATES)
    fixed_subset_counts = {
        count: math.comb(fixed_count, count) for count in range(fixed_count + 1)
    }
    moving_sizes = range(HAMILTONIAN_COUNT - fixed_count, HAMILTONIAN_COUNT + 1)

    moving_rows_by_size: dict[int, list[dict[str, Any]]] = {}
    sample_reps_by_size: dict[int, dict[int, int]] = {}
    for moving_size in moving_sizes:
        rows, sample_reps = enumerate_moving_orbits(
            moving_perms,
            moving_size=moving_size,
        )
        moving_rows_by_size[moving_size] = rows
        sample_reps_by_size[moving_size] = sample_reps

    moving_burnside_by_size: dict[int, int] = {}
    for moving_size in moving_sizes:
        fixed_sum = 0
        for permutation in moving_perms:
            fixed_sum += fixed_subset_counts_by_size(permutation).get(moving_size, 0)
        if fixed_sum % len(ACTIONS):
            raise AssertionError("nonintegral Burnside count")
        moving_burnside_by_size[moving_size] = fixed_sum // len(ACTIONS)

    total_support_count = math.comb(coordinate_count, HAMILTONIAN_COUNT)
    total_orbit_count = 0
    orbit_stabilizer_total = 0
    total_orbit_size_distribution: Counter[int] = Counter()
    total_stabilizer_distribution: Counter[int] = Counter()
    total_determinant_distribution: Counter[str] = Counter()
    by_fixed_count: list[dict[str, Any]] = []
    sample_rows: list[dict[str, Any]] = []

    for fixed_used in range(fixed_count + 1):
        moving_size = HAMILTONIAN_COUNT - fixed_used
        fixed_multiplier = fixed_subset_counts[fixed_used]
        rows = moving_rows_by_size[moving_size]
        orbit_size_distribution: Counter[int] = Counter()
        stabilizer_distribution: Counter[int] = Counter()
        determinant_distribution: Counter[str] = Counter()
        support_count = fixed_multiplier * math.comb(24, moving_size)
        orbit_count = fixed_multiplier * len(rows)
        by_fixed_count.append(
            {
                "fixed_coordinate_count": fixed_used,
                "moving_coordinate_count": moving_size,
                "fixed_subset_choices": fixed_multiplier,
                "support_count": support_count,
                "moving_orbit_count": len(rows),
                "tuple_orbit_count": orbit_count,
            }
        )

        for row in rows:
            weighted_count = fixed_multiplier
            orbit_size = int(row["orbit_size"])
            stabilizer_order = int(row["stabilizer_order"])
            orbit_size_distribution[orbit_size] += weighted_count
            stabilizer_distribution[stabilizer_order] += weighted_count
            determinant_distribution[row["determinant_character"]] += weighted_count
            total_orbit_size_distribution[orbit_size] += weighted_count
            total_stabilizer_distribution[stabilizer_order] += weighted_count
            total_determinant_distribution[row["determinant_character"]] += weighted_count
            orbit_stabilizer_total += weighted_count * orbit_size

        total_orbit_count += orbit_count
        by_fixed_count[-1].update(
            {
                "orbit_size_distribution": dict(sorted(orbit_size_distribution.items())),
                "stabilizer_order_distribution": dict(
                    sorted(stabilizer_distribution.items())
                ),
                "determinant_character_distribution": dict(
                    sorted(determinant_distribution.items())
                ),
            }
        )

        for stabilizer_order, moving_mask in sorted(
            sample_reps_by_size[moving_size].items()
        ):
            fixed_indices = tuple(range(fixed_used))
            sample_rows.append(
                {
                    "fixed_coordinate_count": fixed_used,
                    "moving_coordinate_count": moving_size,
                    **orbit_sample(
                        moving_mask=moving_mask,
                        fixed_indices=fixed_indices,
                        moving_perms=moving_perms,
                        full_perms=permutations,
                        coordinates=coordinates,
                    ),
                }
            )

    burnside_total = 0
    for permutation in moving_perms:
        moving_fixed_counts = fixed_subset_counts_by_size(permutation)
        burnside_total += sum(
            fixed_subset_counts[fixed_used]
            * moving_fixed_counts.get(HAMILTONIAN_COUNT - fixed_used, 0)
            for fixed_used in range(fixed_count + 1)
        )
    if burnside_total % len(ACTIONS):
        raise AssertionError("nonintegral full Burnside count")
    burnside_orbit_count = burnside_total // len(ACTIONS)

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

    add_check("coordinate count", coordinate_count, 28)
    add_check("selected moving orbit size", selected["size"], 24)
    add_check("tuple support count", total_support_count, math.comb(28, 14))
    add_check(
        "support partition by fixed-coordinate count",
        sum(row["support_count"] for row in by_fixed_count),
        total_support_count,
    )
    add_check(
        "moving orbit Burnside check",
        {
            str(size): len(moving_rows_by_size[size])
            for size in moving_sizes
        },
        {str(size): moving_burnside_by_size[size] for size in moving_sizes},
    )
    add_check("full tuple Burnside check", total_orbit_count, burnside_orbit_count)
    add_check("orbit-stabilizer total", orbit_stabilizer_total, total_support_count)
    add_check(
        "orbit-stabilizer divisibility",
        all(
            row["orbit_size"] * row["stabilizer_order"] == len(ACTIONS)
            for rows in moving_rows_by_size.values()
            for row in rows
        ),
        True,
    )
    add_check(
        "nontrivial determinant character appears",
        total_determinant_distribution.get("sign-nontrivial", 0) > 0,
        True,
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
        "schema": "fc1_noether_moving_tuple_census_f4_u2_size24.v1",
        "row_key": ROW_KEY,
        "ring": base["ring"],
        "status": "full size-24 carry-pair moving-coordinate tuple census",
        "certificate_pass": all(check["pass"] for check in checks),
        "sources": {
            "base_census": source_path(BASE_JSON),
            "ext_cocycle": source_path(EXT_JSON),
        },
        "selection_memo": {
            "ranking": [
                {
                    "candidate": "split one full size-24 carry-pair orbit",
                    "rank": 1,
                    "reason": (
                        "maximal FC1 dependency leverage among ready tasks: exact "
                        "moving-coordinate tuple stabilizers/determinant characters "
                        "without treating K_CH as an Ext detector or claiming FC3"
                    ),
                },
                {
                    "candidate": "split selected K_CH commutator representatives",
                    "rank": 2,
                    "reason": (
                        "useful next FC1 layer, but higher overclaim risk because "
                        "K_CH must remain only a Fisher-jet shadow of [kappa]"
                    ),
                },
                {
                    "candidate": "draft bounded FC3 information-investment theorem",
                    "rank": 3,
                    "reason": (
                        "central but premature until the FC1 tuple atlas has more "
                        "non-aggregate stabilizer/determinant data"
                    ),
                },
            ],
            "picked": "split one full size-24 carry-pair orbit",
        },
        "scope": {
            "hamiltonian_tuple_size": HAMILTONIAN_COUNT,
            "coordinate_count": coordinate_count,
            "fixed_coordinates": fixed_count,
            "moving_coordinates": coordinate_count - fixed_count,
            "selected_pair_orbit": {
                "source_index": selected["source_index"],
                "size": selected["size"],
                "path": selected["path"],
                "representative": selected["representative"],
            },
            "not_claimed": [
                "all carry-pair orbits split simultaneously",
                "all K_CH commutator orbit coordinates split",
                "full 637-coordinate tuple census",
                "coefficient-stratified Hamiltonian tuples",
                "support residual 0 as full filtered closure",
                "K_CH as a standalone Ext_CH detector",
            ],
        },
        "coordinate_summary": {
            "coordinates": coordinates,
            "action_rows": action_rows,
        },
        "tuple_census": {
            "support_count": total_support_count,
            "normalizer_orbit_count": total_orbit_count,
            "orbit_size_distribution": dict(sorted(total_orbit_size_distribution.items())),
            "stabilizer_order_distribution": dict(
                sorted(total_stabilizer_distribution.items())
            ),
            "determinant_character_distribution": dict(
                sorted(total_determinant_distribution.items())
            ),
            "by_fixed_coordinate_count": by_fixed_count,
            "sample_orbits": sample_rows[:24],
        },
        "residual_visibility_inherited": {
            "full_filtered_residual": base["row_summary"]["full_filtered_residual"],
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
        "count_checks": checks,
        "next_layer": {
            "needed": True,
            "recommended": (
                "split selected K_CH commutator representatives or add another "
                "carry-pair size-24 orbit, while retaining full/support/H4/H3 "
                "residual fields as separate costs"
            ),
        },
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
    scope = payload["scope"]
    census = payload["tuple_census"]
    residual = payload["residual_visibility_inherited"]
    selected = scope["selected_pair_orbit"]

    lines: list[str] = [
        "# FC1 Noether Moving Tuple Census: F4[u]/(u^2) Size-24 Orbit",
        "",
        "This is the next non-aggregate tuple census after the selected size-12",
        "split.  It splits one full size-24 carry-pair orbit into individual",
        "normalizer-moving coordinates and computes exact aggregate support",
        "orbits, stabilizers, and determinant signs.",
        "",
        "## Candidate Ranking",
        "",
    ]
    lines.extend(
        md_table(
            ["rank", "candidate", "reading"],
            [
                [row["rank"], row["candidate"], row["reason"]]
                for row in payload["selection_memo"]["ranking"]
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Scope",
            "",
            f"- row: `{payload['row_key']}`",
            f"- ring: `{payload['ring']}`",
            f"- status: `{payload['status']}`",
            f"- certificate pass: `{payload['certificate_pass']}`",
            f"- tuple size: `{scope['hamiltonian_tuple_size']}`",
            f"- coordinates: `{scope['coordinate_count']}`",
            f"- selected carry-pair path: `{selected['path']}`",
            f"- selected carry-pair source index: `{selected['source_index']}`",
            "- this is not the full 637-coordinate tuple census.",
            "- support residual `0` is not treated as full filtered closure.",
            "- `K_CH` remains only a Fisher-shadow channel of `[kappa]`.",
            "",
            "## Tuple Census",
            "",
        ]
    )
    lines.extend(
        md_table(
            ["field", "value"],
            [
                ["support count", census["support_count"]],
                ["normalizer orbit count", census["normalizer_orbit_count"]],
                ["orbit size distribution", dist_text(census["orbit_size_distribution"])],
                [
                    "stabilizer order distribution",
                    dist_text(census["stabilizer_order_distribution"]),
                ],
                [
                    "determinant character distribution",
                    dist_text(census["determinant_character_distribution"]),
                ],
            ],
        )
    )
    lines.extend(["", "## By Fixed Coordinates", ""])
    lines.extend(
        md_table(
            [
                "fixed",
                "moving",
                "support count",
                "tuple orbits",
                "stabilizers",
                "determinants",
            ],
            [
                [
                    row["fixed_coordinate_count"],
                    row["moving_coordinate_count"],
                    row["support_count"],
                    row["tuple_orbit_count"],
                    dist_text(row["stabilizer_order_distribution"]),
                    dist_text(row["determinant_character_distribution"]),
                ]
                for row in census["by_fixed_coordinate_count"]
            ],
        )
    )
    lines.extend(["", "## Residual Ledger Inherited From Base Certificate", ""])
    lines.extend(
        md_table(
            ["field", "value"],
            [
                ["full filtered residual", residual["full_filtered_residual"]],
                ["support projection residual", residual["support_projection_residual"]],
                ["H4-visible atoms", residual["h4_visible_atoms"]],
                [
                    "H3-contraction visible from H4-invisible",
                    residual["h3_contraction_visible_from_h4_invisible"],
                ],
                ["remaining invisible atoms", residual["remaining_invisible_atoms"]],
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
    lines.extend(["", "## Sample Orbit Types", ""])
    lines.extend(
        md_table(
            [
                "fixed",
                "moving",
                "stabilizer",
                "det",
                "fixed ids",
                "moving sample",
            ],
            [
                [
                    row["fixed_coordinate_count"],
                    row["moving_coordinate_count"],
                    row["stabilizer_order"],
                    row["determinant_character"],
                    ", ".join(row["fixed_ids"]) or "(none)",
                    ", ".join(row["moving_ids_sample"]),
                ]
                for row in census["sample_orbits"]
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Reading",
            "",
            "This layer gives the first full-orbit moving-coordinate tuple census.",
            "It supplies exact non-aggregate stabilizer and determinant-character",
            "metadata for a size-24 carry-pair orbit while preserving the FC1/FC2",
            "hygiene boundaries.  It is still a declared finite skeleton, not a",
            "classification of arbitrary smooth invariants or all decomposable",
            "current coefficient patterns.",
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
