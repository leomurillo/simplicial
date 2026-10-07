# Lemma 8.1a Occupation-Lift Audit

**Script:** `empirical/verify_lemma_8_1a_occupation_lift.py`
**Source:** `22.primorial_cumulant_noether_rh.md` (Lemma 8.1a, occupation lift)
**Status:** joint-on-disjoint realized — squarefree skeleton [P]; occupation lift is external, not bookkeeping

Deterministic, exact (integers / `Counter` multisets); no floating point enters any
conductor, support, equality, or counting decision. Re-running reproduces this
transcript identically. The transcript below is the record.

```text
Exact-arithmetic audit of Lemma 8.1a (occupation lift from squarefree axes)
of `22.primorial_cumulant_noether_rh.md`.

Grounded-paranoid-delusional gate: the settlement meaning below was fixed BEFORE this
script was run (see PRE-REGISTRATION). The transcript, not any prose, is the record.

Lemma 8.1a was "still to be written out" in the source; this audit writes out its testable
content and decides its true shape.

============================================================================
PRE-REGISTRATION  (Audit of Lemma 8.1a; matched-pair, meaning fixed pre-run)
============================================================================
The von Mangoldt target sum is indexed by the OCCUPATION lattice N^{p<=p_n}: the prime
power p^r is the occupation k = r*e_p, at position r*log p, with weight Lambda(p^r)=log p.
The finite recovery datum and its additive convolutions are indexed by the SQUAREFREE
additive dual \hat R_n = prod F_p (conductors are radicals). Lemma 8.1a asserts that the
single-axis prime-power ladder with weight log p is "remaining algebraic bookkeeping"
over the squarefree axes.

K (positive, the paper's framing): the single-axis prime-power ladder {p^r : r>=1} with
    constant von Mangoldt weight log p is a function of the squarefree additive datum on
    R_n, recoverable by finite conductor-convolution bookkeeping.

L (negative, the split): occupation depth r is NOT a function of the additive characters
    of R_n. Additive convolution on axis F_p wraps mod p, and the radical map
    N^P -> {squarefree divisors}, k -> rad(prod p^{k_p}), forgets all depths (infinite
    fibers). So the prime-power ladder {p^r} cannot be recovered from the squarefree
    additive data; the occupation lift to N^P is strictly additional structure (the
    Thm 5.2.1 "double cutoff" hypothesis), NOT squarefree bookkeeping.

JOINT-ON-DISJOINT: K on the squarefree skeleton + mixed-axis separation (the radical /
    which-axes-lit content IS recoverable, finite algebra, consistent with the R=30
    triple-mixing certificate), and L on the occupation depth (the p^r ladder is not).
    This draws the firewall exactly at "squarefree axis skeleton (finite, on \hat R_n)
    vs prime-power occupation lift (external, on N^P)" -- the line the source's own
    Claim-Hygiene paragraph and Thm 5.2.1 double-cutoff hypothesis already point at.
============================================================================

All arithmetic is exact (integers, multiset Counters, modular sums); no floating point
enters any conductor, equality, support, or counting decision.

================  PART (a): squarefree skeleton + mixed-axis separation  ================

---- R = Z/6 ----
  single-axis packets: cond 2 -> 1 labels, cond 3 -> 2 labels
  order k=1 : conductors present = [2, 3]
  order k=2 : conductors present = [1, 3, 6]   <- full conductor 6
  [a1] every conductor present is squarefree (radical of lit axes) : PASS
  [a2] full conductor 6 first appears at order n=2 (not before)   : PASS
  [a3] single-axis convolution stays single-axis (cond in {1,p})    : PASS

---- R = Z/30 ----
  single-axis packets: cond 2 -> 1 labels, cond 3 -> 2 labels, cond 5 -> 4 labels
  order k=1 : conductors present = [2, 3, 5]
  order k=2 : conductors present = [1, 3, 5, 6, 10, 15]
  order k=3 : conductors present = [1, 2, 3, 5, 6, 10, 15, 30]   <- full conductor 30
  [a1] every conductor present is squarefree (radical of lit axes) : PASS
  [a2] full conductor 30 first appears at order n=3 (not before)   : PASS
  [a3] single-axis convolution stays single-axis (cond in {1,p})    : PASS

================  PART (b): occupation-depth recoverability  ================
  [W1] additive label r*a mod p is periodic in occupation depth r (period p):
        p=2, a=1:  (r -> r*a mod p) = [1, 0, 1, 0]
              depths r=1 and r=3 both give label 1 -> identical character, conductor 2
        p=3, a=1:  (r -> r*a mod p) = [1, 2, 0, 1, 2, 0]
              depths r=1 and r=4 both give label 1 -> identical character, conductor 3
        p=5, a=1:  (r -> r*a mod p) = [1, 2, 3, 4, 0, 1, 2, 3, 4, 0]
              depths r=1 and r=6 both give label 1 -> identical character, conductor 5
  [W2] radical map N^P -> squarefree conductor forgets occupation depth:
        tower {p^r : r=1..8} = [2, 4, 8, 16, 32, 64, 128, 256]  ->  radical/conductor set = [2]
        tower {p^r : r=1..8} = [3, 9, 27, 81, 243, 729, 2187, 6561]  ->  radical/conductor set = [3]
        tower {p^r : r=1..8} = [5, 25, 125, 625, 3125, 15625, 78125, 390625]  ->  radical/conductor set = [5]
        => Lambda(p^r)=log p sits at distinct positions r*log p but ONE conductor; the conductor cannot separate the ladder.
  [C1] occupation profiles over a fixed conductor grow without bound (R_30, n=3 axes):
        #nontrivial squarefree conductors of P_n = 2^n - 1 = 7   (fixed)
        full-support occupation profiles of total depth K  (-> the single conductor 30):
            K=3 : 1 profiles  (e.g. partitions of K into 3 positive prime-occupations)
            K=4 : 3 profiles  (e.g. partitions of K into 3 positive prime-occupations)
            K=5 : 6 profiles  (e.g. partitions of K into 3 positive prime-occupations)
            K=6 : 10 profiles  (e.g. partitions of K into 3 positive prime-occupations)
            K=7 : 15 profiles  (e.g. partitions of K into 3 positive prime-occupations)
            K=8 : 21 profiles  (e.g. partitions of K into 3 positive prime-occupations)
            K=9 : 28 profiles  (e.g. partitions of K into 3 positive prime-occupations)
  [b-verdict] occupation depth not recoverable from additive R_n data : CONFIRMED (L)

================  REALIZED BRANCH  ================
K on the squarefree skeleton: conductors are radicals of lit axes; the full
conductor first appears at convolution order n = #primes; single-axis convolution
stays single-axis. The which-axes-lit (radical) content IS finite-algebraic.

L on the occupation depth: additive convolution on F_p wraps mod p (W1), the radical
map collapses each prime-power tower to one conductor (W2), and the occupation lattice
is infinite-to-one over the finite squarefree-conductor lattice (C1). The {p^r} ladder
with weight log p is NOT a function of the squarefree additive data on R_n.

>>> JOINT-ON-DISJOINT: Lemma 8.1a splits. The squarefree skeleton + mixed separation
>>> is [P] finite algebra; the occupation lift to N^P (prime powers, weight log p) is
>>> NOT squarefree bookkeeping but strictly-additional structure -- the Thm 5.2.1
>>> double-cutoff hypothesis. This refines the source's 'remaining algebraic
>>> bookkeeping' framing and localizes the occupation lift as an external obligation.
```
