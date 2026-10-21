"""Cycle-frequency slope certificates for sampled policies, not all active policies."""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from visibility_potential_probe import build, eigen


def compute(k,gamma):
    rho,x=eigen(k,gamma)
    r,dbl,lifts=build(k)
    live=r[r%3!=0]; index=np.full(len(r),-1); index[live]=np.arange(len(live))
    choice=lifts[np.arange(len(r)),np.argmin(x[lifts],axis=1)]
    edges=[]
    for s in live:
        edges.append((index[s],index[dbl[s]],0))
        if s%3==2 and choice[s]%3:
            edges.append((index[s],index[choice[s]],1))
    rr=[]; cc=[]; vv=[]; bound=[]; n=len(live)
    for row,(s,t,odd) in enumerate(edges):
        rr.extend([row,row,row]); cc.extend([s,t,n]); vv.extend([-1.,1.,-1.]); bound.append(-odd)
    mat=coo_matrix((vv,(rr,cc)),shape=(len(edges),n+1)).tocsr()
    objective=np.zeros(n+1); objective[-1]=1
    fit=linprog(objective,A_ub=mat,b_ub=bound,bounds=[(0,0)]+[(None,None)]*(n-1)+[(0,1)],method='highs')
    assert fit.success,fit.message
    potentials=[F(float(v)) for v in fit.x[:-1]]
    upper=max(F(odd)+potentials[t]-potentials[s] for s,t,odd in edges)
    # Round up to an explicitly verified rational edgewise bound.
    scaled=upper*10**9
    upper=F(-(-scaled.numerator//scaled.denominator),10**9)
    assert all(F(o)+potentials[t]-potentials[s]<=upper for s,t,o in edges)
    integer_potential=[(2*v).numerator//(2*v).denominator for v in potentials]
    half_cycle_certificate=all(2*o+integer_potential[t]-integer_potential[s]<=1 for s,t,o in edges)
    np.savez_compressed(Path(__file__).with_name(f'policy_cycle_k{k}_g{gamma:.1f}.npz'),
                        live=live,chosen=choice[live],height=np.array(integer_potential,dtype=np.int64))
    return dict(k=k,gamma=gamma,rho_estimate=rho,edge_count=len(edges),
                max_cycle_odd_frequency_estimate=float(fit.x[-1]),
                odd_frequency_upper_exact=str(upper),
                log_spectral_derivative_upper_display=float(-np.log(2)+float(upper)*np.log(3)),
                exact_edge_checks_pass=True,
                integer_half_cycle_certificate=half_cycle_certificate,
                limitation='Graph selected numerically; exact check certifies this graph, not its optimality or stability in gamma.')


def main():
    rows=[]
    for k in range(2,10):
        for gamma in (0.8,0.9,1.):
            entry=compute(k,gamma); rows.append(entry); print(json.dumps(entry),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(results=rows),indent=2))


if __name__=='__main__':main()
