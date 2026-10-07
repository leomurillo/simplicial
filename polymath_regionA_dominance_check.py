"""
Tighten/verify the Region-A dominance step. We claim:
  For q>=60 and s in [-1, 1/2]:  -g2_edge(q,s) >= G(q) > 0,
where -g2_edge = A4(s) q^4 + A3(s) q^3 + A2(s) q^2 + A1(s) q + A0,
  A4=(2-s)^2(1-s), A3=(2-s)(s^2+11s-11), A2=-2(19s^2-42s+42), A1=341(2-s), A0=988? or -988?
Check the actual constant term of -g2_edge in s (q^0 coeff):
"""
from sympy import symbols, expand, Poly, factor, Rational, S, solve, diff
import sympy as sp
B,C,q,s=symbols('B C q s', real=True)
g2 = B**3 - B**2*C + 38*B**2 - 15*B*C + 341*B - 68*C + 988
g2e=expand(g2.subs(C,-q*B-q**2))
neg=expand(-g2e.subs(B,-2*q+s*q))   # -g2_edge in (q,s)
pq=Poly(neg,q)
print("-g2_edge as poly in q (coeffs in s):")
coeffs={}
for d,co in zip(range(pq.degree(),-1,-1),pq.all_coeffs()):
    coeffs[d]=factor(co)
    print(f"   q^{d}: {factor(co)}")
A0=coeffs[0]
print("\nConstant (q^0) coeff:", A0, " -> this is the A0 used in G(q). Should be a NUMBER.")

# Now verify pointwise: minimize -g2_edge over s in [-1,1/2] for fixed q, and check >0 for q>=60.
# Since for each fixed q it's a quartic-in-s? No: -g2_edge is degree 3 in s (from A4 having s^... let's see deg in s)
print("\ndegree of -g2_edge in s:", Poly(neg,s).degree())
# Just verify numerically on a grid q=60..2000, s in[-1,1/2], min>0; AND that G(q) lower-bounds it.
import numpy as np
negf=sp.lambdify((q,s),neg,'numpy')
A4mn=S(9)/8; A3a=63; A2a=206; A1a=1023; A0a=988
Gf=lambda qq: float(A4mn)*qq**4-A3a*qq**3-A2a*qq**2-A1a*qq-A0a
worst=None;bad=False
for qq in np.linspace(60,5000,400):
    ss=np.linspace(-1,0.5,300)
    vals=negf(qq,ss)
    m=vals.min()
    g=Gf(qq)
    if m< g-1e-6:   # G should be a LOWER bound
        bad=True
    if worst is None or m<worst[0]:
        worst=(m,qq,ss[np.argmin(vals)])
    if m<=0:
        print("  NEG -g2_edge at q=",qq,"min=",m); bad=True
print("\n  min over grid of -g2_edge (q>=60, s in[-1,1/2]):", worst[0], "at q=",worst[1],"s=",worst[2])
print("  G(q) is a valid lower bound everywhere:", not bad)
print("  -g2_edge>0 for all q>=60, s in[-1,1/2]:", worst[0]>0)
# also confirm at exactly q=60: G(60)
print("  G(60)=",Gf(60), " G(59)=",Gf(59))
