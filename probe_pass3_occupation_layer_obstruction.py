"""Occupation-layer obstruction at the critical center.

For the raw centered Euler row, the m-th zeta residual cumulant receives
from occupation layer r the positive-size term

    r^(2m-1) (log p)^(2m) p^(-r/2) / (2m)!

up to the alternating cumulant sign. The prime sum converges at s=1/2
exactly when r/2 > 1, i.e. r >= 3.

This probe shows numerically that the obstruction is concentrated in
occupation layers r=1 and r=2. Layers r>=3 have stable finite sums.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp


mp.mp.dps = 60


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def first_primes(count: int) -> list[int]:
    primes: list[int] = []
    n = 2
    while len(primes) < count:
        ok = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                ok = False
                break
        if ok:
            primes.append(n)
        n += 1 if n == 2 else 2
    return primes


def layer_ell(primes: list[int], r: int, m: int) -> mp.mpf:
    total = mp.mpf(0)
    for p_int in primes:
        p = mp.mpf(p_int)
        total += (mp.mpf(r) ** (2 * m - 1)) * (mp.log(p) ** (2 * m)) * (
            p ** (-mp.mpf(r) / 2)
        ) / factorial(2 * m)
    return ((-1) ** (m + 1)) * m * total


def main() -> None:
    m = 1
    print("Raw centered Euler contribution by occupation layer")
    print("m=1, center s=1/2")
    print()
    print("nprimes       r=1            r=2            r=3            r=4            r>=3 total")
    for count in (10, 30, 100, 300, 1000, 3000):
        primes = first_primes(count)
        layers = [layer_ell(primes, r, m) for r in range(1, 9)]
        tail = sum(layers[2:])
        print(
            f"{count:7d}  "
            f"{fmt(layers[0], 12):>14} {fmt(layers[1], 12):>14} "
            f"{fmt(layers[2], 12):>14} {fmt(layers[3], 12):>14} "
            f"{fmt(tail, 12):>14}"
        )

    print("\nConvergence criterion")
    print("layer r prime sum ~ sum_p (log p)^(2m) p^(-r/2)")
    print("converges exactly for r >= 3; r=1 and r=2 require continuation.")


if __name__ == "__main__":
    main()
