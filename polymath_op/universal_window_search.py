"""
Search for windows where Q(m)>0 holds for ALL polynomials.
Q(m) = v^2 c_m - u w c_{m+2}, with c_l=f(p_l).
For a fixed window of 4 primes (q0,q1,q2,q3), Q is a function of f.
Q>0  <=>  (f(q2)-f(q1))^2 f(q0) > (f(q1)-f(q0))(f(q3)-f(q2)) f(q2).

We want a window such that this holds for EVERY admissible f (deg>=1, f(p)>0 on primes).
Test on a big basis of monomials and combos. If a window survives ALL test polynomials,
it's a strong candidate for a universal window -> then prove symbolically.

Also: directly test the gap-peak windows. A window with gaps (g0,g1,g2)=(small,LARGE,small).
"""
from sympy import primerange, Integer, Rational, symbols, expand, Poly, factor, simplify

P=list(primerange(2,2000))

def Qval(window, f):
    q0,q1,q2,q3=window
    A,B,C,Dd=f(q0),f(q1),f(q2),f(q3)
    return (C-B)**2*A - (B-A)*(Dd-C)*C

# windows (consecutive primes) by starting index m (1-indexed)
def window(m): return (P[m-1],P[m],P[m+1],P[m+2])

# big test family of monic-ish polynomials (positivity on primes will hold for these on the window)
tests=[]
tests.append(("p", lambda p:p))
tests.append(("p^2", lambda p:p**2))
tests.append(("p^3", lambda p:p**3))
tests.append(("p^4", lambda p:p**4))
tests.append(("p^5", lambda p:p**5))
for c in [1,2,5,10,100,1000,10**6]:
    tests.append((f"p+{c}", lambda p,c=c:p+c))
    tests.append((f"p^2+{c}", lambda p,c=c:p**2+c))
    tests.append((f"p^3+{c}", lambda p,c=c:p**3+c))
for c in [1,2,5,10,100]:
    tests.append((f"p^2+{c}p", lambda p,c=c:p**2+c*p))
    tests.append((f"p^3+{c}p", lambda p,c=c:p**3+c*p))
    tests.append((f"p^3+{c}p^2", lambda p,c=c:p**3+c*p**2))
# polynomials with negative coeffs but still >0 on primes>=2
tests.append(("p-1", lambda p:p-1))
tests.append(("p^2-p+1", lambda p:p**2-p+1))
tests.append(("p^2-2p+2", lambda p:p**2-2*p+2))
tests.append(("p^3-p^2-p+3", lambda p:p**3-p**2-p+3))
tests.append(("2p+1", lambda p:2*p+1))   # non-monic; sign only depends on monic but include
tests.append(("(p-2)(p-3)+1", lambda p:(p-2)*(p-3)+1))

print("Searching m=1..80 for windows where Q>0 for ALL test polynomials...")
universal=[]
for m in range(1,80):
    w=window(m)
    allpos=True
    for name,f in tests:
        # admissibility: f>0 on the 4 window primes
        if any(f(x)<=0 for x in w):
            allpos=False; break
        if Qval(w,f)<=0:
            allpos=False; break
    if allpos:
        universal.append((m,w))
print("Windows with Q>0 for every test polynomial:")
for m,w in universal:
    i=(m-1)//2 if m%2==1 else None
    gaps=(w[1]-w[0],w[2]-w[1],w[3]-w[2])
    print(f"   m={m:3d} window={w} prime-gaps={gaps}  {'(ODD m: consec minor {%d,%d,%d})'%(i,i+1,i+2) if m%2==1 else '(even m)'}")
