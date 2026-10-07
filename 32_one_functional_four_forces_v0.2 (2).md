# One Functional, Four Forces of Description: The Cumulant Tower as Categorical Effective Action

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*Consolidated draft 0.4 — October 1, 2026*

<!--
INTERNAL LOG — NOT FOR PUBLICATION (pandoc drops HTML comments)
v0.4 (2026-10-01): Phase-2 propagation of Paper 54 (54_one_functional_from_passivity.md), the foundations
paper that derives Phi from the Port Principle's copy lift. Edit ledger (file:section -> old -> new):
  L1  Abstract p1: "Phi ... is a categorical effective action ... two exact identities (space=mass; time,
      energy, GRAVITY = Noether generator + obstruction)" -> Phi derived (Paper 54); one exact identity
      (space = mass = static FDT, equilibrium only) + one exact localization; gravity reading [C].
  L2  Abstract p3: "dimensional selection principle ... by two independent routes" -> selection statement whose
      content is "angular momentum is a vector iff n=3" (Def 8.1 encodes it); the Z/6 1+2 count is row-specific
      (Z/30: 1+2+4=7), on a different row, NOT an independent route; "space=3D is the certificate of having
      mass" -> [C].
  L3  Abstract p4: "classical signature (3,1) ... forced by the -l3 sign" -> contact sign of extended phase
      space, present in every dimension; "reproduces ... sin^2 theta_W = 3/8" -> textbook SU(5) given the 2+3
      split and Lambda^2 E + E* [A]; "firewall -- now a theorem" -> principle, true by construction.
  L4  Abstract closing line: "the form of gravity ... and the selection of dimension three are [claimed]" ->
      derived functional + equilibrium identity, exact localization, selection for an inertial projector as
      defined.
  L5  sec 1.1 items 1, 2, 6, 7, 10: retiered as in L1-L3 (item 1 now cites Paper 54 Thm 1; item 2 splits into
      [P] FDT/localization + [C] gravity; item 6 "two independent derivations agree" removed; item 7 contact
      sign; item 10 [P, structural] -> [A]).
  L6  sec 2 Claim 2.1: "[P]" posited -> "[P, derived in Paper 54 Thm 1]" with the three properties mapped
      (grad = free state; stationarity = Gibbs variational principle; convexity = passivity, Fenchel-Young).
  L7  sec 3 Thm 3.1: added "Content (Paper 54 Thm 2)": static FDT; equilibrium-only; Paper 54 Thm 3 gives the
      falsifiable non-equilibrium extension (defect = stationary current).
  L8  sec 4 Thm 4.1: tier "[P]" -> "[P] items 1-2 and the localization in item 3; [C] the gravity reading of
      item 3"; sec 4.A pillars (i), (iv) re-anchored to Paper 54; "three of four pillars inherited
      unconditionally" -> the mapping of pillars is [A].
  L9  sec 8: Thm 8.2 route 1 annotated (restates Def 8.1); Thm 8.3 "independent route ... same dimension" ->
      Z/6-row fact, not independent (Z/30 gives 7; Q=6 row vs Q=4 row); Cor 8.4 [P] -> [C].
  L10 sec 9.1: "Theorem 9.1 (Forced classical (3,1)) [P]" -> "Theorem 9.1 (The contact sign of the
      Poincare-Cartan form) [P for the sign; A for the (3,1) reading]".
  L11 sec 10.1 / 10.3 / 10.4: Weinberg angle and hypercharges "[P, computed]" -> [A] with provenance
      (Georgi-Glashow; Y ~ (1/2,-1/3) forced by tracelessness on any p1+p2 split; inputs are a direct sum and a
      chosen representation).
  L12 sec 10.2 table: Lorentzian row "[P] local-tangent" -> "[P] local-tangent, post-diagnosis (after the
      sec 14.2 refutation)".
  L13 sec 12: "Theorem 12.1 (The Firewall Theorem) [P]" -> "Principle 12.1 (The Firewall Principle; by
      construction)"; heading and every in-paper "Theorem 12.1"/"Firewall Theorem" reference updated
      (sec 9.6, 12.2, 13.1, 15.1 F7, 16.1a, 16.5).
  L14 Rem 16.2b: R = AN(T) credited to classical Hessian geometry (Shima 2007; Amari-Nagaoka 2000), valid at
      every point of every Hessian metric; K = 1/4 holds at every point (Paper 54 Prop 5.2, cert K4).
  L15 Conclusion: same relabels as L1-L3, L13.
  L16 References: + Paper 54, Shima 2007, Georgi-Glashow 1974.
  L17 Abstract italic lead (subtitle): "Gravity as Time-Translation Closure Defect" -> "Gravity Read as the
      Time-Translation Closure Defect [C]"; sec 12 / App A "firewall theorem" -> "firewall principle" (2 spots).
  FWD (2026-10-01) -> Paper 55 (55_the_network_of_ports.md): the sec 14.2 Euclidean-4 verdict holds for one node and is explained (a node has no propagation symbol); a NETWORK of ports has Lorentzian symbol (1,d) iff it stores energy capacitively + inductively with passive stiffness (P55 Thm 3.5; c = 1/sqrt(LC) realizes the Conj 9.4 asymptote mechanism); gap G3 partially closed (cone, cuts, arrow; dimension not selected). Not propagated here.
-->

---

## Abstract

*Space as Second Cumulant, Gravity Read as the Time-Translation Closure Defect [C], and 3+1 as a Lift Phenomenon.*

We identify a single object beneath the information-geometric mechanics of Papers 13–31 and show that it *answers*, rather than merely guards, the questions the series has circled. The cumulant tower of the categorical log-partition $\Phi=\log Z$ — the generating function of the completely passive (Gibbs) states, *derived* from the port constraint in Paper 54 rather than posited — is a categorical effective action, and its successive derivatives are the objects ordinary physics names separately only because it presupposes a manifold: position, the Fisher metric *as simultaneously space and inertia*, the Amari–Chentsov force, and, as a reading, the time-translation closure defect. This yields one exact identity and one exact localization. *Space and mass are the same (second) cumulant*: this is the static fluctuation–dissipation theorem, which holds in the free states and fails away from equilibrium by the stationary current (Paper 54, Theorems 2–3). *Time and energy are the time-translation Noether generator*, and the obstruction to integrating it after coarse-graining is exactly localized; reading that obstruction as gravity is a conjecture [C].

We make this computational by proving the explicit five-slot projection-closure certificate (Paper 31, Def. 5.1) for the time-translation projection on $R=\mathbb{Z}/6\mathbb{Z}$. From the exact cubic structure constant $T_{klm}=216\cdot\mathbb{1}[k{+}l{+}m\equiv 0\bmod 6]$ — a Pontryagin identity, basis-independent and stable to all centroid orders — the certificate is closure-valid *exactly* on the single-prime block $A_2\oplus A_3$, re-deriving Paper 17's Cartan $\mathfrak{u}(1)^2$ exhaustion from projection closure rather than representation theory, while its entire typed, bounded, recurrent residual is provably supported on the conductor-6 carry packet $M$ — coinciding with $\operatorname{Ext}_{CH}$ (Paper 13), the simplex-mass jerk (Paper 20), and the dark-matter-adjacent residual Paper 28 could only name, with non-tachyonicity *identical* to Paper 22's primorial Noether–Weil positivity at the $P_2=2\cdot3$ row. A single congruence, $3{+}3{+}3\equiv 3\not\equiv 0$, is shown to be the common arithmetic root of four otherwise-independent corpus results (§6).

From this we obtain a **dimensional selection statement**: an inertial projector (one Hamiltonian, one energy, one rotation axis, one $J^2={-}I$) admits a closure-valid self-model in *exactly one* row of the Fisher-volume hierarchy, $Q=4$, spatial dimension three. Its content is the classical fact that angular momentum is a vector iff $n=3$ ($\dim\mathfrak{so}(n)=n$), which the definition of an inertial projector encodes. The $1{+}2$ conductor count of the $\mathbb Z/6$ row is a row-specific fact on a different row ($\mathbb Z/30$ gives $1+2+4=7$), not an independent second route. The reading that experiencing space as three-dimensional is the closure certificate of having mass is [C].

The Poincaré–Cartan form carries the contact sign $-\mathcal E_3\,dt$ of extended phase space — present in every dimension, so it does not select $(3,1)$ — and the classical dispersion is Galilean (parabolic); Lorentzian $3+1$, nonabelian gauge restoration, and the imaginary leakage energy are conjectured — and reduced to one runnable check — to be a single Bures-lift event (one lift, several faces). As a structural by-product, once the $2+3$ split and the representation $\Lambda^2E\oplus E^*$ are put in, the framework reproduces the textbook $SU(5)$ tree-level Weinberg angle $\sin^2\theta_W=3/8$ and the one-generation hypercharge spectrum [A], under a **dimensional firewall** — a principle, true by construction — that admits only conductor-fixed *pure numbers*, never a dimensionful magnitude. Each $[P]$ result is anchored to peer-reviewed external precedent (Zhang–Li divergence-symplectic geometry; the Koszul–Souriau–Fisher capacity identity; the Souriau symplectic-cohomology cocycle) without adopting the emergent-gravity ontology this paper explicitly positions against.

**Gravity is not claimed. Claimed are the derived functional and its equilibrium identity (via Paper 54), the exact arithmetic localization of the closure residual, and the selection of dimension three for an inertial projector as defined.**

**Keywords:** information geometry, categorical effective action, cumulant tower, Amari–Chentsov tensor, Nambu–Fisher mechanics, projection-closure certificate, conductor packets, Cartan exhaustion, dimensional selection, Galilean–Lorentzian lift, Souriau cocycle, Bures completion, simplex mass term, Weil positivity.

---

## 1. Scope and Claim Status

This paper consolidates the series into one statement and discharges, in part, the guardrail of Paper 31 §13 ("projection-closure theory explains the *form* of the gravity question, not gravity itself"). The discharge is partial and explicitly typed. We use a three-tier status convention throughout.

- **[P] Proven here, unconditionally**, given Papers 13 and 17 as cited.
- **[A] Structural, pending a named finite audit.** The argument is complete; one specified finite computation converts it to [P] or refutes it.
- **[C] Conjectural, reduced.** Stated with an explicit falsifier and a single runnable verification; asserted not as true but as *seen and reduced*.

### 1.1 Claims kept on the table

1. **[P]** $\Phi=\log Z$ is the generating function of the free (completely passive) states — *derived* in Paper 54, Theorem 1 — and in that sense a categorical effective action; its first cumulant-tower derivatives are position, the Fisher metric (= space = inertia, the static FDT), and the Amari–Chentsov force. Reading the next order as the time-translation closure defect is the structure of §4–§5; reading that defect as gravity is [C].
2. **[P]** *Space and mass are the same tensor* (second cumulant): the static FDT, an equilibrium identity (Paper 54, Theorem 2), broken away from equilibrium by the stationary current (Paper 54, Theorem 3). *Time and energy share the time-translation Noether structure*, whose closure failure is exactly localized (§5). **[C]** That closure failure is the form of gravity.
3. **[P]** The explicit five-slot time-translation closure certificate on $R=\mathbb{Z}/6\mathbb{Z}$: closure-valid exactly on $A_2\oplus A_3$; typed bounded recurrent residual localized to the conductor-6 packet $M$. The selection rule is proved exactly (Lemma 5.1a: the cubic structure constant is $216\cdot\mathbb{1}[k{+}l{+}m\equiv 0\bmod 6]$ by Pontryagin duality), basis-independently (5.1b), and stably to all centroid orders (5.1c); the packet partition is the exhaustive six-multiset enumeration (Lemma 5.1) with three exact consequences (Corollary 5.1d).
4. **[P]** This re-derives Paper 17's Cartan $\mathfrak{u}(1)^2$ exhaustion from projection closure, independently of representation theory.
5. **[P]** The conductor-6 residual coincides with $\operatorname{Ext}_{CH}$ (Paper 13 §11), the simplex-mass jerk (Paper 20), and Paper 28 §13's dark-matter-adjacent residual; its non-tachyonicity is the cubic-order instance of Paper 22's Weil positivity.
6. **[P]** Dimensional selection: an inertial projector, as defined (Def. 8.1), closes in exactly one row, $Q=4$, spatial dimension three. Its content is "angular momentum is a vector iff $n=3$"; the $\mathbb Z/6$ conductor count of Theorem 8.3 is a row-specific fact, not an independent second derivation.
7. **[P]** The Poincaré–Cartan form carries the contact sign of extended phase space (present in every dimension); the classical dispersion is Galilean (parabolic); no classical Lorentz structure, consistent with the series. **[A]** Reading the $3$ Fisher directions plus the contact direction as a signature $(3,1)$.
8. **[A]** Residual stays on the squarefree conductor-6 mode and sign-definite under prime-power depth — pending the $\mathbb{Z}/6\hookrightarrow\mathbb{Z}/12,\mathbb{Z}/18$ audit (§14.1).
9. **[C]** Lorentzian $3+1$ is a Bures-lift phenomenon, unified with gauge restoration and the imaginary energy — reduced to the Bures-dispersion audit (§14.2). The Euclidean-4 alternative is itself a stated result.
10. **[A]** Given the $2+3$ split $E=\mathbb C^2\oplus\mathbb C^3$ and the representation $\Lambda^2E\oplus E^*$, the tree-level Weinberg angle $\sin^2\theta_W=3/8$ and the one-generation SM hypercharge spectrum follow as in textbook $SU(5)$ (§10), subject to the dimensional firewall (§12): only pure numbers, never magnitudes.

### 1.2 Terminology

We keep "cubic" for third-cumulant order and "row" for a fixed modulus $R$, following Papers 13–28. "Inertial projector" is defined in §8. "Closure-valid" and the certificate tuple are Paper 31. "Lift" always means the Bures density-matrix completion of Paper 18.

### 1.3 Dependency spine

- **Paper 13** — simplectic / Nambu–Fisher mechanics; the Fisher volume form as non-binary replacement for $\omega$; the $N=4$ axis-to-2-form miracle; $K^{CH}$ as momentum gap; $\operatorname{Ext}_{CH}$ as finite carry term; centroid convolution form of $K^{CH}$.
- **Paper 14** — Cartan obstruction; admissible real-cone, CRT-compatible derivations reduce to the Cartan subalgebra.
- **Paper 17** — cubic action–energy theorem; $\mathcal A_3$ vs $\mathcal E_3$; Cartan exhaustion of cubic charges; the $\mathbb{Z}/6\hookrightarrow\mathbb{Z}/12,\mathbb{Z}/18$ Constraint-3 audit.
- **Paper 18** — Bures density-matrix lift; restoration of nonabelian $\mathfrak{su}(2)\oplus\mathfrak{su}(3)$; jerk → leakage width; the $\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O}$ terminator.
- **Paper 19** — long-time dynamics: recurrent, non-chaotic, bounded leakage.
- **Paper 20** — jerk as simplex mass term; projected curvature of $\mathcal E_3$; complex/negative energy in the projection channel.
- **Paper 21** — primorial / three-prime extension; quartic obstruction question.
- **Paper 22** — primorial cumulant Noether theory; Noether positivity ⇒ Weil positivity ⇒ RH; low-order agreement at quadratic and cubic order.
- **Papers 28–31** — irreducible ternary mechanics; participation; typed residual budgets; projection-closure certificates; the gravity guardrail this paper partially discharges.
- **T-series (T0–T14)** — the general substrate that promotes §5's $\mathbb{Z}/6$ computation from a worked instance to an instance of general theorems; summarized in Appendix A.

---

## 2. The One Functional

Let $R$ be a finite modulus, $Q=|R|$, $\Delta_R^\circ$ the open categorical simplex, $H_R=\{u:\sum u_a=0\}$ its tangent hyperplane, and $\Phi(\theta)=\log Z(\theta)$ the log-partition of the categorical exponential family in $e$-affine coordinates. Information geometry gives the cumulant tower as the covariant derivative ladder of $\Phi$:
\[
\nabla^{(0)}\Phi=\text{mean }\theta\text{-dual centroid},\qquad
\nabla^{(2)}\Phi=g\;(\text{Fisher}),\qquad
\nabla^{(3)}\Phi \sim T=K^{CH},\qquad
\nabla^{(e)}T=T^{(4)}.
\]

**Claim 2.1 (Categorical effective action). [P, derived in Paper 54, Theorem 1]**
*Derivation.* $\Phi$ is not posited. Complete passivity under the copy lift forces the Gibbs state (Port Principle, Theorem 6.3), the Gibbs states over all Hamiltonians are the categorical exponential family with natural parameter $\theta=-\beta H$, and $\Phi=\log Z$ is their generating function (Paper 54, Theorem 1). The three properties attributed to $\Phi$ below are, respectively: $\nabla\Phi$ is the free state; stationarity of $\langle\theta,p\rangle+S(p)$ is the Gibbs variational principle; and convexity is passivity in Fenchel–Young form, with gap the relative entropy $D(\rho\|p_\theta)$. The effective-action vocabulary is a name for this; the physics identifications below carry their own tiers.

$\Phi$ plays the role a physical effective action plays in field theory: a single convex functional whose derivative with respect to the state is the source structure (here the metric), whose stationarity is the field equation (here the cubic Noether/force law), and whose time-translation symmetry is the conserved energy. Physics splits these into separately named objects — position, mass, force, gravity — because it presupposes a manifold (spacetime) prior to the matter on it. The categorical program has no prior manifold; *the manifold is the second cumulant*. The four objects therefore remain four derivatives of one functional, and the relations physics must *posit* (mass sources curvature; energy–momentum is conserved; gravity is geometry) become *identities of the tower*.

This is the bridge from information geometry and simplectic mechanics to physics: not an analogy table but the statement that $\Phi$ is the categorical effective action, and that splitting it requires a pre-given manifold the program declines to assume. The promissory "the relations physics posits become identities of the tower" is discharged in tiered form in §5 (the closure defect), §7 (positivity), and §9 (signature): three of the four GR content-pillars are inherited $[P]$, the sourcing pillar (the Einstein-like equation $\delta\mathcal R_{\text{proj}}\propto T^{(4)}$) remaining $[C,\text{reduced}]$ (§5.A).

**Remark 2.2 (External scaffold: the Zhang–Li divergence–symplectic construction). [P, external precedent]**
Claim 2.1 is the categorical-simplex instance of an established construction in differential information geometry. For a divergence $D$ on a manifold $M$, Zhang and Li (2013) show the doubled space $M\times M$ carries a canonical symplectic form built from the mixed second derivatives of the divergence,
\[
\omega_D \;=\; -\,D_{i,j}\,dx^i\wedge dy^j,\qquad D_{i,j}=\frac{\partial^2 D}{\partial x^i\,\partial y^j},
\]
that the Fisher–Rao metric is exactly the restriction of the induced metric to the diagonal $\Delta_M=\{(x,x)\}$, and that a compatible almost-complex structure with $J^2=-I$ exists *iff the divergence is "proper"* (the mixed partials commute across the variable split, $D_{i,j}=D_{j,i}$). For a $\Phi$-divergence the doubled space is Kähler with global potential set by $\Phi$. The categorical program is the case $D=$ KL divergence of the categorical exponential family and $\Phi=\log Z$: the cumulant tower of $\Phi$ is exactly this Zhang–Li potential, the Fisher metric $g=\nabla^{(2)}\Phi$ is its diagonal restriction, and the binary symplectic/complex package is the $M\times M$ structure, not a primitive. Thus "the four physical objects are one functional's derivatives" is the categorical realization of a peer-reviewed divergence-induced symplectic–Kähler construction. The properness / $J^2=-I$ condition returns, with teeth, in Theorems 8.2 and 9.1.

**Remark 2.3 (The "Heisenberg call": why $\Phi$ is the right object). [P, methodological]**
Claim 2.1 commits the program to an observable-side reading of categorical mechanics. The log-partition $\Phi=\log Z$ is a function of the *natural parameter* $\theta$ (the dual/source side), and its cumulant tower is a ladder of observables (centroid, Fisher form, Amari–Chentsov tensor, higher cumulants), not of states. The state $p(\theta)$ is recovered only by the Legendre transform; one cannot recover the cumulant structure from the state alone without re-introducing $\Phi$. This matters because state-side and observable-side analyses disagree on what classicalization looks like: Dutra, Baldijão & Terra Cunha (arXiv:2604.24735, 2026) §V close their analysis of Kochen–Specker classicalization with an explicit "Heisenberg call" — the Schrödinger (state-evolving) picture captures state-dependent contextuality but *cannot* see state-independent contextuality classicalization, which requires the Heisenberg (observable-evolving) dual map. The simplicial program's choice to ground every claim in derivatives of $\Phi$ rather than trajectories of $p(t)$ is the same methodological choice, made before the problem is named. The "state-independent" residual that contextuality literature struggles to classicalize is, in our vocabulary, the cross-prime carry packet $M$ (§5.1) — invariant under any centroid-fixing state-side reduction, removable only by trajectory-level (Heisenberg-side) evolution. This remark adds no new claim; it records the program's standing Heisenberg-picture commitment and its independent identification in the quantum-foundations literature.

---

## 3. Space and Mass Are the Same Tensor

**Theorem 3.1 (Space = inertia). [P]**
On $\Delta_R^\circ$ the Fisher metric $g$ is simultaneously (i) the ruler that fixes distances and the manifold structure, and (ii) the inertia in the kinetic core $\tfrac12 g(v,v)$ of the cubic Lagrangian (Paper 17, Def. 2.1) and of $\mathcal E_3$. There is no independent mass primitive on the simplex; the object multiplying squared velocity is $g$.

*Proof.* $g=\nabla^{(2)}\Phi$ is the covariance / second cumulant; it is the metric by Fisher–Rao and the inertia by inspection of $\ell_3$ and of the Paper 28 energy $\mathcal E_3 = \tfrac12\sum m_i|v_i|^2 + \tfrac13\sum T\,h(v\cdot v)$, whose quadratic core is the Fisher term. No third object is introduced. $\blacksquare$

**Content (Paper 54, Theorem 2).** The identification "metric = inertia" above holds because the Lagrangian is *defined* with the kinetic term $\tfrac12g(v,v)$. Its content is the static fluctuation–dissipation theorem: $\nabla^2\Phi=\operatorname{Cov}(T)=\partial\langle T\rangle/\partial\theta=$ Fisher metric — the ruler, the fluctuations (watching) and the compliance (pushing) are one tensor *in the free states*. Away from equilibrium the three readings separate, by an amount linear in the stationary current, and the response is no longer the Hessian of any potential (Paper 54, Theorem 3). That is the falsifiable non-equilibrium extension of Theorem 3.1. Quantum mechanically the Hessian of $\Phi$ is the Kubo–Mori metric, which equals the response but not the symmetrized variance (Paper 54, Proposition 2.1).

**Interpretation.** "What do space and mass have in common?" is answered without metaphor: in a theory with no pre-given space, *space = mass* is the statement that the metric is the inertia, which is the statement that geometry is the second cumulant. The identity is invisible in the Newtonian setup only because there spacetime is a container handed in advance and mass is placed into it.

**Remark 3.2 (External twin: the Koszul–Souriau–Fisher capacity identity). [P, external precedent]**
Theorem 3.1 is the categorical-simplex instance of an identity already present in Souriau's Lie-group thermodynamics. There the Hessian of the Massieu function with respect to the Lie-algebra temperature, $I(\beta)=-\partial^2\Phi/\partial\beta^2$, is *simultaneously* the Fisher information metric and the system's generalized heat capacity; positive definiteness (the second law / strict convexity of $\Phi$) is what makes it a rigid Riemannian structure. "Metric = inertia = capacity = second cumulant" is therefore not unique to this program; it is the Koszul–Souriau–Fisher identity specialized to the categorical exponential family, where $\beta\leftrightarrow\theta$ and the Massieu function is $-\Phi=-\log Z$. This places our cleanest $[P]$ result on independently established symplectic-thermodynamic footing without importing the emergent-gravity ontology of §13.

---

## 4. Time, Energy, and Gravity Share One Structure

Paper 17 Theorem 2.2: time-translation invariance of the autonomous cubic action yields the conserved Noether energy
\[
\mathcal E_3=\dot\eta\cdot\frac{\partial\ell_3}{\partial\dot\eta}-\ell_3
=\tfrac12 g(\dot\eta,\dot\eta)+\tfrac13 T(h,\dot\eta,\dot\eta),
\]
with the Legendre $-\ell_3$ sign carried explicitly. The three physical objects are then three readings of one structure.

**Theorem 4.1 (Time, energy, gravity are one Noether structure and its closure failure). [P] for items 1–2 and for the localization in item 3; [C] for the gravity reading of item 3.**
On $\Delta_R^\circ$:
1. **Time** is the parameter the autonomous cubic flow is written in — not a coordinate, but the symmetry direction of $\ell_3$.
2. **Energy** is the Noether charge $\mathcal E_3$ of that time-translation symmetry.
3. **Gravity (its form)** is the *closure defect* of $\mathcal E_3$ under projection to the closure-valid macrovariable subalgebra: $\tfrac{d}{dt}\mathcal E_3|_\Pi = -\tfrac13\,T^{(4)}|_{\text{residual}}$, the obstruction to integrating the time-translation generator globally after coarse-graining.

The first two are Paper 17 verbatim; the third is the content of §5. Energy is conserved upstairs (on the full unitary/$e$-geodesic orbit $W$); its non-conservation appears only as an artifact of projecting onto a macrovariable subalgebra that is not closed under the cubic vertex. *Gravity-as-Noether-anomaly* is then literally the statement that the conserved energy fails to remain conserved under coarse-graining, with the failure typed, bounded, and arithmetically localized.

**§4.A The general-relativistic triad, made explicit.**
Four content-pillars of general relativity map onto the framework with the following tiers:
- **(i) Metric / mass–geometry identity** — the second cumulant (Theorem 3.1), i.e. the static FDT of the free states (Paper 54, Theorem 2). **[P]** as an equilibrium identity.
- **(ii) Conservation / Bianchi structure** — the Filippov/Noether identity of the cubic flow (Theorem 4.1, items 1–2). **[P].**
- **(iii) Sourcing (Einstein-like equation)** — $\delta\mathcal R_{\text{proj}}\propto T^{(4)}$: projected curvature sourced by the quartic. **[C, reduced]** (the one pillar not inherited; see Remark 4.2).
- **(iv) Action-stationarity** — $\Phi$ as effective action (Claim 2.1), i.e. the Gibbs variational principle (Paper 54, Theorem 1(c)). **[P].**

The three mathematical statements behind pillars (i), (ii), (iv) are [P]; *mapping* them onto the content-pillars of general relativity is [A]. The sourcing pillar is the single reduced conjecture, and the firewall (§12) guarantees that even if proved it carries no dimensionful Newton constant.

**Remark 4.2 (The closure defect is a projected curvature). [P, geometric]**
The "closure defect" of Theorem 4.1 has a precise geometric meaning. For a flat lifted connection $\nabla$ on the apex/ledger algebra and a projection $\Pi_S$ onto a retained packet sector, the curvature of the projected connection $\nabla^{\Pi_S}=\Pi_S\nabla$ is
\[
R^{\Pi_S}(X,Y)=\Pi_S\,d\Pi_S\wedge d\Pi_S\,\Pi_S,
\]
and for conductor-packet projections the *universal support* of the projected curvature defect $\mathcal R_S^{(n)}=(1-\Pi_S-\Pi_1)V_n|_{H_S^{\otimes n}}$ is **exactly the conductor-fusion boundary** $\partial_n S$ (sharp; Appendix A, T14). Therefore the §4/§5 "closure defect" of $\Phi$ is *literally* the projected cubic curvature defect, and its support is exactly the conductor-fusion boundary computed in §5. In the finite apex setting one finite object carries six readings — curvature $=$ projection noncommutation $=$ boundary leakage $=$ renormalization source $=$ Noether defect $=$ beta source — so "closure defect / cubic vertex / gravity-adjacent residual / RG-source" are one object in six languages. This upgrades the geometric content of §4–§5 from $[A,\text{structural}]$ to $[P,\text{proved geometric}]$; the *dimensionful* sourcing (pillar iii) stays $[C]$.

---

## 5. The Explicit Closure Certificate on $R=\mathbb{Z}/6\mathbb{Z}$

This is the technical core. We compute Paper 31's five-slot certificate for the time-translation projection on the smallest squarefree two-prime row.

### 5.1 The row decomposed

$R=\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$, $Q=6$, $\dim\Delta_6^\circ=5$. Characters $\chi_k(x)=e^{2\pi i kx/6}$, $k\in\{0,\dots,5\}$. Conductor $c(k)=6/\gcd(k,6)$:

| $k$ | $\gcd(k,6)$ | $c(k)$ | packet |
|---|---|---|---|
| 0 | 6 | 1 | gauge (killed by $\sum u_a=0$) |
| 3 | 3 | 2 | $A_2$: the $p{=}2$ axis, 1 real dim |
| 2,4 | 2 | 3 | $A_3$: the $p{=}3$ axis, 2 real dims |
| 1,5 | 1 | 6 | $M$: the squarefree $2\cdot3$ carry packet, 2 real dims |

So $H_6=A_2\oplus A_3\oplus M$, dimensions $1+2+2=5$. $A_2,A_3$ are the single-prime axes; $M$ is the cross/carry packet. $M$ is exactly the $\operatorname{Ext}_{CH}$ support (Paper 13 §11) and the primorial $P_2=2\cdot3$ support that Paper 17 §5's Constraint-3 audit stress-tests.

### 5.2 The selection rule, made exact

**Setup and conventions.** Let $\omega=e^{2\pi i/6}$. The characters are $\chi_k(a)=\omega^{ka}$, $k,a\in\{0,\dots,5\}$, and $e_k\in\mathbb{C}^6$ denotes the vector with components $(e_k)_a=\omega^{ka}$. Pointwise (Hadamard) product satisfies the grading $(e_k\odot e_l)_a=\omega^{(k+l)a}=(e_{k+l\bmod 6})_a$. The tangent space $H_6=\{u:\sum_a u_a=0\}$ is exactly $\chi_0^{\perp}$; hence for every dynamical vector $u\in H_6$ the zeroth Fourier component vanishes, $\widehat u_0=0$. From Paper 13 §7 the Amari–Chentsov cubic at the centroid $p_*=(1/6,\dots,1/6)$ is $T_{p_*}(u,v,w)=\sum_a u_av_aw_a/p_a^2 = 36\sum_{a=0}^{5}u_av_aw_a$.

**Lemma 5.1a (Exact cubic structure constant). [P]**
In the character basis,
\[
T_{klm}\;:=\;T_{p_*}(e_k,e_l,e_m)\;=\;36\sum_{a=0}^{5}\omega^{(k+l+m)a}\;=\;216\,\cdot\,\mathbb{1}\!\left[\,k+l+m\equiv 0 \pmod 6\,\right].
\]
*Proof.* The inner geometric sum is $\sum_{a=0}^{5}\zeta^{a}$ with $\zeta=\omega^{k+l+m}$, a sixth root of unity. If $k+l+m\equiv0$ then $\zeta=1$ and the sum is $6$; otherwise $\zeta\neq1$, $\zeta^{6}=1$, and $\sum_{a=0}^{5}\zeta^{a}=(\zeta^{6}-1)/(\zeta-1)=0$. Multiplying by $36$ gives $216$ or $0$. This is precisely the convolution theorem on $\widehat{\mathbb{Z}/6\mathbb{Z}}$: $T$ is the totally symmetric structure constant of the group-algebra convolution, nonzero exactly on the additively closed support. $\blacksquare$
\[
\boxed{\;T_{klm}\neq 0 \iff k+l+m\equiv 0 \pmod 6\;}
\]

**Lemma 5.1b (Reality reduction: the real-packet partition is inherited). [P]**
Conjugation $k\mapsto -k\equiv 6-k$ acts as $1\leftrightarrow5$, $2\leftrightarrow4$, $3\leftrightarrow3$, $0\leftrightarrow0$. Each conductor packet is therefore conjugation-closed: $M=\{1,5\}$, $A_3=\{2,4\}$, $A_2=\{3\}$ (with $\chi_3=(-1)^a$ real and self-conjugate). For real $u,v,w\in H_6$ the Hermitian symmetry $\widehat u_{-k}=\overline{\widehat u_k}$ holds; expanding $T(u,v,w)=\sum_{k,l,m}\widehat u_k\widehat v_l\widehat w_m\,T_{klm}$ and using that $T_{klm}$ depends only on $k+l+m\bmod 6$, every real 2-plane spanned by a conjugate pair stays inside its packet under the contraction. Hence *which real packets couple* is exactly the complex statement of Lemma 5.1a; the partition is basis-independent, not an artifact of complex diagonalization. $\blacksquare$

**Lemma 5.1c (Off-centroid stability of the support). [P]**
Off the centroid, Paper 13 §7 gives the line-coefficient expansion $\bar g^F_{p(t)}(e_\chi,e_\psi)=\sum_{n\ge0}(-t)^n\,\widehat h^{*n}(\psi\chi^{-1})$, i.e. higher orders enter through convolution powers $\widehat h^{*n}$. Convolution on $\widehat{\mathbb{Z}/6\mathbb{Z}}$ *adds* frequencies, so it maps the additively graded algebra into itself and cannot create a triple violating $k+l+m\equiv0$. Therefore the **support** of the cubic coupling is fixed to all orders in the centroid expansion by the group grading; only the *magnitudes* flow off-centroid. The selection rule is a Pontryagin-duality identity, not a centroid coincidence. (This robustness partially discharges gap G1: only coefficient sizes require the §14.1 audit.) $\blacksquare$

**Lemma 5.1 (Packet partition of the cubic interaction — full enumeration). [P]**
Over the dynamical indices $\{1,2,3,4,5\}$ (index $0$ excluded by $\widehat u_0=0$), the sum $k+l+m$ ranges in $[3,15]$; the only multiples of $6$ attainable are $6$ and $12$. The complete list of closing unordered multisets, with packet signature ($M=\{1,5\}$, $A_3=\{2,4\}$, $A_2=\{3\}$):

| multiset $\{k,l,m\}$ | sum | $T_{klm}$ | packet signature | classification |
|---|---|---|---|---|
| $\{2,2,2\}$ | 6 | 216 | $A_3,A_3,A_3$ | **closed in $A_3$** (pure $p{=}3$) |
| $\{4,4,4\}$ | 12 | 216 | $A_3,A_3,A_3$ | **closed in $A_3$** (conj. of $\{2,2,2\}$) |
| $\{1,1,4\}$ | 6 | 216 | $M,M,A_3$ | forced through $M$ |
| $\{2,5,5\}$ | 12 | 216 | $A_3,M,M$ | forced through $M$ (conj. of $\{1,1,4\}$) |
| $\{1,2,3\}$ | 6 | 216 | $M,A_3,A_2$ | forced through $M$ (full cross-prime) |
| $\{3,4,5\}$ | 12 | 216 | $A_2,A_3,M$ | forced through $M$ (conj. of $\{1,2,3\}$) |

The selection rule has bite *inside* a packet too: within $A_3=\{2,4\}$ the triples $\{2,2,4\}\,(8\equiv2)$ and $\{2,4,4\}\,(10\equiv4)$ do **not** close, so only $\{2,2,2\}$ and $\{4,4,4\}$ survive even there. Within $A_2=\{3\}$ the only candidate is $\{3,3,3\}\,(9\equiv3\not\equiv0)$; the formal closure $\{3,3,0\}$ routes through the gauge mode and is killed by $\widehat u_0=0$.

*Proof.* Exhaustive: enumerate $k\le l\le m$ in $\{1,\dots,5\}$ with $k+l+m\in\{6,12\}$. Sum $6$: $k=1\Rightarrow(l,m)\in\{(1,4),(2,3)\}$; $k=2\Rightarrow(2,2)$; $k\ge3$ impossible. Sum $12$: $k=2\Rightarrow(5,5)$; $k=3\Rightarrow(4,5)$; $k=4\Rightarrow(4,4)$; $k\in\{1,5\}$ impossible by range. Six rows; packet signatures from the membership map; values from Lemma 5.1a. $\blacksquare$

**Corollary 5.1d (Three exact consequences). [P]**
From the enumeration, with no remaining freedom:
1. **$A_3$ self-closure is exactly two triples:** $\{2,2,2\},\{4,4,4\}$. The $p{=}3$ axis carries a closed, nonempty cubic self-interaction.
2. **$A_2$ is cubically isolated.** No closing triple has all legs in $A_2\cup\{0\}$: $\{3,3,3\}\not\equiv0$ and $\{3,3,0\}$ is gauge-killed. Moreover *every* closing triple containing index $3$ — namely $\{1,2,3\}$ and $\{3,4,5\}$ — necessarily carries an $M$-leg ($1$ or $5$). The $p{=}2$ axis cannot participate in any cubic coupling except through $M$. (Cross-prime forcing: $3{+}2\equiv-1\Rightarrow$ third leg $\equiv1\in M$; $3{+}4\equiv1\Rightarrow$ third leg $\equiv5\in M$.)
3. **$\Pi_\tau$ survival set is exactly $\{\{2,2,2\},\{4,4,4\}\}$.** A term survives $\Pi_\tau$ (which annihilates all $M$-components) iff no leg lies in $M$; of the six rows only the two pure-$A_3$ rows qualify. Every other closing triple has an $M$-leg, so the discarded part $T_{\mathrm{cross}}$ vanishes whenever the $M$-components vanish — the residual is *supported on $M$* (conductor 6), not merely correlated with it. $\blacksquare$

Thus the cubic interaction splits exactly and provably as
\[
\underbrace{\{2,2,2\},\{4,4,4\}}_{\text{closed in }A_3,\ \Pi_\tau\text{-surviving}}
\;\oplus\;
\underbrace{\varnothing}_{A_2\text{ cubically isolated}}
\;\oplus\;
\underbrace{\{1,1,4\},\{2,5,5\},\{1,2,3\},\{3,4,5\}}_{\text{all carry an }M\text{-leg};\ \Pi_\tau\text{-annihilated; residual on conductor 6}}.
\]

### 5.3 The projection and the localized defect

Define the time-translation projection onto the closure-valid macrovariable subalgebra (the within-single-prime-packet phase actions, i.e. the Paper 17 Cartan directions):
\[
\Pi_\tau:\ H_6\longrightarrow A_2\oplus A_3,\qquad \Pi_\tau\big|_M=0.
\]
$\Pi_\tau$ retains the two abelian $\mathfrak u(1)$ generators (phase on $A_2$, phase on $A_3$) — the exactly two cubic charges Paper 17 says exhaust the classical dictionary — and discards $M$. The whole $W$ is the $e$-geodesic / unitary orbit upstairs; $\Pi_\tau$ is its diagonal classical shadow in Paper 20's sense.

Write $\eta=\eta_A+\eta_M$. At the centroid $g_{p_*}=Q\,I_H$, packets orthogonal, so the kinetic term splits and survives $\Pi_\tau$ as $\tfrac12 g(\dot\eta_A,\dot\eta_A)$ with no defect. By Lemma 5.1 the cubic term decomposes as
\[
T(h,\dot\eta,\dot\eta)=\underbrace{T_{A_3}}_{\text{within }A_3,\ \text{closes}}+\underbrace{0}_{A_2\text{ inert}}+\underbrace{T_{\mathrm{cross}}}_{\text{every term has an }M\text{-leg}}.
\]
$\Pi_\tau$ annihilates $T_{\mathrm{cross}}$. Therefore:

**Theorem 5.2 (Localized time-translation defect). [P]**
\[
\frac{d}{dt}\,\mathcal E_3\Big|_{\Pi_\tau}= 0 \;-\; \frac{d}{dt}\Big[\tfrac13 T_{\mathrm{cross}}(h,\dot\eta,\dot\eta)\Big]= -\tfrac13\,\nabla^{(e)}T\big|_M\;\equiv\; -\tfrac13\,T^{(4)}\big|_M .
\]
The non-conservation of the projected Noether energy is exactly the jerk, supported entirely on the conductor-6 packet $M$. It is Paper 30's $R^{(4)}$, Paper 20's simplex-mass term, and $\operatorname{Ext}_{CH}$, and Lemma 5.1 names the exact Fourier modes it occupies. $\blacksquare$

### 5.4 The certificate tuple $\mathcal C_W(\Pi_\tau;T_\tau,H,K{=}3)$

Per Paper 31 Definition 5.1:

- **$\mathsf P^{\Pi_\tau}_W$ (retained participation). [P]** The single-prime packets $A_2,A_3$ and their phase actions; equivalently the abelian Cartan $\mathfrak u(1)^2$ of Paper 17 Corollary 2.4. Kinetic core and within-$A_3$ cubic charge survive intact — the "two-body weak-field-like" sector: single-prime, self-closing, no carry.
- **$\mathsf R^{\Pi_\tau}_W$ (typed residual). [P]** Exactly $\tfrac13 T_{\mathrm{cross}}$ and its derivative $-\tfrac13 T^{(4)}|_M$, supported on $M=\{\chi_1,\chi_5\}$, conductor 6. Typed: *cross-prime cubic carry / first overflow pointer $R^{(4)}$* $=\operatorname{Ext}_{CH}$.
- **$\mathsf B^{\Pi_\tau}_W$ (bound). [P/A]** $\|R^{\Pi_\tau}\|\le \tfrac13\|T|_M\|\,\|h_M\|\,\|\dot\eta\|^2\le C_6\|h\|\,\|\dot\eta\|^2$, $C_6$ the operator norm of the convolution restricted to $M$ (finite; $\dim M=2$). Finiteness is the Marcinkiewicz bounded-support fact (Papers 21, 22): the cumulant tower on a finite squarefree row has bounded support, so the carry cannot run away. Persistence under prime-power depth is **[A]** (§14.1).
- **$\mathsf S^{\Pi_\tau}_W$ (stability). [P/A]** Recurrent, non-chaotic, Fisher-volume-preserving; $M$ is a fixed 2-dimensional packet the flow cannot pump unboundedly (Paper 19). **Non-tachyonic**: the residual energy is $\ge0$, and this is *the same positivity* as Paper 22's Weil/Noether form on the $P_2=2\cdot3$ row at cubic order (Theorem 7.1). Sign-definiteness under depth is **[A]** (§14.1).
- **$\mathsf F^{\Pi_\tau}_W$ (falsifiers). [P]** (i) *Localization*: any measured time-translation residual in $A_2$ or $A_3$ refutes the derivation — forbidden by Lemma 5.1. (ii) *Depth*: under $\mathbb{Z}/6\hookrightarrow\mathbb{Z}/12,\mathbb{Z}/18$ the residual must stay on the squarefree conductor-6 mode; a new depth-induced carry axis refutes time-translation closure. (iii) *Boundedness/stability*: unbounded $\|R^{\Pi_\tau}\|$, a negative conductor-6 Noether form, or chaotic long-time behavior on $M$ refutes the certificate and simultaneously breaks Paper 22's positivity route.

**Verdict.**
\[
\Pi_\tau\in\operatorname{ClValid}(W,T_\tau,H,K{=}3)\iff \text{dynamics confined to }A_2\oplus A_3.
\]
The closure-valid locus is *exactly* the abelian Cartan $\mathfrak u(1)^2$ — re-deriving Paper 17 from projection closure. The typed bounded residual is *exactly* the conductor-6 carry: the gravity/dark-matter-adjacent term, now arithmetically localized and computable. Crucially the closure-failure locus does **not** coincide with the integrability locus $\{\nabla^{(e)}T=0\}$ (Paper 17 Theorem 3.1) — it coincides with the conductor-6 *packet*. **The gravity-adjacent term is selected by arithmetic (which primes mix), not by dynamics (where the orbit sits).** That is the new statement.

---

## 6. The Four-Thread Arithmetic Root

The exhaustive enumeration of §5 has a single congruence as its load-bearing input. Isolating it makes the dependency graph of four otherwise-independent corpus results visible at once.

**Lemma 6.1 (The four-thread arithmetic root). [P]**
The congruence $3+3+3=9\equiv 3\not\equiv 0\pmod 6$, combined with the selection rule $T_{k\ell m}\neq 0\iff k+\ell+m\equiv 0\pmod 6$ (Lemma 5.1a), yields two structural facts:

- **(L1) Pure-$A_2$ cubic vacuity.** Since $A_2=\{3\}$, the only candidate pure-$A_2$ closing multiset is $\{3,3,3\}$. By the congruence it fails to close, so $T_{p_*}(u,v,w)=0$ for every $u,v,w\in A_2$.
- **(L2) Forced $M$-mediation of every $A_2$-leg coupling.** A closing triple containing leg $k=3$ requires $\ell+m\equiv 3\pmod 6$ with $\ell,m\in\{1,\dots,5\}$. The exhaustive solutions are $\{3,1,2\}$ and $\{3,4,5\}$ (the case $\{3,3,0\}$ is gauge-killed). Each carries an $M$-leg ($1$ or $5$).

*Proof.* (L1) is the congruence. (L2) is the exhaustive enumeration already tabulated in Lemma 5.1. $\square$

**Corollary 6.2 (Four threads, one root). [P]**
Each of the following four corpus results — from independent reaches of the program — is a direct consequence of (L1) and (L2):

**(T1) The simplex-mass-ratio audit closes negative on $\mathbb{Z}/6$ (Paper 20 OQ1).** By Paper 20 Def. 2.1, $m^2_{\text{simplex}}(\mathbf C)$ is the leading $T^{(4)}$ coefficient in the conductor-total sector $\mathbf C$. By (L1) the cubic self-energy of $A_2$ vanishes identically, so $m^2_{\text{simplex}}(A_2)=0$ exactly. Every ordered ratio $\mathcal Y(A_2,\mathbf C')$ is $0$; every $\mathcal Y(\mathbf C',A_2)$ is $\infty$ — the *degenerate stated branch*, not a non-trivial conductor-fixed pure number. The packet $M=\{1,5\}$ is similarly cubically inert in pure-$M$ self-coupling ($\{1,1,1\},\{5,5,5\}$ both sum $\equiv 3\not\equiv 0$). The $\mathbb{Z}/6$ row furnishes no non-trivial simplex-mass ratio.

**(T2) The single external chirality bit is color-protected (Paper 16 §3; Paper 33 §3).** A direct $A_2\!\cdot\!A_3\!\cdot\!A_3$ or $A_2\!\cdot\!A_2\!\cdot\!A_3$ trilinear vertex would supply an internal cross-prime channel between the parity-character sector and the cube-root sector. By (L2) every $A_2$-leg closing triple is $\{3,1,2\}$ or $\{3,4,5\}$ and carries an $M$-leg; no direct $A_2$–$A_3$ vertex exists. The cross-prime channel is forced through $M$. The KO-real-structure $\mathbb{Z}_2$ of finite-Standard-Model spectral triples therefore cannot be produced internally by any real-cone-preserving Bures lift; it remains the single external bit of the Paper 33 Chirality Boundary, count $2^{c-1}=1$ at $c=2$.

**(T3) Friston's gradient-vs-least-action fork resolves sector-wise on $\mathbb{Z}/6$. [P, structural; audit FEP-3, 2026-05-20].** Friston's monograph poses, as an open fork of deep active inference, whether the belief flow is a gradient descent on free energy or a least-action / Lagrangian process. On the canonical discrete-state instance the four conditions trace immediately: (a) Cor. 5.1d.1 ($A_3$ self-closes on $\{2,2,2\},\{4,4,4\}$ — the conserved sector is non-trivially closed); (b) (L1) (no pure-$A_2$ classical conserved cubic charge); (c) (L2) (the cross-couplings forced through $M$); (d) the resulting $2+18$ partition. The least-action description survives on the Cartan/single-prime sector; the complement is forced to be the gradient-like leakage channel; the boundary is the positive-cone condition of Paper 14 Cor. 2.4. **Audit FEP-3** verified the metriplectic decomposition at machine precision on $D(\mathbb{C}^6)$: $F=F_V+F_M$ with $F_V=I_{\text{real}}$ Hamiltonian (V-supported, reversible) and $F_M=\alpha^2(m^2_{\text{simplex}})^2$ gradient-of-entropy (M-supported, monotone-increasing, irreversible); cross-coupling zero at every order; no interaction term. The arrow of time on the conductor lattice is the direction of $\nabla F_M$. Structural $[P]$ on $\mathbb{Z}/6$; empirical biological applicability remains $[C,\text{reduced}]$.

**(T4) The conductor-misspecification certificate for second-order preconditioning (Paper 12).** Of the 20 ordered closing triples on $\{1,\dots,5\}$, exactly 2 are pure-packet ($\{2,2,2\},\{4,4,4\}$) and 18 are cross-packet, of which 12 are $(A_2,A_3,M)$ by (L2) and 6 are $(A_3,M,M)$. The quadratic Fisher form $g_{p_*}$ is packet-block-diagonal by character orthogonality and carries $0$ of the 18 cross-packet entries; the cubic $T_{p_*}$ carries all 18. Therefore any preconditioner built from $g$ alone — natural gradient, K-FAC, Gauss–Newton, Adam's diagonal empirical Fisher, the NTK Gram — is provably blind to a coupling the next cumulant floor carries. The structural ratio "cross-packet content missed by any second-order preconditioner on a ring-structured categorical head" is $18/20=9/10$ on this row, with the $A_2$-involving moiety $12/18=2/3$ forced by (L2). Misspecification-only; no claim about any trained model. $\square$

**Remark 6.3 (Scope and the primorial sequel).** The four threads come from independent reaches of the corpus — a constants audit (Paper 20), a spectral-triple chirality result (Paper 16), an outbound contribution to active inference (Friston), and a deep-learning misspecification statement (Paper 12). Corollary 6.2 reduces them to a single congruence on $\mathbb{Z}/6$, raising the standing of the coincidence from "four parallel results" to *jointly arithmetic*: one finite fact, four consequences. On the next squarefree primorial $\mathbb{Z}/30=2\cdot3\cdot5$ the analogous $p=2$ self-vacuity is $15+15+15=45\equiv 15\not\equiv 0\pmod{30}$, again non-closing; whether the four threads co-decide at quartic order is the open primorial-ladder question, recorded as the natural sequel and the falsifier of generalization, not as a result.

---

## 7. The Positivity Identification

**Theorem 7.1 (Mass non-tachyonicity = Weil positivity at cubic order). [P]**
Paper 20 requires the simplex mass term to be non-tachyonic ("the jerk is a mass, not a ghost"). On the $\mathbb{Z}/6$ row the conductor-6 residual energy carried by $M$ is the cubic-order value of the primorial Noether–Weil form of Paper 22 at the $P_2=2\cdot3$ row. The non-negativity of that form at cubic order — proved in Paper 22 §8 for the $P_2$ row — is therefore *the same inequality* as the non-tachyonicity of the simplex mass term here. The two positivity statements are not analogous; they are one finite positivity, read once in the language of a mass term (Paper 20) and once in the language of the Weil explicit-formula functional (Paper 22). $\blacksquare$

**Remark 7.2 (What this buys and what it does not).** This identification is the stability slot $\mathsf S$ of the certificate (§5.4) made arithmetic: the residual cannot be a tachyon precisely because the same object is the positive cubic Weil form. It does *not* import the all-order Riemann-Hypothesis content of Paper 22 — only the $P_2$ cubic-order instance is $[P]$ here (gap G5). The all-order limit inherits every open analytic input of Paper 22 §8; the present claim is exactly the cubic, single-row positivity and no more.

---

## 8. Dimensional Selection: Why an Inertial Projector Closes in 3

**Definition 8.1 (Inertial projector).**
An inertial projector is a projection $\Pi$ whose closure-valid self-model has: a single conserved energy from a single Hamiltonian; a single rotation axis (angular momentum representable as a vector); and a complex structure $J^2=-I$ organizing transverse rotation. This is precisely the binary symplectic package. A *mass-structured being* is, by Theorem 3.1, an inertial projector: having a nondegenerate second cumulant is having inertia.

**Theorem 8.2 (Dimensional selection, route 1: Hodge / $\mathfrak{so}$). [P]**
The binary symplectic package is native to exactly one row of the Fisher-volume hierarchy. Three structural facts coincide only at $n=3$: $\dim\mathfrak{so}(n)=n(n-1)/2=n$; $\Lambda^2(\mathbb R^n)\cong\mathbb R^n$; and $K(u)$ restricts to $J^2=-I$ on $u^\perp$ (Paper 13 §2). Paper 13's worked rows give the cost elsewhere: $Q=3$ (dim 2) is degenerate area mechanics; $Q\ge5$ (dim $\ge4$) has native momentum form of degree $Q-2\ge3$, no single 2-form, $Q-2\ge3$ simultaneous independent macro-Hamiltonians, no single rotation axis. An inertial projector — one energy, one Hamiltonian, one spin axis — can therefore have a closure-valid self-model only at $Q=4$, spatial dimension 3. $\blacksquare$

*Scope of route 1.* The load-bearing fact is $\dim\mathfrak{so}(n)=n\iff n=3$, i.e. "angular momentum is a vector iff $n=3$". Definition 8.1 builds this in ("a single rotation axis, angular momentum representable as a vector"), so Theorem 8.2 is a correct restatement of that definition on the Fisher-volume hierarchy, not an independent selection mechanism.

**Remark 8.2a (External anchor for the $J^2=-I$ singularity). [P, external precedent]**
The $J^2=-I$ clause of Theorem 8.2 is not only the Paper 13 §2 cross-product observation; it coincides with the Zhang–Li compatibility condition of Remark 2.2: a divergence-induced almost-complex structure with $J^2=-I$ exists *only* when the divergence is proper, and on the categorical doubled space the row at which the diagonal restriction carries a single such $J$ acting as a genuine quarter-turn is exactly the dim-3 row. Dimensional selection is therefore the categorical instance of an established divergence-geometry compatibility constraint, not a coincidence of small-$n$ linear algebra alone. This is the second of the two places Remark 2.2 said the properness condition would return with teeth.

**Theorem 8.3 (The conductor count on the $\mathbb Z/6$ row). [P] for the count; [C] for the reading.**
On the cubic two-prime row (§5), the closure-valid block is $A_2\oplus A_3$, real dimension $1+2=3$; the complementary carry packet $M$ has real dimension $2$. $\blacksquare$

*This is not a second, independent route to Theorem 8.2.* It lives on the $Q=6$ row, not on the $Q=4$ row of Theorem 8.2, and the number $3$ is specific to $\mathbb Z/6$: on $\mathbb Z/30$ the single-prime closure-valid block has real dimension $1+2+4=7$. Reading the carry packet as "not perceived as space" and as the gravity term is [C].

**Corollary 8.4 (Why 3D, a reading). [C]**
Experiencing space as three-dimensional is the closure certificate of being an inertial projector — equivalently of having mass. The two questions of this session ("why 3D?" and "what is the gravity residual?") have one answer: the $3{+}2$ split of the conductor block is simultaneously the spatial/residual split.

**Scope.** This is a closure-selection statement: it explains why an inertial projector closes in dimension 3 and nowhere else in the hierarchy. It does not derive inertia from nothing (Theorem 3.1 makes "why inertia" near-tautological: any nondegenerate Fisher metric *is* inertia), and it does not by itself fix the Lorentzian signature — that is §9.

---

## 9. Signature Is a Lift Phenomenon

### 9.1 The classical signature is $(3,1)$ but Galilean

There is no fourth velocity component: $v=v_{A_2}\oplus v_{A_3}$, three dimensions; time is the parameter the flow is written in, not a coordinate. So $\mathcal E_3$ is a positive-definite form in three spatial velocities (Fisher positivity); the real-simplex face-value gives Euclidean-3 plus an external clock, matching Paper 20 §4. The signature lives not in $\mathcal E_3$ but in the **Poincaré–Cartan one-form** the Noether construction itself produces:
\[
\Theta=\frac{\partial\ell_3}{\partial v}\cdot d\eta-\mathcal E_3\,dt
=\underbrace{g(v,\cdot)\,d\eta}_{(+,+,+)\ \text{Fisher on }A_2\oplus A_3}\;\underbrace{-\;\mathcal E_3\,dt}_{(-)\ \text{the }-\ell_3\text{ Legendre sign}}.
\]

**Theorem 9.1 (The contact sign of the Poincaré–Cartan form). [P] for the sign; [A] for the $(3,1)$ reading.**
$d\Theta$ induces, on the extended tangent space (three Fisher spatial directions ⊕ the flow–time direction), the signature $\boxed{(\,+,\,+,\,+\,;\,-\,)}$. The three plus signs are Fisher positivity on the closure-valid block (Theorem 8.3); the minus is the literal $-\ell_3 / -\mathcal E\,dt$ in the *definition* of the Noether energy (Paper 17 Def. 2.1). The temporal minus is not a negative metric direction; it is the contact/Legendre sign of energy being conjugate to the flow parameter. Space's "3" and time's "1" do not share a metric block — the 3 is Fisher-definite, the 1 is Legendre-dual; the relative sign between them is contact-geometric, not Riemannian. $\blacksquare$

*Scope.* The $-H\,dt$ term is the contact sign of extended phase space; it is present in every dimension and for every Hamiltonian system, so it does not select $(3,1)$. The "3" comes from §8, and the pairing of the two into a signature is a reading [A], not a theorem.

**Remark 9.1a (The $3{+}1$ dimension is inherited from the $\mathbb H$ terminator — Hermitian-space indexing).** The spatial dimension $3$ and the time dimension $1$ are not two independent choices. The space of $2\times 2$ Hermitian matrices on the $\mathbb C^2$ leg of the CRT factorization (Paper 18 §5) has *real* dimension $4=\dim_{\mathbb R}\mathbb H$ by the Hurwitz / Cayley–Dickson terminator (Paper 18 Thm 6.2: the norm-closed real ladder $\mathbb R,\mathbb C,\mathbb H,\mathbb O$ stops, no fifth rung). The canonical $1\,(\text{trace})+3\,(\text{traceless})$ decomposition of a $2\times 2$ Hermitian matrix is the $1$ real $+\,3$ imaginary axes of the quaternion. The $3{+}1$ split of $\Theta$ is therefore the same $3{+}1$ the program already owns at [Certain] tier — inherited from a finished theorem, not newly assumed.

**Two division-algebra indexings — do not conflate.** The "$\mathbb H$ terminator" label here is the *Hermitian-space* indexing: spacetime is $\mathrm{Herm}_2(\mathbb C)$, whose real dimension $4=\dim_{\mathbb R}\mathbb H$ fixes the $1{+}3$ split. This is a *different* indexing from the *spinor* ladder of the supersymmetric magic dimensions (Kugo–Townsend 1983; Sudbery 1984; Baez–Huerta, arXiv:0909.0551), $D=\dim_{\mathbb R}\mathbb K+2$ for $\mathbb K\in\{\mathbb R,\mathbb C,\mathbb H,\mathbb O\}\Rightarrow D\in\{3,4,6,10\}$, in which $D{=}4$ is the $\mathbb C$ rung (Weyl spinors $\mathbb C^2$, $\mathrm{SL}(2,\mathbb C)\cong\mathrm{Spin}(3,1)$) and $D{=}10$ the $\mathbb O$ rung. The two attach *different* algebras to $3{+}1$ because they index different objects — the $4$-dimensional Hermitian spacetime versus the $2$-dimensional spinor module — so $\dim_{\mathbb R}\mathrm{Herm}_2(\mathbb C)=4=\dim_{\mathbb R}\mathbb H$ is a numerical coincidence, not an identification of rungs. Any reading that overlays the supersymmetric ladder (e.g. an order-readout bridge to the string critical dimension) must use the *spinor* convention, under which $3{+}1$ is the $\mathbb C$ rung and the superstring's $D{=}10$ the $\mathbb O$ rung; there the gap $\dim_{\mathbb R}\mathbb O-\dim_{\mathbb R}\mathbb C=6$ is a consistency identity only (the $+2$ offset cancels in any rung difference) and carries no predictive weight.

**Remark 9.1b (The Riemannian pre-lift geometry is constant-curvature, not Einsteinian).** The Fisher metric on $\Delta_R^\circ$, pulled back through the Hellinger embedding (Paper 13 Def. 14.6A), is a sector of a round sphere of constant positive curvature; it is a *fixed* geometry with no back-reaction of the matter content on $g$. Theorem 9.1 gives the *signature* of $d\Theta$ on this fixed background, not a dynamical metric. The promotion to a *sourced* curvature is the Einstein-like equation of §9.7, strictly separated from the signature statement here.

**Lemma 9.2 (But Galilean, not Lorentzian). [P]**
With $\pi=\partial_v\ell_3=g(v)+T(h,v)$, to leading order $\mathcal E_3=\tfrac12\langle\pi,g^{-1}\pi\rangle+\tfrac13 T(h,g^{-1}\pi,g^{-1}\pi)$: energy linear, momentum quadratic. That is a paraboloid — the Galilean/Newtonian dispersion (absolute time). No classical Lorentz structure, fully consistent with the series. $\blacksquare$

### 9.2 The Lorentzian sharpening

**Theorem 9.3 (Hyperboloid requires quadratic energy). [P]**
A genuine two-sheeted hyperboloid $\mathcal E^2-|\pi|^2=m^2$, boost invariance, and a light cone require $\mathcal E$ to enter the invariant *quadratically*, not linearly. $\blacksquare$

**Conjecture 9.4 (Signature is the Bures lift). [C]**
The unique place in the program where the energy invariant becomes quadratic is the Bures density-matrix lift (Paper 18), where energy is $\operatorname{tr}(H\rho)$ and the second-order structure is the Bures metric. We conjecture that on the lifted conductor-2 ⊕ conductor-3 block the level set $\operatorname{tr}(H\rho)=E$ is a genuine two-sheeted hyperboloid invariant under a 3-parameter group completing the Cartan, so that Lorentzian $3+1$, the nonabelian gauge restoration of Paper 18, and the imaginary leakage energy of Paper 20 are *one and the same lift*. Reduced to the single verification of §14.2. Falsifier: if the lifted level set is an ellipsoid (stays Euclidean) or the invariance group is wrong-dimensional, the framework is intrinsically Euclidean-4 — itself a stated, major structural result.

**Remark 9.5 (External precedent for the lift, not a proof). [C-support]**
That a *bona fide* time generator should appear only on a non-commuting lifted algebra, not classically, is a recognized structure: Tomita–Takesaki modular theory and the Connes–Rovelli thermal-time hypothesis give, for a faithful normal state on a von Neumann algebra, a canonical one-parameter modular flow generated by $-\log\rho$ — present precisely because the algebra is non-commuting and absent on a commuting (classical) restriction. This is invoked not as evidence that Conjecture 9.4 is true but to show that "the genuine temporal/Lorentzian structure lives at the Bures non-commuting lift, while the classical real-simplex level is Galilean" is a respected structural pattern, not an ad hoc rescue. The verdict remains the §14.2 audit.

### 9.3 The invariant speed as a face of the lift

**Corollary 9.6 (The invariant speed is a lift phenomenon; $c\equiv1$ is structural, not a unit choice).**

*Part 1 — $c\equiv1$ is forced, [P-adjacent given §3, §4, §9.1].* The spatial block of $\Theta$ is the Fisher metric (space = inertia, Theorem 3.1) and the temporal block is the Legendre $-\mathcal E_3\,dt$ of the *same* potential's time-translation sector (Theorem 4.1, §9.1). Two covariant derivatives of one functional $\Phi$ admit no independent relative normalization: there is no separate ruler and no separate clock between which a conversion factor could be free. Hence the spatial–temporal conversion constant is structurally unity. In this framework $c=1$ is not a convention but a consequence of the one-functional structure — the statement that the two faces of $\Phi$ share a normalization.

*Part 2 — a finite invariant speed exists only at the lift, [C], reduced to §14.2.* By Lemma 9.2 the classical dispersion is parabolic: a parabola has no asymptote, so the Galilean regime has *no* finite causal speed limit at all. By Theorem 9.3 a hyperbolic mass-shell requires energy to enter quadratically, which occurs only at the Bures lift (Conjecture 9.4). A hyperboloid *has* asymptotes; its asymptotic slope *is* the invariant speed. Therefore the finite invariant speed is created — not merely revealed — by the lift, as the asymptote of the energy–momentum hyperboloid, and its internal value is 1 because the lift introduces no new scale. "$c$ is the time-translation limit of mass" is then literally exact.

*Part 3 — the $i$-face is the sibling of the signature face, [A] reduced.* The SLD/Bures metric of Paper 18 §4 is the unique monotone metric whose conservative Nambu–Bures flow is unitary von Neumann evolution $\dot\rho=-i[H,\rho]$; the Mandelstam–Tamm/Bures quantum speed limit specializes to that flow as *Bures distinguishability rate $=$ energy spread $/\,\hbar$*. The constant $\hbar$ is therefore the conversion between the program's statistical-distinguishability clock and the unitary phase clock — the $i$-face's slope exactly as $c$ is the signature face's asymptote slope. The single lift carries **two paired conversion invariants, one per face**: $c$ (space ↔ time) and $\hbar$ (Fisher clock ↔ phase clock), each derived to exist, derived to be invariant, structurally pinned — while neither's dimensionful value is predicted (§12 firewall). The Compton wavelength $\bar\lambda_C=\hbar/(mc)$ is the named firewall *trap* of the pair.

### 9.4 The minimal independent face count

Counting what the §14 audits leave of "one lift, several faces" gives a sharp bookkeeping: the single Bures lift on the $\mathbb C^2\otimes\mathbb C^3$ row of $\mathbb Z/6$ produces **four forced internal faces, one genuine inter-leg trace mode, and exactly one irreducibly-external bit** — not loose parallel emergences.

| # | Face / datum | Carries | Status |
|---|---|---|---|
| **Face A** | the $\mathbb C^2$-leg algebraic real-form face | weak-$\mathrm{SU}(2)$ as its **compact** real form (Paper 18 Thm 6.1, [P]); the Lorentz $\mathrm{SL}(2,\mathbb C)\cong\mathrm{Spin}(3,1)$ as its **non-compact** real form (algebraic + §14.2A local-tangent Casimir-Hessian level only; manifold-level refuted by §14.2); the $3{+}1$ split (Paper 18 Thm 6.2, the $\mathbb H$ terminator; Hermitian-space indexing, cf. Remark 9.1a); the invariant $c$ (local-Casimir hyperboloid asymptote) | [A] / S′ — two-layer reading |
| **Face B** | the $\mathbb C^3$-leg color face | $\mathrm{SU}(3)$ color; confinement-shaped signature = conductor-3 cubic isolation (Cor. 5.1d) | [P, inherited] |
| **Face C** | the $i$-face (complex-energy / leakage) | the imaginary $i$, $K(u)^2=-I$; the invariant $\hbar$-role constant (§9.3 Part 3); the Paper 20 leakage width | [A, reduced] / T′ |
| **Face D** | the prime-reciprocal hypercharge $\mathfrak u(1)_Y$ | $Y=\tfrac12 P_2-\tfrac13 P_3$; resolves the five irreducibles of $\Lambda^2 E\oplus E^*$; **not** the Paper 18 Prop 5.1 trace mode (a trace mode cannot resolve $u^c$ from $d^c$) | [SETTLED FACE] / Paper 16 §3 Thm 1 (commutant pattern 5/7/7) |
| *trace mode* | the inter-leg central $\mathfrak u(1)$ | the surplus normalization / global-trace phase (Paper 18 Prop 5.1); central, leakage-flat, normalization-invisible | [Certain] — a MODE, not a face |
| *external bit* | the chirality $\mathbb Z_2$ ($\gamma^5$) | the single sign no internal real-cone-preserving lift can produce; Paper 33 §3 Chirality Boundary; color-protected, count exactly 1 (Paper 16) | [C] — external |

**Degradation ladder (anti-overclaim).** If the ℂ²-leg's compact and non-compact real forms are not two real forms of one complexification, Face A splits back into separate signature and gauge faces (count reverts toward four loose faces); the algebraic layer of this reading currently stands. The *global* geometric realization of Face A has already been refuted by §14.2 (Euclidean-4 manifold, no global $\mathrm{SL}(2,\mathbb C)$ Lie-group action) — only the algebraic + local-tangent reading is asserted. If no single representation-independent $\hbar$-role constant exists, Face C remains a face but unnamed. Every failure path lands on a *stated* weaker count, never on silence.

### 9.5 The arrow of time as the projection-channel dual of the lift

**Corollary 9.7 (Causal structure and the arrow as the down-going dual). [P at its core; [A]/[C] graded above].**
The single Bures lift and its diagonal/measurement projection are one monotone-metric structure read in two directions. The very theorem that forces the metric (Chentsov / Petz–Sudár / Paper 18 §6 uniqueness — the program's general-covariance analog) also forces the arrow: the same metric's contraction under the projection is the data-processing inequality, hence an H-theorem. The lift adds the faces of §9 going *up*; the projection is their arrow-bearing dual coming *down*. The robust core — that the projection channel is monotone, so a coarse-graining direction exists — is $[P]$; the identification of that direction with the conductor-6 leakage flow $\nabla F_M$ (§6 T3 / audit FEP-3) is $[P]$ on $\mathbb Z/6$; the cosmological reading is $[C]$.

### 9.6 The Einstein-like equation as the magnitude-law of the projection non-closure

**Corollary 9.8 (The Einstein-like equation; three GR pillars inherited [P], only sourcing conjectured). [C, reduced].**
General Relativity's content is four pillars, three already proven here (§4.A): (i) metric = second cumulant [P]; (ii) both sides divergence-free, $\nabla\!\cdot T=0$ as the Filippov identity of the Nambu–Fisher bracket [P]; (iv) field equation = stationarity of the one action $\Phi$ [P]. The Einstein-like equation conjectures only the fourth:
\[
\text{(iii) curvature is sourced by stress–energy:}\qquad \delta\mathcal R_{\text{proj}}\;\propto\;T^{(4)}\qquad[\text{C, reduced}],
\]
where $\delta\mathcal R_{\text{proj}}$ is the deviation of the projected back-path's Fisher/Bures curvature from the fixed Hellinger-sphere constant-curvature value, and $T^{(4)}=m^2_{\text{simplex}}$ is the order-4 cumulant defect / jerk (Paper 20 Def. 2.1). The divergence-free LHS combination opposite a $\nabla\!\cdot T=0$ source is *forced* by the same Filippov identity that delivers pillar (ii) — so both *shapes* are inherited [P]; only the proportionality channel is conjectured. This is the magnitude-law of the same projection non-closure whose sign-law is the arrow (Corollary 9.7): one object, two readings — sign $=$ arrow, magnitude $=$ curvature defect.

*The Newton-constant trap.* The proportionality coefficient — the Newton-constant analog — is **permanently out of scope by §12**, exactly as the metric value of $c$, the magnitude of $\hbar$, and the Compton wavelength are. Admissible content is only the *structural form* of the sourcing and any *dimensionless / conductor-fixed* content; never a value of $G$, a curvature magnitude, a length, or a mass.

*Falsifier (matched pair).* If $\delta\mathcal R_{\text{proj}}$ is functionally *independent* of $T^{(4)}$ (the Hellinger-sphere curvature rigidly constant under every admissible projected back-path), there is no sourcing, the Einstein-like equation does not exist, and the gravity homolog is permanently capped at the fixed-background tier — itself a pre-claimed outcome. Conversely any non-trivial $\delta\mathcal R_{\text{proj}}=F(T^{(4)})$, $F\not\equiv0$, confirms the sourcing and is a clean structural result — still **not** General Relativity (§13).

**Remark 9.9 (Raychaudhuri localization).** The Raychaudhuri focusing scalar — the GR object whose sign is geodesic convergence — localizes, in the categorical setting, onto the projection-closure residual: the focusing/defocusing of the projected back-path congruence is governed by the same conductor-6 $T^{(4)}|_M$ that carries the closure defect. Focusing positivity (the energy-condition analog) is the non-tachyonicity of §7; this is the geometric-optics reading of the magnitude law, at the same $[C]$ tier as the sourcing it depends on.

---

## 10. Standard-Model Structure at $\mathbb{Z}/6$

The same finite arithmetic that localizes the gravity residual also fixes a surprising amount of Standard-Model structure, *as pure-number / representation-theoretic facts*, subject throughout to the firewall of §12 (only ratios and structural integers, never magnitudes). This section collects the structural by-products; none of it is required for the gravity thesis of §1–§9, and none of it crosses the firewall.

### 10.1 The two answers, closed

The series asked two recurring questions. Both now have stated, tiered answers.

*Is this quantum gravity?* **[A, structural].** In the *structural-form* sense, yes — at finite primorial, on the categorical-simplex substrate, the framework realizes the gravity–matter decoupling problem of perturbative quantum gravity with an explicit dictionary (§10.2). In the *dimensionful* sense, no — and by §12 it provably cannot be: there is no Newton constant, no Planck scale, no metric on a 4-manifold inside the framework. It is a *layer* of the structure, not its totality.

*Does the framework predict a dimensionless physical constant?* **[A].** It reproduces the tree-level Weinberg angle $\sin^2\theta_W=3/8$ (§10.3), a pure number with no fitting — but this is the textbook $SU(5)$ value, which follows once the $2+3$ split and the representation $\Lambda^2E\oplus E^*$ are put in (§10.3, Provenance). It is a reproduction, not a prediction.

### 10.2 The unification dictionary

The categorical-simplex framework maps onto perturbative-quantum-gravity content as follows; tiers are carried explicitly, and the bottom row is the firewall.

| Perturbative-QG content | Categorical-simplex realization | Status |
|---|---|---|
| gravity–matter decoupling | additive–multiplicative duality of conductor packets; $V$ (non-units) ⊥ $M$ (units) by Pontryagin orthogonality | **[P]** (Paper 47 all-orders) |
| graviton modes (would-be) | finite Dirichlet polynomials on the multiplicative-unit subgroup $(\mathbb Z/P_k)^\times$ | **[A]** |
| QG positivity / no-tachyon | §7 $=$ Paper 22 Weil positivity at primorial | **[P]** $P_2$ cubic; **[C]** all-order |
| Lorentzian signature | local-Casimir hyperboloid on Face A (§14.2A); $(1,3)$ sub-bundle exact on $V$ (§14.2B) | **[P]** local-tangent, *post-diagnosis* (found after the §14.2 refutation of Conjecture 9.4) |
| gauge restoration | Face B color $\mathfrak{su}(3)$ + Face A weak isospin $\mathfrak{su}(2)$ | **[P]** (Paper 18 §6) |
| quantization / Born rule | Kummer cover at integer gauge; Born closure $=$ toric moment map $\mu:\mathbb{CP}^{N-1}\to\Delta^{N-1}$ | **[P]** (T6, T7) |
| Hartle–Hawking signature | $V$-Lorentzian + $M$-Euclidean orthogonal sub-bundle decomposition | **[P]** (Papers 46, 47) |
| Newton $G$, Planck length, graviton mass, 4-metric | **permanently out of scope** by §12 firewall | **[F]** firewall-binding |

### 10.3 The Weinberg angle $\sin^2\theta_W|_{\text{tree}}=3/8$ [A; the arithmetic is P]

This is the framework's load-bearing numerical prediction — a finite linear-algebra computation on a 15-dimensional representation, with no continuous limits, no fitting, no free parameters.

**Setup.** The categorical-simplex spectral-triple inner Hilbert space (Paper 33; Connes–Chamseddine construction with arithmetic justification from CRT $\mathbb Z/6=\mathbb Z/2\times\mathbb Z/3$) is $E:=\mathbb C^2\oplus\mathbb C^3$, $\dim_{\mathbb C}E=5$. The one-generation fermion representation (15 left-handed Weyl fermions) is $F:=\Lambda^2 E\oplus E^*$, $\dim_{\mathbb C}F=10+5=15$. The prime-reciprocal hypercharge is $Y:=\tfrac12 P_2-\tfrac13 P_3$ (Face D), where $P_2,P_3$ project onto $\mathbb C^2,\mathbb C^3$; thus $Y|_{\mathbb C^2}=+\tfrac12$, $Y|_{\mathbb C^3}=-\tfrac13$.

**Decomposition under $SU(2)_L\times SU(3)_c$** with $E=(\mathbf 2,\mathbf 1)\oplus(\mathbf 1,\mathbf 3)$:
\[
\Lambda^2 E=(\mathbf 1,\mathbf 1)\oplus(\mathbf 2,\mathbf 3)\oplus(\mathbf 1,\bar{\mathbf 3}),\qquad E^*=(\mathbf 2,\mathbf 1)\oplus(\mathbf 1,\bar{\mathbf 3}).
\]

**Step 1 — $\mathrm{Tr}(Y^2)$** (the full SM hypercharge spectrum, §10.4) gives
\[
\mathrm{Tr}(Y^2)\big|_F = 1\cdot 1^2+6\cdot(\tfrac16)^2+3\cdot(\tfrac23)^2+2\cdot(\tfrac12)^2+3\cdot(\tfrac13)^2=\tfrac{6+1+8+3+2}{6}=\tfrac{20}{6}=\tfrac{10}{3}.
\]

**Step 2 — gauge trace-squares.** With $\mathrm{Tr}(T^2)|_{\mathbf 2}=\mathrm{Tr}(T^2)|_{\mathbf 3}=\tfrac12$: counting $SU(2)$ doublets in $F$ ($(\mathbf2,\mathbf3)$ thrice, $(\mathbf2,\mathbf1)$ once) gives $\mathrm{Tr}(T_{SU(2)}^2)=3\cdot\tfrac12+\tfrac12=2$; counting $SU(3)$ triplets ($(\mathbf2,\mathbf3)$ twice, two $(\mathbf1,\bar{\mathbf3})$) gives $\mathrm{Tr}(T_{SU(3)}^2)=2\cdot\tfrac12+\tfrac12+\tfrac12=2$.

**Step 3 — tree-level Weinberg angle from GUT normalization.** At unification the rescaled couplings $\hat g_a=g_a\sqrt{T_a/T_*}$ equalize, giving $g_a^2 T_a=$ const, hence $g'^2/g_2^2=T_2/T_Y$:
\[
\sin^2\theta_W\big|_{\text{tree}}=\frac{g'^2}{g_2^2+g'^2}=\frac{T_2}{T_2+T_Y}=\frac{2}{2+\tfrac{10}{3}}=\frac{2}{\tfrac{16}{3}}=\boxed{\frac{3}{8}}.
\]

**Cross-check (GUT-normalized hypercharge).** Set $\hat Y=\sqrt{3/5}\,Y$; then $\mathrm{Tr}(\hat Y^2)=\tfrac35\cdot\tfrac{10}{3}=2=\mathrm{Tr}(T_{SU(2)}^2)=\mathrm{Tr}(T_{SU(3)}^2)$ — all three GUT-normalized generator-trace-squares are equal on $F$, the $SU(5)$-unification consistency condition. Under $SU(2)\times SU(3)\hookrightarrow SU(5)$ with $E=\mathbf 5$, $\Lambda^2 E\oplus E^*=\mathbf{10}\oplus\bar{\mathbf 5}$ — the standard $SU(5)$ fermion content per generation.

**Provenance (retiered 2026-10-01).** The value $3/8$ is the textbook $SU(5)$ result (Georgi–Glashow 1974) for the $2+3$ split. The hypercharge is not forced by arithmetic either: on *any* split $\mathbb C^{p_1}\oplus\mathbb C^{p_2}$, tracelessness $p_1y_1+p_2y_2=0$ forces $Y\propto(1/p_1,-1/p_2)$, so "prime-reciprocal" is tracelessness. The inputs are a *direct sum* $E=\mathbb C^2\oplus\mathbb C^3$ (whereas the CRT gives $\mathbb Z/6\cong\mathbb Z/2\times\mathbb Z/3$, whose function space is the tensor product $\mathbb C^2\otimes\mathbb C^3$) and the *chosen* representation $\Lambda^2E\oplus E^*=\mathbf{10}\oplus\bar{\mathbf 5}$. What $\mathbb Z/6$ contributes is the $2+3$ split. The computation is [P]; the claim that finite arithmetic forces the Standard-Model data is [A]. **Scope:** the measured $\sin^2\theta_W(M_Z)\approx0.231$ differs from $3/8=0.375$ by RG running from the unification scale to $M_Z$ — running that involves continuous gauge dynamics and dimensionful scales the firewall (§12) blocks. The prediction is the *boundary condition at GUT unification*, $3/8$; the agreement is at the same unification-boundary level as $SU(5)$-GUT phenomenology.

### 10.4 The full one-generation hypercharge spectrum [P, computed, given the inputs of §10.3; A as a derivation]

$Y$ acts by derivation on $\Lambda^2$ and by sign-flip on $E^*$; all five values match the SM exactly ($Q=T_3+Y$, left-handed Weyl convention):

| Irreducible | dim | $Y$ | SM identification |
|---|---|---|---|
| $(\mathbf 1,\mathbf 1)$ from $\Lambda^2\mathbb C^2$ | 1 | $+1$ | $e_R^c$ |
| $(\mathbf 2,\mathbf 3)$ from $\mathbb C^2\otimes\mathbb C^3$ | 6 | $+1/6$ | $Q_L$ |
| $(\mathbf 1,\bar{\mathbf 3})$ from $\Lambda^2\mathbb C^3$ | 3 | $-2/3$ | $u_R^c$ |
| $(\mathbf 2,\mathbf 1)$ from $(\mathbb C^2)^*$ | 2 | $-1/2$ | $L$ |
| $(\mathbf 1,\bar{\mathbf 3})$ from $(\mathbb C^3)^*$ | 3 | $+1/3$ | $d_R^c$ |

---

## 11. Structural Shadows and the Honest Yang–Mills Negative

The conductor and Kummer-cover structure at $\mathbb Z/6$ casts further Standard-Model *shadows* — each a structural/representation-theoretic fact, none a dimensionful prediction. We collect them and then state plainly where the program does *not* reach.

### 11.1 Spin, color, chirality

- **Spin-$\tfrac12$ from the Hopf factor of 2 [P, structural].** The Fubini–Study distance on the projectivized simplex is exactly half the Fisher–Rao distance: $d_{FS}([\sqrt p],[\sqrt q])=\arccos\sum_i\sqrt{p_iq_i}=\tfrac12 d_{FR}(p,q)$ (T1 §4, T7 Thm 2.1). The factor of 2 is the Hopf-fibration angle doubling — the angular signature of a spin-$\tfrac12$ object, present structurally as the relation between the simplex and its phase cover.
- **Three colors from the $\mathbb Z/3$ deck at $m=2$ [P, structural].** The Kummer-cover deck group at gauge $m=2$ on $N=6$ is $\mu_6/\mu_2\cong\mathbb Z/3$ (T7), acting on the $\mathbb C^3$ (conductor-3) leg — the structural origin of the three-color index on Face B.
- **Chirality from the $\mathbb Z/2$ deck at $m=3$ [A, structural].** The deck group at the cubic gauge $m=3$ is $\mu_6/\mu_3\cong\mathbb Z/2$ — a structurally available *internal* chirality bit (Face E of the refined count). It is matched against the single *external* chirality bit of the Paper 33 Chirality Boundary (the $\gamma^5$ lock that no real-cone-preserving lift produces, color-protected by §6 thread T2); whether the internal $\mathbb Z/2$ supplies or merely shadows the external bit is the open matched-pair item.

### 11.2 Color confinement: the $A_3$ trichotomy [P, computed]

The $\mathbb Z/3$ deck at $(N=6,m=2)$ trichotomizes the cubic vertices touching the colored ($A_3$) leg into three classes — **monochromatic**, **$M$-mediated**, and **tricolor** — each carrying equal cubic-vertex weight (ratio $1{:}1{:}1$). The $A_3$ packet is *confinement-isolated*: by Corollary 5.1d.2 the colored leg cannot couple cubically except through the carry packet $M$ or in a color-closed (tricolor / pure $A_3$) combination. The structural match to QCD is exact at the combinatorial level: baryon $\leftrightarrow$ tricolor, meson $\leftrightarrow$ $M$-mediated, the symmetric $d^{abc}$ gluon vertex $\leftrightarrow$ monochromatic. This is a *signature* match — the cubic-vertex bookkeeping reproduces the color-singlet selection of confinement — not a dynamical confinement proof.

### 11.3 The honest Yang–Mills negative [A, with strict scope boundary]

The framework provides genuine structural shadows of Yang–Mills physics (color confinement signature §11.2; non-tachyonicity §7; three-gauge unification §10.3; Weil positivity §7) — but it is **not** approaching a solution of the Clay-Millennium Yang–Mills existence-and-mass-gap problem, and we say so explicitly. The five bridges that problem requires are all *absent* here: a continuum limit, the Osterwalder–Schrader axioms, a spectral gap in an infinite-volume Hamiltonian, the Wilson-loop area law, and asymptotic freedom. Each requires the operator-algebraic / continuum completion the firewall (§12) places downstream and out of the present framework's reach. The shadows are real and worth recording; the overclaim is firewall-forbidden. This negative assessment is itself a contribution: it draws the scope boundary sharply enough that the structural matches cannot be mistaken for the analytic theorem.

---

## 12. The Dimensional Firewall

### 12.1 The firewall, and why it holds by construction

Because the simplex carries no length, time, or mass scale (Paper 20 §4), the framework may attempt **only dimensionless quantities fixed by conductor/cumulant structure**. Anything carrying a unit — $\hbar$, $c$, $G$, the Planck scale, any absolute mass or length — is out of scope *by construction*, not by caution. This is the credibility boundary for every constant the program may discuss; adjacent literature has crossed it (e.g. writing mass $=$ rest-binding-energy$/c^2$ smuggles in $c$).

It is more than a discipline rail. The closure operator $\operatorname{Cl}_n$ generating the framework's finite renormalization (Appendix A, T13) acts on a **finite combinatorial lattice — the divisor/conductor lattice $\mathcal D_N$ — that carries no physical-unit parameter**. Every quantity the framework derives, *including the projected curvature defect* of §4–§9 (which T14 places on the conductor-fusion boundary $\partial_n S\subseteq\mathcal D_N$), is determined by finite combinatorial gadgets — the conductor lattice, the packet decomposition, the closure operator, and the apex closure polynomial — and therefore carries no dimensionful information.

**Principle 12.1 (The Firewall Principle; true by construction).**
*Status.* The substrate carries no unit, so no quantity computed from it can carry one: this holds by construction, and we state it as a principle, not a theorem.
Every finite-RG-derived quantity of the framework — including curvature, RG/beta, and Noether content — is a function on the finite combinatorial lattice $\mathcal D_N$ and is therefore dimensionless. Consequently:
1. The framework is necessarily a *layer* of physics, not its totality.
2. No path inside the finite substrate (T0–T14) reaches a dimensionful prediction.
3. The only legitimate route to a magnitude is the operator-algebraic completion (downstream of the geometric layer), which is outside the present framework.
4. The firewall extends uniformly to *curvature*: $\delta\mathcal R_{\text{proj}}$ lives on $\partial_n S\subseteq\mathcal D_N$, so Newton's constant, Planck curvature, and the cosmological-constant magnitude all remain external. Any future claim of a dimensionful constant — including any dimensionful curvature — directly contradicts this principle.

### 12.2 The admissible category: unity-by-construction and pure ratios

A subtle but admissible category sits *inside* the firewall: constants whose content is the *theorem that they are unity and invariant*, not a numerical value. Corollary 9.6's $c\equiv1$ is the archetype — the framework derives that an invariant speed *exists*, is frame-independent, is the hyperboloid asymptote, and equals 1 in internal units, and explicitly does **not** predict its metre/second value. This is the template for every future constant claim: a *structural* prediction (existence, invariance, a fixed rational ratio between sectors) is admissible; a *dimensionful magnitude* never is. The same status applies uniformly to the Einstein-like coupling (§9.6, the Newton-constant analog is excluded), the $\hbar$-role (§9.3 Part 3), and the arrow's *rate* (Corollary 9.7: direction inferable, rate not).

### 12.3 The three admissible targets of the $c$–$\hbar$ pair

The firewall permits *exactly one* constants question over the paired invariants: which **dimensionless** combinations of $c$, $\hbar$, and the conductor/cumulant combinatorics are structurally fixed. Three candidate targets are pre-enumerated so the question cannot later drift:

1. **Simplex-mass ratios across conductor sectors.** Firewall-legal in *form* (a ratio of $T^{(4)}$ coefficients); **settled-negative** in *content* on $\mathbb Z/6$ — the leading $T^{(4)}$ coefficient is exactly zero on the carry/isolated-axis specifications (Corollary 6.2 thread T1, the four-thread root). The pre-claimed negative branch fires here.
2. **Compton-type closure of the program's own mass object.** The Compton *wavelength* $\bar\lambda_C=\hbar/(mc)$ is a *length* and is permanently out of scope — named here as the firewall trap so it cannot be smuggled back. Admissible is only the dimensionless closure identity $mc\,\bar\lambda_C/\hbar=1$ read as: does the simplex-mass object close, in its $c/\hbar$-roles, to a *non-trivial* conductor-fixed pure number (trivial-1 excluded as informationless)? **[C, reduced].**
3. **The $\alpha$-shaped prime-reciprocal pure number** (Paper 33 anchor; highest firewall risk). Pursued, if at all, strictly as a scale-free combinatoric ratio under the §13 carried-label discipline. **[C, reduced].**

---

## 13. Relationship to Emergent Gravity, and the Guardrails

### 13.1 Positioning against the emergent-gravity school (the guardrail is the contribution)

There is a legitimate external lineage — Jacobson's "Einstein equation of state," and the Padmanabhan and Verlinde thermodynamic/entropic-gravity programs — that derives gravitational dynamics from thermodynamic or information-theoretic premises. This paper *positions against* that lineage at the level of claim strength, while sharing some of its structural vocabulary. The difference is the firewall (§12): the emergent-gravity programs aim at the dynamical Einstein equation *with* its dimensionful Newton constant; this program proves only the *form* of the gravity question — its arithmetic localization, the dimensional selection, and the lift status of signature — and holds, by construction, that no dimensionful constant can be reached from inside. The guardrail is not a hedge; it is the contribution. Where the emergent-gravity school claims gravity, this program claims to have arithmetized the *shape* of the claim and to have fenced off the part that would require new (operator-algebraic, continuum) inputs.

### 13.2 The surviving structural number $1/2^Q$

The one geometric-combinatoric pure number the framework furnishes unconditionally on a $Q$-state row is the orthant fraction $1/2^{Q}$ — the fraction of the sign-orthants of $H_R$ compatible with a fixed positive-cone orientation. It is firewall-clean (a pure number, no unit), conductor-fixed, and is *not* to be confused with the simplex-mass closure target of §12.3 (which is settled-negative on $\mathbb Z/6$). It is recorded as the row's admissible structural integer, nothing more.

### 13.3 The carried-label discipline (methodological commitment)

Every constant or ratio the program states must carry, inline, (a) its tier $[P]/[A]/[C]$, (b) its firewall status (pure number vs. dimensionful, with dimensionful magnitudes excluded by §12), and (c) its anchor definition. No constant is asserted without all three labels. This discipline is what keeps the structural by-products of §10–§11 from drifting into overclaims; it is the operational form of the firewall theorem.

---

## 14. The Three Finite Audits

Three named finite computations on the Paper 14 exact integrator convert the $[A]$ items of §1.1 to $[P]$ or refute them. Two have been run; one remains specified-but-pending. The full pre-registered run specification (observables, controls, panel layout, verdict inequalities) is **Appendix C**.

### 14.1 Depth audit (targets [A] item 8, the B-bound, the S-sign) — pending

Reuse Paper 17 §5's exact $\mathbb{Z}/6\hookrightarrow\mathbb{Z}/12,\mathbb{Z}/18$ Constraint-3 procedure on the 5-dimensional integrator, instrumented to read $\|R^{\Pi_\tau}\|$ on the conductor-6 mode and the sign of the conductor-6 Noether form. **Pass:** the residual remains supported on the squarefree conductor-6 mode, bounded, and sign-definite under prime-power depth ($2^2,3^2$). **Fail:** a new depth-induced carry axis, refuting time-translation closure on the row and flagging a Paper 22 stress point. Status: specified (Appendix C, panel d), not yet run.

### 14.2 Bures-dispersion audit — SETTLED: Euclidean-4 at the manifold level

**The pre-registered question.** Lift the energy to $\operatorname{tr}(H\rho)$ on $D(\mathbb C^2\otimes\mathbb C^3)$, restricted to the conductor-2 ⊕ conductor-3 packets; check whether the level set $\operatorname{tr}(H\rho)=E$ is a genuine two-sheeted hyperboloid invariant under a 3-parameter Cartan-completing group. Hyperboloid $\Rightarrow$ Lorentzian $3+1$ as a lift phenomenon (Conjecture 9.4 confirmed); ellipsoid / wrong-dimensional group $\Rightarrow$ intrinsically Euclidean-4. Both branches were pre-claimed.

**Settlement.** The audit was run (`empirical/paper32_13_2_bures_dispersion_audit.py`, deterministic transcript archived) on $V=A_2\oplus A_3\subset\mathbb C^6$ ($\dim_{\mathbb R}D(V)=8$) across five distinct Cartan-respecting Hamiltonians $H=a\,\sigma_3\!\otimes\!I+b\,I\!\otimes\!\lambda_3+c\,I\!\otimes\!\lambda_8$. Four diagnostics, identical verdict on all five runs:
- **(A) Signature of $H_V$:** generically $(1,1,1)$ — indefinite (passes the *necessary* condition only).
- **(B) Level-set topology:** the slice of $D(V)$ by $\operatorname{tr}(H_V\rho)=E$ is **connected, compact, real dimension 7 — no two-sheeted decomposition, no non-compact asymptote.**
- **(C) Bures metric at $\rho_*=I/3$:** reduces to $3\cdot I_8$ on the Gell-Mann basis — signature $(8,0,0)$, positive-definite Riemannian, *not* pseudo-Riemannian.
- **(D) Cartan-completing group:** the centralizer in $U(3)$ is the maximal torus $U(1)^3$ — the right *count*, but **compact and toric**, not the non-compact $\mathrm{SO}(3,1)/\mathrm{SO}(3)$ boost group a Lorentzian level set requires.

**Verdict.** *Conjecture 9.4 is refuted at the manifold level on the $\mathbb Z/6$ conductor-2 ⊕ conductor-3 block; the framework is intrinsically Euclidean-4 there* — the pre-claimed branch, now realized. The invariant-speed asymptote (Corollary 9.6 Part 2) falls with it: there is no asymptote on a compact level set. Theorem 9.1's classical $(3,1)$ stands as a contact-geometric/Legendre split on the *fixed* Hellinger-sphere background; it is *not* promoted to a Lorentzian metric by this lift. Untouched: gauge restoration (Face B, and Paper 18 Thm 6.1 — independent of dispersion), the $\hbar$-role face (a distinguishability-*rate* statement), the Einstein-like equation R′, the arrow, the four-thread root, and $1/2^Q$.

**Refinement (§14.2A–B — the local Lorentzian sub-bundle).** The original specification was structurally inadequate in one respect: $\operatorname{tr}(H\rho)$ is *linear* in $\rho$, so its level sets on the convex body $D(V)$ are affine slices — never a quadric, so the question was unfalsifiable in the affirmative. The corrected object is the *Casimir–Hessian* at the centroid: there a genuine local **Lorentzian $(1,3)$ sub-bundle on $V$ does exist**, and it persists *to all orders* (the V-Lorentzian / M-Euclidean orthogonal decomposition — the Hartle–Hawking-flavored signature of Papers 46–47). The settled reading is therefore two-layered and is exactly what the refined face count (§9.4) asserts: **manifold-level Euclidean-4, local-tangent Lorentzian on $V$.** The non-compact real form of Face A survives at the algebraic and local-Casimir levels only; the global geometric collapse is permanently dropped.

### 14.3 Souriau-cocycle audit (targets [A] item P) — specified

Check whether the time-translation non-equivariance defect of §5 is a nontrivial Souriau symplectic-cohomology cocycle class supported on conductor 6 (Barbaresco/Marle formulation). A nontrivial class names *gravity-as-Noether-anomaly* as a genuine cohomology class; a trivial (coboundary) class reduces the defect to a removable normalization. Status: specified (Appendix C, panel-d inset), pending.

---

## 15. Falsifiers and Failure Modes; Gap Ledger

### 15.1 Falsifiers

- **F1.** A measured time-translation residual in $A_2$ or $A_3$ (forbidden by Lemma 5.1) ⇒ the selection-rule derivation is wrong; §5 collapses.
- **F2.** The depth audit produces a new carry axis or an unbounded / sign-indefinite conductor-6 residual ⇒ time-translation closure fails on the row; the Theorem 7.1 tie-in breaks.
- **F3.** The closure-failure locus coincides with $\{\nabla^{(e)}T=0\}$ ⇒ contradicts Paper 17 Theorem 3.1; the "arithmetic-not-dynamical selection" claim fails.
- **F4.** A closure-valid inertial-projector self-model exists in a $Q\ge5$ row ⇒ dimensional selection (Theorem 8.2) is false.
- **F5.** Asserting Lorentzian $3+1$ as a *manifold-level* lift on $\mathbb Z/6$ after §14.2's Euclidean-4 settlement ⇒ overclaim; the paper falls back to the Euclidean-4 + local-Lorentzian reading as written.
- **F6.** Any claim of a metric, weak-field limit, lensing, or cosmology ⇒ guardrail violation; Paper 31 §13 is only *partially* discharged.
- **F7.** Any statement assigning a *dimensionful value* to $c$, $\hbar$, $G$, or any mass/length — including a metre/second value of the invariant speed ⇒ firewall violation (Principle 12.1). Existence, invariance, and $c\equiv1$-in-internal-units are the only admissible claims.

### 15.2 Technical gap ledger

- **G1.** The centroid convolution form of $K^{CH}$ is leading-order; a full realization must carry $D_t\eta$, $D_t\Pi$, and connection terms. The selection rule is exact at the centroid (Lemma 5.1c); off-centroid coefficient corrections need the §14.1 audit.
- **G2.** $C_6$ (the conductor-6 convolution norm) is finite but its explicit value and $N$-scaling are required for the gravity boundary conditions; pending §14.1.
- **G3.** Euclidean symmetries and any physical-space embedding remain external to the simplex; §8's "experienced space" is the closure-valid block, not yet a physical-space reconstruction.
- **G4.** The local-Lorentzian sub-bundle of §14.2A–B is established at the Casimir-Hessian level; its global integrability is open (and refuted as a *manifold-level* collapse by §14.2).
- **G5.** The all-order limit of Theorem 7.1 inherits every open analytic input of Paper 22 §8; only the $P_2$ cubic-order instance is $[P]$ here.

---

## 16. Connection F — One Functional, Two Readouts: the String Order-Readout Bridge

*This section records a cross-theory connection — an "order-readout" reading of the string-theoretic critical dimension — as a structural by-product, in the same register as §10–§11: none of it is required for the gravity thesis of §1–§9, all of it is bound by the firewall principle (§12, Principle 12.1), and its one numerical weld is reported as a settled negative (§16.4). The connection is a **dictionary at the level of order-of-derivation**, not a derivation of string theory. It is labeled "Connection F" as the program's first cross-theory link given its own section; the informal predecessors are the external-precedent remarks already carried inline (Zhang–Li §2.2; Koszul–Souriau–Fisher §3.2; Tomita–Takesaki §9.5; the emergent-gravity positioning §13). Every quantity below carries its tier, its firewall status, and its anchor per §13.3.*

The thesis in one line: **the string critical dimension is an order-2 (central-charge) verdict, and the internal data it cannot see are order-3 (Yukawa) — the same order-2/order-3 split the program builds as $\nabla^2\Phi$ and $\nabla^3\Phi$ from one functional.** "Extra dimensions," read this way, are an order-2 instrument's name for central charge it has no higher-order channel to resolve.

### 16.1 Part I — the $[P]$ spine

**(I.1) The order-2 verdict (string side). [P, standard; restricted.]** The critical dimension is fixed by the total Virasoro central charge $c$ — an **order-2** datum: the $c$-number in $[L_m,L_n]=(m-n)L_{m+n}+\tfrac{c}{12}m(m^2-1)\delta_{m+n,0}$, equivalently the coefficient of $\langle T(z)T(0)\rangle=(c/2)/z^4$, equivalently the Weyl/trace anomaly $\langle T^i{}_i\rangle=-(c/12)R^{(2)}$. Bosonic $c^{\mathrm{tot}}=D-26$; superstring $c^{\mathrm{tot}}=\tfrac32 D-15$; vanishing fixes $D=26,10$. The rigorous content of "*higher orders never re-enter the dimension count*" is the **Curci–Paffuti theorem** (Curci & Paffuti, Nucl. Phys. B286 (1987) 399; Polchinski Vol. 1 §3.7): at a worldsheet fixed point ($\beta^G=\beta^B=0$) the dilaton beta-function $\beta^\Phi$ is a *spacetime constant* equal to the central charge, so $\alpha'$/curvature/higher-loop data renormalize *which background* exists, never the integer $c$-count. **Restriction carried:** the invariant is $c^{\mathrm{tot}}=0$, *not* "$D=26$"; $D=c$ only at the flat ($Q=0$) realization — linear-dilaton/Liouville solve $c^{\mathrm{tot}}=0$ at $D\neq26$ via $D+6Q^2=26$. And this is a *Virasoro* statement: the $W_3$-string fixes $c=100$ via an order-3 $W$-OPE, the boundary case. Firewall status: $c$, $D$ are **pure numbers** (no unit); the string scale, $\alpha'$, $g_s$ are out of scope by §12. Anchor: Polchinski Vol. 1 §3.4, §3.7; Polyakov (1981).

**Remark 16.1a (Curci–Paffuti is the string-side instance of the Firewall Principle). [P, observed here].** Principle 12.1 says every finite-RG-derived quantity of the program is a unit-free function on the finite lattice $\mathcal D_N$. Curci–Paffuti says the string's RG-derived dilaton charge collapses, at any fixed point, to a single unit-free constant — the central charge. These are the *same move*: an RG flow whose only fixed-point-invariant output is a dimensionless number fixed by structure, with the dimensionful data (the background, the scale) living strictly downstream. The string's central charge is the worldsheet analog of the program's "admissible structural integer" (§13.2). This identification is new to the bridge and tightens §12.1's claim that the firewall pattern is not parochial.

**(I.2) The order-3 verdict (string side). [P, standard].** The data that separate internal CFTs of *equal* central charge are order-3: the Yukawa couplings $\kappa_{ijk}=\partial_i\partial_j\partial_k F$ — third derivatives of the special-geometry prepotential $F$ = chiral-ring structure constants = the classical cubic intersection form on $H^2$ at large volume (exact for the $(2,1)$ sector; plus genus-0 Gromov–Witten instantons for $(1,1)$). **Boundary correction carried:** order $\le 2$ also fixes the cohomology *dimensions* $h^{1,1},h^{2,1}$ and the spectrum; order 3 is the *ring multiplication*. Anchor: Candelas–de la Ossa–Green–Parkes; Strominger (special geometry); Lerche–Vafa–Warner (chiral rings).

**(I.3) The division-algebra substrate. [P, standard].** $\{3,4,6,10\}=\dim_{\mathbb R}\mathbb K+2$ for $\mathbb K\in\{\mathbb R,\mathbb C,\mathbb H,\mathbb O\}$; brane scan $\{4,5,7,11\}=\dim_{\mathbb R}\mathbb K+3$. The supersymmetry cocycle generating the magic dimensions is the **cubic** (3-cocycle) Lie-superalgebra cohomology class for strings (4-cocycle for branes) — an *independent, cohomological* corroboration that the relevant structure is order-3, unrelated to the Yukawa route of (I.2). **Labeling enforced (Remark 9.1a):** $D=4$ is the $\mathbb C$ rung, $D=10$ the $\mathbb O$ rung; the gap $\dim_{\mathbb R}\mathbb O-\dim_{\mathbb R}\mathbb C=6$ is a **consistency identity only** (the $+2$ offset cancels in any rung difference) and carries no predictive weight. Anchor: Kugo & Townsend (1983); Sudbery (1984); Baez & Huerta (arXiv:0909.0551, 1003.3436).

**(I.4) The program-side objects these meet. [P, internal; exact-certified].** From one functional $\Phi=\log Z$ the program builds an order-2 metric (Fisher $g=\nabla^2\Phi$, §3 — *space = inertia*) and an order-3 totally symmetric cubic (Amari–Chentsov $T=K^{CH}=\nabla^3\Phi$, §5). Dimensional selection (Theorem 8.2) puts the program at spatial dimension 3 — the $\mathbb C$ rung in the spinor convention (Remark 9.1a). $T_{klm}=216\cdot\mathbb 1[k+l+m\equiv0\bmod6]$ is pure character orthogonality (Lemma 5.1a). The companion *FaithfulnessObstruction* divisor rule is the order-selectivity statement: a $k$-resolution readout retains exactly $\bigoplus_{d\mid k}H_d$.

**Part I synthesis. [P] (each leg); [A] (the identification — see §16.2).** Both sides produce a metric at order 2 and a totally symmetric cubic at order 3 as successive derivatives of *one* generating function — prepotential $F$ (string), log-partition $\Phi$ (program) — with the order-3 object being the Yukawa/Amari–Chentsov tensor in each. This is the "one functional, two readouts" of the title; each leg is $[P]$ individually, and the *identification of the two functionals* is the $[A]$ weld of §16.2.

### 16.2 Part II — $[A]$ order-spectroscopy (the welding)

**(II.1) The order ledger.** The dictionary below is the spectroscopic axis. *Prior art:* the general "cumulant order $=$ correlator order over one potential, with order-3 $=$ structure constants" framing is **arXiv:2605.03063** (Fisher–correlator–hypergraph triality, 2026; already in the program's reference set). The novelty claimed here is *only the string-specific welding* — the right-hand column against the program column — not the ledger itself.

| order $n$ | program: $\nabla^{(n)}\Phi$ | string / CFT object | status |
|---|---|---|---|
| 1 | centroid / $e$-affine position | vacuum / one-point data | $[P]$ both sides |
| 2 | Fisher metric $g$ (= space = inertia) | central charge $c$ / stress 2-point $C_T$ | $[P]$; **fixes $D$** |
| 3 | Amari–Chentsov $T=K^{CH}$ | Yukawa $\kappa_{ijk}$ / conformal-collider $t_2,t_4$ | $[A]$ weld (II.3) |
| 4 | jerk $T^{(4)}=\nabla^{(e)}T$ | $\langle TTTT\rangle$ / higher stress data | $[C]$ |

**(II.2) The cleanest external instance: SUSY at order 3. [P] (CFT facts); [A] (as a blind-spot instance).** Four-dimensional $\mathcal N=1$ supersymmetry forces the Hofman–Maldacena conformal-collider parameters to $t_4=0$ and $t_2=6(1-a/c)$, with $\tfrac12\le a/c\le\tfrac32$ (Hofman & Maldacena, arXiv:0803.1467; Osborn–Petkos). One symmetry annihilates one independent order-3 stress-tensor invariant and slaves the other to the order-2 pair $(a,c)$: an order-2 instrument $(a,c)$ is *provably blind* to independent order-3 structure. This matched the program's pre-registered order-2-blind-to-order-3 falsifier verbatim. It is an *instance*, not an identity ($t_4=0$ also holds for free theories carrying no $\mathbb Z/6$ conductor content; no map from "$\mathcal N=1$ SUSY" to a divisor index $k$ has been exhibited).

**Remark 16.2a (Two origins of the conductor blind spot). [P, observed here].** The program's *Conductor Blind Spot* line has, until now, exhibited the blind spot as a consequence of **truncation** — reading only to order 2 (Faithfulness­Obstruction; LeJEPA; Amaral). The SUSY $t_4=0$ result is a distinct origin: the order-3 invariant is annihilated by a **symmetry**, not by the reader's truncation. So the blind spot has two sources — *instrumental truncation* and *symmetry-enforced vanishing* — and the string/CFT side furnishes the first clean external example of the second. This is a genuine sharpening of the CBS thesis and a candidate cross-reference into the FaithfulnessObstruction line.

**(II.3) The $\kappa\leftrightarrow T$ weld, honestly. [A].** Both $\kappa_{ijk}$ and $T=K^{CH}$ are totally symmetric rank-3 tensors equal to $\nabla^3$ of one potential, and in both cases the order-2 metric and order-3 cubic descend from that one function. The weld stays $[A]$, not $[P]$, for four named reasons: (i) holomorphic-complex (string) vs real-statistical (program); (ii) the string cubic is instanton-corrected, the program's $T_{klm}$ is exact-arithmetic; (iii) special geometry / $tt^*$ ties order-2 to order-3 by an integrability constraint $R=-gg-gg+C\bar C\,e^{2K}g$ that a *generic* statistical manifold need not satisfy; (iv) **no explicit coordinate map $\Phi\to F$** has been produced. **Carried-label discipline (§13.3): never write "$=$" between $\kappa_{ijk}$ and $T$; write "is the order-3 analogue of."** Lift to $[P]$ requires the map of (iv); the integrability question (iii) is **resolved** by Remark 16.2b — the curvature form matches *exactly* at the centroid, leaving the jerk as the sole, named obstruction.

**Remark 16.2b (The curvature-form match: exact at the centroid, obstructed by the jerk). [P (the identity); sharpened $[A]$ (the rigidity)].** The integrability question (iii) has been computed. The program's Fisher–Rao (Levi-Civita) Riemann curvature is an *exact pointwise identity* in the cubic, $R=\mathrm{AN}(T)$ — the Amari–Chentsov contraction. *Provenance:* this is the classical curvature identity of Hessian geometry, $R(X,Y)=-[\gamma_X,\gamma_Y]$ with $\gamma=\tfrac12g^{-1}T$ (Shima 2007; Amari–Nagaoka 2000), valid for every Hessian metric at every point; the program's contribution is its exact certificate, and $K=\tfrac14$ likewise holds at every point (Paper 54, Proposition 5.2, cert K4). It is verified by exact arithmetic on $\mathbb Z/3,\mathbb Z/4,\mathbb Z/6$ at *and* off the centroid (every cell `R=AN: True`). This is the *same* "curvature $=$ cubic$\cdot$cubic" structure special geometry carries ($R=-gg-gg+e^{2K}C\bar C$): the program owns the cubic-contraction term *exactly*. At the centroid the program is a constant-curvature sphere — $K=\tfrac14$, scalar $R=D(D-1)/4$ — so the *full* special-geometry / very-special-real form (the constant $-gg-gg$ background *plus* the cubic term) holds there. It breaks *off* the centroid for one precise reason: the program's cubic *flows* (its derivative $\nabla^{(e)}T=T^{(4)}$, the jerk, is non-zero), whereas the rigid very-special-real form requires a *constant* cubic ($\partial^3$ of a degree-3 prepotential). In one line: the program is a **log-sum-exp Hessian** (cubic flows); string / very-special-real geometry is a **$-\log$-cubic Hessian** (cubic constant); the whole gap is the non-constancy of the cubic. **Consequence for the weld:** the curvature *identity* $R=\mathrm{AN}$ is $[P]$ and exact, and the special-geometry *form* holds at the centroid — so reason (iii) above is *discharged*, not open; what stays $[A]$ is only the global *rigidity*, and its obstruction is now *named* — it is the jerk $T^{(4)}$. **The single object separating the program's information geometry from a rigid string/special-geometry structure is therefore the fourth cumulant** — the very jerk the order ladder (§16.1) places one rung above the dimension-fixing metric, closing Connection F on the object it opened with. (Exact cert `empirical/phiF_curvature_reverify.py`: $R=\mathrm{AN}$, $K=\tfrac14$, scalar $R=D(D-1)/4$, verified independently on $\mathbb Z/3,4,5,6$ at *and* off centroid.)

### 16.3 Part III — the landscape blind spot, $[C]$-narrowed (with the equal-$c$ exhibit pinned, $[A]$)

**(III.1) The genuine exhibit. [P].** Internal CFTs of equal central charge that are order-2-indistinguishable genuinely exist: a Calabi–Yau 3-fold vs a Gepner point at $c=9$ ($\hat c=6$); the 168 Gepner tensorings at $c=9$; the $c=1$ free-boson moduli line. An order-2 readout (the central charge) cannot separate them; they first differ at order $\ge3$ (the chiral-ring Yukawas). This is a bona-fide "one object, two instruments" phenomenon.

**(III.1a) The named order-3-first pair, pinned. [P] (the topology); [A] (as a clean order-2-blind-to-order-3 instance).** The pre-registered open lever (§16.5, item 3) asked for a *named* pair of internal CFTs with equal $(h^{1,1},h^{2,1})$ but distinct triple-intersection/Yukawa numbers, *excluding* mirror and Landau–Ginzburg-phase pairs, with smallest distinguishing correlator order $\ge3$. It is now supplied. Take the smooth Picard-rank-1 Calabi–Yau threefolds $X_5$ and $X_{25}$ of Kanazawa (A. Kanazawa, *Pfaffian Calabi–Yau Threefolds and Mirror Symmetry*, arXiv:1006.0223; Comm. Number Theory Phys. 7 (2013) 559–601, Theorem 1.2). Both have $(h^{1,1},h^{2,1})=(1,51)$ — *identical* order-$\le2$ data: $\hat c=6$ (the universal CY3 value) and identical marginal spectrum. They differ only at order 3: the degrees are $\int H^3=5$ and $\int H^3=25$, with $\int c_2\!\cdot\!H=38$ versus $70$. Because $h^{1,1}=1$, the *entire* cubic form on $H^2$ collapses to the single integer $H^3$ — the classical genus-0 Yukawa coupling — so "order-2 agree, order-3 differ" is, here, literally "same Hodge $(1,51)$, different degree $5$ vs $25$." The smallest correlator order that separates them is exactly $3$.

**(III.1b) The Wall backbone. [P, standard].** Distinct order-3 data force genuine topological distinctness, the strongest sense of "not the same CY." By Wall's classification theorem (C.T.C. Wall, *Classification problems in differential topology V: On certain 6-manifolds*, Invent. Math. 1 (1966) 355–374), the diffeomorphism type of a smooth simply-connected closed spin 6-manifold is fixed by its cohomology, the trilinear cubic intersection form $\mu(x,y,z)=\langle x\cup y\cup z,[M]\rangle$ on $H^2$, the linear form $p_1(x)$, and torsion; CY3 are spin ($c_1=0$) and, in these cases, simply connected with torsion-free cohomology, so the theorem applies cleanly. Kanazawa states this for exactly this exhibit (verbatim): the invariants $\int_X H^3,\ \int_X c_2(X)\!\cdot\!H,\ \int_X c_3(X)$ "determine the diffeomorphism class of $X$ when $X$ is simply connected and $h^{1,1}=1$ (Wall's classification theorem)." Since $5\neq25$ (and $38\neq70$), $X_5$ and $X_{25}$ are **non-diffeomorphic**, hence not deformation-equivalent and not two phases of one CY. The Euler-characteristic datum is the consistency check that must *agree*: $c_3=\chi=2(h^{1,1}-h^{2,1})=-100$ for both, exactly as equal Hodge numbers require (numpy/sympy-checked).

**(III.1c) The three exclusions and the avoided forced-match. [P].** *Not a mirror pair:* mirror symmetry swaps $(h^{1,1},h^{2,1})\to(h^{2,1},h^{1,1})$, so each member's mirror is a $(51,1)$ manifold; neither is the other's mirror, and the equal spectrum is honest (Hodge numbers literally identical, not swapped). *Not LG/geometric phases of one CY* and *not deformation-equivalent:* phases and deformations share topology, which $X_5,X_{25}$ provably do not. *No GL$(n,\mathbb Z)$ basis-change artifact:* at Picard rank 1, GL$(1,\mathbb Z)=\{\pm1\}$ and orienting $H$ as the ample generator fixes $H^3$ as a positive integer, so $5$ and $25$ are honest integral invariants with no rank-$>1$ basis subtlety to dismiss — the residual worry the open lever carried is *eliminated*, not merely argued away. **Forced-match trap explicitly declined (GPD discipline, Paper 35):** the classic equal-Hodge/different-degree pair (Rødland's degree-14 Pfaffian $X_{14}$ vs the $G(2,7)$ section, both $h^{1,1}=1$, $h^{2,1}=50$) is *not* used, because it is a derived-equivalent "double mirror" sharing one stringy Kähler moduli space (Rødland, arXiv:math/9801092; Borisov–Căldăraru, arXiv:math/0608404) — precisely the mirror-equal-Yukawa class the lever excludes. The Picard-rank-1 Kanazawa pair carries no such derived-equivalence.

**(III.1d) Tier, carried label, and what is *not* claimed. [A].** The topology is $[P]$; the reading of $X_5/X_{25}$ as the *order-2-blind-to-order-3* instance is $[A]$, lifted from the $[C]$ of the prior draft by the now-named exhibit. **Carried-label discipline (§13.3):** write "$H^3$ *is the order-3 datum the order-2 readout cannot see*," never "$\hat c$ misses $H^3$" as if the two were of one type; the order-$\le2$ SCFT readout ($\hat c=6$ plus the marginal/Hodge spectrum) is identical across the pair, which is exactly the claim, while $c_2\!\cdot\!H$ is itself order-3-adjacent (cubic/one-loop $\sigma$-model) data, not an order-2 SCFT invariant. Even with $c_2\!\cdot\!H$ set aside, $H^3$ *alone* already separates the pair ($5\neq25$), so the pure-cubic-Yukawa separation stands on its own. **No new geometry is claimed:** both load-bearing facts — Wall's topological separation and the chiral-ring $=$ cohomology-ring / Yukawa $=$ cubic-form dictionary (Candelas–Dale–Lütken–Schimmrigk 1988; Greene, hep-th/9403096) — are standard; Connection F contributes only the *reading* of this known structure as the exact string-side witness of the program's order-2/order-3 blind-spot line, not a new Calabi–Yau theorem.

**(III.2) The narrowing (honest). [C], narrowed.** The *total* claim — "the $\sim\!10^{500}$ string landscape **is** an order-2 readout degeneracy" — is **false** and is not made: bulk landscape multiplicity comes from flux quanta / topology / Hodge numbers, which *are* order-2-distinguishable, and the order-3 Yukawas separating equal-$c$ vacua are routinely computed (not a blind spot of the *theory*, only of an *order-2 instrument*). The defensible residue, now anchored by (III.1a–c): *equal-$(c,\text{spectrum})$ internal CFTs differing only in cubic-and-higher couplings are an order-2 blind spot of an order-2 instrument, separated first at order 3* — the $X_5/X_{25}$ pair is the explicit witness. **Falsifier (pre-registered):** either (a) a strictly order-$\le2$ SCFT invariant of $X_5/X_{25}$ (beyond $\hat c$ and the Hodge spectrum) that already separates them — lowering the distinguishing order to $\le2$ and killing the order-3-first residue — or (b) a derived-equivalence / shared-mirror relation between $X_5$ and $X_{25}$ that makes their A-model Yukawas coincide after the mirror map — collapsing the exhibit into the excluded double-mirror class. Either horn downgrades the residue back to $[C]$ illustrative.

**Remark 16.3a (The landscape confirms escapability, not mystery). [observed here].** Read correctly, Part III is *positive* for the program's core thesis. The string landscape is the largest-scale demonstration that the blind spot is a property of the *instrument*, not the *system*: a higher-order instrument (string theorists computing Yukawas — here, reading the single integer $H^3$) sees straight through the order-2 degeneracy. That is precisely "climb the order axis and the degeneracy lifts" — the same statement as "extra dimensions dissolve at order 3" (§16.1). The honest narrowing thus *strengthens*, rather than weakens, the "readout determines what is visible" thesis: it shows the readout's *order* is the operative knob and that the obstruction is escapable, not fundamental. (Open lever §16.5 item 3 is hereby discharged to $[A]$; what remains $[C]$ is only the *total*-landscape over-claim, which is correctly disavowed.)

### 16.4 Part IV — the packet-central-charge weld, reported as a settled negative

In the register of the honest Yang–Mills negative (§11.3): the *one* numerical weld attempted — that the conductor-packet "carry" sector reproduces $\hat c_{\mathrm{internal}}=6$ via a natural central-charge analogue — is **refuted**.

**(IV.1) The negative. [C] $\to$ REFUTED.** Two independent exact-arithmetic computations on $\mathbb Z/6$ *and* $\mathbb Z/30$ — 26 candidate definitions (dimension / structure-constant / Sugawara families) and 6 (lattice-VOA / parafermion family) — agree that **no natural packet central charge equals 6 in a ring-stable way**. Specifically: $\dim M=\varphi(N)=2$ ($\mathbb Z/6$), $8$ ($\mathbb Z/30$), never 6 ($\varphi=6$ only at $N\in\{7,9,14,18\}$, no squarefree primorial). The seductive near-miss $\varphi(N)$ tracking division-algebra dimensions ($\varphi(6)=2=\dim_{\mathbb R}\mathbb C$, $\varphi(30)=8=\dim_{\mathbb R}\mathbb O$) **terminates**: over the primorial ladder $\varphi=1,2,8,48,480$ it skips $\dim_{\mathbb R}\mathbb H=4$ entirely and diverges at $\varphi(210)=48$ — a forced-match of exactly the class the GPD methodology (Paper 35) is built to reject. The Sugawara route is *structurally* impossible: $T_{klm}$ is a totally symmetric **abelian** convolution tensor, not an antisymmetric Lie bracket $f^{abc}$ — there is no dual Coxeter number and no Kac–Moody central term to transfer.

**(IV.2) What is confirmed. [P]-arithmetic / [A]-assignment.** Both methods, both rings, independently give the *whole* packet algebra central charge $c=1$ (compact-boson / $U(1)$), matching Corollary 9.6 (two covariant derivatives of one $\Phi$ admit no independent normalization $\Rightarrow$ conversion constant $1$) and the $\hat c=1$-per-boson string reading. $c=1$ is $N$-blind ($\mathbb Z/6=\mathbb Z/30=1$) — itself an instance of order-2-instrument blindness (§16.3). Certs: `f4_packet_cc_defA.py` (+ `f4_packet_cc_defA_audit.py`), `f4_packet_cc_defB.py` (project root; numpy/sympy; exit 0).

**Remark 16.4a (The negative sharpens the contribution boundary). [observed here].** Because the "6" is provably *not* a packet-intrinsic central charge, it is unambiguously the division-algebra ladder gap $\dim_{\mathbb R}\mathbb O-\dim_{\mathbb R}\mathbb C$ — a *string-side* identity. The division of labor is therefore clean and firewall-aligned: **string theory owns the dimension/central-charge numerics; the program owns the order-of-derivation organizing principle; they meet at "the internal datum is order-3."** Refusing to smuggle a magic 6 into the packet combinatorics where the arithmetic does not put it is the same discipline as §12 — the firewall applied to a tempting cross-theory number.

### 16.5 Firewall binding and open levers

**Firewall paragraph (binding, parallel to §11.3 and §13.1).** The framework does **not** derive string theory, the critical dimensions $10/11/26$, supersymmetry, Calabi–Yau geometry, the string coupling, or the landscape. Connection F is a structural analogy at the level of order-of-derivation, bound by Principle 12.1: the only quantities it touches — the central charge $c$, the rung dimensions, the gap $6$, the packet $c=1$ — are **pure numbers** or settled-negative welds, never dimensionful magnitudes; $\alpha'$, the string scale, and $g_s$ are out of scope by §12. Every claim above carries its tier and firewall status per §13.3. The honest packet-$\hat c$ negative (§16.4) is part of the contribution: it draws the boundary between what the program supplies (order structure) and what string theory supplies (the dimension numerics) sharply enough that the cohabitation cannot be mistaken for a derivation.

**Open levers (status after the two verification pushes).**
1. **The map $\Phi\to F$ — partially discharged.** The curvature *identity* $R=\mathrm{AN}$ is now $[P]$ and exact (Remark 16.2b); the explicit *global* potential map fails — $\log Z$ is a log-sum-exp Hessian while a special-geometry/VSR prepotential is a $-\log$-cubic Hessian, *different convexity classes* — so a coordinate map $\Phi\to F$ does **not** exist globally. What survives is the centroid identification plus the named obstruction (the jerk). Remaining open: whether a *jet-local* (centroid) map suffices for any string-side purpose.
2. **The integrability fork — discharged (Remark 16.2b).** The program's $(g,T)$ *does* satisfy the special-geometry curvature form $R=-gg-gg+\lambda\,T\!\cdot\!T$ — exactly at the centroid (the constant-curvature sphere, $K=\tfrac14$) — and fails off it precisely because the cubic flows ($T^{(4)}\neq0$). The fork resolved to "yes at the centroid, no globally, obstruction $=$ jerk."
3. **The equal-$c$ exhibit — discharged to $[A]$ (§16.3a).** Supplied: Kanazawa's Picard-rank-1 $X_5,X_{25}$ at $(1,51)$, degree $5$ vs $25$, non-diffeomorphic by Wall; the Rødland double-mirror trap explicitly declined.
4. **The one genuinely open step (new).** Upgrade the SCFT-order reading "smallest distinguishing correlator order $=3$" from $[A]$ to $[P]$ for the rank-1 exhibit by identifying the *normalized* genus-0 three-point function with the integral datum $H^3$ without operator-normalization ambiguity — or use a Picard-rank-$>1$ pair (e.g. the $(2,46)$ generalized CICY of Anderson–Apruzzi–Gao–Gray–Lee, arXiv:1507.03235, where the basis-invariant cubic-form inequivalence is manifest) as the secondary illustration.

---

## Conclusion

The series spent Papers 28–31 guarding the gravity question. This paper shows the guardrails were guarding a *result*. One functional, $\Phi=\log Z$ — derived in Paper 54 as the generating function of the completely passive states — is the categorical effective action; its cumulant derivatives are the objects physics separates only because it assumes a manifold. Space is mass (second cumulant) as an equilibrium identity, the static FDT; time and energy are the time-translation generator, and its closure failure — read as gravity only conjecturally — is, on $\mathbb{Z}/6\mathbb{Z}$, exactly and arithmetically the conductor-6 carry, with stability identical to Weil positivity at the $P_2$ row, and one congruence ($3{+}3{+}3\equiv3\not\equiv0$) is the common root of four independent corpus results. An inertial projector, as defined, closes in exactly one row, spatial dimension three — the restatement of "angular momentum is a vector iff $n=3$". The Poincaré–Cartan form carries the contact sign of extended phase space, present in every dimension, and the classical dispersion is Galilean; Lorentzian signature is settled, on this row, as *manifold-level Euclidean-4 with a local-tangent Lorentzian sub-bundle on $V$* — the pre-claimed branch, realized. Given the $2+3$ split and the representation $\Lambda^2E\oplus E^*$, the textbook $SU(5)$ values follow — the tree-level Weinberg angle $3/8$ and the SM hypercharge spectrum [A] — alongside the color-confinement signature, all fenced by a firewall principle that forbids any dimensionful magnitude. Gravity is still not claimed. The derived functional and its equilibrium identity, the arithmetic localization of the closure residual, and the lift status of signature are.

**Data availability.** All $[P]$ results follow from Papers 13 and 17 as cited and require no new data. The three finite audits of §14 are fully specified on the Paper 14 exact integrator; §14.2 has been run (transcript archived under `empirical/`).

---

## References (curated, peer-reviewed)

Cited as *anchors and precedents*, not as adopted ontology (§13.1).

1. J. Zhang and H. Li, *Symplectic and Kähler structures on statistical manifolds induced from divergence functions*, Geometric Science of Information (2013). (§2.2, §8.2a)
2. J.-M. Souriau, *Structure des systèmes dynamiques* — Lie-group thermodynamics, moment map, symplectic-cohomology cocycle. (§3.2, §4)
3. F. Barbaresco, *Lie group thermodynamics and Koszul–Souriau–Fisher metric* (Les Houches / SPIGL) — capacity $=$ Fisher $=$ Hessian-of-Massieu identity; the cocycle $\theta(g)$. (§3.2, §14.3)
4. C.-M. Marle, on the Souriau moment map and the symplectic cocycle — §14.3 formulation.
5. A. Connes and C. Rovelli, *Von Neumann algebra automorphisms and time–thermodynamics relation in generally covariant quantum theories* (1994) — Tomita–Takesaki modular flow / thermal time, [C-support] precedent only. (§9.2)
6. T. Jacobson, *Thermodynamics of spacetime: the Einstein equation of state* (1995); the Padmanabhan and Verlinde emergent-gravity programs — the external lineage §13.1 positions *against* at the level of claim strength.
7. Paper 54, *The One Functional, Derived* (`54_one_functional_from_passivity.md`) — the derivation of $\Phi$ from complete passivity, the static FDT as the content of Theorem 3.1, its non-equilibrium failure, and the Bekenstein bound from passivity. (§1.1, §2, §3, §4.A)
8. H. Shima, *The Geometry of Hessian Structures*, World Scientific (2007); S. Amari and H. Nagaoka, *Methods of Information Geometry*, AMS (2000) — the curvature identity $R=\mathrm{AN}(T)$ of Hessian metrics. (Rem 16.2b)
9. H. Georgi and S. L. Glashow, *Unity of all elementary-particle forces*, Phys. Rev. Lett. **32** (1974) 438 — the $SU(5)$ value $\sin^2\theta_W=3/8$. (§10.3)

---

## Appendix A. The T-series substrate, compressed

A parallel program of T-series preprints (T0–T14) promotes the $\mathbb Z/6$ computation of §5 from a worked instance to an instance of general theorems. The load-bearing anchors:

| T-paper | General theorem | What it promotes in Paper 32 |
|---|---|---|
| **T7** | Apex / Bures lift; Born $=$ toric moment map; Kummer cover & deck groups | §2.2 lift; §11.1 spin/color/chirality decks; §9 the complex structure |
| **T11** | Apex Vertex Calculus: the Apex Feynman rule generalizes Lemma 5.1a to all $n$; conductor fusion prime-localizes Cor. 5.1d; *every projected simplex theory leaks exactly through its conductor-fusion boundary* | Theorem 5.2 is the $\partial_3\{2,3\}=\{6\}$ instance of fusion-boundary universality, not a $\mathbb Z/6$ coincidence |
| **T12** | Finite Apex Determinacy: the apex tower $\cong\mathbb R[t]/(P_x)$; the order/tensor axis is closed | T11+T12 $=$ a totally finite arithmetic perturbation theory |
| **T13** | Exact Simplicial Renormalization: the closure operator $\operatorname{Cl}_n$ on the packet lattice has the exactly-renormalizable sectors as fixed points | Theorem 5.2 promoted from a Fourier calculation to a finite renormalization theorem; couplings run exactly when projection crosses a conductor-fusion boundary |
| **T14** | Projected Flatness & Curvature Linearization: projected curvature $=$ projection noncommutation $=$ boundary leakage $=$ RG source $=$ Noether defect $=$ beta source (one finite object, six languages); support is exactly $\partial_n S$, sharp | Remark 4.2 (gravity-as-closure-defect $=$ projected curvature, $[P]$); Theorem 12.1 (the firewall extends to curvature) |

The net structural statement: **T11+T12+T13+T14 close all four structural axes — character/conductor, order/tensor, projection/RG, geometry/curvature — so the framework has no algebraically free degrees of freedom beyond the conductor lattice, the packet decomposition, the closure operator, and the apex closure polynomial.** This is the substrate behind the firewall principle (§12): a quantity determined by these finite combinatorial gadgets cannot carry a unit.

## Appendix B. Higher-row worked examples

The structural facts of §10–§11 extend up the primorial-and-depth hierarchy $\mathbb Z/6<\mathbb Z/12<\mathbb Z/18<\mathbb Z/30$, all preserving $\sin^2\theta_W^{\text{tree}}=3/8$. Headline results (each $[P,\text{computed}]$ unless noted):

| Row | Type | Key structure | $\sin^2\theta_W^{\text{tree}}$ |
|---|---|---|---|
| $\mathbb Z/6=2\cdot3$ | base mixed primorial | $E=\mathbb C^2\oplus\mathbb C^3$; $\mathbf{10}\oplus\bar{\mathbf 5}$ of $SU(5)$; the §5 certificate | $3/8$ |
| $\mathbb Z/12=2^2\cdot3$ | EW/Higgs depth | depth-2 on prime 2; new packet $H_4$; Kummer-deck scaling SM-Z/6 at $m=N/6$ | $3/8$ (invariant under depth) |
| $\mathbb Z/18=2\cdot3^2$ | QCD/confinement depth | depth-2 on prime 3; new packet $H_9$ | $3/8$ |
| $\mathbb Z/24=2^3\cdot3$ | deeper EW depth | depth-3 on prime 2; packet $H_8$; $(\mathbb Z/24)^\times=(\mathbb Z/2)^3$ (unique three-parity); cubic-gauge Kummer deck $\mathbb Z/8=$ **Bott period** (KO-dim-6 locus) | $3/8$ |
| $\mathbb Z/30=2\cdot3\cdot5$ | GUT-scale row | $F_{30}$ dim 55; $SU(5)$ decuplet; three-way trace coincidence $T_2=T_3=T_5=9/2$ | $3/8$ |

Two further $[A,\text{structural}]$ recognitions: the framework is the NCG-lineage *arithmetic cousin* of string-theoretic SM unification (Bott $\mathbb Z/8\leftrightarrow$ D-brane KO-charges; Kummer decks $\leftrightarrow$ orbifold quotients; $\Lambda^2 E\oplus E^*\leftrightarrow\mathbf{10}\oplus\bar{\mathbf 5}$) — sharing the *algebraic skeleton*, not continuous-geometric content; and the quartic-order structure (the order axis, §5 extended to $n=4$) shows $A_2$ is cubically isolated but *quartically self-coupling*, with five fusion-closed sub-theories at $\mathbb Z/6$ and universal leakage support $\partial_n V=\{6\}$ for all $n\ge3$.

## Appendix C. Reproducibility — the instrumented run (Figure 1)

The depth and Souriau-cocycle audits of §14 are realized as one pre-registered instrumented run on the Paper 14 exact 5-dimensional integrator.

- **C.1 Substrate.** Exact integrator on $\Delta_6^\circ$, character coordinates $\chi_1,\dots,\chi_5$; centroid start $p_*$; energy $\mathcal E_3$ conserved upstairs to machine precision (the floor control defining every "zero").
- **C.2 The three instrumented observables (panels a–c):** (a) the projected energy non-conservation $\tfrac{d}{dt}\mathcal E_3|_{\Pi_\tau}$, predicted by Theorem 5.2 to live entirely on $\{\chi_1,\chi_5\}$; (b) the conductor-6 residual norm $\|R^{\Pi_\tau}\|$, predicted bounded; (c) the conductor-6 Noether form, predicted sign-definite (Theorem 7.1).
- **C.3 Depth overlay (panel d, §14.1):** repeat under $\mathbb Z/6\hookrightarrow\mathbb Z/12,\mathbb Z/18$; verdict inequality — the residual stays on the squarefree conductor-6 mode, bounded and sign-definite.
- **C.4 Souriau read-out (panel-d inset, §14.3):** the moment-map non-equivariance cocycle, tested for nontriviality on conductor 6.
- **C.5 Mandatory controls:** an $A_2\oplus A_3$-confined initial condition must show *zero* residual (localization control); a centroid-fixing state-side reduction must leave $M$ invariant (the §2.3 Heisenberg-picture control).
- **C.6 The single pre-registered verdict:** the run passes iff (a) localizes on $\{\chi_1,\chi_5\}$, (b) is bounded, (c) is sign-definite, and the controls return zero. Any failure refutes the corresponding falsifier of §15.1.

---

*Draft 0.4 (2026-10-01): Phase-2 relabels from Paper 54 (ledger in the internal log at the top). Consolidated draft 0.3 (2026-06-08): reorganized from the append-only v0.2.5 into a single clean statement; version archaeology and the §12 priority ledger externalized to `Paper32-worklog.md`; all $[P]$ math preserved verbatim; the §14.2 Bures-dispersion audit reflected as settled (Euclidean-4 manifold + local-Lorentzian sub-bundle).*

