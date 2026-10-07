"""Primorial/squarefree information-investment frame testbed.

This is the first Paper 25 testbed beyond local fields.  For squarefree
cyclic rows R = Z/nZ, additive characters are packeted by conductor d | n.
Unlike F_q[u]/(u^k), the conductor packets form a divisor lattice rather than
a single wild quotient chain.  The natural prefix for a target conductor d is
therefore the CRT/divisor subspace spanned by packets e | d.

The script builds the real Fourier tangent basis, evaluates the finite
information-investment ledger, and compares the conductor/CRT frame against
Haar-random mixed frames with the same conductor block sizes.  It reports:

* raw reusable ledger terms (Fisher block coupling, projection, reciprocal
  projection, closure, resource, depth);
* packet-commutator and first-order packet-respect costs;
* break-even packet prices needed when a mixed frame lowers the unpriced
  structural ledger; and
* the top mixed frames for inspection.

The purpose is diagnostic, not a theorem: identify what replaces packet-local
invariance in squarefree/primorial rows and quantify the budget needed to keep
CRT prime compatibility.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from math import gcd
from pathlib import Path
from typing import Any

import numpy as np


DEFAULT_JSON = Path("empirical/reports/helmert_primorial_squarefree_testbed.json")
DEFAULT_REPORT = Path("empirical/reports/helmert_primorial_squarefree_testbed.md")


@dataclass(frozen=True)
class Mode:
    kind: str
    label: int
    conductor: int


def parse_int_csv(text: str) -> list[int]:
    return [int(item.strip()) for item in text.split(",") if item.strip()]


def prime_factors(n: int) -> tuple[int, ...]:
    out: list[int] = []
    value = n
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            out.append(factor)
            while value % factor == 0:
                value //= factor
        factor += 1 if factor == 2 else 2
    if value > 1:
        out.append(value)
    return tuple(out)


def is_squarefree(n: int) -> bool:
    for prime in prime_factors(n):
        if n % (prime * prime) == 0:
            return False
    return True


def omega(n: int) -> int:
    return len(prime_factors(n))


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conductor(label: int, n: int) -> int:
    label %= n
    if label == 0:
        return 1
    return n // gcd(label, n)


def packet_labels(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {d: [] for d in divisors(n) if d > 1}
    for label in range(1, n):
        packets[conductor(label, n)].append(label)
    return {d: labels for d, labels in packets.items() if labels}


def conductor_order(n: int) -> list[int]:
    return sorted((d for d in divisors(n) if d > 1), key=lambda d: (omega(d), d))


def real_fourier_basis(n: int) -> tuple[np.ndarray, list[Mode], list[int], list[int]]:
    packets = packet_labels(n)
    order = conductor_order(n)
    x = np.arange(n, dtype=float)
    columns: list[np.ndarray] = []
    modes: list[Mode] = []
    sizes: list[int] = []
    seen: set[int] = set()
    for cond in order:
        before = len(modes)
        for label in sorted(packets[cond]):
            if label in seen:
                continue
            partner = (-label) % n
            if partner == label:
                seen.add(label)
                columns.append(((-1.0) ** x) / np.sqrt(n))
                modes.append(Mode("real", label, cond))
            else:
                chosen = min(label, partner)
                if label != chosen:
                    continue
                seen.add(label)
                seen.add(partner)
                theta = 2.0 * np.pi * chosen * x / n
                columns.append(np.sqrt(2.0 / n) * np.cos(theta))
                modes.append(Mode("cos", chosen, cond))
                columns.append(np.sqrt(2.0 / n) * np.sin(theta))
                modes.append(Mode("sin", chosen, cond))
        sizes.append(len(modes) - before)
    basis = np.column_stack(columns)
    return basis, modes, sizes, order


def block_slices(sizes: list[int]) -> list[slice]:
    out: list[slice] = []
    start = 0
    for size in sizes:
        out.append(slice(start, start + size))
        start += size
    return out


def active_indices(order: list[int], sizes: list[int], target: int) -> list[int]:
    spans = block_slices(sizes)
    active: list[int] = []
    for cond, span in zip(order, spans):
        if target % cond == 0:
            active.extend(range(span.start, span.stop))
    return active


def random_orthogonal(dim: int, rng: np.random.Generator) -> np.ndarray:
    sample = rng.normal(size=(dim, dim))
    q, r = np.linalg.qr(sample)
    signs = np.sign(np.diag(r))
    signs[signs == 0.0] = 1.0
    return q * signs


def safe_probability(h: np.ndarray, amplitude_fraction: float) -> tuple[np.ndarray, float]:
    n = h.shape[0]
    uniform = 1.0 / n
    max_abs = float(np.max(np.abs(h)))
    min_h = float(np.min(h))
    if max_abs == 0.0:
        return np.full(n, uniform), 0.0
    if min_h < 0.0:
        max_amplitude = 0.95 * uniform / (-min_h)
    else:
        max_amplitude = 1.0 / max_abs
    amplitude = amplitude_fraction * max_amplitude
    probability = np.full(n, uniform) + amplitude * h
    if float(probability.min()) <= 0.0:
        raise ValueError("amplitude produced a non-positive probability")
    return probability, amplitude


def fisher_gram(probability: np.ndarray, basis: np.ndarray) -> np.ndarray:
    n = probability.shape[0]
    gram = basis.T @ (basis / probability[:, None]) / n
    return 0.5 * (gram + gram.T)


def off_block_energy(matrix: np.ndarray, sizes: list[int]) -> float:
    total = 0.0
    for i, rows in enumerate(block_slices(sizes)):
        for j, cols in enumerate(block_slices(sizes)):
            if i == j:
                continue
            block = matrix[rows, cols]
            total += float(np.sum(block * block))
    return total


def packet_commutator_impurity(q: np.ndarray, sizes: list[int]) -> float:
    spans = block_slices(sizes)
    dim = q.shape[0]
    total = 0.0
    for candidate_span in spans:
        block = q[:, candidate_span]
        p_block = block @ block.T
        for packet_span in spans:
            p_packet = np.zeros((dim, dim), dtype=float)
            p_packet[packet_span, packet_span] = np.eye(packet_span.stop - packet_span.start)
            commutator = p_block @ p_packet - p_packet @ p_block
            total += float(np.sum(commutator * commutator))
    return total / dim


def first_order_packet_cost(q: np.ndarray, sizes: list[int]) -> float:
    spans = block_slices(sizes)
    total = 0.0
    for true_index, true_span in enumerate(spans):
        for candidate_index, candidate_span in enumerate(spans):
            if true_index == candidate_index:
                continue
            sub = q[true_span, candidate_span]
            total += float(np.linalg.norm(sub, ord="fro"))
    return total


def projection_error(vector: np.ndarray, active_basis: np.ndarray) -> float:
    total = float(vector @ vector)
    if total <= 1e-15:
        return 0.0
    inside = active_basis.T @ vector
    inside_energy = float(inside @ inside)
    return max(0.0, 1.0 - inside_energy / total)


def closure_leakage(
    *,
    basis: np.ndarray,
    q: np.ndarray,
    active: list[int],
) -> float:
    if len(active) == q.shape[0]:
        return 0.0
    q_active = q[:, active]
    point_basis = basis @ q_active
    products = (point_basis[:, :, None] * point_basis[:, None, :]).reshape(basis.shape[0], -1)
    nontrivial_coefficients = basis.T @ products
    denominator = float(np.sum(nontrivial_coefficients * nontrivial_coefficients))
    if denominator <= 1e-15:
        return 0.0
    inside_coefficients = q_active.T @ nontrivial_coefficients
    inside = float(np.sum(inside_coefficients * inside_coefficients))
    return max(0.0, 1.0 - inside / denominator)


def summarize(values: list[float]) -> dict[str, float]:
    if not values:
        return {key: 0.0 for key in ["min", "p05", "median", "mean", "p95", "max"]}
    arr = np.array(values, dtype=float)
    return {
        "min": float(arr.min()),
        "p05": float(np.quantile(arr, 0.05)),
        "median": float(np.median(arr)),
        "mean": float(arr.mean()),
        "p95": float(np.quantile(arr, 0.95)),
        "max": float(arr.max()),
    }


def positive_summary(values: list[float]) -> dict[str, float]:
    return summarize([value for value in values if value > 0.0])


def ledger_terms(
    *,
    q: np.ndarray,
    basis: np.ndarray,
    gram: np.ndarray,
    sizes: list[int],
    active: list[int],
    h_hat: np.ndarray,
    reciprocal_vector: np.ndarray,
    depth_cost: float,
) -> dict[str, float]:
    active_basis = q[:, active]
    return {
        "block_coupling": off_block_energy(q.T @ gram @ q, sizes),
        "fisher_projection_error": projection_error(h_hat, active_basis),
        "reciprocal_projection_error": projection_error(reciprocal_vector, active_basis),
        "closure_leakage": closure_leakage(basis=basis, q=q, active=active),
        "resource_cost": len(active) / q.shape[0],
        "depth_cost": depth_cost,
        "packet_commutator_impurity": packet_commutator_impurity(q, sizes),
        "first_order_packet_cost": first_order_packet_cost(q, sizes),
    }


def weighted_value(terms: dict[str, float], weights: dict[str, float]) -> float:
    return (
        weights["block"] * terms["block_coupling"]
        + weights["fisher_projection"] * terms["fisher_projection_error"]
        + weights["reciprocal_projection"] * terms["reciprocal_projection_error"]
        + weights["closure"] * terms["closure_leakage"]
        + weights["resource"] * terms["resource_cost"]
        + weights["depth"] * terms["depth_cost"]
        + weights["packet_commutator"] * terms["packet_commutator_impurity"]
        + weights["first_order_packet"] * terms["first_order_packet_cost"]
    )


def structural_value(terms: dict[str, float], weights: dict[str, float]) -> float:
    no_packet = dict(weights)
    no_packet["packet_commutator"] = 0.0
    no_packet["first_order_packet"] = 0.0
    return weighted_value(terms, no_packet)


def case_targets(n: int, min_omega: int) -> list[int]:
    return [d for d in conductor_order(n) if omega(d) >= min_omega]


def evaluate_case(
    *,
    n: int,
    target: int,
    samples: int,
    seed: int,
    amplitude_fraction: float,
    weights: dict[str, float],
    keep_top: int,
) -> dict[str, Any]:
    basis, modes, sizes, order = real_fourier_basis(n)
    dim = basis.shape[1]
    active = active_indices(order, sizes, target)
    target_indices = [i for i, mode in enumerate(modes) if mode.conductor == target]
    h_hat = np.zeros(dim, dtype=float)
    h_hat[target_indices] = 1.0
    h_values = basis @ h_hat
    probability, amplitude = safe_probability(h_values, amplitude_fraction)
    gram = fisher_gram(probability, basis)
    reciprocal_values = 1.0 / probability
    reciprocal_vector = basis.T @ reciprocal_values
    depth_cost = omega(target) / max(omega(n), 1)
    identity = np.eye(dim)
    conductor_terms = ledger_terms(
        q=identity,
        basis=basis,
        gram=gram,
        sizes=sizes,
        active=active,
        h_hat=h_hat,
        reciprocal_vector=reciprocal_vector,
        depth_cost=depth_cost,
    )
    conductor_structural = structural_value(conductor_terms, weights)
    conductor_full = weighted_value(conductor_terms, weights)

    rng = np.random.default_rng(seed)
    random_terms: list[dict[str, float]] = []
    random_structural_values: list[float] = []
    random_full_values: list[float] = []
    break_even_packet_commutator: list[float] = []
    break_even_first_order: list[float] = []
    best_mixed: list[dict[str, Any]] = []

    for sample_index in range(samples):
        q = random_orthogonal(dim, rng)
        terms = ledger_terms(
            q=q,
            basis=basis,
            gram=gram,
            sizes=sizes,
            active=active,
            h_hat=h_hat,
            reciprocal_vector=reciprocal_vector,
            depth_cost=depth_cost,
        )
        full = weighted_value(terms, weights)
        structural = structural_value(terms, weights)
        random_terms.append(terms)
        random_full_values.append(full)
        random_structural_values.append(structural)
        structural_gain = conductor_structural - structural
        lambda_needed = (
            structural_gain / terms["packet_commutator_impurity"]
            if structural_gain > 0.0 and terms["packet_commutator_impurity"] > 1e-15
            else 0.0
        )
        mu_needed = (
            structural_gain / terms["first_order_packet_cost"]
            if structural_gain > 0.0 and terms["first_order_packet_cost"] > 1e-15
            else 0.0
        )
        break_even_packet_commutator.append(lambda_needed)
        break_even_first_order.append(mu_needed)
        record = {
            "sample": sample_index,
            "full_value": full,
            "structural_value": structural,
            "structural_gain_vs_conductor": structural_gain,
            "break_even_packet_commutator": lambda_needed,
            "break_even_first_order_packet": mu_needed,
            "terms": terms,
        }
        best_mixed.append(record)
        best_mixed.sort(key=lambda item: item["structural_value"])
        best_mixed = best_mixed[:keep_top]

    better_structural = sum(value < conductor_structural for value in random_structural_values)
    better_full = sum(value < conductor_full for value in random_full_values)
    term_summaries = {
        key: summarize([terms[key] for terms in random_terms])
        for key in conductor_terms
    }
    return {
        "row": f"Z/{n}Z",
        "n": n,
        "target_conductor": target,
        "target_prime_support": prime_factors(target),
        "conductor_order": order,
        "packet_sizes": dict(zip((str(cond) for cond in order), sizes)),
        "dimension": dim,
        "active_dimension": len(active),
        "active_conductors": [cond for cond in order if target % cond == 0],
        "samples": samples,
        "seed": seed,
        "amplitude_fraction": amplitude_fraction,
        "actual_amplitude": amplitude,
        "probability_min": float(probability.min()),
        "probability_max": float(probability.max()),
        "weights": weights,
        "conductor_terms": conductor_terms,
        "conductor_structural_value": conductor_structural,
        "conductor_full_value": conductor_full,
        "random_structural_value": summarize(random_structural_values),
        "random_full_value": summarize(random_full_values),
        "random_term_summaries": term_summaries,
        "random_better_structural_count": better_structural,
        "random_better_full_count": better_full,
        "break_even_packet_commutator": summarize(break_even_packet_commutator),
        "positive_break_even_packet_commutator": positive_summary(break_even_packet_commutator),
        "break_even_first_order_packet": summarize(break_even_first_order),
        "positive_break_even_first_order_packet": positive_summary(break_even_first_order),
        "best_mixed_by_structural_value": best_mixed,
    }


def build_weights(args: argparse.Namespace) -> dict[str, float]:
    return {
        "block": args.block_weight,
        "fisher_projection": args.fisher_projection_weight,
        "reciprocal_projection": args.reciprocal_projection_weight,
        "closure": args.closure_weight,
        "resource": args.resource_weight,
        "depth": args.depth_weight,
        "packet_commutator": args.packet_commutator_weight,
        "first_order_packet": args.first_order_packet_weight,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = parse_int_csv(args.rows)
    weights = build_weights(args)
    results: list[dict[str, Any]] = []
    for row_index, n in enumerate(rows):
        if not is_squarefree(n):
            raise ValueError(f"row {n} is not squarefree")
        for target in case_targets(n, args.min_target_omega):
            results.append(
                evaluate_case(
                    n=n,
                    target=target,
                    samples=args.samples,
                    seed=args.seed + 1009 * row_index + 37 * target,
                    amplitude_fraction=args.amplitude_fraction,
                    weights=weights,
                    keep_top=args.keep_top,
                )
            )
    return {
        "purpose": (
            "Squarefree/primorial information-investment frame testbed: compare "
            "CRT conductor frames against Haar mixed frames on Z/nZ conductor "
            "lattice prefixes and record packet-price budgets."
        ),
        "config": {
            "rows": rows,
            "samples": args.samples,
            "seed": args.seed,
            "amplitude_fraction": args.amplitude_fraction,
            "min_target_omega": args.min_target_omega,
            "weights": weights,
        },
        "results": results,
    }


def render_float(value: float) -> str:
    return f"{value:.7g}"


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Helmert Primorial/Squarefree Testbed",
        "",
        "This report is the first Paper 25 frame-ledger testbed outside local",
        "fields.  For squarefree cyclic rows `Z/nZ`, conductor packets form a",
        "CRT divisor lattice.  A target conductor `d` uses the active prefix",
        "spanned by all packets `e | d`; this replaces the wild quotient prefix",
        "used in `F_q[u]/(u^k)`.",
        "",
        "The table compares the conductor/CRT frame against Haar mixed frames",
        "with the same conductor block sizes.  `structural` means the ledger",
        "without packet-commutator or first-order packet price.  The break-even",
        "columns record the packet price needed when a mixed frame beats that",
        "unpriced structural ledger.",
        "",
        "## Config",
        "",
    ]
    for key, value in payload["config"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines += [
        "",
        "## Summary",
        "",
        "| row | target | active conductors | dim | active dim | conductor structural | random structural min | random structural median | better structural | break-even M max | break-even N max | better full |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in payload["results"]:
        lines.append(
            "| {row} | {target} | {active} | {dim} | {active_dim} | {cstruct} | {rmin} | {rmed} | {better}/{samples} | {bem} | {ben} | {better_full}/{samples} |".format(
                row=result["row"],
                target=result["target_conductor"],
                active=result["active_conductors"],
                dim=result["dimension"],
                active_dim=result["active_dimension"],
                cstruct=render_float(result["conductor_structural_value"]),
                rmin=render_float(result["random_structural_value"]["min"]),
                rmed=render_float(result["random_structural_value"]["median"]),
                better=result["random_better_structural_count"],
                samples=result["samples"],
                bem=render_float(result["break_even_packet_commutator"]["max"]),
                ben=render_float(result["break_even_first_order_packet"]["max"]),
                better_full=result["random_better_full_count"],
            )
        )

    lines += [
        "",
        "## Detail",
        "",
    ]
    for result in payload["results"]:
        lines += [
            f"### {result['row']} target conductor `{result['target_conductor']}`",
            "",
            f"- conductor order: `{result['conductor_order']}`",
            f"- packet sizes: `{result['packet_sizes']}`",
            f"- active conductors: `{result['active_conductors']}`",
            f"- probability range: `{result['probability_min']:.6g}` to `{result['probability_max']:.6g}`",
            "",
            "| term | conductor | random median | random p05 | random p95 |",
            "|---|---:|---:|---:|---:|",
        ]
        for key, conductor_value in result["conductor_terms"].items():
            summary = result["random_term_summaries"][key]
            lines.append(
                f"| {key} | {conductor_value:.7g} | {summary['median']:.7g} | {summary['p05']:.7g} | {summary['p95']:.7g} |"
            )
        lines += [
            "",
            "| best sample | structural | gain vs conductor | break-even M | break-even N | block | closure | projection |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for item in result["best_mixed_by_structural_value"]:
            terms = item["terms"]
            projection = terms["fisher_projection_error"] + terms["reciprocal_projection_error"]
            lines.append(
                "| {sample} | {structural:.7g} | {gain:.7g} | {bem:.7g} | {ben:.7g} | {block:.7g} | {closure:.7g} | {proj:.7g} |".format(
                    sample=item["sample"],
                    structural=item["structural_value"],
                    gain=item["structural_gain_vs_conductor"],
                    bem=item["break_even_packet_commutator"],
                    ben=item["break_even_first_order_packet"],
                    block=terms["block_coupling"],
                    closure=terms["closure_leakage"],
                    proj=projection,
                )
            )
        lines.append("")

    lines += [
        "## Reading",
        "",
        "For local wild rows, Theorems 3.10 and 3.14 use a quotient map that",
        "preserves packet prefixes.  Squarefree rows do not have that single",
        "tower map.  This testbed replaces it with the CRT divisor prefix",
        "`e | d`.  If mixed frames beat the conductor frame structurally, the",
        "break-even columns quantify how much packet budget is needed to keep",
        "prime/conductor compatibility.",
        "",
        "In the default run, full-conductor rows behave like top-prefix rows:",
        "`Z/6Z`, `Z/10Z`, `Z/15Z`, and the full `Z/30Z` target all have",
        "mixed structural wins in every sample, but none survive the unit",
        "packet-commutator price.  The proper CRT faces inside `Z/30Z`,",
        "targets `6`, `10`, and `15`, show no mixed structural wins in 300",
        "samples.  This suggests a candidate squarefree replacement for local",
        "packet-locality: proper primorial faces may have structural",
        "CRT-face stability, while full-conductor rows retain the top-prefix",
        "need for priced carry.",
        "",
        "The next theorem-facing question is whether these budgets and face",
        "stability signals have stable scaling along primorial rows.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", default="6,10,15,30")
    parser.add_argument("--samples", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20260516)
    parser.add_argument("--amplitude-fraction", type=float, default=0.35)
    parser.add_argument("--min-target-omega", type=int, default=2)
    parser.add_argument("--keep-top", type=int, default=5)
    parser.add_argument("--block-weight", type=float, default=1.0)
    parser.add_argument("--fisher-projection-weight", type=float, default=1.0)
    parser.add_argument("--reciprocal-projection-weight", type=float, default=1.0)
    parser.add_argument("--closure-weight", type=float, default=1.0)
    parser.add_argument("--resource-weight", type=float, default=0.1)
    parser.add_argument("--depth-weight", type=float, default=0.1)
    parser.add_argument("--packet-commutator-weight", type=float, default=1.0)
    parser.add_argument("--first-order-packet-weight", type=float, default=0.0)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    payload = run(args)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    args.report.write_text(render_report(payload), encoding="utf-8")

    print(f"wrote {args.json}")
    print(f"wrote {args.report}")
    for result in payload["results"]:
        print(
            "{row} target={target}: better_structural={better}/{samples}, "
            "better_full={better_full}/{samples}, break_even_M_max={bem:.6g}, "
            "break_even_N_max={ben:.6g}".format(
                row=result["row"],
                target=result["target_conductor"],
                better=result["random_better_structural_count"],
                better_full=result["random_better_full_count"],
                samples=result["samples"],
                bem=result["break_even_packet_commutator"]["max"],
                ben=result["break_even_first_order_packet"]["max"],
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
