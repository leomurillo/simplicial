"""probe_pinfF_transfer_map_v2.py -- the stationarity strike, step 1b: the SEAM resolution.

WHAT v1 TAUGHT (corpse retained: probe_pinfF_transfer_map.py, transfer_map_run.log):
  P1 (six-window cross-implementation) and P2 (ledger locality, registered sign) SURVIVED:
  the chain elimination IS the section-21 object and one chain generates the six windows.
  P3/P4 FIRED as a finding: the CLEAN reflection-pair ledger collapses at c_clean ~ 3.3-3.8
  per unit lambda^2 (rms 0.94 -- not even cleanly exponential) with grid-step rho^2_eff up
  to 0.998 -- continuum-smoothness correlation, criterion not arithmetic, at that
  granularity.  The published law c = 0.342 is carried by the section-21 convention whose
  edge cell contains the WRAP POINT i=0 = the window's domain edge = the parity fixed
  point = where the freshest primes (log n ~ L) land through the wrap-distance kernel
  entries.  READING (pre-registered here, tested below): the unpredictable remainder
  CONCENTRATES on the migrating boundary-seam cell; the bulk is slaved at the fast clean
  pace; the transfer map reduces to a seam-renewal map.

PRE-REGISTERED (GPD; fixed before this run):
  Q1 (the seam law): R_seam(lam) = d(i=0 | all other points) / K(0,0) across the six
      windows fits R ~ C e^{-c lam^2} with c_seam in [0.24, 0.45].
      FALSIFIER: c_seam outside => the seam-relocation reading is wrong.
  Q2 (mixed-edge decomposition): the seam carries the section-21 cell: R_seam / (2 R_21)
      in [0.5, 1.5] at every window (the mixed cell's remainder is seam-dominated).
  Q3 (within-build seam ledger): conditioning the lam=2.5 seam on the growing bulk,
      the outermost third of shells (by radius) contributes >= 50% of the total seam
      saturation S0(N) - S0(0) ... measured from the saturation profile S0(m).
      (Concentration of the seam's predictability in the boundary band = section 9.3/20
      seam anatomy in conditioning coordinates.)
  Q4 (odd boundary cell, report-only): R_odd(outermost pair | everything else including
      the seam) across windows; its law logged as the odd-branch input (D1 two-branch).
  Q5 (graft detection, v1-P5 fixed): F.14 off-line curvature graft (gamma0 = 17.5,
      ||DK||_F = 2% ||K||_F) on lam=2.5: R_seam and R_21 BOTH depressed vs clean
      (sign-only; magnitudes reported).  FALSIFIER: graft invisible on the seam =>
      the seam ledger is blind to off-line content and certifies nothing.
  Q6 (seam-profile stationarity -- the proof-target object, first direct look):
      seam saturation-increment profiles dS0 vs distance-from-seam u = L/2 - r, compared
      across the six windows on shared u-grid: report the profile dispersion in the
      outer band (u <= 0.35); soft band <= 0.35 relative (first look, no falsifier).
  Q0 (identity): T3-derived section-21 value reproduces the quoted targets to 2e-3/8e-4
      (same tolerance as v1-P1) -- one elimination pass now yields ALL final objects.

Machinery: as v1 (certified mp builder at dps 35; list-of-lists elimination); ONE pass
per window (pairs innermost->outermost, i=0 never eliminated), trailing 3x3 at
{outermost pair, seam} read for: d_E/d_O(pair | bulk), seam-given-bulk, seam-given-all,
pair-given-all, and the section-21 mixed cell (Schur out the partner within the 3x3).
S0(m) profile recorded each step.  F64 rules respected throughout (exact mp kernels;
cumulative/determinant-ratio observables only).
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
TOL_Q0 = {1.5: 2e-3, 1.8: 2e-3, 2.0: 8e-4, 2.2: 8e-4, 2.35: 8e-4, 2.5: 8e-4}
CASES = [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]


def build_point_kernel(lam, N):
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
    piv = A[k][k]
    Ak = A[k]
    for i in act:
        cik = A[i][k] / piv
        if cik:
            Ai = A[i]
            for j in act:
                Ai[j] -= cik * Ak[j]


def seam_pass(Kr, L, dim):
    """One pass: eliminate pairs innermost->outermost except the outermost; i=0 never.

    Returns: S0 profile (seam saturation vs pairs conditioned), trailing-3x3-derived
    objects, and the within-chain radii."""
    N = (dim - 1) // 2
    dx = L / dim
    pairs = [(N + 1 - m, N + m) for m in range(1, N + 1)]
    A = [row[:] for row in Kr]
    act = set(range(dim))
    bare0 = float(Kr[0][0])
    S0, radii = [], []
    for m, (ia, ib) in enumerate(pairs[:-1], start=1):
        act -= {ia}; eliminate(A, act, ia)
        act -= {ib}; eliminate(A, act, ib)
        S0.append(1 - float(A[0][0]) / bare0)
        radii.append((m - 0.5) * dx)
    a_, b_ = pairs[-1]                      # outermost pair (1, 2N)
    # trailing 3x3 on {a_, b_, 0}
    idx = [a_, b_, 0]
    T3 = [[A[i][j] for j in idx] for i in idx]
    bareE = float((Kr[a_][a_] + Kr[b_][b_]) / 2 + Kr[a_][b_])
    bareO = float((Kr[a_][a_] + Kr[b_][b_]) / 2 - Kr[a_][b_])
    # pair given bulk only
    dE_bulk = float((T3[0][0] + T3[1][1]) / 2 + T3[0][1])
    dO_bulk = float((T3[0][0] + T3[1][1]) / 2 - T3[0][1])
    # seam given bulk only
    seam_bulk = float(T3[2][2])
    # seam given ALL (Schur out the 2x2 pair block)
    det2 = T3[0][0] * T3[1][1] - T3[0][1] * T3[0][1]
    e0, e1 = T3[2][0], T3[2][1]
    seam_all = float(T3[2][2] - (e0 * (T3[1][1] * e0 - T3[0][1] * e1)
                                 + e1 * (T3[0][0] * e1 - T3[0][1] * e0)) / det2)
    # pair given bulk + seam (Schur out the seam)
    s22 = [[float(T3[i][j] - T3[i][2] * T3[j][2] / T3[2][2]) for j in range(2)] for i in range(2)]
    dE_all = (s22[0][0] + s22[1][1]) / 2 + s22[0][1]
    dO_all = (s22[0][0] + s22[1][1]) / 2 - s22[0][1]
    # section-21 mixed cell: condition on the partner b_, cell (delta_a + delta_0)/sqrt2
    m2 = [[float(T3[i][j] - T3[i][1] * T3[j][1] / T3[1][1]) for j in (0, 2)] for i in (0, 2)]
    bare21 = float((Kr[a_][a_] + Kr[0][0]) / 2 + Kr[a_][0])
    d21 = (m2[0][0] + m2[1][1]) / 2 + m2[0][1]
    sig21 = 1 - d21 / bare21
    return dict(S0=np.array(S0), radii=np.array(radii), bare0=bare0, bareE=bareE,
                bareO=bareO, dE_bulk=dE_bulk, dO_bulk=dO_bulk, seam_bulk=seam_bulk,
                seam_all=seam_all, dE_all=dE_all, dO_all=dO_all, sig21=float(sig21),
                R_seam=float(seam_all / bare0), R21=float(1 - sig21),
                RO_all=float(dO_all / bareO), RE_all=float(dE_all / bareE), L=L, dx=dx)


print("== the seam pass (mp dps=35, six windows) ==")
res = {}
for lam, N in CASES:
    t0 = time.time()
    Kr, L = build_point_kernel(lam, N)
    dim = 2 * N + 1
    r = seam_pass(Kr, L, dim)
    r["Kr"], r["dim"] = Kr, dim
    res[lam] = r
    print(f"   lam={lam} ({time.time()-t0:.0f}s): sig21={r['sig21']:.5f} "
          f"R_seam={r['R_seam']:.4e} R21={r['R21']:.4e} seam/bulk-only={r['seam_bulk']/r['bare0']:.3f} "
          f"RO_all={r['RO_all']:.3e} RE_all={r['RE_all']:.3e}")

print("\n== Q0: one-pass cross-implementation (T3-derived section-21 value) ==")
q0 = True
for lam, _ in CASES:
    diff = abs(res[lam]["sig21"] - TARGETS[lam])
    ok = diff <= TOL_Q0[lam]
    q0 &= ok
    print(f"   lam={lam}: {res[lam]['sig21']:.5f} vs {TARGETS[lam]:.5f}  |diff|={diff:.1e}  "
          + ("ok" if ok else "MISS"))
print("   Q0: " + ("SURVIVES" if q0 else "FIRED -- diagnose"))

print("\n== Q1: the seam law across windows ==")
lams = np.array([l for l, _ in CASES])
Rs = np.array([res[l]["R_seam"] for l, _ in CASES])
cf = np.polyfit(lams**2, np.log(Rs), 1)
c_seam = -cf[0]
resid = np.log(Rs) - np.polyval(cf, lams**2)
print("   R_seam: " + "  ".join(f"{l}:{R:.4f}" for l, R in zip(lams, Rs)))
print(f"   fit: c_seam = {c_seam:.3f}  (band [0.24, 0.45]; published mixed-edge law 0.342)"
      f"   rms resid = {np.sqrt(np.mean(resid**2)):.3f}")
per = np.diff(np.log(Rs)) / np.diff(lams**2)
print("   per-interval slopes: " + "  ".join(f"{-v:.3f}" for v in per))
q1 = 0.24 <= c_seam <= 0.45
print("   Q1: " + ("SURVIVES -- the seam carries the law" if q1
                   else "FIRED -- seam-relocation reading wrong"))

print("\n== Q2: mixed-edge decomposition (seam dominance of the section-21 cell) ==")
q2 = True
for lam, _ in CASES:
    ratio = res[lam]["R_seam"] / (2 * res[lam]["R21"])
    ok = 0.5 <= ratio <= 1.5
    q2 &= ok
    print(f"   lam={lam}: R_seam/(2 R21) = {ratio:.3f}  " + ("ok" if ok else "OUT"))
print("   Q2: " + ("SURVIVES -- the published law is the seam's law" if q2
                   else "FIRED -- mixed cell not seam-dominated; decompose further"))

print("\n== Q3: within-build seam ledger (lam=2.5): where is the seam predicted from? ==")
big = res[2.5]
S0, rr = big["S0"], big["radii"]
dS = np.diff(np.concatenate([[0.0], S0]))
Ltot = S0[-1]
third = rr >= (2 / 3) * rr[-1]
share = float(dS[third].sum() / Ltot)
print(f"   total seam saturation S0(N-1) = {Ltot:.4f}; outermost-third share = {share:.3f}")
top = np.argsort(dS)[::-1][:5]
print("   top eating shells: " + "  ".join(f"r={rr[i]:.3f}:{dS[i]:+.3f}" for i in sorted(top)))
q3 = share >= 0.5
print("   Q3: " + ("SURVIVES -- seam predictability lives in the boundary band"
                   if q3 else "CHECK -- interior-dominated; report"))

print("\n== Q4: the odd boundary cell across windows (report-only) ==")
ROs = np.array([res[l]["RO_all"] for l, _ in CASES])
cfo = np.polyfit(lams**2, np.log(ROs), 1)
print("   R_odd(outer pair | all): " + "  ".join(f"{l}:{R:.3e}" for l, R in zip(lams, ROs)))
print(f"   odd-cell law: c_odd = {-cfo[0]:.3f}   (logged as the odd-branch input)")
REs = np.array([res[l]["RE_all"] for l, _ in CASES])
cfe = np.polyfit(lams**2, np.log(REs), 1)
print("   R_even(outer pair | all): " + "  ".join(f"{l}:{R:.3e}" for l, R in zip(lams, REs)))
print(f"   even-outer-cell law: c_Eout = {-cfe[0]:.3f}")

print("\n== Q5: graft detection on the seam (F.14 signature, sign-only) ==")
lam, N = 2.5, 32
Kr, L, dim = big["Kr"], big["L"], big["dim"]
x = [i * L / dim for i in range(dim)]
nrmK = np.sqrt(sum(float(Kr[i][j])**2 for i in range(dim) for j in range(dim)))
raw = [[(x[i] - x[j])**2 * 2 * np.cos(17.5 * (x[i] - x[j])) for j in range(dim)]
       for i in range(dim)]
nrmG = np.sqrt(sum(raw[i][j]**2 for i in range(dim) for j in range(dim)))
amp = 0.02 * nrmK / nrmG
Kg = [[Kr[i][j] + mp.mpf(float(amp * raw[i][j])) for j in range(dim)] for i in range(dim)]
rg = seam_pass(Kg, L, dim)
print(f"   clean:  R_seam={big['R_seam']:.4e}  R21={big['R21']:.4e}")
print(f"   graft:  R_seam={rg['R_seam']:.4e}  R21={rg['R21']:.4e}"
      f"   deficits: seam {1-rg['R_seam']/big['R_seam']:+.3f}, mixed {1-rg['R21']/big['R21']:+.3f}")
q5 = (rg["R_seam"] < big["R_seam"]) and (rg["R21"] < big["R21"])
print("   Q5: " + ("SURVIVES -- the seam ledger sees the off-line signature"
                   if q5 else "FIRED -- blind instrument"))

print("\n== Q6: seam-profile stationarity (the proof-target object, first look) ==")
UGRID = np.linspace(0.02, 0.35, 12)
profs = []
for lam, _ in CASES:
    r = res[lam]
    u = r["L"] / 2 - r["radii"]            # distance from seam
    dS_ = np.diff(np.concatenate([[0.0], r["S0"]])) / r["dx"]
    # cumulative-from-the-seam saturation as fn of u (integrate inward from boundary)
    o = np.argsort(u)
    cums = np.cumsum((dS_[o] * r["dx"]))
    prof = np.interp(UGRID, u[o], cums)
    profs.append(prof / max(cums[-1], 1e-30))
P = np.vstack(profs)
disp = float(np.mean(P.std(0) / np.maximum(P.mean(0), 1e-9)))
print("   normalized cumulative-from-seam profiles on shared u-grid (six windows):")
for (lam, _), p in zip(CASES, profs):
    print(f"     lam={lam}: " + " ".join(f"{v:.2f}" for v in p[::3]))
print(f"   cross-window profile dispersion (u <= 0.35) = {disp:.3f}   (soft band <= 0.35)")
print("   Q6: measurement logged -- the seam-renewal profile's first stationarity data")

np.savez("empirical/p_infinity/transfer_map_seam.npz",
         lams=lams, R_seam=Rs, R21=np.array([res[l]["R21"] for l, _ in CASES]),
         RO=ROs, RE=REs,
         **{f"S0_{lam}": res[lam]["S0"] for lam, _ in CASES},
         **{f"rr_{lam}": res[lam]["radii"] for lam, _ in CASES})

verdict = q0 and q1 and q2 and q5
print("\nRESULT: " + ("GREEN -- seam resolution certified: the law lives on the migrating "
                      "boundary cell; map = seam renewal with slaved bulk"
                      if verdict else "PARTIAL -- see fired blocks (GPD: diagnose, retain)"))
