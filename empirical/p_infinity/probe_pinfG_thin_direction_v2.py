"""probe_pinfG_thin_direction_v2.py -- queue item (i), corrected instrument.

V1 POST-MORTEM (corpse retained): the v1 single-vector reading is F64-5-NONCOMPLIANT --
the crossing modes of K(s*) form a NEAR-DEGENERATE CLUSTER (diagnostic at lam'=2.4166:
two starts converged to distinct near-null vectors, theta = 1.2e-20 and 9.8e-22, mutual
overlap 1.7e-10), and v1's run values were not reproducible in a clean rerun (its
theta's matched no near-null mode; concurrent-run environment suspected, unresolved --
superseded).  The invariant object is the BOTTOM-SUBSPACE-AVERAGED SPECTRAL PROFILE:
P_3(omega) = (1/3) sum_{k<=3} |v_k-hat(omega)|^2 -- rotation-invariant within the
cluster, deflation-honest.

PRE-REGISTERED:
  TD1' (instrument): each deflated vector an exact eigenpair (residual <= 1e-30 rel);
      thetas printed with s* per window (the lookup audited in-log).
  TD2' (stabilization): cross-window overlaps of sqrt P_3 on the common omega-grid;
      dominant omega*; sub-gamma_1 prediction logged (G.4 anatomy: the rescued band).
  TD3' (anatomy): subspace parity share; radial localization.
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

mp.mp.dps = 65
PAIRS = [1.8, 2.0, 2.2, 2.35, 2.5]
zs = np.load(HERE + "pinfG_margin_law.npz")
LAMPS = [float(x) for x in zs["lamps"]]
LOGS = [float(x) for x in zs["log10_sstar"]]


def inv_iter_defl(K, dim, prev, seed, iters=25):
    rng = np.random.default_rng(seed)
    x = mp.matrix(dim, 1)
    for i in range(dim):
        x[i] = mp.mpf(float(rng.uniform(-1, 1)))
    for v in prev:                       # deflate start
        c = mp.fsum(x[i] * v[i] for i in range(dim))
        for i in range(dim):
            x[i] -= c * v[i]
    for _ in range(iters):
        y = mp.lu_solve(K, x)
        for v in prev:                   # deflate each step
            c = mp.fsum(y[i] * v[i] for i in range(dim))
            for i in range(dim):
                y[i] -= c * v[i]
        nrm = mp.sqrt(mp.fsum(y[i]**2 for i in range(dim)))
        x = (1 / nrm) * y
    theta = mp.fsum(x[i] * mp.fsum(K[i, j] * x[j] for j in range(dim)) for i in range(dim))
    r = mp.matrix(dim, 1)
    for i in range(dim):
        r[i] = mp.fsum(K[i, j] * x[j] for j in range(dim)) - theta * x[i]
    res = float(mp.sqrt(mp.fsum(r[i]**2 for i in range(dim))))
    scale = float(max(abs(K[i, i]) for i in range(dim)))
    return x, float(theta), res / scale


print("== queue (i) v2: bottom-SUBSPACE thin direction at the crossings (dps=65) ==\n")
OUT = {}
for lam in PAIRS:
    t0 = time.time()
    W = build_window(lam)
    dim, Np, Lp = W["dim"], W["Np"], float(W["Lp"])
    lamp = float(W["lamp"])
    j = int(np.argmin([abs(k - lamp) for k in LAMPS]))
    le = LOGS[j]
    s_star = mp.power(10, mp.mpf(repr(le)))
    print(f"   lam'={lamp:.5f}: s* lookup -> window {LAMPS[j]:.5f}, log10 s* = {le:.3f}")
    Ks = W["K_true"] + s_star * (W["KA"] - W["KS"])
    vecs, ths, ress = [], [], []
    for k in range(3):
        v, th, rs = inv_iter_defl(Ks, dim, vecs, seed=100 + k)
        vecs.append(v)
        ths.append(th)
        ress.append(rs)
    B = _BCACHE[(dim, mp.mp.dps)]
    P = np.zeros(Np + 1)
    ev_tot, tot = 0.0, 0.0
    rad = 2 * np.abs(np.arange(dim) / dim - 0.5)
    rbar_n, rbar_d = 0.0, 0.0
    for v in vecs:
        vh = B * v
        for k in range(0, Np + 1):
            a = abs(vh[Np + k])**2
            b = abs(vh[Np - k])**2 if k > 0 else 0
            P[k] += float(a + b) / 3
        ev_tot += sum(float(((v[i] + v[(dim - i) % dim]) / 2)**2) for i in range(dim))
        tot += sum(float(v[i]**2) for i in range(dim))
        w2 = np.array([float(v[i]**2) for i in range(dim)])
        rbar_n += float((rad * w2).sum())
        rbar_d += float(w2.sum())
    P /= P.sum()
    om = 2 * np.pi * np.arange(Np + 1) / Lp
    om_star = om[int(np.argmax(P))]
    OUT[lamp] = dict(P=P, om=om, om_star=om_star, even=ev_tot / tot,
                     rbar=rbar_n / rbar_d, ths=ths, ress=ress, Lp=Lp)
    print(f"      ({time.time()-t0:.0f}s) thetas: " + "  ".join(f"{t:.2e}" for t in ths)
          + "   res: " + "  ".join(f"{r:.0e}" for r in ress))
    print(f"      omega* = {om_star:.2f}   even-share = {ev_tot/tot:.3f}   rad-center = "
          f"{rbar_n/rbar_d:.3f}   top-P: "
          + "  ".join(f"({om[i]:.1f},{P[i]:.2f})" for i in np.argsort(P)[-4:][::-1]))

print("\n== TD1': instrument ==")
td1 = all(max(OUT[l]["ress"]) <= 1e-30 for l in OUT)
print("   max residual = " + f"{max(max(OUT[l]['ress']) for l in OUT):.1e}"
      + ("   SURVIVES" if td1 else "   FIRED -- diagnose"))

print("\n== TD2': stabilization (subspace profiles, common grid) ==")
grid = np.arange(0, 60.0, 0.5)
prof = {}
for l in OUT:
    q = np.interp(grid, OUT[l]["om"], np.sqrt(OUT[l]["P"]), right=0)
    prof[l] = q / np.linalg.norm(q)
ls = sorted(OUT)
for a in ls:
    print("   " + f"{a:.3f}: " + "  ".join(f"{float(np.dot(prof[a], prof[b])):.3f}" for b in ls))
print("   omega*: " + "  ".join(f"{OUT[l]['om_star']:.2f}" for l in ls)
      + "   (gamma_1 = 14.13)")
print("   even-share: " + "  ".join(f"{OUT[l]['even']:.3f}" for l in ls)
      + "   rad-center: " + "  ".join(f"{OUT[l]['rbar']:.3f}" for l in ls))

np.savez(HERE + "pinfG_thin_direction_v2.npz",
         lamps=np.array(ls),
         om_star=np.array([OUT[l]["om_star"] for l in ls]),
         even=np.array([OUT[l]["even"] for l in ls]),
         rbar=np.array([OUT[l]["rbar"] for l in ls]),
         grid=grid, profs=np.array([prof[l] for l in ls]),
         thetas=np.array([OUT[l]["ths"] for l in ls]))
print("\nARCHIVED: pinfG_thin_direction_v2.npz")
