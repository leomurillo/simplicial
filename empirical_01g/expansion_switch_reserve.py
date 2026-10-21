"""Exact checks of block-switch reserves; no universal repayment claim."""
from itertools import product
from pathlib import Path
import json


def v2(n):
    n = abs(n)
    assert n
    return (n & -n).bit_length()-1


def data(word):
    S = C = 0
    for a in word:
        C = 3*C + 2**S
        S += a
    return S, C, 3**len(word)-2**S


def apply_word(n, word):
    for a in word:
        assert v2(3*n+1) == a
        n = (3*n+1)//2**a
    return n


def main():
    words = []
    for length in range(1, 6):
        for word in product(range(1, 5), repeat=length):
            S, C, D = data(word)
            if D > 0:
                words.append((word, S, C, D))
    checks = 0
    for word, S, C, D in words:
        for n in range(1, 500, 2):
            k = (v2(D*n+C)-1)//S
            if not k:
                continue
            y = n
            for _ in range(k):
                y = apply_word(y, word)
            remaining = v2(D*y+C)
            assert 1 <= remaining <= S
            for other, T, E, F in words:
                delta = D*E-F*C
                new = v2(F*y+E)
                if not delta:
                    assert new == remaining
                else:
                    separation = v2(delta)
                    if remaining != separation:
                        assert new == min(remaining, separation)
                    else:
                        assert new >= separation+1
                    if new > separation:
                        assert remaining == separation
                checks += 1
    examples = []
    for K in range(1, 101):
        exponent = 4*K+2
        L = pow(pow(2, exponent, 11), -1, 11)
        if not L%2:
            L += 11
        n = (2**exponent*L-23)//11
        assert 11*n+23 == 2**exponent*L
        assert v2(n+1) == 2
        y = apply_word(n, (1,))
        assert y > n
        assert v2(y+1) == 1
        assert v2(11*y+29) == 4*K+1
        for j in range(K):
            z = apply_word(y, (2,1,1))
            assert z > y
            y = z
        assert y == (2*3**(3*K+1)*L-29)//11
        assert v2(11*y+29) == 1
        if K <= 6:
            examples.append(dict(K=K,L=L,start=n,endpoint=y))
    result = dict(status='Exact checks, not a proof of Collatz',
                  expanding_words=len(words),switch_checks=checks,
                  explicit_family_checks=100,examples=examples)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
