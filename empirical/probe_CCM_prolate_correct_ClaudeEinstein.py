"""Connes-Consani-Moscovici prolate operator W_lambda, correct implementation.

Per CCM 2024 (arXiv:2310.18423) equation (4):

  (W_lambda psi)(q) = -partial[(lambda^2 - q^2) partial] psi(q) + (2 pi lambda q)^2 psi(q)

on L^2(R)^{ev} (even functions on R).

Substituting q = lambda * x rescales to the classical PSWF equation on [-1, 1]:

  L_c tilde_psi(x) = -partial_x[(1-x^2) partial_x tilde_psi] + c^2 x^2 tilde_psi

with parameter c = 2 pi lambda^2.

CCM claim: positive eigenvalues of W_lambda relate to {gamma_n^2} after the
quotient construction (Weil radical / range of map E).  The raw PSWF
eigenvalues chi_n(c) are NOT gamma_n^2 directly, but the **quotient
structure** is what produces zeta zeros.

This probe:
  1. Builds the discretized L_c via finite differences on [-1, 1].
  2. Computes its eigenvalues chi_n(c) for various c (= 2 pi lambda^2).
  3. Compares to PSWF asymptotic and to gamma_n^2.
  4. Separates even/odd eigenfunctions (since CCM work in L^2(R)^{ev}).
"""

from __future__ import annotations

import numpy as np


def prolate_diff_op(N: int, c: float) -> np.ndarray:
    """L_c psi = -d/dx [(1-x^2) d/dx psi] + c^2 x^2 psi on [-1, 1] via finite diff.

    Use N interior points x_i in (-1, 1) with Dirichlet boundary conditions
    psi(-1) = psi(1) = 0.  Step h = 2/(N+1).
    """
    h = 2.0 / (N + 1)
    x = np.linspace(-1 + h, 1 - h, N)  # interior grid

    # Coefficient (1 - x^2) evaluated at half-grid points x_{i +/- 1/2}:
    x_half_left = x - h / 2  # x_{i-1/2}
    x_half_right = x + h / 2  # x_{i+1/2}
    p_left = 1 - x_half_left**2
    p_right = 1 - x_half_right**2

    # Build L: tridiagonal
    L = np.zeros((N, N))
    for i in range(N):
        # -d/dx [(1-x^2) d/dx psi] at x_i, central difference:
        # = -(1/h)[ (1-x_{i+1/2}^2)(psi_{i+1} - psi_i)/h - (1-x_{i-1/2}^2)(psi_i - psi_{i-1})/h ]
        # = -(1/h^2) [ (1-x_{i+1/2}^2) psi_{i+1} - ((1-x_{i+1/2}^2)+(1-x_{i-1/2}^2)) psi_i + (1-x_{i-1/2}^2) psi_{i-1} ]
        L[i, i] = (p_left[i] + p_right[i]) / h**2
        if i > 0:
            L[i, i - 1] = -p_left[i] / h**2
        if i < N - 1:
            L[i, i + 1] = -p_right[i] / h**2
        # + c^2 x^2 psi
        L[i, i] += c**2 * x[i] ** 2

    return L, x


def parity_split(eigfuncs: np.ndarray, x: np.ndarray) -> tuple[list[int], list[int]]:
    """Classify eigenfunctions by parity (even = symmetric under x -> -x).

    Returns (even_indices, odd_indices).
    """
    N = len(x)
    even_idx = []
    odd_idx = []
    for k in range(eigfuncs.shape[1]):
        psi = eigfuncs[:, k]
        # Compare psi(x) to psi(-x) by reversing the array (approximate, ok for symmetric grid)
        psi_reversed = psi[::-1]
        if np.allclose(psi, psi_reversed, atol=1e-3):
            even_idx.append(k)
        elif np.allclose(psi, -psi_reversed, atol=1e-3):
            odd_idx.append(k)
        # else: numerical noise, skip
    return even_idx, odd_idx


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

    print("=" * 100)
    print("Connes-Consani-Moscovici prolate operator on [-1,1]")
    print("L_c psi = -d/dx[(1-x^2) d/dx psi] + c^2 x^2 psi,  c = 2 pi lambda^2")
    print("=" * 100)

    # For each lambda, c = 2 pi lambda^2.
    # CCM claim positive eigenvalues of W_lambda relate to gamma_n^2 as lambda -> infty.

    for lam in [1.0, 2.0, 4.0, 8.0]:
        c = 2 * np.pi * lam**2
        N = 1000
        L, x = prolate_diff_op(N, c)
        L_sym = 0.5 * (L + L.T)
        eigvals, eigvecs = np.linalg.eigh(L_sym)

        even_idx, odd_idx = parity_split(eigvecs[:, :30], x)

        print(f"\nlambda = {lam}, c = 2 pi lambda^2 = {c:.4f}")
        print(f"First 10 eigenvalues of L_c:")
        for i in range(min(10, len(eigvals))):
            parity = "even" if i in even_idx else ("odd" if i in odd_idx else "?")
            # PSWF asymptotic: chi_n(c) ~ c(2n+1) - (2n^2+2n+1)/2 for c large
            asymp = c * (2 * i + 1) - (2 * i**2 + 2 * i + 1) / 2 if c > 5 else None
            asymp_str = f"  PSWF asymp = {asymp:.2f}" if asymp is not None else ""
            gamma_sq = gammas[i // 2] ** 2 if i // 2 < len(gammas) else None
            gamma_str = f"  gamma_{i//2+1}^2 = {gamma_sq:.2f}" if gamma_sq else ""
            print(
                f"  chi_{i+1}({c:.2f}) = {eigvals[i]:10.4f}  [{parity}]{asymp_str}{gamma_str}"
            )

    print("\n" + "=" * 100)
    print("Discussion:")
    print("=" * 100)
    print("The raw PSWF eigenvalues chi_n(c) follow the classical asymptotic")
    print("    chi_n(c) ~ c(2n+1) - (2n^2 + 2n + 1)/2 + O(1/c)")
    print("for c >> 1.  They are NOT directly gamma_n^2.")
    print()
    print("CCM 2024 construct zeta zeros via:")
    print("  (a) positive eigenspace of W_lambda (lambda -> infty);")
    print("  (b) quotient by range of E (Weil radical map);")
    print("  (c) scaling operator on quotient -> spectrum = {gamma_n}.")
    print()
    print("The raw spectrum chi_n(c) is the input; the quotient is the")
    print("operation that 'distills' gamma_n out of c-dependent eigenvalues.")
    print()
    print("Parity split: PSWFs are even/odd in x.  Even and odd subspaces")
    print("decouple under L_c (since c^2 x^2 is even and (1-x^2)d^2/dx^2 ")
    print("preserves parity).  This is the Z/2 spectral grading.")


if __name__ == "__main__":
    main()
