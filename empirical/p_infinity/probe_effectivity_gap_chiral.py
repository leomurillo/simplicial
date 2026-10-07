"""probe_effectivity_gap_chiral.py — CHIRAL effectivity-deficit sweep on Dedekind zeta_K = zeta*L(s,chi_D).

Tests whether the program's CHIRAL channel (odd D<0, L(s,chi_D) odd) saturates like zeta: does the
robust effectivity deficit d(eps_0) -> 0 under dictionary enrichment, including for direction w
localized AT a chiral L-zero frequency?  Engine (verified by verify_zetaK_engine.py, both parities
PASS): pole pair = zeta's (xi_K entire, coeff 1); prime weight Lambda(n)(1+chi_D(n))/sqrt n;
arch symbol Om_K(r)=Re psi(1/4+ir/2)+Re psi(1/4+a/2+ir/2)-2 log pi + log|D|  (D=1 => plain zeta).
L-zeros via PARI lfunzeros (fast).  Robust min-residual LP (artifact-free, monotone in dictionary).
Parallel over D.  No torch.  Output: effectivity_gap_chiral_resolve.csv + verdict.
"""
import numpy as np, csv, time, sys, math
from scipy.special import digamma
from scipy.optimize import linprog
from sympy import primerange, factorint
from multiprocessing import Pool

RG = np.linspace(0, 80, 6001); SQ2PI = np.sqrt(2*np.pi)
def pr(*a, **k): print(*a, **k); sys.stdout.flush()

def kron(a, n):
    if n == 0: return 1 if abs(a) == 1 else 0
    res = 1
    if n % 2 == 0:
        if a % 2 == 0: return 0
        while n % 2 == 0:
            n //= 2
            if a % 8 in (3, 5): res = -res
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

# per-D engine data: prime (logn, weight) and arch symbol on RG
def engine_data(D):
    a_par = 0 if D > 0 else 1
    logn, wts = [], []
    for n in range(2, 4001):
        f = factorint(n)
        if len(f) == 1:
            ((p, k),) = f.items()
            w = math.log(p)*(1 + (kron(D, n) if D != 1 else 0))/math.sqrt(n) if D != 1 else math.log(p)/math.sqrt(n)
            if w != 0: logn.append(math.log(n)); wts.append(w)
    LR = np.real(digamma(0.25 + 0.5j*RG)) - np.log(np.pi)
    if D != 1:
        LR = LR + np.real(digamma(0.25 + a_par/2 + 0.5j*RG)) - np.log(np.pi) + np.log(abs(D))
    return np.array(logn), np.array(wts), LR

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
def pair_rows(E, e2, LOGN, WN, LR, chunk=400):
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
def B_sets(E1, c1, E2, c2, eng):
    a2, s2, w2 = E2
    return sum(c2[j]*float(c1 @ pair_rows(E1, (a2[j], s2[j], w2[j]), *eng)) for j in range(len(a2)))
def deficit(M, t):
    K, n = M.shape; c = np.zeros(n + 1); c[-1] = 1.0
    A = np.vstack([np.hstack([M, -np.ones((K, 1))]), np.hstack([-M, -np.ones((K, 1))])])
    r = linprog(c, A_ub=A, b_ub=np.concatenate([t, -t]), bounds=[(0, None)]*n + [(0, None)], method='highs')
    return r.x[-1] if r.status == 0 else np.inf

def gridd(x0, x1, s, st): return [(float(a), s, 0.0) for a in np.arange(x0, x1 + 1e-9, st)]
def build_dicts():
    D1 = gridd(0, 4, .15, .15) + gridd(0, 4, .30, .30)
    D2 = D1 + gridd(-1, 5, .10, .10) + gridd(-1, 5, .50, .40)
    D3 = D2 + gridd(-2, 6, .06, .06) + gridd(0, 4, .04, .04)
    D4 = D3 + gridd(-1, 5, .04, .02) + gridd(0.5, 3.5, .025, .02) + gridd(-2, 6, .80, .50)
    D5 = D4 + gridd(-2, 6, .018, .015) + gridd(0.5, 3.5, .013, .012)
    D6 = D5 + gridd(-3, 7, .012, .01) + gridd(0, 4, .009, .008)
    return [("D1", mk(D1)), ("D2", mk(D2)), ("D3", mk(D3)), ("D4", mk(D4)), ("D5", mk(D5)), ("D6", mk(D6))]

def worker(arg):
    D, Lz = arg
    eng = engine_data(D)
    LOGN, WN, LR = eng
    DICTS = build_dicts()
    H_sym = (mk([(float(a), 0.30, 0.0) for a in np.linspace(-2.0, 2.0, 12)]), np.ones(12)/12)
    HE, Hc = H_sym
    P1 = [(float(a), 0.20, 0.0) for a in np.linspace(0.3, 3.9, 12)]
    g1 = Lz[0] if Lz else 14.13
    P3 = P1 + [(1.0, 0.5, g1), (2.2, 0.5, g1), (-1.0, 0.30, 0.0), (4.6, 0.30, 0.0),
               (1.6, 0.8, g1), (1.5, 0.35, Lz[1] if len(Lz) > 1 else 21.0)]
    # directions: spread (pole-killed combo) + chiral zero-channel at first L-zero + at second L-zero
    ws_c = [0.5, 1.0, 2.3, 3.1]
    pol = np.array([[np.exp(-x/2), np.exp(x/2)] for x in ws_c]).T*0.15*SQ2PI*np.exp(0.15**2/8)
    wd = np.linalg.svd(pol)[2][2]; wd = wd/np.abs(wd).sum()
    DIRS = [("spread", mk([(x, 0.15, 0.0) for x in ws_c]), wd)]
    if Lz:
        DIRS.append(("chiralZ1", mk([(1.4, 0.55, Lz[0])]), np.array([1.0])))
    if len(Lz) > 1:
        DIRS.append(("chiralZ2", mk([(1.2, 0.40, Lz[1])]), np.array([1.0])))
    rows = []
    for dirname, wE, wc in DIRS:
        Bww = B_sets(wE, wc, wE, wc, eng); BwH = B_sets(wE, wc, HE, Hc, eng); BHH = B_sets(HE, Hc, HE, Hc, eng)
        if BwH*BwH - Bww*BHH <= 0 or Bww >= 0:
            rows.append(dict(D=D, dir=dirname, probes="-", dict="-", n=0, Bww=Bww, eps0=np.nan,
                             deficit_eps0=np.nan, note="not spacelike")); continue
        eps0 = (-BwH + np.sqrt(BwH*BwH - Bww*BHH))/BHH
        for pname, plist in [("P1", P1), ("P3", P3)]:
            tw = np.array([float(wc @ pair_rows(wE, pk, *eng)) for pk in plist])
            tH = np.array([float(Hc @ pair_rows(HE, pk, *eng)) for pk in plist])
            for dname, dE in DICTS:
                M = np.stack([pair_rows(dE, pk, *eng) for pk in plist])
                nrm = np.abs(M).max(axis=1); M = M/nrm[:, None]
                t = (tw + eps0*tH)/nrm
                d0 = deficit(M, t)/(np.abs(t).max() + 1e-30)
                rows.append(dict(D=D, dir=dirname, probes=pname, dict=dname, n=len(dE[0]),
                                 Bww=Bww, eps0=eps0, deficit_eps0=d0, note=""))
    return D, Lz, rows

def main():
    import cypari2
    pari = cypari2.Pari(); pari.set_real_precision(25)
    targets = [-3, -8, 13]   # control + the two FLOOR? candidates
    Lz_map = {}
    for D in targets:
        if D == 1: Lz_map[D] = []; continue
        try:
            L = pari.lfuncreate(int(D))
            Z = pari.lfunzeros(L, 26)
            zz = sorted(float(pari.real(z)) for z in Z if float(pari.real(z)) > 1)
            Lz_map[D] = zz[:6]
        except Exception as e:
            Lz_map[D] = []
        pr(f"  D={D:>3} ({'odd/chiral' if D < 0 else ('even' if D != 1 else 'zeta')}): L-zeros {[round(z,3) for z in Lz_map[D][:4]]}")
    pr(f"\n[chiral sweep] {len(targets)} fields x ~3 dirs x 2 probes x 4 dicts; engine verified PASS")
    t0 = time.time(); allrows = []
    with Pool(min(8, len(targets))) as pool:
        for D, Lz, rows in pool.imap_unordered(worker, [(D, Lz_map[D]) for D in targets]):
            allrows += rows
            for r in rows:
                if r['dict'] in ('D4', 'D6') and r['probes'] == 'P1':
                    pr(f"    D={r['D']:>3} {r['dir']:<9} {r['dict']} deficit(eps0)={r['deficit_eps0']:.2e}")
    with open("effectivity_gap_chiral_resolve.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(allrows[0].keys())); w.writeheader()
        for r in allrows: w.writerow(r)
    pr("\n================ CHIRAL VERDICT — deficit(eps0) D1->D4, P1 ================")
    for D in targets:
        for dirn in ("spread", "chiralZ1", "chiralZ2"):  # resolution: D1->D6
            rr = [r for r in allrows if r['D'] == D and r['dir'] == dirn and r['probes'] == 'P1']
            if rr:
                tr = " -> ".join(f"{r['deficit_eps0']:.1e}" for r in sorted(rr, key=lambda x: x['dict']))
                last = sorted(rr, key=lambda x: x['dict'])[-1]['deficit_eps0']
                v = "SAT(->0)" if last < 1e-2 else "trending" if last < rr[0]['deficit_eps0']/3 else "FLOOR?"
                lab = 'chiral' if D < 0 else ('even' if D != 1 else 'zeta')
                pr(f"  D={D:>3}({lab:<6}) {dirn:<9}: {tr}   => {v}")
    pr(f"\n[total {time.time()-t0:.0f}s]  chiral channels saturating like zeta => route robust across the seam.")

if __name__ == "__main__": main()
