"""Prospective two-mode variance-ratio test; tests declared before execution.

Check stored one-mode model consistency <1e-9; selected pair covariance from
dense/adjoint calculations <1e-9; nominal simultaneous orthogonality <1e-9;
exact correlated-ratio formula reduces to F law <1e-12, agrees with Wishart
Monte Carlo within six standard errors, and gives conservative envelope power;
common scaling invariance <1e-12; commuting angle identity <1e-12.
No calibration box is certified by finite stress samples.
"""
from pathlib import Path
import sys,os,json
import numpy as np
from scipy.linalg import eigh
from scipy.stats import f as fdist, wishart
import rc_record_model as rc

OUT=Path(__file__).resolve().parent/'two_mode';OUT.mkdir(exist_ok=True)
checks=[]
def check(name,ok,detail):
    checks.append(dict(name=name,passed=bool(ok),detail=detail))
    print(('PASS ' if ok else 'FAIL ')+name+': '+str(detail),flush=True)

def projected_pair(s,W):
    ell=np.outer(s['H'],W[-1]); V=np.stack([s['rv']*(W.T@W)]*2)
    for j in range(len(W)-1,0,-1):
        for h in [0,1]: V[h]+=ell.T@s[f'Q{h}']@ell
        ell=np.outer(s['H'],W[j-1])+s['F'].T@ell
    V+=ell.T@s['P']@ell
    return V

def tail(S,t,N):
    a,b,c=S[0,0],S[1,1],S[0,1]
    disc=np.sqrt((a+t*b)**2-4*t*c*c)
    # Eigenvalues of Sigma^(1/2) diag(1,-t) Sigma^(1/2).
    q=(disc-a+t*b)/(disc+a-t*b)
    return float(fdist.sf(q,N-1,N-1))
def fpower(r,N,alpha=.05):
    return float(fdist.sf(fdist.ppf(1-alpha,N-1,N-1)/r,N-1,N-1))
def budget(r,alpha=.05,target=.9):
    if r<=1:return None
    lo=2;hi=2
    while fpower(r,hi,alpha)<target and hi<10**8:hi*=2
    if hi>=10**8:return None
    while lo<hi:
        mid=(lo+hi)//2
        if fpower(r,mid,alpha)>=target:hi=mid
        else:lo=mid+1
    return lo

base=rc.state();V0,V1,_=rc.records(base)
old=np.load(OUT.parent/'stress'/'nominal_projection.npz')
oldv=rc.projected(base,old['weights'])
check('unchanged record model',np.max(abs(oldv-[old['v0'],old['v1']]))<1e-9,oldv.tolist())
eig,W=eigh(V1,V0)
P0,P1,_=rc.records(rc.state(noise_sd_factor=0))
fraction=np.einsum('ij,ij->j',W,P0@W) # all W columns have nominal v0=1
# Exclude detector-dominated modes; never choose the reset sample as reference.
eligible=np.flatnonzero((fraction>=.9)&(np.arange(len(eig))<len(eig)-1))
j=int(eligible[np.argmin(eig[eligible])])
pair=W[:,[-1,j]]; S=projected_pair(base,pair)
ratios=S[:,0,0]/S[:,1,1]; contrast=float(ratios[1]/ratios[0])
N=budget(contrast); threshold=ratios[0]*fdist.ppf(.95,N-1,N-1)
dense=np.stack([pair.T@V0@pair,pair.T@V1@pair])
check('two-mode dense versus adjoint',np.max(abs(S-dense))<1e-9,float(np.max(abs(S-dense))))
check('nominal modes independent under both models',np.max(abs(S[:,0,1]))<1e-9,S.tolist())
check('nominal exact budget',tail(S[1],threshold,N)>=.9 and fpower(contrast,N-1)<.9,
      dict(reference_index=j,reference_eigenvalue=float(eig[j]),reference_plant_fraction=float(fraction[j]),
           signal_plant_fraction=float(fraction[-1]),contrast=contrast,N=N,power=tail(S[1],threshold,N)))

# Verify exact paired correlated law independently using Wishart draws.
rng=np.random.default_rng(6011); errors=[]; tol=[]
for aa,rho in [(1.,.7),(1.64,-.5),(1.64,0.)]:
    cov=np.array([[aa,rho*np.sqrt(aa)],[rho*np.sqrt(aa),1.]])
    nt=40;th=1.2;pred=tail(cov,th,nt)
    draws=wishart.rvs(df=nt-1,scale=cov,size=150000,random_state=rng)
    observed=float(np.mean(draws[:,0,0]/draws[:,1,1]>th))
    se=np.sqrt(pred*(1-pred)/len(draws));errors.append((observed-pred)/se)
    tol.append(dict(rho=rho,predicted=pred,observed=observed,standard_errors=float(errors[-1])))
check('correlated ratio law versus Wishart draws',max(abs(x) for x in errors)<6,tol)
err=abs(tail(np.diag([1.64,1]),1.2,40)-fdist.sf(1.2/1.64,39,39))
check('independent reduction and common scale invariance',err<1e-12 and
      abs(tail(S[1]*37,threshold,N)-tail(S[1],threshold,N))<1e-12,float(err))
# When threshold lies between bounded variance ratios, zero correlation is worst.
r=contrast*.95/1.05; NN=budget(r);th=fdist.ppf(.95,NN-1,NN-1)
okay=True
for rho in np.linspace(-.99,.99,51):
    null=np.array([[1,rho],[rho,1]])
    alt=np.array([[r,rho*np.sqrt(r)],[rho*np.sqrt(r),1]])
    okay &= tail(null,th,NN)<=.05+1e-12 and tail(alt,th,NN)>=fpower(r,NN)-1e-12
check('correlation-safe envelope inequality',okay,dict(ratio=r,N=NN))

# Same raw device draws as the previous scalar stress study.
rng=np.random.default_rng(6009);raw=[]
for z in range(64):
    lp=np.zeros(rc.NPAR);lp[:-5]=np.log1p(rng.uniform(-.05,.05,rc.NPAR-5))
    SS=projected_pair(rc.state(lp),pair)
    raw.append(dict(size=tail(SS[0],threshold,N),power=tail(SS[1],threshold,N),
                    r0=float(SS[0,0,0]/SS[0,1,1]),r1=float(SS[1,0,0]/SS[1,1,1]),
                    rho0=float(SS[0,0,1]/np.sqrt(SS[0,0,0]*SS[0,1,1])),
                    rho1=float(SS[1,0,1]/np.sqrt(SS[1,0,0]*SS[1,1,1]))))
rawsum={key:[min(x[key] for x in raw),max(x[key] for x in raw)] for key in raw[0]}
print('RAW '+json.dumps(rawsum),flush=True)

grad=np.empty((2,rc.NPAR));eps=1e-4
for i in range(rc.NPAR):
    lp=np.zeros(rc.NPAR);lp[i]=eps
    plus=projected_pair(rc.state(lp),pair);minus=projected_pair(rc.state(-lp),pair)
    grad[:,i]=(np.log(plus[:,0,0]/plus[:,1,1])-np.log(minus[:,0,0]/minus[:,1,1]))/(2*eps)
cal=[]
for label,comp,fcunc,gunc,tunc,nunc in [('tight',.01,.02,.01,.005,.1),('loose',.05,.1,.03,.02,.2)]:
    unc=np.r_[np.full(rc.NPAR-5,comp),fcunc,gunc,tunc,nunc,nunc];bounds=np.log1p(unc)
    candidates=[np.zeros(rc.NPAR)]
    for h in [0,1]:candidates.extend([bounds*np.sign(grad[h]),-bounds*np.sign(grad[h])])
    candidates.extend(rng.uniform(-1,1,rc.NPAR)*bounds for _ in range(64))
    vals=np.array([projected_pair(rc.state(lp),pair) for lp in candidates])
    rvals=vals[:,:,0,0]/vals[:,:,1,1]
    r0max=float(max(rvals[:,0]));r1min=float(min(rvals[:,1]))
    needed=max(r0max/ratios[0]-1,1-r1min/ratios[1],0)
    u=float(np.ceil((needed+.02)*100)/100)
    robust=contrast*(1-u)/(1+u)
    NN=budget(robust);Nc=budget(robust,alpha=.04,target=.9/.99)
    row=dict(label=label,samples=len(vals),r0max=r0max,r1min=r1min,
             first_order_log_ratio_box=np.sum(abs(grad)*bounds,axis=1).tolist(),
             rounded_ratio_envelope=u,N=NN,N_99pct_coverage=Nc,
             direct_sampled_envelope_N=budget(r1min/r0max))
    cal.append(row);print('CAL '+json.dumps(row),flush=True)

scale=[]
for param,index in [('hardware_gain',-4),('temperature',-3)]:
    for factor in [.5,1.,2.]:
        lp=np.zeros(rc.NPAR);lp[index]=np.log(factor)
        SS=projected_pair(rc.state(lp),pair)
        scale.append(dict(parameter=param,factor=factor,size=tail(SS[0],threshold,N),
                          power=tail(SS[1],threshold,N),ratios=(SS[:,0,0]/SS[:,1,1]).tolist()))
band=[]
for fc in [1.,3.,10.,30.,100.,300.]:
    ss=rc.state(fc=fc);A,B,_=rc.records(ss); ev,U=eigh(B,A)
    PP,_,_=rc.records(rc.state(fc=fc,noise_sd_factor=0))
    frac=np.einsum('ij,ij->j',U,PP@U)
    eligible=np.flatnonzero((frac>=.9)&(np.arange(len(ev))<len(ev)-1))
    jj=int(eligible[np.argmin(ev[eligible])])
    rr=float(ev[-1]/ev[jj])
    band.append(dict(fc_Hz=fc,reference_eigenvalue=float(ev[jj]),contrast=rr,N=budget(rr)))

# Angle identity: rotated commuting C and B^T B, including a dark mode.
rng=np.random.default_rng(631);maxerr=0.
for z in range(12):
    U,_=np.linalg.qr(rng.normal(size=(3,3)))
    c=np.exp(rng.uniform(-2,2,3));b=np.exp(rng.uniform(-2,2,3));b[0]=0
    C=(U*c)@U.T;F=(U*np.sqrt(c*c+b*b))@U.T;Cr=(U*np.sqrt(c))@U.T
    Pi=np.eye(3)-2*Cr@np.linalg.solve(C+F,Cr)
    angle=np.tan(.5*np.arctan(b/c))**2
    maxerr=max(maxerr,float(np.max(abs(Pi-(U*angle)@U.T))))
check('commuting coupling-angle identity',maxerr<1e-12,maxerr)

env=[]
for u in [0,.02,.03,.05,.1,.15,.2,.25]:
    rr=contrast*(1-u)/(1+u);env.append(dict(ratio_uncertainty=u,contrast=rr,N=budget(rr)))
result=dict(status='prospective exact Gaussian ratio test; no measured calibration',checks=checks,
            nominal=dict(N=N,power=tail(S[1],threshold,N),size=tail(S[0],threshold,N),
                         covariance=S.tolist(),contrast=contrast,reference_eigenvalue=float(eig[j]),
                         reference_plant_fraction=float(fraction[j]),threshold=float(threshold)),
            raw_component_mismatch=rawsum,calibration=cal,ratio_envelopes=env,
            scale_sweeps=scale,bandwidth=band,
            log_sensitivities=[dict(parameter=rc.names[i],null=float(grad[0,i]),thermal=float(grad[1,i]))
                              for i in np.argsort(-np.max(abs(grad),axis=0))[:12]])
with (OUT/'results.json').open('x',encoding='utf-8') as ff:json.dump(result,ff,indent=2)
np.savez(OUT/'projection.npz',weights=pair,times_seconds=np.arange(rc.STEPS+1)*.0005)
sys.path.insert(0,str(Path(os.environ['TEMP'])/'boundary60-plot-deps'))
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(11,4.2),layout='constrained')
prior=json.load(open(OUT.parent/'stress'/'stress_results.json'))
ax[0].semilogy([100*x['relative_variance_bound'] for x in prior['variance_envelopes']],
               [x['N'] if x['N'] is not None else np.nan for x in prior['variance_envelopes']],'o-',label='One variance: bound on variance')
ax[0].semilogy([100*x['ratio_uncertainty'] for x in env],
               [x['N'] if x['N'] is not None else np.nan for x in env],'s-',label='Two modes: bound on ratio')
ax[0].set(xlabel='Relative calibration bound (%)',ylabel='Independent records',title='A  Estimating a denominator costs precision')
ax[0].legend(fontsize=8)
ax[1].bar(['One mode\nknown scale','Two modes\nknown shape','One mode\ntight scenario','Two modes\ntight scenario'],
           [prior['nominal']['N'],N,prior['tight_99pct_envelope_allocation']['N'],cal[0]['N_99pct_coverage']])
ax[1].set(ylabel='Independent records',title='B  Tight-scenario envelopes remain conditional')
fig.suptitle('PROSPECTIVE TWO-MODE TEST — gain cancellation versus sampling cost')
for a in ax:a.grid(axis='y',alpha=.2)
fig.savefig(OUT/'comparison.png',dpi=180);fig.savefig(OUT/'comparison.svg');plt.close(fig)
print('FINAL '+json.dumps(result['nominal']),flush=True)
print(f"{sum(c['passed'] for c in checks)}/{len(checks)} checks passed",flush=True)
raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
