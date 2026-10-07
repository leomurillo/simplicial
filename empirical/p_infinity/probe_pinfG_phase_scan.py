"""probe_pinfG_phase_scan.py -- THE PHASE-RESOLVED SCAN: one full gap, nine same-N
windows, the quadrature tested inside a single gap.

The July-4 ensemble + extension established (X1, 2.5 s.e., 20 pairs) a zero-synchronized
class contrast: eating mid-gap, replenishment at the zeros. This scan resolves the phase
INSIDE one gap -- the wide, cheap gamma_8..gamma_9 gap (43.327 -> 48.005, width 4.68,
dps 160 throughout) -- with everything at one fixed N (no sawtooth, no dps step).

Windows: 42.70, 43.50, 44.30, 45.10, 45.90, 46.70, 47.50, 48.30, 49.10
         (Delta = 0.8, N = 67, dps = 160; gamma_8 inside window-pair 1, gamma_9 inside
          window-pair 7)
Rates r_1..r_8 at midpoints 43.10, 43.90, 44.70, 45.50, 46.30, 47.10, 47.90, 48.70.
Classes (locked): NEAR-ZERO = {r1, r2, r7, r8} (interval contains a zero or midpoint
within 0.9 of one); MID-GAP = {r3, r4, r5, r6}. A clean symmetric 4/4 split.

PRE-REGISTERED (locked before first run; GPD):
  PH0: PSD at dps 160 at every window (fixed-N family; F64-6 detector = any PSD failure).
  PH1: mean(MID) - mean(NEAR) >= +0.08  ->  QUADRATURE CONFIRMED phase-resolved;
       <= 0.00                          ->  quadrature DEAD in this gap (report);
       in (0, 0.08)                     ->  between; replicate in gamma_11..gamma_12.
  PH2 (pattern, secondary): >=3 of 4 MID rates positive AND >=2 of 4 NEAR rates <= 0
       ->  the sign pattern box (reported alongside PH1, decides nothing alone).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

WINDOWS = [42.70, 43.50, 44.30, 45.10, 45.90, 46.70, 47.50, 48.30, 49.10]
N = 67
DPS = 160
G8, G9 = 43.327073, 48.005151

mp.mp.dps = DPS
print(f"== phase-resolved scan: gamma_8..gamma_9 gap, N={N} fixed, dps={DPS} ==\n")
R = {}
for l2 in WINDOWS:
    t0 = time.time()
    lam = mp.sqrt(mp.mpf(repr(l2)))
    Q, _, _ = build_QW_mode(lam, N, "true")
    K = to_point(Q, N)
    dim = 2 * N + 1
    if not cholesky_psd(K):
        print(f"   lam^2={l2}: STARVED (PH0 fails) -- abort")
        sys.exit(1)
    d0 = direct_pivot(K, dim, "seam")
    R[l2] = float(d0 / K[0, 0])
    print(f"   lam^2={l2:<6} ({time.time()-t0:.0f}s): R_seam={R[l2]:.5f}")

print("\n== rates and classes ==")
rates = []
for a, b in zip(WINDOWS[:-1], WINDOWS[1:]):
    mid = (a + b) / 2
    rate = -np.log(R[b] / R[a]) / (b - a)
    d = min(abs(mid - G8), abs(mid - G9))
    cls = "NEAR" if (d < 0.9 or (a < G8 < b) or (a < G9 < b)) else "MID"
    rates.append((mid, rate, cls))
    print(f"   r(mid={mid:.2f}) = {rate:+.4f}   [{cls}]  (dist-to-zero {d:.2f})")

mid_r = [r for _, r, c in rates if c == "MID"]
near_r = [r for _, r, c in rates if c == "NEAR"]
diff = np.mean(mid_r) - np.mean(near_r)
print(f"\n   MID  (n={len(mid_r)}): mean {np.mean(mid_r):+.4f}  sd {np.std(mid_r, ddof=1):.4f}")
print(f"   NEAR (n={len(near_r)}): mean {np.mean(near_r):+.4f}  sd {np.std(near_r, ddof=1):.4f}")
print(f"   PH1 statistic: mid - near = {diff:+.4f}")
if diff >= 0.08:
    print("   PH1: QUADRATURE CONFIRMED (phase-resolved)")
elif diff <= 0.0:
    print("   PH1: quadrature DEAD in this gap (report)")
else:
    print("   PH1: between -- replicate in gamma_11..gamma_12")

ph2 = (sum(r > 0 for r in mid_r) >= 3) and (sum(r <= 0 for r in near_r) >= 2)
print(f"   PH2 pattern box: {'CHECKED' if ph2 else 'not checked'} "
      f"(mid>0: {sum(r > 0 for r in mid_r)}/4, near<=0: {sum(r <= 0 for r in near_r)}/4)")

np.savez(HERE + "pinfG_phase_scan.npz",
         l2=np.array(WINDOWS), R=np.array([R[w] for w in WINDOWS]),
         mids=np.array([m for m, _, _ in rates]),
         rates=np.array([r for _, r, _ in rates]),
         cls=np.array([c for _, _, c in rates]))
print("\nARCHIVED: pinfG_phase_scan.npz")
