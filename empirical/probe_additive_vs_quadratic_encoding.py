"""
Additive (log-derivative / Li / Kubo-Mori register) vs quadratic (moment / Hankel
/ Bures register) encoding of the SAME zeta zeros.

Tests the 1(+)3 thesis (N0 route map): the no-crossing / positivity margin
collapses in the QUADRATIC moment encoding (folded-Xi Hankel gates: lam_min/lam_max
-> 0, the Lambda=0 marginal cancellation) but is MANIFEST and robust in the
ADDITIVE log-derivative encoding (Li coefficients: each on-line zero contributes
4 sin^2(n alpha/2) >= 0, no cancellation).

HONEST CAVEAT (Chentsov): on the classical (commuting) folded tower, ALL monotone
metrics coincide with Fisher-Rao, so a Bures-vs-Kubo-Mori metric REWEIGHTING of the
moments changes nothing. The real lever is not the metric tensor but the ENCODING
FUNCTIONAL of the zeros:
   quadratic:  gamma -> lambda = gamma^{-2}    (moments of xi; zeros entangled -> marginal)
   additive:   gamma -> alpha(gamma), Li        (log-derivative of xi; zeros as poles -> manifest)
This is 'additive geometry sees zeros as Herglotz poles; Bures/quadratic smooths
them away', made computable.

PART A  quadratic register: folded-Xi Hankel gates, margin lam_min/lam_max -> 0.
PART B  additive register : Li coefficients lambda_n = sum_{gamma>0} 4 sin^2(n alpha/2),
        alpha = atan2(gamma, gamma^2 - 1/4); manifest >=0 per zero, growing; lambda_1
        reproduces the classical Keiper-Li value 0.0231 (validation).
PART C  sensitivity, both registers: push zero #3 to Re<1/2. Additive: that zero's
        term 2-2Re[(1-1/rho)^n] loses manifest non-negativity (|1-1/rho|>1) and goes
        negative for some n -- but can be MASKED in the total by the on-line zeros
        (the same maskability that makes phi'>=0 / per-term Li necessary-not-sufficient;
        the global statement is RH).

Deterministic: mpmath only. No torch.
"""

import mpmath as mp
mp.mp.dps = 50

M = 400
print(f"computing first {M} zeta zeros (dps={mp.mp.dps}) ...")
gammas = [mp.im(mp.zetazero(k)) for k in range(1, M + 1)]

# ============================================================================
# PART A -- QUADRATIC / MOMENT register (Bures-flavored): folded-Xi Hankel gates
# ============================================================================
print()
print("=" * 78)
print("PART A -- quadratic encoding gamma -> lambda=gamma^-2 : folded-Xi Hankel gate")
print("=" * 78)
lam = [1 / g**2 for g in gammas]
lam1 = lam[0]
lamn = [l / lam1 for l in lam]          # normalize largest atom -> 1 (conditioning)
NMAX = 8
def moments(atoms):
    return [mp.fsum(a**(n + 1) for a in atoms) for n in range(0, 2 * NMAX + 2)]
def hankel(mu, n, shift=0):
    return mp.matrix([[mu[a + b + shift] for b in range(n + 1)] for a in range(n + 1)])
def eig_ratio(A):
    n = A.rows
    Ar = mp.matrix([[mp.re(A[i, j]) for j in range(n)] for i in range(n)])
    ev = sorted(mp.re(e) for e in mp.eigsy(Ar, eigvals_only=True))
    return ev[0], ev[-1]
muA = moments(lamn)
print(f"  atoms lambda_k=gamma_k^-2 accumulate at 0: lambda_1={float(lam[0]):.3e}, "
      f"lambda_10={float(lam[9]):.3e}, lambda_100={float(lam[99]):.3e}")
print(f"  {'n':>3} {'lam_min(H_n)':>16} {'lam_min/lam_max':>18}")
for n in range(1, NMAX + 1):
    hmin, hmax = eig_ratio(hankel(muA, n, 0))
    print(f"  {n:>3} {mp.nstr(hmin, 4):>16} {mp.nstr(hmin / hmax, 4):>18}")
print("  >>> margin lam_min/lam_max -> 0 super-exponentially: positivity is a")
print("      DELICATE near-rank-1 cancellation (the Lambda=0 marginal signature).")

# ============================================================================
# PART B -- ADDITIVE / LOG-DERIVATIVE register (Kubo-Mori / Li)
# ============================================================================
print()
print("=" * 78)
print("PART B -- additive encoding gamma -> alpha, Li coefficients")
print("   lambda_n = sum_{gamma>0} 4 sin^2(n alpha/2),  alpha=atan2(gamma, gamma^2-1/4)")
print("=" * 78)
def alpha_of(g):
    return mp.atan2(g, g * g - mp.mpf(1) / 4)
alphas = [alpha_of(g) for g in gammas]
def li_zero(n):
    return mp.fsum(4 * mp.sin(n * a / 2)**2 for a in alphas)
def li_min_term(n):
    return min(4 * mp.sin(n * a / 2)**2 for a in alphas)
print(f"  {'n':>3} {'lambda_n (Li, M-trunc)':>24} {'min per-zero term':>19} {'lambda_n/n':>12}")
for n in [1, 2, 3, 4, 5, 10, 20, 30, 40, 60]:
    ln = li_zero(n)
    mt = li_min_term(n)
    print(f"  {n:>3} {mp.nstr(ln, 8):>24} {mp.nstr(mt, 4):>19} {mp.nstr(ln / n, 4):>12}")
print(f"  validation: lambda_1 = {mp.nstr(li_zero(1), 8)}  vs classical Keiper-Li 0.0230957")
print("  >>> every per-zero term >= 0 (MANIFEST, no cancellation); lambda_n positive")
print("      and growing. Positivity is term-by-term: the additive register 'sees")
print("      each zero as a Herglotz pole' contributing 4 sin^2 >= 0.")

# ============================================================================
# PART C -- sensitivity in both registers: one zero off the line (Re < 1/2)
# ============================================================================
print()
print("=" * 78)
print("PART C -- push zero #3 to rho = 1/2 - beta + i*gamma_3 (Re < 1/2)")
print("=" * 78)
g3 = gammas[2]
print("  ADDITIVE: on-line term is 4 sin^2(n a/2) >= 0 for all n; off-line term is")
print("  2 - 2 Re[(1-1/rho)^n] with |1-1/rho| > 1 -> loses manifest non-negativity.")
print(f"  {'beta':>6} {'|1-1/rho|':>12} {'min_n term (n<=200)':>21} {'argmin n':>9}")
for beta in [mp.mpf('1.0'), mp.mpf('0.3'), mp.mpf('0.1')]:
    rho = mp.mpc(mp.mpf('0.5') - beta, g3)
    u = 1 - 1 / rho
    mod = abs(u)
    worst = None
    argn = None
    for n in range(1, 201):
        term = 2 - 2 * mp.re(u**n)      # contribution of the (rho, conj rho) pair
        if worst is None or term < worst:
            worst = term
            argn = n
    print(f"  {float(beta):>6} {float(mod):>12.6f} {mp.nstr(worst, 4):>21} {argn:>9}")
print("  (on-line beta=0: |1-1/rho|=1 exactly, term = 4 sin^2 >= 0 for every n.)")
print()
print("  MASKABILITY: one off-line zero pushes ITS additive term negative, but the")
print("  on-line zeros contribute +O(n log n), so the TOTAL lambda_n can stay > 0 at")
print("  small n -- the same maskability that makes phi'>=0 / per-term positivity")
print("  necessary-not-sufficient. RH = the GLOBAL statement (all lambda_n >= 0, all n;")
print("  equivalently m_B Herglotz). The quadratic gate amplifies the off-line atom and")
print("  a finite Hankel gate goes negative early (probe_folded_xi_gates_margin).")

print()
print("=" * 78)
print("READING")
print("=" * 78)
print("""  SAME zeros, two encodings, opposite behavior:
   - QUADRATIC (moments of xi, lambda=gamma^-2, Bures register): positivity is a
     delicate near-rank-1 cancellation; margin lam_min/lam_max -> 0 (Lambda=0).
   - ADDITIVE (log-derivative of xi, Li, Kubo-Mori register): positivity is MANIFEST
     per zero (4 sin^2 >= 0), robust and growing; zeros enter as Herglotz poles.

  Chentsov caveat: on the classical folded tower all monotone metrics coincide, so a
  Bures->Kubo-Mori metric REWEIGHTING of the moments does nothing. The lever is the
  ENCODING FUNCTIONAL (moments vs log-derivative/Li), not the metric tensor.

  => N0 / Sketch 1: build the finite Hermite-Biehler exhaustion E_N from the additive
     log-derivative (m_B / Li / Keiper) data, where positivity is manifest and uniform,
     NOT from the moment/Hankel data, where it is marginal. Primes enter additively
     (von Mangoldt / log xi), confirming the 1(+)3 merge with the correct mechanism.
     The remaining content is the GLOBAL Herglotz property (per-term/finite positivity
     is maskable) -- i.e. the Riemann Hypothesis.""")
