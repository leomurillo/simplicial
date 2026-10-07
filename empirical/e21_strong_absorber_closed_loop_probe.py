"""E21 strong-absorber closed-loop probe.

E20 found that a hybrid value/governance policy outperformed a lightweight
continuous value model in a closed-loop motor-sensing task. E21 gives the
continuous side stronger absorbers:

    - full pairwise quadratic continuous features;
    - random-feature MLP-style continuous features.

The falsifier is simple: if a stronger no-gate continuous absorber matches the
best hybrid policy, then the E20 governance result was probably a capacity
artifact. If the hybrid still wins against comparable capacity, the closed-loop
governance claim survives a more serious absorber baseline.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

import e20_closed_loop_motor_sensing_probe as e20


MODEL_SPECS = [
    ("scalar_lite", "scalar", "lite"),
    ("gate_lite", "gate", "lite"),
    ("continuous_lite", "continuous", "lite"),
    ("continuous_pairwise", "continuous", "pairwise"),
    ("continuous_random_absorber", "continuous", "random"),
    ("hybrid_lite", "hybrid", "lite"),
    ("hybrid_random_absorber", "hybrid", "random"),
]

STRONG_CONTINUOUS = ["continuous_pairwise", "continuous_random_absorber"]
HYBRID_MODELS = ["hybrid_lite", "hybrid_random_absorber"]


@dataclass(frozen=True)
class AbsorberModel:
    name: str
    feature_kind: str
    basis_kind: str
    target_kind: str
    coef: list[float]
    mean: list[float]
    sd: list[float]
    feature_count: int
    expanded_count: int
    random_w: list[list[float]] | None = None
    random_b: list[float] | None = None


def expand_lite(
    x: np.ndarray,
    mean: np.ndarray | None = None,
    sd: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if mean is None:
        mean = x.mean(axis=0)
    if sd is None:
        sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
    return np.hstack([np.ones((z.shape[0], 1)), z, z * z]), mean, sd


def expand_pairwise(
    x: np.ndarray,
    mean: np.ndarray | None = None,
    sd: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if mean is None:
        mean = x.mean(axis=0)
    if sd is None:
        sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
    n, d = z.shape
    expanded_count = 1 + d + d + (d * (d - 1)) // 2
    phi = np.empty((n, expanded_count), dtype=float)
    phi[:, 0] = 1.0
    cursor = 1
    phi[:, cursor : cursor + d] = z
    cursor += d
    phi[:, cursor : cursor + d] = z * z
    cursor += d
    for i in range(d):
        width = d - i - 1
        if width:
            phi[:, cursor : cursor + width] = z[:, [i]] * z[:, i + 1 :]
            cursor += width
    return phi, mean, sd


def expand_random(
    x: np.ndarray,
    hidden: int,
    rng: np.random.Generator | None = None,
    mean: np.ndarray | None = None,
    sd: np.ndarray | None = None,
    random_w: np.ndarray | None = None,
    random_b: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if mean is None:
        mean = x.mean(axis=0)
    if sd is None:
        sd = x.std(axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    z = (x - mean) / sd
    if random_w is None:
        if rng is None:
            raise ValueError("rng is required when random_w is not supplied")
        random_w = rng.normal(scale=1.0 / math.sqrt(max(1, z.shape[1])), size=(z.shape[1], hidden))
    if random_b is None:
        if rng is None:
            raise ValueError("rng is required when random_b is not supplied")
        random_b = rng.uniform(-math.pi, math.pi, size=hidden)
    hidden_features = np.tanh(z @ random_w + random_b)
    phi = np.hstack([np.ones((z.shape[0], 1)), z, z * z, hidden_features])
    return phi, mean, sd, random_w, random_b


def make_basis(
    x_raw: np.ndarray,
    basis_kind: str,
    hidden: int,
    rng: np.random.Generator | None = None,
    mean: np.ndarray | None = None,
    sd: np.ndarray | None = None,
    random_w: np.ndarray | None = None,
    random_b: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray | None, np.ndarray | None]:
    if basis_kind == "lite":
        phi, out_mean, out_sd = expand_lite(x_raw, mean, sd)
        return phi, out_mean, out_sd, None, None
    if basis_kind == "pairwise":
        phi, out_mean, out_sd = expand_pairwise(x_raw, mean, sd)
        return phi, out_mean, out_sd, None, None
    if basis_kind == "random":
        phi, out_mean, out_sd, out_w, out_b = expand_random(
            x_raw,
            hidden=hidden,
            rng=rng,
            mean=mean,
            sd=sd,
            random_w=random_w,
            random_b=random_b,
        )
        return phi, out_mean, out_sd, out_w, out_b
    raise ValueError(f"unknown basis kind: {basis_kind}")


def fit_absorber(
    packets: list[e20.Packet],
    name: str,
    feature_kind: str,
    basis_kind: str,
    target_kind: str,
    gate_threshold: float,
    ridge: float,
    hidden: int,
    seed: int,
) -> AbsorberModel:
    x_raw = e20.raw_matrix(packets, feature_kind, gate_threshold)
    rng = np.random.default_rng(seed)
    phi, mean, sd, random_w, random_b = make_basis(x_raw, basis_kind, hidden, rng=rng)
    y = e20.target_vector(packets, target_kind)
    penalty = ridge * np.eye(phi.shape[1])
    penalty[0, 0] = 0.0
    lhs = phi.T @ phi + penalty
    rhs = phi.T @ y
    try:
        coef = np.linalg.solve(lhs, rhs)
    except np.linalg.LinAlgError:
        coef = np.linalg.pinv(lhs) @ rhs
    return AbsorberModel(
        name=name,
        feature_kind=feature_kind,
        basis_kind=basis_kind,
        target_kind=target_kind,
        coef=[float(v) for v in coef],
        mean=[float(v) for v in mean],
        sd=[float(v) for v in sd],
        feature_count=int(x_raw.shape[1]),
        expanded_count=int(phi.shape[1]),
        random_w=None if random_w is None else [[float(v) for v in row] for row in random_w],
        random_b=None if random_b is None else [float(v) for v in random_b],
    )


def predict_absorber(model: AbsorberModel, packets: list[e20.Packet], gate_threshold: float, hidden: int) -> np.ndarray:
    x_raw = e20.raw_matrix(packets, model.feature_kind, gate_threshold)
    random_w = None if model.random_w is None else np.asarray(model.random_w, dtype=float)
    random_b = None if model.random_b is None else np.asarray(model.random_b, dtype=float)
    phi, _, _, _, _ = make_basis(
        x_raw,
        model.basis_kind,
        hidden=hidden,
        mean=np.asarray(model.mean, dtype=float),
        sd=np.asarray(model.sd, dtype=float),
        random_w=random_w,
        random_b=random_b,
    )
    return phi @ np.asarray(model.coef, dtype=float)


def fit_and_score(
    train: list[e20.Packet],
    test: list[e20.Packet],
    name: str,
    feature_kind: str,
    basis_kind: str,
    gate_threshold: float,
    args: argparse.Namespace,
) -> dict[str, Any]:
    seed_base = args.seed + 21000 + 97 * len(name)
    value_model = fit_absorber(
        train,
        name,
        feature_kind,
        basis_kind,
        "value",
        gate_threshold,
        args.ridge,
        args.random_hidden,
        seed_base,
    )
    select_model = fit_absorber(
        train,
        name,
        feature_kind,
        basis_kind,
        "select",
        gate_threshold,
        args.ridge,
        args.random_hidden,
        seed_base + 1,
    )
    y_value = e20.target_vector(test, "value")
    y_select = e20.target_vector(test, "select")
    value_pred = predict_absorber(value_model, test, gate_threshold, args.random_hidden)
    select_pred = predict_absorber(select_model, test, gate_threshold, args.random_hidden)
    return {
        "value": {
            "rmse_observed": e20.rmse(y_value, value_pred),
            "r2_observed": e20.r2(y_value, value_pred),
        },
        "select_regression": {
            "rmse_observed": e20.rmse(y_select, select_pred),
            "r2_observed": e20.r2(y_select, select_pred),
        },
        "row_selection": e20.row_metrics(test, select_pred, args.row_threshold),
        "policy": e20.policy_metrics(test, select_pred),
        "model": {
            "feature_kind": feature_kind,
            "basis_kind": basis_kind,
            "feature_count": value_model.feature_count,
            "expanded_count": value_model.expanded_count,
        },
    }


def decision_quantities(overall: dict[str, Any]) -> dict[str, float]:
    best_continuous = min(STRONG_CONTINUOUS, key=lambda name: overall[name]["policy"]["mean_regret"])
    best_hybrid = min(HYBRID_MODELS, key=lambda name: overall[name]["policy"]["mean_regret"])
    return {
        "continuous_lite_regret": overall["continuous_lite"]["policy"]["mean_regret"],
        "continuous_pairwise_regret": overall["continuous_pairwise"]["policy"]["mean_regret"],
        "continuous_random_regret": overall["continuous_random_absorber"]["policy"]["mean_regret"],
        "hybrid_lite_regret": overall["hybrid_lite"]["policy"]["mean_regret"],
        "hybrid_random_regret": overall["hybrid_random_absorber"]["policy"]["mean_regret"],
        "best_strong_continuous_regret": overall[best_continuous]["policy"]["mean_regret"],
        "best_hybrid_regret": overall[best_hybrid]["policy"]["mean_regret"],
        "continuous_lite_accuracy": overall["continuous_lite"]["policy"]["action_accuracy"],
        "continuous_pairwise_accuracy": overall["continuous_pairwise"]["policy"]["action_accuracy"],
        "continuous_random_accuracy": overall["continuous_random_absorber"]["policy"]["action_accuracy"],
        "hybrid_lite_accuracy": overall["hybrid_lite"]["policy"]["action_accuracy"],
        "hybrid_random_accuracy": overall["hybrid_random_absorber"]["policy"]["action_accuracy"],
        "best_strong_continuous_accuracy": overall[best_continuous]["policy"]["action_accuracy"],
        "best_hybrid_accuracy": overall[best_hybrid]["policy"]["action_accuracy"],
        "continuous_lite_unnecessary_unsafe": overall["continuous_lite"]["policy"]["unnecessary_unsafe"],
        "continuous_pairwise_unnecessary_unsafe": overall["continuous_pairwise"]["policy"]["unnecessary_unsafe"],
        "continuous_random_unnecessary_unsafe": overall["continuous_random_absorber"]["policy"]["unnecessary_unsafe"],
        "hybrid_lite_unnecessary_unsafe": overall["hybrid_lite"]["policy"]["unnecessary_unsafe"],
        "hybrid_random_unnecessary_unsafe": overall["hybrid_random_absorber"]["policy"]["unnecessary_unsafe"],
        "best_strong_continuous_unnecessary_unsafe": overall[best_continuous]["policy"]["unnecessary_unsafe"],
        "best_hybrid_unnecessary_unsafe": overall[best_hybrid]["policy"]["unnecessary_unsafe"],
        "best_strong_continuous_model": float(STRONG_CONTINUOUS.index(best_continuous)),
        "best_hybrid_model": float(HYBRID_MODELS.index(best_hybrid)),
    }


def classify_finding(args: argparse.Namespace, dq: dict[str, float]) -> str:
    continuous_absorbs = (
        dq["best_strong_continuous_regret"] <= dq["best_hybrid_regret"] + args.regret_margin
        and dq["best_strong_continuous_accuracy"] >= dq["best_hybrid_accuracy"] - args.accuracy_margin
    )
    hybrid_survives = (
        dq["best_hybrid_regret"] + args.regret_margin < dq["best_strong_continuous_regret"]
        and dq["best_hybrid_accuracy"] > dq["best_strong_continuous_accuracy"] + args.accuracy_margin
    )
    capacity_confounded = (
        dq["best_strong_continuous_regret"] + args.regret_margin < dq["hybrid_lite_regret"]
        and dq["best_strong_continuous_accuracy"] > dq["hybrid_lite_accuracy"] + args.accuracy_margin
    )
    hybrid_soft_edge = (
        dq["best_hybrid_regret"] <= dq["best_strong_continuous_regret"] + args.regret_margin
        and dq["best_hybrid_accuracy"] > dq["best_strong_continuous_accuracy"] + args.accuracy_margin
    )
    if continuous_absorbs:
        return "STRONG_ABSORBER_ABSORBS_GOVERNANCE"
    if hybrid_survives:
        return "GOVERNANCE_SURVIVES_STRONG_ABSORBER"
    if capacity_confounded and hybrid_soft_edge:
        return "E20_CAPACITY_CONFOUND_WITH_HYBRID_EDGE"
    if capacity_confounded:
        return "E20_CAPACITY_CONFOUND_DETECTED"
    return "STRONG_ABSORBER_CLOSED_LOOP_INCONCLUSIVE"


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    train, cal, test = e20.build_packets_for_cost(args, args.aim_cost)
    gate_threshold = e20.calibrate_gate(cal, args.alpha)
    overall: dict[str, Any] = {}
    for name, feature_kind, basis_kind in MODEL_SPECS:
        overall[name] = fit_and_score(train, test, name, feature_kind, basis_kind, gate_threshold, args)
    dq = decision_quantities(overall)
    strong_names = {
        "best_strong_continuous": STRONG_CONTINUOUS[int(dq["best_strong_continuous_model"])],
        "best_hybrid": HYBRID_MODELS[int(dq["best_hybrid_model"])],
    }
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": {
            "name": "Synthetic closed-loop motor-sensing field",
            "source": "E20 simulator",
            "classes": len(e20.CLASSES),
            "actions": e20.ACTIONS,
        },
        "config": {
            "seed": args.seed,
            "train_n": args.train_n,
            "calibration_n": args.calibration_n,
            "test_n": args.test_n,
            "aim_cost": args.aim_cost,
            "hold_cost": args.hold_cost,
            "alpha": args.alpha,
            "ridge": args.ridge,
            "random_hidden": args.random_hidden,
            "utility_noise": args.utility_noise,
            "select_noise": args.select_noise,
        },
        "gate_threshold": gate_threshold,
        "train_summary": e20.summarize_packets(train),
        "calibration_summary": e20.summarize_packets(cal),
        "test_summary": e20.summarize_packets(test),
        "overall": overall,
        "decision_quantities": dq,
        "strong_names": strong_names,
    }
    result["finding"] = classify_finding(args, dq)
    return result


def fmt(value: float) -> str:
    if isinstance(value, float) and math.isnan(value):
        return "nan"
    return f"{value:.3f}"


def action_counts(counts: dict[str, int]) -> str:
    return ", ".join(f"{action}:{counts.get(action, 0)}" for action in e20.ACTIONS)


def write_report(path: Path, result: dict[str, Any]) -> None:
    config = result["config"]
    overall = result["overall"]
    dq = result["decision_quantities"]
    strong = result["strong_names"]
    lines: list[str] = []
    lines.extend(
        [
            "# E21 Strong-Absorber Closed-Loop Probe",
            "",
            f"- timestamp: `{result['timestamp']}`",
            f"- dataset: `{result['dataset']['name']}`",
            f"- train/calibration/test episodes: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
            f"- aim/hold cost: `{config['aim_cost']}` / `{config['hold_cost']}`",
            f"- random hidden features: `{config['random_hidden']}`",
            f"- alpha: `{config['alpha']}`",
            f"- gate threshold: `{fmt(result['gate_threshold'])}`",
            f"- finding: **{result['finding']}**",
            "",
            "## Claim Tested",
            "",
            "E21 asks whether the E20 hybrid win survives stronger no-gate",
            "continuous absorbers. The task and simulator are inherited from",
            "E20; only model capacity is changed.",
            "",
            "## Main Decision Quantities",
            "",
            "| quantity | value |",
            "| --- | --- |",
        ]
    )
    for key, value in dq.items():
        if key.endswith("_model"):
            continue
        lines.append(f"| {key.replace('_', ' ')} | {fmt(value)} |")
    lines.extend(
        [
            f"| best strong continuous | {strong['best_strong_continuous']} |",
            f"| best hybrid | {strong['best_hybrid']} |",
            "",
            "## Split Summary",
            "",
            "| split | episodes | packets | mean utility | mean gate | mean unsafe | optimal actions |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for key in ["train_summary", "calibration_summary", "test_summary"]:
        s = result[key]
        lines.append(
            "| "
            + " | ".join(
                [
                    key.replace("_summary", ""),
                    str(s["episodes"]),
                    str(s["packets"]),
                    fmt(s["mean_utility"]),
                    fmt(s["mean_gate_score"]),
                    fmt(s["mean_unsafe"]),
                    action_counts(s["optimal_actions"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Model Summary",
            "",
            "| model | basis | expanded | value RMSE | value R2 | action acc | regret | p90 regret | unsafe choice | unnecessary unsafe | row detect | row false |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for name, _, _ in MODEL_SPECS:
        item = overall[name]
        model = item["model"]
        value = item["value"]
        policy = item["policy"]
        row = item["row_selection"]
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    model["basis_kind"],
                    str(model["expanded_count"]),
                    fmt(value["rmse_observed"]),
                    fmt(value["r2_observed"]),
                    fmt(policy["action_accuracy"]),
                    fmt(policy["mean_regret"]),
                    fmt(policy["p90_regret"]),
                    fmt(policy["unsafe_choice"]),
                    fmt(policy["unnecessary_unsafe"]),
                    fmt(row["optimal_detection"]),
                    fmt(row["nonoptimal_false_admission"]),
                ]
            )
            + " |"
        )

    finding = result["finding"]
    if finding == "STRONG_ABSORBER_ABSORBS_GOVERNANCE":
        interpretation = [
            "The strong no-gate continuous absorber matches the best hybrid",
            "policy. This makes the E20 hybrid result look capacity-dependent.",
        ]
    elif finding == "GOVERNANCE_SURVIVES_STRONG_ABSORBER":
        interpretation = [
            "The hybrid policy still wins after giving continuous value",
            "pairwise and random-feature absorbers. The E20 governance signal",
            "survives this capacity falsifier.",
        ]
    elif finding == "E20_CAPACITY_CONFOUND_WITH_HYBRID_EDGE":
        interpretation = [
            "A stronger continuous absorber erases most of the original",
            "hybrid-lite advantage, so E20 was capacity-sensitive. A",
            "capacity-matched hybrid still keeps a small accuracy edge, but",
            "the regret gap is too small for a strong survival claim.",
        ]
    elif finding == "E20_CAPACITY_CONFOUND_DETECTED":
        interpretation = [
            "A stronger continuous absorber beats the original hybrid-lite",
            "baseline. E20 needs to be restated as a capacity-sensitive result.",
        ]
    else:
        interpretation = [
            "The probe is inconclusive at the configured margins.",
            "It should be read as a capacity diagnostic, not a positive result.",
        ]
    lines.extend(["", "## Interpretation", "", *interpretation])
    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the simulator and task are inherited from E20;",
            "- no-gate continuous models receive pairwise and random nonlinear absorbers;",
            "- hybrid_random_absorber receives comparable random-feature capacity;",
            "- policy metrics choose one action per held-out episode and score regret;",
            "- a governance win is counted only against the best strong continuous baseline.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--train-n", type=int, default=5200)
    parser.add_argument("--calibration-n", type=int, default=1800)
    parser.add_argument("--test-n", type=int, default=3000)
    parser.add_argument("--temperature", type=float, default=0.42)
    parser.add_argument("--hold-gain", type=float, default=0.18)
    parser.add_argument("--correct-gain", type=float, default=0.78)
    parser.add_argument("--wrong-gain", type=float, default=0.70)
    parser.add_argument("--hold-noise", type=float, default=0.11)
    parser.add_argument("--correct-noise", type=float, default=0.09)
    parser.add_argument("--wrong-noise", type=float, default=0.16)
    parser.add_argument("--rupture-gain", type=float, default=0.55)
    parser.add_argument("--rupture-noise", type=float, default=0.28)
    parser.add_argument("--hold-cost", type=float, default=0.018)
    parser.add_argument("--aim-cost", type=float, default=0.040)
    parser.add_argument("--energy-cost", type=float, default=0.012)
    parser.add_argument("--aim-cost-grid", type=float, nargs="+", default=[0.040])
    parser.add_argument("--rupture-penalty", type=float, default=0.10)
    parser.add_argument("--unsafe-penalty", type=float, default=0.03)
    parser.add_argument("--smoothness-scale", type=float, default=1.65)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--ridge", type=float, default=1.2e-2)
    parser.add_argument("--random-hidden", type=int, default=384)
    parser.add_argument("--utility-noise", type=float, default=0.012)
    parser.add_argument("--select-noise", type=float, default=0.020)
    parser.add_argument("--row-threshold", type=float, default=0.50)
    parser.add_argument("--regret-margin", type=float, default=0.006)
    parser.add_argument("--accuracy-margin", type=float, default=0.012)
    parser.add_argument(
        "--report-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "reports",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_probe(args)
    args.report_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.report_dir / "e21_strong_absorber_closed_loop_probe.json"
    md_path = args.report_dir / "e21_strong_absorber_closed_loop_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
