"""Exact Gaussian boundary visibility: checks declared before first execution.

2026-10-09. Author verification after analytic derivation, not blind discovery.
Retain all run logs and report failures. No Monte Carlo. Do not overwrite the
original bridge certificate or its results.

E1 exact scalar c=3,b=4,T=3/2 Riccati and visibility: at tau=log(2)/5,
   information=8/17, visibility=4/21; infinite visibility=1/4.
E2 exact dark mean and visible/dark covariance correlations: J>0 but Dpath=0.
N1 backward information Riccati, forward innovations Fisher calculation,
   and matrix hyperbolic solution agree to 2e-9 on noncommuting C,B^T B.
N2 infinite information solves ARE to 2e-12; visibility independent of T;
   finite-horizon information at t=8 within 2e-8 of infinite limit.
N3 exact sampled full-network observations on nested grids increase to the
   continuous-path formula; at N=2048, information error <2e-5. Compare
   A and 2A networks: both converge to the SAME conditional path information.
N4 direct multitime Gaussian KL agrees with the sufficient-statistic formula
   to 2e-10 for an eight-sample record with known x(0).
N5 exact Gaussian posterior chain identity: input KL - visible KL equals
   expected posterior KL, discrepancy <2e-10.
N6 sharp contraction Dpath<=lambda_max(visibility)*J; mean in top eigenvector
   attains the coefficient to 2e-12. Nearby covariance costs attenuate by
   products lambda_i lambda_j (relative error <0.003 at epsilon=1e-3).
N7 rank-one B with distinct hidden decay rates is observable: finite G is
   positive definite. A dark covariance/correlation control has Dpath=0.
N8 original bridge N2 witness: retain its two-time record, then compute exact
   full path to 0.8 and infinity. Require two-time KL <= D_0.8 <= D_inf < J;
   exact visibility formula agrees with a dense sampled record to 2e-5.
N9 general affine Gaussian conditional: joint (x0, canonical record) Gaussian
   KL equals the averaged formula to 2e-12.
"""

from pathlib import Path
import json
import platform
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm
import sympy as sp

rows = []
details = {}
start = time.perf_counter()


def check(name, ok, detail=""):
    rows.append({"name":name,"pass":bool(ok),"detail":detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def sym(X):
    return (X+X.T)/2


def root(X):
    lam,U = np.linalg.eigh(sym(X))
    if np.min(lam)<-1e-10:
        raise ValueError(f"negative eigenvalue {np.min(lam)}")
    return (U*np.sqrt(np.maximum(lam,0)))@U.T


def logdet(X):
    sign,ld = np.linalg.slogdet(X)
    if sign<=0:
        raise ValueError('not positive definite')
    return ld


def gkl(m,V,m0,V0):
    d=m-m0
    return float((np.trace(np.linalg.solve(V0,V))+d@np.linalg.solve(V0,d)
                  -len(m)+logdet(V0)-logdet(V))/2)


def backward(C,B,T,t):
    h=len(C)
    N=B.T@B/(2*T)
    def rhs(_,flat):
        G=flat.reshape(h,h)
        return (N-C@G-G@C-2*T*G@G).ravel()
    sol=solve_ivp(rhs,(0,t),np.zeros(h*h),rtol=2e-12,atol=2e-14)
    return sym(sol.y[:,-1].reshape(h,h))


def forward(C,B,T,t):
    h=len(C)
    N=B.T@B/(2*T)
    def rhs(_,flat):
        P,U,G=flat.reshape(3,h,h)
        return np.array([-C@P-P@C+2*T*np.eye(h)-P@N@P,
                         (-C-P@N)@U,U.T@N@U]).ravel()
    init=np.array([np.zeros((h,h)),np.eye(h),np.zeros((h,h))]).ravel()
    sol=solve_ivp(rhs,(0,t),init,rtol=2e-12,atol=2e-14)
    return sym(sol.y[:,-1].reshape(3,h,h)[2])


def hyperbolic(C,B,T,t):
    D=root(C@C+B.T@B)
    l,U=np.linalg.eigh(D)
    Co=(U*np.cosh(l*t))@U.T
    Si=(U*np.sinh(l*t))@U.T
    X=Co+np.linalg.solve(D,Si)@C
    Y=D@Si+Co@C
    return sym((np.linalg.solve(X.T,Y.T).T-C)/(2*T))


def infinite(C,B,T):
    return sym((root(C@C+B.T@B)-C)/(2*T))


def visibility(C,T,G):
    S=T*np.linalg.inv(C)
    Sh=root(S)
    Z=sym(Sh@G@Sh)
    Pi=sym(np.eye(len(C))-np.linalg.inv(np.eye(len(C))+Z))
    return Pi,Sh


def costs(C,T,G,a,V,mean_second=None):
    Pi,Sh=visibility(C,T,G)
    Shi=np.linalg.inv(Sh)
    alpha=Shi@a
    W=sym(Shi@V@Shi)
    A=np.outer(alpha,alpha) if mean_second is None else Shi@mean_second@Shi
    R=root(Pi)
    Omega=sym(np.eye(len(C))+R@(W-np.eye(len(C)))@R)
    J=float((np.trace(A)+np.trace(W)-len(C)-logdet(W))/2)
    D=float((np.trace(Pi@A)+np.trace(Pi@(W-np.eye(len(C))))-logdet(Omega))/2)
    return J,D,Pi,W,alpha,Omega


# Symbolic checks, independent of floating-point integration.
q=sp.symbols('q',positive=True)
g=sp.Rational(8,3)*(q-1)/(4*q+1)
ric=sp.simplify(10*q*sp.diff(g,q)-(sp.Rational(16,3)-6*g-3*g*g))
p=sp.cancel((g/2)/(1+g/2))
check('E1 scalar exact',ric==0 and g.subs(q,4)==sp.Rational(8,17)
      and p.subs(q,4)==sp.Rational(4,21) and sp.limit(p,q,sp.oo)==sp.Rational(1,4),
      'finite visibility 4/21; infinite visibility 1/4')
Wexact=sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]])
Piexact=sp.diag(sp.Rational(1,4),0)
Rexact=sp.diag(sp.Rational(1,2),0)
alphaexact=sp.Matrix([0,1])
Oexact=sp.eye(2)+Rexact*(Wexact-sp.eye(2))*Rexact
check('E2 exact dark preparation',Oexact==sp.eye(2)
      and (alphaexact.T*Piexact*alphaexact)[0]==0 and Wexact.det()==sp.Rational(3,4),
      'J=(1-log(3/4))/2 > 0; path KL exactly zero')

C=np.array([[5.,-1.],[-1.,5.]])
B=np.array([[-1.,0.],[-1.,-2.]])
A=np.array([[5.,-1.],[-1.,6.]])
K=np.block([[A,B],[B.T,C]])
T=1.5
S=T*np.linalg.inv(C)
a=np.array([.4,-.6])
V=S/3
tau=.8
Gb=backward(C,B,T,tau)
Gf=forward(C,B,T,tau)
Gh=hyperbolic(C,B,T,tau)
err1=max(np.max(np.abs(Gb-Gf)),np.max(np.abs(Gb-Gh)))
check('N1 independent path-information calculations',err1<2e-9,
      f'max error={err1:.3g}; commutator norm={np.linalg.norm(C@(B.T@B)-(B.T@B)@C):.6g}')
Gi=infinite(C,B,T)
res=B.T@B/(2*T)-C@Gi-Gi@C-2*T*Gi@Gi
Pii,_=visibility(C,T,Gi)
Pi2,_=visibility(C,7.,infinite(C,B,7.))
errinf=np.max(np.abs(backward(C,B,T,8.)-Gi))
check('N2 infinite horizon',np.max(np.abs(res))<2e-12 and np.max(np.abs(Pii-Pi2))<2e-12
      and errinf<2e-8,f'ARE residual={np.max(np.abs(res)):.3g}; long-time error={errinf:.3g}')


def sampled_information(K,T,b,tau,n):
    # Exact full-network transition; deterministic initial q=(0,z).
    dim=len(K); h=dim-b
    F=expm(-K*(tau/n))
    Seq=T*np.linalg.inv(K)
    Q=sym(Seq-F@Seq@F.T)
    P=np.zeros((dim,dim))
    U=np.vstack([np.zeros((b,h)),np.eye(h)])
    G=np.zeros((h,h))
    for _ in range(n):
        Pp=sym(F@P@F.T+Q)
        Up=F@U
        R=Pp[:b,:b]
        O=Up[:b]
        Gain=np.linalg.solve(R,Pp[:b,:]).T
        G+=O.T@np.linalg.solve(R,O)
        P=sym(Pp-Gain@Pp[:b,:])
        U=Up-Gain@O
    return sym(G)

meshes=[8,32,128,512,2048]
grids=[sampled_information(K,T,2,tau,n) for n in meshes]
Kalt=K.copy();Kalt[:2,:2]=2*A
Galt=sampled_information(Kalt,T,2,tau,2048)
griderr=max(np.max(np.abs(grids[-1]-Gb)),np.max(np.abs(Galt-Gb)))
monotone=all(np.min(np.linalg.eigvalsh(y-x))>-1e-11 for x,y in zip(grids[:-1],grids[1:]))
check('N3 full-network sampled paths',monotone and griderr<2e-5,
      f'max dense-grid error={griderr:.3g}; A and 2A have same continuous limit')
details['sample_information_errors']={str(n):float(np.max(np.abs(g-Gb))) for n,g in zip(meshes,grids)}


def direct_record(K,T,b,times,a,V):
    dim=len(K); h=dim-b
    U=np.vstack([np.zeros((b,h)),np.eye(h)])
    S0=U@V@U.T;m0=U@a
    Seq=T*np.linalg.inv(K)
    trans=[expm(-K*t) for t in times]
    means=np.concatenate([(P@m0)[:b] for P in trans])
    cov=np.empty((len(times)*b,len(times)*b))
    for i,ti in enumerate(times):
        for j,tj in enumerate(times):
            # OU covariance at two nonstationary times.
            base=expm(-K*abs(ti-tj))@Seq
            block=base+trans[i]@(S0-Seq)@trans[j].T
            cov[i*b:(i+1)*b,j*b:(j+1)*b]=block[:b,:b]
    return means,sym(cov)

times=np.linspace(tau/8,tau,8)
mp,Sp=direct_record(K,T,2,times,a,V)
mr,Sr=direct_record(K,T,2,times,np.zeros(2),S)
Ddirect=gkl(mp,Sp,mr,Sr)
_,Dgrid,*_=costs(C,T,grids[0],a,V)
check('N4 direct multitime KL',abs(Ddirect-Dgrid)<2e-10,
      f'direct={Ddirect:.12g}; sufficient statistic={Dgrid:.12g}')

J,Dt,Pi,W,alpha,Omega=costs(C,T,Gb,a,V)
R=root(Pi);Noise=np.eye(2)-Pi
Post=np.linalg.inv(np.linalg.inv(W)+Pi@np.linalg.inv(Noise))
Gain=Post@R@np.linalg.inv(Noise)
mean_y=R@alpha
post_diff=Post@np.linalg.solve(W,alpha)+(Gain-R)@mean_y
second_diff=np.outer(post_diff,post_diff)+(Gain-R)@Omega@(Gain-R).T
slack=(np.trace(np.linalg.solve(Noise,Post))+np.trace(np.linalg.solve(Noise,second_diff))
       -2+logdet(Noise)-logdet(Post))/2
check('N5 exact posterior slack',abs(J-Dt-slack)<2e-10,
      f'J={J:.12g}; visible={Dt:.12g}; posterior={slack:.12g}')

lam,U=np.linalg.eigh(Pi)
top=root(S)@U[:,-1]
Jm,Dm,*_=costs(C,T,Gb,top,S)
eps=1e-3
pert=U@np.array([[.3,.4],[.4,-.2]])@U.T
Wnear=np.eye(2)+eps*pert
_,Dnear,*_=costs(C,T,Gb,np.zeros(2),root(S)@Wnear@root(S))
pred=eps**2*np.trace(Pi@pert@Pi@pert)/4
nearerr=abs(Dnear/pred-1)
check('N6 sharp visibility coefficient',Dt<=lam[-1]*J+1e-12 and abs(Dm/Jm-lam[-1])<2e-12
      and nearerr<.003,f'lambda_max={lam[-1]:.9g}; mean ratio={Dm/Jm:.9g}; covariance expansion error={nearerr:.3g}')

Co=np.diag([2.,3.]);Bo=np.array([[1.,1.]])
Go=backward(Co,Bo,T,.7)
Cd=np.diag([2.,3.]);Bd=np.array([[1.,0.]])
Gd=backward(Cd,Bd,T,.7)
Sd=T*np.linalg.inv(Cd)
ad=root(Sd)@np.array([0.,1.])
Vd=root(Sd)@np.array(Wexact,float)@root(Sd)
Jdark,Ddark,*_=costs(Cd,T,Gd,ad,Vd)
check('N7 observability versus visibility',np.min(np.linalg.eigvalsh(Go))>1e-7 and Jdark>0 and abs(Ddark)<1e-14,
      f'observable min eig={np.min(np.linalg.eigvalsh(Go)):.6g}; dark J={Jdark:.9g}, KL={Ddark:.3g}')

# Reproduce the original record, which did NOT include x(0).
L=-np.linalg.solve(C,B.T)
Lift=np.block([[np.eye(2),np.zeros((2,2))],[L,np.eye(2)]])
Sb=np.array([[3.,1.],[1.,4.]])/3
def original_record(v,a):
    S0=Lift@np.block([[Sb,np.zeros((2,2))],[np.zeros((2,2)),v]])@Lift.T
    m0=np.r_[np.zeros(2),a]
    Seq=T*np.linalg.inv(K)
    P1,P2,Pt=expm(-K*.1),expm(-K*.8),expm(-K*.7)
    S1=Seq+P1@(S0-Seq)@P1.T;S2=Seq+P2@(S0-Seq)@P2.T
    cross=(S1@Pt.T)[:2,:2]
    return np.r_[(P1@m0)[:2],(P2@m0)[:2]],np.block([[S1[:2,:2],cross],[cross.T,S2[:2,:2]]])
mold,Sold=original_record(V,a);mref,Sref=original_record(S,np.zeros(2))
Dold=gkl(mold,Sold,mref,Sref)
_,Dinf,*_=costs(C,T,Gi,a,V)
_,Ddense,*_=costs(C,T,grids[-1],a,V)
check('N8 original witness upgraded',Dold<=Dt+1e-12 and Dt<=Dinf+1e-12 and Dinf<J
      and abs(Ddense-Dt)<2e-5,
      f'two-time={Dold:.12g}; full[0,.8]={Dt:.12g}; full[0,infinity)={Dinf:.12g}; J={J:.12g}')
details['original_witness']={'two_time_kl':Dold,'path_to_0_8_kl':Dt,'infinite_path_kl':Dinf,
                             'preparation_kl':J,'infinite_visible_fraction':Dinf/J,
                             'infinite_visibility_eigenvalues':np.linalg.eigvalsh(Pii).tolist(),
                             'finite_visibility_matrix':Pi.tolist(),'infinite_visibility_matrix':Pii.tolist()}

# General affine mean a(x0)=d+F(x0-mx), conditional residual covariance fixed.
Faff=np.array([[.2,-.3],[.1,.4]])
d=np.array([.3,-.1]);Xcov=Sb
meansecond=np.outer(d,d)+Faff@Xcov@Faff.T
Jaff,Daff,*_=costs(C,T,Gb,d,V,mean_second=meansecond)
Shi=np.linalg.inv(root(S));Fwhite=Shi@Faff
cross=Xcov@Fwhite.T@R
Vjoint=np.block([[Xcov,cross],[cross.T,Omega+R@Fwhite@Xcov@Fwhite.T@R]])
# Omega is unaffected by a; it was computed above using the same V.
mjoint=np.r_[np.zeros(2),R@Shi@d]
Vjointref=np.block([[Xcov,np.zeros((2,2))],[np.zeros((2,2)),np.eye(2)]])
Daffdirect=gkl(mjoint,Vjoint,np.zeros(4),Vjointref)
check('N9 affine conditional formula',abs(Daff-Daffdirect)<2e-12,
      f'formula={Daff:.12g}; joint Gaussian={Daffdirect:.12g}; J={Jaff:.12g}')

report={'date':'2026-10-09','status':'author verification, not independent review',
        'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,
        'passed':sum(r['pass'] for r in rows),'total':len(rows),'elapsed_seconds':time.perf_counter()-start,
        'checks':rows,'details':details}
Path(__file__).with_name('visibility_cert_results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(f"RESULT {report['passed']}/{report['total']} in {report['elapsed_seconds']:.2f}s",flush=True)
sys.exit(0 if all(r['pass'] for r in rows) else 1)
