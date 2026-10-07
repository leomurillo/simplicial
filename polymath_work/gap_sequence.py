"""
Understand the gap sequence g_l = f(p_{l+1}) - f(p_l) and whether the recursion
det W_N(c) ~ c1^d * D_{N-1}(gaps) gives a true induction.

PROBLEM: the actual sequence has NO free shift parameter; f is fixed. The leading-c1
identity tells us about f(p)+M for M->infty, not about a single fixed f.

BUT there's a cleaner exact statement. Let me reconsider.

The REAL question: for fixed monic f, is (b_n) non-moment? We have sign(D_N)=sign(det W_N).
det W_2 = c3 g1 g3 - c1 g2^2  where c_l=f(p_l), g_l = f(p_{l+1})-f(p_l).

For monic f deg d, by MVT: g_l = f(p_{l+1})-f(p_l) = f'(xi_l)(p_{l+1}-p_l) for some xi_l in (p_l,p_{l+1}).
f' ~ d * x^{d-1} increasing. The prime GAPS (p_{l+1}-p_l) are irregular.

Let me just TABULATE for many monic f the actual g-sequence and the gap-Hankel det,
and check the N=2 criterion c1 g2^2 > c3 g1 g3 numerically/exactly.

Actually the most promising RIGOROUS route: find an N (depending on f or universal) and
SPECIFIC small index window where det W_N < 0 is FORCED by a prime-gap inequality that
holds for the actual primes 2,3,5,7,11,13,17,19,23,... and provably fails for AP.

Let me compute, for the first primes, the gap sequence and its iterated gaps, and the
Hankel determinants of f(p_l) for a battery of monic f, recording first-failure N* and
WHICH principal minor (not nec leading) is negative.
"""
from sympy import primerange, Matrix, Integer
import itertools

P = list(primerange(2, 2000))

def bn(ff, L):
    b=[Integer(1)]; a=Integer(1)
    for i in range(1, L):
        a *= ff(P[i-1]); b.append(a)
    return b

def hankel(ff, N):
    b = bn(ff, 2*N+2)
    return Matrix(N+1, N+1, lambda i,j: b[i+j])

def first_fail_leading(ff, Nmax=8):
    for N in range(1, Nmax+1):
        d = hankel(ff, N).det()
        if d < 0:
            return N, d
    return None, None

def first_fail_anyminor(ff, Nmax=8):
    # build the largest Hankel and test ALL principal minors
    b = bn(ff, 2*Nmax+2)
    Hfull = Matrix(Nmax+1, Nmax+1, lambda i,j: b[i+j])
    best = None
    for k in range(2, Nmax+2):
        for idx in itertools.combinations(range(Nmax+1), k):
            sub = Hfull[idx, idx]
            d = sub.det()
            if d < 0:
                return idx, d
    return None, None

# Battery of monic f
tests = {
  "p (deg1,c=0)": lambda p: p,
  "p+1": lambda p: p+1,
  "p+2": lambda p: p+2,
  "p+10": lambda p: p+10,
  "p+10^6": lambda p: p+1000000,
  "p^2": lambda p: p**2,
  "p^2+1": lambda p: p**2+1,
  "p^2+10^6": lambda p: p**2+1000000,
  "p^3+1": lambda p: p**3+1,
  "p^3-p+5": lambda p: p**3-p+5,
  "p^4+1": lambda p: p**4+1,
  "p^5+1": lambda p: p**5+1,
  "p^2+p+1": lambda p: p**2+p+1,
  "(p-1)(p+1)+2 = p^2+1": lambda p: (p-1)*(p+1)+2,
}
print(f"{'f':22s} {'N*_leading':>10s} {'D_N*':>16s}")
for name, ff in tests.items():
    N, d = first_fail_leading(ff, 7)
    print(f"{name:22s} {str(N):>10s} {str(d):>16s}")
