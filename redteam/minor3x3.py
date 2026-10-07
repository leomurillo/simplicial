"""Probe small (3x3, 4x4) NON-LEADING principal minors on spread index sets
for the power family f=p^d. Goal: find a minor that's negative at a FIXED
position regardless of d -> would close the whole power family uniformly.

For p^d (and (p+r)^d), b_n = B_n^d, B_n = prod(p_i + r).
The 3x3 minor on indices {a,b,c} (a<b<c) of Hankel is
  det[[B_{2a}, B_{a+b}, B_{a+c}],
      [B_{a+b}, B_{2b}, B_{b+c}],
      [B_{a+c}, B_{b+c}, B_{2c}]]^... no -- entries are b_{i+j}=B_{i+j}^d.
So minor M(a,b,c;d) = det[[B_{2a}^d, B_{a+b}^d, B_{a+c}^d],
                          [B_{a+b}^d, B_{2b}^d, B_{b+c}^d],
                          [B_{a+c}^d, B_{b+c}^d, B_{2c}^d]].
Scan many {a,b,c} and many d; report the SMALLEST max-index minor that goes neg
and whether its negativity persists across d."""
from sympy import primerange, Matrix, Integer
import itertools

P = list(primerange(2, 100000))

def Bn(r, L):
    """B_0..B_{L-1}, B_n=prod_{i=1}^n (p_i+r)."""
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*= (Integer(P[i-1])+r); out.append(a)
    return out

def minor3(B, a, b, c, d):
    idx=[a,b,c]
    M=Matrix(3,3, lambda i,j: B[idx[i]+idx[j]]**d)
    return M.det()

# For f=p^d use r=0. Find spread 3x3 minors negative.
r=0
maxidx=14
B=Bn(r, 2*maxidx+2)
print("Searching 3x3 non-leading minors of p^d for negativity...")
found=[]
for a,b,c in itertools.combinations(range(0,maxidx+1),3):
    # try a few d values
    negd=[]
    for d in [2,4,8,16,32]:
        if minor3(B,a,b,c,d) < 0:
            negd.append(d)
    if negd:
        found.append(((a,b,c), c, negd))
# sort by max index c (smaller = exposes failure earlier)
found.sort(key=lambda x: x[1])
print(f"3x3 minors that go negative for some tested d (sorted by max index):")
for (abc, c, negd) in found[:25]:
    print(f"   indices {abc}, maxidx={c}, negative at d={negd}")
print(f"total such minors: {len(found)}")
