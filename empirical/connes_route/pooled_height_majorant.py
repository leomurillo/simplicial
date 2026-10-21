"""Prime-independent pooled factorial majorants, exact rational feasibility."""
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

def floorsum(N,d):
    q,r=divmod(N,d)
    return d*q*(q-1)//2+q*(r+1)

out=[]
for X in (100,300,1000):
    for multiple in (1,3):
        K=min(X,multiple*math.isqrt(2*X))
        ns=range(2,2*X+1)
        A=np.array([[floorsum(2*X,k*n)-floorsum(X,k*n)
                    -floorsum(2*X,2*k*n)+floorsum(X,2*k*n)
                    for k in range(1,K+1)] for n in ns],dtype=np.int64)
        w=np.array([max(0,min(2*X,2*n-1)-max(X+1,n)+1) for n in ns],dtype=np.int64)
        costs=np.array([math.fsum(math.lgamma(x//k+1)-math.lgamma(x//(2*k)+1)
                                 for x in range(X+1,2*X+1)) for k in range(1,K+1)])
        # A bounded search avoids spurious unboundedness from rounded logarithms
        # in exact null directions. Feasibility is certified independently below.
        res=linprog(costs/(X*X),A_ub=-A,b_ub=-w,bounds=[(-100,100)]*K,method='highs')
        if not res.success: raise RuntimeError(res.message)
        c=[Fraction(float(v)).limit_denominator(100000) for v in res.x]
        repair=Fraction(0)
        for row,target in zip(A,w):
            value=sum((int(a)*v for a,v in zip(row,c)),Fraction(0))
            repair=max(repair,(int(target)-value)/int(row[0]))
        c[0]+=repair
        Q=math.lcm(*(v.denominator for v in c)); v=[int(Q*a) for a in c]
        slack=[sum(int(a)*b for a,b in zip(row,v))-Q*int(t) for row,t in zip(A,w)]
        assert min(slack)>=0
        height=math.fsum(float(a)*b for a,b in zip(c,costs))
        main=X*(3*X+1)/4
        result={'X':X,'K':K,'coefficients':[str(a) for a in c],
                'multiplicity_digits':len(str(Q)), 'rational_repair':str(repair),
                'min_exact_slack':min(slack),'normalized_height_approx':height,
                'block_main':main,'excess_approx':height-main,
                'excess_over_X_3_2':(height-main)/(X**1.5),
                'exact_feasibility':True}
        out.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='coefficients'}),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
