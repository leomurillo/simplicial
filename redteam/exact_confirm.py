"""EXACT confirmation of the p^256 / p^1024 suspects.
Leading-PSD via exact integer LDL pivots (fraction-free where possible).
Then, if leading survives, do a NON-LEADING minor scan (the real PSD test).
This is the make-or-break: exact arithmetic, no float."""
import sys
from sympy import primerange, Integer, Rational
P = list(primerange(2, 100000))

def bn_pow(r, d, L):
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*= (Integer(P[i-1])+r)**d; out.append(a)
    return out

def leading_first_fail_exact(b, Nmax):
    """Exact symmetric Gaussian elimination; report first negative/zero pivot.
    pivot_k > 0 for all k  <=>  all leading minors D_0..D_Nmax > 0."""
    n = Nmax+1
    A = [[Rational(b[i+j]) for j in range(n)] for i in range(n)]
    for k in range(n):
        piv = A[k][k]
        if piv <= 0:
            return (k, 'neg' if piv<0 else 'zero', piv)
        for i in range(k+1, n):
            if A[i][k] == 0:
                continue
            f = A[i][k] / piv
            row_k = A[k]
            row_i = A[i]
            for j in range(k, n):
                row_i[j] = row_i[j] - f*row_k[j]
    return None

if __name__ == "__main__":
    d = int(sys.argv[1]) if len(sys.argv)>1 else 256
    r = int(sys.argv[2]) if len(sys.argv)>2 else 0
    Nmax = int(sys.argv[3]) if len(sys.argv)>3 else 22
    print(f"EXACT leading-PSD: f=(p+{r})^{d}, Nmax={Nmax}")
    b = bn_pow(r, d, 2*Nmax+2)
    res = leading_first_fail_exact(b, Nmax)
    if res is None:
        print(f"  ALL leading minors D_0..D_{Nmax} > 0 (exact). LEADING-PSD HOLDS.")
        print("  -> Candidate: must now check NON-LEADING principal minors.")
    else:
        print(f"  First leading failure at N={res[0]} (pivot {res[1]}).")
