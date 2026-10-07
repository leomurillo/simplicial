"""probe_pinfG_ctest.py -- THE FAMILY-CONSTANT TEST: closes the NS1 loophole.

NS1 (July 5) returned 'between' (dmax = 0.074): the oscillation's shape survives
N -> N+-1 (drop +0.288/+0.290/+0.321; rise -0.19/-0.23/-0.16; no sign flips) -- kernel-
looking with a +-0.07 N-modulation. SELF-ATTACK (registered here, post-NS1): a ripple
periodic in the CONTINUOUS mismatch m = N - 17.312 ln(lambda^2) with period 1 is
INVISIBLE to integer N shifts (m moves by exactly one period), and alias resonances
(F64-4) are periodic in m. NS1 cannot exclude it.

Discriminator: change the family constant. At N matched to C = 20 (N = 76 fixed over
the segment), an m-periodic instrument ripple must change period (lambda^2/C:
2.63 -> 2.28) and shift phase by ~0.7 lambda^2-units across the segment; a kernel
oscillation cannot know C and stays put.

PRE-REGISTERED (locked before first run; GPD):
  CT0: PSD at dps 160 everywhere (N = 76, dim = 153).
  CT1: with r_k the four rates at midpoints 44.70, 45.50, 46.30, 47.10 and the
       archived C=17.312/N=67 values (+0.2897, +0.0018, -0.2299, -0.1227):
       |r_1(C20) - r_1(C17)| <= 0.10 AND sign pattern (+, ., -, -) preserved
           -> KERNEL: the oscillation is arithmetic content; attribution closed;
       r_1 changes by >= 0.20 OR the maximum-drop midpoint moves >= 0.7 units
           -> INSTRUMENT: m-periodic ripple; all July rate-level class verdicts
              formally retracted to instrument-confounded;
       otherwise -> between (report; the two-constant dense scan is next).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

WINDOWS = [44.3, 45.1, 45.9, 46.7, 47.5]
N = 76          # round(20 * ln 45.5) -- the C = 20 family, fixed over the segment
DPS = 160
R17 = [0.2897, 0.0018, -0.2299, -0.1227]   # archived rates, C=17.312 (N=67 scan)

mp.mp.dps = DPS
print(f"== family-constant test: C = 20 (N = {N} fixed), dps = {DPS} ==\n")
R = {}
for l2 in WINDOWS:
    t0 = time.time()
    lam = mp.sqrt(mp.mpf(repr(l2)))
    Q, _, _ = build_QW_mode(lam, N, "true")
    K = to_point(Q, N)
    if not cholesky_psd(K):
        print(f"   lam^2={l2}: STARVED (CT0 fails) -- abort")
        sys.exit(1)
    d0 = direct_pivot(K, 2 * N + 1, "seam")
    R[l2] = float(d0 / K[0, 0])
    print(f"   lam^2={l2:<5} ({time.time()-t0:.0f}s): R_seam={R[l2]:.5f}")

rates = [-np.log(R[b] / R[a]) / (b - a)
         for a, b in zip(WINDOWS[:-1], WINDOWS[1:])]
mids = [(a + b) / 2 for a, b in zip(WINDOWS[:-1], WINDOWS[1:])]
print("\n== CT1: attribution across family constants ==")
print(f"   C=17.3 rates: {['%+.4f' % r for r in R17]}")
print(f"   C=20   rates: {['%+.4f' % r for r in rates]}")
d1 = abs(rates[0] - R17[0])
sign_ok = (rates[0] > 0) and (rates[2] < 0) and (rates[3] < 0)
drop17, drop20 = mids[int(np.argmax(R17))], mids[int(np.argmax(rates))]
moved = abs(drop20 - drop17)
print(f"   |r1(C20)-r1(C17)| = {d1:.4f}; sign pattern preserved = {sign_ok}; "
      f"max-drop midpoint moved {moved:.2f}")
if d1 <= 0.10 and sign_ok:
    print("   CT1: KERNEL -- the oscillation is arithmetic; attribution closed")
elif d1 >= 0.20 or moved >= 0.7:
    print("   CT1: INSTRUMENT -- m-periodic ripple; July class verdicts retracted")
else:
    print("   CT1: between -- two-constant dense scan next")

np.savez(HERE + "pinfG_ctest.npz",
         windows=np.array(WINDOWS), R=np.array([R[w] for w in WINDOWS]),
         rates=np.array(rates), mids=np.array(mids), r17=np.array(R17))
print("\nARCHIVED: pinfG_ctest.npz")
