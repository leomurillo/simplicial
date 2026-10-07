"""
DEGREE 3: monic f(p)=p^3 + B p^2 + C p + E, with f(p)>0 for all primes p (3 params B,C,E).
Step 1: positivity / binding analysis.  f(p)-f(2) = (p^3-8)+B(p^2-4)+C(p-2)
   = (p-2)[ p^2+2p+4 + B(p+2) + C ].  For prime p>=3: p-2>=1>0, and the bracket
   = p^2+2p+4 + B(p+2)+C. Whether 2 binds depends on B,C now (not just a line). Map it.
Step 2: D_2(B,C,E), det W_2, and M234 symbolic factorization.
"""
from sympy import primerange, Matrix, Integer, symbols, factor, expand, simplify, Poly
import sympy as sp

PR=list(primerange(2,100))
B,C,E,p=symbols('B C E p', real=True)
def f(x): return x**3 + B*x**2 + C*x + E
def bn(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(PR[i-1]); b.append(a)
    return b
b=bn(12)

print("f(p)-f(2) factored:", factor(expand(f(p)-f(2))))

print("\n=== D_2 (full) ===")
D2=Matrix(3,3,lambda i,j:b[i+j]).det()
print("D_2 =", factor(D2))

# det W_2 sign-reduced:
def Wdet(N):
    def c(l): return f(PR[l-1])
    def entry(i,j):
        pr=Integer(1)
        for l in range(i+1,i+j+1): pr*=c(l)
        return pr
    return Matrix(N+1,N+1,entry).det()
print("\n=== det W_2 (sign of D_2) ===")
W2=factor(expand(Wdet(2)))
print("det W_2 =", W2)
