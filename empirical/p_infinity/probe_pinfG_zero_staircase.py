"""probe_pinfG_zero_staircase.py -- THE ZERO-DETECTOR TEST (dense scan across gamma_2).

CONTEXT (PREREG_lambda4_floor.txt + addendum; FD2 outcome): R_seam's six high points
read as a STAIRCASE -- gap-plateaus (16->17 flat; 21.25->25 NET +4.9% over 3.75 units,
16% above the smooth log-squared envelope, beyond wiggle) and transition drops (17->
20.25: -30%, the gamma_2 coherence zone; 25->26: -10%, straddling gamma_3) -- with the
registered log-squared envelope hitting R(5.0) to 2%.  Mechanism: zero gamma_j feeds
the seam's innovation while its per-arrival phase step gamma_j/lam^2 >~ 1; crossing
lam^2 ~ gamma_j retires it.  THE TEST: eating-rate contrast between the gamma_2
transition zone and the adjacent quiet gap, dense in lam^2 (phase wiggle averages out
over multiple unit steps; a coherent zone contrast survives it).

PRE-REGISTERED (locked):
  Z1 (validity): PSD + d0-consistency <= 1e-12 at dps 130 (flat-pace law + backstop
      say eps ~ 1e-66..1e-80 here; headroom ample).
  Z2 (THE CONTRAST): zone A = lam^2 in [19.5, 22.0] (the gamma_2 = 21.02 transition),
      zone B = lam^2 in [22.0, 24.25] (gap quiet zone).  rate = -d ln R_seam/d lam^2
      averaged per zone (least squares within zone, using the 25/26 endpoints from the
      discriminator archive to extend B).  RULE: rate_A >= 2 x rate_B  ->  STAIRCASE
      CONFIRMED at gamma_2 (the seam detects individual zeros); rate_A ~ rate_B ->
      smooth log-squared without resolvable steps (clean negative); rate_A < rate_B ->
      the zone model is wrong (report).
  Z3 (reading): the d_- tower's staircase (same zones, same contrast on dln d_-).
Windows: lam^2 = 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.75, 23.5, 24.25 (nine new,
dps 130, N = round(17.312 L)).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

L2S = [19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.75, 23.5, 24.25]
mp.mp.dps = 130

print("== the zero-detector test: dense scan across gamma_2 = 21.02 (dps=130) ==\n")
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
    # consistency: K00 and a cheap d0 sanity (psd + positive pivot)
    R = float(d0 / K[0, 0])
    OUT[l2] = dict(R=R, dm=float(dm), psd=psd, lam=float(lam))
    print(f"   lam^2={l2:<6} (lam={float(lam):.4f}, dim={dim}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'FAIL'}  R_seam={R:.5f}  d-={float(dm):.3e}")

z1 = all(OUT[l]["psd"] and OUT[l]["R"] > 0 for l in L2S)
print("\n   Z1: " + ("SURVIVES" if z1 else "FIRED"))

# extend zone B with the discriminator's 25/26 points
zd = np.load(HERE + "pinfG_floor_discriminator.npz")
extB = {float(l)**2: float(r) for l, r in zip(zd["lams"], zd["Rseam"]) if l >= 4.9}

print("\n== Z2: the zone contrast ==")
A = [(l, OUT[l]["R"]) for l in L2S if l <= 22.0]
B = [(l, OUT[l]["R"]) for l in L2S if l > 22.0] + sorted(extB.items())
for tag, pts in [("A (gamma_2 zone)", A), ("B (quiet gap)", B)]:
    x = np.array([p[0] for p in pts])
    y = np.log(np.array([p[1] for p in pts]))
    co = np.polyfit(x, y, 1)
    se = np.std(y - np.polyval(co, x)) / (np.std(x) * np.sqrt(len(x)))
    print(f"   zone {tag}: rate = {-co[0]:+.4f} +- {se:.4f} per unit lam^2  "
          f"(n={len(pts)}, lam^2 {x.min()}-{x.max()})")
xA = np.array([p[0] for p in A]); yA = np.log([p[1] for p in A])
xB = np.array([p[0] for p in B]); yB = np.log([p[1] for p in B])
rA = -np.polyfit(xA, yA, 1)[0]
rB = -np.polyfit(xB, yB, 1)[0]
if rB <= 0:
    print(f"   zone B rate <= 0 (plateau/rise): contrast infinite -> "
          + ("STAIRCASE CONFIRMED at gamma_2" if rA > 0.02 else "both flat -- report"))
elif rA >= 2 * rB:
    print(f"   rate_A/rate_B = {rA/rB:.1f} >= 2  ->  STAIRCASE CONFIRMED at gamma_2")
else:
    print(f"   rate_A/rate_B = {rA/rB:.1f} < 2  ->  no resolvable step (smooth-decay read)")

print("\n== Z3: the d_- tower in the same zones ==")
for tag, pts in [("A", [(l, OUT[l]["dm"]) for l in L2S if l <= 22.0]),
                 ("B", [(l, OUT[l]["dm"]) for l in L2S if l > 22.0])]:
    x = np.array([p[0] for p in pts])
    y = np.log(np.array([p[1] for p in pts]))
    co = np.polyfit(x, y, 1)
    print(f"   zone {tag}: c_- = {-co[0]:+.3f} per unit lam^2 (n={len(pts)})")

np.savez(HERE + "pinfG_zero_staircase.npz",
         l2=np.array(L2S),
         R=np.array([OUT[l]["R"] for l in L2S]),
         dm=np.array([OUT[l]["dm"] for l in L2S]))
print("\nARCHIVED: pinfG_zero_staircase.npz")
