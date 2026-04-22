# §8 Cycle 2 Formalism Re-Audit — Reviewer X

**Scope.** Verification of the Author's Cycle 2 landing against Cycle 1 findings `[S8-H-1]`, `[S8-H-2]`, `[S8-M-1]`–`[S8-M-4]`, and the three Lows taken (`[S8-X-L-2]`, `[S8-X-L-5]`, `[S8-Y-L-1]`). Re-read §8 (now ~lines 453–483), §1.2 item 6 (line 61), §2.4 (Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$), and §3.4 (line 271) for cross-checks.

## Per-finding landing verdicts

**`[S8-H-1]` — Higher-$N$ wedge-Hodge rank and Lie-theoretic obstruction — CLOSED.**
The new §8.1 middle paragraph correctly states: a wedge of $N-3$ simplicial vectors in $H$ is decomposable; its Hodge dual (a 2-form in an $(N-1)$-dim space) is simple; the associated skew operator is rank 2; and the Rodrigues identity $K^3 = -c^2 K$ therefore applies to each *blade* generator individually for all $N \geq 4$. The obstruction is now correctly re-located to the Lie-theoretic count $\dim \mathfrak{so}(N-1) = \binom{N-1}{2} > N-1$ for $N-1 \geq 4$, forcing a generic element of $\mathfrak{so}(N-1)$ to be a linear combination of non-commuting blade generators, whose exponentials do not refold to a single trigonometric closed form. Dimension arithmetic: for $N=5$, $\binom{4}{2}=6 > 4$; for $N=4$, $\binom{3}{2}=3=N-1$, consistent with the $N=4$ uniqueness. The erroneous "rank greater than 2 / higher-degree minimal polynomial" story is fully excised.

**`[S8-H-2]` — Fixed-subspace claim restricted to simple rotations — CLOSED.**
The corrected sentence "Each individual blade-generated rotation fixes a subspace of dimension $(N-1) - 2 = N - 3$" now binds the grammatical subject to a simple rotation (image under $\exp$ of a single rank-2 blade), which is exactly the scope in which the $N-3$ count holds. The false blanket claim about generic $\mathrm{SO}(N-1)$ is gone. The comparison clause "strictly less than the $N-2$ that a single 1-parameter rotation family in the 3D sense would require" is mathematically correct ($N-3 < N-2$).

**`[S8-M-1]` — "Within our framework" hedge + Eckmann disclaimer — CLOSED.**
The §8.1 final paragraph carries the italicized hedge "*within the simplicial wedge–Hodge framework developed here*", mirroring §1.2 item 6. The octonion disclaimer — "The $n = 7$ octonionic binary cross product admitted by Eckmann's classification arises from a different algebraic structure (non-associative division algebras) and lies outside the framework of this paper (§1.2 item 6)" — is accurate and carries a clean cross-reference. The redundant dimension count has been moved to the preceding paragraph where it carries actual load; the two paragraphs tell a single consistent story.

**`[S8-M-2]` — Weierstrass attribution detached from Wildberger — CLOSED.**
"Substituting the Weierstrass parameter $t = \tan(\theta/2)$ into our formula — in the spirit of Wildberger's program of rational trigonometry [Wildberger] — yields …" The Weierstrass substitution stands unattributed (it is classical, 19th century); Wildberger appears only as author of the rational-trigonometry program.

**`[S8-M-3]` — Concrete "$\sqrt{3}\,u \in \mathbb{Q}^4$" rationalization condition — CLOSED.**
The undefined "tetrahedral symmetry family" has been replaced by the precise condition: axes $u \in H$ with $\sqrt{3}\,u \in \mathbb{Q}^4$. The accompanying justification is mathematically correct: entries of $\tilde{K}(u)$ are cyclic differences $u_i - u_j$ of components of $u$, so if $u_i \in \sqrt{3}\,\mathbb{Q}$ then $u_i - u_j \in \sqrt{3}\,\mathbb{Q}$; the $1/\sqrt{3}$ prefactor of Definition 3.1 clears, leaving rational entries in $K(u)$. Combined with rational $t$, Rodrigues gives rational $R(u,t)$. The open-question sentence now anchors a well-defined candidate set.

**`[S8-M-4]` — Physics-applications overclaim trimmed — CLOSED.**
Renamed "Connections to other disciplines" and reduced to the single structurally well-motivated case: CRNT [Müller-Regensburger], with the explicit skeptical hedge "whether the intrinsic rotation operator developed here has substantive content in that setting — as opposed to the static inner-product structure alone — is an open question." Analog gravity and cognitive hyperdimensional computing dropped, avoiding speculative new citations. This is the trim option recommended in Cycle 1.

**`[S8-X-L-2]` — Musical isomorphism in §8.2 — CLOSED.** "contracted against another vector and raised via the simplicial metric" now states the $H^* \cong H$ identification explicitly; matches the level of care in §§3.4 and 4.

**`[S8-X-L-5]` — Proposition 6.1 pointer — CLOSED.** "(by Proposition 6.1)" parenthetical inserted; makes the "necessarily" traceable.

**`[S8-Y-L-1]` — "companion paper" softened — CLOSED.** "is a natural direction for future investigation" is appropriate.

## New findings introduced by Cycle 2 edits

**`[S8-V-L-1]` (Low) — §8.3 conflates clr with ilr after simplification.**
The simplified sentence "the isometric log-ratio (ilr) transformation maps the probability simplex to $H$ after a component-wise log" calls "ilr" what is strictly the *centered* log-ratio (clr); the ilr postcomposes clr with an orthonormal basis $H \to \mathbb{R}^{N-1}$. Acceptable expository shorthand given the isometry $H \cong \mathbb{R}^{N-1}$; flagged Low for a pre-submission polish.

**`[S8-V-L-2]` (Low) — "Simplicial inner product agrees with Fisher up to a positive scalar" is only true at the uniform distribution.**
Under $x_i = \sqrt{p_i}$, tangent vectors to the sphere image satisfy $\sum x_i v_i = 0$, but *not* $\sum v_i = 0$ in general — the latter holds only at $x \propto \mathbf{1}$. Fisher in $x$-coords is $4\sum v_i^2$ (a constant multiple of Euclidean), while the simplicial form restricted to $T_x(\text{sphere})$ carries the base-point-dependent correction $-\tfrac{1}{3}(\sum v_i)^2$. The two metrics therefore agree up to a scalar only at the barycenter; globally they differ by a position-dependent factor. An inline "at the uniform distribution" qualifier or softer "canonically associated with" would resolve it. Self-correction surfaced on re-read rather than a regression introduced by Cycle 2. Non-blocking.

## Cross-section coherence

- §8.1 and §8.2 now tell a single consistent story: for $N \geq 5$, each *blade* generator is rank 2 and individually Rodrigues-exponentiable; the obstruction to a single-axis closed form is Lie-theoretic. §8.2's "$k = N-3$ vectors, 2-form, contract+musical → vector" construction is internally consistent with §8.1's "operator takes $N-3$ axis inputs" language and with §3.4's Hodge-dual framing.
- §1.2 item 6 and §8.1's uniqueness paragraph now use matching hedges. No inconsistency.
- §3.4 line 271's pre-existing "$d - 1 = N - 3$" conflation (noted out-of-scope in Cycle 1) is untouched and remains out of §8's scope.
- Bibliography unchanged; no new citations introduced, no orphans created.

## Cycle 2 summary

All three Cycle 1 Highs (`[S8-H-1]`, `[S8-H-2]`, plus Reviewer Y's `[S8-Y-H-1]` bridge) CLOSED. All four Cycle 1 Mediums (`[S8-M-1]`–`[S8-M-4]`) CLOSED. The three Lows the Author elected to take are CLOSED. Two new Lows surface on re-read (`[S8-V-L-1]`, `[S8-V-L-2]`), both in the §8.3 information-geometry paragraph and both non-blocking.

**STATUS: GREEN**
