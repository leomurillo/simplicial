"""Exact rational tests for prime Helmert coordinates and Syracuse hexagonal norm.

No floating-point pass/fail arithmetic. Decimal outputs are display only.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from sympy import factorint, primerange


def packet(e):
    n=len(e)
    return sum(e),[sum(e[:k])-k*e[k] for k in range(1,n)]


def reconstruct(mass,balances):
    n=len(balances)+1
    out=[F(mass,n)]*n
    for k,b in enumerate(balances,1):
        x=F(b,k*(k+1))
        for j in range(k): out[j]+=x
        out[k]-=k*x
    return out


def metric(e,f):
    return len(e)*sum(x*y for x,y in zip(e,f))-sum(e)*sum(f)


def hexnorm(p): return max(abs(p[0]),abs(p[1]),abs(p[0]-p[1]))
def conjugate(p): return (p[0]-p[1],-p[1])
def twist_conjugate(p,c): return conjugate(p) if c==0 else (p[1],p[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def half(a): return (a[0]/2,a[1]/2)
def rails(p): return (p[0],p[1],p[0]-p[1])


def main():
    primes=list(primerange(1,101)); checks=0
    for value in range(1,1001):
        facts=factorint(value)
        if any(p>97 for p in facts): continue
        e=[int(facts.get(p,0)) for p in primes]
        mass,b=packet(e)
        assert reconstruct(mass,b)==e; checks+=1
        assert metric(e,e)==len(e)*sum((F(x*x,k*(k+1)) for k,x in enumerate(b,1)),F(0)); checks+=1
        nextmass,nextb=packet(e+[0])
        assert nextb==b+[mass] and nextmass==mass; checks+=1
        assert F(metric(e+[0],e+[0]),len(e)+1)-F(metric(e,e),len(e))==F(mass*mass,len(e)*(len(e)+1)); checks+=1
    for u in range(-10,11):
        for v in range(-10,11):
            z=(F(u),F(v)); q=u*u-u*v+v*v; h=hexnorm(z)
            assert q<=h*h and 3*h*h<=4*q; checks+=1
            for carry in (0,1):
                t=twist_conjugate(z,carry)
                assert hexnorm(t)==h and t[0]*t[0]-t[0]*t[1]+t[1]*t[1]==q; checks+=1
    print(json.dumps({'exact_ladder_and_metric_checks':checks}),flush=True)
    previous=[F(1)]; oldz=None; oldR=None; levels=[]
    for n in range(1,8):
        m=3**n; period=2*3**(n-1); orbit=[1]
        for _ in range(1,period): orbit.append(2*orbit[-1]%m)
        forcing=[F(0)]*m
        for j,x in enumerate(previous): forcing[1+3*j]=x
        f=[forcing[r] for r in orbit]; g=[F(0)]*period
        g[-1]=sum((f[(period-1+a)%period]/2**a for a in range(1,period+1)),F(0))/(1-F(1,2**period))
        for j in range(period-2,-1,-1): g[j]=(f[j+1]+g[j+1])/2
        mu=[F(0)]*m
        for r,x in zip(orbit,g): mu[r]=x
        assert sum(mu)==1
        size=m//3
        z=[(mu[j]-mu[j+2*size],mu[j+size]-mu[j+2*size]) for j in range(size)]
        R=sum(map(hexnorm,z),F(0))
        row=dict(n=n,hex_mass_numerator=str(R.numerator),hex_mass_denominator=str(R.denominator),hex_mass_decimal=float(R))
        if oldz is not None:
            deficit=F(0); contexts=0; signed_totals=[F(0)]*3; opposite_counts=[0]*3
            for j in range(size):
                a=z[2*j%size]
                b=oldz[((2*j-1)//3)%(size//3)] if j%3==2 else (F(0),F(0))
                assert z[j]==half(twist_conjugate(add(a,b),int(2*j>=size)))
                gap=hexnorm(a)+hexnorm(b)-hexnorm(add(a,b))
                assert gap>=0
                signed_gap=F(0)
                for axis,(x,y) in enumerate(zip(rails(a),rails(b))):
                    contribution=min(abs(x),abs(y)) if x*y<0 else F(0)
                    signed_totals[axis]+=contribution
                    opposite_counts[axis]+=int(x*y<0)
                    signed_gap+=contribution
                assert signed_gap==gap
                deficit+=gap; contexts+=1
            assert oldR-R==deficit and 0<R<=oldR
            delta=1-R/oldR
            row.update(contexts_exactly_checked=contexts,defect_numerator=str(delta.numerator),
                       defect_denominator=str(delta.denominator),n_times_defect_decimal=float(n*delta),
                       signed_overlap_fractions=[float(x/deficit) if deficit else 0. for x in signed_totals],
                       opposite_sign_context_counts=opposite_counts,
                       all_exact_identities_pass=True)
        levels.append(row)
        print(json.dumps({k:v for k,v in row.items() if not k.endswith(('numerator','denominator'))}),flush=True)
        previous,oldz,oldR=mu,z,R
    p=list(primerange(1,24))
    examples=[]
    for start in (15,33):
        end=3*start+1
        while end%2==0: end//=2
        e=[int(factorint(start).get(x,0)) for x in p]
        f=[int(factorint(end).get(x,0)) for x in p]
        examples.append(dict(start=start,end=end,N=len(p),energy_before=metric(e,e),energy_after=metric(f,f)))
    Path(__file__).with_suffix('.json').write_text(json.dumps({'exact_checks':checks,'hex_ladder':levels,'height_energy_counterexamples':examples},indent=2))


if __name__=='__main__': main()
