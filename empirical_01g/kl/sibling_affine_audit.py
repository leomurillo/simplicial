"""Exact finite checks for sibling affine transitions; no asymptotic claims."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from syracuse_tao_bridge_exact import lift


def step(h, a, b):
    u, v = h
    slope = u*F(2)**(a-b)
    offset = (slope+2**a*v-1)/3
    if offset.denominator % 3 == 0:
        return None
    return slope, offset


def val3(x):
    if not x:
        return 1000000
    v, num, den = 0, abs(x.numerator), x.denominator
    while num % 3 == 0:
        num //= 3; v += 1
    while den % 3 == 0:
        den //= 3; v -= 1
    return v


def barrier(h):
    return 1+max(0, min(val3(h[0]-1), val3(h[1])))


def main():
    mu = [F(1)]
    laws = [mu]
    for _ in range(6):
        mu = lift(mu, F(1,2)); laws.append(mu)
    # Full geometric sum is finite after grouping by the odometer period.
    reports = []
    for n in range(1, 7):
        m = 3**(n-1)
        old, new = laws[n-1], laws[n]
        f_old = F(2,3)*m*sum(x*x for x in old)
        f_new = F(2,3)*3*m*sum(x*x for x in new)
        sibling_sum = F(0)
        for k in range(1,m+1):
            u, v = pow(4,k,m), ((4**k-1)//3) % m
            corr = sum(old[y]*old[(u*y+v) % m] for y in range(m))
            sibling_sum += F(1,4**k)*F(2,3)*m*corr
        sibling_sum /= 1-F(1,4**m)
        assert f_new-f_old == 2*sibling_sum
        reports.append(dict(n=n, collision_factor=str(f_new), sibling_factor=str(sibling_sum)))
    # The odd numerator of g_word(0) uniquely determines the outer exponents.
    words_checked = 0
    for length in range(1,6):
        numerators = {}
        for prefix in product(range(1,5), repeat=length-1):
            c = F(1)
            for a in reversed(prefix):
                c = 1+F(3,2**a)*c
            assert c.numerator not in numerators
            numerators[c.numerator] = prefix
            words_checked += 1
    # A -> 2x+1 in one paired step; 2x+1 has total outgoing weight 4/3.
    A = (F(4),F(1))
    h = (F(2),F(1))
    assert step(A,1,2) == h
    assert step(h,1,1) == h
    partial = sum((F(3,2**(a+b))*barrier(t)
                   for a in range(1,9) for b in range(1,9)
                   if (t:=step(h,a,b)) is not None), F(0))
    assert partial > barrier(h)
    output = dict(status='Exact finite identities, not a transversality proof',
                  levels=reports, numerator_injectivity_words_checked=words_checked,
                  depth_only_barrier_counterexample=dict(state=['2','1'],
                      barrier_value=barrier(h), positive_partial_transfer=str(partial),
                      cutoff=8, exact_outgoing_weight='4/3', self_loop_weight='3/4'))
    Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(dict(collision_levels_checked=6, numerator_words_checked=words_checked,
                         depth_barrier_partial=str(partial), all_exact_checks_pass=True)))


if __name__ == '__main__':
    main()
