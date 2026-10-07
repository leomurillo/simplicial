"""Top-rung threshold probe for Pass-3 gates.

Each local determinant gate is affine in its top moment:

    D_i = det[mu_{a+b+1}] uses top moment mu_{2i+1}
    G_i = det[rho mu_{a+b+1} - mu_{a+b+2}] uses top moment mu_{2i+2}.

Holding lower moments fixed, there is therefore an exact threshold for the
top rung.  This probe computes those thresholds using the true completed
lower prefix and compares the hybrid and true top moments against them.

This turns the correlated gate problem into a rung-by-rung target.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_sensitivity_jacobian as sens
import probe_pass3_gate_stability_intervals as gates


mp.mp.dps = 90


def fmt(x: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(x, digits)


def gate_value(kind: str, i: int, mu: list[mp.mpf], support: mp.mpf) -> mp.mpf:
    if kind == "D":
        return gates.det_matrix(gates.hankel_matrix(mu, i))
    if kind == "G":
        return gates.det_matrix(gates.localizer_matrix(mu, i, support))
    raise ValueError(kind)


def threshold_for_top_moment(
    kind: str, i: int, lower_prefix: list[mp.mpf], support: mp.mpf
) -> tuple[int, mp.mpf, mp.mpf, mp.mpf]:
    """Return (top one-based moment index, slope, intercept, threshold)."""
    top_zero = 2 * i if kind == "D" else 2 * i + 1
    top_one = top_zero + 1
    needed_len = top_zero + 1
    base = list(lower_prefix[:needed_len])
    base[top_zero] = mp.mpf(0)
    plus = list(base)
    plus[top_zero] = mp.mpf(1)
    intercept = gate_value(kind, i, base, support)
    slope = gate_value(kind, i, plus, support) - intercept
    threshold = -intercept / slope
    return top_one, slope, intercept, threshold


def verdict(kind: str, slope: mp.mpf, top_value: mp.mpf, threshold: mp.mpf) -> str:
    value = slope * (top_value - threshold)
    if value > 0:
        return "passes"
    if value < 0:
        return "fails"
    return "on-threshold"


def main() -> None:
    order = 8
    gamma1 = mp.im(mp.zetazero(1))
    support = 1 / (gamma1 * gamma1)

    _, hybrid_mu, true_mu, x = sens.build_hybrid_mu(order)

    print("Pass-3 top-rung gate thresholds")
    print(f"lower prefix: true completed ledger, hybrid scaffold X={x}")
    print(f"support rho=gamma_1^-2={fmt(support, 18)}")
    print()

    print("gate top  slope              threshold          hybrid top        true top          lambda-to-threshold")
    for kind in ["D", "G"]:
        for i in range(4):
            top_one, slope, intercept, threshold = threshold_for_top_moment(
                kind, i, true_mu, support
            )
            hybrid_top = hybrid_mu[top_one - 1]
            true_top = true_mu[top_one - 1]
            lam = (threshold - hybrid_top) / (true_top - hybrid_top)
            print(
                f"{kind}{i:<2} mu{top_one:<2} {fmt(slope, 12):>18} "
                f"{fmt(threshold, 14):>18} {fmt(hybrid_top, 14):>18} "
                f"{fmt(true_top, 14):>18} {fmt(lam, 12):>18}"
            )

    print()
    print("Gate values reconstructed from top-rung affine formula")
    print("gate  hybrid verdict   true verdict     true gate")
    for kind in ["D", "G"]:
        for i in range(4):
            top_one, slope, _, threshold = threshold_for_top_moment(kind, i, true_mu, support)
            h = verdict(kind, slope, hybrid_mu[top_one - 1], threshold)
            t = verdict(kind, slope, true_mu[top_one - 1], threshold)
            tv = gate_value(kind, i, true_mu, support)
            print(f"{kind}{i:<3} {h:>14} {t:>14} {fmt(tv, 12):>18}")

    print()
    print("Interpretation")
    print("- Each gate has an exact top-rung threshold once lower rungs are certified.")
    print("- lambda-to-threshold tells how much of the hybrid-to-true top correction is needed.")
    print("- The proof can proceed inductively: certify lower gates, then certify the next top rung.")


if __name__ == "__main__":
    main()
