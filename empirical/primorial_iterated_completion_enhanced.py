#!/usr/bin/env python3
"""
primorial_iterated_completion_enhanced.py

Enhanced error analysis for iterated primorial completion.

Improvements over v1:
- Local saving now depends on dual length after completion (more realistic).
- Incorporates square-root cancellation when dual sum is long enough.
- Models the transition between trivial bound and square-root saving.
- Better tracking of how saving behaves as we iterate over small primes.
- Includes a simple model for the X^eps loss per iteration based on log factors.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

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

def local_saving_and_error(p, current_length, X=1e12, eps=0.01):
    """
    More realistic model for one iteration of completion modulo p.

    Parameters:
        p: current small prime
        current_length: approximate length of the sum being completed (before this step)
        X: global size parameter (for modeling X^eps losses)
        eps: controls the strength of X^eps losses per iteration

    Returns:
        saving: multiplicative saving factor from this completion
        error_mult: multiplicative error factor introduced by this step
    """
    # After completing modulo p, dual length is roughly current_length / p
    dual_length = current_length / p

    # Decide regime
    if dual_length > math.sqrt(X):   # Very long dual -> expect square-root cancellation
        # Weil / square-root cancellation ~ 1/sqrt(p) improvement over trivial
        saving = 1.0 / math.sqrt(p) * (1 + 0.5 / math.log(p + 2))
    elif dual_length > p**2:         # Moderately long -> partial saving
        saving = 1.0 / p**0.4        # Some power saving
    else:                            # Short dual -> mostly trivial bound + small oscillation
        saving = 1.0 - 0.08 / math.log(p + 3)

    # Error introduced by completion / Cauchy (grows slowly with p and iteration count)
    error_mult = 1 + eps * math.log(p + 2) + 0.005 * math.log(current_length + 2)

    return max(saving, 1e-12), error_mult

def run_enhanced_analysis(max_k=25, X=1e12, eps=0.012, initial_length=1e10):
    print(f"\n=== Enhanced Primorial Iterated Completion Analysis ===\n")
    print(f"Global X = {X:.0e}, eps = {eps}, initial_length = {initial_length:.0e}\n")
    print(f"{'k':>3} | {'p_k':>6} | {'Current Length':>14} | {'Local Saving':>14} | {'Cumul. Saving':>14} | {'Cumul. Error':>14} | {'Net Factor':>12}")
    print("-" * 105)

    cumulative_saving = 1.0
    cumulative_error = 1.0
    current_length = initial_length

    for k in range(1, max_k + 1):
        p = nth_prime(k)
        saving, err = local_saving_and_error(p, current_length, X=X, eps=eps)
        cumulative_saving *= saving
        cumulative_error *= err
        net = cumulative_saving / cumulative_error

        print(f"{k:3d} | {p:6d} | {current_length:14.2e} | {saving:14.6e} | {cumulative_saving:14.6e} | {cumulative_error:14.6e} | {net:12.6e}")

        # Update length for next iteration (dual becomes new main variable)
        current_length = current_length / p

    print("-" * 105)
    print("\nNote: 'Current Length' is the approximate length of the sum before completing modulo p_k.")
    print("Net Factor = (Cumulative Saving) / (Cumulative Error)")

if __name__ == "__main__":
    run_enhanced_analysis(max_k=22, X=1e12, eps=0.01, initial_length=1e9)
    print("\nEnhanced analysis complete.")