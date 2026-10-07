"""Analyze the effective de Bruijn-Newman calibration.
t*_d(chi) = the t<0 where the degree-d Jensen margin dies under the dBN heat flow = a finite-degree
image of Lambda.  RH <=> Lambda=0 (Rodgers-Tao Lambda>=0), so |t*_d| should march to 0 as d (and
conductor) grow.  Robust claims use d=24 (highest, smallest |t*|, least flow-truncation); low-d points
(large |t*|) carry flow-truncation error from finite MFLOW and are shown but not extrapolated."""
import csv, math, sys
path = sys.argv[1] if len(sys.argv)>1 else "efflambda.csv"
EL=[r for r in csv.DictReader(open(path)) if r['status']=='ok']
try: LZ={r['D']:r for r in csv.DictReader(open("lowzeros.csv")) if r.get('status')=='ok'}
except: LZ={}
def fn(x):
    try: return float(x)
    except: return None
DEGS=[int(c[6:]) for c in EL[0] if c.startswith('tstar_')]
data=[]
for r in EL:
    ts={d:fn(r['tstar_%d'%d]) for d in DEGS}
    if any(ts[d] is None for d in DEGS): continue
    g1=fn(LZ[r['D']]['g1']) if r['D'] in LZ else None
    data.append(dict(D=r['D'],q=int(r['conductor']),par=r['parity'],w=fn(r['w']),ts=ts,g1=g1))
def pear(xs,ys):
    n=len(xs)
    if n<3: return float('nan')
    mx=sum(xs)/n;my=sum(ys)/n
    sx=(sum((x-mx)**2 for x in xs))**.5;sy=(sum((y-my)**2 for y in ys))**.5
    return sum((x-mx)*(y-my) for x,y in zip(xs,ys))/(sx*sy) if sx*sy else float('nan')

print("="*80)
print("EFFECTIVE de BRUIJN-NEWMAN: t*_d(chi) -> 0 couples the margin tower to Rodgers-Tao Lambda>=0")
print("  %s  (%d chars: %d odd, %d even)"%(path,len(data),
      sum(1 for x in data if x['par']=='odd'),sum(1 for x in data if x['par']=='even')))
print("="*80)
dhi=max(DEGS)
print("\n[1] mean t*_d by degree  (|t*_d| should DECREASE toward 0 as d grows = consistent with Lambda=0)")
for par in ('odd','even'):
    pr=[x for x in data if x['par']==par]
    if pr: print("  %-4s n=%d:  %s"%(par,len(pr),
        {d: round(sum(x['ts'][d] for x in pr)/len(pr),4) for d in DEGS}))
print("  (low-d / large-|t*| points carry flow-truncation error; trust the high-d march)")

print("\n[2] even vs odd  |t*_%d|  by conductor bin  (chiral closest to boundary => SMALLER |t*|)"%dhi)
qs=sorted(x['q'] for x in data); bins=[(2,40),(40,80),(80,120),(120,200)]
for lo,hi in bins:
    o=[abs(x['ts'][dhi]) for x in data if x['par']=='odd'  and lo<=x['q']<hi]
    e=[abs(x['ts'][dhi]) for x in data if x['par']=='even' and lo<=x['q']<hi]
    if o and e:
        print("  q[%3d,%3d): odd |t*|=%.3f (n=%d)   even=%.3f (n=%d)   odd/even=%.3f"%(
            lo,hi,sum(o)/len(o),len(o),sum(e)/len(e),len(e),(sum(o)/len(o))/(sum(e)/len(e))))

print("\n[3] what sets the distance-to-boundary |t*_%d| ?  (Pearson r)"%dhi)
allx=data; sub=[x for x in data if x['g1'] is not None]
print("  r(log conductor, |t*|) = %+.3f   (n=%d)"%(pear([math.log(x['q']) for x in allx],[abs(x['ts'][dhi]) for x in allx]),len(allx)))
if len(sub)>=3:
    print("  r(gamma_1,       |t*|) = %+.3f   (n=%d)"%(pear([x['g1'] for x in sub],[abs(x['ts'][dhi]) for x in sub]),len(sub)))
print("  r(smear w,       |t*|) = %+.3f   (n=%d)"%(pear([x['w'] for x in allx],[abs(x['ts'][dhi]) for x in allx]),len(allx)))
if len(sub)>=3:
    print("  r(smear w,    gamma_1) = %+.3f   (n=%d)"%(pear([x['w'] for x in sub],[x['g1'] for x in sub]),len(sub)))

# kernel-positivity events (w<0): the flagged exceptions
neg=[x for x in data if x['w'] is not None and x['w']<0]
print("\n[4] kernel-positivity events (w<0, lambda NOT a moment sequence): %d/%d"%(len(neg),len(data)))
for x in sorted(neg,key=lambda z:z['w'])[:8]:
    print("     D=%5s (%s, cond %d)  w=%.3f  |t*_%d|=%.3f"%(x['D'],x['par'],x['q'],x['w'],dhi,abs(x['ts'][dhi])))
print("="*80)
