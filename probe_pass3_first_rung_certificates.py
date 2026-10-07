"""First-rung certificates for the Pass-3 Helmert/Jacobi target.

This probe turns the local acceptance tests into an auditable table:

    mu_n = ell_{n+1}
    D_i = det(mu_{a+b})_{0<=a,b<=i}
    beta_i = sqrt(D_{i+1} D_{i-1}) / D_i

It also checks the first upper-radius localizer gates for

    R = gamma_1^-2.

Numerical evidence only; not a proof of the native positivity theorem.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp


mp.mp.dps = 120

FOLDED_PATH = Path(__file__).with_name("probe_pass3_folded_xi_trace_model.py")
GNS_PATH = Path(__file__).with_name("probe_pass3_gns_helmert_square_operator.py")

folded_spec = importlib.util.spec_from_file_location("folded_probe", FOLDED_PATH)
folded_probe = importlib.util.module_from_spec(folded_spec)
assert folded_spec.loader is not None
folded_spec.loader.exec_module(folded_probe)

gns_spec = importlib.util.spec_from_file_location("gns_probe", GNS_PATH)
gns_probe = importlib.util.module_from_spec(gns_spec)
assert gns_spec.loader is not None
gns_spec.loader.exec_module(gns_probe)

mp.mp.dps = 120
folded_probe.mp.mp.dps = 120
gns_probe.mp.mp.dps = 120


def fmt(x: mp.mpf, digits: int = 22) -> str:
    return mp.nstr(x, digits)


def det(mat: list[list[mp.mpf]]) -> mp.mpf:
    return mp.det(mp.matrix(mat))


def hankel_det(mu: list[mp.mpf], i: int) -> mp.mpf:
    return det([[mu[a + b] for b in range(i + 1)] for a in range(i + 1)])


def localizer_det(mu: list[mp.mpf], i: int, radius: mp.mpf) -> mp.mpf:
    return det(
        [
            [radius * mu[a + b] - mu[a + b + 1] for b in range(i + 1)]
            for a in range(i + 1)
        ]
    )


def main() -> None:
    order = 12
    coeffs = folded_probe.folded_coefficients(
        order + 2, radius=mp.mpf("1.0"), samples=2048
    )
    mu = folded_probe.formal_log_cumulants(coeffs, order + 1)

    jmat = gns_probe.jacobi_from_moments(mu, 5)

    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)

    print(f"R=gamma_1^-2 {fmt(radius, 28)}")
    print("\nFirst moments mu_n=ell_{n+1}")
    for n in range(5):
        print(f"mu[{n}] = {fmt(mu[n], 28)}")

    d0 = hankel_det(mu, 0)
    d1 = hankel_det(mu, 1)
    d2 = hankel_det(mu, 2)
    d3 = hankel_det(mu, 3)
    d = [d0, d1, d2, d3]

    print("\nHankel volumes D_i")
    for i, value in enumerate(d):
        print(f"D[{i}] = {fmt(value, 28)}")

    alpha0 = mu[1] / mu[0]
    beta0 = mp.sqrt(d1) / d0
    alpha1 = (mu[0] ** 2 * mu[3] - 2 * mu[0] * mu[1] * mu[2] + mu[1] ** 3) / (
        mu[0] * d1
    )
    beta1 = mp.sqrt(d0 * d2) / d1
    beta2 = mp.sqrt(d1 * d3) / d2

    print("\nFormula coefficients")
    print(f"alpha[0] = {fmt(alpha0, 28)}")
    print(f"beta [0] = {fmt(beta0, 28)}")
    print(f"alpha[1] = {fmt(alpha1, 28)}")
    print(f"beta [1] = {fmt(beta1, 28)}")
    print(f"beta [2] = {fmt(beta2, 28)}")

    print("\nJacobi matrix coefficients")
    for i in range(4):
        beta = jmat[i, i + 1] if i < 4 else mp.mpf(0)
        print(f"i={i} alpha={fmt(jmat[i, i], 28)} beta={fmt(beta, 28)}")

    print("\nFormula minus Jacobi")
    print(f"alpha0 diff = {fmt(alpha0 - jmat[0, 0], 8)}")
    print(f"beta0  diff = {fmt(beta0 - jmat[0, 1], 8)}")
    print(f"alpha1 diff = {fmt(alpha1 - jmat[1, 1], 8)}")
    print(f"beta1  diff = {fmt(beta1 - jmat[1, 2], 8)}")
    print(f"beta2  diff = {fmt(beta2 - jmat[2, 3], 8)}")

    print("\nUpper-radius gates det G_i^(R)")
    for i in range(4):
        print(f"G[{i}] = {fmt(localizer_det(mu, i, radius), 28)}")


if __name__ == "__main__":
    main()
