"""Multiplier-sequence test, well-conditioned form (Turan-ratio domination).
T_m = a_m / a~_m  with a~_m = sine coeffs (∝ 1/(2m+1)!).  {T_m} is a multiplier sequence only if it
is log-concave AT EVERY SHIFT n (the 2nd-order / Turan condition of Polya-Schur).  Termwise:
   T_{n+1}^2 >= T_n T_{n+2}   <=>   tau_n(a) := a_{n+1}^2/(a_n a_{n+2}) >= tau_n(sine).
tau_n(sine) = (2n+4)(2n+5)/((2n+2)(2n+3))  (exact).  Scale-invariant; no root-finding; the dominant
geometric backbone cancels in the ratio (unlike the ill-conditioned Jensen-margin-of-T).  H0 already
showed margin domination at the infimum shift n=0; this tests the multiplier-sequence condition at
ALL shifts.  R_n = tau_n(a)/tau_n(sine) >= 1 for all n  =>  {T} log-concave at every shift => the
'rigid sine backbone x multiplier-sequence correction' model holds to 2nd order.
Local mpmath (low conductor) or PARI (box, high conductor).  No torch.  Deterministic."""
import sys, os, argparse, mpmath as mp
from multiprocessing import Pool
mp.mp.dps = int(os.environ.get("MDPS", "90"))
NPTS = int(os.environ.get("MNPTS", "256"))
DMAX = int(os.environ.get("MDMAX", "40"))

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
def kronecker(a,n):
    if n==0: return 1 if abs(a)==1 else 0
    res=1
    if n<0:
        n=-n
        if a<0: res=-res
    if n%2==0:
        if a%2==0: return 0
        while n%2==0:
            n//=2
            if a%8 in (3,5): res=-res
    a%=n
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): res=-res
        a,n=n,a
        if a%4==3 and n%4==3: res=-res
        a%=n
    return res if n==1 else 0
def make_Xi_mpmath(D):
    q=abs(D); eps=1 if D<0 else 0
    chi=[kronecker(D,a) for a in range(q)]
    def L(s): return q**(-s)*mp.fsum(chi[a]*mp.zeta(s, mp.mpf(a)/q) for a in range(1,q) if chi[a])
    def Xi(t):
        s=mp.mpf(1)/2+1j*t
        return (q/mp.pi)**((s+eps)/2)*mp.gamma((s+eps)/2)*L(s)
    return Xi
def make_Xi_pari(pari, D):
    Lf=pari.lfuncreate(int(D)); nd=mp.mp.dps+5; bits=int(mp.mp.dps*3.3219)+40
    PSC=pari(10)**nd; rnd=pari("round"); rl=pari("real"); im=pari("imag"); den=mp.mpf(10)**nd
    def Xi(t):
        tr=pari(mp.nstr(mp.re(t),nd)); ti=pari(mp.nstr(mp.im(t),nd))
        s=pari("1/2")+pari("I")*(tr+ti*pari("I"))
        z=pari.lfunlambda(Lf,s,precision=bits)
        return mp.mpc(mp.mpf(int(rnd(rl(z)*PSC)))/den, mp.mpf(int(rnd(im(z)*PSC)))/den)
    return Xi
def radius_for(q): return max(mp.mpf('0.4'), min(mp.mpf('0.6'), mp.mpf('2.5')/(2+mp.log(q))))
def taylor_a(Xi, M, r):
    pts=[Xi(r*mp.e**(2j*mp.pi*j/NPTS)) for j in range(NPTS)]
    out=[]
    for m in range(M+1):
        c=mp.fsum(pts[j]*mp.e**(-2j*mp.pi*(2*m)*j/NPTS) for j in range(NPTS))/(NPTS*r**(2*m))
        out.append((-1)**m*mp.re(c))
    return out

def worker(item):
    D, backend = item
    try:
        pari=None
        if backend in ("auto","pari"):
            try:
                import cypari2; pari=cypari2.Pari(); pari.set_real_precision(40)
            except Exception: pari=None
        Xi = make_Xi_pari(pari,D) if pari is not None else make_Xi_mpmath(D)
        a = taylor_a(Xi, DMAX, radius_for(abs(D)))
        a0=a[0]; a=[x/a0 for x in a]
        if not all(x>0 for x in a[:8]):
            return (D, abs(D), 'odd' if D<0 else 'even', None, "a_m sign (low)")
        R=[]
        for n in range(DMAX-1):
            if a[n]<=0 or a[n+1]<=0 or a[n+2]<=0: break    # stop at the precision floor (high a_m -> noise)
            tau_a=a[n+1]**2/(a[n]*a[n+2])
            tau_s=mp.mpf((2*n+4)*(2*n+5))/((2*n+2)*(2*n+3))
            R.append(float(tau_a/tau_s))
        if len(R) < 12:
            return (D, abs(D), 'odd' if D<0 else 'even', None, "few valid n (%d)"%len(R))
        def g(i): return R[i] if i < len(R) else float('nan')
        Rmin=min(R); nmin=R.index(Rmin); bad=[n for n,r in enumerate(R) if r<1.0]
        return (D, abs(D), 'odd' if D<0 else 'even',
                dict(Rmin=Rmin, nmin=nmin, nbad=len(bad), nvalid=len(R),
                     R0=g(0), R10=g(10), R20=g(20), R38=g(DMAX-2)), "ok")
    except Exception as e:
        return (D, abs(D), 'odd' if D<0 else 'even', None, "err:"+type(e).__name__)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dmax_disc", type=int, default=120)
    ap.add_argument("--only", default="")
    ap.add_argument("--procs", type=int, default=4)
    ap.add_argument("--backend", choices=["auto","pari","mpmath"], default="mpmath")
    a=ap.parse_args()
    cand=[int(x) for x in a.only.split(",")] if a.only else list(range(-a.dmax_disc, a.dmax_disc+1))
    Ds=[D for D in cand if is_fundamental(D)]
    print("="*96)
    print("TURAN-RATIO MULTIPLIER-SEQUENCE TEST  R_n=tau_n(actual)/tau_n(sine)>=1 ?  (dps=%d, n<=%d, %d chars)"%(mp.mp.dps,DMAX-2,len(Ds)))
    print("R_n>=1 at every n  =>  T log-concave at every shift => 2nd-order MS-domination holds.")
    print("="*96)
    print("  %5s %4s | %8s %5s %5s %5s | %7s %7s %7s %7s"%("D","par","min R_n","@n","#R<1","nval","R_0","R_10","R_20","R_38"))
    res=[]
    with Pool(a.procs) as pool:
        for r in pool.imap_unordered(worker, [(D,a.backend) for D in Ds], chunksize=1):
            res.append(r)
    res.sort(key=lambda r:r[0])
    nfail=0
    for D,q,par,d,st in res:
        if st!="ok": print("  %5d %4s | %s"%(D,par,st)); continue
        flag="" if d['nbad']==0 else "  <-- R<1!"
        if d['nbad']>0: nfail+=1
        print("  %5d %4s | %8.4f %5d %5d %5d | %7.3f %7.3f %7.3f %7.3f%s"%(
            D,par,d['Rmin'],d['nmin'],d['nbad'],d['nvalid'],d['R0'],d['R10'],d['R20'],d['R38'],flag))
    ok=[r for r in res if r[3]]
    print("-"*96)
    print("SUMMARY: %d/%d characters with R_n>=1 at ALL shifts (2nd-order MS-domination);  %d violate."%(
        len(ok)-nfail, len(ok), nfail))
    if ok:
        allmin=min(r[3]['Rmin'] for r in ok); worst=[r for r in ok if r[3]['Rmin']==allmin][0]
        print("global min R_n over all chars = %.4f  (D=%d, n=%d)"%(allmin, worst[0], worst[3]['nmin']))
    print("="*96)

if __name__=="__main__": main()
