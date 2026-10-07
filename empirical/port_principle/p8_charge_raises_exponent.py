"""
Port Principle — P8: a conserved charge raises the copy-threshold exponent (symmetry restriction x copy lift).

Setting (exact int64 surrogates, witnesses re-verified at 50 digits). Five levels, E' = (1, th, th^2, 1+th) with
th^3 = th + 1 (spacing module of rank 3), near equilibrium f = E + delta u, u' = (3/10, -7/10, 9/20, 1/5).
Charge q' = (1, 1, 1, 2) (q_0 = 0). Under the symmetry restriction (Section 7) the admissible relation vectors also
satisfy c.q = 0, i.e. a in the sublattice Lambda_q = {a1 + a2 + a3 + 2 a4 = 0}. Parametrize a = (-a2-a3-2a4, a2, a3, a4);
then c = (a4, -a2-a3-2a4, a2, a3, a4), cost = (2|a4| + |a2+a3+2a4| + |a2| + |a3|)/2, and
a.E' = (a2 + a4)(th - 1) + a3 (th^2 - 1): the charge-neutral spacing module has rank 2.
GGE states e^{-beta(E - mu q)} are exactly those with f|Lambda_q proportional to E|Lambda_q, so delta measures the
distance from the generalized Gibbs family.

PRE-REGISTERED FALSIFIERS (written 2026-10-01, before the first run)
    K8a [exact surrogate]: with the charge, the log-log slope of n*_q vs 1/delta over delta = 1e-2 .. 1e-6 lies in
         [0.40, 0.60] (rank 2), whereas without it (P7.A3, same spectrum and u) the slope is ~1/3.
    K8b [exact]: n*_q >= n* (unrestricted) at every delta (restriction shrinks the admissible set), and
         n*_q / n* grows: ratio at delta = 1e-6 exceeds the ratio at 1e-2.
    K8c: surrogate stability (2^-40 vs 2^-43) and 50-digit witness verification.
    L8: any fails.
"""
import sys, math
from fractions import Fraction as F
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 60
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

th = mp.findroot(lambda t: t ** 3 - t - 1, 1.3247)
Ev = [mp.mpf(1), th, th ** 2, 1 + th]
uv = [F(3, 10), F(-7, 10), F(9, 20), F(1, 5)]
BIG = np.int64(2 ** 62)

def ints(delta, qbits):
    Q = mp.mpf(2) ** qbits
    Ei = [int(mp.nint(x * Q)) for x in Ev]
    Fi = [Ei[k] + int(mp.nint(mp.mpf(uv[k].numerator) / uv[k].denominator * delta * Q)) for k in range(4)]
    return Ei, Fi

def scan_charge(Ei, Fi, B0=4):
    """min cost over (a2,a3,a4) with a = (-a2-a3-2a4, a2, a3, a4), a.E < 0 < a.F. Solve for a4.
    a.X = a2 (X2 - X1) + a3 (X3 - X1) + a4 (X4 - 2 X1)."""
    e2, e3, e4 = (np.int64(Ei[1] - Ei[0]), np.int64(Ei[2] - Ei[0]), np.int64(Ei[3] - 2 * Ei[0]))
    g2, g3, g4 = (np.int64(Fi[1] - Fi[0]), np.int64(Fi[2] - Fi[0]), np.int64(Fi[3] - 2 * Fi[0]))
    assert e4 > 0 and g4 > 0
    B = max(4, B0)
    while True:
        best, wit = int(BIG), None
        a3 = np.arange(-B, B + 1, dtype=np.int64)[None, :]
        for s0 in range(-B, B + 1, 64):
            a2 = np.arange(s0, min(s0 + 64, B + 1), dtype=np.int64)[:, None]
            R = -(a2 * e2 + a3 * e3); hi = (R - 1) // e4
            S = -(a2 * g2 + a3 * g3); lo = S // g4 + 1
            ok = lo <= hi
            a4 = np.clip(0, lo, hi)            # cost is flat between 0 and -(a2+a3)/2 in a4, convex elsewhere
            c = (2 * np.abs(a4) + np.abs(a2 + a3 + 2 * a4) + np.abs(a2) + np.abs(a3)) // 2
            c = np.where(ok, c, BIG); ix = np.unravel_index(np.argmin(c), c.shape)
            if c[ix] < best:
                best = int(c[ix]); a2w, a3w, a4w = int(a2[ix[0], 0]), int(a3[0, ix[1]]), int(a4[ix])
                wit = (-a2w - a3w - 2 * a4w, a2w, a3w, a4w)
        if best <= B: return best, wit
        B = best if best < int(BIG) else 2 * B

# the unrestricted threshold, same spectrum (scan copied verbatim from P7)
def scan(Ev, Fv, chunk=48, B0=4):
    """Iterative deepening; complete once best <= B (any cheaper a has ||a||_inf <= cost). B0 only sets the
    starting radius, so correctness does not depend on it."""
    m = len(Ev)
    E = [np.int64(x) for x in Ev]; Fq = [np.int64(x) for x in Fv]
    B = max(4, B0)
    while True:
        assert (m + 1) * (B + 1) * max(abs(int(x)) for x in list(Ev) + list(Fv)) < 2 ** 62, "overflow risk"
        best, wit = int(BIG), None
        rng_ = np.arange(-B, B + 1, dtype=np.int64)
        if m == 3:
            a2 = rng_[None, :]
            for s0 in range(-B, B + 1, chunk):
                a1 = np.arange(s0, min(s0 + chunk, B + 1), dtype=np.int64)[:, None]
                R = -(a1 * E[0] + a2 * E[1]); hi = (R - 1) // E[2]
                S = -(a1 * Fq[0] + a2 * Fq[1]); lo = S // Fq[2] + 1
                ok = lo <= hi; a3 = np.clip(0, lo, hi)
                c = (np.abs(a1 + a2 + a3) + np.abs(a1) + np.abs(a2) + np.abs(a3)) // 2
                c = np.where(ok, c, BIG); ix = np.unravel_index(np.argmin(c), c.shape)
                if c[ix] < best:
                    best = int(c[ix]); wit = (int(a1[ix[0], 0]), int(a2[0, ix[1]]), int(a3[ix]))
        else:
            a2 = rng_[:, None]; a3 = rng_[None, :]
            base2 = a2 * E[1] + a3 * E[2]; baseF = a2 * Fq[1] + a3 * Fq[2]; s23 = a2 + a3; n23 = np.abs(a2) + np.abs(a3)
            for a1 in range(-B, B + 1):
                R = -(np.int64(a1) * E[0] + base2); hi = (R - 1) // E[3]
                S = -(np.int64(a1) * Fq[0] + baseF); lo = S // Fq[3] + 1
                ok = lo <= hi; a4 = np.clip(0, lo, hi)
                c = (np.abs(a1 + s23 + a4) + abs(a1) + n23 + np.abs(a4)) // 2
                c = np.where(ok, c, BIG); ix = np.unravel_index(np.argmin(c), c.shape)
                if c[ix] < best:
                    best = int(c[ix]); wit = (a1, int(rng_[ix[0]]), int(rng_[ix[1]]), int(a4[ix]))
        if best <= B: return best, wit
        B = best if best < int(BIG) else 2 * B

def verify50(a, delta):
    aE = sum(ai * e for ai, e in zip(a, Ev))
    af = aE + delta * sum(ai * mp.mpf(u.numerator) / u.denominator for ai, u in zip(a, uv))
    return aE < 0 < af and (a[0] + a[1] + a[2] + 2 * a[3]) == 0

xs = np.arange(2.0, 6.01, 0.5)
nq, nf, ds = [], [], []
okstab, okver, okmono = True, True, True
for x in xs:
    delta = mp.mpf(10) ** (-mp.mpf(x))
    E40, F40 = ints(delta, 40); n40, w40 = scan_charge(E40, F40)
    E43, F43 = ints(delta, 43); n43, _ = scan_charge(E43, F43, B0=n40)
    okstab &= n40 == n43; okver &= verify50(w40, delta)
    m0, _ = scan(E40, F40)
    okmono &= n40 >= m0
    nq.append(n40); nf.append(m0); ds.append(float(delta))
    print(f"   delta=1e-{x:.1f}: n*_charge = {n40:>6} (witness a={w40})   n*_free = {m0:>5}")
sq = np.polyfit(np.log(1 / np.array(ds)), np.log(nq), 1)[0]
sf = np.polyfit(np.log(1 / np.array(ds)), np.log(nf), 1)[0]
check("H8.K8a [exact surrogate] a conserved charge raises the exponent: rank 3 -> rank 2", 0.40 <= sq <= 0.60,
      f"slope with charge {sq:.3f}; without {sf:.3f}")
check("H8.K8b [exact] restriction only raises thresholds, increasingly", okmono and nq[-1] / nf[-1] > nq[0] / nf[0],
      f"ratio n*_q/n* : {nq[0]/nf[0]:.2f} at 1e-2 -> {nq[-1]/nf[-1]:.2f} at 1e-6")
check("H8.K8c surrogate stability and 50-digit witnesses (charge-neutral, violating)", okstab and okver)
print(f"\nP8: {sum(res)}/{len(res)} PASS")
