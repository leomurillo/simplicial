"""KU-3 Family D: Stella-octangula / Janus doubled Hamiltonians."""

from __future__ import annotations

import numpy as np

from hpo_common import (
    K_PERM,
    apply_k,
    cyclic_momentum,
    g_balanced,
    hermitian_part,
    k_antisymmetric_diag,
    print_matrix,
    print_spectral_report,
    sym,
)


SIGMA_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SIGMA_Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
SIGMA_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def k_shift_observable(g: np.ndarray) -> np.ndarray:
    return hermitian_part(sym(K_PERM, g))


def janus_time_reversal_defect(matrix: np.ndarray) -> float:
    k_janus = np.kron(K_PERM, SIGMA_X)
    transformed = k_janus @ np.conjugate(matrix) @ k_janus.T.conj()
    return float(np.linalg.norm(transformed - matrix.conj().T))


def stella_octangula_candidate(alpha: float = 1.0, beta: float = 1.0, mu: float = 1.0) -> np.ndarray:
    """Hermitian C6 x C2 candidate with Janus polarity.

    H = alpha * H_B * sigma_z + beta * A_K * sigma_x + mu * P6 * sigma_y.
    The antiunitary Janus polarity is K_J = (P_K tensor sigma_x) conjugation.
    """
    p = cyclic_momentum()
    g = g_balanced()
    h_b = hermitian_part(1j * (g @ p - p @ g))
    a_k = k_shift_observable(k_antisymmetric_diag()) + k_shift_observable(g)
    h = (
        alpha * np.kron(h_b, SIGMA_Z)
        + beta * np.kron(a_k, SIGMA_X)
        + mu * np.kron(p, SIGMA_Y)
    )
    return hermitian_part(h)


def block_control_candidate() -> np.ndarray:
    """Control: doubled direct sum H_B and -H_B without Janus mixing."""
    p = cyclic_momentum()
    g = g_balanced()
    h_b = hermitian_part(1j * (g @ p - p @ g))
    return hermitian_part(np.kron(h_b, SIGMA_Z))


if __name__ == "__main__":
    h = stella_octangula_candidate(alpha=1.0, beta=1.0, mu=1.0)
    print_matrix("H_D = H_B tensor sigma_z + A_K tensor sigma_x + P6 tensor sigma_y", h, precision=3)
    print(f"Janus K-Hermitian defect ||K_J H K_J^-1 - H^*||: {janus_time_reversal_defect(h):.6e}")
    print_spectral_report("Family D.1 Stella-octangula Janus candidate", h)

    h_control = block_control_candidate()
    print_matrix("H_D_control = H_B tensor sigma_z", h_control, precision=3)
    print(f"Janus K-Hermitian defect ||K_J H K_J^-1 - H^*||: {janus_time_reversal_defect(h_control):.6e}")
    print_spectral_report("Family D.2 doubled block control", h_control)
