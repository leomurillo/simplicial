"""
Any 3x3 PRINCIPAL minor of the Hankel matrix (b_{i+j}) must be >=0 for a moment seq.
The principal minor on rows/cols {i,j,k} (i<j<k) of a Hankel matrix is:
  det [[b_{2i}, b_{i+j}, b_{i+k}],
       [b_{i+j}, b_{2j}, b_{j+k}],
       [b_{i+k}, b_{j+k}, b_{2k}]]
Factor out b_{2i},b_{2j},b_{2k}? No -- Hankel principal minors factor differently.
Let's compute the GENERAL 3x3 principal minor sign in terms of ratios and look
for the cleanest universal negativity.

Strategy: the simplest is the {0,1,2} minor = D_2. But maybe {0,1,k} or {i,i+1,i+2}
gives a cleaner gap condition. Compute symbolically.
"""
from sympy import symbols, Matrix, factor, simplify, expand, Integer, prod, collect

# Use a long symbolic ratio chain
N = 14
cs = symbols(f'c1:{N}', positive=True)  # c1..c13

def b(n):
    if n == 0: return Integer(1)
    r = Integer(1)
    for i in range(n): r *= cs[i]
    return r

def minor3(i, j, k):
    idx = [i, j, k]
    M = Matrix(3, 3, lambda r, c: b(idx[r]+idx[c]))
    return M.det()

# 2x2 principal minors first: rows {i,j}, det = b_{2i} b_{2j} - b_{i+j}^2
# = b_{i+j}^2 ( b_{2i}b_{2j}/b_{i+j}^2 - 1 ). For consecutive {i,i+1}:
# b_{2i} b_{2i+2} - b_{2i+1}^2 = b_{2i+1}^2( c_{2i+2}/c_{2i+1} - 1)... let's just see.
print("=== 2x2 consecutive principal minors {i,i+1} ===")
for i in range(0, 5):
    M = Matrix(2,2, lambda r,c: b([i,i+1][r]+[i,i+1][c]))
    d = factor(M.det())
    print(f"  {{{i},{i+1}}}: {d}")
print("  (sign>0 iff c_{2i+2}>c_{2i+1}, i.e. ratio increasing at that index)")
print()

print("=== 3x3 consecutive principal minors {i,i+1,i+2} (sign-carrying part) ===")
for i in range(0, 4):
    d = minor3(i, i+1, i+2)
    # factor out the common b power
    df = factor(d)
    print(f"  {{{i},{i+1},{i+2}}}:")
    print(f"     factored = {df}")
    print()
