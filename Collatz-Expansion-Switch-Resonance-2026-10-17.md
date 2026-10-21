# Expansion switches: an exact resonance law

Status: proved local arithmetic statements and exact checks. Universal repayment remains unproved. No novelty claim is made.

This attack asks whether switching between expanding patterns necessarily consumes a resource that forces eventual repayment. The answer at a single switch is precise: renewal requires a specific 2-adic resonance, but that resonance can replenish arbitrarily much capacity, even between two fixed expanding patterns.

## 1. Expansion capacity

An odd-step exponent word w=(a_1,...,a_m) acts as

\[
F_w(x)=\frac{3^m x+C_w}{2^{S_w}},\qquad S_w=\sum a_i.
\]

For an expanding word let D_w=3^m-2^{S_w}>0. Both C_w and D_w are odd. Its rational fixed point is xi_w=-C_w/D_w, and its capacity at a positive odd integer x is

\[
p_w(x)=v_2(D_wx+C_w).
\]

As established in Section 12.9 of the main manuscript, the exact number of consecutive admissible repetitions is

\[
k_w(x)=\left\lfloor\frac{p_w(x)-1}{S_w}\right\rfloor.
\]

Each admissible repetition consumes S_w units of capacity. After a maximal run, at its endpoint y, the remaining capacity r=p_w(y) lies in [1,S_w].

## 2. The switch resonance theorem

For two expanding words w and v define

\[
\Delta_{wv}=D_wC_v-D_vC_w.
\]

Suppose Delta is nonzero, and put d=v_2(Delta). At any positive odd junction y, let r=p_w(y) and p=p_v(y). Then

\[
\boxed{r\ne d\ \Longrightarrow\ p=\min(r,d),
\qquad r=d\ \Longrightarrow\ p\ge d+1.} \tag{1}
\]

In particular, renewal to capacity p>d is possible only at the exact resonance r=d. If the two rational fixed points coincide, Delta=0 and p=r everywhere: switching names does not replenish capacity.

**Proof.** Write A_w=D_wy+C_w and A_v=D_vy+C_v. The integer identity

\[
D_wA_v-D_vA_w=\Delta_{wv}
\]

has odd coefficients D_w,D_v. Equivalently, D_w A_v=D_v A_w+Delta. When r and d differ, the right side has valuation min(r,d). When they agree, dividing by 2^d leaves a sum of two odd integers, giving valuation at least d+1. The zero-Delta case follows directly. ∎

The number d is also v_2(xi_w-xi_v), since the fixed-point denominators are odd. Thus the condition is exactly the 2-adic separation of the two rational centers.

At a maximal w-run endpoint, r<=S_w. Consequently, if d>S_w, the new capacity is just p=r<=S_w. That pair cannot produce a large renewal at such an endpoint. This gives a rigorous filter on which switches can replenish capacity.

## 3. Arbitrarily large replenishment between fixed expanding words

Choose

\[
w=(1),\qquad v=(2,1,1).
\]

Their maps and centers are

\[
F_w(x)=(3x+1)/2,\quad \xi_w=-1,
\]
\[
F_v(x)=(27x+29)/16,\quad \xi_v=-29/11.
\]

Both slopes exceed one. Here Delta=29-11=18, so d=1. A maximal w-run leaves r=1, exactly the resonance permitting large renewal.

**Theorem.** For every K>=1 there is a positive odd integer n_K whose orbit has exactly one initial w repetition, immediately followed by exactly K repetitions of v. Every complete block increases its input.

Choose any positive odd L with

\[
2^{4K+2}L\equiv23\pmod{11},
\]

and set

\[
n_K=\frac{2^{4K+2}L-23}{11}.
\]

Such an odd L can always be chosen between 1 and 21: solve the congruence modulo 11, then choose the odd representative. The resulting n_K is positive.

**Proof.** Since

\[
n_K+1=\frac{4(2^{4K}L-3)}{11},
\]

we have v_2(n_K+1)=2, giving exactly one w repetition. At its endpoint y=(3n_K+1)/2,

\[
11y+29=\frac{3(11n_K+23)}2
=3\cdot2^{4K+1}L.
\]

Thus p_v(y)=4K+1. Since S_v=4, the repetition formula gives exactly K repetitions. Both affine maps strictly increase every positive input. After the K repetitions the endpoint is

\[
z_K=\frac{2\cdot3^{3K+1}L-29}{11},
\]

and v_2(11z_K+29)=1, so a further v repetition is impossible. ∎

Examples at complete block endpoints:

* K=1: 27 -> 41 -> 71. The v block is 41 -> 31 -> 47 -> 71.
* K=2: 91 -> 137 -> 233 -> 395.

There are contracting individual odd steps inside v. The theorem asserts growth at the block endpoints, not monotonicity at every individual step. For K=1 the intermediate contraction to 31 still remains above the initial 27.

This family refutes a mandatory loss at every expanding-pattern switch, and any universal bound on renewed capacity depending only on these two word types and their separation d. It does not refute eventual repayment: the starting integer increases with K.

## 4. The exact arithmetic of a resonant refill

At a resonant junction write

\[
A_w=2^d u,\quad A_v=2^{d+e}v_0,\quad
\Delta=2^d\delta,
\]

where u,v_0,delta are odd and e>=1. Then the switch identity becomes

\[
\boxed{D_w2^e v_0-D_vu=\delta.} \tag{2}
\]

This is an exact relation between the odd parts and the renewed power of two. In prime-crystal coordinates, it identifies the additive transition that must be controlled. Merely tracking the power of two loses the changing odd parts u and v_0. The explicit family above proves that fixing the word pair and delta is insufficient to bound e.

For a succession of maximal runs, let p_i be each incoming capacity, r_i its remaining capacity, k_i its repetition count, and J_i=p_{i+1}-r_i its switch increment. Then

\[
\sum_{i=0}^{N-1}k_i S_i
=p_0-r_{N-1}+\sum_{i=0}^{N-2}J_i. \tag{3}
\]

This is a conservation identity, not a finite-resource bound: the switch increments can be arbitrarily large. Equation (2) describes exactly where those increments enter.

## 5. Verification and next proof obligation

`empirical_01g/expansion_switch_reserve.py` checked (1) at 20,504 junction/word comparisons drawn from 44 expanding words, and verified the explicit family for K=1,...,100 using exact integers. Results are in the adjacent JSON file. The written algebra proves the statements for all the stated parameters; the finite checks are diagnostics.

A universal argument must control the repeated equations (2) along one orbit, including the changing odd parts. Counting resonant switches as rare under a random model does not exclude an exceptional deterministic orbit. Nor may the increments in (3) be bounded by the initial capacity without a new argument: the family explicitly replenishes them.

This research pass supplies a proved transition law and an exact failure of the proposed local resource argument. It does not prove the global bound on replenishment needed for repayment.
