"""Zero-tail certificate workbench for the explicit-formula r=3 completion.

The explicit-formula completion uses

    (log xi)^(k)(s) = -(k-1)! sum_rho (rho-s)^(-k)

inside the formula for (log zeta)^(k)(s), then Mobius inversion for
P^(k)(3/2).

This probe isolates the zero-tail: how fast does a finite packet of the
first M zero pairs approximate (log zeta)^(k)(s) for the slowest point
s=3/2?

The main expected bottleneck is k=2.  For k>=4 the zero-tail is already
small with modest M.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_explicit_formula_r3_completion as ef


mp.mp.dps = 70


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def exact_log_zeta_derivative(s: mp.mpf, k: int) -> mp.mpf:
    return mp.diff(lambda z: mp.log(mp.zeta(z)), s, k)


def main() -> None:
    s = mp.mpf("1.5")
    orders = [2, 4, 6, 8, 10, 12, 14, 16]
    zero_counts = [10, 20, 50, 100, 200]
    max_zeros = max(zero_counts)
    zeros = ef.zero_list(max_zeros)

    print("Pass-3 zero-tail certificate workbench")
    print("point s=3/2 for (log zeta)^(k)(s)")
    print()

    exact = {k: exact_log_zeta_derivative(s, k) for k in orders}

    print("Relative error of finite zero packet")
    print("k   " + " ".join(f"M={m}".rjust(14) for m in zero_counts))
    for k in orders:
        row = []
        for count in zero_counts:
            approx = ef.log_zeta_derivative_zero_packet(s, k, zeros[:count])
            row.append(abs(approx - exact[k]) / abs(exact[k]))
        print(f"{k:2d}  " + " ".join(f"{fmt(val, 8):>14}" for val in row))

    print()
    print("Absolute error at M=100 and M=200")
    print("k   exact                 err(M=100)          err(M=200)")
    for k in orders:
        approx100 = ef.log_zeta_derivative_zero_packet(s, k, zeros[:100])
        approx200 = ef.log_zeta_derivative_zero_packet(s, k, zeros[:200])
        print(
            f"{k:2d}  {fmt(exact[k], 14):>18} "
            f"{fmt(approx100-exact[k], 12):>18} {fmt(approx200-exact[k], 12):>18}"
        )

    print()
    print("Interpretation")
    print("- k=2 is the slow zero-tail bottleneck.")
    print("- k>=4 converges quickly enough that Mobius/gate sensitivity becomes the next issue.")
    print("- A proof needs an explicit zero-tail bound, not just more zeros.")


if __name__ == "__main__":
    main()
