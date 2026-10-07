"""Build the finite FC1 Noether-atlas seed table.

This script does not enumerate Hamiltonian tuple orbits yet.  It freezes the
finite coordinate skeleton that the orbit/stabilizer computation acts on:
packet energies, H3/H4 orbit families, K_CH visible-shadow orbits, and full
filtered residual metadata already certified by the FC2 row reports.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def row_key(row: dict[str, Any]) -> str:
    return str(row.get("row_key") or row.get("key") or row.get("ring"))


def as_int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def merge_row(target: dict[str, Any], source: dict[str, Any]) -> None:
    for key, value in source.items():
        if value is None:
            continue
        if key not in target or target[key] in (None, {}, [], 0):
            target[key] = value


def main() -> None:
    visible = load_json(REPORTS / "fc2_visible_fisher_kernel.json")
    classifier = load_json(REPORTS / "fc2_row_classification.json")
    certificates = load_json(REPORTS / "finite_row_certificates.json")

    rows: dict[str, dict[str, Any]] = {}

    for raw in classifier.get("rows", []):
        key = row_key(raw)
        constructor = raw.get("constructor", {})
        ext = raw.get("ext_ch", {})
        rows[key] = {
            "row_key": key,
            "ring": raw.get("ring"),
            "gamma_size": constructor.get("gamma_size"),
            "packets": constructor.get("packets", {}),
            "packet_energy_coordinates": len(constructor.get("packets", {})),
            "h3_orbits": raw.get("h3", {}).get("orbits"),
            "h4_orbits": raw.get("h4", {}).get("orbits"),
            "h3_family_orbits": raw.get("h3", {}).get("family_orbit_counts", {}),
            "h4_family_orbits": raw.get("h4", {}).get("family_orbit_counts", {}),
            "carry_pair_orbits": ext.get("pair_orbit_count"),
            "raw_carry_atoms": ext.get("raw_atom_count"),
            "full_filtered_residual": raw.get("classification", {}).get(
                "full_filtered_residual"
            ),
            "support_projection_residual": raw.get("classification", {}).get(
                "support_projection_residual"
            ),
        }

    for raw in visible.get("rows", []):
        key = row_key(raw)
        entry = rows.setdefault(key, {"row_key": key})
        visible_shadow = raw.get("visible_shadow", {})
        h4_lift = visible_shadow.get("input_side_h4_lift", {})
        merge_row(
            entry,
            {
                "ring": raw.get("ring"),
                "gamma_size": raw.get("gamma_size"),
                "packets": raw.get("packets", {}),
                "packet_energy_coordinates": len(raw.get("packets", {})),
                "k_ch_commutator_orbits": visible_shadow.get("commutator_orbits"),
                "k_ch_commutator_entries": visible_shadow.get("commutator_entries"),
                "h4_mixed_orbits_hit": h4_lift.get("mixed_h4_orbits_hit"),
                "h4_mixed_orbits_total": h4_lift.get("mixed_h4_orbits_total"),
                "h4_pure_orbits_hit": h4_lift.get("pure_h4_orbits_hit"),
                "h4_pure_orbits_total": h4_lift.get("pure_h4_orbits_total"),
                "visible_shadow_status": visible_shadow.get("status"),
            },
        )

    for cert in certificates.get("certificates", []):
        key = row_key(cert)
        entry = rows.setdefault(key, {"row_key": key})
        merge_row(
            entry,
            {
                "ring": cert.get("ring"),
                "gamma_size": cert.get("constructor", {}).get("gamma_size"),
                "packets": cert.get("constructor", {}).get("packets", {}),
                "packet_energy_coordinates": len(
                    cert.get("constructor", {}).get("packets", {})
                ),
                "proof_extraction_status": cert.get("proof_extraction_status"),
            },
        )

    ordered = sorted(rows.values(), key=lambda row: row["row_key"])
    for entry in ordered:
        finite_coordinate_count = (
            as_int(entry.get("packet_energy_coordinates"))
            + as_int(entry.get("h3_orbits"))
            + as_int(entry.get("h4_orbits"))
            + as_int(entry.get("k_ch_commutator_orbits"))
            + as_int(entry.get("carry_pair_orbits"))
        )
        entry["finite_observation_coordinate_count_seed"] = finite_coordinate_count
        entry["noether_next_step"] = (
            "enumerate Hamiltonian tuple support patterns in this finite coordinate "
            "skeleton; compute normalizer stabilizers and determinant characters"
        )

    payload = {
        "purpose": (
            "FC1 Noether-atlas seed: finite coordinate skeleton for exact "
            "finite-sufficient Hamiltonian differentials at fixed row/jet data."
        ),
        "coordinate_count_convention": (
            "packet energies + H3 orbits + H4 orbits + K_CH commutator orbits "
            "+ carry-pair orbits when present.  This is a seed count, not a "
            "dimension theorem for all smooth functions."
        ),
        "rows": ordered,
    }

    json_path = REPORTS / "fc1_noether_atlas_seed.json"
    md_path = REPORTS / "fc1_noether_atlas_seed.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# FC1 Noether Atlas Seed",
        "",
        "This report freezes the finite coordinate skeleton for the next FC1",
        "Noether orbit/stabilizer computation.  It is not the tuple-orbit census",
        "yet; it is the finite input table for that census.",
        "",
        "| row | ring | gamma size | packets | H3 | H4 | K_CH orbits | carry pair orbits | seed coords | residual full/support |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for entry in ordered:
        packets = entry.get("packets", {})
        residual = f"{entry.get('full_filtered_residual', '')}/{entry.get('support_projection_residual', '')}"
        lines.append(
            "| {row_key} | {ring} | {gamma} | {packets} | {h3} | {h4} | {kch} | {carry} | {coords} | {residual} |".format(
                row_key=entry.get("row_key", ""),
                ring=entry.get("ring", ""),
                gamma=entry.get("gamma_size", ""),
                packets=len(packets),
                h3=entry.get("h3_orbits", ""),
                h4=entry.get("h4_orbits", ""),
                kch=entry.get("k_ch_commutator_orbits", ""),
                carry=entry.get("carry_pair_orbits", ""),
                coords=entry.get("finite_observation_coordinate_count_seed", ""),
                residual=residual,
            )
        )

    lines.extend(
        [
            "",
            "## Next Computation",
            "",
            "For a fixed polynomial jet order `r`, enumerate Hamiltonian tuple",
            "support patterns inside the seed coordinate set, compute normalizer",
            "stabilizers, compute determinant characters on each stabilized tuple,",
            "and attach the Paper 11 closure-defect and FC2 filtered residual data.",
            "",
            "The seed coordinate count is deliberately conservative bookkeeping:",
            "it prevents support-level closure, K_CH-visible closure, and full",
            "filtered closure from being collapsed into one number.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
