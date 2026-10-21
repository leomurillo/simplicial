# From boundary evidence to a physical observer

## Consolidated Gaussian derivations and reproducibility record

**October 10, 2026. Standalone research note.** This records the exploratory conversation without editing or integrating into existing papers. It is not a submission-ready manuscript, an external certificate, or a historical-priority claim. The companion [claim contract](C:/Projects/simplicial/FEP_gaussian_observer_claim_contract.md) identifies the proposed contribution and the single gap to pursue next.

## 1. Outcome and scope

We can calculate separately (i) evidence present in a complete boundary history, (ii) evidence retained by a physical internal coordinate, and (iii) error of a declared estimate or posterior encoding. A thermal Gaussian example permits exact covariance and work accounting. Numerical designs improve the internal record under fixed hidden dynamics, while an exactly solvable two-register device provides a restricted attainable work/rate frontier.

The active three-coordinate witness does **not** preserve the passive statistical Markov blanket. The reproduced partial correlation is approximately 0.226788 at peak readout and 0.215185 in its driven stationary state. This limits the FEP interpretation: the witness establishes improved internal sensing with an unchanged hidden port experiment, not improved inference under an unchanged blanket.

The strongest present statements are the explicitly scoped propositions below. Classical conditioning, data processing, spectral-spread inequalities, Kalman filtering, and linear stochastic thermodynamics supply their ingredients. A calibrated map from internal state to a posterior does not by itself prove that the internal dynamics perform variational inference.

## 2. Reference, target, record, and decoder

Let q=(e,b,i)^T contain a hidden environmental coordinate, a blanket coordinate, and an internal coordinate. Use the harmonic Hamiltonian H(q)=q^T Kq/2, with

$$
K=\begin{pmatrix}3&4&0\\4&a&h\\0&h&d\end{pmatrix}\succ0,
\qquad a+d=8.
$$

All temperatures are T>0 with k_B=1. Coordinate and time units are fixed before imposing stiffness or rate budgets. The reference initialization is

$$q_0\sim\mathcal N(0,TK^{-1}).$$

This differs from the earlier exploratory example with b_0=i_0=0. All numerical network results in this package use the thermal initialization above; an exactly reset physical memory is not assumed.

The hidden preparation variable is the conditional residual

$$z_0=e_0+\frac43b_0,\qquad u=\sqrt{3/T}\,z_0.$$

Under the reference, u is standard normal and independent of (b_0,i_0). More generally, a preparation changes the law of u while retaining the reference law of (b_0,i_0), independently, and using the same future bath laws. Its input resource is J=D(P_u||N(0,1)). The work calculations below average over the reference P_u=N(0,1), not uniformly over all preparations with finite J.

Let R_t be the complete retained record (b_s,i_s) for 0<=s<=t, including its initial values. The physical readout is M_t=i_t. The target is the **initial residual**, not the current environmental coordinate, an unknown force, or an unknown system parameter. A decoder must be declared for that target and readout time. Additional private randomization must be independent of u conditional on the available record for a Markov-chain argument U -> R -> M to apply.

Because K_ei=0, the initial Gibbs reference has e independent of i given b. This is a static Gaussian precision-matrix statement. Passive evolution preserves it; active evolution requires a new check.

## 3. Exact network readout and Gaussian preparation channel

For a fixed diagonal mobility M=diag(1,1,mu), mu>0, and a boundary-only skew force matrix

$$
N=\begin{pmatrix}0&0&0\\0&0&\omega\\0&-\omega&0\end{pmatrix},
$$

the dynamics are

$$dq=-M(K+N)q\,dt+\sqrt{2TM}\,dW.$$

The covariance Sigma_t is the **reference-ensemble** covariance and solves

$$\dot\Sigma=-A\Sigma-\Sigma A^T+2TM,
\quad A=M(K+N),\quad \Sigma_0=TK^{-1}.$$

It is generally time dependent when N is nonzero. With E_t=exp(-At), the initial residual obeys

$$\operatorname{Cov}(q_0,u)=\sqrt{T/3}\,e_e,
\qquad \operatorname{Cov}(q_t,u)=\sqrt{T/3}\,E_t e_e.$$

**Proposition 1 (instantaneous internal visibility).** The reference-normalized readout is a scalar Gaussian attenuation channel with squared coefficient

$$\boxed{\pi_i(t)=\frac{(T/3)(E_t)_{ie}^2}{(\Sigma_t)_{ii}}.}$$

Its sign is the sign of (E_t)_ie; a known sign reversal of the readout gives the usual positive square root. The independent channel-noise variance is (Sigma_t)_ii-(T/3)(E_t)_ie^2. Consequently,

$$\operatorname{Var}(u\mid i_t)=1-\pi_i(t),\quad
I(u;i_t)=-\tfrac12\log(1-\pi_i(t)),$$

under the reference. For an input mean shift u~N(m,1), the readout KL is exactly pi_i m^2/2 = pi_i J. Gaussian-reference SDPI extends D_output<=pi_i J to every finite-J preparation. The work constraint does not inherit that universal quantifier.

*Proof.* Decompose q_0=sqrt(T/3)e_e u+eta, where eta is independent Gaussian with covariance TK^{-1}-(T/3)e_e e_e^T. Propagate this decomposition through the linear dynamics and independent bath increments. Scalar Gaussian conditioning gives the posterior; the KL and mutual-information expressions follow. SDPI is a cited classical consequence, not a new inequality. QED.

For passive dynamics N=0, Sigma_t=TK^{-1} even when deterministic mobility switches occur with consistent bath noise. For the baseline a=7,h=d=1, (K^{-1})_ii=5/2 and

$$\pi_i(t)=\frac2{15}[(e^{-Kt})_{ie}]^2.$$

Its numerical peak is 0.00778725293 at t=1.95670415. For short times, pi_i(t)=(8/15)t^4+O(t^5); at long times it tends to zero. The delay reflects the two couplings from hidden coordinate to memory.

## 4. What the complete record contains

The hidden equation remains de=(-3e-4b)dt+sqrt(2T)dW_e, independent of the added boundary force. Subtract the known boundary-driven hidden response and transform the observed boundary increments. The resulting experiment is

$$dh=-3h\,dt+\sqrt{2T}\,dW_e,
\qquad dY=-4h\,dt+\sqrt{2T}\,dW_b.$$

This is the fixed-port experiment of Paper 60. Its scalar information coefficient satisfies the initial-state information Riccati equation. The visibility is

$$\pi_R(t)=\frac{I_t/3}{1+I_t/3},\qquad
I_t=\frac{8\tanh(5t)}{5+3\tanh(5t)}\quad(T=1),
\qquad\pi_R(\infty)=\tfrac14.$$

The initial retained state has zero information about u but is included in the record, so the residual transformation is available. The internal mobility changes used here affect only i, not the bath or drift of b or e. The complete record also reconstructs the internal Brownian motion by subtracting its known drift and dividing by its specified noise amplitude. The transformed experiment consists of Y, that independent internal Brownian motion, and the initial retained state. The latter two are ancillary and independent of the hidden target and Y. Invertibility follows from the linear equations with positive prescribed mobility. Thus the same hidden observation experiment survives both the known boundary force and these predetermined internal mobility changes. This is not an unrestricted claim for arbitrary mobility matrices or epistemic actions.

The implication is pi_i(t)<=pi_R(t). An improved instantaneous memory does not imply a better complete-record experiment. The general feedback-neutrality idea predates this application; see Harris et al. and the Paper 60 audit.

## 5. Evidence, memory, and declared inference error

Assume U -> R -> M and finite second moments. Orthogonal conditional-expectation projections give

$$
\mathbb E(U-\widehat u(M))^2
=\mathbb E\operatorname{Var}(U|R)
+\mathbb E(\mathbb E[U|R]-\mathbb E[U|M])^2
+\mathbb E(\mathbb E[U|M]-\widehat u(M))^2.
$$

For a unit-variance scalar Gaussian reference, these terms are

$$\boxed{(1-\pi_R)+(\pi_R-\pi_M)
+\mathbb E(\mathbb E[U|M]-\widehat u(M))^2.}$$

The middle term is loss incurred by replacing a record with the available physical memory. The last term is decoder excess error. This is a standard projection identity, not the novel contribution sought for a companion paper.

Under the needed density and integrability assumptions, expected predictive logarithmic loss has the corresponding identity

$$
\mathbb E[-\log q(U|M)]-H(U|R)
= I(U;R|M)+\mathbb E_M D(p(U|M)\Vert q(U|M)).
$$

The usual variational free-energy gap uses D(q(U|M)||p(U|M)), in the opposite direction. Both vanish for an exact posterior, but they cannot be substituted into the same decomposition. C10 checks this distinction in a concrete Gaussian chain.

An exact posterior for a nearly uninformative memory can have zero variational approximation error. That says nothing by itself about its usefulness for a specified external task. Conversely, interpreting any conditional law as an implicit belief does not establish a physical posterior-update mechanism. A FEP-facing theorem must predeclare the model, target, encoding, and admissible internal dynamics.

## 6. Reversible transfer: classical operator corollary

Whiten a stationary reversible overdamped Gaussian process, so its drift is a symmetric positive matrix H and its covariance is I. Let U=v^T x_0 and Z_t=w^T x_t, with unit v,w and v perpendicular to w. If the eigenvalues of H lie in [alpha,beta], then

$$\operatorname{Corr}(U,Z_t)=w^T e^{-Ht}v.$$

Subtract cI with c=(exp(-alpha t)+exp(-beta t))/2. Orthogonality removes its cross term, and the spectral norm gives

$$\boxed{\pi(t)\le\tfrac14(e^{-\alpha t}-e^{-\beta t})^2<\tfrac14.}$$

This is a spectral-spread corollary, not a new operator inequality. It applies to initially independent linear coordinates and a current-state readout; it does not cover a complete path, inertia, time-switched products of propagators, or nonreversible dynamics. The equality limit 1/4 requires singular time-scale separation; fixed positive finite spectral bounds give a smaller value. The numerical random checks are implementation checks; this argument is the proof.

## 7. Work, retention, and the numerical comparison

The active force is f=-Nq. With diagonal mobility M, its reference-averaged Stratonovich power is

$$\dot W=\operatorname{tr}[N^T M(K+N)\Sigma_t]-T\operatorname{tr}(MN).$$

The second term vanishes for the diagonal M and skew N used here. For unit acquisition mobility this reduces to the expression used in the conversation. Work is integrated through the acquisition phase only. It excludes the physical actuator, clock, mobility-switch mechanism, initial signal preparation, and a reusable measurement/readout apparatus.

For the zero-mean reference evolving from equilibrium,

$$\Delta F_t/T=\tfrac12[\operatorname{tr}(K\Sigma_t/T)-3-\log\det(K\Sigma_t/T)],
\qquad \Sigma_{\rm prod}=W/T-\Delta F_t/T\ge0.$$

After a gate at time tau, remove N and use M_h=diag(1,1,0.01). With H_s=exp(-M_h K s), the readout covariance and propagator at t=tau+s are

$$\Sigma_t=TK^{-1}+H_s(\Sigma_\tau-TK^{-1})H_s^T,
\qquad E_{t,0}=H_s E_{\tau,0}.$$

Changing mobility leaves the Hamiltonian fixed and has no explicit work term in this SDE. The controller cost is outside the model. A prescheduled gate is not an autonomous fixed-parameter network.

The numerical family fixes a+d=8, K>=0.1 I, independent equal-temperature baths, |omega|<=4, and a gate readout at t=10. Constant passive mobility lies in [0.01,1]. Active acquisition and passive gate acquisition last at most 3; passive peak searches allow t<=10. The hidden relaxation/coupling remain 3 and 4. Scripts record every seed, bound, solver status, work value, and candidate.

| Model/protocol | Reported visibility | Classification |
|---|---:|---|
| Original passive peak | 0.00778725293 | Value of a fixed witness |
| Retuned passive peak | 0.00925008774 | Best-found numerical candidate |
| Constant passive, read t=10 | 0.00197790652 | Best-found numerical candidate |
| Passive gate, read t=10 | 0.00861339958 | Best-found numerical candidate |
| Active peak, W/T<=1 | 0.01842812626 | Best-found numerical candidate |
| Active peak, W/T<=10 | 0.04822544982 | Best-found numerical candidate |
| Active then gate, W/T<=1, read t=10 | 0.01656870865 | Best-found numerical candidate |
| Active then gate, W/T<=10, read t=10 | 0.04090894782 | Best-found numerical candidate |

These values validate feasible improvements, not global optimality or experimental performance. Repeating a search can find a better candidate. The component budget is an explicitly chosen comparison class, not a complete material cost model.

### The blanket correction

In a Gaussian law, e independent of i conditional on b is equivalent to (Sigma^-1)_ei=0. For the W/T=1 active peak witness, C09 finds

$$\operatorname{Corr}(e,i|b)\approx0.226788343$$

at its readout time, and approximately 0.215185081 in the stationary driven covariance. The passive witness gives about -1.65e-15. Consequently, this active comparison must not be described as keeping the same statistical blanket. It keeps the hidden port dynamics, which is a different condition.

## 8. Exact attainable work/rate frontier for a transfer stage

Consider normalized registers X=(X_1,X_2)^T initially N(0,I), with

$$dX=-(\alpha I+\omega(t)J)X\,dt+\sqrt{2\alpha}\,dW,
\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$

The target is X_1(0); only X_2(t_f) is read. Alpha is fixed. Controls are deterministic, predetermined rotation schedules with |omega|<=omega_max; t_f is freely chosen in advance. No feedback stopping, stiffness changes, extra baths, auxiliary memory, or upstream acquisition is included.

The covariance remains I. Define theta=integral omega dt and tau=alpha t_f. Commuting propagators give

$$\pi=e^{-2\tau}\sin^2\theta,\qquad
W/T=(2/\alpha)\int\omega(t)^2dt.$$

The work formula follows from the nonconservative force in physical harmonic coordinates; it is reference-averaged. Since the reference density and mean energy remain unchanged, this work is dissipated as heat. This is not a zero-dissipation equilibrium process: its current is nonzero.

**Theorem 2 (restricted attainable frontier).** For E=W_max/T>0 and R=omega_max/alpha>0,

$$\boxed{\Phi(E,R)=\max_{0\le\theta\le\pi/2}
\sin^2\theta\exp[-2\max(2\theta^2/E,\theta/R)].}$$

Every maximum is attained by a constant drive. For E=0, the optimum is zero.

*Proof.* Cauchy-Schwarz gives theta^2 <= t_f integral omega^2 dt <= E tau/2. The rate constraint gives |theta|<=R tau. Thus tau>=max(2theta^2/E,|theta|/R). Visibility at a fixed useful angle decreases with tau. A constant drive at the minimum admissible duration attains the upper bound. Any larger absolute angle has an angle in [0,pi/2] with the same sin^2 and no larger duration/resource requirement; sign reversals cannot improve the lower duration bound. Maximizing completes the proof. QED.

For a complete closed form define

$$\theta_0=\arctan(R/2),\quad \theta_1=\arctan R,
\quad E_0=2R\theta_0,\quad E_1=2R\theta_1.$$

The optimizer is:

- 0<E<E_0: unique theta in (0,theta_0) satisfying E=4theta tan(theta); normalized rate r=2tan(theta), duration tau=theta/r.
- E_0<=E<E_1: theta=E/(2R), rate r=R, duration tau=theta/R.
- E>=E_1: theta=theta_1, rate r=R, duration tau=theta_1/R; some allowed work is unused.

These follow by differentiation on the two branches and comparison at their crossover. On the unconstrained-rate branch, Phi=exp[-theta cot(theta)]sin^2(theta). Its small-E asymptote is E/(4e), and 1-Phi(E,infinity)~pi^2/E at large E. For finite R,

$$\Phi(\infty,R)=\frac{R^2}{1+R^2}\exp[-2\arctan(R)/R].$$

At R=4, the transitions are E_0=8.85718974235 and E_1=10.60654130934. Phi(1,4)=0.08484435006, Phi(5,4)=0.32169223042, Phi(10,4)=0.48204135231, and Phi(infinity,4)=0.48503537447. Exceeding 1/4 requires E>3.53884210615 in this family. This is not a universal work threshold for beating passive memory.

If the first register is itself a justified Gaussian channel from a hidden target with visibility pi_in, and the second register/future baths are independent, channel composition gives pi_out<=pi_in Phi(E,R), with equality for optimal transfer. Acquiring that first register, its initial correlations, and its physical handoff has not been costed by this theorem. It is a transfer frontier, not the full three-coordinate frontier.

## 9. Reproducibility and audit record

Package: [empirical/gaussian_observer](C:/Projects/simplicial/empirical/gaussian_observer/README.md).

From the project root:

```powershell
python empirical\gaussian_observer\verify.py
python empirical\gaussian_observer\optimize.py --case all --seeds 7 23
```

Python 3.12.13, NumPy 2.4.4, and SciPy 1.17.1 were used. Each invocation creates a timestamped output directory, retaining source hashes, environment details, results and failures. The verifier's tolerances were declared before the first package run. The first run passed 10/10 groups without a repair of the checker:

[First audit JSON](C:/Projects/simplicial/empirical/gaussian_observer/runs/20261010T174925_244752Z/results.json), [first audit log](C:/Projects/simplicial/empirical/gaussian_observer/runs/20261010T174925_244752Z/run.log).

The saved two-seed search also completed for all seven optimized cases: [optimization results](C:/Projects/simplicial/empirical/gaussian_observer/optimization_runs/20261010T175019_508844Z/results.json) and [optimization log](C:/Projects/simplicial/empirical/gaussian_observer/optimization_runs/20261010T175019_508844Z/run.log). All fourteen reported candidates met their declared work budgets within numerical feasibility tolerance. This repeat search reproduced the conversation's reported values; it is not a global-optimality certificate.

The audit includes exact-value reproduction, independent ODE covariance/mean/work integration, a direct Van Loan Gaussian channel calculation, entropy-production accounting, temperature scaling, a blanket diagnostic, and independent optimization of the rotation frontier. Two-dimensional numerical search does not prove the frontier; Theorem 2 does. Candidate checks do not prove global optimality of the three-coordinate designs. Sampled reversible inequalities do not establish a universal theorem; Section 6 supplies the proof.

## 10. Provenance and FEP interpretation

- [Friston et al., The free energy principle made simpler but not too simple](https://arxiv.org/abs/2201.06387): use a dynamical, path-aware FEP formulation as the comparison, not a caricature based only on stationary density.
- [Heins and Da Costa, Sparse coupling and Markov blankets](https://arxiv.org/abs/2205.10190), and [Aguilera et al., How particular is the physics of the free energy principle?](https://arxiv.org/abs/2105.11203): the statistical/dynamical assumptions and the inference interpretation require explicit checks.
- [Hartich, Barato and Seifert, Sensory capacity](https://arxiv.org/abs/1509.02111): close antecedent for comparing current physical state with its history and for sufficiency-related performance. Our observable is initial-preparation visibility, not their learning-rate ratio.
- [Harris et al., Minimum requirements for feedback enhanced force sensing](https://arxiv.org/abs/1303.1589): complete-record feedback equivalence is prior work.
- [Dechant and Lutz, Fundamental limits on nonequilibrium sensing](https://arxiv.org/abs/2407.17831): nonreciprocal sensing gains at an energetic cost are prior work. Their force-sensing observable differs from this preparation experiment.
- [Bhatia and Sharma, Positive linear maps and spreads of matrices-II](https://doi.org/10.1016/j.laa.2014.10.030): spectral-spread provenance for the reversible corollary.
- [Landi, Tome and de Oliveira, Entropy production in linear Langevin systems](https://arxiv.org/abs/1507.00232), and [Sagawa and Ueda, Minimal energy cost for thermodynamic information processing](https://arxiv.org/abs/0809.4098): thermodynamic accounting and memory-cost context.
- [Polyanskiy and Wu, Strong data-processing inequalities](https://arxiv.org/abs/1508.06025): information contraction machinery.

No general FEP principle has been proved or refuted here. The presently useful message is operational: specify the external task, accessible record, physical memory and noise, and decoder before interpreting an internal state as a successful inference mechanism. The next theorem must address the compatibility of that operational requirement with a specified blanket and dynamics, rather than merely assigning a posterior after the fact.

**Proposed main theorem for a companion paper:** a quantitative criterion for realizing a declared full-record posterior in a finite noisy internal state, subject to a specified statistical blanket, fixed hidden port, and explicit physical resources.

**Nearest existing result:** sensory capacity/sufficient-statistic characterizations and Gaussian filtering, combined with established blanket conditions. The contribution must be an additional physical compatibility or resource obstruction, not the definition of sufficiency.

**Single missing result:** a realizability or impossibility theorem that enforces the blanket and fixed-port conditions simultaneously and quantifies the remaining posterior deficit. The active witness above does not supply it; the next-turn claim contract makes that gap the target.
