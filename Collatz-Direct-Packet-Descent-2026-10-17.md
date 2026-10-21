# A direct arithmetic descent thread for Collatz

Date: 2026-10-17. Status: exact reductions and obstruction theorems; the universal descent assertion remains unproved. This note is separate from the main manuscript. It makes no novelty claim.

The aim is to bypass the transfer from an averaged Syracuse law to a minimum operator. Collapse the finite chains on which the odd Collatz map uses exactly one halving, then study the induced map on their smallest integers. This gives a direct route to **every integer**, but it does not make the remaining descent theorem automatic.

## 1. Finite packets and their minima

Write

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

for positive odd integers. Factor

\[
n+1=2^s3^tq,\qquad s\ge1,\quad t\ge0,\quad (q,6)=1.
\]

Set \(M=s+t\). The packet containing \(n\) is

\[
\mathcal P_{M,q}=\{2^{M-j}3^jq-1:0\le j<M\}.
\]

Its minimum is

\[
B(n)=2^Mq-1=\frac{2^t(n+1)}{3^t}-1.
\]

**Proposition 1.** These packets partition the positive odd integers. Within a packet, every member except the last maps to the next under \(U\), with exactly one halving. In particular, \(U^t(B(n))=n\).

**Proof.** Unique factorization gives the unique pair \((M,q)\) and position \(j=t\). For \(j<M-1\),

\[
3(2^{M-j}3^jq-1)+1
=2(2^{M-j-1}3^{j+1}q-1),
\]

whose parenthesis is odd. The last member is \(2\cdot3^{M-1}q-1\); its image numerator is \(2(3^Mq-1)\), divisible by at least four. All entries increase with \(j\). ∎

Thus an integer and its packet minimum have the same eventual fate. The set of minima is

\[
\mathcal B=\{b>0:b\text{ odd},\;3\nmid b+1\}.
\]

This is an exact arithmetic quotient, not a probabilistic model.

## 2. The exact packet map

For \(b=2^Mq-1\in\mathcal B\), define

\[
h=v_2(3^Mq-1),\qquad
z=\frac{3^Mq-1}{2^h},\qquad t=v_3(z+1).
\]

Here \(h\ge1\). Following the packet to its exit gives \(U^M(b)=z\). Define

\[
Q(b)=B(z),\qquad
Q(b)+1=\frac{2^t(3^Mq-1+2^h)}{2^h3^t}. \tag{1}
\]

One application of \(Q\) follows the original orbit to an exit, then replaces that exit by the minimum of its packet. Consequently, a \(Q\)-path is not literally a subsequence of the original orbit; it records the packets visited. Replaying each new packet can revisit its initial segment.

There is useful exact coupling of the valuations:

* If \(h\) is odd, then \(t=0\).
* If \(h\) is even and \(j=1+v_3(h/2)<M\), then \(t=j\).

Indeed,

\[
t=v_3(3^Mq+2^h-1).
\]

For odd \(h\), the second summand is nonzero modulo three. For even \(h\), the elementary lifting-the-exponent identity gives \(v_3(2^h-1)=1+v_3(h/2)\); unequal valuations cannot cancel. When \(j\ge M\), that argument does not determine \(t\), and no formula is asserted here.

## 3. A complete conditional route to Collatz

**Theorem 2.** Collatz is equivalent to the following packet descent assertion:

\[
\forall b\in\mathcal B\setminus\{1\}\quad
\exists r\ge1:\quad Q^r(b)<b. \tag{PD}
\]

**Proof of sufficiency.** Use strong induction on the packet minimum. The minimum 1 reaches 1. If (PD) holds for \(b>1\), its \(Q\)-path reaches a smaller minimum, which reaches 1 by induction. For each edge \(b\mapsto Q(b)\), both \(b\) and \(Q(b)\) reach the same exit \(z\): the first after \(M\) steps and the second after \(t\) steps. They therefore have the same eventual fate. Pulling this property backwards along the finite path proves that \(b\) reaches 1. Proposition 1 handles all odd integers, and initial divisions by two handle all positive integers.

**Necessity.** If every original orbit reaches 1, its itinerary through these finite directed packets reaches the packet of 1. The exit of a packet is independent of the entry position, so its packet itinerary is exactly iteration of \(Q\). Thus every \(b>1\) eventually reaches 1 under \(Q\), giving (PD). ∎

This theorem is a direct logical thread to the full conjecture. **(PD) is equivalent to Collatz, not an independently established easier theorem.** No density-one estimate is being substituted for it.

## 4. Exact accumulated descent budget

Equation (1) gives

\[
\frac{Q(b)+1}{b+1}
=\left(\frac32\right)^{M-t}2^{-h}
\left(1+\frac{2^h-1}{3^Mq}\right).
\]

Define the packet credit

\[
C(b)=h\log2-(M-t)\log(3/2)
-\log\left(1+\frac{2^h-1}{3^Mq}\right).
\]

For \(b_i=Q^i(b_0)\), telescoping yields

\[
\sum_{i<r}C(b_i)=\log\frac{b_0+1}{b_r+1}. \tag{2}
\]

Hence the exact missing assertion is: **every packet trajectory starting above 1 has a finite prefix with positive total credit.** This is again (PD), not a proof of it. Formula (2) identifies precisely the arithmetic correlation that a proof must control: large \(M\), halving valuation \(h\), and ternary reset \(t\) cannot be assigned independent distributions. The positive correction inside the logarithm cannot be discarded in a proof of descent.

All finite comparisons can be made by integer cross multiplication in (1), with no floating-point logarithms. This is the useful role of an exact metric here: certify comparisons, while leaving the dynamical inequality to be proved.

## 5. Two rigorous obstructions to simple heights

### Positive additive prime heights fail

The exact map has

\[
Q(7)=13,\qquad Q(27)=31.
\]

Suppose a height \(H(b)=\sum_p w_pv_p(b+1)\), with \(w_2>0\), decreased strictly at every packet step above 1. The first transition, \(8\mapsto14\), requires \(w_7<2w_2\). The second, \(28\mapsto32\), requires \(w_7>3w_2\). Contradiction.

Thus positive linear prime-coordinate heights cannot prove monotone one-step descent for \(Q\). This does not exclude nonlinear heights, history-dependent certificates, or return-time descent.

### Arbitrarily long expanding runs survive packet collapse

**Proposition 3.** For every integer \(L\ge1\) and \(R\ge1\), set

\[
n_j=24L\,9^j8^{R-j}-5,\qquad 0\le j\le R.
\]

Then all \(n_j\) are packet minima with \(v_2(n_j+1)=2\), and

\[
Q(n_j)=n_{j+1}>n_j\qquad(0\le j<R).
\]

**Proof.** Write \(n_j+1=4q_j\), with \(q_j=6L9^j8^{R-j}-1\). This is odd and not divisible by three. For \(j<R\), \(q_j\equiv-1\pmod8\), so \(v_2(9q_j-1)=1\). The odd-valuation rule gives \(t=0\). Equation (1) becomes

\[
Q(n_j)=\frac{9n_j+5}{8}=n_{j+1}.
\]

Strict increase follows from \(n_j>0\). ∎

These runs repeat the original odd-step exponent word \((1,2)\), with slope \(9/8\). They show that collapsing exponent-one chains removes only one source of expansion.

Two consequences are immediate:

1. There is no universal fixed number of packet steps within which every starting minimum descends.
2. For any fixed modulus \(L\), no height of the form
   \[
   H(n)=\log n+F(v_2(n+1),n\bmod L)
   \]
   can decrease at every packet step. Along the displayed family, both arguments of \(F\) remain fixed, while \(n\) increases.

This second statement concerns exactly the displayed class of heights; it does not rule out every finite-state argument or every geometric metric.

## 6. Exact finite checks

The accompanying `empirical_01g/kl/collatz_packet_descent.py` uses integer arithmetic and writes its results to the adjacent JSON file.

* 10,000 odd integers below 20,000 passed packet membership and reconstruction checks.
* All 66,666 packet minima strictly between 1 and 200,000 descended within the computational cap of 10,000 packet steps.
* 18,011 of those minima increased on their first packet step.
* The longest observed first descent took 32 packet steps, starting at 35,655.
* 320 explicit expanding runs were checked: eight choices of \(L\), with each length from 1 through 40.

For example, 27 takes 37 original odd steps to fall below itself; its packet path first falls below 27 after 15 packet steps. These are different clocks. The program's `replayed_odd_steps` counts full packet traversals, including potentially replayed prefixes; it is not an original-orbit stopping time.

Finite success establishes none of (PD) beyond the tested starts. In particular, the existence of the explicit expanding families prevents interpreting the observed maximum as a universal bound.

## 7. What remains worth attacking

The direct target is an adaptive return-time estimate for (2): prove that an expanding episode forces enough subsequent halving or ternary reset to repay its accumulated negative credit. A proof must retain arithmetic information at increasing precision, or use a global argument that makes bounded-precision information unnecessary. Simply observing that every repeated expanding word eventually ends does not control the next word, nor the accumulated height.

The prime crystal can encode \(M,h,t\) and exact comparisons, and the packet quotient can remove redundant motion. Neither supplies the missing repayment theorem. The concrete research question is whether the valuation resonance in Section 2 can be turned into a bound on successive expanding episodes that survives arbitrary changes of word. No such bound is proved here.

The achieved result is therefore a direct exact formulation, plus rigorous exclusions of two tempting metric strategies. It is not a completed proof of Collatz or evidence that its remaining step is small.
