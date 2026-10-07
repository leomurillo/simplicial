"""Local K^CH trust-region controller for categorical Fisher steps.

This prototype wraps an existing Fisher or natural-gradient proposal in the
output simplex.  It does not try to be a full optimizer.  Given a probability
state p and a proposed tangent step s, it computes the raised Amari-Chentsov
cubic

    K^CH_p(s)s = s*s/p - <s,s>_p p

and shrinks the step when the second-order cubic response is too large
relative to the first-order Fisher step.

When the labels are cyclic C_n, the same diagnostic also reports how the
step and cubic response decompose into conductor packets in the character
basis at the uniform point.  Those packet fractions are diagnostic metadata;
the trust-region scaling itself is based on the categorical Fisher geometry
at the supplied base point p.
"""

from __future__ import annotations

import argparse
import json
import math
import struct
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

import numpy as np


PRESETS: dict[str, tuple[str, ...]] = {
    "weekdays": (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ),
    "months": (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
}

EPS = 1e-12


@dataclass(frozen=True)
class StepControllerConfig:
    """Trust-region knobs for one local categorical step."""

    max_cubic_fraction: float = 0.10
    max_fisher_norm: float | None = None
    min_probability: float = 1e-9
    safety: float = 0.98


@dataclass(frozen=True)
class StepDiagnostic:
    """Full diagnostic payload for one proposed output-simplex step."""

    name: str
    base_label: str | None
    target_label: str | None
    n_labels: int
    original_fisher_norm: float
    original_kch_norm: float
    original_directional_rho: float
    original_cubic_fraction: float
    accepted_scale: float
    controlled_fisher_norm: float
    controlled_kch_norm: float
    controlled_cubic_fraction: float
    positivity_scale: float
    fisher_scale: float
    cubic_scale: float
    min_probability_after_step: float
    sum_after_step: float
    recommendation: str
    active_limits: list[str]
    step: list[float]
    controlled_step: list[float]
    kch_step_step: list[float]
    curve_correction: list[float]
    curve_corrected_step: list[float]
    curve_corrected_min_probability: float
    packet_energy_step: dict[str, float] | None
    packet_energy_kch: dict[str, float] | None


def as_probability(row: Iterable[float], *, min_probability: float = EPS) -> np.ndarray:
    """Return a strictly positive normalized probability vector."""

    p = np.asarray(list(row), dtype=float)
    if p.ndim != 1 or p.size < 2:
        raise ValueError("probability vector must be one-dimensional with at least two entries")
    if not np.all(np.isfinite(p)):
        raise ValueError("probability vector contains non-finite entries")
    if np.any(p < 0.0):
        raise ValueError("probability vector contains negative entries")
    total = float(np.sum(p))
    if total <= 0.0:
        raise ValueError("probability vector has non-positive total mass")
    p = p / total
    if np.any(p < min_probability):
        p = np.maximum(p, min_probability)
        p = p / float(np.sum(p))
    return p


def project_tangent(step: Iterable[float]) -> np.ndarray:
    """Project a vector onto the zero-sum tangent hyperplane."""

    s = np.asarray(list(step), dtype=float)
    if s.ndim != 1:
        raise ValueError("step must be one-dimensional")
    if not np.all(np.isfinite(s)):
        raise ValueError("step contains non-finite entries")
    return s - float(np.mean(s))


def fisher_inner(p: np.ndarray, u: np.ndarray, v: np.ndarray) -> float:
    return float(np.sum(u * v / p))


def fisher_norm(p: np.ndarray, u: np.ndarray) -> float:
    return math.sqrt(max(fisher_inner(p, u, u), 0.0))


def k_ch_raise(p: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Raised Amari-Chentsov cubic in moment coordinates."""

    guv = fisher_inner(p, u, v)
    out = (u * v / p) - guv * p
    return project_tangent(out)


def positivity_scale(p: np.ndarray, step: np.ndarray, min_probability: float) -> float:
    """Largest alpha in [0, inf] such that p + alpha step stays above min_probability."""

    negative = step < 0.0
    if not np.any(negative):
        return float("inf")
    margins = (p[negative] - min_probability) / (-step[negative])
    if margins.size == 0:
        return float("inf")
    return max(0.0, float(np.min(margins)))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conductor_packets(n: int) -> dict[int, list[int]]:
    """Character-index packets for the cyclic group C_n, excluding k=0."""

    packets: dict[int, list[int]] = {}
    for k in range(1, n):
        conductor = n // math.gcd(n, k)
        packets.setdefault(conductor, []).append(k)
    return {d: packets[d] for d in sorted(packets)}


def cyclic_packet_energy(vector: np.ndarray) -> dict[str, float]:
    """Energy fractions by cyclic conductor packet in the unitary DFT basis."""

    n = int(vector.size)
    coeff = np.fft.fft(vector) / math.sqrt(n)
    packets = conductor_packets(n)
    raw: dict[str, float] = {}
    for conductor, ks in packets.items():
        raw[f"conductor_{conductor}"] = float(np.sum(np.abs(coeff[ks]) ** 2).real)
    raw["trivial"] = float(abs(coeff[0]) ** 2)
    nontrivial_total = sum(v for k, v in raw.items() if k != "trivial")
    if nontrivial_total <= EPS:
        return {k: 0.0 for k in raw}
    out = {k: v / nontrivial_total for k, v in raw.items() if k != "trivial"}
    out["trivial"] = raw["trivial"]
    return out


def active_limit_names(
    accepted_scale: float,
    positivity: float,
    fisher: float,
    cubic: float,
    *,
    safety: float,
    tol: float = 1e-9,
) -> list[str]:
    if accepted_scale >= 1.0 - tol:
        return []
    raw_scale = accepted_scale
    if raw_scale > 0.0 and safety > 0.0:
        raw_scale = raw_scale / safety
    limits = []
    if positivity < float("inf") and abs(raw_scale - positivity) <= 1e-6:
        limits.append("positivity")
    if fisher < float("inf") and abs(raw_scale - fisher) <= 1e-6:
        limits.append("fisher_radius")
    if cubic < float("inf") and abs(raw_scale - cubic) <= 1e-6:
        limits.append("cubic_fraction")
    return limits or ["combined"]


def control_step(
    p: Iterable[float],
    proposed_step: Iterable[float],
    *,
    config: StepControllerConfig | None = None,
    name: str = "step",
    base_label: str | None = None,
    target_label: str | None = None,
    cyclic_packets: bool = False,
) -> StepDiagnostic:
    """Diagnose and shrink a proposed Fisher/natural-gradient output step."""

    cfg = config or StepControllerConfig()
    p_arr = as_probability(p, min_probability=cfg.min_probability)
    step = project_tangent(proposed_step)
    if step.size != p_arr.size:
        raise ValueError("p and proposed_step must have the same length")

    step_norm = fisher_norm(p_arr, step)
    kch = k_ch_raise(p_arr, step, step)
    kch_norm = fisher_norm(p_arr, kch)

    if step_norm <= EPS:
        accepted = 1.0
        p_next = p_arr.copy()
        zeros = np.zeros_like(step)
        packets_zero = cyclic_packet_energy(zeros) if cyclic_packets else None
        return StepDiagnostic(
            name=name,
            base_label=base_label,
            target_label=target_label,
            n_labels=int(p_arr.size),
            original_fisher_norm=0.0,
            original_kch_norm=0.0,
            original_directional_rho=0.0,
            original_cubic_fraction=0.0,
            accepted_scale=accepted,
            controlled_fisher_norm=0.0,
            controlled_kch_norm=0.0,
            controlled_cubic_fraction=0.0,
            positivity_scale=float("inf"),
            fisher_scale=float("inf"),
            cubic_scale=float("inf"),
            min_probability_after_step=float(np.min(p_next)),
            sum_after_step=float(np.sum(p_next)),
            recommendation="accept: zero step",
            active_limits=[],
            step=zeros.tolist(),
            controlled_step=zeros.tolist(),
            kch_step_step=zeros.tolist(),
            curve_correction=zeros.tolist(),
            curve_corrected_step=zeros.tolist(),
            curve_corrected_min_probability=float(np.min(p_next)),
            packet_energy_step=packets_zero,
            packet_energy_kch=packets_zero,
        )

    original_directional_rho = kch_norm / max(step_norm * step_norm, EPS)
    original_cubic_fraction = 0.5 * kch_norm / max(step_norm, EPS)

    pos_scale = positivity_scale(p_arr, step, cfg.min_probability)
    fisher_scale = float("inf")
    if cfg.max_fisher_norm is not None:
        fisher_scale = max(0.0, cfg.max_fisher_norm / max(step_norm, EPS))

    cubic_scale = float("inf")
    if original_cubic_fraction > cfg.max_cubic_fraction:
        cubic_scale = max(0.0, cfg.max_cubic_fraction / original_cubic_fraction)

    raw_accepted = min(1.0, pos_scale, fisher_scale, cubic_scale)
    accepted = raw_accepted if raw_accepted >= 1.0 else cfg.safety * raw_accepted

    controlled = accepted * step
    controlled_kch = (accepted * accepted) * kch
    controlled_norm = accepted * step_norm
    controlled_kch_norm = (accepted * accepted) * kch_norm
    controlled_fraction = 0.5 * controlled_kch_norm / max(controlled_norm, EPS)
    p_next = p_arr + controlled

    curve_correction = -0.5 * controlled_kch
    curve_corrected = project_tangent(controlled + curve_correction)
    curve_next = p_arr + curve_corrected

    active_limits = active_limit_names(accepted, pos_scale, fisher_scale, cubic_scale, safety=cfg.safety)
    if not active_limits:
        recommendation = "accept: cubic correction inside trust region"
    elif "cubic_fraction" in active_limits:
        recommendation = "damp: cubic correction exceeds trust fraction"
    elif "positivity" in active_limits:
        recommendation = "damp: step approaches simplex boundary"
    elif "fisher_radius" in active_limits:
        recommendation = "damp: Fisher radius cap is active"
    else:
        recommendation = "damp: multiple trust limits are active"

    return StepDiagnostic(
        name=name,
        base_label=base_label,
        target_label=target_label,
        n_labels=int(p_arr.size),
        original_fisher_norm=float(step_norm),
        original_kch_norm=float(kch_norm),
        original_directional_rho=float(original_directional_rho),
        original_cubic_fraction=float(original_cubic_fraction),
        accepted_scale=float(accepted),
        controlled_fisher_norm=float(controlled_norm),
        controlled_kch_norm=float(controlled_kch_norm),
        controlled_cubic_fraction=float(controlled_fraction),
        positivity_scale=float(pos_scale),
        fisher_scale=float(fisher_scale),
        cubic_scale=float(cubic_scale),
        min_probability_after_step=float(np.min(p_next)),
        sum_after_step=float(np.sum(p_next)),
        recommendation=recommendation,
        active_limits=active_limits,
        step=step.tolist(),
        controlled_step=controlled.tolist(),
        kch_step_step=kch.tolist(),
        curve_correction=curve_correction.tolist(),
        curve_corrected_step=curve_corrected.tolist(),
        curve_corrected_min_probability=float(np.min(curve_next)),
        packet_energy_step=cyclic_packet_energy(step) if cyclic_packets else None,
        packet_energy_kch=cyclic_packet_energy(kch) if cyclic_packets else None,
    )


def load_safetensors(path: Path) -> np.ndarray:
    with path.open("rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        data = f.read()
    key = next(k for k in header if k != "__metadata__")
    meta = header[key]
    dtype = np.float32 if meta["dtype"] == "F32" else np.float64
    shape = meta["shape"]
    start, end = meta["data_offsets"]
    return np.frombuffer(data[start:end], dtype=dtype).reshape(shape).copy()


def load_centroids(path: Path) -> np.ndarray:
    if path.suffix.lower() == ".safetensors":
        arr = load_safetensors(path)
    else:
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload.get("centroids") if isinstance(payload, dict) else payload
        arr = np.asarray(rows, dtype=float)
    if arr.ndim != 2 or arr.shape[0] != arr.shape[1]:
        raise ValueError("centroids must be a square n-by-n matrix")
    arr = np.maximum(arr, 0.0)
    arr = arr / arr.sum(axis=1, keepdims=True)
    return arr


def default_centroid_path(preset: str) -> Path:
    root = Path(__file__).resolve().parent.parent
    return root / preset / "baseline" / "per_class_output_dists.safetensors"


def labels_for(preset: str, n: int) -> tuple[str, ...]:
    labels = PRESETS.get(preset)
    if labels is not None and len(labels) == n:
        return labels
    return tuple(f"label_{i}" for i in range(n))


def build_diagnostics(
    centroids: np.ndarray,
    labels: tuple[str, ...],
    scenario: str,
    config: StepControllerConfig,
    *,
    cyclic_packets: bool,
) -> list[StepDiagnostic]:
    n = centroids.shape[0]
    p_star = np.full(n, 1.0 / n)
    diagnostics: list[StepDiagnostic] = []

    if scenario == "uniform":
        for i, label in enumerate(labels):
            diagnostics.append(
                control_step(
                    p_star,
                    centroids[i] - p_star,
                    config=config,
                    name=f"uniform -> {label}",
                    base_label="uniform",
                    target_label=label,
                    cyclic_packets=cyclic_packets,
                )
            )
        return diagnostics

    if scenario == "adjacent":
        for i, label in enumerate(labels):
            j = (i + 1) % n
            diagnostics.append(
                control_step(
                    centroids[i],
                    centroids[j] - centroids[i],
                    config=config,
                    name=f"{label} -> {labels[j]}",
                    base_label=label,
                    target_label=labels[j],
                    cyclic_packets=cyclic_packets,
                )
            )
        return diagnostics

    if scenario == "all-pairs":
        for i, j in combinations(range(n), 2):
            diagnostics.append(
                control_step(
                    centroids[i],
                    centroids[j] - centroids[i],
                    config=config,
                    name=f"{labels[i]} -> {labels[j]}",
                    base_label=labels[i],
                    target_label=labels[j],
                    cyclic_packets=cyclic_packets,
                )
            )
        return diagnostics

    raise ValueError(f"unknown scenario: {scenario}")


def finite_scale_text(value: float) -> str:
    if math.isinf(value):
        return "inf"
    return f"{value:.6f}"


def aggregate_packet_fractions(
    diagnostics: list[StepDiagnostic],
    field_name: str,
) -> dict[str, float] | None:
    values = [getattr(d, field_name) for d in diagnostics if getattr(d, field_name) is not None]
    if not values:
        return None
    keys = sorted({key for value in values for key in value if key != "trivial"})
    return {key: float(np.mean([value.get(key, 0.0) for value in values])) for key in keys}


def make_report(
    diagnostics: list[StepDiagnostic],
    *,
    preset: str,
    model_tag: str,
    source: Path,
    scenario: str,
    config: StepControllerConfig,
    cyclic_packets: bool,
) -> str:
    scales = np.asarray([d.accepted_scale for d in diagnostics], dtype=float)
    raw_fractions = np.asarray([d.original_cubic_fraction for d in diagnostics], dtype=float)
    controlled_fractions = np.asarray([d.controlled_cubic_fraction for d in diagnostics], dtype=float)
    damped = [d for d in diagnostics if d.accepted_scale < 0.999]
    top = sorted(diagnostics, key=lambda d: d.original_cubic_fraction, reverse=True)[:5]

    lines = [
        f"# K^CH Local Step Controller - {preset} / {model_tag}",
        "",
        "## Status",
        "",
        f"- centroid source: `{source}`",
        f"- scenario: `{scenario}`",
        f"- step count: `{len(diagnostics)}`",
        f"- max cubic fraction: `{config.max_cubic_fraction:.6f}`",
        f"- max Fisher norm: `{finite_scale_text(config.max_fisher_norm) if config.max_fisher_norm is not None else 'none'}`",
        f"- min probability: `{config.min_probability:.3e}`",
        f"- cyclic conductor packet audit: `{'on' if cyclic_packets else 'off'}`",
        "",
        "The controller accepts a proposed output-simplex step `s`, computes",
        "",
        "```text",
        "K^CH_p(s)s = s*s/p - <s,s>_p p",
        "cubic_fraction = 0.5 ||K^CH_p(s)s||_p / ||s||_p",
        "```",
        "",
        "and shrinks the step when the cubic fraction exceeds the configured trust target. The optional curve-correction vector is reported but not applied as the default optimizer action.",
        "",
        "## Summary",
        "",
        f"- damped steps: `{len(damped)}` / `{len(diagnostics)}`",
        f"- accepted-scale min / median: `{float(np.min(scales)):.6f}` / `{float(np.median(scales)):.6f}`",
        f"- raw cubic-fraction max / median: `{float(np.max(raw_fractions)):.6f}` / `{float(np.median(raw_fractions)):.6f}`",
        f"- controlled cubic-fraction max: `{float(np.max(controlled_fractions)):.6f}`",
        "",
        "## Step Table",
        "",
        "| step | ||s||_F | ||Kss||_F | rho=||Kss||/||s||^2 | cubic frac | scale | controlled frac | min p next | action |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for d in diagnostics:
        lines.append(
            f"| {d.name} | {d.original_fisher_norm:.6f} | {d.original_kch_norm:.6f} | "
            f"{d.original_directional_rho:.6f} | {d.original_cubic_fraction:.6f} | "
            f"{d.accepted_scale:.6f} | {d.controlled_cubic_fraction:.6f} | "
            f"{d.min_probability_after_step:.3e} | {d.recommendation} |"
        )

    if cyclic_packets:
        step_packets = aggregate_packet_fractions(diagnostics, "packet_energy_step")
        kch_packets = aggregate_packet_fractions(diagnostics, "packet_energy_kch")
        if step_packets and kch_packets:
            keys = sorted(step_packets)
            lines += [
                "",
                "## Mean Conductor Packet Fractions",
                "",
                "Fractions use the uniform cyclic character decomposition. They are packet metadata for the arithmetic audit, not the trust-region scaling rule.",
                "",
                "| packet | step energy | K^CH response energy |",
                "|---|---:|---:|",
            ]
            for key in keys:
                lines.append(f"| {key} | {step_packets.get(key, 0.0):.6f} | {kch_packets.get(key, 0.0):.6f} |")

    lines += [
        "",
        "## Highest Cubic Fractions",
        "",
        "| step | raw cubic frac | scale | active limits | curve-corrected min p |",
        "|---|---:|---:|---|---:|",
    ]
    for d in top:
        limits = ", ".join(d.active_limits) if d.active_limits else "none"
        lines.append(
            f"| {d.name} | {d.original_cubic_fraction:.6f} | {d.accepted_scale:.6f} | "
            f"{limits} | {d.curve_corrected_min_probability:.3e} |"
        )

    lines += [
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/k_ch_step_controller.py "
        f"--preset {preset} --centroids \"{source}\" --model-tag {model_tag} "
        f"--scenario {scenario} --max-cubic-fraction {config.max_cubic_fraction}",
        "```",
        "",
    ]
    return "\n".join(lines)


def json_ready(obj: Any) -> Any:
    if isinstance(obj, float):
        if math.isinf(obj):
            return "inf"
        if math.isnan(obj):
            return "nan"
        return round(obj, 12)
    if isinstance(obj, list):
        return [json_ready(x) for x in obj]
    if isinstance(obj, dict):
        return {k: json_ready(v) for k, v in obj.items()}
    return obj


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=sorted(PRESETS), default="weekdays")
    parser.add_argument("--centroids", type=Path, default=None)
    parser.add_argument("--model-tag", default="llama31_8b")
    parser.add_argument("--scenario", choices=["uniform", "adjacent", "all-pairs"], default="uniform")
    parser.add_argument("--max-cubic-fraction", type=float, default=0.10)
    parser.add_argument("--max-fisher-norm", type=float, default=None)
    parser.add_argument("--min-probability", type=float, default=1e-9)
    parser.add_argument("--safety", type=float, default=0.98)
    parser.add_argument("--no-packets", action="store_true")
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    source = args.centroids or default_centroid_path(args.preset)
    centroids = load_centroids(source)
    labels = labels_for(args.preset, centroids.shape[0])
    config = StepControllerConfig(
        max_cubic_fraction=args.max_cubic_fraction,
        max_fisher_norm=args.max_fisher_norm,
        min_probability=args.min_probability,
        safety=args.safety,
    )
    cyclic_packets = not args.no_packets
    diagnostics = build_diagnostics(
        centroids,
        labels,
        args.scenario,
        config,
        cyclic_packets=cyclic_packets,
    )

    reports_dir = Path(__file__).resolve().parent / "reports"
    report_path = args.report or reports_dir / f"{args.preset}_k_ch_step_controller_{args.model_tag}_{args.scenario}.md"
    json_path = args.json or reports_dir / f"{args.preset}_k_ch_step_controller_{args.model_tag}_{args.scenario}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(
        make_report(
            diagnostics,
            preset=args.preset,
            model_tag=args.model_tag,
            source=source,
            scenario=args.scenario,
            config=config,
            cyclic_packets=cyclic_packets,
        ),
        encoding="utf-8",
    )
    payload = {
        "preset": args.preset,
        "model_tag": args.model_tag,
        "source": str(source),
        "scenario": args.scenario,
        "config": asdict(config),
        "cyclic_packets": cyclic_packets,
        "diagnostics": [asdict(d) for d in diagnostics],
    }
    json_path.write_text(json.dumps(json_ready(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(
        json.dumps(
            json_ready(
                {
                    "steps": len(diagnostics),
                    "damped": sum(d.accepted_scale < 0.999 for d in diagnostics),
                    "max_raw_cubic_fraction": max(d.original_cubic_fraction for d in diagnostics),
                    "max_controlled_cubic_fraction": max(d.controlled_cubic_fraction for d in diagnostics),
                    "min_accepted_scale": min(d.accepted_scale for d in diagnostics),
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
