"""Independent integer-only edge checks of the stored policy graphs and heights."""
from pathlib import Path
import json
import numpy as np


def main():
    reports=[]
    folder=Path(__file__).parent
    for k in range(2,11):
        modulus=3**k
        for gamma in (('1.0',) if k==10 else ('0.8','0.9','1.0')):
            data=np.load(folder/f'policy_cycle_k{k}_g{gamma}.npz')
            live=[int(v) for v in data['live']]
            chosen=[int(v) for v in data['chosen']]
            height={r:int(v) for r,v in zip(live,data['height'])}
            assert set(live)=={r for r in range(modulus) if r%3}
            count=0
            for r,t in zip(live,chosen):
                assert height[2*r%modulus]-height[r]<=1
                count+=1
                if r%3==2:
                    assert (3*t-(2*r-1)) % modulus == 0
                    if t%3:
                        assert height[t]-height[r]<=-1
                        count+=1
            reports.append(dict(k=k,gamma=gamma,edges=count,
                                height_range=max(height.values())-min(height.values()),
                                exact_integer_checks_pass=True))
    result=dict(graphs=len(reports),edges=sum(r['edges'] for r in reports),
                limitation='Certifies stored graphs. Does not certify that they are minimizing, or cover all minimizing policies.',
                reports=reports)
    (folder/'policy_cycle_heights_exact.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(dict(graphs=result['graphs'],edges=result['edges'],all_exact_checks_pass=True)))


if __name__=='__main__':main()
