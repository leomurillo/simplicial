"""Height-pressure audit for the Collatz carry cocycle.

This is the escape-side companion to the primitive cycle sieve.  It studies
the height cocycle

    H(w) = S(w) - |w| log_2(3)

over the full carry shift, where each carry depth s >= 1 has 2-adic cylinder
mass 2^-s.  Positive height means that the affine slope 3^m / 2^S is
contracting.  Nonpositive height prefixes are the coarse expansion windows
that an escaping trajectory would have to exploit repeatedly.

The pressure calculation is exact for the one-state carry shift:

    rho(theta) = sum_{s>=1} 2^-s 2^{-theta(s-log_2 3)}
               = 3^theta / (2^(1+theta) - 1).

The report also computes exact lower-tail masses by total carry depth and a
prefix-survival dynamic program for barriers H(prefix) <= B.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)
MEAN_CARRY = 2.0
MEAN_HEIGHT = MEAN_CARRY - LOG2_3


@dataclass(frozen=True)
class PressureSummary:
    theta_min: float
    pressure_min_log2: float
    chernoff_rate_bits: float
    spectral_radius_min: float
    nonzero_root: float
    mean_height: float


def pressure_log2(theta: float) -> float:
    return theta * LOG2_3 - math.log2((2.0 ** (1.0 + theta)) - 1.0)


def pressure_summary() -> PressureSummary:
    alpha = LOG2_3
    q = alpha / (alpha - 1.0)
    theta_min = math.log2(q) - 1.0
    p_min = pressure_log2(theta_min)
    return PressureSummary(
        theta_min=theta_min,
        pressure_min_log2=p_min,
        chernoff_rate_bits=-p_min,
        spectral_radius_min=2.0**p_min,
        nonzero_root=1.0,
        mean_height=MEAN_HEIGHT,
    )


def log2_comb(n: int, k: int) -> float:
    if k < 0 or k > n:
        return float("-inf")
    return (
        math.lgamma(n + 1)
        - math.lgamma(k + 1)
        - math.lgamma(n - k + 1)
    ) / math.log(2.0)


def log2sumexp(values: list[float]) -> float:
    if not values:
        return float("-inf")
    top = max(values)
    if top == float("-inf"):
        return top
    return top + math.log2(sum(2.0 ** (value - top) for value in values))


def bad_prefix_log_mass(length: int) -> tuple[int, float]:
    """Mass of words of length m with H(w) <= 0."""

    threshold = math.floor(length * LOG2_3)
    if threshold < length:
        return threshold, float("-inf")
    terms = [
        log2_comb(total_depth - 1, length - 1) - total_depth
        for total_depth in range(length, threshold + 1)
    ]
    return threshold, log2sumexp(terms)


def bad_prefix_rows(max_length: int) -> list[dict[str, float | int]]:
    summary = pressure_summary()
    rows = []
    for length in range(1, max_length + 1):
        threshold, log_mass = bad_prefix_log_mass(length)
        chernoff_log_bound = length * summary.pressure_min_log2
        rows.append(
            {
                "length": length,
                "threshold_total_depth": threshold,
                "bad_mass": 0.0 if log_mass == float("-inf") else 2.0**log_mass,
                "bad_log2_mass": log_mass,
                "chernoff_log2_bound": chernoff_log_bound,
                "bound_slack_bits": chernoff_log_bound - log_mass
                if log_mass != float("-inf")
                else float("inf"),
            }
        )
    return rows


def prefix_survival_masses(max_length: int, barrier: float) -> list[dict[str, float | int]]:
    """Mass of paths whose every prefix has H <= barrier."""

    state: dict[int, float] = {0: 1.0}
    rows = []
    for length in range(1, max_length + 1):
        bound = math.floor(length * LOG2_3 + barrier)
        next_state: dict[int, float] = {}
        for total_depth, mass in state.items():
            max_carry = bound - total_depth
            for carry in range(1, max_carry + 1):
                new_depth = total_depth + carry
                next_state[new_depth] = next_state.get(new_depth, 0.0) + mass * (2.0 ** -carry)
        state = next_state
        survival_mass = sum(state.values())
        rows.append(
            {
                "length": length,
                "barrier": barrier,
                "states": len(state),
                "max_allowed_total_depth": bound,
                "survival_mass": survival_mass,
                "survival_log2_mass": math.log2(survival_mass)
                if survival_mass > 0.0
                else float("-inf"),
            }
        )
    return rows


def selected_lengths(max_length: int) -> list[int]:
    candidates = [1, 2, 3, 4, 5, 8, 10, 12, 16, 20, 30, 40, 60, 80, 100, 120, 160, 200]
    out = [length for length in candidates if length <= max_length]
    if max_length not in out:
        out.append(max_length)
    return sorted(set(out))


def parse_barriers(text: str) -> list[float]:
    barriers = []
    for part in text.split(","):
        stripped = part.strip()
        if stripped:
            barriers.append(float(stripped))
    if not barriers:
        raise ValueError("--barriers must contain at least one value")
    return barriers


def rounded(value: object) -> object:
    if isinstance(value, float):
        if math.isinf(value):
            return "inf" if value > 0 else "-inf"
        return round(value, 10)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    return value


def summarize_survival(rows: list[dict[str, float | int]]) -> dict[str, float | int]:
    final = rows[-1]
    half = max(1, len(rows) // 2)
    tail = rows[half - 1 :]
    finite_tail = [
        float(row["survival_log2_mass"]) / int(row["length"])
        for row in tail
        if row["survival_log2_mass"] != float("-inf")
    ]
    return {
        "barrier": final["barrier"],
        "final_length": final["length"],
        "final_survival_mass": final["survival_mass"],
        "final_survival_log2_mass": final["survival_log2_mass"],
        "tail_mean_log2_mass_per_step": (
            sum(finite_tail) / len(finite_tail) if finite_tail else float("-inf")
        ),
        "final_states": final["states"],
    }


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    pressure = payload["pressure"]
    chosen = selected_lengths(settings["max_length"])
    bad_rows = {
        int(row["length"]): row
        for row in payload["bad_prefix_rows"]
    }

    lines = [
        "# Collatz Height Pressure",
        "",
        "## Status",
        "",
        "This report studies the escape-side height cocycle on carry cylinders.  It does not test cycles; it estimates how large the low-height part of the infinite carry tree is.",
        "",
        f"- max prefix length: `{settings['max_length']}`",
        f"- barriers: `{settings['barriers']}`",
        f"- log2(3): `{LOG2_3:.12f}`",
        f"- mean carry depth under Haar: `{MEAN_CARRY:.6f}`",
        f"- mean height per step: `{MEAN_HEIGHT:.12f}`",
        "",
        "## Pressure Operator",
        "",
        "For the one-state carry shift with branch mass `2^-s`,",
        "",
        "```text",
        "rho(theta) = sum_s 2^-s 2^{-theta(s-log2(3))}",
        "           = 3^theta / (2^(1+theta)-1)",
        "P(theta)   = log2 rho(theta)",
        "```",
        "",
        f"- minimizing theta: `{pressure['theta_min']:.12f}`",
        f"- minimum pressure P(theta): `{pressure['pressure_min_log2']:.12f}` bits/step",
        f"- Chernoff lower-tail rate: `{pressure['chernoff_rate_bits']:.12f}` bits/step",
        f"- minimum spectral radius: `{pressure['spectral_radius_min']:.12f}`",
        f"- nonzero pressure root: `{pressure['nonzero_root']:.6f}`",
        "",
        "The negative pressure minimum means nonpositive-height prefixes are exponentially suppressed in 2-adic cylinder mass, even though they occur at every finite depth.",
        "",
        "## Nonpositive-Height Prefix Mass",
        "",
        "This is the exact mass of length-`m` carry words with `S <= floor(m log2(3))`.",
        "",
        "| m | max S | bad mass | log2 bad mass | Chernoff log2 bound | slack bits |",
        "|---:|---:|---:|---:|---:|---:|",
    ]

    for length in chosen:
        row = bad_rows[length]
        lines.append(
            f"| {length} | {row['threshold_total_depth']} | "
            f"{row['bad_mass']:.12g} | {row['bad_log2_mass']:.6f} | "
            f"{row['chernoff_log2_bound']:.6f} | {row['bound_slack_bits']:.6f} |"
        )

    lines += [
        "",
        "## Prefix-Barrier Survival",
        "",
        "For a barrier `B`, this is the mass of carry sequences whose every prefix satisfies `H(prefix) <= B`.  This is stricter than merely having low height at the final prefix.",
        "",
        "| barrier | m | survival mass | log2 survival mass | tail log2 mass/step | final states |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for summary in payload["survival_summaries"]:
        lines.append(
            f"| {summary['barrier']} | {summary['final_length']} | "
            f"{summary['final_survival_mass']:.12g} | "
            f"{summary['final_survival_log2_mass']:.6f} | "
            f"{summary['tail_mean_log2_mass_per_step']:.6f} | "
            f"{summary['final_states']} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The pressure calculation gives the escape-side algebraic shape.  The typical carry word has positive height because `E[s]=2 > log2(3)`, so typical affine slopes contract.  The low-height tree still exists at every finite depth, but its cylinder mass decays exponentially at the pressure rate.",
        "",
        "This is not a proof against escape.  A proof would have to couple this height pressure to the affine cocycle `C_w` and to the Archimedean size of actual positive integers, not only to 2-adic cylinder mass.  The next algebraic object is therefore a two-cocycle pressure system tracking `(H(w), log2 C_w)` or a normalized intercept cocycle alongside height.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_height_pressure.py --max-length {settings['max_length']} --barriers \"{','.join(str(x) for x in settings['barriers'])}\"",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_height_pressure_L{max_length}.md"


def default_json_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_height_pressure_L{max_length}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=120)
    parser.add_argument("--barriers", type=str, default="0,2,4,8")
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    barriers = parse_barriers(args.barriers)

    p_summary = pressure_summary()
    bad_rows = bad_prefix_rows(args.max_length)
    survival_by_barrier = {
        barrier: prefix_survival_masses(args.max_length, barrier)
        for barrier in barriers
    }
    payload = {
        "settings": {
            "max_length": args.max_length,
            "barriers": barriers,
        },
        "pressure": p_summary.__dict__,
        "bad_prefix_rows": bad_rows,
        "survival_by_barrier": survival_by_barrier,
        "survival_summaries": [
            summarize_survival(rows)
            for _barrier, rows in sorted(survival_by_barrier.items())
        ],
    }

    report_path = args.report or default_report_path(args.max_length)
    json_path = args.json or default_json_path(args.max_length)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(p_summary.__dict__), indent=2))


if __name__ == "__main__":
    main()
