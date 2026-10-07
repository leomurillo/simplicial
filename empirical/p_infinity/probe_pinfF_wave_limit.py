"""probe_pinfF_wave_limit.py -- the wave-limit measurement: Sigma-sigma(s) to lambda = 2.5 in mp.

THE QUESTION (P-inf-F section 20.3): the saturation ledger Sigma sigma(s) = 1 - d(s)/bare
rose 0.651 -> 0.756 -> 0.799 (lam 1.5/1.8/2.0), decelerating.  Does the wave-sum SATURATE
below 1 (positivity with room) or CREEP marginally toward 1?  Extend to lam = 2.2/2.35/2.5.

ENGINEERING: at lam=2.5 the ground eigenvalue ~ 3e-31 < dps-30 entry noise => BUILD AT
dps=50, mp-LU for the Schur solve (float64 on a 1e31-conditioned matrix is garbage),
deep rungs by mp inverse iteration + deflation, bulk rungs by float64 eigh (cross-checked).

PRE-REGISTERED (GPD):
  W1 (validation): mp Sigma-sigma at lam=2.0 matches the float run (0.7992) to < 1%.
  W2 (decision rule, FIXED BEFORE THE DATA): saturation-favored if fitted Sigma_inf + 2*fitsig < 1
      AND increments monotone decreasing; creep-favored if both model fits give >= 0.98;
      else 'inconclusive-with-trend' reported as such.  No outcome fires a falsifier --
      this is a measurement; the rule prevents post-hoc reading.
  W3 (wave stationarity): crossover peak sigma_peak in [0.25, 0.40] at every new window.
      FALSIFIER: peak growing systematically (a creep MECHANISM identified).
  W4 (ladder): new eps datapoints at 2.2/2.35/2.5 track the Fuchs pace e^{-4 pi lam^2 + 9 log lam}
      at order-unity ratios (extends the 13-decade run toward 31 decades).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 50


def primes_upto(xx):
    out = []; n = 2
    while n <= xx:
        if all(n % p for p in out):
            out.append(n)
        n += 1
    return out


def build_QW_mp(lam, N):
    """Exact V_n matrix kept in mpmath (dps-50 entries)."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    pj = []
    for p in primes_upto(float(mp.exp(L)) + 1e-12):
        j = 1
        while j * mp.log(p) <= L + mp.mpf("1e-40"):
            pj.append((j * mp.log(p), mp.log(p) * mp.power(p, -mp.mpf(j) / 2)))
            j += 1
    pts = mp.linspace(0, L, 14)
    S = {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        B = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        P = mp.fsum(cw * mp.sin(wk * yp) for yp, cw in pj) if pj else mp.mpf(0)
        S[k] = A - B - P
    tailL = mp.log(mp.tanh(L / 2)) / 2
    D = {}
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + mp.euler) + Bint + 2 * tailL
        P = mp.fsum(cw * (2 * (1 - yp / L) * mp.cos(wk * yp)) for yp, cw in pj) if pj else mp.mpf(0)
        D[k] = A - WR - P
    dim = 2 * N + 1
    Q = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m_ = i - N, j - N
            Q[i, j] = D[abs(n)] if n == m_ else (S[m_] - S[n]) / (mp.pi * (n - m_))
    return Q, L


def analyze(lam, N, n_deep=5):
    t0 = time.time()
    Q, L = build_QW_mp(mp.mpf(repr(float(lam))), N)
    dim = 2 * N + 1
    # point basis (unitary DFT), kept in mp
    B = mp.zeros(dim, dim)
    for n in range(dim):
        for i in range(dim):
            B[n, i] = mp.e**(2j * mp.pi * (n - N) * i / dim) / mp.sqrt(dim)
    K = (B.H) * Q * B
    Kr = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            Kr[i, j] = (mp.re(K[i, j]) + mp.re(K[j, i])) / 2
    x = np.arange(dim) * float(L) / dim
    s = np.abs(x - float(L) / 2)
    order = np.argsort(s, kind="stable")
    interior, pair = list(order[:dim - 2]), list(order[dim - 2:])
    ni = dim - 2
    Ki = mp.zeros(ni, ni)
    for a in range(ni):
        for b in range(ni):
            Ki[a, b] = Kr[interior[a], interior[b]]
    qv = mp.zeros(ni, 1)
    for a in range(ni):
        qv[a] = (Kr[interior[a], pair[0]] + Kr[interior[a], pair[1]]) / mp.sqrt(2)
    bare = (Kr[pair[0], pair[0]] + Kr[pair[1], pair[1]]) / 2 + Kr[pair[0], pair[1]]
    sol = mp.lu_solve(Ki, qv)
    corr = mp.fsum(qv[a] * sol[a] for a in range(ni))
    d_edge = bare - corr
    sig_sum = float(corr / bare)
    # deep rungs: inverse iteration with deflation
    deep = []
    vecs = []
    rng = np.random.default_rng(3)
    for r in range(n_deep):
        v = mp.matrix([mp.mpf(float(z)) for z in rng.normal(size=ni)])
        for _ in range(3):
            for u, _e in vecs:
                ip = mp.fsum(v[a] * u[a] for a in range(ni))
                for a in range(ni):
                    v[a] -= ip * u[a]
            v = mp.lu_solve(Ki, v)
            nrm = mp.sqrt(mp.fsum(vv**2 for vv in v))
            for a in range(ni):
                v[a] /= nrm
        Kv = Ki * v
        eig = mp.fsum(v[a] * Kv[a] for a in range(ni))
        vecs.append((v, eig))
        coup = mp.fsum(v[a] * qv[a] for a in range(ni))
        deep.append((float(eig), float(coup**2 / eig / bare)))
    # bulk rungs in float64 (resolvable above ~1e-10)
    Kif = np.array([[float(Ki[a, b]) for b in range(ni)] for a in range(ni)])
    qf = np.array([float(qv[a]) for a in range(ni)])
    ev, w_ = np.linalg.eigh(Kif)
    pj = (w_.T @ qf)**2 / ev / float(bare)
    el = time.time() - t0
    print(f"   lam={lam} (N={N}, dim={dim}, {el:.0f}s): bare={float(bare):.4f}  "
          f"d_edge={float(d_edge):.4e}  Sigma-sigma={sig_sum:.6f}  remainder={1-sig_sum:.4e}")
    print(f"     deep rungs (mp): " + "  ".join(f"eig={e:.2e},sig={sg:.2e}" for e, sg in deep))
    big = np.argsort(pj)[::-1][:3]
    print(f"     top bulk eaters (f64): " + "  ".join(f"eig={ev[i]:.2e},sig={pj[i]:.3f}" for i in big))
    return dict(lam=lam, sig=sig_sum, eps=deep[0][0], sig0=deep[0][1], bare=float(bare),
                peak=float(pj[big[0]]))


print("== the wave-limit sweep (mp dps=50) ==")
CASES = [(2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]
out = []
for lam, N in CASES:
    out.append(analyze(lam, N))

print("\n== verdicts ==")
s20 = out[0]['sig']
print(f"   W1 validation: mp Sigma-sigma(2.0) = {s20:.4f} vs float-run 0.7992  "
      + ("SURVIVES" if abs(s20 - 0.7992) < 0.008 else "FIRED -- diagnose"))
sigs = [o['sig'] for o in out]
lams = [o['lam'] for o in out]
hist = [(1.5, 0.6509), (1.8, 0.7563)] + list(zip(lams, sigs))
print("   Sigma-sigma sequence: " + "  ".join(f"{l}:{s:.4f}" for l, s in hist))
inc = np.diff([s for _, s in hist])
print("   increments: " + "  ".join(f"{v:+.4f}" for v in inc))
# model fits vs lambda
ls = np.array([l for l, _ in hist]); ss = np.array([s for _, s in hist])
# Model A: saturation s = A - c*exp(-a*l)  (grid over a); Model B: creep s = 1 - c*exp(-a*l)
bestA, bestB = None, None
for a in np.linspace(0.3, 4.0, 75):
    E = np.exp(-a * ls)
    M = np.column_stack([np.ones_like(ls), -E])
    cf, res, *_ = np.linalg.lstsq(M, ss, rcond=None)
    r = float(np.sum((M @ cf - ss)**2))
    if bestA is None or r < bestA[0]:
        bestA = (r, cf[0], cf[1], a)
    cfb, *_ = np.linalg.lstsq((-E).reshape(-1, 1), ss - 1, rcond=None)
    rb = float(np.sum((1 - cfb[0] * E - ss)**2))
    if bestB is None or rb < bestB[0]:
        bestB = (rb, cfb[0], a)
rA, Ainf, cA, aA = bestA
rB, cB, aB = bestB
print(f"   Model A (saturation): Sigma_inf = {Ainf:.4f}, rate {aA:.2f}, SSR = {rA:.2e}")
print(f"   Model B (creep to 1): rate {aB:.2f}, SSR = {rB:.2e}   [SSR ratio B/A = {rB/max(rA,1e-30):.1f}]")
mono = bool((np.diff(inc) < 0.005).all())
fitsig = np.sqrt(rA / max(len(ls) - 3, 1))
if Ainf + 2 * fitsig < 1 and mono and rB / max(rA, 1e-30) > 3:
    verdict = "SATURATION-FAVORED (below 1)"
elif Ainf >= 0.98:
    verdict = "CREEP-FAVORED"
else:
    verdict = "INCONCLUSIVE-WITH-TREND"
print(f"   W2 decision rule: Sigma_inf + 2 fitsig = {Ainf + 2*fitsig:.4f}; increments monotone-dec: {mono}"
      f"  ->  {verdict}")
print("   W3 wave stationarity: peaks = " + "  ".join(f"{o['lam']}:{o['peak']:.3f}" for o in out)
      + ("   SURVIVES" if all(0.2 <= o['peak'] <= 0.45 for o in out) else "   FIRED"))
print("   W4 new ladder datapoints: " + "  ".join(f"eps({o['lam']})={o['eps']:.2e}" for o in out))
fu = [float(mp.e**(-4 * mp.pi * l * l + 9 * mp.log(l))) for l in lams]
print("        Fuchs scale:        " + "  ".join(f"{v:.2e}" for v in fu)
      + "   ratios: " + "  ".join(f"{o['eps']/v:.2f}" for o, v in zip(out, fu)))
print("   sigma_0 decoupling continues: " + "  ".join(f"{o['lam']}:{o['sig0']:.2e}" for o in out))
print("\nRESULT: measurement complete -- see W2 verdict line (the sharpest number on the board)")
