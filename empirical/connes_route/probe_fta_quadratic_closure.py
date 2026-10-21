"""Arithmetic Hilbert-distance diagnostics; classical NB framework, no RH proof."""
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import digamma
import mpmath as mp

def gram(m,n):
    period=math.lcm(m,n)
    r=np.arange(1,period+1,dtype=float)
    weights=(digamma((r+1)/period)-digamma(r/period))/period
    return float(np.dot((r % m)/m*(r % n)/n,weights))

rows=[]
for N in [4,8,12,24]:
    ns=list(range(2,N+1))
    H=np.array([[gram(m,n) for n in ns] for m in ns])
    b=np.log(ns)/np.array(ns)
    a=np.linalg.solve(H,-b)
    value=1+2*np.dot(a,b)+a@H@a
    a1=-sum(a[j]/n for j,n in enumerate(ns))
    rows.append({'N':N,'quadratic_distance_squared':float(value),
                 'matrix_condition_number':float(np.linalg.cond(H)),
                 'pole_constraint_residual':float(a1+sum(a[j]/n for j,n in enumerate(ns))),
                 'a_1':float(a1),'a_2_through_N':a.tolist()})

mp.mp.dps=60
m,n=3,8
L=math.lcm(m,n)
exact_high=mp.fsum(mp.mpf(k%m)/m*mp.mpf(k%n)/n*(
    mp.digamma(mp.mpf(k+1)/L)-mp.digamma(mp.mpf(k)/L))/L for k in range(1,L+1))
out={'status':'Numerical distances, not interval certificates or a proof of convergence',
     'samples':rows,'mp60_check_H_3_8_error':float(abs(exact_high-gram(3,8))),
     'DH_fixed_mobius_convolution_at_6':2}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'samples':[{k:v for k,v in r.items() if k not in ['a_2_through_N']} for r in rows]},indent=2))
