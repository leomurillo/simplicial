# Reviewer X — Front-Matter Harmonization Audit (Cycle 1)

**Scope.** `simplicial_vector_calculus.md` lines 1–77 (Title, Abstract, Keywords, MSC 2020, "Note on the Use of AI Tools," §1 Introduction §§1.1–1.3).
**Context.** §§3–9 are all GREEN. This is a harmonization pass between the final body and the front matter.
**Spot-checks performed against the current body.** §2.4 lines 139–161; §3.1 line 207 / §3.2 Def 3.1 line 217 / Theorem 3.3 line 243; §4 Theorem 4.1 lines 279–285 and Remark 4.2 line 291; §5 eq (5.1) line 325 and §5.3 line 355; §6 Proposition 6.1 lines 387–398; §7.1–7.4 lines 407–449; §8.1–8.2 lines 457–469; §9 opening paragraph lines 489–493.
**Open issue of record read in:** `[L-2-1]` in `reviews/open-issues.md`.

## Overall STATUS: AMBER

- **Critical:** 0
- **High:** 0
- **Medium:** 4
- **Low:** 7

The Abstract and §1 are close to body-consistent after the Cycle 3 spot-patch, but four harmonization gaps remain (hedge-wording regression in the Abstract, the deferred one-slot shorthand in §1.2 item 3, an `autonomous presentation` framing gap in §1.3, and Keywords/MSC coverage of the paper's central constructs). None invalidates a proof. None is blocking in the sense of §§3–9 re-verification. All four are appropriate to close in the current §1 harmonization pass.

---

## Medium findings

### [F1-M-1] Abstract line 21 "unique case" is missing the within-framework hedge (regression of the `[S9-M-2]` pattern)
- **Location.** Abstract, line 21.
- **Current wording.** "We identify $N = 4$ as the unique case in which the construction yields a binary cross product and closed-form exponential, a reflection of the exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$."
- **Body comparanda.**
  - §1.2 item 6 (line 61): *"Within the simplicial / Hodge-dual / axis-to-skew-operator framework developed here*, we identify $N = 4$ as the unique case …"
  - §8.1 (line 463): "The uniqueness of $N = 4$ for a binary cross product with closed-form exponentiation *within the simplicial wedge–Hodge framework developed here* …"
  - §9 (line 493): "The $N = 4$ case is distinguished, *within the simplicial wedge–Hodge framework developed here*, by the coincidence $\dim \mathfrak{so}(3) = 3$ …"
- **Finding.** The body canonicalizes a within-framework hedge on the uniqueness claim (to disclaim the octonionic $n = 7$ binary cross product, which is explicitly acknowledged in §1.2 item 6 and §8.1). The Abstract drops the hedge and reads as an unqualified uniqueness statement. The Abstract is the surface most readers encounter first; the drift here is exactly the regression pattern that was caught and patched as `[S9-M-2]` in §9 Cycle 1.
- **Recommendation.** Insert the canonical hedge — matching §8.1 / §9 wording — into the Abstract:
  > "We identify $N = 4$ as the unique case *within the simplicial wedge–Hodge framework developed here* in which the construction yields a binary cross product and closed-form exponential, a reflection of the exceptional Lie-algebra isomorphism $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$; see §1.2 item 6 and §8.1 for the interaction with Eckmann's classification and the octonionic $n=7$ case."

### [F1-M-2] §1.2 item 3 still carries the one-slot shorthand; `[L-2-1]` is due
- **Location.** §1.2 item 3, line 53. Open issue: `[L-2-1]` in `reviews/open-issues.md`.
- **Current wording.** "… the inner product is gauge-invariant as a scalar (values unchanged under $x \mapsto x + t\mathbf{1}$) …"
- **Body comparanda.**
  - Theorem 4.1(1), line 281: "$\langle a + k\mathbf{1},\, b + m\mathbf{1} \rangle = \langle a, b \rangle$ for all $a, b \in \mathbb{R}^N$ and all $k, m \in \mathbb{R}$."
  - §2.4 line 155: "$\langle a + k\mathbf{1},\, b + m\mathbf{1}\rangle = \langle a, b\rangle$ … confirming that the inner product descends to the quotient."
  - §9 opening, line 489: "gauge-invariant in both arguments."
- **Finding.** The one-slot shorthand was logged as a Low at §4 Cycle 2 and deferred "to next §1 pass or §10 pre-submission sweep." This IS the next §1 pass. The two-slot form is required for descent to the quotient and is the formulation used in the theorem, the §2.4 derivation, and the §9 summary.
- **Recommendation.** Replace the parenthetical with either:
  > "… the inner product is gauge-invariant as a scalar (values unchanged under $a \mapsto a + k\mathbf{1}$, $b \mapsto b + m\mathbf{1}$ in either argument) …"

  or the verbatim Theorem 4.1(1) form:
  > "… the inner product is gauge-invariant as a scalar in both arguments ($\langle a + k\mathbf{1}, b + m\mathbf{1}\rangle = \langle a, b\rangle$) …".

  After this edit, `[L-2-1]` can be marked **RESOLVED** in `reviews/open-issues.md`.

### [F1-M-3] Abstract "unit vector" qualifier is under-specified relative to Def 3.1 / Theorem 3.3
- **Location.** Abstract item 2, line 18.
- **Current wording.** "… the Lie-algebraic identity $K^3 = -K$ when the axis $u$ is a unit vector."
- **Body comparanda.**
  - §3.2 Definition 3.1, line 217: "a zero-sum unit axis $u = (u_l, u_n, u_m, u_p)$ (i.e. $\sum u_i = 0$ and $\tfrac{4}{3}\sum u_i^2 = 1$)."
  - §3.2 Remark 3.2 item 2, line 237: "the identity $K(u)^3 = -K(u)$ … rely on the unit-axis normalization $\tfrac{4}{3}\sum u_i^2 = 1$ and on $\sum u_i = 0$."
  - Theorem 3.3, line 243: "For any zero-sum unit axis $u$ …"
- **Finding.** The Abstract collapses two distinct conditions — *zero-sum* and *unit simplicial norm* — into one undifferentiated "unit vector" descriptor. Both conditions are needed for $K^3 = -K$. The linear extension of $K$ to all of $\mathbb{R}^4$ (Remark 3.2) satisfies $K(\mathbf{1}) = 0$ but does *not* satisfy $K^3 = -K$ for non-zero-sum "unit" inputs. An Abstract reader taking "unit vector" at face value would fall out of the theorem's actual hypotheses.
- **Recommendation.** Use "zero-sum unit axis" (matches Def 3.1 exactly) or spell out both conditions:
  > "… the Lie-algebraic identity $K^3 = -K$ when $u$ is a zero-sum unit axis (i.e. $\sum u_i = 0$ and $\tfrac{4}{3}\sum u_i^2 = 1$)."

### [F1-M-4] §1.3 is silent on the "autonomous *presentation*" framing used as the §9 headline
- **Location.** §1.3 (terminological notes), lines 63–75.
- **Current wording.** §1.3 explicitly retires "native," reserves "*intrinsic*" per §1.2 item 3, and explains "simplicial coordinates / Quadray / zero-sum hyperplane." It does not mention "autonomous presentation."
- **Body comparanda.**
  - Remark 4.2, line 291: "The simplicial (Quadray) description of 3D Euclidean space thereby supports an autonomous *presentation* of this algebraic layer of vector calculus, in the sense made precise in §9."
  - §9 opening, line 489: "The simplicial (Quadray) coordinate system supports an autonomous *presentation* of the algebraic layer of 3D Euclidean vector calculus …".
- **Finding.** "Autonomous *presentation*" is the load-bearing framing of both §4 Remark 4.2 and the §9 opening. §1.3 defines which descriptors are in use (intrinsic yes, native no) but does not anchor this third descriptor even though it is the Conclusion's principal word.
- **Recommendation.** Add one sentence to §1.3 that previews "autonomous presentation" and its relation to "intrinsic":
  > "Section 4 and the Conclusion additionally describe the resulting calculus as an *autonomous presentation* of the algebraic layer of 3D Euclidean vector calculus: *autonomous* in the sense that, once the simplicial Gram data of §2 is fixed, the construction proceeds without recourse to a Cartesian frame; *presentation* rather than "theory" because it is isometric to the classical Cartesian theory via the hyperplane isometry $V$ of §2.5."

---

## Low findings

### [F1-L-1] Abstract stylistic: two consecutive `admits` in line 21
Stylistic only. Vary the second verb, e.g. "For $N \geq 5$, the analogous construction *proceeds* via Hodge duals of wedge products of arity $N-3$, which we leave to future work."

### [F1-L-2] Abstract $R$ vs $R(u,\theta)$, $K$ vs $K(u)$ argumentless-display (line 19)
Argumentless compression is standard in Abstracts. Log only. If the authors prefer symbol parity with §5/§9, write the display as $R(u,\theta) = I + \sin\theta\, K(u) + (1-\cos\theta)\, K(u)^2$.

### [F1-L-3] §1.2 item 5 "without requiring" borderline-reads as a superiority claim
- **Current.** "matches the performance of the quaternion-to-matrix pathway without requiring the $S^3$ double cover."
- **Comparanda.** §7.4 "does not involve the $S^3$ double cover"; §9 "matching quaternion-to-matrix performance without invoking the $S^3$ double cover."
- **Recommendation.** Swap "without requiring" → "without invoking" for verbatim parity with §9. Single-token harmonization.

### [F1-L-4] §1.2 item 6 hedge wording vs canonical §8.1/§9 phrasing
- **Current.** "*Within the simplicial / Hodge-dual / axis-to-skew-operator framework developed here*".
- **Comparanda.** §8.1 and §9 both use "*within the simplicial wedge–Hodge framework developed here*".
- **Recommendation.** Harmonize §1.2 item 6 to "simplicial wedge–Hodge framework developed here."

### [F1-L-5] Keywords omit the paper's central terminological move ("gauge direction") and core construction primitive ("Hodge dual / wedge product")
- **Current.** "simplicial coordinates, Quadray, cross product, Rodrigues formula, Lie algebra, zero-sum hyperplane, rotation."
- **Recommendation.** Proposed revised Keywords:
  > **Keywords:** simplicial coordinates, Quadray coordinates, gauge direction, zero-sum hyperplane, cross product, Hodge dual, wedge product, Rodrigues formula, Lie algebra, rotation.

  Rationale: `gauge direction` and `zero-sum hyperplane` index the paper's central structural moves; `Hodge dual` and `wedge product` index §3.4 and §8 and keep the higher-$N$ generalization discoverable; `Quadray` is upgraded to `Quadray coordinates` for parity with §1.1.

### [F1-L-6] MSC 2020 misses exterior algebra; 22E70 arguably wrong subhead
- **Current.** 15A72, 22E70, 53A45, 65D18.
- **Analysis.** 15A72 ✓ keep. 22E70 ("applications of Lie groups to the sciences") is defensible but 22E60 (Lie algebras of Lie groups) is a closer structural fit for the $\mathfrak{so}(3) \cong (\mathbb{R}^3,\times)$ material. 53A45 ✓ keep. 65D18 ✓ keep. Missing: **15A75** (Exterior algebra, Grassmann algebras) — load-bearing given §3.4 and §8.
- **Recommendation.** Proposed revised MSC 2020:
  > **MSC 2020:** 15A72 (multilinear algebra), 15A75 (exterior algebra, Grassmann algebras), 22E60 (Lie algebras of Lie groups), 53A45 (vector and tensor analysis), 65D18 (numerical aspects of computer graphics).

### [F1-L-7] Cosmetic — §1.3 paragraph boldface convention inconsistency
Log-only; purely cosmetic. Defer to pre-submission polish / LaTeX conversion.

---

## Cross-checks that passed (no finding logged)

1. Abstract line 17 Gram matrix $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$ matches §2.4. ✓
2. Abstract line 17 collapsed quadratic form $\langle c,c\rangle = \tfrac{N}{N-1}\sum_i c_i^2$ matches §2.4 Prop 2.2. ✓
3. Abstract line 15 three-clause structure matches Theorem 4.1 clauses (1)/(2)/(3). ✓
4. Abstract line 21 $R\mathbf{1}=\mathbf{1}$, zero-sum preservation, 9-mult kernel — matches Prop 6.1(2), Prop 6.1(6), Theorem 7.1. ✓
5. Abstract line 21 $\mathfrak{so}(3) \cong (\mathbb{R}^3,\times)$ reflection — matches §8.1 and §9. ✓
6. Abstract line 21 higher-$N$ sentence — matches §8.2 and §1.2 item 6. ✓
7. §1.1 line 43 "Thomson … left as an open question" — consistent with §7.4 comparison and the [Thomson] reference. ✓
8. §1.2 item 2 "axis $u$ that is zero-sum and of unit simplicial norm" — matches Def 3.1 verbatim (the Abstract at F1-M-3 falls short of this standard, not §1.2 item 2). ✓
9. §1.2 item 4 $\mathrm{SO}(4) \cap \mathrm{Stab}(\mathbf{1})$ lift + restriction-to-$H$ — matches §6 Prop 6.1 and §9 novelty list. ✓
10. §1.3 Rodrigues-formula paragraph — display uses $R(u,\theta)$ and $K(u)$ consistently with §5 and §9. ✓
11. §1.3 low-$N$ degeneracies — dimension count on $\Lambda^2 \mathbb{R}^2$ correct. ✓
12. Note on the Use of AI Tools — factual, responsibility-appropriate, consistent with Acknowledgments. ✓
13. §1.2 item 6 octonion disclaimer — consistent with §8.1. ✓

---

## Harmonized front-matter patch list (for the Author)

The four Medium findings can be closed with:

- **F1-M-1** — Abstract line 21: insert "within the simplicial wedge–Hodge framework developed here" into the uniqueness sentence.
- **F1-M-2** — §1.2 item 3 line 53: upgrade to two-slot form. Mark `[L-2-1]` RESOLVED.
- **F1-M-3** — Abstract item 2 line 18: replace "unit vector" with "zero-sum unit axis".
- **F1-M-4** — §1.3 (after line 69 paragraph): add a one-sentence gloss of "autonomous *presentation*" previewing §4 Remark 4.2 and §9.

Plus the stylistic/Keyword/MSC Lows (F1-L-3 through F1-L-6) if the Author batches this pass.

**STATUS: AMBER**
