"""
Is the quark-lepton Yukawa disconnection ACCIDENTAL or PROTECTED?
Test: with SM gauge group and ANY color-singlet scalar, can a 1-Higgs
trilinear ever connect a quark-sector vertex to a lepton-sector vertex?
Also test robustness: add nu^c=(1,1)_0 (Dirac+Majorana). Does c stay 2?
"""
import itertools
# (SU3 triality t in {0:1,1:3,2:3bar via (p-q)mod3}, dimcolor, SU2 2j, Y)
SM = {
 'Q' :('3', 1, +1/6), 'uc':('3b',0,-2/3), 'dc':('3b',0,+1/3),
 'L' :('1', 1, -1/2), 'ec':('1', 0,+1.0),
}
NU = {'nuc':('1',0,0.0)}                    # optional sterile singlet
HIGGS = {'V':('1',1,+1/2),'Vs':('1',1,-1/2)}

def col_singlet(cs):
    # cs: multiset of color labels among '1','3','3b'. With <=2 colored
    # matter + colorless higgs: singlet iff {3,3b} present and rest '1',
    # or all '1'. (3*3,3b*3b,lone 3/3b -> no singlet.)
    nz=[c for c in cs if c!='1']
    if not nz: return True
    if sorted(nz)==['3','3b']: return True
    return False
def su2_singlet(js):
    poss={0}
    for s in js:
        nx=set()
        for a in poss:
            for v in range(abs(a-s),a+s+1,2): nx.add(v)
        poss=nx
    return 0 in poss

def edges(matter):
    E=[]
    for i,j in itertools.combinations_with_replacement(matter,2):
        for h,(hc,hj,hy) in HIGGS.items():
            ci,ji,yi=matter[i]; cj,jj,yj=matter[j]
            if col_singlet([ci,cj,hc]) and su2_singlet([ji,jj,hj]) \
               and abs(yi+yj+hy)<1e-9 and i!=j:
                E.append((i,j,h))
    return E

def components(matter,E):
    import collections
    adj=collections.defaultdict(set)
    for a,b,_ in E: adj[a].add(b); adj[b].add(a)
    seen=set(); comps=[]
    for v in matter:
        if v in seen: continue
        st=[v]; c=[]
        while st:
            x=st.pop()
            if x in seen: continue
            seen.add(x); c.append(x); st+=list(adj[x])
        comps.append(sorted(c))
    return comps

for label,M in [('SM minimal',SM),('SM + nu_R (Dirac)',{**SM,**NU})]:
    E=edges(M); C=components(M,E)
    print(f"\n{label}: edges={[(a,b,h) for a,b,h in E]}")
    print(f"  components={C}  -> c={len(C)}  -> residual bits=2^(c-1)={2**(len(C)-1)}")

# THE KEY TEST: try EVERY conceivable cross-component edge; show each is
# color-forbidden for ANY color-singlet Higgs (color is the obstruction).
print("\nCross-component edge attempts (quark-sector vertex vs lepton-sector):")
qside=['Q','uc','dc']; lside=['L','ec']
for q in qside:
    for l in lside:
        cq=SM[q][0]; cl=SM[l][0]
        # Higgs colorless; need color singlet from {cq,cl,'1'}
        ok=col_singlet([cq,cl,'1'])
        print(f"  {q}({cq}) - {l}({cl}) + colorless Higgs : "
              f"color-singlet possible? {ok}")
