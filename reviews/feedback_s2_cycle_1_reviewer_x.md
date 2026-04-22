# Reviewer X — Formalism Audit — Cycle 1
**Scope:** §2 Simplicial Coordinates: Setup (lines 77–156 of simplicial_vector_calculus.md)
**Reviewer:** Reviewer X (formalism & logic)
**Date:** 2026-04-20

## Findings

### Critical
- None.

### High
- **[F-H-1]** Remark 2.1, line 105 — The cross-discipline claim still overstates the mathematics. The sentence saying the CRNT compatibility classes and the simplicial gauge classes are such that "the structures are formally the same" directly conflicts with §1.2 item 1, line 49, which now limits the claim to a structural analogy and explicitly rejects formal equivalence. No formal identification is constructed here between simplicial gauge classes in $\mathbb{R}^N/\langle\mathbf{1}\rangle$, stoichiometric compatibility classes in CRNT, and the affine simplex constraint from information geometry. This blocks because §2 is the definitional foundation, and the paper cannot present its core gauge notion with a stronger claim than the Introduction is willing to defend.
- **[F-H-2]** §2.1, lines 79–93 — The manuscript calls $\{\mathbf{v}_i\}_{i=1}^N$ a "basis" / "basis vectors" even though the family is explicitly overcomplete and linearly dependent in $\mathbb{R}^{N-1}$. In standard mathematical usage, this is not a basis; it is a spanning family or, more precisely, a frame. The section itself immediately relies on the dependence at line 93. Because the entire paper is built on this object, misnaming it at the point of definition is a foundational formalism error, not cosmetic terminology.

### Medium
- **[F-M-1]** §2.2–§2.3, lines 101–117 — The paper does not separate the quotient space from the canonical section sharply enough. The equivalence relation $c \sim c'$ is stated correctly at line 101, and the zero-sum representative is then introduced at line 109, but the logical bridge "$H$ is a chosen section of the quotient $\mathbb{R}^N/\langle\mathbf{1}\rangle$" is never made explicit here. Instead the exposition jumps from equivalence classes to points in $\mathbb{R}^{N-1}$ and only later, in §2.4 line 139 and §4, speaks of descent to the quotient. For a setup section, that identification should be stated cleanly at first use.
- **[F-M-2]** §2.3, line 119 — The sentence "Matrix operators that respect the gauge (rotations, the cross product, the inner product) all preserve $H$" is false as written. The inner product is scalar-valued, not an operator $H \to H$, and later §1.2 item 3 and §4 correctly distinguish scalar gauge-invariance from vector-valued hyperplane preservation. The setup should not conflate these two different notions. (This is the same shape as Cycle 2 [F-H-4] in the Abstract, which was upgraded; consider whether the §2 site warrants the same upgrade.)
- **[F-M-3]** §2.5, lines 149–154, cross-checked with §3.4 lines 240–245 and §8.3 lines 459–467 — The $N=4$ coordinate ordering $(l,n,m,p)$ is fixed and later used consistently, but the orientation/chirality convention is not made explicit in the setup. Later sections invoke Hodge-dual language and chirality-sensitive basis-axis formulas, which depend on an orientation choice. The listed embedded vertices implicitly determine one, but §2 never says that the standard orientation of the ambient $\mathbb{R}^3$ with this vertex ordering is the orientation being used downstream.

### Low
- **[F-L-1]** §2.3, lines 109–111 — The uniqueness of the zero-sum representative is asserted but not justified. The proof is one line: if $c' = c + k\mathbf{1}$, then $\sum_i c'_i = 0$ forces $k = -\bar c$. In a foundational setup, this is worth spelling out explicitly once.
- **[F-L-2]** §2, lines 81 and 147 — The section assumes $N \geq 3$, which is acceptable, but it does not remind the reader inside §2 why $N=1,2$ are excluded even though §1.3 already records the low-$N$ degeneracies. A short internal reminder would make the setup more self-contained.

## Summary
The Gram-matrix portion is formally sound: §2.4's definition of $G = \tfrac{N}{N-1}I - \tfrac{1}{N-1}J$ matches §1.2 item 2, and Proposition 2.2 is correctly supported by Appendix A. The blockers are earlier in the section: Remark 2.1 still overclaims formal equivalence across disciplines, and §2.1 misnames a linearly dependent frame as a basis at the exact point where the paper is defining its core object.

STATUS: AMBER
