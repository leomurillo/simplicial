"""Theta-tail certificate for the dominant Pass-3 r=3 layer.

The previous r=3 bound dominated primes by all integers:

    sum_{p>X} (log p)^(2m) p^(-3/2)
      <= sum_{n>X} (log n)^(2m) n^(-3/2).

That is valid but wastes one prime-density logarithm.  This probe instead
uses the Chebyshev theta function

    theta(x) = sum_{p<=x} log p.

Write the r=3 prime tail as

    sum_{p>X} (log p)^(2m) p^(-3/2)
      = integral_X^infty (log t)^(2m-1) t^(-3/2) d theta(t).

If an explicit bound theta(t)-theta(X) <= A_theta t is available for
t>=X, then Stieltjes integration by parts gives a sharper certificate:

    <= A_theta integral_X^infty t * ( -d/dt [
         (log t)^(2m-1) t^(-3/2)
       ]) dt.

For large X this replaces a log^(2m) integral by a log^(2m-1) integral.
That is the missing prime-density gain.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

from probe_pass3_tail_control_bounds import integral_tail_power_log, prime_tail_after_x_bound


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def r3_integer_bound(m: int, x: mp.mpf) -> mp.mpf:
    k = 2 * m
    scale = (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1))
    return scale * integral_tail_power_log(mp.mpf("1.5"), k, x)


def r3_theta_bound(m: int, x: mp.mpf, a_theta: mp.mpf = mp.mpf("1.01")) -> mp.mpf:
    """Theta-based r=3 prime-tail certificate.

    Uses h(t)=(log t)^(2m-1)t^(-3/2). For X with h decreasing,

        sum_{p>X} (log p)^(2m)p^(-3/2)
        <= A_theta int_X^inf t(-h'(t))dt.
    """
    k = 2 * m
    j = k - 1
    # t(-h') = (3/2)L^j t^(-3/2) - j L^(j-1)t^(-3/2).
    density_gain = (
        mp.mpf("1.5") * integral_tail_power_log(mp.mpf("1.5"), j, x)
        - mp.mpf(j) * integral_tail_power_log(mp.mpf("1.5"), j - 1, x)
    )
    scale = (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1))
    return scale * a_theta * density_gain


def main() -> None:
    orders = [1, 2, 3, 4, 5]
    cutoffs = [mp.mpf("1e4"), mp.mpf("1e6"), mp.mpf("1e8"), mp.mpf("1e12")]
    a_theta = mp.mpf("1.01")

    print("Pass-3 r=3 theta-tail certificate")
    print(f"theta envelope parameter A_theta={a_theta}")
    print()

    for x in cutoffs:
        print(f"X = {fmt(x, 8)}")
        print("m   crude all-r>=3 bound   r=3 integer bound   r=3 theta bound    gain integer/theta")
        for m in orders:
            crude = prime_tail_after_x_bound(m, x)
            integer = r3_integer_bound(m, x)
            theta = r3_theta_bound(m, x, a_theta)
            print(
                f"{m:1d}  {fmt(crude, 12):>20} {fmt(integer, 12):>18} "
                f"{fmt(theta, 12):>17} {fmt(integer/theta, 8):>20}"
            )
        print()

    print("Interpretation")
    print("- The old integer bound is valid but throws away the prime-density log.")
    print("- The theta certificate recovers that log and targets exactly the r=3 bottleneck.")
    print("- Any stronger explicit theta estimate can be inserted by lowering A_theta.")


if __name__ == "__main__":
    main()
