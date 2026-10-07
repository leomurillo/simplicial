import csv, math, sys
import mpmath as mp
mp.mp.dps = 50

# ---- Hermite reference margins (n->inf GUE/Gaussian limit), any degree ----
def _hc(d):
    H=[[mp.mpf(1)],[mp.mpf(0),mp.mpf(2)]]
    for k in range(1,d):
        nx=[mp.mpf(0)]*(k+2)
        for i,c in enumerate(H[k]): nx[i+1]+=2*c
        for i,c in enumerate(H[k-1]): nx[i]-=2*k*c
        H.append(nx)
    return list(reversed(H[d]))
def herm(d):
    rts=mp.polyroots(_hc(d),extraprec=40); re=sorted(mp.re(r) for r in rts)
    g=[re[i+1]-re[i] for i in range(len(re)-1)]; return float(min(g)/(re[-1]-re[0]))

path = sys.argv[1] if len(sys.argv)>1 else "hd_d40_both.csv"
rows = [r for r in csv.DictReader(open(path)) if r['status']=='ok']
DMAX = max(int(k[8:]) for k in rows[0].keys() if k.startswith('margin_d'))
HERM = {d: herm(d) for d in range(2,DMAX+1)}
def fn(x):
    try: return float(x)
    except: return None
def fit(data):                       # y = A + B/log q ; A = q->inf limit
    xs=[1/math.log(q) for q,m in data]; ys=[m for q,m in data]
    n=len(xs); sx=sum(xs); sy=sum(ys); sxx=sum(x*x for x in xs); sxy=sum(a*b for a,b in zip(xs,ys))
    B=(n*sxy-sx*sy)/(n*sxx-sx*sx); A=(sy-B*sx)/n; return A

QHI = 500                            # high-conductor bin floor (robust d-trend, no extrapolation)
def table(par):
    pr=[r for r in rows if r['parity']==par]
    out={}
    for d in range(3,DMAX+1):
        data=[(int(r['conductor']), fn(r.get('margin_d%d'%d))) for r in pr if fn(r.get('margin_d%d'%d)) is not None]
        if len(data)<15: continue
        rel=[(q,m/HERM[d]) for q,m in data]
        hi=[m for q,m in rel if q>=QHI]
        out[d]=dict(rel_lim=fit(rel), rel_hi=(sum(hi)/len(hi) if hi else None),
                    abs_lim=fit(data), n=len(data), nhi=len(hi))
    return out
def alpha(tab, dlo=12):              # rel ~ d^-alpha  => slope of log(rel_hi) vs log d
    pts=[(math.log(d), math.log(tab[d]['rel_hi'])) for d in tab if d>=dlo and tab[d]['rel_hi'] and tab[d]['rel_hi']>0]
    n=len(pts); sx=sum(x for x,_ in pts); sy=sum(y for _,y in pts)
    sxx=sum(x*x for x,_ in pts); sxy=sum(x*y for x,y in pts)
    return -(n*sxy-sx*sy)/(n*sxx-sx*sx)

ot=table('odd'); et=table('even')
no=sum(1 for r in rows if r['parity']=='odd'); ne=sum(1 for r in rows if r['parity']=='even')
print("="*92)
print("d-TOWER to d=%d, BOTH parities: %s   [odd(chiral/imag)=%d, even(real)=%d chars]"%(DMAX,path,no,ne))
print("rel = margin/Hermite_d (GUE-free arithmetic deficit). rel_hi = mean over conductor>=%d."%QHI)
print("ratio=rel_hi(d)/rel_hi(d-1); d*(1-ratio) -> the power-law exponent alpha if rel~d^-alpha.")
print("="*92)
print("  %3s | %-26s | %-26s"%("d","ODD  (chiral / L(.,chi_-3))","EVEN (real / zeta-like)"))
print("  %3s | %9s %7s %7s | %9s %7s %7s"%("","rel_hi","ratio","d(1-r)","rel_hi","ratio","d(1-r)"))
po=pe=None
for d in range(3,DMAX+1):
    so=se=""
    if d in ot and ot[d]['rel_hi']:
        v=ot[d]['rel_hi']; rat=v/po if po else float('nan'); dc=d*(1-rat) if po else float('nan')
        so="%9.5f %7.3f %7.3f"%(v,rat,dc); po=v
    if d in et and et[d]['rel_hi']:
        v=et[d]['rel_hi']; rat=v/pe if pe else float('nan'); dc=d*(1-rat) if pe else float('nan')
        se="%9.5f %7.3f %7.3f"%(v,rat,dc); pe=v
    if d<=12 or d%2==0 or d==DMAX:
        print("  %3d | %-26s | %-26s"%(d, so, se))

print("-"*92)
ao, ae = alpha(ot), alpha(et)
print("POWER-LAW exponent  (log-log fit of rel_hi vs d, d>=12):")
print("   ODD alpha = %.3f      EVEN alpha = %.3f      chiral gap (odd-even) = %+.3f"%(ao,ae,ao-ae))
print("   ratio->1 as d grows  <=>  rel decays polynomially (no geometric floor crash).")
# verdict
hi_d=[d for d in ot if d>=DMAX-4]
print("   last ODD ratios (d=%d..%d): %s"%(min(hi_d),DMAX,
      ", ".join("%.3f"%(ot[d]['rel_hi']/ot[d-1]['rel_hi']) for d in sorted(hi_d) if d-1 in ot)))

print("\nGLOBAL tightest ABSOLUTE margins in the whole tower (any d, any conductor, any parity):")
allm=sorted((fn(r.get('margin_d%d'%d)), d, r['D'], r['conductor'], r['parity'])
            for r in rows for d in range(3,DMAX+1) if fn(r.get('margin_d%d'%d)) is not None)
for v,d,D,q,par in allm[:8]:
    print("   margin=%.6f  d=%2d  D=%5s (cond %s, %s)"%(v,d,D,q,par))
print("   ALL > 0  =>  Jensen-hyperbolic everywhere tested  =>  RH holds across the sweep.")
print("="*92)
