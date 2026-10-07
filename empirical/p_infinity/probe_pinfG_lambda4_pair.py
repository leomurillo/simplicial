"""probe_pinfG_lambda4_pair.py -- target T3: the lambda >= 4 edge-class run.
lambda = 4.0 -> lambda' = sqrt(17) = 4.12311 (atom-bearing unit step: the band (16, 17]
contains the PRIME 17; Lambda(17)/sqrt(17) = 0.6872 vs mean 0.2462 -> psi-fluc = +0.4410).

THE QUESTION (P-inf-G section 12.3): across twelve pairs the edge constants soften
(c_- : 2.6-3.2 at lam-bar^2 <= 7.8 -> 1.79-2.05 at ~13.5) while p_- = 2 lam-bar^2 c_-
RISES 21 -> 52 -- neither pure-exponential nor pure-power class.  This pair reads the
constants at lam-bar^2 = 16.5, the longest lever available, at an atom-bearing phase.

PRE-REGISTERED:
  W1 (validity, F64-6): mp Cholesky PSD at dps 175 at both windows (floor estimate
      eps(sqrt17) ~ 1e-149; headroom ~26 digits; Cholesky = the starvation detector);
      d0-consistency <= 1e-12; refl <= 1e-60.  Fired -> HALT, do not read.
  W2 (the class reading): c_{+-} at this pair vs the softening sequence
      [2.6-3.3] -> [1.98-2.05] -> [1.76-1.79]: continued fall -> slowly-varying class
      strengthened (candidate c ~ const/ln lam or stretched); bounce above 2.3 ->
      phase-noise re-reading.  Either way: p_{+-} = 2 lam-bar^2 c_{+-} logged.
  W3 (the flows): oddshare/rho/R_seam vs the section 11.2 irrelevant-flow predictions
      (oddshare ~ 1.6/lam^1.87-grade: pred(4.0) ~ 0.105-0.110); the 20-window power law.
  W4 (gearing): the log-identity continues.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])
srcI = open(HERE + "probe_pinfG_increment_bound.py", encoding="utf-8").read()
exec(srcI[srcI.index("def schur_solve"):srcI.index("def tstar_bisect")])

mp.mp.dps = 175
CASES = [(4.0, 48), (float(mp.sqrt(mp.mpf("17"))), 49)]

print("== T3: the lambda = 4 pair (dps=175) ==\n")
RES = {}
for lam, N in CASES:
    t0 = time.time()
    Q, L, pj = build_QW_mode(mp.mpf(repr(float(lam))), N, "true")
    K = to_point(Q, N)
    dim = 2 * N + 1
    psd = cholesky_psd(K)
    dfl = refl_defect(K, dim)
    ob = bridge_observables(K, dim)
    cons = float(abs(ob["d0"] - ob["d0x"]) / abs(ob["d0x"]))
    RES[lam] = dict(ob=ob, psd=psd, dfl=dfl, cons=cons,
                    Rseam=float(ob["d0x"] / ob["K00"]))
    print(f"   lam={float(lam):.5f} (dim={dim}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'FAIL -- STARVED, HALT'}  refl={dfl:.1e}  cons={cons:.1e}")
    print(f"      d-={float(ob['dm']):.4e}  d+={float(ob['dp']):.4e}  "
          f"R_seam={RES[lam]['Rseam']:.5f}  oddshare={ob['oddshare']:.4f}  "
          f"rho={float(ob['gam']/mp.sqrt(ob['v0']*ob['dp'])):.4f}  "
          f"d-/d+={float(ob['dm']/ob['dp']):.4f}")

lamA, lamB = CASES[0][0], CASES[1][0]
A, B = RES[lamA], RES[lamB]
w1 = A["psd"] and B["psd"] and max(A["cons"], B["cons"]) <= 1e-12
print("\n   W1: " + ("SURVIVES" if w1 else "FIRED -- starved/halt"))
fm = 1 - float(B["ob"]["dm"] / A["ob"]["dm"])
fp = 1 - float(B["ob"]["dp"] / A["ob"]["dp"])
f0 = 1 - float(B["ob"]["d0x"] / A["ob"]["d0x"])
cm, cp = -np.log(1 - fm), -np.log(1 - fp)
lb2 = (lamA**2 + lamB**2) / 2
print(f"   W2 class: c- = {cm:.2f}  c+ = {cp:.2f}   p- = {2*lb2*cm:.0f}  p+ = {2*lb2*cp:.0f}"
      f"   (sequence: [2.6-3.3] -> [1.98-2.05] -> [1.76-1.79] -> ?)")
print(f"   W3 flows: R_seam {A['Rseam']:.5f}/{B['Rseam']:.5f}; oddshare "
      f"{A['ob']['oddshare']:.4f}/{B['ob']['oddshare']:.4f} (flow pred ~0.105-0.110); "
      f"f0 = {f0:.4f} [p/(2 lb2) = {3.1/(2*lb2):.4f}]")
dlk = float(mp.log(B["ob"]["kap"] / A["ob"]["kap"]))
dld = float(mp.log(B["ob"]["dm"] / A["ob"]["dm"]))
dlE = float(mp.log(B["ob"]["E"] / A["ob"]["E"]))
print(f"   W4 gearing: {dlk:+.3f} {dld:+.3f} sum {dlk+dld:+.3f} vs dlnE {dlE:+.3f} "
      f"[err {abs(dlk+dld-dlE):.1e}]")
np.savez(HERE + "pinfG_lambda4_pair.npz",
         lams=np.array([lamA, lamB]),
         Rseam=np.array([A["Rseam"], B["Rseam"]]),
         dm=np.array([float(A["ob"]["dm"]), float(B["ob"]["dm"])]),
         dp=np.array([float(A["ob"]["dp"]), float(B["ob"]["dp"])]),
         d0=np.array([float(A["ob"]["d0x"]), float(B["ob"]["d0x"])]),
         E=np.array([float(A["ob"]["E"]), float(B["ob"]["E"])]),
         oddshare=np.array([A["ob"]["oddshare"], B["ob"]["oddshare"]]),
         cpm=np.array([cm, cp]))
print("\nARCHIVED: pinfG_lambda4_pair.npz")
