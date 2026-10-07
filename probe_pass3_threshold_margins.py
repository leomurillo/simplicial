"""Threshold-margin probe for the Pass-3 gate ladder.

Once lower rungs are fixed, each gate is affine in its top moment:

    D_i = D_{i-1} (mu_{2i+1} - theta_i^D),
    G_i = G_{i-1} (theta_i^G - mu_{2i+2}).

Therefore the exact positive margin past threshold is

    mu_{2i+1} - theta_i^D = D_i / D_{i-1},
    theta_i^G - mu_{2i+2} = G_i / G_{i-1}.

This probe computes those margins for the completed ledger and compares
them to the hybrid-to-true correction still needed at each top rung.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_sensitivity_jacobian as sens
import probe_pass3_gate_stability_intervals as gates
import probe_pass3_top_rung_thresholds as thresh


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    if kind == "D":
        return gates.det_matrix(gates.hankel_matrix(mu, i))
    if kind == "G":
        return gates.det_matrix(gates.localizer_matrix(mu, i, support))
    raise ValueError(kind)


def main() -> None:
    order = 8
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)
    _, hybrid_mu, true_mu, x = sens.build_hybrid_mu(order)

    d = [gate_value("D", i, true_mu, support) for i in range(4)]
    g = [gate_value("G", i, true_mu, support) for i in range(4)]
    d_prev = [mp.mpf(1)] + d[:-1]
    g_prev = [mp.mpf(1)] + g[:-1]

    print("Pass-3 threshold margins")
    print(f"hybrid scaffold X={x}, support gamma_1^-2={fmt(support, 18)}")
    print()

    print("Hankel margins: mu_{2i+1} - theta_i^D = D_i/D_{i-1}")
    print("gate top  threshold          true top           margin             needed correction  margin/needed")
    for i in range(4):
        top_one, _, _, threshold = thresh.threshold_for_top_moment("D", i, true_mu, support)
        true_top = true_mu[top_one - 1]
        hybrid_top = hybrid_mu[top_one - 1]
        needed = true_top - hybrid_top
        margin = true_top - threshold
        ratio = margin / abs(needed) if needed else mp.inf
        identity = d[i] / d_prev[i]
        print(
            f"D{i:<2} mu{top_one:<2} {fmt(threshold, 14):>18} "
            f"{fmt(true_top, 14):>18} {fmt(margin, 14):>18} "
            f"{fmt(needed, 12):>18} {fmt(ratio, 8):>14}"
        )
        print(f"     identity D_i/D_(i-1) = {fmt(identity, 14)}")
    print()

    print("Localizer margins: theta_i^G - mu_{2i+2} = G_i/G_{i-1}")
    print("gate top  threshold          true top           margin             needed correction  margin/needed")
    for i in range(4):
        top_one, _, _, threshold = thresh.threshold_for_top_moment("G", i, true_mu, support)
        true_top = true_mu[top_one - 1]
        hybrid_top = hybrid_mu[top_one - 1]
        needed = hybrid_top - true_top
        margin = threshold - true_top
        ratio = margin / abs(needed) if needed else mp.inf
        identity = g[i] / g_prev[i]
        print(
            f"G{i:<2} mu{top_one:<2} {fmt(threshold, 14):>18} "
            f"{fmt(true_top, 14):>18} {fmt(margin, 14):>18} "
            f"{fmt(needed, 12):>18} {fmt(ratio, 8):>14}"
        )
        print(f"     identity G_i/G_(i-1) = {fmt(identity, 14)}")

    print()
    print("Interpretation")
    print("- The threshold margins are exactly adjacent determinant ratios.")
    print("- The margin/needed column shows how close to exact completion the top rung must be.")
    print("- Higher rungs require preserving extremely small positive residues after huge correction.")


if __name__ == "__main__":
    main()
