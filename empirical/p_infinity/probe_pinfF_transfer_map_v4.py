"""probe_pinfF_transfer_map_v4.py -- the stationarity strike, step 1d: the Thompson orbit
(per-arrival boundary-state confinement = hypothesis (U)'s first direct data) + the
lam=3.0 seam extension (7th law point, +40% range).

PRE-REGISTERED (GPD, fixed before the run):
  X1 (the lam=3.0 seam point): R_seam(3.0) in [0.015, 0.060] (the v2 law's extrapolation
      band: c_seam=0.419 fit gives 0.029; band generous for the per-interval drift
      0.28-0.55).  FALSIFIER: outside [0.008, 0.12] => the seam law breaks beyond the
      measured range; stationarity claim dies with it.
  X2 (the Thompson orbit -- (U)'s data): seam-relative even-sector boundary blocks
      (seam + J=4 shells, 5x5, conditioned on the bulk, normalized by the seam entry)
      compared across consecutive windows: distances D_T reported; soft reading: D_T
      bounded (<= 1.5) and not trending up.  No falsifier (first orbit measurement);
      this is the empirical standing of uniform cone confinement.
  X3 (odd-sector orbit, report-only): same with the odd 4x4 blocks.
  X4 (profile densification): the lam=3.0 within-build S0 profile joins the Q6 family
      (cumulative-from-seam on the shared u-grid; report new dispersion).

Windows: the six certified + (3.0, N=38) matched bandwidth (omega_N ~ 108).
Machinery: as v2/v3 (certified mp builder, dps 35, list-of-lists elimination); partial
pass stopping J pairs short of the boundary to read the (2J+1) boundary block given bulk.
"""
import sys
import time
import numpy as np
import mpmath as mp
from scipy.linalg import eigh

sys.stdout.reconfigure(encoding="utf-8")

src = open("empirical/p_infinity/probe_pinfF_wave_limit.py", encoding="utf-8").read()
exec(src.split("def analyze")[0])
mp.mp.dps = 35

CASES = [(1.5, 14), (1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32), (3.0, 38)]
JSH = 4


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


def boundary_pass(Kr, L, dim, Jsh=JSH):
    """Eliminate pairs 1..N-Jsh; read the boundary block (Jsh pairs + seam) given bulk,
    then continue to the full seam objects (R_seam, S0 profile)."""
    N = (dim - 1) // 2
    dx = L / dim
    pairs = [(N + 1 - m, N + m) for m in range(1, N + 1)]
    A = [row[:] for row in Kr]
    act = set(range(dim))
    bare0 = float(Kr[0][0])
    S0, radii = [], []
    blocks = None
    for m, (ia, ib) in enumerate(pairs[:-1], start=1):
        act -= {ia}; eliminate(A, act, ia)
        act -= {ib}; eliminate(A, act, ib)
        S0.append(1 - float(A[0][0]) / bare0)
        radii.append((m - 0.5) * dx)
        if m == N - Jsh:
            # boundary block on the remaining Jsh pairs + seam, even/odd sectors,
            # seam-relative order: (seam, outermost pair, next, ...)
            rem = pairs[m:]                          # Jsh pairs, innermost..outermost
            rem_rel = rem[::-1]                      # outermost first
            EV = np.zeros((Jsh + 1, Jsh + 1))
            for aa in range(Jsh + 1):
                for bb in range(aa, Jsh + 1):
                    if aa == 0 and bb == 0:
                        v = float(A[0][0])
                    elif aa == 0:
                        pa, pb = rem_rel[bb - 1]
                        v = float((A[0][pa] + A[0][pb]) / mp.sqrt(2))
                    else:
                        pa, pb = rem_rel[aa - 1]
                        qa, qb = rem_rel[bb - 1]
                        v = float((A[pa][qa] + A[pa][qb] + A[pb][qa] + A[pb][qb]) / 2)
                    EV[aa, bb] = EV[bb, aa] = v
            OD = np.zeros((Jsh, Jsh))
            for aa in range(Jsh):
                pa, pb = rem_rel[aa]
                for bb in range(aa, Jsh):
                    qa, qb = rem_rel[bb]
                    OD[aa, bb] = OD[bb, aa] = float((A[pa][qa] - A[pa][qb]
                                                     - A[pb][qa] + A[pb][qb]) / 2)
            blocks = (EV, OD)
    a_, b_ = pairs[-1]
    idx = [a_, b_, 0]
    T3 = [[A[i][j] for j in idx] for i in idx]
    det2 = T3[0][0] * T3[1][1] - T3[0][1] * T3[0][1]
    e0, e1 = T3[2][0], T3[2][1]
    seam_all = float(T3[2][2] - (e0 * (T3[1][1] * e0 - T3[0][1] * e1)
                                 + e1 * (T3[0][0] * e1 - T3[0][1] * e0)) / det2)
    return dict(S0=np.array(S0), radii=np.array(radii), bare0=bare0,
                R_seam=seam_all / bare0, blocks=blocks, L=L, dx=dx)


def thompson(W0, W1):
    A0, A1 = W0 / W0[0, 0], W1 / W1[0, 0]
    ev = eigh(A1, A0, eigvals_only=True)
    ev = ev[ev > 0]
    return float(np.max(np.abs(np.log(ev)))) if len(ev) else float("nan")


print("== boundary passes (mp dps=35, seven windows) ==")
res = {}
for lam, N in CASES:
    t0 = time.time()
    Kr, L = build_point_kernel(lam, N)
    r = boundary_pass(Kr, L, 2 * N + 1)
    res[lam] = r
    print(f"   lam={lam} ({time.time()-t0:.0f}s): R_seam={r['R_seam']:.4e}  "
          f"S0_total={r['S0'][-1]:.4f}")

print("\n== X1: the lam=3.0 seam point ==")
R3 = res[3.0]["R_seam"]
lams = np.array([l for l, _ in CASES])
Rs = np.array([res[l]["R_seam"] for l, _ in CASES])
cf6 = np.polyfit(lams[:-1]**2, np.log(Rs[:-1]), 1)
pred = float(np.exp(np.polyval(cf6, 9.0)))
cf7 = np.polyfit(lams**2, np.log(Rs), 1)
resid7 = np.log(Rs) - np.polyval(cf7, lams**2)
print(f"   R_seam(3.0) = {R3:.4e}   (six-window extrapolation {pred:.4e}; "
      f"registered band [0.015, 0.060]; falsifier outside [0.008, 0.12])")
print(f"   seven-window law: c_seam = {-cf7[0]:.3f}  rms resid = {np.sqrt(np.mean(resid7**2)):.3f}")
per = np.diff(np.log(Rs)) / np.diff(lams**2)
print("   per-interval slopes: " + "  ".join(f"{-v:.3f}" for v in per))
x1 = 0.015 <= R3 <= 0.060
x1f = 0.008 <= R3 <= 0.12
print("   X1: " + ("SURVIVES -- the law extends" if x1 else
                   ("soft-miss (inside falsifier bound) -- report" if x1f else
                    "FALSIFIED -- the law breaks beyond the measured range")))

print("\n== X2/X3: the Thompson orbit (per-arrival boundary-state confinement) ==")
print("   consecutive-window distances, seam-relative blocks given bulk:")
prev = None
DEs, DOs = [], []
for lam, _ in CASES:
    EV, OD = res[lam]["blocks"]
    if prev is not None:
        dE = thompson(prev[0], EV)
        dO = thompson(prev[1] / prev[1][0, 0], OD / OD[0, 0])
        DEs.append(dE); DOs.append(dO)
        print(f"   {prev[2]} -> {lam}:  D_T(even 5x5) = {dE:.3f}   D_T(odd 4x4) = {dO:.3f}")
    prev = (EV, OD, lam)
bounded = all(d <= 1.5 for d in DEs)
trend = (len(DEs) >= 3) and all(b > a for a, b in zip(DEs[-3:], DEs[-2:]))
print(f"   even-orbit: max D_T = {max(DEs):.3f}; soft reading: "
      + ("bounded, " + ("trending UP -- flag" if trend else "no upward trend")
         if bounded else "EXCEEDS 1.5 -- flag for the (U) discussion"))

print("\n== X4: profile densification (seven-window Q6 family) ==")
UGRID = np.linspace(0.02, 0.35, 12)
profs = []
for lam, _ in CASES:
    r = res[lam]
    u = r["L"] / 2 - r["radii"]
    dS_ = np.diff(np.concatenate([[0.0], r["S0"]]))
    o = np.argsort(u)
    cums = np.cumsum(dS_[o])
    prof = np.interp(UGRID, u[o], cums)
    profs.append(prof / max(cums[-1], 1e-30))
P = np.vstack(profs)
disp_all = float(np.mean(P.std(0) / np.maximum(P.mean(0), 1e-9)))
P_mat = np.vstack(profs[1:])     # drop the immature lam=1.5
disp_mat = float(np.mean(P_mat.std(0) / np.maximum(P_mat.mean(0), 1e-9)))
for (lam, _), p in zip(CASES, profs):
    print(f"   lam={lam}: " + " ".join(f"{v:.2f}" for v in p[::3]))
print(f"   dispersion: all seven = {disp_all:.3f};  mature (lam >= 1.8) = {disp_mat:.3f}")

np.savez("empirical/p_infinity/transfer_map_orbit.npz",
         lams=lams, R_seam=Rs,
         DE=np.array(DEs), DO=np.array(DOs),
         **{f"EV_{lam}": res[lam]["blocks"][0] for lam, _ in CASES},
         **{f"OD_{lam}": res[lam]["blocks"][1] for lam, _ in CASES})

print("\nRESULT: " + ("GREEN -- law extended to lam=3.0; orbit measured"
                      if x1 else "PARTIAL -- see X1 (soft) / blocks"))
