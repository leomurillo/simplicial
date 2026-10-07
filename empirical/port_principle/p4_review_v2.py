"""
Port Principle — P4: settlement of the v2 review (critical-collaborative review, 2026-09-29).
Exact arithmetic (Fraction / sympy) for every pass/fail decision; floats only in labelled witnesses.

PRE-REGISTERED FALSIFIERS (written before the first run; every branch reportable)

R1  Quantifier structure. Wave variables a=(u+y)/2, b=(y-u)/2 give u*y = a^2 - b^2 (power = in - out),
    so "passive for every input" == contraction; every-instant passivity is the same inequality on every
    truncation, hence implies it (strictness witness = P2.S1.K1b). Cayley: sym(K) PSD <=> S=(K-I)(K+I)^-1
    contraction.  K1: identities exact; PSD-sym K gives I - S^T S PSD; non-passive K gives a non-contraction.
    L1: any fails.
R2  Parity defect.  K2a: for ANY rational K, ||S||^2 - ||A||^2 == tr(K^2) (overlap with time reverse).
    K2b: continuum defect == 2 pi <f, Rf>; causal+stable -> 0; STABLE AMPLIFIER (gain 3) -> 0 (gain does
    not break parity); causal-decaying + unstable-pole (real-axis anticausal) mixture -> -4 pi/(g1+g2).
    L2: stable gain gives nonzero defect (then the reviewer's 'restrict to passive' would be right).
R3  Wiener dichotomy.  K3a: time-averaged return probability == sum of squared spectral atoms (exact).
    K3b (float witness): Wigner-Weisskopf ledger average echo ~ delta/(pi Gamma) within 15%.
R4  Complete passivity edge cases and the symmetry axis.
    K4a: H = c I -> every state completely passive (n<=4): theorem needs non-trivial spectrum. (v1 bug)
    K4b: degenerate E=(0,0,1), p=(1/2,1/3,1/6) passive at n=1, becomes active at some n<=4 (pre-reg: n*=3).
    K4c: GGE with mu != 0 is ACTIVE under unrestricted cycles (n=1) but passive under charge-conserving
         cycles for n<=3 (restriction ENLARGES the free family; not a 'fourth quantifier' of demand).
    K4d: a non-GGE state passive under charge-conserving cycles at n=1 becomes active at some n<=5.
    K4e: if E in span{1,q}, every state is passive under charge-conserving cycles (n<=3).
    L4: any branch fails.
R5  Petz family = frequency filters on chi''.  K5a: w_f(x)=(e^{2x}-1)/f(e^{2x}) equals 2tanh x (SLD),
    2x (KM), sinh 2x (RLD), 4tanh(x/2) (WY), and for WYD(alpha) 2 sinh(ax)sinh((1-a)x)/(a(1-a)sinh x).
    K5b (float witness): skew information -1/2 tr[sqrt(rho),A]^2 == (1/pi) int tanh(x/2) chi''; Petz matrix
    formula == filter formula for WY and RLD.  K5c: ordering chain of weights
    coth x - 1/x <= tanh(x/2) <= tanh x <= 2 tanh(x/2) <= x <= sinh(2x)/2 (grid witness; proofs in text).
R6  Non-Abelian ports (exact).  K6a spin-1/2 jump S_z: L*(S_z)=0 but L*(S_x) = -(g/2) S_x (reading z supplies x).
    K6b spin-1: f(S_z) commutes with S_x iff f constant (Schur).  K6c two spins, jump = Casimir J^2:
    L*(S_k)=0 for all k, singlet/triplet coherence decays at 2g.  K6d three spins, collective jumps
    S_z, S_+, S_-: L*(P_sigma) = 0 for all six permutations (multiplicity-space memory protected).
R7  Active ports need a non-passive port.  K7: beam-splitter generator conserves N_a+N_c; squeezer conserves
    N_a-N_c but not w(N_a+N_c); pump term a+ c+ b conserves w_a N_a + w_c N_c + w_p N_b iff w_p = w_a + w_c
    (exact, truncated Fock space).
R8  The coth law.  K8: (r+ + r-)/(r+ - r-) = coth u for r+/r- = e^{2u}; quantum mode Var/(T chi) = x coth x;
    biased ring TUR ratio sigma Var/J^2 = 2u coth u (>= 2 <=> u coth u >= 1); tunnel junction
    S/(2eI) = coth(eV/2kT).
R10 Noise defect is dilation-independent.  K10: any unitary completion [[S,B],[C,D]] has BB^T = I - SS^T;
    a second (rotated) ledger gives the identical added noise, exactly.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
R_ = sp.Rational

# ---------------------------------------------------------------- R1
print("== R1 quantifier structure ==")
u, y = sp.symbols('u y', real=True)
a, b = (u + y) / 2, (y - u) / 2
Kp = sp.Matrix([[2, 1, 0], [-1, 1, R_(1, 2)], [R_(1, 3), 0, 3]])          # sym part PD
Kn = sp.Matrix([[1, 3, 0], [0, -R_(1, 2), 1], [0, 0, 2]])                  # sym part indefinite
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
I3 = sp.eye(3)
Sp_ = (Kp - I3) * (Kp + I3).inv(); Sn_ = (Kn - I3) * (Kn + I3).inv()
check("R1 power = |a|^2-|b|^2; Cayley: passive K -> contraction, non-passive K -> non-contraction",
      sp.expand(u * y - (a ** 2 - b ** 2)) == 0 and ldl_psd((Kp + Kp.T) / 2) and ldl_psd(I3 - Sp_.T * Sp_)
      and not ldl_psd((Kn + Kn.T) / 2) and not ldl_psd(I3 - Sn_.T * Sn_))

# ---------------------------------------------------------------- R2
print("== R2 parity defect = overlap with time reverse ==")
ok = True
for s in range(8):
    K = [[F(((2 * i + 7 * j + s) % 9) - 4, 1 + (i + 2 * j + s) % 5) for j in range(6)] for i in range(6)]
    S2 = sum(((K[i][j] + K[j][i]) / 2) ** 2 for i in range(6) for j in range(6))
    A2 = sum(((K[i][j] - K[j][i]) / 2) ** 2 for i in range(6) for j in range(6))
    trK2 = sum(K[i][j] * K[j][i] for i in range(6) for j in range(6))
    ok &= (S2 - A2 == trK2)
check("R2.K2a ||S||^2 - ||A||^2 == tr(K^2) for arbitrary kernels (8 exact instances)", ok)
w = sp.symbols('w', real=True)
def defect(chi):
    return sp.simplify(sp.integrate(sp.simplify(sp.re(sp.expand_complex(chi)) ** 2 - sp.im(sp.expand_complex(chi)) ** 2), (w, -sp.oo, sp.oo)))
g1, g2 = R_(1), R_(2)
d_causal = defect(1 / (g1 - sp.I * w))
d_amp = defect(3 / (g1 - sp.I * w))
d_anti = defect(-1 / (g2 + sp.I * w))
d_mix = defect(1 / (g1 - sp.I * w) - 1 / (g2 + sp.I * w))
check("R2.K2b defect: causal 0; stable amplifier (gain 3) 0; pure anticausal 0; mixture == -4pi/(g1+g2)",
      d_causal == 0 and d_amp == 0 and d_anti == 0 and sp.simplify(d_mix + 4 * sp.pi / (g1 + g2)) == 0,
      f"causal={d_causal} amp={d_amp} anti={d_anti} mix={d_mix}")

# ---------------------------------------------------------------- R3
print("== R3 Wiener dichotomy ==")
t = sp.symbols('t', real=True)
wts, lam = [R_(1, 2), R_(1, 3), R_(1, 6)], [0, 1, 3]
amp = sum(wk * sp.exp(-sp.I * lk * t) for wk, lk in zip(wts, lam))
avg = sp.simplify(sp.integrate(sp.expand(amp * sp.conjugate(amp)), (t, 0, 2 * sp.pi)) / (2 * sp.pi))
check("R3.K3a time-averaged return probability == sum of squared atoms (exact)", avg == sum(x ** 2 for x in wts), f"{avg}")
Nl, delta, gc, E0 = 801, 0.025, 0.035, 3.0
Ek = (np.arange(Nl) - (Nl - 1) / 2) * delta
Hm = np.zeros((Nl + 1, Nl + 1)); Hm[0, 0] = E0; Hm[0, 1:] = gc; Hm[1:, 0] = gc; Hm[1:, 1:] = np.diag(Ek)
lam_, V = np.linalg.eigh(Hm); ww = V[0, :] ** 2
Gam = 2 * np.pi * gc ** 2 / delta
check("R3.K3b [witness] finite ledger average echo sum w^2 ~ delta/(pi Gamma) -> 0 in the continuum",
      abs(np.sum(ww ** 2) / (delta / (np.pi * Gam)) - 1) < 0.15, f"sum w^2={np.sum(ww**2):.5f}  delta/(pi Gamma)={delta/(np.pi*Gam):.5f}")

# ---------------------------------------------------------------- R4
print("== R4 complete passivity: edge cases and the symmetry axis ==")
def copies(levels, n):          # levels: (E, q, p)
    out = []
    for c in product(levels, repeat=n):
        E = sum(x[0] for x in c); q = sum(x[1] for x in c); p = F(1)
        for x in c: p *= x[2]
        out.append((E, q, p))
    return out
def ergo(block):
    Es = sorted(E for E, _, _ in block); ps = sorted((p for _, _, p in block), reverse=True)
    return sum(p * E for E, _, p in block) - sum(p * E for p, E in zip(ps, Es))
def active(levels, n, restricted):
    C = copies(levels, n)
    if not restricted: return ergo(C) > 0
    return any(ergo([c for c in C if c[1] == qq]) > 0 for qq in set(c[1] for c in C))
def first_active(levels, nmax, restricted):
    for n in range(1, nmax + 1):
        if active(levels, n, restricted): return n
    return None
flat = [(1, 0, F(1, 2)), (1, 0, F(3, 10)), (1, 0, F(1, 5))]
check("R4.K4a H = c I: a non-uniform state is completely passive (n<=4) -> theorem needs non-trivial spectrum",
      first_active(flat, 4, False) is None)
deg = [(0, 0, F(1, 2)), (0, 0, F(1, 3)), (1, 0, F(1, 6))]
nd = first_active(deg, 4, False)
check("R4.K4b degenerate manifold: passive at n=1, uniformity forced by copies (pre-registered n*=3)",
      not active(deg, 1, False) and nd == 3, f"n*={nd}")
Zg = F(1) + F(1, 2) + F(3, 2) + F(3, 8)
gge = [(0, 0, 1 / Zg), (1, 0, F(1, 2) / Zg), (1, 1, F(3, 2) / Zg), (3, 1, F(3, 8) / Zg)]   # 2^-E 3^q
check("R4.K4c GGE (mu != 0): ACTIVE under unrestricted cycles at n=1, PASSIVE under charge-conserving cycles n<=3",
      active(gge, 1, False) and first_active(gge, 3, True) is None)
Zn = F(1) + F(1, 2) + F(1) + F(3, 8)
non = [(0, 0, 1 / Zn), (1, 0, F(1, 2) / Zn), (1, 1, F(1) / Zn), (3, 1, F(3, 8) / Zn)]
nn = first_active(non, 5, True)
check("R4.K4d non-GGE, passive under charge-conserving cycles at n=1, becomes active at some n<=5",
      not active(non, 1, True) and nn is not None, f"n*={nn}")
triv = [(0, 0, F(1, 2)), (0, 0, F(1, 5)), (1, 1, F(1, 5)), (1, 1, F(1, 10))]           # E = q
check("R4.K4e E in span{1,q}: any state passive under charge-conserving cycles (n<=3)",
      first_active(triv, 3, True) is None)

# ---------------------------------------------------------------- R5
print("== R5 Petz family = frequency filters ==")
x, al, tt = sp.symbols('x alpha t', positive=True)
def wf(f): return ((sp.exp(2 * x) - 1) / f.subs(tt, sp.exp(2 * x)))
def same(e1, e2): return sp.simplify((e1 - e2).rewrite(sp.exp)) == 0
fs = {"SLD": ((1 + tt) / 2, 2 * sp.tanh(x)), "KM": ((tt - 1) / sp.log(tt), 2 * x),
      "RLD": (2 * tt / (1 + tt), sp.sinh(2 * x)), "WY": (((1 + sp.sqrt(tt)) / 2) ** 2, 4 * sp.tanh(x / 2))}
ok5 = all(same(sp.simplify(wf(f).subs(sp.log(sp.exp(2 * x)), 2 * x)), target) for f, target in fs.values())
fwyd = lambda A: A * (1 - A) * (tt - 1) ** 2 / ((tt ** A - 1) * (tt ** (1 - A) - 1))
ok5 &= all(same(wf(fwyd(A)), 2 * sp.sinh(A * x) * sp.sinh((1 - A) * x) / (A * (1 - A) * sp.sinh(x)))
           for A in [R_(1, 2), R_(1, 3), R_(1, 5)])
ok5 &= sp.limit(2 * sp.sinh(al * x) * sp.sinh((1 - al) * x) / (al * (1 - al) * sp.sinh(x)), al, 0) == 2 * x
check("R5.K5a w_f(x) = (e^{2x}-1)/f(e^{2x}): SLD 2tanh x, KM 2x, RLD sinh 2x, WY 4tanh(x/2), WYD closed form (alpha->0: KM)", ok5)
rng = np.random.default_rng(7)
n_, beta = 5, 1.1
X = rng.normal(size=(n_, n_)) + 1j * rng.normal(size=(n_, n_)); H = (X + X.conj().T) / 2
Y = rng.normal(size=(n_, n_)) + 1j * rng.normal(size=(n_, n_)); A = (Y + Y.conj().T) / 2
E, U = np.linalg.eigh(H); p = np.exp(-beta * E); p /= p.sum(); Ae = U.conj().T @ A @ U
rho = U @ np.diag(p) @ U.conj().T; sq = U @ np.diag(np.sqrt(p)) @ U.conj().T
skew = -0.5 * np.trace((sq @ A - A @ sq) @ (sq @ A - A @ sq)).real
lines = [(E[j] - E[i], np.pi * (p[i] - p[j]) * abs(Ae[i, j]) ** 2) for i in range(n_) for j in range(n_) if E[j] - E[i] > 1e-12]
xx = lambda om: beta * om / 2
skew_spec = sum(wt / np.pi * np.tanh(xx(om) / 2) for om, wt in lines)
def petz(fun):
    return sum((p[i] - p[j]) ** 2 / (p[j] * fun(p[i] / p[j])) * abs(Ae[i, j]) ** 2 for i in range(n_) for j in range(n_) if i != j)
F_wy = petz(lambda s: ((1 + np.sqrt(s)) / 2) ** 2); F_rld = petz(lambda s: 2 * s / (1 + s))
Fwy_spec = sum(2 / np.pi * 4 * np.tanh(xx(om) / 2) * wt for om, wt in lines)
Frld_spec = sum(2 / np.pi * np.sinh(2 * xx(om)) * wt for om, wt in lines)
check("R5.K5b [witness] skew info == (1/pi) int tanh(x/2) chi''; Petz WY & RLD == (2/pi) int w_f chi''",
      abs(skew - skew_spec) < 1e-10 and abs(F_wy - Fwy_spec) < 1e-9 and abs(F_rld - Frld_spec) < 1e-8,
      f"skew {skew:.10f}/{skew_spec:.10f}  WY {F_wy:.8f}/{Fwy_spec:.8f}  RLD {F_rld:.6f}/{Frld_spec:.6f}")
xs = np.linspace(1e-3, 12, 4000)
chain = [1 / np.tanh(xs) - 1 / xs, np.tanh(xs / 2), np.tanh(xs), 2 * np.tanh(xs / 2), xs, np.sinh(2 * xs) / 2]
check("R5.K5c [witness] weight chain Var_Q <= skew <= F_SLD/4 <= F_WY/4 <= F_KM/4 <= F_RLD/4 on grid",
      all(np.all(chain[k] <= chain[k + 1] + 1e-12) for k in range(5)))

# ---------------------------------------------------------------- R6
print("== R6 non-Abelian ports ==")
def Ls(jumps, X):   # adjoint Lindbladian on observable X (real jumps)
    out = sp.zeros(*X.shape)
    for g, L in jumps:
        out += g * (L.T * X * L - (L.T * L * X + X * L.T * L) / 2)
    return out
sz = sp.Matrix([[R_(1, 2), 0], [0, -R_(1, 2)]]); sx = sp.Matrix([[0, R_(1, 2)], [R_(1, 2), 0]])
gm = R_(3)
check("R6.K6a spin-1/2, jump S_z: L*(S_z)=0 (no z-supply) but L*(S_x) = -(g/2)S_x (reading z supplies x)",
      Ls([(gm, sz)], sz) == sp.zeros(2) and Ls([(gm, sz)], sx) == -gm / 2 * sx)
fvals = sp.symbols('f1 f0 fm')
Sx1 = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2)
comm = sp.simplify(sp.diag(*fvals) * Sx1 - Sx1 * sp.diag(*fvals))
sol = sp.solve(list(comm), list(fvals), dict=True)
check("R6.K6b spin-1 (irreducible): [f(S_z), S_x] = 0 iff f(1)=f(0)=f(-1) (Schur)",
      len(sol) == 1 and len(set(sol[0].get(v, v) for v in fvals)) == 1, f"{sol}")
def kr(*Ms):
    out = Ms[0]
    for M in Ms[1:]: out = sp.kronecker_product(out, M)
    return out
I2 = sp.eye(2); spl = sp.Matrix([[0, 1], [0, 0]]); smi = spl.T
def coll(op, n): return sum((kr(*[op if k == j else I2 for k in range(n)]) for j in range(n)), sp.zeros(2 ** n))
Sz2, Sp2, Sm2 = coll(sz, 2), coll(spl, 2), coll(smi, 2)
Sx2 = (Sp2 + Sm2) / 2
J2 = Sz2 ** 2 + (Sp2 * Sm2 + Sm2 * Sp2) / 2
jc = [(gm, J2)]
singlet = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2); trip0 = sp.Matrix([0, 1, 1, 0]) / sp.sqrt(2)
rho_c = singlet * trip0.T                                    # coherence operator between j=0 and j=1
Lrho = gm * (J2 * rho_c * J2 - (J2 * J2 * rho_c + rho_c * J2 * J2) / 2)
check("R6.K6c Casimir jump J^2: L*(S_z)=L*(S_+)=L*(S_-)=0 (reads j, supplies nothing); j=0/1 coherence decays at 2g",
      all(sp.simplify(Ls(jc, Op)) == sp.zeros(4) for Op in (Sz2, Sp2, Sm2)) and sp.simplify(Lrho + 2 * gm * rho_c) == sp.zeros(4))
Sz3, Sp3, Sm3 = coll(sz, 3), coll(spl, 3), coll(smi, 3)
def perm_matrix(perm):
    P = sp.zeros(8)
    for idx in range(8):
        bits = [(idx >> (2 - k)) & 1 for k in range(3)]
        nb = [bits[perm[k]] for k in range(3)]
        P[sum(bv << (2 - k) for k, bv in enumerate(nb)), idx] = 1
    return P
import itertools
perms = [perm_matrix(pm) for pm in itertools.permutations(range(3))]
j3 = [(R_(2), Sz3), (R_(5), Sp3), (R_(1, 3), Sm3)]
check("R6.K6d three spins, collective S_z,S_+,S_- noise: L*(P_sigma)=0 for all 6 permutations (multiplicity memory protected)",
      all(Ls(j3, P) == sp.zeros(8) for P in perms))

# ---------------------------------------------------------------- R7
print("== R7 active ports need a non-passive port ==")
d = 3
ad = sp.zeros(d);
for k in range(d - 1): ad[k + 1, k] = sp.sqrt(k + 1)
aa = ad.T; Nn = ad * aa; Id = sp.eye(d)
A_, C_, B_ = kr(aa, Id, Id), kr(Id, aa, Id), kr(Id, Id, aa)
Na, Nc, Nb = kr(Nn, Id, Id), kr(Id, Nn, Id), kr(Id, Id, Nn)
Ad, Cd, Bd = A_.T, C_.T, B_.T
com = lambda X, Y: sp.simplify(X * Y - Y * X)
wa, wc = R_(2), R_(3)
bs, sq = Ad * C_ + A_ * Cd, Ad * Cd + A_ * C_
pump = Ad * Cd * B_ + A_ * C_ * Bd
Hp = lambda wp: wa * Na + wc * Nc + wp * Nb
Z27 = sp.zeros(27)
check("R7.K7 BS conserves N_a+N_c; squeezer conserves N_a-N_c not energy; pump term conserves energy iff w_p=w_a+w_c",
      com(Na + Nc, bs) == Z27 and com(Na - Nc, sq) == Z27 and com(wa * Na + wc * Nc, sq) != Z27
      and com(Hp(wa + wc), pump) == Z27 and com(Hp(wa + wc + 1), pump) != Z27)

# ---------------------------------------------------------------- R8
print("== R8 the coth law ==")
uu, kk = sp.symbols('u k', positive=True)
rp, rm = kk * sp.exp(uu), kk * sp.exp(-uu)
c1 = same((rp + rm) / (rp - rm), sp.coth(uu))
A_aff = 2 * uu
J = rp - rm; Dv = rp + rm; sig = J * A_aff
c2 = same(sig * Dv / J ** 2, 2 * uu * sp.coth(uu))
pi_, pj = sp.symbols('p_i p_j', positive=True)
bw = sp.symbols('b', positive=True)                         # b = beta*omega, p_i/p_j = e^{b}
ratio = ((pi_ + pj) / 2) / ((pi_ - pj) / bw)
c3 = same(ratio.subs(pi_, pj * sp.exp(bw)), (bw / 2) * sp.coth(bw / 2))
e_, V_, kT = sp.symbols('e V kT', positive=True)
Gp, Gm = sp.exp(e_ * V_ / (2 * kT)), sp.exp(-e_ * V_ / (2 * kT))
c4 = same((2 * e_ ** 2 * (Gp + Gm)) / (2 * e_ * (e_ * (Gp - Gm))), sp.coth(e_ * V_ / (2 * kT)))
check("R8.K8 coth law: (r+ + r-)/(r+ - r-) = coth u; TUR ratio = 2u coth u; quantum Var/(T chi) = x coth x; S/2eI = coth(eV/2kT)",
      c1 and c2 and c3 and c4)

# ---------------------------------------------------------------- R10
print("== R10 noise defect is dilation-independent ==")
def cayley(Sk):
    I = sp.eye(Sk.shape[0]); return (I - Sk) * (I + Sk).inv()
V1 = cayley(sp.Matrix([[0, R_(1, 2), R_(-1, 3)], [R_(-1, 2), 0, R_(1, 4)], [R_(1, 3), R_(-1, 4), 0]]))
W1 = cayley(sp.Matrix([[0, R_(-2, 5), R_(1, 7)], [R_(2, 5), 0, R_(3, 8)], [R_(-1, 7), R_(-3, 8), 0]]))
V2 = cayley(sp.Matrix([[0, R_(3, 4), R_(1, 5)], [R_(-3, 4), 0, R_(-2, 3)], [R_(-1, 5), R_(2, 3), 0]]))
sig_, dsg = [R_(3, 5), R_(5, 13), R_(8, 17)], [R_(4, 5), R_(12, 13), R_(15, 17)]
S = V1 * sp.diag(*sig_) * W1
D_ = W1.T * sp.diag(*dsg) * W1; Ds_ = V1 * sp.diag(*dsg) * V1.T
U1 = sp.BlockMatrix([[S, Ds_], [D_, -S.T]]).as_explicit()
# RUN LOG (2026-09-29): first run FAILED "U2 orthogonal" — cause: a stray .applyfunc(sp.nsimplify) here
# re-approximated large exact rationals (checker bug, not mathematics: V2 and diag(I,V2) verified orthogonal
# separately; corner/noise/formula sub-checks passed). Removed; U2 is now built in exact arithmetic only.
U2 = sp.diag(sp.eye(3), V2) * U1 * sp.diag(sp.eye(3), V2.T)
th = R_(7, 3)
def added(U):
    B = U[:3, 3:]; return B * (th * sp.eye(3)) * B.T
check("R10.K10 two different lossless ledgers: both orthogonal, same S corner, identical added noise theta(I - S S^T)",
      sp.simplify(U1.T * U1) == sp.eye(6) and sp.simplify(U2.T * U2) == sp.eye(6) and U2[:3, :3] == S
      and sp.simplify(added(U1) - added(U2)) == sp.zeros(3) and sp.simplify(added(U1) - th * (sp.eye(3) - S * S.T)) == sp.zeros(3))

print(f"\n{sum(res)}/{len(res)} GREEN")
