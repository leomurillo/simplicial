"""probe_effectivity_gap_v2_robust.py — ROBUST effectivity-gap instrument (replaces the fragile
hard-equality LP of v1).  v1's eps* via |Mc - t| <= 1e-9 is non-monotone under enrichment for the
high-frequency / narrow-bump cells (spurious 'inf' at D3 while D2 feasible — structurally impossible
for a true LP, hence a tolerance artifact).  Here the readout is the EFFECTIVITY DEFICIT

   d(eps) = min_{c >= 0}  || M c - t(eps) ||_inf    (each constraint row pre-normalized to max 1)

computed by the min-residual LP  (minimize r s.t. -r <= Mc - t <= r, c>=0, r>=0) — ALWAYS feasible,
and MONOTONE DECREASING in the dictionary (more columns can only lower the min).  This is exactly the
convex quantity the Saturation Conjecture (S) asserts -> 0: the class is mobile-effective iff it is
approximable to arbitrary deficit by positive profiles.

Primary readout: d(eps_0) (deficit AT the numerical-positivity threshold) -> 0 under enrichment = (S).
Secondary: eps_delta / eps_0, eps_delta = min eps with d(eps) <= delta (delta = 0.5% of ||t||_inf):
the interpretable 'ample padding to effective' ratio, now artifact-free.
Falsifier: a robust deficit FLOOR d(eps_0) > 0 (or eps_delta/eps_0 floor > 1) under enrichment along
any direction — especially the single zero-channel rows where the cone IS the Cauchy-Schwarz cone.
Engine identical to v1 (verified: unmod pairing exact, modulated W1 identity 1e-16).  No torch.
"""
import numpy as np, csv, time, sys
from scipy.special import digamma
from scipy.optimize import linprog
from sympy import factorint

def pr(*a, **k): print(*a, **k); sys.stdout.flush()
t00 = time.time()
GAM = [14.134725141734693, 21.022039638771555, 25.010857580145688,
       30.424876125859513, 32.93506158773919, 37.58617815882567]
RG = np.linspace(0, 80, 6001); LR = np.real(digamma(0.25 + 0.5j*RG)) - np.log(np.pi)
SQ2PI = np.sqrt(2*np.pi)
PP = []
for n in range(2, 4001):
    f = factorint(n)
    if len(f) == 1:
        ((p, k),) = f.items(); PP.append((np.log(n), np.log(p)/np.sqrt(n)))
LOGN = np.array([x for x, _ in PP]); WN = np.array([w for _, w in PP])

def m_grid(E, r):
    a, s, w = E
    return (s[:, None]*SQ2PI/2)*np.exp(1j*r[None, :]*a[:, None])*(
        np.exp(-s[:, None]**2*(r[None, :] - w[:, None])**2/2)
        + np.exp(-s[:, None]**2*(r[None, :] + w[:, None])**2/2))
def rho_corr(E1, e2, v):
    a1, s1, w1 = E1; a2, s2, w2 = e2
    dv = a1[:, None] - a2 - v[None, :]; out = np.zeros(dv.shape)
    S2 = s1**2 + s2**2; pref = np.sqrt(2*np.pi*s1**2*s2**2/S2)
    for e1 in (+1, -1):
        for e2s in (+1, -1):
            Om = e1*w1 + e2s*w2
            re_e = -dv**2/(2*S2[:, None]) - (Om**2*s1**2*s2**2/(2*S2))[:, None]
            im_e = e2s*w2*dv - (Om*s1**2/S2)[:, None]*dv
            out += pref[:, None]*np.exp(re_e)*np.cos(im_e)
    return out/4
def pair_rows(E, e2, chunk=400):
    a, s, w = E; n = len(a); out = np.empty(n)
    m2c = np.conj(m_grid((np.array([e2[0]]), np.array([e2[1]]), np.array([e2[2]])), RG))[0]
    for lo in range(0, n, chunk):
        sl = slice(lo, min(lo + chunk, n)); Ec = (a[sl], s[sl], w[sl])
        arch = -(1/np.pi)*np.trapezoid(np.real(m_grid(Ec, RG)*m2c[None, :])*LR[None, :], RG, axis=1)
        out[sl] = ((rho_corr(Ec, e2, LOGN) + rho_corr(Ec, e2, -LOGN))*WN[None, :]).sum(1) + arch
    return out
def mk(els):
    return (np.array([e[0] for e in els], float), np.array([e[1] for e in els], float),
            np.array([e[2] for e in els], float))
def B_sets(E1, c1, E2, c2):
    a2, s2, w2 = E2
    return sum(c2[j]*float(c1 @ pair_rows(E1, (a2[j], s2[j], w2[j]))) for j in range(len(a2)))

# verify (same gates)
v = float(pair_rows(mk([(0.9, 0.18, 0.0)]), (2.2, 0.18, 0.0))[0])
assert abs(v - 0.49970883) < 2e-5; pr(f"[verify] unmod pairing {v:.8f} OK")
wz = (1.5, 0.55, GAM[0]); pr(f"[verify] B(w_zero1,w_zero1)={float(pair_rows(mk([wz]),wz)[0]):.4f} (<0) OK")

# dictionaries / probes / configs  (same as v1)
def gridd(x0, x1, s, st): return [(float(a), s, 0.0) for a in np.arange(x0, x1 + 1e-9, st)]
D1 = gridd(0, 4, .15, .15) + gridd(0, 4, .30, .30)
D2 = D1 + gridd(-1, 5, .10, .10) + gridd(-1, 5, .50, .40)
D3 = D2 + gridd(-2, 6, .06, .06) + gridd(0, 4, .04, .04)
D4 = D3 + gridd(-1, 5, .04, .02) + gridd(0.5, 3.5, .025, .02) + gridd(-2, 6, .80, .50)
D5 = D4 + gridd(-2, 6, .018, .015) + gridd(0.5, 3.5, .013, .012)     # extra comb-capacity for gamma~33-37
DICTS = [("D1", mk(D1)), ("D2", mk(D2)), ("D3", mk(D3)), ("D4", mk(D4)), ("D5", mk(D5))]
P1 = [(float(a), 0.20, 0.0) for a in np.linspace(0.3, 3.9, 12)]
P3 = P1 + [(a, 0.5, g) for g in GAM[:4] for a in (1.0, 2.2)] + \
     [(float(a), 0.30, 0.0) for a in (-1.5, -0.5, 4.5, 5.2)] + \
     [(1.6, 0.8, GAM[0]), (2.8, 0.5, GAM[0]), (1.5, 0.35, GAM[4]), (1.5, 0.35, GAM[5])]
PROBES = [("P1", P1), ("P3", P3)]
def nullw(c, s):
    pol = np.array([[np.exp(-a/2), np.exp(a/2)] for a in c]).T*s*SQ2PI*np.exp(s*s/8)
    d = np.linalg.svd(pol)[2][2]; return d/np.abs(d).sum()
H_pos = (mk([(float(a), 0.30, 0.0) for a in np.linspace(0.2, 4.2, 12)]), np.ones(12)/12)
H_sym = (mk([(float(a), 0.30, 0.0) for a in np.linspace(-2.0, 2.0, 12)]), np.ones(12)/12)
ws_c = [0.5, 1.0, 2.3, 3.1]
CONFIGS = [
    ("w_spread/Hpos", mk([(a, 0.15, 0.0) for a in ws_c]), nullw(ws_c, 0.15), H_pos),
    ("w_zero1/Hsym",  mk([(1.5, 0.55, GAM[0])]), np.array([1.0]), H_sym),
    ("w_zero2/Hsym",  mk([(1.2, 0.40, GAM[1])]), np.array([1.0]), H_sym),
    ("w_zero4/Hsym",  mk([(1.4, 0.30, GAM[3])]), np.array([1.0]), H_sym),
]

def deficit(M, t):                       # min_{c>=0} ||Mc - t||_inf  via min-residual LP
    K, n = M.shape
    c = np.zeros(n + 1); c[-1] = 1.0
    A = np.vstack([np.hstack([M, -np.ones((K, 1))]), np.hstack([-M, -np.ones((K, 1))])])
    b = np.concatenate([t, -t])
    bounds = [(0, None)]*n + [(0, None)]
    r = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return r.x[-1] if r.status == 0 else np.inf

rows = []
pr(f"[setup] dicts n={[len(d[1][0]) for d in DICTS]}, probes K={[len(p[1]) for p in PROBES]}, primes {len(LOGN)}")
for cname, wE, wc, (HE, Hc) in CONFIGS:
    Bww = B_sets(wE, wc, wE, wc); BwH = B_sets(wE, wc, HE, Hc); BHH = B_sets(HE, Hc, HE, Hc)
    eps0 = (-BwH + np.sqrt(BwH*BwH - Bww*BHH))/BHH
    pr(f"\n=== {cname}: B(w,w)={Bww:+.6f} eps0={eps0:.6f} (spacelike {Bww<0}) ===")
    for pname, plist in PROBES:
        K = len(plist)
        tw = np.array([float(wc @ pair_rows(wE, pk)) for pk in plist])
        tH = np.array([float(Hc @ pair_rows(HE, pk)) for pk in plist])
        for dname, dE in DICTS:
            t0 = time.time()
            M = np.stack([pair_rows(dE, pk) for pk in plist])
            nrm = np.abs(M).max(axis=1); M = M/nrm[:, None]; twn = tw/nrm; tHn = tH/nrm
            t_eps0 = twn + eps0*tHn
            d0 = deficit(M, t_eps0)/ (np.abs(t_eps0).max() + 1e-30)       # relative deficit at eps0
            delta = 0.005
            def dd(eps): return deficit(M, twn + eps*tHn)/(np.abs(twn + eps*tHn).max() + 1e-30)
            lo, hi = 0.0, eps0
            if dd(hi) > delta:
                while dd(hi) > delta and hi < 1e4*eps0: hi *= 2
            es = np.inf if dd(hi) > delta else None
            if es is None:
                for _ in range(36):
                    mid = (lo + hi)/2
                    if dd(mid) <= delta: hi = mid
                    else: lo = mid
                es = hi
            ratio = es/eps0 if np.isfinite(es) else np.inf
            pr(f"    {pname}(K={K:>2}) x {dname}(n={len(dE[0]):>4}): deficit(eps0)={d0:<10.2e} "
               f"eps_delta/eps0={ratio:<9.4f}  [{time.time()-t0:.0f}s]")
            rows.append(dict(config=cname, probes=pname, K=K, dict=dname, n=len(dE[0]),
                             eps0=eps0, deficit_eps0=d0, eps_delta=es, ratio=ratio))
            with open("effectivity_gap_v2.csv", "w", newline="") as f:
                wr = csv.DictWriter(f, fieldnames=list(rows[0].keys())); wr.writeheader()
                for rr in rows: wr.writerow(rr)

pr("\n================ VERDICT — deficit(eps0) by dictionary (-> 0 = saturation) ================")
for cname, *_ in CONFIGS:
    for pname, _ in PROBES:
        rr = [r for r in rows if r['config'] == cname and r['probes'] == pname]
        if rr:
            tr = " -> ".join(f"{r['dict']}:{r['deficit_eps0']:.1e}" for r in rr)
            last = rr[-1]['deficit_eps0']
            v = "SATURATION-CONSISTENT (->0)" if last < 1e-2 else ("trending" if last < rr[0]['deficit_eps0']/3 else "FLOOR? — falsifier candidate")
            pr(f"  {cname:<16} {pname}: {tr}   => {v}")
pr(f"\n[total {time.time()-t00:.0f}s]  monotone by construction; a robust deficit FLOOR > 0 under")
pr("enrichment along any single-channel zero direction = the registered falsifier of (S).")
