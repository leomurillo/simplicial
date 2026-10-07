"""Compute H4-to-H3 contraction incidence for F_4[u]/(u^2).

This is a support-level tower diagnostic for Paper 11, Problem 11.6.  Cells
are closed nontrivial additive-character tuples.  A contraction merges two
legs of a closed 4-cell by adding their labels; contractions with zero merged
label are recorded as invalid because the H3 support excludes the trivial
character.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from compute_f4_u2_ext_ch import ACTIONS, add_label, conductor, label_name
from compute_h3_f4_u2 import S3, cell_name as h3_cell_name, h3_cells, transform_cell as transform_h3
from compute_h4_f4_u2 import S4, conductor_family, h4_cells, transform_cell as transform_h4


Label = tuple[int, int]
Cell3 = tuple[Label, Label, Label]
Cell4 = tuple[Label, Label, Label, Label]


def conductor_word(cell: tuple[Label, ...]) -> str:
    return "".join("T" if conductor(label) == "u" else "W" for label in cell)


def orbit_maps_h3() -> tuple[dict[Cell3, int], list[dict[str, object]]]:
    remaining = set(h3_cells())
    cell_to_orbit: dict[Cell3, int] = {}
    rows: list[dict[str, object]] = []
    while remaining:
        seed = min(remaining, key=lambda cell: tuple(label_name(label) for label in cell))
        orbit = {
            transform_h3(seed, action, permutation)
            for action in ACTIONS
            for permutation in S3
        }
        orbit_id = len(rows)
        for cell in orbit:
            cell_to_orbit[cell] = orbit_id
        rows.append(
            {
                "id": orbit_id,
                "size": len(orbit),
                "family": "".join(sorted("T" if conductor(label) == "u" else "W" for label in seed)),
                "representative": h3_cell_name(seed),
            }
        )
        remaining -= orbit
    return cell_to_orbit, rows


def orbit_maps_h4() -> tuple[dict[Cell4, int], list[dict[str, object]]]:
    remaining = set(h4_cells(distinct=False))
    cell_to_orbit: dict[Cell4, int] = {}
    rows: list[dict[str, object]] = []
    while remaining:
        seed = min(remaining, key=lambda cell: tuple(label_name(label) for label in cell))
        orbit = {
            transform_h4(seed, action, permutation)
            for action in ACTIONS
            for permutation in S4
        }
        orbit_id = len(rows)
        for cell in orbit:
            cell_to_orbit[cell] = orbit_id
        rows.append(
            {
                "id": orbit_id,
                "size": len(orbit),
                "family": conductor_family(seed),
                "representative": "(" + ", ".join(label_name(label) for label in seed) + ")",
            }
        )
        remaining -= orbit
    return cell_to_orbit, rows


def contract_pair(cell: Cell4, pair: tuple[int, int]) -> Cell3 | None:
    i, j = pair
    merged = add_label(cell[i], cell[j])
    if merged == (0, 0):
        return None
    rest = [cell[index] for index in range(4) if index not in pair]
    return (merged, rest[0], rest[1])


def compute_summary() -> dict[str, object]:
    h3_cell_to_orbit, h3_rows = orbit_maps_h3()
    h4_cell_to_orbit, h4_rows = orbit_maps_h4()
    cells4 = h4_cells(distinct=False)

    candidate_count = 0
    valid_count = 0
    invalid_zero_merge = 0
    incidence: dict[int, Counter[int]] = defaultdict(Counter)
    h3_preimages: dict[int, Counter[int]] = defaultdict(Counter)
    pair_position_counts: Counter[str] = Counter()
    transition_counts: Counter[tuple[str, str]] = Counter()
    family_transition_counts: Counter[tuple[str, str]] = Counter()

    for cell in cells4:
        h4_orbit = h4_cell_to_orbit[cell]
        h4_family = h4_rows[h4_orbit]["family"]
        for pair in combinations(range(4), 2):
            candidate_count += 1
            contracted = contract_pair(cell, pair)
            if contracted is None:
                invalid_zero_merge += 1
                continue
            valid_count += 1
            h3_orbit = h3_cell_to_orbit[contracted]
            h3_family = h3_rows[h3_orbit]["family"]
            incidence[h4_orbit][h3_orbit] += 1
            h3_preimages[h3_orbit][h4_orbit] += 1
            pair_position_counts[f"{pair[0]}{pair[1]}"] += 1
            transition_counts[(conductor_word(cell), conductor_word(contracted))] += 1
            family_transition_counts[(h4_family, h3_family)] += 1

    orbit_rows = []
    for row in h4_rows:
        oid = row["id"]
        image_counter = incidence.get(oid, Counter())
        orbit_rows.append(
            {
                **row,
                "valid_contractions": sum(image_counter.values()),
                "h3_images": [
                    {
                        "h3_orbit": h3_id,
                        "h3_family": h3_rows[h3_id]["family"],
                        "count": count,
                    }
                    for h3_id, count in sorted(image_counter.items())
                ],
            }
        )

    h3_rows_out = []
    for row in h3_rows:
        oid = row["id"]
        preimage_counter = h3_preimages.get(oid, Counter())
        h3_rows_out.append(
            {
                **row,
                "preimage_h4_orbits": len(preimage_counter),
                "valid_contractions_received": sum(preimage_counter.values()),
                "h4_preimages": [
                    {
                        "h4_orbit": h4_id,
                        "h4_family": h4_rows[h4_id]["family"],
                        "count": count,
                    }
                    for h4_id, count in sorted(preimage_counter.items())
                ],
            }
        )

    return {
        "ring": "F4[u]/(u^2)",
        "h4_cells": len(cells4),
        "h4_orbits": len(h4_rows),
        "h3_cells": len(h3_cells()),
        "h3_orbits": len(h3_rows),
        "candidate_pair_contractions": candidate_count,
        "valid_nonzero_contractions": valid_count,
        "invalid_zero_merge_contractions": invalid_zero_merge,
        "h3_orbits_hit": sorted(set(h3_preimages)),
        "h3_orbits_hit_count": len(h3_preimages),
        "h4_orbits_with_valid_contractions": sum(
            1 for counter in incidence.values() if sum(counter.values()) > 0
        ),
        "pair_position_counts": dict(sorted(pair_position_counts.items())),
        "conductor_word_transitions": {
            f"{src}->{dst}": count for (src, dst), count in sorted(transition_counts.items())
        },
        "family_transitions": {
            f"{src}->{dst}": count
            for (src, dst), count in sorted(family_transition_counts.items())
        },
        "h4_orbit_rows": orbit_rows,
        "h3_orbit_rows": h3_rows_out,
    }


def main() -> None:
    summary = compute_summary()
    out_path = Path(__file__).with_name("reports") / "h4_to_h3_contractions.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
