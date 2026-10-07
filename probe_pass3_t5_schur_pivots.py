"""Schur-pivot form of the T5 harmonic gate ledger.

For a Hankel moment matrix, the adjacent determinant ratio

    D_n / D_{n-1}

is the Schur-complement pivot obtained after projecting t^n against the
lower monomials 1,t,...,t^{n-1}. This is the recursive, gate-local version
of determinant positivity.

The same pivot identity applies to the upper-radius gates after replacing
the moment functional L by L_R(f)=L((R-t)f(t)).
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 16) -> str:
    return mp.nstr(x, digits)


def schur_pivot(mu: list[mp.mpf], n: int) -> tuple[mp.mpf, list[mp.mpf]]:
    if n == 0:
        return mu[0], []

    block = mp.matrix([[mu[a + b] for b in range(n)] for a in range(n)])
    v = mp.matrix([mu[n + a] for a in range(n)])
    coeffs = mp.lu_solve(block, -v)
    pivot = mu[2 * n] + mp.fdot([coeffs[a] for a in range(n)], [mu[n + a] for a in range(n)])
    return mp.re(pivot), [mp.re(coeffs[a]) for a in range(n)]


def det_ratio(mu: list[mp.mpf], n: int) -> mp.mpf:
    det_n = gates.det_matrix(gates.hankel_matrix(mu, n))
    if n == 0:
        return det_n
    return det_n / gates.det_matrix(gates.hankel_matrix(mu, n - 1))


def main() -> None:
    max_n = 4
    order = 2 * max_n + 4
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    boundary_mu = [radius * mu[i] - mu[i + 1] for i in range(order - 1)]

    print("Pass-3 T5 Schur pivots")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()

    print("Interior pivots")
    print("n   Schur pivot h_n        D_n/D_{n-1}         abs diff")
    for n in range(max_n + 1):
        pivot, _ = schur_pivot(mu, n)
        ratio = det_ratio(mu, n)
        print(f"{n:1d}  {fmt(pivot, 18):>22} {fmt(ratio, 18):>22} {fmt(abs(pivot-ratio), 5):>12}")

    print()
    print("Boundary-complement pivots")
    print("n   Schur pivot k_n        G_n/G_{n-1}         abs diff")
    for n in range(max_n + 1):
        pivot, _ = schur_pivot(boundary_mu, n)
        ratio = det_ratio(boundary_mu, n)
        print(f"{n:1d}  {fmt(pivot, 18):>22} {fmt(ratio, 18):>22} {fmt(abs(pivot-ratio), 5):>12}")

    print()
    print("First nontrivial monic residuals")
    for label, moments in (("interior", mu), ("boundary", boundary_mu)):
        print(label)
        for n in range(1, 4):
            pivot, coeffs = schur_pivot(moments, n)
            coeff_text = ", ".join(fmt(c, 10) for c in coeffs)
            print(f"  P_{n}(t)=t^{n}+({coeff_text}); norm^2={fmt(pivot, 14)}")

    print()
    print("Interpretation")
    print("- Each gate ratio is a local residual after lower-rung rebalancing.")
    print("- The proof target can be phrased as positivity of recursive Schur pivots.")


if __name__ == "__main__":
    main()
