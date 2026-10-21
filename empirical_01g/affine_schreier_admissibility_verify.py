"""Exact arithmetic audit; no external dependencies and no asymptotic claim."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def compose(f, g):
    return f[0] * g[0], f[0] * g[1] + f[1]


def inverse(f):
    return 1 / f[0], -f[1] / f[0]


def comm(f, g):
    return compose(compose(compose(f, g), inverse(f)), inverse(g))


def odd_step(n):
    z = 3 * n + 1
    s = 0
    while z % 2 == 0:
        s += 1
        z //= 2
    return z, s


def prefixes(w):
    S = C = 0
    result = []
    for j, s in enumerate(w, 1):
        C = 3 * C + 2**S
        S += s
        result.append((j, S, C))
    return result


def main():
    a, b, t, c = (F(2), F(0)), (F(3), F(1)), (F(1), F(1)), (F(3), F(0))
    assert comm(a, b) == t
    assert compose(inverse(t), b) == c
    assert comm(a, c) == (1, 0)
    assert compose(compose(a, t), inverse(a)) == (1, 2)
    assert compose(compose(c, t), inverse(c)) == (1, 3)
    assert comm(t, compose(compose(a, t), inverse(a))) == (1, 0)
    counts = dict(words=0, cylinder_samples=0, pruning_checks=0, positive_cycle_words=0,
                  expanding_family_checks=0, group_identities=6)
    for m in range(1, 7):
        for w in product(range(1, 5), repeat=m):
            ps = prefixes(w)
            _, S, C = ps[-1]
            modulus = 2**(S + 1)
            r = ((2**S - C) * pow(3**m, -1, modulus)) % modulus
            assert r % 2 == 1
            bounds = [F(cj, 2**sj - 3**j) for j, sj, cj in ps if 2**sj > 3**j]
            bound = min(bounds) if bounds else None
            for n in (r, r + modulus, r + 2 * modulus):
                z = n
                for s in w:
                    z, actual = odd_step(z)
                    assert actual == s
                assert z == (3**m * n + C) // 2**S
                counts['cylinder_samples'] += 1
            for n in range(1, 256, 2):
                z, valid, no_descent = n, True, True
                for s in w:
                    z, actual = odd_step(z)
                    if actual != s:
                        valid = False
                        break
                    no_descent = no_descent and z >= n
                predicted_valid = n % modulus == r
                assert valid == predicted_valid
                predicted_survival = predicted_valid and (bound is None or n <= bound)
                assert (valid and no_descent) == predicted_survival
                counts['pruning_checks'] += 1
            D = 2**S - 3**m
            if D > 0 and C % D == 0:
                n = C // D
                z = n
                for s in w:
                    z, actual = odd_step(z)
                    assert actual == s
                assert z == n
                counts['positive_cycle_words'] += 1
            counts['words'] += 1
    for r in range(1, 101):
        n = 2**(r + 1) - 1
        z = n
        for j in range(1, r + 1):
            old = z
            z, s = odd_step(z)
            assert s == 1 and z > old
            assert z == 3**j * 2**(r + 1 - j) - 1
            counts['expanding_family_checks'] += 1
    result = {'status': 'passed', 'arithmetic': 'integers and Fraction only', **counts}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
