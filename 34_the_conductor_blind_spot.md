# The Conductor Blind Spot: An Exact Representational Limit of Second-Order Preconditioning on Ring-Structured Categorical Models

**Leonardo Murillo Montero**
*May 19, 2026*

**arXiv-style preprint (draft v0.1 — bounded theorem + diagnostic + pre-registered experiment)**

---

## Abstract

We exhibit an exact, finite, decidable representational limit of second-order
optimization on categorical models whose outcome index carries a finite ring
structure. Let the label set be $R=\mathbb{Z}/n\mathbb{Z}$ and let the model
emit a categorical distribution over $R$ (a softmax head). At the
maximum-entropy point $p_*$, in the additive-character basis of the tangent
space, two facts hold *exactly*, by character orthogonality, with no fitted
quantity and no tolerance: **(Q)** the Fisher information form — the curvature
object that *every* purely second-order preconditioner is (natural gradient,
Gauss–Newton, K-FAC, the empirical-Fisher used by Adam-type methods, the
neural-tangent-kernel Gram) — is block-diagonal across conductor packets, so
it carries *zero* inter-packet coupling; **(C)** the Amari–Chentsov cubic
form has *nonzero* inter-packet coupling, governed by the exact selection
rule $k+\ell+m\equiv 0\ (\mathrm{mod}\ n)$. Consequently the second-order
*curvature model class itself* — independent of estimation quality — has a
structural null space exactly aligned with a coupling that provably exists in
the local geometry. We call this the **conductor blind spot**.

This paper is deliberately three-layered and the layers are kept apart on
purpose. **Layer 1 (proven, this paper):** the certificate above, exact at
$p_*$, with a deterministic computational artifact covering
$n\in\{6,8,12,18,30\}$. **Layer 2 (proposed, this paper):** a one-pass,
retraining-free *diagnostic* — the conductor-packet projection of the update
— that converts the qualitative intuition "optimizers miss structure" into a
measured quantity per model per task. **Layer 3 (pre-registered, NOT run):**
a single sharp experiment with a built-in negative control, predicting that a
cheap cubic-aware correction accelerates the acquisition of ring structure
*if and only if* ring structure is present, with a specific prediction for
the delayed-generalization ("grokking") regime on modular tasks. We state
explicitly what is *not* claimed: the certificate is exact *at the
maximum-entropy point*; whether the deficit persists along a training
trajectory through the interior of the simplex is precisely the
pre-registered empirical question of Layer 3, not a corollary of Layer 1. No
performance claim is made by this paper; Layer 1 is a theorem with no
baseline to tune, Layer 2 is a measurement, Layer 3 is a falsifiable protocol
whose negative result is as informative as its positive one.

**Keywords:** second-order optimization, natural gradient, Fisher
information, Amari–Chentsov tensor, categorical models, additive characters,
conductor packets, ring-structured labels, grokking, preconditioning,
information geometry.

---

## 1. Introduction

### 1.1 The claim that keeps dying, and the claim that does not

The intuition that second-order optimizers "miss important structure" in deep
learning is old and widely felt. It does not survive peer review, and the
reason is structural rather than sociological: the intuition, as usually
stated, has no exact failure witness. To support "misses important
structure" one must define *important*, measure *miss*, and show it *matters*
— three empirical commitments, each contestable, each reducible to a
benchmarking dispute ("your baseline was undertuned"). A claim that can
always be deflected by tuning is, in practice, unfalsifiable, and an
unfalsifiable claim about optimizers is unpublishable.

This paper makes a different claim, of a kind that has an exact failure
witness and therefore no baseline to dispute. We do not claim a trained
network misses structure along its trajectory. We prove that the *curvature
model class* used by second-order preconditioning has, at a specific point,
in a specific basis, decided by a specific finite predicate, a structural
null space exactly aligned with a coupling that provably exists in the local
information geometry. The witness is a finite linear-algebra fact. There is
nothing to tune.

The price of having an exact witness is scope. The certificate is exact *at
the maximum-entropy point* of a ring-structured categorical model. We will
argue (Section 5) that this point is not an arbitrary convenience but the
unique configuration where the phenomenon is *provable precisely because it
is dynamically dormant there*; and we will state, with equal precision, that
the persistence of the effect off the maximum-entropy point is an open
empirical question we pre-register rather than a theorem we prove. Keeping
those two statements apart is the entire methodological content of the paper.

### 1.2 Why the bounded version is reachable now

The objects involved are individually classical. Amari's information geometry
named the Fisher metric as the second cumulant and the Amari–Chentsov tensor
as the third decades ago. The inadequacy of second-order curvature estimates
relative to the true Fisher is documented in the empirical-Fisher critique
literature. The appearance of additive-character ("Fourier") features in
networks trained on modular arithmetic is documented in the
mechanistic-interpretability literature on grokking. None of these, however,
*puts a ring structure on the outcome index and then asks what the standard
curvature model class can represent in the induced character basis*. That
single move — index the categorical tangent space by the additive characters
of $\mathbb{Z}/n\mathbb{Z}$, group the characters by conductor, and read off
which couplings the quadratic model class can and cannot carry — produces an
exact selection rule that, to our knowledge, has not been stated. Section 7
makes the relation to each of the three nearest bodies of work precise and
shows where each stops short.

### 1.3 The three layers, and the discipline of keeping them apart

We organize the paper as three layers at three epistemic tiers, using the
tiering convention of the broader program: **[P]** proven, **[A]**
structural and pending an explicitly named audit, **[C]** conjectural and
falsifiable.

* **Layer 1 — the certificate. [P].** Sections 3–4. An exact theorem at
  $p_*$, with a deterministic, exact-arithmetic computational artifact.
* **Layer 2 — the diagnostic. [P]→[A].** Section 6. A measurement
  procedure derived from Layer 1, runnable on any trained model with no
  retraining; it produces a number, not a performance claim.
* **Layer 3 — the experiment. [C], pre-registered, not run.** Section 8.
  A single sharp test with a negative control; both outcome branches are
  pre-claimed so that a negative result is reported as a result, not
  reframed.

The reader is asked to hold the layers apart exactly as the paper does.
Conflating Layer 1 with Layer 3 reproduces the unfalsifiable claim of
Section 1.1 and the paper would deserve the same fate as its predecessors.

---

## 2. Setup and anchored objects

All objects in this section are standard information geometry specialized to
a finite categorical model; none is introduced by this paper, and we use them
exactly as stated in the program's discrete-Fisher development (Paper 12 and
the *beyond_smooth* synthesis), which we treat here as the anchor of record
for the metric and cubic forms.

### 2.1 The categorical model and its ring-structured index

Let $R=\mathbb{Z}/n\mathbb{Z}$, $|R|=n$, and let the model emit
$p\in\Delta_R^\circ$, the open probability simplex over $R$ (a softmax head).
The tangent space at $p$ is $T_p\Delta_R^\circ=\{u\in\mathbb{R}^R:\sum_y
u_y=0\}$, of real dimension $n-1$. "Ring-structured" means only that the
index set $R$ carries the additive group $\mathbb{Z}/n\mathbb{Z}$; we make no
assumption on the model architecture.

### 2.2 The Fisher metric and the Amari–Chentsov cubic (anchored)

The Fisher information form and the Amari–Chentsov cubic form on
$\Delta_R^\circ$ are, respectively,

$$
g_p(u,v)=\sum_{y\in R}\frac{u_y v_y}{p_y},
\qquad
T_p(u,v,w)=\sum_{y\in R}\frac{u_y v_y w_y}{p_y^{2}} .
$$

These are the anchored objects. $g_p$ is, up to convention, the curvature
form that second-order preconditioning uses; $T_p$ is the first
information-geometric object that is *not* a function of $g_p$ — the leading
non-quadratic correction, the "third floor" of the cumulant tower. The
program's anchor states this in exactly these terms: *if the Fisher metric is
the local object that a second-order method sees, the Amari–Chentsov cubic is
the first local object it does not see unless the optimizer is explicitly
cubic-aware.* This paper makes that sentence into a finite certificate.

### 2.3 Additive characters and conductor packets (anchored)

The additive characters of $R$ are $\chi_k(y)=e^{2\pi i k y/n}$ for
$k\in\mathbb{Z}/n\mathbb{Z}$. The nontrivial characters $k=1,\dots,n-1$ span
the complexified tangent space; $k=0$ is the constant mode (the simplex
normal), excluded from the tangent interaction. Characters satisfy exact
orthogonality over $R$:

$$
\sum_{y\in R}\chi_k(y)\,\overline{\chi_\ell(y)}
=\sum_{y\in R}e^{2\pi i (k-\ell)y/n}
= n\,\big[\,k\equiv\ell\ (\mathrm{mod}\ n)\,\big].
$$

The **conductor** of character $k$ is $\mathrm{cond}(k)=n/\gcd(k,n)$. The
**conductor packets** are the groups of nontrivial characters sharing a
conductor $d\mid n$, $d>1$. This is the orthogonal decomposition of the
categorical tangent space into arithmetic blocks; it is the central object
of the discrete-Fisher anchor and is the basis in which the certificate is
stated.

### 2.4 What "second-order preconditioner" means here

By a *second-order preconditioner* we mean any optimization method whose
local model of curvature is a positive-semidefinite quadratic form on the
parameter or output tangent space, used to rescale the gradient. This
includes natural gradient (the exact Fisher), Gauss–Newton and its
Kronecker-factored approximation K-FAC, the (empirical or true) Fisher used
by Adam-type adaptive methods on a categorical head, and the
neural-tangent-kernel Gram in its linearized-training regime. The certificate
concerns the *representational capacity of the quadratic model class itself*;
it is therefore independent of which of these methods is used and independent
of estimation quality. This is the sense in which the result is about deep
learning broadly and not about active inference specifically: any of the
above on a ring-structured categorical head inherits the certificate. (We
develop the active-inference instance, where the categorical object is the
generative model's posterior, in the program's FEP-bridge notes; it is one
instance of the present statement, not its scope.)

---

## 3. Layer 1 — the conductor-blind-spot certificate

### 3.1 The two exact facts at maximum entropy

Let $p_*=\tfrac1n\mathbf{1}$ be the maximum-entropy (uniform) point.

**Lemma 3.1 (Fisher block-diagonality at $p_*$). [P].**
In the additive-character basis, the Fisher form at $p_*$ is exactly
diagonal, hence a fortiori block-diagonal across conductor packets:

$$
g_{p_*}(\chi_k,\overline{\chi_\ell})
= n\sum_{y\in R}\chi_k(y)\,\overline{\chi_\ell(y)}
= n^{2}\,\big[\,k\equiv\ell\ (\mathrm{mod}\ n)\,\big].
$$

*Proof.* $p_{*,y}=1/n$, so $g_{p_*}(u,v)=n\sum_y u_y v_y$. Substituting the
character basis and applying the exact orthogonality of Section 2.3 gives the
displayed Kronecker delta. The off-diagonal entries are *exactly* zero
because $\sum_y e^{2\pi i(k-\ell)y/n}$ is an exact geometric sum that
vanishes identically unless $k\equiv\ell\ (\mathrm{mod}\ n)$. No
floating-point comparison enters the decision; it is the integer predicate
$(k-\ell)\bmod n\ne 0$. $\blacksquare$

**Corollary 3.2 (zero inter-packet content). [P].**
Any quadratic form equal to $g_{p_*}$ — equivalently, any second-order
preconditioner whose curvature model is the Fisher at $p_*$ — carries
*identically zero* coupling between distinct conductor packets. There is no
estimation error here to improve away: the exact object has the null
structure.

**Lemma 3.3 (Amari–Chentsov inter-packet coupling at $p_*$). [P].**
In the same basis,

$$
T_{p_*}(\chi_k,\chi_\ell,\chi_m)
= n^{2}\sum_{y\in R}\chi_k(y)\chi_\ell(y)\chi_m(y)
= n^{2}\sum_{y\in R}e^{2\pi i(k+\ell+m)y/n}
= n^{3}\,\big[\,k+\ell+m\equiv 0\ (\mathrm{mod}\ n)\,\big].
$$

Hence the cubic coupling $(k,\ell,m)$ is nonzero **iff**
$k+\ell+m\equiv 0\ (\mathrm{mod}\ n)$ — again an exact integer predicate, no
tolerance.

*Proof.* $p_{*,y}^{2}=1/n^{2}$, so $T_{p_*}(u,v,w)=n^{2}\sum_y u_y v_y w_y$;
substitute the character basis and apply the same finite geometric-sum
vanishing. $\blacksquare$

### 3.2 The certificate

**Theorem 3.4 (Conductor blind spot). [P].**
Fix $R=\mathbb{Z}/n\mathbb{Z}$ with $n$ not prime (so that more than one
conductor packet exists). Then at $p_*$:

1. *(Q)* the Fisher form is block-diagonal across conductor packets
   (Corollary 3.2): the second-order curvature model class carries zero
   inter-packet coupling;
2. *(C)* there exist triples $(k,\ell,m)$ with $k+\ell+m\equiv 0\
   (\mathrm{mod}\ n)$ whose three legs lie in *distinct* conductor packets
   (Lemma 3.3): the Amari–Chentsov cubic carries nonzero inter-packet
   coupling.

Consequently there exists structured information — the cross-packet cubic
coupling — that is (i) provably present in the local information geometry at
$p_*$ and (ii) provably outside the representational capacity of any purely
second-order preconditioner at $p_*$. This is the conductor blind spot.

*Proof.* (Q) is Corollary 3.2. For (C) it suffices to exhibit, for the
relevant $n$, one $k+\ell+m\equiv0$ triple with legs in three distinct
conductor packets; the computational artifact (Section 4) enumerates *all*
such triples exhaustively for $n\in\{6,8,12,18,30\}$ and finds them in every
case (e.g., for $n=6$: $(1,2,3)$ with conductors $(6,3,2)$, all distinct). A
short structural argument that such triples exist for every non-prime $n$ is
given in Appendix A. $\blacksquare$

**Remark 3.5 (the witness has no tunable parameter).**
The entire certificate is two exact geometric-sum vanishing facts and an
integer predicate. There is no learning rate, no baseline, no benchmark, no
tolerance, no fitted tensor, no trained model. A referee cannot deflect it by
"the baseline was undertuned" because there is no baseline. This is the
property Section 1.1 identified as the reason the bounded claim survives
where the unbounded one does not.

**Remark 3.6 (sign-loss in squared-dot-product attention scoring is the program's cubic mass). [P] for the structural identity from Lemma 3.3 + Theorem 3.4; **[C, reduced]** for the correlation conjecture under [v2insert-04](v2insert-04.md) §3.1 three-outcome rule.**

Thomson 2026 §4.1 (*Algebraic Geometry as AI Accelerant*, ARTexplorer
preprint) proposes spread-based attention scoring
$s(q,k) = 1 - (q \cdot k)^2 / (Q(q) Q(k))$ as a softmax replacement
closed over $\mathbb Q$; the squaring discards $\operatorname{sgn}(q
\cdot k)$. For a categorical readout indexed by $R =
\mathbb Z/n\mathbb Z$, the real-valued characters come in conjugate
pairs $(\chi_k, \chi_{-k})$, and any cross-packet closing triple $(k,
\ell, m)$ with $k + \ell + m \equiv 0 \pmod n$ has a sign-partner
$(-k, -\ell, -m)$ (also closing, by Lemma 3.3) with identical packet
pattern. Hence the *unsigned* cubic mass
$|T_{p_*}(\chi_k, \chi_\ell, \chi_m)|^2$ is symmetric under
simultaneous character inversion, while the *signed* orientation of
the AC tensor against a chosen positive-frequency convention is exactly
what squaring destroys. The sign information lost by spread scoring is
therefore not incidental: it is precisely the cross-packet orientation
that Theorem 3.4 already identifies as missing from any quadratic
preconditioner. A $\mathbb Z_2$ polarity bit of the kind Thomson §6.5
names *Janus* restores this orientation as a typed companion channel —
a Cartan-slot instance in the sense of [Paper 30](30.constrained_overflow_incompatibility_budgets.md)'s typed
residual tuple. Under that augmentation, spread scoring carries cosine
magnitude through $(q \cdot k)^2$ and cross-packet orientation through
the $\mathbb Z_2$ flag; the unsigned-Fisher curvature class cannot use
either, but an attention head exposing the polarity flag can in
principle use the latter.

**Pre-registered correlation conjecture** (three-outcome, per [v2insert-04](v2insert-04.md) §3.1).
On any cyclic task $R = \mathbb Z/n\mathbb Z$ for which the Layer-2
cubic-mass estimator $\rho_x$ of §6.1 is defined, the per-task
performance gain from adding a $\mathbb Z_2$ polarity bit to a
spread-based attention head correlates with $\rho_x(R)$ across rings.
Three branches, all publishable:

- **(K)** positive slope: polarity-bit gain proportional to recovered
  cross-packet orientation; rings with higher cubic mass benefit more.
- **(L)** uncorrelated: sign information is not the dominant content
  the polarity bit recovers; the gain is structural-architecture noise.
- **(joint-on-disjoint)** correlates on one ring sub-family and
  anti-correlates on another: polarity-bit gain is mediated by a second
  factor (e.g., baseline degradation tier of squared scoring is itself
  task-dependent), and the structural dictionary {sign-loss} ↔
  {cubic mass} is correct but composed with a confound the audit must
  identify.

**Audit pointer.** The per-task cubic-mass estimator $\rho_x$ is
already implemented in [`empirical/paper34_conductor_blindspot_demo.py`](empirical/paper34_conductor_blindspot_demo.py)
(Layers 1 + 2, §4 + §6.1); the archived values cover $n \in \{6, 8,
12, 18, 30\}$. The correlation conjecture is settled by extending
[`empirical/paper34_layer3_cubic_experiment.py`](empirical/paper34_layer3_cubic_experiment.py) with a paired
with-/without-polarity-bit cell per ring on the same ladder — one CPU
training run per cell, additive on the existing Layer-3 sweep, and a
single linear-regression $\text{gain}_{\mathbb Z_2}(n) \sim \rho_x(n)$
across rings to adjudicate the three branches. Settles whether
Thomson §6.5's Janus polarity is doing the work it conjectures: if the
correlation is K-branch, the polarity bit is the architectural
realization of the typed Cartan-slot channel from [Paper 30](30.constrained_overflow_incompatibility_budgets.md),
matched to the cross-packet cubic content Lemma 3.3 enumerates; if L or
joint-on-disjoint, the polarity bit has different content and Thomson
§6.5's structural reading needs revision.

**Geometric instance ([Paper 01e](01e.simplicial_two_gauges_and_simplex_lattices.md), Thm. 12.5).** The same sign loss already occurs for a single tetrahedron. Under the Janus inversion $X\mapsto-X$ every quadrance is even ($Q(sX)=s^2Q(X)$) and the oriented volume is odd ($V(sX)=s^3V(X)$). The Cayley–Menger data therefore determine $V^2$ but never $\operatorname{sgn}V$: no function of quadrances recovers the absolute Janus bit. Relative bits are recoverable once five or more points are present, because a product $V(A)V(B)$ of two oriented volumes is a Cayley–Menger bideterminant, polynomial in the quadrances. The dictionary to this remark is exact. Quadrance plays the role of spread scoring. The products $V(A)V(B)$ correspond to the unsigned cubic mass $|T_{p_*}|^2$, both invariant under the global flip. $\operatorname{sgn}V$ corresponds to the signed cross-packet orientation, and fixing it is the job of the $\mathbb Z_2$ polarity flag. A second-order instrument reads products of two odd invariants, which are even, but never a single odd invariant. This also settles Thomson's relational-formulation question (*Geometric Janus Inversion* v10.7, open question 6) negatively for the absolute bit and positively for relative bits.

### 3.3 What the certificate is and is not

The certificate is a statement about the *representational capacity of a
model class at a point*. It is **not**:

* a claim about any trained network's optimization trajectory (that is
  Layer 3, Section 8, [C], pre-registered);
* a claim that the missed coupling is *task-relevant* — that it carries
  gradient signal whose neglect costs performance (that is the empirical
  question of Layer 3; the certificate proves the structure is *missed*,
  not that it is *valuable*);
* a claim that real second-order methods, which re-estimate curvature at
  the current point rather than at $p_*$, are blind off $p_*$ in the same
  exact form (Section 5 treats this precisely and shows it is the
  pre-registered question, not a corollary).

These three fences are the firewall. They are restated formally in Section 9.

---

## 4. The computational artifact (Layer 1, deterministic)

Layer 1 is accompanied by a single deterministic certificate program with no
seeds, no tolerances, and no floating-point in any vanishing decision (every
decision is an exact `(k-l) % n` or `(k+l+m) % n` integer test). The program
enumerates, for each ring in a ladder, the full conductor-packet
decomposition, verifies (Q) by checking that *every* cross-packet Fisher
entry is exactly zero, and verifies (C) by enumerating *all* surviving cubic
triples and counting those whose three legs lie in distinct packets.

Reported result (archived run): for every ring in the ladder
$n\in\{6,8,12,18,30\}$ — the program's canonical row, two squarefree rows,
and two rows with prime-power depth — condition (Q) holds (no cross-packet
Fisher entry; verified exactly) and condition (C) holds (cross-packet cubic
triples present; counts: $n{=}6\!:\!18$, $n{=}8\!:\!42$, $n{=}12\!:\!108$,
$n{=}18\!:\!252$, $n{=}30\!:\!774$). The certificate is therefore confirmed
on the full ladder; the pre-claimed falsifier branch (Fisher *not*
block-diagonal, or cubic with *no* cross-packet coupling, or the character
basis failing to diagonalize $g$) did not occur on any ring.

This artifact is the paper's Layer-1 evidence. It is exact and reproducible;
it makes no empirical claim. (In the program's internal record this is the
INSERT 16 settlement; reproduced here as the paper's computational
appendix.)

---

## 5. The maximum-entropy point: a dormant base case, not a convenience

The single most important methodological section. The objection to the
certificate is immediate and correct as far as it goes: *training does not
sit at maximum entropy*. We address it precisely, and we do not overclaim
the resolution.

### 5.1 Why $p_*$ is where the certificate is provable

At $p_*$ the conductor packets are *exactly* Fisher-orthogonal (Lemma 3.1).
$p_*$ is therefore the unique configuration at which (Q) is an identity
rather than an approximation, which is why a *clean theorem* is available
there and only there. It is also, by construction, the configuration of
maximum predictive uncertainty: the white-noise point, where the model has
learned nothing. The blind spot exists there but is *dynamically dormant* —
there is no structured signal to miss, so the missing capacity costs nothing.
This is not a weakness of the result; it is the reason the result is a
theorem rather than an empirical tendency.

### 5.2 How the displacement enters: through the cubic, anchored

Let $p=p_*+h$ with $h\in T_{p_*}\Delta_R^\circ$ the (small) displacement the
model accumulates as it leaves white noise. Expanding the Fisher form,

$$
g_p(u,v)=\sum_y\frac{u_y v_y}{p_y}
= n\sum_y u_y v_y\;-\;n^{2}\sum_y u_y v_y h_y\;+\;O(h^{2}),
$$

and the first-order correction is *exactly* the Amari–Chentsov cubic
contracted with the displacement,
$-\,T_{p_*}(h,u,v)$, by Lemma 3.3's identity in coordinate form. This is an
anchored algebraic fact, not a heuristic: **the very term that turns the
off-centroid Fisher metric away from block-diagonal is the cubic the
second-order model class cannot represent.** The coupling that "switches on
as the model leaves maximum entropy," in the anchor's words, *is* the
conductor blind spot's object, now made dynamically active by $h$.

### 5.3 What this does and does not license — stated with maximal care

It is tempting, and we explicitly resist it, to conclude "therefore the blind
spot strengthens along training." Here is the precise situation, with the
overclaim fenced.

A real second-order method does not precondition with $g_{p_*}$ forever; it
re-estimates curvature at the current $p$. Off $p_*$ the *true* Fisher
$g_p$ has acquired cross-packet entries (Section 5.2), and a method that
recomputed the exact Fisher at $p$ would see *those*. So the off-centroid
claim is **not** "the method never sees cross-packet coupling." The precise,
defensible statement is narrower and is the following conjecture, not a
theorem:

**Conjecture 5.4 (off-centroid persistence — Layer 3, [C], pre-registered).**
A second-order method preconditions with a *quadratic snapshot* of a
geometry whose cross-packet content is, to leading order, the image of a
*third-order* tensor under the running displacement (Section 5.2). It
therefore models the cubic-induced coupling as a static quadratic to be
re-estimated step by step, with no model of that coupling's *rate of change*
— which is exactly the third-order tensor, outside the quadratic model class.
We conjecture this produces a *persistent preconditioning-rate deficit along
ring-structured directions specifically*, observable as an
acquisition-rate asymmetry (Section 8), and *predict it is null on
index sets with no ring structure*.

Conjecture 5.4 is **not proven by this paper.** Its status is exactly that of
a pre-registered empirical hypothesis with a built-in negative control. The
relationship between Section 3 (Layer 1, proven, exact at $p_*$) and
Conjecture 5.4 (Layer 3, conjectural, off-centroid) is precisely the
relationship between a clean base case and an unproven inductive step. We
state it that way, in those words, in the abstract and the conclusion,
because eliding the gap is the single failure mode that would return this
paper to the unpublishable class of Section 1.1.

---

## 6. Layer 2 — the conductor diagnostic (proposed; runnable, no retraining)

The certificate hands us, for free, a *measurement instrument*. This is the
paper's most immediately usable contribution and the part most likely to be
underweighted; we therefore foreground it.

### 6.1 The diagnostic, specified

Given any trained model with a categorical head over a ring-structured index
$R=\mathbb{Z}/n\mathbb{Z}$, and any evaluation batch:

1. **Form the update direction on the head.** For cross-entropy training the
   per-example logit-gradient is the centered score frame $e_y-p$; average
   over the batch to obtain the mean update direction $u$ on the simplex
   tangent space. (For a second-order method, also form the *preconditioned*
   update $u_{\mathrm{prec}}=M^{-1}u$, where $M$ is the method's curvature
   model.)
2. **Transform to the conductor-packet basis.** Compute the discrete
   additive-character transform of $u$ (an $n$-point DFT on the index),
   group coefficients by conductor $d\mid n$, $d>1$.
3. **Compute the cross-packet cubic mass.** Using the exact selection rule
   $k+\ell+m\equiv0\ (\mathrm{mod}\ n)$, evaluate the fraction of the
   third-cumulant contraction $T_p(u,u,u)$ (and the mixed
   $T_p(\cdot,u,u)$ operator mass) carried by triples whose legs span
   distinct conductor packets.
4. **Report two numbers.** (a) The *cross-packet cubic mass fraction*
   $\rho_\times$ — how much of the update's third-floor structure lives in
   the directions the certificate proves the quadratic model class cannot
   couple. (b) The *preconditioner discard ratio* — comparing $u$ and
   $u_{\mathrm{prec}}$ on the cross-packet subspace, how much of
   $\rho_\times$ the deployed second-order method treats as if it were in
   its block-diagonal quadratic model.

### 6.2 Why a diagnostic is the right contribution

A diagnostic makes *no performance claim* and therefore cannot be
desk-rejected for an undertuned baseline. It converts the unfalsifiable
"optimizers miss structure" into a *measured quantity per model per task*,
computable on existing checkpoints with no retraining. It is the instrument
that *generates* the evidence for or against Layer 3 rather than presupposing
it. In the program's tiering, the diagnostic is [P] in its definition
(it is a deterministic computation derived from the Section 3 certificate)
and [A] in its empirical interpretation (the claim that a large
$\rho_\times$ with a high discard ratio indicates a *consequential* deficit
is pending the Layer-3 audit, Section 8).

### 6.3 Specification of the diagnostic computation (to be implemented)

We specify, but do not in this paper implement, the following computation:

* **D1 — checkpoint sweep.** For a family of public checkpoints with a
  ring-structured categorical head (candidate heads in Section 8.3),
  compute $(\rho_\times,\text{discard ratio})$ across training time. Output:
  a curve of cross-packet cubic mass vs. training step. No claim is attached
  to the curve's shape in this paper; the curve *is* the deliverable.
* **D2 — basis-ablation control.** Recompute D1 after a fixed random
  permutation of the label set that destroys the additive-group meaning
  while preserving dimension and entropy. If the diagnostic is measuring
  something real about ring structure, $\rho_\times$ under D1 must differ
  from $\rho_\times$ under D2 in a way that vanishes when the index has no
  genuine ring structure. D2 is the diagnostic's own internal falsifier.

---

## 7. Relation to existing work (the three steelmen)

We make the relation to the three nearest bodies of work explicit and adverse
to ourselves, since each contains a referee who would, correctly, ask why the
result is not already theirs. (Citations are by result-content; exact
references to be completed in v0.2.)

### 7.1 Amari and information geometry

Information geometry named the Fisher metric as the second cumulant and the
Amari–Chentsov tensor as the third, and studies the cubic as a curvature
correction (the $\alpha$-connections, the e/m duality, higher-order
natural-gradient schemes). A referee from this tradition asks: *is this not
just the well-known fact that natural gradient is second-order and the cubic
is a known correction?* **Where it stops short:** the IG literature treats
the cubic as a correction to the *trajectory* on a generic exponential
family; it does not, as a habit, place an arithmetic ring structure on the
*outcome index* and ask what the quadratic model class can represent in the
induced additive-character basis. The novelty here is neither "the cubic
exists" nor "natural gradient is incomplete," both classical, but the **exact
conductor selection rule** $k+\ell+m\equiv0\ (\mathrm{mod}\ n)$ that names
*which* directions the second-order class is constitutionally unable to
couple, as a finite decidable fact in a specific basis.

### 7.2 The empirical-Fisher critique

A body of work shows that the *empirical Fisher* used by adaptive methods is
a poor proxy for the *true Fisher*, and that this explains some
disappointments of second-order methods. A referee asks: *are you not
rediscovering that the empirical Fisher is a bad curvature estimate?* **Where
it stops short, and why this is stronger:** that critique concerns the
*quality of the estimate* of the curvature. Theorem 3.4 concerns the
*representational capacity of the exact object*. Even an oracle that returned
the exact true Fisher at $p_*$ carries identically zero cross-packet
coupling (Corollary 3.2). The deficit is in the model class, not the
estimator; it cannot be improved away by better estimation. This is a
different and deeper statement than the empirical-Fisher critique and is not
implied by it.

### 7.3 Grokking and modular-arithmetic mechanistic interpretability

The closest and most dangerous referee. This literature shows *empirically*
and *post hoc* that networks trained on modular arithmetic learn
additive-character ("Fourier") features, and documents the delayed,
sudden generalization ("grokking") on such tasks. A referee asks: *do you not
merely re-derive that modular tasks have Fourier structure, already known?*
**Where it stops short, and what is genuinely new:** that work characterizes
the *learned representation*, after training, as an empirical phenomenon on
synthetic modular tasks. Theorem 3.4 is an *a priori* statement about the
*optimizer's curvature model class*, independent of any network or task: the
quadratic class *cannot precondition the cross-packet cubic at all*. This
yields a *mechanistic, falsifiable prediction* the interpretability
literature does not state in this form: ring-structured features are
preconditioned at first-order rates while non-ring features receive
second-order acceleration, predicting an *acquisition-rate asymmetry* whose
signature is consistent with — and sharper than — the qualitative
description of grokking's delay. We claim this as a *prediction to be tested*
(Section 8), explicitly **not** as an explanation of grokking; the
explanatory claim is fenced at [C].

---

## 8. Layer 3 — the pre-registered experiment (NOT run)

We pre-register a single experiment with a built-in negative control and
pre-claim both outcome branches, so that a negative result is reported as a
result and not reframed. Nothing in this section is run in this paper; this
is the protocol, fixed in advance.

### 8.1 Hypothesis and the exact prediction

From Conjecture 5.4: a *cubic-aware correction* — even the cheapest
nontrivial one, the conductor-packet-resolved component of the
Amari–Chentsov operator $K^{CH}_p$ added to the preconditioner — should
**accelerate the acquisition of ring structure if and only if ring structure
is present**, and be **null when it is absent**. The asymmetry, not the
main effect, is the hypothesis. On a delayed-generalization (grokking) task
the sharp prediction is: the cubic-aware correction *reduces the
generalization-delay gap on the ring-structured task specifically*, and does
not reduce it on the matched non-ring control.

### 8.2 Design (pre-registered)

* **Arms.** (i) matched second-order baseline (e.g., K-FAC or a
  Fisher-preconditioned optimizer), tuned to best effort; (ii) identical,
  plus the conductor-resolved cubic correction of Section 8.1.
* **Tasks.** (T1) a genuinely ring-structured categorical task — modular
  addition over $\mathbb{Z}/n\mathbb{Z}$, the canonical grokking testbed;
  (T2) the *negative control* — the *same task* under a fixed random
  permutation of the label set that destroys additive-group meaning while
  preserving dimension, entropy, and sample statistics (the Section 6.3 D2
  ablation, promoted to an experimental arm).
* **Primary endpoint.** The *interaction*: (delay-gap reduction on T1)
  minus (delay-gap reduction on T2). The hypothesis predicts a *positive
  interaction*; the main effects alone are explicitly **not** the endpoint,
  because a main effect without the asymmetry is consistent with generic
  preconditioning improvement and does not bear on the conductor mechanism.
* **Pre-claimed branches (matched-pair discipline).**
  *Branch A (confirms):* positive interaction — cubic-aware specifically
  accelerates ring-structure acquisition and is null on the control.
  *Branch B (falsifies):* zero or negative interaction — cubic-aware helps
  both or neither, or helps the control as much as the task. Branch B is a
  full result: Theorem 3.4 and the diagnostic stand regardless (they make no
  trajectory claim), and Conjecture 5.4 is then reported as **refuted on the
  tested instance**, recorded, not reframed.

### 8.3 Where ring structure is actually present (scope, stated soberly)

The practical reach of Layer 3 is bounded by where ring structure genuinely
occurs. Honest candidate categorical heads: modular/cyclic synthetic tasks
(cleanest, the grokking testbed); calendar- and clock-token prediction
(weekday/month/hour heads with genuine $\mathbb{Z}/7,\mathbb{Z}/12,
\mathbb{Z}/24$ structure); cyclic or rotational classification labels;
positional schemes with modular structure. We explicitly do **not** assert
that general next-token prediction over a natural-language vocabulary has
exploitable ring structure; whether any latent periodic subword structure
makes $\rho_\times$ nontrivial there is itself an instance of the Layer-2
diagnostic D1, to be measured, not assumed.

---

## 9. Safe and unsafe statements (the firewall, explicit)

In the program's convention we state plainly what may and may not be claimed.

**Safe (this paper asserts):**

* At $p_*$, on a ring-structured categorical model, the Fisher form is
  exactly conductor-block-diagonal and the Amari–Chentsov cubic has exact
  cross-packet coupling under $k+\ell+m\equiv0\ (\mathrm{mod}\ n)$
  (Theorem 3.4, [P], with deterministic artifact for
  $n\in\{6,8,12,18,30\}$).
* Therefore the second-order curvature *model class*, independent of
  estimation quality, has a structural null space exactly aligned with a
  coupling provably present in the local geometry *at $p_*$* — the
  conductor blind spot.
* A retraining-free diagnostic ($\rho_\times$ and the preconditioner
  discard ratio) is well-defined and computable on existing checkpoints
  (Section 6, [P] in definition).
* The off-centroid persistence of the deficit, the task-relevance of the
  missed coupling, and the connection to grokking's delay are stated as a
  single pre-registered experiment with a negative control and both branches
  pre-claimed (Section 8, [C]).

**Unsafe (this paper does NOT assert; asserting any of these would return
the work to the unfalsifiable class of Section 1.1):**

* That trained networks' optimization trajectories *are* governed by
  conductor geometry. (That is the suggestive empirical claim of the
  program's prior discrete-Fisher work, with the documented LLM
  conductor-energy split as *suggestive evidence only*; its tier is
  unchanged by this paper and it is firewalled from Theorem 3.4.)
* That the missed coupling is necessarily *task-relevant* or that
  correcting it necessarily improves performance. (That is exactly the
  Layer-3 endpoint, unrun.)
* That the certificate is exact off $p_*$ in the same form. (It is exact
  *at* $p_*$; off-centroid is Conjecture 5.4, [C].)
* That this *explains* grokking. (It *predicts a testable asymmetry*
  consistent with grokking's delay; the explanatory claim is not made.)
* Any claim involving a physical constant, a specific learning rate, or a
  specific model's measured behavior. The paper emits a theorem, a
  measurement procedure, and a protocol; it emits no benchmark number.

---

## 10. Scope, limitations, and the honest assessment

The certificate is exact and unconditional **at the maximum-entropy point**
and for **cyclic** ring structure $\mathbb{Z}/n\mathbb{Z}$. It is verified
computationally on five rings spanning squarefree and prime-power-depth
cases. Its three principal open edges, each stated as a definite next
computation rather than a hope:

* **Off-centroid persistence (the central open question).** Conjecture 5.4.
  Resolved, in the affirmative or negative, only by the Layer-3 experiment.
  The paper's credibility rests on stating this as open, not closed.
* **Non-cyclic ring structure.** Whether the certificate holds for
  $(\mathbb{Z}/2)^k$, product rings $\mathbb{Z}/p\times\mathbb{Z}/q$, and
  other finite abelian index structures. This is a *deterministic* extension
  computation in the exact-arithmetic family of Section 4 — decidable, no
  training — and is the recommended immediate follow-on certificate
  (Appendix B sketches it).
* **Prime-power-depth structure.** The artifact already includes $n=8,18$;
  whether the cross-packet structure is qualitatively richer at higher
  prime-power depth is a finite enumeration, decidable, recommended.

Honest assessment: Layer 1 is a small, exact, defensible theorem with no
tunable adversary surface — its value is precisely its narrowness. Layer 2 is
the immediately useful artifact and the one we expect to matter most in
practice, because it converts an intuition into a measurement that generates
its own evidence. Layer 3 is the prize and is explicitly not claimed; its
negative result is as publishable as its positive one, which is the property
that makes it worth pre-registering. The paper's best defense is its
discipline: it states the bounded version of a claim whose unbounded versions
have repeatedly failed, and it keeps the layers apart even where conflating
them would be more exciting.

---

## 11. The computational program (what we recommend pursuing, in order)

For the empirical/computational work this paper specifies but does not
perform, in priority order:

1. **C1 — the Layer-1 artifact (done).** The deterministic certificate over
   $n\in\{6,8,12,18,30\}$, exact arithmetic, both branches pre-claimed.
   Status: complete; it is the paper's computational appendix.
2. **C2 — the off-centroid persistence certificate (deterministic, next).**
   *Without any training*: along a synthetic ray $p(t)=p_*+t\,h$ for
   ring-structured $h$, compute exactly the fraction of the local Fisher's
   cross-packet content that a step-wise re-estimated quadratic can recover
   versus the residual that provably requires the third-order tensor
   (Section 5.2). This is finite-dimensional exact linear algebra along a
   ray — decidable, no model, in the Section 4 family — and it *sharpens
   Conjecture 5.4 toward a theorem* on the synthetic ray without performing
   the full experiment. Highest-value next computation; firewall-clean.
3. **C3 — the diagnostic D1/D2 (Section 6.3).** Implement $\rho_\times$ and
   the preconditioner-discard ratio; run the checkpoint sweep and the
   basis-ablation control on a small ring-structured task and one public
   model with a calendar/clock head. Produces a curve, no performance
   claim; D2 is its internal falsifier.
4. **C4 — the non-cyclic / product-ring extension certificate
   (deterministic).** Re-run C1 on $(\mathbb{Z}/2)^k$ and
   $\mathbb{Z}/p\times\mathbb{Z}/q$. Decidable; characterizes whether the
   blind spot is cyclic-specific or general abelian.
5. **C5 — the Layer-3 pre-registered experiment (Section 8).** Run *only*
   after C2 and C3, with the protocol and both branches fixed in advance by
   Section 8.2. This is the prize and the only step that touches training; a
   negative interaction is a full, reportable result.

The ordering is deliberate: every step before C5 is deterministic, exact,
and firewall-clean, and each *generates evidence about C5's hypothesis
without presupposing it*. C5 is the only step with an adversary surface, and
it is entered last, pre-registered, with the negative branch already written
down.

---

## Conclusion

We have shown, exactly and with no tunable parameter, that on a
ring-structured categorical model at maximum entropy the second-order
curvature model class has a structural null space precisely aligned with a
cross-packet cubic coupling that provably exists — the conductor blind spot.
The result is deliberately small. Its smallness is the point: it is the
bounded form of a claim whose unbounded forms ("optimizers miss structure")
have repeatedly failed review for lack of an exact witness, and the bounded
form has an exact witness and therefore no baseline to dispute. From the
certificate we derived a retraining-free diagnostic that turns the intuition
into a measurement, and we pre-registered a single sharp experiment, with a
negative control and both branches pre-claimed, whose negative result would
be as informative as its positive one.

We state once more the discipline that the paper's credibility depends on:
Layer 1 is proven and exact *at the maximum-entropy point*; whether the
deficit persists along a training trajectory is the explicit, pre-registered,
unproven question of Layer 3, related to Layer 1 as an unproven inductive
step is related to a clean base case. We have refused, throughout and on
purpose, the more exciting unbounded statement, because the entire reason a
bounded statement of this kind is worth making is that it is the only one
that survives contact with an adversary who wants it to fail.

---

**Data and reproducibility.** The Layer-1 certificate is a deterministic,
exact-arithmetic program over $n\in\{6,8,12,18,30\}$ with no seeds, no
tolerances, and no floating-point in any vanishing decision; archived with
its full run transcript. Layers 2 and 3 are specified (Sections 6, 8, 11)
and explicitly not performed in this paper.

**Tier summary.** Theorem 3.4 and Lemmas 3.1–3.3: **[P]**. The diagnostic of
Section 6: **[P]** in definition, **[A]** in empirical interpretation.
Conjecture 5.4 and the entirety of Layer 3 (Section 8): **[C]**,
pre-registered. No claim crosses from a lower tier to a higher one anywhere
in the paper; the firewall of Section 9 is binding.

---

*Draft v0.1. The Riemann-style discipline of the broader program is applied
here in full: a bounded theorem with an exact witness, an honestly tiered
diagnostic, and a pre-registered experiment whose falsifying branch is
written down before the experiment is run. The unbounded claim — that deep
learning's optimizers are, in deployment, governed by or blinded along their
trajectories by conductor geometry — is named precisely so that it can be
seen not to be claimed.*

---

## Appendix A — existence of cross-packet $k+\ell+m\equiv0$ triples for non-prime $n$ (sketch)

For non-prime $n$ let $d_1\mid n$ and $d_2\mid n$ be two distinct nontrivial
divisors with associated packets. Choosing $k$ with $\mathrm{cond}(k)=n$
(a generator-class character, conductor $n$), and $\ell$ with
$\mathrm{cond}(\ell)=d$ for a proper divisor $d$, the third leg
$m\equiv-(k+\ell)\ (\mathrm{mod}\ n)$ generically has conductor distinct from
both (its conductor is $n/\gcd(k+\ell,n)$, and $k$ of conductor $n$ forces
$\gcd(k+\ell,n)$ away from the values fixing $\mathrm{cond}(\ell)$ for
suitable $\ell$). The artifact's exhaustive enumeration confirms a nonempty
cross-packet set for every $n$ in the tested ladder; the general statement
for all non-prime $n$ is a finite divisor-lattice argument completed in
v0.2. (Marked [A] pending that completion; the per-$n$ statement for the
tested ladder is [P] by exhaustive enumeration.)

## Appendix B — the non-cyclic extension certificate (specification)

Replace $\mathbb{Z}/n\mathbb{Z}$ by a finite abelian group $G$
(e.g. $(\mathbb{Z}/2)^k$ or $\mathbb{Z}/p\times\mathbb{Z}/q$); the additive
characters become the Pontryagin dual $\widehat G$, the conductor of a
character is the order of its restriction structure, and packets group
characters by that invariant. Lemmas 3.1 and 3.3 carry over verbatim with
character orthogonality over $G$ and the selection rule
$\chi_k\chi_\ell\chi_m=\mathbf{1}$ in $\widehat G$. The certificate is then a
finite enumeration over $\widehat G$, decidable in the exact-arithmetic
family of Section 4. This is computation **C4** of Section 11.
