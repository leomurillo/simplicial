#!/usr/bin/env python3
"""
HIGH-d Jensen tower via ZEROS (Newton's identities) -- the RH-bearing joint (d->inf, q->inf) infimum.

Xi_chi(t)/Xi_chi(0) = prod_k (1 - t^2/gamma_k^2) = sum_m (-1)^m e_m t^{2m},  e_m = elem. symm. of {1/gamma^2}.
So a_m = e_m (margins are scale-invariant). Compute e_m from power sums P_j = sum_k 1/gamma_k^{2j} via
Newton-Girard -- EXACT to any order d, high precision, NO contour/radius issue (the contour method was
precision-limited past d~8). Zeros from PARI lfunzeros (fast). RH question: does the relative margin
margin_d / Hermite_d at n=0 LEVEL at a positive floor as d->inf (uniform hyperbolicity) or ->0 (marginal)?

Backends: cypari2 (lfunzeros) on the box; local validation uses mpmath zeta zeros (reproduce d3~0.287).
Usage:  python jensen_dtower_zeros.py --dmax 1500 --tower 24 --kzeros 220 --procs 32 --parity odd --out z.csv
        python jensen_dtower_zeros.py --validate            # local mpmath self-test (no PARI)
No torch. Deterministic.
"""
import sys, csv, argparse, math
import mpmath as mp
from multiprocessing import Pool

# Hermite reference margins (n->inf limit)
def _herm(d):
    H=[[mp.mpf(1)],[mp.mpf(0),mp.mpf(2)]]
    for k in range(1,d):
        nx=[mp.mpf(0)]*(k+2)
        for i,c in enumerate(H[k]): nx[i+1]+=2*c
        for i,c in enumerate(H[k-1]): nx[i]-=2*k*c
        H.append(nx)
    rts=mp.polyroots(list(reversed(H[d])),extraprec=40); re=sorted(mp.re(r) for r in rts)
    g=[re[i+1]-re[i] for i in range(len(re)-1)]; return float(min(g)/(re[-1]-re[0]))

def coeffs_from_zeros(gammas, dmax):
    # power sums of x_k = 1/gamma_k^2 ; Newton -> elementary symmetric e_m = a_m
    P=[mp.fsum(mp.mpf(1)/mp.mpf(g)**(2*j) for g in gammas) for j in range(1,dmax+1)]
    e=[mp.mpf(1)]
    for m in range(1,dmax+1):
        e.append(mp.fsum((-1)**(j-1)*e[m-j]*P[j-1] for j in range(1,m+1))/m)
    return e

def margin(A,d,n=0):
    if A[n+1]==0: return None
    rho=A[n]/A[n+1]
    coef=[mp.binomial(d,j)*A[n+j]*rho**j for j in range(d+1)]
    roots=mp.polyroots([coef[d-j] for j in range(d+1)],maxsteps=600,extraprec=120)
    im=max(abs(mp.im(r)) for r in roots); re=sorted(mp.re(r) for r in roots)
    if im>mp.mpf(10)**-8*(1+max(abs(x) for x in re)): return None
    sp=re[-1]-re[0]
    if sp==0: return None
    g=[re[i+1]-re[i] for i in range(len(re)-1)]
    return float(min(g)/sp)

def tower_margins(gammas, dmax):
    A=coeffs_from_zeros(gammas,dmax)
    if not all(mp.re(x)>0 for x in A[:min(6,dmax+1)]): return None
    return {d:margin(A,d,0) for d in range(2,dmax+1)}

# ---------------- number theory (fundamental discriminants) ----------------
def squarefree(n):
    n=abs(n); d=2
    while d*d<=n:
        if n%(d*d)==0: return False
        if n%d==0: n//=d
        else: d+=1
    return True
def is_fundamental(D):
    if D in (0,1): return False
    if D%4==1: return squarefree(D)
    if D%4==0:
        m=D//4; return (m%4 in (2,3)) and squarefree(m)
    return False

# ---------------- worker (PARI lfunzeros) ----------------
def worker(item):
    D, K, dmax, dps = item
    try:
        import cypari2
        p=cypari2.Pari(); p.set_real_precision(dps)
        L=p.lfuncreate(int(D))
        # estimate height for K zeros, request, grow if needed
        q=abs(D); T=max(30.0, 5.0*K/max(1.0,math.log(q)+1)); gammas=[]
        for _ in range(6):
            Z=p.lfunzeros(L, T)
            gammas=[mp.mpf(str(p.real(z))) for z in Z]
            gammas=[g for g in gammas if g>0]
            if len(gammas)>=K: break
            T*=1.7
        if len(gammas)<K: return (D,q,'odd' if D<0 else 'even',len(gammas),{}, "few_zeros")
        gammas=sorted(gammas)[:K]
        mp.mp.dps=dps
        tm=tower_margins(gammas, dmax)
        if tm is None: return (D,q,'odd' if D<0 else 'even',len(gammas),{}, "coeffs<=0")
        return (D,q,'odd' if D<0 else 'even',float(gammas[0]),tm, "ok")
    except Exception as ex:
        return (D,abs(D),'odd' if D<0 else 'even',None,{}, f"err:{type(ex).__name__}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--validate",action="store_true")
    ap.add_argument("--dmax",type=int,default=1500); ap.add_argument("--tower",type=int,default=24)
    ap.add_argument("--kzeros",type=int,default=220); ap.add_argument("--procs",type=int,default=8)
    ap.add_argument("--dps",type=int,default=80); ap.add_argument("--parity",choices=["odd","even","both"],default="odd")
    ap.add_argument("--out",default="jensen_dtower_zeros.csv")
    a=ap.parse_args()

    if a.validate:
        mp.mp.dps=a.dps
        gam=[mp.im(mp.zetazero(n)) for n in range(1,a.kzeros+1)]
        tm=tower_margins(gam, a.tower)
        print(f"[validate] zeta, K={a.kzeros} zeros, tower d=2..{a.tower}, dps={a.dps}")
        for d in range(2,a.tower+1):
            h=_herm(d); m=tm[d]
            print(f"   d={d:>2}: margin={m if m is None else round(m,5)}  Hermite={h:.5f}  rel={None if m is None else round(m/h,4)}")
        return

    DT=list(range(2,a.tower+1)); HERM={d:_herm(d) for d in DT}
    Ds=[D for D in range(-a.dmax,a.dmax+1) if is_fundamental(D) and
        (a.parity=='both' or (a.parity=='odd')==(D<0))]
    print(f"[ztower] {len(Ds)} chars (parity={a.parity}); tower d=2..{a.tower}; K={a.kzeros} zeros; dps={a.dps}; procs={a.procs}")
    sys.stdout.flush()
    work=[(D,a.kzeros,a.tower,a.dps) for D in Ds]
    rows=[]
    with Pool(a.procs) as pool:
        for i,res in enumerate(pool.imap_unordered(worker,work,chunksize=1)):
            rows.append(res)
            if (i+1)%25==0: print(f"[ztower] {i+1}/{len(Ds)}"); sys.stdout.flush()
    rows.sort(key=lambda r:r[0])
    with open(a.out,"w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["D","conductor","parity","gamma1"]+[f"m_d{d}" for d in DT]+[f"rel_d{d}" for d in DT]+["status"])
        for D,q,par,g1,tm,st in rows:
            mv=[tm.get(d) for d in DT]; rv=[(tm.get(d)/HERM[d]) if tm.get(d) is not None else None for d in DT]
            w.writerow([D,q,par,g1]+mv+rv+[st])
    print(f"[ztower] wrote {a.out}: {sum(1 for r in rows if r[5]=='ok')}/{len(rows)} ok; Hermite={ {d:round(HERM[d],4) for d in DT} }")

if __name__=="__main__":
    main()
