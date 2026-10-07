"""Finite eta scaffold through the Pass-3 Hankel/Jacobi gates.

The eta scaffold is not the final primorial construction, but it is the
finite-centered control model from Lock A2. This probe forms the total
folded cumulants

    ell_m,K = ell_m,end + ell_m,arc + ell_m,zeta(K)

and checks the first Hankel volumes and upper-radius gates. The question
is whether finite centered regularization already enters the same
positive local-lock chamber as the exact folded xi ledger.

Numerical evidence only; not a proof of RH and not the final primorial row.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp


mp.mp.dps = 100


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def eta_euler(s: mp.mpc, kmax: int) -> mp.mpc:
    total = mp.mpc(0)
    row = [mp.mpc(1)]
    for k in range(kmax + 1):
        inner = mp.fsum(((-1) ** j) * row[j] * mp.power(j + 1, -s) for j in range(k + 1))
        total += inner / (mp.mpf(2) ** (k + 1))
        row = [mp.mpc(1)] + [row[j - 1] + row[j] for j in range(1, len(row))] + [mp.mpc(1)]
    return total


def zeta_model(s: mp.mpc, kmax: int | None) -> mp.mpc:
    if kmax is None:
        return mp.zeta(s)
    return eta_euler(s, kmax) / (1 - mp.power(2, 1 - s))


def zeta_residual_ells(kmax: int | None, order: int) -> list[mp.mpf]:
    """Cauchy/DFT extraction of centered zeta residual cumulants."""
    radius = mp.mpf("0.03")
    samples = 128
    z0 = zeta_model(mp.mpf("0.5"), kmax)
    coeffs = [mp.mpc(0) for _ in range(order + 1)]
    for k in range(samples):
        theta = 2 * mp.pi * k / samples
        point = radius * mp.e ** (1j * theta)
        y = mp.sqrt(point)
        value = mp.mpf("0.5") * (
            mp.log(zeta_model(mp.mpf("0.5") + y, kmax) / z0)
            + mp.log(zeta_model(mp.mpf("0.5") - y, kmax) / z0)
        )
        for m in range(order + 1):
            coeffs[m] += value * mp.e ** (-1j * m * theta) / (radius ** m)

    out = []
    for m in range(1, order + 1):
        coeff = coeffs[m] / samples
        ell = ((-1) ** (m + 1)) * m * coeff
        out.append(mp.re(ell))
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


def total_ells(kmax: int | None, order: int) -> list[mp.mpf]:
    zeta_ells = zeta_residual_ells(kmax, order)
    return [
        ell_endpoint(m) + ell_archimedean(m) + zeta_ells[m - 1]
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


def row(kmax: int | None, radius: mp.mpf, order: int = 8) -> tuple[list[mp.mpf], list[mp.mpf]]:
    ells = total_ells(kmax, order)
    mu = ells
    d = [hankel_det(mu, i) for i in range(4)]
    g = [localizer_det(mu, i, radius) for i in range(4)]
    return d, g


def main() -> None:
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)

    print(f"R=gamma_1^-2 {fmt(radius, 24)}")
    print("\nFinite eta total Hankel volumes D_i")
    print("K        D0             D1             D2             D3")
    for kmax in (4, 8, 12, 20, 32, 48, None):
        d, _ = row(kmax, radius)
        label = "true" if kmax is None else str(kmax)
        print(
            f"{label:>4}  "
            f"{fmt(d[0], 14):>14} {fmt(d[1], 14):>14} "
            f"{fmt(d[2], 14):>14} {fmt(d[3], 14):>14}"
        )

    print("\nFinite eta total upper-radius gates det G_i^(R)")
    print("K        G0             G1             G2             G3")
    for kmax in (4, 8, 12, 20, 32, 48, None):
        _, g = row(kmax, radius)
        label = "true" if kmax is None else str(kmax)
        print(
            f"{label:>4}  "
            f"{fmt(g[0], 14):>14} {fmt(g[1], 14):>14} "
            f"{fmt(g[2], 14):>14} {fmt(g[3], 14):>14}"
        )


if __name__ == "__main__":
    main()
