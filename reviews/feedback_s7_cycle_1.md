# §7 — Cycle 1 synthesis

**Scope:** §7 Computational Kernel: The 9-Multiplication Apply — preamble, §7.1 (output redundancy 16 → 12), §7.2 (input redundancy 12 → 9, Theorem 7.1), §7.3 (change-of-basis interpretation), §7.4 (quaternion comparison + renormalization).

**Cycle:** 1 of 3.

**Sub-files:**
- `feedback_s7_cycle_1_reviewer_x.md` — formalism audit: `STATUS: GREEN` (2 Medium + 5 Low).
- `feedback_s7_cycle_1_reviewer_y.md` — narrative audit: `STATUS: AMBER` (2 Medium + 3 Low).

---

## Loop-termination read

**Under the severity ladder (Critical / High / Medium / Low), only Critical and High are loop-blocking.** Neither reviewer returned any Critical or High findings. Reviewer X's closing line is `STATUS: GREEN`; Reviewer Y's closing line is `STATUS: AMBER`, but strictly speaking her findings are all Medium and Low, so the cycle is *not loop-blocked* by either reviewer under the skill's protocol. The discrepancy is a labelling convention: Y uses `AMBER` to signal "worth another pass"; X uses `GREEN` when no C/H items remain. This is noted so the human can read both at face value.

---

## Reviewer X findings (formalism)

| ID | Severity | Location | Issue | Proposed patch |
|----|----------|----------|-------|----------------|
| `[S7-M-1]` | Medium | Theorem 7.1 | Omits "$R$ is a simplicial rotation" / "$R$ preserves $H$" as an explicit precondition. | Restate as "For $N = 4$, a simplicial rotation $R$ (Proposition 6.1), and a zero-sum input $P \in H$, …" |
| `[S7-M-2]` | Medium | §7.3 | "Picking three of the four simplicial basis vectors" is definitionally slightly wrong — $\{e_l, e_n, e_m\}$ are not in $H$; the actual basis is $\{e_l - e_p, e_n - e_p, e_m - e_p\}$. | Name the basis explicitly. |
| `[S7-L-1]` | Low | §7.2 | WLOG aside on which index is absorbed. | One-clause insertion (optional). |
| `[S7-L-2]` | Low | Theorem 7.1 | Storage cost lives in the table, not the theorem. | No change required (table is canonical). |
| `[S7-L-3]` | Low | §7.3 | "Computationally equivalent to $\mathrm{SO}(3)$" is stronger than warranted. | Soften to "same per-apply cost, conjugate via $V$". |
| `[S7-L-4]` | Low | §7.4 table | One-time quaternion→matrix conversion (~18 mults) not acknowledged. | Parenthetical near the table. |
| `[S7-L-5]` | Low | §7.4 renorm | "Columns of $R$ restricted to $H$" is slightly ambiguous. | Sharpen to "$H$-block of $R$, equivalently projections along $\mathbf{1}$". |

## Reviewer Y findings (narrative)

| ID | Severity | Location | Issue | Proposed patch |
|----|----------|----------|-------|----------------|
| `[Y-M-1]` | Medium | Theorem 7.1 | Theorem lacks a proof marker; statement gets swallowed by the surrounding prose. | Add a one-line "*Proof.* The construction of $\tilde{R}$ in §§7.1–7.2 supplies the explicit 9-multiplication algorithm. $\square$" |
| `[Y-M-2]` | Medium | §7.4 final paragraph | Post-patch wall of text: qualitative comparison + numerical drift + Gram–Schmidt recipe crowded together. | Split into two paragraphs: (i) structural differences (no $S^3$, no Hamilton products); (ii) floating-point drift + renormalization recipe. |
| `[Y-L-1]` | Low | §7.4 table | Quaternion multiplication counts lack a citation. | Cite Shoemake (or a standard 3D-math text). |
| `[Y-L-2]` | Low | §7.3 | Two sentences is rushed for a bridging subsection. | Add one bridging sentence. |
| `[Y-L-3]` | Low | §7.4 | Table footnote formatted as body text. | Either true footnote or integrate into prose. |

## Exemplary items (preserve)

Both reviewers flagged elements worth preserving through any future polish:

- Two-stage derivation of 16 → 12 → 9 exposed as two independent structural facts (X).
- Explicit $\tilde R_{ij} = R_{ij} - R_{ip}$ regrouping supports the "= 9" (not "≤ 9") claim (X).
- Table footnote separating per-apply cost from amortized renormalization cost (X, pre-`[Y-L-3]`).
- Post-patch §7.4 paragraph correctly names the non-orthonormality obstruction, rules out QR-on-$\tilde R$, and gives the correct lift-and-re-impose recipe (X).
- Preamble motivates the 9-mul kernel as the payoff to the "matching quaternion performance" narrative (Y).
- Narrative consistency with §1.2 item 5 and §9 on the "no $S^3$ double cover" claim is airtight (Y).

---

## Decision surface for the human

Under strict loop-termination rules, §7 Cycle 1 closes at GREEN (no Critical/High findings from either reviewer). Two paths forward:

**Option A — Accept Cycle 1 as closed, carry open findings into polish.**
Both Mediums from each reviewer become discretionary edits the Author handles in a subsequent pass (alongside the §8 / §9 / §10 review cycles and the pre-submission pass). Reviewer Y's AMBER label is noted but does not re-open the cycle.

**Option B — Run Cycle 2 to clear the Mediums.**
Address all four Mediums (`[S7-M-1]`, `[S7-M-2]`, `[Y-M-1]`, `[Y-M-2]`) in a single Author revision, then a short re-review. This would give a clean GREEN from *both* reviewers, which is the cleaner arXiv-ready state. The four Mediums are all surgical: one theorem-statement edit, one prose correction in §7.3, one "Proof." line, and one paragraph split. Low items can tag along at Author discretion.

Recommended: **Option B.** The four Mediums are cheap, genuinely improve the section, and leave §7 at the same zero-open-findings state as §§1–6 + Appendix D before we move to §8.
