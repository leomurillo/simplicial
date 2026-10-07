import Mathlib

set_option linter.style.header false

/-!
# The RH=true surface: candidate statements with an edge to `RiemannHypothesis`

A first pass at the graph described in the project notes. Every `sorry` below is a
*deliberate* gap: it marks one edge of the graph that is not yet machine-checked.

Edge types, recorded in the docstrings:
  [PROVED]      kernel-checked here or in Mathlib
  [CLAIMED]     a published human proof exists; not yet formalised
  [CONJECTURED] a route from this project; no proof

Terminal node (already in Mathlib):

  RiemannHypothesis : ∀ (s : ℂ), riemannZeta s = 0 →
      (¬∃ n : ℕ, s = -2 * (n + 1)) → s ≠ 1 → s.re = 1 / 2

Observation that motivates the file: `RiemannHypothesis` currently has **degree
zero** in the proved graph — Mathlib contains no theorem of the form
`P ↔ RiemannHypothesis`. Until one exists, RH cannot be approached from the
backward side at all. Giving it a single proved edge is the first job.
-/

open Filter Topology
open scoped ArithmeticFunction Chebyshev

namespace RHGraph

/-! ## Node 0 — the target -/

/-- Restating Mathlib's `RiemannHypothesis` so the file is self-describing. -/
abbrev RH : Prop := RiemannHypothesis

/-! ## Node 1 — Lagarias' criterion  (external, elementary statement)

Lagarias (2002): RH ⟺ σ(n) ≤ H_n + exp(H_n)·log(H_n) for all n ≥ 1.

Chosen as the *first* target for the graph rather than for our machinery: every
symbol is already in Mathlib, and it avoids the thin Euler–Mascheroni API that
Robin's γ-form would need. It contributes nothing to the zeta apparatus — the
point is that it is the cheapest way to give RH a proved neighbour. -/

/-- The Lagarias inequality, as a proposition about all `n ≥ 1`. -/
def LagariasIneq : Prop :=
  ∀ n : ℕ, 1 ≤ n →
    ((ArithmeticFunction.sigma 1 n : ℕ) : ℝ) ≤ (harmonic n : ℝ) + Real.exp (harmonic n) * Real.log (harmonic n)

/-- [CLAIMED] Lagarias 2002. The easy direction of the equivalence. -/
theorem RH_of_lagarias : LagariasIneq → RH := by
  sorry

/-- [CLAIMED] Lagarias 2002, converse direction. -/
theorem lagarias_of_RH : RH → LagariasIneq := by
  sorry

/-! ## Node 2 — Li's criterion  (external; our #19 realises the tower)

Li (1997), Bombieri–Lagarias (1999): RH ⟺ λ_n ≥ 0 for all n ≥ 1, where

  λ_n = (1/(n-1)!) · dⁿ/dsⁿ [ s^(n-1) · log ξ(s) ] |_(s=1).

The derivative form is used rather than the zero-sum Σ_ρ [1 - (1-1/ρ)ⁿ] because the
latter needs a conditionally convergent sum over a zero multiset, for which there is
no Mathlib API. NOTE (revised): `Mathlib/NumberTheory/LSeries/ZetaZeros.lean` does
supply `riemannZetaZeros : Set ℂ` with closedness, discreteness and finiteness on
compacts, so the zero-sum form is more reachable than first assumed and should be
re-examined. Project note #19 realises this tower from apex data to 2.3e-41, and
records the additive encoding λ_n = Σ_{γ>0} 4 sin²(nα/2), manifestly ≥ 0 per zero
on the line. -/

/-- The `n`-th Li coefficient, via the derivative form at `s = 1`. -/
noncomputable def li (n : ℕ) : ℝ :=
  (1 / (Nat.factorial (n - 1) : ℝ)) *
    (iteratedDeriv n
      (fun s : ℂ => s ^ (n - 1) * Complex.log (completedRiemannZeta s)) 1).re

def LiPositivity : Prop := ∀ n : ℕ, 1 ≤ n → 0 ≤ li n

/-- [CLAIMED] Li 1997. -/
theorem RH_of_li : LiPositivity → RH := by
  sorry

/-- [CLAIMED] Li 1997, converse. -/
theorem li_of_RH : RH → LiPositivity := by
  sorry

/-! ## Node 3 — the Chebyshev error term  (external, classical)

RH ⟺ ψ(x) = x + O(x^(1/2+ε)) for every ε > 0.

`Zeta23/FromPNTPlus/` shows the PrimeNumberTheoremAnd material ports cleanly, so
the substrate for this node is partly built already. -/

/-- Uses Mathlib's `Chebyshev.psi`, NOT a local copy.

A hand-rolled `∑ n ∈ Finset.Icc 1 ⌊x⌋₊, Λ n` typechecks and denotes the same
function (`Ioc 0 n = Icc 1 n` on ℕ), but is a *different term*, so it is
unreachable from the ~20 lemmas Mathlib proves about `Chebyshev.psi`
(`psi_eq_sum_Icc`, `psi_eq_psi_coe_floor`, `psi_nonneg`, ...). Restating a node
off the library's blanket is the silent failure mode this file exists to avoid. -/
def ChebyshevSqrtError : Prop :=
  ∀ ε > (0 : ℝ), ∃ C > (0 : ℝ), ∀ x ≥ (2 : ℝ),
    |Chebyshev.psi x - x| ≤ C * x ^ (1 / 2 + ε)

/-- [CLAIMED] classical; via Mellin inversion / Landau's oscillation theorem. -/
theorem RH_of_chebyshev : ChebyshevSqrtError → RH := by
  sorry

/-- [CLAIMED] classical. -/
theorem chebyshev_of_RH : RH → ChebyshevSqrtError := by
  sorry

/-! ## Node 5 — Speiser's criterion  (external; anchors on `deriv riemannZeta`)

Speiser (1934): RH ⟺ ζ′ has no zeros in the strip 0 < Re s < 1/2.

Not in the first-pass list — found by asking Mathlib what it has rather than by
recall. `Mathlib/NumberTheory/LSeries/Deriv.lean` supplies the derivative API, and
`zeta-23-lean`'s `XiPrime/` module already proves unconditional results about the
zeros of ξ′ (all in the open strip; ≥ 0.85838 simple on the line). So this node has
substrate on both the Mathlib side and the zeta-23 side. -/

def SpeiserNoZeros : Prop :=
  ∀ s : ℂ, 0 < s.re → s.re < 1 / 2 → deriv riemannZeta s ≠ 0

/-- [CLAIMED] Speiser 1934. -/
theorem RH_of_speiser : SpeiserNoZeros → RH := by
  sorry

/-- [CLAIMED] Speiser 1934, converse. -/
theorem speiser_of_RH : RH → SpeiserNoZeros := by
  sorry

/-! ## Node 4 — Weil positivity  (external criterion; our closest substrate)

RH ⟺ the Weil functional is positive semidefinite on a suitable test class.

This is the node nearest to `anthropics/zeta-23-lean`, which already formalises
Weil's explicit formula (`Zeta23/WeilEF/`), Riemann–von Mangoldt, Stirling for
Γ'/Γ, Chebyshev–Mertens, Montgomery–Vaughan, and Sylvester inertia — all
sorry-free on the three standard axioms.

The functional is left abstract here on purpose: writing it honestly requires the
zero multiset and the archimedean/prime split, which is exactly the interface
zeta-23 exposes. Filling `WeilForm` is the first real engineering step, and doing
it by assuming an un-instantiated structure would reproduce the failure mode of the
circulating "machine-checked RH" preprints, whose top-level theorem takes a
hypothesis and is therefore a reduction rather than a proof. -/

/-- Placeholder for the Weil quadratic functional. -/
noncomputable def WeilForm (_f : SchwartzMap ℝ ℂ) : ℝ := 0

def WeilPositivity : Prop := ∀ f : SchwartzMap ℝ ℂ, 0 ≤ WeilForm f

/-- [CLAIMED] Weil's criterion, hard direction. Blocked on `WeilForm`. -/
theorem RH_of_weil : WeilPositivity → RH := by
  sorry

/-! ## Program nodes (this project) — stated, not yet expressible

The inventory `RH-Inventory-ProgramOriginals.md` lists 45 items. Its own synthesis
records that every chain — Bures, de Branges, apex, cubic, Gauss–Bonnet,
function-field — terminates at a single wall, with these identified to each other
and to RH:

  gate H_n, J_n ⪰ 0  =  Suzuki (O1)  =  apex no-crossing δ_max < 1/8
                     =  (GBP) u_B ≥ 0  =  arch-domination  =  Λ ≤ 0  =  GRH_N  =  RH

So this is not a broad surface: it is one node wearing many costumes. That is worth
recording precisely, because it means the graph gains nothing from formalising
several of them — but it also means a proved edge from *any* member propagates to
all the others, once the inter-equivalences are themselves formalised.

Not stated in Lean yet: each needs a carrier (the apex unitary `U_N`, the cubic
Weil functional `𝒞_ζ`, the Bures channel) that is a substantial definition on its
own. Deliberately left out of the first pass rather than faked. -/

/-! ## The measurement device

`sorry` is not merely a placeholder: Lean records it as the axiom `sorryAx`, so
"has this collapsed?" is a mechanically decidable question about our own artifact.

  CLOSED   ⟺  a term of type `RiemannHypothesis` (or its negation) with **no
               hypotheses**, whose `#print axioms` lists only
               `propext, Classical.choice, Quot.sound`.
  OPEN     ⟺  `sorryAx` appears, or the theorem takes an argument.

The second disjunct is the one that catches the circulating "machine-checked RH"
preprints: sorry-free and three-axiom-clean, but the top-level theorem binds a
hypothesis, so it is a reduction, not a decision.

Current reading of the instrument on this file: -/

#print axioms RH_of_lagarias
#print axioms RH_of_li
#print axioms RH_of_chebyshev
#print axioms RH_of_weil

/-! ## The RH=false face — the mirror, not a singleton

Earlier note in this file claimed the disproof side had essentially one node
(`∃ off-line zero`). That is wrong. If `P ↔ RH` then `¬P → ¬RH`, so **every
equivalence supplies a disproof route by negation**, and the false face is the
mirror of the true face rather than a point.

Some mirrors are computationally probeable in a way `∃ off-line zero` is not:
`∃ n, λ n < 0` refutes RH, `λ n` is computable, and the tower has been pushed to
n ≈ 3300 in the literature. Project note #19 records the additive encoding
breaking at n ≈ 157 for an off-line zero. That is a live dig face.

The edges below are **derived, not assumed** — each is proved by contraposition
from the corresponding equivalence edge. They carry `sorryAx` transitively (their
premises are still stubs), which is exactly what the audit should show. -/

def RHFalse : Prop := ¬ RiemannHypothesis

/-- Mirror of `LiPositivity`. -/
def LiNegative : Prop := ∃ n : ℕ, 1 ≤ n ∧ li n < 0

/-- Mirror of `LagariasIneq`. -/
def LagariasViolation : Prop :=
  ∃ n : ℕ, 1 ≤ n ∧
    (harmonic n : ℝ) + Real.exp (harmonic n) * Real.log (harmonic n)
      < ((ArithmeticFunction.sigma 1 n : ℕ) : ℝ)

/-- [DERIVED] A single negative Li coefficient refutes RH. -/
theorem RHFalse_of_li_negative (h : LiNegative) : RHFalse := by
  intro hRH
  obtain ⟨n, hn, hneg⟩ := h
  exact absurd (li_of_RH hRH n hn) (not_le.mpr hneg)

/-- [DERIVED] A single violation of Lagarias' inequality refutes RH. -/
theorem RHFalse_of_lagarias_violation (h : LagariasViolation) : RHFalse := by
  intro hRH
  obtain ⟨n, hn, hviol⟩ := h
  exact absurd (lagarias_of_RH hRH n hn) (not_le.mpr hviol)

end RHGraph
