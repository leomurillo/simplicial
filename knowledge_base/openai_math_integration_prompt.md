# Session prompt: integrate OpenAI `openai/math` results into the corpus

*Prepared 2026-10-07. Paste this file, or point the session at it, to launch.*

## Context

On 2026-10-07 OpenAI published https://github.com/openai/math. It holds 722 model-generated manuscripts in 372 "families", with Lean formalizations for many of them. The headline for us is **family 003, the quasi-Riemann hypothesis**. It claims that every Dirichlet L-function (ζ included) and every finite-order Hecke L-function over ℚ(√−3) has no zero in Re s > 7/8, uniformly in modulus and height. The core statement is Lean-formalized; see `lean/docs/003.md` and the comparator `lean/ComparatorChallenges/QuasiRiemannHypothesis.lean`.

- Preprints:
  - `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf` (7/8)
  - `preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf` (alternate 11/12)
  - `preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf`
- Method:
  - a completed Kubota–Patterson cubic-theta sum over ℤ[ω] with sextic residue symbols, computed two exact ways (reflection and Poisson summation);
  - Prop 2.1 ("continuation from a common signal") continues 1/L across the hypothetical rightmost zero;
  - the result is transferred to ℚ by L_F(s, χ∘N) = L(s,χ)·L(s,χχ₋₃).
- Corollary 1.2 in the paper: Vinogradov's least-nonresidue bound n(p) ≪ (log p)^A, and deterministic polynomial-time square roots mod p.

Download the PDFs and run `pdftotext -layout` on them. Put the downloads in a fresh scratch directory, never inside the repo.

## Operating rules (from memory; binding)

- **Papers lead.** Land updates directly in the numbered manuscripts and reports. No status flags, and no new standalone `Note_*.md`.
- **Tier hygiene.**
  - External results are **[A]** (attributed), never [P].
  - Anything that depends on family 003 is tagged as resting on OpenAI 2026, a model-generated result that is Lean-formalized per OpenAI. Record that provenance once and cite it consistently.
  - Never upgrade numerics to theorems.
- **Peer-review discipline.** Give each candidate below an ACCEPT, REFINE or REJECT verdict with reasons in an internal log section.
- Work serially, with no parallel agents and no torch. Chat math is plain Unicode; manuscripts keep LaTeX.
- Build-pipeline gotchas still apply: affiliation line required, no manual hypertargets, run the linker once, and cross-paper § references drop the §.
- Do not commit unless asked.

## Part A: corrections (do these first)

### A1. Paper 22, Lemma 8.1c: the natural-scale route is now [A]

File `22.primorial_cumulant_noether_rh.md`, around lines 2281–2400 (Lemma 8.1c, route 2 "Natural-scale diagonal", and the Claim-hygiene paragraph).

Write out the derivation. Check each step yourself rather than trusting this sketch.

- By 003 and the functional equation, every nontrivial zero of every primitive L(s,χ) has 1/8 ≤ β ≤ 7/8, so |ρ| ≥ 1/8.
- Use the truncated explicit formula (Davenport, Ch. 17 and 19) with N(T,χ) ≪ T log(qT):
  - ψ(X,χ) − δ_χ X ≪ Σ_{|γ|≤T} X^β/|ρ| + X log²(qX)/T ≪ X^{7/8} log²(qT) + X log²(qX)/T.
  - Take T = X.
  - For imprimitive χ, add O(log q · log X).
- Hence max_{χ∈𝒳ₙ} |…| ≪ X^{7/8} log²(PₙX), so E_n(f) ≪ X^{−1/8} log²(PₙX) after partial summation with G_f.
- This is uniform for X ≥ (log Pₙ)^{16+ε}, so a Dirichlet cutoff M_n polynomial in Pₙ works. Blocks below that range keep the existing 8.1a/8.1b treatment.

Then:

- Update the route-2 text, the "classical inputs allowed" list (add 003 as [A]), Proposition 8.2's hypotheses if they change, and Claim hygiene.
- Paper 22's remaining obligations become the 8.1a occupation lift and the Archimedean Noether limit (Conj 5.2). Say so explicitly.
- State plainly that this does **not** prove RH.

### A2. `empirical/reports/lemma_8_1c_wall.md`

- Correct the overstatement "uniform E_n→0 ⟺ no Siegel zero ⟺ GRH for the primorial characters". A fixed half-plane θ < 1 already suffices for E_n → 0.
- The "ONE wall" unification paragraph must be re-scoped. Pointwise uniformity at natural scale is now separated from GRH. The remaining genuine wall in Paper 22 is the archimedean one.
- If the companion script `empirical/verify_lemma_8_1c_wall.py` prints the same claim, fix that too.

### A3. Siegel and class-number reports

Files: `empirical/reports/effective_hR_bound.md`, `real_quadratic_siegel.md`, `rh_selberg_siegel.md`, `verify_grh_siegel_lever.md`, `grh_anisotropy_dividend.md`.

- "Layer 3 = OPEN (Chowla)" and "the residual Siegel zero is open": 003 gives β ≤ 7/8 for every real χ with no exception.
- Derive, or cite, an **effective** lower bound L(1,χ_D) ≫ 1/log log D from the fixed zero-free half-plane. This is classical under quasi-GRH: Littlewood-type, using convexity bounds in the strip.
  - If the derivation is clean, give it with tier [A] on top of 003.
  - If not, state only what the half-plane gives directly.
- Also check the consequences these reports list: effective h(−d), effective Linnik and PNT in arithmetic progressions, and Euler's idoneal numbers via Weinberger.
- The last three reports keep their correct content: no-Siegel-zero is still weaker than GRH, and complex zeros are untouched. Only re-scope the "open" labels.

### A4. `HeightBoundedGRH-PrimorialN210-Draft1.md`

- §4.4 uses the Heath-Brown/Vinogradov–Korobov zero-free region. Add the uniform strip |β − ½| ≤ 3/8 at all heights.
- Theorem C's region only matters for |γ| ≤ T* ≈ 0.66. Say what 003 adds beyond T*.
- Note honestly that classical numerical GRH verification (Platt) already covers q | 210 to large height.

### A5. Sweep

Grep the corpus for remaining "conditional on GRH", "Siegel–Walfisz only", "exceptional zero" and "zero-free region" statements that a uniform 7/8 half-plane now discharges. Start with `GRH-Apex-Integration-Draft1.md`, `43_primorial_moduli_bombieri_vinogradov_hybrid_r0_5.md` (§2 line ~88), `diez.md`, `ocho.md`, `N11-…`, `N7-…` and `OpenProblemsSurvey/`.

Paper 43's θ₀ is **unchanged**. Pointwise uniformity from 003 is nontrivial only for moduli up to about X^{1/8}, far below the BV level ½. Record that as a REJECT, with the reason.

**Out of scope:** the RH apex open step (arch-domination, energy condition, Λ ≤ 0). 003's strip gives only de Bruijn–Newman Λ ≤ 9/32 ≈ 0.281, which is worse than Polymath's 0.22. Record that as a REJECT. Do not touch the apex-thread papers beyond a one-line citation, and only where they list unconditional strip inputs.

## Part B: other families to triage

For each family:

1. Read the family description in `CONTENTS.md` and the abstract.
2. Skim the paper only if the link survives that read.
3. Give an ACCEPT, REFINE or REJECT verdict.
4. On ACCEPT, land a citation or remark in the target paper.

Candidates, roughly ranked:

| # | OpenAI family | Why it may matter | Target in our corpus |
|---|---|---|---|
| 1 | **211**, plus companions: geometric phase diagram, diffusion and spectra of random planar maps; the **"quantum spheres"** (Liouville quantum gravity spheres; critical γ=2 sphere at q=4; √2 sphere for spanning-tree-weighted maps; √3 for FK–Ising) | Discrete planar networks converge to a continuum sphere. Random walks converge to Liouville Brownian motion, with **eigenvalue and heat-trace convergence**. Surface-to-tree transition at q=4. These are **not** noncommutative or Podleś spheres; the link is through random networks and curvature. | `56_the_dynamic_network.md` (curvature carried by bond counts; disclination point mass); `55_the_network_of_ports.md` (cut-law and continuum limit); `58_an_arrow_from_growth_and_defects.md` (Kron reduction and spanning trees); `32.1_the_bekenstein_sphere.md` (the "little sphere"; check whether LQG area law or log-correction language rhymes with its log Q, and fence it if only thematic) |
| 2 | **265**: area laws and tensor networks for 2D gapped systems | Rigorous entanglement area law plus PEPS approximation | Paper 55's cut-law area law; Paper 32.1 |
| 3 | **290**: relative bicentralizers and modular spectral recovery (Connes' bicentralizer conjecture) | Tomita–Takesaki; Connes | P∞-A §8 modular adjudication (Prop 8.3a ax+b obstruction); check consistency |
| 4 | **023**: Patterson's first moment for cubic Gauss sums | Same Eisenstein/cubic machinery as 003; tr(F) is a Gauss sum in our P0 keystone | P0 keystone, N-series, ℤ/6 χ₃ papers |
| 5 | **007**: two-point Chowla and corrected Elliott | Liouville correlations; multiplicative functions | N-series, Paper 22 (prime side), apex cumulant/HL n-tuple arc |
| 6 | **101**: simplices uniquely maximize the isotropic constant; sharp entropy lower bound for log-concave laws | Simplex extremality and an entropy bound | 01/01c (simplicial information geometry); 54 (Φ = log Z) |
| 7 | **088**: Petty projection conjecture, plus a counterexample to Brannen's *simplex* maximization | Simplex extremal geometry (with a negative result) | 01-series; check that no corpus claim assumes the simplex maximizes projection-body volume |
| 8 | **273**: entropy photon-number inequality | Bosonic thermal states attain equality; quantum info | `59_the_arithmetic_of_work_extraction.md` (ergotropy, bosonic protocols); Paper 54 §4 quantum arrow |
| 9 | **260**: spacetime Penrose inequalities (charge, rotation, AdS); Kerr–Newman Penrose inequality | Area/mass bounds | 32.1 Bekenstein sphere; Paper 32 gravity sector; ToE synthesis |
| 10 | **298**: microstates and non-microstates free entropy differ | Free Fisher information | 01c / Paper 24 monotone-metric fork; Petz/DC-gap note |
| 11 | **093**: dimension-free log-Sobolev for log-concave measures | Functional inequality | Fisher-skeleton papers (12, 14) |
| 12 | **013**: Ostmann's inverse Goldbach; **026**: positive density of large prime gaps | Additive and prime structure | Goldbach mod-8 reference; self-certifying sieve (prime gaps) |
| 13 | **015**: torus-packet equidistribution in prime, quartic and sextic degree | Sextic fields; equidistribution | ℤ/6 arc (likely REJECT as thematic) |

Also scan `CONTENTS.md` yourself for anything missed. The ten reasoning-trace PDFs in `reasoning_traces/` are optional; 007 is the only arithmetic one.

## Deliverables

1. Edits from Part A landed in the manuscripts and reports, with derivations checked.
2. An internal log section, in Paper 22's existing audit area or the repo's usual log location (not a new Note file): Part B verdicts with one-line reasons, plus the Part A REJECTs (Paper 43 θ₀, de Bruijn–Newman).
3. Update memory `reference_openai_quasi_rh_7_8.md` with final dispositions, and add memory entries for any ACCEPTed Part B family.
4. Rebuild PDFs only for papers that already ship PDFs and were touched (for example 22).
5. A short chat summary: what changed, which tiers moved, and what stays open.
