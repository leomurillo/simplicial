"""T5 harmonic transfer identities for the Pass-3 gate ladder.

Adjacent determinant ratios are monic norm squares:

    H_i = D_i / D_{i-1}.

Their adjacent ratios are the Jacobi transfer couplings:

    beta_i^2 = H_{i+1} / H_i.

The upper-radius gates have the same interpretation after the Christoffel
boundary transform dnu_R(t) = (R - t) dnu(t):

    K_i = G_i / G_{i-1},
    beta_i(R)^2 = K_{i+1} / K_i.

This is the concrete transfer version of the T5 reading: determinant-ratio
certification is harmonic-gauge certification of the positive transfer flow.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_gns_helmert_square_operator as gns


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 16) -> str:
    return mp.nstr(x, digits)


def determinant_ratios(mu: list[mp.mpf], max_i: int) -> list[mp.mpf]:
    dets = [gates.det_matrix(gates.hankel_matrix(mu, i)) for i in range(max_i + 1)]
    prev = [mp.mpf(1)] + dets[:-1]
    return [dets[i] / prev[i] for i in range(max_i + 1)]


def localizer_ratios(mu: list[mp.mpf], radius: mp.mpf, max_i: int) -> list[mp.mpf]:
    dets = [
        gates.det_matrix(gates.localizer_matrix(mu, i, radius))
        for i in range(max_i + 1)
    ]
    prev = [mp.mpf(1)] + dets[:-1]
    return [dets[i] / prev[i] for i in range(max_i + 1)]


def jacobi_betas_squared(mu: list[mp.mpf], n: int) -> list[mp.mpf]:
    jmat = gns.jacobi_from_moments(mu, n)
    return [mp.re(jmat[i, i + 1] ** 2) for i in range(n - 1)]


def main() -> None:
    max_i = 4
    order = 2 * (max_i + 2) + 3
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    boundary_mu = [radius * mu[i] - mu[i + 1] for i in range(order - 1)]

    h = determinant_ratios(mu, max_i)
    k = localizer_ratios(mu, radius, max_i)
    beta2 = jacobi_betas_squared(mu, max_i + 2)
    beta2_boundary = jacobi_betas_squared(boundary_mu, max_i + 2)

    print("Pass-3 T5 transfer identities")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()

    print("Interior Hankel transfer")
    print("i   H_i=D_i/D_{i-1}       log H_i            H_{i+1}/H_i       beta_i^2          abs diff")
    for i in range(max_i):
        transfer = h[i + 1] / h[i]
        diff = abs(transfer - beta2[i])
        print(
            f"{i:1d}  {fmt(h[i], 16):>20} {fmt(mp.log(h[i]), 16):>18} "
            f"{fmt(transfer, 16):>18} {fmt(beta2[i], 16):>18} {fmt(diff, 5):>12}"
        )

    print()
    print("Upper-radius boundary-complement transfer")
    print("i   K_i=G_i/G_{i-1}       log K_i            K_{i+1}/K_i       beta_i(R)^2      abs diff")
    for i in range(max_i):
        transfer = k[i + 1] / k[i]
        diff = abs(transfer - beta2_boundary[i])
        print(
            f"{i:1d}  {fmt(k[i], 16):>20} {fmt(mp.log(k[i]), 16):>18} "
            f"{fmt(transfer, 16):>18} {fmt(beta2_boundary[i], 16):>18} {fmt(diff, 5):>12}"
        )

    print()
    print("Interpretation")
    print("- H_i and K_i are harmonic-gauge norm squares.")
    print("- log H_i and log K_i are additive reciprocal ledgers.")
    print("- differences of those log ledgers are the Jacobi transfer logs.")


if __name__ == "__main__":
    main()
