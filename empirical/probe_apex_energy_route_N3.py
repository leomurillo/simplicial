#!/usr/bin/env python3
r"""N3 no-crossing via the ENERGY ROUTE -- verdict: total fails, cluster works (sharply).

Goal: bound the leading-straggler displacement delta_max(N) below 1/8 (the half-gap
between adjacent clusters) using displacement-energy functionals, to prove the
spectral-concentration / multiplicity law.

KEY ARITHMETIC. For an eigenvalue lambda near cluster i^c with displacement delta
(in turns), 1 - Re(lambda^4) = 1 - cos(8 pi delta) >= 0, increasing on
delta in [0, 1/8] up to the value 2 at delta = 1/8. Hence, for any nonneg
energy bound E with  1 - cos(8 pi delta_max) <= E:

        E < 2   ==>   delta_max < arccos(1 - E)/(8 pi) < 1/8   (NO-CROSSING).

So a uniform energy bound E* < 2 closes the no-crossing (and gives the explicit
straggler limit delta_inf <= arccos(1-E*)/(8 pi)).

TWO functionals:
  - TOTAL energy  E_tot(N) = (N-1) - Re tr(U_N^4) = sum_i (1 - cos 8 pi delta_i).
    FAILS: E_tot -> ~3.3 > 2, because it sums BOTH stragglers (near +1 and near
    -i). The single-straggler bound 1-cos(8 pi delta_max) <= E_tot is vacuous.
  - CLUSTER-PROJECTED energy  E^(r)(N) = sum_{c_i = r} (1 - cos 8 pi delta_i),
    r in {0,1,2,3} (clusters 1,i,-1,-i). Each cluster contains ONE straggler;
    max_r E^(r) -> ~1.76 < 2, and the bound delta_max <= arccos(1-max_r E^(r))/
    (8 pi) is essentially SHARP (matches delta_max to ~1e-4).

VERDICT (honest). The cluster-projected route is VIABLE and reduces the no-crossing
to the inequality  max_r E^(r)(N) < 2  -- an explicit combination of the power
traces tr((HF)^k), k <= 8 (via the order-4 cluster projector). But E^(r) is
DOMINATED by its single straggler, so the inequality is essentially EQUIVALENT to
the straggler bound it was meant to replace: the energy route reformulates the
problem as an aggregate-trace inequality (a more tractable analytic FORM, opening
explicit tr((HF)^k) tools) WITHOUT independently lowering its difficulty. It does
NOT, by itself, close the theorem.

This script certifies the verdict: (a) E_tot exceeds 2 (route fails), (b) max
cluster energy stays < 2 with the bound sharp on delta_max, for N up to 4096.
"""

from __future__ import annotations

import json

import numpy as np


def U_block(N):
    w = np.exp(2j * np.pi / np.float64(N))
    j = np.arange(N)
    F = w ** np.outer(j, j) / np.sqrt(N)
    H = np.zeros((N, N))
    H[0, :] = 1 / np.sqrt(N)
    for k in range(1, N):
        H[k, :k] = 1.0
        H[k, k] = -k
        H[k] /= np.sqrt(k * (k + 1))
    return (H @ F.T)[1:, 1:]


def energies(N):
    ev = np.linalg.eigvals(U_block(N))
    roots = [1, 1j, -1, -1j]
    Ecl = [0.0, 0.0, 0.0, 0.0]
    dmax = 0.0
    for e in ev:
        c = int(np.argmin([abs(e - r) for r in roots]))
        d = abs(np.angle(e / roots[c])) / (2 * np.pi)
        Ecl[c] += 1 - np.cos(8 * np.pi * d)
        dmax = max(dmax, d)
    return sum(Ecl), Ecl, dmax


def main():
    report = {"probe": "apex_energy_route_N3", "threshold": 2.0}
    rows = []
    total_exceeds_2 = False
    cluster_under_2 = True
    bound_sharp = True

    for N in [16, 64, 256, 1024, 2048, 4096]:
        Etot, Ecl, dmax = energies(N)
        mc = max(Ecl)
        if Etot >= 2.0:
            total_exceeds_2 = True
        if mc >= 2.0:
            cluster_under_2 = False
        bound = float(np.arccos(max(-1.0, 1 - mc)) / (8 * np.pi)) if mc < 2 else float("nan")
        if abs(bound - dmax) > 1e-3:
            bound_sharp = False
        rows.append({"N": N, "E_total": round(Etot, 4),
                     "E_cluster": [round(x, 4) for x in Ecl],
                     "max_cluster_E": round(mc, 4),
                     "delta_max": round(dmax, 5),
                     "bound_from_cluster_E": round(bound, 5),
                     "bound_sharp": bool(abs(bound - dmax) < 1e-3)})

    report["rows"] = rows
    report["total_energy_exceeds_2 (total route FAILS)"] = bool(total_exceeds_2)
    report["max_cluster_energy_under_2 (cluster route viable)"] = bool(cluster_under_2)
    report["cluster_bound_sharp_on_delta_max"] = bool(bound_sharp)
    report["delta_inf_estimate"] = round(rows[-1]["bound_from_cluster_E"], 4)
    report["PASS"] = bool(total_exceeds_2 and cluster_under_2 and bound_sharp)

    print(json.dumps(report, indent=2))
    print("\n=== ENERGY-ROUTE VERDICT CERTIFICATE ===")
    print(f"{'N':>5} | {'E_total':>8} | {'max E^(r)':>9} | {'delta_max':>9} | {'bound(E^r)':>10} | sharp?")
    print("-" * 70)
    for r in rows:
        print(f"{r['N']:>5} | {r['E_total']:>8.4f} | {r['max_cluster_E']:>9.4f} |"
              f" {r['delta_max']:>9.5f} | {r['bound_from_cluster_E']:>10.5f} | {r['bound_sharp']}")
    print(f"\nTotal energy -> exceeds 2 (lumps both stragglers): naive route FAILS.")
    print(f"Max cluster energy -> ~1.76 < 2; bound on delta_max is SHARP "
          f"(delta_inf ~ {report['delta_inf_estimate']} < 1/8 = 0.125).")
    print("Reduces no-crossing to: max_r E^(r)(N) < 2, a tr((HF)^k) inequality "
          "(k<=8) -- straggler-dominated, so a reformulation, not an independent proof.")
    print(f"PASS = {report['PASS']}")
    return 0 if report["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
