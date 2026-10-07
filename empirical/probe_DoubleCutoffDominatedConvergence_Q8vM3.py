"""Probe for Note_DoubleCutoffDominatedConvergence_Q8vM3.

Displays actual finite prime-power truncation errors for detectors in
D_{delta,0}, together with explicit analytic majorant tail bounds.
"""

from __future__ import annotations

import math
from typing import Callable


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i in range(limit + 1) if sieve[i]]


def even_exp(delta: float) -> Callable[[float], float]:
    return lambda u: math.exp(-(1.0 + delta) * abs(u))


def even_gaussian(center: float = 4.5, sigma: float = 0.8) -> Callable[[float], float]:
    def G(u: float) -> float:
        return math.exp(-((u - center) ** 2) / (2 * sigma * sigma)) + math.exp(
            -((u + center) ** 2) / (2 * sigma * sigma)
        )

    return G


def detector_norm(G: Callable[[float], float], delta: float) -> float:
    # A wide deterministic scan is enough for these smooth test detectors.
    step = 0.002
    width = 20.0
    count = int(2 * width / step) + 1
    best = 0.0
    for i in range(count):
        u = -width + i * step
        best = max(best, math.exp((1.0 + delta) * abs(u)) * abs(G(u)))
    return best


def vm_sum(G: Callable[[float], float], P: int, K: int, M: int, p_limit: int) -> float:
    total = 0.0
    for p in primes_upto(p_limit):
        if p > P:
            break
        power = p
        logp = math.log(p)
        for r in range(1, K + 1):
            if power > M:
                break
            total += logp * G(r * logp)
            power *= p
    return total


def reference_sum(G: Callable[[float], float], p_limit: int = 300_000, r_limit: int = 80) -> float:
    total = 0.0
    for p in primes_upto(p_limit):
        logp = math.log(p)
        for r in range(1, r_limit + 1):
            total += logp * G(r * logp)
    return total


def integral_tail(x: float, a: float) -> float:
    if x < 2:
        x = 2
    b = a - 1.0
    return x ** (1.0 - a) * (math.log(x) / b + 1.0 / (b * b))


def integer_log_tail_bound(x: float, a: float) -> float:
    # Crude monotone-integral style bound with one endpoint cushion.
    return math.log(max(2.0, x)) * max(2.0, x) ** (-a) + integral_tail(max(2.0, x), a)


def s1_bound(a: float) -> float:
    return math.log(2.0) * 2.0 ** (-a) + integral_tail(2.0, a)


def majorant_tail_bound(P: int, K: int, M: int, delta: float, norm: float) -> float:
    a = 1.0 + delta
    geom = 1.0 / (1.0 - 2.0 ** (-a))
    axis = norm * geom * integer_log_tail_bound(P, a)
    occupation = norm * s1_bound(a) * (2.0 ** (-a * K)) * geom
    dirichlet = norm * integer_log_tail_bound(M, a)
    return axis + occupation + dirichlet


def run_table(name: str, G: Callable[[float], float], delta: float) -> None:
    norm = detector_norm(G, delta)
    ref = reference_sum(G)
    cutoffs = [
        (31, 3, 10_000),
        (101, 5, 1_000_000),
        (503, 8, 100_000_000),
        (2003, 12, 10_000_000_000),
        (10007, 16, 1_000_000_000_000),
    ]
    print(f"\n{name}")
    print(f"D_delta norm estimate: {norm:.6e}")
    print("P_axis   K       M             abs_error       majorant_bound")
    for P, K, M in cutoffs:
        val = vm_sum(G, P, K, M, p_limit=300_000)
        err = abs(ref - val)
        bound = majorant_tail_bound(P, K, M, delta, norm)
        print(f"{P:6d} {K:3d} {M:14d} {err:15.6e} {bound:20.6e}")


def main() -> None:
    delta = 0.30
    print("Double-cutoff dominated convergence probe")
    print(f"delta={delta}; reference uses p<=300000, r<=80.")
    run_table("Extremal exponential detector exp(-(1+delta)|u|)", even_exp(delta), delta)
    run_table("Even Gaussian detector", even_gaussian(), delta)


if __name__ == "__main__":
    main()

