"""probe_pinfG_increment_bound.py -- P-inf-G round 3: the increment-bound instrument
(Leo's redirect, 2026-06-13: DROP the discrimination proxy -- the resummed object, like
every finite-window object, is RH-unconditional; its value is the EXACT PER-ARRIVAL
INCREMENT, which is the open step's literal content ("the increment stays bounded below
the remainder, forever" = (U) directly), with Theorem G.5's square-positive gearing
doing the sign-bookkeeping through the one chiral scalar.)

THE INSTRUMENT.  The v2 run built true kernels at lam'^2 = lam^2 + 1, giving FIVE EXACT
unit-lambda^2 pairs with BOTH endpoints inside the cone (true-to-true, no mixed base):
(1.8 -> 2.0591), (2.0 -> 2.2361), (2.2 -> 2.4166), (2.35 -> 2.5539), (2.5 -> 2.6926).
This probe computes, per pair and channel:
  (1) the exact per-arrival increments of d_0 (seam), d_- (chiral edge), d_+ (even
      edge), E = d_std - d_0/2 (the certified excess) -- certified-observable
      coordinates only (F64-5);
  (2) the G.5 gearing split  Delta E = kappa~(lam') Delta d_-  +  d_-(lam) Delta kappa~,
      kappa~ = (d_+ + G)^2/(d_+ (d_+ + d_-)) >= 0 manifest;
  (3) the (U)-band: eating fractions f_ch = 1 - d_ch(lam')/d_ch(lam) and margins 1 - f
      across the five arrival phases; oddshare at the five NEW windows (G.5.2's
      registered plateau prediction, tested now);
  (4) the cone margin along the arrival direction: the swap-path boundary crossing t*
      (bisection between PSD t=1 and the G.4'-certified non-PSD t=0), m* = 1 - t* in
      one-arrival units -- the quantitative refinement of Prop G.4'.

PRE-REGISTERED (GPD; locked before the run; per the two-regime lesson NO RH-falsifier
is possible at finite window -- rules below target instrument/lawfulness claims):
  L1 (lineage): rebuilt lam'-window pivots (seam R, odd, even) match the v2 npz values
      to <= 1e-10 relative.  Fired -> build drift: HALT.
  N1 (gearing identities): E = kappa~ d_- at each lam' window <= 1e-25 (mp); the
      Leibniz split of Delta E exact <= 1e-10 (float pairs).  Fired -> algebra bug.
  N2 (the plateau, G.5.2's first test): oddshare at the five new windows inside
      [0.20, 0.34] (certified band [0.24, 0.30] +- 0.04).  OUTSIDE at any window ->
      finding: the plateau bends at interleaved phases (if trending DOWN -> chiral-
      marginality alert; report either way).
  N3 (massive-cell law): per-pair c_{+-} = -Delta ln d_{+-} per unit lambda^2 inside
      [1.8, 3.8] (certified per-pair band 2.15-3.10 widened).  Fired -> the edge law
      breaks at interleaved phases (finding).
  N4 (seam law, densified): 11-point R_0 series (6 certified + 5 new) global power-law
      fit p reported with residuals; per-pair slopes vs p/(2 lambda-bar^2).
  N5 (THE HEADLINE TABLE -- the increment below the remainder): per pair and channel,
      f and margin 1 - f; the seam margin must not collapse monotonically toward 0
      across the five phases (it is predicted to GROW as f ~ p/(2 lambda^2) slides).
  N6 (the arrival-direction cone margin, reading): t*(lam') by 28-step bisection,
      m* = 1 - t*; bracket validity = Cholesky PSD at t=1 and non-PSD at t=0 (G.4');
      the law of m* in lambda reported (expected to track the exp-small ladder; new
      measurable either way).

Machinery: v2 lineage exec-imported (builder, bands, channel_parts, to_point); dps 65;
certified 6-window observables loaded from parity_totals.npz (mp-certified at V6/V7).
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

SMOKE = "--smoke" in sys.argv
DPS = 35 if SMOKE else 65
mp.mp.dps = DPS

PAIRS = [1.8, 2.0, 2.2, 2.35, 2.5]
if SMOKE:
    PAIRS = [2.0]

# certified six windows (mp-certified at V6/V7 in parity_totals)
zc = np.load(HERE + "parity_totals.npz")
CERT = {float(l): dict(dp=zc["d_plus"][i], dm=zc["d_minus"][i], gam=zc["gamma"][i],
                       v0=zc["v0"][i], d0=zc["d0"][i], dstd=zc["d_std"][i])
        for i, l in enumerate(zc["lams"])}
zv = np.load(HERE + "pinfG_cubic_drift_v2.npz")
V2 = {float(l): dict(Rseam=zv["Rseam"][i],
                     d_odd=zv["d_true"][i][0], d_even=zv["d_true"][i][1],
                     d_seam=zv["d_true"][i][2])
      for i, l in enumerate(zv["lams"])}


def schur_solve(A, rhs_list):
    sols = [mp.lu_solve(A, b) for b in rhs_list]
    n = A.rows
    return [[mp.fsum(rhs_list[a][i] * sols[b2][i] for i in range(n))
             for b2 in range(len(rhs_list))] for a in range(len(rhs_list))]


def bridge_observables(K, dim):
    """The full F.27/G.5 observable set from one kernel (mp; parity-aligned frame)."""
    d_ = dim
    m = (dim - 1) // 2
    sq2 = mp.sqrt(2)
    idx = list(range(2, m + 1))
    ni = len(idx)
    Mp = mp.zeros(ni, ni)
    Mm = mp.zeros(ni, ni)
    qp = mp.matrix(ni, 1)
    qm = mp.matrix(ni, 1)
    w0 = mp.matrix(ni, 1)
    for a_, k in enumerate(idx):
        qp[a_] = (K[k, 1] + K[k, d_ - 1] + K[d_ - k, 1] + K[d_ - k, d_ - 1]) / 2
        qm[a_] = (K[k, 1] - K[k, d_ - 1] - K[d_ - k, 1] + K[d_ - k, d_ - 1]) / 2
        w0[a_] = (K[k, 0] + K[d_ - k, 0]) / sq2
        for b_, l in enumerate(idx):
            Mp[a_, b_] = (K[k, l] + K[k, d_ - l] + K[d_ - k, l] + K[d_ - k, d_ - l]) / 2
            Mm[a_, b_] = (K[k, l] - K[k, d_ - l] - K[d_ - k, l] + K[d_ - k, d_ - l]) / 2
    bare_p = (K[1, 1] + K[1, d_ - 1] + K[d_ - 1, 1] + K[d_ - 1, d_ - 1]) / 2
    bare_m = (K[1, 1] - K[1, d_ - 1] - K[d_ - 1, 1] + K[d_ - 1, d_ - 1]) / 2
    GP = schur_solve(Mp, [qp, w0])
    QM = schur_solve(Mm, [qm])[0][0]
    d_plus = bare_p - GP[0][0]
    d_minus = bare_m - QM
    c01 = (K[0, 1] + K[0, d_ - 1]) / sq2
    gamma = c01 - GP[0][1]
    v0 = K[0, 0] - GP[1][1]
    d0 = v0 - gamma**2 / d_plus
    d0_direct = direct_pivot(K, dim, "seam")
    # standard cut edge pair (certified convention)
    # geometry: x_i = i L/dim, s = |x - L/2|; edge = two largest s = {0, wrap-neighbour}
    order = np.argsort(np.abs(np.arange(dim) - dim / 2.0) * -1, kind="stable")
    # equivalent index-only construction (avoids L): s_i = |i - dim/2| max at i=0? no --
    # use the certified construction explicitly:
    xs = np.arange(dim) / dim          # x/L
    s = np.abs(xs - 0.5)
    od = np.argsort(s, kind="stable")
    pair = [int(i) for i in od[dim - 2:]]
    interior = [int(i) for i in od[:dim - 2]]
    sq2_ = sq2
    p0_, p1_ = pair
    bare = (K[p0_, p0_] + K[p1_, p1_]) / 2 + K[p0_, p1_]
    Aint = mp.zeros(dim - 2, dim - 2)
    q = mp.matrix(dim - 2, 1)
    for a_, i in enumerate(interior):
        q[a_] = (K[i, p0_] + K[i, p1_]) / sq2_
        for b_, j in enumerate(interior):
            Aint[a_, b_] = K[i, j]
    d_std = bare - schur_solve(Aint, [q])[0][0]
    G_ = gamma / sq2
    kap = (d_plus + G_)**2 / (d_plus * (d_plus + d_minus))
    E = d_std - d0 / 2
    return dict(dp=d_plus, dm=d_minus, gam=gamma, v0=v0, d0=d0, d0x=d0_direct,
                dstd=d_std, G=G_, kap=kap, E=E, K00=K[0, 0],
                oddshare=float(E / d_std))


def tstar_bisect(K_true, KA, KS, dim, iters=28):
    """Boundary crossing of K(t) = K_true + (1-t)(KA - KS); PSD at t=1, non-PSD at 0."""
    D = KA - KS
    lo, hi = mp.mpf(0), mp.mpf(1)
    if cholesky_psd(K_true + D):           # t = 0
        return None, "t0-PSD"              # bracket invalid (would contradict G.4')
    if not cholesky_psd(K_true):
        return None, "t1-nonPSD"
    for _ in range(iters):
        mid = (lo + hi) / 2
        if cholesky_psd(K_true + (1 - mid) * D):
            hi = mid
        else:
            lo = mid
    return float((lo + hi) / 2), "ok"


print(f"== P-inf-G round 3: the increment-bound instrument (dps={DPS}) ==")
print("   five exact unit-lambda^2 pairs, true-to-true; G.5 gearing; (U)-band\n")

NEW = {}
for lam in PAIRS:
    t0 = time.time()
    W = build_window(lam, Np=(12 if SMOKE else None))
    dim = W["dim"]
    ob = bridge_observables(W["K_true"], dim)
    cons = float(abs(ob["d0"] - ob["d0x"]) / abs(ob["d0x"]))
    ident = float(abs(ob["E"] - ob["kap"] * ob["dm"]) / abs(ob["E"]))
    ts, flag = tstar_bisect(W["K_true"], W["KA"], W["KS"], dim)
    NEW[lam] = dict(lamp=float(W["lamp"]), ob=ob, cons=cons, ident=ident,
                    tstar=ts, tflag=flag,
                    Rseam=float(ob["d0x"] / ob["K00"]))
    print(f"   lam'={float(W['lamp']):.5f} (dim={dim}, {time.time()-t0:.0f}s): "
          f"d-={float(ob['dm']):.4e} d+={float(ob['dp']):.4e} d0={float(ob['d0x']):.4e} "
          f"E={float(ob['E']):.4e}")
    print(f"      oddshare={ob['oddshare']:.4f}  kappa~={float(ob['kap']):.4f}  "
          f"E=kap*d- ident={ident:.1e}  d0-consistency={cons:.1e}")
    print(f"      t* = {ts if ts is None else f'{ts:.6f}'} ({flag})  ->  m* = "
          f"{'n/a' if ts is None else f'{1-ts:.3e}'}")

if SMOKE:
    print("\nSMOKE OK")
    sys.exit(0)

# ---------------------------------------------------------------- L1 lineage
print("\n== L1: lineage vs the v2 archive ==")
l1 = True
for lam in PAIRS:
    r1 = abs(NEW[lam]["Rseam"] - V2[lam]["Rseam"]) / V2[lam]["Rseam"]
    r2 = abs(float(NEW[lam]["ob"]["dm"]) - V2[lam]["d_odd"]) / V2[lam]["d_odd"]
    r3 = abs(float(NEW[lam]["ob"]["dp"]) - V2[lam]["d_even"]) / V2[lam]["d_even"]
    ok = max(r1, r2, r3) <= 1e-10
    l1 &= ok
    print(f"   lam'={NEW[lam]['lamp']:.4f}: dR={r1:.1e} dd-={r2:.1e} dd+={r3:.1e}  "
          + ("ok" if ok else "MISS"))
print("   L1: " + ("SURVIVES" if l1 else "FIRED -- build drift, HALT"))

# ---------------------------------------------------------------- N1 gearing
print("\n== N1: G.5 gearing identities ==")
n1 = all(NEW[lam]["ident"] <= 1e-25 for lam in PAIRS)
print(f"   E = kappa~ d- at lam' windows: max rel = "
      f"{max(NEW[lam]['ident'] for lam in PAIRS):.1e}"
      + ("   SURVIVES" if n1 else "   FIRED"))

# the pairs table: increments + gearing split (float grade: certified side is float64)
print("\n== THE PAIRS: exact per-arrival increments and the gearing split ==")
print("   pair             dd-          dd+          dd0          dE          "
      "kap'*dd-     d-*dkap      split-resid")
n1b = True
rows = []
for lam in PAIRS:
    A, B = CERT[lam], NEW[lam]["ob"]
    Gc = A["gam"] / np.sqrt(2)
    kapc = (A["dp"] + Gc)**2 / (A["dp"] * (A["dp"] + A["dm"]))
    Ec = A["dstd"] - A["d0"] / 2
    ddm = float(B["dm"]) - A["dm"]
    ddp = float(B["dp"]) - A["dp"]
    dd0 = float(B["d0x"]) - A["d0"]
    dE = float(B["E"]) - Ec
    t1 = float(B["kap"]) * ddm
    t2 = A["dm"] * (float(B["kap"]) - kapc)
    resid = abs(dE - (t1 + t2)) / abs(dE)
    n1b &= resid <= 1e-10
    rows.append((lam, ddm, ddp, dd0, dE, t1, t2, kapc, Ec))
    print(f"   {lam:4}->{NEW[lam]['lamp']:.3f}  {ddm:+.3e}  {ddp:+.3e}  {dd0:+.3e}  "
          f"{dE:+.3e}  {t1:+.3e}  {t2:+.3e}  {resid:.1e}")
print("   N1b (Leibniz split exact): " + ("SURVIVES" if n1b else "FIRED -- algebra bug"))

# ---------------------------------------------------------------- N2 plateau
print("\n== N2: the oddshare plateau at the five NEW windows (G.5.2 first test) ==")
n2 = True
for lam in PAIRS:
    os_ = NEW[lam]["ob"]["oddshare"]
    inside = 0.20 <= os_ <= 0.34
    n2 &= inside
    print(f"   lam'={NEW[lam]['lamp']:.4f}: oddshare = {os_:.4f}  "
          + ("inside [0.20, 0.34]" if inside else "OUTSIDE -- finding"))
print("   N2: " + ("SURVIVES -- plateau extends to the interleaved windows"
                   if n2 else "FIRED -- plateau bends (report; check trend)"))

# ---------------------------------------------------------------- N3/N5 the (U)-band
print("\n== N3/N5: eating fractions and margins per channel (THE (U)-BAND) ==")
print("   pair             f_-      f_+      f_0      f_E     | margins: 1-f_-   1-f_0")
n3 = True
for lam, ddm, ddp, dd0, dE, t1, t2, kapc, Ec in rows:
    A, B = CERT[lam], NEW[lam]["ob"]
    fm = 1 - float(B["dm"]) / A["dm"]
    fp = 1 - float(B["dp"]) / A["dp"]
    f0 = 1 - float(B["d0x"]) / A["d0"]
    fE = 1 - float(B["E"]) / Ec
    cm, cp = -np.log(1 - fm), -np.log(1 - fp)
    ok = 1.8 <= cm <= 3.8 and 1.8 <= cp <= 3.8
    n3 &= ok
    print(f"   {lam:4}->{NEW[lam]['lamp']:.3f}  {fm:.4f}  {fp:.4f}  {f0:.4f}  {fE:.4f} |"
          f"   {1-fm:.4f}   {1-f0:.4f}   (c-={cm:.2f}, c+={cp:.2f}"
          + ("" if ok else " <- N3 OUTSIDE") + ")")
print("   N3 (massive-cell law at interleaved phases): " + ("SURVIVES" if n3 else "FIRED (finding)"))

# ---------------------------------------------------------------- N4 seam law densified
print("\n== N4: the densified seam ladder (11 windows) ==")
R_cert = {1.5: 0.4956, 1.8: 0.2884, 2.0: 0.2064, 2.2: 0.1496, 2.35: 0.1130, 2.5: 0.0922}
allpts = sorted([(l, R_cert[l]) for l in R_cert] +
                [(NEW[lam]["lamp"], NEW[lam]["Rseam"]) for lam in PAIRS])
lx = np.log([p[0] for p in allpts])
ly = np.log([p[1] for p in allpts])
co = np.polyfit(lx, ly, 1)
p_fit = -co[0]
resid = ly - np.polyval(co, lx)
print(f"   global power-law fit over 11 windows: p = {p_fit:.3f}  rms(log) = {np.std(resid):.3f}")
for (l, R), rs in zip(allpts, resid):
    print(f"      lam={l:.4f}  R_seam={R:.5f}  dev={np.expm1(rs)*100:+.1f}%")
print("   per-pair seam slopes vs p/(2 lam-bar^2):")
for lam, *_ in rows:
    lp = NEW[lam]["lamp"]
    sl = -np.log(NEW[lam]["Rseam"] / R_cert[lam])      # per unit lambda^2 (exact unit step)
    lb2 = (lam**2 + lp**2) / 2
    print(f"      {lam:4}->{lp:.3f}: slope = {sl:.3f}   p/(2 lb^2) = {p_fit/(2*lb2):.3f}")

# ---------------------------------------------------------------- N6 cone margin
print("\n== N6: the arrival-direction cone margin m* = 1 - t* ==")
for lam in PAIRS:
    ts, flag = NEW[lam]["tstar"], NEW[lam]["tflag"]
    if ts is None:
        print(f"   lam'={NEW[lam]['lamp']:.4f}: bracket invalid ({flag}) -- report")
    else:
        print(f"   lam'={NEW[lam]['lamp']:.4f}: t* = {ts:.7f}   m* = {1-ts:.4e}")
mstars = [(NEW[lam]["lamp"], 1 - NEW[lam]["tstar"]) for lam in PAIRS
          if NEW[lam]["tstar"] is not None]
if len(mstars) >= 3:
    mx = np.log([m[0] for m in mstars])
    my = np.log([m[1] for m in mstars])
    cm_ = np.polyfit(mx, my, 1)
    print(f"   m* power-law reading: m* ~ lam^{cm_[0]:.2f}  (rms {np.std(my-np.polyval(cm_,mx)):.3f})")
    # against the ladder: certified eps at nearest windows for pace comparison
    print("   (pace context: the Fuchs ladder falls ~5-7 decades over the same span)")

np.savez(HERE + "pinfG_increment_bound.npz",
         lams=np.array(PAIRS),
         lamps=np.array([NEW[l]["lamp"] for l in PAIRS]),
         dm_new=np.array([float(NEW[l]["ob"]["dm"]) for l in PAIRS]),
         dp_new=np.array([float(NEW[l]["ob"]["dp"]) for l in PAIRS]),
         d0_new=np.array([float(NEW[l]["ob"]["d0x"]) for l in PAIRS]),
         E_new=np.array([float(NEW[l]["ob"]["E"]) for l in PAIRS]),
         kap_new=np.array([float(NEW[l]["ob"]["kap"]) for l in PAIRS]),
         gam_new=np.array([float(NEW[l]["ob"]["gam"]) for l in PAIRS]),
         v0_new=np.array([float(NEW[l]["ob"]["v0"]) for l in PAIRS]),
         dstd_new=np.array([float(NEW[l]["ob"]["dstd"]) for l in PAIRS]),
         oddshare_new=np.array([NEW[l]["ob"]["oddshare"] for l in PAIRS]),
         Rseam_new=np.array([NEW[l]["Rseam"] for l in PAIRS]),
         tstar=np.array([NEW[l]["tstar"] if NEW[l]["tstar"] is not None else np.nan
                         for l in PAIRS]),
         p_fit=np.array([p_fit]))
print("\nARCHIVED: pinfG_increment_bound.npz")
ok = l1 and n1 and n1b
print("RESULT: " + ("GREEN -- instrument valid; the (U)-band tables above are the deliverable"
                    if ok else "FIRED/PARTIAL -- see L1/N1 (diagnose before reading)"))
