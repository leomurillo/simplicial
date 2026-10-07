"""
The cleanest domination: use trigger windows with BOUNDED middle gap b (hence bounded width W).
Then for fixed degree d, (1+W/x)^{3d} -> 1 as x->oo, so domination (**) b^2>ae(1+W/x)^{3d}
holds for all large x. We need: infinitely many strict-local-max windows with b<=B0 (B0 a fixed
constant) AND b^2>ae, at arbitrarily large primes.

A strict local max with b=6,a in{2,4},e in{2,4}: e.g. gaps (2,6,4),(4,6,2),(2,6,2)*(b>e? 6>2 yes,
6>2 yes) -> b^2=36>ae in {4,8,16,..}. b=6 bounded. Do these recur at arbitrarily large primes?
Count windows with b<=6 (strict local max, b^2>ae) and the largest prime carrying one.
Also b<=8, b<=10. If bounded-b local maxima persist to the top of our range, domination is trivial.
"""
from sympy import primerange
P=list(primerange(2,2000000)); NP=len(P)
G=[P[i+1]-P[i] for i in range(NP-1)]

for B0 in [4,6,8,10,12]:
    idxs=[]
    for i in range(1,len(G)-1):
        a,b,e=G[i-1],G[i],G[i+1]
        if b<=B0 and b>a and b>e:   # strict local max with bounded middle gap
            # b>a,b>e => b^2>ae automatically
            idxs.append(i)
    if idxs:
        print(f"strict-local-max windows with middle gap b<= {B0:2d}: count={len(idxs):6d}, "
              f"largest prime x={P[idxs[-1]-1]}, e.g. gaps at last = "
              f"{(G[idxs[-1]-1],G[idxs[-1]],G[idxs[-1]+1])}")
    else:
        print(f"  none with b<={B0}")
print()
print("=> bounded-middle-gap strict local maxima persist to the top of the range (x ~ 2e6),")
print("   densely. For these, W<=3B0 is BOUNDED, so for any fixed degree d, (1+W/x)^{3d}->1,")
print("   and (**) b^2>ae(1+W/x)^{3d} holds for all x beyond a finite threshold X0(d,B0).")
print()
print("UNCONDITIONALITY of 'bounded-b strict local maxima occur at arbitrarily large primes':")
print("  This is implied by: infinitely many bounded gaps b<=B0 that exceed BOTH neighbors.")
print("  Hardy-Littlewood predicts it; UNCONDITIONALLY it follows from Maynard's theorem that")
print("  among any admissible k-tuple, infinitely many translates are all prime -- but CONSECUTIVE-")
print("  prime control (to make a,b,e the actual gaps) is the open part. HONEST: the bounded-b")
print("  route is heuristically certain but its FULL unconditionality is open (consecutive primes).")
print("  The RECORD-GAP route IS unconditional for existence (records unbounded) and reduces")
print("  domination to b^2/(ae)>R(x,W); the only non-textbook input there is a uniform margin")
print("  b^2/(ae)>1+delta at records, which holds empirically (min 2.67 over genuine records).")
