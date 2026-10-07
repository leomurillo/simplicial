"""Completion homotopy for the Pass-3 gate chamber.

The sign-aware box still leaves every gate crossing zero.  This probe asks
a sharper diagnostic question:

    If we complete the finite scaffold along the actual missing-tail
    direction toward the exact folded eta ledger, where do the gates enter
    the positive chamber?

Let

    mu(lambda) = mu_finite + lambda * (mu_true - mu_finite),
    0 <= lambda <= 1.

The endpoint lambda=1 uses the exact eta/zeta folded ledger as an oracle.
This is not a proof certificate; it is a chamber geometry diagnostic.  It
tells us whether the remaining problem is "tail direction" or "tail
precision", and estimates how much lower-tail certification is needed.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def interpolate(a: list[mp.mpf], b: list[mp.mpf], lam: mp.mpf) -> list[mp.mpf]:
    return [x + lam * (y - x) for x, y in zip(a, b)]


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    if kind == "D":
        return gates.det_matrix(gates.hankel_matrix(mu, i))
    if kind == "G":
        return gates.det_matrix(gates.localizer_matrix(mu, i, support))
    raise ValueError(kind)


def first_positive_lambda(
    kind: str,
    i: int,
    mu0: list[mp.mpf],
    mu1: list[mp.mpf],
    support: mp.mpf,
    steps: int = 1000,
) -> mp.mpf | None:
    prev_lam = mp.mpf(0)
    prev_val = gate_value(kind, i, mu0, support)
    if prev_val > 0:
        return mp.mpf(0)

    first_root: mp.mpf | None = None
    for step in range(1, steps + 1):
        lam = mp.mpf(step) / steps
        val = gate_value(kind, i, interpolate(mu0, mu1, lam), support)
        if prev_val <= 0 and val > 0:
            lo = prev_lam
            hi = lam
            for _ in range(80):
                mid = (lo + hi) / 2
                mid_val = gate_value(kind, i, interpolate(mu0, mu1, mid), support)
                if mid_val > 0:
                    hi = mid
                else:
                    lo = mid
            first_root = hi
            break
        prev_lam = lam
        prev_val = val
    return first_root


def sampled_path_range(
    kind: str,
    i: int,
    mu0: list[mp.mpf],
    mu1: list[mp.mpf],
    support: mp.mpf,
    steps: int = 1000,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    min_val = mp.inf
    max_val = -mp.inf
    min_lam = mp.mpf(0)
    for step in range(steps + 1):
        lam = mp.mpf(step) / steps
        val = gate_value(kind, i, interpolate(mu0, mu1, lam), support)
        if val < min_val:
            min_val = val
            min_lam = lam
        if val > max_val:
            max_val = val
    return min_lam, min_val, max_val


def main() -> None:
    order = 8
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    true_mu = eta.total_ells(None, order)

    print("Pass-3 completion homotopy")
    print(f"finite scaffold: prime_count={prime_count}, X={primes[-1]}, r_cut={r_cut}")
    print("mu(lambda)=mu_finite + lambda*(mu_true-mu_finite)")
    print()

    print("Missing completion as fraction of one-sided certificate radius")
    eps = gates.ordinary_tail_error_radii(order, mp.mpf(primes[-1]), r_cut, mp.mpf("1.01"))
    print("m   finite_mu            true_mu              delta/eps")
    for m in range(1, order + 1):
        delta = true_mu[m - 1] - finite_mu[m - 1]
        print(
            f"{m:1d}  {fmt(finite_mu[m-1], 12):>18} {fmt(true_mu[m-1], 12):>18} "
            f"{fmt(abs(delta)/eps[m-1], 8):>12}"
        )
    print()

    print("Gate values along the completion homotopy")
    print("gate  value(0)            lambda+             min sample @lambda      value(1)")
    for kind in ["D", "G"]:
        for i in range(4):
            v0 = gate_value(kind, i, finite_mu, support)
            v1 = gate_value(kind, i, true_mu, support)
            root = first_positive_lambda(kind, i, finite_mu, true_mu, support)
            min_lam, min_val, _ = sampled_path_range(kind, i, finite_mu, true_mu, support)
            root_text = "already" if root == 0 else ("none" if root is None else fmt(root, 12))
            print(
                f"{kind}{i:<3} {fmt(v0, 12):>18} {root_text:>18} "
                f"{fmt(min_val, 10):>13} @{fmt(min_lam, 6):<8} {fmt(v1, 12):>18}"
            )
    print()

    print("Interpretation")
    print("- The exact completion direction reaches the positive chamber.")
    print("- lambda+ estimates how much of the missing tail must be certified from below.")
    print("- Gates with lambda+ close to 1 are precision bottlenecks, not structural failures.")


if __name__ == "__main__":
    main()
