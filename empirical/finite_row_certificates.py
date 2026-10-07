"""Compact proof-extraction certificates for finite local rows.

The heavy reports contain full orbit tables.  This script builds small
certificate summaries that are suitable for manuscript proof extraction:
source hashes, constructor counts, orbit counts, raw carry counts, and
coboundary residual facts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


REPORT_DIR = Path("empirical/reports")
DEFAULT_JSON = REPORT_DIR / "finite_row_certificates.json"
DEFAULT_MD = REPORT_DIR / "finite_row_certificates.md"

ROW_SOURCES = {
    "f4-u2": {
        "constructor": REPORT_DIR / "local_adjacency_constructor_f4_u2.json",
        "ext": REPORT_DIR / "ext_ch_cocycle_f4_u2.json",
    },
    "f2-u5": {
        "row": REPORT_DIR / "next_local_row_f2_u5.json",
    },
    "f8-u2": {
        "row": REPORT_DIR / "next_local_row_f8_u2.json",
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_record(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
    }


def compact_coboundary(reduction: dict[str, Any] | None) -> dict[str, Any] | None:
    if not reduction:
        return None
    keys = [
        "mode",
        "c2_scope",
        "coefficient_field",
        "c1_generators",
        "c2_dimension",
        "coboundary_rank",
        "residual_dimension",
        "raw_support",
        "residual_support",
        "residual_equal_raw",
        "raw_is_coboundary",
        "rational_rank_certified",
        "raw_non_coboundary_over_q_certified",
    ]
    return {key: reduction[key] for key in keys if key in reduction}


def compact_hyper(data: dict[str, Any], key: str) -> dict[str, Any] | None:
    item = data.get(key)
    if not item:
        return None
    return {
        "cells": item.get("cells"),
        "orbits": item.get("orbits"),
        "family_orbit_counts": item.get("family_orbit_counts"),
        "orbit_size_distribution": item.get("orbit_size_distribution"),
        "signature_collisions": item.get("signature_collisions"),
    }


def f4_u2_certificate() -> dict[str, Any]:
    constructor_path = ROW_SOURCES["f4-u2"]["constructor"]
    ext_path = ROW_SOURCES["f4-u2"]["ext"]
    constructor_report = load_json(constructor_path)
    ext_report = load_json(ext_path)

    return {
        "row_key": "f4-u2",
        "ring": constructor_report["constructor"]["ring"],
        "sources": [source_record(constructor_path), source_record(ext_path)],
        "constructor": constructor_report["constructor"],
        "h3": compact_hyper(constructor_report, "h3"),
        "h4": compact_hyper(constructor_report, "h4"),
        "tower_contraction": {
            key: constructor_report["tower_contraction"].get(key)
            for key in [
                "source_arity",
                "target_arity",
                "source_cells",
                "target_cells",
                "source_orbits",
                "target_orbits",
                "candidate_pair_contractions",
                "valid_nonzero_contractions",
                "invalid_zero_merge_contractions",
                "target_orbits_hit_count",
                "source_orbits_with_valid_contractions",
            ]
        },
        "ext_ch": {
            "raw_atom_count": ext_report["raw_atom_count"],
            "raw_pair_count": ext_report["raw_pair_count"],
            "raw_coefficient_distribution": ext_report["raw_coefficient_distribution"],
            "raw_path_distribution": ext_report["raw_path_distribution"],
            "atom_orbit_count": ext_report["atom_orbit_count"],
            "atom_orbit_size_distribution": ext_report["atom_orbit_size_distribution"],
            "atom_orbit_missing_total": ext_report["atom_orbit_missing_total"],
            "pair_orbit_count": ext_report["pair_orbit_count"],
            "pair_orbit_size_distribution": ext_report["pair_orbit_size_distribution"],
            "pair_orbit_missing_total": ext_report["pair_orbit_missing_total"],
            "full_block_coboundary": compact_coboundary(
                ext_report.get("coboundary_reduction")
            ),
        },
        "proof_extraction_status": "finite lemma ready after independent certificate check",
    }


def next_row_certificate(row_key: str) -> dict[str, Any]:
    path = ROW_SOURCES[row_key]["row"]
    report = load_json(path)
    ext = report["ext_ch"]

    return {
        "row_key": row_key,
        "ring": report["ring"],
        "sources": [source_record(path)],
        "constructor": {
            "ring": report["ring"],
            "label_count": report["labels"],
            "nontrivial_label_count": report["nontrivial_labels"],
            "packets": report["packets"],
            "gamma_size": report["gamma_size"],
            "quotient_shift_count": report["quotient_shift_count"],
            "quotient_shift_support_distribution": report[
                "quotient_shift_support_distribution"
            ],
            "carry_record_count": report["carry_record_count"],
            "carry_path_distribution": report["carry_path_distribution"],
        },
        "h3": compact_hyper(report, "h3"),
        "h4": compact_hyper(report, "h4"),
        "ext_ch": {
            "full_block_dimensions": ext.get("full_block_dimensions"),
            "raw_atom_count": ext["raw_atom_count"],
            "raw_pair_count": ext["raw_pair_count"],
            "raw_coefficient_distribution": ext["raw_coefficient_distribution"],
            "raw_path_distribution": ext["raw_path_distribution"],
            "pair_orbit_count": ext["canonical_pair_orbit_count"],
            "pair_orbit_size_distribution": ext["pair_orbit_size_distribution"],
            "pair_orbit_missing_total": ext["pair_orbit_missing_total"],
            "support_projection_coboundary": compact_coboundary(
                ext.get("support_projection_coboundary")
            ),
            "full_block_coboundary": compact_coboundary(
                ext.get("full_block_coboundary")
            ),
        },
        "proof_extraction_status": "finite lemma ready after independent certificate check",
    }


def build_payload(row_keys: list[str]) -> dict[str, Any]:
    certificates = []
    for row_key in row_keys:
        if row_key == "f4-u2":
            certificates.append(f4_u2_certificate())
        else:
            certificates.append(next_row_certificate(row_key))
    return {
        "purpose": (
            "Compact certificate summaries for proof extraction from exact "
            "finite local-row computations."
        ),
        "certificates": certificates,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Finite Row Proof-Extraction Certificates",
        "",
        "These certificates compress the heavy finite-row reports into the",
        "counts and hashes needed for theorem-facing proof extraction.",
        "",
        "## Rows",
        "",
        "| row | ring | packets | H3 cells/orbits | H4 cells/orbits | raw atoms | raw pairs | full residual | support residual |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    for cert in payload["certificates"]:
        packets = ", ".join(
            f"{key}:{value}" for key, value in cert["constructor"]["packets"].items()
        )
        h3 = cert.get("h3") or {}
        h4 = cert.get("h4") or {}
        ext = cert["ext_ch"]
        full = ext.get("full_block_coboundary") or {}
        support = ext.get("support_projection_coboundary") or {}
        lines.append(
            "| {row} | {ring} | {packets} | {h3_cells}/{h3_orbits} | "
            "{h4_cells}/{h4_orbits} | {atoms} | {pairs} | {full_res} | "
            "{support_res} |".format(
                row=cert["row_key"],
                ring=cert["ring"],
                packets=packets,
                h3_cells=h3.get("cells", "n/a"),
                h3_orbits=h3.get("orbits", "n/a"),
                h4_cells=h4.get("cells", "n/a"),
                h4_orbits=h4.get("orbits", "n/a"),
                atoms=ext["raw_atom_count"],
                pairs=ext["raw_pair_count"],
                full_res=full.get("residual_support", "n/a"),
                support_res=support.get("residual_support", "n/a"),
            )
        )

    lines += ["", "## Source Hashes", ""]
    for cert in payload["certificates"]:
        lines += [f"### {cert['row_key']}", ""]
        for source in cert["sources"]:
            lines.append(f"- `{source['path']}`")
            lines.append(f"  - sha256: `{source['sha256']}`")
            lines.append(f"  - bytes: `{source['bytes']}`")
        lines.append("")

    lines += [
        "## Reading",
        "",
        "The full residual column is the filtered-adjacency obstruction.  The",
        "support residual column is deliberately separate: rows with support",
        "residual `0` and full residual nonzero are the finite counterexamples",
        "to support-level closure implying filtered closure.",
    ]
    return "\n".join(lines) + "\n"


def check_payload(payload: dict[str, Any], path: Path) -> None:
    recorded = load_json(path)
    normalized_payload = json.loads(json.dumps(payload))
    if recorded != normalized_payload:
        recorded_rows = [item.get("row_key") for item in recorded.get("certificates", [])]
        computed_rows = [item.get("row_key") for item in normalized_payload.get("certificates", [])]
        if recorded_rows != computed_rows:
            raise AssertionError(
                f"row keys differ: recorded={recorded_rows} computed={computed_rows}"
            )
        raise AssertionError(f"certificate payload differs from {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rows",
        default=",".join(ROW_SOURCES),
        help="comma-separated row keys",
    )
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_MD)
    parser.add_argument(
        "--check",
        type=Path,
        default=None,
        help="recompute and compare against an existing JSON certificate report",
    )
    args = parser.parse_args()

    row_keys = [key.strip() for key in args.rows.split(",") if key.strip()]
    unknown = sorted(set(row_keys) - set(ROW_SOURCES))
    if unknown:
        raise ValueError(f"unknown row keys: {', '.join(unknown)}")

    payload = build_payload(row_keys)
    if args.check is not None:
        check_payload(payload, args.check)
        print(f"checked {args.check}")
        return

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_markdown(payload), encoding="utf-8")

    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
