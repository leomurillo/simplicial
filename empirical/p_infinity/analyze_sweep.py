import csv, math, sys
path = sys.argv[1] if len(sys.argv) > 1 else "sweep_d2000.csv"
rows = list(csv.DictReader(open(path)))
def fn(x):
    try: return float(x)
    except: return None
TOWER = [2,3,4,5,6,7,8]
HERM = {2:1.0,3:0.5,4:0.3178,5:0.2372,6:0.1855,7:0.1539,8:0.1301}

def fit_loglim(data):  # margin = A + B/log q ; return A (q->inf limit), B
    xs=[1/math.log(q) for q,m in data]; ys=[m for q,m in data]
    n=len(xs); sx=sum(xs); sy=sum(ys); sxx=sum(x*x for x in xs); sxy=sum(x*y for x,y in zip(xs,ys))
    B=(n*sxy-sx*sy)/(n*sxx-sx*sx); A=(sy-B*sx)/n; return A,B

print("="*80); print(f"Jensen d-tower sweep analysis: {path}  ({len(rows)} characters)"); print("="*80)
nok = sum(1 for r in rows if r['status']=='ok')
print(f"ok={nok}/{len(rows)}; odd={sum(1 for r in rows if r['parity']=='odd')}, even={sum(1 for r in rows if r['parity']=='even')}")

# --- d3 margin trend vs conductor, by parity ---
print("\n[d=3 cubic margin vs conductor, binned by parity]  (the chiral/uniform question)")
bins=[(2,100),(100,500),(500,1500),(1500,3000),(3000,6000),(6000,10001)]
for par in ('odd','even'):
    data=[(int(r['conductor']),fn(r['margin_d3'])) for r in rows if r['parity']==par and fn(r['margin_d3']) is not None]
    print(f"  {par.upper()} ({len(data)} pts):")
    for lo,hi in bins:
        v=[m for q,m in data if lo<=q<hi]
        if v: print(f"     q[{lo:>4},{hi:>4}): n={len(v):>3}  mean={sum(v)/len(v):.4f}  min={min(v):.4f}")
    A,B=fit_loglim(data)
    print(f"     FIT  margin = {A:.4f} + {B:.4f}/log q   ->  q->inf LIMIT = {A:.4f}  "
          f"({'POSITIVE (uniform bound)' if A>0.02 else 'NEAR 0 (marginal)'})")

# --- parity effect, matched conductor (same |D| both signs is rare; bin-compare) ---
print("\n[parity effect: mean d3 margin per conductor-bin, odd vs even]")
for lo,hi in bins:
    o=[fn(r['margin_d3']) for r in rows if r['parity']=='odd'  and lo<=int(r['conductor'])<hi and fn(r['margin_d3'])]
    e=[fn(r['margin_d3']) for r in rows if r['parity']=='even' and lo<=int(r['conductor'])<hi and fn(r['margin_d3'])]
    if o and e:
        print(f"  q[{lo:>4},{hi:>4}): odd={sum(o)/len(o):.4f}  even={sum(e)/len(e):.4f}  "
              f"odd-even={sum(o)/len(o)-sum(e)/len(e):+.4f}  {'odd tighter' if sum(o)/len(o)<sum(e)/len(e) else 'even tighter'}")

# --- d-tower: relative margins (margin/Hermite) -> arithmetic deficit; infimum ---
print("\n[d-tower: q->inf limit of the RELATIVE margin (margin/Hermite_d), odd family]")
print("   d : limit(rel)   Hermite   absolute-limit   #pts")
for d in TOWER:
    data=[(int(r['conductor']), fn(r[f'margin_d{d}'])) for r in rows if r['parity']=='odd' and fn(r[f'margin_d{d}']) is not None]
    if len(data)<20: print(f"   {d} : (only {len(data)} pts)"); continue
    rel=[(q, m/HERM[d]) for q,m in data]
    Ar,_=fit_loglim(rel); Aa,_=fit_loglim(data)
    print(f"   {d} : {Ar:.4f}      {HERM[d]:.4f}    {Aa:.4f}        {len(data)}")
print("   (rel-limit near 1 = Hermite/GUE-free; below 1 = arithmetic tightening that PERSISTS to q->inf)")

# --- global minimum margin (the tightest cell anywhere) ---
print("\n[global tightest d=3 margins (the empirical RH-critical extremes)]")
alld3=sorted([(fn(r['margin_d3']), r['D'], r['conductor'], r['parity']) for r in rows if fn(r['margin_d3'])])
for m,D,q,par in alld3[:6]:
    print(f"   margin={m:.4f}  D={D} (cond {q}, {par})")
print("="*80)
