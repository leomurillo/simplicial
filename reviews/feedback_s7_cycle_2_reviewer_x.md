# Reviewer X — Section 7 cycle-2 formalism verification pass

**Scope.** Verification pass on the four Cycle 1 Mediums (`[S7-M-1]`, `[S7-M-2]`, `[Y-M-1]`, `[Y-M-2]`) and the two Lows the Author elected to take (`[S7-L-3]`, `[Y-L-1]`) in §7 of `simplicial_vector_calculus.md` (lines ~403–449, plus References at ~537). Cycle 1 "ok" findings (the five Lows I flagged, the five `[V-*]` items, the proposal-level exemplary elements) are treated as baseline and not relitigated. The four Lows the Author deferred (`[S7-L-1]`, `[S7-L-2]`, `[S7-L-4]`, `[S7-L-5]`) are noted as open but out-of-scope for this pass.

## Verification of landed items

### `[S7-M-1]` — Theorem 7.1 precondition list — **RESOLVED**

New statement (line 427):

> *For $N = 4$, a simplicial rotation $R$ (Proposition 6.1), and a zero-sum input $P \in H$, the rotated point $RP$ can be computed using exactly 9 scalar multiplications.*

Verifications:

- The simplicial-rotation precondition is explicit: "$R$ is a simplicial rotation (Proposition 6.1)". Proposition 6.1 (line 387) enumerates nine structural properties of $R(u,\theta)$, including item 6 (hyperplane preservation) — the exact property that §7.1 invokes to derive the 16 → 12 step — and item 2 / item 7 (gauge fixation / gauge equivariance). Citing the proposition as a whole is appropriate: the theorem uses 6.1(6) directly, and the other items define what "simplicial rotation" even means in this paper (the object produced by Rodrigues in §5).
- The zero-sum precondition "$P \in H$" is explicit.
- "$N = 4$" is explicit. (Strictly this is also redundant with "(Proposition 6.1)", since Proposition 6.1 is an $N = 4$ statement, but this is belt-and-braces, consistent with how Theorem 7.1 was originally staged.)
- Statement is self-contained: a reader reading Theorem 7.1 cold now knows (i) the dimension, (ii) the input constraint, (iii) the operator constraint, and can follow the Prop 6.1 back-pointer if they need the full structural content of "simplicial rotation".

Matches the exact phrasing my Cycle 1 patch suggested. Resolved.

### `[Y-M-1]` — Theorem 7.1 proof marker — **RESOLVED**

New proof block (line 429):

> *Proof.* The reductions of §§7.1–7.2 exhibit an explicit 9-multiplication algorithm: three dot products of length 3 (nine multiplications in total) compute $(RP)_i$ for $i \in \{l, n, m\}$ via the reduced matrix $\tilde{R}_{ij} = R_{ij} - R_{ip}$, and $(RP)_p$ is recovered by negation at no multiplicative cost. $\square$

Verifications:

- **House-style conformance.** Uses the `*Proof.*` ... `$\square$` marker pair. Sampling the manuscript: line 255 (Theorem 3.6 proof body), line 555 (Proposition A.1 in Appendix A). Both use the identical convention. Appendices B, C, D also use this pair (spot-checked in Cycle 1). The new §7 block matches.
- **Mathematical content.** The proof names both ingredients of the reduction:
  1. "Three dot products of length 3 … compute $(RP)_i$ for $i \in \{l, n, m\}$ via $\tilde{R}_{ij} = R_{ij} - R_{ip}$": this is exactly §7.2's construction, where $(RP)_i = \sum_{j \in \{l,n,m\}} \tilde R_{ij} P_j$ with $\tilde R$ defined as stated. $3 \times 3 = 9$ multiplications.
  2. "$(RP)_p$ is recovered by negation at no multiplicative cost": exactly §7.1's $(RP)_p = -[(RP)_l + (RP)_n + (RP)_m]$, which uses three additions and one sign flip, zero multiplications.
- **Coverage of all four output coordinates.** The theorem asserts a cost for computing $RP$ (all four components). The proof covers $\{l, n, m\}$ (9 mults) and $p$ (0 mults); total 9 for all four. ✓
- **"Exactly" vs. upper-bound.** The theorem says "can be computed using exactly 9 scalar multiplications". Read as "exhibiting an explicit algorithm with mult-count 9"; the proof discharges this existential. It is *not* a lower-bound/optimality claim, and the proof correctly does not attempt one. Consistent with Cycle 1 treatment.
- **Reviewer Y's minimal suggestion was a one-line "see §§7.1–7.2" pointer.** The Author's block is a bit expanded (actually naming the two ingredients rather than pointing at them) — this is better, not worse, for a formalism reader. Y's concern was narrative: the theorem gets swallowed without a proof marker. Both readings — her narrative concern and my formalism concern that a theorem should have a discharging proof — are satisfied.

Resolved.

### `[S7-M-2]` — §7.3 basis phrasing — **RESOLVED**

New prose (line 433):

> …it is the restriction $R|_H$ expressed in the (non-orthonormal) basis $\{e_l - e_p,\; e_n - e_p,\; e_m - e_p\}$ of $H$ — where $e_i$ denotes the $i$-th standard coordinate vector of $\mathbb{R}^4$ — obtained by dropping the $e_p$ coordinate and re-expressing $e_p = -(e_l + e_n + e_m)$ via the zero-sum constraint.

Verifications:

- **Is $\{e_l - e_p,\, e_n - e_p,\, e_m - e_p\}$ a basis of $H$?**
  - Each vector is in $H$: the coordinate sum is $1 - 1 = 0$. ✓
  - Linear independence: a null combination $\sum_i \alpha_i (e_i - e_p) = 0$ forces the $e_l, e_n, e_m$ coefficients to vanish ($\alpha_l = \alpha_n = \alpha_m = 0$), hence also the $e_p$ coefficient. ✓
  - Dimension: $\dim H = N - 1 = 3$ matches three basis vectors. ✓
- **Coordinates match the reduction.** For $P \in H$ with $P_p = -(P_l+P_n+P_m)$,
  $$P = P_l(e_l - e_p) + P_n(e_n - e_p) + P_m(e_m - e_p),$$
  so $(P_l, P_n, P_m)$ are the coordinates of $P$ in this basis. $\tilde R$ is then exactly the matrix of $R|_H$ in this basis: $(RP)_i = \sum_{j \in \{l,n,m\}} \tilde R_{ij} P_j$ for $i \in \{l,n,m\}$, and the $p$-coordinate of $RP$ is determined by the zero-sum of $RP$. ✓
- **Non-orthonormality preserved from Cycle 1 text.** The qualifier "(non-orthonormal)" is kept, matching my Cycle 1 verification: in this basis the Gram block is $\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}$ (Euclidean) or $\tfrac{4}{3}$ times that ($G$-), neither proportional to identity. ✓
- **Notation coexistence with §2.5.** §2.5 uses $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ (bold, numerically indexed) for the ambient $\mathbb{R}^3$ Cartesian basis, and $\mathbf{v}_1, \ldots, \mathbf{v}_4$ (bold) for the simplicial vertex vectors in $\mathbb{R}^3$. §7.3 now uses $e_l, e_n, e_m, e_p$ (unbold, letter-indexed) for the $\mathbb{R}^4$ standard coordinate vectors, with an explicit inline definition at first use. Three discriminators keep the symbols distinct on the page: (1) boldness ($\mathbf{e}$ vs. $e$); (2) index type (numeric 1,2,3 vs. letter $l,n,m,p$); (3) ambient space ($\mathbb{R}^3$ vs. $\mathbb{R}^4$). In practice $\mathbf{e}_i$ and $e_j$ cannot collide on a specific symbol (no one writes $\mathbf{e}_l$ or $e_1$ in either section). Acceptable. (See `[S7-C2-L-1]` below for a very mild observation.)
- **"Dropping the $e_p$ coordinate and re-expressing $e_p = -(e_l + e_n + e_m)$ via the zero-sum constraint."** This is the exact procedural phrasing my Cycle 1 patch recommended. As a vector identity in $\mathbb{R}^4$ the equation $e_p = -(e_l+e_n+e_m)$ is not literally true (the standard basis vectors are independent), but the phrasing is a standard mnemonic for the substitution $P_p \mapsto -(P_l+P_n+P_m)$ applied inside a zero-sum coordinate expression — equivalently, a statement in the quotient $\mathbb{R}^4 / \mathrm{span}(\mathbf{1})$. Since I endorsed this phrasing in Cycle 1 and the surrounding sentence makes the "procedural" reading clear ("obtained by dropping … and re-expressing … via the zero-sum constraint"), I do not re-raise this.

Resolved.

### `[S7-L-3]` — Softened SO(3) comparison — **RESOLVED**

New text (tail of line 433):

> …rotation in the simplicial system has the same per-apply cost as $\mathrm{SO}(3)$ acting on $\mathbb{R}^3$, to which it is conjugate via the hyperplane isometry $V$ of §2.5.

Verifications:

- "Same per-apply cost" is a precise, factual claim. Simplicial apply via $\tilde R$: 9 mults (Theorem 7.1). $\mathrm{SO}(3)$ apply via stored $3 \times 3$ matrix: 9 mults. Equal. ✓ — "Same per-apply cost" is now exactly what is said, not the stronger "computationally equivalent".
- "To which it is conjugate via the hyperplane isometry $V$ of §2.5." Verified at the structural level: §2.5 (line 170) establishes $V\colon H \to \mathbb{R}^3$ as the orientation- and metric-preserving isometry, with the intertwining $V K(u) V^{-1} = [Vu]_\times$. Exponentiating both sides: $V R(u,\theta)|_H V^{-1} = V \exp(\theta K(u))|_H V^{-1} = \exp(\theta [Vu]_\times) \in \mathrm{SO}(3)$. Hence $R|_H$ and the classical $\mathrm{SO}(3)$ rotation about $Vu$ by $\theta$ are conjugate via $V$. ✓
- The wording is clean, matches my Cycle 1 suggested softening verbatim, and aligns with the external-cycle-1 `[B6]` framing that rotation operators in this work are carried to their $\mathbb{R}^3$ counterparts under $V$.

Resolved.

### `[Y-L-1]` — Shoemake citation + References propagation — **RESOLVED**

Narrative edit (line 437):

> Standard quaternion rotation pipelines offer two pathways to apply a rotation to a point (the multiplication counts below follow [Shoemake] and are standard in the computer graphics literature):

References entry (line 537):

> [Shoemake] Shoemake, K. "Animating Rotation with Quaternion Curves." *Computer Graphics (SIGGRAPH '85 Proceedings)* 19(3), 245–254 (1985).

Verifications:

- **Citation is appropriate.** Shoemake (1985) is the canonical reference for the quaternion-to-matrix conversion and the quaternion sandwich operation count in the computer-graphics literature. The hedge "and are standard in the computer graphics literature" covers the 15–18 per-apply spread on the quaternion sandwich that I noted in Cycle 1.
- **Alphabetical placement.** References-list ordering in the relevant window (lines 535–541): `[Pawlowsky-Glahn-Egozcue]` → `[Shoemake]` (new) → `[Spivak]` → `[Thomson]` → `[Urner]`. "Pawlowsky…" < "Shoemake" < "Spivak" alphabetically. ✓ Placement correct. ✓
- **No duplicate entry.** Only one `[Shoemake]` line in the References. ✓

Resolved.

### `[Y-M-2]` — §7.4 paragraph split — **RESOLVED**

Verified by direct read: line 447 now ends at "Hamilton products." and line 449 begins with "As with any matrix representation…". Paragraph boundary is at the exact position Reviewer Y requested. Content on either side is unchanged modulo the break. No formalism impact either way; noted for completeness.

Resolved.

## New findings introduced by the Cycle 2 edits

None at Critical / High / Medium severity.

- **`[S7-C2-L-1]` (Low).** *Notation: $e_i$ vs. $\mathbf{e}_i$ in close visual proximity.* The paper uses $\mathbf{e}_i$ (bold, $i \in \{1,2,3\}$) in §2.5 for the ambient $\mathbb{R}^3$ Cartesian basis, and now $e_i$ (unbold, $i \in \{l,n,m,p\}$) in §7.3 for the $\mathbb{R}^4$ standard coordinate vectors. The three discriminators (boldness, index type, ambient space) keep them unambiguous in practice, and the §7.3 inline definition makes the usage self-contained. Purely a nitpick, no change required; if the LaTeX conversion pass tightens notation conventions, a one-line entry in a "Notation" preamble (or in §1.3 / §2.5) stating explicitly "$\mathbf{e}_i \in \mathbb{R}^3$ (Cartesian basis, §2.5); $e_i \in \mathbb{R}^4$ (standard coordinate vector, §7.3)" would make the coexistence a one-line cross-check for the reader. Non-blocking.
- **`[S7-C2-L-2]` (Low).** *Mild redundancy in the Theorem 7.1 proof block.* "Three dot products of length 3 (nine multiplications in total)" states the count twice — once structurally ($3 \times 3$) and once numerically (nine). Either formulation alone would discharge the proof; both together are belt-and-braces. Not a finding worth acting on mid-cycle, but could be tightened to "three dot products of length 3" or "a total of nine multiplications" in a future polish. Non-blocking.

I also spot-checked for:

- **Dangling references to the pre-edit prose.** None. The pre-edit Theorem 7.1 statement, the pre-edit §7.3 basis sentence ("picking three of the four simplicial basis vectors"), the pre-edit §7.3 SO(3) comparison ("computationally equivalent to SO(3)"), and the pre-edit §7.4 paragraph are all consistently replaced; no other section of the manuscript references the old wording. ✓
- **Cross-reference integrity.** Theorem 7.1 now cites Proposition 6.1 (line 387 — present, correctly formed). §7.3 now cites §2.5 (line 163 — present). §7.4 now cites [Shoemake] (line 537 — present). No broken cross-references. ✓
- **Proof-marker house style.** Verified against lines 255 (Theorem 3.6 proof), 555 (Proposition A.1 proof), and the Appendices B/C/D proof blocks sampled in Cycle 1. `*Proof.*` / `$\square$` pair is the consistent convention; the Theorem 7.1 proof matches. ✓
- **Alphabetization of the References list near the new entry.** Already verified above.

## Summary of findings

- Critical: none.
- High: none.
- Medium: none. All four Cycle 1 Mediums (`[S7-M-1]`, `[S7-M-2]`, `[Y-M-1]`, `[Y-M-2]`) are resolved, at the exact fixed point indicated in Cycle 1 or better.
- Low (new, non-blocking): `[S7-C2-L-1]`, `[S7-C2-L-2]`.
- Low (deferred from Cycle 1, out of scope for this verification pass): `[S7-L-1]`, `[S7-L-2]`, `[S7-L-4]`, `[S7-L-5]`.

### Cycle 1 Lows — status

- `[S7-L-3]` — softened SO(3) comparison: **landed**, verified above.
- `[S7-L-1]`, `[S7-L-2]`, `[S7-L-4]`, `[S7-L-5]` — Author-deferred per triage record. I agree with the deferral; none is formalism-blocking, and the Author's rationale in the triage matches my Cycle 1 characterization of each as "not required" / "non-blocking" / "stylistic".

§7 is formalism-ready: no residual Critical/High/Medium findings, and the two new Lows are cosmetic polish that can ride into the LaTeX-conversion pass.

STATUS: GREEN
