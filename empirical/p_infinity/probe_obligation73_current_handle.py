"""
EXPLORATORY -- does the apex channel carry an intrinsic IRREVERSIBLE current that the
symmetric entropy-defect (N14 Thm 7.6) discarded?  (the chiral/RH handle)

The entropy-production defect S(Bp)-S(p) used only majorization Bp<p, which is symmetric
in B (holds for B and B^T alike). The arrow / chiral content lives in the ANTISYMMETRIC
part of the transition -- the probability current J = B - B^T (detailed-balance defect w.r.t.
the uniform vacuum). If J != 0 the apex channel is already non-normal/irreversible and the
chiral handle is intrinsic to U_p.

We measure, per prime p:
  B   = |U_p|^2                          (doubly-stochastic Helmert->character transition)
  J   = B - B^T                          (probability current; J=0 <=> detailed balance/reversible)
  ||J||, and the spectrum of B (complex eigenvalues => non-normal arrow, Im(lambda) = rotation)
  comparison: symmetric part B_S=(B+B^T)/2 (the delivered metric channel) vs current J (the missed chiral part)

No torch. mpmath only. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 40

def apex_unitary(p):
    w = mp.e ** (2j * mp.pi / p)
    N1 = p - 1
    U = mp.zeros(N1, N1)
    for k in range(1, p):
        Rk = 1 / mp.sqrt(p * k * (k + 1))
        for c in range(1, p):
            s = mp.fsum(w ** (c * j) for j in range(0, k)) - k * w ** (c * k)
            U[k - 1, c - 1] = Rk * s
    return U

def mod2_transition(U):
    N1 = U.rows
    B = mp.zeros(N1, N1)
    for k in range(N1):
        for c in range(N1):
            B[c, k] = abs(U[k, c]) ** 2
    return B

def fro(M):
    return mp.sqrt(mp.fsum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))

def parity_perm(p):
    """R: c -> (-c mod p) on character indices {1..p-1} = complex conjugation chi_c -> chi_{-c}
    (the parity that separates even zeta from odd L(.,chi_3))."""
    N1 = p - 1
    R = mp.zeros(N1, N1)
    for c in range(1, p):
        cm = (-c) % p
        R[cm - 1, c - 1] = 1
    return R

def svals(M):
    # singular values via eig of M^H M
    H = M.H * M
    N1 = H.rows
    Hs = mp.matrix(N1, N1)
    for i in range(N1):
        for j in range(N1):
            Hs[i, j] = (H[i, j] + mp.conj(H[j, i])) / 2
    ev = mp.eigsy(Hs, eigvals_only=True)
    return sorted((mp.sqrt(max(mp.re(e), 0)) for e in ev), reverse=True)

print("=" * 78)
print("apex channel: current J=B-B^T, irreversibility gap, and the c->-c parity of J")
print("=" * 78)
for p in (3, 5, 7, 11, 13):
    N1 = p - 1
    U = apex_unitary(p)
    B = mod2_transition(U)
    Bt = B.T
    J = B - Bt
    BS = (B + Bt) / 2
    nJ, nBS = fro(J), fro(BS - mp.eye(N1) * (mp.mpf(1) / N1))
    # irreversibility gap (E10 conveyor): sum sigma(B) - sum |lambda(B)|
    sig = svals(B)
    E = mp.eig(B, left=False, right=False)
    lam = [abs(e) for e in E]
    gap = mp.fsum(sig) - mp.fsum(lam)
    imax = max(abs(mp.im(e)) for e in E)
    # parity test: under R (c->-c), is the current ODD?  R J R = -J  <=> J in the chiral/odd sector.
    R = parity_perm(p)
    RJR = R * J * R
    odd_resid = fro(RJR + J)    # 0 => J is ODD under parity (chiral)
    even_resid = fro(RJR - J)   # 0 => J is EVEN under parity
    # also: is B itself parity-covariant?  R B R = B^T  (conjugation reverses the arrow)
    cov_resid = fro(R * B * R - Bt)
    print(f"\np={p} (N'={N1}):")
    print(f"  ||J||_F = {mp.nstr(nJ,6)}   ||B_S-unif||_F = {mp.nstr(nBS,6)}   J/metric = {mp.nstr(nJ/nBS,5) if nBS>0 else 'NA'}")
    print(f"  irreversibility gap  sum sigma - sum|lambda| = {mp.nstr(gap,6)}   (E10 conveyor gap; 0 => normal)")
    print(f"  max|Im lambda(B)| = {mp.nstr(imax,4)}  (=> conveyor-type, not drift-ring)")
    print(f"  PARITY of current J under c->-c :  ||RJR + J|| = {mp.nstr(odd_resid,4)} (odd)   ||RJR - J|| = {mp.nstr(even_resid,4)} (even)")
    print(f"  channel parity-covariance        :  ||RBR - B^T|| = {mp.nstr(cov_resid,4)}  (0 => conjugation reverses the arrow)")
print("\n" + "=" * 78)
print("reading: J != 0 => apex channel intrinsically NON-NORMAL (chiral arrow lives in U_p).")
print("If ||RJR + J|| ~ 0: the current J is ODD under c->-c = the chiral/L(.,chi_3) sector,")
print("i.e. exactly the RH-bearing part that the symmetric entropy-defect (Thm 7.6) is blind to.")
print("=" * 78)
