"""KU-3 Family A: Berry-Keating xp compressions on the Z/6 Bures lift."""

from __future__ import annotations

import numpy as np

from hpo_common import (
    centered_position,
    cyclic_momentum,
    hermitian_part,
    print_matrix,
    print_projection_residuals,
    print_spectral_report,
    projected_critical_line_ops,
    sym,
)


def cyclic_bk_matrix() -> np.ndarray:
    """Finite cyclic analogue of (xp+px)/2 on the residue basis."""
    x = centered_position()
    p = cyclic_momentum()
    return hermitian_part(sym(x, p))


def hurwitz_projected_bk_matrix() -> np.ndarray:
    """Projected t*(-i d/dt) operator on the six Hurwitz channels."""
    ops = projected_critical_line_ops()
    print_projection_residuals(ops)
    return hermitian_part(sym(ops.x_t, ops.p_t))


if __name__ == "__main__":
    print("\nFamily A.1: canonical finite cyclic Berry-Keating compression")
    h_cyclic = cyclic_bk_matrix()
    print_matrix("H_A_cyclic = 1/2(X_6 P_6 + P_6 X_6)", h_cyclic)
    print_spectral_report("Family A.1 cyclic BK", h_cyclic)

    print("\nFamily A.2: Hurwitz-channel least-squares compression")
    print("basis: f_0(t)=6^(-s), f_r(t)=6^(-s) zeta(s,r/6), s=1/2+it")
    h_hurwitz = hurwitz_projected_bk_matrix()
    print_matrix("H_A_hurwitz = projection of 1/2(t*(-i d/dt)+(-i d/dt)*t)", h_hurwitz)
    print_spectral_report("Family A.2 Hurwitz projected BK", h_hurwitz)
