#!/usr/bin/env python3
"""
primorial_error_accumulation_v2.py

More refined analysis of error accumulation in iterated primorial completion.

This version includes:
- Better modeling of per-prime error contribution (using log p factors)
- Tracking of the X^ε loss more carefully
- Computation of the critical k where effective saving drops below 1
- Simple extrapolation for larger primorials
"""

import math
import numpy as np

def nth_prime(k):
    if k == 1:
        return 2
    p = 3
    count = 1
    while count < k:
        if all(p % d != 0 for d in range(2, int(math.isqrt(p)) + 1)):
            count += 1
        if count < k:
            p += 2
    return p

def model_local_contribution(p, eps=0.01):
    """
    Returns a tuple (saving, error_multiplier)
    saving: multiplicative factor < 1 from local oscillation
    error_multiplier: factor > 1 from this iteration's error
    """
    # Assume a mild saving that improves slowly with p
    saving = 1.0 - 0.12 / math.log(p + 3)

    # Error grows roughly like (log p)^eps or similar
    error_mult = 1 + eps * math.log(p + 2)
    return saving, error_mult

def analyze_accumulation(max_k=30, eps=0.015):
    print(f"\n=== Refined Primorial Error Accumulation Analysis (eps={eps}) ===\n")
    print(f"{'k':>3} | {'p_k':>6} | {'Cumulative Saving':>18} | {'Cumulative Error':>18} | {'Net Factor':>14} | {'Status'}")
    print("-" * 95)

    cumulative_saving = 1.0
    cumulative_error = 1.0
    critical_k = None

    for k in range(1, max_k + 1):
        p = nth_prime(k)
        saving, err = model_local_contribution(p, eps=eps)
        cumulative_saving *= saving
        cumulative_error *= err
        net = cumulative_saving / cumulative_error

        status = ""
        if net < 1.0 and critical_k is None:
            critical_k = k
            status = " <--- Critical point (net < 1)"

        print(f"{k:3d} | {p:6d} | {cumulative_saving:18.8e} | {cumulative_error:18.8e} | {net:14.6e} | {status}")

    print("-" * 95)
    if critical_k:
        print(f"\nNet factor drops below 1 around k ≈ {critical_k} (p_k ≈ {nth_prime(critical_k)})")
    else:
        print("\nNet factor remained > 1 throughout the tested range.")

    # Rough extrapolation
    print("\nRough extrapolation note:")
    print("If the per-prime saving continues at this rate, the method may remain viable")
    print("up to primorials with p_n around exp(c * log X / log log X) before the")
    print("accumulated error overtakes the saving, depending on the precise eps.")

if __name__ == "__main__":
    analyze_accumulation(max_k=25, eps=0.012)
    print("\nDone.")