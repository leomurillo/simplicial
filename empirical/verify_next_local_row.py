"""Verify the next declarative local-ring row through the constructor stack."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from time import perf_counter
from typing import Callable

from cocycle_reducer import CocycleReducer
from fisher_jet_functor import FisherJet
from hyper_adjacency_tower import HyperAdjacencyTower
from local_adjacency_constructor import (
    FiniteLocalRing,
    LocalAdjacencyConstructor,
    make_f2_u2_ring,
    make_f2_u3_ring,
    make_f2_u4_ring,
    make_f2_u5_ring,
    make_f4_u3_ring,
    make_f8_u2_ring,
)


REPORT_JSON = Path(__file__).with_name("reports") / "next_local_row_f2_u5.json"
REPORT_MD = Path(__file__).with_name("reports") / "next_local_row_f2_u5.md"

RING_FACTORIES: dict[str, Callable[[], FiniteLocalRing]] = {
    "f2-u2": make_f2_u2_ring,
    "f2-u3": make_f2_u3_ring,
    "f2-u4": make_f2_u4_ring,
    "f2-u5": make_f2_u5_ring,
    "f4-u3": make_f4_u3_ring,
    "f8-u2": make_f8_u2_ring,
}


def counter_json(counter: Counter[object]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter, key=str)}


def cell_orbit_summary(
    constructor: LocalAdjacencyConstructor,
    arity: int,
) -> dict[str, object]:
    tower = HyperAdjacencyTower(constructor)
    started = perf_counter()
    cells = tower.cells(arity)
    _cell_to_orbit, rows = tower.orbit_maps(arity)
    elapsed = perf_counter() - started
    return {
        "cells": len(cells),
        "orbits": len(rows),
        "family_orbit_counts": dict(sorted(Counter(str(row["family"]) for row in rows).items())),
        "orbit_size_distribution": dict(sorted(Counter(int(row["size"]) for row in rows).items())),
        "orbit_rows": [
            {
                "id": int(row["id"]),
                "size": int(row["size"]),
                "family": str(row["family"]),
                "representative": str(row["representative"]),
            }
            for row in rows
        ],
        "elapsed_seconds": round(elapsed, 3),
    }


def fisher_probe(constructor: LocalAdjacencyConstructor) -> dict[str, object]:
    jet = FisherJet(constructor)
    packet_labels = [labels[0] for labels in constructor.packets.values() if labels]
    left_mode = packet_labels[0]
    right_mode = packet_labels[min(1, len(packet_labels) - 1)]
    alpha = constructor.ring.nontrivial[0]
    expansion = jet.elementary_expansion(alpha, left_mode, right_mode)
    return {
        "alpha": constructor.ring.label_name(alpha),
        "left_mode": constructor.ring.label_name(left_mode),
        "right_mode": constructor.ring.label_name(right_mode),
        "order0_support": len(expansion.order0),
        "left_order1_support": len(expansion.left_order1),
        "right_order1_support": len(expansion.right_order1),
        "mixed_order2_support": len(expansion.mixed_order2),
    }


def full_block_dimensions(constructor: LocalAdjacencyConstructor) -> dict[str, int]:
    packet_sizes = {
        conductor: len(labels)
        for conductor, labels in constructor.packets.items()
    }
    composable_pair_count = 0
    c2_dimension = 0
    for right in constructor.shifts:
        for left in constructor.shifts_by_source.get(right.target, []):
            composable_pair_count += 1
            c2_dimension += packet_sizes[left.target] * packet_sizes[right.source]

    return {
        "c1_generators": sum(
            packet_sizes[shift.source] * packet_sizes[shift.target]
            for shift in constructor.shifts
        ),
        "c2_dimension": c2_dimension,
        "composable_pairs": composable_pair_count,
    }


def ext_summary(
    constructor: LocalAdjacencyConstructor,
    *,
    include_coboundary: bool,
    coboundary_c2_limit: int,
    coboundary_field_prime: int | None,
    include_support_projection: bool,
    support_projection_raw_limit: int,
) -> dict[str, object]:
    reducer = CocycleReducer(constructor)
    dimensions = full_block_dimensions(constructor)
    started = perf_counter()
    atoms = reducer.raw_atoms()
    pair_orbits = reducer.pair_orbits()
    raw_pairs = {atom.pair_key for atom in atoms}
    payload: dict[str, object] = {
        "full_block_dimensions": dimensions,
        "raw_atom_count": len(atoms),
        "raw_pair_count": len(raw_pairs),
        "raw_coefficient_distribution": counter_json(Counter(atom.coefficient for atom in atoms)),
        "raw_path_distribution": dict(sorted(Counter(atom.path_word for atom in atoms).items())),
        "canonical_pair_orbit_count": len(pair_orbits),
        "pair_orbit_size_distribution": dict(
            sorted(Counter(int(orbit["size"]) for orbit in pair_orbits).items())
        ),
        "pair_orbit_missing_total": sum(int(orbit["missing"]) for orbit in pair_orbits),
        "canonical_pair_orbits": [
            {
                "id": index,
                "representative": reducer.pair_json(orbit["representative"]),
                "size": int(orbit["size"]),
                "atom_count": int(orbit["atom_count"]),
                "coefficients": reducer.counter_json(orbit["coefficients"]),
                "path": str(orbit["path"]),
            }
            for index, orbit in enumerate(pair_orbits, 1)
        ],
        "elapsed_seconds_before_coboundary": round(perf_counter() - started, 3),
    }
    if include_support_projection and len(atoms) <= support_projection_raw_limit:
        support_started = perf_counter()
        payload["support_projection_coboundary"] = reducer.coboundary_reduction(
            "support",
            c2_scope="raw_support",
        )
        payload["support_projection_coboundary"]["elapsed_seconds"] = round(
            perf_counter() - support_started,
            3,
        )
    elif include_support_projection:
        payload["support_projection_coboundary"] = {
            "skipped": True,
            "reason": "raw support exceeds limit",
            "raw_support": len(atoms),
            "raw_support_limit": support_projection_raw_limit,
        }

    if include_coboundary and dimensions["c2_dimension"] <= coboundary_c2_limit:
        coboundary_started = perf_counter()
        payload["full_block_coboundary"] = reducer.coboundary_reduction(
            "full_block",
            field_modulus=coboundary_field_prime,
        )
        payload["full_block_coboundary"]["elapsed_seconds"] = round(
            perf_counter() - coboundary_started,
            3,
        )
    elif include_coboundary:
        payload["full_block_coboundary"] = {
            "skipped": True,
            "reason": "c2_dimension exceeds limit",
            "c2_limit": coboundary_c2_limit,
            **dimensions,
        }
    return payload


def build_payload(
    *,
    ring_key: str,
    include_coboundary: bool,
    coboundary_c2_limit: int,
    coboundary_field_prime: int | None,
    include_support_projection: bool,
    support_projection_raw_limit: int,
) -> dict[str, object]:
    ring = RING_FACTORIES[ring_key]()
    constructor = LocalAdjacencyConstructor(ring)
    carry_records = constructor.carry_records()
    support_distribution = Counter(shift.support_size for shift in constructor.shifts)
    carry_paths = Counter(record.path_word for record in carry_records)

    payload = {
        "ring": ring.name,
        "row_key": ring_key,
        "labels": len(ring.labels),
        "nontrivial_labels": len(ring.nontrivial),
        "packets": {
            conductor: len(labels)
            for conductor, labels in constructor.packets.items()
        },
        "gamma_size": len(ring.normalizer_actions),
        "quotient_shift_count": len(constructor.shifts),
        "quotient_shift_support_distribution": dict(sorted(support_distribution.items())),
        "carry_record_count": len(carry_records),
        "carry_path_distribution": dict(sorted(carry_paths.items())),
        "fisher_probe": fisher_probe(constructor),
        "h3": cell_orbit_summary(constructor, 3),
        "h4": cell_orbit_summary(constructor, 4),
        "ext_ch": ext_summary(
            constructor,
            include_coboundary=include_coboundary,
            coboundary_c2_limit=coboundary_c2_limit,
            coboundary_field_prime=coboundary_field_prime,
            include_support_projection=include_support_projection,
            support_projection_raw_limit=support_projection_raw_limit,
        ),
    }
    return payload


def render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Next Local Row Verification",
        "",
        f"- ring: {payload['ring']}",
        f"- labels: {payload['labels']} total, {payload['nontrivial_labels']} nontrivial",
        f"- packets: {payload['packets']}",
        f"- Gamma size: {payload['gamma_size']}",
        f"- quotient-shift generators: {payload['quotient_shift_count']}",
        f"- quotient-shift support distribution: {payload['quotient_shift_support_distribution']}",
        f"- carry records: {payload['carry_record_count']}",
        "",
        "## Carry Paths",
        "",
    ]
    for path, count in payload["carry_path_distribution"].items():
        lines.append(f"- {path}: {count}")

    ext = payload["ext_ch"]
    lines += [
        "",
        "## Ext_CH",
        "",
        f"- raw atoms: {ext['raw_atom_count']}",
        f"- raw carry pairs: {ext['raw_pair_count']}",
        f"- canonical pair orbits: {ext['canonical_pair_orbit_count']}",
        f"- pair-orbit missing total: {ext['pair_orbit_missing_total']}",
        f"- raw coefficient distribution: {ext['raw_coefficient_distribution']}",
        f"- full-block dimensions: C1 {ext['full_block_dimensions']['c1_generators']}, C2 {ext['full_block_dimensions']['c2_dimension']}",
        "",
        "### Canonical Pair-Orbit Representative Table",
        "",
        "| orbit | size | atoms | path | representative | coeffs |",
        "|---:|---:|---:|---|---|---|",
    ]
    for orbit in ext["canonical_pair_orbits"]:
        rep = orbit["representative"]
        rep_text = (
            f"{rep['left_eta']} <- {rep['right_eta']} "
            f"({rep['source']}->{rep['middle']}->{rep['target']})"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(orbit["id"]),
                    str(orbit["size"]),
                    str(orbit["atom_count"]),
                    str(orbit["path"]),
                    "`" + rep_text + "`",
                    "`" + str(orbit["coefficients"]) + "`",
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Closed Cells",
        "",
        f"- H3: {payload['h3']['cells']} cells / {payload['h3']['orbits']} orbits",
        f"- H4: {payload['h4']['cells']} cells / {payload['h4']['orbits']} orbits",
        "",
        "### H3 Orbit Table",
        "",
        "| orbit | size | family | representative |",
        "|---:|---:|---|---|",
    ]
    for orbit in payload["h3"]["orbit_rows"]:
        lines.append(
            f"| {orbit['id']} | {orbit['size']} | {orbit['family']} | `{orbit['representative']}` |"
        )

    lines += [
        "",
        "### H4 Orbit Table",
        "",
        "| orbit | size | family | representative |",
        "|---:|---:|---|---|",
    ]
    for orbit in payload["h4"]["orbit_rows"]:
        lines.append(
            f"| {orbit['id']} | {orbit['size']} | {orbit['family']} | `{orbit['representative']}` |"
        )

    lines += [
        "",
        "## Fisher Probe",
        "",
        f"- modes: {payload['fisher_probe']['left_mode']} and {payload['fisher_probe']['right_mode']}",
        f"- supports: order0 {payload['fisher_probe']['order0_support']}, left1 {payload['fisher_probe']['left_order1_support']}, right1 {payload['fisher_probe']['right_order1_support']}, mixed2 {payload['fisher_probe']['mixed_order2_support']}",
    ]

    if "full_block_coboundary" in ext:
        reduction = ext["full_block_coboundary"]
        lines += ["", "## Full-Block Coboundary Diagnostic", ""]
        if reduction.get("skipped"):
            lines += [
                f"- skipped: {reduction['reason']}",
                f"- C1 generators: {reduction['c1_generators']}",
                f"- C2 dimension: {reduction['c2_dimension']}",
                f"- C2 limit: {reduction['c2_limit']}",
            ]
        else:
            lines += [
                f"- coefficient field: {reduction.get('coefficient_field', 'Q')}",
                f"- C1 generators: {reduction['c1_generators']}",
                f"- C2 dimension: {reduction['c2_dimension']}",
                f"- coboundary rank: {reduction['coboundary_rank']}",
                f"- residual quotient dimension: {reduction['residual_dimension']}",
                f"- raw support: {reduction['raw_support']}",
                f"- residual support: {reduction['residual_support']}",
                f"- residual equals raw cochain: {reduction.get('residual_equal_raw')}",
                f"- raw is coboundary: {reduction['raw_is_coboundary']}",
                f"- rational rank certified: {reduction.get('rational_rank_certified')}",
                f"- rational non-coboundary certified: {reduction.get('raw_non_coboundary_over_q_certified')}",
            ]
    else:
        lines += ["", "## Full-Block Coboundary Diagnostic", "", "- skipped"]

    if "support_projection_coboundary" in ext:
        reduction = ext["support_projection_coboundary"]
        lines += ["", "## Support-Projection Coboundary Diagnostic", ""]
        if reduction.get("skipped"):
            lines += [
                f"- skipped: {reduction['reason']}",
                f"- raw support: {reduction['raw_support']}",
                f"- raw support limit: {reduction['raw_support_limit']}",
            ]
        else:
            lines += [
                f"- mode: {reduction['mode']}",
                f"- C2 scope: {reduction['c2_scope']}",
                f"- coefficient field: {reduction.get('coefficient_field', 'Q')}",
                f"- C1 generators: {reduction['c1_generators']}",
                f"- C2 dimension: {reduction['c2_dimension']}",
                f"- coboundary rank: {reduction['coboundary_rank']}",
                f"- residual quotient dimension: {reduction['residual_dimension']}",
                f"- raw support: {reduction['raw_support']}",
                f"- residual support: {reduction['residual_support']}",
                f"- residual equals raw cochain: {reduction.get('residual_equal_raw')}",
                f"- raw is coboundary in projection: {reduction['raw_is_coboundary']}",
            ]

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ring",
        choices=sorted(RING_FACTORIES),
        default="f2-u5",
        help="declarative local-ring row to verify",
    )
    parser.add_argument(
        "--skip-coboundary",
        action="store_true",
        help="skip the full-block coboundary diagnostic",
    )
    parser.add_argument(
        "--coboundary-c2-limit",
        type=int,
        default=2_000_000,
        help="run full-block coboundary only when C2 dimension is at most this value",
    )
    parser.add_argument(
        "--coboundary-field-prime",
        type=int,
        default=None,
        help="reduce the full-block coboundary over this prime field instead of Q",
    )
    parser.add_argument(
        "--skip-support-projection",
        action="store_true",
        help="skip the support-gauge coboundary projected to raw C2 support",
    )
    parser.add_argument(
        "--support-projection-raw-limit",
        type=int,
        default=300_000,
        help="run support projection only when raw support is at most this value",
    )
    args = parser.parse_args()

    payload = build_payload(
        ring_key=args.ring,
        include_coboundary=not args.skip_coboundary,
        coboundary_c2_limit=args.coboundary_c2_limit,
        coboundary_field_prime=args.coboundary_field_prime,
        include_support_projection=not args.skip_support_projection,
        support_projection_raw_limit=args.support_projection_raw_limit,
    )
    json_path = REPORT_JSON
    markdown_path = REPORT_MD
    if args.ring != "f2-u5":
        json_path = json_path.with_name(f"next_local_row_{args.ring.replace('-', '_')}.json")
        markdown_path = markdown_path.with_name(f"next_local_row_{args.ring.replace('-', '_')}.md")

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    markdown_path.write_text(render_markdown(payload), encoding="utf-8")
    print(render_markdown(payload))
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")


if __name__ == "__main__":
    main()
