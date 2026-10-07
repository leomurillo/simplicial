"""T5 dual-gauge reading of the Pass-3 gate ladder.

T5 says that ratio/reciprocal observables should be read in the harmonic
dual gauge.  The Pass-3 threshold margins are adjacent determinant ratios:

    D_i/D_{i-1},  G_i/G_{i-1}.

This probe records their logarithms.  The log-ratio ledger is the stable
coordinate system for the ultra-thin positive residues.
"""

from __future__ import annotations

import mpmath as mp

import probe_pass3_eta_total_hankel_gates as eta
import probe_pass3_gate_stability_intervals as gates


mp.mp.dps = 80


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
    mu = eta.total_ells(None, order)

    d = [gate_value("D", i, mu, support) for i in range(4)]
    g = [gate_value("G", i, mu, support) for i in range(4)]
    d_prev = [mp.mpf(1)] + d[:-1]
    g_prev = [mp.mpf(1)] + g[:-1]

    print("Pass-3 T5 dual gate ledger")
    print(f"support gamma_1^-2={fmt(support, 18)}")
    print()
    print("Hankel odd/top-rung margins")
    print("i   D_i/D_{i-1}          log ratio")
    for i in range(4):
        ratio = d[i] / d_prev[i]
        print(f"{i:1d}  {fmt(ratio, 16):>20} {fmt(mp.log(ratio), 16):>20}")
    print()
    print("Localizer even/top-rung margins")
    print("i   G_i/G_{i-1}          log ratio")
    for i in range(4):
        ratio = g[i] / g_prev[i]
        print(f"{i:1d}  {fmt(ratio, 16):>20} {fmt(mp.log(ratio), 16):>20}")
    print()
    print("Interpretation")
    print("- The tiny positive residues become additive log-ratio rungs.")
    print("- T5 supplies the right language: direct ratio certification is harmonic gauge work.")


if __name__ == "__main__":
    main()
