"""TEST 3 (the one surviving diagonal): within-family even->odd ratio at MATCHED conductor.
Matched even/odd quadratic characters share |D|=4m only when both +4m and -4m are fundamental,
i.e. m squarefree, m≡2 (mod 4) -> |D| in {8,24,40,56,88,104,...}.  For each such pair form
   mu_m = a_m(chi_{-|D|}) / a_m(chi_{+|D|})    (geometric backbone cancels in the ratio)
and Turán-test mu.  The moment-kill does NOT apply (no kernel identity forces log-convexity of a
ratio of two Xi's), so this is genuinely open: mu Turán-positive deep into the tower => the family is
internally diagonal-comparable => conditional transfer 'even-channel hyperbolic => odd-channel
hyperbolic' is on the table (reduces the critical chiral channel to the zeta-like one)."""
import os, sys
os.environ.setdefault("MDPS","140"); os.environ.setdefault("MNPTS","256"); os.environ.setdefault("MDMAX","40")
import mpmath as mp
from multiprocessing import Pool
import ms_test as M

def squarefree(n):
    n=abs(n); d=2
    while d*d<=n:
        if n%(d*d)==0: return False
        if n%d==0: n//=d
        else: d+=1
    return True

def worker(D):
    try:
        import cypari2; p=cypari2.Pari(); p.set_real_precision(40)
        a=M.taylor_a(M.make_Xi_pari(p,D), M.DMAX, M.radius_for(abs(D)))
        a0=a[0]
        return (D, [x/a0 for x in a])
    except Exception as e:
        return (D, None)

def main():
    Dmax=int(sys.argv[1]) if len(sys.argv)>1 else 1000
    pairs=[4*m for m in range(2, Dmax//4+1) if m%4==2 and squarefree(m)
           and M.is_fundamental(4*m) and M.is_fundamental(-4*m)]
    work=[]
    for D in pairs: work += [D, -D]
    print("Test 3: %d matched even/odd pairs |D|=4m<=%d  (dps=%d, m<=%d)"%(len(pairs),Dmax,mp.mp.dps,M.DMAX)); sys.stdout.flush()
    A={}
    with Pool(min(32,len(work))) as pool:
        for D,a in pool.imap_unordered(worker, work, chunksize=1):
            A[D]=a
    print(" |D|  Turán-pass(mu)   minT   @m   nval   verdict")
    npass_all=0; ntested=0
    for D in pairs:
        ae=A.get(D); ao=A.get(-D)
        if ae is None or ao is None: print(" %4d  compute-failed"%D); continue
        mu=[]
        for m in range(M.DMAX+1):
            if ae[m]<=0 or ao[m]<=0: break
            mu.append(ao[m]/ae[m])
        if len(mu)<8: print(" %4d  few valid (%d)"%(D,len(mu))); continue
        T=[float(mu[m]**2/(mu[m-1]*mu[m+1])) for m in range(1,len(mu)-1)]
        npass=sum(1 for t in T if t>=1.0); minT=min(T); nmin=T.index(minT)+1
        ntested+=1; npass_all += (npass==len(T))
        print(" %4d   %3d/%-3d  %8.4f  %3d  %4d   %s"%(D,npass,len(T),minT,nmin,len(mu),
              "PASS (mu Turán-positive => internally comparable)" if npass==len(T) else "fails Turán"))
    print("-"*70)
    print("SUMMARY: %d/%d matched pairs with mu Turán-positive at ALL shifts."%(npass_all,ntested))
    print("(PASS across the family => the prize hypothesis: a within-family conditional transfer.)")

if __name__=="__main__": main()
