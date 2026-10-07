"""Infinite CM divisor Hilbert-space truncation probe.

Random suffix: Q2wL9

Builds finite divisor measures from the first N zeta zeros on the critical
line and compares their positive Gram kernels with the exact Pick kernel of
m_B=-Xi'/Xi at several sample points.
"""

from __future__ import annotations

import time

import mpmath as mp
import numpy as np


mp.mp.dps = 70


def xi_s(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(z):
    return xi_s(mp.mpf("0.5") + 1j * z)


def Xi_prime(z):
    return 1j * mp.diff(xi_s, mp.mpf("0.5") + 1j * z)


def m_bures(z):
    return -Xi_prime(z) / Xi(z)


def pick_bures(z, w):
    return (m_bures(z) - mp.conj(m_bures(w))) / (z - mp.conj(w))


def first_gammas(n):
    return [mp.im(mp.zetazero(k)) for k in range(1, n + 1)]


def pick_truncated(z, w, gammas):
    total = mp.mpc(0)
    wc = mp.conj(w)
    for gamma in gammas:
        total += 1 / ((gamma - z) * (gamma - wc))
        total += 1 / ((-gamma - z) * (-gamma - wc))
    return total


def matrix_from_kernel(points, kernel):
    matrix = np.empty((len(points), len(points)), dtype=complex)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            matrix[i, j] = complex(kernel(z, w))
    return (matrix + matrix.conj().T) / 2


def rank_from_singular(values, relative=1e-10):
    values = np.asarray(values, dtype=float)
    if values.size == 0 or values[0] == 0:
        return 0
    return int(np.sum(values > relative * values[0]))


def main() -> None:
    gamma1 = mp.im(mp.zetazero(1))
    gamma2 = mp.im(mp.zetazero(2))
    points = [
        mp.mpc("0.7", "0.4"),
        mp.mpc("5.0", "0.5"),
        gamma1 + mp.mpc(0, "0.5"),
        gamma2 + mp.mpc(0, "0.5"),
    ]

    print("sample points:")
    for z in points:
        print(" ", mp.nstr(z, 18))

    exact_diag = [pick_bures(z, z) for z in points]
    print("\nExact P_B diagonal:")
    for z, value in zip(points, exact_diag):
        print(" ", mp.nstr(z, 14), mp.nstr(value, 12))

    for n in [5, 10, 20, 50]:
        start = time.time()
        gammas = first_gammas(n)
        rel_errors = []
        trunc_diag = []
        for z, exact in zip(points, exact_diag):
            approx = pick_truncated(z, z, gammas)
            trunc_diag.append(approx)
            rel_errors.append(abs(approx - exact) / abs(exact))

        matrix = matrix_from_kernel(points, lambda z, w, g=gammas: pick_truncated(z, w, g))
        eigs = np.linalg.eigvalsh(matrix)
        singular = np.linalg.svd(matrix, compute_uv=False)
        print(f"\nN={n} truncation, seconds={time.time() - start:.2f}")
        print("  diag:", [mp.nstr(v, 8) for v in trunc_diag])
        print("  rel_errors:", [mp.nstr(e, 5) for e in rel_errors])
        print("  min_eig:", f"{eigs[0]:+.8e}", "rank:", rank_from_singular(singular))

    zero_points = [mp.im(mp.zetazero(k)) + mp.mpc(0, "0.5") for k in range(1, 11)]
    exact_matrix = matrix_from_kernel(zero_points, pick_bures)
    exact_eigs = np.linalg.eigvalsh(exact_matrix)
    exact_singular = np.linalg.svd(exact_matrix, compute_uv=False)
    print("\nExact P_B on ten near-zero points:")
    print("  eigenvalues:", np.array2string(exact_eigs, precision=8))
    print("  rank:", rank_from_singular(exact_singular))

    gammas10 = first_gammas(10)
    trunc_matrix = matrix_from_kernel(zero_points, lambda z, w: pick_truncated(z, w, gammas10))
    trunc_eigs = np.linalg.eigvalsh(trunc_matrix)
    trunc_singular = np.linalg.svd(trunc_matrix, compute_uv=False)
    print("\nTruncated divisor Gram on same ten points, N=10:")
    print("  eigenvalues:", np.array2string(trunc_eigs, precision=8))
    print("  rank:", rank_from_singular(trunc_singular))
    print("  positive:", bool(np.all(trunc_eigs > -1e-10)))

    print("\nInterpretation:")
    print("  Each truncation is a positive L^2(divisor) Gram kernel.")
    print("  Increasing N grows the Hilbert dimension and approximates P_B.")
    print("  A proof still requires constructing the full positive boundary")
    print("  measure from CM/Bures geometry without assuming RH.")


if __name__ == "__main__":
    main()

