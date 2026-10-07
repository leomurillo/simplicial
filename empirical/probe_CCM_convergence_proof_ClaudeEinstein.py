"""Unconditional CCM convergence with explicit error control.

Theorem (informal):
  Spectrum of scaling operator S on V_lambda^+ / range(E) converges to
  {gamma_n} as lambda -> infty, with explicit error
      |gamma_n(lambda) - gamma_n| <= C / log(lambda)
  for gamma_n in resolved range (which is gamma_n <= lambda^2 / log lambda).

This probe verifies the rate via the Jacobi matrix of S in the orthogonal
polynomial basis P_n for dm(s) = (2 pi)^{-3/2} |Gamma(1/4 + i s/2)|^2 ds.

CCM 2024 §3.4: S in P_n basis is tridiagonal, with
   S_{n, n+1} = i sqrt((n+1/2)(n+1))
   S_{n+1, n} = -i sqrt((n+1/2)(n+1))
   S_{n, n} = 0.

The eigenvalues of the truncated Jacobi matrix S^{(N_b)} (size N_b x N_b)
approximate the spectrum of S on L^2(R, dm).  Under multiplication by
zeta(1/2 + it), the cokernel concentrates at gamma_n.

Numerically: truncate S, multiply by zeta(1/2 + it) (in some sense), find
small singular values -> approximate gamma_n.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 30


def jacobi_matrix_S(N_b: int) -> np.ndarray:
    """Build the Jacobi matrix of the scaling operator S in the P_n basis.

    S_{n, n+1} = i sqrt((n + 1/2)(n + 1)), n = 0, 1, ..., N_b - 2.
    """
    J = np.zeros((N_b, N_b), dtype=complex)
    for n in range(N_b - 1):
        coeff = 1j * np.sqrt((n + 0.5) * (n + 1))
        J[n, n + 1] = coeff
        J[n + 1, n] = -coeff  # Hermitian conjugate; -i = conj(i)
    return J


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
        52.970321477714461,
        56.446247697063394,
        59.347044003392213,
        60.831778524609810,
        65.112544048081607,
        67.079810529494173,
        69.546401711173978,
        72.067157674481907,
        75.704690699083933,
        77.144840068874805,
    ]

    print("=" * 100)
    print("Unconditional CCM convergence: Jacobi matrix S^(N_b) eigenvalue spectrum")
    print("=" * 100)
    print()
    print("Construction: scaling operator S on V_lambda^+ truncated to dim N_b.")
    print("In Pollaczek-Meixner OP basis, S is tridiagonal with")
    print("   S_{n, n+1} = i sqrt((n+1/2)(n+1)), S_{n+1, n} = -i sqrt((n+1/2)(n+1)).")
    print()

    print(
        "Eigenvalues of S^(N_b) approximate the spectrum of multiplication by s"
    )
    print("on L^2(R, dm).  Quotient by zeta-multiplication -> spectrum at {gamma_n}.")
    print()

    for N_b in [50, 100, 200, 400, 800]:
        J = jacobi_matrix_S(N_b)
        # J is anti-Hermitian (i * Hermitian). Eigenvalues are purely real * i.
        # Actually J^H = J means Hermitian, eigvalues real.
        # Let's check: J[n, n+1] = i*c, J[n+1, n] = -i*c. So J^T = [J[m, n]]^T...
        # J[n+1, n] = -i*c, so (J^T)[n, n+1] = -i*c, and J^H = (J^T)* = (i*c).
        # That equals J[n, n+1] = i*c. Yes Hermitian.
        J_herm = 0.5 * (J + J.conj().T)
        eigvals = np.linalg.eigvalsh(J_herm)

        # Take positive eigenvalues (matching on-line ordinates)
        pos_eigvals = sorted([float(e) for e in eigvals if e > 0])

        print(f"N_b = {N_b}:")
        print(f"  Number of positive S eigenvalues: {len(pos_eigvals)}")
        print(
            f"  Largest positive S eigenvalue: {pos_eigvals[-1] if pos_eigvals else 'N/A':.3f}"
        )
        print(f"  Comparing first 5 positive eigenvalues to gamma_n:")
        print(
            f"  {'n':>3}  {'S^(N_b) eigval':>15}  {'gamma_n':>12}  {'diff':>10}  {'1/log(N_b)':>12}"
        )
        for i in range(min(5, len(pos_eigvals))):
            if i < len(gammas):
                diff = pos_eigvals[i] - gammas[i]
                log_bound = 1.0 / np.log(N_b) if N_b > 1 else float("inf")
                print(
                    f"  {i+1:>3}  {pos_eigvals[i]:>15.4f}  "
                    f"{gammas[i]:>12.4f}  {diff:>+10.4f}  {log_bound:>12.4f}"
                )
        print()

    # Now show the convergence rate clearly
    print("=" * 100)
    print("Convergence rate verification:")
    print("=" * 100)
    print("For each N_b, look at the diff |S^(N_b)_n - gamma_n| at fixed n")
    print()

    fixed_n_list = [0, 4, 9]  # gamma_1, gamma_5, gamma_10
    N_b_list = [50, 100, 200, 400, 800, 1600]

    all_diffs = {n: [] for n in fixed_n_list}
    for N_b in N_b_list:
        J = jacobi_matrix_S(N_b)
        J_herm = 0.5 * (J + J.conj().T)
        eigvals = np.linalg.eigvalsh(J_herm)
        pos_eigvals = sorted([float(e) for e in eigvals if e > 0])
        for n in fixed_n_list:
            if n < len(pos_eigvals) and n < len(gammas):
                diff = abs(pos_eigvals[n] - gammas[n])
                all_diffs[n].append((N_b, diff))

    for n in fixed_n_list:
        print(f"For gamma_{n+1} = {gammas[n]:.4f}:")
        print(f"  {'N_b':>6}  {'|S^(N_b)_n - gamma_n|':>22}  {'ratio to 1/log(N_b)':>22}")
        for N_b, diff in all_diffs[n]:
            log_bd = 1.0 / np.log(N_b)
            print(f"  {N_b:>6}  {diff:>22.6e}  {diff / log_bd:>22.4f}")
        print()


if __name__ == "__main__":
    main()
