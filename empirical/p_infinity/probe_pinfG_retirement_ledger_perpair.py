"""probe_pinfG_retirement_ledger_perpair.py -- ADDENDUM to the retirement-ledger probe:
the per-pair predicted rates for the exact crossing-ensemble design, from the three
models fitted on archived data (pinfG_retirement_ledger.npz). Locked BEFORE the
ensemble returns; no free parameters here -- pure readout of the registered fits.

Also prints the low-subset (g4/g5/g6 + gapA/gapB analogue) aggregate, comparable to the
fixed-N instrument's measured D = +0.0118 at those heights, and the blur diagnostic
(local zero spacing in ln lambda^2 vs the transition width w = 0.30).
"""
import sys
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

z = np.load(HERE + "pinfG_retirement_ledger.npz")
A1, An, ce = float(z["A_1rad"]), float(z["A_nyq"]), float(z["c_env"])

mp.mp.dps = 20
gam = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, 121)])
W = 0.30


def ledger_lnR_part(l2, tau, A):
    lx = np.log(l2)
    S = 1.0 / (1.0 + np.exp(-np.clip((lx - np.log(tau * gam)) / W, -60, 60)))
    return -A * (S / gam).sum()


PAIRS = [
    ("g4", 29.62, 31.22, 1), ("g5", 32.14, 33.74, 1), ("g6", 36.79, 38.39, 1),
    ("g7", 40.12, 41.72, 1), ("g8", 42.53, 44.13, 1), ("g11", 52.17, 53.77, 1),
    ("g12", 55.65, 57.25, 1), ("g17", 68.75, 70.35, 1),
    ("g9+10", 47.19, 50.59, 2), ("g13+14", 58.39, 61.79, 2), ("g15+16", 64.40, 67.80, 2),
    ("gapA", 44.50, 46.90, 0), ("gapB", 54.00, 55.60, 0),
    ("gapC", 62.00, 63.60, 0), ("gapD", 73.00, 74.60, 0),
]

print("== per-pair predicted rates (locked): tag | T-1rad | T-Nyq | envelope | label ==")
rows = {}
for name, a, b, nz in PAIRS:
    r1 = -(ledger_lnR_part(b, 1.0, A1) - ledger_lnR_part(a, 1.0, A1)) / (b - a)
    rn = -(ledger_lnR_part(b, 1 / np.pi, An) - ledger_lnR_part(a, 1 / np.pi, An)) / (b - a)
    re = ce * 0.25 * (np.log(b) ** 2 - np.log(a) ** 2) / (b - a)
    rows[name] = (r1, rn, re, nz)
    print(f"   {name:7s}  {r1:+.4f}  {rn:+.4f}  {re:+.4f}   "
          f"{'crossing' if nz else 'gap'}")

low_c = [rows[t][0] for t in ("g4", "g5", "g6")]
print(f"\n   low-subset T-1rad crossing mean (g4/g5/g6): {np.mean(low_c):+.4f}"
      f"   [fixed-N measured crossing mean at these: +0.0195, gaps +0.0077]")

print("\n== blur diagnostic: local zero spacing in ln(lambda^2) vs w = 0.30 ==")
for j in (3, 4, 5, 7, 10, 13, 16, 19):
    dln = np.log(gam[j + 1]) - np.log(gam[j])
    print(f"   gamma_{j+1}={gam[j]:7.3f} -> gamma_{j+2}: spacing {dln:.3f} "
          f"{'BLURRED (< w)' if dln < W else 'resolved'}")
