"""
We need an UNCONDITIONAL source of windows with b^2 > a e (b=mid gap, a,e=outer).
Specific prime constellations are open. But UNBOUNDED GAPS are unconditional.

Idea: take b = a LARGE gap (g_n unbounded). Its neighbors a=g_{n-1}, e=g_{n+1}.
If we can find large gaps whose immediate neighbors are not too large, b^2>ae holds.
But neighbors of a large gap could also be large.

Alternative unconditional levers to test numerically first (then prove):
 (L1) "b is a strict local max among (a,b,e) with b>=2max(a,e)"  -> b^2>=4ae*... no, need b^2>ae.
      Even b>max(a,e) gives b^2>a e only if b^2>ae; b>max(a,e)=> b^2>max(a,e)^2>=ae. YES!
      So a STRICT local max gap (b>a and b>e) gives b^2 > ae automatically (b^2>a e since b>a,b>e => b^2>ae).
 (L2) local max gaps are infinite & occur at arbitrarily large primes (need to confirm unconditional).

So the trigger reduces to: INFINITELY MANY n with g_n > g_{n-1} and g_n > g_{n+1}
(a strict local-max prime gap), occurring at arbitrarily large primes.
=> then b=g_n, a=g_{n-1}, e=g_{n+1}, b>a,b>e => b^2>ae => Q>0 for large primes/any f.

Check: do strict local-max gaps occur infinitely often & arbitrarily large prime?
Also need b>a AND b>e STRICT. Count them.
"""
from sympy import primerange

P=list(primerange(2,200000))
G=[P[i+1]-P[i] for i in range(len(P)-1)]   # G[i]=gap after P[i]

# strict local max gap at index i (1<=i<=len-2): G[i]>G[i-1] and G[i]>G[i+1]
locmax=[]
for i in range(1,len(G)-1):
    if G[i]>G[i-1] and G[i]>G[i+1]:
        locmax.append(i)
print(f"Total strict-local-max gaps among first {len(P)} primes: {len(locmax)}")
print("First 15 (index i, prime P[i], window (P[i-1..i+2]), gaps (a,b,e)):")
for i in locmax[:15]:
    a,bb,e=G[i-1],G[i],G[i+1]
    print(f"  i={i:5d} P[i]={P[i]:6d} window=({P[i-1]},{P[i]},{P[i+1]},{P[i+2]}) gaps=({a},{bb},{e}) b^2={bb*bb} ae={a*e} -> b^2>ae: {bb*bb>a*e}")
print("Last 8 (largest primes in range):")
for i in locmax[-8:]:
    a,bb,e=G[i-1],G[i],G[i+1]
    print(f"  i={i:5d} P[i]={P[i]:6d} gaps=({a},{bb},{e}) b^2>ae: {bb*bb>a*e}")
print(f"\nLargest prime with a strict-local-max gap in range: P={P[locmax[-1]]}")
print("Fraction of indices that are strict local max:", round(len(locmax)/len(G),3))
