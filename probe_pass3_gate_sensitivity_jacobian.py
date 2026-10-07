"""Gate sensitivity/Jacobian probe for correlated completion.

After the hybrid split, the m=1 completion is certifiable, but the gates
remain outside the positive chamber.  The remaining problem is correlated
control of moments m>=2.

This probe computes exact determinant gradients with respect to the moment
coordinates mu_j by cofactors.  It then decomposes the hybrid-to-true
completion correction into gate contributions:

    delta gate ~= sum_j (d gate / d mu_j) delta mu_j.

The goal is diagnostic: identify which moment directions dominate each
thin gate and measure how much cancellation the determinant requires.
"""

from __future__ import annotations

from math import factorial, log

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_hybrid_r3_completion_split as hybrid


mp.mp.dps = 80


def fmt(x: mp.mpf, digits: int = 10) -> str:
    return mp.nstr(x, digits)


def minor_matrix(mat: list[list[mp.mpf]], row_skip: int, col_skip: int) -> list[list[mp.mpf]]:
    return [
        [value for c, value in enumerate(row) if c != col_skip]
        for r, row in enumerate(mat)
        if r != row_skip
    ]


def cofactor_matrix(mat: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    n = len(mat)
    if n == 1:
        return [[mp.mpf(1)]]
    cof = [[mp.mpf(0) for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            cof[r][c] = ((-1) ** (r + c)) * gates.det_matrix(minor_matrix(mat, r, c))
    return cof


def gate_matrix(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> list[list[mp.mpf]]:
    if kind == "D":
        return gates.hankel_matrix(mu, i)
    if kind == "G":
        return gates.localizer_matrix(mu, i, support)
    raise ValueError(kind)


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    return gates.det_matrix(gate_matrix(kind, i, mu, support))


def gate_gradient(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> list[mp.mpf]:
    mat = gate_matrix(kind, i, mu, support)
    cof = cofactor_matrix(mat)
    n = len(mat)
    needed = 2 * i + 1 if kind == "D" else 2 * i + 2
    grad = [mp.mpf(0) for _ in range(needed)]
    for a in range(n):
        for b in range(n):
            # d det / d A_ab = cofactor_ab
            c = cof[a][b]
            if kind == "D":
                grad[a + b] += c
            else:
                grad[a + b] += support * c
                grad[a + b + 1] -= c
    return grad


def build_hybrid_mu(order: int) -> tuple[list[mp.mpf], list[mp.mpf], list[mp.mpf], int]:
    prime_count = 30000
    r_cut = 64
    mobius_cutoff = 60
    zero_count = 100

    zeros = hybrid.ef.zero_list(zero_count)
    finite_mu, primes = gates.finite_scaffold_mu(order, prime_count, r_cut, mobius_cutoff)
    finite_r3 = gates.fast_direct_tail_ells(primes, 3, 3, order)

    hybrid_r3_full = [
        hybrid.hybrid_r3_layer_ell(m, zeros, mobius_cutoff) for m in range(1, order + 1)
    ]
    hybrid_mu = [
        finite_mu[m - 1] + hybrid_r3_full[m - 1] - finite_r3[m - 1]
        for m in range(1, order + 1)
    ]
    true_mu = eta.total_ells(None, order)
    return finite_mu, hybrid_mu, true_mu, primes[-1]


def contribution_summary(
    grad: list[mp.mpf], delta: list[mp.mpf], limit: int = 4
) -> tuple[mp.mpf, mp.mpf, list[tuple[int, mp.mpf]]]:
    terms = [grad[j] * delta[j] for j in range(len(grad))]
    linear = mp.fsum(terms)
    l1 = mp.fsum(abs(t) for t in terms)
    ranked = sorted(enumerate(terms, start=1), key=lambda row: abs(row[1]), reverse=True)
    return linear, l1, ranked[:limit]


def main() -> None:
    order = 8
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)
    finite_mu, hybrid_mu, true_mu, x = build_hybrid_mu(order)
    delta = [true_mu[i] - hybrid_mu[i] for i in range(order)]

    print("Pass-3 gate sensitivity Jacobian")
    print(f"hybrid scaffold: X={x}, support gamma_1^-2={fmt(support, 18)}")
    print("delta = true completed ledger - hybrid completed ledger")
    print()

    print("Remaining hybrid-to-true moment correction")
    print("m   hybrid_mu            true_mu              delta")
    for m in range(1, order + 1):
        print(
            f"{m:1d}  {fmt(hybrid_mu[m-1], 12):>18} "
            f"{fmt(true_mu[m-1], 12):>18} {fmt(delta[m-1], 12):>18}"
        )
    print()

    print("Gate Jacobian contribution at the true completed ledger")
    print("gate  hybrid gate        true gate          linear delta      L1/|linear|   top terms")
    for kind in ["D", "G"]:
        for i in range(4):
            needed = 2 * i + 1 if kind == "D" else 2 * i + 2
            grad = gate_gradient(kind, i, true_mu, support)
            linear, l1, top = contribution_summary(grad, delta[:needed])
            hval = gate_value(kind, i, hybrid_mu, support)
            tval = gate_value(kind, i, true_mu, support)
            ratio = l1 / max(abs(linear), mp.mpf("1e-80"))
            top_text = ", ".join(f"m{idx}:{fmt(val, 4)}" for idx, val in top)
            print(
                f"{kind}{i:<3} {fmt(hval, 10):>16} {fmt(tval, 10):>16} "
                f"{fmt(linear, 10):>16} {fmt(ratio, 8):>12}   {top_text}"
            )

    print()
    print("Interpretation")
    print("- L1/|linear| measures cancellation among moment directions.")
    print("- Large ratios mean the gate requires correlated moment control, not scalar boxes.")
    print("- The top terms identify which cumulant rungs drive each gate.")


if __name__ == "__main__":
    main()
