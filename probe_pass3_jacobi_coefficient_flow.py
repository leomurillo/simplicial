"""Track finite Jacobi/Helmert coefficient flow across moment windows.

The Pass-3 native target is no longer an abstract positivity statement:
derive the nearest-neighbor Helmert-Jacobi coefficients alpha_i, beta_i.

This probe computes the GNS/Jacobi matrix for increasing window sizes and
prints the first coefficients. Stabilization of fixed low rungs is the
finite evidence expected from a genuine limiting bounded operator.

Numerical evidence only; not a proof.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp


mp.mp.dps = 120

GNS_PATH = Path(__file__).with_name("probe_pass3_gns_helmert_square_operator.py")
spec = importlib.util.spec_from_file_location("gns_probe", GNS_PATH)
gns_probe = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gns_probe)
mp.mp.dps = 120
gns_probe.mp.mp.dps = 120
gns_probe.folded_probe.mp.mp.dps = 120


def fmt(x: mp.mpf, digits: int = 15) -> str:
    return mp.nstr(x, digits)


def coefficients(n: int, ell: list[mp.mpf]):
    jmat = gns_probe.jacobi_from_moments(ell, n)
    alpha = [mp.re(jmat[i, i]) for i in range(n)]
    beta = [mp.re(jmat[i, i + 1]) for i in range(n - 1)]
    return alpha, beta


def main() -> None:
    sizes = [4, 6, 8, 10, 12]
    max_n = max(sizes)
    order = 2 * max_n + 6
    b = gns_probe.folded_probe.folded_coefficients(
        order + 2, radius=mp.mpf("1.0"), samples=2048
    )
    ell = gns_probe.folded_probe.formal_log_cumulants(b, order + 1)

    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)
    print(f"support R=gamma_1^-2 {fmt(support, 24)}")

    previous: dict[int, tuple[list[mp.mpf], list[mp.mpf]]] = {}
    for n in sizes:
        alpha, beta = coefficients(n, ell)
        previous[n] = (alpha, beta)
        print(f"\nN={n}")
        print("i   alpha_i                 beta_i")
        for i in range(min(8, n)):
            beta_str = fmt(beta[i], 18) if i < len(beta) else "0"
            print(f"{i:2d}  {fmt(alpha[i], 18):>22}  {beta_str:>22}")

    print("\nFixed-rung stabilization against N=12")
    ref_alpha, ref_beta = previous[max_n]
    for n in sizes[:-1]:
        alpha, beta = previous[n]
        k_alpha = min(len(alpha), 6)
        k_beta = min(len(beta), 6)
        da = max(abs(alpha[i] - ref_alpha[i]) for i in range(k_alpha))
        db = max(abs(beta[i] - ref_beta[i]) for i in range(k_beta))
        print(
            f"N={n:2d}  max |alpha_i-alpha_i(12)| i<6 = {fmt(da, 8)}; "
            f"max |beta_i-beta_i(12)| i<6 = {fmt(db, 8)}"
        )


if __name__ == "__main__":
    main()
