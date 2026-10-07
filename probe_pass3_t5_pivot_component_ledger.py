"""Component ledger for T5 Schur pivots.

Schur pivots are nonlinear functions of the moments. But after the total
moment ledger chooses the monic residual polynomial P_n, the pivot is the
linear square observable

    h_n = L_total(P_n^2).

This probe evaluates that same residual square against the endpoint,
Archimedean, and centered-zeta pieces:

    h_n = L_end(P_n^2) + L_arc(P_n^2) + L_zeta(P_n^2).

It repeats the same calculation for the boundary-complement functional
L_R(f)=L((R-t)f(t)).

Numerical evidence only; the purpose is to expose which carrier pieces pay
for the positive pivot residues.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def ell_endpoint(m: int) -> mp.mpf:
    return ((-1) ** m) * mp.mpf(4) ** m


def ell_archimedean(m: int) -> mp.mpf:
    c_arc = (
        (mp.mpf("0.5") ** (2 * m))
        * mp.polygamma(2 * m - 1, mp.mpf("0.25"))
        / factorial(2 * m)
    )
    return ((-1) ** (m + 1)) * m * c_arc


def component_moments(order: int) -> dict[str, list[mp.mpf]]:
    total = eta.total_ells(None, order)
    endpoint = [ell_endpoint(k + 1) for k in range(order)]
    arch = [ell_archimedean(k + 1) for k in range(order)]
    zeta = [total[k] - endpoint[k] - arch[k] for k in range(order)]
    return {
        "total": total,
        "endpoint": endpoint,
        "arch": arch,
        "zeta": zeta,
    }


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def square_value(poly: list[mp.mpf], moments: list[mp.mpf]) -> mp.mpf:
    total = mp.mpf(0)
    for i, ai in enumerate(poly):
        for j, aj in enumerate(poly):
            total += ai * aj * moments[i + j]
    return mp.re(total)


def monic_residual(moments: list[mp.mpf], n: int) -> list[mp.mpf]:
    if n == 0:
        return [mp.mpf(1)]
    _, coeffs = pivots.schur_pivot(moments, n)
    return coeffs + [mp.mpf(1)]


def print_component_table(
    label: str,
    basis_moments: list[mp.mpf],
    ledgers: dict[str, list[mp.mpf]],
    max_n: int,
) -> None:
    print(label)
    print("n   total pivot          endpoint piece       arch piece           zeta piece")
    rows: list[tuple[int, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
    for n in range(max_n + 1):
        poly = monic_residual(basis_moments, n)
        pieces = {
            name: square_value(poly, moments)
            for name, moments in ledgers.items()
            if name != "total"
        }
        total_piece = sum(pieces.values())
        rows.append((n, total_piece, pieces["endpoint"], pieces["arch"], pieces["zeta"]))
        print(
            f"{n:1d}  {fmt(total_piece, 16):>20} "
            f"{fmt(pieces['endpoint'], 16):>20} "
            f"{fmt(pieces['arch'], 16):>20} "
            f"{fmt(pieces['zeta'], 16):>20}"
        )
    print()
    print("normalized compensation against -endpoint")
    print("n   total/(-end)         arch/(-end)        zeta/(-end)        arch-zeta")
    for n, total_piece, endpoint, arch, zeta in rows:
        scale = -endpoint
        print(
            f"{n:1d}  {fmt(total_piece/scale, 12):>18} "
            f"{fmt(arch/scale, 12):>18} "
            f"{fmt(zeta/scale, 12):>18} "
            f"{fmt((arch-zeta)/scale, 12):>18}"
        )
    print()
    print("midline defects around half-compensation")
    print("n   arch-half           half-zeta           surplus")
    for n, total_piece, endpoint, arch, zeta in rows:
        scale = -endpoint
        arch_half = arch / scale - mp.mpf("0.5")
        half_zeta = mp.mpf("0.5") - zeta / scale
        surplus = total_piece / scale
        print(
            f"{n:1d}  {fmt(arch_half, 12):>18} "
            f"{fmt(half_zeta, 12):>18} "
            f"{fmt(surplus, 12):>18}"
        )
    print()


def main() -> None:
    max_n = 4
    order = 2 * max_n + 6
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    components = component_moments(order)
    boundary_components = {
        name: boundary(moments, radius) for name, moments in components.items()
    }

    print("Pass-3 T5 pivot component ledger")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print_component_table(
        "Interior residual squares P_n under total orthogonalization",
        components["total"],
        components,
        max_n,
    )
    print_component_table(
        "Boundary-complement residual squares Q_n under total boundary orthogonalization",
        boundary_components["total"],
        boundary_components,
        max_n,
    )

    print("Interpretation")
    print("- The residual polynomial is chosen by the completed ledger.")
    print("- The same residual square can then be charged to endpoint, Archimedean, and zeta pieces.")
    print("- A native proof should show that the centered sum pays a positive pivot at every rung.")


if __name__ == "__main__":
    main()
