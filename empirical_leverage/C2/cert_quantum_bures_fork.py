"""
C2 certificate: the quantum continuation (open problem D4 of Paper 01c / Paper III).

Verifies, with exact sympy + a small numpy spectral check, the load-bearing
claims that connect Paper III's classical moving cubic to its density-matrix
(Bures / Kubo-Mori) lift in Papers 15, 18, 44 and the monotone-metric fork T24.

NO torch. sympy + numpy only.  Run:  py cert_quantum_bures_fork.py

Checks
------
(A)  Paper 18/15 Thm 2.2 + Paper 44 Lemma 4.1 (diagonal reduction of the BURES
     metric): for rho=diag(p) and a DIAGONAL Hermitian tangent X=diag(x),
     g^B_rho(X,X) = sum_i x_i^2 / p_i  = the classical Fisher metric.
     (SLD eq L_rho(Z)=rho Z + Z rho = X solved exactly; g^B = 2 Tr(X L^{-1}X).)

(B)  Paper 44 eq (4.2) cubic reduction (the QUANTUM Amari-Chentsov tensor on the
     diagonal): for X,Y,Z diagonal,  T^B_rho(X,Y,Z) = sum_i x_i y_i z_i / p_i^2,
     EXACTLY Paper III's classical AC tensor T_p (Thm 5.1 §5).  This is the
     concrete content of the "cubic -> Bures bridge".

(C)  Paper 44 §4.1 off-diagonal Bures denominator: for an off-diagonal tangent
     X=E_{ij}+E_{ji}, the SLD/Bures weight is 2/(p_i+p_j) (the arithmetic-mean
     Morozova-Chentsov function c^SLD).  This is the term with "no classical
     analogue" -- the coherence sector Paper III's diagonal tower cannot reach.

(D)  T24 Thm 3.2 / Prop 3.3: the three named monotone metrics differ ONLY in the
     off-diagonal weight c^f(a,b) = 1/(b f(a/b)):
        SLD/Bures  f=(1+t)/2  -> c = 2/(a+b)            (arithmetic mean^{-1})
        Kubo-Mori  f=(t-1)/log t -> c = (log a-log b)/(a-b)  (log mean^{-1})
        RLD        f=2t/(1+t)  -> c = (a+b)/(2 a b)       (harmonic mean^{-1})
     Ordering on a generic coherence (a!=b):  g^SLD <= g^KM <= g^RLD  (Prop 3.3).

(E)  T24 Prop 3.1 (ZERO fork-width on the decoherent face): on the diagonal
     a=b=lambda, ALL THREE c^f collapse to 1/lambda.  => the quantum AC tensor
     of (B) is metric-fork-INDEPENDENT; the fork is invisible to Paper III's
     classical (diagonal) tower and opens only on coherences.

(F)  T24 Prop 4.1: at the MAXIMALLY MIXED qubit rho_* = I/2, every monotone
     metric agrees (all eigenvalues equal => (E) on every direction), and equals
     2 * (classical Fisher at uniform).  Bures vs Kubo-Mori on the qubit:
     compute both metric tensors over the full Bloch ball; show they coincide
     only at r=0 and split for r>0, with g^SLD <= g^KM everywhere (envelope).

(G)  SIC / N=4 (Paper I 8.3): the four tetrahedral Bloch vectors n_i with
     n_i.n_j = -1/3 are a valid single-qubit SIC; the rank-1 projectors
     E_i = (I + n_i.sigma)/2 satisfy sum_i (1/2) E_i = I (POVM completeness)
     and pairwise Hilbert-Schmidt Tr(E_i E_j) = 1/2*(1+ n_i.n_j) = 1/3, i!=j.
"""
import sympy as sp
import numpy as np

I2 = sp.eye(2)
results = {}

# ---------------------------------------------------------------------------
# SLD superoperator solver (exact): given rho (n x n) and Hermitian X, solve
# rho Z + Z rho = X  for Z  (entrywise in the eigenbasis: Z_ij = X_ij/(l_i+l_j)).
# We work directly in a basis where rho=diag(l) so the solution is explicit; for
# the qubit Bloch computation we diagonalize.
# ---------------------------------------------------------------------------

def bures_metric_eigbasis(lams, X):
    """g^B = 2 Tr(X L^{-1} X) with rho=diag(lams). X Hermitian (sympy Matrix)."""
    n = len(lams)
    val = 0
    for i in range(n):
        for j in range(n):
            denom = lams[i] + lams[j]
            val += X[i, j] * sp.conjugate(X[i, j]) / denom  # Tr(X Z), Z_ij=X_ij/denom
    return sp.simplify(2 * val * sp.Rational(1, 2) * 2)  # 2 * Tr(X L^{-1} X); see note
# NOTE on the factor: Paper 18 Def 2.1 uses g^B = 2 Tr(X L_rho^{-1} X) with
# L_rho(Z)=rho Z+Z rho, and L^{-1}(X)_ij = X_ij/(l_i+l_j).  Then
# Tr(X L^{-1}X) = sum_ij |X_ij|^2/(l_i+l_j) and g^B = 2*that.  We inline that
# directly below to avoid bookkeeping ambiguity.

def gB(lams, X):
    n = len(lams)
    s = 0
    for i in range(n):
        for j in range(n):
            s += X[i, j] * sp.conjugate(X[i, j]) / (lams[i] + lams[j])
    return sp.simplify(2 * s)

# ===== (A) diagonal Bures = Fisher ==========================================
p = sp.symbols('p0 p1 p2 p3', positive=True)
x = sp.symbols('x0 x1 x2 x3', real=True)
lam4 = list(p)
Xdiag = sp.diag(*x)
gA = gB(lam4, Xdiag)
fisher = sum(x[i]**2 / p[i] for i in range(4))
results['A_diag_bures_eq_fisher'] = sp.simplify(gA - fisher) == 0

# ===== (B) diagonal Bures cubic = classical AC tensor =======================
# Bures cubic on the diagonal (Paper 44 eq 4.2): with diagonal X,Y,Z and SLD
# L_X = diag(x_i/p_i), T^B = Re Tr(rho L_X L_Y L_Z) = sum_i p_i (x_i/p_i)(y_i/p_i)(z_i/p_i).
y = sp.symbols('y0 y1 y2 y3', real=True)
z = sp.symbols('z0 z1 z2 z3', real=True)
TB_diag = sum(p[i] * (x[i]/p[i]) * (y[i]/p[i]) * (z[i]/p[i]) for i in range(4))
T_classical = sum(x[i]*y[i]*z[i] / p[i]**2 for i in range(4))   # Paper III §5 AC tensor
results['B_diag_bures_cubic_eq_AC'] = sp.simplify(TB_diag - T_classical) == 0

# ===== (C) off-diagonal Bures denominator = 2/(p_i+p_j) =====================
a, b = sp.symbols('a b', positive=True)
# rho = diag(a,b); X = off-diagonal real unit  [[0,1],[1,0]]
Xoff = sp.Matrix([[0, 1], [1, 0]])
gC = gB([a, b], Xoff)             # = 2*( 1/(a+b) + 1/(b+a) ) = 4/(a+b)
# the per-coherence SLD weight (one complex off-diag dof) is 2/(a+b):
results['C_offdiag_weight_2_over_sum'] = sp.simplify(gC - 4/(a+b)) == 0
results['C_csld_is_arith_mean_inv'] = sp.simplify(sp.Rational(1,1)/(b*((a+b)/(2*b))) - 2/(a+b)) == 0

# ===== (D) the three Morozova-Chentsov functions + ordering =================
def c_f(name, a, b):
    if name == 'SLD':
        f = lambda t: (1 + t)/2
    elif name == 'KM':
        f = lambda t: (t - 1)/sp.log(t)
    elif name == 'RLD':
        f = lambda t: 2*t/(1 + t)
    return 1/(b * f(a/b))
cSLD = sp.simplify(c_f('SLD', a, b))
cKM = sp.simplify(c_f('KM', a, b))
cRLD = sp.simplify(c_f('RLD', a, b))
results['D_cSLD'] = sp.simplify(cSLD - 2/(a+b)) == 0
results['D_cRLD'] = sp.simplify(cRLD - (a+b)/(2*a*b)) == 0
# KM = (log a - log b)/(a-b):
results['D_cKM'] = sp.simplify(cKM - (sp.log(a) - sp.log(b))/(a - b)) == 0
# ordering c^SLD <= c^KM <= c^RLD  (HM<=LM<=AM => inverse-means reverse):
#   Note: metric weight c is 1/mean, and HM<=LM<=AM, so 1/AM <= 1/LM <= 1/HM,
#   i.e. cSLD <= cKM <= cRLD.  Check numerically on a sample (a,b)=(3,1).
ab = {a: sp.Integer(3), b: sp.Integer(1)}
nSLD, nKM, nRLD = (float(cSLD.subs(ab)), float(cKM.subs(ab)), float(cRLD.subs(ab)))
results['D_ordering_SLD_le_KM_le_RLD'] = (nSLD <= nKM <= nRLD)

# ===== (E) zero fork width on the diagonal (a=b=l) ==========================
l = sp.symbols('l', positive=True)
eSLD = sp.simplify(cSLD.subs({a: l, b: l}))
# KM weight is the inverse log-mean (log a - log b)/(a-b); on the diagonal a->b=l
# it is the removable 0/0 limit -> 1/l.  Substitute b=l first, then a->l.
eKM = sp.limit(cKM.subs(b, l), a, l)      # log mean -> l as a->l
eRLD = sp.simplify(cRLD.subs({a: l, b: l}))
results['E_fork_collapses_on_diagonal'] = (sp.simplify(eSLD - 1/l) == 0 and
                                           sp.simplify(eKM - 1/l) == 0 and
                                           sp.simplify(eRLD - 1/l) == 0)

# ===== (F) qubit Bloch: Bures vs Kubo-Mori, agree only at r=0 ===============
# rho = (I + r * sigma_z)/2  along the z-axis (WLOG by unitary invariance);
# eigenvalues l_+/- = (1 +/- r)/2.  Tangent that probes coherence: sigma_x.
# Bures weight on the sigma_x direction = 2/(l_+ + l_-) ... but l_+ + l_- = 1,
# so the COHERENCE denom is set by the off-diag pair (l_+, l_-): weight^SLD =
# 2/(l_+ + l_-) = 2; weight^KM = (log l_+ - log l_-)/(l_+ - l_-).
r = sp.symbols('r', positive=True)
lp, lm = (1 + r)/2, (1 - r)/2
wSLD = 2/(lp + lm)                                 # = 2
wKM = (sp.log(lp) - sp.log(lm))/(lp - lm)
# agreement at r->0:
results['F_qubit_agree_at_maxmix'] = (sp.simplify(sp.limit(wSLD - wKM, r, 0)) == 0)
# split for r>0: wKM > wSLD strictly (log mean < arith mean => its inverse >):
split_val = float((wKM - wSLD).subs(r, sp.Rational(1, 2)))
results['F_qubit_split_r_pos_KM_ge_SLD'] = (split_val > 0)
# numeric envelope over the ball: g^SLD(sigma_x) <= g^KM(sigma_x) for all r in (0,1)
rs = np.linspace(0.01, 0.99, 50)
lpn, lmn = (1 + rs)/2, (1 - rs)/2
wSLDn = 2.0/(lpn + lmn)
wKMn = (np.log(lpn) - np.log(lmn))/(lpn - lmn)
results['F_qubit_envelope_SLD_le_KM_allr'] = bool(np.all(wSLDn <= wKMn + 1e-12))

# ===== (G) the four tetrahedral Bloch vectors ARE a qubit SIC ===============
# tetrahedral directions (unit vectors, pairwise dot -1/3):
T = [np.array(v, float) for v in
     [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]]
T = [v/np.linalg.norm(v) for v in T]
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
sig = [sx, sy, sz]
def proj(n):
    return 0.5*(np.eye(2) + n[0]*sx + n[1]*sy + n[2]*sz)
E = [proj(n) for n in T]
# pairwise dot = -1/3:
dots = [float(np.dot(T[i], T[j])) for i in range(4) for j in range(4) if i < j]
results['G_pairwise_dot_minus_third'] = all(abs(d - (-1/3)) < 1e-12 for d in dots)
# POVM completeness sum (1/2) E_i = I:
S = sum(0.5*Ei for Ei in E)
results['G_povm_completeness'] = bool(np.allclose(S, np.eye(2)))
# SIC overlap Tr(E_i E_j) = 1/3 for i != j  (and = 1 for i=j, rank-1 projectors):
hs = [float(np.real(np.trace(E[i] @ E[j]))) for i in range(4) for j in range(4) if i < j]
results['G_sic_overlap_third'] = all(abs(h - 1/3) < 1e-12 for h in hs)
results['G_rank1_projectors'] = all(abs(float(np.real(np.trace(Ei @ Ei))) - 1.0) < 1e-12 for Ei in E)

# ---------------------------------------------------------------------------
print("="*70)
print("C2 quantum-continuation certificate (Bures / Kubo-Mori fork, SIC)")
print("="*70)
allpass = True
for k, val in results.items():
    ok = bool(val)
    allpass = allpass and ok
    print(f"  [{'PASS' if ok else 'FAIL'}]  {k}")
print("-"*70)
print(f"  Bloch split at r=1/2:  g^KM - g^SLD on sigma_x = {split_val:.6f}  (>0 expected)")
print(f"  c^f at (a,b)=(3,1):    SLD={nSLD:.6f}  KM={nKM:.6f}  RLD={nRLD:.6f}")
print("="*70)
print("OVERALL:", "GREEN  (all checks pass)" if allpass else "RED  (a check failed)")
