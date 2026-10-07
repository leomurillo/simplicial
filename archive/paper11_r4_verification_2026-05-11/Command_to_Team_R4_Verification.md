# Command to Team — Verify Heaven's R⁽⁴⁾ Recipe Before Upgrading Paper 11

**Date:** May 11, 2026
**From:** lead
**Subject:** Staged-answer protocol preserved. Heaven's number \(R^{(4)}(u,1,1,u)|_{u\leftarrow u} = -1\) is held as a sealed triage anchor. It does not upgrade Paper 11 until §A's recipe is verified internally. Two-cell verification task assigned. Wurgaft outreach proceeds in parallel under the lead.

## Decision

Heaven returned the §A definition, the cell value (\(-1\)), the §6 phrasing recommendation, and a derivation summary. The §A definition is precise. The derivation summary at §B is recipe-level, not arithmetic. The transition from a full Leibniz expansion (which gives Π₄ structure at this cell, evaluating to \(-2\)) to the reported \(-1\) must happen either by reinterpreting the product rule as a non-crossing Leibniz, or by the antisymmetric paired-slot projection killing the crossing partition's contribution. The latter is plausible. Neither is shown arithmetically.

By the staged-answer protocol stated in Message to Heaven 7: recipe is not symbolic backing. The anchor \(-1\) is sealed. Paper 11 §6 is not rewritten and Theorem 9.3 stays at support level externally until internal verification lands.

## Task — Two-Cell Verification

### Cell 1 — verify Heaven's number on the original target

Implement Heaven's §A definition as code at:

```
cell    = (tau, omega, beta, iota) = (u, 1, 1, u)
entry   = u <- u
family  = TTWW, H_4 orbit size 72
```

Implement the four operational pieces in §A as labeled stages:

1. **Fourth covariant derivative at \(p_*\).** Expand each \(\overline K^{CH}_{p(t)}(x_i)\) as a Taylor series in the two-parameter displacement \(h = s h_\tau + r h_{\omega_0}\), to second order. The relevant operators are \(M_{x_i}\), \(B_{x_i}^\tau\), \(B_{x_i}^{\omega_0}\), and \(C_{x_i}\) exactly as in §9.1. Compose four such expansions.

2. **Lower-order contraction subtraction.** Apply the Leibniz product rule to the Taylor-expanded product of four \(\overline K^{CH}_{p(t)}\) operators, subtract the path-composed \(\overline K^{CH}_{p(t)}(x_1 + x_2 + x_3 + x_4)\) (i.e. \(\overline K^{CH}_{p(t)}(0)\) at this cell, since the labels sum to zero), and extract the leading mixed coefficient. Do not impose any partition-lattice or non-crossing restriction by hand. The Leibniz expansion is the whole product rule; any cancellation must arise from step 3, not from a pre-imposed combinatorial filter.

3. **Antisymmetric paired-slot projection.** Apply Heaven's six-term Bianchi-type alternation: \([K^{CH}(u), K^{CH}(v)]\) against \((w, z)\), summed with alternating signs over the three pair-of-pairs splittings \(\{(u,v;w,z),\ (u,w;v,z),\ (u,z;v,w)\}\) per Heaven §A.

4. **Normalization \(1/4!\).** Apply the overall factor to obtain the matrix entry at \(u \leftarrow u\).

Report the value. Three outcomes are meaningful:

- **\(-1\):** Heaven's recipe verified. The single-cell NC₄ match was coincidence-with-curvature, not coincidence-with-lift. Anchor unsealed. Draft 0.3.1 §6 may be rewritten per Heaven's recommended phrasing.
- **\(-2\):** Heaven's prose recipe, as implemented, produces Π₄ at this cell. Either we misread §A (most likely the antisymmetric projection in step 3) or the recipe omits a non-crossing constraint Heaven did not state explicitly. Anchor stays sealed. Re-escalate with one targeted question about §A step 2 or §A step 3 — not a re-ask of the whole question.
- **Anything else:** the recipe is inconsistent with our setup or our interpretation. Anchor stays sealed. Re-escalate.

### Cell 2 — discriminate global NC₄

In parallel, pick any one cell from the \(+2\) stratum of the TTWW size-24 NC₄ value distribution (40 records available; the existing `compute_h4_mobius_followups.py` already filters by family, orbit size, and cumulant value). Implement the same §A recipe at that cell.

The \(+2\) stratum is the discriminator. If \(R^{(4)}\) at a \(+2\)-stratum cell equals \(+2\), then NC₄ tracks \(R^{(4)}\) globally on this row, and the class-scan independence finding has a clean structural explanation: the inherited lift coefficient is not \(R^{(4)}\); the cumulant is. If \(R^{(4)}\) at that cell equals something other than \(+2\), then NC₄ does not track globally, the cancellation rule is cell-specific or family-dependent, and the freeness question note becomes the live Paper 11 track.

Two cells, one recipe, two values. That is enough to know which branch of the original three-branch ambiguity we are in.

## What Does Not Happen

- Paper 11 §6 is not rewritten until Cell 1 returns \(-1\). The Draft 0.3.1 downgrade as currently stated stands.
- Theorem 9.3 stays at support level externally.
- No new Heaven escalation unless Cell 1 verification fails. In that case, the next message is one targeted question about §A, not a re-ask.
- The freeness question note continues parallel and non-blocking. Cell 2's result will sharpen it or close it.
- The Wurgaft outreach track is unaffected. The lead handles Task 1 in parallel based on the team's existing weekday computation (\(r = 0.886448\) vs reported \(0.89\)). The Δ⁽⁴⁾ verification work does not block the outreach.

## Acceptance Criteria

A single artifact — `compute_R4_covariant_at_cell.py` — that takes the cell labels as input, computes \(R^{(4)}\) from §A's definition step by step (each of the four stages emitting a visible intermediate value into the report), and returns the matrix entry value.

Hard constraint: no invocation of the NC₄ cumulant, the Π₄ cumulant, or the input-side lift coefficient during the computation. Importing the \(M\), \(B\), \(C\) operators from §9.1's arity-2 implementation is correct and expected. Importing anything from `compute_h4_mobius_witness.py` or `compute_h4_mobius_followups.py` for the purpose of computing the value is incorrect; the implementation must be rewritten if it does so. The cumulant scripts may be imported only for *comparison after the fact*, never for the value itself. The verification is only meaningful if the recipe stands on its own.

## Files to Produce

- `empirical/compute_R4_covariant_at_cell.py`
- `empirical/reports/h4_R4_covariant_target_cell.md` — Cell 1 result with full stage-by-stage derivation trace.
- `empirical/reports/h4_R4_covariant_plus2_cell.md` — Cell 2 result with full stage-by-stage derivation trace.
- Updates to `Draft_0.3.1_Delta4_NC4_cumulant.md` and `Paper11_Returning_Leader_Report.md` only if Cell 1 returns \(-1\), per Heaven's recommended §6 phrasing.

## Decision Posture

Protocol preserved. Two-cell verification owns the next compute cycle on this track. Outreach proceeds in parallel under the lead. Heaven is not re-asked unless verification fails. Paper 11 external posture unchanged.

— lead
