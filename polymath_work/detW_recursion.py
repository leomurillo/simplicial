"""
RECURSIVE STRUCTURE DISCOVERY.

det W_2 = c3 g1 g3 - c1 g2^2.  Leading term in c1 (=c3 also ~c1+...):
  coefficient structure. Let me check: is [c1^3 coeff of det W_3] = -det of Hankel(gaps)?

Hankel of gaps G3 = [[g1,g2,g3],[g2,g3,g4],[g3,g4,g5]].
det G3 = g1(g3 g5 - g4^2) - g2(g2 g5 - g3 g4) + g3(g2 g4 - g3^2)
       = g1 g3 g5 - g1 g4^2 - g2^2 g5 + g2 g3 g4 + g2 g3 g4 - g3^3
       = g1 g3 g5 - g1 g4^2 - g2^2 g5 + 2 g2 g3 g4 - g3^3.
That's EXACTLY the c1^3 coefficient!  So [c1^3 coeff] = det(Hankel of gaps).

And for det W_2: leading in c1. det W_2 = c3 g1 g3 - c1 g2^2.
Write c3 = c1 + g1 + g2. Leading c1 coeff = g1 g3 - g2^2 = det[[g1,g2],[g2,g3]] = Hankel(gaps) 2x2!

THE PATTERN:  det W_N = c1^{?} * det(Hankel_N(gaps)) + lower order in c1.
  where Hankel_N(gaps) = (g_{i+j+1})_{0<=i,j<=N-1}  is the (N x N) Hankel of the GAP sequence.

So the LEADING coefficient (as c1->infty, i.e. huge additive constant) of sign(det W_N)
is the sign of D_{N-1}(gap sequence) = Hankel det of the gaps g_l!

=> If gaps g_l = c_{l+1}-c_l are themselves NON-MOMENT, det W_N flips negative for large c1.
This is a DESCENT / RECURSION: moment-ness of (c_l) at large additive shift is controlled
by moment-ness of the gap sequence (g_l), which is itself f(p_{l+1})-f(p_l) -- a polynomial-ish
of LOWER degree behavior! This explains 'large additive constant -> smaller N*'.

Let me VERIFY the leading-coefficient = Hankel(gaps) identity for N=2,3, and conjecture/verify N=4.
"""
from sympy import symbols, Matrix, factor, expand, Integer, Poly

def Wmat(N, c):
    def entry(i, j):
        p = Integer(1)
        for l in range(i+1, i+j+1):
            p *= c[l]
        return p
    return Matrix(N+1, N+1, entry)

def hankel_gaps(N, g):
    # N x N Hankel of gap sequence: (g_{i+j+1})_{0<=i,j<=N-1}
    return Matrix(N, N, lambda i,j: g[i+j+1])

for N in range(2,5):
    c1 = symbols('c1', positive=True)
    # gaps g1..g_{2N-1}
    gs = symbols('g1:%d' % (2*N))   # g1..g_{2N-1}
    g = {l: gs[l-1] for l in range(1, 2*N)}
    # c_l = c1 + sum_{k=1}^{l-1} g_k
    cdict = {}
    for l in range(1, 2*N+1):
        s = c1
        for k in range(1, l):
            s = s + g[k]
        cdict[l] = s
    W = Wmat(N, cdict)
    dW = expand(W.det())
    pol = Poly(dW, c1)
    topdeg = pol.degree()
    topcoef = factor(pol.nth(topdeg))
    Hg = hankel_gaps(N, g)
    detHg = factor(Hg.det())
    print(f"N={N}: top c1 degree = {topdeg}, top coeff = {topcoef}")
    print(f"       Hankel(gaps) {N}x{N} det = {detHg}")
    print(f"       MATCH (topcoef - detHg)==0 ? {expand(pol.nth(topdeg) - Hg.det())==0}")
    print()
