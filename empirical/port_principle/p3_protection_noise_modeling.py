"""
Port Principle — P3: protection, noise-as-defect, and the modeling calculus.
Exact arithmetic (Fraction / sympy Rational); no float enters any pass/fail decision.

PRE-REGISTERED FALSIFIERS (written before the run; every branch is reportable)

N1  Noise = temperature x squared dilation defect (classical Kirchhoff/Bosma form).
    K1a: the Halmos ledger U=[[S,D*],[D,-S^T]] is exactly orthogonal and the port's added
         noise is theta*(I - S S^T) exactly.
    K1b: at uniform temperature (incident = theta I) the output is theta I exactly
         (a passive port is invisible in equilibrium).
    K1c: reciprocal S (S=S^T): emissivity_i == absorptivity_i for every port;
         nonreciprocal S: some e_i != a_i but sum e == sum a exactly.
    L1:  any of the above fails -> "noise is the dilation defect" is wrong as stated.
N2  Quantum noise defect, passive and active in one formula.
    K2a: a phase-insensitive Gaussian channel (tau, N) is completely positive iff
         N >= |1 - tau|/2   (eigenvalues of the CP matrix are N +- (1-tau)/2).
    K2b: beam-splitter (tau<1) and two-mode-squeezer (tau>1) dilations with a thermal
         hidden mode give N = |1 - tau| (n + 1/2), saturating K2a at n = 0 (Caves).
    K2c: n + 1/2 = (1/2) coth(hbar w / 2kT) -> kT/(hbar w) classically (same coth as FDT).
    L2:  mismatch in any.
N3  The port-charge table (Noether charge Q of a logical bit; gauge qubit alongside).
    K3a neither supply nor read (gauge-only jumps): logical reduced state is EXACTLY invariant.
    K3b read-only (jump = Q): logical populations and <Q> invariant; logical coherence
        decays at exactly gamma/2 (QND watching = dephasing).
    K3c supply (sigma-, sigma+ with KMS ratio r = e^{-beta Delta}): dp1/dt = gamma r p0 - gamma p1;
        stationary p1/p0 = r exactly (flips need the environment to supply the charge; gapped
        carriers => rate proportional to e^{-beta Delta}).
    K3d combined: coherence rate = Gamma1/2 + Gamma_phi exactly (T1/T2 split = supply/read split).
    L3: any identity fails.
N5  Modeling calculus (port-Hamiltonian closure).
    K5a energy balance: sym part of Q(J-R)Q == -QRQ  (dH/dt = -x'QRQx + y'u).
    K5b power-conserving interconnection u1=-y2, u2=y1 yields J_c skew, R_c PSD exactly.
    K5c effort-constraint reduction W=QV(V'QV)^-1: J_r skew, R_r PSD, Q_r PD exactly, and
        Re G_r(i w) >= 0 at test frequencies (reduced model positive-real).
    L5: any fails.
N6  Local FDT => port FDT for ANY readout (Levin's direct approach), exact.
    K6: -Im(p'Gp) == w * p' G C conj(G) p, hence component noise 4kT C at every damper gives
        the readout spectrum (4kT/w)|Im chi_pp| = 8kT W_diss/(w^2 F0^2).
    L6: mismatch.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

res = []
def check(name, ok, detail=""):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(r) for r in zip(*A)]
def eye(d): return [[F(int(i == j)) for j in range(d)] for i in range(d)]
def add(A, B, s=1): return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scal(c, A): return [[c * x for x in r] for r in A]
def diag(v): return [[v[i] if i == j else F(0) for j in range(len(v))] for i in range(len(v))]
def cayley(S):
    d = len(S); I = eye(d)
    M = sp.Matrix([[I[i][j] + S[i][j] for j in range(d)] for i in range(d)]).inv()
    Mi = [[F(int(sp.fraction(M[i, j])[0]), int(sp.fraction(M[i, j])[1])) for j in range(d)] for i in range(d)]
    return mm([[I[i][j] - S[i][j] for j in range(d)] for i in range(d)], Mi)

# ---------------------------------------------------------------- N1
print("== N1 noise = temperature x squared dilation defect ==")
V = cayley([[F(0), F(1, 2), F(-1, 3)], [F(-1, 2), F(0), F(1, 4)], [F(1, 3), F(-1, 4), F(0)]])
W = cayley([[F(0), F(-2, 5), F(1, 7)], [F(2, 5), F(0), F(3, 8)], [F(-1, 7), F(-3, 8), F(0)]])
sig, dsg = [F(3, 5), F(5, 13), F(8, 17)], [F(4, 5), F(12, 13), F(15, 17)]
def ledger(S, Vl, Wr):
    D = mm(mm(tr(Wr), diag(dsg)), Wr); Ds = mm(mm(Vl, diag(dsg)), tr(Vl))
    U = [[F(0)] * 6 for _ in range(6)]
    for i in range(3):
        for j in range(3):
            U[i][j] = S[i][j]; U[i][3 + j] = Ds[i][j]; U[3 + i][j] = D[i][j]; U[3 + i][3 + j] = -S[j][i]
    return U
theta = F(7, 3)
for label, S, Vl, Wr in [("nonreciprocal", mm(mm(V, diag(sig)), W), V, W),
                         ("reciprocal", mm(mm(V, diag(sig)), tr(V)), V, tr(V))]:
    U = ledger(S, Vl, Wr)
    orth = mm(tr(U), U) == eye(6)
    Sa = [[F(1), F(1, 2), F(0)], [F(1, 2), F(2), F(-1, 3)], [F(0), F(-1, 3), F(3, 2)]]   # arbitrary incident covariance
    Sin = [[F(0)] * 6 for _ in range(6)]
    for i in range(3):
        for j in range(3): Sin[i][j] = Sa[i][j]
        Sin[3 + i][3 + i] = theta
    out = [r[:3] for r in mm(mm(U, Sin), tr(U))[:3]]
    pred = add(mm(mm(S, Sa), tr(S)), scal(theta, add(eye(3), mm(S, tr(S)), -1)))
    check(f"N1.K1a [{label}] ledger orthogonal & added noise == theta (I - S S^T)", orth and out == pred)
    Sin_eq = [[theta if i == j else F(0) for j in range(6)] for i in range(6)]
    out_eq = [r[:3] for r in mm(mm(U, Sin_eq), tr(U))[:3]]
    check(f"N1.K1b [{label}] uniform temperature in -> theta I out (port invisible in equilibrium)", out_eq == scal(theta, eye(3)))
    e = [1 - sum(S[i][j] ** 2 for j in range(3)) for i in range(3)]
    a = [1 - sum(S[j][i] ** 2 for j in range(3)) for i in range(3)]
    if label == "reciprocal":
        check("N1.K1c [reciprocal] emissivity_i == absorptivity_i for all ports (Kirchhoff)", e == a,
              f"e={[str(x) for x in e]}")
    else:
        check("N1.K1c [nonreciprocal] some e_i != a_i, yet sum e == sum a (Kirchhoff violated per port, not in total)",
              e != a and sum(e) == sum(a), f"e={[str(x) for x in e]} a={[str(x) for x in a]}")

# ---------------------------------------------------------------- N2
print("== N2 quantum noise defect: passive and active ports in one formula ==")
tau, N, n, x = sp.symbols('tau N n x', positive=True)
CP = sp.Matrix([[N, sp.I * (1 - tau) / 2], [-sp.I * (1 - tau) / 2, N]])
ev = sorted([sp.simplify(e) for e in CP.eigenvals().keys()], key=str)
check("N2.K2a CP matrix eigenvalues == N -+ (1-tau)/2  (CP <=> N >= |1-tau|/2)",
      set(sp.simplify(e - N) for e in ev) == {(1 - tau) / 2, -(1 - tau) / 2}, f"{ev}")
# Heisenberg dilations acting on quadrature variances (V_vac = 1/2, V_thermal = n + 1/2)
Vin, Vc = sp.symbols('V_in V_c', positive=True)
bs_out = tau * Vin + (1 - tau) * Vc          # b = sqrt(tau) a + sqrt(1-tau) c        (tau<1)
sq_out = tau * Vin + (tau - 1) * Vc          # b = sqrt(tau) a + sqrt(tau-1) c^dagger (tau>1)
unified = lambda t: t * Vin + sp.Abs(1 - t) * (n + sp.Rational(1, 2))
ok = all(sp.simplify(bs_out.subs({tau: t, Vc: n + sp.Rational(1, 2)}) - unified(t)) == 0 for t in [sp.Rational(1, 3), sp.Rational(4, 5)]) \
    and all(sp.simplify(sq_out.subs({tau: t, Vc: n + sp.Rational(1, 2)}) - unified(t)) == 0 for t in [sp.Rational(3, 2), sp.Rational(7, 2)])
check("N2.K2b beam splitter & two-mode squeezer both give added noise |1-tau|(n+1/2); n=0 saturates CP (Caves)", ok)
nb = 1 / (sp.exp(x) - 1)
# RUN LOG (2026-09-29): first run FAILED here — sp.simplify does not close coth identities;
# diagnosed as a gate artifact (identity true: rewrite(exp) -> 0; spot x=log 3 -> 0). Fixed by rewrite(exp).
check("N2.K2c n + 1/2 == (1/2)coth(x/2), x = hbar w/kT; x -> 0: (n+1/2) x -> 1 (kT per mode)",
      sp.simplify(((nb + sp.Rational(1, 2)) - sp.coth(x / 2) / 2).rewrite(sp.exp)) == 0
      and sp.limit((nb + sp.Rational(1, 2)) * x, x, 0) == 1)

# ---------------------------------------------------------------- N3
print("== N3 the port-charge table (supply / read) ==")
def kron(A, B):
    return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])] for j in range(len(A[0]) * len(B[0]))]
            for i in range(len(A) * len(B))]
I2 = eye(2); sm = [[F(0), F(1)], [F(0), F(0)]]; sp_ = tr(sm); sz = [[F(1), F(0)], [F(0), F(-1)]]
Qop = [[F(0), F(0)], [F(0), F(1)]]
def lind(jumps, rho):
    out = [[F(0)] * 4 for _ in range(4)]
    for g, A in jumps:
        AtA = mm(tr(A), A)
        term = add(mm(mm(A, rho), tr(A)), scal(F(1, 2), add(mm(AtA, rho), mm(rho, AtA))), -1)
        out = add(out, scal(g, term))
    return out
def ptr_g(X): return [[sum(X[2 * q + g][2 * qq + g] for g in range(2)) for qq in range(2)] for q in range(2)]
basis = []
for i in range(4):
    for j in range(4):
        Eij = [[F(int(a == i and b == j)) for b in range(4)] for a in range(4)]; basis.append(Eij)
gam, gr, r = F(3), F(5, 2), F(1, 7)          # r = e^{-beta Delta} supplied by KMS (any rational)
# (a) neither supply nor read: gauge-only jumps
ja = [(F(3), kron(I2, sm)), (F(5), kron(I2, sz)), (F(2), kron(I2, sp_))]
check("N3.K3a neither-supply-nor-read: Tr_gauge L(rho) == 0 for all rho (noiseless subsystem)",
      all(ptr_g(lind(ja, E)) == [[0, 0], [0, 0]] for E in basis))
# (b) read-only
jb = [(gr, kron(Qop, I2))]
okb = True
for E in basis:
    d, p = ptr_g(lind(jb, E)), ptr_g(E)
    okb &= d[0][0] == 0 and d[1][1] == 0 and d[0][1] == -gr / 2 * p[0][1] and d[1][0] == -gr / 2 * p[1][0]
Qf = kron(Qop, I2)
okb &= all(sum(mm(Qf, lind(jb, E))[k][k] for k in range(4)) == 0 for E in basis)
check("N3.K3b read-only: populations & <Q> conserved, logical coherence decays at exactly gamma/2 (QND = dephasing)", okb)
# (c) supply with detailed balance
jc = [(gam, kron(sm, I2)), (gam * r, kron(sp_, I2))]
okc = True
for E in basis:
    d, p = ptr_g(lind(jc, E)), ptr_g(E)
    okc &= d[1][1] == gam * r * p[0][0] - gam * p[1][1] and d[0][0] == -d[1][1]
ss = [[1 / (1 + r), F(0)], [F(0), r / (1 + r)]]
stat = kron(ss, [[F(1, 2), F(0)], [F(0), F(1, 2)]])
okc &= ptr_g(lind(jc, stat)) == [[0, 0], [0, 0]]
check("N3.K3c supply: dp1/dt = gamma r p0 - gamma p1, stationary p1/p0 = r = e^{-beta Delta} exactly", okc, f"r={r}")
# (d) combined T1/T2
jd = jc + jb
G1, Gphi = gam * (1 + r), gr / 2
okd = all(ptr_g(lind(jd, E))[0][1] == -(G1 / 2 + Gphi) * ptr_g(E)[0][1] for E in basis)
check("N3.K3d combined: coherence rate == Gamma1/2 + Gamma_phi exactly (T1 = supply, T_phi = read)", okd,
      f"Gamma1={G1}, Gamma_phi={Gphi}")

# ---------------------------------------------------------------- N5
print("== N5 modeling calculus: port-Hamiltonian closure ==")
R_ = sp.Rational
def ph(n, s):
    Jm = sp.Matrix(n, n, lambda i, j: 0 if i == j else (R_((i * 3 + j * 5 + s) % 7 - 3, 1 + (i + j + s) % 3) if i < j else 0))
    Jm = Jm - Jm.T
    Mr = sp.Matrix(n, n, lambda i, j: R_((2 * i + j + s) % 5 - 2, 1 + (i * j + s) % 3))
    Nq = sp.Matrix(n, n, lambda i, j: R_((i + 3 * j + s) % 5 - 2, 2 + (i + j) % 2))
    B = sp.Matrix(n, 1, lambda i, j: R_((i + s) % 4 - 1, 1 + i % 2))
    return Jm, Mr.T * Mr, Nq.T * Nq + sp.eye(n), B
def _psd_ldl(M):
    M = sp.Matrix(M); n_ = M.shape[0]
    for k in range(n_):      # symmetric Gaussian elimination with pivot >= 0 (zero pivot => zero row)
        if M[k, k] < 0: return False
        if M[k, k] == 0:
            if any(M[k, j] != 0 for j in range(k, n_)): return False
            continue
        for i in range(k + 1, n_):
            f = M[i, k] / M[k, k]
            for j in range(k, n_): M[i, j] -= f * M[k, j]
    return True
J1, R1, Q1, B1 = ph(4, 1); J2, R2, Q2, B2 = ph(3, 2)
sym = Q1 * (J1 - R1) * Q1; sym = (sym + sym.T) / 2
check("N5.K5a energy balance: sym[Q(J-R)Q] == -QRQ  (dH/dt = -dissipation + y.u)", sym == -Q1 * R1 * Q1)
Jc = sp.diag(J1, J2); Jc[:4, 4:] = -B1 * B2.T; Jc[4:, :4] = B2 * B1.T
Rc = sp.diag(R1, R2)
check("N5.K5b power-conserving interconnection: J_c skew, R_c PSD exactly", Jc == -Jc.T and _psd_ldl(Rc))
Vr = sp.Matrix([[1, 0], [R_(1, 2), 1], [0, R_(-1, 3)], [R_(2, 5), R_(1, 4)]])
Qr = Vr.T * Q1 * Vr
Wr = Q1 * Vr * Qr.inv()
Jr, Rr, Br = Wr.T * J1 * Wr, Wr.T * R1 * Wr, Wr.T * B1
w = sp.symbols('w', real=True)
def Gre(Jm, Rm, Qm, Bm, wv):
    n_ = Jm.shape[0]
    G = (Bm.T * Qm * (sp.I * wv * sp.eye(n_) - (Jm - Rm) * Qm).inv() * Bm)[0, 0]
    return sp.nsimplify(sp.re(sp.simplify(G)))
wts = [R_(1, 3), R_(1), R_(5, 2)]
pr_full = [Gre(J1, R1, Q1, B1, wv) for wv in wts]
pr_red = [Gre(Jr, Rr, Qr, Br, wv) for wv in wts]
check("N5.K5c reduction keeps structure: J_r skew, R_r PSD, Q_r PD; Re G(iw) >= 0 full & reduced",
      Jr == -Jr.T and _psd_ldl(Rr) and all(Qr[:k, :k].det() > 0 for k in (1, 2))
      and all(v >= 0 for v in pr_full + pr_red), f"ReG_full={pr_full} ReG_red={pr_red}")

# ---------------------------------------------------------------- N6
print("== N6 local FDT => port FDT for any readout (Levin) ==")
Mm = sp.Matrix([[2, R_(1, 2), 0], [R_(1, 2), 3, R_(1, 3)], [0, R_(1, 3), 1]])
Km = sp.Matrix([[5, -2, 0], [-2, 4, -1], [0, -1, 3]])
Cm = sp.Matrix([[R_(1, 5), 0, 0], [0, 0, 0], [0, 0, R_(1, 2)]])      # loss only on two elements
p = sp.Matrix([1, R_(1, 2), -1])
ok6 = True
for wv in [R_(1, 2), R_(3, 2), R_(3)]:
    G = (Km - wv ** 2 * Mm + sp.I * wv * Cm).inv()
    chi = sp.expand((p.T * G * p)[0, 0])
    Gc = G.applyfunc(sp.conjugate)
    rhs = sp.expand(wv * (p.T * G * Cm * Gc * p)[0, 0])
    Wd_over_F2 = sp.expand(wv ** 2 / 2 * (p.T * Gc * Cm * G * p)[0, 0])
    ok6 &= sp.simplify(-sp.im(chi) - rhs) == 0 and sp.simplify(rhs / wv * 4 - 8 * Wd_over_F2 / wv ** 2) == 0
check("N6.K6 -Im chi_pp == w p'GC conj(G)p: 4kT C at each damper => (4kT/w)|Im chi_pp| = 8kT W_diss/(w^2 F0^2) at any readout", ok6)

print(f"\n{sum(res)}/{len(res)} GREEN")
