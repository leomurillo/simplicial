r"""
Paper 54, section 4.1 -- the quantum arrow (Lindblad version of Theorem 3).  Certificate p54q_lindblad_cert.py
=============================================================================================================
Exact arithmetic decides every vanishing / equality: sympy Rational and the field Q(l, i), with l = log 2 kept
as a positive SYMBOL (an identity in l is stronger than one at l = log 2).  Strict signs are decided by RIGOROUS
interval arithmetic (mpmath.iv) at l = log 2.  Floats appear only in lines labelled [witness].  No torch.

SETTING (qubit, basis |0>, |1>):  sigma = diag(4,1)/5, so log(p0/p1) = 2l.  On matrix units E_ij the Petz
multiplications Gamma_f are diagonal with weights
    c_SLD = (p_i+p_j)/2,   c_KMS = sqrt(p_i p_j),   c_BKM = (p_i-p_j)/(log p_i - log p_j)  (= p_i on the diagonal),
and the GNS weight is p_j (right multiplication).  <X,Y>_f = tr(X^dag Gamma_f Y).  For a Lindbladian with Heisenberg
generator Lh:  f-time reversal  Lt_f = Gamma_f^{-1} Ls Gamma_f,  S_f = (Lh + Lt_f)/2,  A_f = (Lh - Lt_f)/2;
f-detailed balance (f-DB) <=> A_f = 0.  An "f-potential perturbation by V" has source  s = L'(sigma) = -Gamma_f S_f V;
the static response sigma' solves Ls sigma' = -s, tr sigma' = 0, and chi(A) = tr(A sigma').
Generators:
    L_G = 4 D[s-] + D[s+] + D[s_z]                     (Davies-type pure dissipator; s- = |0><1|)
    L_N = D[M] - i[H,.] + kappa (tau tr(.) - id),       M = [[1,1],[0,1]], H = sigma_x/2,
          tau = sigma - (D[M] - i[H,.])(sigma)/kappa,   kappa = least of {1,2,4,8,16} with tau >= 0
    L_K = KMS-symmetrization of L_N:  Lh_K = (Lh_N + Lt_{N,KMS})/2
    L_R = L_G + i[K,.] (Heisenberg),  K = diag(0,1), sigma = e^{-beta K}/Z with beta = 2l
    L_H = i[sigma_x,.] + D[s_z]^dag  on sigma = 1/2     (hypocoercive control)

PRE-REGISTERED FALSIFIERS (written 2026-10-01 BEFORE the first run; every branch is reportable)
------------------------------------------------------------------------------------------------
K6a  Theorem 3Q(a): for f in {SLD, KMS, BKM} and generators {L_G, L_K, L_N}, V in the Hermitian basis
     {E00, E11, sigma_x, sigma_y}: the DIRECT solve (route i) equals the closed form
     sigma' = Gamma_f( Vbar + Lt_f^{-1} A_f Vbar )  (route ii), identically in l.   L: any mismatch.
K6b  The jump tilt is the SLD potential perturbation.
     (i)  d/de at 0 of  Lh_e = K_e^{-1} Lh K_e - (1/2){(K_e^{-1} Lh K_e)(1), .},  K_e(X) = e^{eV/4} X e^{eV/4},
          equals the Jordan carre du champ  (1/2)[Lh(V o X) - V o Lh(X) - X o Lh(V)]  (all three generators, all V);
     (ii) its source equals -Gamma_SLD S_SLD V  (all three generators, all V);
     (iii) on the classical part 4D[s-]+D[s+] with V = diag(v0,v1) the population block is the theta=1/2 rate
          tilt w_xy (V_y - V_x)/2 of Paper 54 Theorem 3;
     (iv) at finite tilt eV/4 = l sigma_x (e^{l sigma_x} = (5I+3 sigma_x)/4, exact) Lh_e on L_G is unital, its
          Schroedinger dual is trace preserving, and its Choi matrix is conditionally positive (a Lindbladian).
     L: any failure.
K6c  Detailed-balance hierarchy (joint on disjoint: L_K satisfies one f and violates two).
     L_G: GNS-symmetric, commutes with the modular superoperator, A_f = 0 for f in {SLD, KMS, BKM}.
     L_K: a valid Lindbladian (unital, TP, conditionally CP) with sigma stationary; A_KMS = 0, A_SLD != 0,
          A_BKM != 0, not GNS-symmetric.
     L_N: sigma its unique stationary state; A_f != 0 for all three f.
     L: any branch different.
K6d  Theorem 3Q(c)-(d) on the 3 x 3 grid {G,K,N} x {SLD,KMS,BKM}: chi(A) = <A,Vbar>_f for all A,V  <=>  f-DB
     <=> f-response matrix symmetric <=> Cramer-Rao equality chi(V)^2 = <Vbar,Vbar>_f I_f(V) for all V.
     PREDICTED DB pattern (SLD,KMS,BKM): G = (T,T,T), K = (F,T,F), N = (F,F,F); in every non-DB cell some V
     gives a strict Cramer-Rao inequality (interval-certified).   L: any cell off the pattern.
K6e  Two tilts on L_G (GNS-DB).  Kinetic (jump) tilt: sigma' = J_sigma(Vbar) = (sigma Vbar + Vbar sigma)/2 for all V.
     Free-energy (BKM) tilt: sigma' = Gamma_BKM(Vbar) for all V.  PREDICTED for V = sigma_x:
         chi_kin(sigma_x) - chi_th(sigma_x) = 1 - 3/(5 l)   (= quantum variance, > 0),
     and = 0 for diagonal V.  [witness] the true Gibbs tilt exp(log sigma + e sigma_x)/Z and the true finitely
     jump-tilted L_G (exact exponentials, mpmath 60 digits, e = 1e-25) reproduce Gamma_BKM(sigma_x) and
     J_sigma(sigma_x) by finite difference to relative 1e-15.   L: any failure.
K6f  Reversible part.  i[K,.] is f-antisymmetric for SLD, KMS, BKM and GNS.  On L_R, the energy tilt (BKM source
     on the dissipator + K -> K - V/beta) gives sigma' = Gamma_BKM(Vbar) for every V in the basis; the same
     construction in the SLD and KMS conventions FAILS for V = sigma_x.  Uniqueness: (1-t)/f(t) = -log t holds for
     f_BKM and fails (interval-certified at t = 4) for f_SLD, f_KMS.   L: any failure.
K6g  Hypocoercive control L_H: unique stationary state, primitive (every nonzero eigenvalue has negative real
     part), yet ker S has dimension 2 > 1 (lambda_S = 0: the bound of 3Q(b) is vacuous); A != 0 and the response
     matrix is not symmetric (3Q(c) still decides).   L: any failure.

RUN LOG (append-only; failures retained)
---------------------------------------
Pre-run code fixes (before run 1, falsifiers untouched): removed two sp.nsimplify calls and a third in the sign
  helper (the K3d lesson of p54_cert.py: sympy evaluates sqrt of rational squares exactly; no canonicalizer).
Run 1 (2026-10-01, blind; p54q_run1.log): 11/11, 26 s.  kappa = 1, tau = [[3/5, 3/10 - 3i/10],[3/10 + 3i/10, 2/5]].
  Every pre-registered prediction held: the DB pattern G=(T,T,T), K=(F,T,F), N=(F,F,F); chi_kin - chi_th
  (sigma_x) = 1 - 3/(5l); energy-tilt neutrality for BKM only; hypocoercive spectrum {0, -2, -1 +- i sqrt3}.
  Treated as suspect (all-positive): K6a's two routes share objects, and the only numerically independent route
  ran on the equilibrium generator.
Run 2 (2026-10-01; p54q_run2.log): 13/13, 33 s.  Adds K6h, POST-RUN and NOT BLIND: (1) the true finitely
  jump-tilted L_N and L_K reproduce route (i) by finite difference (max abs err 1.3e-17; the complex generator
  entries enter this witness at double precision, which sets that floor); (2) the 3Q(b) bound holds on L_N, L_K
  for all three metrics (max lhs/rhs = 0.981: nearly tight).
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
# COPIED VERBATIM from empirical/foundations54/p54_cert.py (itself verbatim from P5 / P4)
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

# ================================================================================================
print("== K6a Theorem 3Q(a): direct solve == closed form ==")
ok = True
for gname, g in GENS.items():
    ok &= stationary_ok(g)
    for f in FS:
        for vn, V in BASIS.items():
            s1 = g.respond(g.pot_source(f, V)); s2 = g.route_ii(f, V)
            ok &= iszero(s1 - s2)
check("K6a sigma' (direct) == Gamma_f(Vbar + Lt_f^-1 A_f Vbar), 3 generators x 3 metrics x 4 V, identically in l", ok)

# ================================================================================================
print("== K6b the jump tilt is the SLD potential perturbation ==")
eps = sp.symbols("eps")
def jordan_cdc(Lh, V):
    Lop = lambda X: unvec(Lh * vec(X))
    jo = lambda A, B: (A * B + B * A) / 2
    return superop(lambda X: (Lop(jo(V, X)) - jo(V, Lop(X)) - jo(X, Lop(V))) / 2)
def tilted(Lh, Kf, Kinv):
    Kp = superop(Kf); Ki = superop(Kinv)
    Psi = Ki * Lh * Kp
    Psi1 = unvec(Psi * vec(Id))
    return Psi - superop(lambda X: (Psi1 * X + X * Psi1) / 2)
okb1 = okb2 = True
for gname, g in GENS.items():
    for vn, V in BASIS.items():
        a = Id + eps * V / 4; ai = Id - eps * V / 4
        Le = tilted(g.Lh, lambda X: a * X * a, lambda X: ai * X * ai)
        d1 = simp(Le.diff(eps).subs(eps, 0))
        J1 = simp(jordan_cdc(g.Lh, V))
        okb1 &= iszero(d1 - J1)
        src = unvec(J1.H * vec(g.sigma))
        okb2 &= iszero(src - g.pot_source("SLD", V))
check("K6b(i) d/de of the tilted generator == Jordan carre du champ (3 generators x 4 V)", okb1)
check("K6b(ii) its source == -Gamma_SLD S_SLD V: the jump tilt is the SLD potential perturbation", okb2)
v0, v1 = sp.symbols("v0 v1", real=True)
Lcl = superop(total(lambda r: 4 * Dis(sm)(r), Dis(spl))).H
Jcl = jordan_cdc(simp(Lcl), sp.diag(v0, v1))
pop = [0, 3]
blk = sp.Matrix(2, 2, lambda a, b: Jcl[pop[a], pop[b]])
w = {(1, 0): 4, (0, 1): 1}
Vv = [v0, v1]
cl = sp.zeros(2, 2)
for (x, y), r in w.items():
    cl[x, y] += r * (Vv[y] - Vv[x]) / 2; cl[x, x] -= r * (Vv[y] - Vv[x]) / 2
check("K6b(iii) classical reduction: population block == theta=1/2 rate tilt of Paper 54 Thm 3", iszero(blk - cl),
      f"block={blk.tolist()}")
ea = (5 * Id + 3 * sx) / 4; eai = (5 * Id - 3 * sx) / 4          # e^{+-l sigma_x}, exact
assert simp(ea * eai) == Id
LeF = simp(tilted(G.Lh, lambda X: ea * X * ea, lambda X: eai * X * eai))
okb4 = iszero(LeF * vec(Id)) and choi_ccp(simp(LeF.H))
check("K6b(iv) finite jump tilt (e^{l sigma_x}, exact) of L_G is a Lindbladian: unital, TP, conditionally CP", okb4)

# ================================================================================================
print("== K6c detailed-balance hierarchy ==")
CG = G.C["GNS"]
gns_G = iszero(CG * G.Lh - (CG * G.Lh).H)
Dmod = sp.diag(*[P0[i] / P0[j] for i in range(d) for j in range(d)])
mod_G = iszero(G.Lh * Dmod - Dmod * G.Lh)
dbG = [iszero(G.A(f)) for f in FS]
validK = choi_ccp(K.Ls) and iszero(K.Lh * vec(Id)) and stationary_ok(K)
dbK = [iszero(K.A(f)) for f in FS]
gns_K = iszero(CG * K.Lh - (CG * K.Lh).H)
dbN = [iszero(N.A(f)) for f in FS]
validN = choi_ccp(N.Ls) and stationary_ok(N)
okc = (gns_G and mod_G and dbG == [True, True, True] and validK and dbK == [False, True, False] and not gns_K
       and validN and dbN == [False, False, False] and choi_ccp(G.Ls))
check("K6c GNS-DB => all f-DB (L_G); KMS-DB but not SLD/BKM/GNS (L_K, a valid Lindbladian); none (L_N)", okc,
      f"G:{dbG} gns={gns_G} mod={mod_G} | K:{dbK} gns={gns_K} valid={validK} | N:{dbN} valid={validN}")

# ================================================================================================
print("== K6d Theorem 3Q(c)-(d) on the 3x3 grid ==")
pattern, okd = {}, True
for gname, g in GENS.items():
    for f in FS:
        db = iszero(g.A(f))
        names = list(BASIS)
        Mresp = sp.zeros(4, 4); fdt = True; cr_eq_all = True; cr_strict_some = False
        for b_, vn in enumerate(names):
            V = BASIS[vn]; sig1 = g.respond(g.pot_source(f, V)); Vb = g.Vbar(V)
            h = unvec(g.C[f].inv() * vec(sig1))          # f-representation of sigma'
            for a_, an in enumerate(names):
                A_ = BASIS[an]
                chi = sp.simplify((A_ * sig1).trace())
                Mresp[a_, b_] = chi
                fdt &= sp.simplify(chi - g.ip(f, A_, Vb)) == 0
            chiV = sp.simplify((V * sig1).trace())
            gap = sp.simplify(g.ip(f, Vb, Vb) * g.ip(f, h, h) - chiV ** 2)
            if sp.simplify(gap) != 0:
                cr_eq_all = False
                if sign_iv(gap) == 1: cr_strict_some = True
        sym = iszero(Mresp - Mresp.T)
        pattern[(gname, f)] = db
        cell_ok = (fdt == db) and (sym == db) and (cr_eq_all == db) and (db or cr_strict_some)
        okd &= cell_ok
pred = {("G", f): True for f in FS}
pred.update({("K", "SLD"): False, ("K", "KMS"): True, ("K", "BKM"): False})
pred.update({("N", f): False for f in FS})
okd &= (pattern == pred)
check("K6d FDT <=> f-DB <=> symmetric response <=> Cramer-Rao equality, on all 9 cells; pattern as predicted", okd,
      " ".join(f"{k[0]}/{k[1]}:{'DB' if v else '--'}" for k, v in pattern.items()))

# ================================================================================================
print("== K6e two tilts on L_G: kinetic -> SLD (watching), free energy -> Kubo-Mori (pushing) ==")
oke = True
for vn, V in BASIS.items():
    Vb = G.Vbar(V)
    kin = G.respond(unvec(jordan_cdc(G.Lh, V).H * vec(SIG)))
    th = G.respond(G.pot_source("BKM", V))
    oke &= iszero(kin - (SIG * Vb + Vb * SIG) / 2) and iszero(th - G.Gam("BKM", Vb))
    diff = sp.simplify(((V * kin).trace() - (V * th).trace()))
    if vn == "sx":
        oke &= sp.simplify(diff - (1 - R(3, 5) / ell)) == 0 and sign_iv(diff) == 1
        dsx = diff
    if vn in ("E00", "E11"):
        oke &= (diff == 0)
check("K6e kinetic tilt sigma' = J_sigma(Vbar); BKM tilt sigma' = Gamma_BKM(Vbar); chi_kin - chi_th (sigma_x) = 1 - 3/(5l) > 0",
      oke, f"diff(sigma_x) = {dsx}")
# [witness] true Gibbs tilt and true finite jump tilt, mpmath
mp.mp.dps = 60
def mpm(M): return mp.matrix([[mp.mpc(complex(sp.N(M[i, j], 70))) if M[i, j].has(I) else mp.mpf(str(sp.N(M[i, j], 70))) for j in range(M.shape[1])] for i in range(M.shape[0])])
ep = mp.mpf(10) ** -25
Lsig = mp.diag([mp.log(mp.mpf(4) / 5), mp.log(mp.mpf(1) / 5)])
sxm = mp.matrix([[0, 1], [1, 0]])
def gibbs(e):
    X = mp.expm(Lsig + e * sxm); return X / (X[0, 0] + X[1, 1])
fd_g = (gibbs(ep) - gibbs(0)) / ep
pred_g = (mp.mpf(3) / 5) / (2 * mp.log(2))                    # Gamma_BKM(sigma_x) off-diagonal entry
okw = abs(fd_g[0, 1] - pred_g) < mp.mpf(10) ** -15
# true finite jump tilt of L_G, numerically: jumps conjugated by e^{e V/4}, generator built from the tilted map
def Lh_num(e):
    a = mp.expm(e * sxm / 4); ai = mp.expm(-e * sxm / 4)
    Lh = mpm(G.Lh)
    def sup(F):
        M = mp.matrix(4, 4)
        for k in range(4):
            Ek = mp.matrix(2, 2); Ek[k // 2, k % 2] = 1
            Y = F(Ek)
            for i in range(2):
                for j in range(2): M[2 * i + j, k] = Y[i, j]
        return M
    Kp = sup(lambda X: a * X * a); Ki = sup(lambda X: ai * X * ai)
    Psi = Ki * Lh * Kp
    v1 = mp.matrix([1, 0, 0, 1]); p1 = Psi * v1
    P1 = mp.matrix([[p1[0], p1[1]], [p1[2], p1[3]]])
    return Psi - sup(lambda X: (P1 * X + X * P1) / 2)
def stat(Lh):
    Ls = Lh.H
    A = mp.matrix(5, 4)
    for i in range(4):
        for j in range(4): A[i, j] = Ls[i, j]
    A[4, 0] = 1; A[4, 3] = 1
    b = mp.matrix([0, 0, 0, 0, 1])
    return mp.lu_solve(A.H * A, A.H * b)
fd_k = (stat(Lh_num(ep)) - stat(Lh_num(0))) / ep
okw &= abs(fd_k[1] - mp.mpf(1) / 2) < mp.mpf(10) ** -15      # J_sigma(sigma_x) = sigma_x / 2
check("K6e [witness] true Gibbs tilt -> Gamma_BKM(sigma_x); true finite jump tilt -> J_sigma(sigma_x) (60 digits)", okw,
      f"Gibbs coherence {mp.nstr(fd_g[0,1],12)} vs {mp.nstr(pred_g,12)}; jump-tilt coherence {mp.nstr(fd_k[1],12)} vs 0.5")

# ================================================================================================
print("== K6f the reversible part: FDT-neutral exactly in the Kubo-Mori metric ==")
okf = True
for f in ("SLD", "KMS", "BKM", "GNS"):
    C = G.C[f]
    okf &= iszero(C * adK_h + (C * adK_h).H)
res_f = {}
for f in FS:
    good = True
    for vn, V in BASIS.items():
        Vb = Rg.Vbar(V)
        s_diss = unvec(-Rg.C[f] * Rg.S(f) * vec(V))
        s_K = I * (V * SIG - SIG * V) / beta                      # d/de of -i[K - eV/beta, sigma]
        sig1 = Rg.respond(s_diss + s_K)
        good &= iszero(sig1 - Rg.Gam(f, Vb))
    res_f[f] = good
okf &= res_f == {"SLD": False, "KMS": False, "BKM": True}
t = sp.Integer(4)
uq = {"BKM": sp.simplify((1 - t) / ((t - 1) / (2 * ell)) + 2 * ell),
      "SLD": (1 - t) / ((1 + t) / 2) + 2 * ell, "KMS": (1 - t) / sp.sqrt(t) + 2 * ell}
okf &= (uq["BKM"] == 0) and sign_iv(uq["SLD"]) != 0 and sign_iv(uq["KMS"]) != 0
check("K6f i[K,.] antisymmetric in all four metrics; energy tilt FDT-neutral only for BKM; (1-t)/f = -log t only for BKM",
      okf, f"energy-tilt FDT by metric: {res_f}")

# ================================================================================================
print("== K6g hypocoercive control ==")
uniq = iszero(Hh.Ls * vec(Hh.sigma)) and Hh.Ls.rank() == 3
evs = Hh.Lh.eigenvals()
prim = all(sp.re(ev) < 0 for ev in evs if ev != 0) and list(evs).count(0) <= 1 and evs.get(0, 0) == 1
S_H = Hh.S("SLD"); kerS = 4 - S_H.rank()
A_H = Hh.A("SLD")
Mh = sp.zeros(4, 4)
names = list(BASIS)
for b_, vn in enumerate(names):
    sig1 = Hh.respond(Hh.pot_source("SLD", BASIS[vn]))
    for a_, an in enumerate(names):
        Mh[a_, b_] = sp.simplify((BASIS[an] * sig1).trace())
okg = uniq and prim and kerS == 2 and not iszero(A_H) and not iszero(Mh - Mh.T)
check("K6g hypocoercive: primitive, unique sigma, dim ker S = 2 (bound vacuous), A != 0, response not symmetric", okg,
      f"eigenvalues={list(evs)}  dim ker S={kerS}")

# ================================================================================================
# K6h -- POST-RUN CROSS-CHECK, NOT BLIND (added after run 1 returned 11/11; written before running it).
# Why: K6a compares two routes built from the same objects, and the only numerically independent route in run 1
# was on the equilibrium generator L_G.  Here (1) the TRUE finitely jump-tilted NON-equilibrium generators L_N and
# L_K (exact exponentials, mpmath 60 digits) must reproduce route (i) with the SLD source by finite difference,
# and (2) the bound of Theorem 3Q(b), not pre-registered, is tested where lambda_f > 0.
print("== K6h [post-run, NOT blind] independent cross-checks on non-equilibrium generators ==")
def Lh_num_gen(g, V, e):
    a = mp.expm(e * mpm(V) / 4); ai = mp.expm(-e * mpm(V) / 4)
    Lh = mpm(g.Lh)
    def sup(F):
        M = mp.matrix(4, 4)
        for k in range(4):
            Ek = mp.matrix(2, 2); Ek[k // 2, k % 2] = 1
            Y = F(Ek)
            for i in range(2):
                for j in range(2): M[2 * i + j, k] = Y[i, j]
        return M
    Kp = sup(lambda X: a * X * a); Ki = sup(lambda X: ai * X * ai)
    Psi = Ki * Lh * Kp
    p1 = Psi * mp.matrix([1, 0, 0, 1])
    P1 = mp.matrix([[p1[0], p1[1]], [p1[2], p1[3]]])
    return Psi - sup(lambda X: (P1 * X + X * P1) / 2)
okh = True; worst = mp.mpf(0)
for gname in ("N", "K"):
    g = GENS[gname]
    for vn in ("sx", "sy", "E00"):
        V = BASIS[vn]
        pred = g.respond(g.pot_source("SLD", V))
        fd = (stat(Lh_num_gen(g, V, ep)) - stat(Lh_num_gen(g, V, 0))) / ep
        for k in range(4):
            ex = mp.mpc(complex(sp.N(pred[k // 2, k % 2], 70)))
            err = abs(fd[k] - ex); worst = max(worst, err)
            okh &= err < mp.mpf(10) ** -15
check("K6h(1) [post-run, NOT blind] true finite jump tilt of L_N and L_K reproduces route (i) (SLD source)", okh,
      f"max abs err {mp.nstr(worst, 3)}")
okb = True; ratios = []
for gname in ("N", "K"):
    g = GENS[gname]
    for f in FS:
        Sm = g.S(f).subs(ell, sp.log(2)); Am = g.A(f).subs(ell, sp.log(2))
        Cm = g.C[f].subs(ell, sp.log(2))
        Ch = mp.matrix([[mp.sqrt(mp.mpf(str(sp.N(Cm[i, i], 70)))) if i == j else 0 for j in range(4)] for i in range(4)])
        Chi = Ch ** -1
        Ssym = Ch * mpm(Sm) * Chi; Asym = Ch * mpm(Am) * Chi
        evS = sorted(-mp.re(x) for x in mp.eig(Ssym)[0])
        lam = [x for x in evS if x > mp.mpf(10) ** -40][0]
        nA = max(mp.sqrt(abs(x)) for x in mp.eig(Asym.H * Asym)[0])
        for vn in ("sx", "sy", "E00"):
            V = BASIS[vn]; Vb = g.Vbar(V)
            sig1 = g.respond(g.pot_source(f, V)).subs(ell, sp.log(2))
            h = unvec(Cm.inv() * vec(sig1))
            u = h - Vb
            nu = mp.sqrt(abs(mp.mpc(complex(sp.N(g.ip(f, u, u).subs(ell, sp.log(2)), 70)))))
            nV = mp.sqrt(abs(mp.mpc(complex(sp.N(g.ip(f, Vb, Vb).subs(ell, sp.log(2)), 70)))))
            okb &= nu <= nA * nV / lam * (1 + mp.mpf(10) ** -30)
            if nV > 0 and nA > 0: ratios.append(float(nu / (nA * nV / lam)))
check("K6h(2) [post-run, NOT blind] Theorem 3Q(b): ||h - Vbar||_f <= ||A_f|| ||Vbar||_f / lambda_f (L_N, L_K; 3 metrics)", okb,
      f"max lhs/rhs = {max(ratios):.4f}")

print(f"\nSUMMARY: {sum(res)}/{len(res)} checks passed  ({time.time() - T0:.1f}s)")
