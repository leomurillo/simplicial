"""probe_pinfG_lambda36_pair.py -- queue item (iii): the edge-class extension.
lambda = 3.6 -> lambda' = sqrt(13.96) = 3.73631 (an ATOM-BEARING unit step: the band
(12.96, 13.96] contains the prime 13; Lambda(13)/sqrt(13) = 0.7113, mean 0.2726,
psi-fluc = +0.4386 -- the phase complement of round 4's composite step).

THE QUESTION (P-inf-G section 11.1): the massive-cell constants softened at the 3.5-step
(c_- = 2.05, c_+ = 1.98 vs certified 2.6-3.3).  Class question: exponential with
arrival-phase noise, or slowly-varying (a second decode)?  This pair reads c_{+-} at
lam-bar^2 ~ 13.5 at an atom-bearing phase; with round 4's no-atom step it brackets the
phase confound.

PRE-REGISTERED:
  V1 (validity, F64-6): mp Cholesky PSD at dps 120 both windows (floor eps(3.74) ~
      1e-100 estimated; ~20 digits headroom); d0-consistency <= 1e-12; refl <= 1e-40.
  V2 (the class reading): c_{+-} at this pair reported against the certified band
      [2.6, 3.3] and the 3.5-step's [1.98, 2.05]; BOTH inside-low -> softening is real
      (slowly-varying class candidate); back inside the certified band -> phase noise.
  V3 (the law): R_seam at both windows vs the 13-window power law; oddshare and rho
      continue the section-11.2 irrelevant flow (oddshare ~ lam^-1.87, rho^2 ~
      lam^-1.77 predictions: oddshare(3.6) ~ 0.128, rho(3.6) ~ -0.43).
  V4 (gearing): the log-identity continues exactly.
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

mp.mp.dps = 120
CASES = [(3.6, 44), (float(mp.sqrt(mp.mpf("13.96"))), 46)]

print("== queue (iii): the lam=3.6 atom-bearing pair (dps=120) ==\n")
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
          f"PSD={'OK' if psd else 'FAIL'}  refl={dfl:.1e}  cons={cons:.1e}")
    print(f"      d-={float(ob['dm']):.4e}  d+={float(ob['dp']):.4e}  "
          f"R_seam={RES[lam]['Rseam']:.5f}  oddshare={ob['oddshare']:.4f}  "
          f"rho={float(ob['gam']/mp.sqrt(ob['v0']*ob['dp'])):.4f}")

lamA, lamB = CASES[0][0], CASES[1][0]
A, B = RES[lamA], RES[lamB]
v1 = A["psd"] and B["psd"] and max(A["cons"], B["cons"]) <= 1e-12
print("\n   V1: " + ("SURVIVES" if v1 else "FIRED -- starved/halt"))
fm = 1 - float(B["ob"]["dm"] / A["ob"]["dm"])
fp = 1 - float(B["ob"]["dp"] / A["ob"]["dp"])
f0 = 1 - float(B["ob"]["d0x"] / A["ob"]["d0x"])
cm, cp = -np.log(1 - fm), -np.log(1 - fp)
print(f"   V2 class: c- = {cm:.2f}  c+ = {cp:.2f}   (certified [2.6,3.3]; 3.5-step ~2.0)")
print(f"   V3 law: R_seam {A['Rseam']:.5f}/{B['Rseam']:.5f}; "
      f"oddshare {A['ob']['oddshare']:.4f}/{B['ob']['oddshare']:.4f} (flow pred ~0.128); "
      f"f0 = {f0:.4f}")
dlk = float(mp.log(B["ob"]["kap"] / A["ob"]["kap"]))
dld = float(mp.log(B["ob"]["dm"] / A["ob"]["dm"]))
dlE = float(mp.log(B["ob"]["E"] / A["ob"]["E"]))
print(f"   V4 gearing: {dlk:+.3f} {dld:+.3f} sum {dlk+dld:+.3f} vs dlnE {dlE:+.3f} "
      f"[err {abs(dlk+dld-dlE):.1e}]")
np.savez(HERE + "pinfG_lambda36_pair.npz",
         lams=np.array([lamA, float(lamB)]),
         Rseam=np.array([A["Rseam"], B["Rseam"]]),
         dm=np.array([float(A["ob"]["dm"]), float(B["ob"]["dm"])]),
         dp=np.array([float(A["ob"]["dp"]), float(B["ob"]["dp"])]),
         d0=np.array([float(A["ob"]["d0x"]), float(B["ob"]["d0x"])]),
         E=np.array([float(A["ob"]["E"]), float(B["ob"]["E"])]),
         oddshare=np.array([A["ob"]["oddshare"], B["ob"]["oddshare"]]),
         cpm=np.array([cm, cp]))
print("\nARCHIVED: pinfG_lambda36_pair.npz")
