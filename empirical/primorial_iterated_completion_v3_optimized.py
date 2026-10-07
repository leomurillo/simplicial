#!/usr/bin/env python3
"""
primorial_iterated_completion_v3_optimized.py

Advanced version with:
- Variable initial length
- Explicit 2^k divisor penalty
- Automatic detection of optimal switch point (where continuing iteration hurts more than it helps)
- Comparison of "full iteration" vs "switch after optimal k"
- Support for running multiple scenarios
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

def local_saving_and_error(p, current_length, X=1e12, eps=0.01):
    dual_length = current_length / p

    if dual_length > math.sqrt(X):
        saving = 1.0 / math.sqrt(max(p, 2)) * (1 + 0.4 / math.log(p + 2))
    elif dual_length > p**1.5:
        saving = 1.0 / p**0.35
    else:
        saving = 1.0 - 0.07 / math.log(p + 3)

    error_mult = 1 + eps * math.log(p + 2) + 0.003 * math.log(max(current_length, 2))
    return max(saving, 1e-12), error_mult

def analyze_with_switch(initial_length=1e9, X=1e12, eps=0.01, max_k=25, verbose=True):
    """
    Run the iteration and find the best point to stop (switch to another method).
    """
    cumulative_saving = 1.0
    cumulative_error = 1.0
    current_length = initial_length

    best_net = 0.0
    best_k = 0
    history = []

    for k in range(1, max_k + 1):
        p = nth_prime(k)
        saving, err = local_saving_and_error(p, current_length, X=X, eps=eps)
        cumulative_saving *= saving
        cumulative_error *= err

        # Include explicit divisor penalty 2^k
        divisor_penalty = 2 ** k
        net = (cumulative_saving / cumulative_error) / divisor_penalty

        history.append({
            'k': k,
            'p': p,
            'net': net,
            'cum_saving': cumulative_saving,
            'cum_error': cumulative_error
        })

        if net > best_net:
            best_net = net
            best_k = k

        current_length = current_length / p

    if verbose:
        print(f"\n=== Analysis: initial_length={initial_length:.0e}, X={X:.0e}, eps={eps} ===")
        print(f"Best switch point: after k={best_k} (p={nth_prime(best_k)}), Net factor = {best_net:.6e}")
        print("\nk | p   | Net Factor (with 2^k penalty)")
        print("-" * 40)
        for h in history:
            marker = " <-- best" if h['k'] == best_k else ""
            print(f"{h['k']:2d} | {h['p']:3d} | {h['net']:.6e}{marker}")

    return best_k, best_net, history

def run_multiple_scenarios():
    scenarios = [
        {'initial_length': 1e10, 'X': 1e12, 'eps': 0.01},
        {'initial_length': 1e9,  'X': 1e12, 'eps': 0.01},
        {'initial_length': 1e8,  'X': 1e12, 'eps': 0.012},
        {'initial_length': 1e10, 'X': 1e14, 'eps': 0.008},
    ]

    print("\n" + "="*70)
    print("MULTIPLE SCENARIOS - Optimal Switch Point Analysis")
    print("="*70)

    for s in scenarios:
        best_k, best_net, _ = analyze_with_switch(
            initial_length=s['initial_length'],
            X=s['X'],
            eps=s['eps'],
            verbose=False
        )
        print(f"initial_len={s['initial_length']:.0e} | X={s['X']:.0e} | eps={s['eps']:.3f} "
              f"→ Best k={best_k:2d}, Net={best_net:.4e}")

if __name__ == "__main__":
    # Run detailed analysis for one scenario
    analyze_with_switch(initial_length=1e9, X=1e12, eps=0.01, max_k=22)

    # Run multiple scenarios
    run_multiple_scenarios()

    print("\nDone.")