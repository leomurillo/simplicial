"""
The WINDOW quantity:  for a 4-term window (c_m, c_{m+1}, c_{m+2}, c_{m+3}):
   Q(m) := c_m*(c_{m+1}-c_{m+2})^2 + c_{m+2}*(c_m-c_{m+1})*(c_{m+3}-c_{m+2})
The 3x3 consecutive principal minor on rows {i,i+1,i+2} (m=2i+1) is < 0  <=>  Q(m) > 0.
[Note only ODD m = 2i+1 arise from consecutive minors; but ANY principal minor counts,
 and we'll also check whether non-consecutive index sets give EVEN m or other windows.]

Verify:
 (a) the identity Q(m) = (the bracket) matches the symbolic minor sign,
 (b) evaluate Q(m) for f(p)=p across windows and locate positivity.
"""
from sympy import symbols, Matrix, factor, simplify, Integer, primerange, expand

P = list(primerange(2, 5000))

def Qwin(c, m):
    """c is a 1-indexed accessor: c(l)=ratio at index l. window starting at m."""
    cm, cm1, cm2, cm3 = c(m), c(m+1), c(m+2), c(m+3)
    return cm*(cm1-cm2)**2 + cm2*(cm-cm1)*(cm3-cm2)

# symbolic check that minor {i,i+1,i+2} sign = -Q(2i+1)
Ncs = 16
cs = symbols(f'c1:{Ncs}', positive=True)
def bsym(n):
    r=Integer(1)
    for k in range(n): r*=cs[k]
    return r
def csym(l): return cs[l-1]  # 1-indexed
for i in range(0,3):
    idx=[i,i+1,i+2]
    M=Matrix(3,3,lambda r,cc: bsym(idx[r]+idx[cc]))
    det=M.det()
    m=2*i+1
    Q=Qwin(csym, m)
    # det should be -(positive prefactor)*Q. Check det/(-Q) is a positive monomial
    ratio=simplify(det/(-Q))
    print(f"  minor{{{i},{i+1},{i+2}}} / (-Q({m})) = {factor(ratio)}  (should be positive monomial in c's)")
print()

# Now numeric for f(p)=p: c_l = p_l
print("=== f(p)=p : Q(m) over windows (m=1..40). Q>0 => 3x3 minor negative => NON-MOMENT ===")
def cprime(l): return Integer(P[l-1])
anyneg_minor = []
for m in range(1, 45):
    q = Qwin(cprime, m)
    flag = "  <== Q>0 (minor NEG)" if q>0 else ""
    if m<=20 or q>0:
        print(f"  m={m:3d}  window=({P[m-1]},{P[m]},{P[m+1]},{P[m+2]})  Q={q}{flag}")
    if q>0 and m%2==1:
        anyneg_minor.append(m)
print("\n odd m (=2i+1) with Q>0 (=> consecutive 3x3 principal minor {i,i+1,i+2} < 0):", anyneg_minor)
