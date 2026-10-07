"""Emit the first FC1 Noether-atlas census certificate.

This is the executable first layer for the FC1 Noether atlas program.  It
does not enumerate all 14-Hamiltonian tuple supports in the 637-coordinate
seed.  Instead it certifies the finite orbit skeleton on which that tuple
enumeration will act: packet-energy coordinates, H3/H4 hyper-adjacency orbit
buckets, K_CH commutator orbits, carry-pair orbits, and the FC2 residual
visibility ledger.

The current target is deliberately narrow: F_4[u]/(u^2).
"""

from __future__ import annotations

from collections import Counter
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"
ROW_KEY = "f4-u2"
OUT_JSON = REPORTS / "fc1_noether_atlas_census_f4_u2.json"
OUT_MD = REPORTS / "fc1_noether_atlas_census_f4_u2.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def find_row(payload: dict[str, Any], key: str) -> dict[str, Any]:
    for row in payload.get("rows", []):
        if row.get("row_key") == key:
            return row
    raise KeyError(f"row {key!r} not found")


def int_counter_from_mapping(mapping: dict[str, Any]) -> Counter[int]:
    return Counter({int(key): int(value) for key, value in mapping.items()})


def counter_rows(counter: Counter[Any]) -> list[dict[str, Any]]:
    return [
        {"value": value, "count": count}
        for value, count in sorted(counter.items(), key=lambda item: item[0])
    ]


def distribution_text(rows: list[dict[str, Any]] | Counter[Any]) -> str:
    if isinstance(rows, Counter):
        items = sorted(rows.items(), key=lambda item: item[0])
    else:
        items = [(row["value"], row["count"]) for row in rows]
    return ", ".join(f"{value}:{count}" for value, count in items)


def orbit_stabilizer(group_order: int, orbit_size: int) -> dict[str, Any]:
    exact = orbit_size != 0 and group_order % orbit_size == 0
    return {
        "group_order": group_order,
        "orbit_size": orbit_size,
        "stabilizer_order": group_order // orbit_size if exact else None,
        "orbit_stabilizer_integral": exact,
    }


def add_check(
    checks: list[dict[str, Any]],
    name: str,
    observed: Any,
    expected: Any,
    note: str = "",
) -> None:
    checks.append(
        {
            "name": name,
            "observed": observed,
            "expected": expected,
            "pass": observed == expected,
            "note": note,
        }
    )


def stabilizer_distribution(rows: list[dict[str, Any]], group_order: int) -> Counter[int]:
    distribution: Counter[int] = Counter()
    for row in rows:
        size = int(row["size"])
        if size and group_order % size == 0:
            distribution[group_order // size] += 1
        else:
            distribution[-1] += 1
    return distribution


def source_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def build_packet_energy_orbits(row: dict[str, Any]) -> list[dict[str, Any]]:
    gamma_size = int(row["gamma_size"])
    return [
        {
            "id": index,
            "coordinate": f"E_{packet}",
            "packet": packet,
            "packet_size": size,
            "symmetry_group": "Gamma_R",
            **orbit_stabilizer(gamma_size, 1),
            "determinant_character_on_1d_bucket": "trivial",
        }
        for index, (packet, size) in enumerate(row.get("packets", {}).items())
    ]


def build_hyper_orbits(
    rows: list[dict[str, Any]],
    *,
    arity: int,
    gamma_size: int,
) -> list[dict[str, Any]]:
    group_order = gamma_size * math.factorial(arity)
    out: list[dict[str, Any]] = []
    for row in rows:
        size = int(row["size"])
        out.append(
            {
                "id": row["id"],
                "arity": arity,
                "family": row["family"],
                "representative": row["representative"],
                "symmetry_group": f"Gamma_R x S_{arity}",
                **orbit_stabilizer(group_order, size),
                "valid_contractions": row.get("valid_contractions"),
                "target_images": row.get("target_images", []),
                "source_preimages": row.get("source_preimages", []),
                "determinant_character_on_1d_bucket": "trivial",
            }
        )
    return out


def build_normalizer_orbit_rows(
    rows: list[dict[str, Any]],
    *,
    gamma_size: int,
    keep: int | None = None,
) -> list[dict[str, Any]]:
    selected = rows if keep is None else rows[:keep]
    out: list[dict[str, Any]] = []
    for row in selected:
        size = int(row["size"])
        out.append(
            {
                "id": row.get("id"),
                "representative": row.get("representative"),
                "path": row.get("path"),
                "matrix_transition": row.get("matrix_transition"),
                "operand_conductors": row.get("operand_conductors"),
                "coefficient": row.get("coefficient") or row.get("coefficients"),
                "symmetry_group": "Gamma_R",
                **orbit_stabilizer(gamma_size, size),
                "determinant_character_on_1d_bucket": "trivial",
            }
        )
    return out


def build_report() -> dict[str, Any]:
    seed_path = REPORTS / "fc1_noether_atlas_seed.json"
    local_path = REPORTS / "local_adjacency_constructor_f4_u2.json"
    ext_path = REPORTS / "ext_ch_cocycle_f4_u2.json"
    ext_orbits_path = REPORTS / "f4_u2_ext_orbits.json"
    atom_path = REPORTS / "fc2_atom_shadow_map.json"
    contraction_path = REPORTS / "fc2_h4_contraction_shadow.json"

    seed = load_json(seed_path)
    local = load_json(local_path)
    ext = load_json(ext_path)
    ext_orbits = load_json(ext_orbits_path)
    atom = find_row(load_json(atom_path), ROW_KEY)
    contraction = find_row(load_json(contraction_path), ROW_KEY)
    seed_row = find_row(seed, ROW_KEY)

    gamma_size = int(seed_row["gamma_size"])
    h3_group_order = gamma_size * math.factorial(3)
    h4_group_order = gamma_size * math.factorial(4)

    packet_energy_orbits = build_packet_energy_orbits(seed_row)
    h3_orbits = build_hyper_orbits(
        local["tower_contraction"]["target_orbit_rows"],
        arity=3,
        gamma_size=gamma_size,
    )
    h4_orbits = build_hyper_orbits(
        local["tower_contraction"]["source_orbit_rows"],
        arity=4,
        gamma_size=gamma_size,
    )
    carry_pair_orbits = build_normalizer_orbit_rows(
        ext["canonical_pair_orbits"],
        gamma_size=gamma_size,
    )
    atom_orbit_samples = build_normalizer_orbit_rows(
        ext["canonical_atom_orbits"],
        gamma_size=gamma_size,
        keep=12,
    )
    commutator_orbit_samples = build_normalizer_orbit_rows(
        ext_orbits["commutator_orbits"],
        gamma_size=gamma_size,
        keep=12,
    )

    kch_size_distribution = Counter(
        int(row["size"]) for row in ext_orbits["commutator_orbits"]
    )
    full_defect_size_distribution = Counter(
        int(row["size"]) for row in ext_orbits["full_defect_orbits"]
    )
    kch_transition_distribution = Counter(
        row["matrix_transition"] for row in ext_orbits["commutator_orbits"]
    )
    full_transition_distribution = Counter(
        row["matrix_transition"] for row in ext_orbits["full_defect_orbits"]
    )

    atom_accounting = atom["atom_accounting"]
    contraction_accounting = contraction["atom_accounting"]
    h4_visible = int(atom_accounting["visible_h4_incident_atoms"])
    h3_from_h4_invisible = int(
        contraction_accounting["h4_invisible_h3_contraction_visible_atoms"]
    )
    remaining_invisible = int(contraction_accounting["remaining_invisible_atoms"])
    residual_total = int(atom_accounting["raw_residual_atoms"])

    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "gamma size agrees across seed/local/ext",
        [gamma_size, local["constructor"]["gamma_size"], ext["gamma_size"]],
        [24, 24, 24],
    )
    add_check(
        checks,
        "seed coordinate count",
        int(seed_row["finite_observation_coordinate_count_seed"]),
        len(packet_energy_orbits)
        + len(h3_orbits)
        + len(h4_orbits)
        + int(seed_row["k_ch_commutator_orbits"])
        + len(carry_pair_orbits),
        "packet energies + H3 + H4 + K_CH commutator orbits + carry-pair orbits",
    )
    add_check(
        checks,
        "H3 orbit-size sum",
        sum(int(row["orbit_size"]) for row in h3_orbits),
        int(local["h3"]["cells"]),
    )
    add_check(
        checks,
        "H4 orbit-size sum",
        sum(int(row["orbit_size"]) for row in h4_orbits),
        int(local["h4"]["cells"]),
    )
    add_check(
        checks,
        "K_CH commutator orbit-size sum",
        sum(size * count for size, count in kch_size_distribution.items()),
        int(ext_orbits["summary"]["commutator_tangent_compatible_entries"]),
    )
    add_check(
        checks,
        "carry-pair orbit-size sum",
        sum(int(row["orbit_size"]) for row in carry_pair_orbits),
        int(ext["raw_pair_count"]),
    )
    atom_size_distribution = int_counter_from_mapping(ext["atom_orbit_size_distribution"])
    add_check(
        checks,
        "raw atom orbit-size sum",
        sum(size * count for size, count in atom_size_distribution.items()),
        int(ext["raw_atom_count"]),
    )
    add_check(
        checks,
        "support/full residual kept separate",
        [
            atom["projection_summary"]["full_filtered_residual"],
            atom["projection_summary"]["support_projection_residual"],
        ],
        [1569, 0],
        "support residual 0 is not full filtered closure",
    )
    add_check(
        checks,
        "residual visibility partition",
        h4_visible + h3_from_h4_invisible + remaining_invisible,
        residual_total,
        "H4-visible + H3-contraction-visible from H4-invisible + remaining invisible",
    )
    add_check(
        checks,
        "K_CH is not an Ext_CH detector",
        h4_visible < residual_total,
        True,
        "visible H4 incidence is only a Fisher-shadow channel",
    )
    add_check(
        checks,
        "H3 contraction still leaves hidden residue",
        remaining_invisible > 0,
        True,
        "remaining invisible atoms require richer coefficient or higher-arity channels",
    )

    certificate_pass = all(check["pass"] for check in checks)

    payload = {
        "schema": "fc1_noether_atlas_census.v1",
        "row_key": ROW_KEY,
        "ring": seed_row["ring"],
        "status": "first orbit-skeleton census certificate; full tuple enumeration deferred",
        "certificate_pass": certificate_pass,
        "scope": {
            "finite_adjacency_fisher_jet_order": "seed/report order",
            "polynomial_jet_order": "orbit-skeleton layer",
            "declared_skeleton": (
                "packet energies + H3/H4 orbit buckets + K_CH commutator "
                "orbits + carry-pair orbits"
            ),
            "not_claimed": [
                "all smooth invariant functions",
                "all Fisher-volume-preserving currents",
                "all 14-Hamiltonian tuple supports inside 637 seed coordinates",
                "K_CH as a standalone Ext_CH detector",
                "support residual 0 as full filtered closure",
            ],
        },
        "sources": {
            "seed": source_path(seed_path),
            "local_adjacency": source_path(local_path),
            "ext_cocycle": source_path(ext_path),
            "ext_orbits": source_path(ext_orbits_path),
            "atom_shadow": source_path(atom_path),
            "h4_contraction_shadow": source_path(contraction_path),
        },
        "row_summary": {
            "gamma_size": gamma_size,
            "packet_energy_coordinates": len(packet_energy_orbits),
            "h3_orbits": len(h3_orbits),
            "h4_orbits": len(h4_orbits),
            "k_ch_commutator_orbits": int(seed_row["k_ch_commutator_orbits"]),
            "carry_pair_orbits": len(carry_pair_orbits),
            "seed_coordinate_count": int(
                seed_row["finite_observation_coordinate_count_seed"]
            ),
            "full_filtered_residual": atom["projection_summary"][
                "full_filtered_residual"
            ],
            "support_projection_residual": atom["projection_summary"][
                "support_projection_residual"
            ],
            "h4_visible_atoms": h4_visible,
            "h3_contraction_visible_from_h4_invisible": h3_from_h4_invisible,
            "remaining_invisible_atoms": remaining_invisible,
        },
        "count_checks": checks,
        "determinant_character_status": {
            "orbit_bucket_coordinates": (
                "For a single orbit-bucket coordinate, the stabilizer fixes the "
                "aggregate coordinate, so the determinant character is trivial."
            ),
            "tuple_determinants": (
                "Not yet enumerated.  The next layer must choose finite "
                "Hamiltonian tuple supports/coefficient patterns and compute "
                "det(A_gamma) on each tuple stabilizer."
            ),
        },
        "orbit_skeleton": {
            "packet_energy_orbits": packet_energy_orbits,
            "h3_orbits": h3_orbits,
            "h4_orbits": h4_orbits,
            "carry_pair_orbits": carry_pair_orbits,
            "k_ch_commutator_summary": {
                "symmetry_group": "Gamma_R",
                "group_order": gamma_size,
                "orbit_count": len(ext_orbits["commutator_orbits"]),
                "orbit_size_distribution": counter_rows(kch_size_distribution),
                "stabilizer_order_distribution": counter_rows(
                    stabilizer_distribution(ext_orbits["commutator_orbits"], gamma_size)
                ),
                "matrix_transition_distribution": counter_rows(
                    kch_transition_distribution
                ),
                "sample_orbits": commutator_orbit_samples,
            },
            "full_defect_summary": {
                "symmetry_group": "Gamma_R",
                "group_order": gamma_size,
                "orbit_count": len(ext_orbits["full_defect_orbits"]),
                "orbit_size_distribution": counter_rows(full_defect_size_distribution),
                "stabilizer_order_distribution": counter_rows(
                    stabilizer_distribution(ext_orbits["full_defect_orbits"], gamma_size)
                ),
                "matrix_transition_distribution": counter_rows(
                    full_transition_distribution
                ),
            },
            "raw_atom_orbit_summary": {
                "symmetry_group": "Gamma_R",
                "group_order": gamma_size,
                "orbit_count": int(ext["atom_orbit_count"]),
                "orbit_size_distribution": counter_rows(atom_size_distribution),
                "stabilizer_order_distribution": counter_rows(
                    Counter(
                        {
                            gamma_size // size: count
                            for size, count in atom_size_distribution.items()
                            if gamma_size % size == 0
                        }
                    )
                ),
                "sample_orbits": atom_orbit_samples,
            },
        },
        "residual_visibility_ledger": {
            "full_filtered_residual_atoms": residual_total,
            "support_projection_residual": atom["projection_summary"][
                "support_projection_residual"
            ],
            "h4_visible_atoms": h4_visible,
            "h4_invisible_atoms": int(atom_accounting["h4_invisible_atoms"]),
            "h3_contraction_visible_from_h4_invisible": h3_from_h4_invisible,
            "remaining_invisible_atoms": remaining_invisible,
            "h4_invisible_family_visibility": contraction[
                "h4_invisible_family_visibility"
            ],
            "h4_invisible_path_visibility": contraction[
                "h4_invisible_path_visibility"
            ],
        },
        "next_tuple_layer": {
            "needed": True,
            "reason": (
                "The orbit skeleton is finite and count-checked, but the actual "
                "FC1 tuple census must still choose tuple support/coefficient "
                "patterns in this skeleton and compute tuple stabilizers and "
                "determinant characters."
            ),
            "recommended_first_tuple_skeleton": {
                "row": ROW_KEY,
                "max_coordinate_blocks": [
                    "packet_energy",
                    "carry_pair",
                    "h4_visible_incidence_bucket",
                    "remaining_invisible_bucket",
                ],
                "purpose": (
                    "small enough to test determinant-character and closure-defect "
                    "bookkeeping before touching all K_CH orbit coordinates"
                ),
            },
        },
    }
    return payload


def md_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return lines


def write_markdown(payload: dict[str, Any]) -> None:
    summary = payload["row_summary"]
    checks = payload["count_checks"]
    skeleton = payload["orbit_skeleton"]
    residual = payload["residual_visibility_ledger"]

    lines: list[str] = [
        "# FC1 Noether Atlas Census: F4[u]/(u^2)",
        "",
        "This is the first executable FC1 Noether-atlas census certificate.",
        "It certifies the finite orbit skeleton for the smallest mixed local row.",
        "It is not the full 14-Hamiltonian tuple-orbit census yet.",
        "",
        "## Scope",
        "",
        f"- row: `{payload['row_key']}`",
        f"- ring: `{payload['ring']}`",
        f"- status: `{payload['status']}`",
        f"- certificate pass: `{payload['certificate_pass']}`",
        "- support residual `0` is kept separate from full filtered closure.",
        "- `K_CH` is used only as a Fisher-shadow channel of `[kappa]`.",
        "",
        "## Seed Coordinates",
        "",
    ]

    lines.extend(
        md_table(
            ["block", "count"],
            [
                ["packet energies", summary["packet_energy_coordinates"]],
                ["H3 orbit buckets", summary["h3_orbits"]],
                ["H4 orbit buckets", summary["h4_orbits"]],
                ["K_CH commutator orbits", summary["k_ch_commutator_orbits"]],
                ["carry-pair orbits", summary["carry_pair_orbits"]],
                ["seed total", summary["seed_coordinate_count"]],
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
                for check in checks
            ],
        )
    )

    lines.extend(["", "## Orbit-Stabilizer Summary", ""])
    lines.extend(
        md_table(
            ["block", "group", "orbits", "size distribution", "stabilizer distribution"],
            [
                [
                    "H3",
                    "Gamma_R x S3",
                    len(skeleton["h3_orbits"]),
                    distribution_text(
                        Counter(row["orbit_size"] for row in skeleton["h3_orbits"])
                    ),
                    distribution_text(
                        Counter(row["stabilizer_order"] for row in skeleton["h3_orbits"])
                    ),
                ],
                [
                    "H4",
                    "Gamma_R x S4",
                    len(skeleton["h4_orbits"]),
                    distribution_text(
                        Counter(row["orbit_size"] for row in skeleton["h4_orbits"])
                    ),
                    distribution_text(
                        Counter(row["stabilizer_order"] for row in skeleton["h4_orbits"])
                    ),
                ],
                [
                    "K_CH commutator",
                    "Gamma_R",
                    skeleton["k_ch_commutator_summary"]["orbit_count"],
                    distribution_text(
                        skeleton["k_ch_commutator_summary"]["orbit_size_distribution"]
                    ),
                    distribution_text(
                        skeleton["k_ch_commutator_summary"][
                            "stabilizer_order_distribution"
                        ]
                    ),
                ],
                [
                    "carry pairs",
                    "Gamma_R",
                    len(skeleton["carry_pair_orbits"]),
                    distribution_text(
                        Counter(
                            row["orbit_size"] for row in skeleton["carry_pair_orbits"]
                        )
                    ),
                    distribution_text(
                        Counter(
                            row["stabilizer_order"]
                            for row in skeleton["carry_pair_orbits"]
                        )
                    ),
                ],
                [
                    "raw atoms",
                    "Gamma_R",
                    skeleton["raw_atom_orbit_summary"]["orbit_count"],
                    distribution_text(
                        skeleton["raw_atom_orbit_summary"]["orbit_size_distribution"]
                    ),
                    distribution_text(
                        skeleton["raw_atom_orbit_summary"][
                            "stabilizer_order_distribution"
                        ]
                    ),
                ],
            ],
        )
    )

    lines.extend(["", "## Residual Visibility Ledger", ""])
    lines.extend(
        md_table(
            ["field", "value"],
            [
                ["full filtered residual atoms", residual["full_filtered_residual_atoms"]],
                ["support projection residual", residual["support_projection_residual"]],
                ["H4-visible atoms", residual["h4_visible_atoms"]],
                ["H4-invisible atoms", residual["h4_invisible_atoms"]],
                [
                    "H3-contraction visible from H4-invisible",
                    residual["h3_contraction_visible_from_h4_invisible"],
                ],
                ["remaining invisible atoms", residual["remaining_invisible_atoms"]],
            ],
        )
    )

    lines.extend(
        [
            "",
            "## Determinant Characters",
            "",
            "At this orbit-bucket layer, each single coordinate bucket has trivial",
            "one-dimensional determinant character on its stabilizer.  The tuple",
            "determinant characters are deliberately not claimed here: they require",
            "the next layer, where finite Hamiltonian tuple supports/coefficient",
            "patterns are chosen and stabilized.",
            "",
            "## Next Tuple Layer",
            "",
            "Use this certificate as the finite base table for the first real tuple",
            "enumeration.  The recommended first tuple skeleton is small: packet",
            "energies, carry-pair buckets, the H4-visible incidence bucket, and",
            "the remaining-invisible bucket.  Once that determinant-character",
            "machinery passes, expand to all K_CH commutator orbit coordinates.",
            "",
            "## Sources",
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
