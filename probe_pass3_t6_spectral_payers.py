"""Which spectral atoms pay the Pass-3 residual angle?

Under the trace-gauge spectral model

    mu_k = sum_j lambda_j^{k+1}, lambda_j=gamma_j^{-2},

the Schur pivot has the spectral expansion

    h_n = sum_j lambda_j P_n(lambda_j)^2.

The boundary-complement pivot has weights

    k_n = sum_{j>=2} (R-lambda_j) lambda_j Q_n(lambda_j)^2,

because the first atom at R=lambda_1 is killed.

This probe shows how much of each pivot is paid by the first few spectral
atoms. Numerical evidence only; it uses the computed residual polynomials
from the exact folded ledger.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 120


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def lambdas(count: int) -> list[mp.mpf]:
    out = []
    for k in range(1, count + 1):
        gamma = mp.im(mp.zetazero(k))
        out.append(1 / (gamma * gamma))
    return out


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def monic_residual(moments: list[mp.mpf], n: int) -> list[mp.mpf]:
    if n == 0:
        return [mp.mpf(1)]
    _, coeffs = pivots.schur_pivot(moments, n)
    return coeffs + [mp.mpf(1)]


def poly_value(poly: list[mp.mpf], x: mp.mpf) -> mp.mpf:
    total = mp.mpf(0)
    for coeff in reversed(poly):
        total = total * x + coeff
    return total


def print_payers(label: str, poly: list[mp.mpf], pivot: mp.mpf, lam: list[mp.mpf], radius: mp.mpf | None = None) -> None:
    rows = []
    for idx, la in enumerate(lam, start=1):
        if radius is None:
            weight = la
        else:
            weight = (radius - la) * la
        if weight <= 0:
            continue
        contribution = weight * poly_value(poly, la) ** 2
        rows.append((idx, la, contribution, contribution / pivot))
    rows.sort(key=lambda row: row[2], reverse=True)

    print(label)
    print("rank zero#  lambda_j             contribution/pivot    cumulative")
    cumulative = mp.mpf(0)
    for rank, (idx, la, contribution, share) in enumerate(rows[:12], start=1):
        cumulative += share
        print(
            f"{rank:2d}   {idx:3d}  {fmt(la, 12):>16} "
            f"{fmt(share, 12):>20} {fmt(cumulative, 12):>14}"
        )
    print()


def main() -> None:
    max_n = 8
    zero_count = 80
    order = 2 * max_n + 8
    lam = lambdas(zero_count)
    radius = lam[0]
    mu = eta.total_ells(None, order)
    boundary_mu = boundary(mu, radius)

    print("Pass-3 T6 spectral payers")
    print(f"using first {zero_count} folded atoms")
    print(f"R=lambda_1={fmt(radius, 20)}")
    print()

    for n in (2, 3, 4, 6, 8):
        pivot, _ = pivots.schur_pivot(mu, n)
        poly = monic_residual(mu, n)
        print_payers(f"Interior n={n}", poly, pivot, lam, radius=None)

        bpivot, _ = pivots.schur_pivot(boundary_mu, n)
        bpoly = monic_residual(boundary_mu, n)
        print_payers(f"Boundary n={n}", bpoly, bpivot, lam, radius=radius)

    print("Interpretation")
    print("- Contributions are sorted by actual share of the residual pivot.")
    print("- If one atom dominated, one row would be near 1. Distributed shares mean a tail packet pays the residual.")


if __name__ == "__main__":
    main()
