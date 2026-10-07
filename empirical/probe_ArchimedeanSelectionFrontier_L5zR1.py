"""Probe the Archimedean selection frontier.

Random suffix: L5zR1

The probe verifies the positive oscillator Mellin packet that supplies the
gamma-factor side, and contrasts it with the divisor/Pick side, which still
requires boundary support.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def gamma_even_integral(s):
    alpha = s / 2
    return mp.quad(lambda x: mp.e ** (-x) * x ** (alpha - 1), [0, mp.inf])


def gamma_odd_integral(s):
    alpha = (s + 1) / 2
    return mp.quad(lambda x: mp.e ** (-x) * x ** (alpha - 1), [0, mp.inf])


def xi_s(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z):
    return xi_s(mp.mpf("0.5") + 1j * z)


def Xi_prime(z):
    return 1j * mp.diff(xi_s, mp.mpf("0.5") + 1j * z)


def m_bures(z):
    return -Xi_prime(z) / Xi(z)


def pick_diag(z):
    return mp.im(m_bures(z)) / mp.im(z)


def oscillator_character(beta, n_terms=2000):
    q = mp.e ** (-beta)
    return sum(q ** (n + mp.mpf("0.5")) for n in range(n_terms))


def oscillator_character_closed(beta):
    q = mp.e ** (-beta)
    return q ** mp.mpf("0.5") / (1 - q)


def main() -> None:
    samples = [
        mp.mpc("0.7", "1.3"),
        mp.mpc("1.2", "4.0"),
        mp.mpc("2.5", "7.0"),
    ]

    print("Positive oscillator Mellin packet:")
    for s in samples:
        even_num = gamma_even_integral(s)
        odd_num = gamma_odd_integral(s)
        even_exact = mp.gamma(s / 2)
        odd_exact = mp.gamma((s + 1) / 2)
        product_rel = abs(even_num * odd_num - even_exact * odd_exact) / abs(even_exact * odd_exact)
        print(
            "s=", mp.nstr(s, 14),
            "even_err=", mp.nstr(abs(even_num - even_exact), 4),
            "odd_err=", mp.nstr(abs(odd_num - odd_exact), 4),
            "product_rel=", mp.nstr(product_rel, 4),
        )

    print("\nPositive-energy oscillator character:")
    for beta in [mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf("1.5")]:
        approx = oscillator_character(beta)
        exact = oscillator_character_closed(beta)
        print(
            "beta=", beta,
            "character=", mp.nstr(exact, 12),
            "rel_err=", mp.nstr(abs(approx - exact) / abs(exact), 4),
        )

    print("\nCompleted xi functional equation check:")
    for s in [mp.mpc("0.4", "14.0"), mp.mpc("0.2", "21.0"), mp.mpc("0.8", "30.0")]:
        lhs = xi_s(s)
        rhs = xi_s(1 - s)
        print("s=", mp.nstr(s, 14), "rel_err=", mp.nstr(abs(lhs - rhs) / max(abs(lhs), mp.mpf("1e-80")), 4))

    print("\nPick diagonal samples for m_B:")
    points = [
        mp.mpc("0.7", "0.4"),
        mp.mpc("5.0", "0.5"),
        mp.im(mp.zetazero(1)) + mp.mpc(0, "0.5"),
        mp.im(mp.zetazero(2)) + mp.mpc(0, "0.5"),
    ]
    for z in points:
        print("z=", mp.nstr(z, 14), "Pdiag=", mp.nstr(pick_diag(z), 12))

    print("\nInterpretation:")
    print("  The oscillator packet supplies a positive gamma-factor mechanism.")
    print("  The Pick diagonal is positive on tested points, but proving it")
    print("  globally is exactly the boundary-support / RH step.")
    print("  The missing theorem is metaplectic CM selection of a positive")
    print("  canonical system whose Weyl function is -Xi'/Xi.")


if __name__ == "__main__":
    main()

