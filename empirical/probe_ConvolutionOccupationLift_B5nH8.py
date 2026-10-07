"""Probe the convolution occupation lift to von Mangoldt weights."""

import cmath
import itertools
import math


def add_multi(a, b):
    return tuple(x + y for x, y in zip(a, b))


def basis(i, n):
    return tuple(1 if j == i else 0 for j in range(n))


def convolve(A, B):
    out = {}
    for a, ca in A.items():
        for b, cb in B.items():
            out[add_multi(a, b)] = out.get(add_multi(a, b), 0) + ca * cb
    return out


def is_single_axis(alpha):
    return sum(1 for x in alpha if x != 0) == 1


def occupied_prime(alpha, primes):
    for i, r in enumerate(alpha):
        if r:
            return primes[i], r
    raise ValueError("not an occupation")


def main():
    primes = [2, 3, 5, 7, 11]
    s = 2.0 + 0.3j
    kmax = 8
    n = len(primes)

    H = {basis(i, n): p ** (-s) for i, p in enumerate(primes)}
    power = {tuple(0 for _ in primes): 1.0}

    log_series = {}
    d_log_series = {}
    mixed_mass = 0.0
    mixed_count = 0

    for r in range(1, kmax + 1):
        power = convolve(power, H)
        for alpha, coeff in power.items():
            log_coeff = coeff / r
            d_coeff = 0
            # -d/ds of product p_i^{-alpha_i s} is
            # (sum alpha_i log p_i) times the product.
            weight = sum(alpha[i] * math.log(primes[i]) for i in range(n))
            d_coeff = weight * log_coeff

            log_series[alpha] = log_series.get(alpha, 0) + log_coeff
            d_log_series[alpha] = d_log_series.get(alpha, 0) + d_coeff
            if not is_single_axis(alpha):
                mixed_mass += abs(d_coeff)
                mixed_count += 1

    max_err = 0.0
    rows = []
    for alpha, coeff in d_log_series.items():
        if not is_single_axis(alpha):
            continue
        p, r = occupied_prime(alpha, primes)
        expected = math.log(p) * p ** (-r * s)
        err = abs(coeff - expected)
        max_err = max(max_err, err)
        if r <= 4:
            rows.append((p, r, coeff, expected, err))

    print("Convolution occupation lift")
    print(f"primes={primes}, s={s}, occupation cutoff={kmax}")
    print()
    print("max error on single-axis von Mangoldt coefficients:", f"{max_err:.3e}")
    print("mixed terms before primitive projection:", mixed_count)
    print("mixed derivative mass before projection:", f"{mixed_mass:.6e}")
    print()
    print("p, r, recovered coefficient, expected Lambda(p^r) p^{-rs}, abs error")
    for p, r, coeff, expected, err in rows[:12]:
        print(
            f"{p:2d} {r:2d} "
            f"{coeff.real: .12e}{coeff.imag:+.12e}j "
            f"{expected.real: .12e}{expected.imag:+.12e}j "
            f"{err:.3e}"
        )


if __name__ == "__main__":
    main()
