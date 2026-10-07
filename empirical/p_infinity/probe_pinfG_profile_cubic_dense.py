"""probe_pinfG_profile_cubic_dense.py -- target T2: the densified profile-cubic
regression (P-inf-G section 12.2 follow-up).

Builds SEVEN new windows -- the unit-step partners of the second-generation windows
(2.2891, 2.4495, 2.6153, 2.7427, 2.8723 -> lam' = 2.4986, 2.6458, 2.7995, 2.9210,
3.0414) and of the high pair ends (3.6401 -> sqrt(14.25) = 3.7749; 3.7363 ->
sqrt(14.96) = 3.8678) -- giving NINETEEN exact unit-lambda^2 pairs total (the 12
existing incl. the 3.6-pair + 7 new).  Regression per channel on
{1, 1/lam-bar^2, fluc, fluc^2, fluc^3}.

PRE-REGISTERED:
  PD0 (validity): all new windows PSD (dps per F64-6 schedule below); d0-consistency
      <= 1e-12.  Fired -> drop the window, report.
  PD1 (pooled fit): both channels, n = 19, five regressors; coefficients +- s.e.
  PD2 (registered rule): a2(seam) > 0 at >= 2 s.e. pooled -> the variance-replenishment
      law stands; |a2| < 1 s.e. -> washes out (finding; the seed's 2.6 s.e. was
      sample-fragile).
  PD3 (persistence, the G.1'-windowed reading): split pairs at the median lam-bar^2;
      a2 per half per channel; the seam/chiral SIGN ASYMMETRY (a2_seam > 0 > a2_chiral)
      in both halves = the windowed persistence seed.
  PD4: a3 resolved at >= 2 s.e.?  Report either way.
  PD5: the 26-window ladder refit (certified 6 + interleaved 5 + second-gen 5 + new 7
      + round-4 2 + 3.6-pair 1... all distinct windows currently archived).
dps schedule: 65 (lam' <= 2.80), 70 (2.92), 80 (3.04), 125 (3.77), 130 (3.87).
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

NEWWIN = [
    # (lam_base of the pair, lam' = sqrt(base^2+1), N', dps)
    (2.2891, 2.4986, None, 65),
    (2.4495, 2.6458, None, 65),
    (2.6153, 2.7995, None, 65),
    (2.7427, 2.9210, None, 70),
    (2.8723, 3.0414, None, 80),
    (3.6401, 3.7749, None, 125),
    (3.7363, 3.8678, None, 130),
]

print("== T2: densified profile-cubic regression -- seven new windows ==\n")
NEW = {}
for base, lamp_t, _, dps in NEWWIN:
    t0 = time.time()
    mp.mp.dps = dps
    lam2 = mp.mpf(repr(base))**2
    lamp = mp.sqrt(lam2 + 1)
    Lp = 2 * mp.log(lamp)
    Np = int(round(float(24 / (2 * mp.log(2)) * Lp)))
    Q, L, pj = build_QW_mode(lamp, Np, "true")
    K = to_point(Q, Np)
    dim = 2 * Np + 1
    psd = cholesky_psd(K)
    ob = bridge_observables(K, dim)
    cons = float(abs(ob["d0"] - ob["d0x"]) / abs(ob["d0x"]))
    NEW[base] = dict(lamp=float(lamp), Rseam=float(ob["d0x"] / ob["K00"]),
                     dm=float(ob["dm"]), psd=psd, cons=cons,
                     oddshare=ob["oddshare"])
    print(f"   lam'={float(lamp):.5f} (dim={dim}, dps={dps}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'FAIL'} cons={cons:.1e}  "
          f"R_seam={NEW[base]['Rseam']:.5f}  d-={NEW[base]['dm']:.3e}  "
          f"oddshare={NEW[base]['oddshare']:.4f}")

pd0 = all(NEW[b]["psd"] and NEW[b]["cons"] <= 1e-12 for b in NEW)
print("\n   PD0: " + ("SURVIVES" if pd0 else "FIRED -- drop affected windows"))

# ---------------- assemble all nineteen pairs ----------------
mp.mp.dps = 40
zi = np.load(HERE + "pinfG_increment_bound.npz")
R3 = {float(l): dict(R=zi["Rseam_new"][i], dm=zi["dm_new"][i]) for i, l in enumerate(zi["lamps"])}
zs = np.load(HERE + "pinfG_profile_cubic_seed.npz")
SG = {float(r[1]): None for r in zs["pairs"]}  # second-gen lamps in pairs col 1
z4 = np.load(HERE + "pinfG_lambda35.npz")
z36 = np.load(HERE + "pinfG_lambda36_pair.npz")
RCERT = {1.8: 0.2884, 2.0: 0.2064, 2.2: 0.1496, 2.35: 0.1130, 2.5: 0.0922}
zc = np.load(HERE + "parity_totals.npz")
DMC = {float(l): zc["d_minus"][i] for i, l in enumerate(zc["lams"])}
# second-gen window observables from the seed run's archive: R and dm stored via pairs
# (pairs cols: la, lb, fluc, dlnR0, dlnd-) -> reconstruct lb-values from R3/la
SEED = {}
for la, lb, f, y0, ym in zs["pairs"]:
    la, lb = float(la), float(lb)
    if la in R3 or any(abs(la - k) < 1e-4 for k in R3):
        key = min(R3, key=lambda k: abs(k - la))
        if abs(key - la) < 1e-4:
            SEED[lb] = dict(R=R3[key]["R"] * np.exp(y0), dm=R3[key]["dm"] * np.exp(ym))


def band_fluc(lam):
    lam2 = mp.mpf(repr(float(lam)))**2
    atoms = band_atoms(lam2, lam2 + 1)
    am = float(mp.fsum(w for _, w in atoms)) if atoms else 0.0
    return am - float(2 * (mp.sqrt(lam2 + 1) - mp.sqrt(lam2)))


pairs = []
# 1-5: certified -> interleaved
for lam in [1.8, 2.0, 2.2, 2.35, 2.5]:
    lp = min(R3, key=lambda k: abs(k**2 - (lam**2 + 1)))
    pairs.append((lam, lp, RCERT[lam], R3[lp]["R"], DMC[lam], R3[lp]["dm"]))
# 6-10: interleaved -> second-gen (from the seed archive)
for la in [2.0591, 2.2361, 2.4166, 2.5539, 2.6926]:
    key = min(R3, key=lambda k: abs(k - la))
    lb = float(np.sqrt(la**2 + 1))
    sk = min(SEED, key=lambda k: abs(k - lb))
    pairs.append((la, sk, R3[key]["R"], SEED[sk]["R"], R3[key]["dm"], SEED[sk]["dm"]))
# 11: 3.5 -> 3.6401 ; 12: 3.6 -> 3.7363
pairs.append((3.5, float(z4["lams"][1]), float(z4["Rseam"][0]), float(z4["Rseam"][1]),
              float(z4["dm"][0]), float(z4["dm"][1])))
pairs.append((3.6, float(z36["lams"][1]), float(z36["Rseam"][0]), float(z36["Rseam"][1]),
              float(z36["dm"][0]), float(z36["dm"][1])))
# 13-17: second-gen -> third-gen (this probe)
for base in [2.2891, 2.4495, 2.6153, 2.7427, 2.8723]:
    sk = min(SEED, key=lambda k: abs(k - base))
    pairs.append((base, NEW[base]["lamp"], SEED[sk]["R"], NEW[base]["Rseam"],
                  SEED[sk]["dm"], NEW[base]["dm"]))
# 18-19: high pairs 3.6401 -> 3.7749, 3.7363 -> 3.8678
pairs.append((3.6401, NEW[3.6401]["lamp"], float(z4["Rseam"][1]), NEW[3.6401]["Rseam"],
              float(z4["dm"][1]), NEW[3.6401]["dm"]))
pairs.append((3.7363, NEW[3.7363]["lamp"], float(z36["Rseam"][1]), NEW[3.7363]["Rseam"],
              float(z36["dm"][1]), NEW[3.7363]["dm"]))

print("\n== the nineteen pairs ==")
print("   pair                fluc      dlnR0      dlnd-      lb2")
rows = []
for la, lb, Ra, Rb, da, db in pairs:
    f = band_fluc(la)
    y0 = float(np.log(Rb / Ra))
    ym = float(np.log(db / da))
    lb2 = (la**2 + lb**2) / 2
    rows.append((la, lb, f, y0, ym, lb2))
    print(f"   {la:6.4f}->{lb:6.4f}  {f:+.4f}  {y0:+.4f}   {ym:+.4f}   {lb2:5.2f}")

X = np.array([[1.0, 1.0 / r[5], r[2], r[2]**2, r[2]**3] for r in rows])
names = ["const", "a0/lb2", "a1 (linear)", "a2 (quad)", "a3 (CUBIC)"]
results = {}
for tag, y in [("dlnR0 (seam)", np.array([r[3] for r in rows])),
               ("dlnd- (chiral)", np.array([r[4] for r in rows]))]:
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    dof = len(y) - X.shape[1]
    s2 = float(np.sum((y - yhat)**2) / dof)
    cov = s2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    r2 = 1 - np.sum((y - yhat)**2) / np.sum((y - np.mean(y))**2)
    results[tag] = (beta, se)
    print(f"\n   {tag}  (n={len(y)}, R^2={r2:.3f}):")
    for nm, b, s in zip(names, beta, se):
        print(f"      {nm:12} = {b:+.4f} +- {s:.4f}   ({abs(b)/s if s>0 else 0:.1f} s.e.)")

b, s = results["dlnR0 (seam)"]
pd2 = b[3] > 0 and b[3] / s[3] >= 2
print("\n   PD2 (a2 seam > 0 at >= 2 s.e.): " + ("SURVIVES -- replenishment law stands"
      if pd2 else ("FIRED -- washes out" if abs(b[3]) < s[3] else "between (1-2 s.e.) -- report")))

print("\n== PD3: persistence split (median lam-bar^2) ==")
med = np.median([r[5] for r in rows])
for half, sel in [("low ", [r for r in rows if r[5] <= med]),
                  ("high", [r for r in rows if r[5] > med])]:
    Xh = np.array([[1.0, 1.0 / r[5], r[2], r[2]**2] for r in sel])   # drop cubic (small n)
    for tag, y in [("seam ", np.array([r[3] for r in sel])),
                   ("chiral", np.array([r[4] for r in sel]))]:
        beta, *_ = np.linalg.lstsq(Xh, y, rcond=None)
        yhat = Xh @ beta
        dof = max(len(y) - Xh.shape[1], 1)
        s2 = float(np.sum((y - yhat)**2) / dof)
        cov = s2 * np.linalg.inv(Xh.T @ Xh)
        se = np.sqrt(np.diag(cov))
        print(f"   {half} {tag}: a2 = {beta[3]:+.3f} +- {se[3]:.3f}")

print("\n== PD5: the ladder refit (all archived windows) ==")
allR = dict(RCERT); allR[1.5] = 0.4956
for k, v in R3.items():
    allR[k] = v["R"]
for k, v in SEED.items():
    allR[k] = v["R"]
for b_ in NEW:
    allR[NEW[b_]["lamp"]] = NEW[b_]["Rseam"]
allR[3.5] = float(z4["Rseam"][0]); allR[float(z4["lams"][1])] = float(z4["Rseam"][1])
allR[3.6] = float(z36["Rseam"][0]); allR[float(z36["lams"][1])] = float(z36["Rseam"][1])
lx = np.log(np.array(sorted(allR)))
ly = np.log(np.array([allR[k] for k in sorted(allR)]))
co = np.polyfit(lx, ly, 1)
print(f"   p = {-co[0]:.3f}   rms(log) = {np.std(ly - np.polyval(co, lx)):.3f}   "
      f"({len(allR)} windows, lam in [{min(allR):.2f}, {max(allR):.2f}])")

np.savez(HERE + "pinfG_profile_cubic_dense.npz",
         pairs=np.array([(r[0], r[1], r[2], r[3], r[4], r[5]) for r in rows]),
         ladder_lams=np.array(sorted(allR)),
         ladder_R=np.array([allR[k] for k in sorted(allR)]))
print("\nARCHIVED: pinfG_profile_cubic_dense.npz")
