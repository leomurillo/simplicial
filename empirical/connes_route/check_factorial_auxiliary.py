"""Exact valuation checks for the truncated Mobius factorial auxiliary."""
import json
import math
from fractions import Fraction
from pathlib import Path
import sympy as sp

LIMIT = 80
mu = [0] + [int(sp.mobius(k)) for k in range(1, LIMIT + 1)]
primes = list(sp.primerange(2, LIMIT + 1))
M = [0]
for value in mu[1:]:
    M.append(M[-1] + value)

def vf(n, p):
    value = 0
    while n:
        n //= p
        value += n
    return value

def target(x, p):
    count, power = 0, p
    while power <= x:
        count += power > x // 2
        power *= p
    return count

def valuation(x, K, p):
    return sum(mu[k] * (vf(x // k, p) - vf(x // (2*k), p))
               for k in range(1, K + 1))

first = None
checks = 0
for x in range(2, LIMIT + 1):
    for K in range(1, x + 1):
        for p in primes:
            if p > x:
                break
            v = valuation(x, K, p)
            t = target(x, p)
            # Group the omitted Mobius terms by floor(x/k).
            tail = 0
            for j in range(1, x // (K + 1) + 1):
                lo = max(K, x // (j + 1))
                hi = x // j
                if hi > lo:
                    tail += (M[hi] - M[lo]) * (vf(j, p) - vf(j // 2, p))
            assert v + tail == t
            assert v + max(0, t-v) == t + max(0, v-t)
            if K == x:
                assert v == t
            if v < 0 and first is None:
                first = {"x": x, "K": K, "prime": p, "valuation": v}
            checks += 1

x, K = 18, 5
ratio = Fraction(1)
for k in range(1, K + 1):
    ratio *= Fraction(math.factorial(x // k), math.factorial(x // (2*k))) ** mu[k]
assert ratio == Fraction(4862, 3)
result = {"range": [2, LIMIT], "exact_prime_valuation_checks": checks,
          "first_negative_valuation": first,
          "counterexample": str(ratio),
          "grouped_tail_identity": "passed",
          "minimal_repair_identity": "passed",
          "full_complexity_identity": "passed"}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
