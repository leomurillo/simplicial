"""
The 3x3 principal minor on index set {2,3,4}: M234 = det of submatrix H[{2,3,4},{2,3,4}]
where H[i][j]=b_{i+j}. Entries:
  i,j in {2,3,4}:  b_{i+j} for i+j in {4,5,6,7,8}.
  Row i=2: b4 b5 b6 ; row 3: b5 b6 b7 ; row 4: b6 b7 b8.
This is itself a Hankel(b4,b5,b6,b7,b8). Its sign: factor out b? Let's just compute symbolically.
Compare to D_4 (5x5). Also compute the W-reduced sign version.
"""
from sympy import primerange, Matrix, Integer, symbols, factor, expand, Poly, simplify
import sympy as sp

P=list(primerange(2,100))
B,C=symbols('B C', real=True)
def f(p): return p*p+B*p+C
def bn(L):
    b=[Integer(1)];a=Integer(1)
    for i in range(1,L): a*=f(P[i-1]); b.append(a)
    return b

b=bn(10)   # b0..b9
# M234 = det Hankel(b4..b8)
M=Matrix(3,3,lambda i,j: b[4+i+j])
print("Computing M234 = det H[{2,3,4}] (3x3 minor)...")
M234=factor(M.det())
print("\nM234 FACTORED =")
print(M234)

# sign-reduced: M234 = (b2*b3*b4)^2 / ... no. Factor b_i out of each ROW i (i=2,3,4):
# row i has entries b_{i+2},b_{i+3},b_{i+4}. b_{i+k}=b_i * prod_{l=i+1}^{i+k} c_l. So b_i factors from row i.
# det = b2 b3 b4 * det[ prod_{l=i+1}^{i+j+... } ]. Let's just confirm sign factorization numerically later.
# Save
with open(r"C:\Projects\simplicial\M234_factored.txt","w") as fh:
    fh.write(str(M234)+"\n")
print("\n(saved M234_factored.txt)")

# Also: factor structure. Pull common factors:
print("\nFactors of M234:")
for fac in sp.factor_list(M.det())[1]:
    print("   ", fac)
