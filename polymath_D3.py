"""
Compute det W_3(B,C) symbolically for monic quadratic f(p)=p^2+Bp+C.
det W_3 is sign-equivalent to D_3. W_3 is 4x4. Entries W[i][j] = prod_{l=i+1}^{i+j} c_l,
c_l = f(P[l-1]), 1-indexed primes p_1=2,...,p_6=13 (need up to p_6 for 4x4 -> indices 0..3,
i+j up to 6 -> primes p_1..p_6 = 2,3,5,7,11,13).
"""
from sympy import primerange, Matrix, Integer, symbols, factor, expand, simplify, collect, Poly
import sympy as sp

P = list(primerange(2, 100))
B, C = symbols('B C', real=True)

def f(p): return p*p + B*p + C
def c(l): return f(P[l-1])   # 1-indexed

def Wdet(N):
    def entry(i,j):
        prod=Integer(1)
        for l in range(i+1, i+j+1):
            prod*=c(l)
        return prod
    return Matrix(N+1,N+1,entry).det()

print("Computing det W_3 (this may take a moment)...")
W3 = Wdet(3)
W3 = sp.expand(W3)
print("det W_3 (expanded) has", len(W3.args) if W3.is_Add else 1, "terms")
W3f = factor(W3)
print("\ndet W_3 FACTORED =")
print(W3f)
# Save
with open(r"C:\Projects\simplicial\W3_factored.txt","w") as fh:
    fh.write("det W_3 factored:\n")
    fh.write(str(W3f)+"\n\n")
    fh.write("det W_3 expanded:\n")
    fh.write(str(W3)+"\n")
print("\n(saved to W3_factored.txt)")
