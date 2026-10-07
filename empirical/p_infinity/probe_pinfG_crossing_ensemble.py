"""probe_pinfG_crossing_ensemble.py -- THE ENSEMBLE TEST: 11 crossings + 4 gap controls,
same-N pairs (sawtooth-free), gamma_4 .. gamma_20.

Decides, with ensemble statistics (the per-pair wiggle sigma ~ 0.06 averages down by
sqrt(n)): (a) the staircase's existence at >= 2 s.e. (the three prior ratio-2.5 firings
were each sub-1-sigma); (b) T-1rad vs T-Nyq (PREREG addendum 2: under T-Nyq the high
crossings show NOTHING); (c) the depth law delta_j gamma_j (q-exponent seed).

PRE-REGISTERED (locked):
  E1: per-window PSD at the scheduled dps (160 for lam^2 <= 55, 190 above); starved
      windows dropped and reported (the ensemble tolerates losses).
  E2 (THE TEST, with teeth this time): D = mean(crossing rates) - mean(gap rates);
      s.e. from ensemble scatter (s_c^2/n_c + s_g^2/n_g)^(1/2).
      D >= 2 s.e. -> STAIRCASE ESTABLISHED (T-1rad); |D| < 1 s.e. -> T-Nyq gains
      decisively (high crossings silent); between -> report, extend ensemble.
  E3: delta_j gamma_j per crossing (doubles weighted per zero); the [3,10] band score.
  E4: the envelope extended to lam^2 = 77.9.
Design: singles (span +-0.8) at gamma_4,5,6,7,8,11,12,17; doubles (span +-1.7) at
(g9+g10), (g13+g14), (g15+g16); gaps (44.5,46.9), (54.0,55.6), (62.0,63.6), (73.0,74.6).
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
    ("g4", 30.4249, 29.62, 31.22, 1), ("g5", 32.9351, 32.14, 33.74, 1),
    ("g6", 37.5862, 36.79, 38.39, 1), ("g7", 40.9187, 40.12, 41.72, 1),
    ("g8", 43.3271, 42.53, 44.13, 1), ("g11", 52.9703, 52.17, 53.77, 1),
    ("g12", 56.4462, 55.65, 57.25, 1), ("g17", 69.5464, 68.75, 70.35, 1),
    ("g9+10", 48.8895, 47.19, 50.59, 2), ("g13+14", 60.0894, 58.39, 61.79, 2),
    ("g15+16", 66.0962, 64.40, 67.80, 2),
    ("gapA", None, 44.50, 46.90, 0), ("gapB", None, 54.00, 55.60, 0),
    ("gapC", None, 62.00, 63.60, 0), ("gapD", None, 73.00, 74.60, 0),
]

print("== the crossing ensemble: gamma_4..gamma_20 (same-N pairs) ==\n")
OUT = {}
for tag, gam, a, b, nz in PAIRS:
    center = (a + b) / 2
    dps = 160 if center <= 55 else 190
    mp.mp.dps = dps
    N = int(round(float(24 / (2 * mp.log(2)) * mp.log(mp.mpf(repr(center))))))
    res = {}
    ok = True
    for l2 in (a, b):
        t0 = time.time()
        lam = mp.sqrt(mp.mpf(repr(l2)))
        Q, _, _ = build_QW_mode(lam, N, "true")
        K = to_point(Q, N)
        dim = 2 * N + 1
        psd = cholesky_psd(K)
        if not psd:
            ok = False
            print(f"   [{tag}] lam^2={l2}: STARVED at dps {dps} -- pair dropped")
            break
        d0 = direct_pivot(K, dim, "seam")
        res[l2] = float(d0 / K[0, 0])
        print(f"   [{tag}] lam^2={l2:<6} (N={N}, dps={dps}, {time.time()-t0:.0f}s): "
              f"R_seam={res[l2]:.5f}")
    if not ok:
        continue
    rate = -np.log(res[b] / res[a]) / (b - a)
    OUT[tag] = dict(rate=rate, gam=gam, nz=nz, span=b - a, res=res)
    print(f"   [{tag}] rate = {rate:+.4f}" + (f"  (gamma {gam})" if gam else "  (gap)"))

print("\n== E2: the ensemble verdict ==")
rc = np.array([OUT[t]["rate"] for t in OUT if OUT[t]["nz"] >= 1])
rg = np.array([OUT[t]["rate"] for t in OUT if OUT[t]["nz"] == 0])
D = rc.mean() - rg.mean()
se = np.sqrt(rc.var(ddof=1) / len(rc) + rg.var(ddof=1) / len(rg))
print(f"   crossings (n={len(rc)}): mean {rc.mean():+.4f}  sd {rc.std(ddof=1):.4f}")
print(f"   gaps      (n={len(rg)}): mean {rg.mean():+.4f}  sd {rg.std(ddof=1):.4f}")
print(f"   D = {D:+.4f} +- {se:.4f}  ({abs(D)/se:.1f} s.e.)")
if D >= 2 * se:
    print("   E2: STAIRCASE ESTABLISHED (T-1rad)")
elif abs(D) < se:
    print("   E2: high crossings silent -> T-Nyq gains decisively")
else:
    print("   E2: between (report; extend ensemble)")

print("\n== E3: depth law ==")
inb = 0
tot = 0
for t in OUT:
    if OUT[t]["nz"] < 1:
        continue
    d = (OUT[t]["rate"] - rg.mean()) * OUT[t]["span"] / OUT[t]["nz"]
    dg = d * OUT[t]["gam"]
    tot += 1
    inb += (3 <= dg <= 10)
    print(f"   {t}: delta = {d:+.4f}   delta*gamma = {dg:+.2f}")
print(f"   in [3,10]: {inb}/{tot}")

print("\n== E4: the envelope to lam^2 = 77.9 ==")
c = 0.486
allR = [(l2, OUT[t]["res"][l2]) for t in OUT for l2 in OUT[t]["res"]]
x = np.array([p[0] for p in allR])
y = np.array([p[1] for p in allR])
pred = 0.03422 * np.exp(-c * ((np.log(x)**2 - np.log(12.25)**2) / 4))
print(f"   rms(log) vs envelope = {np.std(np.log(y) - np.log(pred)):.3f}  "
      f"mean offset {np.mean(np.log(y) - np.log(pred)):+.3f}  (n={len(x)})")

np.savez(HERE + "pinfG_crossing_ensemble.npz",
         tags=np.array([t for t in OUT]),
         rates=np.array([OUT[t]["rate"] for t in OUT]),
         nz=np.array([OUT[t]["nz"] for t in OUT]),
         l2=x, R=y)
print("\nARCHIVED: pinfG_crossing_ensemble.npz")
