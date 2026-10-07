"""FC2 curvature-carry certificate for the first mixed local row.

This script packages the exact finite evidence behind the theorem-facing
version of FC2:

  R = F_4[u]/(u^2)

The certificate deliberately separates three facts:

1. the binary filtered carry is a nontrivial section 2-cocycle;
2. the arity-4 Fisher curvature support is the input-side lift of the binary
   commutator support;
3. the closed-nontrivial hypercell boundary is not itself the cohomology
   object, because its natural signed all-pair differential has d^2 != 0 over Z.

The resulting theorem uses the filtered adjacency extension class as the
cohomological object, and treats higher arity curvature/carry as Fisher-jet
shadows of that class.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from compute_f4_u2_ext_ch import coefficient_by_key, compute_witnesses, tangent_compatible
from compute_h4_curvature_lift import (
    INPUT_SIDE,
    cell_text,
    h2_commutator_orbits,
    h4_orbit_rows,
    projection_summary,
)


REPORT_DIR = Path(__file__).with_name("reports")
EXT_JSON = REPORT_DIR / "ext_ch_cocycle_f4_u2.json"
DEFAULT_JSON = REPORT_DIR / "fc2_curvature_carry_certificate.json"
DEFAULT_MD = REPORT_DIR / "fc2_curvature_carry_certificate.md"


def load_ext_summary() -> dict[str, Any]:
    return json.loads(EXT_JSON.read_text(encoding="utf-8"))


def all_pair_d2_witness_z2_squared() -> dict[str, Any]:
    """Return the small d^2 witness used to rule out the naive complex.

    The witness is for the all-pair signed contraction on closed nontrivial
    cells of (Z/2)^2.  It is small enough to state directly and mirrors
    empirical/verify_d_squared_z2_squared.py.
    """

    return {
        "ring": "(Z/2)^2",
        "cell": [1, 2, 1, 2],
        "d4_cell": {"(1, 2, 3)": -3, "(2, 1, 3)": -1},
        "d3_d4_cell_over_Z": {"(3, 3)": 4, "(2, 2)": -2, "(1, 1)": 2},
        "d_squared_zero_over_Z": False,
        "d_squared_zero_mod_2_on_witness": True,
        "interpretation": (
            "The nontrivial closed-cell all-pair boundary cannot be the "
            "FC2 cohomology over Q/Z.  FC2 must use the filtered adjacency "
            "extension class, with hypercell boundaries as support shadows."
        ),
    }


def h4_lift_summary() -> dict[str, Any]:
    cell_to_h4_orbit, h4_rows = h4_orbit_rows()
    commutator_orbits, key_to_h2_orbit, _defect_orbits = h2_commutator_orbits()
    commutator_keys = set(
        coefficient_by_key(tangent_compatible(compute_witnesses("commutator")))
    )
    summary = projection_summary(
        INPUT_SIDE,
        commutator_keys,
        key_to_h2_orbit,
        cell_to_h4_orbit,
        h4_rows,
    )
    hit_h4_orbits = set(summary["h4_to_h2"])
    family_orbit_counts = Counter(row["family"] for row in h4_rows)
    hit_family_orbit_counts = Counter(h4_rows[orbit_id]["family"] for orbit_id in hit_h4_orbits)
    pure_hits = [
        orbit_id
        for orbit_id in sorted(hit_h4_orbits)
        if h4_rows[orbit_id]["family"] in {"TTTT", "WWWW"}
    ]
    mixed_rows = []
    for orbit_id in sorted(
        hit_h4_orbits,
        key=lambda oid: (h4_rows[oid]["family"], h4_rows[oid]["size"], oid),
    ):
        row = h4_rows[orbit_id]
        mixed_rows.append(
            {
                "h4_orbit": orbit_id,
                "family": row["family"],
                "size": row["size"],
                "h2_commutator_orbits": len(summary["h4_to_h2"][orbit_id]),
                "entry_hits": summary["h4_entry_hits"][orbit_id],
                "representative": cell_text(row["seed"]),
            }
        )

    return {
        "closed_nontrivial_4_cells": 3165,
        "gamma_x_s4_orbits": len(h4_rows),
        "family_orbit_counts": dict(sorted(family_orbit_counts.items())),
        "arity_2_commutator_orbits": len(commutator_orbits),
        "lifted_arity_2_commutator_orbits": len(summary["h2_orbits"]),
        "h2_to_h4_multiplicity": dict(
            sorted(Counter(len(ids) for ids in summary["h2_to_h4"].values()).items())
        ),
        "mixed_h4_orbits_hit": sum(
            count
            for family, count in hit_family_orbit_counts.items()
            if family in {"TTWW", "TWWW"}
        ),
        "mixed_h4_orbits_total": 7,
        "pure_h4_orbits_hit": len(pure_hits),
        "pure_h4_orbits_total": 11,
        "entry_hits_by_family": dict(sorted(summary["family_entry_hits"].items())),
        "mixed_orbit_image_table": mixed_rows,
    }


def build_payload() -> dict[str, Any]:
    ext = load_ext_summary()
    reduction = ext["coboundary_reduction"]

    return {
        "claim": "FC2 finite-row theorem certificate",
        "ring": "F_4[u]/(u^2)",
        "cohomological_object": (
            "filtered quotient-character adjacency extension class "
            "[kappa] in the section-change/Hochschild 2-cohomology model"
        ),
        "not_the_object": (
            "the signed all-pair boundary on closed nontrivial hypercells; "
            "that boundary fails d^2=0 over Z"
        ),
        "binary_ext_ch": {
            "raw_atom_count": ext["raw_atom_count"],
            "raw_pair_count": ext["raw_pair_count"],
            "atom_orbit_count": ext["atom_orbit_count"],
            "pair_orbit_count": ext["pair_orbit_count"],
            "raw_coefficient_distribution": ext["raw_coefficient_distribution"],
            "raw_path_distribution": ext["raw_path_distribution"],
            "coboundary_field": reduction["coefficient_field"],
            "c1_generators": reduction["c1_generators"],
            "c2_dimension": reduction["c2_dimension"],
            "coboundary_rank": reduction["coboundary_rank"],
            "raw_support": reduction["raw_support"],
            "residual_support": reduction["residual_support"],
            "raw_is_coboundary": reduction["raw_is_coboundary"],
            "raw_non_coboundary_over_q_certified": reduction[
                "raw_non_coboundary_over_q_certified"
            ],
        },
        "arity4_curvature_shadow": h4_lift_summary(),
        "naive_hypercell_complex_obstruction": all_pair_d2_witness_z2_squared(),
        "fc2_status": (
            "Solved for the first mixed local row: the binary Ext_CH class is "
            "the cohomological source, K_CH is its cubic Fisher shadow, and "
            "the arity-4 curvature support is its input-side Fisher-jet lift."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    ext = payload["binary_ext_ch"]
    h4 = payload["arity4_curvature_shadow"]
    d2 = payload["naive_hypercell_complex_obstruction"]

    lines = [
        "# FC2 Curvature-Carry Certificate",
        "",
        f"- ring: `{payload['ring']}`",
        f"- cohomological object: {payload['cohomological_object']}",
        f"- not the object: {payload['not_the_object']}",
        "",
        "## Binary Filtered Carry",
        "",
        f"- raw atoms: `{ext['raw_atom_count']}`",
        f"- raw carry pairs: `{ext['raw_pair_count']}`",
        f"- atom orbits: `{ext['atom_orbit_count']}`",
        f"- pair orbits: `{ext['pair_orbit_count']}`",
        f"- full-block coboundary rank: `{ext['coboundary_rank']}` / `{ext['c1_generators']}`",
        f"- C2 dimension: `{ext['c2_dimension']}`",
        f"- residual support: `{ext['residual_support']}`",
        f"- raw is coboundary: `{ext['raw_is_coboundary']}`",
        f"- non-coboundary over Q certified: `{ext['raw_non_coboundary_over_q_certified']}`",
        "",
        "## Arity-4 Fisher Curvature Shadow",
        "",
        f"- closed nontrivial 4-cells: `{h4['closed_nontrivial_4_cells']}`",
        f"- Gamma_R x S4 orbits: `{h4['gamma_x_s4_orbits']}`",
        f"- arity-2 commutator orbits: `{h4['arity_2_commutator_orbits']}`",
        f"- lifted commutator orbits: `{h4['lifted_arity_2_commutator_orbits']}`",
        f"- mixed H4 orbits hit: `{h4['mixed_h4_orbits_hit']} / {h4['mixed_h4_orbits_total']}`",
        f"- pure H4 orbits hit: `{h4['pure_h4_orbits_hit']} / {h4['pure_h4_orbits_total']}`",
        f"- entry hits by family: `{h4['entry_hits_by_family']}`",
        "",
        "| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |",
        "|---:|---|---:|---:|---:|---|",
    ]

    for row in h4["mixed_orbit_image_table"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["h4_orbit"]),
                    row["family"],
                    str(row["size"]),
                    str(row["h2_commutator_orbits"]),
                    str(row["entry_hits"]),
                    "`" + row["representative"] + "`",
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Why This Is Not Hypercell Cohomology",
        "",
        "The closed nontrivial all-pair boundary fails `d^2=0` over `Z` on a",
        "tiny control row:",
        "",
        f"- witness ring: `{d2['ring']}`",
        f"- witness cell: `{d2['cell']}`",
        f"- `d_3 d_4(cell)` over `Z`: `{d2['d3_d4_cell_over_Z']}`",
        f"- `d^2 = 0` over `Z`: `{d2['d_squared_zero_over_Z']}`",
        f"- witness vanishes mod 2: `{d2['d_squared_zero_mod_2_on_witness']}`",
        "",
        "So FC2 is solved by using the filtered adjacency extension class as",
        "the cohomological source.  The hyper-adjacency tower remains the",
        "Fisher-jet support shadow of that source.",
        "",
        "## Status",
        "",
        payload["fc2_status"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    DEFAULT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    DEFAULT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(render_markdown(payload))
    print(f"Wrote {DEFAULT_JSON}")
    print(f"Wrote {DEFAULT_MD}")


if __name__ == "__main__":
    main()

