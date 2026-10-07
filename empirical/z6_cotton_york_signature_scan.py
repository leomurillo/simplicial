"""Cotton-York eigen-signature scan for the Z6 Jacobi-Fisher obstruction.

The scalar I=(tr CY^3)^2/(tr CY^2)^3 can overlap even when the full
scale-free eigenvalue signature does not.  This audit computes normalized
eigenvalues of the mixed Cotton-York tensor, sorted and scaled to unit
Euclidean norm, and compares sampled physical-shape signatures against sampled
Z6 Fisher-sector signatures by nearest-neighbor distance.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from z6_cotton_york_obstruction_audit import cotton_york, fisher_sector_metric
from z6_jacobi_fisher_execution_audit import shape_metric, sides_from_sigma, shape_quality_from_sides


def signature(eigenvalues: list[float]) -> list[float] | None:
    vals = np.sort(np.array(eigenvalues, dtype=float))
    vals -= np.mean(vals)
    norm = float(np.linalg.norm(vals))
    if norm < 1.0e-12:
        return None
    # Fix the sign ambiguity by making the largest-magnitude end positive when needed.
    vals = vals / norm
    if abs(vals[0]) > abs(vals[-1]) and vals[0] > 0:
        vals = -vals
    elif abs(vals[-1]) >= abs(vals[0]) and vals[-1] < 0:
        vals = -vals
    return vals.tolist()


def sample_shape_points(args: argparse.Namespace) -> list[np.ndarray]:
    rng = np.random.default_rng(args.seed)
    rho0 = math.log(args.perimeter0)
    points = []
    while len(points) < args.shape_samples:
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
    while len(points) < args.fisher_samples and attempts < args.fisher_samples * 200:
        attempts += 1
        x = rng.uniform(-args.fisher_radius, args.fisher_radius, size=3)
        try:
            fisher_sector_metric(x, args.epsilon)
        except ValueError:
            continue
        points.append(x)
    return points


def signatures_for(metric_fn, points: list[np.ndarray], h: float) -> tuple[list[list[float]], int]:
    sigs = []
    failures = 0
    for point in points:
        try:
            cy = cotton_york(metric_fn, point, h)
            sig = signature(cy["eigenvalues"])
            if sig is None:
                failures += 1
            else:
                sigs.append(sig)
        except Exception:
            failures += 1
    return sigs, failures


def nearest_distances(source: np.ndarray, target: np.ndarray) -> np.ndarray:
    dists = []
    for row in source:
        diff = target - row[None, :]
        dists.append(float(np.min(np.linalg.norm(diff, axis=1))))
    return np.array(dists)


def scan(args: argparse.Namespace) -> dict:
    masses = np.array(args.masses, dtype=float)
    shape_fn = lambda sigma: shape_metric(sigma, masses, args.metric_step)
    fisher_fn = lambda x: fisher_sector_metric(x, args.epsilon)
    shape_sigs, shape_failures = signatures_for(
        shape_fn, sample_shape_points(args), args.curvature_step
    )
    fisher_sigs, fisher_failures = signatures_for(
        fisher_fn, sample_fisher_points(args), args.curvature_step
    )
    shape_arr = np.array(shape_sigs)
    fisher_arr = np.array(fisher_sigs)
    if len(shape_arr) == 0 or len(fisher_arr) == 0:
        status = "INCONCLUSIVE"
        shape_to_fisher = np.array([float("inf")])
        fisher_to_shape = np.array([float("inf")])
    else:
        shape_to_fisher = nearest_distances(shape_arr, fisher_arr)
        fisher_to_shape = nearest_distances(fisher_arr, shape_arr)
        status = (
            "SEPARATED_EVIDENCE"
            if float(np.min(shape_to_fisher)) > args.signature_tol
            else "OVERLAP_OR_INCONCLUSIVE"
        )
    return {
        "claim_tested": "sampled full Cotton-York normalized eigen-signature separation",
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "summary": {
            "status": status,
            "shape_count": len(shape_sigs),
            "fisher_count": len(fisher_sigs),
            "shape_failures": shape_failures,
            "fisher_failures": fisher_failures,
            "min_shape_to_fisher_distance": float(np.min(shape_to_fisher)),
            "median_shape_to_fisher_distance": float(np.median(shape_to_fisher)),
            "min_fisher_to_shape_distance": float(np.min(fisher_to_shape)),
            "median_fisher_to_shape_distance": float(np.median(fisher_to_shape)),
        },
        "shape_signatures": shape_sigs,
        "fisher_signatures": fisher_sigs,
    }


def write_report(result: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    s = result["summary"]
    lines = [
        "# Z6 Cotton-York Eigen-Signature Scan",
        "",
        f"- Claim tested: {result['claim_tested']}",
        f"- Status: {s['status']}",
        f"- shape signatures/failures: {s['shape_count']} / {s['shape_failures']}",
        f"- Fisher signatures/failures: {s['fisher_count']} / {s['fisher_failures']}",
        f"- min shape-to-Fisher distance: {s['min_shape_to_fisher_distance']:.6e}",
        f"- median shape-to-Fisher distance: {s['median_shape_to_fisher_distance']:.6e}",
        f"- min Fisher-to-shape distance: {s['min_fisher_to_shape_distance']:.6e}",
        f"- median Fisher-to-shape distance: {s['median_fisher_to_shape_distance']:.6e}",
        "",
        "## Interpretation",
        "",
        "SEPARATED_EVIDENCE would motivate a certified eigen-signature obstruction.",
        "OVERLAP_OR_INCONCLUSIVE means sampled full Cotton-York signatures do not",
        "globally kill Z6; a pointwise mismatch still kills the tested point map.",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--masses", nargs=3, type=float, default=[1.0, 1.25, 0.85])
    parser.add_argument("--perimeter0", type=float, default=3.0)
    parser.add_argument("--shape-samples", type=int, default=32)
    parser.add_argument("--fisher-samples", type=int, default=32)
    parser.add_argument("--rho-radius", type=float, default=0.15)
    parser.add_argument("--contrast-radius", type=float, default=0.2)
    parser.add_argument("--fisher-radius", type=float, default=0.35)
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    parser.add_argument("--metric-step", type=float, default=1.0e-5)
    parser.add_argument("--curvature-step", type=float, default=3.0e-4)
    parser.add_argument("--min-shape-quality", type=float, default=1.0e-3)
    parser.add_argument("--signature-tol", type=float, default=2.5e-2)
    parser.add_argument("--seed", type=int, default=6636)
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("empirical/reports/z6_cotton_york_signature_scan.md"),
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("empirical/reports/z6_cotton_york_signature_scan.json"),
    )
    args = parser.parse_args()
    result = scan(args)
    write_report(result, args.report)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
