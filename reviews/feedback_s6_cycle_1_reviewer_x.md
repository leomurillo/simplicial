# §6 + Appendix D — Reviewer X (Formalism), Cycle 1

**Scope:** `simplicial_vector_calculus.md` — §6 Properties of the Rotation Matrix (≈L379–397), Appendix C proofs backing Proposition 6.1 (≈L603–638), Appendix D Worked Example Computations (≈L641–686).

## Findings

### Critical

- **[F-C-1] Proposition 6.1(5) contradicts Proposition 6.1(9) and Appendix C.**  
  Item (5) states $\operatorname{tr} R = 1 + 2\cos\theta$. Item (9) lists eigenvalues $\{1, 1, e^{i\theta}, e^{-i\theta}\}$, whose sum is $2 + 2\cos\theta$. Appendix C computes $\operatorname{tr}(R) = 4 + (1-\cos\theta)\operatorname{tr}(K^2) = 2 + 2\cos\theta$ for the $4\times 4$ realisation. The value $1 + 2\cos\theta$ is the **classical trace of the planar/triple rotation on $H\cong\mathbb{R}^3$**, not the trace of the ambient $4\times 4$ lift. As written, (5) is false for the matrix $R$ defined in §5 unless “trace” is qualified.

### High

None, contingent on resolving **[F-C-1]** (the misstatement propagates to the **Trace** heading in Appendix C, L631, which announces $1+2\cos\theta$ while the displayed computation gives $2+2\cos\theta).

### Medium

- **[F-M-1] Metric preservation (item 8) — inner product.**  
  Item (8) writes $\langle RP, RQ\rangle = \langle P, Q\rangle$ without the $\langle\cdot,\cdot\rangle_s$ subscript. Elsewhere (Theorem 4.1, §4) the simplicial Gram pairing is the intrinsic one. Ambient orthogonality $R^\top R = I$ implies Euclidean preservation $P^\top Q$, but the simplicial form requires $R^\top G R = G$. Both hold for this $R$ (see §4 / Remark 3.2), but the proposition would read more precisely with the simplicial inner product named explicitly on both sides.

- **[F-M-2] Appendix C, determinant.**  
  The proof cites $\det\exp(\theta K)=\exp(\operatorname{tr}K)=1$. The manuscript’s $R$ is the **finite** Rodrigues polynomial, which agrees with $\exp(\theta K)$ when $K^3=-K$; the determinant step is correct but would be tighter if it cited that equality explicitly (optional polish).

### Low

- **[F-L-1] Appendix D.**  
  Arithmetic for $\tilde{K}$, $K$, $K^2$, and $R$ is consistent with Definition 3.1 and §5.4; the trace check matches $2+2\cos(2\pi/3)$. No issues found.

---

**Post-revision note (Author, Cycle 1):** **[F-C-1]** addressed in `simplicial_vector_calculus.md` — Proposition 6.1(5) and Appendix C **Trace** now align ($2+2\cos\theta$ vs.\ $1+2\cos\theta$ on $H$). **[F-M-1]** addressed via $\langle\cdot,\cdot\rangle_s$ and $R^\top G R = G$ in item (8).

**STATUS: GREEN**
