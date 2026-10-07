"""
For a FIXED gap pattern (a,b,e) with b^2>ae, find the threshold x>=X0 beyond which
Q(x) = v^2 c_m - u w c_{m+2} > 0 for f(p)=p^d, as a function of d.
This tells us how large x must be (relative to the pattern) for the leading term to win.

We treat x as a real variable (window x,x+a,x+a+b,x+a+b+e) and find the largest real root
of Q(x) for f=x^d. If X0(d) stays BOUNDED as d->oo for a fixed pattern, then a single
pattern occurring at arbitrarily large primes closes everything. Check several patterns.

We also handle GENERAL monic f (not just monomial): the worst case among monic f of degree d.
But first the monomial picture.
"""
from sympy import symbols, Poly, Rational, real_roots, nsimplify, Integer, RealField
import mpmath as mp
mp.mp.dps=40

x=symbols('x', real=True)

def maxroot_monomial(a,b,e,d):
    q0=x; q1=x+a; q2=x+a+b; q3=x+a+b+e
    F=lambda t:t**d
    u=F(q1)-F(q0); v=F(q2)-F(q1); w=F(q3)-F(q2)
    Q=Poly((v**2*F(q0)-u*w*F(q2)).expand(), x)
    coeffs=[mp.mpf(str(c)) for c in Q.all_coeffs()]
    roots=mp.polyroots(coeffs, maxsteps=200, extraprec=200)
    realpos=[r.real for r in roots if abs(r.imag)<1e-12 and r.real>0]
    return max(realpos) if realpos else 0.0

patterns=[(2,4,2),(2,6,4),(2,10,2),(4,6,2),(6,8,4),(2,8,6),(4,14,4),(6,10,2)]
print("Largest positive real root X0(d) of Q(x) for f=x^d (Q>0 for x>X0):")
print("pattern(a,b,e)  b^2,ae |  d=1    d=2    d=3    d=5    d=8    d=12   d=20   d=40")
for (a,b,e) in patterns:
    row=[]
    for d in [1,2,3,5,8,12,20,40]:
        row.append(maxroot_monomial(a,b,e,d))
    print(f"  ({a},{b},{e})  {b*b:3d},{a*e:3d} | " + " ".join(f"{r:6.1f}" for r in row))
print("\nIf X0(d) stays bounded (or grows slowly) for a fixed tight pattern, a single recurring")
print("bounded pattern at large primes suffices. (2,4,2)=twin-cousin-twin is the tightest.")
