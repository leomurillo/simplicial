"""probe_effectivity_gap_v1_production.py — PRODUCTION enrichment sweep of the effectivity gap.

Upgrades over v0/v0.1:
  * generalized elements G(x;a,s)cos(w(x-a)) — ZERO-FREQUENCY probes (w = gamma_j) make the finite
    test read the class at the zeros: the channels where (S) carries RH content;
  * comb-capable dictionaries (bumps down to s=0.025 on steps 0.02): CS-extremality (= Dirac combs
    on the gamma-lattice) becomes approximable — the sharp prediction is eps*/eps_0 -> ~1 exactly
    when the dictionary becomes comb-capable at the target's frequency;
  * five direction/ample configurations including zero-localized w with SYMMETRIC ample H
    (the marginal regime: for single-channel classes the light cone IS the Cauchy-Schwarz cone
    |h^(1/2+i g)|^2 <= h^(0) h^(1), equality = gamma-combs);
  * mass tracking ||c||_1 at eps* (the boundedness clause of (S)).

READOUT per (direction, probe set K, dictionary n): eps*(K, dict)/eps_0.  Saturation predicts the
dictionary-enrichment limit <= 1 for every K.  Registered falsifier: a robust floor > 1 under
enrichment.  No torch.  Deterministic.  Output: effectivity_gap_v1.csv + verdict table.
"""
import numpy as np, csv, time, sys
from scipy.special import digamma
from scipy.optimize import linprog
from sympy import factorint

t00 = time.time()
GAM = [14.134725141734693, 21.022039638771555, 25.010857580145688,
       30.424876125859513, 32.93506158773919, 37.58617815882567]

# ---------------- engine: elements (a, s, w);  profile = G(x;a,s) cos(w(x-a)) ----------------
# grids verified sufficient: modulated W1 identity holds to 1e-16, unmod pairing exact to 1e-15
RG = np.linspace(0, 80, 6001)
LR = np.real(digamma(0.25 + 0.5j*RG)) - np.log(np.pi)
SQ2PI = np.sqrt(2*np.pi)
def pr(*a, **k):                      # unbuffered print
    print(*a, **k); sys.stdout.flush()

PP = []
for n in range(2, 4001):
    f = factorint(n)
    if len(f) == 1:
        ((p, k),) = f.items()
        PP.append((np.log(n), np.log(p)/np.sqrt(n)))
LOGN = np.array([x for x, _ in PP]); WN = np.array([w for _, w in PP])

def m_grid(E, r):
    """m(ir) on grid r for element array E=(a,s,w): complex (n, len(r))."""
    a, s, w = E
    return (s[:, None]*SQ2PI/2)*np.exp(1j*r[None, :]*a[:, None])*(
        np.exp(-s[:, None]**2*(r[None, :] - w[:, None])**2/2)
        + np.exp(-s[:, None]**2*(r[None, :] + w[:, None])**2/2))

def rho_corr(E1, e2, v):
    """correlation int p1(x) p2(x - v) dx for element array E1 vs single element e2, at v-array.
    p_j = (1/2)[E+ + E-];  4 complex-Gaussian terms."""
    a1, s1, w1 = E1; a2, s2, w2 = e2
    dv = a1[:, None] - a2 - v[None, :]                       # (n, nv)
    out = np.zeros(dv.shape)
    S2 = (s1**2 + s2**2)                                      # (n,)
    pref = np.sqrt(2*np.pi*s1**2*s2**2/S2)                    # (n,)
    for e1 in (+1, -1):
        for e2s in (+1, -1):
            Om = e1*w1 + e2s*w2                               # (n,)
            # exponents combined analytically (no overflow): the product is a decaying Gaussian
            re_exp = -dv**2/(2*S2[:, None]) - (Om**2*s1**2*s2**2/(2*S2))[:, None]
            im_exp = e2s*w2*dv - (Om*s1**2/S2)[:, None]*dv
            out += pref[:, None]*np.exp(re_exp)*np.cos(im_exp)
    return out/4

def pair_rows(E, e2, chunk=250):
    """pairing B(E_i, e2) for all i: primes + arch (vectorized, chunked)."""
    a, s, w = E; n = len(a)
    out = np.empty(n)
    m2c = np.conj(m_grid((np.array([e2[0]]), np.array([e2[1]]), np.array([e2[2]])), RG))[0]
    for lo in range(0, n, chunk):
        sl = slice(lo, min(lo + chunk, n))
        Ec = (a[sl], s[sl], w[sl])
        arch = -(1/np.pi)*np.trapezoid(np.real(m_grid(Ec, RG)*m2c[None, :])*LR[None, :], RG, axis=1)
        rr = rho_corr(Ec, e2, LOGN) + rho_corr(Ec, e2, -LOGN)
        out[sl] = (rr*WN[None, :]).sum(1) + arch
    return out

def B_sets(E1, c1, E2, c2):
    tot = 0.0
    a2, s2, w2 = E2
    for j in range(len(a2)):
        tot += c2[j]*float(c1 @ pair_rows(E1, (a2[j], s2[j], w2[j])))
    return tot

def mk(els):
    a = np.array([e[0] for e in els], float); s = np.array([e[1] for e in els], float)
    w = np.array([e[2] for e in els], float)
    return (a, s, w)

# ---------------- verification against the certified mpmath engine ----------------
import mpmath as mp
mp.mp.dps = 25
def mp_pair_unmod(a1, s1, a2, s2):
    S2m = mp.mpf(s1)**2 + mp.mpf(s2)**2
    rho = lambda v: mp.mpf(s1)*mp.mpf(s2)*mp.sqrt(2*mp.pi/S2m)*mp.e**(-(a1 - a2 - v)**2/(2*S2m))
    ps = mp.fsum(mp.mpf(float(wn))*(rho(mp.mpf(float(ln))) + rho(-mp.mpf(float(ln))))
                 for ln, wn in zip(LOGN[:300], WN[:300]))
    mf = lambda a, s, z: mp.mpf(s)*mp.sqrt(2*mp.pi)*mp.e**(z*a + mp.mpf(s)**2*z*z/2)
    Ls = lambda r: mp.re(mp.digamma(mp.mpf('0.25') + 1j*r/2)) - mp.log(mp.pi)
    arch = -(1/mp.pi)*mp.quad(lambda r: mp.re(mf(a1, s1, 1j*r)*mf(a2, s2, -1j*r))*Ls(r), [0, 4, 12, 40])
    return float(ps + arch)
v_np = float(pair_rows(mk([(0.9, 0.18, 0.0)]), (2.2, 0.18, 0.0))[0])
v_mp = mp_pair_unmod(0.9, 0.18, 2.2, 0.18)
assert abs(v_np - v_mp) < 2e-5, (v_np, v_mp)
pr(f"[verify 1] unmodulated pairing: engine {v_np:.8f} vs certified mpmath {v_mp:.8f}  OK")

# modulated self-pairing vs zeros side (80 zeros)
wz = (1.5, 0.55, GAM[0])
B_loc = float(pair_rows(mk([wz]), wz)[0])
zers = [mp.im(mp.zetazero(k)) for k in range(1, 61)]
def m_mp(a, s, w, z):
    return mp.e**(z*a)*(mp.mpf(s)*mp.sqrt(2*mp.pi)/2)*(mp.e**(mp.mpf(s)**2*(z + 1j*w)**2/2)
                                                       + mp.e**(mp.mpf(s)**2*(z - 1j*w)**2/2))
poles = 2*mp.re(m_mp(*wz, mp.mpf(-1)/2)*m_mp(*wz, mp.mpf(1)/2))
zs = mp.fsum(2*mp.re(m_mp(*wz, 1j*g)*m_mp(*wz, -1j*g)) for g in zers)
B_zer = float(poles - zs)
assert abs(B_loc - B_zer) < 5e-4*abs(B_zer), (B_loc, B_zer)
pr(f"[verify 2] modulated self-pairing: local {B_loc:.6f} vs zeros-side {B_zer:.6f}  OK"
      f"  (B(w_zero1,w_zero1) < 0: {'yes' if B_loc < 0 else 'NO'})")

# ---------------- configurations ----------------
def gridd(x0, x1, s, st): return [(float(a), s, 0.0) for a in np.arange(x0, x1 + 1e-9, st)]
D1 = gridd(0, 4, .15, .15) + gridd(0, 4, .30, .30)
D2 = D1 + gridd(-1, 5, .10, .10) + gridd(-1, 5, .50, .40)
D3 = D2 + gridd(-2, 6, .06, .06) + gridd(0, 4, .04, .04)
D4 = D3 + gridd(-1, 5, .04, .02) + gridd(0.5, 3.5, .025, .02) + gridd(-2, 6, .80, .50)
DICTS = [("D1", mk(D1)), ("D2", mk(D2)), ("D3", mk(D3)), ("D4", mk(D4))]

P1 = [(float(a), 0.20, 0.0) for a in np.linspace(0.3, 3.9, 12)]
P2 = P1 + [(a, 0.5, g) for g in GAM[:4] for a in (1.0, 2.2)]
P3 = P2 + [(float(a), 0.30, 0.0) for a in (-1.5, -1.0, -0.5, 0.0, 4.5, 5.2)] + \
     [(1.6, 0.8, GAM[0]), (1.6, 0.8, GAM[1]), (2.8, 0.5, GAM[0]), (0.6, 0.5, GAM[0]),
      (1.5, 0.35, GAM[4]), (1.5, 0.35, GAM[5])]
PROBES = [("P1", P1), ("P2", P2), ("P3", P3)]

def nullw(centers, s):
    pol = np.array([[np.exp(-a/2), np.exp(a/2)] for a in centers]).T*s*SQ2PI*np.exp(s*s/8)
    d = np.linalg.svd(pol)[2][2]
    return d/np.abs(d).sum()

H_pos = (mk([(float(a), 0.30, 0.0) for a in np.linspace(0.2, 4.2, 12)]), np.ones(12)/12)
H_sym = (mk([(float(a), 0.30, 0.0) for a in np.linspace(-2.0, 2.0, 12)]), np.ones(12)/12)
ws_c = [0.5, 1.0, 2.3, 3.1]; wl_c = [0.3, 0.6, 0.9, 1.2]
CONFIGS = [
    ("w_spread/Hpos", mk([(a, 0.15, 0.0) for a in ws_c]), nullw(ws_c, 0.15), H_pos),
    ("w_lowx/Hpos",   mk([(a, 0.12, 0.0) for a in wl_c]), nullw(wl_c, 0.12), H_pos),
    ("w_zero1/Hpos",  mk([(1.5, 0.55, GAM[0])]), np.array([1.0]), H_pos),
    ("w_zero1/Hsym",  mk([(1.5, 0.55, GAM[0])]), np.array([1.0]), H_sym),
    ("w_zero2/Hsym",  mk([(1.2, 0.40, GAM[1])]), np.array([1.0]), H_sym),
]

rows_out = []
print(f"\n[setup] dicts n = {[len(d[1][0]) for d in DICTS]};  probes K = {[len(p[1]) for p in PROBES]};"
      f"  prime powers {len(LOGN)};  r-grid {len(RG)}")
for cname, wE, wc, (HE, Hc) in CONFIGS:
    Bww = B_sets(wE, wc, wE, wc)
    BwH = B_sets(wE, wc, HE, Hc)
    BHH = B_sets(HE, Hc, HE, Hc)
    disc = BwH*BwH - Bww*BHH
    eps0 = (-BwH + np.sqrt(disc))/BHH
    print(f"\n=== {cname}:  B(w,w)={Bww:+.6f}  B(w,H)={BwH:+.6f}  B(H,H)={BHH:+.6f}  eps_0={eps0:.6f} ===")
    if Bww >= 0:
        pr("    !! primitive direction NOT spacelike — numerical red flag, skipping"); continue
    for pname, plist in PROBES:
        K = len(plist)
        # target rows
        tw = np.array([float(wc @ pair_rows(wE, pk)) for pk in plist])
        tH = np.array([float(Hc @ pair_rows(HE, pk)) for pk in plist])
        for dname, dE in DICTS:
            t0 = time.time()
            M = np.stack([pair_rows(dE, pk) for pk in plist])         # (K, n)
            nrm = np.abs(M).max(axis=1); M = M/nrm[:, None]
            twn = tw/nrm; tHn = tH/nrm
            nvar = M.shape[1]
            def feas(eps, ret_l1=False):
                t = twn + eps*tHn; eta = 1e-9
                r = linprog(np.ones(nvar), A_ub=np.vstack([M, -M]),
                            b_ub=np.concatenate([t + eta, -t + eta]), bounds=(0, None), method='highs')
                return (r.status == 0, (r.fun if r.status == 0 else np.inf)) if ret_l1 else (r.status == 0)
            if feas(0.0):
                es = 0.0
            else:
                lo, hi = 0.0, 8*eps0
                while not feas(hi):
                    hi *= 2
                    if hi > 1e4*eps0: hi = np.inf; break
                if np.isinf(hi):
                    es = np.inf
                else:
                    for _ in range(42):
                        mid = (lo + hi)/2
                        if feas(mid): hi = mid
                        else: lo = mid
                    es = hi
            l1 = feas(es*1.02, ret_l1=True)[1] if np.isfinite(es) else np.inf
            ratio = es/eps0 if np.isfinite(es) else np.inf
            dt = time.time() - t0
            pr(f"    {pname}(K={K:>2}) x {dname}(n={len(dE[0]):>4}): eps*={es:<10.6f} "
                  f"eps*/eps0={ratio:<9.4f} |c|1={l1:<9.3f} [{dt:.0f}s]")
            rows_out.append(dict(config=cname, probes=pname, K=K, dict=dname, n=len(dE[0]),
                                 eps0=eps0, eps_star=es, ratio=ratio, l1=l1))
            with open("effectivity_gap_v1.csv","w",newline="") as _f:
                _w=csv.DictWriter(_f,fieldnames=list(rows_out[0].keys())); _w.writeheader()
                for _r in rows_out: _w.writerow(_r)

with open("effectivity_gap_v1.csv", "w", newline="") as f:
    wcsv = csv.DictWriter(f, fieldnames=list(rows_out[0].keys())); wcsv.writeheader()
    for r in rows_out: wcsv.writerow(r)

print("\n================ VERDICT (ratio = eps*/eps_0 at richest probes P3, by dictionary) ================")
for cname, *_ in CONFIGS:
    rr = [r for r in rows_out if r['config'] == cname and r['probes'] == 'P3']
    if rr:
        tr = "  ->  ".join(f"{r['dict']}:{r['ratio']:.3f}" for r in rr)
        last = rr[-1]['ratio']
        verdict = ("SATURATION-CONSISTENT (<=1)" if last <= 1.02 else
                   "approaching 1 — enrichment-limited" if last <= 2.0 else
                   "elevated — keep enriching / candidate floor")
        pr(f"  {cname:<16} {tr}   => {verdict}")
print(f"\n[total {time.time()-t00:.0f}s]  saturation predicts the enrichment limit <= 1 for every K;")
pr("a robust floor > 1 under enrichment along any direction = the registered falsifier of (S).")
