"""KU-3 Family B: K-Hermitian / PT-style Bures-amplitude Hamiltonians."""

from __future__ import annotations

import numpy as np

from hpo_common import (
    apply_k,
    g_balanced,
    hermitian_part,
    k_antisymmetric_diag,
    print_matrix,
    print_projection_residuals,
    print_spectral_report,
    projected_critical_line_ops,
)


def finite_commutator_candidate(lambda_even: float = 1.0) -> np.ndarray:
    """Pure C6 K-Hermitian commutator candidate.

    H = i [G, P6] + lambda * (G + G^K)/2.
    This is the finite matrix analogue of i(B_G d - d B_G), with the cyclic
    momentum standing in for the derivative.
    """
    from hpo_common import cyclic_momentum

    g = g_balanced()
    p = cyclic_momentum()
    even = 0.5 * (g + apply_k(g))
    return hermitian_part(1j * (g @ p - p @ g) + lambda_even * even)


def hurwitz_bures_commutator(lambda_even: float = 1.0) -> np.ndarray:
    """Projected i(B_G d_s - d_s B_G) plus K-even correction."""
    ops = projected_critical_line_ops()
    print_projection_residuals(ops)
    d_s = -1j * ops.d_dt
    raw = 1j * (ops.b_mult @ d_s - d_s @ ops.b_mult)
    even = 0.5 * (g_balanced() + apply_k(g_balanced()))
    return hermitian_part(raw) + lambda_even * hermitian_part(even)


def k_odd_diagonal_control() -> np.ndarray:
    """Control using the diagonal K-odd observable from the Hurwitz FE probe."""
    from hpo_common import cyclic_momentum

    a = k_antisymmetric_diag()
    p = cyclic_momentum()
    return hermitian_part(1j * (a @ p - p @ a))


if __name__ == "__main__":
    h_finite = finite_commutator_candidate(lambda_even=1.0)
    print_matrix("H_B_finite = i[G_bal,P6] + (G_bal+G_bal^K)/2", h_finite)
    print_spectral_report("Family B.1 finite K-Hermitian commutator", h_finite)

    h_hurwitz = hurwitz_bures_commutator(lambda_even=1.0)
    print_matrix("H_B_hurwitz = Herm(i(B_G d_s - d_s B_G)) + K-even correction", h_hurwitz)
    print_spectral_report("Family B.2 Hurwitz Bures-amplitude commutator", h_hurwitz)

    h_control = k_odd_diagonal_control()
    print_matrix("H_B_control = i[A_Kodd,P6]", h_control)
    print_spectral_report("Family B.3 K-odd diagonal control", h_control)
