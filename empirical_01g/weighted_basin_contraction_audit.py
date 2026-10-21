"""Exact tests of the attempted weight contraction; no universal decay claim."""
from fractions import Fraction as F
from pathlib import Path
import json
from peak_bottleneck_audit import predecessors


def w(n):
    return F(1,n*(n+1))


def main():
    # K excludes the terminal state 1.
    ratios=[]
    for m in (5,10,16,100,1000000):
        incoming=w(2*m)
        if m%6==4 and m>4:
            incoming+=w((m-1)//3)
        expected=F(m+1,2*(2*m+1))
        if m%6==4 and m>4:
            expected+=F(9*m*(m+1),(m-1)*(m+2))
        assert incoming/w(m)==expected
        ratios.append(dict(m=m,incoming_weight_ratio=str(expected),decimal=float(expected)))
    paths=0
    for r in range(1,31):
        for L in (1,7,10**9):
            n=2**(r+1)*L-1;m=2*3**r*L-1;z=n
            for _ in range(r):
                assert z%4==3
                z=(3*z+1)//2
            assert z==m
            assert w(n)/w(m)>F(3,2)**(2*r)
            paths+=1
    # Rigorous finite intervals: sum floors with denominator 2^100.
    intervals=[];den=2**100
    for H in (9231,9232,250504,1000000):
        B=predecessors(1,H)
        low=den//(H+1);terms=1
        for n in range(1,H+1):
            if n not in B:
                low+=den//(n*(n+1));terms+=1
        high=low+terms
        intervals.append(dict(H=H,basin_size=len(B),lower_numerator=low,
                              upper_numerator=high,denominator=den,
                              display_lower=low/den,display_upper=high/den))
    result=dict(status='passed',one_step_ratios=ratios,
                expanding_inverse_path_checks=paths,finite_weight_intervals=intervals,
                conclusion='The weight is not pointwise contracting. Finite W_H values do not prove zero limit.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
