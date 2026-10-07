# 54 — The One Functional, Derived: Gibbs, the Cumulant Tower, and Space = Inertia as Fluctuation–Dissipation

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*Draft 4 — October 2, 2026*

<!--
Program record (internal; pandoc drops HTML comments).
Foundations paper, first layer of the 2026-10-01 corpus reorganization: the Port Principle sits BELOW Paper 32.
Paper 32 (Claim 2.1) posits Phi = log Z as "the categorical effective action"; Paper 32 Thm 3.1 ("space = inertia")
holds there because the Lagrangian is defined with (1/2) g(v,v). This note derives Phi from complete passivity
(PortPrinciple.md Thm 6.3), states the static FDT as the content of Thm 3.1, proves where it fails (the current),
credits the classical tower facts (Cencov, Amari-Nagaoka, Shima), and rebuilds the Bekenstein bound on
relative-entropy positivity (Casini; Bisognano-Wichmann). Supersedes the shared "Phi as effective action" claim
of T2 sec. 6, 01c sec. 7 and Paper 32 sec. 2 by deriving it (those papers now carry forward pointers).
Certificate: empirical/foundations54/p54_cert.py. Run 1 (blind) 19/21: K2d and K3d failed on CHECKER
ARTIFACTS (assumption-blind simplifier; nsimplify corrupting an exact rational -- same classes as P3.N2 and
P4.R10), retained in the run log; run 2 21/21. Excluded by design: RH, consciousness, cosmology.
Phase-2 propagation (same day): Paper 32, Paper 32.1, T2, 01c, README; ledgers in those files' internal logs.
Draft 2 (same day, Leo: "proceed a quantum (Lindblad) version of Thm 3"): added sec. 4.1 -- Theorem 3Q (static FDT
in each Petz metric f iff f-detailed balance), Prop 4.1 (kinetic jump tilt = SLD convention; free-energy tilt =
BKM convention; energy-generated Hamiltonian flow FDT-neutral only in BKM), Prop 4.2 (GNS => all f; KMS => neither
SLD nor BKM; KMS-dual of a Lindbladian is a Lindbladian), Cor 4.3 (kinetic - thermodynamic = quantum variance).
Certificate empirical/foundations54/p54q_lindblad_cert.py: run 1 blind 11/11; run 2 adds 2 post-run NOT-blind
cross-checks (true finite tilts of the non-equilibrium generators; the 3Q(b) bound): 13/13. Section numbers kept
(Papers 32/32.1 cite them).
Draft 3 (same day, Leo: "proceed with the frequency-resolved Harada-Sasa quantum version"): added sec. 4.2 --
Theorem 3H (quantum Agarwal formula; violation spectrum; sum rules: 1/omega moment = static defect, first moment summed
over a basis = ||A_f||_HS^2), Prop 4.4 (reductions: Harada-Sasa heat for Langevin coordinates; Kubo for energy-generated
Hamiltonian arrows in BKM; static), Prop 4.5 (frequency-wise positivity: second order, high frequency, commuting case),
Open Problem 4.6 (positivity in general). Certificate p54hs_harada_sasa_cert.py: runs 1-2 stopped (sympy blowup; no
verdict past H1), checker switched to exact evaluation with degree certificates; run 3 8/8 (H2-H6 blind). Exploratory
not-blind probe p54hs_explore_positivity.py: 4900 random cases, no counterexample.
Draft 4 (2026-10-02, Leo: "prove Open Problem 4.6"): PROVED.  Lemma 4.6 (arrow pencil): p(s) = det(i omega - M - sA)
is even, p = q(s^2), Delta_tot = 2 Sum Im u_r/|1 - u_r|^2 over the roots of q, and every root has Im u_r =
2 omega |v|^2 v*Mv / beta^2 >= 0.  Theorem 4.7: Delta_tot(omega) >= 0 for all omega > 0, every primitive Lindbladian,
every Petz metric (also finite Markov chains and linear dissipative systems).  Prop 4.5 retitled "explicit forms".
Certificate p54hs_op46_proof_cert.py: run 1 stopped (symbolic n=4 too heavy, no verdict); run 2 3/4 -- P4 FAILED on
spurious infinite generalized eigenvalues of a singular pencil (odd n), RETAINED; run 3 adds P4' post-diagnosis
(genuine eigenpairs only) -> 4/5.
-->

---

## Abstract

Paper 32 posits one functional, the log-partition $\Phi=\log Z$ of the categorical exponential family. This note derives it from the Port Principle's constraint — *no port gives more than it takes* — lifted to every number of copies. **(1)** Complete passivity forces the Gibbs state, so the free states over all Hamiltonians form the open simplex with natural parameter $\theta=-\beta H$, and $\Phi$ is their generating function: its gradient is the free state, its Legendre dual is $-S$, and its Fenchel–Young gap is the relative entropy $D(\rho\|p_\theta)$. **(2)** $\nabla^2\Phi$ is at once covariance (watching), response (pushing) and Fisher metric (distinguishing): the static fluctuation–dissipation theorem, which is the content of Paper 32's "space = inertia". Quantum mechanically the Hessian is Kubo–Mori and watching exceeds pushing by the quantum variance. **(3)** For a finite Markov chain the static response operator is $(L^*)^{-1}L_S$. Every term of its defect carries one factor of the stationary current; the defect vanishes, and the response matrix is symmetric (so that a generating potential exists at all), iff detailed balance holds; the currents span $b_1$ dimensions. Quantum mechanically (Lindblad) the same holds separately in every monotone metric: tilting the jump operators tests SLD-detailed balance, tilting the free energy tests Kubo–Mori-detailed balance, KMS-detailed balance guarantees neither, and at GNS-detailed balance the two pushes differ by exactly the quantum variance. Resolved in frequency, the first moment of the FDT violation, summed over a complete set of observables, equals the squared Hilbert–Schmidt norm of the arrow — a quantum Harada–Sasa equality that reduces to Harada–Sasa's heat for Langevin coordinates and to Kubo's theorem when the arrow is a Hamiltonian generated by the energy. At every positive frequency the total violation is nonnegative: a short determinant argument on the arrow pencil places every root of the relevant polynomial in the upper half-plane. **(4)** The third rung is the Amari–Chentsov tensor, and $R=\mathrm{AN}(T)$ is classical Hessian geometry (Shima). **(5)** The finite Bekenstein inequality is the same Fenchel–Young gap. Its isentropic face is passivity, its $\beta=0$ face is the capacity $\log Q$, and its continuum form is Casini's theorem, whose $2\pi$ is the Bisognano–Wichmann KMS inverse temperature. One functional, one inequality. An exact certificate (21 checks) verifies every finite claim; the two checker artifacts of its first run are retained.

---

## 1. What is derived, and from what

Paper 32 (Claim 2.1) calls $\Phi=\log Z$ "the categorical effective action" and starts from it. Its Theorem 3.1 ("space = inertia") holds because its Lagrangian is *defined* with the kinetic term $\tfrac12g(v,v)$. The Port Principle (PortPrinciple.md) contains what makes both derivable: under the copy lift the only free states are Gibbs states (its Theorem 6.3). This note writes the derivation once, so that T2 (§6), 01c (§7) and Paper 32 (§2–§3) cite it instead of restating the functional.

**Assumptions:** finite dimension $Q$; reference states passive under cyclic unitaries; energy additive over copies; in §4, a continuous-time Markov chain. No arithmetic structure on the outcomes is used. **Tiers:** [P] proven here (finite, exact, certified) or a cited theorem used as stated; [A] structural reading; [C] conjecture, fenced. Theorems 1–4, 3Q and 3H, Propositions 4.1–4.2 and 4.4–4.5, and Corollary 4.3 are [P]; Lemma 4.6 and Theorem 4.7 are [P]; Propositions 5.1–5.2 are [P, credited]; §7 is [A].

---

## 2. From the port constraint to $\Phi$

**Setting.** Fix a basis of a $Q$-level system and the Hamiltonians diagonal in it. Diagonal states are $p\in\Delta_Q$, faithful ones $p\in\Delta_Q^\circ$; the sufficient statistic is the one-hot vector $T(x)=e_x$. For $\theta\in\mathbb R^Q$,
$$p_\theta=e^{\theta}/Z(\theta),\qquad Z(\theta)=\textstyle\sum_xe^{\theta_x},\qquad \Phi(\theta)=\log Z(\theta),$$
with $p_{\theta+c\mathbf 1}=p_\theta$ and $\Phi(\theta+c\mathbf 1)=\Phi(\theta)+c$.

**Theorem 1 (the free states and their generating function) [P].**

- **(a)** A faithful state is completely passive for a Hamiltonian $H$ with at least two distinct levels iff it is $p_\theta$ with $\theta=-\beta H$, $\beta\ge0$. Every faithful $p$ is free for $H=-\log p$ at $\beta=1$ (the uniform $p$ for any $H$ at $\beta=0$), so the free states over all Hamiltonians are exactly $\Delta_Q^\circ$, and $\theta\mapsto p_\theta$ is a bijection $\mathbb R^Q/\mathbb R\mathbf 1\to\Delta_Q^\circ$. Only $\theta=-\beta H$ matters.
- **(b)** $\theta\mapsto p_\theta$ has a symmetric Jacobian, hence is a gradient; its potential is $\Phi=\log Z$, unique up to a constant. $\Phi=-\beta F$ is the Massieu function.
- **(c)** $\Phi$ is convex with Legendre dual $\Phi^*(p)=\sum_xp_x\log p_x=-S(p)$; equivalently $\Phi(\theta)=\max_p[\langle\theta,p\rangle+S(p)]$, uniquely attained at $p_\theta$ (the Gibbs variational principle).
- **(d)** For every state $\rho$, $\ \Phi(\theta)+\Phi^*(\rho)-\langle\theta,\rho\rangle=D(\rho\|p_\theta)\ge0$, with equality iff $\rho=p_\theta$. For $\theta=-\beta H$, $D/\beta=F(\rho)-F(p_\theta)$ is the maximal work a port can extract from $\rho$ with a bath at $\beta$ (Esposito–Van den Broeck 2011; Skrzypczyk–Short–Popescu 2014). Between free states, $D(p_\theta\|p_{\theta'})=\Phi(\theta')-\Phi(\theta)-\langle\nabla\Phi(\theta),\theta'-\theta\rangle$, the Bregman divergence of $\Phi$.
- **(e)** (a)–(d) hold verbatim quantum mechanically: $\theta=-\beta H$ Hermitian mod $\mathbf 1$, $\Phi=\log\operatorname{tr}e^\theta$, von Neumann $S$, Umegaki $D$; the free states are all faithful density matrices.

*Proof.* (a) is Port Theorem 6.3, the finite form of Pusz–Woronowicz (1978) and Lenard (1978); the inverse is $\theta=\log p\bmod\mathbf 1$. (b) $\partial p_x/\partial\theta_y=p_x\delta_{xy}-p_xp_y$ is symmetric and $\partial_x\log Z=p_x$. (c, d) Since $\log p_\theta=\theta-\Phi(\theta)\mathbf 1$, $\ \Phi(\theta)+\sum_x\rho_x\log\rho_x-\langle\theta,\rho\rangle=\sum_x\rho_x(\log\rho_x-\log p_\theta(x))=D(\rho\|p_\theta)$, which is $\ge0$ with equality iff $\rho=p_\theta$ (Gibbs' inequality); so $\sup_\rho[\langle\theta,\rho\rangle-\Phi^*(\rho)]=\Phi(\theta)$, attained only at $p_\theta$. With $\theta=-\beta H$ the same line is $\beta$ times the free-energy difference. The Bregman form is (d) at $\theta'$ applied to $\rho=p_\theta$, using equality at the Gibbs point. (e) $\frac{d}{dt}\operatorname{tr}e^{\theta+tX}|_0=\operatorname{tr}(e^\theta X)$ gives $\nabla\Phi=\sigma_\theta$, and the computation in (d) goes through with traces (Klein's inequality). Certificate K1, K2d–e, K5a. $\square$

*Reading.* Paper 32's Claim 2.1 attributes three properties to $\Phi$: its derivative is the source structure, its stationarity is the field equation, and it is one convex functional. Theorem 1 derives each: $\nabla\Phi$ is the free state; stationarity of $\langle\theta,p\rangle+S(p)$ is the Gibbs variational principle; convexity is passivity in Fenchel–Young form. **$\Phi$ is the generating function of the free states of the copy lift, and its Fenchel–Young gap is the work available against them.** Part (b) also says *why* a potential exists: the free state's response is reciprocal. Theorem 3(c) shows that this is exactly what fails away from equilibrium.

---

## 3. Static fluctuation–dissipation is the second rung

**Theorem 2 (watching = pushing = distinguishing) [P].** At every $\theta$,
$$\nabla^2\Phi=\operatorname{Cov}_{p_\theta}(T)=\frac{\partial\langle T\rangle_\theta}{\partial\theta}=\mathbb E_\theta\big[\partial\log p_\theta\otimes\partial\log p_\theta\big],\qquad(\nabla^2\Phi)_{xy}=p_x\delta_{xy}-p_xp_y ,$$
and $\frac{d}{d\varepsilon}\langle A\rangle_{\theta+\varepsilon V}|_0=\operatorname{Cov}_\theta(A,V)$ for all observables $A,V$. On a gauge slice ($\theta_Q=0$) the Hessian is positive *definite*, with leading minors $p_1\cdots p_k(1-p_1-\dots-p_k)$. On the redundant chart $\mathbb R^Q$ it is only positive *semidefinite*, of rank $Q-1$, with kernel $\mathbb R\mathbf 1$.

*Proof.* $\partial_yp_x=p_x(\delta_{xy}-p_y)=\operatorname{Cov}(T_x,T_y)$ and $\partial_y\log p_\theta(x)=\delta_{xy}-p_y$; the minors follow from the matrix determinant lemma. Certificate K2a–b. $\square$

**Watching** is the covariance, measured without disturbing. **Pushing** is the response of the mean to a change of $\theta=-\beta H$. **Distinguishing** is the Fisher metric, the unique monotone metric up to scale (Čencov 1972). Their coincidence is the static fluctuation–dissipation theorem, the zero-frequency case of Callen–Welton (1951) and Kubo (1957). In Souriau's thermodynamics (Souriau 1970; Koszul 1961; Barbaresco 2014) it says that the Hessian of the Massieu function is both a heat capacity and the Fisher metric; Paper 32 Remark 3.2 cites this twin.

**Proposition 2.1 (the quantum split) [P].** For $\Phi=\log\operatorname{tr}e^\theta$, Hermitian $X$, $\sigma=\sigma_\theta$ and $\tilde X=X-\langle X\rangle$,
$$\tfrac{d^2}{dt^2}\Phi(\theta+tX)\big|_0=\textstyle\int_0^1\operatorname{tr}\big(\sigma^s\tilde X\sigma^{1-s}\tilde X\big)\,ds,$$
the Kubo–Mori variance. It equals the isothermal response (pushing; Kubo's identity) and the BKM metric (distinguishing). The symmetrized variance (watching) exceeds it by the quantum variance — on each Bohr pair the filter $\coth x-1/x$ of Port Theorem 6.10 — and the two agree iff $[X,\theta]=0$. For $\theta=\operatorname{diag}(a,-a)$, $X=\begin{psmallmatrix}x&y\\y&z\end{psmallmatrix}$: Hessian $p_1p_2(x-z)^2+y^2\tanh a/a$, watching $p_1p_2(x-z)^2+y^2$ (certificate K2q, exact). $\square$

So quantum mechanically the three readings give two numbers. The gap exists inside the Gibbs state: it is the quantum variance (Frérot–Roscilde 2016), not an arrow. The monotone metric that is the Hessian of $\Phi$ is Kubo–Mori, not Bures (Petz 1996).

**Paper 32 Theorem 3.1, made explicit.** That theorem identifies metric with inertia because a kinetic term $\tfrac12g(v,v)$ is written down. The content is Theorem 2: the ruler, the fluctuations and the compliance are one tensor *in the free states*. Which tensor a Lagrangian carries is a modeling choice; the static FDT is a theorem, and leaving equilibrium tests it.

---

## 4. Where it fails: the arrow is the current

**Pre-registered falsifier** (fixed before the derivation and the certificate): *the response–covariance gap vanishes for all observables iff detailed balance holds.*

**Setting.** An irreducible continuous-time Markov chain on a finite set $X$ has rates $w_{xy}>0\Leftrightarrow w_{yx}>0$, generator $(Lf)_x=\sum_yw_{xy}(f_y-f_x)$ and stationary law $\pi$. Write $\langle f,g\rangle_\pi=\sum_x\pi_xf_xg_x$ and $\bar f=f-\langle f\rangle_\pi$. The time reversal is $L^*_{xy}=\pi_yL_{yx}/\pi_x$, and $L_S=\tfrac12(L+L^*)$, $L_A=\tfrac12(L-L^*)$. The current $J_{xy}=\pi_xw_{xy}-\pi_yw_{yx}$ is antisymmetric and divergence-free, and detailed balance $\Leftrightarrow J=0\Leftrightarrow L_A=0$. Perturb by a potential $V$ with an arbitrary symmetric kinetic factor $\sigma$:
$$w_{xy}(\varepsilon)=w_{xy}\exp\!\big(\varepsilon[\tfrac12(V_y-V_x)+\sigma_{xy}]\big).$$
At detailed balance this tilts $\pi$ to $\pi e^{\varepsilon V}/Z$ exactly, for every $\sigma$. Let $\chi(A)=\frac{d}{d\varepsilon}\langle A\rangle_{\pi(\varepsilon)}|_0$.

**Theorem 3 (static FDT out of equilibrium) [P].**

- **(a)** $\chi(A)=\langle\bar A,h\rangle_\pi$ with $h=\bar V+(L^*)^{-1}(L_A\bar V-k_\sigma)$ and $(k_\sigma)_x=\pi_x^{-1}\sum_y\sigma_{xy}J_{xy}$, the inverse taken on mean-zero functions.
- **(b)** Both terms of the defect $\chi(A)-\operatorname{Cov}_\pi(A,V)$ are linear in $J$, and its modulus is at most $\|\bar A\|_\pi(\|L_A\|_\pi\|\bar V\|_\pi+\|k_\sigma\|_\pi)/\lambda_S$, with $\lambda_S$ the spectral gap of $-L_S$.
- **(c)** $\chi(A)=\operatorname{Cov}_\pi(A,V)$ for all $A,V$ iff detailed balance holds. With $\sigma=0$, the response matrix $\partial\pi_x/\partial V_y$ is symmetric — equivalently, $V\mapsto\pi(V)$ is a gradient near $0$ — iff detailed balance holds.
- **(d)** With $I_V=\|h\|_\pi^2$ the Fisher information of the stationary family, $\chi(A)^2\le\operatorname{Var}_\pi(A)\,I_V$. At detailed balance $\operatorname{Var}_\pi(V)=\chi(V)=I_V$; with $\sigma=0$, equality $\chi(V)^2=\operatorname{Var}_\pi(V)I_V$ for all $V$ holds iff detailed balance holds.
- **(e)** $J$ lies in the cycle space of the transition graph, and every cycle is the current of some rates: the possible arrows form a space of dimension $b_1=|E|-|X|+1$. On a tree every chain is reversible and the static FDT is exact (Kolmogorov 1936).

*Proof.* (a) Differentiating $\pi L=0$ gives $\pi'L=-\pi L'$. With $\pi'=\pi\odot h$, $(\pi'L)_y=\pi_y(L^*h)_y$. In $(\pi L')_y=\sum_x[\pi_xw_{xy}a_{xy}-\pi_yw_{yx}a_{yx}]$, with exponent $a=\tfrac12\delta V+\sigma$, the antisymmetric half of $a$ pairs with the symmetric traffic and the symmetric half pairs with the current, so $\pi L'=\pi\odot(-L_SV+k_\sigma)$. Hence $L^*h=L_SV-k_\sigma=L^*\bar V+L_A\bar V-k_\sigma$, since $L^*=L_S-L_A$ and $L_S\mathbf 1=0$. Here $L^*$ is invertible on mean-zero functions, and $\langle h\rangle_\pi=0$.

(b) For mean-zero $u=(L^*)^{-1}f$, $\langle u,-L^*u\rangle_\pi=\langle u,-L_Su\rangle_\pi\ge\lambda_S\|u\|^2$, because an antisymmetric operator has zero quadratic form; so $\|u\|\le\|f\|/\lambda_S$.

(c) $J=0$ gives $L_A=0=k_\sigma$ and $h=\bar V$. Conversely, $h=\bar V$ for all $V$ forces $L_A\bar V=k_\sigma$ for all $V$; $V=0$ gives $k_\sigma=0$, hence $L_A=0$ and $J=0$. With $\sigma=0$, $\partial\pi_x/\partial V_y=\langle\bar e_x,R\bar e_y\rangle_\pi$ with $R=(L^*)^{-1}L_S$. Symmetry means $R$ is self-adjoint in $L^2(\pi)$, i.e. $L_SL_A=-L_AL_S$. Then $L_A$ maps the $\mu$-eigenspace of $L_S$ into its $(-\mu)$-eigenspace, and $L_S$ is negative definite on mean-zero functions, so $L_A=0$.

(d) Cauchy–Schwarz. Equality for all $V$ forces $R=\lambda I$, so $(1-\lambda)L_S=-\lambda L_A$; its symmetric and antisymmetric parts give $\lambda=1$ and $L_A=0$.

(e) $\sum_yJ_{xy}=0$ is stationarity. Conversely, a cycle $J$ is realized with $\pi$ uniform by $w_{xy}=|X|(s_{xy}+\tfrac12J_{xy})$, for symmetric $s_{xy}>\tfrac12|J_{xy}|$. Certificate K3. $\square$

**Example (the driven 3-cycle; closed form pre-registered).** Take rate $a$ forward and $b$ backward, so $\pi$ is uniform. With $(Sf)_x=f_{x+1}$, $\tau^2=\frac{(a-b)^2}{3(a+b)^2}$ and $\sigma=0$,
$$h=\frac{\bar V-\frac{a-b}{3(a+b)}(S-S^{-1})\bar V}{1+\tau^2},\qquad\frac{\chi(V)}{\operatorname{Var}(V)}=\frac{3(a+b)^2}{3(a+b)^2+(a-b)^2}\ \ \text{for every non-constant }V,$$
which is $27/28$, $12/13$ and $49/52$ at $(a,b)=(2,1),(3,1),(5,2)$. The rotation term, linear in $a-b$, makes the response matrix partly antisymmetric, so no potential generates this steady state. On a generic four-state steady state, $\operatorname{Var}(V)$, $\chi(V)$ and $I_V$ are three different numbers (certificate K3e).

*Reading.* This is Port Principle §10 — the arrow is the gap between watching and pushing — made static and exact. Watching is $\operatorname{Var}$, pushing is $\chi$, distinguishing is $I$. The copy lift makes them one number (Theorem 2); away from equilibrium the stationary current separates them, at first order in $J$, and nothing else does. By (c), a potential for the static response exists only at detailed balance: **the one functional is an equilibrium object.** Part (e) is the Markov form of the program's "arrow dimension $=b_1$" (forward3_reversibility.md).

*Credit.* The operator form is elementary. Nonequilibrium response formulas for Markov processes go back to Agarwal (1972); the entropic/frenetic split (here the $L_A$ and $k_\sigma$ terms) is due to Baiesi–Maes–Wynants (2009); steady-state FDTs appear in Prost–Joanny–Parrondo (2009) and Seifert–Speck (2010). The frequency-resolved, dissipative version is Harada–Sasa (2005), and (d) is the static, linear-order form of the fluctuation–response inequality of Dechant–Sasa (2020).

### 4.1 The quantum arrow (Lindblad)

Quantum mechanically, "multiplying by $\pi$" is ambiguous: a density matrix can be paired with an observable in many ways. This is the monotone-metric fork of Proposition 2.1, now inside the dynamics.

**Setting.** $\mathcal L$ is a Lindbladian on $M_d(\mathbb C)$, $\mathcal L^\dagger$ its Heisenberg generator, and $\sigma$ its unique faithful stationary state; the semigroup is primitive (every nonzero eigenvalue has negative real part). For a Petz function $f$ (operator monotone, $f(1)=1$, $f(t)=tf(1/t)$), $\Gamma_f=R_\sigma f(L_\sigma R_\sigma^{-1})$ is the corresponding multiplication by $\sigma$: $\Gamma_{\rm SLD}(X)=\tfrac12\{\sigma,X\}$, $\Gamma_{\rm KMS}(X)=\sigma^{1/2}X\sigma^{1/2}$, $\Gamma_{\rm BKM}(X)=\int_0^1\sigma^sX\sigma^{1-s}ds$. Put $\langle X,Y\rangle_f=\operatorname{tr}(X^\dagger\Gamma_fY)$, the $f$-time reversal $\tilde{\mathcal L}_f=\Gamma_f^{-1}\mathcal L\Gamma_f$ (the $\langle\cdot,\cdot\rangle_f$-adjoint of $\mathcal L^\dagger$), $\mathcal S_f=\tfrac12(\mathcal L^\dagger+\tilde{\mathcal L}_f)$ and $\mathcal A_f=\tfrac12(\mathcal L^\dagger-\tilde{\mathcal L}_f)$. **$f$-detailed balance** means $\mathcal A_f=0$. A perturbation $\mathcal L_\varepsilon$ acts through its source $\mathcal L'(\sigma)$. It is an **$f$-potential perturbation by $V$** if $\mathcal L'(\sigma)=-\Gamma_f(\mathcal S_fV)$: the dissipation sees the tilted potential, and the antisymmetric dynamics does not. Classically every $f$ gives the same object, the $\theta=\tfrac12$ rate tilt of Theorem 3.

**Theorem 3Q (the static FDT in a quantum steady state) [P].** For an $f$-potential perturbation, with $\chi(A)=\frac{d}{d\varepsilon}\operatorname{tr}(A\sigma_\varepsilon)|_0$:

- **(a)** $\chi(A)=\langle A,h\rangle_f$, i.e. $\sigma'=\Gamma_f(h)$, with $h=\bar V+\tilde{\mathcal L}_f^{-1}\mathcal A_f\bar V$, $\bar V=V-\operatorname{tr}(\sigma V)$, the inverse taken on $f$-mean-zero observables.
- **(b)** $|\chi(A)-\langle A,\bar V\rangle_f|\le\|\bar A\|_f\|\mathcal A_f\|_f\|\bar V\|_f/\lambda_f$ whenever the gap $\lambda_f$ of $-\mathcal S_f$ on $\mathbf 1^\perp$ is positive. Unlike the classical case, $\lambda_f$ can vanish for a primitive $\mathcal L$ (hypocoercive generators); (a), (c), (d) still hold.
- **(c)** $\chi(A)=\langle A,\bar V\rangle_f$ for all $A,V$ $\iff$ $f$-detailed balance $\iff$ the $f$-response matrix is symmetric.
- **(d)** $\chi(A)^2\le\langle\bar A,\bar A\rangle_f\,I_f(V)$, where $I_f=\langle h,h\rangle_f$ is the $f$-Fisher information of the stationary family; equality for all $V$ $\iff$ $f$-detailed balance.

*Proof.* The proof of Theorem 3 runs verbatim in the Hilbert space $(M_d,\langle\cdot,\cdot\rangle_f)$, with $\pi\odot h$ replaced by $\Gamma_f(h)$. Two inputs are quantum. First, $\mathcal S_f\le0$: $e^{t\mathcal L}$ fixes $\sigma$ and contracts every monotone metric (Petz 1996), so $e^{t\tilde{\mathcal L}_f}$ is an $f$-contraction. Second, in (c) and (d) primitivity replaces irreducibility. If $\mathcal S_f\mathcal A_f+\mathcal A_f\mathcal S_f=0$, then $\mathcal A_f$ maps the $\mu$-eigenspace of $\mathcal S_f$ into the $(-\mu)$-eigenspace, so it vanishes off $\ker\mathcal S_f$ and is antisymmetric on it. There $\mathcal L^\dagger$ would have purely imaginary eigenvalues, which primitivity excludes unless $\mathcal A_f=0$. Certificate K6a, K6d, K6g, K6h. $\square$

So far this is the classical theorem with an index $f$. Its content is *which* $f$ a given push tests.

**Proposition 4.1 (two pushes, two metrics) [P].**

- **(i) Kinetic push.** Tilt the jump operators, $L_j\mapsto e^{\varepsilon V/4}L_je^{-\varepsilon V/4}$, conjugate the effective Hamiltonian alike, and restore unitality symmetrically:
$$\mathcal L^\dagger_\varepsilon=\mathcal K_\varepsilon^{-1}\mathcal L^\dagger\mathcal K_\varepsilon-\tfrac12\{(\mathcal K_\varepsilon^{-1}\mathcal L^\dagger\mathcal K_\varepsilon)(\mathbf 1),\cdot\},\qquad\mathcal K_\varepsilon(X)=e^{\varepsilon V/4}Xe^{\varepsilon V/4}.$$
  This is a Lindbladian for every $\varepsilon$. Its first-order term is the Jordan carré du champ $\tfrac12[\mathcal L^\dagger(V\circ X)-V\circ\mathcal L^\dagger X-X\circ\mathcal L^\dagger V]$, it reduces to the classical $\theta=\tfrac12$ rate tilt, and its source is $-\Gamma_{\rm SLD}(\mathcal S_{\rm SLD}V)$. **The kinetic push is the SLD potential perturbation, for every $\mathcal L$.**
- **(ii) Free-energy push.** Suppose $\mathcal L$ is a gradient flow of the relative entropy, $\dot\rho=-K_\rho(\log\rho-\log\sigma)$ with $K_\rho$ symmetric and positive. Then $\mathcal L$ is BKM-symmetric, and tilting the free energy, $D(\rho\|\sigma)\to D(\rho\|\sigma)-\varepsilon\operatorname{tr}(\rho V)$ at fixed $K$, is the BKM potential perturbation. At BKM-detailed balance its response is the Gibbs tilt, $\sigma'=\frac{d}{d\varepsilon}e^{\log\sigma+\varepsilon V}/Z=\Gamma_{\rm BKM}(\bar V)$: $\chi$ is the Kubo–Mori covariance, the Hessian of $\Phi$ (Proposition 2.1).
- **(iii) Reversible part.** A Hamiltonian term $i[H_0,\cdot]$ with $[H_0,\sigma]=0$ is antisymmetric in every metric, so it belongs to $\mathcal A_f$. Suppose it is generated by the energy, $\sigma=e^{-\beta H_0}/Z$, and the push shifts it with the potential ($H_0\to H_0-V/\beta$). Then its contribution cancels exactly in the BKM metric and in no other, because $\Gamma_f^{-1}([V,\sigma])=[V,\log\sigma]$ for all $V$ iff $(1-t)/f(t)=-\log t$, i.e. $f=f_{\rm BKM}$.

*Proof.*

(i) $\mathcal K_\varepsilon^{-1}\mathcal L^\dagger\mathcal K_\varepsilon$ has the form $X\mapsto\sum_j\tilde L_j^\dagger X\tilde L_j-\tilde GX-X\tilde G^\dagger$, and subtracting the symmetric correction makes it unital, hence a Lindblad generator. Differentiating at $0$ gives the carré du champ. Pairing it with $\sigma$ and using $\operatorname{tr}(\sigma(V\circ Y))=\operatorname{tr}(\Gamma_{\rm SLD}(V)Y)$ gives $\operatorname{tr}(X\mathcal L'(\sigma))=-\tfrac12(\langle\mathcal L^\dagger X,V\rangle_{\rm SLD}+\langle X,\mathcal L^\dagger V\rangle_{\rm SLD})=-\langle X,\mathcal S_{\rm SLD}V\rangle_{\rm SLD}$.

(ii) At $\sigma$, $d\log\rho=\Gamma_{\rm BKM}^{-1}d\rho$, so the linearized flow is $\mathcal L=-K_\sigma\Gamma_{\rm BKM}^{-1}$. Hence $\tilde{\mathcal L}_{\rm BKM}=-\Gamma_{\rm BKM}^{-1}K_\sigma$, which is BKM-symmetric. The source of the tilt is $K_\sigma\bar V=-\Gamma_{\rm BKM}\mathcal S_{\rm BKM}\bar V$, and Duhamel's formula gives $\frac{d}{d\varepsilon}e^{\log\sigma+\varepsilon V}=\Gamma_{\rm BKM}(V)$. Carlen–Maas (2017) construct such gradient flows under GNS-detailed balance.

(iii) In the eigenbasis of $\sigma$, $\Gamma_f^{-1}[V,\sigma]$ has entries $V_{ij}(p_j-p_i)/(p_jf(p_i/p_j))$, and $[V,\log\sigma]$ has entries $V_{ij}(\log p_j-\log p_i)$. The shift contributes the source $\tfrac i\beta[V,\sigma]$, so the $f$-equation for $h$ reduces to $\tilde{\mathcal L}_fh=\tilde{\mathcal L}_f\bar V$ exactly when these entries agree.

Certificate K6b, K6e, K6f. $\square$

**Proposition 4.2 (quantum detailed balance is not one condition) [P].**

- *GNS-detailed balance* ($\mathcal L^\dagger$ self-adjoint for $\operatorname{tr}(\sigma X^\dagger Y)$) forces $\mathcal L^\dagger$ to commute with the modular operator (Alicki 1976; see Carlen–Maas 2017), hence $f$-detailed balance for every Petz $f$. Under it both pushes obey their FDTs at once.
- *KMS-detailed balance* (Fagnola–Umanità 2007; Carlen–Maas 2017) is $f$-detailed balance for $f(t)=\sqrt t$ only. It implies neither the SLD nor the BKM condition.
- For any Lindbladian $\mathcal L$ with stationary $\sigma$, the KMS dual $\sigma^{-1/2}\mathcal L(\sigma^{1/2}\cdot\sigma^{1/2})\sigma^{-1/2}$ is again a Lindbladian (conditionally completely positive and unital), so $\tfrac12(\mathcal L^\dagger+\tilde{\mathcal L}_{\rm KMS})$ has KMS-detailed balance.
- Certificate K6c builds such a generator from a qubit steady state with population–coherence mixing. Its $\sqrt t$-FDT holds exactly, while the kinetic (SLD) and free-energy (BKM) FDTs both fail. By Proposition 4.1(ii) it is not a gradient flow of relative entropy for any metric.

**Corollary 4.3 (the quantum variance is the gap between the two pushes) [P].** At GNS-detailed balance the kinetic push moves $\sigma$ along $\tfrac12\{\sigma,\bar V\}$ and the free-energy push along $\Gamma_{\rm BKM}(\bar V)$. Their responses differ by $\chi_{\rm kin}(A)-\chi_{\rm th}(A)=\langle A,\bar V\rangle_{\rm SLD}-\langle A,\bar V\rangle_{\rm BKM}$. For $A=V$ this is the quantum variance of Proposition 2.1,
$$\sum_{p_i>p_j}|V_{ij}|^2(p_i-p_j)\Big(\coth x_{ij}-\frac1{x_{ij}}\Big),\qquad x_{ij}=\tfrac12\log\frac{p_i}{p_j},$$
which vanishes iff $[V,\sigma]=0$. For $\sigma=\operatorname{diag}(4,1)/5$ and $V=\sigma_x$ it equals $1-3/(5\log2)$ (certificate K6e, exact). In a witness, the true Gibbs tilt and the true finite jump tilt reproduce both directions to 60 digits.

*Reading.* Quantum mechanically, the watch–push structure of Theorem 2 splits along the monotone-metric family, and so does the arrow. The quantum arrow is $\mathcal A_f$, and *which* $f$ is decided by how one pushes. Tilting the kinetics tests SLD-detailed balance. Tilting the energy tests BKM-detailed balance — the metric that is the Hessian of $\Phi$, that relative-entropy gradient flows require, and in which the energy's own Hamiltonian flow is FDT-neutral. At GNS-detailed balance everything holds, and the two pushes differ only by the quantum variance: a quantum effect inside the Gibbs state, not an arrow. $\mathcal A_f$ collects every time-reversal-odd part of the generator. That includes irreversible currents, which produce entropy, and reversible Hamiltonian parts not generated by the energy, which do not (the Onsager–Casimir case).

*Credit.* Quantum detailed balance and its inequivalent forms: Agarwal (1973), Alicki (1976), Kossakowski–Frigerio–Gorini–Verri (1977), Fagnola–Umanità (2007), Temme–Kastoryano–Ruskai–Wolf–Verstraete (2010), Carlen–Maas (2017). As far as we found, the $f$-indexed equivalence and the two-push dictionary are new as stated.

### 4.2 The frequency-resolved arrow: a quantum Harada–Sasa equality

Theorem 3Q is static. Driving the same push with a time-dependent amplitude $h(t)$ resolves it in time and frequency. That is where Harada and Sasa located dissipation for Langevin systems (Port Principle, Theorem 10.1).

**Setting.** Keep the notation of §4.1 and apply an $f$-potential push with amplitude $h(t)$. At linear order only the source enters: $\delta\langle A\rangle(t)=\int R_{AV}(t-s)h(s)\,ds$ with $R_{AV}(\tau)=\operatorname{tr}(Ae^{\tau\mathcal L}\mathcal L'(\sigma))$ for $\tau>0$. The $f$-correlation is $C^f_{AB}(\tau)=\langle e^{\tau\mathcal L^\dagger}\bar A,\bar B\rangle_f$ for $\tau\ge0$, extended evenly when $A=B$. By the quantum regression theorem, $f=$ SLD gives the symmetrized two-time correlation $\tfrac12\langle\{A(\tau),B\}\rangle$, and $f=$ BKM gives Kubo's canonical correlation. For $A=V$ let $\tilde C^f_V(\omega)$ be the spectrum, $\tilde R''_V(\omega)$ the dissipative part of the response, and
$$\Delta_V(\omega)=\tfrac{\omega}{2}\tilde C^f_V(\omega)-\tilde R''_V(\omega)$$
the violation spectrum; the dynamic $f$-FDT is $\Delta_V\equiv0$. Let $\Delta_{\rm tot}$ be its sum over an $f$-orthonormal basis of $W$, the $f$-mean-zero Hermitian observables.

**Theorem 3H (a quantum Harada–Sasa equality) [P].**

- **(a) Time domain.** $R_{AV}(\tau)=-\frac{d}{d\tau}C^f_{AV}(\tau)-C^f_{A,\mathcal A_fV}(\tau)$. The response is the slope of the watched correlation plus the correlation of $A(\tau)$ with the current observable $\mathcal A_f\bar V$.
- **(b) Spectrum.** $\Delta_V(\omega)=\int_0^\infty\sin(\omega\tau)\,C^f_{V,\mathcal A_fV}(\tau)\,d\tau=-\operatorname{Im}\langle\bar V,(i\omega+\tilde{\mathcal L}_f)^{-1}\mathcal A_f\bar V\rangle_f$. In total, $\Delta_{\rm tot}(\omega)=-\operatorname{Im}\operatorname{Tr}_W[(i\omega+\tilde{\mathcal L}_f)^{-1}\mathcal A_f]=\omega\operatorname{Tr}_W[(\tilde{\mathcal L}_f^2+\omega^2)^{-1}\mathcal A_f]$.
- **(c) Sum rules.** $\frac1\pi\int\Delta_V\frac{d\omega}{\omega}=\operatorname{Var}_f(V)-\chi_{VV}$, the static defect of Theorem 3Q. $\frac1\pi\int\omega\Delta_V\,d\omega=\langle\mathcal L^\dagger\bar V,\mathcal A_f\bar V\rangle_f$. Summed over a basis,
$$\frac1\pi\int_{-\infty}^{\infty}\omega\,\Delta_{\rm tot}(\omega)\,d\omega=\|\mathcal A_f\|_{\rm HS}^2:$$
**the first moment of the total FDT violation is the squared Hilbert–Schmidt norm of the arrow.**
- **(d)** $\Delta_{\rm tot}\equiv0$ iff $f$-detailed balance holds. Per observable, the moments can take either sign; only the total is sign-definite.

*Proof.*

(a) Since $e^{\tau\mathcal L}\Gamma_f=\Gamma_fe^{\tau\tilde{\mathcal L}_f}$, $R(\tau)=-\langle e^{\tau\mathcal L^\dagger}\bar A,\mathcal S_f\bar V\rangle_f$, while $\dot C=\langle e^{\tau\mathcal L^\dagger}\bar A,(\mathcal S_f-\mathcal A_f)\bar V\rangle_f$.

(b) Take $A=V$ and Fourier-transform. Here $g(\tau):=C^f_{V,\mathcal A_fV}(\tau)$ is real, with $g(0)=\langle\bar V,\mathcal A_f\bar V\rangle_f=0$. For the last form, $\tilde{\mathcal L}_f$ is real on $W$, so $(i\omega+\tilde{\mathcal L}_f)^{-1}=(\tilde{\mathcal L}_f-i\omega)(\tilde{\mathcal L}_f^2+\omega^2)^{-1}$.

(c) $\int\sin(\omega\tau)\,d\omega/\omega=\pi$ gives $\int_0^\infty g=-\langle\bar V,\tilde{\mathcal L}_f^{-1}\mathcal A_f\bar V\rangle_f$, which Theorem 3Q(a) identifies. Integrating by parts, $\omega\Delta_V=\int_0^\infty\cos(\omega\tau)g'(\tau)\,d\tau$, whose integral is $\pi g'(0)=\pi\langle\mathcal L^\dagger\bar V,\mathcal A_f\bar V\rangle_f$. In an orthonormal basis the sum is $\operatorname{Tr}(\mathcal A_f^*\mathcal L^\dagger)=\operatorname{Tr}(\mathcal A_f^*\mathcal S_f)+\|\mathcal A_f\|^2_{\rm HS}$, and the trace of an antisymmetric times a symmetric operator vanishes.

(d) follows from (c).

Certificate H1–H3: exact, with the frequency integrals checked by 30-digit quadrature. $\square$

**Proposition 4.4 (three reductions) [P].**

- *Harada–Sasa.* Take overdamped Langevin dynamics $dx=F\,dt+\sqrt{2T}\,dW$ ($\gamma=1$) with the coordinates as observables. Then $\mathcal A x_i=\nu_i$ is the local mean velocity (Speck–Seifert 2006). The first moments sum to $E[F\cdot\nu]=E|\nu|^2$, because $E[\nabla\log\pi\cdot\nu]=-\int\log\pi\,\nabla\!\cdot(\pi\nu)=0$ at stationarity; this is the Harada–Sasa heat rate, without the mean-drift term. The individual cross terms $\langle\mathcal Sx_i,\mathcal Ax_i\rangle$ need not vanish; only their sum does. Certificate H4 checks a non-normal linear example (cross terms $\pm\tfrac4{25}$, total $\tfrac{16}3=E|\nu|^2$) and the circulating example of Port Principle P1.C3 ($2\varepsilon^2kT$).
- *Kubo.* Suppose the antisymmetric part is a Hamiltonian generated by the energy, and the push shifts it (Proposition 4.1(iii)). Then the violation term vanishes in the BKM metric, and $R=-\frac{d}{d\tau}C^{\rm Kubo}$: Kubo's classical-form FDT in the canonical correlation, now for an open system. In every other metric the same push violates (certificate H5).
- *Static.* The $1/\omega$ moment is Theorem 3Q.

**Proposition 4.5 (explicit forms) [P].** In three regimes $\Delta_{\rm tot}$ has an explicit, manifestly positive form; Theorem 4.7 below covers the general case:

- to second order in $\mathcal A_f$, where $\Delta_{\rm tot}(\omega)=\sum_{ab}(\mathcal A_f)_{ab}^2\,\omega(\lambda_a+\lambda_b)/((\omega^2+\lambda_a^2)(\omega^2+\lambda_b^2))$, with $-\lambda_a$ the eigenvalues of $\mathcal S_f$ on $W$;
- at high frequency to all orders, $\Delta_{\rm tot}(\omega)=2\omega^{-3}\operatorname{Tr}[(-\mathcal S_f)\mathcal A_f^*\mathcal A_f]+O(\omega^{-5})$;
- at any arrow strength when $\mathcal S_f$ and $\mathcal A_f$ commute (for example, a uniformly driven cycle), where a joint mode with $\mathcal S_f=-\lambda$ and $\mathcal A_f=\pm i\alpha$ contributes $4\omega\lambda\alpha^2/|(\lambda+i\alpha)^2+\omega^2|^2$.

*Proof.*

- Expand $(\tilde{\mathcal L}_f^2+\omega^2)^{-1}$ to first order in $\mathcal A_f$; the zeroth-order trace vanishes (symmetric times antisymmetric).
- Expand in $1/\omega$, using $\operatorname{Tr}(\tilde{\mathcal L}_f^2\mathcal A_f)=-2\operatorname{Tr}(\mathcal S_f\mathcal A_f^2)$ and the fact that both $-\mathcal S_f$ and $-\mathcal A_f^2$ are positive semidefinite.
- In the commuting case, diagonalize jointly.

Certificate H6 checks finite-arrow positivity on all seven non-equilibrium test cells: five exactly, by Sturm counts, and two by 30-digit scans. $\square$

**Lemma 4.6 (the arrow pencil) [P].** Let $P=-M-A$ be real, with $M=M^{\mathsf T}\succeq0$ and $A^{\mathsf T}=-A$. Let $\omega>0$ with $P+i\omega$ invertible, and put $p(s)=\det(i\omega-M-sA)$. Then $p$ is even, $p(s)=q(s^2)$, and
$$-\operatorname{Im}\operatorname{Tr}[(P+i\omega)^{-1}A]=\omega\operatorname{Tr}[(P^2+\omega^2)^{-1}A]=2\sum_r\frac{\operatorname{Im}u_r}{|1-u_r|^2}\ \ge0,$$
where $u_r$ runs over the roots of $q$ with multiplicity, and each root satisfies $\operatorname{Im}u_r\ge0$.

*Proof.*

- **Evenness.** $X=i\omega-M$ is complex symmetric, so $p(s)=\det((X-sA)^{\mathsf T})=\det(X+sA)=p(-s)$.
- **The root formula.** Jacobi's formula gives $\operatorname{Tr}[(X-A)^{-1}A]=-p'(1)/p(1)=-2q'(1)/q(1)=-2\sum_r(1-u_r)^{-1}$; both sides vanish if $q$ is constant. Since $X-A=P+i\omega$, taking $-\operatorname{Im}$ gives the formula, because $\operatorname{Im}\frac1{1-u}=\operatorname{Im}u/|1-u|^2$.
- **Each root lies in the closed upper half-plane.** For a root $u_r$ choose $s$ with $s^2=u_r$ and $v\ne0$ with $Xv=sAv$. Then $i\omega|v|^2-v^*Mv=s\,v^*Av$. Here $v^*Av=i\beta$ is purely imaginary, since $A$ is real antisymmetric, and $\beta\ne0$, since $\omega|v|^2>0$. Hence $s=(\omega|v|^2+i\,v^*Mv)/\beta$, and $\operatorname{Im}u_r=2\omega|v|^2\,v^*Mv/\beta^2\ge0$. $\square$

**Theorem 4.7 (the total FDT violation is nonnegative at every positive frequency) [P].**

- For every primitive Lindbladian and every Petz metric $f$, $\Delta_{\rm tot}(\omega)\ge0$ for all $\omega>0$.
- If $\mathcal A_f\ne0$, it vanishes at only finitely many frequencies; if $\mathcal A_f=0$, it vanishes identically.
- The same holds for every irreducible finite Markov chain and every linear dissipative system.
- Equivalently, at every frequency the total watched spectrum dominates the total pushed absorption: $\sum_k[\tfrac\omega2\tilde C^f_{B_k}(\omega)-\tilde R''_{B_k}(\omega)]\ge0$ over any $f$-orthonormal basis of $W$.

*Proof.* In an $f$-orthonormal real basis of $W$, $\tilde{\mathcal L}_f=\mathcal S_f-\mathcal A_f$, with $\mathcal S_f\preceq0$ (Petz monotonicity, §4.1) and $\mathcal A_f$ antisymmetric. Primitivity makes $\tilde{\mathcal L}_f+i\omega$ invertible. Then Theorem 3H(b) and Lemma 4.6, with $M=-\mathcal S_f$ and $A=\mathcal A_f$, give $\Delta_{\rm tot}(\omega)\ge0$. $\Delta_{\rm tot}$ is rational in $\omega$, and by Theorem 3H(c) its first moment is $\|\mathcal A_f\|^2_{\rm HS}$. So if $\mathcal A_f\ne0$ it is not identically zero, and its zeros are finite in number. $\square$

The question was first posed as an open problem. Before the proof was found, an exploratory probe found no counterexample in 4,900 random cases (`p54hs_explore_positivity.py`).

The certificate checks each step (`p54hs_op46_proof_cert.py`):

- for $n=2,3$ the closed form; at $n=4$ a Pfaffian term enters, yet the lemma still holds;
- evenness and the Jacobi step, exactly, on all seven Lindblad cells;
- every root in the upper half-plane, at 50 digits.

Its pre-registered random-matrix check failed on three spurious infinite eigenvalues of a singular pencil. That failure is retained, and the post-diagnosis check passes on the same 1,980 matrices.

*Reading.* Harada and Sasa measured dissipation as the first moment of the FDT violation. In a finite system, classical or quantum, the exact statement is that this first moment, summed over a complete set of observables, is the squared Hilbert–Schmidt norm of the arrow. That number is basis-free and vanishes exactly at $f$-detailed balance. For Langevin coordinates it is the heat rate. For a jump process it is not the entropy production, which is not a quadratic form in $\mathcal A_f$. Frequency by frequency, the violation is the sine transform of the correlation between an observable and its own current. At equilibrium the push and the watch agree at every frequency. Out of equilibrium the arrow appears at the relaxation frequencies of $\tilde{\mathcal L}_f$, and with a positive sign at every one (Theorem 4.7).

*Credit.* Harada–Sasa (2005, 2006) for the equality in Langevin systems; Speck–Seifert (2006) for the local mean velocity; Agarwal (1972) for the response as a correlation; Kubo (1957) for the canonical correlation.

---

## 5. The next rungs, with provenance

**Proposition 5.1 (the third rung) [P, credited].** $\nabla^n\Phi$ is the $n$-th joint cumulant of $T$. At $n=3$ it equals the Amari–Chentsov tensor $\mathbb E[\partial\ell\otimes\partial\ell\otimes\partial\ell]$, $\ell=\log p_\theta$ (Čencov 1972; Amari 1985). Certificate K2c.

**Proposition 5.2 (curvature is quadratic in the cubic) [P, credited].** For a Hessian metric $g=\nabla^2\Phi$ in an affine chart, $\Gamma_{ij,k}=\tfrac12T_{ijk}$ and
$$R_{ijkl}=\tfrac14\,g^{pq}\big(T_{ilp}T_{jkq}-T_{ikp}T_{jlq}\big)=:\mathrm{AN}(T)_{ijkl},$$
i.e. $R(X,Y)=-[\gamma_X,\gamma_Y]$ with difference tensor $\gamma=\tfrac12g^{-1}T$ (Shima 2007, Ch. 2; Amari–Nagaoka 2000). For the categorical family, moreover, $\mathrm{AN}(T)=\tfrac14(g_{ik}g_{jl}-g_{il}g_{jk})$ everywhere. Through $p\mapsto2\sqrt p$ the Fisher geometry is a sector of the round sphere of radius $2$, with Fisher–Rao distance $2\arccos\sum_x\sqrt{p_xq_x}$ and diameter $\pi$ (Čencov; Atkinson–Mitchell 1981; Amari–Nagaoka 2000), and maximal entropy $\log Q$ at the centroid.

*Proof.* The fourth-derivative terms of $R$ cancel, and $\partial g^{-1}=-g^{-1}Tg^{-1}$ leaves the quadratic term. Certificate K4 checks $Q=3,4,5$, at and off the centroid, by two independent routes: the mixture-chart routine of `empirical/phiF_curvature_reverify.py`, reused verbatim, and a natural-chart computation from the fourth cumulant. $\square$

*Provenance.* Paper 32 Remark 16.2b presents $R=\mathrm{AN}(T)$ "at and off the centroid" as a finding. It holds for every Hessian metric at every point and is classical; the program contributes the exact certificate. The Hellinger sphere, its diameter and the capacity $\log Q$ (Paper 32.1, Theorems 3.1, 4.1–4.2) are classical too.

**The tower is the expansion of the one inequality.** By Theorem 1(d),
$$D(p_\theta\|p_{\theta+\delta})=\Phi(\theta+\delta)-\Phi(\theta)-\langle\nabla\Phi(\theta),\delta\rangle=\textstyle\sum_{n\ge2}\frac1{n!}\nabla^n\Phi(\theta)[\delta^{\otimes n}].$$
The first-order term cancels (a "first law"); rung 2 is Fisher, rung 3 Amari–Chentsov, rung 4 the program's "jerk". The cumulant tower is the Taylor expansion of the Fenchel–Young gap (certificate K2e).

---

## 6. Bekenstein from passivity

**Theorem 4 (the finite Bekenstein inequality is passivity of a KMS state) [P].** Let $\sigma=e^{-\beta H}/Z$ be a faithful Gibbs state, $\beta\ge0$. For every state $\rho$,
$$S(\rho)-S(\sigma)\ \le\ \beta\big(\langle H\rangle_\rho-\langle H\rangle_\sigma\big),$$
with equality iff $\rho=\sigma$. The defect is exactly $D(\rho\|\sigma)$, the Fenchel–Young gap of Theorem 1(d). Three faces:

- **(i) isentropic** ($\rho=U\sigma U^\dagger$): $0\le\beta W$, passivity of $\sigma$ (Port Corollary 6.13);
- **(ii) $\beta=0$** ($\sigma=\mathbf 1/Q$): $S(\rho)\le\log Q$, the capacity of Paper 32.1 Theorem 4.1;
- **(iii) bath** ($\sigma$ a bath's Gibbs state, $\rho$ its state after an interaction): $\Delta S_B\le\beta Q_B$, the bath half of the sharp Landauer identity $\beta Q=\Delta S_{\rm sys}+I+D$ (Port Proposition 8.5(a); Reeb–Wolf 2014).

*Proof.* $D(\rho\|\sigma)=-S(\rho)+\beta\langle H\rangle_\rho+\log Z$ and $S(\sigma)=\beta\langle H\rangle_\sigma+\log Z$; Klein's inequality. Certificate K5: symbolic identity; exact signs on 44 classical and 8 quantum rational pairs, via $e^{ND}$ compared with $1$; equality exactly at $\rho=\sigma$; faces (i) and (ii) on disjoint instance sets. $\square$

**The continuum form [P, cited].** For a region of a quantum field theory with vacuum-reduced state $\sigma_V=e^{-K}/Z$, positivity of relative entropy gives $\Delta S\le\Delta\langle K\rangle$ for every state; both differences are finite although $S$ and $\langle K\rangle$ separately diverge (Casini 2008). For the Rindler wedge, Bisognano–Wichmann (1975, 1976) give $K=2\pi\int_{x>0}x\,T_{00}\,d^{d-1}x$ ($\hbar=c=1$): the vacuum is KMS at inverse temperature $2\pi$ for boosts. For a positive-energy excitation within proper distance $R$ of the edge, $\Delta\langle K\rangle\le2\pi RE$, which is Bekenstein's $S\le2\pi RE$; this step is [A] (Casini: weakly self-gravitating systems, semiclassically).

Finite and continuum forms are one statement: **the entropy of a KMS reference state can rise by at most the rise of its modular energy.** The Bekenstein inequality is the Port Principle's passivity of a KMS state, tested against all states rather than unitary orbits only. Its $2\pi$, carried by Paper 32.1 (§9) as "[C], character/Hopf-angle candidate", is the Bisognano–Wichmann modular inverse temperature, [P, cited]. $K$ is dimensionless; $\hbar$ and $c$ enter only when $K$ is written as $2\pi$ times a boost generator in laboratory units.

---

## 7. What this does to the dictionary [A]

| Item (where) | Before | After |
|---|---|---|
| $\Phi$ as effective action (32 Claim 2.1; T2 §6; 01c §7) | posited | generating function of the free states (Thm 1) [P] |
| Space = inertia (32 Thm 3.1) | [P] via $\tfrac12g(v,v)$ | static FDT, equilibrium identity (Thm 2) [P]; broken by the current (Thm 3), testable |
| $R=\mathrm{AN}(T)$ (32 Rem 16.2b) | presented as found | classical (Shima) [P, credited] |
| Hellinger sphere, $\log Q$ (32.1 §3–4) | [P] | classical [P, credited]; $\log Q$ = $\beta=0$ face of Thm 4 |
| Bekenstein "$\le$" (32.1 §6) | data processing of a projection | relative-entropy positivity against a KMS state [P] |
| $2\pi$ (32.1 §9) | [C] | KMS inverse temperature [P, cited] |
| 32.1 Remark 4.3 energy | defined so as to saturate | circular; demoted |
| Gravity = closure defect (32 Thm 4.1(3)) | [P] | localization [P] (32 §5); gravity reading [C] |
| Firewall (32 §12) | Theorem | Principle, true by construction |
| Holographic boundary (32.1 §7) | "boundary" | arithmetic (unit-group) boundary, not spatial |
| Quantum detailed balance (32 §9, §14; T24 fork) | one notion | a family indexed by the monotone metric; the push decides which (§4.1) [P] |

**Phase-2 relabels in Paper 32 (out of scope here).** Dimensional selection (§8): route 1 is "angular momentum is a vector iff $n=3$", which Definition 8.1 encodes, and route 2 is specific to $\mathbb Z/6$ on a different row ($\mathbb Z/30$ gives $1+2+4=7$), so they are not two independent routes that agree. Theorem 9.1: the $-H\,dt$ is the contact sign of extended phase space, present in every dimension. §10.2: the Lorentzian row is post-diagnosis. §10.3: $\sin^2\theta_W=3/8$ is textbook $SU(5)$ given the $2+3$ split, and $Y\propto(\tfrac12,-\tfrac13)$ is forced by tracelessness on any split; [A].

**Where the tower legitimately meets gravity [A, cited].** Relative entropy between nearby KMS states is the expansion of §5. In holographic field theory rung 1, the first law $\delta S=\delta\langle K\rangle$ (Blanco–Casini–Hung–Myers 2013), yields the linearized Einstein equations (Faulkner–Guica–Hartman–Myers–Van Raamsdonk 2014; cf. Jacobson 2016). Rung 2 is the canonical energy of the gravitational perturbation, which equals the quantum Fisher information (Lashkari–Van Raamsdonk 2016), i.e. the Kubo–Mori Hessian of Proposition 2.1. That route runs through modular Hamiltonians of spatial regions, not through the categorical simplex, and nothing here shortens it. It is the honest address for Paper 32's gravity readings.

**Safe:** $\Phi$ is the generating function of the free states of the copy lift; "space = inertia" is the static FDT, an equilibrium identity broken at first order by the current; the Bekenstein inequality is relative-entropy positivity against a KMS state. **Unsafe:** "$\Phi$ is the effective action of physics"; "gravity is the closure defect"; "the Bekenstein bound follows from the categorical simplex".

---

## 8. Certificate

`empirical/foundations54/p54_cert.py`: exact `Fraction`/`sympy` arithmetic decides everything; `mpmath` appears only in the K3f witness. Falsifiers were written into the docstring before the first run.

| Checks | Content | Result |
|---|---|---|
| K1a–c | Gibbs passive to $n=5$; 29 passive non-Gibbs states activate at the Stern–Brocot $n^*$ (brute force); $\theta=\log p$ | PASS |
| K2a–e, K2q | Thm 2 (symbolic, $Q=3,4$; PD on a slice, PSD rank $Q-1$ on $\mathbb R^Q$); Prop 5.1; Legendre; Bregman; Prop 2.1 | PASS (K2d: run-1 artifact) |
| K3a–f | Thm 3: detailed balance exact; 3-cycle $27/28,12/13,49/52$; trees; rank $=b_1$; three readings; [witness] bound and true exponential perturbation | PASS (K3d: run-1 artifact) |
| K4a–b | Prop 5.2, $Q=3,4,5$, two routes | PASS |
| K5a–c | Thm 4: identity, exact signs, faces | PASS |
| K6a–g | Thm 3Q, Props 4.1–4.2, Cor 4.3 (qubit, exact in $\mathbb Q(\log2,i)$; `p54q_lindblad_cert.py`): DB pattern $G=(T,T,T)$, $K=(F,T,F)$, $N=(F,F,F)$; $1-3/(5\log2)$; BKM-only neutrality; hypocoercive control | PASS (blind, 11/11) |
| K6h | [post-run, not blind] true finite tilts of the non-equilibrium generators; the 3Q(b) bound | PASS |
| H1–H6 | Thm 3H, Props 4.4–4.5 (`p54hs_harada_sasa_cert.py`; exact identities certified by evaluation beyond the degree bound): Agarwal formula; violation spectrum and its DB pattern; sum rules, $\|\mathcal A_f\|^2_{\rm HS}$; Langevin $16/3=E|\nu|^2$; Kubo; positivity in 7 cells | PASS (run 3, 8/8) |
| P1–P4′ | Lemma 4.6, Theorem 4.7 (`p54hs_op46_proof_cert.py`): closed forms for $n=2,3$ (failing at $n=4$ by a Pfaffian term, as predicted); evenness and the Jacobi step exact on 7 Lindblad cells at 12 frequencies; every root in the upper half-plane (50 digits); 1,980 random dissipative matrices | 4/5: P4 failed (spurious infinite eigenvalues), retained; P4′ post-diagnosis passes |

**Run log (frequency-resolved).** Runs 1 and 2 of `p54hs_harada_sasa_cert.py` were stopped by hand while symbolic simplification of complex rational functions of $\omega$ ran past 30 minutes; no verdict past H1 had been seen. The checker was changed to exact evaluation at more points than the degree bound of each rational identity, and run 3 passed 8/8, blind for H2–H6. The all-positive result was again treated as suspect, and an exploratory, not-blind probe searched for counterexamples to frequency-wise positivity (none in 4,900 cases); the statement was then proved (Lemma 4.6, Theorem 4.7). In the proof certificate, run 1 was stopped inside a fully symbolic $n=4$ expansion before any verdict. The pre-registered random-matrix check P4 then failed: the floating-point generalized eigensolver returned three spurious infinite eigenvalues of a singular pencil (odd $n$; residuals $0.16$–$0.94$, so not eigenpairs). The failure is retained; a post-diagnosis check that keeps only genuine eigenpairs passes on the same 1,980 matrices.

**Run log (quantum).** `p54q_lindblad_cert.py` ran 11/11 blind. Because an all-positive run is itself suspect, two checks were added after it and are labelled not blind: the true finitely tilted non-equilibrium generators reproduce the predicted responses (agreement $1.3\times10^{-17}$, the floor set by double-precision complex entries in that witness), and the 3Q(b) bound holds with ratio at most $0.98$.

**Run log (classical).** Run 1 (blind): 19/21. K2d failed because an assumption-blind simplifier could not cancel $-\log x-\log(1/x)$ without knowing $x>0$ (30-digit witness $0$). K3d failed because `nsimplify` turned an exact rational stationary law on one $K_4$ assignment into a surd approximation, giving a spurious rank $4>b_1$. These are the failure classes of Port P3.N2 and P4.R10. Both checkers were fixed and logged; neither failure counts as a result. Run 2: 21/21, not blind for the two repaired checkers.

---

## References

- G. S. Agarwal, *Z. Physik* 252 (1972) 25; Open quantum Markovian systems and the microreversibility, *Z. Physik* 258 (1973) 409. — R. Alicki, *Rep. Math. Phys.* 10 (1976) 249. — S. Amari, *Differential-Geometrical Methods in Statistics*, Springer, 1985; S. Amari, H. Nagaoka, *Methods of Information Geometry*, AMS, 2000.
- C. Atkinson, A. F. S. Mitchell, Rao's distance measure, *Sankhyā A* 43 (1981) 345.
- M. Baiesi, C. Maes, B. Wynants, *PRL* 103 (2009) 010602. — F. Barbaresco, *Entropy* 16 (2014) 4521.
- E. A. Carlen, J. Maas, Gradient flow and entropy inequalities for quantum Markov semigroups with detailed balance, *J. Funct. Anal.* 273 (2017) 1810.
- F. Fagnola, V. Umanità, Generators of detailed balance quantum Markov semigroups, *IDAQP* 10 (2007) 335.
- J. J. Bisognano, E. H. Wichmann, *J. Math. Phys.* 16 (1975) 985; 17 (1976) 303.
- D. Blanco, H. Casini, L.-Y. Hung, R. C. Myers, Relative entropy and holography, *JHEP* 08 (2013) 060.
- H. B. Callen, T. A. Welton, *Phys. Rev.* 83 (1951) 34. — H. Casini, Relative entropy and the Bekenstein bound, *CQG* 25 (2008) 205021.
- N. N. Čencov, *Statistical Decision Rules and Optimal Inference*, Nauka 1972; AMS 1982.
- A. Dechant, S. Sasa, *PNAS* 117 (2020) 6430. — M. Esposito, C. Van den Broeck, *EPL* 95 (2011) 40004.
- T. Faulkner, M. Guica, T. Hartman, R. C. Myers, M. Van Raamsdonk, *JHEP* 03 (2014) 051. — I. Frérot, T. Roscilde, *PRB* 94 (2016) 075121.
- T. Harada, S. Sasa, *PRL* 95 (2005) 130602; Energy dissipation and violation of the fluctuation-response relation in nonequilibrium Langevin systems, *PRE* 73 (2006) 026131. — T. Jacobson, *PRL* 116 (2016) 201101.
- A. Kossakowski, A. Frigerio, V. Gorini, M. Verri, Quantum detailed balance and KMS condition, *CMP* 57 (1977) 97.
- A. Kolmogorov, *Math. Ann.* 112 (1936) 155. — J.-L. Koszul, *Bull. SMF* 89 (1961) 515. — R. Kubo, *J. Phys. Soc. Jpn.* 12 (1957) 570.
- N. Lashkari, M. Van Raamsdonk, Canonical energy is quantum Fisher information, *JHEP* 04 (2016) 153.
- A. Lenard, *J. Stat. Phys.* 19 (1978) 575. — D. Petz, *Linear Algebra Appl.* 244 (1996) 81.
- J. Prost, J.-F. Joanny, J. M. R. Parrondo, *PRL* 103 (2009) 090601. — W. Pusz, S. L. Woronowicz, *CMP* 58 (1978) 273.
- D. Reeb, M. M. Wolf, *NJP* 16 (2014) 103011. — J. Schnakenberg, *Rev. Mod. Phys.* 48 (1976) 571.
- T. Speck, U. Seifert, Restoring a fluctuation-dissipation theorem in a nonequilibrium steady state, *EPL* 74 (2006) 391.
- U. Seifert, T. Speck, *EPL* 89 (2010) 10007. — H. Shima, *The Geometry of Hessian Structures*, World Scientific, 2007.
- K. Temme, M. J. Kastoryano, M. B. Ruskai, M. M. Wolf, F. Verstraete, The $\chi^2$-divergence and mixing times of quantum Markov processes, *J. Math. Phys.* 51 (2010) 122201.
- P. Skrzypczyk, A. J. Short, S. Popescu, *Nat. Commun.* 5 (2014) 4185. — J.-M. Souriau, *Structure des systèmes dynamiques*, Dunod, 1970.
- Program: PortPrinciple.md (Thms 6.3, 6.10; Cor 6.13; Prop 8.5; §10); Paper 32; Paper 32.1; T2; 01c; forward3_reversibility.md; Paper 53.
