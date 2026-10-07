"""probe_pinfF_transfer_map_v3.py -- the stationarity strike, step 1c: graft ladder + the
mixed-cell mechanism (diagnosis blocks for v2's Q2/Q5 firings; corpses retained).

V2 STANDINGS (transfer_map_v2_run.log): Q0/Q1/Q3 SURVIVED (seam law c=0.419 rms 0.057;
boundary-band share 0.879); Q4 logged (outer pair cells BOTH bulk-pace ~2.7 -- the law's
carrier at the boundary is the single even seam site); Q2 FIRED at band edge (0.499 vs
my [0.5,1.5] -- band MIS-CENTERED: the slaved-partner prediction is 0.5, data locks onto
it); Q5 FIRED on SIGN (graft RAISED R_seam +93% -- sub-threshold off-line content shows
as EXCESS remainder, not deficit; my registered sign was wrong; kept as corpse).

PRE-REGISTERED (GPD, fixed before this run):
  V1 (two-phase violation signature): on lam=2.5, the F.14 graft family at relative
      Frobenius amplitudes [0.02, 0.05, 0.10, 0.20]: R_seam rises with amplitude in the
      shielded phase, and at SOME amplitude in the ladder the chain produces a negative
      pivot (detection/crash phase).  FALSIFIER: no negativity through amp=0.20 AND
      monotone benign rise => the ledger cannot certify violations at window 2.5
      (sensitivity-without-detection; must be reported as the instrument's limit).
  V2m (mixed-cell mechanism): print M2 = Cov((a,0) | bulk+b), bare0, bare21; the slaved
      prediction d21 -> (M2_00 + corrections)/2 with M2_aa -> 0: check M2_aa/M2_00 <= 0.25
      at lam = 2.35, 2.5 (the partner is slaved; the mixed cell's remainder is the seam's).
      FALSIFIER: M2_aa comparable to M2_00 at the late windows.
  V3m (graft anatomy, report-only): outermost-third S0-share under graft amp=0.02 vs
      clean (does off-line content change WHERE the seam is predicted from?).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")

src = open("empirical/p_infinity/probe_pinfF_wave_limit.py", encoding="utf-8").read()
exec(src.split("def analyze")[0])
mp.mp.dps = 35


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


def seam_pass_v3(Kr, L, dim):
    """As v2's seam_pass + min-pivot tracking + M2 decomposition outputs."""
    N = (dim - 1) // 2
    dx = L / dim
    pairs = [(N + 1 - m, N + m) for m in range(1, N + 1)]
    A = [row[:] for row in Kr]
    act = set(range(dim))
    bare0 = float(Kr[0][0])
    S0, radii = [], []
    minpiv = float("inf")
    for m, (ia, ib) in enumerate(pairs[:-1], start=1):
        minpiv = min(minpiv, float(A[ia][ia]))
        act -= {ia}; eliminate(A, act, ia)
        minpiv = min(minpiv, float(A[ib][ib]))
        act -= {ib}; eliminate(A, act, ib)
        S0.append(1 - float(A[0][0]) / bare0)
        radii.append((m - 0.5) * dx)
    a_, b_ = pairs[-1]
    idx = [a_, b_, 0]
    T3 = [[A[i][j] for j in idx] for i in idx]
    minpiv = min(minpiv, float(T3[0][0]))
    # seam given all
    det2 = T3[0][0] * T3[1][1] - T3[0][1] * T3[0][1]
    e0, e1 = T3[2][0], T3[2][1]
    seam_all = float(T3[2][2] - (e0 * (T3[1][1] * e0 - T3[0][1] * e1)
                                 + e1 * (T3[0][0] * e1 - T3[0][1] * e0)) / det2)
    # M2 = Cov((a,0) | bulk + b)
    m2 = [[float(T3[i][j] - T3[i][1] * T3[j][1] / T3[1][1]) for j in (0, 2)] for i in (0, 2)]
    bare21 = float((Kr[a_][a_] + Kr[0][0]) / 2 + Kr[a_][0])
    d21 = (m2[0][0] + m2[1][1]) / 2 + m2[0][1]
    return dict(S0=np.array(S0), radii=np.array(radii), bare0=bare0,
                seam_all=seam_all, R_seam=seam_all / bare0, M2=m2, bare21=bare21,
                d21=d21, R21=d21 / bare21, minpiv=minpiv)


print("== build lam=2.5 (mp dps=35) ==")
t0 = time.time()
lam, N = 2.5, 32
Kr, L = build_point_kernel(lam, N)
dim = 2 * N + 1
print(f"   built ({time.time()-t0:.0f}s)")

clean = seam_pass_v3(Kr, L, dim)
print(f"   clean: R_seam={clean['R_seam']:.4e}  R21={clean['R21']:.4e}  "
      f"minpiv={clean['minpiv']:.3e}")

print("\n== V2m: the mixed-cell mechanism (M2 decomposition, lam=2.35 and 2.5) ==")
Kr235, L235 = build_point_kernel(2.35, 30)
c235 = seam_pass_v3(Kr235, L235, 61)
v2m = True
for tag, c in (("2.35", c235), ("2.5", clean)):
    M2 = c["M2"]
    ratio = M2[0][0] / M2[1][1]
    ok = ratio <= 0.25
    v2m &= ok
    print(f"   lam={tag}: M2_aa={M2[0][0]:.4e}  M2_00={M2[1][1]:.4e}  M2_a0={M2[0][1]:.4e}"
          f"  bare0={c['bare0']:.3f}  bare21={c['bare21']:.3f}")
    print(f"            M2_aa/M2_00 = {ratio:.3f}  (slaved-partner criterion <= 0.25: "
          + ("ok" if ok else "OUT") + ")")
    print(f"            d21 = {c['d21']:.4e} vs seam_all/2 = {c['seam_all']/2:.4e}"
          f"  (slaved prediction ratio {c['d21']/(c['seam_all']/2):.3f})")
print("   V2m: " + ("SURVIVES -- the partner is slaved; the mixed cell IS the seam"
                    if v2m else "FIRED -- partner not slaved; decompose further"))

print("\n== V1: the graft amplitude ladder (two-phase signature) ==")
x = [i * L / dim for i in range(dim)]
nrmK = np.sqrt(sum(float(Kr[i][j])**2 for i in range(dim) for j in range(dim)))
raw = [[(x[i] - x[j])**2 * 2 * np.cos(17.5 * (x[i] - x[j])) for j in range(dim)]
       for i in range(dim)]
nrmG = np.sqrt(sum(raw[i][j]**2 for i in range(dim) for j in range(dim)))
rows = []
for rel in (0.02, 0.05, 0.10, 0.20):
    amp = rel * nrmK / nrmG
    Kg = [[Kr[i][j] + mp.mpf(float(amp * raw[i][j])) for j in range(dim)] for i in range(dim)]
    rg = seam_pass_v3(Kg, L, dim)
    rows.append((rel, rg))
    crash = rg["minpiv"] < 0 or rg["seam_all"] < 0
    print(f"   amp={rel:.2f}: R_seam={rg['R_seam']:+.4e}  R21={rg['R21']:+.4e}  "
          f"minpiv={rg['minpiv']:+.3e}" + ("   <-- NEGATIVE (crash phase)" if crash else ""))
rise = all(rg["R_seam"] > clean["R_seam"] for rel, rg in rows[:2])
crashed = any(rg["minpiv"] < 0 or rg["seam_all"] < 0 for _, rg in rows)
v1 = rise and crashed
print("   V1: " + ("SURVIVES -- two-phase signature: excess remainder (shielded) then "
                   "negativity (detection)" if v1 else
                   ("PARTIAL: rise without crash -- sensitivity without detection at this "
                    "window (report as instrument limit)" if rise else
                    "FIRED -- see ladder")))

print("\n== V3m: graft anatomy (where is the grafted seam predicted from?) ==")
rg02 = rows[0][1]
for tag, c in (("clean", clean), ("graft02", rg02)):
    dS = np.diff(np.concatenate([[0.0], c["S0"]]))
    tot = c["S0"][-1]
    third = c["radii"] >= (2 / 3) * c["radii"][-1]
    print(f"   {tag}: S0_total={tot:.4f}  outer-third share={float(dS[third].sum()/tot):.3f}")

print("\nRESULT: " + ("GREEN -- mechanism + two-phase detection certified"
                      if (v1 and v2m) else "PARTIAL -- see blocks (GPD: diagnose, retain)"))
