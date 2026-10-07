"""
Precise characterization of the valid region V = {(B,C): p^2+Bp+C>0 for all primes p}.

Claim: for a MONIC quadratic h(x)=x^2+Bx+C, positivity at ALL primes is equivalent
to a finite condition. Vertex at x=-B/2, min value C - B^2/4.
- If -B/2 <= 2 (i.e. B >= -4): h is increasing on [2,oo) restricted to primes? Not exactly,
  but the minimum over primes is at the smallest prime >= vertex (and the prime just below).
- Rigorous finite reduction: h(p)>0 for all primes p  <=>  h(p)>0 for every prime p with
  p <= some bound. Since h(x)->+oo, only finitely many primes can be <=0. Precisely:
  h(p)>0 fails only if p lies strictly between the two real roots r- < r+ (if real).
  The roots are (-B +- sqrt(B^2-4C))/2. A prime violates positivity iff r- < p < r+.
  => V = { (B,C): no prime lies in the open root-interval }.
For the analysis we mainly need: the region is OPEN, and contains a neighborhood; we will
test the boundary curve C*(B) against it. Let's just MAP which primes are 'binding'.
"""
from sympy import symbols, primerange, Rational, sqrt, S, nsimplify
import sympy as sp
import numpy as np

P = list(primerange(2, 200))

# Numerically scan the (B,C) plane to visualize the valid region and the curve detW2=0.
def f(B,C,x): return x*x + B*x + C

def valid(B,C):
    for q in P:
        if f(B,C,q) <= 0:
            return False
    return True

def Cstar(B):
    return (B**3 + 38*B**2 + 341*B + 988)/(B**2 + 15*B + 68)

# For a grid of B, find the range of C that is valid, and compare to Cstar(B).
print(" B     Cmin_valid(approx)   Cstar(B)    valid@Cstar?   note")
for Bv in [-20,-15,-12,-10,-8,-6,-5,-4,-3,-2,-1,0,1,2,5,10,50,100,1000]:
    # smallest C (most negative allowed): we need NO prime in root interval.
    # Just scan C from high down to find min valid C on a fine grid.
    cs = float(Cstar(Bv))
    # find min valid C by scanning
    lo, hi = -1e7, 1e7
    # coarse: check validity at Cstar and around
    vс = valid(Bv, cs)
    # find approximate min valid C via bisection on "valid" predicate is not monotone-safe,
    # but validity in C IS monotone increasing: larger C => h larger => still positive. YES monotone.
    # So there is a threshold Cmin(B): valid iff C > Cmin(B) (strict).
    a, b = -1e8, 1e8
    for _ in range(200):
        m = (a+b)/2
        if valid(Bv, m):
            b = m
        else:
            a = m
    Cmin = b
    print(f"{Bv:6} {Cmin:18.4f} {cs:14.4f}    {str(vс):5}    Cstar-Cmin={cs-Cmin:.3f}")
