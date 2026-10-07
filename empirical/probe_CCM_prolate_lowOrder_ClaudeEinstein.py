"""Low-order numerical Connes-Consani-Moscovici prolate operator.

Per CCM (Annals of Functional Analysis 2024, arXiv:2310.18423), the prolate
operator on L^2(R, dx) is

    W := S^2 + N

where S = -i (x d/dx + 1/2) is the squared scaling and N is the Hermite
grading operator.  Eigenvalues asymptotically are gamma_n^2.

Concrete realization: use the Hermite-function basis on R, in which:

    Hermite basis: h_n(x) = (2^n n! sqrt(pi))^{-1/2} H_n(x) e^{-x^2/2}
    N h_n = n h_n
    S in Hermite basis: matrix element <h_m | S | h_n> = -i (m+1/2) delta_{m,n}
        only if we have the right basis -- actually S = -i(x d/dx + 1/2) is NOT
        diagonal in Hermite basis.

For an honest low-order construction, project S^2 + N onto the finite-dimensional
subspace spanned by the first N_b Hermite functions and diagonalize.

This probe constructs the matrix of W in the Hermite basis and computes
its eigenvalues, comparing to gamma_n^2.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 30


def hermite_matrix_x_dx(N_b: int) -> np.ndarray:
    """Matrix of x d/dx in Hermite basis up to size N_b x N_b.

    In Hermite basis: x h_n = sqrt(n/2) h_{n-1} + sqrt((n+1)/2) h_{n+1}
                      d/dx h_n = sqrt(n/2) h_{n-1} - sqrt((n+1)/2) h_{n+1}
    So x d/dx h_n = sqrt(n/2)(sqrt((n-1)/2) h_{n-2} + sqrt(n/2) h_n)
                   - sqrt((n+1)/2)(sqrt(n/2) h_n + sqrt((n+2)/2) h_{n+2})
                  = (n/2) h_n - sqrt((n+1)(n+2))/2 h_{n+2}
                    + sqrt(n(n-1))/2 h_{n-2}
                    - (n+1)/2 h_n
                  = -1/2 h_n + sqrt(n(n-1))/2 h_{n-2} - sqrt((n+1)(n+2))/2 h_{n+2}
    """
    M = np.zeros((N_b, N_b))
    for n in range(N_b):
        M[n, n] = -0.5
        if n - 2 >= 0:
            M[n - 2, n] = np.sqrt(n * (n - 1)) / 2
        if n + 2 < N_b:
            M[n + 2, n] = -np.sqrt((n + 1) * (n + 2)) / 2
    return M


def prolate_operator_matrix(N_b: int) -> np.ndarray:
    """W = S^2 + N where S = -i(x d/dx + 1/2).

    S = -i (x d/dx + 1/2) = -i (x d/dx) - i/2.
    S^2 = -(x d/dx + 1/2)^2.
    Using shortcut: S^2 + N = -(x d/dx + 1/2)^2 + N.
    """
    xddx = hermite_matrix_x_dx(N_b)
    half_I = 0.5 * np.eye(N_b)
    S_op = -1j * (xddx + half_I)
    S_squared = S_op @ S_op
    N_op = np.diag(np.arange(N_b, dtype=float))
    W = -np.real(S_squared) + N_op  # S^2 real because S Hermitian on tempered domain
    # Actually let's be careful: S is anti-Hermitian here since we constructed it as -i(...).
    # S^2 is then -(...)^2 which is negative-definite (so we use -(S^2 with i^2)).
    # Easier: just construct H = (xddx + 1/2 I)^2 + N (real symmetric).
    M = xddx + half_I
    H = M @ M + N_op
    # Symmetrize for numerical safety
    H = 0.5 * (H + H.T)
    return H


def main():
    gammas = [
        14.134725141734693,
        21.022039638771554,
        25.010857580145688,
        30.424876125859513,
        32.935061587739189,
        37.586178158825671,
        40.918719012147495,
        43.327073280914999,
        48.005150881167159,
        49.773832477672302,
    ]
    gamma_squared = [g**2 for g in gammas]

    print("=" * 100)
    print("Connes-Consani-Moscovici prolate operator W = (x d/dx + 1/2)^2 + N")
    print("=" * 100)
    print(f"Hermite truncation: N_b = 50, 100, 200, 400")
    print()

    print("First 10 expected gamma_n^2:")
    for n, gs in enumerate(gamma_squared, 1):
        print(f"  gamma_{n}^2 = {gs:.4f}")
    print()

    for N_b in [50, 100, 200, 400]:
        H = prolate_operator_matrix(N_b)
        eigvals = sorted(np.linalg.eigvalsh(H))
        # Compare to gamma_n^2
        print(f"N_b = {N_b}, first 10 eigenvalues of W:")
        for i in range(min(10, len(eigvals))):
            eig = eigvals[i]
            if i < len(gamma_squared):
                gs = gamma_squared[i]
                diff = (eig - gs) / gs
                print(
                    f"  W_{i+1} = {eig:.4f}  (gamma_{i+1}^2 = {gs:.4f}, "
                    f"rel diff = {diff:+.3f})"
                )
            else:
                print(f"  W_{i+1} = {eig:.4f}")
        print()


if __name__ == "__main__":
    main()
