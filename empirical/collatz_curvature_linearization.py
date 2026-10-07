"""Curvature-linearization probe for the accelerated odd Collatz map.

The accelerated odd map is

    U(n) = (3n + 1) / 2^v2(3n + 1),  n odd.

On a finite quotient Q = Z/(2^a 3^b)Z, this map is not a single deterministic
quotient function unless enough hidden 2-adic lift data is retained.  This
script samples those hidden lifts, builds the induced stochastic kernel on odd
residue classes, fits a finite affine-convolution linear skeleton, and measures
the Fisher residual grouped by carry depth.

The point is reverse engineering, not proof: isolate which part of the
projected dynamics is linear quotient motion and which part is structured
carry curvature.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable


Vector = dict[int, float]
Rows = dict[int, Counter[int]]
JointRows = Counter[tuple[int, int, int]]


@dataclass(frozen=True)
class Kernel:
    two_bits: int
    three_pow: int
    lift_bits: int
    modulus: int
    lift_count: int
    sources: tuple[int, ...]
    row_counts: Rows
    carry_counts: dict[int, Counter[int]]
    joint_counts: JointRows


@dataclass(frozen=True)
class ModelMetrics:
    name: str
    multiplier: int
    offset: int
    mean_fisher_energy: float
    mean_fisher_norm: float
    max_fisher_norm: float
    mean_hellinger: float
    max_hellinger: float
    mean_l1: float
    max_l1: float


@dataclass(frozen=True)
class AffineModel:
    name: str
    multiplier: int
    offset: int
    delta_distribution: Vector
    metrics: ModelMetrics


def vp(n: int, prime: int) -> int:
    if n <= 0:
        raise ValueError("vp is defined here only for positive integers")
    depth = 0
    while n % prime == 0:
        n //= prime
        depth += 1
    return depth


def accelerated_odd_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("accelerated odd step requires a positive odd integer")
    raised = 3 * n + 1
    depth = vp(raised, 2)
    return raised >> depth, depth


def entropy(counter: Counter[object]) -> float:
    total = sum(counter.values())
    if total == 0:
        return 0.0
    value = 0.0
    for count in counter.values():
        p = count / total
        value -= p * math.log2(p)
    return value


def normalize(counter: Counter[int]) -> Vector:
    total = sum(counter.values())
    if total == 0:
        return {}
    return {key: count / total for key, count in sorted(counter.items())}


def rounded(value: object) -> object:
    if isinstance(value, float):
        return round(value, 8)
    if isinstance(value, dict):
        return {str(key): rounded(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [rounded(inner) for inner in value]
    if isinstance(value, tuple):
        return [rounded(inner) for inner in value]
    return value


def residue_label(residue: int, two_bits: int, three_pow: int) -> str:
    return (
        f"{residue}"
        f" [2:{residue % (1 << two_bits):0{two_bits}b},"
        f" 3:{residue % (3**three_pow)}]"
    )


def build_kernel(two_bits: int, three_pow: int, lift_bits: int) -> Kernel:
    modulus = (1 << two_bits) * (3**three_pow)
    lift_count = 1 << lift_bits
    sources = tuple(range(1, modulus, 2))
    row_counts: Rows = {}
    carry_counts: dict[int, Counter[int]] = {}
    joint_counts: JointRows = Counter()

    for source in sources:
        targets: Counter[int] = Counter()
        carries: Counter[int] = Counter()
        for lift in range(lift_count):
            n = source + lift * modulus
            target, carry = accelerated_odd_step(n)
            target_residue = target % modulus
            targets[target_residue] += 1
            carries[carry] += 1
            joint_counts[(source, target_residue, carry)] += 1
        row_counts[source] = targets
        carry_counts[source] = carries

    return Kernel(
        two_bits=two_bits,
        three_pow=three_pow,
        lift_bits=lift_bits,
        modulus=modulus,
        lift_count=lift_count,
        sources=sources,
        row_counts=row_counts,
        carry_counts=carry_counts,
        joint_counts=joint_counts,
    )


def kernel_summary(kernel: Kernel) -> dict[str, object]:
    outdegrees = Counter(len(row) for row in kernel.row_counts.values())
    entropies = [entropy(row) for row in kernel.row_counts.values()]
    carry_total: Counter[int] = Counter()
    for counts in kernel.carry_counts.values():
        carry_total.update(counts)
    return {
        "modulus": kernel.modulus,
        "odd_sources": len(kernel.sources),
        "hidden_lifts_per_source": kernel.lift_count,
        "total_samples": len(kernel.sources) * kernel.lift_count,
        "outdegree_distribution": dict(sorted(outdegrees.items())),
        "mean_row_entropy_bits": sum(entropies) / len(entropies),
        "max_row_entropy_bits": max(entropies),
        "carry_distribution": dict(sorted(carry_total.items())),
    }


def affine_delta_distribution(kernel: Kernel, multiplier: int, offset: int) -> Vector:
    counts: Counter[int] = Counter()
    for source, row in kernel.row_counts.items():
        base = (multiplier * source + offset) % kernel.modulus
        for target, count in row.items():
            counts[(target - base) % kernel.modulus] += count
    return normalize(counts)


def affine_model_row(
    kernel: Kernel,
    multiplier: int,
    offset: int,
    delta_distribution: Vector,
    source: int,
) -> Vector:
    base = (multiplier * source + offset) % kernel.modulus
    row = {
        target: delta_distribution.get((target - base) % kernel.modulus, 0.0)
        for target in kernel.sources
    }
    total = sum(row.values())
    if total <= 0.0:
        uniform = 1.0 / len(kernel.sources)
        return {target: uniform for target in kernel.sources}
    if abs(total - 1.0) > 1e-12:
        return {target: value / total for target, value in row.items()}
    return row


def true_row(kernel: Kernel, source: int) -> Vector:
    return {
        target: count / kernel.lift_count
        for target, count in kernel.row_counts[source].items()
    }


def evaluate_counts_model(
    kernel: Kernel,
    name: str,
    multiplier: int,
    offset: int,
    counts_by_source: Rows,
    totals_by_source: dict[int, int],
    sources: tuple[int, ...],
    row_model: Callable[[int], Vector],
) -> ModelMetrics:
    n = len(kernel.sources)
    fisher_energies: list[float] = []
    fisher_norms: list[float] = []
    hellingers: list[float] = []
    l1s: list[float] = []

    for source in sources:
        total = totals_by_source[source]
        p = {
            target: count / total
            for target, count in counts_by_source[source].items()
        }
        q = row_model(source)
        l2 = 0.0
        l1 = 0.0
        affinity = 0.0
        for target in kernel.sources:
            pv = p.get(target, 0.0)
            qv = q.get(target, 0.0)
            delta = pv - qv
            l2 += delta * delta
            l1 += abs(delta)
            if pv > 0.0 and qv > 0.0:
                affinity += math.sqrt(pv * qv)
        fisher_energy = n * l2
        fisher_energies.append(fisher_energy)
        fisher_norms.append(math.sqrt(max(0.0, fisher_energy)))
        hellingers.append(math.sqrt(max(0.0, 1.0 - affinity)))
        l1s.append(l1)

    return ModelMetrics(
        name=name,
        multiplier=multiplier,
        offset=offset,
        mean_fisher_energy=sum(fisher_energies) / len(fisher_energies),
        mean_fisher_norm=sum(fisher_norms) / len(fisher_norms),
        max_fisher_norm=max(fisher_norms),
        mean_hellinger=sum(hellingers) / len(hellingers),
        max_hellinger=max(hellingers),
        mean_l1=sum(l1s) / len(l1s),
        max_l1=max(l1s),
    )


def evaluate_model(
    kernel: Kernel,
    name: str,
    multiplier: int,
    offset: int,
    row_model: Callable[[int], Vector],
) -> ModelMetrics:
    return evaluate_counts_model(
        kernel,
        name,
        multiplier,
        offset,
        kernel.row_counts,
        {source: kernel.lift_count for source in kernel.sources},
        kernel.sources,
        row_model,
    )


def build_affine_model(kernel: Kernel, name: str, multiplier: int, offset: int) -> AffineModel:
    q = affine_delta_distribution(kernel, multiplier, offset)
    metrics = evaluate_model(
        kernel,
        name,
        multiplier,
        offset,
        lambda source: affine_model_row(kernel, multiplier, offset, q, source),
    )
    return AffineModel(name, multiplier, offset, q, metrics)


def affine_image_size(
    kernel: Kernel,
    multiplier: int,
    offset: int,
    sources: tuple[int, ...] | None = None,
) -> int:
    active_sources = sources or kernel.sources
    return len({
        (multiplier * source + offset) % kernel.modulus
        for source in active_sources
    })


def fit_best_affine_model(
    kernel: Kernel,
    *,
    allow_zero_multiplier: bool,
    min_image_size: int,
) -> AffineModel:
    best: AffineModel | None = None
    for multiplier in range(kernel.modulus):
        if multiplier == 0 and not allow_zero_multiplier:
            continue
        for offset in range(kernel.modulus):
            if affine_image_size(kernel, multiplier, offset) < min_image_size:
                continue
            candidate = build_affine_model(kernel, "best affine-convolution", multiplier, offset)
            if best is None:
                best = candidate
                continue
            left = candidate.metrics
            right = best.metrics
            if (
                left.mean_fisher_energy,
                left.mean_hellinger,
                left.max_fisher_norm,
            ) < (
                right.mean_fisher_energy,
                right.mean_hellinger,
                right.max_fisher_norm,
            ):
                best = candidate
    assert best is not None
    return best


def conditional_delta_distribution(
    kernel: Kernel,
    counts_by_source: Rows,
    multiplier: int,
    offset: int,
) -> Vector:
    counts: Counter[int] = Counter()
    for source, row in counts_by_source.items():
        base = (multiplier * source + offset) % kernel.modulus
        for target, count in row.items():
            counts[(target - base) % kernel.modulus] += count
    return normalize(counts)


def build_conditional_affine_model(
    kernel: Kernel,
    name: str,
    counts_by_source: Rows,
    totals_by_source: dict[int, int],
    sources: tuple[int, ...],
    multiplier: int,
    offset: int,
) -> AffineModel:
    q = conditional_delta_distribution(kernel, counts_by_source, multiplier, offset)
    metrics = evaluate_counts_model(
        kernel,
        name,
        multiplier,
        offset,
        counts_by_source,
        totals_by_source,
        sources,
        lambda source: affine_model_row(kernel, multiplier, offset, q, source),
    )
    return AffineModel(name, multiplier, offset, q, metrics)


def fit_conditional_affine_model(
    kernel: Kernel,
    name: str,
    counts_by_source: Rows,
    totals_by_source: dict[int, int],
    sources: tuple[int, ...],
    *,
    min_image_size: int,
) -> AffineModel:
    best: AffineModel | None = None
    for multiplier in range(kernel.modulus):
        for offset in range(kernel.modulus):
            if affine_image_size(kernel, multiplier, offset, sources) < min_image_size:
                continue
            candidate = build_conditional_affine_model(
                kernel,
                name,
                counts_by_source,
                totals_by_source,
                sources,
                multiplier,
                offset,
            )
            if best is None:
                best = candidate
                continue
            left = candidate.metrics
            right = best.metrics
            if (
                left.mean_fisher_energy,
                left.mean_hellinger,
                left.max_fisher_norm,
            ) < (
                right.mean_fisher_energy,
                right.mean_hellinger,
                right.max_fisher_norm,
            ):
                best = candidate
    assert best is not None
    return best


def carry_delta_distributions(
    kernel: Kernel,
    multiplier: int,
    offset: int,
) -> dict[int, Vector]:
    counts_by_carry: dict[int, Counter[int]] = defaultdict(Counter)
    for (source, target, carry), count in kernel.joint_counts.items():
        base = (multiplier * source + offset) % kernel.modulus
        counts_by_carry[carry][(target - base) % kernel.modulus] += count
    return {
        carry: normalize(counts)
        for carry, counts in sorted(counts_by_carry.items())
    }


def carry_conditional_counts(kernel: Kernel, carry: int) -> tuple[Rows, dict[int, int], tuple[int, ...]]:
    counts_by_source: Rows = {}
    totals_by_source: dict[int, int] = {}
    for source in kernel.sources:
        targets: Counter[int] = Counter()
        for (joint_source, target, joint_carry), count in kernel.joint_counts.items():
            if joint_source == source and joint_carry == carry:
                targets[target] += count
        if targets:
            counts_by_source[source] = targets
            totals_by_source[source] = sum(targets.values())
    sources = tuple(sorted(counts_by_source))
    return counts_by_source, totals_by_source, sources


def fit_carry_sliced_models(kernel: Kernel) -> dict[int, AffineModel]:
    carry_totals: Counter[int] = Counter()
    for counts in kernel.carry_counts.values():
        carry_totals.update(counts)

    models: dict[int, AffineModel] = {}
    for carry in sorted(carry_totals):
        counts_by_source, totals_by_source, sources = carry_conditional_counts(kernel, carry)
        min_image_size = max(1, len(sources) // 2)
        models[carry] = fit_conditional_affine_model(
            kernel,
            f"carry-sliced affine s={carry}",
            counts_by_source,
            totals_by_source,
            sources,
            min_image_size=min_image_size,
        )
    return models


def carry_aware_row(
    kernel: Kernel,
    multiplier: int,
    offset: int,
    q_by_carry: dict[int, Vector],
    source: int,
) -> Vector:
    row = {target: 0.0 for target in kernel.sources}
    for carry, count in kernel.carry_counts[source].items():
        carry_weight = count / kernel.lift_count
        q = q_by_carry[carry]
        packet_row = affine_model_row(kernel, multiplier, offset, q, source)
        for target, value in packet_row.items():
            row[target] += carry_weight * value
    total = sum(row.values())
    if total <= 0.0:
        uniform = 1.0 / len(kernel.sources)
        return {target: uniform for target in kernel.sources}
    if abs(total - 1.0) > 1e-12:
        return {target: value / total for target, value in row.items()}
    return row


def carry_sliced_row(
    kernel: Kernel,
    models_by_carry: dict[int, AffineModel],
    source: int,
) -> Vector:
    row = {target: 0.0 for target in kernel.sources}
    for carry, count in kernel.carry_counts[source].items():
        carry_weight = count / kernel.lift_count
        model = models_by_carry[carry]
        packet_row = affine_model_row(
            kernel,
            model.multiplier,
            model.offset,
            model.delta_distribution,
            source,
        )
        for target, value in packet_row.items():
            row[target] += carry_weight * value
    total = sum(row.values())
    if total <= 0.0:
        uniform = 1.0 / len(kernel.sources)
        return {target: uniform for target in kernel.sources}
    if abs(total - 1.0) > 1e-12:
        return {target: value / total for target, value in row.items()}
    return row


def exact_carry_lift_metrics(kernel: Kernel) -> ModelMetrics:
    return evaluate_model(
        kernel,
        "exact carry-lift oracle",
        -1,
        -1,
        lambda source: true_row(kernel, source),
    )


def carry_lift_formula_audit(kernel: Kernel) -> list[dict[str, object]]:
    """Audit the exact formula after retaining k mod 2^s lift coordinates.

    For n = source + kQ and s = v2(3n+1), the projected target is

        ((3(source + kQ) + 1) / 2^s) mod Q.

    At fixed source and carry depth s, the target is determined by k mod 2^s.
    This audit records how source-only ambiguity collapses after that lift
    coordinate is retained.
    """

    source_targets: dict[int, dict[int, set[int]]] = defaultdict(lambda: defaultdict(set))
    lift_cell_targets: dict[int, dict[tuple[int, int], set[int]]] = defaultdict(lambda: defaultdict(set))
    lift_cell_counts: dict[int, Counter[tuple[int, int]]] = defaultdict(Counter)
    formula_failures: Counter[int] = Counter()

    for source in kernel.sources:
        for lift in range(kernel.lift_count):
            n = source + lift * kernel.modulus
            target, carry = accelerated_odd_step(n)
            target_residue = target % kernel.modulus
            formula_target = ((3 * n + 1) >> carry) % kernel.modulus
            if formula_target != target_residue:
                formula_failures[carry] += 1
            lift_cell = lift % (1 << carry)
            source_targets[carry][source].add(target_residue)
            lift_cell_targets[carry][(source, lift_cell)].add(target_residue)
            lift_cell_counts[carry][(source, lift_cell)] += 1

    rows: list[dict[str, object]] = []
    for carry in sorted(source_targets):
        source_degrees = [len(targets) for targets in source_targets[carry].values()]
        cell_degrees = [len(targets) for targets in lift_cell_targets[carry].values()]
        cell_sample_counts = list(lift_cell_counts[carry].values())
        rows.append(
            {
                "carry": carry,
                "samples": sum(cell_sample_counts),
                "sources_hit": len(source_targets[carry]),
                "source_target_edges": sum(source_degrees),
                "mean_source_outdegree": sum(source_degrees) / len(source_degrees),
                "max_source_outdegree": max(source_degrees),
                "lift_bits_required": carry,
                "complete_lift_cycle_sampled": carry <= kernel.lift_bits,
                "lift_cells": len(lift_cell_targets[carry]),
                "deterministic_lift_cells": sum(1 for degree in cell_degrees if degree == 1),
                "max_lift_cell_outdegree": max(cell_degrees),
                "mean_lift_cell_sample_count": sum(cell_sample_counts) / len(cell_sample_counts),
                "formula_failures": formula_failures.get(carry, 0),
            }
        )
    return rows


def carry_residual_rows(
    kernel: Kernel,
    multiplier: int,
    offset: int,
    q_global: Vector,
    q_by_carry: dict[int, Vector],
    sliced_models: dict[int, AffineModel],
) -> list[dict[str, object]]:
    n = len(kernel.sources)
    carry_totals: Counter[int] = Counter()
    for counts in kernel.carry_counts.values():
        carry_totals.update(counts)

    rows = []
    for carry, sample_count in sorted(carry_totals.items()):
        global_energy = 0.0
        carry_energy = 0.0
        sliced_energy = 0.0
        source_count = 0
        sliced_model = sliced_models[carry]
        for source in kernel.sources:
            source_carry_count = kernel.carry_counts[source].get(carry, 0)
            if source_carry_count == 0:
                continue
            source_count += 1
            carry_weight = source_carry_count / kernel.lift_count
            q0 = affine_model_row(kernel, multiplier, offset, q_global, source)
            q1_packet = affine_model_row(
                kernel,
                multiplier,
                offset,
                q_by_carry[carry],
                source,
            )
            q2_packet = affine_model_row(
                kernel,
                sliced_model.multiplier,
                sliced_model.offset,
                sliced_model.delta_distribution,
                source,
            )
            for target in kernel.sources:
                true_value = kernel.joint_counts.get((source, target, carry), 0) / kernel.lift_count
                baseline_value = carry_weight * q0[target]
                carry_value = carry_weight * q1_packet[target]
                sliced_value = carry_weight * q2_packet[target]
                global_delta = true_value - baseline_value
                carry_delta = true_value - carry_value
                sliced_delta = true_value - sliced_value
                global_energy += n * global_delta * global_delta
                carry_energy += n * carry_delta * carry_delta
                sliced_energy += n * sliced_delta * sliced_delta

        top_deltas = sorted(
            sliced_model.delta_distribution.items(),
            key=lambda item: (-item[1], item[0]),
        )[:8]
        rows.append(
            {
                "carry": carry,
                "samples": sample_count,
                "sources_hit": source_count,
                "global_residual_energy": global_energy,
                "carry_conditioned_residual_energy": carry_energy,
                "carry_sliced_residual_energy": sliced_energy,
                "reduction_fraction": (
                    1.0 - carry_energy / global_energy if global_energy > 0.0 else 0.0
                ),
                "sliced_reduction_fraction": (
                    1.0 - sliced_energy / global_energy if global_energy > 0.0 else 0.0
                ),
                "sliced_multiplier": sliced_model.multiplier,
                "sliced_offset": sliced_model.offset,
                "sliced_image_size": affine_image_size(
                    kernel,
                    sliced_model.multiplier,
                    sliced_model.offset,
                    tuple(
                        source
                        for source in kernel.sources
                        if kernel.carry_counts[source].get(carry, 0) > 0
                    ),
                ),
                "top_affine_deltas": top_deltas,
            }
        )
    return rows


def top_residual_edges(
    kernel: Kernel,
    row_model: Callable[[int], Vector],
    limit: int,
) -> list[dict[str, object]]:
    edges = []
    for source in kernel.sources:
        p = true_row(kernel, source)
        q = row_model(source)
        for target in kernel.sources:
            true_value = p.get(target, 0.0)
            model_value = q.get(target, 0.0)
            residual = true_value - model_value
            if abs(residual) <= 1e-12:
                continue
            true_count = kernel.row_counts[source].get(target, 0)
            carry_mix = {
                carry: count / true_count
                for (joint_source, joint_target, carry), count in kernel.joint_counts.items()
                if joint_source == source and joint_target == target and true_count > 0
            }
            edges.append(
                {
                    "source": source,
                    "target": target,
                    "true_probability": true_value,
                    "model_probability": model_value,
                    "residual": residual,
                    "carry_mix": dict(sorted(carry_mix.items())),
                }
            )
    edges.sort(key=lambda row: (-abs(float(row["residual"])), int(row["source"]), int(row["target"])))
    return edges[:limit]


def top_distribution_entries(distribution: Vector, limit: int) -> list[tuple[int, float]]:
    return sorted(distribution.items(), key=lambda item: (-item[1], item[0]))[:limit]


def metrics_table(models: list[ModelMetrics]) -> list[str]:
    lines = [
        "| model | A | B | mean Fisher energy | mean Fisher norm | max Fisher norm | mean Hellinger | mean L1 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for model in models:
        multiplier = "-" if model.multiplier < 0 else str(model.multiplier)
        offset = "-" if model.offset < 0 else str(model.offset)
        lines.append(
            "| "
            + " | ".join(
                [
                    model.name,
                    multiplier,
                    offset,
                    f"{model.mean_fisher_energy:.6f}",
                    f"{model.mean_fisher_norm:.6f}",
                    f"{model.max_fisher_norm:.6f}",
                    f"{model.mean_hellinger:.6f}",
                    f"{model.mean_l1:.6f}",
                ]
            )
            + " |"
        )
    return lines


def make_report(
    kernel: Kernel,
    summary: dict[str, object],
    null_model: AffineModel,
    seed_model: AffineModel,
    best_model: AffineModel,
    carry_metrics: ModelMetrics,
    carry_sliced_metrics: ModelMetrics,
    oracle_metrics: ModelMetrics,
    q_by_carry: dict[int, Vector],
    carry_rows: list[dict[str, object]],
    carry_lift_rows: list[dict[str, object]],
    residual_edges: list[dict[str, object]],
) -> str:
    same_base_reduction = (
        1.0 - carry_metrics.mean_fisher_energy / best_model.metrics.mean_fisher_energy
        if best_model.metrics.mean_fisher_energy > 0.0
        else 0.0
    )
    sliced_reduction = (
        1.0 - carry_sliced_metrics.mean_fisher_energy / best_model.metrics.mean_fisher_energy
        if best_model.metrics.mean_fisher_energy > 0.0
        else 0.0
    )

    lines = [
        f"# Collatz Curvature Linearization: 2^{kernel.two_bits} x 3^{kernel.three_pow}",
        "",
        "## Status",
        "",
        "This report samples the accelerated odd Collatz map on a finite quotient simplex, fits an affine-convolution linear skeleton, and measures the residual as carry-depth curvature.",
        "",
        f"- modulus: `{kernel.modulus}`",
        f"- odd residue states: `{len(kernel.sources)}`",
        f"- hidden lifts per state: `{kernel.lift_count}`",
        f"- total samples: `{summary['total_samples']}`",
        f"- fitted affine image size: `{affine_image_size(kernel, best_model.multiplier, best_model.offset)}` of `{len(kernel.sources)}` odd states",
        f"- true-kernel outdegree distribution: `{summary['outdegree_distribution']}`",
        f"- mean true row entropy: `{summary['mean_row_entropy_bits']:.6f}` bits",
        f"- max true row entropy: `{summary['max_row_entropy_bits']:.6f}` bits",
        "",
        "## Linear Skeleton Fit",
        "",
        "The null model is the source-blind target marginal.  The seed model uses the visible affine numerator `3n+1`.  The fitted model searches source-sensitive affine bases `A*n+B (mod Q)` and learns one translation-invariant residual packet over affine deltas.  The carry-sliced model repeats that affine fit separately inside each carry packet.",
        "",
        *metrics_table([
            null_model.metrics,
            seed_model.metrics,
            best_model.metrics,
            carry_metrics,
            carry_sliced_metrics,
            oracle_metrics,
        ]),
        "",
        f"Same-base carry conditioning changes the fitted mean Fisher residual energy by `{100.0 * same_base_reduction:.2f}%` relative to the best global affine-convolution model.",
        f"Carry-sliced affine linearization changes it by `{100.0 * sliced_reduction:.2f}%`.",
        "The exact carry-lift oracle keeps the hidden lift coordinate required by division by `2^s`, so its residual is zero by construction; the audit below records the coordinate cost.",
        "",
        "Top deltas in the best global affine residual packet:",
        "",
    ]
    for delta, probability in top_distribution_entries(best_model.delta_distribution, 12):
        lines.append(f"- delta `{delta}`: `{probability:.6f}`")

    lines += [
        "",
        "## Carry Packets",
        "",
        "Each row below holds one carry channel `s = v2(3n+1)`.  The two residual columns compare the global affine model with a carry-conditioned affine model using the same fitted `A,B`.",
        "",
        "| s | samples | sources hit | sliced A,B | image | global energy | same-base energy | sliced energy | sliced reduction | top sliced deltas |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in carry_rows:
        top_delta_text = ", ".join(
            f"{delta}:{probability:.4f}"
            for delta, probability in row["top_affine_deltas"]
        )
        lines.append(
            f"| {row['carry']} | {row['samples']} | {row['sources_hit']} | "
            f"{row['sliced_multiplier']},{row['sliced_offset']} | "
            f"{row['sliced_image_size']} | "
            f"{row['global_residual_energy']:.6f} | "
            f"{row['carry_conditioned_residual_energy']:.6f} | "
            f"{row['carry_sliced_residual_energy']:.6f} | "
            f"{100.0 * row['sliced_reduction_fraction']:.2f}% | `{top_delta_text}` |"
        )

    lines += [
        "",
        "Global carry-depth distribution:",
        "",
    ]
    for carry, count in summary["carry_distribution"].items():
        lines.append(f"- `s={carry}`: `{count}`")

    lines += [
        "",
        "## Exact Carry-Lift Formula",
        "",
        "For `n = x + kQ` and `s = v2(3n+1)`, the exact lifted linearization is",
        "",
        "```text",
        "target = ((3 * (x + kQ) + 1) / 2^s) mod Q",
        "```",
        "",
        "At fixed `x` and `s`, the target is determined by the hidden residue `k mod 2^s`.  The table shows source-only ambiguity before retaining that coordinate, and deterministic lift cells after retaining it.",
        "",
        "| s | samples | sources hit | source edges | mean source outdegree | max source outdegree | lift bits | full cycle sampled | lift cells | deterministic cells | max cell outdegree | formula failures |",
        "|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|",
    ]
    for row in carry_lift_rows:
        lines.append(
            f"| {row['carry']} | {row['samples']} | {row['sources_hit']} | "
            f"{row['source_target_edges']} | "
            f"{row['mean_source_outdegree']:.6f} | "
            f"{row['max_source_outdegree']} | "
            f"{row['lift_bits_required']} | "
            f"{row['complete_lift_cycle_sampled']} | "
            f"{row['lift_cells']} | "
            f"{row['deterministic_lift_cells']} | "
            f"{row['max_lift_cell_outdegree']} | "
            f"{row['formula_failures']} |"
        )

    lines += [
        "",
        "## Largest Signed Residual Edges",
        "",
        "Positive residual means the true sampled kernel puts more mass on the edge than the fitted global affine skeleton predicts; negative means the skeleton predicts mass that the sampled kernel does not use at that source.",
        "",
        "| source | target | true | model | residual | true carry mix |",
        "|---|---|---:|---:|---:|---|",
    ]
    for edge in residual_edges:
        source = residue_label(int(edge["source"]), kernel.two_bits, kernel.three_pow)
        target = residue_label(int(edge["target"]), kernel.two_bits, kernel.three_pow)
        carry_mix = ", ".join(
            f"{carry}:{probability:.3f}"
            for carry, probability in edge["carry_mix"].items()
        )
        lines.append(
            f"| `{source}` | `{target}` | "
            f"{edge['true_probability']:.6f} | "
            f"{edge['model_probability']:.6f} | "
            f"{edge['residual']:.6f} | "
            f"`{carry_mix or '-'}` |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The affine skeleton gives a quotient-linear explanation of the sampled odd map only after we choose what information it is allowed to see.  A source-blind marginal is a strong null model at this coarse quotient; the meaningful test is whether resolving carry packets lets low-complexity affine pieces outperform that null.  If the carry-sliced row lowers Fisher energy, the nonlinear part is being carried by discrete 2-adic depth rather than by featureless noise.  If it does not, this quotient is still too coarse or the affine family is too weak.",
        "",
        "The exact carry-lift audit is the reverse-engineering payload: source-only quotient rows are many-valued, but after adjoining `k mod 2^s` every sampled lift cell is deterministic and the divided affine formula has no failures.  That identifies the missing coordinate rather than merely measuring residual size.",
        "",
        "In the manuscript vocabulary, this is the Collatz analogue of isolating a mixed tame/wild obstruction: the visible affine numerator is the tame-looking part, and the variable 2-adic carry is the wild depth packet that survives linearization.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        f"python empirical/collatz_curvature_linearization.py --two-bits {kernel.two_bits} --three-pow {kernel.three_pow} --lift-bits {kernel.lift_bits}",
        "```",
        "",
    ]
    return "\n".join(lines)


def default_report_path(two_bits: int, three_pow: int, lift_bits: int) -> Path:
    return Path("empirical/reports") / (
        f"collatz_curvature_linearization_2p{two_bits}_3p{three_pow}_l{lift_bits}.md"
    )


def default_json_path(two_bits: int, three_pow: int, lift_bits: int) -> Path:
    return Path("empirical/reports") / (
        f"collatz_curvature_linearization_2p{two_bits}_3p{three_pow}_l{lift_bits}.json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--two-bits", type=int, default=4)
    parser.add_argument("--three-pow", type=int, default=1)
    parser.add_argument("--lift-bits", type=int, default=10)
    parser.add_argument("--allow-zero-multiplier", action="store_true")
    parser.add_argument("--min-affine-image-size", type=int, default=0)
    parser.add_argument("--top-residuals", type=int, default=16)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    if args.two_bits < 1:
        raise ValueError("--two-bits must be at least 1")
    if args.three_pow < 1:
        raise ValueError("--three-pow must be at least 1")
    if args.lift_bits < 1:
        raise ValueError("--lift-bits must be at least 1")

    kernel = build_kernel(args.two_bits, args.three_pow, args.lift_bits)
    summary = kernel_summary(kernel)

    null_model = build_affine_model(kernel, "source-blind null", 0, 0)
    seed_model = build_affine_model(kernel, "seed affine 3n+1", 3 % kernel.modulus, 1)
    min_image_size = args.min_affine_image_size or max(2, len(kernel.sources) // 2)
    best_model = fit_best_affine_model(
        kernel,
        allow_zero_multiplier=args.allow_zero_multiplier,
        min_image_size=min_image_size,
    )
    q_by_carry = carry_delta_distributions(
        kernel,
        best_model.multiplier,
        best_model.offset,
    )
    carry_metrics = evaluate_model(
        kernel,
        "same-base carry-conditioned affine",
        best_model.multiplier,
        best_model.offset,
        lambda source: carry_aware_row(
            kernel,
            best_model.multiplier,
            best_model.offset,
            q_by_carry,
            source,
        ),
    )
    sliced_models = fit_carry_sliced_models(kernel)
    carry_sliced_metrics = evaluate_model(
        kernel,
        "carry-sliced affine",
        -1,
        -1,
        lambda source: carry_sliced_row(kernel, sliced_models, source),
    )
    oracle_metrics = exact_carry_lift_metrics(kernel)
    carry_lift_rows = carry_lift_formula_audit(kernel)
    carry_rows = carry_residual_rows(
        kernel,
        best_model.multiplier,
        best_model.offset,
        best_model.delta_distribution,
        q_by_carry,
        sliced_models,
    )
    residual_edges = top_residual_edges(
        kernel,
        lambda source: affine_model_row(
            kernel,
            best_model.multiplier,
            best_model.offset,
            best_model.delta_distribution,
            source,
        ),
        args.top_residuals,
    )

    report_path = args.report or default_report_path(
        args.two_bits,
        args.three_pow,
        args.lift_bits,
    )
    json_path = args.json or default_json_path(
        args.two_bits,
        args.three_pow,
        args.lift_bits,
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(
        make_report(
            kernel,
            summary,
            null_model,
            seed_model,
            best_model,
            carry_metrics,
            carry_sliced_metrics,
            oracle_metrics,
            q_by_carry,
            carry_rows,
            carry_lift_rows,
            residual_edges,
        ),
        encoding="utf-8",
    )

    payload = {
        "settings": {
            "two_bits": args.two_bits,
            "three_pow": args.three_pow,
            "lift_bits": args.lift_bits,
            "min_affine_image_size": min_image_size,
        },
        "kernel_summary": summary,
        "seed_model": {
            "multiplier": seed_model.multiplier,
            "offset": seed_model.offset,
            "metrics": asdict(seed_model.metrics),
            "top_delta_distribution": top_distribution_entries(seed_model.delta_distribution, 24),
        },
        "source_blind_null_model": {
            "multiplier": null_model.multiplier,
            "offset": null_model.offset,
            "metrics": asdict(null_model.metrics),
            "top_delta_distribution": top_distribution_entries(null_model.delta_distribution, 24),
        },
        "best_model": {
            "multiplier": best_model.multiplier,
            "offset": best_model.offset,
            "metrics": asdict(best_model.metrics),
            "top_delta_distribution": top_distribution_entries(best_model.delta_distribution, 24),
        },
        "carry_conditioned_model": {
            "multiplier": best_model.multiplier,
            "offset": best_model.offset,
            "metrics": asdict(carry_metrics),
        },
        "carry_sliced_model": {
            "metrics": asdict(carry_sliced_metrics),
            "per_carry_models": {
                carry: {
                    "multiplier": model.multiplier,
                    "offset": model.offset,
                    "metrics": asdict(model.metrics),
                    "top_delta_distribution": top_distribution_entries(model.delta_distribution, 24),
                }
                for carry, model in sorted(sliced_models.items())
            },
        },
        "exact_carry_lift_oracle": {
            "metrics": asdict(oracle_metrics),
            "formula_audit": carry_lift_rows,
        },
        "carry_residual_rows": carry_rows,
        "top_residual_edges": residual_edges,
    }
    json_path.write_text(json.dumps(rounded(payload), indent=2), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(json.dumps(rounded(asdict(best_model.metrics)), indent=2))
    print(json.dumps(rounded(asdict(carry_sliced_metrics)), indent=2))
    print(json.dumps(rounded(asdict(oracle_metrics)), indent=2))


if __name__ == "__main__":
    main()
