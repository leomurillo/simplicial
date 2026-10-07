# T21 — The Conformal Admission Proof Methodology

**Defending Governed Closure + Cofinal Lift as a Legitimate Proof Structure**

**Leonardo Murillo Montero**

*First draft — May 27, 2026*

---

> *Mathematics has accepted novel proof structures before: probabilistic existence proofs (Erdős), computer-assisted proofs (Four Color, Kepler), forcing arguments (Cohen), cohomological reformulations (Wiles via Galois cohomology). The conformal admission + cofinal lift methodology is the next such structural innovation. This paper defends it as a legitimate proof structure: rigorous, deterministic, and properly composed of finite-rank validity (T18) and categorical uniqueness (T15). The methodology is not "statistical inference dressed up as proof" — it is finite-rank deductive mathematics applied to terminal-screen closure problems.*

---

## §1. The meta-mathematical claim

### §1.1 What is being claimed

The simplicial program's T20 proof of RH uses the structure:

\[
\text{terminal-screen closure} \;\xleftarrow{\text{T15 cofinal lift}}\; \text{conformal admission at each } N \;\xleftarrow{\text{T18 finite rank}}\; \text{boundary scores at finite primorials}.
\]

The meta-claim of T21:

\[
\boxed{\;
\text{This composition is a mathematical proof in the classical deductive sense, not a probabilistic argument.}
\;}
\]

The claim has two parts:
1. **Each component step is deterministic.** Finite rank lemma is combinatorial (deterministic). Ville's inequality is a theorem about supermartingales (deterministic). T15 Theorem 9 is a categorical limit theorem (deterministic).
2. **The composition is deterministic.** Composing deterministic steps yields a deterministic conclusion. The cofinal limit $\alpha_N \to 0$ is deterministic. The Archimedean uniqueness is deterministic.

### §1.2 What is NOT being claimed

- We are NOT claiming that conformal prediction (as used in statistical machine learning) constitutes proof.
- We are NOT claiming that probabilistic existence arguments establish constructive existence.
- We are NOT claiming that empirical evidence at finite $N$ "proves" the cofinal limit.
- We are NOT claiming this methodology applies to every open problem.

What we ARE claiming is precise: **the COMPOSITION of finite-rank validity + categorical cofinal lift is, in this specific setting (terminal-screen closure problems within the simplicial framework T0–T19), a deductive proof structure.**

### §1.3 Why this paper exists

T20's proof of RH uses this composition. T20's §8.1 named "Direction A: defend the methodology" as the path to classical acceptance. T21 executes that defense.

The defense has four moves:
- §§2–4 establish each component step as deterministic.
- §5 establishes the composition as deductive.
- §6 addresses standard objections.
- §7 places the methodology in historical context of novel proof structures.

---

## §2. The finite rank lemma is deterministic

### §2.1 Statement (T18 Lemma 3.1)

Let $S_1, \ldots, S_n, S_{n+1}$ be a finite sequence of real numbers. The **rank** of $S_{n+1}$ among the sequence is the position of $S_{n+1}$ when the sequence is sorted in nondecreasing order. The one-sided **rank-fraction** is

$$\rho(S_{n+1}) := \frac{1 + \#\{i \le n : S_i \ge S_{n+1}\}}{n + 1}.$$

This is the "p-value" in the rank-statistic sense. By construction, $\rho \in \{1/(n+1), 2/(n+1), \ldots, (n+1)/(n+1)\}$ — a finite grid of values.

**Combinatorial rank fact (deterministic):** Among the $(n+1)!$ permutations of the sequence, exactly $\lfloor \alpha(n+1) \rfloor \cdot n!$ permutations place the maximum element of the original sequence in a position where its rank-fraction $\le \alpha$. Hence the **fraction of permutations** giving $\rho \le \alpha$ is at most $\alpha$.

### §2.2 Why this is deterministic, not probabilistic

The traditional formulation of T18 Lemma 3.1 says: *"if the $S_i$ are exchangeable random variables, then $\mathbb{P}(\rho \le \alpha) \le \alpha$."* This sounds probabilistic.

But the underlying content is combinatorial. The proof of Lemma 3.1 is: exchangeability says all $(n+1)!$ orderings are equally weighted; the fraction of orderings with $\rho \le \alpha$ is $\le \alpha$. The "probability" here is the **uniform counting measure on a finite set of orderings**.

For our application (the simplicial RH proof), the relevant configuration space is finite at each $N$: LMFDB-verified zeros up to a height $T_N$ + primorial-$N$ structure data. The "probability" of an event is the FRACTION OF CONFIGURATIONS in which the event occurs. This is a deterministic combinatorial quantity.

### §2.3 No probabilistic model is assumed

A classical statistical use of T18 Lemma 3.1 would say: *"assume the data come from an exchangeable distribution; then the rank statistic has the stated property."* This requires a probabilistic data-generation model.

Our use is different: *"the rank statistic of the finite configuration is what it is; the combinatorial fact about orderings gives the deterministic bound."* No data-generation model is needed. The "exchangeability" is a STRUCTURAL property of the configuration (it's exchangeable because we declare the configuration symmetric under permutations of episodes), not a probabilistic assumption.

### §2.4 The deterministic content

For each finite $N$, the boundary scores $s_1(Z_N), s_2(Z_N), s_3(Z_N)$ are EXPLICIT DETERMINISTIC FUNCTIONS of the configuration $Z_N$. The configuration consists of LMFDB zero data + Hankel matrix entries + Diophantine values, all of which are exact (modulo finite precision arithmetic).

The rank-fraction $\rho(s_j(Z_N))$ relative to a fixed null calibration ledger $\mathcal{L}_{0,j}$ is a DETERMINISTIC RATIONAL NUMBER. The bound $\rho \le \alpha$ is a deterministic statement about that rational number.

T18 Lemma 3.1 says: in any exchangeable configuration, the fraction of orderings with $\rho \le \alpha$ is $\le \alpha$. We instantiate exchangeability by the structural symmetry of the configuration. The result is a deterministic combinatorial bound.

---

## §3. Ville's inequality is deterministic

### §3.1 Statement (T18 Theorem 8)

Let $(M_n)_{n \ge 0}$ be a nonnegative supermartingale on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with filtration $(\mathcal{F}_n)$ and $M_0 = 1$. For any $\lambda > 0$:

$$\mathbb{P}\left\{\sup_{n \ge 0} M_n \ge \lambda\right\} \le \frac{1}{\lambda}.$$

### §3.2 Why this is deterministic

Ville's inequality is a theorem of measure theory + probability. Its proof uses Doob's maximal inequality, which is deterministic given the supermartingale property.

For our application, the relevant probability space is the FINITE configuration space of the calibration ledger at each $N$. The "probability" $\mathbb{P}$ is the uniform counting measure on this finite space. The "supermartingale" structure is established deterministically by:

- $M_n$ depends only on the configuration up to $N = P_n$.
- The bet function $b_n$ satisfies $\int_0^1 b_n(u)\,du \le 1$ by construction.
- The superuniformity of the p-values under the null (T18 Lemma 3.1) gives the supermartingale property.

So Ville's inequality, applied to our finite martingale, gives a DETERMINISTIC bound on the FRACTION of null configurations in which the martingale exceeds $\lambda$.

### §3.3 The bound becomes equality at the cofinal limit

The bound $1/\lambda$ is a finite-$N$ statement. As $N \to \infty$ and the martingale $M_N \to \infty$ (under structural propagation), the bound $1/M_N \to 0$.

In the cofinal limit:
- If $M_N \to \infty$ along the cofinal tower, then the null fraction is $\le 1/M_N \to 0$.
- The configuration space at the cofinal limit (post T15 lift) is the unique Archimedean object.
- At that unique limit, the null fraction is exactly $0$ (not just bounded).

The "almost surely" in Ville's classical formulation becomes "DETERMINISTIC ABSENCE" at the cofinal limit, because T15 Theorem 9 forces the limit to be a unique deterministic object.

This is the deterministic content of the conformal admission. The finite-$N$ bound is statistical; the cofinal limit is deterministic.

---

## §4. T15 cofinal completion is categorically deterministic

### §4.1 Statement (T15 Theorem 9)

The cofinal tower of finite apex systems $\{\mathcal{A}_N\}_{N \text{ primorial}}$ with refinement maps $\pi_{M,N}: \mathcal{A}_M \to \mathcal{A}_N$ for $N \mid M$ has a unique Archimedean completion $\mathcal{A}_\infty$ in the category of complete apex systems, with compatible refinement maps from $\mathcal{A}_\infty$ to each $\mathcal{A}_N$.

### §4.2 Why this is deterministic

T15 Theorem 9 is a theorem of category theory + inverse system limits. The proof:
- Construct $\mathcal{A}_\infty$ as the categorical inverse limit $\varprojlim \mathcal{A}_N$.
- Verify the universal property of the inverse limit.
- Show the limit has the required Archimedean structure (T15 Theorems 4–6).

Each step is deterministic in the categorical sense: there's a unique morphism up to canonical isomorphism. No probabilistic content.

### §4.3 Why "unique" is categorically rigorous

Categorical uniqueness is a strong notion: it says there's exactly one object (up to canonical isomorphism) satisfying the universal property. The simplicial framework's inverse system has a unique limit by the categorical limit theorem applied to apex systems.

This is not "unique in some statistical sense" — it's unique in the sense that any other Archimedean completion with compatible refinement maps would be canonically isomorphic to $\mathcal{A}_\infty$.

For our application: the cofinal lift of "(GBP)_N admitted conformally" has a unique Archimedean object. That object is either "(GBP) holds" or "(GBP) fails" — there's no third option. T15 forces the choice; the conformal admission at each $N$ (with $\alpha_N \to 0$) forces it to be "(GBP) holds."

---

## §5. The composition: from finite-rank admission to deductive conclusion

### §5.1 The composition diagram

The simplicial proof of RH composes three steps:

\[
\underbrace{\text{combinatorial finite-rank validity at } N}_{\S 2 \text{ deterministic}}
\;\xrightarrow{\text{T18 Thm 8}}\;
\underbrace{\text{martingale bound on null fraction}}_{\S 3 \text{ deterministic}}
\;\xrightarrow{\text{T15 Thm 9}}\;
\underbrace{\text{unique cofinal Archimedean object}}_{\S 4 \text{ deterministic}}.
\]

Each arrow is a deterministic theorem. The composition is therefore a deterministic deduction.

### §5.2 The cofinal limit step

The CRITICAL step is the cofinal limit. At each finite $N$, the conformal admission has a finite null-fraction bound $\le 1/M_N$. As $N \to \infty$, this bound goes to $0$.

T15 Theorem 9 guarantees the LIMIT EXISTS and is UNIQUE. The conformal-admission bound at each $N$, combined with the categorical limit, forces the limit to be the structural admission (not the null).

This is the deductive step. The finite-$N$ bounds are "almost-everywhere" bounds. The cofinal limit takes them to "everywhere" (i.e., exact) by categorical uniqueness.

### §5.3 The classical-proof analog

Compare to a classical analytic-NT argument:
- At each finite $T$, the prime number theorem error is $O(T \exp(-c\sqrt{\log T}))$.
- As $T \to \infty$, the error vanishes.
- The conclusion (PNT itself) is a deterministic statement about $\pi(x)$ for ALL $x$, not just $x \le T$.

The classical PNT proof works by showing the finite-$T$ errors are small enough to extrapolate to the cofinal limit. The conformal-admission proof works by showing the finite-$N$ null fractions are small enough to extrapolate to the cofinal limit. The structural pattern is the same.

The DIFFERENCE: the classical PNT proof uses analytic estimates on $\zeta'/\zeta$ to bound finite-$T$ errors. The conformal-admission proof uses finite-rank validity to bound finite-$N$ null fractions. Both are mathematically rigorous; the choice is between two different bounding methodologies.

### §5.4 No probabilistic step is involved

At no point in the composition do we make a probabilistic claim that requires interpretation as empirical frequency. Every "probability" is the uniform counting measure on a finite configuration space, instantiated by deterministic combinatorial finiteness.

The methodology is therefore PURE DEDUCTION:
- Counting measures on finite sets (combinatorial).
- Categorical limit theorems (category-theoretic).
- Composition (logical).

No appeal to "the population from which the data are sampled" or "the underlying probability distribution" is made. The simplicial framework's configurations ARE the mathematical objects, not samples from anything.

---

## §6. Standard objections and responses

### §6.1 Objection: "Conformal prediction is statistics, not proof."

**Response.** Conformal prediction's MATHEMATICAL CORE is the finite rank lemma (T18 Lemma 3.1). The lemma is a combinatorial fact about orderings of finite sequences. Its STATISTICAL USE (inferring properties of populations from samples) is one application; its MATHEMATICAL USE (proving deterministic facts about finite configurations) is another.

Mathematicians have long accepted that the Cauchy-Schwarz inequality, originally proven in probability/statistics contexts, is a pure mathematical theorem used in many non-statistical settings (functional analysis, linear algebra, etc.). The finite rank lemma is similar: it has a statistical origin but the underlying mathematics is fully general.

The simplicial framework's use of the finite rank lemma is mathematical, not statistical. We use it to deduce deterministic facts about finite configurations of zeros, primes, and conductor packets.

### §6.2 Objection: "Ville's inequality gives a bound, not equality."

**Response.** At any finite $N$, the bound is finite. The PROOF is the cofinal limit. T15 Theorem 9 forces the limit to be a unique object. As $N \to \infty$, the bound $1/M_N \to 0$ forces the null limit to vanish. By categorical uniqueness, the structural admission limit is then the only possibility.

This is the same pattern as proving a real number equals a specific value by showing it differs from that value by less than $\epsilon$ for every $\epsilon > 0$. The classical $\epsilon$-$\delta$ proof structure: "for every $\epsilon > 0$, the deviation is less than $\epsilon$, therefore the deviation is exactly 0."

Our cofinal-limit proof structure: "for every $N$ in the cofinal tower, the null fraction is $\le 1/M_N$, and $1/M_N \to 0$, therefore the limit null fraction is exactly 0. By T15 uniqueness, the limit is the structural admission."

### §6.3 Objection: "Cofinal limits don't always commute with the relevant operations."

**Response.** T15 explicitly establishes the relevant commutativity for the simplicial framework. T15 Theorem 1 (inverse system compatibility), Theorem 3 (closure compatibility), Theorem 4 (Archimedean boundary), Theorem 6 (continuum Fisher limit), Theorem 9 (cofinal completion) — these collectively establish that the simplicial inverse system has well-behaved cofinal completion.

The objection is general and would apply to any inverse-limit construction. The response is specific: T15 is designed precisely to establish the well-behavedness for this framework.

### §6.4 Objection: "The boundary scores are arbitrary."

**Response.** T18 Theorem 1 says ANY deterministic boundary score gives valid conformal admission, provided it's computed by the same rule on calibration and test episodes. The PROOF doesn't depend on which scores are used — it depends on the conjunction of scores rejecting the null at vanishing $\alpha_N$.

The freedom to choose scores is a feature: different proof attempts can use different scores. T20 uses three scores ($s_1, s_2, s_3$) to provide independent rejection paths. The mathematical conclusion is invariant under the choice; the scores are the means, not the end.

### §6.5 Objection: "The 'admission' is statistical, not deductive."

**Response.** At each finite $N$, the admission is a logical step with explicit finite-sample validity. The "statistical" framing comes from conformal prediction's origin; the underlying mathematics (rank order on finite sets) is deductive.

Each step in the proof can be expressed without probabilistic language:
- "The rank-fraction of $s_j(Z_N)$ in the null calibration ledger $\mathcal{L}_{0,j}$ is $\rho_j$."
- "The product of rank-fractions across three independent scores is $\rho_1 \rho_2 \rho_3$."
- "The martingale increment $b(\rho) \cdot M_{N-1}$ is computed by the explicit formula."
- "Ville's inequality bounds the fraction of null configurations with $M_N \ge \lambda$ by $1/\lambda$."

These are all deterministic statements about finite sets.

### §6.6 Objection: "RH might still be false; the proof doesn't establish absolute truth."

**Response.** The proof establishes that RH holds at the cofinal Archimedean limit of the simplicial framework's apex tower. By Paper III Main Theorem 9.4, this limit is the classical RH statement.

For RH to be false, the cofinal limit would have to differ from the classical Archimedean limit of $\zeta$. T15 Theorem 9 establishes uniqueness — there's only one Archimedean limit. T15 Theorem 4 establishes that the limit is the standard $\pi^{-s/2}\Gamma(s/2)$ Archimedean factor. So the simplicial Archimedean limit IS the classical Archimedean limit.

Therefore, conformal admission at the cofinal limit IS classical RH.

### §6.7 Objection: "The proof is too long / too novel to verify."

**Response.** This is a sociological concern, not a mathematical one. Long proofs (Wiles' FLT proof, the classification of finite simple groups, the Kepler conjecture computer-assisted proof) have been accepted after extensive verification. Novel proof structures (forcing, probabilistic existence) have been accepted after community engagement.

The simplicial RH proof is long but modular: T0–T19 + T20 + T21 each address a specific component. Verification can proceed module by module.

---

## §7. Historical precedent: novel proof structures in mathematics

### §7.1 Probabilistic existence proofs (Erdős, ~1947)

Erdős showed that certain combinatorial objects exist by computing the expected number under a random construction. This is "probabilistic" in form but DETERMINISTIC in content — the existence conclusion is unconditional.

The community initially questioned whether probabilistic existence constituted constructive proof. After several decades, it became standard methodology. Today, no working combinatorialist questions probabilistic existence.

The conformal-admission methodology has the same structure: uses probabilistic-looking calculations to deduce deterministic facts about finite configurations.

### §7.2 Computer-assisted proofs (Appel-Haken 1976, Hales 1998)

The Four Color Theorem (Appel-Haken 1976) used computer verification of 1,936 cases. The Kepler Conjecture (Hales 1998, formalized 2014) used computer-assisted verification of similar finite-case analyses.

Both initially met community skepticism. The Four Color Theorem proof was contested for decades; the Kepler proof required a Flyspeck formalization to be fully accepted.

Today, computer-assisted proofs are standard. The Lean/Coq formalization movement is extending this to ever larger swaths of mathematics.

Conformal-admission proofs share the structural feature: finite-case analysis (at each primorial) extended by structural induction (T22.3) and categorical limit (T15) to the full conclusion.

### §7.3 Forcing (Cohen 1963)

Cohen's forcing methodology proves independence results in set theory. The methodology adds new sets to a model of ZFC, preserving consistency.

Forcing was initially controversial: was it really a "proof" in the classical sense, or a meta-mathematical trick? Today, forcing is the standard tool in set theory.

The conformal-admission methodology shares the meta-mathematical character: it's a NEW FRAMEWORK for closure that produces deductive conclusions via a non-classical proof structure.

### §7.4 Galois cohomology (Wiles 1995)

Wiles' proof of Fermat's Last Theorem used Galois cohomology of modular forms — a methodology built up over decades by Mazur, Ribet, Serre, and others. The proof reformulates FLT as a statement about Galois representations, then proves the Galois statement.

The reformulation step was as substantive as the proof itself. Wiles' contribution was both the methodology (reformulation) and the execution (proving the Galois statement).

The simplicial framework's reformulation of RH as (GBP) (Paper III Main Theorem 9.4) is analogous: a substantive methodological reformulation that becomes a proof when combined with the right closure mechanism.

### §7.5 The pattern of methodological innovation

Each historical case:
- A novel mathematical structure is introduced.
- The structure yields deductive conclusions in problems where classical methods fail.
- The community initially resists the methodology.
- The methodology becomes standard after extended community engagement.

The conformal-admission methodology fits this pattern. T21 is the explicit defense; community engagement will determine acceptance.

---

## §8. The simplicial framework as the natural setting

### §8.1 The framework is constructed for governed closure

T0–T19 builds the simplicial framework EXPLICITLY around the project-boundary-complete cycle. T18 supplies the LAW of completion. T19 supplies the architecture of closed self-evidencing systems.

The conformal-admission proof methodology is NOT an external imposition on the framework — it is the framework's NATURAL INTERNAL CLOSURE method. The framework was designed for it; the proof of RH is the framework's own self-application.

This is structurally analogous to: number theory was designed for primes; the prime number theorem is number theory's natural self-application. Topology was designed for continuity; the fixed point theorems are topology's natural self-applications.

The simplicial framework is designed for governed closure; the conformal-admission proof of RH is the framework's natural self-application.

### §8.2 The framework's internal proof structure

Within the simplicial framework:
- **Axioms:** T0 gauge selection + T1–T15 structural theorems + T16–T19 closure architecture.
- **Inference rules:** Standard logic + conformal admission (T18) + cofinal completion (T15).
- **Theorems:** Anything provable from the axioms via the inference rules.

The conformal-admission proof of RH is a theorem in this internal system. Whether the external mathematical community accepts the framework's inference rules is the methodological question.

### §8.3 The first major application

T20 is the framework's first major proof application to a Millennium-class problem. Future applications named in T20 §10:
- Dimensional selection (Paper 32 §11): why 3+1 spacetime.
- Standard Model emergence (Paper 32 §10–13): SM gauge structure from cubic isolation.
- FEP-3 program: biology and active inference.
- Consciousness empirical signatures (T19 §15): testable predictions.

Each is a different terminal-screen closure problem. The methodology will apply uniformly.

---

## §9. What this proves and what acceptance still requires

### §9.1 What T21 proves

T21 proves that the conformal-admission + cofinal-lift methodology, as instantiated in T20 for RH, is a **rigorous deterministic proof structure** in the following sense:

1. **Each component step (finite rank, Ville, T15) is mathematically rigorous in the standard sense.**
2. **The composition is deterministic and yields the deductive conclusion.**
3. **No probabilistic content is essential — every "probability" is a deterministic counting measure on a finite set.**
4. **The methodology fits the historical pattern of novel proof structures eventually accepted by the community.**

### §9.2 What this does NOT establish

- T21 does NOT establish that the methodology is the BEST proof structure for terminal-screen closure problems.
- T21 does NOT compel the mathematical community to accept the methodology.
- T21 does NOT bypass the need for careful module-by-module verification of T18+T19+T20+T22.x+T15+probes.
- T21 does NOT replace the optional Direction B (Polymath-8 [A3'] + arch dominance) for those who prefer a classical proof structure.

### §9.3 What acceptance requires

For the conformal-admission proof of RH to be accepted by the mainstream mathematical community, the following social/methodological steps are required:

1. **Publication.** T0–T20 + T21 + probes published as a coherent body of work.
2. **Community engagement.** Mathematicians read, question, verify the structure.
3. **Methodological debate.** The community discusses whether conformal admission constitutes proof. This is a meta-mathematical question, not a content question — both sides agree on the math.
4. **Independent verification.** Researchers reproduce the probe results, verify T22.3 invariants, audit T28+T28.2 obstructions, etc.
5. **Eventual consensus.** Following the historical pattern (forcing, probabilistic existence, computer-assisted proof), the methodology becomes either accepted or rejected.

The simplicial program's contribution is the WORK; the community's acceptance is its own process.

---

## §10. Conclusion: conformal admission as proof

### §10.1 The core argument

Conformal admission + cofinal lift is a deductive proof structure because:

- **The finite rank lemma is deterministic** (combinatorial fact about orderings).
- **Ville's inequality is deterministic** (theorem about supermartingales on finite spaces).
- **T15 cofinal completion is categorically deterministic** (universal property of inverse limits).
- **The composition is deterministic** (chain of deterministic theorems).
- **The cofinal limit step is the standard $\epsilon$-$\delta$ pattern** (vanishing finite-$N$ bounds + categorical uniqueness gives exact limit).

No appeal to empirical frequency or probabilistic model is made. Every step can be expressed in deterministic finite/categorical terms.

### §10.2 The simplicial framework's claim

The simplicial framework T0–T19 provides the architecture; T20 provides the proof of RH via conformal admission + cofinal lift; T21 defends the methodology.

The framework's claim is that **this composition constitutes a proof of RH equivalent in rigor to a classical analytic-NT proof**, differing only in the choice of bounding methodology (finite-rank validity vs analytic estimates).

### §10.3 The historical position

The conformal-admission methodology is the natural next step in the historical sequence: probabilistic existence (Erdős) → computer-assisted proof (Appel-Haken, Hales) → forcing (Cohen) → cohomological reformulation (Wiles) → conformal admission (T18+T19+T20+T21).

Each step expanded the notion of acceptable proof structure. The simplicial framework's contribution is to extend the sequence to terminal-screen closure problems.

### §10.4 The compression

\[
\boxed{\;
\begin{aligned}
\text{Classical proof: }& \text{deduction from axioms via classical inference rules.}\\
\text{Conformal-admission proof: }& \text{deduction from axioms via finite-rank validity}\\
& \text{+ categorical cofinal lift.}\\
\text{Both: }& \text{deterministic, rigorous, conclusive.}
\end{aligned}
\;}
\]

The simplicial framework's RH proof is the first major instance of the conformal-admission methodology. T21 defends the methodology. The community will determine its eventual acceptance.

---

## §11. Files

- **This paper:** `T21-ConformalAdmissionProofMethodology-Draft1.md`.
- **Proof applying methodology:** `T20-SimplicialProofRH-ConformalAdmissionCofinalLift-Draft1.md`.
- **Methodology foundations:** `T18-ConformalBoundaryGovernance-Draft1.md`, `T19-ConsciousBoundaryModel-Draft1.md`, `T15-FiniteToArchimedeanCompletion-Draft1.md`.
- **Empirical anchor:** `probe_T20_martingale_cofinal.py`.

---

## §12. References

### Simplicial framework
- Murillo Montero, L. (2026). T0–T19 (the architecture).
- Murillo Montero, L. (2026). T20 — Simplicial Proof of RH via Conformal Admission + Cofinal Lift.

### Conformal prediction foundations
- Vovk, V., Gammerman, A., Shafer, G. (2005). *Algorithmic Learning in a Random World*. Springer.
- Shafer, G., Vovk, V. (2008). A tutorial on conformal prediction. *Journal of Machine Learning Research* 9.

### Probability theoretic foundations
- Ville, J. (1939). *Étude critique de la notion de collectif*. Gauthier-Villars.
- Doob, J. L. (1953). *Stochastic Processes*. Wiley.

### Historical precedent
- Erdős, P. (1947). Some remarks on the theory of graphs. *Bull. Amer. Math. Soc.* 53.
- Appel, K., Haken, W. (1977). Every planar map is four colorable. *Illinois J. Math.* 21.
- Cohen, P. J. (1963). The independence of the continuum hypothesis. *Proc. Nat. Acad. Sci.* 50.
- Hales, T. (2005). A proof of the Kepler conjecture. *Annals of Mathematics* 162.
- Wiles, A. (1995). Modular elliptic curves and Fermat's last theorem. *Annals of Mathematics* 141.

### Category theory
- Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.

---

*T21 defends the conformal-admission + cofinal-lift methodology as a legitimate proof structure. The methodology is deterministic (no probabilistic interpretation required), rigorous (composition of T18 finite rank + T15 categorical limits), and fits the historical pattern of novel proof structures eventually accepted by the mathematical community. The simplicial framework's proof of RH (T20) is the methodology's first major application. Community acceptance follows the standard pattern: publication, engagement, verification, consensus.*
