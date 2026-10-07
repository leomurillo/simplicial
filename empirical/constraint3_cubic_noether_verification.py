#!/usr/bin/env python3
"""Trajectory-level Constraint 3 cubic Noether audit.

This replaces the retired FFT mean-cube proxy.  It follows Paper 17's local
objects:

    E3(p, v) = 1/2 g_p(v, v) + 1/3 T_p(h, v, v)
    K^CH_p(v, v) = v*v/p - <v, v>_p p

where h = p - p_* and v is an actual Nambu-Fisher vector field on a regular
linear leaf.  The script tests whether the squarefree two-prime conductor
support {2, 3, 6} is closed under the cubic force when embedded in R=6, 12,
and 18.

The diagnostic is not the value of T(h, v, v) alone.  It is the fraction of
the genuine cubic force K^CH(v, v) leaking outside the selected conductor
support along a Nambu-Fisher trajectory.  The known-closed R=6 row supplies the
noise floor.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np


EPS = 1e-14
ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "empirical" / "reports"


@dataclass(frozen=True)
class SeedAudit:
    row: int
    seed: int
    support: list[int]
    outside: list[int]
    min_probability: float
    max_sum_error: float
    mean_abs_normalized_charge: float
    mean_signed_normalized_charge: float
    mean_force_leakage: float
    max_force_leakage: float
    mean_energy_density: float
    energy_density_span: float


@dataclass(frozen=True)
class RowSummary:
    row: int
    support: list[int]
    outside: list[int]
    seeds: int
    mean_abs_normalized_charge: float
    std_abs_normalized_charge: float
    mean_force_leakage: float
    median_force_leakage: float
    max_force_leakage: float
    leakage_snr_vs_z6_floor: float | None
    max_sum_error: float
    min_probability: float
    assessment: str


def project_tangent(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    return vector - float(np.mean(vector))


def fisher_inner(p: np.ndarray, u: np.ndarray, v: np.ndarray) -> float:
    return float(np.sum(u * v / p))


def fisher_norm(p: np.ndarray, u: np.ndarray) -> float:
    return math.sqrt(max(fisher_inner(p, u, u), 0.0))


def ch_cubic(p: np.ndarray, h: np.ndarray, u: np.ndarray, v: np.ndarray) -> float:
    """Amari-Chentsov cubic T_p(h, u, v) in moment coordinates."""

    return float(np.sum(h * u * v / (p * p)))


def k_ch_raise(p: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    guv = fisher_inner(p, u, v)
    return project_tangent((u * v / p) - guv * p)


def fisher_density(p: np.ndarray) -> float:
    return float(np.prod(p) ** -0.5)


def conductor_packets(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {}
    for k in range(1, n):
        conductor = n // math.gcd(n, k)
        packets.setdefault(conductor, []).append(k)
    return {d: packets[d] for d in sorted(packets)}


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    m = n
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def radical(n: int) -> int:
    out = 1
    for p in prime_factors(n):
        out *= p
    return out


def squarefree_two_prime_support(n: int) -> list[int]:
    rad = radical(n)
    return [d for d in sorted(conductor_packets(n)) if d > 1 and rad % d == 0]


def project_to_conductors(vector: np.ndarray, conductors: list[int]) -> np.ndarray:
    n = int(vector.size)
    packets = conductor_packets(n)
    keep = np.zeros(n, dtype=bool)
    for conductor in conductors:
        for k in packets.get(conductor, []):
            keep[k] = True
    keep[0] = False
    coeff = np.fft.fft(project_tangent(vector))
    return project_tangent(np.fft.ifft(np.where(keep, coeff, 0.0)).real)


def leakage_fraction(p: np.ndarray, vector: np.ndarray, support: list[int]) -> float:
    total = fisher_norm(p, vector)
    if total <= EPS:
        return 0.0
    inside = project_to_conductors(vector, support)
    outside = project_tangent(vector - inside)
    leak = fisher_norm(p, outside)
    return float((leak * leak) / (total * total))


def random_unit_in_support(
    rng: np.random.Generator,
    n: int,
    support: list[int],
) -> np.ndarray:
    p_star = np.ones(n) / n
    for _ in range(200):
        raw = rng.standard_normal(n)
        projected = project_to_conductors(raw, support)
        norm = fisher_norm(p_star, projected)
        if norm > 1e-10:
            return projected / norm
    raise RuntimeError(f"could not sample a nonzero vector in support {support}")


def make_nambu_field(
    direction: np.ndarray,
    p0: np.ndarray,
    speed: float,
):
    """Return a volume-dual Nambu field on the linear leaf normal to direction.

    If the macro-Hamiltonians are any constant-gradient basis of the Fisher
    local chart orthogonal to `direction`, their volume-dual vector is
    proportional to direction / rho_F(p).  The constant below sets the initial
    Fisher speed.  This preserves the selected linear macro leaf and the
    Fisher volume form up to the usual Nambu scale choice.
    """

    rho0 = fisher_density(p0)
    initial_norm = fisher_norm(p0, direction)
    if initial_norm <= EPS:
        raise ValueError("Nambu direction has zero Fisher norm at p0")
    scale = speed * rho0 / initial_norm

    def field(p: np.ndarray) -> np.ndarray:
        return (scale / fisher_density(p)) * direction

    return field


def rk4_step(p: np.ndarray, dt: float, field) -> np.ndarray:
    k1 = field(p)
    k2 = field(p + 0.5 * dt * k1)
    k3 = field(p + 0.5 * dt * k2)
    k4 = field(p + dt * k3)
    out = p + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return out / float(np.sum(out))


def audit_seed(
    row: int,
    seed: int,
    *,
    support: list[int],
    amplitude: float,
    speed: float,
    horizon: float,
    steps: int,
) -> SeedAudit:
    rng = np.random.default_rng(seed)
    p_star = np.ones(row) / row
    direction = random_unit_in_support(rng, row, support)
    p = p_star + amplitude * direction
    if float(np.min(p)) <= 0.0:
        raise ValueError(
            f"amplitude {amplitude} leaves simplex for row {row}, seed {seed}"
        )

    field = make_nambu_field(direction, p, speed)
    dt = horizon / steps

    normalized_charges: list[float] = []
    force_leakages: list[float] = []
    energy_densities: list[float] = []
    min_probability = float(np.min(p))
    max_sum_error = abs(float(np.sum(p)) - 1.0)

    for _ in range(steps + 1):
        x = field(p)
        h = p - p_star
        h_norm = fisher_norm(p, h)
        x_norm = fisher_norm(p, x)
        cubic = ch_cubic(p, h, x, x)
        if h_norm > EPS and x_norm > EPS:
            normalized_charges.append(cubic / (h_norm * x_norm * x_norm))
        force = k_ch_raise(p, x, x)
        force_leakages.append(leakage_fraction(p, force, support))
        energy_densities.append(0.5 * x_norm * x_norm + cubic / 3.0)

        p = rk4_step(p, dt, field)
        min_probability = min(min_probability, float(np.min(p)))
        max_sum_error = max(max_sum_error, abs(float(np.sum(p)) - 1.0))
        if min_probability <= 0.0:
            raise RuntimeError(f"trajectory left simplex for row {row}, seed {seed}")

    packets = conductor_packets(row)
    outside = [d for d in packets if d not in support]
    charges = np.asarray(normalized_charges, dtype=float)
    leak = np.asarray(force_leakages, dtype=float)
    energy = np.asarray(energy_densities, dtype=float)
    return SeedAudit(
        row=row,
        seed=seed,
        support=support,
        outside=outside,
        min_probability=min_probability,
        max_sum_error=max_sum_error,
        mean_abs_normalized_charge=float(np.mean(np.abs(charges))),
        mean_signed_normalized_charge=float(np.mean(charges)),
        mean_force_leakage=float(np.mean(leak)),
        max_force_leakage=float(np.max(leak)),
        mean_energy_density=float(np.mean(energy)),
        energy_density_span=float(np.max(energy) - np.min(energy)),
    )


def summarize_row(
    row: int,
    audits: list[SeedAudit],
    *,
    z6_floor: float | None,
    tolerance: float,
) -> RowSummary:
    charges = np.asarray([a.mean_abs_normalized_charge for a in audits], dtype=float)
    leak = np.asarray([a.mean_force_leakage for a in audits], dtype=float)
    max_leak = np.asarray([a.max_force_leakage for a in audits], dtype=float)
    floor = None if z6_floor is None else max(z6_floor, tolerance)
    snr = None if floor is None else float(np.mean(leak) / floor)
    support = audits[0].support
    outside = audits[0].outside
    mean_leak = float(np.mean(leak))
    if row == 6 and mean_leak <= tolerance:
        assessment = "known-closed baseline at numerical floor"
    elif mean_leak <= 10.0 * (floor or tolerance):
        assessment = "no cubic-force leakage above baseline"
    else:
        assessment = "cubic-force leakage above Z/6 baseline"
    return RowSummary(
        row=row,
        support=support,
        outside=outside,
        seeds=len(audits),
        mean_abs_normalized_charge=float(np.mean(charges)),
        std_abs_normalized_charge=float(np.std(charges)),
        mean_force_leakage=mean_leak,
        median_force_leakage=float(np.median(leak)),
        max_force_leakage=float(np.max(max_leak)),
        leakage_snr_vs_z6_floor=snr,
        max_sum_error=float(max(a.max_sum_error for a in audits)),
        min_probability=float(min(a.min_probability for a in audits)),
        assessment=assessment,
    )


def json_ready(obj: Any) -> Any:
    if isinstance(obj, float):
        if math.isnan(obj):
            return "nan"
        if math.isinf(obj):
            return "inf"
        return obj
    if isinstance(obj, list):
        return [json_ready(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): json_ready(v) for k, v in obj.items()}
    return obj


def fmt(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value == 0.0:
        return "0"
    if abs(value) < 1e-3 or abs(value) >= 1e4:
        return f"{value:.3e}"
    return f"{value:.6f}"


def make_report(
    summaries: list[RowSummary],
    audits: dict[int, list[SeedAudit]],
    *,
    report_json: Path,
    seeds: int,
    amplitude: float,
    speed: float,
    horizon: float,
    steps: int,
    tolerance: float,
) -> str:
    lines = [
        "# Constraint 3 Cubic Noether Verification",
        "",
        "## Status",
        "",
        f"- JSON artifact: `{report_json}`",
        "- theorem source: Paper 17, Definition 2.1 and Theorems 2.2-2.3",
        "- retired FFT proxy: not used",
        "- vector field: volume-dual Nambu-Fisher field on a linear regular leaf",
        "- charge density: scale-normalized `T_p(h, X_C, X_C)` along the trajectory",
        "- closure residual: Fisher fraction of `K^CH_p(X_C, X_C)` outside the squarefree two-prime support",
        f"- seeds per row: `{seeds}`",
        f"- amplitude / initial Fisher speed: `{amplitude}` / `{speed}`",
        f"- horizon / RK4 steps: `{horizon}` / `{steps}`",
        f"- numerical floor used for SNR: `{tolerance:.1e}`",
        "",
        "This is the first trajectory-level audit for Constraint 3.  It does not",
        "use `sum(IFFT(FFT(J)^3))`; it follows an actual Nambu-Fisher trajectory",
        "and contracts the Amari-Chentsov cubic with the trajectory vector field.",
        "",
        "## Row Summary",
        "",
        "| row | support | outside | mean abs normalized charge | mean leakage | median leakage | max leakage | SNR vs Z/6 floor | assessment |",
        "|---:|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for summary in summaries:
        lines.append(
            f"| {summary.row} | `{summary.support}` | `{summary.outside}` | "
            f"{fmt(summary.mean_abs_normalized_charge)} | "
            f"{fmt(summary.mean_force_leakage)} | "
            f"{fmt(summary.median_force_leakage)} | "
            f"{fmt(summary.max_force_leakage)} | "
            f"{fmt(summary.leakage_snr_vs_z6_floor)} | "
            f"{summary.assessment} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The `Z/6Z` row is the known-closed Paper 17 baseline.  Its outside",
        "support is empty because the squarefree two-prime support is the full",
        "nontrivial conductor support.  Its leakage therefore measures numerical",
        "floor only.",
        "",
        "For `Z/12Z` and `Z/18Z`, the same squarefree support `{2, 3, 6}` is",
        "embedded in a row with prime-power depth.  Leakage measures whether the",
        "genuine cubic force exits that squarefree support into the depth packets.",
        "This is a real cubic response diagnostic; it is not a random-phase mean.",
        "",
        "## Per-Row Seed Ranges",
        "",
        "| row | min leakage | median leakage | max leakage | min probability | max sum error |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row, row_audits in audits.items():
        leak = np.asarray([a.mean_force_leakage for a in row_audits], dtype=float)
        min_probability = min(a.min_probability for a in row_audits)
        max_sum_error = max(a.max_sum_error for a in row_audits)
        lines.append(
            f"| {row} | {fmt(float(np.min(leak)))} | {fmt(float(np.median(leak)))} | "
            f"{fmt(float(np.max(leak)))} | {fmt(min_probability)} | {fmt(max_sum_error)} |"
        )

    lines += [
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/constraint3_cubic_noether_verification.py",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, nargs="+", default=[6, 12, 18])
    parser.add_argument("--seeds", type=int, default=50)
    parser.add_argument("--seed-offset", type=int, default=20260515)
    parser.add_argument("--amplitude", type=float, default=0.04)
    parser.add_argument("--speed", type=float, default=0.02)
    parser.add_argument("--horizon", type=float, default=1.0)
    parser.add_argument("--steps", type=int, default=240)
    parser.add_argument("--tolerance", type=float, default=1e-14)
    parser.add_argument("--report", type=Path, default=REPORTS / "constraint3_cubic_noether_verification.md")
    parser.add_argument("--json", type=Path, default=REPORTS / "constraint3_cubic_noether_verification.json")
    args = parser.parse_args()

    audits_by_row: dict[int, list[SeedAudit]] = {}
    for row in args.rows:
        support = squarefree_two_prime_support(row)
        if support != [2, 3, 6]:
            raise ValueError(
                f"row {row} does not contain the expected two-prime support [2, 3, 6]"
            )
        audits_by_row[row] = [
            audit_seed(
                row,
                args.seed_offset + 1000 * row + seed,
                support=support,
                amplitude=args.amplitude,
                speed=args.speed,
                horizon=args.horizon,
                steps=args.steps,
            )
            for seed in range(args.seeds)
        ]

    z6_audits = audits_by_row.get(6)
    if not z6_audits:
        raise ValueError("R=6 must be included to establish the known-closed floor")
    z6_floor = max(a.mean_force_leakage for a in z6_audits)

    summaries = [
        summarize_row(
            row,
            audits,
            z6_floor=None if row == 6 else z6_floor,
            tolerance=args.tolerance,
        )
        for row, audits in audits_by_row.items()
    ]

    payload = {
        "config": {
            "rows": args.rows,
            "seeds": args.seeds,
            "seed_offset": args.seed_offset,
            "amplitude": args.amplitude,
            "speed": args.speed,
            "horizon": args.horizon,
            "steps": args.steps,
            "tolerance": args.tolerance,
        },
        "summaries": [asdict(s) for s in summaries],
        "audits": {
            row: [asdict(audit) for audit in audits]
            for row, audits in audits_by_row.items()
        },
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(json_ready(payload), indent=2), encoding="utf-8")
    args.report.write_text(
        make_report(
            summaries,
            audits_by_row,
            report_json=args.json,
            seeds=args.seeds,
            amplitude=args.amplitude,
            speed=args.speed,
            horizon=args.horizon,
            steps=args.steps,
            tolerance=args.tolerance,
        ),
        encoding="utf-8",
    )

    print(f"Wrote {args.report}")
    print(f"Wrote {args.json}")
    print(
        json.dumps(
            json_ready({"summaries": [asdict(summary) for summary in summaries]}),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
