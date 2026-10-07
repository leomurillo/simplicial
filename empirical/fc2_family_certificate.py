"""Finite-atlas certificate for the FC2 filtered curvature-carry family theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPORT_DIR = Path(__file__).with_name("reports")
FINITE_ROWS_JSON = REPORT_DIR / "finite_row_certificates.json"
FC2_ROW_JSON = REPORT_DIR / "fc2_curvature_carry_certificate.json"
DEFAULT_JSON = REPORT_DIR / "fc2_family_certificate.json"
DEFAULT_MD = REPORT_DIR / "fc2_family_certificate.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def row_certificate_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for cert in payload["certificates"]:
        ext = cert["ext_ch"]
        full = ext.get("full_block_coboundary") or {}
        support = ext.get("support_projection_coboundary") or {}
        h3 = cert.get("h3") or {}
        h4 = cert.get("h4") or {}
        rows.append(
            {
                "row_key": cert["row_key"],
                "ring": cert["ring"],
                "packets": cert["constructor"]["packets"],
                "h3_cells": h3.get("cells"),
                "h3_orbits": h3.get("orbits"),
                "h4_cells": h4.get("cells"),
                "h4_orbits": h4.get("orbits"),
                "raw_atoms": ext["raw_atom_count"],
                "raw_pairs": ext["raw_pair_count"],
                "pair_orbits": ext.get("pair_orbit_count"),
                "full_residual": full.get("residual_support"),
                "full_non_coboundary": full.get("raw_non_coboundary_over_q_certified")
                if "raw_non_coboundary_over_q_certified" in full
                else (False if full.get("raw_is_coboundary") else True),
                "support_residual": support.get("residual_support"),
                "support_is_coboundary": support.get("raw_is_coboundary"),
            }
        )
    return rows


def build_payload() -> dict[str, Any]:
    finite_rows = load_json(FINITE_ROWS_JSON)
    fc2_first = load_json(FC2_ROW_JSON)
    rows = row_certificate_rows(finite_rows)
    return {
        "claim": "FC2 filtered curvature-carry family theorem finite-atlas certificate",
        "theorem_scope": (
            "All finite local conductor-filtered quotient-character adjacency "
            "rows satisfying the section-extension hypotheses; visible support "
            "is computed after quotienting by the Fisher-jet kernel."
        ),
        "formal_source": "filtered section class [kappa] in the section-change complex",
        "formal_shadows": [
            "K_CH cubic Fisher commutator shadow",
            "higher arity hyper-adjacency/Fisher-jet support shadows",
        ],
        "first_mixed_row_shadow": {
            "ring": fc2_first["ring"],
            "commutator_orbits": fc2_first["arity4_curvature_shadow"][
                "arity_2_commutator_orbits"
            ],
            "lifted_commutator_orbits": fc2_first["arity4_curvature_shadow"][
                "lifted_arity_2_commutator_orbits"
            ],
            "mixed_h4_orbits_hit": fc2_first["arity4_curvature_shadow"][
                "mixed_h4_orbits_hit"
            ],
            "mixed_h4_orbits_total": fc2_first["arity4_curvature_shadow"][
                "mixed_h4_orbits_total"
            ],
            "pure_h4_orbits_hit": fc2_first["arity4_curvature_shadow"][
                "pure_h4_orbits_hit"
            ],
            "pure_h4_orbits_total": fc2_first["arity4_curvature_shadow"][
                "pure_h4_orbits_total"
            ],
        },
        "certified_rows": rows,
        "all_certified_rows_have_full_nonzero_residual": all(
            row["full_residual"] and row["full_residual"] > 0 for row in rows
        ),
        "support_projection_can_hide_full_carry": any(
            row["support_residual"] == 0 and row["full_residual"] and row["full_residual"] > 0
            for row in rows
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# FC2 Family Certificate",
        "",
        f"- theorem scope: {payload['theorem_scope']}",
        f"- formal source: {payload['formal_source']}",
        "- formal shadows: "
        + ", ".join(f"`{shadow}`" for shadow in payload["formal_shadows"]),
        f"- all certified rows have full nonzero residual: `{payload['all_certified_rows_have_full_nonzero_residual']}`",
        f"- support projection can hide full carry: `{payload['support_projection_can_hide_full_carry']}`",
        "",
        "## First Mixed Row Shadow",
        "",
    ]
    first = payload["first_mixed_row_shadow"]
    lines += [
        f"- ring: `{first['ring']}`",
        f"- commutator orbits lifted: `{first['lifted_commutator_orbits']} / {first['commutator_orbits']}`",
        f"- mixed H4 orbits hit: `{first['mixed_h4_orbits_hit']} / {first['mixed_h4_orbits_total']}`",
        f"- pure H4 orbits hit: `{first['pure_h4_orbits_hit']} / {first['pure_h4_orbits_total']}`",
        "",
        "## Certified Local Rows",
        "",
        "| row | ring | packets | H3 | H4 | raw atoms | raw pairs | pair orbits | full residual | support residual |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in payload["certified_rows"]:
        packets = ", ".join(f"{key}:{value}" for key, value in row["packets"].items())
        lines.append(
            "| "
            + " | ".join(
                [
                    row["row_key"],
                    row["ring"],
                    packets,
                    f"{row['h3_cells']}/{row['h3_orbits']}",
                    f"{row['h4_cells']}/{row['h4_orbits']}",
                    str(row["raw_atoms"]),
                    str(row["raw_pairs"]),
                    str(row["pair_orbits"]),
                    str(row["full_residual"]),
                    "n/a" if row["support_residual"] is None else str(row["support_residual"]),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Reading",
        "",
        "The family theorem is formal: the source of curvature-carry is the",
        "filtered section class `[kappa]`, and visible curvature/carry supports",
        "are its Fisher-jet images.  The table certifies nonzero full filtered",
        "carry on the current finite local atlas.  Rows with support residual",
        "`0` show why support closure alone is not the theorem.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    payload = build_payload()
    DEFAULT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    DEFAULT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(render_markdown(payload))
    print(f"Wrote {DEFAULT_JSON}")
    print(f"Wrote {DEFAULT_MD}")


if __name__ == "__main__":
    main()
