"""
Rewrite Q(m) in gap variables to expose WHY it goes positive, and to find
a universal trigger valid for every polynomial f.

Q = c_m*(c_{m+1}-c_{m+2})^2 + c_{m+2}*(c_m-c_{m+1})*(c_{m+3}-c_{m+2})

Let A=c_m, B=c_{m+1}, C=c_{m+2}, Dd=c_{m+3}.
Q = A*(B-C)^2 + C*(A-B)*(Dd-C).

Try gap variables:
  u = B - A  (gap 1)
  v = C - B  (gap 2)
  w = Dd - C (gap 3)
So B=A+u, C=A+u+v, Dd=A+u+v+w.
"""
from sympy import symbols, expand, factor, collect, simplify, Integer

A,u,v,w = symbols('A u v w', real=True)
B = A+u
C = A+u+v
Dd = A+u+v+w
Q = A*(B-C)**2 + C*(A-B)*(Dd-C)
Qe = expand(Q)
print("Q in (A,u,v,w):", Qe)
print()
print("collect on A:", collect(Qe, A))
print()
# coefficient of A and constant part
print("As poly in A:")
from sympy import Poly
pa = Poly(Qe, A)
for (deg,), coeff in pa.terms():
    print(f"   A^{deg} : {factor(coeff)}")
print()

# So Q is LINEAR in A (the base value c_m).
# Q = A * [coeff] + [const]. If coeff>0 and A large => Q>0.
# coeff of A^1:
c1coeff = pa.coeff_monomial(A)
c0coeff = pa.coeff_monomial(1)
print("coeff of A (linear):", expand(c1coeff), "=", factor(c1coeff))
print("coeff A^0 (const):", expand(c0coeff), "=", factor(c0coeff))
print()
# The A-coefficient: this drives sign for large base value.
print(">>> Q = A*(", factor(c1coeff), ") + (", factor(c0coeff), ")")
