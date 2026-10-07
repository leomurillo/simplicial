"""probe_pinfG_ir_locality.py -- the frequency-locality of the conspiracy (the
7-dim-reduction decider; section 13.5's queued Markov question, made well-posed).

THE OBJECT.  S_IR^(J)(lambda) = the conditional form of the IR block V_3 given only the
next J frequency shells (the Fourier vectors with 3 < k <= 3+J), interpolating from the
raw IR block (J = 0) to the exact S_IR (J = N-3: the Fourier vectors span the grid).
The J-convergence profile of the bottom margin measures HOW MUCH UV the conspiracy
needs -- the frequency-space analogue of the chain's spatial locality (F.21).

THE DICHOTOMY (registered):
  - J*(lambda) bounded (a fixed UV neighborhood suffices at every window) -> the crawl
    is a FINITE-DIMENSIONAL flow (the 7+2J* reduction exists; section 13.5's Markov
    program lives);
  - J*(lambda) grows (e.g. ~ lambda^2, tracking the arrival count) -> the conspiracy is
    genuinely full-band; the finite-dim reduction dies (decisive corpse; the renewal
    keeps growing memory).

PRE-REGISTERED:
  L1 (instrument): at J = full, the margins reproduce the T1 exact values (pinfG_ir_
      ladder.npz) to <= 1e-6 relative.  Fired -> basis/machinery bug, HALT.
  L2 (the reading): J*(lambda) = min J with bottom-margin within x2 of exact, per
      window; its growth verdict.
  L3 (anatomy): the convergence profile margin(J)/margin(exact) per window -- sudden
      collapse at some J (a shell that carries the conspiracy) vs gradual.
Windows: 1.8, 2.2361, 2.6926 (dps 65).  J in {0, 1, 2, 4, 8, 16, 32, full}.
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
HERE = "empirical/p_infinity/"

src = open(HERE + "probe_pinfG_cubic_drift_v2.py", encoding="utf-8").read()
exec(src[src.index("def primes_upto"):src.index("# ---------------------------------------------------------------- W0c")])

WINDOWS = [(1.8, 20, 65), (2.2361, 28, 65), (2.6926, 34, 65)]
zT1 = np.load(HERE + "pinfG_ir_ladder.npz")
T1 = {float(l): (zT1["me"][i], zT1["mo"][i]) for i, l in enumerate(zT1["lams"])}


def fourier_basis(dim, Kmax):
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


print("== IR frequency-locality: how much UV does the conspiracy need? ==\n")
OUT = {}
for lam, N, dps in WINDOWS:
    t0 = time.time()
    mp.mp.dps = dps
    Q, L, pj = build_QW_mode(mp.mpf(repr(lam)), N, "true")
    K = to_point(Q, N)
    dim = 2 * N + 1
    vs = fourier_basis(dim, N)          # complete basis (2N+1 vectors)
    # K in the Fourier basis: Ktil[a,b] = v_a^T K v_b  (one pass of matvecs)
    nv = len(vs)
    KV = []
    for _, _, v in vs:
        w = mp.matrix(dim, 1)
        for i in range(dim):
            w[i] = mp.fsum(K[i, j] * v[j] for j in range(dim))
        KV.append(w)
    Ktil = mp.zeros(nv, nv)
    for a in range(nv):
        for b in range(a, nv):
            Ktil[a, b] = Ktil[b, a] = mp.fsum(vs[a][2][i] * KV[b][i] for i in range(dim))
    idx_ir = [a for a, (t, k, _) in enumerate(vs) if k <= 3]
    res = {}
    Js = [0, 1, 2, 4, 8, 16, 32, N - 3]
    for J in Js:
        if J > N - 3:
            continue
        idx_uv = [a for a, (t, k, _) in enumerate(vs) if 3 < k <= 3 + J]
        nI, nU = len(idx_ir), len(idx_uv)
        A = mp.zeros(nI, nI)
        for ai, a in enumerate(idx_ir):
            for bi, b in enumerate(idx_ir):
                A[ai, bi] = Ktil[a, b]
        if nU:
            B = mp.zeros(nI, nU)
            C = mp.zeros(nU, nU)
            for ai, a in enumerate(idx_ir):
                for bi, b in enumerate(idx_uv):
                    B[ai, bi] = Ktil[a, b]
            for ai, a in enumerate(idx_uv):
                for bi, b in enumerate(idx_uv):
                    C[ai, bi] = Ktil[a, b]
            S = mp.zeros(nI, nI)
            for ci in range(nI):
                for cj in range(nI):
                    S[ci, cj] = A[ci, cj]
            for cj in range(nI):
                rhs = mp.matrix(nU, 1)
                for r in range(nU):
                    rhs[r] = B[cj, r]
                x = mp.lu_solve(C, rhs)
                for ci in range(nI):
                    S[ci, cj] -= mp.fsum(B[ci, r] * x[r] for r in range(nU))
        else:
            S = A
        evs = eig_sym_mp(S)
        res[J] = evs[0]
    OUT[lam] = dict(res=res, Js=[J for J in Js if J <= N - 3], N=N)
    exact = T1[min(T1, key=lambda k: abs(k - lam))][0][0]
    print(f"   lam={lam} (dim={dim}, {time.time()-t0:.0f}s): exact bottom = {exact:.3e}")
    for J in OUT[lam]["Js"]:
        r = res[J] / exact
        print(f"      J={J:>3}: bottom = {res[J]:+.3e}   ratio to exact = {r:+.3e}")

print("\n== L1: instrument (J=full vs T1 exact) ==")
l1 = True
for lam, N, _ in WINDOWS:
    exact = T1[min(T1, key=lambda k: abs(k - lam))][0][0]
    full = OUT[lam]["res"][N - 3]
    rel = abs(full - exact) / exact
    l1 &= rel <= 1e-6
    print(f"   lam={lam}: rel = {rel:.1e}")
print("   L1: " + ("SURVIVES" if l1 else "FIRED -- machinery bug"))

print("\n== L2: J*(lambda) (min J with bottom within x2 of exact) ==")
for lam, N, _ in WINDOWS:
    exact = T1[min(T1, key=lambda k: abs(k - lam))][0][0]
    Jstar = None
    for J in OUT[lam]["Js"]:
        if OUT[lam]["res"][J] > 0 and OUT[lam]["res"][J] <= 2 * exact:
            Jstar = J
            break
    print(f"   lam={lam}: J* = {Jstar}   (N-3 = {N-3})")

np.savez(HERE + "pinfG_ir_locality.npz",
         lams=np.array([w[0] for w in WINDOWS]),
         Js=np.array([0, 1, 2, 4, 8, 16, 32]),
         bottoms=np.array([[float(OUT[w[0]]["res"].get(J, np.nan))
                            for J in [0, 1, 2, 4, 8, 16, 32]] for w in WINDOWS]),
         full=np.array([float(OUT[w[0]]["res"][w[1] - 3]) for w in WINDOWS]))
print("\nARCHIVED: pinfG_ir_locality.npz")
