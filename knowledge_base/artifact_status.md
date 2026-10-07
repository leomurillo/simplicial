# Artifact Status And Deprecation Register

Created: 2026-05-15

This register keeps knowledge management lightweight.  It does not move or
delete source material.  It states which files are current authorities, which
are supporting evidence, and which should not be cited until rewritten or
extracted into the claim graph.

## Operating Rules

1. `knowledge_base/claim_graph.md` is the current claim source of truth.
2. `knowledge_base/evidence_ledger.md` is the current evidence source of
   truth.
3. Discovery notes, team todos, duplicate drafts, generated PDFs, and copied
   external drafts are not current claims unless their content is extracted into
   the graph or ledger.
4. Deprecated means "do not cite as current authority"; it does not mean
   "delete."

## Current Control Artifacts

| Artifact | Status | Use |
|---|---|---|
| `knowledge_base/claim_graph.md` | current authority | Claim IDs, dependencies, evidence level, and disconfirmation questions. |
| `knowledge_base/evidence_ledger.md` | current authority | Empirical/computational evidence and what it can actually support. |
| `knowledge_base/artifact_status.md` | current authority | Deprecation and source-of-truth routing. |
| `knowledge_base/critical_leaf_closure_theorem_candidate.md` | active theorem target | Critical-leaf/tower closure program with finite residual blockers visible. |
| `knowledge_base/paper_change_queue.md` | active queue | Manuscript changes implied by the graph. |
| `knowledge_base/fundamental_conjecture_program.md` | private strategy | Theorem-selection spine, not public language. |

## Supporting Knowledge Notes

| Artifact family | Status | Use |
|---|---|---|
| `knowledge_base/a0_f0_bridge_strategy.md` and `knowledge_base/b0_*.md` | active theorem notes | Supporting derivations for B0-B8 and A0; cite graph nodes first, then these notes. |
| `knowledge_base/fc2_*.md` | active theorem notes | Supporting FC2 family theorem, first-row solution, and row-classification details. |
| `knowledge_base/gap_closure_plan.md` | active work plan | Proof-extraction and closure backlog. |
| `knowledge_base/publication_strategy.md` | active strategy | Audience packaging and risk register. |
| `knowledge_base/theorem_mass.md` | speculative north-star | Private agenda attractor only; not a public theorem source. |

## Active Manuscript Spine

| Files | Status | Note |
|---|---|---|
| `01.*` through `13.*` | active spine | Core simplicial/Fisher/conductor/AI/simplectic sequence. |
| `14.*`, `15.*`, `17.*`, `18.*`, `19.*`, `24.*` | active cubic/Bures spine | Paper 24 is the compact public synthesis; Papers 14, 15, 17, 18, and 19 keep component proofs and audits. |
| `21.*`, `22.*`, `Paper23_Primorial_Noether_Weil_Identity (4).md` | active conditional primorial program | Keep explicitly conditional; no RH proof claim. |
| `beyond_smooth_spaces_discrete_fisher_skeletons.md` | active public-facing condensation | Use as an AI-facing article derived from Paper 12, with evidence boundaries intact. |

## Superseded Or Archive Candidates

| Artifact family | Status | Action |
|---|---|---|
| `single-discrete_fisher_skeletons_for_ai_optimization.md` and PDF | superseded by Paper 12 and `beyond_smooth...` | Keep as historical draft; do not cite unless comparing draft evolution. |
| `Paper11_*` notes and `Paper11_Team_Todo.md` | discovery/team logistics | Extract only current finite-row facts into graph/ledger; then archive later if desired. |
| `Note_*.md` files | discovery notes | Keep while active, but cite the resulting paper section or empirical report instead of the note. |
| `fromgrok/` | external/scratch import | Use only as idea source; claims must be rederived or cited through local proof/evidence artifacts. |
| generated PDFs next to Markdown drafts | build artifacts | Cite the Markdown source unless the PDF is the only available source. |

## Quarantined

| Artifact | Reason | Safe handling |
|---|---|---|
| `paper16_draft (1).pdf` | Overstates the physical three-body conclusion ("three-body problem is not chaotic") and is not in the active README spine. | Do not cite as a current claim.  If revived, rewrite as a bounded Bures-lift analogy downstream of T15/T16, with no claim to solve Newtonian three-body dynamics. |
| Retired `Z/12Z` vs `Z/18Z` FFT proxy for Constraint 3 | Reduces to a random-phase mean statistic and has been replaced. | Cite `empirical/reports/constraint3_cubic_noether_verification.md` instead. |

## Cleanup Backlog

1. Rename versioned working files with spaces/parentheses after the next
   manuscript freeze, especially
   `Paper23_Primorial_Noether_Weil_Identity (4).md`.
2. Move superseded single-paper drafts and team notes into `archive/` only
   after confirming no active build or citation path depends on their current
   location.
3. Add a small machine-readable claim table after one human pass over the
   updated graph.
