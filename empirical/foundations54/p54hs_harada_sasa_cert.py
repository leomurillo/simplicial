r"""
Paper 54, section 4.2 -- the frequency-resolved arrow (a quantum Harada-Sasa equality).  Certificate p54hs_harada_sasa_cert.py
==========================================================================================================================
Exact arithmetic decides every vanishing / equality: sympy rational functions of z (Laplace variable), omega (real) and
the positive symbol l = log 2.  Strict signs: exact Sturm root counting where coefficients are rational, rigorous interval
arithmetic (mpmath.iv) at l = log 2 otherwise.  Frequency integrals (sum rules) are [witness] quadratures at 30 digits;
the operator identities they reduce to are checked exactly.  No torch.

SETTING: the qubit generators of p54q_lindblad_cert.py (helpers and generators spliced VERBATIM below): sigma = diag(4,1)/5;
L_G (GNS-DB), L_K (KMS-DB only), L_N (no DB), L_R = L_G + i[K,.] (reversible part), L_H (hypocoercive, sigma = 1/2).
f-potential push with time-dependent amplitude: source s = -Gamma_f S_f V; response R_AV(t) = tr(A e^{tLs} s), t > 0;
f-correlation C_AB(t) = <e^{t Lh} Abar, Bbar>_f (t >= 0), even extension; Laplace: Rhat(z) = tr(A (z - Ls)^-1 s),
Chat_AB(z) = <Abar, (z - Lt_f)^-1 Bbar>_f.  Violation spectrum (A = V):
    Delta_V(omega) := (omega/2) Ctilde_VV(omega) - Im Rtilde_VV(omega),  Ctilde = 2 Re Chat(-i omega), Rtilde = Rhat(-i omega).
Total (basis-free) spectrum: Delta_tot(omega) = -Im Tr_W[(i omega + Lt_f)^-1 A_f], W = f-mean-zero Hermitian observables.

PRE-REGISTERED FALSIFIERS (written 2026-10-01 BEFORE the first run; every branch is reportable)
------------------------------------------------------------------------------------------------
H1  Time-domain quantum Agarwal formula, exact in the Laplace variable:  Rhat_AV(z) = C_AV(0) - z Chat_AV(z) - Chat_{A, A_f V}(z)
    i.e. R(t) = -dC_AV/dt - C_{A, A_f V}(t), for generators {G, K, N}, f in {SLD, KMS, BKM}, A, V in {E00, sigma_x, sigma_y}.
    [witness] the same identity in the time domain at t in {0.37, 1.3} via mpmath expm (60 digits) on N/SLD and N/BKM.
    L: any mismatch.
H2  Violation spectrum: Delta_V(omega) == -Im <Vbar, (i omega + Lt_f)^-1 A_f Vbar>_f identically in omega (exact), and
    Delta_V == 0 for every V  <=>  f-DB, on the 3 x 3 grid (pattern G=(T,T,T), K=(F,T,F), N=(F,F,F)).   L: any failure.
H3  Sum rules.  [exact] Var_f(V) - chi_VV == -<Vbar, Lt^-1 A Vbar>_f ;  first moment value M1_V := <Lh Vbar, A Vbar>_f ;
    total: Sum over an f-orthonormal basis of W of M1 == ||A_f||_HS^2 (computed via Gram matrices), zero exactly in the DB
    cells and > 0 (interval) in the others.  [witness, 30 digits] (1/pi) Int Delta_V/omega = Var - chi and
    (1/pi) Int omega Delta_V = M1_V by quadrature, for V in {E00, sigma_x} on N and K (SLD and BKM), and the total first
    moment == ||A_f||_HS^2 on N/SLD.   L: any mismatch beyond 1e-20.
H4  Classical reduction to Harada-Sasa (overdamped linear Langevin, T = 1, gamma = 1, exact): for dx = Bx dt + sqrt(2) dW
    with B = [[-1,3],[-1,-2]] (non-normal), Sigma from the Lyapunov equation, nu = (B + Sigma^-1) x:
    per-coordinate M1_i = E[(Bx)_i nu_i]; cross terms M1_i - E[nu_i^2] = -Omega_ii are NONZERO individually but sum to 0;
    Sum_i M1_i = E|nu|^2 (Harada-Sasa heat rate).  Isotropic circulating case B = -k(I - eps J) (Port Principle P1.C3):
    Sum_i M1_i = 2 eps^2 k T symbolically.  Detailed-balance control (B symmetric): all M1_i = 0.   L: any failure.
H5  Kubo as the reversible-compensated case (L_R): the energy push (BKM source on the dissipator + K -> K - V/beta) gives
    Rhat = C(0) - z Chat^BKM exactly (no violation, all A, V); the dissipative-only push violates for V = sigma_x; the SLD
    analogue of the energy push violates for V = sigma_x.   L: any failure.
H6  Frequency-resolved positivity (RISKY; proven only to second order in A_f): Delta_tot(omega) > 0 for every omega > 0 in
    every non-DB cell {K/SLD, K/BKM, N/SLD, N/KMS, N/BKM, R/SLD (dissipative convention), H/SLD}, and Delta_tot == 0 in the
    DB cells.  Exact (Sturm count of positive roots + sign at omega = 1) where coefficients are rational; for BKM cells a
    [witness] scan of 2001 log-spaced omega in [1e-4, 1e4] at l = log 2.   L: any sign change (reportable as a finite-arrow
    failure of the second-order statement).

RUN LOG (append-only; failures retained)
---------------------------------------
Run 1 (2026-10-01, blind; p54hs_run1.log): H1 PASS (symbolic in z), H1 witness PASS; then H2 ran > 30 min at 1.5 GB
  (sp.simplify on complex rational functions of omega and l) and was STOPPED by hand.  No H2-H6 verdict was seen.
Run 2 (p54hs_run2.log): simplify -> cancel/together; slower still in H1 (> 30 min); STOPPED.  No verdict seen.
Checker-method change before run 3 (falsifiers untouched; H2-H6 still blind): exact identities of rational functions
  are certified by exact evaluation at more points than the numerator-degree bound (z: 8 points > 4; omega: 12 > 8),
  in Q(i)(l); H6's exact numerator is rebuilt by interpolation over the known denominator |det(i omega + Lt)|^2 and
  verified at 6 independent nodes before the Sturm count.  Quadratures use mpmath linear solves directly.
Run 3 (2026-10-01, blind for H2-H6; p54hs_run3.log): 8/8, 267 s.  H2 pattern exactly as predicted; H3 ||A_f||_HS^2 =
  0 in the DB cells, 6.25e-4 (K/SLD), 7.8e-5 (K/BKM), 4.20 / 4.05 / 4.09 (N: SLD/KMS/BKM); per-observable first moments
  and static defects can be NEGATIVE (K/SLD, V = sigma_x: M1 = -1.25e-3) -- only the basis total is sign-definite;
  H4 cross terms +4/25, -4/25 (sum 0), Sum M1 = 16/3 = E|nu|^2; H5 violations at z = 1: 12/(625 l) (dissipative-only),
  (12 - 20 l)/(625 l) (SLD energy push); H6: positive in all 7 non-DB cells (5 exact Sturm, deg Q = 5; 2 BKM witnesses).
  All-positive again, so treated as suspect: an exploratory, NOT blind probe (p54hs_explore_positivity.py, float64)
  searched for counterexamples to frequency-wise positivity with strong non-normal arrows: 1600 random Lindbladians
  (d = 2, 3; Hamiltonians up to kappa = 25; SLD, BKM) and 3300 random dissipative matrices (n <= 12, antisymmetric part
  up to 100x, hypocoercive cases included): 0 negative.  Positivity stays a CONJECTURE in general (Open Problem 4.6),
  proven to second order, at high frequency, and in the normal case.
2026-10-02: Open Problem 4.6 PROVED in general (Lemma 4.6 arrow pencil, Theorem 4.7); certificate
  p54hs_op46_proof_cert.py (4/5 with P4 retained, P4' post-diagnosis pass).
"""
import sys
import time

import sympy as sp
import mpmath as mp

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
T0 = time.time()

# ----------------------------------------------------------------------------------------------
# COPIED VERBATIM from empirical/foundations54/p54q_lindblad_cert.py (check, ldl_psd)
res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
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
# COPIED VERBATIM from empirical/foundations54/p54q_lindblad_cert.py (helpers, metrics, generators, sign_iv)
I = sp.I
R = sp.Rational
ell = sp.symbols("ell", positive=True)          # ell = log 2
d = 2

def E(i, j):
    M = sp.zeros(d, d); M[i, j] = 1; return M
def vec(X):
    return sp.Matrix([X[i, j] for i in range(d) for j in range(d)])
def unvec(v):
    return sp.Matrix(d, d, lambda i, j: v[d * i + j])
def superop(F):
    cols = [vec(F(E(i, j))) for i in range(d) for j in range(d)]
    return sp.Matrix.hstack(*cols)
def simp(M):
    return M.applyfunc(lambda z: sp.simplify(sp.expand(z)))
def iszero(M):
    return all(sp.simplify(sp.expand(z)) == 0 for z in M)

def Dis(M):
    return lambda r: M * r * M.H - (M.H * M * r + r * M.H * M) / 2
def Ham(H):
    return lambda r: -I * (H * r - r * H)
def Reset(tau):
    return lambda r: r.trace() * tau - r
def total(*Fs):
    return lambda r: sum((F(r) for F in Fs), sp.zeros(d, d))

sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -I], [I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
sm = E(0, 1); spl = E(1, 0)
Id = sp.eye(d)
BASIS = {"E00": E(0, 0), "E11": E(1, 1), "sx": sx, "sy": sy}

def weights(p, logdiff, kind):
    """diagonal superoperator Gamma_kind on matrix units, index d*i+j"""
    w = []
    for i in range(d):
        for j in range(d):
            if kind == "SLD":
                c = (p[i] + p[j]) / 2
            elif kind == "KMS":
                c = sp.sqrt(p[i] * p[j])
            elif kind == "BKM":
                c = p[i] if (i == j or p[i] == p[j]) else (p[i] - p[j]) / logdiff(i, j)
            elif kind == "GNS":
                c = p[j]
            w.append(c)   # sympy evaluates sqrt of a rational square exactly (no canonicalizer: lesson K3d)
    return sp.diag(*w)

P0 = [R(4, 5), R(1, 5)]
logdiff0 = lambda i, j: 2 * ell * (j - i)        # log p_i - log p_j = (j - i) * log 4
SIG = sp.diag(*P0)

class Gen:
    def __init__(self, Ls, p, logdiff, sigma):
        self.Ls = simp(Ls); self.Lh = simp(Ls.H); self.p = p; self.logdiff = logdiff; self.sigma = sigma
        self.C = {k: weights(p, logdiff, k) for k in ("SLD", "KMS", "BKM", "GNS")}
    def Lt(self, f):
        C = self.C[f]; return simp(C.inv() * self.Ls * C)
    def S(self, f): return simp((self.Lh + self.Lt(f)) / 2)
    def A(self, f): return simp((self.Lh - self.Lt(f)) / 2)
    def Gam(self, f, X): return unvec(self.C[f] * vec(X))
    def ip(self, f, X, Y): return sp.simplify((vec(X).H * self.C[f] * vec(Y))[0])
    def Vbar(self, V): return V - (self.sigma * V).trace() * Id
    def respond(self, s):
        """route (i): Ls sigma' = -s, tr sigma' = 0"""
        A = self.Ls.col_join(sp.Matrix([[1 if i == j else 0 for i in range(d) for j in range(d)]]))
        b = (-vec(s)).col_join(sp.Matrix([0]))
        x = A.gauss_jordan_solve(b)[0]
        return simp(unvec(x))
    def pot_source(self, f, V):
        return unvec(-self.C[f] * self.S(f) * vec(V))
    def route_ii(self, f, V):
        Vb = self.Vbar(V); Lt = self.Lt(f)
        rhs = self.A(f) * vec(Vb)
        row = sp.Matrix([[self.sigma[j, i] for i in range(d) for j in range(d)]])   # tr(sigma u)
        A = Lt.col_join(row); b = rhs.col_join(sp.Matrix([0]))
        u = A.gauss_jordan_solve(b)[0]
        return simp(self.Gam(f, Vb + unvec(u)))

def make(Fs, p=P0, logdiff=logdiff0, sigma=SIG):
    return Gen(superop(Fs), p, logdiff, sigma)

# ------------------------------------------------------------------ generators
G = make(total(lambda r: 4 * Dis(sm)(r), Dis(spl), Dis(sz)))
Mj = sp.Matrix([[1, 1], [0, 1]]); Hn = sx / 2
r0 = total(Dis(Mj), Ham(Hn))(SIG)
kap, tau = None, None
for k in (1, 2, 4, 8, 16):
    t_ = simp(SIG - r0 / k)
    if ldl_psd(t_):
        kap, tau = k, t_; break
N = make(total(Dis(Mj), Ham(Hn), lambda r: kap * Reset(tau)(r)))
LhK = simp((N.Lh + N.Lt("KMS")) / 2)
K = Gen(LhK.H, P0, logdiff0, SIG)
Kop = sp.diag(0, 1)
beta = 2 * ell
adK_h = superop(lambda X: I * (Kop * X - X * Kop))           # Heisenberg i[K, .]
Rg = Gen((G.Lh + adK_h).H, P0, logdiff0, SIG)
PH = [R(1, 2), R(1, 2)]
Hh = Gen(superop(total(Ham(sx), Dis(sz))), PH, lambda i, j: 0, sp.eye(2) / 2)

GENS = {"G": G, "K": K, "N": N}
FS = ("SLD", "KMS", "BKM")

def stationary_ok(g):
    return iszero(g.Ls * vec(g.sigma)) and g.Ls.rank() == d * d - 1
print(f"kappa = {kap};  tau = {tau.tolist()}")

def choi_ccp(Ls):
    """Lindblad test: TP (Schroedinger) and conditionally CP (Choi on the complement of Omega)."""
    C = sp.zeros(d * d, d * d)
    for i in range(d):
        for j in range(d):
            C += sp.kronecker_product(E(i, j), unvec(Ls * vec(E(i, j))))
    om = sp.Matrix([1 if (k // d) == (k % d) else 0 for k in range(d * d)])
    P = sp.eye(d * d) - om * om.T / d
    tp = iszero(sp.Matrix([[1 if i == j else 0 for i in range(d) for j in range(d)]]) * Ls)
    herm = iszero(C - C.H)
    return tp and herm and ldl_psd(simp(P * C * P))

IV_L = mp.iv.log(2)
def sign_iv(expr):
    """rigorous sign of a real rational function of ell at ell = log 2 (interval arithmetic)."""
    expr = sp.simplify(sp.expand_complex(sp.expand(expr)))
    assert not expr.has(sp.I), "sign_iv needs a real expression"
    num, den = sp.fraction(sp.together(expr))
    def ev(e):
        poly = sp.Poly(sp.expand(e), ell)
        acc = mp.iv.mpf(0)
        for (k,), c in poly.terms():
            c = sp.Rational(c)
            acc += mp.iv.mpf(int(c.p)) / int(c.q) * IV_L ** k
        return acc
    n, dn = ev(num), ev(den)
    q = n / dn
    if q.a > 0: return 1
    if q.b < 0: return -1
    return 0
# ----------------------------------------------------------------------------------------------
# COPIED VERBATIM from empirical/foundations54/p54q_lindblad_cert.py (mpm, stat witness helpers)
def mpm(M): return mp.matrix([[mp.mpc(complex(sp.N(M[i, j], 70))) if M[i, j].has(I) else mp.mpf(str(sp.N(M[i, j], 70))) for j in range(M.shape[1])] for i in range(M.shape[0])])
def stat(Lh):
    Ls = Lh.H
    A = mp.matrix(5, 4)
    for i in range(4):
        for j in range(4): A[i, j] = Ls[i, j]
    A[4, 0] = 1; A[4, 3] = 1
    b = mp.matrix([0, 0, 0, 0, 1])
    return mp.lu_solve(A.H * A, A.H * b)
# ----------------------------------------------------------------------------------------------

z = sp.symbols("z")
om = sp.symbols("omega", positive=True)
def conjI(x): return x.subs(sp.I, -sp.I)        # all other symbols are real
def rat(x): return sp.cancel(sp.together(sp.expand(x)))   # exact canonical form of a rational function
def Re(x): return rat((x + conjI(x)) / 2)
def Im(x): return rat((x - conjI(x)) / (2 * sp.I))

# EXACT IDENTITY BY EVALUATION (checker method, run 3).  Every z-quantity below is P(z)/det(z - Ls) with deg P <= 4
# (Lt_f is similar to Ls, so det(z - Lt_f) = det(z - Ls)); every omega-quantity is Q(omega)/|det(i omega + Lt_f)|^2
# with deg Q <= 8.  A rational identity of this shape holds identically iff it holds at more points than deg P (deg Q)
# that are not roots of the denominator.  Positive integers z and positive rationals omega are never roots, because
# the generators are primitive (spectrum in Re < 0 except the simple eigenvalue 0).  Evaluations are exact in Q(i)(l).
ZPTS = [sp.Integer(k) for k in range(1, 9)]                 # 8 > 4
WPTS = [sp.Rational(k, 3) for k in range(1, 13)]            # 12 > 8
LTC = {}
def LT(g, f):
    key = (id(g), f)
    if key not in LTC: LTC[key] = g.Lt(f)
    return LTC[key]
INV = {}
def inv_at(key, M):
    if key not in INV: INV[key] = M.inv().applyfunc(rat)
    return INV[key]
def Rhat_at(g, A, s, zv):
    x = inv_at(("R", id(g), zv), zv * sp.eye(4) - g.Ls) * vec(s)
    return rat((vec(A).H * x)[0])
def Chat_at(g, f, A, B, zv):
    Ab, Bb = g.Vbar(A), g.Vbar(B)
    x = inv_at(("C", id(g), f, zv), zv * sp.eye(4) - LT(g, f)) * vec(Bb)
    return rat((vec(Ab).H * g.C[f] * x)[0])
def Aop(g, f, V):
    return unvec(g.A(f) * vec(g.Vbar(V)))
OBS = {"E00": E(0, 0), "sx": sx, "sy": sy}
GRID = {"G": G, "K": K, "N": N}

# ================================================================================================
print("== H1 quantum Agarwal formula R = -dC/dt - C_{A, A V} (Laplace, exact) ==")
ok1 = True
for gn, g in GRID.items():
    for f in FS:
        for vn, V in OBS.items():
            s = g.pot_source(f, V); AV = Aop(g, f, V)
            for an, A_ in OBS.items():
                c0 = g.ip(f, g.Vbar(A_), g.Vbar(V))
                for zv in ZPTS:
                    lhs = Rhat_at(g, A_, s, zv)
                    rhs = c0 - zv * Chat_at(g, f, A_, V, zv) - Chat_at(g, f, A_, AV, zv)
                    ok1 &= rat(lhs - rhs) == 0
check("H1 Rhat_AV(z) == C_AV(0) - z Chat_AV(z) - Chat_{A,A V}(z), 3 gens x 3 metrics x 3 A x 3 V (exact, 8-point degree certificate)", ok1)
# [witness] time domain
mp.mp.dps = 60
okw = True
def mpnum(x):
    x = sp.sympify(x).subs(ell, sp.log(2))
    if x.has(sp.I):
        return mp.mpc(mp.mpf(str(sp.N(sp.re(x), 70))), mp.mpf(str(sp.N(sp.im(x), 70))))   # full precision (K6h lesson)
    return mp.mpf(str(sp.N(x, 70)))
def mpmat(M): return mp.matrix([[mpnum(sp.sympify(M[i, j])) for j in range(M.shape[1])] for i in range(M.shape[0])])
for f in ("SLD", "BKM"):
    g = N
    Ls_, Lt_, Cw = mpmat(g.Ls), mpmat(LT(g, f)), mpmat(g.C[f])
    for vn in ("sx", "E00"):
        V = OBS[vn]; s = mpmat(vec(g.pot_source(f, V))); Vb = mpmat(vec(g.Vbar(V)))
        AV = mpmat(vec(Aop(g, f, V)))
        for an in ("sx", "sy"):
            Ab = mpmat(vec(g.Vbar(OBS[an])))
            for t in (mp.mpf("0.37"), mp.mpf("1.3")):
                Rt = (Ab.H * (mp.expm(t * Ls_) * s))[0]
                Cfun = lambda tt, X: (Ab.H * Cw * (mp.expm(tt * Lt_) * X))[0]
                dC = (Ab.H * Cw * (Lt_ * (mp.expm(t * Lt_) * Vb)))[0]          # analytic d/dt
                okw &= abs(Rt - (-dC - Cfun(t, AV))) < mp.mpf(10) ** -40
check("H1 [witness] time domain at t = 0.37, 1.3 (N; SLD, BKM; mpmath expm, 60 digits)", okw)

# ================================================================================================
print("== H2 violation spectrum ==")
def delta_def_at(g, f, V, wv):
    s = g.pot_source(f, V)
    Ct = 2 * Re(Chat_at(g, f, V, V, -sp.I * wv))
    Rt = Rhat_at(g, V, s, -sp.I * wv)
    return rat(wv / 2 * Ct - Im(Rt))
def delta_G_at(g, f, V, wv):
    Vb = g.Vbar(V)
    x = inv_at(("G", id(g), f, wv), sp.I * wv * sp.eye(4) + LT(g, f)) * (g.A(f) * vec(Vb))
    return rat(-Im(rat((vec(Vb).H * g.C[f] * x)[0])))
ok2 = True; pat2 = {}
for gn, g in GRID.items():
    for f in FS:
        allzero = True
        for vn, V in OBS.items():
            for wv in WPTS:
                d1, d2 = delta_def_at(g, f, V, wv), delta_G_at(g, f, V, wv)
                ok2 &= rat(d1 - d2) == 0
                allzero &= (d1 == 0)
        pat2[(gn, f)] = allzero
pred = {("G", f): True for f in FS}
pred.update({("K", "SLD"): False, ("K", "KMS"): True, ("K", "BKM"): False})
pred.update({("N", f): False for f in FS})
check("H2 Delta_V(omega) == -Im<Vbar,(i omega + Lt)^-1 A Vbar>_f exactly; Delta == 0 for all V <=> f-DB (pattern)",
      ok2 and pat2 == pred, " ".join(f"{k[0]}/{k[1]}:{'0' if v else 'x'}" for k, v in pat2.items()))

# ================================================================================================
print("== H3 sum rules ==")
def lt_inv(g, f, Y):
    row = sp.Matrix([[g.sigma[j, i] for i in range(d) for j in range(d)]])
    u = LT(g, f).col_join(row).gauss_jordan_solve(vec(Y).col_join(sp.Matrix([0])))[0]
    return unvec(u)
def M1(g, f, V):
    Vb = g.Vbar(V)
    return rat(g.ip(f, unvec(g.Lh * vec(Vb)), Aop(g, f, V)))
WB = [E(0, 0), sx, sy]
def gram_traces(g, f):
    Bs = [g.Vbar(B) for B in WB]
    Gm = sp.Matrix(3, 3, lambda k, l: g.ip(f, Bs[k], Bs[l]))
    Nm = sp.Matrix(3, 3, lambda k, l: g.ip(f, unvec(g.Lh * vec(Bs[k])), unvec(g.A(f) * vec(Bs[l]))))
    Pm = sp.Matrix(3, 3, lambda k, l: g.ip(f, unvec(g.A(f) * vec(Bs[k])), unvec(g.A(f) * vec(Bs[l]))))
    Gi = Gm.inv()
    return rat((Gi * Nm.T).trace()), rat((Gi * Pm).trace())
ok3 = True; hs = {}
for gn, g in GRID.items():
    for f in FS:
        for vn, V in OBS.items():
            Vb = g.Vbar(V)
            chi = rat((V * g.respond(g.pot_source(f, V))).trace())
            ok3 &= rat(g.ip(f, Vb, Vb) - chi + g.ip(f, Vb, lt_inv(g, f, Aop(g, f, V)))) == 0
        trN, trP = gram_traces(g, f)
        ok3 &= rat(trN - trP) == 0
        db = iszero(g.A(f))
        ok3 &= (trP == 0) if db else (sign_iv(trP) == 1)
        hs[(gn, f)] = trP
check("H3 [exact] Var - chi == -<Vbar,Lt^-1 A Vbar>; Sum_k M1 == ||A_f||_HS^2 (Gram); zero iff DB, else > 0", ok3,
      " ".join(f"{k[0]}/{k[1]}:{sp.N(v.subs(ell, sp.log(2)), 6)}" for k, v in hs.items()))
mp.mp.dps = 30
def delta_num(g, f, V):
    Lt_, Cw = mpmat(LT(g, f)), mpmat(g.C[f])
    Vb = mpmat(vec(g.Vbar(V))); AV = mpmat(vec(Aop(g, f, V)))
    def Df(w_):
        x = mp.lu_solve(mp.mpc(0, 1) * w_ * mp.eye(4) + Lt_, AV)
        return -mp.im((Vb.H * Cw * x)[0])
    return Df
okq = True; qrep = []
for gn in ("N", "K"):
    g = GRID[gn]
    for f in ("SLD", "BKM"):
        for vn in ("E00", "sx"):
            V = OBS[vn]
            Df = delta_num(g, f, V)
            Vb = g.Vbar(V)
            chi = (V * g.respond(g.pot_source(f, V))).trace()
            m0 = mpnum(rat(g.ip(f, Vb, Vb) - chi))
            m1 = mpnum(M1(g, f, V))
            q0 = 2 / mp.pi * mp.quad(lambda w_: Df(w_) / w_, [0, 1, 10, mp.inf])
            q1 = 2 / mp.pi * mp.quad(lambda w_: w_ * Df(w_), [0, 1, 10, mp.inf])
            okq &= abs(q0 - m0) < mp.mpf(10) ** -20 and abs(q1 - m1) < mp.mpf(10) ** -20
            qrep.append(f"{gn}/{f}/{vn}: m0={mp.nstr(m0, 8)} m1={mp.nstr(m1, 8)}")
check("H3 [witness, 30 digits] (1/pi)Int Delta/omega = Var - chi and (1/pi)Int omega Delta = M1 (N, K; SLD, BKM)", okq, "; ".join(qrep))

# ================================================================================================
print("== H4 classical reduction: overdamped linear Langevin -> Harada-Sasa heat ==")
def langevin(B, T=1):
    S = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"S{min(i,j)}{max(i,j)}"))
    eqs = list(B * S + S * B.T + 2 * T * sp.eye(2))
    sol = sp.solve(eqs, list(S.free_symbols), dict=True)[0]
    S = S.subs(sol)
    Om = B + T * S.inv()
    M1i = [rat((B * S * Om.T)[i, i]) for i in range(2)]
    nu2 = [rat((Om * S * Om.T)[i, i]) for i in range(2)]
    return S, Om, M1i, nu2
B1 = sp.Matrix([[-1, 3], [-1, -2]])
S1, Om1, M1i, nu2 = langevin(B1)
cross = [rat(M1i[i] - nu2[i]) for i in range(2)]
ok4 = all(c != 0 for c in cross) and rat(sum(cross)) == 0 and rat(sum(M1i) - sum(nu2)) == 0 and sum(nu2) > 0
ok4 &= all(rat(cross[i] + Om1[i, i]) == 0 for i in range(2))
kk, ee, TT = sp.symbols("k epsilon T", positive=True)
Jm = sp.Matrix([[0, 1], [-1, 0]])
S2, Om2, M1b, nu2b = langevin(-kk * (sp.eye(2) - ee * Jm), TT)
ok4 &= rat(sum(M1b) - 2 * ee ** 2 * kk * TT) == 0
S3, Om3, M1c, nu2c = langevin(sp.Matrix([[-2, 1], [1, -3]]))
ok4 &= all(rat(x) == 0 for x in M1c) and iszero(Om3)
check("H4 Langevin: per-coordinate cross terms nonzero but sum to 0; Sum M1_i = E|nu|^2; circulating case = 2 eps^2 k T; DB control 0",
      ok4, f"non-normal B: M1={M1i}, E nu_i^2={nu2}, cross={cross}")

# ================================================================================================
print("== H5 Kubo as the reversible-compensated case ==")
ok5 = True
def energy_push(g, f, V):
    return unvec(-g.C[f] * g.S(f) * vec(V)) + sp.I * (V * SIG - SIG * V) / beta
for vn, V in OBS.items():
    s = energy_push(Rg, "BKM", V)
    for an, A_ in OBS.items():
        c0 = Rg.ip("BKM", Rg.Vbar(A_), Rg.Vbar(V))
        for zv in ZPTS:
            lhs = Rhat_at(Rg, A_, s, zv)
            rhs = c0 - zv * Chat_at(Rg, "BKM", A_, V, zv)
            ok5 &= rat(lhs - rhs) == 0
viol_diss = rat(Chat_at(Rg, "BKM", sx, Aop(Rg, "BKM", sx), ZPTS[0]))
s_sld = energy_push(Rg, "SLD", sx)
viol_sld = rat(Rhat_at(Rg, sx, s_sld, ZPTS[0]) - (Rg.ip("SLD", sx, sx) - ZPTS[0] * Chat_at(Rg, "SLD", sx, sx, ZPTS[0])))
ok5 &= viol_diss != 0 and viol_sld != 0
check("H5 energy push (BKM): R = -dC^Kubo/dt exactly; dissipative-only push and SLD energy push violate (V = sigma_x)", ok5,
      f"violations at z=1: dissipative {viol_diss}, SLD {viol_sld}")

# ================================================================================================
print("== H6 frequency-resolved positivity of the total violation spectrum ==")
def delta_tot_at(g, f, wv):
    Bs = [g.Vbar(B) for B in WB]
    Gm = sp.Matrix(3, 3, lambda k, l: g.ip(f, Bs[k], Bs[l]))
    Gi = Gm.inv()
    Mi = inv_at(("G", id(g), f, wv), sp.I * wv * sp.eye(4) + LT(g, f))
    tot = 0
    for l in range(3):
        for m in range(3):
            x = Mi * (g.A(f) * vec(Bs[m]))
            tot += Gi[l, m] * (vec(Bs[l]).H * g.C[f] * x)[0]
    return rat(-Im(rat(tot)))
CELLS = [("K", "SLD"), ("K", "BKM"), ("N", "SLD"), ("N", "KMS"), ("N", "BKM"), ("R", "SLD"), ("H", "SLD")]
DBC = [("G", "SLD"), ("G", "KMS"), ("G", "BKM"), ("K", "KMS")]
ALL = dict(GRID); ALL["R"] = Rg; ALL["H"] = Hh
ok6 = True; rep6 = []
for gn, f in DBC:
    ok6 &= all(delta_tot_at(ALL[gn], f, wv) == 0 for wv in WPTS)
XPTS = [sp.Integer(k) for k in range(1, 13)]          # interpolation nodes (12 > deg Q <= 8)
VPTS = [sp.Rational(2 * k + 1, 7) for k in range(6)]  # independent verification nodes
for gn, f in CELLS:
    g = ALL[gn]
    if not LT(g, f).has(ell) and not g.C[f].has(ell):
        det = sp.expand((sp.I * om * sp.eye(4) + LT(g, f)).det())
        Dd = sp.Poly(sp.expand(det * conjI(det)), om)            # |det(i omega + Lt)|^2, real coefficients
        pts = [(x, delta_tot_at(g, f, x) * Dd.eval(x)) for x in XPTS]
        Qp = sp.Poly(sp.interpolate(pts, om), om)
        okv = all(rat(Qp.eval(x) - delta_tot_at(g, f, x) * Dd.eval(x)) == 0 for x in VPTS)
        pn, pd = Qp, Dd
        while pn.eval(0) == 0 and not pn.is_zero:
            pn = sp.Poly(sp.cancel(pn.as_expr() / om), om)
        while pd.eval(0) == 0 and not pd.is_zero:
            pd = sp.Poly(sp.cancel(pd.as_expr() / om), om)
        rn = pn.count_roots(0, None); rd = pd.count_roots(0, None)
        s1 = sp.sign(pn.eval(1)) * sp.sign(pd.eval(1))
        good = okv and rn == 0 and rd == 0 and s1 == 1 and Qp.degree() <= 8
        rep6.append(f"{gn}/{f}: exact (deg Q={Qp.degree()}, verified={okv}, pos roots num={rn}, den={rd}, sign={s1})")
    else:
        mp.mp.dps = 30
        Lt_, Cw = mpmat(LT(g, f)), mpmat(g.C[f])
        Bs = [g.Vbar(B) for B in WB]
        Gi = sp.Matrix(3, 3, lambda k, l: g.ip(f, Bs[k], Bs[l])).inv()
        Gin = mpmat(Gi); Bv = [mpmat(vec(B)) for B in Bs]; ABv = [mpmat(g.A(f) * vec(B)) for B in Bs]
        def Dtot(w_):
            M = mp.mpc(0, 1) * w_ * mp.eye(4) + Lt_
            tot = 0
            for l in range(3):
                for m in range(3):
                    tot += Gin[l, m] * (Bv[l].H * Cw * mp.lu_solve(M, ABv[m]))[0]
            return -mp.im(tot)
        vals = [Dtot(mp.mpf(10) ** (mp.mpf(-4) + 8 * mp.mpf(k) / 2000)) for k in range(2001)]
        good = all(v > 0 for v in vals)
        rep6.append(f"{gn}/{f}: witness min={mp.nstr(min(vals), 5)}")
    ok6 &= good
check("H6 Delta_tot(omega) > 0 for all omega > 0 in every non-DB cell; == 0 in DB cells", ok6, "; ".join(rep6))

print(f"\nSUMMARY: {sum(res)}/{len(res)} checks passed  ({time.time() - T0:.1f}s)")
