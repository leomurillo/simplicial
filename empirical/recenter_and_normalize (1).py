#!/usr/bin/env python3
"""
Re-center Cumulants around arg min Λ_n and Compute Normalized κ_r
"""

import numpy as np
import sympy as sp

def run(R=2310, seed=42, max_iter=40):
    Q = R
    nontriv = [d for d in range(1, R+1) if R % d == 0 and d != 1]
    packets = {d: [k for k in range(Q) if R // sp.gcd(k, R) == d] for d in nontriv}

    np.random.seed(seed)
    h = np.zeros(Q, dtype=complex)
    idx = packets[max(packets.keys())]
    h[idx[:8]] = 0.02 * np.exp(2j * np.pi * np.random.rand(8))
    h = h - np.mean(h)
    h = h / np.linalg.norm(h)

    def project_crit(J):
        Jc = J.copy().astype(complex)
        for d in nontriv:
            Jc[packets[d]] -= np.mean(Jc[packets[d]])
        return Jc

    Jc = project_crit(h)

    def leakage_proxy(J):
        conv4 = np.fft.ifft(np.fft.fft(J)**2 * np.fft.fft(J) * np.fft.fft(J))
        conv5 = np.fft.ifft(np.fft.fft(J)**3 * np.fft.fft(J) * np.fft.fft(J) * np.fft.fft(J))
        return np.abs(np.sum(conv4)) + np.abs(np.sum(conv5))

    best_J = Jc.copy()
    best_leak = leakage_proxy(best_J)
    step = 0.005

    for _ in range(max_iter):
        grad = np.zeros_like(best_J, dtype=complex)
        for i in range(0, Q, max(1, Q//200)):
            pert = best_J.copy()
            pert[i] += 1e-5
            grad[i] = (leakage_proxy(pert) - best_leak) / 1e-5
        best_J = best_J - step * grad
        best_J = project_crit(best_J)
        new_leak = leakage_proxy(best_J)
        if new_leak < best_leak:
            best_leak = new_leak
        else:
            step *= 0.6
        if step < 1e-7:
            break

    T2 = np.sum(np.abs(best_J)**2) / Q

    raw = {}
    for r in [3,4,5]:
        power = r - 2
        conv = np.fft.ifft(np.fft.fft(best_J)**power * np.fft.fft(best_J) * np.fft.fft(best_J))
        raw[r] = np.abs(np.sum(conv)) / (Q ** (r/2))

    k3 = raw[3] / (T2 ** 1.5)
    k4 = raw[4] / (T2 ** 2.0)
    k5 = raw[5] / (T2 ** 2.5)

    return {
        'R': R,
        'T2': T2,
        'k3': k3,
        'k4': k4,
        'k5': k5,
        'leakage': best_leak
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", type=int, default=2310)
    args = parser.parse_args()
    result = run(args.row)
    print(result)