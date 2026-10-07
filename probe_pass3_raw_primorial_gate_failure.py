"""Raw primorial Euler rows through the Pass-3 local gates.

This is a diagnostic for the remaining native problem. It uses the most
literal finite prime-row scaffold:

    log zeta_{n,K}(s) = sum_{p<=p_n} sum_{r<=K} p^(-r s) / r

then centers around s=1/2 with x=y^2:

    1/2[log zeta_{n,K}(1/2+y)
       +log zeta_{n,K}(1/2-y)
       -2 log zeta_{n,K}(1/2)].

The result is intentionally compared against the eta-centered scaffold.
Raw centering alone is not analytic continuation, and this probe shows
where it fails the local Hankel/radius gates.

Numerical evidence only; not a proof.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def first_primes(count: int) -> list[int]:
    primes: list[int] = []
    n = 2
    while len(primes) < count:
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1 if n == 2 else 2
    return primes


def ell_endpoint(m: int) -> mp.mpf:
    return ((-1) ** m) * mp.mpf(4) ** m


def ell_archimedean(m: int) -> mp.mpf:
    c_arc = (
        (mp.mpf("0.5") ** (2 * m))
        * mp.polygamma(2 * m - 1, mp.mpf("0.25"))
        / factorial(2 * m)
    )
    return ((-1) ** (m + 1)) * m * c_arc


def raw_primorial_zeta_ells(prime_count: int, occupation_cutoff: int, order: int) -> list[mp.mpf]:
    primes = first_primes(prime_count)
    out: list[mp.mpf] = []
    for m in range(1, order + 1):
        coeff = mp.mpf(0)
        for p_int in primes:
            p = mp.mpf(p_int)
            logp = mp.log(p)
            for r in range(1, occupation_cutoff + 1):
                coeff += (mp.mpf(r) ** (2 * m - 1)) * (logp ** (2 * m)) * (
                    p ** (-mp.mpf(r) / 2)
                ) / factorial(2 * m)
        ell = ((-1) ** (m + 1)) * m * coeff
        out.append(ell)
    return out


def total_ells(prime_count: int, occupation_cutoff: int, order: int) -> list[mp.mpf]:
    zeta = raw_primorial_zeta_ells(prime_count, occupation_cutoff, order)
    return [
        ell_endpoint(m) + ell_archimedean(m) + zeta[m - 1]
        for m in range(1, order + 1)
    ]


def det(mat: list[list[mp.mpf]]) -> mp.mpf:
    return mp.det(mp.matrix(mat))


def hankel_det(mu: list[mp.mpf], i: int) -> mp.mpf:
    return det([[mu[a + b] for b in range(i + 1)] for a in range(i + 1)])


def localizer_det(mu: list[mp.mpf], i: int, radius: mp.mpf) -> mp.mpf:
    return det(
        [
            [radius * mu[a + b] - mu[a + b + 1] for b in range(i + 1)]
            for a in range(i + 1)
        ]
    )


def main() -> None:
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    order = 8
    occupation_cutoff = 32

    print("Raw centered primorial Euler rows at s=1/2")
    print(f"occupation cutoff K={occupation_cutoff}")
    print(f"support gate R=gamma_1^-2 {fmt(radius, 24)}")
    print()
    print("nprimes  ell_zeta_1       ell_total_1      D1              D2              G0              G1")
    for prime_count in (1, 2, 3, 5, 8, 13, 21, 34):
        zeta = raw_primorial_zeta_ells(prime_count, occupation_cutoff, order)
        mu = total_ells(prime_count, occupation_cutoff, order)
        d1 = hankel_det(mu, 1)
        d2 = hankel_det(mu, 2)
        g0 = localizer_det(mu, 0, radius)
        g1 = localizer_det(mu, 1, radius)
        print(
            f"{prime_count:7d}  {fmt(zeta[0], 12):>14} {fmt(mu[0], 12):>14} "
            f"{fmt(d1, 12):>14} {fmt(d2, 12):>14} {fmt(g0, 12):>14} {fmt(g1, 12):>14}"
        )

    print("\nExact target reference")
    print("ell_zeta_1 = 1.87343884880203013")
    print("ell_total_1 = 0.02310499311541897079")


if __name__ == "__main__":
    main()
