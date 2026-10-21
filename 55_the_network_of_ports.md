# 55 — The Network of Ports: Space, Light Cones, and Area Laws from Passive Composition

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*Draft 2 — October 2, 2026*

<!--
INTERNAL LOG — NOT FOR PUBLICATION (pandoc drops HTML comments)
2026-10-01 v0.1. Construction paper: the program's missing spatial layer (Layer II/III spatial half of the
2026-10-01 architecture). Session prompt: PROMPT_network_of_ports.md. Breaks two of the three negatives it was given
(Paper 32 Sec. 14.2 Lorentzian; Paper 32.1 Sec. 7 area law) at the network level and partially breaks the third
(Paper 32 gap G3). Excluded by design from the technical body: RH, consciousness, the finite-grid thesis; the
Occupation Thesis appears once, fenced, in Sec. 7.2.
Certificate: empirical/network55/p55_cert.py (K/L pre-registered in its docstring before run 1).
  Run 1 = run 2: 25/29 pre-registered PASS. Retained failures: K1a (L-control masked: an active two-port inside a
  passive network left the composite passive), K2d (pre-registered MONOTONE finite-t deviation; limit holds),
  K3d C2 (wrong analytic expectation for all-to-all MI; it obeys the cut law), K6 (the handed-over isotropy claim;
  K6', written from a hand expansion before the run, predicted the failure exactly).
  Post-diagnosis, NOT BLIND, criteria fixed before run 2: K1a', K2d', K3d' 3/3.
  Run 3: checker hygiene only (removed sp.nsimplify on exact rationals in the K1d helper); all lines identical.
Forward pointers added (one line each) to the internal logs of Papers 32, 32.1, 46.
FWD (2026-10-01) -> Paper 56 (56_the_dynamic_network.md) addresses O1: weights do not gravitate (Jacobson volume term
  4-9% of target, area-order response); entanglement counts bonds and a disclination realizes Jacobson's deficit term;
  gravity is combinatorial (bond count), causality is in the weights.
2026-10-02 v0.2 (gap closures; Paper 57 synthesis pass):
  - NEW Sec. 3.8, Theorem 3.8 (storage order): a cone iff exactly one of the two conjugate storages is ultralocal and the
    other gradient; both gradient = Schrodinger (no signal speed); Maxwell's vacuum = ultralocal electric + curl-curl
    magnetic storage, c = 1/sqrt(mu0 eps0), Z0 = 376.73 Ohm.  Links the Port Principle's base lift (a lossless
    ledger is rotations between two storages; Foster) to the network cone.
  - NEW Sec. 6.5, Theorem 6.6 + Lemma 6.7: CLOSES O2.  Fourth-order isotropy needs >= 7 bond pairs in d = 3 (six would
    have to lie along the icosahedral axes, which no lattice contains); sc + bcc at 8:1 (z = 14, the D3Q15 stencil)
    attains it; sc + fcc at 2:1 (D3Q19); fcc + bcc never; d = 2 triangular (z = 6).  Credit: lattice Boltzmann
    (Qian-d'Humieres-Lallemand 1992) for the stencils; Haantjes / Lemmens-Seidel for equiangular lines; new here =
    minimality.
  - Sec. 7.1 [C] reading CORRECTED (and Sec. 5 reading): the cycle lattice H_1 (arrow, holonomy) and the spacing module
    M of mode frequencies (echo arithmetic) are different lattices (5-ring: b_1 = 1, rank M = 2).  A peer review of the
    program had built a "holographic boundary principle" on the conflation; rejected, and the fenced sentence that
    invited it is fixed.
  - Certificate empirical/network55/p55b_storage_isotropy_cert.py: run 1 8/9 (S1 failed on a CHECKER ARTIFACT:
    sympy did not cancel 16 sin^4(kl/2) - (2 - 2 cos kl)^2; every pre-registered value passed; retained); run 2 9/9
    (not blind for the repaired checker).
-->

---

## Abstract

Everything the program has built so far lives on *one* finite system: a categorical simplex, its Fisher sphere, its cumulant tower. Three earlier results say that physical space cannot live there. A single simplex's Bures lift is Euclidean (Paper 32, Sec. 14.2). Its "boundary" is an arithmetic locus, with no geometric area law (Paper 32.1, Sec. 7). Its "experienced space" is a closure-valid block, not a reconstruction of physical space (Paper 32, gap G3). We take the three negatives as targets and build the missing layer: **a network of ports**. Nodes are finite systems. Edges are passive ports joined by Kirchhoff's laws. The network's graph Laplacian, discrete exterior calculus and cycle space are the candidate geometry, tested three ways — by a light cone, by a cut, and by loops.

**Composition (Sec. 2) [P].** Kirchhoff composition of passive ports is a passive multiport, and the network admittance is a weighted graph Laplacian. Kirchhoff's current law is the Noether identity of the potential shift $\varphi\mapsto\varphi+c\mathbf 1$, whose generator is the program's gauge line $\ker d_0=H^0$. For the complete network on four vertices the admittance is $4I-J$, the frame metric of Paper 01. The converse of composition fails: an active port can be masked by passive neighbours (a retained certificate failure).

**Light cones (Sec. 3) [P].** The second-order symbol of a network equation is $C\omega^2-k^{\mathsf T}Ak$. It is Lorentzian, of signature $(1,d)$, exactly when the nodes store energy capacitively ($C>0$), the links store it inductively, and the link stiffness is passive ($A\succ0$). Loss is lower order: it keeps the cone and turns ballistic transport ($c^2t^2$) diffusive ($2Dt$) after the loss time. An RC network has no time direction, an isolated node has no space, and an active link adds a second timelike direction, which is exponential growth. In continuous time the LC front is a Debye front at the maximal group velocity $c=1/\sqrt{LC}$, with super-exponential tails; strict discrete cones are stencil artefacts that diffusion shares. A single lossless port is a one-dimensional LC line (Cauer), so one port carries at most a canonical line. Where the two storages sit decides the physics. One ultralocal and one gradient storage give a cone. Both gradient give Schrödinger's equation, which has no signal speed. Maxwell's vacuum is of the first kind, and $c=1/\sqrt{\mu_0\varepsilon_0}$ is its LC speed (Theorem 3.8). The network form and the multiplicative intersection form of Pinf-WhatIsMultiplicative are two Lorentzian forms of one *type*: each has a complement whose definiteness is a passivity condition. They are not the same form.

**Area law and capacity (Sec. 4) [P].** For every Gibbs state, $I(A{:}B)+D(\rho_A\otimes\rho_B\Vert\rho)=\beta\big(\langle H_\partial\rangle_{\rho_A\otimes\rho_B}-\langle H_\partial\rangle_\rho\big)$. Hence for harmonic networks of passive ports $I(A{:}B)\le\beta\sum_{e\in\partial A}w_eX_{ij}$, a cut law, which on a lattice is an area law. The bound holds exactly, and exact-covariance numerics on chain, square, cubic and diamond lattices give $I/|\partial A|$ constant to within $3\%$. Two long-range controls violate the *geometric* area law and obey the *cut* law. Information flow across a cut is bounded by the sum of the cut ports' capacities. That bound is attained by max-flow/min-cut, and for multicast it needs network coding. Each port's capacity is set by its thermal defect noise, or by the Bekenstein–Pendry bound $\dot S\le\sqrt{\pi P/3\hbar}$. Per-port additivity requires independent hidden ports.

**The arrow (Sec. 5) [P].** Stationary currents live in the cycle space, of dimension $b_1$. Entropy production is the pairing of the affinity class in $H^1$ with the current in $H_1$. Trees carry no current. A circulating current is not an arrow by itself; dissipation needs a nonzero affinity in the loop. A lossless five-node ring has golden frequency ratio and echoes at Fibonacci times.

**Which network (Sec. 6) [P].** An isotropic sound speed needs a centred bond star with at least $d+1$ bonds. With $d+1$ bonds the star is a regular simplex, whose Gram matrix for $d=3$ is the frame metric $4I-J$. So four-valent tetrahedral coordination is singled out at second order. At fourth order it is not: the coefficient handed to this session, $\ell^2k^2/36$ ($\tilde\eta=1/72$), holds only along the cube axes, and the anisotropy between $\langle111\rangle$ and $\langle100\rangle$ is exactly $7/3$. Two shells cure the anisotropy. Simple-cubic plus body-centred bonds with weights $8{:}1$ are isotropic through fourth order. Fourteen bonds is the least possible, because six bond pairs would have to lie along the icosahedron's axes, which no lattice contains (Theorem 6.6). Four-valent elastic networks are floppy. The four-valent network is the dual 1-skeleton of a tetrahedral cell complex, whose top Hodge Laplacian is its graph Laplacian.

**Verdict.** The Lorentzian and area-law negatives hold for one node and break for networks. The third negative breaks partially. A network supplies a cone, cuts, and an arrow; it does not select its own dimension, and nothing here gives the network dynamics. Certificate: 25 of 29 pre-registered checks pass, the four failures are retained, and 3 of 3 post-diagnosis checks (not blind) pass. A second certificate, for storage order and isotropy, passes 9 of 9 on its second run; its first run failed on a checker artifact, which is retained.

---

## 1. Why one simplex cannot be space

### 1.1 Three negatives

The program's objects so far are attached to a single finite system: the categorical simplex $\Delta_Q$ of a $Q$-outcome node, its Fisher (and Bures) metric, its cumulant tower, and its conductor arithmetic. Three earlier results mark the limit of that arena as a model of physical space.

1. **No Lorentzian signature at the manifold level.** Paper 32 (Sec. 14.2) lifted the energy to $\operatorname{tr}(H\rho)$ on $D(\mathbb C^2\otimes\mathbb C^3)$ and asked for a two-sheeted hyperboloid. The level sets are compact, the Bures metric at the centroid is $3\cdot I_8$, and the centralizer is a compact torus. The verdict was Euclidean-4.
2. **No geometric area law.** Paper 32.1 (Sec. 7) found that the boundary carrying the closure residual is the unit group $(\mathbb Z/N)^\times$, a boundary in the divisor poset. Its share follows $\prod_{p\mid N}(1-1/p)$, not a codimension-one area exponent, and no metric rescues it at the saturating centroid.
3. **No physical-space reconstruction.** Paper 32 (gap G3) concedes that "experienced space" is the closure-valid block, "not yet a physical-space reconstruction".

### 1.2 The common cause

All three negatives are statements about one node. A light cone is a property of a *propagation equation*: a characteristic surface in the cotangent space of space-time. An area law is a property of a *bipartition by a cut*. A topological arrow is a property of *loops*. A single node has no spatial index, so its equation of motion has no spatial derivatives. Its bipartitions are tensor factorizations of one Hilbert space, with no notion of where the cut runs. It has no loops.

**Proposition 1.1 (one node is ultralocal) [P].** Let a node's dynamics be any linear second-order system $C\ddot x+\Gamma\dot x+Kx=0$ on its internal coordinates. Its symbol $C\omega^2-i\omega\Gamma-K$ depends on no wavevector. Its characteristic set $\{\det(C\omega^2)=0\}$ is $\{\omega=0\}$ for $C\succ0$, so it has no cone through spatial directions. Any Riemannian metric on the node's state space — Fisher, Bures, or any monotone metric — is a metric on states, not a propagation symbol.

*Proof.* There is no spatial variable to Fourier transform. The second-order symbol is $C\omega^2$, positive definite in $\omega$ and independent of everything else. $\square$

**Remark 1.2 (the local $(1,3)$ of Paper 46) [P for the lemma, A for the reading].** Paper 46 reports a Lorentzian $(1,3)$ sub-bundle in the Hessian at $\rho_*=I/6$ of the Casimir $I_{\rm complex}=\langle H\rangle^2+\alpha^2(m^2)^2-\sum_{a=1}^3\langle P_a\rangle^2$, with $H,P_a$ traceless on the single-prime sector. The signature is the one written into the Casimir. Expectation values $f(\rho)=\operatorname{tr}(F\rho)$ are affine in $\rho$, so for affine $f_0,f_1,\dots,f_m$ with linearly independent gradients, the Hessian of $f_0^2-\sum_af_a^2$ is $2\,(\nabla f_0\otimes\nabla f_0-\sum_a\nabla f_a\otimes\nabla f_a)$ at *every* point. Its signature is $(1,m)$ on the span of the gradients and $0$ elsewhere, whatever the $f$'s are. This also explains why the pattern is "exact along rays to all orders". Paper 46's $(1,3)$ is therefore the signature of the quadratic form $\mathrm{diag}(1,-1,-1,-1)$ chosen to define $I_{\rm complex}$, pulled back by an injective linear map. It is consistent, but it is an input and not an output. Section 3 finds a signature that is an output.

### 1.3 What this paper builds, and what is new

A **network of ports** joins many nodes by passive ports under Kirchhoff's laws. We test whether its combinatorial geometry — graph Laplacian, discrete exterior calculus (DEC), Hodge theory, Betti numbers — behaves as space in three ways: a light cone (Sec. 3), area laws for cuts (Sec. 4), and an arrow on loops (Sec. 5). Section 6 asks which network, and Section 7 is a fenced outlook.

**Prior art, credited.** Every ingredient below is classical:
- Kirchhoff (1847) and Tellegen (1952);
- Kron reduction (Kron 1939; Dörfler–Bullo 2013);
- Foster (1924), Cauer (1926), Brune (1931) and Darlington (1939) synthesis;
- Willems' dissipativity (1972);
- port-Hamiltonian systems, in particular on graphs (van der Schaft–Maschke 2013);
- compositional passive networks (Baez–Fong 2018);
- lattice dispersion (Brillouin 1946) and Lieb–Robinson bounds (1972);
- thermal and harmonic area laws (Wolf–Verstraete–Hastings–Cirac 2008; Cramer–Eisert 2006; Hastings 2007; Eisert–Cramer–Plenio 2010);
- the ground-state entanglement area law for two-dimensional gapped finite-range Hamiltonians, with polynomial-bond-dimension PEPS approximation (OpenAI 2026, `github.com/openai/math`, family 265; model-generated; cited at tier [A]).  This paper's area laws are the thermal (Gibbs) and harmonic cases.  The gapped ground-state theorem has a different hypothesis.  It is cited and not used.
- max-flow/min-cut and network coding (Ford–Fulkerson 1956; Elias–Feinstein–Shannon 1956; Ahlswede–Cai–Li–Yeung 2000);
- information-flow bounds (Bekenstein 1981; Pendry 1983);
- Schnakenberg's cycle theory (1976) and Kolmogorov's criterion (1936);
- spherical designs (Delsarte–Goethals–Seidel 1977) and Maxwell counting (Maxwell 1864; Calladine 1978);
- DEC and FEEC (Desbrun–Hirani–Leok–Marsden 2005; Arnold–Falk–Winther 2006).

**Relation to port-Hamiltonian theory.** The closest existing framework is port-Hamiltonian theory on graphs. It already has Kirchhoff's laws as a Dirac structure built from the incidence matrix, passivity of interconnection, and Kron-type reduction. What this paper adds is:
1. reading the network as a candidate *physical space*, judged by three tests and settled with tiers;
2. the signature theorem for the network symbol, stated in passivity terms and compared with the multiplicative intersection form (Theorem 3.5, Sec. 3.6);
3. the thermal cut law written as an identity with an exact relative-entropy slack, its harmonic-network instance, and the two caveats found by the certificate (masking; correlated hidden ports) (Theorem 4.2, Corollary 4.3, Theorem 4.4);
4. the result that the minimal isotropic bond star is the regular simplex, whose Gram matrix is the program's frame metric, together with the fourth-order anisotropy settlement (Theorems 6.1, 6.2);
5. the readings "one port is one line" (Cauer) and "the four-valent network is the dual of a tetrahedral complex" (Propositions 3.7, 6.5);
6. the storage-order theorem: a cone exactly when one storage is ultralocal and the other gradient, Schrödinger's equation when both are gradient, and Maxwell's vacuum as a network of the first kind (Theorem 3.8);
7. the least coordination with fourth-order isotropic dispersion: fourteen bonds in three dimensions, because six bond pairs would have to be icosahedral (Theorem 6.6, Lemma 6.7).

The individual arguments are short. The contribution is the settlement, the organization, and exact certificates (Sec. 8).

**Tiers.** **[P]** proven here (finite and exact, certified wherever a computation is involved) or a cited theorem used as stated. **[A]** a structural identification or standard physical argument not proven here. **[C]** conjectural, fenced, no evidentiary weight.

---

## 2. Networks of ports: composition

### 2.1 Definitions

**Definition 2.1 (network of ports).** A *network of ports* consists of:
- a finite graph $G=(V,E)$ with oriented edges, and its coboundary $d_0:\mathbb C^V\to\mathbb C^E$, $(d_0\varphi)_e=\varphi_j-\varphi_i$ for $e=(i\to j)$;
- at each edge a passive port. A *one-port* has admittance $y_e(s)$: holomorphic on $\operatorname{Re}s>0$, with $\operatorname{Re}y_e\ge0$ there. A *two-port* has a $2\times2$ admittance $Y_e(s)$ between the node potentials of its endpoints, referenced to a common ground, whose Hermitian part is positive semidefinite on $\operatorname{Re}s>0$;
- optionally, a passive shunt $y_v(s)$ from each node to ground.

The node potentials $\varphi$ determine the edge efforts $v=d_0\varphi$ (Kirchhoff's voltage law). Edge flows $i\in\mathbb C^E$ and external injections $j$ satisfy $j=d_0^{\mathsf T}i+\operatorname{diag}(y_v)\varphi$ (Kirchhoff's current law).

### 2.2 Composition

**Theorem 2.2 (composition) [P].**
- **(a) Tellegen.** For every $\varphi\in\mathbb C^V$ and every $i\in\mathbb C^E$, $\langle d_0\varphi,i\rangle=\langle\varphi,d_0^{\mathsf T}i\rangle$: the power delivered to the edges equals the power injected at the nodes.
- **(b) Laplacian and passivity.** With one-port edges, the network admittance is
  $$Y(s)=d_0^{\mathsf T}\operatorname{diag}\big(y_e(s)\big)\,d_0+\operatorname{diag}\big(y_v(s)\big),$$
  a weighted graph Laplacian plus shunts. With two-port edges it is $Y(s)=\sum_eP_e^{\mathsf T}Y_e(s)P_e$, where $P_e$ selects the endpoints. In both cases
  $$\operatorname{Re}\langle\varphi,Y(s)\varphi\rangle=\sum_e\operatorname{Re}\langle P_e\varphi,Y_e(s)P_e\varphi\rangle\ \ge0\qquad(\operatorname{Re}s>0),$$
  so $Y$ is a positive-real multiport. If every element is lossless ($y_e(i\omega)\in i\mathbb R$), then $Y(i\omega)$ has zero Hermitian part.
- **(c) Kron reduction.** For a partition $V=B\sqcup I$ with $Y_{II}(s)$ invertible, the Schur complement $Y_B=Y_{BB}-Y_{BI}Y_{II}^{-1}Y_{IB}$ is positive-real. It is the admittance seen at $B$ when the interior injections vanish.
- **(d) The converse fails.** A composite can be passive while containing an active element.

*Proof.* (a) is the definition of the transpose. (b) Expand the quadratic form edge by edge; each term has nonnegative real part by Definition 2.1. (c) Put $\varphi_I=-Y_{II}^{-1}Y_{IB}\varphi_B$. Then $Y(\varphi_B,\varphi_I)=(Y_B\varphi_B,0)$, so $\langle\varphi_B,Y_B\varphi_B\rangle=\langle\varphi,Y\varphi\rangle$, whose real part is $\ge0$ by (b). (d) Certificate K1a′ gives a witness. $\square$

Certificates:
- **K1a:** three random networks of random RLC two-ports $Y_e=G_e+sC_e+\Gamma_e/s$ ($G,C,\Gamma\succeq0$, rational). The full and the Kron-reduced Hermitian parts are PSD at five points of $\operatorname{Re}s>0$, in exact arithmetic.
- **K1a's L-control failed**, and the failure is retained. Replacing one $G_e$ by $\operatorname{diag}(1,-3)$, an active two-port, left the composite passive at all five points: the passive neighbours *masked* the active element.
- **K1a′** (post-diagnosis, not blind): the element alone is active, the composite is passive at 5 of 5 points, and a strong element $\operatorname{diag}(1,-100)$ is flagged at 5 of 5. Passivity of a whole does not certify its parts. This is the Port Principle's boundary rule (PortPrinciple.md, Definition 2.5) seen from inside: a boundary that encloses the source can be passive.

**Proposition 2.3 (Kirchhoff's current law is a Noether identity) [P].** Take an LC network with node capacitances $C_v$ to ground and inductive links $L_e$, without shunt inductors. In flux coordinates (node voltage $\dot\varphi_v$), its Lagrangian is
$$\mathcal L=\tfrac12\sum_vC_v\dot\varphi_v^2-\tfrac12\sum_eL_e^{-1}(d_0\varphi)_e^2 .$$
It is invariant under the potential shift $\varphi\mapsto\varphi+c\mathbf 1$, because $d_0\mathbf 1=0$. The Noether charge of that shift is $\sum_v\partial\mathcal L/\partial\dot\varphi_v=\sum_vC_v\dot\varphi_v$, the total node charge. Its conservation is the sum over nodes of the equations of motion $C_v\ddot\varphi_v=-(d_0^{\mathsf T}L^{-1}d_0\varphi)_v$, i.e. of Kirchhoff's current law. Each node's equation is the local form, a continuity equation. Without shunts, $Y(s)\mathbf 1=0$ and $\mathbf 1^{\mathsf T}Y(s)=0$ for every $s$. A shunt to ground (a mass term) breaks the symmetry.

The generator $\mathbf 1$ spans $\ker d_0=H^0(G)$. That is the program's gauge line (Paper 01b, Theorem 10.1(2); Paper 01d, Theorem 2.1). On a network, the gauge line acquires a dynamical meaning: its Noether charge is total charge. *Proof:* direct. *Certificate K1b* (exact, symbolic in $s$): $Y=d_0^{\mathsf T}\operatorname{diag}(y)d_0$ equals the stamped Laplacian, $d_0\mathbf 1=0$, $\mathbf 1^{\mathsf T}Y=0$, and Tellegen holds. $\square$

**Corollary 2.4 (the tetrahedron) [P].** Give the complete graph $K_N$ unit conductances. Its admittance is $NI-J$, and the effective resistance between any two vertices is $2/N$. For $N=4$ the admittance is $4I-J$: the integer frame metric of Paper 01 (Paper 01b, Theorem 10.1(1); Paper 01d, Theorem 2.1; forward1). So the program's metric is the admittance matrix of the complete resistor network on the frame's vertices.

*Proof.* $d_0^{\mathsf T}d_0$ has diagonal $N-1$ and off-diagonal entries $-1$. On $\mathbf 1^\perp$ it acts as $N$, so its pseudo-inverse is $\frac1N(I-J/N)$, and $(e_i-e_j)^{\mathsf T}L^+(e_i-e_j)=2/N$. *Certificate K1c,* $N=3,\dots,7$. $\square$

**Proposition 2.5 (the defect Gram of a network port) [P].** Kron-reduce a passive network to a single node. Its driving-point admittance $y(s)$ has positive semidefinite Pick matrices $\big[(y(s_j)+\overline{y(s_k)})/(s_j+\bar s_k)\big]$. The Pick matrix is the defect Gram of Paper 53 (Lemma 3.2), and its rank counts the minimal ledger (Paper 53, Corollary 4.1). *Certificate K1d:* six points, PSD exactly. A shunt of conductance $-100$ at the port makes the matrix indefinite. $\square$

---

## 3. Light cones from reactive networks

### 3.1 Dispersion

Work in lattice units on the one-dimensional chain: node capacitance $C$ to ground, and links with a series inductor $L$ and possibly a series resistor $R$. Put $c=1/\sqrt{LC}$, $D=1/(RC)$ and $\gamma=R/L$. Eliminating the link currents gives, at every node,
$$LC\,\ddot V_n+RC\,\dot V_n=V_{n+1}-2V_n+V_{n-1}.$$
The **LC chain** is the case $R=0$, the **RC chain** the overdamped case $L=0$, and the **RLC chain** is the telegraph equation on the lattice.

**Theorem 3.1 (dispersion) [P].**
- **LC:** $\omega^2=\frac4{LC}\sin^2\frac k2$, and the group velocity is $\cos(k/2)/\sqrt{LC}\le c$, with equality only at $k=0$.
- **RC:** the Bloch exponent $s(k)=-\frac4{RC}\sin^2\frac k2$ is real and $\le0$: no Bloch mode propagates.
- **General Bravais network:** with node storage $C$ and link weights $w_e$ (inverse inductances) along bond vectors $\delta_e$,
  $$\omega^2(k)=\frac1C\sum_e2w_e\big(1-\cos k\cdot\delta_e\big).$$

*Certificate K2a (exact, symbolic).* $\square$

### 3.2 Ballistic versus diffusive transport

**Theorem 3.2 (spreading of the impulse response) [P].** Let $G_n(t)$ be the response to a unit displacement at the origin. Its generating function $F(k,t)=\sum_nG_n(t)e^{ikn}$ has the following closed forms and mean-square displacements $\mathrm{MSD}(t)=\sum_nn^2G_n(t)=-\partial_k^2F|_{k=0}$:

| Network | $F(k,t)$ | MSD |
|---|---|---|
| LC | $\cos\!\big(2ct\sin\tfrac k2\big)$ | $c^2t^2$ (ballistic) |
| RC | $\exp\!\big(-2Dt(1-\cos k)\big)$ | $2Dt$ (diffusive) |
| RLC | — | $\dfrac{2c^2}{\gamma}\Big(t-\dfrac{1-e^{-\gamma t}}{\gamma}\Big)$ |

For RLC, the MSD equals $c^2t^2+O(t^3)$ for $t\ll1/\gamma$ and $2Dt-2D/\gamma+o(1)$ for $t\gg1/\gamma$. Here $D=c^2/\gamma$, so the RC chain is the overdamped limit $L\to0$ at fixed $R$ and $C$, in which $c\to\infty$ with $D$ fixed.

*Proof.* $F$ solves the Bloch ODE with $F(k,0)=1$ and $\partial_tF(k,0)=0$. Differentiating the RLC equation twice in $k$ at $k=0$ gives $\ddot m+\gamma\dot m=2c^2$ with $m(0)=\dot m(0)=0$. *Certificate K2b.* $\square$

*Reading.* Loss does not remove propagation. It converts bulk transport inside the cone from ballistic to diffusive after the loss time $1/\gamma$. Diffusion's infinite speed is the limit of vanishing inductance.

### 3.3 Fronts: what is, and what is not, a strict cone

**Theorem 3.3 (fronts in continuous time) [P, with Bessel and Debye asymptotics cited].**
- **(a)** For the LC chain, $G_n(t)=J_{2|n|}(2ct)$.
- **(b) Lieb–Robinson-type bound.** $|G_n(t)|\le(ct)^{2|n|}/(2|n|)!\le\big(ect/2|n|\big)^{2|n|}$, so the response is super-exponentially small for $|n|>ect/2$.
- **(c) No strict cone.** $G_n(t)>0$ whenever $|n|>ct$, because the first positive zero of $J_\nu$ exceeds $\nu$. For example $G_{60}(50)=1.15\times10^{-5}$ at $c=1$, velocity $1.2c$.
- **(d) The front.** At fixed velocity $v=n/t$ the decay rate $r(v)=-\lim t^{-1}\ln|G_{vt}(t)|$ is
  $$r(v)=0\ \ (|v|\le c),\qquad r(v)=2v\operatorname{arccosh}\frac vc-2\sqrt{v^2-c^2}\ \ (|v|>c).$$
  The front moves at the maximal group velocity $c$. This is sharper than the bound in (b), whose velocity is $(e/2)c$.
- **(e) RC.** $G_n(t)=e^{-2Dt}I_n(2Dt)>0$ for every $n$ and every $t>0$, so the support is unbounded at once. Its rate $r_{\rm RC}(v)=2D-\sqrt{v^2+4D^2}+v\operatorname{arsinh}\frac v{2D}$ is positive for every $v\ne0$.

The **zero-rate velocity set** is $[-c,c]$ for LC and $\{0\}$ for RC. That set is the network's light cone.

*Proof.* (a) $\cos(z\sin\theta)=J_0(z)+2\sum_{m\ge1}J_{2m}(z)\cos2m\theta$. (b) uses $|J_\nu(x)|\le(x/2)^\nu/\Gamma(\nu+1)$. (d) is Debye's expansion $J_\nu(\nu\operatorname{sech}\alpha)\sim e^{\nu(\tanh\alpha-\alpha)}/\sqrt{2\pi\nu\tanh\alpha}$, with $\nu=2vt$ and $\cosh\alpha=v/c$, together with the oscillatory regime for $v<c$ (DLMF 10.19). (e) $e^{z\cos k}=\sum_nI_n(z)e^{ikn}$, plus the uniform expansion of $I_\nu(\nu z)$ (DLMF 10.41). $\square$

**Certificate K2d** (50 digits):
- The ODE and generating-function residuals are below $10^{-50}$, and the bound in (b) holds on a grid.
- $r(1.2c)$ measured at $t=400$ is $0.16789$, against $0.16702$.
- $r(0.8c)=0.0083$. The RC rate at $v=0.8$ is $0.1658$, against $0.1580$.
- **Pre-registered failure, retained:** a *monotone* decrease of $|r(t)-r^*|$ over $t\in\{50,100,200,400\}$. The measured sequence was $0.0103$, $0.0027$, $0.00013$, $0.00087$. The $\pm3$ window used in the measurement lowers the rate by about $2\operatorname{arccosh}(v)\cdot3/t$, and the Debye prefactor raises it by about $\ln\sqrt{2\pi\nu\tanh\alpha}/t$. The two biases cross between $t=200$ and $t=400$.
- **K2d′** (post-diagnosis, not blind) measures without the window, at $n=1.2t$ exactly. There $|G|/(\text{Debye leading term})-1$ equals $0.0041$, $0.0021$, $0.0010$ and $0.00052$ for $t=100,200,400,800$. It halves as $t$ doubles, and the first Debye correction $u_1(\coth\alpha)/\nu$ is confirmed.

**Proposition 3.4 (strict discrete cones are stencil artefacts) [P].** Discretize time.
- Leapfrog for LC with Courant number $\lambda\le1$ and explicit Euler for RC with $\mu=D\Delta t/\Delta x^2\le\tfrac12$ *both* vanish exactly outside $|n|\le m$ after $m$ steps.
- They differ in MSD, exactly: $\lambda^2m^2$ against $2\mu m$.
- They differ in the continuum limit. The discrete cone speed is $\Delta x/\Delta t=c/\lambda$ for LC, which stays finite, and $D/(\mu\Delta x)$ for RC, which tends to $\infty$.
- At the magic step $\lambda=1$, leapfrog is exactly dispersionless: $\varphi^m=\tfrac12(\delta_m+\delta_{-m})$.

*Proof.* Each update has a nearest-neighbour stencil. The MSD recursion is $b_{m+1}=2b_m-b_{m-1}-2\lambda^2$, with $b_0=0$ and $b_1=-\lambda^2$. *Certificate K2c* (exact rationals, $\lambda^2\in\{1,\tfrac14\}$, $\mu\in\{\tfrac12,\tfrac14\}$). $\square$

So a strict cone in a cellular or quantum-circuit sense is a property of locality and discrete time, which diffusion shares. The discriminator is the continuum limit, Theorem 3.3(d).

### 3.4 The signature of a network

Pass to the continuum limit of a Bravais network: $C\,\partial_t^2\varphi+\Gamma\,\partial_t\varphi+m^2\varphi-\nabla\!\cdot(A\nabla\varphi)=0$, with
$$A=\sum_ew_e\,\delta_e\delta_e^{\mathsf T}\quad(\text{per cell}).$$
Its **second-order (principal) symbol** is the quadratic form
$$\sigma_2(\omega,k)=C\omega^2-k^{\mathsf T}Ak\qquad\text{on }(\omega,k)\in\mathbb R^{1+d}.$$

**Theorem 3.5 (the signature of a network) [P].**
- **(a) Lorentzian.** If $C>0$ (capacitive storage at the nodes) and $A\succ0$ (inductive storage on passive links whose bond vectors span $\mathbb R^d$), then $\sigma_2$ has signature $(1,d)$. Its null cone $\omega^2=k^{\mathsf T}Ak/C$ is the characteristic cone, with direction-dependent speed $c(\hat k)=\sqrt{\hat k^{\mathsf T}A\hat k/C}$. Solutions have finite propagation speed $\max c(\hat k)$ (energy estimate for hyperbolic systems; Courant–Hilbert). Loss $\Gamma\succeq0$ and mass $m^2\ge0$ are lower order and change neither $\sigma_2$ nor the cone.
- **(b) No inductance (RC).** The equation is first order in time, so $\sigma_2=-k^{\mathsf T}Ak$, of signature $(0,1,d)$. Time is degenerate, the equation is parabolic, and the speed is infinite.
- **(c) No links (an isolated node).** $\sigma_2=C\omega^2$, of signature $(1,d,0)$: no spatial direction and no cone (Proposition 1.1).
- **(d) An active link.** If $A$ is indefinite because some $w_e<0$, then $\sigma_2$ has signature $(1+p,\,d-p)$ with $p\ge1$, and $\omega^2(\varepsilon k)<0$ for small $\varepsilon$ along any $k$ with $k^{\mathsf T}Ak<0$. *Gain is a second timelike direction*: an exponentially growing mode. In a cell with several nodes, the number of growing Bloch modes at $k$ equals the number of negative eigenvalues of the stiffness matrix $K(k)$ (Sylvester's law of inertia).

*Proof.* Each case is a congruence class of quadratic forms. For (d), expand $1-\cos x=x^2/2+O(x^4)$ in Theorem 3.1. *Certificate K2f* (exact signatures, Sylvester/Descartes), on a square lattice with $C=1$, $w=(1,2)$:
- LC and RLC: $(1,0,2)$;
- RC: $(0,1,2)$;
- isolated node: $(1,2,0)$;
- active link $w_y<0$: $(2,0,1)$, with $\omega^2(0,\pi/2)=-2$. $\square$

**Remark 3.6 (what loss and mass do).**
- *Loss* keeps the cone (the telegraph equation has finite speed) and damps transport inside it (Theorem 3.2).
- *Mass* — a node shunt inductor $L_0$, with $m^2=1/(L_0C)$ — gives $\omega^2=m^2+\frac4{LC}\sin^2\frac k2\approx m^2+c^2k^2$. For $ck\ll m$ this is $\omega\approx m+c^2k^2/2m$: the Galilean paraboloid of Paper 32 (Lemma 9.2) is the small-$k$ shadow of a gapped network dispersion, not its opposite.
- *The invariant speed.* Paper 32 (Conjecture 9.4, Corollary 9.6) sought a finite invariant speed as the asymptote of an energy–momentum hyperboloid. A network realizes that mechanism with $c=1/\sqrt{LC}$, but through spatial coupling, not through the Bures lift.
- *The contact sign.* Paper 32's Theorem 9.1 sign — the contact sign of $\Theta=p\,dq-E\,dt$ — is the relative sign of kinetic and potential energy in $\mathcal L=T-V$. It is necessary for (a), but on a single node it produces no cone, because $V$ has no $k$-dependence. The missing ingredient was the gradient energy $\tfrac12\sum_eL_e^{-1}(d_0\varphi)_e^2$.

### 3.5 A single port is a line

**Proposition 3.7 (Cauer: every lossless port is a one-dimensional LC line) [P, cited; certified instance].**
- **(a) Cauer.** A finite lossless positive-real impedance of degree $n$ with $Z(\infty)=0$ has a Cauer (Stieltjes continued-fraction) realization
  $$Z(s)=\cfrac{1}{sC_1+\cfrac{1}{sL_2+\cfrac{1}{sC_3+\cdots}}},$$
  with $n$ positive elements (Cauer 1926; Stieltjes 1894). This is an inhomogeneous LC chain whose first node is the port.
- **(b) Lanczos.** Equivalently, tridiagonalizing the minimal ledger's generator with the port vector as the starting vector gives a Jacobi matrix: a nearest-neighbour chain. Its continuum analogue is the Krein string (Dym–McKean 1976).
- **(c) Two realizations, one port.** The Foster form of the same port (Paper 53, Theorem 3.1(5)) is ultralocal: a series of tanks with no coupling between them. Both are minimal realizations of one scattering function, so they are unitarily equivalent by Arov's theorem (Paper 53, Corollary 4.2).

*Certificate K2e:* Paper 53's three-tank port $\sum_{a=1}^32s/(s^2+a^2)$ has the Cauer elements $(C,L,C,L,C,L)=(\tfrac16,\tfrac97,\tfrac13,\tfrac{49}{54},\tfrac{81}{100},\tfrac{100}{189})$, which reproduce $Z$ exactly. Replacing $s^2+4$ by $s^2-4$ (not a reactance) produces the element $L_4=-\tfrac{5547}{1402}<0$. $\square$

*Reading [A].* Spatial structure is not an invariant of a port. It is a choice of local (sparse) basis on its ledger. One port carries at most a canonical one-dimensional space, its Krylov line, whose length is its Pick rank (Paper 53, Corollary 4.1). A space of dimension $d\ge2$ needs many ports joined into a network.

### 3.6 Two Lorentzian forms

Pinf-WhatIsMultiplicative (Sec. 2) found a second Lorentzian form in the program: the intersection form on $\mathrm{NS}(C\times C)$, of signature $(1,\rho-1)$ by the Hodge index theorem. Its primitive part is negative definite exactly when $|a|\le2g\sqrt q$ (Hasse–Weil), and it flips $(1,3)\to(2,2)$ when a Frobenius eigenvalue leaves the circle. The two forms compare as follows.

| | one node (additive) | network symbol | intersection form (multiplicative) |
|---|---|---|---|
| object | Fisher or Bures metric on a state space | $\sigma_2=C\omega^2-k^{\mathsf T}Ak$ on $(\omega,k)$ | intersection pairing on $\mathrm{NS}(C\times C)$ |
| signature | Riemannian | $(1,d)$ | $(1,\rho-1)$ |
| the one positive direction | none | inertia (the $\omega^2$ term) | the ample class |
| complement definite iff | — | links passive ($A\succ0$) | Hasse–Weil bound |
| flip | — | active link: growing mode | eigenvalue off the circle |
| status | [P] (Paper 32, Sec. 14.2; Pinf, Theorem 2.3) | [P] (Theorem 3.5) | [P] over $\mathbb F_q$ (Pinf, Theorems 2.1–2.2) |

*Certificate K2f* evaluates both flips with the same exact Sylvester test. The Pinf form at $q=7$ is negative definite at $a=5$ and indefinite at $a=6$. The second value is counterfactual: $|a|\le2\sqrt7$ for every elliptic curve over $\mathbb F_7$ (Hasse), so over $\mathbb F_q$ the flip never happens. On a network the flip is physically realizable: an active link.

**Verdict [A].** The two forms are of the same **type**, not the same form. Each has one distinguished positive direction and a complement whose definiteness is a passivity condition, and losing that condition creates a second timelike direction, which reads as growth. They live on different spaces, and neither is derived from the other here. The network form carries a *physical* light cone with a computable speed. The intersection form carries an arithmetic one. Whether a network whose ports carry multiplicative data realizes the intersection form as its symbol is open [C].

### 3.7 What becomes of the first negative

The negative of Paper 32 (Sec. 14.2) **holds for one node and is explained** by Proposition 1.1 and Theorem 3.5(c): a metric on a node's state space is not a propagation symbol. It **breaks for networks** [P]. The Lorentzian signature $(1,d)$ is a property of a network whose nodes and links store energy in the two conjugate forms (capacitive and inductive) and whose links are passive. Loss does not destroy it; the absence of inertia does. The prediction handed to this session — "Lorentzian signature is a property of lossless networks" — is sharpened. The cone is a *reactive* property: losslessness is not needed for the cone, only for undamped propagation inside it (echo; Sec. 5).

### 3.8 Which storage goes where

A lossless port is a ledger of rotations (PortPrinciple.md, Remark 4.7). A rotation exchanges energy between two conjugate storages, and by Foster's theorem every lossless port is a sum of LC tanks. A network has a choice that a single port does not: each storage can be *ultralocal* (the energy of one node) or *gradient* (the energy of a difference across a link).

**Setting.** A lossless quadratic network has conjugate variables $(q_v,p_v)$ at each node and Hamiltonian $H=\tfrac12p^{\mathsf T}Ap+\tfrac12q^{\mathsf T}Bq$, with $A,B$ real symmetric, positive semidefinite, translation invariant and of finite range. Then $\ddot q=-ABq$, so $\omega^2(k)=\hat A(k)\hat B(k)$ (the eigenvalues of $\hat A\hat B$ when a cell has several nodes). In the continuum limit, at spacing $\ell\to0$ with the physical coefficients fixed, $\hat A(k)=\sum_{j\le s_A}a_{2j}(k)$ with $a_{2j}$ homogeneous of degree $2j$ and $a_{2s_A}\neq0$. Call $s_A$ the *differential order* of the storage: $0$ for ultralocal storage (capacitance, mass), $1$ for gradient storage (inductive links, tension), $2$ for bending storage.

**Theorem 3.8 (storage order) [P].**
- **(a) One ultralocal, one gradient** ($s_A+s_B=1$). The principal symbol is $\omega^2-a_0\,b_2(k)$. It is Lorentzian, of signature $(1,d)$, exactly when the gradient part is positive definite and the ultralocal part positive. The maximal signal speed $c=\max_{\hat k}\sqrt{a_0b_2(\hat k)}$ is independent of $\ell$. This is Theorem 3.5(a), and it is the only placement with a cone.
- **(b) Both ultralocal** ($s_A+s_B=0$). The symbol has no spatial part: isolated oscillators (Theorem 3.5(c)).
- **(c) Total order two or more** ($s_A+s_B\ge2$). At long wavelength $\omega\propto|k|^{s_A+s_B}$, and the lattice's maximal group velocity diverges like $\ell^{\,1-s_A-s_B}$, so no finite signal speed survives the continuum limit. With both storages gradient, $(1,1)$, this is the real form of Schrödinger's equation: with $\psi=q+ip$, $\dot q=-\Delta p$ and $\dot p=\Delta q$ read $i\partial_t\psi=-\Delta\psi$. The case $(0,2)$ is a bending beam.
- **(d) One storage replaced by a loss.** The equation becomes first order, $\dot q=-DBq$: diffusion (Theorem 3.5(b)).

*Proof.* The top-degree part of $\hat A\hat B$ is $a_{2s_A}b_{2s_B}$, homogeneous of degree $2(s_A+s_B)$. It fixes the principal symbol and the long-wavelength exponent. On a one-dimensional lattice the gradient symbol is $(2-2\cos k\ell)/\ell^2=(2\sin\tfrac{k\ell}2/\ell)^2$. For $(0,1)$ the group velocity is $\sqrt{a_0b}\cos\tfrac{k\ell}2\le\sqrt{a_0b}$. For $(1,1)$ it is $2\sqrt{ab}\,\sin(k\ell)/\ell$, with maximum $2\sqrt{ab}/\ell$, and likewise for $(0,2)$. *Certificate p55b,* S1–S4. $\square$

| placement $(s_A,s_B)$ | dispersion | signal speed | examples |
|---|---|---|---|
| $(0,1)$: one ultralocal, one gradient | $\omega^2=c^2k^2\,(+m^2)$ | $c$, finite | LC lattice, string, sound, Maxwell's vacuum, Klein–Gordon |
| $(1,1)$: both gradient | $\omega\propto k^2$ | none ($\propto1/\ell$) | Schrödinger (real form) |
| $(0,2)$: ultralocal and bending | $\omega\propto k^2$ | none | Euler–Bernoulli beam, flexural plate |
| $(0,0)$: both ultralocal | $\omega=$ const | zero | isolated oscillators |
| one storage and a loss | $\omega=-iDk^2$ | parabolic | RC lattice, diffusion |

*Maxwell's vacuum is a network of this kind.* In temporal gauge, with vector potential $A$ and conjugate momentum $\Pi=-\varepsilon_0E$, the energy is $\int\big[|\Pi|^2/(2\varepsilon_0)+|\nabla\times A|^2/(2\mu_0)\big]$. The electric storage is ultralocal and the magnetic storage is gradient (curl–curl). The transverse modes obey $\omega^2=|k|^2/(\varepsilon_0\mu_0)$, and the longitudinal mode is the gauge line, $\omega=0$ (Proposition 2.3). So $c=1/\sqrt{\mu_0\varepsilon_0}$ is the LC-line speed of Theorem 3.1, with the vacuum's permittivity and permeability playing capacitance and inductance per unit length. The vacuum's characteristic impedance is $Z_0=\sqrt{\mu_0/\varepsilon_0}\approx376.73\ \Omega$. A coaxial line with $L'=250$ nH/m and $C'=100$ pF/m has $v=1/\sqrt{L'C'}=2\times10^8$ m/s and $Z=\sqrt{L'/C'}=50\ \Omega$ (*certificate* S3). The Yee lattice of computational electrodynamics (Yee 1966) is this network, discretized.

*Reading [A].* The base lift supplies the two conjugate storages, since a lossless ledger is made of rotations (Foster's tanks). Locality decides where the storages live, and passivity of the gradient storage makes the cone Lorentzian. **Relativistic causality is the placement "one storage on the nodes, one on the links."** Schrödinger's equation is what the same two storages do when both leak to their neighbours. It appears as the slow envelope of a gapped relativistic network: writing $\varphi=\mathrm{Re}\,(\psi e^{-imt})$ in the Klein–Gordon network turns the placement $(0,1)$ into an effective $(1,1)$ for $\psi$, with energy $\tfrac{c^2}{2m}(|\nabla q|^2+|\nabla p|^2)$ (Remark 3.6). That is why it has no finite signal speed of its own.

---

## 4. Area law and boundary capacity

### 4.1 Thermal states of passive networks

**Theorem 4.1 (the Gibbs state of a passive network) [P].** Write a passive network in port-Hamiltonian form
$$\dot x=(J-R)\nabla H+\xi,\qquad H=\tfrac12x^{\mathsf T}Qx,$$
with $J$ skew, $R\succeq0$, $Q\succ0$, and white noise $\xi$ of covariance $2TR$: the fluctuation–dissipation assignment "$k_BT$ on every loss" (PortPrinciple.md, Theorem 8.4). Then $\Sigma=TQ^{-1}$ is a stationary covariance. If $(J-R)Q$ is Hurwitz it is the unique one, so the stationary law is Gibbs, $\propto e^{-H/T}$, whatever $J$ and $R$ are. With losses at different temperatures, the stationary law is in general not Gibbs at any temperature.

*Proof.* $(J-R)T+T(J-R)^{\mathsf T}+2TR=T(J-R-J-R)+2TR=0$. *Certificate K3a* (exact): random rational $J,R,Q$. With two resistor groups at $T_1=1$ and $T_2=3$, the unique stationary $\Sigma$ satisfies $\Sigma Q\not\propto I$. $\square$

This is the copy lift at the level of a network: the thermal state of a passive network is the Gibbs state of its stored energy (Paper 54, Theorem 1; PortPrinciple.md, Theorem 6.3). Quantum mechanically, the thermal state of a lossless LC network is the Gaussian Gibbs state of $H$.

### 4.2 The cut law, with exact slack

**Theorem 4.2 (thermal cut law with exact slack) [P].** Let $\rho=e^{-\beta H}/Z$ on $\mathcal H_A\otimes\mathcal H_B$, with $H=H_A+H_B+H_\partial$, where $H_\partial$ collects the terms that couple $A$ to $B$. Then
$$\boxed{\ I(A{:}B)+D(\rho_A\otimes\rho_B\Vert\rho)=\beta\big(\langle H_\partial\rangle_{\rho_A\otimes\rho_B}-\langle H_\partial\rangle_\rho\big).\ }$$
Consequently:
- $I(A{:}B)\le\beta\big(\langle H_\partial\rangle_{\rho_A\otimes\rho_B}-\langle H_\partial\rangle_\rho\big)$;
- for bounded terms, $I(A{:}B)\le2\beta\|H_\partial\|\le2\beta\sum_{e\in\partial A}\|h_e\|$ (Wolf–Verstraete–Hastings–Cirac 2008);
- equality holds iff $\rho=\rho_A\otimes\rho_B$.

The slack $D=\beta\big(F(\rho_A\otimes\rho_B)-F(\rho)\big)$ is $\beta$ times the work a port can extract from the decoupled state with a bath at $\beta$ (PortPrinciple.md, Corollary 6.13; Paper 54, Theorem 1(d)). So the mutual information across a cut equals $\beta$ times the energy cost of cutting the boundary bonds, minus $\beta$ times the work recoverable from the cut state.

*Proof.* $-\ln\rho=\beta H+\ln Z$, so $D(\sigma\Vert\rho)=-S(\sigma)+\beta\langle H\rangle_\sigma+\ln Z$ for every $\sigma$, and $S(\rho)=\beta\langle H\rangle_\rho+\ln Z$. For $\sigma=\rho_A\otimes\rho_B$, subtracting gives $D=-I+\beta(\langle H\rangle_\sigma-\langle H\rangle_\rho)$. Since $\sigma$ and $\rho$ have the same marginals, $\langle H_A\rangle$ and $\langle H_B\rangle$ cancel. The same computation holds for unbounded $H$ whenever the expectations are finite, e.g. for Gaussian states. $\square$

The identity is the Wolf–Verstraete–Hastings–Cirac argument written as an equality. Its use here is the port reading of the slack and the instance below.

**Corollary 4.3 (harmonic networks of passive ports) [P].** Take $H=\tfrac12p^{\mathsf T}p+\tfrac12x^{\mathsf T}Kx$ with $K=d_0^{\mathsf T}Wd_0+m^2I$, $w_e>0$, $m>0$. Split the diagonal of $K$ between $A$ and $B$. Then $H_\partial=-\sum_{e=(i,j)\in\partial A}w_ex_ix_j$ and $\langle H_\partial\rangle_{\rho_A\otimes\rho_B}=0$, so
$$I(A{:}B)\ \le\ \beta\sum_{e\in\partial A}w_eX_{ij},\qquad X=\langle xx^{\mathsf T}\rangle=\frac1\beta\sum_{n\in\mathbb Z}\big(K+\nu_n^2\big)^{-1},\quad \nu_n=\frac{2\pi n}\beta .$$
- *Positivity.* $X$ is entrywise nonnegative, because each $K+\nu_n^2$ is a nonsingular M-matrix.
- *Area law.* $X_{ij}\le\sqrt{X_{ii}X_{jj}}\le X_{\max}$, so $I(A{:}B)\le\beta\,w_{\max}X_{\max}\,|\partial A|$, where $|\partial A|$ is the number of cut edges.
- *Classical limit.* $\beta X\to K^{-1}$, and the bound becomes $\sum_{\partial A}w_e(K^{-1})_{ij}$, independent of temperature.

On a lattice, $|\partial A|$ is the geometric area.

*Proof.* Theorem 4.2, plus the Matsubara identity $\coth(\beta\sqrt\lambda/2)/(2\sqrt\lambda)=\beta^{-1}\sum_n(\lambda+\nu_n^2)^{-1}$. *Certificate K3b* (40 digits): on a six-node network the identity holds to $7\times10^{-41}$, with $I=0.334$, $D=0.550$ and $\beta\sum wX=0.884$, computing $S(AB)$ from symplectic eigenvalues and $\beta\langle H\rangle+\ln Z$ from normal modes. $\square$

### 4.3 The numbers

*Certificate K3c* uses thermal Gaussian states at $\beta=1$, $w=1$, $m^2=1$, from exact covariance formulas (no sampling). Here $|\partial A|$ is the number of cut edges, the band is $\max/\min$ of $I/|\partial A|$, the volume ratio is $(I/|A|)_{\text{largest}}/(I/|A|)_{\text{smallest}}$, and the bound is $\beta\sum_{\partial A}wX$.

| Lattice (periodic) | Blocks | $I/\lvert\partial A\rvert$ | Band | Volume ratio | Slope vs $\lvert\partial A\rvert$ | Slope vs $\lvert A\rvert$ | $I$/bound |
|---|---|---|---|---|---|---|---|
| chain, $N=240$ | $\ell=4..64$ | $I=0.1583$ for every $\ell$ ($\lvert\partial A\rvert=2$) | 1.000 | 0.063 | — | — | — |
| square, $24^2$ | $\ell=2..10$ | 0.03146–0.03239 | 1.030 | 0.206 | 1.017 | 0.509 | 0.458–0.472 |
| cubic, $10^3$ | $\ell=2..5$ | 0.01553–0.01588 | 1.022 | 0.409 | 1.012 | 0.675 | 0.466–0.477 |
| diamond, $6^3$ cells | $\ell=1..4$ cells | 0.02713–0.02714 | 1.001 | 0.313 | 1.000 | 0.721 | 0.454 |

Every pre-registered band passed. The volume slopes sit at $(d-1)/d$ to within corner corrections, and the bound of Corollary 4.3 is attained to within a factor of about $2.2$.

**Controls** (on 576 nodes, with square-lattice block geometry):
- **(C1) Long-range expander:** a random 4-regular multigraph. $I$ rises from $0.42$ to $8.74$ nats. $I$ per geometric boundary grows by a factor of $4.20$: the *geometric* area law is violated. Yet $I$ per cut edge stays in a band of $1.03$, and the cut bound holds.
- **(C2) All-to-all, $w=1/N$.** $I$ rises from $0.0017$ to $0.035$ nats. The pre-registered expectation, that $I/\text{cut}$ falls tenfold, **failed** ($0.97$), and the failure is retained. The diagnosis is that mean-field mutual information is a function of $f_A=|A|/N$ that is linear for small $f_A$, so it tracks the weighted cut $|A||B|/N$.
- **K3d′** (post-diagnosis, not blind): the numerics match the mean-field closed form $s(\nu(f))+s(\nu(1-f))-s(\nu_1)-s(\nu_2)$ to $10^{-9}$. $I$ per geometric boundary grows by $4.02$, and $I$ per weighted cut stays in a band of $1.03$.

Both controls make the same point. **The law is a cut law; locality is what makes the cut an area.**

### 4.4 Capacity across a cut

**Theorem 4.4 (boundary-capacity bound) [P, cited and certified].** Let each edge of a network be a channel, i.e. a passive port with its own hidden thermal port, with noises independent across edges.
- **(a) Cut-set bound.** For every partition $(A,B)$ and any coding by the nodes, the rate of information from $A$ to $B$ per use is at most $\sum_{e\in\partial A}C_e$ (Elias–Feinstein–Shannon 1956; Cover–Thomas, cut-set bound). In finite form: for independent port noises and arbitrarily correlated inputs, $I(X;Y)\le\sum_eI(X_e;Y_e)$ by Hadamard's inequality, with equality iff the outputs are uncorrelated.
- **(b) Achievability.** The unicast capacity is the min cut (max-flow/min-cut with channel coding on each edge; Ford–Fulkerson 1956). The multicast capacity is the least of the sinks' min cuts, attained with network coding (Ahlswede–Cai–Li–Yeung 2000) but not, in general, by routing.
- **(c) Per-port capacity.** For a Gaussian thermal port with transmissivity $\tau$, hidden port at $\theta=k_BT$, bandwidth $W$ and input power $P$, the added noise is $\theta(1-\tau)$ per unit bandwidth: temperature times the defect Gram (PortPrinciple.md, Theorem 8.1). Then
  $$C_e=W\log_2\!\Big(1+\frac{\tau P}{\theta(1-\tau)W}\Big)\ \le\ \frac{\tau P}{\theta(1-\tau)\ln2}\quad\text{bits per second}.$$
  For a single bosonic channel the entropy flux at power $P$ obeys $\dot S\le\sqrt{\pi P/3\hbar}$ ($k_B=1$), with equality for thermal radiation (Bekenstein 1981; Pendry 1983).
- **(d) Independence is needed.** If the hidden ports are correlated across the cut (a non-diagonal defect Gram), per-port additivity can fail. The number of independent channels across a cut is still at most the number of cut ports.

*Certificates:*
- **K4a:** max flow equals min cut, exactly, on 40 random rational networks.
- **K4b:** Hadamard on 20 random correlated inputs, with equality for diagonal inputs. In the correlated-noise control $\Sigma_N=2(I-W)$, the joint ratio $\tfrac{1403}{1200}$ exceeds the per-port product $\tfrac{441}{400}$.
- **K4c:** $P=\pi T^2/12$ and $\dot S=\pi T/6$, so $\dot S^2=\pi P/3$, exactly.
- **K4d:** in the butterfly network the min cut to each sink is 2. XOR coding at the bottleneck delivers both bits to both sinks, and each pure forwarding choice fails one sink. $\square$

**Corollary 4.5 (dynamic area law) [P].** On a local network, the information rate across $\partial A$ is at most $|\partial A|\max_eC_e$. At an energy flux $P$ per port it is at most $|\partial A|\sqrt{\pi P/3\hbar}$ (quantum). Classically, it is at most the total cut power divided by $k_BT\ln2$ (the energy-per-bit form).

Theorem 4.4 is the rigorous form of a node-scale "screening" bound $I\le\sum_j\mathrm{cap}(b_{ij})$: it is the cut-set bound for the cut that encloses one node.

### 4.5 What becomes of the second negative

The negative of Paper 32.1 (Sec. 7) **holds for one simplex**: it has no spatial cut, and its "boundary" is the unit group of $\mathbb Z/N$. It **breaks for networks** [P]. The static law (Corollary 4.3) and the dynamic law (Corollary 4.5) are both cut laws. On local networks they are area laws, certified with bands of at most $1.03$ on four lattices. Paper 32.1's positive result — the arithmetic boundary share $\prod_p(1-1/(p^2-p+1))\approx0.515$ — remains a statement about one node's spectrum, orthogonal to the spatial area law. Paper 54 rebuilds the Bekenstein bound on relative-entropy positivity (Casini). Theorem 4.2 is that positivity evaluated at a cut.

---

## 5. The arrow lives on the cycle space

**Theorem 5.1 (currents, cycles, and affinity classes) [P].** Consider a Markov jump process on a connected graph $G$, with rates $k_{ij},k_{ji}>0$ on each edge and stationary law $\pi$. Let $J_e=\pi_ik_{ij}-\pi_jk_{ji}$ and $\mathcal A_e=\ln(k_{ij}/k_{ji})$.
- **(a) Cycle space.** $d_0^{\mathsf T}J=0$: $J$ lies in the cycle space $Z_1(G)=\ker d_0^{\mathsf T}$, of dimension $b_1=|E|-|V|+1$.
- **(b) Fundamental cycles.** For any spanning tree with fundamental cycles $z_f$, one per non-tree edge $f$, $J=\sum_fJ_fz_f$.
- **(c) Trees.** If $G$ is a tree, then $J=0$: detailed balance is automatic.
- **(d) Entropy production.** $\sigma=\sum_eJ_e\ln\frac{\pi_ik_{ij}}{\pi_jk_{ji}}=\langle\mathcal A,J\rangle=\sum_fJ_f\,\mathcal A(z_f)$. It depends on $\mathcal A$ only through its class $[\mathcal A]\in H^1(G;\mathbb R)=\operatorname{Hom}(H_1,\mathbb R)$: entropy production is the pairing of an affinity *cohomology* class with a current *homology* class.
- **(e) Kolmogorov.** Detailed balance holds iff $[\mathcal A]=0$, iff every cycle affinity vanishes, iff $J=0$.

On a 2-complex, with plaquettes filled, $J$ splits into a coexact part (circulation around plaquettes) and a harmonic part of dimension $b_1$ of the complex. The harmonic part is the topologically protected arrow of forward3 and Paper 01d (Theorem 5.1). Paper 54 (Theorem 3) shows that a node's static-response defect — the failure of "watching = pushing" — is linear in this same current. On a network, that defect lives on the cycle space.

*Proof.* (a) Stationarity is zero net flux into each node. (b) $J-\sum_fJ_fz_f$ is a cycle supported on a tree, hence zero. (c) $b_1=0$. (d) $\sum_eJ_e(\ln\pi_i-\ln\pi_j)=-\langle d_0\ln\pi,J\rangle=-\langle\ln\pi,d_0^{\mathsf T}J\rangle=0$. (e) Detailed balance means $\mathcal A=d_0\ln\pi$, which is exact. Conversely, if $\mathcal A=d_0u$, then $\pi\propto e^{u}$ is balanced, and uniqueness of $\pi$ gives $J=0$. Schnakenberg (1976); Kolmogorov (1936). $\square$

*Certificates:*
- **K5a:** ten random networks; exact rational $\pi$; $d_0^{\mathsf T}J=0$; $\dim\ker d_0^{\mathsf T}=b_1$; and $J=\sum_fJ_fz_f$.
- **K5b:** 20 random trees give $J=0$ exactly.
- **K5c:** Kolmogorov rates give $J=0$. With one rate perturbed, $J\ne0$ and the edge and cycle forms of $\sigma$ agree exactly in log algebra, with $\sigma=0.1212$.

**Proposition 5.2 (echo and forgetting on loops) [P; witness].**
- **(a) Lossless.** A finite lossless LC network is a finite lossless ledger: every mode is undamped, every port response is almost periodic, and every return amplitude comes back within any $\varepsilon$ (PortPrinciple.md, Theorem 4.5(2)).
- **(b) The five-node ring.** For a ring of $N$ nodes the normal frequencies are $\omega_k=2c|\sin(\pi k/N)|$. For $N=5$ the two nonzero frequencies have ratio $2\cos(\pi/5)=\varphi$, the golden ratio. The local return amplitude $G_0(t)=\tfrac15(1+2\cos\omega_1t+2\cos\omega_2t)$ nearly returns at $t=2\pi F/\omega_1$ with $F$ a Fibonacci number.
- **(c) Lossy.** With series loss, every non-uniform mode decays at rate $\gamma/2$, while the uniform mode (the conserved charge, Proposition 2.3) does not. So $G_0\to1/N$: the loop forgets everything except its charge.
- **(d) Driven and lossy.** A source with nonzero cycle affinity (an EMF around the loop) sustains a stationary circulating current with $\sigma>0$ (Theorem 5.1).

*Certificate K5d* (30 digits): the golden ratio holds exactly. The best echo in $[1,2000]$ is $0.99997$, at $t=1245.3=2\pi\cdot233/\omega_1$. The lossy ring with $\gamma=0.05$ deviates from $1/5$ by at most $2.4\times10^{-5}$ on $[400,2000]$. $\square$

**Remark 5.3 (a current is not yet an arrow).** A lossless loop can carry a persistent circulating current, i.e. trapped flux. That current is odd under time reversal but produces no entropy. The harmonic sector is where an arrow *can* live. It does live there only when the loop carries a nonzero affinity, which requires dissipation (Theorem 5.1(d)). This sharpens the reading "arrow $=b_1$" of forward3: $b_1$ counts the independent places an arrow can be, and $\sigma=\langle[\mathcal A],J\rangle$ says whether it is there.

*Reading [A].* The Port Principle's echo–yield duality (PortPrinciple.md, Proposition 6.9e) attaches to a network through its normal modes. Watching the lossless network in time asks when all normal-mode phases return. The echo exponent is $r-1$, where $r$ is the rank of the $\mathbb Z$-module of mode frequencies. It is not the cycle rank $b_1$: the five-node ring has $b_1=1$ and $r=2$. For the five-node ring $r=2$ (spacings $\{1,\varphi\}$), and the echoes are Fibonacci-timed, as in the Port Principle's golden case (its Proposition 6.8(c)). Lossless loops echo with an arithmetic set by their frequency module. Lossy loops, and infinite networks with continuous spectra, forget. Driven lossy loops carry the arrow.

---

## 6. Which network?

### 6.1 Second order: the tetrahedron is singled out

The acoustic branch of a network with two nodes per cell and equal bond weights $w$, with bond star $\delta_1,\dots,\delta_z$ from a node to its neighbours, has small-$k$ tensor
$$A_{\rm ac}=\frac w2\sum_i(\delta_i-\bar\delta)(\delta_i-\bar\delta)^{\mathsf T},\qquad \bar\delta=\frac1z\sum_i\delta_i ,$$
from $|f(k)|=z-\tfrac12\sum_i(k\cdot\delta_i)^2+\tfrac1{2z}(k\cdot z\bar\delta)^2+O(k^4)$, where $f(k)=\sum_ie^{ik\cdot\delta_i}$. The sound speed is isotropic iff the centred star has isotropic second moment.

**Theorem 6.1 (minimal isotropic star) [P].** Let $\delta_1,\dots,\delta_z\in\mathbb R^d$ satisfy $\sum_i\delta_i=0$ and $\sum_i\delta_i\delta_i^{\mathsf T}=\kappa I$ with $\kappa>0$. Then $z\ge d+1$. If $z=d+1$, the Gram matrix is
$$\big[\delta_i\cdot\delta_j\big]=\kappa\Big(I-\frac{J}{d+1}\Big)=\frac{\kappa}{d+1}\big((d+1)I-J\big),$$
so the $\delta_i$ are the vertices of a regular simplex centred at the node. For $d=3$ the Gram matrix is $\frac\kappa4(4I-J)$: the frame metric of Paper 01, and the $K_4$ admittance of Corollary 2.4.

*Proof.* Let $V=[\delta_1\cdots\delta_z]$. Then $V\mathbf 1=0$ gives $\operatorname{rank}V\le z-1$, and $VV^{\mathsf T}=\kappa I$ gives $\operatorname{rank}V=d$. The Gram matrix $G=V^{\mathsf T}V$ satisfies $G^2=\kappa G$ and $G\mathbf 1=0$, so $G/\kappa$ is an orthogonal projector of rank $d$ with $\mathbf 1$ in its kernel. If $z=d+1$ the kernel is exactly $\mathbb R\mathbf 1$. $\square$

*Certificate K6b* (exact): the tetrahedral star with $|\delta|=\ell$ has $\sum\delta=0$, $\sum\delta\delta^{\mathsf T}=\tfrac43\ell^2I$, and Gram matrix $\tfrac{\ell^2}3(4I-J)$.

This is the tight-frame (spherical 2-design) bound of Delsarte–Goethals–Seidel (1977), read for networks. A Bravais lattice has a symmetric neighbour set $\pm\delta$ and needs $z\ge2d$. A two-sublattice network reaches the absolute minimum $d+1$, and **in three dimensions the four-valent tetrahedral (diamond) star is the least coordination with an isotropic light cone, and the only one at that valence**. Its sound speed is $c^2=\tfrac23\Omega^2\ell^2$ in every direction, with $\Omega^2=w/C$.

### 6.2 Fourth order: the tetrahedron is not singled out

**Theorem 6.2 (fourth-order dispersion of the tetrahedral shell) [P].** Consider the single-shell phase dispersion $\omega^2=\Omega^2\sum_{n=1}^4\big(1-\cos k\cdot\delta_n\big)$, with $\delta_n=\frac\ell{\sqrt3}(\pm1,\pm1,\pm1)$ (even number of minus signs). Put $P(k)=k_1^2k_2^2+k_1^2k_3^2+k_2^2k_3^2$. Then
$$\omega^2=c^2k^2\Big[1-\frac{\ell^2}{36}\Big(k^2+\frac{4P(k)}{k^2}\Big)\Big]+O(k^6),\qquad c^2=\tfrac23\Omega^2\ell^2 .$$
Writing $\omega=ck\big(1-\tilde\eta(\hat k)\,\ell^2k^2+\dots\big)$, we get $\tilde\eta(\hat k)=\big(1+4P(\hat k)\big)/72\in\big[\tfrac1{72},\tfrac7{216}\big]$:

| Direction | magnitude of the (negative) $\ell^2k^2$ coefficient in $\omega^2/c^2k^2$ | $\tilde\eta$ |
|---|---|---|
| $\langle100\rangle$ | $1/36$ | $1/72$ |
| $\langle110\rangle$ | $1/18$ | $1/36$ |
| $\langle111\rangle$ | $7/108$ | $7/216$ |

The anisotropy $\langle111\rangle/\langle100\rangle$ is exactly $7/3$. The diamond acoustic branch $\Omega^2(4-|f(k)|)$ agrees with the single-shell formula through $O(k^4)$, and differs at $O(k^6)$ by $-\tfrac2{27}\Omega^2\ell^6(k_1k_2k_3)^2$.

*Proof.* Expand $1-\cos x$ to $x^6$. Over the tetrahedral sign vectors $s_n$, $\sum_ns_1^as_2^bs_3^c$ vanishes unless $a,b,c$ are all even or all odd, so $\sum_n(k\cdot s_n)^4=4\big((k^2)^2+4P\big)$ and $\sum_n(k\cdot s_n)^3=24k_1k_2k_3$. For the acoustic branch, $|f|=4-a+b^2/8+O(k^8)$ with $a=\sum(1-\cos)$ and $b=\sum\sin$. *Certificate K6′* (exact, sympy), with a 60-digit witness that the truncation error scales as $k^8$ (ratio $256.0$ when $k$ is halved). $\square$

**The handed-over claim (K6) fails, and the failure is retained.** The claim "$\omega^2=c^2k^2(1-\ell^2k^2/36)$, isotropic, $\tilde\eta=1/72$" is true only along the cube axes. K6′, written from a hand expansion before the certificate's first run, predicted the failure and all three directional coefficients exactly.

**Proposition 6.3 (no crystallographic shell is isotropic at fourth order) [P for the shells tested].** The fourth-moment ratio $\sum(\hat k\cdot\delta)^4/\big(\sum(\hat k\cdot\delta)^2\big)^2$ along $\langle100\rangle$ and $\langle111\rangle$ is:
- sc: $\tfrac12$ and $\tfrac16$;
- bcc: $\tfrac18$ and $\tfrac7{24}$;
- fcc: $\tfrac18$ and $\tfrac16$;
- tetrahedral: $\tfrac14$ and $\tfrac7{12}$;
- icosahedral 12-star: $\tfrac3{20}$ and $\tfrac3{20}$.

Isotropy at fourth order requires the shell to be a spherical 4-design. The icosahedral star is a 5-design, but it is not a lattice star (crystallographic restriction). None of the four standard shells is. *Certificate K6c* (exact, with $\sqrt5$). $\square$

### 6.3 Rigidity, and the DEC reading

**Proposition 6.4 (Maxwell counting) [P].** A bar-and-joint framework in $\mathbb R^3$ needs average degree at least $6$ to be rigid (Maxwell 1864). Four-valent networks are therefore floppy as *elastic* networks. *Certificate K6d* (exact rank of periodic rigidity matrices):
- diamond, $2\times2\times2$ conventional cells: rank $127$ of $189$ (128 bonds, one self-stress), so floppy;
- sc, $4^3$: rank $144$ of $189$, floppy despite $z=6$ — Maxwell's count is necessary, not sufficient (Calladine 1978);
- fcc, $2\times2\times2$: rank $93$ of $93$, rigid. $\square$

The scalar (phase, LC) network of Sections 3–4 has no rigidity requirement. The four-valent star is singled out for **reactive scalar** networks and fails for elastic ones.

**Proposition 6.5 (the four-valent network is the dual of a tetrahedral complex) [P].** Let $X$ be a closed, coherently oriented tetrahedral 3-complex, and let $B_3$ be its tetrahedron–triangle incidence matrix, the matrix of the coboundary $d_2:C^2\to C^3$. Then
$$B_3B_3^{\mathsf T}=4I-A_{\rm dual}=L_3,$$
the graph Laplacian of the 4-regular dual graph, which equals the top Hodge Laplacian $d_2d_2^{\mathsf T}$ (since $d_3=0$).

*Proof.* Each tetrahedron has four triangles. A coherent orientation induces opposite orientations on a shared triangle. $\square$

*Certificate K6e* (exact integers):
- the boundary of the 4-simplex gives $B_3B_3^{\mathsf T}=5I-J$, the frame metric of the 5-frame;
- the Kuhn (Freudenthal) triangulation of the 3-torus, with 162 tetrahedra and 324 triangles, gives $4I-A$, with every triangle in exactly two tetrahedra.

*Reading.* A tetrahedral cell complex (Paper 01b, Sec. 10; Paper 01d, Sec. 4) carries two networks:
- the **primal** 1-skeleton, whose node Laplacian is $d_0^{\mathsf T}d_0$, equal to $4I-J$ on each cell (Corollary 2.4);
- the **dual** graph, which is four-valent, with node Laplacian $L_3=d_2d_2^{\mathsf T}$, acting on cell densities.

The four-valent network of ports is the dual reading of a $K_4$-cell complex.

### 6.4 Verdict on H6

Four-valent tetrahedral coordination is singled out **at second order, for reactive scalar networks**. It is the least coordination with an isotropic cone, it is unique, and its bond-star Gram matrix is the frame metric. It is **not** singled out at fourth order: its anisotropy is $7/3$, as with every crystallographic shell tested. Two shells together do reach fourth-order isotropy, and fourteen bonds is the minimum (Sec. 6.5). It is not singled out for elastic networks, which are floppy. The **dimension** is an input: it is the rank of the bond star. If one identifies a node's bond star with the $N$ rays of its categorical frame, then $d=N-1$ [A]. That is a modeling choice, not a selection.

### 6.5 Fourth order with several shells (Open Problem O2, closed)

The anisotropy of Theorem 6.2 is a property of single shells, not of networks. A combination of shells removes it.

**Theorem 6.6 (fourth-order isotropy) [P].** Let a Bravais network have bond vectors $\pm\delta_e$ with weights $w_e>0$. Its dispersion $\omega^2=(2/C)\sum_ew_e(1-\cos k\cdot\delta_e)$ is isotropic through $O(k^4)$ iff $\sum_ew_e(k\cdot\delta_e)^2\propto|k|^2$ and $\sum_ew_e(k\cdot\delta_e)^4\propto|k|^4$.
- **(a)** In $d=3$ this requires at least seven bond pairs ($z\ge14$), and seven are enough. The simple-cubic and body-centred shells together, with per-bond weights $w_{\rm sc}=8w_{\rm bcc}$, are isotropic through $O(k^4)$. Among the other combinations of standard shells, sc + fcc with $w_{\rm sc}=2w_{\rm fcc}$ ($z=18$) is isotropic, and fcc + bcc never is with positive weights.
- **(b)** In $d=2$ three bond pairs are necessary and sufficient. The triangular lattice ($z=6$) is isotropic through $O(k^4)$; the square lattice needs next-nearest neighbours, with weights $4{:}1$ ($z=8$).
- **(c)** The fourteen-bond star is anisotropic at $O(k^6)$.

These are the D3Q15, D3Q19, D2Q7 and D2Q9 stencils of the lattice Boltzmann method, where the same moment conditions secure isotropic hydrodynamics (Qian–d'Humières–Lallemand 1992; Wolf-Gladrow 2000). What is added here is the minimality.

**Lemma 6.7 (six pairs force the icosahedron) [P].** Let unit vectors $a_1,\dots,a_N\in\mathbb R^3$ and weights $\lambda_i>0$ satisfy $\sum_i\lambda_i(a_i\cdot x)^4=|x|^4$. Then $N\ge6$. If $N=6$, then $\lambda_i=\tfrac56$ and $(a_i\cdot a_j)^2=\tfrac15$ for all $i\neq j$. The six lines are therefore equiangular, which in $\mathbb R^3$ forces the six axes of the icosahedron (Haantjes 1948; Lemmens–Seidel 1973).

*Proof.* Polarizing the identity gives $\sum_i\lambda_i(a_i\cdot x)^2(a_i\cdot y)^2=\tfrac13\big(|x|^2|y|^2+2(x\cdot y)^2\big)$. On the six-dimensional space of symmetric matrices, with the trace inner product and $P_i=a_ia_i^{\mathsf T}$, this reads $\sum_i\lambda_i|P_i\rangle\langle P_i|=\tfrac13|I\rangle\langle I|+\tfrac23\,\mathrm{Id}$. The right side has full rank 6, so $N\ge6$.

Now let $N=6$. Let $W$ be the matrix with columns $\sqrt{\lambda_i}P_i$, and let $G=W^{\mathsf T}W$, so $G_{ij}=\sqrt{\lambda_i\lambda_j}(a_i\cdot a_j)^2$. Then $G$ has the spectrum of $WW^{\mathsf T}$, namely $\tfrac53$ once and $\tfrac23$ five times. Moreover $G^2-\tfrac23G=\tfrac13uu^{\mathsf T}$, with $u_i=\langle I,\sqrt{\lambda_i}P_i\rangle=\sqrt{\lambda_i}$. Hence $G=\tfrac23I+\tfrac15uu^{\mathsf T}$. Comparing diagonals gives $\lambda_i=\tfrac23+\tfrac{\lambda_i}5$, that is $\lambda_i=\tfrac56$; comparing off-diagonal entries gives $(a_i\cdot a_j)^2=\tfrac15$. $\square$

*Proof of Theorem 6.6.* The equivalence is the expansion $1-\cos x=\tfrac{x^2}2-\tfrac{x^4}{24}+O(x^6)$.
- **(a)** Write the fourth-moment condition as $\sum_e\lambda_e(a_e\cdot k)^4=\kappa|k|^4$, with $a_e=\delta_e/|\delta_e|$ and $\lambda_e\propto w_e|\delta_e|^4$. Lemma 6.7 gives at least six pairs, and exactly six would put lattice vectors along all six icosahedral axes.
  - *No lattice contains them.* Six lattice vectors in $\mathbb R^3$ satisfy three independent rational linear relations. Rescaling the vectors multiplies the relation matrix by diagonal matrices, which leaves its cross-ratios unchanged, so every cross-ratio would be rational. But the relation matrix of the icosahedral axes has the cross-ratio $\tfrac{1-\sqrt5}2$ (*certificate* I3). An exhaustive search confirms that no equiangular sextuple exists among integer directions with coordinates in $[-3,3]$ (I4). Hence $z\ge14$.
  - *Sufficiency.* The shell fourth moments are $2S_4$ for sc, $8S_4+24P$ for fcc, and $8S_4+48P$ for bcc, with $S_4=\sum_ik_i^4$ and $P=\sum_{i<j}k_i^2k_j^2$, while $|k|^4=S_4+2P$. Isotropy needs the coefficient of $P$ to be twice that of $S_4$. This gives $8{:}1$ for sc + bcc and $2{:}1$ for sc + fcc, and no positive solution for fcc + bcc (I1). Cubic symmetry makes the second moments isotropic.
- **(b)** In $d=2$ the space of binary quadratic forms has dimension 3, so the same argument gives at least three pairs. The six triangular directions realize the bound (I5).
- **(c)** Certificate I6. $\square$

*Reading.* Lorentz invariance of a lattice cone is an order-by-order property. Single shells break it at $O(k^2\ell^2)$ relative to $c^2k^2$; fourteen well-weighted bonds restore it to that order; each further order needs a higher design. Exact invariance belongs to the continuum limit, which is the program's general verdict on symmetries of finite networks.

---

## 7. Fenced outlook

### 7.1 Gauge on a network [P for the statements; C for the reading]

On a network, an abelian edge connection $A\in C^1(G;\mathbb R/2\pi\mathbb Z)$ changes under $A\mapsto A+d_0\chi$. Its gauge-invariant content is its holonomies around $b_1$ independent cycles: a point of the torus
$$\operatorname{Hom}\big(H_1(G),U(1)\big)\cong\mathbb T^{b_1},$$
the Pontryagin dual of the cycle lattice $H_1(G)\cong\mathbb Z^{b_1}$. On a graph every connection is flat, since there are no 2-cells. Once plaquettes are filled, the curvature $F=d_1A$ lives on them.

The abelian flatness of forward5 concerns the frame's gauge line $\mathbb R\mathbf 1$, which $S_4$ fixes. It does not extend to edge connections on networks with loops. On a triangulated annulus ($b_1=1$), a flat connection with holonomy $1$ around the hole is not exact (*certificate K7*): an Aharonov–Bohm flux. The stochastic affinity $\mathcal A$ of Section 5 is such a connection (Polettini 2012). Detailed balance is trivial holonomy, and the arrow is a holonomy.

*Reading [C], corrected 2026-10-02.* Two different lattice–torus pairs are attached to a network, and they must not be conflated.
- The cycle lattice $H_1(G)\cong\mathbb Z^{b_1}$ and its torus $\operatorname{Hom}(H_1,U(1))$ carry the arrow (Sec. 5: affinity classes paired with currents) and abelian gauge holonomy.
- The module $M$ of normal-mode frequencies and its torus carry the echo arithmetic (PortPrinciple.md, Proposition 6.9e).

Their ranks differ in general. The five-node ring has $b_1=1$ but $\operatorname{rank}M=2$ (frequencies in ratio $1{:}\varphi$), and a tree has $b_1=0$ while its modes can have any rank. Whether the two pairs are related for special networks is open [C].

### 7.2 Lineage

This construction has a speculative ancestor in the author's unpublished Occupation Thesis. That work posited:
- a four-valent tetrahedral network of nodes;
- a phase-sector dispersion with an $O(k^4)$ correction;
- a node-scale capacity bound $I\le\sum\mathrm{cap}(b_{ij})$;
- a looped versus unlooped distinction between matter and radiation.

Paper 55 tests what of this survives as mathematics:
- the four-valent star is the minimal isotropic star (Theorem 6.1);
- the dispersion correction is anisotropic (Theorem 6.2);
- the capacity bound is the cut-set bound (Theorem 4.4);
- looped versus unlooped maps, as a reading only, onto echo versus forgetting and onto the cycle space (Sec. 5).

None of the Thesis's physical identifications is used or supported here.

### 7.3 The network layer in the architecture

In the 2026-10-01 architecture, the axioms (finite distinguishability; composable, dilatable channels; passivity) force the Port Principle and the derived functional of Paper 54 on each node. This paper composes nodes. Composition is Kirchhoff's (Theorem 2.2). Space is tested by cones (Sec. 3), cuts (Sec. 4) and loops (Sec. 5). The arithmetic of finite spectra (Papers 32 and 32.1) stays inside nodes.

The Port Principle (Sec. 14) located gravity where local passive ports fail to glue into a global passive state. Kirchhoff composition is now the explicit glue. What remains missing is any rule by which the network's own weights $(L_e,C_v)$ respond to what flows through them [C].

### 7.4 Open problems

- **O1.** *Network dynamics.* Let link weights respond to stored energy, and demand entanglement equilibrium at every cut: stationarity of the slack $D$ of Theorem 4.2 at first order (Jacobson 2016). Does the response obey a discrete Einstein- or Regge-type equation sourced by energy density? This is the network layer's gravity question [C]. *(Addressed in Paper 56: weights fail the test at area order; the bond count carries Jacobson's term.)*
- **O2.** *Fourth-order isotropy.* Is there a weighted combination of crystallographic shells whose $k^4$ anisotropy cancels exactly, and what is the least coordination that achieves it? *(Closed by Theorem 6.6. Simple-cubic plus body-centred shells with weights $8{:}1$ achieve it, and $z=14$ is the least possible in three dimensions.)*
- **O3.** *Dimension.* Can any passivity or stability criterion select the rank of the bond star?
- **O4.** *Multiplicative ports.* Is there a network whose propagation symbol is the intersection form of Section 3.6?

---

## 8. What is proven, what is a reading, what failed

**Summary by hypothesis.**

| Hypothesis | Settlement | Tier |
|---|---|---|
| H1 composition | passive composition, Laplacian, KCL = Noether, $K_4\mapsto4I-J$ (Thm 2.2, Prop 2.3, Cor 2.4); converse fails (masking) | [P] |
| H2 light cones | cone iff two reactances and passive stiffness; loss lower order; RC parabolic; node ultralocal; gain = second timelike direction (Thms 3.1–3.5, Prop 3.4); one port = one line (Prop 3.7) | [P] |
| H2 comparison | network symbol and intersection form are one type, two forms (Sec. 3.6) | [A] |
| H2′ storage placement | cone iff one storage ultralocal and one gradient; both gradient = Schrödinger, no signal speed; Maxwell's vacuum is the first kind (Thm 3.8) | [P] |
| H3 area law | exact slack identity; harmonic cut law; bands at most 1.03 on four lattices; controls obey the cut and violate the geometric area (Thm 4.2, Cor 4.3, Sec. 4.3) | [P]; numerics with exact covariance |
| H4 capacity | cut-set bound, max-flow/min-cut, coding, per-port Shannon–Nyquist and Pendry–Bekenstein, independence needed (Thm 4.4, Cor 4.5) | [P, cited and certified] |
| H5 arrow | currents in the cycle space; $\sigma=\langle[\mathcal A],J\rangle$; trees carry none (Thm 5.1); echo and forgetting on loops (Prop 5.2) | [P]; echo–yield tie [A] |
| H6 which network | minimal isotropic star = regular simplex = frame metric (Thm 6.1); fourth order anisotropic $7/3$ (Thm 6.2); handed-over isotropy **false**; floppy (Prop 6.4); dual of a tetrahedral complex (Prop 6.5) | [P] |
| H6′ fourth-order isotropy (O2) | at least 7 bond pairs in $d=3$ (Lemma 6.7: six would be icosahedral); sc + bcc at $8{:}1$ attains it (Thm 6.6) | [P] |
| H7 gauge | holonomy torus $\mathbb T^{b_1}$; flat but nontrivial on loops; affinity as connection | [P] statements, [C] reading, fenced |

**The three negatives.**

| Negative | For one node | For a network |
|---|---|---|
| Paper 32 (Sec. 14.2): Euclidean, no Lorentzian | holds, and is explained (Prop 1.1, Thm 3.5(c)) | broken [P]: $(1,d)$ with $c=1/\sqrt{LC}$ |
| Paper 32.1 (Sec. 7): no geometric area law | holds (no spatial cut) | broken [P]: static and dynamic cut laws, which are area laws on local networks |
| Paper 32 (G3): no physical-space reconstruction | holds | partially broken: cone, cuts, arrow [P]; dimension and dynamics not derived |

**Certificate** `empirical/network55/p55_cert.py`: numpy, sympy and mpmath only. K/L were pre-registered in the docstring before run 1. Runs 1–3 are identical on the pre-registered checks (run 3 was a checker-hygiene rerun).

| Group | Pre-registered | Result |
|---|---|---|
| K1 composition | K1a–K1d | 3/4; **K1a failed, retained** (control masked); K1a′ (not blind) passes |
| K2 light cones | K2a–K2f | 5/6; **K2d failed, retained** (monotone finite-$t$ criterion); K2d′ (not blind) passes |
| K3 area law | K3a–K3d | 3/4; **K3d failed, retained** (C2 expectation wrong); K3d′ (not blind) passes |
| K4 capacity | K4a–K4d | 4/4 |
| K5 arrow | K5a–K5d | 4/4 |
| K6 which network | K6, K6′, K6b–K6e | 5/6; **K6 failed, retained** (isotropy false, as K6′ predicted) |
| K7 gauge | K7 | 1/1 |
| **Total** | 29 | **25/29**; post-diagnosis **3/3** (not blind) |
| `p55b_storage_isotropy_cert.py`: S storage order, I isotropy | S1–S4, I1–I5 (I6 report) | run 1 8/9 (**S1 failed on a checker artifact, retained**: a trig identity sympy did not close; every pre-registered value passed); run 2 **9/9** (not blind for the repaired checker) |

**Lessons carried forward.**
- A passivity control can be *masked* by passive surroundings. Controls should test elements, not only composites.
- Finite-size deviations from an asymptotic rate need not be monotone. Pre-register limits and bands, not monotonicity (the same lesson as PortPrinciple P7).
- "O(1) in $N$" is not "flat in $|A|$". The all-to-all control obeyed the cut law it was meant to stress.

**Safe statements.**
- A passive network has a Lorentzian propagation symbol iff it stores energy in two conjugate forms with passive stiffness.
- Thermal mutual information across any cut is at most $\beta$ times the energy the cut bonds lose when the state is decoupled across the cut, with exact relative-entropy slack.
- Steady currents live on cycles.
- The minimal isotropic star is the regular simplex.
- A lossless network has a finite signal speed exactly when one of its two conjugate storages is ultralocal and the other gradient; Maxwell's vacuum is such a network.
- Fourth-order isotropy needs at least fourteen bonds in three dimensions, and fourteen suffice.

**Unsafe statements.**
- "The network derives three-dimensional space." The dimension is an input.
- "The lattice light cone is Lorentz invariant." A single shell is anisotropic at $O(k^2\ell^2)$. Fourteen well-weighted bonds restore isotropy to that order (Theorem 6.6), but not beyond it.
- "The network symbol is the intersection form." It is the same type, not the same form.
- "Any of this is gravity." Network dynamics is open (O1).

---

## References

- D. N. Arnold, R. S. Falk, R. Winther, Finite element exterior calculus, homological techniques, and applications, *Acta Numer.* 15 (2006) 1–155.
- D. Z. Arov, Passive linear stationary dynamic systems, *Sibirsk. Mat. Zh.* 20 (1979) 211–228.
- R. Ahlswede, N. Cai, S.-Y. R. Li, R. W. Yeung, Network information flow, *IEEE Trans. Inf. Theory* 46 (2000) 1204–1216.
- J. C. Baez, B. Fong, A compositional framework for passive linear networks, *Theory Appl. Categ.* 33 (2018) 1158–1222.
- J. D. Bekenstein, Energy cost of information transfer, *Phys. Rev. Lett.* 46 (1981) 623–626.
- L. Brillouin, *Wave Propagation in Periodic Structures*, McGraw-Hill, 1946.
- O. Brune, Synthesis of a finite two-terminal network whose driving-point impedance is a prescribed function of frequency, *J. Math. Phys.* 10 (1931) 191–236.
- C. R. Calladine, Buckminster Fuller's "tensegrity" structures and Clerk Maxwell's rules for the construction of stiff frames, *Int. J. Solids Struct.* 14 (1978) 161–172.
- W. Cauer, Die Verwirklichung von Wechselstromwiderständen vorgeschriebener Frequenzabhängigkeit, *Arch. Elektrotech.* 17 (1926) 355–388.
- R. Courant, D. Hilbert, *Methods of Mathematical Physics*, vol. II, Interscience, 1962.
- T. M. Cover, J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley, 2006.
- M. Cramer, J. Eisert, Correlations, spectral gap and entanglement in harmonic quantum systems on generic lattices, *New J. Phys.* 8 (2006) 71.
- S. Darlington, Synthesis of reactance 4-poles, *J. Math. Phys.* 18 (1939) 257–353.
- P. Delsarte, J. M. Goethals, J. J. Seidel, Spherical codes and designs, *Geom. Dedicata* 6 (1977) 363–388.
- M. Desbrun, A. N. Hirani, M. Leok, J. E. Marsden, Discrete exterior calculus, arXiv:math/0508341 (2005).
- DLMF, NIST Digital Library of Mathematical Functions, Sec. 10.19 (Debye expansions) and 10.41 (uniform expansions).
- F. Dörfler, F. Bullo, Kron reduction of graphs with applications to electrical networks, *IEEE Trans. Circuits Syst. I* 60 (2013) 150–163.
- H. Dym, H. P. McKean, *Gaussian Processes, Function Theory, and the Inverse Spectral Problem*, Academic Press, 1976.
- J. Eisert, M. Cramer, M. B. Plenio, Area laws for the entanglement entropy, *Rev. Mod. Phys.* 82 (2010) 277–306.
- P. Elias, A. Feinstein, C. E. Shannon, A note on the maximum flow through a network, *IRE Trans. Inf. Theory* 2 (1956) 117–119.
- L. R. Ford, D. R. Fulkerson, Maximal flow through a network, *Can. J. Math.* 8 (1956) 399–404.
- R. M. Foster, A reactance theorem, *Bell Syst. Tech. J.* 3 (1924) 259–267.
- H. Freudenthal, Simplizialzerlegungen von beschränkter Flachheit, *Ann. of Math.* 43 (1942) 580–582.
- J. Haantjes, Equilateral point-sets in elliptic two- and three-dimensional spaces, *Nieuw Arch. Wisk.* 22 (1948) 355–362.
- M. B. Hastings, An area law for one-dimensional quantum systems, *J. Stat. Mech.* (2007) P08024.
- T. Jacobson, Entanglement equilibrium and the Einstein equation, *Phys. Rev. Lett.* 116 (2016) 201101.
- G. Kirchhoff, Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird, *Ann. Phys. Chem.* 72 (1847) 497–508.
- A. Kolmogoroff, Zur Theorie der Markoffschen Ketten, *Math. Ann.* 112 (1936) 155–160.
- G. Kron, *Tensor Analysis of Networks*, Wiley, 1939.
- P. W. H. Lemmens, J. J. Seidel, Equiangular lines, *J. Algebra* 24 (1973) 494–512.
- E. H. Lieb, D. W. Robinson, The finite group velocity of quantum spin systems, *Commun. Math. Phys.* 28 (1972) 251–257.
- J. C. Maxwell, On the calculation of the equilibrium and stiffness of frames, *Phil. Mag.* 27 (1864) 294–299.
- J. B. Pendry, Quantum limits to the flow of information and entropy, *J. Phys. A* 16 (1983) 2161–2171.
- M. Polettini, Nonequilibrium thermodynamics as a gauge theory, *EPL* 97 (2012) 30003.
- Y. H. Qian, D. d'Humières, P. Lallemand, Lattice BGK models for Navier–Stokes equation, *Europhys. Lett.* 17 (1992) 479–484.
- J. Schnakenberg, Network theory of microscopic and macroscopic behavior of master equation systems, *Rev. Mod. Phys.* 48 (1976) 571–585.
- T. J. Stieltjes, Recherches sur les fractions continues, *Ann. Fac. Sci. Toulouse* 8 (1894) J1–J122.
- B. D. H. Tellegen, A general network theorem, with applications, *Philips Res. Rep.* 7 (1952) 259–269.
- A. van der Schaft, B. Maschke, Port-Hamiltonian systems on graphs, *SIAM J. Control Optim.* 51 (2013) 906–937.
- J. C. Willems, Dissipative dynamical systems, *Arch. Rational Mech. Anal.* 45 (1972) 321–393.
- D. A. Wolf-Gladrow, *Lattice-Gas Cellular Automata and Lattice Boltzmann Models*, Springer, 2000.
- M. M. Wolf, F. Verstraete, M. B. Hastings, J. I. Cirac, Area laws in quantum systems: mutual information and correlations, *Phys. Rev. Lett.* 100 (2008) 070502.
- K. S. Yee, Numerical solution of initial boundary value problems involving Maxwell's equations in isotropic media, *IEEE Trans. Antennas Propag.* 14 (1966) 302–307.
- Program: PortPrinciple.md (Defs 2.1–2.5; Thms 4.1–4.5, 5.1, 6.3, 8.1, 8.4; Prop 6.8, 6.9e; Cor 6.13; Sec. 14); Paper 53 (Thm 3.1, Lemma 3.2, Cors 4.1–4.2); Paper 54 (Thm 1); Paper 01b (Thm 10.1); Paper 01d (Thms 2.1, 5.1, Sec. 4); forward1; forward3; forward5; Paper 32 (Sec. 8, 9, 14.2, G3); Paper 32.1 (Sec. 7); Paper 46 (Thm 3.1); Pinf-WhatIsMultiplicative (Sec. 2).
