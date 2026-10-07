# The Gauge Curvature of Varying Simplicial Frames: An Abelian Triviality and a Discrete Orientation Field

**Leonardo Murillo Montero**

*leonardo.murillo@gmail.com*

*Probe note — June 2026*

**Question.** Paper 01b §9 sketched a gauge-covariant derivative $D=\nabla+A$ for the simplicial frame, with $A$ a connection valued in the gauge line $\mathbb{R}\mathbf 1$ and curvature $\mathcal F=dA$, and asked: is $\mathcal F$ ever nontrivial over a mesh of varying frames? Paper 01 §2.2.1 had flagged the gauge analogy as "interpretive motivation, not a formal equivalence of categories." This note settles both: the continuous abelian curvature is identically zero, but a genuine *discrete* gauge theory does appear — the orientation field — upgrading the analogy to a formal (topological) gauge structure. Exact-certified in `empirical_integration/cert_gauge_curvature.py`.

---

## 1. The continuous abelian curvature vanishes

The gauge freedom is the shift $c\mapsto c+k(x)\mathbf 1$ along the gauge line $\mathbb{R}\mathbf 1$ — an abelian ($\mathbb{R}$, additive) gauge group. A connection is an $\mathbb{R}$-valued 1-form $A$ with $A\mapsto A-dk$ under a gauge change, and curvature $\mathcal F=dA$.

**Proposition 1.1 (Abelian flatness).** *Over any mesh of simplicial frames, the $\mathbb{R}\mathbf 1$ curvature is identically zero, $\mathcal F=dA\equiv0$, and its holonomy is trivial.*

*Proof.* The structure group of frame relabelings is the symmetric group $S_4$ (permuting the four frame rays), acting on $\mathbb{R}^4=H\oplus\mathbb{R}\mathbf 1$. Every permutation fixes the gauge line: $P_\sigma\mathbf 1=\mathbf 1$ for all $24$ elements of $S_4$ (certified). Hence the $\mathbb{R}\mathbf 1$ sub-bundle is $S_4$-invariant and trivial. Independently, the mean-subtraction (zero-sum) section $c\mapsto c-\bar c\,\mathbf 1$ is defined *globally* — one can always subtract the mean, on every cell, with no obstruction — so the gauge bundle admits a global flat section and $\mathcal F\equiv0$ in that gauge, hence in every gauge ($\mathcal F$ is gauge-invariant). $\square$

The §9 program — a continuous abelian gauge theory with nonzero field strength — therefore does **not** materialize. The reason is structural and clean: the gauge direction $\mathbf 1$ is the one thing every frame relabeling fixes, and the mean is always subtractable.

## 2. The discrete orientation field is genuinely curved

The nontrivial gauge content lives not in the continuous shift but in the **orientation** — the datum Paper 01 §2.5 singled out as "the extra datum beyond the Gram matrix," the class in $S_4/A_4\cong\mathbb{Z}/2$. Over a mesh, assign to each adjacency (edge $e$) the relabeling $\sigma_e\in S_4$ gluing the two cells, and let the orientation connection be the $\mathbb{Z}/2$ edge variable $\operatorname{sgn}(\sigma_e)$.

**Proposition 2.1 (Orientation lattice gauge field).** *The plaquette product*
$$\mathcal F_f=\prod_{e\in\partial f}\operatorname{sgn}(\sigma_e)\in\{\pm1\}$$
*is gauge-invariant under cell-orientation flips $\sigma_e\mapsto\tau_{c'}\sigma_e\tau_c^{-1}$, and can equal $-1$. A value $\mathcal F_f=-1$ is a genuine orientation defect (a disclination in the frame field) that no local gauge change removes; the global holonomy $\prod_{e\in\gamma}\operatorname{sgn}(\sigma_e)$ around a loop $\gamma$ is the first Stiefel–Whitney class $w_1\in H^1(\text{mesh};\mathbb{Z}/2)$ — the obstruction to a globally consistent orientation.*

*Proof.* Gauge invariance: under cell flips the plaquette product conjugates by $\tau_{c_0}$ and $\operatorname{sgn}$ is a class function, so $\prod\operatorname{sgn}$ is unchanged (certified: a defect stays $-1$, a flat plaquette stays $+1$, under explicit cell flips). The defect example (one odd gluing around a $4$-cell loop) gives $\mathcal F=-1$; a Möbius loop (a single odd gluing closing up) has $w_1\neq0$ and no global orientation, while every cell is locally consistent — the obstruction is purely global (all certified). $\square$

**The cross product feels it.** The orientation curvature is not abstract: by Paper 01 Proposition 2.2, $P_\sigma^{-1}K(P_\sigma u)P_\sigma=\operatorname{sgn}(\sigma)K(u)$, so transporting the cross-product generator around a loop of net-odd holonomy returns it negated, $K\mapsto-K$ (certified). An orientation defect is exactly a place where the oriented algebra of Paper 01 cannot be globally trivialized — the cross product comes back with the wrong sign.

## 3. Verdict

**The gauge theory is real but discrete.** Paper 01 §2.2.1's analogy upgrades to a formal gauge structure: a flat $S_4$ lattice gauge theory of frame relabelings, with the orientation $\mathbb{Z}/2$ sub-field carrying gauge-invariant curvature.

- **Continuous / abelian $(\mathbb{R}\mathbf 1)$:** curvature $\mathcal F=dA\equiv0$, always. Trivial — the §9 differential gauge theory does not exist, because $\mathbf 1$ is fixed by the whole structure group and the mean is globally subtractable.
- **Discrete / orientation $(\mathbb{Z}/2=S_4/A_4)$:** gauge-invariant plaquette curvature $\mathcal F_f=\prod\operatorname{sgn}(\sigma_e)\in\{\pm1\}$, nontrivial on orientation defects, with global holonomy $w_1$. The full frame bundle is a flat $S_4$ bundle classified by its holonomy $\pi_1\to S_4$.

So the simplicial frame's "gauge curvature" is **topological, not differential**: there is no local field strength, but there are orientation defects (codimension-2 disclinations, $\mathcal F_f=-1$) and global twists ($w_1$, $S_4$ holonomy). This is the precise and honest form of the §2.2.1 analogy — a discrete gauge theory whose only nonzero invariant is the orientation class Paper 01 already identified as essential.

**Program reading.** This closes the one forward thread that did not fold into the bigrading bicomplex: the orientation $\mathbb{Z}/2$ is genuinely separate, a topological field over the mesh rather than a move within $P_n\Lambda^k$. It is the discrete companion of the harmonic/$b_1$ current of forward3 — both are topological invariants of the global frame arrangement (one $\mathbb{Z}/2$ orientation, one $\mathbb{Z}$/Betti current) rather than local algebra on a single cell.

---

## Appendix: certificate

`empirical_integration/cert_gauge_curvature.py` (sympy, exact):
- **A.** $P_\sigma\mathbf 1=\mathbf 1$ for all $24$ $\sigma\in S_4$; mean-subtraction is a global zero-sum section $\Rightarrow$ abelian $\mathcal F\equiv0$.
- **B.** plaquette curvature $\prod\operatorname{sgn}(\sigma_e)$: $-1$ (defect) / $+1$ (flat); gauge-invariant under explicit cell flips; Prop 2.2 transport $P_h^{-1}K(P_hu)P_h=\operatorname{sgn}(h)K(u)$ (odd $h\Rightarrow-K$).
- **C.** flat $S_4$ holonomy example; Möbius loop has $w_1\neq0$, no global orientation, each cell locally flat.

---

*[End of probe note.]*
