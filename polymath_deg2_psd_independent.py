"""
Independent confirmation for degree 2: a negative principal minor => Hankel NOT PSD =>
not a Hamburger moment sequence. Verify via EIGENVALUES (exact char poly sign / numpy) that
the relevant Hankel block has a negative eigenvalue at representative points of each region.
Also confirm the logical reduction: PSD <=> all principal minors >=0 (standard).
"""
from sympy import primerange, Matrix, Integer, Rational
import sympy as sp
import numpy as np

P=list(primerange(2,2000))
def bn_num(Bv,Cv,L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=(P[i-1]**2+Bv*P[i-1]+Cv); b.append(a)
    return b

# Region A point and Region B point
tests=[("A: B=-6,C=10",(-6,Rational(10))),
       ("A: B=-20,C=100",(-20,Rational(100))),
       ("B: B=24/5,C=-27/2",(Rational(24,5),Rational(-27,2))),
       ("B: B=5,C=-13",(5,Rational(-13))),
       ("B: B=0,C=-3",(0,Rational(-3)))]
for lab,(Bv,Cv) in tests:
    # build a sufficiently large Hankel (size 6) and get min eigenvalue (float, scaled)
    b=bn_num(Bv,Cv,14)
    H=np.array([[float(b[i+j]) for j in range(7)] for i in range(7)])
    # scale to avoid overflow in eig: divide by geometric mean of diagonal
    d=np.sqrt(np.abs(np.diag(H)))
    Hs=H/np.outer(d,d)
    w=np.linalg.eigvalsh(Hs)
    print(f"{lab}: min eigenvalue of (scaled) 7x7 Hankel = {w.min():.4e}  ({'NEG => not PSD' if w.min()<0 else 'all>=0'})")
print("\nStandard fact: a real symmetric matrix is PSD iff ALL principal minors >=0 (Sylvester/")
print("the principal-minor criterion). One negative principal minor => not PSD => (b_n) not a")
print("Hamburger moment sequence (Hamburger: moment seq <=> infinite Hankel PSD).")
