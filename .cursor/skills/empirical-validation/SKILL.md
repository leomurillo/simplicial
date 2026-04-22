---
name: empirical-validation
description: Guides computational validation of theorems, lemmas, and numerical claims via code, QA, execution, and didactic reporting. Use when empirical checks, simulations, counter-examples, or numerical bounds are needed for a math manuscript.
---

# Empirical software validation

## When to use

- A claim in the paper should be tested by computation (bounds, algorithms, edge cases).
- The user asks for scripts, simulations, or refutation searches tied to the manuscript.

## Scope

All generated code, data, and reports live under `empirical/`. The Empirical Skeptical agent MUST NOT edit the LaTeX manuscript; only the Author integrates empirical findings into the paper.

## Severity ladder (applies to every QA finding)

- **Critical:** Bug that invalidates the numerical conclusion (wrong math, unstable algorithm, falsely triggered counter-example). QA-blocking.
- **High:** Numerical hazard likely to mislead (catastrophic cancellation, unchecked tolerances, wrong norm). QA-blocking.
- **Medium:** Performance, style, redundancy. Not QA-blocking.
- **Low:** Polish, comments, formatting. Not QA-blocking.

## Cycle protocol

1. **Hypothesis extraction:** The Author (or orchestrator) flags a specific theorem, lemma, or numerical claim to validate and records it in `empirical/reports/cycle_{n}.md`.
2. **Code generation + execution (Empirical Skeptical):** Produce an executable script (typically Python with NumPy) that implements the test and documents how each step maps to the mathematics, **then run it** and capture the output (stdout, any generated plots or tables) inline in a draft report or transcript alongside the script. Scripts should be designed to print compact, human-readable output — the Empirical Reviewer consumes both the code and its output as a single package.
3. **Code + output QA (Empirical Reviewer):** Review the script for numerical stability, algorithmic correctness versus the stated math, and practicality (runtime, vectorization), **and** review the captured output for plausibility (do the max errors sit near machine epsilon? does the verdict match the observed values? are there silent warnings or nan/inf?). Return severity-tagged findings and a closing `STATUS:` line.
4. **Revision loop:** If STATUS AMBER, the Empirical Skeptical revises the script, re-executes, and re-submits the code + fresh output for another QA pass (up to the 3-loop limit).
5. **Reporting and integration:** After STATUS GREEN, the Empirical Skeptical writes the final didactic report under `empirical/reports/` and the Author integrates confirmed bounds or edge cases into the manuscript.

Design implication for scripts: prefer a single `main()` that prints a compact summary table (hypothesis | trials | threshold | observed error | verdict) at the end. Long debug output is fine during development but trim before submission so the Reviewer can assess plausibility at a glance.

## Termination

- **CRITICAL LIMIT:** Do not exceed **3 QA loops** per claim (each loop = one revision + re-execution + re-review).
- **STATUS GREEN:** Empirical Reviewer issues GREEN when the script is bug-free *and* its captured output supports the claim (no Critical or High findings, observed errors within predicted bounds). The didactic report is then written and the results are certified for the Author.
- **STATUS AMBER:** If after the 3rd QA loop the Empirical Reviewer still returns Critical or High findings, halt. Present the current script, its latest output, and open QA concerns to the user, append the dispute to `reviews/open-issues.md`, and do not feed the empirical results into the manuscript until a human adjudicates.
- **STATUS RED (escalation, not a loop outcome):** If the Empirical Reviewer judges the script correct but its output constitutes a genuine counter-example to a paper claim, immediately stop treating the claim as proved. The Empirical Skeptical agent drafts an "Empirical Refutation Report" under `empirical/reports/`, the Author halts writing on that claim, and the contradiction is logged in `reviews/open-issues.md` as a mathematical problem requiring a theoretical fix or downgrade (e.g., to a conjecture). RED overrides GREEN. Because execution now precedes QA, a RED is evident at the first QA pass — there is no "certified" intermediate state to roll back.

## Open-issues log

`reviews/open-issues.md` is shared with the authorship loop. Append AMBER QA stalemates and RED refutations with a dated entry and cycle number so the human reviewer sees the full empirical state alongside formalism and narrative disputes.
