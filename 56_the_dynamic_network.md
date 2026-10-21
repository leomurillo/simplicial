# 56 — The Dynamic Network: Entanglement Equilibrium on Networks of Ports

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*Draft 2 — October 2, 2026*

<!--
INTERNAL LOG — NOT FOR PUBLICATION (pandoc drops HTML comments)
2026-10-01 v0.1. Answers Paper 55's open problem O1 ("make the network dynamic"): let the network's geometry respond
to what it stores, by Jacobson's entanglement equilibrium.  Two candidate geometries tested: weights (the causal
geometry of Paper 55) and combinatorics (the bond count of Paper 55's cut law).  Excluded from the technical body:
RH, consciousness, the finite-grid thesis, the Occupation Thesis.
Certificate: empirical/network56/p56_cert.py (K/L pre-registered in its docstring before run 1).  Runs:
  run 1: E 5/5; V 4/6 (V3 failed: quadrature end truncation; checker artifact, fixed).
  run 2: V 6/6; J2 1/4 (V5 failed => inconclusive; pre-registration error: the "harmonic" exterior was the 3D one);
         J3 2/4 (V5 failed at the margin => formally inconclusive; printed branch L_J0); D 3/5 (D3, D4 failed).
  run 3 (NOT BLIND): P1 0/2 (L_J0; IR gate missed at 10.2%), P2 1/2 (gate pass; L_J0), P3 0/1 (2+1 BW deficit is
         box-independent), P4 0/3 void (checker artifact in the sparse P; fixed).
  run 4 (NOT BLIND): P4 rerun 0/3 (apex weight still saturating; sparse/dense still differ by 3%).
  run 5 (NOT BLIND): P5 1/1 -- at 60 digits the entanglement spectrum reaches eps = 49 and the centre's modular
         weight rises 15.84 -> 20.87 (BW ratio 0.84 -> 1.11): M2, P3, D3, D4, P4 were float64 artifacts of the
         modular-kernel estimator (spectrum clipped at eps ~ 30), not physics.  Entropy-level results unaffected.
2026-10-02: Sec. 4.4 added -- the 3+1 Regge hinge test (p56b_regge_cert.py run 1: 5/8, R3-R5 pointwise failures retained;
  p56b_post.py not blind: slopes 0.929 / 0.959 / 0.848, 3/3).  O1 updated.
2026-10-02 (later; Paper 57 synthesis pass): O2 CLOSED AT 60 DIGITS.  Exact dihedral reduction (the apex lies in the trivial
  irrep of D_k; invariant sector 196 orbits instead of 1756 nodes).  p56c_apex_mp_cert.py run 1: 8/9 -- gates G1-G4 pass
  (reduction reproduces stage-D float64 weights to 1.7e-5; 60 vs 80 digits agree to 3e-19); K_BW PASS (flat apex BW ratio
  1.113 -> 1.213, R = 6..12); K_M PASS (M_1 R-independent, max/min 1.034; M_7 < 0, |M_7|/M_1 1.15-1.17); K_eta FAILED,
  RETAINED (mass = 0.762 of eta delta c / 2pi, band [0.8, 1.25]).  Post-diagnosis p56d (NOT BLIND; two parallel jobs,
  p56d_run1_flat.log, p56d_run1_cone5.log): box R_max 26 -> 36.  IR1: flat BW ratio at R = 12 falls 6.5% (1.213 -> 1.134;
  R = 6..12: 1.087 -> 1.134) => the overshoot's growth with R is mostly infrared, ~9% remains at R = 6.  IR2: K_eta ratio
  0.762 -> 0.772 (stable), M_1 spread 3.4% -> 6.6%.  The earlier reading "the overshoot accounts for the miss" was too
  strong and is replaced by a factorization hypothesis [A] (overshoot ~1.1 x digital geometry ~0.96 x entropy per bond
  ~0.93, as in the 3+1 hinge).
  Peer pass (program-level review): "no-go theorem for weight gravity" rejected (numerics + exact Weyl covariance, not a
  theorem); "disjoint tiers" refined to "weights fix the constants, combinatorics carries the curvature" (Sec. 5.1);
  "locking = FDT for spacetime" kept as a reading with its precise content (Remark 5.1a), "Einstein = static FDT" and
  "gravity = nonequilibrium current" rejected (first- vs second-order faces; static fields are equilibria).
-->

---

## Abstract

Paper 55 built physical space as a network of ports and left one question open: what makes the network itself respond to what it carries? We answer it with Jacobson's entanglement equilibrium. If the entanglement entropy of every small ball is stationary at fixed volume when geometry and matter vary together, the Einstein equation follows, with Newton's constant fixed by the entanglement per unit area, $1/(4G)=\eta$. A network has two candidate geometries:
- its **weights**, which carry the light cone of Paper 55 ($c=1/\sqrt{LC}$);
- its **combinatorics**, which Paper 55's cut law counts (entanglement per cut bond).

We test both, with pre-registered falsifiers and exact or exact-covariance certificates.

**Exact backbone [P].**
- *Metric dictionary.* A static metric $(N,\Omega)$ with curvature coupling $\xi$ maps to node inertias $\Omega^d/N$, link weights $N\Omega^{d-2}$ and node masses $\xi N\Omega^dR$. Every entanglement entropy depends only on $\tilde K=M^{-1/2}(L_w+\mu)M^{-1/2}$. To first order, a spatial deformation $\Omega=1-\Psi$ acts as $\delta\tilde K=(\Psi L+L\Psi)+\kappa_\xi\,\mathrm{diag}(\Delta\Psi)$.
- *Weyl invariance at conformal coupling.* A spacetime Weyl rescaling of the network changes no entanglement, exactly at first order, if and only if $\xi=(d-1)/(4d)$.
- *Classical regions.* The modular Hamiltonian of a region of a classical harmonic network is $\beta$ times its Kron reduction. The mutual information is a ratio of spanning-forest polynomials.
- *Induced free energy.* Matter's free energy as a function of the weights is concave, with gradient equal to the effective resistance (Foster's theorem is equipartition).
- *First and second order.* The first-order term of relative entropy vanishes (the first law) and the second-order term is Fisher information (stability).

**Weights are not the gravitating geometry [numerics].** On cubic lattices in $3+1$ dimensions, the ball's ground-state entanglement responds to curvature written into the weights at *area* order.
- The volume-order term that Jacobson's derivation requires is $4$–$9\%$ of its target, and statistically marginal.
- Matter's modular energy follows Bisognano–Wichmann at volume order (within $10\%$).
- So no local equilibrium exists between matter and weight-curvature.

The small induced volume term has the structure of heat-kernel induced gravity, vanishing at $\xi_0=0.164\pm0.017$ (that is, $1/6$). In $2+1$ dimensions the same holds ($3\%$ of target). The reason is structural: entanglement counts bonds, and weights move the cutoff together with the metric (the network is a Weyl-covariant regulator).

**Combinatorics carries Jacobson's term [numerics].** On triangulated cones in $2+1$ dimensions:
- the entanglement per cut bond is the same with positive, zero and negative curvature defects, to $0.5\%$;
- at fixed node count, a disclination changes the entanglement by exactly $\eta_b$ times its bond deficit (ratios $0.93\to0.999$). That is Jacobson's area-deficit term, realized combinatorially.

**The same holds in $3+1$ [numerics].** Take a Regge hinge, a cosmic-string line of deficit $\pm\pi/3$ in a stacked prism network. The entanglement per bond does not see the hinge. At fixed node count, the entanglement change around the hinge equals $\eta\,\delta A|_V=-\tfrac23\eta\,\delta R^2$ with fitted slope $0.85\pm0.03$, and $\eta_b$ times the bond deficit with slope $0.93\pm0.02$.

**Verdict.** The network becomes dynamic through its combinatorics, not through its weights. Weights fix the constants and carry causality (Paper 55); bond counts carry the curvature. Newton's constant is the inverse entanglement per bond in cell units: $G=a_{\rm cell}/(4\eta_b)$ [A, conditional].

**The matter side.** It is Bisognano–Wichmann on the lattice: within $10\%$ in $3+1$, and within $11\%$ in $2+1$ once the modular spectrum is resolved at 60 digits. On the cones, an exact dihedral reduction makes 60 digits affordable (Section 4.3).
- The apex modular weight exceeds Bisognano–Wichmann by $11$–$21\%$ at $R_{\max}=26$, and by $9$–$13\%$ in a larger box. Its growth with $R$ is mostly an infrared effect.
- The point-mass law holds: $-\delta S/\beta(0)$ is independent of the ball radius to $3.4\%$ for $R=6$–$12$ ($6.6\%$ in the larger box), against an $86\%$ drift in float64.
- Its value is $0.76$–$0.77$ of the continuum $\eta\delta c/2\pi$ in both boxes. That is a pre-registered miss, retained, and its continuum limit is open.

The certificate retains every failure:
- a quadrature artifact (V3), fixed;
- two truncation and IR gates;
- a pre-registration error in the 2D exterior profile;
- a family of apparent $2+1$ Bisognano–Wichmann failures, which a 60-digit check traced to float64 clipping of the entanglement spectrum (P5);
- at 60 digits on the cones, the mass value at $0.76$ of the continuum prediction, just outside its pre-registered band (K_eta).

---

## 1. The question

### 1.1 From Paper 55

Paper 55 showed that a network of passive ports supports a light cone (when nodes and links store energy in two conjugate forms), cut laws (thermal mutual information and capacity bounded by the cut), and an arrow on its cycle space. It ended with an open problem (its O1): the network's own weights $(L_e,C_v)$ do not yet respond to what flows through them. Without that, there is no gravity. This paper supplies the response law and tests it.

### 1.2 Entanglement equilibrium, and why it is the program's inequality

Jacobson (2016) proposed the *maximal vacuum entanglement hypothesis*. Vary the geometry and the quantum state together around the vacuum of a small ball $A$ at fixed volume. Then the ball's entanglement is stationary:
$$\delta S_A=\delta S_{\rm UV}+\delta S_{\rm IR}=\eta\,\delta A\big|_V+\delta\langle K_A\rangle=0 .$$
Here $\eta$ is the entanglement per unit area and $K_A$ is the Bisognano–Wichmann modular Hamiltonian:
$$K_A=2\pi\int_A\frac{R^2-r^2}{2R}\,T_{00}.$$
For a ball, the area deficit at fixed volume is $\delta A|_V=-\frac{\Omega_{d-1}R^{d+1}}{(d+1)^2-1}\,G_{00}$. Equating the two terms for every ball gives $G_{ab}=8\pi G\,T_{ab}$ with $1/(4G)=\eta$.

In the program's language, the first-order term $\delta S_A=\delta\langle K_A\rangle$ is the first law of entanglement. It is the first-order vanishing of relative entropy, and the second-order term is Fisher information ($\ge0$; Lashkari–Van Raamsdonk 2016). Relative-entropy positivity is the program's one inequality (passivity), so gravity by entanglement equilibrium is that inequality at first order. Stability is the same inequality at second order (Proposition 2.6).

### 1.3 Two geometries on a network

A network carries two different notions of geometry.
- **Causal.** Its weights fix local light speeds and travel times, hence a metric (Paper 55, Section 3).
- **Entropic.** Its combinatorics fixes how many bonds a cut crosses. Paper 55's area laws count cut bonds (its Corollary 4.3), and Section 4.1 below shows that the entanglement per bond is independent of curvature.

In a continuum these are one metric. On a network they need not be. We test which one can carry Jacobson's equilibrium.

### 1.4 Prior art, and what is new

**Classical, credited:**
- entanglement equilibrium (Jacobson 1995, 2016);
- the first law of entanglement and gravitation from entanglement (Blanco–Casini–Hung–Myers 2013; Faulkner–Guica–Hartman–Myers–Van Raamsdonk 2014; Lashkari–Van Raamsdonk 2016);
- induced gravity (Sakharov 1967; Visser 2002) and its equality with entanglement for minimally coupled fields (Susskind–Uglum 1994; Solodukhin 2011);
- area laws on lattices (Srednicki 1993; Eisert–Cramer–Plenio 2010);
- the Bisognano–Wichmann theorem (1975) and its lattice tests;
- Regge calculus (1961), dynamical triangulations, and causal sets (Sorkin);
- random planar maps, i.e. random gases of degree (disclination) defects, and their Liouville quantum gravity limits.  Spanning-tree-weighted and critical Fortuin–Kasteleyn maps converge to Liouville quantum spheres, and random walk converges to Liouville Brownian motion.  For FK–Ising maps there is also eigenvalue and heat-trace convergence, using stated Brownian/LQG inputs (OpenAI 2026, `github.com/openai/math`, family 211; model-generated; tier [A]).  These results average over random defect configurations.  They do not bear on the single-disclination ratio $0.76$ above, whose continuum limit stays open.
- point particles in $2+1$ gravity as conical deficits (Staruszkiewicz 1963; Deser–Jackiw–'t Hooft 1984);
- the Kirchhoff matrix-tree and Foster theorems.

**New here:**
1. the network metric dictionary, with exact first-order lattice Weyl invariance at conformal coupling (Theorem 2.1, Corollary 2.2);
2. the classical modular Hamiltonian as Kron reduction and the Kirchhoff form of network mutual information (Proposition 2.4);
3. a pre-registered, validated Jacobson test on fixed graphs in $2+1$ and $3+1$ dimensions, with a quantified negative and the heat-kernel $\xi$-structure of the residue (Section 3);
4. the bond-count universality and the combinatorial realization of Jacobson's deficit term (Section 4);
5. the synthesis: weights fix the constants and carry causality, bonds carry the curvature (Section 5);
6. the matter half of the disclination law at 60 digits, made feasible by an exact dihedral reduction (Section 4.3).

**Tiers.** [P] proven (exact, certified) or cited; [A] structural reading or conditional derivation; [C] conjecture, fenced. Numerics use exact covariance formulas (no sampling) and are labelled [numerics].

---

## 2. The exact backbone

### 2.1 The metric dictionary

**Theorem 2.1 (network metric dictionary) [P].** Take a scalar field with curvature coupling $\xi$ on a static metric $g=-N^2dt^2+\Omega^2\delta_{ij}dx^idx^j$ in $d$ space dimensions. Discretize it on a cubic lattice of unit spacing with node inertia $M_v=\Omega_v^d/N_v$, link weight $w_e=N_e\Omega_e^{d-2}$ (bond averages) and node mass $\mu_v=\xi N_v\Omega_v^dR_v$.
- Every entanglement entropy of every region in the ground state depends only on $\tilde K=M^{-1/2}(L_w+\operatorname{diag}\mu)M^{-1/2}$.
- To first order in $\Psi$, with $\Omega=1-\Psi$ and $\Delta$ the lattice Laplacian with mirror walls, $\delta\tilde K$ takes two forms:

$$\textbf{(a) spatial }(N=1):\qquad \delta\tilde K=(\Psi L+L\Psi)+\kappa_\xi\,\mathrm{diag}(\Delta\Psi),\qquad \kappa_\xi=2(d-1)\xi-\tfrac{d-2}2;$$
$$\textbf{(b) spacetime Weyl }(N=\Omega):\qquad \delta\tilde K=\Big(2d\xi-\tfrac{d-1}2\Big)\mathrm{diag}(\Delta\Psi).$$

*Proof.*
- *Reduction to $\tilde K$.* The canonical transformation $y=M^{1/2}x$, $p_y=M^{-1/2}p$ is a product of local symplectic maps, so it preserves every entanglement entropy. In the new variables $H=\tfrac12p_y^2+\tfrac12y^{\mathsf T}\tilde Ky$.
- *First order.* Expand to first order and use the identity $\sum_e\Psi_eb_eb_e^{\mathsf T}=\tfrac12(\Psi L+L\Psi)+\tfrac12\operatorname{diag}(\Delta\Psi)$, with $\Psi_e$ the bond average and wall bonds carrying the site value.
- *Curvature.* The scalar curvature is $2(d-1)\Delta\Psi$ (spatial) or $2d\,\Delta\Psi$ (Weyl) at first order.

*Certificate E3* (symbolic in $\Psi$ and $\xi$; $4\times4$ and $3\times3\times3$ Dirichlet lattices). $\square$

**Corollary 2.2 (the network is exactly Weyl invariant at conformal coupling) [P].** In (b), $\delta\tilde K\equiv0$ if and only if $\xi=\frac{d-1}{4d}$, the conformal coupling in $D=d+1$ dimensions. A Weyl rescaling of a conformally coupled network changes no entanglement of any region at first order. *Certificate E3.* $\square$

**Corollary 2.3 (only gradients are felt) [P].** For uniform $\Psi$ in a massless network, $\delta\tilde K=2\Psi L$ is a uniform rescaling. The ground state transforms as $X\to\lambda^{-1/2}X$, $P\to\lambda^{1/2}P$, so every $X_AP_A$ is invariant. Entanglement therefore sees only the gradients and curvature of the metric. *Certificate V3:* $|\sum_v(L\mathcal W)_{vv}|\le2.5\times10^{-9}$ of $\sum_v|(L\mathcal W)_{vv}|$. $\square$

### 2.2 Modular Hamiltonians and induced free energies

**Proposition 2.4 (classical modular Hamiltonian = Kron reduction) [P].** Let $\rho\propto e^{-\beta x^{\mathsf T}Kx/2}$ be a classical Gibbs state of a harmonic network, and split it into regions $A$ and $B$.
- The marginal on $A$ is Gibbs for the Kron-reduced stiffness $K/K_{BB}=K_{AA}-K_{AB}K_{BB}^{-1}K_{BA}$. So the modular Hamiltonian of a region is $\beta$ times its Kron-reduced energy, which is the reduced admittance of Paper 55 (Theorem 2.2(c)).
- The mutual information is
  $$I(A{:}B)=\tfrac12\ln\frac{\det K_{AA}\,\det K_{BB}}{\det K},$$
  a ratio of rooted spanning-forest polynomials (matrix-tree).

*Proof.* Schur complements; $\det\Sigma_{AA}=\det K_{BB}/\det K$. *Certificate E1* (exact rationals; $I=0.2171$ on the instance). $\square$

**Proposition 2.5 (the induced free energy of the weights) [P].** For the classical network, $F(w)=\tfrac T2\ln\det K(w)$ up to a constant.
- **(i) Hellmann–Feynman.** $\partial F/\partial w_e=\tfrac12\langle(x_i-x_j)^2\rangle=\tfrac T2R_{\rm eff}(e)$.
- **(ii) Foster is equipartition.** $\sum_ew_eR_{\rm eff}(e)=n-1$.
- **(iii) Concavity.** $\partial^2F/\partial w_e\partial w_f=-\tfrac T2\big(b_e^{\mathsf T}K^{-1}b_f\big)^2\preceq0$.

So matter makes the geometry softer, the network form of Sakharov's induced action.

*Certificate E2* (symbolic weights on a random 6-node graph: matrix-tree polynomial enumerated, Hellmann–Feynman, Foster, and a negative definite Hessian of signature $(0,0,9)$). $\square$

**Proposition 2.6 (first law, vacuum stationarity, stability) [P].**
- **(a) First law, and stability.** For Gaussian states, $D(\rho+\delta\rho\,\Vert\,\rho)$ has no first-order term, and its second-order term is the Fisher information. *Certificate E5:* classical Gaussian instance, $e^2$-coefficient $=\tfrac14\operatorname{tr}((\Sigma^{-1}\Delta)^2)>0$.
- **(b) Vacuum stationarity.** For any first-order perturbation $\delta K$ of a Gaussian ground state, $\delta\langle H_{\rm old}\rangle=\frac1{2\pi}\int_0^\infty\operatorname{tr}\big((t^2-L)G_t\,\delta K\,G_t\big)dt=0$, because $\int_0^\infty\frac{t^2-\lambda}{(\lambda+t^2)^2}dt=0$. *Certificate E4.*

*Consequence.* $\delta S_A=\delta\langle K_A\rangle$ for every first-order change of state. Geometry-induced and matter-induced changes of a region's entanglement are both modular energies. But a geometry change of the *vacuum* carries no net energy at first order, while a matter excitation does. Section 3.5 shows that this asymmetry is what removes the volume term from weight geometry. $\square$

---

## 3. Weights as geometry: the Jacobson test

### 3.1 Setup and targets

**The system.** We take a massless scalar on a Dirichlet cube (cubic lattice, unit weights), in its ground state, with ball $A=\{|x-c|\le R\}$ and $R_{\rm eff}=(n_A/V_d)^{1/d}$.

**The geometry variation** is a spatial deformation with uniform curvature inside $R_c=R+1.5$ and a harmonic exterior:
- $\Psi=r^2/2$ inside, so $\Delta\Psi=d$;
- $\Psi=\tfrac32R_c^2-R_c^3/r$ outside in 3D;
- $\Psi=\tfrac12R_c^2+R_c^2\ln(r/R_c)$ outside in 2D.

By Theorem 2.1, $\delta S_A(\xi)=y_s+\kappa_\xi y_m$, where $y_s$ is the response to the $(\Psi L+L\Psi)$ part and $y_m$ the response to $\operatorname{diag}(\Delta\Psi)$.

**Targets (fixed before any run).**
- *Jacobson.* The area deficit at fixed volume for this curvature is $-(8\pi/5)R^4$ in 3D and $-(\pi/2)R^3$ in 2D. So entanglement equilibrium predicts
  $$\delta S_{\rm geom}=-J_d\,\eta\,R^{d+1}+\text{lower},\qquad J_3=\tfrac{8\pi}5,\ J_2=\tfrac\pi2 .$$
- *Matter.* Bisognano–Wichmann predicts the modular weight sums $(8\pi^2/15)R^4$ (3D) and $(\pi^2/2)R^3$ (2D).
- *Consistency ratio.* $r_J=-c_{\rm top}/(J_d\eta)$, with $c_{\rm top}$ the fitted $R^{d+1}$ coefficient of $\delta S_{\rm geom}$ at minimal coupling.
- *Pre-registered branches:*
  - **K_J**: $c_{\rm top}<0$, dominance $|c_{\rm top}|R_{\max}^{d+1}\ge\tfrac12|y(R_{\max})|$, and $r_J\in[0.5,2]$;
  - **L_J0**: no volume-order response (dominance fails);
  - **L_J1**: repulsive;
  - **L_J2**: wrong strength.

### 3.2 Method and validation

The response is computed by linear response:
$$\delta S_A=\operatorname{tr}(\delta\tilde K\,\mathcal W),\qquad \mathcal W=\frac1\pi\int_0^\infty G_t[\,\cdot\,,A]\,(t^2D_P-D_X)\,G_t[A,\,\cdot\,]\,dt,$$
with $G_t=(L+t^2)^{-1}$. Here $D_X=\partial S/\partial X_A$ and $D_P=\partial S/\partial P_A$ are half the modular-Hamiltonian kernels.

The resolvent is applied by discrete sine transforms. The $t$-integral uses a trapezoid rule in $u=\ln t$ with exact geometric-sum end corrections.

*Validation (certificate V):*
- **V1.** The quadrature reproduces $X_A$ to $2\times10^{-13}$.
- **V2.** Linear response agrees with an independent dense finite difference, to $10^{-6}$ (scaling channel) and $3\times10^{-9}$ (mass channel).
- **V3.** Uniform rescaling is invisible to $10^{-9}$.

**A retained failure.** In run 1, V3 failed at $5\times10^{-7}$. The cause was the quadrature's truncated large-$t$ tail in the $P$ channel, a checker artifact; the end corrections fixed it before any physics run.

### 3.3 Results

| Run | $d$ | Lattice | Gate | $c_{\rm top}(\xi=0)$ | Jacobson target $-J_d\eta$ | $r_J$ | Dominance | Scaling of $\lvert\delta S\rvert$ | Branch |
|---|---|---|---|---|---|---|---|---|---|
| J3 (pre-registered) | 3 | $L=33$, truncated sums | V5 0.100 (fail at margin) | $-0.0090\pm0.0056$ | $-0.099$ ($\eta=0.0197$) | 0.091 | 0.47 | — | L_J0 (formally inconclusive) |
| P2 (not blind) | 3 | $L=25$, full sums | IR 3% (pass) | $-0.0078\pm0.0026$ | $-0.099$ to $-0.18$ | 0.04–0.08 | 0.30 | $R^{2.18}$ | **L_J0** |
| J2 (pre-registered) | 2 | $L=81$ | V5 fail; profile error | — | — | — | — | — | inconclusive |
| P1 (not blind) | 2 | $L=161$, full sums, log exterior | IR 10.2% (miss) | $-0.0036\pm0.0012$ | $-0.130$ ($\eta=0.083$) | 0.028 | 0.27 | $R^{1.52}$ | **L_J0** |

The 3D area-law coefficient is not sharply determined on these small balls: $\eta=0.020$ from the $R\le6$ fit and $0.036$ from the $R\le5$ fit. The range of $r_J$ reflects this; either way $r_J\ll\tfrac12$.

At $R_{\rm eff}\approx5$ in 3D:
- Jacobson's equilibrium would need $\delta S_{\rm geom}\approx-60$ per unit curvature, attractive and volume order;
- the network gives $+16$ ($y_s=3.48$, $y_m=-25.1$), area order with the wrong sign;
- Bisognano–Wichmann matter gives $3.09\times10^3$ against $3.22\times10^3$ predicted.

**The pre-registration error (retained).** The exterior profile of the pre-registered 2D run was the 3D harmonic function. In 2D, $\nabla^2(1/r)\ne0$, so J2 tested a different profile from the one its prose describes. P1 repeats the test with the correct logarithmic exterior. This is the "artifact and prose agree, the premise is wrong" trap of the GPD method (Paper 35), recorded as such.

### 3.4 The residue is induced gravity with the heat-kernel structure

The fitted volume coefficient as a function of coupling, $c_{\rm top}(\xi)=c_s+\kappa_\xi c_m$, vanishes at
$$\xi_0=0.164\pm0.017\ \ (\text{P2}),\qquad \xi_0=0.166\pm0.034\ \ (\text{J3}).$$
Both are consistent with $1/6$, where the heat-kernel coefficient of the induced Einstein–Hilbert term, $\propto(1/6-\xi)$, vanishes. The network does induce a Newton term of Sakharov type with the right $\xi$-structure. Its strength is about an order of magnitude below what its own area law would require [numerics, indicative; the error on $c_m$ is $40$–$70\%$].

### 3.5 Why weights cannot carry Jacobson's term [A]

Two exact facts and one measured fact explain the negative.
1. **Entanglement counts bonds.** The entanglement per cut bond is the same across curvature defects (Section 4.1, to $0.5\%$), and the cubic-lattice area law counts cut bonds (Paper 55).
2. **Weights move the cutoff with the metric.** Rescaling weights rescales the cell, so the number of cut bonds, and the entanglement per bond, are unchanged (Corollaries 2.2–2.3). The network is a Weyl-covariant regulator. Jacobson's term $\eta\,\delta A|_V$ requires the proper area to change at a *fixed proper cutoff*, and that has no counterpart when only weights change.
3. **Vacuum stationarity removes the monopole.** By Proposition 2.6(b), a geometry change carries no net modular energy at first order. Only the second moment of the energy-density response survives, and that is the induced (Sakharov) term of Section 3.4.

Matter excitations do carry a modular-energy monopole, so they respond at volume order. On a fixed graph the two sides of the equilibrium scale differently. **A fixed graph cannot gravitate through its weights.**

### 3.6 The matter side

In 3D, the kinetic modular weights follow Bisognano–Wichmann within $10\%$ (ratios $0.90$–$1.04$, M3 and P2). In 2D the float64 estimator appeared to fail:
- the ratio fell from $1.03$ to $0.56$ as $R$ went from $4$ to $16$;
- it was identical at $L=81,161,241$ (P3).

**This was a precision artifact, not physics.** The modular kernels $D_X,D_P$ are dominated by modes of large modular energy $\varepsilon=\ln\frac{\nu+1/2}{\nu-1/2}$. Bisognano–Wichmann puts $\varepsilon$ up to about $\beta(0)\,\omega_{\max}$, which is about $100$ at $R=12$ in 2D. Float64 resolves $\nu-\tfrac12$ only to about $10^{-13}$, so it clips $\varepsilon$ near $30$. The clip explains the whole pattern:
- the saturation;
- a deficit that grows with $R$;
- box-independence;
- a milder effect in 3D, where the weight sum is less centre-weighted.

*Certificate P5* (not blind; criteria written first) repeats a 2D disk ($R=6$) at 60 digits. The spectrum reaches $\varepsilon_{\max}=49.3$, with 24 modes above 30. The centre's kinetic modular weight rises from $15.84$ to $20.87$, so the Bisognano–Wichmann ratio goes from $0.84$ to $1.11$. The entropy is identical in both precisions.

Entropy-level quantities — every J verdict, and D1–D2 below — are insensitive to the clip. Geometric perturbations keep the global state pure, so nearly pure modes receive only exponentially small first-order changes; V2 validated these quantities. Matter excitations, by contrast, inject noise into nearly pure modes, so the matter side needs the extra precision.

---

## 4. Combinatorics as geometry: disclinations in $2+1$ dimensions

### 4.1 Triangulated cones, and the bond-count law

**The cones.** Glue $k$ triangular sectors around an apex, with unit weights and a Dirichlet outer ring:
- $k=6$ is the flat triangular lattice;
- $k=5$ has a positive deficit $\pi/3$;
- $k=7$ has a negative deficit.

Every vertex except the apex has degree 6. Graph balls are the rings $0..R$, and $\mathrm{cut}(R)=k(2R+1)$ counts the links leaving ring $R$.

**D1 (passed).** Fitting $S=\eta_b\,\mathrm{cut}+s_0$ over $R\in[4,12]$ gives $\eta_b=0.03669$ ($k=6$), $0.03654$ ($k=5$) and $0.03679$ ($k=7$). The entanglement per bond does not see the curvature defect, to $0.5\%$.

### 4.2 The disclination realizes Jacobson's deficit

**D2 (passed).** Compare a cone ball with a flat ball holding the same number of nodes (the combinatorial volume), with the flat data interpolated. The entanglement difference equals $\eta_b$ times the bond deficit:

| $R$ | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|
| $k=5$ (positive curvature) | 0.932 | 0.948 | 0.961 | 0.974 | 0.986 |
| $k=7$ (negative curvature) | 0.946 | 0.961 | 0.974 | 0.986 | 0.999 |

The ratio rises toward $1$ as the ball grows. In continuum terms, the bond deficit at fixed node count is the circumference deficit at fixed area, $\delta C|_V=-\tfrac R2\,\delta$. *Combinatorial curvature produces exactly Jacobson's term $\eta\,\delta A|_V$*, with the $\eta$ of the area law — the consistency that weight-geometry missed by an order of magnitude.

### 4.3 The matter side at the apex, at 60 digits

Entanglement equilibrium for balls centred on the apex reads $\eta\,\tfrac R2\,\delta=\beta(0)\,M$. With Bisognano–Wichmann, $\beta(0)=\pi R/c$, so a disclination of deficit $\delta$ would be a point mass $M=\eta\,\delta\,c/(2\pi)$, independent of $R$. That is the $2+1$ law $\delta=8\pi GM$ with $G=1/(4\eta)$.

**The float64 test (retained).**
- **D3 (failed).** The apex kinetic weight saturates: the Bisognano–Wichmann ratio falls from $0.82$ to $0.48$ for $R=6\ldots12$ at $R_{\max}=26$.
- **D4 (failed).** As a consequence, $M_1(R)$ drifts from $0.015$ to $0.028$.
- **D5 (passed).** On average $M_1\cdot2\pi/(\eta\,\delta\,c)=1.36$, within the pre-registered $[0.5,2]$.
- **Post-diagnosis P4.** A sparse route at $R_{\max}=78$ failed in the same way.

All of these are the float64 clip of Section 3.6. Resolving the apex weight at $R=12$ needs the reduced covariances to about $e^{-100}$.

**The multiprecision test.** An exact reduction makes 60 digits affordable.
- *The reduction.* Each cone graph has the dihedral symmetry $D_k$, generated by rotating the sectors and by the reflection $m\mapsto-m$ of every ring. Every matrix function of $K$, and every ball, block-diagonalizes over the irreducible representations of $D_k$. The apex spans its own orbit, so it lies in the trivial one. The apex weight $2D_P(0,0)$ is therefore computed exactly inside the invariant sector: 196 orbits instead of 1756 nodes.
- *The gates.* Certificate `p56c_apex_mp_cert.py` (falsifiers pre-registered) reproduces the float64 stage-D weights inside that sector to $1.7\times10^{-5}$ (gate G2). Its 60- and 80-digit runs agree to $3\times10^{-19}$ (G4). The entanglement spectrum now reaches $\varepsilon_{\max}=101$ at $R=12$, where float64 stopped near 30.

| $R$ | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| flat apex weight / $(\pi R_{\rm eff}/c)$, float64 (D3) | 0.824 | 0.739 | 0.668 | 0.610 | 0.560 | 0.518 | 0.481 |
| the same at 60 digits (K_BW) | 1.113 | 1.125 | 1.139 | 1.153 | 1.170 | 1.190 | 1.213 |
| $M_1=-\delta S_5/\beta_5(0)$, 60 digits (K_M) | 0.01172 | 0.01192 | 0.01204 | 0.01211 | 0.01212 | 0.01208 | 0.01200 |
| $M_7=-\delta S_7/\beta_7(0)$, 60 digits | $-0.01376$ | $-0.01389$ | $-0.01395$ | $-0.01396$ | $-0.01393$ | $-0.01386$ | $-0.01376$ |

- **K_BW (passed).** The flat apex weight follows Bisognano–Wichmann within $11$–$21\%$, rising slowly with $R$. Most of the rise is infrared (see "Box size" below).
- **K_M (passed).** The disclination is a point mass. $M_1$ is independent of $R$ to $3.4\%$ (max/min $1.034$), against an $86\%$ drift in float64. The negative disclination has the opposite sign, with $|M_7|/M_1=1.15$–$1.17$, an effect of second order in $\delta$.
- **K_eta (failed, retained).** The value of the mass is $0.762$ of the area-law prediction $\eta\delta c/(2\pi)$ (with $\eta_{\rm len}=0.0771$), just below the pre-registered band $[0.8,1.25]$.

**Box size (post-diagnosis, not blind).** Certificate `p56d_ir_check.py`, with its criteria written before the run, enlarges the box from $R_{\max}=26$ to $36$ (an invariant sector of 361 orbits):

| $R$ | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| flat apex weight / $(\pi R_{\rm eff}/c)$, $R_{\max}=36$ | 1.087 | 1.093 | 1.099 | 1.107 | 1.115 | 1.124 | 1.134 |
| $M_1$, $R_{\max}=36$ | 0.01191 | 0.01220 | 0.01240 | 0.01253 | 0.01262 | 0.01267 | 0.01269 |

- **IR1.** At $R=12$ the flat ratio falls by $6.5\%$, from $1.213$ to $1.134$. The criterion was a drop of more than $2\%$, so the overshoot is partly infrared. Its growth with $R$ comes mostly from the Dirichlet wall, and about $9\%$ remains at $R=6$.
- **IR2.** The mass ratio moves only from $0.762$ to $0.772$ (with $\eta_{\rm len}$ going from $0.0771$ to $0.0789$). The spread of $M_1$ over $R=6$–$12$ grows from $3.4\%$ to $6.6\%$.

So the normalization gap is not an artifact of the box, while most of the overshoot's slow growth is.

**Reading the miss [A].** The apex modular weight equals the flat centre's at the same hop radius to $2$–$3\%$ in both boxes. At equal geodesic radius, the apex therefore inherits the flat overshoot, which is $9$–$13\%$ in the larger box. If $\beta(0)$ is replaced by its Bisognano–Wichmann value, the inferred mass is $0.90$–$1.03$ of $\eta\delta c/2\pi$ (both boxes), but it then drifts with $R$ by about $10\%$. With the lattice's own modular weight it is flatter ($3$–$7\%$), and it sits at $0.76$–$0.77$. So the *point-mass property* is carried best by the true modular Hamiltonian, and the *normalization* falls short of the continuum value. A plausible factorization: the overshoot ($\approx1.1$) times digital-geometry and entropy-per-bond factors of the size measured for the $3+1$ hinge in Section 4.4 ($0.96$ and $0.93$) gives about $0.8$. Whether these lattice factors tend to 1 in the continuum is open.

**What the law now says [numerics, A].** Entanglement equilibrium at the apex, with the lattice's own modular Hamiltonian, makes a disclination a point mass: one number, nearly independent of the radius at which it is weighed. Its value is $0.76$–$0.77$ of the continuum $\eta\delta c/2\pi$ at these sizes, in two box sizes. It is open whether that gap closes in the continuum limit, in which case $\delta=8\pi GM$ holds exactly, or renormalizes the mass. In continuum units the elementary disclination ($\delta=\pi/3$) would have mass $\eta c/6$.

### 4.4 The $3+1$ Regge hinge

In $3+1$ dimensions Regge curvature lives on hinges, which have codimension 2: lines in space. The cleanest hinge is a straight cosmic string, a line around which space has a conical deficit $\delta$.

**Jacobson's prediction for a string.** Take a geodesic ball of radius $R$ centred on the line.
- The cone-times-line geometry multiplies both volume and area by $1-\delta/2\pi$. At fixed volume this gives
  $$\delta A|_V=4\pi R^2\big[(1-\delta/2\pi)^{1/3}-1\big]=-\tfrac23\,\delta R^2+O(\delta^2).$$
- A string of mass per length $\mu$ through the centre has Bisognano–Wichmann modular energy $\tfrac{4\pi}3\mu R^2/c$.
- Equilibrium then gives $\delta=2\pi\mu/\eta=8\pi G\mu$ with $G=1/(4\eta)$: the general-relativistic cosmic-string deficit. Both sides scale as $R^2$, so the balance holds at every radius.

**The network.** The prism network stacks the cones of Section 4.1 along $z$, with $k=5,6,7$ sectors and 41 layers.
- In-plane links have weight $1$ and vertical links $3/2$, so the long-wavelength light speed is isotropic ($c^2=3/2$ both ways; exact).
- The hinge is the vertical line through the apex.
- Balls are geodesic, $\rho^2+(z-z_0)^2\le R^2$, using the intrinsic cone distance $\rho^2=r^2-rj+j^2$ (exact).
- The ground state comes from the exact product structure (dense in-plane eigenbasis tensored with sine modes along $z$). It matches a dense diagonalization of the full prism to $2\times10^{-15}$.
- Everything here is entropy-level, so it is robust in float64 (Section 3.6).

*Certificate* `empirical/network56/p56b_regge_cert.py`, with the K/L pre-registered:
- **R1 (passed).** The flat prism obeys the bond-count law $S=\eta_\parallel c_\parallel+\eta_\perp c_\perp+s_0$, with $\eta_\parallel=0.0128$, $\eta_\perp=0.0114$ and rms $0.94\%$.
- **R2 (passed).** Around the hinge the entanglement per bond is unchanged. The cone balls' residuals from the flat bond-count law are $0.08$, against a deficit signal of $0.70$–$0.78$.
- **R3–R5 (failed, retained).** These pre-registered *pointwise* ratios mostly fall in $[0.90,1.04]$ and $[0.73,0.98]$, but individual digitized balls give outliers ($0.34$–$1.79$). The deficit is about $5\%$ of the cut count, comparable to the digitization jitter of single balls. The pre-registration repeated a mistake the program had already recorded: it used pointwise values at finite size instead of bands or fitted slopes.

*Post-diagnosis* (`p56b_post.py`; not blind; regression slopes through the origin over all $R\in[3,7.5]$, with $k=5$ and $7$ jointly; criteria written first):

| Statement | Slope | $k=5$ | $k=7$ | Band | Result |
|---|---|---|---|---|---|
| R3′: $\delta S=\eta_b\times$ bond deficit | $0.929\pm0.022$ | $0.930$ | $0.927$ | $[0.85,1.15]$ | pass |
| R4′: bond deficit $=\sigma_b\times(-\tfrac23\delta R^2)$ | $0.959\pm0.057$ | $0.908$ | $1.011$ | $[0.75,1.3]$ | pass |
| **R5′: $\delta S|_n=\eta\,\delta A|_V$** | $\mathbf{0.848\pm0.033}$ | $0.796\pm0.038$ | $0.899\pm0.051$ | $[0.75,1.3]$ | **pass** |

**A $3+1$ Regge hinge carries Jacobson's term** at $85\%$ of its continuum value for $R\le7.5$. The shortfall factorizes:
- $0.93$ for entropy per bond deficit, which is where the $2+1$ analogue (D2) stood at comparable radii before rising to $0.999$;
- $0.96$ for the digital geometry.

The matter half, the string's modular energy, is not tested yet. The dihedral reduction of Section 4.3 extends to the prism: the invariant sector of each cone, tensored with the axial sine modes, holds the axis of the hinge. So the same 60-digit test is feasible. Until it is run, the cosmic-string law $\mu=\eta\,\delta/(2\pi)$ stays [A].

---

## 5. The dynamic network

### 5.1 Two geometries, one locking condition

A network of ports carries:
- a **causal metric**, set by weights (local light speeds and travel times; Paper 55);
- an **entropic metric**, set by combinatorics (bonds per cut; Section 4.1).

The results above assign them different jobs, and the division is sharper than "weights versus bonds".
- **The weights fix the constants.** They set the light speed, $c(\hat k)^2=\hat k^{\mathsf T}A\hat k/C$. They set Newton's constant, $G=a_{\rm cell}/(4\eta_b)$, through the entanglement per bond and the proper area per bond. They also carry a weak induced Newton term (Section 3.4).
- **The combinatorics carries the curvature.** A curvature defect is a bond deficit (Sections 4.2, 4.4).
- **Neither tier stands alone.** The cone needs the directions of the bond star ($A=\sum_ew_e\delta_e\delta_e^{\mathsf T}$), and $\eta_b$ depends on the weights.

A single spacetime metric exists only if the two geometries agree, that is, if the proper area per cut bond, read from travel times, is the same everywhere. We call such a network *locked* [A].

**Remark 5.1a (locking as watching against pushing) [A].** The causal metric is read by *pushing*: it is the support of the retarded response. The entropic metric is read by *watching*: it is the entanglement of vacuum fluctuations. For the weights the two readings cannot be separated. Every entanglement entropy and the retarded propagator are functions of the one operator $\tilde K$ (Theorem 2.1). In a ground or thermal state, the fluctuation–dissipation theorem ties the watched correlations to the pushed response. A weight deformation therefore moves both together. That is the Weyl covariance of Corollaries 2.2–2.3, and it is why weights cannot produce Jacobson's term at a fixed proper cutoff (Section 3.5). A combinatorial defect changes the number of bonds at fixed cell size, and so shifts the entropic metric against the causal one. Locking requires that this shift be matched everywhere by the geometry.

Jacobson (1995) called the resulting Einstein equation an *equation of state*. Its first-law form is the first-order face of the same equilibrium whose second-order face is the static fluctuation–dissipation theorem (Paper 54, Theorem 2) and the Fisher stability of Proposition 2.6. The two are faces of one equilibrium, not one statement: the balance condition is first order, the fluctuation–dissipation theorem second order. A network out of local entanglement equilibrium would carry nonequilibrium corrections of the Eling–Guedens–Jacobson (2006) type. Static gravitational fields are equilibrium configurations, not currents.

### 5.2 The field equation [A, conditional]

Suppose:
- the entanglement per bond is universal (Section 4.1);
- a combinatorial curvature defect changes entanglement by $\eta_b$ times its bond deficit (Section 4.2);
- matter's modular energy is Bisognano–Wichmann (on the lattice: within $10\%$ in $3+1$, within $11\%$ in $2+1$ once resolved at 60 digits, and within $9$–$13\%$ at the centre of a ball on the flat triangular network in the larger box; Sections 3.6, 4.3).

Then entanglement equilibrium at fixed node count, applied to every ball, is Jacobson's equilibrium written in bond units. In the continuum limit of a locked network it gives
$$G_{ab}=8\pi G\,T_{ab},\qquad G=\frac{a_{\rm cell}}{4\eta_b},$$
with $a_{\rm cell}$ the proper area per cut bond. **The dynamic variable is the network's combinatorics:** matter must change the bond count around itself. In $2+1$ dimensions that change is a disclination; in $3+1$, deficit angles on hinges (Regge 1961). The weights must follow, to stay locked.

The $3+1$ combinatorial step is now tested for a straight hinge (Section 4.4). Its entropy carries Jacobson's term at $85\%$ of the continuum value at $R\le7.5$, so the geometric half of the field equation holds in $3+1$. The matter half still rests on the lattice Bisognano–Wichmann check of Section 3.6.

### 5.3 Stability, and what moves

Second-order relative entropy is Fisher information (Proposition 2.6(a)), so entanglement equilibria are stable against first-order state perturbations [P for Gaussian states]. The induced free energy of the weights is concave (Proposition 2.5): matter softens the weights. With the measured induced Newton term about an order of magnitude below the area-law value, the weights' own gravitational response is subleading.

The network's dynamics is then:
- **combinatorial rewiring** that keeps every ball in entanglement equilibrium (gravity);
- **reactive propagation** on the weights (Paper 55's light cones).

The weights adjust to stay locked [C for the rewiring dynamics as a time-evolution law].

### 5.4 Outlook [C, fenced]

- **O1.** The $3+1$ Regge test at larger radii and for non-straight hinges (networks of hinges, the Regge form of a Newtonian mass). The straight hinge passes at $85\%$ (Section 4.4).
- **O2.** *(Done at 60 digits for $R_{\max}=26$ and $36$, Section 4.3.)* The point-mass law holds ($3$–$7\%$ over $R=6$–$12$), and the mass sits at $0.76$–$0.77$ of $\eta\delta c/2\pi$ in both boxes. Still open: the continuum limit of the apex modular-weight overshoot, and the same test for the $3+1$ cosmic string (Section 4.4).
- **O3.** Locking: is there a passive dynamics that drives weights to the combinatorial metric?
- **O4.** Whether the sub-leading induced term, with its $1/6$ zero, is the lattice image of the heat-kernel coefficient exactly.

In the architecture of the program, Paper 55's network layer now has a definite dynamic variable: geometry gravitates through combinatorics. In the Port Principle's phrase, gravity is where local passive ports fail to glue. On a network, the glue that gravitates is the bond count, not the bond strength.

---

## 6. Ledger

**Hypotheses and settlements.**

| Hypothesis | Settlement | Tier |
|---|---|---|
| metric dictionary, Weyl invariance at $\xi_c$, scale invisibility | Theorem 2.1, Corollaries 2.2–2.3 | [P] |
| classical modular Hamiltonian = Kron; mutual information = forest ratio | Proposition 2.4 | [P] |
| induced free energy concave; Foster = equipartition | Proposition 2.5 | [P] |
| first law, vacuum stationarity, Fisher stability | Proposition 2.6 | [P] |
| weights as gravitating geometry | **L_J0** in $3+1$ (volume term $4$–$9\%$ of target) and $2+1$ ($3\%$) | [numerics] |
| induced residue has the heat-kernel zero at $\xi\approx1/6$ | $\xi_0=0.164\pm0.017$ | [numerics, indicative] |
| entanglement counts bonds across curvature defects | D1, $0.5\%$ | [numerics] |
| combinatorial curvature = Jacobson's deficit term | D2, $0.93\to0.999$ ($2+1$); R5′ slope $0.85\pm0.03$ ($3+1$ hinge) | [numerics] |
| entanglement per bond does not see a $3+1$ hinge | R1, R2 | [numerics] |
| lattice Bisognano–Wichmann | $3+1$: $\le10\%$; $2+1$: $11\%$ at 60 digits (the float64 "failures" were clipping); flat triangular centre $11$–$21\%$ at $R_{\max}=26$, $9$–$13\%$ at $R_{\max}=36$ (60 digits; the growth with $R$ is mostly infrared) | [numerics] |
| disclination = point mass ($2+1$) | $-\delta S/\beta(0)$ independent of $R$ to $3.4\%$ ($R_{\max}=26$; K_M) and $6.6\%$ ($R_{\max}=36$) at 60 digits; value $0.76$–$0.77\times\eta\delta c/2\pi$ in both boxes (K_eta missed, retained) | [numerics]; continuum value [A] |
| $G=a_{\rm cell}/(4\eta_b)$; gravity is combinatorial | Section 5.2 | [A, conditional] |

**Certificate** `empirical/network56/p56_cert.py`: K/L pre-registered before run 1; post-diagnosis criteria written into the run log before each post-diagnosis run.

| Block | Result |
|---|---|
| E (exact) | 5/5 |
| V (validation) | 6/6 after the V3 checker artifact (run 1: 4/6, retained) |
| J2 | inconclusive (V5 gate; profile error) |
| J3 | L_J0, formally inconclusive (V5 at 0.100) |
| D | 3/5 (D3, D4 failed, retained; precision artifact per P5) |
| R ($3+1$ hinge, `p56b_regge_cert.py`) | 5/8 (R3–R5 pointwise failed, retained); post-diagnosis slopes 3/3 |
| P1, P2 (not blind) | L_J0 in both; P2 gate passed, P1 gate missed (10.2%) |
| P3 (not blind) | failed (box-independent deficit), explained by P5 |
| P4 (not blind) | run 3 void (checker artifact); run 4 failed (same clip) |
| P5 (not blind) | 1/1: the clip, confirmed at 60 digits |
| apex at 60 digits (`p56c_apex_mp_cert.py`) | 8/9: gates G1–G4 pass; K_BW and K_M pass; **K_eta failed (0.762), retained** |
| box size (`p56d_ir_check.py`, not blind) | $R_{\max}=26\to36$: flat overshoot at $R=12$ down $6.5\%$ (partly infrared); mass ratio $0.762\to0.772$ (stable) (Section 4.3) |

**Safe statements.**
- A fixed network's ball entanglement responds to curvature written into its weights at area order.
- Entanglement per bond does not see curvature defects.
- A disclination changes entanglement by $\eta_b$ times its bond deficit.
- With the lattice's own modular Hamiltonian, entanglement equilibrium at the apex assigns a disclination one mass, independent of the ball radius (60 digits, $2+1$).
- Matter's modular energy is Bisognano–Wichmann in $3+1$ on the lattice.

**Unsafe statements.**
- "The network derives Einstein's equation." The $3+1$ hinge test covers the geometric half for one straight hinge, at $85\%$. The matter half is tested only in $2+1$, where it gives a point mass at $0.76$–$0.77$ of the continuum value. The $3+1$ matter half and general hinge networks are untested.
- "Disclinations are quantized masses with the continuum value." At 60 digits a disclination is a point mass, nearly independent of the ball radius, but its value is $0.76$–$0.77$ of $\eta\delta c/2\pi$ at these sizes, in two box sizes.
- "The induced term is exactly the heat-kernel one." The fit uncertainty is $40$–$70\%$.

---

## References

- J. J. Bisognano, E. H. Wichmann, On the duality condition for a Hermitian scalar field, *J. Math. Phys.* 16 (1975) 985.
- D. D. Blanco, H. Casini, L.-Y. Hung, R. C. Myers, Relative entropy and holography, *JHEP* 08 (2013) 060.
- C. Eling, R. Guedens, T. Jacobson, Nonequilibrium thermodynamics of spacetime, *Phys. Rev. Lett.* 96 (2006) 121301.
- S. Deser, R. Jackiw, G. 't Hooft, Three-dimensional Einstein gravity: dynamics of flat space, *Ann. Phys.* 152 (1984) 220.
- J. Eisert, M. Cramer, M. B. Plenio, Area laws for the entanglement entropy, *Rev. Mod. Phys.* 82 (2010) 277.
- T. Faulkner, M. Guica, T. Hartman, R. C. Myers, M. Van Raamsdonk, Gravitation from entanglement in holographic CFTs, *JHEP* 03 (2014) 051.
- T. Jacobson, Thermodynamics of spacetime: the Einstein equation of state, *Phys. Rev. Lett.* 75 (1995) 1260.
- T. Jacobson, Entanglement equilibrium and the Einstein equation, *Phys. Rev. Lett.* 116 (2016) 201101.
- N. Lashkari, M. Van Raamsdonk, Canonical energy is quantum Fisher information, *JHEP* 04 (2016) 153.
- T. Regge, General relativity without coordinates, *Nuovo Cimento* 19 (1961) 558.
- A. D. Sakharov, Vacuum quantum fluctuations in curved space and the theory of gravitation, *Dokl. Akad. Nauk SSSR* 177 (1967) 70.
- S. N. Solodukhin, Entanglement entropy of black holes, *Living Rev. Relativ.* 14 (2011) 8.
- R. D. Sorkin, Causal sets: discrete gravity, in *Lectures on Quantum Gravity*, Springer, 2005.
- M. Srednicki, Entropy and area, *Phys. Rev. Lett.* 71 (1993) 666.
- A. Staruszkiewicz, Gravitation theory in three-dimensional space, *Acta Phys. Polon.* 24 (1963) 735.
- L. Susskind, J. Uglum, Black hole entropy in canonical quantum gravity and superstring theory, *Phys. Rev. D* 50 (1994) 2700.
- M. Visser, Sakharov's induced gravity: a modern perspective, *Mod. Phys. Lett. A* 17 (2002) 977.
- Program: Paper 55 (Theorems 2.2, 3.5, 4.2; Corollary 4.3; O1); PortPrinciple.md (Section 14; Corollary 6.13); Paper 54 (Theorem 1); Paper 35 (the GPD method); Pinf-WhatIsMultiplicative.
