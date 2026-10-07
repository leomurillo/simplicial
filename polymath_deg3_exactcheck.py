"""
Exact-arithmetic spot check of degree-3 grid findings: take several (B,C,E) (rational),
confirm validity and the first-negative leading minor with EXACT sympy determinants
(guards against float slogdet artifacts). Include an N*=4 case and an N*=1 case.
"""
from sympy import primerange, Matrix, Integer, Rational
import sympy as sp

P=list(primerange(2,3000))
def valid(Bv,Cv,Ev):
    return all(P[i]**3+Bv*P[i]**2+Cv*P[i]+Ev>0 for i in range(150))
def first_neg_exact(Bv,Cv,Ev,Nmax=8):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,2*Nmax+2):
        pp=P[i-1]; a*=(pp**3+Bv*pp**2+Cv*pp+Ev); b.append(a)
    signs=[]
    firstneg=None
    for N in range(1,Nmax+1):
        d=Matrix(N+1,N+1,lambda i,j:b[i+j]).det()
        signs.append('+' if d>0 else ('-' if d<0 else '0'))
        if d<0 and firstneg is None: firstneg=N
    return firstneg, signs

tests=[
    (Rational(-2385,100),Rational(17949,100),Rational(-27158,100)),  # the N*=4 max case
    (-24,180,-272),
    (0,0,Rational(1,1)),       # f(p)=p^3+1, all positive, simple
    (0,0,1000000),             # big additive constant
    (5,-30,Rational(1,2)),
    (-10,20,Rational(1,1)),
    (3,3,3),
    (-5,10,Rational(1,1)),
]
for Bv,Cv,Ev in tests:
    v=valid(Bv,Cv,Ev)
    if not v:
        print(f"B={Bv},C={Cv},E={Ev}: NOT VALID (skip)"); continue
    fn,signs=first_neg_exact(Bv,Cv,Ev,8)
    print(f"B={Bv}, C={Cv}, E={Ev}: valid; leading-minor signs D_1..D_8 = {signs}; first neg N*={fn}")
