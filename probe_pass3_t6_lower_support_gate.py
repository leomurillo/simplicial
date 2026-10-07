"""Lower-support SOS gate for the Pass-3 completed ledger.

For a Hausdorff moment measure on [0,R], one needs the three finite forms:

    L(f^2) >= 0,
    L(t f^2) >= 0,
    L((R-t) f^2) >= 0.

The current Pass-3 work emphasized the interior Hankel cone and the upper
localizer. This probe checks the lower localizer

    J_n = (mu_{a+b+1})_{0<=a,b<=n}

and compares it with the interior and upper cones.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta


mp.mp.dps = 100


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def hankel(moments: list[mp.mpf], n: int, shift: int = 0) -> mp.matrix:
    return mp.matrix([[moments[a + b + shift] for b in range(n + 1)] for a in range(n + 1)])


def upper_moments(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def eig_range(mat: mp.matrix) -> tuple[mp.mpf, mp.mpf]:
    vals = [mp.re(v) for v in mp.eigsy(mat, eigvals_only=True)]
    return min(vals), max(vals)


def main() -> None:
    max_n = 9
    order = 2 * max_n + 10
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    upper = upper_moments(mu, radius)

    print("Pass-3 T6 lower-support gate")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print("n   min H=L(f^2)     min J=L(t f^2)   min K=L((R-t)f^2)")
    for n in range(max_n + 1):
        hmin, _ = eig_range(hankel(mu, n, 0))
        jmin, _ = eig_range(hankel(mu, n, 1))
        kmin, _ = eig_range(hankel(upper, n, 0))
        print(f"{n:2d}  {fmt(hmin, 12):>16} {fmt(jmin, 12):>18} {fmt(kmin, 12):>22}")
    print()
    print("Interpretation")
    print("- H is the interior square cone.")
    print("- J is the lower-support cone at t=0.")
    print("- K is the upper-support cone at R.")
    print("- A full [0,R] certificate must preserve all three.")


if __name__ == "__main__":
    main()
