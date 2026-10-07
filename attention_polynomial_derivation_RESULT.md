# Deriving the Minimal Attention Polynomial from Interaction Structure

*Result note, 2026-06-26.* The one-week theory probe proposed after the poly-attention literature
sweep. Tests whether the program's interaction-structure tools supply the **selection principle**
both higher-order-attention papers leave open ("choose the attention polynomial h based on the data"
— with no rule for *which* h). Cert: `empirical_leverage/attention_polynomial_derivation.py`
(19/19, exact numpy, no torch). Anchor: poly-attention, arXiv:2602.02422 (ICLR 2026); 2-simplicial,
arXiv:2507.02754.

## The principle (honest two-step)

Given a task, decompose its input→output map by functional-ANOVA (Walsh–Hadamard). Then:

- **Step 1 — ANOVA *shape* → cost class.**
  - Spectrum **spread** (lower-order mass present) ⟹ **decomposable** ⟹ tree-attention, O(n²).
  - Mass **irreducible at order k** (concentrated at the top, ~0 below) ⟹ **irreducible** ⟹ Strassen
    cycle O(n^ω) / k-tensor O(nᵏ).
- **Step 2 — factor graph → the specific polynomial.**
  - Markov-chain / path factorization ⟹ path h_r = Σ xᵢxᵢ₊₁ (tree).
  - Symmetric irreducible k-relation ⟹ k-clique (Strassen) or k-tensor.

ANOVA alone gives the dichotomy + cost; the *exact* polynomial needs the factor graph.

## What is exact and verified

- **Irreducible family (Match-k / modular sum / parity-k):** ANOVA mass is *exactly and only* at
  order k, **zero order-2** (k=2,3,4,5). No pairwise/tree decomposition exists. ⟹ Match3 / (a+b+c) mod p
  derive to the **triangle** x₁x₂+x₂x₃+x₃x₁ (Strassen, one cycle, O(n^ω)) or x₁x₂x₃ (3-tensor, O(n³)),
  **not** a tree, **not** self-attention.
- **Function composition:** ANOVA spectrum is **spread** (order-1 0.5, order-2 0.25, order-3 0.25 for
  2-fold; spreads to order-4 for 3-fold) — order-2 mass present ⟹ decomposable. The factor graph is the
  **path** x–f₁–…–f_r (composition factors through each intermediate yᵢ = a Markov chain), giving
  h_r = Σ xᵢxᵢ₊₁ (tree) ⟹ O(n²), for all r.
- **Decisive contrast:** 3-fold composition and (a+b+c) mod p are *both nominally order-3*, but the
  composition spectrum is spread (order-2 mass > 0) while the modular sum is concentrated (order-2 mass
  = 0). **Same order, opposite shape ⟹ opposite minimal polynomial and cost class.** This is the crux:
  what separates cheap-high-order from expensive-high-order is *factorization*, not order.

## Cross-check vs the poly-attention table — reproduces every entry

| task | derived h | cost | paper |
|---|---|---|---|
| (a+b) mod p | x₁x₂ | n² | self-attn ✓ |
| 2-fold composition | x₁x₂+x₂x₃ (tree) | n² | h₂, tree ✓ |
| r-fold composition | Σ xᵢxᵢ₊₁ (tree) | n² | h_r, tree, all r ✓ |
| Match3 / (a+b+c) mod p | triangle (cycle) | n^ω | Strassen / 3-tensor ✓ |
| r-term modular sum | r-clique / r-tensor | superquad. | Match-r / t-tensor ✓ |

## Honest limitations (one caught by the computation)

- **Overclaim corrected:** I asserted the order-2 ANOVA *graph* of composition is a tree. The
  computation returned `forest=False` — the bit/multiplexer encoding manufactures order-2 cycles. So
  the exact tree is **not** read off the bit-level ANOVA graph; it comes from the role-level factor
  graph. The ANOVA's solid contribution is the decomposable-vs-irreducible *call*, not the graph shape.
- **At the role level, composition is also order-r** (all roles jointly needed) — same nominal order as
  Match. The true separator is the **Markov factorization**, which the bit-level spread detects as a
  proxy. So "ANOVA order" alone is insufficient; "ANOVA *shape* + factorization" is the working signal.
- **Validated by reproduction, not yet by prediction.** It recovers the paper's known assignments. The
  real test is applying it to a task the paper did *not* analyze and predicting h before checking. That
  is the next step if this is pursued.

## Verdict

The probe **held**: the program's interaction-structure analysis (ANOVA shape + factor graph) supplies
a working version of the selection principle the papers leave open, and reproduces their full
task→polynomial→cost table — with the honest refinement that ANOVA gives the *cost class* and the factor
graph gives the *specific polynomial*. It **passes the forced-analogy kill criterion**: this is a real
computed correspondence (the ANOVA *is* the interaction structure), not the cumulant tower forced onto
something unrelated. It is theory-only, exact, and uses the program's own tools. It is **modest** —
organizing/deriving known results with a principle — until it predicts a novel task's h. Files:
`empirical_leverage/attention_polynomial_derivation.py`. Companion to
[[reference_higher_order_attention_2simplicial]].

---

## Phase 1 — predicting a NOVEL task (2026-06-26)

`empirical_leverage/phase1_novel_task_prediction.py` (8/8). Moves the principle from *reproduces* to
*predicts*, on a matched pair the poly-attention paper does **not** tabulate:

- **A — chain:** out = f₃(f₂(f₁(x))). Computation DAG = a path (no recombination).
- **B — diamond:** out = g(f₁(x), f₂(x)). DAG = a collider (x branches to f₁,f₂; they recombine at g).

**Sharpened principle.** ANOVA first rules out the irreducible (parity/Match) branch — here both A and B
are *decomposable* (spread spectra), so ANOVA alone can't separate them. Among decomposable tasks, the
cost class is governed by the **treewidth of the moral graph of the computation DAG**: treewidth-1
(tree) → O(n²) tree-attention; treewidth-2 (one cycle) → O(n^ω) Strassen; higher → worse. A collider
(recombination) *marries co-parents*, which is what can raise treewidth.

**Pre-registered prediction (made from the principle, then checked vs the paper's cost theorem):**
- A (chain): moral graph = path = **treewidth 1** → **O(n²)** [cheap].
- B (diamond): moral graph = K₄−e (x–f₁, x–f₂, f₁–f₂, f₁–g, f₂–g) = **treewidth 2, a cycle** →
  **O(n^ω)** [expensive].
- **Non-obvious claim:** branching-with-recombination is strictly harder than chaining, *same token
  count* — the recombination collider is the cause. Verified consistent with the paper's tree→n² /
  cycle→n^ω characterization.

**Honest scope of Phase 1.** This establishes the *prediction* and shows its derived h's cost class is
*consistent with* the paper's complexity theorem. It does **not** yet prove the diamond *requires* the
cycle (i.e., that no tree-attention solves it) — that expressibility lower bound is **Phase 2**
(constructive: build the cycle-h that solves B, show a tree-h provably cannot). So: *prediction made +
cost-class verified*, not yet *expressibility-confirmed*. The kill criterion did not trip.

---

## Phase 2 — constructive confirmation **in the exact poly-attention model** (2026-06-26)

`empirical_leverage/phase2_constructive_separation.py` (12/12, exact numpy, no torch). Built the
**literal** poly-attention forward pass of arXiv:2602.02422 (Def 2.4) with the paper's own
Kozachinskiy **sum-of-squares** construction: explicit input features `X`, explicit query-key maps
`W_Q^(j)`, so each polynomial **edge** `xₐxᵦ` realizes `⟨Q^a,Q^b⟩ = −(equality residual)²` (verified:
all four cycle-edge inner products vanish at the correct tuple; a mismatched g-token is strictly
penalized). The softmax then concentrates on the unique all-residuals-zero tuple = the answer. This is
faithful poly-attention, not a bespoke scorer.

**Upper bounds (constructed + verified).**
- **Chain** `f₂(f₁(x))` solved by the **path** polynomial `h₂ = x₁x₂+x₂x₃` — *exhaustively* over all
  32 instances at n=2.
- **Diamond** `g(f₁(x),f₂(x))` solved by the **4-cycle** polynomial `x₁x₂+x₁x₃+x₂x₄+x₃x₄` —
  *exhaustively* over all 512 instances at n=2, plus 150 random n=3 instances. (Query pins both
  f-tokens via 1-2, 1-3; the g-token must match *both* lookups via 2-4, 3-4 → 4-cycle.)

**Lower-bound teeth (the part Phase 1 lacked) — edge-minimality, exact.** The 4-cycle is
**edge-minimal**: dropping *any* one edge yields a **witnessed indistinguishability** — two diamond
instances with *different correct answers* on which the reduced head returns the *identical* output
(so it provably errs on ≥1). Mechanism, verified per edge by the forward pass:
- drop 2-4 / 3-4 (readout side): g's a/b coordinate goes unmatched → vary f₁(x)/f₂(x) → same output.
- drop 1-2 / 1-3 (pinning side): the slot then reads only the f-*value* (position-independent), so two
  instances with the **same value-multiset but permuted positions** are identical to the head.
Since a forest on 4 vertices has **≤3 edges**, it cannot contain all four → **no tree-attention solves
the diamond** in the single-head, degree-2, per-table model. The information-flow reason is general:
slot 4 must be adjacent to slots 2 and 3 (to see both f₁(x), f₂(x)), which must each be adjacent to
slot 1 (to be pinned to x) — exactly the four cycle edges.

**The Phase-1 correction (the most valuable output).** Phase 1 invoked *treewidth of the moral graph of
the computation DAG*. That is **not** the paper's cost model — the paper's cost is a **cycle in the
attention-polynomial's variable graph**. They *coincide* for the diamond, but the right object is the
polynomial graph, and the separation is **conditional on the encoding**: the **escape hatch** (verified
on all 512 n=2 instances) — pre-merge `F(x)=(f₁(x),f₂(x)) : [n]→[n²]` and the diamond becomes 2-fold
composition `g(F(x))`, solved by the **path** polynomial. The cycle is traded for an **n→n² alphabet
blowup** — precisely the graphical-models moralization/treewidth tradeoff (merging the collider's
co-parents into one product variable), now correctly located in the attention cost model.

**Honest scope.** The exact lower bound here is for **single-head, degree-2, per-table** encodings. The
*fully general* lower bound (arbitrary embedding dim, multiple heads) is the paper's
communication-complexity regime (myopic pointer jumping, `apx_func-comp` Lem cc-lb) — **cited, not
re-derived**. Within the stated model the result is exact and exhaustive.

**Verdict.** Phase 2 turns the prediction from *cost-class consistent* into *constructively confirmed
with teeth*: the predicted polynomials provably solve their tasks, the cycle is provably necessary
(edge-minimal, no forest suffices), **and** the framework self-corrected — the chain/diamond separation
is real but encoding-conditional, with the product-alphabet flattening as the exact escape. Theory-only,
exact, torch-free; reproduces and extends the paper's own constructions.
