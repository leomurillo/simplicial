"""probe_pinfG_twoconstant_scan.py -- THE CT1 'BETWEEN' BRANCH: complete the C=20
profile of the gamma_8..gamma_9 gap and decompose kernel vs ripple pointwise.

CT1 (July 5) split the object: the gamma_8 drop (mid 44.70) is family-invariant to
0.012 (kernel, five configurations), while the tail reorganized (+0.00,-0.23,-0.12 ->
-0.21,+0.05,+0.01), sliding ~0.8 units with the family change (the m-ripple, amplitude
+-0.1-0.2). This probe completes the C=20 scan (four missing windows: 42.7, 43.5,
48.3, 49.1 at N=76; the segment 44.3-47.5 is archived in pinfG_ctest.npz), yielding
both full 8-rate profiles at C=17.312 and C=20 on identical midpoints.

PRE-REGISTERED (locked before first run; GPD):
  DS0: PSD at dps 160 everywhere.
  DS1 (second kernel feature): a midpoint within 0.9 of gamma_9 = 48.005 (i.e. 47.90
       or 48.70) with |r17 - r20| <= 0.10 AND |mean rate| >= 0.10
       -> the lagged-step motif has a second family-invariant instance near a zero;
          REGISTER the step-hunt campaign (gamma_9/10/11 downstream neighborhoods,
          two families each);
       no such midpoint -> the gamma_8 drop is a singleton (report; step-hunt
          suspended pending a third gap).
  DS2 (pointwise decomposition, descriptive): kernel estimate = mean(r17, r20) where
       |r17 - r20| <= 0.10; ripple amplitude = |r17 - r20|/2 elsewhere; both tabulated.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

NEW = [42.7, 43.5, 48.3, 49.1]
N = 76
DPS = 160
G9 = 48.005151

# archived C=20 segment (pinfG_ctest.npz) and full C=17.312 scan (pinfG_phase_scan.npz)
ct = np.load(HERE + "pinfG_ctest.npz")
R20 = {float(w): float(r) for w, r in zip(ct["windows"], ct["R"])}
ps = np.load(HERE + "pinfG_phase_scan.npz")
R17 = {float(w): float(r) for w, r in zip(ps["l2"], ps["R"])}

mp.mp.dps = DPS
print(f"== two-constant scan completion: C=20 (N={N}), four new windows ==\n")
for l2 in NEW:
    t0 = time.time()
    lam = mp.sqrt(mp.mpf(repr(l2)))
    Q, _, _ = build_QW_mode(lam, N, "true")
    K = to_point(Q, N)
    if not cholesky_psd(K):
        print(f"   lam^2={l2}: STARVED (DS0 fails) -- abort")
        sys.exit(1)
    d0 = direct_pivot(K, 2 * N + 1, "seam")
    R20[l2] = float(d0 / K[0, 0])
    print(f"   lam^2={l2:<5} ({time.time()-t0:.0f}s): R_seam={R20[l2]:.5f}")

WINDOWS = sorted(R17)
mids, r17s, r20s = [], [], []
for a, b in zip(WINDOWS[:-1], WINDOWS[1:]):
    mids.append((a + b) / 2)
    r17s.append(-np.log(R17[b] / R17[a]) / (b - a))
    r20s.append(-np.log(R20[b] / R20[a]) / (b - a))

print("\n== DS2: pointwise decomposition (mid | r17 | r20 | verdict) ==")
second = False
for m, r17, r20 in zip(mids, r17s, r20s):
    dv = abs(r17 - r20)
    if dv <= 0.10:
        verdict = f"KERNEL ~ {0.5*(r17+r20):+.4f}"
        if abs(m - G9) <= 0.9 and abs(0.5 * (r17 + r20)) >= 0.10:
            second = True
            verdict += "   <-- DS1: second invariant feature (near gamma_9)"
    else:
        verdict = f"ripple +-{0.5*dv:.4f}"
    print(f"   {m:5.2f}  {r17:+.4f}  {r20:+.4f}   {verdict}")

print("\n== DS1 ==")
if second:
    print("   DS1: SECOND family-invariant feature near gamma_9 -> lagged-step motif")
    print("        n=2; REGISTER the step-hunt campaign (gamma_9/10/11, two families)")
else:
    print("   DS1: no second invariant feature near gamma_9 -> the gamma_8 drop is a")
    print("        singleton so far; step-hunt suspended pending a third gap")

np.savez(HERE + "pinfG_twoconstant_scan.npz",
         windows=np.array(WINDOWS),
         R17=np.array([R17[w] for w in WINDOWS]),
         R20=np.array([R20[w] for w in WINDOWS]),
         mids=np.array(mids), r17=np.array(r17s), r20=np.array(r20s))
print("\nARCHIVED: pinfG_twoconstant_scan.npz")
