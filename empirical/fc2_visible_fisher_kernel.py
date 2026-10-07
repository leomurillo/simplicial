"""Visible Fisher-jet kernel classifier for FC2 row classification.

This is the second FC2 classifier layer after `fc2_row_classifier.py`.
It does not re-open the FC2 source theorem.  The source object remains the
filtered section class `[kappa_R]`; this script asks what the tested cubic
Fisher-jet channel sees:

* conductor-mixed K_CH commutator support under `FisherJet`;
* input-side H4 lift support for those commutator orbits;
* deterministic gate/profile data for rows too large for exact extraction.

The raw-support projection is kept separate.  It is not the K_CH map.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from time import perf_counter
from typing import Any, Callable, Iterable

from fisher_jet_functor import FisherJet
from hyper_adjacency_tower import HyperAdjacencyTower
from local_adjacency_constructor import (
    FiniteLocalRing,
    Label,
    LocalAdjacencyConstructor,
    make_f16_ring,
    make_f2_u4_ring,
    make_f2_u5_ring,
    make_f4_u2_ring,
    make_f8_u2_ring,
)


REPORT_DIR = Path(__file__).with_name("reports")
DEFAULT_JSON = REPORT_DIR / "fc2_visible_fisher_kernel.json"
DEFAULT_MD = REPORT_DIR / "fc2_visible_fisher_kernel.md"
ROW_CLASSIFICATION_JSON = REPORT_DIR / "fc2_row_classification.json"

ROW_FACTORIES: dict[str, Callable[[], FiniteLocalRing]] = {
    "f4-u2": make_f4_u2_ring,
    "f2-u5": make_f2_u5_ring,
    "f8-u2": make_f8_u2_ring,
    "f16-field": make_f16_ring,
    "f2-u4-control": make_f2_u4_ring,
}

EXECUTION_NOTES: dict[str, list[str]] = {
    "f2-u5": [
        (
            "2026-05-14 pre-streaming forced exact run timed out after 900 "
            "seconds.  After the streaming orbit canonicalizer was added, "
            "`--force-exact f2-u5` completed exactly; the combined report "
            "records the current timing."
        )
    ],
    "f8-u2": [
        (
            "2026-05-14 pre-sparse forced exact runs timed out after 900 "
            "seconds.  After the sparse commutator formula and support-set "
            "orbiting path were added, `--force-exact f8-u2` completed exactly; "
            "the combined report records the current timing."
        )
    ]
}

Key = tuple[int, int, int, int, int, int]
POSITIONS = ("left_mode", "right_mode", "alpha", "beta", "input", "output")
INPUT_SIDE = ((0, 1, 2, 4), (0, 1, 3, 4))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def counter_json(counter: Counter[Any]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter, key=str)}


def load_row_classification() -> dict[str, dict[str, Any]]:
    if not ROW_CLASSIFICATION_JSON.exists():
        return {}
    payload = json.loads(ROW_CLASSIFICATION_JSON.read_text(encoding="utf-8"))
    return {row["row_key"]: row for row in payload.get("rows", [])}


def encoded_action_maps(constructor: LocalAdjacencyConstructor) -> tuple[tuple[int, ...], ...]:
    ring = constructor.ring
    return tuple(
        tuple(ring.label_index[ring.apply(action, label)] for label in ring.labels)
        for action in ring.normalizer_actions
    )


def encoded_addition_table(constructor: LocalAdjacencyConstructor) -> tuple[tuple[int, ...], ...]:
    ring = constructor.ring
    return tuple(
        tuple(ring.label_index[ring.add(left, right)] for right in ring.labels)
        for left in ring.labels
    )


def label_name(constructor: LocalAdjacencyConstructor, index: int) -> str:
    return constructor.ring.label_name(constructor.ring.labels[index])


def key_json(constructor: LocalAdjacencyConstructor, key: Key) -> dict[str, str]:
    return {
        position: label_name(constructor, index)
        for position, index in zip(POSITIONS, key, strict=True)
    }


def cell_text(constructor: LocalAdjacencyConstructor, cell: tuple[Label, ...]) -> str:
    return "(" + ", ".join(constructor.ring.label_name(label) for label in cell) + ")"


def mixed_packet_pairs(
    constructor: LocalAdjacencyConstructor,
) -> list[tuple[str, str, tuple[Label, ...], tuple[Label, ...]]]:
    packets = list(constructor.packets.items())
    pairs: list[tuple[str, str, tuple[Label, ...], tuple[Label, ...]]] = []
    for left_index, (left_conductor, left_modes) in enumerate(packets):
        for right_conductor, right_modes in packets[left_index + 1 :]:
            pairs.append((left_conductor, right_conductor, left_modes, right_modes))
    return pairs


def candidate_profile(
    constructor: LocalAdjacencyConstructor,
    left_modes: tuple[Label, ...],
    right_modes: tuple[Label, ...],
) -> dict[str, int]:
    mode_pair_count = len(left_modes) * len(right_modes)
    nontrivial = len(constructor.ring.nontrivial)
    tangent_operator_pairs = nontrivial * (nontrivial - 1)
    return {
        "left_mode_count": len(left_modes),
        "right_mode_count": len(right_modes),
        "mode_pair_count": mode_pair_count,
        "tangent_operator_pairs_per_mode_pair": tangent_operator_pairs,
        "candidate_tangent_products": mode_pair_count * tangent_operator_pairs,
    }


def iter_mode_pair_samples(
    left_modes: tuple[Label, ...],
    right_modes: tuple[Label, ...],
    limit: int,
) -> Iterable[tuple[Label, Label]]:
    emitted = 0
    for left_mode in left_modes:
        for right_mode in right_modes:
            if emitted >= limit:
                return
            emitted += 1
            yield left_mode, right_mode


def commutator_keys_for_modes(
    constructor: LocalAdjacencyConstructor,
    jet: FisherJet,
    left_modes: Iterable[Label],
    right_modes: Iterable[Label],
    *,
    add_table: tuple[tuple[int, ...], ...] | None = None,
    nontrivial_indices: tuple[int, ...] | None = None,
) -> tuple[set[Key], Counter[str], int]:
    ring = constructor.ring
    key_set: set[Key] = set()
    coefficients: Counter[str] = Counter()
    entry_count = 0
    index = ring.label_index
    zero = index[ring.zero]
    if add_table is None:
        add_table = encoded_addition_table(constructor)
    if nontrivial_indices is None:
        nontrivial_indices = tuple(index[label] for label in ring.nontrivial)

    for left_mode in left_modes:
        left_mode_index = index[left_mode]
        for right_mode in right_modes:
            right_mode_index = index[right_mode]
            mode_sum = add_table[left_mode_index][right_mode_index]
            for alpha_index in nontrivial_indices:
                for beta_index in nontrivial_indices:
                    if add_table[alpha_index][beta_index] == zero:
                        continue
                    entries = [
                        (alpha_index, add_table[mode_sum][beta_index], "-1"),
                        (beta_index, add_table[mode_sum][alpha_index], "1"),
                    ]
                    for output, input_label, coefficient in entries:
                        if input_label == zero:
                            continue
                        entry_count += 1
                        coefficients[coefficient] += 1
                        key_set.add(
                            (
                                left_mode_index,
                                right_mode_index,
                                alpha_index,
                                beta_index,
                                input_label,
                                output,
                            )
                        )
    return key_set, coefficients, entry_count


def profile_packet_pair_samples(
    constructor: LocalAdjacencyConstructor,
    jet: FisherJet,
    left_modes: tuple[Label, ...],
    right_modes: tuple[Label, ...],
    sample_mode_pairs: int,
    add_table: tuple[tuple[int, ...], ...] | None = None,
    nontrivial_indices: tuple[int, ...] | None = None,
) -> list[dict[str, Any]]:
    samples: list[dict[str, Any]] = []
    for left_mode, right_mode in iter_mode_pair_samples(
        left_modes,
        right_modes,
        sample_mode_pairs,
    ):
        started = perf_counter()
        keys, coefficients, entry_count = commutator_keys_for_modes(
            constructor,
            jet,
            (left_mode,),
            (right_mode,),
            add_table=add_table,
            nontrivial_indices=nontrivial_indices,
        )
        samples.append(
            {
                "left_mode": constructor.ring.label_name(left_mode),
                "right_mode": constructor.ring.label_name(right_mode),
                "commutator_entries": entry_count,
                "unique_support_keys": len(keys),
                "coefficient_distribution": counter_json(coefficients),
                "elapsed_seconds": round(perf_counter() - started, 3),
            }
        )
    return samples


def first_order_map_index(
    *,
    mode: int,
    gamma: int,
    zero: int,
    add_table: tuple[tuple[int, ...], ...],
) -> tuple[int, int] | None:
    if gamma == zero:
        return mode, -2
    output = add_table[mode][gamma]
    if output == zero:
        return None
    return output, -1


def mixed_second_order_map_index(
    *,
    left_mode: int,
    right_mode: int,
    gamma: int,
    zero: int,
    add_table: tuple[tuple[int, ...], ...],
) -> tuple[int, int] | None:
    if gamma == left_mode:
        return right_mode, 3
    if gamma == right_mode:
        return left_mode, 3
    output = add_table[add_table[left_mode][right_mode]][gamma]
    if output == zero:
        return None
    return output, 2


def direct_mixed_product_entries(
    *,
    alpha: int,
    beta: int,
    left_mode: int,
    right_mode: int,
    zero: int,
    nontrivial_indices: tuple[int, ...],
    add_table: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, int], int]:
    entries: dict[tuple[int, int], int] = {}

    for input_index in nontrivial_indices:
        # M_alpha O_beta
        middle = add_table[beta][input_index]
        if middle != zero:
            gamma = add_table[alpha][middle]
            mapped = mixed_second_order_map_index(
                left_mode=left_mode,
                right_mode=right_mode,
                gamma=gamma,
                zero=zero,
                add_table=add_table,
            )
            if mapped is not None:
                output, coefficient = mapped
                entries[(output, input_index)] = entries.get((output, input_index), 0) + coefficient

        # L_alpha R_beta
        gamma = add_table[beta][input_index]
        right = first_order_map_index(
            mode=right_mode,
            gamma=gamma,
            zero=zero,
            add_table=add_table,
        )
        if right is not None:
            middle, right_coefficient = right
            gamma = add_table[alpha][middle]
            left = first_order_map_index(
                mode=left_mode,
                gamma=gamma,
                zero=zero,
                add_table=add_table,
            )
            if left is not None:
                output, left_coefficient = left
                entries[(output, input_index)] = (
                    entries.get((output, input_index), 0)
                    + right_coefficient * left_coefficient
                )

        # R_alpha L_beta
        gamma = add_table[beta][input_index]
        left = first_order_map_index(
            mode=left_mode,
            gamma=gamma,
            zero=zero,
            add_table=add_table,
        )
        if left is not None:
            middle, left_coefficient = left
            gamma = add_table[alpha][middle]
            right = first_order_map_index(
                mode=right_mode,
                gamma=gamma,
                zero=zero,
                add_table=add_table,
            )
            if right is not None:
                output, right_coefficient = right
                entries[(output, input_index)] = (
                    entries.get((output, input_index), 0)
                    + left_coefficient * right_coefficient
                )

        # O_alpha M_beta
        gamma = add_table[beta][input_index]
        mixed = mixed_second_order_map_index(
            left_mode=left_mode,
            right_mode=right_mode,
            gamma=gamma,
            zero=zero,
            add_table=add_table,
        )
        if mixed is not None:
            middle, mixed_coefficient = mixed
            output = add_table[alpha][middle]
            if output != zero:
                entries[(output, input_index)] = (
                    entries.get((output, input_index), 0) + mixed_coefficient
                )

    return {key: value for key, value in entries.items() if value}


def direct_mixed_commutator_entries(
    *,
    alpha: int,
    beta: int,
    left_mode: int,
    right_mode: int,
    zero: int,
    nontrivial_indices: tuple[int, ...],
    add_table: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, int], Fraction]:
    left_product = direct_mixed_product_entries(
        alpha=alpha,
        beta=beta,
        left_mode=left_mode,
        right_mode=right_mode,
        zero=zero,
        nontrivial_indices=nontrivial_indices,
        add_table=add_table,
    )
    right_product = direct_mixed_product_entries(
        alpha=beta,
        beta=alpha,
        left_mode=left_mode,
        right_mode=right_mode,
        zero=zero,
        nontrivial_indices=nontrivial_indices,
        add_table=add_table,
    )
    entries: dict[tuple[int, int], Fraction] = {}
    for key in set(left_product) | set(right_product):
        value = left_product.get(key, 0) - right_product.get(key, 0)
        if value:
            entries[key] = Fraction(value, 2)
    return entries


def orbit_decomposition(
    keys: set[Key],
    action_maps: tuple[tuple[int, ...], ...],
) -> tuple[dict[Key, int], list[dict[str, Any]]]:
    remaining = set(keys)
    key_to_orbit: dict[Key, int] = {}
    rows: list[dict[str, Any]] = []

    while remaining:
        seed = min(remaining)
        ambient = {
            tuple(action_map[index] for index in seed)
            for action_map in action_maps
        }
        present = ambient & keys
        orbit_id = len(rows)
        representative = min(present)
        for key in present:
            key_to_orbit[key] = orbit_id
        rows.append(
            {
                "id": orbit_id,
                "representative": representative,
                "size": len(present),
                "ambient_size": len(ambient),
                "missing": len(ambient - keys),
            }
        )
        remaining -= present

    return key_to_orbit, rows


def is_pure_family(family: object) -> bool:
    text = str(family)
    return len(set(text)) == 1


def projection_summary(
    constructor: LocalAdjacencyConstructor,
    *,
    keys: set[Key],
    key_to_h2_orbit: dict[Key, int],
    cell_to_h4_orbit: dict[tuple[Label, ...], int],
    h4_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    labels = constructor.ring.labels
    ring = constructor.ring

    h2_orbits: set[int] = set()
    h4_to_h2: dict[int, set[int]] = defaultdict(set)
    h2_to_h4: dict[int, set[int]] = defaultdict(set)
    h4_entry_hits: Counter[int] = Counter()
    family_entry_hits: Counter[str] = Counter()
    closed_hits = 0

    for key in keys:
        h2_orbit = key_to_h2_orbit[key]
        for projection in INPUT_SIDE:
            cell = tuple(labels[key[index]] for index in projection)
            if ring.add_many(cell) != ring.zero:
                continue
            h4_orbit = cell_to_h4_orbit[cell]
            h2_orbits.add(h2_orbit)
            h4_to_h2[h4_orbit].add(h2_orbit)
            h2_to_h4[h2_orbit].add(h4_orbit)
            h4_entry_hits[h4_orbit] += 1
            family_entry_hits[str(h4_rows[h4_orbit]["family"])] += 1
            closed_hits += 1

    family_orbit_counts = Counter(str(row["family"]) for row in h4_rows)
    hit_family_orbit_counts = Counter(
        str(h4_rows[orbit_id]["family"]) for orbit_id in h4_to_h2
    )
    pure_total = sum(
        count for family, count in family_orbit_counts.items() if is_pure_family(family)
    )
    pure_hit = sum(
        count for family, count in hit_family_orbit_counts.items() if is_pure_family(family)
    )
    mixed_total = len(h4_rows) - pure_total
    mixed_hit = len(h4_to_h2) - pure_hit

    image_table = []
    for orbit_id in sorted(
        h4_to_h2,
        key=lambda oid: (
            str(h4_rows[oid]["family"]),
            int(h4_rows[oid]["size"]),
            oid,
        ),
    ):
        row = h4_rows[orbit_id]
        representative_cell = row.get("representative_cell")
        representative = row.get("representative")
        if representative is None and representative_cell is not None:
            representative = cell_text(constructor, representative_cell)
        image_table.append(
            {
                "h4_orbit": orbit_id,
                "family": str(row["family"]),
                "size": int(row["size"]),
                "h2_commutator_orbits": len(h4_to_h2[orbit_id]),
                "entry_hits": h4_entry_hits[orbit_id],
                "representative": str(representative),
            }
        )

    return {
        "lifted_commutator_orbits": len(h2_orbits),
        "h4_orbits_hit": len(h4_to_h2),
        "closed_input_side_hits": closed_hits,
        "h2_to_h4_multiplicity": counter_json(
            Counter(len(ids) for ids in h2_to_h4.values())
        ),
        "h4_family_orbits_total": counter_json(family_orbit_counts),
        "h4_family_orbits_hit": counter_json(hit_family_orbit_counts),
        "h4_entry_hits_by_family": counter_json(family_entry_hits),
        "mixed_h4_orbits_hit": mixed_hit,
        "mixed_h4_orbits_total": mixed_total,
        "pure_h4_orbits_hit": pure_hit,
        "pure_h4_orbits_total": pure_total,
        "h4_orbit_image_table": image_table,
    }


def canonical_key(
    key: Key,
    action_maps: tuple[tuple[int, ...], ...],
) -> Key:
    return min(
        tuple(action_map[index] for index in key)
        for action_map in action_maps
    )


def ambient_orbit_size(
    key: Key,
    action_maps: tuple[tuple[int, ...], ...],
) -> int:
    return len(
        {
            tuple(action_map[index] for index in key)
            for action_map in action_maps
        }
    )


def empty_lift_accumulator() -> dict[str, Any]:
    return {
        "h2_orbits": set(),
        "h4_to_h2": defaultdict(set),
        "h2_to_h4": defaultdict(set),
        "h4_entry_hits": Counter(),
        "family_entry_hits": Counter(),
        "closed_hits": 0,
    }


def record_input_side_lift(
    accumulator: dict[str, Any],
    *,
    constructor: LocalAdjacencyConstructor,
    key: Key,
    orbit_key: Key,
    cell_to_h4_orbit: dict[tuple[Label, ...], int],
    h4_rows: list[dict[str, Any]],
) -> None:
    labels = constructor.ring.labels
    ring = constructor.ring
    for projection in INPUT_SIDE:
        cell = tuple(labels[key[index]] for index in projection)
        if ring.add_many(cell) != ring.zero:
            continue
        h4_orbit = cell_to_h4_orbit[cell]
        accumulator["h2_orbits"].add(orbit_key)
        accumulator["h4_to_h2"][h4_orbit].add(orbit_key)
        accumulator["h2_to_h4"][orbit_key].add(h4_orbit)
        accumulator["h4_entry_hits"][h4_orbit] += 1
        accumulator["family_entry_hits"][str(h4_rows[h4_orbit]["family"])] += 1
        accumulator["closed_hits"] += 1


def summarize_lift_accumulator(
    constructor: LocalAdjacencyConstructor,
    accumulator: dict[str, Any],
    h4_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    h4_to_h2: dict[int, set[Key]] = accumulator["h4_to_h2"]
    h2_to_h4: dict[Key, set[int]] = accumulator["h2_to_h4"]
    h4_entry_hits: Counter[int] = accumulator["h4_entry_hits"]
    family_entry_hits: Counter[str] = accumulator["family_entry_hits"]

    family_orbit_counts = Counter(str(row["family"]) for row in h4_rows)
    hit_family_orbit_counts = Counter(
        str(h4_rows[orbit_id]["family"]) for orbit_id in h4_to_h2
    )
    pure_total = sum(
        count for family, count in family_orbit_counts.items() if is_pure_family(family)
    )
    pure_hit = sum(
        count for family, count in hit_family_orbit_counts.items() if is_pure_family(family)
    )
    mixed_total = len(h4_rows) - pure_total
    mixed_hit = len(h4_to_h2) - pure_hit

    image_table = []
    for orbit_id in sorted(
        h4_to_h2,
        key=lambda oid: (
            str(h4_rows[oid]["family"]),
            int(h4_rows[oid]["size"]),
            oid,
        ),
    ):
        row = h4_rows[orbit_id]
        representative_cell = row.get("representative_cell")
        representative = row.get("representative")
        if representative is None and representative_cell is not None:
            representative = cell_text(constructor, representative_cell)
        image_table.append(
            {
                "h4_orbit": orbit_id,
                "family": str(row["family"]),
                "size": int(row["size"]),
                "h2_commutator_orbits": len(h4_to_h2[orbit_id]),
                "entry_hits": h4_entry_hits[orbit_id],
                "representative": str(representative),
            }
        )

    return {
        "lifted_commutator_orbits": len(accumulator["h2_orbits"]),
        "h4_orbits_hit": len(h4_to_h2),
        "closed_input_side_hits": int(accumulator["closed_hits"]),
        "h2_to_h4_multiplicity": counter_json(
            Counter(len(ids) for ids in h2_to_h4.values())
        ),
        "h4_family_orbits_total": counter_json(family_orbit_counts),
        "h4_family_orbits_hit": counter_json(hit_family_orbit_counts),
        "h4_entry_hits_by_family": counter_json(family_entry_hits),
        "mixed_h4_orbits_hit": mixed_hit,
        "mixed_h4_orbits_total": mixed_total,
        "pure_h4_orbits_hit": pure_hit,
        "pure_h4_orbits_total": pure_total,
        "h4_orbit_image_table": image_table,
    }


def orbit_lift_summary_from_keys(
    constructor: LocalAdjacencyConstructor,
    *,
    keys: set[Key],
    action_maps: tuple[tuple[int, ...], ...],
    h4_rows: list[dict[str, Any]],
    cell_to_h4_orbit: dict[tuple[Label, ...], int],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    remaining = set(keys)
    orbit_rows: list[dict[str, Any]] = []
    lift = empty_lift_accumulator()

    while remaining:
        seed = next(iter(remaining))
        ambient = {
            tuple(action_map[index] for index in seed)
            for action_map in action_maps
        }
        present = ambient & keys
        orbit_id = len(orbit_rows)
        representative = min(present)
        for key in present:
            record_input_side_lift(
                lift,
                constructor=constructor,
                key=key,
                orbit_key=orbit_id,
                cell_to_h4_orbit=cell_to_h4_orbit,
                h4_rows=h4_rows,
            )
        orbit_rows.append(
            {
                "id": orbit_id,
                "representative": representative,
                "size": len(present),
                "ambient_size": len(ambient),
                "missing": len(ambient - keys),
            }
        )
        remaining -= present

    orbit_rows.sort(key=lambda row: row["representative"])
    for orbit_id, row in enumerate(orbit_rows):
        row["id"] = orbit_id
    return orbit_rows, summarize_lift_accumulator(constructor, lift, h4_rows)


def exact_visible_shadow(
    constructor: LocalAdjacencyConstructor,
    packet_profiles: list[dict[str, Any]],
) -> dict[str, Any]:
    jet = FisherJet(constructor)
    action_maps = encoded_action_maps(constructor)
    add_table = encoded_addition_table(constructor)
    nontrivial_indices = tuple(
        constructor.ring.label_index[label] for label in constructor.ring.nontrivial
    )
    tower = HyperAdjacencyTower(constructor)
    h4_started = perf_counter()
    cell_to_h4_orbit, h4_rows = tower.orbit_maps(4)
    h4_elapsed = perf_counter() - h4_started

    packet_pair_keys: dict[str, set[Key]] = {}
    packet_pair_coefficients: dict[str, Counter[str]] = {}
    packet_pair_entries: dict[str, int] = {}
    all_keys: set[Key] = set()
    all_coefficients: Counter[str] = Counter()
    started = perf_counter()

    for profile in packet_profiles:
        left_conductor = profile["left_conductor"]
        right_conductor = profile["right_conductor"]
        left_modes = constructor.packets[left_conductor]
        right_modes = constructor.packets[right_conductor]
        pair_key = f"{left_conductor}|{right_conductor}"
        keys, coefficients, entry_count = commutator_keys_for_modes(
            constructor,
            jet,
            left_modes,
            right_modes,
            add_table=add_table,
            nontrivial_indices=nontrivial_indices,
        )
        packet_pair_keys[pair_key] = keys
        packet_pair_coefficients[pair_key] = coefficients
        packet_pair_entries[pair_key] = entry_count
        all_keys |= keys
        all_coefficients.update(coefficients)

    witness_elapsed = perf_counter() - started
    orbit_started = perf_counter()
    orbit_rows, lift = orbit_lift_summary_from_keys(
        constructor,
        keys=all_keys,
        action_maps=action_maps,
        h4_rows=h4_rows,
        cell_to_h4_orbit=cell_to_h4_orbit,
    )
    orbit_elapsed = perf_counter() - orbit_started

    packet_pair_rows = []
    for profile in packet_profiles:
        pair_key = f"{profile['left_conductor']}|{profile['right_conductor']}"
        pair_orbit_rows, pair_lift = orbit_lift_summary_from_keys(
            constructor,
            keys=packet_pair_keys[pair_key],
            action_maps=action_maps,
            h4_rows=h4_rows,
            cell_to_h4_orbit=cell_to_h4_orbit,
        )
        packet_pair_rows.append(
            {
                **profile,
                "commutator_entries": packet_pair_entries[pair_key],
                "unique_support_keys": len(packet_pair_keys[pair_key]),
                "commutator_orbits": len(pair_orbit_rows),
                "coefficient_distribution": counter_json(
                    packet_pair_coefficients[pair_key]
                ),
                "input_side_h4_lift": {
                    key: pair_lift[key]
                    for key in [
                        "lifted_commutator_orbits",
                        "h4_orbits_hit",
                        "closed_input_side_hits",
                        "h4_family_orbits_hit",
                        "h4_entry_hits_by_family",
                        "mixed_h4_orbits_hit",
                        "mixed_h4_orbits_total",
                        "pure_h4_orbits_hit",
                        "pure_h4_orbits_total",
                    ]
                },
            }
        )

    representative_orbits = [
        {
            "id": int(row["id"]),
            "representative": key_json(constructor, row["representative"]),
            "size": int(row["size"]),
            "ambient_size": int(row["ambient_size"]),
            "missing": int(row["missing"]),
        }
        for row in orbit_rows[:20]
    ]

    return {
        "status": "exact",
        "commutator_entries": sum(packet_pair_entries.values()),
        "unique_support_keys": len(all_keys),
        "commutator_orbits": len(orbit_rows),
        "commutator_orbit_size_distribution": counter_json(
            Counter(int(row["size"]) for row in orbit_rows)
        ),
        "coefficient_distribution": counter_json(all_coefficients),
        "representative_commutator_orbits_sample": representative_orbits,
        "input_side_h4_lift": lift,
        "packet_pair_rows": packet_pair_rows,
        "timing_seconds": {
            "witness_generation": round(witness_elapsed, 3),
            "commutator_orbits": round(orbit_elapsed, 3),
            "h4_orbits": round(h4_elapsed, 3),
        },
    }


def profile_row(
    row_key: str,
    constructor: LocalAdjacencyConstructor,
    *,
    sample_mode_pairs: int,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    jet = FisherJet(constructor)
    add_table = encoded_addition_table(constructor)
    nontrivial_indices = tuple(
        constructor.ring.label_index[label] for label in constructor.ring.nontrivial
    )
    packet_profiles: list[dict[str, Any]] = []
    totals = Counter()

    for left_conductor, right_conductor, left_modes, right_modes in mixed_packet_pairs(
        constructor
    ):
        profile = {
            "left_conductor": left_conductor,
            "right_conductor": right_conductor,
            **candidate_profile(constructor, left_modes, right_modes),
        }
        if sample_mode_pairs > 0:
            samples = profile_packet_pair_samples(
                constructor,
                jet,
                left_modes,
                right_modes,
                sample_mode_pairs,
                add_table=add_table,
                nontrivial_indices=nontrivial_indices,
            )
            profile["sample_mode_pairs"] = samples
            if samples:
                average_entries = sum(
                    sample["commutator_entries"] for sample in samples
                ) / len(samples)
                profile["sample_scaled_commutator_entry_estimate"] = round(
                    average_entries * profile["mode_pair_count"]
                )
        packet_profiles.append(profile)
        totals["mode_pair_count"] += profile["mode_pair_count"]
        totals["candidate_tangent_products"] += profile["candidate_tangent_products"]

    return packet_profiles, dict(totals)


def residual_accounting(
    row_key: str,
    row_classifications: dict[str, dict[str, Any]],
    shadow_status: str,
    commutator_orbits: int | None,
) -> dict[str, Any]:
    row = row_classifications.get(row_key, {})
    classification = row.get("classification", {})
    full_residual = classification.get("full_filtered_residual")
    support_residual = classification.get("support_projection_residual")
    erased = classification.get("support_projection_erased_from_full")
    visible_shadow = bool(commutator_orbits and commutator_orbits > 0)
    return {
        "full_filtered_residual_atoms": full_residual,
        "raw_support_projection_residual": support_residual,
        "raw_support_erased_atoms": erased,
        "visible_fisher_shadow_present": visible_shadow,
        "tested_fisher_channel": "conductor-mixed K_CH commutator with input-side H4 lift",
        "atom_resolution_status": (
            "not atom-resolved: K_CH/H4 is a Fisher-jet shadow of [kappa], "
            "not a standalone Ext_CH atom detector"
        ),
        "atom_level_visible_count": None,
        "atom_level_invisible_count": None,
        "unresolved_filtered_atoms_for_atom_level_visibility": full_residual,
        "shadow_status": shadow_status,
    }


def analyze_row(
    row_key: str,
    *,
    max_exact_mode_pairs: int,
    max_exact_candidate_products: int,
    force_exact: set[str],
    sample_mode_pairs: int,
    row_classifications: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    constructor = LocalAdjacencyConstructor(ROW_FACTORIES[row_key]())
    packet_profiles, totals = profile_row(
        row_key,
        constructor,
        sample_mode_pairs=sample_mode_pairs,
    )
    packet_sizes = {name: len(labels) for name, labels in constructor.packets.items()}
    eligibility = {
        "mixed_packet_pairs": len(packet_profiles),
        "conductor_mixed_mode_pairs": totals.get("mode_pair_count", 0),
        "candidate_tangent_products": totals.get("candidate_tangent_products", 0),
        "max_exact_mode_pairs": max_exact_mode_pairs,
        "max_exact_candidate_products": max_exact_candidate_products,
        "forced_exact": row_key in force_exact,
    }

    if not packet_profiles:
        shadow = {
            "status": "empty",
            "reason": "one conductor packet only; no conductor-mixed K_CH mode pairs",
            "commutator_entries": 0,
            "unique_support_keys": 0,
            "commutator_orbits": 0,
            "packet_pair_rows": [],
        }
    elif (
        row_key in force_exact
        or (
            eligibility["conductor_mixed_mode_pairs"] <= max_exact_mode_pairs
            and eligibility["candidate_tangent_products"] <= max_exact_candidate_products
        )
    ):
        shadow = exact_visible_shadow(constructor, packet_profiles)
    else:
        shadow = {
            "status": "gated",
            "reason": (
                "exact K_CH/H4 extraction exceeds configured limits; packet-pair "
                "profile and deterministic samples are recorded"
            ),
            "commutator_entries": None,
            "unique_support_keys": None,
            "commutator_orbits": None,
            "packet_pair_rows": packet_profiles,
        }

    return {
        "row_key": row_key,
        "ring": constructor.ring.name,
        "label_count": len(constructor.ring.labels),
        "nontrivial_label_count": len(constructor.ring.nontrivial),
        "gamma_size": len(constructor.ring.normalizer_actions),
        "packets": packet_sizes,
        "eligibility": eligibility,
        "visible_shadow": shadow,
        "execution_notes": EXECUTION_NOTES.get(row_key, []),
        "residual_accounting": residual_accounting(
            row_key,
            row_classifications,
            str(shadow["status"]),
            shadow.get("commutator_orbits"),
        ),
    }


def build_payload(
    *,
    row_keys: list[str],
    max_exact_mode_pairs: int,
    max_exact_candidate_products: int,
    force_exact: set[str],
    sample_mode_pairs: int,
) -> dict[str, Any]:
    row_classifications = load_row_classification()
    rows = [
        analyze_row(
            row_key,
            max_exact_mode_pairs=max_exact_mode_pairs,
            max_exact_candidate_products=max_exact_candidate_products,
            force_exact=force_exact,
            sample_mode_pairs=sample_mode_pairs,
            row_classifications=row_classifications,
        )
        for row_key in row_keys
    ]

    return {
        "classification_layer": "FC2 visible Fisher-jet kernel",
        "source_theorem_status": (
            "FC2 source theorem is treated as solved; this report classifies "
            "visible shadows and tested projection kernels"
        ),
        "projection_conventions": {
            "raw_support_projection": (
                "support-gauge C2 quotient from fc2_row_classifier; residual 0 "
                "means erasure in that projection, not filtered triviality"
            ),
            "k_ch": (
                "antisymmetric mixed second-order Fisher commutator.  It is a "
                "Fisher-jet shadow of [kappa], not an Ext_CH detector by itself"
            ),
            "h4_lift": (
                "input-side lift of a commutator key "
                "(left_mode,right_mode,alpha,beta,input,output) to closed H4 "
                "cells (left_mode,right_mode,alpha,input) and "
                "(left_mode,right_mode,beta,input)"
            ),
        },
        "exact_limits": {
            "max_exact_mode_pairs": max_exact_mode_pairs,
            "max_exact_candidate_products": max_exact_candidate_products,
            "sample_mode_pairs_per_packet": sample_mode_pairs,
            "force_exact": sorted(force_exact),
        },
        "rows": rows,
        "exact_rows": [
            row["row_key"]
            for row in rows
            if row["visible_shadow"]["status"] == "exact"
        ],
        "gated_rows": [
            row["row_key"]
            for row in rows
            if row["visible_shadow"]["status"] == "gated"
        ],
        "empty_rows": [
            row["row_key"]
            for row in rows
            if row["visible_shadow"]["status"] == "empty"
        ],
        "fc1_implications": [
            (
                "Conductor packet sizes, mixed mode-pair counts, H4 orbit image "
                "families, and commutator-orbit multiplicities are row "
                "macrovariables for the FC1 census."
            ),
            (
                "Rows can agree on raw-support erasure while differing in the "
                "visible Fisher-shadow support."
            ),
        ],
        "fc3_implications": [
            (
                "FC3 should keep full filtered residual cost separate from "
                "projection-visible Fisher-shadow cost."
            ),
            (
                "Gated rows carry explicit computation-price metadata: the "
                "information-investment channel can charge the cost of making "
                "a hidden filtered residual visible."
            ),
        ],
    }


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    return str(value)


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# FC2 Visible Fisher-Jet Kernel",
        "",
        "This report starts the visible Fisher-jet kernel phase of FC2",
        "classification.  The filtered source theorem is not being re-proved:",
        "`[kappa_R]` is the source class, while `K_CH` and H4 are tested",
        "Fisher-jet shadows of that class.",
        "",
        "The raw-support projection is kept separate from `K_CH`.  A support",
        "residual of `0` means erasure in that quotient, not filtered closure.",
        "",
        "## Extraction Limits",
        "",
        f"- max exact conductor-mixed mode pairs: `{payload['exact_limits']['max_exact_mode_pairs']}`",
        f"- max exact candidate tangent products: `{payload['exact_limits']['max_exact_candidate_products']}`",
        f"- sampled mode pairs per gated packet pair: `{payload['exact_limits']['sample_mode_pairs_per_packet']}`",
        f"- forced exact rows: `{payload['exact_limits']['force_exact']}`",
        "",
        "## Row Summary",
        "",
        "| row | ring | packets | mixed mode pairs | candidate products | status | K_CH entries | K_CH orbits | H4 lift | residual accounting |",
        "|---|---|---|---:|---:|---|---:|---:|---|---|",
    ]

    for row in payload["rows"]:
        shadow = row["visible_shadow"]
        lift = shadow.get("input_side_h4_lift", {})
        if shadow["status"] == "exact":
            h4_text = (
                f"{lift['lifted_commutator_orbits']}/{shadow['commutator_orbits']} "
                f"H2; mixed {lift['mixed_h4_orbits_hit']}/{lift['mixed_h4_orbits_total']}; "
                f"pure {lift['pure_h4_orbits_hit']}/{lift['pure_h4_orbits_total']}"
            )
        elif shadow["status"] == "empty":
            h4_text = "empty mixed channel"
        else:
            h4_text = "gated"
        residual = row["residual_accounting"]
        residual_text = (
            f"full {fmt(residual['full_filtered_residual_atoms'])}; "
            f"support {fmt(residual['raw_support_projection_residual'])}; "
            "atom map unresolved"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    row["row_key"],
                    row["ring"],
                    str(row["packets"]),
                    str(row["eligibility"]["conductor_mixed_mode_pairs"]),
                    str(row["eligibility"]["candidate_tangent_products"]),
                    shadow["status"],
                    fmt(shadow.get("commutator_entries")),
                    fmt(shadow.get("commutator_orbits")),
                    h4_text,
                    residual_text,
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Execution Notes",
        "",
    ]
    note_seen = False
    for row in payload["rows"]:
        for note in row.get("execution_notes", []):
            note_seen = True
            lines.append(f"- `{row['row_key']}`: {note}")
    if not note_seen:
        lines.append("- none")

    lines += [
        "",
        "## Exact Shadows",
        "",
    ]
    for row in payload["rows"]:
        shadow = row["visible_shadow"]
        if shadow["status"] != "exact":
            continue
        lift = shadow["input_side_h4_lift"]
        lines += [
            f"### {row['row_key']}",
            "",
            f"- commutator entries: `{shadow['commutator_entries']}`",
            f"- commutator orbits: `{shadow['commutator_orbits']}`",
            f"- orbit sizes: `{shadow['commutator_orbit_size_distribution']}`",
            f"- coefficients: `{shadow['coefficient_distribution']}`",
            f"- lifted input-side H2 orbits: `{lift['lifted_commutator_orbits']} / {shadow['commutator_orbits']}`",
            f"- H4 mixed/pure hit: `{lift['mixed_h4_orbits_hit']} / {lift['mixed_h4_orbits_total']}` mixed, `{lift['pure_h4_orbits_hit']} / {lift['pure_h4_orbits_total']}` pure",
            f"- H2 to H4 multiplicity: `{lift['h2_to_h4_multiplicity']}`",
            f"- timings: `{shadow['timing_seconds']}`",
            "",
            "| H4 orbit | family | size | H2 commutator orbits | entry hits | representative |",
            "|---:|---|---:|---:|---:|---|",
        ]
        for image in lift["h4_orbit_image_table"]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(image["h4_orbit"]),
                        str(image["family"]),
                        str(image["size"]),
                        str(image["h2_commutator_orbits"]),
                        str(image["entry_hits"]),
                        "`" + str(image["representative"]) + "`",
                    ]
                )
                + " |"
            )
        lines.append("")
        lines += [
            "Packet-pair breakdown:",
            "",
            "| packet pair | mode pairs | entries | orbits | H4 hit | family hits |",
            "|---|---:|---:|---:|---:|---|",
        ]
        for packet in shadow["packet_pair_rows"]:
            pair_lift = packet["input_side_h4_lift"]
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"{packet['left_conductor']}->{packet['right_conductor']}",
                        str(packet["mode_pair_count"]),
                        str(packet["commutator_entries"]),
                        str(packet["commutator_orbits"]),
                        str(pair_lift["h4_orbits_hit"]),
                        "`" + str(pair_lift["h4_family_orbits_hit"]) + "`",
                    ]
                )
                + " |"
            )
        lines.append("")

    lines += [
        "## Gated Profiles",
        "",
    ]
    gated_seen = False
    for row in payload["rows"]:
        shadow = row["visible_shadow"]
        if shadow["status"] != "gated":
            continue
        gated_seen = True
        lines += [
            f"### {row['row_key']}",
            "",
            f"- reason: {shadow['reason']}",
            "",
            "| packet pair | mode pairs | candidate products | sample entries | scaled entry estimate | sample modes |",
            "|---|---:|---:|---:|---:|---|",
        ]
        for packet in shadow["packet_pair_rows"]:
            sample_entries = sum(
                sample["commutator_entries"]
                for sample in packet.get("sample_mode_pairs", [])
            )
            estimate = packet.get("sample_scaled_commutator_entry_estimate")
            sample_modes = "; ".join(
                f"{sample['left_mode']}->{sample['right_mode']}"
                for sample in packet.get("sample_mode_pairs", [])
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"{packet['left_conductor']}->{packet['right_conductor']}",
                        str(packet["mode_pair_count"]),
                        str(packet["candidate_tangent_products"]),
                        str(sample_entries),
                        fmt(estimate),
                        "`" + sample_modes + "`",
                    ]
                )
                + " |"
            )
        lines.append("")
    if not gated_seen:
        lines.append("No rows were gated under this run.")
        lines.append("")

    lines += [
        "## Atom-Level Accounting",
        "",
        "This report deliberately does not count `K_CH` as an `Ext_CH` atom",
        "detector.  The exact rows prove that a row has a visible Fisher-jet",
        "shadow and identify its commutator/H4 support.  They do not yet assign",
        "individual full filtered residual atoms to visible or invisible K_CH",
        "buckets.  That coefficient-level atom map is the next refinement.",
        "",
        "## FC1/FC3 Handoff",
        "",
        "For FC1, the new natural invariants are mixed mode-pair counts,",
        "commutator orbit sizes, input-side H4 image families, and gated",
        "candidate-product profiles.  For FC3, the split is now explicit:",
        "full filtered residual cost, raw-support-erased cost, and the cost of",
        "paying for a richer visible Fisher channel are separate quantities.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rows",
        default="f4-u2,f2-u5,f8-u2,f16-field,f2-u4-control",
        help="comma-separated row keys",
    )
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_MD)
    parser.add_argument("--max-exact-mode-pairs", type=int, default=100)
    parser.add_argument("--max-exact-candidate-products", type=int, default=50_000)
    parser.add_argument(
        "--force-exact",
        default="",
        help="comma-separated row keys to run exactly despite the profile gate",
    )
    parser.add_argument("--sample-mode-pairs", type=int, default=1)
    args = parser.parse_args()

    row_keys = [key.strip() for key in args.rows.split(",") if key.strip()]
    unknown = sorted(set(row_keys) - set(ROW_FACTORIES))
    if unknown:
        raise ValueError(f"unknown row keys: {', '.join(unknown)}")
    force_exact = {key.strip() for key in args.force_exact.split(",") if key.strip()}
    unknown_force = sorted(force_exact - set(ROW_FACTORIES))
    if unknown_force:
        raise ValueError(f"unknown forced row keys: {', '.join(unknown_force)}")

    payload = build_payload(
        row_keys=row_keys,
        max_exact_mode_pairs=args.max_exact_mode_pairs,
        max_exact_candidate_products=args.max_exact_candidate_products,
        force_exact=force_exact,
        sample_mode_pairs=args.sample_mode_pairs,
    )
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_markdown(payload), encoding="utf-8")
    print(render_markdown(payload))
    print(f"Wrote {args.json}")
    print(f"Wrote {args.report}")


if __name__ == "__main__":
    main()
