"""probe_pinfG_thin_direction.py -- queue item (i): the thin-direction stabilization
measurement (the cornering reformulation of P-inf-G section 11.3).

THE OBJECT.  The cone's THIN DIRECTION at window lam' = the mode that dies first along
the physical arrival-swap path: the near-null vector of K(s*) = K_true + s* (KA - KS),
with s* the measured crossing (probe_pinfG_margin_law, G.4'').  NOTE: this is NOT the
bottom eigenvector of K_true -- the margin law showed s* >> eps/O(1), i.e. the arrival
direction decouples from the bottom rung; the binding mode is interior to the ladder.

THE QUESTION.  Does the thin direction STABILIZE across windows (a fixed symbol in the
frequency frame)?  If yes, RH's open step = the boundedness of ONE explicit prime
functional sequence (the thin-direction pairing) with budget s*(lam) -- the most
concrete face available.  Per the two-regime lesson these are unconditional objects;
the deliverable is the stabilization reading, not a discrimination.

PRE-REGISTERED:
  TD1 (instrument): inverse-iteration residual ||K(s*)v - theta v||/||K(s*)|| <= 1e-20
      relative to scale; two independent starts agree to overlap >= 0.99.
      Fired -> the crossing mode is degenerate/cluster at this resolution: report the
      subspace caveat (F64-5) and read profiles only.
  TD2 (the stabilization reading): dominant frequency omega* per window; cross-window
      overlap matrix of the spectral profiles |v-hat(omega)| on a common grid.
      Stabilization = overlaps rising toward 1 with lam.  Logged prediction (not a
      falsifier): the G.4/F.4 anatomy puts the rescued band BELOW gamma_1 = 14.13 --
      omega* expected in the sub-gamma_1 band.
  TD3 (anatomy): parity share of v (even/odd), y-localization (boundary band vs bulk;
      the section 23.2 Q3 band r >~ 0.78 expected).
Machinery: v2-lineage builds at the five lam' windows with measured s*; dps 65;
inverse iteration via mp LU (the near-singular K(s*) is ideal for it).
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
SSTAR = {float(l): float(s) for l, s in zip(zs["lamps"], zs["log10_sstar"])}


def inv_iter(K, dim, start, iters=40):
    x = mp.matrix(dim, 1)
    for i in range(dim):
        x[i] = mp.mpf(start[i])
    for _ in range(iters):
        y = mp.lu_solve(K, x)
        nrm = mp.sqrt(mp.fsum(y[i]**2 for i in range(dim)))
        x = (1 / nrm) * y
    theta = mp.fsum(x[i] * mp.fsum(K[i, j] * x[j] for j in range(dim)) for i in range(dim))
    r = mp.matrix(dim, 1)
    for i in range(dim):
        r[i] = mp.fsum(K[i, j] * x[j] for j in range(dim)) - theta * x[i]
    res = float(mp.sqrt(mp.fsum(r[i]**2 for i in range(dim))))
    scale = float(max(abs(K[i, i]) for i in range(dim)))
    return x, float(theta), res / scale


print("== queue (i): the thin direction at the measured crossings (dps=65) ==\n")
OUT = {}
for lam in PAIRS:
    t0 = time.time()
    W = build_window(lam)
    dim, Np, Lp = W["dim"], W["Np"], float(W["Lp"])
    lamp = float(W["lamp"])
    s_star = mp.power(10, mp.mpf(repr(SSTAR[round(lamp, 4)] if round(lamp, 4) in SSTAR
                                      else min(SSTAR, key=lambda k: abs(k - lamp)))))
    Ks = W["K_true"] + s_star * (W["KA"] - W["KS"])
    rng = np.random.default_rng(11)
    v1, th1, r1 = inv_iter(Ks, dim, [1.0] * dim)
    v2, th2, r2 = inv_iter(Ks, dim, list(rng.uniform(-1, 1, dim)))
    ov = abs(float(mp.fsum(v1[i] * v2[i] for i in range(dim))))
    # spectral profile: v-hat = B v (B cached by to_point at this dim/dps)
    B = _BCACHE[(dim, mp.mp.dps)]
    vh = B * v1
    P = np.zeros(Np + 1)
    for k in range(0, Np + 1):
        a = abs(vh[Np + k])**2
        b = abs(vh[Np - k])**2 if k > 0 else 0
        P[k] = float(a + b)
    P /= P.sum()
    om = 2 * np.pi * np.arange(Np + 1) / Lp
    om_star = om[int(np.argmax(P))]
    # parity + localization
    ev = sum(float(((v1[i] + v1[(dim - i) % dim]) / 2)**2) for i in range(dim))
    tot = sum(float(v1[i]**2) for i in range(dim))
    xs = np.arange(dim) / dim
    rad = 2 * np.abs(xs - 0.5)               # 0 = center, 1 = wrap/edge
    w2 = np.array([float(v1[i]**2) for i in range(dim)])
    rbar = float((rad * w2).sum() / w2.sum())
    OUT[lamp] = dict(P=P, om=om, om_star=om_star, even=ev / tot, rbar=rbar,
                     th=th1, res=r1, ov=ov, Lp=Lp)
    print(f"   lam'={lamp:.4f} (dim={dim}, {time.time()-t0:.0f}s): theta={th1:.2e} "
          f"res={r1:.1e} two-start-ov={ov:.6f}")
    print(f"      omega* = {om_star:.2f}   even-share = {ev/tot:.3f}   "
          f"radial center = {rbar:.3f}   top-P: "
          + "  ".join(f"({om[i]:.1f},{P[i]:.2f})" for i in np.argsort(P)[-4:][::-1]))

print("\n== TD1: instrument ==")
td1 = all(OUT[l]["res"] <= 1e-20 and OUT[l]["ov"] >= 0.99 for l in OUT)
print("   " + ("SURVIVES" if td1 else
               "FIRED -- near-degenerate crossing mode (F64-5 caveat: profiles only)"))

print("\n== TD2: stabilization (common-grid overlaps of sqrt-profiles) ==")
grid = np.arange(0, 60.0, 0.5)
prof = {}
for l in OUT:
    q = np.interp(grid, OUT[l]["om"], np.sqrt(OUT[l]["P"]), right=0)
    prof[l] = q / np.linalg.norm(q)
ls = sorted(OUT)
print("   overlap matrix:")
for a in ls:
    print("   " + f"{a:.3f}: " + "  ".join(f"{float(np.dot(prof[a], prof[b])):.3f}" for b in ls))
print("   omega* sequence: " + "  ".join(f"{OUT[l]['om_star']:.2f}" for l in ls)
      + f"   (gamma_1 = 14.13; sub-gamma_1 prediction logged)")

np.savez(HERE + "pinfG_thin_direction.npz",
         lamps=np.array(ls),
         om_star=np.array([OUT[l]["om_star"] for l in ls]),
         even=np.array([OUT[l]["even"] for l in ls]),
         rbar=np.array([OUT[l]["rbar"] for l in ls]),
         grid=grid, profs=np.array([prof[l] for l in ls]),
         theta=np.array([OUT[l]["th"] for l in ls]),
         res=np.array([OUT[l]["res"] for l in ls]))
print("\nARCHIVED: pinfG_thin_direction.npz")
