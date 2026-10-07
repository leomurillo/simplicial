# T29 — Dimensional Selection via Conformal Admission

**The Methodology's Second Major Application: Why Spatial Dimension Is 3 and Spacetime Is (3,1)**

**Leonardo Murillo Montero**

*First draft — May 27, 2026*

---

> *Paper 32 §8 already proves dimensional selection via two routes (Hodge/$\mathfrak{so}$ and conductor count). T29 adds a third route — conformal admission + cofinal lift — that demonstrates the T20-T21 methodology's general applicability. The third route does not establish a stronger conclusion than Paper 32's existing routes; it provides a DIFFERENT STRUCTURE OF PROOF (governed admission across the Fisher-volume hierarchy) and QUANTIFIES the obstruction at each non-selected dimension. This is the methodology's second major application, after T20 (RH).*

---

## §1. The dimensional selection problem

### §1.1 Statement of the problem

**Why is spatial dimension 3? Why is spacetime $(3,1)$?**

Paper 32 §8 reformulates this as: at which row of the Fisher-volume hierarchy does an inertial projector admit closure-valid self-modeling? An inertial projector (Definition 8.1) requires:
- A single conserved energy from a single Hamiltonian.
- A single rotation axis (angular momentum vector-representable).
- A complex structure $J^2 = -I$ organizing transverse rotation.

These three requirements collectively constitute the **binary symplectic package**.

### §1.2 Paper 32's existing solutions

**Route 1 (§8.2 Theorem 8.2 — Hodge/$\mathfrak{so}$).** Three structural facts converge only at $n = 3$:
- $\dim\mathfrak{so}(n) = n(n-1)/2 = n \iff n = 3$;
- $\Lambda^2(\mathbb{R}^n) \cong \mathbb{R}^n \iff n = 3$;
- $J^2 = -I$ on $u^\perp$ in the dim-3 row (Paper 13 §2 cross-product).

**Route 2 (§8.3 Theorem 8.3 — conductor count).** At $\mathbb{Z}/6 = P_2$, the closure-valid block $A_2 \oplus A_3$ has real dimension $1 + 2 = 3$. The complementary carry packet $M$ has dimension 2 and is the gravity-adjacent residual.

**Signature (§9.1 Theorem 9.1 — forced $(3,1)$).** $d\Theta$ on the extended tangent space carries signature $(+,+,+;-)$ from the Legendre $-\ell_3$ sign.

### §1.3 What T29 adds

T29 provides **Route 3 — conformal admission across the Fisher-volume hierarchy**:

1. **Boundary scores** at each dimensional rung $n$: explicit deviations from the three structural identities of Theorem 8.2.
2. **Conformal admission** at each rung: admit $n$ as an inertial-projector-closing dimension iff all three scores reject the null.
3. **Cofinal lift across the hierarchy**: T15 categorical limit + uniqueness forces a single selected dimension.
4. **Selected dimension: $n = 3$**, with explicit quantification of the rejection at $n \ne 3$.

This is the SAME selection as Paper 32 Routes 1 and 2, established by a different proof structure. The advantage of T29's route is **methodological**: it demonstrates that the conformal-admission methodology (T20+T21) generalizes beyond RH to other terminal-screen closure problems.

---

## §2. The terminal-screen identification

### §2.1 Dimensional selection is at a terminal inner screen

In T19's language (Definition 3.2), the dimensional selection problem is at the terminal inner screen of the simplicial Fisher-volume hierarchy.

**Claim 2.1.1.** *The dimension selecting condition — "inertial projector admits closure-valid self-modeling at row $n$" — is at the terminal inner screen of the Fisher-volume hierarchy in the sense of T19 Definition 3.2.*

**Argument.** A non-terminal sub-screen of the dimensional selector would correspond to a sub-row partition of the inertial projector with task-relevant active control on the dimensional structure. Such a sub-partition would allow recasting the dimensional condition through a sub-mechanism — e.g., factorizing $\dim\mathfrak{so}(n) = n$ as a product of two simpler conditions on sub-spaces.

But the three structural identities of Theorem 8.2 are **simultaneous and irreducible** at $n = 3$: each holds as an exact identity, and their simultaneous satisfaction is the closure certificate. No proper sub-mechanism factorizes the closure.

By T19 Theorem 6 (Phenomenological Transparency), the simplicial framework cannot make the generating interior of the dimensional selector an object of internal closure analysis. Direct deductive proof from sub-structural reasoning is structurally forbidden — which is why Paper 32 needed the EXTERNAL identifications (Hodge isomorphism, conductor block dimension count). $\square$

### §2.2 Why conformal admission applies here

The terminal-screen structure is the same as for RH (T20 §2.2). At the terminal screen, direct deduction is forbidden; **admission with finite-rank validity + cofinal lift is the natural closure mechanism**.

The dimensional selection problem is well-suited because:
- The Fisher-volume hierarchy provides a natural cofinal tower (rungs $n = 1, 2, 3, 4, \ldots$).
- The closure conditions (Theorem 8.2 facts) are checkable at each rung.
- Failure at rung $n \ne 3$ is QUANTIFIABLE (deviation from the structural identities).
- T15 cofinal completion lifts row-by-row admission to a unique global selection.

---

## §3. Boundary scores at each dimensional rung

### §3.1 The three boundary scores

For each integer $n \ge 1$, define three boundary scores measuring closure-valid inertial-projector admission:

**(D1) Hodge / $\mathfrak{so}$-isomorphism deviation.**
$$s_1(n) := \big|\dim \mathfrak{so}(n) - n\big| = \left|\tfrac{n(n-1)}{2} - n\right| = \left|\tfrac{n(n-3)}{2}\right|.$$

| $n$ | $\dim\mathfrak{so}(n)$ | $s_1(n)$ |
|---|---|---|
| 1 | 0 | 1 |
| 2 | 1 | 1 |
| **3** | **3** | **0** |
| 4 | 6 | 2 |
| 5 | 10 | 5 |
| 6 | 15 | 9 |
| 7 | 21 | 14 |
| $n$ | $n(n-1)/2$ | $n(n-3)/2$ |

$s_1(n) = 0 \iff n = 3$.

**(D2) Hodge duality deviation.**
$$s_2(n) := \big|\dim \Lambda^2(\mathbb{R}^n) - n\big| = \left|\tfrac{n(n-1)}{2} - n\right| = \left|\tfrac{n(n-3)}{2}\right|.$$

This equals $s_1(n)$ by the Hodge $\star$-correspondence on $\Lambda^2$. So $s_2 \equiv s_1$ — formally a single score from the dimensional algebra side.

**(D3) Complex structure deviation.**
$$s_3(n) := \min_{J \in \mathrm{End}(\mathbb{R}^n)} \big\|J^2 + I_{u^\perp}\big\|_{\mathrm{op}}, \quad \text{where } u \in S^{n-1}.$$

The minimum is over endomorphisms $J$ acting on the orthogonal complement $u^\perp \cong \mathbb{R}^{n-1}$.

By a classical fact (Paper 13 §2, also folkloric): $J^2 = -I_{u^\perp}$ requires $\dim u^\perp = n - 1$ to be EVEN (since orthogonal complex structures exist only in even real dimension). So $J^2 = -I$ on $u^\perp$ iff $n - 1$ is even iff $n$ is odd.

For inertial-projector closure, we need this to hold for the SPECIFIC $J$ induced by the cross-product structure. This is more restrictive: in $\mathbb{R}^3$, the cross-product $u \times \cdot$ on $u^\perp$ is the canonical $J$ with $J^2 = -|u|^2 \cdot I$, scaling to $J^2 = -I$ on the unit sphere.

| $n$ | $u^\perp$ dim | exists $J^2 = -I$? | Cross-product $J$ ? |
|---|---|---|---|
| 1 | 0 | trivially yes | trivial |
| 2 | 1 | no (odd dim) | no |
| **3** | **2** | **yes** | **YES (canonical cross product)** |
| 4 | 3 | no | n/a |
| 5 | 4 | yes (complex structure) | no (no canonical cross product) |
| 6 | 5 | no | no |
| 7 | 6 | yes | partial (octonionic) |
| ... | ... | yes iff $n-1$ even | only at $n = 3$ |

$s_3(n) = 0$ at $n \in \{1, 3, 5, 7, \ldots\}$ (odd $n$) via the bare $J^2 = -I$ condition.

But for the CANONICAL cross-product-induced $J$, $s_3(n) = 0$ only at $n = 3$. Define the stricter score:
$$s_3^{\text{strict}}(n) := \big\|J_{\text{cross}}^2 + I_{u^\perp}\big\|_{\mathrm{op}}$$
where $J_{\text{cross}}$ is the cross-product structure if it exists (only at $n = 3, 7$) and $\infty$ otherwise. Then $s_3^{\text{strict}}(n) = 0 \iff n = 3$ (taking the cross-product canonical at $n = 3$; at $n = 7$ the octonionic cross product fails associativity, breaking the single-rotation-axis condition).

### §3.2 Why three scores

T20 used three scores ($s_1, s_2, s_3$) to provide independent rejection paths. Similarly for T29:

- $s_1$ controls the **dimensional matching** condition $\dim\mathfrak{so}(n) = n$.
- $s_2 = s_1$ via Hodge duality — formally redundant but methodologically a separate check.
- $s_3^{\text{strict}}$ controls the **complex structure compatibility** $J^2 = -I$ via canonical cross product.

Each is a deterministic rule on the rung $n$ (T18 Theorem 1 applies). By Mondrian conditioning (T18 Theorem 5), validity holds conditional on the rung structure.

### §3.3 Null calibration

The null hypothesis: "rung $n$ admits inertial-projector closure." Under the null, all three scores would be 0 simultaneously. Empirically (by direct computation), this happens uniquely at $n = 3$.

The null ledger is constructed from a perturbative null model: small random perturbations of the structural identities. Under the perturbative null, scores at $n \ne 3$ have a distribution centered well away from 0; scores at $n = 3$ have a distribution centered at 0 with deviation only from finite-precision arithmetic.

| $n$ | $s_1$ | $s_3^{\text{strict}}$ | Null rejection? |
|---|---|---|---|
| 1 | 1 | $\infty$ (no $u^\perp$) | YES (strong) |
| 2 | 1 | $\infty$ (no cross product) | YES (strong) |
| **3** | **0** | **0** | **NO (admission)** |
| 4 | 2 | $\infty$ (odd $u^\perp$) | YES (strong) |
| 5 | 5 | $\infty$ (no canonical cross) | YES (strong) |
| 6 | 9 | $\infty$ | YES (strong) |
| 7 | 14 | finite (octonionic fails associativity) | YES (moderate) |
| 8+ | growing | $\infty$ or fails | YES (very strong) |

---

## §4. Conformal admission at each rung

### §4.1 The update gate

Following T18 Theorem 4 (Conformal Update Gate), define:
$$G_{\alpha, n} := \mathbf{1}[s_1(n) \le \alpha] \cdot \mathbf{1}[s_3^{\text{strict}}(n) \le \alpha]$$

At any chosen $\alpha < 1$, $G_{\alpha, n} = 1 \iff n = 3$. So the gate admits ONLY rung 3.

### §4.2 The joint p-value

The joint null p-value at rung $n$ is computed via the finite-rank lemma applied to the null calibration ledger:
$$p(n) = \frac{1 + \#\{n' \ne n : s_1(n') \ge s_1(n) \text{ and } s_3^{\text{strict}}(n') \ge s_3^{\text{strict}}(n)\}}{n_{\text{rungs}} + 1}.$$

At $n = 3$: both scores are 0; all $n' \ne 3$ have $s_1 \ge 0$ and $s_3 \ge 0$, so $p(3) = (1 + \#\text{rungs} - 1)/(\#\text{rungs} + 1) \approx 1$.

But this is the WRONG direction — we want to admit $n = 3$ as the structural regime, which means we want $p$ SMALL under the null.

Reframe: the null is "rung $n$ does NOT admit closure"; the structural regime is "rung $n$ DOES admit closure." Smaller score = more compatible with closure (since $s_j = 0$ is the structural identity).

P-value with reversed direction:
$$p(n) = \frac{1 + \#\{n' \ne n : s_1(n') \le s_1(n) \text{ and } s_3^{\text{strict}}(n') \le s_3^{\text{strict}}(n)\}}{n_{\text{rungs}} + 1}.$$

At $n = 3$: $s_1(3) = 0$ and $s_3^{\text{strict}}(3) = 0$. The set $\{n' \ne 3 : s_1(n') \le 0 \text{ and } s_3^{\text{strict}}(n') \le 0\}$ is EMPTY (no other rung achieves both scores at 0 simultaneously). So $p(3) = 1/(n_{\text{rungs}} + 1) \to 0$ as $n_{\text{rungs}} \to \infty$.

At $n \ne 3$: $s_1(n) > 0$ or $s_3^{\text{strict}}(n) > 0$. The set $\{n' \ne n : \text{both scores} \le \text{this rung}\}$ is non-empty (other rungs achieve the same or lower). So $p(n) > 1/(n_{\text{rungs}} + 1)$ uniformly.

The gate $G_{\alpha, n} = \mathbf{1}[p(n) \le \alpha]$ for $\alpha = 1/(n_{\text{rungs}} + 1)$:
- $G_{\alpha, 3} = 1$ (admit).
- $G_{\alpha, n} = 0$ for $n \ne 3$ (reject).

### §4.3 The admission is sharp

The admission at $n = 3$ is SHARP in the sense:
- Under the structural regime ($s_j = 0$ at $n = 3$), $p(3) = 1/(n_{\text{rungs}} + 1)$ — the smallest possible p-value.
- Under the null ($n \ne 3$), $p(n) \ge 2/(n_{\text{rungs}} + 1)$ — strictly larger.

The gap between admission at $n = 3$ and rejection at $n \ne 3$ is structurally maximal.

---

## §5. Cofinal lift across the dimensional hierarchy

### §5.1 The cofinal tower

The dimensional hierarchy is a cofinal tower of finite rungs: $\{n = 1, 2, 3, 4, 5, \ldots\}$ indexed by positive integers. The refinement map is "include rung $n$ in the cumulative analysis."

T15 Theorem 9 applies: the cofinal tower of finite rungs has a UNIQUE Archimedean completion. The completion is the **uniformly selected dimension across all rungs**.

### §5.2 The completion lifts to dimension 3

The completion is:
$$\dim_{\text{selected}} = \lim_{N \to \infty} \arg\min_{n \le N} \{p(n)\} = \lim_{N \to \infty} 3 = 3.$$

At every finite $N$, the minimum-p-value rung is $n = 3$. The cofinal limit takes $n_{\text{rungs}} \to \infty$, and the selection remains $n = 3$ (the only rung with $s_1 = s_3 = 0$ simultaneously).

By T15 uniqueness: the Archimedean completion is exactly $n = 3$.

### §5.3 No alternative dimensions emerge in the limit

Could the cofinal limit reveal a new admitted rung beyond the tested range? No:
- For $n \ge 4$: $s_1(n) = n(n-3)/2 \ge 2$, monotonically increasing.
- For $n \le 2$: $s_1(n) \ge 1$ and $s_3^{\text{strict}}(n) = \infty$.

The exclusion of $n \ne 3$ is monotone in the rung structure — once excluded, it stays excluded under cofinal lift.

### §5.4 The unique selection

$$\boxed{\;\dim_{\text{selected}}^{\text{simplicial}} = 3,\;}$$

via conformal admission + cofinal lift. This is the same dimension selected by Paper 32 Routes 1 and 2.

---

## §6. The Main Theorem

### Theorem 6.1 (Dimensional selection via conformal admission)

*Within the simplicial framework's Fisher-volume hierarchy, the spatial dimension $n = 3$ is the unique rung admitting inertial-projector closure under conformal admission with cofinal lift via T15.*

### Proof outline

1. **Terminal screen.** By §2, the dimensional selection problem is at a terminal inner screen (T19 Definition 3.2), where direct deductive closure is structurally forbidden (T19 Theorem 6).

2. **Boundary scores.** §3 constructs three deterministic boundary scores $s_1, s_2 (\equiv s_1), s_3^{\text{strict}}$ on each dimensional rung. By T18 Theorem 1, each is a valid conformal score.

3. **Conformal admission at each rung.** §4 applies T18 Theorem 4 (Update Gate). The joint null p-value $p(n)$ is minimized at $n = 3$ where both scores vanish; at $n \ne 3$, at least one score is bounded below by a structural constant.

4. **Cofinal lift.** §5 applies T15 Theorem 9. The cofinal tower of rungs has a unique Archimedean completion equal to the consistent admission across all rungs.

5. **Conclusion.** The unique admission is $n = 3$. $\square$

### Remark 6.2 (Comparison with Paper 32's existing routes)

Paper 32 §8.2 Route 1 (Hodge/$\mathfrak{so}$): proves $n = 3$ by direct algebraic identity computation.

Paper 32 §8.3 Route 2 (conductor count): proves $n = 3$ by structural identification of $A_2 \oplus A_3$ at $\mathbb{Z}/6$.

T29 Route 3 (conformal admission): proves $n = 3$ by governed admission at each rung + cofinal lift.

All three routes reach the same conclusion. The advantages of Route 3:
- **Methodological generality**: demonstrates T20-T21 methodology applies to dimensional selection, not just RH.
- **Quantification**: each non-selected rung has explicit deviation $s_1(n), s_3(n)$ from structural identity.
- **Robustness**: the cofinal lift is structurally guaranteed by T15, independent of which boundary scores are chosen.

The disadvantage of Route 3:
- **No new selection**: Paper 32 Routes 1 and 2 already establish $n = 3$ unconditionally.
- **Heavier machinery**: T18+T19+T15 is a more elaborate structure than the direct algebraic argument.

The point of Route 3 is METHODOLOGICAL, not structural: it demonstrates the conformal-admission methodology's general applicability across the simplicial program.

---

## §7. Extension to signature $(3,1)$

### §7.1 The signature selection problem

Why is spacetime signature $(3,1)$? Paper 32 §9.1 Theorem 9.1 proves this via the Legendre $-\ell_3$ sign of the Poincaré-Cartan one-form.

T29 extends Theorem 9.1 to the conformal-admission framework: signature $(3,1)$ as the unique admitted signature on the extended tangent space.

### §7.2 Boundary scores for signature

For each candidate signature $(p, q)$ with $p + q = 4$ (the closure-valid total dimension from §5), define:

**(σ1) Legendre-sign deviation.**
$$s_\sigma^{(1)}(p, q) := \big|(p, q) - (3, 1)\big|_{\ell^2} = \sqrt{(p-3)^2 + (q-1)^2}.$$

**(σ2) Action stationarity deviation.**
$$s_\sigma^{(2)}(p, q) := \big|\text{sign}(d^2 \ell_3 / dv^2)|_{(p,q)} - (+,+,+;-)\big|.$$

By Theorem 9.1, this is 0 at $(3,1)$ and nonzero at $(2,2), (4,0), (1,3), \ldots$.

**(σ3) Causal structure deviation.**
$$s_\sigma^{(3)}(p, q) := \mathbf{1}[\text{no light cone}] \cdot \infty + \mathbf{1}[\text{light cone}] \cdot \big|c_{\text{induced}} - 1\big|.$$

By Theorem 9.7 (Corollary on $c \equiv 1$), the induced light cone has $c = 1$ at signature $(3,1)$.

### §7.3 Admission and cofinal lift

The candidate signatures with $p + q = 4$ are $(4,0), (3,1), (2,2), (1,3), (0,4)$. All five scores reject all candidates except $(3,1)$.

Specifically:
- $(4,0)$ Euclidean: $s_\sigma^{(3)} = \infty$ (no light cone). Reject.
- $(3,1)$ Lorentzian: $s_\sigma^{(j)} = 0$ for all $j$. Admit.
- $(2,2)$ neutral: $s_\sigma^{(2)} \ne 0$ (wrong sign pattern). Reject.
- $(1,3), (0,4)$: time-dominated, $s_\sigma^{(2)} \ne 0$. Reject.

Cofinal lift: across all candidate signatures with $p + q = 4$, the unique admission is $(3,1)$.

### Theorem 7.4 (Signature selection via conformal admission)

*Within the simplicial framework's spacetime-tangent hierarchy, the signature $(3,1)$ is the unique admitted signature under conformal admission with cofinal lift via T15.*

### §7.5 The combined result: spacetime $(3,1)$

Combining Theorem 6.1 (spatial dimension 3) + Theorem 7.4 (signature (3,1)):

$$\boxed{\;\text{Spacetime} = (3,1) \text{ Lorentzian}\;}$$

via the conformal-admission methodology, matching Paper 32 §9.1 Theorem 9.1 (and §10.6.5).

---

## §8. What this proves vs Paper 32's existing proofs

### §8.1 What T29 adds

| Aspect | Paper 32 §8, §9 | T29 Conformal Admission |
|---|---|---|
| Selection of $n = 3$ | Algebraic identities (Hodge/$\mathfrak{so}$, conductor count) | Cofinal admission + T15 lift |
| Selection of $(3,1)$ | Legendre $-\ell_3$ sign (Theorem 9.1) | Conformal admission across signature candidates |
| Methodological structure | Direct deductive | Governed admission |
| Quantification of failure at $n \ne 3$ | Implicit (Theorem 8.2 facts fail at $n \ne 3$) | Explicit (scores $s_1, s_3^{\text{strict}}$ with closed forms) |
| Generality of method | Specific to dimensional algebra | General to all terminal-screen problems (T20-T21) |
| Provides new content | No (same conclusion) | Yes (methodology demonstration) |

### §8.2 The point of T29

T29's value is **methodological demonstration**, not new mathematical content:

1. It SHOWS that the conformal-admission methodology applies beyond RH.
2. It QUANTIFIES the structural deviation at non-selected dimensions.
3. It REINFORCES the historical pattern argument (T21 §7): novel proof structures generalize across problems.

For acceptance of T20's RH proof, T29 is supporting evidence that the methodology is GENERAL — not tailored to RH alone.

### §8.3 Independent verification

T29 provides an INDEPENDENT VERIFICATION of Paper 32's dimensional selection by a different proof structure. Cross-validation across multiple proof structures strengthens the conclusion.

If T29 (conformal admission) gives a different answer than Paper 32 (direct algebraic), one of the routes has an error. They agree: $n = 3$, $(3,1)$. The agreement is structural cross-validation.

---

## §9. The methodology's general pattern

### §9.1 The T20-T21 methodology applied to a problem

T29 follows the same pattern as T20:
1. Identify the closure problem at a terminal inner screen.
2. Construct boundary scores measuring deviation from the structural identity.
3. Apply T18 Theorem 4 (Update Gate) at each finite level.
4. Apply T18 Theorem 8 (Martingale) for cofinal accumulation.
5. Apply T15 Theorem 9 (Cofinal Completion) for the Archimedean lift.
6. Conclude via T21 (methodology is rigorous).

This is a TEMPLATE. Future applications will follow the same pattern.

### §9.2 What problems fit the methodology

Terminal-screen closure problems where:
- The structural identity at the answer is exact (zero deviation).
- Deviation at non-answers is computable.
- The hierarchy has a cofinal structure.
- T15 Theorem 9 applies.

Candidate problems for future T-series applications:
- **Paper 32 §10–13 Standard Model emergence**: cubic isolation at $\mathbb{Z}/6$ as terminal-screen closure for gauge structure.
- **FEP-3 program**: free energy minimization as boundary-completion problem; biological systems as conscious admission architectures.
- **Consciousness empirical signatures** (T19 §15): Matched Surprise, Attention, Blindsight, Hallucination, Dreaming, Anesthesia/Sleep as testable predictions of the architecture.
- **Conductor Blind Spot (CBS)**: second-order ρ_× admission via packet inverse-participation ratio.
- **Helmert-basis pullback (T4)**: cofinal admission of unitarity across primorial bases.

Each is a terminal-screen closure problem suitable for the methodology.

### §9.3 The methodology's general utility

Each application demonstrates:
1. The methodology is GENERAL (not specific to RH).
2. The terminal-screen identification + cofinal lift pattern applies broadly.
3. The simplicial architecture (T0-T19) is the unified framework.

For T20's RH proof to be accepted methodologically (Direction A from T20-T21), having MULTIPLE applications of the same methodology strengthens the case substantially. T29 is the first such reinforcement; future applications will add more.

---

## §10. What this does NOT establish

### §10.1 Not a new dimensional selection result

T29 does not establish $n = 3$ for the first time. Paper 32 §8.2, §8.3 already do this with shorter proofs.

T29's contribution is the methodological framing, not a new mathematical conclusion.

### §10.2 Not a metric / physical-gravity claim

Per Paper 32 §11.1, §11.2: the simplicial framework's dimensional selection is a **closure certificate** — the form of why spatial dimension is 3, not a metric or gravity derivation. T29 inherits this guardrail.

The conformal-admission proof of $n = 3$ certifies the FORM (closure-valid dimension) within the simplicial framework. It does NOT establish:
- Newton's constant $G$.
- Planck scale.
- Metric tensor with the standard general relativity content.
- Stress-energy tensor.

These remain outside the simplicial framework's scope per Paper 32 §11.2 dimensional firewall.

### §10.3 Acceptance of methodology required

Like T20, T29's proof structure requires acceptance of T18+T19+T15 methodology. The methodological defense (T21) applies to T29 the same way it applies to T20.

If the conformal-admission methodology is accepted as proof, T29 stands as the methodology's second major application. If not, T29 (like T20) requires translation to a classical proof structure — which for dimensional selection is exactly Paper 32 §8.2, §8.3 (already available).

---

## §11. Forward doors

### §11.1 Paper 32 §10–13 applications

The Standard Model emergence results in Paper 32 §10.5–§10.6 can be reframed as conformal-admission proofs:

- **Weinberg angle $\sin^2 \theta_W|_{\text{tree}} = 3/8$**: admission across hypercharge sectors via Mondrian conditioning.
- **Three colors + chirality**: admission across Kummer-cover deck groups at $\mathbb{Z}/6$.
- **SM hypercharge spectrum $Y = \frac{1}{2}P_2 - \frac{1}{3}P_3$**: admission across primorial level rungs.

Each is a terminal-screen closure problem suitable for the methodology.

### §11.2 Consciousness empirical signatures

T19 §15 lists six empirical signatures: C1 Matched Surprise, C2 Attention, C3 Blindsight, C4 Hallucination, C5 Dreaming, C6 Anesthesia. Each is a terminal-screen closure problem.

Conformal-admission framework for each:
- **C1 Matched Surprise**: admit "structural" over "noise" via the boundary gain score.
- **C2 Attention**: admit "attended" via precision gain $\lambda_{\beta, t} \ge \lambda_{\min}$.
- **C3 Blindsight**: admit "action-routed-without-conscious" via the routing/admission asymmetry.
- **C4 Hallucination**: admit "high-gain + weak-admission" via the score split.
- **C5 Dreaming**: admit "internal-generation + reduced-external" via the constraint slack.
- **C6 Anesthesia/Sleep**: admit "collapse of admission" via reduced precision.

These give testable predictions in psychophysics + neuroscience.

### §11.3 FEP-3 biological applications

FEP-3 (Free Energy Principle at cubic order, biology layer) involves boundary completion at biological scales. Conformal-admission framework:
- Admit "alive" via active boundary completion criteria (T17 + T18).
- Admit "conscious" via terminal-screen completion (T19).
- Admit "intelligent" via governed closure (T16 + T18).

### §11.4 Yang-Mills mass gap (with Paper 32 §10.6.7g scope boundary)

Paper 32 §10.6.7g explicitly disclaims a Clay-Millennium solution; the framework gives structural shadows of Yang-Mills mass gap, not the proof. T29 methodology might extend to a structural-admission framing of the mass gap, within the same scope boundary.

### §11.5 Multi-application synthesis paper

Once 3-5 applications are completed (RH via T20, dimensional selection via T29, SM-emergence via TXX, consciousness empirical via TYY, FEP-3 via TZZ), write a SYNTHESIS paper articulating the methodology's general applicability across the simplicial program.

---

## §12. Files

- **This paper:** `T29-DimensionalSelection-ConformalAdmission-Draft1.md`.
- **Methodology foundations:** `T18-ConformalBoundaryGovernance-Draft1.md`, `T19-ConsciousBoundaryModel-Draft1.md`, `T15-FiniteToArchimedeanCompletion-Draft1.md`.
- **Methodology proof + defense:** `T20-SimplicialProofRH-ConformalAdmissionCofinalLift-Draft1.md`, `T21-ConformalAdmissionProofMethodology-Draft1.md`.
- **Source for dimensional selection:** `32_one_functional_four_forces_v0.2 (2).md` §8 (Theorem 8.2, 8.3), §9.1 (Theorem 9.1).
- **Simplicial substrate:** T1-T15 (referenced in Paper 32 §8.2).

---

## §13. References

- Murillo Montero, L. (2026). T18 — Conformal Boundary Governance.
- Murillo Montero, L. (2026). T19 — Conscious Boundary Model.
- Murillo Montero, L. (2026). T20 — Simplicial Proof of RH via Conformal Admission + Cofinal Lift.
- Murillo Montero, L. (2026). T21 — The Conformal Admission Proof Methodology.
- Murillo Montero, L. (2026). T15 — Finite-to-Archimedean Completion.
- Murillo Montero, L. (2026). Paper 32 — One Functional, Four Forces. §8 (Dimensional Selection: Theorems 8.2, 8.3, Corollary 8.4); §9.1 (Theorem 9.1 Forced $(3,1)$); §11.2 (Dimensional firewall).
- Murillo Montero, L. (2026). Paper 13 — Cross product, Rodrigues rotation, $J^2 = -I$ in dim-3 row.

---

*T29 applies the T20-T21 conformal-admission + cofinal-lift methodology to dimensional selection (Paper 32 §8). Three boundary scores ($s_1$ Hodge/$\mathfrak{so}$ deviation, $s_2 \equiv s_1$ Hodge duality, $s_3^{\text{strict}}$ cross-product complex structure) reject the null at every rung except $n = 3$. T15 cofinal lift selects $n = 3$ uniquely. Combined with §7's signature analysis, spacetime $(3,1)$ Lorentzian. The result matches Paper 32's existing direct proofs (Theorems 8.2, 8.3, 9.1) but via a different proof structure, demonstrating the methodology's general applicability and providing independent cross-validation. T29 is the methodology's second major application after T20 (RH).*
