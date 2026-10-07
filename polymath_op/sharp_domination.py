"""
SHARPER domination: the crude bound lost the cancellation. Let's compute Q for monic f exactly
in terms of x and the gaps, keeping enough orders to see the TRUE requirement.

For f(t)=t^d (leading behavior; lower terms are even smaller corrections), expand Q in 1/x.
Q = v^2 c_m - u w c_{m+2}, window x,x+a,x+a+b,x+a+b+e.
We found leading term d^2(b^2-ae) x^{3d-2}. Get the NEXT term to see the correction sign/size,
and the exact condition Q>0 for the monomial as a clean inequality.

Then: the question is whether b^2>ae (margin possibly ->1) plus x>>W suffices, by checking the
ratio (correction)/(leading) -> 0 and is controlled by W/x times a constant (not W^2/x or worse).
"""
from sympy import symbols, series, Poly, expand, factor, O, Rational, simplify, collect

x,a,b,e,d = symbols('x a b e d', positive=True)

# do it for symbolic small d to see pattern of first two terms; then argue general d.
for dd in [1,2,3,4,5,6]:
    F=lambda t: t**dd
    q0,q1,q2,q3=x,x+a,x+a+b,x+a+b+e
    u=F(q1)-F(q0); v=F(q2)-F(q1); w=F(q3)-F(q2)
    Q=expand(v**2*F(q0)-u*w*F(q2))
    pQ=Poly(Q,x)
    deg=pQ.degree()
    c_top=pQ.nth(deg)
    c_next=pQ.nth(deg-1)
    print(f"d={dd}: deg_x={deg}  lead={factor(c_top)}")
    print(f"        next-coeff (x^{deg-1}) = {factor(c_next)}")
    # ratio next/lead determines correction ~ (c_next/c_top)/x
    print(f"        (next/lead) = {factor(simplify(c_next/c_top))}")
    print()
