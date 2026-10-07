"""Christoffel/inverse-Hankel form of the Pass-3 survival angle.

For the Hankel block H_n=(mu_{a+b})_{0<=a,b<=n},

    h_n = D_n/D_{n-1} = 1 / (H_n^{-1})_{n,n}.

Therefore the survival angle satisfies

    rho_n = h_n / mu_{2n}
          = 1 / (mu_{2n} (H_n^{-1})_{n,n}).

Equivalently, the projection fraction is

    1-rho_n = v_n^T H_{n-1}^{-1} v_n / mu_{2n}.

This is the Christoffel certificate form of the T6 residual angle.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 120


def fmt(x: mp.mpf, digits: int = 14) -> str:
    return mp.nstr(x, digits)


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def hankel(moments: list[mp.mpf], n: int) -> mp.matrix:
    return mp.matrix([[moments[a + b] for b in range(n + 1)] for a in range(n + 1)])


def projection_fraction(moments: list[mp.mpf], n: int) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    block = mp.matrix([[moments[a + b] for b in range(n)] for a in range(n)])
    v = mp.matrix([moments[n + a] for a in range(n)])
    projected = mp.fdot(v, mp.lu_solve(block, v))
    return projected / moments[2 * n]


def row(moments: list[mp.mpf], n: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    pivot, _ = pivots.schur_pivot(moments, n)
    rho = pivot / moments[2 * n]
    inv = mp.inverse(hankel(moments, n))
    inverse_rho = 1 / (moments[2 * n] * inv[n, n])
    proj = projection_fraction(moments, n)
    return rho, inverse_rho, proj, rho + proj


def print_table(label: str, moments: list[mp.mpf], max_n: int) -> None:
    print(label)
    print("n   rho pivot/top       rho inverse-H      projection frac    rho+proj")
    for n in range(1, max_n + 1):
        rho, inverse_rho, proj, total = row(moments, n)
        print(
            f"{n:2d}  {fmt(rho, 14):>18} {fmt(inverse_rho, 14):>18} "
            f"{fmt(proj, 14):>18} {fmt(total, 14):>14}"
        )
    print()


def main() -> None:
    max_n = 8
    order = 2 * max_n + 8
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    boundary_mu = boundary(mu, radius)

    print("Pass-3 T6 Christoffel angle certificate")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print_table("Interior", mu, max_n)
    print_table("Boundary-complement", boundary_mu, max_n)
    print("Interpretation")
    print("- rho equals the inverse-Hankel Christoffel expression.")
    print("- rho+projection fraction equals 1.")
    print("- Positivity becomes nonzero Christoffel distance from t^n to lower rungs.")


if __name__ == "__main__":
    main()
