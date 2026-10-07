"""
RIGOROUS sufficient condition. For monic f of degree d>=1 with f>0 on primes:
At a window q1<q2<q3<q4, define
   u=f(q2)/f(q1), v=f(q3)/f(q2), s=f(q4)/f(q3); a=u-1,b=v-1,e=s-1 (all >0 if f increasing).
   minor M_{r,r+1,r+2} < 0  <=>  R := a e - b^2 + a b e (2+b) < 0.

Strategy 'TWIN-SPIKE-TWIN': pick q1,q2 twin (q2=q1+2), q3,q4 twin (q4=q3+2), middle gap big.
Then bound:
  a = f(q1+2)/f(q1) - 1.  For monic f deg d, f increasing on [q1,inf) once q1 >= some bound.
     KEY BOUND: for x>0 large, f(x+2)/f(x) <= (something). Use f(x)=x^d * h(x), h->1.
  Actually cleanest: take f(x)=x^d as the EXTREMAL case and PROVE x^d is the worst (max R) at
  a twin-spike window among all monic f of degree d. Then reduce to a pure prime inequality.

Here: numerically test the claim 'x^d maximizes R over monic-deg-d at twin-spike windows'.
If TRUE, the whole problem reduces to: for x^d, exhibit a twin-spike window with R<0,
i.e. a pure statement about primes + the exponent d.
"""
from sympy import primerange, Integer, Rational
import random

P = list(primerange(2, 50_000_000))
Pset=set(P)

def Rgen(coeffs,q1,q2,q3,q4):
    def f(x):
        v=Integer(0)
        for cf in coeffs: v=v*x+cf
        return v
    u=Rational(f(q2),f(q1)); v=Rational(f(q3),f(q2)); s=Rational(f(q4),f(q3))
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

def Rxd(d,q1,q2,q3,q4):
    u=Rational(q2,q1)**d; v=Rational(q3,q2)**d; s=Rational(q4,q3)**d
    a=u-1;b=v-1;e=s-1
    return a*e-b**2+2*a*b*e+a*b**2*e

# Test: is x^d the worst (largest R)? Compare R(x^d) to R(monic deg-d random) at fixed windows.
random.seed(11)
# pick a few twin-spike windows
windows=[(6947,6949,6959,6961),(8969,8971,8999,9001),(9437,9439,9461,9463)]
print("=== Is x^d the MAX of R over monic deg-d? (R(x^d) should be >= R(other monic)) ===")
viol=0; checks=0
for (q1,q2,q3,q4) in windows:
    for d in [2,3,4,5,8,12]:
        Rbase=Rxd(d,q1,q2,q3,q4)
        for _ in range(60):
            coeffs=[Integer(1)]+[Integer(random.randint(-d*3, d*5)) for _ in range(d)]
            # ensure positive on the 4 primes
            def f(x,cc=coeffs):
                vv=Integer(0)
                for c_ in cc: vv=vv*x+c_
                return vv
            if min(f(q1),f(q2),f(q3),f(q4))<=0: continue
            # also need increasing (a,b,e>0): require f(q1)<f(q2)<f(q3)<f(q4)
            if not (f(q1)<f(q2)<f(q3)<f(q4)): continue
            Rg=Rgen(coeffs,q1,q2,q3,q4)
            checks+=1
            if Rg > Rbase:   # other monic has LARGER R than x^d -> x^d not the max
                viol+=1
                if viol<=10:
                    print(f"  VIOLATION window=({q1},{q2},{q3},{q4}) d={d}: R(other)={float(Rg):.4e} > R(x^d)={float(Rbase):.4e}, coeffs={coeffs}")
print(f"checks={checks}, violations(x^d not max)={viol}")

# Also directly: does R(x^d)<0 at these twin-spike windows for the relevant d-range?
print("\n=== R(x^d)<0 at twin-spike windows ===")
for (q1,q2,q3,q4) in windows:
    bad=[d for d in [1,2,5,10,50,100,500,1000] if Rxd(d,q1,q2,q3,q4)>=0]
    print(f"  ({q1},{q2},{q3},{q4}): d with R>=0 among sample: {bad}")
