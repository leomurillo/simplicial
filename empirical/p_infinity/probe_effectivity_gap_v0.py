"""probe_effectivity_gap_v0.py — the effectivity-gap instrument (P-infinity-C, pillar IV probe). v0.

THE QUESTION (Saturation, the RR step of the Castelnuovo map): is every NUMERICALLY POSITIVE class
of the scaling square EFFECTIVE — representable by a pointwise-positive correspondence profile h >= 0?
Over F_q this is what Riemann-Roch delivers and it is the sole non-formal input of Weil's proof
besides geometric positivity (certified GREEN in probe_castelnuovo_geometric_positivity.py).

FINITE INSTRUMENT.  Fix a primitive direction w (pole-killed signed bump combo) and the ample class
H (broad positive bump).  The class v(eps) = w + eps*H turns numerically positive at
   eps_0 = unique positive root of  B(w,w) + 2 eps B(w,H) + eps^2 B(H,H) = 0
(B = the intersection pairing, computed from the LOCAL side: primes + archimedean kernel — so the
form knows the true zeros).  Saturation demands: for every eps > eps_0 the class v(eps) is effective.
Finite necessary test: effective-representability against K probe functionals —
   exists c >= 0 :  B(sum_i c_i G_i - v(eps), phi_k) = 0  for k = 1..K        (an LP)
giving the effectivity threshold eps*(K) = min feasible eps.  SATURATION PREDICTS eps*(K) <= eps_0
for all K (the effective cone CONTAINS the positive cone; it may be larger).  A persistent crossing
eps*(K) > eps_0 as K grows FALSIFIES saturation along w — the route's registered kill criterion.

v0: float64 engine (Gaussian closed forms; archimedean symbol on a grid), single width s = 0.15,
dictionary n = 36, probe ladder K = 6, 10, 14, 18, two primitive directions.  Spot-checked against
the mpmath certified engine.  No torch.  Deterministic.
"""
import numpy as np
from scipy.special import digamma
from scipy.optimize import linprog
from sympy import factorint

S = 0.15                      # common bump width (x = log lambda)
SQ2PI = np.sqrt(2*np.pi)

# ---------------- the pairing kernel  B(G_a, G_b) = Kk(a - b)  (single width) ----------------
# poles:  ghat(0)hhat(1)+ghat(1)hhat(0) appear on BOTH sides of the certified identity and cancel
# against A_inf; the LOCAL form of the pairing is  primes + arch  (probe_castelnuovo: GREEN).
rgrid = np.linspace(0, 40, 4001)
Lr = np.real(digamma(0.25 + 0.5j*rgrid)) - np.log(np.pi)

def arch_of_delta(delta):
    # -(1/pi) int_0^inf cos(r delta) e^{-S^2 r^2} (S^2 2pi) L(r) dr
    integ = np.cos(np.outer(np.atleast_1d(delta), rgrid))*np.exp(-S*S*rgrid**2)*Lr
    return -(S*S*2*np.pi/np.pi)*np.trapezoid(integ, rgrid, axis=-1)

LAM = []
for n in range(2, 601):
    f = factorint(n)
    if len(f) == 1:
        ((p, k),) = f.items()
        LAM.append((np.log(n), np.log(p)/np.sqrt(n)))
LOGN = np.array([x for x, _ in LAM]); WN = np.array([w for _, w in LAM])

def primes_of_delta(delta):
    d = np.atleast_1d(delta)[:, None]
    rho = (S*S/np.sqrt(2*S*S))*SQ2PI*np.exp(-(d - LOGN[None, :])**2/(4*S*S))
    rho2 = (S*S/np.sqrt(2*S*S))*SQ2PI*np.exp(-(d + LOGN[None, :])**2/(4*S*S))
    return ((rho + rho2)*WN[None, :]).sum(axis=1)

def Kk(delta):
    return primes_of_delta(delta) + arch_of_delta(delta)

# ---------------- spot-check the engine against the certified mpmath probe ----------------
import mpmath as mp
mp.mp.dps = 25
def pair_local_mp(a1, a2):
    s1 = s2 = mp.mpf(S); S2m = s1*s1 + s2*s2
    rho_c = lambda v: s1*s2*mp.sqrt(2*mp.pi/S2m)*mp.e**(-(a1 - a2 - v)**2/(2*S2m))
    ps = mp.mpf(0)
    for ln, w in zip(LOGN, WN):
        ps += mp.mpf(float(w))*(rho_c(mp.mpf(float(ln))) + rho_c(-mp.mpf(float(ln))))
    Ls = lambda r: mp.re(mp.digamma(mp.mpf('0.25') + 1j*r/2)) - mp.log(mp.pi)
    mfun = lambda a, z: mp.mpf(S)*mp.sqrt(2*mp.pi)*mp.e**(z*a + mp.mpf(S)**2*z*z/2)
    arch = -(1/mp.pi)*mp.quad(lambda r: mp.re(mfun(mp.mpf(a1), 1j*r)*mfun(mp.mpf(a2), -1j*r))*Ls(r), [0, 4, 12, 40])
    return float(ps + arch)
chk = float(Kk(np.array([0.9 - 2.2]))[0]); ref = pair_local_mp(0.9, 2.2)
assert abs(chk - ref) < 5e-6, (chk, ref)
print(f"[engine] spot-check vs certified mpmath pairing: {chk:.8f} vs {ref:.8f}  OK")

# ---------------- classes ----------------
DICT = np.linspace(0.15, 3.6, 36)                  # effective dictionary (c >= 0)
PROBE = np.linspace(0.30, 3.40, 18)                # probe functionals phi_k
HAMP = np.linspace(0.4, 3.2, 8)                    # ample H = uniform positive combo (same width)
H_C = np.ones(len(HAMP))/len(HAMP)

def polevec(a):                                     # (ghat(0), ghat(1)) up to common constants
    return np.array([np.exp(-a/2), np.exp(a/2)])*S*SQ2PI*np.exp(S*S/8)

def make_primitive(centers):
    A = np.stack([polevec(a) for a in centers], axis=1)        # 2 x 4
    ns = np.linalg.svd(A)[2][2:]                                # null space (2-dim)
    d = ns[0]
    return d/np.abs(d).sum()

W1c = np.array([0.7, 1.25, 1.9, 2.6]); W1d = make_primitive(W1c)
W2c = np.array([0.5, 1.0, 2.3, 3.1]);  W2d = make_primitive(W2c)

def B_combo(cen1, co1, cen2, co2):
    deltas = cen1[:, None] - cen2[None, :]
    return float(co1 @ Kk(deltas.ravel()).reshape(deltas.shape) @ co2)

def thresholds(cen, d):
    Bww = B_combo(cen, d, cen, d)
    BwH = B_combo(cen, d, HAMP, H_C)
    BHH = B_combo(HAMP, H_C, HAMP, H_C)
    disc = BwH*BwH - Bww*BHH                       # Bww<0 expected => disc>0
    eps0 = (-BwH + np.sqrt(disc))/BHH
    return Bww, BwH, BHH, eps0

def feasible(cen, d, eps, K):
    probes = PROBE[np.linspace(0, len(PROBE)-1, K).astype(int)]
    M = np.empty((K, len(DICT))); t = np.empty(K)
    for k, pk in enumerate(probes):
        M[k] = Kk(DICT - pk)
        t[k] = float(d @ Kk(cen - pk)) + eps*float(H_C @ Kk(HAMP - pk))
        nrm = np.abs(M[k]).max()
        M[k] /= nrm; t[k] /= nrm
    eta = 1e-9
    A_ub = np.vstack([M, -M]); b_ub = np.concatenate([t + eta, -t + eta])
    res = linprog(np.ones(len(DICT)), A_ub=A_ub, b_ub=b_ub, bounds=(0, None), method='highs')
    return res.status == 0, (res.fun if res.status == 0 else np.inf)

def eps_star(cen, d, K, hi):
    lo_f, _ = feasible(cen, d, 0.0, K)
    if lo_f: return 0.0, 0.0
    lo, h = 0.0, hi
    f_hi, _ = feasible(cen, d, h, K)
    while not f_hi:
        h *= 2; f_hi, _ = feasible(cen, d, h, K)
        if h > 64*hi: return np.inf, np.inf
    for _ in range(40):
        mid = (lo + h)/2
        f, _ = feasible(cen, d, mid, K)
        if f: h = mid
        else: lo = mid
    _, l1 = feasible(cen, d, h, K)
    return h, l1

print(f"[setup] dict n={len(DICT)} (s={S}), probes up to K={len(PROBE)}, ample = {len(HAMP)}-bump positive combo")
for name, cen, d in (("w1", W1c, W1d), ("w2", W2c, W2d)):
    Bww, BwH, BHH, eps0 = thresholds(cen, d)
    print(f"\n[{name}] primitive: B(w,w)={Bww:+.6f} (spacelike: {'yes' if Bww<0 else 'NO'}), "
          f"B(w,H)={BwH:+.6f}, B(H,H)={BHH:+.6f}  =>  numerical threshold eps_0 = {eps0:.6f}")
    print(f"   {'K':>3} | {'eps*(K)':>10} | {'eps*/eps_0':>10} | {'|c|_1':>9} | saturation (needs eps* <= eps_0)")
    for K in (6, 10, 14, 18):
        es, l1 = eps_star(cen, d, K, 3*eps0)
        verdict = "consistent" if es <= eps0*1.0001 else "EXCEEDS — watch trend"
        print(f"   {K:>3} | {es:>10.6f} | {es/eps0:>10.4f} | {l1:>9.3f} | {verdict}")

print("\nREADOUT: eps*(K) rising toward eps_0 from below and stalling at/below it = saturation-consistent;")
print("a persistent crossing above eps_0 with K = the registered FALSIFIER of the Castelnuovo route.")
print("v0 calibration only: single width, n=36, K<=18; the production sweep (widths, directions,")
print("Dirichlet versions odd/even) is registered for the box.")
