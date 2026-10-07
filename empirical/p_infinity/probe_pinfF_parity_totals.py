"""probe_pinfF_parity_totals.py -- the invariant branch decomposition of the eating law
(P-inf-F section 23 target).

CONTEXT (P-inf-F sections 19-22 + the invariance audit): RH <=> d(s) > 0 <=> R(s) > 0 in
chain coordinates; remainder law R ~ C e^{-c lambda^2}, c = 0.342 (mp dps-50, six windows);
ladder self-similarity = TWO parity branches (D1: dispersion 0.107 even / 0.019 odd vs
0.79 mixed).  The first-draft branch closure "(1-0.25)(1-0.06) = 0.705" was RETRACTED by
the invariance audit (per-rung bin-means + a migrating ladder boundary).  THIS probe
computes the branch decomposition in the INVARIANT coordinate: parity-resolved TOTAL
cumulatives -- quadratic forms q_p^T K_int^{-1} q_p -- no eigenvalue boundary anywhere
(F64-5 compliant: spectral functions / quadratic forms only, no per-rung quantities).

THE GRID DEFECT (step zero): the DFT point grid x_i = iL/dim (dim odd) has reflection
i -> (dim-i) mod dim with i=0 fixed; the standard chain cut (interior = all minus the
outermost pair {0, dim-1}) is NOT reflection-closed: exactly one interior point (the
orphan, generically grid index 1) has its reflection partner inside the edge pair.
Handled in three layers:
  (1) full-grid reflection invariance of K is EXACT (kernel symmetry: Toeplitz part even,
      pole pair swaps as a set, arch kernel even) -- certified numerically per window;
  (2) the standard ledger splits into channels e/o/orphan + crosses -- ALL measured;
      the standard cut differs from the parity-aligned cut by a ONE-COORDINATE (orphan)
      bordering, so all parity pollution is explicitly quantified;
  (3) the PARITY-ALIGNED chain (edge cell = the symmetric pair {1, dim-1} over the
      reflection-closed interior {2..dim-2}; wrap point i=0 as its own final cell)
      decouples EXACTLY into two independent sub-chains (even and odd) -- the invariant
      two-branch object; branch-own remainder laws c_plus / c_minus are new measurables.

PRE-REGISTERED (GPD; tolerances locked BEFORE the run):
  V1: Sigma-sigma at mp windows matches the dps-50 truths (0.7992/0.8600/0.8867/0.9125
      at lam = 2.0/2.2/2.35/2.5) within 0.5%.
  V2: float windows match 0.6509/0.7563 (lam = 1.5/1.8) within 0.5%.
  V3: channel-sum identity |sum_ab S_ab - Sigma-sigma| <= 1e-8 (mp) / 1e-10 (float-lift).
  V4 (float windows only): standard-chain pivot weld p1*p2 = d_plus*d_minus and
      p3 = d_0, relative <= 1e-4 (ties the aligned frame to the certified chain lineage).
  V5: c_glob (fresh refit of -dlnR_std/dlambda^2 over the six windows) within 0.06
      of 0.342.
  V6 (wrap consistency): d_0 computed two ways -- directly (Schur over everything) and
      via the aligned frame (v_0 - gamma^2/d_plus, where gamma = Cov(delta_0, E_1 | int'),
      v_0 = Var(delta_0 | int')) -- relative <= 1e-6.
  V7 (THE BRIDGE IDENTITY, derived pre-run from exact parity decoupling): with
      t = delta_0/sqrt2 + (E_1 +- O_1)/2 (= e_std) and u = the orphan direction,
        d_std = Var(t|int') - Cov(t,u|int')^2 / Var(u|int'),
        Var(t) = v_0/2 + (d_+ + d_-)/4 + gamma/sqrt2,
        Cov(t,u) = [(d_+ - d_-)/2 + gamma/sqrt2]/sqrt2,   Var(u) = (d_+ + d_-)/2,
      orientation-independent; relative <= 1e-6 at every window.  COROLLARY (the
      pre-registered structural prediction): d_std -> d_0/2 as d_- -> 0 -- the certified
      remainder law's carrier migrates onto the WRAP-CELL (even-sector) innovation, and
      the invariant branch decomposition of the eating law is ADDITIVE in remainders,
      d_std = d_0/2 + kappa * d_- + O(d_-^2),  kappa = 1/4 + (A/2+G)(3A/2+G)/A^2,
      (A = d_+, G = gamma/sqrt2), NOT multiplicative in eating fractions.
  P0a: full-grid defect ||K - RKR||_F / ||K||_F <= 1e-8 (float) / 1e-30 (mp).
       [fires -> build asymmetry: HALT, diagnose before any reading]
  P0b: orphan-channel ledger share (S_dd + |X_ed| + |X_od| + |X_eo|) reported per window;
       DESIGN RULE (locked): if > 0.10 * Sigma-sigma at any window, the parity-aligned
       ledger becomes the PRIMARY instrument (standard-cut parity reading demoted to
       bordering diagnostics).  Either way both frames are reported.
  P1: standard-cut parity cross |X_eo| <= 0.05 * min(S_ee, S_oo) expected (orphan-
      mediated only; report regardless).  Aligned frame: cross-block max entry / scale
      <= 1e-8 (mp) = the exact-decoupling certificate.
  P2 (even dominance, invariant form): global c_ee >= 2 * c_oo  (qualitative prior from
      s22.3: ladder cumulatives 0.25-0.45 even vs 0.05-0.08 odd).
      FALSIFIER (finding-level, NOT RH-relevant): c_oo >= c_ee -- the prior fails in
      invariant form; branch picture rewritten.
  P3 (closure; tolerance locked BEFORE data): with f_p = 1 - e^{-c_pp},
      c_pp = c_glob * (global eating share of channel pp),
      CLOSURE HOLDS  if |c_ee + c_oo - 0.342| <= 0.06 (the law's own band, s21);
      THIRD CHANNEL named if the gap exceeds 0.06: by the exact channel identity the gap
      is carried by the measured orphan + cross channels -- quantified and named (the
      anticipated name: ambiguous-parity / bulk leakage).  RH-true fires NO falsifier
      here (W2 lesson: laws and their constants are the deliverables).
  P4 (lambda-stability = the stationarity bridge): per-pair shares share_ee,n and
      share_oo,n have std/mean <= 0.35 across the 5 window pairs and no monotone
      factor-2 end-to-end trend.

Machinery: certified lineage only -- build_QW (f5, float windows 1.5/1.8),
build_QW_mp (wave_limit, dps 50, windows 2.0/2.2/2.35/2.5; mp REQUIRED >= 2.2 per
F64-3), uniform mp linear algebra on lifted matrices (LU quadratic forms; NO
eigenvectors anywhere).  Float cross-check at lam=2.0 (both builds).  Runtime ~6-12
min (mp DFT dominates).  Archive: parity_totals.npz.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")

HERE = "empirical/p_infinity/"
src2 = open(HERE + "probe_pinfF_f5_sampling.py", encoding="utf-8").read()
exec(src2.split('# ---- zeros')[0])          # primes_upto, build_QW (float lineage); dps=30
src3 = open(HERE + "probe_pinfF_innovation_chain.py", encoding="utf-8").read()
exec(src3[src3.index("def point_basis_form"):src3.index('print("== building')])
src4 = open(HERE + "probe_pinfF_wave_limit.py", encoding="utf-8").read()
exec(src4[src4.index("def build_QW_mp"):src4.index("def analyze")])   # build_QW_mp

R_MP = {2.0: 0.20081, 2.2: 0.13997, 2.35: 0.11329, 2.5: 0.08750}     # dps-50 truths (s21)
R_F64 = {1.5: 0.3491, 1.8: 0.2437}
CASES = [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]
MP_WINDOWS = {2.0, 2.2, 2.35, 2.5}
C_LAW = 0.342


def schur_quads(Alist, rhs_list):
    """Gram matrix of K^{-1}-quadratic forms: G[a][b] = rhs_a^T A^{-1} rhs_b (mp LU)."""
    nloc = len(Alist)
    A = mp.zeros(nloc, nloc)
    for i in range(nloc):
        for j in range(nloc):
            A[i, j] = Alist[i][j]
    sols = []
    for v in rhs_list:
        b = mp.matrix(nloc, 1)
        for i in range(nloc):
            b[i] = v[i]
        sols.append(mp.lu_solve(A, b))
    return [[mp.fsum(rhs_list[a][i] * sols[b2][i] for i in range(nloc))
             for b2 in range(len(rhs_list))] for a in range(len(rhs_list))]


def measure(lam, N, force_float=False):
    t0 = time.time()
    is_mp = (lam in MP_WINDOWS) and not force_float
    dim = 2 * N + 1
    piv3 = None
    if is_mp:
        mp.mp.dps = 50
        Q, Lmp = build_QW_mp(mp.mpf(repr(float(lam))), N)
        L = float(Lmp)
        B = mp.zeros(dim, dim)
        for n in range(dim):
            for i in range(dim):
                B[n, i] = mp.e**(2j * mp.pi * (n - N) * i / dim) / mp.sqrt(dim)
        Kc = (B.H) * Q * B
        K = [[(mp.re(Kc[i, j]) + mp.re(Kc[j, i])) / 2 for j in range(dim)]
             for i in range(dim)]
    else:
        mp.mp.dps = 30
        QW, L = build_QW(mp.mpf(repr(float(lam))), N, True)
        Kf, xg = point_basis_form(QW, N, L)
        order_f, _ = center_out_order(xg, L)
        piv = chain_pivots(Kf, order_f)
        piv3 = [float(p) for p in piv[-3:]]
        K = [[mp.mpf(float(Kf[i, j])) for j in range(dim)] for i in range(dim)]
    # ---- geometry (index-only; robust to ulp tie-breaks) ----
    x = np.arange(dim) * L / dim
    s = np.abs(x - L / 2)
    order = np.argsort(s, kind="stable")
    interior = [int(i) for i in order[:dim - 2]]
    pair = [int(i) for i in order[dim - 2:]]
    pos = {idx: a for a, idx in enumerate(interior)}
    refl = lambda i: (dim - i) % dim
    orphans = [i for i in interior if refl(i) not in pos]
    assert len(orphans) == 1 and 0 in pair, (orphans, pair)
    orph = orphans[0]
    # ---- P0a: full-grid reflection invariance ----
    num = mp.fsum((K[refl(i)][refl(j)] - K[i][j])**2
                  for i in range(dim) for j in range(dim))
    den = mp.fsum(K[i][j]**2 for i in range(dim) for j in range(dim))
    defect_full = float(mp.sqrt(num / den))
    # ---- standard cut: channel decomposition of the certified ledger ----
    p0_, p1_ = pair
    bare = (K[p0_][p0_] + K[p1_][p1_]) / 2 + K[p0_][p1_]
    sq2 = mp.sqrt(2)
    q = [(K[i][p0_] + K[i][p1_]) / sq2 for i in interior]
    ni = dim - 2
    qe = [mp.mpf(0)] * ni
    qo = [mp.mpf(0)] * ni
    qd = [mp.mpf(0)] * ni
    for a, idx in enumerate(interior):
        if idx == orph:
            qd[a] = q[a]
        else:
            b = pos[refl(idx)]
            qe[a] = (q[a] + q[b]) / 2
            qo[a] = (q[a] - q[b]) / 2
    Aint = [[K[i][j] for j in interior] for i in interior]
    G = schur_quads(Aint, [qe, qo, qd, q])
    S = {'ee': float(G[0][0] / bare), 'oo': float(G[1][1] / bare),
         'dd': float(G[2][2] / bare), 'eo': float(2 * G[0][1] / bare),
         'ed': float(2 * G[0][2] / bare), 'od': float(2 * G[1][2] / bare)}
    sig_total = float(G[3][3] / bare)
    ident_err = abs(S['ee'] + S['oo'] + S['dd'] + S['eo'] + S['ed'] + S['od'] - sig_total)
    # ---- parity-aligned frame: exact two-branch chains + wrap cell ----
    m = (dim - 1) // 2
    d_ = dim
    idx_in = list(range(2, m + 1))            # reflection-closed interior pairs
    Mp_ = [[(K[k][l] + K[k][d_ - l] + K[d_ - k][l] + K[d_ - k][d_ - l]) / 2
            for l in idx_in] for k in idx_in]
    Mm_ = [[(K[k][l] - K[k][d_ - l] - K[d_ - k][l] + K[d_ - k][d_ - l]) / 2
            for l in idx_in] for k in idx_in]
    qp = [(K[k][1] + K[k][d_ - 1] + K[d_ - k][1] + K[d_ - k][d_ - 1]) / 2 for k in idx_in]
    qm = [(K[k][1] - K[k][d_ - 1] - K[d_ - k][1] + K[d_ - k][d_ - 1]) / 2 for k in idx_in]
    bare_p = (K[1][1] + K[1][d_ - 1] + K[d_ - 1][1] + K[d_ - 1][d_ - 1]) / 2
    bare_m = (K[1][1] - K[1][d_ - 1] - K[d_ - 1][1] + K[d_ - 1][d_ - 1]) / 2
    w0 = [(K[k][0] + K[d_ - k][0]) / sq2 for k in idx_in]   # delta_0 couplings (even)
    GP = schur_quads(Mp_, [qp, w0])
    QP = GP[0][0]
    QM = schur_quads(Mm_, [qm])[0][0]
    d_plus = bare_p - QP
    d_minus = bare_m - QM
    sig_p, sig_m = float(QP / bare_p), float(QM / bare_m)
    c01 = (K[0][1] + K[0][d_ - 1]) / sq2                    # E_1^T K delta_0
    gamma = c01 - GP[0][1]
    v0 = K[0][0] - GP[1][1]
    # exact-decoupling certificate: largest cross-parity block entry (incl. wrap row)
    crossmax = mp.mpf(0)
    for l in range(1, m + 1):
        crossmax = max(crossmax, abs((K[0][l] - K[0][d_ - l]) / sq2))
        for k in range(1, m + 1):
            crossmax = max(crossmax, abs((K[k][l] - K[k][d_ - l]
                                          + K[d_ - k][l] - K[d_ - k][d_ - l]) / 2))
    scale = max(abs(K[i][i]) for i in range(dim))
    cross_rel = float(crossmax / scale)
    # wrap cell: final pivot d_0 = Schur of i=0 over everything else
    rest = [i for i in range(dim) if i != 0]
    k0 = [K[i][0] for i in rest]
    Arest = [[K[i][j] for j in rest] for i in rest]
    d0 = K[0][0] - schur_quads(Arest, [k0])[0][0]
    # V6: wrap consistency (aligned-frame route)
    d0_pred = v0 - gamma**2 / d_plus
    v6err = float(abs(d0_pred - d0) / abs(d0))
    # V7: the bridge identity (exact; orientation-independent)
    G_ = gamma / sq2
    var_t = v0 / 2 + (d_plus + d_minus) / 4 + G_
    cov_tu = ((d_plus - d_minus) / 2 + G_) / sq2
    var_u = (d_plus + d_minus) / 2
    d_std_pred = var_t - cov_tu**2 / var_u
    d_std_exact = bare - G[3][3]
    v7err = float(abs(d_std_pred - d_std_exact) / abs(d_std_exact))
    kappa = mp.mpf(1) / 4 + (d_plus / 2 + G_) * (3 * d_plus / 2 + G_) / d_plus**2
    odd_share = float((d_std_exact - d0 / 2) / d_std_exact)
    out = dict(lam=lam, L=L, dim=dim, orph=orph, pair=tuple(pair),
               defect_full=defect_full, cross_rel=cross_rel,
               bare=float(bare), sig=sig_total, R=1 - sig_total, S=S,
               ident=ident_err,
               qn_e=float(mp.sqrt(mp.fsum(v**2 for v in qe))),
               qn_o=float(mp.sqrt(mp.fsum(v**2 for v in qo))),
               qn_d=float(abs(qd[pos[orph]])),
               bare_p=float(bare_p), bare_m=float(bare_m),
               sig_p=sig_p, sig_m=sig_m, Rp=1 - sig_p, Rm=1 - sig_m,
               d_plus=float(d_plus), d_minus=float(d_minus),
               d0=float(d0), bare0=float(K[0][0]), R0=float(d0 / K[0][0]),
               gamma=float(gamma), v0=float(v0), v6=v6err, v7=v7err,
               kappa=float(kappa), odd_share=odd_share,
               d_std=float(d_std_exact),
               piv3=piv3, mp=is_mp)
    tag = "mp50" if is_mp else "f64-lift"
    print(f"   lam={lam} ({tag}, dim={dim}, {time.time()-t0:.0f}s): "
          f"Sigma-sigma={sig_total:.4f} R={1-sig_total:.4f} | "
          f"sig+={sig_p:.4f} sig-={sig_m:.4f} | d0/K00={out['R0']:.4f}")
    print(f"      defect_full={defect_full:.2e}  cross_rel={cross_rel:.2e}  "
          f"ident={ident_err:.2e}  orphan(idx {orph})")
    print(f"      S: ee={S['ee']:.4f} oo={S['oo']:.4f} dd={S['dd']:.4f} "
          f"eo={S['eo']:+.4f} ed={S['ed']:+.4f} od={S['od']:+.4f}")
    print(f"      bridge: d_std={out['d_std']:.4e}  d0/2={out['d0']/2:.4e}  "
          f"d-={out['d_minus']:.4e}  kappa={out['kappa']:.3f}  "
          f"odd_share={odd_share:.3f}  [V6={v6err:.1e} V7={v7err:.1e}]")
    return out


SMOKE = "--smoke" in sys.argv
print("== parity-totals: invariant branch decomposition (pre-registered header above) ==")
RES = {}
for lam, N in (CASES[:1] if SMOKE else CASES):
    RES[lam] = measure(lam, N)
if not SMOKE:
    print("   [float cross-check build at lam=2.0]")
    RES['2.0f'] = measure(2.0, 24, force_float=True)

if SMOKE:
    print("\nSMOKE OK")
    sys.exit(0)

lams = [c[0] for c in CASES]
l2 = np.array([l * l for l in lams])

# ---------------- validations ----------------
print("\n== V-checks ==")
v1 = all(abs(RES[l]['sig'] - (1 - R_MP[l])) <= 0.005 for l in R_MP)
v2 = all(abs(RES[l]['sig'] - (1 - R_F64[l])) <= 0.005 for l in R_F64)
print("   V1 (mp truths): " + "  ".join(
    f"{l}:{RES[l]['sig']:.4f}/{1-R_MP[l]:.4f}" for l in sorted(R_MP)) +
    ("   SURVIVES" if v1 else "   FIRED"))
print("   V2 (float truths): " + "  ".join(
    f"{l}:{RES[l]['sig']:.4f}/{1-R_F64[l]:.4f}" for l in sorted(R_F64)) +
    ("   SURVIVES" if v2 else "   FIRED"))
v3 = all(RES[l]['ident'] <= (1e-8 if RES[l]['mp'] else 1e-10) for l in lams)
print(f"   V3 (channel-sum identity): max = {max(RES[l]['ident'] for l in lams):.2e}"
      + ("   SURVIVES" if v3 else "   FIRED"))
v4 = True
for l in (1.5, 1.8):
    r = RES[l]
    w1 = abs(r['piv3'][0] * r['piv3'][1] - r['d_plus'] * r['d_minus']) / abs(r['d_plus'] * r['d_minus'])
    w2 = abs(r['piv3'][2] - r['d0']) / abs(r['d0'])
    v4 &= (w1 <= 1e-4) and (w2 <= 1e-4)
    print(f"   V4 weld lam={l}: |p1p2 - d+d-|/d+d- = {w1:.2e}   |p3 - d0|/d0 = {w2:.2e}")
print("   V4: " + ("SURVIVES -- aligned frame welded to certified chain" if v4 else "FIRED"))
xq = RES['2.0f']
xdiff = max(abs(xq['S'][k] - RES[2.0]['S'][k]) for k in xq['S'])
print(f"   float-vs-mp channel cross-check at lam=2.0: max |dS| = {xdiff:.2e} "
      f"(dSigma = {abs(xq['sig'] - RES[2.0]['sig']):.2e})")

Rstd = np.array([RES[l]['R'] for l in lams])
c_glob = -np.polyfit(l2, np.log(Rstd), 1)[0]
v5 = abs(c_glob - C_LAW) <= 0.06
print(f"   V5: c_glob (refit) = {c_glob:.3f} vs 0.342" + ("   SURVIVES" if v5 else "   FIRED"))
v6 = all(RES[l]['v6'] <= 1e-6 for l in lams)
v7 = all(RES[l]['v7'] <= 1e-6 for l in lams)
print(f"   V6 wrap consistency: max = {max(RES[l]['v6'] for l in lams):.1e}"
      + ("   SURVIVES" if v6 else "   FIRED"))
print(f"   V7 BRIDGE IDENTITY: max = {max(RES[l]['v7'] for l in lams):.1e}"
      + ("   SURVIVES -- d_std is an exact function of (d_+, d_-, gamma, v_0)"
         if v7 else "   FIRED -- derivation wrong, diagnose"))

# ---------------- P0: the defect audit ----------------
print("\n== P0: step zero -- the parity-defect audit ==")
p0a = all(RES[l]['defect_full'] <= (1e-30 if RES[l]['mp'] else 1e-8) for l in lams)
print("   P0a full-grid ||K-RKR||/||K||: " + "  ".join(
    f"{l}:{RES[l]['defect_full']:.1e}" for l in lams)
    + ("   SURVIVES (kernel reflection-invariance exact)" if p0a else "   FIRED -- HALT"))
print("   aligned-frame cross-block (exact decoupling): " + "  ".join(
    f"{l}:{RES[l]['cross_rel']:.1e}" for l in lams))
orphshare = {l: (RES[l]['S']['dd'] + abs(RES[l]['S']['ed'])
                 + abs(RES[l]['S']['od']) + abs(RES[l]['S']['eo'])) for l in lams}
rule = any(orphshare[l] > 0.10 * RES[l]['sig'] for l in lams)
print("   P0b orphan+cross ledger share: " + "  ".join(
    f"{l}:{orphshare[l]:.3f}({orphshare[l]/RES[l]['sig']*100:.0f}%)" for l in lams))
print("   DESIGN RULE: " + ("FIRES -- parity-aligned ledger is PRIMARY; standard-cut "
                            "parity channels = bordering diagnostics" if rule else
                            "quiet -- standard-cut channels readable as parity"))

# ---------------- the ledger decomposition and the laws ----------------
print("\n== branch totals per window (invariant, boundary-free) ==")
print("   lam    S_ee     S_oo     S_dd     X_eo      X_ed      X_od     | Sigma   R")
for l in lams:
    r = RES[l]
    print(f"   {l:4}  {r['S']['ee']:.4f}  {r['S']['oo']:.4f}  {r['S']['dd']:.4f}  "
          f"{r['S']['eo']:+.4f}  {r['S']['ed']:+.4f}  {r['S']['od']:+.4f}  | "
          f"{r['sig']:.4f}  {r['R']:.4f}")

print("\n== per-pair eating decomposition (differences of totals; per unit lambda^2) ==")
print("   pair        dSig    c_n    sh_ee   sh_oo   sh_dd   sh_eo   sh_ed   sh_od")
pairs_tab = []
for n in range(5):
    la, lb = lams[n], lams[n + 1]
    dl2 = lb * lb - la * la
    dSig = RES[lb]['sig'] - RES[la]['sig']
    c_n = -(np.log(RES[lb]['R']) - np.log(RES[la]['R'])) / dl2
    sh = {k: (RES[lb]['S'][k] - RES[la]['S'][k]) / dSig for k in RES[la]['S']}
    pairs_tab.append((la, lb, dl2, dSig, c_n, sh))
    print(f"   {la}-{lb}   {dSig:.4f}  {c_n:.3f}  " + "  ".join(
        f"{sh[k]:+.3f}" for k in ('ee', 'oo', 'dd', 'eo', 'ed', 'od')))
shg = {k: (RES[2.5]['S'][k] - RES[1.5]['S'][k]) / (RES[2.5]['sig'] - RES[1.5]['sig'])
       for k in RES[1.5]['S']}
c_ch = {k: c_glob * shg[k] for k in shg}
print("   GLOBAL shares (1.5 -> 2.5): " + "  ".join(
    f"{k}:{shg[k]:+.3f}" for k in ('ee', 'oo', 'dd', 'eo', 'ed', 'od')))
print("   GLOBAL channel rates c_pp = c_glob * share: " + "  ".join(
    f"{k}:{c_ch[k]:+.4f}" for k in ('ee', 'oo', 'dd', 'eo', 'ed', 'od')))

print("\n== branch-own laws (parity-aligned chains; new constants) ==")
Rp = np.array([RES[l]['Rp'] for l in lams])
Rm = np.array([RES[l]['Rm'] for l in lams])
R0 = np.array([RES[l]['R0'] for l in lams])
c_plus = -np.polyfit(l2, np.log(Rp), 1)[0]
c_minus = -np.polyfit(l2, np.log(Rm), 1)[0]
c_wrap = -np.polyfit(l2, np.log(R0), 1)[0]
print("   lam:   R_+ (even edge)   R_- (odd edge)    R_0 (wrap)")
for l in lams:
    print(f"   {l:4}   {RES[l]['Rp']:.5f}          {RES[l]['Rm']:.3e}        {RES[l]['R0']:.4f}")
print(f"   laws: c_plus = {c_plus:.3f}   c_minus = {c_minus:.3f}   c_wrap = {c_wrap:.3f}"
      f"   (c_glob = {c_glob:.3f}, law 0.342)")
for n in range(5):
    la, lb = lams[n], lams[n + 1]
    dl2 = lb * lb - la * la
    cp = -(np.log(RES[lb]['Rp']) - np.log(RES[la]['Rp'])) / dl2
    cm = -(np.log(RES[lb]['Rm']) - np.log(RES[la]['Rm'])) / dl2
    c0 = -(np.log(RES[lb]['R0']) - np.log(RES[la]['R0'])) / dl2
    print(f"   pair {la}-{lb}: c_plus,n = {cp:.3f}   c_minus,n = {cm:.3f}   c_wrap,n = {c0:.3f}")

print("\n== the additive decomposition of the certified remainder (bridge corollary) ==")
print("   lam    d_std       d0/2        kappa*d-    sum/d_std   odd_share   kappa   g=G/d+    rho")
for l in lams:
    r = RES[l]
    apx = r['d0'] / 2 + r['kappa'] * r['d_minus']
    g_ = r['gamma'] / np.sqrt(2) / r['d_plus']
    rho_ = r['gamma'] / np.sqrt(r['v0'] * r['d_plus'])
    print(f"   {l:4}   {r['d_std']:.4e}  {r['d0']/2:.4e}  {r['kappa']*r['d_minus']:.4e}"
          f"  {apx/r['d_std']:.4f}      {r['odd_share']:+.3f}     {r['kappa']:+.3f}  "
          f"{g_:+.3f}   {rho_:+.3f}")

# ---------------- verdicts ----------------
print("\n== VERDICTS (pre-registered) ==")
p1v = all(abs(RES[l]['S']['eo']) <= 0.05 * min(RES[l]['S']['ee'], RES[l]['S']['oo'])
          for l in lams)
print(f"   P1 cross: |X_eo| <= 5% min(S_ee,S_oo) at all windows: "
      + ("YES" if p1v else "NO (orphan-mediated; see tables)")
      + f"; aligned decoupling cross_rel max = {max(RES[l]['cross_rel'] for l in lams):.1e}")
p2v = c_ch['ee'] >= 2 * c_ch['oo']
p2f = c_ch['oo'] >= c_ch['ee']
print(f"   P2 even dominance: c_ee = {c_ch['ee']:.4f} vs c_oo = {c_ch['oo']:.4f}  ->  "
      + ("SURVIVES (>= 2x)" if p2v else ("FALSIFIER FIRED (odd >= even)" if p2f
                                         else "between (1x-2x) -- report")))
cc = c_ch['ee'] + c_ch['oo']
fe, fo = 1 - np.exp(-c_ch['ee']), 1 - np.exp(-c_ch['oo'])
gap = cc - C_LAW
leak = c_glob - cc
print(f"   P3 closure: c_ee + c_oo = {cc:.4f} vs 0.342 (gap {gap:+.4f}; tol 0.06)")
print(f"      (1-f_e)(1-f_o) = {(1-fe)*(1-fo):.4f} vs e^-0.342 = {np.exp(-C_LAW):.4f}"
      f"   [f_e = {fe:.4f}, f_o = {fo:.4f}]")
print(f"      leak (orphan+cross channels) = {leak:+.4f} of c_glob = {c_glob:.4f}")
if abs(gap) <= 0.06:
    print("      -> CLOSURE HOLDS: the two-branch account of the eating law is complete")
else:
    print("      -> THIRD CHANNEL: gap carried by the measured orphan/cross channels "
          "(ambiguous-parity / bulk leakage) -- named and quantified above")
she = [pt[5]['ee'] for pt in pairs_tab]
sho = [pt[5]['oo'] for pt in pairs_tab]
ste = float(np.std(she) / np.mean(she)) if np.mean(she) != 0 else np.inf
sto = float(np.std(sho) / np.mean(sho)) if np.mean(sho) != 0 else np.inf
trend_e = max(she) / min(she) if min(she) > 0 else np.inf
trend_o = max(sho) / min(sho) if min(sho) > 0 else np.inf
p4v = ste <= 0.35 and sto <= 0.35 and trend_e <= 2 and trend_o <= 2
print(f"   P4 stability: share_ee std/mean = {ste:.2f} (spread x{trend_e:.2f}); "
      f"share_oo std/mean = {sto:.2f} (x{trend_o:.2f})  ->  "
      + ("SURVIVES -- per-arrival fractions lambda-stable (stationarity bridge)"
         if p4v else "NOT stable -- see per-pair table (report as measured)"))

np.savez(HERE + "parity_totals.npz",
         lams=np.array(lams), l2=l2,
         sig=np.array([RES[l]['sig'] for l in lams]), R=Rstd,
         S_ee=np.array([RES[l]['S']['ee'] for l in lams]),
         S_oo=np.array([RES[l]['S']['oo'] for l in lams]),
         S_dd=np.array([RES[l]['S']['dd'] for l in lams]),
         X_eo=np.array([RES[l]['S']['eo'] for l in lams]),
         X_ed=np.array([RES[l]['S']['ed'] for l in lams]),
         X_od=np.array([RES[l]['S']['od'] for l in lams]),
         sig_p=np.array([RES[l]['sig_p'] for l in lams]),
         sig_m=np.array([RES[l]['sig_m'] for l in lams]),
         Rp=Rp, Rm=Rm, R0=R0,
         bare=np.array([RES[l]['bare'] for l in lams]),
         bare_p=np.array([RES[l]['bare_p'] for l in lams]),
         bare_m=np.array([RES[l]['bare_m'] for l in lams]),
         d0=np.array([RES[l]['d0'] for l in lams]),
         gamma=np.array([RES[l]['gamma'] for l in lams]),
         v0=np.array([RES[l]['v0'] for l in lams]),
         kappa=np.array([RES[l]['kappa'] for l in lams]),
         d_std=np.array([RES[l]['d_std'] for l in lams]),
         d_plus=np.array([RES[l]['d_plus'] for l in lams]),
         d_minus=np.array([RES[l]['d_minus'] for l in lams]),
         c_fits=np.array([c_glob, c_plus, c_minus, c_wrap]),
         defect=np.array([RES[l]['defect_full'] for l in lams]),
         cross_rel=np.array([RES[l]['cross_rel'] for l in lams]))
print("\nARCHIVED: parity_totals.npz")
ok = v1 and v2 and v3 and v4 and v5 and v6 and v7 and p0a
print("RESULT: " + ("GREEN -- instrument validated; verdicts above are readings"
                    if ok else "RED/PARTIAL -- a V-check or P0a fired; diagnose first"))
