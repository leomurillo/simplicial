# A substantial paper from the prime crystal

17 October 2026. Recommendation based on the supplied inspiration note, the current main manuscript, local derivations, and a targeted, non-exhaustive source search.

## Decision

Lead with a theorem about arithmetic geometry that can stand without Collatz or RH. Keep nearly linear Collatz preimage growth as a separate high-impact research program. Do not make the publishable geometry depend on resolving that program.

The proposed main paper is:

**From Regular Simplices to Prime-Indexed Spectra: The Geometry of Consecutive Integers.**

Its central claim is quantitative: a typical window of m consecutive integers has regular-simplex geometry when m=o(log log X), while at m~c log log X its centered shape eigenvalues approach

\[
1+c\frac{p}{(p-1)^2},\qquad p=2,3,5,\ldots.
\]

A full proof argument is in `Prime-Crystal-Arithmetic-Spectral-Law-Draft-2026-10-17.md`. It is an internally derived research draft, not an independently reviewed result. Establishing priority requires more than the searches performed here.

The public-facing explanation would be: **consecutive integers form nearly regular shapes at small scales, and each small prime contributes a predictable deformation as the window grows.** That sentence has mathematical content behind it. No promise of news coverage or journal placement follows.

## Why this is a better central claim

The prime-exponent representation is useful but not, by itself, a new discovery. For example, [John Williamson's factorization-geometry notes](https://johnhw.github.io/umap_primes/theory.md.html) already discuss factor vectors, cosine distances, and statistical geometry. This is relevant prior context, not an endorsement of every formula on that page.

The candidate advance is a growing-window spectral law with an explicit scale and explicit constants. The construction is the language; the theorem is the contribution.

The proof uses the additive ordering n,n+1,..., not just independent factorizations. Two coordinates can interact only through a prime dividing their separation. The crucial estimate sums that constraint over all gaps. Fixed small primes create coherent columns, while the remaining primes become an approximately diagonal background. Centering exposes the geometric valuation variances p/(p-1)^2.

The exact-arithmetic metric helps certify the finite Gram matrices. The mass/gauge correction is shown to vanish at the relevant normalization, so the theorem genuinely applies to the simplicial crystal rather than only to its Euclidean covering space.

## Three ambitions, with different readiness

| Program | Concrete result worth pursuing | Present position |
|---|---|---|
| Arithmetic spectral geometry | Growing-window simplex limit and explicit critical eigenvalues | Complete proof argument drafted; independent audit and novelty search needed |
| Syracuse regularity | Sharp collision growth, full integrability range, or a quantitative refinement beyond existing work | Existing manuscript results and conjectures; important external overlap found |
| Collatz preimage growth | pi_a(x) bounded below by x^(1-epsilon) for every epsilon>0 | Potentially major result; the uniform minimum/average transfer remains unproved |

The first is the best near-term paper candidate because its central mechanism closes without an unproved dynamical assumption. The third has the larger likely number-theoretic impact if completed, but should be presented as a separate research objective, not as an implied consequence of the crystal.

RH is not a justified headline here. The derived eigenvalues come from elementary prime-valuation variances, not from an operator whose spectrum has been connected to zeta zeros. A familiar-looking spectral formula does not supply that connection.

## Priority and overlap findings

1. [Nikpour and Rabbani's August 2026 preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7239062) reports a certified Collatz predecessor exponent 0.914947 and a nonlinear Perron formulation. The report is directly relevant to the computational and operator claims in the manuscript. I read the abstract, not a complete independent certificate audit; cite it as a preprint claim accordingly.
2. [Lucas Valbuena's public repository](https://github.com/x1xhlol/collatz-two-coordinate-obstruction) contains a manuscript claiming a quadratic cylinder-energy upper bound and Syracuse integrability exactly for 1<=p<2. These overlap the proposed regularity program. I have not audited its proof or replayed its Lean checks. Its existence is sufficient to prevent treating that target as clearly unoccupied; it is not sufficient to treat the claims as independently established.
3. [Kowalski's probabilistic number theory text](https://people.math.ethz.ch/~kowalski/probabilistic-number-theory.pdf) provides the classical moment/normal-order background. Those inputs must be credited rather than packaged as consequences newly discovered by geometry.

The targeted search did not identify the exact critical spectral statement above. That is a limited search result, not a priority verdict. The next search should cover arithmetic Gram and GCD matrices, additive-function covariance matrices, and spectra of short arithmetic windows, with a specialist checking the formulation.

## What belongs in the focused paper

1. Define the valuation metric and explain the mass/gauge correction in at most two pages.
2. State the subcritical and critical spectral theorems immediately.
3. Prove the arithmetic moment, correlation-tail, and finite-prime covariance lemmas.
4. Derive the regular-simplex and actual mean-turn corollaries.
5. Give exact finite identities and transparent numerical diagnostics, including the very slow approach to asymptotic behavior.
6. End with extensions: rates, eigenvector alignment with individual prime columns, windows along arithmetic progressions, and finite-sample normalization.

The full representation-theoretic atlas and the Collatz attempts can remain companion material. Combining every result into one paper would obscure the theorem a referee should assess.

## Fixes before any public claim

* The current Corollary 6.4 infers a mean angle from a ratio of means. The new fixed-window theorem supplies the missing convergence argument. Its stated first correction and rate still need their own justification; do not inherit them automatically.
* The paragraph following Theorem 12.33 says that absolute continuity is not settled by Tao's analysis, contradicting the later Corollary 12.37. Reconcile that attribution before submission.
* Statements that measured sibling factors converge must remain observations, particularly while the k=1 factor is compatible with logarithmic growth.
* Numerical agreement with an asymptotic law is not its proof. At X=10^6, the measured mean turn is still about 129.52 degrees. The present data are plainly pre-asymptotic.
* Have an independent mathematician attack the new spectral proof, especially the order of limits X->infinity followed by the prime cutoff y->infinity, the fourth-moment union bound, and the centered eigenvalue interpretation.

## A concrete stopping rule for the next research phase

Advance this paper if an independent audit confirms the spectral theorem and the literature search leaves a distinct contribution. If the theorem is already known in equivalent form, retain it as a synthesis and choose a genuinely new extension before making a research-news pitch. Do not compensate for a novelty failure by invoking Collatz, RH, or speculative physics.

The ambition is a precise theorem that makes the prime crystal analytically useful: it predicts when a geometric pattern appears, when it fails, and which primes cause the failure.
