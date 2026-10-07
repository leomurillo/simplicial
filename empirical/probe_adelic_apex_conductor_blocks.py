"""
First conductor-block probe for the Adelic Apex Operator (N4 sequel).

The leap: M_N = H F = 1 (+) U_N is the operator-theoretic completed object
 xi = prod_v Z_v, with
   pole at s=1        <-> the split-off trivial mode "1"          (N2)
   finite Euler p|N   <-> conductor-d blocks of U_N, dim phi(d)   (T9.4)
   archimedean Z_inf  <-> the sqrt(N) edge limit (A-I)Phi          (N4)

SHARP TEST (this probe).  For squarefree primorial N = prod_{p in P} p, the
character side factors by CRT (Good-Thomas): the conductor packet for a subset
S subset P (d = prod_{p in S} p) is  (x)_{p in S} (nontrivial chars of Z/p),
of dimension prod_{p in S}(p-1) = phi(d).  IF the apex unitary is an operator
Euler product -- i.e. U_N is conjugate to the place-factored apex -- then its
spectrum must be exactly the inclusion-exclusion multiset
   spec_pred(U_N) = U_{S != empty}  { prod_{p in S} lambda_p : lambda_p in spec(U_p) },
of size prod_p p - 1 = N - 1.  We compare spec_pred(U_N) to the actual
spec(U_N).  Match => spectral Euler product is real (leap de-risked).
Mismatch => the Helmert frame scrambles the places spectrally (the adelic
operator needs the CRT-factored real basis, not Helmert) -- still informative.

Also: dictionary checks (pole split, conductor dims), cluster-multiplicity
comparison, and the Helmert conductor-mass profile mu(k,d).

Deterministic: numpy only.
"""

import numpy as np
from itertools import combinations, product
from math import gcd

# --------------------------------------------------------------------------
def apex_unitary(N):
    """U_N in U(N-1), closed-form geometric entries (rows k, cols c, 1..N-1)."""
    if N == 2:
        return np.array([[1.0 + 0j]])
    k = np.arange(1, N).reshape(-1, 1)
    c = np.arange(1, N).reshape(1, -1)
    w = np.exp(2j * np.pi / N)
    wck = w ** (c * k)
    wc = w ** c
    geom = (wck - 1.0) / (wc - 1.0)
    Ckc = geom - k * wck
    R = 1.0 / np.sqrt(N * k * (k + 1))
    return R * Ckc

def full_apex(N):
    """M_N = H F^T as the full N x N matrix, to verify the 1 (+) U_N split."""
    j = np.arange(N)
    # Helmert H: row 0 = mean; row k = h_k/||h_k||
    H = np.zeros((N, N))
    H[0, :] = 1.0 / np.sqrt(N)
    for kk in range(1, N):
        h = np.zeros(N); h[:kk] = 1.0; h[kk] = -kk
        H[kk, :] = h / np.sqrt(kk * (kk + 1))
    w = np.exp(2j * np.pi / N)
    F = w ** (np.outer(j, j)) / np.sqrt(N)        # symmetric Fourier
    return H @ F.T

def prime_factors(N):
    P, m, d = [], N, 2
    while d * d <= m:
        if m % d == 0:
            P.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        P.append(m)
    return P

def euler_factor(p):
    return p - 1  # phi(p); = dim U_p

def euler_predicted_spectrum(N, P):
    specs = {p: np.linalg.eigvals(apex_unitary(p)) for p in P}
    pred = []
    for r in range(1, len(P) + 1):
        for S in combinations(P, r):
            for combo in product(*[specs[p] for p in S]):
                pred.append(np.prod(combo))
    return np.array(pred), specs

def cluster_mult(ev):
    """Counts near 1, i, -1, -i."""
    ang = np.angle(ev) / (2 * np.pi) % 1.0
    near = np.round(ang * 4).astype(int) % 4
    return [int(np.sum(near == r)) for r in range(4)]  # [+1, +i, -1, -i]

def sorted_compare(a, b):
    """Sort two equal-length unit-circle multisets by angle, elementwise max diff."""
    sa = a[np.argsort(np.angle(a) % (2 * np.pi))]
    sb = b[np.argsort(np.angle(b) % (2 * np.pi))]
    return np.max(np.abs(sa - sb)), sa, sb

def hausdorff(a, b):
    """Symmetric nearest-neighbour distance between the two multisets (as sets)."""
    D = np.abs(a.reshape(-1, 1) - b.reshape(1, -1))
    return max(np.max(np.min(D, axis=1)), np.max(np.min(D, axis=0)))

# ==========================================================================
print("=" * 76)
print("ADELIC APEX OPERATOR -- conductor-block probe at N = 6, 30, 210")
print("=" * 76)

for N in [6, 30, 210]:
    P = prime_factors(N)
    print(f"\n{'='*76}\nN = {N} = {' * '.join(map(str,P))}   (primes P = {P})\n{'='*76}")

    # ---- dictionary: the 1 (+) U_N pole split ----------------------------
    M = full_apex(N)
    U = apex_unitary(N)
    pole_err = max(np.max(np.abs(M[0, 1:])), np.max(np.abs(M[1:, 0])),
                   abs(M[0, 0] - 1.0), np.max(np.abs(M[1:, 1:] - U)))
    print(f"[dictionary] M_N = 1 (+) U_N  (pole = trivial mode):  max dev = {pole_err:.2e}")

    # ---- conductor partition: sizes = phi(d), sum = N-1 ------------------
    cond = {}
    for c in range(1, N):
        d = N // gcd(c, N)
        cond.setdefault(d, []).append(c)
    sizes = {d: len(cs) for d, cs in sorted(cond.items())}
    print(f"[dictionary] conductor packets (d: dim=phi(d)): {sizes}")
    print(f"             sum of dims = {sum(sizes.values())} = N-1 = {N-1}  "
          f"[{'OK' if sum(sizes.values())==N-1 else 'FAIL'}]")

    # ---- SHARP TEST: spectral Euler product ------------------------------
    ev = np.linalg.eigvals(U)
    pred, specs = euler_predicted_spectrum(N, P)
    print(f"\n[Euler test] |spec(U_N)| = {len(ev)},  |spec_pred| = {len(pred)}  "
          f"(prod(p)-1 = {np.prod(P)-1})")
    for p in P:
        print(f"             spec(U_{p}) angles/turn: "
              f"{np.round(np.sort(np.angle(specs[p])/(2*np.pi)%1.0),4)}")
    mx, sa, sb = sorted_compare(ev, pred)
    hd = hausdorff(ev, pred)
    print(f"[Euler test] sorted elementwise max |actual - predicted| = {mx:.4f}")
    print(f"[Euler test] Hausdorff(actual, predicted)               = {hd:.4f}")
    cm_a, cm_p = cluster_mult(ev), cluster_mult(pred)
    print(f"[Euler test] cluster mult (+1,+i,-1,-i):  actual {cm_a}   predicted {cm_p}"
          f"   [{'MATCH' if cm_a==cm_p else 'differ'}]")
    verdict = ("SPECTRAL EULER PRODUCT HOLDS" if mx < 1e-8 else
               "clusters match, fine spectrum differs" if cm_a == cm_p else
               "Helmert scrambles places spectrally")
    print(f"[Euler test] >>> {verdict}")
    if N == 6:
        print("   actual angles/turn   :", np.round(np.angle(sa)/(2*np.pi)%1.0, 4))
        print("   predicted angles/turn:", np.round(np.angle(sb)/(2*np.pi)%1.0, 4))

    # ---- Helmert conductor-mass profile mu(k,d) (does Helmert respect d?) -
    if N <= 30:
        dlist = sorted(cond)
        mu = np.zeros((N - 1, len(dlist)))
        for ki in range(N - 1):
            for di, d in enumerate(dlist):
                cols = [c - 1 for c in cond[d]]
                mu[ki, di] = np.sum(np.abs(U[ki, cols]) ** 2)
        # row-concentration: max share each Helmert row puts in one conductor
        conc = np.max(mu, axis=1)
        print(f"[Helmert]    mean row conductor-concentration max_d mu(k,d) = "
              f"{np.mean(conc):.3f}  (1.0 = Helmert respects conductors; "
              f"~1/{len(dlist)}={1/len(dlist):.3f} = fully spread)")

print(f"\n{'='*76}\nINTERPRETATION")
print("=" * 76)
print("""  If the spectral Euler product holds (max diff ~ 0): U_N is conjugate to
  the place-factored apex (x)_p U_p, so the apex unitary IS the operator Euler
  product and the Adelic Apex Operator is exact -- the leap is de-risked.

  If only clusters match: the CRT multiplicity structure survives but the
  Helmert frame rotates the fine spectrum; the adelic operator wants the
  CRT-factored real basis.

  If neither: the Helmert apex is genuinely not a tensor product over places;
  the adelic assembly must be built in the character/CRT basis, with Helmert
  entering only as the dimensional-axis dressing.""")
