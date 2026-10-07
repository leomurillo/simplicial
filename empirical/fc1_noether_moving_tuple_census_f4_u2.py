"""Selected moving-coordinate tuple census for FC1 on F4[u]/(u^2).

This is the first non-aggregate stabilizer/determinant test after the small
24-coordinate orbit-bucket baseline.  It splits one carry-pair orbit of size
12 into its individual normalizer-moving coordinates and keeps four fixed
macro/residual coordinates:

    E_u, E_u^2, H4-visible residual bucket, remaining-invisible residual bucket.

The tuple size is still Q-2 = 14 for |F4[u]/(u^2)| = 16.  The resulting
finite skeleton has 16 coordinates and C(16,14)=120 supports, small enough to
enumerate exactly under all 24 Hayes-Frobenius normalizer actions.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
import math
from pathlib import Path
from typing import Any

from compute_f4_u2_ext_ch import ACTIONS, Label, NONTRIVIAL, label_name


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"
BASE_JSON = REPORTS / "fc1_noether_atlas_census_f4_u2.json"
EXT_JSON = REPORTS / "ext_ch_cocycle_f4_u2.json"
OUT_JSON = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_selected.json"
OUT_MD = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_selected.md"

ROW_KEY = "f4-u2"
HAMILTONIAN_COUNT = 14
FIXED_COORDINATES = (
    {"id": "PE:u", "kind": "packet_energy", "label": "E_u"},
    {"id": "PE:u^2", "kind": "packet_energy", "label": "E_u^2"},
    {
        "id": "VIS:h4_visible",
        "kind": "residual_visibility_bucket",
        "label": "H4_visible_incidence",
    },
    {
        "id": "VIS:remaining_invisible",
        "kind": "residual_visibility_bucket",
        "label": "remaining_invisible_after_H3_contraction",
    },
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def source_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def label_map() -> dict[str, Label]:
    return {label_name(label): label for label in NONTRIVIAL}


def parse_label(text: str) -> Label:
    labels = label_map()
    if text not in labels:
        raise KeyError(f"unknown F4[u]/u2 label text {text!r}")
    return labels[text]


def pair_key_from_json(row: dict[str, Any]) -> tuple[Label, Label, str, str, str]:
    rep = row["representative"]
    return (
        parse_label(rep["left_eta"]),
        parse_label(rep["right_eta"]),
        rep["source"],
        rep["middle"],
        rep["target"],
    )


def key_text(key: tuple[Label, Label, str, str, str]) -> str:
    left, right, source, middle, target = key
    return f"{label_name(left)}|{label_name(right)}|{source}->{middle}->{target}"


def transform_pair_key(
    key: tuple[Label, Label, str, str, str],
    action: dict[Label, Label],
) -> tuple[Label, Label, str, str, str]:
    left, right, source, middle, target = key
    return (action[left], action[right], source, middle, target)


def selected_pair_orbit(ext: dict[str, Any]) -> dict[str, Any]:
    size_12 = [
        (index, row)
        for index, row in enumerate(ext["canonical_pair_orbits"])
        if int(row["size"]) == 12
    ]
    if not size_12:
        raise ValueError("no size-12 carry-pair orbit found")

    # Prefer a mixed-boundary path so the selected moving coordinates touch
    # the tame/wild carry interface rather than only the pure tame control.
    for index, row in size_12:
        if row["path"] in {"u->u->u^2", "u^2->u->u"}:
            return {"source_index": index, **row}
    index, row = size_12[0]
    return {"source_index": index, **row}


def build_coordinates(
    selected: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[list[int]], list[dict[str, Any]]]:
    seed = pair_key_from_json(selected)
    orbit_keys = sorted(
        {transform_pair_key(seed, action) for action in ACTIONS},
        key=key_text,
    )
    key_to_index = {key: index + len(FIXED_COORDINATES) for index, key in enumerate(orbit_keys)}

    coordinates = [dict(coord, moving=False) for coord in FIXED_COORDINATES]
    for local_index, key in enumerate(orbit_keys):
        coordinates.append(
            {
                "id": f"M:{local_index}",
                "kind": "moving_carry_pair_coordinate",
                "label": key_text(key),
                "moving": True,
                "left_eta": label_name(key[0]),
                "right_eta": label_name(key[1]),
                "path": f"{key[2]}->{key[3]}->{key[4]}",
            }
        )

    permutations: list[list[int]] = []
    action_rows: list[dict[str, Any]] = []
    for action_index, action in enumerate(ACTIONS):
        perm = list(range(len(coordinates)))
        for key in orbit_keys:
            perm[key_to_index[key]] = key_to_index[transform_pair_key(key, action)]
        permutations.append(perm)
        moved = sum(1 for index, image in enumerate(perm) if image != index)
        action_rows.append({"action_index": action_index, "moved_coordinates": moved})
    return coordinates, permutations, action_rows


def mask_from_indices(indices: tuple[int, ...]) -> int:
    mask = 0
    for index in indices:
        mask |= 1 << index
    return mask


def indices_from_mask(mask: int) -> list[int]:
    return [index for index in range(mask.bit_length()) if mask & (1 << index)]


def transform_mask(mask: int, permutation: list[int]) -> int:
    out = 0
    bit = mask
    while bit:
        lsb = bit & -bit
        index = lsb.bit_length() - 1
        out |= 1 << permutation[index]
        bit ^= lsb
    return out


def permutation_sign(values: list[int]) -> int:
    inversions = 0
    for i, value in enumerate(values):
        for other in values[i + 1 :]:
            if value > other:
                inversions += 1
    return -1 if inversions % 2 else 1


def determinant_sign_for_stabilizer(
    mask: int,
    permutation: list[int],
) -> int:
    support = indices_from_mask(mask)
    position = {coord: index for index, coord in enumerate(support)}
    induced = [position[permutation[coord]] for coord in support]
    return permutation_sign(induced)


def support_summary(mask: int, coordinates: list[dict[str, Any]]) -> dict[str, Any]:
    support = indices_from_mask(mask)
    kind_counts = Counter(coordinates[index]["kind"] for index in support)
    fixed_ids = [coordinates[index]["id"] for index in support if not coordinates[index]["moving"]]
    moving_ids = [coordinates[index]["id"] for index in support if coordinates[index]["moving"]]
    return {
        "support_ids": [coordinates[index]["id"] for index in support],
        "kind_counts": dict(kind_counts),
        "fixed_ids": fixed_ids,
        "moving_count": len(moving_ids),
        "moving_ids_sample": moving_ids[:8],
    }


def build_report() -> dict[str, Any]:
    base = load_json(BASE_JSON)
    ext = load_json(EXT_JSON)
    selected = selected_pair_orbit(ext)
    coordinates, permutations, action_rows = build_coordinates(selected)

    coordinate_count = len(coordinates)
    all_masks = {
        mask_from_indices(indices)
        for indices in combinations(range(coordinate_count), HAMILTONIAN_COUNT)
    }
    unvisited = set(all_masks)
    orbit_rows: list[dict[str, Any]] = []

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
        determinant_distribution = Counter(determinant_values)
        orbit_rows.append(
            {
                "orbit_id": len(orbit_rows),
                "representative_mask": representative,
                "orbit_size": len(present_orbit),
                "stabilizer_order": len(stabilizer_actions),
                "stabilizer_action_indices": stabilizer_actions,
                "determinant_distribution": {
                    str(key): value for key, value in sorted(determinant_distribution.items())
                },
                "determinant_character": (
                    "trivial"
                    if set(determinant_values) == {1}
                    else "sign-nontrivial"
                ),
                "support_summary": support_summary(representative, coordinates),
            }
        )
        unvisited -= present_orbit

    orbit_size_distribution = Counter(row["orbit_size"] for row in orbit_rows)
    stabilizer_distribution = Counter(row["stabilizer_order"] for row in orbit_rows)
    determinant_character_distribution = Counter(
        row["determinant_character"] for row in orbit_rows
    )
    fixed_coverage_distribution = Counter(
        tuple(row["support_summary"]["fixed_ids"]) for row in orbit_rows
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

    add_check("coordinate count", coordinate_count, 16)
    add_check("selected moving orbit size", selected["size"], 12)
    add_check("tuple support count", len(all_masks), math.comb(16, 14))
    add_check(
        "orbit-stabilizer total",
        sum(row["orbit_size"] for row in orbit_rows),
        len(all_masks),
    )
    add_check(
        "orbit-stabilizer divisibility",
        all(row["orbit_size"] * row["stabilizer_order"] == len(ACTIONS) for row in orbit_rows),
        True,
    )
    add_check(
        "nontrivial moving-coordinate orbits exist",
        any(row["orbit_size"] > 1 for row in orbit_rows),
        True,
    )
    add_check(
        "nontrivial determinant character appears",
        determinant_character_distribution.get("sign-nontrivial", 0) > 0,
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
        "schema": "fc1_noether_moving_tuple_census_f4_u2_selected.v1",
        "row_key": ROW_KEY,
        "ring": base["ring"],
        "status": "selected moving-coordinate tuple census; one size-12 carry-pair orbit split",
        "certificate_pass": all(check["pass"] for check in checks),
        "sources": {
            "base_census": source_path(BASE_JSON),
            "ext_cocycle": source_path(EXT_JSON),
        },
        "scope": {
            "hamiltonian_tuple_size": HAMILTONIAN_COUNT,
            "coordinate_count": coordinate_count,
            "fixed_coordinates": len(FIXED_COORDINATES),
            "moving_coordinates": coordinate_count - len(FIXED_COORDINATES),
            "selected_pair_orbit": {
                "source_index": selected["source_index"],
                "size": selected["size"],
                "path": selected["path"],
                "representative": selected["representative"],
            },
            "not_claimed": [
                "all carry-pair orbits split",
                "all K_CH commutator orbit coordinates split",
                "full 637-coordinate tuple census",
                "coefficient-stratified Hamiltonian tuples",
            ],
        },
        "coordinate_summary": {
            "coordinates": coordinates,
            "action_rows": action_rows,
        },
        "tuple_census": {
            "support_count": len(all_masks),
            "normalizer_orbit_count": len(orbit_rows),
            "orbit_size_distribution": dict(sorted(orbit_size_distribution.items())),
            "stabilizer_order_distribution": dict(
                sorted(stabilizer_distribution.items())
            ),
            "determinant_character_distribution": dict(
                sorted(determinant_character_distribution.items())
            ),
            "fixed_coverage_distribution": {
                ",".join(key) if key else "(none)": value
                for key, value in sorted(
                    fixed_coverage_distribution.items(), key=lambda item: item[0]
                )
            },
            "orbits": orbit_rows,
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
                "split a full size-24 carry-pair orbit or selected K_CH "
                "commutator orbit representatives after this selected size-12 "
                "moving-coordinate determinant check"
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
        "# FC1 Noether Moving Tuple Census: F4[u]/(u^2) Selected Orbit",
        "",
        "This is the first non-aggregate tuple census.  It splits one",
        "normalizer-moving carry-pair orbit into individual coordinates and",
        "computes support orbits, stabilizers, and determinant signs exactly.",
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
        "",
        "## Tuple Census",
        "",
    ]
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
    lines.extend(["", "## Orbit Representatives", ""])
    lines.extend(
        md_table(
            [
                "orbit",
                "size",
                "stabilizer",
                "det",
                "fixed ids",
                "moving count",
            ],
            [
                [
                    row["orbit_id"],
                    row["orbit_size"],
                    row["stabilizer_order"],
                    row["determinant_character"],
                    ", ".join(row["support_summary"]["fixed_ids"]) or "(none)",
                    row["support_summary"]["moving_count"],
                ]
                for row in census["orbits"]
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Reading",
            "",
            "This is the first layer where determinant characters are not forced",
            "to be trivial by aggregate buckets.  The selected moving orbit already",
            "produces nontrivial sign characters on some tuple stabilizers.",
            "",
            "The next layer should split either a full size-24 carry-pair orbit or",
            "selected `K_CH` commutator representatives, while keeping the same",
            "support/full/H4/H3 residual distinctions.",
            "",
        ]
    )
    for label, path in payload["sources"].items():
        lines.append(f"- `{label}`: `{path}`")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    payload = build_report()
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(payload)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"certificate_pass={payload['certificate_pass']}")


if __name__ == "__main__":
    main()

