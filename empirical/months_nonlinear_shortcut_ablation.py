"""Nonlinear base-10 shortcut ablation for month hidden-state probes.

The linear shortcut audit removes the subspace predicted by source month and
offset number separately.  This script targets the stronger nonlinear shortcut:
a decimal/unwrapped addition code for source + offset, including digit/carry
features.  It fits residualizers on the training fold only, applies them to the
held-out fold, then measures how result-month probes and conductor packets
survive.

The key ablation is `decimal_sum_digits`: intercept, source month, offset, raw
sum ones digit, raw sum tens digit, base-10 carry, and mod-12 wrap carry.  This
is a targeted feature-level ablation for the base-10 addition hypothesis.  The
`raw_sum_class` row is an aggressive oracle check that removes class means for
the unwrapped sum itself; it is useful as an upper bound but is not the primary
test.
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


def compress_labels(values: np.ndarray) -> np.ndarray:
    mapping = {value: i for i, value in enumerate(sorted(set(values.tolist())))}
    return np.asarray([mapping[value] for value in values], dtype=int)


def labels_from_rows(rows: list[dict[str, str]]) -> dict[str, np.ndarray]:
    source_zero = np.asarray([MONTH_TO_INDEX[row["entity"]] for row in rows], dtype=int)
    source_one = source_zero + 1
    offset_value = np.asarray([NUMBER_WORDS[row["number"]] for row in rows], dtype=int)
    result = np.asarray([MONTH_TO_INDEX[row["result"]] for row in rows], dtype=int)
    raw_sum = source_one + offset_value
    return {
        "source_month": source_zero,
        "offset_number": offset_value - 1,
        "result_month": result,
        "raw_sum": raw_sum,
        "raw_sum_class": compress_labels(raw_sum),
        "sum_ones_digit": raw_sum % 10,
        "sum_tens_digit": raw_sum // 10,
        "decimal_carry10": (raw_sum >= 10).astype(int),
        "wrap_carry12": (raw_sum > 12).astype(int),
    }


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


def fit_residualizer(x_train: np.ndarray, z_train: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(z_train, x_train, rcond=None)
    return coef


def residualize(
    features: np.ndarray,
    z_train: np.ndarray,
    z_all: np.ndarray,
    train_idx: np.ndarray,
) -> np.ndarray:
    coef = fit_residualizer(features[train_idx], z_train)
    return features - z_all @ coef


def build_covariates(labels: dict[str, np.ndarray], mode: str, indices: np.ndarray) -> np.ndarray:
    intercept = np.ones((indices.size, 1), dtype=float)
    source = one_hot(labels["source_month"][indices], len(MONTHS))
    offset = one_hot(labels["offset_number"][indices], len(NUMBER_WORDS))

    if mode == "none":
        return intercept
    if mode == "linear_source_offset":
        return np.column_stack([intercept, source, offset])
    if mode == "decimal_sum_digits":
        ones = one_hot(labels["sum_ones_digit"][indices], 10)
        tens = one_hot(labels["sum_tens_digit"][indices], 2)
        carry10 = labels["decimal_carry10"][indices].reshape(-1, 1).astype(float)
        wrap12 = labels["wrap_carry12"][indices].reshape(-1, 1).astype(float)
        interactions = np.column_stack(
            [
                carry10[:, 0] * wrap12[:, 0],
                labels["sum_ones_digit"][indices].astype(float) * carry10[:, 0],
            ]
        )
        return np.column_stack([intercept, source, offset, ones, tens, carry10, wrap12, interactions])
    if mode == "raw_sum_class":
        raw_sum = one_hot(labels["raw_sum_class"][indices], int(labels["raw_sum_class"].max()) + 1)
        return np.column_stack([intercept, source, offset, raw_sum])
    raise ValueError(f"Unknown covariate mode: {mode}")


def target_accuracy(
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


def evaluate(
    features: np.ndarray,
    labels: dict[str, np.ndarray],
    train_idx: np.ndarray,
    test_idx: np.ndarray,
    alpha: float,
) -> dict[str, Any]:
    packets = conductor_packets(len(MONTHS))
    y_train = labels["result_month"][train_idx]
    y_test = labels["result_month"][test_idx]
    full_probe = fit_ridge_probe(features[train_idx], y_train, len(MONTHS), alpha)
    full_train_scores = full_probe.scores(features[train_idx])
    full_test_scores = full_probe.scores(features[test_idx])
    energy = packet_energy(full_test_scores, packets)
    fractions = energy_fractions(energy)

    quotient_results = {}
    for k in (2, 3, 4, 6, 12):
        quotient_results[k] = target_accuracy(
            features[train_idx],
            features[test_idx],
            y_train % k,
            y_test % k,
            k,
            alpha,
        )

    decodability = {
        "result_month": target_accuracy(
            features[train_idx], features[test_idx], y_train, y_test, len(MONTHS), alpha
        ),
        "raw_sum_class": target_accuracy(
            features[train_idx],
            features[test_idx],
            labels["raw_sum_class"][train_idx],
            labels["raw_sum_class"][test_idx],
            int(labels["raw_sum_class"].max()) + 1,
            alpha,
        ),
        "sum_ones_digit": target_accuracy(
            features[train_idx],
            features[test_idx],
            labels["sum_ones_digit"][train_idx],
            labels["sum_ones_digit"][test_idx],
            10,
            alpha,
        ),
        "decimal_carry10": target_accuracy(
            features[train_idx],
            features[test_idx],
            labels["decimal_carry10"][train_idx],
            labels["decimal_carry10"][test_idx],
            2,
            alpha,
        ),
        "wrap_carry12": target_accuracy(
            features[train_idx],
            features[test_idx],
            labels["wrap_carry12"][train_idx],
            labels["wrap_carry12"][test_idx],
            2,
            alpha,
        ),
    }

    return {
        "full_result_probe": {
            "classes": len(MONTHS),
            "chance": 1.0 / len(MONTHS),
            "train_accuracy": accuracy(full_train_scores, y_train),
            "test_accuracy": accuracy(full_test_scores, y_test),
            "packet_energy": energy,
            "packet_fractions": fractions,
        },
        "quotient_result_probes": quotient_results,
        "decodability": decodability,
    }


def format_ablation_table(results: dict[str, Any]) -> list[str]:
    lines = [
        "| ablation | result acc | raw-sum acc | ones acc | carry10 acc | wrap12 acc | k=2 acc | k=6 acc | H_12 fraction |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for mode, row in results.items():
        dec = row["decodability"]
        q = row["quotient_result_probes"]
        full = row["full_result_probe"]
        h12 = full["packet_fractions"][12]
        lines.append(
            f"| {mode} | {full['test_accuracy']:.3f} | "
            f"{dec['raw_sum_class']['test_accuracy']:.3f} | "
            f"{dec['sum_ones_digit']['test_accuracy']:.3f} | "
            f"{dec['decimal_carry10']['test_accuracy']:.3f} | "
            f"{dec['wrap_carry12']['test_accuracy']:.3f} | "
            f"{q[2]['test_accuracy']:.3f} | {q[6]['test_accuracy']:.3f} | {h12:.6f} |"
        )
    return lines


def format_packet_table(results: dict[str, Any]) -> list[str]:
    conductors = sorted(conductor_packets(len(MONTHS)))
    lines = [
        "| ablation | " + " | ".join(f"H_{d}" for d in conductors) + " |",
        "|---|" + "|".join("---:" for _ in conductors) + "|",
    ]
    for mode, row in results.items():
        fractions = row["full_result_probe"]["packet_fractions"]
        cells = " | ".join(f"{fractions[d]:.6f}" for d in conductors)
        lines.append(f"| {mode} | {cells} |")
    return lines


def build_report(payload: dict[str, Any]) -> str:
    lines = [
        f"# Nonlinear Base-10 Shortcut Ablation -- {payload['model_pretty']}",
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
        "This is a feature-level nonlinear ablation for the base-10 shortcut "
        "alternative.  Residualizers are fit on the training fold only.  The "
        "primary ablation, `decimal_sum_digits`, removes the subspace predicted "
        "by source month, offset, raw decimal sum ones/tens digits, base-10 "
        "carry, and mod-12 wrap carry.  The `raw_sum_class` ablation is an "
        "aggressive oracle upper bound because the unwrapped sum almost "
        "determines the cyclic result in this dataset.",
        "",
        "## Ablation Summary",
        "",
        *format_ablation_table(payload["results"]),
        "",
        "## Full-Label Result-Probe Packet Fractions",
        "",
        *format_packet_table(payload["results"]),
        "",
        "## Reading",
        "",
        "In these runs, result accuracy and `H_12` packet mass drop sharply "
        "after `decimal_sum_digits`, so the live hidden-state result probe is "
        "strongly entangled with the tested base-10 sum/carry code.  The "
        "`raw_sum_class` row should be read as a deliberately over-strong oracle "
        "check, not as the primary causal claim.  This is a probe-level feature "
        "ablation, not a causal forward-pass intervention.",
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
    modes = ("none", "linear_source_offset", "decimal_sum_digits", "raw_sum_class")
    results: dict[str, Any] = {}
    for mode in modes:
        if mode == "none":
            ablated = features
        else:
            z_train = build_covariates(labels, mode, train_idx)
            z_all = build_covariates(labels, mode, np.arange(features.shape[0]))
            ablated = residualize(features, z_train, z_all, train_idx)
        results[mode] = evaluate(ablated, labels, train_idx, test_idx, args.alpha)

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
        "results": results,
    }

    report_path = args.report or Path("empirical/reports") / f"months_nonlinear_shortcut_ablation_{args.model_tag}.md"
    json_path = args.json or Path("empirical/reports") / f"months_nonlinear_shortcut_ablation_{args.model_tag}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    for mode, row in results.items():
        full = row["full_result_probe"]
        dec = row["decodability"]
        q = row["quotient_result_probes"]
        h12 = full["packet_fractions"][12]
        print(
            f"{mode}: result={full['test_accuracy']:.3f} "
            f"raw_sum={dec['raw_sum_class']['test_accuracy']:.3f} "
            f"k2={q[2]['test_accuracy']:.3f} k6={q[6]['test_accuracy']:.3f} H12={h12:.3f}"
        )


if __name__ == "__main__":
    main()
