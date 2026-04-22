# §6 + Appendix D — Cycle 1 synthesis

**Scope:** §6 Properties of the Rotation Matrix; Appendix C (proofs of Proposition 6.1); Appendix D Worked Example Computations.

**Cycle:** 1 of 3 (terminated at **STATUS GREEN**).

## Reviewer X (formalism)

See `feedback_s6_cycle_1_reviewer_x.md`.

**Blocking finding:** **[F-C-1]** — Proposition 6.1(5) stated $\operatorname{tr} R = 1 + 2\cos\theta$, which contradicted item (9) and Appendix C ($2 + 2\cos\theta$ for the ambient $4\times 4$ matrix).

**Non-blocking:** **[F-M-1]** simplicial subscript on metric preservation; **[F-M-2]** optional tighter determinant bridge; **[F-L-1]** Appendix D numerics OK.

## Reviewer Y (narrative)

See `feedback_s6_cycle_1_reviewer_y.md`.

**Non-blocking:** **[N-M-1]** pointer to Appendix C; **[N-L-1]**–**[N-L-2]** optional polish.

---

## Author triage (Cycle 1)

| ID | Action |
|----|--------|
| **[F-C-1]** | **Resolved.** Proposition 6.1(5) now gives $\operatorname{tr} R = 2 + 2\cos\theta$ for the $4\times 4$ lift and states $\operatorname{tr}(R|_H)=1+2\cos\theta$ with one-line justification via $\mathbb{R}^4=\mathrm{span}\{\mathbf{1}\}\oplus H$. Appendix C **Trace** block retitled and the closing split $\operatorname{tr}(R)=1+\operatorname{tr}(R|_H)$ replaces the older “$\operatorname{tr}(R)-1$” shorthand that confused gauge vs. classical trace. |
| **[F-M-1]** | **Addressed.** Item (8) now uses $\langle\cdot,\cdot\rangle_s$ and cites $R^\top G R = G$. |
| **[N-M-1]** | **Addressed.** §6 opening: “Item-by-item proofs appear in Appendix C.” |

**Propagation check:** §5.4 worked-example trace line already reads $\operatorname{tr} R = 1 = 2 + 2\cos(2\pi/3)$ — consistent with the revised proposition. No further sweeps required.

---

**Termination:** Reviewer X **STATUS: GREEN** (Critical resolved). Reviewer Y **STATUS: GREEN**. Halt §6 + Appendix D loop; human sign-off on manuscript.

**Suggested follow-up (optional, not blocking):** Appendix C could expand the omitted “Hyperplane preservation, gauge-equivariance, metric preservation” line into two sentences using $G K = K G$ from Remark 3.2 — defer to pre-submission polish.
