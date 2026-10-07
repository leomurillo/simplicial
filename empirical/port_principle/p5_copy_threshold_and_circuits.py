"""

Port Principle — P5: the copy threshold (arithmetic of the copy lift) and the circuit reading of Petz metrics.
Exact arithmetic for every decision marked [exact]; floats only in labelled [witness] checks.

PRE-REGISTERED FALSIFIERS (written before the first run; every branch reportable)

SPLIT NOTE (2026-09-29): split verbatim from p5_headline_candidates.py when v3 of PortPrinciple.md was
written. Falsifier text, code, and run logs are preserved unchanged; only this header was added.

H2  WHEN DO COPIES BECOME EXPLOITABLE? (Farey law for the copy lift.)
    K2a [exact]: for passive 3-level states (E0<E1<E2), the first copy number at which work is
         extractable equals the HEIGHT (max(num,den)) of the Stern-Brocot simplest fraction strictly
         between the energy ratio E1/E2 and the entropy ratio f1/f2 (f = -ln p + const).
         Checked against brute-force exact ergotropy for n <= 7 on 40 instances.
    K2b [exact]: two Gibbs qubit-ports (gaps eA, eB; unequal temperatures): the smallest heat engine
         (first n with joint work) = height of the simplest fraction strictly between eA/eB and
         fA/fB, against brute force n <= 6 on 30 instances.
    K2c [exact number theory]: near equilibrium (T ratio 1+delta), n* grows like delta^-1 for a
         resonant gap ratio (1/2) but like delta^-1/2 for the golden ratio: fitted log-log slopes
         in [0.95,1.05] and [0.35,0.65] over delta = 1e-2..1e-10.
    L2: any mismatch; or slopes outside the windows.
H3  QUANTUM FISHER METRICS ARE RESISTOR-INDUCTOR CIRCUITS; PETZ SYMMETRY IS DETAILED BALANCE.
    K3a [exact]: filter w_f(x) = (e^{2x}-1)/f(e^{2x}) is odd in x  <=>  f(t) = t f(1/t) (Petz symmetry).
    K3b [exact]: RL realizations: SLD = series(R=1/2, L=1/2); RLD = parallel(R=2, L=2);
         sqrt(t) = (1/pi) int_0^oo t lam^{-1/2}/(lam+t) dlam (continuum of parallel RL cells);
         WY = series(1/4, 1/4) + (1/2) sqrt-element; KM = int_0^1 t^s ds; all self-dual under R<->L.
    K3c [witness]: the quadratic mean f = sqrt((1+t^2)/2) is symmetric (odd filter) but NOT an RL
         impedance (branch points at +-i): it fails operator monotonicity (2x2 witness) and
         VIOLATES data processing for some channel, while SLD, WY, KM, RLD never do on the same trials.
    L3: any fails.

ADDITIONAL PRE-REGISTERED CHECKS (added 2026-09-29 for v3 of PortPrinciple.md, before their first run)
    K2d [exact]: on 400 deterministic open intervals with rational endpoints in (0,3), the Stern-Brocot
         simplest fraction has BOTH the least denominator and the least numerator of all fractions in the
         interval (so it also minimizes max(num, den)).
    K2e [exact]: Carnot window. For eA, eB > 0, betaA > betaB (A colder) and every k/m on a grid:
         eA/eB < k/m < (betaA/betaB)(eA/eB)  <=>  0 < eta < eta_C, with eta = 1 - m eA/(k eB),
         eta_C = 1 - betaB/betaA.
    K2f [exact]: (i) golden gaps: n* = F_n with n the least EVEN index such that phi^{2n-1} > sqrt5/delta + 1/phi,
         for delta = 10^-2 .. 10^-14; (ii) resonant x = p/q in {1/2,1/3,2/3,2/5,3/7}: n* > 1/(p delta), and
         for x = 1/2, n* = least odd integer > 1/delta; (iii) badly approximable gaps with partial quotients
         <= A: n* <= (A+1)^2 / sqrt(x delta), checked for sqrt2 - 1 (A = 2) and the golden ratio (A = 1).
    K3d [exact]: the exchange Z(s) -> s Z(1/s) maps a resistor a to an inductor a, an inductor b to a resistor
         b, and the parallel cell (1+lam)s/(lam+s) to the cell with parameter 1/lam; every cell equals 1 at
         s = 1 (so f(1) = 1 iff the cell measure is a probability measure); the sqrt-element's cell density
         lam^{-1/2}/(pi(1+lam)) has mass 1, is invariant under lam -> 1/lam, and reproduces sqrt(s).
    L (each): any failure is reported and retained.
    K3e [exact] (added 2026-09-29 after a flaw was found in the K3c witness: its A carried a +1e-9 I
         regularization that made B - A marginally NON-PSD): A = [[1,1],[1,1]], B = [[2,1],[1,1]] give
         B - A = diag(1,0) >= 0 exactly, while f(B) - f(A) for the quadratic mean f(t) = sqrt((1+t^2)/2)
         has negative determinant (exact sympy sign), i.e. f is not operator monotone.
"""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

# ================================================================ H2
print("== H2 Farey law for copy thresholds and the smallest heat engine ==")
def simplest(below_lo, above_hi):
    """Stern-Brocot simplest fraction p/q in (lo, hi), with exact predicates.
    below_lo(p,q): p/q <= lo ; above_hi(p,q): p/q >= hi. Run-length jumps."""
    lp, lq, rp, rq = 0, 1, 1, 0
    while True:
        mp, mq = lp + rp, lq + rq
        if below_lo(mp, mq):
            k = 1
            while below_lo(lp + 2 * k * rp, lq + 2 * k * rq): k *= 2
            lo_k, hi_k = k, 2 * k
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if below_lo(lp + mid * rp, lq + mid * rq): lo_k = mid
                else: hi_k = mid
            lp, lq = lp + lo_k * rp, lq + lo_k * rq
        elif above_hi(mp, mq):
            k = 1
            while above_hi(rp + 2 * k * lp, rq + 2 * k * lq): k *= 2
            lo_k, hi_k = k, 2 * k
            while hi_k - lo_k > 1:
                mid = (lo_k + hi_k) // 2
                if above_hi(rp + mid * lp, rq + mid * lq): lo_k = mid
                else: hi_k = mid
            rp, rq = rp + lo_k * lp, rq + lo_k * lq
        else:
            return mp, mq
def ergo(levels):
    Es = sorted(E for E, _ in levels); ps = sorted((p for _, p in levels), reverse=True)
    return sum(p * E for E, p in levels) - sum(p * E for p, E in zip(ps, Es))
def copies(levels, n):
    out = []
    for c in product(levels, repeat=n):
        E = sum(x[0] for x in c); p = F(1)
        for x in c: p *= x[1]
        out.append((E, p))
    return out
def brute(levels, nmax):
    for n in range(1, nmax + 1):
        if ergo(copies(levels, n)) > 0: return n
    return None
def farey3(E1, E2, p0, p1, p2):
    A, B = p0 / p1, p0 / p2                         # f1 = ln A, f2 = ln B
    cmpE = lambda p, q: (p * E2 > q * E1) - (p * E2 < q * E1)            # sign(p/q - E1/E2)
    def cmpF(p, q):                                 # sign(p/q - f1/f2) = sign(p ln B - q ln A)
        lhs, rhs = B ** p, A ** q
        return (lhs > rhs) - (lhs < rhs)
    sEF = (B ** E1 > A ** E2) - (B ** E1 < A ** E2)   # sign(E1/E2 - f1/f2)
    if sEF == 0: return None
    lo, hi = (cmpF, cmpE) if sEF > 0 else (cmpE, cmpF)
    p, q = simplest(lambda a, b: lo(a, b) <= 0, lambda a, b: hi(a, b) >= 0)
    return max(p, q)
okA, cases = True, 0
fr = [F(1, 2), F(2, 3), F(3, 4), F(3, 5), F(4, 5), F(5, 7), F(2, 5), F(5, 6), F(7, 9), F(1, 3)]
for i, (E1, E2) in enumerate([(1, 2), (1, 3), (2, 3), (2, 5), (1, 4)]):
    for j in range(8):
        a = fr[(i * 3 + j) % len(fr)]; b = a * fr[(i + 2 * j + 1) % len(fr)]
        Z = 1 + a + b; lv = [(0, 1 / Z), (E1, a / Z), (E2, b / Z)]
        if not ergo(lv) == 0: continue
        nf = farey3(E1, E2, F(1), a, b)
        if nf is None: continue
        nb = brute(lv, 7); cases += 1
        okA &= (nb == nf) if nf <= 7 else (nb is None)
check("H2.K2a [exact] 3-level copy threshold == height of simplest fraction between E1/E2 and f1/f2", okA and cases >= 30,
      f"{cases} instances vs brute force (n<=7)")
okB, casesB = True, 0
rs = [F(1, 2), F(1, 3), F(2, 5), F(1, 4), F(3, 7), F(2, 3)]
for (eA, eB) in [(1, 2), (2, 3), (1, 3), (3, 5), (2, 5)]:
    for (rA, rB) in [(x, y) for x in rs for y in rs if x != y][:6]:
        A = [(0, 1 / (1 + rA)), (eA, rA / (1 + rA))]; B = [(0, 1 / (1 + rB)), (eB, rB / (1 + rB))]
        J = [(ea + eb, pa * pb) for (ea, pa), (eb, pb) in product(A, B)]
        iA, iB = 1 / rA, 1 / rB                       # fA = ln iA, fB = ln iB
        cmpE = lambda p, q: (p * eB > q * eA) - (p * eB < q * eA)          # sign(p/q - eA/eB)
        cmpF = lambda p, q: (iB ** p > iA ** q) - (iB ** p < iA ** q)       # sign(p/q - fA/fB)
        s = (iB ** eA > iA ** eB) - (iB ** eA < iA ** eB)                   # sign(eA/eB - fA/fB)
        if s == 0: continue
        lo, hi = (cmpF, cmpE) if s > 0 else (cmpE, cmpF)
        p, q = simplest(lambda a, b: lo(a, b) <= 0, lambda a, b: hi(a, b) >= 0)
        nf = max(p, q); nb = brute(J, 6); casesB += 1
        okB &= (nb == nf) if nf <= 6 else (nb is None)
check("H2.K2b [exact] smallest two-temperature heat engine == height of simplest fraction between eA/eB and fA/fB", okB and casesB >= 25,
      f"{casesB} instances vs brute force (n<=6)")
def nstar_res(dn):   # window (1/2, (1/2)(1+1/dn))
    return max(simplest(lambda p, q: 2 * p <= q, lambda p, q: 2 * p * dn >= q * (dn + 1)))
def nstar_gold(dn):  # window (x, x(1+1/dn)), x = (sqrt5-1)/2
    below = lambda p, q: (2 * p + q) ** 2 <= 5 * q * q
    above = lambda p, q: (2 * p * dn + q * (dn + 1)) ** 2 >= 5 * q * q * (dn + 1) ** 2
    return max(simplest(below, above))
dns = [10 ** j for j in range(2, 11)]
nr = [nstar_res(dn) for dn in dns]; ng = [nstar_gold(dn) for dn in dns]
sr = np.polyfit(np.log(dns), np.log(nr), 1)[0]; sg = np.polyfit(np.log(dns), np.log(ng), 1)[0]
check("H2.K2c [exact] resonant gaps need ~1/delta copies, golden-ratio gaps ~1/sqrt(delta)",
      0.95 <= sr <= 1.05 and 0.35 <= sg <= 0.65,
      f"slopes resonant={sr:.3f} golden={sg:.3f}; n* at delta=1e-10: resonant={nr[-1]}, golden={ng[-1]}")

# ================================================================ H3
print("== H3 quantum Fisher metrics are RL circuits; Petz symmetry is detailed balance ==")
x, s, lam, tt = sp.symbols('x s lam t', positive=True)
f = sp.Function('f')
w = lambda X: (sp.exp(2 * X) - 1) / f(sp.exp(2 * X))
odd = sp.simplify((w(x) + w(-x)).subs(f(sp.exp(-2 * x)), f(sp.exp(2 * x)) * sp.exp(-2 * x)))
check("H3.K3a [exact] Petz symmetry f(t)=t f(1/t) makes the filter odd (w(-x) = -w(x): emission<->absorption)", odd == 0)
Zser = lambda R, L: R + L * s
Zpar = lambda R, L: 1 / (1 / R + 1 / (L * s))
sqrt_el = sp.simplify(sp.integrate(s * lam ** sp.Rational(-1, 2) / (lam + s), (lam, 0, sp.oo)) / sp.pi)
km_int = sp.simplify(sp.integrate(s ** tt, (tt, 0, 1)))
# RUN LOG (2026-09-29): first run FAILED K3b — sympy returns int_0^1 s^t dt as a Piecewise whose s=1 branch
# is an unresolved 0/0 (checker artifact; generic branch == (s-1)/log s exactly; value 1 at s=1 is the limit).
# Fixed by taking the generic (s != 1) branch.
if isinstance(km_int, sp.Piecewise): km_int = km_int.args[0][0]
self_dual = lambda Z: sp.simplify(s * Z.subs(s, 1 / s) - Z) == 0
okb = (sp.simplify(Zser(sp.Rational(1, 2), sp.Rational(1, 2)) - (1 + s) / 2) == 0
       and sp.simplify(Zpar(2, 2) - 2 * s / (1 + s)) == 0
       and sp.simplify(sqrt_el - sp.sqrt(s)) == 0
       and sp.simplify(Zser(sp.Rational(1, 4), sp.Rational(1, 4)) + sqrt_el / 2 - ((1 + sp.sqrt(s)) / 2) ** 2) == 0
       and sp.simplify(km_int - (s - 1) / sp.log(s)) == 0
       and all(self_dual(Z) for Z in [(1 + s) / 2, 2 * s / (1 + s), ((1 + sp.sqrt(s)) / 2) ** 2, (s - 1) / sp.log(s)]))
check("H3.K3b [exact] RL realizations: SLD=series(1/2,1/2), RLD=parallel(2,2), sqrt=continuum of parallel RL, WY, KM; all R<->L self-dual", okb)
qm = lambda T: np.sqrt((1 + T ** 2) / 2)
def mfun(fn, A):
    ev, V = np.linalg.eigh(A); return V @ np.diag(fn(ev)) @ V.conj().T
A2 = np.array([[1.0, 1.0], [1.0, 1.0]]) + 1e-9 * np.eye(2); B2 = np.array([[2.0, 1.0], [1.0, 1.0]])
not_om = np.linalg.eigvalsh(mfun(qm, B2) - mfun(qm, A2)).min() < -1e-3
fams = {"SLD": lambda T: (1 + T) / 2, "WY": lambda T: ((1 + np.sqrt(T)) / 2) ** 2,
        "KM": lambda T: np.where(np.abs(T - 1) < 1e-12, 1.0, (T - 1) / np.log(np.where(T == 1, 2, T))),
        "RLD": lambda T: 2 * T / (1 + T), "QM": qm}
def metric(fn, rho, X):
    p, U = np.linalg.eigh(rho); Xt = U.conj().T @ X @ U
    P, Q = np.meshgrid(p, p, indexing='ij')
    return float(np.sum(np.abs(Xt) ** 2 / (Q * fn(P / Q))).real)
rng = np.random.default_rng(3)
viol = {k: 0 for k in fams}; worst = {k: 0.0 for k in fams}
for trial in range(6000):
    dd = 3
    G = rng.normal(size=(dd, dd)) + 1j * rng.normal(size=(dd, dd)); rho = G @ G.conj().T; rho /= np.trace(rho).real
    Hh = rng.normal(size=(dd, dd)) + 1j * rng.normal(size=(dd, dd)); X = Hh + Hh.conj().T; X -= np.trace(X) / dd * np.eye(dd)
    Vi = np.linalg.qr(rng.normal(size=(dd * 2, dd)) + 1j * rng.normal(size=(dd * 2, dd)))[0]
    Kr = [Vi[k * dd:(k + 1) * dd, :] for k in range(2)]
    ch = lambda Y: sum(Kk @ Y @ Kk.conj().T for Kk in Kr)
    for k, fn in fams.items():
        r = metric(fn, ch(rho), ch(X)) / metric(fn, rho, X)
        if r > 1 + 1e-9: viol[k] += 1; worst[k] = max(worst[k], r)
check("H3.K3c [witness] quadratic mean: odd filter but not RL -> fails operator monotonicity AND data processing; Petz members never",
      not_om and viol["QM"] > 0 and all(viol[k] == 0 for k in ["SLD", "WY", "KM", "RLD"]),
      f"violations/6000: {viol}; worst QM ratio {worst['QM']:.4f}")
# RUN LOG (2026-09-29): K3c FAILED as pre-registered — 0/6000 violations: random Kraus-rank-2 qutrit channels
# never sample the violating maps. Diagnosis found them: PINCHING (complete dephasing = the port READING)
# and PARTIAL TRACE. Retained; K3c' is POST-DIAGNOSIS (not blind).
def ptrace(Mm): return Mm.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
pin = lambda Y: np.diag(np.diag(Y))
rng2 = np.random.default_rng(5)
mx = {k: 0.0 for k in fams}
for trial in range(8000):
    for dd, chn in [(3, pin), (4, ptrace)]:
        G = rng2.normal(size=(dd, dd)) + 1j * rng2.normal(size=(dd, dd)); rho = G @ G.conj().T; rho /= np.trace(rho).real
        Hh = rng2.normal(size=(dd, dd)) + 1j * rng2.normal(size=(dd, dd)); X = Hh + Hh.conj().T; X -= np.trace(X) / dd * np.eye(dd)
        for k, fn in fams.items():
            mx[k] = max(mx[k], metric(fn, chn(rho), chn(X)) / metric(fn, rho, X))
check("H3.K3c' [witness, post-diagnosis] pinching/partial trace: quadratic mean INCREASES (reading creates 'information'); Petz members never",
      mx["QM"] > 1.05 and all(mx[k] <= 1 + 1e-9 for k in ["SLD", "WY", "KM", "RLD"]),
      f"max ratio: { {k: round(v, 4) for k, v in mx.items()} }")


# ---------------------------------------------------------------- additional checks for v3 (pre-registered above)
print("== K2d-K2f, K3d (added for v3) ==")
cands = set()
for j in range(1, 13):
    for i in range(1, 3 * j):
        for l in range(1, 13):
            for k in range(1, 3 * l):
                lo, hi = F(i, j), F(k, l)
                if lo < hi < 3: cands.add((lo, hi))
cands = sorted(cands)
step = max(1, len(cands) // 400)
cands = cands[::step][:400]
okd = True
for lo, hi in cands:
    p, q = simplest(lambda a, b: a * lo.denominator <= b * lo.numerator, lambda a, b: a * hi.denominator >= b * hi.numerator)
    qm = 1
    while True:
        pl = (lo * qm).numerator // (lo * qm).denominator + 1
        if F(pl, qm) < hi: break
        qm += 1
    pm = 1
    while True:
        qc = (F(pm) / hi).numerator // (F(pm) / hi).denominator + 1
        if F(qc) < F(pm) / lo: break
        pm += 1
    okd &= (q == qm and p == pm)
check("K2d [exact] simplest fraction has the least denominator AND the least numerator (400 intervals)", okd and len(cands) == 400)
oke = True
bet = [F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(5, 2)]
for eA in (1, 2, 3):
    for eB in (1, 2, 3):
        for bA in bet:
            for bB in bet:
                if not bA > bB: continue
                for kk in range(1, 13):
                    for mm in range(1, 13):
                        r = F(kk, mm); inwin = F(eA, eB) < r < (bA / bB) * F(eA, eB)
                        eta = 1 - F(mm * eA, kk * eB); etaC = 1 - bB / bA
                        oke &= (inwin == (0 < eta < etaC))
check("K2e [exact] gear ratio in the window  <=>  0 < efficiency < Carnot", oke)
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
def gold_formula(D):
    n = 2
    while True:
        L = fib(2 * n - 1) + 2 * fib(2 * n - 2) + 1; Rc = 2 * D - fib(2 * n - 1) + 1
        if Rc <= 0 or L * L > 5 * Rc * Rc: return fib(n)
        n += 2
okf = True
for jj in range(2, 15):
    D = 10 ** jj
    okf &= (nstar_gold(D) == gold_formula(D))
for (pp, qq) in [(1, 2), (1, 3), (2, 3), (2, 5), (3, 7)]:
    for jj in range(2, 11):
        D = 10 ** jj
        ns = max(simplest(lambda a, b: a * qq <= pp * b, lambda a, b: a * qq * D >= pp * b * (D + 1)))
        okf &= (ns * pp > D)
        if (pp, qq) == (1, 2): okf &= (ns == D + 1)
for jj in range(2, 13):
    D = 10 ** jj
    below2 = lambda a, b: (a + b) ** 2 <= 2 * b * b
    above2 = lambda a, b: (a * D + b * (D + 1)) ** 2 >= 2 * b * b * (D + 1) ** 2
    n2 = max(simplest(below2, above2))
    okf &= (2 * n2 ** 4 <= (81 * D + n2 ** 2) ** 2)                 # n* <= 9/sqrt(x delta), x = sqrt2-1
    ng_ = nstar_gold(D)
    okf &= (5 * ng_ ** 4 <= (32 * D + ng_ ** 2) ** 2)                # n* <= 4/sqrt(x delta), x = 1/phi
check("K2f [exact] golden n* = F_n (least even n with phi^(2n-1) > sqrt5/delta + 1/phi); resonant n* > 1/(p delta), "
      "x=1/2 exact; badly approximable n* <= (A+1)^2/sqrt(x delta)", okf)
lam_, s_ = sp.symbols('lam s', positive=True)
cell = lambda L: (1 + L) * s_ / (L + s_)
exch = lambda Z: sp.simplify(s_ * Z.subs(s_, 1 / s_))
dens = lam_ ** sp.Rational(-1, 2) / (sp.pi * (1 + lam_))
okk = (sp.simplify(exch(cell(lam_)) - cell(1 / lam_)) == 0
       and sp.simplify(exch(sp.Integer(3)) - 3 * s_) == 0 and sp.simplify(exch(5 * s_) - 5) == 0
       and sp.simplify(cell(lam_).subs(s_, 1) - 1) == 0
       and sp.simplify(sp.integrate(dens, (lam_, 0, sp.oo)) - 1) == 0
       and sp.simplify(dens.subs(lam_, 1 / lam_) / lam_ ** 2 - dens) == 0
       and sp.simplify(sp.integrate(dens * cell(lam_), (lam_, 0, sp.oo)) - sp.sqrt(s_)) == 0)
check("K3d [exact] R<->L exchange maps cell lam to cell 1/lam; cells =1 at s=1; sqrt-element = probability measure, inversion-invariant", okk)
def mat_fun_exact(M, fn):
    P, Dg = M.diagonalize(normalize=True)
    return sp.simplify(P * sp.diag(*[fn(Dg[i, i]) for i in range(Dg.shape[0])]) * P.T)
Aq = sp.Matrix([[1, 1], [1, 1]]); Bq = sp.Matrix([[2, 1], [1, 1]])
fq = lambda v: sp.sqrt((1 + v ** 2) / 2)
diffBA = Bq - Aq
detdiff = sp.nsimplify(sp.simplify((mat_fun_exact(Bq, fq) - mat_fun_exact(Aq, fq)).det()))
ok3e = (diffBA == sp.diag(1, 0)) and bool(sp.simplify(detdiff) < 0)
check("K3e [exact] A<=B exactly (B-A = diag(1,0)) but det(f(B)-f(A)) < 0 for the quadratic mean: not operator monotone", ok3e,
      f"det = {sp.N(detdiff, 12)}")

print(f"\n{sum(res)}/{len(res)} GREEN  (K3c: pre-registered failure retained; superseded by post-diagnosis K3c')")
