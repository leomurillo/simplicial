"""
Degree 3: M234 (3x3 minor on {2,3,4}) symbolic factorization.
Hope: M234 = const * prod f(p_k)^{m_k} * Psi3(B,C,E) with Psi3 simpler (linear in E?).
"""
from sympy import primerange, Matrix, Integer, symbols, factor, expand, simplify, Poly
import sympy as sp

PR=list(primerange(2,100))
B,C,E=symbols('B C E', real=True)
def f(x): return x**3 + B*x**2 + C*x + E
def bn(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(PR[i-1]); b.append(a)
    return b
b=bn(12)
print("Computing M234 for cubic...")
M234=Matrix(3,3,lambda i,j:b[4+i+j]).det()
fl=sp.factor_list(M234)
print("constant:", fl[0])
nontrivial=[]
for fac,m in fl[1]:
    # identify f(p_k) factors
    print(f"  factor^{m}: {fac}")
    nontrivial.append((fac,m))
# Save big factor
with open(r"C:\Projects\simplicial\polymath_certs\deg3_M234.txt","w") as fh:
    fh.write("constant: "+str(fl[0])+"\n")
    for fac,m in fl[1]:
        fh.write(f"factor^{m}: {fac}\n")
print("\n(saved deg3_M234.txt)")

# Identify which factors are f(p_k):
print("\nIdentify f(p_k) among factors:")
for pk in [2,3,5,7,11,13]:
    fk=expand(f(pk))
    print(f"  f({pk}) = {fk}")
