"""Search binary local-pattern ranks for the partial A/B map. Exploratory LP."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
import numpy as np
import sympy as sp
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, vstack, csr_matrix


def features(n,k):
    s='^'*(k-1)+bin(n)[2:]+'$'*(k-1)
    return Counter(s[j:j+k] for j in range(len(s)-k+1))


def transitions(limit):
    for n in range(3,limit,4):
        yield n,(3*n+1)//2,'A'
    for n in range(9,limit,32):
        yield n,(27*n+29)//16,'B'


def main():
    pairs=list(transitions(16384))
    results=[]
    for k in range(1,9):
        rows=[]; keys=set()
        for n,m,label in pairs:
            d=features(n,k)
            d.subtract(features(m,k))
            d={key:value for key,value in d.items() if value}
            keys.update(d)
            rows.append(d)
        keys=sorted(keys); index={key:i for i,key in enumerate(keys)}
        ri=[]; ci=[]; values=[]
        for r,d in enumerate(rows):
            for key,v in d.items():
                ri.append(r); ci.append(index[key]); values.append(v)
        matrix=coo_matrix((values,(ri,ci)),shape=(len(rows),len(keys))).tocsr()
        # Interior counts are nonnegative; boundary counts have uniformly
        # bounded multiplicity, so free boundary weights preserve a lower bound.
        bounds=[(None,None) if '^' in key or '$' in key else (0,None) for key in keys]
        fit=linprog(np.zeros(len(keys)),A_ub=-matrix,b_ub=-np.ones(len(rows)),
                    bounds=bounds,method='highs')
        row=dict(window=k,features=len(keys),transitions=len(rows),
                 status=int(fit.status),message=fit.message)
        if fit.success:
            row['weights']={key:float(value) for key,value in zip(keys,fit.x) if abs(value)>1e-8}
        elif fit.status == 2:
            interior=[j for j,key in enumerate(keys) if '^' not in key and '$' not in key]
            boundary=[j for j,key in enumerate(keys) if '^' in key or '$' in key]
            equality=vstack([matrix[:,boundary].T,csr_matrix(np.ones((1,len(rows))))])
            dual=linprog(np.zeros(len(rows)),A_ub=matrix[:,interior].T,
                         b_ub=np.zeros(len(interior)),A_eq=equality,
                         b_eq=np.r_[np.zeros(len(boundary)),1],
                         bounds=(0,None),method='highs')
            assert dual.success
            witness=[(i,Fraction(float(x)).limit_denominator(10**6))
                     for i,x in enumerate(dual.x) if x>1e-9]
            aggregate={key:sum((weight*rows[i].get(key,0) for i,weight in witness),Fraction(0))
                       for key in keys}
            if not all(aggregate[key] == 0 if '^' in key or '$' in key
                       else aggregate[key]<=0 for key in keys):
                support=[i for i,x in enumerate(dual.x) if x>1e-9]
                raw=np.asarray(matrix.T @ dual.x).ravel()
                active=boundary+[j for j in interior if abs(raw[j])<1e-7]
                equations=matrix[support,:][:,active].T.toarray().astype(int).tolist()
                equations.append([1]*len(support))
                solution,params,free=sp.Matrix(equations).gauss_jordan_solve(
                    sp.Matrix([0]*(len(equations)-1)+[1]),freevar=True)
                substitution={param:sp.Rational(Fraction(float(dual.x[support[j]])).limit_denominator(10**6))
                              for param,j in zip(params,free)}
                solution=solution.subs(substitution)
                witness=[(i,Fraction(int(x.p),int(x.q))) for i,x in zip(support,solution) if x]
                aggregate={key:sum((weight*rows[i].get(key,0) for i,weight in witness),Fraction(0))
                           for key in keys}
            assert witness and all(weight>0 for _,weight in witness)
            assert all(aggregate[key] == 0 if '^' in key or '$' in key
                       else aggregate[key]<=0 for key in keys)
            row['exact_certificate']=[dict(start=pairs[i][0],end=pairs[i][1],
                                           block=pairs[i][2],numerator=weight.numerator,
                                           denominator=weight.denominator) for i,weight in witness]
            row['certificate_support']=len(witness)
            row['exact_certificate_verified']=True
        results.append(row)
        print(json.dumps({key:value for key,value in row.items()
                          if key not in ('weights','exact_certificate')}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__':main()
