# Thermal visibility experiment: stress test and model-discrimination budget

*October 9, 2026. Prospective calculations for the proposed 13-loop circuit. No hardware data or measured calibration uncertainties are available.*

## Decision

For a prespecified scalar covariance test, the nominal apparatus requires **71 independent records** for a one-sided 5% significance level and at least 90% power against the model omitting hidden bath noise. If both predicted projected variances have certified ±10% bounds, the sufficient budget becomes **198 records**. If those bounds instead have at least 99% joint coverage from independent calibration, allocate calibration failure into the error budget: **219 records**, or a rounded pilot target of **220**, gives overall size at most 5% and power at least 90%, conditional on the stated Gaussian model and coverage assumptions.

The component sensitivity study supports ±10% as a plausible *target* for a tightly calibrated apparatus; it does not certify that envelope over the entire component-uncertainty box. A 220-record acquisition is therefore not yet a laboratory performance guarantee. Calibration and independent resets must be established first.

The main vulnerability is calibration, not the tested bandwidth range. In 64 random circuits with uncalibrated ±5% component mismatch, the nominal 5% test had false-positive rates from 0.50% to **21.49%**. A loose calibration scenario produced overlapping projected-variance ranges, for which this one-sided test has no uniform 90%-power guarantee regardless of record count.

## The hypotheses—and the distinction from preparation visibility

Both models use the same calibrated drift, initial thermal distribution, detector, and any deterministic preparation mean. At the start of the record:

- $H_1$: all resistors continue to supply their thermal noises.
- $H_0$: the hidden bath noises are omitted, while the boundary bath and detector noises remain.

This $H_0$ is the diagnostic counterfactual in the earlier protocol, not a stationary equilibrium model satisfying the same fluctuation–dissipation relation. Its covariance relaxes away from the common thermal initial covariance. The models have the same mean response and different record covariances, $V_1$ and $V_0$. They can consequently be distinguished using **unprepared reference trials**, with no hidden mean shift at all.

The 71–219 record budgets test this covariance-model difference. They do **not** replace the roughly 28,000 prepared trials previously estimated for 20% precision on depth-2 preparation KL, and rejecting $H_0$ does not validate the spatial visibility theorem. The covariance test is a bath-model and apparatus check; preparation-to-record KL remains the second-stage scientific test. Do not pool different preparation depths or labels into one variance test: variable mean responses would add a spurious variance.

## Physical mismatches are modeled in the plant

Keep nominal units $R_*=10\,\mathrm{M}\Omega$, $C_*=1\,\mathrm{nF}$, $t_*=R_*C_*=10\,\mathrm{ms}$. There are 13 private resistors, 13 private capacitors nominally $5C_*$, and 14 shared/end capacitors nominally $C_*$. Each may vary independently. In dimensionless charge coordinates,
$$
K_{ii}=C_{p,i}^{-1}+C_{c,i}^{-1}+C_{c,i+1}^{-1},\qquad
K_{i,i+1}=-C_{c,i+1}^{-1},\qquad \Gamma=\operatorname{diag}(R_i).
$$
The drift is $-\Gamma^{-1}K$ and the full thermal diffusion covariance is $2T\Gamma^{-1}$. This preserves the equilibrium charge covariance $TK^{-1}$ even when the mobilities differ. Under $H_0$, only hidden entries of the diffusion covariance are removed; the drift is unchanged. We use the exact state-space model, not the unit-friction closed formula on a mismatched plant.

The measured private-capacitor voltage also changes with $C_{p,0}$. Its conversion factor $5/C_{p,0}$ and an independent detector gain factor are included. Ignoring this transduction change would underestimate capacitor-calibration sensitivity.

## Bandwidth and detector noise

The detector has one dynamical state,
$$
dz=\omega(q_0-z)dt+\omega\sqrt{S_{\rm in}}\,dW_D,\qquad
y_j=g\frac{5}{C_{p,0}}z(t_j)+\epsilon_j,
$$
where $\omega=2\pi f_c t_*$, the detector Wiener noise is independent of plant noise, and the output sample noise $\epsilon_j$ is independent Gaussian noise. The input white-noise PSD is fixed as the cutoff changes. At the nominal 100 Hz cutoff, 80% of the previously assumed detector noise variance is assigned to the filtered input and 20% to sample noise. This is an explicit assumed noise model, not an instrument characterization.

The detector state is **reset to known zero at record start**, while the circuit starts in thermal equilibrium. This avoids introducing an unrecorded prehistory through a detector state correlated with hidden coordinates. A physical reset must not disturb the circuit. If reset is unavailable, its initial state and cross-covariance need a separately calibrated model; none of the numerical budgets here covers that alternative automatically.

Records contain 401 samples over 200 ms, with 0.5 ms intervals. The augmented linear SDE is discretized exactly:
$$
F=e^{A\Delta t},\quad AS_h+S_hA^{\mathsf T}+D_h=0,\quad
Q_h=S_h-FS_hF^{\mathsf T},\qquad h\in\{0,1\}.
$$
Both hypotheses have the same initial covariance $P_*=\operatorname{diag}(TK^{-1},0)$. For $i\ge j$, the record covariance is
$$
(V_h)_{ij}=H F^{i-j}S_hH^{\mathsf T}
+H F^i(P_*-S_h)(F^j)^{\mathsf T}H^{\mathsf T}
+\sigma_{\rm out}^2\delta_{ij}.
$$
This includes the filter startup transient and the nonstationarity of $H_0$.

| Cutoff | Largest variance ratio | Model-test records | Depth-2 preparation KL under $H_1$, $J=1$ |
|---:|---:|---:|---:|
| 1 Hz | 1.63824 | 71 | 0.00597444 |
| 3 Hz | 1.63959 | 71 | 0.00658919 |
| 10 Hz | 1.64017 | 71 | 0.00684994 |
| 30 Hz | 1.64042 | 71 | 0.00690596 |
| 100 Hz | 1.64053 | 71 | 0.00691785 |
| 300 Hz | 1.64048 | 71 | 0.00691561 |

The covariance test predominantly uses a slow record mode, so these cutoffs barely affect its power under the assumed noise PSD. The small high-cutoff decline is allowed because increasing bandwidth also increases aliased input detector noise. These calculations do not imply that bandwidth never matters. The preparation KL at 1 Hz is about 14% below its 100 Hz value. Reoptimizing the projection for each cutoff is allowed only using calibration/model data before the held-out test.

At 100 Hz, multiplying both detector-noise standard-deviation scales by 3, 10, and 30 raises the covariance-test budget from 71 to **73, 96, and 445**, respectively. The assumed detector noise floor still needs measurement, particularly its low-frequency drift and correlations.

## Exact test and power calculation

Use calibration to select a fixed vector $w$ maximizing
$$
\lambda=\frac{w^{\mathsf T}V_1w}{w^{\mathsf T}V_0w}.
$$
It is a leading generalized eigenvector of $(V_1,V_0)$. Freeze it before seeing test data. Its coefficients and sample times are saved in `empirical/boundary60/stress/nominal_projection.npz`. At the nominal point, normalize $v_0=w^{\mathsf T}V_0w=1$; then $v_1=1.6405331214$.

For $N$ independent records, compute scalar scores $Z_i=w^{\mathsf T}Y_i$ and their sample variance $s_Z^2$. Center by their sample mean, so an unknown common preparation mean does not affect the test. Under a Gaussian model, $(N-1)s_Z^2/v$ is exactly chi-squared with $N-1$ degrees of freedom. Reject $H_0$ when
$$
\frac{(N-1)s_Z^2}{v_0}>\chi^2_{N-1,0.95}.
$$
The power under $H_1$ is exactly
$$
\mathcal P_N=1-F_{\chi^2_{N-1}}\left(\frac{\chi^2_{N-1,0.95}}{\lambda}\right).
$$
It is 0.89910 at $N=70$ and 0.90250 at $N=71$. These are finite-sample quantiles, not a normal approximation. The statistic is the standard Gaussian [chi-square variance test described by NIST](https://www.itl.nist.gov/div898/handbook/eda/section3/eda358.htm), applied to a model-selected projection of correlated time samples. Independence is required between entire trial records, not between samples within a record.

The reported $N$ is minimal for this fixed scalar variance test. It is not the globally minimum sample count among all tests: a full Gaussian likelihood-ratio test could use more than one record mode. The full-record $D(P_1\Vert P_0)$ is 0.30204 nats per trial at the nominal point, a different quantity from preparation KL.

## Shared calibration uncertainty

A calibration error is a fixed nuisance across the batch. Drawing it anew for each trial or dividing it by $\sqrt N$ would incorrectly make a systematic error disappear.

Suppose valid calibration bounds give $v_0\le v_0^+$ and $v_1\ge v_1^-$. Threshold using $v_0^+$ and calculate power using the least-favorable ratio $r=v_1^-/v_0^+$. If each nominal projected variance has a relative bound $u$, a sufficient choice is
$$
r=\lambda\frac{1-u}{1+u}.
$$

| Bound on each projected variance | Least-favorable ratio | Sufficient records, 5% size / 90% power |
|---:|---:|---:|
| Exact calibration | 1.64053 | 71 |
| ±2% | 1.57620 | 83 |
| ±5% | 1.48429 | 110 |
| ±10% | 1.34225 | 198 |
| ±15% | 1.21257 | 460 |
| ±20% | 1.09369 | 2,130 |
| ±25% | 0.98432 | No uniform guarantee for this one-sided test |

The symmetric envelopes touch at $u=(\lambda-1)/(\lambda+1)=24.2577\%$. Beyond this point increasing $N$ cannot guarantee the desired performance for this scalar test. This is not proof that every full-record test is unidentifiable; covariance shape may still discriminate the models.

If a ±10% envelope has at least 99% **joint coverage under either model**, based on independent calibration, use conditional size 4% and conditional power at least $0.90/0.99$. The exact chi-square calculation then gives **219 records**. Total size is bounded by $0.04+0.01=0.05$, and total power is at least $0.99(0.90/0.99)=0.90$. Calibration acquisition itself is not included in 219. Its cost cannot be inferred without a measurement model for the calibration instruments and the intended confidence construction.

## Mapping component tolerances to variance uncertainty

The script uses 45 nuisance parameters: individual resistances and capacitances, cutoff, gain, temperature, and two detector-noise scales. It evaluates central log sensitivities, targeted sign corners, and random parameter draws with the *same frozen projection*. The scenario boxes are symmetric in log parameters: $|\log(p/p_*)|\le\log(1+u_p)$.

| Scenario | Assumed residual calibration bounds | Tested range relevant to the robust ratio | Interpretation |
|---|---|---|---|
| Tight | Components 1%; cutoff 2%; gain 1%; temperature 0.5%; noise PSD/variance 10% | $v_0^{\max}=1.07172$, $v_1^{\min}=1.52993$ | Tested extremes require about 7.2% projected-variance allowance; rounded to a 10% target with margin |
| Loose | Components 5%; cutoff 10%; gain 3%; temperature 2%; noise PSD/variance 20% | $v_0^{\max}=1.34299$, $v_1^{\min}=1.21543$ | Overlap already occurs among tested cases; simple variance-threshold protection fails |

Each scenario includes the nominal point, four targeted corners, and 64 random points. These are not certified global extrema, and the added margin does not turn sampling into an interval proof. The exact conditional budgets above remain valid if their projected-variance bounds are established, but this study alone does not establish a 99% calibration-coverage claim.

The largest nominal log sensitivities are nearly common scale effects: gain has sensitivity about 2 under both models, the observed private capacitance about -1.75, and temperature about 1. A 1% uncorrected gain error therefore shifts the projected variance by about 2%. Boundary resistance is more model-dependent: sensitivities are about 0.97 under $H_0$ and 0.58 under $H_1$. Calibrate the boundary transduction and mobility before spending effort on deep interior tolerances.

The separate uncalibrated mismatch study drew 64 independent devices with each physical R/C component uniform within ±5%, while keeping detector and temperature parameters nominal. Applying the *nominal* threshold to these devices produced false-positive rates up to 21.49% and powers as low as 71.48%. These are observed stress-case extrema, not worst-case guarantees for every device in the box.

## Recommended acquisition order

1. Validate the detector reset model, low-frequency noise, loading, and the plant's calibrated response/FDT relation. Establish cross-trial independence with records not used for the test.
2. Freeze the projected score and a nuisance-aware null threshold. Obtain a valid projected-variance envelope; the tight component scenario is a target, not certification.
3. If a ±10% envelope with 99% joint coverage is established, acquire **220 independent unprepared reference records** for the bath-model pilot. Count calibration, reset validation, and failed acquisitions separately.
4. Only then acquire the depth-1/2 preparation trials needed to test absolute preparation visibility, saturation, and the predicted likelihood-score distributions. The small bath-model budget does not make the KL experiment equally cheap.

Do not interpret a failure to reject $H_0$ as confirmation, or a rejection as confirmation of all assumptions. Unexpected detector memory, bath correlations, or random preparation amplitude can also change covariance and must be separated from the intended effect.

![Prospective stress calculations](C:/Projects/simplicial/empirical/boundary60/stress/stress.png)

## Verification and remaining limits

`empirical/boundary60/experiment_stress.py` passed **7/7 declared checks on run 1**. The augmented thermal Lyapunov residual is $5.11\times10^{-15}$. Dense record covariances and an independent adjoint noise-accumulation calculation agree to relative $6.77\times10^{-16}$. A separate full-state exact-transition Monte Carlo with 12,000 trials under each hypothesis agrees with projected variances within 0.79 standard errors. Exact quantiles establish the scalar power threshold. Results, projection weights, CSV, and figures are in `empirical/boundary60/stress/`; the retained log is `stress_run1.log`.

Unmodeled amplifier backaction, charge leakage, colored bath noise, uncertain filter initialization, preparation jitter, and cross-trial drift are not covered by the numerical guarantees. The follow-up `60_visibility_two_mode_test.md` derives a two-mode variance-ratio test, including its exact correlated-pair law. The tested pair cancels common overall gain but does not improve the present budget: it needs 147 nominal records and 467 under its tight-scenario conditional coverage assumptions, versus 71 and 219 here. Retain this one-mode baseline pending a nuisance-aware comparison using more record modes or a better reference-mode selection rule.
