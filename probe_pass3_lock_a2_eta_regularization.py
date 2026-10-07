"""Probe Lock A2 with a finite centered eta regularization.

This is a control experiment, not the final primorial construction.
It replaces zeta near s=1/2 by a finite Euler-transformed eta model

    zeta_K(s) = eta_K(s) / (1 - 2^(1-s))

and computes the centered folded zeta cumulants

    1/2[log zeta_K(1/2+y) + log zeta_K(1/2-y) - 2 log zeta_K(1/2)].

The purpose is to test Lock A2's shape: finite regularization must be
centered before taking the limit. Raw pieces are not determinant-scale;
the folded centered coefficients converge to the zeta residual ledger.
"""

from __future__ import annotations

from math import factorial

import mpmath as mp


mp.mp.dps = 80


def eta_euler(s: mp.mpc, kmax: int) -> mp.mpc:
    """Euler transform partial sum for Dirichlet eta."""
    total = mp.mpc(0)
    row = [mp.mpc(1)]  # binomial row for k=0
    for k in range(kmax + 1):
        inner = mp.fsum(((-1) ** j) * row[j] * mp.power(j + 1, -s) for j in range(k + 1))
        total += inner / (mp.mpf(2) ** (k + 1))
        # Next Pascal row.
        row = [mp.mpc(1)] + [row[j - 1] + row[j] for j in range(1, len(row))] + [mp.mpc(1)]
    return total


def zeta_eta_model(s: mp.mpc, kmax: int) -> mp.mpc:
    return eta_euler(s, kmax) / (1 - mp.power(2, 1 - s))


def folded_zeta_log_coeffs(kmax: int | None, order: int) -> list[mp.mpf]:
    """Return zeta-residual cumulants ell_m for m=1..order."""

    def zfun(s: mp.mpc) -> mp.mpc:
        if kmax is None:
            return mp.zeta(s)
        return zeta_eta_model(s, kmax)

    z0 = zfun(mp.mpf("0.5"))

    def folded(y: mp.mpc) -> mp.mpc:
        return mp.mpf("0.5") * (
            mp.log(zfun(mp.mpf("0.5") + y) / z0)
            + mp.log(zfun(mp.mpf("0.5") - y) / z0)
        )

    ells = []
    for m in range(1, order + 1):
        coeff = mp.diff(folded, mp.mpf("0"), 2 * m) / factorial(2 * m)
        ell = ((-1) ** (m + 1)) * m * coeff
        ells.append(mp.re(ell))
    return ells


def fmt(x: mp.mpf, digits: int = 14) -> str:
    return mp.nstr(x, digits)


def main() -> None:
    order = 5
    true_ells = folded_zeta_log_coeffs(None, order)
    print("Centered zeta-residual cumulants via finite eta regularization")
    print("K     max relative error     ell_1                 ell_2                 ell_3")
    for kmax in (4, 8, 12, 20, 32, 48):
        ells = folded_zeta_log_coeffs(kmax, order)
        rels = [
            abs(ells[i] - true_ells[i]) / max(mp.mpf("1e-60"), abs(true_ells[i]))
            for i in range(order)
        ]
        print(
            f"{kmax:2d}    {fmt(max(rels), 8):>14}    "
            f"{fmt(ells[0], 18):>20} {fmt(ells[1], 18):>20} {fmt(ells[2], 18):>20}"
        )

    print("\ntrue  " + " ".join(fmt(v, 18) for v in true_ells[:3]))


if __name__ == "__main__":
    main()
