---
name: authorship-orchestration
description: Orchestrates iterative drafting and red-team review between Author and Reviewers X and Y for LaTeX math manuscripts. Use when refining arXiv-style papers, coordinating formalism and narrative audits, or running multi-agent author–reviewer loops.
---

# Authorship & editing orchestration

## When to use

- The user wants a structured loop between writing (or editing an existing draft) and adversarial review.
- Work spans major sections (introduction, a specific proof, full document pass) before submission.

## Posture

The current workspace already contains a full draft manuscript. Default to **editing-first**: target specific sections the Author has touched, not a green-field rewrite.

## Source format

Drafting happens in Markdown (`simplicial_vector_calculus.md`) with `$...$` / `$$...$$` math, previewed live via Cursor's Markdown preview (Ctrl+K V). LaTeX `.tex` is produced only in the pre-submission pass (see "Submission pass" below). Reviewers evaluate the Markdown source during normal cycles; they do not block on the absence of `\label{}` / `\ref{}` or theorem environments until the submission pass.

## Severity ladder (applies to every reviewer finding)

- **Critical:** Invalidates a theorem, proof, or definition. Loop-blocking.
- **High:** Unstated assumption, broken reference, non-standard notation that will mislead the reader. Loop-blocking.
- **Medium:** Readability, redundant phrasing, suboptimal motivation. Not loop-blocking.
- **Low:** Typos, polish, stylistic preferences. Not loop-blocking.

A loop is "blocking" only if a reviewer returns at least one Critical or High finding.

## Entry points

The cycle body is the same regardless of entry point, but the first step differs:

- **Editing an existing section (the default for this project):** Start at **step 1 (Review)**. The draft already exists; Reviewers X and Y audit it first, and the Author responds. This is the correct entry point for every section of `simplicial_vector_calculus.md` that has not yet been through a review cycle.
- **Writing a new section from scratch:** Start at **step 0 (Draft)** below. The Author drafts the section first, then reviewers audit.

## Scoping

Do not review the whole manuscript in one cycle. One scope per cycle, chosen by section or appendix (e.g., "§3 Intrinsic Cross Product", "Appendix B: Proof of $K^3 = -K$"). Record the scope in the feedback file header. A suggested order when priorities are unclear:

1. §1 Introduction (framing first; everything downstream depends on it).
2. §2 Simplicial Coordinates: Setup (definitions the proofs rely on).
3. §3, §5, §7, §8 (contribution-bearing theorems and their specializations).
4. §4, §6, §9, §10 (completeness, properties, future work, conclusion).
5. Appendices A–E (formalism-heavy; best reviewed after the body they support is stable).

## Cycle protocol

0. **Draft (new-section entry point only):** The Author writes the section in Markdown.
1. **Reviewer X (Formalism Audit):** Request a formalism audit of the current scope (definitions, proofs, edge cases).
2. **Reviewer Y (Structural & Narrative Audit):** In parallel with step 1, request a narrative audit (flow, motivation, notation, literature).
3. **Synthesis:** Collect both critiques into `reviews/feedback_cycle_{n}.md`, preserving each finding's severity tag and the reviewer's closing `STATUS:` line. The file header records the scope (section label) and cycle number.
4. **Triage & revision:** The Author addresses every Critical and High finding, records accept/reject decisions (with mathematical justification when rejecting), and edits the Markdown source. Medium and Low findings are addressed at Author discretion and do not force another loop.
5. **Re-review:** Return to step 1 for the same scope. Stop per the termination rules below.

## Termination

- **CRITICAL LIMIT:** Do not exceed **3 revision loops** per section scope.
- **STATUS GREEN:** Issued by a reviewer when no Critical or High findings remain. If *both* Reviewer X and Reviewer Y issue STATUS GREEN in the same cycle, halt the loop for that scope and present the finalized section for human sign-off. Also surface any entries the Author appended to `reviews/open-issues.md` so the human sees open mathematical disputes alongside the approval.
- **STATUS AMBER:** If after the 3rd revision cycle either reviewer still returns Critical or High findings, immediately halt. Present the current section to the user with a STATUS AMBER warning and explicitly list the unresolved findings (citing specific Theorem, Lemma, or equation labels) so the human can adjudicate. Entries already in `reviews/open-issues.md` remain; surface them alongside the amber disputes.

## Submission pass (Markdown → LaTeX)

Once all target sections have reached STATUS GREEN in Markdown and the human has signed off:

1. **Convert:** The Author converts `simplicial_vector_calculus.md` to `main.tex` (typically via `pandoc simplicial_vector_calculus.md -o main.tex --standalone`). Optionally split into per-section `\input{}` files.
2. **Repair:** The Author promotes plain-text "Theorem 3.1" labels to `\begin{theorem}\label{thm:foo}...\end{theorem}` environments, wires up `\ref{}` / `\eqref{}` / `\cite{}`, and installs the bibliography.
3. **One additional cycle:** Run a single Reviewer X (Formalism) + Reviewer Y (Narrative) pass on the `.tex` source, scoped *specifically* to conversion artefacts: broken or stale cross-references, mangled math macros, theorem-environment mis-grouping, citation format, over- or under-escaped characters, and figure/float placement.
4. **Terminate:** The submission pass uses the same severity ladder and 3-loop cap. On STATUS GREEN from both reviewers, the `.tex` is ready for arXiv packaging. On STATUS AMBER, append unresolved conversion issues to `reviews/open-issues.md` and halt for human sign-off.

## Cross-scope propagation check

When an Author revision retires, narrows, or rephrases terminology or a claim in the current scope, the same language may survive elsewhere in the manuscript and create a cross-cycle regression later (as happened for §2 Remark 2.1 after §1.2 item 1 was softened). To guard against this, at the end of every Author cycle:

1. Identify retired or narrowed phrasings (e.g., "mass-action ray" → "gauge direction", "formally the same" → "structurally analogous", "complete intrinsic vector calculus" → narrowed scope).
2. Run a propagation grep for each retired phrasing across the full manuscript. For every match outside the current scope, the Author either:
   - **Sweeps immediately** — apply parallel edits and record each site in the triage under a `### Propagation check` subsection; or
   - **Logs for later** — append an entry to `reviews/open-issues.md` labelled "terminology-propagation pending" so the regression is flagged at the next scope's Cycle 1 rather than as a surprise.
3. If the Author sweeps immediately, the out-of-scope edits are considered *consequential* rather than scope creep, provided they are strictly mechanical propagation of the cycle's resolved language. Any substantive change requires the adjacent scope's own cycle.

This step does not replace the Cycle 1 review of downstream scopes; it prevents already-adjudicated consensus from silently rotting.

## Post-AMBER spot-patch (human-authorized)

Once a scope hits STATUS AMBER at the 3-loop cap, the default path is human adjudication. If, after reviewing the open issues, the human explicitly authorizes a **minimal targeted fix** for specific findings (by ID), the orchestrator may run a single bounded patch pass under the following constraints:

- **Authorization:** the human must name the findings (e.g., "address [F-H-5], [F-M-7], [F-M-8]"). The Author may not broaden the scope beyond the named IDs.
- **Scope:** strictly surgical edits at the lines the findings cite. No general revisions, no new content, no renaming of sections.
- **Verification:** the originating reviewer(s) of the named findings spot-verify the changed lines only. They do not re-audit the whole scope. Their verification report is a short confirmation of RESOLVED / NOT-RESOLVED per finding and carries its own closing `STATUS:` line.
- **Cap does not reset:** a spot-patch pass does not count as a new cycle and does not restart the 3-loop budget. If the spot-patch itself introduces a new Critical or High finding, the scope returns to AMBER and requires human re-adjudication.
- **Record:** append an `## Author triage (post-AMBER spot-patch)` section to the terminal cycle's feedback file, and update the corresponding entries in `reviews/open-issues.md` (mark RESOLVED with date, or add a new entry for any new finding).

## Open-issues log

`reviews/open-issues.md` is the persistent record of disputes the Author could not resolve, claims downgraded to conjecture, and cross-cycle concerns. Every AMBER halt must append its unresolved findings there with a dated entry and the originating cycle number. Post-AMBER spot-patches update these entries in place (RESOLVED / partially resolved).
