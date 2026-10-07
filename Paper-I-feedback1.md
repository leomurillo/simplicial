# Paper I feedback 1: mathematical rigor pass

Scope: proof layer and semantic layer only. I did not review exposition,
paper formalities, positioning, or citation polish except where they affect
mathematical trust.

## Short verdict

Several core identifications check out in their natural domains:

- The prime-axis Euler product identification in Sec. 2 is correct on
  `Re(s) > 1`.
- The finite categorical cumulant contraction in Theorem 3.1 is correct as
  the third cumulant of the random variables `chi_a(X), chi_b(X), chi_c(X)`
  for `X ~ Q^(N)(s)`.
- The `s -> 1+` limit of Theorem 3.1 recovers the trilogy selection rule.
- The explicit `N = 6` Hurwitz formulas in Theorem 5.1 are algebraically
  correct, and Theorem 5.2 is the right parity decomposition.
- The Dedekind factorization
  `zeta_{Q(sqrt(-3))}(s) = zeta(s) L(s, chi_3)` is classical and correct.

But I would not currently accept the paper's proof spine as rigorous. The
main blocker is Sec. 4: the claimed scalar functional equation for the
normalized additive twists is false, and Theorem 4.1 rests on it. There are
also several places where a true computation is semantically upgraded into a
stronger geometric/Galois statement without enough definitions.

## Blocking issues

### P0. Sec. 4 functional equation and Theorem 4.1 are false as stated

The claimed clean functional equation for
`\hat Q_k^(N)(s) = zeta_N(s,k)/zeta(s)` does not survive the smallest test.

Take `N = 2`, `k = 1`. Then

```tex
zeta_2(s,1) = \sum_{m >= 1} (-1)^m m^{-s}
            = (2^{1-s} - 1) zeta(s),
```

so

```tex
\hat Q_1^(2)(s) = 2^{1-s} - 1.
```

Here `d_k = N = 2`, so the boxed modulus identity in Sec. 4.4 predicts
power factor `N^{1/2-Re(s)} d_k^{Re(s)-1/2} = 1`, hence

```tex
|\hat Q_1^(2)(s)| = |\hat Q_1^(2)(1-s)|
```

for all `s`. At `s = 2`, this says `|1/2 - 1| = |4 - 1|`, i.e. `1/2 = 3`.
So the identity is not correct.

The underlying issue is structural: a periodic/additive zeta twist is not,
in general, a single completed Dirichlet `L`-function with one scalar
functional equation. Its functional equation mixes Hurwitz channels and
parity components, and even/odd Dirichlet characters have different gamma
factors. The asserted chi-factor cancellation is therefore not available in
the stated generality.

Consequences:

- Lines around Secs. 4.2-4.4 need to be replaced by the correct vector or
  parity-decomposed functional equation.
- Theorem 4.1 cannot be used as a theorem until reproved from the corrected
  functional equation.
- The "critical line as unique `N`-uniformity locus" should be downgraded or
  removed for now.

There is also an internal proof issue independent of the counterexample:
the proof says "fixed `k` (hence fixed `d_k`) and growing `N = P_n`." Across
changing moduli, fixed integer `k` does not define a fixed conductor packet;
for example `k = 1` has `d_k = N`. A primorial-ladder statement needs an
explicit embedding of fixed-conductor characters into each row.

### P0. `log zeta` is being analytically continued too casually

Theorem 2.1 is fine on `Re(s) > 1`, but the sentence that analytic
continuation extends `log zeta(s)` to `C \ {1}` is false. `zeta` is
meromorphic on `C`; `log zeta` is not globally single-valued and has
branch singularities at zeros as well as at the pole. A rigorous statement
needs one of:

- restrict `log zeta` to `Re(s) > 1`;
- choose a branch on a simply connected zero-free domain; or
- replace global `log zeta` claims by the meromorphic logarithmic derivative
  `-zeta'/zeta`.

This also affects the semantic geometry in Sec. 2.4. The Bhattacharyya
pairing is a genuine Hilbert/probability inner product only in the
convergence/positivity region. At `s_1 = 1/2 + it`, `s_2 = 1/2 - it`, the
series has midpoint exponent `1/2`, so it diverges before analytic
continuation. The displayed value involving `zeta(1/2)` can be presented as
an analytically continued kernel identity, not as an actual Bhattacharyya
inner product of probability amplitudes.

### P0/P1. Theorem 3.1 is correct, but its semantic label is too strong

The formula in Theorem 3.1 checks as the finite-simplex third cumulant at
the point `Q^(N)(s)`. More precisely, it is

```tex
cum_{Q^(N)(s)}(chi_a(X), chi_b(X), chi_c(X)).
```

That is a solid result.

What is not yet justified is calling it "the Amari-Chentsov tensor of
`log zeta`" without further construction. The finite categorical tensor is
the tensor of the `N`-point simplex evaluated at the residue-projected zeta
distribution. It is not literally `partial^3 log zeta` in residue-character
natural parameters unless the paper defines a finite exponential deformation
such as

```tex
Phi_N(theta; s) = log sum_r Q_r^(N)(s) exp(sum_k theta_k chi_k(r))
```

and then identifies Theorem 3.1 as its third derivative at `theta = 0`.
This would make the semantic layer rigorous.

## Major issues to repair

### P1. The DFT relation between additive twists and Hurwitz channels is wrong as written

In Sec. 5.1 the displayed formula around the DFT relation contains a clear
normalization/typing error. The correct relation is

```tex
zeta_N(s,k) = N^{-s} sum_{r=1}^N exp(2 pi i k r/N) zeta(s,r/N),
```

with inverse

```tex
N^{-s} zeta(s,r/N)
  = (1/N) sum_{k mod N} exp(-2 pi i k r/N) zeta_N(s,k).
```

If using normalized Fourier coefficients `\hat Q_k`, divide the whole
right-hand side by `zeta(s)`. As written, the line saying
`zeta_N(s,k) = (1/zeta(s)) * 0 if k = 0` is nonsensical.

This is probably a local typo, because Theorem 5.1 itself can be derived
correctly without it.

### P1. The conductor-packet dependence is overstated

The statement that `\hat Q_k^(N)(s)` depends on `k` only through its
conductor is false. It also depends on the reduced residue class `k'` modulo
the conductor. For example, at prime modulus `N = 5`, the twists with
`k = 1` and `k = 2` have the same conductor but are different functions.

Safer wording: `\hat Q_k^(N)` is attached to the conductor packet `H_{d_k}`,
but the value varies inside that packet according to the reduced index.

### P1. Gauss-sum duality is too compressed and overclaims equivalence

Sec. 3.6 is directionally useful, but not rigorous enough for the weight it
is asked to carry. Additive characters on `Z/N` and multiplicative Dirichlet
characters on `(Z/N)^x` are not simply dual bases of the same space. The
non-unit residues and imprimitive/lower-conductor terms are not harmless
bookkeeping if the statement is used as a theorem.

In particular, the additive selection rule

```tex
a + b + c = 0 mod N
```

does not automatically translate to the multiplicative condition

```tex
psi_a psi_b psi_c = psi_0
```

without a precise expansion and hypotheses. I would either make Sec. 3.6 a
clearly labeled dictionary/intuition paragraph or replace it with a fully
stated lemma including imprimitive terms.

### P1. The `N = 6` "2-dimensional function space" wording is ambiguous

Theorem 5.1's formulas are correct, but the phrase "the five Hurwitz
channels live in a 2-dimensional function space spanned by `zeta` and
`L(s,chi_3)`" is not literally true over constant complex coefficients.
The coefficients involve `2^s`, `3^s`, `2^{-s}`, and `3^{-s}`.

What is true:

- for each fixed `s`, the five values lie in the two-channel value space
  generated by `Z(s)` and `L_3(s)`;
- as functions of `s`, they form a rank-2 module over the coefficient ring
  generated by the elementary factors `2^{\pm s}`, `3^{\pm s}`.

This distinction matters because later "Galois eigenspace" language sounds
like a constant-coefficient vector-space decomposition.

### P1. Theorem 5.3 needs a certified proof, not a database decimal

The nonnegativity input plus an LMFDB decimal is not, by itself, a proof of
strict positivity. If this theorem is load-bearing later, include either:

- a citation to a rigorous certified computation for this exact central
  value;
- a short interval-arithmetic computation in the paper/probe with an
  explicit lower bound; or
- a classical exact/special-value argument if available.

The theorem is almost certainly true, but the current proof is not a proof.

### P1. The zero-residue discussion in Sec. 5.6 needs limiting language and extra hypotheses

At a zeta zero `rho`, `T^zeta` has poles because of the powers of
`1/zeta(s)`. The expression

```tex
zeta(rho)^3 T^zeta(...; rho, 6)
```

should be written as the limit

```tex
lim_{s -> rho} zeta(s)^3 T^zeta(...; s, 6).
```

Also, the claim "non-vanishing iff none of `a,b,c` lies in a K-fixed orbit"
needs additional conditions. The displayed proportionality includes
`L_3(rho)^3` and the beta factors, so non-vanishing also requires
`L_3(rho) != 0` and the relevant `beta_j(rho) != 0`. The draft does not
exclude common zeros of `zeta` and `L(s,chi_3)`.

### P1. The Connes-Consani/Bures identification is presently a dictionary, not a theorem

The arithmetic part of Sec. 6 is sound: `Q(zeta_6) = Q(sqrt(-3))`,
Galois conjugation sends `zeta_6` to `zeta_6^{-1}`, and the Dedekind zeta
factorization is correct.

The stronger table in Identification T3.3 needs downgrading or more
construction. In particular:

- "Arakelov metric = Bures Hermitian metric" is not proved from the data
  given.
- "Program's `Z/6` Bures carrier = degree-2 cover of the Connes-Consani
  adele class space" is not a mathematically defined equivalence yet.
- The table says "joint zeros of `zeta` and `L_{chi_3}`", but
  `zeta_K = zeta * L_{chi_3}` has zero set equal to the union, not the
  joint intersection. The later prose says union, so the table should be
  corrected.

I would label this section as a structural dictionary unless Paper II
supplies the missing functorial construction.

## Smaller mathematical cleanups

- In the derivation of induced characters modulo 6, the text says "the four
  characters modulo 6"; there are `phi(6) = 2` Dirichlet characters modulo
  6. The surrounding computation uses the right two characters, so this is
  likely just a typo.
- The Hurwitz multiplication formula should avoid the `alpha = 0`,
  `r = 0` presentation, where `zeta(s,0)` is not a standard Hurwitz channel.
  Use `r = 1,...,N`.
- The proof of the `r = 5/6` formula should not rely on "complex conjugation"
  language for general complex `s`; derive it by the same residue-class
  linear system or by the explicit `A-B` equations.
- Any statement involving `Q^(N)(s)` as a probability distribution should be
  restricted to real `s > 1`. For complex `s`, call it a normalized complex
  measure or meromorphic family.

## What I would keep as the mathematical core

If Sec. 4 is removed or corrected, I would still regard the following as a
valuable and coherent Paper I core:

1. `log zeta` on `Re(s) > 1` is the log-partition of the prime-axis
   geometric product family.
2. Pushing the zeta distribution to `Z/N` and evaluating the finite
   categorical third cumulant in the additive character basis gives the
   closed polynomial formula of Theorem 3.1.
3. The `s -> 1+` limit recovers the trilogy cubic selection rule.
4. At `N = 6`, the residue/Hurwitz packet has an explicit two-channel
   decomposition into the `zeta` and `L(s,chi_3)` channels, with K-parity
   matching conjugation on `mu_6`.
5. The corresponding Artin/Dedekind factorization for `Q(sqrt(-3))` is the
   correct number-theoretic name for that two-channel arithmetic.

That is enough for a strong identification paper. I would not let Theorem
4.1 or the Connes-Consani/Bures equivalence be load-bearing until the above
repairs are made.
