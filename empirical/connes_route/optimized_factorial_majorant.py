"""Find prime-independent floor majorants; certify rational feasibility exactly.

Numerical optimization is a search only. The output certificate consists of
rational coefficients and verification of every floor inequality required at x.
No assertion of exact optimality or of an asymptotic error bound is made.
"""
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
import sympy as sp

rows = []
for x in (1000, 4000, 10000):
    K = math.isqrt(x) + (math.isqrt(x)**2 < x)
    ys = np.arange(1, x//2 + 1, dtype=np.int64)[:, None]
    ks = np.arange(1, K + 1, dtype=np.int64)[None, :]
    A = ys//ks - ys//(2*ks)
    b = np.zeros(x//2); b[0] = 1
    costs = np.array([math.lgamma(x//k+1)-math.lgamma(x//(2*k)+1)
                      for k in range(1, K+1)])
    solution = linprog(costs, A_ub=-A, b_ub=-b,
                       bounds=[(None,None)]*K, method='highs')
    if not solution.success:
        raise RuntimeError(solution.message)
    c = [Fraction(float(v)).limit_denominator(10000) for v in solution.x]
    correction = Fraction(0)
    for y, row in enumerate(A, 1):
        value = sum((int(a)*v for a,v in zip(row,c)), Fraction(0))
        correction = max(correction, (int(y == 1)-value)/int(row[0]))
    c[0] += correction
    Q = math.lcm(*(v.denominator for v in c))
    integers = [int(v*Q) for v in c]
    slack = [sum(int(a)*v for a,v in zip(row, integers))-Q*int(y==1)
             for y,row in enumerate(A,1)]
    assert min(slack) >= 0
    height = math.fsum(float(v)*cost for v,cost in zip(c,costs))
    # Independent reference value; primes do not enter the optimization.
    window = 0.0
    for p in sp.primerange(2,x+1):
        power = p
        while power <= x:
            if power > x//2:
                window += math.log(p)
            power *= p
    result = {'x': x, 'K': K, 'coefficients': [str(v) for v in c],
              'multiplicity': Q, 'min_integer_slack': min(slack),
              'rational_repair': str(correction),
              'normalized_log_height_approx': height,
              'height_minus_x_over_2_approx': height-x/2,
              'height_minus_prime_window_approx': height-window,
              'excess_over_sqrt_x_approx': (height-x/2)/math.sqrt(x),
              'exact_feasibility': True}
    rows.append(result)
    print(json.dumps({k:v for k,v in result.items() if k != 'coefficients'}), flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows, indent=2)+'\n', encoding='utf-8')
