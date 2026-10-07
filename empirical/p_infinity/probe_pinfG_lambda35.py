"""probe_pinfG_lambda35.py -- P-inf-G round 4: the lambda = 3.5 discriminator
(registered F section 23.6; now TRIPLE-LOADED after sections 9-10).

Builds the true kernels at lambda = 3.5 (lam^2 = 12.25) and its exact unit-step partner
lambda' = sqrt(13.25) = 3.64005 (the SIXTH true-to-true pair; band (11.25, 12.25]
contains only n = 12 = 2^2*3, composite -- a no-atom step like the 2.5-pair), and reads
the full bridge-observable set at both.

PRE-REGISTERED (locked; W2-compliant -- rules target laws and instrument, not RH):
  U1 (validity, F64-6): mp Cholesky PSD at dps 110 at both windows (floor eps(3.64) ~
      1e-90 estimated; dps 110 leaves ~20 digits headroom -- the Cholesky IS the
      starvation detector); d0-consistency (v0 - gamma^2/d+ vs direct Schur) <= 1e-12;
      reflection defect <= 1e-40.  Fired -> HALT (raise dps, do not read).
  U2 (THE p-DISCRIMINATOR, G.3's falsifiable prediction): the 11-window power law
      (p = 3.204) predicts R_seam(3.5) = 0.0354; the per-arrival exponential
      C e^{-0.342 lam^2} anchored at lam=2.5 predicts 0.0118 (separated x3).
      RULE: |ln R - ln pred_pow| <= 0.25 -> p HOLDS (the lawful deceleration
      terminates; G.3 supported).  R within 0.25 log of the EXPONENTIAL track ->
      law-degradation alert (marginal-contact-consistent; honest report).
      Intermediate -> report both residuals as measured.
  U3 (plateau, G.5.2): oddshare(3.5), oddshare(3.64) inside [0.18, 0.34]; the section
      10.3 downward drift trend reported against the new points.
  U4 (drift watch-items): d-/d+ and rho at both windows vs the rising 0.96 -> 1.93
      trend; report.
  U5 (the 6th pair, no-atom phase): f_-, f_+ -> c_{+-} inside [2.0, 4.0]; f_0 vs
      p/(2 lam-bar^2) = 0.126.
  U6 (gearing): Delta ln kappa~ + Delta ln d_- = Delta ln E (identity; the compensation
      law's continuation at the new phase).
Output: 13-window p refit; all observables archived.
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

SMOKE = "--smoke" in sys.argv
DPS = 40 if SMOKE else 110
mp.mp.dps = DPS

CASES = [(3.5, 43), (float(mp.sqrt(mp.mpf("13.25"))), 45)]
if SMOKE:
    CASES = [(3.5, 12)]

R11 = {1.5: 0.4956, 1.8: 0.2884, 2.0: 0.2064, 2.0591: 0.17443, 2.2: 0.1496,
       2.2361: 0.15417, 2.35: 0.1130, 2.4166: 0.10297, 2.5: 0.0922,
       2.5539: 0.09322, 2.6926: 0.08192}

print(f"== P-inf-G round 4: lambda = 3.5 triple-loaded discriminator (dps={DPS}) ==\n")
RES = {}
for lam, N in CASES:
    t0 = time.time()
    lam_mp = mp.mpf(repr(float(lam)))
    Q, L, pj = build_QW_mode(lam_mp, N, "true")
    K = to_point(Q, N)
    dim = 2 * N + 1
    psd = cholesky_psd(K)
    dfl = refl_defect(K, dim)
    ob = bridge_observables(K, dim)
    cons = float(abs(ob["d0"] - ob["d0x"]) / abs(ob["d0x"]))
    RES[lam] = dict(ob=ob, psd=psd, dfl=dfl, cons=cons,
                    Rseam=float(ob["d0x"] / ob["K00"]), dim=dim)
    el = time.time() - t0
    print(f"   lam={float(lam):.5f} (dim={dim}, {el:.0f}s): PSD={'OK' if psd else 'FAIL'}"
          f"  refl={dfl:.1e}  d0-cons={cons:.1e}")
    print(f"      d-={float(ob['dm']):.4e}  d+={float(ob['dp']):.4e}  d0={float(ob['d0x']):.5f}"
          f"  E={float(ob['E']):.4e}  kappa~={float(ob['kap']):.4e}")
    print(f"      R_seam={RES[lam]['Rseam']:.5f}  oddshare={ob['oddshare']:.4f}  "
          f"rho={float(ob['gam']/mp.sqrt(ob['v0']*ob['dp'])):.4f}  "
          f"d-/d+={float(ob['dm']/ob['dp']):.4f}")

if SMOKE:
    print("\nSMOKE OK")
    sys.exit(0)

lamA, lamB = CASES[0][0], CASES[1][0]
A, B = RES[lamA], RES[lamB]

print("\n== U1: validity ==")
u1 = all(R["psd"] for R in (A, B)) and all(R["cons"] <= 1e-12 for R in (A, B)) \
     and all(R["dfl"] <= 1e-40 for R in (A, B))
print("   " + ("SURVIVES" if u1 else "FIRED -- HALT, raise dps"))

print("\n== U2: the p-discriminator ==")
lx = np.log(np.array(sorted(R11)))
ly = np.log(np.array([R11[k] for k in sorted(R11)]))
co = np.polyfit(lx, ly, 1)
pred_pow = float(np.exp(np.polyval(co, np.log(3.5))))
pred_exp = 0.0922 * np.exp(-0.342 * (12.25 - 6.25))
r_pow = abs(np.log(A["Rseam"] / pred_pow))
r_exp = abs(np.log(A["Rseam"] / pred_exp))
print(f"   R_seam(3.5) = {A['Rseam']:.5f}   pow-pred(p={-co[0]:.3f}) = {pred_pow:.5f} "
      f"[|dln|={r_pow:.3f}]   exp-pred = {pred_exp:.5f} [|dln|={r_exp:.3f}]")
if r_pow <= 0.25:
    print("   U2: p HOLDS -- the RG power law extends to lam=3.5 (G.3's prediction supported)")
elif r_exp <= 0.25:
    print("   U2: LAW-DEGRADATION ALERT -- tracks the per-arrival exponential (report honestly)")
else:
    print("   U2: intermediate -- both residuals reported as measured")
lx13 = np.append(lx, [np.log(3.5), np.log(float(lamB))])
ly13 = np.append(ly, [np.log(A["Rseam"]), np.log(B["Rseam"])])
co13 = np.polyfit(lx13, ly13, 1)
print(f"   13-window refit: p = {-co13[0]:.3f}   rms(log) = "
      f"{np.std(ly13 - np.polyval(co13, lx13)):.3f}")

print("\n== U3/U4: plateau and drifts ==")
u3 = all(0.18 <= R["ob"]["oddshare"] <= 0.34 for R in (A, B))
print(f"   oddshare: {A['ob']['oddshare']:.4f} (3.5), {B['ob']['oddshare']:.4f} (3.64)  "
      + ("inside [0.18,0.34] -- plateau holds" if u3 else "OUTSIDE -- finding"))
print(f"   d-/d+: {float(A['ob']['dm']/A['ob']['dp']):.3f}, {float(B['ob']['dm']/B['ob']['dp']):.3f}"
      f"   (trend was 0.96 -> 1.93 at 2.06 -> 2.69)")
rhoA = float(A["ob"]["gam"] / mp.sqrt(A["ob"]["v0"] * A["ob"]["dp"]))
rhoB = float(B["ob"]["gam"] / mp.sqrt(B["ob"]["v0"] * B["ob"]["dp"]))
print(f"   rho: {rhoA:.4f}, {rhoB:.4f}   (certified band [-0.76, -0.60])")

print("\n== U5/U6: the 6th pair (no-atom step) and the gearing ==")
fm = 1 - float(B["ob"]["dm"] / A["ob"]["dm"])
fp = 1 - float(B["ob"]["dp"] / A["ob"]["dp"])
f0 = 1 - float(B["ob"]["d0x"] / A["ob"]["d0x"])
fE = 1 - float(B["ob"]["E"] / A["ob"]["E"])
cm, cp = -np.log(1 - fm), -np.log(1 - fp)
print(f"   f_-={fm:.4f} (c-={cm:.2f})  f_+={fp:.4f} (c+={cp:.2f})  "
      f"f_0={f0:.4f} [law 0.126]  f_E={fE:.4f}")
u5 = 2.0 <= cm <= 4.0 and 2.0 <= cp <= 4.0
print("   U5: " + ("SURVIVES" if u5 else "OUTSIDE [2,4] -- finding"))
dlk = float(mp.log(B["ob"]["kap"] / A["ob"]["kap"]))
dld = float(mp.log(B["ob"]["dm"] / A["ob"]["dm"]))
dlE = float(mp.log(B["ob"]["E"] / A["ob"]["E"]))
print(f"   U6 gearing: dln kap = {dlk:+.3f}  dln d- = {dld:+.3f}  sum = {dlk+dld:+.3f}"
      f"  vs dln E = {dlE:+.3f}  [ident err {abs(dlk+dld-dlE):.1e}]")

np.savez(HERE + "pinfG_lambda35.npz",
         lams=np.array([lamA, float(lamB)]),
         Rseam=np.array([A["Rseam"], B["Rseam"]]),
         dm=np.array([float(A["ob"]["dm"]), float(B["ob"]["dm"])]),
         dp=np.array([float(A["ob"]["dp"]), float(B["ob"]["dp"])]),
         d0=np.array([float(A["ob"]["d0x"]), float(B["ob"]["d0x"])]),
         E=np.array([float(A["ob"]["E"]), float(B["ob"]["E"])]),
         kap=np.array([float(A["ob"]["kap"]), float(B["ob"]["kap"])]),
         oddshare=np.array([A["ob"]["oddshare"], B["ob"]["oddshare"]]),
         rho=np.array([rhoA, rhoB]),
         p13=np.array([-co13[0]]))
print("\nARCHIVED: pinfG_lambda35.npz")
print("RESULT: " + ("GREEN" if (u1 and u3 and u5) else "PARTIAL -- see blocks") +
      " -- verdicts above")
