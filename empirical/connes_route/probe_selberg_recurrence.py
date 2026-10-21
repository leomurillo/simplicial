"""Finite Selberg recurrence diagnostics; not an RH certificate."""
import json
import math
from pathlib import Path
import numpy as np
from probe_translated_prime_cancellation import prime_powers

limit = 1_000_000
pairs = prime_powers(limit)
ns = np.array([n for n,p in pairs], dtype=np.int64)
weights = np.array([math.log(p) for n,p in pairs])
lam = np.zeros(limit+1)
lam[ns] = weights
psi = np.cumsum(lam)
records = []
for X in [100,1000,10000,100000,1000000]:
    mask = ns <= X
    n, w = ns[mask], weights[mask]
    # R(X/n) uses the real argument X/n, not floor(X/n) in its main term.
    convolution = math.fsum((w*(psi[X//n]-X/n)).tolist())
    R = float(psi[X]-X)
    S = R*math.log(X)+convolution
    norms = {}
    for beta in [.5,.75,.875]:
        exact = math.fsum((w/n.astype(float)**beta).tolist())/math.log(X)
        asymptotic = X**(1-beta)/((1-beta)*math.log(X))
        norms[str(beta)] = {'positive_operator_factor':exact,
                            'asymptotic_factor':asymptotic,
                            'ratio':exact/asymptotic}
    records.append({'X':X,'R':R,'S_over_X':S/X,
                    'centered_S_over_X':S/X+1+.5772156649015328606,
                    'factors':norms})
result = {'status':'Finite numerical diagnostics only','samples':records}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
