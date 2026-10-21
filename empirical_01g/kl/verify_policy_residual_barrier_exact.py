"""Verify saved residual barriers using fractions only for every assertion."""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np
from syracuse_tao_bridge_exact import lift


def choices(v,r):
    m=len(v)
    if r%3 != 2:
        return [v[2*r % m]/2]
    base=((2*r-1)//3) % (m//3)
    return [v[2*r % m]/2+F(3,2)*v[base+j*(m//3)] for j in range(3)]


def main():
    folder=Path(__file__).parent
    mu=[F(1)]
    reports=[]; total=0
    for k in range(1,8):
        mu=lift(mu,F(1,2))
        if k<2: continue
        data=np.load(folder/f'policy_residual_barrier_k{k}.npz')
        x=[F(float(t)) for t in data['x']]
        h=[F(float(t)) for t in data['h']]
        live=[r for r in range(len(mu)) if r%3]
        assert all(h[r]>=0 and x[r]>0 for r in live)
        ratios=[min(choices(x,r))/x[r] for r in live]
        a=min(ratios)
        b=max(max(ratios),F(float(data['b'])))
        assert 0<a<=b<1
        d={r:mu[r]-min(choices(mu,r)) for r in live}
        assert all(t>=0 for t in d.values())
        raw=max((d[r]-min(choices(h,r))+b*h[r])/mu[r] for r in live)
        scaled=raw*10**9
        epsilon=F(-(-scaled.numerator//scaled.denominator),10**9)
        assert epsilon>=raw and epsilon>=0
        count=0
        for r in live:
            for image in choices(h,r):
                assert epsilon*mu[r]+image-b*h[r]>=d[r]
                count+=1
        assert F(1)-epsilon<=a
        total+=count
        report=dict(k=k,rows_verified=count,epsilon=str(epsilon),
                    epsilon_decimal=float(epsilon),
                    spectral_lower_exact=str(a),spectral_upper_exact=str(b),
                    spectral_lower_decimal=float(a),spectral_upper_decimal=float(b),
                    cost_baseline_decimal=float(max(d[r]/mu[r] for r in live)),
                    all_exact_checks_pass=True)
        reports.append(report)
        print(json.dumps({key:value for key,value in report.items() if not key.endswith('_exact')}),flush=True)
    (folder/'policy_residual_barrier_exact.json').write_text(json.dumps(
        dict(status='Exact rational verification of finite certificates',
             total_row_inequalities=total,levels=reports),indent=2))


if __name__=='__main__': main()
