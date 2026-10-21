"""Exploratory float64 LPs, NOT interval or exact-arithmetic certificates.

Independent implementation; does not import scripts that run on import.
Writes only its own JSON. Run: python visibility_potential_probe.py --max-k 6
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def build(k):
    m = 3**k
    r = np.arange(m)
    q = ((2*r-1)//3) % (m//3)
    return r, (2*r) % m, np.stack([q+j*(m//3) for j in range(3)], axis=1)


def phi(k, gamma, c):
    r, dbl, lifts = build(k)
    out = 2**(-gamma)*c[dbl]
    out += np.where(r % 3 == 2, 1.5**gamma*c[lifts].min(axis=1), 0)
    return np.where(r % 3 != 0, out, 0)


def eigen(k, gamma):
    r, dbl, lifts = build(k)
    live, odd = r % 3 != 0, r % 3 == 2
    c = live.astype(float); c /= c.sum()
    for iteration in range(100000):
        nxt = np.where(live, 2**(-gamma)*c[dbl] + np.where(odd, 1.5**gamma*c[lifts].min(axis=1), 0), 0)
        lam = nxt.sum(); nxt /= lam
        if np.max(np.abs(nxt-c)) < 2e-14*np.max(nxt):
            return float(lam), nxt
        c = nxt
    raise RuntimeError('Eigen-iteration did not converge')


def critical(k):
    lo, hi = 0., 1.
    for _ in range(38):
        mid = (lo+hi)/2
        lam, _ = eigen(k, mid)
        if lam >= 1: lo = mid
        else: hi = mid
    gamma = (lo+hi)/2
    return gamma, eigen(k, gamma)[1]


def potential_lp(k, gamma, c, mode):
    """v_i=c_i z_group(i), 0<=z<=1; maximize epsilon with Phi(v)>=v+epsilon*c."""
    level = k+1
    r, dbl, lifts = build(level)
    live = r[r % 3 != 0]
    if mode == 'full': labels = live
    elif mode == 'old_digits': labels = live % (3**k)
    elif mode.startswith('top_low'):
        low = int(mode[-1])
        labels = (live % (3**low))*3 + live//(3**k)
    elif mode == 'ordering_chamber':
        # Include the actual order of the critical lower lift triple and the
        # selected new-digit position; distinguish the r=1 and r=2 rows.
        lower=3**k; triple_mod=lower//3; labels=[]
        for i in live:
            partner=int(i if i%3==2 else (2*i)%len(r))
            selected=((2*partner-1)//3)%lower
            base=selected%triple_mod
            order=np.argsort(c[[base+j*triple_mod for j in range(3)]],kind='stable')
            order_code=int(order[0]+3*order[1]+9*order[2])
            labels.append((int(i%3)*27+order_code)*3+selected//triple_mod)
        labels=np.array(labels)
    elif mode == 'depth':
        def depth(x):
            n, d = int(x)+1, 0
            while n % 3 == 0: n //= 3; d += 1
            return d
        labels = np.array([depth(x) for x in live])
    else: raise ValueError(mode)
    _, groups = np.unique(labels, return_inverse=True)
    group = np.full(len(r), -1); group[live] = groups
    nvar = int(groups.max())+1
    rows, cols, vals, row = [], [], [], 0
    for i in live:
        targets = lifts[i] if i % 3 == 2 else [-1]
        for t in targets:
            entries = [(group[i], 1.), (group[dbl[i]], -2**(-gamma)*c[dbl[i]]/c[i]), (nvar, 1.)]
            if t >= 0 and t % 3 != 0:
                entries.append((group[t], -1.5**gamma*c[t]/c[i]))
            for j, value in entries:
                rows.append(row); cols.append(j); vals.append(value)
            row += 1
    mat = coo_matrix((vals, (rows, cols)), shape=(row, nvar+1)).tocsr()
    obj = np.zeros(nvar+1); obj[-1] = -1
    sol = linprog(obj, A_ub=mat, b_ub=np.zeros(row), bounds=[(0,1)]*nvar+[(None,None)],
                  method='highs', options={'primal_feasibility_tolerance':1e-9, 'dual_feasibility_tolerance':1e-9})
    if not sol.success: raise RuntimeError(sol.message)
    v = np.zeros(len(r)); v[live] = c[live]*sol.x[groups]
    eps = float(sol.x[-1])
    residual = float(np.min((phi(level,gamma,v)[live]-v[live])/c[live]-eps))
    if mode == 'full':
        np.savez_compressed(Path(__file__).with_name(f'visibility_potential_k{k}.npz'),
                            c=c, v=v, gamma=gamma, epsilon=eps)
    return dict(mode=mode, variables=nvar, epsilon=eps, residual_min=residual,
                z_min=float(sol.x[:-1].min()), z_max=float(sol.x[:-1].max()))


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--max-k', type=int, default=6)
    args = parser.parse_args(); rows = []
    for k in range(2,args.max_k+1):
        gamma, ck = critical(k)
        c = ck[np.arange(3**(k+1)) % (3**k)]
        gain = phi(k+1,gamma,c)-c
        H = float(gain.sum()/c.sum()); exact_H = 2**(-gamma)+1.5**gamma/3-1
        G = eigen(k+1,gamma)[0]-1
        delta = 1-3*(1-2**(-gamma))/1.5**gamma
        results = [potential_lp(k,gamma,c,mode) for mode in ('old_digits','depth','top_low1','top_low2','ordering_chamber','full')]
        entry = dict(k=k,gamma=gamma,G=G,H=H,exact_H=exact_H,delta=delta,
                     eigen_residual=float(np.max(np.abs(phi(k,gamma,ck)-ck))),potentials=results)
        rows.append(entry)
        print(json.dumps(entry),flush=True)
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps({'status':'exploratory floating point, not rigorous certificates','levels':rows},indent=2))


if __name__ == '__main__': main()
