"""
RIGOR: prove that for B > -5, f(p)=p^2+Bp+C>0 for ALL primes p  <=>  f(2)>0  (<=> C>-2B-4).
Equivalently: for B>-5, min over primes of f(p) is f(2).  i.e. f(2) <= f(p) for all primes p>=3.
f(p)-f(2) = (p^2-4) + B(p-2) = (p-2)(p+2) + B(p-2) = (p-2)(p+2+B).
For p>=3 prime: p-2>=1>0, and p+2+B >= 3+2+B = 5+B > 0 when B>-5.
=> f(p)-f(2) = (p-2)(p+2+B) > 0 for all primes p>=3 when B>-5.  PROVED (elementary).
Hence f(2) is the strict minimum, validity <=> f(2)>0 <=> C>-2B-4.

ALSO the boundary B=-5: f(p)-f(2)=(p-2)(p-3). For p=3 this is 0 (f(3)=f(2)); for p>=5 it's >0.
So at B=-5, min is f(2)=f(3); validity <=> f(2)>0 <=> C>6. B=-5 is in region A (B<=-5). Fine.

Symbolic confirmation:
"""
from sympy import symbols, factor, expand, primerange
import sympy as sp
B,C,p=symbols('B C p', real=True)
f=p**2+B*p+C
diff_p2 = factor(expand(f - f.subs(p,2)))
print("f(p) - f(2) =", diff_p2, "  = (p-2)(p+2+B)")
print("For prime p>=3 and B>-5: (p-2)>=1>0 and (p+2+B)>=(5+B)>0 => f(p)>f(2). Binding prime is 2.")
print()
# Region A binding for B<=-5: we used envelope; reconfirm that the envelope/binding analysis used
# only Bertrand + the per-piece N_q>=0. That part is independent. Here just CONFIRM the split point:
print("At B=-5: f(p)-f(2)=(p-2)(p-3); p=3 gives equality, p>=5 gives >0. min=f(2)=f(3). B=-5 in region A.")
print()
# Final: the two regions A (B<=-5) and B (B>-5) cover ALL real B. Each closed. QED structure.
print("Regions A: B<=-5 (D_2<0) and B: B>-5 (M234<0) partition R. Proof complete (modulo the")
print("two sub-lemmas: (A) N_q>=0 on pieces, (B) E2>0 on [-5,inf), both established).")
