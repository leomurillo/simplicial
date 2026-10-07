"""probe_pinfG_floor_discriminator.py -- THE FLOOR DISCRIMINATOR (lambda = 4.5 and 5
pairs; the registered follow-up to the lambda-4 result R_seam flat at 0.0288).

CONTEXT.  PREREG_lambda4_floor.txt's read rule FIRED FOR THE DECELERATION CLASS:
R_seam(4.0) = 0.02883, R_seam(4.1231) = 0.02884 (flat; H-pow's 0.0229 missed by +26%).
All renewal coordinates flatten in concert (oddshare 0.112, rho -0.414, d-/d+ 1.55,
c_pm 0.90).  Open: FLOOR (interior fixed point, f summable) vs LOG-DECAY (R ~ C/ln
lambda -- the Sliwinski/CCM crawl shape!) vs residual power.  The flat-pace ladder law
(P-inf-G section 13.4, log10 eps = -4.85 lam^2 + 7.3) makes lambda = 5 affordable
(dps ~150 vs the retired accelerating estimate's ~260).

PRE-REGISTERED (locked before the run):
  FD1 (validity/starvation): PSD + d0-consistency <= 1e-12 at every window at the
      scheduled dps (130/150 -- set BY the new flat-pace law: if FD1 fires at 4.61 or
      5.10, the flat law itself broke above 3.5 -- a finding; rerun higher).
  FD2 (THE DISCRIMINATION; anchored at R(4.0) = 0.02883):
      FLOOR:      R(4.5) ~ 0.0288, R(5.0) ~ 0.0288  (flat +- 6-10% wiggle)
      LOG-DECAY:  R(4.5) = 0.0266, R(5.0) = 0.0248  (C/ln lambda)
      RESIDUAL POWER (p ~ 1.2): R(4.5) = 0.0250, R(5.0) = 0.0221
      READ RULE: R(5.0) >= 0.0275 -> FLOOR; 0.024 <= R(5.0) < 0.0275 -> LOG-CLASS
      (the crawl's own shape surfacing in the seam remainder); R(5.0) < 0.024 ->
      residual power.  Both pair-internal slopes reported (both steps are no-atom:
      bands (20.25, 21.25] contain 21 = 3*7, (25, 26] contain 26 = 2*13 -- composite:
      clean smooth-phase reads, no atom shock).
  FD3 (fixed-point coordinates): oddshare, rho, d-/d+, c_pm at lam-bar^2 = 20.75 and
      25.5 -- convergence-or-not of each.
  FD4: the gearing identity continues.
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

PAIRS = [
    (4.5, float(mp.sqrt(mp.mpf("21.25"))), 52, 53, 130),
    (5.0, float(mp.sqrt(mp.mpf("26"))), 56, 56, 150),
]

print("== THE FLOOR DISCRIMINATOR: lambda = 4.5 and 5 pairs ==\n")
RES = {}
for lamA, lamB, NA, NB, dps in PAIRS:
    mp.mp.dps = dps
    for lam, N in [(lamA, NA), (lamB, NB)]:
        t0 = time.time()
        Q, L, pj = build_QW_mode(mp.mpf(repr(float(lam))), N, "true")
        K = to_point(Q, N)
        dim = 2 * N + 1
        psd = cholesky_psd(K)
        ob = bridge_observables(K, dim)
        cons = float(abs(ob["d0"] - ob["d0x"]) / abs(ob["d0x"]))
        RES[lam] = dict(ob=ob, psd=psd, cons=cons,
                        Rseam=float(ob["d0x"] / ob["K00"]))
        print(f"   lam={float(lam):.5f} (dim={dim}, dps={dps}, {time.time()-t0:.0f}s): "
              f"PSD={'OK' if psd else 'FAIL -- STARVED'}  cons={cons:.1e}")
        print(f"      R_seam={RES[lam]['Rseam']:.5f}  oddshare={ob['oddshare']:.4f}  "
              f"rho={float(ob['gam']/mp.sqrt(ob['v0']*ob['dp'])):.4f}  "
              f"d-/d+={float(ob['dm']/ob['dp']):.4f}  d-={float(ob['dm']):.3e}")

print("\n== FD1 ==")
fd1 = all(RES[l]["psd"] and RES[l]["cons"] <= 1e-12 for l in RES)
print("   " + ("SURVIVES" if fd1 else "FIRED -- flat-pace law broke / starved: rerun higher dps"))

print("\n== FD2: the discrimination (anchored R(4.0) = 0.02883) ==")
for lamA, lamB, *_ in PAIRS:
    A, B = RES[lamA], RES[lamB]
    print(f"   R({lamA}) = {A['Rseam']:.5f}   R({lamB:.4f}) = {B['Rseam']:.5f}   "
          f"pair slope p = {-np.log(B['Rseam']/A['Rseam'])/np.log(lamB/lamA):+.2f}")
R5 = RES[5.0]["Rseam"]
if R5 >= 0.0275:
    print(f"   READ: R(5.0) = {R5:.5f} >= 0.0275  ->  FLOOR (interior fixed point)")
elif R5 >= 0.024:
    print(f"   READ: R(5.0) = {R5:.5f} in [0.024, 0.0275)  ->  LOG-CLASS decay (the crawl's shape)")
else:
    print(f"   READ: R(5.0) = {R5:.5f} < 0.024  ->  residual power")

print("\n== FD3/FD4: fixed-point coordinates and the gearing ==")
for lamA, lamB, *_ in PAIRS:
    A, B = RES[lamA], RES[lamB]
    fm = 1 - float(B["ob"]["dm"] / A["ob"]["dm"])
    fp = 1 - float(B["ob"]["dp"] / A["ob"]["dp"])
    lb2 = (lamA**2 + lamB**2) / 2
    cm, cp = -np.log(1 - fm), -np.log(1 - fp)
    dlk = float(mp.log(B["ob"]["kap"] / A["ob"]["kap"]))
    dld = float(mp.log(B["ob"]["dm"] / A["ob"]["dm"]))
    dlE = float(mp.log(B["ob"]["E"] / A["ob"]["E"]))
    print(f"   pair {lamA}: c- = {cm:.2f}  c+ = {cp:.2f}  (lb2 = {lb2:.1f})   "
          f"gearing err {abs(dlk+dld-dlE):.1e}")

np.savez(HERE + "pinfG_floor_discriminator.npz",
         lams=np.array(sorted(RES)),
         Rseam=np.array([RES[l]["Rseam"] for l in sorted(RES)]),
         oddshare=np.array([RES[l]["ob"]["oddshare"] for l in sorted(RES)]),
         dm=np.array([float(RES[l]["ob"]["dm"]) for l in sorted(RES)]),
         dp=np.array([float(RES[l]["ob"]["dp"]) for l in sorted(RES)]))
print("\nARCHIVED: pinfG_floor_discriminator.npz")
