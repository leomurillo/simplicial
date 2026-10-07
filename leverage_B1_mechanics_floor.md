# Leverage B1 — Grounding the Mechanics Line on the Finished Simplicial-Frame Series

**Scope.** This is a *grounding map*, not an edit. It connects the "mechanics on the
categorical simplex" line — Papers 13, 14, 17, 20, 24 (classical) and 15, 18 (quantum lift) —
to the closed frame-coordinate results of the finished four-paper simplicial-frame series:

- **Paper II** = `01b.simplicial_vector_calculus.md` — ∇, div, curl, Δ; the Helmholtz / `S+A`
  (symmetric strain / antisymmetric current) split of the field Jacobian; gauge–Hodge.
- **Paper III** = `01c.simplicial_information_geometry.md` — the moving Amari–Chentsov cubic
  `K^CH_p(u)v = D_p(u⊙v) − ⟨u,v⟩_{g_p} p`; the **frozen-geometry × Fisher-diagonal**
  factorization; the cumulant tower `T^(n)=∇ⁿφ` with `T^(n)=c_n Δ^(n) D_p^{n-1}`; the
  **α-collapse** `Γ^(α) = −((1+α)/2) T`; the Legendre `φ↔Φ` duality and the chart-localization
  of the quartic obstruction.
- **Paper IV** = `01d.simplicial_keystone_integration.md` — `M_N = NI−J` complete-graph
  Laplacian, universal eigenvalue `N`; the order×degree FEEC bicomplex; `S+A`/Betti arrow.

**HARD TIER (stated up front, confirmed at the end).** Per the program plan this item
**grounds and tidies; it does not move the mechanics results.** Every object the mechanics
papers need is already classical Amari–Chentsov / Nambu information geometry; Papers II–III
supply the *closed frame-coordinate form* and the *exact certificates*, plus three genuine
sharpenings that are new **to these papers** (not to the literature): (1) the explicit
α-family collapse as a single tensor; (2) the frozen/breathing factorization sharpening the
force law; (3) the chart-localization that pins the jerk `T^(4)` to the exponential chart.
None of these change a theorem in 13/14/17/20/24 — they tighten statements that were made
implicitly or in a different (character/e-chart) basis. The one item that genuinely **adds a
result** these papers do not contain (the α-collapse as one closed tensor) is flagged in §C.

---

## A. What the mechanics papers actually use (verified against the sources)

| Object | Mechanics-paper form | Source lines |
|---|---|---|
| **Generalized force** | `F_i = ẍη_i = K_CH(v,v)_i = T_{ijk}(v) vʲ vᵏ` | 17 L26, L79; 20 L36; 24 L22 |
| **Cubic tensor (raised)** | `K^CH = Γ^(m) − Γ^(e)`, with `g_p(K^CH_p(u)v,w)=T_p(u,v,w)` | 13 L97, L1109, L1115 |
| **Cubic tensor (lowered)** | `T_p(u,v,w) = Σ_a u_a v_a w_a / p_a²` | 13 L1124 |
| **Connection data** | the **two flat affine structures** m-flat and e-flat; their **difference** is `K^CH` | 13 L101, L1102–1109 |
| **Centroid convolution form** | `K^CH_{p_*}(h)v = Q·h*v − Q⟨h,v⟩p_*` (cyclic) | 13 L1136–1142 |
| **Cumulant tower** | log-partition `ψ(θ)=log Σ_a e^{θ_a}` = "categorical effective action": c1=position, c2=Fisher ruler/**inertia/mass**, c3=AC=**force**, c4+=**jerk/projection defect** | 13 L204–217, L264; 17 L31–37 |
| **Jerk** | `⃛η = ∇^(e)T = T^(4)` (fourth cumulant), pointer to quartic momentum | 17 L28, L81; 20 L11, L26; 18 L79 |
| **Simplex mass** | `m²_simplex = leading T^(4) coefficient in conductor-total sector`, `≥0` | 20 L66–73 |
| **Lagrangian/energy** | `ℓ₃ = ½ g(v,v) + ⅓ T(h,v,v)`; `E₃ = ½ g(v,v) + ⅓ T(h,v,v)` | 17 L48–64; 20 L20–33 |
| **Metric (classical)** | Fisher–Rao `g_p(u,v)=Σ_a u_a v_a / p_a`; at centroid `g_{p_*}=Q·I_H` | 13 L699, L708; 24 L106 |
| **Metric (quantum)** | Bures–Helstrom `g^B_ρ(X,Y)=2Tr(X L_ρ^{-1}Y)`, `L_ρ(Z)=ρZ+Zρ`; `=` Fisher on diagonal | 15 L52, L72; 18 L100 |
| **Cubic structure constant** (Z/6) | `T_{klm} = 216·𝟙[k+ℓ+m≡0 mod 6]` (character/e-chart basis) | 17 L234; 20 L52–55, L120 |

**Verdict on the two posed verification questions:**

1. **"Force = cubic (Amari–Chentsov)" — CONFIRMED, verbatim and central.** All five classical
   papers state `F = K_CH(v,v)` and `K^CH = Γ^(m)−Γ^(e)`. The lowered tensor
   `Σ u_a v_a w_a / p_a²` is *identical* (up to the global Fisher-scale convention) to Paper III's
   Amari–Chentsov tensor `T_p(u,v,w)=Σ u_i v_i w_i / p_i²` (III §5, before Thm 5.1). The raised
   operators match exactly: Paper III Thm 5.1 `K^CH_p(u)v = D_p(u⊙v) − ⟨u,v⟩_{g_p} p`
   **is** Paper 13's force operator written in closed coordinate form. They are the same object.

2. **"Connection = α-family" — PARTIALLY. The papers use only the two ENDPOINTS, never the
   family.** Grep across 13/14/17/20/24 for `α-connection / Christoffel / Levi-Civita / Γ^(α) /
   (1+α)/2` returns **zero matches**. The papers invoke `Γ^(m)` and `Γ^(e)` (the m-flat and
   e-flat connections) and their difference `K^CH`, but never the one-parameter interpolation,
   never the Levi-Civita `Γ^(0)`, never a closed-form Christoffel. So the connection data is
   present only as its two flat extremes. **This is the gap Paper III §6 closes** (see §C).

---

## B. The grounding map (per paper)

For each paper: **(a)** the object Papers II–III now give in closed frame-coordinate form;
**(b)** a draft citation/insert sentence (NOT applied); **(c)** what Papers II–III reveal that
the paper stated only implicitly.

### Paper 13 — *Simplectic Mechanics on the Categorical Simplex*

**(a) Closed forms now available.**
- The force operator. Paper 13's `K^CH` momentum-gap (§7, "the simplectic replacement for
  force", L1172–1177) is given pointwise in closed coordinates by **Paper III Thm 5.1**:
  `K^CH_p(u)v = D_p(u⊙v) − ⟨u,v⟩_{g_p} p`, `D_p=diag(1/p_i)`. Paper 13's centroid convolution
  form `Q·h*v − Q⟨h,v⟩p_*` (L1136) is exactly the `p_*` reduction in Thm 5.1
  (`N(u⊙v) − (Σ u_i v_i)𝟙`).
- The metric/inertia. Paper 13's "second cumulant = Fisher ruler and inertia/mass matrix"
  (L208) at the centroid is `g_{p_*}=Q·I_H` — which by **Paper IV Thm 2.1/3.1** is the
  `K_Q` graph Laplacian `M_Q|_H = Q·I_H`, the universal eigenvalue. The mass matrix is the
  complete-graph Laplacian.
- The `N=4` "axis ↔ 2-form miracle" (§2) is the same `d=N−1=3` exceptionality catalogued in
  **Paper IV §7** (four faces of `d=3`), and `K(u)²=−I` on `u^⊥` is **Paper II / Cor 01.3.6**
  (`K(u)²=P_∥−I`).

**(b) Draft inserts.**
- (§7, after L1170) *"In closed frame coordinates the momentum-gap operator is
  `K^CH_p(u)v = D_p(u⊙v) − ⟨u,v⟩_{g_p}\,p` with `D_p=\mathrm{diag}(1/p_a)` (Paper III, Thm 5.1);
  its centroid reduction `Q(u⊙v) − Q⟨u,v⟩p_*` is the convolution form used above, and the
  componentwise product `⊙` carries the position-independent cross-product-square realization
  `I+K(τ_a)^2` of Paper III §5 — only the diagonal Fisher gain `D_p` depends on the state."*
- (Source Anchor 1, replacing the single "Simplicial Vector Calculus" entry) *"**Papers I–IV
  (simplicial-frame series).** Paper I supplies the cross product `K(u)` and `K^3=−\|u\|^2K`;
  Paper II the curl/`S+A` Helmholtz split; **Paper III the moving Amari–Chentsov cubic in
  closed frame coordinates, its frozen-geometry × Fisher-diagonal factorization, and the
  α-connection collapse**; Paper IV the complete-graph Laplacian and the universal eigenvalue
  `N` (= the centroid Fisher/inertia matrix)."*

**(c) What is revealed.**
- **Frozen factorization SHARPENS the force law.** Paper 13 says only that `K^CH` "leaks across
  conductor packets off the centroid" and that the leak coefficients are arithmetic convolution
  (L1167–1177). Paper III Thm 5.1 + the §5 "Reading" make precise *what is fixed and what moves*:
  the cross-product/tetrahedral-multiplication **geometry is position-independent** (the
  projectors `I+K(τ_a)^2` are frozen across the whole simplex); the *entire* state-dependence of
  the force is the single diagonal Fisher gain `D_p`. The mechanics force law is "the fixed
  tetrahedral multiplication of Paper I heard through a position-dependent diagonal gain." This
  is a strictly sharper statement than "the gap is `Γ^(m)−Γ^(e)`."
- **`S+A` reading of the momentum/force is already in Paper II.** Paper 13's binary-vs-simplectic
  framing (the `J²=−I` quarter-turn, the antisymmetric primitive) is exactly the antisymmetric
  half of **Paper II Prop 7.3**: a field Jacobian splits `DF=S+A`, `A=½K̃(curl F)`. The "current"
  primitive Paper 13 reaches for is Paper II's solenoidal/curl sector; the "curvature" primitive
  is the gradient/strain sector. This grounds Paper 13's central dichotomy in a proven split.

### Paper 14 — *The Classical Cartan Obstruction and the Forced Quantum Lift*

**(a) Closed forms.** Same force/metric closed forms as Paper 13. Additionally, Paper 14's
`Γ^(m), Γ^(e)` (implicit in `K^CH`) acquire their **full closed-form connection content** from
**Paper III Thm 6.1**: in the m-affine (simplicial) chart `Γ^(−1)=0` (manifest m-flatness),
`Γ^(0)=−½T`, `Γ^(+1)=−T`, and the whole family is `Γ^(α) = −((1+α)/2)T`.

**(b) Draft insert.** (after Thm 2.2′ setup, where the m/e affine structures enter) *"In the
simplicial m-affine chart the connection data is a single tensor: `Γ^(α)=−\tfrac{1+α}{2}T`
(Paper III, Thm 6.1), with `Γ^{(−1)}=0` (the chart is mixture-affine), `Γ^{(+1)}=−T` the
e-connection, and `T=K^{CH}` the Amari–Chentsov cubic. The `m`/`e` pair used here is the
`α=∓1` specialization, and the obstruction analysis below depends only on `T`."*

**(c) What is revealed.**
- The Cartan-obstruction proof (Thm 2.2′) is a statement about which directions in `H_R`
  preserve the real cone and commute with the conductor projectors. Paper III's **diagonality of
  the m-chart tower** (Thm 4.1) and the **`φ↔Φ` duality** (Prop 7.1) give the clean reason the
  *character* basis is the right basis for that proof: the genuine cumulants (the off-diagonal,
  `2+2`-Wick-structured objects whose mixing the proof forbids) live in the e/character chart
  `∇ⁿΦ`, while the m-chart tower is purely diagonal and carries no packet-mixing block at all.
  The obstruction is therefore *intrinsically an e-chart phenomenon* — which Paper III states as
  a theorem (Prop 7.2) and Paper 14 uses implicitly.

### Paper 17 — *The Cubic Noether Theorem*

**(a) Closed forms.**
- Lagrangian `ℓ₃ = ½g(v,v)+⅓T(h,v,v)`: `g` is **Paper IV's** centroid Laplacian (order-2 rung),
  `T` is **Paper III's** order-3 rung `T^(3)=∇³φ` in closed form (Thm 5.1).
- The jerk `∇^(e)T = T^(4)`: this is **Paper III's order-4 cumulant rung**. In the m-chart,
  Paper III Thm 4.1/4.2 give it in closed form, `T^(4) = c_4 Δ^(4) D_p^3` with `c_4 = +24`
  (`(−1)^4·2! = 2`? — note Paper III's stated coefficient is `c_4 = (−1)^4(4−2)! = 2`; the
  table value "24" in III is for `n=6` — **see flag in §E**).

**(b) Draft inserts.**
- (Def 2.1, after introducing `T`) *"`T=K^{CH}` is the order-3 rung `T^{(3)}=∇^3φ` of the
  cumulant tower; in closed frame coordinates `g_p(T_p(u)v,w)=Σ_a u_a v_a w_a/p_a^2` and
  `T_p(u)v = D_p(u⊙v)−⟨u,v⟩_{g_p}p` (Paper III, Thm 5.1)."*
- (Thm 2.2, at "the next e-covariant derivative … is the jerk `∇^{(e)}T=T^{(4)}`") *"`T^{(4)}`
  is the order-4 rung of the cumulant tower `T^{(n)}=∇^nφ` (Paper III, §4). On the entropy
  (m) chart this rung is purely diagonal (Paper III, Thm 4.1) and therefore carries no `2+2`
  Wick block; the genuine quartic content — the obstruction to a classical quartic charge — is a
  phenomenon of the conjugate exponential chart `∇^4Φ` (Paper III, Prop 7.2). This is the
  information-geometric reason the quartic loophole is closed independently of the
  representation-theoretic Cartan argument."*

**(c) What is revealed — the strongest cross-pollination in the batch.**
- Paper 17 *asserts* (Thm 3.1, L170–175) that a quartic charge from `T^(4)` is forbidden because
  it would require conductor-packet-mixing generators (Cartan obstruction). **Paper III Prop 7.2
  gives a second, independent, structural reason**: the m-chart cumulant tower is *provably
  diagonal* (Thm 4.1), so it has *no `i i j j` component at all* — the `2+2` Wick block that a
  quartic obstruction is made of literally cannot live on the entropy tower; it lives only on the
  dual log-partition tower `∇^4Φ`. So Paper 17's "the jerk points at quartic momentum but it
  cannot close classically" is **doubly grounded**: (i) representation theory forbids the
  generators (Paper 14); (ii) the m-chart tower is the wrong chart to even host the object
  (Paper III). These are complementary, and Paper III's is the cleaner *negative structural*
  statement.
- The spin-decomposition (Rmk 2.2A, the Stuart–Landau `γ=−⅛[…]=−w̄₃` identity) is a 2-D
  reduction of the same cubic vertex `T`; Paper III's frozen factorization explains why that
  constant `⅛` is *position-independent* (the cubic geometry does not breathe; only `D_p` does),
  which is implicit in Paper 17's promotion "from a measured scaling law to an identity."

### Paper 20 — *The Jerk as Simplex Mass Term*

**(a) Closed forms.** `m²_simplex = leading T^(4) coefficient`: `T^(4)` is **Paper III's order-4
rung in closed form** (Thm 4.1/4.2). The "`m²_simplex` vanishes at the centroid" property
(L70) is exactly the `p`-dependence `D_p^3` of `T^(4) = c_4 Δ^(4) D_p^3` evaluated against a
displacement `h` (the diagonal weight is state-dependent and the leading on-centroid contraction
vanishes by the zero-sum/`Σ` structure — see the Prop 7.1 inverse-scaling statement).

**(b) Draft insert.** (Def 2.1) *"`T^{(4)}=∇^{(e)}T` is the order-4 rung of the cumulant tower
`T^{(n)}=∇^nφ` (Paper III §4); on the entropy chart it factors as `T^{(4)}=c_4Δ^{(4)}D_p^{3}`
with `Δ^{(4)}` the position-independent all-equal-index selector and `D_p=\mathrm{diag}(1/p_a)`
the breathing Fisher weight (Paper III, Thm 4.2), making the centroid-vanishing of
`m^2_{\text{simplex}}` manifest."*

**(c) What is revealed.**
- The **diagonal/off-diagonal split** Paper 20 leans on — m-chart tower (where the closed cubic
  variational problem lives) vs. the projected-back-path defect (where `T^(4)` becomes a real
  curvature) — is exactly Paper III's `φ`-tower (diagonal) vs `Φ`-tower (`2+2` Wick) dichotomy.
  Paper 20's "the jerk is the order-4 *projection-closure residual*" is the mechanics reading of
  Paper III Prop 7.2's "the obstruction's home is the conjugate chart."
- Paper 20 repeatedly couples `m²_simplex≥0` to the Z/6 character rule `k+ℓ+m≡0 mod 6` and the
  structure constant `216` (L52–55). That `216` is the **character-basis (e-chart) form** of the
  AC cubic; Paper III gives the *coordinate-free, basis-independent* form (`D_p(u⊙v)−⟨u,v⟩p`)
  and the cross-product-square realization of `⊙`. So Paper 20's arithmetic constant and Paper
  III's geometric operator are the two charts of one tensor.

### Paper 24 — *Cubic Information-Geometric Mechanics on the Categorical Simplex*

**(a) Closed forms.** This is the consolidation of 13/14/17/20 for `R=Z/6`. All four closed
forms above apply verbatim: force `K^CH_p` (III Thm 5.1), metric `g_{p_*}=Q·I_H` (IV), tower
rungs `T^(3), T^(4)` (III §4), connection family (III Thm 6.1).

**(b) Draft insert.** (§3, where the Fisher volume and `K^CH(v,v)` are introduced) *"The raised
cubic is `K^{CH}_p(u)v=D_p(u⊙v)−⟨u,v⟩_{g_p}p` (Paper III, Thm 5.1); all `α`-connection content
on the simplex reduces to this one tensor, `Γ^{(α)}=−\tfrac{1+α}{2}K^{CH}` (Paper III, Thm 6.1),
with `m`-flatness `Γ^{(−1)}=0` manifest in the simplicial chart."*

**(c) What is revealed.** Same α-collapse and frozen-factorization leverage as 13/14; because 24
is the synthesis paper it is the natural host for the single sentence that says "the connection
data of this whole line is one tensor in closed frame coordinates."

### Papers 15 & 18 — the quantum (Bures) lift (overlaps C2)

**(a) Closed forms.** On the **diagonal/commuting submanifold** the Bures–Helstrom metric
restricts *exactly* to Fisher (15 Thm 2.2, `ι*Ω^B = Ω_R^F`; 18 §3), so every closed form above
holds on the diagonal. The quantum cubic is the **quantum Amari–Chentsov tensor** on
`D(ℂ²⊗ℂ³)`.

**(b) Draft insert.** (15 §2 or 18 §3, at the diagonal-restriction theorem) *"On the diagonal
commuting submanifold the lift restricts to the simplicial-frame information geometry of Paper
III: the Bures metric becomes the Fisher/`K_N`-Laplacian metric (Paper IV) and the quantum
Amari–Chentsov cubic restricts to `K^{CH}_p` of Paper III, Thm 5.1. The monotone-metric choice
(SLD/Bures vs Kubo–Mori) is Paper III's Open Problem D4."*

**(c) What is revealed.** Paper III's closing **Open Problem D4** *names this exact lift*: "the
quantum continuation: the moving cubic on the density-matrix manifold … where the
monotone-metric fork (Bures versus Kubo–Mori) replaces the unique Fisher metric." Papers 15/18
are the worked answer to D4 — and the **Petz–Bures uniqueness** they invoke (18 §1: "the unique
monotone metric whose conservative Nambu–Bures flow is von Neumann evolution") is the resolution
of the fork that Paper III left open. Conversely, Paper III's `α↔−α` involution and the
self-dual order-2 rung are the *classical shadow* of the SLD-selection rigidity. (This is the
B1↔C2 seam: C2 owns the quantum monotone-metric story; B1 supplies the classical floor and the
D4 pointer.)

---

## C. The α-collapse: does Paper III give the connection data as one tensor? — YES, and it is
genuinely new TO THESE PAPERS

**Finding.** The mechanics papers carry connection data only as the *difference of two flat
charts*, `K^CH = Γ^(m) − Γ^(e)` (Paper 13 L1109; reused by 14/17/24). They never write the
Levi-Civita connection, never the α-interpolation, never a closed Christoffel. Verified by
zero-match grep over all five classical papers for `α-connection / Christoffel / Levi-Civita /
Γ^(α) / (1+α)/2`.

**Paper III Theorem 6.1** supplies, in the simplicial m-affine chart, the *entire* connection
content as a single cubic tensor:
> `Γ^(0) = −½T` identically ⟹ `Γ^(α) = −((1+α)/2) T` for all α,
> with `Γ^(−1)=0` (manifest m-flatness), `Γ^(+1)=−T` (e-connection), `T=K^CH`.

This means the mechanics line's "two flat affine structures" are the `α=∓1` endpoints of a
one-parameter family that is *entirely carried by the force tensor `T` itself*. Concretely it
adds, for free, to the mechanics papers:
- the **Levi-Civita** (metric, `α=0`) connection `Γ^(0)=−½K^CH` — never written in 13/14/17/24;
- the statement that **dual flatness is a curvature identity on the single cubic** (`R^(+1)=0`),
  i.e. the whole `(g, ∇^(±1))` dually-flat package the mechanics presupposes is one equation
  on `K^CH`;
- the manifest m-flatness `Γ^(−1)=0` that makes the simplicial chart the canonical mixture
  chart (the chart Paper 13 §3/§6 already uses for `h=p−p_*` but never identifies as
  `Γ^(−1)=0`).

**Tier call on this item.** This is the one place where the grounding **adds a result the
mechanics papers do not state**. It still does **not move** any mechanics theorem (the force law,
the Cartan obstruction, the cubic Noether charge are all unchanged — they only ever used the two
endpoints, and the endpoints are correct). But it is more than tidying: it tells the mechanics
line that *its connection, curvature, and dual-flat structure are all one tensor in closed form*,
which none of 13/14/17/24 says. Recommend it be presented in Paper 24 (the synthesis) as a
one-paragraph "connection content" remark citing Paper III Thm 6.1, with 13/14/17 getting the
one-line `α=∓1`-endpoint footnote.

**Position-independence of the cubic geometry (frozen factorization) — does it sharpen the force
law? YES.** Paper 13's force law is stated as "the gap `Γ^(m)−Γ^(e)`" plus "leaks across
conductor packets, coefficients = arithmetic convolution." Paper III Thm 5.1 + Thm 4.2 sharpen
this to: **the cubic's tetrahedral-multiplication geometry (`I+K(τ_a)^2`) is frozen across the
entire simplex; the only state-dependence of the force is the diagonal Fisher gain `D_p`** (and,
at all higher orders, `D_p^{n-1}`). For the mechanics line this means the force's *direction
field* is position-independent and only its *gain* breathes — a strictly stronger and more
useful statement than the convolution-coefficient bookkeeping. (It also explains why the
Stuart–Landau constant `⅛` in Paper 17 Rmk 2.2A is a fixed number, not a state-dependent one.)

---

## D. Jerk (Paper 20) and Cubic Noether (Paper 17) ↔ the order-3/order-4 cumulant rungs

This is the cleanest weld in the batch, because Papers III and IV already **name the cumulant
order as an axis** (IV §4, the FEEC bicomplex; III §8 "the cumulant tower is the order axis").

- **Force (Paper 17/13/24) = order-3 rung.** `K^CH = T^(3) = ∇³φ` (Paper III §5). The mechanics
  "force = third cumulant = Amari–Chentsov" is *literally* the third rung of `T^(n)=∇ⁿφ`.
- **Jerk (Paper 17/20) = order-4 rung.** `⃛η = ∇^(e)T = T^(4) = ∇⁴φ` (or `∇⁴Φ` on the dual).
  Paper III §4 gives `T^(4)` in closed form; Paper III §7 (Prop 7.2) explains **why the jerk is a
  conjugate-chart object**: the entropy (m) tower is diagonal and obstruction-free at the `2+2`
  level, so the genuine quartic content (the jerk-as-defect, `m²_simplex`) is necessarily an
  e/character-chart phenomenon. This is exactly Paper 20's "projection-closure residual" and
  Paper 17's "quartic loophole is closed."
- **The order axis is a proven structure, not a metaphor.** Paper IV Thm 4.1/4.2 places the
  cumulant tower as the `k=0` column of the FEEC bicomplex `P_nΛ^k`, with total degree `n+k`
  the invariant. So Paper 13's "position / inertia / force / jerk = cumulants 1/2/3/4"
  (L208–211, L265) is the `k=0` order-axis climb of the bicomplex — and the *reason* the
  mechanics stops cleanly at cubic-force + quartic-jerk is that climbing the order axis past
  `n=3` lands on the diagonal-tower wall (III Prop 7.2) / the Cartan wall (14 Thm 2.2′).

**One-line weld for Papers 17 & 20** (already drafted in §B): cite `T^(n)=∇ⁿφ` (Paper III §4)
for the rungs and Prop 7.2 for the chart-localization of the jerk.

---

## E. Honest tier confirmation + flags

**Tier: GROUNDS AND TIDIES; DOES NOT MOVE — confirmed,** with one "adds-a-result" exception
(§C, the α-collapse as one closed tensor) that still moves *no theorem*. Specifically:

- Force law, Cartan obstruction, cubic Noether charge, jerk-as-mass, Bures lift — **all
  unchanged.** Papers II–III supply closed coordinate forms and exact certificates for objects
  the mechanics papers already use correctly.
- The three sharpenings (α-collapse / frozen-factorization / jerk-chart-localization) tighten
  *implicit* or *character-basis* statements into *explicit, basis-free, certified* ones. The
  α-collapse is the only one that supplies content (the Levi-Civita connection + dual-flat
  curvature identity) absent from the mechanics papers; it changes no result.

**Flags (things to check before any future edit):**

1. **Coefficient `c_4` discrepancy to resolve before citing.** Paper III Thm 4.1 states
   `c_n=(−1)^n(n−2)!`, giving `c_4 = (−1)^4·2! = 2` and the table `1,−1,2,−6,24` for `n=2..6`.
   So the **order-4 coefficient is `2`** (the `24` is the `n=6` entry). My draft inserts in §B
   for Paper 20 say `c_4` without a numeral — keep it symbolic, or write `c_4=2`, **not** 24.
   No error in Paper III; just don't mis-transcribe the table when grounding Paper 20.
2. **Global Fisher-scale convention.** Paper III uses `g_p(u,v)=Σ u_i v_i/p_i` (no `Q` factor;
   `g_{p_*}=N·Σ` only via `M`-normalization). The mechanics papers carry an explicit
   `g_{p_*}=Q·I_H` and sometimes "up to the global normalization convention" (13 L1128). The
   closed forms match *up to that scale*; any inserted sentence should say "up to the global
   Fisher-scale convention" to stay honest (as Paper 13 already does).
3. **`Γ^(m)−Γ^(e)` sign vs Paper III `Γ^(α)=−((1+α)/2)T`.** Paper 13 fixes `K^CH=Γ^(m)−Γ^(e)`
   (= `Γ^(−1)−Γ^(+1)`). Paper III gives `Γ^(−1)=0`, `Γ^(+1)=−T`, so `Γ^(−1)−Γ^(+1)=+T`. Thus
   `K^CH=+T` in both — **consistent** — but the bookkeeping (`m`=`α=−1`, `e`=`α=+1`) should be
   stated explicitly in any insert so the sign convention is unambiguous.
4. **"Simplicial Vector Calculus" reference in Paper 13 is the PRE-SPLIT title.** Source Anchor 1
   (L4657) predates the four-paper split (I/II/III/IV). The grounding insert should upgrade it to
   the current Papers I–IV with DOIs, and crucially **add Paper III** (currently uncited for the
   moving cubic) and **Paper IV** (uncited for the Laplacian/inertia identification).
5. **No certificate is claimed here.** I ran no sympy/numpy (the identities are already
   certified in Papers II–III Appendix A: `cert_moving_infogeom.py`, `cert_cumulant_tower.py`,
   `cert_simplicial_calculus.py`). The matches asserted above are read-offs against those
   certified statements, not new computation.

---

## F. Cross-pollination notes (to the other batch items)

- **A2 (Paper 21 quartic / Wick).** The jerk `T^(4)` is the bridge. Paper III Prop 7.2 localizes
  the quartic `2+2` Wick obstruction to the **exponential chart** `∇⁴Φ` and proves the entropy
  chart `∇⁴φ` is `2+2`-obstruction-free (purely diagonal). Paper 17/20's "quartic loophole is
  closed / jerk is a projected defect" is the mechanics face of the *same* obstruction A2 studies
  as the `n=4` Wick block. **Seam:** A2 should treat Paper 21's quartic obstruction and Paper
  20's `m²_simplex` (= leading `T^(4)`) as the *same object in two charts*; Paper III Prop 7.2 is
  the hinge that says which chart carries it. Worth checking whether Paper 21's quartic
  obstruction tensor equals `∇⁴Φ`'s `2+2` block on `Z/6` (the `216`/character side).
- **B2 (T11 / Paper IV vertex calculus).** The "inertia/mass = order-2 cumulant = `K_N` graph
  Laplacian = universal eigenvalue `N`" identification (Paper IV Thm 3.1) is the order-2 floor
  under the mechanics metric. B2 owns the vertex/Laplacian calculus; B1's grounding of the
  *mechanics inertia matrix* as that Laplacian is the shared boundary. The FEEC bicomplex (IV §4)
  is the common frame: B1's order axis (cumulant force/jerk) is the `k=0` column; B2's degree
  axis (Hodge/Laplacian) is the row; they meet at the corner `(2,0)` = the mass matrix.
- **C1 (RH apex N14/N15).** Paper 20 itself wires `m²_simplex≥0` to the primorial Noether
  positivity whose all-order limit is conjecturally Weil positivity (20 L75, citing Paper 22
  Rmk 5.0). Paper III's `φ↔Φ` Legendre pair is flagged in III §8 as "the cleanest *finite* model
  of global Legendre = Tate–Poisson = functional equation" — *explicitly fenced as analogy only*
  (III §8 fenced speculation). **Seam/guardrail:** B1 should keep the III §8 firewall — the
  finite separable entropy potential cannot host the archimedean FE; C1's N14/N15 relative-
  entropy/Weil-positivity machinery is the real arithmetic object. The honest connection is "the
  cubic Noether positivity is the cubic-order *shadow*, not the theorem" (matches the MEMORY
  N14/N15 and Paper 22 §11 "Unsafe statement" boundary).
- **C2 (quantum Bures — overlaps 15/18).** Direct overlap. B1's reading of 15/18 (§B above) is
  the classical-floor view: the Bures lift answers Paper III **Open Problem D4**, and Petz–Bures
  SLD-uniqueness resolves the monotone-metric fork (Kubo–Mori vs Bures) that III left open. C2
  owns the quantum monotone-metric / Chentsov-uniqueness story; B1 supplies the D4 pointer and
  the diagonal-restriction = Fisher/`K_N`-Laplacian identification. **No conflict; clean handoff
  at the diagonal submanifold.**
- **C3 (unification).** Paper II §10.2 / Open Problem C3 *literally names* "the floor under the
  program's mechanics on the categorical simplex line" as the moving-information-geometry door,
  and Paper IV §8 lists the five roles of `K̃` (rotation / curl / coboundary / arrow / cumulant
  cubic) as the spine that makes the whole series cohere. B1 is the realization of that C3 door
  for the mechanics papers: one tensor (`K^CH=T`) is the force, the connection family, and (via
  `K̃`'s role 5) the frozen cross-product geometry. **Seam:** C3's unification claim "everything
  sorts into `S+A` of one object" (IV §9) is exactly the dichotomy Paper 13's binary-vs-simplectic
  framing reaches for; B1 grounds the mechanics half.

---

## G. Open follow-ups

1. **Resolve the `c_4` numeral** (flag E.1) before any insert touches Paper 20.
2. **Verify Paper 21's quartic obstruction tensor = `∇⁴Φ` `2+2` block on `Z/6`** (the A2/B1
   seam). If they coincide, Paper III Prop 7.2 + Paper 20 `m²_simplex` + Paper 21 quartic become
   one statement in three papers — worth a single shared lemma. (Deterministic: the `216`/
   character-rule side is already symbolic in Paper 20/32.)
3. **Decide host for the α-collapse remark** (§C). Recommend Paper 24 (synthesis) gets the
   paragraph; 13/14/17 get the one-line `α=∓1`-endpoint footnote. This is the only "adds-content"
   item and should land once, cleanly.
4. **Upgrade Paper 13 Source Anchor 1** to Papers I–IV with DOIs and add the Paper III / Paper IV
   citations (currently absent). Mechanical but load-bearing for the grounding to be legible.
5. **Confirm the global Fisher-scale convention** (flag E.2) is stated wherever a closed form is
   inserted, to keep the `Σ u v/p` (Paper III) vs `Q·Σ` (mechanics) bookkeeping honest.
6. **(Forward-only, low priority)** Paper III Open Problem D2 asks whether the cross-product-
   square realization of `⊙` extends to an `n`-fold product through `I+K(τ_a)^2`. If yes, it
   would give the *jerk* `T^(4)` (and all higher rungs) the same frozen-geometry reading the
   force has — directly sharpening Paper 20's `m²_simplex`. Flagged as a genuine open lever, not
   claimed.
