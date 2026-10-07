#!/usr/bin/env python3
"""
Retired Z/18 FFT mean-cube proxy audit.

This does not verify Constraint 3. The proxy below reduces to
|sum(Jc)|^3 / R after packet projection, so it measures the seeded
random-phase mean rather than a cubic Noether charge.
"""

import numpy as np
from math import gcd

def run():
    R = 18
    Q = R
    nontriv = [d for d in range(1, R+1) if R % d == 0 and d != 1]
    packets = {d: [k for k in range(Q) if R // gcd(k, R) == d] for d in nontriv}

    np.random.seed(42)
    h = np.zeros(Q, dtype=complex)
    idx = packets[18]
    h[idx[:len(idx)]] = 0.04 * np.exp(2j * np.pi * np.random.rand(len(idx)))
    h = h - np.mean(h)
    h = h / np.linalg.norm(h)

    def project_crit(J):
        Jc = J.copy().astype(complex)
        for d in nontriv:
            Jc[packets[d]] -= np.mean(Jc[packets[d]])
        return Jc

    Jc = project_crit(h)

    def T3_proxy(J):
        # Retired proxy: kept only to reproduce the old non-diagnostic value.
        conv = np.fft.ifft(np.fft.fft(J) * np.fft.fft(J) * np.fft.fft(J))
        return np.abs(np.sum(conv)) / Q

    charge = float(T3_proxy(Jc))
    return {
        'R': R,
        'retired_proxy': charge,
        'formula': '|sum(Jc)|^3 / R',
        'diagnostic': False,
        'warning': 'Not a cubic Noether charge; do not use to verify Constraint 3.',
    }

if __name__ == "__main__":
    result = run()
    print(result)
