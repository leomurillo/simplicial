"""Hyper-adjacency tower over a local adjacency constructor.

This is the layer after FisherJet: it packages the arity-n closed cells,
normalizer/symmetric orbits, and contraction maps that should eventually carry
the operadic structure of the quotient-character tower.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from local_adjacency_constructor import Label, LocalAdjacencyConstructor


Cell = tuple[Label, ...]


class HyperAdjacencyTower:
    """Arity-n support cells and contraction incidence over one constructor."""

    def __init__(self, constructor: LocalAdjacencyConstructor) -> None:
        self.constructor = constructor
        self.ring = constructor.ring

    def cells(self, arity: int) -> tuple[Cell, ...]:
        return self.constructor.closed_cells(arity)

    def orbit_maps(self, arity: int) -> tuple[dict[Cell, int], list[dict[str, object]]]:
        cell_to_orbit: dict[Cell, int] = {}
        rows: list[dict[str, object]] = []
        orbits = self.constructor.tuple_orbits(self.cells(arity))

        for orbit_id, orbit in enumerate(orbits):
            seed = min(orbit, key=self.constructor.tuple_name)
            for cell in orbit:
                cell_to_orbit[cell] = orbit_id
            rows.append(
                {
                    "id": orbit_id,
                    "arity": arity,
                    "size": len(orbit),
                    "family": self.constructor.conductor_family(seed),
                    "representative_cell": seed,
                    "representative": "("
                    + ", ".join(self.ring.label_name(label) for label in seed)
                    + ")",
                }
            )
        return cell_to_orbit, rows

    def contract_pair(self, cell: Cell, pair: tuple[int, int]) -> Cell | None:
        i, j = pair
        merged = self.ring.add(cell[i], cell[j])
        if merged == self.ring.zero:
            return None
        rest = [cell[index] for index in range(len(cell)) if index not in pair]
        return (merged, *rest)

    def pair_contraction_summary(self, arity: int) -> dict[str, object]:
        """Summarize all pair contractions H^(arity) -> H^(arity-1)."""

        if arity < 3:
            raise ValueError("pair contractions require arity >= 3")

        source_cell_to_orbit, source_rows = self.orbit_maps(arity)
        target_cell_to_orbit, target_rows = self.orbit_maps(arity - 1)
        source_cells = self.cells(arity)

        candidate_count = 0
        valid_count = 0
        invalid_zero_merge = 0
        incidence: dict[int, Counter[int]] = defaultdict(Counter)
        target_preimages: dict[int, Counter[int]] = defaultdict(Counter)
        pair_position_counts: Counter[str] = Counter()
        family_transition_counts: Counter[tuple[str, str]] = Counter()

        for cell in source_cells:
            source_orbit = source_cell_to_orbit[cell]
            source_family = source_rows[source_orbit]["family"]
            for pair in combinations(range(arity), 2):
                candidate_count += 1
                contracted = self.contract_pair(cell, pair)
                if contracted is None:
                    invalid_zero_merge += 1
                    continue
                valid_count += 1
                target_orbit = target_cell_to_orbit[contracted]
                target_family = target_rows[target_orbit]["family"]
                incidence[source_orbit][target_orbit] += 1
                target_preimages[target_orbit][source_orbit] += 1
                pair_position_counts[f"{pair[0]}{pair[1]}"] += 1
                family_transition_counts[(source_family, target_family)] += 1

        source_orbit_rows = []
        for row in source_rows:
            source_orbit = int(row["id"])
            image_counter = incidence.get(source_orbit, Counter())
            source_orbit_rows.append(
                {
                    **row,
                    "valid_contractions": sum(image_counter.values()),
                    "target_images": [
                        {
                            "target_orbit": target_id,
                            "target_family": target_rows[target_id]["family"],
                            "count": count,
                        }
                        for target_id, count in sorted(image_counter.items())
                    ],
                }
            )

        target_orbit_rows = []
        for row in target_rows:
            target_orbit = int(row["id"])
            preimage_counter = target_preimages.get(target_orbit, Counter())
            target_orbit_rows.append(
                {
                    **row,
                    "preimage_source_orbits": len(preimage_counter),
                    "valid_contractions_received": sum(preimage_counter.values()),
                    "source_preimages": [
                        {
                            "source_orbit": source_id,
                            "source_family": source_rows[source_id]["family"],
                            "count": count,
                        }
                        for source_id, count in sorted(preimage_counter.items())
                    ],
                }
            )

        return {
            "ring": self.ring.name,
            "source_arity": arity,
            "target_arity": arity - 1,
            "source_cells": len(source_cells),
            "target_cells": len(self.cells(arity - 1)),
            "source_orbits": len(source_rows),
            "target_orbits": len(target_rows),
            "candidate_pair_contractions": candidate_count,
            "valid_nonzero_contractions": valid_count,
            "invalid_zero_merge_contractions": invalid_zero_merge,
            "target_orbits_hit": sorted(set(target_preimages)),
            "target_orbits_hit_count": len(target_preimages),
            "source_orbits_with_valid_contractions": sum(
                1 for counter in incidence.values() if sum(counter.values()) > 0
            ),
            "pair_position_counts": dict(sorted(pair_position_counts.items())),
            "family_transitions": {
                f"{source}->{target}": count
                for (source, target), count in sorted(family_transition_counts.items())
            },
            "source_orbit_rows": source_orbit_rows,
            "target_orbit_rows": target_orbit_rows,
        }
