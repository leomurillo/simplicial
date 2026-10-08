import numpy as np, itertools, math, sys
from collections import defaultdict
from worm_fit import ewald_green, E, A1
def classes(fn):
    d=np.load(fn,allow_pickle=True).item(); hist=d['hist']; lam=d['lam']; nc=d['nc']; closed=d['closed']
    L=round(nc**(1/3)); cells=np.array(list(itertools.product(range(L),repeat=3)))
    agg=defaultdict(int)
    for (t,h),c in hist.items():
        ct=cells[t%nc]; ch=cells[h%nc]
        agg[(t>=nc, h>=nc, tuple((ch-ct)%L))]+=c
    G,xi=ewald_green(L); rows=[]
    shifts=[np.array(s) for s in itertools.product((-1,0,1),repeat=3)]
    for (tt,ht,dc),c in agg.items():
        base=np.array(dc)
        off=(E[0] if ht else 0)-(E[0] if tt else 0)
        dv=min(((base+L*s)@A1+off for s in shifts), key=np.linalg.norm)
        R=lam*c/(closed*nc)
        rows.append((np.linalg.norm(dv), G(dv)-xi, R, c))
    return L, np.array(rows)
if __name__=='__main__':
    K=float(sys.argv[1]); files=sys.argv[2:]
    for fn in files:
        L,rows=classes(fn)
        for rmin in (1.5,2.0,2.5):
            sel=rows[:,0]>=rmin; w=rows[sel,3]
            Rinf_i=rows[sel,2]*np.exp(-4*K*rows[sel,1])
            Rinf=np.sum(w*Rinf_i)/np.sum(w); sd=np.sqrt(np.sum(w*(Rinf_i-Rinf)**2)/np.sum(w))
            # free slope fit for consistency
            X=np.vstack([np.ones(sel.sum()),rows[sel,1]]).T; Wd=np.diag(w)
            beta=np.linalg.solve(X.T@Wd@X,X.T@Wd@np.log(rows[sel,2]))
            print(f'L={L} r>={rmin}: classes {sel.sum():4d}, raw mean R {np.average(rows[sel,2],weights=w):.4f}, R_inf(K={K}) = {Rinf:.4f} (scatter {sd:.4f}); free-slope K = {beta[1]/4:.3f}, R_inf(free) = {math.exp(beta[0]):.4f}')
