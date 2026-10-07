#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper 37 (α, ε) Substitution Sweep on the Months Task
=====================================================

Pre-registered protocol: 37_label_smoothing_in_the_conductor_blind_spot.md §4.
This script is the audit λ driver for the V/M empirical bridge specified in
v2insert-06.md.  The V/M aggregation step is in
empirical/label_smoothing_substitution_sweep_VM_binning.py.

ANCHORED [P] OBJECTS
--------------------
* Months task on ℤ/12: input is (start month index, offset 1..11) → target
  (start + offset) mod 12.  Paper 12 setup; same prompts as
  empirical/conductor_calendar_transformer.py.
* Character-level attention classifier model; widths W ∈ {16, 32, 64}.
* Label-smoothed cross-entropy:
      q_ε(c|y) = (1-ε)·δ_{c,y} + ε/N        (Paper 37 §2.1)
      L_ε(θ) = -Σ q_ε(c|y) · log p_θ(x)_c
  Gradient with respect to logits: ∇_z L_ε = p_θ - q_ε.
* Pareto rule with strength α ∈ [0,1] (Paper 37 §2.2):
      U_α(g) = (1-α) g + α · P_S g
  where g is the Adam-preconditioned descent direction and P_S is the
  orthogonal projector onto the closed packet support S in the character
  basis of the output-layer logit row.  α = 0 is plain Adam; α = 1 is the
  Paper 12 "update-projection 100%" rule.
* Closed packet support S = {12} per Paper 37 §4.1 / Paper 12 §7.4.1.

PAPER 12 ANCHOR (Paper 37 §7; F2 falsifier)
-------------------------------------------
At W=32, S={12}:
    (α=0, ε=0)  →  test loss ≈ 6.125 (Paper 12 §7.4.1)
    (α=1, ε=0)  →  test loss ≈ 4.0514 (Paper 12 §7.4.1; primary anchor)
Note: Paper 37 §1 cites 9.0838 as the (α=0, ε=0, W=32) reference; this
appears to be a transcription of Paper 12's W=64 row, which Paper 12
reports at 9.0838.  We honor the Paper 12 §7.4.1 anchor as listed there.
Falsifier band: |G(α=1, ε=0, W=32) - 4.0514| would put us outside [3.5, 4.5].

CHARACTER PACKETS ON ℤ/12 (Paper 36 §2.3; Paper 12 §7.4.1)
----------------------------------------------------------
Conductor packets H_d (d ∈ {2, 3, 4, 6, 12}):
    d = 2:  characters {6}                       (single prime, prime 2)
    d = 3:  characters {4, 8}                    (single prime, prime 3)
    d = 4:  characters {3, 9}                    (prime-power 2² on prime 2)
    d = 6:  characters {2, 10}                   (cross-prime carry 2·3)
    d = 12: characters {1, 5, 7, 11}             (cross-prime carry 2²·3)

V/M binning (v2insert-06 §2):
    V (single-prime / prime-power)  = H_2 + H_3 + H_4
    M (cross-prime carry)           = H_6 + H_12
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import numpy as np


SCRIPT_VERSION = "audit_lambda_v0.1_2026_05_20"

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = Path(__file__).resolve().parent / "reports"


MONTH_LABELS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)

ORDINALS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
}
NUMBER_WORDS = {value: key for key, value in ORDINALS.items()}


# ------------------------------------------------------------------ #
# Conductor / character bookkeeping                                  #
# ------------------------------------------------------------------ #

def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def conductor_packets(n: int) -> dict[int, list[int]]:
    """Map conductor d -> list of character indices k in {1..n-1} with n/gcd(n,k) = d."""
    packets: dict[int, list[int]] = {}
    for d in divisors(n):
        chars = [k for k in range(1, n) if n // math.gcd(n, k) == d]
        if chars:
            packets[d] = chars
    return packets


def closed_character_mask(n: int, closed: tuple[int, ...]) -> np.ndarray:
    """Boolean character-basis mask: keep trivial (index 0) plus selected conductor packets."""
    packets = conductor_packets(n)
    mask = np.zeros(n, dtype=bool)
    mask[0] = True
    for c in closed:
        if c not in packets:
            raise ValueError(f"conductor {c} is not present in C_{n}")
        mask[packets[c]] = True
    return mask


def center_rows(rows: np.ndarray) -> np.ndarray:
    return rows - np.mean(rows, axis=-1, keepdims=True)


def project_class_axis(rows: np.ndarray, closed_mask: np.ndarray) -> np.ndarray:
    """Project the final axis onto the selected cyclic character support.
    Same operator as empirical/conductor_calendar_transformer.py:project_class_axis.
    """
    n = rows.shape[-1]
    means = np.mean(rows, axis=-1, keepdims=True)
    centered = rows - means
    coeffs = np.fft.fft(centered, axis=-1) / math.sqrt(n)
    coeffs[..., ~closed_mask] = 0.0
    projected = np.fft.ifft(coeffs * math.sqrt(n), axis=-1).real
    return means + projected


def packet_energies(rows: np.ndarray, n: int) -> dict[int, float]:
    """Raw nontrivial-character energy by conductor packet.
    rows: shape (..., n).  Returns dict d -> Σ_{k∈H_d} |hat_k|^2 (in unitary-FFT
    convention with /sqrt(n) normalization), summed over leading axes.
    """
    coeffs = np.fft.fft(center_rows(rows), axis=-1) / math.sqrt(n)
    energies = np.abs(coeffs) ** 2
    packets = conductor_packets(n)
    out: dict[int, float] = {}
    for d, ks in packets.items():
        out[d] = float(np.sum(energies[..., ks]))
    return out


def packet_fractions(rows: np.ndarray, n: int) -> dict[int, float]:
    """f_d := Σ |hat_k|^2 / Σ_{k≠0} |hat_k|^2 = packet d's fraction of nontrivial energy.
    This is Paper 36 §2.3's logit packet-fraction on the model-facing logits
    (centroid-removed character basis).  Returns 0.0 for all d if no nontrivial energy.
    """
    raw = packet_energies(rows, n)
    total = sum(raw.values())
    if total <= 1e-30:
        return {d: 0.0 for d in raw}
    return {d: e / total for d, e in raw.items()}


def energy_split(rows: np.ndarray, closed_mask: np.ndarray) -> tuple[float, float, float]:
    """Closed-nontrivial energy, leak energy, fractional leakage."""
    n = rows.shape[-1]
    coeffs = np.fft.fft(center_rows(rows), axis=-1) / math.sqrt(n)
    energies = np.abs(coeffs) ** 2
    nontrivial = np.ones(n, dtype=bool)
    nontrivial[0] = False
    closed_nt = closed_mask & nontrivial
    leak_mask = nontrivial & ~closed_mask
    closed = float(np.sum(energies[..., closed_nt]))
    leak = float(np.sum(energies[..., leak_mask]))
    total = closed + leak
    leakage = 0.0 if total <= 1e-30 else leak / total
    return closed, leak, leakage


# ------------------------------------------------------------------ #
# Months task: prompts, encoding, splits                             #
# ------------------------------------------------------------------ #

@dataclass(frozen=True)
class CalendarCase:
    prompt: str
    label_index: int
    start_label: str
    offset: int


def make_case(start_index: int, offset: int) -> CalendarCase:
    label = MONTH_LABELS[start_index]
    out = (start_index + offset) % len(MONTH_LABELS)
    prompt = f"Q: What month is {NUMBER_WORDS[offset]} months after {label}?\nA:"
    return CalendarCase(prompt=prompt, label_index=out, start_label=label, offset=offset)


def build_cases(load_from_json: bool = True) -> list[CalendarCase]:
    """Load the 84 checked-in months cases from months/baseline/train_samples.json
    (Paper 12 / conductor_calendar_transformer.py canonical setup).  Offsets in
    the JSON are 1..7; the 84 = 12 × 7 = months × offsets.
    If load_from_json=False, generate the full 12 × 11 = 132 grid.
    """
    import re as _re
    if load_from_json:
        path = ROOT / "months" / "baseline" / "train_samples.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        label_index = {label.lower(): i for i, label in enumerate(MONTH_LABELS)}
        pattern = _re.compile(
            r"What month is ([a-z]+) months? after ([A-Za-z]+)\?", _re.IGNORECASE,
        )
        cases: list[CalendarCase] = []
        for sample in payload["samples"]:
            prompt = str(sample["raw_input"])
            output = str(sample["raw_output"]).strip()
            m = pattern.search(prompt)
            if not m:
                raise ValueError(f"cannot parse: {prompt!r}")
            ordinal, start_label = m.groups()
            offset = ORDINALS[ordinal.lower()]
            cases.append(CalendarCase(
                prompt=prompt, label_index=label_index[output.lower()],
                start_label=start_label, offset=offset,
            ))
        return cases
    cases = []
    for start in range(len(MONTH_LABELS)):
        for offset in range(1, 12):
            cases.append(make_case(start, offset))
    return cases


def build_vocab(cases: list[CalendarCase]) -> dict[str, int]:
    chars = sorted({c for case in cases for c in case.prompt})
    vocab = {"<pad>": 0}
    for c in chars:
        vocab[c] = len(vocab)
    return vocab


@dataclass(frozen=True)
class EncodedData:
    inputs: np.ndarray
    mask: np.ndarray
    last_index: np.ndarray
    labels: np.ndarray
    vocab: dict[str, int]


def encode(cases: list[CalendarCase], vocab: dict[str, int]) -> EncodedData:
    max_len = max(len(c.prompt) for c in cases)
    inp = np.zeros((len(cases), max_len), dtype=np.int32)
    msk = np.zeros((len(cases), max_len), dtype=bool)
    lab = np.array([c.label_index for c in cases], dtype=np.int32)
    last = np.zeros(len(cases), dtype=np.int32)
    for r, c in enumerate(cases):
        ids = [vocab[ch] for ch in c.prompt]
        inp[r, :len(ids)] = ids
        msk[r, :len(ids)] = True
        last[r] = len(ids) - 1
    return EncodedData(inputs=inp, mask=msk, last_index=last, labels=lab, vocab=vocab)


def random_split(n: int, train_fraction: float, split_seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(split_seed)
    idx = np.arange(n)
    rng.shuffle(idx)
    n_train = int(round(train_fraction * n))
    n_train = min(max(1, n_train), n - 1)
    train = np.sort(idx[:n_train])
    test = np.sort(idx[n_train:])
    return train, test


# ------------------------------------------------------------------ #
# Model (matches conductor_calendar_transformer.py forward/backward) #
# ------------------------------------------------------------------ #

@dataclass(frozen=True)
class TrainConfig:
    width: int = 32              # d_model
    ff_factor: int = 2           # d_ff = ff_factor * d_model
    epochs: int = 300
    batch_size: int = 16
    lr: float = 5e-4
    beta1: float = 0.9
    beta2: float = 0.999
    adam_eps: float = 1e-8
    grad_clip: float = 1.0
    init_scale: float = 0.035
    split_seed: int = 4242
    train_fraction: float = 0.75


def xavier(rng: np.random.Generator, shape: tuple[int, ...], scale: float) -> np.ndarray:
    if len(shape) < 2:
        return rng.normal(0.0, scale, size=shape)
    fan = shape[0] + shape[1]
    std = math.sqrt(2.0 / fan)
    return rng.normal(0.0, std, size=shape)


def init_params(seed: int, vocab_size: int, max_len: int, n_classes: int, cfg: TrainConfig) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(seed)
    d = cfg.width
    d_ff = cfg.ff_factor * d
    return {
        "token_embed": rng.normal(0.0, cfg.init_scale, size=(vocab_size, d)),
        "pos_embed":   rng.normal(0.0, cfg.init_scale, size=(max_len, d)),
        "wq": xavier(rng, (d, d), cfg.init_scale),
        "wk": xavier(rng, (d, d), cfg.init_scale),
        "wv": xavier(rng, (d, d), cfg.init_scale),
        "wo": xavier(rng, (d, d), cfg.init_scale),
        "w1": xavier(rng, (d, d_ff), cfg.init_scale),
        "b1": np.zeros(d_ff),
        "w2": xavier(rng, (d_ff, d), cfg.init_scale),
        "b2": np.zeros(d),
        "wc": xavier(rng, (d, n_classes), cfg.init_scale),
        "bc": np.zeros(n_classes),
    }


def clone(params: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    return {k: v.copy() for k, v in params.items()}


def softmax(rows: np.ndarray) -> np.ndarray:
    s = rows - np.max(rows, axis=-1, keepdims=True)
    e = np.exp(s)
    return e / np.sum(e, axis=-1, keepdims=True)


def forward(
    params: dict[str, np.ndarray],
    inputs: np.ndarray, mask: np.ndarray, last_index: np.ndarray,
    labels: np.ndarray | None = None,
    epsilon: float = 0.0,
    need_cache: bool = False,
) -> tuple[np.ndarray, float | None, dict[str, np.ndarray] | None]:
    """Returns logits, label-smoothed loss (if labels given), cache (if needed)."""
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
        n_classes = logits.shape[1]
        # Label-smoothed cross-entropy: q_ε(c|y) = (1-ε)·δ_{c,y} + ε/N
        # L_ε = -Σ_c q_ε log p_c = -(1-ε) log p_y - (ε/N) Σ_c log p_c.
        log_probs = np.log(np.maximum(probs, 1e-12))
        true_term = log_probs[np.arange(batch), labels]
        smooth_term = np.sum(log_probs, axis=-1) / n_classes
        per_example = -((1.0 - epsilon) * true_term + epsilon * smooth_term)
        loss = float(np.mean(per_example))

    cache: dict[str, np.ndarray] | None = None
    if need_cache:
        if labels is None or probs is None:
            raise ValueError("labels required for cache")
        cache = {
            "inputs": inputs, "mask": mask, "last_index": last_index, "labels": labels,
            "x": x, "xq": xq, "q": q, "k": k, "v": v, "attn": attn, "context": context,
            "h0": h0, "z1": z1, "h1": h1, "ff": ff, "hidden_pre": hidden_pre,
            "hidden": hidden, "probs": probs,
            "epsilon": np.asarray(epsilon),
        }
    return logits, loss, cache


def backward(params: dict[str, np.ndarray], cache: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    """Backprop with label-smoothed CE.
    dL/dlogits = p - q_ε  where q_ε = (1-ε)·e_y + (ε/N)·1.
    """
    inputs = cache["inputs"]; mask = cache["mask"]; last_index = cache["last_index"]
    labels = cache["labels"]
    x = cache["x"]; xq = cache["xq"]; q = cache["q"]; k = cache["k"]; v = cache["v"]
    attn = cache["attn"]; context = cache["context"]
    h0 = cache["h0"]; h1 = cache["h1"]; hidden = cache["hidden"]
    probs = cache["probs"].copy()
    epsilon = float(cache["epsilon"])

    batch = inputs.shape[0]
    n_classes = probs.shape[1]
    d_model = params["wq"].shape[0]
    grads = {key: np.zeros_like(value) for key, value in params.items()}

    # dL/dlogits = p - q_ε
    q_eps = np.full_like(probs, epsilon / n_classes)
    q_eps[np.arange(batch), labels] += (1.0 - epsilon)
    dlogits = probs - q_eps
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
    norm = math.sqrt(sum(float(np.sum(v * v)) for v in grads.values()))
    if max_norm > 0.0 and norm > max_norm:
        s = max_norm / max(norm, 1e-12)
        for k in grads:
            grads[k] *= s
    return norm


def adam_step_alpha(
    params: dict[str, np.ndarray],
    grads: dict[str, np.ndarray],
    state: dict[str, Any],
    cfg: TrainConfig,
    alpha: float,
    closed_mask: np.ndarray,
) -> float:
    """Adam update with Paper 37 §2.2 Pareto rule U_α(g) = (1-α)g + α P_S g
    applied to the output-head update (wc, bc) only.  α ∈ [0,1]; α=0 is plain
    Adam; α=1 is Paper 12's update-projection 100%.
    Returns the leakage of the applied (wc, bc) update.
    """
    state["t"] += 1
    update_rows: list[np.ndarray] = []
    for key, value in params.items():
        state["m"][key] = cfg.beta1 * state["m"][key] + (1.0 - cfg.beta1) * grads[key]
        state["v"][key] = cfg.beta2 * state["v"][key] + (1.0 - cfg.beta2) * grads[key] * grads[key]
        m_hat = state["m"][key] / (1.0 - cfg.beta1 ** state["t"])
        v_hat = state["v"][key] / (1.0 - cfg.beta2 ** state["t"])
        step = -cfg.lr * m_hat / (np.sqrt(v_hat) + cfg.adam_eps)
        if key == "wc":
            proj = project_class_axis(step, closed_mask)
            step = (1.0 - alpha) * step + alpha * proj
            update_rows.append(step)
        elif key == "bc":
            proj = project_class_axis(step[None, :], closed_mask)[0]
            step = (1.0 - alpha) * step + alpha * proj
            update_rows.append(step[None, :])
        value += step

    if not update_rows:
        return 0.0
    _, _, leakage = energy_split(np.vstack(update_rows), closed_mask)
    return leakage


def init_adam_state(params: dict[str, np.ndarray]) -> dict[str, Any]:
    return {
        "t": 0,
        "m": {k: np.zeros_like(v) for k, v in params.items()},
        "v": {k: np.zeros_like(v) for k, v in params.items()},
    }


def minibatches(n: int, epochs: int, batch_size: int, seed: int) -> list[list[np.ndarray]]:
    rng = np.random.default_rng(seed + 77_777)
    out: list[list[np.ndarray]] = []
    for _ in range(epochs):
        order = np.arange(n)
        rng.shuffle(order)
        out.append([order[s:s + batch_size] for s in range(0, n, batch_size)])
    return out


# ------------------------------------------------------------------ #
# Evaluation / metrics                                                #
# ------------------------------------------------------------------ #

def eval_loss_acc(
    params: dict[str, np.ndarray], data: EncodedData, indices: np.ndarray,
    epsilon: float = 0.0,
) -> tuple[float, float, np.ndarray]:
    """Evaluate at given indices.  Note: test loss uses ε=0 (held-out true-class
    NLL is the reportable test-loss metric per Paper 37 §4.4)."""
    logits, loss, _ = forward(
        params, data.inputs[indices], data.mask[indices], data.last_index[indices],
        data.labels[indices], epsilon=epsilon, need_cache=False,
    )
    pred = np.argmax(logits, axis=1)
    acc = float(np.mean(pred == data.labels[indices]))
    assert loss is not None
    return loss, acc, logits


def ece_from_logits(logits: np.ndarray, labels: np.ndarray, n_bins: int = 10) -> float:
    """Expected calibration error at uniform binning of max-prob."""
    probs = softmax(logits)
    conf = np.max(probs, axis=1)
    pred = np.argmax(probs, axis=1)
    correct = (pred == labels).astype(float)
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0
    n = labels.shape[0]
    for i in range(n_bins):
        lo, hi = bins[i], bins[i + 1]
        if i == n_bins - 1:
            sel = (conf >= lo) & (conf <= hi)
        else:
            sel = (conf >= lo) & (conf < hi)
        ns = int(np.sum(sel))
        if ns == 0:
            continue
        avg_conf = float(np.mean(conf[sel]))
        avg_acc = float(np.mean(correct[sel]))
        ece += (ns / n) * abs(avg_conf - avg_acc)
    return ece


# ------------------------------------------------------------------ #
# Single run                                                          #
# ------------------------------------------------------------------ #

@dataclass(frozen=True)
class RunResult:
    width: int
    alpha: float
    epsilon: float
    seed: int
    final_train_loss: float
    final_test_loss: float
    final_train_acc: float
    final_test_acc: float
    gen_gap: float
    ece_test: float
    leakage_logit: float
    leakage_update_mean: float
    packet_fractions_logit: dict[int, float]
    packet_fractions_logit_test_only: dict[int, float]
    sigma_V: float
    sigma_M: float
    rho_VM: float


def run_single(
    width: int,
    alpha: float,
    epsilon: float,
    seed: int,
    data: EncodedData,
    train_idx: np.ndarray,
    test_idx: np.ndarray,
    closed_conductors: tuple[int, ...],
    cfg: TrainConfig,
    vocab_size: int,
    max_len: int,
    n_classes: int,
    log_prefix: str = "",
) -> RunResult:
    closed_mask = closed_character_mask(n_classes, closed_conductors)

    # Initialize, then project output head into S at start (per Paper 12 protocol
    # for α>0; we project only when α>0 to keep α=0 strictly equal to plain Adam).
    params = init_params(seed, vocab_size, max_len, n_classes, cfg)
    if alpha > 0.0:
        params["wc"] = project_class_axis(params["wc"], closed_mask)
        params["bc"] = project_class_axis(params["bc"][None, :], closed_mask)[0]

    state = init_adam_state(params)
    batches = minibatches(len(train_idx), cfg.epochs, cfg.batch_size, seed)

    update_leakages: list[float] = []
    for epoch in range(1, cfg.epochs + 1):
        for local in batches[epoch - 1]:
            bi = train_idx[local]
            _, _, cache = forward(
                params, data.inputs[bi], data.mask[bi], data.last_index[bi],
                data.labels[bi], epsilon=epsilon, need_cache=True,
            )
            assert cache is not None
            grads = backward(params, cache)
            clip_gradients(grads, cfg.grad_clip)
            update_leakages.append(adam_step_alpha(params, grads, state, cfg, alpha, closed_mask))

    # Final-epoch evaluation
    # Per Paper 37 §4.4 the primary outcome is the held-out test cross-entropy
    # with respect to the true labels (NOT label-smoothed). We report ε=0 test loss.
    train_loss, train_acc, train_logits = eval_loss_acc(params, data, train_idx, epsilon=0.0)
    test_loss, test_acc, test_logits = eval_loss_acc(params, data, test_idx, epsilon=0.0)
    all_logits = np.vstack([train_logits, test_logits])
    _, _, leakage_logit = energy_split(all_logits, closed_mask)

    ece = ece_from_logits(test_logits, data.labels[test_idx])

    # Packet fractions on logits (all-cases vs test-only)
    pf_all = packet_fractions(all_logits, n_classes)
    pf_test = packet_fractions(test_logits, n_classes)

    sigma_V = pf_all.get(2, 0.0) + pf_all.get(3, 0.0) + pf_all.get(4, 0.0)
    sigma_M = pf_all.get(6, 0.0) + pf_all.get(12, 0.0)
    rho_VM = (sigma_V / sigma_M) if sigma_M > 1e-30 else float("inf")

    return RunResult(
        width=width, alpha=alpha, epsilon=epsilon, seed=seed,
        final_train_loss=train_loss, final_test_loss=test_loss,
        final_train_acc=train_acc, final_test_acc=test_acc,
        gen_gap=test_loss - train_loss, ece_test=ece,
        leakage_logit=leakage_logit,
        leakage_update_mean=float(np.mean(update_leakages)) if update_leakages else 0.0,
        packet_fractions_logit=pf_all,
        packet_fractions_logit_test_only=pf_test,
        sigma_V=sigma_V, sigma_M=sigma_M, rho_VM=rho_VM,
    )


# ------------------------------------------------------------------ #
# Sweep driver                                                        #
# ------------------------------------------------------------------ #

def parse_list_float(text: str) -> list[float]:
    return [float(x) for x in text.split(",") if x.strip()]


def parse_list_int(text: str) -> list[int]:
    return [int(x) for x in text.split(",") if x.strip()]


def parse_closed(text: str) -> tuple[int, ...]:
    return tuple(sorted({int(x) for x in text.split(",") if x.strip()}))


def main() -> None:
    # Reconfigure stdout for UTF-8 if possible (Windows cp1252 default cannot
    # encode σ, ρ, α, ε used in print statements).
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="Paper 37 (alpha, eps) sweep -- audit lambda driver")
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--alphas", type=str, default="0,0.25,0.5,0.75,1.0")
    parser.add_argument("--epsilons", type=str, default="0,0.03,0.06,0.1,0.15,0.2")
    parser.add_argument("--seeds", type=str, default="9101,9102,9103")
    parser.add_argument("--support", type=str, default="12", help="Closed conductor support (Paper 37 §4.1)")
    parser.add_argument("--epochs", type=int, default=300)
    parser.add_argument("--task", type=str, default="months")
    parser.add_argument("--output-dir", type=str, default=str(REPORT_DIR))
    parser.add_argument("--anchor-only", action="store_true",
                        help="Run only the Paper 12 anchor configuration (α=1, ε=0)")
    args = parser.parse_args()

    if args.task != "months":
        raise ValueError("audit λ is months-only per Paper 37 §4.1")

    width = args.width
    alphas = parse_list_float(args.alphas)
    epsilons = parse_list_float(args.epsilons)
    seeds = parse_list_int(args.seeds)
    closed = parse_closed(args.support)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cfg = TrainConfig(width=width, epochs=args.epochs)

    # Setup task once
    cases = build_cases()
    vocab = build_vocab(cases)
    data = encode(cases, vocab)
    train_idx, test_idx = random_split(len(cases), cfg.train_fraction, cfg.split_seed)
    vocab_size = len(vocab)
    max_len = data.inputs.shape[1]
    n_classes = 12

    print(f"# label_smoothing_substitution_sweep version {SCRIPT_VERSION}")
    print(f"# task=months N=12  width={width}  epochs={cfg.epochs}  batch={cfg.batch_size}")
    print(f"# closed support S = {closed}")
    print(f"# alphas = {alphas}")
    print(f"# epsilons = {epsilons}")
    print(f"# seeds = {seeds}")
    print(f"# train/test = {len(train_idx)} / {len(test_idx)}")
    print(f"# split_seed = {cfg.split_seed}")
    print(f"# total cases = {len(cases)}")
    print(f"# closed_character_mask = {closed_character_mask(n_classes, closed).astype(int).tolist()}")
    print()

    if args.anchor_only:
        configs = [(1.0, 0.0)]
    else:
        configs = [(a, e) for a in alphas for e in epsilons]

    results: list[RunResult] = []
    t_start = time.time()
    for (alpha, epsilon) in configs:
        for seed in seeds:
            t0 = time.time()
            r = run_single(
                width=width, alpha=alpha, epsilon=epsilon, seed=seed,
                data=data, train_idx=train_idx, test_idx=test_idx,
                closed_conductors=closed, cfg=cfg,
                vocab_size=vocab_size, max_len=max_len, n_classes=n_classes,
            )
            dt = time.time() - t0
            print(f"[W={width:3d} a={alpha:.2f} e={epsilon:.2f} s={seed:5d}] "
                  f"test_loss={r.final_test_loss:.4f}  train_loss={r.final_train_loss:.4f}  "
                  f"acc={r.final_test_acc:.4f}  ece={r.ece_test:.4f}  "
                  f"leakage={r.leakage_logit:.3e}  "
                  f"sV={r.sigma_V:.4f}  sM={r.sigma_M:.4f}  rho={r.rho_VM:.4f}  "
                  f"({dt:.1f}s)",
                  flush=True)
            results.append(r)

    t_total = time.time() - t_start
    print()
    print(f"# total wall time: {t_total:.1f}s = {t_total/60.0:.2f}m")

    # Write JSON
    def jsonable(o: Any) -> Any:
        if isinstance(o, float):
            if math.isnan(o) or math.isinf(o):
                return str(o)
            return round(o, 12)
        if isinstance(o, dict):
            return {str(k): jsonable(v) for k, v in o.items()}
        if isinstance(o, list):
            return [jsonable(v) for v in o]
        return o

    payload = {
        "script_version": SCRIPT_VERSION,
        "task": "months",
        "N": n_classes,
        "width": width,
        "epochs": cfg.epochs,
        "batch_size": cfg.batch_size,
        "lr": cfg.lr,
        "closed_support": list(closed),
        "split_seed": cfg.split_seed,
        "train_fraction": cfg.train_fraction,
        "alphas": alphas,
        "epsilons": epsilons,
        "seeds": seeds,
        "results": [jsonable(asdict(r)) for r in results],
    }
    out_json = output_dir / f"label_smoothing_substitution_months_width{width}.json"
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"# wrote {out_json}")


if __name__ == "__main__":
    main()
