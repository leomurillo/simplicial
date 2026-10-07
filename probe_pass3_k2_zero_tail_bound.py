"""Explicit k=2 zero-tail bound for the Pass-3 completion lock.

For s=3/2 and k=2, the nontrivial-zero contribution to
(log xi)''(s) from a conjugate pair rho=1/2 +/- i gamma is

    -[1/(rho-s)^2 + 1/(conj(rho)-s)^2]
      = 2(gamma^2 - 1)/(gamma^2 + 1)^2.

The omitted zero tail after height T is therefore bounded by

    2 sum_{gamma>T} 1/gamma^2.

Using an explicit zero-counting envelope

    N(t) <= t/(2*pi) log(t/(2*pi*e)) + 7/8
            + a log t + b log log t + c,

we get

    sum_{gamma>T} 1/gamma^2
      <= 2 integral_T^infty N_upper(t) t^(-3) dt,

where we deliberately drop the negative boundary term for a simple safe
certificate.  This probe compares that bound to the observed finite-zero
tail error for (log zeta)''(3/2).

Constants default to the Hasanalizade--Shen--Wong explicit N(T) envelope:

    a=0.1038, b=0.2573, c=9.3675.

The bound is conservative; the point is to make the k=2 bottleneck
certifiable.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_explicit_formula_r3_completion as ef


mp.mp.dps = 70


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def n_upper(t: mp.mpf, a: mp.mpf, b: mp.mpf, c: mp.mpf) -> mp.mpf:
    main = t / (2 * mp.pi) * mp.log(t / (2 * mp.pi * mp.e)) + mp.mpf("0.875")
    err = a * mp.log(t) + b * mp.log(mp.log(t)) + c
    return main + err


def zero_tail_pair_bound_k2(t: mp.mpf, a: mp.mpf, b: mp.mpf, c: mp.mpf) -> mp.mpf:
    # Bound 2 sum 1/gamma^2 by dropping the negative boundary term:
    # 2 * [2 integral_T^inf N_upper(u)u^-3 du].
    integrand = lambda u: n_upper(u, a, b, c) / (u**3)
    return 4 * mp.quad(integrand, [t, mp.inf])


def zero_tail_pair_bound_k2_with_boundary(
    t: mp.mpf, zero_count_at_t: int, a: mp.mpf, b: mp.mpf, c: mp.mpf
) -> mp.mpf:
    # For f(t)=t^-2:
    # sum_{gamma>T} f(gamma) = -N(T)f(T) - int_T^inf N(u)f'(u)du
    # <= -N(T)/T^2 + 2 int_T^inf N_upper(u)u^-3 du.
    # Multiply by 2 for the conjugate-pair k=2 bound.
    integrand = lambda u: n_upper(u, a, b, c) / (u**3)
    one_sided = -mp.mpf(zero_count_at_t) / (t**2) + 2 * mp.quad(integrand, [t, mp.inf])
    return 2 * max(one_sided, mp.mpf(0))


def zero_tail_observed_k2(count: int, zeros: list[mp.mpf], exact: mp.mpf) -> mp.mpf:
    approx = ef.log_zeta_derivative_zero_packet(mp.mpf("1.5"), 2, zeros[:count])
    return exact - approx


def main() -> None:
    counts = [10, 20, 50, 100, 200, 500]
    zeros = ef.zero_list(max(counts))
    exact = mp.diff(lambda z: mp.log(mp.zeta(z)), mp.mpf("1.5"), 2)
    a = mp.mpf("0.1038")
    b = mp.mpf("0.2573")
    c = mp.mpf("9.3675")

    print("Pass-3 k=2 zero-tail bound")
    print("Envelope: |N(T)-main| <= 0.1038 log T + 0.2573 log log T + 9.3675")
    print()
    print("M   T=gamma_M          observed tail       loose bound         boundary bound      bound/observed")
    for count in counts:
        t = zeros[count - 1]
        observed = zero_tail_observed_k2(count, zeros, exact)
        bound = zero_tail_pair_bound_k2(t, a, b, c)
        sharp = zero_tail_pair_bound_k2_with_boundary(t, count, a, b, c)
        print(
            f"{count:3d} {fmt(t, 12):>16} {fmt(observed, 12):>18} "
            f"{fmt(bound, 12):>18} {fmt(sharp, 12):>18} {fmt(sharp/observed, 8):>16}"
        )

    print()
    print("Interpretation")
    print("- The k=2 zero-tail has an explicit integral certificate from N(T).")
    print("- The current bound is safe but loose; retaining the boundary term should sharpen it.")
    print("- This is enough to make the first zero-tail lock mathematically checkable.")


if __name__ == "__main__":
    main()
