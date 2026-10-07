"""Conductor-closed optimizer prototype on F4[u]/(u^2) output labels.

The experiment is deliberately small and output-side only.  It asks whether
an optimizer that keeps its logit updates inside a declared conductor-closed
Fourier subalgebra can suppress carry leakage on a genuinely mixed 16-label
task.

Labels are the additive group of

    R = F4[u]/(u^2),   F4 = F2[w]/(w^2 + w + 1).

The synthetic target distributions are generated from natural parameters
whose Fourier support is the mixed closed subspace

    span_F2{1, u, w u}.

This support contains the full tame packet {u, wu, (w+1)u} and one wild
principal fiber {1 + b u : b in F4}.  The remaining eight nontrivial Fourier
modes are treated as carry-leakage modes.  Online one-hot labels create noisy
off-closure gradient pressure even though the population optimum is closed.

Compared optimizers:

* Adam in the full 16-label logit table.
* Plain categorical natural gradient in the full logit table.
* Conductor-closed optimizer: Adam-style moments fed by the conductor-projected
  gradient, with the actual update projected in the Walsh/Fourier character
  basis onto the mixed closed support before it is applied.

The main reported leakage is the fraction of nontrivial Fourier energy outside
the closed support, both for the final model and for the second-order
K^CH_p(s)s response of applied logit steps.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Literal

import numpy as np


Label = tuple[int, int]
MethodName = Literal["adam", "natural_gradient", "conductor_closed"]

F4_NAMES = {
    0: "0",
    1: "1",
    2: "w",
    3: "w+1",
}

ZERO: Label = (0, 0)
LABELS: tuple[Label, ...] = tuple((a, b) for a in range(4) for b in range(4))
LABEL_INDEX = {label: index for index, label in enumerate(LABELS)}
N_LABELS = len(LABELS)
UNIFORM = np.full(N_LABELS, 1.0 / N_LABELS)
EPS = 1e-12


def f4_add(left: int, right: int) -> int:
    """Add in F4 under the binary polynomial encoding."""

    return left ^ right


def add_label(left: Label, right: Label) -> Label:
    return (f4_add(left[0], right[0]), f4_add(left[1], right[1]))


def label_code(label: Label) -> int:
    """Pack a+b*u as four F2 bits."""

    return label[0] | (label[1] << 2)


def parity(value: int) -> int:
    return value.bit_count() & 1


def conductor(label: Label) -> str:
    if label == ZERO:
        return "1"
    if label[0] == 0:
        return "u"
    return "u^2"


def label_name(label: Label) -> str:
    lead, tail = label
    if label == ZERO:
        return "0"

    def tail_name(value: int) -> str:
        if value == 1:
            return "u"
        if value == 2:
            return "wu"
        return "(w+1)u"

    if tail == 0:
        return F4_NAMES[lead]
    if lead == 0:
        return tail_name(tail)
    return f"{F4_NAMES[lead]}+{tail_name(tail)}"


def span(generators: Iterable[Label]) -> tuple[Label, ...]:
    """F2-linear additive span of a finite set of labels."""

    items = tuple(generators)
    out: set[Label] = set()
    for mask in range(1 << len(items)):
        label = ZERO
        for index, generator in enumerate(items):
            if mask & (1 << index):
                label = add_label(label, generator)
        out.add(label)
    return tuple(sorted(out, key=lambda item: LABEL_INDEX[item]))


CLOSED_GENERATORS: tuple[Label, ...] = ((1, 0), (0, 1), (0, 2))
CLOSED_MODES: tuple[Label, ...] = tuple(label for label in span(CLOSED_GENERATORS) if label != ZERO)
CLOSED_MASK = np.zeros(N_LABELS, dtype=bool)
for _label in CLOSED_MODES:
    CLOSED_MASK[LABEL_INDEX[_label]] = True

NONTRIVIAL_MASK = np.ones(N_LABELS, dtype=bool)
NONTRIVIAL_MASK[LABEL_INDEX[ZERO]] = False
LEAKAGE_MASK = NONTRIVIAL_MASK & ~CLOSED_MASK


def character_matrix() -> np.ndarray:
    """Unitary real character table for the additive F2^4 label group."""

    table = np.empty((N_LABELS, N_LABELS), dtype=float)
    scale = 1.0 / math.sqrt(N_LABELS)
    for row, label in enumerate(LABELS):
        x = label_code(label)
        for col, mode in enumerate(LABELS):
            alpha = label_code(mode)
            table[row, col] = -scale if parity(x & alpha) else scale
    return table


CHAR = character_matrix()


def softmax(logits: np.ndarray) -> np.ndarray:
    centered = logits - np.max(logits, axis=-1, keepdims=True)
    exp = np.exp(centered)
    return exp / np.sum(exp, axis=-1, keepdims=True)


def center_rows(rows: np.ndarray) -> np.ndarray:
    return rows - np.mean(rows, axis=-1, keepdims=True)


def to_fourier(rows: np.ndarray) -> np.ndarray:
    return rows @ CHAR


def from_fourier(coefficients: np.ndarray) -> np.ndarray:
    return coefficients @ CHAR.T


def project_closed(rows: np.ndarray) -> np.ndarray:
    coefficients = to_fourier(center_rows(rows))
    projected = np.zeros_like(coefficients)
    projected[..., CLOSED_MASK] = coefficients[..., CLOSED_MASK]
    return center_rows(from_fourier(projected))


def mix_project_closed(rows: np.ndarray, fraction: float) -> np.ndarray:
    """Move rows fractionally toward the declared conductor-closed subspace."""

    if fraction <= 0.0:
        return center_rows(rows)
    if fraction >= 1.0:
        return project_closed(rows)
    centered = center_rows(rows)
    return center_rows((1.0 - fraction) * centered + fraction * project_closed(centered))


def split_energy(rows: np.ndarray) -> tuple[float, float]:
    """Return outside-closed and total nontrivial Fourier energy."""

    coefficients = to_fourier(center_rows(rows))
    outside = float(np.sum(coefficients[..., LEAKAGE_MASK] ** 2))
    total = float(np.sum(coefficients[..., NONTRIVIAL_MASK] ** 2))
    return outside, total


def leakage_ratio(rows: np.ndarray) -> float:
    outside, total = split_energy(rows)
    if total <= EPS:
        return 0.0
    return outside / total


def packet_energy_fractions(rows: np.ndarray) -> dict[str, float]:
    coefficients = to_fourier(center_rows(rows))
    raw: dict[str, float] = {}
    for packet in ("u", "u^2"):
        mask = np.array([conductor(label) == packet for label in LABELS], dtype=bool)
        raw[packet] = float(np.sum(coefficients[..., mask] ** 2))
    total = sum(raw.values())
    if total <= EPS:
        return {key: 0.0 for key in raw}
    return {key: value / total for key, value in raw.items()}


def log_loss(true_probs: np.ndarray, logits: np.ndarray) -> float:
    probs = np.maximum(softmax(logits), EPS)
    return float(-np.mean(np.sum(true_probs * np.log(probs), axis=1)))


def entropy(probs: np.ndarray) -> float:
    clipped = np.maximum(probs, EPS)
    return float(-np.mean(np.sum(clipped * np.log(clipped), axis=1)))


def rms_clip(rows: np.ndarray, max_rms: float) -> np.ndarray:
    rms = np.sqrt(np.mean(rows * rows, axis=1, keepdims=True))
    scale = np.minimum(1.0, max_rms / np.maximum(rms, EPS))
    return rows * scale


def logit_to_moment_step(probs: np.ndarray, logit_step: np.ndarray) -> np.ndarray:
    expectation = np.sum(probs * logit_step, axis=1, keepdims=True)
    return probs * (logit_step - expectation)


def k_ch_raise(probs: np.ndarray, moment_step: np.ndarray) -> np.ndarray:
    fisher_norm_sq = np.sum(moment_step * moment_step / np.maximum(probs, EPS), axis=1, keepdims=True)
    return center_rows(moment_step * moment_step / np.maximum(probs, EPS) - fisher_norm_sq * probs)


@dataclass(frozen=True)
class ExperimentConfig:
    contexts: int = 64
    steps: int = 2500
    batch_size: int = 128
    signal_scale: float = 2.4
    adam_lr: float = 0.08
    natural_lr: float = 0.003
    closed_lr: float = 0.08
    max_natural_rms: float = 4.0
    adam_beta1: float = 0.9
    adam_beta2: float = 0.999
    adam_eps: float = 1e-8
    closed_gradient_projection: float = 1.0
    closed_update_projection: float = 1.0


@dataclass(frozen=True)
class MethodResult:
    seed: int
    method: str
    gradient_projection: float
    update_projection: float
    final_true_ce: float
    final_true_kl: float
    final_logit_leakage: float
    final_probability_leakage: float
    cumulative_update_leakage: float
    cumulative_kch_carry_leakage: float
    final_closed_logit_energy: float
    final_leak_logit_energy: float


@dataclass(frozen=True)
class SeedResult:
    seed: int
    target_entropy: float
    target_logit_leakage: float
    target_probability_leakage: float
    target_packet_energy: dict[str, float]
    method_results: list[MethodResult]


@dataclass(frozen=True)
class SummaryRow:
    method: str
    gradient_projection: float
    update_projection: float
    final_true_kl_mean: float
    final_true_kl_std: float
    final_logit_leakage_mean: float
    final_logit_leakage_std: float
    final_probability_leakage_mean: float
    final_probability_leakage_std: float
    cumulative_update_leakage_mean: float
    cumulative_kch_carry_leakage_mean: float


@dataclass(frozen=True)
class ParetoRow:
    gradient_projection: float
    update_projection: float
    final_true_kl_mean: float
    final_true_kl_std: float
    final_probability_leakage_mean: float
    final_probability_leakage_std: float
    cumulative_update_leakage_mean: float
    cumulative_kch_carry_leakage_mean: float


def make_target(seed: int, config: ExperimentConfig) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    coefficients = np.zeros((config.contexts, N_LABELS), dtype=float)

    tame_modes = [LABEL_INDEX[label] for label in CLOSED_MODES if conductor(label) == "u"]
    wild_modes = [LABEL_INDEX[label] for label in CLOSED_MODES if conductor(label) == "u^2"]

    coefficients[:, tame_modes] = rng.normal(
        loc=0.0,
        scale=config.signal_scale,
        size=(config.contexts, len(tame_modes)),
    )
    coefficients[:, wild_modes] = rng.normal(
        loc=0.0,
        scale=0.85 * config.signal_scale,
        size=(config.contexts, len(wild_modes)),
    )

    # Force both packets to be visibly present in every context family.  This
    # keeps the task mixed even for unlucky small random seeds.
    coefficients[:, tame_modes[0]] += config.signal_scale * np.sin(
        np.linspace(0.0, 2.0 * math.pi, config.contexts, endpoint=False)
    )
    coefficients[:, wild_modes[0]] += 0.8 * config.signal_scale * np.cos(
        np.linspace(0.0, 4.0 * math.pi, config.contexts, endpoint=False)
    )

    logits = center_rows(from_fourier(coefficients))
    return logits, softmax(logits)


def sample_batches(
    seed: int,
    true_probs: np.ndarray,
    config: ExperimentConfig,
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed + 1_000_003)
    contexts = rng.integers(0, config.contexts, size=(config.steps, config.batch_size))
    uniforms = rng.random(size=(config.steps, config.batch_size))
    cdf = np.cumsum(true_probs[contexts], axis=-1)
    labels = np.sum(uniforms[..., None] > cdf, axis=-1)
    return contexts.astype(np.int32), labels.astype(np.int32)


def batch_counts(
    contexts: np.ndarray,
    labels: np.ndarray,
    n_contexts: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    counts = np.zeros((n_contexts, N_LABELS), dtype=float)
    np.add.at(counts, (contexts, labels), 1.0)
    totals = np.sum(counts, axis=1)
    active = totals > 0.0
    empirical = np.zeros_like(counts)
    empirical[active] = counts[active] / totals[active, None]
    return active, empirical, totals


def applied_step_leakage(
    probs: np.ndarray,
    logit_delta: np.ndarray,
) -> tuple[float, float, float, float]:
    update_outside, update_total = split_energy(logit_delta)
    moment_step = logit_to_moment_step(probs, logit_delta)
    kch = k_ch_raise(probs, moment_step)
    kch_outside, kch_total = split_energy(kch)
    return update_outside, update_total, kch_outside, kch_total


def run_method(
    method: MethodName,
    seed: int,
    true_probs: np.ndarray,
    target_entropy: float,
    batches: tuple[np.ndarray, np.ndarray],
    config: ExperimentConfig,
    *,
    gradient_projection: float | None = None,
    update_projection: float | None = None,
) -> MethodResult:
    logits = np.zeros((config.contexts, N_LABELS), dtype=float)
    first_moment = np.zeros_like(logits)
    second_moment = np.zeros_like(logits)
    update_leak_outside = 0.0
    update_leak_total = 0.0
    kch_leak_outside = 0.0
    kch_leak_total = 0.0
    batch_contexts, batch_labels = batches
    gradient_projection = (
        config.closed_gradient_projection if gradient_projection is None else gradient_projection
    )
    update_projection = (
        config.closed_update_projection if update_projection is None else update_projection
    )

    for step_index in range(config.steps):
        active, empirical, totals = batch_counts(
            batch_contexts[step_index],
            batch_labels[step_index],
            config.contexts,
        )
        if not np.any(active):
            continue

        active_logits = logits[active]
        active_probs = softmax(active_logits)

        if method in ("adam", "conductor_closed"):
            gradient = np.zeros_like(logits)
            weight = totals[active, None] / float(config.batch_size)
            gradient[active] = weight * (active_probs - empirical[active])
            if method == "conductor_closed":
                gradient[active] = mix_project_closed(gradient[active], gradient_projection)
            first_moment = config.adam_beta1 * first_moment + (1.0 - config.adam_beta1) * gradient
            second_moment = (
                config.adam_beta2 * second_moment
                + (1.0 - config.adam_beta2) * gradient * gradient
            )
            bias1 = 1.0 - config.adam_beta1 ** (step_index + 1)
            bias2 = 1.0 - config.adam_beta2 ** (step_index + 1)
            lr = config.closed_lr if method == "conductor_closed" else config.adam_lr
            update = -lr * (first_moment / bias1) / (
                np.sqrt(second_moment / bias2) + config.adam_eps
            )
            update = center_rows(update)
            if method == "conductor_closed":
                update[active] = mix_project_closed(update[active], update_projection)
            applied = update[active]
        else:
            direction = empirical[active] / np.maximum(active_probs, EPS)
            direction = rms_clip(center_rows(direction), config.max_natural_rms)
            lr = config.natural_lr
            applied = lr * direction
            update = np.zeros_like(logits)
            update[active] = applied

        outside, total, kch_outside, kch_total = applied_step_leakage(active_probs, applied)
        update_leak_outside += outside
        update_leak_total += total
        kch_leak_outside += kch_outside
        kch_leak_total += kch_total

        logits[active] = center_rows(logits[active] + applied)

    final_ce = log_loss(true_probs, logits)
    final_kl = final_ce - target_entropy
    leak_energy, total_energy = split_energy(logits)
    closed_energy = max(total_energy - leak_energy, 0.0)

    return MethodResult(
        seed=seed,
        method=method,
        gradient_projection=gradient_projection if method == "conductor_closed" else 0.0,
        update_projection=update_projection if method == "conductor_closed" else 0.0,
        final_true_ce=final_ce,
        final_true_kl=final_kl,
        final_logit_leakage=leakage_ratio(logits),
        final_probability_leakage=leakage_ratio(softmax(logits) - UNIFORM),
        cumulative_update_leakage=(
            update_leak_outside / update_leak_total if update_leak_total > EPS else 0.0
        ),
        cumulative_kch_carry_leakage=(
            kch_leak_outside / kch_leak_total if kch_leak_total > EPS else 0.0
        ),
        final_closed_logit_energy=closed_energy,
        final_leak_logit_energy=leak_energy,
    )


def run_seed(seed: int, config: ExperimentConfig) -> SeedResult:
    target_logits, true_probs = make_target(seed, config)
    target_entropy = entropy(true_probs)
    batches = sample_batches(seed, true_probs, config)
    method_results = [
        run_method(method, seed, true_probs, target_entropy, batches, config)
        for method in ("adam", "natural_gradient", "conductor_closed")
    ]
    return SeedResult(
        seed=seed,
        target_entropy=target_entropy,
        target_logit_leakage=leakage_ratio(target_logits),
        target_probability_leakage=leakage_ratio(true_probs - UNIFORM),
        target_packet_energy=packet_energy_fractions(target_logits),
        method_results=method_results,
    )


def summarize(seed_results: list[SeedResult]) -> list[SummaryRow]:
    rows: list[SummaryRow] = []
    for method in ("adam", "natural_gradient", "conductor_closed"):
        results = [
            result
            for seed_result in seed_results
            for result in seed_result.method_results
            if result.method == method
        ]

        def values(name: str) -> np.ndarray:
            return np.asarray([getattr(result, name) for result in results], dtype=float)

        kl = values("final_true_kl")
        logit_leak = values("final_logit_leakage")
        prob_leak = values("final_probability_leakage")
        update_leak = values("cumulative_update_leakage")
        kch_leak = values("cumulative_kch_carry_leakage")
        rows.append(
            SummaryRow(
                method=method,
                gradient_projection=float(results[0].gradient_projection) if results else 0.0,
                update_projection=float(results[0].update_projection) if results else 0.0,
                final_true_kl_mean=float(np.mean(kl)),
                final_true_kl_std=float(np.std(kl)),
                final_logit_leakage_mean=float(np.mean(logit_leak)),
                final_logit_leakage_std=float(np.std(logit_leak)),
                final_probability_leakage_mean=float(np.mean(prob_leak)),
                final_probability_leakage_std=float(np.std(prob_leak)),
                cumulative_update_leakage_mean=float(np.mean(update_leak)),
                cumulative_kch_carry_leakage_mean=float(np.mean(kch_leak)),
            )
        )
    return rows


def projection_grid_summary(results: list[MethodResult]) -> ParetoRow:
    if not results:
        raise ValueError("projection grid summary needs at least one result")

    def values(name: str) -> np.ndarray:
        return np.asarray([getattr(result, name) for result in results], dtype=float)

    kl = values("final_true_kl")
    prob_leak = values("final_probability_leakage")
    update_leak = values("cumulative_update_leakage")
    kch_leak = values("cumulative_kch_carry_leakage")
    return ParetoRow(
        gradient_projection=float(results[0].gradient_projection),
        update_projection=float(results[0].update_projection),
        final_true_kl_mean=float(np.mean(kl)),
        final_true_kl_std=float(np.std(kl)),
        final_probability_leakage_mean=float(np.mean(prob_leak)),
        final_probability_leakage_std=float(np.std(prob_leak)),
        cumulative_update_leakage_mean=float(np.mean(update_leak)),
        cumulative_kch_carry_leakage_mean=float(np.mean(kch_leak)),
    )


def run_projection_pareto(
    seeds: list[int],
    config: ExperimentConfig,
    fractions: list[float],
) -> tuple[list[ParetoRow], dict[str, float]]:
    by_fraction: dict[tuple[float, float], list[MethodResult]] = {
        (gradient_fraction, update_fraction): []
        for gradient_fraction in fractions
        for update_fraction in fractions
    }
    target_logit_leakages: list[float] = []
    target_probability_leakages: list[float] = []
    target_tame_fractions: list[float] = []
    target_wild_fractions: list[float] = []

    for seed in seeds:
        target_logits, true_probs = make_target(seed, config)
        target_entropy = entropy(true_probs)
        batches = sample_batches(seed, true_probs, config)
        packets = packet_energy_fractions(target_logits)
        target_logit_leakages.append(leakage_ratio(target_logits))
        target_probability_leakages.append(leakage_ratio(true_probs - UNIFORM))
        target_tame_fractions.append(packets["u"])
        target_wild_fractions.append(packets["u^2"])

        for gradient_fraction in fractions:
            for update_fraction in fractions:
                result = run_method(
                    "conductor_closed",
                    seed,
                    true_probs,
                    target_entropy,
                    batches,
                    config,
                    gradient_projection=gradient_fraction,
                    update_projection=update_fraction,
                )
                by_fraction[(gradient_fraction, update_fraction)].append(result)

    rows = [
        projection_grid_summary(results)
        for _key, results in sorted(by_fraction.items())
    ]
    target_summary = {
        "target_logit_leakage_mean": float(np.mean(target_logit_leakages)),
        "target_probability_leakage_mean": float(np.mean(target_probability_leakages)),
        "target_tame_energy_mean": float(np.mean(target_tame_fractions)),
        "target_wild_energy_mean": float(np.mean(target_wild_fractions)),
    }
    return rows, target_summary


def parse_fractions(text: str) -> list[float]:
    fractions = [float(part.strip()) for part in text.split(",") if part.strip()]
    if not fractions:
        raise ValueError("at least one projection fraction is required")
    for fraction in fractions:
        if fraction < 0.0 or fraction > 1.0:
            raise ValueError("projection fractions must lie in [0, 1]")
    return sorted(set(fractions))


def method_label(method: str) -> str:
    return {
        "adam": "Adam",
        "natural_gradient": "plain natural gradient",
        "conductor_closed": "conductor-closed optimizer",
    }[method]


def ratio_text(numerator: float, denominator: float) -> str:
    if numerator <= EPS:
        return "inf"
    return f"{denominator / numerator:.1f}x"


def markdown_report(
    seed_results: list[SeedResult],
    summary: list[SummaryRow],
    config: ExperimentConfig,
    json_path: Path,
) -> str:
    target_tame = float(np.mean([row.target_packet_energy["u"] for row in seed_results]))
    target_wild = float(np.mean([row.target_packet_energy["u^2"] for row in seed_results]))
    target_logit_leak = float(np.mean([row.target_logit_leakage for row in seed_results]))
    target_prob_leak = float(np.mean([row.target_probability_leakage for row in seed_results]))
    closed = next(row for row in summary if row.method == "conductor_closed")
    adam = next(row for row in summary if row.method == "adam")
    nat = next(row for row in summary if row.method == "natural_gradient")

    lines = [
        "# Conductor-Closed Optimizer Prototype",
        "",
        "## Verdict",
        "",
        "On this synthetic mixed-output task, the conductor-closed optimizer keeps",
        "the learned logits and the applied K^CH carry response inside the declared",
        "mixed conductor closure up to floating-point noise.  Adam and plain natural",
        "gradient both leak substantial energy into the eight off-closure character",
        "modes created by online one-hot sampling noise.",
        "",
        f"- final probability leakage reduction vs Adam: `{ratio_text(closed.final_probability_leakage_mean, adam.final_probability_leakage_mean)}`",
        f"- final probability leakage reduction vs plain natural gradient: `{ratio_text(closed.final_probability_leakage_mean, nat.final_probability_leakage_mean)}`",
        f"- K^CH carry-response leakage reduction vs Adam: `{ratio_text(closed.cumulative_kch_carry_leakage_mean, adam.cumulative_kch_carry_leakage_mean)}`",
        f"- K^CH carry-response leakage reduction vs plain natural gradient: `{ratio_text(closed.cumulative_kch_carry_leakage_mean, nat.cumulative_kch_carry_leakage_mean)}`",
        "",
        "## Algebra",
        "",
        "- label algebra: `F4[u]/(u^2)`, `F4 = F2[w]/(w^2+w+1)`",
        f"- output labels: `{N_LABELS}`",
        "- closed generators: "
        + ", ".join(f"`{label_name(label)}`" for label in CLOSED_GENERATORS),
        "- nontrivial closed modes: "
        + ", ".join(f"`{label_name(label)}`" for label in CLOSED_MODES),
        f"- closed nontrivial modes: `{int(np.sum(CLOSED_MASK))}`",
        f"- leakage nontrivial modes: `{int(np.sum(LEAKAGE_MASK))}`",
        "",
        "The target natural parameters use both conductor packets:",
        "",
        f"- mean target logit energy in conductor `u`: `{target_tame:.6f}`",
        f"- mean target logit energy in conductor `u^2`: `{target_wild:.6f}`",
        f"- target logit leakage: `{target_logit_leak:.3e}`",
        f"- target probability leakage: `{target_prob_leak:.3e}`",
        "",
        "## Setup",
        "",
        f"- seeds: `{len(seed_results)}`",
        f"- contexts: `{config.contexts}`",
        f"- online steps per seed: `{config.steps}`",
        f"- batch size: `{config.batch_size}`",
        f"- signal scale: `{config.signal_scale}`",
        f"- JSON payload: `{json_path}`",
        "",
        "The model is a free 16-logit table per context.  Since the population",
        "target is conductor-closed, off-closure Fourier energy measures optimizer",
        "leakage rather than target complexity.  The stochastic labels are one-hot",
        "samples from the closed target distributions.",
        "",
        "## Summary",
        "",
        "| optimizer | true KL mean | true KL std | final logit leakage | final probability leakage | applied update leakage | K^CH carry leakage |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| {method_label(row.method)} | "
            f"{row.final_true_kl_mean:.6f} | "
            f"{row.final_true_kl_std:.6f} | "
            f"{row.final_logit_leakage_mean:.6e} +/- {row.final_logit_leakage_std:.1e} | "
            f"{row.final_probability_leakage_mean:.6e} +/- {row.final_probability_leakage_std:.1e} | "
            f"{row.cumulative_update_leakage_mean:.6e} | "
            f"{row.cumulative_kch_carry_leakage_mean:.6e} |"
        )

    lines += [
        "",
        "## Per-Seed Results",
        "",
        "| seed | optimizer | true KL | final probability leakage | K^CH carry leakage |",
        "|---:|---|---:|---:|---:|",
    ]
    for seed_result in seed_results:
        for result in seed_result.method_results:
            lines.append(
                f"| {seed_result.seed} | {method_label(result.method)} | "
                f"{result.final_true_kl:.6f} | "
                f"{result.final_probability_leakage:.6e} | "
                f"{result.cumulative_kch_carry_leakage:.6e} |"
            )

    lines += [
        "",
        "## Interpretation",
        "",
        "This is a prototype, not yet a general optimizer package.  The positive",
        "result is that the conductor projection is doing real work on a mixed local",
        "row: it suppresses both final off-closure probability energy and the",
        "second-order K^CH carry response while remaining competitive on population",
        "KL in this finite-sample regime.",
        "",
        "The important control is that the target itself has essentially zero",
        "off-closure leakage while using both tame and wild packets.  Plain Adam",
        "and plain natural gradient therefore leak because of their update rule",
        "under stochastic labels, not because the task secretly requires those",
        "modes.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/conductor_closed_optimizer.py",
        "```",
        "",
    ]
    return "\n".join(lines)


def percent_text(value: float) -> str:
    return f"{100.0 * value:.0f}%"


def markdown_pareto_report(
    rows: list[ParetoRow],
    target_summary: dict[str, float],
    config: ExperimentConfig,
    json_path: Path,
) -> str:
    symmetric = [
        row
        for row in rows
        if abs(row.gradient_projection - row.update_projection) <= 1e-12
    ]
    symmetric = sorted(symmetric, key=lambda row: row.gradient_projection)
    full_closed = next(
        row
        for row in rows
        if abs(row.gradient_projection - 1.0) <= 1e-12
        and abs(row.update_projection - 1.0) <= 1e-12
    )
    no_projection = next(
        row
        for row in rows
        if abs(row.gradient_projection) <= 1e-12 and abs(row.update_projection) <= 1e-12
    )
    best_kl = min(rows, key=lambda row: row.final_true_kl_mean)
    best_nonzero_leak = min(
        (row for row in rows if row.cumulative_kch_carry_leakage_mean > EPS),
        key=lambda row: row.final_true_kl_mean,
        default=best_kl,
    )

    lines = [
        "# Projection-Strength Pareto Sweep",
        "",
        "## Verdict",
        "",
        "The conductor tax curve is sharp on this synthetic F4[u]/(u^2) row.",
        "Fractional projection reduces leakage smoothly, and the sweep separates",
        "the useful closure mechanism from unnecessary projection strength.  In",
        "this run, the best KL setting is reported below rather than assumed.",
        "",
        f"- no projection KL / K^CH leakage: `{no_projection.final_true_kl_mean:.6f}` / `{no_projection.cumulative_kch_carry_leakage_mean:.6f}`",
        f"- full projection KL / K^CH leakage: `{full_closed.final_true_kl_mean:.6f}` / `{full_closed.cumulative_kch_carry_leakage_mean:.3e}`",
        f"- best KL setting: gradient `{percent_text(best_kl.gradient_projection)}`, update `{percent_text(best_kl.update_projection)}`, KL `{best_kl.final_true_kl_mean:.6f}`",
        f"- best nonzero-leak KL setting: gradient `{percent_text(best_nonzero_leak.gradient_projection)}`, update `{percent_text(best_nonzero_leak.update_projection)}`, K^CH leakage `{best_nonzero_leak.cumulative_kch_carry_leakage_mean:.6f}`",
        "",
        "## Target Control",
        "",
        f"- target logit leakage: `{target_summary['target_logit_leakage_mean']:.3e}`",
        f"- target probability leakage: `{target_summary['target_probability_leakage_mean']:.3e}`",
        f"- mean target conductor `u` energy: `{target_summary['target_tame_energy_mean']:.6f}`",
        f"- mean target conductor `u^2` energy: `{target_summary['target_wild_energy_mean']:.6f}`",
        "",
        "## Setup",
        "",
        f"- contexts: `{config.contexts}`",
        f"- online steps: `{config.steps}`",
        f"- batch size: `{config.batch_size}`",
        f"- closed Adam-style learning rate: `{config.closed_lr}`",
        f"- JSON payload: `{json_path}`",
        "",
        "Projection is applied fractionally as",
        "",
        "```text",
        "x <- (1-rho) x + rho P_closed x",
        "```",
        "",
        "separately for the stochastic gradient and the Adam-style update.  Logits",
        "are not hard-projected after partial steps, so the intermediate rows are",
        "real leakage/accuracy tradeoffs rather than hidden 100% projections.",
        "",
        "## Symmetric Tax Curve",
        "",
        "| projection | true KL mean | final probability leakage | applied update leakage | K^CH carry leakage |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in symmetric:
        lines.append(
            f"| {percent_text(row.gradient_projection)} | "
            f"{row.final_true_kl_mean:.6f} +/- {row.final_true_kl_std:.6f} | "
            f"{row.final_probability_leakage_mean:.6e} | "
            f"{row.cumulative_update_leakage_mean:.6e} | "
            f"{row.cumulative_kch_carry_leakage_mean:.6e} |"
        )

    lines += [
        "",
        "## Full Gradient/Update Grid",
        "",
        "| gradient projection | update projection | true KL mean | final probability leakage | K^CH carry leakage |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(rows, key=lambda item: (item.gradient_projection, item.update_projection)):
        lines.append(
            f"| {percent_text(row.gradient_projection)} | "
            f"{percent_text(row.update_projection)} | "
            f"{row.final_true_kl_mean:.6f} | "
            f"{row.final_probability_leakage_mean:.6e} | "
            f"{row.cumulative_kch_carry_leakage_mean:.6e} |"
        )

    lines += [
        "",
        "## Reading",
        "",
        "Both projection sites matter, but they do different engineering jobs.",
        "Update-side projection gives a direct monotone closure control even when",
        "the gradient is left noisy.  Gradient-side projection changes the internal",
        "Adam moments and can itself close this particular row when taken to 100%.",
        "The practical primitive suggested by the sweep is therefore not automatic",
        "'project everything'; it is a tunable conductor filter whose best setting",
        "should be selected against the KL/leakage Pareto curve.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/conductor_closed_optimizer.py --pareto-sweep",
        "```",
        "",
    ]
    return "\n".join(lines)


def json_ready(value: object) -> object:
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
        return round(value, 12)
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=6)
    parser.add_argument("--seed-start", type=int, default=3107)
    parser.add_argument("--contexts", type=int, default=ExperimentConfig.contexts)
    parser.add_argument("--steps", type=int, default=ExperimentConfig.steps)
    parser.add_argument("--batch-size", type=int, default=ExperimentConfig.batch_size)
    parser.add_argument("--signal-scale", type=float, default=ExperimentConfig.signal_scale)
    parser.add_argument("--adam-lr", type=float, default=ExperimentConfig.adam_lr)
    parser.add_argument("--natural-lr", type=float, default=ExperimentConfig.natural_lr)
    parser.add_argument("--closed-lr", type=float, default=ExperimentConfig.closed_lr)
    parser.add_argument("--max-natural-rms", type=float, default=ExperimentConfig.max_natural_rms)
    parser.add_argument("--closed-gradient-projection", type=float, default=ExperimentConfig.closed_gradient_projection)
    parser.add_argument("--closed-update-projection", type=float, default=ExperimentConfig.closed_update_projection)
    parser.add_argument("--pareto-sweep", action="store_true")
    parser.add_argument("--projection-fractions", default="0,0.25,0.5,0.75,1.0")
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = ExperimentConfig(
        contexts=args.contexts,
        steps=args.steps,
        batch_size=args.batch_size,
        signal_scale=args.signal_scale,
        adam_lr=args.adam_lr,
        natural_lr=args.natural_lr,
        closed_lr=args.closed_lr,
        max_natural_rms=args.max_natural_rms,
        closed_gradient_projection=args.closed_gradient_projection,
        closed_update_projection=args.closed_update_projection,
    )
    seeds = [args.seed_start + index for index in range(args.seeds)]

    reports_dir = Path(__file__).resolve().parent / "reports"
    if args.pareto_sweep:
        fractions = parse_fractions(args.projection_fractions)
        pareto_rows, target_summary = run_projection_pareto(seeds, config, fractions)
        report_path = args.report or reports_dir / "conductor_projection_pareto_f4_u2.md"
        json_path = args.json or reports_dir / "conductor_projection_pareto_f4_u2.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "config": asdict(config),
            "projection_fractions": fractions,
            "closed_generators": [label_name(label) for label in CLOSED_GENERATORS],
            "closed_modes": [label_name(label) for label in CLOSED_MODES],
            "target_summary": target_summary,
            "pareto_rows": [asdict(row) for row in pareto_rows],
        }
        json_path.write_text(json.dumps(json_ready(payload), indent=2), encoding="utf-8")
        report_path.write_text(
            markdown_pareto_report(pareto_rows, target_summary, config, json_path),
            encoding="utf-8",
        )
        print(f"Wrote {report_path}")
        print(f"Wrote {json_path}")
        print(
            json.dumps(
                json_ready(
                    {
                        f"g={row.gradient_projection:.2f},u={row.update_projection:.2f}": {
                            "final_true_kl_mean": row.final_true_kl_mean,
                            "final_probability_leakage_mean": row.final_probability_leakage_mean,
                            "cumulative_kch_carry_leakage_mean": row.cumulative_kch_carry_leakage_mean,
                        }
                        for row in pareto_rows
                    }
                ),
                indent=2,
            )
        )
        return

    seed_results = [run_seed(seed, config) for seed in seeds]
    summary = summarize(seed_results)

    report_path = args.report or reports_dir / "conductor_closed_optimizer_f4_u2.md"
    json_path = args.json or reports_dir / "conductor_closed_optimizer_f4_u2.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "config": asdict(config),
        "closed_generators": [label_name(label) for label in CLOSED_GENERATORS],
        "closed_modes": [label_name(label) for label in CLOSED_MODES],
        "leakage_modes": [label_name(label) for label in LABELS if LEAKAGE_MASK[LABEL_INDEX[label]]],
        "seed_results": [asdict(result) for result in seed_results],
        "summary": [asdict(row) for row in summary],
    }
    json_path.write_text(json.dumps(json_ready(payload), indent=2), encoding="utf-8")
    report_path.write_text(markdown_report(seed_results, summary, config, json_path), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(
        json.dumps(
            json_ready(
                {
                    row.method: {
                        "final_true_kl_mean": row.final_true_kl_mean,
                        "final_probability_leakage_mean": row.final_probability_leakage_mean,
                        "cumulative_kch_carry_leakage_mean": row.cumulative_kch_carry_leakage_mean,
                    }
                    for row in summary
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
