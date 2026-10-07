"""Export the F_4[u]/(u^2) Ext_CH orbit table as JSON.

The markdown diagnostic in ``compute_f4_u2_ext_ch.py`` gives the human-facing
summary.  This exporter keeps the same arithmetic source but writes a stable
machine-readable table of the tangent-compatible full-defect and commutator
normalizer orbits.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
from typing import Any

from compute_f4_u2_ext_ch import (
    ACTIONS,
    ZERO,
    add_label,
    canonical_local_signature,
    coarse_local_signature,
    coefficient_by_key,
    compute_witnesses,
    conductor,
    fraction_text,
    label_name,
    tangent_compatible,
    transformed_key,
    swap_key,
)


Label = tuple[int, int]
Key = tuple[Label, Label, Label, Label, Label, Label]

POSITIONS = ("tau", "omega", "alpha", "beta", "input", "output")
REPORT_PATH = Path(__file__).with_name("reports") / "f4_u2_ext_orbits.json"


def key_sort_key(key: Key) -> tuple[Label, ...]:
    return key


def fraction_json(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": fraction_text(value),
    }


def f4_element_json(value: object) -> object:
    if not isinstance(value, int):
        return value
    names = {0: "0", 1: "1", 2: "w", 3: "w+1"}
    return {"value": value, "name": names[value]}


def label_json(label: Label) -> dict[str, object]:
    return {
        "coefficients": [label[0], label[1]],
        "text": label_name(label),
        "conductor": conductor(label),
    }


def key_json(key: Key) -> dict[str, object]:
    return {
        position: label_json(label)
        for position, label in zip(POSITIONS, key, strict=True)
    }


def signature_json(signature: tuple[tuple[object, ...], ...]) -> list[dict[str, object]]:
    return [
        {
            "kind": kind,
            "leading": f4_element_json(leading),
            "tail": f4_element_json(tail),
        }
        for kind, leading, tail in signature
    ]


def coarse_signature_json(signature: tuple[object, ...]) -> dict[str, object]:
    return {
        "operand_conductors": list(signature[0]),
        "matrix_transition": signature[1],
        "swap_kind": signature[2],
        "frobenius_cycle_length": signature[3],
        "wild_leading_residue_count": signature[4],
        "wild_tail_rank": signature[5],
    }


def add_many(labels: tuple[Label, ...]) -> Label:
    out = ZERO
    for label in labels:
        out = add_label(out, label)
    return out


def lift_flags(key: Key) -> dict[str, bool]:
    tau, omega, alpha, beta, input_label, output_label = key
    return {
        "input_alpha_lift_closed": add_many((tau, omega, alpha, input_label)) == ZERO,
        "input_beta_lift_closed": add_many((tau, omega, beta, input_label)) == ZERO,
        "output_alpha_lift_closed": add_many((tau, omega, alpha, output_label)) == ZERO,
        "output_beta_lift_closed": add_many((tau, omega, beta, output_label)) == ZERO,
        "operator_pair_closed": add_many((tau, omega, alpha, beta)) == ZERO,
    }


def support_flags(keys: set[Key], commutator_keys: set[Key] | None = None) -> dict[str, bool]:
    commutator_keys = commutator_keys or set()
    flags = {
        "tangent_compatible": all(add_label(key[2], key[3]) != ZERO for key in keys),
        "full_depth_to_full_depth": any(
            conductor(key[4]) == "u^2" and conductor(key[5]) == "u^2" for key in keys
        ),
        "has_tame_input_or_output": any(
            conductor(key[4]) == "u" or conductor(key[5]) == "u" for key in keys
        ),
        "has_equal_input_output": any(key[4] == key[5] for key in keys),
        "commutator_supported": bool(keys & commutator_keys),
    }
    for flag in lift_flags(next(iter(keys))):
        flags[f"any_{flag}"] = any(lift_flags(key)[flag] for key in keys)
    return flags


def counter_json(counter: Counter[Any]) -> list[dict[str, object]]:
    rows = []
    for value, count in sorted(counter.items(), key=lambda item: item[0]):
        if isinstance(value, Fraction):
            encoded_value: object = fraction_json(value)
        else:
            encoded_value = value
        rows.append({"value": encoded_value, "count": count})
    return rows


def deterministic_orbits(witnesses: list[dict[str, object]]) -> list[dict[str, object]]:
    coeff_by_key = coefficient_by_key(witnesses)
    key_set = set(coeff_by_key)
    remaining = set(coeff_by_key)
    orbits: list[dict[str, object]] = []

    while remaining:
        seed = min(remaining, key=key_sort_key)
        orbit = {transformed_key(seed, action) for action in ACTIONS}
        present = orbit & key_set
        representative = min(present, key=key_sort_key)
        coefficients = Counter(coeff_by_key[key] for key in present)
        orbits.append(
            {
                "representative": representative,
                "keys": present,
                "size": len(present),
                "ambient_size": len(orbit),
                "missing": len(orbit - key_set),
                "coefficients": coefficients,
            }
        )
        remaining -= present

    return sorted(orbits, key=lambda orbit: key_sort_key(orbit["representative"]))


def coefficient_field(coefficients: Counter[Fraction]) -> dict[str, object]:
    values = list(coefficients)
    return {
        "constant": len(values) == 1,
        "value": fraction_json(values[0]) if len(values) == 1 else None,
        "distribution": counter_json(coefficients),
    }


def orbit_signature_fields(
    representative: Key,
    swap_kind: str,
) -> dict[str, object]:
    exact = canonical_local_signature(representative)
    coarse = coarse_local_signature(representative, swap_kind)
    return {
        "exact_local": signature_json(exact),
        "exact_local_key": repr(exact),
        "coarse_local": coarse_signature_json(coarse),
        "coarse_local_key": repr(coarse),
    }


def orbit_base_row(
    orbit_id: int,
    orbit: dict[str, object],
    commutator_keys: set[Key],
    swap_partner_id: int,
) -> dict[str, object]:
    representative: Key = orbit["representative"]
    keys: set[Key] = orbit["keys"]
    coefficients: Counter[Fraction] = orbit["coefficients"]
    swap_kind = "swap-fixed" if swap_partner_id == orbit_id else "swap-asymmetric"
    return {
        "id": orbit_id,
        "representative": key_json(representative),
        "representative_key": [list(label) for label in representative],
        "size": orbit["size"],
        "ambient_size": orbit["ambient_size"],
        "missing_from_support": orbit["missing"],
        "coefficient": coefficient_field(coefficients),
        "operand_conductors": [conductor(representative[2]), conductor(representative[3])],
        "matrix_transition": f"{conductor(representative[4])}->{conductor(representative[5])}",
        "swap_partner_id": swap_partner_id,
        "support_flags": support_flags(keys, commutator_keys),
        "signatures": orbit_signature_fields(representative, swap_kind),
    }


def build_export() -> dict[str, object]:
    defect = tangent_compatible(compute_witnesses("defect"))
    commutator = tangent_compatible(compute_witnesses("commutator"))
    full_orbits = deterministic_orbits(defect)
    commutator_orbits = deterministic_orbits(commutator)

    defect_coeffs = coefficient_by_key(defect)
    commutator_coeffs = coefficient_by_key(commutator)
    commutator_keys = set(commutator_coeffs)

    key_to_full_orbit: dict[Key, int] = {}
    for orbit_id, orbit in enumerate(full_orbits):
        for key in orbit["keys"]:
            key_to_full_orbit[key] = orbit_id

    key_to_commutator_orbit: dict[Key, int] = {}
    for orbit_id, orbit in enumerate(commutator_orbits):
        for key in orbit["keys"]:
            key_to_commutator_orbit[key] = orbit_id

    full_swap_partners = [
        key_to_full_orbit[swap_key(orbit["representative"])] for orbit in full_orbits
    ]
    commutator_swap_partners = [
        key_to_commutator_orbit[swap_key(orbit["representative"])]
        for orbit in commutator_orbits
    ]

    commutator_orbit_ids_by_full_orbit: dict[int, int] = {}
    for commutator_orbit_id, orbit in enumerate(commutator_orbits):
        full_ids = {key_to_full_orbit[key] for key in orbit["keys"]}
        if len(full_ids) != 1:
            raise AssertionError("commutator orbit crosses full-defect orbits")
        commutator_orbit_ids_by_full_orbit[next(iter(full_ids))] = commutator_orbit_id

    full_rows = []
    for orbit_id, orbit in enumerate(full_orbits):
        row = orbit_base_row(
            orbit_id,
            orbit,
            commutator_keys,
            full_swap_partners[orbit_id],
        )
        if orbit_id in commutator_orbit_ids_by_full_orbit:
            commutator_orbit_id = commutator_orbit_ids_by_full_orbit[orbit_id]
            commutator_values = Counter(
                commutator_coeffs[key]
                for key in orbit["keys"]
                if key in commutator_coeffs
            )
            row["commutator_orbit_id"] = commutator_orbit_id
            row["commutator_coefficient"] = coefficient_field(commutator_values)
        else:
            row["commutator_orbit_id"] = None
            row["commutator_coefficient"] = coefficient_field(Counter({Fraction(0): orbit["size"]}))
        full_rows.append(row)

    commutator_rows = []
    for orbit_id, orbit in enumerate(commutator_orbits):
        representative: Key = orbit["representative"]
        full_orbit_id = key_to_full_orbit[representative]
        row = orbit_base_row(
            orbit_id,
            orbit,
            set(),
            commutator_swap_partners[orbit_id],
        )
        row["full_defect_orbit_id"] = full_orbit_id
        row["full_defect_coefficient"] = coefficient_field(
            Counter({defect_coeffs[representative]: orbit["size"]})
        )
        row["support_flags"]["commutator_supported"] = True
        commutator_rows.append(row)

    full_signatures = Counter(row["signatures"]["exact_local_key"] for row in full_rows)
    commutator_signatures = Counter(
        row["signatures"]["exact_local_key"] for row in commutator_rows
    )
    full_coefficient_counts = Counter(
        next(iter(orbit["coefficients"])) for orbit in full_orbits
    )
    commutator_coefficient_counts = Counter(
        next(iter(orbit["coefficients"])) for orbit in commutator_orbits
    )

    export = {
        "schema": "f4_u2_ext_orbits.v1",
        "source_script": "empirical/compute_f4_u2_ext_ch.py",
        "generated_by": "empirical/export_f4_u2_ext_orbits.py",
        "ring": "F_4[u]/(u^2)",
        "positions": list(POSITIONS),
        "normalizer_action_size": len(ACTIONS),
        "summary": {
            "full_defect_tangent_compatible_entries": len(defect),
            "commutator_tangent_compatible_entries": len(commutator),
            "full_defect_orbits": len(full_rows),
            "commutator_orbits": len(commutator_rows),
            "full_defect_orbit_sizes": counter_json(Counter(row["size"] for row in full_rows)),
            "commutator_orbit_sizes": counter_json(
                Counter(row["size"] for row in commutator_rows)
            ),
            "full_defect_coefficients_by_orbit": counter_json(full_coefficient_counts),
            "commutator_coefficients_by_orbit": counter_json(commutator_coefficient_counts),
            "full_defect_exact_signature_collision_buckets": sum(
                1 for count in full_signatures.values() if count > 1
            ),
            "commutator_exact_signature_collision_buckets": sum(
                1 for count in commutator_signatures.values() if count > 1
            ),
            "commutator_supported_full_defect_orbits": sum(
                1 for row in full_rows if row["support_flags"]["commutator_supported"]
            ),
        },
        "full_defect_orbits": full_rows,
        "commutator_orbits": commutator_rows,
    }

    expected = {
        "full_defect_orbits": 4438,
        "commutator_orbits": 592,
        "full_signature_collisions": 0,
        "commutator_signature_collisions": 0,
    }
    observed = {
        "full_defect_orbits": export["summary"]["full_defect_orbits"],
        "commutator_orbits": export["summary"]["commutator_orbits"],
        "full_signature_collisions": export["summary"][
            "full_defect_exact_signature_collision_buckets"
        ],
        "commutator_signature_collisions": export["summary"][
            "commutator_exact_signature_collision_buckets"
        ],
    }
    if observed != expected:
        raise AssertionError(f"unexpected orbit export summary: {observed} != {expected}")

    return export


def main() -> None:
    export = build_export()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(export, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(export["summary"], indent=2, sort_keys=True))
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
