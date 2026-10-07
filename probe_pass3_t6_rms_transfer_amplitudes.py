"""T6 RMS reading of the Pass-3 Schur-pivot ladder.

T6 says RMS is the gauge of squared substance. The Pass-3 Schur pivots are
exactly squared residual norms:

    h_n = L(P_n^2),      k_n = L_R(Q_n^2).

Therefore sqrt(h_n) and sqrt(k_n) are the residual amplitudes, while

    beta_n = sqrt(h_{n+1}/h_n),
    beta_n(R) = sqrt(k_{n+1}/k_n)

are the RMS transfer amplitudes between consecutive monic residual rungs.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_t5_schur_pivots as pivots


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 14) -> str:
    return mp.nstr(x, digits)


def schur_norms(mu: list[mp.mpf], max_n: int) -> list[mp.mpf]:
    return [pivots.schur_pivot(mu, n)[0] for n in range(max_n + 1)]


def main() -> None:
    max_n = 5
    order = 2 * max_n + 6
    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    mu = eta.total_ells(None, order)
    boundary_mu = [radius * mu[i] - mu[i + 1] for i in range(order - 1)]

    h = schur_norms(mu, max_n)
    k = schur_norms(boundary_mu, max_n)

    print("Pass-3 T6 RMS transfer amplitudes")
    print(f"support R=gamma_1^-2={fmt(radius, 20)}")
    print()
    print("Interior residual RMS ladder")
    print("n   h_n=L(P_n^2)          sqrt(h_n)           beta_n=sqrt(h_{n+1}/h_n)")
    for n in range(max_n):
        beta = mp.sqrt(h[n + 1] / h[n])
        print(f"{n:1d}  {fmt(h[n], 16):>20} {fmt(mp.sqrt(h[n]), 16):>20} {fmt(beta, 16):>28}")
    print(f"{max_n:1d}  {fmt(h[max_n], 16):>20} {fmt(mp.sqrt(h[max_n]), 16):>20} {'':>28}")

    print()
    print("Boundary-complement residual RMS ladder")
    print("n   k_n=L_R(Q_n^2)        sqrt(k_n)           beta_n(R)=sqrt(k_{n+1}/k_n)")
    for n in range(max_n):
        beta = mp.sqrt(k[n + 1] / k[n])
        print(f"{n:1d}  {fmt(k[n], 16):>20} {fmt(mp.sqrt(k[n]), 16):>20} {fmt(beta, 16):>28}")
    print(f"{max_n:1d}  {fmt(k[max_n], 16):>20} {fmt(mp.sqrt(k[max_n]), 16):>20} {'':>28}")

    print()
    print("Interpretation")
    print("- T5 reads h_n,k_n as reciprocal/log norm-square coordinates.")
    print("- T6 reads sqrt(h_n),sqrt(k_n) as RMS residual amplitudes.")
    print("- The Jacobi couplings beta_n are amplitude transfer ratios.")


if __name__ == "__main__":
    main()
