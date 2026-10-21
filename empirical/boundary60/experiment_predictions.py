"""Prospective RC-chain predictions; synthetic calculations, no experimental data.

Before first execution: verify dense vs innovations sampled KL <1e-10;
sampled visibility <= continuous ceiling (2e-10 tolerance); denser nested
sampling improves ideal information; fixed thermal-unit detector noise gives
temperature collapse to 2e-10; fixed physical detector noise lowers visibility
when cooled; finite-ramp preparation endpoint error <1e-8; lattice antecedent
decay factor equals exp(-2*kappa) to 1e-12.

No simulation result is described as a physical experiment. Outputs have a
separate directory from earlier theorem certificates. Matplotlib is loaded
from a task-specific temporary dependency directory if not installed.
"""
from pathlib import Path
import os, sys, json, csv
import numpy as np
from scipy.linalg import expm, eigh, solve_continuous_lyapunov
from scipy.integrate import solve_ivp
from scipy.stats import norm

HERE=Path(__file__).resolve().parent
OUT=HERE/'experiment'; OUT.mkdir(exist_ok=True)
checks=[]
def check(name, condition, value):
    checks.append(dict(name=name,passed=bool(condition),value=value))
    print(('PASS ' if condition else 'FAIL ')+name+': '+str(value),flush=True)
def sym(A): return (A+A.T)/2
def chain(n,m):
    return np.diag(np.full(n+1,m+2))+np.diag(-np.ones(n),1)+np.diag(-np.ones(n),-1)
def root(A):
    e,V=eigh(sym(A)); return (V*np.sqrt(e))@V.T
def ideal(n,m):
    C=chain(n-1,m); E=np.zeros((n,n)); E[0,0]=1
    F=root(C@C+E); M=sym(C-2*C@np.linalg.solve(C+F,C))
    return np.diag(M)/(m+2)

def sampled(n,m,T,tau,steps,noise_var=0.,boundary_delta=0.,hidden_noise=True,history=False):
    K0=chain(n,m); K=K0.copy(); K[0,0]+=boundary_delta
    dt=tau/steps; F=expm(-K*dt)
    D=2*T*np.eye(n+1)
    if not hidden_noise: D[1:,1:]=0
    Sdyn=solve_continuous_lyapunov(K,D)
    Q=sym(Sdyn-F@Sdyn@F.T)
    P=T*np.linalg.inv(K0)  # same original reference before feedback switch
    U=np.vstack([np.zeros((1,n)),np.eye(n)])
    G=np.zeros((n,n)); hist=[]
    for j in range(steps+1):
        if j:
            P=sym(F@P@F.T+Q); U=F@U
        var=P[0,0]+noise_var; H=U[0].copy(); gain=P[:,0]/var
        G+=np.outer(H,H)/var
        U-=np.outer(gain,H); P=sym(P-np.outer(gain,P[0]))
        if history: hist.append((j*dt,(T*np.diag(G)/(m+2)).tolist()))
    return T*np.diag(G)/(m+2),hist

# Dense Gaussian record is separate from the recursive innovations calculation.
n=3; m=.2; T=1.3; tau=2.; steps=20; nv=.03
K=chain(n,m); S=T*np.linalg.inv(K); times=np.linspace(0,tau,steps+1)
Fs=[expm(-K*t) for t in times]
H=np.array([F[0,1:] for F in Fs])
V=np.array([[ (S@expm(-K*abs(t-s)))[0,0] for s in times] for t in times])+nv*np.eye(steps+1)
dense=T*np.diag(H.T@np.linalg.solve(V,H))/(m+2)
recursive,_=sampled(n,m,T,tau,steps,nv)
err=float(np.max(abs(dense-recursive)))
check('dense record versus innovations',err<1e-10,err)

n=12; m=.2; T=1.; tau=20.; steps=400
ceil=ideal(n,m); basevar=np.linalg.inv(chain(n,m))[0,0]
nv=.1**2*basevar  # assumed per-sample detector SD = 10% of base thermal SD
noiseless,hist=sampled(n,m,T,tau,steps,history=True)
detected,_=sampled(n,m,T,tau,steps,nv)
fine,_=sampled(n,m,T,tau,steps*4)
nohidden,_=sampled(n,m,T,tau,steps,nv,hidden_noise=False)
check('record obeys ideal ceiling',bool(np.all(detected<=noiseless+2e-10) and np.all(noiseless<=ceil+2e-10)),
      float(np.max(noiseless-ceil)))
check('nested noiseless sampling improves',bool(np.all(fine>=noiseless-2e-10)),float(np.min(fine-noiseless)))
collapsed=[]; fixed=[]
for temp in [.5,1.,2.]:
    normalized,_=sampled(n,m,temp,tau,steps,temp*nv)
    physical,_=sampled(n,m,temp,tau,steps,nv)
    collapsed.append(normalized); fixed.append(physical)
err=float(np.max(abs(np.array(collapsed)-detected)))
check('thermal-unit temperature collapse',err<2e-10,err)
check('fixed detector cooling penalty',bool(np.all(fixed[0]<=fixed[1]+1e-12) and np.all(fixed[1]<=fixed[2]+1e-12)),
      [float(row[1]) for row in fixed])

# Deterministic pre-drive shifts the equilibrium mean exactly without changing covariance.
duration=.4; depth=3; amp=np.sqrt(2/(m+2)); v=np.eye(n+1)[depth]*amp
K=chain(n,m)
def prep_rhs(t,mean):
    u=t/duration; s=3*u*u-2*u**3; ds=(6*u-6*u*u)/duration
    f=ds*v+K@(s*v)
    return -K@mean+f
sol=solve_ivp(prep_rhs,(0,duration),np.zeros(n+1),rtol=1e-11,atol=1e-13)
err=float(np.max(abs(sol.y[:,-1]-v)))
check('finite ramp local preparation',err<1e-8,err)
kap=np.arccosh(1+m/2); alpha=(m+2)**2/2-1
decay=alpha-np.sqrt(alpha*alpha-1)
check('prior lattice exponent matches',abs(decay-np.exp(-2*kap))<1e-12,float(decay))

# Power assumptions: mean preparation J=1 nat, equal covariance and known models.
rows=[]
for j in range(6):
    D=float(detected[j]); theta=float(ceil[j])
    n_class=int(np.ceil(2*norm.ppf(.9)**2/D))
    n_precision=int(np.ceil(2*norm.ppf(.975)**2/(.2**2*D)))
    rows.append(dict(depth=j+1,theta_infinity=theta,theta_sampled=float(noiseless[j]),
                     theta_detector=D,theta_no_hidden_noise=float(nohidden[j]),
                     N_error_10pct=n_class,N_20pct_relative_KL_95pct=n_precision))
print(json.dumps(rows,indent=2),flush=True)
feedback=[]
for delta in [0.,2.,8.]:
    coarse,_=sampled(n,m,1.,tau,400,0.,delta)
    finer,_=sampled(n,m,1.,tau,1600,0.,delta)
    feedback.append(dict(boundary_delta=delta,coarse=coarse[:6].tolist(),fine=finer[:6].tolist()))

physical=dict(R_ohm=1e7,Cc_F=1e-9,Cp_F=5e-9,temperature_K=300.,
              time_unit_s=.01,sample_interval_s=.0005,record_duration_s=.2,
              q_unit_C=float(np.sqrt(1.380649e-23*300*1e-9)),
              displacement_J1_C=float(np.sqrt(2*1.380649e-23*300*1e-9/(m+2))),
              detector_rms_V=float(np.sqrt(nv*1.380649e-23*300*1e-9)/5e-9))
data=dict(status='prospective model calculations; not experimental observations',checks=checks,
          n=n,m_over_k=m,J=1,record_tau=tau,steps=steps,detector_variance=nv,
          physical=physical,depths=rows,feedback=feedback,
          fixed_detector_temperature_ratios=[.5,1,2],fixed_detector_theta=[x[:6].tolist() for x in fixed])
with (OUT/'predictions.json').open('x',encoding='utf-8') as f: json.dump(data,f,indent=2)
with (OUT/'depth_predictions.csv').open('x',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

# Standard scientific plot, deliberately marked as model predictions.
try: import matplotlib
except ImportError:
    sys.path.insert(0,str(Path(os.environ['TEMP'])/'boundary60-plot-deps'))
    import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(14,4.3),layout='constrained')
d=np.arange(1,7)
axes[0].semilogy(d,ceil[:6],'o-',label='Infinite-time ideal')
axes[0].semilogy(d,detected[:6],'s--',label='Finite sampled + detector')
axes[0].semilogy(d,nohidden[:6],'^:',label='Hidden bath noise omitted')
axes[0].set(xlabel='Preparation depth d',ylabel='Visible fraction D/J',title='A  Depth: exact finite-chain predictions')
axes[0].legend(fontsize=8)
ht=np.array([r[0] for r in hist]); hv=np.array([r[1] for r in hist])
for j in [0,1,3]:
    axes[1].plot(ht,hv[:,j]/ceil[j],label=f'd = {j+1}')
axes[1].axhline(1,color='gray',lw=.7)
axes[1].set(xlabel='Horizon / (R Cc)',ylabel='Fraction of infinite-time visibility',title='B  Ideal sampled observation saturates',ylim=(0,1.04))
axes[1].legend(fontsize=8)
axes[2].semilogy(d,[r['N_error_10pct'] for r in rows],'o-',label='10% classification error')
axes[2].semilogy(d,[r['N_20pct_relative_KL_95pct'] for r in rows],'s--',label='KL: 20% relative precision, 95%')
axes[2].set(xlabel='Preparation depth d',ylabel='Independent prepared trials',title='C  Trial budget, J = 1 nat')
axes[2].legend(fontsize=8)
for ax in axes: ax.grid(alpha=.2)
fig.suptitle('PROSPECTIVE MODEL PREDICTIONS — 13-loop RC chain, m/k = 0.2',fontsize=13)
fig.savefig(OUT/'predictions.png',dpi=180)
fig.savefig(OUT/'predictions.svg')
plt.close(fig)
print(f"{sum(x['passed'] for x in checks)}/{len(checks)} checks passed",flush=True)
raise SystemExit(0 if all(x['passed'] for x in checks) else 1)
