"""
FINAL BATTERY: large randomized set of monic f (varied degree, coeffs incl huge constants,
negative middle coeffs as long as f(p)>0). Confirm EVERY one has an explicit negative principal
3x3 Hankel minor (a firing window s), and record the witness. NO survivor expected.
"""
from sympy import primerange, Integer
import random
Pg=list(primerange(2,2000000))
def fires(coeffs,s):
    # coeffs: list a_d..a_0 (a_d=1 monic). f(p)=sum a_k p^k.
    def f(p):
        v=0
        for ck in coeffs: v=v*p+ck
        return v
    def C(l): return f(Pg[l-1])
    g0=C(s+1)-C(s); g1=C(s+2)-C(s+1); g2=C(s+3)-C(s+2)
    if g0<=0 or g2<=0: return None  # need increasing
    return C(s)*g1*g1 > C(s+2)*g0*g2
def f_at(coeffs,p):
    v=0
    for ck in coeffs: v=v*p+ck
    return v

random.seed(12345)
def positive_on_primes(coeffs, npr=200):
    return all(f_at(coeffs,Pg[i])>0 for i in range(npr))

tests=[]
# systematic
for d in range(1,9):
    for const in [0,1,2,5,10,10**6]:
        c=[1]+[0]*(d-1)+[const]
        tests.append(c)
# random
cnt=0
while cnt<60:
    d=random.randint(1,7)
    c=[1]+[random.randint(-5,20) for _ in range(d-1)]+[random.randint(0,10**6)]
    if positive_on_primes(c):
        tests.append(c); cnt+=1

survivors=[]
maxwitness=0
for c in tests:
    # search for a firing window (odd s preferred), up to s=2000
    w=None
    for s in range(1,3000):
        r=fires(c,s)
        if r is True:
            w=s; break
    if w is None:
        survivors.append(c)
    else:
        maxwitness=max(maxwitness,w)
print(f"Tested {len(tests)} monic f (deg 1..8, consts incl 10^6, random coeffs).")
print(f"Survivors (NO negative minor found up to s=3000): {len(survivors)}")
if survivors:
    for c in survivors[:10]: print("  SURVIVOR:", c)
else:
    print(f"NO SURVIVORS. Every monic f has a firing window; max witness index s used = {maxwitness}.")
# also confirm a couple high-degree ones explicitly with exact determinant
from sympy import Matrix
def exact_neg_minor(coeffs):
    def f(p):
        v=0
        for ck in coeffs: v=v*p+ck
        return v
    b=[Integer(1)];A=Integer(1)
    for i in range(1,40):
        A*=f(Pg[i-1]); b.append(A)
    import itertools
    H=Matrix(18,18,lambda i,j:b[i+j])
    for idx in itertools.combinations(range(15),3):
        if H[idx,idx].det()<0: return idx,H[idx,idx].det()
    return None
ex=exact_neg_minor([1,0,0,0,0,0,0,5])  # p^7+5
print("p^7+5: explicit negative principal minor:", ex[0], "det<0:", ex[1]<0)
