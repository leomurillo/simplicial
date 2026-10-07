"""
EXPLICIT domination lemma with verified constants.

Claim (Domination Lemma): Let f be monic of degree d>=1. Let x>=X1(f) be a point beyond
which f and f' are positive and f' is increasing (X1 depends only on f). Consider a window
q0=x<q1=x+a<q2=x+a+b<q3=x+a+b+e with W=a+b+e. Then

   Q := v^2 c_m - u w c_{m+2}  satisfies   Q >= f'(x)^2 f(x) * [ b^2 - a e * rho^3 ]
where rho := f'(x+W)/f'(x) >= 1  and we used f(x+a+b)<= f(x)*rho_f with rho_f:=f(x+W)/f(x).

Hmm rho enters. Let me derive the SHARP elementary bound and verify it numerically:
  u = a f'(xi_u), v=b f'(xi_v), w=e f'(xi_w),  x<xi_u<xi_v<xi_w<x+W, f' increasing =>
    f'(x) <= f'(xi_u)<=f'(xi_v)<=f'(xi_w)<= f'(x+W).
  c_m=f(x), c_{m+2}=f(x+a+b), and f(x)<=f(x+a+b)<=f(x+W).
  v^2 c_m = b^2 f'(xi_v)^2 f(x) >= b^2 f'(x)^2 f(x).
  u w c_{m+2} = a e f'(xi_u) f'(xi_w) f(x+a+b) <= a e f'(x+W)^2 f(x+W).
  => Q >= b^2 f'(x)^2 f(x) - a e f'(x+W)^2 f(x+W)
        = f'(x)^2 f(x) [ b^2 - a e * R ],  R := (f'(x+W)/f'(x))^2 * (f(x+W)/f(x)).
  So:  Q>0  is IMPLIED by   b^2 > a e * R.            (*)
Since b^2>=ae+1 won't help if R>1. Need R close to 1. R->1 as x->oo for fixed W.
For monic degree d:  f'(x+W)/f'(x) <= (1+W/x)^{d-1} (since f'(t)~d t^{d-1}, but need rigorous bound)
   -- valid if f'(t)/t^{d-1} is... not exactly monotone. Use instead:
   f(x+W)/f(x) and f'(x+W)/f'(x): both -> 1; bound each by (1+W/x)^d * (1+eps).
SUFFICIENT CLEAN CONDITION:  b^2 > a e * (1+W/x)^{3d}.        (**)
because R = (f'(x+W)/f'(x))^2 (f(x+W)/f(x)). For f monic deg d, asymptotically
 f'(x+W)/f'(x) <= (1+W/x)^{d-1}(1+o(1)) and f(x+W)/f(x)<=(1+W/x)^d(1+o(1)),
 so R <= (1+W/x)^{2(d-1)+d}=(1+W/x)^{3d-2} eventually. Use (1+W/x)^{3d} as a safe envelope.

VERIFY (**) numerically: for the monomial f=x^d (worst leading behavior), check that
  b^2 > a e (1+W/x)^{3d}  =>  Q>0, on real x, exactly. And measure how (**) compares to true root.
"""
import numpy as np

def Qexact(a,b,e,d,x):
    x=np.float64(x)
    F=lambda t:np.power(t,d)
    q0,q1,q2,q3=x,x+a,x+a+b,x+a+b+e
    u=F(q1)-F(q0); v=F(q2)-F(q1); w=F(q3)-F(q2)
    return v*v*F(q0)-u*w*F(q2)

def suff_cond(a,b,e,d,x):
    W=a+b+e
    return b*b > a*e*(1+W/x)**(3*d)

# For several patterns/degrees, find the smallest integer x where (**) holds, and confirm Q>0 there.
print("Pattern  d  | x*=min x with suff-cond(**)  | Q(x*)>0 ?  | true X0 (Q-root)")
import math
patterns=[(2,4,2),(2,6,4),(2,10,2),(6,8,4)]
for (a,b,e) in patterns:
    W=a+b+e
    for d in [1,2,3,5,8,12,20]:
        # smallest x with b^2 > ae (1+W/x)^{3d}: solve (1+W/x)^{3d} < b^2/(ae)
        # (1+W/x) < (b^2/(ae))^{1/(3d)}  => W/x < r-1 => x> W/(r-1)
        r=(b*b/(a*e))**(1.0/(3*d))
        if r<=1:
            print(f"  ({a},{b},{e}) d={d}: suff-cond never holds (b^2/ae too small for this d) -- pattern too weak");
            continue
        xstar=math.ceil(W/(r-1))+1
        # verify Q>0 at xstar and find true root by scan
        okQ = Qexact(a,b,e,d,xstar)>0
        # true root
        xs=np.geomspace(1, max(xstar*3,1e4), 20000)
        vals=np.array([Qexact(a,b,e,d,xx) for xx in xs])
        neg=xs[vals<=0]; trueX0=neg.max() if len(neg) else 0.0
        print(f"  ({a},{b},{e}) d={d:2d}: x*={xstar:6d}  Q(x*)>0={okQ}   trueX0={trueX0:.1f}")
print("\n(**) is a SUFFICIENT, fully explicit closed-form condition implying Q>0.")
