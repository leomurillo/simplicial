"""OASR-style conductor packet repulsion on F4[u]/(u^2) - fully self-contained version"""

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

Label = tuple[int, int]
ZERO = (0, 0)
LABELS = tuple((a, b) for a in range(4) for b in range(4))
N = len(LABELS)

CONDUCTOR_PACKETS = {
    1: [0],
    2: [4, 8, 12],      # u-packet
    3: [5, 9, 13],      # wu
    4: [6, 10, 14],     # (w+1)u
    6: [7, 11, 15],     # mixed wild
}

def conductor_mask(closed: set[int]) -> np.ndarray:
    mask = np.zeros(N, dtype=bool)
    for p in closed:
        if p in CONDUCTOR_PACKETS:
            for i in CONDUCTOR_PACKETS[p]:
                mask[i] = True
    return mask

def project(rows: np.ndarray, mask: np.ndarray) -> np.ndarray:
    n = rows.shape[-1]
    m = np.mean(rows, axis=-1, keepdims=True)
    c = rows - m
    coeffs = np.fft.fft(c, axis=-1) / math.sqrt(n)
    coeffs[..., ~mask] = 0
    return m + np.fft.ifft(coeffs * math.sqrt(n), axis=-1).real

def energy_split(rows: np.ndarray, mask: np.ndarray) -> tuple[float, float, float]:
    n = rows.shape[-1]
    c = rows - np.mean(rows, axis=-1, keepdims=True)
    coeffs = np.fft.fft(c, axis=-1) / math.sqrt(n)
    e = np.abs(coeffs)**2
    closed = float(np.sum(e[..., mask & (np.arange(n) != 0)]))
    leak = float(np.sum(e[..., ~mask & (np.arange(n) != 0)]))
    tot = closed + leak
    return closed, leak, (leak / tot if tot > 1e-18 else 0.0)

def make_target(n=2048, seed=42):
    rng = np.random.default_rng(seed)
    # Target is exactly in span{1, u, wu} = packets 1,2,3
    logits = rng.normal(0, 0.6, (n, N))
    logits = project(logits, conductor_mask({1,2,3}))
    p = np.exp(logits - np.max(logits, 1, keepdims=True))
    p /= p.sum(1, keepdims=True)
    y = np.array([rng.choice(N, p=pp) for pp in p])
    return p, y

@dataclass
class Result:
    seed: int
    closed: list[int]
    kl: float
    leakage: float
    packet_energy: dict

def run_once(seed: int, closed_set: set[int], repel_set: set[int], repel_strength: float, steps=2000):
    rng = np.random.default_rng(seed)
    target_p, target_y = make_target(2048, seed)
    mask = conductor_mask(closed_set)
    repel_mask = conductor_mask(repel_set)

    W = rng.normal(0, 0.08, (N, N))
    m = np.zeros_like(W)
    v = np.zeros_like(W)
    t = 0
    lr = 0.008
    b1, b2 = 0.9, 0.999

    for _ in range(steps):
        idx = rng.choice(len(target_y), 128, replace=False)
        y = target_y[idx]
        onehot = np.eye(N)[y]
        logits = W @ onehot.T
        probs = np.exp(logits - np.max(logits, 0, keepdims=True))
        probs /= (probs.sum(0, keepdims=True) + 1e-12)

        grad = np.mean(probs - target_p[idx].T, axis=1, keepdims=True)  # average over batch
        grad = np.broadcast_to(grad, (N, N))  # simple broadcast for stability

        t += 1
        m = b1*m + (1-b1)*grad
        v = b2*v + (1-b2)*grad**2
        mh = m / (1-b1**t)
        vh = v / (1-b2**t)
        upd = -lr * mh / (np.sqrt(vh) + 1e-8)

        # Repulsion penalty
        if repel_set:
            rep_e = np.abs(np.fft.fft(upd, axis=0))**2
            pen = repel_strength * np.sum(rep_e[repel_mask])
            upd = upd * (1 - 0.6 * pen / (np.sum(rep_e) + 1e-9))

        upd = project(upd.T, mask).T
        W += upd.T

    # Final metrics
    final_logits = W @ np.eye(N)[target_y[:128]].T
    fp = np.exp(final_logits - np.max(final_logits, 0, keepdims=True))
    fp /= (fp.sum(0, keepdims=True) + 1e-12)
    kl = float(np.mean(np.sum(target_p[:128] * np.log((target_p[:128] + 1e-12) / (fp + 1e-12)), 1)))

    _, _, leakage = energy_split(final_logits.T, mask)

    coeffs = np.fft.fft(final_logits.T - np.mean(final_logits.T, -1, keepdims=True), axis=-1)
    e = np.abs(coeffs)**2
    packet_e = {p: float(np.sum(e[:, CONDUCTOR_PACKETS[p]])) for p in CONDUCTOR_PACKETS}

    return Result(seed, sorted(closed_set), kl, leakage, packet_e)

def run_oasr(K=5, base={1,2,3}, strength=0.35):
    results = []
    used = set()
    rng = np.random.default_rng(1234)

    for k in range(K):
        extra = {p for p in [2,3,4,6] if rng.random() > 0.4}
        current = base | extra

        res = run_once(9100 + k, current, used, strength)
        results.append(res)

        high = {p for p, en in res.packet_energy.items() if en > 0.18 * sum(res.packet_energy.values())}
        used |= high

        print(f"Run {k+1}: closed={res.closed}  KL={res.kl:.4f}  leakage={res.leakage:.2e}")

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=5)
    parser.add_argument("--repulsion", type=float, default=0.35)
    args = parser.parse_args()

    res = run_oasr(args.K, strength=args.repulsion)
    Path("oasr_f4_u2_results.json").write_text(json.dumps([asdict(r) for r in res], indent=2))
    print("\nDone. Results saved to oasr_f4_u2_results.json")