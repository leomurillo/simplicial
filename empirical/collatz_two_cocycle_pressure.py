"""Two-cocycle pressure audit for the accelerated odd Collatz map.

The carry-word algebra writes every accelerated odd branch as

    U_w(n) = (3^m n + C_w) / 2^S
           = 2^{-H(w)} n + B_w,

where

    H(w) = S - m log_2(3),
    B_w = C_w / 2^S.

The height cocycle alone says typical branches contract.  This script adds
the normalized intercept cocycle

    B_{w,s} = (3 B_w + 1) / 2^s

and measures the paired pressure.  The point is to expose which algebra is
needed for escape: not just quotient labels, not just carry heights, but a
triangular affine cocycle over the carry shift.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any


LOG2_3 = math.log2(3.0)


@dataclass
class MomentState:
    mass: float = 0.0
    b1: float = 0.0
    b2: float = 0.0
    min_b: float = math.inf
    max_b: float = -math.inf
    min_word: tuple[int, ...] = ()
    max_word: tuple[int, ...] = ()


def pressure_log2(theta: float) -> float:
    return theta * LOG2_3 - math.log2((2.0 ** (1.0 + theta)) - 1.0)


def pressure_theta_min() -> float:
    q = LOG2_3 / (LOG2_3 - 1.0)
    return math.log2(q) - 1.0


def degree_pressure_log2(degree: int, theta: float) -> float:
    """Leading spectral pressure on the degree-r polynomial intercept mode."""

    shifted = 1.0 + theta + degree
    return (theta + degree) * LOG2_3 - math.log2((2.0**shifted) - 1.0)


def word_runs(word: tuple[int, ...]) -> list[tuple[int, int]]:
    if not word:
        return []
    runs: list[tuple[int, int]] = []
    current = word[0]
    count = 1
    for carry in word[1:]:
        if carry == current:
            count += 1
            continue
        runs.append((current, count))
        current = carry
        count = 1
    runs.append((current, count))
    return runs


def word_signature(word: tuple[int, ...], limit: int = 12) -> str:
    runs = word_runs(word)
    parts = [
        str(carry) if count == 1 else f"{carry}^{count}"
        for carry, count in runs
    ]
    if len(parts) <= limit:
        return "(" + " ".join(parts) + ")"
    head = " ".join(parts[: limit // 2])
    tail = " ".join(parts[-(limit // 2) :])
    return f"({head} ... {tail})"


def update_state(target: MomentState, source: MomentState, carry: int) -> None:
    scale = math.ldexp(1.0, -carry)
    scale2 = scale * scale
    scale3 = scale2 * scale

    target.mass += scale * source.mass
    target.b1 += scale2 * (3.0 * source.b1 + source.mass)
    target.b2 += scale3 * (
        9.0 * source.b2 + 6.0 * source.b1 + source.mass
    )

    if source.min_b < math.inf:
        candidate = (3.0 * source.min_b + 1.0) * scale
        if candidate < target.min_b:
            target.min_b = candidate
            target.min_word = source.min_word + (carry,)

    if source.max_b > -math.inf:
        candidate = (3.0 * source.max_b + 1.0) * scale
        if candidate > target.max_b:
            target.max_b = candidate
            target.max_word = source.max_word + (carry,)


def step_states(
    states: dict[int, MomentState],
    max_depth: int,
    allowed_depth: int | None = None,
) -> dict[int, MomentState]:
    next_states: dict[int, MomentState] = {}
    depth_bound = max_depth if allowed_depth is None else min(max_depth, allowed_depth)
    for total_depth, state in states.items():
        max_carry = depth_bound - total_depth
        for carry in range(1, max_carry + 1):
            new_depth = total_depth + carry
            target = next_states.setdefault(new_depth, MomentState())
            update_state(target, state, carry)
    return next_states


def initial_states() -> dict[int, MomentState]:
    return {
        0: MomentState(
            mass=1.0,
            b1=0.0,
            b2=0.0,
            min_b=0.0,
            max_b=0.0,
            min_word=(),
            max_word=(),
        )
    }


def finite_or_none(value: float) -> float | None:
    if math.isfinite(value):
        return value
    return None


def summarize_depth_states(
    states: dict[int, MomentState],
    length: int,
    barrier: float,
    label: str,
) -> dict[str, Any]:
    allowed_depth = math.floor(length * LOG2_3 + barrier)
    selected = {
        depth: state
        for depth, state in states.items()
        if depth <= allowed_depth and state.mass > 0.0
    }
    total_mass = sum(state.mass for state in selected.values())
    b1 = sum(state.b1 for state in selected.values())
    b2 = sum(state.b2 for state in selected.values())

    if total_mass <= 0.0:
        return {
            "label": label,
            "length": length,
            "barrier": barrier,
            "allowed_depth": allowed_depth,
            "states": 0,
            "mass": 0.0,
            "log2_mass": float("-inf"),
        }

    weighted_height = sum(
        state.mass * (depth - length * LOG2_3)
        for depth, state in selected.items()
    )
    mean_b = b1 / total_mass
    rms_b = math.sqrt(max(0.0, b2 / total_mass))

    max_depth, max_state = max(
        selected.items(),
        key=lambda item: item[1].max_b,
    )
    min_depth, min_state = min(
        selected.items(),
        key=lambda item: item[1].min_b,
    )

    max_affine_value = -math.inf
    max_affine_depth = 0
    max_affine_word: tuple[int, ...] = ()
    for depth, state in selected.items():
        height = depth - length * LOG2_3
        slope = 2.0 ** (-height)
        affine_value = slope + state.max_b
        if affine_value > max_affine_value:
            max_affine_value = affine_value
            max_affine_depth = depth
            max_affine_word = state.max_word

    contraction_mass = 0.0
    contraction_b1 = 0.0
    contraction_cap_sum = 0.0
    max_cap = -math.inf
    max_cap_depth = 0
    max_cap_word: tuple[int, ...] = ()
    expansion_mass = 0.0
    min_height = math.inf
    max_height = -math.inf

    for depth, state in selected.items():
        height = depth - length * LOG2_3
        min_height = min(min_height, height)
        max_height = max(max_height, height)
        if height > 0.0:
            denom = 1.0 - (2.0 ** (-height))
            cap_scale = 1.0 / denom
            contraction_mass += state.mass
            contraction_b1 += state.b1
            contraction_cap_sum += state.b1 * cap_scale
            candidate_cap = state.max_b * cap_scale
            if candidate_cap > max_cap:
                max_cap = candidate_cap
                max_cap_depth = depth
                max_cap_word = state.max_word
        else:
            expansion_mass += state.mass

    return {
        "label": label,
        "length": length,
        "barrier": barrier,
        "allowed_depth": allowed_depth,
        "states": len(selected),
        "mass": total_mass,
        "log2_mass": math.log2(total_mass),
        "mean_height": weighted_height / total_mass,
        "min_height": min_height,
        "max_height": max_height,
        "mean_intercept": mean_b,
        "rms_intercept": rms_b,
        "intercept_rms_over_mean": rms_b / mean_b if mean_b > 0.0 else math.inf,
        "min_intercept": min_state.min_b,
        "min_intercept_depth": min_depth,
        "min_intercept_word": list(min_state.min_word),
        "min_intercept_signature": word_signature(min_state.min_word),
        "max_intercept": max_state.max_b,
        "max_intercept_log2": math.log2(max_state.max_b)
        if max_state.max_b > 0.0
        else float("-inf"),
        "max_intercept_depth": max_depth,
        "max_intercept_word": list(max_state.max_word),
        "max_intercept_signature": word_signature(max_state.max_word),
        "max_affine_at_one": max_affine_value,
        "max_affine_at_one_log2": math.log2(max_affine_value),
        "max_affine_at_one_depth": max_affine_depth,
        "max_affine_at_one_word": list(max_affine_word),
        "max_affine_at_one_signature": word_signature(max_affine_word),
        "contraction_mass": contraction_mass,
        "contraction_log2_mass": math.log2(contraction_mass)
        if contraction_mass > 0.0
        else float("-inf"),
        "contraction_mass_fraction": contraction_mass / total_mass,
        "expansion_mass": expansion_mass,
        "expansion_log2_mass": math.log2(expansion_mass)
        if expansion_mass > 0.0
        else float("-inf"),
        "expansion_mass_fraction": expansion_mass / total_mass,
        "mean_contracting_intercept": contraction_b1 / contraction_mass
        if contraction_mass > 0.0
        else None,
        "mean_contracting_cap": contraction_cap_sum / contraction_mass
        if contraction_mass > 0.0
        else None,
        "max_contracting_cap": finite_or_none(max_cap),
        "max_contracting_cap_log2": math.log2(max_cap)
        if max_cap > 0.0 and math.isfinite(max_cap)
        else None,
        "max_contracting_cap_depth": max_cap_depth if max_cap > -math.inf else None,
        "max_contracting_cap_word": list(max_cap_word) if max_cap > -math.inf else None,
        "max_contracting_cap_signature": word_signature(max_cap_word)
        if max_cap > -math.inf
        else None,
    }


def unrestricted_intercept_moments(max_length: int) -> list[dict[str, float | int]]:
    mean = 0.0
    second = 0.0
    rows = []
    for length in range(1, max_length + 1):
        old_mean = mean
        old_second = second
        mean = old_mean + (1.0 / 3.0)
        second = (9.0 * old_second + 6.0 * old_mean + 1.0) / 7.0
        rows.append(
            {
                "length": length,
                "mean_intercept": mean,
                "second_intercept_moment": second,
                "rms_intercept": math.sqrt(second),
                "rms_over_mean": math.sqrt(second) / mean,
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


def compute_final_window_summaries(
    max_length: int,
    barriers: list[float],
) -> list[dict[str, Any]]:
    max_depth = math.floor(max_length * LOG2_3 + max(barriers))
    states = initial_states()
    summaries = []
    for length in range(1, max_length + 1):
        states = step_states(states, max_depth=max_depth)
        if length == max_length:
            for barrier in barriers:
                summaries.append(
                    summarize_depth_states(
                        states,
                        length=length,
                        barrier=barrier,
                        label="final-window",
                    )
                )
    return summaries


def compute_prefix_barrier_summaries(
    max_length: int,
    barriers: list[float],
) -> list[dict[str, Any]]:
    summaries = []
    for barrier in barriers:
        states = initial_states()
        max_depth = math.floor(max_length * LOG2_3 + barrier)
        for length in range(1, max_length + 1):
            allowed_depth = math.floor(length * LOG2_3 + barrier)
            states = step_states(
                states,
                max_depth=max_depth,
                allowed_depth=allowed_depth,
            )
        summaries.append(
            summarize_depth_states(
                states,
                length=max_length,
                barrier=barrier,
                label="prefix-barrier",
            )
        )
    return summaries


def degree_pressure_rows(theta_min: float, max_degree: int) -> list[dict[str, float | int]]:
    rows = []
    for degree in range(max_degree + 1):
        p0 = degree_pressure_log2(degree, 0.0)
        pmin = degree_pressure_log2(degree, theta_min)
        rows.append(
            {
                "degree": degree,
                "pressure_log2_at_theta_0": p0,
                "spectral_radius_at_theta_0": 2.0**p0,
                "pressure_log2_at_height_theta_min": pmin,
                "spectral_radius_at_height_theta_min": 2.0**pmin,
            }
        )
    return rows


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


def format_optional_float(value: object, digits: int = 6) -> str:
    if value is None:
        return "-"
    return f"{float(value):.{digits}f}"


def make_summary_table(summaries: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| barrier | mass | log2 mass | mean H | mean B | rms B | max log2 B | expansion % | max cap log2 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            f"| {row['barrier']} | {row['mass']:.12g} | {row['log2_mass']:.6f} | "
            f"{row['mean_height']:.6f} | {row['mean_intercept']:.6f} | "
            f"{row['rms_intercept']:.6f} | {row['max_intercept_log2']:.6f} | "
            f"{100.0 * row['expansion_mass_fraction']:.4f} | "
            f"{format_optional_float(row['max_contracting_cap_log2'])} |"
        )
    return lines


def make_witness_table(summaries: list[dict[str, Any]], key_prefix: str) -> list[str]:
    lines = [
        "| barrier | depth | log2 value | witness carry signature |",
        "|---:|---:|---:|---|",
    ]
    for row in summaries:
        value_key = f"{key_prefix}_log2"
        depth_key = f"{key_prefix}_depth"
        signature_key = f"{key_prefix}_signature"
        value = row.get(value_key)
        if value is None:
            lines.append(f"| {row['barrier']} | - | - | - |")
            continue
        lines.append(
            f"| {row['barrier']} | {row.get(depth_key)} | "
            f"{float(value):.6f} | `{row.get(signature_key)}` |"
        )
    return lines


def make_report(payload: dict[str, Any]) -> str:
    settings = payload["settings"]
    theta_min = payload["height_pressure"]["theta_min"]
    unrestricted = payload["unrestricted_intercept_moments"][-1]

    lines = [
        "# Collatz Two-Cocycle Pressure",
        "",
        "## Status",
        "",
        "This report couples the escape-side height cocycle to the normalized affine intercept.  It asks how much additive lift remains inside the same low-height carry windows measured by the height-pressure audit.",
        "",
        f"- max prefix length: `{settings['max_length']}`",
        f"- barriers: `{settings['barriers']}`",
        f"- log2(3): `{LOG2_3:.12f}`",
        "",
        "## Affine Cocycle",
        "",
        "For a carry word `w=(s_1,...,s_m)`,",
        "",
        "```text",
        "U_w(n) = 2^{-H(w)} n + B_w",
        "H(w)   = S(w) - m log2(3)",
        "B_{w,s}= (3 B_w + 1) / 2^s",
        "```",
        "",
        "The polynomial moment algebra is triangular.  The leading degree-`r` pressure mode is",
        "",
        "```text",
        "lambda_r(theta) = sum_s 2^-s 2^{-theta(s-log2(3))} (3/2^s)^r",
        "                = 3^{theta+r} / (2^{1+theta+r}-1)",
        "```",
        "",
        f"The height pressure minimizer is `theta={theta_min:.12f}`.",
        "",
        "| degree r | log2 lambda_r(0) | lambda_r(0) | log2 lambda_r(theta*) | lambda_r(theta*) |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in payload["degree_pressure_rows"]:
        lines.append(
            f"| {row['degree']} | {row['pressure_log2_at_theta_0']:.6f} | "
            f"{row['spectral_radius_at_theta_0']:.9f} | "
            f"{row['pressure_log2_at_height_theta_min']:.6f} | "
            f"{row['spectral_radius_at_height_theta_min']:.9f} |"
        )

    lines += [
        "",
        "The degree-1 intercept mode is neutral at theta zero: `lambda_1(0)=1`.  The degree-2 mode is already expansive, so intercept variance grows even though typical height contracts.",
        "",
        "## Unrestricted Intercept Moments",
        "",
        f"At length `{settings['max_length']}`, the unrestricted carry shift has:",
        "",
        f"- mean `B_w`: `{unrestricted['mean_intercept']:.12g}`",
        f"- rms `B_w`: `{unrestricted['rms_intercept']:.12g}`",
        f"- rms/mean: `{unrestricted['rms_over_mean']:.12g}`",
        "",
        "This is the first concrete sign that the escape algebra is not scalar: average additive lift is mild, but higher moments are controlled by rare low-carry branches.",
        "",
        "## Final Low-Height Windows",
        "",
        "These rows select all words whose final height satisfies `H(w) <= barrier`, without requiring earlier prefixes to stay below the barrier.",
        "",
        *make_summary_table(payload["final_window_summaries"]),
        "",
        "### Max Final-Window Intercepts",
        "",
        *make_witness_table(payload["final_window_summaries"], "max_intercept"),
        "",
        "### Max Final-Window Contracting Caps",
        "",
        "For `H>0`, a branch has real cap `B_w / (1 - 2^{-H})`; above that cap the branch decreases after the whole word.",
        "",
        *make_witness_table(payload["final_window_summaries"], "max_contracting_cap"),
        "",
        "## Prefix-Barrier Windows",
        "",
        "These rows are stricter: every prefix must satisfy `H(prefix) <= barrier`.  They are the finite analogue of a persistently low-height escape corridor.",
        "",
        *make_summary_table(payload["prefix_barrier_summaries"]),
        "",
        "### Max Prefix-Barrier Intercepts",
        "",
        *make_witness_table(payload["prefix_barrier_summaries"], "max_intercept"),
        "",
        "### Max Prefix-Barrier Contracting Caps",
        "",
        *make_witness_table(payload["prefix_barrier_summaries"], "max_contracting_cap"),
        "",
        "## Interpretation",
        "",
        "The algebra needed for Collatz is a finite quotient carry algebra lifted to a triangular affine cocycle.  The quotient/carry layer supplies exact branch labels; the height layer supplies contraction pressure; the intercept layer supplies the additive carry memory that scalar pressure cannot see.",
        "",
        "The important obstruction is now sharper.  Low-height corridors are exponentially small in 2-adic mass, but inside them the intercept cocycle has neutral and expanding polynomial modes.  A proof-facing escape argument has to dominate this intercept growth against the height pressure and the exact domain cylinders.",
        "",
        "Next computational target: build the transfer operator on binned `(H, log2 B)` states and compare its leading spectral radius against the exact domain-cylinder constraints modulo `2^S`.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_two_cocycle_pressure.py --max-length {settings['max_length']} --barriers \"{','.join(str(x) for x in settings['barriers'])}\"",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_two_cocycle_pressure_L{max_length}.md"


def default_json_path(max_length: int) -> Path:
    return Path("empirical/reports") / f"collatz_two_cocycle_pressure_L{max_length}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-length", type=int, default=120)
    parser.add_argument("--barriers", type=str, default="0,2,4,8")
    parser.add_argument("--max-degree", type=int, default=4)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.max_length < 1:
        raise ValueError("--max-length must be at least 1")
    if args.max_degree < 0:
        raise ValueError("--max-degree must be nonnegative")

    barriers = parse_barriers(args.barriers)
    theta_min = pressure_theta_min()
    height_p_min = pressure_log2(theta_min)

    payload = {
        "settings": {
            "max_length": args.max_length,
            "barriers": barriers,
            "max_degree": args.max_degree,
        },
        "height_pressure": {
            "theta_min": theta_min,
            "pressure_min_log2": height_p_min,
            "chernoff_rate_bits": -height_p_min,
        },
        "degree_pressure_rows": degree_pressure_rows(theta_min, args.max_degree),
        "unrestricted_intercept_moments": unrestricted_intercept_moments(args.max_length),
        "final_window_summaries": compute_final_window_summaries(
            args.max_length,
            barriers,
        ),
        "prefix_barrier_summaries": compute_prefix_barrier_summaries(
            args.max_length,
            barriers,
        ),
    }

    report_path = args.report or default_report_path(args.max_length)
    json_path = args.json or default_json_path(args.max_length)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(make_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(payload["height_pressure"]), indent=2))


if __name__ == "__main__":
    main()
