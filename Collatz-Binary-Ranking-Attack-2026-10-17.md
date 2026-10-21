# Binary ranking attack: exact exclusions and the rationality boundary

Status: no universal repayment proof. This pass searched for a concrete termination measure for the restricted two-block system and obtained exact impossibility certificates for the specified local additive family, through window length eight.

## 1. Literature boundary

The implication from a rational 2-adic starting point to an eventually periodic Collatz parity code is Lagarias' Periodicity Conjecture, not an available theorem. See [Rozier, Section 3.3](https://math.colgate.edu/~integers/t8/t8.pdf). The finite binary expansion of a positive integer must not be silently transferred to its dynamically generated code.

[Yolcu, Aaronson, and Heule](https://arxiv.org/html/2105.14697v3) develop termination proofs using mixed binary–ternary rewriting and matrix interpretations. Their Section 4.5 treats residue-avoidance questions and identifies unresolved weakenings. This supports trying explicit termination certificates, but supplies no proof of our A/B exclusion. Their impossibility theorem for a unary rewriting system is different from the finite binary-window certificates below.

## 2. The exact partial system

The allowed odd-only blocks are

\[
A=(1):\quad n\equiv3\pmod4,\quad n\mapsto(3n+1)/2,
\]
\[
B=(2,1,1):\quad n\equiv9\pmod{32},\quad n\mapsto(27n+29)/16.
\]

These residue conditions prescribe the exact listed halving exponents, not merely an integral affine output. Both block maps increase every positive input. Nevertheless, a measure of binary structure could conceivably decrease and prove that a positive integer cannot follow these blocks forever.

## 3. The ranking family searched

Let bin(n) be the ordinary binary expansion with no leading zero. For a fixed window k, pad it with k-1 start markers ^ and k-1 end markers $. Let N_sigma(n) count occurrences of the length-k word sigma in this padded string. Consider

\[
R(n)=\sum_\sigma w_\sigma N_\sigma(n).
\]

Initially the search required w_sigma>=0 for interior words sigma in {0,1}^k and allowed arbitrary real weights for boundary words containing markers. Such R is bounded below: the number of boundary windows is uniformly bounded by 2(k-1), independently of n, while the interior contribution is nonnegative.

We sought R(n)>R(F(n)) for every admissible A or B transition. For finitely many sampled transitions, strict inequalities can be scaled to decreases of at least one. Failure on a finite sample rules out a universal member of the same family.

## 4. Exact certificate theorem

**Theorem.** For each k=1,...,8, no rank in the preceding family strictly decreases on every A and B transition.

For each k, the certificate supplies finitely many valid transitions n_j->m_j and positive rational weights lambda_j. Define

\[
V_\sigma=\sum_j\lambda_j\bigl(N_\sigma(n_j)-N_\sigma(m_j)\bigr).
\]

The exact certificate satisfies

\[
V_\sigma=0\quad\text{for every boundary word},\qquad
V_\sigma\le0\quad\text{for every interior word}.
\]

Therefore sum_j lambda_j(R(n_j)-R(m_j))<=0 for any allowed weights. If R decreased strictly on every transition in the certificate, the same sum would be strictly positive. Contradiction. This proof uses no floating-point tolerance.

The certificate supports have sizes 2, 1, 1, 11, 23, 50, 94, and 167 for k=1,...,8 respectively. For example, at k=2 the single A transition 1427->2141 is sufficient. At k=3 the single B transition 3017->5093 is sufficient; that arrow denotes three odd-only steps.

## 5. Allowing negative interior coefficients does not rescue a bounded-below additive rank

The conclusion extends to any rank of this same additive padded-window form that is bounded below on all positive odd integers, even if its original interior weights have either sign.

For k>=2, form the directed graph whose vertices are (k-1)-bit words and whose edges are k-bit words; an edge goes from its first k-1 bits to its last k-1 bits, with weight w_sigma. There can be no negative-weight directed cycle. Otherwise place arbitrarily many repetitions of that cycle inside a binary string beginning and ending in 1. Fixed connecting paths and bounded boundary contributions would make R tend to minus infinity on positive odd integers.

A finite graph without negative cycles has vertex potentials p such that

\[
w'_{u\to v}=w_{u\to v}+p(u)-p(v)\ge0.
\]

For instance, add a source with zero-weight edges to all vertices and take shortest-path distances. Along a binary string the potential terms telescope. They can be absorbed into its prefix and suffix boundary weights, so the rank has an equivalent representation with nonnegative interior weights. Strings shorter than k-1 have only boundary windows; their finitely many values can be preserved by weights on windows containing both markers. At length k-1 the two endpoint potentials cancel. Thus the exact certificates also exclude the original bounded-below rank. For k=1, the same conclusion follows directly by considering arbitrarily long runs of zeros or ones inside positive odd binary strings.

This extension concerns additive window counts with boundary terms of the stated form. It does not cover arbitrary joint functions of the two boundaries, nonlinear functions of pattern counts, unbounded windows, vector orders, or ranks defined only on a specially restricted invariant subset.

## 6. Search, reconstruction, and independent verification

The search used the 4,608 admissible A/B transitions with input below 16,384, for each window k=1,...,8. All eight linear programs were infeasible. Floating-point dual solutions were then reconstructed over the rationals. Naive separate rational rounding initially failed an exact equality check; those cases were instead reconstructed by solving the active equations exactly. Only certificates that passed exact checks were retained.

Files:

* `empirical_01g/binary_pattern_rank_probe.py`: search and rational reconstruction.
* `empirical_01g/binary_pattern_rank_probe.json`: all rational witnesses.
* `empirical_01g/verify_binary_pattern_rank_certificate.py`: independent standard-library checker, with no optimization library.
* `empirical_01g/verify_binary_pattern_rank_certificate.json`: all eight certificates passed; 349 weighted transitions checked.

The independent checker recomputes every individual halving exponent inside each block, every binary pattern count, and every rational certificate inequality. Infeasibility is a theorem about this ranking family; it is not evidence of a divergent integer orbit.

## 7. Consequence for the proof effort

The desired positive-integer termination theorem has not been proved. This pass removes a concrete candidate mechanism: an additive bounded-below measure of binary patterns of length at most eight cannot force exit from even the restricted A/B family by strict decrease at every block.

A remaining approach must use structure outside that certified exclusion, such as a nonlinear interaction between counts, an adaptive return rule, or information whose scale grows with the trajectory. Those possibilities are directions to investigate, not established solutions. The prime-crystal encoding does not itself supply the missing inequality.
