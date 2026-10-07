"""probe_pinfG_gap_extension.py -- THE FIRED E2 BRANCH: extend the gap class 4 -> 9.

The July-4 ensemble returned D = -0.1044 +- 0.0374 (2.8 s.e., SIGN-INVERTED vs the
staircase): remainder rises across zero crossings, falls mid-gap. Its gap class had
n = 4, mean leaning on two large members. This probe adds five fresh same-N gap pairs
in previously unsampled gap interiors, then pools with the archived ensemble.

PRE-REGISTERED (locked before this script is first run; GPD):
  X0: per-window PSD at scheduled dps (160 center <= 55, 190 above); starved dropped.
  X1 (pooled verdict): D_ext = mean(11 archived crossing rates) - mean(4 archived +
      5 new gap rates); s.e. from class scatter as in E2.
      D_ext <= -2 s.e.  -> ANTI-STAIRCASE ESTABLISHED (zero-synchronized replenishment:
                           eating mid-gap, feeding at the zeros);
      |D_ext| < 1 s.e.  -> the July-4 D was gap-class noise; staircase question REOPENS;
      between           -> supported-not-settled; next instrument = the phase-resolved
                           single-gap scan (registered separately).
  X2 (independence): new-gaps-only mean >= +0.04 at >= 1.5 s.e. (vs its own scatter)
      -> mid-gap eating confirmed independent of the July-4 four.
  Note: the quadrature hypothesis being tested was formed from the July-4 data
  (post-hoc there, labeled); THIS run is its first out-of-sample test.

Gap pairs (no zero inside any window span; zeta zeros gamma_8..gamma_18 bracket them):
  (43.90, 45.50)  gap g8-g9    (gamma_8=43.327, gamma_9=48.005)
  (50.30, 51.90)  gap g10-g11  (gamma_10=49.774, gamma_11=52.970)
  (57.00, 58.60)  gap g12-g13  (gamma_12=56.446, gamma_13=59.347)
  (61.20, 62.80)  gap g14-g15  (gamma_14=60.832, gamma_15=65.113)
  (70.20, 71.80)  gap g17-g18  (gamma_17=69.546, gamma_18=72.067; upper edge 0.27
                                below gamma_18 -- the nearest approach, noted)
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

NEWGAPS = [
    ("xg8-9", 43.90, 45.50), ("xg10-11", 50.30, 51.90), ("xg12-13", 57.00, 58.60),
    ("xg14-15", 61.20, 62.80), ("xg17-18", 70.20, 71.80),
]

print("== gap-class extension: five fresh same-N gap pairs ==\n")
new_rates = []
for tag, a, b in NEWGAPS:
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
        if not cholesky_psd(K):
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
    new_rates.append(rate)
    print(f"   [{tag}] rate = {rate:+.4f}  (gap)")

ens = np.load(HERE + "pinfG_crossing_ensemble.npz")
rc = ens["rates"][ens["nz"] >= 1]
rg_old = ens["rates"][ens["nz"] == 0]
rg = np.concatenate([rg_old, np.array(new_rates)])

print("\n== X1: the pooled verdict ==")
D = rc.mean() - rg.mean()
se = np.sqrt(rc.var(ddof=1) / len(rc) + rg.var(ddof=1) / len(rg))
print(f"   crossings (n={len(rc)}): mean {rc.mean():+.4f}  sd {rc.std(ddof=1):.4f}")
print(f"   gaps      (n={len(rg)}): mean {rg.mean():+.4f}  sd {rg.std(ddof=1):.4f}  "
      f"(old {rg_old.mean():+.4f}, new {np.mean(new_rates):+.4f})")
print(f"   D_ext = {D:+.4f} +- {se:.4f}  ({abs(D)/se:.1f} s.e.)")
if D <= -2 * se:
    print("   X1: ANTI-STAIRCASE ESTABLISHED (replenishment at zeros, eating mid-gap)")
elif abs(D) < se:
    print("   X1: July-4 D was gap-class noise -- staircase question REOPENS")
else:
    print("   X1: between (supported-not-settled; phase-resolved scan next)")

print("\n== X2: new gaps alone ==")
ng = np.array(new_rates)
se2 = ng.std(ddof=1) / np.sqrt(len(ng))
print(f"   new-gap mean {ng.mean():+.4f} +- {se2:.4f}")
if ng.mean() >= 0.04 and ng.mean() >= 1.5 * se2:
    print("   X2: mid-gap eating CONFIRMED independent of the July-4 four")
else:
    print("   X2: not confirmed independently (report)")

np.savez(HERE + "pinfG_gap_extension.npz",
         new_rates=ng, rc=rc, rg=rg)
print("\nARCHIVED: pinfG_gap_extension.npz")
