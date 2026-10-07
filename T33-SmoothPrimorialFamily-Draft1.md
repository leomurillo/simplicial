# T33 — The Smooth Primorial Family: Bohr–Mollerup, Wielandt, and the Constant Tower of the Prime Ladder

**Leonardo Murillo Montero**

*First draft — May 28, 2026 — opening tool paper for the smooth primorial framework*

<!--
PLANTATION — file-level notes.

This is T33: a single tool paper that builds the smooth primorial function
and its divisor-lattice family, with two uniqueness theorems (Bohr–Mollerup,
Wielandt) and an explicit constant-tower indexed by starting prime.

The paper sits between Γ (which already smooths factorial) and the
primorial ladder Z/P_k that drives the T-series. It is the analytic
continuation of the program's primorial-indexed objects to a continuous
parameter, with three principal applications:

  (i)   N1 dimension refinement (Item 3): the apex unitary's principal
        block has smooth dimension tilde-phi(z), not pri(z) - 1.
  (ii)  GG-ledger gravity-localization rate (Item 4 of yesterday's list):
        the fraction of apex degrees of freedom that is gravity-carrying
        is 1/(e^{tilde-gamma-star} log p_n) — Mertens-density quantitative
        form of the program's claim "gravity localizes to multiplicative
        units."
  (iii) Constant tower (the destiny-window insight): every "standard"
        analytic-NT constant (γ, ζ(k), log 2, log(2π)) is the "start-from-2"
        representative of a family indexed by which primes have already
        been captured.

Structure follows Paper 35 (grounded-paranoid-delusional):
  §0 Status and methodology
  §1 Delusional (Historic Fiction — the vision)
  §2 Standalone object (anchored definitions, no T-series prereqs)
  §3 Paranoid (pre-claimed audits)
  §4 Grounded — Part A (prime-side)
  §5 Grounded — Part B (duality)
  §6 Grounded — Part C (Bohr–Mollerup)
  §7 Grounded — Part D (Wielandt)
  §8 The divisor family (Mertens, Jordan, ζ(k))
  §9 The destiny window (sieve structure)
  §10 The constant tower (starting-prime family)
  §11 Negative ledger (what doesn't translate)
  §12 Implications for the program (N1, GG-ledger, RH)
  §13 Ledger (tiered claims)
  §14 Safe / unsafe statements
  §15 Coda

Plantation notes throughout are scoped to the section they sit in.
They are the methodological record (Paper 35 §3.6) and are kept inline.
-->

---

## §0 Status and methodology

This paper applies the grounded-paranoid-delusional methodology of [Paper 35](35_grounded_paranoid_delusional_methodology.md) to the construction of a canonical continuous interpolation of the primorial function and its divisor-lattice family of related multiplicative invariants. The question is high-variance (a single foundational tool, potentially load-bearing for the N-series and the RH program in primorial-side form) and high-conviction (the framework yields explicit constant-tower identities and forces structural sharpenings of [N1](N1-ApexUnitaries-Draft1.md)), and Paper 35 §1.1 names exactly this combination as the setting requiring an explicit verification gate inside the elaboration loop.

The structure of the paper traces one full cycle through the methodology:

- **Delusional** (§1). The Historic Fiction — what a fully realized continuous-primorial framework would look like. Permitted to determine *what is worth attempting*; explicitly denied any vote on truth.
- **Paranoid** (§3). Four audits — existence, uniqueness, analyticity, divisor-family emission — each with K / L / joint-on-disjoint outcomes pre-committed in writing *before* §4–§8 was executed.
- **Grounded** (§4–§8). Deterministic settlements: Part A (prime-side smooth primorial), Part B (index–prime duality), Part C (Bohr–Mollerup uniqueness), Part D (Wielandt analyticity), and the divisor-family closure with explicit constant emissions.

The three-tier ledger ([P] proven, [A] structural pending named audit, [C] conjectural reduced) is used throughout. §13 lists every claim by tier. §14 states what the paper does and does not assert.

The methodology's principal failure mode — Paper 35 §6.1, *divergence as permanent deferral of settlement* — is the visible risk for any tool paper of this scope. The defense executed here: each Part (A, B, C, D) settles a concrete result at the [P] tier, with proofs reproducible by hand. The divisor-family closure (§8) gives one explicit positive constant emission ($1/\zeta(k)$, exact, no bias) and one explicit *negative* result with corrected bias term ($\widetilde\gamma_*$, smooth Mertens, biased from $\gamma$ by a named Riemann-error integral). The deferral risk is acknowledged but not used.

<!--
PLANTATION — methodology check.

The pre-claim for the divisor-family audit (§3.4) was written *before* §8
was executed. I had initially conjectured (during the conversational
development of these results) that γ would emerge cleanly from the
pri/tilde-phi ratio. The §8 grounded computation REVEALED a smooth-vs-discrete
bias of ≈ 0.035 = γ̃_* − γ. The corrected statement records both constants
and identifies the bias as a Riemann-error integral over (π − Li)/(u(u−1)).

This is the methodology working as designed: the paranoid pre-claim was
strong ("γ emerges"); the grounded computation falsified the strong form
but produced a richer structural result (two constants linked by an
explicit Riemann-error integral). Recorded honestly in §3.4 and §8.

No tier-crossing: the discrete Mertens γ and the smooth γ̃_* are both [P]
at their own statements; the relation between them is [P] via Abel summation.

Possible counter-narrative I considered and rejected: "this is just a
boundary-constant adjustment, of no structural content." Rejected because
the bias is identifiable as a specific number-theoretic integral and the
correction propagates predictably to higher Jordan totients (where it
vanishes for k ≥ 2, the structural reason for the clean Item 4 closure).
-->

---

## §1 The Historic Fiction — the smooth primorial family fully realized (delusional layer)

<!--
PLANTATION — Paper 35 §5 Historic Fiction.

This section is permitted to be ambitious. It supplies direction. It does
not vote on truth. Anything I assert here passes through §3 pre-claims
and §4–§8 grounded settlement before being citable.
-->

The factorial function $n \mapsto n!$ has a unique canonical analytic interpolation: $\Gamma(z+1)$. This interpolation is forced by the recursion $\Gamma(z+1) = z\Gamma(z)$, the boundary $\Gamma(1) = 1$, and either log-convexity (Bohr–Mollerup) or analytic boundedness on a strip (Wielandt). $\Gamma$ admits a Hadamard product, a reflection formula, a duplication formula, a digamma function emitting Euler's constant $\gamma$, and a Mellin transform representation. It completes $\zeta$ via the explicit formula $\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ symmetric under $s \leftrightarrow 1-s$.

The primorial function $n \mapsto P_n = \prod_{k\le n} p_k$ has had no analogous canonical interpolation. Numerical interpolation by log-linear chord (the trivial $C^0$ extension) exists but is non-analytic; the smoothness gap to $\Gamma$-quality analytic interpolation has been a foundational hole in the program's continuous-parameter machinery.

The thesis of this paper is that **the primorial admits a canonical analytic interpolation forced by Riemann's explicit formula**, and that this interpolation is one component of a *family* of smooth functions indexed by the divisor-lattice multiplicative invariants ($\phi$, $\sigma$, $J_k$, $d$, etc.), with the asymptotic ratios between family members being the canonical analytic-NT constants ($\gamma$, $\zeta(k)$, log primes, log $2\pi$) in their natural structural homes.

The Historic Fiction of a fully realized smooth primorial framework — read as a vision, not as a claim — is:

**T33 (this paper).** *The smooth primorial family.* Bohr–Mollerup and Wielandt uniqueness, divisor-lattice family, constant-tower emissions, integration with the apex unitary dimension refinement. The series's entry hall.

**T33.1.** *The Hadamard product of $\mathrm{pri}_{\mathrm{idx},\sharp}$.* Explicit zero locations, growth rate, comparison with $\Gamma$'s Hadamard structure. The smooth primorial's intrinsic complex-analytic skeleton.

**T33.2.** *Stieltjes-Phragmén–Lindelöf form of Wielandt.* Replace Wielandt's strip-boundedness condition with a finite-exponential-type condition, eliminating the artificial growth-tracking requirement. The cleanest possible analytic uniqueness theorem.

**T33.3.** *The Mellin transform representation.* $\mathrm{pri}_{\mathrm{idx},\sharp}$ as the Mellin transform of an explicit kernel function. Companion to $\Gamma$'s $e^{-t}$ kernel.

**T33.4.** *Transfinite extensions.* $\mathrm{pri}_{\mathrm{idx},\sharp}(\omega)$, $\mathrm{pri}_{\mathrm{idx},\sharp}(\omega+1)$, regularized values at countable ordinals; connection to $\zeta$-regularization of primorial-indexed products.

**T33.5.** *The starting-prime tower.* The 1-parameter family $\mathrm{pri}^{(p)}$ indexed by starting prime $p$, with explicit shift formulas between members. Identification of the "absolute base" of the constant tower (the $p \to \infty$ limit) and the "ladder-bottom" (the $p = 2$ standard case).

**T34.** *The smooth primorial in N-series applications.* Refinement of N1's apex unitary dimension claim (principal block lives in $U(\widetilde\phi(z)/2)$, the K-antisymmetric half); smooth-family identities for $\det U_{P_n}$, $\mathrm{tr}\,U_{P_n}$, $\mathrm{Spec}(U_{P_n})$.

**T35.** *Gravity-localization rate.* Quantitative form of the GG-ledger claim "gravity localizes to multiplicative units" via $\widetilde\phi(z)/\mathrm{pri}_{\mathrm{idx},\sharp}(z) \sim 1/(e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z))$. Numerical localization fractions at $P_1, P_2, \ldots, P_{30}$.

What T33 must deliver to launch the framework legitimately:

1. A standalone definition of $\mathrm{pri}_{\mathrm{idx},\sharp}$ requiring no T-series prerequisites (§2).
2. At least one uniqueness theorem at the [P] tier with the proof reproducible by hand (§6 Bohr–Mollerup, §7 Wielandt; both settled).
3. Explicit constant emissions with honest accounting of bias terms (§8, [P] with named correction).
4. Pre-claimed audits for the next layer (§3) with both outcomes pre-committed.
5. An explicit, tiered ledger (§13) and a safe/unsafe statement set (§14).

<!--
PLANTATION — what's deliberately NOT in §1.

The Historic Fiction does *not* assert that any of T33.1–T35 will close
positively. They might all close jointly-on-disjoint, or two might
close negative with the negatives themselves being publishable
results. Per Paper 35 §3.1, the pre-claim is what determines value,
not the realized branch.

I am also deliberately NOT including any speculation about RH closure
via the smooth primorial. The investigation conducted alongside this
draft (see §11, RH negative ledger) settles this: the smooth pri family
inherits the structural envelope of finite-Q Hurwitz, which per
nueve §6.6 does not separate on-line from off-line zeros. The smooth
framework is a tool for analytic continuation and constant emission,
NOT a new attack on RH. Stating this honestly in §1 prevents the
Historic Fiction from drifting into press-release territory.
-->

---

## §2 The objects — definitions standalone, no T-series prerequisites

<!--
PLANTATION — anchoring (Paper 35 §3.3).

This section is intentionally self-contained. A reader who has never
read T0/T4/T9/N1 should be able to take the §2 definitions, the §3
pre-claims, and the §4–§8 settlements, and verify the constructions
from scratch. The anchored objects are the formulas on lines (2.1)–(2.5).

Cross-references to T-series are kept as parenthetical pointers
("(cf. N1 §2)") for the program reader; they are not load-bearing
for the §4–§8 settlements.
-->

### 2.1 The discrete primorial

For $n \in \mathbb Z_{\ge 0}$, the *index-side primorial* is
$$P_n := \prod_{k=1}^n p_k, \qquad P_0 := 1,$$
where $p_k$ is the $k$-th prime ($p_1 = 2$, $p_2 = 3$, $p_3 = 5$, …). For $x \ge 2$, the *prime-side primorial* is
$$\mathrm{pri}_*(x) := \prod_{p \le x} p, \qquad \mathrm{pri}_*(x) := 1 \text{ for } x < 2.$$
These are right-continuous, monotone-non-decreasing, $\mathbb Z_{>0}$-valued functions with $\mathrm{pri}_*(p_n) = P_n$.

### 2.2 The Chebyshev–primorial identity

The two primorials are related by Chebyshev's first function $\vartheta(x) := \sum_{p\le x}\log p$:
$$\log\mathrm{pri}_*(x) = \vartheta(x), \qquad \log P_n = \vartheta(p_n).$$

### 2.3 The logarithmic integral and its inverse

For $x \ge 2$, let
$$\mathrm{Li}(x) := \int_2^x \frac{dt}{\log t}$$
denote the Eulerian (shifted) logarithmic integral, $\mathrm{Li}(2) = 0$. $\mathrm{Li}$ is real-analytic, strictly increasing, and strictly concave on $(1,\infty)$, with $\mathrm{Li}(x) \sim x/\log x$ as $x \to \infty$ (Euler–Maclaurin). The inverse function $\mathrm{Li}^{-1}: [0,\infty) \to [2,\infty)$ is real-analytic, strictly increasing, strictly convex, with $\mathrm{Li}^{-1}(0) = 2$ and $(\mathrm{Li}^{-1})'(z) = \log\bigl(\mathrm{Li}^{-1}(z)\bigr)$.

### 2.4 The smooth primorial — prime side and index side

The *canonical smooth prime-side primorial* is
$$\boxed{\;\mathrm{pri}_\sharp(x) \;:=\; \frac{e^x}{2\pi}, \qquad x \in \mathbb R.\;} \qquad (2.1)$$
The *canonical smooth index-side primorial* is
$$\boxed{\;פ(z) \;\equiv\; \mathrm{pri}_{\mathrm{idx},\sharp}(z) \;:=\; \frac{e^{\mathrm{Li}^{-1}(z)}}{2\pi}, \qquad z \in [0,\infty).\;} \qquad (2.2)$$
These are linked by $פ(z) = \mathrm{pri}_\sharp(\mathrm{Li}^{-1}(z))$ — the duality of §5. We adopt the symbol **פ** (Hebrew *pe*, for *primorial*; notation and completion-theoretic meaning introduced in [T15 §12](T15-FiniteToArchimedeanCompletion-Draft1.md)) for the index-side smooth primorial, and use $\mathrm{pri}_\sharp$ for its prime-side form. **T15 §12 owns what פ *means*** — it is the scalar finite-to-archimedean completion of the primorial tower, the $1/(2\pi)$ being the archimedean boundary, and the moment obstruction (§9A.5 below) proving the real place is not a finite packet. **This paper provides the analytic construction.**

### 2.5 The divisor-family extensions

For each multiplicative invariant of primorials, the *smooth family member* is defined via the smooth integral of $\log$ of the multiplier:
$$\log\widetilde\phi(z) := \int_0^z \log\bigl(\mathrm{Li}^{-1}(t) - 1\bigr)dt + C_\phi, \qquad (2.3)$$
$$\log\widetilde\sigma(z) := \int_0^z \log\bigl(\mathrm{Li}^{-1}(t) + 1\bigr)dt + C_\sigma, \qquad (2.4)$$
$$\log\widetilde J_k(z) := \int_0^z \log\bigl(\mathrm{Li}^{-1}(t)^k - 1\bigr)dt + C_{J_k}, \quad k \ge 1, \qquad (2.5)$$
with boundary constants $C_\phi, C_\sigma, C_{J_k}$ chosen by the discrete-matching condition of §8 (one degree of freedom per family member, fixed by the Mertens or Euler-product asymptotic).

### 2.6 The full ledger of objects

The smooth primorial family is the tuple
$$\bigl(\mathrm{pri}_{\mathrm{idx},\sharp},\, \widetilde\phi,\, \widetilde\sigma,\, \widetilde J_k\bigr)_{z \in [0,\infty), k \ge 1}$$
together with the Möbius/character extensions $\widetilde\mu(z) = e^{i\pi z}$ (degenerate; §11) and the starting-prime variants $\mathrm{pri}^{(p)}$ (§10). All eight first-level objects (the four in §2.4–§2.5 plus the four starting-prime shifts) are canonically defined modulo the boundary constants, which are fixed once each by the discrete matching of §8.

---

## §3 Pre-claimed audits — paranoid layer

Before any of §4–§8 was executed, the following matched-pair pre-claims were committed in writing. Each branch is stated with the same concreteness as the others. The realized branch in each case is recorded in §4–§8.

### 3.1 The existence-and-canonicity audit (Part A and B)

**Question.** Is there a canonical smooth primorial, and if so, what forces it?

**Pre-claim — branches:**

- **K (forced by explicit formula).** There exists a canonical smooth primorial $\mathrm{pri}_\sharp(x)$ such that $\log\mathrm{pri}_*(x) - \log\mathrm{pri}_\sharp(x) = -\sum_\rho x^\rho/\rho + O(\sqrt x)$, where the sum is over non-trivial zeros of $\zeta$. The constant in $\mathrm{pri}_\sharp$ is forced to be $1/(2\pi)$ by $-\zeta'(0)/\zeta(0) = \log(2\pi)$ in Riemann's explicit formula for $\psi$.
- **L (free constant).** No constant is forced; the smooth primorial is only determined up to a multiplicative gauge.
- **Joint-on-disjoint.** A canonical constant exists but is not $1/(2\pi)$ — instead some other constant from the explicit formula (e.g., $\log 2$ from the prime-power leakage between $\psi$ and $\vartheta$).

**Anchored settlement target.** Direct comparison of the leading non-oscillatory part of Riemann's explicit formula for $\psi$ (resp. $\vartheta$) with the prescribed smooth $\mathrm{pri}_\sharp(x) = e^x/(2\pi)$. K-branch fires iff the non-oscillatory part matches $\mathrm{pri}_\sharp$ up to the prime-power leakage $O(\sqrt x)$.

**Realized branch.** K, in the sharp form (4.2). The constant $1/(2\pi)$ is forced by $-\zeta'(0)/\zeta(0)$.

<!--
PLANTATION — note the asymmetry between L and joint-on-disjoint.

L is the "no canonical answer" branch — would force us to publish the
smooth pri only up to gauge, with the gauge ambiguity itself being the
result. Joint-on-disjoint allows a canonical constant but not 1/(2π);
would require us to identify a different explicit-formula constant
and recompute the duality.

Both branches were pre-committed as publishable outcomes per Paper 35
§3.1. The K-branch realization in §4 supersedes the contingency, but
the pre-claim's articulation of the alternatives was substantive.
-->

### 3.2 The uniqueness audit (Part C — Bohr–Mollerup)

**Question.** Once a canonical smooth primorial is defined, is it unique under Bohr–Mollerup-style conditions?

**Pre-claim — branches:**

- **K (unique via log-convexity).** $\log\mathrm{pri}_{\mathrm{idx},\sharp}$ is the unique convex function on $[0,\infty)$ satisfying the recursion (BM1) and boundary (BM2) of Theorem C.3 below.
- **L (non-unique).** Multiple convex log-functions satisfy the recursion-plus-boundary, with the non-uniqueness encoding additional arithmetic information (e.g., a 1-parameter family of "boundary phase" choices).
- **Joint-on-disjoint.** Uniqueness holds but the proof requires a stronger condition than log-convexity — e.g., $\log\log$ convexity, or convexity of $\log(\log\mathrm{pri}/(\log z))$ (a "Stirling-normalized" log).

**Realized branch.** K, with proof by the classical Bohr–Mollerup squeeze applied to $\Delta(z) := \mathrm{Li}^{-1}(z+1) - \mathrm{Li}^{-1}(z)$. The monotonicity of $\Delta$ (a consequence of $\mathrm{Li}^{-1}$ convex) is the only structural ingredient required beyond the standard $\Gamma$-proof.

### 3.3 The analyticity audit (Part D — Wielandt)

**Question.** Does $\mathrm{pri}_{\mathrm{idx},\sharp}$ have a Wielandt-style analytic uniqueness characterization?

**Pre-claim — branches:**

- **K (Stirling-rate decay).** $\mathrm{pri}_{\mathrm{idx},\sharp}$ decays on vertical strips at the same exponential rate as $\Gamma$ (i.e., $|t|^{c}e^{-\pi|t|/2}$ for some explicit $c$), enabling a Wielandt-style strip-boundedness uniqueness.
- **L (different rate).** Decay exists but at a different rate (e.g., $e^{-\pi|t|}$ or $e^{-\pi|t|/4}$), breaking the structural parallel with $\Gamma$.
- **Joint-on-disjoint.** Same rate $\pi/2$, but the polynomial prefactor differs from $\Gamma$'s $|t|^{\sigma - 1/2}$ in a structurally meaningful way (e.g., $|t|^\sigma$ vs $|t|^{\sigma - 1/2}$, indicating a "Stirling-like correction" specific to the smooth primorial).

**Realized branch.** Joint-on-disjoint. The exponential rate $\pi/2$ matches $\Gamma$; the polynomial prefactor is $|t|^\sigma$ (one half-power higher than $\Gamma$'s $|t|^{\sigma - 1/2}$). The Wielandt argument goes through with a small adjustment to the boundedness condition.

### 3.4 The divisor-family audit (Part D ext / §8)

**Question.** Do the smooth-family ratios $\mathrm{pri}/\widetilde\phi$, $\widetilde\sigma/\mathrm{pri}$, $\widetilde J_k/\mathrm{pri}^k$ emit the canonical analytic-NT constants ($\gamma$, $\zeta(k)$) cleanly in the asymptotic $z \to \infty$?

**Pre-claim — branches:**

- **K (clean emission).** Every smooth-family ratio emits the discrete-Mertens or Euler-product constant exactly: $\mathrm{pri}/\widetilde\phi \to e^\gamma \log\mathrm{Li}^{-1}(z)$, $\widetilde J_k/\mathrm{pri}^k \to 1/\zeta(k)$ for $k \ge 2$.
- **L (no emission).** The ratios diverge or oscillate without producing identifiable constants.
- **Joint-on-disjoint.** Some ratios emit cleanly ($\widetilde J_k$ for $k \ge 2$), others emit a *shifted* constant (e.g., $\mathrm{pri}/\widetilde\phi$ emits $\gamma$ plus a named Riemann-error integral). The partition is governed by Euler-product convergence regime: absolutely convergent ($s \ge 2$) gives clean emission; conditionally convergent ($s = 1$, Mertens regime) gives shifted emission.

**Realized branch.** Joint-on-disjoint. The clean partition between $\zeta(k)$ for $k \ge 2$ (no bias) and $\gamma$-Mertens (bias $\widetilde\gamma_* - \gamma = \int_2^\infty (\pi - \mathrm{Li})/(u(u-1))\,du$) is exactly the partition predicted by absolute-vs-conditional convergence of the underlying Euler product.

<!--
PLANTATION — the joint-on-disjoint realization is structurally rich.

The strong K-claim (γ emerges cleanly) was my initial conjecture during
the conversational development. The grounded computation in §8 revealed
that the smooth Mertens constant γ̃_* differs from γ by an explicit
Riemann-error integral. This is the joint-on-disjoint branch realizing:
γ does emerge, but with a known bias term that is itself a named
number-theoretic constant.

This is genuinely better than the clean K-branch would have been:
- Clean K would have given γ and stopped.
- Joint-on-disjoint gives γ̃_*, the explicit bias, AND the identification
  of the bias as a Riemann-error integral — a richer structural result.

The §13 ledger records both γ̃_* and the bias-as-integral as separate
[P] items.
-->

### 3.5 What would falsify the whole T33 framework

If §4 returned a smooth $\mathrm{pri}_\sharp$ with no canonical constant (L-branch of 3.1), the framework would devolve to a gauge-ambiguous tool with limited program utility. Re-examination of the explicit formula's non-oscillatory part is the diagnostic; if the L-branch survived, fold T33 into a no-go paper documenting the obstruction.

If §6/§7 failed to give uniqueness (L-branches of 3.2/3.3), $\mathrm{pri}_{\mathrm{idx},\sharp}$ would be one of many smooth primorials, removing the "canonical" claim and reducing the paper to a single construction without a characterization.

If §8 failed to emit named constants (L-branch of 3.4), the divisor-family extension would be without analytic content, removing the constant-tower interpretation.

These contingencies are pre-committed. The negative outcomes are publishable. The methodology forbids reframing a negative as anything else (Paper 35 §3.1).

<!--
PLANTATION — the failure-publication commitment matters.

Paper 35 §3.1 demands that the negative branch be stated with the same
concreteness as the positive. Here the negatives name exactly what
the alternative paper would look like: "no-go demarcation on smooth
primorial canonicity / uniqueness / emission." The K (and joint-on-disjoint)
realizations supersede these contingencies; recording the contingencies
is the methodological audit trail.
-->

---

## §4 Part A — Prime-side smooth primorial (grounded)

### 4.1 The exact prime-side object

$\mathrm{pri}_*(x) = \prod_{p\le x} p$ is the right-continuous step function with jump $p$ at each prime $p$. The identity $\log\mathrm{pri}_*(x) = \vartheta(x)$ is tautological.

### 4.2 The Riemann–von Mangoldt explicit formula

The standard explicit formula for $\psi(x) := \sum_{n\le x}\Lambda(n)$ is, for $x > 1$ not a prime power,
$$\psi_0(x) \;=\; x \;-\; \sum_\rho\frac{x^\rho}{\rho} \;-\; \log(2\pi) \;-\; \tfrac12\log(1 - x^{-2}),$$
where $\rho$ ranges over the non-trivial zeros of $\zeta$ and the sum is interpreted symmetrically. The penultimate constant equals $-\zeta'(0)/\zeta(0) = \log(2\pi)$.

For $\vartheta = \psi - \sum_{k\ge 2}\vartheta(x^{1/k})$, the prime-power leakage contributes $O(\sqrt x)$:
$$\vartheta(x) \;=\; x \;-\; \log(2\pi) \;-\; \sum_\rho\frac{x^\rho}{\rho} \;-\; \tfrac12\log(1 - x^{-2}) \;-\; \sum_{k\ge 2}\vartheta(x^{1/k}). \qquad (4.1)$$

### 4.3 The canonical smooth prime-side primorial

Extracting the non-oscillatory leading part of (4.1) — the terms independent of zero locations and prime-power leakage — gives the canonical smooth Chebyshev function $\vartheta_{\text{smooth}}(x) = x - \log(2\pi)$, hence
$$\boxed{\;\mathrm{pri}_\sharp(x) \;:=\; \exp(\vartheta_{\text{smooth}}(x)) \;=\; \frac{e^x}{2\pi}.\;} \qquad (4.2)$$

This is **forced** by the explicit formula: no constant is free; every term in $\mathrm{pri}_\sharp$ comes from $\zeta$ at $s = 0$. The K-branch of audit 3.1 fires sharply. The factor $1/(2\pi) = e^{-\log 2\pi}$ with $\log(2\pi) = -\zeta'(0)/\zeta(0)$ is the **archimedean boundary term**: it is what [T15 §12.2](T15-FiniteToArchimedeanCompletion-Draft1.md) identifies as the real-place completion of the finite primorial tower (פ is the scalar instance of T15's completion).

**Settlement (4.2) is [P]**, contingent on Riemann's explicit formula (a classical result of [Riemann 1859]; rigorous form due to [von Mangoldt 1895]; cf. Titchmarsh §3).

### 4.4 The deviation is the Riemann zero-sum

**Proposition 4.1.** For $x > 1$ not a prime power,
$$\log\frac{\mathrm{pri}_*(x)}{\mathrm{pri}_\sharp(x)} \;=\; -\sum_\rho\frac{x^\rho}{\rho} \;+\; O(\sqrt x). \qquad (4.3)$$

*Proof.* From (4.1): $\vartheta(x) - (x - \log 2\pi) = -\sum_\rho x^\rho/\rho - \tfrac12\log(1-x^{-2}) - \sum_{k\ge 2}\vartheta(x^{1/k})$. The latter two terms are $O(\sqrt x)$. $\square$

**Corollary 4.2 (RH in prime-side form).** The following are equivalent:

(i) The Riemann hypothesis.

(ii) $\log\mathrm{pri}_*(x) - \log\mathrm{pri}_\sharp(x) = O(\sqrt x\,\log^2 x)$ as $x\to\infty$.

This is RH stated entirely inside the primorial framework. The proof is the standard equivalence $\mathrm{RH} \Leftrightarrow \vartheta(x) = x + O(\sqrt x\log^2 x)$.

### 4.5 Order, growth, Hadamard

$\mathrm{pri}_\sharp(x) = e^x/(2\pi)$ is entire of order 1, type 1. The exact $\mathrm{pri}_*(x)$ is a sum-of-step-functions with the explicit-formula representation (4.1). The Hadamard product for $\mathrm{pri}_*$ thus inherits from $\zeta$'s via the explicit formula; the smooth primorial's analytic structure is, in a precise sense, $\zeta$'s analytic structure exponentiated.

---

## §5 Part B — Index–prime duality (grounded)

### 5.1 The integer duality

**Lemma 5.1.** For $n \in \mathbb Z_{\ge 0}$,
$$P_n \;=\; \mathrm{pri}_*(p_n).$$

*Proof.* The primes $\le p_n$ are exactly $p_1, \ldots, p_n$. $\square$

This is tautological, but it is the load-bearing identity for the duality. It says: $P_n$ is $\mathrm{pri}_*$ reparameterized via the prime-enumeration map $n \mapsto p_n$.

### 5.2 The canonical reparameterization

The map $n \mapsto p_n$ is the inverse of $\pi(x) := \#\{p \le x : p\text{ prime}\}$ at integers. To lift to a smooth $\tilde p: \mathbb R_{\ge 0} \to \mathbb R_{\ge 2}$ with $\tilde p(n) \approx p_n$, we choose a smooth replacement for $\pi$.

Riemann's explicit formula for $\pi$ gives the leading non-oscillatory term as $\mathrm{Li}(x)$:
$$\pi(x) \;=\; \mathrm{Li}(x) \;-\; \sum_\rho \mathrm{Li}(x^\rho) \;-\; \log 2 \;+\; \int_x^\infty\frac{dt}{t(t^2-1)\log t}.$$

The canonical smooth $\tilde p$ is therefore $\mathrm{Li}^{-1}$:
$$\boxed{\;\tilde p(z) := \mathrm{Li}^{-1}(z),\quad \tilde p(0) = 2,\quad \tilde p(n) = p_n + O(\sqrt{p_n}\log p_n) \text{ under RH}.\;} \qquad (5.1)$$

Alternative refinement: $\tilde p(z) := R^{-1}(z)$ where $R(x) := \sum_{k\ge 1}\frac{\mu(k)}{k}\mathrm{Li}(x^{1/k})$ (Riemann's $R$-function). All structural results transfer verbatim with $R^{-1}$ replacing $\mathrm{Li}^{-1}$; the choice between them is refinement of constants, not framework.

### 5.3 The smooth index-side primorial

$$\boxed{\;\mathrm{pri}_{\mathrm{idx},\sharp}(z) \;:=\; \mathrm{pri}_\sharp\bigl(\tilde p(z)\bigr) \;=\; \frac{\exp\bigl(\mathrm{Li}^{-1}(z)\bigr)}{2\pi}.\;} \qquad (5.2)$$

### 5.4 The duality diagrams

**Exact (integer) duality:**
$$
\begin{array}{ccc}
\mathbb Z_{\ge 0} & \xrightarrow{n \mapsto p_n} & \{p_n\} \\
\downarrow P_\bullet & & \downarrow \mathrm{pri}_* \\
\mathbb Z_{>0} & = & \mathbb Z_{>0}
\end{array}
$$

**Smooth duality:**
$$
\begin{array}{ccc}
[0,\infty) & \xrightarrow{\tilde p\,=\,\mathrm{Li}^{-1}} & [2,\infty) \\
\downarrow \mathrm{pri}_{\mathrm{idx},\sharp} & & \downarrow \mathrm{pri}_\sharp \\
(0,\infty) & = & (0,\infty)
\end{array}
$$

The difference between the two diagrams is concentrated entirely in the top horizontal arrow ($\tilde p$ vs the discrete $n\mapsto p_n$). The vertical arrows are forced once the top is chosen.

### 5.5 The boundary baseline constant

$\mathrm{pri}_{\mathrm{idx},\sharp}(0) = e^2/(2\pi) \approx 1.177$, **not** $1$. The exact $P_0 = 1$ differs from the smooth baseline by an explicit factor $e^{-2}\cdot 2\pi$. This is honest: the smooth and exact functions differ even at the boundary, by an amount fixed by the explicit-formula constant $\log(2\pi)$. Forcing $\mathrm{pri}_{\mathrm{idx},\sharp}(0) = 1$ by ad-hoc renormalization would discard the $\log(2\pi)$ that completes $\zeta$ into $\xi$; we keep the structural constant and accept the boundary offset.

### 5.6 RH in dual form

**Corollary 5.2 (RH in index form).** RH is equivalent to
$$\log P_n - \log\mathrm{pri}_{\mathrm{idx},\sharp}(n) \;=\; O\bigl(\sqrt{p_n}\log^2 p_n\bigr).$$

This is the index-side companion to Corollary 4.2.

### 5.7 Numerical verification at small $n$

By Newton's method on $\mathrm{Li}(x) = n$ with starting point $x_0$ near $p_n$:

| $n$ | $\mathrm{Li}^{-1}(n)$ | $\mathrm{pri}_{\mathrm{idx},\sharp}(n)$ | $P_n$ | ratio |
|---|---|---|---|---|
| 0 | $2.0000$ | $1.177$ | $1$ | $1.177$ |
| 1 | $2.8945$ | $2.879$ | $2$ | $1.440$ |
| 2 | $4.1086$ | $9.687$ | $6$ | $1.614$ |
| 3 | $5.6875$ | $46.998$ | $30$ | $1.567$ |
| 4 | $7.572$ | $309.27$ | $210$ | $1.473$ |
| 5 | $9.72$ | $1850$ | $2310$ | $0.801$ |
| 10 | $\approx 23.5$ | $\approx 2.57\times 10^9$ | $6.47\times 10^9$ | $0.40$ |

The ratio is not monotone; it crosses 1 between $n=4$ and $n=5$. At small $n$ the smooth overshoots; at $n \ge 5$ it undershoots. The crossover is exactly the index-side reflection of the prime-counter sign flip $\mathrm{Li}^{-1}(n) - p_n$.

<!--
PLANTATION — non-monotonicity is the truth.

An early version of the conversational development asserted monotone
convergence to ratio 1. This was wrong: the multiplicative ratio
diverges in BOTH directions, oscillating with Riemann-zero-sum-scale
amplitude. The log-ratio is what tends to 0 in PNT-relative sense,
not the multiplicative ratio.

§5.7 records the honest table. The crossover at n ≈ 5 is the index-side
shadow of the cross-over of (π − Li) at small primes (around p₅ = 11,
where Li(11) ≈ 5.55 first exceeds π(11) = 5).
-->

---

## §6 Part C — Bohr–Mollerup uniqueness (grounded)

### 6.1 The convexity setup

**Lemma 6.1.** $\mathrm{Li}^{-1}: [0,\infty) \to [2,\infty)$ is strictly convex.

*Proof.* $\mathrm{Li}'(t) = 1/\log t > 0$ and $\mathrm{Li}''(t) = -1/(t\log^2 t) < 0$ on $(1,\infty)$, so $\mathrm{Li}$ is concave; its inverse $\mathrm{Li}^{-1}$ is convex. Explicitly, $(\mathrm{Li}^{-1})''(z) = \log(\mathrm{Li}^{-1}(z))/\mathrm{Li}^{-1}(z) > 0$. $\square$

**Corollary 6.2.** $\Delta(z) := \mathrm{Li}^{-1}(z+1) - \mathrm{Li}^{-1}(z)$ is strictly increasing in $z$. This is the smooth analogue of "$\log p_{n+1}$ is increasing in $n$" — the bare structural input the Bohr–Mollerup argument needs.

### 6.2 The theorem

**Theorem 6.3 (Bohr–Mollerup for the smooth primorial).** Let $f: [0,\infty) \to (0,\infty)$ satisfy

(BM1) $f(z+1) = e^{\Delta(z)}f(z)$ for all $z \ge 0$,

(BM2) $f(0) = e^2/(2\pi)$,

(BM3) $\log f$ is convex on $[0,\infty)$.

Then $f(z) = e^{\mathrm{Li}^{-1}(z)}/(2\pi) = \mathrm{pri}_{\mathrm{idx},\sharp}(z)$ for all $z \ge 0$.

### 6.3 Proof

Let $g := \log f$. By (BM1) and telescoping,
$$g(n+z) - g(z) \;=\; \sum_{k=0}^{n-1}\Delta(z+k) \;=\; \mathrm{Li}^{-1}(n+z) - \mathrm{Li}^{-1}(z),$$
for $z \ge 0, n \in \mathbb Z_{\ge 0}$. In particular $g(n) - g(0) = \mathrm{Li}^{-1}(n) - 2$.

Fix $z \in [0,1]$. By convexity of $g$ on $[n-1, n+1]$:
$$z\,\Delta(n-1) \;\le\; g(n+z) - g(n) \;\le\; z\,\Delta(n).$$
(Upper bound: chord above curve on $[n,n+1]$. Lower bound: left tangent slope $\ge \Delta(n-1)$.)

Substituting the telescoping identity:
$$z\Delta(n-1) \;\le\; \bigl[g(z) - g(0)\bigr] + \bigl[\mathrm{Li}^{-1}(n+z) - \mathrm{Li}^{-1}(n)\bigr] - \mathrm{Li}^{-1}(z) + 2 \;\le\; z\Delta(n).$$

Take $n \to \infty$. Two estimates:

**(a)** $z\Delta(n) - [\mathrm{Li}^{-1}(n+z) - \mathrm{Li}^{-1}(n)] = z\log(\mathrm{Li}^{-1}(\xi_1)) - z\log(\mathrm{Li}^{-1}(\xi_2))$ for some $\xi_1, \xi_2 \in (n, n+1)$ (MVT). The variation of $\log(\mathrm{Li}^{-1}(\cdot))$ on $[n, n+1]$ is $O(1/n)$ by the chain rule. So this difference $\to 0$.

**(b)** $z[\Delta(n) - \Delta(n-1)] = O(1/n)$ by the same chain rule, hence $\to 0$.

Therefore both bracketing bounds converge to the same limit:
$$g(z) - g(0) - \mathrm{Li}^{-1}(z) + 2 \;=\; 0,$$
i.e., $g(z) = g(0) + \mathrm{Li}^{-1}(z) - 2 = (2 - \log 2\pi) + \mathrm{Li}^{-1}(z) - 2 = \mathrm{Li}^{-1}(z) - \log(2\pi)$.

Hence $f(z) = e^{\mathrm{Li}^{-1}(z)}/(2\pi)$ on $[0,1]$, and by (BM1) on all $[0,\infty)$. $\square$

### 6.4 What this trophy says

Once the smooth multiplier $\Delta(z)$ is canonized as $\mathrm{Li}^{-1}(z+1) - \mathrm{Li}^{-1}(z)$ (forced by Riemann's explicit formula for $\pi$), log-convexity makes $\mathrm{pri}_{\mathrm{idx},\sharp}$ **unique** with no remaining freedom. The proof is the classical Bohr–Mollerup squeeze, with $\log z$ replaced by $\Delta(z)$, justified by Corollary 6.2. **Same shape as Bohr–Mollerup for $\Gamma$.**

**Theorem 6.3 is [P]** at the level of rigor of the standard Bohr–Mollerup theorem.

---

## §7 Part D — Wielandt analyticity (grounded)

### 7.1 The needed asymptotic — $\mathrm{Li}^{-1}$ on vertical strips

**Lemma 7.1.** As $|t|\to\infty$ with $\sigma \in [1,2]$ fixed,
$$\mathrm{Li}^{-1}(\sigma + it) \;=\; \bigl(\sigma\log|t| - \tfrac{\pi}{2}|t|\bigr) \;+\; i\bigl(t\log|t| + \tfrac{\pi}{2}\sigma\,\mathrm{sgn}(t)\bigr) \;+\; o(|t|).$$

*Proof sketch.* The asymptotic $\mathrm{Li}(z) = z/\log z\cdot(1 + O(1/\log z))$ holds uniformly in any closed sector avoiding the branch cut $[0,1]$. Inverting: $z = w\log z + o(z/\log z)$ for $\mathrm{Li}(z) = w$. To leading order $z \sim w\log w$. With $w = \sigma + it$ and $\log w = \log|t| + i\frac{\pi}{2}\mathrm{sgn}(t) + O(1/|t|)$ for large $|t|$, the result follows by expanding $(\sigma + it)(\log|t| + i\frac{\pi}{2}\mathrm{sgn}(t))$. $\square$

**Corollary 7.2 (Stirling-type decay).** On the strip $\{1\le\mathrm{Re}(z)\le 2\}$,
$$|\mathrm{pri}_{\mathrm{idx},\sharp}(\sigma + it)| \;=\; \frac{e^{\mathrm{Re}(\mathrm{Li}^{-1}(\sigma+it))}}{2\pi} \;\sim\; \frac{|t|^\sigma}{2\pi}\,e^{-\pi|t|/2}.$$

**This is the same exponential rate as Stirling for $\Gamma$**, with polynomial prefactor $|t|^\sigma$ vs $\Gamma$'s $|t|^{\sigma-1/2}$. Joint-on-disjoint branch of audit 3.3 realized: same rate, different prefactor.

### 7.2 The theorem

**Theorem 7.3 (Wielandt for the smooth primorial).** Let $H_+ := \{z \in \mathbb C : \mathrm{Re}(z) > 0\}$ and let $f: H_+ \to \mathbb C^*$ be holomorphic and nowhere zero, satisfying:

(W1) $f(z+1)/f(z) = \exp\bigl(\mathrm{Li}^{-1}(z+1) - \mathrm{Li}^{-1}(z)\bigr)$ for $z \in H_+$;

(W2) $\lim_{z\to 0^+}f(z) = e^2/(2\pi)$;

(W3) $f(z)\cdot e^{-\mathrm{Li}^{-1}(z)}$ is bounded on $\{1\le\mathrm{Re}(z)\le 2\}$.

Then $f(z) = e^{\mathrm{Li}^{-1}(z)}/(2\pi) = \mathrm{pri}_{\mathrm{idx},\sharp}(z)$ on $H_+$.

### 7.3 Proof

Let $g := \mathrm{pri}_{\mathrm{idx},\sharp}$. Both $f$ and $g$ are holomorphic, nowhere zero on $H_+$. Define
$$\phi(z) \;:=\; \log f(z) - \mathrm{Li}^{-1}(z) + \log(2\pi).$$

By (W1), $\phi(z+1) - \phi(z) = 0$; **$\phi$ is 1-periodic in $\mathrm{Re}(z)$**.

By (W3), $\mathrm{Re}\,\phi = \log|f\cdot e^{-\mathrm{Li}^{-1}}\cdot 2\pi|$ is bounded on the strip. Imaginary part of $\phi$ is bounded by a single branch choice. So $\phi$ is bounded on the strip $\{1\le\mathrm{Re}(z)\le 2\}$.

By 1-periodicity, $\phi$ extends to all of $\mathbb C$ and is bounded on every translate of the strip — hence bounded everywhere.

A bounded entire function is constant (Liouville). So $\phi \equiv c$ for some constant $c$.

By (W2): $\phi(0^+) = \log(e^2/(2\pi)) - 2 + \log(2\pi) = (2 - \log 2\pi) - 2 + \log 2\pi = 0$. So $c = 0$.

Hence $\log f(z) = \mathrm{Li}^{-1}(z) - \log(2\pi)$, i.e., $f = g$. $\square$

### 7.4 Comparison with Wielandt for $\Gamma$

Wielandt's classical theorem for $\Gamma$ asks for "$f$ bounded on $\{1\le\mathrm{Re}(z)\le 2\}$" because $\Gamma$ itself decays on that strip by Stirling, so "$f$ bounded" is equivalent to "$f$ tracks $\Gamma$ in growth rate."

For $\mathrm{pri}_{\mathrm{idx},\sharp}$, the canonical solution decays exponentially on strips at rate $\pi|t|/2$ (Corollary 7.2). The Wielandt-style condition is "$f$ tracks $\mathrm{pri}_{\mathrm{idx},\sharp}$ in growth rate," encoded as (W3): $f\cdot e^{-\mathrm{Li}^{-1}}$ bounded. The two conditions are structurally identical; the apparent asymmetry is only because $\Gamma$'s asymptotic was historically absorbed into "bounded."

**Theorem 7.3 is [P]** at the same rigor level as Wielandt's original theorem.

### 7.5 Open: Phragmén–Lindelöf cleanup

The boundedness condition (W3) presupposes the answer's growth rate. The natural improvement is a Phragmén–Lindelöf-style condition: **$f$ of finite exponential type at most $\pi/2$ in $|\mathrm{Im}(z)|$, uniformly on $H_+$**, combined with not vanishing. Heuristic: $\phi$ would then be 1-periodic and of exponential type, and Phragmén–Lindelöf forces it constant. Tightening this argument is **Trophy D2 (open)**, deferred to T33.2.

---

## §8 The divisor-lattice family

<!--
PLANTATION — the divisor family is what makes this a family paper.

§§4–7 build a single function. §8 builds the rest of the row. The
six members of the smooth primorial family are pri_idx, tilde-phi,
tilde-sigma, tilde-J_k for k ≥ 2, tilde-d = 2^z, and tilde-mu = e^{iπz}.
The first four have nontrivial asymptotic ratios with named constant
emissions; the last two are degenerate (tilde-d is linear in log, tilde-mu
is pure oscillation).

§8 closes Item 4 of yesterday's list (clean ζ(k) emissions for k ≥ 2)
and Item 1 with the corrected smooth-Mertens form.
-->

### 8.1 Smooth Euler totient $\widetilde\phi$

Define $\widetilde\phi$ by the recursion $\widetilde\phi(z+1) = (\mathrm{Li}^{-1}(z+1) - 1)\widetilde\phi(z)$, with boundary $\widetilde\phi(0)$ to be fixed by Mertens-matching:
$$\log\widetilde\phi(z) \;=\; \int_0^z\log\bigl(\mathrm{Li}^{-1}(t) - 1\bigr)dt \;+\; C_\phi. \qquad (8.1)$$

### 8.2 The smooth Mertens constant — corrected statement

**Theorem 8.1 (Smooth Mertens).** As $z \to \infty$,
$$\log\frac{\mathrm{pri}_{\mathrm{idx},\sharp}(z)}{\widetilde\phi(z)} \;=\; \log\log\mathrm{Li}^{-1}(z) \;+\; \widetilde\gamma_* \;+\; o(1),$$
where
$$\boxed{\;\widetilde\gamma_* \;:=\; C^* - \log\log 2, \qquad C^* := \sum_{k\ge 2}\frac{E_1((k-1)\log 2)}{k}.\;} \qquad (8.2)$$

*Proof.* By (8.1) and §5.3,
$$\log\frac{\mathrm{pri}_{\mathrm{idx},\sharp}}{\widetilde\phi} = \int_0^z\log\Bigl(\frac{\mathrm{Li}^{-1}(t)}{\mathrm{Li}^{-1}(t) - 1}\Bigr)dt + (\text{boundary})= -\int_0^z\log\Bigl(1 - \frac{1}{\mathrm{Li}^{-1}(t)}\Bigr)dt + (\text{boundary}).$$

Substituting $u = \mathrm{Li}^{-1}(t)$:
$$-\int_2^{\mathrm{Li}^{-1}(z)}\frac{\log(1 - 1/u)}{\log u}\,du \;=\; \sum_{k\ge 1}\frac{1}{k}\int_2^{\mathrm{Li}^{-1}(z)}\frac{du}{u^k\log u}.$$

The $k=1$ term gives $\log\log\mathrm{Li}^{-1}(z) - \log\log 2$. For $k\ge 2$, the integral converges as $z\to\infty$ to $E_1((k-1)\log 2)$ via the substitution $u = e^t$. Boundary constant $C_\phi$ is fixed to absorb the discrete-matching shift. $\square$

**Numerical evaluation.** From the Taylor series $E_1(x) = -\gamma - \log x + \sum_{n\ge 1}(-1)^{n+1}\frac{x^n}{n\cdot n!}$:

| $j$ | $E_1(j\log 2)$ | $E_1(j\log 2)/(j+1)$ |
|---|---|---|
| 1 | $0.378697$ | $0.189349$ |
| 2 | $0.118658$ | $0.039553$ |
| 3 | $0.043966$ | $0.010992$ |
| 4 | $0.017402$ | $0.003480$ |
| 5 | $0.007011$ | $0.001168$ |
| 6 | $0.0032$ | $0.000457$ |
| $\ge 7$ | tail | $\approx 0.00029$ |

$$C^* \;\approx\; 0.24527, \qquad \widetilde\gamma_* \;\approx\; 0.6119.$$

### 8.3 The bias from Euler's $\gamma$ is a Riemann-error integral

**Theorem 8.2.** The smoothing bias
$$\widetilde\gamma_* - \gamma \;=\; \int_2^\infty\frac{\pi(u) - \mathrm{Li}(u)}{u(u-1)}\,du \;\approx\; 0.0347. \qquad (8.3)$$

*Proof.* Compare the smooth integral $\int_2^x\log(1-1/u)/\log u\,du$ to the discrete sum $\sum_{p\le x}\log(1-1/p)$ via Abel summation. The difference is precisely
$$\sum_{p \le x}f(p) - \int_2^x f(u)\,d\mathrm{Li}(u) \;=\; -\int_2^x f'(u)[\pi(u) - \mathrm{Li}(u)]du + O(\text{boundary})$$
for $f(u) = \log(1-1/u)$, $f'(u) = 1/(u(u-1))$. Discrete Mertens gives $\gamma$; smooth integral gives $\widetilde\gamma_*$; their difference is the integral above. $\square$

**This is the structurally honest form of the trophy.** The smooth pri family does not emit $\gamma$ directly; it emits $\widetilde\gamma_*$, with the bias being a named Riemann-error integral. Both constants and their relationship are [P].

### 8.4 The clean partition: $\widetilde J_k/\mathrm{pri}^k$ emits $1/\zeta(k)$ exactly for $k \ge 2$

For $k \ge 1$, the smooth Jordan totient:
$$\log\widetilde J_k(z) := \int_0^z\log\bigl(\mathrm{Li}^{-1}(t)^k - 1\bigr)dt + C_{J_k}. \qquad (8.4)$$

**Theorem 8.3.** For $k \ge 2$,
$$\boxed{\;\lim_{z\to\infty}\frac{\widetilde J_k(z)}{\mathrm{pri}_{\mathrm{idx},\sharp}(z)^k} \;=\; \frac{1}{\zeta(k)}, \qquad \text{exactly, no bias.}\;} \qquad (8.5)$$

*Proof.* By (8.4) and (2.2),
$$\log\frac{\widetilde J_k(z)}{\mathrm{pri}_{\mathrm{idx},\sharp}(z)^k} = \int_0^z\log\bigl(1 - \mathrm{Li}^{-1}(t)^{-k}\bigr)dt + (\text{boundary}).$$
Every term in the series expansion $\log(1 - u^{-k}) = -\sum_{m\ge 1}u^{-mk}/m$ has $mk \ge 2$, so the integrals $\int du/(u^{mk}\log u)$ all converge absolutely. The boundary constant $C_{J_k}$ is fixed to match the discrete value $J_k(P_n)/P_n^k = \prod_{j\le n}(1 - p_j^{-k}) \to 1/\zeta(k)$ (absolutely convergent Euler product). $\square$

**No smoothing bias.** The reason is structural: the Euler product at $s = k \ge 2$ is absolutely convergent, so the smooth-vs-discrete discrepancy is itself a convergent integral $\int(\pi - \mathrm{Li})/u^k$ — but the value is absorbed into the boundary matching, leaving the asymptotic exact.

### 8.5 The clean partition principle

**Theorem 8.4 (Partition by Euler-product convergence).** The smooth primorial family ratios at $z\to\infty$ emit canonical constants according to the absolute/conditional convergence of the underlying Euler product:

- **Absolutely convergent ($s \ge 2$).** Clean emission of $\zeta(k)$, no bias. Applies to $\widetilde J_k/\mathrm{pri}^k$ for $k\ge 2$, $\widetilde\sigma_k/\mathrm{pri}^k$ for $k\ge 2$.
- **Conditionally convergent ($s = 1$, Mertens regime).** Shifted emission with bias term being a named Riemann-error integral. Applies to $\mathrm{pri}/\widetilde\phi$, $\widetilde\sigma/\mathrm{pri}$, $\widetilde\sigma/\widetilde\phi$.

This is the structural classification of the family's constant emissions.

### 8.6 The full table

| Smooth ratio | Asymptotic | Emitted constant | Bias |
|---|---|---|---|
| $\mathrm{pri}_{\mathrm{idx},\sharp}/\widetilde\phi$ | $e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z)$ | $\widetilde\gamma_* = 0.6119$ | $\widetilde\gamma_* - \gamma = \int_2^\infty(\pi-\mathrm{Li})/(u(u-1))\,du \approx 0.0347$ |
| $\widetilde\sigma/\mathrm{pri}_{\mathrm{idx},\sharp}$ | $\frac{6}{\pi^2}e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z)$ | $\widetilde\gamma_* - \log\zeta(2)$ | inherits Mertens bias |
| $\widetilde\sigma/\widetilde\phi$ | $\frac{6}{\pi^2}e^{2\widetilde\gamma_*}\log^2\mathrm{Li}^{-1}(z)$ | $2\widetilde\gamma_* - \log\zeta(2)$ | bias × 2 |
| $\widetilde J_2/\mathrm{pri}_{\mathrm{idx},\sharp}^2$ | $1/\zeta(2) = 6/\pi^2$ | $-\log\zeta(2)$ | **none** |
| $\widetilde J_3/\mathrm{pri}_{\mathrm{idx},\sharp}^3$ | $1/\zeta(3)$ | $-\log\zeta(3)$ | **none** |
| $\widetilde J_k/\mathrm{pri}_{\mathrm{idx},\sharp}^k$, any $k\ge 2$ | $1/\zeta(k)$ | $-\log\zeta(k)$ | **none** |

---

## §9 The destiny window — sieve structure of the smooth primorial

<!--
PLANTATION — the sieve insight closes the framework.

The destiny window is the Eratosthenes sieve rephrased as a property
of the smooth primorial: each primorial level defines a "window of
certainty" in which the next batch of primes is forced.

This isn't new arithmetic — it's the Eratosthenes sieve. But naming
the window makes the smooth pri family's structural role visible:
each smooth pri at level z parameterizes a window of size ≈ p_n²
in which the next batch of primes appears with density φ(P_n)/P_n.

The user named this "destiny written" — every prime's primality is
forced at the moment the previous primorial is built. The smooth
framework's role: track the WINDOW PARAMETERS (location, size,
density) as smooth functions of z.
-->

### 9.1 The destiny window theorem

**Theorem 9.1 (Destiny window).** For each $n \ge 1$, every prime $p$ with $p_n < p < p_{n+1}^2$ is determined to be prime by the primorial $P_n$ alone: $p$ is coprime to $P_n$ and has no prime divisor in the range $(p_n, p_{n+1}^2)$.

*Proof.* Coprime to $P_n$ ⟹ no prime divisor $\le p_n$. Less than $p_{n+1}^2$ ⟹ no prime divisor $\ge p_{n+1}$ (else the cofactor would also be $\ge p_{n+1}$, giving $p \ge p_{n+1}^2$). So $p$ has no prime divisors, hence is prime. $\square$

### 9.2 The destiny batch

The set of primes whose destiny is written at $P_n$ is
$$\mathcal B_n \;:=\; \{p \text{ prime} : p_n < p < p_{n+1}^2\}.$$
By Theorem 9.1, every $p \in \mathcal B_n$ has primality forced by $P_n$.

| $n$ | $p_n$ | $P_n$ | window $(p_n, p_{n+1}^2)$ | $|\mathcal B_n|$ |
|---|---|---|---|---|
| 1 | 2 | 2 | $(2, 9)$ | $3$ |
| 2 | 3 | 6 | $(3, 25)$ | $7$ |
| 3 | 5 | 30 | $(5, 49)$ | $12$ |
| 4 | 7 | 210 | $(7, 121)$ | $26$ |
| 5 | 11 | 2310 | $(11, 169)$ | $34$ |
| 6 | 13 | 30030 | $(13, 289)$ | $55$ |

### 9.3 The Mertens density estimate

**Theorem 9.2 (Batch-size approximation).** $|\mathcal B_n| = \frac{\phi(P_n)}{P_n}(p_{n+1}^2 - p_n) + O(1)$ for $n$ small; under RH the error grows as $O(p_n\log^2 p_n)$ on the window scale.

| $n$ | Mertens density $\phi(P_n)/P_n$ | window size $p_{n+1}^2 - p_n$ | predicted $|\mathcal B_n|$ | actual | error |
|---|---|---|---|---|---|
| 1 | $1/2$ | $7$ | $3.50$ | $3$ | $-0.50$ |
| 2 | $1/3$ | $22$ | $7.33$ | $7$ | $-0.33$ |
| 3 | $4/15$ | $44$ | $11.73$ | $12$ | $+0.27$ |
| 4 | $8/35$ | $114$ | $26.06$ | $26$ | $-0.06$ |
| 5 | $16/77$ | $158$ | $32.83$ | $34$ | $+1.17$ |
| 6 | $192/1001$ | $276$ | $52.95$ | $55$ | $+2.05$ |

**This is PNT/RH on a single primorial rung.** The Mertens-density-times-window-size formula matches the actual count to $\pm 1$ at small $n$ and slowly-growing oscillations at larger $n$ — exactly the size of the Riemann-zero-sum on the window scale.

### 9.4 The smooth destiny window

For smooth $z$, the destiny-window object is the smooth pair $(\widetilde{w}_z, \widetilde\rho_z)$:
- Window: $\widetilde{w}_z := (\mathrm{Li}^{-1}(z), \mathrm{Li}^{-1}(z+1)^2)$.
- Density: $\widetilde\rho_z := \widetilde\phi(z)/\mathrm{pri}_{\mathrm{idx},\sharp}(z)$.

Expected batch size:
$$\widetilde N(z) \;:=\; [\mathrm{Li}^{-1}(z+1)^2 - \mathrm{Li}^{-1}(z)] \cdot \widetilde\rho_z.$$

For large $z$: $\widetilde\rho_z \sim 1/(e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z))$ by Theorem 8.1, and $\mathrm{Li}^{-1}(z+1)^2 \sim (\mathrm{Li}^{-1}(z))^2 \cdot (1 + O(1/z))$, so
$$\widetilde N(z) \;\sim\; \frac{\mathrm{Li}^{-1}(z)^2}{e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z)}.$$

This is the smooth expected batch size at smooth ladder index $z$.

### 9.5 The structural picture

The destiny window theorem says: **each primorial defines a window of certainty in which the next batch of primes is forced.** The smooth pri family parameterizes the window data (location, size, density) as smooth functions of the continuous ladder index $z$. The actual batch size deviates from the smooth prediction by Riemann-zero-sized fluctuations.

This is the *structural role* of the smooth pri family in the Eratosthenes sieve: not to replace the discrete sieve, but to **parameterize the windows** as smooth objects, with the discrete batches being samples of the smooth prediction with bounded Riemann-error oscillations.

---

## §9A Addendum — the persistence barcode and the exactness question

<!--
PLANTATION — external-convention discipline (per directive 2026-05-28).
This addendum is written in standard mathematical language only. The
program-internal coinages stay here in comments:
  - "destiny written" (§9.1–9.5) = BIRTH in the barcode language below.
  - the window (p_n, p_{n+1}^2) is the certification window; its left edge
    is the promotion of p_n, its right edge the first shadow of p_{n+1}.
  - apex / GG-ledger / K-mark connections: none load-bearing here; the
    barcode is a statement about the Eratosthenes filtration of Z, full stop.
The barcode is the persistence diagram of the prime sequence over the
sieve filtration; "persistence barcode" is the standard TDA term and is
used descriptively (a multiset of birth–death intervals), with no claim
of an underlying homological persistence module.
-->

### 9A.1 The sieve filtration and the certification window

The sieve of Eratosthenes filters $\mathbb Z_{\ge 2}$ in stages: at stage $n$, remove the multiples of $p_1, \ldots, p_n$, leaving the integers coprime to $P_n = p_1\cdots p_n$. The following elementary fact controls the entire structure.

**Lemma 9A.1 (sieve horizon).** Fix $n$. In the interval $(p_{n+1}, p_{n+1}^2)$, the three conditions "coprime to $P_n$", "coprime to $P_{n+1}$", and "prime" coincide. In particular, recruiting $p_{n+1}$ at stage $n+1$ removes no element of this interval.

*Proof.* Let $m \in (p_{n+1}, p_{n+1}^2)$ be coprime to $P_n$. If $p_{n+1} \mid m$, write $m = p_{n+1}k$ with $2 \le k < p_{n+1}$ (since $p_{n+1} < m < p_{n+1}^2$). Then $k$ has a prime factor $\le k < p_{n+1}$, hence $\le p_n$, so that prime divides $m$ — contradicting coprimality to $P_n$. Thus $p_{n+1}\nmid m$, so $m$ is coprime to $P_{n+1}$. Finally, any composite coprime to $P_n$ has two prime factors $> p_n$, hence $\ge p_{n+1}$, so is $\ge p_{n+1}^2$; in the open interval $(p_{n+1}, p_{n+1}^2)$ no such composite exists, so $m$ is prime. $\square$

Lemma 9A.1 is the precise statement of the classical sieve bound: **a prime $p$ changes no primality verdict below $p^2$.** Its first sieving effect is its square. This is why $\sqrt{\cdot}$, not the integer itself, is the natural scale of certification.

### 9A.2 The barcode

A prime $q$ is *certified prime* at the earliest stage whose remaining sieve cannot mask it. By Lemma 9A.1 this is the stage at which the sieving primes reach $\sqrt q$. Define, on the filtration indexed by stage $n$:

$$\text{birth } b(q) := \pi(\sqrt q), \qquad \text{death } d(q) := \pi(q), \qquad \text{lifetime } \ell(q) := \pi(q) - \pi(\sqrt q). \qquad (9A.1)$$

Here *death* $= \pi(q)$ is the stage at which $q$ itself is recruited into the primorial (and so leaves the set of "not-yet-recruited certified primes"). The interval $[\,b(q), d(q)\,)$ is the bar of $q$; the multiset $\{[\,b(q),d(q)\,) : q \text{ prime}\}$ is the **persistence barcode of the sieve filtration**.

**Proposition 9A.2.** The set of primes certified-but-not-yet-recruited at stage $n$ is exactly the interval set $\{q : b(q) \le n < d(q)\} = \{q : p_n < q < p_{n+1}^2\}$ — the window of §9.2. A prime $q$ occupies exactly $\ell(q) = \pi(q) - \pi(\sqrt q)$ consecutive stages.

*Proof.* $b(q)\le n \iff \pi(\sqrt q)\le n \iff \sqrt q < p_{n+1} \iff q < p_{n+1}^2$; and $n < d(q) \iff n < \pi(q) \iff p_n < q$. $\square$

| $q$ | $b(q)=\pi(\sqrt q)$ | $d(q)=\pi(q)$ | $\ell(q)$ | stages occupied |
|---|---|---|---|---|
| 5 | 1 | 3 | 2 | 1–2 |
| 7 | 1 | 4 | 3 | 1–3 |
| 11 | 2 | 5 | 3 | 2–4 |
| 23 | 2 | 9 | 7 | 2–8 |
| 47 | 3 | 15 | 12 | 3–14 |
| 113 | 4 | 30 | 26 | 4–29 |

The bar of 47 opens at stage 3 (largest prime $\le\sqrt{47}\approx 6.9$ is $5 = p_3$) and closes at stage 15 ($\pi(47)=15$): twelve stages, matching $\ell(47)=15-3$.

### 9A.3 Birth and death rates

The death process is **rigid**: exactly one prime is recruited per stage, so the death rate is identically $1$. The birth process is **explosive**: the primes born at stage $n$ are those $q$ with $\pi(\sqrt q)=n$, i.e. $p_n^2 \le q < p_{n+1}^2$, numbering
$$\pi(p_{n+1}^2) - \pi(p_n^2) \;\sim\; \frac{p_{n+1}^2 - p_n^2}{2\log p_n} \;\sim\; p_n \;\sim\; n\log n$$
by the prime number theorem and the average gap $p_{n+1}-p_n \sim \log p_n$. Births outpace deaths by a factor $\sim p_n$, and the occupied population at stage $n$ is the window count $|\mathcal B_n| = \pi(p_{n+1}^2) - n \sim \tfrac12 n^2\log n$. The batches of §9.2 grow not because primes get denser — they thin — but because each certified prime waits $\sim\pi(q)$ stages for recruitment while $\sim p_n$ new ones are certified behind it.

### 9A.4 The birth-inclusive companion is the lcm

The exact prime-side primorial is $\mathrm{pri}_*(x) = \prod_{p\le x}p = e^{\vartheta(x)}$. The natural birth-inclusive companion records each prime *together with the powers that are its later shadows*. That object is classical:
$$\mathrm{lcm}(1, 2, \ldots, \lfloor x\rfloor) \;=\; \prod_{p^k \le x} p \;=\; e^{\psi(x)}, \qquad (9A.2)$$
the exponential of the second Chebyshev function $\psi(x) = \sum_{n\le x}\Lambda(n)$. Its logarithm exceeds $\vartheta$ by exactly the prime-power contribution:
$$\psi(x) - \vartheta(x) \;=\; \vartheta(\sqrt x) + \vartheta(x^{1/3}) + \cdots \;=\; \sum_{k\ge 2}\vartheta(x^{1/k}) \;\sim\; \sqrt x. \qquad (9A.3)$$

The right side of (9A.3) is, term by term, the running mass of *first shadows*: a prime $p$ casts its first shadow at $p^2$, so by scale $x$ the shadow-casting primes are those with $p\le\sqrt x$, contributing $\vartheta(\sqrt x)$. **The prime-power leakage of the explicit formula is the integrated birth measure of the barcode.**

**Observation 9A.3.** Both $\mathrm{pri}_*$ and $\mathrm{lcm}(1,\ldots,\lfloor\cdot\rfloor)$ have the *same* canonical smoothing $e^x/(2\pi)$, because $\psi$ and $\vartheta$ share the leading non-oscillatory part $x - \log(2\pi)$ (their explicit formulas differ only at the $\sqrt{\cdot}$ scale). The smooth primorial of §4 cannot distinguish the primorial from the lcm; their difference $e^{\psi-\vartheta}\approx e^{\sqrt x}$ lives entirely in the term discarded to form the smoothing. That discarded term is the same $\sqrt{\cdot}$-scale quantity whose size is governed by the Riemann hypothesis (Corollary 4.2). The birth structure of the barcode and the analytic location of the zeros are two faces of the one $\sqrt{\cdot}$-scale object.

### 9A.5 Is there an exact smooth primorial? The moment obstruction

The Gamma function matches the factorial *exactly* at integers — $\Gamma(n+1)=n!$ — not asymptotically. The smooth primorial of §5 matches the primorial only up to a Riemann-error factor (§5.7): $\mathrm{pri}_{\mathrm{idx},\sharp}(2)\approx 9.69$ while $P_2 = 6$. Is this a defect of the construction, or an obstruction? It is an obstruction, and it is computable.

**The source of $\Gamma$'s exactness.** $\Gamma$ is exact because the factorial is a *moment sequence*:
$$n! \;=\; \int_0^\infty t^n\, e^{-t}\,dt,$$
so $\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt$ interpolates exactly by construction. The exactness is a property of the integral representation, and integral representations of this Mellin type exist precisely for moment sequences.

**The moment criterion (pedagogical).** A sequence $(m_k)_{k\ge0}$ equals $\int t^k\,d\mu$ for some positive measure $\mu$ only if, for every choice of real coefficients $c_0,\ldots,c_N$,
$$\sum_{i,j} c_i c_j\, m_{i+j} \;=\; \int\Bigl(\sum_i c_i t^i\Bigr)^2 d\mu \;\ge\; 0,$$
i.e. the Hankel matrices $H_N := (m_{i+j})_{0\le i,j\le N}$ are positive semidefinite. Equivalently, all Hankel determinants $D_N := \det H_N$ are $\ge 0$. A single negative $D_N$ rules out *any* representing measure.

**The test for the primorial.** Take $m_k = P_k$, so $(P_k) = 1, 2, 6, 30, 210, 2310, 30030, \ldots$. The Hankel determinants:
$$D_0 = 1, \qquad D_1 = \begin{vmatrix}1&2\\2&6\end{vmatrix} = 2, \qquad D_2 = \begin{vmatrix}1&2&6\\2&6&30\\6&30&210\end{vmatrix} = 24,$$
$$D_3 = \begin{vmatrix}1&2&6&30\\2&6&30&210\\6&30&210&2310\\30&210&2310&30030\end{vmatrix} = -787680.$$

(The $D_3$ computation: row-reduce with the first row to clear column 1, leaving the $3\times3$ block $\bigl(\begin{smallmatrix}2&18&150\\18&174&2130\\150&2130&29130\end{smallmatrix}\bigr)$ with determinant $10{,}137{,}240 + 5{,}751{,}000 + 5{,}751{,}000 - 3{,}915{,}000 - 9{,}438{,}120 - 9{,}073{,}800 = -787{,}680$.)

**Theorem 9A.4 (no moment representation).** $D_3(P) = -787680 < 0$. Hence the primorial sequence $(P_n)$ is not a moment sequence: there is no positive measure $\mu$ with $P_n = \int t^n\,d\mu$. Consequently **no Mellin-type integral $\mathrm{pri}(z)=\int_0^\infty t^{z-1}\,d\mu(t)$ can interpolate the primorial**, and the $\Gamma$-route to an exact smooth primorial does not exist.

The factorial is the moment sequence of the exponential distribution, so $\Gamma$ is exact; the primorial's growth ratios are the primes $P_{n+1}/P_n = p_{n+1}$, too irregular to be the moment ratios of any measure — positivity first fails at $N=3$. **The completion-theoretic reading of this obstruction** — that a pure finite-prime (Euler-product) object cannot generate its own real-place completion, so the archimedean factor $\Gamma_\infty$ must be adjoined externally — **is developed in [T15 §12.3](T15-FiniteToArchimedeanCompletion-Draft1.md)**, whose Proposition 12.2 cites this theorem as the analytic proof that the real place is not a finite packet.

**Corollary 9A.5 (the interpolation trilemma).** For the primorial, the three properties *exact at integers*, *real-analytic*, and *canonical* cannot be obtained together by the two standard mechanisms:

- **analytic + canonical**, sacrificing exact: $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/(2\pi)$ of §5 (Bohr–Mollerup and Wielandt unique; matches only asymptotically).
- **exact + canonical**, sacrificing analytic: the log-linear interpolation $\mathrm{pri}_{\mathrm{lin}}(n+t)=P_n\,p_{n+1}^{\,t}$ (exact at integers, $C^0$, not differentiable at integers).
- **exact + analytic**, sacrificing canonical: entire interpolations of order $1$ exist by Newton-series / Carlson interpolation, but are non-unique (any multiple of $\sin\pi z$ may be added) and admit no Mellin representation (Theorem 9A.4).

The factorial escapes the trilemma because $(n!)$ is a moment sequence; the primorial does not, because $(P_n)$ is not (Theorem 9A.4). The deviation of the canonical analytic interpolation from exactness is, by Proposition 4.1, exactly the Riemann zero-sum $-\sum_\rho x^\rho/\rho$: **the gap between "asymptotic" and "exact" for the primorial is the same object that the Riemann hypothesis measures.**

<!--
PLANTATION — why this is the right answer to the user's question.
The user asked: "Γ is an exact match for factorial at integers; do we have
our exact pri matching the primorial?" The honest, rigorous answer is NO,
and the reason is a one-line computable fact: D_3(P) = -787680 < 0, so the
primorials are not a moment sequence and admit no Γ-style integral.

This is BETTER than a vague "it's only asymptotic." It pins the obstruction
to a specific determinant and explains the factorial/primorial dichotomy
structurally: factorial = moments of e^{-t} (measure exists, Γ exact);
primorial = moments of nothing (no measure, no exact integral). The prime
ratios are the obstruction, and they bite first at N=3.

Cross-check on the factorial side: (n!) = 1,1,2,6,24,... has Hankel
determinants 1,1,4,36,... all > 0 (classical; (n!) are the Stieltjes
moments of e^{-t} on [0,∞)). The contrast is exact and verifiable by hand.
-->

### 9A.6 Summary of the addendum

1. **Barcode.** Each prime $q$ has birth $\pi(\sqrt q)$, death $\pi(q)$, lifetime $\pi(q)-\pi(\sqrt q)$ in the sieve filtration; the window of §9.2 is the slice of bars open at stage $n$ (Prop. 9A.2). The sieve horizon (Lemma 9A.1) is the reason births occur at the $\sqrt{\cdot}$ scale.
2. **Demography.** Death rate $\equiv 1$; birth rate $\sim p_n$; population $\sim\tfrac12 n^2\log n$.
3. **lcm companion.** The birth-inclusive exact primorial is $\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)=e^{\psi(x)}$; it shares the smoothing $e^x/(2\pi)$ with $\mathrm{pri}_*=e^{\vartheta(x)}$ and differs by the $\sqrt{\cdot}$-scale prime-power leakage (Obs. 9A.3), which is the integrated birth measure.
4. **Exactness.** There is **no** exact Mellin-type smooth primorial: $(P_n)$ is not a moment sequence ($D_3=-787680<0$, Theorem 9A.4). The primorial cannot match the factorial's exact-analytic-canonical trifecta (Cor. 9A.5); the canonical analytic interpolation's deviation from exactness is the Riemann zero-sum.

---

## §10 The constant tower at starting primes

### 10.1 The starting-prime family is the translation orbit of $\mathrm{pri}$

For each prime $p$, the smooth primorial *started at $p$* is defined through its own logarithmic integral $\mathrm{Li}_p(x) := \int_p^x dt/\log t$ (so $\mathrm{Li}_p^{-1}(0) = p$):
$$\mathrm{Pri}_p(z) := \frac{e^{\mathrm{Li}_p^{-1}(z)}}{2\pi}.$$

**Theorem 10.0 (translation identity).** Since $\mathrm{Li}_p(x) = \mathrm{Li}(x) - \mathrm{Li}(p)$, one has $\mathrm{Li}_p^{-1}(z) = \mathrm{Li}^{-1}(z + \mathrm{Li}(p))$, hence
$$\boxed{\;\mathrm{Pri}_p(z) \;=\; \mathrm{pri}\bigl(z + \mathrm{Li}(p)\bigr).\;} \qquad (10.0)$$
**The starting-prime family is not a family of distinct functions** — it is the orbit of the single master curve $\mathrm{pri}$ under the translation semigroup generated by the marked abscissae $\{\mathrm{Li}(p) : p \text{ prime}\}$.

*Proof.* $\mathrm{Li}_p(x) = \int_p^x = \int_2^x - \int_2^p = \mathrm{Li}(x) - \mathrm{Li}(p)$; invert and exponentiate. $\square$

**The marked abscissae are unit-spaced.** $\mathrm{Li}(2) = 0$, and by PNT $\mathrm{Li}(p_{n+1}) - \mathrm{Li}(p_n) = \int_{p_n}^{p_{n+1}}dt/\log t \to 1$ (primes have $\mathrm{Li}$-density $1$). The origins sit at
$$\{\mathrm{Li}(p)\} = \{0,\ 1.118,\ 2.589,\ 3.712,\ 5.55,\ \ldots\},$$
approximately unit-spaced. Advancing the start by one prime translates the origin right by $\approx 1$ — exactly one step of the recursion $\mathrm{pri}(z+1) = e^{\Delta(z)}\mathrm{pri}(z)$. **Starting one prime later and multiplying in one more prime are the same operation**, read from the two ends of the ladder.

**Ground state ($p = 2$).** $\mathrm{Li}(2) = 0$, so $\mathrm{Pri}_2 = \mathrm{pri}$: the standard primorial is the unique member with zero translation. It corresponds to the *complete* $\zeta$; every later start corresponds to the incomplete Euler product $\prod_{q \ge p}(1 - q^{-s})^{-1}$, prime-thinned at the bottom (cf. §10.2, the $\log(2\pi)$ entry).

**Prime-side dual.** On the prime side the same shift is a vertical rescaling: $\mathrm{Pri}_{p,\sharp}(x) = e^{x}/(2\pi\,e^{\vartheta(p^-)})$ — e.g. start-at-$3$ gives $e^{x}/(4\pi)$ ("the odd primorial is half"). The index side (10.0) carries the translation; the prime side carries the division by the removed primorial $e^{\vartheta(p^-)}$.

### 10.2 Shift formulas: every constant is the master curve read at $\mathrm{Li}(p)$

By Theorem 10.0, each emitted constant of §8 at start $p$ is the master curve $\mathrm{pri}$ — or one of its log-derivatives — **evaluated at the marked abscissa $z = \mathrm{Li}(p)$**. The transformations below are then automatic.

**Boundary derivative (digamma at 0).** $(\mathrm{Li}_p^{-1})'(0) = (\mathrm{Li}^{-1})'(\mathrm{Li}(p)) = \log\bigl(\mathrm{Li}^{-1}(\mathrm{Li}(p))\bigr) = \log p$ — literally the slope of $\log\mathrm{pri}$ read at $z = \mathrm{Li}(p)$. The "$\log 2$" at start $2$ becomes $\log p$ at start $p$.

**Jordan-totient constants ($\zeta(k)$ family).** For $k\ge 2$,
$$R_k^{(p)} \;:=\; \prod_{q > p}(1 - q^{-k}) \;=\; \frac{1}{\zeta(k)\,\prod_{q\le p}(1 - q^{-k})}. \qquad (10.1)$$

Numerically for $k=2$:

| $p$ | $R_2^{(p)}\cdot\pi^2$ | rational form |
|---|---|---|
| 2 | $8$ | $8/\pi^2$ |
| 3 | $9$ | $9/\pi^2$ |
| 5 | $9.375$ | $75/(8\pi^2)$ |
| 7 | $9.570$ | $1225/(128\pi^2)$ |
| 11 | $9.650$ | $148225/(15360\pi^2)$ |
| $\to\infty$ | $\to \pi^2 \approx 9.870$ | $\to 1$ |

**The sequence $R_2^{(p)}\cdot\pi^2$ climbs from $8$ toward $\pi^2$.** Each captured prime trims a known rational factor; the destination is $1$ (no prime structure left in the residual product).

For $k=3$: sequence $R_3^{(p)}\cdot\zeta(3)$ climbs from $8/7$ toward $1$ (the destination $\zeta(3)\approx 1.202$).

**Smooth Mertens constant.** $\widetilde\gamma_*^{(p)} = C^*_p - \log\log p$ with $C^*_p := \sum_{k\ge 2} E_1((k-1)\log p)/k$.

Numerical:

| $p$ | $C^*_p$ | $-\log\log p$ | $\widetilde\gamma_*^{(p)}$ | discrete $\gamma - \log\prod^{-1}_{q\le p}(1{-}1/q)$ | bias |
|---|---|---|---|---|---|
| 2 | $0.2453$ | $+0.3666$ | $+0.612$ | $-0.116$ | $+0.728$ |
| 3 | $0.1080$ | $-0.0941$ | $+0.014$ | $-0.521$ | $+0.535$ |
| 5 | $0.0395$ | $-0.476$ | $-0.437$ | $-0.745$ | $+0.308$ |
| 7 | $0.0165$ | $-0.665$ | $-0.649$ | $-0.899$ | $+0.250$ |

**The smoothing bias decreases as we start later.** This is the structural signal that Li-density is a worse approximation at the bottom of the ladder than at the top — the bottom primes (2, 3, 5) sit far from Li-prescribed locations, and the bias measures exactly this.

**Explicit-formula constant ($\log 2\pi$).** This is the *only* constant of the family that does not shift. $\log(2\pi) = -\zeta'(0)/\zeta(0)$ lives on the archimedean side of $\zeta$, encoding the coupling between the prime-product side and the gamma-factor side; truncating the Euler product at $p$ doesn't change the archimedean coupling. Formally, $\zeta_{>p}(0) = \zeta(0)\prod_{q\le p}(1 - 1) = 0$, so $\zeta'/\zeta$ has no analogue and the constant disappears entirely from the truncated explicit formula.

### 10.3 The structural classification

**Theorem 10.1 (Constant tower classification).** Emitted constants of the smooth primorial family at starting prime $p$ fall into three classes:

1. **Telescoping-toward-1 (clean).** $R_k^{(p)}$ for $k \ge 2$. Each captured prime multiplies by an explicit rational Euler factor $\prod_{q\le p}(1 - q^{-k})^{-1}$. Destination: $1$ (asymptotically pure, no prime structure).
2. **Logarithmic-growth (ladder accumulators).** $\log p$, $\widetilde\gamma_*^{(p)}$, $\log\prod_{q\le p}(1-1/q)$. These grow (or decay to $-\infty$) logarithmically as $p$ increases, encoding the *cumulative captured Euler weight* rather than a fixed leftover.
3. **Archimedean-invariant (single representative).** $\log(2\pi)$. Does not have a starting-prime family — lives on the archimedean side of $\zeta$.

### 10.4 The dance

The dance the user observed: **every captured prime simultaneously closes a $R_k$-family factor (toward $1$) and opens a new Mertens-weight ledger entry (toward $\pm\infty$).** Both motions happen at every prime. The convergent constants ($\zeta(k)$ for $k\ge 2$) chase their absolute destination; the divergent ones ($\gamma$, $\log p$) chase their cumulative weight. Together they form the constant tower of the smooth primorial family, indexed by the prime ladder.

The "standard" analytic-NT constants ($\gamma$, $\zeta(2)$, $\zeta(3)$, $\log 2$, $\log(2\pi)$) are the **start-from-2 representatives** of these families — by Theorem 10.0, the readings of the master curve and its slopes at the origin $z = \mathrm{Li}(2) = 0$. The standard names hide the broader family structure; this paper makes it visible.

### 10.5 The whole real line and the left floor

Identity (10.0) extends the starting-prime parameter past the primes, in both directions. For $x \in (1, 2)$, $\mathrm{Li}(x) < 0$: "starting below $2$" is a *negative* translation, reading $\mathrm{pri}$ to the left of its origin. Pushing to the bottom, $\mathrm{Li}^{-1}(z) \to 1^+$ as $z \to -\infty$ (since $\mathrm{Li}(x) \to -\infty$ as $x \to 1^+$), so the master curve has a finite **left floor**:
$$\boxed{\;\mathrm{pri}(-\infty) \;=\; \frac{e^{1}}{2\pi} \;=\; \frac{e}{2\pi} \;\approx\; 0.43260.\;} \qquad (10.2)$$
This is the value "at the prime $1$" — the empty-product / multiplicative-unit threshold below all primes. The climb from the floor to the first prime is exactly a factor of $e$:
$$\frac{\mathrm{pri}(0)}{\mathrm{pri}(-\infty)} = \frac{e^{2}/(2\pi)}{e/(2\pi)} = e.$$
Thus $\mathrm{pri}: \mathbb{R} \to (e/2\pi,\ \infty)$ runs monotonically from the floor $e/(2\pi)$ at $z = -\infty$, through the marked primes $\mathrm{Li}(p)$, to $+\infty$. The starting-prime tower is the act of choosing which marked point to call the origin; the constant tower (§10.2–§10.4) is the readout of $\mathrm{pri}$ and its slopes along the marks.

---

## §11 Negative ledger — what doesn't translate

<!--
PLANTATION — paper 35 §3.6 demands the negatives be recorded.

This section closes out three open items from yesterday's list with
honest negatives plus one structural refinement.
-->

### 11.1 Smooth Möbius / Liouville

$\mu(P_n) = \lambda(P_n) = (-1)^n$. The smooth extension is the trivial
$$\widetilde\mu(z) = \widetilde\lambda(z) = e^{i\pi z}. \qquad (11.1)$$
At integer $z=n$, recovers $(-1)^n$ exactly. Dirichlet series $\sum (-1)^n/P_n^s$ is entire in $s$ but does not connect to standard $\zeta, L$-machinery via Möbius inversion the way $\sum\mu(n)/n^s = 1/\zeta(s)$ does. **Negative**: no new arithmetic emission from smooth Möbius.

### 11.2 Smooth Dirichlet characters

For non-principal $\chi$ mod $q$ with $q | P_n$: $\chi(P_n) = 0$ identically (since $p | P_n$ for some $p | q$). Smooth extension requires $\chi$ defined on non-integer arguments, which is not canonical — Dirichlet characters live on $\mathbb Z/q\mathbb Z$, not on $\mathbb R$. Forced extensions exist but are ad hoc.

The naive smoothing $\widetilde L_z(s, \chi)$ does not connect to the discrete $L(s, \chi)$ structure in a way that produces Dirichlet-zero data. **Negative**: smooth characters do not give clean new emissions beyond what conductor-block decomposition (§12.1) already provides.

### 11.3 RH attack via smooth primorial

The translation of the FE-cluster identity ([nueve.md:332](nueve.md:332)) into smooth pri-family language is structurally clean (§12.1) but does not separate on-line from off-line zeros. The decisive constraint is [nueve.md:387](nueve.md:387): *"pushing to higher Q in the cross-Gram, or chaining Hurwitz FE across primorials, recovers structural identities but no new analytic separation."* The smooth pri family is, definitionally, "going to higher Q smoothly" — inheriting the same envelope.

What the translation DOES give: a one-line statement of the K-antisymmetric F-vector constraints in smooth integral form (§12.1, Theorem 12.1). What it does NOT give: a new attack on RH.

**Negative**: smooth pri family does not open a new RH front. Recommendation: do not pursue further as an RH attack; treat the translation as structural restatement.

### 11.4 [A3'] Burgess-side BV bound

The primorial-indexed Bombieri–Vinogradov bound at rate $\theta_0 = 1 - C^*/n$ ([diez.md:207](diez.md:207)) lives at the per-prime Burgess saving level. Each prime contributes $\eta_p = (\log p)^{-c}$ with explicit $c > 0$. The smooth pri framework averages over primes via the Li density, which loses the per-prime cancellation. **Negative**: smooth pri cannot help close $C^* \leq 2.80$.

---

## §12 Implications for the program

### 12.1 The FE-cluster identity in smooth form

The Bures amplitude at $\mathbb Z/6 = \mathbb Z/P_2$ (nueve §6.2):
$$B_G(s) = 6^{-s}\sum_{r=1}^5\zeta(s, r/6)G_{rr} = Z(s) - \tfrac12 L(s,\chi_6) + \tfrac{2^{-s}}{4}L(s,\chi_3).$$

The pri-family generalization:
$$\widetilde B_G(s; z) \;:=\; \mathrm{pri}_{\mathrm{idx},\sharp}(z)^{-s}\int_0^1 G_z(u)\zeta(s, u)du, \qquad (12.1)$$
with conductor-block decomposition
$$\widetilde B_G(s; z) \;=\; A_0(s; z)\zeta(s) + \sum_{d \mid \lfloor\mathrm{pri}\rfloor, d>1}A_d(s; z)L(s, \chi_d). \qquad (12.2)$$

**Theorem 12.1 (Smooth K-antisymmetric constraint at zeros).** With $G_z$ satisfying $G_z(1-u) = -\overline{G_z(u)}$, the three discrete F-vector constraints of nueve §6.3 ($F_3 = 0$, $F_4 + F_2 = 0$, $F_5 + F_1 = 0$) become the single smooth integral identity
$$\int_0^{1/2}G_z(u)[\zeta(\rho, u) - \zeta(\rho, 1-u)]du \;=\; 0 \qquad (12.3)$$
at every nontrivial zero $\rho$ of $\zeta$.

**This is a clean structural restatement.** Same arithmetic content as the discrete constraints, one line instead of three. Worth folding into nueve §6.3 as a corollary.

### 12.2 N1 dimension refinement

The apex unitary $U_{P_n} \in U(P_n - 1)$ has conductor-block decomposition
$$U_{P_n} \;=\; \bigoplus_{d \mid P_n, d>1}U_d, \qquad U_d \in U(\phi(d)),$$
where $V_d$ has dimension $\phi(d)$ (the number of characters of exact conductor $d$).

**Smooth refinement.** The structurally interesting principal block is $U_{P_n} \in U(\phi(P_n))$, with smooth dimension $\widetilde\phi(z)$.

**Further refinement via smooth K-antisymmetry (§12.1).** The K-antisymmetric constraint (12.3) picks up only odd-character L-content. The structurally load-bearing sub-block of the apex unitary is therefore the **K-antisymmetric half** of the multiplicative-units block, of dimension $\widetilde\phi(z)/2$ where applicable.

**N1 Draft 2 actionable.** Promote N1's anchored object from $U_N \in U(N-1)$ to $U_{P_n,\text{principal}} \in U(\phi(P_n))$, with smooth dimension $\widetilde\phi(z)$. Where K-antisymmetry is operative, refine further to dimension $\widetilde\phi(z)/2$. Conjecture 4.1 of N1 (the determinant pattern) should be tested on the principal-block determinant, not the full mean-zero-block determinant.

### 12.3 GG-ledger gravity-localization rate

The GG-ledger claim: gravity localizes to $(\mathbb Z/P_n)^\times$ of dimension $\phi(P_n)$.

**Quantitative form via smooth pri family:**
$$\frac{\widetilde\phi(z)}{\mathrm{pri}_{\mathrm{idx},\sharp}(z)} \;\sim\; \frac{e^{-\widetilde\gamma_*}}{\log\mathrm{Li}^{-1}(z)} \;\sim\; \frac{e^{-\widetilde\gamma_*}}{\log p_n}. \qquad (12.4)$$

**Numerical localization fractions** $\phi(P_n)/P_n$:

| $n$ | $P_n$ | $\phi(P_n)$ | fraction |
|---|---|---|---|
| 1 | 2 | 1 | 50.00% |
| 2 | 6 | 2 | 33.33% |
| 3 | 30 | 8 | 26.67% |
| 4 | 210 | 48 | 22.86% |
| 5 | 2310 | 480 | 20.78% |
| 6 | 30030 | 5760 | 19.18% |
| 10 | $6.47\times 10^9$ | $1.06\times 10^9$ | 16.35% |
| 30 | $\sim 10^{50}$ | $\sim 1.05\times 10^{49}$ | $\sim 10.5\%$ |

The fraction decreases slowly toward 0, never reaches it. **This is the quantitative form of the GG-ledger localization claim.** Worth folding into [T32](32_one_functional_four_forces_v0.2%20(2).md) §2.5.6/QQ as a structural refinement.

This same fraction is the **dimensional boundary share** $\beta_{\dim}(N)=\varphi(N)/(N-1)$ of the Bekenstein companion [Paper 32.1 §7, §13.4](32.1_the_bekenstein_sphere.md) (the two agree up to the normalization $N/(N-1)\to1$): it is the $\beta=0$ "dimensional corner" of that paper's boundary-share curve $S(\beta)=1/\prod_p\!\bigl(1+1/((p-1)p^{\beta})\bigr)$. Paper 32.1's discrete Mertens decay $e^{-\gamma}/\log x$ is the discrete shadow of (12.4); the smooth constant $\widetilde\gamma_*$ of §8.2 is its canonical replacement, with the $\widetilde\gamma_*-\gamma$ gap (§8.3) the correction. The *non-vanishing* $\beta=1$ conductor corner of that curve is the Landau ratio $\zeta(6)/(\zeta(2)\zeta(3))$, whose order-2 / order-3 factors are precisely the §8.4 emissions $\widetilde J_k/\mathrm{pri}^k\to1/\zeta(k)$. So the GG-localization rate (this section), the smooth Mertens constant (§8.2), and the Jordan-totient emissions (§8.4) are the $\beta=0,\,\beta\!\to\!0\text{-rate},$ and $\beta=1$ readings of a single Euler-product curve shared with Paper 32.1.

### 12.4 Constants ledger with structural origins

Every analytic-NT constant the program touches now has a structural slot in the smooth pri family:

| Constant | Structural origin | Family |
|---|---|---|
| $\log(2\pi)$ | $-\zeta'(0)/\zeta(0)$, explicit-formula constant | archimedean-invariant (no family) |
| $\gamma$ | discrete Mertens at start 2 | start-2 representative of $\widetilde\gamma_*^{(p)}$ family |
| $\widetilde\gamma_* \approx 0.612$ | smooth Mertens at start 2 (with bias) | start-2 representative |
| $\zeta(k)$ for $k\ge 2$ | Euler-product at $s=k$, no bias | absolute representative of $R_k^{(p)}$ family |
| $\log 2$ | $(\mathrm{Li}^{-1})'(0)$, digamma at 0 | start-2 representative of $\log p$ family |
| $\log p$ for prime $p$ | $(\mathrm{Li}^{(p),-1})'(0)$ | starting-prime variants of $\log 2$ |

No more "where did $\gamma$ come from?" — it's the §8 emission. No more "what is $\zeta(2)$ doing here?" — it's the Item 4 closure at $k=2$. The constants are no longer ambient; they're emissions.

### 12.5 The Bekenstein conductor share is a smooth divisor-family ratio

The companion paper [32.1 (the Bekenstein sphere)](32.1_the_bekenstein_sphere.md) produces, as its holographic-boundary constant, the conductor-weighted unit share
$$\beta_{\mathrm{cond}}(N) \;=\; \frac{\varphi(N)\,N}{\sum_{c\mid N,\,c>1}\varphi(c)\,c} \;=\; \frac{\prod_{p\mid N}(p^2-p)}{\prod_{p\mid N}(p^2-p+1)\;-\;1},$$
the second equality by multiplicativity ($\sum_{c\mid N}\varphi(c)c=\prod_{p\mid N}(1+(p-1)p)$ for squarefree $N$). Both numerator and denominator are values of smooth divisor-family members (§2.5). The numerator's per-prime multiplier is $u^2-u=u(u-1)$, the member
$$\log\widetilde{P}_{2^-}(z) \;:=\; \int_0^z\log\bigl(\mathrm{Li}^{-1}(t)^2-\mathrm{Li}^{-1}(t)\bigr)\,dt + C_{2^-},$$
interpolating $\varphi(N)\,N=\prod p(p-1)$ (it is $\widetilde\phi\cdot\mathrm{pri}$ up to the boundary constant). The denominator's multiplier is the **sixth cyclotomic polynomial** $\Phi_6(u)=u^2-u+1$ — a new family member,
$$\boxed{\;\log\widetilde\Psi_6(z) \;:=\; \int_0^z\log\bigl(\mathrm{Li}^{-1}(t)^2-\mathrm{Li}^{-1}(t)+1\bigr)\,dt + C_{\Phi_6},\;}$$
the *smooth $\Phi_6$-totient*, interpolating $\prod_{p\mid N}\Phi_6(p)$. The canonical smooth interpolation of the Bekenstein boundary share is the ratio $\widetilde\beta_{\mathrm{cond}}(z):=\widetilde{P}_{2^-}(z)/(\widetilde\Psi_6(z)-1)$.

**Theorem 12.2 (Bekenstein constant = a clean $\Phi_6$ emission).** *As $z\to\infty$,*
$$\lim_{z\to\infty}\widetilde\beta_{\mathrm{cond}}(z) \;=\; \prod_p\frac{p^2-p}{p^2-p+1} \;=\; \prod_p\frac{1-p^{-2}}{1+p^{-3}} \;=\; \frac{\zeta(6)}{\zeta(2)\,\zeta(3)} \;=\; 0.5145101015\ldots,$$
*exactly, with no Mertens bias.* The per-factor is $1-1/(p^2-p+1)=1-O(p^{-2})$, so the product is **absolutely convergent**: by the partition principle (Theorem 8.4) this is a clean ($s\ge2$) emission, like $\widetilde J_k/\mathrm{pri}^k\to1/\zeta(k)$ and unlike the conditionally-convergent Mertens ratios $\mathrm{pri}/\widetilde\phi$. This is exactly Paper 32.1 Theorem 11.1 (the reciprocal of Landau's totient constant); the smooth-family reading *explains why it is bias-free* — it lives in the absolutely-convergent regime — and adjoins $\widetilde\Psi_6$ to the family as the $\Phi_6$-cyclotomic companion of the Jordan totients. **[P]** (cert `empirical/paper32_1_T33_beta_cond_bridge.py`: $\beta_{\mathrm{cond}}(P_k)=3/5,\,6/11,\,5040/9481,\,277200/526223$ exact; product $\to\zeta$-ratio to $2\times10^{-7}$ at the $2\times10^5$ prime cut).

**The weight curve, and where $\beta_\infty$ sits.** Paper 32.1 §13.3 deforms the conductor weight, $L(\beta):=\prod_p\bigl(1+1/((p-1)p^{\beta})\bigr)$, and finds the new constant $\beta_\infty=0.954352187581\ldots$ as the root of $L(\beta)=2$. Its two *integer-weight endpoints* are T33 tower constants:
$$L(1)=\prod_p\frac{p^2-p+1}{p^2-p}=\frac1{\lim\widetilde\beta_{\mathrm{cond}}}=\frac{\zeta(2)\zeta(3)}{\zeta(6)}\ (\text{Landau}),\qquad L(0)=\prod_p\frac{p}{p-1}=\frac1{\text{unit density}}=\infty,$$
the latter the reciprocal of the $\beta=0$ gravity-localization corner of §12.3. But $\beta_\infty$ is an **interior** root, strictly between $\beta=0$ and $\beta=1$, and is *not* a divisor-order (integer-$k$) emission nor a marked-abscissa reading: it does not reduce to the tower. So T33 **homes** the family — its $\beta=0$ and $\beta=1$ endpoints are the unit density and the $\Phi_6$ emission — and identifies $\beta_\infty$ as the $L=2$ level set of the weight-deformed $\Phi_6$ member, but does not contain it. This is consistent with Paper 32.1's own `mpmath.identify` returning nothing: $\beta_\infty$ is a genuinely new constant, classified here by *position* (the interior balance point of a T33-anchored family) rather than reduced to a catalog emission. **[P]**, negative-classification.

---

## §13 Ledger — every claim tiered

[P] proven, [A] structural pending named audit, [C] conjectural reduced.

| ID | Claim | Tier |
|---|---|---|
| A1 | $\log\mathrm{pri}_*(x) = \vartheta(x)$ (tautological) | [P] |
| A2 | $\mathrm{pri}_\sharp(x) = e^x/(2\pi)$ canonical via explicit formula | [P, mod Riemann–von Mangoldt] |
| A3 | $\log(\mathrm{pri}_*/\mathrm{pri}_\sharp) = -\sum_\rho x^\rho/\rho + O(\sqrt x)$ (Prop 4.1) | [P] |
| A4 | RH ⟺ $\log\mathrm{pri}_* - \log\mathrm{pri}_\sharp = O(\sqrt x\log^2 x)$ (Cor 4.2) | [P, RH-equivalent] |
| B1 | $P_n = \mathrm{pri}_*(p_n)$ (Lemma 5.1) | [P] |
| B2 | $\tilde p = \mathrm{Li}^{-1}$ canonical via explicit formula for $\pi$ | [P, mod Riemann] |
| B3 | $\mathrm{pri}_{\mathrm{idx},\sharp}(z) = e^{\mathrm{Li}^{-1}(z)}/(2\pi)$ (5.2) | [P] |
| B4 | Index↔prime duality diagrams (§5.4) | [P] |
| B5 | Boundary baseline $e^2/(2\pi) \ne 1$ honest record | [P] |
| B6 | RH ⟺ index-side bound (Cor 5.2) | [P, RH-equivalent] |
| C1 | $\mathrm{Li}^{-1}$ strictly convex (Lemma 6.1) | [P] |
| C2 | $\Delta(z)$ strictly increasing (Cor 6.2) | [P] |
| C3 | Bohr–Mollerup uniqueness (Theorem 6.3) | [P] |
| D1 | $\mathrm{Li}^{-1}$ asymptotic on vertical strips (Lemma 7.1) | [P] |
| D2 | Stirling-type decay $|t|^\sigma e^{-\pi|t|/2}$ (Cor 7.2) | [P] |
| D3 | Wielandt uniqueness (Theorem 7.3) | [P, with growth-tracking W3] |
| D4 | Phragmén–Lindelöf-style uniqueness | [C], reduced to single open task |
| E1 | $C^* = \sum_{k\ge 2}E_1((k-1)\log 2)/k \approx 0.2453$ (8.2) | [P] |
| E2 | $\widetilde\gamma_* = C^* - \log\log 2 \approx 0.6119$ (8.2) | [P] |
| E3 | Bias $\widetilde\gamma_* - \gamma = \int(\pi-\mathrm{Li})/(u(u-1))du \approx 0.0347$ (8.3) | [P] |
| E4 | $\widetilde J_k/\mathrm{pri}^k \to 1/\zeta(k)$ exact for $k\ge 2$ (8.5) | [P] |
| E5 | Partition by Euler-product convergence (Thm 8.4) | [P] |
| F1 | Destiny window theorem (9.1) | [P] |
| F2 | Mertens density × window-size = batch size + $O(1)$ (9.2) | [P, RH-conditional sharper form] |
| F3 | Smooth batch size $\widetilde N(z)$ formula (9.4) | [P] |
| F4 | Sieve-horizon lemma — $p$ removes nothing below $p^2$ (Lemma 9A.1) | [P] |
| F5 | Persistence barcode: birth $\pi(\sqrt q)$, death $\pi(q)$, lifetime $\pi(q)-\pi(\sqrt q)$ (9A.1, Prop 9A.2) | [P] |
| F6 | Death rate $\equiv 1$, birth rate $\sim p_n$, population $\sim\tfrac12 n^2\log n$ (§9A.3) | [P] |
| F7 | Birth-inclusive companion $=\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)=e^{\psi(x)}$; shares smoothing $e^x/(2\pi)$ with primorial; differ by $e^{\psi-\vartheta}\approx e^{\sqrt x}$ (9A.2–9A.3, Obs 9A.3) | [P] |
| F8 | $(P_n)$ not a moment sequence: $D_3 = -787680 < 0$ (Theorem 9A.4) | [P] |
| F9 | No exact Mellin-type smooth primorial; interpolation trilemma (Cor 9A.5) | [P] for moment route; [A] for trilemma framing |
| F10 | Deviation of canonical analytic interpolation from exactness = Riemann zero-sum (= A3 restated at integers) | [P] |
| G0 | Translation identity $\mathrm{Pri}_p(z) = \mathrm{pri}(z+\mathrm{Li}(p))$; starting-prime family = translation orbit of $\mathrm{pri}$; marked abscissae $\{\mathrm{Li}(p)\}$ unit-spaced (Theorem 10.0) | [P] |
| G0' | Left floor $\mathrm{pri}(-\infty) = e/(2\pi)\approx 0.4326$; $\mathrm{pri}(0)/\mathrm{pri}(-\infty)=e$ (10.2) | [P] |
| G1 | $R_k^{(p)}$ explicit Euler-factor formula (10.1) | [P] |
| G2 | $\widetilde\gamma_*^{(p)}$ numerical values, decreasing bias | [P] |
| G3 | $\log(2\pi)$ has no starting-prime family (archimedean invariant) | [P] |
| G4 | Three-class constant tower (Theorem 10.1) | [P] |
| H1 | Smooth Möbius is degenerate $e^{i\pi z}$ | [P], negative |
| H2 | Smooth characters do not extend canonically | [P], negative |
| H3 | Smooth pri does not separate on/off-line zeros (per nueve §6.6) | [P], negative |
| H4 | Smooth pri cannot improve $C^* \le 2.80$ in [A3'] | [P], negative |
| I1 | Smooth K-antisymmetric constraint (Theorem 12.1) | [P] |
| I2 | N1 dimension refinement to $\widetilde\phi(z)$ (or $\widetilde\phi(z)/2$ with K) | [A], reduced to N1 Draft 2 verification |
| I3 | GG-ledger localization rate (12.4) | [P, mod E2] |
| I4 | Constants ledger structural origins (§12.4) | [P, compilation] |
| I5 | Bekenstein conductor share = smooth $\Phi_6$ ratio $\widetilde\Psi_6/\widetilde P_{2^-}$; limit $\zeta(6)/(\zeta(2)\zeta(3))$ clean (abs. conv.) emission (Thm 12.2) | [P] |
| I6 | $\beta_\infty$ (32.1) is the interior $L=2$ root, not a tower emission; endpoints $L(0),L(1)$ are T33 constants (§12.5) | [P], negative-classification |
| J1 | T33.1 Hadamard product of $\mathrm{pri}_{\mathrm{idx},\sharp}$ | [C], deferred |
| J2 | T33.2 Phragmén–Lindelöf-style Wielandt | [C], deferred to T33.2 |
| J3 | T33.3 Mellin transform representation | [C], deferred to T33.3 |
| J4 | T33.4 Transfinite extensions (regularized $\mathrm{pri}(\omega)$) | [C], deferred to T33.4 |
| J5 | T33.5 Absolute base of constant tower | [C], deferred to T33.5 |

---

## §14 Safe / unsafe statements

Per Paper 35 §7 convention.

**Safe to assert (from this paper):**

- The smooth primorial $\mathrm{pri}_{\mathrm{idx},\sharp}(z) = e^{\mathrm{Li}^{-1}(z)}/(2\pi)$ exists, is canonical, and is unique under Bohr–Mollerup (Theorem 6.3) or Wielandt (Theorem 7.3) conditions.
- RH is equivalent to the smooth-vs-exact pri gap being $O(\sqrt x\log^2 x)$ (Corollaries 4.2 and 5.2).
- The smooth Mertens constant $\widetilde\gamma_*$ exists, differs from Euler's $\gamma$ by a named Riemann-error integral, and equals the smooth-pri-family emission $\log(\mathrm{pri}/\widetilde\phi)/\log\log\mathrm{Li}^{-1}$.
- The Jordan-totient ratios $\widetilde J_k/\mathrm{pri}^k$ emit $1/\zeta(k)$ exactly for $k \ge 2$, no smoothing bias.
- The destiny window theorem (9.1): every prime $p \in (p_n, p_{n+1}^2)$ has primality forced by $P_n$.
- The Mertens × window-size formula for batch size, accurate to $\pm 1$ at small $n$ (under PNT) and to $O(\sqrt{p_n}\log^2 p_n)$ asymptotically (under RH).
- The starting-prime constant tower: $\log p$, $\widetilde\gamma_*^{(p)}$, $R_k^{(p)}$ for various $p$ are explicit shifts of the standard constants.
- The starting-prime family is the translation orbit of a single master curve: $\mathrm{Pri}_p(z) = \mathrm{pri}(z + \mathrm{Li}(p))$ (Theorem 10.0), with primes as unit-spaced marked abscissae $\{\mathrm{Li}(p)\}$ and $\mathrm{Li}(2)=0$ the ground state.
- The master curve has a finite left floor $\mathrm{pri}(-\infty) = e/(2\pi) \approx 0.4326$, with $\mathrm{pri}(0)/\mathrm{pri}(-\infty) = e$.
- The smooth pri family inherits the "no on/off-line discriminator" envelope of finite-Q Hurwitz (nueve §6.6); the framework does not open a new RH attack.
- The smooth K-antisymmetric constraint (Theorem 12.1) is a clean one-line restatement of the discrete F-vector constraints.
- N1 should use $\widetilde\phi(z)$ as the smooth dimension of the apex unitary's principal block (Item 3 closure).
- The GG-ledger gravity-localization fraction is $\phi(P_n)/P_n \sim 1/(e^{\widetilde\gamma_*}\log p_n)$.
- The Bekenstein boundary constant of Paper 32.1 is the clean smooth-family emission $\widetilde\Psi_6/\widetilde{P}_{2^-}\to\zeta(6)/(\zeta(2)\zeta(3))$ (Theorem 12.2), the $\Phi_6$-cyclotomic companion of the Jordan-totient emissions; its sweet-spot constant $\beta_\infty$ is the interior $L=2$ root of the weight-deformed family and is *not* reducible to the tower.
- Every prime $q$ has a birth $\pi(\sqrt q)$ and death $\pi(q)$ in the sieve filtration; lifetime $\pi(q)-\pi(\sqrt q)$ (§9A.2).
- The birth-inclusive exact companion is the classical $\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)=e^{\psi(x)}$, sharing the smoothing $e^x/(2\pi)$ with the primorial.
- **There is no exact Mellin-type smooth primorial**: the primorials are not a moment sequence ($D_3 = -787680 < 0$, Theorem 9A.4). The factorial's exact $\Gamma$ rests on $(n!)$ being the moment sequence of $e^{-t}$; the primorial has no representing measure. The deviation of the canonical analytic interpolation from exactness is the Riemann zero-sum.

**Unsafe to assert (NOT delivered by this paper):**

- The smooth pri family closes RH, opens a new attack on RH, or improves any specific RH-related bound.
- The smooth Mertens constant $\widetilde\gamma_*$ equals $\gamma$ (it differs by $\approx 0.035$; the difference is the structural content).
- The smooth pri family produces canonical $L$-function emissions beyond what the conductor-block decomposition (§12.1) gives.
- The Phragmén–Lindelöf-style Wielandt theorem (open in §7.5).
- Closed form for $C^*$ beyond the explicit $E_1$-sum formula (numerically $\approx 0.2453$).
- Bounds on the Riemann-error integral $\widetilde\gamma_* - \gamma$ better than the unconditional $|\pi(u) - \mathrm{Li}(u)| = O(u\exp(-c\sqrt{\log u}))$.
- The existence of a $\Gamma$-quality interpolation of the primorial — exact at integers, real-analytic, and canonical simultaneously. Theorem 9A.4 rules out the moment route; the trilemma (Cor 9A.5) records that the two standard mechanisms each sacrifice one property. (An absolute impossibility theorem across *all* mechanisms is not claimed — only that the moment and smooth-recursion routes fail.)

---

## §15 Coda — what T34 will do

T34 (N1.5 in alternative numbering): apply T33 to N1.

**Concrete deliverables for T34:**

1. **Promote N1's anchored object** from $U_N \in U(N-1)$ to $U_{P_n,\text{principal}} \in U(\phi(P_n))$, with smooth dimension $\widetilde\phi(z)$ (Item 3 closure of this paper).
2. **Restate N1 Conjecture 4.1** ($\det U_N = \zeta_N^{f(N)}\epsilon(N)$) as a property of the principal-block determinant, not the full mean-zero-block determinant.
3. **Compute the principal-block determinants at $N = 5, 6, 7, 8$** using the refined N1 setup. Test whether the smooth $\widetilde\phi(z)$-scaling predicts the pattern.
4. **Smooth K-antisymmetric extension** (§12.1, Theorem 12.1): if applicable, refine the principal block further to its K-antisymmetric half $U(\widetilde\phi(z)/2)$.
5. **Integration with GG-ledger** (T32 §2.5.6/QQ refinement): fold the quantitative localization rate $1/(e^{\widetilde\gamma_*}\log p_n)$ into the gravity-on-units claim.

T34 is the immediate follow-up; T33.1–T33.5 (Hadamard, Phragmén–Lindelöf, Mellin, transfinite, absolute base) are longer-term deferred items.

---

## Acknowledgments

This paper synthesizes a sequence of structural results developed in conversation with Claude (Opus 4.7). The methodology overlay (Paper 35 grounded-paranoid-delusional) was applied consistently throughout. The explicit numerical computations (Newton iteration on $\mathrm{Li}^{-1}$, $E_1$ Taylor series for $C^*$, Mertens-density verification on the destiny windows) are reproducible by hand at the precision stated.

---

## References

- [N1-ApexUnitaries-Draft1.md](N1-ApexUnitaries-Draft1.md) — the N1 paper whose dimension claim is sharpened by §12.2.
- [T9-HelmertFourierTransferMatrix-Draft1.md](T9-HelmertFourierTransferMatrix-Draft1.md) — the apex unitary's structural definition.
- [T32-PhysicsMarriage-EpicClosure-Draft1.md](T32-PhysicsMarriage-EpicClosure-Draft1.md) — the program's anchor paper; §12.3 of T33 refines T32's GG-ledger §2.5.6/QQ.
- [nueve.md](nueve.md) — the RH program's cumulant-tower paper. §6.2 (FE-cluster identity at $\mathbb Z/6$) is restated in smooth form in §12.1 of T33. §6.6 (negative ledger) bounds T33's RH-attack contribution.
- [diez.md](diez.md) — the RH program's [A1'],[A2'],[A3'] technical companion. §11.4 of T33 records the negative on smooth pri improving $C^* \le 2.80$.
- [35_grounded_paranoid_delusional_methodology.md](35_grounded_paranoid_delusional_methodology.md) — the methodology overlay.
- [32.1_the_bekenstein_sphere.md](32.1_the_bekenstein_sphere.md) — the Bekenstein companion to T32. Its dimensional boundary share (§7, §13.4) is the discrete form of T33's GG-localization rate (§12.3); its conductor constant $\zeta(6)/(\zeta(2)\zeta(3))$ ratios T33's Jordan-totient emissions (§8.4); and its boundary-share curve $S(\beta)$ is the smooth interpolation target of §12.5 below.
- Riemann, B. (1859). *Über die Anzahl der Primzahlen unter einer gegebenen Größe.* Monatsberichte Berlin Akad.
- von Mangoldt, H. (1895). *Zu Riemanns Abhandlung "Über die Anzahl der Primzahlen unter einer gegebenen Größe".* J. Reine Angew. Math. **114**, 255–305.
- Mertens, F. (1874). *Ein Beitrag zur analytischen Zahlentheorie.* J. Reine Angew. Math. **78**, 46–62.
- Bohr, H., Mollerup, J. (1922). *Lærebog i Matematisk Analyse III.* Copenhagen.
- Wielandt, H. (1939). *Mathematische Werke*, Band 2, Berlin (posthumous publication of the $\Gamma$-uniqueness theorem).
- Remmert, R. (1998). *Classical Topics in Complex Function Theory*. Springer GTM **172**, §2.3.2 (Wielandt's theorem and proof).
- Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Oxford.

<!--
PLANTATION — closing note.

T33 settles four parts of a previously-empty framework slot, identifies
three negative results honestly, sharpens N1 by one structural claim,
and produces an explicit constant tower whose start-from-2 representatives
are the standard analytic-NT constants. The methodology kept the paper
honest about the smooth-vs-discrete bias (yesterday's strong γ-emission
claim turned out to be γ̃_* ≠ γ; the corrected statement is structurally
richer).

The framework's main remaining open task is T34: applying the dimension
refinement to N1 Draft 2 and computing principal-block determinants at
N ∈ {5, 6, 7, 8}. Everything in T33.1–T33.5 is deferred.

What T33 does NOT do: open a new RH attack. This is honest negative
recorded explicitly in §11.3 and §14. The framework gives clean
analytic continuation and constant emission; it does not give a new
RH front.
-->
