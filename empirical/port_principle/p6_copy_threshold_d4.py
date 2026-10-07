"""
Port Principle — P6: copy thresholds beyond three levels (probe of Open Problem 6.9).
Exact arithmetic for every decision marked [exact]; integer surrogates (exact int64) for irrational spectra,
with witnesses re-verified at 50 digits on the true spectrum.

SETUP. E_0 = 0 < E_1 < E_2 < E_3, f_i = -ln p_i (shifted so f_0 = 0), rho passive, faithful, not Gibbs.
Lemma 6.2: n* = min sum(c+) over c in Z^4, sum c = 0, c.E < 0 < c.f. With a = (c_1, c_2, c_3):
sum(c+) = (|a_1 + a_2 + a_3| + |a_1| + |a_2| + |a_3|) / 2  >=  ||a||_inf.

PRE-REGISTERED FALSIFIERS (written 2026-10-01, before the first run; every branch reportable)

H6  COPY THRESHOLDS BEYOND THREE LEVELS.
    K6a [exact]: the Lemma 6.2 lattice minimum (exact enumeration of c) equals the brute-force exact-ergotropy
         threshold of rho^{(x)n} on >= 40 passive 4-level instances with rational populations (n <= 6).
    K6a' [exact]: the fast integer scan (iterative-deepening box over (a1, a2), exact int64 floor division for the
         a3-interval, cost-optimal a3 = clip(0, lo, hi)) equals exact enumeration on >= 100 instances with rational
         (E, f).
    L6a: any mismatch.

    K6b [exact] TRIPLE REDUCTION. Conjecture TR: n*_4 = min over the four triples {i<j<k} of the Theorem 6.6
         thresholds (equivalently: some minimizing c has support <= 3).
         PRE-REGISTERED EXPECTATION: TR is FALSE. K6b passes iff an exact counterexample exists (n*_4 < TR),
         confirmed by brute-force ergotropy: the 4-level state is active at n*_4 copies while none of its four
         3-level restrictions is. Report the fraction of random instances on which TR holds.
    L6b: TR holds on every instance (then TR becomes a conjecture with evidence, in tension with K6c).

    K6c [exact surrogate] RESONANCE-RANK LAW (d = 4). Near equilibrium f = E + delta*u (beta = 1),
         u = (0, 3/10, -7/10, 9/20). r = rank of the gap module M = Z<E_1, E_2, E_3>. Prediction n* ~ delta^(-1/r):
           r=1  E = (0, 1, 2, 3)                          slope in [0.90, 1.10]   delta = 10^-1.5 .. 10^-3.5
           r=2  E = (0, 1, phi, 2)                        slope in [0.40, 0.60]   delta = 10^-2   .. 10^-6
           r=3  E = (0, 1, theta, theta^2), theta^3=theta+1 (plastic)
                                                          slope in [0.25, 0.42]   delta = 10^-2   .. 10^-8
         and for r=3 the TR value (best triple, each triple has a rank-2 gap module) has slope in [0.35, 0.65],
         so TR fails for all small delta.
         Surrogates: gaps rounded to the 2^-40 grid; n* must be unchanged on the 2^-43 grid (surrogate stability);
         the minimizing witness is re-verified at 50 digits on the true spectrum.
    L6c: any slope outside its window, any surrogate instability, any witness failing 50-digit verification.

    K6d [exact] THEOREM BOUNDS. If every NONZERO value a.E' (a in Z^3, ||a||_inf <= H) has |a.E'| >= kappa H^-(r-1),
         then n* > (kappa / (delta ||u'||_1))^(1/r)   [u' = (u1,u2,u3); proof: n* >= ||a||_inf =: H and
         kappa H^-(r-1) <= |a.E'| < delta a.u' <= delta ||u'||_1 H].
           r=1: kappa = 1.
           r=2: kappa = 1/(3 + 1/phi)            (norm form m^2 + m n - n^2 of Z[phi], m = a1 + 2 a3, n = a2).
           r=3: kappa = 1/(1 + theta^-1/2 + theta^-1)^2   (norm of Z[theta]; |theta'|^2 = 1/theta).
         Checks: (i) the kappa inequalities hold on all a with ||a||_inf <= 25 (integer norm form != 0, exact sympy
         for r=3; 50-digit values); (ii) every n* of K6c respects its lower bound; (iii) boundedness:
         max/min of n* delta^(1/r) over the delta range <= 12 for each r.
    L6d: any violation.

    K6e [exact] THREE-RESERVOIR ENGINE. Three Gibbs qubit ports, gaps eps_j, Boltzmann ratios r_j = p_j(1)/p_j(0).
         Prediction: n* = min ||m||_inf over m in Z^3 (net excitations per port) with m.eps < 0 < m.phi,
         phi_j = -ln r_j. Checked against brute-force exact ergotropy of the 8-level joint state (n <= 4) on
         >= 20 instances. Near equilibrium beta_j = 1 + delta v_j, v = (1, 0, -1):
           eps = (1, theta, theta^2): slope in [0.25, 0.42], delta = 10^-2 .. 10^-8;
           eps = (1, 2, 3):           slope in [0.90, 1.10], delta = 10^-1.5 .. 10^-3.5.
    L6e: any mismatch or slope outside its window.
"""
import sys
from fractions import Fraction as F
from itertools import product, combinations
import math
import numpy as np
import sympy as sp
import mpmath as mp

sys.stdout.reconfigure(encoding="utf-8")
mp.mp.dps = 50
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

# ---------------------------------------------------------------- exact tools
def compositions(n, k):
    """k positive parts summing to n."""
    if k == 1:
        yield (n,); return
    for first in range(1, n - k + 2):
        for rest in compositions(n - first, k - 1):
            yield (first,) + rest

def cvecs(d, n):
    """all c in Z^d with sum c = 0 and sum(c+) = n."""
    idx = range(d)
    for kp in range(1, d):
        for S in combinations(idx, kp):
            rest = [i for i in idx if i not in S]
            for kn in range(1, len(rest) + 1):
                for T in combinations(rest, kn):
                    for P in compositions(n, kp):
                        for N in compositions(n, kn):
                            c = [0] * d
                            for i, x in zip(S, P): c[i] = x
                            for i, x in zip(T, N): c[i] = -x
                            yield tuple(c)

def violates(c, E, P):
    """c.E < 0 < c.f with f = -ln p  <=>  c.E < 0 and prod p_i^{c_i} < 1 (exact)."""
    if sum(ci * Ei for ci, Ei in zip(c, E)) >= 0: return False
    num, den = F(1), F(1)
    for ci, pi in zip(c, P):
        if ci > 0: num *= pi ** ci
        elif ci < 0: den *= pi ** (-ci)
    return num < den

def lattice_enum(E, P, nmax, maxsupp=None):
    for n in range(1, nmax + 1):
        for c in cvecs(len(E), n):
            if maxsupp is not None and sum(1 for x in c if x) > maxsupp: continue
            if violates(c, E, P): return n, c
    return None, None

def ergo_pos(levels):
    Es = sorted(E for E, _ in levels); ps = sorted((p for _, p in levels), reverse=True)
    return sum(p * E for E, p in levels) - sum(p * E for p, E in zip(ps, Es)) > 0

def brute(levels, nmax):
    for n in range(1, nmax + 1):
        lv = []
        for cfg in product(levels, repeat=n):
            e = sum(x[0] for x in cfg); p = F(1)
            for x in cfg: p *= x[1]
            lv.append((e, p))
        if ergo_pos(lv): return n
    return None

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

def triple_threshold_int(E, Fv, i, j, k):
    """Theorem 6.6 on levels i<j<k with exact integer data: denominator of the simplest fraction strictly between
    rE = (E_j-E_i)/(E_k-E_i) and rf = (f_j-f_i)/(f_k-f_i). None if rE == rf."""
    eN, eD = E[j] - E[i], E[k] - E[i]
    fN, fD = Fv[j] - Fv[i], Fv[k] - Fv[i]
    s = eN * fD - fN * eD                       # sign(rE - rf)
    if s == 0: return None
    cE = lambda p, q: p * eD - q * eN           # sign(p/q - rE)
    cF = lambda p, q: p * fD - q * fN           # sign(p/q - rf)
    lo, hi = (cF, cE) if s > 0 else (cE, cF)
    p, q = simplest(lambda a, b: lo(a, b) <= 0, lambda a, b: hi(a, b) >= 0)
    return q

# ---------------------------------------------------------------- fast exact integer scan
BIG = np.int64(2 ** 62)
def scan(Ev, Fv, cost="N", chunk=64):
    """Ev = (E1, E2, E3), Fv = (f1, f2, f3): python ints (scaled), E3 > 0, f3 > 0.
    Minimizes cost over a in Z^3 with a.E < 0 < a.F. cost 'N' = (|sum a| + ||a||_1)/2 ; 'inf' = ||a||_inf.
    Iterative deepening: a box of radius B over (a1, a2) is complete once the best cost found is <= B."""
    E1, E2, E3 = (np.int64(x) for x in Ev); F1, F2, F3 = (np.int64(x) for x in Fv)
    B = 4
    while True:
        assert 3 * (B + 1) * max(abs(int(x)) for x in list(Ev) + list(Fv)) < 2 ** 62, "int64 overflow risk"
        best, wit = int(BIG), None
        a2 = np.arange(-B, B + 1, dtype=np.int64)[None, :]
        for s0 in range(-B, B + 1, chunk):
            a1 = np.arange(s0, min(s0 + chunk, B + 1), dtype=np.int64)[:, None]
            R = -(a1 * E1 + a2 * E2); hi = (R - 1) // E3          # a3*E3 < R
            S = -(a1 * F1 + a2 * F2); lo = S // F3 + 1            # a3*F3 > S
            ok = lo <= hi
            a3 = np.clip(0, lo, hi)
            if cost == "N":
                c = (np.abs(a1 + a2 + a3) + np.abs(a1) + np.abs(a2) + np.abs(a3)) // 2
            else:
                c = np.maximum(np.maximum(np.abs(a1), np.abs(a2)), np.abs(a3))
            c = np.where(ok, c, BIG)
            ix = np.unravel_index(np.argmin(c), c.shape)
            if c[ix] < best:
                best = int(c[ix]); wit = (int(a1[ix[0], 0]), int(a2[0, ix[1]]), int(a3[ix]))
        if best <= B: return best, wit
        B = best if best < int(BIG) else 2 * B

# ================================================================ K6a / K6a'
print("== H6 copy thresholds beyond three levels (d = 4) ==")
rng = np.random.default_rng(61)
ratios = [F(1, 2), F(2, 3), F(3, 4), F(3, 5), F(4, 5), F(5, 7), F(2, 5), F(1, 3), F(5, 6), F(7, 9), F(4, 7), F(8, 9)]
def rand_instance():
    e = sorted(rng.choice(np.arange(1, 9), size=3, replace=False).tolist())
    E = [0] + e
    r = [ratios[i] for i in rng.integers(0, len(ratios), size=3)]
    P = [F(1), r[0], r[0] * r[1], r[0] * r[1] * r[2]]
    return E, P
okA, nA, inst_A = True, 0, []
while nA < 45:
    E, P = rand_instance()
    nl, c = lattice_enum(E, P, 6)
    lv = list(zip(E, P))
    nb = brute(lv, 6)
    if nl is None and nb is None: continue          # Gibbs or threshold > 6: uninformative
    nA += 1; okA &= (nl == nb); inst_A.append((E, P, nl))
check("H6.K6a [exact] Lemma 6.2 lattice minimum == brute-force ergotropy threshold (d=4)", okA and nA >= 40,
      f"{nA} instances (n<=6); thresholds seen: {sorted(set(x[2] for x in inst_A))}")

okA2, nA2 = True, 0
while nA2 < 120:
    e = sorted(rng.choice(np.arange(1, 13), size=3, replace=False).tolist()); E = [0] + e
    D = int(rng.integers(2, 9))
    fv = sorted(rng.choice(np.arange(1, 13 * D), size=3, replace=False).tolist()); f = [0] + fv   # f/D, increasing
    if any(E[i] * f[j] == E[j] * f[i] for i in range(1, 4) for j in range(i + 1, 4)) and \
       all(E[i] * f[3] == E[3] * f[i] for i in range(1, 4)):
        continue                                     # Gibbs
    # exact enumeration with linear f (f.c > 0 exactly)
    nl = None
    for n in range(1, 25):
        for c in cvecs(4, n):
            if sum(ci * Ei for ci, Ei in zip(c, E)) < 0 < sum(ci * fi for ci, fi in zip(c, f)):
                nl = n; break
        if nl is not None: break
    if nl is None: continue
    ns, _ = scan(E[1:], f[1:])
    nA2 += 1; okA2 &= (ns == nl)
check("H6.K6a' [exact] fast integer scan == exact enumeration", okA2 and nA2 >= 100, f"{nA2} instances")

# ================================================================ K6b triple reduction
TRhold, TRtot, cex = 0, 0, []
for trial in range(400):
    E, P = rand_instance()
    nl, c = lattice_enum(E, P, 9)
    if nl is None: continue
    nt, ct = lattice_enum(E, P, 9, maxsupp=3)
    TRtot += 1
    if nt == nl: TRhold += 1
    else: cex.append((E, P, nl, c, nt))
# hand-built candidate from the gap analysis: gaps g=(2,1,1), h ∝ (1,1,2), c=(1,-1,-1,1)
cex_hand = ([0, 2, 3, 4], [F(1), F(1, 2), F(1, 4), F(1, 16)])
nl_h, c_h = lattice_enum(*cex_hand, 9); nt_h, _ = lattice_enum(*cex_hand, 9, maxsupp=3)
def confirm_cex(E, P, n4):
    lv = list(zip(E, P))
    if brute(lv, n4) != n4: return False
    for tri in combinations(range(4), 3):
        sub = [lv[i] for i in tri]
        if brute(sub, n4) is not None: return False   # some 3-level restriction already active by n4
    return True
conf = [confirm_cex(E, P, n4) for (E, P, n4, _, _) in cex[:6]]
hand_ok = nl_h is not None and (nt_h is None or nt_h > nl_h) and confirm_cex(*cex_hand, nl_h)
check("H6.K6b [exact] triple reduction FAILS: a 4-level state activates before all of its 3-level restrictions",
      (len(cex) > 0 and all(conf)) or hand_ok,
      f"TR held on {TRhold}/{TRtot} random instances; counterexamples {len(cex)} (brute-confirmed {sum(conf)}/{len(conf)}); "
      f"hand case E=(0,2,3,4), p∝(1,1/2,1/4,1/16): n*4={nl_h} via c={c_h}, TR={nt_h}")
for (E, P, n4, c, nt) in cex[:3]:
    print(f"      e.g. E={E}, p∝{[str(x) for x in P]}: n*_4={n4} via c={c} (support {sum(1 for x in c if x)}), TR={nt}")

# ================================================================ K6c resonance-rank law
phi_m = (1 + mp.sqrt(5)) / 2
theta_m = mp.findroot(lambda t: t ** 3 - t - 1, 1.3247)
u = [F(0), F(3, 10), F(-7, 10), F(9, 20)]; u1norm = float(sum(abs(x) for x in u[1:]))
spectra = {
    1: ([mp.mpf(0), mp.mpf(1), mp.mpf(2), mp.mpf(3)], np.arange(1.5, 3.51, 0.5)),
    2: ([mp.mpf(0), mp.mpf(1), phi_m, mp.mpf(2)], np.arange(2.0, 6.01, 0.5)),
    3: ([mp.mpf(0), mp.mpf(1), theta_m, theta_m ** 2], np.arange(2.0, 8.01, 0.5)),
}
def surrogate(Evals, uvals, delta, qbits):
    Q = mp.mpf(2) ** qbits
    Ei = [int(mp.nint(x * Q)) for x in Evals[1:]]
    Fi = [Ei[k] + int(mp.nint(mp.mpf(uvals[k + 1].numerator) / uvals[k + 1].denominator * delta * Q)) for k in range(3)]
    return Ei, Fi
def verify50(Evals, uvals, delta, a, cost="N"):
    aE = sum(a[k] * Evals[k + 1] for k in range(3))
    af = aE + delta * sum(a[k] * mp.mpf(uvals[k + 1].numerator) / uvals[k + 1].denominator for k in range(3))
    return aE < 0 < af
kap = {1: mp.mpf(1), 2: 1 / (3 + 1 / phi_m), 3: 1 / (1 + theta_m ** mp.mpf(-0.5) + 1 / theta_m) ** 2}
slopes, results = {}, {}
okstab, okver, okLB, okbd = True, True, True, True
for r, (Ev, xs) in spectra.items():
    ns, ds, trs = [], [], []
    for x in xs:
        delta = mp.mpf(10) ** (-mp.mpf(x))
        E40, F40 = surrogate(Ev, u, delta, 40); n40, w40 = scan(E40, F40)
        E43, F43 = surrogate(Ev, u, delta, 43); n43, _ = scan(E43, F43)
        okstab &= (n40 == n43)
        okver &= verify50(Ev, u, delta, w40)
        lb = float((kap[r] / (delta * u1norm)) ** (mp.mpf(1) / r))
        okLB &= n40 > lb
        ns.append(n40); ds.append(float(delta))
        if r == 3:
            Eall, Fall = [0] + E40, [0] + F40
            tr = min(t for t in (triple_threshold_int(Eall, Fall, *tri) for tri in combinations(range(4), 3)) if t)
            trs.append(tr)
        supp = sum(1 for v in list(w40) + [-sum(w40)] if v)
        print(f"   r={r} delta=1e-{x:.1f}: n*={n40:>7}  witness a={w40} (support {supp}/4)  lower bound {lb:9.1f}"
              + (f"  TR={trs[-1]}" if r == 3 else ""))
    s = np.polyfit(np.log(1 / np.array(ds)), np.log(ns), 1)[0]
    slopes[r] = s
    scaled = np.array(ns) * np.array(ds) ** (1 / r)
    okbd &= scaled.max() / scaled.min() <= 12
    results[r] = (ns, ds, trs)
    if r == 3:
        slopes["TR"] = np.polyfit(np.log(1 / np.array(ds)), np.log(trs), 1)[0]
okslope = (0.90 <= slopes[1] <= 1.10 and 0.40 <= slopes[2] <= 0.60 and 0.25 <= slopes[3] <= 0.42
           and 0.35 <= slopes["TR"] <= 0.65)
check("H6.K6c [exact surrogate] resonance-rank law n* ~ delta^(-1/r) for d=4; best triple stays at rank 2",
      okslope and okstab and okver,
      f"slopes r=1:{slopes[1]:.3f} r=2:{slopes[2]:.3f} r=3:{slopes[3]:.3f} TR(r=3):{slopes['TR']:.3f}; "
      f"surrogate-stable={okstab}; 50-digit witnesses={okver}")

# ================================================================ K6d bounds
okk = True
th = sp.Symbol('t'); minpoly = th ** 3 - th - 1
H = 25
for a in product(range(-H, H + 1), repeat=3):
    if a == (0, 0, 0): continue
    Hn = max(abs(v) for v in a)
    # r=1
    v1 = a[0] + 2 * a[1] + 3 * a[2]
    if v1 != 0: okk &= abs(v1) >= 1
    # r=2: m + n phi with m = a1 + 2 a3, n = a2 ; norm m^2 + m n - n^2
    m_, n_ = a[0] + 2 * a[2], a[1]
    if (m_, n_) != (0, 0):
        okk &= (m_ * m_ + m_ * n_ - n_ * n_) != 0
        okk &= abs(m_ + n_ * phi_m) >= kap[2] / Hn
    # r=3: a1 + a2 theta + a3 theta^2, Z[theta]-norm via resultant (integer, must be nonzero)
    if abs(a[0]) + abs(a[1]) + abs(a[2]) <= 12:          # exact resultant on a sub-box (sympy is slow)
        nrm = sp.resultant(minpoly, a[0] + a[1] * th + a[2] * th ** 2, th)
        okk &= nrm != 0
    okk &= abs(a[0] + a[1] * theta_m + a[2] * theta_m ** 2) >= kap[3] / Hn ** 2
check("H6.K6d [exact] theorem bounds: kappa inequalities on ||a||<=25; every n* above its lower bound; n* delta^(1/r) bounded",
      okk and okLB and okbd, f"kappa={[float(kap[r]) for r in (1, 2, 3)]}; lower bounds respected={okLB}; bounded={okbd}")

# ================================================================ K6e three-reservoir engine
def port_lattice(eps, rr, nmax):
    for n in range(1, nmax + 1):
        for m in product(range(-n, n + 1), repeat=3):
            if max(abs(v) for v in m) != n: continue
            if sum(mi * ei for mi, ei in zip(m, eps)) >= 0: continue
            num, den = F(1), F(1)
            for mi, ri in zip(m, rr):
                if mi > 0: num *= ri ** mi
                elif mi < 0: den *= ri ** (-mi)
            if num < den: return n
    return None
okE, nE = True, 0
rrs = [F(1, 2), F(1, 3), F(2, 3), F(2, 5), F(3, 4), F(3, 5), F(1, 4), F(4, 5)]
for trial in range(300):
    eps = sorted(rng.choice(np.arange(1, 6), size=3, replace=True).tolist())
    rr = [rrs[i] for i in rng.integers(0, len(rrs), size=3)]
    lv = []
    for b in product((0, 1), repeat=3):
        e = sum(bi * ei for bi, ei in zip(b, eps)); p = F(1)
        for bi, ri in zip(b, rr): p *= ri if bi else 1
        lv.append((e, p))
    nl = port_lattice(eps, rr, 4); nb = brute(lv, 4)
    if nl is None and nb is None: continue
    nE += 1; okE &= (nl == nb)
    if nE >= 24: break
slE = {}
for name, epsv, xs in [("plastic", [mp.mpf(1), theta_m, theta_m ** 2], np.arange(2.0, 8.01, 0.5)),
                       ("resonant", [mp.mpf(1), mp.mpf(2), mp.mpf(3)], np.arange(1.5, 3.51, 0.5))]:
    ns, ds = [], []
    for x in xs:
        delta = mp.mpf(10) ** (-mp.mpf(x)); Q = mp.mpf(2) ** 40
        v = [1, 0, -1]
        Ei = [int(mp.nint(e * Q)) for e in epsv]
        Fi = [int(mp.nint(e * (1 + delta * vj) * Q)) for e, vj in zip(epsv, v)]
        n_, w_ = scan(Ei, Fi, cost="inf")
        ns.append(n_); ds.append(float(delta))
    slE[name] = np.polyfit(np.log(1 / np.array(ds)), np.log(ns), 1)[0]
    print(f"   three-port {name}: n* = {ns}")
check("H6.K6e [exact] three-reservoir engine: n* = min ||m||_inf (Carnot cone in Z^3); slopes 1/3 (plastic) vs 1 (resonant)",
      okE and nE >= 20 and 0.25 <= slE["plastic"] <= 0.42 and 0.90 <= slE["resonant"] <= 1.10,
      f"{nE} brute-force instances (n<=4); slopes plastic={slE['plastic']:.3f} resonant={slE['resonant']:.3f}")

print(f"\nP6: {sum(res)}/{len(res)} PASS")
