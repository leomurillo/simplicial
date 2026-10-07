# The order-4 selection rule and the Z/30 atlas (the program's named-open quartic computation)

**Script:** `empirical/verify_quartic_selection_z30.py`  (builds on T3, T2, Paper 21, Paper 22).
**Finding:** the order-4 cumulant selection rule is delta_{a+b+c+d=0} MINUS three Wick pairings
delta_{a+b=0}delta_{c+d=0} (verified to machine precision on N=6,8). Order 4 is the FIRST order with
a Gaussian (Wick) subtraction -- the two-tower (Beyond-CBS) split made arithmetic. On Z/30 the
CONNECTED (no-sub-pair) quadruples spanning {2,3,5} are the genuine three-prime obstruction Paper 22
sec 7 named; this extends Paper 22 sec 5.3 (cubic on Z/6) to the quartic row and answers Paper 21's
open question (order 4 IS qualitatively new). NO claim RH is proved; conservation of difficulty holds.
**Nature:** numerical/exact-combinatorial; builds on the corpus, does not reinvent it.

```text
The ORDER-4 selection rule and the Z/30 atlas: the program's own named-open quartic computation
(Paper 21 "what remains" item 5; Paper 22 sec 7), done -- informed by the two-tower (Beyond-CBS) lens.

CONTEXT (not reinventing -- building on the corpus):
  * T3 proved the ORDER-3 selection rule a+b+c=0 (mod N) for the Amari-Chentsov cubic on Z/N
    (additive characters), and Paper 22 sec 5.3 used it to organize the cubic term of the Weil form:
    Q_2(R_2 f) = W_zeta(f*f^*)|_{<=3} on Z/6, recovering the first prime correction sum_{p=2,3} log p.
  * Paper 21 (quartic force law) NAMED the order-4 / three-prime question OPEN: "run the first finite
    atlas on Z/30 ... decide whether the fourth-cumulant case is just more of the same or qualitatively
    new." T2 left Q_{ijkl}=d^4 Phi's form uncomputed ("not needed for what follows").
  * Paper 22 sec 7: Z/30 = Z/2 x Z/3 x Z/5 is "the first row where a genuine three-prime conductor
    class can exist ... the first non-pairwise obstruction."

THE NEW STRUCTURE (this probe's finding, derived + verified):
  the order-4 CUMULANT (connected) selection rule, on non-trivial characters, is
      Q(chi_a,chi_b,chi_c,chi_d)|_u = delta_{a+b+c+d=0}
            - delta_{a+b=0}delta_{c+d=0} - delta_{a+c=0}delta_{b+d=0} - delta_{a+d=0}delta_{b+c=0}.
  Order 3 had NO subtraction (the only 2+1 partition isolates a single index, which vanishes on
  non-trivial chi). Order 4 is the FIRST order with a WICK (pairwise) SUBTRACTION -- the three
  delta_{a+b=0}delta_{c+d=0} pairings are exactly the GAUSSIAN / 2nd-order content (the conductor
  blind spot floor), and the cumulant SUBTRACTS them, leaving the CONNECTED part (a+b+c+d=0 with NO
  vanishing sub-pair) = the genuine beyond-Gaussian 4th-order content. This IS Beyond-CBS's TWO TOWERS
  (distributional cumulant vs Gaussian), realized exactly and arithmetically on the conductor lattice
  -- and it ANSWERS Paper 21's open question: order 4 IS qualitatively new (the first Gaussian subtraction).

THIS PROBE:
  (A) VERIFY the order-4 selection rule on N=6,8: build Q_{ijkl}|_u by the moment-cumulant partition
      formula (uniform categorical moments M(block)=1/N iff all-equal), contract on characters, confirm
      it equals connected - Wick to machine precision.
  (B) The Z/30 ATLAS: conductor packets, and the CONNECTED quadruples (a+b+c+d=0, no sub-pair=0),
      classified by conductor multiset -- isolating the genuine THREE-PRIME quadruples (the first
      non-pairwise obstruction Paper 22 sec 7 named).
  (C) the two-tower reading + the Weil-form (Paper 22) connection + honest residual.

NUMERICAL (numpy/exact-combinatorial); builds on T3/T2/21/22; NO claim RH is proved.

================  PART A: verify the order-4 cumulant selection rule on N=6, N=8  ============
  N=6: contracted Q_{ijkl}|_u vs (delta_{sum=0} - 3 Wick pairings) over 625 nontrivial quadruples; max|diff| = 8.76e-15  MATCH
  N=8: contracted Q_{ijkl}|_u vs (delta_{sum=0} - 3 Wick pairings) over 2401 nontrivial quadruples; max|diff| = 1.24e-14  MATCH
  => the order-4 cumulant selection rule is CONFIRMED: connected (a+b+c+d=0) MINUS the three
     Gaussian Wick pairings (a+b=0,c+d=0). Order 3 (T3) had NO subtraction; order 4 is the FIRST
     order carrying the Gaussian/2nd-order floor as an explicit subtraction -- the two towers, arithmetic.

================  PART B: the Z/30 = Z/2 x Z/3 x Z/5 atlas (the three-prime row)  ============
  conductor packets H_d (d|30, d>1):  d : dim phi(d) : primes(d)
     H_2  : dim 1 : primes [2] : k in [15]
     H_3  : dim 2 : primes [3] : k in [10, 20]
     H_5  : dim 4 : primes [5] : k in [6, 12, 18, 24]
     H_6  : dim 2 : primes [2, 3] : k in [5, 25]
     H_10 : dim 4 : primes [2, 5] : k in [3, 9, 21, 27]
     H_15 : dim 8 : primes [3, 5] : k in [2, 4, 8, 14, 16, 22, 26, 28]
     H_30 : dim 8 : primes [2, 3, 5] : k in [1, 7, 11, 13, 17, 19, 23, 29]

  enumerating quadruples a+b+c+d=0 (mod 30), a,b,c,d in {1..29}, up to ordering...
  quadruples with a+b+c+d=0 (unordered): 1202 total
     WICK-reducible (some sub-pair=0; Gaussian/2nd-order, conductor-blind-spot floor): 120
     CONNECTED (no sub-pair=0; genuine 4th-order, beyond-Gaussian): 1082

  CONNECTED quadruples by the prime-set their four conductors span (the cross-prime reach):
     primes [5]          : 4 connected quadruples
     primes [2, 3]       : 6 connected quadruples
     primes [2, 5]       : 32 connected quadruples
     primes [3, 5]       : 126 connected quadruples
     primes [2, 3, 5]    : 914 connected quadruples
  => the {2,3,5} rows are GENUINE THREE-PRIME obstructions: connected order-4 vertices that
     couple all three primes and are NOT reducible to a Gaussian pairing or a pairwise (two-prime)
     face -- exactly the 'first non-pairwise obstruction' Paper 22 sec 7 named, now counted.
  sample three-prime connected quadruples (indices ; their conductors):
     (1, 1, 1, 27) ; conductors (30, 30, 30, 10)
     (1, 1, 2, 26) ; conductors (30, 30, 15, 15)
     (1, 1, 3, 25) ; conductors (30, 30, 10, 6)
     (1, 1, 4, 24) ; conductors (30, 30, 15, 5)
     (1, 1, 5, 23) ; conductors (30, 30, 6, 30)
     (1, 1, 6, 22) ; conductors (30, 30, 5, 15)

================  PART C: reading + Paper 22 Weil connection + honest residual  ==============
TWO-TOWER (Beyond-CBS), arithmetic and exact:
  * the WICK-reducible quadruples (delta_{a+b=0}delta_{c+d=0}) are the GAUSSIAN / 2nd-order
    content -- the conductor-blind-spot floor; a 2nd-moment / symmetric instrument sees only these.
  * the CONNECTED quadruples are the genuine 4th-CUMULANT (beyond-Gaussian) content; the cumulant
    Q SUBTRACTS the Wick part, isolating them. Order 4 is the FIRST order with this split (order 3
    is pure-connected) -- the arithmetic realization of 'the two towers coincide only at the Gaussian'.
  * ANSWERS Paper 21's open question: the fourth-cumulant case IS qualitatively new -- the first
    Gaussian (Wick) subtraction -- and on Z/30 it produces genuine THREE-PRIME connected vertices.

PAPER 22 (the program's RH route) connection:
  Paper 22 sec 5.3: the ORDER-3 selection rule organizes Q_2 = W_zeta(f*f^*)|_{<=3} on Z/6,
  recovering the first prime correction sum_{p=2,3} log p. The ORDER-4 atlas here is the next
  truncation W_zeta(f*f^*)|_{<=4} on Z/30: the connected three-prime quadruples carry the genuine
  quartic prime-interaction content (p=5 enters; the non-pairwise term), while the Wick part
  reproduces the Gaussian/2nd-order (archimedean main + pairwise) piece already present at order 2.
  This EXTENDS Paper 22 sec 5.3 from cubic to quartic -- the computation Papers 21/22 named open.

HONEST RESIDUAL (tiered):
  [P] the order-4 selection rule (connected - 3 Wick pairings), verified to machine precision; the
      Z/30 packet atlas and the connected/three-prime quadruple counts (exact combinatorics).
  [A] the two-tower reading (Wick=Gaussian floor, connected=beyond-Gaussian) and the Weil-truncation
      placement W_zeta|_{<=4}; the claim that order 4 is the first Gaussian-subtraction order.
  [open == RH] this is one more finite row of Paper 22's tower; positivity/boundedness here is the
      order-4 instance, NOT a proof of RH. Conservation of difficulty holds: the all-order limit
      (Paper 22 Conjecture 5.2: von Mangoldt recovery + Archimedean Noether Limit + leakage
      extinction) remains the hard step. The NEW content is the qualitative order-4 structure (the
      Wick split / three-prime obstruction), answering Paper 21 and feeding Paper 22's quartic row.
```
