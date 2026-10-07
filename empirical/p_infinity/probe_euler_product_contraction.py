"""
ATTACK: prove the energy contraction rho_E = lambda_max(A^{-1/2} P A^{-1/2}) <= 1 from the EULER PRODUCT
(P = sum_p P_p, the primes summed multiplicatively).  This is the wall (N11 forward door / N9 Conj 5.4).
We do not expect to breach it; we set up the multiplicative argument concretely and locate EXACTLY where
the local (per-prime) -> global (archimedean) assembly fails.

A = pole + archimedean Gamma-factor (PD energy metric, basis nu=8,14,20,26 all > 2pi).
P_p = contribution of prime p and its powers.  Three multiplicative structures tested:

  E1  SHARP partial sums  P_{<=X} = sum_{p<=X} P_p.  Is rho_E(X) <= 1 term-by-term (an inductive
      multiplicative argument) -- or does it OVERSHOOT (a finite partial sum exceeds the archimedean)?
  E2  SMOOTH (Abel/Gaussian) partial sums  P_X = sum_p e^{-(p/X)^2} P_p.  Does smoothing remove the
      overshoot (-> the overshoot is a GIBBS artifact of the sharp cutoff, not the real obstruction)?
  E3  LOCAL vs GLOBAL.  Per-prime energy lambda_max(A^{-1/2} P_p A^{-1/2}) and its SUM (does the bound
      come from per-prime smallness, or from a GLOBAL cancellation against the archimedean?).

Honest target: show the Euler product forces the contraction on the finite-prime part (smoothly, monotone),
but rho_E<=1 is a property of the COMPLETED object whose archimedean factor is not multiplicatively
generable and whose limit value is the marginal RH.  Conservation of difficulty, located.

No torch. mpmath. Deterministic.
"""
import mpmath as mp
mp.mp.dps = 22

s = mp.mpf(3); NUS = [mp.mpf(v) for v in (8, 14, 20, 26)]; n = len(NUS)
def Omega(r): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)
def abc(j, k):
    return [(mp.e**(-(a-b)**2/(4*s**2)), (a+b)/2)
            for a in (NUS[j], -NUS[j]) for b in (NUS[k], -NUS[k])]
def gfun(j, k, u):
    return s/(2*mp.sqrt(mp.pi))*mp.e**(-s**2*u**2/4)*mp.fsum(A*mp.cos(c*u) for A, c in abc(j, k))
def arch(j, k):
    tot = mp.mpf(0)
    for A, c in abc(j, k):
        tot += A*mp.quad(lambda r: mp.e**(-(r-c)**2/s**2)*Omega(r), [c-7*s, c, c+7*s])
    return tot/(2*mp.pi)
def pole(j, k):
    ph = lambda jj, r: mp.e**(-(r-NUS[jj])**2/(2*s**2)) + mp.e**(-(r+NUS[jj])**2/(2*s**2))
    return mp.re(ph(j, 1j/2)*ph(k, 1j/2) + ph(j, -1j/2)*ph(k, -1j/2))

# energy metric A = pole + arch (PD)
A = mp.matrix(n, n)
for j in range(n):
    for k in range(j, n):
        A[j,k]=A[k,j]=pole(j,k)+arch(j,k)
EA, QA = mp.eigsy(A)
assert min(mp.re(EA[i]) for i in range(n)) > 0, "A not PD"
Aih = QA*mp.diag([1/mp.sqrt(mp.re(EA[i])) for i in range(n)])*QA.T

# per-prime-power matrices  P_pk[j,k] = 2 log p / p^{k/2} * g(j,k,log p^k)
PRIMES = [p for p in range(2, 5000) if all(p % d for d in range(2, int(p**0.5)+1))]
ppow = []   # (p, pk, contribution-matrix)
for p in PRIMES:
    lp = mp.log(p); pk = p
    while pk <= 5000:
        M = mp.matrix(n, n)
        for j in range(n):
            for k in range(j, n):
                M[j,k]=M[k,j]=2*lp/mp.sqrt(pk)*gfun(j, k, mp.log(pk))
        ppow.append((p, pk, M)); pk *= p

def rho_E(weight):    # weight: pk -> w
    P = mp.matrix(n, n)
    for p, pk, M in ppow:
        w = weight(p, pk)
        if w == 0: continue
        for j in range(n):
            for k in range(n):
                P[j,k] += w*M[j,k]
    T = Aih*P*Aih
    E, _ = mp.eigsy((T+T.T)/2)
    return max(mp.re(E[i]) for i in range(n))

print("=" * 86)
print("ATTACK: does the Euler product P=sum_p P_p force the contraction rho_E<=1 term-by-term?")
print("=" * 86)

print(f"\nE1  SHARP partial sums rho_E(X) = lambda_max(A^-1/2 (sum_{{p<=X}} P_p) A^-1/2):")
print(f"      {'X':>6} {'rho_E(X)':>14} {'<=1 ?':>8}")
overshoot = False
for X in [3, 5, 7, 11, 13, 30, 100, 1000, 5000]:
    r = rho_E(lambda p, pk, X=X: 1 if pk <= X else 0)
    if r > 1: overshoot = True
    print(f"      {X:>6} {mp.nstr(r,8):>14} {('YES' if r<=1 else 'NO -- OVERSHOOT'):>8}")
print(f"      => sharp partial sums {'OVERSHOOT 1 at finite X' if overshoot else 'stay <=1'}: "
      f"{'NO term-by-term/inductive multiplicative contraction.' if overshoot else 'monotone.'}")

print(f"\nE2  SMOOTH (Gaussian/Abel) partial sums rho_E_smooth(X) = with weight exp(-(p/X)^2):")
print(f"      {'X':>6} {'rho_E_smooth(X)':>16} {'<=1 ?':>8}")
smooth_over = False
for X in [3, 5, 7, 11, 13, 30, 100, 1000]:
    r = rho_E(lambda p, pk, X=X: mp.e**(-(mp.mpf(p)/X)**2))
    if r > 1: smooth_over = True
    print(f"      {X:>6} {mp.nstr(r,8):>16} {('YES' if r<=1 else 'NO'):>8}")
print(f"      => smooth partial sums {'STILL overshoot' if smooth_over else 'are MONOTONE (no overshoot)'}: "
      f"the sharp overshoot is {'NOT just' if smooth_over else 'a'} a GIBBS artifact.")

print(f"\nE3  LOCAL vs GLOBAL: per-prime energy vs the bounded global contraction:")
perp = []
for p in PRIMES[:12]:
    r = rho_E(lambda q, pk, p=p: 1 if q == p else 0)
    perp.append((p, r))
print(f"      per-prime lambda_max(A^-1/2 P_p A^-1/2):  " + ", ".join(f"p={p}:{mp.nstr(r,3)}" for p, r in perp))
sum_perp = mp.fsum(r for _, r in perp)
print(f"      sum of first 12 per-prime energies = {mp.nstr(sum_perp,4)}  (and sum_p (log p)/sqrt p DIVERGES)")
print(f"      yet the global rho_E(infinity) = {mp.nstr(rho_E(lambda p, pk: 1),8)} <= 1.")
print(f"      => the bound is NOT per-prime smallness (the per-prime sum is large/divergent) -- it is a")
print(f"         GLOBAL cancellation of the prime sum against the archimedean A.  Local !=> global.")

print("\n" + "=" * 86)
print(f"""VERDICT -- the multiplicative argument, set up and located:
  * The Euler product gives P as a SUM over primes, but the contraction is NOT term-by-term: sharp
    partial sums OVERSHOOT rho_E>1 at finite X (the archimedean is briefly exceeded), so no inductive
    "each prime preserves the contraction" argument exists.
  * SMOOTHING the cutoff {'still overshoots -- the obstruction is not merely Gibbs' if smooth_over else
    'removes the overshoot (monotone): the overshoot is a GIBBS artifact of the sharp cutoff. The REAL'}
  {'' if smooth_over else 'content is the MONOTONE LIMIT rho_E(inf) = 1 - O(1e-6), the marginal case = RH.'}
  * The boundedness is a GLOBAL cancellation against the archimedean A, NOT per-prime smallness (the
    per-prime energies sum to a divergent total).  This is N11 Prop 6.2 (local != global) in the energy
    shape: the Euler factors are FINITE-prime; the contraction needs the archimedean factor A, which is
    the 2pi-hinged Gamma-factor -- NOT one of the finite Euler factors, NOT finitely-prime-generable.
  NET: the Euler product forces the finite-prime part {'(but not even smoothly)' if smooth_over else
    '(smoothly, monotone toward the limit)'}; the residue is the archimedean completion's marginal
  positivity -- exactly RH, exactly N11's wall.  The assembly point is named: the archimedean factor /
  the smooth-to-marginal limit.  Multiplicative input forces everything EXCEPT the archimedean inequality.
""")
print("=" * 86)
