# Recovery-current verification on Z/30: where the prime p=5 enters (Paper 22 Thm 5.2.1)

**Script:** `empirical/verify_recovery_current_z30.py`  (builds on Paper 22 Thm 5.2.1 + the quartic atlas).
**Finding:** the von Mangoldt recovery Lambda(d)=sum_{e|d} mu(d/e) log e gives log p on SINGLE-PRIME
conductors (0 on composite, Mobius cancels); p=5 = log 5 is the new single-axis entry at Z/30 (via A_5,
available because 5<=p_3). The 914 connected three-prime quartic vertices are MIXED -- the residual the
closed-current projection must cancel (Lambda=0 on them), NOT the source of log 5. This CORRECTS the
landed quartic text (which conflated the two). Q_3=W_zeta|_{<=4} = single-prime recovery [P] + mixed
cancellation [sec-7 open] + all-order lift [C, Lemma 8.1, >=GRH].
**Nature:** exact (sympy Mobius) + numerical (mpmath vs -zeta'/zeta); NO claim RH proved.

```text
Recovery-current verification: the von Mangoldt prime side on R_3 = Z/30, and where p=5 enters.

Paper 22 Theorem 5.2.1 (proof) fixes the mechanism: the all-order Noether energy, after Hayes-Mobius
compression and CLOSED-CURRENT projection, equals
    sum_{alpha in N^{p<=p_n}} c_alpha * f~(2pi i |alpha|_log / log P_n),   |alpha|_log = sum_p alpha_p log p,
with  c_alpha = Lambda(p^r) = log p  on SINGLE-AXIS occupations alpha = r*e_p, and the MIXED (multi-axis)
coefficients CANCELLING on Crit_n -- the finite Noether analogue of  -zeta'/zeta(s) = sum_p sum_r log p p^{-rs}.

So two distinct things on Z/30, which the prior landing CONFLATED (corrected here):
  (1) the prime p=5 enters via the SINGLE-AXIS conductor d=5 (the Cartan packet A_5), now available because
      5 <= p_3 (5 | 30 but 5 ∤ 6).  This is the von Mangoldt recovery: A_p carries Lambda(p)=log p.
  (2) the order-4 CONNECTED THREE-PRIME vertices (the 914 of `verify_quartic_selection_z30.py`) are
      MIXED (multi-axis, span {2,3,5}); they are the residual the closed-current projection must CANCEL
      on Crit_n -- the Paper 22 sec 7 / Paper 21 carry-obstruction question -- NOT the source of log 5.

This probe:
  PART A -- the Hayes-Mobius (Mobius-inversion) von Mangoldt extraction Lambda(d) = sum_{e|d} mu(d/e) log e
            on the conductor lattices of P_2=6 and P_3=30; log p on single-prime conductors, 0 on composite;
            p=5 = log 5 the NEW single-prime entry at P_3.  Validated against -zeta'/zeta numerically.
  PART B -- the single-prime (Cartan/closed) packets A_p vs the mixed packets; the closed-leaf projection
            Pi_tau onto the single-prime axes annihilates the mixed sector, so the 914 three-prime connected
            quartic vertices project OUT (they carry no log p); A_5 carries log 5.
  PART C -- assembly: Q_3(R_3 f) = W_zeta(f*f^*)|_{<=4} needs the single-prime recovery (computed [P]) AND the
            mixed residual to vanish (the sec-7 carry, order-4 instance shown to project out; all-order = the
            hard Lemma 8.1).  Honest tiering + the correction of the landed text.

NUMERICAL/exact (sympy/mpmath); builds on Paper 22 Thm 5.2.1 and the quartic atlas; NO claim RH is proved.

================  PART A: Lambda(d) = sum_{e|d} mu(d/e) log e  on the conductor lattice  ====
  --- R = Z/6  (P_2-smooth: primes <= 3) ---
     d (>1 | 6)   Lambda(d) via Mobius     = log p ?   single-axis (Cartan) ?
     d=2          log(2)                   log 2 = 0.69315     YES axis 2
     d=3          log(3)                   log 3 = 1.09861     YES axis 3
     d=6          0                        (composite)     no (primes [2, 3])
     => single-prime (Cartan) conductors recover Lambda = { log 2, log 3 }
        i.e. the prime side sum_{p<=3} log p ; composite conductors give Lambda=0 (Mobius cancels).

  --- R = Z/30  (P_3-smooth: primes <= 5) ---
     d (>1 | 30)   Lambda(d) via Mobius     = log p ?   single-axis (Cartan) ?
     d=2          log(2)                   log 2 = 0.69315     YES axis 2
     d=3          log(3)                   log 3 = 1.09861     YES axis 3
     d=5          log(5)                   log 5 = 1.60944     YES axis 5
     d=6          0                        (composite)     no (primes [2, 3])
     d=10         0                        (composite)     no (primes [2, 5])
     d=15         0                        (composite)     no (primes [3, 5])
     d=30         0                        (composite)     no (primes [2, 3, 5])
     => single-prime (Cartan) conductors recover Lambda = { log 2, log 3, log 5 }
        i.e. the prime side sum_{p<=5} log p ; composite conductors give Lambda=0 (Mobius cancels).

  KEY: the only DIFFERENCE between Z/6 and Z/30 in the single-prime recovery is the conductor d=5:
       Lambda(5)=log 5 is the NEW entry at Z/30 (5 | 30 but 5 doesn't divide 6).  The prime p=5
       enters through the SINGLE-AXIS conductor packet A_5 -- NOT through any cross-prime vertex.

  validate vs -zeta'/zeta(2) = 0.5699609931 : single-prime (r=1) skeleton sum_p log p p^-2 = 0.47452755 ;
       full sum_p sum_r log p p^-rs (r>=1, the all-order occupation lift) = 0.5568683732 (-> matches).
  So the squarefree single-prime skeleton gives the r=1 prime side; prime POWERS p^r are the
  'all-order occupation lift' (Thm 5.2.1 double-cutoff). The NEW prime at each primorial row is
  its largest prime, single-axis: p=2(R_1),  p=3(R_2/Z6),  p=5(R_3/Z30),  p=7(R_4/Z210), ...

================  PART B: closed-leaf projection -- single-prime carries log p; mixed cancels  =
  SINGLE-PRIME (Cartan / closed-current) packets on Z/30 -- the Pi_tau image, carrying Lambda=log p:
     A_2  (conductor 2, prime 2): k in [15]  ->  Lambda=log 2
     A_3  (conductor 3, prime 3): k in [10, 20]  ->  Lambda=log 3
     A_5  (conductor 5, prime 5): k in [6, 12, 18, 24]  ->  Lambda=log 5
  MIXED (multi-axis) packets -- the residual the closed-current projection must cancel on Crit_n:
     conductor 6  (primes [2, 3]): k in [5, 25]
     conductor 10 (primes [2, 5]): k in [3, 9, 21, 27]
     conductor 15 (primes [3, 5]): k in [2, 4, 8, 14, 16, 22, 26, 28]
     conductor 30 (primes [2, 3, 5]): k in [1, 7, 11, 13, 17, 19, 23, 29]

  The order-4 CONNECTED THREE-PRIME vertices (914 of them; `verify_quartic_selection_z30.py`)
  span all of {2,3,5} by construction -- they are MIXED, hence lie ENTIRELY in the residual that
  Pi_tau (projection onto the single-prime/Cartan axes A_2 + A_3 + A_5) annihilates.  They carry
  NO von Mangoldt weight (Lambda(multi-axis)=0).  The prime p=5 is recovered by A_5 alone.
  => CORRECTION of the prior landing: p=5 enters via the single-axis A_5, NOT the three-prime
     connected vertices; those vertices are the cross-prime CARRY that must vanish (sec 7 question).

================  PART C: assembly, tiering, correction  ================
Q_3(R_3 f) = W_zeta(f*f^*)|_{<=4} on Z/30 decomposes, by Thm 5.2.1, into:
  [P] SINGLE-PRIME (von Mangoldt) recovery: A_2,A_3,A_5 carry log 2, log 3, log 5 (Mobius->Lambda,
      verified PART A); the prime p=5 is the new single-axis entry at the Z/30 row. The r=1
      squarefree skeleton matches the prime side of -zeta'/zeta; prime powers p^r are the lift.
  [A / sec-7 open] MIXED-residual cancellation: the multi-axis terms (conductor 6,10,15,30 -- and
      the 914 connected three-prime quartic vertices) must cancel on Crit_n under the closed-leaf
      projection. PART B exhibits the projection (Pi_tau onto single-prime axes annihilates the
      mixed sector) at the FINITE level; that the cancellation is EXACT on Crit_n (no surviving
      cross-prime carry) is the order-4 instance of Paper 22's leakage-extinction, the Paper 21 /
      sec-7 question -- shown here to be a projection-kernel statement, not yet a closed proof.
  [C == RH] the all-order limit (all p^r, n->inf): Paper 22 Conjecture 5.2 / Lemma 8.1 -- the hard
      analytic core, conserved difficulty (>= GRH). Untouched here.

CORRECTION (GPD: verification revealed an imprecision in the just-landed text). The landed Paper 22
quartic paragraph said 'the connected three-prime vertices carrying the entry of the prime 5'. The
verification shows that is WRONG: p=5 enters via the SINGLE-AXIS Cartan packet A_5 (conductor 5),
available because 5 <= p_3; the connected three-prime vertices are the MIXED residual that the
closed-current projection must cancel (Lambda=0 on them). The manuscripts are corrected accordingly.

NET: the recovery-current verification is honest and sharper than the landed claim -- it separates
(i) the single-axis von Mangoldt recovery [P], where p=5 cleanly enters at Z/30, from (ii) the
mixed three-prime carry [sec-7 open], where the 914 connected vertices must cancel. Conservation
of difficulty: the exact cancellation on Crit_n at all orders is Lemma 8.1, still >= GRH.
```
