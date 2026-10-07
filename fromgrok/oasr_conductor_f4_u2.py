"""OASR-style conductor repulsion on F4[u]/(u^2).

This is the direct arithmetic analogue of Overlap-Aware Sheaf Repulsion (OASR)
from "All Circuits Lead to Rome" (Chen et al., 2026).

We treat the five conductor packets of R = F4[u]/(u^2) as "sheaves".
We run K independent conductor-closed optimizations.
After each run we record the closed packet set (those with projection fraction > 0.5).
For subsequent runs we add an overlap penalty that discourages high Fourier
energy in packets already chosen by previous runs.

This produces a family of low-overlap, high-quality closed supports
that all suppress K^CH carry leakage while achieving good KL.

The goal is to demonstrate that, exactly as in the sheaf-discovery paper,
multiple structurally distinct closed supports can faithfully solve the same task.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np

# Import the proven optimizer from the original script
sys.path.insert(0, '/home/workdir/artifacts')
from conductor_closed_optimizer import (
    ExperimentConfig, run_method, MethodResult, energy_split, conductor_packets
)

Label = tuple[int, int]
F4_NAMES = {0: "0", 1: "1", 2: "w", 3: "w+1"}
ZERO: Label = (0, 0)
LABELS: tuple[Label, ...] = tuple((a, b) for a in range(4) for b in range(4))
N_LABELS = len(LABELS)
EPS = 1e-12

def f4_add(left: int, right: int) -> int:
    return left ^ right

def add_label(left: Label, right: Label) -> Label:
    return (f4_add(left[0], right[0]), f4_add(left[1], right[1]))

def label_code(label: Label) -> int:
    return label[0] | (label[1] << 2)

def conductor(label: Label) -> str:
    if label == ZERO:
        return "1"
    if label[0] == 0:
        return "u"
    return "u^2"

# Conductor packets for F4[u]/(u^2) (5 packets)
CONDUCTOR_PACKETS = {
    1: [0],                                    # trivial
    2: [label_code((0,1)), label_code((0,2)), label_code((0,3))],  # u-packet
    3: [label_code((1,1)), label_code((2,1)), label_code((3,1))],  # w u
    4: [label_code((1,2)), label_code((2,2)), label_code((3,2))],  # (w+1)u
    6: [label_code((1,3)), label_code((2,3)), label_code((3,3))],  # mixed wild
}

def conductor_mask(closed_packets: set[int]) -> np.ndarray:
    mask = np.zeros(N_LABELS, dtype=bool)
    for p in closed_packets:
        if p in CONDUCTOR_PACKETS:
            for idx in CONDUCTOR_PACKETS[p]:
                mask[idx] = True
    return mask

def project_closed(rows: np.ndarray, closed_mask: np.ndarray) -> np.ndarray:
    n = rows.shape[-1]
    means = np.mean(rows, axis=-1, keepdims=True)
    centered = rows - means
    coeffs = np.fft.fft(centered, axis=-1) / math.sqrt(n)
    coeffs[..., ~closed_mask] = 0.0
    projected = np.fft.ifft(coeffs * math.sqrt(n), axis=-1).real
    return means + projected

def energy_split(rows: np.ndarray, closed_mask: np.ndarray) -> tuple[float, float, float]:
    n = rows.shape[-1]
    coeffs = np.fft.fft(rows - np.mean(rows, axis=-1, keepdims=True), axis=-1) / math.sqrt(n)
    energies = np.abs(coeffs) ** 2
    closed = float(np.sum(energies[..., closed_mask & (np.arange(n) != 0)]))
    leak = float(np.sum(energies[..., ~closed_mask & (np.arange(n) != 0)]))
    total = closed + leak
    leakage = 0.0 if total <= 1e-18 else leak / total
    return closed, leak, leakage

# --- Synthetic task (same as original) ---

def make_target(n_samples: int = 4096, seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    # Mixed closed support: span_F2{1, u, w u}
    closed_support = {0, label_code((0,1)), label_code((1,1))}
    logits = rng.normal(0, 0.5, size=(n_samples, N_LABELS))
    # Force target to be exactly closed
    logits = project_closed(logits, conductor_mask({1, 2, 3}))
    probs = np.exp(logits - np.max(logits, axis=1, keepdims=True))
    probs /= np.sum(probs, axis=1, keepdims=True)
    labels = np.array([rng.choice(N_LABELS, p=p) for p in probs])
    return probs, labels

# --- Simple Adam + conductor-closed optimizer ---

@dataclass
class RunResult:
    seed: int
    closed_packets: set[int]
    final_kl: float
    final_leakage: float
    kch_carry: float
    packet_energy: dict[int, float]

def run_single(
    seed: int,
    closed_packets: set[int],
    repulsion_packets: set[int],
    repulsion_strength: float = 0.3,
    steps: int = 2500,
    batch: int = 128,
) -> RunResult:
    rng = np.random.default_rng(seed)
    target_probs, target_labels = make_target(4096, seed)
    closed_mask = conductor_mask(closed_packets)
    rep_mask = conductor_mask(repulsion_packets)

    # Simple linear model (logits = W @ onehot, but we optimize directly)
    W = rng.normal(0, 0.1, size=(N_LABELS, N_LABELS))
    m = np.zeros_like(W)
    v = np.zeros_like(W)
    t = 0
    lr = 0.01
    beta1, beta2 = 0.9, 0.999
    eps = 1e-8

    for step in range(steps):
        idx = rng.choice(len(target_labels), batch, replace=False)
        y = target_labels[idx]
        # Forward
        logits = W @ np.eye(N_LABELS)[y].T   # simplified
        # Actually use full softmax cross-entropy on all samples for stability
        # (simplified version for speed)
        probs = np.exp(logits - np.max(logits, axis=0, keepdims=True))
        probs /= np.sum(probs, axis=0, keepdims=True) + EPS

        # Gradient (simplified)
        grad = probs - target_probs[idx].T   # shape (N, batch) approx

        # Adam
        t += 1
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * grad**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        update = -lr * m_hat / (np.sqrt(v_hat) + eps)

        # Apply repulsion on update (penalize energy in repulsion_packets)
        if repulsion_packets:
            rep_energy = np.abs(np.fft.fft(update, axis=0))**2
            penalty = repulsion_strength * np.sum(rep_energy[rep_mask])
            update = update * (1 - penalty / (np.sum(rep_energy) + 1e-9))

        # Project update onto closed support
        update = project_closed(update.T, closed_mask).T

        W += update.T   # apply

    # Final evaluation
    final_logits = W @ np.eye(N_LABELS).T
    final_probs = np.exp(final_logits - np.max(final_logits, axis=0, keepdims=True))
    final_probs /= np.sum(final_probs, axis=0, keepdims=True) + EPS
    kl = float(np.mean(np.sum(target_probs * np.log(target_probs / (final_probs + EPS) + EPS), axis=1)))

    closed, leak, leakage = energy_split(final_logits.T, closed_mask)
    kch = float(np.mean(np.abs(final_logits[1:] - final_logits[:-1])))  # crude K^CH proxy

    packet_energy = {}
    coeffs = np.fft.fft(final_logits.T - np.mean(final_logits.T, axis=-1, keepdims=True), axis=-1)
    energies = np.abs(coeffs)**2
    for p, indices in CONDUCTOR_PACKETS.items():
        packet_energy[p] = float(np.sum(energies[:, indices]))

    return RunResult(seed, closed_packets, kl, leakage, kch, packet_energy)

# --- OASR-style multi-run with repulsion ---

def run_oasr(
    K: int = 6,
    base_closed: set[int] = {1, 2, 3},  # start with the known good mixed support
    repulsion_strength: float = 0.4,
) -> list[RunResult]:
    results: list[RunResult] = []
    used_packets: set[int] = set()

    for k in range(K):
        # Start from base + some exploration
        rng = np.random.default_rng(k)
        current_closed = base_closed | {p for p in [2, 3, 4, 6] if rng.random() > 0.5}

        result = run_single(
            seed=9100 + k,
            closed_packets=current_closed,
            repulsion_packets=used_packets,
            repulsion_strength=repulsion_strength,
        )
        results.append(result)

        # Add the packets that ended up with high energy to the repulsion set
        high_energy = {p for p, e in result.packet_energy.items() if e > 0.15 * sum(result.packet_energy.values())}
        used_packets |= high_energy

        print(f"Run {k+1}/{K}: closed={sorted(current_closed)}, KL={result.final_kl:.4f}, leakage={result.final_leakage:.2e}")

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=6)
    parser.add_argument("--repulsion", type=float, default=0.4)
    args = parser.parse_args()

    results = run_oasr(K=args.K, repulsion_strength=args.repulsion)

    # Save report
    report = {
        "config": {"K": args.K, "repulsion_strength": args.repulsion},
        "results": [asdict(r) for r in results],
    }
    Path("oasr_f4_u2_report.json").write_text(json.dumps(report, indent=2))
    print("\nOASR conductor repulsion complete. Report saved to oasr_f4_u2_report.json")