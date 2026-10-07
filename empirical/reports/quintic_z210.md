# The quintic row Z/210: general cross-prime cancellation, order-5 Wick structure, p=7 entry

**Script:** `empirical/verify_quintic_z210.py`  (works around the mu_210 memory block via the 13
single-prime characters + a general theorem; builds on Paper 22 sec 5.3/sec 7 and the quartic probes).
**Finding:** a GENERAL theorem -- no connected single-prime tuple (any order, any squarefree primorial)
spans >= 2 primes -- so Pi_tau annihilates the cross-prime sector at EVERY order/row, subsuming the cubic
and quartic results. Spot-checked: 0 connected cross-prime single-prime tuples on Z/6, Z/30, Z/210 (orders
3-5). p=7 = log 7 the new single-axis entry at Z/210. Order-5 Wick subtraction = Gaussian pair x
Amari-Chentsov triple (verified N=6). sec-7 coherence: all three-prime obstructions vanish coherently;
no four-prime carry. ALL-ORDER LIMIT (Conjecture 5.2) untouched; mu_210 full energy not needed/blocked.
**Nature:** exact-combinatorial + general proof + numerical (order-5 formula). NO claim RH proved.

```text
The quintic row R_4 = Z/210 (adds p=7): the cross-prime cancellation generalized to ALL orders/rows,
the order-5 Wick structure (Gaussian pair x Amari-Chentsov triple), and the p=7 von Mangoldt entry.

Works AROUND the mu_210 memory block: the full order-5 energy on Z/210 is 210^5 ~ 4e11 (blocked), but the
sec-7 cancellation question only needs the SINGLE-PRIME characters -- 1+2+4+6 = 13 of them -- and the
cubic/quartic pattern generalizes to a theorem proved without any large enumeration:

  GENERAL CROSS-PRIME CANCELLATION THEOREM.  Let N be squarefree (a primorial). A single-prime (Cartan)
  character on axis p is == 0 mod q for every other prime q | N and != 0 mod p.  Then NO connected vertex
  (sum == 0 mod N, no proper subset == 0 mod N), of ANY order, built from single-prime characters can span
  >= 2 primes.  PROOF: if it spans axes p_1,...,p_m (m>=2), the chars on axis p_1 form a non-empty PROPER
  subset; their sum is == 0 mod p_1 (the full sum is, and only axis-p_1 chars are nonzero mod p_1) and == 0
  mod q for q != p_1 (single-prime), hence == 0 mod N by CRT -- a vanishing proper subset, contradicting
  connectivity.  []  Consequently the closed-leaf projection Pi_tau (onto the single-prime Cartan axes)
  annihilates the ENTIRE cross-prime sector at EVERY order and EVERY primorial row -- the sec-7 carry
  vanishes uniformly (cubic Z/6, quartic Z/30, quintic Z/210, ...), subsuming Paper 22 sec 5.3 and the
  quartic result into one statement.

This probe:
  PART A -- the theorem, spot-checked: enumerate single-prime tuples (multisets) on Z/6, Z/30, Z/210 at
            orders 3,4,5; confirm 0 connected cross-prime.  Von Mangoldt single-axis recovery (Lambda via
            Mobius): p=2,3,5,7 -> log p on Z/210; p=7 the NEW entry; the single-axis connected quintets in
            A_7 carry log 7.
  PART B -- the order-5 cumulant selection rule (verified on N=6): kappa_5 = delta_{a+b+c+d+e=0}
            - sum_{10 pairs} delta_{pair=0} delta_{triple=0} -- the first order whose Wick subtraction is a
            GAUSSIAN PAIR x AMARI-CHENTSOV TRIPLE (order 2 x order 3), not pair x pair.
  PART C -- the sec-7 'triple-face coherence' answer + honest scope.

NUMERICAL/exact-combinatorial; builds on Paper 22 sec 5.3/sec 7, the quartic atlas/leakage probes. NO RH claim.

================  PART A: general cross-prime cancellation -- spot-check + von Mangoldt  ======
  --- Z/6 : single-prime (Cartan) characters by axis ---
     A_2 (dim 1): [3]
     A_3 (dim 2): [2, 4]
     connected CROSS-PRIME single-prime tuples (orders 3-5): 0  (theorem: must be 0)
     connected SINGLE-AXIS single-prime tuples that SURVIVE Pi_tau (carry log p):
        order 3, axis 3 : 2  (-> log 3)

  --- Z/30 : single-prime (Cartan) characters by axis ---
     A_2 (dim 1): [15]
     A_3 (dim 2): [10, 20]
     A_5 (dim 4): [6, 12, 18, 24]
     connected CROSS-PRIME single-prime tuples (orders 3-5): 0  (theorem: must be 0)
     connected SINGLE-AXIS single-prime tuples that SURVIVE Pi_tau (carry log p):
        order 3, axis 3 : 2  (-> log 3)
        order 3, axis 5 : 4  (-> log 5)
        order 4, axis 5 : 4  (-> log 5)
        order 5, axis 5 : 4  (-> log 5)

  --- Z/210 : single-prime (Cartan) characters by axis ---
     A_2 (dim 1): [105]
     A_3 (dim 2): [70, 140]
     A_5 (dim 4): [42, 84, 126, 168]
     A_7 (dim 6): [30, 60, 90, 120, 150, 180]
     connected CROSS-PRIME single-prime tuples (orders 3-5): 0  (theorem: must be 0)
     connected SINGLE-AXIS single-prime tuples that SURVIVE Pi_tau (carry log p):
        order 3, axis 3 : 2  (-> log 3)
        order 3, axis 5 : 4  (-> log 5)
        order 3, axis 7 : 8  (-> log 7)
        order 4, axis 5 : 4  (-> log 5)
        order 4, axis 7 : 12  (-> log 7)
        order 5, axis 5 : 4  (-> log 5)
        order 5, axis 7 : 12  (-> log 7)

  => 0 connected cross-prime single-prime tuples on every row -- the theorem holds; Pi_tau
     annihilates the cross-prime sector at orders 3,4,5 on Z/6, Z/30, AND Z/210.  In particular
     the quintic four-prime row Z/210 adds NO new surviving carry: 'more of the same'.

  von Mangoldt recovery Lambda(d)=sum_{e|d} mu(d/e) log e on the conductor lattice of 210:
     A_2 : Lambda = log 2 = 0.69315   (single-axis, survives Pi_tau)
     A_3 : Lambda = log 3 = 1.09861   (single-axis, survives Pi_tau)
     A_5 : Lambda = log 5 = 1.60944   (single-axis, survives Pi_tau)
     A_7 : Lambda = log 7 = 1.94591   (single-axis, survives Pi_tau)
     composite conductors (6,10,...,210): Lambda = 0 (Mobius cancels) -- the mixed residual.
     single-prime recovery on Z/210 = { log 2, log 3, log 5, log 7 };  p=7 (log 7) is the NEW entry at the four-prime row.

================  PART B: order-5 cumulant selection rule (verified on N=6)  ==================
  Bell(5) = 52 set-partitions; non-singleton ones (survive on H_0): full (1) + 3+2 (10) = 11.
  kappa_5 contracted vs  delta_{a+b+c+d+e=0} - sum_{10 pairs} delta_{pair=0} delta_{triple=0} :
     over 300 random non-trivial 5-tuples, max|diff| = 2.03e-14  MATCH
  => the order-5 Wick subtraction is the 3+2 partition: a GAUSSIAN PAIR (order 2) times an
     AMARI-CHENTSOV TRIPLE (order 3).  Order 5 is the first order whose disconnected part
     contains the CUBIC -- the cumulant tower's order-2 and order-3 content meeting in one rung
     (cf. order 4, whose only Wick term was pair x pair = Gaussian x Gaussian).

================  PART C: sec-7 triple-face coherence + scope  ================
Paper 22 sec 7 asks, at the quintic four-prime row Z/210, whether the three-prime obstructions
compose 'coherently across the divisor lattice' -- the four triple-faces 30, 42, 70, 105
(=2*3*5, 2*3*7, 2*5*7, 3*5*7).  ANSWER (general theorem, PART A): every cross-prime connected
vertex -- on any triple-face, on the full 210, at any order -- contains a mixed character and
lies in ker Pi_tau.  So ALL the three-prime obstructions vanish, COHERENTLY and uniformly; there
is no surviving four-prime carry.  The composition is trivial-by-cancellation, not a new obstruction.

HONEST SCOPE:
  [P] the finite cross-prime cancellation is now GENERAL: Pi_tau annihilates the cross-prime
      sector at every order and every primorial row (one proof, PART A), subsuming the cubic
      (Paper 22 sec 5.3) and quartic results; the quintic Z/210 confirms it and adds log 7.
  [P] order-5 cumulant structure: the 3+2 (Gaussian pair x cubic triple) Wick subtraction, verified.
  [open == Conjecture 5.2] the ALL-ORDER LIMIT (projective compatibility + mu_n^*(H_n)polylog->0
      across n->inf) is untouched -- the conserved hard core, >= GRH.  The general FINITE theorem
      does NOT give the uniform limit; it removes the cross-prime CARRY worry uniformly, leaving
      the limit as the sole obstruction (as Paper 22 sec 8 already states).
  [C == RH] the full identity and Thm 6.1.
  NOTE: the full order-5 Noether ENERGY on Z/210 (mu_210, 210^5) is memory-blocked and NOT
        computed here; the cancellation needed only the 13 single-prime characters + the theorem.

NET: the quintic row contributes no new carry (general theorem); p=7 enters single-axis; the new
structural feature is the order-5 Gaussian-x-cubic Wick term.  The cross-prime carry-obstruction is
now closed UNIFORMLY across the primorial tower at finite order; the entire residual difficulty is
the all-order limit (Conjecture 5.2), unchanged.  Conservation holds.
```
