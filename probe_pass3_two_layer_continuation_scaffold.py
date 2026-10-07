"""Two-layer continuation scaffold for the Pass-3 native target.

The raw prime row fails at the critical center because occupation
layers r=1 and r=2 diverge. This probe replaces those two layers by the
continued prime-zeta combination

    C_12(s) = P(s) + 1/2 P(2s),

where

    P(s) = sum_{k>=1} mu(k)/k log zeta(k s).

In the combination C_12, the singular log zeta(2s) coefficient cancels:

    coeff_n = (mu(n) + 1_{2|n} mu(n/2)) / n,
    coeff_2 = 0.

The exact r>=3 tail is recovered as the complement to the true zeta
residual after subtracting the continued r=1,2 pair. A finite ordinary
prime sum is then compared against that exact tail to expose the
tail-control cost. This is the first executable model of the proposed
native replacement:

    continued (r=1,2) + ordinary (r>=3).

Numerical evidence only; not a proof of the primorial construction.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp


mp.mp.dps = 90
S0 = mp.mpf("0.5")


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def first_primes(count: int) -> list[int]:
    primes: list[int] = []
    n = 2
    while len(primes) < count:
        ok = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                ok = False
                break
        if ok:
            primes.append(n)
        n += 1 if n == 2 else 2
    return primes


def mobius(n: int) -> int:
    m = n
    count = 0
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            count += 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1 if p == 2 else 2
    if m > 1:
        count += 1
    return -1 if count % 2 else 1


def pair_coeff(n: int) -> mp.mpf:
    coeff = mp.mpf(mobius(n)) / n
    if n % 2 == 0:
        coeff += mp.mpf(mobius(n // 2)) / n
    return coeff


def two_layer_folded_value(y: mp.mpc, mobius_cutoff: int) -> mp.mpc:
    total = mp.mpc(0)
    for n in range(1, mobius_cutoff + 1):
        if n == 2:
            continue
        coeff = pair_coeff(n)
        if coeff == 0:
            continue
        center = mp.zeta(n * S0)
        plus = mp.zeta(n * (S0 + y))
        minus = mp.zeta(n * (S0 - y))
        total += coeff * mp.mpf("0.5") * (
            mp.log(plus / center) + mp.log(minus / center)
        )
    return total


def true_zeta_folded_value(y: mp.mpc) -> mp.mpc:
    center = mp.zeta(S0)
    return mp.mpf("0.5") * (
        mp.log(mp.zeta(S0 + y) / center)
        + mp.log(mp.zeta(S0 - y) / center)
    )


def cumulants_from_folded_values(value_fn, order: int, radius: mp.mpf, samples: int) -> list[mp.mpf]:
    coeffs = [mp.mpc(0) for _ in range(order + 1)]
    for k in range(samples):
        theta = 2 * mp.pi * k / samples
        point = radius * mp.e ** (1j * theta)
        y = mp.sqrt(point)
        value = value_fn(y)
        for m in range(order + 1):
            coeffs[m] += value * mp.e ** (-1j * m * theta) / (radius ** m)

    out: list[mp.mpf] = []
    for m in range(1, order + 1):
        coeff = coeffs[m] / samples
        ell = ((-1) ** (m + 1)) * m * coeff
        out.append(mp.re(ell))
    return out


def direct_tail_ells(primes: list[int], r_min: int, r_max: int, order: int) -> list[mp.mpf]:
    out: list[mp.mpf] = []
    for m in range(1, order + 1):
        coeff = mp.mpf(0)
        for p_int in primes:
            p = mp.mpf(p_int)
            logp = mp.log(p)
            for r in range(r_min, r_max + 1):
                coeff += (mp.mpf(r) ** (2 * m - 1)) * (logp ** (2 * m)) * (
                    p ** (-mp.mpf(r) / 2)
                ) / factorial(2 * m)
        ell = ((-1) ** (m + 1)) * m * coeff
        out.append(ell)
    return out


def ell_endpoint(m: int) -> mp.mpf:
    return ((-1) ** m) * mp.mpf(4) ** m


def ell_archimedean(m: int) -> mp.mpf:
    c_arc = (
        (mp.mpf("0.5") ** (2 * m))
        * mp.polygamma(2 * m - 1, mp.mpf("0.25"))
        / factorial(2 * m)
    )
    return ((-1) ** (m + 1)) * m * c_arc


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
    order = 8
    samples = 128
    # Keep sqrt(radius_x) < 1/6 so the r=3 tail remains inside
    # absolute convergence throughout the Cauchy circle.
    radius_x = mp.mpf("0.01")
    mobius_cutoff = 60
    prime_count = 3000
    r_max = 32

    print("Two-layer continuation scaffold")
    print(f"mobius cutoff={mobius_cutoff}, prime_count={prime_count}, r_max={r_max}")
    print("\nFirst coefficients of C_12(s)=P(s)+1/2 P(2s)")
    print("n   coeff of log zeta(n s)")
    for n in range(1, 13):
        print(f"{n:2d}  {fmt(pair_coeff(n), 14):>18}")

    pair = cumulants_from_folded_values(
        lambda y: two_layer_folded_value(y, mobius_cutoff),
        order,
        radius_x,
        samples,
    )
    true_zeta = cumulants_from_folded_values(true_zeta_folded_value, order, radius_x, samples)
    exact_tail = [true_zeta[i] - pair[i] for i in range(order)]

    print("\nExact split: true zeta residual = continued pair + exact tail")
    print("m      true                  continued pair        exact tail")
    for m in range(1, 6):
        print(
            f"{m:1d}  {fmt(true_zeta[m-1], 18):>22} "
            f"{fmt(pair[m-1], 18):>22} {fmt(exact_tail[m-1], 18):>22}"
        )

    direct_tail = direct_tail_ells(first_primes(prime_count), 3, r_max, order)
    print("\nDirect finite ordinary tail error against exact tail")
    print("m      direct r=3..32,p<=p_3000     exact tail            abs.err")
    for m in range(1, 6):
        err = abs(direct_tail[m - 1] - exact_tail[m - 1])
        print(
            f"{m:1d}  {fmt(direct_tail[m-1], 18):>28} "
            f"{fmt(exact_tail[m-1], 18):>22} {fmt(err, 8):>12}"
        )

    combined_zeta = [pair[i] + direct_tail[i] for i in range(order)]
    total_mu = [
        ell_endpoint(m) + ell_archimedean(m) + combined_zeta[m - 1]
        for m in range(1, order + 1)
    ]
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    print("\nTotal folded gates from finite direct-tail scaffold")
    print("D0,D1,D2,D3")
    print(" ".join(fmt(hankel_det(total_mu, i), 16) for i in range(4)))
    print("G0,G1,G2,G3")
    print(" ".join(fmt(localizer_det(total_mu, i, support), 16) for i in range(4)))


if __name__ == "__main__":
    main()
