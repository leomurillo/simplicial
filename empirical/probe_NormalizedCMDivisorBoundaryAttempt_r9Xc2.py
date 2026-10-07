"""Probe the normalized CM divisor boundary-support attempt.

Random suffix: r9Xc2

This script demonstrates two facts:
1. The normalized CM divisor is exactly the Xi divisor, so boundary support is
   equivalent to RH.
2. The already-proved algebraic/K package does not force boundary support:
   a real-even K-symmetric fake denominator with an off-boundary quartet gives
   the same normalized-divisor structure but violates Pick positivity.
"""

from __future__ import annotations

import cmath

import numpy as np


def fake_X(z: complex, gamma: float = 3.0, delta: float = 0.7) -> complex:
    return ((z - gamma) ** 2 + delta**2) * ((z + gamma) ** 2 + delta**2)


def fake_X_prime(z: complex, gamma: float = 3.0, delta: float = 0.7) -> complex:
    f1 = (z - gamma) ** 2 + delta**2
    f2 = (z + gamma) ** 2 + delta**2
    return 2 * (z - gamma) * f2 + 2 * (z + gamma) * f1


def m_fake(z: complex, gamma: float = 3.0, delta: float = 0.7) -> complex:
    return -fake_X_prime(z, gamma, delta) / fake_X(z, gamma, delta)


def pick_diag(z: complex) -> float:
    return m_fake(z).imag / z.imag


def pick_kernel(points: list[complex]) -> np.ndarray:
    n = len(points)
    K = np.empty((n, n), dtype=complex)
    for i, z in enumerate(points):
        for j, w in enumerate(points):
            K[i, j] = (m_fake(z) - np.conj(m_fake(w))) / (z - np.conj(w))
    return K


def normalized_cm_transfer(fake_A, z: complex) -> complex:
    """Toy normalized CM transfer C/A with C = X*A."""
    fake_C = fake_X(z) * fake_A(z)
    return fake_C / fake_A(z)


def main() -> None:
    gamma = 3.0
    delta = 0.7
    zeros = [
        gamma + 1j * delta,
        gamma - 1j * delta,
        -gamma + 1j * delta,
        -gamma - 1j * delta,
    ]

    print("fake zeros:")
    for z0 in zeros:
        print(" ", z0, "X(z0)=", abs(fake_X(z0)))

    print("\nK symmetry checks for X#=X and evenness:")
    samples = [0.4 + 0.2j, 2.0 + 0.3j, -1.5 + 0.9j]
    for z in samples:
        sharp_err = abs(np.conj(fake_X(np.conj(z))) - fake_X(z))
        even_err = abs(fake_X(-z) - fake_X(z))
        print("z=", z, "sharp_err=", f"{sharp_err:.3e}", "even_err=", f"{even_err:.3e}")

    print("\nToy normalized CM transfer C/A = X:")
    fake_A = lambda z: 1 + 0.2 * z + 0.05 * z * z
    for z in samples:
        transfer = normalized_cm_transfer(fake_A, z)
        print("z=", z, "|C/A-X|=", f"{abs(transfer - fake_X(z)):.3e}")

    print("\nPick diagonal around the upper off-boundary zero:")
    for eps in [0.2, 0.1, 0.05, 0.02]:
        above = gamma + 1j * (delta + eps)
        below = gamma + 1j * (delta - eps)
        print(
            "eps=", eps,
            "Pdiag_above=", f"{pick_diag(above):+.6e}",
            "Pdiag_below=", f"{pick_diag(below):+.6e}",
        )

    points = [
        gamma + 1j * (delta - 0.1),
        gamma + 0.4 + 1j * (delta + 0.2),
        -gamma + 1j * (delta + 0.15),
    ]
    K = pick_kernel(points)
    eigs = np.linalg.eigvalsh((K + K.conj().T) / 2)
    print("\nPick matrix Hermitian eigenvalues:")
    print(np.array2string(eigs, precision=8))
    print("min_eigenvalue:", f"{eigs[0]:+.6e}")

    print("\nConclusion:")
    print("  K-symmetric off-boundary divisor satisfies the same normalized")
    print("  transfer shape C/A=X, but Pick positivity fails. Therefore")
    print("  boundary support needs an additional positivity law.")


if __name__ == "__main__":
    main()

