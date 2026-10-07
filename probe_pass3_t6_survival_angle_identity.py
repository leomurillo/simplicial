"""Survival ratio as a residual angle identity.

For the monic Schur residual

    P_n = t^n - projection onto span{1,...,t^{n-1}},

the top-pair survival ratio from the T6 packet audit is

    rho_n = h_n / mu_{2n}.

This is the squared residual fraction of t^n after projection. In a genuine
Hilbert moment space it is sin^2(theta_n), where theta_n is the angle from
t^n to the lower polynomial subspace.

The same identity holds for the boundary-complement functional.
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


def row(moments: list[mp.mpf], n: int) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    pivot, _ = pivots.schur_pivot(moments, n)
    top_norm = moments[2 * n]
    rho = pivot / top_norm
    angle = mp.asin(mp.sqrt(rho))
    return pivot, top_norm, rho, angle


def print_table(label: str, moments: list[mp.mpf], max_n: int) -> None:
    print(label)
    print("n   pivot h/k          top norm mu_2n     rho=pivot/top    angle(rad)")
    for n in range(1, max_n + 1):
        pivot, top_norm, rho, angle = row(moments, n)
        print(
            f"{n:2d}  {fmt(pivot, 12):>16} {fmt(top_norm, 12):>18} "
            f"{fmt(rho, 12):>16} {fmt(angle, 12):>14}"
        )
    print()


def main() -> None:
    max_n = 10
    order = 2 * max_n + 6
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    boundary_mu = boundary(mu, radius)

    print("Pass-3 T6 survival angle identity")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print_table("Interior", mu, max_n)
    print_table("Boundary-complement", boundary_mu, max_n)
    print("Interpretation")
    print("- rho is the fraction of top monomial energy not explained by lower rungs.")
    print("- angle = asin(sqrt(rho)) is the residual angle to the lower polynomial ladder.")
    print("- Positivity is equivalent to a nonzero residual angle at every rung.")


if __name__ == "__main__":
    main()
