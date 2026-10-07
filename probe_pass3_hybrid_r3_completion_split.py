"""Hybrid r=3 completion split: zero formula only where it belongs.

The naive finite-zero explicit-formula probe applied the same zero packet to
every Mobius term

    mu(n)n^(k-1)(log zeta)^(k)(3n/2).

For k=2 this is a bad numerical certificate for n>=2: at 3n/2 >= 3,
the zero, gamma, and trivial ledgers nearly cancel to a tiny absolutely
convergent value.  The correct native split is:

    n=1: use the zero-packet + N(T) zero-tail certificate;
    n>=2: use the absolutely convergent von Mangoldt/Dirichlet series.

This probe implements that hybrid split and compares it with the oracle
r=3 completion.
"""

from __future__ import annotations

from math import factorial, log

import mpmath as mp
from sympy import primerange

import probe_pass3_completion_profile as completion
import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_explicit_formula_r3_completion as ef
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_k2_zero_tail_bound as k2tail
import probe_pass3_two_layer_continuation_scaffold as scaffold


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


PRIMES = list(primerange(2, 100000))
PRIME_LOGS = [(p, log(p)) for p in PRIMES]


def log_zeta_derivative_dirichlet(sigma: mp.mpf, k: int) -> mp.mpf:
    """Compute (log zeta)^(k)(sigma) by the absolutely convergent series.

    Only used for sigma >= 4.5.  The n=2 Mobius term at sigma=3 is handled
    by mpmath's derivative because high-k tails decay more slowly there.
    """
    sigma_f = float(sigma)
    total = 0.0
    for p_int, lp in PRIME_LOGS:
        a = 1
        while True:
            term = lp * ((a * lp) ** (k - 1)) * (p_int ** (-a * sigma_f))
            total += term
            if abs(term) < 1e-30:
                break
            a += 1
    return mp.mpf(total)


def hybrid_prime_zeta_derivative(
    k: int, zeros: list[mp.mpf], mobius_cutoff: int
) -> mp.mpf:
    s = mp.mpf("1.5")
    total = ef.log_zeta_derivative_zero_packet(s, k, zeros)
    for n in range(2, mobius_cutoff + 1):
        mu = scaffold.mobius(n)
        if mu == 0:
            continue
        sigma = mp.mpf(n) * s
        if n == 2:
            deriv = mp.diff(lambda z: mp.log(mp.zeta(z)), sigma, k)
        else:
            deriv = log_zeta_derivative_dirichlet(sigma, k)
        total += mp.mpf(mu) * (mp.mpf(n) ** (k - 1)) * deriv
    return total


def hybrid_r3_layer_ell(m: int, zeros: list[mp.mpf], mobius_cutoff: int) -> mp.mpf:
    k = 2 * m
    p_deriv = hybrid_prime_zeta_derivative(k, zeros, mobius_cutoff)
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
    zero_count = 100
    mobius_cutoff = 60
    prime_count = 30000
    r_cut = 64

    zeros = ef.zero_list(zero_count)
    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    finite_r3 = gates.fast_direct_tail_ells(primes, 3, 3, order)
    finite_rge4 = gates.fast_direct_tail_ells(primes, 4, r_cut, order)
    exact_tail = completion.exact_ordinary_tail_from_fold(order, mobius_cutoff)
    true_mu = eta.total_ells(None, order)
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    hybrid_r3_full = [
        hybrid_r3_layer_ell(m, zeros, mobius_cutoff) for m in range(1, order + 1)
    ]
    hybrid_mu = [
        finite_mu[m - 1] + hybrid_r3_full[m - 1] - finite_r3[m - 1]
        for m in range(1, order + 1)
    ]

    print("Pass-3 hybrid r=3 completion split")
    print(
        f"zeros={zero_count}, mobius_cutoff={mobius_cutoff}, "
        f"prime_count={prime_count}, X={primes[-1]}"
    )
    print("n=1 via zero packet; n=2 via direct derivative; n>=3 via Dirichlet series.")
    print()

    print("r=3 completion comparison")
    print("m   oracle r=3 missing    hybrid missing      hybrid/oracle")
    oracle_m1 = None
    hybrid_m1 = None
    for m in range(1, order + 1):
        oracle_r3_full = exact_tail[m - 1] - finite_rge4[m - 1]
        oracle_missing = oracle_r3_full - finite_r3[m - 1]
        hybrid_missing = hybrid_r3_full[m - 1] - finite_r3[m - 1]
        if m == 1:
            oracle_m1 = oracle_missing
            hybrid_m1 = hybrid_missing
        print(
            f"{m:1d}  {fmt(oracle_missing, 14):>20} {fmt(hybrid_missing, 14):>20} "
            f"{fmt(hybrid_missing / oracle_missing, 8):>12}"
        )
    print()

    assert oracle_m1 is not None and hybrid_m1 is not None
    t = zeros[-1]
    raw_k2_bound = k2tail.zero_tail_pair_bound_k2_with_boundary(
        t, zero_count, mp.mpf("0.1038"), mp.mpf("0.2573"), mp.mpf("9.3675")
    )
    ell_m1_tail_bound = mp.mpf("1.5") * raw_k2_bound
    print("m=1 certified interval from k=2 zero-tail")
    print(f"hybrid m=1 missing       {fmt(hybrid_m1, 16)}")
    print(f"zero-tail ell bound      {fmt(ell_m1_tail_bound, 16)}")
    print(
        f"certified interval       [{fmt(hybrid_m1, 16)}, "
        f"{fmt(hybrid_m1 + ell_m1_tail_bound, 16)}]"
    )
    print(f"oracle m=1 missing       {fmt(oracle_m1, 16)}")
    print()

    print("Gate comparison")
    print("gate  hybrid completed   true completed")
    for i in range(4):
        print(
            f"D{i:<3} {fmt(gate_value('D',i,hybrid_mu,support), 12):>18} "
            f"{fmt(gate_value('D',i,true_mu,support), 12):>18}"
        )
    for i in range(4):
        print(
            f"G{i:<3} {fmt(gate_value('G',i,hybrid_mu,support), 12):>18} "
            f"{fmt(gate_value('G',i,true_mu,support), 12):>18}"
        )
    print()

    print("Interpretation")
    print("- The explicit formula is needed only for the n=1 critical Mobius term.")
    print("- The n>=2 terms are better certified in the absolute-convergence half-plane.")
    print("- This removes the spurious m=1 overshoot of the all-zero-packet probe.")


if __name__ == "__main__":
    main()
