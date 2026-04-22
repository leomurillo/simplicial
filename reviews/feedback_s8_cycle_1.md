# §8 Cycle 1 — Synthesis + Proposition 6.1 empirical validation

**Scope.** Cycle 1 on §8 ("Higher Dimensions and Future Work") of `simplicial_vector_calculus.md`, plus an independent empirical validation of Proposition 6.1 (nine structural properties of $R$) dispatched in parallel. The user authorized: "advance to section 8 … in parallel, let's launch empirical agents to validate Proposition 6.1's nine structural properties of $R$."

**Workflow change landed in this cycle.** The empirical-validation skill now requires the Empirical Skeptical to **execute the script before submitting to the Empirical Reviewer**, and the Reviewer now audits the code *and* the captured stdout together. Updated files:

- `.cursor/skills/empirical-validation/SKILL.md` (cycle protocol and termination rules rewritten).
- `.cursor/agents/empirical-skeptical.md` (new "Execute Before Submitting" core directive).
- `.cursor/agents/empirical-reviewer.md` (new Output Plausibility directive; Critical severity now also covers procedural failures like "no output captured"; GREEN is conditioned on both code and output passing).

The Proposition 6.1 validation was the first use of the new workflow and it worked cleanly: the Skeptical submitted one package (code + captured summary table), the Reviewer issued GREEN on the first QA pass, no revision loop needed.

## 1. §8 text review — status

### Reviewer X (formalism)

**File:** `reviews/feedback_s8_cycle_1_reviewer_x.md`.

**STATUS: AMBER.** Two High findings that must be resolved before §8 is submission-ready:

- **`[S8-H-1]` (§8.1, line 459).** "For $N \geq 5$ … produces skew operators of rank greater than 2, whose minimal polynomials are higher-degree and do not admit the same clean trigonometric refolding" is **factually wrong**. The wedge-Hodge construction spelled out in §8.2 produces a *simple* 2-form (by construction, a wedge of vectors is simple), whose Hodge dual is *also* simple, hence a rank-2 operator. The obstruction to higher-$N$ Rodrigues is not the rank of any single generator — it is the Lie-theoretic fact $\dim \mathfrak{so}(N-1) = \binom{N-1}{2} > N-1$ for $N \geq 5$, so generic rotations are sums of rank-2 "blade" generators with non-commuting supports whose exponentials do not refold. The next paragraph (line 461) already makes this correct Lie-theoretic point; the two paragraphs in the current text therefore give inconsistent reasons for the same conclusion.

- **`[S8-H-2]` (§8.1, line 459).** "Rotations in $\mathrm{SO}(N-1)$ for $N-1 \geq 4$ … have fixed subspaces of dimension $N-3$" is **false for generic rotations**. A rotation in $\mathrm{SO}(m)$ with $k$ nontrivial 2-plane blocks fixes a subspace of dimension $m - 2k$; generic rotations have $k = \lfloor m/2 \rfloor$, so the generic fixed subspace has dimension 0 (if $m$ even) or 1 (if $m$ odd). The value $N-3$ holds only for *simple* rotations (single rank-2 block). The prose conflates "simple" with "generic"; fix by restricting the claim to simple rotations.

**Plus four Mediums** — (M1) §8.1 drops the "within our framework" hedge that §1.2 item 6 carefully supplied for Eckmann's classification; (M2) §8.3 mis-attributes the classical Weierstrass substitution to Wildberger; (M3) "tetrahedral symmetry family" is undefined (candidate: $\sqrt 3 u \in \mathbb{Q}^4$); (M4) §8.3's generalized-physics paragraph overclaims "all exhibit the gauge-direction plus zero-sum-hyperplane structure" (cognitive hyperdimensional computing is uncited and structurally tenuous; analog gravity is a stretch).

**Plus six Lows** — minimal-polynomial qualifier, musical-isomorphism step in §8.2, ilr/clr factorization wording, Fisher-metric up-to-scalar hedge, Prop-6.1 traceability on composition assertion, typography / references (the latter all clean).

### Reviewer Y (narrative)

**File:** `reviews/feedback_s8_cycle_1_reviewer_y.md`.

**STATUS: AMBER.** One High finding:

- **`[S8-Y-H-1]` (lines 453–455).** §7 ends on a highly applied computational note (9-mul kernel, quaternion pipelines); §8 immediately snaps back to the algebraic theory of §5. The reader experiences a structural whiplash. Recommendation: insert a bridging sentence that zooms out from the computational kernel back to the $N=4$ structural setting before diving into the minimal polynomial argument.

**Plus three Mediums** — (Y-M1) "tetrahedral symmetry family" undefined (concurrent with Reviewer X's M3); (Y-M2) ilr description density in §8.3 presupposes Aitchison familiarity; (Y-M3) §8.3's physics-application triple feels scatter-shot and buzzword-y.

**Plus two Lows** — cumulative weight of forward-commitment promises ("deferred to future work" × 3); slight disjointedness between the two $N=4$ uniqueness strands in §8.1.

**Tonal consistency with §9 is good** — the "autonomous *presentation*" framing landed in external cycle 1 has held.

### Convergent findings across X and Y

Four of the nine findings above are concurrent hits on the same sentence or region:

- **M3 (X) + Y-M1 (Y):** "tetrahedral symmetry family" undefined in §8.3.
- **M4 (X) + Y-M3 (Y):** §8.3 physics-applications paragraph overclaims / scatter-shot.
- **L3 (X) + Y-M2 (Y):** ilr / clr factorization in §8.3 is dense or ambiguous.
- **Y-M1 and X-M3** are the same finding but at different severities (X Medium, Y Medium — convergent).

This convergence suggests §8.3 is where the next Cycle 2 effort should concentrate; §8.1's Highs are concentrated on the $N \geq 5$ minimal-polynomial / fixed-subspace paragraph.

## 2. Proposition 6.1 empirical validation — status

**Track summary.** Single QA loop. Skeptical drafted the script, executed it, captured the summary table, and submitted code + output as one package; Reviewer issued GREEN on first review.

**Artifacts.**

- Script: `empirical/verify_proposition_6_1_rotation_properties.py` (312 lines; reuses `build_K_u`, `generate_random_zero_sum_vector` byte-identical to the certified Theorem 7.1 script; adds a modified `generate_random_rotation_via_Ku` returning $(R, u, \theta)$ so $\theta$ is exposed for trace + spectrum tests).
- QA report: `empirical/reports/qa_proposition_6_1_reviewer.md` (`STATUS: GREEN`, 4 Lows, 0 M/H/C).
- Didactic report: `empirical/reports/proposition_6_1_rotation_properties.md`.

**Captured execution output:**

```text
Running preflight checks...
Preflight checks passed.

Testing Proposition 6.1 Properties (10,000 trials each)...

=============================================================================
PROPERTY                  | STATUS | MAX ERROR
=============================================================================
P1 (Orthogonality)        | PASS   | 4.99600e-15
P2 (Row sums = 1)         | PASS   | 1.11022e-15
P3 (Col sums = 1)         | PASS   | 1.50990e-14
P4 (Determinant = +1)     | PASS   | 6.21725e-15
P5 (Trace)                | PASS   | 2.99760e-15
P6 (Hyperplane pres.)     | PASS   | 6.66134e-15
P7 (Gauge-equivariance)   | PASS   | 2.66454e-15
P8 (Metric preservation)  | PASS   | 2.48690e-14
P9 (Spectrum)             | PASS   | 3.55271e-15
P5' (Appendix D det.)     | PASS   | 4.44089e-16
=============================================================================
```

**Interpretation.** All ten tests PASS at or below machine epsilon; every Proposition 6.1 property is empirically validated across 90,000 randomized trials plus the Appendix D deterministic anchor. The max errors sit within a factor of ~15 of the float64 per-operation floor (~1e-15), consistent with predicted accumulation for each operation class (4×4 matmul ~ 5× epsilon; two successive matmuls for the $R^\top G R$ form ~ 15× epsilon). No `nan` / `inf` / warnings; no counter-example; no `STATUS: RED` trigger.

**Four Low findings from the Reviewer**, all non-blocking and logged in `reviews/open-issues.md` under `[E-Proposition-6-1-Polish]`:

1. P5 docstring omits the equivalent restricted-trace form $\operatorname{tr}(R|_H) = 1 + 2\cos\theta$ (implied by P2 + subtraction).
2. P9 eigenvalue pairing sort key has theoretical edge-case fragility at $\theta \in \{0, \pi, 2\pi\}$; Hungarian matching would be defensively more robust. Not triggered at seed 42.
3. P3's ~15× tail extremum above structurally symmetric P2 is a sampling artefact, not a generator bug.
4. P5' deterministic block doesn't mirror P9's eigenspace/rank checks; stochastic P9 covers it.

## 3. Consolidated state

| Track | Status | Blockers |
|---|---|---:|
| Reviewer X (§8 formalism) | AMBER | 2 High, 4 Medium, 6 Low |
| Reviewer Y (§8 narrative) | AMBER | 1 High, 3 Medium, 2 Low |
| Empirical (Proposition 6.1) | GREEN | 0 C/H/M; 10/10 tests PASS |

**Stabilized scope to date.** §§1–7 + Appendix D cleared at zero C/H/M findings. Theorem 7.1 and Proposition 6.1 both empirically validated end-to-end. §8 is at first-cycle AMBER; §9 has been implicitly audited at external cycle 1 / §7 cycle 2 (for the B6 reframing) and is not presently open.

## 4. Decision surface

§8 has three Highs spread across X and Y, so a Cycle 2 is indicated. Concretely, the fixes are:

- **X-H1 + X-H2:** rewrite §8.1's middle paragraph to invoke the Lie-theoretic obstruction (already correctly given in the next paragraph) rather than the incorrect rank-of-generator story; restrict the fixed-subspace claim to simple rotations.
- **Y-H1:** insert a bridging sentence at the top of §8.
- **M1 (X-M1):** mirror §1.2 item 6's "within our framework" hedge on §8.1's uniqueness claim.
- **M2 (X-M2):** detach Weierstrass from Wildberger.
- **M3 + Y-M1 (concurrent):** concretize or drop "tetrahedral symmetry family"; a simple concrete candidate is $\sqrt 3 u \in \mathbb{Q}^4$.
- **M4 + Y-M3 (concurrent):** trim or re-cite §8.3's generalized-physics paragraph. Reviewer X's cleanest suggestion is to keep only the CRNT / stoichiometric example (already well-cited via `[Müller-Regensburger]`) and drop the others, or to re-cite them properly (Kanerva for HDC, a specific analog-gravity reference if retained).
- **Y-M2 + X-L3 (concurrent):** simplify the ilr description to "Aitchison's ilr transformation relies on the same zero-sum hyperplane geometry" without the full factorization.

All seven items above are surgical; the Lows are pure polish. This is a typical single-Author-pass Cycle 2.

Three paths:

- **Option A (recommended).** Launch §8 Cycle 2 now. Clear the three Highs and the four Mediums in a single Author pass; defer the eight Lows to the pre-submission polish. Target a clean double-GREEN Cycle 2 verification pass. This mirrors the §7 Cycle 2 pattern that worked cleanly.
- **Option B.** Close §8 Cycle 1 at AMBER, list the three Highs + four Mediums in `reviews/open-issues.md`, and advance to §9 Cycle 1 in parallel. Not recommended — the §8 Highs include a factually-incorrect claim (X-H1) that should not sit in the paper.
- **Option C.** Skip §9 entirely (it was already audited during external cycle 1 for the B6 reframing and landed in §7 cycle 2 downstream-sweep) and advance directly to a pre-submission polish pass across §§1–9 + appendices.

**Recommendation.** Option A: launch §8 Cycle 2 with the Author clearing Highs + Mediums. Orchestrator will follow up with a double-Reviewer verification pass.

Let me know which you want.
