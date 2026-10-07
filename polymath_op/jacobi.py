"""
Jacobi recurrence coefficients (a_n, lambda_n) for b_n = prod f(p_i).
lambda_n = D_{n-2} D_n / D_{n-1}^2  (D_{-1}=1, D_0=b_0=1)
A real measure (Hamburger moment) => lambda_n >= 0 for all n.
First n with lambda_n < 0  <=>  first D going negative.

We compute exactly via the monic orthogonal polynomial recurrence using
the moment-determined Hankel determinants, AND independently via the
Gram-Schmidt / Chebyshev algorithm to cross-check.
"""
from sympy import primerange, Matrix, Integer, Rational, nsimplify, factor, symbols

P = list(primerange(2, 4000))

def bn(f, L):
    b = [Integer(1)]; a = Integer(1)
    for i in range(1, L):
        a *= f(P[i-1]); b.append(a)
    return b

def hankel_dets(b, Nmax):
    """D_{-1}=1, D_N = det(b_{i+j})_{0..N}."""
    Ds = {-1: Integer(1)}
    for N in range(0, Nmax+1):
        Ds[N] = Matrix(N+1, N+1, lambda i, j: b[i+j]).det()
    return Ds

def jacobi_from_dets(Ds, Nmax):
    """lambda_n = D_{n-2} D_n / D_{n-1}^2 for n>=1."""
    lam = {}
    for n in range(1, Nmax+1):
        lam[n] = Rational(Ds[n-2]*Ds[n], Ds[n-1]**2)
    return lam

def jacobi_chebyshev(b, Nmax):
    """
    Exact a_n, lambda_n via the Chebyshev/modified-moment-free algorithm
    on monic orthogonal polynomials using inner products <x^i,x^j>=b_{i+j}.
    Build monic p_0=1, p_1=x-a_0, p_{n+1}=(x-a_n)p_n - lambda_n p_{n-1}.
    Represent polynomials by coefficient vectors; inner product via moments.
    Works as long as all <p_n,p_n> != 0 (i.e. D_{n-1}!=0).
    Returns (a, lam) where a indexed 0..Nmax-1, lam indexed 1..Nmax-1.
    """
    # need moments up to degree 2*Nmax
    def ip(u, v):
        # u,v coefficient lists (low to high). sum u_i v_j b_{i+j}
        s = Integer(0)
        for i, ui in enumerate(u):
            if ui == 0: continue
            for j, vj in enumerate(v):
                if vj == 0: continue
                s += ui*vj*b[i+j]
        return s
    def xmul(u):
        return [Integer(0)] + list(u)
    def axpy(u, alpha, v):
        # u - alpha*v  (lists possibly different length)
        m = max(len(u), len(v))
        u = list(u)+[Integer(0)]*(m-len(u))
        v = list(v)+[Integer(0)]*(m-len(v))
        return [u[k]-alpha*v[k] for k in range(m)]
    polys = []
    a = {}; lam = {}
    p_prev = None
    p_cur = [Integer(1)]  # p_0 = 1
    norm_cur = ip(p_cur, p_cur)  # = b_0 = 1
    norm_prev = None
    for n in range(0, Nmax):
        xp = xmul(p_cur)
        a[n] = Rational(ip(xp, p_cur), norm_cur)
        # p_{n+1} = x p_n - a_n p_n - lam_n p_{n-1}
        q = axpy(xp, a[n], p_cur)
        if p_prev is not None:
            lam[n] = Rational(norm_cur, norm_prev)  # lambda_n = ||p_n||^2/||p_{n-1}||^2
            q = axpy(q, lam[n], p_prev)
        p_prev, norm_prev = p_cur, norm_cur
        p_cur = q
        norm_cur = ip(p_cur, p_cur)
    # final lambda_{Nmax}
    if p_prev is not None:
        lam[Nmax] = Rational(norm_cur, norm_prev) if norm_prev != 0 else None
    return a, lam

def analyze(name, f, Nmax=9):
    print("="*70)
    print(f"f(p) = {name}")
    print("="*70)
    b = bn(f, 2*Nmax+3)
    print("  b_n =", [str(b[i]) if b[i] < 10**12 else f"~1e{len(str(b[i]))-1}" for i in range(min(8,len(b)))])
    print("  ratios c_i=f(p_i):", [f(P[i-1]) for i in range(1, min(10, Nmax+2))])
    Ds = hankel_dets(b, Nmax)
    lam_det = jacobi_from_dets(Ds, Nmax)
    a_cb, lam_cb = jacobi_chebyshev(b, Nmax)
    print("\n  n :  D_n                         lambda_n (det)        lambda_n (cheb)   sign")
    first_neg = None
    for n in range(0, Nmax+1):
        dn = Ds.get(n)
        ld = lam_det.get(n)
        lc = lam_cb.get(n)
        s = ""
        if ld is not None:
            s = "NEG <---" if ld < 0 else ("0" if ld==0 else "+")
            if ld < 0 and first_neg is None:
                first_neg = n
        match = "OK" if (ld is None or lc is None or ld==lc) else "MISMATCH!"
        dn_str = str(dn) if (dn is not None and abs(dn) < 10**15) else (f"~{'+' if dn>0 else '-'}1e{len(str(abs(dn)))-1}" if dn is not None else "")
        print(f"  {n} :  {dn_str:28s} {str(ld) if ld is not None else '':22s} {s:8s} {match}")
    print(f"\n  ==> FIRST lambda_n < 0 at n = {first_neg}  (=> first D_n<0 at N={first_neg})")
    print("\n  a_n (recurrence centers):")
    for n in sorted(a_cb):
        an = a_cb[n]
        print(f"    a_{n} = {an}   (~{float(an):.4f})")
    return first_neg, a_cb, lam_cb

# ---- run on the requested families ----
analyze("p",     lambda p: p)
analyze("p-1",   lambda p: p-1)
analyze("p^2",   lambda p: p**2)
analyze("p+5",   lambda p: p+5)
analyze("p+1000000", lambda p: p+1000000, Nmax=6)
