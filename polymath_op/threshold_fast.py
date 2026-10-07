"""
FAST: threshold X0 for fixed pattern (a,b,e), f=x^d, using float64 root bracketing
(bisection on Q(x), which is positive for large x when b^2>ae). Avoids slow high-prec polyroots.
"""
from sympy import symbols, Poly
import numpy as np

def Qfun_factory(a,b,e,d):
    def Q(xv):
        xv=np.array(xv,dtype=float)
        q0,q1,q2,q3=xv,xv+a,xv+a+b,xv+a+b+e
        F=lambda t:t**d
        u=F(q1)-F(q0); v=F(q2)-F(q1); w=F(q3)-F(q2)
        return v*v*F(q0)-u*w*F(q2)
    return Q

def largest_root(a,b,e,d,hi=1e7):
    Q=Qfun_factory(a,b,e,d)
    # Q(x) ~ d^2(b^2-ae) x^{3d-2} >0 for large x. Find largest sign change scanning down.
    # scan x on a grid (log) from high to low; find last x where Q<=0
    xs=np.unique(np.concatenate([np.arange(1,200), np.geomspace(1,hi,4000)]))
    vals=Q(xs)
    neg=xs[vals<=0]
    if len(neg)==0: return 0.0
    x_lo=neg.max()
    # refine: between x_lo and next grid point Q crosses; bisect upward
    # find smallest grid x>x_lo with Q>0
    pos_above=xs[(xs>x_lo)&(vals>0)]
    if len(pos_above)==0: return x_lo
    x_hi=pos_above.min()
    for _ in range(80):
        mid=0.5*(x_lo+x_hi)
        if Q(mid)>0: x_hi=mid
        else: x_lo=mid
    return x_hi

patterns=[(2,4,2),(2,6,4),(2,10,2),(4,6,2),(6,8,4),(4,14,4),(6,10,2),(2,8,6)]
print("Largest x-root X0(d) (Q>0 for x>X0), f=x^d:")
print("pattern       b^2,ae | d=1   d=2   d=3   d=5   d=8   d=12  d=20  d=40  d=80")
for (a,b,e) in patterns:
    row=[largest_root(a,b,e,d) for d in [1,2,3,5,8,12,20,40,80]]
    print(f"  ({a},{b},{e})  {b*b:3d},{a*e:3d} | "+" ".join(f"{r:5.1f}" for r in row))
print("\nIf X0(d) is BOUNDED in d for the tightest patterns, one recurring bounded pattern closes it.")
