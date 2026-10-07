"""
Check: in the binding-2 region (relevant for M234 closure), is coeffE>0 (so Psi3 increasing in E)?
coeffE = 912B^2+60BC+41340B+C^2+1342C+474285, min -256 at (B,C)=(-45,679).
The negativity ellipse is around B=-45. Binding-2 region has B>-8 (Q_3 etc). Is the ellipse
disjoint from binding-2 region? Find where coeffE<=0 and check its B-range.
"""
from sympy import symbols, solve, S, Rational, hessian, factor
import sympy as sp
import numpy as np
B,C=symbols('B C', real=True)
coeffE = 912*B**2 + 60*B*C + 41340*B + C**2 + 1342*C + 474285
# coeffE<=0 region: ellipse. Its B-extent: for each B, min over C of coeffE = complete square in C.
# coeffE = C^2 + (60B+1342)C + (912B^2+41340B+474285)
# minC coeffE = (912B^2+41340B+474285) - (60B+1342)^2/4
minC = sp.expand((912*B**2+41340*B+474285) - (60*B+1342)**2/4)
print("min over C of coeffE (function of B):", factor(minC))
# coeffE can be <=0 only where minC<=0:
roots=solve(sp.Eq(minC,0),B)
print("B-range where ellipse exists (minC<=0):", [float(r) for r in roots if r.is_real])
print("=> coeffE<0 only for B in this range (around -45). Binding-2 region (B>-8) is DISJOINT.")
print("   minC at B=-8:", float(minC.subs(B,-8)), " at B=-5:", float(minC.subs(B,-5)), "(>0 => coeffE>0 there)")
print("   => On binding-2 region, coeffE>0 => Psi3 strictly increasing in E. M234 bulk argument valid.")
