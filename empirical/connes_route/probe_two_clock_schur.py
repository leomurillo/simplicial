"""Prime-side overlapping packet Gram and Schur tests. No interval certificate."""
import json
import math
from fractions import Fraction
from pathlib import Path
import mpmath as mp
from probe_translated_prime_cancellation import prime_powers

zooms=[1,2,3,6,4,9,12,18,36]
pairs=prime_powers(72)

def run(dps):
    mp.mp.dps=dps
    a=mp.log(2)
    def g(v):
        u=abs(v)
        return 2*mp.exp(-u)-mp.exp(u)/2 if u<a else mp.mpf(0)
    A=mp.mpf(4)/3*(5-3*mp.sqrt(2))
    cache={}
    def K(ratio):
        ratio=max(ratio,1/ratio)
        if ratio in cache:
            return cache[ratio]
        t=mp.log(mp.mpf(ratio.numerator)/ratio.denominator)
        R=t+a
        h0=g(t)
        def h(v):
            return (g(v-t)+g(v+t))/2
        def integrand(v):
            if v==0:
                return -mp.mpf(7)/4 if t==0 else (mp.mpf(1) if t==a else h0/2)
            return (mp.exp(v/2)*h(v)-h0)/mp.sinh(v)
        cuts=sorted(set([mp.mpf(0),R]+[v for v in [a-t,t-a,t] if 0<v<R]))
        arch=mp.quad(integrand,cuts)
        prime=mp.fsum(mp.log(p)/mp.sqrt(n)*(g(mp.log(n)-t)+g(mp.log(n)+t)) for n,p in pairs)
        value=2*A*mp.cosh(t/2)-h0*(mp.euler+mp.log(4*mp.pi)+mp.log(mp.tanh(R/2)))-arch-prime
        cache[ratio]=value
        return value
    M=mp.matrix([[K(Fraction(j,k)) for k in zooms] for j in zooms])
    q=M[0,0]
    schur=[q]
    for size in range(2,len(zooms)+1):
        old=M[:size-1,:size-1]
        b=M[:size-1,size-1]
        schur.append(q-(b.T*mp.lu_solve(old,b))[0])
    eig=mp.eigsy(M,eigvals_only=True)
    return M,{'dps':dps,'q0':mp.nstr(q,35),
              'zooms':zooms,'normalized_schur_pivots':[mp.nstr(v/q,30) for v in schur],
              'minimum_eigenvalue_over_q0':mp.nstr(eig[0]/q,30),
              'K_values':{str(r):mp.nstr(v,35) for r,v in cache.items()}}

M40,r40=run(40)
M70,r70=run(70)
out={'status':'Arithmetic 40/70-digit cross-check, not interval certification',
     'max_precision_crosscheck_difference':mp.nstr(max(abs(M40[i,j]-M70[i,j]) for i in range(9) for j in range(9)),8),
     'result':r70}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
