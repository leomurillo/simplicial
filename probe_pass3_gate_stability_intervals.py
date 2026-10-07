"""Gate-aware stability intervals for Pass-3 tail certificates.

Scalar tail bounds are not enough: the Pass-3 gates are Hankel/Jacobi
determinants, so each scalar moment error must be propagated through a
determinant.

This probe builds a finite scaffold

    endpoint + Archimedean + continued (r=1,2) + direct ordinary tail

and assigns each moment ell_m an ordinary-tail error radius

    eps_m =
      theta-certified r=3 prime tail after X
      + faster r>=4 prime tail after X
      + occupation tail after R.

For each determinant gate, it computes a conservative Leibniz perturbation
radius:

    |det(A+E)-det(A)|
      <= sum_perm ( prod_i(|a_i,perm(i)|+e_i,perm(i)|)
                    - prod_i |a_i,perm(i)| ).

If the resulting interval avoids zero, the gate is sign-stable under the
ordinary-tail certificate. If it crosses zero, the gate is unresolved at
that cutoff/certificate strength.

This does not include the separate truncation error of the continued
two-layer Mobius scaffold; it isolates the ordinary-tail gate propagation.
"""

from __future__ import annotations

from math import factorial, log
from itertools import permutations

import mpmath as mp

import probe_pass3_two_layer_continuation_scaffold as scaffold
from probe_pass3_r3_tail_dominance import r_ge4_prime_tail_bound
from probe_pass3_r3_theta_tail_certificate import r3_theta_bound
from probe_pass3_tail_control_bounds import occupation_tail_after_r_bound


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def hankel_matrix(mu: list[mp.mpf], i: int) -> list[list[mp.mpf]]:
    return [[mu[a + b] for b in range(i + 1)] for a in range(i + 1)]


def hankel_error_matrix(eps: list[mp.mpf], i: int) -> list[list[mp.mpf]]:
    return [[eps[a + b] for b in range(i + 1)] for a in range(i + 1)]


def localizer_matrix(mu: list[mp.mpf], i: int, radius: mp.mpf) -> list[list[mp.mpf]]:
    return [
        [radius * mu[a + b] - mu[a + b + 1] for b in range(i + 1)]
        for a in range(i + 1)
    ]


def localizer_error_matrix(
    eps: list[mp.mpf], i: int, radius: mp.mpf
) -> list[list[mp.mpf]]:
    return [
        [abs(radius) * eps[a + b] + eps[a + b + 1] for b in range(i + 1)]
        for a in range(i + 1)
    ]


def det_matrix(mat: list[list[mp.mpf]]) -> mp.mpf:
    return mp.det(mp.matrix(mat))


def determinant_perturbation_radius(
    mat: list[list[mp.mpf]], err: list[list[mp.mpf]]
) -> mp.mpf:
    n = len(mat)
    total = mp.mpf(0)
    for perm in permutations(range(n)):
        prod_plus = mp.mpf(1)
        prod_base = mp.mpf(1)
        for row, col in enumerate(perm):
            prod_plus *= abs(mat[row][col]) + err[row][col]
            prod_base *= abs(mat[row][col])
        total += prod_plus - prod_base
    return total


def gate_interval(nominal: mp.mpf, radius: mp.mpf) -> tuple[mp.mpf, mp.mpf, str]:
    lo = nominal - radius
    hi = nominal + radius
    if lo > 0:
        verdict = "positive"
    elif hi < 0:
        verdict = "negative"
    else:
        verdict = "unresolved"
    return lo, hi, verdict


def ordinary_tail_error_radii(
    order: int, x: mp.mpf, r_cut: int, a_theta: mp.mpf
) -> list[mp.mpf]:
    radii: list[mp.mpf] = []
    for m in range(1, order + 1):
        radii.append(
            r3_theta_bound(m, x, a_theta)
            + r_ge4_prime_tail_bound(m, x)
            + occupation_tail_after_r_bound(m, r_cut)
        )
    return radii


def finite_scaffold_mu(
    order: int, prime_count: int, r_cut: int, mobius_cutoff: int
) -> tuple[list[mp.mpf], list[int]]:
    primes = scaffold.first_primes(prime_count)
    radius_x = mp.mpf("0.01")
    samples = 128
    pair = scaffold.cumulants_from_folded_values(
        lambda y: scaffold.two_layer_folded_value(y, mobius_cutoff),
        order,
        radius_x,
        samples,
    )
    direct_tail = fast_direct_tail_ells(primes, 3, r_cut, order)
    mu = [
        scaffold.ell_endpoint(m) + scaffold.ell_archimedean(m) + pair[m - 1] + direct_tail[m - 1]
        for m in range(1, order + 1)
    ]
    return mu, primes


def fast_direct_tail_ells(
    primes: list[int], r_min: int, r_max: int, order: int
) -> list[mp.mpf]:
    """Float-accelerated direct ordinary tail.

    The direct tail is only the nominal center of a much wider certified
    interval, so ordinary double precision is enough for this probe and is
    dramatically faster than doing millions of mpmath operations.
    """
    coeffs = [0.0 for _ in range(order)]
    facts = [factorial(2 * m) for m in range(1, order + 1)]
    for p in primes:
        lp = log(p)
        log_powers = [lp ** (2 * m) for m in range(1, order + 1)]
        p_factor = p ** (-0.5)
        p_power = p ** (-r_min / 2)
        for r in range(r_min, r_max + 1):
            r_powers = [r ** (2 * m - 1) for m in range(1, order + 1)]
            for m in range(1, order + 1):
                coeffs[m - 1] += r_powers[m - 1] * log_powers[m - 1] * p_power / facts[m - 1]
            p_power *= p_factor
    out: list[mp.mpf] = []
    for m, coeff in enumerate(coeffs, start=1):
        out.append(mp.mpf(((-1) ** (m + 1)) * m * coeff))
    return out


def print_gate_table(
    label: str,
    matrices: list[tuple[str, list[list[mp.mpf]], list[list[mp.mpf]]]],
) -> None:
    print(label)
    print("gate  nominal              radius               interval                         verdict")
    for name, mat, err in matrices:
        nominal = det_matrix(mat)
        radius = determinant_perturbation_radius(mat, err)
        lo, hi, verdict = gate_interval(nominal, radius)
        print(
            f"{name:<4} {fmt(nominal, 12):>18} {fmt(radius, 12):>20} "
            f"[{fmt(lo, 8):>12}, {fmt(hi, 8):>12}] {verdict:>12}"
        )
    print()


def main() -> None:
    order = 8
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    a_theta = mp.mpf("1.01")
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    mu, primes = finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    x = mp.mpf(primes[-1])
    eps = ordinary_tail_error_radii(order, x, r_cut, a_theta)

    print("Pass-3 gate stability intervals")
    print(
        f"prime_count={prime_count}, X={primes[-1]}, r_cut={r_cut}, "
        f"mobius_cutoff={mobius_cutoff}, A_theta={a_theta}"
    )
    print(f"support radius gamma_1^-2={fmt(support, 18)}")
    print()

    print("Moment error radii from ordinary-tail certificates")
    print("m   nominal ell_m          eps_m               eps/|ell_m|")
    for m in range(1, order + 1):
        rel = eps[m - 1] / max(abs(mu[m - 1]), mp.mpf("1e-80"))
        print(
            f"{m:1d}  {fmt(mu[m-1], 14):>18} {fmt(eps[m-1], 14):>18} {fmt(rel, 8):>14}"
        )
    print()

    hankel = [
        (f"D{i}", hankel_matrix(mu, i), hankel_error_matrix(eps, i))
        for i in range(4)
    ]
    localizer = [
        (f"G{i}", localizer_matrix(mu, i, support), localizer_error_matrix(eps, i, support))
        for i in range(4)
    ]

    print_gate_table("Hankel gates D_i", hankel)
    print_gate_table("Upper-radius Jacobi gates G_i", localizer)

    print("Interpretation")
    print("- A positive verdict means the scalar tail certificates preserve that gate's sign.")
    print("- Unresolved means the scalar tail intervals are still too wide for that determinant.")
    print("- This probe isolates ordinary-tail error; the continued pair needs its own certificate.")


if __name__ == "__main__":
    main()
