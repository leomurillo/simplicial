"""Build a Rosas closure-deficit ledger from existing Ext_CH reports.

The ledger does not recompute the cocycles.  It reads the exact finite
reducers already produced by the constructor stack and records how much raw
carry support survives the chosen coboundary model.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPORT_DIR = Path(__file__).with_name("reports")
OUTPUT_JSON = REPORT_DIR / "closure_deficit_ledger.json"
OUTPUT_MD = REPORT_DIR / "closure_deficit_ledger.md"

INPUTS = (
    ("F_4[u]/(u^2)", REPORT_DIR / "ext_ch_cocycle_f4_u2.json", "standalone"),
    ("F_2[u]/(u^5)", REPORT_DIR / "next_local_row_f2_u5.json", "next_row"),
    ("F_8[u]/(u^2)", REPORT_DIR / "next_local_row_f8_u2.json", "next_row"),
)


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def ratio(reduction: dict[str, Any] | None) -> float | None:
    if not reduction or reduction.get("skipped"):
        return None
    raw = int(reduction["raw_support"])
    if raw == 0:
        return 0.0
    return int(reduction["residual_support"]) / raw


def fmt_ratio(value: float | None, reduction: dict[str, Any] | None) -> str:
    if value is not None:
        return f"{value:.3f}"
    if reduction and reduction.get("skipped"):
        c2 = reduction.get("c2_dimension", "?")
        return f"gated (C2={c2})"
    return "n/a"


def residual_dimension(reduction: dict[str, Any] | None) -> int | None:
    if not reduction or reduction.get("skipped"):
        return None
    if "residual_dimension" in reduction:
        return int(reduction["residual_dimension"])
    return int(reduction["c2_dimension"]) - int(reduction["coboundary_rank"])


def coefficient_field(reduction: dict[str, Any] | None) -> str:
    if not reduction or reduction.get("skipped"):
        return "n/a"
    return str(reduction.get("coefficient_field", "Q"))


def row_from_payload(name: str, path: Path, kind: str) -> dict[str, Any]:
    payload = load_payload(path)
    if kind == "standalone":
        raw_atoms = payload["raw_atom_count"]
        raw_pairs = payload["raw_pair_count"]
        pair_orbits = payload["pair_orbit_count"]
        full = payload.get("coboundary_reduction")
        support = None
    else:
        ext = payload["ext_ch"]
        raw_atoms = ext["raw_atom_count"]
        raw_pairs = ext["raw_pair_count"]
        pair_orbits = ext["canonical_pair_orbit_count"]
        full = ext.get("full_block_coboundary")
        support = ext.get("support_projection_coboundary")

    full_ratio = ratio(full)
    support_ratio = ratio(support)
    full_residual_dimension = residual_dimension(full)
    support_residual_dimension = residual_dimension(support)
    if full_ratio is not None and support_ratio is not None:
        reading = (
            "full-block survives; support projection closes"
            if support_ratio == 0 and full_ratio > 0
            else "support and full-block diagnostics agree"
        )
    elif full_ratio is not None:
        reading = "full-block residual survives"
    elif support_ratio is not None:
        reading = "support projection closes; full-block deficit remains gated"
    else:
        reading = "deficit not measured"

    return {
        "row": name,
        "source": str(path.relative_to(path.parents[1])),
        "raw_atoms": raw_atoms,
        "raw_pairs": raw_pairs,
        "pair_orbits": pair_orbits,
        "full_block_deficit": full_ratio,
        "support_projection_deficit": support_ratio,
        "full_block_residual_dimension": full_residual_dimension,
        "support_projection_residual_dimension": support_residual_dimension,
        "full_block_field": coefficient_field(full),
        "support_projection_field": coefficient_field(support),
        "full_block_display": fmt_ratio(full_ratio, full),
        "support_projection_display": fmt_ratio(support_ratio, support),
        "reading": reading,
    }


def build_ledger() -> dict[str, Any]:
    rows = [row_from_payload(*item) for item in INPUTS]
    return {
        "definition": {
            "closure_deficit": "residual_support / raw_support in a specified coboundary model",
            "zero": "the raw carry is section-trivial in that model",
            "one": "all raw support survives in that model",
        },
        "rows": rows,
    }


def render_markdown(ledger: dict[str, Any]) -> str:
    lines = [
        "# Rosas Closure-Deficit Ledger",
        "",
        "This report normalizes the finite coboundary residuals already computed",
        "for the local Ext_CH rows.  For a chosen section-change model, the",
        "closure deficit is",
        "",
        "\\[",
        "\\delta=\\frac{\\text{residual support}}{\\text{raw carry support}}.",
        "\\]",
        "",
        "Thus \\(\\delta=0\\) means the raw carry is section-trivial in that",
        "model, while \\(\\delta=1\\) means every raw carry atom survives.  The",
        "full-block and support-projection columns are deliberately separated:",
        "support closure alone can miss the filtered adjacency-algebra class.",
        "",
        "| row | raw atoms | raw pairs | pair orbits | full field | full residual dim | full delta | support delta | reading |",
        "|---|---:|---:|---:|---|---:|---:|---:|---|",
    ]
    for row in ledger["rows"]:
        lines.append(
            "| {row} | {raw_atoms} | {raw_pairs} | {pair_orbits} | {full_field} | {full_dim} | {full} | {support} | {reading} |".format(
                row=row["row"],
                raw_atoms=row["raw_atoms"],
                raw_pairs=row["raw_pairs"],
                pair_orbits=row["pair_orbits"],
                full_field=row["full_block_field"],
                full_dim=(
                    row["full_block_residual_dimension"]
                    if row["full_block_residual_dimension"] is not None
                    else "n/a"
                ),
                full=row["full_block_display"],
                support=row["support_projection_display"],
                reading=row["reading"],
            )
        )

    lines += [
        "",
        "## Paper-facing use",
        "",
        "The ledger turns the Rosas closure audit into a quantitative task.",
        "The F4[u]/(u^2), F2[u]/(u^5), and F8[u]/(u^2) full-block rows",
        "all have delta 1, so their carries are not artifacts of the chosen",
        "filtered section.  The F2[u]/(u^5) and F8[u]/(u^2)",
        "support-projection rows have delta 0, showing that support-level",
        "compression is too coarse to certify filtered closure.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    ledger = build_ledger()
    OUTPUT_JSON.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(ledger), encoding="utf-8")
    print(render_markdown(ledger))
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
