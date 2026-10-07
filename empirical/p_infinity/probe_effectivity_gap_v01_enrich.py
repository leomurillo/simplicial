"""probe_effectivity_gap_v01_enrich.py — dictionary-enrichment test of the effectivity-gap instrument.
v0 found eps*/eps_0 ~ 12-15 with a poor dictionary (36 bumps, single width s=0.15).  Since the
dictionary INNER-approximates the effective cone {h >= 0}, eps* is biased UP by dictionary poverty.
Decisive v0 question: does eps* FALL toward eps_0 as the dictionary is enriched (multi-width, denser,
wider range)?  Saturation predicts eps*(dict) -> <= eps_0; a robust floor ABOVE eps_0 under
enrichment is the falsification signal (to be confirmed at production scale)."""
import numpy as np
from scipy.special import digamma
from scipy.optimize import linprog
from sympy import factorint

rgrid = np.linspace(0, 60, 6001)
Lr = np.real(digamma(0.25 + 0.5j*rgrid)) - np.log(np.pi)
LAM = []
for n in range(2, 601):
    f = factorint(n)
    if len(f) == 1:
        ((p, k),) = f.items()
        LAM.append((np.log(n), np.log(p)/np.sqrt(n)))
LOGN = np.array([x for x, _ in LAM]); WN = np.array([w for _, w in LAM])
SQ2PI = np.sqrt(2*np.pi)

def pairing(a1, s1, a2, s2):
    """B(G_{a1,s1}, G_{a2,s2}) = primes + arch (vectorized over a1 array)."""
    a1 = np.atleast_1d(a1); s1v = np.full_like(a1, s1) if np.isscalar(s1) else s1
    d = a1 - a2; S2 = s1v**2 + s2**2
    # primes
    pref = s1v*s2*SQ2PI/np.sqrt(S2)
    ps = (pref[:, None]*(np.exp(-(d[:, None] - LOGN[None, :])**2/(2*S2[:, None]))
                         + np.exp(-(d[:, None] + LOGN[None, :])**2/(2*S2[:, None])))*WN[None, :]).sum(1)
    # arch
    integ = np.cos(d[:, None]*rgrid[None, :])*np.exp(-S2[:, None]*rgrid[None, :]**2/2)*Lr[None, :]
    arch = -(s1v*s2*2*np.pi/np.pi)*np.trapezoid(integ, rgrid, axis=1)
    return ps + arch

def B_sets(cen1, ss1, co1, cen2, ss2, co2):
    tot = 0.0
    for a2, s2, c2 in zip(cen2, ss2, co2):
        tot += c2*float(co1 @ pairing(cen1, ss1, a2, s2))
    return tot

# primitive w2 and ample H exactly as v0 (s=0.15 family)
S0 = 0.15
def polevec(a): return np.array([np.exp(-a/2), np.exp(a/2)])*S0*SQ2PI*np.exp(S0*S0/8)
W2c = np.array([0.5, 1.0, 2.3, 3.1])
A = np.stack([polevec(a) for a in W2c], axis=1)
W2d = np.linalg.svd(A)[2][2]; W2d = W2d/np.abs(W2d).sum()
W2s = np.full(4, S0)
HAMP = np.linspace(0.4, 3.2, 8); H_C = np.ones(8)/8; H_S = np.full(8, S0)

Bww = B_sets(W2c, W2s, W2d, W2c, W2s, W2d)
BwH = B_sets(W2c, W2s, W2d, HAMP, H_S, H_C)
BHH = B_sets(HAMP, H_S, H_C, HAMP, H_S, H_C)
eps0 = (-BwH + np.sqrt(BwH*BwH - Bww*BHH))/BHH
print(f"[w2] B(w,w)={Bww:+.6f}  eps_0={eps0:.6f}")

PROBE_C = np.linspace(0.30, 3.40, 14); PROBE_S = np.full(14, S0)

def eps_star(dcen, dss, hi):
    M = np.empty((14, len(dcen))); tw = np.empty(14); tH = np.empty(14)
    for k in range(14):
        M[k] = pairing(dcen, dss, PROBE_C[k], PROBE_S[k])
        tw[k] = float(W2d @ pairing(W2c, W2s, PROBE_C[k], PROBE_S[k]))
        tH[k] = float(H_C @ pairing(HAMP, H_S, PROBE_C[k], PROBE_S[k]))
        nrm = np.abs(M[k]).max(); M[k] /= nrm; tw[k] /= nrm; tH[k] /= nrm
    def feas(eps):
        t = tw + eps*tH; eta = 1e-9
        r = linprog(np.ones(M.shape[1]), A_ub=np.vstack([M, -M]),
                    b_ub=np.concatenate([t + eta, -t + eta]), bounds=(0, None), method='highs')
        return r.status == 0
    if feas(0.0): return 0.0
    lo, h = 0.0, hi
    while not feas(h):
        h *= 2
        if h > 1e3: return np.inf
    for _ in range(40):
        mid = (lo + h)/2
        if feas(mid): h = mid
        else: lo = mid
    return h

DICTS = {
    "v0      (n= 36, s=0.15, x<=3.6)": (np.linspace(0.15, 3.6, 36), np.full(36, 0.15)),
    "dense   (n= 70, s=0.15, x<=3.6)": (np.linspace(0.15, 3.6, 70), np.full(70, 0.15)),
    "widths  (n=122, s in 0.10-0.40)": (np.concatenate([np.linspace(0.12, 3.6, 46), np.linspace(0.15, 3.6, 36),
                                                        np.linspace(0.2, 3.6, 24), np.linspace(0.3, 3.4, 16)]),
                                        np.concatenate([np.full(46, 0.10), np.full(36, 0.15),
                                                        np.full(24, 0.25), np.full(16, 0.40)])),
    "range   (n=160, + x in 3.6-6.5, + narrow s=0.07)": (
        np.concatenate([np.linspace(0.12, 3.6, 46), np.linspace(0.15, 3.6, 36), np.linspace(0.2, 3.6, 24),
                        np.linspace(0.3, 3.4, 16), np.linspace(3.7, 6.5, 18), np.linspace(0.1, 3.6, 20)]),
        np.concatenate([np.full(46, 0.10), np.full(36, 0.15), np.full(24, 0.25),
                        np.full(16, 0.40), np.full(18, 0.25), np.full(20, 0.07)])),
}
print(f"{'dictionary':<50} {'eps*':>10} {'eps*/eps_0':>11}")
for name, (dc, ds) in DICTS.items():
    es = eps_star(dc, ds, 3*eps0)
    print(f"{name:<50} {es:>10.6f} {es/eps0:>11.4f}")
print("\nsaturation predicts eps*/eps_0 -> <= 1 under enrichment; a robust floor > 1 = falsifier signal.")
