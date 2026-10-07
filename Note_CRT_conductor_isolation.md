# Note: CRT Conductor Isolation — Correct Statement, Proof, and Numerical Confirmation

**Status:** Companion to H7B computation (`empirical/compute_H7B_cross_conductor.py`).
Completes the [K^CH, K^CH] universality claim (Part 1) and establishes the
CRT conductor isolation theorem (Part 2), contrasted with C_7 (Part 3).

---

## 0. Correction to Script v1

The original `coupling_matrix` function computed

```
h_star_n[eta] = IFFT(DFT(h)^n)[eta]   ← WRONG
```

which equals the eta-th POSITION coordinate of the n-fold position-space
convolution h^{*n pos}.  This is not the Taylor coefficient of the Fisher
metric.

The correct quantity is the n-th CHARACTER-SPACE convolution power:

```
h_hat^{*n char}(eta) = N^{n-1} * DFT(h^n)[eta]   ← CORRECT
```

where h^n is the **pointwise** n-th power of h in position space.  The
derivation is given in §1 below.  The N^{n-1} overall scale is omitted in the
code (it does not affect which entries are zero).

---

## 1. Taylor Expansion of the Fisher Metric — Correct Formula

Let p_t = p* + t h be the m-geodesic through the centroid p* = 1/N in
direction h ∈ H (zero-sum).  The Fisher metric at p_t in the character basis
is

$$
g^F_{p_t}(\chi_\ell, \chi_m)
= \sum_x \chi_{\ell-m}(x) \cdot \frac{1}{p_t(x)}
= N \sum_{n \geq 0} (-tN)^n \sum_x \chi_{\ell-m}(x)\, h(x)^n.
$$

The **n-th Taylor coefficient** in the character-pair (ℓ, m) is therefore

$$
[C_n^{[f,e]}(h)]_{\ell,m}
= \sum_x \chi_{\ell-m}(x)\, h(x)^n
= \widehat{h^n}(\ell - m),
$$

where \widehat{h^n}(k) denotes the positive-exponent DFT of h^n:

$$
\widehat{h^n}(k) = \sum_x h(x)^n\, e^{2\pi i k x / N} = \mathrm{FFT}(h^n)[-k \bmod N].
$$

### Relation to character-space convolution power

The character convolution theorem gives DFT(f · g)[k] = (1/N)(DFT(f) *_{char} DFT(g))[k].
Therefore:

$$
\widehat{h^n}(\eta)
= \mathrm{FFT}(h^n)[-\eta]
= \frac{1}{N^{n-1}}\, \widehat{h}^{*n\,\mathrm{char}}(-\eta),
$$

where \hat h^{*n char}(\eta) = \sum_{k_1 + \dots + k_n \equiv \eta} \hat h(k_1) \cdots \hat h(k_n) is
the n-fold convolution of h_hat in character space.  For support analysis the
factor N^{n-1} is irrelevant.

**Key support lemma.**  supp(\widehat{h^n}) ⊆ n-fold sumset of supp(\hat h) in ℤ/N.

---

## 2. The CRT Conductor Isolation Theorem

**Setup.**  N = ab with gcd(a, b) = 1. Define the a-primary character subgroup

$$
P_a = \{k \in \mathbb{Z}/N : a \mid k\} = b \cdot (\mathbb{Z}/N),
$$

which has |P_a| = b elements and is closed under addition mod N.

**Theorem 2.1 (CRT conductor isolation).**
Let h ∈ H_{C_N} with supp(\hat h) ⊆ P_a. Then:

1. supp(\widehat{h^n}) ⊆ P_a for all n ≥ 1.
2. For all ℓ ∈ X_{b-\mathrm{primary}}, m ∈ X_{a-\mathrm{primary}}, and all n ≥ 1:
   [C_n^{[b\text{-prim}, a\text{-prim}]}(h)]_{\ell,m} = 0.
3. The full adjacency algebra block A^{[b\text{-prim}, a\text{-prim}]} is invisible to
   pure a-primary displacements at every Taylor order.

**Proof.**  P_a is a subgroup of (ℤ/N, +).  A subgroup is closed under
n-fold sums: P_a + P_a + … + P_a = P_a for all n.  By the support lemma,
supp(\widehat{h^n}) ⊆ P_a.

For ℓ ∈ X_{b\text{-primary}}, m ∈ X_{a\text{-primary}}: (ℓ - m) mod N ∉ P_a (since ℓ
is divisible by a but not b, m is divisible by b but not a, so a ∤ (ℓ-m)).
Therefore [C_n(h)]_{\ell,m} = \widehat{h^n}(\ell - m) = 0. □

**Corollary 2.2 (Symmetric isolation).**
By the same argument with a and b swapped, supp(\hat h) ⊆ P_b implies zero
coupling in A^{[a\text{-prim}, b\text{-prim}]}.

**Corollary 2.3 (n=1 zero for mixed support).**
If supp(\hat h) ⊆ X_{\mathrm{mixed}} = \{k : a \nmid k,\; b \nmid k\}, then
supp(\hat h) ∩ P_a = ∅ and supp(\hat h) ∩ P_b = ∅.  However the n=1 sumset
{k - m : k ∈ supp(\hat h), m ∈ X_{a\text{-prim}}} need not lie in P_a.  So the
n=1 block C_1^{[b\text{-prim}, a\text{-prim}]}(h) = 0 (since the 1-fold sumset of
supp(\hat h) = supp(\hat h) itself, and \hat h is not supported on differences
ℓ-m).  From n=2 onward, cross-coupling can be nonzero.

---

## 3. Numerical Confirmation for C_12

N = 12 = 4 × 3, gcd(4,3) = 1.

| CRT block | Character indices | Subgroup |
|---|---|---|
| 4-primary | {3, 6, 9} | P_4 = {0,3,6,9} (multiples of 3) |
| 3-primary | {4, 8} | P_3 = {0,4,8} (multiples of 4) |
| mixed | {1,2,5,7,10,11} | neither subgroup |

Three displacement types, with DFT support:
- **h_4p**: supported on {3,6,9} ⊆ P_4
- **h_3p**: supported on {4,8} ⊆ P_3
- **h_mix**: supported on {3,4,6,8,9} (straddles both primaries)

### Cross-primary coupling ||C_n^{[3p, 4p]}(h)||_F (rows ℓ ∈ {4,8}, cols m ∈ {3,6,9})

| n | h_4p | h_3p | h_mix |
|---|---|---|---|
| 1 | **0** | **0** | **0** |
| 2 | **0** | **0** | **nonzero** |
| 3 | **0** | **0** | nonzero |
| 4 | **0** | **0** | nonzero |
| 5 | **0** | **0** | nonzero |

**Interpretation:**
- h_4p: ĥ^n supported in P_4, differences ℓ-m ∉ P_4 → identically zero, all orders ✓
- h_3p: ĥ^n supported in P_3, differences ℓ-m ∉ P_3 → identically zero, all orders ✓
- h_mix at n=1: 1-fold sumset of {3,4,6,8,9} does not include {1,2,5,7,10,11} → zero ✓
- h_mix at n=2: 2-fold sumset of {3,4,6,8,9} = all of ℤ/12 (e.g., 4+9=13≡1) → nonzero ✓

The CRT isolation is **exact** (floating-point zero, not just small), confirming it is an algebraic
property, not an approximation.

---

## 4. Part 1 Confirmation: Universal Commutator

The commutator [K^CH, K^CH] equals the round-sphere curvature universally:

| N | max |commutator − sphere_curvature| |
|---|---|
| 7 | 1.42×10⁻¹⁴ |
| 12 | 6.13×10⁻¹⁴ |

This is floating-point noise; the formula is exact.  See `Note_prime_cyclic_ext_ch.md` §1
for the algebraic proof.

---

## 5. Contrast: C_7 Has No CRT Isolation

For N = 7 (prime), ℤ/7 has no proper nontrivial subgroups.  Every displacement
with \hat h ≠ 0 has nonempty support in the unique nontrivial conductor packet.
Its additive convolution envelope reaches every nontrivial quotient character
by order 6, although exact coefficient support can still have accidental
cancellations at selected orders.

**Single-mode displacement h = χ_1 + ĉ (real, zero-mean):**

| n | nontrivial Fourier modes |
|---|---|
| 1 | {1, 6} |
| 2 | {2, 5} |
| 3 | {1, 3, 4, 6} |
| 4 | {2, 3, 4, 5} |
| 5 | {1, 2, 3, 4, 5, 6} ← **full** |
| 6 | {1, 2, 3, 4, 5, 6} |

The support envelope is conductor-total by order p-1 = 6.  For this symmetric
two-mode displacement the exact nontrivial support is already full at n = 5:
the pair {1,6} reaches every nonzero residue by five-fold sums.

There is **no subgroup** of (ℤ/7, +) to confine the sumset: any nonzero element
generates the entire group.  Therefore:

> No displacement h ∈ H_{C_7} ever has a proper CRT-isolated block.  The
> adjacency algebra A_{C_7} is irreducible at the conductor level: every
> nontrivial quotient character lies in the same prime packet, and the
> convolution envelope connects the packet to itself.

This is the ALGEBRAIC statement of "no CRT isolation" — distinct from, and
complementary to, the Riemannian statement that the commutator [K^CH, K^CH]
equals sphere curvature for all N (which is the SAME for C_7 and C_12).

---

## 6. Summary Table

| Property | C_p (prime) | C_12 (4-primary h) | C_12 (mixed h) |
|---|---|---|---|
| CRT subgroups | none | P_4 or P_3 | both |
| Cross-block coupling at n=1 | N/A (no blocks) | **zero** | zero |
| Cross-block coupling at n=2 | N/A | **zero** | **nonzero** |
| Conductor-total envelope order | p-1 | never (stays in block) | 2 |
| [K^CH, K^CH] | sphere curvature | sphere curvature | sphere curvature |

---

## 7. What This Tells the Paper 12 Experimental Program

The CRT isolation theorem predicts a BLOCK-DIAGONAL Fisher adjacency structure
for models trained on C_{ab} tasks (e.g., C_{12} months):

- A transformer trained on {Jan, …, Dec} should show near-zero Fisher coupling
  between the 4-primary "quarterly" characters {3,6,9} and the 3-primary
  "trimestral" characters {4,8} in its output distribution.
- This decoupling should hold at all Taylor orders if the model's centroid
  displacement h is supported on one primary block.
- A mixed displacement (model "knows about" both 3-month and 4-month cycles)
  breaks isolation starting at the QUADRATIC term in the Fisher expansion.

The C_7 weekday task (control row) has no such block structure: the Fisher
adjacency envelope is conductor-total by n = p-1 Taylor orders.  This is the
algebraic content of the single-packet property (Theorem 3.1 in
`Note_prime_cyclic_ext_ch.md`).
