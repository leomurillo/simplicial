"""Bareiss fraction-free elimination: exact integer arithmetic, no Rationals.
After Bareiss, the (k,k) entry equals the leading principal minor D_k (integer).
So we read off ALL leading minors D_0..D_N exactly and cheaply.
This is the fast exact engine for huge p^d entries."""
import sys
from sympy import primerange, Integer
P = list(primerange(2, 100000))

def bn_pow(r, d, L):
    out=[Integer(1)]; a=Integer(1)
    for i in range(1,L):
        a*= (Integer(P[i-1])+r)**d; out.append(a)
    return out

def leading_minors_bareiss(b, N):
    """Return list D_0..D_N of leading principal minors (exact ints) via Bareiss.
    M is (N+1)x(N+1) Hankel. Bareiss: after step k, M[k][k] = det of top-left (k+1)."""
    n = N+1
    M = [[b[i+j] for j in range(n)] for i in range(n)]
    dets = []
    prev = Integer(1)
    for k in range(n):
        # before eliminating, leading minor of size k+1 is current M[k][k] (Bareiss invariant)
        # Standard Bareiss: M[i][j] = (M[i][j]*M[k][k] - M[i][k]*M[k][j]) / prev
        # The pivot M[k][k] at this point already equals D_k.
        dets.append(M[k][k])
        if M[k][k] == 0:
            # zero pivot: leading block singular; fill remaining as None
            dets += [None]*(n-1-k)
            return dets
        pk = M[k][k]
        for i in range(k+1, n):
            Mik = M[i][k]
            for j in range(k+1, n):
                M[i][j] = (M[i][j]*pk - Mik*M[k][j]) // prev
            M[i][k] = Integer(0)
        prev = pk
    return dets

if __name__ == "__main__":
    d = int(sys.argv[1]); r = int(sys.argv[2]) if len(sys.argv)>2 else 0
    Nmax = int(sys.argv[3]) if len(sys.argv)>3 else 22
    b = bn_pow(r, d, 2*Nmax+2)
    dets = leading_minors_bareiss(b, Nmax)
    signs = ''.join('+' if (x is not None and x>0) else ('0' if x==0 else '-') for x in dets)
    print(f"f=(p+{r})^{d}, leading D_0..D_{Nmax} signs: {signs}")
    firstneg = next((i for i,x in enumerate(dets) if x is not None and x<0), None)
    firstzero = next((i for i,x in enumerate(dets) if x==0), None)
    print(f"  first leading NEGATIVE at N={firstneg}; first ZERO at N={firstzero}")
