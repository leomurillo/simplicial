"""Worst SOS-cone directions for the Pass-3 quadratic half-compensation target.

The Schur residuals give one local basis for the thin positive cone. This
probe instead takes the minimum-eigenvalue direction of the Gram matrices

    H_n = (mu_{a+b}),        K_n = (nu_{a+b})

and splits the corresponding square observable into endpoint, Archimedean,
and zeta pieces.

If the same half-compensation pattern appears in the worst eigen-directions,
then the phenomenon belongs to the whole cone, not just the Schur basis.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta


mp.mp.dps = 100


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
    return {"total": total, "endpoint": endpoint, "arch": arch, "zeta": zeta}


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def hankel(moments: list[mp.mpf], n: int) -> mp.matrix:
    return mp.matrix([[moments[a + b] for b in range(n + 1)] for a in range(n + 1)])


def quadratic_value(coeffs: list[mp.mpf], moments: list[mp.mpf]) -> mp.mpf:
    total = mp.mpf(0)
    for a, ca in enumerate(coeffs):
        for b, cb in enumerate(coeffs):
            total += ca * cb * moments[a + b]
    return mp.re(total)


def min_eigenvector(mat: mp.matrix) -> tuple[mp.mpf, list[mp.mpf]]:
    vals, vecs = mp.eigsy(mat, eigvals_only=False)
    min_idx = min(range(len(vals)), key=lambda i: vals[i])
    coeffs = [mp.re(vecs[i, min_idx]) for i in range(mat.rows)]
    # Fix sign so top coefficient is positive, for stable display.
    if coeffs[-1] < 0:
        coeffs = [-c for c in coeffs]
    return mp.re(vals[min_idx]), coeffs


def summarize(label: str, ledgers: dict[str, list[mp.mpf]], n: int) -> None:
    mat = hankel(ledgers["total"], n)
    eig, coeffs = min_eigenvector(mat)
    endpoint = quadratic_value(coeffs, ledgers["endpoint"])
    arch = quadratic_value(coeffs, ledgers["arch"])
    zeta = quadratic_value(coeffs, ledgers["zeta"])
    total = endpoint + arch + zeta
    debt = -endpoint
    arch_excess = arch / debt - mp.mpf("0.5")
    zeta_shortfall = mp.mpf("0.5") - zeta / debt
    surplus = total / debt
    top_coeff = coeffs[-1]

    print(
        f"{label:<9} {n:2d} {fmt(eig, 10):>14} {fmt(total, 10):>14} "
        f"{fmt(debt, 10):>14} {fmt(arch_excess, 10):>14} "
        f"{fmt(zeta_shortfall, 10):>14} {fmt(surplus, 10):>14} "
        f"{fmt(top_coeff, 10):>14}"
    )


def main() -> None:
    max_n = 9
    order = 2 * max_n + 8
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    components = component_moments(order)
    boundary_components = {
        name: boundary(moments, radius) for name, moments in components.items()
    }

    print("Pass-3 T6 worst cone directions")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print(
        "ladder     n   min eig        total         debt          "
        "arch-half     half-zeta     surplus       top coeff"
    )
    for n in range(1, max_n + 1):
        summarize("interior", components, n)
        summarize("boundary", boundary_components, n)
    print()
    print("Interpretation")
    print("- The minimum-eigenvalue direction is the thinnest SOS-cone direction.")
    print("- Positive surplus means Archimedean excess beats zeta shortfall in that worst direction.")


if __name__ == "__main__":
    main()
