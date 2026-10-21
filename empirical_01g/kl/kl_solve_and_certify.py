"""Paper 01g Section 12.8: worst-case-lift Perron solver for the Krasikov-Lagarias linear programs L_k^NT(lambda).
Usage: python kl_solve_and_certify.py <outdir> k1 k2 ... ; writes kl_cert_k{k}.npy (principal variables, min=1) and kl_cert_summary.json.
Verify each output independently with verify_kl_certificate.py."""
import numpy as np, math, sys, time, json
sys.stdout.reconfigure(encoding="utf-8")
OUT=sys.argv[1]; KS=[int(a) for a in sys.argv[2:]]
alpha=math.log2(3)
def build(k):
    M=3**k; r=np.arange(M,dtype=np.int64)
    even=(2*r)%M; live=(r%3!=0); odd_ok=(r%3==2)
    q=((2*r-1)//3)%(M//3)
    lifts=np.stack([(q+j*(M//3))%M for j in range(3)],axis=1)
    return M,even,live,odd_ok,lifts
def eig(Bk,g,c0=None,tol=1e-13,iters=50000):
    M,even,live,odd_ok,lifts=Bk
    c=live.astype(float) if c0 is None else c0.copy(); c/=c.sum(); lam=0
    for it in range(iters):
        new=np.where(live,2**(-g)*c[even]+np.where(odd_ok,(1.5**g)*c[lifts].min(1),0.0),0.0)
        s=new.sum(); new/=s
        if it>30 and abs(s-lam)<tol: return s,new
        lam=s; c=new
    return lam,c
def kl_check(k,lam_,c):
    # KL linear program L_k^NT(lambda): principal variables c_k^m for m = 2 mod 3 (mod 3^k); auxiliary c_{k-1}^m = min over the 3 lifts (2.15)
    M=3**k; m=np.arange(M); prin=(m%3==2)
    ck=c.copy(); ck=ck/ck[prin].min()                # normalize min principal = 1   (L0)
    def aux(idx):                                   # c_{k-1}^{idx mod 3^(k-1)} = min over lifts mod 3^k
        b=idx%(M//3); return np.minimum(np.minimum(ck[b],ck[b+M//3]),ck[b+2*(M//3)])
    L=lam_; viol=0.0; slack_min=np.inf
    m2=m[prin & (m%9==2)]; rhs=ck[(4*m2)%M]*L**-2+aux(((4*m2-2)//3))*L**(alpha-2); s=(rhs-ck[m2])/ck[m2]
    slack_min=min(slack_min,s.min())
    m5=m[prin & (m%9==5)]; rhs=ck[(4*m5)%M]*L**-2; s=(rhs-ck[m5])/ck[m5]; slack_min=min(slack_min,s.min())
    m8=m[prin & (m%9==8)]; rhs=ck[(4*m8)%M]*L**-2+aux(((2*m8-1)//3))*L**(alpha-1); s=(rhs-ck[m8])/ck[m8]
    slack_min=min(slack_min,s.min())
    return slack_min, ck[prin].max(), ck[prin].mean()*1.0
res={}
B={}
cprev=None
for k in KS:
    t=time.time(); B[k]=build(k)
    lo,hi=0.80,0.92; c=None
    while hi-lo>2e-6:
        mid=(lo+hi)/2; lam,c2=eig(B[k],mid,c)
        if lam>=1: lo=mid; c=c2
        else: hi=mid
    gcrit=lo
    gcert=math.floor((gcrit-2e-5)*1e4)/1e4         # certify a value safely below the critical exponent
    lam,cc=eig(B[k],gcert,c)
    slack,cmax,cmean=kl_check(k,2**gcert,cc)
    M=3**k; m=np.arange(M); prin=(m%3==2); ck=cc/cc[prin].min()
    b=np.arange(M//3); prin1=(b%3==2)
    aux=np.minimum(np.minimum(ck[b],ck[b+M//3]),ck[b+2*(M//3)])
    cbar_kk=ck[prin].sum()/3**(k-1); cbar_k1=aux[prin1].sum()/3**(k-2)
    np.save(f"{OUT}/kl_cert_k{k}.npy",ck[prin].astype(np.float64))
    res[k]=dict(gamma_crit=gcrit,gamma_cert=gcert,lambda_cert=2**gcert,eig_at_cert=lam,min_rel_slack=float(slack),Cmax=float(cmax),cbar_kk=float(cbar_kk),cbar_k1k=float(cbar_k1),ratio=float(cbar_k1/cbar_kk),secs=time.time()-t)
    print(f"k={k}: critical gamma {gcrit:.6f}; certified gamma {gcert:.4f} (eigenvalue {lam:.8f}); KL (L1)-(L3) min relative slack {slack:.3e}; Cmax {cmax:.2f}; cbar_kk {cbar_kk:.4f} cbar_k-1,k {cbar_k1:.4f} ratio {cbar_k1/cbar_kk:.4f} ({time.time()-t:.0f}s)",flush=True)
    json.dump(res,open(f"{OUT}/kl_cert_summary.json","w"),indent=1)
