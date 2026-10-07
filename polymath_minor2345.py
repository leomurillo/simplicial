"""
Compute the 4x4 principal minor on {2,3,4,5} for BOTH deg2 and deg3, factor, pull out f(p_k).
M2345 uses b_{i+j} for i,j in {2,3,4,5}, i.e. b_4..b_10 (needs primes up to p_10=29).
By row-factoring (b_i out of row i), sign(M2345) = sign of a reduced poly. Let's just factor_list.
"""
from sympy import primerange, Matrix, Integer, symbols, factor, expand, simplify
import sympy as sp
PR=list(primerange(2,200))

def analyze(degree, label):
    if degree==2:
        B,C=symbols('B C', real=True); params=(B,C)
        def f(x): return x*x+B*x+C
    else:
        B,C,E=symbols('B C E', real=True); params=(B,C,E)
        def f(x): return x**3+B*x**2+C*x+E
    b=[Integer(1)];a=Integer(1)
    for i in range(1,13): a*=f(PR[i-1]); b.append(a)   # b0..b12 (need up to b10)
    M=Matrix(4,4,lambda i,j: b[4+i+j])   # indices {2,3,4,5} -> b_{4..10}
    print(f"\n===== {label}: M2345 (4x4 on {{2,3,4,5}}) =====")
    fl=sp.factor_list(M.det())
    print("constant:", fl[0])
    core=None
    for fac,m in fl[1]:
        # detect f(p_k) factors
        isfk=None
        for pk in [2,3,5,7,11,13,17,19,23,29]:
            if expand(fac-f(pk))==0 or expand(fac+f(pk))==0:
                isfk=pk; break
        tag=f"  [= f({isfk})]" if isfk else "  [CORE]"
        nterms = len(fac.args) if fac.is_Add else 1
        print(f"  factor^{m} ({nterms} terms){tag}: {fac if (not fac.is_Add or nterms<=8) else '(<<'+str(nterms)+' terms, saved>>)'}")
        if isfk is None:
            core=fac
    return core

c2=analyze(2,"DEGREE 2")
import os; os.makedirs(r"C:\Projects\simplicial\polymath_certs",exist_ok=True)
if c2 is not None:
    with open(r"C:\Projects\simplicial\polymath_certs\deg2_M2345_core.txt","w") as fh:
        fh.write(str(factor(c2)))
print("\n(deg2 core saved)")
