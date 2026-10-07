"""
SHIFTED 3x3 PRINCIPAL MINORS.

The Hankel matrix H=(b_{i+j}). A principal 3x3 minor on rows/cols {i,i+1,i+2}
(contiguous) is det of [[b_{2i},b_{2i+1},b_{2i+2}],[b_{2i+1},b_{2i+2},b_{2i+3}],
[b_{2i+2},b_{2i+3},b_{2i+4}]]. Factoring out b_{2i},b_{2i+1}? Not directly Hankel of W,
but: the contiguous 3x3 minor starting at index i equals
   b_{2i} * b_{2i+1} * ... hmm let me just compute its sign via a 'shifted det W'.

Cleaner: For the contiguous principal minor M_i (3x3) of the Hankel matrix on indices
{i,i+1,i+2}, we have (by the same row-factoring b_i out of each row, but now rows are
i,i+1,i+2):
   M_i = b_i b_{i+1} b_{i+2} * det W2^{(i)}
where W2^{(i)} uses c_{i+1},...,c_{i+4} (the ratios shifted by i).
So sign(M_i) = sign( c_{i+3} g_{i+1} g_{i+3} - c_{i+1} g_{i+2}^2 )  [shifted N=2 form]
   where now c_l=f(p_l), g_l=c_{l+1}-c_l, and the window starts at l=i+1.

i.e. define for window start s (s>=1):
   Psi(s) = c_{s+2} g_s g_{s+2} - c_s g_{s+1}^2.
   Contiguous 3x3 minor at offset => sign = sign(Psi(s)). NEGATIVE => non-moment.

So: NON-MOMENT if EXISTS s>=1 with  c_s g_{s+1}^2 > c_{s+2} g_s g_{s+2}.
   ( <=> g_{s+1}^2 / (g_s g_{s+2})  >  c_{s+2}/c_s )

Let me VERIFY M_i = b_i b_{i+1} b_{i+2} * Psi(s=i+1)/(...) carefully and test across windows.
"""
from sympy import primerange, Matrix, Integer, symbols, expand, factor

P = list(primerange(2, 5000))

def make_b(ff, L):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a *= ff(P[i-1]); b.append(a)
    return b

def contiguous_minor3(ff, i):
    # rows/cols {i,i+1,i+2} of Hankel
    b = make_b(ff, 2*i+5+2)
    M = Matrix(3,3, lambda r,c: b[(i+r)+(i+c)])
    return M.det()

def Psi(ff, s):
    # window starting at prime index s: uses c_s..c_{s+2}, g_s,g_{s+1},g_{s+2}
    # c_l = f(p_l). g_l=c_{l+1}-c_l.
    def c(l): return Integer(ff(P[l-1]))
    cs, cs1, cs2, cs3 = c(s), c(s+1), c(s+2), c(s+3)
    gs = cs1-cs; gs1=cs2-cs1; gs2=cs3-cs2
    return cs2*gs*gs2 - cs*gs1**2   # sign matches det W2 shifted (= c_{s+2} g_s g_{s+2} - c_s g_{s+1}^2)

# Verify sign(contiguous_minor3 at i) == sign(Psi at s=i+1)
tests = {
  "p": lambda p: p,
  "p+1": lambda p: p+1,
  "p+5": lambda p:p+5,
  "p^2": lambda p: p**2,
  "p^2+1": lambda p: p**2+1,
  "p^3+1": lambda p: p**3+1,
  "p^4+1": lambda p: p**4+1,
}
print("Check sign(contiguous 3x3 minor M_i) == sign(Psi(s=i+1)) and find FIRST negative window:")
for name, ff in tests.items():
    found=False
    def sgn(x):
        x=int(x); return (x>0)-(x<0)
    for i in range(0, 15):
        m = contiguous_minor3(ff, i)
        ps = Psi(ff, i+1)
        if sgn(m) != sgn(ps):
            print(f"  {name}: SIGN MISMATCH at i={i}! M={m}, Psi={ps}")
        if m<0 and not found:
            print(f"  {name:8s}: first negative contiguous 3x3 minor at window i={i} (primes p_{i+1}..p_{i+4}), M_i={m}")
            found=True
    if not found:
        print(f"  {name:8s}: NO negative contiguous 3x3 minor in first 15 windows")
