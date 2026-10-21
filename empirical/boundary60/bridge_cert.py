"""Finite thermal Gaussian boundary bridge: reproducible witnesses.

Criteria written before the first execution, 2026-10-09. These are author
checks of an already-derived theorem, not blind discovery or independent review.
All failed runs are to be retained beside this file. Exact checks use SymPy;
N1/N2 are numerical checks with explicit tolerances. No Monte Carlo is used.

E1: completion of squares, determinant factorization, thermal marginal,
    and static response agree exactly on a pinned four-node network.
E2: full Gaussian KL = marginal KL + conditional KL, including nonzero means,
    changed covariance, and conditional mean mismatch.
E3: thermal recovery costs zero; nonthermal refinement adds its conditional KL;
    Gaussian displacement loss is the hidden conditional energy / T.
E4: marginalization, conditional recovery, and KL loss compose in two orders.
E5: dynamic Schur response AND noise transfer compose as rational functions of s.
E6: at three rational frequencies, full correlated-bath noise obeys reduced FDT,
    susceptibility FDT, and the two elimination orders agree exactly.
E7: memory-kernel Laplace formula and finite-time thermal/nonthermal noise
    covariance are exact; the transient covariance retains initial preparation.
E8: rational right-half-plane impedances are positive definite (Sylvester).
E9: cascade scattering defects and equal-temperature added noise compose.
C1: discarding induced hidden noise violates FDT on an exact two-node witness.
C2: discarding induced cross-correlations changes the final noise exactly.
C3: quantum thermal marginal is NOT the naive Schur-complement oscillator:
    X_B=67/120, P_B=59/60, P_B-K_eff X_B=9/100 at T=1/(2 log 2).
N1: integrated reduced spectrum and full OU Lyapunov covariance reproduce
    T K_eff^-1 to absolute 2e-8 (deterministic quadrature).
N2: two future boundary observations distinguish two preparations with the
    SAME present boundary marginal, but their KL is <= conditional cost + 1e-10.
"""

from pathlib import Path
import json
import platform
import sys
import time

import numpy as np
import scipy
from scipy.integrate import quad_vec
from scipy.linalg import expm, solve_continuous_lyapunov
import sympy as sp

results = []


def clean(x):
    return sp.cancel(sp.expand_log(x, force=True))


def zero(x):
    if isinstance(x, sp.MatrixBase):
        return all(clean(v) == 0 for v in x)
    return sp.simplify(clean(x)) == 0


def check(name, ok, detail=""):
    ok = bool(ok)
    results.append({"name": name, "pass": ok, "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def reduce_matrix(A, keep):
    hidden = [i for i in range(A.rows) if i not in keep]
    E = sp.zeros(len(keep), A.rows)
    for j, i in enumerate(keep):
        E[j, i] = 1
    if hidden:
        cross = -A.extract(keep, hidden) * A.extract(hidden, hidden).inv()
        for j in range(len(keep)):
            for k, i in enumerate(hidden):
                E[j, i] = cross[j, k]
    return (E * A).extract(list(range(len(keep))), keep).applyfunc(sp.cancel), E.applyfunc(sp.cancel)


def kl(m, S, Q):
    """N(m,S) relative to N(0,Q)."""
    d = S.rows
    return (sp.trace(Q.inv() * S) + (m.T * Q.inv() * m)[0]
            - d + sp.log(Q.det() / S.det())) / 2


def pd(A):
    return all(sp.simplify(A[:j, :j].det()) > 0 for j in range(1, A.rows + 1))


start = time.perf_counter()
T = sp.Rational(3, 2)
K = sp.Matrix([[5, -1, -1, 0], [-1, 6, -1, -2],
               [-1, -1, 5, -1], [0, -2, -1, 5]])
keep, hidden = [0, 1], [2, 3]
A, B, C = K[:2, :2], K[:2, 2:], K[2:, 2:]
Kr, E0 = reduce_matrix(K, keep)
L = -C.inv() * B.T
Vth = T * C.inv()
U = sp.eye(4)
U[2:, :2] = L
Seq = T * K.inv()
check("E1 static bridge", pd(K) and zero(U.T*K*U-sp.diag(Kr,C))
      and zero(K.det()-Kr.det()*C.det())
      and zero(Seq[:2,:2]-T*Kr.inv())
      and zero(K.inv()[:2,:2]-Kr.inv()), "square completion, determinants, covariance, compliance")

S = sp.Matrix([[3,1,1,0],[1,4,0,1],[1,0,3,1],[0,1,1,4]]) / 3
m = sp.Matrix([sp.Rational(1,2), -1, 2, sp.Rational(1,3)])
Sb, mb, mi = S[:2,:2], m[:2,:], m[2:,:]
R = S[2:,:2] * Sb.inv()
V = S[2:,2:] - R * S[:2,2:]
W = Vth.inv()
dm = mi-L*mb
J = (sp.trace(W*V)-2+sp.log(Vth.det()/V.det())
     + (dm.T*W*dm)[0]+sp.trace(W*(R-L)*Sb*(R-L).T))/2
Df, Db = kl(m,S,Seq), kl(mb,Sb,Seq[:2,:2])
check("E2 general Gaussian KL chain", pd(S) and zero(Df-Db-J), f"conditional cost = {float(J):.9g}")

Srec = U*sp.diag(Sb,Vth)*U.T
mrec = sp.Matrix.vstack(mb,L*mb)
meanloss = ((mi-L*mb).T*C*(mi-L*mb))[0]/(2*T)
check("E3 recovery and displacement", zero(kl(mrec,Srec,Seq)-Db)
      and zero(kl(m,Seq,Seq)-kl(mb,Seq[:2,:2],Seq[:2,:2])-meanloss)
      and zero(kl(m-mrec,S,Srec)-J), "thermal recovery zero; conditional cost equals recovery KL")

def conditional_map(Q, k):
    # Gaussian conditional mean of all variables from the retained coordinates.
    return Q[:,k] * Q.extract(k,k).inv()

Kx, _ = reduce_matrix(K,[0])
static_ok = True
for mid in ([0,1,2],[0,1,3]):
    Km, _ = reduce_matrix(K,list(mid))
    Kseq, _ = reduce_matrix(Km,[0])
    Qm = Seq.extract(mid,mid)
    rec_direct = conditional_map(Seq,[0])
    rec_mid = conditional_map(Seq,list(mid))
    rec_sub = conditional_map(Qm,[0])
    v_mid = Seq-rec_mid*Qm*rec_mid.T
    v_sub = Qm-rec_sub*Qm[:1,:1]*rec_sub.T
    v_direct = Seq-rec_direct*Seq[:1,:1]*rec_direct.T
    Dmid = kl(m.extract(mid,[0]), S.extract(mid,mid), Qm)
    Dx = kl(m[:1,:],S[:1,:1],Seq[:1,:1])
    static_ok &= zero(Kseq-Kx) and zero(rec_mid*rec_sub-rec_direct)
    static_ok &= zero(v_mid+rec_mid*v_sub*rec_mid.T-v_direct)
    static_ok &= zero((Df-Dmid)+(Dmid-Dx)-(Df-Dx))
check("E4 successive static elimination", static_ok, "both orders: Schur, recovery mean/covariance, KL budget")

s = sp.symbols('s')
Kd = sp.Matrix([[4,-1,-1],[-1,3,-1],[-1,-1,4]])
Gd = sp.Matrix([[3,1,0],[1,4,1],[0,1,2]])
Md = sp.Matrix([[2,sp.Rational(1,4),0],[sp.Rational(1,4),3,0],[0,0,1]])
D = Kd+s*Gd+s*s*Md
Dr, Ed = reduce_matrix(D,[0])
chains = []
dynamic_ok = True
for mid in ([0,1],[0,2]):
    Dmid, E1 = reduce_matrix(D,list(mid))
    Dseq, E2 = reduce_matrix(Dmid,[0])
    chains.append((Dseq,E2,E1))
    dynamic_ok &= zero(Dseq-Dr) and zero(E2*E1-Ed)
check("E5 rational dynamic composition", dynamic_ok, "response and full source-transfer identity for arbitrary s")

fdt_ok = True
for omega in [sp.Rational(1,3), sp.Integer(1), sp.Integer(2)]:
    Dw, Ew = D.subs(s,sp.I*omega), Ed.subs(s,sp.I*omega)
    Dw_r = Dr.subs(s,sp.I*omega)
    Qr = 2*T*Ew*Gd*Ew.H
    ImD = (Dw_r-Dw_r.H)/(2*sp.I)
    chi = Dw_r.inv()
    fdt_ok &= zero(Qr-2*T*ImD/omega)
    fdt_ok &= zero(chi*Qr*chi.H+(2*T/omega)*(chi-chi.H)/(2*sp.I))
    fdt_ok &= zero(chi-Dw.inv()[:1,:1])
    for _, E2, E1 in chains:
        F1, F2 = E1.subs(s,sp.I*omega), E2.subs(s,sp.I*omega)
        fdt_ok &= zero(F2*(2*T*F1*Gd*F1.H)*F2.H-Qr)
check("E6 induced noise and FDT", fdt_ok, "3 exact frequencies, correlated bath, both elimination orders")

t,u,r = sp.symbols('t u r', positive=True, real=True)
Cm = sp.diag(2,3)
Bm = sp.Matrix([[1,-1],[2,1]])
Krm = sp.Matrix([[3,-1],[-1,4]])
Am = Krm+Bm*Cm.inv()*Bm.T
Vm = sp.Matrix([[sp.Rational(1,4),sp.Rational(1,10)],
                [sp.Rational(1,10),sp.Rational(1,3)]])
Et, Eu = sp.diag(sp.exp(-2*t),sp.exp(-3*t)), sp.diag(sp.exp(-2*u),sp.exp(-3*u))
conv = sp.diag(*[sp.integrate(sp.exp(-c*(t-r))*sp.exp(-c*(u-r)),(r,0,u)) for c in (2,3)])
raw = Bm*(Et*Vm*Eu+2*T*conv)*Bm.T
pred = T*Bm*sp.diag(sp.exp(-2*(t-u)),sp.exp(-3*(t-u)))*Cm.inv()*Bm.T + Bm*Et*(Vm-T*Cm.inv())*Eu*Bm.T
Dmem = s*sp.eye(2)+Am-Bm*(s*sp.eye(2)+Cm).inv()*Bm.T
Gmemory = Bm*(s*sp.eye(2)+Cm).inv()*Cm.inv()*Bm.T
check("E7 memory and preparation noise", zero(Dmem-Krm-s*(sp.eye(2)+Gmemory))
      and zero(raw-pred), "exact t>=u>=0 covariance including nonthermal transient")

pr_ok = True
for z in (sp.Rational(1,2)+sp.I/3, 1+2*sp.I, 2-sp.I):
    Z = D.subs(s,z)/z
    Zr = Dr.subs(s,z)/z
    pr_ok &= pd((Z+Z.H)/2) and pd((Zr+Zr.H)/2)
check("E8 positive-real witnesses", pr_ok, "3 rational right-half-plane points")

S1 = sp.Matrix([[sp.Rational(1,3),sp.Rational(1,6)],[0,sp.Rational(1,2)]])
S2 = sp.Matrix([[sp.Rational(1,2),0],[sp.Rational(1,5),sp.Rational(1,3)]])
delta = lambda X: sp.eye(X.rows)-X*X.H
check("E9 cascade defect/noise", pd(delta(S1)) and pd(delta(S2))
      and zero(delta(S2*S1)-delta(S2)-S2*delta(S1)*S2.H), "noncommuting rational contractions")

D2 = sp.Matrix([[2,-1],[-1,2]])+sp.I*sp.eye(2)-sp.eye(2)
D2r,E2r = reduce_matrix(D2,[0])
true_noise = (2*T*E2r*E2r.H)[0]
check("C1 omitted hidden noise detected", zero(true_noise-3*T) and true_noise != 2*T,
      "at omega=1 true PSD=3T, retained white source alone=2T")

Dmid,Efirst = reduce_matrix(D,[0,1])
_,Esecond = reduce_matrix(Dmid,[0])
F1,F2 = Efirst.subs(s,sp.I),Esecond.subs(s,sp.I)
Qmid = (2*T*F1*Gd*F1.H).applyfunc(sp.simplify)
Qdiag = sp.diag(*[Qmid[i,i] for i in range(2)])
cross_error = sp.simplify((F2*(Qmid-Qdiag)*F2.H)[0])
check("C2 discarded noise correlations detected", cross_error != 0, f"final PSD error = {cross_error}")

Kq = sp.Matrix([[sp.Rational(5,2),-sp.Rational(3,2)],[-sp.Rational(3,2),sp.Rational(5,2)]])
Kqr,_ = reduce_matrix(Kq,[0])
Xq = (sp.Rational(5,3)+sp.Rational(17,15)/2)/4
Pq = (sp.Rational(5,3)+2*sp.Rational(17,15))/4
qerror = sp.simplify(Pq-Kqr[0]*Xq)
check("C3 naive quantum Kron rejected", Xq==sp.Rational(67,120) and Pq==sp.Rational(59,60)
      and qerror==sp.Rational(9,100), f"P_B-K_eff X_B = {qerror}")

# Numerical witnesses are separate from the exact algebra above.
Kn = np.array(Kd,float)
Gn = np.array(Gd,float)
Mn = np.array(Md,float)
Tn = float(T)
n = len(Kn)
Mi = np.linalg.inv(Mn)
F = np.block([[np.zeros((n,n)),np.eye(n)],[-Mi@Kn,-Mi@Gn]])
Q = np.zeros((2*n,2*n))
Q[n:,n:] = 2*Tn*Mi@Gn@Mi
Cov = solve_continuous_lyapunov(F,-Q)
target = Tn*np.linalg.inv(Kn)

def spectrum(w):
    full = Kn+1j*w*Gn-w*w*Mn
    E = np.column_stack([np.eye(1), -full[:1,1:]@np.linalg.inv(full[1:,1:])])
    dr = full[:1,:1]-full[:1,1:]@np.linalg.solve(full[1:,1:],full[1:,:1])
    ch = np.linalg.inv(dr)
    return (ch@(2*Tn*E@Gn@E.conj().T)@ch.conj().T).real

integ,err = quad_vec(spectrum,0,np.inf,epsabs=1e-10,epsrel=1e-10)
err_cov = float(np.max(np.abs(Cov[:n,:n]-target)))
err_spec = float(np.max(np.abs(integ/np.pi-target[:1,:1])))
check("N1 integrated FDT and Lyapunov", err_cov<2e-8 and err_spec<2e-8,
      f"covariance error {err_cov:.3g}; spectrum error {err_spec:.3g}; quadrature estimate {err:.3g}")

def kl_np(m1,S1,m0,S0):
    dm = m1-m0
    return float((np.trace(np.linalg.solve(S0,S1))+dm@np.linalg.solve(S0,dm)-len(dm)
                  +np.linalg.slogdet(S0)[1]-np.linalg.slogdet(S1)[1])/2)

Kn4 = np.array(K,float)
Un = np.array(U,float)
Sbn = np.array(Sb,float)
Vtn = np.array(Vth,float)
Vbad = Vtn/3
ab = np.array([0.4,-0.6])
def bdiag(X,Y):
    return np.block([[X,np.zeros((len(X),len(Y)))],[np.zeros((len(Y),len(X))),Y]])
Sgood = Un@bdiag(Sbn,Vtn)@Un.T
Sbad = Un@bdiag(Sbn,Vbad)@Un.T
mgood = np.zeros(4)
mbad = np.concatenate([np.zeros(2),ab])
Qeq = Tn*np.linalg.inv(Kn4)
Obs = np.eye(4)[:2]

def path_pair(m0,S0):
    t1,t2 = 0.1,0.8
    P1,P2,Pt = expm(-Kn4*t1),expm(-Kn4*t2),expm(-Kn4*(t2-t1))
    Sone = Qeq+P1@(S0-Qeq)@P1.T
    Stwo = Qeq+P2@(S0-Qeq)@P2.T
    cross = Obs@Sone@Pt.T@Obs.T
    return np.concatenate([Obs@P1@m0,Obs@P2@m0]), np.block([[Obs@Sone@Obs.T,cross],[cross.T,Obs@Stwo@Obs.T]])

mp,Sp = path_pair(mbad,Sbad)
mr,Sr = path_pair(mgood,Sgood)
path_kl = kl_np(mp,Sp,mr,Sr)
Jnum = kl_np(mbad,Sbad,mgood,Sgood)
check("N2 preparation predicts future boundary", 0<path_kl<=Jnum+1e-10
      and np.allclose(Sbad[:2,:2],Sgood[:2,:2]) and np.allclose(mbad[:2],mgood[:2]),
      f"present KL=0; two-time KL={path_kl:.9g}; conditional cost={Jnum:.9g}")

report = {"criteria_written":"2026-10-09", "status":"author verification, not independent review",
          "python":platform.python_version(),"sympy":sp.__version__,"numpy":np.__version__,"scipy":scipy.__version__,
          "elapsed_seconds":time.perf_counter()-start,"passed":sum(x['pass'] for x in results),
          "total":len(results),"checks":results}
out = Path(__file__).with_name('bridge_cert_results.json')
out.write_text(json.dumps(report,indent=2)+"\n",encoding='utf-8')
print(f"RESULT {report['passed']}/{report['total']} in {report['elapsed_seconds']:.2f}s",flush=True)
sys.exit(0 if all(x['pass'] for x in results) else 1)
