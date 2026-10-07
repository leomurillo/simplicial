# N11 — The Capstone: One Wall, Mapped. The Apex/Cubic Reduction of the Riemann Hypothesis to Archimedean Spectral Realization

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*June 6, 2026*

<!--
Program record. N11 is the capstone consolidation of the apex/cubic program's assault on RH. It does
NOT prove RH and does not claim to. It assembles, into one honestly-tiered document, the genuine
deposits — the multiplicative skeleton (N9), the geometric reduction and its signature ceiling (N10),
the CBS<->RH operator unification, and the explicit operator-build (deficiency/normality, tasks 1-2) —
around the spine that organizes them all: conservation of difficulty. Every independent route reduces
RH to the SAME wall, the archimedean spectral realization (Connes-Consani), and N11's contribution is
that it maps to that wall more sharply than the program has before, builds the explicit operator the
wall concerns, and CLOSES several tempting shortcuts concretely. Certificates (empirical/):
probe_fusion_closure_nogo.py (N9), probe_cayley_menger_hamiltonian.py + probe_complexified_cone_signature.py
(N10), probe_debranges_cbs_predictor.py + apex_recovery/ E1-E16 (CBS), probe_apex_operator_normality.py
(task 1), probe_hp_deficiency_indices.py (task 2), and the adversarial convergence map.
Discipline throughout: structural reduction (real) is separated from proof of RH (not achieved).
-->

---

## Abstract

We consolidate the apex/cubic program's reduction of the Riemann Hypothesis. The Hypothesis is equivalent, unconditionally, to the de Branges/Herglotz positivity of $m_B=-\Xi'/\Xi$ (equivalently $E_B=\Xi+i\Xi'$ Hermite–Biehler, equivalently the assembled Weil form's marginal positivity). The program reduces this from four independent directions — multiplicative, geometric, dynamical/operator, and information-geometric — and we prove that all four terminate at one wall: the **archimedean spectral realization**, the construction over $\mathbb Q$ of the fixed self-dual positive object that Weil's surface supplies for free over a function field. We record the genuine, certified deposits: (i) **multiplicative** — cross-prime multiplicativity (the Euler product) is the exact invariant separating the RH-respecting class from the Davenport–Heilbronn counterexamples, discharging them as a No-Go (N9); (ii) **geometric** — the de Branges Pick kernel *is* the resolvent Gram of the divisor Hilbert space, free positivity holds on the critical line but the off-axis Hermitian Gram is a generalized-Nevanlinna kernel whose negative index equals the number of off-line zeros, so it carries **no fixed Hodge signature** (N10); (iii) **operator** — the apex–archimedean operator is **non-normal**, its non-normality carried entirely by the archimedean phase $e^{i\pi s/2}=\sqrt i$, so the arrow of time and the archimedean place are one object; and its self-adjoint-extension freedom is a $U(1)$ phase that only shifts an arithmetic ladder, hence cannot encode the zeros' (Weyl-)increasing density (tasks 1–2); (iv) **information-geometric** — the de Branges block $\Xi+i\Xi'$ is exactly the CBS predictor block $S+A$, so the arrow is $\Xi'$, the symmetric/quadratic positivity instruments are blind to it by parity, and the de Bruijn–Newman constant $\Lambda$ (Rodgers–Tao: $\Lambda\ge0$; RH $\iff\Lambda\le0$) is the dynamical form of the same wall. We close, concretely, the tempting shortcuts — a cubic-Gram floor, an RG fixed point, a Li/operator-square positivity, a curvature-domination bound, a Kähler lift, a chart split, and a boundary-condition extension — each by exhibiting the precise step where a free finite/on-axis object is conflated with the RH-bearing infinite/off-axis one. The net is a sharp, exactly-localized reduction-and-ceiling: **structural reduction — real; proof of RH — not achieved.**

**MSC 2020:** 11M26, 11M41, 46E22, 47B25, 47B32, 11F66, 62B11.

---

## 1. The one wall

Write $\Xi(z)=\xi(\tfrac12+iz)$, $E_B(z)=\Xi(z)+i\Xi'(z)$, $m_B(z)=-\Xi'(z)/\Xi(z)$, $P_B(z,w)=\dfrac{m_B(z)-\overline{m_B(w)}}{z-\overline w}$.

**The reduction chain (unconditional).** $\ \mathrm{RH}\iff E_B\ \text{Hermite–Biehler}\iff m_B\ \text{Herglotz}\iff P_B\succeq0\iff\varphi'(x)\ge0\ (\text{monotone clock})\iff$ the assembled Weil form is positive semidefinite in the archimedean limit. Each link is classical or proved in the program (N0, N5–N7).

**The meta-theorem (conservation of difficulty) $\mathsf{[A]}$.** *Every route the program constructs to the positivity above reduces, at its closure point, to one object — the archimedean spectral realization: a fixed self-dual positive (Hermitian/operator) structure over $\mathbb Q$ whose collapse locus is the zeros. Over a function field this object exists (Weil's surface $C\times C$ with its fixed-signature Hodge intersection form and Frobenius); over $\mathbb Q$ it is the missing $\mathbb F_1$ self-product, and its construction is open.* The remainder of N11 is the proof of this organizing claim, route by route, together with the genuine partial structure each route deposits.

The discipline of the program is to keep the two halves apart: the reduction is exact and the wall is sharply named; the wall is not breached.

---

## 2. The multiplicative route: cross-prime fusion (N9) $\mathsf{[P]}+\mathsf{[A]}$

A functional equation does not imply RH: the Davenport–Heilbronn family $f=\tfrac{1-i\kappa}2L(s,\chi)+\tfrac{1+i\kappa}2L(s,\overline\chi)$ ($\chi$ order-4 mod 5) has a functional equation yet zeros off the line. The exact invariant the counterexamples violate is **cross-prime multiplicativity**.

**Theorem 2.1 $\mathsf{[P]}$.** *Cross-prime fusion closure ($a_{mn}=a_ma_n$, coprime $m,n$ $\iff$ Euler product) separates the classes: $\zeta$ and every primitive Dirichlet $L$ have defect $0$ exactly; Davenport–Heilbronn has defect $\ge1$. The order-three vertex adds nothing beyond order two (multiplicativity is pairwise-generated).* (Certified `probe_fusion_closure_nogo.py`.)

**Corollary 2.2 (the No-Go) $\mathsf{[P]}$.** The functional equation is strictly weaker than fusion closure; DH is discharged (it is not fusion-closed, hence not a counterexample to "fusion-closed $\Rightarrow$ RH").

**Proposition 2.3 $\mathsf{[A]}$.** Fusion closure is the tensor/Euler factorization $H=\bigotimes_p H_p$ — the multiplicative skeleton. It is **necessary** for RH but **not sufficient**: the fusion-closed class is the Selberg class, for which RH is open. The residue is archimedean (§6).

---

## 3. The geometric route: Bures–Cayley and the signature ceiling (N10) $\mathsf{[P]}+\mathsf{[A]}$

$\mathbb Z/6$ is the six-edge coordinate system of the $N=4$ tetrahedron; the Cayley–Menger determinant $\Delta_{\mathrm{CM}}=288V^2$ is a cubic in the squared edges (the geometric twin of the Amari–Chentsov cubic); the zeros of $\Xi$ are the simplex degenerations.

**Theorem 3.1 (Pick $=$ resolvent Gram) $\mathsf{[P]}$.** *$P_B(z,w)=\sum_\gamma m_\gamma/((\gamma-z)(\gamma-\overline w))=\langle R_z,R_w\rangle$ in $L^2(\mathrm{div}\,\Xi)$; hence $P_B\succeq0\iff$ positive divisor measure $\iff$ RH.* (Certified to $3\times10^{-16}$.)

**Theorem 3.2 (on-axis free / off-axis RH) $\mathsf{[P]}$.** *On the critical line the Bures edges are real and cone membership $\Delta_{\mathrm{CM}}\ge0$ is automatic (Bures is a genuine metric); off the line the edge-squares are complex and cone membership reduces exactly to Pick positivity.*

**Theorem 3.3 (the signature ceiling) $\mathsf{[P]}$.** *The Hermitian Bures–Cayley/Pick Gram is a generalized-Nevanlinna (Kreĭn–Langer) kernel whose number of negative squares equals the number of zeros off the critical line:*
$$\kappa(P_B)=\#\{\text{zeros of }\Xi,\ \operatorname{Im}>0\}.$$
*Hence it has no fixed Hodge signature — its signature is the very count RH asks about, and $\kappa=0\iff$ RH.* (Certified `probe_complexified_cone_signature.py`: $\#$negative eigenvalues $=\#$injected off-line zeros, exactly.)

**Proposition 3.4 (why the $\mathbb F_q$ Hodge index does not lift) $\mathsf{[A]}$.** The Castelnuovo–Hodge forcing needs a *fixed* surface with a *fixed* signature and a *finite-rank* Frobenius class. The number-field substitute fails all three: the Bures–Cayley "surface" is $z$-parameterized (no fixed signature), the apex–archimedean spectrum is continuous (no finite class), and the only fixed-signature object is the on-axis real Gram (Thm 3.2). One obstruction: the missing $\mathbb F_1$ self-product.

---

## 4. The information-geometric route: the arrow and the right instrument (CBS$\leftrightarrow$RH) $\mathsf{[P]}+\mathsf{[A]}$

The de Branges object decomposes as a transition operator's symmetric-plus-antisymmetric split.

**Theorem 4.1 (de Branges block $=$ predictor block) $\mathsf{[P]}$.** *$E_B=\Xi+i\Xi'$ is the CBS predictor block $B=\Xi\cdot I+\Xi'\cdot J$: the even $\Xi$ is the symmetric part $S$, the odd $\Xi'$ is the antisymmetric part $A$ — the current, the arrow of time. The quadratic form sees only $\Xi$ ($v^\top Bv=\Xi\|v\|^2$, with $\Xi'$ in its kernel); the functional equation $s\leftrightarrow1-s$ is the time-reversal $T\leftrightarrow T^{*}$. RH $\iff m_B=-\Xi'/\Xi$ Herglotz $\iff$ the arrow is correctly phased everywhere.* (Certified `probe_debranges_cbs_predictor.py` to $10^{-32}$.)

**Corollary 4.2 (why symmetric positivity is blind) $\mathsf{[P]}$.** Every quadratic/Hankel/Bombieri-type Weil form is a functional of $S$ alone ($\langle h,Ah\rangle=0$ for real $h$); the arrow $\Xi'$ lies in its kernel. The instrument that sees it is the **predictor** (two-chart SVD), not a single symmetric form. This is the structural reason the program's quadratic-positivity attempts could not reach RH.

**Theorem 4.3 (the dynamical form) $\mathsf{[A]}$.** The program's stability constant is the **de Bruijn–Newman** $\Lambda$. Rodgers–Tao proved $\Lambda\ge0$ (the zeros sit *barely* on the attractor — Newman's "if true, only barely"); RH $\iff\Lambda\le0$. The unconditional Fan–Hoffman gap $\Delta=\sum\sigma_i(T)-\sum\lambda_i(S)\ge0$ reproduces the Hasse–Weil bound over $\mathbb F_q$ (finite operator) but is pointwise-trivial for $\zeta$ (infinite); the missing half $\Lambda\le0$ is the archimedean wall.

---

## 5. The operator route: the explicit apex–archimedean operator (tasks 1–2) $\mathsf{[P]}+\mathsf{[A]}$

The apex edge operator $\mathcal U=(A-I)\Phi$ (N4–N5) has Mellin symbol $\widetilde k(s)=\tfrac{s}{1-s}(2\pi)^{-s}e^{i\pi s/2}\Gamma(s)$ and is identified with the Connes–Consani archimedean operator.

**Theorem 5.1 (non-normality $=$ the archimedean phase) $\mathsf{[P]}$.** *$\mathcal U=M_{\widetilde k}\circ R$ is **non-normal**: $|\widetilde k(\tfrac12-it)|/|\widetilde k(\tfrac12+it)|=e^{\pi t}$ exactly, so $[\mathcal U,\mathcal U^*]\neq0$. Removing the archimedean phase $e^{i\pi s/2}$ makes the modulus even (normal); the entire non-normality is the archimedean $i^s$ phase, the N4 threshold $\sqrt i=\tfrac18$.* Hence **the arrow (the antisymmetric/non-normal part) is the archimedean phase** — the object the symmetric instrument cannot see and the object at the place at infinity coincide. (Certified `probe_apex_operator_normality.py`.)

**Theorem 5.2 (deficiency indices) $\mathsf{[P]}$.** *The Hilbert–Pólya dilation generator $D=-i(x\partial_x+\tfrac12)$ on $L^2(\mathbb R_+)$ has deficiency indices $(0,0)$ — essentially self-adjoint, with continuous spectrum. Its Connes-type cutoff has indices $(1,1)$: a $U(1)$ family of self-adjoint extensions with eigenvalues $(2\pi n+\theta)/L$ — an arithmetic progression. No extension tracks the zeros: their density grows like $\tfrac1{2\pi}\log\tfrac\gamma{2\pi}$, while a boundary phase only shifts a constant-spacing ladder.* (Certified `probe_hp_deficiency_indices.py`: best arithmetic fit residual large; gaps shrink, Weyl density grows.)

**Corollary 5.3 (two shortcuts closed) $\mathsf{[A]}$.** The self-adjoint-extension freedom is the *wrong knob* — the zeros' density is a **potential** effect (the archimedean $\Gamma$-curvature / the Weyl law), not a boundary condition. Combined with §4: the HP operator's *arrow* (Thm 5.1) and its spectral *density* (Thm 5.2) both live in the archimedean potential; neither the non-normality nor the extension freedom is a lever.

---

## 6. Conservation of difficulty: the closed shortcuts $\mathsf{[A]}$

Each independent attempt produces a positivity that is *free* on a finite/on-axis/multiplicative object and conflates it with the RH-bearing infinite/off-axis/archimedean object. We record the precise conflation in each, all certified:

| route | the free object | the RH object | the conflation |
|---|---|---|---|
| cubic Gram floor | $G^{(3)}$ well-conditioned (Parseval-equiv.) | the marginal Weil edge | bulk trace vs edge gap |
| RG fixed point | the completion exists (functional eq.) | $\Lambda\le0$ (stability) | existence vs stability |
| Li / operator-square | even moment $\int S_g^{2k}\eta\ge0$ (vacuous) | $\lambda_n\ge0$ (the cumulant) | definite $\Leftrightarrow$ vacuous (tower thm) |
| curvature-domination | unitary transfer preserves the load (Parseval) | $r_k<1$ (the bound) | unitary $\neq$ small |
| Kähler / linear lift | $C^\dagger C\succeq0$ (always) | the Pick kernel | lift Gram $\neq P_B$ off-axis |
| chart split (geometry) | real Schoenberg Gram, fixed sig. | off-axis Hermitian Gram | $z$-parameterized, $\kappa=\#$off-line |
| boundary phase (operator) | $(1,1)$ extension ladder | the zeros' Weyl density | boundary vs potential |

**Proposition 6.1 (the tower theorem) $\mathsf{[P]}$.** Over $\mathbb Q$, at every cumulant order $m\ge2$: definite $\iff$ vacuous, contentful $\iff$ indefinite. The even moments are definite-but-vacuous; the connected cumulants are indefinite (odd by parity at $m=3$; Wick-subtracted at $m=4$, the program's own certified selection rule). The unique exception is order-2 over $\mathbb F_q$, where the Hodge form is both definite and RH-encoding — because the surface exists.

**Proposition 6.2 (local $\neq$ global) $\mathsf{[A]}$.** On the Fermat cubic, $|J_p|=\sqrt p$ holds for all $p$ unconditionally (Hasse, the local geometric forcing), yet GRH for its $L$-function is open. Local multiplicative positivity does not assemble to global RH; the gap is the archimedean place.

These are not seven failures; they are one theorem with seven proofs. Each free object is a *shadow* of the archimedean object, exact only where the surface (function field) or the critical line (on-axis) supplies it for free.

**The second wave: the information-theoretic sweep (2026-06) $\mathsf{[P]}+\mathsf{[A]}$.** The seven routes above are positivity-from-geometry/operator shortcuts. A later sweep tested the *information-theoretic* and *convergence* reformulations — the relative-entropy frame (N14–N15), its convex duality, and the spectral-limit tightness — each proposing a domination of the prime term $P$ by the archimedean term $A$. Each is closed by the same conservation, now in the entropy register; all are certified (`empirical/p_infinity/`). This subsection records them so they are not re-proposed.

| proposed lever | tested as | why it fails | reduces to |
|---|---|---|---|
| tightness / escape-of-mass (positivity survives the high-freq limit) | `probe_highfreq_accumulation` | unfolded marginality is scale-invariant (GUE-universal) — no comfortable regime (§7) | uniform-in-height repulsion |
| entropy / difference-of-convex domination | `probe_toland_dual_signpreserving` (N15) | the Toland–Singer dual is an exact **sign-preserving** identity — it cannot manufacture positivity | the conjugate swap, no slack |
| monotone / Petz–DPI domination | `probe_obligation73_*` (N14) | the DPI defect is **phase-blind** ($|U_p|^2$ discards $\arg U_p$) and **reversible-transfer-blind** ($\tau_n=(-1)^n\Rightarrow$ defect $\equiv0$) — delivers the even/metric half, structurally misses the chiral phase | the chiral object $C(\rho)=\operatorname{Im}\rho_\chi$ |
| uniform convex barrier (a floor held off $0$) | `probe_toland_barrier_margin` (N15) | the margin collapses $1.5\times10^{-3}\to10^{-11}$ across $\tau=1$; $\kappa>1$ drives it strongly negative; a held floor $=$ no-Siegel-zero, **weaker** than RH | no free floor |
| variance / second-moment tightness signature | `probe_individual_pair_repulsion`, `probe_prime_variance_X_sweep` | the Montgomery–Soundararajan short-interval excess **flips sign with $X$** — fluctuation, not a residual | the analytic level of distribution $\theta$ |
| chiral margin / step (a) (even-beats-odd) | `probe_obligation73_genuine_chiral_audit` | $C(\rho)$ locates RH exactly, but its definite sign **is** $L(\tfrac12,\chi_3)\ne0$ — supplying it from $\chi_3$ is a forced match (it belongs to $\mathrm{GRH}(\chi_3)$, not to $\zeta$) | arithmetic input $=$ RH |

**Proposition 6.3 (the second wave has one residual) $\mathsf{[A]}$.** *Every reformulation above reduces, non-circularly, to a single analytic statement: the uniform individual GUE repulsion at every height — equivalently the uniform level of distribution $\theta$ of the primes on primorial moduli in the Bombieri–Vinogradov range. The unconditional frontier is $\theta_0\approx0.515$ (trilinear Kloosterman: Wright; Fouvry–Radziwiłł; Bettin–Chandee), discharging bounded $n$; Pascadi's $c^{-1/12}$ primorial saving lifts this to $\theta_0\le 6/11\approx0.545$ ($\mathsf{[A]}$, pending the standard dispersion bookkeeping); the open target is $\theta\to1$ (Elliott–Halberstam strength), which is RH-bearing.* This is the **same wall** as §7 — the archimedean energy contraction $\rho_E\le1$ — now reached from the information-geometric side and handed to the one analytic frontier that carries live external machinery. $\mathsf{[P]}$ the six kills (certified); $\mathsf{[A]}$ the reduction to uniform $\theta$; the closure $\theta\to1$ is RH ($\mathsf{[C]}$). (The retracted figure $\theta_0(5)\approx0.538$ of an earlier Paper-43 draft was an unsupported midpoint — no cited result yields it; the honest levels are $\tfrac12$, $0.515$, $6/11$ above.)

These are not six further failures. The entropy dual is *sign-preserving*, the monotone is *phase-blind*, the barrier is *marginal*, the variance signature is a *fluctuation*, the chiral object *locates but does not supply* — each the §6 conflation continued into the information-theoretic register, a shadow of the archimedean object exact precisely where it carries no RH content. The lesson is structural and now durable across **two waves**: no reformulation — geometric (§6) or information-theoretic (§6.3) — closes the wall; effort is correctly spent only on the residual itself, the uniform level of distribution / the $\mathbb F_1$ self-product (§7).

---

## 7. The wall, named exactly $\mathsf{[C]}$

All routes terminate at the **archimedean spectral realization**:

> *There exists a fixed self-dual positive object over $\mathbb Q$ — equivalently a fixed-signature Hermitian form on a fixed arithmetic surface; equivalently a self-adjoint operator with a confining archimedean potential whose discrete spectrum is the zeros; equivalently the off-axis positivity $P_B\succeq0$ proved without assuming the edges real — whose positivity is as automatic as a Euclidean volume yet whose collapse locus is the zeros.*

Over a function field this is Weil's theorem (the surface, the fixed Hodge signature, Frobenius). Over $\mathbb Q$ it is the missing $\mathbb F_1$ self-product / the Connes–Consani archimedean positivity, and it is **open**. The program contributes: the explicit operator whose arrow ($\Xi'=$ the archimedean phase $\sqrt i$, Thm 5.1) and spectral density (the archimedean potential, Thm 5.2) the realization must reconcile; the precise instrument (the predictor / two-chart SVD, Thm 4.1); and the proof that no finite, multiplicative, on-axis, or boundary-condition structure supplies it (§6). What would breach the wall is the construction of the fixed-signature object itself — not a reformulation, of which seven are now closed.

**Forward door (the fusion-contingent metric) $\mathsf{[C]}$.** Every reformulation closed in §6 is *fusion-blind*: it uses only data the Davenport–Heilbronn function $f_{\mathrm{DH}}$ shares with $\Xi$ — functional equation, order, the archimedean $\Gamma$-factor — and so cannot distinguish them, yet $f_{\mathrm{DH}}$ has off-line zeros (§2). The one direction the closed routes do not touch is therefore the one that is at once **fusion-sighted** and **archimedean**: that the apex metric $\eta$ — the de Branges/divisor inner product in which $P_B$ is the resolvent Gram (Thm 3.1), equivalently the positive metric that resolves the non-normal $\sqrt i$ of $\mathcal U$ into real spectrum (Thm 5.1) — is positive on the cross-prime-fusion-closed sector, with the positivity necessarily fusion-dependent (it fails for $f_{\mathrm{DH}}$, whose Gram carries $\kappa=\#$off-line zeros, Thm 3.3). This is [N9] Conjecture 5.4. It is equivalent to the archimedean realization above (hence $\mathsf{[C]}$, open), but it is the *correctly-shaped* form: alone among the residue's phrasings it makes the resolution of $\sqrt i$ contingent on the Euler product, so the Davenport–Heilbronn No-Go (§2) does not already refute it. Breaching the wall along this door means proving the metric positive by an argument that is essentially multiplicative — fusing the cross-prime skeleton (§2) with the archimedean operator (§5).

**Update (exact-frame consolidation) $\mathsf{[P]}$.** Three would-be components of the wall are now discharged exactly in the metric-adjusted frame (signature, not conditioning), narrowing the residue to the archimedean transcendental alone. The super-exponential *marginality* is a floating-frame artifact — the exact signature is robust ([N5], Rem. 8.1). The *fusion* defect separating $\zeta$ from Davenport–Heilbronn is an exact finite signature ([N9], Rem. 5.5). The archimedean phase $\sqrt i$ is an exact cyclotomic integer rotation, absorbed into the prime-$2$ metric exactly as $M=4I-J$ absorbs $\sqrt3$ in the rotor calculus ([N4], Rem. 4.3). All three are Sylvester-separated from the open positivity, whose only non-exact input is the transcendental zeros / $\Gamma$-envelope. The wall is unbreached and now contains nothing algebraic: the residue is purely the archimedean transcendental positivity. (Certified `empirical/probe_exact_signature_dispels_marginality.py`, `probe_helmert_fourier_fusion_metric.py`, `probe_sqrt_i_absorption.py`.) Equivalently, the obstruction is classified by metric type ([N5], Rem. 8.2): the $\sqrt i$ skin is metric-removable, a defective core (a multiple zero) is excluded by zero-simplicity, and RH $\iff$ there is no genuine-drift core — no off-line (complex) eigenvalue.

**Update (the energy-condition chain — symmetry vs inequality, resolved by frequency) $\mathsf{[P]}+\mathsf{[A]}$.** A prime-side decomposition of the assembled Weil form $W=A-P$ — $A=$ pole $+$ archimedean $\Gamma$-factor, $P=$ the prime oscillation — splits the wall into a *symmetry* half and an *inequality* half, and locates the residue by frequency. Seven certified probes (`empirical/p_infinity/`).

- *(Convergence — apex$\to$archimedean from the primes alone, $\mathsf{[P]}$.)* $W^{\mathrm{ef}}(P)\to W^{\mathrm{zero}}$ to $10^{-10}$ by $P=50$ primes; $\lambda_{\min}\to+9.3\times10^{-7}$. The completion is fast; the difficulty is not the convergence but the *marginal* residual. (`probe_apex_archimedean_convergence.py`.)
- *(The FE gives equality, not a bound, $\mathsf{[A]}$.)* Along the critical direction $v$ the functional equation forces the archimedean mean and the prime defect to *coincide*: $v^\top Pv/v^\top Av=1-3.4\times10^{-6}$, a $99.9997\%$ cancellation. An involution delivers the *balance* $v^\top Av=v^\top Pv$ but cannot sign the residual; the operator-norm and $L^2$ defect bounds both fail ($\lambda_{\min}(A)-\lambda_{\max}(P)=-0.10$). RH needs an *inequality*, which a symmetry cannot supply — the sharp reason the FE is strictly weaker than RH (§2). (`probe_selfduality_mean_minus_defect.py`.)
- *(Order-2 complete; the order-3 channel is empty for $\zeta$, $\mathsf{[P]}$.)* The off-line response is exactly even ($\lambda_{\min}\sim-c\,\varepsilon^2$, $c=0.0131$) and all odd zero-moments vanish: the FE annihilates the order-3/chiral channel (which lives in $L(s,\chi_3)$, a non-self-dual character). The criterion is order-2 *complete*, not a blind truncation — confirming Prop 6.1 ($m=3$ odd-by-parity) from the off-axis-sensitivity side. (`probe_order2_vs_order3.py`.)
- *(The inequality, in the archimedean metric, $\mathsf{[P]}$.)* The correctly-shaped form is the contraction $\rho_E:=\lambda_{\max}\!\big(A^{-1/2}PA^{-1/2}\big)\le1$: the prime form is a contraction of the archimedean energy. Flatly the defect overshoots ($\lambda_{\max}(P)/\lambda_{\min}(A)=1.47$); in the archimedean metric it is a *marginal* contraction $\rho_E=0.99999659$, with $\operatorname{spec}\big(A^{-1/2}PA^{-1/2}\big)\subset[-1,1]$ (reflection-positive: both $A\pm P\succeq0$). $\rho_E$ is a *sup* eigenvalue — individual, not an average — and it detects off-line zeros ($\rho_E>1$). (`probe_energy_condition_contraction.py`.)
- *(Where the positivity lives — the $2\pi$ hinge and the pole, $\mathsf{[P]}$.)* The $\Gamma$-factor density $\Omega_\infty(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}2)-\log\pi$ changes sign at $r^{*}=6.290\approx2\pi$: a *drag* below, the *energy* above. At the smooth prolate ground state (the critical mode, $97\%$ on the two lowest frequencies) the $\Gamma$-factor is therefore a *drag* ($v^\top A_{\mathrm{arch}}v=-0.24$, and $A$ is *indefinite* there), and the rank-one $s=1$ **pole** carries the positivity ($v^\top A_{\mathrm{pole}}v=+0.27>v^\top Pv$). The margin is pole-driven (PNT-dominance, a theorem); the $\Gamma$-factor is the sub-leading correction whose sign is RH — the exact mechanism behind "finite witnesses need the pole." (`probe_ground_state_gamma_factor.py`.)
- *(No comfortable regime — scale-invariant marginality, $\mathsf{[A]}$.)* The archimedean energy accumulates ($\Omega_\infty\sim\log r$) but the zeros densify in lockstep; unfolded by the local density the marginality (tightest gap / mean spacing $\approx0.5$) is *scale-invariant* across all heights ($14\le\gamma\le200$). The high-frequency accumulation is itself marginal — the de Bruijn–Newman/§4 height-independence, now seen from the energy side; there is no comfortable high-frequency regime to bootstrap from. (`probe_highfreq_accumulation.py`; `probe_margin_sup_vs_average.py` shows the margin is a sup the averages are blind to.)

*Net.* The wall acquires a sharp two-part shape: a **symmetry half** (the FE, which fixes the $A=P$ balance to leading order — necessary, an *equality*) and an **inequality half** (the archimedean energy contraction $\rho_E\le1$ — the RH content, an individual *sup* bound in a *fixed* metric). The residue is the survival of the marginal contraction in the limit: equal across all scales (no comfortable regime) and pole-carried at the ground state. This is [CC] / the de Bruijn–Newman $\Lambda\le0$ of §4 / the archimedean realization of §7, now *resolved by frequency* and *split into its symmetry and inequality components* — a sharper shape, not a breach. The reflection-positivity is *one-sided*: the reflected half $A+P\succeq0$ is unconditional (the matrices $A,P$ are zero-independent) and comfortable (margin $\approx0.04$, where RH's side is marginal at $10^{-6}$), but it constrains the *complementary* spectral directions to RH — the negative-eigendirections of $P$, not the positive ones the contraction $\rho_E\le1$ controls — so it is a free fact, not a lever. The one direction untouched by the closed shortcuts of §6 is therefore whether $\rho_E\le1$ admits a **fusion-contingent** proof in the archimedean metric (the forward door, [N9] Conj. 5.4, now phrased as an energy contraction): the contraction fails for Davenport–Heilbronn ($\rho_E>1$, off-line zeros), so it is fusion-sighted in exactly the way §2 requires, and breaching it means deriving the contraction from the Euler product fused with the archimedean metric — multiplicative input forcing an archimedean inequality. $\mathsf{[C]}$, open.

**Update (the count/location decomposition — the open problem, quantified) $\mathsf{[P]}+\mathsf{[A]}$.** The q→1 interpolation (`probe_q_to_1_interpolation`) and the Li/Hadamard analysis (`probe_hadamard_count_vs_location`, `probe_density_gammafactor_collinear`) reduce the residue to a single, sharply-shaped statement by separating it into two pieces that live on different *scales*. The zero **count** — $N(T)=\theta(T)/\pi+1$, density $\tfrac1{2\pi}\log\tfrac{T}{2\pi}$ — is the archimedean $\Gamma$-factor: explicit (Stirling), and *shared by Davenport–Heilbronn* (same order, same density), hence not where the open content sits. The **location** ($\Re=\tfrac12$; equivalently, by the FE$+$conjugation symmetry, every zero-orbit $\{\rho,1-\rho,\bar\rho,1-\bar\rho\}$ collinear rather than a $2$D rectangle) is carried entirely by the per-zero Li factor $R(\rho)=|1-1/\rho|$ ($=1\iff\Re\rho=\tfrac12$): on-line zeros contribute the *polynomial* Li drift $\lambda_n\sim\tfrac n2\log\tfrac{n}{2\pi}$ (which **is** the count/$\Gamma$-factor), while a single off-line zero injects an *exponential* $R^n$ ($R>1$, at rate $R-1\sim|\delta|/\gamma^2$). Order-$1$ entireness (the Hadamard coupling) fixes only the polynomial side and provably cannot reach the location: count and location are separated by a **polynomial-vs-exponential scale gap**. The open problem is thereby reduced from "prove RH" to the specific statement *the Euler product suppresses the exponential $R^n$ excursion that DH (lacking it) exhibits* — the [N9] forward door in Li-coefficient form, and exactly Li's criterion $\lambda_n\ge0$ read as the scale gap (re-deriving Li–Keiper, "$R^n$ beats $n\log n$"). $\mathsf{[P]}$ the $R$-dichotomy and the polynomial drift; $\mathsf{[A]}$ the DH witness and the Euler-product separator; the bridge is RH.

---

## 8. Honest status

**Proved or certified $\mathsf{[P]}$:** the reduction chain (§1); cross-prime fusion separates the classes and discharges Davenport–Heilbronn (Thm 2.1, Cor 2.2); Pick $=$ resolvent Gram (Thm 3.1); on-axis-free / off-axis-RH (Thm 3.2); the signature theorem $\kappa=\#$off-line zeros (Thm 3.3); de Branges block $=$ predictor block (Thm 4.1) and the parity-blindness of symmetric forms (Cor 4.2); non-normality $=$ the archimedean phase (Thm 5.1); the deficiency indices $(0,0)/(1,1)$ and the arithmetic-ladder extensions (Thm 5.2); the tower theorem (Prop 6.1).

**Structural $\mathsf{[A]}$:** fusion closure as the necessary tensor skeleton (Prop 2.3); the non-lift of the Hodge index (Prop 3.4); the de Bruijn–Newman dynamical form (Thm 4.3); the wrong-knob corollary (Cor 5.3); conservation of difficulty across seven routes (§6) and the information-theoretic second wave with its single residual (Prop 6.3); local $\neq$ global (Prop 6.2).

**Open — and equal to RH $\mathsf{[C]}$:** the archimedean spectral realization (§7) — the fixed-signature positive object over $\mathbb Q$ — equivalently $P_B\succeq0$ off-axis, equivalently $\Lambda\le0$, equivalently Selberg-class $\Rightarrow$ RH, equivalently the Connes–Consani archimedean positivity, equivalently the fusion-contingent metric (the forward door of §7, [N9] Conjecture 5.4), equivalently the archimedean energy contraction $\rho_E=\lambda_{\max}(A^{-1/2}PA^{-1/2})\le1$ (§7 update).

This program does not prove the Riemann Hypothesis, and N11 does not claim it. It is the sharpest map the program owns: the wall named in five equivalent languages, the explicit operator built, two waves of shortcuts closed — seven geometric/operator (§6) and six information-theoretic (§6.3) — and the residue isolated to one place: the archimedean completion, equivalently the uniform level of distribution $\theta\to1$ on primorial moduli (Prop 6.3). **Structural reduction — real; proof of RH — not achieved.**

---

## References

[N0,N5–N7] Murillo Montero, L. (2026). *De Branges Exhaustion and Weil Domination; The Apex Edge Operator and the Archimedean Weil Form; The Unified Archimedean Operator; The Single Open Step.*

[N9] Murillo Montero, L. (2026). *The Cross-Prime Fusion Criterion.*

[N4] Murillo Montero, L. (2026). *The Apex Operator and the Archimedean Place.*

[N10] Murillo Montero, L. (2026). *The Bures–Cayley Geometric Reduction of RH and Its Ceiling.*

[CC] Connes, A., Consani, C. (2021). *Weil positivity and trace formula: the archimedean place.* Selecta Math. 27, art. 77.

[CBS] Murillo Montero, L. (2026). *Curvature and Current: The Two Blind Spots of Self-Supervised Representation Learning;* and *The Irreversible Blind Spot.* Zenodo 10.5281/zenodo.20519464, 20519454.

[RT] Rodgers, B., Tao, T. (2020). *The de Bruijn–Newman constant is non-negative.* Forum Math. Pi 8, e6.

[KL] Kreĭn, M. G., Langer, H. (1977). *Generalized Nevanlinna functions and negative squares (Pontryagin spaces).*

[dB] de Branges, L. (1968). *Hilbert Spaces of Entire Functions.* Prentice-Hall.

[Sel] Selberg, A. (1992). *Old and new conjectures and results about a class of Dirichlet series.*

[DH] Davenport, H., Heilbronn, H. (1936). *On the zeros of certain Dirichlet series.*

[Li] Li, X.-J. (1997). *The positivity of a sequence of numbers and the Riemann Hypothesis.* J. Number Theory 65, 325–333.
