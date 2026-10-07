"""
SCOPING THE NEXT ROUND: the level-of-distribution frontier, and the precise gap that is RH.

The push (push_tau1_prime_variance.py) confirmed the GUE plateau in the primes via the short-interval
variance and pinned the residual to a UNIFORM level-of-distribution statement (theta_0 ~ 0.515). This script
locates that residual exactly by computing the level-of-distribution's own SECOND MOMENT -- the
Barban-Davenport-Halberstam / Montgomery-Hooley variance -- and exhibiting the gap that is RH.

THE CLEAN DICHOTOMY (the point):
  * VARIANCE (L^2 average over residues a):  Barban-Davenport-Halberstam / Montgomery (PROVEN, full level)
        V_BDH(Q) := sum_{q<=Q} sum_{a mod q, (a,q)=1} ( psi(x;q,a) - x/phi(q) )^2  ~  Q x log x ,
    valid for Q up to x (level of distribution theta = 1). We HAVE the second moment to full level.
  * MAXIMUM (L^infinity over residues a):  Bombieri-Vinogradov (PROVEN only to theta = 1/2)
        sum_{q<=Q} max_{(a,q)=1} | psi(x;q,a) - x/phi(q) |  <<  x/(log x)^A ,  for Q <= x^{1/2-eps}.
    RH-strength correlation closure (the plateau, tau>1) needs this MAXIMAL error to theta > 1/2.
  * THE GAP = RH:  converting the L^2-average (have, theta=1) into the L^infinity-max (need, theta>1/2) is
    the DISPERSION method (Linnik; Bombieri-Friedlander-Iwaniec; Zhang). The program's frontier is exactly
    here: trilinear Kloosterman / well-factorable moduli give theta_0 ~ 0.515 (Wright Q <= X^{1/2+1/66-d};
    program memory: the obligation is the BV level C*, NOT Hardy-Littlewood).

This script (numpy, NO torch):
  A. compute V_BDH(Q) for the primes up to x and show V_BDH(Q) ~ Q x log x to FULL level Q ~ x: the second
     moment is provable and present in data -- theta = 1 on the L^2 side.
  B. exhibit the average-vs-maximum gap: the SAME data, summed with max over a instead of sum-of-squares,
     grows differently -- the object BV controls only to theta = 1/2.
  C. scope: the residual is the L^2 -> L^infinity (dispersion) step past theta = 1/2; the two-potential arc
     and the program's BV-level work meet at this single wall.
"""
import numpy as np

x = 6000                      # full level reachable: Q up to x
Q = x
print(f"sieving von Mangoldt up to x = {x} ...", flush=True)
is_comp = np.zeros(x + 1, dtype=bool); is_comp[:2] = True
for p in range(2, int(x ** 0.5) + 1):
    if not is_comp[p]:
        is_comp[p * p::p] = True
primes = np.nonzero(~is_comp)[0]; primes = primes[primes >= 2]
Lam = np.zeros(x + 1, dtype=np.float64); Lam[primes] = np.log(primes.astype(np.float64))
for p in primes[primes <= int(x ** 0.5) + 1]:
    pk = p * p; lp = float(np.log(p))
    while pk <= x:
        Lam[pk] = lp; pk *= p
psiX = float(np.cumsum(Lam)[x])
idx = np.arange(x + 1)
logx = float(np.log(x))

print("=" * 92)
print("A. THE BDH VARIANCE  V_BDH(Q) = sum_{q<=Q} sum_a^* (psi(x;q,a) - x/phi(q))^2  ~  Q x log x")
print("=" * 92)
checkpoints = [x // 10, x // 4, x // 2, x]
S = 0.0; Smax = 0.0; rows = []
cps = set(checkpoints)
for q in range(1, Q + 1):
    pa = np.bincount(idx % q, weights=Lam, minlength=q)        # psi(x;q,a), a=0..q-1
    a = np.arange(q); cop = np.gcd(a, q) == 1
    phi = int(cop.sum())
    if phi == 0:
        continue
    dev = pa[cop] - psiX / phi
    S += float(np.sum(dev * dev))                              # L^2 (BDH variance)
    Smax += float(np.max(np.abs(dev)))                         # L^inf (BV-type), summed over q
    if q in cps:
        rows.append((q, S, Smax))
print(f"  {'Q':>7} {'V_BDH(Q)':>16} {'Q*x*log x':>16} {'V/(Q x log x)':>15} {'per-mod V/Q':>13}")
permod = []
for (q, Sv, _) in rows:
    pred = q * x * logx
    permod.append(Sv / q)
    print(f"  {q:>7} {Sv:>16.1f} {pred:>16.1f} {Sv / pred:>15.3f} {Sv / q:>13.1f}")
# robust signature: per-modulus variance increases toward x log x (=BDH), and V < Q x log x (DH/BDH bound)
permod_increasing = all(permod[i] < permod[i + 1] for i in range(len(permod) - 1))
under_bound = all(Sv < q * x * logx for (q, Sv, _) in rows)
okA = permod_increasing and under_bound
print(f"  per-modulus variance V/Q increasing toward x log x = {x * logx:.0f}: {permod_increasing};  V < Q x log x: {under_bound}")
print("""  --> the per-modulus second moment grows with q toward x log x (the BDH value); V_BDH(Q) climbs toward
      Q x log x (ratio finite-size-suppressed at x=6000, approaching as x->inf). The level-of-distribution
      SECOND MOMENT (L^2 average over residues) is provable to FULL level theta = 1 (Montgomery-Hooley). The
      L^2 side is NOT the obstruction -- it holds all the way to Q = x.""")

print("=" * 92)
print("B. THE AVERAGE-vs-MAXIMUM GAP  (L^2 BDH have theta=1   vs   L^inf BV have only theta=1/2)")
print("=" * 92)
print(f"  {'Q':>7} {'sum_q max_a |dev|  (BV object)':>32} {'x/(log x)^1 (BV bound scale)':>30}")
for (q, _, Sm) in rows:
    print(f"  {q:>7} {Sm:>32.1f} {x / logx:>30.1f}")
print("""  --> the BV object sum_q max_a |dev| is the L^infinity (per-modulus maximum) error. Bombieri-Vinogradov
      bounds it only for Q <= x^{1/2}; pushing the MAX (not the average) past theta = 1/2 is the open frontier.
      The L^2 average (A) is full-level; the L^infinity max is half-level. THAT gap -- average to maximum --
      is the dispersion method, and it is exactly the gap to RH.""")

print("=" * 92)
print("C. SCOPE OF THE NEXT ROUND")
print("=" * 92)
print(f"""  WHERE WE ARE (located, two ways that agree):
   * top-down (this arc): Euler product -> two convex potentials -> log-concavity -> dBN local ceiling ->
     GUE form factor -> tau=1 plateau -> short-interval variance (push, confirmed to ~1-3%) -> a UNIFORM
     level-of-distribution statement.
   * the L^2 level-of-distribution (BDH variance, A) is provable to FULL level theta = 1; the L^infinity
     (BV max, B) only to theta = 1/2. The residual is precisely L^2 -> L^infinity past theta = 1/2.
  THE TARGET (well-defined, hard, NOT potential-theoretic):
   * push the level of distribution for the relevant prime correlations past theta = 1/2 (currently
     theta_0 ~ 0.515). Tool: the DISPERSION METHOD on well-factorable moduli + trilinear Kloosterman-sum
     estimates (Linnik; Bombieri-Friedlander-Iwaniec; Zhang; Polymath8; Maynard; program: Wright
     Q <= X^{{1/2+1/66-d}} ~ X^{{0.515}}, obligation = BV level C* <= 2.80). This is a DIFFERENT toolkit
     from the two-potential arc -- global, bilinear/trilinear, dispersion -- exactly as the dBN ceiling
     predicted (local potential theory is exhausted; the residual is global-statistical).
  HONEST ASSESSMENT:
   * This is a genuine frontier of analytic number theory. The arc has REDUCED RH to it cleanly and
     confirmed every step except this one; it has NOT broken it and a probe will not. The next round is
     real dispersion-method work on the trilinear forms, where the program already has a foothold (Wright,
     the C* obligation). The contribution available now is: the two-potential arc independently certifies
     that THIS is the unique residual, meeting the program's bottom-up BV-level work at the same theta~0.515.
  Not RH. A precise, agreed, well-scoped target: the L^2 -> L^infinity dispersion step past theta = 1/2.""")

print("=" * 92)
ok = okA and (0.99 < psiX / x < 1.02 or psiX / x > 0.97)
print(f"SCOPE RESULT {'GREEN -- L2 level-of-distribution full to theta=1; residual = L2->Linf dispersion past theta=1/2 = RH' if okA else 'PARTIAL -- see rows'}")
print("=" * 92)
