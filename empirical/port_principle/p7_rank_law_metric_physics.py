"""
Port Principle — P7: the resonance-rank law at intermediate ranks, for almost every spectrum, near resonance,
for harmonic modes, on real platforms, and its echo-yield dual.
Exact arithmetic (Python ints / Fractions / exact int64 surrogates) for every decision marked [exact];
witnesses of surrogate scans re-verified at 50 digits on the true spectrum.

PRE-REGISTERED FALSIFIERS (written 2026-10-01, before the first run; every branch reportable)

H7a INTERMEDIATE RANKS (1 < r < d-1). Claim: n* ~ delta^(-1/r) for a badly approximable spacing module M of rank r,
    whether or not the entropy direction u' "sees" the resonant kernel K = {a : a.E' = 0}. Near equilibrium
    f = E + delta u (beta = 1). Fitted log-log slopes of n* vs 1/delta must fall in:
      A1  d=4, E'=(1,phi,2),           u'=(3/10,-7/10,3/5)       [K-BLIND: u'.(-2,0,1)=0]   delta 1e-2..1e-6  [0.40,0.60]
      A2  d=5, E'=(1,phi,2,1+phi),     u'=(3/10,-7/10,9/20,1/5)  [K-visible, rank K = 2]   delta 1e-1.5..1e-4 [0.35,0.65]
      A3  d=5, E'=(1,th,th^2,1+th),    u'=(3/10,-7/10,9/20,1/5)  [K-visible]  (th^3=th+1) delta 1e-2..1e-6  [0.25,0.42]
      A4  d=5, E'=(1,th,th^2,1+th),    u'=(3/10,-7/10,9/20,-2/5) [K-BLIND: u'.(-1,-1,0,1)=0] delta 1e-2..1e-6 [0.25,0.42]
      A5  d=5, E'=(1,ps,ps^2,ps^3),    u'=(3/10,-7/10,9/20,1/5)  [full rank 4] (ps^4=ps+1) delta 1e-2..1e-8 [0.18,0.32]
    and every n* above the Theorem 6.9(a) lower bound (kappa per case, computed in-script).
    A6 (universality of the K-visible upper bound, NO Diophantine condition): d=4, E'=(1,1+xL,2) with xL very well
      approximable (continued fraction a_{k+1} = q_k^2), u'=(3/10,-7/10,9/20): every local exponent
      ln n*/ln(1/delta) <= 0.60 for delta in 1e-2..1e-7 (the lower bound may fail; report the minimum).
    Surrogates on the 2^-40 grid must agree with the 2^-43 grid; witnesses verified at 50 digits.
    L7a: any slope outside its window, any lower-bound violation, any surrogate instability/witness failure,
         any A6 exponent > 0.60.

H7b ALMOST EVERY SPECTRUM. Claim: for Lebesgue-a.e. gap ratio, ln n*/ln(1/delta) -> 1/2 (two ports / three levels).
    (i)  300 uniform random x in (1/4, 3/4) (exact rationals with denominator 2^100), two-port window (x, x(1+delta)),
         delta = 1e-12: >= 85% of local exponents in [0.40, 0.60] and median in [0.46, 0.54].
    (ii) Control, golden x = 1/phi (badly approximable): every local exponent in [0.42, 0.58] for delta in 1e-3..1e-70.
    (iii) Very well approximable xL (a_{k+1} = q_k^2, so q_{k+1} ~ q_k^3): local exponents OSCILLATE over
         delta in 1e-3..1e-70 with max >= 0.65 and min <= 0.35 (predicted band ~ [1/4, 3/4]).
    L7b: any of (i)-(iii) fails.

H7c NEAR RESONANCE (Proposition 6.8a). x = p/q + s*eta, window (x, x + w), w = x delta, here p/q = 1/2,
    eta in {(sqrt2-1)/100, (sqrt2-1)/1000} (exact surrogates), delta = 10^-0.25 .. 10^-9 (step 0.25).
    AWAY side (s=+1): for every delta, n* > 1/(q(eta+w)); and whenever w >= q^2 eta (eta + w),
         n* <= 1/(q(eta+w)) + q.
    TOWARD side (s=-1): whenever w > eta, n* = max(p,q) = 2; whenever q^2 eta^2 <= w <= eta,
         1/(q eta) < n* <= 1/(q eta) + q.
    L7c: any violation.

H7d HARMONIC MODES: ORDER OF THE ENGINE. Two Gibbs oscillators (truncated at L = 10 levels each; gaps eA, eB small
    integers; Boltzmann ratios rA, rB rational; A colder). The least total order |dnA| + |dnB| of a work-extracting
    level exchange in ONE copy equals k + m for the simplest fraction k/m in the Carnot window (eA/eB, fA/fB),
    fA = -ln rA, fB = -ln rB — checked by brute force over all level pairs on >= 30 instances whose predicted
    max(k, m) <= 8. L7d: any mismatch.

H7e PLATFORM NUMBERS (two-port window (x, x(1+delta)); qubit ports: n* = max(k,m); harmonic modes: order k+m).
    (i)  golden vs resonant: (n*_{1/2} / n*_{1/phi}) * delta^(1/2) in [0.2, 2] for delta = 1e-2..1e-10.
    (ii) two-ion axial modes x = 1/sqrt3 (badly approximable): n* delta^(1/2) in [0.1, 5] for delta = 1e-2..1e-10.
    (iii) transmon-like near resonance, eps = |alpha|/omega = 0.05, eta = eps/(2(2-eps)):
         away (x = 1/2 + eta): n* <= 41 for delta in [10^-2.5, 10^-1];
         toward (x = 1/2 - eta): n* = 2 for delta in {0.03, 0.1, 0.3}.
    L7e: any fails. (The full table is printed for the manuscript.)

H7f ECHO-YIELD DUALITY. For the spacing modules of P6.K6c (r = 1, 2, 3; bases (1), (1,phi), (1,th,th^2)):
    q_rec(eps) = least q >= 1 with max_j ||q alpha_j|| < eps (alpha_j = omega_j/omega_1) has log-log slope
    e_r (echo exponent): e_1 = 0 exactly (q_rec = 1); e_2 in [0.85,1.15] over eps 1e-1..1e-6; e_3 in [1.7,2.3]
    over eps 1e-1..1e-3.5. With the P6 yield exponents y_r (0.996, 0.498, 0.351): y_r (e_r + 1) in [0.85, 1.15].
    L7f: any fails.
"""
import sys, math
from fractions import Fraction as F
from itertools import product
import numpy as np
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 60
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

def simplest(below_lo, above_hi):
    """Stern-Brocot simplest fraction p/q in (lo, hi) (copied from P5, exact predicates)."""
    lp, lq, rp, rq = 0, 1, 1, 0
    while True:
        mp_, mq = lp + rp, lq + rq
        if below_lo(mp_, mq):
            k = 1
            while below_lo(lp + 2 * k * rp, lq + 2 * k * rq): k *= 2
            lo_k, hi_k = k, 2 * k
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if below_lo(lp + mid * rp, lq + mid * rq): lo_k = mid
                else: hi_k = mid
            lp, lq = lp + lo_k * rp, lq + lo_k * rq
        elif above_hi(mp_, mq):
            k = 1
            while above_hi(rp + 2 * k * lp, rq + 2 * k * lq): k *= 2
            lo_k, hi_k = k, 2 * k
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if above_hi(rp + mid * lp, rq + mid * lq): lo_k = mid
                else: hi_k = mid
            rp, rq = rp + lo_k * lp, rq + lo_k * lq
        else:
            return mp_, mq
# RUN LOG (2026-10-01): the first two runs hung in H7b. Cause: a transcription bug in this copy of simplest()
# (`rq + lo_k * rq` instead of P5/P6's `rq + lo_k * lq`), a checker artifact, not a result. Fixed; K/L text unchanged.
# H7a does not use simplest(); its first-run verdict (FAIL: A6 local exponent 0.604 > 0.60) is retained.

def window_frac(lo: F, hi: F):
    """simplest fraction strictly inside (lo, hi), exact rationals."""
    a, b, c, d = lo.numerator, lo.denominator, hi.numerator, hi.denominator
    return simplest(lambda p, q: p * b <= q * a, lambda p, q: p * d >= q * c)

def two_port(x: F, delta: F):
    k, m = window_frac(x, x * (1 + delta))
    return k, m

# ---------------------------------------------------------------- exact int64 scans (m = 3 or 4 coordinates)
BIG = np.int64(2 ** 62)
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

def surrogate(Evals, uvals, delta, qbits):
    Q = mp.mpf(2) ** qbits
    Ei = [int(mp.nint(x * Q)) for x in Evals]
    Fi = [Ei[k] + int(mp.nint(mp.mpf(uvals[k].numerator) / uvals[k].denominator * delta * Q)) for k in range(len(Evals))]
    return Ei, Fi

def verify50(Evals, uvals, delta, a):
    aE = sum(ai * e for ai, e in zip(a, Evals))
    af = aE + delta * sum(ai * mp.mpf(u.numerator) / u.denominator for ai, u in zip(a, uvals))
    return aE < 0 < af

phi = (1 + mp.sqrt(5)) / 2
th = mp.findroot(lambda t: t ** 3 - t - 1, 1.3247)
ps = mp.findroot(lambda t: t ** 4 - t - 1, 1.2207)

def norm_kappa(minpoly_coeffs, root, deg):
    """kappa = 1 / prod_{sigma != id} sum_{k<deg} |sigma root|^k."""
    roots = mp.polyroots(minpoly_coeffs, maxsteps=200, extraprec=200)
    others = [z for z in roots if abs(z - root) > mp.mpf(10) ** -30]
    assert len(others) == deg - 1
    prod = mp.mpf(1)
    for z in others: prod *= sum(abs(z) ** k for k in range(deg))
    return 1 / prod

k3 = norm_kappa([1, 0, -1, -1], th, 3)
k4 = norm_kappa([1, 0, 0, -1, -1], ps, 4)
k2_A1 = 1 / (3 + 1 / phi)            # m = a1 + 2 a3, n = a2  (|m| <= 3H)
k2_A2 = 1 / (4 + 2 / phi)            # m = a1 + 2 a3 + a4, n = a2 + a4  (|m| <= 4H, |n| <= 2H)

# ---------------------------------------------------------------- very well approximable number xL
def cf_value(cf):
    p0, q0, p1, q1 = 1, 0, cf[0], 1
    convs = [(cf[0], 1)]
    for a in cf[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        convs.append((p1, q1))
    return F(p1, q1), convs
cfL = [0, 2]
while True:
    _, cv = cf_value(cfL)
    if cv[-1][1] > 10 ** 220: break
    cfL.append(cv[-1][1] ** 2)
xL, convL = cf_value(cfL)

# ================================================================ H7a intermediate ranks
print("== H7a intermediate ranks ==")
U = lambda *v: [F(x) for x in v]
cases = {
    "A1 d=4 r=2 K-blind":   ([mp.mpf(1), phi, mp.mpf(2)], U(F(3, 10), F(-7, 10), F(3, 5)), 2, k2_A1, np.arange(2.0, 6.01, 0.5), (0.40, 0.60)),
    "A2 d=5 r=2 K-visible": ([mp.mpf(1), phi, mp.mpf(2), 1 + phi], U(F(3, 10), F(-7, 10), F(9, 20), F(1, 5)), 2, k2_A2, np.arange(1.5, 4.01, 0.5), (0.35, 0.65)),
    "A3 d=5 r=3 K-visible": ([mp.mpf(1), th, th ** 2, 1 + th], U(F(3, 10), F(-7, 10), F(9, 20), F(1, 5)), 3, k3 / 4, np.arange(2.0, 6.01, 0.5), (0.25, 0.42)),
    "A4 d=5 r=3 K-blind":   ([mp.mpf(1), th, th ** 2, 1 + th], U(F(3, 10), F(-7, 10), F(9, 20), F(-2, 5)), 3, k3 / 4, np.arange(2.0, 6.01, 0.5), (0.25, 0.42)),
    "A5 d=5 r=4 full":      ([mp.mpf(1), ps, ps ** 2, ps ** 3], U(F(3, 10), F(-7, 10), F(9, 20), F(1, 5)), 4, k4, np.arange(2.0, 8.01, 0.5), (0.18, 0.32)),
}
okA = True; slopes = {}
for name, (Ev, uv, r, kap, xs, (lo_s, hi_s)) in cases.items():
    u1 = float(sum(abs(x) for x in uv)); ns, ds, okstab, okver, oklb = [], [], True, True, True
    for x in xs:
        delta = mp.mpf(10) ** (-mp.mpf(x))
        E40, F40 = surrogate(Ev, uv, delta, 40); n40, w40 = scan(E40, F40)
        E43, F43 = surrogate(Ev, uv, delta, 43); n43, _ = scan(E43, F43, B0=n40)
        okstab &= n40 == n43; okver &= verify50(Ev, uv, delta, w40)
        lb = float((kap / (delta * u1)) ** (mp.mpf(1) / r)); oklb &= n40 > lb
        ns.append(n40); ds.append(float(delta))
    s = np.polyfit(np.log(1 / np.array(ds)), np.log(ns), 1)[0]; slopes[name] = s
    ok = lo_s <= s <= hi_s and okstab and okver and oklb
    okA &= ok
    print(f"   {name}: slope {s:.3f} in [{lo_s},{hi_s}]  n*={ns}  stable={okstab} verified={okver} above-LB={oklb}")
# A6: universality of the K-visible upper bound
xLm = mp.mpf(xL.numerator) / xL.denominator
Ev6 = [mp.mpf(1), 1 + xLm, mp.mpf(2)]; uv6 = U(F(3, 10), F(-7, 10), F(9, 20))
exps6, ns6 = [], []
okA6 = True
for x in np.arange(2.0, 7.01, 0.25):
    delta = mp.mpf(10) ** (-mp.mpf(x))
    E40, F40 = surrogate(Ev6, uv6, delta, 40); n40, w40 = scan(E40, F40)
    E43, F43 = surrogate(Ev6, uv6, delta, 43); n43, _ = scan(E43, F43, B0=n40)
    okA6 &= (n40 == n43) and verify50(Ev6, uv6, delta, w40)
    ns6.append(n40); exps6.append(math.log(n40) / math.log(10 ** x))
okA6 &= max(exps6) <= 0.60
print(f"   A6 d=4 r=2 very-well-approximable, K-visible: local exponents in [{min(exps6):.3f}, {max(exps6):.3f}]  n*={ns6}")
check("H7a [exact surrogate] intermediate ranks: n* ~ delta^(-1/r) for K-visible and K-blind u'; K-visible upper bound needs no Diophantine condition",
      okA and okA6, f"slopes { {k.split()[0]: round(v, 3) for k, v in slopes.items()} }; A6 max exponent {max(exps6):.3f}")

# ================================================================ H7b almost every spectrum
print("== H7b almost every spectrum ==")
rng = np.random.default_rng(71)
D = 2 ** 100
def local_exp(x, k):     # delta = 10^-k exactly
    _, m = two_port(x, F(1, 10 ** k)); return math.log(m) / (k * math.log(10)), m
e12 = []; e6 = []
for _ in range(300):
    X = int(rng.integers(0, 2 ** 62)) * (2 ** 38) + int(rng.integers(0, 2 ** 38))
    x = F(D // 4 + X % (D // 2), D)
    e12.append(local_exp(x, 12)[0]); e6.append(local_exp(x, 6)[0])
e12 = np.array(e12); e6 = np.array(e6)
frac12 = np.mean((e12 >= 0.40) & (e12 <= 0.60)); frac6 = np.mean((e6 >= 0.40) & (e6 <= 0.60))
med12 = float(np.median(e12))
# golden control and very-well-approximable oscillation
gold_cf = [0] + [1] * 400
xg, _ = cf_value(gold_cf)
ks = np.arange(3.0, 70.01, 0.25)
def local_exp_real(x, kk):  # delta = 10^-kk with kk possibly fractional: use rational approx of 10^-kk
    dl = F(mp.nstr(mp.mpf(10) ** (-mp.mpf(kk)), 40))
    _, m = two_port(x, dl); return math.log(m) / (kk * math.log(10))
eg = [local_exp_real(xg, kk) for kk in ks]
eL = [local_exp_real(xL, kk) for kk in ks]
okB = frac12 >= 0.85 and 0.46 <= med12 <= 0.54 and min(eg) >= 0.42 and max(eg) <= 0.58 and max(eL) >= 0.65 and min(eL) <= 0.35
check("H7b [exact] almost every gap ratio: exponent -> 1/2; golden stays at 1/2; very well approximable ratios oscillate",
      okB, f"random x: {100*frac12:.1f}% in [0.4,0.6] at 1e-12 (vs {100*frac6:.1f}% at 1e-6), median {med12:.3f}; "
           f"golden in [{min(eg):.3f},{max(eg):.3f}]; xL oscillates in [{min(eL):.3f},{max(eL):.3f}]")

# ================================================================ H7c near resonance
print("== H7c near resonance (Proposition 6.8a) ==")
okC, nchk = True, 0
p, q = 1, 2
for etaf in [mp.sqrt(2) - 1, (mp.sqrt(2) - 1) / 10]:
    eta = F(int(mp.nint(etaf / 100 * D)), D)
    for s in (+1, -1):
        x = F(p, q) + s * eta
        for kk in np.arange(0.25, 9.01, 0.25):
            dl = F(mp.nstr(mp.mpf(10) ** (-mp.mpf(kk)), 40)); w = x * dl
            kf, n = window_frac(x, x + w)
            n = max(kf, n)
            if s > 0:
                okC &= F(n) > 1 / (q * (eta + w)); nchk += 1
                if w >= q * q * eta * (eta + w):
                    okC &= F(n) <= 1 / (q * (eta + w)) + q; nchk += 1
            else:
                if w > eta:
                    okC &= n == max(p, q); nchk += 1
                elif q * q * eta * eta <= w:
                    okC &= 1 / (q * eta) < F(n) <= 1 / (q * eta) + q; nchk += 1
check("H7c [exact] near resonance: away side n* = 1/(q(eta+w)) + O(q); toward side plateau 1/(q eta) then collapse to q",
      okC, f"{nchk} exact inequalities")

# ================================================================ H7d harmonic modes: order of the engine
print("== H7d harmonic modes: order of the engine ==")
okD, nD = True, 0
rr = [F(1, 2), F(1, 3), F(2, 3), F(2, 5), F(3, 4), F(3, 5), F(1, 4), F(4, 5), F(5, 7), F(5, 9)]
L = 10
for trial in range(2000):
    eA, eB = (int(v) for v in rng.integers(1, 6, size=2))
    rA, rB = rr[int(rng.integers(0, len(rr)))], rr[int(rng.integers(0, len(rr)))]
    # A colder: beta_A > beta_B  <=>  fA/eA > fB/eB  <=>  rA^eB < rB^eA
    if not (rA ** eB < rB ** eA): continue
    # Carnot window (eA/eB, fA/fB), fA = -ln rA ; p/q vs fA/fB: sign(p fB - q fA) = sign(ln(rA^q / rB^p))
    below = lambda P, Q: P * eB <= Q * eA
    above = lambda P, Q: rA ** Q >= rB ** P          # p/q >= fA/fB
    k, m = simplest(below, above)
    if max(k, m) > L - 2: continue
    levels = [(nA, nB) for nA in range(L) for nB in range(L)]
    best = None
    Pl = {lv: rA ** lv[0] * rB ** lv[1] for lv in levels}
    for (a1, b1) in levels:
        E1 = a1 * eA + b1 * eB; P1 = Pl[(a1, b1)]
        for (a2, b2) in levels:
            E2 = a2 * eA + b2 * eB
            if E1 < E2 and P1 < Pl[(a2, b2)]:
                o = abs(a1 - a2) + abs(b1 - b2)
                best = o if best is None else min(best, o)
    nD += 1; okD &= best == k + m
    if nD >= 32: break
check("H7d [exact] two harmonic modes: one copy is never passive; least order of a work-extracting exchange = k+m of the simplest fraction",
      okD and nD >= 30, f"{nD} brute-force instances (L={L} levels per mode)")

# ================================================================ H7e platform numbers
print("== H7e platform numbers ==")
x_res = F(1, 2)
x_gold = xg
x_ion = cf_value([0, 1] + [1, 2] * 200)[0]           # 1/sqrt3 = [0; 1, 1, 2, 1, 2, ...]
assert abs(float(x_ion) - 1 / math.sqrt(3)) < 1e-12
eps = F(1, 20); eta_t = eps / (2 * (2 - eps))
x_away, x_tow = F(1, 2) + eta_t, F(1, 2) - eta_t
okE = True
print("   delta     | 1/2 (harm.) | 1/sqrt3 (ions) | 1/phi (golden) | transmon away | transmon toward   [n* = max(k,m); order k+m]")
for kk in [0.5, 1, 1.5, 2, 2.5, 3, 4, 6, 8, 10]:
    dl = F(mp.nstr(mp.mpf(10) ** (-mp.mpf(kk)), 40))
    row = []
    for xx in [x_res, x_ion, x_gold, x_away, x_tow]:
        k, m = two_port(xx, dl); row.append((max(k, m), k + m))
    print(f"   1e-{kk:<4}   " + "  ".join(f"{a:>8} [{b:>8}]" for a, b in row))
    if 2 <= kk <= 10:
        okE &= 0.2 <= row[0][0] / row[2][0] * float(dl) ** 0.5 <= 2
        okE &= 0.1 <= row[1][0] * float(dl) ** 0.5 <= 5
    if 1 <= kk <= 2.5: okE &= row[3][0] <= 41
for dl in [F(3, 100), F(1, 10), F(3, 10)]:
    k, m = two_port(x_tow, dl); okE &= max(k, m) == 2
check("H7e [exact] platform numbers: golden saves ~sqrt(T/dT) over harmonic; ion modes sqrt-scaling; transmon plateau <= 41 / two-copy engine",
      okE, f"transmon eta = {float(eta_t):.5f} -> plateau 1/(2 eta) = {float(1/(2*eta_t)):.1f}")

# ================================================================ H7f echo-yield duality
print("== H7f echo-yield duality ==")
def qrec(alphas, eps_, qmax):
    al = np.array([float(a) for a in alphas])
    for s0 in range(1, qmax + 1, 2_000_000):
        qq = np.arange(s0, min(s0 + 2_000_000, qmax + 1), dtype=np.float64)[:, None]
        fr = qq * al[None, :]; dist = np.abs(fr - np.round(fr)).max(axis=1)
        hit = np.nonzero(dist < eps_)[0]
        if hit.size: return int(qq[hit[0], 0])
    return None
e_s = {}
eps2 = [10.0 ** -k for k in np.arange(1, 6.01, 0.5)]
q2 = [qrec([phi], e, 10 ** 8) for e in eps2]
e_s[2] = np.polyfit(np.log(1 / np.array(eps2)), np.log(q2), 1)[0]
eps3 = [10.0 ** -k for k in np.arange(1, 3.51, 0.25)]
q3 = [qrec([th, th ** 2], e, 10 ** 8) for e in eps3]
e_s[3] = np.polyfit(np.log(1 / np.array(eps3)), np.log(q3), 1)[0]
e_s[1] = 0.0                                      # r = 1: every phase is a multiple of one gap: q_rec = 1
y = {1: 0.996, 2: 0.498, 3: 0.351}                # P6.K6c yield exponents
prods = {r: y[r] * (e_s[r] + 1) for r in (1, 2, 3)}
okF = 0.85 <= e_s[2] <= 1.15 and 1.7 <= e_s[3] <= 2.3 and all(0.85 <= v <= 1.15 for v in prods.values())
print(f"   q_rec golden: {q2}\n   q_rec plastic: {q3}")
check("H7f [exact] echo-yield duality: echo exponent e = r-1, yield exponent y = 1/r, y(e+1) = 1",
      okF, f"e = { {r: round(v, 3) for r, v in e_s.items()} }; y(e+1) = { {r: round(v, 3) for r, v in prods.items()} }")

print(f"\nP7: {sum(res)}/{len(res)} PASS")
