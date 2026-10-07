"""Third-layer dominance probe for the ordinary Pass-3 tail.

After the two critical occupation layers r=1,2 have been replaced by the
continued pair carrier, the remaining ordinary prime carrier is

    T_{>=3}(s) = sum_{r>=3} P(r s) / r.

At the critical center s=1/2, the first convergent layer is r=3. This
probe splits the omitted prime tail after p>X into:

    r = 3       the dominant ordinary layer,
    r >= 4      the faster ordinary remainder.

The bounds are intentionally conservative. Their job is to make the
sentence "control the third layer" executable.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

from probe_pass3_tail_control_bounds import integer_tail_bound


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def r_layer_prime_tail_bound(m: int, r: int, x: mp.mpf) -> mp.mpf:
    """Bound omitted prime tail for a single occupation layer r."""
    k = 2 * m
    a = mp.mpf(r) / 2
    return (
        (mp.mpf(m) / factorial(2 * m))
        * (mp.mpf(r) ** (2 * m - 1))
        * integer_tail_bound(a, k, x)
    )


def r_ge4_prime_tail_bound(m: int, x: mp.mpf) -> mp.mpf:
    """Bound omitted prime tail for all occupation layers r>=4."""
    k = 2 * m
    q = ((mp.mpf(5) / 4) ** (2 * m - 1)) / mp.sqrt(x)
    if q >= 1:
        return mp.inf
    first = (mp.mpf(4) ** (2 * m - 1)) * integer_tail_bound(mp.mpf(2), k, x)
    return (mp.mpf(m) / factorial(2 * m)) * first / (1 - q)


def r_ge5_prime_tail_bound(m: int, x: mp.mpf) -> mp.mpf:
    """Bound omitted prime tail for all occupation layers r>=5."""
    k = 2 * m
    q = ((mp.mpf(6) / 5) ** (2 * m - 1)) / mp.sqrt(x)
    if q >= 1:
        return mp.inf
    first = (mp.mpf(5) ** (2 * m - 1)) * integer_tail_bound(mp.mpf("2.5"), k, x)
    return (mp.mpf(m) / factorial(2 * m)) * first / (1 - q)


def main() -> None:
    print("Pass-3 third-layer prime-tail dominance")
    print("Bounds are for omitted primes p > X at the critical center s=1/2.")
    print()

    cutoffs = [mp.mpf("1e4"), mp.mpf("1e6"), mp.mpf("1e8"), mp.mpf("1e12")]
    orders = [1, 2, 3, 4, 5]

    for x in cutoffs:
        print(f"X = {fmt(x, 8)}")
        print("m   r=3 bound          r>=4 bound         ratio r>=4/r=3     r>=5/r=3")
        for m in orders:
            b3 = r_layer_prime_tail_bound(m, 3, x)
            b4plus = r_ge4_prime_tail_bound(m, x)
            b5plus = r_ge5_prime_tail_bound(m, x)
            print(
                f"{m:1d}  {fmt(b3, 12):>16} {fmt(b4plus, 12):>18} "
                f"{fmt(b4plus / b3, 8):>18} {fmt(b5plus / b3, 8):>14}"
            )
        print()

    print("Interpretation")
    print("- r=3 is the first convergent ordinary layer and the dominant omitted prime tail.")
    print("- r>=4 is already a faster remainder; r>=5 is smaller again.")
    print("- Pass-3 tail work should therefore target r=3 acceleration/certification first.")


if __name__ == "__main__":
    main()
