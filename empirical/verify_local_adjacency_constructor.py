"""Regression driver for the algebra-first local adjacency constructor.

The F_4[u]/(u^2) row is the required fixture.  A correct constructor must
recover the existing Paper 11 census numbers from the reusable ring, packet,
normalizer, quotient-shift, and carry data.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable

from cocycle_reducer import CocycleReducer
from fisher_jet_functor import FisherJet
from hyper_adjacency_tower import HyperAdjacencyTower
from local_adjacency_constructor import (
    FiniteLocalRing,
    LocalAdjacencyConstructor,
    make_f16_ring,
    make_f16_ring_from_spec,
    make_f2_u4_ring,
    make_f2_u4_ring_from_spec,
    make_f4_u2_ring,
    make_f4_u2_ring_from_spec,
)


REPORT_JSON = Path(__file__).with_name("reports") / "local_adjacency_constructor_f4_u2.json"
REPORT_MD = Path(__file__).with_name("reports") / "local_adjacency_constructor_f4_u2.md"


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def counter_json(counter: Counter[object]) -> dict[str, int]:
    def key_text(key: object) -> str:
        if isinstance(key, Fraction):
            return fraction_text(key)
        return str(key)

    return {key_text(key): counter[key] for key in sorted(counter, key=key_text)}


def check_equal(checks: list[dict[str, object]], name: str, actual: object, expected: object) -> None:
    passed = actual == expected
    checks.append(
        {
            "name": name,
            "actual": actual,
            "expected": expected,
            "passed": passed,
        }
    )
    if not passed:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def orbit_diagnostics(
    constructor: LocalAdjacencyConstructor,
    coefficients: dict[tuple[object, ...], Fraction],
) -> dict[str, object]:
    key_set = set(coefficients)
    remaining = set(key_set)
    orbit_sizes: Counter[int] = Counter()
    coefficient_entries: Counter[Fraction] = Counter()
    missing_total = 0
    nonconstant_orbits = 0
    orbit_count = 0

    while remaining:
        seed = next(iter(remaining))
        ambient = {
            constructor.ring.transform_tuple(seed, action, None)
            for action in constructor.ring.normalizer_actions
        }
        present = ambient & key_set
        missing_total += len(ambient - key_set)
        coeffs = Counter(coefficients[key] for key in present)
        if len(coeffs) != 1:
            nonconstant_orbits += 1
        coefficient_entries.update({coeff: coeffs[coeff] for coeff in coeffs})
        orbit_sizes[len(present)] += 1
        orbit_count += 1
        remaining -= present

    return {
        "orbit_count": orbit_count,
        "missing_total": missing_total,
        "nonconstant_orbits": nonconstant_orbits,
        "orbit_size_distribution": dict(sorted(orbit_sizes.items())),
        "coefficient_entry_distribution": counter_json(coefficient_entries),
    }


def witness_coefficients(kind: str) -> dict[tuple[object, ...], Fraction]:
    constructor = LocalAdjacencyConstructor(make_f4_u2_ring())
    jet = FisherJet(constructor)
    witnesses = jet.tangent_compatible(
        jet.witnesses(
            kind,  # type: ignore[arg-type]
            left_modes=constructor.packets["u"],
            right_modes=constructor.packets["u^2"],
        )
    )
    return jet.coefficient_by_key(witnesses)


def cell_orbit_summary(
    constructor: LocalAdjacencyConstructor,
    arity: int,
) -> dict[str, object]:
    tower = HyperAdjacencyTower(constructor)
    cells = tower.cells(arity)
    _cell_to_orbit, rows = tower.orbit_maps(arity)
    family_counts = Counter(str(row["family"]) for row in rows)
    orbit_size_distribution = Counter(int(row["size"]) for row in rows)
    payload: dict[str, object] = {
        "cells": len(cells),
        "orbits": len(rows),
        "family_orbit_counts": dict(sorted(family_counts.items())),
        "orbit_size_distribution": dict(sorted(orbit_size_distribution.items())),
    }
    if constructor.ring.local_signature is not None:
        signatures = Counter(
            constructor.ring.local_signature(row["representative_cell"])
            for row in rows
        )
        payload["signature_collisions"] = sum(1 for count in signatures.values() if count > 1)
    return payload


def control_row_summary(ring: FiniteLocalRing) -> dict[str, object]:
    constructor = LocalAdjacencyConstructor(ring)
    return {
        "ring": ring.name,
        "gamma_size": len(ring.normalizer_actions),
        "arity3": cell_orbit_summary(constructor, 3),
        "arity4": cell_orbit_summary(constructor, 4),
    }


def comparable_constructor_summary(summary: dict[str, object]) -> dict[str, object]:
    return {
        key: summary[key]
        for key in (
            "label_count",
            "nontrivial_label_count",
            "packets",
            "gamma_size",
            "quotient_shift_count",
            "quotient_shift_support_distribution",
            "carry_record_count",
            "carry_path_distribution",
            "associativity_failures",
        )
    }


def spec_equivalence_payload() -> dict[str, object]:
    f4_spec_constructor = LocalAdjacencyConstructor(make_f4_u2_ring_from_spec())
    f16_old = control_row_summary(make_f16_ring())
    f16_spec = control_row_summary(make_f16_ring_from_spec())
    f2u4_old = control_row_summary(make_f2_u4_ring())
    f2u4_spec = control_row_summary(make_f2_u4_ring_from_spec())
    return {
        "f4_u2_constructor": f4_spec_constructor.summary(),
        "f16_old": f16_old,
        "f16_spec": f16_spec,
        "f2_u4_old": f2u4_old,
        "f2_u4_spec": f2u4_spec,
    }


def r4_distribution() -> dict[str, object]:
    from compute_R4_covariant_at_cell import grouped_records, lifted_mixed_records

    records = lifted_mixed_records()
    final_distribution = Counter(record.final_value for record in records)
    stage2_distribution = Counter(record.stage2_value for record in records)
    inherited_distribution = Counter(record.coefficient for record in records)
    return {
        "records": len(records),
        "mixed_orbit_groups": len(grouped_records(records)),
        "inherited_coefficient_distribution": counter_json(inherited_distribution),
        "unrestricted_leibniz_distribution": counter_json(stage2_distribution),
        "paired_slot_distribution": counter_json(final_distribution),
    }


def build_payload(*, include_r4: bool, include_controls: bool) -> dict[str, object]:
    checks: list[dict[str, object]] = []
    constructor = LocalAdjacencyConstructor(make_f4_u2_ring())
    constructor_summary = constructor.summary()

    check_equal(checks, "F4[u]/u2 label count", constructor_summary["label_count"], 16)
    check_equal(
        checks,
        "F4[u]/u2 nontrivial label count",
        constructor_summary["nontrivial_label_count"],
        15,
    )
    check_equal(checks, "F4[u]/u2 packet sizes", constructor_summary["packets"], {"u": 3, "u^2": 12})
    check_equal(checks, "F4[u]/u2 Gamma size", constructor_summary["gamma_size"], 24)
    check_equal(checks, "quotient-shift associativity failures", constructor_summary["associativity_failures"], 0)

    h3 = cell_orbit_summary(constructor, 3)
    check_equal(checks, "H3 closed cells", h3["cells"], 210)
    check_equal(checks, "H3 Gamma x S3 orbits", h3["orbits"], 5)
    check_equal(checks, "H3 signature collisions", h3["signature_collisions"], 0)

    h4 = cell_orbit_summary(constructor, 4)
    check_equal(checks, "H4 closed cells", h4["cells"], 3165)
    check_equal(checks, "H4 Gamma x S4 orbits", h4["orbits"], 18)
    check_equal(
        checks,
        "H4 family orbit counts",
        h4["family_orbit_counts"],
        {"TTTT": 2, "TTWW": 4, "TWWW": 3, "WWWW": 9},
    )

    tower_contraction = HyperAdjacencyTower(constructor).pair_contraction_summary(4)
    check_equal(
        checks,
        "H4-to-H3 candidate pair contractions",
        tower_contraction["candidate_pair_contractions"],
        18990,
    )
    check_equal(
        checks,
        "H4-to-H3 valid nonzero contractions",
        tower_contraction["valid_nonzero_contractions"],
        17640,
    )
    check_equal(checks, "H4-to-H3 H3 orbits hit", tower_contraction["target_orbits_hit_count"], 5)
    check_equal(
        checks,
        "H4-to-H3 H4 orbits with valid contractions",
        tower_contraction["source_orbits_with_valid_contractions"],
        16,
    )

    cocycle = CocycleReducer(constructor).summary()
    check_equal(checks, "Ext_CH raw carry atoms", cocycle["raw_atom_count"], 1569)
    check_equal(checks, "Ext_CH raw carry pairs", cocycle["raw_pair_count"], 369)
    check_equal(checks, "Ext_CH atom orbits", cocycle["atom_orbit_count"], 71)
    check_equal(checks, "Ext_CH pair orbits", cocycle["pair_orbit_count"], 20)
    check_equal(checks, "Ext_CH pair orbit missing total", cocycle["pair_orbit_missing_total"], 0)

    full_defect = orbit_diagnostics(constructor, witness_coefficients("defect"))
    check_equal(checks, "arity-2 full-defect orbits", full_defect["orbit_count"], 4438)
    check_equal(checks, "arity-2 full-defect missing support", full_defect["missing_total"], 0)
    check_equal(checks, "arity-2 full-defect nonconstant orbits", full_defect["nonconstant_orbits"], 0)

    commutator = orbit_diagnostics(constructor, witness_coefficients("commutator"))
    check_equal(checks, "arity-2 commutator orbits", commutator["orbit_count"], 592)
    check_equal(checks, "arity-2 commutator missing support", commutator["missing_total"], 0)
    check_equal(checks, "arity-2 commutator nonconstant orbits", commutator["nonconstant_orbits"], 0)
    check_equal(
        checks,
        "arity-2 commutator coefficient distribution",
        commutator["coefficient_entry_distribution"],
        {"-1": 7056, "1": 7056},
        )

    spec_equivalence = spec_equivalence_payload()
    check_equal(
        checks,
        "F4[u]/u2 spec constructor summary",
        comparable_constructor_summary(spec_equivalence["f4_u2_constructor"]),
        comparable_constructor_summary(constructor_summary),
    )
    check_equal(checks, "F16 spec Gamma", spec_equivalence["f16_spec"]["gamma_size"], 60)
    check_equal(
        checks,
        "F16 spec H3/H4 controls",
        (
            spec_equivalence["f16_spec"]["arity3"]["orbits"],
            spec_equivalence["f16_spec"]["arity4"]["orbits"],
        ),
        (
            spec_equivalence["f16_old"]["arity3"]["orbits"],
            spec_equivalence["f16_old"]["arity4"]["orbits"],
        ),
    )
    check_equal(checks, "F2[u]/u4 spec Gamma", spec_equivalence["f2_u4_spec"]["gamma_size"], 32)
    check_equal(
        checks,
        "F2[u]/u4 spec H3/H4 controls",
        (
            spec_equivalence["f2_u4_spec"]["arity3"]["orbits"],
            spec_equivalence["f2_u4_spec"]["arity4"]["orbits"],
        ),
        (
            spec_equivalence["f2_u4_old"]["arity3"]["orbits"],
            spec_equivalence["f2_u4_old"]["arity4"]["orbits"],
        ),
    )

    r4 = None
    if include_r4:
        r4 = r4_distribution()
        check_equal(checks, "R4 mixed-lift records", r4["records"], 592)
        check_equal(checks, "R4 mixed orbit groups", r4["mixed_orbit_groups"], 7)
        check_equal(
            checks,
            "R4 paired-slot distribution",
            r4["paired_slot_distribution"],
            {"-1": 44, "1": 504, "2": 44},
        )

    controls: list[dict[str, object]] = []
    if include_controls:
        controls = [control_row_summary(make_f16_ring()), control_row_summary(make_f2_u4_ring())]
        f16 = controls[0]
        f2u4 = controls[1]
        check_equal(checks, "F16 H3 control orbits", f16["arity3"]["orbits"], 2)
        check_equal(checks, "F16 H4 control orbits", f16["arity4"]["orbits"], 7)
        check_equal(checks, "F2[u]/u4 H3 control orbits", f2u4["arity3"]["orbits"], 7)
        check_equal(checks, "F2[u]/u4 H4 control orbits", f2u4["arity4"]["orbits"], 32)

    return {
        "constructor": constructor_summary,
        "h3": h3,
        "h4": h4,
        "tower_contraction": tower_contraction,
        "cocycle": cocycle,
        "arity2_full_defect": full_defect,
        "arity2_commutator": commutator,
        "r4_mixed_lift": r4,
        "controls": controls,
        "spec_equivalence": spec_equivalence,
        "checks": checks,
    }


def markdown_table(rows: Iterable[dict[str, object]]) -> list[str]:
    lines = ["| check | actual | expected |", "|---|---:|---:|"]
    for row in rows:
        lines.append(f"| {row['name']} | `{row['actual']}` | `{row['expected']}` |")
    return lines


def render_markdown(payload: dict[str, object]) -> str:
    constructor = payload["constructor"]
    lines = [
        "# Local Adjacency Constructor Regression",
        "",
        "This report is generated by `empirical/verify_local_adjacency_constructor.py`.",
        "It checks the algebra-first constructor, the `FisherJet` analytic functor,",
        "and the `HyperAdjacencyTower` contraction functor against the existing",
        "F4[u]/(u^2) Paper 11 fixtures.",
        "",
        "## Constructor",
        "",
        f"- ring: {constructor['ring']}",
        f"- labels: {constructor['label_count']} total, {constructor['nontrivial_label_count']} nontrivial",
        f"- packets: {constructor['packets']}",
        f"- Gamma size: {constructor['gamma_size']}",
        f"- quotient-shift generators: {constructor['quotient_shift_count']}",
        f"- nonzero carry records: {constructor['carry_record_count']}",
        f"- associativity failures: {constructor['associativity_failures']}",
        "",
        "Carry path distribution:",
        "",
    ]
    for path, count in constructor["carry_path_distribution"].items():
        lines.append(f"- {path}: {count}")

    lines += [
        "",
        "## Regression Checks",
        "",
        *markdown_table(payload["checks"]),
        "",
        "## Arity Summaries",
        "",
        f"- H3: {payload['h3']['cells']} cells, {payload['h3']['orbits']} orbits, signature collisions {payload['h3'].get('signature_collisions', '-')}",
        f"- H4: {payload['h4']['cells']} cells, {payload['h4']['orbits']} orbits, family orbits {payload['h4']['family_orbit_counts']}",
        f"- H4-to-H3 contractions: {payload['tower_contraction']['valid_nonzero_contractions']} valid / {payload['tower_contraction']['candidate_pair_contractions']} candidates, H3 orbits hit {payload['tower_contraction']['target_orbits_hit_count']}",
        f"- Ext_CH cocycle: {payload['cocycle']['raw_atom_count']} atoms, {payload['cocycle']['raw_pair_count']} carry pairs, {payload['cocycle']['pair_orbit_count']} canonical pair orbits",
        "",
        "## Arity-2 Orbit Fixtures",
        "",
        f"- full defect orbits: {payload['arity2_full_defect']['orbit_count']}",
        f"- commutator orbits: {payload['arity2_commutator']['orbit_count']}",
        f"- commutator coefficient entries: {payload['arity2_commutator']['coefficient_entry_distribution']}",
        "",
    ]

    if payload["r4_mixed_lift"] is not None:
        r4 = payload["r4_mixed_lift"]
        lines += [
            "## R4 Mixed-Lift Fixture",
            "",
            f"- records: {r4['records']}",
            f"- mixed orbit groups: {r4['mixed_orbit_groups']}",
            f"- paired-slot distribution: {r4['paired_slot_distribution']}",
            "",
        ]

    if payload["controls"]:
        lines += ["## Control Rows", ""]
        for control in payload["controls"]:
            lines.append(
                f"- {control['ring']}: Gamma {control['gamma_size']}, "
                f"H3 {control['arity3']['cells']}/{control['arity3']['orbits']}, "
                f"H4 {control['arity4']['cells']}/{control['arity4']['orbits']}"
            )
        lines.append("")

    spec = payload["spec_equivalence"]
    lines += [
        "## Spec-Backed Equivalence Rows",
        "",
        f"- {spec['f4_u2_constructor']['ring']}: shifts {spec['f4_u2_constructor']['quotient_shift_count']}, carry {spec['f4_u2_constructor']['carry_record_count']}",
        f"- {spec['f16_spec']['ring']}: Gamma {spec['f16_spec']['gamma_size']}, H3 {spec['f16_spec']['arity3']['orbits']}, H4 {spec['f16_spec']['arity4']['orbits']}",
        f"- {spec['f2_u4_spec']['ring']}: Gamma {spec['f2_u4_spec']['gamma_size']}, H3 {spec['f2_u4_spec']['arity3']['orbits']}, H4 {spec['f2_u4_spec']['arity4']['orbits']}",
        "",
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-r4", action="store_true", help="skip the slower paired-slot R4 fixture")
    parser.add_argument("--skip-controls", action="store_true", help="skip F16 and F2[u]/u4 control rows")
    args = parser.parse_args()

    payload = build_payload(include_r4=not args.skip_r4, include_controls=not args.skip_controls)
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    REPORT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(render_markdown(payload))
    print(f"\nWrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()
