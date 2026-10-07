#!/usr/bin/env python3
"""
primorial_iterated_completion_error_analysis.py

Purpose:
    Numerical and semi-symbolic exploration of error accumulation
    in the iterated completion / Cauchy-Schwarz process for bilinear forms
    twisted by characters modulo primorial-smooth moduli.

This script helps analyze whether the product of local savings from
iterated completion over the first k small primes can overcome the
accumulated error terms and the 2^{pi(p_n)} factor from summing over
divisors of the primorial.

Focus: Error analysis of the "primorial iteration" idea.
"""

import math
import numpy as np
from mpmath import mp, mpf, log, exp, pi
import matplotlib.pyplot as plt

# Set high precision
mp.dps = 50

def primorial(k):
    """Return the k-th primorial P_k = product of first k primes."""
    if k == 0:
        return 1
    p = 2
    prod = 1
    count = 0
    while count < k:
        if all(p % d != 0 for d in range(2, int(math.sqrt(p)) + 1)):
            prod *= p
            count += 1
        p += 1 if p == 2 else 2
    return prod

def nth_prime(k):
    """Return the k-th prime (simple implementation)."""
    if k == 1:
        return 2
    p = 3
    count = 1
    while count < k:
        if all(p % d != 0 for d in range(2, int(math.sqrt(p)) + 1)):
            count += 1
        if count < k:
            p += 2
    return p

def local_saving_factor(p, model='moderate'):
    """
    Model the local saving factor after completing modulo p^e.
    In reality this depends on the character and the bilinear coefficients.
    We use simple models for exploration:
        - 'optimistic': strong saving ~ 1/sqrt(p)
        - 'moderate'  : mild saving ~ 1 - c/log p
        - 'pessimistic': very weak saving
    """
    if model == 'optimistic':
        return 1.0 / math.sqrt(p)
    elif model == 'moderate':
        return 1.0 - 0.15 / math.log(p + 2)
    elif model == 'pessimistic':
        return 1.0 - 0.05 / math.log(p + 2)
    else:
        return 1.0

def accumulated_error(k_primes, model='moderate', include_divisor_factor=True):
    """
    Simulate the accumulated multiplicative error after iterating
    completion over the first k_primes primes.

    Returns:
        total_saving : product of local savings
        error_factor : rough estimate of accumulated error (X^eps type losses)
        effective_saving : total_saving / error_factor
    """
    primes = [nth_prime(i) for i in range(1, k_primes + 1)]
    total_saving = 1.0
    error_factor = 1.0

    for p in primes:
        saving = local_saving_factor(p, model=model)
        total_saving *= saving
        # Each iteration introduces some X^eps loss (modeled crudely)
        error_factor *= (1 + 0.01 * math.log(p + 1))

    if include_divisor_factor:
        # Penalty from summing over ~2^{pi(p_n)} divisors
        divisor_penalty = 2 ** k_primes
        effective_saving = total_saving / (error_factor * math.log(divisor_penalty + 2))
    else:
        effective_saving = total_saving / error_factor

    return total_saving, error_factor, effective_saving, primes

def run_analysis(max_k=25, models=None):
    if models is None:
        models = ['optimistic', 'moderate', 'pessimistic']

    results = {}
    for model in models:
        savings = []
        errors = []
        effectives = []
        for k in range(1, max_k + 1):
            ts, ef, es, _ = accumulated_error(k, model=model)
            savings.append(ts)
            errors.append(ef)
            effectives.append(es)
        results[model] = {
            'total_saving': savings,
            'error_factor': errors,
            'effective_saving': effectives
        }
    return results

def print_table(results, max_k=25):
    print("\n=== Iterated Completion Error Analysis ===\n")
    print(f"{'k':>3} | {'Prime':>6} | {'Model':12} | {'Total Saving':>14} | {'Error Factor':>14} | {'Effective Saving':>16}")
    print("-" * 85)

    for k in range(1, max_k + 1):
        p = nth_prime(k)
        for model in results:
            ts = results[model]['total_saving'][k-1]
            ef = results[model]['error_factor'][k-1]
            es = results[model]['effective_saving'][k-1]
            print(f"{k:3d} | {p:6d} | {model:12} | {ts:14.6e} | {ef:14.6e} | {es:16.6e}")
        print("-" * 85)

def plot_results(results, max_k=25):
    k_values = list(range(1, max_k + 1))
    plt.figure(figsize=(10, 6))

    for model in results:
        plt.plot(k_values, results[model]['effective_saving'], label=f'{model} model', linewidth=2)

    plt.yscale('log')
    plt.xlabel('Number of primes in primorial (k)')
    plt.ylabel('Effective Saving (log scale)')
    plt.title('Accumulated Effective Saving vs Number of Primes\n(Iterated Completion over Primorial)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('/home/workdir/artifacts/scripts/primorial_iterated_completion_saving.png', dpi=150)
    print("\nPlot saved to: /home/workdir/artifacts/scripts/primorial_iterated_completion_saving.png")

if __name__ == "__main__":
    print("Running primorial iterated completion error analysis...\n")
    results = run_analysis(max_k=20)
    print_table(results, max_k=20)
    plot_results(results, max_k=20)
    print("\nAnalysis complete.")