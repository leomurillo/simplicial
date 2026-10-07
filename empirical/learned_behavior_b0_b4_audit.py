"""Learned-behavior B0/B4 audit.

This audit moves the B0-B4 information-investment framework from exact finite
supports into two learned evidence channels:

1. behavior tables: saved per-class output distributions for weekdays/months;
2. update experiments: conductor-calendar transformer and F4[u]/(u^2)
   optimizer reports.

The exact-support theorem evidence stays separate.  Here we infer behavior-side
supports from learned tables or declared update filters, compute B2 subgroup
descent and B3 normalizer saturation, and then score candidates with J-style
projection, closure, balance, and resource terms where raw coefficients are
available.  For update-only JSON reports, the script records support closure
and reported leakage/accuracy deltas without pretending those summaries are raw
logit tables.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import struct
import sys
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Hashable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = Path(__file__).resolve().parent / "reports"
DEFAULT_JSON = REPORT_DIR / "learned_behavior_b0_b4_audit.json"
DEFAULT_REPORT = REPORT_DIR / "learned_behavior_b0_b4_audit.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))

from information_investment_functional import (  # noqa: E402
    FiniteRow,
    build_rows,
    conductor_packet_support,
    descent_balance_cost,
    generated_subgroup,
    normalizer_saturation,
    resource_cost,
    score_candidate,
)


Mode = Hashable

BEHAVIOR_TABLES = {
    "weekdays": {
        "row_key": "c7",
        "table": ROOT / "weekdays" / "baseline" / "per_class_output_dists.safetensors",
        "activation_report": REPORT_DIR / "activation_pullback_weekdays_llama31_8b.md",
    },
    "months": {
        "row_key": "c12",
        "table": ROOT / "months" / "baseline" / "per_class_output_dists.safetensors",
        "activation_report": REPORT_DIR / "activation_pullback_months_llama31_8b.md",
    },
}

CALENDAR_JSONS = (
    REPORT_DIR / "conductor_calendar_transformer_months.json",
    REPORT_DIR / "conductor_calendar_transformer_months_no_c2.json",
    REPORT_DIR / "conductor_calendar_transformer_months_c3_c4_c12.json",
    REPORT_DIR / "conductor_calendar_transformer_months_d64_offset_ood.json",
    REPORT_DIR / "conductor_calendar_transformer_months_d64_offset_ood_no_c2.json",
    REPORT_DIR / "conductor_calendar_transformer_months_d64_offset_ood_c6_c12.json",
    REPORT_DIR / "conductor_calendar_transformer_months_d64_offset_ood_full.json",
)

OPTIMIZER_JSON = REPORT_DIR / "conductor_closed_optimizer_f4_u2.json"
OPTIMIZER_PARETO_JSON = REPORT_DIR / "conductor_projection_pareto_f4_u2.json"

EPS = 1e-12


@dataclass(frozen=True)
class AggregateCoefficients:
    coefficients: dict[Mode, complex]
    energy_fraction: dict[Mode, float]
    total_nonzero_energy: float


def load_safetensors(path: Path) -> np.ndarray:
    """Load the single tensor stored in a safetensors file."""

    with path.open("rb") as handle:
        header_len = struct.unpack("<Q", handle.read(8))[0]
        header = json.loads(handle.read(header_len))
        data = handle.read()

    key = next(key for key in header if key != "__metadata__")
    meta = header[key]
    dtype_name = meta["dtype"]
    if dtype_name == "F32":
        dtype = np.float32
    elif dtype_name == "F64":
        dtype = np.float64
    elif dtype_name == "BF16":
        start, end = meta["data_offsets"]
        raw = np.frombuffer(data[start:end], dtype=np.uint16).copy()
        out = np.zeros(raw.size, dtype=np.uint32)
        out |= raw.astype(np.uint32) << 16
        return out.view(np.float32).reshape(meta["shape"])
    else:
        raise ValueError(f"unsupported safetensors dtype {dtype_name!r}")

    start, end = meta["data_offsets"]
    return np.frombuffer(data[start:end], dtype=dtype).reshape(meta["shape"]).copy()


def row_by_key(key: str) -> FiniteRow:
    return build_rows([key])[0]


def sorted_modes(row: FiniteRow, support: Iterable[Mode]) -> list[Mode]:
    return sorted(set(support), key=row.label_name)


def support_names(row: FiniteRow, support: Iterable[Mode], max_items: int | None = None) -> list[str]:
    modes = sorted_modes(row, support)
    if max_items is not None and len(modes) > max_items:
        shown = modes[:max_items]
        return [row.label_name(mode) for mode in shown] + [f"...(+{len(modes) - max_items})"]
    return [row.label_name(mode) for mode in modes]


def support_record(row: FiniteRow, support: set[Mode]) -> dict[str, Any]:
    descent = generated_subgroup(row, support)
    filtered = conductor_packet_support(row, support)
    normalizer = normalizer_saturation(row, support)
    return {
        "support_size": len(support),
        "resource_cost": resource_cost(row, support),
        "support": support_names(row, support),
        "b2_descent_size": len(descent),
        "b2_missing_count": len(descent - support),
        "b2_missing": support_names(row, descent - support),
        "b2_closed": support == descent,
        "full_filtered_size": len(filtered),
        "full_filtered_extra_count": len(filtered - support),
        "full_filtered_extra": support_names(row, filtered - support, max_items=12),
        "normalizer_size": len(normalizer),
        "normalizer_extra_count": len(normalizer - support),
        "normalizer_extra": support_names(row, normalizer - support, max_items=12),
    }


def cyclic_conductor(n: int, mode: int) -> int:
    mode %= n
    if mode == 0:
        return 1
    return n // math.gcd(n, mode)


def conductor_packets(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {}
    for mode in range(1, n):
        packets.setdefault(cyclic_conductor(n, mode), []).append(mode)
    return dict(sorted(packets.items()))


def support_from_cyclic_conductors(row: FiniteRow, conductors: Iterable[int]) -> set[Mode]:
    wanted = {int(conductor) for conductor in conductors}
    return {
        mode
        for mode in row.nonzero_modes
        if int(row.conductor(mode)) in wanted
    }


def aggregate_coefficients(row: FiniteRow, values: np.ndarray) -> AggregateCoefficients:
    """Aggregate per-row Fourier energy into one coefficient dictionary.

    The returned coefficient magnitudes are square roots of aggregate energy.
    This preserves projection-error and closure-weight ratios used by B0
    scoring while avoiding a phase convention for multiple behavior rows.
    """

    if values.ndim != 2 or values.shape[1] != len(row.labels):
        raise ValueError(
            f"expected a [contexts, {len(row.labels)}] table, got {values.shape}"
        )

    energy_by_mode: dict[Mode, float] = {}
    for mode in row.modes:
        chars = np.asarray(
            [row.character(mode, label) for label in row.labels],
            dtype=np.complex128,
        )
        coeffs = values @ chars
        energy_by_mode[mode] = float(np.sum(np.abs(coeffs) ** 2))

    total = sum(energy_by_mode[mode] for mode in row.nonzero_modes)
    fractions = {
        mode: (energy_by_mode[mode] / total if total > EPS else 0.0)
        for mode in row.modes
    }
    coefficients = {
        mode: complex(math.sqrt(max(energy_by_mode[mode], 0.0)), 0.0)
        for mode in row.modes
    }
    return AggregateCoefficients(
        coefficients=coefficients,
        energy_fraction=fractions,
        total_nonzero_energy=total,
    )


def infer_support(
    row: FiniteRow,
    fractions: Mapping[Mode, float],
    threshold: float,
) -> set[Mode]:
    support = {
        mode
        for mode in row.nonzero_modes
        if fractions.get(mode, 0.0) >= threshold
    }
    if support:
        return support
    best = max(row.nonzero_modes, key=lambda mode: fractions.get(mode, 0.0))
    return {best}


def score_policy_map(
    row: FiniteRow,
    h_hat: dict[Mode, complex],
    m_hat: dict[Mode, complex],
    policies: Mapping[str, set[Mode]],
    resource_weight: float,
) -> dict[str, Any]:
    scored = {}
    for name, support in policies.items():
        score = score_candidate(row, support, h_hat, m_hat, resource_weight)
        scored[name] = {
            **score,
            **support_record(row, support),
        }
    return dict(sorted(scored.items(), key=lambda item: (item[1]["J"], item[0])))


def transform_coefficients(
    row: FiniteRow,
    coefficients: Mapping[Mode, complex],
    action: Mapping[Mode, Mode],
) -> dict[Mode, complex]:
    transformed = {mode: 0.0j for mode in row.modes}
    for mode, value in coefficients.items():
        transformed[action[mode]] = value
    return transformed


def transform_support(row: FiniteRow, support: set[Mode], action: Mapping[Mode, Mode]) -> set[Mode]:
    return {action[mode] for mode in support if action[mode] != row.zero}


def structural_part(score: Mapping[str, float], resource_weight: float) -> float:
    return float(score["J"] - resource_weight * score["resource_cost"])


def transfer_estimate(
    row: FiniteRow,
    source_support: set[Mode],
    h_hat: dict[Mode, complex],
    m_hat: dict[Mode, complex],
    resource_weight: float,
) -> dict[str, Any]:
    source_minimal = generated_subgroup(row, source_support)
    source_normalizer = normalizer_saturation(row, source_support)
    records: list[dict[str, float]] = []

    for action in row.normalizer_actions:
        target_h = transform_coefficients(row, h_hat, action)
        target_m = transform_coefficients(row, m_hat, action)
        minimal_score = score_candidate(
            row,
            source_minimal,
            target_h,
            target_m,
            resource_weight,
        )
        normalizer_score = score_candidate(
            row,
            source_normalizer,
            target_h,
            target_m,
            resource_weight,
        )
        premium = resource_weight * (
            normalizer_score["resource_cost"] - minimal_score["resource_cost"]
        )
        structural_gain = structural_part(minimal_score, resource_weight) - structural_part(
            normalizer_score,
            resource_weight,
        )
        net_gain = minimal_score["J"] - normalizer_score["J"]
        records.append(
            {
                "premium": premium,
                "structural_gain": structural_gain,
                "net_gain": net_gain,
                "normalizer_beats_minimal": 1.0 if net_gain > 1e-12 else 0.0,
            }
        )

    if not records:
        return {
            "source_minimal_size": len(source_minimal),
            "source_normalizer_size": len(source_normalizer),
            "mean_premium": 0.0,
            "mean_structural_gain": 0.0,
            "mean_net_gain": 0.0,
            "normalizer_beats_minimal_rate": 0.0,
            "action_count": 0,
        }

    return {
        "source_minimal_size": len(source_minimal),
        "source_normalizer_size": len(source_normalizer),
        "mean_premium": mean([record["premium"] for record in records]),
        "mean_structural_gain": mean([record["structural_gain"] for record in records]),
        "mean_net_gain": mean([record["net_gain"] for record in records]),
        "normalizer_beats_minimal_rate": mean(
            [record["normalizer_beats_minimal"] for record in records]
        ),
        "action_count": len(records),
    }


def support_coefficients(row: FiniteRow, support: set[Mode]) -> dict[Mode, complex]:
    return {
        mode: (1.0 + 0.0j if mode in support else 0.0j)
        for mode in row.modes
    }


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return float(sum(items) / len(items)) if items else 0.0


def parse_activation_report(path: Path) -> dict[str, float] | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")

    def find(pattern: str) -> float | None:
        match = re.search(pattern, text)
        if not match:
            return None
        return float(match.group(1))

    values = {
        "between_class_fraction": find(r"between-class\s+\|\s+\*\*([0-9.]+)\*\*"),
        "within_class_fraction": find(r"within-class\s+\|\s+([0-9.]+)"),
        "activation_hellinger_r": find(
            r"activation distance vs Hellinger chord\s+\|\s+\*\*([0-9.]+)\*\*"
        ),
        "activation_cyclic_arc_r": find(
            r"activation distance vs cyclic Hellinger arc\s+\|\s+\*\*([0-9.]+)\*\*"
        ),
        "pullback_metric_cv": find(r"coefficient of variation\s+\|\s+\*\*([0-9.]+)\*\*"),
    }
    return {key: float(value) for key, value in values.items() if value is not None}


def behavior_table_audit(
    task: str,
    spec: Mapping[str, Any],
    probability_threshold: float,
    reciprocal_threshold: float,
    resource_weight: float,
) -> dict[str, Any]:
    row = row_by_key(str(spec["row_key"]))
    table_path = Path(spec["table"])
    probabilities = load_safetensors(table_path).astype(float)
    probabilities = probabilities / np.sum(probabilities, axis=1, keepdims=True)
    uniform = np.full_like(probabilities, 1.0 / probabilities.shape[1])
    tangent = probabilities - uniform
    reciprocal = 1.0 / np.maximum(probabilities, EPS)
    reciprocal = reciprocal - np.mean(reciprocal, axis=1, keepdims=True)

    probability_coeffs = aggregate_coefficients(row, tangent)
    reciprocal_coeffs = aggregate_coefficients(row, reciprocal)
    probability_support = infer_support(
        row,
        probability_coeffs.energy_fraction,
        probability_threshold,
    )
    reciprocal_support = infer_support(
        row,
        reciprocal_coeffs.energy_fraction,
        reciprocal_threshold,
    )
    b2 = generated_subgroup(row, reciprocal_support)
    b3 = normalizer_saturation(row, reciprocal_support)
    filtered = conductor_packet_support(row, reciprocal_support)
    policies = {
        "probability_active_support": probability_support,
        "reciprocal_active_support": reciprocal_support,
        "b2_minimal_descent": b2,
        "full_filtered_closure": filtered,
        "b3_normalizer_saturation": b3,
        "full": set(row.nonzero_modes),
    }
    scores = score_policy_map(
        row,
        probability_coeffs.coefficients,
        reciprocal_coeffs.coefficients,
        policies,
        resource_weight,
    )
    transfer = transfer_estimate(
        row,
        reciprocal_support,
        probability_coeffs.coefficients,
        reciprocal_coeffs.coefficients,
        resource_weight,
    )
    conductor_energy = {}
    for conductor in sorted({row.conductor(mode) for mode in row.nonzero_modes}, key=str):
        conductor_energy[str(conductor)] = sum(
            reciprocal_coeffs.energy_fraction[mode]
            for mode in row.nonzero_modes
            if row.conductor(mode) == conductor
        )

    return {
        "task": task,
        "source_kind": "learned_behavior_table",
        "row_key": row.key,
        "row": row.name,
        "path": str(table_path),
        "table_shape": list(probabilities.shape),
        "thresholds": {
            "probability_energy_fraction": probability_threshold,
            "reciprocal_energy_fraction": reciprocal_threshold,
        },
        "probability_active_support": support_names(row, probability_support),
        "reciprocal_active_support": support_names(row, reciprocal_support),
        "probability_active_size": len(probability_support),
        "reciprocal_active_size": len(reciprocal_support),
        "b2_minimal_size": len(b2),
        "b3_normalizer_size": len(b3),
        "full_filtered_size": len(filtered),
        "symmetry_premium_resource": resource_weight
        * (resource_cost(row, b3) - resource_cost(row, b2)),
        "reciprocal_conductor_energy_fraction": conductor_energy,
        "policy_scores": scores,
        "transfer_estimate": transfer,
        "activation_pullback_context": parse_activation_report(Path(spec["activation_report"])),
    }


def method_summary(payload: Mapping[str, Any], method: str) -> dict[str, float]:
    for row in payload.get("summary", []):
        if row.get("method") == method:
            return {key: float(value) for key, value in row.items() if isinstance(value, (int, float))}
    return {}


def calendar_audit(path: Path, resource_weight: float) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    config = payload["config"]
    row = row_by_key("c12")
    closed_conductors = tuple(int(item) for item in payload["closed_conductors"])
    declared = support_from_cyclic_conductors(row, closed_conductors)
    b2 = generated_subgroup(row, declared)
    b3 = normalizer_saturation(row, declared)
    filtered = conductor_packet_support(row, declared)
    adam = method_summary(payload, "adam")
    conductor = method_summary(payload, "conductor_update")
    declared_proxy = (
        conductor.get("logit_leakage_mean", 0.0)
        + conductor.get("update_leakage_mean", 0.0)
        + descent_balance_cost(row, declared)
        + resource_weight * resource_cost(row, declared)
    )

    return {
        "source_kind": "learned_update_summary",
        "path": str(path),
        "task": config["task"],
        "split_mode": config.get("split_mode", "random"),
        "d_model": config.get("d_model"),
        "closed_conductors": list(closed_conductors),
        "declared_support": support_record(row, declared),
        "b2_minimal_support": support_record(row, b2),
        "b3_normalizer_support": support_record(row, b3),
        "full_filtered_support": support_record(row, filtered),
        "symmetry_premium_resource": resource_weight
        * (resource_cost(row, b3) - resource_cost(row, b2)),
        "reported_deltas_conductor_minus_adam": {
            "test_accuracy": conductor.get("test_accuracy_mean", 0.0)
            - adam.get("test_accuracy_mean", 0.0),
            "generalization_gap": conductor.get("generalization_gap_mean", 0.0)
            - adam.get("generalization_gap_mean", 0.0),
            "final_logit_leakage": conductor.get("logit_leakage_mean", 0.0)
            - adam.get("logit_leakage_mean", 0.0),
            "output_update_leakage": conductor.get("update_leakage_mean", 0.0)
            - adam.get("update_leakage_mean", 0.0),
        },
        "declared_filter_J_proxy": declared_proxy,
        "reading": (
            "Leakage is measured relative to the declared update filter. "
            "B2 descent closure is reported separately and can be larger."
        ),
    }


def optimizer_audit(resource_weight: float) -> dict[str, Any]:
    row = row_by_key("f4-u2")
    payload = json.loads(OPTIMIZER_JSON.read_text(encoding="utf-8"))
    name_to_mode = {row.label_name(mode): mode for mode in row.nonzero_modes}
    declared = {name_to_mode[name] for name in payload["closed_modes"]}
    b2 = generated_subgroup(row, declared)
    b3 = normalizer_saturation(row, declared)
    filtered = conductor_packet_support(row, declared)
    h_hat = support_coefficients(row, declared)
    m_hat = support_coefficients(row, declared)
    transfer = transfer_estimate(row, declared, h_hat, m_hat, resource_weight)
    summary = {
        item["method"]: item
        for item in payload["summary"]
    }

    pareto = None
    if OPTIMIZER_PARETO_JSON.exists():
        pareto_payload = json.loads(OPTIMIZER_PARETO_JSON.read_text(encoding="utf-8"))
        rows = pareto_payload["pareto_rows"]
        best_kl = min(rows, key=lambda item: item["final_true_kl_mean"])
        best_zero_leak = min(
            rows,
            key=lambda item: (
                item["final_probability_leakage_mean"] > 1e-12,
                item["final_true_kl_mean"],
            ),
        )
        pareto = {
            "path": str(OPTIMIZER_PARETO_JSON),
            "best_kl": best_kl,
            "best_zero_probability_leakage": best_zero_leak,
        }

    return {
        "source_kind": "learned_optimizer_update_table",
        "path": str(OPTIMIZER_JSON),
        "row_key": row.key,
        "row": row.name,
        "declared_closed_support": support_record(row, declared),
        "b2_minimal_support": support_record(row, b2),
        "b3_normalizer_support": support_record(row, b3),
        "full_filtered_support": support_record(row, filtered),
        "symmetry_premium_resource": resource_weight
        * (resource_cost(row, b3) - resource_cost(row, b2)),
        "method_summary": summary,
        "transfer_estimate": transfer,
        "pareto_summary": pareto,
        "reading": (
            "The declared optimizer support is B2 closed, while full conductor "
            "filtering and B3 normalizer saturation both buy the remaining "
            "eight local modes."
        ),
    }


def fmt(value: float) -> str:
    if abs(value) >= 1000.0 or (abs(value) < 1e-4 and value != 0.0):
        return f"{value:.3e}"
    return f"{value:.6f}"


def render_markdown(payload: Mapping[str, Any]) -> str:
    lines = [
        "# Learned Behavior B0/B4 Audit",
        "",
        "## Verdict",
        "",
        "This report keeps exact-support theorems separate from learned evidence.",
        "Raw learned behavior tables are scored with B0-style projection, closure,",
        "balance, and resource terms.  Calendar and optimizer reports are treated",
        "as update-side summaries, so their declared filters are checked for B2",
        "closure without being upgraded into exact-support evidence.",
        "",
    ]

    behavior = payload["behavior_tables"]
    full_count = sum(
        1
        for item in behavior
        if item["b2_minimal_size"] == item["policy_scores"]["full"]["support_size"]
    )
    lines += [
        f"- behavior tables with full B2 closure: `{full_count}` / `{len(behavior)}`",
        "- cyclic learned behavior has zero B3 symmetry premium because B2 and B3 coincide;",
        "- C12 update filters often suppress declared leakage while underbuying B2 closure;",
        "- the F4[u]/(u^2) optimizer support is genuinely B2 closed, but B3 would buy the full local row for transfer.",
        "",
        "## Learned Behavior Tables",
        "",
        "| task | row | reciprocal active | B2 size | B3 size | filtered size | winner | premium | net transfer | pullback CV |",
        "|---|---|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for item in behavior:
        winner = next(iter(item["policy_scores"]))
        pullback = item.get("activation_pullback_context") or {}
        lines.append(
            f"| {item['task']} | {item['row']} | "
            f"{item['reciprocal_active_size']} | "
            f"{item['b2_minimal_size']} | "
            f"{item['b3_normalizer_size']} | "
            f"{item['full_filtered_size']} | "
            f"{winner} | "
            f"{fmt(item['symmetry_premium_resource'])} | "
            f"{fmt(item['transfer_estimate']['mean_net_gain'])} | "
            f"{fmt(pullback.get('pullback_metric_cv', 0.0))} |"
        )

    lines += [
        "",
        "The active support above is inferred from reciprocal-density Fourier energy",
        f"with threshold `{payload['config']['reciprocal_threshold']}`.  Probability",
        "support is also stored in the JSON, but B2 is computed from reciprocal",
        "support to match the B0 theorem.",
        "",
        "## Behavior Policy Scores",
        "",
    ]
    for item in behavior:
        lines += [
            f"### {item['task']} ({item['row']})",
            "",
            "| policy | J | Fisher | reciprocal | closure | balance | resource | support |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for name, score in item["policy_scores"].items():
            lines.append(
                f"| {name} | {fmt(score['J'])} | "
                f"{fmt(score['fisher_projection_error'])} | "
                f"{fmt(score['reciprocal_projection_error'])} | "
                f"{fmt(score['closure_leakage'])} | "
                f"{fmt(score['descent_balance_cost'])} | "
                f"{fmt(score['resource_cost'])} | "
                f"{score['support_size']} |"
            )
        lines.append("")

    lines += [
        "## Calendar Update Filters",
        "",
        "| report | split | conductors | declared | B2 | missing B2 | acc delta | gap delta | leakage delta | proxy J |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in payload["calendar_updates"]:
        report_name = Path(item["path"]).name.replace("conductor_calendar_transformer_", "")
        declared = item["declared_support"]
        deltas = item["reported_deltas_conductor_minus_adam"]
        lines.append(
            f"| {report_name} | {item['split_mode']} | "
            f"{','.join(str(x) for x in item['closed_conductors'])} | "
            f"{declared['support_size']} | "
            f"{declared['b2_descent_size']} | "
            f"{declared['b2_missing_count']} | "
            f"{fmt(deltas['test_accuracy'])} | "
            f"{fmt(deltas['generalization_gap'])} | "
            f"{fmt(deltas['final_logit_leakage'])} | "
            f"{fmt(item['declared_filter_J_proxy'])} |"
        )

    lines += [
        "",
        "`missing B2` is the count of subgroup-descent modes absent from the declared",
        "calendar filter.  A zero declared leakage number is therefore a filter",
        "invariant, not proof that the filter is B2 minimal.",
        "",
        "## Optimizer Update Audit",
        "",
    ]
    opt = payload["optimizer_update"]
    closed = opt["method_summary"]["conductor_closed"]
    adam = opt["method_summary"]["adam"]
    b2 = opt["b2_minimal_support"]
    b3 = opt["b3_normalizer_support"]
    transfer = opt["transfer_estimate"]
    lines += [
        f"- declared support: `{opt['declared_closed_support']['support_size']}` modes",
        f"- B2 minimal descent: `{b2['support_size']}` modes",
        f"- B3 normalizer saturation: `{b3['support_size']}` modes",
        f"- symmetry premium at resource weight `{payload['config']['resource_weight']}`: `{fmt(opt['symmetry_premium_resource'])}`",
        f"- conductor-closed KL vs Adam: `{fmt(closed['final_true_kl_mean'])}` vs `{fmt(adam['final_true_kl_mean'])}`",
        f"- conductor-closed probability leakage: `{fmt(closed['final_probability_leakage_mean'])}`",
        f"- support-transfer estimate gain/premium/net: `{fmt(transfer['mean_structural_gain'])}` / `{fmt(transfer['mean_premium'])}` / `{fmt(transfer['mean_net_gain'])}`",
        "",
    ]
    pareto = opt.get("pareto_summary")
    if pareto:
        best = pareto["best_kl"]
        lines += [
            "The projection Pareto report selects update-only full projection as the",
            "best KL setting in the saved sweep:",
            "",
            f"- gradient/update projection: `{100*best['gradient_projection']:.0f}%` / `{100*best['update_projection']:.0f}%`",
            f"- KL: `{fmt(best['final_true_kl_mean'])}`",
            f"- probability leakage: `{fmt(best['final_probability_leakage_mean'])}`",
            "",
        ]

    lines += [
        "## Reading",
        "",
        "B5 should be treated as an empirical audit/protocol, not a theorem.",
        "For learned behavior tables, the current weekday/month rows do not show a",
        "compression win: the inferred reciprocal support already forces full B2",
        "cyclic closure at the default threshold.  For update experiments, the",
        "evidence is real but narrower: conductor filters can reduce leakage, and",
        "the F4[u]/(u^2) optimizer shows a B2-closed update policy with strong",
        "fixed-task performance.  The support-level B4 transfer estimate in this",
        "report should be read alongside the direct learned normalizer-transfer",
        "experiment in `learned_normalizer_transfer_f4_u2.md`.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        "python empirical/learned_behavior_b0_b4_audit.py",
        "python empirical/learned_behavior_b0_b4_audit.py --check empirical/reports/learned_behavior_b0_b4_audit.json",
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


def build_payload(args: argparse.Namespace) -> dict[str, Any]:
    behavior = [
        behavior_table_audit(
            task,
            spec,
            args.probability_threshold,
            args.reciprocal_threshold,
            args.resource_weight,
        )
        for task, spec in BEHAVIOR_TABLES.items()
    ]
    calendar = [
        calendar_audit(path, args.resource_weight)
        for path in CALENDAR_JSONS
        if path.exists()
    ]
    return {
        "purpose": (
            "Learned-behavior B0/B4 audit: infer behavior/update supports, "
            "compute B2 descent and B3 normalizer saturation, and keep "
            "exact-support evidence separate from learned artifacts."
        ),
        "config": {
            "probability_threshold": args.probability_threshold,
            "reciprocal_threshold": args.reciprocal_threshold,
            "resource_weight": args.resource_weight,
        },
        "behavior_tables": behavior,
        "calendar_updates": calendar,
        "optimizer_update": optimizer_audit(args.resource_weight),
    }


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
    parser.add_argument("--probability-threshold", type=float, default=0.01)
    parser.add_argument("--reciprocal-threshold", type=float, default=0.01)
    parser.add_argument("--resource-weight", type=float, default=0.25)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--check", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload(args)
    if args.check is not None:
        check_payload(payload, args.check)
        print(f"checked {args.check}")
        return
    write_json(payload, args.json)
    write_report(payload, args.report)
    print(f"wrote {args.report}")
    print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
