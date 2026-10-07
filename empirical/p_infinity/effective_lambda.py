"""Effective de Bruijn-Newman calibration.  The dBN heat flow Phi -> e^{t u^2} Phi acts on the Taylor
coefficients of Xi_chi by an EXACT shift (from d/dt b_m = (2m+1)(2m+2) b_{m+1}):

    b_m(t) = sum_{k>=0} (t^k / k!) * (2m+2k)!/(2m)! * a_{m+k}(0).

At finite degree d the Jensen margin m_d(0) > 0; push t negative and two real Jensen roots collide at
t*_d(chi) < 0 (the margin dies).  RH <=> Lambda = 0 (Rodgers-Tao Lambda >= 0), so t*_d(chi) -> 0^- as
d -> inf: t*_d is a finite-degree image of Lambda.  Measure (i) t*_d -> 0 trend, (ii) chiral/odd
channel has |t*_d| SMALLER (dies sooner, closest to the proven boundary), (iii) correlation of t*_d
with the smear width w(chi) and gamma_1.  This couples the margin tower to the ONE proven theorem
on the axis.  Reuses ms_test (PARI contour).  No torch.  Deterministic."""
import os, sys, csv, argparse
os.environ.setdefault("MDPS","180"); os.environ.setdefault("MNPTS","256"); os.environ.setdefault("MDMAX","44")
import mpmath as mp
from multiprocessing import Pool
import ms_test as M

MFLOW = int(os.environ.get("MDMAX","44"))
DEGS = [int(x) for x in os.environ.get("EDEGS","6,12,18,24").split(",")]

def margin(A, d, n=0):
    if A[n+1]==0: return None
    rho=A[n]/A[n+1]
    coef=[mp.binomial(d,j)*A[n+j]*rho**j for j in range(d+1)]
    roots=mp.polyroots([coef[d-j] for j in range(d+1)], maxsteps=900, extraprec=200)
    im=max(abs(mp.im(r)) for r in roots); re=sorted(mp.re(r) for r in roots)
    if im>mp.mpf(10)**-6*(1+max(abs(x) for x in re)): return None
    sp=re[-1]-re[0]
    if sp==0: return None
    g=[re[i+1]-re[i] for i in range(len(re)-1)]
    return float(min(g)/sp)

def heat(a0, t, d):
    Mav=len(a0)-1; out=[]
    for m in range(d+1):
        s=mp.mpf(0); fact=mp.mpf(1); coef=mp.mpf(1)
        for k in range(0, Mav-m+1):
            if k>0:
                fact*= t/k; coef*= (2*m+2*k-1)*(2*m+2*k)
            s+= fact*coef*a0[m+k]
        out.append(s)
    return out

def alive(a0, t, d):
    # death = the degree-d Jensen polynomial loses real-rootedness (roots collide -> complex).
    # coefficient signs are NOT the criterion (a flowed b_m can go negative while roots stay real).
    b=heat(a0, t, d)
    if b[1]==0: return True            # measure-zero; skip (division guard only)
    return margin(b, d, 0) is not None

def find_tstar(a0, d):
    if not alive(a0, mp.mpf(0), d): return None
    lo=mp.mpf(0); hi=None; t=mp.mpf('-0.0005')
    for _ in range(32):
        if not alive(a0, t, d): hi=t; break
        lo=t; t*=mp.mpf('1.5')
        if t < -10: break
    if hi is None: return None
    for _ in range(30):
        mid=(lo+hi)/2
        if alive(a0, mid, d): lo=mid
        else: hi=mid
    return float((lo+hi)/2)

def worker(D):
    try:
        import cypari2; pari=cypari2.Pari(); pari.set_real_precision(50)
        a=M.taylor_a(M.make_Xi_pari(pari,D), MFLOW, M.radius_for(abs(D)))
        a0=a[0]; a=[x/a0 for x in a]
        if not all(x>0 for x in a[:8]): return (D,abs(D),'odd' if D<0 else 'even',None,"a sign")
        lam=[a[m]*mp.factorial(2*m+1) for m in range(3)]
        w=float(lam[0]*lam[2]/lam[1]**2-1)               # smear width (lambda log-convexity)
        ts={d:find_tstar(a,d) for d in DEGS}
        return (D,abs(D),'odd' if D<0 else 'even',dict(w=w,ts=ts),"ok")
    except Exception as e:
        return (D,abs(D),'odd' if D<0 else 'even',None,"err:"+type(e).__name__)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dmax",type=int,default=120)
    ap.add_argument("--only",default="")
    ap.add_argument("--procs",type=int,default=32)
    ap.add_argument("--out",default="efflambda.csv")
    a=ap.parse_args()
    cand=[int(x) for x in a.only.split(",")] if a.only else list(range(-a.dmax,a.dmax+1))
    Ds=[D for D in cand if M.is_fundamental(D)]
    print("[efflambda] %d chars; dps=%d MFLOW=%d degs=%s"%(len(Ds),mp.mp.dps,MFLOW,DEGS)); sys.stdout.flush()
    rows=[]
    with Pool(a.procs) as pool:
        for i,r in enumerate(pool.imap_unordered(worker,Ds,chunksize=1)):
            rows.append(r)
            if (i+1)%20==0: print("[efflambda] %d/%d"%(i+1,len(Ds))); sys.stdout.flush()
    rows.sort(key=lambda r:r[0])
    with open(a.out,"w",newline="") as f:
        wr=csv.writer(f)
        wr.writerow(["D","conductor","parity","w"]+["tstar_%d"%d for d in DEGS]+["status"])
        for D,q,par,d,st in rows:
            if d: wr.writerow([D,q,par,d['w']]+[d['ts'][dd] for dd in DEGS]+[st])
            else: wr.writerow([D,q,par,""]+[""]*len(DEGS)+[st])
    okrows=[r for r in rows if r[3]]
    print("[efflambda] wrote %s: %d/%d ok"%(a.out,len(okrows),len(rows)))
    for par in ('odd','even'):
        pr=[r for r in okrows if r[2]==par]
        if not pr: continue
        means={}
        for d in DEGS:
            v=[r[3]['ts'][d] for r in pr if r[3]['ts'][d] is not None]
            means[d]=round(sum(v)/len(v),5) if v else None
        print("  %-4s n=%d  mean t*_d = %s"%(par,len(pr),means))
    print("SUMMARY done")

if __name__=="__main__": main()
