"""H3: is the chiral (odd) vs real (even) Jensen-margin gap an ARCHIMEDEAN / low-lying-zero effect?
Join the lowest zeros with the d=40 margins. Test (A) symplectic signature (zeros repelled from
center), (B) mechanism: does the margin track the low zeros?, (C) does the even/odd low-zero
difference predict the even/odd margin gap (chiral channel = the one sitting closest to center)?"""
import csv, math

LZ = {r['D']: r for r in csv.DictReader(open("lowzeros.csv")) if r.get('status')=='ok'}
MG = {r['D']: r for r in csv.DictReader(open("hd_d40_both.csv")) if r['status']=='ok'}
def fn(x):
    try: return float(x)
    except: return None

data=[]
for D,z in LZ.items():
    if D not in MG: continue
    g=[fn(z['g%d'%k]) for k in range(1,7)]
    if any(v is None for v in g): continue
    q=int(z['conductor']); par=z['parity']
    u1=g[0]*math.log(q/(2*math.pi))/(2*math.pi)        # scaled lowest zero (Riemann-von Mangoldt density)
    delta=(g[5]-g[0])/5.0                               # local mean spacing (convention-free)
    v1=g[0]/delta if delta>0 else None                 # lowest zero / local spacing
    data.append(dict(D=D,q=q,par=par,g1=g[0],g2=g[1],u1=u1,v1=v1,gap=g[1]-g[0],
                     m3=fn(MG[D].get('margin_d3')), m40=fn(MG[D].get('margin_d40'))))

def stats(xs):
    n=len(xs); m=sum(xs)/n; sd=(sum((x-m)**2 for x in xs)/n)**0.5; return n,m,sd,min(xs)
def pearson(xs,ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    sx=(sum((x-mx)**2 for x in xs))**0.5; sy=(sum((y-my)**2 for y in ys))**0.5
    return sum((x-mx)*(y-my) for x,y in zip(xs,ys))/(sx*sy) if sx*sy else float('nan')

print("="*80)
print("H3: low-lying zeros vs the chiral Jensen-margin gap  (%d chars joined)"%len(data))
print("="*80)
print("\n[A] scaled lowest zero u1 = g1*log(q/2pi)/(2pi).  symplectic => zeros REPELLED from 0.")
for par in ('odd','even','all'):
    n,m,sd,lo=stats([d['u1'] for d in data if par=='all' or d['par']==par])
    n2,mv,sd2,lo2=stats([d['v1'] for d in data if (par=='all' or d['par']==par) and d['v1']])
    print("   %4s: n=%3d  mean u1=%.4f (sd %.3f, min %.4f)   mean v1=g1/spacing=%.4f"%(par,n,m,sd,lo,mv))

print("\n[B] MECHANISM -- correlation of margin with low-zero observables (Pearson r):")
for par in ('odd','even'):
    sub=[d for d in data if d['par']==par and d['m40'] is not None and d['v1']]
    print("   %4s (n=%d):"%(par,len(sub)))
    for lab,f in [("g1 lowest zero",lambda d:d['g1']),("u1 scaled g1",lambda d:d['u1']),
                  ("v1 g1/spacing",lambda d:d['v1']),("first gap g2-g1",lambda d:d['gap'])]:
        xs=[f(d) for d in sub]
        r3=pearson(xs,[d['m3'] for d in sub]); r40=pearson(xs,[d['m40'] for d in sub])
        print("       r(%-16s, m3)=%+.3f   r(%-16s, m40)=%+.3f"%(lab,r3,lab,r40))

print("\n[C] EVEN vs ODD by conductor bin:  mean u1  and  mean m40  (odd is the tighter channel)")
print("   %-13s | %14s | %14s | %s"%("q bin","ODD u1 / m40","EVEN u1 / m40","contrast"))
for lo,hi in [(2,200),(200,500),(500,800),(800,1001)]:
    o=[d for d in data if d['par']=='odd'  and lo<=d['q']<hi and d['m40']]
    e=[d for d in data if d['par']=='even' and lo<=d['q']<hi and d['m40']]
    if o and e:
        ou=sum(d['u1'] for d in o)/len(o); om=sum(d['m40'] for d in o)/len(o)
        eu=sum(d['u1'] for d in e)/len(e); em=sum(d['m40'] for d in e)/len(e)
        print("   q[%4d,%4d) | %.3f / %.2e | %.3f / %.2e | du1=%+.3f  m40 odd/even=%.3f"%(
            lo,hi,ou,om,eu,em, ou-eu, om/em))
print("="*80)
print("READ: if r(u1,m40) is strong => margin IS controlled by the lowest zero (archimedean).")
print("      if odd has smaller u1 (lowest zero closer to center) AND smaller m40, the chiral")
print("      channel's tighter margin = its lowest zero sitting closer to the center = the")
print("      archimedean Gamma-factor (eps=1) imprint -> the one-level-density / repulsion gap.")
print("="*80)
