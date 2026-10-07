"""
Degree 3: M2345 (4x4 on {2,3,4,5}) factorization, isolate the CORE polynomial.
sign(M2345) = (sign const)*(prod f(p_k)^m)*sign(CORE). On valid region f(p_k)>0, so
sign(M2345) = sign(const)*sign(CORE). We need M2345<0 on the deg-3 sliver => CORE has the right sign.
"""
import os; os.makedirs(r"C:\Projects\simplicial\polymath_certs",exist_ok=True)
from sympy import primerange, Matrix, Integer, symbols, factor, expand
import sympy as sp
PR=list(primerange(2,200))
B,C,E=symbols('B C E', real=True)
def f(x): return x**3+B*x**2+C*x+E
b=[Integer(1)];a=Integer(1)
for i in range(1,13): a*=f(PR[i-1]); b.append(a)
print("Computing deg-3 M2345 (4x4)...")
M=Matrix(4,4,lambda i,j:b[4+i+j])
fl=sp.factor_list(M.det())
print("constant:", fl[0])
core=None
for fac,m in fl[1]:
    isfk=None
    for pk in [2,3,5,7,11,13,17,19,23,29]:
        if expand(fac-f(pk))==0: isfk=pk;break
    if isfk: print(f"  factor^{m} = f({isfk})")
    else:
        core=fac
        nt=len(fac.args) if fac.is_Add else 1
        print(f"  factor^{m} = CORE ({nt} terms)")
with open(r"C:\Projects\simplicial\polymath_certs\deg3_M2345_core.txt","w") as fh:
    fh.write("constant: "+str(fl[0])+"\n")
    fh.write("CORE:\n"+str(core)+"\n")
print("(saved deg3_M2345_core.txt)")
# degree of core in E:
print("\nCORE degree in E:", sp.Poly(core,E).degree())
print("CORE degree in B:", sp.Poly(core,B).degree())
print("CORE degree in C:", sp.Poly(core,C).degree())
print("CORE coeff of highest E power:", factor(sp.Poly(core,E).all_coeffs()[0]))
