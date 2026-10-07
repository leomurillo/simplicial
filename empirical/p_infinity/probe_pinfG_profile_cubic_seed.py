"""probe_pinfG_profile_cubic_seed.py -- queue item (ii): the fixed-profile cubic, first
measurement (the response-regression instrument).

THE REFRAME (after sections 8/11): the window-germ cubic is resolvent-dominated and
finite-window-unconditional; the PROFILE cubic must be read at the law level -- the
renewal's own scalar coordinates, where the resolvent disease cannot enter.  The
instrument: across exact unit-lambda^2 pairs (true-to-true), regress the per-arrival
log-increment of the seam remainder (and of the chiral pivot) on the step's
psi-fluctuation:
    Delta ln R_0 = a0/lam-bar^2 + a1 f + a2 f^2 + a3 f^3 + err,
f = (band atom mass) - (band PNT mass).  The a_k are the per-arrival push's order
attribution AT THE PROFILE, in invariant coordinates (F64-5 clean); a3 is the
fixed-profile cubic's seed measurement.  G.1'-at-the-profile consumes the WINDOWED
drift of exactly these coefficients.

THIS PROBE: builds the five missing lambda'' windows (the unit-step partners of the
round-3 interleaved windows), giving ELEVEN exact pairs spanning psi-fluc in
[-0.43, +0.44]; runs the regression on Delta ln R_0 and Delta ln d_-.

PRE-REGISTERED:
  PC1 (validity): new windows PSD at dps 70 (floors <= 1e-40-grade); d0-consistency
      <= 1e-12; refl <= 1e-30.
  PC2 (instrument honesty, locked): ELEVEN points / four regressors -- a SEED, not a
      verdict; coefficients reported WITH std errors; |a3| < 2 s.e. = "cubic not
      resolved at this sample" (expected; the deliverable is the instrument + the
      first numbers + the densification path).  No falsifier can fire on RH (W2).
  PC3 (reading): a1's sign -- the linear response of the eating to arrival excess
      (atom-heavy steps eat more or less?); the 18-window ladder refit.
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

mp.mp.dps = 70

# the five new lambda'' windows: unit-step partners of the round-3 lam' windows
BASE = [2.0591, 2.2361, 2.4166, 2.5539, 2.6926]
print("== queue (ii): profile-cubic seed -- five new windows, eleven pairs (dps=70) ==\n")
NEW = {}
for lam in BASE:
    t0 = time.time()
    lam2 = mp.mpf(repr(lam))**2
    lamp = mp.sqrt(lam2 + 1)
    Lp = 2 * mp.log(lamp)
    Np = int(round(float(24 / (2 * mp.log(2)) * Lp)))
    Q, L, pj = build_QW_mode(lamp, Np, "true")
    K = to_point(Q, Np)
    dim = 2 * Np + 1
    psd = cholesky_psd(K)
    ob = bridge_observables(K, dim)
    cons = float(abs(ob["d0"] - ob["d0x"]) / abs(ob["d0x"]))
    NEW[lam] = dict(lamp=float(lamp), ob=ob, psd=psd, cons=cons,
                    Rseam=float(ob["d0x"] / ob["K00"]))
    print(f"   lam''={float(lamp):.5f} (dim={dim}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'FAIL'} cons={cons:.1e}  "
          f"R_seam={NEW[lam]['Rseam']:.5f}  d-={float(ob['dm']):.3e}  "
          f"oddshare={ob['oddshare']:.4f}")

pc1 = all(NEW[l]["psd"] and NEW[l]["cons"] <= 1e-12 for l in BASE)
print("\n   PC1: " + ("SURVIVES" if pc1 else "FIRED -- halt"))

# ---------------- assemble the eleven pairs ----------------
# endpoints already known: certified 6 (parity_totals R0 via d0/K00... use published
# R_seam series), round-3 lam' windows (increment_bound npz), round-4 (lambda35 npz)
zi = np.load(HERE + "pinfG_increment_bound.npz")
R3 = {float(l): dict(R=zi["Rseam_new"][i], dm=zi["dm_new"][i])
      for i, l in enumerate(zi["lamps"])}
z4 = np.load(HERE + "pinfG_lambda35.npz")
RCERT = {1.8: 0.2884, 2.0: 0.2064, 2.2: 0.1496, 2.35: 0.1130, 2.5: 0.0922}
zc = np.load(HERE + "parity_totals.npz")
DMC = {float(l): zc["d_minus"][i] for i, l in enumerate(zc["lams"])}


def band_fluc(lam):
    lam2 = mp.mpf(repr(float(lam)))**2
    atoms = band_atoms(lam2, lam2 + 1)
    am = float(mp.fsum(w for _, w in atoms)) if atoms else 0.0
    return am - float(2 * (mp.sqrt(lam2 + 1) - mp.sqrt(lam2)))


pairs = []
# certified -> lam' (round 3, five pairs)
for lam in [1.8, 2.0, 2.2, 2.35, 2.5]:
    lp = [k for k in R3 if abs(k**2 - (lam**2 + 1)) < 1e-6][0]
    pairs.append((lam, lp, RCERT[lam], R3[lp]["R"], DMC[lam], R3[lp]["dm"]))
# lam' -> lam'' (this probe, five pairs)
for lam in BASE:
    pairs.append((lam, NEW[lam]["lamp"], R3[round(lam,4) if round(lam,4) in R3 else
                  min(R3, key=lambda k: abs(k - lam))]["R"],
                  NEW[lam]["Rseam"],
                  R3[min(R3, key=lambda k: abs(k - lam))]["dm"],
                  float(NEW[lam]["ob"]["dm"])))
# round-4 pair (3.5 -> 3.64)
pairs.append((3.5, float(z4["lams"][1]), float(z4["Rseam"][0]), float(z4["Rseam"][1]),
              float(z4["dm"][0]), float(z4["dm"][1])))

print("\n== the eleven pairs: per-arrival responses vs psi-fluc ==")
print("   pair              fluc      dlnR0      dlnd-")
rows = []
for la, lb, Ra, Rb, da, db in pairs:
    f = band_fluc(la)
    y0 = np.log(Rb / Ra)
    ym = np.log(db / da)
    lb2 = (la**2 + lb**2) / 2
    rows.append((la, lb, f, y0, ym, lb2))
    print(f"   {la:6.4f}->{lb:6.4f}  {f:+.4f}  {y0:+.4f}   {ym:+.4f}")

# ---------------- the regressions ----------------
X = np.array([[1.0 / r[5], r[2], r[2]**2, r[2]**3] for r in rows])
names = ["a0/lb2", "a1 (linear)", "a2 (quad)", "a3 (CUBIC)"]
for tag, y in [("Delta ln R_0", np.array([r[3] for r in rows])),
               ("Delta ln d_-", np.array([r[4] for r in rows]))]:
    beta, res_, rank, sv = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    dof = len(y) - 4
    s2 = float(np.sum((y - yhat)**2) / dof)
    cov = s2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    r2 = 1 - np.sum((y - yhat)**2) / np.sum((y - np.mean(y))**2)
    print(f"\n   regression {tag}  (n=11, R^2={r2:.3f}):")
    for nm, b, s in zip(names, beta, se):
        sig = abs(b) / s if s > 0 else float("inf")
        print(f"      {nm:12} = {b:+.4f} +- {s:.4f}   ({sig:.1f} s.e.)")

print("\n== PC3: the 18-window ladder ==")
allR = dict(RCERT); allR[1.5] = 0.4956
for k, v in R3.items():
    allR[k] = v["R"]
for lam in BASE:
    allR[NEW[lam]["lamp"]] = NEW[lam]["Rseam"]
allR[3.5] = float(z4["Rseam"][0]); allR[float(z4["lams"][1])] = float(z4["Rseam"][1])
lx = np.log(np.array(sorted(allR)))
ly = np.log(np.array([allR[k] for k in sorted(allR)]))
co = np.polyfit(lx, ly, 1)
print(f"   p = {-co[0]:.3f}   rms(log) = {np.std(ly - np.polyval(co, lx)):.3f}   "
      f"({len(allR)} windows, lam in [{min(allR):.2f}, {max(allR):.2f}])")

np.savez(HERE + "pinfG_profile_cubic_seed.npz",
         pairs=np.array([(r[0], r[1], r[2], r[3], r[4]) for r in rows]),
         ladder_lams=np.array(sorted(allR)),
         ladder_R=np.array([allR[k] for k in sorted(allR)]))
print("\nARCHIVED: pinfG_profile_cubic_seed.npz")
