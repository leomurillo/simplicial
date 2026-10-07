"""Probe gamma multiplier uniqueness versus measure freedom.

Random suffix: M7aQ2

For several even positive height measures, this script checks that the same
Riemann-Siegel gamma multiplier defines a unitary height-reflection involution.
It then shows the resulting resolvent Gram kernels differ, demonstrating that
gamma phase selection alone does not select the divisor measure.
"""

from __future__ import annotations

import cmath

import mpmath as mp
import numpy as np


mp.mp.dps = 50


def theta(t: float) -> float:
    tc = mp.mpf(t)
    return float(mp.im(mp.log(mp.gamma(mp.mpf("0.25") + 0.5j * tc))) - 0.5 * tc * mp.log(mp.pi))


def gamma_multiplier(t: float) -> complex:
    return cmath.exp(2j * theta(t))


def involution_matrix(grid: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Matrix of iota f(t)=gamma(t) f(-t) on a symmetric grid."""
    n = len(grid)
    lookup = {round(float(t), 12): i for i, t in enumerate(grid)}
    matrix = np.zeros((n, n), dtype=complex)
    for i, t in enumerate(grid):
        j = lookup[round(float(-t), 12)]
        matrix[i, j] = gamma_multiplier(float(t))
    return matrix


def weighted_unitarity_error(U: np.ndarray, weights: np.ndarray) -> float:
    W = np.diag(weights)
    return float(np.linalg.norm(U.conj().T @ W @ U - W))


def resolvent_gram(points: list[complex], atoms: np.ndarray, weights: np.ndarray) -> np.ndarray:
    K = np.empty((len(points), len(points)), dtype=complex)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            total = 0j
            for atom, weight in zip(atoms, weights):
                total += weight / ((atom - z) * (atom - np.conj(w)))
            K[i, j] = total
    return (K + K.conj().T) / 2


def symmetric_measure(kind: str, n: int = 21) -> tuple[np.ndarray, np.ndarray]:
    half = np.linspace(0.5, 20.5, n // 2)
    atoms = np.concatenate([-half[::-1], half])
    if kind == "gaussian":
        weights = np.exp(-0.03 * atoms**2)
    elif kind == "cauchy":
        weights = 1 / (1 + atoms**2)
    elif kind == "flat_atoms":
        weights = np.ones_like(atoms)
    elif kind == "fake_divisor":
        base = np.array([14.13472514, 21.02203964, 25.01085758, 30.42487613, 32.93506159])
        atoms = np.concatenate([-base[::-1], base])
        weights = np.ones_like(atoms)
    else:
        raise ValueError(kind)
    return atoms.astype(float), weights.astype(float)


def main() -> None:
    print("Gamma multiplier modulus and phase samples:")
    for t in [0.5, 3.0, 14.13472514, 21.02203964, 50.0]:
        g = gamma_multiplier(t)
        print("t=", t, "|gamma|=", f"{abs(g):.12f}", "arg=", f"{cmath.phase(g):+.6f}")

    print("\nUnitary involution check for multiple even measures:")
    for kind in ["gaussian", "cauchy", "flat_atoms", "fake_divisor"]:
        atoms, weights = symmetric_measure(kind)
        U = involution_matrix(atoms, weights)
        err = weighted_unitarity_error(U, weights)
        invol_err = np.linalg.norm(U @ U - np.eye(len(atoms)))
        print(kind, "unitarity_err=", f"{err:.3e}", "involution_err=", f"{invol_err:.3e}")

    points = [0.7 + 0.4j, 5.0 + 0.5j, 14.13472514 + 0.5j]
    print("\nResolvent Gram diagonals for different even measures:")
    for kind in ["gaussian", "cauchy", "flat_atoms", "fake_divisor"]:
        atoms, weights = symmetric_measure(kind)
        K = resolvent_gram(points, atoms, weights)
        eigs = np.linalg.eigvalsh(K)
        print(kind, "diag=", np.array2string(np.real(np.diag(K)), precision=6), "min_eig=", f"{eigs[0]:+.6e}")

    print("\nConclusion:")
    print("  The same gamma multiplier is unitary for every even positive measure.")
    print("  The resulting Gram kernels are positive but different.")
    print("  Therefore the Archimedean phase law does not select the Hilbert-Polya")
    print("  divisor measure. The missing RH theorem is measure selection.")


if __name__ == "__main__":
    main()

