"""Exact finite-branch separation witnesses for block norm lower bounds.

Uses rational affine maps f_a(x)=(3x+1)/2^a and all a<=A.
No numerical norm evaluation or asymptotic inference is used.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json


def valuation3(nonzero):
    x=abs(nonzero); v=0
    assert x
    while x%3==0: x//=3; v+=1
    return v


def witness(m,A):
    maps={}
    for word in product(range(1,A+1),repeat=m):
        slope,intercept=F(1),F(0)
        for a in word:
            slope,intercept=3*slope/2**a,(3*intercept+1)/2**a
        maps[(slope,intercept)]=maps.get((slope,intercept),F(0))+F(1,2**sum(word))
    affine=list(maps)
    bad=set()
    for (p,q),(r,s) in combinations(affine,2):
        if p!=r:
            root=(s-q)/(p-r)
            if root.denominator==1 and root>0: bad.add(int(root))
    J=1
    while J%3==0 or J in bad: J+=1
    values=[p*J+q for p,q in affine]
    assert len(set(values))==len(values)
    max_v=-1
    for x,y in combinations(values,2):
        d=x-y
        assert d.denominator%3
        max_v=max(max_v,valuation3(d.numerator))
    n=max(2,max_v-m+2)
    while J>=3**(n-1): n+=1
    modulus=3**(n+m-1)
    residues=[(x.numerator*pow(x.denominator,-1,modulus))%modulus for x in values]
    assert len(set(residues))==len(values)
    mass=sum(maps.values(),F(0))
    assert mass==(1-F(1,2**A))**m
    lower=2*mass-1
    return dict(steps=m,max_branch_exponent=A,words=A**m,distinct_affine_maps=len(maps),
                seed_context=J,start_level=n,end_level=n+m,max_difference_v3=max_v,
                all_retained_outputs_distinct_mod_context=True,
                retained_mass=[mass.numerator,mass.denominator],
                rigorous_block_norm_lower_bound=[lower.numerator,lower.denominator],
                lower_bound_decimal=float(lower))


def main():
    rows=[]
    for m,A in [(1,6),(2,6),(3,6),(4,4)]:
        row=witness(m,A); rows.append(row); print(json.dumps(row),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'method':'exact Fraction arithmetic and modular inverses; applies at the recorded starting level and every higher one','witnesses':rows},indent=2))


if __name__=='__main__': main()
