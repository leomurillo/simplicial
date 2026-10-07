"""Range scan for Cotton-York invariant obstruction in the Z6 testbed.

This is Path B from the Paper 28 T*1' attack: estimate the ranges of the
scale-free Cotton-York invariant I for

  1. the physical mass-weighted shape metric, sampled in (rho,u,w), and
  2. the Z6 Fisher metric restricted to V2+V3, sampled inside the simplex.

If the sampled intervals are robustly disjoint, that is strong evidence for a
global obstruction.  It is not a proof until upgraded to certified bounds.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from z6_cotton_york_obstruction_audit import cotton_york, fisher_sector_metric
from z6_jacobi_fisher_execution_audit import shape_metric, sides_from_sigma, shape_quality_from_sides


def sample_shape_points(args: argparse.Namespace) -> list[np.ndarray]:
    rng = np.random.default_rng(args.seed)
    rho0 = math.log(args.perimeter0)
    points = []
    attempts = 0
    while len(points) < args.shape_samples and attempts < args.shape_samples * 100:
        attempts += 1
        sigma = np.array(
            [
                rho0 + rng.uniform(-args.rho_radius, args.rho_radius),
                rng.uniform(-args.contrast_radius, args.contrast_radius),
                rng.uniform(-args.contrast_radius, args.contrast_radius),
            ]
        )
        if shape_quality_from_sides(sides_from_sigma(sigma)) >= args.min_shape_quality:
            points.append(sigma)
    return points


def sample_fisher_points(args: argparse.Namespace) -> list[np.ndarray]:
    rng = np.random.default_rng(args.seed + 1)
    points = []
    attempts = 0
    while len(points) < args.fisher_samples and attempts < args.fisher_samples * 100:
        attempts += 1
        x = rng.uniform(-args.fisher_radius, args.fisher_radius, size=3)
        try:
            fisher_sector_metric(x, args.epsilon)
        except ValueError:
            continue
        points.append(x)
    return points


def invariant_range(values: list[float]) -> dict:
    arr = np.array(values, dtype=float)
    return {
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "mean": float(np.mean(arr)),
        "p05": float(np.quantile(arr, 0.05)),
        "p95": float(np.quantile(arr, 0.95)),
    }


def scan(args: argparse.Namespace) -> dict:
    masses = np.array(args.masses, dtype=float)
    shape_fn = lambda sigma: shape_metric(sigma, masses, args.metric_step)
    fisher_fn = lambda x: fisher_sector_metric(x, args.epsilon)
    shape_values = []
    fisher_values = []
    shape_failures = 0
    fisher_failures = 0
    for sigma in sample_shape_points(args):
        try:
            value = cotton_york(shape_fn, sigma, args.curvature_step)["I"]
            if value is None or not np.isfinite(value):
                shape_failures += 1
            else:
                shape_values.append(float(value))
        except Exception:
            shape_failures += 1
    for x in sample_fisher_points(args):
        try:
            value = cotton_york(fisher_fn, x, args.curvature_step)["I"]
            if value is None or not np.isfinite(value):
                fisher_failures += 1
            else:
                fisher_values.append(float(value))
        except Exception:
            fisher_failures += 1
    shape_range = invariant_range(shape_values)
    fisher_range = invariant_range(fisher_values)
    overlap = not (shape_range["max"] < fisher_range["min"] or fisher_range["max"] < shape_range["min"])
    robust_overlap = not (shape_range["p95"] < fisher_range["p05"] or fisher_range["p95"] < shape_range["p05"])
    status = "DISJOINT_EVIDENCE" if not overlap else "OVERLAP_OR_INCONCLUSIVE"
    return {
        "claim_tested": "sampled Cotton-York invariant range separation for Z6 Jacobi-Fisher obstruction",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "summary": {
            "status": status,
            "sampled_interval_overlap": overlap,
            "sampled_5_95_overlap": robust_overlap,
            "shape_range": shape_range,
            "fisher_range": fisher_range,
            "shape_count": len(shape_values),
            "fisher_count": len(fisher_values),
            "shape_failures": shape_failures,
            "fisher_failures": fisher_failures,
        },
        "shape_values": shape_values,
        "fisher_values": fisher_values,
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    sr = s["shape_range"]
    fr = s["fisher_range"]
    lines = [
        "# Z6 Cotton-York Range Scan",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- sampled interval overlap: {s['sampled_interval_overlap']}",
        f"- sampled 5-95% overlap: {s['sampled_5_95_overlap']}",
        f"- shape samples used/failures: {s['shape_count']} / {s['shape_failures']}",
        f"- Fisher samples used/failures: {s['fisher_count']} / {s['fisher_failures']}",
        "",
        "## Ranges",
        "",
        "| side | min | p05 | mean | p95 | max |",
        "|---|---:|---:|---:|---:|---:|",
        f"| shape | {sr['min']:.6e} | {sr['p05']:.6e} | {sr['mean']:.6e} | {sr['p95']:.6e} | {sr['max']:.6e} |",
        f"| Fisher | {fr['min']:.6e} | {fr['p05']:.6e} | {fr['mean']:.6e} | {fr['p95']:.6e} | {fr['max']:.6e} |",
        "",
        "## Interpretation",
        "",
        "DISJOINT_EVIDENCE is not a theorem. It is a target for certified interval",
        "bounds or a symbolic range proof. OVERLAP_OR_INCONCLUSIVE means Z6 is not",
        "globally killed by this sampled scalar invariant alone.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--perimeter0", type=float, default=3.0)
    parser.add_argument("--shape-samples", type=int, default=24)
    parser.add_argument("--fisher-samples", type=int, default=24)
    parser.add_argument("--rho-radius", type=float, default=0.15)
    parser.add_argument("--contrast-radius", type=float, default=0.2)
    parser.add_argument("--fisher-radius", type=float, default=0.35)
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--metric-step", type=float, default=1.0e-5)
    parser.add_argument("--curvature-step", type=float, default=3.0e-4)
    parser.add_argument("--min-shape-quality", type=float, default=1.0e-3)
    parser.add_argument("--seed", type=int, default=6626)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_cotton_york_range_scan.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_cotton_york_range_scan.json"),
    )
    args = parser.parse_args()
    result = scan(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
