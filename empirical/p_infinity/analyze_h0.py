"""H0 (model identification): re-normalize the actual Jensen margins by a CONCRETE Laguerre-Polya
reference (the sine / picket-fence function sin(pi t)/(pi t), zeros equally spaced, maximally rigid,
manifestly RH) instead of the Hermite (n->inf) limit. If margin_actual/margin_sine LEVELS at a
positive floor as d->inf, the L-function tracks the rigid ideal up to a bounded factor (strong
RH-safety; the d^-2 vs-Hermite decay was a yardstick artifact). If it ->0, there is genuine extra
arithmetic tightening beyond rigidity, and its rate is the real RH content."""
import csv, math
import mpmath as mp
mp.mp.dps = 60
DMAX = 40

def margin(A, d, n=0):
    if A[n+1] == 0: return None
    rho = A[n]/A[n+1]
    coef = [mp.binomial(d, j)*A[n+j]*rho**j for j in range(d+1)]
    roots = mp.polyroots([coef[d-j] for j in range(d+1)], maxsteps=900, extraprec=200)
    im = max(abs(mp.im(r)) for r in roots); re = sorted(mp.re(r) for r in roots)
    if im > mp.mpf(10)**-6*(1+max(abs(x) for x in re)): return None
    sp = re[-1]-re[0]
    if sp == 0: return None
    g = [re[i+1]-re[i] for i in range(len(re)-1)]
    return float(min(g)/sp)

# --- references ---
# sine kernel  sin(pi t)/(pi t) = sum (-1)^m (pi)^2m t^2m/(2m+1)!  -> a_m ∝ 1/(2m+1)! (scale-invariant)
Asine = [mp.mpf(1)/mp.factorial(2*m+1) for m in range(DMAX+1)]
Msine = {d: margin(Asine, d, 0) for d in range(2, DMAX+1)}
# Hermite (n->inf GORZ limit), for context
def _hc(d):
    H=[[mp.mpf(1)],[mp.mpf(0),mp.mpf(2)]]
    for k in range(1,d):
        nx=[mp.mpf(0)]*(k+2)
        for i,c in enumerate(H[k]): nx[i+1]+=2*c
        for i,c in enumerate(H[k-1]): nx[i]-=2*k*c
        H.append(nx)
    return list(reversed(H[d]))
def herm(d):
    r=mp.polyroots(_hc(d),extraprec=40); re=sorted(mp.re(x) for x in r)
    g=[re[i+1]-re[i] for i in range(len(re)-1)]; return float(min(g)/(re[-1]-re[0]))
HERM = {d: herm(d) for d in range(2, DMAX+1)}

print("="*82)
print("H0: reference margins -- Hermite (n->inf) vs sine/picket-fence (rigid LP function)")
print("="*82)
print("  %3s | %10s %10s | %10s   <- does a concrete LP fn also decay vs Hermite?"%("d","Hermite","sine","sine/Herm"))
for d in [2,3,4,6,8,12,16,20,28,40]:
    print("  %3d | %10.5f %10.5f | %10.4f"%(d, HERM[d], Msine[d], Msine[d]/HERM[d]))

rows = [r for r in csv.DictReader(open("hd_d40_both.csv")) if r['status']=='ok']
def fn(x):
    try: return float(x)
    except: return None

print("\nactual margin / sine margin  (mean over conductor>=500), ratio = value(d)/value(d-1):")
print("  if ratio -> 1  the actual margins track the rigid sine ideal (a positive FLOOR).")
print("  %3s | %-26s | %-26s"%("d","ODD (chiral)","EVEN (real)"))
print("  %3s | %12s %8s | %12s %8s"%("","m/m_sine","ratio","m/m_sine","ratio"))
res={}
for par in ('odd','even'):
    pr=[r for r in rows if r['parity']==par and int(r['conductor'])>=500]
    seq={}
    for d in range(3, DMAX+1):
        vals=[fn(r.get('margin_d%d'%d))/Msine[d] for r in pr if fn(r.get('margin_d%d'%d)) is not None]
        if vals: seq[d]=sum(vals)/len(vals)
    res[par]=seq
po=pe=None
for d in range(3, DMAX+1):
    so=se=""
    if d in res['odd']:
        v=res['odd'][d]; rt=v/po if po else float('nan'); so="%12.5f %8.4f"%(v,rt); po=v
    if d in res['even']:
        v=res['even'][d]; rt=v/pe if pe else float('nan'); se="%12.5f %8.4f"%(v,rt); pe=v
    if d in (3,4,5,6,8,10,12,16,20,24,28,32,36,40):
        print("  %3d | %-26s | %-26s"%(d, so, se))

# verdict: power-law fit of m/m_sine vs d over d>=12
def alpha(seq, dlo=12):
    pts=[(math.log(d), math.log(seq[d])) for d in seq if d>=dlo and seq[d]>0]
    n=len(pts); sx=sum(x for x,_ in pts); sy=sum(y for _,y in pts)
    sxx=sum(x*x for x,_ in pts); sxy=sum(x*y for x,y in pts)
    return -(n*sxy-sx*sy)/(n*sxx-sx*sx)
print("-"*82)
print("power-law exponent of m_actual/m_sine (d>=12):  ODD=%.3f  EVEN=%.3f"%(alpha(res['odd']), alpha(res['even'])))
print("  (exponent ~0  => FLOOR: actual tracks the rigid ideal.  exponent >0 => extra tightening.)")
print("  last ODD ratios d=36..40:", ", ".join("%.4f"%(res['odd'][d]/res['odd'][d-1]) for d in range(37,41)))
print("="*82)
