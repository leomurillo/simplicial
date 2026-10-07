"""Tiny calendar transformer test for update-only conductor projection.

This is the first training-loop integration of the F4[u]/(u^2) Pareto rule:

    gradient projection = 0%, update projection = 100%.

The script trains a small NumPy attention classifier on the checked-in
weekday/month calendar prompts.  It compares plain Adam with an output-head
Adam variant whose applied class-axis update is projected in the cyclic
character basis after the Adam moments are formed.  The stochastic gradient is
left untouched.  The projected arm also starts with its output head projected
into the same class-character support so that subsequent update projection has
a genuine invariant to preserve.

The existing calendar train/test JSON files are identical enumerations, so the
script builds its own deterministic holdout split before training.  Reports
include train/test metrics, the final generalization gap, and per-epoch
conductor-packet energy of the model logits.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Literal

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = Path(__file__).resolve().parent / "reports"

PRESETS: dict[str, tuple[str, ...]] = {
    "weekdays": (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ),
    "months": (
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
    ),
}

ORDINALS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
}
NUMBER_WORDS = {value: key for key, value in ORDINALS.items()}

Method = Literal["adam", "conductor_update"]


@dataclass(frozen=True)
class CalendarCase:
    prompt: str
    output: str
    label_index: int
    start_label: str
    offset: int


@dataclass(frozen=True)
class TrainingConfig:
    task: str = "months"
    seeds: int = 3
    seed_start: int = 9101
    split_mode: str = "random"
    split_seed: int = 4242
    train_fraction: float = 0.75
    train_offsets: str = "1-6"
    test_offsets: str = "7-12"
    epochs: int = 300
    batch_size: int = 16
    d_model: int = 32
    d_ff: int = 64
    lr: float = 0.0005
    beta1: float = 0.9
    beta2: float = 0.999
    adam_eps: float = 1e-8
    grad_clip: float = 1.0
    init_scale: float = 0.035
    closed_conductors: str = "primitive"


@dataclass(frozen=True)
class EpochMetrics:
    epoch: int
    train_loss: float
    test_loss: float
    train_accuracy: float
    test_accuracy: float
    logit_closed_energy: float
    logit_leak_energy: float
    logit_leakage: float
    update_leakage: float
    conductor_fractions: dict[str, float]
    gradient_packet_norms: dict[str, float]


@dataclass(frozen=True)
class MethodRun:
    seed: int
    method: Method
    final_train_loss: float
    final_test_loss: float
    final_train_accuracy: float
    final_test_accuracy: float
    final_generalization_gap: float
    final_accuracy_gap: float
    final_logit_leakage: float
    final_update_leakage: float
    closed_energy_growth: float
    leak_energy_growth: float
    history: list[EpochMetrics]


@dataclass(frozen=True)
class SummaryRow:
    method: Method
    train_loss_mean: float
    test_loss_mean: float
    generalization_gap_mean: float
    train_accuracy_mean: float
    test_accuracy_mean: float
    accuracy_gap_mean: float
    logit_leakage_mean: float
    update_leakage_mean: float
    closed_energy_growth_mean: float
    leak_energy_growth_mean: float


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conductor_packets(n: int) -> dict[int, list[int]]:
    packets: dict[int, list[int]] = {}
    for d in divisors(n):
        chars = [k for k in range(1, n) if n // math.gcd(n, k) == d]
        if chars:
            packets[d] = chars
    return packets


def parse_closed_conductors(spec: str, n: int) -> tuple[int, ...]:
    packets = conductor_packets(n)
    text = spec.strip().lower()
    if text in {"all", "full"}:
        return tuple(sorted(packets))
    if text in {"primitive", "max"}:
        return (max(packets),)
    if text in {"none", "zero"}:
        return ()
    out: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        value = int(part)
        if value not in packets:
            raise ValueError(f"conductor {value} is not present in C_{n}")
        out.append(value)
    if not out:
        raise ValueError("closed conductor set is empty")
    return tuple(sorted(set(out)))


def parse_offset_spec(spec: str) -> tuple[int, ...]:
    offsets: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            left_text, right_text = part.split("-", 1)
            left = int(left_text)
            right = int(right_text)
            if right < left:
                raise ValueError(f"offset range {part!r} is descending")
            offsets.update(range(left, right + 1))
        else:
            offsets.add(int(part))
    if not offsets:
        raise ValueError("offset list cannot be empty")
    if min(offsets) <= 0:
        raise ValueError("calendar offsets must be positive")
    missing_words = sorted(offset for offset in offsets if offset not in NUMBER_WORDS)
    if missing_words:
        raise ValueError(f"no prompt word is defined for offsets {missing_words}")
    return tuple(sorted(offsets))


def closed_character_mask(n: int, closed_conductors: tuple[int, ...]) -> np.ndarray:
    packets = conductor_packets(n)
    mask = np.zeros(n, dtype=bool)
    mask[0] = True
    for conductor in closed_conductors:
        mask[packets[conductor]] = True
    return mask


def center_rows(rows: np.ndarray) -> np.ndarray:
    return rows - np.mean(rows, axis=-1, keepdims=True)


def project_class_axis(rows: np.ndarray, closed_mask: np.ndarray) -> np.ndarray:
    """Project the final axis onto the selected cyclic character support."""

    n = rows.shape[-1]
    means = np.mean(rows, axis=-1, keepdims=True)
    centered = rows - means
    coeffs = np.fft.fft(centered, axis=-1) / math.sqrt(n)
    coeffs[..., ~closed_mask] = 0.0
    projected = np.fft.ifft(coeffs * math.sqrt(n), axis=-1).real
    return means + projected


def energy_split(rows: np.ndarray, closed_mask: np.ndarray) -> tuple[float, float, float]:
    n = rows.shape[-1]
    coeffs = np.fft.fft(center_rows(rows), axis=-1) / math.sqrt(n)
    energies = np.abs(coeffs) ** 2
    nontrivial = np.ones(n, dtype=bool)
    nontrivial[0] = False
    closed_nontrivial = closed_mask & nontrivial
    leak_mask = nontrivial & ~closed_mask
    closed = float(np.sum(energies[..., closed_nontrivial]))
    leak = float(np.sum(energies[..., leak_mask]))
    total = closed + leak
    leakage = 0.0 if total <= 1e-18 else leak / total
    return closed, leak, leakage


def conductor_fractions(rows: np.ndarray, n: int) -> dict[str, float]:
    coeffs = np.fft.fft(center_rows(rows), axis=-1) / math.sqrt(n)
    energies = np.abs(coeffs) ** 2
    packets = conductor_packets(n)
    raw = {
        str(conductor): float(np.sum(energies[..., indices]))
        for conductor, indices in packets.items()
    }
    total = sum(raw.values())
    if total <= 1e-18:
        return {key: 0.0 for key in raw}
    return {key: value / total for key, value in raw.items()}


def zero_packet_norms(n: int) -> dict[str, float]:
    return {str(conductor): 0.0 for conductor in conductor_packets(n)}


def output_gradient_packet_norms(grads: dict[str, np.ndarray], n: int) -> dict[str, float]:
    """L2 norms of output-head gradients by cyclic conductor packet."""

    rows = np.vstack([grads["wc"], grads["bc"][None, :]])
    coeffs = np.fft.fft(center_rows(rows), axis=-1) / math.sqrt(n)
    energies = np.abs(coeffs) ** 2
    return {
        str(conductor): math.sqrt(float(np.sum(energies[..., indices])))
        for conductor, indices in conductor_packets(n).items()
    }


def mean_packet_norms(items: list[dict[str, float]], n: int) -> dict[str, float]:
    if not items:
        return zero_packet_norms(n)
    keys = [str(conductor) for conductor in conductor_packets(n)]
    return {key: mean([item[key] for item in items]) for key in keys}


def make_case(task: str, start_index: int, offset: int) -> CalendarCase:
    labels = PRESETS[task]
    label = labels[start_index]
    output = labels[(start_index + offset) % len(labels)]
    noun = "day" if task == "weekdays" else "month"
    unit = "days" if task == "weekdays" else "months"
    prompt = f"Q: What {noun} is {NUMBER_WORDS[offset]} {unit} after {label}?\nA:"
    return CalendarCase(
        prompt=prompt,
        output=output,
        label_index=(start_index + offset) % len(labels),
        start_label=label,
        offset=offset,
    )


def load_cases(task: str, required_offsets: tuple[int, ...] | None = None) -> tuple[list[CalendarCase], int, int]:
    labels = PRESETS[task]
    label_index = {label.lower(): index for index, label in enumerate(labels)}
    path = ROOT / task / "baseline" / "train_samples.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    pattern = re.compile(
        r"What (?:day|month) is ([a-z]+) (?:days|months?) after ([A-Za-z]+)\?",
        re.IGNORECASE,
    )
    cases: list[CalendarCase] = []
    seen: set[tuple[str, int]] = set()
    for sample in payload["samples"]:
        prompt = str(sample["raw_input"])
        output = str(sample["raw_output"]).strip()
        match = pattern.search(prompt)
        if not match:
            raise ValueError(f"cannot parse calendar prompt: {prompt!r}")
        ordinal, start_label = match.groups()
        offset = ORDINALS[ordinal.lower()]
        key = output.lower()
        if key not in label_index:
            raise ValueError(f"unknown output label {output!r} for task {task}")
        case = CalendarCase(
            prompt=prompt,
            output=output,
            label_index=label_index[key],
            start_label=start_label,
            offset=offset,
        )
        cases.append(case)
        seen.add((start_label, offset))

    checked_in_count = len(cases)
    if required_offsets is not None:
        for start_index, label in enumerate(labels):
            for offset in required_offsets:
                if (label, offset) not in seen:
                    cases.append(make_case(task, start_index, offset))
                    seen.add((label, offset))
    generated_count = len(cases) - checked_in_count
    return cases, checked_in_count, generated_count


def build_split(
    cases: list[CalendarCase],
    train_fraction: float,
    split_seed: int,
    split_mode: str,
    train_offsets: tuple[int, ...],
    test_offsets: tuple[int, ...],
) -> tuple[np.ndarray, np.ndarray]:
    if split_mode == "offset_ood":
        overlap = set(train_offsets) & set(test_offsets)
        if overlap:
            raise ValueError(f"train/test offsets overlap: {sorted(overlap)}")
        train = np.array(
            [index for index, case in enumerate(cases) if case.offset in train_offsets],
            dtype=np.int32,
        )
        test = np.array(
            [index for index, case in enumerate(cases) if case.offset in test_offsets],
            dtype=np.int32,
        )
        if len(train) == 0 or len(test) == 0:
            raise ValueError(
                f"empty offset split: train={len(train)} test={len(test)}"
            )
        return train, test
    if split_mode != "random":
        raise ValueError(f"unknown split mode {split_mode!r}")
    rng = np.random.default_rng(split_seed)
    indices = np.arange(len(cases))
    rng.shuffle(indices)
    train_size = int(round(train_fraction * len(cases)))
    train_size = min(max(1, train_size), len(cases) - 1)
    train = np.sort(indices[:train_size])
    test = np.sort(indices[train_size:])
    return train, test


def build_vocab(cases: list[CalendarCase]) -> dict[str, int]:
    chars = sorted({char for case in cases for char in case.prompt})
    vocab = {"<pad>": 0}
    for char in chars:
        vocab[char] = len(vocab)
    return vocab


@dataclass(frozen=True)
class EncodedData:
    inputs: np.ndarray
    mask: np.ndarray
    last_index: np.ndarray
    labels: np.ndarray
    vocab: dict[str, int]


def encode_cases(cases: list[CalendarCase], vocab: dict[str, int]) -> EncodedData:
    max_len = max(len(case.prompt) for case in cases)
    inputs = np.zeros((len(cases), max_len), dtype=np.int32)
    mask = np.zeros((len(cases), max_len), dtype=bool)
    labels = np.array([case.label_index for case in cases], dtype=np.int32)
    last_index = np.zeros(len(cases), dtype=np.int32)
    for row, case in enumerate(cases):
        ids = [vocab[char] for char in case.prompt]
        inputs[row, : len(ids)] = ids
        mask[row, : len(ids)] = True
        last_index[row] = len(ids) - 1
    return EncodedData(inputs=inputs, mask=mask, last_index=last_index, labels=labels, vocab=vocab)


def xavier(rng: np.random.Generator, shape: tuple[int, ...], scale: float) -> np.ndarray:
    if len(shape) < 2:
        return rng.normal(0.0, scale, size=shape)
    fan = shape[0] + shape[1]
    std = math.sqrt(2.0 / fan)
    return rng.normal(0.0, std, size=shape)


def init_params(
    seed: int,
    vocab_size: int,
    max_len: int,
    n_classes: int,
    config: TrainingConfig,
) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(seed)
    d = config.d_model
    return {
        "token_embed": rng.normal(0.0, config.init_scale, size=(vocab_size, d)),
        "pos_embed": rng.normal(0.0, config.init_scale, size=(max_len, d)),
        "wq": xavier(rng, (d, d), config.init_scale),
        "wk": xavier(rng, (d, d), config.init_scale),
        "wv": xavier(rng, (d, d), config.init_scale),
        "wo": xavier(rng, (d, d), config.init_scale),
        "w1": xavier(rng, (d, config.d_ff), config.init_scale),
        "b1": np.zeros(config.d_ff),
        "w2": xavier(rng, (config.d_ff, d), config.init_scale),
        "b2": np.zeros(d),
        "wc": xavier(rng, (d, n_classes), config.init_scale),
        "bc": np.zeros(n_classes),
    }


def clone_params(params: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    return {key: value.copy() for key, value in params.items()}


def softmax(rows: np.ndarray) -> np.ndarray:
    centered = rows - np.max(rows, axis=-1, keepdims=True)
    exp = np.exp(centered)
    return exp / np.sum(exp, axis=-1, keepdims=True)


def forward(
    params: dict[str, np.ndarray],
    inputs: np.ndarray,
    mask: np.ndarray,
    last_index: np.ndarray,
    labels: np.ndarray | None = None,
    need_cache: bool = False,
) -> tuple[np.ndarray, float | None, dict[str, np.ndarray] | None]:
    batch, seq_len = inputs.shape
    positions = np.arange(seq_len)
    x = params["token_embed"][inputs] + params["pos_embed"][positions][None, :, :]
    x = x * mask[..., None]
    xq = x[np.arange(batch), last_index]
    q = xq @ params["wq"]
    k = x @ params["wk"]
    v = x @ params["wv"]
    scores = np.einsum("bd,bld->bl", q, k) / math.sqrt(q.shape[1])
    scores = np.where(mask, scores, -1.0e9)
    attn = softmax(scores)
    context = np.einsum("bl,bld->bd", attn, v)
    out = context @ params["wo"]
    h0 = xq + out
    z1 = h0 @ params["w1"] + params["b1"]
    h1 = np.tanh(z1)
    ff = h1 @ params["w2"] + params["b2"]
    hidden_pre = h0 + ff
    hidden = np.tanh(hidden_pre)
    logits = hidden @ params["wc"] + params["bc"]

    loss: float | None = None
    probs: np.ndarray | None = None
    if labels is not None:
        probs = softmax(logits)
        loss = float(-np.mean(np.log(np.maximum(probs[np.arange(batch), labels], 1e-12))))

    cache = None
    if need_cache:
        if labels is None or probs is None:
            raise ValueError("labels are required when need_cache=True")
        cache = {
            "inputs": inputs,
            "mask": mask,
            "last_index": last_index,
            "labels": labels,
            "x": x,
            "xq": xq,
            "q": q,
            "k": k,
            "v": v,
            "attn": attn,
            "context": context,
            "h0": h0,
            "z1": z1,
            "h1": h1,
            "ff": ff,
            "hidden_pre": hidden_pre,
            "hidden": hidden,
            "probs": probs,
        }
    return logits, loss, cache


def backward(params: dict[str, np.ndarray], cache: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    inputs = cache["inputs"]
    mask = cache["mask"]
    last_index = cache["last_index"]
    labels = cache["labels"]
    x = cache["x"]
    xq = cache["xq"]
    q = cache["q"]
    k = cache["k"]
    v = cache["v"]
    attn = cache["attn"]
    context = cache["context"]
    h0 = cache["h0"]
    h1 = cache["h1"]
    hidden = cache["hidden"]
    probs = cache["probs"].copy()

    batch = inputs.shape[0]
    d_model = params["wq"].shape[0]
    grads = {key: np.zeros_like(value) for key, value in params.items()}

    dlogits = probs
    dlogits[np.arange(batch), labels] -= 1.0
    dlogits /= float(batch)

    grads["wc"] += hidden.T @ dlogits
    grads["bc"] += np.sum(dlogits, axis=0)
    dhidden = dlogits @ params["wc"].T

    dhidden_pre = dhidden * (1.0 - hidden * hidden)
    dh0 = dhidden_pre.copy()
    dff = dhidden_pre

    grads["w2"] += h1.T @ dff
    grads["b2"] += np.sum(dff, axis=0)
    dh1 = dff @ params["w2"].T
    dz1 = dh1 * (1.0 - h1 * h1)

    grads["w1"] += h0.T @ dz1
    grads["b1"] += np.sum(dz1, axis=0)
    dh0 += dz1 @ params["w1"].T

    dxq = dh0.copy()
    dout = dh0
    grads["wo"] += context.T @ dout
    dcontext = dout @ params["wo"].T

    dattn = np.einsum("bd,bld->bl", dcontext, v)
    dv = attn[..., None] * dcontext[:, None, :]
    dscores = attn * (dattn - np.sum(dattn * attn, axis=1, keepdims=True))
    dscores = np.where(mask, dscores, 0.0)

    scale = 1.0 / math.sqrt(d_model)
    dq = np.einsum("bl,bld->bd", dscores, k) * scale
    dk = dscores[..., None] * q[:, None, :] * scale

    grads["wq"] += xq.T @ dq
    dxq += dq @ params["wq"].T
    grads["wk"] += np.einsum("bld,ble->de", x, dk)
    grads["wv"] += np.einsum("bld,ble->de", x, dv)

    dx = dk @ params["wk"].T + dv @ params["wv"].T
    np.add.at(dx, (np.arange(batch), last_index), dxq)
    dx *= mask[..., None]

    np.add.at(grads["token_embed"], inputs.reshape(-1), dx.reshape(-1, d_model))
    grads["pos_embed"][: inputs.shape[1]] += np.sum(dx, axis=0)
    return grads


def clip_gradients(grads: dict[str, np.ndarray], max_norm: float) -> float:
    norm = math.sqrt(sum(float(np.sum(value * value)) for value in grads.values()))
    if max_norm > 0.0 and norm > max_norm:
        scale = max_norm / max(norm, 1e-12)
        for key in grads:
            grads[key] *= scale
    return norm


def adam_step(
    params: dict[str, np.ndarray],
    grads: dict[str, np.ndarray],
    state: dict[str, Any],
    config: TrainingConfig,
    method: Method,
    closed_mask: np.ndarray,
) -> float:
    state["t"] += 1
    update_rows: list[np.ndarray] = []
    for key, value in params.items():
        state["m"][key] = config.beta1 * state["m"][key] + (1.0 - config.beta1) * grads[key]
        state["v"][key] = config.beta2 * state["v"][key] + (1.0 - config.beta2) * grads[key] * grads[key]
        m_hat = state["m"][key] / (1.0 - config.beta1 ** state["t"])
        v_hat = state["v"][key] / (1.0 - config.beta2 ** state["t"])
        step = -config.lr * m_hat / (np.sqrt(v_hat) + config.adam_eps)
        if method == "conductor_update" and key == "wc":
            step = project_class_axis(step, closed_mask)
        elif method == "conductor_update" and key == "bc":
            step = project_class_axis(step[None, :], closed_mask)[0]
        if key == "wc":
            update_rows.append(step)
        elif key == "bc":
            update_rows.append(step[None, :])
        value += step

    if not update_rows:
        return 0.0
    _, _, leakage = energy_split(np.vstack(update_rows), closed_mask)
    return leakage


def init_adam_state(params: dict[str, np.ndarray]) -> dict[str, Any]:
    return {
        "t": 0,
        "m": {key: np.zeros_like(value) for key, value in params.items()},
        "v": {key: np.zeros_like(value) for key, value in params.items()},
    }


def minibatches(
    n_items: int,
    epochs: int,
    batch_size: int,
    seed: int,
) -> list[list[np.ndarray]]:
    rng = np.random.default_rng(seed + 77_777)
    batches: list[list[np.ndarray]] = []
    for _ in range(epochs):
        order = np.arange(n_items)
        rng.shuffle(order)
        batches.append([order[start : start + batch_size] for start in range(0, n_items, batch_size)])
    return batches


def evaluate(
    params: dict[str, np.ndarray],
    data: EncodedData,
    indices: np.ndarray,
) -> tuple[float, float, np.ndarray]:
    logits, loss, _ = forward(
        params,
        data.inputs[indices],
        data.mask[indices],
        data.last_index[indices],
        data.labels[indices],
        need_cache=False,
    )
    predictions = np.argmax(logits, axis=1)
    accuracy = float(np.mean(predictions == data.labels[indices]))
    assert loss is not None
    return loss, accuracy, logits


def epoch_metrics(
    epoch: int,
    params: dict[str, np.ndarray],
    data: EncodedData,
    train_indices: np.ndarray,
    test_indices: np.ndarray,
    n_classes: int,
    closed_mask: np.ndarray,
    update_leakages: list[float],
    gradient_packet_norms: dict[str, float] | None = None,
) -> EpochMetrics:
    train_loss, train_acc, train_logits = evaluate(params, data, train_indices)
    test_loss, test_acc, test_logits = evaluate(params, data, test_indices)
    all_logits = np.vstack([train_logits, test_logits])
    closed, leak, logit_leakage = energy_split(all_logits, closed_mask)
    update_leakage = float(np.mean(update_leakages)) if update_leakages else 0.0
    return EpochMetrics(
        epoch=epoch,
        train_loss=train_loss,
        test_loss=test_loss,
        train_accuracy=train_acc,
        test_accuracy=test_acc,
        logit_closed_energy=closed,
        logit_leak_energy=leak,
        logit_leakage=logit_leakage,
        update_leakage=update_leakage,
        conductor_fractions=conductor_fractions(all_logits, n_classes),
        gradient_packet_norms=gradient_packet_norms or zero_packet_norms(n_classes),
    )


def run_method(
    method: Method,
    seed: int,
    initial_params: dict[str, np.ndarray],
    data: EncodedData,
    train_indices: np.ndarray,
    test_indices: np.ndarray,
    batches: list[list[np.ndarray]],
    n_classes: int,
    config: TrainingConfig,
    closed_mask: np.ndarray,
) -> MethodRun:
    params = clone_params(initial_params)
    if method == "conductor_update":
        params["wc"] = project_class_axis(params["wc"], closed_mask)
        params["bc"] = project_class_axis(params["bc"][None, :], closed_mask)[0]
    state = init_adam_state(params)
    history: list[EpochMetrics] = [
        epoch_metrics(0, params, data, train_indices, test_indices, n_classes, closed_mask, [])
    ]

    for epoch in range(1, config.epochs + 1):
        update_leakages = []
        gradient_packet_norm_items: list[dict[str, float]] = []
        for local_batch in batches[epoch - 1]:
            batch_indices = train_indices[local_batch]
            _, _, cache = forward(
                params,
                data.inputs[batch_indices],
                data.mask[batch_indices],
                data.last_index[batch_indices],
                data.labels[batch_indices],
                need_cache=True,
            )
            assert cache is not None
            grads = backward(params, cache)
            gradient_packet_norm_items.append(output_gradient_packet_norms(grads, n_classes))
            clip_gradients(grads, config.grad_clip)
            update_leakages.append(adam_step(params, grads, state, config, method, closed_mask))
        history.append(
            epoch_metrics(
                epoch,
                params,
                data,
                train_indices,
                test_indices,
                n_classes,
                closed_mask,
                update_leakages,
                mean_packet_norms(gradient_packet_norm_items, n_classes),
            )
        )

    first = history[0]
    final = history[-1]
    return MethodRun(
        seed=seed,
        method=method,
        final_train_loss=final.train_loss,
        final_test_loss=final.test_loss,
        final_train_accuracy=final.train_accuracy,
        final_test_accuracy=final.test_accuracy,
        final_generalization_gap=final.test_loss - final.train_loss,
        final_accuracy_gap=final.train_accuracy - final.test_accuracy,
        final_logit_leakage=final.logit_leakage,
        final_update_leakage=final.update_leakage,
        closed_energy_growth=final.logit_closed_energy - first.logit_closed_energy,
        leak_energy_growth=final.logit_leak_energy - first.logit_leak_energy,
        history=history,
    )


def mean(values: list[float]) -> float:
    return float(np.mean(values)) if values else float("nan")


def summarize(runs: list[MethodRun]) -> list[SummaryRow]:
    rows = []
    for method in ("adam", "conductor_update"):
        selected = [run for run in runs if run.method == method]
        rows.append(
            SummaryRow(
                method=method,  # type: ignore[arg-type]
                train_loss_mean=mean([run.final_train_loss for run in selected]),
                test_loss_mean=mean([run.final_test_loss for run in selected]),
                generalization_gap_mean=mean([run.final_generalization_gap for run in selected]),
                train_accuracy_mean=mean([run.final_train_accuracy for run in selected]),
                test_accuracy_mean=mean([run.final_test_accuracy for run in selected]),
                accuracy_gap_mean=mean([run.final_accuracy_gap for run in selected]),
                logit_leakage_mean=mean([run.final_logit_leakage for run in selected]),
                update_leakage_mean=mean([run.final_update_leakage for run in selected]),
                closed_energy_growth_mean=mean([run.closed_energy_growth for run in selected]),
                leak_energy_growth_mean=mean([run.leak_energy_growth for run in selected]),
            )
        )
    return rows


def method_label(method: Method) -> str:
    if method == "adam":
        return "Adam"
    return "update-only conductor Adam"


def fmt(value: float) -> str:
    if abs(value) >= 1000.0 or (abs(value) < 1e-4 and value != 0.0):
        return f"{value:.3e}"
    return f"{value:.6f}"


def json_ready(value: Any) -> Any:
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
        return round(value, 12)
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    return value


def markdown_report(
    config: TrainingConfig,
    labels: tuple[str, ...],
    cases: list[CalendarCase],
    checked_in_count: int,
    generated_count: int,
    train_indices: np.ndarray,
    test_indices: np.ndarray,
    train_offsets: tuple[int, ...],
    test_offsets: tuple[int, ...],
    closed_conductors: tuple[int, ...],
    summary: list[SummaryRow],
    runs: list[MethodRun],
    json_path: Path,
) -> str:
    packets = conductor_packets(len(labels))
    by_method = {row.method: row for row in summary}
    adam = by_method["adam"]
    conductor = by_method["conductor_update"]
    gap_delta = conductor.generalization_gap_mean - adam.generalization_gap_mean
    acc_delta = conductor.test_accuracy_mean - adam.test_accuracy_mean
    leakage_delta = conductor.logit_leakage_mean - adam.logit_leakage_mean
    if config.split_mode == "offset_ood":
        split_note = [
            "This run uses an offset-OOD split: training examples use only the",
            "declared train offsets, while test examples use offsets never seen",
            "during training.  Missing calendar offsets are generated from the",
            "exact cyclic label rule before tokenization.",
        ]
    else:
        split_note = [
            "The checked-in calendar train/test files are identical enumerations, so",
            "this run uses a deterministic holdout split before training.  This makes",
            "the generalization gap a real held-out-case measurement rather than a",
            "copy of the training score.",
        ]

    lines = [
        f"# Calendar Transformer Conductor Filter ({config.task})",
        "",
        "## Verdict",
        "",
        "This is a small real-sequence training-loop pilot for the Pareto rule",
        "`gradient projection 0%, update projection 100%`.  The model is a",
        "trainable character-level attention classifier over the checked-in",
        f"{config.task} prompts; only the output-head Adam update is projected",
        "in the cyclic character basis.",
        "The projected arm starts with the output head in the same support,",
        "then leaves the stochastic gradient and all Adam moments unprojected.",
        "",
        f"- test accuracy delta vs Adam: `{acc_delta:+.6f}`",
        f"- generalization-gap delta vs Adam: `{gap_delta:+.6f}`",
        f"- final logit-leakage delta vs Adam: `{leakage_delta:+.6f}`",
        f"- JSON payload: `{json_path}`",
        "",
        *split_note,
        "",
        "## Setup",
        "",
        f"- task: `{config.task}`",
        f"- labels: `{', '.join(labels)}`",
        f"- cases: `{len(cases)}`",
        f"- checked-in/generated cases: `{checked_in_count}` / `{generated_count}`",
        f"- split mode: `{config.split_mode}`",
        f"- train offsets: `{', '.join(str(x) for x in train_offsets)}`",
        f"- test offsets: `{', '.join(str(x) for x in test_offsets)}`",
        f"- train/test split: `{len(train_indices)}` / `{len(test_indices)}`",
        f"- seeds: `{config.seeds}` starting at `{config.seed_start}`",
        f"- epochs: `{config.epochs}`",
        f"- batch size: `{config.batch_size}`",
        f"- model width / FF width: `{config.d_model}` / `{config.d_ff}`",
        f"- learning rate: `{config.lr}`",
        f"- closed conductors: `{', '.join(str(x) for x in closed_conductors)}`",
        "",
        "## Character Packets",
        "",
        "| conductor | character indices | kept by filter |",
        "|---:|---|---|",
    ]
    for conductor, chars in packets.items():
        kept = "yes" if conductor in closed_conductors else "no"
        lines.append(f"| {conductor} | `{', '.join(str(x) for x in chars)}` | {kept} |")

    lines += [
        "",
        "## Final Metrics",
        "",
        "| method | train loss | test loss | gen gap | train acc | test acc | acc gap | final logit leakage | output-update leakage | closed energy growth | leak energy growth |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| {method_label(row.method)} | "
            f"{fmt(row.train_loss_mean)} | "
            f"{fmt(row.test_loss_mean)} | "
            f"{fmt(row.generalization_gap_mean)} | "
            f"{fmt(row.train_accuracy_mean)} | "
            f"{fmt(row.test_accuracy_mean)} | "
            f"{fmt(row.accuracy_gap_mean)} | "
            f"{fmt(row.logit_leakage_mean)} | "
            f"{fmt(row.update_leakage_mean)} | "
            f"{fmt(row.closed_energy_growth_mean)} | "
            f"{fmt(row.leak_energy_growth_mean)} |"
        )

    lines += [
        "",
        "## Per-Seed Results",
        "",
        "| seed | method | train loss | test loss | gen gap | train acc | test acc | final leakage |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for run in runs:
        lines.append(
            f"| {run.seed} | {method_label(run.method)} | "
            f"{fmt(run.final_train_loss)} | "
            f"{fmt(run.final_test_loss)} | "
            f"{fmt(run.final_generalization_gap)} | "
            f"{fmt(run.final_train_accuracy)} | "
            f"{fmt(run.final_test_accuracy)} | "
            f"{fmt(run.final_logit_leakage)} |"
        )

    lines += [
        "",
        "## Per-Epoch Energy Trace",
        "",
        "Values below are seed means over the logits on all calendar cases.",
        "",
        "| epoch | method | closed energy | leak energy | leakage |",
        "|---:|---|---:|---:|---:|",
    ]

    epoch_marks = sorted(set([0, 1, config.epochs // 4, config.epochs // 2, config.epochs]))
    for epoch in epoch_marks:
        for method in ("adam", "conductor_update"):
            selected = [run.history[epoch] for run in runs if run.method == method]
            lines.append(
                f"| {epoch} | {method_label(method)} | "
                f"{fmt(mean([item.logit_closed_energy for item in selected]))} | "
                f"{fmt(mean([item.logit_leak_energy for item in selected]))} | "
                f"{fmt(mean([item.logit_leakage for item in selected]))} |"
            )

    packet_keys = [str(conductor) for conductor in packets]
    lines += [
        "",
        "## Per-Epoch Output Gradient Packet Norms",
        "",
        "Values are seed means of the mean minibatch output-head gradient L2",
        "norms before gradient clipping.  These gradients are not projected in",
        "the conductor arm; only the resulting Adam update is filtered.",
        "",
        "| epoch | method | " + " | ".join(f"cond {key}" for key in packet_keys) + " |",
        "|---:|---|" + "|".join("---:" for _ in packet_keys) + "|",
    ]
    for epoch in epoch_marks:
        for method in ("adam", "conductor_update"):
            selected = [run.history[epoch] for run in runs if run.method == method]
            values = [
                fmt(mean([item.gradient_packet_norms[key] for item in selected]))
                for key in packet_keys
            ]
            lines.append(f"| {epoch} | {method_label(method)} | " + " | ".join(values) + " |")

    lines += [
        "",
        "## Reading",
        "",
        "The filter is deliberately output-side: it does not modify the stochastic",
        "gradient, and it does not constrain the attention or feed-forward weights.",
        "Only the applied class-axis update is projected after Adam's moment",
        "calculation.",
        "For C12 the closed packet choice is a modeling assumption, not a theorem.",
        "The useful object produced here is the harness plus a first held-out",
        "measurement of how much accuracy/generalization is paid for a declared",
        "class-character update filter.",
        "",
        "## Reproduction",
        "",
        "```powershell",
        (
            "python empirical/conductor_calendar_transformer.py "
            f"--task {config.task} "
            f"--split-mode {config.split_mode} "
            f"--train-offsets {config.train_offsets} "
            f"--test-offsets {config.test_offsets} "
            f"--closed-conductors {config.closed_conductors} "
            f"--epochs {config.epochs} "
            f"--batch-size {config.batch_size} "
            f"--d-model {config.d_model} "
            f"--d-ff {config.d_ff} "
            f"--lr {config.lr}"
        ),
        "```",
        "",
    ]
    return "\n".join(lines)


def run_experiment(config: TrainingConfig) -> tuple[
    tuple[str, ...],
    list[CalendarCase],
    int,
    int,
    np.ndarray,
    np.ndarray,
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
    list[SummaryRow],
    list[MethodRun],
]:
    labels = PRESETS[config.task]
    n_classes = len(labels)
    train_offsets = parse_offset_spec(config.train_offsets)
    test_offsets = parse_offset_spec(config.test_offsets)
    required_offsets = (
        tuple(sorted(set(train_offsets) | set(test_offsets)))
        if config.split_mode == "offset_ood"
        else None
    )
    cases, checked_in_count, generated_count = load_cases(config.task, required_offsets)
    train_indices, test_indices = build_split(
        cases,
        config.train_fraction,
        config.split_seed,
        config.split_mode,
        train_offsets,
        test_offsets,
    )
    vocab = build_vocab(cases)
    data = encode_cases(cases, vocab)
    closed_conductors = parse_closed_conductors(config.closed_conductors, n_classes)
    closed_mask = closed_character_mask(n_classes, closed_conductors)
    runs: list[MethodRun] = []

    for offset in range(config.seeds):
        seed = config.seed_start + offset
        initial = init_params(seed, len(vocab), data.inputs.shape[1], n_classes, config)
        batches = minibatches(len(train_indices), config.epochs, config.batch_size, seed)
        for method in ("adam", "conductor_update"):
            runs.append(
                run_method(
                    method,  # type: ignore[arg-type]
                    seed,
                    initial,
                    data,
                    train_indices,
                    test_indices,
                    batches,
                    n_classes,
                    config,
                    closed_mask,
                )
            )
    return (
        labels,
        cases,
        checked_in_count,
        generated_count,
        train_indices,
        test_indices,
        train_offsets,
        test_offsets,
        closed_conductors,
        summarize(runs),
        runs,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=sorted(PRESETS), default=TrainingConfig.task)
    parser.add_argument("--seeds", type=int, default=TrainingConfig.seeds)
    parser.add_argument("--seed-start", type=int, default=TrainingConfig.seed_start)
    parser.add_argument("--split-mode", choices=["random", "offset_ood"], default=TrainingConfig.split_mode)
    parser.add_argument("--split-seed", type=int, default=TrainingConfig.split_seed)
    parser.add_argument("--train-fraction", type=float, default=TrainingConfig.train_fraction)
    parser.add_argument("--train-offsets", default=TrainingConfig.train_offsets)
    parser.add_argument("--test-offsets", default=TrainingConfig.test_offsets)
    parser.add_argument("--epochs", type=int, default=TrainingConfig.epochs)
    parser.add_argument("--batch-size", type=int, default=TrainingConfig.batch_size)
    parser.add_argument("--d-model", type=int, default=TrainingConfig.d_model)
    parser.add_argument("--d-ff", type=int, default=TrainingConfig.d_ff)
    parser.add_argument("--lr", type=float, default=TrainingConfig.lr)
    parser.add_argument("--grad-clip", type=float, default=TrainingConfig.grad_clip)
    parser.add_argument("--closed-conductors", default=TrainingConfig.closed_conductors)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = TrainingConfig(
        task=args.task,
        seeds=args.seeds,
        seed_start=args.seed_start,
        split_mode=args.split_mode,
        split_seed=args.split_seed,
        train_fraction=args.train_fraction,
        train_offsets=args.train_offsets,
        test_offsets=args.test_offsets,
        epochs=args.epochs,
        batch_size=args.batch_size,
        d_model=args.d_model,
        d_ff=args.d_ff,
        lr=args.lr,
        grad_clip=args.grad_clip,
        closed_conductors=args.closed_conductors,
    )
    (
        labels,
        cases,
        checked_in_count,
        generated_count,
        train_indices,
        test_indices,
        train_offsets,
        test_offsets,
        closed_conductors,
        summary,
        runs,
    ) = run_experiment(config)

    split_suffix = "_offset_ood" if config.split_mode == "offset_ood" else ""
    report_path = args.report or REPORT_DIR / f"conductor_calendar_transformer_{config.task}{split_suffix}.md"
    json_path = args.json or REPORT_DIR / f"conductor_calendar_transformer_{config.task}{split_suffix}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "config": asdict(config),
        "labels": labels,
        "case_counts": {
            "total": len(cases),
            "checked_in": checked_in_count,
            "generated": generated_count,
        },
        "split": {
            "mode": config.split_mode,
            "train_offsets": train_offsets,
            "test_offsets": test_offsets,
            "train_indices": train_indices.tolist(),
            "test_indices": test_indices.tolist(),
            "train_cases": [asdict(cases[index]) for index in train_indices],
            "test_cases": [asdict(cases[index]) for index in test_indices],
        },
        "character_packets": conductor_packets(len(labels)),
        "closed_conductors": closed_conductors,
        "summary": [asdict(row) for row in summary],
        "runs": [asdict(run) for run in runs],
    }
    json_path.write_text(json.dumps(json_ready(payload), indent=2), encoding="utf-8")
    report_path.write_text(
        markdown_report(
            config,
            labels,
            cases,
            checked_in_count,
            generated_count,
            train_indices,
            test_indices,
            train_offsets,
            test_offsets,
            closed_conductors,
            summary,
            runs,
            json_path,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(
        json.dumps(
            json_ready(
                {
                    row.method: {
                        "test_loss": row.test_loss_mean,
                        "generalization_gap": row.generalization_gap_mean,
                        "test_accuracy": row.test_accuracy_mean,
                        "final_logit_leakage": row.logit_leakage_mean,
                    }
                    for row in summary
                }
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
