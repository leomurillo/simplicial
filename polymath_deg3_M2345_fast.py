"""
FAST degree-3 M2345 core: compute det, then DIVIDE by known f(p_k) factors (multiplicities
from the deg-2 block pattern for {2,3,4,5}: f(2)^4 f(3)^4 f(5)^4 f(7)^4 f(11)^3 f(13)^2 f(17)^1,
times constant). Avoid the expensive factor_list. Verify divisibility (remainder 0).
M2345 sign = (const sign)*(prod f(p_k)>0)*sign(core). const sign we get from leading behavior.
"""
import os; os.makedirs(r"C:\Projects\simplicial\polymath_certs",exist_ok=True)
from sympy import primerange, Matrix, Integer, symbols, factor, expand, cancel, Poly, div, simplify
import sympy as sp
PR=list(primerange(2,200))
B,C,E=symbols('B C E', real=True)
def f(x): return x**3+B*x**2+C*x+E
b=[Integer(1)];a=Integer(1)
for i in range(1,13): a*=f(PR[i-1]); b.append(a)
print("Building M2345 determinant (deg3)...")
M=Matrix(4,4,lambda i,j:b[4+i+j])
det=expand(M.det())
print("det computed, expanding done. #terms:", len(det.args) if det.is_Add else 1)

# Known factors and multiplicities for block {2,3,4,5}:
mult={2:4,3:4,5:4,7:4,11:3,13:2,17:1}
denom=Integer(1)
for pk,mk in mult.items():
    denom*= f(pk)**mk
denom=expand(denom)
# core = det / (const * denom). First divide polynomial det by denom:
q,r=sp.div(sp.Poly(det,B,C,E), sp.Poly(denom,B,C,E))
print("remainder after dividing det by prod f(p_k)^m:", r.as_expr()==0)
core_times_const = q.as_expr()
# core_times_const should be (constant)*core. Extract integer content:
cc=sp.factor_list(core_times_const)
print("\nconstant of (det/prod):", cc[0])
core=None
for fac,m in cc[1]:
    # any remaining f(p_k)? shouldn't be
    print(f"  factor^{m}: ({len(fac.args) if fac.is_Add else 1} terms)")
    if fac.is_Add and (len(fac.args)>3):
        core=fac
print("\nFull constant prefactor of M2345 (= const from div * any leftover):")
print("  det = [", cc[0], "] * (remaining factors) ; with denom=prod f(p_k)^m")
with open(r"C:\Projects\simplicial\polymath_certs\deg3_M2345_core.txt","w") as fh:
    fh.write("const(det/prod): "+str(cc[0])+"\n")
    fh.write("CORE:\n"+str(core)+"\n")
print("(saved)")
if core is not None:
    print("\nCORE degree in E:", sp.Poly(core,E).degree(),
          " in B:", sp.Poly(core,B).degree(), " in C:", sp.Poly(core,C).degree())
    print("CORE leading-E coeff:", factor(sp.Poly(core,E).all_coeffs()[0]))
