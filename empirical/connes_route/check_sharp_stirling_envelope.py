"""Check the analytic sharp-envelope bound; decimals are not interval certificates."""
import json
import math
from pathlib import Path
import mpmath as mp
import numpy as np

mp.mp.dps = 60
N = 100000
prime = np.ones(N+1,dtype=bool); prime[:2] = False
for p in range(2,math.isqrt(N)+1):
    if prime[p]: prime[p*p::p] = False
ps = np.flatnonzero(prime)
mu = np.ones(N+1,dtype=np.int64); mu[0] = 0
for p in ps:
    mu[p::p] *= -1
    mu[p*p::p*p] = 0
M = np.cumsum(mu)

def main(n):
    return (mp.mpf(n)+mp.mpf('0.5'))*mp.log(n)-n

rows=[]
for x in (1000,10000,100000):
    B=1
    while B**6<x: B+=1
    E=mp.mpf(0); exact=mp.mpf(0); width_sum=mp.mpf(0)
    groups=0
    k=1
    while k<=x//2:
        m=x//k; end=x//m
        c=int(M[end]-M[k-1]); l=m//2
        F=mp.loggamma(m+1)-mp.loggamma(l+1)
        if m<=B:
            lo=hi=F
        else:
            center=main(m)-main(l)
            lo=center+mp.mpf(1)/(12*m+1)-mp.mpf(1)/(12*l)
            hi=center+mp.mpf(1)/(12*m)-mp.mpf(1)/(12*l+1)
            assert lo<F<hi
        E+=c*(hi if c>=0 else lo)
        exact+=c*F
        width_sum+=abs(c)*(hi-lo)
        groups+=1; k=end+1
    window=mp.mpf(0)
    for pp in ps:
        p=int(pp)
        if p>x: break
        power=p
        while power<=x:
            if power>x//2: window+=mp.log(p)
            power*=p
    bound=mp.mpf(5)/72*(mp.mpf(x)/(3*B**3)+mp.mpf(1)/B)
    assert abs(exact-window)<mp.mpf('1e-45')
    assert -mp.mpf('1e-45')<=E-window<=width_sum+mp.mpf('1e-45')
    assert width_sum<=bound
    row={'x':x,'B':B,'groups':groups,
         'envelope_minus_window':mp.nstr(E-window,25),
         'weighted_width':mp.nstr(width_sum,25),
         'proved_bound':mp.nstr(bound,25),
         'mobius_identity_residual':mp.nstr(abs(exact-window),5)}
    rows.append(row); print(json.dumps(row),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
