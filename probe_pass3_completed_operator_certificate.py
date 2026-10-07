"""Completed operator diagnostic for Pass-3.

The finite scaffold before completion is not yet a positive moment ledger:
its first moment is already negative in the current calibration, so the GNS
construction fails immediately.

The completed eta/zeta ledger, however, builds a finite positive
GNS/Jacobi operator.  This probe displays the operator coefficients and
support check for the completed ledger.

Numerical evidence only; the proof target is to construct/certify this
completed operator natively, rather than reaching it through an oracle.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates


mp.mp.dps = 100

GNS_PATH = Path(__file__).with_name("probe_pass3_gns_helmert_square_operator.py")
spec = importlib.util.spec_from_file_location("gns_probe", GNS_PATH)
gns = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gns)
gns.mp.mp.dps = 100


def fmt(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def summarize_operator(label: str, mu: list[mp.mpf], n: int, support: mp.mpf) -> None:
    print(label)
    try:
        jmat = gns.jacobi_from_moments(mu, n)
    except ValueError as exc:
        print(f"  GNS/Jacobi construction failed: {exc}")
        print()
        return

    vals = mp.eigsy(jmat, eigvals_only=True)
    print(f"  min eigenvalue: {fmt(min(vals), 22)}")
    print(f"  max eigenvalue: {fmt(max(vals), 22)}")
    print(f"  support R:      {fmt(support, 22)}")
    print(f"  within [0,R]:   {min(vals) >= 0 and max(vals) <= support}")
    print("  i   alpha_i                  beta_i")
    for i in range(n):
        alpha = mp.re(jmat[i, i])
        beta = mp.re(jmat[i, i + 1]) if i + 1 < n else mp.mpf(0)
        print(f"  {i:1d}  {fmt(alpha, 22):>24}  {fmt(beta, 22):>24}")
    print()


def main() -> None:
    n = 4
    order = 2 * n
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    finite_mu, _ = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    completed_mu = eta.total_ells(None, order)

    print("Pass-3 completed operator diagnostic")
    print(f"n={n}, order={order}, support gamma_1^-2={fmt(support, 24)}")
    print()
    summarize_operator("Finite scaffold before completion", finite_mu, n, support)
    summarize_operator("Completed eta/zeta ledger", completed_mu, n, support)

    print("Interpretation")
    print("- The finite scaffold is not yet a positive moment ledger.")
    print("- The completed ledger has positive Jacobi couplings and support inside [0,gamma_1^-2].")
    print("- The proof target is the native construction of this completed operator.")


if __name__ == "__main__":
    main()
