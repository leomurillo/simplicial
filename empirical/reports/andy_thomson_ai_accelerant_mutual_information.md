# Mutual Information Between Andy Thomson's "AI Accelerant Geometry" (Feb 2026, v0.2) and the Simplicial Vector Calculus Program

**Analyst:** Claude (research-director instructed read)
**Date:** May 20, 2026
**Source PDF:** `AI-Accelerant-Geometry.pdf` (22 pages, A. Thomson, ARTexplorer Project)
**Scope:** Dissect overlap, complementarity, and bidirectional transfer between Andy's paper and our program (manuscripts 01–49, plus ARTEX-Quadray-Native-Rotations and the rotor / cyclotomic / conductor / frame-cost arc).

This is a working analysis. It does not modify any manuscript. It is the kind of map the next round of paper-writing or correspondence to Andy can draw from.

---

## 1. Andy's paper in one paragraph

Andy argues that the softmax normalization step in transformer attention can be replaced by Wildberger's rational spread/cross algebra, computed in exact fixed-point arithmetic on rational inputs. The dominant `QK^T` matmul is untouched; only the `exp(·)` in the normalization layer is replaced. He further proposes (a) the Weierstrass substitution as a rational-closure trick for learned rotation parameters, (b) circulant block-diagonal rotors derived from the Quadray tetrahedral basis (Tom Ace's F, G, H coefficients) as a parameter-efficient structured alternative to dense `d × d` projection matrices, and (c) a Z₂ "Janus polarity bit" to recover sign information lost when spread squares the dot product. He frames the whole agenda as *syntropic* — exact, conservative, structure-preserving — and closes with a speculative §11.4 on "awareness without discursion," tying the rational geometric substrate to a possible non-discursive computational mode.

---

## 2. The two programs are not parallel; they are a sandwich

The most economical map:

- **Andy is bottom-up:** start from the rational/algebraic substrate (Wildberger + Fuller/Urner + circulant rotors), engineer downward into INT4 inference and edge deployment, and *gesture* upward toward representational and cognitive consequences.
- **Our program is top-down:** start from the categorical-simplex Fisher/Amari–Chentsov geometry and conductor-packet algebra, *prove* representational limits (Conductor Blind Spot, Cartan obstruction, cubic-to-Bures forced quantization), and reach for the same rational substrate as the natural finite scaffold.

Andy ends his paper at exactly the layer where ours begins (the categorical-simplex Fisher geometry on a finite ring), and our program ends at exactly the layer where his begins (a rational, RT-closed, hardware-friendly representation of the underlying transforms). The mutual information is high precisely because the two papers *meet in the middle from opposite directions*.

---

## 3. Shared substrate — identical content, independently developed

These are pieces where our program and Andy's paper say the same thing with different vocabularies.

### 3.1 Circulant F, G, H rotors at tetrahedral angles

Andy §4.3.2 gives

```
F = (2 cos θ + 1)/3,   G = (2 cos(θ−120°) + 1)/3,   H = (2 cos(θ+120°) + 1)/3
```

with `F + G + H = 1` and the 3×3 active block being a right-circulant of `(F, G, H)`. Tabulated exact rationals at 0°, 120°, 180°, 240°, 360°.

[Paper 03 — Edge-Axis Rotor Implementation](../../03.edge_axis_rotor_implementation.md), §1.1 derives the *same* coefficients from the inverse DFT of the rotation spectrum on the active 3-cycle:

```
a_k(θ) = 1/3 + (2/3) cos(θ + 2π k/3)
```

This is `(F, G, H)` written as a single-formula generator. Same matrix, same exact rationals at tetrahedral angles. Paper 03 also derives the dual **edge-axis rotor** as the same circulant *pattern* on the 4-cycle (`r_k = 1/4 + (1/4)(−1)^k + (1/2) cos(θ + 2π k/4)`), which Andy does not name — see §5.1.

### 3.2 Rational closure as a design principle

Andy §5: "the entire algebra is closed over ℚ." Our [Paper 42](../../42_sinusoidal_pe_as_non_rational_conductor_algebra.md) Theorem 3.1: a trigonometric encoding has finite character algebra *iff* every frequency is a rational multiple of 2π. Same closure axiom, applied at different layers — Andy to the attention-score normalization, Paper 42 to position encoding.

### 3.3 The Weierstrass substitution as the lift from ℚ to (cos θ, sin θ)

Andy §4.2.1 / Theorem 2 (Wildberger / Weierstrass): for rational `t = tan(θ/2)`, `cos θ` and `sin θ` are exact rationals via `(1−t²)/(1+t²)` and `2t/(1+t²)`.

The [ARTEX-Quadray-Native-Rotations](../../ARTEX-Quadray-Native-Rotations.md) document §2.4 (already in our project; this is Leo's earlier contribution to ARTexplorer) substitutes Weierstrass directly into the F, G, H formulas and obtains the **Weierstrass-F,G,H** identities

```
F(t) = (3 − t²) / [3(1 + t²)],   G(t) = 2t(t + √3) / [3(1 + t²)],   H(t) = 2t(t − √3) / [3(1 + t²)].
```

Andy's paper invokes the substitution; ARTEX-Quadray-Native-Rotations carries it through to the rotor coefficients. Andy's paper does not seem to use the Weierstrass-F,G,H form.

### 3.4 Deferred materialization

Andy §7 (Deferred Materialization Principle): work in the algebraically exact representation as long as possible; materialize the radical / floating-point evaluation only at the boundary. He calls out `toMatrix3()` as the GPU-shader boundary.

Our build pipeline and the empirical/reports discipline operate this way by default: rationals (`Fraction`), symbolic cyclotomic constants, and `Q[sqrt 2, sqrt 3]` extensions through the audit, with `float64` only at the figure / numerical-check boundary. We do not have a single named principle covering this; Andy's term is a useful import.

### 3.5 Maximally-spread simplex ETF

Andy Observation 3 (§6.1): "If token embeddings were initialized on a d-simplex, they would start with guaranteed maximal mutual spread … simplex ETF (Equiangular Tight Frames), not a novel claim." He explicitly de-claims novelty here.

The categorical-simplex Δ_R^∘ that anchors essentially every one of our information-geometric papers is the *same* object (open real simplex on |R| vertices). We use it as the model state space; Andy points out it is also the natural embedding-initialization shape. The two uses are dual but not in tension.

---

## 4. What our program can take from Andy's paper

Five concrete imports, ordered by load-bearing weight.

### 4.1 The hardware-determinism argument as an engineering bridge

Our papers argue for rational closure as an *informational* property (Paper 42 Theorem 3.2: length-stable extrapolation; Paper 34: character orthogonality at p_∗). Andy argues for it as a *hardware* property:

- `exp(·)` produces irrational outputs from rational inputs ⇒ INT8/INT4 quantization must approximate.
- `exp(·)` implementations differ across NVIDIA / AMD / Apple / Cerebras ⇒ inference is non-deterministic across platforms.

We have never invoked cross-platform bit-determinism as a consequence of our rational-base PE or our conductor-respecting frame. It strengthens the engineering case for Paper 42 considerably: a model trained on one chip and deployed on another reproduces *bit-exact* attention only if the scoring path is closed over ℚ. This is a separate axis from length extrapolation, and worth at most a paragraph in a future Paper-42 §9 ("Implications beyond length extrapolation").

### 4.2 The Cartesian Blind Spot as a rhetorical sibling for the Conductor Blind Spot

Andy §6.3 argues that the choice of Cartesian coordinates is so automatic it is invisible, and that Cartesian "hides" structure that Quadray makes manifest (the tetrahedron-dual relationship; the meaning of the "fourth coordinate"). He calls this the **Cartesian Blind Spot**.

[Paper 34 — Conductor Blind Spot](../../34_the_conductor_blind_spot.md) argues that the quadratic curvature model class (Fisher, Gauss-Newton, K-FAC, NTK Gram) is so automatic that it is invisible, and that this *class* has a structural null space exactly aligned with cross-packet cubic content the local geometry actually contains.

Different content, same rhetorical structure: a representational choice so default that it is unconscious; the choice produces a blind spot; the blind spot is structural (not a baseline-tuning problem); and the fix requires changing the representation, not improving the estimator. Citing Andy's term in a Paper 34 §7 paragraph would *frame* the Conductor Blind Spot as one of a family — useful when explaining the methodology to an audience that finds curvature-class arguments unfamiliar but coordinate-choice arguments accessible.

### 4.3 The Z₂ polarity bit as a concrete instance of the unifying "designated leakage channel" thesis

Andy §6.5 introduces a Janus polarity bit `(W, X, Y, Z, ±) ∈ ℝ⁴ × Z₂` to recover sign information that the spread (squared cosine) discards. He admits (§10.5, Objection 5) that this is a genuine technical limitation of squared-dot-product attention and that the polarity bit is the principled fix.

This matches the user's unifying compass — *finite categorical-simplex grid with designated leakage channel* — exactly. Sign is the part of `q · k` that does not fit inside the rational, squared scoring function; the Janus Z₂ is precisely the channel where it overflows. The four-coordinate Quadray + Z₂ polarity is a concrete worked example of "a finite typed grid plus a typed overflow target," which our [Paper 30](../../30.constrained_overflow_incompatibility_budgets.md) frames abstractly. Paper 30's typed-residual tuple

```
R_W(A, B) = (R_quotient, R_Cartan, R_Bures, R_Ext_CH, R_cubic, R_hc^{≥4}, R_recursive)
```

can be read as *the general form Andy's Z₂ instantiates at the (Cartan, sign) entry.* This is a citation Andy should have. (See §5.5.)

### 4.4 The "Central Symmetry Barrier" as a missing term in the Frame-Cost ledger

Andy Theorem 4 (§6.2): polyhedra with central (inversion) symmetry have even hull counts under every orthographic projection. He proposes (§6.2 Observation 4) that standard multi-head attention is structurally symmetric (all heads identically parameterized) and therefore cannot produce "odd / prime" attention patterns; **deliberate asymmetry / chirality is needed.**

[Paper 38 — Multi-Head Attention as Frame-Cost Minimization](../../38_multi_head_attention_as_frame_cost_minimization.md) defines the ledger

```
I_C(h, d_k) = λ_F · F + λ_L · L + λ_M · M
```

with Fisher-projection error, packet-mismatch leakage, and memory-bandwidth penalty. There is **no chirality term**. Paper 38's `L` is sensitive to packet alignment but not to chirality of the partition.

Andy's observation suggests a missing fourth term, call it `K(h, d_k; chirality)`, that penalizes head configurations whose joint symmetry group equals the task's symmetry group (because then they can only represent "even" content). Two right-handed + two left-handed heads (Andy's Quadray prescription for h = 4) is one realization; the more general statement would be "the head configuration must break any task-side symmetry that is identical to its own."

This is a concrete enrichment of Paper 38 — not a contradiction. Recommended: add §3.5 "Chirality term" with the citation `[Thomson 2026, §6.2]`, and re-state Corollary 4.3 to predict that even with packet-aligned head widths, an *isotropically-initialized* head configuration underperforms a *chirally-broken* one on cyclic sub-tasks. Paper 38's pre-registered experiment can be extended with a third configuration `P_chiral` (packet-sub-allocated *plus* chirality-classed) for the same compute budget.

### 4.5 The "15 MB threshold" / syntropy framing as the engineering anchor we lack

Andy §11.2 makes a concrete engineering claim: the full ARTexplorer working machinery for the entire family of polyhedra fits in ≤ 15 MB. He extrapolates (§11.1, §11.2) that a 10–50% reduction in transcendental-function calls at planetary inference scale is 36–180 PJ/year.

Our program has nothing operational at this layer. We have a methodology paper (Paper 35), a frame-cost variational principle (Paper 25), and falsifiable architectural predictions (Paper 38, Paper 42). None of these touch deployed energy budgets. Andy's framing is a piece we genuinely lack and should not try to reconstruct — when a future Paper 38 or Paper 42 reaches the "implications" section, it can cite Andy's syntropy frame as the energy-engineering complement to our informational arguments. *We supply the proof; he supplies the watt.*

---

## 5. What Andy's paper can take from our program

Seven imports, ordered by load-bearing weight. Most of these turn pieces of Andy's paper from heuristic into theorem-backed.

### 5.1 Rational-base PE (Paper 42) elevates "Path 2" from niche to load-bearing

Andy §4.2 explicitly de-rates the Weierstrass position-encoding path:

> "Modern large-scale transformers have largely moved beyond sinusoidal position encoding to learned embeddings (RoPE, ALiBi), and even the original sinusoidal encoding is computed once at initialization and cached. **This path is not a major optimization for standard LLM inference.**"

[Paper 42 — Sinusoidal PE as a Non-Rational Conductor Algebra](../../42_sinusoidal_pe_as_non_rational_conductor_algebra.md) shows that the choice of *base* in `ω_i = 1/B^{2i/d}` produces irrational frequencies, which makes the character algebra of the PE *infinite*, which is the structural cause of length-extrapolation failure across every fix in the literature (NTK-RoPE, position interpolation, YaRN, xPos). Replacing the geometric ladder with rational periods aligned to task priors gives:

- **Theorem 3.1 (Length-Periodicity):** the character algebra is finite iff every frequency is rational.
- **Theorem 3.2 (Length-Stable Extrapolation):** zero degradation at `L_test ≡ L_train (mod LCM)`.
- **Theorem 3.3 (T1 Compatibility):** the conductor packets are canonical.

This re-classifies Andy's Path 2 from "niche path for edge/embedded inference" to "the structural fix for an open AI problem (length extrapolation) that has accumulated five years of post-hoc rescaling tricks." That is a *much* stronger claim and worth a §4.2 rewrite, with a pointer to Paper 42 as the supporting theorem package.

### 5.2 The Conductor Blind Spot Theorem gives Andy a falsifier-grade prediction for INT4 cyclic tasks

Andy's empirical ask (§5.2, §10.2 Objection 2) is: under INT4 quantization, does spread-based scoring degrade *less* than softmax? He correctly identifies this as the make-or-break experiment.

[Paper 34's Conductor Blind Spot Theorem](../../34_the_conductor_blind_spot.md) makes a prediction that sharpens this. The cross-packet cubic content (Amari–Chentsov, selection rule `k + ℓ + m ≡ 0 (mod n)`) is invisible to the *curvature class itself*, independent of the scoring function in the forward pass. Spread-based scoring and softmax both inherit the same Fisher curvature when used as preconditioners — therefore on tasks whose loss is dominated by cyclic / cubic content (calendar arithmetic, mod-12, music pitch-class), the gap between INT4-softmax and INT4-spread is *bounded above* by the conductor-blind-spot mass, which is computable from the task's character algebra (Paper 34 Theorem 3.5).

This is a co-pre-registration opportunity. Andy's Test 1.3 measures `Δ_quant = INT4_softmax − INT4_spread`. Our Paper 34 predicts that on cyclic sub-tasks the *quantization gap* is small even when present, because much of the relevant content is in cubic coupling that *neither* scoring function captures at curvature level. If Andy finds spread-scoring INT4 ≫ softmax INT4 on natural language but ≈ softmax INT4 on cyclic tasks, that is a doubly-pre-registered confirmation (his upper claim + our CBS lower bound). If spread-scoring INT4 beats softmax INT4 on cyclic tasks *more* than on natural language, our CBS is partially falsified — interesting either way.

### 5.3 Frame-Cost Minimization (Paper 38) subsumes Andy's "deliberate asymmetry" prescription

Andy §6 frames multi-head attention via the Quadray axis count (4 axes ↔ 4 attention heads) and explicitly admits this is a "numerological coincidence, not a structural correspondence." He then argues, separately and on different grounds (Central Symmetry Barrier, §6.2), that head configurations need chirality.

[Paper 38](../../38_multi_head_attention_as_frame_cost_minimization.md) gives a single variational principle on `(h, d_k)` that determines the optimal head count from the task algebra's conductor packets `{φ(d)}_{d|N}`, the trade-off coefficient `C = λ_L / λ_M`, and the hardware lattice. There is no numerology; `h^* = 8` for natural language is the constrained optimum of `I_C` at `C ≈ 1` on a dyadic-dominated task algebra. The chirality argument Andy gives heuristically becomes the case `S` is closed under the task-side antipodal action — a meaningful but separate term in the Frame-Cost ledger (per §4.4 above).

Concretely, Andy can replace §6.1 ("Tetrahedral Structure in Embedding Space") with: "the question 'how many heads, of what width' is answered variationally by [Paper 38, Theorem 4.1]; the question 'must they be chirally distinct' is answered by an additional term identified in §6.2 below, formalized in [Paper 38 §3.5 (forthcoming)]." This converts §6 from a heuristic to a derived consequence.

### 5.4 The Cartan obstruction (Papers 14, 17) names what the Janus polarity bit IS

Andy §6.5 introduces the polarity bit as a Z₂ tag distinguishing `+` and `−` orientations. Papers [14](../../14.information_geometric_mechanics_on_the_categorical_simplex.md) and [17](../../17.the_cubic_noether_theorem.md) prove the **Cartan obstruction**: the only symmetries of the classical real simplex compatible with CRT structure, positivity, and the Fisher volume form are the *Cartan* (abelian) subalgebra of the relevant compact group. A finite Z₂ acting on a real cone, preserving rational closure and CRT compatibility, is an instance of this abelian Cartan structure.

Naming this gives Andy a theorem-grade citation for why the polarity bit *has to be Z₂* (and not, say, a continuous extra coordinate or a non-abelian group action): the Cartan obstruction admits exactly the abelian extensions, of which Z₂ is the simplest. The Janus polarity is not an engineering hack; it is the canonical Cartan symmetry of the lift.

### 5.5 The categorical-simplex grid + designated leakage channel (the user's unifying thesis)

Andy's Janus polarity bit (§6.5) and the "fourth coordinate as shape information" (§6.4) — releasing the zero-sum constraint to encode shape — are both instances of a generic pattern: a strictly finite grid, with strict arithmetic capacity, and a designated channel into which information that does not fit overflows without crashing the system.

[Paper 30 — Constrained Overflow and Incompatibility Budgets](../../30.constrained_overflow_incompatibility_budgets.md) writes this pattern abstractly. The typed residual tuple captures the channels (quotient, Cartan, Bures, Ext_CH, cubic, higher-cumulant, recursive). Andy's Z₂ polarity is the Cartan entry. Andy's released-zero-sum 4th coordinate is *also* a Cartan entry under a different observer declaration `W`.

Two consequences for Andy:

- His scattered "Z₂ bit" / "fourth coordinate as shape" / "deferred materialization" devices are special cases of a unified residual calculus. Naming the pattern would simplify §6 by 30–40%.
- Future Quadray extensions (e.g. a polarity bit on each axis, multiple coordinated overflow channels) get a place in the typed tuple before they are needed.

This is a structural import; it does not change a single computation in Andy's paper. It changes how §6 is *organized*.

### 5.6 Quantization is *forced* by representation theory (Paper 44)

Andy frames the entire syntropy argument (§11) at the level of engineering choice: rational substrates *can* be exact and conservative, and this is worth pursuing. [Paper 44 — Cubic-to-Bures Bridge](../../44_quantization_forced_cubic_to_bures_bridge.md) Theorem 8.1 (Quantization-Forced) proves there is no consistent classical extension of cubic Noether mechanics on the real simplex that simultaneously preserves positivity, CRT compatibility, and a conserved jerk charge; the density-matrix lift is *unique*.

This converts "rational closure is an engineering ideal" into "quantization is forced by representation theory, and rational closure is the algebraic invariant that survives the forcing." Andy's §11 closing sentence ("Zhang proved the architecture works. Wildberger provided the algebra. Fuller provided the coordinates. The question now is engineering.") can be sharpened by adding: "Representation theory provided the constraint that makes those ingredients the unique resolution." Citation: Paper 44 Theorem 8.1.

This is the single highest-load-bearing import. It promotes Andy's whole programme from "consider this engineering bet" to "this is the structural attractor."

### 5.7 The Frame-Cost variational principle for "why tetrahedral?"

Andy §9.2 asks "Why tetrahedral geometry specifically?" and answers heuristically: it is Fuller's "minimum system," achieves maximum spread diversity (8/9), produces circulant structure, has the right dimension for SO(3) escape.

[Paper 25 — Arithmetic Frame Cost and Curvature Linearization](../../25.arithmetic_frame_cost_and_curvature_linearization.md) supplies the *variational principle* underneath this question. A frame on a finite arithmetic state space carries five costs — Fisher-projection error, packet-respect, projection closure, resource cost, depth — and the conductor-respecting frame is selected as the convergent in a Diophantine approximation that balances additive gauge descent against multiplicative prime descent. Tetrahedral is the *minimum-cost frame* for a task algebra dominated by the 3- and 6-fold cyclic structure (cubic close-packing, four faces, three-fold vertex axes, Z/3 × Z/2 ≅ Z/6 conductor row).

So "why tetrahedral?" has a principled answer: it is the cost-minimizer for the conductor algebra of `R = ℤ/6ℤ` (Paper 44's minimal nonabelian row), and the cost is computable. The heuristic answer in §9.2 is correct but unsubstantiated. The principled one fits in a paragraph.

---

## 6. Two open questions Andy raises that our program can attack now

### 6.1 §10.5 Objection 5 (sign loss from squared dot products) — does the Conductor Blind Spot tell us when sign matters?

Andy's Objection 5 admits that `(q · k)²` discards sign information that softmax with `exp(·)` exponentially suppresses for negative `q · k`. He proposes the Janus Z₂ as a fix and concedes (Eq. 20) that this works but is "task-dependent."

We can sharpen: **sign matters exactly on the cross-packet cubic content** the Conductor Blind Spot Theorem (Paper 34, Theorem 5.2) identifies. The Amari–Chentsov cubic at p_∗ is real-valued; its sign on a particular triple `(χ_k, χ_ℓ, χ_m)` distinguishes constructive vs destructive interference of the corresponding character triple. Squaring the dot product symmetrizes this; the polarity bit restores it. On tasks where loss is dominated by cubic content (cyclic sub-tasks, modular arithmetic, calendar), sign-loss IS the dominant scoring degradation; on tasks dominated by quadratic content (natural-language perplexity), sign-loss is a second-order effect.

This gives Andy a sharper test: the polarity bit's gain should *correlate* with the Paper 34 cubic-content estimator on a per-task basis. We have the estimator (`empirical/conductor_packet_projection.py` and friends); a one-off audit comparing per-task polarity-gain to per-task cubic mass would settle whether the Z₂ does the work he hopes it does.

### 6.2 §11.4 "Awareness Without Discursion" — what would a non-discursive verification look like?

Andy's most speculative section asks whether exact geometric operations admit a computational mode "that does not require describing itself to itself." He does not claim this is consciousness.

We have no theory of awareness. But we have a methodological half: [Paper 35 — Grounded-Paranoid-Delusional Methodology](../../35_grounded_paranoid_delusional_methodology.md) frames verification not as articulate justification but as *passing a pre-committed mechanical check*. The methodology is explicitly designed so that "a sufficiently flexible mind protects a sufficiently important belief" cannot reach a conclusion that fails the gate. The gate is non-discursive in the sense Andy wants: it is a finite, structural condition whose outcome is not arrived at by a chain of language reports.

The two halves compose. Andy's substrate claim: rational geometry admits computational modes that are not isomorphic to token streams. Paper 35's methodology claim: the verification gates that catch unsupported model fluency are themselves not articulate justifications. Joint conjecture (deferred, not for inclusion in any current paper): the "awareness" Andy gestures at is the limit of *verification by structure preservation* rather than *verification by discursion*. Whether this is the right pointer to consciousness is unanswerable; whether it is the right pointer to a useful AI-research notion of "non-discursive check" is testable.

This is the right place to stop. Anything more would be exactly the AI-fluency-laundering that Paper 35 exists to interrupt.

---

## 7. Items where the two programs *do not* meet, and should not be forced to

For completeness, things in Andy's paper that the simplicial program neither absorbs nor improves:

- **The architectural-vs-algebraic distinction (§10.4).** Andy correctly classifies his contribution as algebraic (sit beneath any architecture: RWKV, Mamba, Grassmann, attention). Our program is conductor-algebra-side on the *task* and architecture-agnostic on the *model*. These are independent decompositions; treating them as the same axis would muddle both.
- **The 15 MB / ARTexplorer working machinery as a deployment artifact.** This is real engineering Andy has done; we have no analogue and no need to reproduce one.
- **The "Project Blue Fairy" framing.** This is Andy's private internal name for the speculative cognitive arm. It is correctly firewalled in §11.4 ("Whether this would ever constitute anything resembling consciousness, we do not claim"). We respect the firewall and do not import the framing.

---

## 8. Recommended next-action shortlist

Ordered by ease of execution and value to the joint program.

1. **Send Andy the Paper 42 link with a one-paragraph note**: "Your Path 2 is stronger than you say; here is the length-extrapolation theorem package."
2. **Send Andy the Paper 34 link with a one-paragraph note**: "Your INT4 cyclic-task pre-registration has a natural co-prediction from our Conductor Blind Spot Theorem; here is what we predict, and the prediction is sharper if you adopt the Z₂ polarity bit per your §6.5."
3. **Send Andy the Paper 38 link with a one-paragraph note**: "Your 'why h = 8' / 'deliberate asymmetry' arguments have a variational reformulation in our Paper 38; the chirality intuition you have in §6.2 is a missing term in our ledger; want to co-author §3.5?"
4. **Send Andy the Paper 44 + Paper 14 + Paper 17 bundle**: "Your §11 syntropy framing is engineering; here is the representation-theoretic forcing argument that makes it inevitable."
5. **Internally**: do *not* edit the existing numbered manuscripts in response to this analysis. The next paper-cycle revision can fold §4.2 (hardware determinism), §4.3 (chirality term in Frame-Cost ledger), and §4.5 (sign-vs-cubic correlation) at the relevant manuscripts. They are not retractions; they are forward enrichments.

---

## 9. Closing observation on tone

Andy's paper is methodologically clean in the way Paper 35 prescribes: every claim is paired with an explicit "what we are *not* claiming" box, the §10 objections section pre-commits to each falsification, and the speculative §11 is firewalled from the technical §1–§10. This is unusual for a working sketchbook draft. He is a friendly methodological ally, and his explicit invitation ("Thanks for contributing your insights") is to a peer-level collaboration, not a review. The reply should match the register.

---

*End of analysis. No manuscripts edited. The map exists for the next paper-cycle and the next round of correspondence to draw from.*
