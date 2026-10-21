"""Exact rational verification of saved finite-level subeigenvectors.

No claim the saved gamma is the exact critical exponent. Coefficient LOWER
bounds use positive rational Taylor series with proved geometric tail bounds.
All row inequalities are evaluated as fractions, not floating point.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent


def log_bounds(z, n=20):
    t = (z-1)/(z+1)
    assert 0 < t < 1
    lo = 2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)), F(0))
    tail = 2*t**(2*n+1)/((2*n+1)*(1-t*t))
    return lo, lo+tail


def exp_bounds(x, n=20):
    assert 0 <= x < 1
    term = F(1); lo = term
    for j in range(1,n+1):
        term *= x/j; lo += term
    first = term*x/(n+1)
    tail = first/(1-x/F(n+2))
    return lo, lo+tail


def ratio(x):
    return [str(x.numerator),str(x.denominator)]


def main():
    results = []
    for path in sorted(HERE.glob('visibility_potential_k*.npz')):
        k = int(path.stem.split('_k')[-1]); data = np.load(path)
        gamma = F(float(data['gamma']))
        c = [F(float(x)) for x in data['c']]
        v = [F(float(x)) for x in data['v']]
        eps = F(float(data['epsilon']))-F(1,10**9)
        log2lo, log2hi = log_bounds(F(2))
        log15lo, log15hi = log_bounds(F(3,2))
        alpha_lo = 1/exp_bounds(gamma*log2hi)[1]
        beta_lo = exp_bounds(gamma*log15lo)[0]
        m = len(c); live = [r for r in range(m) if r % 3]
        assert m == 3**(k+1)
        assert 0 < gamma < 1 and eps > 0
        assert all(0 < v[r] <= c[r] for r in live)
        assert all(c[r] == v[r] == 0 for r in range(0,m,3))
        margins = []
        for r in live:
            out = alpha_lo*v[(2*r)%m]
            if r % 3 == 2:
                q = ((2*r-1)//3) % (m//3)
                out += beta_lo*min(v[q+j*(m//3)] for j in range(3))
            margin = out-v[r]-eps*c[r]
            assert margin >= 0, (k,r)
            margins.append(margin/c[r])
        result = dict(k=k,level=k+1,parameter_gamma=ratio(gamma),epsilon=ratio(eps),
                      alpha_lower=ratio(alpha_lo),beta_lower=ratio(beta_lo),
                      rows_checked=len(live),all_exact_inequalities_pass=True,
                      epsilon_decimal=float(eps),minimum_normalized_margin_decimal=float(min(margins)))
        results.append(result)
        print(json.dumps({key:result[key] for key in ('k','rows_checked','epsilon_decimal','minimum_normalized_margin_decimal','all_exact_inequalities_pass')}),flush=True)
    assert results, 'No saved potentials found'
    HERE.joinpath('visibility_potentials_exact_results.json').write_text(json.dumps({
        'claim':'At each recorded exact rational gamma, Phi(v) >= v + epsilon*c >= (1+epsilon)*v. This does not certify gamma equals gamma_k.',
        'method':'Exact rational rows; atanh log series and exponential series with geometric upper tails.',
        'results':results},indent=2))


if __name__ == '__main__': main()
