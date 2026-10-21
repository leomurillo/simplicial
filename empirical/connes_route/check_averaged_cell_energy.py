"""Exact expansion of averaged hyperbola-cell energy into Mobius pairs."""
import json
import math
from pathlib import Path
import sympy as sp

results = []
for X in (100, 300, 1000):
    L = math.isqrt(X)
    mu = [0] + [int(sp.mobius(n)) for n in range(1, 2*X+1)]
    M = [0]
    for v in mu[1:]:
        M.append(M[-1]+v)
    direct = sum(m*(M[x//m]-M[x//(m+1)])**2
                 for x in range(X+1,2*X+1) for m in range(2,L+1))
    diagonal = positive = negative = 0
    for m in range(2,L+1):
        for a in range((X+1)//(m+1), 2*X//m+1):
            if a < 1 or mu[a] == 0:
                continue
            for b in range(a, min(2*X//m, ((m+1)*a-1)//m)+1):
                if mu[b] == 0:
                    continue
                count = max(0, min(2*X,(m+1)*a-1)-max(X+1,m*b)+1)
                term = m*count*mu[a]*mu[b]
                if a == b:
                    diagonal += term
                elif term >= 0:
                    positive += 2*term
                else:
                    negative += 2*term
    assert direct == diagonal+positive+negative
    row = {'X': X, 'L': L, 'energy': direct, 'diagonal': diagonal,
           'positive_off_diagonal': positive, 'negative_off_diagonal': negative,
           'net_off_diagonal': positive+negative, 'exact_identity': True}
    results.append(row)
    print(json.dumps(row), flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
