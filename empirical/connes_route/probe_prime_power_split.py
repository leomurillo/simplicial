"""Prime-power decomposition and a positive comparison measure.

Finite diagnostics only. The comparison measure is not the prime measure.
"""
import json
import math
from pathlib import Path
import mpmath as mp
from probe_translated_prime_cancellation import prime_powers, g, G

mp.mp.dps = 60
data = prime_powers(2_000_000)
A = float(G(mp.mpf('.5')))
rows = []
for X in [100, 1000, 10000, 100000, 1000000]:
    buckets = [[], [], []]
    for n, p in data:
        if X/2 <= n <= 2*X:
            r = n/X
            weight = 2*r-1/(2*r) if r <= 1 else 2/r-r/2
            index = 0 if n == p else (1 if n == p*p else 2)
            buckets[index].append(math.log(p)/math.sqrt(n)*weight)
    primes, squares, higher = map(math.fsum, buckets)
    rows.append({'X':X,'primes':primes,'squares':squares,'higher_powers':higher,
                 'all_power_discrepancy':primes+squares+higher-A*math.sqrt(X),
                 'prime_discrepancy_with_half_correction':primes-A*math.sqrt(X)+.5,
                 'higher_times_X_to_one_sixth':higher*X**(1/6)})

delta, H = mp.mpf('.25'), mp.mpf(14)
beta = delta+mp.mpf('.5')
z = beta+1j*H
epsilon = 1/(4*abs(z))
a = mp.log(2)
checks = []
for X in [10, 1000, 1000000]:
    # Integrate the oscillatory component separately to avoid cancellation.
    direct = epsilon*mp.re(z*mp.mpf(X)**(delta+1j*H)*mp.quad(
        lambda v:g(v)*mp.exp((delta+1j*H)*v), [-a,0,a]))
    formula = epsilon*mp.re(z*G(delta+1j*H)*mp.mpf(X)**(delta+1j*H))
    checks.append({'X':X,'comparison_discrepancy':mp.nstr(formula,30),
                   'quadrature_error':float(abs(direct-formula))})
out = {'status':'Numerical checks only; comparison measure is not primes',
       'prime_power_samples':rows,
       'comparison_density_lower_bound':.75,
       'comparison_density_upper_bound':1.25,
       'comparison_discrepancy_exponent':str(delta),
       'comparison_checks':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
