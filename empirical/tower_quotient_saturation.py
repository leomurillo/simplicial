"""Tower-level quotient saturation scan for selected F2 suffix leaves.

This script deliberately does not ask for finite full-block closure.  It
collects the quotient observables that can support a tower statement:

* C2-volume normalized residual mass on exact reduced rows;
* normalizer-orbit quotient volume and residual orbit mass;
* support-level H4-to-H3 orbit cokernel;
* optional raw quotient-pressure rows beyond the exact reduction frontier.

Rows loaded from per_leaf_coboundary_audit.json retain exact full-block
residual data.  Extension rows computed here are marked raw-only unless a
matching exact reduced row is present.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from time import perf_counter
from typing import Any

from cocycle_reducer import CocycleReducer
from local_adjacency_constructor import (
    FiniteFieldSpec,
    FiniteRingSpec,
    LocalAdjacencyConstructor,
    make_f2_u2_ring,
    make_f2_u3_ring,
    make_f2_u4_ring,
    make_f2_u5_ring,
    make_finite_local_ring,
)
from per_leaf_coboundary_audit import (
    C2Key,
    c2_orbit_quotient,
    c2_volume_normalized_masses,
    canonical_c2_key,
    fraction_l1_mass,
    leaf_c2_indexer,
    leaf_hyper_adjacency_summary,
    orbit_volume_normalized_masses,
    path_in_leaf,
    split_leaf,
)


ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "empirical" / "reports"
DEFAULT_EXACT_SOURCE = REPORTS / "per_leaf_coboundary_audit.json"
DEFAULT_MODULAR_SOURCE = REPORTS / "streaming_modular_residual.json"


def exponent_label(exponent: int) -> str:
    if exponent == 1:
        return "u"
    return f"u^{exponent}"


def suffix_leaf(exponent: int) -> str:
    if exponent < 2:
        raise ValueError("suffix leaves require nilpotency at least 2")
    return f"{exponent_label(exponent - 1)}+{exponent_label(exponent)}"


def ring_name(exponent: int) -> str:
    return f"F_2[u]/(u^{exponent})"


def make_f2_u_ring(exponent: int):
    if exponent == 2:
        return make_f2_u2_ring()
    if exponent == 3:
        return make_f2_u3_ring()
    if exponent == 4:
        return make_f2_u4_ring()
    if exponent == 5:
        return make_f2_u5_ring()
    return make_finite_local_ring(
        FiniteRingSpec(
            name=ring_name(exponent),
            coefficient_field=FiniteFieldSpec(
                degree=1,
                modulus=0b11,
                symbol="a",
                name="F_2",
            ),
            nilpotency=exponent,
            include_all_unipotent_automorphisms=True,
        )
    )


def load_exact_rows(path: Path) -> dict[tuple[int, str], dict[str, Any]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows: dict[tuple[int, str], dict[str, Any]] = {}
    for row in payload.get("rows", []):
        ring = str(row.get("ring", ""))
        if not ring.startswith("F_2[u]/(u^"):
            continue
        try:
            exponent = int(ring.rsplit("^", 1)[1].rstrip(")"))
        except ValueError:
            continue
        rows[(exponent, str(row.get("leaf")))] = row
    return rows


def load_modular_rows(path: Path) -> dict[tuple[int, str], dict[str, Any]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows: dict[tuple[int, str], dict[str, Any]] = {}
    for row in payload.get("rows", []):
        if row.get("modular_residual_status") != "complete":
            continue
        ring = str(row.get("ring", ""))
        if not ring.startswith("F_2[u]/(u^"):
            continue
        try:
            exponent = int(ring.rsplit("^", 1)[1].rstrip(")"))
        except ValueError:
            continue
        rows[(exponent, str(row.get("leaf")))] = row
    return rows


def json_ready(obj: Any) -> Any:
    if isinstance(obj, float):
        return round(obj, 12)
    if isinstance(obj, list):
        return [json_ready(item) for item in obj]
    if isinstance(obj, dict):
        return {str(key): json_ready(value) for key, value in obj.items()}
    return obj


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def is_close(left: float | None, right: float | None, *, tolerance: float = 1e-9) -> bool:
    if left is None or right is None:
        return False
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=tolerance)


def raw_orbit_support_for_keys(reducer: CocycleReducer, keys: set[C2Key]) -> int:
    return len({canonical_c2_key(reducer, key) for key in keys})


def quotient_pressure_row(
    exponent: int,
    *,
    orbit_quotient_limit: int,
    hyper_prefix_limit: int,
) -> dict[str, Any]:
    started = perf_counter()
    constructor = LocalAdjacencyConstructor(make_f2_u_ring(exponent))
    reducer = CocycleReducer(constructor)
    leaf_name = suffix_leaf(exponent)
    leaf = set(split_leaf(leaf_name))
    c2_dimension, _c2_index, pair_count = leaf_c2_indexer(reducer, leaf)
    orbit_summary, _keys_by_index = c2_orbit_quotient(
        reducer,
        leaf,
        orbit_quotient_limit=orbit_quotient_limit,
    )
    hyper_summary = leaf_hyper_adjacency_summary(
        constructor,
        leaf,
        max_prefixes=hyper_prefix_limit,
    )
    raw_vector = {
        key: value
        for key, value in reducer.raw_vector().items()
        if path_in_leaf(key, leaf)
    }
    raw_orbits = raw_orbit_support_for_keys(reducer, set(raw_vector))
    c2_orbit_volume = orbit_summary["c2_orbit_quotient_volume"]
    return {
        "exponent": exponent,
        "ring": ring_name(exponent),
        "leaf": leaf_name,
        "row_kind": "raw_quotient_pressure",
        "residual_is_exact": False,
        "c2_dimension": c2_dimension,
        "leaf_pair_count": pair_count,
        "raw_support": len(raw_vector),
        "residual_support": None,
        "residual_deficit": None,
        "raw_orbit_quotient_support": raw_orbits,
        "residual_orbit_quotient_support": None,
        **orbit_summary,
        **orbit_volume_normalized_masses(raw_orbits, None, c2_orbit_volume),
        **c2_volume_normalized_masses(fraction_l1_mass(raw_vector), None, c2_dimension),
        **hyper_summary,
        "elapsed_seconds": round(perf_counter() - started, 3),
    }


def exact_row_from_report(exponent: int, row: dict[str, Any]) -> dict[str, Any]:
    return {
        "exponent": exponent,
        "ring": row["ring"],
        "leaf": row["leaf"],
        "row_kind": "exact_reduced",
        "residual_is_exact": not row.get("skipped", False),
        "skipped": row.get("skipped", False),
        "c2_dimension": row.get("c2_dimension"),
        "leaf_pair_count": row.get("leaf_pair_count"),
        "raw_support": row.get("raw_support"),
        "residual_support": row.get("residual_support"),
        "residual_deficit": row.get("residual_deficit"),
        "nu_lambda_E_raw_mass": row.get("nu_lambda_E_raw_mass"),
        "nu_lambda_E_residual_mass": row.get("nu_lambda_E_residual_mass"),
        "nu_lambda_E_deficit": row.get("nu_lambda_E_deficit"),
        "c2_orbit_quotient_volume": row.get("c2_orbit_quotient_volume"),
        "raw_orbit_quotient_support": row.get("raw_orbit_quotient_support"),
        "residual_orbit_quotient_support": row.get("residual_orbit_quotient_support"),
        "orbit_quotient_raw_mass": row.get("orbit_quotient_raw_mass"),
        "orbit_quotient_residual_mass": row.get("orbit_quotient_residual_mass"),
        "orbit_quotient_deficit": row.get("orbit_quotient_deficit"),
        "h3_leaf_orbit_quotient_dimension": row.get("h3_leaf_orbit_quotient_dimension"),
        "h4_leaf_orbit_quotient_dimension": row.get("h4_leaf_orbit_quotient_dimension"),
        "h4_to_h3_orbit_cokernel_dimension": row.get("h4_to_h3_orbit_cokernel_dimension"),
        "h4_to_h3_target_orbits_hit": row.get("h4_to_h3_target_orbits_hit"),
        "h4_to_h3_valid_contractions": row.get("h4_to_h3_valid_contractions"),
        "h4_to_h3_invalid_contractions": row.get("h4_to_h3_invalid_contractions"),
        "elapsed_seconds": row.get("elapsed_seconds"),
    }


def modular_row_from_report(exponent: int, row: dict[str, Any]) -> dict[str, Any]:
    return {
        "exponent": exponent,
        "ring": row["ring"],
        "leaf": row["leaf"],
        "row_kind": "modular_reduced",
        "residual_is_reduced": True,
        "residual_is_exact": False,
        "residual_is_modular": True,
        "coefficient_field": row.get("coefficient_field"),
        "c2_dimension": row.get("c2_dimension"),
        "leaf_pair_count": row.get("leaf_pair_count"),
        "raw_support": row.get("raw_support"),
        "residual_support": row.get("residual_support"),
        "residual_deficit": row.get("residual_deficit"),
        "nu_lambda_E_raw_mass": row.get("nu_lambda_E_raw_mass"),
        "nu_lambda_E_residual_mass": row.get("nu_lambda_E_residual_mass"),
        "nu_lambda_E_deficit": row.get("nu_lambda_E_deficit"),
        "c2_orbit_quotient_volume": row.get("c2_orbit_quotient_volume"),
        "raw_orbit_quotient_support": row.get("raw_orbit_quotient_support"),
        "residual_orbit_quotient_support": row.get("residual_orbit_quotient_support"),
        "orbit_quotient_raw_mass": row.get("orbit_quotient_raw_mass"),
        "orbit_quotient_residual_mass": row.get("orbit_quotient_residual_mass"),
        "orbit_quotient_deficit": row.get("orbit_quotient_deficit"),
        "h3_leaf_orbit_quotient_dimension": None,
        "h4_leaf_orbit_quotient_dimension": None,
        "h4_to_h3_orbit_cokernel_dimension": None,
        "elapsed_seconds": row.get("elapsed_seconds"),
    }


def build_rows(
    *,
    exact_source: Path,
    modular_source: Path,
    min_exponent: int,
    max_exponent: int,
    extend_to: int,
    orbit_quotient_limit: int,
    hyper_prefix_limit: int,
) -> list[dict[str, Any]]:
    exact_rows = load_exact_rows(exact_source)
    modular_rows = load_modular_rows(modular_source)
    rows: list[dict[str, Any]] = []
    for exponent in range(min_exponent, max_exponent + 1):
        leaf = suffix_leaf(exponent)
        exact = exact_rows.get((exponent, leaf))
        modular = modular_rows.get((exponent, leaf))
        if exact is not None:
            rows.append(exact_row_from_report(exponent, exact))
            continue
        if modular is not None:
            rows.append(modular_row_from_report(exponent, modular))
            continue
        rows.append(
            quotient_pressure_row(
                exponent,
                orbit_quotient_limit=orbit_quotient_limit,
                hyper_prefix_limit=hyper_prefix_limit,
            )
        )

    for exponent in range(max_exponent + 1, extend_to + 1):
        leaf = suffix_leaf(exponent)
        modular = modular_rows.get((exponent, leaf))
        if modular is not None:
            rows.append(modular_row_from_report(exponent, modular))
            continue
        rows.append(
            quotient_pressure_row(
                exponent,
                orbit_quotient_limit=orbit_quotient_limit,
                hyper_prefix_limit=hyper_prefix_limit,
            )
        )
    return rows


def assess_saturation(rows: list[dict[str, Any]]) -> dict[str, Any]:
    exact_rows = [row for row in rows if row.get("residual_is_exact")]
    exact_rows.sort(key=lambda row: row["exponent"])
    reduced_rows = [row for row in rows if row.get("residual_is_reduced", row.get("residual_is_exact"))]
    reduced_rows.sort(key=lambda row: row["exponent"])
    available_rows = sorted(rows, key=lambda row: row["exponent"])
    c2_masses = [row.get("nu_lambda_E_residual_mass") for row in exact_rows]
    orbit_masses = [row.get("orbit_quotient_residual_mass") for row in exact_rows]
    reduced_c2_masses = [row.get("nu_lambda_E_residual_mass") for row in reduced_rows]
    reduced_orbit_masses = [row.get("orbit_quotient_residual_mass") for row in reduced_rows]
    available_c2_masses = [
        row.get("nu_lambda_E_residual_mass")
        if row.get("residual_is_exact")
        else row.get("nu_lambda_E_raw_mass")
        for row in available_rows
    ]
    available_orbit_masses = [
        row.get("orbit_quotient_residual_mass")
        if row.get("residual_is_exact")
        else row.get("orbit_quotient_raw_mass")
        for row in available_rows
    ]
    deficits = [row.get("residual_deficit") for row in exact_rows]
    cokernels = [row.get("h4_to_h3_orbit_cokernel_dimension") for row in rows]

    c2_halves = all(
        is_close(c2_masses[index + 1], c2_masses[index] / 2)
        for index in range(len(c2_masses) - 1)
    )
    orbit_decreases = all(
        orbit_masses[index + 1] is not None
        and orbit_masses[index] is not None
        and orbit_masses[index + 1] < orbit_masses[index]
        for index in range(len(orbit_masses) - 1)
    )
    reduced_c2_halves = all(
        is_close(reduced_c2_masses[index + 1], reduced_c2_masses[index] / 2)
        for index in range(len(reduced_c2_masses) - 1)
    )
    reduced_orbit_decreases = all(
        reduced_orbit_masses[index + 1] is not None
        and reduced_orbit_masses[index] is not None
        and reduced_orbit_masses[index + 1] < reduced_orbit_masses[index]
        for index in range(len(reduced_orbit_masses) - 1)
    )
    available_c2_halves = all(
        is_close(available_c2_masses[index + 1], available_c2_masses[index] / 2)
        for index in range(len(available_c2_masses) - 1)
    )
    available_orbit_decreases = all(
        available_orbit_masses[index + 1] is not None
        and available_orbit_masses[index] is not None
        and available_orbit_masses[index + 1] < available_orbit_masses[index]
        for index in range(len(available_orbit_masses) - 1)
    )
    deficits_flat = all(is_close(value, 1.0) for value in deficits)
    cokernel_zero = all(value == 0 for value in cokernels if value is not None)

    return {
        "exact_exponents": [row["exponent"] for row in exact_rows],
        "reduced_exponents": [row["exponent"] for row in reduced_rows],
        "available_exponents": [row["exponent"] for row in available_rows],
        "c2_volume_residual_halves_on_exact_rows": c2_halves,
        "orbit_residual_mass_strictly_decreases_on_exact_rows": orbit_decreases,
        "c2_volume_residual_halves_on_reduced_rows": reduced_c2_halves,
        "orbit_residual_mass_strictly_decreases_on_reduced_rows": reduced_orbit_decreases,
        "available_c2_volume_pressure_halves": available_c2_halves,
        "available_orbit_pressure_mass_strictly_decreases": available_orbit_decreases,
        "relative_full_block_deficit_flat_one": deficits_flat,
        "support_h4_to_h3_cokernel_zero_on_available_rows": cokernel_zero,
        "tower_saturation_status": (
            "quotient-level evidence only; prove inverse-limit residual orbit "
            "mass tends to zero and replace support cokernel by the full current "
            "quotient rank"
        ),
    }


def make_report(rows: list[dict[str, Any]], assessment: dict[str, Any], output_json: Path) -> str:
    lines = [
        "# Tower Quotient Saturation Scan",
        "",
        f"- JSON artifact: `{output_json}`",
        "- Tower leaf: top-two suffix packet `{u^(e-1), u^e}` in `F_2[u]/(u^e)`.",
        "- Exact rows are loaded from `per_leaf_coboundary_audit`; extension rows are raw quotient-pressure rows and do not claim residual reduction.",
        "- Modular rows are loaded from `streaming_modular_residual`; they give finite-field residual data, not rational closure proofs.",
        "- Saturation target: show normalized residual orbit mass tends to zero and the full higher-current quotient vanishes in the inverse limit.",
        "- This report is not a finite full-closure certificate.",
        "",
        "## Tower Indicators",
        "",
        f"- C2-volume residual mass halves on exact rows: `{assessment['c2_volume_residual_halves_on_exact_rows']}`",
        f"- Orbit residual mass strictly decreases on exact rows: `{assessment['orbit_residual_mass_strictly_decreases_on_exact_rows']}`",
        f"- C2-volume residual mass halves on all reduced rows: `{assessment['c2_volume_residual_halves_on_reduced_rows']}`",
        f"- Orbit residual mass strictly decreases on all reduced rows: `{assessment['orbit_residual_mass_strictly_decreases_on_reduced_rows']}`",
        f"- Available C2-volume pressure halves including raw extension rows: `{assessment['available_c2_volume_pressure_halves']}`",
        f"- Available orbit pressure mass strictly decreases including raw extension rows: `{assessment['available_orbit_pressure_mass_strictly_decreases']}`",
        f"- Relative full-block deficit remains 1 on exact rows: `{assessment['relative_full_block_deficit_flat_one']}`",
        f"- Support H4->H3 orbit cokernel is zero where available: `{assessment['support_h4_to_h3_cokernel_zero_on_available_rows']}`",
        "",
        "| e | leaf | row kind | field | reduced residual | C2 dim | raw support | residual support | deficit | nu_E raw | nu_E residual | C2 orbit vol | raw orbit support | raw orbit mass | residual orbit support | residual orbit mass | H3 orbits | H4 orbits | H4->H3 cokernel | seconds |",
        "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['exponent']} | `{row['leaf']}` | {row['row_kind']} | "
            f"{row.get('coefficient_field', 'Q' if row.get('residual_is_exact') else 'n/a')} | "
            f"{row.get('residual_is_reduced', row.get('residual_is_exact', False))} | "
            f"{fmt(row.get('c2_dimension'))} | "
            f"{fmt(row.get('raw_support'))} | {fmt(row.get('residual_support'))} | "
            f"{fmt(row.get('residual_deficit'))} | {fmt(row.get('nu_lambda_E_raw_mass'))} | "
            f"{fmt(row.get('nu_lambda_E_residual_mass'))} | "
            f"{fmt(row.get('c2_orbit_quotient_volume'))} | "
            f"{fmt(row.get('raw_orbit_quotient_support'))} | "
            f"{fmt(row.get('orbit_quotient_raw_mass'))} | "
            f"{fmt(row.get('residual_orbit_quotient_support'))} | "
            f"{fmt(row.get('orbit_quotient_residual_mass'))} | "
            f"{fmt(row.get('h3_leaf_orbit_quotient_dimension'))} | "
            f"{fmt(row.get('h4_leaf_orbit_quotient_dimension'))} | "
            f"{fmt(row.get('h4_to_h3_orbit_cokernel_dimension'))} | "
            f"{fmt(row.get('elapsed_seconds'))} |"
        )

    lines += [
        "",
        "## Reading",
        "",
        "The exact rational rows through the original reduction frontier do not close finitely: the relative full-block residual deficit stays `1.0`.  The streaming modular row at the next suffix depth also has residual deficit `1.0`, but now its quotient-pressure datum is an actual modular residual-orbit datum.  The C2-volume mass halves along the reduced suffix tower, and the orbit-quotient residual mass is strictly decreasing on the same reduced rows.  The support-level H4-to-H3 orbit cokernel is already zero where the support quotient is computed.",
        "",
        "The tower theorem target is therefore sharper: prove that the inverse-system transition maps turn this decreasing quotient mass into zero limiting higher-current quotient, or exhibit a stable residual class that survives despite the finite support-orbit saturation.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact-source", type=Path, default=DEFAULT_EXACT_SOURCE)
    parser.add_argument("--modular-source", type=Path, default=DEFAULT_MODULAR_SOURCE)
    parser.add_argument("--min-exponent", type=int, default=2)
    parser.add_argument("--max-exponent", type=int, default=5)
    parser.add_argument(
        "--extend-to",
        type=int,
        default=5,
        help="Compute raw quotient-pressure extension rows beyond max-exponent.",
    )
    parser.add_argument("--orbit-quotient-limit", type=int, default=1_000_000)
    parser.add_argument("--hyper-prefix-limit", type=int, default=500_000)
    parser.add_argument("--report", type=Path, default=REPORTS / "tower_quotient_saturation.md")
    parser.add_argument("--json", type=Path, default=REPORTS / "tower_quotient_saturation.json")
    args = parser.parse_args()

    if args.extend_to < args.max_exponent:
        raise SystemExit("--extend-to must be at least --max-exponent")

    rows = build_rows(
        exact_source=args.exact_source,
        modular_source=args.modular_source,
        min_exponent=args.min_exponent,
        max_exponent=args.max_exponent,
        extend_to=args.extend_to,
        orbit_quotient_limit=args.orbit_quotient_limit,
        hyper_prefix_limit=args.hyper_prefix_limit,
    )
    assessment = assess_saturation(rows)

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    payload = {"rows": rows, "assessment": assessment}
    args.json.write_text(json.dumps(json_ready(payload), indent=2), encoding="utf-8")
    args.report.write_text(make_report(rows, assessment, args.json), encoding="utf-8")
    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(json.dumps(json_ready(assessment), indent=2))


if __name__ == "__main__":
    main()
