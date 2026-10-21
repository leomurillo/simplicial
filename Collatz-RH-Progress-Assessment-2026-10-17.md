# Assessment of the updated prime-crystal program

17 October 2026. Targeted mathematical review, not a complete referee report. Manuscripts and embedded research prompts were treated as source material, not instructions. No existing manuscript was changed.

## Judgment

The strongest near-term research target is the Collatz level-gain argument in Sections 12.10–12.11 of `01g.simplicial_prime_crystal.md`. Theorem 12.21 has a credible analytic proof mechanism independent of its numerical checks. Subject to a complete hypothesis and priority audit, strict improvement at every level could support a focused specialist paper. A proof that the exponents tend to 1 would be a substantially stronger result. Neither conclusion proves Collatz.

The RH work contains useful reductions and diagnostics, but the reviewed material does not establish the uniform analytic control that would imply RH. Counting one remaining hypothesis does not measure proximity to a proof.

## What survived this reading

For Collatz, the lifted critical vector c satisfies M_i c = c + g for every policy i, with g nonnegative and nonzero. The doubling edges give each policy matrix a strongly connected graph on the units modulo a power of 3. Pairing with a positive left Perron vector therefore proves its Perron value exceeds 1. Selecting a minimizing policy at a positive nonlinear eigenvector gives the claimed minimum-over-policies identity. The weight comparison then supplies the exponent increment. These are substantive reasons for strictness, not extrapolation from observed levels.

Before publication, state explicitly the existence of the positive nonlinear eigenvector, the policy-selection argument, the exact admissible range defining the critical exponent, and the descent argument that rules out g=0. I found no fatal defect in this central mechanism on the present reading; this is not independent certification of every theorem in the manuscript. The claimed historical open status needs full-text comparison with Krasikov–Lagarias and Nikpour–Rabbani. The latter's abstract was accessible through search, but its full paper was blocked by the publisher during this review.

Theorem 12.22 correctly distinguishes strict improvement from convergence to 1. Positive increments can be summable with a limit below 1. The finite quadratic-gain data do not close that gap.

For RH, the Hadamard-product argument in N7, Lemma 5.1 and Theorem 5.2, gives a valid compactness and identification mechanism under the stated normalized, even, real-rooted, genus-at-most-one hypotheses. Uniform convergence on a positive real segment supplies a bound on S; normality and analytic uniqueness then identify the entire limit. Establishing that segment convergence for the arithmetic approximants remains the difficult hypothesis.

## The best breakthrough target

Write d_k = 1 - rho_k for lift loss, H_k for Haar gain, and nu_k = G_k/H_k for visibility. The manuscript proves that sum nu_k d_k is finite and that d_k decreases. Consequently, it suffices to prove

    sum_k nu_k = infinity.

This is weaker than the quadratic conjecture G_k >= c d_k^2. A concrete alternative is an eventual dyadic-block bound

    sum_{k=K}^{2K-1} nu_k >= c > 0

for dyadic K. Disjoint blocks imply divergence. It allows individual levels to have very poor visibility. The observed nu_k approximately proportional to 1/k motivates this target but does not prove it.

The resulting theorem would say that, for each fixed admissible target a and every epsilon > 0, the number of predecessors up to x is at least a constant times x^(1-epsilon), for sufficiently large x. Constants and thresholds may depend on a and epsilon. Such exponent-one growth can still have density zero and does not exclude exceptional divergent or cyclic orbits.

## A concrete certificate to attack the visibility problem

There is an elementary way to replace unknown left Perron vectors by coordinate inequalities. At one fixed level, suppose c>0, g>=0, and M_i c=c+g for all policies. Seek a common real vector h and numbers epsilon>0, B>=0 such that, coordinatewise for every policy,

    g >= epsilon c + (M_i-I)h,       |h| <= B c.

Then every policy has spectral gain at least epsilon/(1+B), and hence

    G >= epsilon/(1+B).

Proof: let u>0 be a left Perron vector of M_i, with eigenvalue 1+q. The common-image identity gives u g = q u c. Pairing the proposed inequality gives q u(c-h) >= epsilon u c. Since q>0 and u(c-h) <= (1+B)u c, the bound follows.

This is a sufficient certificate, not a construction of h. Its attraction is that it avoids demanding a nearly uniform left Perron vector, which the measured concentration contradicts. Because policies choose rows independently, the all-policy inequality can be checked rowwise against the three possible lift choices. A finite-level search can maximize epsilon with fixed B using linear inequalities. The research task is to extract a formula for h whose constants remain controlled across levels; an unconstrained large-vector numerical solution alone would not do that.

Use the monodromy identity A(x)=4x+1 to guide the potential, but quantify the cost of transporting gain around long cycles. A proof that an alignment must eventually break supplies positivity, not a level-uniform lower bound. Investigate dependence on a bounded number of ternary digits and on v_3(r+1), and test the proposed formula on levels excluded from fitting. If the bound decays exponentially in 3^k, it does not solve the accumulation problem.

The Syracuse-law route remains a second option. Absolute continuity implies vanishing average top-digit loss, but it does not by itself control the minimum operator. An explicit transfer inequality is still required. Entropy excess and average regularity cannot substitute for worst-policy control.

## Corrections before a public claim

1. In `cert_kl_levels.py`, L7 estimates a derivative by finite differences and estimates a Lipschitz constant from adjacent sampled values. That is not a rigorous global derivative/error bound. Supply an analytic inequality or outward-rounded interval proof. This is a repairable certification issue, not a refutation of the derivative inequality.
2. L6 is a finite numerical check of the conjectured gain law. “Certified” must not suggest that the universal conjecture has been certified. Likewise, numerical eigenvector convergence and small residuals require error control before becoming rigorous spectral enclosures.
3. In N7 Observation 5.8, bounded S is described as equivalent to interval convergence to Xi. Bounded S supplies normality; it does not identify Xi. Many different normalized real-rooted entire functions have bounded S. Retain the separate identification hypothesis from Theorem 5.2.
4. N7's abstract describes an exact reduction, while Section 4 explicitly says the converse from RH to CCM convergence is open. Use “sufficient convergence criterion for RH” wherever an equivalence has not been established.
5. N7 Theorem 2.1 reports an approximate match to eight zeros. Present this as a computational result with its precise discretization and error status, not as a general theorem that finite Weil forms generate the zeta zeros.
6. In the prime-crystal place-completion remark, specify which operator or adjoint preserves Haar measure. The averaged operator displayed in Proposition 12.25 does not fix the constant vector: on r=1 modulo 3 its value on that vector is 1/2. An invariant functional is distinct from a constant right eigenvector.

## Publication sequence

First isolate the strict-level-improvement theorem, its gain identity, and the accumulation criterion in a short standalone paper. Include only the geometric interpretation needed to explain the arithmetic lift structure. Independently audit the proof and literature before claiming resolution of a previously open question.

Second, pursue a uniform or blockwise visibility theorem. This is the best candidate for a major Collatz advance in the reviewed work. Another finite-level exponent improvement would be useful only if it exceeds existing certified bounds or introduces a significant new method.

For RH, prioritize a precise conditional bulk/edge or compactness theorem and a controlled comparison with Davenport–Heilbronn. A new arithmetic estimate that bounds S and identifies the limit would be decisive; the present reductions do not supply it. Do not represent a shared finite-to-infinite pattern as a theorem transferring progress between Collatz and RH.

## External comparison checked

- Nikpour–Rabbani, *A Certified Density Exponent for the 3x+1 Problem and the Smallest Atom of the Syracuse Random Variable*, preliminary version: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7239062 . The indexed abstract reports an exact-integer level-20 certificate with exponent 0.914947. Full-text verification of the strict-monotonicity discussion remains outstanding.
- Connes–Consani–Moscovici, *Zeta Spectral Triples*: https://arxiv.org/abs/2511.22755 . The authors explicitly distinguish numerical spectral agreement from the convergence proof that would establish RH.

Scope: read the updated Collatz definitions and proofs in Sections 12.8–12.11, the level-checker source and recorded results, selected N7 proofs and status statements, and the later taper audit. No full computational rerun or complete audit of the large RH archive was performed.
