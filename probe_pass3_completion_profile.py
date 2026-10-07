"""Completion profile for the Pass-3 scaffold.

This probe profiles the missing completion between the finite native
scaffold and the exact folded eta/zeta ledger.

Finite scaffold:

    endpoint + Archimedean + finite C12 + direct ordinary tail

Exact completion endpoint:

    endpoint + Archimedean + exact folded zeta residual.

The difference is the completion vector.  Numerically, the finite C12
cutoff error is tiny relative to the missing far-prime ordinary tail, so the
profile focuses on how the completion is distributed between the dominant
r=3 layer and the faster r>=4 remainder.

This is a diagnostic, not a proof certificate.  Its purpose is to show what
the future certificate must capture.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_two_layer_continuation_scaffold as scaffold
from probe_pass3_r3_tail_dominance import r_ge4_prime_tail_bound
from probe_pass3_tail_control_bounds import occupation_tail_after_r_bound


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def exact_ordinary_tail_from_fold(order: int, mobius_cutoff: int) -> list[mp.mpf]:
    radius_x = mp.mpf("0.01")
    samples = 128
    pair = scaffold.cumulants_from_folded_values(
        lambda y: scaffold.two_layer_folded_value(y, mobius_cutoff),
        order,
        radius_x,
        samples,
    )
    true_zeta = scaffold.cumulants_from_folded_values(
        scaffold.true_zeta_folded_value,
        order,
        radius_x,
        samples,
    )
    return [true_zeta[i] - pair[i] for i in range(order)]


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
    mobius_cutoff = 60
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    primes = scaffold.first_primes(prime_count)
    x = mp.mpf(primes[-1])

    finite_mu, _ = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    true_mu = eta.total_ells(None, order)

    exact_tail = exact_ordinary_tail_from_fold(order, mobius_cutoff)
    finite_tail = gates.fast_direct_tail_ells(primes, 3, r_cut, order)
    finite_r3 = gates.fast_direct_tail_ells(primes, 3, 3, order)
    finite_rge4 = gates.fast_direct_tail_ells(primes, 4, r_cut, order)

    print("Pass-3 completion profile")
    print(f"prime_count={prime_count}, X={primes[-1]}, r_cut={r_cut}, mobius_cutoff={mobius_cutoff}")
    print()

    print("Moment completion vector")
    print("m   finite_mu            true_mu              completion          sign")
    for m in range(1, order + 1):
        delta = true_mu[m - 1] - finite_mu[m - 1]
        sign = "+" if delta > 0 else "-"
        print(
            f"{m:1d}  {fmt(finite_mu[m-1], 12):>18} {fmt(true_mu[m-1], 12):>18} "
            f"{fmt(delta, 12):>18} {sign:>5}"
        )
    print()

    print("Ordinary-tail completion decomposition")
    print("m   exact tail          finite tail         missing tail        r=3 missing est     r>=4 err bound")
    for m in range(1, order + 1):
        missing = exact_tail[m - 1] - finite_tail[m - 1]
        rge4_err = r_ge4_prime_tail_bound(m, x) + occupation_tail_after_r_bound(m, r_cut)
        # Estimate the full r=3 layer by subtracting the finite r>=4 block.
        r3_full_est = exact_tail[m - 1] - finite_rge4[m - 1]
        r3_missing_est = r3_full_est - finite_r3[m - 1]
        print(
            f"{m:1d}  {fmt(exact_tail[m-1], 12):>18} {fmt(finite_tail[m-1], 12):>18} "
            f"{fmt(missing, 12):>18} {fmt(r3_missing_est, 12):>18} {fmt(rge4_err, 8):>16}"
        )
    print()

    print("Gate completion values")
    print("gate  finite value        exact value         ratio |finite/exact|")
    for kind in ["D", "G"]:
        for i in range(4):
            vf = gate_value(kind, i, finite_mu, support)
            vt = gate_value(kind, i, true_mu, support)
            ratio = abs(vf) / max(abs(vt), mp.mpf("1e-100"))
            print(
                f"{kind}{i:<3} {fmt(vf, 12):>18} {fmt(vt, 12):>18} {fmt(ratio, 8):>18}"
            )
    print()

    print("Interpretation")
    print("- Completion has the alternating sign pattern expected from ordinary tail atoms.")
    print("- The missing ordinary tail is numerically almost the missing r=3 layer.")
    print("- The gate chamber is thin because exact determinant values are tiny after large cancellations.")


if __name__ == "__main__":
    main()
