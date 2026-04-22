# Reviewer X — Section 7 cycle-1 formalism audit

**Scope.** Fresh audit of §7 "Computational Kernel: The 9-Multiplication Apply" (preamble; §7.1 output redundancy; §7.2 input redundancy and Theorem 7.1; §7.3 change-of-basis reading; §7.4 comparison table plus post-patch renormalization paragraph). Dependencies spot-checked: Proposition 6.1(6) (hyperplane preservation), Proposition 6.1(7) (gauge equivariance), Remark 3.2(1), and the §2.5 isometry $V$. The `[V-L-1]` / `[V-L-2]` items closed in `feedback_external_cycle_1_verify_reviewer_x.md` and the subsequent spot-patches are treated as the baseline and not relitigated.

## Preamble (line 405)

- The count "16 scalar multiplications" for a direct apply of a generic $4\times4$ matrix to a 4-vector is exact (four rows × four mults per dot product). The parallel claim of "12 additions" is not made in the text but is implicit and correct. No finding.
- "…matching the per-apply cost of the quaternion-to-matrix rotation pipeline in graphics applications." Consistent with the §7.4 table row; fair framing.

## §7.1 Output redundancy (16 → 12)

I walked through the reduction:

- "$P \in H \Rightarrow RP \in H$ by Proposition 6.1 item 6": the cited item 6 is exactly the hyperplane-preservation clause of Proposition 6.1. Pointer is correct.
- "three dot products of length 4 = 12 multiplications": $3 \times 4 = 12$, correct.
- $(RP)_p = -[(RP)_l + (RP)_n + (RP)_m]$: follows from $(RP)_l+(RP)_n+(RP)_m+(RP)_p = 0$. Correct; three additions + one negation, zero multiplications.

No finding.

## §7.2 Input redundancy (12 → 9) and Theorem 7.1

Substitution check. With $P_p = -(P_l + P_n + P_m)$:

$$(RP)_i = \sum_{j\in\{l,n,m\}} R_{ij}P_j + R_{ip}(-(P_l+P_n+P_m)) = \sum_{j\in\{l,n,m\}}(R_{ij}-R_{ip})P_j.$$

So $\tilde R_{ij} = R_{ij} - R_{ip}$ is correct. Cost: 3 mults × 3 rows = 9, exact (not approximate). The claim "the fourth output coordinate is recovered by negation at no multiplicative cost" is precisely correct (zero multiplicative operations; three additions and one sign flip).

- **`[S7-M-1]` (Medium).** *Theorem 7.1, precondition list.* The theorem currently reads "For $N = 4$ and a zero-sum input $P \in H$, the rotated point $RP$ can be computed using exactly 9 scalar multiplications." It does not record that $R$ must be a simplicial rotation (equivalently, that $R$ preserves $H$), which is what makes the output-side 16 → 12 step in §7.1 go through via Proposition 6.1(6). In context the standing assumption is obvious — §6 defines $R$, §7.1 explicitly invokes 6.1(6) — but a self-contained theorem statement is cheap and formally preferable. Suggested patch: "For $N = 4$, a simplicial rotation $R$ (Proposition 6.1), and a zero-sum input $P \in H$, the rotated point $RP$ can be computed using exactly 9 scalar multiplications."

- **`[S7-L-1]` (Low).** *Choice of absorbed index.* The reduction picks index $p$ to absorb via the zero-sum constraint. Any of the four indices can play that role and all four choices yield the same linear map $R|_H$ (in different bases), so the theorem's count is independent of the choice. A one-clause aside ("for any choice of index to absorb; WLOG $p$") would remove the appearance of a distinguished index but is not required — the formulas fix the choice explicitly.

- **`[S7-L-2]` (Low).** *Storage cost in theorem statement.* The theorem states only the per-apply mult count. The table in §7.4 records storage (9 entries for $\tilde R$) separately. Keeping storage out of the theorem is defensible (theorem = multiplicative kernel cost; table = storage + apply cost). No change required.

## §7.3 Interpretation as a change of basis

I verified the change-of-basis reading algebraically:

- For $P \in H$, writing $P_p = -(P_l+P_n+P_m)$ gives $P = P_l(e_l - e_p) + P_n(e_n - e_p) + P_m(e_m - e_p)$, so $(P_l, P_n, P_m)$ are the coordinates of $P$ in the basis $B := \{e_l - e_p,\, e_n - e_p,\, e_m - e_p\}$ of $H$.
- Each vector in $B$ is in $H$, and $\dim H = 3$; the three vectors are linearly independent (direct check), so $B$ is indeed a basis of $H$.
- Expressing $R|_H$ in $B$: for $i \in \{l,n,m\}$, $(RP)_i = \sum_j \tilde R_{ij} P_j$ with $\tilde R_{ij} = R_{ij} - R_{ip}$, which is exactly the matrix of $R|_H$ in basis $B$. ✓
- $B$ is not orthonormal (either Euclidean or $G$-): e.g., $\|e_l - e_p\|_E^2 = 2$, $\langle e_l - e_p, e_n - e_p\rangle_E = 1$, so the hyperplane Gram block in this basis is $\begin{pmatrix}2 & 1 & 1\\ 1 & 2 & 1\\ 1 & 1 & 2\end{pmatrix}$ and thus not proportional to identity. Consistent with the paper's "non-orthonormal" qualifier. ✓

- **`[S7-M-2]` (Medium).** *"Three of the four simplicial basis vectors" as a basis of $H$.* Taken literally, $\{e_l, e_n, e_m\}$ are not vectors in $H$ (they are not zero-sum), so "picking three of the four simplicial basis vectors" is not by itself a basis of $H$ — it is a basis of a coordinate 3-plane in $\mathbb{R}^4$ that is not $H$. The correct basis of $H$ reached by "absorbing $e_p$ via the zero-sum constraint" is $B = \{e_l - e_p,\, e_n - e_p,\, e_m - e_p\}$ (or any of the four analogues obtained by picking a different absorbed index). The intent is clear from the $\tilde R_{ij} = R_{ij} - R_{ip}$ formula, so a reader who chases the algebra will not be misled, but the prose sentence as stated is definitionally slightly wrong. Suggested patch: replace "…obtained by picking three of the four simplicial basis vectors and absorbing the fourth into the zero-sum constraint" with something like "…namely $\{e_l - e_p,\, e_n - e_p,\, e_m - e_p\}$, obtained by dropping the $e_p$ coordinate and re-expressing $e_p = -(e_l + e_n + e_m)$ via the zero-sum constraint."

- **`[S7-L-3]` (Low).** *"Computationally equivalent to $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$".* The intended sense — "same per-apply cost as $\mathrm{SO}(3)$ on $\mathbb{R}^3$, and moreover conjugate to it via the isometry $V$ of §2.5" — is correct but the phrase "computationally equivalent" is stronger than "same per-apply cost" in the usual reading, and is not formally defined in the paper. Suggested softening: "has the same per-apply cost (9 multiplications) as $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$, to which it is conjugate via the hyperplane isometry $V$ of §2.5."

## §7.4 Comparison table and discussion

Row-by-row:

- "Quaternion sandwich $q v q^{-1}$ … ~15": published optimized counts cluster in the 15–18 range (e.g., the $v + 2q_0(q_v\times v) + 2q_v\times(q_v\times v)$ form yields ~18; further factoring of the shared cross product drops this). Naïve two-quaternion-product evaluation runs ~28. The "~" hedge covers this spread; the figure is fair.
- "Quaternion → $3\times 3$ matrix, then apply: 4+9 derived, 9": storage of 4 (quaternion) + 9 (derived matrix), per-apply 9. The one-time conversion cost (~15–18 mults) is not listed because the table explicitly reports "per apply"; the footnote following the table (*"per-apply cost only; periodic re-orthogonalization…"*) covers the same cost-separation principle. Accurate.
- "Intrinsic simplicial: 9, 9": storage of 9 for the full $\tilde R$, per-apply of 9. Correct.

- **`[S7-L-4]` (Low).** *One-time conversion acknowledgment.* The "quaternion → $3\times 3$ matrix, then apply" row compares cleanly to the simplicial row on per-apply cost only; a reader optimizing a single-rotation-applied-once workload (rather than many applies from one stored rotation) would need to account for the ~15–18 conversion mults on the first row. The footnote about "periodic re-orthogonalization under repeated composition" addresses the amortization story but not the one-time build cost. A one-line parenthetical next to the table (e.g., "quaternion-to-matrix conversion adds a one-time ≈ 18 mults, amortized over repeated applies") would close this transparency gap. Non-blocking.

### Renormalization paragraph (post-`[V-L-1]` spot-patch)

The patched text reads: "via a Gram–Schmidt pass on the hyperplane block of $R$ (equivalently, standard Euclidean Gram–Schmidt applied to the columns of $R$ restricted to $H$, since the simplicial inner product reduces to a constant rescaling of the ambient Euclidean inner product on $H$)."

I verified the "constant rescaling" claim arithmetically:

- $G = \tfrac{4}{3} I_4 - \tfrac{1}{3} J$ with $J = \mathbf{1}\mathbf{1}^\top$. For $c \in H$, $Jc = 0$, so $Gc = \tfrac{4}{3} c$ and $\langle c, c'\rangle_G = \tfrac{4}{3}\, c^\top c'$. Hence $G|_H = \tfrac{4}{3} I_H$, a pure rescaling.
- $G$-unit and Euclidean-unit on $H$ differ by a factor of $\sqrt{3/4}$ per vector, so Gram–Schmidt in either inner product produces orthogonal systems that coincide up to this global scaling of each output vector — in particular, $G$-orthogonality and Euclidean-orthogonality coincide on $H$. The claim is accurate.

The patch cleanly sidesteps the singularity of $G$ on $\operatorname{span}(\mathbf{1}) \subset \mathbb{R}^4$ flagged in `[V-L-1]` by restricting the inner-product operation to $H$.

- **`[S7-L-5]` (Low).** *"The columns of $R$ restricted to $H$".* Slightly ambiguous: the phrase can be parsed as (a) the columns of $R|_H$ represented in some basis of $H$, or (b) the columns of the $4\times 4$ $R$ each projected onto $H$ along $\operatorname{span}(\mathbf{1})$. Because $R$ preserves the orthogonal decomposition $\mathbb{R}^4 = \mathbb{R}\mathbf{1} \oplus H$, the two readings produce the same $H$-valued vectors (modulo the representation choice). The intent is clear and the result is the same under either reading; the sentence could be sharpened to "…Euclidean Gram–Schmidt applied to the columns of the $H$-block of $R$ (equivalently, to the projections of the columns of $R$ onto $H$ along $\mathbf{1}$)", but this is purely stylistic.

## Cross-dependency spot-checks

- **Proposition 6.1(6)** as cited from §7.1: correct pointer (the item is the hyperplane-preservation clause). No regression vs. its proof in §6.
- **$\tilde R$ definition** internal consistency: $\tilde R_{ij} = R_{ij} - R_{ip}$ with $i,j \in \{l,n,m\}$ is well-posed and well-defined given $R$; there is no circular dependence on §7.3 (which reinterprets $\tilde R$ rather than defining it).
- **Well-definedness of "the reduced apply as a map on coordinate triples":** the map $(P_l, P_n, P_m) \mapsto ((RP)_l, (RP)_n, (RP)_m)$ is $\tilde R$; because $R|_H$ is a bijection of $H$ and $B$ is a basis of $H$, $\tilde R$ is invertible ($\tilde R \in \mathrm{GL}_3(\mathbb{R})$, and further $\det \tilde R = +1$ matches $\det R|_H$), but invertibility is not needed for Theorem 7.1 and is correctly left implicit.
- **No hidden assumption on the axis $u$.** The 9-mul reduction depends only on (i) $R$ preserving $H$ and (ii) $P \in H$; it is agnostic about the axis, angle, or genericity of $u$. No precondition gap.

## Exemplary elements (preserve these)

Noted so the Author knows what *not* to disturb in subsequent polish:

- The two-stage derivation (output redundancy in §7.1, then input redundancy in §7.2) is cleanly staged, with the reduction from 16 to 12 to 9 exposed as two genuinely independent structural facts (hyperplane preservation on output, zero-sum substitution on input) rather than as a single black-box trick.
- The algebraic substitution in §7.2 shows the $\tilde R_{ij} = R_{ij} - R_{ip}$ regrouping explicitly rather than asserting it, which is exactly what a formalism reviewer wants for a "= 9" (not "≤ 9") claim.
- §7.4 now separates the per-apply cost (table body) from the amortized renormalization cost (footnote) — this pre-empts a common source of confusion when comparing against quaternion pipelines.
- The post-patch §7.4 renormalization paragraph handles the non-orthonormality of $\tilde R$ correctly: it names the obstruction ($\tilde R^\top \tilde R \neq I_3$), rules out the wrong fix (QR/GS on $\tilde R$ alone), and specifies the correct recipe (lift to the $4 \times 4$ $R$, re-impose $R^\top R = I$ and $R\mathbf{1} = \mathbf{1}$).
- The "~15" hedge in the quaternion-sandwich row, rather than a single citation-specific integer, is the correct calibration for a quantity whose published value varies with implementation.

## Summary of findings

- Critical: none.
- High: none.
- Medium: `[S7-M-1]` (Theorem 7.1 preconditions); `[S7-M-2]` (§7.3 basis phrasing).
- Low: `[S7-L-1]`, `[S7-L-2]`, `[S7-L-3]`, `[S7-L-4]`, `[S7-L-5]`.

STATUS: GREEN
