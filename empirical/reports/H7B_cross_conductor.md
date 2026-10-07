# H7B: Cross-Conductor Fisher Coupling — C_12 vs C_7

**Claim 1**: [K^CH, K^CH] is the round-sphere curvature for all N (prime or composite).
**Claim 2**: Pure CRT-primary displacements in C_12 do not generate cross-primary
conductor coupling at any Taylor order. Mixed displacements do, starting at n=2.
**Claim 3**: This CRT isolation is absent in C_7 (prime): no subgroup separation exists.

## Part 1: Universal Commutator Formula

[K^CH_{p*}(u), K^CH_{p*}(v)](w) = N*(⟨u,w⟩ v − ⟨v,w⟩ u) for all N.

| N | max|commutator − sphere_curvature| |
|---|---|
| 7 | 1.42e-14 |
| 12 | 6.57e-14 |
| 4 | 7.11e-15 |
| 6 | 2.84e-14 |
| 9 | 6.75e-14 |
| 15 | 2.27e-13 |

All errors are floating-point noise. The formula is exact and universal.

## Part 2: C_12 — Three Displacement Types

CRT subgroups: 4-primary = [3, 6, 9], 3-primary = [4, 8], mixed = [1, 2, 5, 7, 10, 11]

Displacements (all zero-mean, unit-scale for comparison):
- **h_4p**: supported on 4-primary chars {3,6,9}
- **h_3p**: supported on 3-primary chars {4,8}
- **h_mix**: sum h_4p + h_3p (mixed CRT support)

DFT support of h_4p:  [3, 6, 9]
DFT support of h_3p:  [4, 8]
DFT support of h_mix: [3, 4, 6, 8, 9]

### Cross-primary coupling ||C_n^{[3p, 4p]}(h)||_F

Coupling FROM 4-primary packet {3,6,9} TO 3-primary packet {4,8}.

| n | h_4p | h_3p | h_mix |
|---|---|---|---|
| 1 | 0.0000 | 0.0000 | 0.0000 |
| 2 | 0.0000 | 0.0000 | 0.9798 |
| 3 | 0.0000 | 0.0000 | 0.5692 |
| 4 | 0.0000 | 0.0000 | 0.4246 |
| 5 | 0.0000 | 0.0000 | 0.2688 |

**Prediction**: h_4p and h_3p columns = 0 at all orders (CRT isolation).
h_mix column = 0 at n=1, nonzero from n=2 onward (mixed coupling through convolution).

### Coupling to mixed-conductor chars ||C_n^{[mixed, 4p]}(h)||_F

| n | h_4p | h_3p | h_mix |
|---|---|---|---|
| 1 | 0.0000 | 6.0000 | 3.7947 |
| 2 | 0.0000 | 1.2247 | 1.4697 |
| 3 | 0.0000 | 0.7500 | 1.1063 |
| 4 | 0.0000 | 0.2552 | 0.7126 |
| 5 | 0.0000 | 0.1146 | 0.4724 |

### Coupling to mixed-conductor chars ||C_n^{[mixed, 3p]}(h)||_F

| n | h_4p | h_3p | h_mix |
|---|---|---|---|
| 1 | 4.8990 | 0.0000 | 3.7947 |
| 2 | 1.6330 | 0.0000 | 1.3856 |
| 3 | 0.9526 | 0.0000 | 1.0000 |
| 4 | 0.4536 | 0.0000 | 0.6004 |
| 5 | 0.2306 | 0.0000 | 0.3922 |

### Within-primary self-coupling ||C_n^{[4p, 4p]}(h)||_F

| n | h_4p | h_3p | h_mix |
|---|---|---|---|
| 1 | 4.8990 | 0.0000 | 3.7947 |
| 2 | 2.3805 | 1.7321 | 1.9900 |
| 3 | 1.1139 | 0.3536 | 0.8967 |
| 4 | 0.5650 | 0.2165 | 0.5591 |
| 5 | 0.2809 | 0.0737 | 0.3411 |

### C_2^{[3p, 4p]}(h_mix) — the first nonzero cross-primary matrix

Shape: 2 × 3  (rows = 3-primary [4, 8],  cols = 4-primary [3, 6, 9])

```
[[0.4 0.4 0.4]
 [0.4 0.4 0.4]]
```

This matrix is nonzero because h_hat^{*2}(ell - m) for ell ∈ {4,8}, m ∈ {3,6,9}
involves cross-terms like hat_h(4) * hat_h(9-4+ell-m) where the two Fourier
coefficients come from different CRT factors.

## Part 3: C_7 — No CRT Isolation

In C_7 (prime), Z/7Z has no proper nontrivial subgroup.
Every nonzero displacement h eventually generates coupling to ALL modes
through convolution. There is no notion of '2-primary' or '3-primary' block.

Single-mode displacement h = chi_1 (+ conj) in C_7:

Convolution power support (nonzero Fourier modes at order n):

| n | nonzero Fourier modes (k=1..6) | full support? |
|---|---|---|
| 1 | [1, 6] | False |
| 2 | [2, 5] | False |
| 3 | [1, 3, 4, 6] | False |
| 4 | [2, 3, 4, 5] | False |
| 5 | [1, 2, 3, 4, 5, 6] | True |
| 6 | [1, 2, 3, 4, 5, 6] | True |
| 7 | [1, 2, 3, 4, 5, 6] | True |

Full coupling matrix ||C_n^{[X_7, X_7]}(h_single)||_F in C_7:

| n | Frobenius norm | all off-diagonal entries nonzero? |
|---|---|---|
| 1 | 3.1623 | False |
| 2 | 0.8330 | False |
| 3 | 0.2041 | False |
| 4 | 0.0573 | False |
| 5 | 0.0148 | False |
| 6 | 0.0042 | True |

In C_7 there is no block structure: a single-mode displacement generates
full coupling across all character pairs by n = p-1 = 6 (Fermat).
There is no CRT subgroup to confine the coupling.

## Part 4: Why — The Subgroup Theorem

**Theorem (CRT conductor isolation)**:
Let N = ab with gcd(a,b)=1. Let P_a = {k ∈ Z/N : a | k} be the a-primary
character subgroup of (Z/N, +). Then:

1. P_a is closed under addition mod N (it is the subgroup b·(Z/N)).
2. If hat_h is supported on P_a, then hat_h^{*n} is supported on P_a for all n≥1.
3. Therefore C_n^{[f,e]}(h_a) = 0 whenever (e-f) mod N ∉ P_a.
   In particular, cross-CRT coupling between the a-primary and b-primary blocks is zero.

**Proof**: P_a = {k : a|k} = b·(Z/N) is a subgroup of (Z/N,+).
A subgroup is closed under convolution (the sum of two P_a-supported functions
has Fourier support in P_a + P_a = P_a). By induction, all powers stay in P_a. □

**For C_7 (prime)**: The only subgroups of (Z/7,+) are {0} and Z/7 itself.
No proper nontrivial subgroup exists. Any nonzero displacement has support
that generates all of Z/7 under repeated addition (Fermat: k·(p-1) cycles through
all residues for k≠0). CRT isolation does not apply.

**The diagnostic statement**: In C_12, the displacement h encodes which
CRT primary blocks are active. Pure 2-primary or pure 3-primary displacements
have DECOUPLED Fisher adjacency: the 4-primary characters never see the
3-primary characters through Fisher coupling, regardless of Taylor order.
The only coupling mechanism is the MIXED character block {1,2,5,7,10,11},
and it activates only when h has support in BOTH primary subgroups.
In C_7, there is no such decoupling — every character sees every other.
