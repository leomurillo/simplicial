"""Direct learned B4 normalizer-transfer experiment on F4[u]/(u^2).

B4 says to buy the B3 symmetry premium exactly when expected transfer gain
exceeds the resource-weighted premium.  The earlier transfer audit was exact
support scoring.  This script turns the same decision into a learned update
experiment:

* sample a source reciprocal support S in F4[u]/(u^2);
* choose held-out normalizer transforms gamma.S;
* generate target categorical distributions from the transformed support;
* train free context-logit tables from samples while constraining Adam updates
  to a source-declared support policy;
* compare measured held-out target KL against resource cost.

This is still a synthetic structured-output experiment, not evidence about a
general neural loss landscape.  Its job is narrower: test whether the B4
premium/gain rule survives stochastic learned updates in the first local row
where B2 and B3 differ.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Hashable, Mapping

import numpy as np


sys.path.insert(0, str(Path(__file__).resolve().parent))

from conductor_closed_optimizer import (  # noqa: E402
    CHAR,
    EPS,
    LABELS,
    LABEL_INDEX,
    N_LABELS,
    UNIFORM,
    center_rows,
    entropy,
    from_fourier,
    k_ch_raise,
    label_name,
    log_loss,
    logit_to_moment_step,
    softmax,
    to_fourier,
)
from information_investment_functional import (  # noqa: E402
    FiniteRow,
    build_rows,
    conductor_packet_support,
    generated_subgroup,
    normalizer_saturation,
    resource_cost,
)


Mode = Hashable
DEFAULT_REPORT = Path("empirical/reports/learned_normalizer_transfer_f4_u2.md")
DEFAULT_JSON = Path("empirical/reports/learned_normalizer_transfer_f4_u2.json")


@dataclass(frozen=True)
class ExperimentConfig:
    source_tasks: int = 8
    transfers_per_source: int = 4
    contexts: int = 32
    steps: int = 800
    batch_size: int = 96
    signal_scale: float = 2.0
    lr: float = 0.08
    beta1: float = 0.9
    beta2: float = 0.999
    adam_eps: float = 1e-8
    gradient_projection: float = 0.0
    update_projection: float = 1.0
    resource_weight: float = 0.25
    max_source_size: int = 2
    nontrivial_transfers_only: bool = True
    seed: int = 20260514


@dataclass(frozen=True)
class PolicyResult:
    policy: str
    support_size: int
    resource_cost: float
    target_support_coverage: float
    target_logit_projection_leakage: float
    final_true_kl: float
    final_policy_probability_leakage: float
    cumulative_update_leakage: float
    cumulative_kch_carry_leakage: float
    measured_J: float


def row() -> FiniteRow:
    return build_rows(["f4-u2"])[0]


def mode_index(mode: Mode) -> int:
    return LABEL_INDEX[mode]  # type: ignore[index]


def support_mask(support: set[Mode]) -> np.ndarray:
    mask = np.zeros(N_LABELS, dtype=bool)
    for mode in support:
        mask[mode_index(mode)] = True
    return mask


def nontrivial_mask() -> np.ndarray:
    mask = np.ones(N_LABELS, dtype=bool)
    mask[LABEL_INDEX[(0, 0)]] = False
    return mask


NONTRIVIAL_MASK = nontrivial_mask()


def project_support(rows: np.ndarray, mask: np.ndarray) -> np.ndarray:
    coeffs = to_fourier(center_rows(rows))
    projected = np.zeros_like(coeffs)
    projected[..., mask] = coeffs[..., mask]
    return center_rows(from_fourier(projected))


def mix_project_support(rows: np.ndarray, mask: np.ndarray, fraction: float) -> np.ndarray:
    if fraction <= 0.0:
        return center_rows(rows)
    if fraction >= 1.0:
        return project_support(rows, mask)
    centered = center_rows(rows)
    return center_rows((1.0 - fraction) * centered + fraction * project_support(centered, mask))


def split_energy(rows: np.ndarray, mask: np.ndarray) -> tuple[float, float]:
    coeffs = to_fourier(center_rows(rows))
    outside_mask = NONTRIVIAL_MASK & ~mask
    outside = float(np.sum(coeffs[..., outside_mask] ** 2))
    total = float(np.sum(coeffs[..., NONTRIVIAL_MASK] ** 2))
    return outside, total


def leakage_ratio(rows: np.ndarray, mask: np.ndarray) -> float:
    outside, total = split_energy(rows, mask)
    return 0.0 if total <= EPS else outside / total


def support_names(finite_row: FiniteRow, support: set[Mode], max_items: int = 10) -> list[str]:
    modes = sorted(support, key=finite_row.label_name)
    out = [finite_row.label_name(mode) for mode in modes[:max_items]]
    if len(modes) > max_items:
        out.append(f"...(+{len(modes) - max_items})")
    return out


def random_support(finite_row: FiniteRow, size: int, rng: random.Random) -> set[Mode]:
    nonzero = list(finite_row.nonzero_modes)
    if size >= len(nonzero):
        return set(nonzero)
    return set(rng.sample(nonzero, size))


def random_source_support(
    finite_row: FiniteRow,
    rng: random.Random,
    max_size: int,
) -> set[Mode]:
    nonzero = list(finite_row.nonzero_modes)
    for _ in range(10_000):
        size = rng.randint(1, min(max_size, len(nonzero)))
        support = set(rng.sample(nonzero, size))
        minimal = generated_subgroup(finite_row, support)
        saturated = normalizer_saturation(finite_row, support)
        if len(saturated) > len(minimal):
            return support
    raise RuntimeError("could not sample a source support with positive B3 premium")


def transform_support(
    finite_row: FiniteRow,
    support: set[Mode],
    action: Mapping[Mode, Mode],
) -> set[Mode]:
    return {action[mode] for mode in support if action[mode] != finite_row.zero}


def choose_transfer_action(
    finite_row: FiniteRow,
    source_support: set[Mode],
    rng: random.Random,
    nontrivial_only: bool,
) -> tuple[int, Mapping[Mode, Mode], set[Mode]]:
    source_minimal = generated_subgroup(finite_row, source_support)
    action_items = list(enumerate(finite_row.normalizer_actions))
    rng.shuffle(action_items)
    for index, action in action_items:
        target = transform_support(finite_row, source_support, action)
        if not nontrivial_only or not target <= source_minimal:
            return index, action, target
    index, action = action_items[0]
    return index, action, transform_support(finite_row, source_support, action)


def make_source_coefficients(
    finite_row: FiniteRow,
    source_support: set[Mode],
    rng: np.random.Generator,
    config: ExperimentConfig,
) -> np.ndarray:
    coeffs = np.zeros((config.contexts, N_LABELS), dtype=float)
    grid = np.linspace(0.0, 2.0 * math.pi, config.contexts, endpoint=False)
    for index, mode in enumerate(sorted(source_support, key=finite_row.label_name)):
        mode_col = mode_index(mode)
        phase = rng.uniform(0.0, 2.0 * math.pi)
        wave = np.sin((index + 1) * grid + phase)
        coeffs[:, mode_col] = (
            rng.normal(0.0, 0.45 * config.signal_scale, size=config.contexts)
            + config.signal_scale * wave
        )
    return coeffs


def transform_coefficients(
    finite_row: FiniteRow,
    coeffs: np.ndarray,
    action: Mapping[Mode, Mode],
) -> np.ndarray:
    out = np.zeros_like(coeffs)
    for mode in finite_row.modes:
        out[:, mode_index(action[mode])] = coeffs[:, mode_index(mode)]
    return out


def sample_batches(
    true_probs: np.ndarray,
    seed: int,
    config: ExperimentConfig,
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
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
    mask: np.ndarray,
) -> tuple[float, float, float, float]:
    update_outside, update_total = split_energy(logit_delta, mask)
    moment_step = logit_to_moment_step(probs, logit_delta)
    kch = k_ch_raise(probs, moment_step)
    kch_outside, kch_total = split_energy(kch, mask)
    return update_outside, update_total, kch_outside, kch_total


def support_coverage(target_support: set[Mode], policy_support: set[Mode]) -> float:
    if not target_support:
        return 1.0
    return len(target_support & policy_support) / len(target_support)


def train_policy(
    finite_row: FiniteRow,
    policy_name: str,
    policy_support: set[Mode],
    target_support: set[Mode],
    target_logits: np.ndarray,
    true_probs: np.ndarray,
    batches: tuple[np.ndarray, np.ndarray],
    config: ExperimentConfig,
) -> PolicyResult:
    mask = support_mask(policy_support)
    logits = np.zeros((config.contexts, N_LABELS), dtype=float)
    first_moment = np.zeros_like(logits)
    second_moment = np.zeros_like(logits)
    update_leak_outside = 0.0
    update_leak_total = 0.0
    kch_leak_outside = 0.0
    kch_leak_total = 0.0
    target_entropy = entropy(true_probs)
    batch_contexts, batch_labels = batches

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
        gradient = np.zeros_like(logits)
        weight = totals[active, None] / float(config.batch_size)
        gradient[active] = weight * (active_probs - empirical[active])
        if config.gradient_projection > 0.0:
            gradient[active] = mix_project_support(
                gradient[active],
                mask,
                config.gradient_projection,
            )

        first_moment = config.beta1 * first_moment + (1.0 - config.beta1) * gradient
        second_moment = config.beta2 * second_moment + (1.0 - config.beta2) * gradient * gradient
        bias1 = 1.0 - config.beta1 ** (step_index + 1)
        bias2 = 1.0 - config.beta2 ** (step_index + 1)
        update = -config.lr * (first_moment / bias1) / (
            np.sqrt(second_moment / bias2) + config.adam_eps
        )
        update = center_rows(update)
        if config.update_projection > 0.0:
            update[active] = mix_project_support(update[active], mask, config.update_projection)
        applied = update[active]

        outside, total, kch_outside, kch_total = applied_step_leakage(
            active_probs,
            applied,
            mask,
        )
        update_leak_outside += outside
        update_leak_total += total
        kch_leak_outside += kch_outside
        kch_leak_total += kch_total

        logits[active] = center_rows(logits[active] + applied)

    final_kl = log_loss(true_probs, logits) - target_entropy
    policy_prob_leakage = leakage_ratio(softmax(logits) - UNIFORM, mask)
    update_leakage = update_leak_outside / update_leak_total if update_leak_total > EPS else 0.0
    kch_leakage = kch_leak_outside / kch_leak_total if kch_leak_total > EPS else 0.0
    target_projection_leakage = leakage_ratio(target_logits, mask)
    resource = resource_cost(finite_row, policy_support)
    return PolicyResult(
        policy=policy_name,
        support_size=len(policy_support),
        resource_cost=resource,
        target_support_coverage=support_coverage(target_support, policy_support),
        target_logit_projection_leakage=target_projection_leakage,
        final_true_kl=final_kl,
        final_policy_probability_leakage=policy_prob_leakage,
        cumulative_update_leakage=update_leakage,
        cumulative_kch_carry_leakage=kch_leakage,
        measured_J=final_kl + config.resource_weight * resource,
    )


def policy_map(
    finite_row: FiniteRow,
    source_support: set[Mode],
    target_support: set[Mode],
    rng: random.Random,
) -> dict[str, set[Mode]]:
    source_minimal = generated_subgroup(finite_row, source_support)
    source_normalizer = normalizer_saturation(finite_row, source_support)
    return {
        "source_raw": set(source_support),
        "source_minimal_b2": source_minimal,
        "source_normalizer_b3": source_normalizer,
        "source_conductor_packet": conductor_packet_support(finite_row, source_support),
        "oracle_target_b2": generated_subgroup(finite_row, target_support),
        "random_minimal_budget": random_support(finite_row, len(source_minimal), rng),
        "random_normalizer_budget": random_support(finite_row, len(source_normalizer), rng),
        "full": set(finite_row.nonzero_modes),
    }


def run_experiment(config: ExperimentConfig) -> dict[str, Any]:
    finite_row = row()
    py_rng = random.Random(config.seed)
    np_seed = np.random.SeedSequence(config.seed)
    child_seeds = iter(np_seed.spawn(config.source_tasks * config.transfers_per_source + 1))
    records: list[dict[str, Any]] = []
    b4_records: list[dict[str, float]] = []
    examples: list[dict[str, Any]] = []
    wins: dict[str, int] = defaultdict(int)

    for source_index in range(config.source_tasks):
        source_support = random_source_support(finite_row, py_rng, config.max_source_size)
        source_minimal = generated_subgroup(finite_row, source_support)
        source_normalizer = normalizer_saturation(finite_row, source_support)
        source_np_rng = np.random.default_rng(next(child_seeds))
        source_coeffs = make_source_coefficients(
            finite_row,
            source_support,
            source_np_rng,
            config,
        )

        for transfer_index in range(config.transfers_per_source):
            action_index, action, target_support = choose_transfer_action(
                finite_row,
                source_support,
                py_rng,
                config.nontrivial_transfers_only,
            )
            target_coeffs = transform_coefficients(finite_row, source_coeffs, action)
            target_logits = center_rows(from_fourier(target_coeffs))
            true_probs = softmax(target_logits)
            transfer_seed = config.seed + 10_000 * source_index + transfer_index
            batches = sample_batches(true_probs, transfer_seed, config)
            policies = policy_map(finite_row, source_support, target_support, py_rng)
            result_by_policy: dict[str, PolicyResult] = {}

            for name, support in policies.items():
                result_by_policy[name] = train_policy(
                    finite_row,
                    name,
                    support,
                    target_support,
                    target_logits,
                    true_probs,
                    batches,
                    config,
                )

            winner = min(result_by_policy.values(), key=lambda result: (result.measured_J, result.policy))
            wins[winner.policy] += 1

            minimal = result_by_policy["source_minimal_b2"]
            normalizer = result_by_policy["source_normalizer_b3"]
            premium = config.resource_weight * (
                normalizer.resource_cost - minimal.resource_cost
            )
            resource_delta = normalizer.resource_cost - minimal.resource_cost
            measured_gain = minimal.final_true_kl - normalizer.final_true_kl
            net_gain = measured_gain - premium
            b4_records.append(
                {
                    "resource_delta": resource_delta,
                    "premium": premium,
                    "measured_transfer_gain": measured_gain,
                    "measured_net_gain": net_gain,
                    "b3_beats_b2_by_measured_J": 1.0
                    if normalizer.measured_J + 1e-12 < minimal.measured_J
                    else 0.0,
                    "target_coverage_gain": (
                        normalizer.target_support_coverage - minimal.target_support_coverage
                    ),
                }
            )

            record = {
                "source_index": source_index,
                "transfer_index": transfer_index,
                "action_index": action_index,
                "source_support": support_names(finite_row, source_support),
                "target_support": support_names(finite_row, target_support),
                "source_minimal_size": len(source_minimal),
                "source_normalizer_size": len(source_normalizer),
                "winner_by_measured_J": winner.policy,
                "premium": premium,
                "measured_transfer_gain": measured_gain,
                "measured_net_gain": net_gain,
                "policies": {
                    name: asdict(result)
                    for name, result in sorted(result_by_policy.items())
                },
            }
            records.append(record)
            if len(examples) < 6 and (
                net_gain > 0.0 or normalizer.target_support_coverage > minimal.target_support_coverage
            ):
                examples.append(record)

    policy_summaries = summarize_policies(records, wins)
    b4_summary = summarize_b4(b4_records)
    return {
        "purpose": (
            "Direct learned B4 normalizer-transfer experiment on F4[u]/(u^2): "
            "train constrained logit tables on held-out normalizer-transformed "
            "targets and compare measured transfer gain with the symmetry premium."
        ),
        "config": asdict(config),
        "row": finite_row.name,
        "label_count": len(finite_row.labels),
        "nonzero_modes": len(finite_row.nonzero_modes),
        "policy_summaries": policy_summaries,
        "b4_summary": b4_summary,
        "examples": examples,
        "records": records,
    }


def summarize_policies(records: list[dict[str, Any]], wins: Mapping[str, int]) -> dict[str, Any]:
    by_policy: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for record in records:
        for name, result in record["policies"].items():
            by_policy[name].append(result)

    summaries: dict[str, Any] = {}
    for name, items in by_policy.items():
        summaries[name] = {
            "count": len(items),
            "wins_by_measured_J": wins.get(name, 0),
            "mean_support_size": mean(item["support_size"] for item in items),
            "mean_resource_cost": mean(item["resource_cost"] for item in items),
            "mean_target_support_coverage": mean(
                item["target_support_coverage"] for item in items
            ),
            "mean_target_logit_projection_leakage": mean(
                item["target_logit_projection_leakage"] for item in items
            ),
            "mean_final_true_kl": mean(item["final_true_kl"] for item in items),
            "mean_policy_probability_leakage": mean(
                item["final_policy_probability_leakage"] for item in items
            ),
            "mean_update_leakage": mean(item["cumulative_update_leakage"] for item in items),
            "mean_kch_carry_leakage": mean(
                item["cumulative_kch_carry_leakage"] for item in items
            ),
            "mean_measured_J": mean(item["measured_J"] for item in items),
        }
    return dict(sorted(summaries.items(), key=lambda item: (item[1]["mean_measured_J"], item[0])))


def summarize_b4(records: list[Mapping[str, float]]) -> dict[str, float]:
    mean_resource_delta = mean(record["resource_delta"] for record in records)
    mean_gain = mean(record["measured_transfer_gain"] for record in records)
    return {
        "count": float(len(records)),
        "mean_resource_delta": mean_resource_delta,
        "mean_premium": mean(record["premium"] for record in records),
        "mean_measured_transfer_gain": mean_gain,
        "mean_measured_net_gain": mean(record["measured_net_gain"] for record in records),
        "break_even_resource_weight": (
            mean_gain / mean_resource_delta if mean_resource_delta > EPS else 0.0
        ),
        "b3_beats_b2_by_measured_J_rate": mean(
            record["b3_beats_b2_by_measured_J"] for record in records
        ),
        "mean_target_coverage_gain": mean(record["target_coverage_gain"] for record in records),
    }


def mean(values: Any) -> float:
    items = list(values)
    return float(sum(float(item) for item in items) / len(items)) if items else 0.0


def fmt(value: float) -> str:
    if abs(value) >= 1000.0 or (abs(value) < 1e-4 and value != 0.0):
        return f"{value:.3e}"
    return f"{value:.6f}"


def method_label(policy: str) -> str:
    return {
        "source_raw": "source raw",
        "source_minimal_b2": "source B2",
        "source_normalizer_b3": "source B3",
        "source_conductor_packet": "source conductor packet",
        "oracle_target_b2": "oracle target B2",
        "random_minimal_budget": "random B2 budget",
        "random_normalizer_budget": "random B3 budget",
        "full": "full",
    }.get(policy, policy)


def render_markdown(payload: Mapping[str, Any]) -> str:
    config = payload["config"]
    b4 = payload["b4_summary"]
    lines = [
        "# Learned B4 Normalizer-Transfer Experiment",
        "",
        "## Verdict",
        "",
        "This is a direct learned update test of the B4 premium rule on",
        "`F4[u]/(u^2)`.  Each held-out target is a normalizer transform of a",
        "source support.  Policies train from samples using the same stochastic",
        "Adam update loop, but their applied updates are projected into the",
        "source-declared support.",
        "",
        f"- transfer cases: `{int(b4['count'])}`",
        f"- mean measured transfer gain B3 over B2: `{fmt(b4['mean_measured_transfer_gain'])}`",
        f"- mean resource-weighted premium: `{fmt(b4['mean_premium'])}`",
        f"- mean measured net gain: `{fmt(b4['mean_measured_net_gain'])}`",
        f"- implied break-even resource weight: `{fmt(b4['break_even_resource_weight'])}`",
        f"- B3 beats B2 by measured J rate: `{b4['b3_beats_b2_by_measured_J_rate']:.3f}`",
        "",
        "## Setup",
        "",
        f"- row: `{payload['row']}`",
        f"- source tasks / transfers per source: `{config['source_tasks']}` / `{config['transfers_per_source']}`",
        f"- contexts: `{config['contexts']}`",
        f"- training steps: `{config['steps']}`",
        f"- batch size: `{config['batch_size']}`",
        f"- signal scale: `{config['signal_scale']}`",
        f"- learning rate: `{config['lr']}`",
        f"- resource weight: `{config['resource_weight']}`",
        f"- gradient/update projection: `{config['gradient_projection']}` / `{config['update_projection']}`",
        f"- nontrivial transfers only: `{config['nontrivial_transfers_only']}`",
        "",
        "Measured J is `final_true_kl + resource_weight * resource_cost`.",
        "The primary transfer gain is the measured KL improvement of source B3",
        "over source B2 on the held-out target.",
        "",
        "## Policy Summary",
        "",
        "| policy | wins | support | resource | target coverage | target proj leak | KL | policy leak | K^CH leak | measured J |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, summary in payload["policy_summaries"].items():
        lines.append(
            f"| {method_label(name)} | "
            f"{summary['wins_by_measured_J']} | "
            f"{fmt(summary['mean_support_size'])} | "
            f"{fmt(summary['mean_resource_cost'])} | "
            f"{fmt(summary['mean_target_support_coverage'])} | "
            f"{fmt(summary['mean_target_logit_projection_leakage'])} | "
            f"{fmt(summary['mean_final_true_kl'])} | "
            f"{fmt(summary['mean_policy_probability_leakage'])} | "
            f"{fmt(summary['mean_kch_carry_leakage'])} | "
            f"{fmt(summary['mean_measured_J'])} |"
        )

    lines += [
        "",
        "## Payoff Examples",
        "",
    ]
    for example in payload["examples"][:6]:
        lines.append(
            "- source `{source}` -> target `{target}`; B2/B3 sizes `{b2}`/`{b3}`; "
            "gain/premium/net `{gain}`/`{premium}`/`{net}`; winner `{winner}`".format(
                source=", ".join(example["source_support"]),
                target=", ".join(example["target_support"]),
                b2=example["source_minimal_size"],
                b3=example["source_normalizer_size"],
                gain=fmt(example["measured_transfer_gain"]),
                premium=fmt(example["premium"]),
                net=fmt(example["measured_net_gain"]),
                winner=method_label(example["winner_by_measured_J"]),
            )
        )

    lines += [
        "",
        "## Reading",
        "",
        "This is stronger than the earlier support-only B4 audit because the numbers",
        "come after stochastic training on target samples.  It is still scoped:",
        "the model is a free context-logit table, so the result tests support-policy",
        "investment under learned updates, not representation learning in a deep",
        "network.",
        "",
        "A positive result here means the next A0 test should introduce a shared",
        "parameterization or real checkpoint dynamics.  A negative result would",
        "say that the support-level premium/gain rule is not enough once learned",
        "updates and finite samples enter.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/learned_normalizer_transfer_experiment.py",
        "python empirical/learned_normalizer_transfer_experiment.py --check empirical/reports/learned_normalizer_transfer_f4_u2.json",
        "```",
        "",
    ]
    return "\n".join(lines)


def json_ready(value: Any) -> Any:
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
        return round(value, 12)
    if isinstance(value, np.floating):
        return json_ready(float(value))
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    if isinstance(value, tuple):
        return [json_ready(item) for item in value]
    return value


def write_json(payload: Mapping[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(json_ready(payload), indent=2) + "\n", encoding="utf-8")


def write_report(payload: Mapping[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(payload), encoding="utf-8")


def check_payload(payload: Mapping[str, Any], path: Path) -> None:
    recorded = json.loads(path.read_text(encoding="utf-8"))
    current = json_ready(payload)
    if recorded != current:
        raise AssertionError(f"payload differs from {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-tasks", type=int, default=ExperimentConfig.source_tasks)
    parser.add_argument("--transfers-per-source", type=int, default=ExperimentConfig.transfers_per_source)
    parser.add_argument("--contexts", type=int, default=ExperimentConfig.contexts)
    parser.add_argument("--steps", type=int, default=ExperimentConfig.steps)
    parser.add_argument("--batch-size", type=int, default=ExperimentConfig.batch_size)
    parser.add_argument("--signal-scale", type=float, default=ExperimentConfig.signal_scale)
    parser.add_argument("--lr", type=float, default=ExperimentConfig.lr)
    parser.add_argument("--gradient-projection", type=float, default=ExperimentConfig.gradient_projection)
    parser.add_argument("--update-projection", type=float, default=ExperimentConfig.update_projection)
    parser.add_argument("--resource-weight", type=float, default=ExperimentConfig.resource_weight)
    parser.add_argument("--max-source-size", type=int, default=ExperimentConfig.max_source_size)
    parser.add_argument("--allow-trivial-transfers", action="store_true")
    parser.add_argument("--seed", type=int, default=ExperimentConfig.seed)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--check", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = ExperimentConfig(
        source_tasks=args.source_tasks,
        transfers_per_source=args.transfers_per_source,
        contexts=args.contexts,
        steps=args.steps,
        batch_size=args.batch_size,
        signal_scale=args.signal_scale,
        lr=args.lr,
        gradient_projection=args.gradient_projection,
        update_projection=args.update_projection,
        resource_weight=args.resource_weight,
        max_source_size=args.max_source_size,
        nontrivial_transfers_only=not args.allow_trivial_transfers,
        seed=args.seed,
    )
    payload = run_experiment(config)
    if args.check is not None:
        check_payload(payload, args.check)
        print(f"checked {args.check}")
        return
    write_json(payload, args.json)
    write_report(payload, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")
    print(
        json.dumps(
            json_ready(
                {
                    "b4_summary": payload["b4_summary"],
                    "winner_order": list(payload["policy_summaries"].keys()),
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
