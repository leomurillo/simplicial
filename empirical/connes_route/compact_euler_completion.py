"""Exact certificates for a compact multiplicative taper and balance completion.

Feasibility checks use integers after denominator clearing. Decimal costs are
diagnostics. This family is proved to miss the RH approximation rate.
"""
from fractions import Fraction
from math import prod, lcm
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps=60

def build(primes, weights):
    P=prod(primes)
    c={1:Fraction(1)}
    for p in primes:
        c.update({p*d:-weights[p]*v for d,v in list(c.items())})
    E=prod((1-weights[p]/p for p in primes),start=Fraction(1))
    h=P*E
    a={}
    for d,v in c.items():
        a[d]=a.get(d,Fraction())+v
        a[2*d]=a.get(2*d,Fraction())-v
    a[2*P]-=h
    return P,{d:v for d,v in a.items() if v},E,h

def real(q):
    return mp.mpf(q.numerator)/q.denominator

rows=[]
for bound in (2,3,5,7,11,13):
    primes=[p for p in (2,3,5,7,11,13) if p<=bound]
    for mode in ('full','half_after_3'):
        weights={p:Fraction(1) if mode=='full' or p<=3 else Fraction(1,2) for p in primes}
        P,a,E,h=build(primes,weights)
        L=2*P
        assert sum((v/d for d,v in a.items()),Fraction())==0
        assert a[1]==1 and -sum(a.values())==h
        Q=lcm(*(v.denominator for v in a.values()))
        jumps=[0]*L
        for d,v in a.items():
            for j in range(d,L,d):
                jumps[j]+=int(v*Q)
        values=[]
        running=0
        for jump in jumps:
            running+=jump
            values.append(running)
        assert min(values)==0 and max(values)==h*Q
        assert all(values[j]+values[L-1-j]==h*Q for j in range(L))
        C=-sum(real(v)*mp.log(d)/d for d,v in a.items())
        closed=real(E)/2*(mp.log(4*P)+sum(real(weights[p])*mp.log(p)/(p-real(weights[p])) for p in primes))
        assert abs(C-closed)<mp.mpf('1e-50')
        rows.append({'prime_cutoff':bound,'mode':mode,'period':L,'height':str(h),
                     'C':str(C),'delta':str(C-mp.mpf('.5')),
                     'delta_h':str((C-mp.mpf('.5'))*real(h)),
                     'coefficient_count':len(a),'exact_feasibility':True,
                     'cost_identity_error':str(abs(C-closed))})
        print(json.dumps(rows[-1]),flush=True)

Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
