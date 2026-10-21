"""Exact checks for the expanding-block attack; no conjecture verification claim."""
from itertools import product
import json
from pathlib import Path

def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1

def data(word):
    s = c = 0
    for a in word:
        c = 3*c + 2**s
        s += a
    return s, c, 3**len(word) - 2**s

def repeats(n, word):
    k = 0
    while True:
        x = n
        for a in word:
            t = 3*x + 1
            if v2(t) != a:
                return k
            x = t >> a
        n = x
        k += 1

checked = 0
words = 0
for length in range(1, 6):
    for word in product(range(1, 5), repeat=length):
        s, c, d = data(word)
        if d <= 0:
            continue
        words += 1
        for n in range(1, 2000, 2):
            predicted = (v2(d*n+c)-1)//s
            actual = repeats(n, word)
            assert predicted == actual, (word, n, predicted, actual)
            checked += 1

reset_examples = []
for m in range(3, 202, 2):
    n = (2**(m+2)-5)//3
    x = 3*n+1
    assert v2(n+1) == 1 and v2(x) == 2
    y = x//4
    assert y == 2**m-1 and v2(y+1) == m
    assert repeats(y, (1,)) == m-1
    z = y
    for _ in range(m-1):
        z = (3*z+1)//2
    assert z == 2*3**(m-1)-1 and z > n
    if m <= 11:
        reset_examples.append({'M':m,'start':n,'after_halving_block':y,'after_expanding_run':z})

return_checks = 0
for x in range(1, 40000, 4):
    a = v2(3*x+1)
    y = (3*x+1) >> a
    b = v2(y+1)
    numerator = 3**(b-1)*(3*x+1+2**a)
    assert numerator % 2**(a+b-1) == 0
    predicted = numerator//2**(a+b-1)-1
    actual = y
    for _ in range(b-1):
        assert v2(actual+1) > 1 and v2(3*actual+1) == 1
        actual = (3*actual+1)//2
    assert actual == predicted and v2(actual+1) == 1
    return_checks += 1

# Odd cores and the next return (Argon, Section 12.9): R(x)+1 = 2*3^(b-1)*u,
# a' = 1 + v2(3^b u - 1), 2^(a'-1+b') u' = 3^b u + 2^(a'-1) - 1; cores coprime across a' = 2.
from math import gcd
import random
def ret(x):
    a = v2(3*x+1); y = (3*x+1) >> a; b = v2(y+1); u = (y+1) >> b
    z = y
    for _ in range(b-1):
        z = (3*z+1)//2
    return a, b, u, z
rng = random.Random(20261017)
core_checks = 0
for x in list(range(1, 40000, 4)) + [4*rng.randrange(1, 10**30)+1 for _ in range(2000)]:
    a, b, u, x1 = ret(x)
    a1, b1, u1, _ = ret(x1)
    assert x1 % 4 == 1 and x1+1 == 2*3**(b-1)*u and 3*x1+1 == 2*(3**b*u-1)
    assert a1 == 1+v2(3**b*u-1) and 2**(a1-1+b1)*u1 == 3**b*u+2**(a1-1)-1
    if a1 == 2:
        assert gcd(u, u1) == 1
    core_checks += 1
for m in range(3, 202, 2):
    assert ret(ret((2**(m+2)-5)//3)[3])[:2] == (2, 1)

# The bridge identity (Argon): 3 n0 + 2^a1 n2 = (2^a0 + 3) n1 and gcd(n0, n2) | 2^a0 + 3.
bridge_checks = 0
for n0 in range(1, 200000, 2):
    a0 = v2(3*n0+1); n1 = (3*n0+1) >> a0; a1 = v2(3*n1+1); n2 = (3*n1+1) >> a1
    assert 3*n0 + 2**a1*n2 == (2**a0+3)*n1 and (2**a0+3) % gcd(n0, n2) == 0
    bridge_checks += 1

# One-return cycles: (2^(a-1+b) - 3^b) u = 2^(a-1) - 1 has the single positive odd solution
# (a, b, u) = (2, 1, 1) for b <= 60, a <= 120 (a finite check; the full statement is Steiner's theorem).
one_return = []
for b in range(1, 61):
    for a in range(2, 121):
        den = 2**(a-1+b) - 3**b; num = 2**(a-1) - 1
        if den > 0 and num % den == 0 and (num//den) % 2 == 1:
            one_return.append((a, b, num//den))
assert one_return == [(2, 1, 1)]

result = {'status':'All exact checks passed', 'expanding_words':words,
          'word_start_checks':checked, 'reset_family_checks':100,
          'return_map_checks':return_checks,
          'odd_core_checks':core_checks, 'bridge_checks':bridge_checks,
          'one_return_solutions':one_return,
          'reset_examples':reset_examples,
          'scope':'Finite identity checks supporting the written proofs; not a proof of Collatz.'}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
