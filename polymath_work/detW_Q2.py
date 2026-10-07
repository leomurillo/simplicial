"""
Q2(u,v,w) = u v^2 w - u v^2 - v^2 w + 2 v - 1, sign(det W_2)=sign(Q2).
u = c2/c1, v = c3/c2, w = c4/c3.

We want Q2 < 0 for the prime/monic case, and Q2 >= 0 for AP case.

Let me see what Q2 looks like in terms of c's directly (divide d2 by c2*c3, say).
d2 = c3 c4 (c2-c1) - c2(c1 c2 - 2 c1 c3 + c3^2).
Divide by c1 c2 c3 (>0):
  d2/(c1 c2 c3) = c4(c2-c1)/(c1 c2) - (c1 c2 - 2 c1 c3 + c3^2)/(c1 c3)
"""
from sympy import symbols, simplify, factor, expand, Rational, collect, solve

u,v,w = symbols('u v w', positive=True)
Q2 = u*v**2*w - u*v**2 - v**2*w + 2*v - 1

# Collect by w:
print("Q2 collect w:", collect(expand(Q2), w))
# = w*(u v^2 - v^2) + (-u v^2 + 2 v - 1)
# = v^2 (u-1) w  - u v^2 + 2 v - 1
# Solve Q2 = 0 for w:
wsol = solve(Q2, w)
print("w solving Q2=0:", wsol)
# Q2 < 0  <=>  (for u>1, coefficient of w positive) w < w*(crit)
print()

# Now: what does the AP case give? c_i = a + b i (i index of c, i.e. c_l = a+b l).
# Actually established: AP in c is moment. AP means c_l = A + B l (l=1,2,3,...).
# Let's PARAMETRIZE c_l = A + B*l. Then:
A,B,l = symbols('A B l', positive=True)
c1ap = A + B*1
c2ap = A + B*2
c3ap = A + B*3
c4ap = A + B*4
uap = c2ap/c1ap; vap = c3ap/c2ap; wap = c4ap/c3ap
Q2ap = Q2.subs({u:uap, v:vap, w:wap})
Q2ap_s = simplify(Q2ap)
print("Q2 for AP c_l=A+B l:", Q2ap_s)
print("factor:", factor(Q2ap_s))
