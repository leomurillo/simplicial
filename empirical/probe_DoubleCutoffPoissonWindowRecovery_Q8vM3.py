"""Numerical probe for Note_DoubleCutoffPoissonWindowRecovery_Q8vM3.

The theorem is analytic, not numerical: exponential log-side decay gives an
absolutely summable prime-power majorant, so all cofinal cutoffs converge by
dominated convergence.  This probe displays the tail behavior for two detector
kernels and checks the Siegel-Walfisz scale inequalities that separate the
existence-safe diagonal from natural finite-row scale.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
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


def gaussian_even(u: float, center: float = 6.0, sigma: float = 1.1) -> float:
    return math.exp(-((u - center) ** 2) / (2 * sigma**2)) + math.exp(
        -((u + center) ** 2) / (2 * sigma**2)
    )


def exp_even(u: float, delta: float = 0.35) -> float:
    return math.exp(-(1.0 + delta) * abs(u))


@dataclass(frozen=True)
class Cutoff:
    p_axis: int
    k_occ: int
    m_dirichlet: int


def vm_sum(
    G: Callable[[float], float],
    primes: list[int],
    cutoff: Cutoff,
    reflected: bool = False,
) -> float:
    total = 0.0
    for p in primes:
        if p > cutoff.p_axis:
            break
        logp = math.log(p)
        power = p
        r = 1
        while r <= cutoff.k_occ and power <= cutoff.m_dirichlet:
            u = r * logp
            total += logp * (G(u) + (G(-u) if reflected else 0.0))
            r += 1
            power *= p
    return total


def reference_sum(
    G: Callable[[float], float],
    p_limit: int,
    r_limit: int,
    reflected: bool = False,
) -> float:
    total = 0.0
    for p in primes_upto(p_limit):
        logp = math.log(p)
        for r in range(1, r_limit + 1):
            u = r * logp
            total += logp * (G(u) + (G(-u) if reflected else 0.0))
    return total


def tail_majorant(p_axis: int, k_occ: int, m_dirichlet: int, delta: float) -> float:
    # Finite approximation to the summable majorant tail
    # sum_{p>p_axis or r>k_occ or p^r>m} log(p) p^{-r(1+delta)}.
    p_limit = max(200000, p_axis * 100)
    total = 0.0
    for p in primes_upto(p_limit):
        logp = math.log(p)
        power = p
        for r in range(1, 80):
            term = logp * p ** (-r * (1.0 + delta))
            if p > p_axis or r > k_occ or power > m_dirichlet:
                total += term
            if term < 1e-18:
                break
            power *= p
    return total


def primorials(count: int) -> list[int]:
    out = []
    acc = 1
    for p in primes_upto(100):
        acc *= p
        out.append(acc)
        if len(out) == count:
            return out
    return out


def print_convergence_table(name: str, G: Callable[[float], float]) -> None:
    primes = primes_upto(200000)
    ref = reference_sum(G, p_limit=200000, r_limit=80, reflected=True)
    if "Gaussian" in name:
        # The Gaussian is centered at u=6, so the main r=1 mass lies near
        # p ~= exp(6) = 403.  These cutoffs deliberately pass that scale.
        cutoffs = [
            Cutoff(101, 3, 1_000_000),
            Cutoff(401, 4, 1_000_000_000),
            Cutoff(1009, 5, 10_000_000_000),
            Cutoff(5003, 6, 1_000_000_000_000),
            Cutoff(20011, 8, 1_000_000_000_000_000),
        ]
    else:
        cutoffs = [
            Cutoff(7, 2, 200),
            Cutoff(43, 4, 200_000),
            Cutoff(251, 8, 100_000_000),
            Cutoff(1009, 12, 10_000_000_000),
            Cutoff(5003, 16, 1_000_000_000_000),
        ]
    print(f"\n{name}")
    print("p_axis  K      M             symmetric_sum       abs_error      exp_majorant_tail")
    for cutoff in cutoffs:
        val = vm_sum(G, primes, cutoff, reflected=True)
        err = abs(ref - val)
        maj = tail_majorant(cutoff.p_axis, cutoff.k_occ, cutoff.m_dirichlet, delta=0.25)
        print(
            f"{cutoff.p_axis:6d} {cutoff.k_occ:2d} {cutoff.m_dirichlet:12d} "
            f"{val:18.12e} {err:14.6e} {maj:18.6e}"
        )


def print_sw_scale_table() -> None:
    print("\nSiegel-Walfisz scale audit")
    print("P_n    beta  A       P_n <= (log exp(P_n^beta))^A?   natural P_n <= (log P_n^4)^A?")
    for P in primorials(7):
        beta = 0.5
        A = 3.0
        safe_rhs = (P**beta) ** A
        natural_rhs = math.log(P**4) ** A
        print(
            f"{P:6d} {beta:5.2f} {A:4.1f} "
            f"{str(P <= safe_rhs):>12s} ({safe_rhs:12.3e}) "
            f"{str(P <= natural_rhs):>12s} ({natural_rhs:12.3e})"
        )


def main() -> None:
    print("Double-cutoff Poisson-window recovery probe")
    print("Reference sums use p <= 200000 and r <= 80.")
    print_convergence_table("Even Gaussian detector", gaussian_even)
    print_convergence_table("Even exponential detector", exp_even)
    print_sw_scale_table()


if __name__ == "__main__":
    main()
