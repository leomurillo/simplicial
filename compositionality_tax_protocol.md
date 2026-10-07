# The Compositionality Tax — A Falsifiable Measuring Stick for Interpretability Faithfulness

*Protocol + pre-registration, 2026-06-25.* Tier-A prediction (pure ML; no firewall involved).
Turns the D-IV faithfulness obstruction into an *instrument*. Synthetic core certified:
`empirical_leverage/compositionality_tax.py` (8/8 GREEN). LLM test specified below — GCP/torch,
not run locally (hardware constraint).

## The prediction (precise, falsifiable)

> **The minimum probe order needed to faithfully read a behavior equals the cumulant order of its
> interactions, which equals its compositional depth. Faithfulness is a phase boundary, not a
> gradient: an order-$m$ probe is faithful to an order-$k$ behavior iff $m\ge k$, and is *exactly*
> blind below $k$.**

Consequence — the **compositionality tax** $\tau$: the order at which a readout saturates is a
*measured number* equal to the behavior's compositional depth. "How compositional is this circuit?"
becomes answerable with a ruler.

## Synthetic core (certified, the deterministic gate)

For true order $k$, the $k$-th finite difference $\Delta^k=[(-1)^{k-j}\binom{k}{j}]$ is the null
vector of the order-$(k{-}1)$ moment map, so $p=\text{base}+\varepsilon\Delta^k$ and
$q=\text{base}-\varepsilon\Delta^k$ are **matched through order $k{-}1$ and differ at order $k$**.
An order-$m$ probe (moments up to $m$) distinguishes them iff $m\ge k$. The faithfulness matrix is a
clean lower-triangular **step**:

```
        m=0  1  2  3  4  5
   k=2:   0  0  1  1  1  1
   k=3:   0  0  0  1  1  1
   k=4:   0  0  0  0  1  1
   k=5:   0  0  0  0  0  1
```

Discrepancy is **exactly zero** below $k$ and jumps at $k$ (a discontinuity, not a ramp);
$\tau(k)=k$ for all tested $k$. This is the faithfulness obstruction (order-2 blind to order-3,
D-IV) generalized to every order, and reframed as a measuring stick.

## The LLM test (GCP/torch — specified, not yet run)

**Operationalize "order-$m$ probe" as a degree-$m$ polynomial-kernel readout.** The degree-$m$
polynomial kernel $K_m(x,y)=(1+x\!\cdot\!y)^m$ captures activation interactions up to order $m$
exactly; "order-$m$ probe" = kernel ridge/logistic on $K_m$. (Linear probe = $m{=}1$; SAE-style
linear dictionary and any Gram/covariance method $\approx m{=}2$.)

**Design.**
1. Model: a small open transformer (Pythia / GPT-2 / Llama-class), activations at a fixed layer.
2. Behaviors of *controlled compositional order* $k$: $k$-way feature conjunctions (e.g. token is
   {noun} ∧ {plural} ∧ {subject} for $k{=}3$), or $k$-hop lookups. Build, for each $k$, a
   **matched-pair prompt set** whose activation statistics agree through order $k{-}1$ and differ at
   order $k$ (the activation-space analogue of $\Delta^k$).
3. For $m=1,2,3,4$: train the degree-$m$ kernel probe; measure faithfulness (accuracy at recovering
   the behavior / distinguishing the matched pair) on held-out prompts.
4. Read off $\tau$ = the smallest $m$ at which faithfulness saturates.

**Predicted signature:** for each behavior of true order $k$, faithfulness is a **single sharp
jump** from chance to saturated at $m=k$ (a step), and $\tau=k$.

## Pre-registered falsifier (symmetric)

- **FALSIFIED:** faithfulness rises *smoothly* with $m$ (partial faithfulness at $m=k-1$ on a
  genuinely order-$k$ behavior) — a gradient, not a step; **or** $\tau\neq k$ for controlled-order
  behaviors; **or** an $m{=}2$ probe faithfully reads a verified order-$\ge3$ conjunction.
- **CONFIRMED:** a single sharp step at $m=k$ with $\tau=k$, robust across layers and behaviors.
- **Discriminating variable (named in advance):** the *shape* of faithfulness vs $m$ — step
  (confirms) vs ramp (falsifies). We commit to reading the shape, not just a correlation.

## Why this is the lead claim

It converts the program's grandest interpretive thread — "interpretability is an order-2 readout of
an order-$\ge3$ world" — into (i) a *theorem* (the phase boundary, certified synthetically), (ii) a
*measuring stick* ($\tau$, a number any lab can compute), and (iii) a *runnable falsifier* on real
models. It connects directly to live anchors: DCD's 87% mixed-faithfulness (= behaviors with
$\tau>2$), the vec2vec order-2 floor ($\tau=2$ tasks solvable, $\tau>2$ not), SAEs as $m{=}2$
instruments (faithful only where $\tau\le2$), and the κ-audit's mid-depth localization (where
high-$\tau$ behaviors concentrate).

## Honest tiers

- [P] the synthetic phase boundary and $\tau(k)=k$ (certified, exact).
- [A] the operationalization (degree-$m$ kernel = order-$m$ probe; matched-pair activation construction).
- [open] the LLM result — *the* thing to run on GCP; the prediction is on record before the data.

## Files
- `empirical_leverage/compositionality_tax.py` (8/8 GREEN, synthetic gate).
- To build (GCP): `compositionality_tax_llm.py` (degree-$m$ kernel probes on activations; torch,
  GCP-only). Anchors: `D4_meaning_faithfulness.md`, FaithfulnessObstruction.md, the κ-audit,
  DCD, vec2vec, LeJEPA. Folds into the lead paper "The Faithfulness Ceiling."
