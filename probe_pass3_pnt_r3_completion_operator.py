"""PNT-completed r=3 operator probe for Pass-3.

The completion profile showed that the missing ordinary tail is almost
entirely the missing r=3 layer.  This probe replaces that missing layer by
the prime-number-theorem/theta-density approximation

    d theta(t) ~= dt,

so

    sum_{p>X} (log p)^(2m) p^(-3/2)
      ~= integral_X^infty (log t)^(2m-1) t^(-3/2) dt.

This is not a proof certificate.  It is the first native completion model:
finite scaffold + analytic r=3 density completion.  If it lands near the
completed Jacobi operator, then the remaining proof target is an explicit
theta-error/residue certificate.
"""

from __future__ import annotations

from math import factorial

import importlib.util
from pathlib import Path

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
from probe_pass3_tail_control_bounds import integral_tail_power_log


mp.mp.dps = 100

GNS_PATH = Path(__file__).with_name("probe_pass3_gns_helmert_square_operator.py")
spec = importlib.util.spec_from_file_location("gns_probe", GNS_PATH)
gns = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gns)
gns.mp.mp.dps = 100


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def pnt_r3_missing_ell(m: int, x: mp.mpf) -> mp.mpf:
    k = 2 * m
    scale = ((-1) ** (m + 1)) * (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1))
    return scale * integral_tail_power_log(mp.mpf("1.5"), k - 1, x)


def pnt_completed_mu(
    order: int, prime_count: int, r_cut: int, mobius_cutoff: int
) -> tuple[list[mp.mpf], int]:
    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    x = mp.mpf(primes[-1])
    return [finite_mu[m - 1] + pnt_r3_missing_ell(m, x) for m in range(1, order + 1)], primes[-1]


def dets(mu: list[mp.mpf], support: mp.mpf) -> tuple[list[mp.mpf], list[mp.mpf]]:
    d = [gates.det_matrix(gates.hankel_matrix(mu, i)) for i in range(4)]
    g = [gates.det_matrix(gates.localizer_matrix(mu, i, support)) for i in range(4)]
    return d, g


def summarize_operator(label: str, mu: list[mp.mpf], n: int, support: mp.mpf) -> None:
    print(label)
    try:
        jmat = gns.jacobi_from_moments(mu, n)
    except ValueError as exc:
        print(f"  GNS failed: {exc}")
        return
    vals = mp.eigsy(jmat, eigvals_only=True)
    print(f"  min eigenvalue {fmt(min(vals), 18)}")
    print(f"  max eigenvalue {fmt(max(vals), 18)}")
    print(f"  within [0,R]  {min(vals) >= 0 and max(vals) <= support}")
    print("  i   alpha_i               beta_i")
    for i in range(n):
        alpha = mp.re(jmat[i, i])
        beta = mp.re(jmat[i, i + 1]) if i + 1 < n else mp.mpf(0)
        print(f"  {i:1d}  {fmt(alpha, 18):>22} {fmt(beta, 18):>22}")


def main() -> None:
    order = 8
    n = 4
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    x = mp.mpf(primes[-1])
    pnt_mu = [finite_mu[m - 1] + pnt_r3_missing_ell(m, x) for m in range(1, order + 1)]
    true_mu = eta.total_ells(None, order)

    print("Pass-3 PNT r=3 completion operator")
    print(f"prime_count={prime_count}, X={primes[-1]}, r_cut={r_cut}, mobius_cutoff={mobius_cutoff}")
    print()

    print("Moment comparison")
    print("m   finite_mu          PNT completed      true completed     PNT-true")
    for m in range(1, order + 1):
        print(
            f"{m:1d}  {fmt(finite_mu[m-1], 12):>16} {fmt(pnt_mu[m-1], 12):>16} "
            f"{fmt(true_mu[m-1], 12):>16} {fmt(pnt_mu[m-1]-true_mu[m-1], 8):>14}"
        )
    print()

    print("Gate comparison")
    print("gate  finite             PNT completed     true completed")
    finite_d, finite_g = dets(finite_mu, support)
    pnt_d, pnt_g = dets(pnt_mu, support)
    true_d, true_g = dets(true_mu, support)
    for i in range(4):
        print(f"D{i:<3} {fmt(finite_d[i], 10):>16} {fmt(pnt_d[i], 10):>16} {fmt(true_d[i], 10):>16}")
    for i in range(4):
        print(f"G{i:<3} {fmt(finite_g[i], 10):>16} {fmt(pnt_g[i], 10):>16} {fmt(true_g[i], 10):>16}")
    print()

    summarize_operator("PNT-completed ledger", pnt_mu, n, support)
    print()
    summarize_operator("True completed ledger", true_mu, n, support)
    print()

    print("Interpretation")
    print("- PNT r=3 completion moves moments close to the exact completion.")
    print("- The remaining gap is the theta fluctuation/residue around dtheta=dt.")
    print("- If the PNT-completed operator is not positive, the residue is gate-relevant.")


if __name__ == "__main__":
    main()
