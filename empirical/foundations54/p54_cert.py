r"""
Paper 54 -- The One Functional, Derived.  Certificate p54_cert.py
====================================================================
Exact arithmetic (fractions.Fraction / sympy Rational / symbolic) decides every vanishing,
equality, sign and membership.  Floats / mpmath appear ONLY in lines labelled [witness].
torch is never imported (local-gate policy).

PRE-REGISTERED FALSIFIERS (written 2026-10-01 BEFORE the first run; every branch is reportable)
---------------------------------------------------------------------------------------------
K1  Complete passivity forces Gibbs (Port Principle Thm 6.3), by brute-force ergotropy of rho^{(x)n}.
    K1a  Gibbs states p_i ~ x^{E_i} (x rational in (0,1), integer E) are passive for every n <= 5:
         {E=(0,1,2), x=1/2}, {E=(0,1,3), x=2/3}, {E=(0,2,3,5), x=1/3}.        L1a: any positive ergotropy.
    K1b  Passive non-Gibbs 3-level states turn active at EXACTLY the n* of Port Thm 6.6 (Stern-Brocot
         simplest fraction strictly between r_E and r_f), computed by P5's farey3 and checked against
         P5's brute (both COPIED VERBATIM) on a NEW deterministic panel of >= 12 instances, n <= 7.
         L1b: brute != predicted on any instance.
    K1c  The free family is the whole open simplex, parametrized by theta = -beta H mod 1:
         theta(p) = log p, p_{theta(p)} = p (symbolic, Q=3,4); theta and theta + c*1 give the same state.
         L1c: the round trip fails.
K2  Static FDT = second cumulant (Thm 2), exact and symbolic, Q = 3 and Q = 4 (reduced chart theta_Q = 0).
    K2a  Hess Phi == Cov_p(T) == d<T>/dtheta == E[d_i l d_j l] == -E[d_i d_j l], identically in theta.
    K2b  Definiteness (lesson: PD vs PSD).  Reduced chart: leading minors of Hess Phi equal
         p_1...p_k (1 - p_1 - ... - p_k) > 0, so positive DEFINITE.  Full redundant chart (Q coordinates):
         only positive SEMIdefinite, rank Q-1, kernel exactly span{1}.
         L2b: PD in the full chart, or rank != Q-1, or a minor formula fails.
    K2c  d^3 Phi == third central moment of T == Amari-Chentsov tensor E[d_i l d_j l d_k l], identically.
    K2d  Legendre: Phi*(mu) = sum_i mu_i log mu_i (negative entropy) and Hess Phi* = (Hess Phi)^{-1}.
    K2e  Bregman = relative entropy: D(p_th || p_th') == Phi(th') - Phi(th) - <grad Phi(th), th'-th>,
         identically; along th' = th + eps*d its eps-derivative vanishes at 0 (rung 1, "first law") and
         its second eps-derivative at 0 is d^T Hess Phi d (rung 2).
    K2q  Quantum, 2x2 symbolic: d^2/dt^2 log tr exp(theta + tX)|_0 == Kubo-Mori (canonical) variance
         p1 p2 (x-z)^2 + y^2 tanh(a)/a, for theta = diag(a,-a), a > 0, X = [[x,y],[y,z]].  The symmetrized
         variance exceeds it by y^2 (1 - tanh(a)/a) >= 0, zero iff y = 0 ([X,theta] = 0).
         L2q: the Hessian equals the symmetrized variance with y != 0.
K3  Non-equilibrium matched pair (Thm 3).  Rates w_ij -> w_ij exp(eps[(V_j - V_i)/2 + sigma_ij]),
    sigma symmetric.  Route (i): DIRECT exact solve of pi' L = -pi L', sum pi' = 0.
    Route (ii): closed form h = Vbar + (L*)^{-1}(L_A Vbar - k_sigma), pi' = pi . h, with
    L* the time reversal, L_A = (L - L*)/2, (k_sigma)_j = (1/pi_j) sum_i sigma_ij J_ij, J_ij = pi_i w_ij - pi_j w_ji.
    K3a  Detailed balance (pi = (1/2,1/3,1/6), symmetric traffic s01=1, s02=2, s12=3): response == covariance
         for all indicator A, V and for sigma in {0, (s01,s02,s12)=(1,-2,5)}; response matrix symmetric;
         route (i) == route (ii).
    K3b  Driven 3-cycle (rate a forward i->i+1, b backward), (a,b) in {(2,1),(3,1),(5,2)}.  PREDICTED (sigma=0):
             h = [Vbar - (a-b)/(3(a+b)) (S - S^{-1}) Vbar] / (1 + tau^2),   tau^2 = (a-b)^2 / (3 (a+b)^2),
         (S f)_i = f_{i+1}; hence chi_VV / Var(V) = 3(a+b)^2 / (3(a+b)^2 + (a-b)^2) = 27/28, 12/13, 49/52
         for EVERY non-constant V (checked on 4 V's per chain); response matrix NOT symmetric (no potential);
         route (i) == route (ii) == prediction.  Uniform sigma has no effect; a non-uniform sigma changes the
         response, and route (i) == route (ii) with that sigma.
         L3b: zero gap, wrong ratio, symmetric response matrix, or a route mismatch.
    K3c  Trees (b1 = 0): 3-state path (w01=5, w10=1, w12=2, w21=7) and 4-state star (centre 0) with
         unequal rates have J = 0 and response == covariance exactly (Kolmogorov).  L3c: nonzero J on a tree.
    K3d  Arrow dimension = b1: for path (b1=0), triangle (1), square + one diagonal (2), K4 (3), the
         stationary currents of 6 deterministic rate assignments are divergence-free and span a space of
         dimension exactly b1.  L3d: rank != b1 or a non-zero divergence.
    K3e  Three readings separate (4-state NESS on K4, sigma = 0): Var(V), chi_VV = <Vbar,h>, I_V = <h,h>
         pairwise distinct and chi_VV^2 < Var(V) I_V strictly; at detailed balance all three are equal.
         L3e: any equality out of equilibrium, or inequality at detailed balance.
    K3f  [witness, mpmath 60 digits]  (1) bound ||h - Vbar|| <= ||L_A|| ||Vbar|| / lambda_S (sigma=0) on the
         K3b and K3e chains; (2) the TRUE exponentially perturbed chain at eps = 1e-25 reproduces route (i)
         by finite difference to relative 1e-15.
K4  Hessian-geometry curvature identity R = AN(T) (Shima), Q = 3, 4, 5, centroid and off-centroid.
    K4a  REUSED VERBATIM: check_N from empirical/phiF_curvature_reverify.py (mixture chart, Christoffels
         differentiated from g):  R == (1/4)(g g - g g), R == AN, scalar = D(D-1)/4.
    K4b  INDEPENDENT natural chart: cumulants from the CGF at a rational point, Gamma = (1/2) g^{-1} T,
         d Gamma from the 4th cumulant, Riemann tensor by definition; compare with
         AN(T) = (1/4) g^{pq}(T_adp T_bcq - T_acp T_bdq) and with (1/4)(g_ac g_bd - g_ad g_bc).
    L4: any component mismatch.
K5  Finite Bekenstein = passivity of a KMS state (Thm 5).  sigma_i ~ x^{E_i} (beta = -log x), rho rational.
    K5a  Identity (symbolic): D(rho||sigma) == beta(<H>_rho - <H>_sigma) - (S(rho) - S(sigma))
         == Phi(theta) + Phi*(rho) - <theta, rho> (Fenchel-Young gap), theta = -beta E.
    K5b  Sign (exact, via exp(N D) = prod (rho_i/sigma_i)^{N rho_i} compared with 1): D >= 0 on >= 40
         deterministic classical pairs and >= 8 quantum pairs (rho = U diag(r) U^T, U rational orthogonal),
         with equality exactly on the pairs where rho == sigma (included in the panel).
    K5c  Faces of the one inequality, realized on disjoint instance sets: isentropic face (rho = P sigma,
         P a permutation) gives D == beta W exactly with W >= 0 (passivity; Port Cor 6.13); beta = 0 face
         gives D == log Q - S(rho) (capacity; Paper 32.1 Thm 4.1).
    L5: any negative D, any equality with rho != sigma, or any identity failure.

RUN LOG (append-only; failures retained)
---------------------------------------
Run 1 (2026-10-01, blind; p54_run1.log): 19/21.
  FAIL K2d -- CHECKER ARTIFACT.  The Hess Phi* (Hess Phi) = I half passed exactly; the residual
       Phi* - sum mu log mu returned as -log(x) - log(1/x), x = 1 - m1 - m2, which sympy could not cancel
       because nothing told it x > 0 (assumption-blind simplifier; same class as P3.N2.K2c).  30-digit
       witness at a rational point: 0e-165.  Fix: manifestly positive chart mu_i = a_i / sum a.
  FAIL K3d -- CHECKER ARTIFACT.  On one K4 rate assignment (kk=2) the stationary() helper passed an
       exact rational through sp.nsimplify, which replaced it by a surd approximation
       (2**(161/174)*3**(97/174)*...); the corrupted "pi" was not stationary, its "current" was not
       divergence-free, and the rank came out 4 > b1 = 3.  The other five K4 assignments were exactly
       divergence-free.  Same class as P4.R10 (nsimplify corrupting exact rationals).  Fix: no nsimplify;
       assert exact rationals.  Same hardening applied to cumulants_nat (K4b passed in run 1).
  Neither artifact is counted as a result.  Run 2 re-runs the whole file unchanged otherwise.
Run 2 (2026-10-01, after the two logged artifact fixes; p54_run2.log): 21/21, 20.6 s.
  Every pre-registered prediction held, including the closed-form 3-cycle ratios 27/28, 12/13, 49/52,
  the PSD-not-PD rank Q-1 statement, K4 rank b1 = 3, and the two independent curvature routes.
  Not blind with respect to the two repaired checkers; blind for every other check.
"""
import sys
import time
import math
from fractions import Fraction as F
from itertools import product, combinations

import numpy as np
import sympy as sp
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

T0 = time.time()

# ----------------------------------------------------------------------------------------------
# COPIED VERBATIM from empirical/port_principle/p5_copy_threshold_and_circuits.py (lines 59-62)
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# COPIED VERBATIM from empirical/port_principle/p4_review_v2.py (ldl_psd)
def ldl_psd(M):
    M = sp.Matrix(M); n = M.shape[0]
    for k in range(n):
        if M[k, k] < 0: return False
        if M[k, k] == 0:
            if any(M[k, j] != 0 for j in range(k, n)): return False
            continue
        for i in range(k + 1, n):
            f = M[i, k] / M[k, k]
            for j in range(k, n): M[i, j] -= f * M[k, j]
    return True
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# COPIED VERBATIM from empirical/port_principle/p5_copy_threshold_and_circuits.py (H2 helpers)
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
# ----------------------------------------------------------------------------------------------

# ================================================================================================
print("== K1 complete passivity forces Gibbs (brute-force ergotropy of rho^(x)n) ==")
okA = True
for E, x in [((0, 1, 2), F(1, 2)), ((0, 1, 3), F(2, 3)), ((0, 2, 3, 5), F(1, 3))]:
    w = [x ** e for e in E]; Z = sum(w)
    lv = [(e, wi / Z) for e, wi in zip(E, w)]
    for n in range(1, 6):
        okA &= (ergo(copies(lv, n)) == 0)
check("K1a Gibbs states p ~ x^E stay passive for every n <= 5 (three spectra)", okA)

okB, casesB, rows = True, 0, []
fr = [F(3, 4), F(1, 2), F(2, 3), F(4, 7), F(5, 8), F(3, 5), F(7, 10), F(5, 9), F(2, 5), F(6, 7)]
for i, (E1, E2) in enumerate([(1, 2), (2, 3), (1, 3), (3, 4), (2, 5)]):
    for j in range(6):
        a = fr[(2 * i + j) % len(fr)]; b = a * fr[(i + 3 * j + 2) % len(fr)]
        if not (1 > a > b > 0): continue
        Z = 1 + a + b; lv = [(0, 1 / Z), (E1, a / Z), (E2, b / Z)]
        if ergo(lv) != 0: continue
        nf = farey3(E1, E2, F(1), a, b)
        if nf is None: continue
        nb = brute(lv, 7); casesB += 1
        okB &= (nb == nf) if nf <= 7 else (nb is None)
        rows.append((E1, E2, a, b, nf, nb))
check("K1b passive non-Gibbs 3-level states activate at the Stern-Brocot n* (new panel, brute n<=7)",
      okB and casesB >= 12, f"{casesB} instances; e.g. {rows[:3]}")

ok = True
for Q in (3, 4):
    pp = sp.symbols(f"p1:{Q+1}", positive=True)
    th = [sp.log(pi) for pi in pp]
    c = sp.symbols("c", real=True)
    Zs = sum(sp.exp(t) for t in th); Zc = sum(sp.exp(t + c) for t in th)
    norm = sum(pp)
    for i in range(Q):
        ok &= sp.simplify(sp.exp(th[i]) / Zs - pp[i] / norm) == 0
        ok &= sp.simplify(sp.exp(th[i] + c) / Zc - sp.exp(th[i]) / Zs) == 0
check("K1c free family = open simplex: theta(p)=log p round-trips, theta ~ theta + c1 (Q=3,4)", ok)

# ================================================================================================
print("== K2 static FDT = second cumulant (symbolic) ==")

def family(Q):
    th = list(sp.symbols(f"t1:{Q}", real=True))           # reduced chart, theta_Q = 0
    thf = th + [sp.Integer(0)]
    Z = sum(sp.exp(t) for t in thf)
    Phi = sp.log(Z)
    p = [sp.exp(t) / Z for t in thf]
    Tst = [[sp.Integer(1) if x == i else sp.Integer(0) for i in range(Q - 1)] for x in range(Q)]  # one-hot
    return th, thf, Z, Phi, p, Tst

_U = sp.symbols("w1:5", positive=True)
def z(expr):
    """exact zero test: substitute t_i = log(w_i) (w_i > 0), then cancel the rational function"""
    sub = {sp.Symbol(f"t{i+1}", real=True): sp.log(_U[i]) for i in range(4)}
    e = sp.cancel(sp.together(sp.expand_log(sp.sympify(expr).subs(sub), force=True)))
    return e == 0 or sp.simplify(e) == 0

ok2a = ok2c = ok2b = ok2d = ok2e = True
for Q in (3, 4):
    th, thf, Z, Phi, p, Tst = family(Q)
    D = Q - 1
    H = sp.hessian(Phi, th)
    m = [sum(p[x] * Tst[x][i] for x in range(Q)) for i in range(D)]
    Cov = sp.Matrix(D, D, lambda i, j: sum(p[x] * Tst[x][i] * Tst[x][j] for x in range(Q)) - m[i] * m[j])
    Resp = sp.Matrix(D, D, lambda i, j: sp.diff(m[i], th[j]))
    logp = [thf[x] - Phi for x in range(Q)]
    Fish = sp.Matrix(D, D, lambda i, j: sum(p[x] * sp.diff(logp[x], th[i]) * sp.diff(logp[x], th[j]) for x in range(Q)))
    Fish2 = sp.Matrix(D, D, lambda i, j: -sum(p[x] * sp.diff(logp[x], th[i], th[j]) for x in range(Q)))
    for i in range(D):
        for j in range(D):
            ok2a &= z(H[i, j] - Cov[i, j]) and z(H[i, j] - Resp[i, j]) and z(H[i, j] - Fish[i, j]) and z(H[i, j] - Fish2[i, j])
    # K2b leading minors in the reduced chart
    for k in range(1, D + 1):
        target = sp.Mul(*p[:k]) * (1 - sum(p[:k]))
        ok2b &= z(H[:k, :k].det() - target)
    # K2c third derivative = third central moment = Amari-Chentsov E[dl dl dl]
    for i in range(D):
        for j in range(i, D):
            for k in range(j, D):
                d3 = sp.diff(Phi, th[i], th[j], th[k])
                cm3 = sum(p[x] * (Tst[x][i] - m[i]) * (Tst[x][j] - m[j]) * (Tst[x][k] - m[k]) for x in range(Q))
                ac = sum(p[x] * sp.diff(logp[x], th[i]) * sp.diff(logp[x], th[j]) * sp.diff(logp[x], th[k]) for x in range(Q))
                ok2c &= z(d3 - cm3) and z(d3 - ac)
    # K2d Legendre dual on the mean chart
    aa = list(sp.symbols(f"a1:{Q+1}", positive=True)); sa = sum(aa)
    mu = list(sp.symbols(f"m1:{Q}", positive=True)); muQ = 1 - sum(mu)
    posp = {mu[i]: aa[i] / sa for i in range(D)}          # mu_i = a_i / sum a  (all > 0), mu_Q = a_Q / sum a
    thstar = {th[i]: sp.log(mu[i] / muQ) for i in range(D)}
    grad_at = [sp.simplify(sp.diff(Phi, th[i]).subs(thstar)) for i in range(D)]
    ok2d &= all(z(grad_at[i] - mu[i]) for i in range(D))
    Phistar = sum(mu[i] * thstar[th[i]] for i in range(D)) - Phi.subs(thstar)
    negent = sum(mu[i] * sp.log(mu[i]) for i in range(D)) + muQ * sp.log(muQ)
    ok2d &= sp.simplify(sp.expand_log(sp.simplify((Phistar - negent).subs(posp)), force=True)) == 0
    HPs = sp.hessian(negent, mu)
    Hat = H.subs(thstar)
    ok2d &= sp.simplify(HPs * Hat - sp.eye(D)) == sp.zeros(D, D)
    # K2e Bregman = KL; rung 1 vanishes; rung 2 = Hessian
    thp = list(sp.symbols(f"u1:{Q}", real=True)); thpf = thp + [sp.Integer(0)]
    Zp = sum(sp.exp(t) for t in thpf); Phip = sp.log(Zp); pp_ = [sp.exp(t) / Zp for t in thpf]
    KL = sum(p[x] * (sp.log(p[x]) - sp.log(pp_[x])) for x in range(Q))
    breg = Phip - Phi - sum(sp.diff(Phi, th[i]) * (thp[i] - th[i]) for i in range(D))
    ok2e &= sp.simplify(sp.expand_log(KL - breg, force=True)) == 0
    eps = sp.symbols("eps", real=True); dvec = [sp.Integer(i + 2) for i in range(D)]
    along = {thp[i]: th[i] + eps * dvec[i] for i in range(D)}
    Dl = breg.subs(along)
    r1 = sp.diff(Dl, eps).subs(eps, 0); r2 = sp.diff(Dl, eps, 2).subs(eps, 0)
    quad = sum(dvec[i] * H[i, j] * dvec[j] for i in range(D) for j in range(D))
    ok2e &= z(r1) and z(r2 - quad)
check("K2a Hess Phi == Cov(T) == d<T>/dtheta == E[dl dl] == -E[d2 l], identically (Q=3,4)", ok2a)
check("K2b reduced-chart leading minors == p1..pk (1 - p1 - .. - pk) > 0 (positive DEFINITE)", ok2b)
# full redundant chart: PSD, rank Q-1, kernel span{1}
okfull = True
for Q, pv in [(3, [F(1, 2), F(1, 3), F(1, 6)]), (4, [F(2, 5), F(3, 10), F(1, 5), F(1, 10)])]:
    Hf = sp.Matrix(Q, Q, lambda i, j: (sp.Rational(pv[i]) if i == j else 0) - sp.Rational(pv[i]) * sp.Rational(pv[j]))
    ns = Hf.nullspace()
    okfull &= ldl_psd(Hf) and Hf.rank() == Q - 1 and len(ns) == 1 and all(v == ns[0][0] for v in ns[0]) and Hf.det() == 0
check("K2b full chart: Hess Phi is PSD, NOT PD: rank Q-1, kernel exactly span{1} (Q=3,4)", okfull)
check("K2c d^3 Phi == third central moment == Amari-Chentsov E[dl dl dl], identically (Q=3,4)", ok2c)
check("K2d Legendre dual Phi* = sum mu log mu (negative entropy); Hess Phi* = (Hess Phi)^-1 (Q=3,4)", ok2d)
check("K2e D(p_th||p_th') == Bregman(Phi); rung-1 term vanishes; rung-2 == d^T Hess Phi d (Q=3,4)", ok2e)

a_, x_, y_, z_, t_ = sp.symbols("a x y z t", real=True)
a_ = sp.symbols("a", positive=True)
M = sp.Matrix([[a_ + t_ * x_, t_ * y_], [t_ * y_, -a_ + t_ * z_]])
disc = sp.sqrt((M[0, 0] - M[1, 1]) ** 2 + 4 * M[0, 1] ** 2)
lp_, lm_ = (M.trace() + disc) / 2, (M.trace() - disc) / 2
PhiQ = sp.log(sp.exp(lp_) + sp.exp(lm_))
HQ = sp.simplify(sp.diff(PhiQ, t_, 2).subs(t_, 0))
p1 = sp.exp(a_) / (sp.exp(a_) + sp.exp(-a_)); p2 = 1 - p1
KM = p1 * p2 * (x_ - z_) ** 2 + y_ ** 2 * sp.tanh(a_) / a_
SYM = p1 * p2 * (x_ - z_) ** 2 + y_ ** 2
okq = sp.simplify((HQ - KM).rewrite(sp.exp)) == 0
gap = sp.simplify((SYM - HQ).rewrite(sp.exp) - (y_ ** 2 * (1 - sp.tanh(a_) / a_)).rewrite(sp.exp)) == 0
L2q_fires = sp.simplify((HQ - SYM).subs({y_: 1, a_: 1, x_: 0, z_: 0})) == 0
check("K2q quantum: Hess log tr e^theta == Kubo-Mori variance; symmetrized variance exceeds it by y^2(1-tanh a/a)",
      okq and gap and not L2q_fires, f"HQ={sp.simplify(HQ)}")

# ================================================================================================
print("== K3 non-equilibrium matched pair: the static FDT defect is the current ==")
R_ = sp.Rational

def generator(n, w):
    L = sp.zeros(n, n)
    for (i, j), r in w.items():
        L[i, j] += r; L[i, i] -= r
    return L

def stationary(L):
    n = L.shape[0]
    A = L.T.col_join(sp.ones(1, n)); b = sp.zeros(n, 1).col_join(sp.Matrix([1]))
    sol = A.gauss_jordan_solve(b)[0]
    out = list(sol)
    assert all(v.is_Rational for v in out), "stationary law must be exact rational"
    return out

def route_i(n, w, pi, V, sig):
    Lp = sp.zeros(n, n)
    for (i, j), r in w.items():
        val = r * (R_(V[j] - V[i], 2) + sig.get(frozenset((i, j)), 0))
        Lp[i, j] += val; Lp[i, i] -= val
    L = generator(n, w)
    rhs = -(sp.Matrix([pi]) * Lp)
    A = L.T.col_join(sp.ones(1, n)); b = rhs.T.col_join(sp.Matrix([0]))
    return list(A.gauss_jordan_solve(b)[0])                     # pi'

def route_ii(n, w, pi, V, sig):
    L = generator(n, w)
    Ls = sp.Matrix(n, n, lambda i, j: pi[j] * L[j, i] / pi[i])    # time reversal L*
    LA = (L - Ls) / 2
    mean = sum(pi[i] * V[i] for i in range(n))
    Vb = sp.Matrix([V[i] - mean for i in range(n)])
    J = {(i, j): pi[i] * w.get((i, j), 0) - pi[j] * w.get((j, i), 0) for i in range(n) for j in range(n)}
    k = sp.Matrix([sum(sig.get(frozenset((i, j)), 0) * J[(i, j)] for i in range(n) if i != j) / pi[j] for j in range(n)])
    rhs = LA * Vb - k
    A = Ls.col_join(sp.Matrix([pi])); b = rhs.col_join(sp.Matrix([0]))
    u = A.gauss_jordan_solve(b)[0]
    h = Vb + u
    return [pi[i] * h[i] for i in range(n)], h, Vb, LA, Ls, J

def cov(pi, A, V):
    n = len(pi); mA = sum(pi[i] * A[i] for i in range(n)); mV = sum(pi[i] * V[i] for i in range(n))
    return sum(pi[i] * (A[i] - mA) * (V[i] - mV) for i in range(n))

def chi(dpi, A):
    return sum(dpi[i] * A[i] for i in range(len(A)))

def ind(n, i):
    return [1 if k == i else 0 for k in range(n)]

def resp_matrix(n, w, pi, sig):
    cols = [route_i(n, w, pi, ind(n, j), sig) for j in range(n)]
    return sp.Matrix(n, n, lambda i, j: cols[j][i])            # d pi_i / d V_j

# K3a detailed balance
pi_db = [R_(1, 2), R_(1, 3), R_(1, 6)]
s_db = {(0, 1): 1, (0, 2): 2, (1, 2): 3}
w_db = {}
for (i, j), s in s_db.items():
    w_db[(i, j)] = R_(s) / pi_db[i]; w_db[(j, i)] = R_(s) / pi_db[j]
pis = stationary(generator(3, w_db))
ok3a = (pis == pi_db)
for sig in [{}, {frozenset((0, 1)): 1, frozenset((0, 2)): -2, frozenset((1, 2)): 5}]:
    for jv in range(3):
        V = ind(3, jv)
        d1 = route_i(3, w_db, pi_db, V, sig); d2 = route_ii(3, w_db, pi_db, V, sig)[0]
        ok3a &= all(sp.simplify(d1[i] - d2[i]) == 0 for i in range(3))
        for ia in range(3):
            ok3a &= (chi(d1, ind(3, ia)) - cov(pi_db, ind(3, ia), V) == 0)
Mdb = resp_matrix(3, w_db, pi_db, {})
ok3a &= (Mdb - Mdb.T == sp.zeros(3, 3))
check("K3a detailed balance: response == covariance (all A,V; sigma in {0, nonuniform}); response matrix symmetric", ok3a)

# K3b driven 3-cycle
ok3b, ratios = True, []
for (a, b), pred in [((2, 1), R_(27, 28)), ((3, 1), R_(12, 13)), ((5, 2), R_(49, 52))]:
    w = {}
    for i in range(3):
        w[(i, (i + 1) % 3)] = R_(a); w[(i, (i - 1) % 3)] = R_(b)
    pi = stationary(generator(3, w))
    ok3b &= (pi == [R_(1, 3)] * 3)
    tau2 = R_((a - b) ** 2, 3 * (a + b) ** 2)
    for V in ([1, 0, 0], [0, 1, 0], [2, -1, 5], [3, 3, -7]):
        d1 = route_i(3, w, pi, V, {})
        d2, h, Vb, LA, Ls, J = route_ii(3, w, pi, V, {})
        S_Vb = [Vb[(i + 1) % 3] for i in range(3)]; Sm_Vb = [Vb[(i - 1) % 3] for i in range(3)]
        hpred = [(Vb[i] - R_(a - b, 3 * (a + b)) * (S_Vb[i] - Sm_Vb[i])) / (1 + tau2) for i in range(3)]
        ok3b &= all(d1[i] == d2[i] for i in range(3)) and all(h[i] == hpred[i] for i in range(3))
        r = chi(d1, V) / cov(pi, V, V)
        ok3b &= (r == pred) and (chi(d1, V) != cov(pi, V, V))
        ratios.append(r)
    Mc = resp_matrix(3, w, pi, {})
    ok3b &= (Mc - Mc.T != sp.zeros(3, 3))
    # sigma: uniform has no effect; non-uniform changes response, routes agree
    V = [2, -1, 5]
    base = route_i(3, w, pi, V, {})
    uni = route_i(3, w, pi, V, {frozenset((0, 1)): 4, frozenset((1, 2)): 4, frozenset((0, 2)): 4})
    nonu = {frozenset((0, 1)): 1, frozenset((1, 2)): 0, frozenset((0, 2)): -3}
    nu1 = route_i(3, w, pi, V, nonu); nu2 = route_ii(3, w, pi, V, nonu)[0]
    ok3b &= (base == uni) and (nu1 != base) and all(nu1[i] == nu2[i] for i in range(3))
check("K3b driven 3-cycle: chi_VV/Var(V) == 3(a+b)^2/(3(a+b)^2+(a-b)^2) for every V; predicted h exact; "
      "response matrix NOT symmetric; sigma: uniform inert, non-uniform active; routes agree", ok3b,
      f"ratios={sorted(set(ratios))}")

# K3c trees
ok3c = True
for n, w in [(3, {(0, 1): R_(5), (1, 0): R_(1), (1, 2): R_(2), (2, 1): R_(7)}),
             (4, {(0, 1): R_(3), (1, 0): R_(1, 2), (0, 2): R_(1), (2, 0): R_(4), (0, 3): R_(2, 3), (3, 0): R_(5)})]:
    pi = stationary(generator(n, w))
    J = [pi[i] * w.get((i, j), 0) - pi[j] * w.get((j, i), 0) for i in range(n) for j in range(n)]
    ok3c &= all(x == 0 for x in J)
    for jv in range(n):
        V = ind(n, jv); d1 = route_i(n, w, pi, V, {})
        ok3c &= all(chi(d1, ind(n, ia)) == cov(pi, ind(n, ia), V) for ia in range(n))
check("K3c trees (b1=0): J == 0 and response == covariance for arbitrary rates (path, star)", ok3c)

# K3d arrow dimension = b1
graphs = {"path": (3, [(0, 1), (1, 2)], 0), "triangle": (3, [(0, 1), (1, 2), (0, 2)], 1),
          "square+diag": (4, [(0, 1), (1, 2), (2, 3), (0, 3), (0, 2)], 2),
          "K4": (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], 3)}
ok3d, ranks = True, {}
for name, (n, E, b1) in graphs.items():
    Js = []
    for kk in range(6):
        w = {}
        for (i, j) in E:
            w[(i, j)] = R_(1 + (3 * i + 5 * j + 7 * kk) % 11); w[(j, i)] = R_(1 + (2 * j + 7 * i + 3 * kk * kk) % 13)
        pi = stationary(generator(n, w))
        Jv = [pi[i] * w[(i, j)] - pi[j] * w[(j, i)] for (i, j) in E]
        div = [sum(Jv[e] * (1 if E[e][0] == v else -1 if E[e][1] == v else 0) for e in range(len(E))) for v in range(n)]
        ok3d &= all(dv == 0 for dv in div)
        Js.append(Jv)
    rk = sp.Matrix(Js).rank(); ranks[name] = (rk, b1)
    ok3d &= (rk == b1)
check("K3d stationary currents are divergence-free and span exactly b1 dimensions", ok3d, f"{ranks}")

# K3e three readings separate on a 4-state NESS; equal at detailed balance
def three(n, w, pi, V):
    d, h, Vb, *_ = route_ii(n, w, pi, V, {})
    var = sum(pi[i] * Vb[i] ** 2 for i in range(n))
    chv = sum(pi[i] * Vb[i] * h[i] for i in range(n))
    I = sum(pi[i] * h[i] ** 2 for i in range(n))
    return var, chv, I
E4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
w_ness = {}
for (i, j) in E4:
    w_ness[(i, j)] = R_(1 + (3 * i + 5 * j) % 7); w_ness[(j, i)] = R_(1 + (5 * i + 2 * j) % 5, 2)
pi_ness = stationary(generator(4, w_ness))
V4 = [1, 0, 2, -1]
var, chv, I = three(4, w_ness, pi_ness, V4)
ok3e = (len({var, chv, I}) == 3) and (chv ** 2 < var * I)
pi_eq = [R_(1, 10), R_(2, 10), R_(3, 10), R_(4, 10)]
w_eq = {}
for idx, (i, j) in enumerate(E4):
    s = R_(1 + idx)
    w_eq[(i, j)] = s / pi_eq[i]; w_eq[(j, i)] = s / pi_eq[j]
var0, chv0, I0 = three(4, w_eq, pi_eq, V4)
ok3e &= (var0 == chv0 == I0)
check("K3e out of equilibrium Var(V), chi_VV, I_V pairwise distinct with chi^2 < Var*I; at detailed balance all equal",
      ok3e, f"NESS: Var={var}, chi={chv}, I={I}; DB: {var0},{chv0},{I0}")

# K3f witnesses
mp.mp.dps = 60
def MP(x):
    return mp.mpf(str(sp.N(x, 70)))
def bound_witness(n, w, pi, V):
    d, h, Vb, LA, Ls, J = route_ii(n, w, pi, V, {})
    L = generator(n, w)
    Dh = sp.diag(*[sp.sqrt(x) for x in pi]); Dhi = sp.diag(*[1 / sp.sqrt(x) for x in pi])
    LAs = Dh * LA * Dhi; LSs = Dh * ((L + Ls) / 2) * Dhi
    LAm = mp.matrix(n, n); LSm = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            LAm[i, j] = MP(LAs[i, j]); LSm[i, j] = MP(LSs[i, j])
    normLA = max(mp.sqrt(abs(e)) for e in mp.eig(LAm.T * LAm)[0])
    evS = sorted(-mp.re(e) for e in mp.eig(LSm)[0])
    lamS = [e for e in evS if e > mp.mpf(10) ** -40][0]
    nrm = lambda f: mp.sqrt(sum(MP(pi[i] * f[i] ** 2) for i in range(n)))
    lhs = nrm([h[i] - Vb[i] for i in range(n)]); rhs = normLA * nrm(list(Vb)) / lamS
    return lhs <= rhs, (float(lhs), float(rhs))
wit = []
okf = True
w_c = {}
for i in range(3):
    w_c[(i, (i + 1) % 3)] = R_(2); w_c[(i, (i - 1) % 3)] = R_(1)
for (n, w, pi, V) in [(3, w_c, [R_(1, 3)] * 3, [1, 0, 0]), (4, w_ness, pi_ness, V4)]:
    okk, vals = bound_witness(n, w, pi, V); okf &= okk; wit.append(vals)
# finite difference of the true exponential perturbation
epsf = mp.mpf(10) ** -25
def true_pi(n, w, V, e):
    Lm = mp.matrix(n, n)
    for (i, j), r in w.items():
        val = mp.mpf(int(sp.Rational(r).p)) / int(sp.Rational(r).q) * mp.e ** (e * mp.mpf(V[j] - V[i]) / 2)
        Lm[i, j] += val; Lm[i, i] -= val
    A = mp.matrix(n + 1, n); bb = mp.matrix(n + 1, 1)
    for i in range(n):
        for j in range(n):
            A[i, j] = Lm[j, i]
    for j in range(n):
        A[n, j] = 1
    bb[n] = 1
    return mp.lu_solve(A.T * A, A.T * bb)
for (n, w, pi, V) in [(3, w_c, [R_(1, 3)] * 3, [2, -1, 5]), (4, w_ness, pi_ness, V4)]:
    d1 = route_i(n, w, pi, V, {})
    p_e = true_pi(n, w, V, epsf); p_0 = true_pi(n, w, V, 0)
    for i in range(n):
        fd = (p_e[i] - p_0[i]) / epsf; ex = MP(d1[i])
        okf &= abs(fd - ex) <= mp.mpf(10) ** -15 * max(abs(ex), mp.mpf(1))
check("K3f [witness] ||h-Vbar|| <= ||L_A|| ||Vbar|| / lambda_S; true exp-perturbed chain matches route (i) by finite difference",
      okf, f"(lhs, rhs) = {wit}")

# ================================================================================================
print("== K4 Hessian-geometry curvature identity R = AN(T) ==")
# ----------------------------------------------------------------------------------------------
# COPIED VERBATIM from empirical/phiF_curvature_reverify.py (check_N), cited in Paper 54 Section 4.
def check_N(N, pvals, label):
    D = N - 1
    p = sp.symbols(f'p0:{D}', positive=True)
    pN = 1 - sum(p)
    g = sp.Matrix(D, D, lambda i, j: (1/p[i] if i == j else sp.Integer(0)) + 1/pN)
    ginv = sp.Matrix(D, D, lambda i, j: (p[i] if i == j else sp.Integer(0)) - p[i]*p[j])

    def C(i, j, k):
        return 1/pN**2 - ((1/p[i]**2) if (i == j == k) else sp.Integer(0))

    # Christoffel ^i_{jk} with closed-form inverse (no premature simplify)
    dg = [[[sp.diff(g[a, b], p[c]) for c in range(D)] for b in range(D)] for a in range(D)]
    Gam = [[[sum(ginv[i, m]*(dg[m][k][j] + dg[m][j][k] - dg[j][k][m]) for m in range(D))/2
             for k in range(D)] for j in range(D)] for i in range(D)]

    def Rup(i, j, k, l):  # R^i_{jkl}
        t = sp.diff(Gam[i][l][j], p[k]) - sp.diff(Gam[i][k][j], p[l])
        t += sum(Gam[i][k][m]*Gam[m][l][j] - Gam[i][l][m]*Gam[m][k][j] for m in range(D))
        return t

    subs = {p[i]: pvals[i] for i in range(D)}
    gv = g.subs(subs)
    giv = ginv.subs(subs)
    assert (gv*giv) == sp.eye(D), "closed-form inverse check failed"
    Cv = {(i, j, k): C(i, j, k).subs(subs) for i in range(D) for j in range(D) for k in range(D)}

    R = {}
    for i in range(D):
        for j in range(D):
            for k in range(D):
                for l in range(D):
                    R[(i, j, k, l)] = sp.together(sum(g[i, m]*Rup(m, j, k, l) for m in range(D)).subs(subs))

    K = sp.Rational(1, 4)
    okGG = all(sp.simplify(R[(i, j, k, l)] - K*(gv[i, k]*gv[j, l] - gv[i, l]*gv[j, k])) == 0
               for i in range(D) for j in range(D) for k in range(D) for l in range(D))

    def AN(i, j, k, l):
        # dually-flat (Amari-Nagaoka) curvature-from-cubic, standard sign:
        # R_ijkl = (1/4) g^{mn}(C_ilm C_jkn - C_ikm C_jln)
        return K*sum(giv[m, n]*(Cv[(i, l, m)]*Cv[(j, k, n)] - Cv[(i, k, m)]*Cv[(j, l, n)])
                     for m in range(D) for n in range(D))
    okAN = all(sp.simplify(R[(i, j, k, l)] - AN(i, j, k, l)) == 0
               for i in range(D) for j in range(D) for k in range(D) for l in range(D))

    Ric = sp.Matrix(D, D, lambda j, l: sum(giv[i, k]*R[(i, j, k, l)] for i in range(D) for k in range(D)))
    scal = sp.simplify(sum(giv[j, l]*Ric[j, l] for j in range(D) for l in range(D)))
    okScal = (scal == sp.Rational(D*(D-1), 4))
    return okGG, okAN, scal, okScal
# ----------------------------------------------------------------------------------------------

ok4a, det4a = True, []
for N in (3, 4, 5):
    D = N - 1; T_ = N * (N + 1) // 2
    for nm, pv in [("centroid", [sp.Rational(1, N)] * D), ("off", [sp.Rational(i + 1, T_) for i in range(D)])]:
        okGG, okAN, scal, okScal = check_N(N, pv, nm)
        ok4a &= okGG and okAN and okScal
        det4a.append(f"Q={N}/{nm}:{okGG and okAN and okScal}")
check("K4a [reused verbatim, phiF_curvature_reverify.check_N] mixture chart: R==(1/4)(gg-gg), R==AN, scalar=D(D-1)/4",
      ok4a, " ".join(det4a))

def cumulants_nat(pv):
    """g, T, T4 in the NATURAL chart (reference atom = last), exact rationals, from the CGF."""
    Q = len(pv); D = Q - 1
    t = sp.symbols(f"s1:{Q}", real=True)
    K = sp.log(pv[-1] + sum(pv[a] * sp.exp(t[a]) for a in range(D)))
    at0 = {ti: 0 for ti in t}
    cache = {}
    def d(*idx):
        key = tuple(sorted(idx))
        if key not in cache:
            cache[key] = sp.Rational(sp.simplify(sp.diff(K, *[t[i] for i in key]).subs(at0)))
        return cache[key]
    g = sp.Matrix(D, D, lambda i, j: d(i, j))
    T = {(i, j, k): d(i, j, k) for i in range(D) for j in range(D) for k in range(D)}
    T4 = {(i, j, k, l): d(i, j, k, l) for i in range(D) for j in range(D) for k in range(D) for l in range(D)}
    return g, T, T4

ok4b, det4b = True, []
for N in (3, 4, 5):
    D = N - 1; T_ = N * (N + 1) // 2
    off = [sp.Rational(i + 1, T_) for i in range(D)]; off.append(1 - sum(off))
    gen = [sp.Rational(k + 2, 2 ** (k + 2)) for k in range(D)]; gen.append(1 - sum(gen))
    for nm, pv in [("centroid", [sp.Rational(1, N)] * N), ("off", off), ("generic", gen)]:
        g, T, T4 = cumulants_nat(pv); gi = g.inv(); rng = range(D)
        Gam = {(l, i, j): sum(gi[l, m] * T[(i, j, m)] for m in rng) / 2 for l in rng for i in rng for j in rng}
        dgi = {(i, l, m): -sum(gi[l, a] * gi[m, b] * T[(a, b, i)] for a in rng for b in rng) for i in rng for l in rng for m in rng}
        dGam = {(i, l, j, k): (sum(dgi[(i, l, m)] * T[(j, k, m)] + gi[l, m] * T4[(j, k, m, i)] for m in rng)) / 2
                for i in rng for l in rng for j in rng for k in rng}          # d_i Gamma^l_{jk}
        good = True
        for a in rng:
            for b in rng:
                for c in rng:
                    for dd in rng:
                        Rup = {}
                        Rl = sp.Integer(0)
                        for e in rng:
                            Re = dGam[(c, e, dd, b)] - dGam[(dd, e, c, b)] + sum(Gam[(e, c, f)] * Gam[(f, dd, b)] - Gam[(e, dd, f)] * Gam[(f, c, b)] for f in rng)
                            Rl += g[a, e] * Re
                        AN = sum(gi[p_, q_] * (T[(a, dd, p_)] * T[(b, c, q_)] - T[(a, c, p_)] * T[(b, dd, q_)]) for p_ in rng for q_ in rng) / 4
                        GG = (g[a, c] * g[b, dd] - g[a, dd] * g[b, c]) / 4
                        good &= (sp.simplify(Rl - AN) == 0) and (sp.simplify(Rl - GG) == 0)
        ok4b &= good; det4b.append(f"Q={N}/{nm}:{good}")
check("K4b [independent, natural chart] Riemann(Gamma = g^-1 T/2, dGamma from 4th cumulant) == AN(T) == (1/4)(gg-gg)",
      ok4b, " ".join(det4b))

# ================================================================================================
print("== K5 finite Bekenstein = passivity of a KMS state ==")
# K5a symbolic identities
n5 = 3
rr = sp.symbols("r1:4", positive=True); EE = sp.symbols("E1:4", real=True); bb = sp.symbols("beta", positive=True)
Zs = sum(sp.exp(-bb * e) for e in EE); sg = [sp.exp(-bb * e) / Zs for e in EE]
S = lambda q: -sum(qi * sp.log(qi) for qi in q)
Dkl = sum(rr[i] * (sp.log(rr[i]) - sp.log(sg[i])) for i in range(n5))
cons = {rr[2]: 1 - rr[0] - rr[1]}
bek = bb * (sum(rr[i] * EE[i] for i in range(n5)) - sum(sg[i] * EE[i] for i in range(n5))) - (S(rr) - S(sg))
fy = sp.log(Zs) + sum(rr[i] * sp.log(rr[i]) for i in range(n5)) + bb * sum(rr[i] * EE[i] for i in range(n5))
ok5a = (sp.simplify(sp.expand_log((Dkl - bek).subs(cons), force=True)) == 0 and
        sp.simplify(sp.expand_log((Dkl - fy).subs(cons), force=True)) == 0)
check("K5a D(rho||sigma) == beta(<H>_rho-<H>_sigma) - (S(rho)-S(sigma)) == Fenchel-Young gap (symbolic)", ok5a)

def exp_ND(rho_spec, rho_diag, sigma):
    """Return exp(N*D) as an exact rational, D = sum_k r_k log r_k - sum_i rho_ii log sigma_i."""
    den = 1
    for v in list(rho_spec) + list(rho_diag):
        den = den * F(v).denominator // math.gcd(den, F(v).denominator)
    num = F(1)
    for r in rho_spec:
        if r > 0: num *= F(r) ** int(F(r) * den)
    dn = F(1)
    for d_, s in zip(rho_diag, sigma):
        if d_ > 0: dn *= F(s) ** int(F(d_) * den)
    return num / dn

panel_cl, eq_hits, eq_expected = [], 0, 0
probs = [F(1, 2), F(1, 3), F(1, 6), F(2, 5), F(3, 10), F(1, 10), F(1, 4), F(5, 12), F(1, 3)]
ok5b = True
for E, x in [((0, 1, 2), F(1, 2)), ((0, 1, 3), F(2, 3)), ((0, 2, 5), F(3, 4)), ((0, 1, 1), F(1, 3))]:
    wv = [x ** e for e in E]; Zv = sum(wv); sig = [wi / Zv for wi in wv]
    cand = [sig]
    for k in range(10):
        a = probs[k % 9]; b = probs[(k + 4) % 9] * (1 - a)
        cand.append([a, b, 1 - a - b])
    for rho in cand[:11]:
        if min(rho) <= 0: continue
        val = exp_ND(rho, rho, sig)
        eq_expected += (rho == sig)
        ok5b &= (val >= 1)
        if val == 1:
            eq_hits += 1; ok5b &= (rho == sig)
        panel_cl.append(val)
# quantum pairs: rho = U diag(r) U^T with U rational orthogonal (Cayley transform of rational skew A)
qcount = 0
for A_ in [sp.Matrix([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]) / 4, sp.Matrix([[0, 2, 0], [-2, 0, 1], [0, -1, 0]]) / 3]:
    U = (sp.eye(3) - A_) * (sp.eye(3) + A_).inv()
    assert U * U.T == sp.eye(3)
    for E, x in [((0, 1, 2), F(1, 2)), ((0, 1, 3), F(2, 3))]:
        wv = [x ** e for e in E]; Zv = sum(wv); sig = [wi / Zv for wi in wv]
        for r in ([F(1, 2), F(1, 3), F(1, 6)], [F(3, 5), F(3, 10), F(1, 10)]):
            rho = U * sp.diag(*[sp.Rational(v) for v in r]) * U.T
            diag = [F(int(sp.Rational(rho[i, i]).p), int(sp.Rational(rho[i, i]).q)) for i in range(3)]
            val = exp_ND(r, diag, sig)
            ok5b &= (val > 1); qcount += 1
check("K5b D >= 0 exactly (classical + quantum rational panels); equality exactly where rho == sigma",
      ok5b and len(panel_cl) >= 40 and qcount >= 8 and eq_hits == eq_expected >= 4,
      f"classical pairs={len(panel_cl)}, quantum pairs={qcount}, equalities={eq_hits} (all at rho==sigma)")

# K5c faces
ok5c = True
xs = sp.symbols("x", positive=True)
for E in [(0, 1, 2), (0, 1, 3), (0, 2, 3)]:
    wv = [xs ** e for e in E]; Zv = sum(wv); sg_ = [wi / Zv for wi in wv]
    beta = -sp.log(xs)
    for perm in [(1, 0, 2), (2, 1, 0), (1, 2, 0), (2, 0, 1)]:
        rho = [sg_[perm[i]] for i in range(3)]
        Dp = sum(rho[i] * (sp.log(rho[i]) - sp.log(sg_[i])) for i in range(3))
        W = sum(rho[i] * E[i] for i in range(3)) - sum(sg_[i] * E[i] for i in range(3))
        ok5c &= sp.simplify(sp.expand_log(Dp - beta * W, force=True)) == 0
        for xv in (F(1, 2), F(1, 3), F(2, 3)):
            ok5c &= (sp.Rational(W.subs(xs, sp.Rational(xv.numerator, xv.denominator))) >= 0)
Qs = 4
r4 = sp.symbols("q1:5", positive=True)
cons4 = {r4[3]: 1 - r4[0] - r4[1] - r4[2]}
D0 = sum(r4[i] * (sp.log(r4[i]) - sp.log(sp.Rational(1, Qs))) for i in range(Qs))
ok5c &= sp.simplify(sp.expand_log((D0 - (sp.log(Qs) - S(r4))).subs(cons4), force=True)) == 0
check("K5c faces: isentropic (rho = P sigma) D == beta W, W >= 0 (passivity); beta=0: D == log Q - S (capacity)", ok5c)

# ================================================================================================
print(f"\nSUMMARY: {sum(res)}/{len(res)} checks passed  ({time.time() - T0:.1f}s)")
