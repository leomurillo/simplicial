"""KU-3 Family C: cumulant-tower generator candidates."""

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
    print_projection_residuals,
    print_spectral_report,
    projected_critical_line_ops,
    sym,
)


def k_shift_observable(g: np.ndarray) -> np.ndarray:
    """Hermitian linear shadow of the antiunitary K-mark: (P_K G + G P_K)/2."""
    return hermitian_part(sym(K_PERM, g))


def finite_cumulant_generator(alpha: float = 1.0, beta: float = 1.0) -> np.ndarray:
    """K-shift plus dilation candidate on C6.

    H = alpha * {P6, A_KG}/2 + beta * {P6, A_Kodd}/2,
    where A_KG is the linear K-marked observable.
    """
    p = cyclic_momentum()
    a_g = k_shift_observable(g_balanced())
    a_odd = k_shift_observable(k_antisymmetric_diag())
    return hermitian_part(alpha * sym(p, a_g) + beta * sym(p, a_odd))


def hurwitz_cumulant_generator(alpha: float = 1.0, beta: float = 1.0) -> np.ndarray:
    """Same K-shift generator using the projected Hurwitz dilation P_t."""
    ops = projected_critical_line_ops()
    print_projection_residuals(ops)
    a_g = k_shift_observable(g_balanced())
    a_odd = k_shift_observable(k_antisymmetric_diag())
    return hermitian_part(alpha * sym(ops.p_t, a_g) + beta * sym(ops.p_t, a_odd))


def k_even_rate_shadow() -> np.ndarray:
    """Multiplicative rate-shadow control from G^K G symmetrized."""
    g = g_balanced()
    return hermitian_part(0.5 * (apply_k(g) @ g + g @ apply_k(g)))


if __name__ == "__main__":
    h_finite = finite_cumulant_generator(alpha=1.0, beta=1.0)
    print_matrix("H_C_finite = {P6,A_KG}/2 + {P6,A_Kodd}/2", h_finite)
    print_spectral_report("Family C.1 finite cumulant generator", h_finite)

    h_hurwitz = hurwitz_cumulant_generator(alpha=1.0, beta=1.0)
    print_matrix("H_C_hurwitz = projected {P_t,A_KG}/2 + {P_t,A_Kodd}/2", h_hurwitz)
    print_spectral_report("Family C.2 Hurwitz cumulant generator", h_hurwitz)

    h_rate = k_even_rate_shadow()
    print_matrix("H_C_rate_shadow = Herm((G^K G + G G^K)/2)", h_rate)
    print_spectral_report("Family C.3 K-even rate shadow", h_rate)
