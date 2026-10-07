"""probe_pinfF_transfer_map_v5.py -- the stationarity strike, step 1e: the lam=3.0 point at
proper precision + the renormalized (correlation) orbit.

V4 DIAGNOSES (corpses retained; transfer_map_v4_run.log):
  X1 soft-miss = DPS-STARVATION ARTIFACT: eps(3.0) ~ 2e-45 < dps-35 entry noise (1e-35);
  smoking gun = NEGATIVE conditioning increments in the lam=3.0 S0 profile (impossible for
  a PSD kernel) + non-monotone S0_total.  METHODS RULE (F64-6, deposited): "exact mp" is
  not a fixed dps -- dps must clear the spectral floor: dps >= -log10 eps(lam) + ~15.
  X2 mis-aimed instrument = section-22-E3's lesson in Thompson coordinates: raw boundary
  blocks are MIXED objects (stationary shape x slaved directions deepening lawfully at the
  clean pace); their Thompson distance reads the known collapse, not profile instability.
  The (U)-confinement object is the RENORMALIZED profile = each direction in its own
  scale = the block's CORRELATION matrix.

PRE-REGISTERED (GPD, fixed before the run):
  Y1 (lam=3.0 at dps 65): R_seam(3.0) in [0.015, 0.060] (X1's band, now properly
      instrumented); falsifier outside [0.008, 0.12].  Sanity gates that DEFINE
      trustworthiness (the dps-starvation detectors): all S0 increments >= -1e-10 and
      S0_total(3.0) >= S0_total(2.5) - 0.02.  If the gates fail at dps 65, raise to 80
      before any law conclusion (report only).
  Y2 (the correlation orbit -- (U)'s renormalized data): even-sector boundary-block
      correlation matrices C = D^{-1/2} W D^{-1/2} across consecutive windows (blocks
      from transfer_map_orbit.npz for lam <= 2.5; the new dps-65 block for 3.0):
      reading rule fixed now: Frobenius distances ||C_k - C_{k+1}||_F reported; the
      confinement reading is 'bounded <= 0.5 and the last three not increasing by more
      than 0.1 per step'; otherwise 'not confined at this instrument' is reported as-is.
  Y3 (profile redo): the seven-window cumulative-from-seam family with the clean lam=3.0;
      mature-window (lam >= 1.8) dispersion reported.
"""
import sys
import time
import numpy as np
import mpmath as mp
from scipy.linalg import eigh

sys.stdout.reconfigure(encoding="utf-8")

src = open("empirical/p_infinity/probe_pinfF_wave_limit.py", encoding="utf-8").read()
exec(src.split("def analyze")[0])
mp.mp.dps = 65
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
            rem_rel = pairs[m:][::-1]
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
            blocks = EV
    a_, b_ = pairs[-1]
    idx = [a_, b_, 0]
    T3 = [[A[i][j] for j in idx] for i in idx]
    det2 = T3[0][0] * T3[1][1] - T3[0][1] * T3[0][1]
    e0, e1 = T3[2][0], T3[2][1]
    seam_all = float(T3[2][2] - (e0 * (T3[1][1] * e0 - T3[0][1] * e1)
                                 + e1 * (T3[0][0] * e1 - T3[0][1] * e0)) / det2)
    return dict(S0=np.array(S0), radii=np.array(radii), bare0=bare0,
                R_seam=seam_all / bare0, EV=blocks, L=L, dx=dx)


print("== Y1: lam=3.0 at dps 65 ==")
t0 = time.time()
Kr3, L3 = build_point_kernel(3.0, 38)
r3 = boundary_pass(Kr3, L3, 77)
print(f"   built+passed ({time.time()-t0:.0f}s): R_seam(3.0) = {r3['R_seam']:.4e}  "
      f"S0_total = {r3['S0'][-1]:.4f}")
dmin = float(np.diff(np.concatenate([[0.0], r3["S0"]])).min())
gate1 = dmin >= -1e-10
gate2 = r3["S0"][-1] >= 0.8574 - 0.02
print(f"   sanity gates: min dS0 = {dmin:.2e} ({'ok' if gate1 else 'STARVED'});  "
      f"S0_total vs 2.5's 0.8574 ({'ok' if gate2 else 'STARVED'})")
R3 = r3["R_seam"]
y1 = gate1 and gate2 and 0.015 <= R3 <= 0.060
y1soft = gate1 and gate2 and 0.008 <= R3 <= 0.12
lams = np.array([1.5, 1.8, 2.0, 2.2, 2.35, 2.5, 3.0])
Rs = np.array([0.49558, 0.28839, 0.20639, 0.14963, 0.11299, 0.092155, R3])
if gate1 and gate2:
    cf = np.polyfit(lams**2, np.log(Rs), 1)
    resid = np.log(Rs) - np.polyval(cf, lams**2)
    per = np.diff(np.log(Rs)) / np.diff(lams**2)
    print(f"   seven-window law: c_seam = {-cf[0]:.3f}  rms = {np.sqrt(np.mean(resid**2)):.3f}")
    print("   per-interval slopes: " + "  ".join(f"{-v:.3f}" for v in per))
print("   Y1: " + ("SURVIVES -- the law extends to lam=3" if y1 else
                   ("soft-miss inside falsifier bound -- report with the slopes" if y1soft else
                    ("FALSIFIED -- law break (instrumented properly this time)"
                     if (gate1 and gate2) else "gates failed -- dps 80 required, no conclusion"))))

print("\n== Y2: the correlation orbit (renormalized boundary states) ==")
dat = np.load("empirical/p_infinity/transfer_map_orbit.npz")
seq = [1.5, 1.8, 2.0, 2.2, 2.35, 2.5]
Cs = {}
for lam in seq:
    W = dat[f"EV_{lam}"]
    d = np.sqrt(np.diag(W))
    Cs[lam] = W / np.outer(d, d)
if gate1 and gate2:
    W = r3["EV"]
    d = np.sqrt(np.diag(W))
    Cs[3.0] = W / np.outer(d, d)
    seq = seq + [3.0]
dists = []
for a, b in zip(seq[:-1], seq[1:]):
    fr = float(np.linalg.norm(Cs[a] - Cs[b]))
    ev = eigh(Cs[b], Cs[a], eigvals_only=True)
    th = float(np.max(np.abs(np.log(ev[ev > 0]))))
    dists.append((a, b, fr, th))
    print(f"   {a} -> {b}:  ||dC||_F = {fr:.3f}   D_T(corr) = {th:.3f}")
frs = [fr for _, _, fr, _ in dists]
mature = frs[1:]
bounded = all(f <= 0.5 for f in mature)
trend = len(mature) >= 3 and all(b - a > 0.1 for a, b in zip(mature[-3:], mature[-2:]))
print("   Y2 reading (rule fixed pre-run): " +
      ("CONFINED at this instrument -- bounded, no strong upward trend"
       if bounded and not trend else
       ("bounded but trending up -- flagged" if bounded else
        "NOT confined at this instrument -- reported as-is")))

print("\n== Y3: the seven-window profile family (clean lam=3.0) ==")
UGRID = np.linspace(0.02, 0.35, 12)
seam = np.load("empirical/p_infinity/transfer_map_seam.npz")
fam = [(lam, seam[f"S0_{lam}"], seam[f"rr_{lam}"],
        {1.5: 0.81093, 1.8: 1.17557, 2.0: 1.38629, 2.2: 1.57691, 2.35: 1.70838,
         2.5: 1.83258}[lam]) for lam in [1.5, 1.8, 2.0, 2.2, 2.35, 2.5]]
if gate1 and gate2:
    fam.append((3.0, r3["S0"], r3["radii"], L3))
rows = []
for lam, S0, rr, L in fam:
    u = L / 2 - rr
    dS_ = np.diff(np.concatenate([[0.0], S0]))
    o = np.argsort(u)
    cums = np.cumsum(dS_[o])
    prof = np.interp(UGRID, u[o], cums)
    rows.append((lam, prof / max(cums[-1], 1e-30)))
P = np.vstack([p for lam, p in rows if lam >= 1.8])
disp = float(np.mean(P.std(0) / np.maximum(P.mean(0), 1e-9)))
for lam, p in rows:
    print(f"   lam={lam}: " + " ".join(f"{v:.2f}" for v in p[::3]))
print(f"   mature-window dispersion (lam >= 1.8) = {disp:.3f}")

np.savez("empirical/p_infinity/transfer_map_v5.npz",
         R_seam3=np.array([R3]), S0_3=r3["S0"], rr_3=r3["radii"],
         EV_3=(r3["EV"] if r3["EV"] is not None else np.zeros((JSH + 1, JSH + 1))),
         corr_dists=np.array([[a, b, fr, th] for a, b, fr, th in dists]))

print("\nRESULT: " + ("GREEN" if (y1 or y1soft) else "PARTIAL") +
      " -- Y1/Y2/Y3 above (GPD: corpses of X1/X2 retained in v4 log)")
