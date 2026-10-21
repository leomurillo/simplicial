# Can the existing thermal blanket realize its full-record posterior?

Research decision and proved, scoped obstruction — October 10, 2026.
Standalone companion to the observer derivation note and claim contract. No manuscript changes.

## Decision

In the existing three-coordinate family, the three requested properties cannot coexist: fixed hidden port, a reference statistical blanket preserved throughout acquisition, and exact realization of the full-record posterior by the current internal coordinate. Nonzero circulation breaks the blanket immediately. Zero circulation preserves the blanket, but the physical memory still has a strictly positive posterior deficit. Independent internal thermal noise also prevents exact realization in the active family, whether or not a blanket is required.

This closes the proposed compatibility test for this family. It is not a general impossibility theorem for FEP, arbitrary blankets, shared-noise observers, or noiseless filtering hardware. The mathematical ingredients are standard covariance evolution and Gaussian projection. We should develop a restricted technical companion, not announce an FEP breakthrough on this basis.

## 1. Model and exact meaning of the requirements

Write the internal coupling as k to avoid confusing it with a hidden process:

\[
K=\begin{pmatrix}3&4&0\\4&a&k\\0&k&d\end{pmatrix}\succ0,
\quad M=\operatorname{diag}(1,1,\mu),\quad
N=\begin{pmatrix}0&0&0\\0&0&\omega\\0&-\omega&0\end{pmatrix}.
\]

For constant finite parameters, T>0 and mu>0,

\[
dq=-M(K+N)q\,dt+\sqrt{2TM}\,dW,
\quad q=(e,b,i),\quad q_0\sim N(0,TK^{-1}).
\]

All results below concern this Gaussian reference ensemble. A changed preparation need not preserve the same instantaneous blanket. The inference target is the initial residual

\[
U=\sqrt{3/T}(e_0+4b_0/3)\sim N(0,1).
\]

The full retained record R_t comprises both paths b and i and their initial values. The physical memory is the scalar i_t. A decoder may use the known time and parameters but not an additional stored path. Exact posterior realization means a measurable map from i_t to the distribution p(U|R_t), almost surely. This is stronger than a synchronization map between conditional expected states.

The fixed port is the unchanged hidden equation de=(-3e-4b)dt+sqrt(2T)dW_e and the unchanged blanket bath. A preserved statistical blanket means e_t is conditionally independent of i_t given b_t at every acquisition time in this reference ensemble, equivalently (Sigma_t^{-1})_{ei}=0. It does not mean only a missing e-i stiffness edge or independence at one selected time.

## 2. Theorem: immediate blanket obstruction

For any fixed mu>0, the reference blanket is preserved throughout an interval starting at zero if and only if omega=0.

**Proof.** Let Q=Sigma^{-1}, A=M(K+N). Covariance and precision satisfy

\[
\dot\Sigma=-A\Sigma-\Sigma A^T+2TM,
\qquad \dot Q=QA+A^TQ-2TQMQ.
\]

At Q_0=K/T,

\[
\dot Q_0=(KMN-NMK)/T,
\qquad (\dot Q_0)_{ei}=4\omega/T.
\]

Thus nonzero omega creates a nonzero precision entry at first order. For omega=0, Sigma=TK^{-1} is stationary and its precision has zero e-i entry. This proves both directions. In particular the initial conditional correlation has slope -4 omega/sqrt(3d).

The conclusion also rules out a first nonzero interval of a piecewise constant circulation schedule following passive equilibrium evolution: the same derivative applies at its onset. No claim is made here about arbitrary adaptive controls or isolated later zero crossings of Q_ei.

## 3. Theorem: a computable physical-memory deficit

Define g by dg=(-3g-4b)dt, g_0=-4b_0/3, and H=e-g. Then

\[
dH=-3Hdt+\sqrt{2T}\,dW_e,\quad H_0=\sqrt{T/3}U,
\qquad dY=-4Hdt+\sqrt{2T}\,dW_b.
\]

Y is computable from the retained record by

\[
dY=db+[4g+ab+(k+\omega)i]dt.
\]

Conversely, given Y, the independent initial retained coordinates and W_i, the retained paths are reconstructed by the linear equations below. The full record also reconstructs W_i. Thus the record is equivalent to Y plus ancillary variables independent of (U,Y); its posterior equals p(U|Y). This statement does not assert independence of the raw i-path and U conditional on the raw b-path.

Set X=(g,b,i). Its reconstruction equation is

\[
dX=LXdt+e_b\,dY+\sqrt{2T\mu}\,e_i\,dW_i,
\quad L=\begin{pmatrix}-3&-4&0\\-4&-a&-(k+\omega)\\0&-\mu(k-\omega)&-\mu d\end{pmatrix}.
\]

Let S_0=(TK^{-1})_{(b,i),(b,i)},
J_0=\begin{pmatrix}-4/3&0\\1&0\\0&1\end{pmatrix},
V_0=J_0S_0J_0^T, and E_L(t)=exp(Lt). Then the conditional memory variance is exactly

\[
V_{\rm anc}(t):=\operatorname{Var}(i_t\mid Y_{[0,t]})
=e_i^TE_L(t)V_0E_L(t)^Te_i
+2T\mu\int_0^t(e_i^TE_L(s)e_i)^2ds.
\tag{1}
\]

The second term V_priv is the private internal bath contribution. It is strictly positive for every t>0 because its integrand is continuous and equals one at s=0. The first term is uncertainty inherited from initial retained coordinates. Neither is information about U.

Let s_i=Sigma_ii(t), eta=V_anc/s_i, and define reference visibility pi_i=Cov(U,i_t)^2/s_i. The record visibility is

\[
\pi_R(t)=\frac{I_t}{3+I_t},\qquad
I_t=\frac{8\tanh(5t)}{5+3\tanh(5t)}.
\]

For every t>0,

\[
\boxed{\pi_i\leq\pi_R(1-\eta)<\pi_R.}\tag{2}
\]

Consequently no decoder of the scalar current internal state realizes the full-record posterior exactly.

**Proof.** Write m=E[U|Y] and i_t=f(Y)+xi, where f=E[i_t|Y]. The linear Gaussian reconstruction gives xi independent of (U,Y), with variance V_anc in (1). Therefore Cov(U,i)=Cov(m,f), Var(m)=pi_R, and Var(f)=s_i-V_anc. Cauchy–Schwarz proves (2). Exact Gaussian sufficiency would require pi_i=pi_R, which is excluded. Nonlinear decoding cannot improve the conditional expectation or restore a missing sufficient statistic. Equality in the first inequality holds precisely when f is proportional to m almost surely (including f=0). It is generally not attained by these observers.

The strict obstruction exists even without the blanket requirement. The blanket theorem separately prevents treating the earlier active witnesses as comparisons at a preserved statistical blanket. Neither theorem relies on a global numerical optimum.

## 4. Operational error and the source of the loss

The best squared-error decoder has risk 1-pi_i; the record posterior has risk 1-pi_R. Hence

\[
\Delta_{\rm MSE}=\pi_R-\pi_i\geq\pi_R\eta>0.
\tag{3}
\]

More exactly the deficit separates into pi_R eta plus [pi_R(1-eta)-pi_i]. The first term comes from ancillary memory variance; the remaining nonnegative term measures the mismatch between the temporal statistic f(Y) and the ideal posterior mean. Replacing eta by V_priv/s_i gives a weaker bound attributable to the internal bath alone.

For optimal predictive densities the excess expected log loss is

\[
\Delta_{\log}=I(U;R_t\mid i_t)
=\tfrac12\log\frac{1-\pi_i}{1-\pi_R}
\geq\tfrac12\log\left(1+\frac{\pi_R\eta}{1-\pi_R}\right)>0.
\tag{4}
\]

Any approximate decoder adds its expected forward KL from p(U|i_t). Equation (4) is not the usual reverse-KL variational free-energy objective. This distinction is essential for an FEP-facing presentation.

These are parameter-dependent bounds, not sharp globally optimized resource frontiers. All quantities are independent of T when K, mu, omega and t are fixed: covariances and the two ancillary variances scale together with T. This does not remove energetic or hardware constraints.

## 5. Reproduction and numerical witnesses

Run `python empirical/gaussian_observer/compatibility.py`. The script uses matrix exponentials and scalar quadrature for (1), checks it against a separately integrated covariance ODE, and tests the precision derivative by finite differences. One hundred seeded admissible parameter draws also check (2). These are implementation checks supporting the analytic proof, not an independent peer review or experimental data.

Recorded output: `empirical/gaussian_observer/compatibility_runs/20261010T175920_564340Z/results.json`. First run passed; maximum ancillary-covariance discrepancy 1.50e-11; maximum precision-slope discrepancy 2.95e-5 against declared tolerance 2e-4. Source hashes are recorded. No optimizer was rerun or required.

| Reference candidate | pi_R | pi_i | eta | Bound pi_R(1-eta) | Excess log loss (nats) |
|---|---:|---:|---:|---:|---:|
| Passive baseline at its peak | 0.250000 | 0.007787 | 0.896186 | 0.025953 | 0.139932 |
| Previously optimized passive candidate | 0.250000 | 0.009250 | 0.887800 | 0.028050 | 0.139194 |
| Active W/T=1 candidate | 0.249997 | 0.018428 | 0.855658 | 0.036085 | 0.134539 |
| Active W/T=10 candidate | 0.249286 | 0.048225 | 0.740578 | 0.064670 | 0.118651 |

For the baseline s_i=2.5, V_priv=1.2135976, so private thermal noise alone implies a visibility deficit at least 0.121360. Including initial retained uncertainty raises the bound to 0.224047, against the actual deficit 0.242213. The remaining 0.018166 is temporal-statistic mismatch. A variance fraction eta is not itself a fraction of hidden preparation KL; the equations specify its operational meaning.

## 6. Literature audit and publication consequence

[Parr et al., Memory and Markov Blankets (2021)](https://www.mdpi.com/1099-4300/23/9/1105) explicitly distinguish independence in a steady-state density from memory of earlier configurations. The coexistence of memory and a statistical blanket is therefore not our discovery, and the present obstruction must retain its particular dynamics and posterior target.

[Da Costa et al., Bayesian mechanics for stationary processes (2021)](https://doi.org/10.1098/rspa.2021.0518), sections 2–3, construct a synchronization map between conditional expected internal and external states. Their posterior construction distinguishes an actual internal state from its conditional expectation. Our single-realization, full-history initial-target criterion is stronger and different; failure of it does not contradict that result.

[Hartich, Barato and Seifert, Sensory capacity: an information theoretical measure of the performance of a sensor (2016)](https://arxiv.org/abs/1509.02111) is the direct prior for comparisons between physical sensor states and observation histories. [Heins and Da Costa, Sparse coupling and Markov blankets (2022)](https://arxiv.org/abs/2205.10190) is pertinent to the distinction between coupling sparsity and statistical blankets. The present calculation supplies an explicit fixed-port thermal benchmark, not a new filtering principle. No exhaustive priority claim is made for equation (2).

**Publication decision:** the breakthrough gate in the claim contract is not passed. Retain this result as a technical companion about operational posterior fidelity in thermal observers. A defensible angle is *From boundary information to physical inference: an exact thermal observer benchmark*. Lead with the measured target, record ceiling, realized-memory loss and an experimentally estimable posterior deficit. Do not headline a contradiction of FEP or a universal cost of beliefs.

**Next best turn:** consolidate the companion outline and its one decisive figure around the chain “hidden preparation → boundary record → physical memory → declared posterior.” Use these proved inequalities and existing verified witnesses; place the FEP interpretation after the operational result. Before claiming any broader FEP advance, specify a genuinely additional empirical prediction that survives the above prior-art comparison. Do not add another model merely to sustain breakthrough framing.
