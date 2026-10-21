"""Exact finite checks of the identification and minimum-operator residual.

Tao's asymptotic theorem is an external mathematical input, not tested here.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def lift(previous, q):
    m = 3 * len(previous)
    length = 2 * m // 3
    orbit = [1]
    for _ in range(1, length):
        orbit.append(2 * orbit[-1] % m)
    forcing = [F(0)] * m
    for j, x in enumerate(previous):
        forcing[1 + 3*j] = x
    f = [forcing[r] for r in orbit]
    g = [F(0)] * length
    g[-1] = sum(((1-q)*q**(a-1)*f[(length-1+a) % length]
                 for a in range(1, length+1)), F(0)) / (1-q**length)
    for j in range(length-2, -1, -1):
        g[j] = q*g[j+1] + (1-q)*f[j+1]
    mu = [F(0)] * m
    for r, x in zip(orbit, g):
        mu[r] = x
    return mu


def main():
    reports = []
    for q, maximum in [(F(1,2), 7), (F(3,5), 5)]:
        previous = [F(1)]
        old_r = None
        for n in range(1, maximum+1):
            mu = lift(previous, q)
            m, size = len(mu), len(previous)
            assert sum(mu) == 1
            triples = [mu[j::size] for j in range(size)]
            assert all(sum(t) == previous[j] for j,t in enumerate(triples))
            osc = sum((sum(abs(x-previous[j]/3) for x in t)
                       for j,t in enumerate(triples)), F(0))
            r = sum((max(t)-min(t) for t in triples), F(0))
            loss = sum((sum(t)-3*min(t) for t in triples), F(0))
            assert r <= osc and r <= loss <= 2*r
            # General averaged operator: lambda=1, alpha=q, beta=3(1-q).
            residual = F(0)
            for j in range(m):
                target = triples[((2*j-1)//3) % size] if j%3 == 2 else [F(0)]*3
                averaged = q*mu[2*j % m] + (1-q)*sum(target)
                minimum = q*mu[2*j % m] + 3*(1-q)*min(target)
                assert averaged == mu[j] and averaged >= minimum
                residual += averaged-minimum
            assert residual == (1-q)*loss
            if q == F(1,2) and n >= 2:
                for j,t in enumerate(triples):
                    assert all(F(2,21)*previous[j] <= x <= F(11,21)*previous[j] for x in t)
                assert old_r/3 <= r <= old_r
            if q == F(1,2) and n == 2:
                assert mu == [F(x,63) for x in (0,8,16,0,11,4,0,2,22)]
            reports.append(dict(q=str(q), n=n, hex_mass=str(r),
                                oscillation=str(osc), lift_loss=str(loss),
                                all_exact_checks_pass=True))
            previous, old_r = mu, r
    output = dict(levels_checked=len(reports), reports=reports,
                  limitation='Finite identities only; asymptotic mixing is cited from Tao Proposition 1.14.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2))
    print(json.dumps(dict(levels_checked=len(reports), all_exact_checks_pass=True)))


if __name__ == '__main__':
    main()
