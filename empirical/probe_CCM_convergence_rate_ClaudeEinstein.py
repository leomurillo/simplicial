"""Convergence rate of CCM construction: |gamma_n(lambda) - gamma_n| vs lambda.

The CCM construction at finite "scale" lambda (corresponding to Mellin-grid
size N ~ 4 pi lambda^2):
  1. Mellin grid on t in [0, T_lambda] with N points, spacing dt = T_lambda / N.
  2. T_lambda ~ resolved range ~ lambda^2 / log(lambda).
  3. Find local minima of |zeta(1/2 + it)| -> approximate gamma_n.
  4. Error |gamma_n(lambda) - gamma_n| <~ dt (grid resolution).

Heuristic: error ~ T_lambda / N ~ 1 / log(lambda) (since N ~ lambda^2 and
T_lambda ~ lambda^2 / log lambda, so dt ~ 1/log lambda).

This probe varies N and verifies the 1/log(lambda)-like rate.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


mp.mp.dps = 30


def zeta_at_critical(t: float) -> complex:
    return complex(mp.zeta(mp.mpc(mp.mpf("0.5"), t)))


def find_minima(vals: np.ndarray, t_grid: np.ndarray, threshold: float):
    """Find local minima of |vals| below threshold."""
    minima = []
    for i in range(1, len(vals) - 1):
        if (
            vals[i] < vals[i - 1]
            and vals[i] < vals[i + 1]
            and vals[i] < threshold
        ):
            # Parabolic interpolation
            denom = vals[i - 1] - 2 * vals[i] + vals[i + 1]
            if abs(denom) > 1e-30:
                dx = 0.5 * (vals[i - 1] - vals[i + 1]) / denom
                t_refined = t_grid[i] + dx * (t_grid[i + 1] - t_grid[i])
            else:
                t_refined = t_grid[i]
            minima.append(t_refined)
    return minima


def main():
    known_gammas = [
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
    print("CCM convergence rate: |gamma_n(lambda) - gamma_n| as Mellin grid refines")
    print("=" * 100)
    print()
    print("In CCM: dim V_lambda^+ ~ 4 pi lambda^2.")
    print("Identify with Mellin grid size N.  Set T = 50, dt = T/N.")
    print()
    print("Expect: |gamma_n(lambda) - gamma_n| <~ dt ~ 1/N (grid resolution).")
    print()

    T_max = 50.0

    # First validate by varying N from 1000 to 32000 (lambda ~ N/(4 pi))^{1/2}
    N_list = [1000, 2000, 4000, 8000, 16000, 32000]

    results = {n: [] for n in range(5)}

    for N_grid in N_list:
        t_grid = np.linspace(0.01, T_max, N_grid)
        zeta_vals = np.array([abs(zeta_at_critical(float(t))) for t in t_grid])

        gamma_approx = find_minima(zeta_vals, t_grid, threshold=0.5)[:10]
        dt = (T_max - 0.01) / N_grid
        # Equivalent lambda
        lam_eq = np.sqrt(N_grid / (4 * np.pi))

        print(f"N = {N_grid}, dt = {dt:.5f}, lambda_equiv = {lam_eq:.2f}")
        for n, gn in enumerate(gamma_approx[:5]):
            if n < len(known_gammas):
                err = abs(gn - known_gammas[n])
                results[n].append((N_grid, lam_eq, err))
                print(
                    f"  gamma_{n+1}(lambda) = {gn:.6f}  known = {known_gammas[n]:.6f}  "
                    f"err = {err:.4e}"
                )
        print()

    # Convergence rate analysis
    print("=" * 100)
    print("Convergence rate analysis: err vs 1/N and 1/log(lambda)")
    print("=" * 100)

    for n in range(5):
        print(f"\nFor gamma_{n+1} = {known_gammas[n]:.4f}:")
        print(
            f"  {'N':>6}  {'lambda':>8}  {'err':>14}  {'err*N':>10}  {'err*log(lambda)':>18}"
        )
        for N_grid, lam_eq, err in results[n]:
            err_N = err * N_grid
            err_log = err * np.log(lam_eq)
            print(
                f"  {N_grid:>6}  {lam_eq:>8.2f}  {err:>14.4e}  "
                f"{err_N:>10.4f}  {err_log:>18.4e}"
            )

    # Final remark: a cleaner test of the 1/N law
    print("\n" + "=" * 100)
    print("Cleanest fit: err ~ C/N (grid resolution rate)")
    print("=" * 100)
    print(
        f"\n{'gamma_n':>9}  {'C from N=1000':>16}  {'C from N=4000':>16}  "
        f"{'C from N=16000':>16}  {'C from N=32000':>16}"
    )
    for n in range(5):
        row = [f"  gamma_{n+1}"]
        for idx in [0, 2, 4, 5]:
            if idx < len(results[n]):
                N_grid, lam_eq, err = results[n][idx]
                C_val = err * N_grid
                row.append(f"{C_val:>16.4f}")
            else:
                row.append(f"{'--':>16}")
        print("  ".join(row))


if __name__ == "__main__":
    main()
