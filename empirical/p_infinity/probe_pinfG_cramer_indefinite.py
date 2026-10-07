"""probe_pinfG_cramer_indefinite.py -- P-inf-G strike 1b: is the fluctuation-free (PNT-mean)
window Weil form indefinite?  (Proposition G.4 candidate; the base-point diagnosis of
probe_pinfG_cubic_drift made rigorous.)

THE SCHUR CERTIFICATE ALREADY IN HAND: d0_cramer(lam=2.0) = 3.448 > bare0 ~ 2.78 -- a Schur
complement exceeding its diagonal entry is impossible for a PSD form, so the lam=2.0 Cramer
interior is indefinite.  This probe settles it spectrally at every window and kills (or
confirms) the convention worry: the smooth prime mass on (0, log 2) is fictitious (no
prime powers there); does removing it restore positivity?

PRE-REGISTERED (GPD, fixed before the run):
  I1 (indefiniteness): min eig(K_cramer) < -1e-3 at >= 4 of the 5 windows under
      convention A (smooth mass from u=0).  FALSIFIER: definite at >= 2 windows =>
      the lam=2.0 Schur certificate is a convention artifact; G.4 dies as stated.
  I2 (robustness): the same verdict under convention B (smooth mass from u=log 2).
      FALSIFIER: definite under B at >= 2 windows => G.4 must carry the convention
      caveat explicitly (the (0, log 2) deficit is then itself the indefinite agent --
      report as the finding instead).
  I3 (anatomy, report-only): for the top negative directions: parity under reflection,
      boundary-vs-bulk localization, dominant frequency band -- what the arithmetic
      fluctuation must rescue (input to the corrected per-arrival instrument).
  I4 (scale sanity): |min eig| in [1e-3, 5] (an O(0.01-1) violation -- float64-safe,
      far from the mp floors; if marginal (<1e-6) escalate to mp before any claim).

Float64 is sufficient by I4's expected scale (K_cramer has no exp-small ladder; its
spectrum is O(1) -- the question is a sign at O(0.1), not a near-null resolution).
Builder: the certified-lineage build_QW_mode from probe_pinfG_cubic_drift (exec-import).
"""
import sys
import time
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")

src = open("empirical/p_infinity/probe_pinfG_cubic_drift.py", encoding="utf-8").read()
exec(src.split("def prime_atom_Q")[0].split('"""', 2)[2])   # primes_upto, build_QW_mode
mp.mp.dps = 30


def build_cramer_B(lam, N):
    """Convention B: smooth prime mass on [log 2, L] only."""
    L = 2 * mp.log(lam)
    w = lambda k: 2 * mp.pi * k / L
    lo = mp.log(2)
    pts = mp.linspace(0, L, 14)
    ptsB = mp.linspace(lo, L, 12)
    S, D = {}, {}
    for k in range(-N, N + 1):
        wk = w(k)
        A = mp.quad(lambda y: mp.sin(wk * y) * 2 * mp.cosh(y / 2), pts)
        Bb = mp.quad(lambda y: mp.exp(y / 2) * mp.sin(wk * y) / (2 * mp.sinh(y)) if y != 0 else wk / 2, pts)
        P = mp.quad(lambda u: mp.exp(u / 2) * mp.sin(wk * u), ptsB)
        S[k] = A - Bb - P
    tailL = mp.log(mp.tanh(L / 2)) / 2
    for k in range(0, N + 1):
        wk = w(k)
        qd = lambda y: 2 * (1 - y / L) * mp.cos(wk * y)
        A = mp.quad(lambda y: qd(y) * 2 * mp.cosh(y / 2), pts)
        Bint = mp.quad(lambda y: (mp.exp(y / 2) * qd(y) - 2) / (2 * mp.sinh(y)) if y != 0
                       else (mp.mpf(1) / 2 - 1 / L), pts)
        WR = (mp.log(4 * mp.pi) + mp.euler) + Bint + 2 * tailL
        P = mp.quad(lambda u: mp.exp(u / 2) * 2 * (1 - u / L) * mp.cos(wk * u), ptsB)
        D[k] = A - WR - P
    dim = 2 * N + 1
    Q = mp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            n, m_ = i - N, j - N
            Q[i, j] = D[abs(n)] if n == m_ else (S[m_] - S[n]) / (mp.pi * (n - m_))
    return Q, L


def Q_to_K_float(Q, N):
    dim = 2 * N + 1
    Qf = np.array([[complex(Q[i, j]) for j in range(dim)] for i in range(dim)])
    n_idx = np.arange(-N, N + 1)
    i_idx = np.arange(dim)
    B = np.exp(2j * np.pi * np.outer(n_idx, i_idx) / dim) / np.sqrt(dim)
    K = np.conj(B).T @ Qf @ B
    return np.real(0.5 * (K + np.conj(K).T))


CASES = [(1.8, 20), (2.0, 24), (2.2, 27), (2.35, 30), (2.5, 32)]
print("== the spectrum of the fluctuation-free (Cramer/PNT-mean) window form ==")
res = {}
for lam, N in CASES:
    t0 = time.time()
    dim = 2 * N + 1
    QA, L, _ = build_QW_mode(mp.mpf(repr(lam)), N, "cramer")
    QB, _ = build_cramer_B(mp.mpf(repr(lam)), N)
    KA, KB = Q_to_K_float(QA, N), Q_to_K_float(QB, N)
    evA, vA = np.linalg.eigh(KA)
    evB, vB = np.linalg.eigh(KB)
    negA, negB = int((evA < 0).sum()), int((evB < 0).sum())
    res[lam] = dict(evA=evA, vA=vA, evB=evB, negA=negA, negB=negB, L=float(L), dim=dim)
    print(f"   lam={lam} ({time.time()-t0:.0f}s): conv-A min eig = {evA[0]:+.4f} "
          f"(#neg {negA});  conv-B min eig = {evB[0]:+.4f} (#neg {negB})")

print("\n== I1/I2 verdicts ==")
i1 = sum(res[l]["evA"][0] < -1e-3 for l, _ in CASES) >= 4
i2 = sum(res[l]["evB"][0] < -1e-3 for l, _ in CASES) >= 4
i4 = all(1e-3 <= abs(res[l]["evA"][0]) <= 5 for l, _ in CASES)
print(f"   I1 (conv A indefinite >= 4/5): {'SURVIVES' if i1 else 'FIRED'}")
print(f"   I2 (conv B same verdict):      {'SURVIVES' if i2 else 'FIRED -- convention caveat'}")
print(f"   I4 (scale float64-safe):       {'ok' if i4 else 'MARGINAL -- escalate to mp'}")

print("\n== I3: anatomy of the negative directions (conv A, lam=2.5) ==")
big = res[2.5]
ev, V = big["evA"], big["vA"]
dim, L = big["dim"], big["L"]
x = np.arange(dim) * L / dim
refl = np.array([(dim - i) % dim for i in range(dim)])
for k in range(min(3, big["negA"])):
    v = V[:, k]
    par = float(v @ v[refl])
    r = np.abs(x - L / 2)
    bnd = float((v[r >= (2/3) * (L/2)]**2).sum())
    vf = np.fft.fft(v)
    kf = int(np.argmax(np.abs(vf[:dim // 2])))
    print(f"   eig {ev[k]:+.4f}: parity={par:+.2f}  boundary-third mass={bnd:.2f}  "
          f"dominant DFT mode k={kf} (omega ~ {2*np.pi*kf/L:.1f})")

np.savez("empirical/p_infinity/pinfG_cramer_spectrum.npz",
         **{f"evA_{l}": res[l]["evA"] for l, _ in CASES},
         **{f"evB_{l}": res[l]["evB"] for l, _ in CASES})

print("\nRESULT: " + ("GREEN -- Proposition G.4 stands (both conventions)" if (i1 and i2)
                      else "PARTIAL -- see I1/I2 (convention caveat path)"))
