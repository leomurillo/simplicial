"""Discover policy-sensitive residual barriers; float discovery, separate exact audit."""
from pathlib import Path
import json
import numpy as np
from scipy.sparse import coo_matrix, eye, hstack, vstack, csr_matrix
from scipy.optimize import linprog
from policy_concentration_parameter_probe import law
from visibility_potential_probe import build, eigen, phi


def problem(k):
    mu = law(k)
    rho, x = eigen(k, 1.)
    residues, double, lifts = build(k)
    live = residues[residues % 3 != 0]
    index = np.full(len(mu), -1); index[live] = np.arange(len(live))
    b = float(max(phi(k,1.,x)[live]/x[live])+1e-10)
    e = (mu-phi(k,1.,mu))[live]/mu[live]
    return mu,x,rho,b,residues,double,lifts,live,index,e


def solve(k, mode, cap=10., endpoint_only=False):
    mu,x,rho,b,residues,double,lifts,live,index,e = problem(k)
    if endpoint_only: b=1.
    if mode == 'full':
        basis = eye(len(live),format='csr')
    else:
        vectors = [mu[live], x[live]]
        if mode in ('sibling','combined','ladder_combined'):
            modulus = len(mu)
            for power in (-9,-4,-3,-2,-1,1,2,3,4,9):
                # A has period 3^k, so negative powers can be evaluated modulo that period.
                exponent = power % modulus
                multiplier = pow(4, exponent, 3*modulus)
                offset = ((multiplier-1)//3) % modulus
                image = (multiplier*live+offset) % modulus
                vectors.append(mu[image])
        if mode in ('doubling','combined','ladder_combined'):
            for power in range(-6,7):
                if power:
                    vectors.append(mu[(pow(2,power,len(mu))*live) % len(mu)])
        if mode in ('ladder','ladder_combined'):
            old=np.load(Path(__file__).with_name(f'policy_residual_barrier_k{k-1}.npz'))
            low=live % len(old['mu'])
            top=live // len(old['mu'])
            density=old['h'][low]/old['mu'][low]
            vectors.extend([old['h'][low]/3,mu[live]*density,
                            mu[live]*density*(top-1),
                            mu[live]*density*np.array([1,-2,1])[top]])
        arr = np.stack(vectors,axis=1)/mu[live,None]
        arr /= np.maximum(np.max(abs(arr),axis=0),1e-300)
        basis=csr_matrix(arr)
    rows=[]; cols=[]; values=[]; costs=[]; row=0
    for j,r in enumerate(live):
        for t in (lifts[r] if r%3 == 2 else [-1]):
            rows.extend([row,row]); cols.extend([j,index[double[r]]])
            values.extend([b,-.5*mu[double[r]]/mu[r]])
            if t>=0 and t%3:
                rows.append(row); cols.append(index[t]); values.append(-1.5*mu[t]/mu[r])
            costs.append(e[j]); row+=1
    operator=coo_matrix((values,(rows,cols)),shape=(row,len(live))).tocsr()
    inequalities=hstack([operator@basis,-np.ones((row,1))],format='csr')
    if mode=='full':
        bounds=[(0,cap)]*len(live)+[(0,None)]
        rhs=-np.array(costs)
    else:
        inequalities=vstack([inequalities,
            hstack([basis,csr_matrix((len(live),1))]),
            hstack([-basis,csr_matrix((len(live),1))])],format='csr')
        rhs=np.r_[-np.array(costs),np.full(len(live),cap),np.zeros(len(live))]
        bounds=[(None,None)]*basis.shape[1]+[(0,None)]
    objective=np.zeros(basis.shape[1]+1); objective[-1]=1
    result=linprog(objective,A_ub=inequalities,b_ub=rhs,bounds=bounds,method='highs',
                   options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    if not result.success: raise RuntimeError(result.message)
    z=np.asarray(basis@result.x[:-1]).ravel()
    h=np.zeros(len(mu)); h[live]=mu[live]*np.maximum(z,0)
    epsilon=float(max((mu-phi(k,1.,mu)-phi(k,1.,h)+b*h)[live]/mu[live]))
    entry=dict(k=k,mode=mode,cap=cap,spectral_upper=b,rho_estimate=rho,
               endpoint_only=endpoint_only,variables=basis.shape[1],epsilon=epsilon,
               epsilon_lp=float(result.x[-1]),max_h_over_mu=float(max(z)),
               baseline=float(max(e)),spectral_gap_estimate=1-rho)
    if mode=='full' and not endpoint_only and cap==10.:
        np.savez_compressed(Path(__file__).with_name(f'policy_residual_barrier_k{k}.npz'),
                            h=h,x=x,mu=mu,epsilon=epsilon,b=b)
    return entry


def main():
    results=[]
    for k in range(2,8):
        for mode in ('sibling','doubling','combined','full'):
            entry=solve(k,mode)
            results.append(entry); print(json.dumps(entry),flush=True)
        entry=solve(k,'full',endpoint_only=True)
        results.append(entry); print(json.dumps(entry),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(
        dict(status='Float discovery, not exact certification',results=results),indent=2))


if __name__=='__main__': main()
