"""
Asymptotic sign of R = s*v^2*(u-1) - (u*v^2 - 2v + 1) as window primes -> infinity.
Q>0  <=>  R<0.
Set u=1+a, v=1+b, s=1+e with a,b,e -> 0+ (consecutive prime ratios minus 1, raised to d).
Expand R to leading order.
"""
from sympy import symbols, series, expand, O, simplify, factor, Rational, collect

a,b,e = symbols('a b e', positive=True)
u=1+a; v=1+b; s=1+e
R = s*v**2*(u-1) - (u*v**2 - 2*v + 1)
Rex = expand(R)
print("R exact in (a,b,e):", Rex)
print("R factored:", factor(Rex))

# group by total degree
from sympy import Poly
# leading terms: collect by degree
terms = Rex.as_ordered_terms()
print("\nterms of R (a=u-1,b=v-1,e=s-1):")
for t in terms:
    print("   ", t)

# The constant and linear parts should vanish (R->0). Check:
R0 = Rex.subs({a:0,b:0,e:0})
print("\nR at a=b=e=0:", R0)
# linear part
from sympy import diff
print("dR/da at 0:", diff(Rex,a).subs({a:0,b:0,e:0}))
print("dR/db at 0:", diff(Rex,b).subs({a:0,b:0,e:0}))
print("dR/de at 0:", diff(Rex,e).subs({a:0,b:0,e:0}))

# quadratic part (Hessian-level). Extract degree-2 homogeneous part:
def homog_part(expr, vars, deg):
    p = Poly(expr, *vars)
    res = 0
    for monom, coeff in p.terms():
        if sum(monom)==deg:
            term=coeff
            for vi,pw in zip(vars,monom):
                term*= vi**pw
            res+=term
    return res

for d in range(0,5):
    hp = homog_part(Rex,[a,b,e],d)
    print(f"\ndegree-{d} part of R:", expand(hp))
