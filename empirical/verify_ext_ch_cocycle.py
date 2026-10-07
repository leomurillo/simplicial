"""Verify and export the canonical Ext_CH cocycle representative."""

from __future__ import annotations

import argparse
from pathlib import Path

from cocycle_reducer import CocycleReducer, write_reports
from local_adjacency_constructor import LocalAdjacencyConstructor, make_f4_u2_ring


REPORT_JSON = Path(__file__).with_name("reports") / "ext_ch_cocycle_f4_u2.json"
REPORT_MD = Path(__file__).with_name("reports") / "ext_ch_cocycle_f4_u2.md"


def check_equal(name: str, actual: object, expected: object) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--coboundary-mode",
        choices=["full_block", "support", "off_support"],
        default="full_block",
        help="finite section-change model to use for the coboundary diagnostic",
    )
    args = parser.parse_args()

    reducer = CocycleReducer(LocalAdjacencyConstructor(make_f4_u2_ring()))
    payload = reducer.summary(coboundary_mode=args.coboundary_mode)

    check_equal("raw atom count", payload["raw_atom_count"], 1569)
    check_equal("raw carry pair count", payload["raw_pair_count"], 369)
    check_equal("atom orbit count", payload["atom_orbit_count"], 71)
    check_equal("pair orbit count", payload["pair_orbit_count"], 20)
    check_equal("atom orbit missing total", payload["atom_orbit_missing_total"], 0)
    check_equal("pair orbit missing total", payload["pair_orbit_missing_total"], 0)
    check_equal("raw coefficient distribution", payload["raw_coefficient_distribution"], {"-1": 1569})

    reduction = payload["coboundary_reduction"]
    check_equal("coboundary raw support", reduction["raw_support"], 1569)
    check_equal("coboundary residual support", reduction["residual_support"], 1569)
    check_equal("raw is not coboundary", reduction["raw_is_coboundary"], False)

    write_reports(payload, json_path=REPORT_JSON, markdown_path=REPORT_MD)
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()

