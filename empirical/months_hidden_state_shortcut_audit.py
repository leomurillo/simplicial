"""Shortcut audit for month hidden-state probes.

This is the non-tautological live-hidden-state audit for the conductor probe
obstruction note.  It asks three questions on the saved layer-28 month
activation features:

1. How much held-out result accuracy do quotient probes retain?
2. What conductor packet profile does an unconstrained full-label result probe
   put in its twelve output logits, before any quotient lift is applied?
3. Does result accuracy survive after linearly residualizing the input-side
   shortcut variables, namely source month and offset number?

The residualizer is fit on the training fold only and then applied to the held
out fold using the corresponding source-month/offset covariates.
"""

from __future__ import annotations

import argparse
import json
import math
import struct
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import numpy as np


EPS = 1e-12
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
NUMBER_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
}
MONTH_TO_INDEX = {name: i for i, name in enumerate(MONTHS)}


@dataclass(frozen=True)
class RidgeProbe:
    mean: np.ndarray
    scale: np.ndarray
    weights: np.ndarray

    def scores(self, features: np.ndarray) -> np.ndarray:
        x = (features - self.mean) / self.scale
        x_aug = np.column_stack([x, np.ones(x.shape[0])])
        return x_aug @ self.weights


def load_safetensors(path: Path) -> np.ndarray:
    with path.open("rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        data = f.read()
    key = next(k for k in header if k != "__metadata__")
    meta = header[key]
    start, end = meta["data_offsets"]
    if meta["dtype"] == "BF16":
        raw = np.frombuffer(data[start:end], dtype=np.uint16).copy()
        out = np.zeros(raw.size, dtype=np.uint32)
        out |= raw.astype(np.uint32) << 16
        return out.view(np.float32).reshape(meta["shape"]).copy()
    dtype_map = {"F64": np.float64, "F32": np.float32, "F16": np.float16}
    if meta["dtype"] not in dtype_map:
        raise ValueError(f"Unsupported dtype: {meta['dtype']}")
    return np.frombuffer(data[start:end], dtype=dtype_map[meta["dtype"]]).reshape(meta["shape"]).copy()


def load_rows(path: Path) -> list[dict[str, str]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    rows: list[dict[str, str]] = []
    for row in raw:
        item = row["input"]
        rows.append(
            {
                "entity": item["entity"],
                "number": item["number"],
                "result": item["result"],
            }
        )
    return rows


def labels_from_rows(rows: list[dict[str, str]]) -> dict[str, np.ndarray]:
    entity = np.asarray([MONTH_TO_INDEX[row["entity"]] for row in rows], dtype=int)
    number_value = np.asarray([NUMBER_WORDS[row["number"]] for row in rows], dtype=int)
    number = number_value - 1
    result = np.asarray([MONTH_TO_INDEX[row["result"]] for row in rows], dtype=int)
    unwrapped_sum = entity + number_value
    return {
        "source_month": entity,
        "offset_number": number,
        "result_month": result,
        "unwrapped_source_plus_offset": compress_labels(unwrapped_sum),
    }


def compress_labels(labels: np.ndarray) -> np.ndarray:
    values = {value: i for i, value in enumerate(sorted(set(labels.tolist())))}
    return np.asarray([values[value] for value in labels], dtype=int)


def stratified_split(labels: np.ndarray, test_per_class: int, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    train_parts: list[np.ndarray] = []
    test_parts: list[np.ndarray] = []
    for label in sorted(set(labels.tolist())):
        idx = np.flatnonzero(labels == label)
        rng.shuffle(idx)
        if idx.size <= test_per_class:
            raise ValueError(f"Not enough examples for label {label}")
        test_parts.append(idx[:test_per_class])
        train_parts.append(idx[test_per_class:])
    train = np.concatenate(train_parts)
    test = np.concatenate(test_parts)
    rng.shuffle(train)
    rng.shuffle(test)
    return train, test


def one_hot(labels: np.ndarray, n_classes: int) -> np.ndarray:
    out = np.zeros((labels.size, n_classes), dtype=float)
    out[np.arange(labels.size), labels] = 1.0
    return out


def fit_ridge_probe(features: np.ndarray, labels: np.ndarray, n_classes: int, alpha: float) -> RidgeProbe:
    mean = features.mean(axis=0)
    scale = features.std(axis=0)
    scale = np.where(scale < EPS, 1.0, scale)
    x = (features - mean) / scale
    y = one_hot(labels, n_classes)
    y_mean = y.mean(axis=0)
    y_centered = y - y_mean
    if x.shape[1] <= x.shape[0]:
        reg = alpha * np.eye(x.shape[1])
        feature_weights = np.linalg.solve(x.T @ x + reg, x.T @ y_centered)
    else:
        reg = alpha * np.eye(x.shape[0])
        dual = np.linalg.solve(x @ x.T + reg, y_centered)
        feature_weights = x.T @ dual
    weights = np.vstack([feature_weights, y_mean])
    return RidgeProbe(mean=mean, scale=scale, weights=weights)


def accuracy(scores: np.ndarray, labels: np.ndarray) -> float:
    return float(np.mean(np.argmax(scores, axis=1) == labels))


def conductor_packets(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {}
    for character in range(1, n):
        conductor = n // math.gcd(n, character)
        packets.setdefault(conductor, []).append(character)
    return {d: packets[d] for d in sorted(packets)}


def packet_energy(scores: np.ndarray, packets: dict[int, list[int]]) -> dict[int, float]:
    n = scores.shape[1]
    energy = {d: 0.0 for d in packets}
    for row in scores:
        centered = row - float(np.mean(row))
        coeff = np.fft.fft(centered) / math.sqrt(n)
        for d, indices in packets.items():
            energy[d] += float(np.sum(np.abs(coeff[indices]) ** 2).real)
    return energy


def energy_fractions(energy: dict[int, float]) -> dict[int, float]:
    total = sum(energy.values())
    if total <= EPS:
        return {d: 0.0 for d in energy}
    return {d: float(value / total) for d, value in energy.items()}


def covariate_matrix(labels: dict[str, np.ndarray], indices: np.ndarray) -> np.ndarray:
    source = one_hot(labels["source_month"][indices], len(MONTHS))
    offset = one_hot(labels["offset_number"][indices], len(NUMBER_WORDS))
    intercept = np.ones((indices.size, 1), dtype=float)
    return np.column_stack([intercept, source, offset])


def fit_residualizer(x_train: np.ndarray, z_train: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(z_train, x_train, rcond=None)
    return coef


def target_summary(
    x_train: np.ndarray,
    x_test: np.ndarray,
    y_train: np.ndarray,
    y_test: np.ndarray,
    n_classes: int,
    alpha: float,
) -> dict[str, float]:
    probe = fit_ridge_probe(x_train, y_train, n_classes, alpha)
    train_scores = probe.scores(x_train)
    test_scores = probe.scores(x_test)
    return {
        "classes": int(n_classes),
        "chance": float(1.0 / n_classes),
        "train_accuracy": accuracy(train_scores, y_train),
        "test_accuracy": accuracy(test_scores, y_test),
    }


def evaluate_representation(
    name: str,
    x_train: np.ndarray,
    x_test: np.ndarray,
    labels: dict[str, np.ndarray],
    train_idx: np.ndarray,
    test_idx: np.ndarray,
    alpha: float,
) -> dict[str, Any]:
    packets = conductor_packets(len(MONTHS))
    y_result_train = labels["result_month"][train_idx]
    y_result_test = labels["result_month"][test_idx]

    full_probe = fit_ridge_probe(x_train, y_result_train, len(MONTHS), alpha)
    full_train_scores = full_probe.scores(x_train)
    full_test_scores = full_probe.scores(x_test)
    full_energy = packet_energy(full_test_scores, packets)
    full_fractions = energy_fractions(full_energy)

    quotient_results: dict[int, dict[str, float]] = {}
    for k in (2, 3, 4, 6, 12):
        y_train = y_result_train % k
        y_test = y_result_test % k
        quotient_results[k] = target_summary(x_train, x_test, y_train, y_test, k, alpha)

    target_results: dict[str, dict[str, float]] = {}
    target_specs = {
        "result_month": len(MONTHS),
        "source_month": len(MONTHS),
        "offset_number": len(NUMBER_WORDS),
        "unwrapped_source_plus_offset": int(labels["unwrapped_source_plus_offset"].max()) + 1,
    }
    for target, n_classes in target_specs.items():
        target_results[target] = target_summary(
            x_train,
            x_test,
            labels[target][train_idx],
            labels[target][test_idx],
            n_classes,
            alpha,
        )

    return {
        "name": name,
        "full_result_probe": {
            "classes": len(MONTHS),
            "chance": 1.0 / len(MONTHS),
            "train_accuracy": accuracy(full_train_scores, y_result_train),
            "test_accuracy": accuracy(full_test_scores, y_result_test),
            "packet_energy": full_energy,
            "packet_fractions": full_fractions,
        },
        "quotient_result_probes": quotient_results,
        "target_decodability": target_results,
    }


def format_target_table(results: dict[str, dict]) -> list[str]:
    lines = [
        "| representation | target | classes | chance | train acc | test acc |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for rep_name, rep in results.items():
        for target, row in rep["target_decodability"].items():
            lines.append(
                f"| {rep_name} | {target} | {row['classes']} | {row['chance']:.3f} | "
                f"{row['train_accuracy']:.3f} | {row['test_accuracy']:.3f} |"
            )
    return lines


def format_quotient_table(results: dict[str, dict]) -> list[str]:
    lines = [
        "| representation | k=2 | k=3 | k=4 | k=6 | k=12 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for rep_name, rep in results.items():
        cells = []
        for k in (2, 3, 4, 6, 12):
            row = rep["quotient_result_probes"][k]
            cells.append(f"{row['test_accuracy']:.3f}")
        lines.append(f"| {rep_name} | " + " | ".join(cells) + " |")
    return lines


def format_packet_table(results: dict[str, dict]) -> list[str]:
    conductors = sorted(conductor_packets(len(MONTHS)))
    lines = [
        "| representation | full-label test acc | " + " | ".join(f"H_{d}" for d in conductors) + " |",
        "|---|---:|" + "|".join("---:" for _ in conductors) + "|",
    ]
    for rep_name, rep in results.items():
        full = rep["full_result_probe"]
        fractions = full["packet_fractions"]
        cells = " | ".join(f"{fractions[d]:.6f}" for d in conductors)
        lines.append(f"| {rep_name} | {full['test_accuracy']:.3f} | {cells} |")
    return lines


def build_report(payload: dict[str, Any]) -> str:
    results = payload["representations"]
    lines = [
        f"# Hidden-State Shortcut Audit -- {payload['model_pretty']}",
        "",
        f"**Run date:** {payload['run_date']}",
        f"**Feature source:** `{payload['features_path']}`",
        f"**Dataset source:** `{payload['dataset_path']}`",
        f"**Split:** {payload['n_train']} train / {payload['n_test']} test "
        f"({payload['test_per_class']} held out per result month)",
        f"**Ridge alpha:** `{payload['alpha']}`",
        "",
        "## Experiment",
        "",
        "This audit uses per-example layer-28 hidden features rather than saved "
        "class centroids.  It is designed to test the base-10/input-side "
        "shortcut warning directly.  The `full hidden features` condition trains "
        "ordinary affine probes.  The `after source+offset residualization` "
        "condition first removes the linear subspace predicted by source month "
        "and offset number, fitting that residualizer only on the training fold.",
        "",
        "No quotient lift is used for the full-label result probe, so its packet "
        "fractions are not forced by T1.  Quotient-probe accuracies are also "
        "ordinary held-out accuracies, not projector identities.",
        "",
        "## Input-Side Target Decodability",
        "",
        *format_target_table(results),
        "",
        "## Result Quotient Probe Test Accuracy",
        "",
        *format_quotient_table(results),
        "",
        "## Full-Label Result-Probe Packet Fractions",
        "",
        *format_packet_table(results),
        "",
        "## Reading",
        "",
        "If result-month accuracy survives source+offset residualization, the "
        "hidden state contains a linearly accessible result code beyond a linear "
        "readout of the obvious input-side variables.  In these runs it survives "
        "and improves, so the linear input-shortcut alternative is falsified.  "
        "This does not rule out a nonlinear base-10 sum/carry mechanism, which "
        "requires the separate nonlinear ablation.  The packet fractions in the "
        "full-label probe are likewise empirical: unlike the quotient lift, an "
        "unconstrained twelve-class probe is allowed to place energy in any "
        "conductor packet.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--features",
        type=Path,
        default=Path("months/subspace/pca_k64/result/features/training_features.safetensors"),
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("months/subspace/pca_k64/result/train_dataset.json"),
    )
    parser.add_argument("--model-tag", default="llama31_8b")
    parser.add_argument("--model-pretty", default="Llama-3.1-8B")
    parser.add_argument("--alpha", type=float, default=1e-2)
    parser.add_argument("--test-per-class", type=int, default=2)
    parser.add_argument("--seed", type=int, default=20260516)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    features = np.asarray(load_safetensors(args.features), dtype=float)
    rows = load_rows(args.dataset)
    labels = labels_from_rows(rows)
    if features.shape[0] != len(rows):
        raise ValueError(f"Feature/row mismatch: {features.shape[0]} vs {len(rows)}")

    train_idx, test_idx = stratified_split(labels["result_month"], args.test_per_class, args.seed)
    x_train = features[train_idx]
    x_test = features[test_idx]

    z_train = covariate_matrix(labels, train_idx)
    z_test = covariate_matrix(labels, test_idx)
    residual_coef = fit_residualizer(x_train, z_train)
    x_train_resid = x_train - z_train @ residual_coef
    x_test_resid = x_test - z_test @ residual_coef

    representations = {
        "full hidden features": evaluate_representation(
            "full hidden features",
            x_train,
            x_test,
            labels,
            train_idx,
            test_idx,
            args.alpha,
        ),
        "after source+offset residualization": evaluate_representation(
            "after source+offset residualization",
            x_train_resid,
            x_test_resid,
            labels,
            train_idx,
            test_idx,
            args.alpha,
        ),
    }

    payload = {
        "run_date": date.today().isoformat(),
        "features_path": str(args.features),
        "dataset_path": str(args.dataset),
        "model_tag": args.model_tag,
        "model_pretty": args.model_pretty,
        "alpha": args.alpha,
        "seed": args.seed,
        "test_per_class": args.test_per_class,
        "n_train": int(train_idx.size),
        "n_test": int(test_idx.size),
        "train_indices": train_idx.tolist(),
        "test_indices": test_idx.tolist(),
        "representations": representations,
    }

    report_path = args.report or Path("empirical/reports") / f"months_hidden_state_shortcut_audit_{args.model_tag}.md"
    json_path = args.json or Path("empirical/reports") / f"months_hidden_state_shortcut_audit_{args.model_tag}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    for rep_name, rep in representations.items():
        full = rep["full_result_probe"]
        q = rep["quotient_result_probes"]
        fractions = full["packet_fractions"]
        print(
            f"{rep_name}: full_test={full['test_accuracy']:.3f} "
            f"k2={q[2]['test_accuracy']:.3f} k6={q[6]['test_accuracy']:.3f} "
            f"H12={fractions[12]:.3f}"
        )


if __name__ == "__main__":
    main()
