"""Project cyclic centroid displacements onto conductor leaves.

This runner is the finite, executable version of the "critical leaf" probe
for the C7 and C12 output algebras.  It treats a regular leaf as a nonempty
subset of cyclic conductor packets, projects each centroid displacement onto
that packet support in the DFT basis, and scores the projected step with the
existing K^CH controller.

The script intentionally reports both the controller's cubic fraction and the
closure leakage of the K^CH response outside the selected packet support.  The
former is the local carry size used by k_ch_step_controller.py; the latter is
the finite-atlas support closure defect for this conductor-leaf proxy.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from k_ch_step_controller import (
    PRESETS,
    StepControllerConfig,
    control_step,
    conductor_packets,
    cyclic_packet_energy,
    fisher_norm,
    k_ch_raise,
    labels_for,
    load_centroids,
    project_tangent,
)


EPS = 1e-12
ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "empirical" / "reports"


def default_runs() -> list[dict[str, str]]:
    """Workspace-local centroid sources that already exist in this project."""

    candidates = [
        {
            "preset": "weekdays",
            "model_tag": "llama31_8b",
            "centroids": str(ROOT / "weekdays" / "baseline" / "per_class_output_dists.safetensors"),
        },
        {
            "preset": "months",
            "model_tag": "llama31_8b",
            "centroids": str(ROOT / "months" / "baseline" / "per_class_output_dists.safetensors"),
        },
        {
            "preset": "weekdays",
            "model_tag": "mistral_7b",
            "centroids": str(ROOT / "per_class_output_dists.safetensors"),
        },
    ]
    return [item for item in candidates if Path(item["centroids"]).exists()]


def parse_run_spec(spec: str) -> dict[str, str]:
    """Parse preset:model_tag:path."""

    parts = spec.split(":", 2)
    if len(parts) != 3:
        raise ValueError("--run entries must be preset:model_tag:path")
    preset, model_tag, centroids = parts
    if preset not in PRESETS:
        raise ValueError(f"unknown preset {preset!r}; expected one of {sorted(PRESETS)}")
    return {"preset": preset, "model_tag": model_tag, "centroids": centroids}


def selected_frequencies(n: int, conductors: tuple[int, ...]) -> list[int]:
    packets = conductor_packets(n)
    ks: list[int] = []
    for conductor in conductors:
        ks.extend(packets[conductor])
    return sorted(set(ks))


def project_to_conductors(vector: np.ndarray, conductors: tuple[int, ...]) -> np.ndarray:
    """Orthogonally project a real zero-sum vector onto cyclic conductor support."""

    n = int(vector.size)
    coeff = np.fft.fft(project_tangent(vector))
    keep = np.zeros(n, dtype=bool)
    keep[selected_frequencies(n, conductors)] = True
    keep[0] = False
    projected = np.fft.ifft(np.where(keep, coeff, 0.0)).real
    return project_tangent(projected)


def energy_fraction(p: np.ndarray, numerator: np.ndarray, denominator: np.ndarray) -> float:
    denom = fisher_norm(p, denominator)
    if denom <= EPS:
        return 0.0
    num = fisher_norm(p, numerator)
    return float((num * num) / (denom * denom))


def closure_leakage_fraction(p: np.ndarray, kch: np.ndarray, conductors: tuple[int, ...]) -> float:
    total = fisher_norm(p, kch)
    if total <= EPS:
        return 0.0
    closed = project_to_conductors(kch, conductors)
    leak = project_tangent(kch - closed)
    leak_norm = fisher_norm(p, leak)
    return float((leak_norm * leak_norm) / (total * total))


def leaf_name(conductors: tuple[int, ...], all_conductors: tuple[int, ...]) -> str:
    if conductors == all_conductors:
        return "full_nontrivial"
    return "+".join(f"conductor_{d}" for d in conductors)


def packet_balance(packet_means: dict[str, float], conductors: tuple[int, ...]) -> float:
    if not conductors:
        return 0.0
    target = 1.0 / len(conductors)
    return 0.5 * sum(abs(packet_means.get(f"conductor_{d}", 0.0) - target) for d in conductors)


def summarize_leaf(
    *,
    centroids: np.ndarray,
    labels: tuple[str, ...],
    conductors: tuple[int, ...],
    all_conductors: tuple[int, ...],
    config: StepControllerConfig,
    min_retained_fraction: float,
) -> dict[str, Any]:
    n = int(centroids.shape[0])
    p_star = np.full(n, 1.0 / n)
    rows: list[dict[str, Any]] = []
    packet_rows: list[dict[str, float]] = []

    for i, label in enumerate(labels):
        h = project_tangent(centroids[i] - p_star)
        h_leaf = project_to_conductors(h, conductors)
        h_residual = project_tangent(h - h_leaf)
        diagnostic = control_step(
            p_star,
            h_leaf,
            config=config,
            name=f"uniform -> {label} [{leaf_name(conductors, all_conductors)}]",
            base_label="uniform",
            target_label=label,
            cyclic_packets=True,
        )
        kch = k_ch_raise(p_star, h_leaf, h_leaf)
        retained = energy_fraction(p_star, h_leaf, h)
        packet_energy = cyclic_packet_energy(h_leaf)
        packet_rows.append(packet_energy)
        rows.append(
            {
                "label": label,
                "retained_fisher_fraction": retained,
                "displacement_leakage_fraction": energy_fraction(p_star, h_residual, h),
                "rho": diagnostic.original_directional_rho,
                "rho_frac": diagnostic.original_cubic_fraction,
                "kch_norm": diagnostic.original_kch_norm,
                "fisher_norm": diagnostic.original_fisher_norm,
                "kch_closure_leakage_fraction": closure_leakage_fraction(p_star, kch, conductors),
                "packet_energy_step": packet_energy,
                "packet_energy_kch": diagnostic.packet_energy_kch,
            }
        )
        rows[-1]["balanced_leakage"] = rows[-1]["rho_frac"] * math.sqrt(
            rows[-1]["kch_closure_leakage_fraction"]
        )

    def mean_field(name: str) -> float:
        return float(np.mean([row[name] for row in rows]))

    packet_keys = [f"conductor_{d}" for d in conductors]
    packet_means = {
        key: float(np.mean([packet.get(key, 0.0) for packet in packet_rows]))
        for key in packet_keys
    }
    mean_retained = mean_field("retained_fisher_fraction")
    mean_rho_frac = mean_field("rho_frac")
    mean_closure = mean_field("kch_closure_leakage_fraction")
    mean_kch_norm = mean_field("kch_norm")
    mean_balanced_leakage = mean_field("balanced_leakage")
    return {
        "leaf": leaf_name(conductors, all_conductors),
        "conductors": list(conductors),
        "character_indices": selected_frequencies(n, conductors),
        "is_full_nontrivial": conductors == all_conductors,
        "is_regular_by_retention": mean_retained >= min_retained_fraction,
        "is_quadratically_flat": mean_kch_norm <= 1e-10 and mean_rho_frac <= 1e-10,
        "mean_retained_fisher_fraction": mean_retained,
        "mean_displacement_leakage_fraction": mean_field("displacement_leakage_fraction"),
        "mean_rho": mean_field("rho"),
        "mean_rho_frac": mean_rho_frac,
        "mean_kch_norm": mean_kch_norm,
        "mean_balanced_leakage": mean_balanced_leakage,
        "max_rho_frac": float(np.max([row["rho_frac"] for row in rows])),
        "mean_kch_closure_leakage_fraction": mean_closure,
        "max_kch_closure_leakage_fraction": float(np.max([row["kch_closure_leakage_fraction"] for row in rows])),
        "mean_packet_energy_step": packet_means,
        "packet_balance_l1_to_uniform": packet_balance(packet_means, conductors),
        "score": mean_rho_frac,
        "closure_weighted_score": mean_rho_frac * (1.0 + mean_closure),
        "balanced_leakage_score": mean_balanced_leakage,
        "per_label": rows,
    }


def conductor_subsets(n: int) -> list[tuple[int, ...]]:
    conductors = tuple(sorted(conductor_packets(n)))
    out: list[tuple[int, ...]] = []
    for r in range(1, len(conductors) + 1):
        out.extend(tuple(combo) for combo in itertools.combinations(conductors, r))
    return out


def run_one(
    *,
    preset: str,
    model_tag: str,
    centroids_path: Path,
    config: StepControllerConfig,
    min_retained_fraction: float,
) -> dict[str, Any]:
    centroids = load_centroids(centroids_path)
    labels = labels_for(preset, centroids.shape[0])
    expected = len(PRESETS[preset])
    if centroids.shape != (expected, expected):
        raise ValueError(
            f"{preset}/{model_tag} expected a {expected}x{expected} centroid matrix, "
            f"got {centroids.shape} from {centroids_path}"
        )

    all_conductors = tuple(sorted(conductor_packets(expected)))
    leaves = [
        summarize_leaf(
            centroids=centroids,
            labels=labels,
            conductors=conductors,
            all_conductors=all_conductors,
            config=config,
            min_retained_fraction=min_retained_fraction,
        )
        for conductors in conductor_subsets(expected)
    ]
    regular = [leaf for leaf in leaves if leaf["is_regular_by_retention"]]
    proper_regular = [leaf for leaf in regular if not leaf["is_full_nontrivial"]]
    nonflat_regular = [leaf for leaf in regular if not leaf["is_quadratically_flat"]]
    proper_nonflat = [
        leaf for leaf in nonflat_regular
        if not leaf["is_full_nontrivial"]
    ]
    best_regular = min(regular, key=lambda item: item["score"]) if regular else None
    best_proper = min(proper_regular, key=lambda item: item["score"]) if proper_regular else None
    best_nonflat = min(nonflat_regular, key=lambda item: item["score"]) if nonflat_regular else None
    best_proper_nonflat = min(proper_nonflat, key=lambda item: item["score"]) if proper_nonflat else None
    best_closure = min(regular, key=lambda item: item["closure_weighted_score"]) if regular else None
    best_balanced = min(regular, key=lambda item: item["balanced_leakage_score"]) if regular else None

    return {
        "preset": preset,
        "model_tag": model_tag,
        "centroids": str(centroids_path),
        "labels": labels,
        "n": expected,
        "all_conductors": all_conductors,
        "min_retained_fraction": min_retained_fraction,
        "best_regular_by_rho_frac": best_regular["leaf"] if best_regular else None,
        "best_proper_by_rho_frac": best_proper["leaf"] if best_proper else None,
        "best_nonflat_by_rho_frac": best_nonflat["leaf"] if best_nonflat else None,
        "best_proper_nonflat_by_rho_frac": best_proper_nonflat["leaf"] if best_proper_nonflat else None,
        "best_regular_by_closure_weighted_score": best_closure["leaf"] if best_closure else None,
        "best_regular_by_balanced_leakage": best_balanced["leaf"] if best_balanced else None,
        "leaves": sorted(leaves, key=lambda item: item["score"]),
    }


def json_ready(obj: Any) -> Any:
    if isinstance(obj, float):
        if math.isnan(obj):
            return "nan"
        if math.isinf(obj):
            return "inf"
        return round(obj, 12)
    if isinstance(obj, tuple):
        return [json_ready(x) for x in obj]
    if isinstance(obj, list):
        return [json_ready(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): json_ready(v) for k, v in obj.items()}
    return obj


def fmt(value: float) -> str:
    return f"{value:.6f}"


def make_report(results: list[dict[str, Any]], *, output_json: Path) -> str:
    lines = [
        "# Critical Leaf Projection Census",
        "",
        "## Status",
        "",
        f"- JSON artifact: `{output_json}`",
        "- leaf model: nonempty cyclic conductor-packet subsets in the DFT basis",
        "- leakage score: mean `rho_frac = 0.5 ||K^CH_p(s)s||_p / ||s||_p` after projection",
        "- closure defect: fraction of the projected step's K^CH response outside the selected conductor support",
        "- balanced leakage: mean `rho_frac * sqrt(closure defect)`, the outside cubic budget proxy",
        "",
        "This is an empirical conductor-leaf proxy. It is a finite audit artifact, not by itself a proof of the RH reduction.",
        "",
    ]

    for result in results:
        lines += [
            f"## {result['preset']} / {result['model_tag']}",
            "",
            f"- centroid source: `{result['centroids']}`",
            f"- conductors: `{', '.join(str(x) for x in result['all_conductors'])}`",
            f"- best regular leaf by rho_frac: `{result['best_regular_by_rho_frac']}`",
            f"- best proper leaf by rho_frac: `{result['best_proper_by_rho_frac']}`",
            f"- best non-flat leaf by rho_frac: `{result['best_nonflat_by_rho_frac']}`",
            f"- best proper non-flat leaf by rho_frac: `{result['best_proper_nonflat_by_rho_frac']}`",
            f"- best regular leaf by closure-weighted score: `{result['best_regular_by_closure_weighted_score']}`",
            f"- best regular leaf by balanced leakage: `{result['best_regular_by_balanced_leakage']}`",
            "",
            "| rank | leaf | retained Fisher frac | rho | rho_frac | KCH norm | closure leakage | balanced leakage | packet balance | flags |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
        for rank, leaf in enumerate(result["leaves"][:12], start=1):
            flags = []
            if leaf["is_full_nontrivial"]:
                flags.append("full")
            if leaf["is_quadratically_flat"]:
                flags.append("flat")
            lines.append(
                f"| {rank} | `{leaf['leaf']}` | "
                f"{fmt(leaf['mean_retained_fisher_fraction'])} | "
                f"{fmt(leaf['mean_rho'])} | "
                f"{fmt(leaf['mean_rho_frac'])} | "
                f"{fmt(leaf['mean_kch_norm'])} | "
                f"{fmt(leaf['mean_kch_closure_leakage_fraction'])} | "
                f"{fmt(leaf['mean_balanced_leakage'])} | "
                f"{fmt(leaf['packet_balance_l1_to_uniform'])} | "
                f"{', '.join(flags) if flags else 'regular'} |"
            )
        lines += [
            "",
            "### Best Leaf Detail",
            "",
        ]
        best_name = result["best_regular_by_rho_frac"]
        best = next(leaf for leaf in result["leaves"] if leaf["leaf"] == best_name)
        lines += [
            "| label | retained Fisher frac | rho_frac | closure leakage | balanced leakage |",
            "|---|---:|---:|---:|---:|",
        ]
        for row in best["per_label"]:
            lines.append(
                f"| {row['label']} | {fmt(row['retained_fisher_fraction'])} | "
                f"{fmt(row['rho_frac'])} | {fmt(row['kch_closure_leakage_fraction'])} | "
                f"{fmt(row['balanced_leakage'])} |"
            )
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--run",
        action="append",
        default=None,
        help="Run spec preset:model_tag:path. May be supplied more than once.",
    )
    parser.add_argument("--max-cubic-fraction", type=float, default=0.10)
    parser.add_argument("--max-fisher-norm", type=float, default=None)
    parser.add_argument("--min-probability", type=float, default=1e-9)
    parser.add_argument("--safety", type=float, default=0.98)
    parser.add_argument("--min-retained-fraction", type=float, default=0.05)
    parser.add_argument("--report", type=Path, default=REPORTS / "critical_leaf_projection_census.md")
    parser.add_argument("--json", type=Path, default=REPORTS / "critical_leaf_projection_census.json")
    args = parser.parse_args()

    run_specs = [parse_run_spec(spec) for spec in args.run] if args.run else default_runs()
    if not run_specs:
        raise SystemExit("No centroid sources found. Provide at least one --run preset:model_tag:path.")

    config = StepControllerConfig(
        max_cubic_fraction=args.max_cubic_fraction,
        max_fisher_norm=args.max_fisher_norm,
        min_probability=args.min_probability,
        safety=args.safety,
    )
    results = [
        run_one(
            preset=spec["preset"],
            model_tag=spec["model_tag"],
            centroids_path=Path(spec["centroids"]),
            config=config,
            min_retained_fraction=args.min_retained_fraction,
        )
        for spec in run_specs
    ]

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(json_ready({"runs": results}), indent=2), encoding="utf-8")
    args.report.write_text(make_report(results, output_json=args.json), encoding="utf-8")

    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(
        json.dumps(
            json_ready(
                {
                    f"{result['preset']}/{result['model_tag']}": {
                        "best_regular_by_rho_frac": result["best_regular_by_rho_frac"],
                        "best_proper_by_rho_frac": result["best_proper_by_rho_frac"],
                        "best_nonflat_by_rho_frac": result["best_nonflat_by_rho_frac"],
                        "best_proper_nonflat_by_rho_frac": result["best_proper_nonflat_by_rho_frac"],
                        "best_regular_by_closure_weighted_score": result["best_regular_by_closure_weighted_score"],
                        "best_regular_by_balanced_leakage": result["best_regular_by_balanced_leakage"],
                    }
                    for result in results
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
