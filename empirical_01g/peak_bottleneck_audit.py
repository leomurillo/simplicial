"""Exact capped inverse-tree audit; no assumption of universal convergence."""
from collections import deque
from pathlib import Path
import json


def predecessors(root, cap):
    seen={root}; queue=deque([root])
    while queue:
        x=queue.popleft()
        candidates=[2*x]
        if x%6==4:
            candidates.append((x-1)//3)
        for y in candidates:
            if 1<=y<=cap and y not in seen:
                seen.add(y);queue.append(y)
    return seen


def main():
    rows=[]
    for H in [16,52,160,9232,13120,250504]:
        before=predecessors(1,H-1);after=predecessors(1,H)
        added=after-before
        assert before<=after
        assert added==predecessors(H,H)
        rows.append(dict(H=H,before=len(before),after=len(after),added=len(added),
                         least_added=min(added),fraction_of_after=len(added)/len(after)))
        if H==9232:
            assert predecessors(3077,H)==added-{H}
            assert len(added)==1579
    C=S=0;w=[4,2,2,4,3]
    for s in w:
        C=3*C+2**S;S+=s
    modulus=2**(S+1)
    r=(2**S-C)*pow(3**len(w),-1,modulus)%modulus
    assert (C,S,r,modulus)==(5953,15,3077,65536)
    for k in range(1000):
        n=3077+65536*k;z=n
        for s in w:
            v=3*z+1
            a=(v&-v).bit_length()-1
            assert a==s
            z=v>>a
        assert z==23+486*k and z<n
    result=dict(status='passed',capped_basins=rows,
                gate=dict(exponents=w,C=C,S=S,residue=r,modulus=modulus,
                          input='3077+65536k',output='23+486k',tested_k=1000),
                convention='Standard Collatz; inverse branches 2x and (x-1)/3 when x=4 mod 6; positive vertices only.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
