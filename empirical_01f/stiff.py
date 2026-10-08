import numpy as np, itertools, random, sys, time
E=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/4.0; A1=np.array([E[0]-E[1],E[0]-E[2],E[0]-E[3]])
L=int(sys.argv[1]); SW=int(sys.argv[2]); random.seed(int(sys.argv[3]))
cells=[np.array(c) for c in itertools.product(range(L),repeat=3)]; nc=len(cells); cid={tuple(c):i for i,c in enumerate(cells)}
dvec=[np.zeros(3,int)]+[-np.eye(3,dtype=int)[i] for i in range(3)]
Aend=[];Bend=[];pos=[];ev=[]
for c in cells:
    for n in range(4):
        Aend.append(cid[tuple(c)]); Bend.append(nc+cid[tuple(np.mod(c+dvec[n],L))]); pos.append(c@A1+E[n]/2); ev.append(E[n])
pos=np.array(pos); ev=np.array(ev); nb=4*nc
inc=[[] for _ in range(2*nc)]
for b in range(nb): inc[Aend[b]].append(b); inc[Bend[b]].append(b)
sig=np.array([1,1,-1,-1]*nc)
def loop_update():
    node=random.randrange(2*nc); visited={node:0}; pb=[]
    while True:
        outs=[b for b in inc[node] if sig[b]==(1 if node<nc else -1)]
        b=outs[random.randrange(2)]; nxt=Bend[b] if node<nc else Aend[b]; pb.append(b)
        if nxt in visited: sig[pb[visited[nxt]:]]*=-1; return
        visited[nxt]=len(pb); node=nxt
rec=2*np.pi*np.linalg.inv(A1).T
qs=[]
for m in itertools.product(range(-2,3),repeat=3):
    if any(m): qs.append(np.array(m)/L@rec)
qs=np.array(qs); qn=np.linalg.norm(qs,axis=1); keep=qn<=np.sort(np.unique(np.round(qn,6)))[2]+1e-9; qs=qs[keep]; qn=qn[keep]
ph=np.exp(-1j*pos@qs.T)            # nb x nq
V=nc*abs(np.linalg.det(A1))
acc=np.zeros(len(qs)); n=0; t0=time.time()
for sw in range(SW):
    for _ in range(nc//2): loop_update()
    if sw>=SW//10:
        B=(sig[:,None]*ph).T@ev        # nq x 3
        acc+=np.sum(np.abs(B)**2,axis=1)/V; n+=1
S=acc/n
for qq in np.unique(np.round(qn,6)):
    sel=np.abs(qn-qq)<1e-6
    print(f'L={L} |q|={qq:.4f} n={sel.sum()}  <|B|^2>/V = {S[sel].mean():.4f} +- {S[sel].std()/np.sqrt(sel.sum()):.4f}   K_q = {2/S[sel].mean():.4f}')
print(f'{time.time()-t0:.0f}s')
