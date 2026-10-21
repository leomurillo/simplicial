"""Exact first-contraction boundary bound, counterexamples, and finite audit.

No floating-point logarithms, no external packages, no claim about unbounded time.
"""
import json
from pathlib import Path


def step(n):
    z = 3 * n + 1
    s = (z & -z).bit_length() - 1
    return z >> s, s


def word_data(n, word):
    A, C, S, z = 1, 0, 0, n
    path = [n]
    for s in word:
        z, actual = step(z)
        assert actual == s
        C, S, A = 3 * C + (1 << S), S + s, 3 * A
        path.append(z)
    M = 1 << (S + 1)
    r = ((1 << S) - C) * pow(A, -1, M) % M
    assert r == n and A * n + C == (1 << S) * z
    return dict(n=n, word=word, path=path, m=len(word), S=S, A=A,
                C=C, D=(1 << S)-A, residue=r, q=(n-z)//2)


def main():
    horizon = 1000
    A, B, maximum, maximizer = 1, 0, 0, None
    records = []
    # B_m=sum_{j<m} 3^(m-1-j) 2^floor(log_2(3^j)).
    for m in range(1, horizon + 1):
        B = 3 * B + (1 << (A.bit_length() - 1))
        A *= 3
        S_min = A.bit_length()
        D_min = (1 << S_min) - A
        limit = B // D_min
        if limit > maximum:
            maximum = limit
            maximizer = dict(m=m, S_min=S_min, B=B, D_min=D_min, limit=limit)
            records.append(dict(m=m, S_min=S_min, limit=limit))
    tested = crossed = unresolved = max_crossing = 0
    for n in range(3, maximum + 1, 2):
        tested += 1
        z, S, A = n, 0, 1
        for m in range(1, horizon + 1):
            z, s = step(z)
            S += s
            A *= 3
            if (1 << S) > A:
                assert z < n, (n, m, S, z)
                crossed += 1
                max_crossing = max(max_crossing, m)
                break
        else:
            unresolved += 1
    examples = [
        word_data(165, [4,1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3]),
        word_data(231, [1,1,2,1,1,2,6,1,1,1,1,2,2,1,2,1,1]),
    ]
    assert all(e['D'] > 0 and e['q'] == -1 for e in examples)
    anchor = word_data(231, examples[1]['word'][:-1])
    assert anchor['D'] > 0 and anchor['q'] == 38
    result = dict(status='passed', horizon=horizon, seed_bound=maximum,
                  records=records, maximizer=maximizer, tested_odd_seeds=tested,
                  first_crossings_with_descent=crossed, no_crossing_by_horizon=unresolved,
                  largest_observed_first_crossing=max_crossing,
                  contracting_word_counterexamples=examples, append_one_anchor=anchor,
                  scope='Every first coefficient crossing by 1000 odd steps descends for all positive odd starts >1. No assertion that a crossing occurs for every start.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('maximizer','contracting_word_counterexamples','append_one_anchor')}, indent=2))


if __name__ == '__main__':
    main()
