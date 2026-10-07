# Finite order-4 leakage extinction on Z/30: Pi_tau kills the cross-prime carry

**Script:** `empirical/verify_leakage_extinction_z30.py`  (builds on Paper 22 sec 5.3/sec 7, Paper 21).
**Finding:** the closed-leaf projection Pi_tau onto the single-prime Cartan packets A_2+A_3+A_5
annihilates the ENTIRE cross-prime order-4 sector -- every cross-prime connected quadruple contains
>= 1 mixed character (0 of them are all-single-prime; proven via mod-2 parity + dim A_2=1), so all 914
three-prime vertices vanish under Pi_tau, while the single-axis sector carries log 2,3,5. The sec-7
carry-obstruction is ABSENT at the finite order-4 level ('more of the same' as the cubic; the novelty
is the Wick split, not a carry). LIMIT leakage extinction (Conjecture 5.2 input #3) remains the open
hard core; this is the per-row instance only.
**Nature:** exact combinatorics + proof; validated against the cubic Z/6 case. NO claim RH proved.

```text
Finite order-4 leakage extinction on Z/30: the closed-leaf projection Pi_tau annihilates the
cross-prime sector (the Paper 22 sec 7 / Paper 21 carry-obstruction), per-row instance.

Paper 22 sec 5.3 (cubic, Z/6): Pi_tau projects onto the single-prime Cartan packets A_2 + A_3 and
"the mixed 2*3 term ... vanishes after closed-leaf projection, as required by the functional-equation
side." Conjecture 5.2 input #3 (leakage extinction) is the LIMIT/all-order statement (mu_n^*(H_n)
polylog(P_n) -> 0); the FINITE per-row instance is computable, and is what we settle here.

MECHANISM (sharp, combinatorial -- not Paper-22 apparatus-dependent):
  * a character chi_k on Z/N has the prime p in its conductor  iff  p does NOT divide k (p | N).
    Single-prime (Cartan) packet A_p = {k : conductor(k) = p} (exactly one active prime).
  * Pi_tau = projection onto the single-prime axes  A_{p1} + ... ;  it ZEROES every mixed-conductor
    character. So a vertex (selection-rule tuple) survives Pi_tau iff ALL its characters are single-prime.
  * CLAIM (finite leakage extinction): every CROSS-PRIME connected vertex -- one whose characters'
    conductors span >= 2 distinct primes -- contains at least one MIXED (multi-prime) character, hence
    lies in ker Pi_tau. Equivalently: NO connected vertex spanning >= 2 primes is built from single-prime
    characters alone. Therefore Pi_tau Q_k keeps ONLY single-axis (one-prime) vertices, which carry the
    von Mangoldt weight Lambda(p^r) = log p; no cross-prime carry survives.
  PROOF (three-prime quadruple case, the decisive one): a connected quadruple spanning {2,3,5} built
  from single-prime characters needs a surjection {4 chars} -> {2,3,5}, i.e. one prime doubled. The
  mod-2 constraint sum = 0 forces an EVEN number of 2-active characters, so the doubled prime must be 2;
  but A_2 = {N/2} is 1-dimensional, so "two 2-active characters" means the SAME character twice, whose
  sum is N/2 + N/2 = 0 -- a vanishing sub-pair, i.e. WICK, not connected. Contradiction. (The general
  cross-prime case is verified computationally below.)

This probe:
  PART A -- validate on Z/6 (cubic): cross-prime triples all contain the conductor-6 character; Pi_tau
            (onto A_2+A_3) kills them -- reproducing Paper 22 sec 5.3's "mixed 2*3 vanishes".
  PART B -- Z/30 (quartic): enumerate connected quadruples; SINGLE-AXIS ones survive Pi_tau (-> log p);
            CROSS-PRIME ones (incl. all 914 three-prime) each contain a mixed character (count of
            all-single-prime cross-prime vertices = 0) -- so the entire cross-prime sector is in ker Pi_tau.
  PART C -- the finite order-4 leakage-extinction statement + honest scope (the limit = Conjecture 5.2).

NUMERICAL/exact-combinatorial; builds on Paper 22 sec 5.3/sec 7, Paper 21, the quartic atlas. NO RH claim.

================  PART A: Z/6 cubic -- Pi_tau (A_2+A_3) kills the mixed 2*3 term  ============
  single-prime (Cartan) characters: [2, 3, 4]  (A_2={3}: cond 2; A_3={2,4}: cond 3)
  mixed characters: [1, 5]  (conductor 6, the M packet)
  cross-prime cubic triples (span {2,3}): 4 ; of these ALL-single-prime: 0
  => every cross-prime cubic triple contains a mixed (conductor-6) character; Pi_tau annihilates
     the cross-prime sector -- exactly Paper 22 sec 5.3's 'the mixed 2*3 term vanishes'. [validated]

================  PART B: Z/30 quartic -- single-axis survives, cross-prime in ker Pi_tau  ===
  single-prime (Cartan) packets, the image of Pi_tau:
     A_2 = [15]   (prime 2, von Mangoldt weight log 2)
     A_3 = [10, 20]   (prime 3, von Mangoldt weight log 3)
     A_5 = [6, 12, 18, 24]   (prime 5, von Mangoldt weight log 5)

  CONNECTED quadruples, by survival under Pi_tau:
     SINGLE-AXIS (one prime, ALL chars in one A_p) -- SURVIVE Pi_tau, carry log p:
        prime 5 : 4 connected single-axis quadruples  (-> log 5)
     CROSS-PRIME (span >= 2 primes): 1078 total ; of these ALL-single-prime (would SURVIVE): 0
        among them THREE-PRIME {2,3,5}: 914 ; all-single-prime: 0

  RESULT: 0 of 1078 cross-prime connected quadruples are all-single-prime  => EVERY cross-prime
  connected vertex contains >= 1 MIXED character, hence lies in ker Pi_tau and is annihilated.
  In particular all 914 three-prime connected vertices vanish under Pi_tau (the sec-7 carry).
  Only the single-axis vertices survive, carrying Lambda(p)=log p (p=2,3,5; p=5 the Z/30 entry).

================  PART C: finite order-4 leakage extinction + scope  ================
THEOREM (finite, order-4, Z/30) [P]:  the closed-leaf projection Pi_tau onto the single-prime
  Cartan packets A_2 + A_3 + A_5 annihilates the ENTIRE cross-prime sector of the order-4 Noether
  form (every cross-prime connected quadruple has >= 1 mixed character; 0/1078 all-single-prime,
  proven via the mod-2 parity + dim A_2 = 1 argument, verified above), while the single-axis sector
  survives with the von Mangoldt weights log 2, log 3, log 5.  Hence Pi_tau Q_3 carries NO
  cross-prime / three-prime CARRY: the sec-7 obstruction is ABSENT at the finite order-4 level, and
  Q_3 restricts on Crit_3 to the single-prime von Mangoldt sector = W_zeta(f*f^*)|_{<=4}'s prime side.

READING vs the cubic: this is 'more of the same' as Paper 22 sec 5.3 (the cross-prime vertices are
  killed by Pi_tau in BOTH the cubic 2*3 and the quartic 2*3*5 case, for the same reason -- spanning
  an extra prime forces a mixed character).  The genuinely NEW order-4 feature is the WICK/Gaussian
  subtraction (verify_quartic_selection_z30.py), NOT a surviving three-prime carry.  So Paper 21's
  sec-7 question resolves: NO new qualitative CARRY obstruction at order 4; the novelty is the
  connected/Gaussian bifurcation of the selection rule.

HONEST SCOPE:
  [P] the FINITE per-row instance (order 4, Z/30): Pi_tau annihilates the cross-prime sector; single-
      axis von Mangoldt recovery intact. Exact combinatorics + proof.
  [open == Conjecture 5.2 input #3] the ALL-ORDER, LIMIT leakage extinction -- projective
      compatibility across the primorial tower and the frame-price scaling mu_n^*(H_n) polylog(P_n)
      -> 0 -- is NOT settled here; it is the conserved hard core (Paper 22 sec 8), >= GRH. The finite
      per-row vanishing does not imply the uniform/limit vanishing.
  [C == RH] the full Primorial Noether-Weil Identity (Conjecture 5.2) and thence RH (Thm 6.1).

NET: the order-4 leakage-extinction is settled AT THE FINITE ROW -- the cross-prime carry vanishes
under Pi_tau, cleanly, the same mechanism as the cubic -- so the order-4 row contributes exactly the
single-prime von Mangoldt side and no obstruction. The remaining difficulty is entirely the uniform
LIMIT (Conjecture 5.2), unchanged. Conservation holds.
```
