"""Exact certificates for signed periodic pooled factorial majorants.

No optimizer or prime data is used here. Decimal costs are diagnostics;
the coefficient lists, balance, and full-period feasibility are exact.
"""
import json
import math
from fractions import Fraction
from pathlib import Path

RULES = {
    2: {1: 1, 2: -2},
    12: {1: 1, 2: -2, 3: -1, 4: 1, 6: 1, 12: -1},
    2520: {1:1,2:-2,3:-1,4:1,5:-1,6:2,7:-1,10:2,12:-2,
           14:1,15:1,18:-1,20:-1,21:1,24:1,30:-3,35:1,36:2,
           42:-2,60:2,70:-2,72:-1,84:1,90:2,105:-2,120:-1,
           126:1,140:2,168:-1,180:-3,210:4,252:-3,280:-1,
           315:1,360:1,420:-1,504:1,630:-2,1260:-1,2520:-3},
}

def floor_sum(N, d):
    q, r = divmod(N, d)
    return d*q*(q-1)//2 + q*(r+1)

def pooled(X, k, n):
    return (floor_sum(2*X,k*n)-floor_sum(X,k*n)
            -floor_sum(2*X,2*k*n)+floor_sum(X,2*k*n))

def weight(X, n):
    return max(0,min(2*X,2*n-1)-max(X+1,n)+1)

def coefficients(a, X):
    c = {}
    for d, v in a.items():
        k = d
        while k <= X:
            c[k] = c.get(k,0)+v
            k *= 2
    return {k:v for k,v in c.items() if v}

def main():
    rows=[]
    for L,a in RULES.items():
        assert all(L%d==0 for d in a)
        assert sum((Fraction(v,d) for d,v in a.items()),Fraction())==0
        values=[sum(v*(n//d) for d,v in a.items()) for n in range(L)]
        assert min(values)>=0 and values[1]==1
        C=-math.fsum(v*math.log(d)/d for d,v in a.items())
        S=sum(abs(v) for v in a.values())
        checks=[]
        for X in (2,7,37,100,1000):
            c=coefficients(a,X)
            slacks=[sum(v*pooled(X,k,n) for k,v in c.items())-weight(X,n)
                    for n in range(2,2*X+1)]
            assert min(slacks)>=0
            direct=math.fsum(v*math.lgamma(x//d+1)
                             for x in range(X+1,2*X+1) for d,v in a.items())
            converted=math.fsum(v*(math.lgamma(x//k+1)-math.lgamma(x//(2*k)+1))
                                for x in range(X+1,2*X+1) for k,v in c.items())
            assert abs(direct-converted)<1e-7*max(1,abs(direct))
            A=X*(3*X+1)/4
            assert direct <= 2*C*A+S*X*(1+2*math.log(4*X))+1e-7
            checks.append({'X':X,'min_exact_slack':min(slacks),
                           'support_size':len(c),'height_approx':direct})
        row={'period':L,'a':a,'coefficient_l1':S,'C_approx':C,
             'main_multiplier_approx':2*C,'min_period_value':min(values),
             'max_period_value':max(values),'checks':checks}
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('a','checks')}))
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':
    main()
