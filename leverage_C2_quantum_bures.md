# Leverage C2 — The Quantum Continuation (Open Problem D4): Moving Cubic → Bures / Kubo–Mori

**Assessment of Paper III's open problem D4 against the program's quantum line.**
Read-only scan of Papers 44, 15, 18, T24, with the classical objects in Paper III
(`01c.simplicial_information_geometry.md`) and the SIC connection in Paper I §8.3
(`01.simplicial_vector_algebra.md`). Deterministic cert in
`empirical_leverage/C2/cert_quantum_bures_fork.py` (16 checks, **GREEN**).

Tier: **genuine forward door, moderate — CONFIRMED.** D4 is *already substantially
answered* by the existing quantum line; what is new here is the explicit
identification (the bridge is the diagonal reduction; the fork is T24; the SIC is
the N=4 corner) plus the cert that crystallizes it. No new theorem is needed to
open the door; one finite check (SLD-uniqueness inside Petz–Sudár, Paper 18 Thm 6.1)
is needed to *close* it.

---

## (a) What 44 / 15 / 18 / T24 actually establish

### Paper 15 — the Bures lift of the mechanics (proof-level)
- **Thm 2.2 (classical recovery).** Diagonal embedding `ι: Δ_R° ↪ D(ℂ²⊗ℂ³)`,
  `p ↦ diag(p)`; the Bures–Helstrom volume form pulls back exactly to the Fisher
  volume form, `ι*Ω^B = Ω_R^F`. Proof is explicit: for diagonal `ρ=diag(p)` and
  diagonal tangent `Y`, the SLD equation `ρZ+Zρ=Y` gives `Z_aa=y_a/(2p_a)`, so
  `g^B = Σ x_a y_a / p_a` = Fisher. **Solid.**
- **Thm 3.2 (Nambu–Bures → von Neumann).** Unitary invariance of Bures ⟹ the
  conservative flow is `ρ̇ = −i[H,ρ]`. Solid (Cartan's formula + flow-box).
- **Thm 4.1 (gauge recovery).** Maximal CRT-local, Bures-volume-preserving,
  positivity-preserving symmetry algebra on `D(ℂ²⊗ℂ³)` is exactly
  `su(2) ⊕ su(3)`. The classical real-cone Cartan obstruction (`u(1)²` only) is
  lifted because off-diagonal coherences absorb nonabelian mixing while keeping
  positivity/trace. Solid as stated (it is finite Lie bookkeeping on the
  effective algebra `(u(2)⊕u(3))/u(1)_diag`).
- §5 is an *exploratory* transformer residual-stream audit (Llama-3.1-8B,
  Mistral-7B), explicitly flagged non-dispositive (task accuracy 0.32 / 0.51).
  Not load-bearing.

### Paper 18 — Bures completion + the rigidity that forces it
- §3 restates the diagonal Fisher recovery; §4 restates the Nambu–Bures →
  unitary reduction; §5 the completion statement (Cartan floor `u(1)²` ⊂
  `su(2)⊕su(3)⊕u(1)`, the surplus `u(1)` = inter-leg trace/normalization phase,
  Prop 5.1 [Certain]).
- **Thm 6.1 (Petz–Bures rigidity) [Bare-assertion rel. §4].** *Assuming* the §4
  selection (SLD/Bures is the monotone metric whose Nambu–Bures flow is von
  Neumann) is **unique inside the Petz–Sudár family**, unitary invariance + CRT
  leg dims (2,3) force `su(2)⊕su(3)`. **The honest open node is named:** the
  finite check "does §4 select SLD *uniquely*, or merely select *a* monotone
  metric?" Until discharged, Thm 6.1 stays at the displayed tier.
- **Thm 6.2 (Hurwitz as terminator) [Certain].** ℝ,ℂ,ℍ,𝕆 in dims 1,2,4,8 is the
  *terminator* (why no 5th norm-closed rung), **not** the generator of the gauge
  content. Earlier closed-current/norm-closure route **Withdrawn** (Rem 6.3): it
  conflated unitary-invariance (forces `su(n)` per leg) with norm-multiplicativity
  (forces the division-algebra ladder). They coincide *numerically* at legs (2,3)
  but are different mechanisms. Honest.
- **Rem 6.4 (Open Problem O) [Conjectural].** The single open node in the
  Petz–Bures layer: does closed-current positivity force the *joint* monotone
  metric on the tensor product `D(ℂ²⊗ℂ³)` — including off-block cross-coherences
  — to be the minimal SLD/Bures member? This is *exactly* the tensor-product face
  of the T24 fork.

### Paper 44 — the worked cubic→Bures bridge on ℤ/6
- Constructs everything explicitly in ℂ⁶ ≅ ℂ²⊗ℂ³ as 6×6 Hermitians.
- **§4.1 Bures metric in coords:** `g^B_{ρ_p}(X,X) = Σ_i X_ii²/p_i +
  Σ_{i≠j} 2|X_ij|²/(p_i+p_j)` — Fisher diagonal **+** Bures coherence
  `2/(p_i+p_j)` (= arithmetic-mean Morozova–Chentsov weight; no classical analog).
- **§4.2 + Lemma 4.1 — THE BRIDGE:** the Bures cubic tensor
  `T^B_ρ(X,Y,Z) = Re Tr(ρ L_X L_Y L_Z)_sym` reduces *on the diagonal* to
  `Σ_i X_ii Y_ii Z_ii / p_i²` = the **classical Amari–Chentsov tensor** (Paper III
  §5). Off-diagonal it grows new cross-coherence terms with denominators
  `(p_i+p_j)`, `(p_j+p_k)`, `(p_k+p_i)` — the quantum cross-packet content.
  **This is the literal "moving cubic on the density-matrix manifold."**
- **Thm 5.1 (Lift Isometry):** classical cubic Noether energy `E₃^(C)` = Bures
  cubic Noether energy `E₃^(B)` restricted to the diagonal. Proof = apply Lemma
  4.1 termwise (all args diagonal). **Solid** (it is the diagonal-reduction
  corollary; the cert verifies its two ingredients exactly).
- **Thm 7.1 (Leakage = Jerk):** for a Bures-stationary trajectory starting on the
  diagonal, the off-diagonal coherence grows as `(t³/6)Φ(J(0))` where `J(0) =
  ∇^(e)T(h,η̇,η̇)` is the classical jerk (Paper 17 Thm 3.1's "forbidden" 4th-cumulant
  term). The leakage *constant* `c₆ ≈ 0.42` (normalized) is a cross-packet
  Clebsch–Gordan sum. The leading-`t³` identity is the substantive content;
  higher orders flagged open (OP3). The `c₆≈0.42` value is a pre-registered
  prediction for an *unrun* RK-integration cert (§9.2) — **not yet verified**.
- **Thm 8.1 (Quantization Forced):** no classical extension realizes the jerk as
  a conserved charge under (real-cone + CRT) constraints; the Bures lift is the
  canonical resolution. **Rem 8.2 is honest:** "forced" ≠ "only mathematical
  structure"; other quantum info-geometries (Wigner–Yanase, Petz–Sudár family,
  α-connections) exist — Bures is the one preserving unitary-invariance +
  Fisher-restriction. §8.3 adds a Lindblad/depolarizing (DBT26) open-system
  reading: the Cartan `u(1)²` is the kernel of asymptotic depolarization.

### T24 — the monotone-metric fork (scoping paper)
- **Thm 2.1 (Morozova–Chentsov–Petz):** quantum monotone metrics ↔ operator-
  monotone `f` with `f(1)=1`, `f(t)=tf(1/t)`; eigenbasis form
  `g^f_ρ(A,A) = Σ_{ij} c^f(λ_i,λ_j)|A_ij|²`, `c^f(x,y)=1/(y f(x/y))`. Classically
  Chentsov gives **one** (Fisher); quantumly a **family** (Cor 2.2 dichotomy).
- **Prop 3.1 (zero fork-width on the decoherent face):** `c^f(λ,λ)=1/λ` for *all*
  `f` ⟹ on diagonal `ρ` every member restricts to the *same* classical Fisher.
  The family separates **only** off-diagonal, where `[log ρ, C_c]≠0`.
- **Thm 3.2 / Prop 3.3 (the three members + ordering):**
  | member | `f(t)` | mean | `c^f(x,y)` | role |
  |---|---|---|---|---|
  | SLD/Bures | `(1+t)/2` | arithmetic | `2/(x+y)` | **minimal**; `4g^SLD`=QFI |
  | Kubo–Mori | `(t−1)/log t` | logarithmic | `(log x−log y)/(x−y)` | **dually flat**; Hess of rel. entropy |
  | RLD | `2t/(1+t)` | harmonic | `(x+y)/2xy` | **maximal** |

  HM≤LM≤AM reverses (since `c=1/mean`) to `g^SLD ≤ g^KM ≤ g^RLD`.
- **Prop 4.1:** the one-observable generator `M_ρ(β,c) = (det ρ)^{−β/N}·
  (1/N)Tr(ρ^β C_c*)` is unambiguous and tilts *inside the log* (`ρ^β=e^{β log ρ}`)
  ⟹ it draws the **Kubo–Mori e-geodesic**. The fork lives at *second* order
  (Thm 4.3): the covariance of two non-commuting character observables forces an
  ordering = choice of `f`.
- **Thm 5.1 (Grasselli–Streater):** Kubo–Mori is the **unique** monotone metric
  admitting a dually-flat (e/m) pair — the additive/Pythagorean relative-entropy
  member. **This is the quantum continuation of "what is additive?"**
- **The T24 verdict directly contradicts the default Paper 18 framing:** T24 §6
  audits Paper 18/T7 for silently writing "Bures" and recommends **Kubo–Mori**
  for the *additivity* question (SLD only for *estimation*).

---

## (b) Classical → quantum map + monotone-fork analysis + SIC

### Map of Paper III's three classical objects to their density-matrix versions

| Paper III (classical, `01c`) | quantum lift | where |
|---|---|---|
| Fisher `g_p(u,v)=Σ u_i v_i/p_i` (§2, Hess of `−`entropy) | Bures `g^B_ρ` (diagonal block) | P15 Thm 2.2; P18 §3; P44 §4.1 |
| **Moving AC cubic** `K^CH_p(u)v = D_p(u⊙v) − ⟨u,v⟩_{g_p} p`, `T_p(u,v,w)=Σ u_i v_i w_i/p_i²` (§5) | **Bures cubic** `T^B_ρ(X,Y,Z)=Re Tr(ρ L_X L_Y L_Z)_sym` | P44 §4.2, Lemma 4.1, Thm 5.1 |
| **frozen geometry × Fisher diagonal** (§4 Thm 4.2: `T^(n)=c_n Δ^(n) D_p^{n−1}`) | Morozova–Chentsov weight `c^f(λ_i,λ_j)` on each `(i,j)` block | T24 Thm 2.1 + Prop 3.1 |
| **α-collapse** `Γ^(α)=−((1+α)/2)T`, dual flat (§6) | quantum `±1`-connections — dual flat **for Kubo–Mori only** | T24 Thm 5.1 |
| diagonal entropy tower can't host the 2+2 quartic obstruction (§7, Prop 7.2) | obstruction lives in the *coherence* block, off the decoherent face | T24 Prop 3.1; P44 §4.2 three-coherence term |

**The quantum Amari–Chentsov tensor** is `T^B_ρ`. On the diagonal it equals the
classical `T_p` *exactly* (cert check B); its genuinely new content is the
off-diagonal three-coherence term `~(p_i+p_j)^{−1}(p_j+p_k)^{−1}(p_k+p_i)^{−1}`
(Paper 44 §4.2) — the cross-packet cubic that the classical tower is structurally
blind to (Paper III Prop 7.2). This is one and the same blind spot read on two
sides: classically it is "the diagonal `∇⁴φ` has no `iijj` block"; quantumly it is
"the fork (and the obstruction) opens only on coherences."

### Does the "frozen geometry × Fisher diagonal" factorization have a quantum analog? — **Yes, and it is precisely where the fork lives.**

Classically (Paper III Thm 4.2) the order-`n` tower factors as
`c_n · Δ^(n) · D_p^{n−1}`: a *position-independent* combinatorial selector
`Δ^(n)` (frozen — the cross-product-square geometry of Paper I) times a breathing
diagonal Fisher weight `D_p^{n−1}=diag(1/p_i^{n−1})`. The single moving part is
the diagonal weight `1/p_i`.

Quantumly (T24 Thm 2.1) the metric is `g^f_ρ(A,A)=Σ_{ij} c^f(λ_i,λ_j)|A_ij|²`.
The **diagonal weight `1/p_i` is replaced by the two-index Morozova–Chentsov
weight `c^f(λ_i,λ_j)`**. The factorization survives in the following exact sense
(cert checks A, B, E):

- **On the diagonal block `i=j`:** `c^f(λ,λ)=1/λ` for *every* `f` — the breathing
  Fisher diagonal `D_p` is recovered identically, and the "frozen geometry × Fisher
  diagonal" picture holds verbatim. **The classical factorization is the
  decoherent-face restriction of the quantum metric.**
- **On the off-diagonal block `i≠j`:** the single scalar weight `1/p_i` splits into
  the *whole Petz family* `c^f(λ_i,λ_j)`. This is the fork. The "Fisher diagonal"
  has become a "monotone-metric off-diagonal," and *which* function fills it is the
  modeling choice T24 names.

So Paper III's factorization does have a quantum analog, and the
Bures-vs-Kubo–Mori choice **changes it precisely off the diagonal**:

- **Does the cross-product-square geometry survive?** The *frozen selector*
  `Δ^(n)` (Paper I's `I+K(τ_i)²` projectors) is a diagonal-sector object — it
  builds the componentwise product `⊙` on `H`, which is the *classical* (commuting)
  multiplication. It survives **verbatim on the diagonal/decoherent face** (cert
  check B reproduces the classical AC tensor there). Off-diagonal it is *replaced*,
  not deformed: the coherence sector has no `⊙` analog; it has the genuinely
  non-commutative `c^f` interleaving instead. The cross-product square is the
  `r=0` (commuting) shadow of the quantum object — exactly as the SIC tetrahedron
  is the `r=1` (pure-state) shadow (see SIC below).
- **Which metric makes it dually flat?** **Kubo–Mori, uniquely** (T24 Thm 5.1,
  Grasselli–Streater). Paper III's whole §6 α-collapse rests on dual flatness
  (`Γ^(−1)=0`, `R^(+1)=0`). The α-connection family `Γ^(α)=−((1+α)/2)T` is a
  *dually-flat* statement; its honest quantum continuation requires the *unique*
  monotone metric carrying a dually-flat `±1` pair. That is **Kubo–Mori, not
  Bures**. Bures (= the program's default in P15/P18/P44) is the *minimal/estimation*
  member and is **not** dually flat. The α-collapse continues to the quantum sector
  on the Kubo–Mori member; on Bures the "single cubic carries the whole
  α-family" structure breaks (the SLD second moment is not a cumulant of the
  power family — T24 §5.2 thread 3).

**The tension, stated sharply.** The cubic *mechanics* line (P15/P18/P44) selects
**Bures** because Bures is the metric whose Nambu–Bures flow is von Neumann
(`ρ̇=−i[H,ρ]`) — a *dynamics/estimation* criterion. The cubic *information-
geometry* line (Paper III's α-collapse / dual-flatness) selects **Kubo–Mori**
because KM is the *additive/dually-flat* member — an *information* criterion. These
are different members of the same Petz corridor. **This is the real content of D4,
and it is a genuine open fork, not a notational one.** Paper 18 Rem 6.4 (Open
Problem O) and T24 are the two ends of it; they have not been reconciled in the
corpus. (See follow-up F1.)

### The SIC / N=4 connection (Paper I §8.3)

Paper I §8.3 ("Equiangular tight frames and single-qubit SIC-POVMs") establishes:
the N=4 simplicial frame = the real ETF of four unit vectors in ℝ³ with pairwise
dot `−1/3`, which *is exactly* the four Bloch vectors of a single-qubit SIC-POVM.
The dictionary (cert check G, all exact):
- SIC overlap `|⟨ψ_i|ψ_j⟩|² = 1/3` ↔ `n_i·n_j = 2|⟨ψ_i|ψ_j⟩|²−1 = −1/3` ✓
- POVM completeness `Σ E_i = I` ↔ `Σ n_i = 0` (the frame's zero-sum identity) ✓
- `Tr(E_i E_j)=½(1+n_i·n_j)=1/3` for `i≠j`; rank-1 projectors `Tr(E_i²)=1` ✓
- The rotation operators `R(u,θ)` (Paper I §5) realize the
  `SO(3) ≅ SU(2)/{±I}` action of projective qubit unitaries directly on `H`,
  without the SU(2) double cover.

**What the calculus gives for single-qubit geometry.** The qubit is the `N=2`
density-matrix manifold — the **Bloch ball** `D(ℂ²)`. Three readings line up:
1. **The SIC tetrahedron is the pure-state corner.** `n_i·n_j=−1/3` is the Paper I
   uniform tetrahedral angle `arccos(−1/3)`; the four SIC states are the
   maximally-symmetric pure states. The Amari–Chentsov cubic *at the center*
   `p_*` (Paper I Cor 3.9, built from `I+K(τ_i)²`) is the classical (diagonal)
   shadow; the SIC is the same tetrahedron read as *pure* `ρ`'s on the **boundary**
   of the Bloch ball.
2. **The fork is the radial coordinate.** On the qubit, every monotone metric
   agrees at the center `ρ_*=I/2` (maximally mixed, both eigenvalues `1/2` —
   Prop 3.1 on every direction, cert check F) and *splits* outward with radius
   `r=|n|`. The Bures and Kubo–Mori weights on a coherence direction (e.g. `σ_x`
   at `ρ=(I+rσ_z)/2`) are `w^SLD=2` (constant) and `w^KM=(log λ_+−log λ_−)/(λ_+−λ_−)`
   with `λ_±=(1±r)/2`; they coincide at `r→0` and obey `w^SLD ≤ w^KM` everywhere
   (cert F, envelope verified on 50 radii; split `0.197` at `r=½`). **So the
   monotone fork of T24 is, on the qubit, literally the gap between two ways of
   measuring distance as you move off the maximally-mixed center toward the SIC
   tetrahedron on the boundary.**
3. **`N=4` is doubly special.** Paper I §8.1: `N=4` is the unique single-axis case
   (`dim so(3)=3`). The SIC is the `N=4` ETF. The cubic-mechanics ℤ/6 worked
   example (P44) is a *different* `N=6=2·3` object (CRT ℂ²⊗ℂ³, `su(2)⊕su(3)`); the
   `N=4` SIC is the *single-qubit* `D(ℂ²)`, the `su(2)`-only / minimal-leg corner.
   The program's quantum-sector geometry thus has two canonical small instances:
   the **qubit Bloch ball** (`N=4` frame = SIC, single `su(2)`) and the **ℤ/6 CRT
   lift** (`N=6`, `su(2)⊕su(3)`). The calculus gives the first one for free.

---

## (c) Tier — confirm/adjust

**CONFIRMED: "genuine forward door, moderate."**

- *Genuine forward door* — yes. D4 (Paper III's flagged open problem) maps cleanly
  onto an already-built quantum line (P15/P18/P44) plus the fork paper (T24). The
  door is open: the moving cubic *does* lift (the Bures cubic `T^B_ρ`, reducing to
  the classical AC tensor on the diagonal — cert B), and the monotone fork *is*
  the quantum replacement of the unique Fisher metric (cert A/D/E).
- *Moderate* — yes, not "major." Three reasons it is not a breakthrough: (i) the
  hard reductions (diagonal Bures=Fisher, diagonal cubic=AC) are corollaries of
  standard SLD algebra, verified here but not deep; (ii) the *closing* node
  (SLD-uniqueness in Petz–Sudár, P18 Thm 6.1; and the joint-tensor Open Problem O,
  P18 Rem 6.4) is genuinely open and is finite-checkable but unproven; (iii) the
  Bures-vs-Kubo–Mori reconciliation between the *mechanics* line and the
  *information-geometry* (dual-flatness) line is unresolved in the corpus.
- **One honest downgrade flag inside Paper 44:** Thm 7.1's `c₆≈0.42` and the
  `t³`-leakage scaling are *pre-registered predictions* for an RK-integration cert
  (§9.2) that does **not** appear to be run (no `leakage_jerk_verification_z6.py`
  output in-repo at scan time). The *static* bridge (Lemma 4.1 / Thm 5.1) is
  solid; the *dynamical* leakage constant is asserted, not verified.

---

## (d) Cert status

**GREEN** — `empirical_leverage/C2/cert_quantum_bures_fork.py`, 16/16 checks
(sympy exact + a small numpy spectral check; **no torch**). Run with `py`.

- **A** diagonal Bures metric = classical Fisher `Σ x_i²/p_i` (SLD solved exactly).
- **B** diagonal Bures cubic `T^B` = classical Amari–Chentsov `Σ x_i y_i z_i/p_i²`
  — **the cubic→Bures bridge, verified** (Paper 44 §4.2 / Thm 5.1 ingredient).
- **C** off-diagonal Bures weight = `2/(p_i+p_j)` = inverse arithmetic mean
  (the coherence term with no classical analog).
- **D** the three Morozova–Chentsov functions `c^SLD=2/(x+y)`,
  `c^KM=(log x−log y)/(x−y)`, `c^RLD=(x+y)/2xy`, with ordering
  `c^SLD ≤ c^KM ≤ c^RLD` (Prop 3.3).
- **E** fork collapses on the diagonal: `c^f(λ,λ)=1/λ` for all three (Prop 3.1)
  ⟹ the quantum AC tensor is fork-independent on the decoherent face.
- **F** qubit Bloch: Bures = Kubo–Mori at `ρ_*=I/2`; split for `r>0` with
  `g^SLD ≤ g^KM` over the whole ball (Prop 4.1 / the radial reading).
- **G** the four tetrahedral Bloch vectors are a valid single-qubit SIC: pairwise
  dot `−1/3`, `Σ½E_i=I`, `Tr(E_iE_j)=1/3`, rank-1 projectors (Paper I §8.3).

(Cert deliberately does **not** attempt Paper 44's `c₆≈0.42` dynamical leakage —
that requires trajectory integration and is flagged open above.)

---

## (e) Cross-pollination

- **A2 (Paper 21 quartic / Wick).** Direct hand-off. Paper III §7 (Prop 7.2):
  the quartic obstruction is the `2+2` Wick block of `∇⁴Φ` (exponential chart),
  and the diagonal entropy tower **cannot** host it. T24 locates the same split
  quantumly: the obstruction lives off the decoherent face, on coherences, where
  the fork opens. So A2's quartic/Wick object is the **order-4 sibling** of the
  order-3 cubic this item lifts — and Paper 44 OP3 (higher-order leakage,
  `O(t⁴)` = the quartic) is exactly the dynamical face of A2. If A2 finds the
  Wick block is the first *non-dually-flat* rung, that is the same statement as
  "Kubo–Mori dual flatness is an order-≤3 phenomenon." **Shared object: the
  2+2 Wick block as the first obstruction rung.**
- **B1 (mechanics floor — overlaps 15/18).** B1 *is* the classical mechanics whose
  quantum lift this item assesses. Papers 15/18 are shared between B1 and C2:
  B1 owns the real-simplex Nambu–Fisher mechanics (Paper 14) and its cubic Noether
  theory (Paper 17); C2 owns the Bures lift (P15/P18/P44). The seam is the
  diagonal embedding `ι` and the Lift Isometry Thm 5.1. **Coordinate so B1 and C2
  agree on what "the cubic" is** (the AC tensor `T_p`, raised to `K^CH_p`); C2 adds
  that its quantum continuation is `T^B_ρ` with the fork on coherences.
- **B2 (T11).** T11 is the vertex/apex calculus; T24 (this item's fork paper) is
  the *quantum* apex selection (Kubo–Mori vs Bures for the density-matrix apex
  `M_ρ`). If B2 touches the apex generator `M_x(β,c)`, note T24 Prop 4.1: its
  quantum lift `M_ρ` tilts inside the log ⟹ draws the Kubo–Mori e-geodesic. **The
  apex's own generator already chose Kubo–Mori.**
- **C1 (RH apex N14/N15).** The dually-flat/additive selection here is the *same
  shape* as the N14/N15 "archimedean Weil positivity = relative entropy /
  separable convex" reading: Kubo–Mori is the *unique* member whose canonical
  divergence is quantum relative entropy with a Pythagorean (additive)
  decomposition (T24 Thm 5.1). Both pick the relative-entropy/log-convex member
  as the additive one. The cubic vs the quartic split (even/ζ vs chiral/odd
  channel in the RH line) mirrors Paper III's diagonal/off-diagonal (entropy
  vs character chart) split. **Analogy only** — finite separable potential, as
  Paper III §8 itself fences; do not over-weld. But the *selection principle*
  (additivity ⟹ relative-entropy member) is genuinely the same on both sides.
- **C3 (unification).** Paper 44 §10 + Paper 15/18 are the explicit bid that the
  quantum lift's effective algebra `su(2)⊕su(3)` (and `⊕u(1)` trace mode) is the
  SM local gauge structure; Paper 18 Prop 5.1 / Rem 5.1A carefully separates the
  trace *mode* from the prime-reciprocal hypercharge *face*. C2 supplies the
  geometry (the Bures cubic, the fork) under that bid; C3 owns the
  "one functional, four forces" framing. **The honest scoping in P15 §7 / P18 §5 /
  P44 §1.3 (no chirality/generations/Yukawa/anomaly/gravity) should bound C3's
  claims.**

---

## (f) Open follow-ups

- **F1 (the central reconciliation).** The cubic-*mechanics* line selects **Bures**
  (von-Neumann-flow / estimation criterion, P15 Thm 3.2, P18 §4); the cubic-
  *information-geometry* line (Paper III α-collapse / dual flatness) selects
  **Kubo–Mori** (additivity criterion, T24 Thm 5.1). These are *different* Petz
  members. **Which one is "the quantum moving cubic"?** Resolution likely:
  *both, on different structures* — Bures carries the Nambu–Bures **dynamics**,
  Kubo–Mori carries the dually-flat **connection/α-family**. They agree on the AC
  *tensor value* on the diagonal (cert B) and at the maximally-mixed center (cert
  F), and diverge only on the coherence connection data. Writing this out is the
  natural sequel and would *close* the conceptual half of D4.
- **F2 (discharge P18 Thm 6.1's finite check).** Is the §4 selection (Nambu–Bures
  flow = von Neumann) **unique** inside Petz–Sudár, or does it only select *a*
  monotone metric? This is finite and checkable (the von-Neumann-flow condition vs
  the operator-monotone `f`). Settling it promotes Thm 6.1 off "bare-assertion."
  Caution: the von Neumann flow `ρ̇=−i[H,ρ]` is *unitary* hence preserves the
  spectrum and is metric-agnostic on the orbit — so "the metric whose flow is von
  Neumann" may **not** single out Bures at all (every monotone metric is unitarily
  invariant). If so, the mechanics line's Bures selection is *under-determined*,
  and F1 tilts toward Kubo–Mori. **Flagged as the load-bearing soft spot.**
- **F3 (run Paper 44's dynamical certs).** §9.2 leakage-equals-jerk (`c₆≈0.42`,
  `t³` scaling) and §9.3 Cartan-obstruction are pre-registered but un-run at scan
  time. §9.1 (Lift Isometry) and §9.4 (cubic-tensor audit) are now effectively
  covered by this cert's checks A/B and the Paper 44 §2.3 selection table; §9.2 is
  the one needing RK integration (numpy, no torch — safe to run locally).
- **F4 (joint-tensor Open Problem O, P18 Rem 6.4).** Does closed-current positivity
  force the *joint* monotone metric on `D(ℂ²⊗ℂ³)` (including off-block
  cross-coherences) to be minimal/Bures? This is the *tensor-product* face of the
  T24 fork and is the single remaining node in the Petz–Bures crystallization
  layer. Distinct from F2 (which is the single-factor selection).
- **F5 (qubit cert extension).** The cert computes the Bures/KM split only on the
  `σ_x` coherence direction. A full `g^f` tensor over the Bloch ball (all of
  `σ_x,σ_y,σ_z`) would give the exact "fork width as radial diagnostic" of T24 §8.3
  (the candidate quantum sibling of the CBS `σ_PI` packet-IPR). Small, numpy-only.
