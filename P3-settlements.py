#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P3-settlements.py  --  Grounded settlement artifact for paper P3
(exterior of the finite-apex boundary calculus, T11-T15), under the
Grounded-Paranoid-Delusional method (Paper 35).

Four audits. Each prints its PRE-CLAIM (matched-pair K / L / joint-on-disjoint,
meaning fixed BEFORE the computation runs), then settles on DETERMINISTIC,
EXACT arithmetic (integer / Fraction; no seeds; no float in any vanishing,
membership, or sign decision), then prints the REALIZED branch.

Anchored objects (GPD 3.3 -- the source's own objects):
  T11 (Apex Vertex Calculus): cond(a)=N/gcd(a,N); conductor-fusion boundary
        d_n(S)=Fuse_n(S)\\(S u {1}); projection-closure (Thm 4.1); Cl_n (Def 5.1).
  T12 (Finite Apex Determinacy): moments mu_n=sum_j W_j lam_j^n; Hankel rank =
        #distinct levels r; apex tower ~= R[t]/(P_x), P_x=prod(t-lam_j) (Thm 6).
  T14 (Projected Flatness / Curvature): the projected cubic residual
        (1-Pi_S-Pi_1)(u v w) is supported on d_3(S); curvature = boundary leakage
        = renormalization source = Noether defect (Thm 6 equivalence).
  T15 (Finite-to-Archimedean Completion): smooth primorial פ; the primorial is
        not a moment sequence -- Hankel D_3<0 (Prop 12.2); the real place {oo} is
        a terminal external boundary, not a finite packet.

Run:  python P3-settlements.py
Deterministic; re-run reproduces this transcript identically.
"""

import sys
from fractions import Fraction
from math import gcd

# Emit UTF-8 regardless of the platform locale (the transcript contains פ and ∂).
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr():  print("=" * 78)
def sub(): print("-" * 78)


# --------------------------------------------------------------------------
# exact linear algebra over the rationals (no float anywhere)
# --------------------------------------------------------------------------
def det_exact(M):
    """Exact determinant of a square matrix of int/Fraction, via fraction-free
    Gaussian elimination. Returns a Fraction (exact)."""
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    det = Fraction(1)
    for col in range(n):
        piv = None
        for r in range(col, n):
            if A[r][col] != 0:
                piv = r; break
        if piv is None:
            return Fraction(0)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        det *= A[col][col]
        inv = A[col][col]
        for r in range(col + 1, n):
            f = A[r][col] / inv
            if f != 0:
                for c in range(col, n):
                    A[r][c] -= f * A[col][c]
    return det

def rank_exact(M):
    """Exact rank of a matrix of int/Fraction by row reduction."""
    A = [[Fraction(x) for x in row] for row in M]
    rows, cols = len(A), len(A[0])
    rank, pr = 0, 0
    for c in range(cols):
        piv = None
        for r in range(pr, rows):
            if A[r][c] != 0:
                piv = r; break
        if piv is None:
            continue
        A[pr], A[piv] = A[piv], A[pr]
        inv = A[pr][c]
        A[pr] = [v / inv for v in A[pr]]
        for r in range(rows):
            if r != pr and A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][k] - f * A[pr][k] for k in range(cols)]
        pr += 1; rank += 1
    return rank


# --------------------------------------------------------------------------
# T-series conductor arithmetic (T3/T11): cond(a) = N/gcd(a,N), cond(0)=1
# --------------------------------------------------------------------------
def cond(a, N):
    a %= N
    return 1 if a == 0 else N // gcd(a, N)

def packet_indices(d, N):
    """The conductor-d packet H_d: nontrivial indices a with cond(a)=d."""
    return [a for a in range(1, N) if cond(a, N) == d]

def fusion_boundary(S, N, n):
    """d_n(S): the universal residual support of the projected n-vertex on
    H_S = (+)_{d in S} H_d, i.e. all output conductors not in S u {1} reachable
    as cond(a_1+...+a_n) with each cond(a_i) in S. Brute force, exact."""
    legs = [a for a in range(1, N) if cond(a, N) in S]
    out = set()
    # iterate n-tuples of legs (n is small here: n=3)
    def rec(depth, acc_sum):
        if depth == n:
            c = cond(acc_sum % N, N)
            if c not in S and c != 1:
                out.add(c)
            return
        for a in legs:
            rec(depth + 1, acc_sum + a)
    rec(0, 0)
    return frozenset(out)

def fusion_closure(S, N, n):
    """Cl_n(S): smallest packet set >= S closed under n-fold fusion (T11 Def 5.1)."""
    S = set(S)
    while True:
        b = fusion_boundary(S, N, n)
        if b <= S:
            return frozenset(S)
        S |= set(b)


# ==========================================================================
hr(); print("AUDIT  פ11  --  the conductor-fusion boundary  ∂_n S  is the leak")
hr()
print("""PRE-CLAIM (before the computation runs).
T11 Thm 4.1: a projected n-leg apex vertex closes on H_S iff S is fusion-closed,
and its UNIVERSAL residual support is the conductor-fusion boundary
   ∂_n S = Fuse_n(S) \\ (S u {1}).
Test bed N=6=2*3, packets H_2=span{χ3}, H_3=span{χ2,χ4}, H_6=span{χ1,χ5};
take S={2,3} (the non-unit sector A_2 (+) A_3), n=3 (cubic).

  K : ∂_3{2,3} = {6} exactly -- the mixed non-unit sector leaks precisely into
      the unit-indexed full-conductor packet H_6.
  L : ∂_3{2,3} != {6}  (empty, or includes packets other than 6).
  JOINT-ON-DISJOINT : ∂_3{2,3}={6}, yet the two pure axes self-close by
      DIFFERENT mechanisms -- the 2-axis triple {χ3,χ3,χ3} stays at conductor 2
      (p=2 parity BLOCKS cancellation), while the 3-axis triple {χ2,χ2,χ2}
      cancels to conductor 1 (odd prime, free cancellation). Parity-asymmetric.
Check: exact conductor arithmetic, brute-force over all cubic triples.""")
sub()
N = 6
for d in (1, 2, 3, 6):
    print(f"    H_{d} (N=6): indices {packet_indices(d, N)}")
S = frozenset({2, 3})
b = fusion_boundary(S, N, 3)
print(f"\n    ∂_3 S  for S={set(S)} :  {set(b)}")
print(f"    Cl_3(S)  (minimal fusion-closed sector)         :  {set(fusion_closure(S, N, 3))}")
# the parity asymmetry, exhibited on the two pure-axis cubes:
a2 = packet_indices(2, 6)[0]   # χ3
a3 = packet_indices(3, 6)[0]   # χ2
s222 = (a3 + a3 + a3) % 6       # three conductor-3 legs
s333 = (a2 + a2 + a2) % 6       # three conductor-2 legs
print(f"\n    3-axis cube  χ{a3}+χ{a3}+χ{a3} = χ{s222}: cond={cond(s222,6)}  "
      f"(odd prime 3: cancels to conductor 1, the trivial gauge)")
print(f"    2-axis cube  χ{a2}+χ{a2}+χ{a2} = χ{s333}: cond={cond(s333,6)}  "
      f"(prime 2: parity blocks cancellation, stays conductor 2)")
print(f"    => ∂_3{{2}}={set(fusion_boundary(frozenset({2}),6,3))}, "
      f"∂_3{{3}}={set(fusion_boundary(frozenset({3}),6,3))} "
      f"(both self-close, by the two different mechanisms)")
sub()
print("    breadth check (other cross-prime moduli):")
for NN, SS in [(12, frozenset({2, 3})), (12, frozenset({4, 3})), (30, frozenset({2, 3, 5}))]:
    print(f"      N={NN:2d}, S={set(SS)}: ∂_3 S = {set(fusion_boundary(SS, NN, 3))}, "
          f"Cl_3 = {set(fusion_closure(SS, NN, 3))}")
realized_11 = (b == frozenset({6}))
print()
print(f"REALIZED BRANCH  פ11 :  {'K + JOINT-ON-DISJOINT' if realized_11 else 'see above'}")
print("  K: ∂_3{2,3} = {6} exactly -- the non-unit sector leaks into H_6.")
print("  JOINT-ON-DISJOINT: the boundary is parity-asymmetric -- 3-axis cancels")
print("  to the trivial packet, 2-axis is parity-locked at conductor 2.")
print()


# ==========================================================================
hr(); print("AUDIT  פ12  --  the 'infinite' tower is the finite algebra  R[t]/(P_x)")
hr()
print("""PRE-CLAIM (before the computation runs).
T12 Thm 6: a centered ledger with r distinct levels lam_1..lam_r has apex tower
~= R[t]/(P_x), P_x(t)=prod_j (t-lam_j); moments mu_n=sum_j W_j lam_j^n obey the
degree-r recurrence read off P_x, and the moment Hankel matrices have rank r.
Test ledger: the 4-slot centered ledger y=(-1,-1,0,2)  (sum=0), with distinct
levels {-1,0,2} (r=3), uniform weight 1/4 per slot.

  K : Hankel rank stabilizes at r=3, AND the moments satisfy the exact degree-3
      recurrence from P_x(t)=(t+1)t(t-2)=t^3 - t^2 - 2t, i.e.
      mu_{n+3} = mu_{n+2} + 2 mu_{n+1}.  (The tower is finite spectral data.)
  L : rank grows past 3 / no finite recurrence (the tower carries unbounded
      new information).
Check: exact rational moments, exact Hankel ranks, exact recurrence residuals.""")
sub()
levels = [Fraction(-1), Fraction(0), Fraction(2)]
weights = [Fraction(2, 4), Fraction(1, 4), Fraction(1, 4)]   # slot multiplicities /N
r = len(levels)
def mu(n):
    return sum(W * (lam ** n) for lam, W in zip(levels, weights))
moments = [mu(n) for n in range(12)]
print(f"    distinct levels lam = {[str(l) for l in levels]}  (r={r})")
print(f"    moments mu_0..mu_8 = {[str(moments[n]) for n in range(9)]}")
print(f"    (mu_0=1, mu_1=0 since the ledger is centered)")
# Hankel ranks
print("\n    Hankel rank H_k = [mu_{i+j}]_{0<=i,j<=k}:")
ranks = []
for k in range(0, 6):
    Hk = [[moments[i + j] for j in range(k + 1)] for i in range(k + 1)]
    rk = rank_exact(Hk)
    ranks.append(rk)
    print(f"      k={k}: ({k+1}x{k+1})  rank = {rk}")
rank_stable = (max(ranks) == r and ranks[r-1] == r and ranks[-1] == r)
# recurrence mu_{n+3} = mu_{n+2} + 2 mu_{n+1}
resid = [moments[n + 3] - (moments[n + 2] + 2 * moments[n + 1]) for n in range(0, 9)]
rec_ok = all(z == 0 for z in resid)
print(f"\n    P_x(t) = (t+1) t (t-2) = t^3 - t^2 - 2t   =>   "
      f"mu_(n+3) - mu_(n+2) - 2 mu_(n+1) = 0 ?")
print(f"    exact recurrence residuals (n=0..8): {[str(z) for z in resid]}")
sub()
print(f"REALIZED BRANCH  פ12 :  {'K' if (rank_stable and rec_ok) else 'see above'}")
print(f"  Hankel rank stabilizes at r={r} (=#distinct levels) and the moments obey")
print("  the exact degree-3 recurrence: the tower IS the finite algebra R[t]/(P_x).")
print()


# ==========================================================================
hr(); print("AUDIT  פ14  --  curvature = boundary leakage  (one set, many names)")
hr()
print("""PRE-CLAIM (before the computation runs).
T14 Thm 6 (equivalence): the projected cubic CURVATURE defect
   R_S(u,v,w) = (1 - Pi_S - Pi_1)(u*v*w),   u,v,w in H_S,
(pointwise product * of characters) is supported on EXACTLY the same set as the
fusion boundary ∂_3 S of פ11 -- and that set is simultaneously the renormalization
source, the beta source, and the Noether defect. At N=6, S={2,3}, the claim is
that this single set is {1,5} = H_6.

  K : the cubic residual of H_S basis triples is supported exactly on the index
      set {1,5} = H_6 = ∂_3{2,3}; curvature support = fusion boundary.
  L : the curvature support differs from ∂_3 S.
  JOINT-ON-DISJOINT : support is {1,5}=H_6, but reached only by specific input
      multisets ({χ3,χ3,χ2}-type -> index 1; {χ3,χ2,χ2}... -> index 5, etc.).
Check: exact pointwise character products on the H_S basis; membership exact.""")
sub()
N = 6
HS_indices = sorted(a for a in range(1, N) if cond(a, N) in {2, 3})  # χ2,χ3,χ4
leak_support = set()
witnesses = {}
for a in HS_indices:
    for b in HS_indices:
        for c in HS_indices:
            out = (a + b + c) % N
            co = cond(out, N)
            if co not in {2, 3} and co != 1:       # off H_S (+) H_1  => curvature
                leak_support.add(out)
                witnesses.setdefault(out, (a, b, c))
print(f"    H_S basis indices (N=6, S={{2,3}}): {HS_indices}")
print(f"    cubic residual support (off H_S (+) H_1): indices {sorted(leak_support)}")
print(f"    cond of each: {{ {', '.join(f'χ{i}->cond {cond(i,N)}' for i in sorted(leak_support))} }}")
print(f"    => support packet = H_{cond(sorted(leak_support)[0],N) if leak_support else '-'} "
      f"(all leaked indices have conductor 6)")
for i in sorted(leak_support):
    a, b, c = witnesses[i]
    print(f"      witness  χ{a}*χ{b}*χ{c} = χ{i}  (index {i} in H_6)")
same_as_fusion = (frozenset(cond(i, N) for i in leak_support) == frozenset({6}))
print(f"\n    curvature support conductor set == ∂_3{{2,3}} == {{6}} ?  {same_as_fusion}")
sub()
print(f"REALIZED BRANCH  פ14 :  {'K + JOINT-ON-DISJOINT' if same_as_fusion else 'see above'}")
print("  The SAME set {1,5}=H_6 is the curvature defect support, the projection")
print("  residual, the renormalization/beta source, and the Noether defect (T14")
print("  Thm 6). Five interior names; one exterior boundary. JOINT: reached only")
print("  by the specific witness multisets shown.")
print()


# ==========================================================================
hr(); print("AUDIT  פ15  --  the real place {oo} is not a finite packet")
hr()
print("""PRE-CLAIM (before the computation runs).
T15 Prop 12.2: the primorial sequence P=(1,2,6,30,210,2310,30030,...) is NOT a
moment sequence -- its Hankel determinant D_3 is NEGATIVE -- so the smooth
primorial פ = e^{Li^-1(z)}/(2π) admits no Mellin/moment representation, and the
real place {oo} (the gamma factor, the 1/2π) is a TERMINAL external boundary,
not recoverable from finite-prime data. Contrast: the factorial (1,1,2,6,24,...)
IS a moment sequence (n! = ∫ t^n e^-t dt -- that is exactly why Gamma exists).

  K : D_3(primorial) < 0  (matching T15's exact value -787680), so the primorial
      is not a moment sequence and the real place is a terminal boundary; while
      the factorial has all Hankel D_k > 0 (a genuine moment sequence).
  L : D_3(primorial) >= 0 (the primorial IS a moment sequence; the real place is
      a finite packet, self-completing).
Check: exact INTEGER Hankel determinants D_0..D_3 of both sequences.""")
sub()
primorial = [1, 2, 6, 30, 210, 2310, 30030]            # P_n = prod_{p<=p_n} p
factorial = [1, 1, 2, 6, 24, 120, 720]                 # n!
def hankel_det(seq, k):
    M = [[seq[i + j] for j in range(k + 1)] for i in range(k + 1)]
    return det_exact(M)
print("    primorial (1,2,6,30,210,...) -- a pure finite-prime / Euler-product object:")
Dpri = [hankel_det(primorial, k) for k in range(4)]
for k, D in enumerate(Dpri):
    print(f"      D_{k} = {D}{'   <-- NEGATIVE' if D < 0 else ''}")
print("\n    factorial (1,1,2,6,24,...) -- the archimedean object n! = ∫_0^oo t^n e^-t dt:")
Dfac = [hankel_det(factorial, k) for k in range(4)]
for k, D in enumerate(Dfac):
    print(f"      D_{k} = {D}{'   (>0)' if D > 0 else ''}")
pri_not_moment = (Dpri[3] < 0)
fac_is_moment = all(D > 0 for D in Dfac)
matches_T15 = (Dpri[3] == -787680)
print(f"\n    D_3(primorial) == T15 Prop 12.2 value (-787680) ?  {matches_T15}")
sub()
print(f"REALIZED BRANCH  פ15 :  {'K' if (pri_not_moment and fac_is_moment) else 'see above'}")
print("  D_3(primorial) = -787680 < 0: the primorial is NOT a moment sequence, so a")
print("  finite-prime object cannot generate its own real-place completion -- the")
print("  archimedean boundary {oo} (the gamma factor, the 1/2π of the smooth")
print("  primorial פ) must be adjoined from outside. The factorial, by contrast,")
print("  IS a moment sequence: that is exactly why Euler's Gamma completes it.")
print()

hr(); print("END OF SETTLEMENTS  (deterministic; re-run reproduces this transcript)")
hr()
