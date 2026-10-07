"""probe_pinfG_fixedN_steps.py -- the per-zero step test, SAWTOOTH-FREE (the corrected
instrument registered in P-inf-G section 15's multicrossing addendum).

DESIGN.  Each local comparison uses TWO windows built at the SAME N (killing the
N-rounding bandwidth sawtooth that swamped the multicrossing run): three crossing pairs
centered on gamma_4 = 30.42, gamma_5 = 32.94, gamma_6 = 37.59 (span Delta lam^2 = 2.4)
and two gap-control pairs centered between crossings (same span).  N per pair =
round(17.312 * ln(center)).

PRE-REGISTERED:
  FX1 (validity): PSD + positive pivots at dps 160; same-N within each pair by
      construction (logged).
  FX2 (THE TEST): mean crossing rate >= 2 x mean gap rate (3 vs 2 pairs, each
      internally sawtooth-free) -> staircase CONFIRMED with a clean instrument;
      comparable rates -> smooth envelope (clean negative this time).
  FX3 (the depth law): delta_j = (rate_cross - mean gap rate) x 2.4 per crossing;
      delta_j * gamma_j reported against the section-15.4 band [3, 10]; the q-exponent
      read from the three crossings (delta ~ 1/gamma^(q-?) discrimination seed).
Pairs (lam^2): g4: (29.22, 31.62); g5: (31.74, 34.14); g6: (36.39, 38.79);
gaps: (34.05, 36.45), (38.05, 40.45).  dps 160.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

PAIRS = [
    ("g4", 30.42, 29.22, 31.62),
    ("g5", 32.94, 31.74, 34.14),
    ("g6", 37.59, 36.39, 38.79),
    ("gapA", None, 34.05, 36.45),
    ("gapB", None, 38.05, 40.45),
]
mp.mp.dps = 160

print("== fixed-N per-zero step test (dps=160) ==\n")
OUT = {}
for tag, gam, a, b in PAIRS:
    center = (a + b) / 2
    N = int(round(float(24 / (2 * mp.log(2)) * mp.log(mp.mpf(repr(center))))))
    res = {}
    for l2 in (a, b):
        t0 = time.time()
        lam = mp.sqrt(mp.mpf(repr(l2)))
        Q, _, _ = build_QW_mode(lam, N, "true")
        K = to_point(Q, N)
        dim = 2 * N + 1
        psd = cholesky_psd(K)
        d0 = direct_pivot(K, dim, "seam")
        res[l2] = dict(R=float(d0 / K[0, 0]), psd=psd)
        print(f"   [{tag}] lam^2={l2:<6} (N={N}, dim={dim}, {time.time()-t0:.0f}s): "
              f"PSD={'OK' if psd else 'FAIL'}  R_seam={res[l2]['R']:.5f}")
    rate = -np.log(res[b]["R"] / res[a]["R"]) / (b - a)
    OUT[tag] = dict(rate=rate, gam=gam, res=res, N=N)
    print(f"   [{tag}] same-N rate = {rate:+.4f} per unit lam^2"
          + (f"   (crossing gamma = {gam})" if gam else "   (gap control)"))

fx1 = all(all(r["psd"] for r in OUT[t]["res"].values()) for t in OUT)
print("\n   FX1: " + ("SURVIVES" if fx1 else "FIRED"))

print("\n== FX2/FX3 ==")
rc = [OUT[t]["rate"] for t in ("g4", "g5", "g6")]
rg = [OUT[t]["rate"] for t in ("gapA", "gapB")]
mc, mg = np.mean(rc), np.mean(rg)
print(f"   crossing rates: {[f'{r:+.4f}' for r in rc]}   mean {mc:+.4f}")
print(f"   gap rates:      {[f'{r:+.4f}' for r in rg]}   mean {mg:+.4f}")
if mg <= 0:
    print("   gap mean <= 0 (plateau): " + ("STAIRCASE CONFIRMED (crossings eat, gaps don't)"
          if mc > 0.02 else "both flat -- report"))
elif mc >= 2 * mg:
    print(f"   ratio = {mc/mg:.1f} >= 2  ->  STAIRCASE CONFIRMED (clean instrument)")
else:
    print(f"   ratio = {mc/mg:.1f} < 2  ->  smooth envelope (clean negative)")
for t in ("g4", "g5", "g6"):
    d = (OUT[t]["rate"] - mg) * 2.4
    print(f"   {t}: delta_j = {d:+.4f}   delta_j*gamma_j = {d*OUT[t]['gam']:+.2f}   [band 3-10]")

np.savez(HERE + "pinfG_fixedN_steps.npz",
         tags=np.array([t for t, *_ in PAIRS]),
         rates=np.array([OUT[t]["rate"] for t, *_ in PAIRS]))
print("\nARCHIVED: pinfG_fixedN_steps.npz")
