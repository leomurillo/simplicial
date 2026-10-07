"""E22 trained-MLP closed-loop absorber probe.

E21 showed that a full pairwise continuous absorber nearly erased E20's
governance advantage. E22 replaces the random-feature absorber with a genuinely
trained NumPy MLP. The task and simulator are inherited from E20; the question
is whether a learned nonlinear no-gate state-action predictor absorbs the gate,
or whether a gate-aware hybrid MLP keeps a residual policy advantage.
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
import e21_strong_absorber_closed_loop_probe as e21


MODEL_ORDER = [
    "continuous_pairwise_ridge",
    "continuous_mlp",
    "hybrid_mlp",
]


@dataclass
class MLP:
    x_mean: np.ndarray
    x_sd: np.ndarray
    y_mean: float
    y_sd: float
    weights: list[np.ndarray]
    biases: list[np.ndarray]
    history: list[dict[str, float]]
    feature_kind: str
    target_kind: str


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(x, 0.0)


def init_mlp(input_dim: int, hidden: list[int], rng: np.random.Generator) -> tuple[list[np.ndarray], list[np.ndarray]]:
    dims = [input_dim, *hidden, 1]
    weights = []
    biases = []
    for i in range(len(dims) - 1):
        scale = math.sqrt(2.0 / max(1, dims[i]))
        weights.append(rng.normal(scale=scale, size=(dims[i], dims[i + 1])))
        biases.append(np.zeros(dims[i + 1], dtype=float))
    return weights, biases


def forward(weights: list[np.ndarray], biases: list[np.ndarray], x: np.ndarray) -> tuple[np.ndarray, list[np.ndarray], list[np.ndarray]]:
    activations = [x]
    preacts = []
    h = x
    for w, b in zip(weights[:-1], biases[:-1]):
        z = h @ w + b
        preacts.append(z)
        h = relu(z)
        activations.append(h)
    out = h @ weights[-1] + biases[-1]
    preacts.append(out)
    activations.append(out)
    return out[:, 0], activations, preacts


def predict_mlp(model: MLP, x_raw: np.ndarray) -> np.ndarray:
    x = (x_raw - model.x_mean) / model.x_sd
    y_scaled, _, _ = forward(model.weights, model.biases, x)
    return y_scaled * model.y_sd + model.y_mean


def adam_step(
    weights: list[np.ndarray],
    biases: list[np.ndarray],
    grad_w: list[np.ndarray],
    grad_b: list[np.ndarray],
    state: dict[str, list[np.ndarray] | int],
    lr: float,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> None:
    state["t"] = int(state["t"]) + 1
    t = int(state["t"])
    mw = state["mw"]
    vw = state["vw"]
    mb = state["mb"]
    vb = state["vb"]
    assert isinstance(mw, list) and isinstance(vw, list) and isinstance(mb, list) and isinstance(vb, list)
    for i in range(len(weights)):
        mw[i] = beta1 * mw[i] + (1.0 - beta1) * grad_w[i]
        vw[i] = beta2 * vw[i] + (1.0 - beta2) * (grad_w[i] * grad_w[i])
        mb[i] = beta1 * mb[i] + (1.0 - beta1) * grad_b[i]
        vb[i] = beta2 * vb[i] + (1.0 - beta2) * (grad_b[i] * grad_b[i])
        mw_hat = mw[i] / (1.0 - beta1**t)
        vw_hat = vw[i] / (1.0 - beta2**t)
        mb_hat = mb[i] / (1.0 - beta1**t)
        vb_hat = vb[i] / (1.0 - beta2**t)
        weights[i] -= lr * mw_hat / (np.sqrt(vw_hat) + eps)
        biases[i] -= lr * mb_hat / (np.sqrt(vb_hat) + eps)


def train_mlp(
    train_x: np.ndarray,
    train_y: np.ndarray,
    val_x: np.ndarray,
    val_y: np.ndarray,
    feature_kind: str,
    target_kind: str,
    args: argparse.Namespace,
    seed_offset: int,
) -> MLP:
    rng = np.random.default_rng(args.seed + seed_offset)
    x_mean = train_x.mean(axis=0)
    x_sd = train_x.std(axis=0)
    x_sd = np.where(x_sd < 1e-8, 1.0, x_sd)
    y_mean = float(train_y.mean())
    y_sd = float(train_y.std())
    if y_sd < 1e-8:
        y_sd = 1.0
    x = (train_x - x_mean) / x_sd
    y = (train_y - y_mean) / y_sd
    xv = (val_x - x_mean) / x_sd
    yv = (val_y - y_mean) / y_sd

    weights, biases = init_mlp(x.shape[1], args.hidden, rng)
    best_weights = [w.copy() for w in weights]
    best_biases = [b.copy() for b in biases]
    best_val = float("inf")
    patience_left = args.patience
    history: list[dict[str, float]] = []
    state: dict[str, list[np.ndarray] | int] = {
        "t": 0,
        "mw": [np.zeros_like(w) for w in weights],
        "vw": [np.zeros_like(w) for w in weights],
        "mb": [np.zeros_like(b) for b in biases],
        "vb": [np.zeros_like(b) for b in biases],
    }

    for epoch in range(1, args.epochs + 1):
        order = rng.permutation(len(x))
        for start in range(0, len(x), args.batch_size):
            idx = order[start : start + args.batch_size]
            xb = x[idx]
            yb = y[idx]
            pred, activations, preacts = forward(weights, biases, xb)
            grad = (2.0 / len(xb)) * (pred - yb)
            delta = grad[:, None]
            grad_w = [np.zeros_like(w) for w in weights]
            grad_b = [np.zeros_like(b) for b in biases]
            for layer in reversed(range(len(weights))):
                grad_w[layer] = activations[layer].T @ delta + args.l2 * weights[layer]
                grad_b[layer] = delta.sum(axis=0)
                if layer > 0:
                    delta = delta @ weights[layer].T
                    delta = delta * (preacts[layer - 1] > 0.0)
            adam_step(weights, biases, grad_w, grad_b, state, args.lr)

        train_pred, _, _ = forward(weights, biases, x)
        val_pred, _, _ = forward(weights, biases, xv)
        train_loss = float(np.mean((train_pred - y) ** 2))
        val_loss = float(np.mean((val_pred - yv) ** 2))
        if epoch == 1 or epoch % args.history_every == 0 or epoch == args.epochs:
            history.append({"epoch": float(epoch), "train_mse_scaled": train_loss, "val_mse_scaled": val_loss})
        if val_loss < best_val - args.min_delta:
            best_val = val_loss
            best_weights = [w.copy() for w in weights]
            best_biases = [b.copy() for b in biases]
            patience_left = args.patience
        else:
            patience_left -= 1
            if patience_left <= 0:
                break

    return MLP(
        x_mean=x_mean,
        x_sd=x_sd,
        y_mean=y_mean,
        y_sd=y_sd,
        weights=best_weights,
        biases=best_biases,
        history=history,
        feature_kind=feature_kind,
        target_kind=target_kind,
    )


def train_and_score_mlp(
    train: list[e20.Packet],
    cal: list[e20.Packet],
    test: list[e20.Packet],
    name: str,
    feature_kind: str,
    gate_threshold: float,
    args: argparse.Namespace,
    seed_offset: int,
) -> dict[str, Any]:
    train_x = e20.raw_matrix(train, feature_kind, gate_threshold)
    cal_x = e20.raw_matrix(cal, feature_kind, gate_threshold)
    test_x = e20.raw_matrix(test, feature_kind, gate_threshold)

    train_value = e20.target_vector(train, "value")
    cal_value = e20.target_vector(cal, "value")
    test_value = e20.target_vector(test, "value")
    train_select = e20.target_vector(train, "select")
    cal_select = e20.target_vector(cal, "select")
    test_select = e20.target_vector(test, "select")

    value_model = train_mlp(train_x, train_value, cal_x, cal_value, feature_kind, "value", args, seed_offset)
    select_model = train_mlp(train_x, train_select, cal_x, cal_select, feature_kind, "select", args, seed_offset + 1)

    value_pred = predict_mlp(value_model, test_x)
    select_pred = predict_mlp(select_model, test_x)

    return {
        "value": {
            "rmse_observed": e20.rmse(test_value, value_pred),
            "r2_observed": e20.r2(test_value, value_pred),
        },
        "select_regression": {
            "rmse_observed": e20.rmse(test_select, select_pred),
            "r2_observed": e20.r2(test_select, select_pred),
        },
        "row_selection": e20.row_metrics(test, select_pred, args.row_threshold),
        "policy": e20.policy_metrics(test, select_pred),
        "model": {
            "feature_kind": feature_kind,
            "basis_kind": "trained_mlp",
            "feature_count": int(train_x.shape[1]),
            "hidden": args.hidden,
            "value_history": value_model.history,
            "select_history": select_model.history,
        },
    }


def pairwise_reference(
    train: list[e20.Packet],
    test: list[e20.Packet],
    gate_threshold: float,
    args: argparse.Namespace,
) -> dict[str, Any]:
    return e21.fit_and_score(
        train,
        test,
        "continuous_pairwise_ridge",
        "continuous",
        "pairwise",
        gate_threshold,
        args,
    )


def decision_quantities(overall: dict[str, Any]) -> dict[str, float]:
    return {
        "pairwise_regret": overall["continuous_pairwise_ridge"]["policy"]["mean_regret"],
        "continuous_mlp_regret": overall["continuous_mlp"]["policy"]["mean_regret"],
        "hybrid_mlp_regret": overall["hybrid_mlp"]["policy"]["mean_regret"],
        "pairwise_accuracy": overall["continuous_pairwise_ridge"]["policy"]["action_accuracy"],
        "continuous_mlp_accuracy": overall["continuous_mlp"]["policy"]["action_accuracy"],
        "hybrid_mlp_accuracy": overall["hybrid_mlp"]["policy"]["action_accuracy"],
        "pairwise_unnecessary_unsafe": overall["continuous_pairwise_ridge"]["policy"]["unnecessary_unsafe"],
        "continuous_mlp_unnecessary_unsafe": overall["continuous_mlp"]["policy"]["unnecessary_unsafe"],
        "hybrid_mlp_unnecessary_unsafe": overall["hybrid_mlp"]["policy"]["unnecessary_unsafe"],
        "continuous_mlp_value_rmse": overall["continuous_mlp"]["value"]["rmse_observed"],
        "hybrid_mlp_value_rmse": overall["hybrid_mlp"]["value"]["rmse_observed"],
    }


def classify_finding(args: argparse.Namespace, dq: dict[str, float]) -> str:
    mlp_absorbs = (
        dq["continuous_mlp_regret"] <= dq["hybrid_mlp_regret"] + args.regret_margin
        and dq["continuous_mlp_accuracy"] >= dq["hybrid_mlp_accuracy"] - args.accuracy_margin
    )
    hybrid_survives = (
        dq["hybrid_mlp_regret"] + args.regret_margin < dq["continuous_mlp_regret"]
        and dq["hybrid_mlp_accuracy"] > dq["continuous_mlp_accuracy"] + args.accuracy_margin
    )
    pairwise_still_best = (
        dq["pairwise_regret"] + args.regret_margin < min(dq["continuous_mlp_regret"], dq["hybrid_mlp_regret"])
    )
    if mlp_absorbs:
        return "TRAINED_MLP_ABSORBS_GATE"
    if hybrid_survives:
        return "GATE_RESIDUAL_SURVIVES_TRAINED_MLP"
    if pairwise_still_best:
        return "PAIRWISE_ABSORBER_STILL_STRONGER_THAN_MLP"
    return "TRAINED_MLP_CLOSED_LOOP_INCONCLUSIVE"


def run_probe(args: argparse.Namespace) -> dict[str, Any]:
    train, cal, test = e20.build_packets_for_cost(args, args.aim_cost)
    gate_threshold = e20.calibrate_gate(cal, args.alpha)
    overall: dict[str, Any] = {}
    overall["continuous_pairwise_ridge"] = pairwise_reference(train, test, gate_threshold, args)
    overall["continuous_mlp"] = train_and_score_mlp(train, cal, test, "continuous_mlp", "continuous", gate_threshold, args, 2400)
    overall["hybrid_mlp"] = train_and_score_mlp(train, cal, test, "hybrid_mlp", "hybrid", gate_threshold, args, 2600)
    dq = decision_quantities(overall)
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
            "hidden": args.hidden,
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "patience": args.patience,
        },
        "gate_threshold": gate_threshold,
        "train_summary": e20.summarize_packets(train),
        "calibration_summary": e20.summarize_packets(cal),
        "test_summary": e20.summarize_packets(test),
        "overall": overall,
        "decision_quantities": dq,
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
    lines: list[str] = []
    lines.extend(
        [
            "# E22 Trained-MLP Closed-Loop Probe",
            "",
            f"- timestamp: `{result['timestamp']}`",
            f"- dataset: `{result['dataset']['name']}`",
            f"- train/calibration/test episodes: `{config['train_n']}` / `{config['calibration_n']}` / `{config['test_n']}`",
            f"- aim/hold cost: `{config['aim_cost']}` / `{config['hold_cost']}`",
            f"- hidden layers: `{config['hidden']}`",
            f"- epochs/patience: `{config['epochs']}` / `{config['patience']}`",
            f"- alpha: `{config['alpha']}`",
            f"- gate threshold: `{fmt(result['gate_threshold'])}`",
            f"- finding: **{result['finding']}**",
            "",
            "## Claim Tested",
            "",
            "E22 replaces E21's random-feature absorber with a genuinely",
            "trained NumPy MLP. The simulator is unchanged from E20/E21.",
            "The decisive comparison is continuous_mlp versus hybrid_mlp.",
            "",
            "## Main Decision Quantities",
            "",
            "| quantity | value |",
            "| --- | --- |",
        ]
    )
    for key, value in dq.items():
        lines.append(f"| {key.replace('_', ' ')} | {fmt(value)} |")
    lines.extend(
        [
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
            "| model | basis | raw features | expanded/hidden | value RMSE | value R2 | select RMSE | action acc | regret | p90 regret | unsafe choice | unnecessary unsafe | row detect | row false |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for name in MODEL_ORDER:
        item = overall[name]
        model = item["model"]
        value = item["value"]
        select = item["select_regression"]
        policy = item["policy"]
        row = item["row_selection"]
        raw_features = model.get("feature_count", "")
        expanded = model.get("expanded_count", model.get("hidden", ""))
        basis = model.get("basis_kind", "unknown")
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    str(basis),
                    str(raw_features),
                    str(expanded),
                    fmt(value["rmse_observed"]),
                    fmt(value["r2_observed"]),
                    fmt(select["rmse_observed"]),
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
    if finding == "TRAINED_MLP_ABSORBS_GATE":
        interpretation = [
            "The trained no-gate continuous MLP absorbs the gate-aware hybrid.",
            "This means the gate residual is not irreducible in this simulator.",
        ]
    elif finding == "GATE_RESIDUAL_SURVIVES_TRAINED_MLP":
        interpretation = [
            "The gate-aware hybrid MLP beats the no-gate continuous MLP.",
            "This is the first stronger evidence that a gate-like residual",
            "survives learned nonlinear state-action prediction.",
        ]
    elif finding == "PAIRWISE_ABSORBER_STILL_STRONGER_THAN_MLP":
        interpretation = [
            "The trained MLP did not beat the pairwise ridge absorber.",
            "This makes E22 a capacity diagnostic rather than a gate result.",
        ]
    else:
        interpretation = [
            "The trained MLP comparison is inconclusive at the configured",
            "margins.",
        ]
    lines.extend(["", "## Interpretation", "", *interpretation])
    lines.extend(
        [
            "",
            "## Anti-Tautology Checks",
            "",
            "- the task and simulator are inherited from E20/E21;",
            "- continuous_mlp has no gate features;",
            "- hybrid_mlp has the same architecture plus gate features;",
            "- both MLPs are trained by minibatch Adam with validation early stopping;",
            "- continuous_pairwise_ridge is retained as the E21 absorber reference;",
            "- policy metrics choose one action per held-out episode and score regret.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--train-n", type=int, default=2400)
    parser.add_argument("--calibration-n", type=int, default=900)
    parser.add_argument("--test-n", type=int, default=1600)
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
    parser.add_argument("--random-hidden", type=int, default=128)
    parser.add_argument("--utility-noise", type=float, default=0.012)
    parser.add_argument("--select-noise", type=float, default=0.020)
    parser.add_argument("--row-threshold", type=float, default=0.50)
    parser.add_argument("--hidden", type=int, nargs="+", default=[64, 32])
    parser.add_argument("--epochs", type=int, default=55)
    parser.add_argument("--batch-size", type=int, default=384)
    parser.add_argument("--lr", type=float, default=0.0025)
    parser.add_argument("--l2", type=float, default=2e-4)
    parser.add_argument("--patience", type=int, default=8)
    parser.add_argument("--min-delta", type=float, default=1e-5)
    parser.add_argument("--history-every", type=int, default=10)
    parser.add_argument("--regret-margin", type=float, default=0.008)
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
    json_path = args.report_dir / "e22_trained_mlp_closed_loop_probe.json"
    md_path = args.report_dir / "e22_trained_mlp_closed_loop_probe.md"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_report(md_path, result)
    print(json.dumps({"finding": result["finding"], "json": str(json_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
