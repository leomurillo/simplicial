"""Probe for Note_ArchimedeanMetaplecticSelectionResolution_Q8vM3.

This is not a zeta-zero computation.  It checks the representation-theoretic
logic behind the Archimedean no-go:

1. the gamma branch reflection is unitary on an even atomic height measure;
2. the same reflection acts by Bures-isometric unitary conjugation on density
   matrices;
3. an atomic height operator cannot be the position branch of a regular Weyl
   system, because Weyl covariance would translate its spectral support.
"""

from __future__ import annotations

import cmath
import math

import mpmath as mp
import numpy as np


mp.mp.dps = 40


def gamma_R(s: complex) -> complex:
    z = mp.mpc(s)
    return complex(mp.power(mp.pi, -z / 2) * mp.gamma(z / 2))


def gamma_phase(t: float) -> complex:
    return gamma_R(0.5 + 1j * t) / gamma_R(0.5 - 1j * t)


def matrix_sqrt_psd(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2)
    vals = np.maximum(vals, 0.0)
    return (vecs * np.sqrt(vals)) @ vecs.conj().T


def fidelity(rho: np.ndarray, sigma: np.ndarray) -> float:
    root = matrix_sqrt_psd(rho)
    middle = root @ sigma @ root
    return float(np.real(np.trace(matrix_sqrt_psd(middle))) ** 2)


def random_density(rng: np.random.Generator, dim: int) -> np.ndarray:
    a = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def atomic_packet() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    atoms = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], dtype=float)
    masses = np.exp(-np.abs(atoms))
    masses = masses / masses.sum()

    dim = len(atoms)
    index = {float(t): i for i, t in enumerate(atoms)}
    u = np.zeros((dim, dim), dtype=complex)
    for i, t in enumerate(atoms):
        j = index[float(-t)]
        u[i, j] = gamma_phase(float(t))
    return atoms, masses, u


def reflection_unitarity_check(atoms: np.ndarray, masses: np.ndarray, u: np.ndarray) -> None:
    f = np.array(
        [cmath.exp(0.2j * t) * (1.0 + 0.1 * t + 0.03j * t * t) for t in atoms],
        dtype=complex,
    )
    before = float(np.sum(masses * np.abs(f) ** 2))
    after = float(np.sum(masses * np.abs(u @ f) ** 2))
    involution_error = float(np.linalg.norm(u @ u - np.eye(len(atoms))))
    print("Gamma reflection on even atomic measure")
    print(f"weighted norm before : {before:.12e}")
    print(f"weighted norm after  : {after:.12e}")
    print(f"norm difference      : {abs(before - after):.3e}")
    print(f"U^2-I Frobenius norm : {involution_error:.3e}")


def bures_isometry_check(u: np.ndarray) -> None:
    rng = np.random.default_rng(20260522)
    rho = random_density(rng, len(u))
    sigma = random_density(rng, len(u))
    before = fidelity(rho, sigma)
    rho_u = u @ rho @ u.conj().T
    sigma_u = u @ sigma @ u.conj().T
    after = fidelity(rho_u, sigma_u)
    print("\nBures/Petz unitary-conjugation check")
    print(f"fidelity before      : {before:.12e}")
    print(f"fidelity after       : {after:.12e}")
    print(f"fidelity difference  : {abs(before - after):.3e}")


def weyl_covariance_obstruction(atoms: np.ndarray) -> None:
    support = set(float(t) for t in atoms)
    shifted = set(float(t + 0.5) for t in atoms)
    rank_support = len(support)
    rank_shifted_inside_packet = len(support.intersection(shifted))

    print("\nWeyl covariance obstruction")
    print(f"rank E_T(Z-support)          : {rank_support}")
    print(f"rank E_T(Z-support + 1/2)    : {rank_shifted_inside_packet}")
    print(
        "unitary covariance would preserve rank, so the atomic height branch "
        "cannot satisfy V(v) T V(v)^* = T + vI."
    )


def finite_trace_ccr_obstruction(dim: int) -> None:
    hbar = 1.0
    trace_commutator = 0.0
    trace_identity_side = 1j * hbar * dim
    print("\nFinite-row CCR trace obstruction")
    print(f"Tr([Q,P]) for finite matrices : {trace_commutator}")
    print(f"Tr(i*hbar*I) if CCR held      : {trace_identity_side}")


def oscillator_mellin_check() -> None:
    print("\nConditional oscillator Mellin check")
    for s in [0.5 + 2.0j, 1.3 + 0.4j]:
        z = mp.mpc(s)
        even_integral = 2 * mp.quad(
            lambda x: mp.e ** (-mp.pi * x * x) * x ** (z - 1), [0, mp.inf]
        )
        odd_integral = 2 * mp.quad(
            lambda x: mp.e ** (-mp.pi * x * x) * x ** z, [0, mp.inf]
        )
        even_gamma = mp.power(mp.pi, -z / 2) * mp.gamma(z / 2)
        odd_gamma = mp.power(mp.pi, -(z + 1) / 2) * mp.gamma((z + 1) / 2)
        print(
            f"s={s}: even error={float(abs(even_integral - even_gamma)):.3e}, "
            f"odd error={float(abs(odd_integral - odd_gamma)):.3e}"
        )


def main() -> None:
    atoms, masses, u = atomic_packet()
    reflection_unitarity_check(atoms, masses, u)
    bures_isometry_check(u)
    weyl_covariance_obstruction(atoms)
    finite_trace_ccr_obstruction(len(atoms))
    oscillator_mellin_check()


if __name__ == "__main__":
    main()

