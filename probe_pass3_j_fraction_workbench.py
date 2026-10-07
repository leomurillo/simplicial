"""J-fraction workbench for the Pass-3 trace-gauge normal form.

This probe checks the continued-fraction resolvent

    F_N(x) = mu_0 / (1 + alpha_0 x
                     - beta_0^2 x^2 / (1 + alpha_1 x - ...))

against the direct logarithmic derivative

    F(x) = d/dx log B(x),  B(x)=Xi(i sqrt(x))/Xi(0).

The coefficients alpha_i, beta_i are computed from the folded xi moment
ledger by the finite GNS/Jacobi construction. This is a numerical
workbench for the final Pass-3 target, not a proof of the native
primorial construction.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp


mp.mp.dps = 100

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

mp.mp.dps = 100
folded_probe.mp.mp.dps = 100
gns_probe.mp.mp.dps = 100


def fmt(x: mp.mpf | mp.mpc, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def direct_f(x: mp.mpf) -> mp.mpf:
    b = folded_probe.B_folded
    return mp.re(mp.diff(b, x) / b(x))


def j_fraction(mu0: mp.mpf, alpha: list[mp.mpf], beta: list[mp.mpf], x: mp.mpf) -> mp.mpf:
    n = len(alpha)
    denom = 1 + alpha[-1] * x
    for i in range(n - 2, -1, -1):
        denom = 1 + alpha[i] * x - (beta[i] ** 2) * (x ** 2) / denom
    return mu0 / denom


def coefficients(mu: list[mp.mpf], n: int) -> tuple[mp.mpf, list[mp.mpf], list[mp.mpf]]:
    jmat = gns_probe.jacobi_from_moments(mu, n)
    alpha = [mp.re(jmat[i, i]) for i in range(n)]
    beta = [mp.re(jmat[i, i + 1]) for i in range(n - 1)]
    return mu[0], alpha, beta


def main() -> None:
    sizes = [4, 6, 8, 10, 12]
    max_n = max(sizes)
    order = 2 * max_n + 8
    coeffs = folded_probe.folded_coefficients(
        order + 2, radius=mp.mpf("1.0"), samples=2048
    )
    mu = folded_probe.formal_log_cumulants(coeffs, order + 1)

    points = [mp.mpf("0"), mp.mpf("1"), mp.mpf("10"), mp.mpf("100")]
    truth = {x: direct_f(x) for x in points}

    print("Direct F(x)=d/dx log B(x)")
    for x in points:
        print(f"x={fmt(x, 8):>6}  F(x)={fmt(truth[x], 28)}")

    print("\nFinite J-fraction approximants")
    print("N    x        F_N(x)                         rel.err")
    for n in sizes:
        mu0, alpha, beta = coefficients(mu, n)
        for x in points:
            approx = j_fraction(mu0, alpha, beta, x)
            err = abs(approx - truth[x]) / max(abs(truth[x]), mp.mpf("1e-80"))
            print(f"{n:2d}  {fmt(x, 8):>6}  {fmt(approx, 30):>32}  {fmt(err, 8)}")
        print()

    gamma1 = mp.im(mp.zetazero(1))
    radius = 1 / (gamma1 * gamma1)
    print(f"support gate R=gamma_1^-2 {fmt(radius, 28)}")
    mu0, alpha, beta = coefficients(mu, max_n)
    print("\nN=12 first coefficients")
    print("i   alpha_i                         beta_i")
    for i in range(8):
        beta_str = fmt(beta[i], 28) if i < len(beta) else "0"
        print(f"{i:2d}  {fmt(alpha[i], 28):>30}  {beta_str:>30}")


if __name__ == "__main__":
    main()
