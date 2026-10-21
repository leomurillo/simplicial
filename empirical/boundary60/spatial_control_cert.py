"""Author checks for Paper 60 Theorems 6.7--6.9, declared before execution.

N1: 70-digit matrix square-root visibility and spectral heat Gram obey every
    intermediate and final spatial bound on m/k=.2,1,3 and n=1,4,10 (all d).
    Check ARE and Green-function identities to relative 1e-55 / absolute 1e-55.
N2: d=n=8,16,24,32: report exact log rates and compare to proved finite bounds;
    no claim that these finite computations prove the limiting exponent.
N3: independently discretized full-network observations under three linear
    boundary feedback gains converge to the same continuous information.
    Grids 32,128,512,2048; final max error <2e-5 and errors decrease.
N4: nonlinear history feedback: discrete path transformation and its inverse
    agree to 1e-11 with a shared latent observation path.
N5: a non-Gaussian symmetric mixture obeys the local scalar SDPI, via direct
    one-dimensional quadrature (1e-10 tolerance).
N6: deep-subspace sharp coefficients obey the uniform geometric trace bound
    and dominate the single-site coefficient, for n=6 and every depth.

Logs/results use exclusive creation. These are author checks, not independent
peer validation, and do not replace proofs. Earlier certificates untouched.
"""
from pathlib import Path
import json
import time
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.integrate import solve_ivp, quad
from scipy.special import logsumexp

mp.mp.dps = 70
rows, details = [], {}
start = time.perf_counter()

def check(name, condition, detail):
    rows.append(dict(name=name, passed=bool(condition), detail=detail))
    print(('PASS ' if condition else 'FAIL ') + name + ': ' + str(detail), flush=True)

def chain(n, m, k=1):
    C = mp.eye(n)*(m+2*k)
    for j in range(n-1):
        C[j,j+1] = C[j+1,j] = -k
    return C

def matrices(n, m, k=mp.mpf(1)):
    C=chain(n,m,k)
    E=mp.zeros(n); E[0,0]=k*k
    ev,U=mp.eigsy(C*C+E)
    F=U*mp.diag([mp.sqrt(x) for x in ev])*U.T
    I=(F-C)/2  # T=1
    M=C-2*C*((C+F)**-1)*C
    cv,V=mp.eigsy(C)
    gram=[]
    for d in range(n):
        b=[V[0,j]*V[d,j] for j in range(n)]
        gram.append(mp.fsum(b[i]*b[j]/(cv[i]+cv[j]) for i in range(n) for j in range(n)))
    return C,I,M,gram

def constants(m,k=mp.mpf(1)):
    a=m+2*k; kap=mp.acosh(a/(2*k)); v=mp.sqrt(a*a-4*k*k)
    Q=(1+k*k/m**2)*(1+k*k/(4*m**2))
    lo=m*(1-mp.exp(-2*kap))**2*mp.exp(-2*m/v)/(a*Q)
    hi=k*mp.exp(kap)/(2*a)
    return a,kap,Q,lo,hi

okay=True; worst=mp.mpf(0); count=0
for m in map(mp.mpf,['.2','1','3']):
    for n in [1,4,10]:
        C,I,M,G=matrices(n,m)
        a,kap,Q,lo,hi=constants(m)
        E=mp.zeros(n); E[0,0]=mp.mpf('.5')
        residual=mp.norm(E-C*I-I*C-2*I*I)
        worst=max(worst,residual)
        inv=C**-1
        for j in range(n):
            d=j+1; th=M[j,j]/a; scale=mp.exp(-2*kap*d)
            green=mp.sinh((n+1-d)*kap)/mp.sinh((n+1)*kap)
            okay &= abs(inv[0,j]-green)<mp.mpf('1e-55')
            okay &= lo*scale/d <= th <= hi*scale
            okay &= G[j]/(2*a*Q) <= th <= G[j]/(2*a)
            okay &= G[j]/(2*(1+1/m**2)) <= I[j,j] <= G[j]/2
            count+=1
check('N1 spatial bounds and identities',okay and worst<mp.mpf('1e-55'),
      dict(cases=count,max_are_residual=float(worst)))

rate_rows=[]; okay=True
for d in [8,16,24,32]:
    C,I,M,G=matrices(d,mp.mpf(1))
    a,kap,Q,lo,hi=constants(mp.mpf(1))
    th=M[d-1,d-1]/a
    lower=lo/d*mp.exp(-2*kap*d); upper=hi*mp.exp(-2*kap*d)
    okay &= lower <= th <= upper
    row=dict(d=d,theta=mp.nstr(th,18),rate=float(-mp.log(th)/d),
             target=float(2*kap),lower=mp.nstr(lower,12),upper=mp.nstr(upper,12))
    rate_rows.append(row)
    print('RATE '+json.dumps(row),flush=True)
details['spatial_rates']=rate_rows
check('N2 deep preparations at high precision',okay,rate_rows[-1])

def sym(X): return (X+X.T)/2
def sampled(K,T,tau,n):
    dim=len(K); h=dim-1
    F=expm(-K*tau/n); S=T*np.linalg.inv(K); Q=sym(S-F@S@F.T)
    P=np.zeros((dim,dim)); U=np.vstack([np.zeros((1,h)),np.eye(h)])
    G=np.zeros((h,h))
    for _ in range(n):
        Pp=sym(F@P@F.T+Q); Up=F@U
        R=Pp[:1,:1]; O=Up[:1]; gain=Pp[:,:1]/R[0,0]
        G+=O.T@O/R[0,0]
        P=sym(Pp-gain@Pp[:1]); U=Up-gain@O
    return sym(G)

C=np.diag([3.]*3)+np.diag([-1.]*2,1)+np.diag([-1.]*2,-1)
B=np.array([[-1.,0,0]]); T=1.; tau=2.
def rhs(_,flat):
    I=flat.reshape(3,3)
    return (B.T@B/(2*T)-C@I-I@C-2*T*I@I).ravel()
sol=solve_ivp(rhs,(0,tau),np.zeros(9),rtol=2e-12,atol=2e-14)
target=sol.y[:,-1].reshape(3,3)
control_rows=[]; okay=True
for aeff in [.75,3.,12.]:
    K=np.block([[np.array([[aeff]]),B],[B.T,C]])
    errors=[float(np.max(abs(sampled(K,T,tau,n)-target))) for n in [32,128,512,2048]]
    okay &= errors[-1]<2e-5 and all(errors[j+1]<errors[j] for j in range(3))
    control_rows.append(dict(boundary_stiffness=aeff,errors=errors))
details['feedback_sampled_errors']=control_rows
check('N3 full-network controlled observations',okay,control_rows)

rng=np.random.default_rng(6107); dt=.0005; steps=2000
hidden=np.array([.4,-.2,.1]); Y=[0.]
for j in range(steps):
    Y.append(Y[-1]+(-B@hidden).item()*dt+np.sqrt(2*T*dt)*rng.normal())
    hidden=hidden-C@hidden*dt+np.sqrt(2*T*dt)*rng.normal(size=3)
Y=np.array(Y); error=0.
for policy in ['zero','nonlinear_memory','time_dependent']:
    x=.2; g=-np.linalg.solve(C,B.T).ravel()*x; integral=0.; recovered=0.
    for j in range(steps):
        f=(.4*np.sin(x)+.1*integral if policy=='nonlinear_memory' else
           np.sin(j*dt)+.2*np.cos(j*dt)*x if policy=='time_dependent' else 0.)
        drift=-3*x-(B@g).item()+f
        xn=x+Y[j+1]-Y[j]+drift*dt
        recovered+=xn-x-drift*dt
        error=max(error,abs(recovered-Y[j+1]))
        integral+=x*dt; g+=(-C@g-B.ravel()*x)*dt; x=xn
check('N4 nonlinear causal path round trip',error<1e-11,dict(max_error=error))

def mixture_kl(shift):
    def integrand(x):
        lp=logsumexp([-.5*(x-shift)**2,-.5*(x+shift)**2])-np.log(2)-.5*np.log(2*np.pi)
        lref=-.5*x*x-.5*np.log(2*np.pi)
        return np.exp(lp)*(lp-lref)
    return quad(integrand,-max(12,abs(shift)+12),max(12,abs(shift)+12),
                epsabs=1e-12,epsrel=1e-11)[0]
C,I,M,G=matrices(6,mp.mpf(1)); theta=float(M[1,1]/3)
mixture_rows=[]; okay=True
for shift in [.5,2.,5.]:
    J=mixture_kl(shift); D=mixture_kl(np.sqrt(theta)*shift)
    okay &= D>=-1e-10 and D<=theta*J+1e-10
    mixture_rows.append(dict(shift=shift,J=J,D=D,ceiling=theta*J))
check('N5 non-Gaussian local-mode contraction',okay,mixture_rows)
details['mixture']=mixture_rows

subspace_rows=[]; okay=True
a,kap,Q,lo,hi=constants(mp.mpf(1))
for d in range(1,7):
    Ct=C[d-1:6,d-1:6]; Mt=M[d-1:6,d-1:6]
    ev,V=mp.eigsy(Ct); invroot=V*mp.diag([1/mp.sqrt(x) for x in ev])*V.T
    eig=mp.eigsy(invroot*Mt*invroot,eigvals_only=True)
    sharp=eig[len(eig)-1]
    bound=mp.exp(kap)/(2*(1-mp.exp(-2*kap)))*mp.exp(-2*kap*d)
    local=M[d-1,d-1]/3
    okay &= sharp>=local-mp.mpf('1e-60') and sharp<=bound
    subspace_rows.append(dict(d=d,sharp=float(sharp),local=float(local),bound=float(bound)))
check('N6 deep-subspace uniform bound',okay,subspace_rows)
details['deep_subspaces']=subspace_rows

out=dict(checks=rows,details=details,mp_digits=mp.mp.dps,seconds=time.perf_counter()-start)
path=Path(__file__).with_name('spatial_control_cert_results.json')
with path.open('x',encoding='utf-8') as f: json.dump(out,f,indent=2)
print(f"{sum(r['passed'] for r in rows)}/{len(rows)} passed; {out['seconds']:.2f}s",flush=True)
raise SystemExit(0 if all(r['passed'] for r in rows) else 1)
