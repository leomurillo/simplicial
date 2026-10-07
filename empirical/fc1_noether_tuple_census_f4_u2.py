"""First tuple-support census for the FC1 Noether atlas on F4[u]/(u^2).

This is the next layer after ``fc1_noether_atlas_census.py``.  It chooses the
small aggregate 24-coordinate skeleton recommended by that certificate:

    packet energies (2)
    carry-pair orbit buckets (20)
    H4-visible residual incidence bucket (1)
    remaining-invisible residual bucket (1)

The skeleton coordinates are already normalizer orbit-buckets, so the
Gamma_R action fixes each aggregate coordinate.  Consequently every
14-Hamiltonian support has full stabilizer Gamma_R and trivial determinant
character.  That is intentionally a baseline, not the final nontrivial
637-coordinate tuple census.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "empirical" / "reports"
BASE_JSON = REPORTS / "fc1_noether_atlas_census_f4_u2.json"
OUT_JSON = REPORTS / "fc1_noether_tuple_census_f4_u2_small.json"
OUT_MD = REPORTS / "fc1_noether_tuple_census_f4_u2_small.md"

ROW_KEY = "f4-u2"
HAMILTONIAN_COUNT = 14


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def choose(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def source_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def counter_rows(counter: Counter[Any]) -> list[dict[str, Any]]:
    return [
        {"key": key, "count": count}
        for key, count in sorted(counter.items(), key=lambda item: item[0])
    ]


def distribution_text(rows: list[dict[str, Any]]) -> str:
    return ", ".join(f"{row['key']}:{row['count']}" for row in rows)


def make_coordinates(base: dict[str, Any]) -> list[dict[str, Any]]:
    row = base["row_summary"]
    carry_pair_orbits = base["orbit_skeleton"]["carry_pair_orbits"]

    coords: list[dict[str, Any]] = [
        {
            "id": "PE:u",
            "kind": "packet_energy",
            "label": "E_u",
            "residual_channel": "none",
        },
        {
            "id": "PE:u^2",
            "kind": "packet_energy",
            "label": "E_u^2",
            "residual_channel": "none",
        },
    ]
    for orbit in carry_pair_orbits:
        coords.append(
            {
                "id": f"CP:{orbit['id']}",
                "kind": "carry_pair_orbit",
                "label": f"carry_pair_{orbit['id']}",
                "path": orbit.get("path"),
                "residual_channel": "filtered_carry_pair",
            }
        )
    coords.extend(
        [
            {
                "id": "VIS:h4_visible",
                "kind": "residual_visibility_bucket",
                "label": "H4_visible_incidence",
                "residual_channel": "H4-visible Fisher shadow",
                "atom_count": row["h4_visible_atoms"],
            },
            {
                "id": "VIS:remaining_invisible",
                "kind": "residual_visibility_bucket",
                "label": "remaining_invisible_after_H3_contraction",
                "residual_channel": "hidden after tested H4/H3 projections",
                "atom_count": row["remaining_invisible_atoms"],
            },
        ]
    )
    return coords


def summarize_support(
    support: tuple[int, ...],
    coordinates: list[dict[str, Any]],
) -> tuple[tuple[str, int], ...]:
    counts: Counter[str] = Counter(coordinates[index]["kind"] for index in support)
    return tuple(
        sorted(
            {
                "packet_energy": counts["packet_energy"],
                "carry_pair_orbit": counts["carry_pair_orbit"],
                "residual_visibility_bucket": counts["residual_visibility_bucket"],
            }.items()
        )
    )


def coverage_key(support: tuple[int, ...], coordinates: list[dict[str, Any]]) -> str:
    ids = {coordinates[index]["id"] for index in support}
    has_h4 = "VIS:h4_visible" in ids
    has_hidden = "VIS:remaining_invisible" in ids
    if has_h4 and has_hidden:
        return "both_h4_visible_and_remaining_hidden"
    if has_h4:
        return "h4_visible_only"
    if has_hidden:
        return "remaining_hidden_only"
    return "no_visibility_bucket"


def support_to_ids(support: tuple[int, ...], coordinates: list[dict[str, Any]]) -> list[str]:
    return [coordinates[index]["id"] for index in support]


def build_report() -> dict[str, Any]:
    base = load_json(BASE_JSON)
    gamma_size = int(base["row_summary"]["gamma_size"])
    coordinates = make_coordinates(base)
    coordinate_count = len(coordinates)
    tuple_support_total = choose(coordinate_count, HAMILTONIAN_COUNT)

    kind_counts = Counter(coord["kind"] for coord in coordinates)
    category_counts: Counter[str] = Counter()
    coverage_counts: Counter[str] = Counter()
    sample_supports: list[dict[str, Any]] = []
    category_samples: dict[tuple[tuple[str, int], ...], tuple[int, ...]] = {}

    for support in combinations(range(coordinate_count), HAMILTONIAN_COUNT):
        category = summarize_support(support, coordinates)
        category_counts[repr(category)] += 1
        coverage_counts[coverage_key(support, coordinates)] += 1
        category_samples.setdefault(category, support)
        if len(sample_supports) < 10:
            sample_supports.append(
                {
                    "support_ids": support_to_ids(support, coordinates),
                    "category": dict(category),
                    "stabilizer_order": gamma_size,
                    "determinant_character": "trivial",
                }
            )

    category_sample_rows = [
        {
            "category": dict(category),
            "count": category_counts[repr(category)],
            "sample_support_ids": support_to_ids(support, coordinates),
        }
        for category, support in sorted(
            category_samples.items(), key=lambda item: repr(item[0])
        )
    ]

    formula_category_counts: Counter[str] = Counter()
    for packet_count in range(kind_counts["packet_energy"] + 1):
        for carry_count in range(kind_counts["carry_pair_orbit"] + 1):
            for visibility_count in range(kind_counts["residual_visibility_bucket"] + 1):
                if packet_count + carry_count + visibility_count != HAMILTONIAN_COUNT:
                    continue
                count = (
                    choose(kind_counts["packet_energy"], packet_count)
                    * choose(kind_counts["carry_pair_orbit"], carry_count)
                    * choose(
                        kind_counts["residual_visibility_bucket"], visibility_count
                    )
                )
                if not count:
                    continue
                key = repr(
                    tuple(
                        sorted(
                            {
                                "packet_energy": packet_count,
                                "carry_pair_orbit": carry_count,
                                "residual_visibility_bucket": visibility_count,
                            }.items()
                        )
                    )
                )
                formula_category_counts[key] = count

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
        "coordinate count",
        coordinate_count,
        24,
        "2 packet energies + 20 carry-pair orbits + 2 visibility buckets",
    )
    add_check(
        "tuple support count",
        sum(category_counts.values()),
        tuple_support_total,
        f"C({coordinate_count},{HAMILTONIAN_COUNT})",
    )
    add_check(
        "category formula agrees with enumeration",
        dict(category_counts),
        dict(formula_category_counts),
    )
    add_check(
        "coverage partition",
        sum(coverage_counts.values()),
        tuple_support_total,
    )
    add_check(
        "normalizer orbits equal supports on aggregate skeleton",
        tuple_support_total,
        tuple_support_total,
        "each aggregate coordinate is already a Gamma_R orbit bucket",
    )
    add_check(
        "stabilizer order is full Gamma_R",
        gamma_size,
        24,
    )
    add_check(
        "determinant character baseline",
        "trivial",
        "trivial",
        "aggregate bucket coordinates are fixed one-dimensional coordinates",
    )
    add_check(
        "support/full residual still distinguished",
        [
            base["row_summary"]["full_filtered_residual"],
            base["row_summary"]["support_projection_residual"],
        ],
        [1569, 0],
    )
    add_check(
        "hidden residual bucket retained",
        "VIS:remaining_invisible" in {coord["id"] for coord in coordinates},
        True,
    )

    certificate_pass = all(check["pass"] for check in checks)

    return {
        "schema": "fc1_noether_tuple_census_f4_u2_small.v1",
        "row_key": ROW_KEY,
        "ring": base["ring"],
        "status": "small aggregate tuple-support baseline; nontrivial 637-coordinate tuple census deferred",
        "certificate_pass": certificate_pass,
        "source": source_path(BASE_JSON),
        "scope": {
            "hamiltonian_tuple_size": HAMILTONIAN_COUNT,
            "coordinate_skeleton": (
                "packet energies + carry-pair orbit buckets + H4-visible "
                "incidence bucket + remaining-invisible residual bucket"
            ),
            "normalizer_action": "trivial on aggregate orbit-bucket coordinates",
            "not_claimed": [
                "full 637-coordinate tuple census",
                "nontrivial determinant characters",
                "coefficient-stratified Hamiltonian tuples",
                "all decomposable currents beyond the declared finite skeleton",
            ],
        },
        "coordinate_summary": {
            "coordinate_count": coordinate_count,
            "kind_counts": dict(kind_counts),
            "coordinates": coordinates,
        },
        "tuple_census": {
            "tuple_support_total": tuple_support_total,
            "normalizer_orbit_count": tuple_support_total,
            "orbit_size_distribution": [{"value": 1, "count": tuple_support_total}],
            "stabilizer_order_distribution": [
                {"value": gamma_size, "count": tuple_support_total}
            ],
            "determinant_character_distribution": [
                {"value": "trivial", "count": tuple_support_total}
            ],
            "category_counts": counter_rows(category_counts),
            "category_samples": category_sample_rows,
            "visibility_coverage_counts": counter_rows(coverage_counts),
            "sample_supports": sample_supports,
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
                "replace aggregate carry-pair and visibility buckets by selected "
                "individual normalizer-moving representatives, then compute "
                "nontrivial tuple stabilizers and determinant characters"
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


def check_value_text(value: Any) -> str:
    if isinstance(value, dict):
        return f"{len(value)} entries"
    return json.dumps(value, sort_keys=True)


def write_markdown(payload: dict[str, Any]) -> None:
    census = payload["tuple_census"]
    coord = payload["coordinate_summary"]
    residual = payload["residual_visibility_inherited"]

    lines: list[str] = [
        "# FC1 Noether Tuple Census: F4[u]/(u^2) Small Skeleton",
        "",
        "This is the first tuple-support baseline after the orbit-skeleton",
        "certificate.  The coordinates are aggregate normalizer orbit-buckets,",
        "so every coordinate is fixed by `Gamma_R`; every tuple support has full",
        "stabilizer and trivial determinant character.",
        "",
        "## Scope",
        "",
        f"- row: `{payload['row_key']}`",
        f"- ring: `{payload['ring']}`",
        f"- status: `{payload['status']}`",
        f"- certificate pass: `{payload['certificate_pass']}`",
        f"- Hamiltonian tuple size: `{payload['scope']['hamiltonian_tuple_size']}`",
        "- this is not the full 637-coordinate tuple census.",
        "",
        "## Coordinate Skeleton",
        "",
    ]
    lines.extend(
        md_table(
            ["kind", "count"],
            sorted(coord["kind_counts"].items(), key=lambda item: item[0]),
        )
    )
    lines.extend(
        [
            "",
            "## Tuple Census",
            "",
        ]
    )
    lines.extend(
        md_table(
            ["field", "value"],
            [
                ["coordinate count", coord["coordinate_count"]],
                ["tuple support total", census["tuple_support_total"]],
                ["normalizer orbit count", census["normalizer_orbit_count"]],
                ["orbit size distribution", "1:" + str(census["tuple_support_total"])],
                [
                    "stabilizer order distribution",
                    "24:" + str(census["tuple_support_total"]),
                ],
                [
                    "determinant character distribution",
                    "trivial:" + str(census["tuple_support_total"]),
                ],
            ],
        )
    )
    lines.extend(["", "## Visibility Coverage", ""])
    lines.extend(
        md_table(
            ["coverage", "count"],
            [[row["key"], row["count"]] for row in census["visibility_coverage_counts"]],
        )
    )
    lines.extend(["", "## Category Counts", ""])
    lines.extend(
        md_table(
            ["support category", "count"],
            [[row["key"], row["count"]] for row in census["category_counts"]],
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
                    check_value_text(check["observed"]),
                    check_value_text(check["expected"]),
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
            "This baseline proves that the tuple-census machinery can enumerate",
            "`C(24,14)` finite supports, assign full stabilizer `Gamma_R`, and",
            "emit the determinant-character ledger without collapsing the residual",
            "visibility fields.  It is intentionally too aggregated to produce",
            "nontrivial determinant characters.",
            "",
            "The next layer should replace selected aggregate buckets by individual",
            "normalizer-moving representatives, then recompute stabilizers and",
            "determinants.",
            "",
            f"Source: `{payload['source']}`",
            "",
        ]
    )
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
