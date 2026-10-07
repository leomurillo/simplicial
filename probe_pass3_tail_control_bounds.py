"""Tail-control bounds for the ordinary r>=3 prime carrier.

For the centered zeta residual, the ordinary tail contribution is

    sum_{r>=3} P(r s) / r.

At s=1/2 this is absolutely convergent, but high cumulants carry powers
of log p. This probe compares:

1. the actual error of a finite direct tail p<=X, 3<=r<=R against the
   exact complement tail;
2. a simple analytic upper bound obtained by dominating primes by
   integers and using incomplete-gamma integral tails.

The bound is intentionally conservative. Its purpose is to turn "control
the tail" into explicit inequalities.
"""

from __future__ import annotations

import importlib.util
from math import factorial
from pathlib import Path

import mpmath as mp


mp.mp.dps = 80

SCAFFOLD_PATH = Path(__file__).with_name("probe_pass3_two_layer_continuation_scaffold.py")
spec = importlib.util.spec_from_file_location("two_layer", SCAFFOLD_PATH)
two_layer = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(two_layer)

mp.mp.dps = 80
two_layer.mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def integral_tail_power_log(a: mp.mpf, k: int, x: mp.mpf) -> mp.mpf:
    """Integral from x to infinity of (log t)^k t^(-a) dt."""
    b = a - 1
    return mp.gammainc(k + 1, b * mp.log(x), mp.inf) / (b ** (k + 1))


def integer_tail_bound(a: mp.mpf, k: int, x: mp.mpf) -> mp.mpf:
    """Bound sum_{n>x} (log n)^k n^(-a) by an integral.

    Valid when the function is decreasing on [x, infinity), which is the
    case for log(x) > k/a. The caller chooses x large enough.
    """
    return integral_tail_power_log(a, k, x)


def prime_tail_after_x_bound(m: int, x: mp.mpf) -> mp.mpf:
    """Bound omitted prime tail for all r>=3 and p>x."""
    k = 2 * m
    q = (mp.mpf(4) / 3) ** (2 * m - 1) / mp.sqrt(x)
    if q >= 1:
        return mp.inf
    base = (mp.mpf(3) ** (2 * m - 1)) * integer_tail_bound(mp.mpf("1.5"), k, x)
    return (mp.mpf(m) / factorial(2 * m)) * base / (1 - q)


def occupation_tail_after_r_bound(m: int, r_cut: int) -> mp.mpf:
    """Bound omitted occupation tail r>r_cut over all primes."""
    k = 2 * m
    r0 = r_cut + 1
    # Ratio of consecutive occupation layers after r0, after dominating
    # prime sums by integer sums and the slowest base n=2.
    q = ((mp.mpf(r0 + 1) / r0) ** (2 * m - 1)) / mp.sqrt(2)
    if q >= 1:
        return mp.inf
    a = mp.mpf(r0) / 2
    first = (mp.mpf(r0) ** (2 * m - 1)) * integer_tail_bound(a, k, mp.mpf(2))
    return (mp.mpf(m) / factorial(2 * m)) * first / (1 - q)


def combined_tail_bound(m: int, x: mp.mpf, r_cut: int) -> mp.mpf:
    return prime_tail_after_x_bound(m, x) + occupation_tail_after_r_bound(m, r_cut)


def exact_tail_cumulants(order: int) -> list[mp.mpf]:
    # Keep sqrt(radius_x) < 1/6 so the ordinary r=3 tail is in its
    # absolute-convergence half-plane throughout the Cauchy circle.
    radius_x = mp.mpf("0.01")
    samples = 128
    mobius_cutoff = 60
    pair = two_layer.cumulants_from_folded_values(
        lambda y: two_layer.two_layer_folded_value(y, mobius_cutoff),
        order,
        radius_x,
        samples,
    )
    true_zeta = two_layer.cumulants_from_folded_values(
        two_layer.true_zeta_folded_value,
        order,
        radius_x,
        samples,
    )
    return [true_zeta[i] - pair[i] for i in range(order)]


def main() -> None:
    order = 5
    r_cut = 32
    prime_counts = [3000, 10000, 30000]

    exact = exact_tail_cumulants(order)

    print("Tail control for ordinary r>=3 carrier")
    print(f"occupation cutoff R={r_cut}")
    print()
    for count in prime_counts:
        primes = two_layer.first_primes(count)
        x = mp.mpf(primes[-1])
        direct = two_layer.direct_tail_ells(primes, 3, r_cut, order)
        print(f"prime_count={count}, X={primes[-1]}")
        print("m   actual_abs_error       analytic_bound        prime_tail_bound      r_tail_bound")
        for m in range(1, order + 1):
            actual = abs(direct[m - 1] - exact[m - 1])
            prime_bound = prime_tail_after_x_bound(m, x)
            r_bound = occupation_tail_after_r_bound(m, r_cut)
            bound = prime_bound + r_bound
            print(
                f"{m:1d}  {fmt(actual, 12):>18} {fmt(bound, 12):>20} "
                f"{fmt(prime_bound, 12):>20} {fmt(r_bound, 12):>16}"
            )
        print()

    print("Cutoff estimates for target absolute errors")
    print("m   target      sufficient X using prime-tail bound only")
    for m, target in [(1, mp.mpf("1e-3")), (2, mp.mpf("1e-3")), (3, mp.mpf("1e-2"))]:
        x = mp.mpf(10)
        while prime_tail_after_x_bound(m, x) > target:
            x *= 2
        print(f"{m:1d}  {fmt(target, 4):>8}    X >= {fmt(x, 8)}")


if __name__ == "__main__":
    main()
