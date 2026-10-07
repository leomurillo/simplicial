"""Final bounded FC1 Noether-atlas certificate for F4[u]/(u^2).

The analytic FC1 theorem is proved in the knowledge-base notes.  This script
emits the exact finite certificate layer that demonstrates the theorem on the
first mixed local row under the declared bounded atlas scope.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"

BASE_JSON = REPORTS / "fc1_noether_atlas_census_f4_u2.json"
SMALL_JSON = REPORTS / "fc1_noether_tuple_census_f4_u2_small.json"
SELECTED_JSON = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_selected.json"
SIZE24_JSON = REPORTS / "fc1_noether_moving_tuple_census_f4_u2_size24.json"
CARRY_PAIR_JSON = REPORTS / "fc1_noether_carry_pair_atlas_f4_u2.json"
OUT_JSON = REPORTS / "fc1_noether_atlas_certificate_f4_u2.json"
OUT_MD = REPORTS / "fc1_noether_atlas_certificate_f4_u2.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def source_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def md_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(item) for item in row) + " |")
    return lines


def build_report() -> dict[str, Any]:
    base = load_json(BASE_JSON)
    small = load_json(SMALL_JSON)
    selected = load_json(SELECTED_JSON)
    size24 = load_json(SIZE24_JSON)
    carry_pair = load_json(CARRY_PAIR_JSON)

    residual_tuple = [
        base["row_summary"]["full_filtered_residual"],
        base["row_summary"]["support_projection_residual"],
    ]
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

    add_check(
        "component certificates pass",
        {
            "base": base["certificate_pass"],
            "aggregate_tuple": small["certificate_pass"],
            "selected_size12": selected["certificate_pass"],
            "size24": size24["certificate_pass"],
            "carry_pair_atlas": carry_pair["certificate_pass"],
        },
        {
            "base": True,
            "aggregate_tuple": True,
            "selected_size12": True,
            "size24": True,
            "carry_pair_atlas": True,
        },
    )
    add_check("seed coordinate count", base["row_summary"]["seed_coordinate_count"], 637)
    add_check(
        "aggregate tuple support count",
        small["tuple_census"]["tuple_support_total"],
        1961256,
    )
    add_check(
        "selected size-12 moving chart orbits",
        selected["tuple_census"]["normalizer_orbit_count"],
        15,
    )
    add_check(
        "size-24 moving chart support/orbits",
        [
            size24["tuple_census"]["support_count"],
            size24["tuple_census"]["normalizer_orbit_count"],
        ],
        [40116600, 1674272],
    )
    add_check(
        "carry-pair atlas assessed/capable/companion",
        [
            carry_pair["scope"]["canonical_carry_pair_orbits"],
            carry_pair["scope"]["tuple_capable_one_split_charts"],
            carry_pair["scope"]["requires_companion_coordinates"],
        ],
        [20, 18, 2],
    )
    add_check(
        "support/full residual kept separate",
        residual_tuple,
        [1569, 0],
    )
    add_check(
        "residual visibility partition",
        base["row_summary"]["h4_visible_atoms"]
        + base["row_summary"]["h3_contraction_visible_from_h4_invisible"]
        + base["row_summary"]["remaining_invisible_atoms"],
        base["row_summary"]["full_filtered_residual"],
    )

    return {
        "schema": "fc1_noether_atlas_certificate_f4_u2.v1",
        "row_key": "f4-u2",
        "ring": base["ring"],
        "status": "bounded FC1 Noether-atlas certificate delivered",
        "certificate_pass": all(check["pass"] for check in checks),
        "analytic_status": {
            "fc1_a": "proved at centroid finite-sufficient quadratic jet scope",
            "fc1_b1": "proved for fixed finite-jet exact decomposable currents",
            "fc1_c": "proved for fixed finite-jet off-centroid closure defects",
            "certificate_role": (
                "exact finite demonstration/computer-assisted certificate, "
                "not empirical neural evidence"
            ),
        },
        "bounded_atlas_scope": {
            "row": "F4[u]/(u^2)",
            "tuple_size": 14,
            "seed_coordinates": base["row_summary"]["seed_coordinate_count"],
            "delivered_layers": [
                "orbit skeleton base certificate",
                "aggregate 24-coordinate tuple baseline",
                "selected size-12 moving carry-pair chart",
                "full size-24 moving carry-pair chart",
                "all canonical carry-pair one-split charts assessed",
            ],
            "not_claimed": [
                "simultaneous C(637,14) tuple enumeration",
                "all K_CH commutator coordinates split",
                "arbitrary smooth invariant functions",
                "all Fisher-volume-preserving currents",
                "global sufficiency beyond the declared finite skeleton",
            ],
        },
        "delivered_layer_summary": {
            "base_seed_coordinates": base["row_summary"]["seed_coordinate_count"],
            "base_k_ch_commutator_orbits": base["row_summary"][
                "k_ch_commutator_orbits"
            ],
            "base_carry_pair_orbits": base["row_summary"]["carry_pair_orbits"],
            "aggregate_tuple_supports": small["tuple_census"][
                "tuple_support_total"
            ],
            "aggregate_determinants": "trivial baseline",
            "selected_size12_orbits": selected["tuple_census"][
                "normalizer_orbit_count"
            ],
            "selected_size12_sign_nontrivial": selected["tuple_census"][
                "determinant_character_distribution"
            ].get("sign-nontrivial"),
            "size24_supports": size24["tuple_census"]["support_count"],
            "size24_orbits": size24["tuple_census"]["normalizer_orbit_count"],
            "size24_sign_nontrivial": size24["tuple_census"][
                "determinant_character_distribution"
            ].get("sign-nontrivial"),
            "carry_pair_charts": carry_pair["summary"]["status_distribution"],
            "carry_pair_chart_orbits_not_simultaneous": carry_pair["summary"][
                "chart_orbit_count_total_not_simultaneous"
            ],
        },
        "tuple_level_residual_label": {
            "kappa_source": "FC2 filtered section class [kappa]",
            "support_projection_residual": base["row_summary"][
                "support_projection_residual"
            ],
            "full_filtered_residual": base["row_summary"][
                "full_filtered_residual"
            ],
            "h4_visible_atoms": base["row_summary"]["h4_visible_atoms"],
            "h3_contraction_visible_from_h4_invisible": base["row_summary"][
                "h3_contraction_visible_from_h4_invisible"
            ],
            "remaining_invisible_atoms": base["row_summary"][
                "remaining_invisible_atoms"
            ],
            "interpretation": [
                "support residual 0 is not full filtered closure",
                "K_CH/H4/H3 are visibility channels modulo kernels",
                "tuple labels are relative to the declared finite skeleton",
            ],
        },
        "sources": {
            "base_census": source_path(BASE_JSON),
            "aggregate_tuple": source_path(SMALL_JSON),
            "selected_size12": source_path(SELECTED_JSON),
            "size24": source_path(SIZE24_JSON),
            "carry_pair_atlas": source_path(CARRY_PAIR_JSON),
            "fc1_theorem_note": "knowledge_base/fc1_natural_macrovariable_theorem.md",
            "fc1_census_target": "knowledge_base/fc1_noether_atlas_census_target.md",
        },
        "count_checks": checks,
    }


def write_markdown(payload: dict[str, Any]) -> None:
    analytic = payload["analytic_status"]
    scope = payload["bounded_atlas_scope"]
    layers = payload["delivered_layer_summary"]
    residual = payload["tuple_level_residual_label"]

    lines: list[str] = [
        "# FC1 Noether Atlas Certificate: F4[u]/(u^2)",
        "",
        "This is the bounded FC1 Noether-atlas delivery certificate for the",
        "first mixed local row.  The analytic theorem is recorded in the FC1",
        "knowledge-base notes; this artifact is the exact finite demonstration",
        "layer for the declared atlas scope.",
        "",
        "## Analytic Status",
        "",
    ]
    lines.extend(
        md_table(
            ["piece", "status"],
            [
                ["FC1-A", analytic["fc1_a"]],
                ["FC1-B1", analytic["fc1_b1"]],
                ["FC1-C", analytic["fc1_c"]],
                ["certificate role", analytic["certificate_role"]],
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Delivered Scope",
            "",
            f"- row: `{payload['row_key']}`",
            f"- ring: `{payload['ring']}`",
            f"- status: `{payload['status']}`",
            f"- certificate pass: `{payload['certificate_pass']}`",
            f"- tuple size: `{scope['tuple_size']}`",
            f"- seed coordinates: `{scope['seed_coordinates']}`",
            "- this is a bounded finite atlas certificate, not the simultaneous `C(637,14)` atlas.",
            "",
            "## Layer Summary",
            "",
        ]
    )
    lines.extend(
        md_table(
            ["layer", "value"],
            [
                ["base seed coordinates", layers["base_seed_coordinates"]],
                ["base K_CH commutator orbits", layers["base_k_ch_commutator_orbits"]],
                ["base carry-pair orbits", layers["base_carry_pair_orbits"]],
                ["aggregate tuple supports", layers["aggregate_tuple_supports"]],
                ["aggregate determinants", layers["aggregate_determinants"]],
                ["selected size-12 orbits", layers["selected_size12_orbits"]],
                [
                    "selected size-12 sign-nontrivial",
                    layers["selected_size12_sign_nontrivial"],
                ],
                ["size-24 supports", layers["size24_supports"]],
                ["size-24 orbits", layers["size24_orbits"]],
                ["size-24 sign-nontrivial", layers["size24_sign_nontrivial"]],
                ["carry-pair charts", json.dumps(layers["carry_pair_charts"], sort_keys=True)],
                [
                    "carry-pair chart orbits, not simultaneous",
                    layers["carry_pair_chart_orbits_not_simultaneous"],
                ],
            ],
        )
    )
    lines.extend(["", "## Tuple-Level Residual Label", ""])
    lines.extend(
        md_table(
            ["field", "value"],
            [
                ["source", residual["kappa_source"]],
                ["support projection residual", residual["support_projection_residual"]],
                ["full filtered residual", residual["full_filtered_residual"]],
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
    lines.extend(
        [
            "",
            "## Non-Claims",
            "",
        ]
    )
    for item in scope["not_claimed"]:
        lines.append(f"- {item}")
    lines.extend(["", "## Sources", ""])
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
