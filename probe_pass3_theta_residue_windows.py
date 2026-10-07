"""Window profile for the r=3 theta residue.

The PNT completion replaces dtheta(t) by dt.  The residue is

    integral_X^infty h_m(t) d(theta(t)-t),

where h_m(t)=(log t)^(2m-1)t^(-3/2), times the folded cumulant scale.

This probe computes the partial residue over finite windows [X,Y]:

    sum_{X<p<=Y} (log p)^(2m) p^(-3/2)
      - integral_X^Y (log t)^(2m-1)t^(-3/2) dt,

and compares it to the total oracle residue true - PNT.

It answers: is the gate-relevant theta residue local near the cutoff, or
distributed over a long tail?
"""

from __future__ import annotations

from math import factorial, log

import mpmath as mp
from sympy import primerange

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_pnt_r3_completion_operator as pnt
from probe_pass3_tail_control_bounds import integral_tail_power_log


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def scaled_window_residue(m: int, x: int, y: int) -> mp.mpf:
    k = 2 * m
    j = k - 1
    prime_part = mp.mpf(0)
    for p in primerange(x + 1, y + 1):
        lp = log(p)
        prime_part += mp.mpf((lp ** k) * (p ** -1.5))
    integral_part = integral_tail_power_log(mp.mpf("1.5"), j, mp.mpf(x)) - integral_tail_power_log(
        mp.mpf("1.5"), j, mp.mpf(y)
    )
    scale = ((-1) ** (m + 1)) * (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1))
    return scale * (prime_part - integral_part)


def main() -> None:
    order = 8
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60

    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    x = primes[-1]
    x_mpf = mp.mpf(x)
    true_mu = eta.total_ells(None, order)
    pnt_mu = [finite_mu[m - 1] + pnt.pnt_r3_missing_ell(m, x_mpf) for m in range(1, order + 1)]
    total_residue = [true_mu[m - 1] - pnt_mu[m - 1] for m in range(1, order + 1)]

    multipliers = [2, 5, 10, 20, 50]

    print("Pass-3 theta-residue window profile")
    print(f"X={x}")
    print("Each entry is partial window residue divided by total oracle residue.")
    print()
    print("m   " + " ".join(f"Y={mult}X".rjust(14) for mult in multipliers))
    for m in range(1, order + 1):
        ratios = []
        for mult in multipliers:
            y = int(x * mult)
            partial = scaled_window_residue(m, x, y)
            ratios.append(partial / total_residue[m - 1])
        print(f"{m:1d}   " + " ".join(f"{fmt(r, 8):>14}" for r in ratios))

    print()
    print("Raw total oracle theta residues")
    for m, val in enumerate(total_residue, start=1):
        print(f"m={m}: {fmt(val, 14)}")

    print()
    print("Interpretation")
    print("- Ratios near 1 mean the theta residue is captured by that finite window.")
    print("- Slow approach means the gate-relevant residue is distributed far into the tail.")


if __name__ == "__main__":
    main()
