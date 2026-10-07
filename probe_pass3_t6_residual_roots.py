"""Residual polynomial roots against folded-zero atom locations.

If the Pass-3 moment ledger has the trace-gauge spectral form

    mu_k = sum_j lambda_j^{k+1},  lambda_j = gamma_j^{-2},

then the monic Schur residual P_n should cancel the dominant spectral atoms.
This probe compares roots of P_n and of the boundary-complement residual Q_n
with the largest folded zero locations lambda_j.

Numerical evidence only.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 100


def fmt(x: mp.mpf | mp.mpc, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def boundary(moments: list[mp.mpf], radius: mp.mpf) -> list[mp.mpf]:
    return [radius * moments[k] - moments[k + 1] for k in range(len(moments) - 1)]


def monic_residual(moments: list[mp.mpf], n: int) -> list[mp.mpf]:
    if n == 0:
        return [mp.mpf(1)]
    _, coeffs = pivots.schur_pivot(moments, n)
    return coeffs + [mp.mpf(1)]


def roots_low_to_high(poly: list[mp.mpf]) -> list[mp.mpc]:
    # mp.polyroots expects coefficients from highest degree to constant.
    coeffs = list(reversed(poly))
    roots = mp.polyroots(coeffs, maxsteps=200, error=False)
    return sorted(roots, key=lambda z: mp.re(z), reverse=True)


def atom_locations(n: int, start: int = 1) -> list[mp.mpf]:
    out = []
    for k in range(start, start + n):
        gamma = mp.im(mp.zetazero(k))
        out.append(1 / (gamma * gamma))
    return out


def print_roots(label: str, moments: list[mp.mpf], max_n: int, atom_start: int = 1) -> None:
    print(label)
    for n in range(1, max_n + 1):
        poly = monic_residual(moments, n)
        roots = roots_low_to_high(poly)
        atoms = atom_locations(n, atom_start)
        print(f"n={n}")
        print("j   root                         gamma_j^-2                  rel.err")
        for j, root in enumerate(roots, start=1):
            atom = atoms[j - 1]
            rel = abs(mp.re(root) - atom) / atom
            imag = abs(mp.im(root))
            imag_note = "" if imag < mp.mpf("1e-40") else f" imag={fmt(imag, 5)}"
            print(f"{j:1d}  {fmt(root, 22):>28} {fmt(atom, 22):>28} {fmt(rel, 8):>12}{imag_note}")
        print()


def main() -> None:
    max_n = 8
    order = 2 * max_n + 8
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    boundary_mu = boundary(mu, radius)

    print("Pass-3 T6 residual roots")
    print(f"support R=gamma_1^-2={fmt(radius, 22)}")
    print()
    print_roots("Interior residual roots P_n", mu, max_n, atom_start=1)
    print_roots("Boundary-complement residual roots Q_n", boundary_mu, max_n, atom_start=2)


if __name__ == "__main__":
    main()
