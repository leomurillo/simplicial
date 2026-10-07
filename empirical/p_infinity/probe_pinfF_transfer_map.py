"""probe_pinfF_transfer_map.py -- the stationarity strike, step 1: the transfer map T written
explicitly and certified against the six measured windows.

THE MAP (P-inf-F section 23 target).  Center-out chain (Thm F.21); state after pair m = the
conditional future form Omega_m (Schur complement of the interior on the future); one step =
Schur conditioning at the leading pair.  Exact scalar shadow per parity sector (the LEVINSON
form, all quantities determinant ratios = basis-free, F64-5 compliant):

    d_{m+1} = d'_{m+1} - gt_m^2 / d_m = d'_{m+1} (1 - rho_m^2)

with d_m = current even-edge pivot, d'_{m+1} = next pair's skip-pivot (conditioned on the
interior but NOT on pair m), gt_m = innovation cross-covariance of consecutive edges,
rho_m = innovation correlation.  Ledger R_m = d_m / bare_m; eating per step splits EXACTLY:
    ln(R ratio) = ln(d'/d) [pace] + ln(1 - rho^2_eff) [correlation eating] + ln(bare ratio).
Joint saturation (the only CS-open failure mode) = rho^2_eff -> 1.

PRE-REGISTERED (GPD; fixed before the run):
  P1 (cross-implementation validation): final-edge Sigma-sigma in the SECTION-21 convention
      (stable-argsort order, mixed edge pair, identical bare) reproduces the quoted truths
      {1.5: 0.6509, 1.8: 0.7563, 2.0: 0.79919, 2.2: 0.86003, 2.35: 0.88671, 2.5: 0.91250}
      to 2e-3 (float-quoted 1.5/1.8) / 8e-4 (mp-quoted four).  FALSIFIER: any miss => my
      elimination is NOT the section-21 object; stop and diagnose before any map claim.
  P2 (LEDGER LOCALITY -- "T generates the six windows"): the lam=2.5 build's in-chain clean
      ledger Sigma_E(r), interpolated at the final clean radii of the five smaller builds,
      matches those builds' standalone clean finals within 0.08 absolute (lam_j = 1.5, 1.8)
      / 0.05 (lam_j = 2.0, 2.2, 2.35).  Expected deviation SIGN (registered): in-chain >=
      standalone (the big build's Fejer damping admits more prime weight at shared shifts).
      FALSIFIER: |delta| > 2x tolerance at any radius => one-chain reading of the six
      windows is wrong => the section-22.4 proof target needs re-coordinatization.
  P3 (the remainder law IN-CHAIN -- one kernel, one chain, no rebuilds): on the lam=2.5
      clean chain, ln R_E vs lambda^2 = e^{2r} over r >= ln 1.5 is linear with global slope
      -c_chain, c_chain in [0.222, 0.462] (0.342 +- 0.12); per-unit-lambda^2 eating
      fractions f in [0.18, 0.42] at every whole-unit interval.  FALSIFIER (creep mechanism
      in map coordinates): f increasing monotonically across >= 3 consecutive unit intervals
      by > 0.05 each.
  P4 (joint-saturation guard + the split): at every clean pair-step with r >= ln 1.5,
      rho^2_eff <= 0.75 (FALSIFIER: any rho^2_eff > 0.9 = single-step near-saturation, a
      danger the cumulative law hides).  Decomposition reported: pace share vs correlation
      share of c_chain.  Soft registered reading: pace carries >= 50% of the eating.
  P5 (instrument non-vacuity -- the map DETECTS the RH-false world): grafting the F.14
      off-line curvature signature DK(x,y) = amp*(x-y)^2*2cos(gamma0*(x-y)), gamma0 = 17.5
      (mid-gap), ||DK||_F = 2% ||K||_F, onto the lam=2.5 kernel produces R_graft(r) <
      R_clean(r) at each of the last 10 clean pairs (sign-only; magnitude reported).
      FALSIFIER: graft invisible => the ledger is structurally blind to off-line content
      and certifies nothing about RH.
  P6 (measurement, no falsifier -- the contraction trace): Thompson distances D_m between
      consecutive seam-relative even-sector J=6 conditional profiles (normalized by leading
      entry), reported along the chain; first empirical standing for the Birkhoff-Hopf
      part-(i) hypothesis (U).
  P0 (sanity, report): bare_E within [1.5, 2.4] along every chain (multiplier scale).

Machinery: certified mp builder (exec-import from probe_pinfF_wave_limit.py, dps set to 35
here: chain pivots stay >= 1e-4 at these windows -- no deep-mode inversions, forward
elimination only, the numerically stable direction); list-of-lists mp Gaussian elimination;
section-21-convention pass + clean reflection-pair pass per window; npz archive of profiles.
F64 rules: exact mp kernels (1); no per-rung spectral readings anywhere (5); alias-safe
grids inherited from the certified builder (4).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")

src = open("empirical/p_infinity/probe_pinfF_wave_limit.py", encoding="utf-8").read()
exec(src.split("def analyze")[0])          # primes_upto, build_QW_mp (certified lineage)
mp.mp.dps = 35

TARGETS = {1.5: 0.6509, 1.8: 0.7563, 2.0: 0.79919, 2.2: 0.86003, 2.35: 0.88671, 2.5: 0.91250}
TOL_P1 = {1.5: 2e-3, 1.8: 2e-3, 2.0: 8e-4, 2.2: 8e-4, 2.35: 8e-4, 2.5: 8e-4}
CASES = [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]


def build_point_kernel(lam, N):
    """Exact mp window Weil form in the point basis (mirrors wave_limit's analyze())."""
    Q, L = build_QW_mp(mp.mpf(repr(float(lam))), N)
    dim = 2 * N + 1
    B = mp.zeros(dim, dim)
    for n in range(dim):
        for i in range(dim):
            B[n, i] = mp.e**(2j * mp.pi * (n - N) * i / dim) / mp.sqrt(dim)
    K = (B.H) * Q * B
    Kr = [[(mp.re(K[i, j]) + mp.re(K[j, i])) / 2 for j in range(dim)] for i in range(dim)]
    return Kr, float(L)


def eliminate(A, act, k):
    """One Gaussian elimination step at point k over the active index list."""
    piv = A[k][k]
    Ak = A[k]
    for i in act:
        cik = A[i][k] / piv
        if cik:
            Ai = A[i]
            for j in act:
                Ai[j] -= cik * Ak[j]
    return


def sec21_pass(Kr, L, dim):
    """Section-21 convention: stable-argsort order, mixed edge pair; returns Sigma-sigma."""
    x = np.arange(dim) * L / dim
    s = np.abs(x - L / 2)
    order = list(np.argsort(s, kind="stable"))
    interior, pair = order[:dim - 2], order[dim - 2:]
    A = [row[:] for row in Kr]
    act = set(range(dim))
    for k in interior:
        act.discard(k)
        eliminate(A, act, k)
    p0, p1 = pair
    bare = (Kr[p0][p0] + Kr[p1][p1]) / 2 + Kr[p0][p1]
    d_edge = (A[p0][p0] + A[p1][p1]) / 2 + A[p0][p1]
    return float(1 - d_edge / bare)


def clean_chain(Kr, L, dim, lam, Jseam=6):
    """Clean reflection-pair chain: pairs (N+1-m, N+m), m=1..N, center-out; i=0 stays future.

    Returns per-pair records: radius, bare_E/O, d_E/O, skip-pivot, rho2 splits, identity
    residual, plus seam-relative J-block (float) for the Thompson trace."""
    N = (dim - 1) // 2
    dx = L / dim
    pairs = [(N + 1 - m, N + m) for m in range(1, N + 1)]
    A = [row[:] for row in Kr]
    act = set(range(dim))
    recs = []
    seam_blocks = []
    for m, (ia, ib) in enumerate(pairs, start=1):
        bareE = float((Kr[ia][ia] + Kr[ib][ib]) / 2 + Kr[ia][ib])
        bareO = float((Kr[ia][ia] + Kr[ib][ib]) / 2 - Kr[ia][ib])
        dE = (A[ia][ia] + A[ib][ib]) / 2 + A[ia][ib]
        dO = (A[ia][ia] + A[ib][ib]) / 2 - A[ia][ib]
        rec = dict(m=m, r=(m - 0.5) * dx, bareE=bareE, bareO=bareO,
                   dE=float(dE), dO=float(dO))
        if m < N:
            ja, jb = pairs[m]
            d2E = (A[ja][ja] + A[jb][jb]) / 2 + A[ja][jb]          # skip-pivot d'
            gE = (A[ia][ja] + A[ia][jb] + A[ib][ja] + A[ib][jb]) / 2   # E_m -- E_{m+1}
            lEO = (A[ia][ja] + A[ia][jb] - A[ib][ja] - A[ib][jb]) / 2  # O_m -- E_{m+1}
            cEO = (A[ia][ia] - A[ib][ib]) / 2                          # E_m -- O_m
            det = dE * dO - cEO * cEO
            eat = (gE * (dO * gE - cEO * lEO) + lEO * (dE * lEO - cEO * gE)) / det
            dE_next_pred = d2E - eat
            rec.update(d2E=float(d2E), rho2_EE=float(gE * gE / (dE * d2E)),
                       rho2_eff=float(eat / d2E), pred_next=float(dE_next_pred))
        # seam-relative even-sector J-block on the NEXT J pairs (before eliminating pair m
        # it would include pair m; convention: read AFTER eliminating pair m, below)
        eliminate(A, act := act - {ia}, ia)
        eliminate(A, act := act - {ib}, ib)
        J = min(Jseam, N - m)
        if J >= 2:
            W = np.zeros((J, J))
            for a in range(J):
                pa, pb = pairs[m + a]
                for b in range(a, J):
                    qa, qb = pairs[m + b]
                    W[a, b] = W[b, a] = float((A[pa][qa] + A[pa][qb]
                                               + A[pb][qa] + A[pb][qb]) / 2)
            seam_blocks.append((m, W))
        recs.append(rec)
    # identity check: predicted next even pivot vs directly-read next even pivot
    for k in range(len(recs) - 1):
        if "pred_next" in recs[k]:
            recs[k]["ident_res"] = abs(recs[k]["pred_next"] - recs[k + 1]["dE"]) / recs[k + 1]["bareE"]
    return recs, seam_blocks


def thompson(W0, W1):
    """Thompson distance between leading-entry-normalized SPD blocks of equal size."""
    from scipy.linalg import eigh
    A0, A1 = W0 / W0[0, 0], W1 / W1[0, 0]
    ev = eigh(A1, A0, eigvals_only=True)
    ev = ev[ev > 0]
    return float(np.max(np.abs(np.log(ev)))) if len(ev) else float("nan")


print("== building + running the six chains (mp dps=35) ==")
results = {}
for lam, N in CASES:
    t0 = time.time()
    Kr, L = build_point_kernel(lam, N)
    dim = 2 * N + 1
    sig21 = sec21_pass(Kr, L, dim)
    recs, seams = clean_chain(Kr, L, dim, lam)
    results[lam] = dict(L=L, dim=dim, sig21=sig21, recs=recs, seams=seams, Kr=Kr)
    fin = recs[-1]
    print(f"   lam={lam} (dim={dim}, {time.time()-t0:.0f}s): sec21 Sigma={sig21:.5f} "
          f"(target {TARGETS[lam]:.5f}); clean final r={fin['r']:.3f} "
          f"Sigma_E={1-fin['dE']/fin['bareE']:.5f} R_E={fin['dE']/fin['bareE']:.4e} "
          f"R_O={fin['dO']/fin['bareO']:.4e}")

print("\n== P1: cross-implementation validation (section-21 convention) ==")
p1 = True
for lam, _ in CASES:
    diff = abs(results[lam]["sig21"] - TARGETS[lam])
    ok = diff <= TOL_P1[lam]
    p1 &= ok
    print(f"   lam={lam}: Sigma21={results[lam]['sig21']:.5f}  target={TARGETS[lam]:.5f}  "
          f"|diff|={diff:.1e}  {'ok' if ok else 'MISS'}")
print("   P1: " + ("SURVIVES -- the elimination IS the section-21 object" if p1
                   else "FIRED -- diagnose before any map claim"))

print("\n== P0: bare scale along the clean chains ==")
p0 = True
for lam, _ in CASES:
    bs = [rec["bareE"] for rec in results[lam]["recs"]]
    p0 &= (min(bs) >= 1.5) and (max(bs) <= 2.4)
    print(f"   lam={lam}: bare_E in [{min(bs):.3f}, {max(bs):.3f}]")
print("   P0: " + ("ok -- multiplier scale" if p0 else "outside band -- report"))

print("\n== P2: ledger locality (in-chain of lam=2.5 vs standalone clean finals) ==")
big = results[2.5]
rs = np.array([rec["r"] for rec in big["recs"]])
SE = np.array([1 - rec["dE"] / rec["bareE"] for rec in big["recs"]])
p2 = True
print("   lam_j   r_final   standalone Sigma_E   in-chain Sigma_E(r)   delta   tol")
for lam, _ in CASES[:-1]:
    fin = results[lam]["recs"][-1]
    r_j = fin["r"]
    s_j = 1 - fin["dE"] / fin["bareE"]
    s_in = float(np.interp(r_j, rs, SE))
    tol = 0.08 if lam <= 1.8 else 0.05
    d_ = s_in - s_j
    ok = abs(d_) <= 2 * tol
    within = abs(d_) <= tol
    p2 &= ok
    print(f"   {lam:4}   {r_j:.4f}    {s_j:.5f}              {s_in:.5f}            "
          f"{d_:+.4f}  {tol}  {'ok' if within else ('soft-miss' if ok else 'FALSIFIED')}")
print("   P2: " + ("SURVIVES (within falsifier bound) -- one chain generates the windows"
                   if p2 else "FIRED -- one-chain reading wrong; re-coordinatize"))

print("\n== P3: the remainder law in-chain (lam=2.5 chain, r >= ln 1.5) ==")
mask = rs >= np.log(1.5)
lam2 = np.exp(2 * rs[mask])
RE = np.array([rec["dE"] / rec["bareE"] for rec in big["recs"]])[mask]
cfit = np.polyfit(lam2, np.log(RE), 1)
c_chain = -cfit[0]
# per-unit-lambda^2 eating fractions at whole-unit checkpoints
l2grid = np.arange(np.ceil(lam2.min()), np.floor(lam2.max()) + 0.001, 1.0)
Rgrid = np.exp(np.interp(l2grid, lam2, np.log(RE)))
fs = 1 - Rgrid[1:] / Rgrid[:-1]
print(f"   global fit: c_chain = {c_chain:.3f}   (band [0.222, 0.462]; cross-window mp 0.342)")
print("   unit-interval eating fractions f: "
      + "  ".join(f"[{a:.0f}->{a+1:.0f}]:{f_:.3f}" for a, f_ in zip(l2grid[:-1], fs)))
resid = np.log(RE) - np.polyval(cfit, lam2)
print(f"   fit residual rms = {np.sqrt(np.mean(resid**2)):.3f} (log units)")
inc = np.diff(fs)
creep = any(all(inc[i + k] > 0.05 for k in range(3)) for i in range(max(0, len(inc) - 2)))
p3 = (0.222 <= c_chain <= 0.462) and all(0.18 <= f_ <= 0.42 for f_ in fs) and not creep
also = []
for lam in (2.2, 2.35):
    rr = np.array([rec["r"] for rec in results[lam]["recs"]])
    mE = np.array([rec["dE"] / rec["bareE"] for rec in results[lam]["recs"]])
    mk = rr >= np.log(1.5)
    cf = np.polyfit(np.exp(2 * rr[mk]), np.log(mE[mk]), 1)
    also.append((lam, -cf[0]))
print("   consistency (in-chain c of smaller builds): "
      + "  ".join(f"lam={l}: {c:.3f}" for l, c in also))
print("   P3: " + ("SURVIVES -- the law is generated by the map's own iteration"
                   if p3 else "FIRED/CHECK -- see numbers"))

print("\n== P4: joint-saturation guard + the eating decomposition ==")
p4 = True
worst = 0.0
pace_tot, corr_tot, n_steps = 0.0, 0.0, 0
for rec, nxt in zip(big["recs"][:-1], big["recs"][1:]):
    if rec["r"] < np.log(1.5) or "rho2_eff" not in rec:
        continue
    worst = max(worst, rec["rho2_eff"])
    p4 &= rec["rho2_eff"] <= 0.9
    pace_tot += np.log(rec["d2E"] / rec["dE"])
    corr_tot += np.log(1 - rec["rho2_eff"])
    n_steps += 1
ident = max(rec.get("ident_res", 0.0) for rec in big["recs"])
print(f"   identity residual (Levinson prediction vs direct read): max = {ident:.2e}")
print(f"   max rho^2_eff over law regime = {worst:.3f}   (guard 0.75; falsifier 0.9)")
tot = pace_tot + corr_tot
print(f"   eating decomposition over the law regime: pace sum = {pace_tot:+.3f}, "
      f"correlation sum = {corr_tot:+.3f}  (total {tot:+.3f}; "
      f"shares {abs(pace_tot)/max(abs(pace_tot)+abs(corr_tot),1e-12):.2f}/"
      f"{abs(corr_tot)/max(abs(pace_tot)+abs(corr_tot),1e-12):.2f})")
p4 &= worst <= 0.75 and ident < 1e-20
print("   P4: " + ("SURVIVES -- no single step approaches saturation; split measured"
                   if p4 else "FIRED -- see worst step / identity"))

print("\n== P5: the graft test (F.14 off-line curvature signature, sign-only) ==")
lam, N = 2.5, 32
Kr, L = big["Kr"], big["L"]
dim = 2 * N + 1
x = [i * L / dim for i in range(dim)]
nrmK = np.sqrt(sum(float(Kr[i][j])**2 for i in range(dim) for j in range(dim)))
raw = [[(x[i] - x[j])**2 * 2 * np.cos(17.5 * (x[i] - x[j])) for j in range(dim)]
       for i in range(dim)]
nrmG = np.sqrt(sum(raw[i][j]**2 for i in range(dim) for j in range(dim)))
amp = 0.02 * nrmK / nrmG
Kg = [[Kr[i][j] + mp.mpf(repr(amp * raw[i][j])) for j in range(dim)] for i in range(dim)]
recg, _ = clean_chain(Kg, L, dim, lam, Jseam=2)
REc = [rec["dE"] / rec["bareE"] for rec in big["recs"]]
REg = [rec["dE"] / rec["bareE"] for rec in recg]
last10 = list(range(len(REc) - 10, len(REc)))
sign_ok = all(REg[i] < REc[i] for i in last10)
mag = np.mean([1 - REg[i] / REc[i] for i in last10])
print(f"   graft: gamma0=17.5, ||DK||_F/||K||_F = 0.02, amp={amp:.3e}")
print("   last-10 clean pairs: R_graft < R_clean at "
      + f"{sum(REg[i] < REc[i] for i in last10)}/10; mean R-deficit = {mag:+.3f}")
neg = [i for i, rec in enumerate(recg) if rec["dE"] < 0 or rec["dO"] < 0]
print(f"   grafted-chain negative pivots: {len(neg)}"
      + (f" (first at pair {neg[0]+1}, r={recg[neg[0]]['r']:.3f})" if neg else ""))
p5 = sign_ok
print("   P5: " + ("SURVIVES -- the ledger SEES the off-line signature (non-vacuous)"
                   if p5 else "FIRED -- instrument blind; certificate void"))

print("\n== P6: the contraction trace (Thompson distances, seam-relative J=6 blocks) ==")
for lam in (2.0, 2.5):
    sb = results[lam]["seams"]
    Ds = []
    for (m0, W0), (m1, W1) in zip(sb[:-1], sb[1:]):
        if W0.shape == W1.shape and W0.shape[0] == 6:
            Ds.append((m1, thompson(W0, W1)))
    msk = [(m, D) for m, D in Ds if (m - 0.5) * results[lam]["L"] / results[lam]["dim"] >= np.log(1.4)]
    print(f"   lam={lam}: D_m sequence (law regime): "
          + "  ".join(f"m={m}:{D:.3f}" for m, D in msk))
print("   P6: measurement logged (the part-(i) hypothesis (U)'s first empirical standing)")

np.savez("empirical/p_infinity/transfer_map_profiles.npz",
         **{f"r{lam}": np.array([rec["r"] for rec in results[lam]["recs"]]) for lam, _ in CASES},
         **{f"RE{lam}": np.array([rec["dE"] / rec["bareE"] for rec in results[lam]["recs"]])
            for lam, _ in CASES},
         **{f"RO{lam}": np.array([rec["dO"] / rec["bareO"] for rec in results[lam]["recs"]])
            for lam, _ in CASES})

verdict = p1 and p2 and p3 and p4 and p5
print("\nRESULT: " + ("GREEN -- T written, certified as the generator of the six windows; "
                      "law + split + guard + detection all in band"
                      if verdict else "PARTIAL -- see fired blocks above (diagnose per GPD)"))
