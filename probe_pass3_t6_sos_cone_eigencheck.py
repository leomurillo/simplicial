"""Finite sum-of-squares cone check for the Pass-3 completed ledger.

Interior Hankel positivity is equivalent to

    L(f^2) > 0

for nonzero polynomials f in the finite degree window.

Boundary-complement positivity is equivalent to

    L((R-t) f^2) > 0.

Together these are the finite Hausdorff/Stieltjes support gates for [0,R].
This probe prints eigenvalue ranges and condition numbers of the two Gram
matrices. Numerical evidence only.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta


mp.mp.dps = 100


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def hankel(moments: list[mp.mpf], n: int) -> mp.matrix:
    return mp.matrix([[moments[a + b] for b in range(n + 1)] for a in range(n + 1)])


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def eig_range(mat: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    vals = [mp.re(v) for v in mp.eigsy(mat, eigvals_only=True)]
    return min(vals), max(vals)


def main() -> None:
    max_n = 10
    order = 2 * max_n + 8
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    bmu = boundary(mu, radius)

    print("Pass-3 T6 SOS cone eigencheck")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print("n   min eig H_n        max eig H_n        cond H_n          min eig K_n        max eig K_n        cond K_n")
    for n in range(0, max_n + 1):
        h = hankel(mu, n)
        k = hankel(bmu, n)
        hmin, hmax = eig_range(h)
        kmin, kmax = eig_range(k)
        print(
            f"{n:2d}  {fmt(hmin, 10):>14} {fmt(hmax, 10):>14} {fmt(hmax/hmin, 10):>14} "
            f"{fmt(kmin, 10):>14} {fmt(kmax, 10):>14} {fmt(kmax/kmin, 10):>14}"
        )
    print()
    print("Interpretation")
    print("- H_n is the Gram matrix of L(f^2).")
    print("- K_n is the Gram matrix of L((R-t)f^2).")
    print("- Positivity of both cones is the finite [0,R] support gate.")


if __name__ == "__main__":
    main()
