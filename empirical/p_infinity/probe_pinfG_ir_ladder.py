"""probe_pinfG_ir_ladder.py -- target T1 (leverage 1): the IR-BLOCK FUNCTIONAL LADDER.

THE OBJECT (prescribed by the section 12.1 identification: thin direction = the window's
infrared sector).  For the IR subspace V_K = span{c_0, c_1..c_K, s_1..s_K} (point-basis
Fourier vectors c_k[i] = sqrt(2/dim) cos(2 pi k i/dim), s_k likewise sin, c_0 = 1/sqrt(dim);
orthonormal), the CONDITIONAL FORM of the IR block given the rest of the window is
    S_IR = ((K^{-1})_VV)^{-1}   computed as   G = V^T K^{-1} V (one LU, 2K+1 solves),
    S_IR = G^{-1};   lambda_min(S_IR) = 1/lambda_max(G).
Its parity-blocked eigenvalues (even (K+1)x(K+1), odd KxK) are THE FOUR-COORDINATE
LADDER at K = 3: the conditional margins of the lowest-frequency window content -- and
the kernel rows feeding them are EXPLICIT PRIME SUMS (the builder's S[k], D[k] at
k <= 3: Fejer-weighted Lambda(n) n^{-1/2} sums at the slow frequencies 2 pi k/L).
The lam -> inf uniformity of these margins IS the crawl, in explicit coordinates.

PRE-REGISTERED:
  IR0 (validity): K_true PSD per window; G symmetric-PD; parity cross-block of G
      <= 1e-30 relative.  Fired -> halt window.
  IR1 (the identification weld, REGISTERED RULE): capture ratio
      lambda_min(S_IR^(K=3)) / lambda_min(K) <= 10 at every window (lambda_min(K) by
      10-step inverse iteration; interlacing guarantees ratio >= 1).  Fired -> the IR
      block fails to capture the global bottom at that window: the section 12.1
      identification has a hole (finding).
  IR2 (the ladder): per window, the even/odd conditional margins; their lambda-laws.
  IR3 (the explicit coordinates): the prime-side moments -- the builder's P-content at
      k = 0..3 -- displayed per window (the classical face of the four coordinates).
  IR4 (capture depth): the ratio of IR1 at K = 1, 2, 3, 4 -- the thin direction's
      bandwidth, measured.
Windows: 1.8, 2.0591, 2.2361, 2.4166, 2.5539, 2.6926 (dps 65) + 3.5 (dps 110).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

WINDOWS = [(1.8, 20, 65), (2.0591, 25, 65), (2.2361, 28, 65), (2.4166, 31, 65),
           (2.5539, 32, 65), (2.6926, 34, 65), (3.5, 43, 110)]


def ir_vectors(dim, Kmax):
    """Orthonormal point-basis Fourier vectors: [c_0, c_1..c_K, s_1..s_K]."""
    vs = []
    c0 = mp.matrix(dim, 1)
    for i in range(dim):
        c0[i] = 1 / mp.sqrt(dim)
    vs.append(("c", 0, c0))
    for k in range(1, Kmax + 1):
        ck = mp.matrix(dim, 1)
        sk = mp.matrix(dim, 1)
        for i in range(dim):
            ang = 2 * mp.pi * k * i / dim
            ck[i] = mp.sqrt(mp.mpf(2) / dim) * mp.cos(ang)
            sk[i] = mp.sqrt(mp.mpf(2) / dim) * mp.sin(ang)
        vs.append(("c", k, ck))
        vs.append(("s", k, sk))
    return vs


def eig_sym_mp(M):
    E, _ = mp.eigsy(M)
    return sorted(float(E[i]) for i in range(M.rows))


print("== T1: the IR-block functional ladder ==\n")
OUT = {}
for lam, N, dps in WINDOWS:
    t0 = time.time()
    mp.mp.dps = dps
    lam_mp = mp.mpf(repr(lam))
    Q, L, pj = build_QW_mode(lam_mp, N, "true")
    K = to_point(Q, N)
    dim = 2 * N + 1
    psd = cholesky_psd(K)
    # IR3: the explicit prime-side moments (Q-basis diagonals/off at k<=3)
    irD = [float(Q[N + k, N + k]) for k in range(0, 4)]
    # solves for K = 4 (covers IR4's nesting)
    vs = ir_vectors(dim, 4)
    sols = [mp.lu_solve(K, v) for _, _, v in vs]
    nV = len(vs)
    G = mp.zeros(nV, nV)
    for a in range(nV):
        for b in range(a, nV):
            G[a, b] = G[b, a] = mp.fsum(vs[a][2][i] * sols[b][i] for i in range(dim))
    # global bottom by inverse iteration (10 steps from the c0+noise start)
    x = mp.matrix(dim, 1)
    rng = np.random.default_rng(5)
    for i in range(dim):
        x[i] = mp.mpf(float(rng.uniform(-1, 1)))
    for _ in range(10):
        y = mp.lu_solve(K, x)
        nrm = mp.sqrt(mp.fsum(y[i]**2 for i in range(dim)))
        x = (1 / nrm) * y
    lam_min = float(mp.fsum(x[i] * mp.fsum(K[i, j] * x[j] for j in range(dim))
                            for i in range(dim)))
    # capture ratios at K = 1..4 (sub-Grams; lambda_min(S_IR) = 1/lambda_max(G_sub))
    caps = {}
    for Km in (1, 2, 3, 4):
        idx = [a for a, (t, k, _) in enumerate(vs) if k <= Km]
        Gs = mp.zeros(len(idx), len(idx))
        for ai, a in enumerate(idx):
            for bi, b in enumerate(idx):
                Gs[ai, bi] = G[a, b]
        evs = eig_sym_mp(Gs)
        caps[Km] = (1 / evs[-1]) / lam_min
    # the K=3 parity-blocked margins
    idx_e = [a for a, (t, k, _) in enumerate(vs) if k <= 3 and t == "c"]
    idx_o = [a for a, (t, k, _) in enumerate(vs) if k <= 3 and t == "s"]
    cross = mp.mpf(0)
    scale = mp.mpf(0)
    for a in idx_e:
        for b in idx_o:
            cross = max(cross, abs(G[a, b]))
    for a in idx_e + idx_o:
        scale = max(scale, abs(G[a, a]))
    Ge = mp.zeros(len(idx_e), len(idx_e))
    for ai, a in enumerate(idx_e):
        for bi, b in enumerate(idx_e):
            Ge[ai, bi] = G[a, b]
    Go = mp.zeros(len(idx_o), len(idx_o))
    for ai, a in enumerate(idx_o):
        for bi, b in enumerate(idx_o):
            Go[ai, bi] = G[a, b]
    # margins = eigenvalues of S_blocks = reciprocals of G-block eigenvalues
    me = sorted(1 / e for e in eig_sym_mp(Ge))
    mo = sorted(1 / e for e in eig_sym_mp(Go))
    OUT[lam] = dict(psd=psd, lam_min=lam_min, caps=caps, me=me, mo=mo,
                    cross=float(cross / scale), irD=irD)
    print(f"   lam={lam:<7} (dim={dim}, dps={dps}, {time.time()-t0:.0f}s): "
          f"PSD={'OK' if psd else 'FAIL'}  lam_min(K)={lam_min:.3e}  "
          f"G-cross={float(cross/scale):.1e}")
    print(f"      capture ratio K=1..4: " + "  ".join(f"{caps[k]:.3f}" for k in (1, 2, 3, 4)))
    print(f"      even margins (K=3): " + "  ".join(f"{m:.3e}" for m in me))
    print(f"      odd  margins (K=3): " + "  ".join(f"{m:.3e}" for m in mo))
    print(f"      IR3 prime-moment diag D[0..3]: " + "  ".join(f"{d:+.4f}" for d in irD))

print("\n== IR0/IR1 verdicts ==")
ir0 = all(OUT[l]["psd"] and OUT[l]["cross"] <= 1e-30 for l, _, _ in WINDOWS)
print("   IR0: " + ("SURVIVES" if ir0 else "FIRED"))
ir1 = all(OUT[l]["caps"][3] <= 10 for l, _, _ in WINDOWS)
print("   IR1 (K=3 capture <= 10): " + ("SURVIVES -- the IR block holds the global bottom"
      if ir1 else "FIRED at some window -- identification hole (see table)"))

print("\n== IR2: the ladder laws ==")
ls = [l for l, _, _ in WINDOWS]
for tag, key in [("even bottom", "me"), ("odd bottom", "mo")]:
    ys = np.array([OUT[l][key][0] for l in ls])
    print(f"   {tag}: " + "  ".join(f"{y:.2e}" for y in ys))
print("   lam_min(K): " + "  ".join(f"{OUT[l]['lam_min']:.2e}" for l in ls))

np.savez(HERE + "pinfG_ir_ladder.npz",
         lams=np.array(ls),
         lam_min=np.array([OUT[l]["lam_min"] for l in ls]),
         cap=np.array([[OUT[l]["caps"][k] for k in (1, 2, 3, 4)] for l in ls]),
         me=np.array([OUT[l]["me"] for l in ls]),
         mo=np.array([OUT[l]["mo"] for l in ls]),
         irD=np.array([OUT[l]["irD"] for l in ls]))
print("\nARCHIVED: pinfG_ir_ladder.npz")
