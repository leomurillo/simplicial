import numpy as np, itertools, random, time, sys, math
from collections import defaultdict
E = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/4.0
A1 = np.array([E[0]-E[1],E[0]-E[2],E[0]-E[3]])
L = int(sys.argv[1]); STEPS = int(float(sys.argv[2])); seed=int(sys.argv[3]) if len(sys.argv)>3 else 1
random.seed(seed)
cells=[np.array(c) for c in itertools.product(range(L),repeat=3)]; nc=len(cells)
cid={tuple(c):i for i,c in enumerate(cells)}
dvec=[np.zeros(3,int)]+[-np.eye(3,dtype=int)[i] for i in range(3)]
Aend=[];Bend=[]
for c in cells:
    for n in range(4): Aend.append(cid[tuple(c)]); Bend.append(nc+cid[tuple(np.mod(c+dvec[n],L))])
nb=4*nc; NT=2*nc
inc=[[] for _ in range(NT)]
for b in range(nb): inc[Aend[b]].append(b); inc[Bend[b]].append(b)
sig=[1,1,-1,-1]*nc
# tetra fractional coordinates (in A1 basis) for displacement; B tet offset E0 in cartesian
A1inv=np.linalg.inv(A1)
pos=[cells[t]@A1 for t in range(nc)]+[cells[t]@A1+E[0] for t in range(nc)]
lam=nb/3.0
closed_steps=0; hist=defaultdict(int); state_open=False; tail=head=-1
def out_bonds(t):
    if t<nc: return [b for b in inc[t] if sig[b]==1]
    return [b for b in inc[t] if sig[b]==-1]
def other(b,t): return Bend[b] if Aend[b]==t else Aend[b]
t0=time.time()
for step in range(STEPS):
    if not state_open:
        closed_steps+=1
        b=random.randrange(nb)
        u = Aend[b] if sig[b]==1 else Bend[b]      # out-end
        w = Bend[b] if sig[b]==1 else Aend[b]
        sig[b]=-sig[b]; tail,head=u,w; state_open=True
    else:
        hist[(tail,head) if False else (tail<nc, head)]  # placeholder no-op
        key=(tail>=nc, tail, head)
        hist[(tail,head)]+=1
        ob=out_bonds(head)            # head has 3 out-bonds
        b=ob[random.randrange(len(ob))]
        x=other(b,head); sig[b]=-sig[b]
        if x==tail: state_open=False
        else: head=x
print(f'L={L} steps={STEPS:.1e} closed={closed_steps} time {time.time()-t0:.0f}s', flush=True)
# aggregate by (tail type, displacement vector)
agg=defaultdict(int)
for (t,h),c in hist.items():
    d=pos[h]-pos[t]; f=d@A1inv; f=f-np.round(f/L)*L; d=f@A1
    agg[(t>=nc, tuple(np.round(d,6)))]+=c
raw=dict(hist); np.save(f'worm_raw_L{L}_s{seed}.npy',{'hist':raw,'closed':closed_steps,'lam':lam,'nc':nc}); np.save(f'worm_L{L}_s{seed}.npy', {'agg':dict(agg),'closed':closed_steps,'lam':lam,'nc':nc,'L':L})
# adjacency check: R for adjacent displacements should be 1/2
adj=[k for k in agg if abs(np.linalg.norm(k[1])-np.linalg.norm(E[0]))<1e-6]
Rs=[lam*agg[k]/(closed_steps*nc) for k in adj]
print('adjacent R values (expect 0.5):', np.round(Rs,3))
