"""Train quotient-tied linear probes and score their conductor packets.

This is the concrete T2/T3 instantiation for the local month activation
features.  For each quotient size k | 12, the script trains an affine ridge
probe from hidden features to k quotient labels, lifts the k logits back to the
full C_12 label space by pullback, and decomposes the lifted logits into cyclic
conductor packets.

The lifted forbidden-packet zeros are analytic consequences of the pullback.
The non-tautological quantities are the held-out accuracies retained by each
coarse, packet-blind probe.
"""

from __future__ import annotations

import argparse
import json
import math
import struct
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import numpy as np


EPS = 1e-12
DEFAULT_QUOTIENTS = (2, 3, 4, 6, 12)
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
    dtype_map = {"F64": np.float64, "F32": np.float32, "F16": np.float16}
    if meta["dtype"] not in dtype_map:
        raise ValueError(f"Unsupported dtype for this probe script: {meta['dtype']}")
    start, end = meta["data_offsets"]
    return np.frombuffer(data[start:end], dtype=dtype_map[meta["dtype"]]).reshape(meta["shape"]).copy()


def load_month_labels(path: Path) -> np.ndarray:
    rows = json.loads(path.read_text(encoding="utf-8"))
    labels = []
    for row in rows:
        result = row["input"]["result"]
        if result not in MONTH_TO_INDEX:
            raise ValueError(f"Unknown month label: {result}")
        labels.append(MONTH_TO_INDEX[result])
    return np.asarray(labels, dtype=int)


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


def fit_ridge_probe(
    features: np.ndarray,
    labels: np.ndarray,
    n_classes: int,
    alpha: float,
) -> RidgeProbe:
    mean = features.mean(axis=0)
    scale = features.std(axis=0)
    scale = np.where(scale < EPS, 1.0, scale)
    x = (features - mean) / scale
    x_aug = np.column_stack([x, np.ones(x.shape[0])])
    y = one_hot(labels, n_classes)
    reg = alpha * np.eye(x_aug.shape[1])
    reg[-1, -1] = 0.0
    weights = np.linalg.solve(x_aug.T @ x_aug + reg, x_aug.T @ y)
    return RidgeProbe(mean=mean, scale=scale, weights=weights)


def accuracy(scores: np.ndarray, labels: np.ndarray) -> float:
    return float(np.mean(np.argmax(scores, axis=1) == labels))


def conductor_packets(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {}
    for character in range(1, n):
        conductor = n // math.gcd(n, character)
        packets.setdefault(conductor, []).append(character)
    return {d: packets[d] for d in sorted(packets)}


def lift_quotient_scores(scores: np.ndarray, n: int, k: int) -> np.ndarray:
    """Pull back C_k scores to C_n using q_k(x mod n) = x mod k."""

    full = np.zeros((scores.shape[0], n), dtype=float)
    for label in range(n):
        full[:, label] = scores[:, label % k]
    return full


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
    return {d: value / total for d, value in energy.items()}


def proper_forbidden_fraction(
    fractions: dict[int, float],
    energy: dict[int, float],
    k: int,
    n: int,
) -> tuple[float, float]:
    forbidden = [d for d in fractions if k % d != 0]
    if not forbidden:
        return 0.0, 0.0
    total_forbidden_fraction = sum(fractions[d] for d in forbidden)
    max_forbidden_energy = max(abs(energy[d]) for d in forbidden)
    return float(total_forbidden_fraction), float(max_forbidden_energy)


def format_packet_table(rows: dict[int, dict[int, float]]) -> list[str]:
    conductors = sorted(next(iter(rows.values())))
    lines = ["| quotient k | " + " | ".join(f"H_{d}" for d in conductors) + " |"]
    lines.append("|---:|" + "|".join("---:" for _ in conductors) + "|")
    for k in sorted(rows):
        values = " | ".join(f"{rows[k][d]:.6f}" for d in conductors)
        lines.append(f"| {k} | {values} |")
    return lines


def format_accuracy_table(results: dict[int, dict]) -> list[str]:
    lines = [
        "| quotient k | train acc | test acc | analytic forbidden fraction | analytic max forbidden energy | allowed packets | forbidden packets |",
        "|---:|---:|---:|---:|---:|---|---|",
    ]
    for k in sorted(results):
        row = results[k]
        lines.append(
            f"| {k} | {row['train_accuracy']:.3f} | {row['test_accuracy']:.3f} | "
            f"{row['forbidden_fraction']:.3e} | {row['max_forbidden_energy']:.3e} | "
            f"{', '.join(row['allowed_packets']) or 'none'} | "
            f"{', '.join(row['forbidden_packets']) or 'none'} |"
        )
    return lines


def build_report(payload: dict) -> str:
    results = payload["results"]
    packet_fractions = {int(k): v["packet_fractions"] for k, v in results.items()}
    lines = [
        f"# Quotient-Tied Linear Probe Packet Score -- {payload['model_pretty']}",
        "",
        f"**Run date:** {payload['run_date']}",
        f"**Feature source:** `{payload['features_path']}`",
        f"**Dataset source:** `{payload['dataset_path']}`",
        f"**Split:** {payload['n_train']} train / {payload['n_test']} test "
        f"({payload['test_per_class']} held out per month)",
        f"**Ridge alpha:** `{payload['alpha']}`",
        "",
        "## Experiment",
        "",
        "For each quotient `k | 12`, an affine ridge probe is trained from the "
        "saved layer-28 PCA-64 month features to the coarse label `month mod k`. "
        "The `k` probe logits are lifted back to twelve labels by pullback "
        "`score_12[x] = score_k[x mod k]`, then the held-out lifted logits are "
        "decomposed into cyclic conductor packets.",
        "",
        "This is an actual trained quotient probe/lens instantiation of T2/T3, "
        "but the lifted forbidden-packet zeros are analytic consequences of "
        "the pullback `q^*`, not independent model evidence.  The empirical "
        "content is the held-out accuracy retained while the probe is forced "
        "to use a packet-blind coarse codomain.",
        "",
        "## Probe Accuracy And Analytic Forbidden-Energy Check",
        "",
        *format_accuracy_table({int(k): v for k, v in results.items()}),
        "",
        "## Held-Out Lifted-Logit Packet Fractions",
        "",
        *format_packet_table(packet_fractions),
        "",
        "## Reading",
        "",
        "The numerical-zero forbidden energy is a sanity check that the lifted "
        "scores really lie in the quotient subspace.  It should not be counted "
        "as evidence about the model: once the script sets "
        "`score_12[x] = score_k[x mod k]`, T1 already forces those entries to "
        "zero.",
        "",
        "The evidence is instead in the accuracies.  A coarse quotient probe can "
        "retain real held-out behavior while being algebraically blind to high "
        "conductor packets.  The full `k = 12` probe is the escape hatch: because "
        "its target is the full label algebra, the conductor obstruction does "
        "not remove any packet.",
        "",
        "## Insights",
        "",
        "1. Accuracy and packet visibility decouple.  A quotient probe can be "
        "accurate on its coarse target while still being exactly blind to packets "
        "outside the quotient algebra.",
        "2. Bias and ridge tuning do not matter for the obstruction.  They change "
        "the function inside `L^2(C_k)`, but the pullback remains inside the "
        "quotient subspace.",
        "3. A poor full-label probe would not refute T2.  The theorem says the "
        "full codomain permits all packets, not that a particular training run "
        "must learn all of them.",
        "4. The stronger native final-logit version is supplied by "
        "`native_logit_lens_binning_packet_score.py`.  The remaining stronger "
        "variant is a true tuned lens across intermediate layers, packet-scored "
        "before and after quotient binning.",
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
    parser.add_argument(
        "--quotients",
        default=",".join(str(k) for k in DEFAULT_QUOTIENTS),
    )
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    n = 12
    quotients = [int(part.strip()) for part in args.quotients.split(",") if part.strip()]
    bad = [k for k in quotients if n % k != 0]
    if bad:
        raise ValueError(f"All quotients must divide {n}; got {bad}")

    features = np.asarray(load_safetensors(args.features), dtype=float)
    labels = load_month_labels(args.dataset)
    if features.shape[0] != labels.size:
        raise ValueError(f"Feature/label mismatch: {features.shape[0]} vs {labels.size}")

    train_idx, test_idx = stratified_split(labels, args.test_per_class, args.seed)
    packets = conductor_packets(n)

    results: dict[int, dict] = {}
    for k in quotients:
        y_train = labels[train_idx] % k
        y_test = labels[test_idx] % k
        probe = fit_ridge_probe(features[train_idx], y_train, k, args.alpha)
        train_scores = probe.scores(features[train_idx])
        test_scores = probe.scores(features[test_idx])
        lifted = lift_quotient_scores(test_scores, n, k)
        energy = packet_energy(lifted, packets)
        fractions = energy_fractions(energy)
        forbidden_fraction, max_forbidden_energy = proper_forbidden_fraction(fractions, energy, k, n)
        allowed = [f"H_{d}" for d in packets if k % d == 0]
        forbidden = [f"H_{d}" for d in packets if k % d != 0]
        results[k] = {
            "target_classes": k,
            "train_accuracy": accuracy(train_scores, y_train),
            "test_accuracy": accuracy(test_scores, y_test),
            "packet_energy": energy,
            "packet_fractions": fractions,
            "forbidden_fraction": forbidden_fraction,
            "max_forbidden_energy": max_forbidden_energy,
            "allowed_packets": allowed,
            "forbidden_packets": forbidden,
        }

    payload = {
        "run_date": date.today().isoformat(),
        "features_path": str(args.features),
        "dataset_path": str(args.dataset),
        "model_tag": args.model_tag,
        "model_pretty": args.model_pretty,
        "n_labels": n,
        "quotients": quotients,
        "alpha": args.alpha,
        "seed": args.seed,
        "test_per_class": args.test_per_class,
        "n_train": int(train_idx.size),
        "n_test": int(test_idx.size),
        "train_indices": train_idx.tolist(),
        "test_indices": test_idx.tolist(),
        "results": results,
    }

    report_path = args.report or Path("empirical/reports") / f"quotient_probe_packet_score_months_{args.model_tag}.md"
    json_path = args.json or Path("empirical/reports") / f"quotient_probe_packet_score_months_{args.model_tag}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    for k in quotients:
        row = results[k]
        print(
            f"k={k:2d} train_acc={row['train_accuracy']:.3f} "
            f"test_acc={row['test_accuracy']:.3f} "
            f"forbidden_fraction={row['forbidden_fraction']:.3e}"
        )


if __name__ == "__main__":
    main()
