# Reviewer X — Formalism Audit — Cycle 2
**Scope:** §1 Introduction (lines 35–76 of simplicial_vector_calculus.md, post-Cycle-1 revision)
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Resolution of Cycle 1 findings

- **[F-H-1] PARTIALLY RESOLVED** — §1.1 now correctly narrows the claim to an intrinsic algebra of rotations and explicitly excludes differential operators, but the Abstract and §4 still advertise a "complete intrinsic calculus" / "complete realization of 3D Euclidean vector calculus," so the manuscript no longer has one formally consistent scope statement.
- **[F-H-2] PARTIALLY RESOLVED** — §1.1, §1.2 item 3, and §1.3 now use the correct qualified formulation ("once the simplicial Gram data is fixed"), but the Abstract and §4 Remark 4.2 revert to the stronger unqualified claim that the construction is defined without Cartesian reference, leaving the dependence on prior Euclidean metric data formally blurred.
- **[F-H-3] RESOLVED** — §1.2 item 7 now explicitly restricts uniqueness to the simplicial / Hodge-dual / axis-to-skew-operator framework, and this is coherent with §9.1–§9.2, which explain why the binary case is special and why higher-$N$ analogues become higher-arity.

## New findings

### Critical
- None.

### High
- **[F-H-4]** The Abstract and §4 now formally contradict the revised §1: the introduction carves out differential operators and defines "intrinsic" only after fixing simplicial Gram data, whereas the Abstract still says the three operators form a "complete intrinsic calculus" and §4 still calls them a "complete realization of 3D Euclidean vector calculus" that can be carried out "without reference to a coordinate frame"; this manuscript-level inconsistency must be normalized before the introduction can be considered formalism-ready.

### Medium
- **[F-M-6]** §1.2 item 3 advertises a "Joint gauge-compatibility theorem (Section 4)," but §4 is still headed "Completeness of the Intrinsic Vector Calculus" and Theorem 4.1 is stated as a closure theorem rather than with the sharper quotient/descent language now used in the introduction; the mathematical content is nearby, but the theorem-signposting is no longer fully aligned.

### Low
- None.

## Summary
The Cycle 1 repairs inside §1 are real: the scope restriction, the qualified notion of intrinsicness, and the scoped uniqueness claim are all materially better. But the revision has exposed a manuscript-level inconsistency, because §1 now says something formally narrower and more precise than the Abstract and §4 still say. Until that global scope statement is made coherent, I cannot clear the introduction at High severity.

STATUS: AMBER
