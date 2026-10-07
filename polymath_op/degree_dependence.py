"""
Understand how the trigger ratio  R(window,f) := v^2 c_m / (u w c_{m+2})
depends on the DEGREE d of f, for a fixed window of primes.
Trigger Q>0  <=>  R>1.

For f(p)=p^d (pure monomial, the extreme high-degree behavior), on window (q0,q1,q2,q3):
  R = (q2^d-q1^d)^2 q0^d / [ (q1^d-q0^d)(q3^d-q2^d) q2^d ].
As d->oo this ->  (q2/q2)^{...}? Let's compute the d->oo limit and the d=1 value,
and check monotonicity in d. If R>1 for d=1 AND d->oo (and ideally all d), the window
is universal for pure monomials; general f is a positive combo and needs separate care.
"""
from sympy import primerange, Integer, Rational, Symbol, limit, oo, simplify, nsimplify

P=list(primerange(2,2000))

def R_monomial(window,d):
    q0,q1,q2,q3=[Integer(x) for x in window]
    num=(q2**d-q1**d)**2*q0**d
    den=(q1**d-q0**d)*(q3**d-q2**d)*q2**d
    return Rational(num,den)

def window(m): return (P[m-1],P[m],P[m+1],P[m+2])

# d->oo limit: dominated by largest prime powers.
# (q2^d-q1^d) ~ q2^d, (q1^d-q0^d)~q1^d, (q3^d-q2^d)~q3^d.
# R ~ q2^{2d} q0^d / (q1^d q3^d q2^d) = q0^d q2^d/(q1^d q3^d) = (q0 q2/(q1 q3))^d -> 0 since q0q2<q1q3.
# So for pure monomial, HIGH degree KILLS the trigger (R->0)! Important.
print("Pure monomial R=v^2 c_m/(u w c_m+2) for window vs degree d:")
for mlab,m in [("m=3",3),("m=15",15),("m=17",17),("m=43",43),("m=33",33)]:
    w=window(m)
    print(f"\n {mlab} window={w} gaps={(w[1]-w[0],w[2]-w[1],w[3]-w[2])}")
    for d in [1,2,3,4,5,8,12,20]:
        R=R_monomial(w,d)
        print(f"    d={d:3d}: R={float(R):.4f}  {'TRIGGER' if R>1 else ''}")
