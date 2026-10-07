"""
Paper 56, O2 post-diagnosis (NOT BLIND): is the apex Bisognano-Wichmann overshoot an infrared (finite-box) effect?

Context: p56c_apex_mp_cert.py (run 1, 8/9) found, at R_max = 26 and 60 digits, the flat apex weight
2 D_P(0,0) / (pi R_eff / c) = 1.113 -> 1.213 for R = 6..12 (rising with R), an R-independent point mass
M_1 = 0.01172..0.01212 (max/min 1.034, K_M PASS), and mean M_1 2pi/(eta_len (pi/3) c) = 0.762 (K_eta FAILED, band
[0.8, 1.25]).  The rise of the BW ratio with R could be an IR effect of the Dirichlet wall at R_max = 26.

CRITERIA (written 2026-10-02 before this run; post-diagnosis, NOT BLIND).  Same cones, same estimator, same 60 digits,
a larger box (R_max = 36).  Two jobs: mode "flat" (k = 6: apex weights) and mode "cone5" (k = 5 apex weights, plus
k = 6 float64 entropies for the flat interpolation and eta_len).
  IR1  If the flat ratio at R = 12 drops by more than 2% relative to R_max = 26 (1.2127), the overshoot is at least
       partly infrared; if it changes by less than 1%, it is a lattice (ultraviolet) property at these radii.
  IR2  Report the K_eta ratio at the larger box and the spread max/min of M_1 over R = 6..12.
Usage: python p56d_ir_check.py Rmax dps mode       (mode = flat | cone5)
"""
import sys, time, math
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline

RMAX = int(sys.argv[1]); DPS = int(sys.argv[2]); MODE = sys.argv[3]
RS = list(range(1, 14))
src = open(__file__.replace("p56d_ir_check.py", "p56c_apex_mp_cert.py"), encoding="utf-8").read()
defs = src.split("t0 = time.time()")[0]
defs = defs.replace("DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 60", "").replace("RMAX = 26", "")
exec(defs)          # cone_graph, symmetry_maps, orbits, gauss_stuff, mp_gauss, sector_matrices (verbatim)
mp.mp.dps = DPS
t0 = time.time()
print(f"== p56d (NOT BLIND): IR check, R_max = {RMAX}, {DPS} digits, mode {MODE} ==", flush=True)

def float_entropies(k):
    K, ring, cut = cone_graph(k, RMAX)
    lam_, V = np.linalg.eigh(K)
    X = (V * (0.5 / np.sqrt(lam_))) @ V.T; P = (V * (0.5 * np.sqrt(lam_))) @ V.T
    out = []
    for R in RS:
        Af = np.where(ring <= R)[0]
        S, _, _ = gauss_stuff(X[np.ix_(Af, Af)], P[np.ix_(Af, Af)])
        out.append((len(Af), S))
    return out

def apex_weights(k):
    K, ring, cut = cone_graph(k, RMAX)
    rot, ref = symmetry_maps(k, RMAX)
    assert np.array_equal(K[np.ix_(rot, rot)], K) and np.array_equal(K[np.ix_(ref, ref)], K)
    orbs = orbits(rot, ref)
    oring = np.array([ring[o[0]] for o in orbs])
    apex = [i for i, o in enumerate(orbs) if o == [0]][0]
    Kf, Km = sector_matrices(K, orbs)
    t1 = time.time()
    E, Vm = mp.eigsy(Km)
    nsec = len(orbs)
    print(f"   k={k}: sector size {nsec}; mp eigsy {time.time() - t1:.0f} s", flush=True)
    idx13 = [i for i in range(nsec) if oring[i] <= max(RS)]
    fx = [1 / (2 * mp.sqrt(E[i])) for i in range(nsec)]
    fp = [mp.sqrt(E[i]) / 2 for i in range(nsec)]
    Xm = mp.matrix(len(idx13), len(idx13)); Pm = mp.matrix(len(idx13), len(idx13))
    for a, i in enumerate(idx13):
        for b, j in enumerate(idx13):
            if b < a:
                continue
            Xm[a, b] = Xm[b, a] = mp.fsum(Vm[i, l] * Vm[j, l] * fx[l] for l in range(nsec))
            Pm[a, b] = Pm[b, a] = mp.fsum(Vm[i, l] * Vm[j, l] * fp[l] for l in range(nsec))
    out = []
    for R in RS:
        sel = [a for a, i in enumerate(idx13) if oring[i] <= R]
        XA = mp.matrix(len(sel), len(sel)); PA = mp.matrix(len(sel), len(sel))
        for a2, a in enumerate(sel):
            for b2, b in enumerate(sel):
                XA[a2, b2] = Xm[a, b]; PA[a2, b2] = Pm[a, b]
        b0, Ssec, epsmax = mp_gauss(XA, PA, sel.index(idx13.index(apex)))
        n = int(sum(len(orbs[i]) for i in range(nsec) if oring[i] <= R))
        out.append((n, float(b0)))
        print(f"   k={k} R={R} n={n} b0={mp.nstr(b0, 12)} eps_max={mp.nstr(epsmax, 5)}", flush=True)
    return out

cl = math.sqrt(1.5)
Rarr = np.array(RS); sel6 = (Rarr >= 6) & (Rarr <= 12)
S6 = float_entropies(6)
for R, (n, S) in zip(RS, S6):
    print(f"   k=6 float64 R={R} n={n} S={S:.8f}", flush=True)
if MODE == "flat":
    w6 = apex_weights(6)
    n6 = np.array([n for n, _ in w6], float)
    Reff6 = np.sqrt(n6 * math.sqrt(3) / (2 * math.pi))
    bw6 = np.array([b for _, b in w6]) / (math.pi * Reff6 / cl)
    r26 = [1.1127, 1.125, 1.1388, 1.1532, 1.17, 1.1897, 1.2127]
    print(f"   flat BW ratios R=6..12 at R_max={RMAX}: {np.round(bw6[sel6], 4).tolist()} (R_max=26: {r26})", flush=True)
    drop = 1 - bw6[11] / 1.2127
    verdict = "partly infrared" if drop > 0.02 else ("ultraviolet (lattice)" if abs(drop) < 0.01 else "indeterminate (1-2%)")
    print(f"   IR1: relative change at R=12: {-drop:+.4f} -> {verdict}", flush=True)
else:
    S5 = float_entropies(5)
    w5 = apex_weights(5)
    spl = CubicSpline(Rarr.astype(float), np.array([S for _, S in S6]))
    def flat_S(nv):
        Rx = (-1 + math.sqrt(1 + 4 * (nv - 1) / 3)) / 2
        return float(spl(Rx))
    dS5 = np.array([S - flat_S(n) for n, S in S5])
    M1 = -dS5 / np.array([b for _, b in w5])
    m1 = M1[sel6]
    n6 = np.array([n for n, _ in S6], float)
    Reff6 = np.sqrt(n6 * math.sqrt(3) / (2 * math.pi))
    selR = (Rarr >= 4) & (Rarr <= 12)
    A_ = np.vstack([Reff6[selR], np.ones(selR.sum())]).T
    slope = np.linalg.lstsq(A_, np.array([S for _, S in S6])[selR], rcond=None)[0][0]
    eta_len = slope / (2 * math.pi)
    ratio = float(np.mean(m1)) * 2 * math.pi / (eta_len * (math.pi / 3) * cl)
    print(f"   IR2: M_1 = {np.round(m1, 6).tolist()} (max/min {m1.max() / m1.min():.4f}); K_eta ratio {ratio:.4f} "
          f"(R_max=26: 0.7623); eta_len {eta_len:.6f}", flush=True)
print(f"   done in {time.time() - t0:.0f} s")
