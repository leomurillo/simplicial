import itertools, numpy as np
from collections import defaultdict
L=2
cells=[np.array(c) for c in itertools.product(range(L),repeat=3)]; nc=len(cells); cid={tuple(c):i for i,c in enumerate(cells)}
dvec=[np.zeros(3,int)]+[-np.eye(3,dtype=int)[i] for i in range(3)]
bonds=[(cid[tuple(c)], cid[tuple(np.mod(c+dvec[n],L))]) for c in cells for n in range(4)]
def count(charge):   # charge[t] for t in 0..2nc-1 : required sum of out-flux (A: sum sigma ; B: -sum sigma)
    states={tuple([0]*nc):1}; left=[4]*nc
    for a in range(nc):
        allowed=[s for s in itertools.product([1,-1],repeat=4) if sum(s)==charge[a]]
        mine=[(n,bonds[4*a+n][1]) for n in range(4)]
        for n,b in mine: left[b]-=1
        new=defaultdict(int)
        for st,w in states.items():
            for s in allowed:
                lst=list(st)
                for (n,b),x in zip(mine,s): lst[b]+=x
                ok=True
                for b in range(nc):
                    need=-charge[nc+b]          # B out-flux = -sum sigma  => sum sigma = -charge
                    if abs(lst[b]-need)>left[b]: ok=False;break
                if ok: new[tuple(lst)]+=w
        states=new
    return sum(w for st,w in states.items() if all(st[b]==-charge[nc+b] for b in range(nc)))
ice=count([0]*(2*nc)); print('ice',ice)
res={}
for t,h in [(0,nc+0),(0,nc+1),(0,1),(0,nc+7),(0,7)]:
    ch=[0]*(2*nc); ch[t]=-2; ch[h]=2
    res[(t,h)]=count(ch)/ice
print('exact R(tail,head):',res)
np.save('worm_exact_L2.npy',res)
