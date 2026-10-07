"""
CORRECT factoring of contiguous 3x3 Hankel minor on indices {i,i+1,i+2}.

H_{rc} = b_{r+c}. Minor rows/cols i,i+1,i+2:
  [[b_{2i},   b_{2i+1}, b_{2i+2}],
   [b_{2i+1}, b_{2i+2}, b_{2i+3}],
   [b_{2i+2}, b_{2i+3}, b_{2i+4}]]
Row r (r=i,i+1,i+2): entries b_{r+i},b_{r+i+1},b_{r+i+2}. Factor b_{r+i} from row r:
  Row i: b_{2i}*(1, c_{2i+1}, c_{2i+1}c_{2i+2})
  Row i+1: b_{2i+1}*(1, c_{2i+2}, c_{2i+2}c_{2i+3})
  Row i+2: b_{2i+2}*(1, c_{2i+3}, c_{2i+3}c_{2i+4})
So M_i = b_{2i} b_{2i+1} b_{2i+2} * det V, where V is the W2-type matrix but with
ratio INDICES starting at 2i+1 and STEP... rows use c_{2i+1.. }, c_{2i+2..}, c_{2i+3..}.
The ROW index advances the starting ratio by 1, but the GAP between rows is: row i starts
ratio 2i+1, row i+1 starts ratio 2i+2 -- consecutive. SAME as before but window start = 2i+1!
Wait, but row i FIRST col is b_{2i} (=index 2i), and we factor b_{r+i}. For r=i that's b_{2i}.
Row i col j -> b_{2i+j}, /b_{2i} = prod_{l=2i+1}^{2i+j} c_l. Good.
Row i+1 col j -> b_{2i+1+j}, /b_{2i+1} = prod_{l=2i+2}^{2i+1+j} c_l.
Row i+2 col j -> b_{2i+2+j}, /b_{2i+2} = prod_{l=2i+3}^{2i+2+j} c_l.
So V row r (r=0,1,2): (1, c_{2i+1+r}, c_{2i+1+r} c_{2i+2+r}).
=> V = W2-type with window starting at s=2i+1. So sign(M_i)=sign(det W2 at window s=2i+1)!
NOT s=i+1. THAT was my bug -- the window start is 2i+1, not i+1.

So contiguous 3x3 minor at offset i  <=>  shifted det W2 starting at ratio index s=2i+1.
=> Psi(s=2i+1) = c_{s+2} g_s g_{s+2} - c_s g_{s+1}^2  with s=2i+1.

Let me re-verify.
"""
from sympy import primerange, Matrix, Integer

P = list(primerange(2, 20000))

def make_b(ff, L):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a *= ff(P[i-1]); b.append(a)
    return b

def contiguous_minor3(ff, i):
    b = make_b(ff, 2*i+5+2)
    M = Matrix(3,3, lambda r,c: b[(i+r)+(i+c)])
    return M.det()

def Psi(ff, s):
    def c(l): return Integer(ff(P[l-1]))
    cs, cs1, cs2, cs3 = c(s), c(s+1), c(s+2), c(s+3)
    gs = cs1-cs; gs1=cs2-cs1; gs2=cs3-cs2
    return cs2*gs*gs2 - cs*gs1**2

def sgn(x):
    x=int(x); return (x>0)-(x<0)

tests = {
  "p": lambda p: p, "p+1": lambda p: p+1, "p+5": lambda p:p+5,
  "p^2": lambda p: p**2, "p^2+1": lambda p: p**2+1,
  "p^3+1": lambda p: p**3+1, "p^4+1": lambda p: p**4+1, "p^5+1": lambda p:p**5+1,
}
print("Verify sign(contiguous 3x3 minor M_i) == sign(Psi(s=2i+1)):")
allok=True
for name, ff in tests.items():
    for i in range(0, 12):
        m = contiguous_minor3(ff, i)
        ps = Psi(ff, 2*i+1)
        if sgn(m) != sgn(ps):
            print(f"  {name}: MISMATCH i={i} s={2*i+1}: sgn M={sgn(m)} sgn Psi={sgn(ps)}")
            allok=False
print("ALL MATCH" if allok else "had mismatches")
