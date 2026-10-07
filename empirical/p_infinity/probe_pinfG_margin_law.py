"""probe_pinfG_margin_law.py -- P-inf-G round 3b: the LAW of the arrival-direction cone
margin (the N6 follow-up: round 3's linear bisection saturated at its resolution floor
2^-29 at ALL windows -- the margin m* = 1 - t* is below 1.9e-9 everywhere; this probe
resolves it by bisection on log10 s, s = 1 - t).

OBJECT: K(s) = K_true + s (KA - KS) along the arrival-swap direction; s* = the largest
s with K PSD (the cone margin in one-arrival units).  PREDICTION (registered): s*
tracks the exp-small ladder floor (s* ~ eps(lam')/coupling) -- the Fuchs pace, ~5-7
decades over the span lam' = 2.06 -> 2.69.  Either law is a new (U)-coordinate.

PRE-REGISTERED:
  M1 (bracket): PSD at s = 1e-45, non-PSD at s = 3.7e-9 (round 3's floor) per window.
      Fired at the low end -> the margin is below 1e-45: report as bound, stop.
  M2 (the law, reading): log10 s* vs lam' -- fit pace per unit lambda^2; compare with
      the Fuchs ladder pace (interpolated log10 eps: ~ -13.6 -> -27.7 over the span,
      i.e. ~ -4.7/unit-lambda^2).  Monotone-in-s assumption checked by the bracket.
Machinery: v2 lineage exec-import; dps 65; 20 log-bisection steps per window.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])
exec(src[src.index("def build_window"):src.index("def window_phis")])

mp.mp.dps = 65
PAIRS = [1.8, 2.0, 2.2, 2.35, 2.5]

print("== P-inf-G round 3b: the arrival-direction margin law (log bisection, dps=65) ==\n")
out = []
for lam in PAIRS:
    t0 = time.time()
    W = build_window(lam)
    D = W["KA"] - W["KS"]
    def psd_at(le):                 # le = log10 s
        s = mp.power(10, mp.mpf(repr(float(le))))
        return cholesky_psd(W["K_true"] + s * D)
    lo, hi = -45.0, float(np.log10(3.7e-9))
    ok_lo, ok_hi = psd_at(lo), psd_at(hi)
    if not ok_lo:
        print(f"   lam'={float(W['lamp']):.5f}: NON-PSD already at s=1e-45 -- bound only")
        out.append((float(W["lamp"]), None))
        continue
    if ok_hi:
        print(f"   lam'={float(W['lamp']):.5f}: PSD at 3.7e-9?! bracket broken -- diagnose")
        out.append((float(W["lamp"]), None))
        continue
    for _ in range(20):
        mid = (lo + hi) / 2
        if psd_at(mid):
            lo = mid
        else:
            hi = mid
    s_star = (lo + hi) / 2
    out.append((float(W["lamp"]), s_star))
    print(f"   lam'={float(W['lamp']):.5f} (dim={W['dim']}, {time.time()-t0:.0f}s): "
          f"log10 s* = {s_star:.3f}   s* = {10**s_star:.2e}")

pts = [(l, s) for l, s in out if s is not None]
if len(pts) >= 3:
    lx = np.array([p[0]**2 for p in pts])          # lambda'^2 (arrival clock)
    ly = np.array([p[1] for p in pts])
    co = np.polyfit(lx, ly, 1)
    print(f"\n   law: log10 s* = {co[0]:+.2f} * lam'^2 {co[1]:+.2f}   "
          f"(rms {np.std(ly - np.polyval(co, lx)):.3f})")
    print("   Fuchs-ladder pace over the same span: ~ -4.7 per unit lambda^2 (interpolated)")
np.savez(HERE + "pinfG_margin_law.npz",
         lamps=np.array([p[0] for p in out]),
         log10_sstar=np.array([p[1] if p[1] is not None else np.nan for p in out]))
print("\nARCHIVED: pinfG_margin_law.npz")
