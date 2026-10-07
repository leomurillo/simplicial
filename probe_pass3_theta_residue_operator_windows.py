"""Operator path for partial theta-residue completion.

Start from the PNT-completed r=3 ledger.  Then add the actual theta
fluctuation over a finite window [X,Y]:

    dtheta - dt on [X,Y],

leaving PNT density beyond Y.  This produces a path of ledgers:

    finite + PNT tail beyond X + exact theta residue on [X,Y].

The previous window probe showed that early windows can point opposite to
the total oracle residue.  This probe asks what that does to the determinant
gates and GNS/Jacobi construction.
"""

from __future__ import annotations

from math import factorial, log

import importlib.util
from pathlib import Path

import mpmath as mp
from sympy import primerange

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_pnt_r3_completion_operator as pnt
from probe_pass3_tail_control_bounds import integral_tail_power_log


mp.mp.dps = 90

GNS_PATH = Path(__file__).with_name("probe_pass3_gns_helmert_square_operator.py")
spec = importlib.util.spec_from_file_location("gns_probe", GNS_PATH)
gns = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(gns)
gns.mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 10) -> str:
    return mp.nstr(x, digits)


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    if kind == "D":
        return gates.det_matrix(gates.hankel_matrix(mu, i))
    if kind == "G":
        return gates.det_matrix(gates.localizer_matrix(mu, i, support))
    raise ValueError(kind)


def gns_status(mu: list[mp.mpf], n: int, support: mp.mpf) -> str:
    try:
        jmat = gns.jacobi_from_moments(mu, n)
    except ValueError as exc:
        msg = str(exc)
        if "degree" in msg:
            return "fail " + msg.split(":")[0].replace("nonpositive norm at ", "")
        return "fail"
    vals = mp.eigsy(jmat, eigvals_only=True)
    if min(vals) >= 0 and max(vals) <= support:
        return "positive bounded"
    return f"spectrum [{fmt(min(vals), 4)}, {fmt(max(vals), 4)}]"


def residue_scales(order: int) -> list[mp.mpf]:
    scales = []
    for m in range(1, order + 1):
        k = 2 * m
        scales.append(((-1) ** (m + 1)) * (mp.mpf(m) / factorial(k)) * (mp.mpf(3) ** (k - 1)))
    return scales


def main() -> None:
    order = 8
    n = 4
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    multipliers = [2, 5, 10, 20, 50]

    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)
    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    x = primes[-1]
    x_mpf = mp.mpf(x)
    pnt_mu = [finite_mu[m - 1] + pnt.pnt_r3_missing_ell(m, x_mpf) for m in range(1, order + 1)]
    true_mu = eta.total_ells(None, order)

    milestones = {int(x * mult): mult for mult in multipliers}
    max_y = max(milestones)
    raw_prime_sums = [0.0 for _ in range(order)]
    scales = residue_scales(order)

    print("Pass-3 theta-residue operator windows")
    print(f"X={x}, maxY={max_y}")
    print("Ledger: PNT-completed plus exact dtheta-dt over [X,Y].")
    print()
    print("Y/X   D0          D1          G0          G1          GNS")

    sorted_milestones = sorted(milestones)
    next_idx = 0
    for prime in primerange(x + 1, max_y + 1):
        lp = log(prime)
        base = prime ** -1.5
        for m in range(1, order + 1):
            raw_prime_sums[m - 1] += (lp ** (2 * m)) * base

        while next_idx < len(sorted_milestones) and prime >= sorted_milestones[next_idx]:
            y = sorted_milestones[next_idx]
            residue = []
            for m in range(1, order + 1):
                j = 2 * m - 1
                integral = integral_tail_power_log(mp.mpf("1.5"), j, x_mpf) - integral_tail_power_log(
                    mp.mpf("1.5"), j, mp.mpf(y)
                )
                residue.append(scales[m - 1] * (mp.mpf(raw_prime_sums[m - 1]) - integral))
            mu = [pnt_mu[i] + residue[i] for i in range(order)]
            print(
                f"{milestones[y]:>3} "
                f"{fmt(gate_value('D',0,mu,support), 8):>11} "
                f"{fmt(gate_value('D',1,mu,support), 8):>11} "
                f"{fmt(gate_value('G',0,mu,support), 8):>11} "
                f"{fmt(gate_value('G',1,mu,support), 8):>11} "
                f"{gns_status(mu,n,support)}"
            )
            next_idx += 1

    while next_idx < len(sorted_milestones):
        y = sorted_milestones[next_idx]
        residue = []
        for m in range(1, order + 1):
            j = 2 * m - 1
            integral = integral_tail_power_log(mp.mpf("1.5"), j, x_mpf) - integral_tail_power_log(
                mp.mpf("1.5"), j, mp.mpf(y)
            )
            residue.append(scales[m - 1] * (mp.mpf(raw_prime_sums[m - 1]) - integral))
        mu = [pnt_mu[i] + residue[i] for i in range(order)]
        print(
            f"{milestones[y]:>3} "
            f"{fmt(gate_value('D',0,mu,support), 8):>11} "
            f"{fmt(gate_value('D',1,mu,support), 8):>11} "
            f"{fmt(gate_value('G',0,mu,support), 8):>11} "
            f"{fmt(gate_value('G',1,mu,support), 8):>11} "
            f"{gns_status(mu,n,support)}"
        )
        next_idx += 1

    print()
    print("Reference")
    print(
        f"PNT "
        f"{fmt(gate_value('D',0,pnt_mu,support),8):>11} "
        f"{fmt(gate_value('D',1,pnt_mu,support),8):>11} "
        f"{fmt(gate_value('G',0,pnt_mu,support),8):>11} "
        f"{fmt(gate_value('G',1,pnt_mu,support),8):>11} "
        f"{gns_status(pnt_mu,n,support)}"
    )
    print(
        f"true"
        f"{fmt(gate_value('D',0,true_mu,support),8):>10} "
        f"{fmt(gate_value('D',1,true_mu,support),8):>11} "
        f"{fmt(gate_value('G',0,true_mu,support),8):>11} "
        f"{fmt(gate_value('G',1,true_mu,support),8):>11} "
        f"{gns_status(true_mu,n,support)}"
    )


if __name__ == "__main__":
    main()
