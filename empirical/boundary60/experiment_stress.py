"""Prospective bandwidth/mismatch/calibration stress test, 2026-10-09.

Declared checks: thermal plant covariance solves FDT Lyapunov identity <1e-10;
dense record and independent adjoint projected variance agree <1e-9 relative;
record covariance difference is PSD to 1e-9; scalar Gaussian sample-variance
test has exact size .05 and power >=.9 at reported N, with N-1 insufficient;
closed-form variance envelopes dominate their sampled/corner stress cases;
exact-transition Monte Carlo variance lies within six standard errors.

Detector: reset first-order low-pass, fixed input white-noise PSD plus output
sample noise. Calibration nuisance is fixed across a batch, NOT redrawn for
each trial. Component corners/random draws are sensitivity studies, not a
global interval certificate. Exact robust budgets are conditional on declared
bounds for the two projected variances. All outputs are prospective.
"""
from pathlib import Path
import os, sys, json, csv
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, toeplitz, eigh
from scipy.stats import chi2

OUT=Path(__file__).resolve().parent/'stress'; OUT.mkdir(exist_ok=True)
NQ=13; DT=.05; STEPS=400; DIM=NQ+1
Kbase=np.diag(np.full(NQ,2.2))+np.diag(-np.ones(NQ-1),1)+np.diag(-np.ones(NQ-1),-1)
BASEVAR=np.linalg.inv(Kbase)[0,0]; NV=.01*BASEVAR
OMEGA0=2*np.pi*100*.01
NPAR=3*NQ+1+5
# Packed log multipliers: 13 R, 13 Cp, 14 Cc, fc, gain, T, input PSD, output var.
names=([f'R{i}' for i in range(NQ)]+[f'Cp{i}' for i in range(NQ)]+
       [f'Cc{i}' for i in range(NQ+1)]+['fc','gain','T','input_noise_PSD','output_noise_var'])
checks=[]
def check(name,okay,detail):
    checks.append(dict(name=name,passed=bool(okay),detail=detail))
    print(('PASS ' if okay else 'FAIL ')+name+': '+str(detail),flush=True)
def sym(A): return (A+A.T)/2

def state(logp=None,fc=100.,noise_sd_factor=1.,dt=DT):
    p=np.exp(np.zeros(NPAR) if logp is None else logp)
    R=p[:NQ]; Cp=5*p[NQ:2*NQ]; Cc=p[2*NQ:3*NQ+1]
    fcm,gain,T,front,post=p[-5:]
    K=np.diag(1/Cp+1/Cc[:-1]+1/Cc[1:])
    K+=np.diag(-1/Cc[1:-1],1)+np.diag(-1/Cc[1:-1],-1)
    A=np.zeros((DIM,DIM)); A[:NQ,:NQ]=-K/R[:,None]
    omega=2*np.pi*fc*fcm*.01
    A[-1,0]=omega; A[-1,-1]=-omega
    # White detector input PSD fixed as bandwidth changes; 80/20 split at 100 Hz.
    D1=np.zeros((DIM,DIM)); D1[np.arange(NQ),np.arange(NQ)]=2*T/R
    D1[-1,-1]=omega**2*(2*.8*NV/OMEGA0)*front*noise_sd_factor**2
    D0=D1.copy(); D0[np.arange(1,NQ),np.arange(1,NQ)]=0.
    F=expm(A*dt)
    S1=sym(solve_continuous_lyapunov(A,-D1))
    S0=sym(solve_continuous_lyapunov(A,-D0))
    Q1=sym(S1-F@S1@F.T); Q0=sym(S0-F@S0@F.T)
    Pinit=np.zeros((DIM,DIM)); Pinit[:NQ,:NQ]=T*np.linalg.inv(K)
    H=np.zeros(DIM); H[-1]=gain*5/Cp[0]
    rv=.2*NV*post*noise_sd_factor**2
    return dict(F=F,P=Pinit,H=H,Q0=Q0,Q1=Q1,S0=S0,S1=S1,rv=rv,K=K,A=A,D1=D1,T=T)

def records(s,steps=STEPS):
    F,H=s['F'],s['H']; O=np.empty((steps+1,DIM)); O[0]=H
    for j in range(steps): O[j+1]=O[j]@F
    out=[]
    for j in [0,1]:
        S=s[f'S{j}']; lag=O@S@H
        V=toeplitz(lag)+O@(s['P']-S)@O.T+s['rv']*np.eye(steps+1)
        out.append(sym(V))
    return out[0],out[1],O

def projected(s,w):
    # Independent backward accumulation of initial and exact step noises.
    ell=s['H']*w[-1]; v=np.array([s['rv']*(w@w)]*2)
    for j in range(len(w)-1,0,-1):
        v+=np.array([ell@s['Q0']@ell,ell@s['Q1']@ell])
        ell=s['H']*w[j-1]+s['F'].T@ell
    v+=ell@s['P']@ell
    return v

def power(ratio,N,alpha=.05):
    return float(chi2.sf(chi2.ppf(1-alpha,N-1)/ratio,N-1))
def budget(ratio,alpha=.05,target=.9):
    if ratio<=1: return None
    hi=2
    while power(ratio,hi,alpha)<target and hi<10**8: hi*=2
    if hi>=10**8: return None
    lo=2
    while lo<hi:
        mid=(lo+hi)//2
        if power(ratio,mid,alpha)>=target: hi=mid
        else: lo=mid+1
    return lo

base=state(); V0,V1,O=records(base)
e,W=eigh(V1,V0); w=W[:,-1]; ratio=float(e[-1])
vnom=projected(base,w); nnom=budget(ratio)
fdt=sym(base['A']@base['S1']+base['S1']@base['A'].T+base['D1'])
check('thermal augmented FDT residual',np.max(abs(fdt))<1e-10,float(np.max(abs(fdt))))
err=float(np.max(abs(vnom-np.array([w@V0@w,w@V1@w])))/np.max(vnom))
check('dense covariance versus adjoint',err<1e-9,err)
mineig=float(eigh(V1-V0,eigvals_only=True)[0])
check('hidden noise adds PSD record covariance',mineig>-1e-9,mineig)
check('exact scalar budget minimality',power(ratio,nnom)>=.9 and (nnom==2 or power(ratio,nnom-1)<.9),
      dict(ratio=ratio,N=nnom,power=power(ratio,nnom),previous_power=power(ratio,nnom-1)))

band=[]
for fc in [1.,3.,10.,30.,100.,300.]:
    s=state(fc=fc); A,B,Obs=records(s)
    ev,U=eigh(B,A,subset_by_index=[STEPS,STEPS]); ww=U[:,0]
    rr=float(ev[0]); means=Obs[:,1:NQ]*np.sqrt(2/2.2)
    d1=.5*np.diag(means.T@np.linalg.solve(B,means))
    d0=.5*np.diag(means.T@np.linalg.solve(A,means))
    row=dict(fc_Hz=fc,variance_ratio=rr,N=budget(rr),
             Dprep_thermal_d2=float(d1[1]),Dprep_omitted_d2=float(d0[1]))
    band.append(row); print('BAND '+json.dumps(row),flush=True)

noise=[]
for factor in [1.,3.,10.,30.]:
    s=state(noise_sd_factor=factor); A,B,_=records(s)
    rr=float(eigh(B,A,subset_by_index=[STEPS,STEPS],eigvals_only=True)[0])
    noise.append(dict(detector_sd_multiplier=factor,variance_ratio=rr,N=budget(rr)))

# Exact conditional envelope budgets; no Gaussian approximation to test power.
envelopes=[]
for u in [0.,.02,.05,.1,.15,.2,.25]:
    r=ratio*(1-u)/(1+u)
    envelopes.append(dict(relative_variance_bound=u,least_favorable_ratio=r,N=budget(r)))

# Component mismatch: fixed nominal w; no reoptimization using test data.
rng=np.random.default_rng(6009); raw=[]
for j in range(64):
    lp=np.zeros(NPAR); lp[:-5]=np.log1p(rng.uniform(-.05,.05,NPAR-5))
    vv=projected(state(lp),w)
    raw.append(dict(v0=float(vv[0]),v1=float(vv[1]),paired_ratio=float(vv[1]/vv[0]),
                    actual_size=power(vv[0]/vnom[0],nnom),power=power(vv[1]/vnom[0],nnom)))
raw_summary=dict(draws=64,component_tolerance=.05,
                 v0_range=[min(x['v0'] for x in raw),max(x['v0'] for x in raw)],
                 v1_range=[min(x['v1'] for x in raw),max(x['v1'] for x in raw)],
                 actual_size_range=[min(x['actual_size'] for x in raw),max(x['actual_size'] for x in raw)],
                 power_range=[min(x['power'] for x in raw),max(x['power'] for x in raw)])
print('RAW '+json.dumps(raw_summary),flush=True)

# Log sensitivities. Their L1 combination is a first-order box estimate only.
eps=1e-4; grad=np.empty((2,NPAR))
for i in range(NPAR):
    lp=np.zeros(NPAR); lp[i]=eps
    vp=projected(state(lp),w); vm=projected(state(-lp),w)
    grad[:,i]=(np.log(vp)-np.log(vm))/(2*eps)
calrows=[]
for label,comp,fcunc,gunc,tunc,nunc in [
    ('tight',.01,.02,.01,.005,.1),('loose',.05,.1,.03,.02,.2)]:
    unc=np.r_[np.full(NPAR-5,comp),fcunc,gunc,tunc,nunc,nunc]
    bounds=np.log1p(unc)
    candidates=[np.zeros(NPAR)]
    for j in range(2):
        candidates.extend([bounds*np.sign(grad[j]),-bounds*np.sign(grad[j])])
    candidates.extend(rng.uniform(-1,1,NPAR)*bounds for _ in range(64))
    vals=np.array([projected(state(lp),w) for lp in candidates])
    v0max=float(max(vals[:,0])); v1min=float(min(vals[:,1]))
    linear=np.sum(abs(grad)*bounds,axis=1)
    # Rounded projected variance envelope, covering tested points plus 2 points
    # of absolute fractional margin. This is NOT proof for the full parameter box.
    needed=max(v0max/vnom[0]-1,1-v1min/vnom[1],0)
    u=float(np.ceil((needed+.02)*100)/100)
    rr=ratio*(1-u)/(1+u)
    row=dict(label=label,component_uncertainty=comp,fc_uncertainty=fcunc,
             gain_uncertainty=gunc,temperature_uncertainty=tunc,noise_uncertainty=nunc,
             parameterization='symmetric log box +/- log(1+u)',
             samples=len(vals),v0max=v0max,v1min=v1min,
             first_order_log_variance_box=linear.tolist(),
             rounded_variance_envelope=u,conditional_robust_N=budget(rr),
             direct_stress_ratio=v1min/v0max,direct_stress_N=budget(v1min/v0max))
    calrows.append(row);print('CAL '+json.dumps(row),flush=True)
    check(label+' variance envelope covers stress points',
          v0max<=vnom[0]*(1+u) and v1min>=vnom[1]*(1-u),u)

# Exact-step independent Monte Carlo on a shorter record, not scalar Gaussian draws.
s=state(dt=.2); shortsteps=50; A,B,_=records(s,shortsteps)
ev,U=eigh(B,A,subset_by_index=[shortsteps,shortsteps]); ww=U[:,0]
expected=projected(s,ww)
def psdroot(A):
    v,V=eigh(sym(A)); return V*np.sqrt(np.maximum(v,0))
trials=12000; vals=[]
for model in [0,1]:
    X=rng.normal(size=(trials,DIM))@psdroot(s['P']).T
    z=ww[0]*(X@s['H']+np.sqrt(s['rv'])*rng.normal(size=trials))
    L=psdroot(s[f'Q{model}'])
    for i in range(1,shortsteps+1):
        X=X@s['F'].T+rng.normal(size=(trials,DIM))@L.T
        z+=ww[i]*(X@s['H']+np.sqrt(s['rv'])*rng.normal(size=trials))
    vals.append(float(np.var(z,ddof=1)))
zerr=np.abs(np.array(vals)/expected-1)*np.sqrt((trials-1)/2)
check('full-state exact-transition Monte Carlo',np.max(zerr)<6,
      dict(trials=trials,expected=expected.tolist(),observed=vals,standard_errors=zerr.tolist()))

# Confidence allocation if a calibrated variance envelope has only 99% coverage.
u=calrows[0]['rounded_variance_envelope']; rr=ratio*(1-u)/(1+u)
confN=budget(rr,alpha=.04,target=.9/.99)
summary=dict(status='prospective, no measured hardware calibration',checks=checks,
             record=dict(loops=NQ,dt_s=.0005,duration_s=.2,filter_reset=True),
             hypotheses='H0 hidden bath noise absent after record start; H1 full thermal baths; common initial thermal state',
             nominal=dict(ratio=ratio,N=nnom,size=.05,power=power(ratio,nnom),
                          whole_record_KL_thermal_vs_omitted=float(.5*np.sum(e-1-np.log(e))),
                          covariance_eigenvalue_range=[float(e[0]),float(e[-1])]),
             bandwidth=band,detector_noise=noise,variance_envelopes=envelopes,
             raw_mismatch=raw_summary,calibration=calrows,
             tight_99pct_envelope_allocation=dict(envelope=u,conditional_alpha=.04,
                 conditional_power_target=.9/.99,N=confN,
                 unconditional_size_bound=.05,unconditional_power_bound=.9),
             largest_log_sensitivities=[dict(parameter=names[i],H0=float(grad[0,i]),H1=float(grad[1,i]))
                 for i in np.argsort(-np.max(abs(grad),axis=0))[:12]])
with (OUT/'stress_results.json').open('x',encoding='utf-8') as f: json.dump(summary,f,indent=2)
np.savez(OUT/'nominal_projection.npz',weights=w,times_seconds=np.arange(STEPS+1)*.0005,
         v0=vnom[0],v1=vnom[1])
with (OUT/'bandwidth.csv').open('x',newline='',encoding='utf-8') as f:
    wr=csv.DictWriter(f,fieldnames=band[0]);wr.writeheader();wr.writerows(band)

sys.path.insert(0,str(Path(os.environ['TEMP'])/'boundary60-plot-deps'))
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(14,4.3),layout='constrained')
ax[0].semilogx([r['fc_Hz'] for r in band],[r['N'] for r in band],'o-')
ax[0].set(xlabel='Detector cutoff (Hz)',ylabel='Independent records',title='A  Exact scalar test: 5% size, 90% power')
ax[1].semilogy([100*r['relative_variance_bound'] for r in envelopes],
               [r['N'] if r['N'] is not None else np.nan for r in envelopes],'o-')
critical=100*(ratio-1)/(ratio+1);ax[1].axvline(critical,ls='--',color='red',label='Variance envelopes overlap')
ax[1].set(xlabel='Bound on each projected variance (%)',ylabel='Independent records',title='B  Calibration uncertainty is shared')
ax[1].legend(fontsize=8)
ax[2].plot(np.arange(STEPS+1)*.5,w)
ax[2].set(xlabel='Time after detector reset (ms)',ylabel='Projection weight (arbitrary normalization)',title='C  Frozen covariance-test projection')
for a in ax:a.grid(alpha=.25)
fig.suptitle('PROSPECTIVE STRESS TEST — covariance-model rejection, not preparation-KL validation',fontsize=12)
fig.savefig(OUT/'stress.png',dpi=180);fig.savefig(OUT/'stress.svg');plt.close(fig)
print('FINAL '+json.dumps(summary['nominal'])+' confidence_N='+str(confN),flush=True)
print(f"{sum(c['passed'] for c in checks)}/{len(checks)} checks passed",flush=True)
raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
