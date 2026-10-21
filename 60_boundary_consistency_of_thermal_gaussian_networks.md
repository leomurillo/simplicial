# 60 — What a Boundary Can Know

## Exact elimination, thermal visibility, and the canonical-correlation spectrum of Gaussian networks

*Research note — consolidated October 9, 2026; Section 8.10 added October 13, 2026*

## Abstract

A finite harmonic network at one temperature is observed only at its boundary. We ask two questions. What must a boundary description retain to remain consistent with the full network? And how much of the hidden interior can the boundary ever learn?

For the first question, eliminating hidden coordinates has four mutually consistent descriptions:

- a Schur-complement stiffness;
- the Gibbs state of that stiffness;
- a frequency-dependent Schur response whose induced, correlated noise obeys fluctuation–dissipation;
- a conditional free-energy excess that prices the information lost.

All four compose under successive elimination, and thermal conditional refinement is an exact right inverse of marginalization. The naive quantum analogue is false. The true reduced quantum marginal is a thermal oscillator with renormalized mass, 12% heavier in an exact witness, and Petz recovery replaces the classical refinement.

For the second question, we compute exactly the relative entropy between the entire continuous boundary records produced by a hidden preparation and by its thermal refinement.

- **Exact channel.** The preparation-to-record channel is a Gaussian attenuation channel with visibility matrix $\Pi$. Its largest eigenvalue is a sharp contraction coefficient for every finite-entropy preparation, Gaussian or not, and it is strictly below one. In the original witness, observing the boundary forever reveals 0.82% of the preparation's relative entropy, and no preparation can expose more than 6.9%.
- **Feedback and depth.** Known boundary feedback cannot improve the ideal experiment. In pinned chains, deep preparations are screened at the exact exponential rate $2\operatorname{arcosh}(1+m/2k)$.
- **Harvest equals visibility.** The largest mean work that open-loop boundary forcing can extract from a hidden mean preparation is $T$ times the relative entropy of the entire boundary record, through the same matrix $\Pi_\infty$. The work a port must waste is $T$ times the information it cannot see, which is the posterior slack.
- **General networks.** Overdamped networks with any friction matrix keep a closed form. Inertial networks need one Riccati equation, and their ceiling is strict exactly when the hidden sector has a *private bath*. A shared bath, an undamped coupled boundary direction, or a noiseless visible mode makes the hidden state legible.
- **Impedance alone.** The visibility spectrum is the past–future canonical-correlation spectrum of the boundary random force. It is therefore fixed by the dissipative boundary impedance alone, which explains why it does not depend on temperature and makes it measurable at the boundary.
- **Compression.** Dropping hidden coordinates in order of visibility yields a smaller *physical* network that keeps every retained visibility exactly. In pinned chains the spectrum decays geometrically, so the boundary's memory of an infinite chain is effectively finite-dimensional.

We close with a prospective RC-circuit test, including exact finite-record predictions and trial budgets. The results are theorems about classical Gaussian networks, supported by author certificates; no experiment has been performed.

## 1. Claims, scope, and positioning

The paper has three parts.

**Part I — boundary consistency (Sections 2–7).** For the network class below, reduce the response, transport the complete random-force law, marginalize the thermal reference, and keep the conditional preparation cost. Doing this in stages gives the same final response, noise, reference state, and total information loss as eliminating all hidden coordinates at once. This is the finite theorem behind the statement that a change of boundary must carry its discarded information and induced fluctuations with it. It does not identify energy loss, state relative entropy, and noise covariance as one scalar. The naive quantum version fails, and the true quantum marginal is computed explicitly.

**Part II — what a boundary can know (Sections 8–11).** A hidden preparation that leaves the present boundary marginal unchanged can still alter the boundary's future. For the entire continuous boundary record we prove the following.

1. The preparation-to-record channel is an exact Gaussian attenuation channel. Its visibility matrix $\Pi_\tau$ gives the record's relative entropy in closed form and a sharp, strictly subunit contraction coefficient for every finite-entropy preparation (Section 8).
2. Known boundary feedback cannot improve the ideal experiment, and in pinned chains deep preparations are screened exponentially (Sections 8.8–8.9). Open-loop boundary forcing harvests from a hidden mean exactly $T$ times what the record learns, and its unavoidable dissipation is $T$ times the posterior slack (Section 8.10).
3. Overdamped networks with any friction keep the closed form. Inertial networks need one Riccati equation. The ceiling is strict exactly when the hidden sector has a *private* bath: a shared bath, an undamped boundary direction, or a noiseless hidden mode makes part of the hidden state fully legible (Section 9).
4. The visibility spectrum is the past–future canonical-correlation spectrum of the boundary random force. It is therefore fixed by the dissipative boundary impedance alone, which explains its temperature independence and makes it measurable at the boundary (Section 10).
5. Truncating hidden coordinates in visibility order yields a smaller *physical* network that keeps every retained visibility exactly (Section 11).

**Part III — test and accounting (Sections 12–14).** A prospective thermal-circuit test with exact finite-record predictions and trial budgets, a statement of what is and is not established, and author certificates.

**Assumptions.** There are finitely many real coordinates. The stiffness $K=K^{\mathsf T}\succ0$ is pinned, or already restricted to a specified complement of its zero modes. The temperature is $T>0$ and $k_B=1$. All noises are Gaussian. External applied forces are specified, and internal applied forces are set to zero when a boundary response is defined. Frequencies are real unless stated otherwise.

- **Part I** uses constant friction $\Gamma=\Gamma^{\mathsf T}\succ0$ and either $M=0$ (overdamped) or $M=M^{\mathsf T}\succ0$ (inertial). Cross-coordinate friction and mass terms are allowed.
- **Part II.** Section 8 uses overdamped unit friction. Section 9 allows arbitrary $\Gamma\succ0$ in the overdamped case, and $\Gamma\succeq0$ with $M\succ0$ and a unique Gibbs law in the inertial case. Section 10 assumes block-diagonal friction. Section 11 is overdamped.

Strict positivity avoids undamped poles, nonnormalizable translation modes, and descriptor-system qualifications wherever it is assumed. Where Section 9 relaxes it, the consequences are the subject of the theorems. No continuum limit, scale separation, weak inter-node coupling, or Markov approximation after elimination is used. A finite network coupled to ideal white-noise baths is an open stochastic system, not a finite closed Hamiltonian bath.

**Notation.** $X^\dagger$ is the conjugate transpose, $\operatorname{Re}_HX=(X+X^\dagger)/2$, and $\operatorname{Im}_HX=(X-X^\dagger)/(2i)$. Fourier transforms use $\widehat f(\omega)=\int e^{-i\omega t}f(t)\,dt$, so differentiation becomes $i\omega$. Noise spectra are two-sided: $\langle\widehat\xi(\omega)\widehat\xi(\omega')^\dagger\rangle=2\pi\delta(\omega-\omega')S_\xi(\omega)$. The visibility eigenvalues are $\pi_i$, and their largest value is $\lambda_\tau=\lambda_{\max}(\Pi_\tau)$.

**Provenance.** The ingredients are classical, and no component is claimed as historically new without a separate audit.

- Schur complements, Gaussian conditioning, the KL chain rule, and linear generalized Langevin reduction are classical. Ford–Kac–Mazur (1965) and Zwanzig (1973) are the canonical antecedents for harmonic-bath reduction and for the initial-state dependence of the random force. Schur associativity is the Crabtree–Haynsworth quotient identity (1969).
- Kalman–Bucy filtering (1961) supplies the Riccati framework. Its convergence theory (Kwakernaak–Sivan 1972; Anderson–Moore 1979) and the Bryson–Johansen (1965) treatment of perfect measurements are used in Section 9.
- The arbitrary-preparation contraction uses the Gaussian strong data-processing inequality (Polyanskiy–Wu; Anantharam–Gohari–Kamath–Nair) and Gaussian log-Sobolev entropy decay (Gross 1975).
- Canonical correlations of stationary processes and stochastically balanced realizations are due to Akaike (1975) and Desai–Pal (1984); see Lindquist–Picci (2015). Section 10 uses them without modification; its contribution is the physical identification.
- Within this program, Paper 55 supplies passive Kron reduction, Paper 56 its classical modular Hamiltonian, and Paper 58 a scalar conditional-refinement example. Baez–Fong give compositional passive-network semantics, and Ma–Li–Liu are a modern Langevin-reduction reference.

**Positioning against the closest prior work.** A focused primary-source comparison (October 9, 2026; not an exhaustive priority search) found the following.

- **Spatial exponent.** The exponent in Theorem 8.8 is already present in lattice controllability-Gramian decay (Klickstein–Sorrentino 2020). What is shown here is its transfer to thermal preparation relative entropy with bounds uniform in chain length.
- **Feedback neutrality.** This is an established principle in force sensing (Harris et al. 2013). Theorem 8.7 identifies the invariant experiment explicitly.
- **Observability versus recoverability.** Information-based stochastic observability (Subaşı–Demirekler 2014; Baram–Kailath 1988; Powel–Morgansen) already separates posterior improvement from deterministic observability. Studies of continuously monitored quantum systems already treat information acquisition competing with environmental loss.

The defensible claims are specific to this setting:

- the exact thermal preparation-to-record channel and its closed ceiling (Section 8);
- the private-bath criterion and the degenerate-boundary recursion (Section 9);
- the identification of visibility with the canonical correlations of the GLE random force, with its impedance-only consequence (Section 10);
- hereditary, structure-preserving visibility truncation (Section 11).

Reviewers may regard the combination as a useful specialization of control and information theory unless the physical predictions of Section 12 are tested.

## 2. Static boundary, thermal marginal, and response

Split the coordinates as $q=(x,y)$, with $x\in\mathbb R^b$ retained and $y\in\mathbb R^h$ hidden. Write
$$
K=\begin{pmatrix}A&B\\B^{\mathsf T}&C\end{pmatrix},\qquad
K_B=A-BC^{-1}B^{\mathsf T},\qquad L=-C^{-1}B^{\mathsf T}.
$$
The subscript $B$ on $K_B$ denotes the boundary; the unscripted $B$ denotes the off-diagonal block.

**Theorem 2.1 (static bridge).** For $H(q)=q^{\mathsf T}Kq/2$ and $\sigma(dq)=Z_K^{-1}e^{-H(q)/T}\,dq$:

1. $K_B\succ0$, and
   $$H(x,y)=\tfrac12x^{\mathsf T}K_Bx+\tfrac12(y-Lx)^{\mathsf T}C(y-Lx).$$
2. The normalized marginal is $\sigma_B=\mathcal N(0,TK_B^{-1})$, and
   $$\sigma(dy\mid x)=\mathcal N(Lx,TC^{-1})(dy).$$
3. With force $f$ applied only to $x$, the static compliance is $K_B^{-1}$. At thermal equilibrium,
   $$\frac{\partial\langle x\rangle_f}{\partial f}=K_B^{-1}
   =\frac1T\operatorname{Cov}_{\sigma_B}(x).$$
4. For the family of retained mean displacements $\mathcal N(m_B,TK_B^{-1})$, the Fisher matrix in the **mean coordinates** $m_B$ is $K_B/T$. Thus compliance and mean-coordinate Fisher information are inverse matrices up to $T$; they are not literally the same matrix in the same coordinates.

*Proof.* Complete the square. Positivity of $K_B$ follows by minimizing the strictly positive quadratic form over $y$ at fixed nonzero $x$. The change $(x,y)\mapsto(x,z=y-Lx)$ has unit Jacobian and factorizes the density into independent Gaussians of precisions $K_B/T$ and $C/T$. Minimizing $H-f^{\mathsf T}x$ gives $y=Lx$ and $K_Bx=f$. Exponential tilting by the same force gives the same mean and covariance. Finally, the mean-family score is $(TK_B^{-1})^{-1}(x-m_B)$, whose covariance is $K_B/T$. $\square$

**Normalization must be kept when the geometry changes.** The unnormalized partition function satisfies
$$
Z_K=Z_{K_B}\,(2\pi T)^{h/2}(\det C)^{-1/2},\qquad
\det K=\det C\det K_B.
$$
Accordingly the effective free-energy function obtained by integrating out $y$ is
$$
H_{\rm mf}(x)=\tfrac12x^{\mathsf T}K_Bx
-\tfrac{hT}{2}\log(2\pi T)+\tfrac T2\log\det C.
$$
The last two terms cancel out of a normalized marginal but matter for free-energy differences between networks. Changing the number of coordinates also requires a common choice of phase-space measure and a preparation protocol; raw differential entropies at different dimensions are not an invariant capacity measure.

## 3. Conditional preparation and the information defect

Let $\mathcal C_B\rho=\rho_B$ denote marginalization. Define **thermal conditional refinement** by
$$
(\mathcal R_\sigma p)(dx,dy)=p(dx)\,\sigma(dy\mid x).
$$
It is a classical Markov kernel and $\mathcal C_B\mathcal R_\sigma=\mathrm{id}$. It restores a chosen thermal conditional, not an arbitrary original hidden state.

**Theorem 3.1 (conditional free-energy identity).** For any $\rho$ with finite $D(\rho\Vert\sigma)$,
$$
\boxed{
D(\rho\Vert\sigma)
=D(\rho_B\Vert\sigma_B)+J_B(\rho),\qquad
J_B(\rho)=\mathbb E_{\rho_B}D(\rho(dy\mid x)\Vert\sigma(dy\mid x)).
}
$$
Moreover,
$$
J_B(\rho)=D(\rho\Vert\mathcal R_\sigma\rho_B),\qquad
D(\mathcal R_\sigma p\Vert\sigma)=D(p\Vert\sigma_B).
$$
Thus $J_B\ge0$, with equality exactly when the actual conditional is thermal for $\rho_B$-almost every $x$. Among all extensions of a fixed marginal $p$, $\mathcal R_\sigma p$ uniquely minimizes relative entropy to $\sigma$.

Whenever the energy and entropy expressions are finite, with $F_K(\rho)=\mathbb E_\rho H-TS(\rho)$,
$$
F_K(\rho)-F_K(\mathcal R_\sigma\rho_B)=T J_B(\rho).
$$
This is an exact constrained free-energy excess. Its interpretation as an achievable work cost additionally requires suitable isothermal controls. It is not automatically a one-shot work yield or a cyclic-unitary ergotropy.

*Proof.* Factor both densities into marginal and conditional densities in $\log(d\rho/d\sigma)$, and integrate. For $\mathcal R_\sigma p$, the conditional logarithmic ratio is zero. Replacing $\sigma$ in the denominator by $\mathcal R_\sigma\rho_B$ leaves precisely the conditional term. Gibbs' inequality gives nonnegativity and equality. Finally $TD(\rho\Vert\sigma)=F_K(\rho)+T\log Z_K$; subtract the two equalities on the same full state space. $\square$

**Corollary 3.2 (Gaussian formula).** Suppose $\rho=\mathcal N(m,\Sigma)$ is faithful, with blocks
$$
R=\Sigma_{y x}\Sigma_{xx}^{-1},\qquad
V=\Sigma_{yy}-\Sigma_{yx}\Sigma_{xx}^{-1}\Sigma_{xy},\qquad
V_*=TC^{-1},\qquad d=m_y-Lm_x.
$$
Then
$$
\boxed{
J_B=\tfrac12\left[
\operatorname{tr}(V_*^{-1}V)-h+\log\frac{\det V_*}{\det V}
+d^{\mathsf T}V_*^{-1}d
+\operatorname{tr}\big(V_*^{-1}(R-L)\Sigma_{xx}(R-L)^{\mathsf T}\big)
\right].
}
$$
The three contributions measure conditional covariance mismatch, conditional mean offset, and conditional dependence on the retained coordinates. For $\rho=\mathcal N(m,TK^{-1})$ only the mean offset survives:
$$
J_B=\frac{(m_y-Lm_x)^{\mathsf T}C(m_y-Lm_x)}{2T}.
$$

*Proof.* The actual conditional has covariance $V$ and mean $m_y+R(x-m_x)$. Its displacement from the reference conditional is $d+(R-L)(x-m_x)$. Insert the usual Gaussian relative-entropy formula and average its quadratic mean term. $\square$

**Refinement form.** Start from any coarse law $p$. Prepare
$$
y=Lx+a+\epsilon,\qquad \epsilon\sim\mathcal N(0,V),
$$
independently of $x$. The increment relative to compatible coarse and fine thermal references is
$$
J=\tfrac12\left[\operatorname{tr}(CV/T)-h-\log\det(CV/T)
+a^{\mathsf T}Ca/T\right].
$$
It is independent of $p$, and vanishes precisely at $a=0$, $V=TC^{-1}$. Paper 58 is the case $h=1$, $a=0$, $C=4k$, $V=\varepsilon$. Growth at thermal conditional preparation adds no relative-entropy resource, even if arbitrarily fast.

Zero $J$ does not say that constructing new nodes or changing the Hamiltonian costs no work. It says that no *excess over the new compatible thermal reference* was inserted. Hardware formation, changes in equilibrium free energy, and the preparation apparatus have separate physical budgets.

For repeated compatible refinements followed by reference-preserving relaxation steps,
$$
D_N=D_0+\sum_kJ_k-\sum_k\ell_k,\qquad \ell_k\ge0.
$$
Here each $J_k$ is computed against that refinement's conditional reference and $\ell_k$ is the actual relative-entropy decrease during the following relaxation. This is a resource budget, not a claim that $\ell_k$ equals every definition of total entropy production. Under inertial dynamics use the full phase-space state for the relaxation inequality; position marginal dynamics alone is generally not Markov.

Compatibility here means that the new fine reference has the **old reference as its marginal**. If its marginal is instead $\sigma'_B\ne\sigma_B$, the insertion step also contributes $D(p\Vert\sigma'_B)-D(p\Vert\sigma_B)$, which need not be nonnegative. Fresh attachments with no compensating stiffness change need not be Kron-compatible.

## 4. Exact dynamic elimination and induced noise

Consider the force-driven Langevin network
$$
M\ddot q+\Gamma\dot q+Kq=f+\xi,
\qquad \mathbb E\xi(t)\xi(u)^{\mathsf T}=2T\Gamma\,\delta(t-u).
$$
For $M=0$ interpret this as an overdamped SDE. For $M\succ0$ the equilibrium phase-space covariance in $(q,v)$ coordinates is
$$
\operatorname{Cov}(q,v)=\operatorname{diag}(TK^{-1},TM^{-1}).
$$
The deterministic energy derivative is $-v^{\mathsf T}\Gamma v$, and $K,\Gamma\succ0$ exclude nonzero undamped modes. The drift is stable; substituting the stated covariance in its Lyapunov equation verifies the unique stationary Gaussian. For $M=0$, substituting $TK^{-1}$ in the overdamped Lyapunov equation gives the same position marginal.

Define the dynamic stiffness, velocity impedance, and elimination map
$$
D(s)=K+s\Gamma+s^2M,\qquad Z(s)=D(s)/s,
$$
$$
E_B(s)=\begin{bmatrix}I&-D_{B I}(s)D_{I I}(s)^{-1}\end{bmatrix},
\qquad
D_B(s)=D_{BB}(s)-D_{BI}(s)D_{II}(s)^{-1}D_{IB}(s).
$$
Block labels in this section denote index sets. They do not reuse the static off-diagonal matrix $B$ from Section 2.

**Theorem 4.1 (response, passivity, and noise reduce together).**

1. With no internal applied force, the exact retained response is
   $$\chi_B(s)=D_B(s)^{-1}=[D(s)^{-1}]_{BB}.$$
   Its zero-frequency limit is $\chi_B(0)=K_B^{-1}$.
2. $Z_B(s)=D_B(s)/s$ is positive-real on $\operatorname{Re}s>0$. The response is causal and stable; the reduced dynamic stiffness is generally rational, not a new constant-coefficient mass/friction/stiffness polynomial.
3. In a stationary realization on the whole time axis, the effective force noise is
   $$\widehat\eta_B(\omega)=E_B(i\omega)\widehat\xi(\omega),\qquad
   Q_B(\omega)=2T E_B(i\omega)\Gamma E_B(i\omega)^\dagger.$$
   This noise is generally colored and correlated across retained nodes. For $\omega\ne0$,
   $$\boxed{
   Q_B(\omega)=\frac{2T}{\omega}\operatorname{Im}_H D_B(i\omega)
   =2T\operatorname{Re}_H Z_B(i\omega).
   }$$
4. At equilibrium the boundary position spectrum satisfies
   $$\boxed{
   S_{x}(\omega)=\chi_B Q_B\chi_B^\dagger
   =-\frac{2T}{\omega}\operatorname{Im}_H\chi_B(i\omega).
   }$$
   The minus sign follows from the declared Fourier convention. The zero-frequency values are the continuous limits. Integrating the spectrum gives
   $$\frac1{2\pi}\int_{-\infty}^{\infty}S_x(\omega)\,d\omega
   =T K_B^{-1}.$$

*Proof.* Solving the internal block equation gives the Schur response and the transformed force. Equivalently,
$$
E_BD=\begin{bmatrix}D_B&0\end{bmatrix},\qquad E_BDE_B^\dagger=D_B.
\tag{4.1}
$$
The latter is a pointwise congruence identity; it remains true although $E_B$ depends on frequency.

For $\operatorname{Re}s>0$,
$$
\operatorname{Re}_H Z(s)
=(\operatorname{Re}s)M+\Gamma+\operatorname{Re}(s^{-1})K\succ0.
$$
This also makes $Z_{II}$, hence $D_{II}$, invertible there. Equation (4.1), divided by $s$, gives $Z_B=E_BZE_B^\dagger$ and therefore positivity of its Hermitian part. The rational internal inverse is stable by the same energy argument for the pinned internal subsystem. Proper inverse response and stable poles give causality. At $s=i\omega$, $D-D^\dagger=2i\omega\Gamma$; take the anti-Hermitian part of (4.1) to obtain the noise identity.

The inverse identity
$$
\operatorname{Im}_H D_B^{-1}
=-D_B^{-1}(\operatorname{Im}_H D_B)D_B^{-\dagger}
$$
gives the position FDT. The integral is the stationary covariance of the same retained process, which equals the retained block of $TK^{-1}$; Theorem 2.1 identifies that block as $TK_B^{-1}$. $\square$

**Force sources and initial data cannot be erased.** If internal forces are present the reduced applied force is $f_B-D_{BI}D_{II}^{-1}f_I$, not simply $f_B$. For a one-sided Laplace transform starting at $0$, the exact equation is
$$
D_B(s)\widehat x(s)=E_B(s)\left[\widehat f(s)+\widehat\xi(s)
+(sM+\Gamma)q(0)+M\dot q(0)\right].
\tag{4.2}
$$
For $M=0$ omit the mass terms. Equation (4.2) retains the full joint distribution of initial data. Stationary spectral formulas cannot be substituted for arbitrary nonthermal initial preparations without their transient terms. The next section gives these terms explicitly.

## 5. Conditional preparation becomes a memory-force transient

For a transparent finite-time formula specialize to overdamped unit friction,
$$
\dot x=-Ax-By+f_B+\xi_B,\qquad
\dot y=-B^{\mathsf T}x-Cy+\xi_I,
$$
with independent white noises of covariance $2T I\delta$. The matrices $A,B,C$ are again those of Section 2. Put
$$
z_0=y(0)-Lx(0),\qquad
\mathsf G(t)=B e^{-Ct}C^{-1}B^{\mathsf T}\quad(t\ge0).
$$

**Theorem 5.1 (finite-time memory and preparation bridge).** The retained coordinates obey exactly
$$
\boxed{
\dot x(t)+\int_0^t\mathsf G(t-u)\dot x(u)\,du+K_Bx(t)
=f_B(t)+\eta(t),
}
$$
where
$$
\eta(t)=\xi_B(t)-B e^{-Ct}z_0
-B\int_0^t e^{-C(t-u)}\xi_I(u)\,du.
\tag{5.1}
$$
The convolution with $\dot x$ is understood through the integrated SDE (or integration by parts against its deterministic smooth kernel), not as a classical derivative of Brownian paths.

If the hidden conditional is thermal, $z_0\sim\mathcal N(0,TC^{-1})$ independently of $x(0)$ and future noises, then the random force has zero mean, is independent of $x(0)$, and
$$
\boxed{
\mathbb E\eta(t)\eta(u)^{\mathsf T}
=2T I\delta(t-u)+T\mathsf G(|t-u|).
}
\tag{5.2}
$$
This is the exact second FDT of the reduced memory equation. It holds even when the retained initial law is nonthermal; stationarity of $x$ itself also requires a thermal retained initial law.

For a nonthermal independent residual $z_0\sim\mathcal N(a,V)$,
$$
\mathbb E\eta(t)=-B e^{-Ct}a,
$$
$$
\boxed{
\operatorname{Cov}(\eta(t),\eta(u))
=2T I\delta(t-u)+T\mathsf G(|t-u|)
+B e^{-Ct}(V-TC^{-1})e^{-Cu}B^{\mathsf T}.
}
\tag{5.3}
$$
Its conditional preparation cost is exactly the $J$ of Section 3. A general Gaussian conditional replaces $a$ by $a(x(0))=m_y+R(x(0)-m_x)-Lx(0)$ when conditioning on $x(0)$; it consequently also introduces initial boundary/force correlations. Corollary 3.2 includes their information cost.

These transient formulas and $J$ depend on the same preparation parameters; they do not equate a transient amplitude with relative entropy. Their quantitative observable link is the full-path formula in Theorem 8.2 and Corollary 8.6.

*Proof.* Solve the hidden equation by variation of constants and substitute it into the retained equation. Integration by parts gives
$$
\int_0^t e^{-C(t-u)}B^{\mathsf T}x(u)\,du
=C^{-1}B^{\mathsf T}x(t)-e^{-Ct}C^{-1}B^{\mathsf T}x(0)
-\int_0^t e^{-C(t-u)}C^{-1}B^{\mathsf T}\dot x(u)\,du.
$$
Combining the initial term with $y(0)$ gives $z_0$ and proves (5.1). Under thermal conditional preparation, the process
$$
w(t)=e^{-Ct}z_0+\int_0^t e^{-C(t-u)}\xi_I(u)\,du
$$
is a stationary Ornstein–Uhlenbeck process with covariance $T e^{-C|t-u|}C^{-1}$. Since $\eta=\xi_B-Bw$ and the noises are independent, (5.2) follows. For nonthermal preparation, its mean gains $e^{-Ct}a$ and its covariance gains $e^{-Ct}(V-TC^{-1})e^{-Cu}$. This proves (5.3). $\square$

**Frequency check.** The Laplace transform of the memory kernel is
$$
\widehat{\mathsf G}(s)=B(sI+C)^{-1}C^{-1}B^{\mathsf T},
$$
and
$$
sI+A-B(sI+C)^{-1}B^{\mathsf T}
=K_B+s\big(I+\widehat{\mathsf G}(s)\big).
$$
For thermal preparation the force spectrum is
$$
Q_B(\omega)=2T\left[I+B(C^2+\omega^2I)^{-1}B^{\mathsf T}\right].
$$
These are precisely Theorem 4.1 in the unit-friction overdamped specialization.

**What does and does not become visible.** Nonzero $J$ need not create a detectable transient at a chosen boundary: a mode can lie in the kernel of every $B e^{-Ct}$. Thus the bridge gives an exact accounting and an upper bound on visibility, not a claim that every hidden preparation is observable.

## 6. Successive elimination: response, noise, reference, and cost

Partition the coordinates into $X,Y,Z$. First eliminate $Z$, retain $A=X\cup Y$, then eliminate $Y$.

**Theorem 6.1 (composition).**

**(a) Response and sources.** Let $D^{(1)}$ be the Schur reduction to $A$, with elimination map $E_1$, and let $D^{(2)}$ be its reduction to $X$, with map $E_2$. If $D_X,E_X$ denote direct elimination of $Y\cup Z$, then
$$
D^{(2)}=D_X,\qquad E_2E_1=E_X.
\tag{6.1}
$$
The identities hold at every regular $s$ and as rational identities. They apply equally to deterministic forces, stochastic forces, and the initial-data source in (4.2).

**(b) Noise.** For any full force spectral covariance $Q(\omega)$, thermal or not,
$$
Q^{(1)}=E_1QE_1^\dagger,\qquad
Q^{(2)}=E_2Q^{(1)}E_2^\dagger=E_XQE_X^\dagger.
\tag{6.2}
$$
For a common temperature this is the FDT covariance of the final Schur response. Intermediate cross-correlations must be retained; replacing $Q^{(1)}$ by its diagonal generally destroys (6.2).

**(c) Thermal references and recovery.** At zero frequency, stiffness Schur complements are associative; the reference marginal on $X$ is independent of order. Compatible conditional refinements satisfy
$$
\mathcal R_{XY\to XYZ}\,\mathcal R_{X\to XY}=\mathcal R_{X\to XYZ}.
\tag{6.3}
$$
In particular their Gaussian means, conditional covariances, and normalization determinants compose.

**(d) Conditional costs.** For any initial full law with finite relative entropy,
$$
\boxed{
D(\rho\Vert\sigma)-D(\rho_X\Vert\sigma_X)
=\left[D(\rho\Vert\sigma)-D(\rho_{XY}\Vert\sigma_{XY})\right]
+\left[D(\rho_{XY}\Vert\sigma_{XY})-D(\rho_X\Vert\sigma_X)\right].
}
\tag{6.4}
$$
Each bracket is a nonnegative conditional cost. The total is independent of the elimination order, although the allocation between stages need not be.

*Proof.* For (a), multiply the block identities
$$
E_1D=[D^{(1)},0],\qquad E_2D^{(1)}=[D^{(2)},0].
$$
Then $E_2E_1D$ has zero hidden columns and identity coefficient on the retained variables in $E_2E_1$. The hidden-block linear system has a unique solution, namely $-D_{X,I}D_{I,I}^{-1}$; hence $E_2E_1=E_X$ and the retained block is $D_X$. This also proves static associativity. Part (b) is congruence composition. Part (c) is the conditional chain rule
$$
\sigma(dy\mid x)\sigma(dz\mid x,y)=\sigma(dy,dz\mid x).
$$
Its Gaussian version follows either by conditioning or by the same block factorization. Part (d) telescopes; the KL chain rule identifies and signs both brackets. $\square$

**Scope of order independence.** This theorem compares exact descriptions of the same network and the same state or source law. Two physically different nonthermal refinement protocols need not yield the same state, work cost, or trajectories. Order independence does not license resetting intermediate noises or conditionals to new thermal ones for free.

**Cascade companion.** For contractions $S_1,S_2$ and $\Delta(S)=I-SS^\dagger$,
$$
\Delta(S_2S_1)=\Delta(S_2)+S_2\Delta(S_1)S_2^\dagger.
$$
Independent hidden inputs at common available noise power $T$ give exactly this covariance law multiplied by $T$. This is a cascade identity, not the general formula for feedback interconnection. It is structurally parallel to (6.4), but an operator defect and a state-relative-entropy loss remain distinct objects.

## 7. Exact controls and the quantum boundary

### 7.1 Dropping induced noise fails even for two nodes

Take $K=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$, $M=\Gamma=I$, retain node 1, and evaluate at $\omega=1$. Then $D_{II}=1+i$ and $E=[1,(1+i)^{-1}]$. The true force spectrum is
$$Q_B=2T\left(1+\left|(1+i)^{-1}\right|^2\right)=3T.$$
Keeping only the retained node's original white source gives $2T$, contradicting the unchanged reduced response's FDT. A deterministic reduction followed by an arbitrary noise assignment is not the bridge.

### 7.2 Quantum thermal marginalization is not classical Kron reduction

For an isolated quantum harmonic network, $\hbar=1$, $M=I$, and $\Omega=K^{1/2}$,
$$
X=\tfrac12\Omega^{-1}\coth(\Omega/(2T)),\qquad
P=\tfrac12\Omega\coth(\Omega/(2T)).
$$
Partial trace retains covariance subblocks, which compose associatively. These subblocks are generally not the thermal covariance of the classical Schur stiffness with retained mass.

**Proposition 7.1 (exact thermal quantum counterexample).** Take
$$
K=\begin{pmatrix}5/2&-3/2\\-3/2&5/2\end{pmatrix},\qquad
T=\frac1{2\log2}.
$$
The normal frequencies are $1,2$, so $\coth(\log2)=5/3$ and $\coth(2\log2)=17/15$. For either one-node marginal,
$$
X_B=67/120,\qquad P_B=59/60,\qquad K_B=8/5,
$$
and
$$P_B-K_BX_B=9/100\ne0.$$
But an isolated single oscillator with mass 1 and stiffness $K_B$ satisfies $P_B=K_BX_B$ at every temperature. Thus the naive quantum Schur/Gibbs identification is false at a strictly positive, exactly specified temperature. $\square$

The quantum replacement is the actual Gaussian marginal and its modular Hamiltonian, which generally contains renormalized kinetic as well as potential terms; Proposition 7.3 computes it for a single retained mode. The classical result is recovered in the high-temperature limit. No claim here equates finite-temperature quantum entanglement with a classical conditional KL.

**Proposition 7.2 (universal quantum refinement obstruction).** A quantum channel $\mathcal R:B\to B\otimes I$ satisfying $\operatorname{Tr}_I\mathcal R(\rho)=\rho$ for every input state must have the form $\mathcal R(\rho)=\rho\otimes\tau_I$. Consequently such a universal right inverse cannot map a boundary reference to a correlated full reference.

*Proof.* Dilate $\mathcal R$ to an isometry $V:B\to B\otimes I\otimes E$. Preservation of a pure marginal forces $V|\psi\rangle=|\psi\rangle\otimes|e_\psi\rangle$. Apply this to basis vectors and their superpositions. Linearity and preservation of the superposed pure marginal force the environment vectors to be the same (with phases absorbed consistently), so $V|\psi\rangle=|\psi\rangle\otimes|e\rangle$. Tracing $E$ yields a fixed $\tau_I$. The same argument applies to normal oscillator channels through finite superpositions and continuity. $\square$

This does not forbid recovery on a restricted state family or commuting algebra. Quantum data processing and its loss composition remain valid; equality/recovery questions must be posed for the chosen family, rather than assuming the classical conditional kernel exists on all quantum states.

**Proposition 7.3 (the true quantum marginal is a thermal oscillator with renormalized mass).** Every zero-mean single-mode Gaussian state with uncorrelated $X=\langle x^2\rangle$, $P=\langle p^2\rangle$, and $XP>\tfrac14$ is the Gibbs state, at a prescribed temperature $T$, of a unique oscillator $p^2/(2m_{\rm eff})+m_{\rm eff}\omega_{\rm eff}^2x^2/2$, with
$$
\coth\frac{\omega_{\rm eff}}{2T}=2\sqrt{XP},\qquad m_{\rm eff}=\frac{\sqrt{P/X}}{\omega_{\rm eff}}.
\tag{7.1}
$$
This oscillator divided by $T$ is the modular Hamiltonian of the marginal. For the witness of Proposition 7.1, $2\sqrt{X_BP_B}=\sqrt{3953/1800}=1.4819282$, so $\omega_{\rm eff}=1.1822857$, $m_{\rm eff}=1.1224866$, and $k_{\rm eff}=m_{\rm eff}\omega_{\rm eff}^2=1.5690111$, against $K_B=8/5$. Quantum reduction raises the retained mass by 12.2% and lowers the stiffness by 1.9%. At high temperature $m_{\rm eff}\to1$ and $k_{\rm eff}\to K_B$, the classical bridge.

*Proof.* For the oscillator, $X=\coth(\omega/2T)/(2m\omega)$ and $P=m\omega\coth(\omega/2T)/2$. Hence $XP=\tfrac14\coth^2(\omega/2T)$ and $P/X=m^2\omega^2$. Since $\coth$ maps $(0,\infty)$ bijectively onto $(1,\infty)$, both relations invert uniquely. $\square$

**Remark 7.4 (Petz recovery is the correlated refinement on its natural domain).** The Petz map
$$
\mathcal P_\sigma(\rho_B)=\sigma^{1/2}\big(\sigma_B^{-1/2}\rho_B\sigma_B^{-1/2}\otimes I\big)\sigma^{1/2}
$$
is completely positive and trace preserving, and it maps $\sigma_B$ to the correlated reference $\sigma$ exactly. For commuting states it is the classical refinement $\mathcal R_\sigma$ of Section 3. By Proposition 7.2 it cannot be a right inverse of the partial trace on all states. How well it recovers a given state is controlled by the relative-entropy loss, through rotated Petz maps (Junge et al. 2018). This is the restricted recovery a quantum bridge requires: exact on the reference, approximate elsewhere, with the loss as the price.

### 7.3 The quantum frequency-domain congruence does survive, conditionally

Suppose a physically specified linear quantum Langevin model has the same retarded $D(s)$ and a common-temperature symmetrized force spectrum
$$
Q^{\rm sym}(\omega)=\nu_T(\omega)\Gamma,\qquad
\nu_T(\omega)=\hbar\omega\coth\left(\frac{\hbar\omega}{2T}\right).
$$
Then the algebra of Theorems 4.1 and 6.1 gives
$$
Q_B^{\rm sym}=\nu_T E_B\Gamma E_B^\dagger
=\frac{\nu_T}{\omega}\operatorname{Im}_H D_B,
$$
and successive elimination is still exact. This is a conditional algebraic extension, not a construction of every such bath or a claim that its strongly coupled stationary state equals the isolated system's Gibbs state. Bath commutators, ultraviolet regularization, and initial system–bath correlations require their own physical specification. In particular, it does not repair Proposition 7.1.

## 8. Exact Gaussian visibility of a hidden preparation

The general data-processing bound is retained as a baseline. The quantitative result for the unit-friction overdamped model of Section 5 is Theorem 8.2 and its corollaries: they compute the full continuous-path KL, its exact invisible directions, and its strict infinite-time ceiling. Section 9 extends the exact formula to arbitrary friction and to inertial networks, Section 10 identifies $\Pi_\infty$ with a canonical-correlation spectrum, and Section 11 uses that identification to compress boundary memory.

### 8.1 General bound

**Theorem 8.1 (boundary-history bound).** Fix the full dynamics and the same external driving protocol in two experiments. Let the initial states be $\rho$ and $\bar\rho=\mathcal R_\sigma\rho_B$. Let $\mathbb P_B^\rho$ and $\mathbb P_B^{\bar\rho}$ be the distributions of the retained trajectory on any fixed finite time interval. Then
$$
\boxed{
D(\mathbb P_B^\rho\Vert\mathbb P_B^{\bar\rho})\le J_B(\rho).
}
$$
The same bound holds for any sampled or noisy record obtained by a common observation channel. For inertial dynamics the initial state and refinement here must include all the relevant phase-space variables, not positions alone.

*Proof.* The stochastic evolution followed by observation of the boundary path is one Markov kernel $\mathcal P_B$ from the full initial state. Both experiments use the same kernel, including the same conditional distribution of bath noise given initial data (independent future thermal increments in the model above). Data processing and Theorem 3.1 give
$$
D(\mathcal P_B\rho\Vert\mathcal P_B\bar\rho)
\le D(\rho\Vert\bar\rho)=J_B(\rho).
$$
Further observation contracts relative entropy again. $\square$

The initial boundary marginals are identical, but their future histories need not be. This distinguishes a thermodynamically correct present marginal from a dynamically sufficient description. The memory/noise/preparation data supply the missing predictive content. A nonthermal retained marginal is allowed; only the reference conditional used to compare the two preparations is fixed.

### 8.2 Exact full-path formula

Use the unit-friction model of Section 5, with independent boundary and interior Brownian noises, $T>0$, $C\succ0$, and $K\succ0$. The record is the **entire continuous path $x|_{[0,\tau]}$, including $x(0)$**. The applied force is the same known deterministic function in the two experiments. The common initial boundary distribution is $\mu$. Initially,
$$
z_0=y(0)-Lx(0),\qquad
\bar\rho: z_0\sim\mathcal N(0,S),\quad
\rho: z_0\sim\mathcal N(a,V),\qquad S=TC^{-1},\quad V\succ0,
$$
independently of $x(0)$ and future noises. The common $\mu$ need not be thermal or Gaussian in this independent-residual case.

Define the deterministic **initial-state information matrix** $\mathcal I_\tau$ by
$$
\boxed{
\frac{d\mathcal I_\tau}{d\tau}
=\frac{B^{\mathsf T}B}{2T}-C\mathcal I_\tau-\mathcal I_\tau C-2T\mathcal I_\tau^2,
\qquad\mathcal I_0=0.
}
\tag{8.1}
$$
This is an information equation for the **initial hidden state**, not the usual forward covariance of the current hidden state. Let
$$
\Xi_\tau=S^{1/2}\mathcal I_\tau S^{1/2},\qquad
\Pi_\tau=\Xi_\tau(I+\Xi_\tau)^{-1},\qquad
\alpha=S^{-1/2}a,\qquad W=S^{-1/2}VS^{-1/2},
$$
$$
\Omega_\tau=I+\Pi_\tau^{1/2}(W-I)\Pi_\tau^{1/2}.
$$
All square roots are symmetric positive square roots. The matrix $\Pi_\tau$ is the **visibility matrix**: $0\preceq\Pi_\tau\prec I$ for every finite horizon.

**Theorem 8.2 (exact Gaussian visibility).** The relative entropy between the two boundary path laws is
$$
\boxed{
\mathcal D_\tau:=D(\mathbb P_x^\rho|_{[0,\tau]}\Vert\mathbb P_x^{\bar\rho}|_{[0,\tau]})
=\frac12\left[
\alpha^{\mathsf T}\Pi_\tau\alpha
+\operatorname{tr}\big(\Pi_\tau(W-I)\big)
-\log\det\Omega_\tau
\right].
}
\tag{8.2}
$$
The initial conditional preparation KL is
$$
J=\tfrac12\left[\alpha^{\mathsf T}\alpha+\operatorname{tr}(W-I)-\log\det W\right].
\tag{8.3}
$$
Thus (8.2), rather than $\mathcal D_\tau\le J$, is the exact Gaussian replacement for Theorem 8.1. It is a finite-matrix formula for a continuous path law, not a time-sampling approximation. For continuous observation with known dynamics it depends on $B,C,T$ and the conditional preparation; it does not depend on the retained stiffness $A$ or on $\mu$.

*Proof, step 1: remove known boundary feedback.* Set
$$
g(t)=e^{-Ct}Lx(0)-\int_0^t e^{-C(t-u)}B^{\mathsf T}x(u)\,du,
\qquad h(t)=y(t)-g(t).
$$
Then $dh=-Ch\,dt+\sqrt{2T}\,dW_I$, with $h(0)=z_0$. From the observed path form
$$
dY(t)=dx(t)+[Ax(t)+Bg(t)-f_B(t)]dt.
$$
It obeys the standard linear Gaussian observation model
$$
\boxed{
dh=-Ch\,dt+\sqrt{2T}\,dW_I,
\qquad dY=-Bh\,dt+\sqrt{2T}\,dW_B.
}
\tag{8.4}
$$
For fixed $x(0)$ the transformation between $x$ and $Y$ is causal, invertible, and independent of $a,V$: its inverse is the unique solution of the linear Volterra equation defining $g$. It preserves relative entropy. Under $\bar\rho$, the transformed observation is independent of $x(0)$; under the independent-residual $\rho$ it is as well. This proves the absence of $A$ and $\mu$ in the answer.

*Step 2: finite sufficient statistic for the whole path.* Conditional on $z_0=z$, (8.4) is a Gaussian channel with deterministic mean observation derivative $-Be^{-Ct}z$ and a covariance independent of $z$. On a finite interval the observation covariance has the strictly positive white-noise component $2T I$, so its Cameron–Martin information is finite. Gaussian completion of the square in the path likelihood gives
$$
\frac{d\mathbb P^z}{d\mathbb P^0}(Y)
=\exp\left(z^{\mathsf T}s_\tau(Y)-\tfrac12 z^{\mathsf T}\mathcal I_\tau z\right),
\qquad
s_\tau\mid z\sim\mathcal N(\mathcal I_\tau z,\mathcal I_\tau).
\tag{8.5}
$$
One concrete operator definition is $\mathcal I_\tau=\mathcal O_\tau^*\mathcal N_\tau^{-1}\mathcal O_\tau$, where $(\mathcal O_\tau z)(t)=-Be^{-Ct}z$ and $\mathcal N_\tau$ is the observation-derivative covariance for $h(0)=0$. Its positive white component makes the inverse bounded on $L^2([0,\tau])$.

Equation (8.5) shows that all likelihood ratios obtained by mixing over initial preparations depend only on $s_\tau$. The conditional law of the remaining path given this statistic is common to both preparations. Consequently the path KL equals the statistic KL, even if $\mathcal I_\tau$ is singular.

*Step 3: compute the information.* A first infinitesimal observation interval adds $B^{\mathsf T}B\,d\tau/(2T)$ of information. Propagating a future likelihood backward through $h(d\tau)=(I-Cd\tau)h(0)+\mathcal N(0,2T I d\tau)$ transforms its quadratic coefficient $\mathcal I$ to
$$
(I-Cd\tau)^{\mathsf T}
\left[\mathcal I-2T\mathcal I^2d\tau\right](I-Cd\tau)+o(d\tau).
$$
This follows by Gaussian integration of the future exponential-quadratic likelihood; linear score terms affect the new score and normalization, not this quadratic coefficient. Time homogeneity and the empty-horizon value give (8.1). Equivalently it is the backward Gaussian information Riccati equation for (8.4).

For a separate forward computation, put $N=B^{\mathsf T}B/(2T)$ and solve
$$
\dot P=-CP-PC+2TI-PNP,\quad P(0)=0,
\qquad\dot U=(-C-PN)U,\quad U(0)=I.
$$
Whitening the observations by this zero-initial-state Kalman filter gives
$$
\mathcal I_\tau=\int_0^\tau U(t)^{\mathsf T}N U(t)\,dt.
\tag{8.6}
$$
This independently computes the same likelihood coefficient. The certificate checks the two Riccati calculations against each other and against full-network sampled paths.

*Step 4: normalize the sufficient statistic.* With $u=S^{-1/2}z_0$, a linear transformation of (8.5) on its range, an orthogonal change of output coordinates, and the addition of independent irrelevant standard normals on its kernel give the equivalent canonical channel
$$
r=\Pi_\tau^{1/2}u+(I-\Pi_\tau)^{1/2}\epsilon,
\qquad\epsilon\sim\mathcal N(0,I).
\tag{8.7}
$$
For example, first whiten the score noise to obtain $\mathcal I_\tau^{1/2}S^{1/2}u+\epsilon$, use polar decomposition to replace its signal matrix by $\Xi_\tau^{1/2}$, and whiten the reference covariance $I+\Xi_\tau$. Independent kernel components change neither likelihood ratios nor KL.

The reference input is $u\sim\mathcal N(0,I)$, hence the reference output is $r\sim\mathcal N(0,I)$. The actual output is $\mathcal N(\Pi_\tau^{1/2}\alpha,\Omega_\tau)$. Its finite-dimensional Gaussian relative entropy is exactly (8.2). $\square$

### 8.3 Closed finite- and infinite-time information

**Proposition 8.3 (explicit solution and thermal visibility ceiling).** Put
$$
F=(C^2+B^{\mathsf T}B)^{1/2},
$$
$$
X_\tau=\cosh(F\tau)+F^{-1}\sinh(F\tau)C,
\qquad
Y_\tau=F\sinh(F\tau)+\cosh(F\tau)C.
$$
Then
$$
\mathcal I_\tau=\frac{Y_\tau X_\tau^{-1}-C}{2T},
\qquad
\boxed{\mathcal I_\infty=\frac{F-C}{2T}.}
\tag{8.8}
$$
The products need not commute; their order in (8.8) is part of the formula. Although $Y_\tau X_\tau^{-1}$ is not manifestly symmetric, it is symmetric by its Riccati equation. For long numerical horizons use that equation or the algebraic limit rather than overflowing matrix hyperbolic functions.

The information and visibility matrices increase in Loewner order with the horizon and converge. In particular,
$$
\boxed{
\Pi_\infty=I-2C^{1/2}(C+F)^{-1}C^{1/2}\prec I.
}
\tag{8.9}
$$
For Gaussian preparations, the full-path KL on $[0,\infty)$ is (8.2) with $\Pi_\infty$.

*Proof.* With $R=C+2T\mathcal I$, (8.1) becomes $\dot R=F^2-R^2$, $R(0)=C$. The displayed $X,Y$ solve $\dot X=Y$, $\dot Y=F^2X$; hence $R=YX^{-1}$ solves the Riccati equation with that initial value.

Additional observations increase Fisher information in the likelihood (8.5). Also $\mathcal N_\tau\succeq2TI$, so
$$
0\preceq\mathcal I_\tau\preceq\frac1{2T}\int_0^\infty e^{-Ct}B^{\mathsf T}Be^{-Ct}\,dt,
$$
which is finite since $C\succ0$. Thus $\mathcal I_\tau$ has a finite limit, which solves the autonomous algebraic Riccati equation. Its $R=C+2T\mathcal I_\infty\succ0$ satisfies $R^2=F^2$, so $R=F$. Substitution into the definition of $\Pi$ proves (8.9). The subtracted matrix is positive definite, establishing the strict upper bound. Finally, the infinite-path sigma-algebra is generated by finite horizons; the variational characterization of relative entropy gives $\mathcal D_\infty=\sup_\tau\mathcal D_\tau$, and continuity of (8.2) supplies the stated limit. $\square$

**Remark 8.3a (temperature-independent visibility ceiling).** At fixed $B,C$ and horizon, the equation $\dot R=F^2-R^2$, $R(0)=C$, contains no temperature. Since
$$
\Xi_\tau=\tfrac12 C^{-1/2}(R_\tau-C)C^{-1/2},
$$
both $\Pi_\tau$ and its largest eigenvalue are independent of $T>0$. In particular, the infinite-time ceiling is determined entirely by the coupling $B$ relative to the hidden stiffness $C$. Equal bath strengths $2T$ make thermal randomization and observation noise scale together; lowering their common temperature cannot raise this ceiling. This statement concerns the dimensionless channel and its optimal visible fraction. For a fixed preparation in physical coordinates, $J$ and $\mathcal D_\tau$ can still change with $T$ because the thermal reference and normalization change. Preparations fixed in thermal coordinates have temperature-independent input and output KL. These conclusions use the equal-temperature, independent-bath, unit-friction overdamped model of this section. Corollary 10.2 derives the same invariance structurally, without the Riccati equation, and Proposition 9.3 extends it to every friction matrix.

**Remark 8.3b (coupling-angle form).** In the scalar case, with $\theta=\arctan(|b|/c)$, $\pi_\infty=(f-c)/(f+c)=b^2/(f+c)^2=\tan^2(\theta/2)$. If $C$ and $B^{\mathsf T}B$ commute, their common modes with eigenvalues $c_i>0$ and $b_i^2\ge0$ likewise have $\pi_i=\tan^2(\theta_i/2)$, $\theta_i=\arctan(b_i/c_i)\in[0,\pi/2)$. Thus each ceiling is below one and approaches one only as $b_i/c_i\to\infty$. This modewise angle interpretation requires commutation; it is not a replacement for the noncommuting matrix formula (8.9).

**Scalar example.** For one hidden decay rate $c>0$ and scalar coupling $b$, let $f=\sqrt{c^2+b^2}$. Then
$$
\mathcal I_\tau=\frac{b^2\sinh(f\tau)}{2T[f\cosh(f\tau)+c\sinh(f\tau)]},
\qquad
\boxed{\pi_\infty=\frac{\sqrt{c^2+b^2}-c}{\sqrt{c^2+b^2}+c}.}
\tag{8.10}
$$
For a pure mean preparation, the visible fraction is exactly $\mathcal D_\tau/J=\pi_\tau$. For a covariance ratio $w=V/S$ and normalized mean $\alpha$,
$$
\mathcal D_\tau=\tfrac12\left[\pi_\tau\alpha^2+\pi_\tau(w-1)
-\log(1+\pi_\tau(w-1))\right].
$$
At weak coupling $\pi_\infty=b^2/(4c^2)+O((b/c)^4)$. At finite $b,c$ it never equals 1. With $c=3,b=4$, it is exactly $1/4$; at $\tau=\log2/5$ the finite-time visibility is exactly $4/21$.

### 8.4 Invisible preparations, strictness, and sharp attenuation

**Theorem 8.4 (observability and exact visibility loss).** For every $\tau>0$:

1. The exact nullspace is
   $$\ker\mathcal I_\tau=\bigcap_{j=0}^{h-1}\ker(BC^j),$$
   the unobservable subspace of $(C,B)$. Thus $\ker\Pi_\tau=S^{-1/2}\ker\mathcal I_\tau$.
2. A Gaussian preparation is invisible, $\mathcal D_\tau=0$, exactly when
   $$\Pi_\tau^{1/2}\alpha=0,\qquad
   \Pi_\tau^{1/2}(W-I)\Pi_\tau^{1/2}=0.$$
   The covariance condition allows correlations between observable and dark coordinates to change without becoming visible. It is stronger and more precise than saying only that dark means are invisible.
3. **All finite-entropy preparations.** Let $\mu$ be the common initial boundary law and let $\nu_x$ be any conditional law of the normalized hidden residual $u=S^{-1/2}(y(0)-Lx(0))$ given $x(0)=x$. The reference conditional law is $\gamma=\mathcal N(0,I)$, and assume only
   $$J=\int D(\nu_x\Vert\gamma)\,\mu(dx)<\infty.$$
   Use the same dynamics and known forcing for both preparations, with future bath noises independent of the initial state, and include $x(0)$ in the boundary record. Let $\lambda_\tau=\lambda_{\max}(\Pi_\tau)$. Then, without any Gaussian assumption on $\nu_x$ or $\mu$,
   $$\boxed{0\le\mathcal D_\tau\le\lambda_\tau J,\qquad \lambda_\tau\le\lambda_\infty<1.}$$
   Also $\mathcal D_\infty\le\lambda_\infty J$. The coefficient is sharp over this entire class: already the Gaussian mean shifts $W=I$ with a nonzero $\alpha$ in a top eigenspace attain $\mathcal D_\tau/J=\lambda_\tau$, including the infinite-horizon limit. For $0<J<\infty$, the original data-processing inequality is **strict even at infinite time** in this model. Observable does not mean noiselessly recoverable. The closed KL formula (8.2) and item 2 remain Gaussian statements.

*Proof.* The covariance operator in (8.5) has bounded strictly positive inverse on finite intervals. Its Gram has the same kernel as $z\mapsto Be^{-Ct}z$. Analyticity and Cayley–Hamilton identify that kernel with the displayed finite intersection. Normalization gives the kernel of $\Pi$. Gaussian KL vanishes exactly when both mean and covariance equal the reference; this proves item 2.

For item 3, the likelihood factorization (8.5) and sufficient statistic do not depend on the initial prior. Thus, conditional on each $x(0)=x$, the boundary experiment is equivalent to the canonical channel (8.7), denoted $K_\Pi$, for every input law $\nu_x$. In particular,
$$
\mathcal D_\tau=\int D(\nu_xK_{\Pi_\tau}\Vert\gamma)\,\mu(dx).
$$
Take $0<\lambda=\lambda_{\max}(\Pi)<1$. Factor $K_\Pi$ into scalar attenuation with visibility $\lambda I$, followed by attenuation with visibility $\Pi/\lambda$. Their independent noise covariances compose to $I-\Pi$, and both channels preserve $\gamma$. The first channel is the Ornstein–Uhlenbeck semigroup $P_t$ on laws at $t=-\tfrac12\log\lambda$, with $P_t\nu$ the law of $e^{-t}u+\sqrt{1-e^{-2t}}\epsilon$.

For a smooth density relative to $\gamma$, entropy dissipation and the Gaussian logarithmic Sobolev inequality give
$$
\frac{d}{dt}D(P_t\nu\Vert\gamma)=-\mathsf I_\gamma(P_t\nu),
\qquad D(\eta\Vert\gamma)\le\tfrac12\mathsf I_\gamma(\eta),
$$
where $\mathsf I_\gamma(\eta)=\int\|\nabla\log(d\eta/d\gamma)\|^2\,d\eta$ is relative Fisher information. Hence
$$
D(P_t\nu\Vert\gamma)\le e^{-2t}D(\nu\Vert\gamma).
$$
Approximation by smooth densities with convergent relative entropy, followed by lower semicontinuity, extends this inequality to every $\nu$ with finite relative entropy. This is the classical Gaussian log-Sobolev/Ornstein–Uhlenbeck entropy contraction; see Gross (1975). Applying data processing to the second channel yields
$$
D(\nu K_\Pi\Vert\gamma)\le\lambda D(\nu\Vert\gamma).
$$
For $\lambda=0$, the output is exactly $\gamma$. Apply this bound to $\nu_x$ and integrate. The infinite-path sigma-algebra is generated by finite horizons, so $\mathcal D_\infty=\sup_\tau\mathcal D_\tau\le\lambda_\infty J$. Gaussian mean shifts in a top eigenspace prove sharpness, and Proposition 8.3 gives $\lambda_\infty<1$. $\square$

**Strong data-processing provenance.** The coefficient in item 3 is the classical Gaussian-reference KL strong data-processing coefficient, equal here to the squared maximal correlation of the jointly Gaussian reference input and output. See Polyanskiy–Wu, *Strong data-processing inequalities for channels and Bayesian networks*, and Anantharam–Gohari–Kamath–Nair, *On Maximal Correlation, Hypercontractivity, and the Data Processing Inequality studied by Erkip and Cover*. Equality with squared maximal correlation is specific to this Gaussian setting, not a general identity for arbitrary channels. The contraction principle is standard; the network-specific result is the explicit matrix $\Pi_\tau$, its closed infinite-time form, and the resulting thermal visibility ceiling.

**Mean and covariance are attenuated differently near equilibrium.** If $\alpha=\varepsilon v$ and $W=I+\varepsilon H$, $H=H^{\mathsf T}$, then
$$
J=\tfrac{\varepsilon^2}{2}\|v\|^2+\tfrac{\varepsilon^2}{4}\operatorname{tr}H^2+O(\varepsilon^3),
$$
$$
\mathcal D_\tau=\tfrac{\varepsilon^2}{2}v^{\mathsf T}\Pi_\tau v
+\tfrac{\varepsilon^2}{4}\operatorname{tr}(\Pi_\tau H\Pi_\tau H)+O(\varepsilon^3).
$$
In a visibility eigenbasis the covariance term is $\varepsilon^2\sum_{ij}\pi_i\pi_jH_{ij}^2/4$. Mean information is attenuated by one visibility eigenvalue; covariance information by products of two. This explains why a cold covariance preparation can be especially difficult to see through a noisy boundary.

### 8.5 The exact missing amount is posterior distinguishability

**Corollary 8.5 (posterior slack identity).** In the canonical channel (8.7),
$$
\boxed{
J-\mathcal D_\tau
=\mathbb E_{r\sim\rho_r}
D\big(\rho(du\mid r)\Vert\bar\rho(du\mid r)\big).
}
\tag{8.11}
$$
The chain-rule identity holds for any input law with finite $J$; for conditional preparations it is applied at each $x(0)$ and averaged. For Gaussian inputs, everything on the right is a finite-dimensional Gaussian calculation. Write $R=\Pi^{1/2}$ and $N_0=I-\Pi\succ0$. The reference posterior is $\mathcal N(Rr,N_0)$. The Gaussian actual posterior has covariance and mean
$$
P=(W^{-1}+\Pi(I-\Pi)^{-1})^{-1},\qquad
m(r)=P[W^{-1}\alpha+R N_0^{-1}r].
$$
Average their Gaussian KL over $r\sim\mathcal N(R\alpha,\Omega)$ to evaluate the exact slack. The formula remains valid at infinite horizon since $I-\Pi_\infty\succ0$.

*Proof.* The joint input/output KL is $J$ because both preparations pass through the same channel. Apply the KL chain rule in the opposite order. Gaussian conditioning gives the displayed posterior formulas. $\square$

### 8.6 General jointly Gaussian conditional preparations

For the actual Gaussian initial state of Corollary 3.2 the conditional residual has mean
$$
a(x(0))=d+(R_0-L)(x(0)-m_x),\qquad R_0=\Sigma_{yx}\Sigma_{xx}^{-1},
$$
and fixed covariance $V$. The reference conditional residual is $\mathcal N(0,S)$ independently of $x(0)$. Define
$$
A_0=S^{-1/2}\left[dd^{\mathsf T}+(R_0-L)\Sigma_{xx}(R_0-L)^{\mathsf T}\right]S^{-1/2}.
$$
**Corollary 8.6.** Equations (8.2) and (8.3) remain exact after replacing $\alpha^{\mathsf T}\Pi\alpha$ by $\operatorname{tr}(\Pi A_0)$ and $\alpha^{\mathsf T}\alpha$ by $\operatorname{tr}A_0$. The same sharp contraction bound holds. The path includes $x(0)$, so the proof is to condition on that common initial marginal, apply Theorem 8.2, and average. This covers all faithful jointly Gaussian initial preparations in the stated overdamped setting.

### 8.7 The original witness: full observation still reveals less than one percent

The original certificate's N2 used
$$
A=\begin{pmatrix}5&-1\\-1&6\end{pmatrix},\quad
B=\begin{pmatrix}-1&0\\-1&-2\end{pmatrix},\quad
C=\begin{pmatrix}5&-1\\-1&5\end{pmatrix},\quad T=3/2,
$$
$$a=(0.4,-0.6)^{\mathsf T},\qquad V=S/3.$$
The exact formulas, evaluated numerically, give:

| Record | Boundary KL (nats) | Fraction of $J$ |
|---|---:|---:|
| Original two observations at $t=0.1,0.8$, without recording $x(0)$ | 0.002684533970 | 0.1840% |
| Entire continuous path on $[0,0.8]$, including $x(0)$ | 0.011951983061 | 0.8194% |
| Entire continuous path on $[0,\infty)$, including $x(0)$ | 0.011954085736 | 0.8196% |
| Full conditional preparation cost $J$ | 1.458612288668 | 100% |

Both infinite-time visibility eigenvalues are positive, approximately $0.0054442390$ and $0.0689573093$: the pair is observable. Yet **no preparation with finite conditional KL in this network can expose more than 6.8958% of that KL through this boundary**, even with ideal continuous observation forever, under the common boundary marginal and dynamics of Theorem 8.4(3). This particular covariance-heavy preparation exposes only 0.8196%. The original loose bound was predominantly loose because of intrinsic noisy visibility, not merely sparse sampling. Recording $x(0)$ also matters when comparing the first two rows.

The new certificate checks the exact formula using three computations of continuous-path information (backward Riccati, forward Kalman innovations, and matrix hyperbolic solution), independently generated exact full-network sampled transitions, and direct multitime Gaussian covariance matrices. The sampled comparisons use the full $K$ dynamics, not a discretization of the reduced observation model.

### 8.8 Boundary driving and feedback cannot improve the ideal experiment

**Theorem 8.7 (boundary-control equivalence).** Keep $B,C,T$ and the initial comparison fixed. Replace the prescribed boundary force by a known causal policy $f_t[x_{[0,t]}]$ in
$$
dx=(-Ax-By+f_t[x])dt+\sqrt{2T}\,dW_B,
\qquad dy=(-B^{\mathsf T}x-Cy)dt+\sqrt{2T}\,dW_I.
$$
Assume the policy is nonanticipating and the inverse Volterra equation below has a unique nonexplosive solution which is a measurable function of its continuous input on every finite interval. A sufficient condition is a globally Lipschitz history functional with linear growth on each finite interval. The same policy is used under both initial laws, and it has access only to the recorded boundary history. Then the full controlled boundary record, including $x(0)$, is statistically equivalent to the uncontrolled canonical experiment (8.4). In particular, its preparation KL, visibility matrix, and sharp contraction coefficient are exactly independent of the policy, at finite or infinite horizon. This holds for arbitrary initial preparations, not only Gaussian ones.

*Proof.* Compute $g[x]$ as in the proof of Theorem 8.2 and set
$$
Y_t=x_t-x_0+\int_0^t[Ax_s+Bg[x](s)-f_s[x]]\,ds.
\tag{8.12}
$$
Because $dg=(-Cg-B^{\mathsf T}x)dt$, the residual $h=y-g$ satisfies exactly (8.4), with $h(0)=z_0$. Conversely, given $x_0,Y$, solve
$$
x_t=x_0+Y_t+\int_0^t[-Ax_s-Bg[x](s)+f_s[x]]\,ds.
$$
The well-posedness assumption makes this a causal measurable inverse. Both maps are independent of the hidden initial law. Thus the controlled record and $(x_0,Y)$ determine each other; their likelihood ratios and KL agree. The law of the latter experiment contains no policy. Consistent finite-horizon inverses give the same result for the infinite record. $\square$

An independent randomized controller is also covered if its seed is recorded: condition on the seed and apply the theorem. Discarding the seed or degrading the record can only reduce distinguishability. The result allows known time-dependent and nonlinear boundary feedback, but not a controller with additional hidden-state measurements, an unknown force, or a policy selected using knowledge of which preparation occurred. It concerns ideal continuous observation; it does not assert equality for fixed-rate sampled records or an imperfect detector.

**Physical scope and provenance.** Additive forcing, including boundary-only stiffness feedback, can change trajectories and energy expenditure without improving this ideal preparation experiment. To change its ceiling one must change the hidden observation channel, for example $B,C$, the bath model, or the observed coordinates. This is an initial-preparation version of the established feedback-neutrality principle, not a claim to have discovered that principle. Harris et al. (2013), *Minimum requirements for feedback enhanced force sensing*, give the closely related measurement-record equivalence for linear force sensing. The result here identifies the invariant experiment explicitly and therefore preserves the exact ceiling and spatial bounds below.

### 8.9 A spatial screening theorem for pinned chains

**Spatial provenance.** Klickstein–Sorrentino (2020) already derive exponential lattice-Gramian decay. Their preprint equations (20)–(21), with $p=-a$, $s=k$, give $\widetilde z=\alpha-\sqrt{\alpha^2-1}=e^{-2\kappa}$, where $\alpha=a^2/(2k^2)-1$. The exponent itself is therefore an antecedent, not a novelty claim here. The results below transfer it to thermal preparation KL with uniform finite-chain bounds.

Consider sites $0,1,\ldots,n$, observing only site $0$. Let the full stiffness be tridiagonal with diagonal $a=m+2k$ and adjacent entries $-k$, where $m,k>0$. This is a uniformly pinned chain with coupling $k$ and an additional end spring to ground at each end. Its hidden block and boundary coupling are
$$
C_n=\operatorname{tridiag}(-k,a,-k),\qquad B=-k e_1^{\mathsf T}.
$$
Here $m$ denotes pinning stiffness, not inertial mass; the dynamics remains overdamped with unit friction. Let $d\in\{1,\ldots,n\}$ be distance from the observed site, and prepare a local conditional mean displacement $q e_d$, $q\ne0$, keeping the thermal conditional covariance $S=TC_n^{-1}$. Define its full infinite-time visible fraction
$$
\theta_{n,d}=\frac{\mathcal D_\infty}{J}
=\frac{e_d^{\mathsf T}C_n^{1/2}\Pi_\infty C_n^{1/2}e_d}{a},
\qquad J=\frac{q^2a}{2T}.
\tag{8.13}
$$
This is a spatially localized mean shift in physical coordinates, not a choice of the most visible global eigenmode.

**Theorem 8.8 (uniform spatial screening and its exact exponential rate).** Put
$$
\kappa=\operatorname{arcosh}\left(1+\frac{m}{2k}\right),\quad
v=\sqrt{a^2-4k^2}=2k\sinh\kappa,\quad
Q=\left(1+\frac{k^2}{m^2}\right)\left(1+\frac{k^2}{4m^2}\right).
$$
For every finite $n\ge d\ge1$,
$$
\boxed{\frac{c_-}{d}e^{-2\kappa d}\le\theta_{n,d}\le c_+e^{-2\kappa d},}
\qquad
c_- =\frac{m(1-e^{-2\kappa})^2e^{-2m/v}}{aQ},\quad
c_+=\frac{k e^\kappa}{2a}.
\tag{8.14}
$$
Consequently, for every sequence $n(d)\ge d$,
$$
\boxed{\lim_{d\to\infty}-\frac1d\log\theta_{n(d),d}=2\kappa.}
\tag{8.15}
$$
All constants are independent of chain length, temperature, and displacement amplitude. The same fraction and bounds hold under every admissible boundary controller in Theorem 8.7. These are bounds with a sharp exponential rate; they do not specify an exact algebraic prefactor.

*Proof, step 1: compare visibility with a positive heat-kernel integral.* Write $C=C_n$ and
$$
p_{n,d}(t)=(e^{-Ct})_{1d}\ge0,\qquad G_{n,d}=\int_0^\infty p_{n,d}(t)^2dt.
$$
For $h(0)=0$, the observation-derivative noise covariance is $\mathcal N=2T(I+k^2 HH^*)$, where
$$
(Hw)(t)=\int_0^t e_1^{\mathsf T}e^{-C(t-s)}w(s)\,ds.
$$
Since $C\succeq mI$, Young's convolution inequality gives $\|H\|\le1/m$. Hence the deterministic initial-state information satisfies
$$
\frac{k^2G_{n,d}}{2T(1+k^2/m^2)}\le (\mathcal I_\infty)_{dd}
\le\frac{k^2G_{n,d}}{2T},\qquad
\|\mathcal I_\infty\|\le\frac{k^2}{4Tm}.
$$
These statements follow first on finite intervals and then by increasing the horizon. Put $\Xi=S^{1/2}\mathcal I_\infty S^{1/2}$. Because $\|\Xi\|\le k^2/(4m^2)$,
$$
\frac{\mathcal I_\infty}{1+k^2/(4m^2)}
\preceq S^{-1/2}\Pi_\infty S^{-1/2}
\preceq\mathcal I_\infty.
$$
Taking the $dd$ entry in (8.13) gives
$$
\frac{k^2}{2aQ}G_{n,d}\le\theta_{n,d}\le\frac{k^2}{2a}G_{n,d}.
\tag{8.16}
$$

*Step 2: an upper spatial bound.* The positive vector $w_j=e^{\kappa j}$ satisfies $Cw\ge0$, so positivity of the semigroup implies $e^{-Ct}w\le w$. Thus $p_{n,d}(t)\le e^{-\kappa(d-1)}$. The elementary tridiagonal Green function is
$$
\int_0^\infty p_{n,d}(t)dt=(C^{-1})_{1d}
=\frac{\sinh((n+1-d)\kappa)}{k\sinh((n+1)\kappa)}
\le\frac{e^{-\kappa d}}{k}.
\tag{8.17}
$$
The formula follows by solving the second-order difference equation with zero values at sites $0,n+1$; see also Maximenko–Sánchez Arzate (2016) for these classical inverse formulas. Multiply the integral by the pointwise bound to get $G_{n,d}\le e^\kappa e^{-2\kappa d}/k$.

*Step 3: a matching lower exponential rate.* For $s>0$, Cauchy–Schwarz gives
$$
G_{n,d}\ge2s\left(\int_0^\infty e^{-st}p_{n,d}(t)dt\right)^2
=2s\big[((C+sI)^{-1})_{1d}\big]^2.
$$
Set $\kappa_s=\operatorname{arcosh}((a+s)/(2k))$. Formula (8.17) applied with $\kappa_s$ implies, uniformly for $n\ge d$,
$$
((C+sI)^{-1})_{1d}\ge\frac{1-e^{-2\kappa_s}}{k}e^{-\kappa_s d}.
$$
Since $\kappa_s\le\kappa+s/v$, choose $s=m/d$ to obtain
$$
G_{n,d}\ge\frac{2m}{k^2d}(1-e^{-2\kappa})^2e^{-2m/v}e^{-2\kappa d}.
$$
Combine with (8.16). Taking logarithms and dividing by $d$ proves (8.15). $\square$

**Corollary 8.9 (non-Gaussian preparation of the local displacement mode).** Let
$$
w_d=\frac{C_n^{1/2}e_d}{\sqrt a},\qquad
u=w_d\zeta+u_\perp,
$$
where $\zeta$ has any law $\nu$ with $D(\nu\Vert\gamma_1)<\infty$, $u_\perp$ is an independent standard Gaussian on $w_d^\perp$, and $\gamma_1=\mathcal N(0,1)$. The residual is $z_0=S^{1/2}u$ and is independent of the initial boundary state. Then $J=D(\nu\Vert\gamma_1)$ and
$$
\boxed{\mathcal D_\infty\le\theta_{n,d}J\le c_+e^{-2\kappa d}J.}
\tag{8.18}
$$
The first coefficient is sharp over this class. Indeed, after integrating out $u_\perp$, (8.7) becomes $r=b\zeta+\eta$, where $b=\Pi_\infty^{1/2}w_d$ and $\operatorname{Cov}\eta=I-bb^{\mathsf T}$. Projection along $b$ gives the scalar Gaussian channel with visibility $\|b\|^2=\theta_{n,d}$; the remaining components are independent reference noise. Apply Theorem 8.4(3) in one dimension. Gaussian mean shifts attain equality. Changes in $\zeta$ move the physical residual only along $S^{1/2}w_d=\sqrt{T/a}\,e_d$; the complementary thermal distribution is held fixed. This is a specified local displacement-mode family, not a bound for arbitrary changes to every deep-interior correlation. $\square$

**Corollary 8.10 (arbitrary preparation within the deep displacement subspace).** Let $E_d=[e_d,\ldots,e_n]$, $C_d=E_d^{\mathsf T}C_nE_d$, and
$$
U_d=C_n^{1/2}E_d C_d^{-1/2},\qquad U_d^{\mathsf T}U_d=I.
$$
Prepare $u=U_d\zeta+u_\perp$, where $\zeta$ has any finite-KL law relative to the standard Gaussian on $\mathbb R^{n-d+1}$, and $u_\perp$ remains an independent standard Gaussian on the orthogonal complement. Such changes act only on physical coordinates $d,\ldots,n$, since $S^{1/2}U_d=\sqrt T E_d C_d^{-1/2}$. The sharp coefficient over this class is
$$
\Lambda_{n,d}=\lambda_{\max}(U_d^{\mathsf T}\Pi_\infty U_d),
\qquad\mathcal D_\infty\le\Lambda_{n,d}J,
$$
and
$$
\boxed{\frac{c_-}{d}e^{-2\kappa d}\le\Lambda_{n,d}
\le\min\left\{\lambda_\infty,\frac{k e^\kappa}{2m(1-e^{-2\kappa})}e^{-2\kappa d}\right\}.}
\tag{8.19}
$$
Thus the sharp coefficient for this entire deep-subspace preparation class has the same exact exponential rate $2\kappa$, uniformly in the number of hidden coordinates beyond depth $d$.

*Proof.* Integrating out the complementary Gaussian and taking a singular-value decomposition gives a Gaussian attenuation channel with visibility $U_d^{\mathsf T}\Pi_\infty U_d$. Apply Theorem 8.4(3); mean shifts in a leading singular direction attain the coefficient. Because $w_d$ from Corollary 8.9 belongs to the range of $U_d$, $\Lambda_{n,d}\ge\theta_{n,d}$. For the upper bound, $C_d\succeq mI$ and positivity give
$$
\Lambda_{n,d}\le\operatorname{tr}(U_d^{\mathsf T}\Pi_\infty U_d)
\le\frac1m\operatorname{tr}(E_d^{\mathsf T}C_n^{1/2}\Pi_\infty C_n^{1/2}E_d)
=\frac a m\sum_{j=d}^n\theta_{n,j}.
$$
Sum the geometric upper bound (8.14) and use compression to get $\Lambda_{n,d}\le\lambda_\infty$. $\square$

The independent thermal-complement condition specifies the allowed preparation channel. Neither corollary asserts a depth bound for every joint law with an unchanged shallow marginal: changes to correlations across the depth boundary need not belong to this class.

**Operational consequence (independent repetitions).** Let $C_* = k e^\kappa/[2m(1-e^{-2\kappa})]$. In $N$ independent repetitions comparing one preparation from Corollary 8.10 against its thermal refinement, KL additivity and Pinsker's inequality give
$$
\operatorname{TV}(\mathbb P^{\otimes N},\bar{\mathbb P}^{\otimes N})
\le\sqrt{\frac{N C_* e^{-2\kappa d}J}{2}}.
$$
Consequently equal-prior binary discrimination with error at most $1/2-\varepsilon$, $0<\varepsilon<1/2$, requires
$$
N\ge\frac{8\varepsilon^2}{C_*J}e^{2\kappa d}.
$$
At fixed preparation cost per trial, maintaining a fixed discrimination advantage thus requires at least exponentially many independent preparations with increasing depth, even when each trial records the entire boundary history. This is a necessary sample-size bound, not an achievability assertion.

**Physical interpretation and limits.** The equilibrium boundary Green function has exponential length $\xi_{\rm eq}=1/\kappa$, while the local-preparation KL has exponential length
$$
\boxed{\xi_{\rm KL}=\frac1{2\kappa}=\frac12\xi_{\rm eq}
\sim\frac12\sqrt{\frac{k}{m}}\quad(m/k\to0).}
$$
These lengths are measured in lattice spacings. Every finite chain is observable from its end: its sine eigenvectors have nonzero first component and its eigenvalues are distinct. Nevertheless, even the entire infinite-time boundary record has exponentially small sensitivity to a fixed-cost displacement prepared deep inside. Longer observation or admissible boundary feedback cannot remove this suppression. The global coefficient $\lambda_{\max}(\Pi_\infty)$ need not vanish with chain length, since preparations near the boundary remain accessible. The theorem assumes fixed positive pinning; it does not establish the unpinned limit, the exact polynomial prefactor, or higher-dimensional spatial laws. The Green-function decay and feedback neutrality are classical ingredients; the claim proved here is their quantitative consequence for the exact thermal preparation experiment. A priority claim requires a separate literature audit.

### 8.10 What a boundary can harvest

*Added October 13, 2026.* Sections 8.1–8.9 ask how much a boundary can learn about a hidden preparation. Here we ask how much work it can extract from the same preparation by acting only on the boundary. The answer uses the same visibility matrix.

**Setting.** Use the unit-friction overdamped model of Section 8.2. A boundary force $f(t)$ is **admissible** if it is a deterministic, locally bounded function of time (open loop), with $f(0^-)=0$ and $f(t)=0$ for all sufficiently large $t$. With $H_f=H-f^{\mathsf T}x$, the mean extracted work is the Sekimoto integral
$$
W[f]=\int_{[0,\infty)}\langle x(t)\rangle^{\mathsf T}df(t),
$$
which includes any jumps of $f$. Write $m=(m_x,m_y)$ for the initial mean, $\bar z=m_y-Lm_x$ for the mean conditional residual, $\bar\alpha=S^{-1/2}\bar z$, and $X=C+F$ with $F=(C^2+B^{\mathsf T}B)^{1/2}$ as in Proposition 8.3.

**Theorem 8.11 (port harvest equals port visibility).** For every initial law with finite second moments and every admissible protocol,
$$
\boxed{
W[f]\le\tfrac12m_x^{\mathsf T}K_Bm_x+\tfrac T2\,\bar\alpha^{\mathsf T}\Pi_\infty\bar\alpha,
}
\tag{8.20}
$$
and the supremum over admissible protocols equals the right side. Equivalently, the minimal mean dissipation is
$$
\mathcal V=\bar w^{\mathsf T}X^{-1}\bar w=\frac{\bar w^{\mathsf T}P_f\,\bar w}{2T},\qquad \bar w=C\bar z,
$$
where $\bar w$ is the mean restoring force on the hidden coordinates and $P_f=2TX^{-1}$ is the stationary tracking covariance of Proposition 10.4. Moreover,
$$
\boxed{
W[f]\le T\left[D(\rho_B\Vert\sigma_B)+\mathcal D_\infty\right],
}
\tag{8.21}
$$
with equality of the supremum for every thermal-covariance mean shift $\rho=\mathcal N(m,TK^{-1})$. There the boundary can harvest exactly $T$ times what its entire infinite record can learn.

*Proof, step 1: only the mean works.* Since $f$ is deterministic, $\langle x^{\mathsf T}df\rangle=m_x^{\mathsf T}df$, and the mean obeys $\dot m=-Km+(f,0)$ exactly, whatever the covariance or non-Gaussianity of the preparation. With $\mathcal E=\tfrac12m^{\mathsf T}Km-f^{\mathsf T}m_x$, one has $d\mathcal E=-|\dot m|^2dt-m_x^{\mathsf T}df$. Because $f$ vanishes eventually, $m\to0$. Hence
$$
W[f]=\mathcal E_0-\int_0^\infty|\dot m|^2dt,\qquad
\mathcal E_0=\tfrac12m_x^{\mathsf T}K_Bm_x+\tfrac12\bar z^{\mathsf T}C\bar z,
$$
using Theorem 2.1(1).

*Step 2: a lower bound on dissipation.* Put $v=\dot m_x$ and $w=B^{\mathsf T}m_x+Cm_y=C(m_y-Lm_x)$, so $\dot m_y=-w$ and $|\dot m|^2=|v|^2+|w|^2$. Since $(X-C)^2=F^2=C^2+B^{\mathsf T}B$, we have $X^2-XC-CX=B^{\mathsf T}B$. Multiplying by $G=X^{-1}$ on both sides gives
$$
GB^{\mathsf T}BG+GC+CG=I.
$$
For $\mathcal V(m)=w^{\mathsf T}Gw$, $\dot w=B^{\mathsf T}v-Cw$ gives
$$
|v|^2+|w|^2+\frac{d}{dt}\mathcal V=|v+BGw|^2\ge0.
$$
Integrating, every admissible protocol dissipates at least $\mathcal V(m(0))-\lim\mathcal V=\mathcal V(m(0))$.

*Step 3: attainability.* The protocol $f=v+Am_x+Bm_y$, with $v=-BGw$ along the mean path, is deterministic and admissible on any finite interval. It gives $\dot w=-(B^{\mathsf T}BG+C)w$. Since $B^{\mathsf T}BG+C=(X^2-XC-CX)X^{-1}+C=XFX^{-1}$, which is similar to $F\succ0$, $w(t)=Xe^{-Ft}X^{-1}w(0)\to0$, and the dissipation on this phase is $\mathcal V(m(0))-\mathcal V(m(t))$. It ends near the zero-cost set $w=0$ with $m_x\ne0$ in general. Returning $m_x$ linearly to zero over a time $\tau_r$ and then switching $f$ off costs $O(1/\tau_r)$ plus the exponentially small remainder of $\mathcal V$. The supremum is therefore approached but not attained.

*Step 4: the visibility form.* By (8.9),
$$
\tfrac12\bar z^{\mathsf T}C\bar z-\bar z^{\mathsf T}CX^{-1}C\bar z
=\tfrac12\bar z^{\mathsf T}C^{1/2}\Pi_\infty C^{1/2}\bar z
=\tfrac T2\bar\alpha^{\mathsf T}\Pi_\infty\bar\alpha,
$$
since $S^{-1/2}=(C/T)^{1/2}$. The identity $P_f=2TX^{-1}$ is Proposition 10.4.

*Step 5: comparison with relative entropy.* Let $\gamma=\mathcal N(0,\Sigma)$. For a law $\nu$ with mean $\mu$ and covariance $\Lambda$, $D(\nu\Vert\gamma)=D(\nu\Vert\mathcal N(\mu,\Lambda))+D(\mathcal N(\mu,\Lambda)\Vert\gamma)\ge\tfrac12\mu^{\mathsf T}\Sigma^{-1}\mu$, because $\log\gamma$ is quadratic. Applied to $\rho_B$, this gives $TD(\rho_B\Vert\sigma_B)\ge\tfrac12m_x^{\mathsf T}K_Bm_x$. By Theorem 8.4(3), $\mathcal D_\infty=\int D(\nu_xK_{\Pi_\infty}\Vert\gamma)\,\mu(dx)$, and the output mean of $K_{\Pi}$ is $\Pi^{1/2}$ times the input mean. The moment bound and Jensen's inequality then give $\mathcal D_\infty\ge\tfrac12\bar\alpha^{\mathsf T}\Pi_\infty\bar\alpha$. For $\rho=\mathcal N(m,TK^{-1})$ both bounds are equalities. $\square$

The retained stiffness $A$ is absent from the hidden term, as in (8.2). The theorem is temperature-free in thermal coordinates, like the visibility matrix (Remark 8.3a).

**Corollary 8.12 (the work a port must waste is the information it cannot see).** Let $\rho=\mathcal N(m,TK^{-1})$. Forcing every coordinate quasi-statically extracts the whole excess $TD(\rho\Vert\sigma)=\mathcal E_0$. Under boundary-only admissible forcing, the minimal mean dissipation is
$$
\boxed{
TD(\rho\Vert\sigma)-\sup_fW[f]=T\left(J-\mathcal D_\infty\right)
=T\,\mathbb E_{r}\,D\big(\rho(du\mid r)\Vert\bar\rho(du\mid r)\big),
}
\tag{8.22}
$$
which is $T$ times the posterior slack of Corollary 8.5. The harvested fraction of the hidden excess $TJ$ is $\bar\alpha^{\mathsf T}\Pi_\infty\bar\alpha/|\bar\alpha|^2\le\lambda_\infty$, attained along a top eigenvector. Learning and harvesting therefore share one coefficient.

*Proof.* $J=|\bar\alpha|^2/2$ and $\mathcal D_\infty=\bar\alpha^{\mathsf T}\Pi_\infty\bar\alpha/2$ for this preparation; with $W=I$ in (8.2), subtract (8.20) from $\mathcal E_0$. The second equality is (8.11). Full actuation makes every velocity a control, so slow transport to the origin has arbitrarily small dissipation. $\square$

In the original witness of Section 8.7, the preparation is covariance-heavy. Additive forcing harvests $0.017108500$, against $T\mathcal D_\infty=0.017931129$ and $TJ=2.187918433$ (energy units, $T=3/2$). That is $0.782\%$ of the hidden excess, beside the $0.820\%$ visible fraction. The covariance part of $\mathcal D_\infty$ is legible but cannot be harvested by any additive force, so (8.21) is strict here, with ratio $0.954$.

**Corollary 8.13 (ignorance penalty).** Let the preparation be drawn from a prior over thermal-covariance mean shifts $\rho_\theta$ with a common boundary law. Write $\alpha_\theta$ for the normalized residual means, with prior mean $\bar\alpha$ and covariance $\Sigma_\alpha$. One admissible protocol chosen without knowledge of $\theta$ has prior-averaged harvest at most the right side of (8.20) at $\bar\alpha$, and it attains it. Protocols tailored to each $\theta$ harvest the prior average of (8.20). The difference is
$$
\Delta W=\tfrac T2\operatorname{tr}(\Pi_\infty\Sigma_\alpha)
\ \ge\ \tfrac T2\log\det\big(I+\Pi_\infty^{1/2}\Sigma_\alpha\Pi_\infty^{1/2}\big)
\ \ge\ T\,I(\theta;\text{entire boundary record}).
\tag{8.23}
$$

*Proof.* Mean paths are affine in the preparation. Under a fixed protocol, $m_\theta(t)=m_{\bar\theta}(t)+e^{-Kt}\delta_\theta$, where $\delta_\theta$ has prior mean zero. The work difference $\int(e^{-Kt}\delta_\theta)_x^{\mathsf T}df$ is linear in $\delta_\theta$ and averages to zero, so the averaged harvest is the harvest of the prior-mean preparation, and Theorem 8.11 applies. The equality is the difference of quadratic forms. For the information bound, the canonical record (8.7) given $\theta$ is $\mathcal N(\Pi_\infty^{1/2}\alpha_\theta,I)$ and $x(0)$ does not depend on $\theta$. Gaussian maximum entropy gives the middle term, and $\log\det(I+M)\le\operatorname{tr}M$ gives the first inequality. $\square$

**Remark 8.14 (exploration and exploitation at a port).** Theorem 8.7 says that additive boundary actions, even adaptive ones, cannot change what the ideal record reveals: their epistemic value is identically zero. Theorem 8.11 says that the harvestable part of a hidden mean is fixed by the same $\Pi_\infty$. In this class, actions can therefore have epistemic value only outside the hypotheses of Theorem 8.7: changing $B$ or $C$ (bond weights, as in Paper 56), the bath, the observed coordinates, or the sampling. This is narrower than expected-free-energy accounts of exploration in active inference, which present an epistemic term plus a pragmatic term as a parameter-free resolution. Two cautions apply there. First, $D\big(P(o,s\mid a)\Vert Q(o)P(s\mid o,a)\big)=D\big(P(o\mid a)\Vert Q(o)\big)$ is risk alone. The information-gain form satisfies $-I(S;O)+\mathbb E[-\log Q(o)]=D\big(P(o\mid a)\Vert Q(o)\big)+H(O\mid S)$, which adds ambiguity (Millidge–Tschantz–Buckley 2021). Second, encoding rewards as $Q(o)\propto e^{r(o)/\lambda}$ reintroduces a temperature. The results here are exact statements for passive Gaussian networks, not a theory of agents.

**Scope.** The theorem is classical, uses unit friction, and covers open-loop additive boundary forcing.

- **Feedback** ($f$ depending on the record) is not covered. It leaves the record's information unchanged (Theorem 8.7), but it can change work, as Sagawa–Ueda demons do. Whether causal adaptation recovers part of the penalty (8.23) is the open feedback-work question of Proposition 10.4.
- **Parametric control** (changing $K$) is needed to harvest covariance preparations and is not treated.
- **General friction and inertia** (Section 9) are not claimed for this theorem.

## 9. General thermal networks: friction, inertia, and the private-bath principle

Section 8 used overdamped dynamics with unit friction. This section removes that restriction. The record is always the entire boundary position path $x|_{[0,\tau]}$, including $x(0)$. The reference is the thermal conditional law of the hidden phase-space variables given the boundary ones. The two preparations differ only in that conditional law and share future bath noise.

The outcome has three parts. Overdamped networks with *any* friction matrix keep the closed form of Section 8 with effective matrices. Inertial networks need one Riccati equation, and their ceiling is strict exactly when the hidden sector has noise of its own. Undamped boundary directions or noiseless hidden modes make part of the hidden state perfectly legible, either immediately or asymptotically.

### 9.1 One reduction for every linear thermal network

Consider
$$
M\ddot q+\Gamma\dot q+Kq=f+\xi,\qquad \mathbb E\,\xi(t)\xi(u)^{\mathsf T}=2T\Gamma\,\delta(t-u),
$$
with $K\succ0$, $\Gamma=\Gamma^{\mathsf T}\succeq0$, and either $M\succ0$ or $M=0$ with $\Gamma\succ0$. Assume a unique stationary Gibbs law, so every normal mode of the full network is damped. Positivity of the boundary friction block $\Gamma_{BB}$ is not assumed in this subsection.

**Lemma 9.1 (cross mass can be removed).** The hidden shift $y'=y+M_{II}^{-1}M_{IB}x$ makes the mass matrix block diagonal. Because $x$ is recorded, records and hidden preparations correspond one to one; every relative entropy, visibility matrix, and contraction coefficient is unchanged. A further block-diagonal rescaling $q\mapsto M^{1/2}q$ gives unit mass.

*Proof.* With $P=M_{II}^{-1}M_{IB}$ and $U=\begin{pmatrix}I&0\\-P&I\end{pmatrix}$, the coordinates $q=Uq'$ give $(U^{\mathsf T}MU)_{BI}=M_{BI}-P^{\mathsf T}M_{II}=0$. Stiffness, friction, and noise transform by the same congruence, so the Gibbs law and the fluctuation–dissipation relation are preserved. The map is the identity on $x$ and, for each recorded $x$, invertible on $y$. $\square$

Henceforth the inertial mass is $M=I$. Write $v=\dot x$ and $w=\dot y$. The thermal conditional law of the hidden phase-space variables is $y\mid x\sim\mathcal N(Lx,TC^{-1})$ and $w\sim\mathcal N(0,TI)$, independent of $v$. The conditional residual and its reference are therefore
$$
z_0=\big(y(0)-Lx(0),\,w(0)\big),\qquad S=T\operatorname{diag}(C^{-1},I).
\tag{9.1}
$$
Observing the differentiable path $x$ reveals $v$ exactly. This is *not* a degenerate observation of the hidden sector. Hidden information enters through the increments of $v$, and those carry the boundary bath noise.

**Theorem 9.2 (exact visibility of inertial networks with a damped boundary).** Let $M=I$ and $\Gamma_{BB}\succ0$. Put
$$
F=\begin{pmatrix}0&I\\-C&-\Gamma_{II}\end{pmatrix},\quad
H=-\begin{bmatrix}B&\Gamma_{BI}\end{bmatrix},\quad
R=2T\Gamma_{BB},\quad
N=\begin{pmatrix}0\\2T\Gamma_{IB}\end{pmatrix},\quad
Q=\begin{pmatrix}0&0\\0&2T\Gamma_{II}\end{pmatrix},
$$
and $F'=F-NR^{-1}H$, $Q'=Q-NR^{-1}N^{\mathsf T}$. Explicitly,
$$
F'=\begin{pmatrix}0&I\\-C^\sharp&-\Gamma/\Gamma_{BB}\end{pmatrix},\qquad
Q'=\begin{pmatrix}0&0\\0&2T\,\Gamma/\Gamma_{BB}\end{pmatrix},
\qquad
C^\sharp=C-\Gamma_{IB}\Gamma_{BB}^{-1}B,
\tag{9.2}
$$
where $\Gamma/\Gamma_{BB}=\Gamma_{II}-\Gamma_{IB}\Gamma_{BB}^{-1}\Gamma_{BI}$ is the Schur complement of the friction. Let
$$
\frac{d\mathcal I_\tau}{d\tau}=H^{\mathsf T}R^{-1}H+F'^{\mathsf T}\mathcal I_\tau+\mathcal I_\tau F'-\mathcal I_\tau Q'\mathcal I_\tau,\qquad \mathcal I_0=0.
\tag{9.3}
$$
With $\Xi_\tau=S^{1/2}\mathcal I_\tau S^{1/2}$, $\Pi_\tau=\Xi_\tau(I+\Xi_\tau)^{-1}$, and $\alpha,W$ formed from the preparation $\mathcal N(a,V)$ relative to $S$, formula (8.2) holds exactly for the entire boundary path. Theorem 8.4 holds with this $\Pi_\tau$: its kernel, its invisibility conditions, and its sharp contraction coefficient for arbitrary preparations with finite conditional relative entropy. The whitened problem contains no temperature.

*Proof.* Let $g$ solve the hidden equations driven by the recorded $(x,v)$, with $g(0)=(Lx(0),0)$. Then $h=(y,w)-g$ satisfies $dh=Fh\,dt+(0,\text{hidden noise})$ with $h(0)=z_0$. The boundary velocity equation becomes the observation $dY=Hh\,dt+\text{boundary noise}$, and the two noises have cross-intensity $N$. Write the hidden noise as $NR^{-1}$ times the observation noise plus an independent remainder of intensity $Q'$. The pair becomes a standard observation model with drift $F'$ and a known input. The map from $x$ to $(x(0),Y)$ is causal, invertible, and independent of the preparation. Steps 2–4 of the proof of Theorem 8.2 then apply verbatim: completing the square in the path likelihood gives a finite sufficient statistic whose information solves (9.3). For temperature independence, $S\propto T$, $R\propto T$, and $Q'\propto T$, so $S^{1/2}H^{\mathsf T}R^{-1}HS^{1/2}$, $S^{-1/2}F'S^{1/2}$, and $S^{-1/2}Q'S^{-1/2}$ are free of $T$. $\square$

**Proposition 9.3 (overdamped networks with any friction keep the closed form).** Let $\Gamma\dot q=-Kq+f+\xi$ with arbitrary $\Gamma\succ0$, cross friction included, and mobility $\mathcal M=\Gamma^{-1}$. The conditional hidden dynamics and the private hidden noise are
$$
F'=-\Gamma_{II}^{-1}C,\qquad Q'=2T\,\Gamma_{II}^{-1}.
\tag{9.4}
$$
Thus the hidden sector, conditioned on the boundary record, moves with its own friction block, whatever the cross friction. Put
$$
\widetilde C=\Gamma_{II}^{-1/2}C\,\Gamma_{II}^{-1/2},\qquad
\widetilde B=\mathcal M_{BB}^{-1/2}\big(\mathcal M_{BB}B+\mathcal M_{BI}C\big)\Gamma_{II}^{-1/2}.
\tag{9.5}
$$
Every statement of Section 8 then holds after $(C,B)\mapsto(\widetilde C,\widetilde B)$ in the hidden coordinates $\Gamma_{II}^{1/2}y$. In particular, $\Pi_\infty$ is orthogonally equivalent to $I-2\widetilde C^{1/2}(\widetilde C+\widetilde F)^{-1}\widetilde C^{1/2}$ with $\widetilde F=(\widetilde C^2+\widetilde B^{\mathsf T}\widetilde B)^{1/2}$. Because $Q'\succ0$, an overdamped network always has a strictly subunit ceiling. For block-diagonal friction, $\widetilde B=\Gamma_{BB}^{-1/2}B\Gamma_{II}^{-1/2}$. In the scalar case the coupling angle of Remark 8.3b becomes
$$
\tan\theta=\frac{|b|}{c}\sqrt{\frac{\gamma_I}{\gamma_B}}.
$$
A stickier hidden coordinate, relative to the boundary, is more visible.

*Proof.* The dynamics is $\dot q=-\mathcal MKq+\mathcal Mf+\text{noise}$ with noise intensity $2T\mathcal M$. Removing known feedback as in Theorem 8.2 gives hidden drift $-(\mathcal M_{IB}B+\mathcal M_{II}C)$ and observation matrix $H=-(\mathcal M_{BB}B+\mathcal M_{BI}C)$. The intensities are $R=2T\mathcal M_{BB}$, $N=2T\mathcal M_{IB}$, and $Q=2T\mathcal M_{II}$. Then $F'=-(\mathcal M_{II}-\mathcal M_{IB}\mathcal M_{BB}^{-1}\mathcal M_{BI})C$ and $Q'=2T(\mathcal M_{II}-\mathcal M_{IB}\mathcal M_{BB}^{-1}\mathcal M_{BI})$. The Schur complement of an inverse is the inverse of the complementary block, so both reduce to (9.4). The change $y'=\Gamma_{II}^{1/2}y$ maps $(F',Q',S,H^{\mathsf T}R^{-1}H)$ to $(-\widetilde C,\,2TI,\,T\widetilde C^{-1},\,\widetilde B^{\mathsf T}\widetilde B/2T)$, which is exactly the unit-friction problem (8.1). $\square$

### 9.2 The private-bath principle

**Theorem 9.4 (when the ceiling is strict).** Let $M=I$, $\Gamma\succeq0$, and assume a unique Gibbs law. Let $P_0$ be the orthogonal projector onto $\ker\Gamma_{BB}$. Positivity of $\Gamma$ gives $\ker\Gamma_{BB}\subseteq\ker\Gamma_{IB}$.

1. **Undamped coupled boundary direction.** If $P_0B\ne0$, then $\lambda_\tau=\lambda_{\max}(\Pi_\tau)=1$ for every $\tau>0$. Part of the hidden state is read without noise (Theorem 9.5).
2. **Otherwise the private noise decides.** Suppose $P_0B=0$, and restrict attention to the observable subspace of $(F',H)$; directions outside it carry no information, as in Theorem 8.4(1). If every mode of $F'$ there with $\operatorname{Re}\lambda\ge0$ is reached by the private noise, meaning its left eigenvector $\ell$ satisfies $\ell^*Q'\ell>0$, then $\lambda_\infty<1$. If some observable mode with $\operatorname{Re}\lambda\ge0$ is not reached, then $\lambda_\tau<1$ at every finite horizon but $\lambda_\tau\to1$.
3. **Block-diagonal friction.** If $\Gamma_{BI}=0$, then $F'=F$. Its non-strictly-stable modes are exactly the undamped hidden modes: eigenvectors $\varphi$ of $C$ with $\Gamma_{II}\varphi=0$. These receive no noise. Hence $\lambda_\infty<1$ if and only if $P_0B=0$ and $B\varphi=0$ for every such $\varphi$.

*Proof.* (1) is Theorem 9.5. For (2), the observation noise is nondegenerate on the range of $\Gamma_{BB}$. The noiseless components of $v$ carry no hidden information, because $P_0B=0$ and $P_0\Gamma_{BI}=0$. Read (9.3) as the filter Riccati equation of the dual system. Reaching every non-strictly-stable observable mode with noise is then the detectability condition of the dual. Under it, the solution started at zero converges to a finite limit (Kwakernaak–Sivan 1972; Anderson–Moore 1979), so $\Pi_\infty\prec I$. Conversely, a mode not reached by noise evolves deterministically given the record. For an undamped mode, Proposition 9.7 shows that its Fisher information grows linearly in $\tau$. For an unstable mode it grows exponentially. Either way the posterior variance of that functional tends to zero and $\lambda_\tau\to1$. For (3), an imaginary eigenvalue $i\omega$ of $F$ with eigenvector $(p,i\omega p)$ satisfies $(C-\omega^2)p=-i\omega\Gamma_{II}p$. Taking $p^*(\cdot)$ forces $p^*\Gamma_{II}p=0$, so $\Gamma_{II}p=0$ and $Cp=\omega^2p$. The span of $(\varphi,0)$ and $(0,\varphi)$ is $F$-invariant, has an $F$-invariant orthogonal complement, and is noise-free, because $\Gamma_{II}^{1/2}\varphi=0$. $\square$

**Corollary 9.6 (a shared bath makes the hidden sector legible).** Suppose the friction has no private hidden part, $\Gamma/\Gamma_{BB}=0$; equivalently $\operatorname{rank}\Gamma=\operatorname{rank}\Gamma_{BB}$, as for a single bath $\Gamma=gg^{\mathsf T}$ coupled to both sides. Then $Q'=0$ and $F'=\begin{pmatrix}0&I\\-C^\sharp&0\end{pmatrix}$ has no strictly stable modes, so $\lambda_\tau\to1$ whenever the boundary observes any hidden mode at all.

In the certificate's scalar network, a common bath gives $\lambda_\tau=0.387$, $0.810$, $0.976$, and $0.9975$ at $\tau=1,10,100,1000$. With separate baths of the same friction coefficients, the ceiling is $0.3436$. A hidden mode that is undamped but dark ($B\varphi=0$) leaves the ceiling unchanged at $0.2332$. Making that same mode visible moves $\lambda_\tau$ from $0.643$ at $\tau=100$ to $0.876$ at $\tau=400$.

**Interpretation.** The thermal visibility ceiling is not a statement about temperature or coupling strength. It exists because the hidden sector has noise the boundary does not share. A shared bath acts as side information: the boundary observes the common noise through its own motion and subtracts it from the hidden dynamics. *A hidden sector stays private only if it has a private bath.* Overdamped networks always have one (Proposition 9.3). Inertial networks can lose it, through an undamped hidden mode, a shared bath, or an undamped boundary direction.

### 9.3 Undamped boundary directions: exact visibility and a terminating recursion

**Theorem 9.5 (exact visibility through an undamped boundary direction).** Take block-diagonal friction; cross friction adds only the correlated-noise substitution of Theorem 9.2. Suppose $P_0B\ne0$, and write $B_d$ for the damped rows. The record determines
$$
Ez_0,\qquad E=\begin{pmatrix}P_0B&0\\0&P_0B\end{pmatrix},
$$
exactly: hidden positions *and* hidden velocities along the rows of $P_0B$. The remaining data are equivalent to the continuous observation
$$
dY_d=-B_dh_y\,dt+\text{noise},\qquad
dY_u=-P_0B\big(Ch_y+\Gamma_{II}h_w\big)dt+P_0B\sqrt{2T\Gamma_{II}}\,dW_I.
\tag{9.6}
$$
The noise of $dY_u$ is correlated with the private hidden noise. Treat (9.6) with the correlated-noise substitution of Theorem 9.2, and let $\mathcal I_c$ be its initial-state information. Then $\mathcal D_\tau$ is the finite-dimensional Gaussian relative entropy between the laws of $(Ez_0,\ \mathcal I_c^{1/2}z_0+\epsilon)$, $\epsilon\sim\mathcal N(0,I)$, under the two preparations. Equivalently, (8.2) holds with $\Pi_\tau$ equal to $1$ on the whitened subspace $\operatorname{range}(S^{1/2}E^{\mathsf T})$. If $P_0B\Gamma_{II}B^{\mathsf T}P_0$ is singular on the range of $P_0B$, differentiate the still-noiseless rows of (9.6) again. Each step either adds exact functionals or terminates, so the recursion stops after at most $2h$ steps. This is the Bryson–Johansen (1965) reduction for perfect measurements.

*Proof.* Since $P_0\Gamma_{BB}=0$, the component $P_0v$ is differentiable with $P_0\dot v=-P_0(Ax+By)+P_0f$, so $P_0By(t)$ is known on $[0,\tau]$. Because $\dot y=w$, $P_0Bw(t)$ is known as well, and its increments give $dY_u$. The initial values $(P_0By(0),P_0Bw(0))$, together with the increments of $P_0Bw$ and of the damped rows, reconstruct the record, and conversely. Conditional on $z_0$, the continuous part is Gaussian with covariance independent of $z_0$. The likelihood is therefore $\delta(Ez_0-e)\exp(z_0^{\mathsf T}s-\tfrac12z_0^{\mathsf T}\mathcal I_cz_0)$, and $(Ez_0,s)$ is sufficient. $\square$

The certificate compares this formula with a 45-digit brute-force calculation on the full network. The brute force samples the boundary path, whose undamped component is twice differentiable. A double-precision attempt failed exactly as one would expect: it returned a sampled relative entropy above $J$, which data processing forbids.

### 9.4 Rates, closed forms, and the inertial gauge

**Proposition 9.7 (approach to full visibility).** Take block-diagonal friction with $\Gamma_{BB}\succ0$, and suppose the undamped hidden modes $\varphi_j$ ($C\varphi_j=\omega_j^2\varphi_j$, $\Gamma_{II}\varphi_j=0$) have distinct frequencies. Then
$$
\lim_{\tau\to\infty}\tau\,(1-\lambda_\tau)=\min_j\frac{4\omega_j^2}{(B\varphi_j)^{\mathsf T}\Phi(i\omega_j)^{-1}(B\varphi_j)},
\qquad
\Phi(s)=\Gamma_{BB}+B(s^2+s\Gamma_{II}+C)^{-1}\Gamma_{II}(s^2-s\Gamma_{II}+C)^{-1}B^{\mathsf T}.
\tag{9.7}
$$
$\Phi(i\omega_j)$ is finite because $\Gamma_{II}\varphi_j=0$ cancels the mode's own pole. $2T\Phi(i\omega)$ is the spectral density of the boundary force noise that remains after the undamped modes are removed. The limit does not depend on temperature.

*Proof (asymptotic).* Decompose as in Theorem 9.4(3). The complement of the undamped modes is Hurwitz, so its contribution to the observation is stationary Gaussian noise with a rational spectral density, finite at $\omega_j$. Along $\varphi_j$ the hidden position is $\alpha\cos\omega_jt+\beta\sin\omega_jt$, with $\operatorname{Var}\alpha=\operatorname{Var}\beta=T/\omega_j^2$ under the reference. Whittle's asymptotics for a sinusoid in stationary Gaussian noise give Fisher information $\tfrac\tau2(B\varphi_j)^{\mathsf T}(2T\Phi(i\omega_j))^{-1}(B\varphi_j)+O(1)$ for each amplitude. Initial transients of the damped part contribute $O(1)$. The whitened information of the mode is therefore $\tau(B\varphi_j)^{\mathsf T}\Phi(i\omega_j)^{-1}(B\varphi_j)/(4\omega_j^2)+O(1)$, and $1-\lambda_\tau=1/(1+\Xi)$ gives (9.7). $\square$

The certificate checks (9.7) in two cases. With $\Gamma_{II}=0$, the prediction is $2.17125$ and the $1/\tau$-extrapolated value is $2.1712$. With $\Gamma_{II}\ne0$ and colored residual noise, the prediction is $56.585$ and the extrapolated value is $56.574$.

**Proposition 9.8 (scalar inertial closed form).** Let $h=b=1$ with block-diagonal friction $\gamma_B,\gamma_I>0$. Put $\sigma=\sqrt c$, $\rho=\sqrt{c+\gamma_Ib^2/(\gamma_Bc)}$, and $\ell=\sqrt{\gamma_I^2+2\sigma(\rho-\sigma)}$. In whitened $(y,w)$ coordinates,
$$
\boxed{\Xi_\infty=\frac1{2\gamma_I}\begin{pmatrix}(\rho\ell-\sigma\gamma_I)/\sigma&\rho-\sigma\\ \rho-\sigma&\ell-\gamma_I\end{pmatrix}.}
\tag{9.8}
$$
As $\gamma_B,\gamma_I\to\infty$ at fixed ratio, the position visibility $(\Pi_\infty)_{yy}\to(\rho-\sigma)/(\rho+\sigma)=\tan^2(\theta/2)$, the overdamped value of Proposition 9.3. Lower friction raises visibility. For $c=3$, $b=4$, $\gamma_I=2\gamma_B$, the position visibility is $0.9094$, $0.6636$, $0.5173$, $0.3895$, $0.3646$, and $0.3619$ at $\gamma_B=0.1,0.5,1,3,10,100$, against the overdamped value $0.3619$. An underdamped hidden sector is legible; an overdamped one is comparatively private.

*Proof.* The whitened algebraic equation has $\widetilde F=\begin{pmatrix}0&\sigma\\-\sigma&-\gamma_I\end{pmatrix}$, $\widetilde Q=\operatorname{diag}(0,2\gamma_I)$, and $\widehat H=\operatorname{diag}(b^2/(2\gamma_Bc),0)$. Its four solution branches are explicit, and (9.8) is the unique one with $\Xi\succeq0$. The limit follows by expanding in $1/\gamma$. $\square$

**Proposition 9.9 (one rotation is the whole noncommuting obstruction).** Take block-diagonal friction with $\Gamma_{II}\succ0$. In whitened coordinates write
$$
F'=-\tfrac12\widetilde Q+\widetilde A,\qquad \widetilde A=\begin{pmatrix}0&\Sigma\\-\Sigma&0\end{pmatrix},\qquad \Sigma=C^{1/2},
$$
which is the fluctuation–dissipation split into dissipative and reversible parts. Put $Y=\Xi_\infty+\tfrac12I=\begin{pmatrix}Y_{11}&X\\X^{\mathsf T}&Y_{22}\end{pmatrix}$, $\widehat H_B=\tfrac12\Sigma^{-1}B^{\mathsf T}\Gamma_{BB}^{-1}B\Sigma^{-1}$, $K=\Sigma\Gamma_{II}^{-1/2}/\sqrt2$, and $N=\widehat H_B+KK^{\mathsf T}$. Then there is an orthogonal $O\in O(h)$ with
$$
X=\big(N^{1/2}O-K\big)\Gamma_{II}^{-1/2}/\sqrt2,\qquad
Y_{22}=\Gamma_{II}^{-1/2}\Big[\tfrac12\Gamma_{II}^{1/2}\big(\tfrac12\Gamma_{II}+X^{\mathsf T}\Sigma+\Sigma X\big)\Gamma_{II}^{1/2}\Big]^{1/2}\Gamma_{II}^{-1/2},\qquad
Y_{11}=(\Sigma+2X\Gamma_{II})Y_{22}\Sigma^{-1},
\tag{9.9}
$$
and $O$ is fixed by requiring $Y_{11}=Y_{11}^{\mathsf T}$ together with $\Xi\succeq0$. If $C$, $\Gamma_{II}$, and $B^{\mathsf T}\Gamma_{BB}^{-1}B$ commute, then $O=I$, (9.9) is an explicit formula in matrix square roots, and it reduces mode by mode to (9.8). In the certificate's noncommuting network, $O$ is a rotation by $-0.93^\circ$.

*Proof.* Substituting $Y$ turns the whitened algebraic equation into
$$
Y\widetilde QY-[Y,\widetilde A]=\widehat H+\tfrac14\widetilde Q.
$$
Its $(1,1)$ block, $2X\Gamma_{II}X^{\mathsf T}+X\Sigma+\Sigma X^{\mathsf T}=\widehat H_B$, completes to $(\sqrt2X\Gamma_{II}^{1/2}+K)(\cdot)^{\mathsf T}=N$, which determines $X$ up to $O$. The $(2,2)$ block is a matrix square-root equation for $Y_{22}$. The $(1,2)$ block gives $Y_{11}$. In the commuting case the scalar branch has $O=+1$: $N^{1/2}=\rho/\sqrt{2\gamma_I}$ and $K=\sigma/\sqrt{2\gamma_I}$ give $X=(\rho-\sigma)/(2\gamma_I)$, which is (9.8). $\square$

The reversible part $\widetilde A$ is what prevents a general closed form. The overdamped problem has no velocity frame, hence no $\widetilde A$ and no gauge. The spectrum of the inertial problem is nevertheless explicit (Proposition 10.3). An explicit rule for $O$ in the noncommuting case remains open.

## 10. The visibility spectrum is a canonical-correlation spectrum

Sections 8 and 9 compute visibility from a Riccati equation that needs the hidden model $(B,C,\Gamma_{II})$. This section shows that the visibility spectrum is an intrinsic property of the *boundary force alone*.

Step 1 in the proofs of Theorems 8.2 and 9.2 turns the record into increments $dY=\eta\,dt$. Here $\eta$ is the random force of the reduced memory equation: $\eta=\xi_B-Bh$ in (5.1), and $\eta=\xi_B-Bh_y$ in the inertial case with block-diagonal friction. Under the thermal reference the hidden residual is stationary with covariance $S$. Then $\eta$ extends to a stationary Gaussian process on the whole time axis, with spectral density $Q_B(\omega)=2T\operatorname{Re}_HZ_B(i\omega)$ (Theorem 4.1).

**Theorem 10.1 (visibility is past–future canonical correlation).** Assume block-diagonal friction with $\Gamma_{BB}\succ0$ and an observable hidden pair. Let $\sigma_1\ge\sigma_2\ge\cdots$ be the canonical correlation coefficients between the past $\{\eta(t):t<0\}$ and the future $\{\eta(t):t>0\}$ of the stationary thermal random force.

1. **Overdamped.** The $\sigma_i$ are exactly the eigenvalues of $\Pi_\infty$.
2. **Inertial.** The $\sigma_i$ are the singular values of $\Pi_\infty^{1/2}\varepsilon\,\Pi_\infty^{1/2}$, where $\varepsilon=\operatorname{diag}(I,-I)$ reverses hidden velocities. In particular $\sigma_1\le\lambda_{\max}(\Pi_\infty)$.

*Proof.* (i) *Markov property.* Given $h(0)$, the future of $\eta$ depends only on future noise and the past only on past noise; the stationary hidden process is Markov in both time directions. Past and future are therefore conditionally independent given $u=S^{-1/2}h(0)$, and $\operatorname{Cov}u=I$.

(ii) *Factorization.* For a Gaussian chain $\mathrm{past}\to u\to\mathrm{future}$, $\operatorname{Cov}(\mathrm{future},\mathrm{past})=\operatorname{Cov}(\mathrm{future},u)\operatorname{Cov}(u,\mathrm{past})$. By Theorems 8.2 and 9.2, $\operatorname{Cov}(\mathbb E[u\mid\mathrm{future}])=I-(I+\Xi_f)^{-1}=\Pi_f$. So the whitened cross-covariance between future and $u$ has polar form $V_f\Pi_f^{1/2}$ with $V_f$ a partial isometry, and similarly the past gives $\Pi_p$. The whitened past–future cross-covariance is therefore $V_f\Pi_f^{1/2}\Pi_p^{1/2}V_p^{\mathsf T}$, and its singular values are those of $\Pi_f^{1/2}\Pi_p^{1/2}$.

(iii) *Detailed balance.* The hidden drift and covariance satisfy $SF^{\mathsf T}=\varepsilon F\varepsilon S$; in the inertial case both sides equal $T\begin{pmatrix}0&-I\\I&-\Gamma_{II}\end{pmatrix}$. So the time-reversed stationary process is the same process composed with $\varepsilon$. A force is even under reversal, hence $\Pi_p=\varepsilon\Pi_f\varepsilon$. In the overdamped case $\varepsilon=I$. $\square$

The certificate computes the canonical correlations directly from exact increment covariances of $\eta$, with no Riccati equation. For the Section 8.7 witness, extrapolation in the time step gives $0.0689577$ and $0.0054443$, against the eigenvalues $0.0689573$ and $0.0054442$ of $\Pi_\infty$. For an inertial network it gives $0.387488$, $0.285291$, $0.080834$, and $0.051503$, against the singular values $0.387512$, $0.285352$, $0.080835$, and $0.051507$, while $\lambda_{\max}(\Pi_\infty)=0.4926$.

**Corollary 10.2 (the boundary impedance alone fixes the ceiling).** The canonical correlations of a stationary Gaussian process depend only on its spectral density, and they do not change when that density is multiplied by a constant. The force spectrum is $2T\operatorname{Re}_HZ_B(i\omega)$. Therefore, in the overdamped class, the entire visibility spectrum, and in particular the ceiling $\lambda_\infty=\sigma_1$, is a functional of the dissipative part of the boundary impedance alone. Three consequences follow.

1. **Temperature independence is structural.** Remark 8.3a follows without the Riccati equation: fluctuation–dissipation makes the force spectrum $T$ times a $T$-free function, and canonical correlations discard the factor.
2. **The ceiling is measurable at the boundary.** Within the model class, boundary impedance spectroscopy determines $\lambda_\infty$ without identifying the hidden matrices. The eigenvectors, that is, which hidden directions are visible, still require the model.
3. **Inertial lower bound.** In the inertial class the same measurement gives the model-free lower bound $\sigma_1\le\lambda_\infty$.

In stochastic-realization language, the $\sigma_i$ are the canonical correlation coefficients of Akaike (1975), equivalently the Hankel singular values of the stochastically balanced realization (Desai–Pal 1984; Lindquist–Picci 2015). The eigenbasis of $\Pi_\infty$ is the balanced basis. Because the past and future predictor covariances coincide, one orthogonal diagonalization balances both. The mathematics of canonical correlations is classical. What is identified here is its physical content: it is the preparation-visibility spectrum of the thermal network behind the boundary.

**Proposition 10.3 (the optimal boundary filter's poles are impedance zeros).** Let
$$
\Phi(s)=\tfrac12\big[Z_B(s)+Z_B(-s)^{\mathsf T}\big].
$$
This equals $I+B(C^2-s^2)^{-1}B^{\mathsf T}$ for overdamped unit friction, and the $\Phi(s)$ of (9.7) in the inertial block-diagonal case. The eigenvalues of the Hamiltonian matrix $\begin{pmatrix}F'&-Q'\\-H^{\mathsf T}R^{-1}H&-F'^{\mathsf T}\end{pmatrix}$ of (9.3) are the zeros of $\det\Phi(s)$, and the closed-loop matrix $F'-Q'\mathcal I_\infty$ carries the left-half-plane zeros. In the overdamped case these are $\pm\operatorname{eig}\big((C^2+B^{\mathsf T}B)^{1/2}\big)$, consistent with Proposition 8.3.

*Proof.* The Hamiltonian spectrum of a stationary Kalman–Bucy problem consists of the zeros of the para-Hermitian observation spectral density: the closed-loop poles are the zeros of its minimum-phase spectral factor. By Theorem 4.1 that density is $2T\Phi(i\omega)$. In the overdamped case, Sylvester's determinant identity gives $\det\Phi(s)=\det(F^2-s^2)/\det(C^2-s^2)$ with $F=(C^2+B^{\mathsf T}B)^{1/2}$. $\square$

**Proposition 10.4 (no causal boundary observer tracks the hidden state better than the ceiling).** Let $P_f$ be the steady-state error covariance of the Kalman–Bucy estimate of $h(t)$ from the boundary record up to time $t$. Then
$$
P_f=\varepsilon\,(S^{-1}+\mathcal I_\infty)^{-1}\varepsilon,\qquad\text{equivalently}\qquad S^{-1/2}P_fS^{-1/2}=I-\varepsilon\Pi_\infty\varepsilon.
\tag{10.1}
$$
Consequently, for every hidden linear functional,
$$
\operatorname{Var}\big(\ell^{\mathsf T}h(t)\,\big|\,\text{record up to }t\big)\ \ge\ (1-\lambda_\infty)\operatorname{Var}_\sigma(\ell^{\mathsf T}h).
$$
For overdamped unit friction, $P_f=2T(C+F)^{-1}$.

*Proof.* With the stationary prior $S$, the posterior covariance of $h(0)$ given the future record is $(S^{-1}+\mathcal I_\infty)^{-1}$ (Theorem 8.2). Time reversal, as in the proof of Theorem 10.1, maps the future record to the past record and $h(0)$ to $\varepsilon h(0)$. $\square$

A boundary feedback controller (a "boundary demon") can therefore never acquire more than the fraction $\lambda_\infty$ of any hidden thermal variance. Feedback-work bounds of Sagawa–Ueda type limit extractable work by acquired information. Whether this gives a quantitative ceiling on the work that boundary feedback can extract from a hidden sector needs its own argument and is not claimed. For **open-loop** boundary forcing the question is settled by Theorem 8.11, where the same matrix $(C+F)^{-1}=P_f/(2T)$ is the minimal-dissipation form. The feedback case remains open.

**Remark 10.5 (stored versus transmitted information).** Under the thermal reference, the information the entire future record carries about the hidden state is $I(u;\mathrm{future})=-\tfrac12\log\det(I-\Pi_\infty)$. The past–future mutual information of the boundary force, its predictive information in the sense of Bialek–Nemenman–Tishby (2001), is $-\tfrac12\sum_i\log(1-\sigma_i^2)$. In the overdamped class the difference is $\tfrac12\sum_i\log(1+\pi_i)$. In the language of computational mechanics (Crutchfield–Ellison–Mahoney 2009), this is the crypticity of the Gaussian causal state $\mathbb E[u\mid\mathrm{past}]$: information the boundary's own history stores about the hidden sector but never transmits to its future. For the Section 8.7 witness the three numbers are $0.0384546$, $0.0023980$, and $0.0360566$ nats. This is an information-theoretic reading, not a thermodynamic identity.

## 11. Invisible memory is compressible memory

Theorem 5.1 says that eliminating hidden coordinates produces memory. Sections 8–10 say how visible each hidden direction is. This section joins the two: the hidden directions a boundary can barely see are exactly the ones a boundary model can drop.

Take overdamped unit friction; any friction matrix reduces to this by Proposition 9.3. In the whitened hidden coordinates $u=S^{-1/2}(y-Lx)$ the drift is $-C$, because $C$ commutes with $S=TC^{-1}$, and the observation matrix is $BS^{1/2}$.

**Theorem 11.1 (visibility truncation is exact on what it keeps).** Let $V_r\in\mathbb R^{h\times r}$ have orthonormal columns spanning an invariant subspace of $\Pi_\infty$, for example its $r$ most visible eigenvectors. Put
$$
C_r=V_r^{\mathsf T}CV_r,\qquad B_r=BC^{-1/2}V_rC_r^{1/2},\qquad A_r=K_B+B_rC_r^{-1}B_r^{\mathsf T}.
\tag{11.1}
$$

1. **Physical.** $K_r=\begin{pmatrix}A_r&B_r\\B_r^{\mathsf T}&C_r\end{pmatrix}\succ0$ is a pinned network of the same class with $r$ hidden coordinates, and its boundary Schur complement is $K_B$. The static response and the thermal boundary marginal are unchanged, and its random force obeys the fluctuation–dissipation relation (5.2) automatically.
2. **Compressed memory.** Its memory kernel is the compression
   $$
   \widehat{\mathsf G}_r(s)=BC^{-1/2}V_r(sI+C_r)^{-1}V_r^{\mathsf T}C^{-1/2}B^{\mathsf T}
   \quad\text{of}\quad
   \widehat{\mathsf G}(s)=BC^{-1/2}(sI+C)^{-1}C^{-1/2}B^{\mathsf T}.
   $$
3. **Hereditary visibility.** Its infinite-horizon visibility matrix is exactly $V_r^{\mathsf T}\Pi_\infty V_r$. Every preparation supported on the retained whitened subspace therefore has the same infinite-horizon relative entropy and the same sharp contraction coefficient in the reduced network as in the original.
4. **Balanced.** The truncation is the stochastically balanced (canonical-correlation) truncation of the boundary force of Desai and Pal (1984).

*Proof.* (1) $C_r\succ0$ because it is a compression of $C$, and $K_r\succ0$ because its Schur complement $K_B$ is positive. (2) Substitute (11.1) into $B_r(sI+C_r)^{-1}C_r^{-1}B_r^{\mathsf T}$ (Section 5). (3) In whitened form, the steady state of (8.1) reads
$$
\widehat H=C\Xi+\Xi C+2\Xi C\Xi,\qquad \widehat H=\tfrac12C^{-1/2}B^{\mathsf T}BC^{-1/2}.
$$
Choose a basis adapted to the $\Xi$-invariant splitting, so the off-diagonal blocks of $\Xi$ vanish. The retained block of this equation is $\widehat H_r=C_r\Xi_r+\Xi_rC_r+2\Xi_rC_r\Xi_r$, with $\Xi_r=V_r^{\mathsf T}\Xi V_r$ and $\widehat H_r=V_r^{\mathsf T}\widehat HV_r=\tfrac12C_r^{-1/2}B_r^{\mathsf T}B_rC_r^{-1/2}$. That is the steady equation of the reduced network. Its positive-semidefinite solution is unique, because $R=C+2T\mathcal I$ must satisfy $R^2=F^2$ with $R\succ0$ (Proposition 8.3). Formula (8.2) depends on $\Pi$ only through its action on the support of the preparation. (4) In the coordinates $u$, the past and future predictor covariances both equal $\Pi_\infty$ (Theorem 10.1), so the eigenbasis of $\Pi_\infty$ is the stochastically balanced basis, and (11.1) truncates the realization in that basis. $\square$

Item 3 is unusual for balanced truncation, which generally changes the retained Hankel singular values. Here detailed balance makes the truncation hereditary. The certificate finds the retained visibilities unchanged to $1.2\times10^{-13}$ over 200 random truncations.

**Observation 11.2 (error law; numerical).** Let
$$
e=\sup_\omega\big\|Q_B^{-1/2}(Q_{B,r}-Q_B)Q_B^{-1/2}\big\|
$$
be the largest relative error of the boundary force spectrum. Over 500 random truncations,
$$
e\ \approx\ \prod_{i\ \mathrm{dropped}}\Big(\frac{1+\pi_i}{1-\pi_i}\Big)^2-1\ \approx\ 4\sum_{i\ \mathrm{dropped}}\pi_i,
$$
In the certificate's 500 cases, the largest error divided by the product is $1.00000$ and the median is $0.980$. An exploratory set of 1500 cases reached $1.0005$. The bracket is the square of Green's (1988) relative-error bound for balanced *stochastic* truncation, converted from a spectral factor to a spectral density. Our truncation is the Desai–Pal *stochastically balanced* truncation instead, for which that bound is not a theorem, and the small observed excursions above it confirm the difference. We therefore record an empirical law, not a theorem. Truncating instead by hidden decay rates or by modal boundary weight gives a larger error in 96.6% of the certificate's random networks. In an exploratory set of 600 networks the median penalty was $3.7\times$.

**Observation 11.3 (pinned chains compress geometrically).** For the chain of Section 8.9 with $m=k=1$, the visibility spectrum is geometric:
$$
3.796\times10^{-2},\ 1.392\times10^{-3},\ 5.106\times10^{-5},\ 1.872\times10^{-6},\ 6.87\times10^{-8},\ \ldots,
$$
with constant ratio $0.03667$, unchanged between $n=20$ and $n=30$. With Observation 11.2, three hidden coordinates reproduce the boundary force of an arbitrarily long chain to relative error about $8\times10^{-6}$, and four to about $3\times10^{-7}$. A closed form for the ratio is not derived here. The two spatial statements are complementary. Theorem 8.8 says that depth costs visibility exponentially *in space*. Observation 11.3 says that the visibility spectrum also decays geometrically *in index*, so the boundary's memory of an infinite chain is effectively finite-dimensional.

**Inertial case.** The block-restriction identity in item 3 holds verbatim for the inertial whitened equation of Section 9, and the compressed noise still satisfies the fluctuation–dissipation identity $F'+F'^{\mathsf T}+Q'=0$ in whitened form. But the compressed drift generally mixes positions and velocities, so the reduced model need not be mechanical, and uniqueness of the retained solution has not been established. A structure-preserving inertial truncation is open.

## 12. A prospective thermal-circuit test

*Proposed apparatus and model predictions only. No hardware has been built, no data have been acquired, and no detector specification has been validated.*

**Experimental question.** Can an independently calibrated thermal network predict how well a boundary voltage record distinguishes two initial preparations, including the loss caused by ongoing hidden thermal noise? A spatial exponential slope alone cannot answer this. The same exponent occurs in established lattice-Gramian results (Section 1), and a model without hidden bath noise shows it too. The discriminating evidence is absolute visibility, its saturation with record length, and its response to controlled changes of the observation channel.

### 12.1 A passive RC mesh realization of the chain

Use $n+1$ planar meshes $0,\ldots,n$. Each mesh has a private series resistor $R$, a private capacitor $C_p$, and a calibrated series voltage-source port. Adjacent meshes share a capacitor $C_c$, and each exterior mesh also has an end capacitor $C_c$. Let $q_i$ be the oriented integrated mesh current, equivalently the charge on the private capacitor. On the fixed-charge sector the electrostatic energy is
$$
U(q)=\frac1{2C_p}\sum_{i=0}^nq_i^2+\frac1{2C_c}\Big[q_0^2+\sum_{i=0}^{n-1}(q_i-q_{i+1})^2+q_n^2\Big],
$$
so $K_{ii}=C_p^{-1}+2C_c^{-1}$ and $K_{i,i+1}=-C_c^{-1}$. Every resistor is private to one mesh, so the dissipation matrix is $RI$. Ideal Johnson noise at common temperature $\Theta$ gives
$$
R\,dq=(-Kq+f)\,dt+\sqrt{2Rk_B\Theta}\,dW,\qquad \Sigma_{\rm eq}=k_B\Theta K^{-1}.
$$
After rescaling $\hat t=t/(RC_c)$ and $\hat q=q/\sqrt{k_B\Theta C_c}$, this is exactly the chain of Section 8.9 with $k=1$ and $m/k=C_c/C_p$. A generic node-voltage RC ladder need not have this independent-noise, unit-mobility structure. Thermal RC networks mapped to coupled overdamped coordinates have experimental precedent (Baiesi et al. 2016).

| Proposed quantity | Value | Status |
|---|---:|---|
| Loops | 13: one boundary and 12 hidden | Illustrative design |
| Private resistance | $10\,\mathrm{M}\Omega$ | Assumed equal; calibrate each |
| Shared and end capacitance | $1\,\mathrm{nF}$ | Assumed ideal |
| Private capacitance | $5\,\mathrm{nF}$ | Gives $m/k=0.2$ |
| Bath temperature | $300\,\mathrm K$ | Illustrative |
| Time unit $RC_c$ | $10\,\mathrm{ms}$ | Derived |
| Record | $200\,\mathrm{ms}$ at $0.5\,\mathrm{ms}$ | 401 samples, including $t=0$ |
| Detector RMS per sample | $32.6\,\mathrm{nV}$ | Assumed white; not a verified capability |

For this design the visibility spectrum (Theorem 10.1) is
$$
0.1179,\ 1.27\times10^{-2},\ 1.36\times10^{-3},\ 1.42\times10^{-4},\ldots .
$$
Its ceiling $\lambda_\infty=0.1179$ is also the leading past–future canonical correlation of the boundary force.

### 12.2 Preparation, likelihood, and predictions

**Covariance-preserving preparation.** Start in equilibrium. To create a mean displacement $\delta e_d$ without changing the covariance, follow a smooth $\bar q(t)=s(t)\delta e_d$, with $s$ rising from $0$ to $1$ and $\dot s$ vanishing at both ends, by applying $f(t)=R\dot{\bar q}+K\bar q$. Deterministic additive forcing does not change the covariance evolution. At the record start the boundary marginal is unchanged and the hidden conditional mean is shifted by exactly $\delta e_d$. For target cost $J$, $\delta=\sqrt{2k_B\Theta J/(C_p^{-1}+2C_c^{-1})}$. For $J=1$ nat at the operating point this is $1.9405\,\mathrm{fC}$, or $0.3881\,\mu\mathrm V$ on the target capacitor. Preparation may use interior ports; the scored observation uses only the boundary record.

**Exact sampled likelihood.** For boundary samples at times $t_i$, including $0$, put $F(t)=e^{-Kt/R}$ and
$$
b_i=\delta\,e_0^{\mathsf T}F(t_i)e_d,\qquad
V_{ij}=e_0^{\mathsf T}F(|t_i-t_j|)\Sigma_{\rm eq}e_0+(V_{\rm det})_{ij},\qquad
D_{\rm rec}=\tfrac12b^{\mathsf T}V^{-1}b.
$$
The log-likelihood ratio $\ell(y)=b^{\mathsf T}V^{-1}y-D_{\rm rec}$ is $\mathcal N(D_{\rm rec},2D_{\rm rec})$ under the prepared law and $\mathcal N(-D_{\rm rec},2D_{\rm rec})$ under the reference. This gives a directly testable score distribution and needs no high-dimensional nonparametric estimate of relative entropy. A miscalibrated model need not reproduce these moments, so held-out validation is essential.

| Depth | Ideal infinite-time $D/J$ | Finite detector-record $D/J$ | Trials for 10% classification error | Trials for 20% KL precision at 95% |
|---:|---:|---:|---:|---:|
| 1 | 0.0490316 | 0.0481224 | 69 | 3,992 |
| 2 | 0.00697043 | 0.00695410 | 473 | 27,621 |
| 3 | 0.00178929 | 0.00178731 | 1,838 | 107,465 |
| 4 | 0.000549132 | 0.000548662 | 5,987 | 350,075 |
| 5 | 0.000183627 | 0.000183485 | 17,902 | 1,046,803 |
| 6 | 0.0000645135 | 0.0000644630 | 50,956 | 2,979,585 |

All rows use $J=1$ nat. The trial counts treat calibrated parameters as known. At depth 2, deleting the hidden process noise from the comparison model predicts $0.00857554$ instead of $0.00695410$, about 23% higher. That counterfactual is a diagnostic, not an equilibrium model.

### 12.3 The cheaper first test: the bath model itself

The thermal hypothesis $H_1$ (all resistors supply noise) and the counterfactual $H_0$ (hidden bath noises omitted) have the same mean response but different record covariances $V_1,V_0$. They can be distinguished using *unprepared* equilibrium records, as a bath-model and apparatus check. That is distinct from, and much cheaper than, measuring preparation relative entropy.

**Scalar covariance test.** Freeze, from calibration data, the leading generalized eigenvector $w$ of $(V_1,V_0)$. At the nominal point $\lambda=w^{\mathsf T}V_1w/w^{\mathsf T}V_0w=1.6405$. For $N$ independent records, $(N-1)s_Z^2/v_0$ is exactly $\chi^2_{N-1}$ under a Gaussian model. Rejecting at the 95% quantile gives power $1-F_{\chi^2_{N-1}}(\chi^2_{N-1,0.95}/\lambda)$, which is at least 90% from $N=71$. Shared calibration errors are a fixed nuisance across the batch and are not reduced by $\sqrt N$. If both projected variances carry certified $\pm10\%$ bounds, the sufficient budget becomes 198 records. If the bounds have only 99% joint coverage, allotting the coverage failure to the error budget gives 219, rounded to a 220-record pilot. Beyond a symmetric envelope of $(\lambda-1)/(\lambda+1)=24.26\%$, no record count guarantees the target power for this test.

**What the stress study found.** The study included detector bandwidth, a reset detector state, 45 nuisance parameters, and exact discretization.

- Bandwidth from 1 to 300 Hz barely changes the covariance-test budget, which stays at 71. The depth-2 preparation relative entropy at 1 Hz is about 14% below its 100 Hz value.
- Uncalibrated $\pm5\%$ component mismatch drives the nominal 5% test to false-positive rates of up to 21.5%.
- Calibrate first the gain (log-sensitivity about 2), the observed private capacitance (about $-1.75$), temperature (about 1), and the boundary resistance, whose sensitivity differs between models (0.97 versus 0.58).

**Two-mode ratio test.** Using the variance ratio of the leading and a physical reference generalized mode cancels an unknown common gain exactly, and its law is exact even when mismatch correlates the two scores. Let the per-trial score pair be Gaussian with covariance $\begin{pmatrix}a&c\\c&b\end{pmatrix}$, and $\nu=N-1$. Then
$$
\Pr(R_N>t)=\overline F_{\nu,\nu}\big(k(t)\big),\qquad
k(t)=\frac{\Delta(t)-a+tb}{\Delta(t)+a-tb},\qquad \Delta(t)=\sqrt{(a+tb)^2-4tc^2},
$$
a standard Gaussian quadratic-form calculation that was checked against Wishart sampling. For thresholds above the ratio $a/b$, correlation only lowers the tail, so the uncorrelated case is conservative. The tested pair nevertheless needs 147 records nominally and 467 under its tight conditional coverage, against 71 and 219 for the one-mode test. The denominator adds sampling noise and increases sensitivity to boundary resistance and detector cutoff. The one-mode test remains the baseline.

### 12.4 New handles from Part II

- **Impedance-only prediction (Corollary 10.2).** Measure the boundary port impedance and compute the canonical correlations of $\operatorname{Re}Z_B(i\omega)$. This predicts $\lambda_\infty=0.1179$ for the design above without using the component values that predict the same number from the network model. Agreement between the two routes tests the thermal network model at the boundary.
- **Friction-structure control (Proposition 9.3).** Changing how resistance is shared changes the ceiling in a parameter-free way, through $(\widetilde C,\widetilde B)$ in (9.5). Adding $2R$ in series in mesh 1 raises $\lambda_\infty$ from $0.118$ to $0.220$: a stickier hidden mesh is more visible. A resistor $R$ shared by meshes 0 and 1 introduces cross friction and *lowers* it to $0.046$. The opposite signs test the friction dependence directly. This overdamped circuit always has private noise. The legibility caused by a shared bath (Corollary 9.6) is an inertial effect and would need an underdamped LC realization.
- **Compression (Theorem 11.1).** A reduced RC network with the three most visible modes should reproduce the boundary force spectrum of the 13-loop chain to about $4\sum_{i>3}\pi_i\approx6\times10^{-4}$.

### 12.5 Recommended order and limits

1. Validate the detector reset, low-frequency noise, loading, and the plant's calibrated response and fluctuation–dissipation relation. Establish independence between trials.
2. Run the impedance-only cross-check of Section 12.4.
3. Freeze the projected score and a nuisance-aware threshold. If a $\pm10\%$ envelope with 99% joint coverage is established, acquire about 220 unprepared records for the bath-model pilot.
4. Only then acquire depth-1 and depth-2 preparation trials, to test absolute visibility, saturation with record length, and the predicted score distributions.

Amplifier backaction, charge leakage, colored bath noise, filter initialization, preparation jitter, and drift between trials are not covered by these calculations. Failing to reject $H_0$ is not confirmation, and rejecting it does not confirm every assumption.

## 13. What is established, and what is not

**Part I.** The exact class is closed under boundary elimination *with memory, correlated noise, and preparation data retained*. It is generally not closed within memoryless local networks. Static thermal marginalization and zero-frequency response agree, but the full dynamic response needs frequency information. The relative-entropy defect identifies a unique classical thermal refinement and prices departures from it. Those departures alter the finite-time random force, and every elimination stage composes without changing the final account. Kron-compatible thermal growth adds no relative-entropy resource, while nonthermal conditional preparation contributes $TJ$. A change of the coarse reference adds the explicit mismatch term of Section 3. A quantum bridge requires modular-state reduction (Proposition 7.3) or restricted recovery (Remark 7.4), not an unqualified classical construction.

**Part II.** For linear thermal networks, the boundary record sees a hidden preparation through an exact Gaussian attenuation channel. Its visibility spectrum has four equivalent descriptions:

- the eigenvalues of an initial-state information matrix (Sections 8–9);
- the normalized variance reduction of the optimal boundary tracker (Proposition 10.4);
- the past–future canonical correlations of the boundary random force (Theorem 10.1), which depend only on the dissipative boundary impedance (Corollary 10.2);
- the retention order of a structure-preserving model reduction (Theorem 11.1).

The ceiling is strictly below one exactly when the hidden sector has noise the boundary does not share (Theorem 9.4). Overdamped networks always do. Inertial networks can lose that privacy through a shared bath, an undamped coupled boundary direction, or a noiseless visible hidden mode. In pinned chains the spectrum is screened exponentially in depth (Theorem 8.8) and decays geometrically in index (Observation 11.3). The same spectrum also prices action. Open-loop boundary forcing harvests from a hidden mean exactly $T$ times what the record learns, and it must dissipate $T$ times the posterior slack (Theorem 8.11, Corollary 8.12).

**Statements this paper does not make.**

- It does not claim a first spatial screening law; the deterministic Gramian exponent is prior work.
- "Feedback cannot improve measurement" holds only for an ideal record and a controller with no extra information (Theorem 8.7).
- "Cooling cannot help" is not claimed. The normalized coefficient is independent of temperature, but fixed physical preparations and fixed detector noise are not.
- "Information loss is heat" is claimed only in the scoped form of Corollary 8.12. For thermal-covariance mean shifts under open-loop additive boundary forcing, the minimal mean dissipation equals $T$ times the posterior slack. No such identification is made for covariance preparations, feedback, or parametric control.
- "Every deep preparation is screened" is not claimed. The complementary thermal modes and their independence are part of the preparation class.
- "The visibility ceiling bounds boundary feedback work" is not claimed (Proposition 10.4 and the remark after it). It is proved only for open-loop forcing (Theorem 8.11).
- "Exploration resolves itself" is not claimed. In this class additive boundary actions have zero epistemic value (Theorem 8.7), and the ignorance penalty (8.23) is not shown to be recoverable by any adaptive protocol.
- There is no experimental confirmation; Section 12 contains predictions only.

**Open problems.**

1. An explicit rule for the inertial gauge $O$ (Proposition 9.9).
2. A structure-preserving inertial truncation and a proved error bound for visibility truncation (Observation 11.2).
3. A closed form for the geometric ratio of the chain spectrum (Observation 11.3).
4. Spatial laws in higher dimensions and the unpinned limit.
5. A quantum preparation-to-record channel for correlated references.
6. Feedback harvesting: how much of the ignorance penalty (8.23) a causal boundary policy can recover, net of measurement and memory costs.
7. Parametric harvesting of covariance preparations, and Theorem 8.11 for general friction and inertial networks.

No geometry-locking equation, continuum gravitational law, or arithmetic positivity theorem is deduced here. What is available is an exact baseline against which a proposed reduction, refinement, or claim of hidden-sector legibility can be checked.

## 14. Certificates and reproducibility

All scripts are author certificates. Their criteria were written before first execution, after the derivations; they are neither blind discovery nor independent review. Finite witnesses support the algebra, and the proofs carry the universal quantifiers. Run everything from the repository root. Each script writes machine-readable results beside itself, and execution logs and any checker repairs are retained.

### 14.1 Bridge certificate (Part I)

`empirical/boundary60/bridge_cert.py`, results in `bridge_cert_results.json`, log `run1.log`. **Run 1: 14/14 passed in 3.61 s** (Python 3.12.13, SymPy 1.14.0, NumPy 2.4.4, SciPy 1.17.1), with no failed checks or repairs.

| Checks | Result and evidence |
|---|---|
| E1–E4: static, conditional KL, recovery, two elimination orders | 4/4 exact; a general conditional-mismatch witness has $J=9.34979115$ nats |
| E5: dynamic response and source transfer | Exact rational-function identity in $s$, both orders |
| E6: correlated noise, reduced FDT, susceptibility FDT | Exact at three rational frequencies, both orders |
| E7: memory kernel and preparation transient | Exact Laplace identity and finite-time covariance for $t\ge u\ge0$ |
| E8–E9: passivity and cascade defect | Exact rational witnesses |
| C1–C3: controls | All detected: omitted hidden noise, discarded induced correlations, naive quantum Kron marginal |
| N1: integrated equilibrium spectrum and Lyapunov covariance | Maximum covariance error $1.28\times10^{-15}$; quadrature estimate $2.91\times10^{-13}$ |
| N2: predictive visibility | Initial boundary KL $=0$; future two-time KL $=0.00268453397$ nats, below the conditional cost $1.45861229$ nats |

### 14.2 Visibility certificate (Section 8.1–8.7)

`empirical/boundary60/visibility_cert.py`, results in `visibility_cert_results.json`, log `visibility_run1.log`. **Run 1: 11/11 passed in 1.04 s**, with no failed checks or repairs. E1–E2 are symbolic; N1–N9 are deterministic numerical checks with tolerances declared before execution.

| Check | Result |
|---|---|
| E1: scalar information and visibility | Exact Riccati identity; $\pi_{\log2/5}=4/21$, $\pi_\infty=1/4$ for $c=3,b=4$ |
| E2: dark mean and visible/dark covariance correlation | Exact zero path KL despite positive preparation KL |
| N1: backward Riccati / forward innovations / hyperbolic solution | Maximum disagreement $5.56\times10^{-14}$ for noncommuting $C,B^{\mathsf T}B$ |
| N2: infinite-horizon algebraic solution | Residual $7.11\times10^{-15}$; long-time discrepancy $2.72\times10^{-14}$; temperature invariance checked |
| N3: exact full-network sampled paths | Nested-grid information increases toward the continuous result; maximum error $4.61\times10^{-7}$ at 2048 samples |
| N4: direct multitime covariance KL | Agrees with the sufficient-statistic formula within $2\times10^{-10}$ |
| N5: posterior slack | $1.458612288668-0.011951983061=1.446660305607$ nats |
| N6: sharp contraction, local covariance attenuation | Mean preparation attains the largest eigenvalue; quadratic expansion relative error $9.98\times10^{-6}$ |
| N7: observability | Rank-one observation of distinct decay rates gives positive-definite information; the dark control stays exactly invisible |
| N8: original witness | Infinite-path visible fraction $0.008195519693$; dense sampled record converges to the finite-path formula |
| N9: affine conditional mean | Averaged formula agrees with the joint $(x(0),r)$ Gaussian KL within $2\times10^{-12}$ |

The angle identity of Remark 8.3b was checked separately in `two_mode_test.py`: twelve rotated three-mode cases, each with a dark mode, agree within $6.25\times10^{-16}$.

### 14.3 Spatial and control certificate (Sections 8.8–8.9)

`empirical/boundary60/spatial_control_cert.py`, results in `spatial_control_cert_results.json`. **Run 2: 6/6 passed in 8.77 s.** Run 1 passed its spatial and linear-control checks, then stopped at a NumPy array-to-scalar conversion error in the nonlinear round-trip check. Replacing that conversion by `.item()` repaired the script; formulas and tolerances were unchanged. Check N6 was added before run 2. Both logs are retained.

| Check | Result |
|---|---|
| N1: all intermediate and final spatial bounds | 45 chain/depth cases at 70-digit precision; maximum Riccati residual $1.03\times10^{-68}$; explicit Green function verified |
| N2: deep local preparations | At $m=k=1$, $n=d=8,16,24,32$, fractions $4.86345\times10^{-9}$, $6.49541\times10^{-16}$, $1.05824\times10^{-22}$, $1.85472\times10^{-29}$ lie between the proved bounds |
| N3: exact sampled full-network transitions | Three boundary-feedback gains converge to the same continuous information; maximum error at 2048 samples $1.46\times10^{-6}$ |
| N4: nonlinear causal feedback | Discrete transformation and inverse agree within $3.11\times10^{-15}$; a consistency check, not a convergence proof |
| N5: non-Gaussian local preparation | Direct quadrature for three symmetric Gaussian mixtures satisfies the scalar contraction bound |
| N6: deep-subspace coefficient | All six depths of a six-site interior satisfy the trace bound and dominate the local coefficient |

The finite numerical log-rates approach $2\kappa$ but do not establish the limit. The analytic bounds (8.14) and (8.19) establish it uniformly in chain length.

### 14.3a Harvest certificate (Section 8.10)

`empirical/boundary60/harvest_cert.py`, results in `harvest_cert_results.json`, logs `harvest_run1.log` and `harvest_run2.log`. **Run 2: 8/8 passed in 51.8 s.** Run 1 passed 5/8, and all three failures were in the checks themselves:
- H2 declared the closed-loop identity $B^{\mathsf T}BG+C=F$, which is false for noncommuting $C,B^{\mathsf T}B$ (error $0.19$). The correct $XFX^{-1}$ is the one stated in the proof of Theorem 8.11.
- H7's quadrature underflowed.
- C1's full-actuation control was mis-specified.

Repairs are documented in the script header; no other criterion changed.

| Check | Result |
|---|---|
| H1: scalar exact | $G=1/(c+f)$ solves the Riccati identity symbolically. For $c=3,b=4$ the PSD solution is $P=ww^{\mathsf T}/8$, $w=(4,3)$, and the harvest fraction is exactly $1/4=\pi_\infty$ |
| H2: matrix identities, independent control solver | 201 networks with boundary and hidden dimensions $1$–$4$. The free-end LQ Riccati ODE, integrated backward from zero, matches $[B;C]X^{-1}[B;C]^{\mathsf T}$ to $1.0\times10^{-13}$; the harvest matrix matches $\Pi_\infty$ from (8.8) to $3.2\times10^{-12}$ |
| H3: Sekimoto work in time | Energy balance $3.2\times10^{-13}$. $W(\tau_r)=0.35155,\ldots,0.37243$ increases to Richardson $0.3738303$ against $W^*=0.3738310$ |
| H4: full-network Monte Carlo | 20,000 exact-transition paths with *nonthermal* covariance: $0.36299\pm0.00329$ against the mean-only prediction $0.36230$ ($z=0.21$) |
| H5: no protocol beats $W^*$ | 400 random and near-optimal protocols give at most $0.36296<0.37383$; $f\equiv0$ gives $0$ |
| H6: equality and strictness | Mean shift: ratio $1.000000000000$. Witness: harvest $0.017108500<T\mathcal D_\infty=0.017931129$ |
| H7: ignorance penalty | Averaging identity $9\times10^{-16}$; penalty $0.050049=\tfrac T2\operatorname{tr}(\Pi\Sigma_\alpha)$, above $TI=0.040301$ |
| C1: controls | Wrong gain $(2C)^{-1}$ harvests $0.372504<W^*$; the full-actuation solver returns $P=0$ |

### 14.4 General-network certificate (Sections 9–11 and Proposition 7.3)

`empirical/boundary60/general_networks_cert.py`, results in `general_networks_cert_results.json`, log `general_networks_run1.log`. **Run 1: 17/17 passed in 464.5 s** (Python 3.12.13, NumPy 2.4.4, SciPy 1.17.1, mpmath 1.3.0), with no failed checks or repairs. The brute-force comparisons never use the reduced observation model. They sample the *full* network's exact Gaussian transitions and compute the relative entropy of the sampled boundary record directly. Extrapolation orders were declared with the criteria.

| Check | Result |
|---|---|
| G1: overdamped arbitrary friction (Prop. 9.3) | Closed form with $(\widetilde C,\widetilde B)$ $0.0797623783$; correlated Riccati identical; full-network brute force with second-order Richardson $0.0797623783$ |
| G2: inertial, block-diagonal friction (Thm. 9.2) | Formula $0.206652117$; brute force extrapolated $0.206652029$ |
| G3: inertial, cross friction (Thm. 9.2) | Formula $0.270999897$; brute force extrapolated $0.270999730$ |
| G4: undamped boundary direction (Thm. 9.5) | Bryson–Johansen formula $0.701945404$; 45-digit brute force extrapolated $0.701950176$; exact-direction $1-\mathcal D/J=2.41\times10^{-4},3.06\times10^{-5},3.86\times10^{-6}$ (third order) |
| G5: private-bath principle (Thm. 9.4, Cor. 9.6) | Common bath $\lambda_\tau=0.387,0.810,0.976,0.9975$; private baths saturate at $0.3436$; dark undamped mode fixed at $0.2332021144$; visible undamped mode $0.643\to0.876$ |
| G6: approach rate (Prop. 9.7) | $\Gamma_{II}=0$: predicted $2.17125$, extrapolated $2.17120$; $\Gamma_{II}\ne0$: predicted $56.5854$, extrapolated $56.5745$ |
| G7: scalar inertial closed form (Prop. 9.8) | Largest mismatch from the numerical equation $6.7\times10^{-16}$; position visibility decreases to $0.361941$ against $\tan^2(\theta/2)=0.361914$ |
| G8: inertial gauge (Prop. 9.9) | Noncommuting: $O$ orthogonal to $6.7\times10^{-16}$, rotation $-0.9331^\circ$; commuting: $O=I$ |
| C1: canonical correlations, overdamped (Thm. 10.1) | Witness $0.0689577,0.0054443$ vs eig $\Pi_\infty$ $0.0689573,0.0054442$; strong coupling $0.5100671,0.2442669$ vs $0.5100671,0.2442667$ |
| C2: canonical correlations, inertial (Thm. 10.1) | $0.387488,0.285291,0.080834,0.051503$ vs singular values $0.387512,0.285352,0.080835,0.051507$; $\lambda_{\max}=0.492638$ |
| C3: Hamiltonian spectrum (Prop. 10.3) | All 8 eigenvalues are zeros of $\det\Phi$ to normalized $1.4\times10^{-14}$ |
| C4: tracking bound (Prop. 10.4) | Kalman steady state equals $\varepsilon(S^{-1}+\mathcal I_\infty)^{-1}\varepsilon$ to $5.0\times10^{-16}$; overdamped $2T(C+F)^{-1}$ to $5.6\times10^{-17}$ |
| C5: information budget (Rem. 10.5) | Stored $0.0384546$, transmitted $0.0023980$, crypticity $0.0360566$ nats |
| R1: hereditary truncation (Thm. 11.1) | 200 truncations: retained visibilities unchanged to $1.2\times10^{-13}$; $K_r\succ0$; Schur complement preserved to $1.3\times10^{-14}$ |
| R2: error law (Obs. 11.2) | 500 truncations: largest error divided by $\prod((1+\pi_i)/(1-\pi_i))^2-1$ is $1.00000$, median $0.980$; visibility truncation beats the better of two modal truncations in 96.6% |
| R3: chain spectrum (Obs. 11.3) | $n=30$, $m=k=1$: $3.7963\times10^{-2}$, $1.3923\times10^{-3}$, $5.1055\times10^{-5}$, $1.8722\times10^{-6}$, $6.8657\times10^{-8}$, $2.5177\times10^{-9}$; every ratio $0.03667$; $n=20$ agrees |
| Q1: effective quantum oscillator (Prop. 7.3) | $X_B=67/120$, $P_B=59/60$, $2\sqrt{X_BP_B}=1.4819282$, $\omega_{\rm eff}=1.1822857$, $m_{\rm eff}=1.1224866$, $k_{\rm eff}=1.5690111$; at $T=100$, $m_{\rm eff}=1.000007$ and $k_{\rm eff}=1.600000$ |

### 14.5 Experimental prediction scripts (Section 12)

These are model calculations only; no experimental validation has been performed.

- `experiment_predictions.py`: **7/7 declared checks on run 1** (`experiment_run1.log`). Dense record inversion agrees with an independent innovations recursion to $1.53\times10^{-16}$. Sampled and noisy records obey the ideal ceiling, and denser sampling improves information. Temperature normalization and the fixed-detector exception behave as predicted. The finite-ramp preparation agrees to $2.38\times10^{-14}$. The prior lattice exponent maps exactly onto ours. Outputs are in `experiment/`.
- `experiment_stress.py`: **7/7 on run 1** (`stress_run1.log`). The augmented thermal Lyapunov residual is $5.11\times10^{-15}$. Dense and adjoint covariances agree to relative $6.77\times10^{-16}$. A full-state Monte Carlo with 12,000 trials per hypothesis agrees with the projected variances within 0.79 standard errors. Outputs, including frozen projection weights, are in `stress/`.
- `two_mode_test.py`: **8/8 on run 1** (`two_mode_run1.log`), including the correlated-ratio law against 150,000 Wishart samples in each of three cases. `rc_record_model.py` exposes the shared record-model definitions. Outputs are in `two_mode/`.

## References and local antecedents

- I. Klickstein and F. Sorrentino, *The controllability Gramian of lattice graphs*, Automatica 114 (2020), 108833. [DOI](https://doi.org/10.1016/j.automatica.2020.108833). Accessible preprint titled *Optimal Input Placement in Lattice Graphs*, [arXiv:1808.07750](https://arxiv.org/abs/1808.07750). Direct antecedent for the chain spatial exponent.
- Y. Subaşı and M. Demirekler, *Quantitative measure of observability for linear stochastic systems*, Automatica 50 (2014), 1669–1674. [Institutional record](https://open.metu.edu.tr/handle/11511/58015). Information-based stochastic observability antecedent; the earlier [IFAC 2011 paper](https://skoge.folk.ntnu.no/prost/proceedings/ifac11-proceedings/data/html/papers/0829.pdf) is openly available.
- G. I. Harris, D. L. McAuslan, T. M. Stace, A. C. Doherty and W. P. Bowen, *Minimum requirements for feedback enhanced force sensing*, Physical Review Letters 111 (2013), 103603. [arXiv:1303.1589](https://arxiv.org/abs/1303.1589). Measurement-record equivalence and feedback-neutrality antecedent for Theorem 8.7.
- E. A. Maximenko and G. Sánchez Arzate, *Inverses of positive tridiagonal Toeplitz matrices* (2016). [Author manuscript](https://www.egormaximenko.com/toeplitz/inverses_of_positive_tridiagonal_Toeplitz_matrices.pdf). Classical hyperbolic Green-function formulas used in Theorem 8.8.
- Y. Polyanskiy and Y. Wu, *Strong data-processing inequalities for channels and Bayesian networks* (2015; revised 2016). [arXiv:1508.06025](https://arxiv.org/abs/1508.06025). Strong data-processing coefficients and their relation to maximal correlation; provenance for Theorem 8.4(3).
- V. Anantharam, A. Gohari, S. Kamath and C. Nair, *On Maximal Correlation, Hypercontractivity, and the Data Processing Inequality studied by Erkip and Cover* (2013). [arXiv:1304.6133](https://arxiv.org/abs/1304.6133). Tight contraction constants and the distinction from squared maximal correlation in general.
- L. Gross, *Logarithmic Sobolev Inequalities*, American Journal of Mathematics 97 (1975), 1061–1083. [DOI](https://doi.org/10.2307/2373688). Gaussian log-Sobolev inequality underlying the arbitrary-preparation entropy contraction.
- R. E. Kalman and R. S. Bucy, *New Results in Linear Filtering and Prediction Theory*, Journal of Basic Engineering 83 (1961), 95–108. [Original paper](https://eceweb1.rutgers.edu/~gajic/pdffiles/519KalmanFiltering/KalmanBucy1961.pdf). Canonical filtering/Riccati provenance; Section 8 derives its initial-state information specialization directly.
- G. W. Ford, M. Kac and P. Mazur, *Statistical Mechanics of Assemblies of Coupled Oscillators*, Journal of Mathematical Physics 6 (1965), 504–515. [Original paper](https://fig.if.usp.br/~marchett/fismat3/coupled-oscillators_ford-kac-mazur.pdf).
- R. Zwanzig, *Nonlinear generalized Langevin equations*, Journal of Statistical Physics 9 (1973), 215–220. [Publisher](https://link.springer.com/article/10.1007/BF01008729).
- D. E. Crabtree and E. V. Haynsworth, *An identity for the Schur complement of a matrix*, Proceedings of the American Mathematical Society 22 (1969), 364–366. [DOI](https://doi.org/10.1090/S0002-9939-1969-0255573-1). Quotient identity underlying Section 6.
- J. C. Baez and B. Fong, *A Compositional Framework for Passive Linear Networks*, Theory and Applications of Categories 33 (2018), 1158–1222. [arXiv:1504.05625](https://arxiv.org/abs/1504.05625).
- L. Ma, X. Li and C. Liu, *The Derivation and Approximation of Coarse-grained Dynamics from Langevin Dynamics* (2016; revised 2017). [arXiv:1605.04886](https://arxiv.org/abs/1605.04886). Prior work on memory and FDT in Langevin reduction.
- M. Junge, R. Renner, D. Sutter, M. M. Wilde and A. Winter, *Universal recovery maps and approximate sufficiency of quantum relative entropy*, Annales Henri Poincare 19 (2018), 2955–2978. [arXiv:1509.07127](https://arxiv.org/abs/1509.07127). Quantum recovery context; the classical proofs here are elementary.
- H. Akaike, *Markovian representation of stochastic processes by canonical variables*, SIAM Journal on Control 13 (1975), 162–173. Canonical correlations between past and future; Theorem 10.1.
- U. B. Desai and D. Pal, *A transformation approach to stochastic model reduction*, IEEE Transactions on Automatic Control 29 (1984), 1097–1100. Stochastically balanced realizations and truncation; Sections 10–11.
- A. Lindquist and G. Picci, *Linear Stochastic Systems: A Geometric Approach to Modeling, Estimation and Identification*, Springer (2015). Stochastic realization, splitting subspaces, and canonical correlations.
- M. Green, *A relative error bound for balanced stochastic truncation*, IEEE Transactions on Automatic Control 33 (1988), 961–965. The bound compared in Observation 11.2.
- A. E. Bryson and D. E. Johansen, *Linear filtering for time-varying systems using measurements containing colored noise*, IEEE Transactions on Automatic Control 10 (1965), 4–10. Reduction for perfect measurements; Theorem 9.5.
- H. Kwakernaak and R. Sivan, *Linear Optimal Control Systems*, Wiley (1972); B. D. O. Anderson and J. B. Moore, *Optimal Filtering*, Prentice-Hall (1979). Riccati convergence under detectability; Theorem 9.4.
- D. Petz, *Sufficient subalgebras and the relative entropy of states of a von Neumann algebra*, Communications in Mathematical Physics 105 (1986), 123–131. Petz recovery map; Remark 7.4.
- W. Bialek, I. Nemenman and N. Tishby, *Predictability, complexity, and learning*, Neural Computation 13 (2001), 2409–2463. Predictive information; Remark 10.5.
- J. P. Crutchfield, C. J. Ellison and J. R. Mahoney, *Time's barbed arrow: irreversibility, crypticity, and stored information*, Physical Review Letters 103 (2009), 094101. Crypticity; Remark 10.5.
- T. Sagawa and M. Ueda, *Generalized Jarzynski equality under nonequilibrium feedback control*, Physical Review Letters 104 (2010), 090602. Feedback work and information; remark after Proposition 10.4.
- Y. Baram and T. Kailath, *Estimability and regulability of linear systems*, IEEE Transactions on Automatic Control 33 (1988), 1116–1121. [NASA record](https://ntrs.nasa.gov/citations/19990111676). Posterior improvement versus deterministic observability.
- N. D. Powel and K. A. Morgansen, *Empirical observability Gramian for stochastic observability of nonlinear systems*. [arXiv:2006.07451](https://arxiv.org/abs/2006.07451). Process noise and information-based observability.
- *Informational steady states and conditional entropy production in continuously monitored systems*, PRX Quantum 3 (2022), 010303. [DOI](https://doi.org/10.1103/PRXQuantum.3.010303). Information acquisition competing with environmental loss.
- M. Baiesi, S. Ciliberto, G. Falasco and C. Yolcu, *Thermal response of nonequilibrium RC-circuits*. [arXiv:1607.01531](https://arxiv.org/abs/1607.01531). Experimental thermal RC networks mapped to overdamped harmonic coordinates; Section 12.
- NIST/SEMATECH *e-Handbook of Statistical Methods*, chi-square and F tests for variances. [Chi-square](https://www.itl.nist.gov/div898/handbook/eda/section3/eda358.htm), [F test](https://itl.nist.gov/div898/handbook/eda/section3/eda359.htm). Section 12.3.
- K. Sekimoto, *Stochastic Energetics*, Lecture Notes in Physics 799, Springer (2010). Work along stochastic trajectories; Section 8.10.
- B. Millidge, A. Tschantz and C. L. Buckley, *Whence the Expected Free Energy?*, Neural Computation 33 (2021), 447–482. [DOI](https://doi.org/10.1162/neco_a_01354), [arXiv:2004.08128](https://arxiv.org/abs/2004.08128). Risk/ambiguity structure of expected free energy; Remark 8.14.
- PortPrinciple.md, Proposition 4.4 and Theorem 8.1: completion-independent defect and thermal noise.
- Paper 54, Theorems 1–2: relative entropy/free energy and static FDT.
- Paper 55, Theorem 2.2: passive composition and Kron reduction.
- Paper 56, Proposition 2.4: classical modular Hamiltonian and Kron reduction.
- Paper 58, Theorem 1: single-mode conditional refinement cost. The present result extends its identity to matrix conditionals, dynamical noise, and a prediction bound.
