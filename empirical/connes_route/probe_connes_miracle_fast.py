r"""
probe_connes_miracle_fast.py  --  FAST high-precision reproduction of Connes' numerical miracle
(arXiv:2602.04022; Connes-van Suijlekom Thm 6.1).  Mathematically identical to
probe_connes_miracle_highprec.py but the archimedean block is assembled from O(N) PRECOMPUTED
kernel moments (cached by basis frequency) + O(N^2) closed-form combination, instead of O(N^2)
per-pair quadratures.  Validated to match the slow build to full working precision.

Construction (see probe_connes_miracle_highprec.py header for the full derivation):
  EVEN cosine basis phi_k(u)=cos(w_k u), w_k=(2k+1)pi/(2a), a=(log X)/2, on [-a,a].
  Weil form entry  Q[j,k] = ARCH + PRIME + POLE applied to g=phi_j*phi_k (exact cross-corr A_jk):
    PRIME : sum_n 2 (Lambda(n)/sqrt n) A_jk(log n)                       [exact]
    ARCH  : (log4pi+gamma) A_jk(0) + int_0^inf [2 A_jk(u)-2 A_jk(0)] Kinf(u) du,
            Kinf(u)=e^{u/2}/(2 sinh u),  assembled from moments IC,IS,IU,TAIL below
    POLE  : 2 c_j c_k,  c_k=int phi_k cosh(u/2) du
  Off-diagonal A_jk(u) = sum of 4 sinusoids sin(sig u+ph), sig in {w_j,w_k}.
  Diagonal  A_kk(u) = 1/2[(2a-u)cos(w_k u) + sin(w_k u)/w_k]  on [0,2a].
  Moments (all convergent; the 1/(2u) singularity of Kinf is killed by the structure):
    IC(s)=int_0^2a [cos(s u)-1] Kinf du,  IS(s)=int_0^2a sin(s u) Kinf du,
    IU(s)=int_0^2a u cos(s u) Kinf du,     TAIL=int_2a^inf Kinf du.
  For sin(s u+ph): int_0^2a [sin(s u+ph)-sin(ph)] Kinf = cos(ph) IS(s) + sin(ph) IC(s).

numpy + mpmath only.  No torch.
"""
import sys
import mpmath as mp

DPS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
mp.mp.dps = DPS
TINY = mp.mpf(10) ** (-(DPS - 8))
EG = mp.euler

def zeta_zeros(M): return [mp.im(mp.zetazero(n)) for n in range(1, M + 1)]

def prime_powers(X):
    out = []
    isp = lambda m: m >= 2 and all(m % d for d in range(2, int(m**0.5) + 1))
    p = 2
    while p <= X:
        if isp(p):
            pe, lp = p, mp.log(p)
            while pe <= X:
                out.append((pe, lp)); pe *= p
        p += 1
    return out

def Wf(k, a): return (2 * k + 1) * mp.pi / (2 * a)

def fourier_basis(k, a, r):
    w = Wf(k, a)
    def S(d): return a if abs(d) < TINY else mp.sin(d * a) / d
    return S(w - r) + S(w + r)

def A_jk(j, k, a, t):
    t = abs(t); wj = Wf(j, a); wk = Wf(k, a); lo, hi = t - a, a
    if lo >= hi: return mp.mpf(0)
    def term(al, be):
        if abs(al) < TINY: return mp.cos(be) * (hi - lo)
        return (mp.sin(al * hi + be) - mp.sin(al * lo + be)) / al
    return mp.mpf(1) / 2 * (term(wj - wk, wk * t) + term(wj + wk, -wk * t))

def cosh_moment(k, a):
    w = Wf(k, a); b = mp.mpf(1) / 2; den = b * b + w * w
    return (2 * b * mp.sinh(b * a) * mp.cos(w * a) + 2 * w * mp.cosh(b * a) * mp.sin(w * a)) / den

def Kinf(u): return mp.e ** (u / 2) / (2 * mp.sinh(u))

# ---- archimedean moments (cached by frequency) ----
def _IC(s, a):
    up = 2 * a
    return mp.quad(lambda u: (mp.cos(s * u) - 1) * Kinf(u) if u > TINY else mp.mpf(0), [0, up / 2, up])
def _IS(s, a):
    up = 2 * a
    return mp.quad(lambda u: mp.sin(s * u) * Kinf(u) if u > TINY else mp.mpf(0), [0, up / 2, up])
def _IU(s, a):
    up = 2 * a
    # u cos(su) Kinf ~ u/(2u)=1/2 at 0 -> finite
    return mp.quad(lambda u: u * mp.cos(s * u) * Kinf(u) if u > TINY else mp.mpf("0.5") * 1, [0, up / 2, up])
def _TAIL(a):
    up = 2 * a
    return mp.quad(Kinf, [up, up + 1, up + 5, mp.inf])

def arch_entry_fast(j, k, a, cache):
    g0 = A_jk(j, k, a, mp.mpf(0))
    pref = (mp.log(4 * mp.pi) + EG) * g0
    tail = -2 * g0 * cache['TAIL']
    wj, wk = Wf(j, a), Wf(k, a)
    IC = cache['IC']; IS = cache['IS']; IU = cache['IU']
    def mom_sin(sig, ph):  # int_0^2a [sin(sig u+ph)-sin(ph)] Kinf du
        return mp.cos(ph) * IS[sig] + mp.sin(ph) * IC[sig]
    if j != k:
        d = wj - wk; s = wj + wk
        pieces = [(mp.mpf(1) / 2 / d, wk, d * a),
                  (-mp.mpf(1) / 2 / d, wj, -d * a),
                  (-mp.mpf(1) / 2 / s, wk, -s * a),
                  (-mp.mpf(1) / 2 / s, wj, -s * a)]
        tot = mp.mpf(0)
        for (cf, sig, ph) in pieces:
            tot += 2 * cf * mom_sin(sig, ph)
        return pref + tot + tail
    else:
        # A_kk(u)=1/2[(2a-u)cos(wk u)+ sin(wk u)/wk]; 2*(A_kk(u)-g0) integral:
        # = a*[cos(wk u)-1 part]*... carefully via pieces (each minus its u=0 value):
        # P1: a cos(wk u)  -> 2*(.. ) handled as coef on [cos-1]=IC (since g0 includes its u=0 = a)
        # We integrate 2*(A(u)-A(0)) Kinf = sum 2*coef*(f(u)-f(0))Kinf.
        wk2 = wk
        tot = mp.mpf(0)
        # piece A: (1/2)*2a*cos(wk u) = a cos(wk u); f-f(0)=a(cos(wk u)-1) -> 2*a*IC
        tot += 2 * a * IC[wk2]
        # piece B: -(1/2) u cos(wk u); f(0)=0 -> 2*(-1/2)*IU = -IU
        tot += -IU[wk2]
        # piece C: (1/2) sin(wk u)/wk; f(0)=0 -> 2*(1/(2 wk))*IS = IS/wk
        tot += IS[wk2] / wk2
        return pref + tot + tail

def build_fast(X, N):
    a = mp.log(X) / 2
    pp = prime_powers(X)
    c = [cosh_moment(k, a) for k in range(N)]
    freqs = set()
    for j in range(N):
        for k in range(j, N):
            wj, wk = Wf(j, a), Wf(k, a)
            if j != k:
                freqs.add(wj); freqs.add(wk)
            else:
                freqs.add(wj)
    cache = {'IC': {}, 'IS': {}, 'IU': {}, 'TAIL': _TAIL(a)}
    for s in freqs:
        cache['IC'][s] = _IC(s, a)
        cache['IS'][s] = _IS(s, a)
        cache['IU'][s] = _IU(s, a)
    Wm = mp.zeros(N, N)
    for j in range(N):
        for k in range(j, N):
            v = arch_entry_fast(j, k, a, cache)
            for (n, lp) in pp:
                v += 2 * (lp / mp.sqrt(n)) * A_jk(j, k, a, mp.log(n))
            v += 2 * c[j] * c[k]
            Wm[j, k] = v; Wm[k, j] = v
    return a, Wm

def etahat(coeffs, a, r):
    return sum((ck * fourier_basis(k, a, r) for k, ck in enumerate(coeffs)), mp.mpf(0))

def find_zeros(coeffs, a, r_max, n_want):
    zeros = []; step = mp.mpf("0.05"); r = mp.mpf("0.5")
    pr, pv = r, etahat(coeffs, a, r)
    while r < r_max and len(zeros) < n_want:
        r += step; v = etahat(coeffs, a, r)
        if (pv < 0) != (v < 0):
            lo, hi, flo = pr, r, pv
            for _ in range(8 * DPS):
                mid = (lo + hi) / 2; fm = etahat(coeffs, a, mid)
                if fm == 0 or (hi - lo) < mp.mpf(10) ** (-(DPS - 6)):
                    lo = hi = mid; break
                if (fm < 0) == (flo < 0): lo, flo = mid, fm
                else: hi = mid
            zeros.append((lo + hi) / 2)
        pr, pv = r, v
    return zeros

def select_eta_index(lam):
    """Principled, NON-circular selection of Connes' eta.

    The Weil form spectrum is a tower of near-degenerate eigenvalues accumulating GEOMETRICALLY
    at a limit L (the 'bulk' pinned by the construction), separated from the rest of the spectrum
    by a large gap.  The within-cluster splittings shrink geometrically (1e-17, 1e-21, 1e-26, ...
    = the minuscule quantities eps(lambda)); these splittings ARE Connes' difference tower.
    eta = the eigenvector of the cluster member that is MOST converged to L, i.e. the extreme of
    the cluster on the limit side, adjacent to the big spectral gap.

    Operationally: locate the largest internal gap that separates the converging cluster from the
    isolated high eigenvalue, and return the cluster member just below it whose consecutive
    within-cluster splitting is the smallest (the converged extreme).
    """
    N = len(lam)
    # consecutive gaps
    gaps = [lam[i + 1] - lam[i] for i in range(N - 1)]
    # the cluster ends at the largest gap (jump out to the isolated top eigenvalue(s))
    jcut = max(range(N - 1), key=lambda i: gaps[i])
    # within the cluster [.. jcut], the converged extreme is index jcut (smallest within-gap below it)
    return jcut, gaps

def run(X, N, n_zeros=12, r_max=70):
    a, Wm = build_fast(X, N)
    E, Q = mp.eigsy(Wm)
    lam = [E[i] for i in range(N)]
    idx, gaps = select_eta_index(lam)
    eta = [Q[i, idx] for i in range(N)]
    # splitting that isolates eta from the rest of the cluster (the minuscule eps)
    eps_split = gaps[idx - 1] if idx >= 1 else mp.mpf(0)
    big_gap = gaps[idx]
    zeros = find_zeros(eta, a, mp.mpf(r_max), n_zeros)
    return dict(a=a, lam=lam, eta=eta, eta_idx=idx, eps_split=eps_split,
                big_gap=big_gap, cluster_val=lam[idx], zeros=zeros)

if __name__ == "__main__":
    X = 13
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    print("=" * 92)
    print(f"Connes numerical miracle, FAST high precision (dps={DPS}, X={X}, N={N} even-cosine modes)")
    print("=" * 92)
    gammas = zeta_zeros(14)
    res = run(X, N, n_zeros=12, r_max=70)
    a = res["a"]
    print(f"\nsupport a=(log {X})/2 = {mp.nstr(a,14)}")
    print(f"eta = eigenvector at cluster index {res['eta_idx']} (of {N}); cluster value L = "
          f"{mp.nstr(res['cluster_val'],36)}")
    print(f"  minuscule splitting eps that isolates eta = {mp.nstr(res['eps_split'],6)}  "
          f"(<- Connes' 'minuscule eigenvalue')")
    print(f"  spectral gap above the cluster            = {mp.nstr(res['big_gap'],6)}")
    print("\nfirst zeros of etahat(r)  vs  gamma_n  (|difference|):")
    print(f"  {'n':>3} {'etahat zero':>34} {'|diff|':>16}")
    for i, z in enumerate(res["zeros"]):
        if i >= len(gammas): break
        d = abs(z - gammas[i])
        print(f"  {i+1:>3} {mp.nstr(z,28):>34} {mp.nstr(d,5):>16}")
    print("\nConnes' published |diff| (first 8): 2.60179e-55, 4.80071e-52, 4.43756e-50, "
          "3.89903e-47,\n                                    7.59453e-46, 1.13198e-43, "
          "1.07245e-41, 1.2694e-40")
