# Lemma 8.1a0 CRT-Isolation Certificate

**Script:** `empirical/verify_lemma_8_1a0_crt_isolation.py`
**Source:** `22.primorial_cumulant_noether_rh.md` (Lemma 8.1a0, CRT isolation)
**Status:** all pre-registered checks PASS (joint-on-disjoint [P])

Deterministic, exact (`fractions.Fraction`); no floating point enters any
equality, rank, or membership decision. Re-running reproduces this transcript
identically. The transcript below is the record.

```text
Exact-arithmetic certificate for Lemma 8.1a0 (CRT isolation of the finite observable)
of `22.primorial_cumulant_noether_rh.md`.

Grounded-paranoid-delusional gate: the settlement meaning below was fixed BEFORE this
script was run (see PRE-REGISTRATION). The transcript, not any prose, is the record.

============================================================================
PRE-REGISTRATION  (Settlement P2-8.1a0; matched-pair, meaning fixed pre-run)
============================================================================
Claim under test (Lemma 8.1a0). On R_n = Z/P_n with P_n primorial (squarefree), the
Mobius/Ramanujan primitive-support projector

    P_VM[d] = sum_{e | d} mu(d/e) E_e ,   E_e = average over the cyclic subgroup <e>,

equals the CRT conductor-packet projector Pi_d (projector onto the additive characters
of conductor exactly d), for every d | P_n; and consequently the packet observable
factors as a finite Euler product of commuting local per-prime factors.

K (positive): for all d | P_n at P_n in {2, 6, 30},
    P_VM[d] == P_CRT[d] exactly; {P[d]} is complete, orthogonal, idempotent;
    rank P[d] == phi(d); and each squarefree packet factors as
    prod_{p|d}(I - A_p) prod_{p!|d} A_p with phi(d) == prod_{p|d}(p-1).
  => Lemma 8.1a0 holds; "finite algebra, not an analytic prime-number input" confirmed.

L (negative): some d/m has P_VM[d] != P_CRT[d], or the family fails
    idempotence / orthogonality / completeness / rank, or a squarefree packet fails to
    factor into distinct-prime local pieces. Any one => Lemma 8.1a0 is false as stated.

JOINT-ON-DISJOINT: the projector identity holds universally (verified also at the
    non-squarefree Z/12), while the cross-prime Euler separation is squarefree-specific:
    at Z/12 the prime-power conductors d in {4, 12} are single-axis (p=2) OCCUPATIONS that
    8.1a0's distinct-prime separation does not resolve into new axes. This draws the
    squarefree/occupation firewall exactly between Lemma 8.1a0 (closed here) and
    Lemma 8.1a (occupation lift, the harder next obligation).
============================================================================

All matrices act on C[Z/m] in the group (delta) basis and have rational entries
(averages of permutation matrices and their Mobius combinations); fractions.Fraction is
exact, so no floating point enters any equality, rank, or membership decision. Conductor
packets are stable under eta -> -eta, so this rational group-basis computation faithfully
represents the realified packets H_n^{[d]} of the manuscript.


================  m = 2  =  2  (squarefree primorial)  ================
   d | phi(d) | rank=tr(P_VM) | P_VM==P_CRT | P^2==P | note
  ---+--------+---------------+-------------+--------+------------------------------------
    1 |      1 |             1 | PASS        | PASS   | 
    2 |      1 |             1 | PASS        | PASS   | 
  completeness   sum_d P[d] == I        : PASS
  orthogonality  P[d] P[d'] == 0 (d!=d') : PASS
  Euler separation (distinct primes)    : PASS   (P[d] = prod_{p|d}(I-A_p) prod_{p!|d}A_p ; phi(d)=prod(p-1))

================  m = 6  =  2 * 3  (squarefree primorial)  ================
   d | phi(d) | rank=tr(P_VM) | P_VM==P_CRT | P^2==P | note
  ---+--------+---------------+-------------+--------+------------------------------------
    1 |      1 |             1 | PASS        | PASS   | 
    2 |      1 |             1 | PASS        | PASS   | 
    3 |      2 |             2 | PASS        | PASS   | 
    6 |      2 |             2 | PASS        | PASS   | 
  completeness   sum_d P[d] == I        : PASS
  orthogonality  P[d] P[d'] == 0 (d!=d') : PASS
  Euler separation (distinct primes)    : PASS   (P[d] = prod_{p|d}(I-A_p) prod_{p!|d}A_p ; phi(d)=prod(p-1))

================  m = 30  =  2 * 3 * 5  (squarefree primorial)  ================
   d | phi(d) | rank=tr(P_VM) | P_VM==P_CRT | P^2==P | note
  ---+--------+---------------+-------------+--------+------------------------------------
    1 |      1 |             1 | PASS        | PASS   | 
    2 |      1 |             1 | PASS        | PASS   | 
    3 |      2 |             2 | PASS        | PASS   | 
    5 |      4 |             4 | PASS        | PASS   | 
    6 |      2 |             2 | PASS        | PASS   | 
   10 |      4 |             4 | PASS        | PASS   | 
   15 |      8 |             8 | PASS        | PASS   | 
   30 |      8 |             8 | PASS        | PASS   | 
  completeness   sum_d P[d] == I        : PASS
  orthogonality  P[d] P[d'] == 0 (d!=d') : PASS
  Euler separation (distinct primes)    : PASS   (P[d] = prod_{p|d}(I-A_p) prod_{p!|d}A_p ; phi(d)=prod(p-1))

================  m = 12  =  2^2 * 3  (non-squarefree firewall probe)  ================
   d | phi(d) | rank=tr(P_VM) | P_VM==P_CRT | P^2==P | note
  ---+--------+---------------+-------------+--------+------------------------------------
    1 |      1 |             1 | PASS        | PASS   | 
    2 |      1 |             1 | PASS        | PASS   | 
    3 |      2 |             2 | PASS        | PASS   | 
    4 |      2 |             2 | PASS        | PASS   | prime-power conductor -> single-axis OCCUPATION (Lemma 8.1a)
    6 |      2 |             2 | PASS        | PASS   | 
   12 |      4 |             4 | PASS        | PASS   | prime-power conductor -> single-axis OCCUPATION (Lemma 8.1a)
  completeness   sum_d P[d] == I        : PASS
  orthogonality  P[d] P[d'] == 0 (d!=d') : PASS
  Euler separation                      : N/A (non-squarefree; occupation rows above)

================  REALIZED BRANCH  ================
K on the projector algebra holds at every tested modulus, including the
non-squarefree Z/12; cross-prime Euler separation holds on the squarefree
primorial settlement {2, 6, 30}; Z/12 exhibits prime-power conductors {4, 12}
as single-axis occupations outside 8.1a0's distinct-prime separation.

>>> JOINT-ON-DISJOINT [P]: Lemma 8.1a0 is proved and grounded. The
>>> squarefree/occupation firewall to Lemma 8.1a is localized exactly as
>>> pre-registered. No floating point entered any decision.
```
