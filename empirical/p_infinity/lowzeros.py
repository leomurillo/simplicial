#!/usr/bin/env python3
"""H3: extract the lowest 6 zeros of each quadratic L-function L(s,chi_D).
Purpose: test whether the chiral (odd) vs real (even) Jensen-margin gap is an ARCHIMEDEAN /
low-lying-zero effect -- i.e. tracks the one-level density (zeros repelled from the center,
symplectic symmetry), with an even/odd Gamma-factor split. Output joins with the d=40 margins.
Zeros via PARI lfunzeros (fast; float64 plenty for the statistics). No torch. Deterministic."""
import sys, csv, argparse
from multiprocessing import Pool

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

def worker(D):
    try:
        import cypari2
        p=cypari2.Pari(); p.set_real_precision(30)
        L=p.lfuncreate(int(D))
        T=50.0; g=[]
        for _ in range(6):
            Z=p.lfunzeros(L, T)
            g=sorted(float(p.real(z)) for z in Z if float(p.real(z))>1e-9)
            if len(g)>=6: break
            T*=1.6
        g6=(g+[float('nan')]*6)[:6]
        return (D, abs(D), 'odd' if D<0 else 'even', g6, 'ok' if len(g)>=6 else 'few')
    except Exception as e:
        return (D, abs(D), 'odd' if D<0 else 'even', [float('nan')]*6, 'err:'+type(e).__name__)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dmax", type=int, default=1000)
    ap.add_argument("--procs", type=int, default=32)
    ap.add_argument("--out", default="lowzeros.csv")
    a=ap.parse_args()
    Ds=[D for D in range(-a.dmax,a.dmax+1) if is_fundamental(D)]
    print(f"[lowzeros] {len(Ds)} fundamental discriminants |D|<={a.dmax}; procs={a.procs}"); sys.stdout.flush()
    rows=[]
    with Pool(a.procs) as pool:
        for i,res in enumerate(pool.imap_unordered(worker, Ds, chunksize=4)):
            rows.append(res)
            if (i+1)%75==0: print(f"[lowzeros] {i+1}/{len(Ds)}"); sys.stdout.flush()
    rows.sort(key=lambda r:r[0])
    with open(a.out,"w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["D","conductor","parity","g1","g2","g3","g4","g5","g6","status"])
        for D,q,par,g,st in rows:
            w.writerow([D,q,par]+["%.10f"%x for x in g]+[st])
    print(f"[lowzeros] wrote {a.out}: {sum(1 for r in rows if r[4]=='ok')}/{len(rows)} ok")

if __name__=="__main__": main()
