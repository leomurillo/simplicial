"""Exact realization of finite A/B schedules, not an infinite-orbit proof."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

BLOCKS = {'A': (1,), 'B': (2, 1, 1)}


def realize(schedule):
    word = tuple(a for block in schedule for a in BLOCKS[block])
    S = C = 0
    for a in word:
        C = 3*C + 2**S
        S += a
    modulus = 2**(S+1)
    start = ((2**S-C)*pow(3**len(word), -1, modulus)) % modulus
    assert start > 0 and start%2
    n = start
    odd_path = [n]
    for a in word:
        numerator = 3*n+1
        assert (numerator & -numerator).bit_length()-1 == a
        n = numerator//2**a
        odd_path.append(n)
        if schedule[0] == 'A':
            assert n > start
    assert n == (3**len(word)*start+C)//2**S
    return dict(schedule=schedule,start=start,endpoint=n,
                odd_steps=len(word),halvings=S,modulus=modulus,odd_path=odd_path)


def main():
    count = steps = 0
    for length in range(1, 13):
        mass = Fraction(0)
        for tail in product('AB', repeat=length-1):
            schedule = 'A'+''.join(tail)
            row = realize(schedule)
            count += 1
            steps += row['odd_steps']
            mass += Fraction(1,2**row['halvings'])
        assert mass == Fraction(1,2)*Fraction(9,16)**(length-1)
    examples = [realize(s) for s in ('AB','ABB','ABAB','ABABAB','AABBAB')]
    result = dict(status='Finite constructions only; infinite positive survival unresolved',
                  schedules_checked=count,individual_odd_steps_checked=steps,
                  exact_mass_levels_checked=12,examples=examples)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
