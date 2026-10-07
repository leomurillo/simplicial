"""Spectral product estimate for Pass-3 survival angles.

If the monic residual P_n locks onto the largest n atoms

    lambda_j = gamma_j^{-2},

then a first survival-angle estimate is

    h_n ~ w_{n+1} prod_{j=1}^n (lambda_j-lambda_{n+1})^2,
    mu_{2n} ~ w_1 lambda_1^{2n}.

For the trace-gauge ledger used here, w_j=lambda_j, so

    rho_n = h_n/mu_{2n}
          ~ lambda_{n+1} prod_{j=1}^n (lambda_j-lambda_{n+1})^2
             / lambda_1^{2n+1}.

For the boundary-complement ledger L_R=(R-t)L, the first atom is killed.
The active weights are w_j^R=(R-lambda_j)lambda_j, j>=2, and Q_n locks onto
lambda_2,...,lambda_{n+1}.

Numerical evidence only; this tests the asymptotic target.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 140


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


def actual_rho(moments: list[mp.mpf], n: int) -> mp.mpf:
    pivot, _ = pivots.schur_pivot(moments, n)
    return pivot / moments[2 * n]


def interior_estimate(lam: list[mp.mpf], n: int) -> mp.mpf:
    target = lam[n]  # lambda_{n+1}
    product = mp.mpf(1)
    for j in range(n):
        product *= (lam[j] - target) ** 2
    return target * product / (lam[0] ** (2 * n + 1))


def boundary_estimate(lam: list[mp.mpf], n: int) -> mp.mpf:
    radius = lam[0]
    target = lam[n + 1]  # lambda_{n+2}
    product = mp.mpf(1)
    for j in range(1, n + 1):
        product *= (lam[j] - target) ** 2
    numerator = (radius - target) * target * product
    denominator = (radius - lam[1]) * lam[1] ** (2 * n + 1)
    return numerator / denominator


def main() -> None:
    max_n = 10
    order = 2 * max_n + 6
    lam = lambdas(max_n + 3)
    radius = lam[0]
    mu = eta.total_ells(None, order)
    boundary_mu = boundary(mu, radius)

    print("Pass-3 T6 spectral survival asymptotic")
    print(f"lambda_1=R={fmt(radius, 20)}")
    print()
    print("Interior")
    print("n   actual rho          product estimate    actual/estimate")
    for n in range(1, max_n + 1):
        actual = actual_rho(mu, n)
        estimate = interior_estimate(lam, n)
        print(f"{n:2d}  {fmt(actual, 14):>18} {fmt(estimate, 14):>18} {fmt(actual/estimate, 12):>16}")
    print()
    print("Boundary-complement")
    print("n   actual rho          product estimate    actual/estimate")
    for n in range(1, max_n + 1):
        actual = actual_rho(boundary_mu, n)
        estimate = boundary_estimate(lam, n)
        print(f"{n:2d}  {fmt(actual, 14):>18} {fmt(estimate, 14):>18} {fmt(actual/estimate, 12):>16}")
    print()
    print("Interpretation")
    print("- The product estimate assumes exact root locking to the dominant atoms.")
    print("- The ratio should approach 1 if the next uncancelled atom dominates the residual.")


if __name__ == "__main__":
    main()
