# Two-mode covariance test: exact law and calibration tradeoff

*October 9, 2026. Prospective analysis of the same RC/filter model. No experimental observations.*

## Result and recommendation

The two-mode test removes an unknown common overall gain exactly, and its power can be computed exactly even when component mismatch correlates the modes. However, **the tested pair does not improve the current experiment budget**:

| Design | Known calibration/shape | Tight-scenario conditional budget with 99% envelope coverage |
|---|---:|---:|
| One projected variance | 71 records | 219 records |
| Two-mode variance ratio | 147 records | 467 records |

Both columns target overall size at most 5% and power at least 90%. The calibrated column uses the same component-uncertainty scenario and the same rounding rule as the previous stress study. For one mode, the assumed final envelope bounds each projected variance by ±10%; for two modes, it bounds each predicted variance ratio by ±10%. Neither envelope's coverage is certified by the finite component stress cases.

Keep the one-mode design as the current baseline. The ratio test is useful when a common scale is genuinely unknown, but it replaces scale calibration with covariance-shape calibration and adds denominator noise. This result concerns the explicit pair-selection rule below; it is not an optimality theorem against every possible pair or multi-mode statistic.

## Choose a physical reference mode, not a detector-noise mode

Let $V_0,V_1$ be the calibrated 401-sample record covariances under omitted hidden noise and full thermal noise, respectively. Choose generalized eigenvectors satisfying
$$
V_1w_j=\lambda_jV_0w_j,\qquad w_i^{\mathsf T}V_0w_j=\delta_{ij}.
$$
The numerator is the largest-eigenvalue mode. For the denominator, choose the smallest-eigenvalue distinct mode whose null variance is at least 90% attributable to the physical plant, as evaluated by turning detector noise off in the covariance calculation. This avoids choosing the reset sample, which contains only output detector noise and would not track physical gain or temperature.

This rule is fixed before test data. At the nominal 100 Hz cutoff it selects
$$
\lambda_+=1.6405331214,\qquad \lambda_-=1.0080424582,
\qquad r=\frac{\lambda_+}{\lambda_-}=1.6274444674.
$$
The numerator and denominator plant fractions are 99.7709% and 90.0568%, respectively. Their two-score covariance matrices are, to numerical precision,
$$
\Sigma_0=I_2,\qquad \Sigma_1=\operatorname{diag}(\lambda_+,\lambda_-).
$$
For each trial record $Y_i$, compute $X_i=w_+^{\mathsf T}Y_i$ and $Z_i=w_-^{\mathsf T}Y_i$. Use sample variances about their respective sample means, and form $R_N=s_X^2/s_Z^2$. Both scores use the same record; **147 means 147 records, not 294**. The score sequences are independent at the nominal model because they are jointly Gaussian and uncorrelated under each hypothesis.

## Exact nominal power

Put $\nu=N-1$. Under $H_0$, $R_N\sim F_{\nu,\nu}$; under $H_1$, $R_N/r\sim F_{\nu,\nu}$. Reject at $R_N>F_{\nu,\nu;0.95}$. The exact power is
$$
\mathcal P_N=\overline F_{\nu,\nu}\left(\frac{F_{\nu,\nu;0.95}}{r}\right).
$$
At $N=147$, the threshold is 1.31409310 and power is 0.901237. $N=146$ is insufficient for 90% power. This is the standard normal-theory [variance-ratio F test](https://itl.nist.gov/div898/handbook/eda/section3/eda359.htm), with independence supplied here by the chosen Gaussian record modes rather than separate experiments.

## Exact tail when mismatch correlates the pair

**Proposition.** Suppose the per-trial score pair is Gaussian with any common mean and positive-definite covariance
$$
\Sigma=\begin{pmatrix}a&c\\c&b\end{pmatrix}.
$$
Trials are independent. For $t>0$, define
$$
\Delta(t)=\sqrt{(a+tb)^2-4tc^2},\qquad
k(t)=\frac{\Delta(t)-a+tb}{\Delta(t)+a-tb}.
$$
Then
$$
\boxed{\Pr(R_N>t)=\overline F_{\nu,\nu}(k(t)),\qquad\nu=N-1.}
$$

*Proof.* The centered scatter matrix is Wishart with $\nu$ degrees of freedom and scale $\Sigma$. The event is that the sum of $X^2-tZ^2$ over $\nu$ independent centered Gaussian pairs is positive. The symmetric quadratic form $\Sigma^{1/2}\operatorname{diag}(1,-t)\Sigma^{1/2}$ has eigenvalues
$$
\ell_\pm=\tfrac12(a-tb\pm\Delta(t)),\qquad \ell_+>0>\ell_-.
$$
After orthogonal rotation the event is $\ell_+U> |\ell_-|V$, where $U,V$ are independent $\chi^2_\nu$ variables. Their ratio gives the displayed tail. The mean disappears through centering. $\square$

This derivation is a standard Gaussian-quadratic-form calculation, not a claim of a new general distribution. It prevents treating perturbed score pairs as independent without checking.

**Correlation-safe bounds.** Write $q=a/b$ and $\rho=c/\sqrt{ab}$. For a threshold $t>q$, increasing $|\rho|$ decreases the upper-tail probability relative to $\rho=0$. For $t<q$, increasing $|\rho|$ increases it. This follows directly from the expression for $k(t)$ as its square root decreases with $|\rho|$.

Consequently, if calibrated bounds give $q_0\le q_0^+$ and $q_1\ge q_1^-$, use threshold $q_0^+F_{\nu,\nu;1-\alpha}$. Whenever that threshold is below $q_1^-$, taking both correlations to be zero is conservative for null size and alternative power. For relative bounds $u$ on both nominal ratios, the sufficient contrast is
$$
r_{\rm safe}=r\frac{1-u}{1+u}.
$$
Choosing $N$ for target power above one half automatically puts the threshold below the bounded alternative ratio. Thus exact robust power does not require certifying that mismatch preserves zero correlation.

## What gain cancellation does—and does not—remove

For any fixed nonzero overall scale $g$, $Y_i\mapsto gY_i$ scales both sample variances by $g^2$ and leaves $R_N$ unchanged sample by sample. This is exact. It also removes a common scale multiplying the entire Gaussian covariance.

A hardware gain upstream of additive output noise is not a common scale on the complete record. Temperature does not scale a fixed detector-noise floor either. In the adopted physical detector model, halving/doubling the hardware gain changes nominal-test size to 3.08%/5.62% and power to 85.65%/91.08%. Halving/doubling temperature changes size to 1.39%/8.93% and power to 76.75%/94.39%. The ratio substantially removes some scale dependence but does not justify a universal claim of detector- or temperature-independent inference.

## Stress results

The same 64 raw ±5% component draws used in the one-mode study give:

| Quantity | One mode | Tested two-mode pair |
|---|---:|---:|
| Maximum calculated false-positive rate at nominal threshold | 21.49% | 18.73% |
| Minimum calculated power | 71.48% | 74.40% |
| Tight-scenario rounded conditional envelope | ±10% variance | ±10% ratio |
| Conditional records with certified envelope | 198 | 420 |
| Records allowing 1% calibration-coverage failure | 219 | 467 |

For the two-mode tight scenario, targeted corners and random samples yielded $q_0^{\max}=1.07720$ and $q_1^{\min}=1.50792$. As before, we round the needed fractional allowance upward after adding two percentage points of margin. These finite checks do not certify the full parameter box. The loose scenario already has overlapping tested ranges, so the simple envelope method gives no uniform power guarantee.

The largest ratio sensitivities have moved to boundary resistance and detector cutoff. Their null log sensitivities are approximately 1.77 and -1.44; the thermal values are 1.40 and -1.44. The scalar test's common gain sensitivity was about 2, but the ratio's new shape sensitivities offset that advantage in the current uncertainty budget.

Bandwidth also matters more because a physical reference mode is needed. After selecting the pair from the calibrated model at each cutoff, nominal budgets at 1, 3, 10, 30, 100, and 300 Hz are **343, 199, 160, 150, 147, and 147** records. Low bandwidth suppresses the available reference modes as well as the signal. The one-mode covariance test needed 71 across those same nominal cases.

## Angle-form addition to Paper 60

Remark 6.3b now states, for $c>0$ and $\theta=\arctan(|b|/c)$,
$$
\pi_\infty=\frac{\sqrt{c^2+b^2}-c}{\sqrt{c^2+b^2}+c}
=\frac{b^2}{(\sqrt{c^2+b^2}+c)^2}=\tan^2(\theta/2).
$$
If $C$ commutes with $B^{\mathsf T}B$, use their common eigenmodes with eigenvalues $c_i$ and $b_i^2$ to get the same identity per mode. The remark retains the commuting qualification. Twelve rotated three-mode checks, each including a dark mode, agree with the matrix formula to $6.25\times10^{-16}$.

## Verification and next decision

`empirical/boundary60/two_mode_test.py` passed **8/8 declared checks on run 1**. It verifies the unchanged record model, dense versus adjoint two-score covariances, nominal independence, exact sample count, the correlated law against 150,000 Wishart samples in each of three cases, common-scale invariance, the correlation-safe bound, and the angle identity. Results and frozen projection weights are in `empirical/boundary60/two_mode/`; the log is `two_mode_run1.log`. `rc_record_model.py` exposes the existing record-model definitions without rerunning earlier experiments or overwriting their artifacts.

![Two-mode tradeoff](C:/Projects/simplicial/empirical/boundary60/two_mode/comparison.png)

Do not replace the 220-record conditional pilot by this pair. A better next analysis is to profile or eliminate a small set of nuisance parameters using several record modes, retaining exact or independently validated type-I error control. Compare that method against both existing tests using the same independent calibration budget. Reference-mode selection itself can also be optimized for nuisance sensitivity; the current rule optimizes contrast subject to a plant-fraction threshold, not the final robust acquisition cost.
