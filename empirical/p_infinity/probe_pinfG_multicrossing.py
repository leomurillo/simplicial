"""probe_pinfG_multicrossing.py -- THE PER-ZERO LAW TEST (crossings gamma_4..gamma_7).

CONTEXT (P-inf-G section 15.4 + the Z2 verdict): the staircase is supported at gamma_2
(~1 sigma); the per-zero retirement model predicts step depths delta_j ~ c/gamma_j with
c ~ 6.3 (i.e. delta_j gamma_j ~ const ~ 5-7), and gap-plateaus between crossings.  This
scan resolves FOUR crossings -- gamma_4 = 30.42, gamma_5 = 32.94, gamma_6 = 37.59,
gamma_7 = 40.92 -- with flanking gap baselines: cumulative statistics across four steps
beat the per-window wiggle that limited Z2.

PRE-REGISTERED:
  M1 (validity): PSD + positive pivots at dps 160 throughout (the decelerating-ladder
      budget; Cholesky = starvation detector).
  M2 (THE LAW): per-crossing step depths delta_j from the local drops (crossing-zone
      rate minus flanking-gap rate, x zone width); registered test: delta_j gamma_j
      inside [3, 10] for at least 3 of the 4 crossings -> the per-zero law stands;
      systematic sign failure (no excess eating at crossings, pooled across all four)
      -> the staircase dies (clean negative; the log-squared envelope then carries
      everything smoothly).
  M3 (envelope): the 12 points against the log-squared extrapolation (c = 0.486
      anchored at R(3.5), R(4.0)); rms reported.
  M4 (reading): the d_- tower's crossings; oddshare NOT computed (lean probe).
Windows (lam^2): 28.0, 29.5 | 30.5, 31.5 (g4) | 32.5, 33.5 (g5) | 35.0, 36.5 |
37.5, 38.5 (g6) | 40.5, 41.5 (g7).  dps 160.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

L2S = [28.0, 29.5, 30.5, 31.5, 32.5, 33.5, 35.0, 36.5, 37.5, 38.5, 40.5, 41.5]
GAMMAS = {"g4": 30.42, "g5": 32.94, "g6": 37.59, "g7": 40.92}
mp.mp.dps = 160

print("== the per-zero law test: crossings gamma_4..gamma_7 (dps=160) ==\n")
OUT = {}
for l2 in L2S:
    t0 = time.time()
    lam = mp.sqrt(mp.mpf(repr(l2)))
    L = 2 * mp.log(lam)
    N = int(round(float(24 / (2 * mp.log(2)) * L)))
    Q, _, _ = build_QW_mode(lam, N, "true")
    K = to_point(Q, N)
    dim = 2 * N + 1
    psd = cholesky_psd(K)
    d0 = direct_pivot(K, dim, "seam")
    dm = direct_pivot(K, dim, "odd")
    R = float(d0 / K[0, 0])
    OUT[l2] = dict(R=R, dm=float(dm), psd=psd)
    print(f"   lam^2={l2:<5} (dim={dim}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'FAIL'}  R_seam={R:.5f}  d-={float(dm):.3e}")

m1 = all(OUT[l]["psd"] and OUT[l]["R"] > 0 for l in L2S)
print("\n   M1: " + ("SURVIVES" if m1 else "FIRED"))

print("\n== M2: per-crossing steps ==")
x = np.array(L2S)
y = np.log([OUT[l]["R"] for l in L2S])
pairs_rate = -(np.diff(y) / np.diff(x))
for i in range(len(L2S) - 1):
    mid = (L2S[i] + L2S[i + 1]) / 2
    near = [g for g, gv in GAMMAS.items() if L2S[i] <= gv <= L2S[i + 1]]
    print(f"   {L2S[i]}-{L2S[i+1]}: rate = {pairs_rate[i]:+.4f}"
          + (f"   <-- crossing {near[0]} = {GAMMAS[near[0]]}" if near else ""))
# crossing vs gap pooled
cross_idx = [i for i in range(len(L2S) - 1)
             if any(L2S[i] <= gv <= L2S[i + 1] for gv in GAMMAS.values())]
gap_idx = [i for i in range(len(L2S) - 1) if i not in cross_idx]
rc = pairs_rate[cross_idx]
rg = pairs_rate[gap_idx]
print(f"   pooled crossing rate = {rc.mean():+.4f} +- {rc.std()/np.sqrt(len(rc)):.4f} (n={len(rc)})")
print(f"   pooled gap rate      = {rg.mean():+.4f} +- {rg.std()/np.sqrt(len(rg)):.4f} (n={len(rg)})")
ok3 = 0
for g, gv in GAMMAS.items():
    i = [i for i in range(len(L2S) - 1) if L2S[i] <= gv <= L2S[i + 1]]
    if not i:
        continue
    i = i[0]
    width = L2S[i + 1] - L2S[i]
    delta = (pairs_rate[i] - rg.mean()) * width
    dg = delta * gv
    inside = 3 <= dg <= 10
    ok3 += inside
    print(f"   {g}: delta_j = {delta:+.4f}   delta_j*gamma_j = {dg:+.2f}"
          + ("   [3,10] OK" if inside else "   outside [3,10]"))
print("   M2: " + ("LAW STANDS (>=3 of 4 inside)" if ok3 >= 3 else
                   ("staircase DIES (no crossing excess)" if rc.mean() <= rg.mean()
                    else f"partial ({ok3}/4 inside) -- report")))

print("\n== M3: the log-squared envelope ==")
c = 0.486
R35, l35 = 0.03422, 12.25
pred = R35 * np.exp(-c * (np.log(x)**2 - np.log(l35)**2) / 1.0)   # ln lam^2 squared /4*4
# careful: ln R = -c (ln lam^2)^2/4 + const -> use difference form with (ln l2)^2/4
pred = R35 * np.exp(-c * ((np.log(x)**2 - np.log(l35)**2) / 4))
resid = np.log([OUT[l]["R"] for l in L2S]) - np.log(pred)
print(f"   rms(log) vs envelope = {np.std(resid):.3f}; mean offset {np.mean(resid):+.3f}")

np.savez(HERE + "pinfG_multicrossing.npz",
         l2=x, R=np.array([OUT[l]["R"] for l in L2S]),
         dm=np.array([OUT[l]["dm"] for l in L2S]))
print("\nARCHIVED: pinfG_multicrossing.npz")
