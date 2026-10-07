"""probe_pinfG_step_hunt.py -- THE STEP-HUNT CAMPAIGN (DS1 fired: n=2 family-certified
lagged steps -- gamma_8: +0.2835 at u~1.4, delta*gamma~9.8; gamma_9: +0.1397 at u~0.7,
delta*gamma~5.4). Hunt the next two zeros' downstream neighborhoods at BOTH bandwidth
families; only family-invariant rates count (F64-7).

Design: for gamma_10 = 49.774 and gamma_11 = 52.970, three windows each spanning the
downstream zone u in [0.2, 1.8]:
  gamma_10: lambda^2 = 50.0, 50.8, 51.6   (rates at u = 0.63, 1.43)
  gamma_11: lambda^2 = 53.2, 54.0, 54.8   (rates at u = 0.63, 1.43)
Each window at C = 17.312 (N = round(17.312 ln center): 68) and C = 20 (N = 79).
dps 160.

PRE-REGISTERED (locked before first run; GPD):
  SH0: PSD everywhere; starved windows abort their family.
  SH1 (step certification, per zero): some midpoint u in (0, 2) downstream with
       |r17 - r20| <= 0.10 AND mean rate >= +0.10  ->  step CERTIFIED at that zero.
  SH2 (depth law): over ALL certified steps to date (gamma_8, gamma_9 + any new),
       delta_j * gamma_j in [3, 12] for >= 3 of n  ->  the Sec 15.4 depth law holds on
       family-certified instances (delta_j = mean-rate x 0.8, the interval share).
  SH3 (lags): reported, no rule (n too small to fit).
  Honest note: gamma_10's downstream zone partially overlaps gamma_11's upstream
  approach (gap 3.20) and gamma_9's zone sits 0.2-1.1 below window 1 -- feature
  assignment at narrow gaps is by nearest-zero-below, reported as such.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

CAMPAIGN = [
    ("g10", 49.774, [50.0, 50.8, 51.6]),
    ("g11", 52.970, [53.2, 54.0, 54.8]),
]
FAMILIES = [("C17", 17.312), ("C20", 20.0)]
DPS = 160

mp.mp.dps = DPS
results = {}
for tag, gam, wins in CAMPAIGN:
    center = wins[1]
    for fam, C in FAMILIES:
        N = int(round(C * float(mp.log(mp.mpf(repr(center))))))
        R = {}
        print(f"== [{tag}] family {fam} (N={N}) ==")
        for l2 in wins:
            t0 = time.time()
            lam = mp.sqrt(mp.mpf(repr(l2)))
            Q, _, _ = build_QW_mode(lam, N, "true")
            K = to_point(Q, N)
            if not cholesky_psd(K):
                print(f"   lam^2={l2}: STARVED -- family aborted")
                R = None
                break
            d0 = direct_pivot(K, 2 * N + 1, "seam")
            R[l2] = float(d0 / K[0, 0])
            print(f"   lam^2={l2:<5} ({time.time()-t0:.0f}s): R_seam={R[l2]:.5f}")
        if R is None:
            continue
        rates = [-np.log(R[b] / R[a]) / (b - a)
                 for a, b in zip(wins[:-1], wins[1:])]
        results[(tag, fam)] = rates
        print(f"   rates: {['%+.4f' % r for r in rates]}")

print("\n== SH1: step certification ==")
certified = [("g8", 43.327, 0.2835, 1.37), ("g9", 48.005, 0.1397, 0.69)]  # archived
for tag, gam, wins in CAMPAIGN:
    if (tag, "C17") not in results or (tag, "C20") not in results:
        print(f"   [{tag}] incomplete families -- no verdict")
        continue
    r17, r20 = results[(tag, "C17")], results[(tag, "C20")]
    got = False
    for k, (a, b) in enumerate(zip(wins[:-1], wins[1:])):
        mid = (a + b) / 2
        u = mid - gam
        dv = abs(r17[k] - r20[k])
        mean = 0.5 * (r17[k] + r20[k])
        line = (f"   [{tag}] mid={mid:.2f} (u={u:+.2f}): r17={r17[k]:+.4f} "
                f"r20={r20[k]:+.4f}  ")
        if dv <= 0.10 and mean >= 0.10 and 0 < u < 2:
            got = True
            certified.append((tag, gam, mean, u))
            line += f"-> STEP CERTIFIED (mean {mean:+.4f})"
        elif dv <= 0.10:
            line += f"-> family-invariant, sub-threshold (mean {mean:+.4f})"
        else:
            line += f"-> ripple (+-{dv/2:.4f})"
        print(line)
    if not got:
        print(f"   [{tag}] no certified step in u in (0,2)")

print("\n== SH2: the depth law on certified instances ==")
inb = 0
for tag, gam, rate, u in certified:
    dg = rate * 0.8 * gam
    inb += (3 <= dg <= 12)
    print(f"   {tag}: delta*gamma = {dg:+.2f}   (lag u = {u:+.2f})")
print(f"   in [3,12]: {inb}/{len(certified)}  "
      f"({'DEPTH LAW HOLDS' if inb >= 3 else 'insufficient'} on family-certified steps)")

np.savez(HERE + "pinfG_step_hunt.npz",
         certified=np.array([(g, r, u) for _, g, r, u in certified]),
         **{f"{t}_{f}": np.array(v) for (t, f), v in results.items()})
print("\nARCHIVED: pinfG_step_hunt.npz")
