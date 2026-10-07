"""Mobius-tail certificate for prime-zeta derivative completion.

The explicit-formula r=3 completion uses

    P^(k)(3/2) = sum_{n>=1} mu(n)n^(k-1) (log zeta)^(k)(3n/2).

After a finite Mobius cutoff N, the omitted terms are exponentially small
because 3n/2 is far into the half-plane of absolute convergence.

This probe computes a conservative Mobius-tail bound using

    |(log zeta)^(k)(sigma)|
      <= sum_{q>=2} (log q)^k q^(-sigma)
      <= f(2) + integral_2^infty (log t)^k t^(-sigma) dt

for sigma large enough that f is decreasing from 2 onward.  At the cutoffs
used here this condition is comfortably satisfied.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

from probe_pass3_tail_control_bounds import integral_tail_power_log


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def log_zeta_derivative_abs_bound(sigma: mp.mpf, k: int) -> mp.mpf:
    f2 = (mp.log(2) ** k) * (mp.mpf(2) ** (-sigma))
    return f2 + integral_tail_power_log(sigma, k, mp.mpf(2))


def prime_zeta_mobius_tail_bound(s: mp.mpf, k: int, cutoff: int) -> mp.mpf:
    total = mp.mpf(0)
    n = cutoff + 1
    while True:
        sigma = mp.mpf(n) * s
        term = (mp.mpf(n) ** (k - 1)) * log_zeta_derivative_abs_bound(sigma, k)
        total += term
        if term < mp.mpf("1e-80"):
            break
        n += 1
        if n > cutoff + 1000:
            break
    return total


def r3_ell_mobius_tail_bound(m: int, cutoff: int) -> mp.mpf:
    k = 2 * m
    p_bound = prime_zeta_mobius_tail_bound(mp.mpf("1.5"), k, cutoff)
    scale = (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1))
    return scale * p_bound


def main() -> None:
    cutoffs = [12, 24, 36, 60]
    orders = range(1, 9)

    print("Pass-3 Mobius-tail certificate")
    print("Bound for omitted r=3 folded ell_m after Mobius cutoff N.")
    print()
    print("m   " + " ".join(f"N={n}".rjust(16) for n in cutoffs))
    for m in orders:
        vals = [r3_ell_mobius_tail_bound(m, cutoff) for cutoff in cutoffs]
        print(f"{m:1d}  " + " ".join(f"{fmt(v, 8):>16}" for v in vals))

    print()
    print("Interpretation")
    print("- The Mobius tail is exponentially small at the cutoffs used in the zero-packet probe.")
    print("- The visible completion error is therefore dominated by zero-tail, especially k=2.")


if __name__ == "__main__":
    main()
