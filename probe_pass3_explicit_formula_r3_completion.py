"""Explicit-formula r=3 completion via zeta zeros.

This probe converts the dominant r=3 completion into a zero-spectrum
calculation.

Use the Hadamard product for xi:

    xi(s) = xi(0) prod_rho (1 - s/rho),

so for k>=2,

    (log xi)^(k)(s) = -(k-1)! sum_rho (rho-s)^(-k).

Then

    log zeta(s)
      = log xi(s) - log s - log(s-1)
        + (s/2)log pi - log Gamma(s/2) + const,

and prime zeta derivatives follow by Mobius inversion:

    P^(k)(s) = sum_n mu(n)n^(k-1) (log zeta)^(k)(n s).

The r=3 folded cumulant layer is a scale multiple of P^(2m)(3/2).

This is still a finite zero-packet diagnostic, not a proof: the tail of
the zero sum and the Mobius cutoff need explicit certificates.  But it is
the correct explicit-formula shape of the completion.
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial

import mpmath as mp

import probe_pass3_completion_profile as completion
import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_two_layer_continuation_scaffold as scaffold


mp.mp.dps = 80
S0 = mp.mpf("0.5")


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


@lru_cache(maxsize=None)
def zero_ordinate(index: int) -> mp.mpf:
    return mp.im(mp.zetazero(index))


def zero_list(count: int) -> list[mp.mpf]:
    return [zero_ordinate(i) for i in range(1, count + 1)]


def log_xi_derivative_zero_packet(s: mp.mpf, k: int, zeros: list[mp.mpf]) -> mp.mpf:
    total = mp.mpc(0)
    for gamma in zeros:
        rho = mp.mpc(mp.mpf("0.5"), gamma)
        total += 1 / ((rho - s) ** k)
        total += 1 / ((mp.conj(rho) - s) ** k)
    return mp.re(-mp.factorial(k - 1) * total)


def log_zeta_derivative_zero_packet(s: mp.mpf, k: int, zeros: list[mp.mpf]) -> mp.mpf:
    value = log_xi_derivative_zero_packet(s, k, zeros)
    value += ((-1) ** k) * mp.factorial(k - 1) * (1 / (s**k) + 1 / ((s - 1) ** k))
    value -= (mp.mpf("0.5") ** k) * mp.polygamma(k - 1, s / 2)
    return value


def prime_zeta_derivative_zero_packet(
    s: mp.mpf, k: int, zeros: list[mp.mpf], mobius_cutoff: int
) -> mp.mpf:
    total = mp.mpf(0)
    for n in range(1, mobius_cutoff + 1):
        mu = scaffold.mobius(n)
        if mu == 0:
            continue
        total += (
            mp.mpf(mu)
            * (mp.mpf(n) ** (k - 1))
            * log_zeta_derivative_zero_packet(mp.mpf(n) * s, k, zeros)
        )
    return total


def r3_layer_ell_from_zero_packet(m: int, zeros: list[mp.mpf], mobius_cutoff: int) -> mp.mpf:
    k = 2 * m
    p_deriv = prime_zeta_derivative_zero_packet(mp.mpf("1.5"), k, zeros, mobius_cutoff)
    scale = ((-1) ** (m + 1)) * (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1))
    return scale * p_deriv


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    if kind == "D":
        return gates.det_matrix(gates.hankel_matrix(mu, i))
    if kind == "G":
        return gates.det_matrix(gates.localizer_matrix(mu, i, support))
    raise ValueError(kind)


def main() -> None:
    order = 8
    prime_count = 30000
    r_cut = 64
    pair_mobius_cutoff = 60
    zero_mobius_cutoff = 24
    zero_count = 100

    zeros = zero_list(zero_count)
    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, pair_mobius_cutoff)
    finite_r3 = gates.fast_direct_tail_ells(primes, 3, 3, order)
    finite_rge4 = gates.fast_direct_tail_ells(primes, 4, r_cut, order)

    exact_tail = completion.exact_ordinary_tail_from_fold(order, pair_mobius_cutoff)
    true_mu = eta.total_ells(None, order)
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    zero_r3_full = [
        r3_layer_ell_from_zero_packet(m, zeros, zero_mobius_cutoff)
        for m in range(1, order + 1)
    ]
    zero_completed_mu = [
        finite_mu[m - 1] + zero_r3_full[m - 1] - finite_r3[m - 1]
        for m in range(1, order + 1)
    ]

    print("Pass-3 explicit-formula r=3 completion")
    print(
        f"zeros={zero_count}, zero_mobius_cutoff={zero_mobius_cutoff}, "
        f"prime_count={prime_count}, X={primes[-1]}"
    )
    print()

    print("r=3 completion comparison")
    print("m   oracle r=3 missing    zero-packet missing   zero/oracle")
    for m in range(1, order + 1):
        oracle_r3_full = exact_tail[m - 1] - finite_rge4[m - 1]
        oracle_missing = oracle_r3_full - finite_r3[m - 1]
        zero_missing = zero_r3_full[m - 1] - finite_r3[m - 1]
        print(
            f"{m:1d}  {fmt(oracle_missing, 14):>20} {fmt(zero_missing, 14):>20} "
            f"{fmt(zero_missing / oracle_missing, 8):>12}"
        )
    print()

    print("Gate comparison")
    print("gate  finite             zero-r3 completed  true completed")
    for i in range(4):
        print(
            f"D{i:<3} {fmt(gate_value('D',i,finite_mu,support), 10):>16} "
            f"{fmt(gate_value('D',i,zero_completed_mu,support), 10):>16} "
            f"{fmt(gate_value('D',i,true_mu,support), 10):>16}"
        )
    for i in range(4):
        print(
            f"G{i:<3} {fmt(gate_value('G',i,finite_mu,support), 10):>16} "
            f"{fmt(gate_value('G',i,zero_completed_mu,support), 10):>16} "
            f"{fmt(gate_value('G',i,true_mu,support), 10):>16}"
        )
    print()

    print("Interpretation")
    print("- This is the explicit-formula shape of r=3 completion.")
    print("- Finite zero packets need zero-tail certificates, especially for low cumulants.")
    print("- Agreement of higher cumulants tests the zero/Mobius machinery before proving it.")


if __name__ == "__main__":
    main()
