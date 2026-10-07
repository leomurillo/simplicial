# Trilogy/Identification Review: Borrowed vs. Derived Claim Boundary

Scope: `T1-NativeSimplicialChart.md`, `T2-CumulantTowerEffectiveAction.md`,
`T3-CharacterOrthogonalityConductorLattice.md`, and
`Paper-I-Identification-Draft1.md`.

## Blocking Findings

### P0. Paper I, Section 4: the additive-twist functional equation is false as stated

Affected claims:

- `Paper-I-Identification-Draft1.md:718-777`
- `Paper-I-Identification-Draft1.md:795-820`
- downstream mentions at `Paper-I-Identification-Draft1.md:1417-1420` and
  `Paper-I-Identification-Draft1.md:1486-1488`

The asserted scalar functional equation for
`\hat Q_k^(N)(s) = zeta_N(s,k)/zeta(s)` is not a standard theorem and fails
direct tests. For example, with `N = 2`, `k = 1`,

```tex
zeta_2(s,1) = sum_{m >= 1} (-1)^m m^{-s} = (2^{1-s}-1) zeta(s),
```

so `\hat Q_1^(2)(s) = 2^{1-s}-1`. Since `d_k = N`, the boxed modulus identity
in Section 4.4 predicts

```tex
|\hat Q_1^(2)(s)| = |\hat Q_1^(2)(1-s)|
```

for every `s`. At `s = 2`, this gives `1/2 = 3`.

I also checked the manuscript's primitive-frequency case numerically with
`N = 6`, `k = 1`: for `s = 0.7 + 2i`, the ratio
`|\hat Q_1^(6)(s)| / |\hat Q_{-1}^(6)(1-s)|` is about `0.6394`, not `1`.

The borrowed literature does support functional equations for Riemann zeta,
Dirichlet `L`-functions, Hurwitz zeta, and periodic/Lerch zeta functions, but
not the scalar chi-factor cancellation claimed here. Periodic/additive twists
generally have vector/parity-mixed functional equations, not a one-line scalar
Dirichlet-`L` functional equation. DLMF's zeta/Hurwitz sections and the standard
Apostol/Iwaniec-Kowalski references support the classical pieces, but not the
paper's simplification.

Required action: remove Theorem 4.1 as a theorem, or replace Sections 4.2-4.5
with the correct vector/parity-decomposed functional equation and reprove a
weaker statement from that corrected formula.

### P0. Paper I, Theorem 2.1: `log zeta` is analytically continued too strongly

Affected claims:

- `Paper-I-Identification-Draft1.md:423-437`
- `Paper-I-Identification-Draft1.md:1396-1404`
- `Paper-I-Identification-Draft1.md:1480-1482`

The Euler-product/log-partition identification is correct on `Re(s) > 1`.
The sentence extending `log zeta(s)` to `C \ {1}` is false as written.
`zeta(s)` is meromorphic with a simple pole at `s = 1`, but `log zeta` is not
a globally single-valued meromorphic function; zeros of `zeta` create branch
singularities. DLMF 25.2 records the meromorphic continuation of `zeta`; DLMF
25.10 records the zero structure. Those facts do not license a global
`log zeta` on `C \ {1}`.

Required action: state Theorem 2.1 on `Re(s) > 1`; or choose a branch on a
specified simply connected zero-free domain; or replace global `log zeta`
claims by statements about `zeta`, `zeta'/zeta`, or local branches.

### P0/P1. Paper I, Theorem 3.1: formula is correct, but "A-C tensor of log zeta" is overclaimed

Affected claims:

- `Paper-I-Identification-Draft1.md:576-647`
- `Paper-I-Identification-Draft1.md:1407-1415`
- `Paper-I-Identification-Draft1.md:1483-1485`

The displayed polynomial is a valid finite-simplex third cumulant:

```tex
cum_{Q^(N)(s)}(chi_a(X), chi_b(X), chi_c(X)).
```

What is not yet derived is that it is literally the third derivative of
`log zeta` in residue-character natural parameters. To make the semantic
claim rigorous, the paper needs to define a finite exponential deformation,
for example

```tex
Phi_N(theta; s) =
  log sum_r Q_r^(N)(s) exp(sum_k theta_k chi_k(r)),
```

and then identify Theorem 3.1 as `partial_theta^3 Phi_N |_{theta=0}`.

Required action: either add that finite deformation proof, or retitle the
result as the categorical A-C tensor of the residue-projected zeta
distribution, not of `log zeta` itself.

## Major Findings

### P1. Paper I, Section 5.1: the DFT relation between additive twists and Hurwitz channels is wrong as written

Affected claim:

- `Paper-I-Identification-Draft1.md:882-896`

The line beginning with `zeta_N(s,k) = 1/zeta(s) * 0 if k = 0` is typed
incorrectly and mathematically nonsensical. The correct unnormalized relation is

```tex
zeta_N(s,k) =
  N^{-s} sum_{r=1}^N exp(2 pi i k r/N) zeta(s,r/N),
```

with inverse

```tex
N^{-s} zeta(s,r/N) =
  (1/N) sum_{k mod N} exp(-2 pi i k r/N) zeta_N(s,k).
```

If normalized coefficients `\hat Q_k` are intended, divide the whole
right-hand side by `zeta(s)`. DLMF 25.11.15 gives the relevant Hurwitz
multiplication formula background.

Theorem 5.1 itself checks algebraically despite this local error.

### P1. Paper I, Section 3.3: conductor-packet dependence is overstated

Affected claim:

- `Paper-I-Identification-Draft1.md:550-554`

`\hat Q_k^(N)(s)` does not depend only on the conductor `d_k`; it also depends
on the reduced residue class inside that conductor packet. At prime modulus
`N = 5`, the twists with `k = 1` and `k = 2` have the same conductor but are
different functions.

Required action: say `\hat Q_k^(N)` is attached to the packet `H_{d_k}`, but
varies within the packet by reduced index.

### P1. Paper I, Section 3.6: additive/multiplicative character dictionary overclaims equivalence

Affected claims:

- `Paper-I-Identification-Draft1.md:676-708`

The cited Gauss-sum technology is real, but additive characters of `Z/N` and
multiplicative Dirichlet characters on `(Z/N)^x` are not dual bases of the same
space. Non-unit residues and imprimitive/lower-conductor terms are not harmless
if the result is used as a theorem.

The additive selection rule

```tex
a + b + c = 0 mod N
```

does not automatically become

```tex
psi_a psi_b psi_c = psi_0
```

without a precise expansion and hypotheses. Keep this as a dictionary
paragraph, or state and prove a lemma with all imprimitive and non-unit terms.

### P1. Paper I, Theorem 5.3: strict positivity needs a certified proof

Affected claims:

- `Paper-I-Identification-Draft1.md:1139-1155`
- `Paper-I-Identification-Draft1.md:1497-1499`

The value `L(1/2, chi_3) = 0.4808675576...` is numerically correct; I verified
it by the Hurwitz representation. But "Iwaniec-Sarnak nonnegativity + LMFDB
decimal" is not a proof of strict positivity. The Iwaniec-Sarnak paper is about
non-vanishing proportions in families of automorphic forms; the accessible
abstract does not support the manuscript's specific claim that it proves
`L(1/2, chi) >= 0` for every real primitive Dirichlet character.

Required action: include a rigorous interval computation for this exact
degree-1 `L`-value, or cite a source proving strict positivity for this
specific character. A database decimal can support a check, not carry a theorem.

### P1. Paper I, Section 5.6: zero-residue statements need limiting language and hypotheses

Affected claims:

- `Paper-I-Identification-Draft1.md:1076-1138`

At a zeta zero `rho`, `T^zeta` has poles because of powers of `1/zeta(s)`.
The expression

```tex
zeta(rho)^3 T^zeta(...; rho, 6)
```

should be a limit:

```tex
lim_{s -> rho} zeta(s)^3 T^zeta(...; s, 6).
```

The non-vanishing claim also requires `L_3(rho) != 0` and nonzero beta
factors. The draft does not exclude common zeros of `zeta` and `L(s,chi_3)`.

### P1. Paper I, Sections 6.4-6.5: Connes-Consani/Bures identification is a dictionary, not a theorem

Affected claims:

- `Paper-I-Identification-Draft1.md:1236-1378`
- `Paper-I-Identification-Draft1.md:1434-1437`
- `Paper-I-Identification-Draft1.md:1492-1495`

The borrowed Connes-Consani paper does support the high-level summary that the
adele class space of the rationals is interpreted as a monoidal extension of
the Picard group with rigidifying data, including a norm, a morphism to
`R_{>0}`, and root-of-unity combinatorics (arXiv:2602.15941). It does not prove
the paper's Bures-carrier equivalence.

The arithmetic pieces are secure:

- `Q(zeta_6) = Q(sqrt(-3))`;
- complex conjugation sends `zeta_6` to `zeta_6^{-1}`;
- `zeta_{Q(sqrt(-3))}(s) = zeta(s) L(s, chi_3)` is classical for quadratic
  fields.

The additional rows "Arakelov metric = Bures Hermitian metric" and
"program's Z/6 Bures carrier = degree-2 cover of the Connes-Consani adele
class space" are not proved from the data in Paper I. Label as a structural
dictionary/handoff unless Paper II supplies a functorial construction.

Also fix the table row saying "joint zeros": the zero set of
`zeta_K = zeta * L_chi3` is the union of zeros of the two factors, not their
joint intersection.

### P1. T2: "closure defect" is new terminology, not a borrowed standard fact

Affected claims:

- `T2-CumulantTowerEffectiveAction.md:24`
- `T2-CumulantTowerEffectiveAction.md:51`
- `T2-CumulantTowerEffectiveAction.md:203`
- `T2-CumulantTowerEffectiveAction.md:296-299`

The borrowed claim that derivatives of a log-partition function are cumulants
is standard. The identification of `Q = partial^4 Phi` as the fourth cumulant is
derived correctly.

What is not borrowed and not proved is the stronger statement that `Q` measures
failure of third-order dynamics to close, or that a Jacobi-like identity would
make the cubic theory terminate. This should be presented as a definition or
programmatic interpretation unless a closure operation and residual theorem are
added.

### P1. T2: the e/m connection description mislabels the role of `T`

Affected claim:

- `T2-CumulantTowerEffectiveAction.md:200`

`T_{ijk}` is a symmetric Amari-Chentsov cubic tensor, not an "antisymmetric
piece." The nearby formula

```tex
Gamma^(alpha)_{ijk} = Gamma^LC_{ijk} - (alpha/2) T_{ijk}
```

is the right boundary: e- and m-connections differ by `T` after lowering an
index with the Fisher metric. Replace "antisymmetric piece" with "cubic
difference tensor" or "the tensor measuring the split between the alpha = +1
and alpha = -1 connections."

### P1. T3: additive conductor terminology is misleadingly identified with Dirichlet conductor

Affected claims:

- `T3-CharacterOrthogonalityConductorLattice.md:99`
- `T3-CharacterOrthogonalityConductorLattice.md:113`
- `T3-CharacterOrthogonalityConductorLattice.md:340`
- `T3-CharacterOrthogonalityConductorLattice.md:348`

For additive characters `chi_k(x)=exp(2 pi i kx/N)`, the value
`N/gcd(k,N)` is the order/additive conductor/minimal quotient modulus. That is
correct.

But additive characters are not Dirichlet characters, and the Dirichlet
induction definition quoted in the manuscript applies to multiplicative
characters on units. The phrase "the conductor in this number-theoretic sense
coincides" is therefore too strong.

Required action: call this the "additive conductor" or "minimal quotient
modulus"; mention that the word is analogous to Dirichlet conductor, not
literally the same definition.

### P2. T1: "Fisher-Rao isometry group at the uniform is SO(H0)" needs tangent/local qualification

Affected claims:

- `T1-NativeSimplicialChart.md:167-175`
- `T3-CharacterOrthogonalityConductorLattice.md:314`

The derivation proves that `SO(H0)` is the full linear isometry group of the
Fisher-Rao tangent inner product at the uniform, equivalently the stabilizer
action on `T_{psi(u)} S^{N-1}`. It does not prove that `SO(H0)` is the global
isometry group of the open probability simplex or that rotations preserve the
positive orthant. Globally, only the much smaller relabeling symmetry is
automatic.

Required action: phrase as "the infinitesimal/tangent isometry group at the
uniform" or "the isotropy representation on the tangent space."

## Claims That Check Out With Existing Literature or Direct Derivation

- T1's square-root/sphere pullback of Fisher-Rao, the factor `1/4`, the
  Bhattacharyya coefficient as amplitude inner product, and the Fisher-Rao
  distance as spherical angle are standard and correctly derived. The existing
  Fisher/Rao/Bhattacharyya/Chentsov/Amari citations are appropriate.

- T1's `H0` tangent-space identification and the `N = 4` Hodge-dual cross
  product are internally derived correctly. The only needed repair is the
  local/global isometry wording above.

- T2's categorical exponential-family formulas
  `partial_i Phi = p_i`,
  `Sigma_ij = p_i delta_ij - p_i p_j`, and the displayed third cumulant formula
  are correct. The borrowed support is standard exponential-family/cumulant
  theory.

- T2's statement that the Amari-Chentsov tensor is a standard information
  geometric object is citation-safe. The stronger "force law" and "closure
  defect" readings are programmatic and should be labeled as such.

- T3's Pontryagin/Fourier basis, character orthogonality, dimension count
  `sum_{d|N} phi(d)=N`, scalar Fisher metric at the uniform, and cubic selection
  rule
  `a+b+c = 0 mod N`
  are correct as finite Fourier calculations. The selection rule is derived,
  not borrowed.

- Paper I Theorem 2.1 is correct on `Re(s)>1`: the prime-axis product family's
  partition function is Euler's product for `zeta`, and the mean distribution is
  `q_n(s)=n^{-s}/zeta(s)` for real `s>1`.

- Paper I Theorem 3.1 is correct as the finite categorical third cumulant at
  `Q^(N)(s)`, and its `s -> 1+` limit correctly recovers T3's selection rule.

- Paper I Theorem 5.1's five `N=6` Hurwitz formulas are algebraically correct.
  Theorem 5.2's K-parity decomposition follows by substitution. Wording should
  distinguish a fixed-`s` two-channel value space from a constant-coefficient
  two-dimensional function space, because the coefficients contain powers of
  `2^{+-s}` and `3^{+-s}`.

- Paper I's Dedekind factorization
  `zeta_{Q(sqrt(-3))}(s) = zeta(s) L(s,chi_3)` is classical and citation-safe.
  It is the strongest secure part of Section 6.

## Source Checks Used

- DLMF 25.2, Riemann zeta definition/meromorphic continuation/Euler product:
  https://dlmf.nist.gov/25.2
- DLMF 25.10, Riemann zeta zeros:
  https://dlmf.nist.gov/25.10
- DLMF 25.11, Hurwitz zeta and multiplication/special-value formulas:
  https://dlmf.nist.gov/25.11
- Fisher-Rao square-root embedding background:
  https://en.wikipedia.org/wiki/Fisher_information_metric
- Fisher/Amari-Chentsov invariant tensor characterization:
  https://arxiv.org/abs/1207.6736
- Iwaniec-Sarnak paper metadata/abstract:
  https://doi.org/10.1007/s11856-000-1275-9
- Connes-Consani 2026 paper:
  https://arxiv.org/abs/2602.15941
