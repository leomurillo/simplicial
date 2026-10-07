"""Stable OASR-style conductor repulsion on F4[u]/(u^2)"""

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

N = 16
CONDUCTOR_PACKETS = {
    1: [0],
    2: [4, 8, 12],
    3: [5, 9, 13],
    4: [6, 10, 14],
    6: [7, 11, 15],
}

def conductor_mask(closed):
    mask = np.zeros(N, dtype=bool)
    for p in closed:
        if p in CONDUCTOR_PACKETS:
            for i in CONDUCTOR_PACKETS[p]:
                mask[i] = True
    return mask

def project(rows, mask):
    n = rows.shape[-1]
    m = np.mean(rows, axis=-1, keepdims=True)
    c = rows - m
    coeffs = np.fft.fft(c, axis=-1) / math.sqrt(n)
    coeffs[..., ~mask] = 0
    return m + np.fft.ifft(coeffs * math.sqrt(n), axis=-1).real

def energy_split(rows, mask):
    n = rows.shape[-1]
    c = rows - np.mean(rows, axis=-1, keepdims=True)
    coeffs = np.fft.fft(c, axis=-1) / math.sqrt(n)
    e = np.abs(coeffs)**2
    closed = float(np.sum(e[..., mask & (np.arange(n) != 0)]))
    leak = float(np.sum(e[..., ~mask & (np.arange(n) != 0)]))
    tot = closed + leak
    return closed, leak, (leak / tot if tot > 1e-18 else 0.0)

def make_target(n_samples=2048, seed=42):
    rng = np.random.default_rng(seed)
    logits = rng.normal(0, 0.55, (n_samples, N))
    logits = project(logits, conductor_mask({1,2,3}))
    p = np.exp(logits - np.max(logits, 1, keepdims=True))
    p /= p.sum(1, keepdims=True) + 1e-12
    y = np.array([rng.choice(N, p=pp) for pp in p])
    return p, y

@dataclass
class Result:
    seed: int
    closed: list
    kl: float
    leakage: float
    packet_energy: dict

def run_once(seed, closed_set, repel_set, repel_strength, steps=2500):
    rng = np.random.default_rng(seed)
    target_p, target_y = make_target(2048, seed)
    mask = conductor_mask(closed_set)
    repel_mask = conductor_mask(repel_set)

    W = rng.normal(0, 0.07, (N, N))
    m = np.zeros((N, N))
    v = np.zeros((N, N))
    t = 0
    lr = 0.007
    b1, b2 = 0.9, 0.999

    for _ in range(steps):
        idx = rng.choice(2048, 64, replace=False)
        y = target_y[idx]
        onehot = np.eye(N)[y]          # (64, 16)
        logits = W @ onehot.T          # (16, 64)
        probs = np.exp(logits - np.max(logits, 0, keepdims=True))
        probs /= (probs.sum(0, keepdims=True) + 1e-12)

        grad = probs - target_p[idx].T   # (16, 64)
        grad = np.mean(grad, axis=1, keepdims=True)  # (16, 1)
        grad = np.broadcast_to(grad, (N, N))

        t += 1
        m = b1 * m + (1 - b1) * grad
        v = b2 * v + (1 - b2) * grad**2
        mh = m / (1 - b1**t)
        vh = v / (1 - b2**t)
        upd = -lr * mh / (np.sqrt(vh) + 1e-8)

        if repel_set:
            rep_e = np.abs(np.fft.fft(upd, axis=0))**2
            pen = repel_strength * np.sum(rep_e[repel_mask])
            upd = upd * (1 - 0.5 * pen / (np.sum(rep_e) + 1e-9))

        upd = project(upd.T, mask).T
        W += upd.T

    # Final evaluation on full set
    final_logits = W @ np.eye(N)[target_y].T          # (16, 2048)
    fp = np.exp(final_logits - np.max(final_logits, 0, keepdims=True))
    fp /= (fp.sum(0, keepdims=True) + 1e-12)
    kl = float(np.mean(np.sum(target_p * np.log((target_p + 1e-12) / (fp.T + 1e-12)), 1)))

    _, _, leakage = energy_split(final_logits.T, mask)

    coeffs = np.fft.fft(final_logits.T - np.mean(final_logits.T, -1, keepdims=True), axis=-1)
    e = np.abs(coeffs)**2
    packet_e = {p: float(np.sum(e[:, CONDUCTOR_PACKETS[p]])) for p in CONDUCTOR_PACKETS}

    return Result(seed, sorted(closed_set), kl, leakage, packet_e)

def run_oasr(K=5, base={1,2,3}, strength=0.35):
    results = []
    used = set()
    rng = np.random.default_rng(12345)

    for k in range(K):
        extra = {p for p in [2,3,4,6] if rng.random() > 0.45}
        current = base | extra

        res = run_once(9100 + k, current, used, strength)
        results.append(res)

        high = {p for p, en in res.packet_energy.items() if en > 0.17 * sum(res.packet_energy.values())}
        used |= high

        print(f"Run {k+1}/{K}: closed={res.closed}  KL={res.kl:.4f}  leakage={res.leakage:.2e}")

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=5)
    parser.add_argument("--repulsion", type=float, default=0.35)
    args = parser.parse_args()

    res = run_oasr(args.K, strength=args.repulsion)
    Path("oasr_f4_u2_stable_results.json").write_text(json.dumps([asdict(r) for r in res], indent=2))
    print("\nOASR complete. Results saved.")