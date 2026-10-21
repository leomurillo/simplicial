# Paper 60: a prospective thermal-circuit test

*October 9, 2026. Proposed apparatus and model predictions. No hardware has been built, no data have been acquired, and no detector specification has been validated.*

## Experimental question

Can an independently calibrated thermal network predict the distinguishability of two initial preparations from a boundary voltage record, including the loss caused by ongoing hidden thermal noise?

The first experiment should test absolute finite-record likelihoods at shallow depths and saturation in time. A spatial exponential slope alone is inadequate: the same exponent occurs in established lattice-Gramian results. See `60_visibility_literature_audit.md`.

## A passive RC mesh realization of the chain

Use $n+1$ planar meshes, labeled $0,\ldots,n$. Each mesh has one private series resistor $R$, one private capacitor $C_p$, and a calibrated series voltage-source port. Adjacent meshes share a capacitor $C_c$; each exterior mesh also has an end capacitor $C_c$. A concrete topology has a row of $n+2$ upper junctions, a capacitor $C_c$ from each junction to a common lower conductor, and a series $R,C_p$ branch between each adjacent pair of upper junctions. The $n+1$ windows are the mesh loops. Treat capacitances, input loading, and wiring parasitics explicitly during apparatus validation.

Let $q_i$ be oriented integrated mesh current, equivalently the charge on its private capacitor. With consistent orientations, a shared capacitor carries $q_i-q_{i+1}$. On the fixed-charge constraint sector the electrostatic energy is
$$
U(q)=\frac{1}{2C_p}\sum_{i=0}^n q_i^2
+\frac{1}{2C_c}\left[q_0^2+\sum_{i=0}^{n-1}(q_i-q_{i+1})^2+q_n^2\right].
$$
Thus $K_{ii}=C_p^{-1}+2C_c^{-1}$ and $K_{i,i+1}=-C_c^{-1}$. Each resistor is private to a mesh, so the dissipative matrix is $RI$ in these coordinates. At common temperature $\Theta$, ideal Johnson noise gives
$$
R\,dq=(-Kq+f)dt+\sqrt{2Rk_B\Theta}\,dW,
\qquad\Sigma_{\rm eq}=k_B\Theta K^{-1}.
$$
Measuring the voltage across the private capacitor in mesh 0 measures $q_0/C_p$. This construction is important: a generic node-voltage RC ladder need not have the independent-noise, unit-mobility structure of Paper 60.

Thermal RC experiments and their harmonic-coordinate mapping have precedent in Baiesi et al., [*Thermal response of nonequilibrium RC-circuits*](https://arxiv.org/abs/1607.01531). That paper supports the platform choice; the multi-mesh layout and component values here are a proposed extension requiring circuit-level review.

Set $\hat t=t/(RC_c)$ and $\hat q=q/\sqrt{k_B\Theta C_c}$. Then the drift is exactly the dimensionless chain used in the theorem, with $k=1$ and $m/k=C_c/C_p$.

| Proposed quantity | Value | Status |
|---|---:|---|
| Loops | 13: one boundary and 12 hidden | Illustrative design |
| Private resistance | $10\,\mathrm{M}\Omega$ | Assumed equal; calibrate each |
| Shared and end capacitance | $1\,\mathrm{nF}$ | Assumed ideal |
| Private capacitance | $5\,\mathrm{nF}$ | Gives $m/k=0.2$ |
| Common bath temperature | $300\,\mathrm K$ | Illustrative operating point |
| Time unit | $RC_c=10\,\mathrm{ms}$ | Derived |
| Recorded duration | $200\,\mathrm{ms}$ | Dimensionless horizon 20 |
| Sample interval | $0.5\,\mathrm{ms}$ | 400 intervals, including the initial sample |
| Detector RMS per sample | $32.6\,\mathrm{nV}$ on the private capacitor | Assumed white additive noise, not a verified instrument capability |

The detector assumption is 10% of the equilibrium RMS boundary voltage at the base temperature. Real detector noise has bandwidth and correlation; replace this white-sample model with a measured covariance or a calibrated detector state-space model before drawing experimental conclusions. Input capacitance, leakage, and amplifier backaction can change the physical plant and are not covered by treating the detector as a passive observation channel.

## Exact finite-duration mean preparation

Start in equilibrium. To create a mean displacement $\delta e_d$ without changing covariance, choose a smooth trajectory $\bar q(t)=s(t)\delta e_d$, where $s$ rises from 0 to 1 and $\dot s$ vanishes at both endpoints. Apply the deterministic voltage vector
$$
f(t)=R\dot{\bar q}(t)+K\bar q(t).
$$
Then the mean follows $\bar q$ exactly. The covariance remains $k_B\Theta K^{-1}$ because deterministic additive forcing does not change its evolution. Only mesh $d$ and its neighbors require forcing. Turn every preparation drive off at the record start. At that instant the boundary marginal is unchanged and the hidden conditional mean shift is exactly $\delta e_d$.

This avoids assuming an instantaneous ideal kick. It also avoids hidden-state feedback during readout. Preparation and calibration may access interior ports; the scored observation uses only the boundary record. The reference preparation is equilibrium. For target cost $J$ choose
$$
\delta=\sqrt{\frac{2k_B\Theta J}{C_p^{-1}+2C_c^{-1}}}.
$$
At the proposed operating point, $J=1$ nat needs $\delta=1.9405\,\mathrm{fC}$, or a $0.3881\,\mu\mathrm V$ shift on the target private capacitor. The script verifies a cubic ramp over dimensionless duration 0.4. Actual source noise and finite switching transients must be included in the independently measured preparation covariance.

## Calibrate before using preparation labels

Use separate calibration records to determine the response matrix, mobilities, equilibrium covariance, detector transfer function/noise, and the achieved preparation mean and covariance. All-node access during calibration is allowed; it is not part of the boundary-only inference record. Check whether the measured drift and covariance satisfy the intended equilibrium relation, rather than declaring an injected noise source to be thermal by its amplitude alone.

Freeze the analysis parameters before inspecting held-out labeled trials. Randomize prepared/reference labels and trial order, and keep source-drive traces and interior monitors out of the classifier. Establish sufficiently independent resets from measured cross-trial correlations; a waiting time estimated from relaxation is only a starting estimate. Estimate uncertainties of calibrated parameters and propagate them into predicted KL. The trial counts below treat these parameters as known and therefore omit that additional uncertainty.

## Exact observable and likelihood

For the ideal uncontrolled plant, define $F(t)=e^{-Kt/R}$ and $\Sigma=k_B\Theta K^{-1}$. For boundary charge-equivalent samples at times $t_i$, including 0,
$$
b_i=\delta\,e_0^{\mathsf T}F(t_i)e_d,\qquad
V_{ij}=e_0^{\mathsf T}F(|t_i-t_j|)\Sigma e_0+(V_{\rm detector})_{ij}.
$$
The two record laws have equal covariance $V$, means $b$ and zero, and exact sampled KL
$$
D_{\rm rec}=\tfrac12 b^{\mathsf T}V^{-1}b.
$$
Their log likelihood ratio is $\ell(y)=b^{\mathsf T}V^{-1}y-D_{\rm rec}$. Under the prepared law, $\ell\sim\mathcal N(D_{\rm rec},2D_{\rm rec})$; under the reference it has mean $-D_{\rm rec}$ and the same variance. This gives a directly testable score distribution, without a high-dimensional nonparametric KL estimator. A wrong calibrated model need not have these score moments, which is why held-out validation is essential.

For a common linear boundary feedback switched on at record start, propagate the original equilibrium initial covariance with the controlled drift and unchanged bath covariance; do not silently replace it by the controlled stationary covariance. The accompanying code implements this with exact matrix-exponential transitions. Its feedback sweep assumes noiseless boundary feedback; actual detector-driven feedback requires its measurement noise and any induced correlations in the closed-loop model. The ideal continuous-record theorem predicts equivalence; fixed-rate sampled and noisy records can differ under feedback. Such differences are not a violation of that theorem.

For a local variance-only preparation in the thermal displacement-mode family, with scalar variance ratio $w$, the same sampled channel has coefficient $\theta_{\rm rec}=D_{\rm rec}/J$ from a mean-shift calibration, and predicts
$$
D_{\rm variance}=\tfrac12\left[(w-1)\theta_{\rm rec}-\log(1+(w-1)\theta_{\rm rec})\right].
$$
This is an optional second-stage test; implementing such a preparation needs a separately validated covariance-control protocol.

## Prospective predictions and trial budget

The following are calculated predictions for the assumed detector, not observations. All rows use $J=1$ nat and the same record duration.

| Depth | Ideal infinite-time $D/J$ | Finite detector-record $D/J$ | Trials for 10% classification error | Trials for 20% KL precision at 95% |
|---:|---:|---:|---:|---:|
| 1 | 0.0490316 | 0.0481224 | 69 | 3,992 |
| 2 | 0.00697043 | 0.00695410 | 473 | 27,621 |
| 3 | 0.00178929 | 0.00178731 | 1,838 | 107,465 |
| 4 | 0.000549132 | 0.000548662 | 5,987 | 350,075 |
| 5 | 0.000183627 | 0.000183485 | 17,902 | 1,046,803 |
| 6 | 0.0000645135 | 0.0000644630 | 50,956 | 2,979,585 |

For $N$ independent records of the same unknown hypothesis, equal-prior optimal error is $\Phi(-\sqrt{ND_{\rm rec}/2})$. For estimating $D_{\rm rec}$ by the prepared-trial average of $\ell$, a 95% normal interval has relative half-width $1.96\sqrt{2/(ND_{\rm rec})}$. These two tasks have very different trial budgets. The precision column counts prepared trials only and excludes reference validation, calibration, resets, and drift controls. It is a baseline for this estimator, not a universal lower bound on all estimators of model parameters.

At depth 2, deleting hidden process noise in the comparison model predicts a visible fraction $0.00857554$ instead of $0.00695410$, about 23% higher. At depth 4 the corresponding excess is about 45%, but the data cost is much larger. The alternative is a diagnostic counterfactual, not an equilibrium model satisfying the same FDT. Merely seeing an exponential slope would not distinguish it from the thermal prediction. The follow-up `60_visibility_experiment_stress_test.md` now supplies an exact scalar covariance-test power calculation with finite detector bandwidth and shared calibration uncertainty. It finds that bath-model rejection is possible using unprepared records and is much cheaper than estimating preparation KL; these are distinct experimental tasks.

**Recommended first stage:** depths 1 and 2, several nested record horizons, and held-out score means/variances. Add depth 3 only after noise, reset independence, and parameter stability meet the analysis requirements. Use exact finite-chain predictions; shallow-depth slopes need not equal the asymptotic exponent. Boundary feedback is a secondary equivalence check. Temperature scans are secondary because component drift and fixed detector noise complicate the clean normalized invariance.

At fixed thermal-unit preparation and detector noise, the calculations collapse exactly across temperature. At fixed physical detector noise they do not: cooling lowers normalized visibility. At fixed physical displacement even the ideal input cost changes with temperature. These distinctions belong in the experimental claim.

![Prospective predictions](C:/Projects/simplicial/empirical/boundary60/experiment/predictions.png)

## Verification and deliverables

`empirical/boundary60/experiment_predictions.py` produced `experiment/predictions.json`, `experiment/depth_predictions.csv`, and PNG/SVG figures. **Seven declared checks passed on run 1.** Dense record inversion agrees with an independent innovations recursion to $1.53\times10^{-16}$; sampled/noisy records obey the ideal ceiling; denser ideal sampling improves information; temperature normalization and the fixed-detector exception behave as predicted; finite-ramp preparation agrees to $2.38\times10^{-14}$; and the prior lattice exponent maps exactly to ours. The log is `empirical/boundary60/experiment_run1.log`. These are author computations, not experimental validation.

The protocol is ready for an apparatus and inference-design review. The follow-up stress test gives a conditional 220-record bath-model pilot target if a ±10% projected-variance envelope with 99% joint calibration coverage can be established. Its sampled component scenarios do not certify that coverage. A SPICE-level parasitic/loading model, measured detector covariance, source-noise budget, and valid calibration uncertainty propagation remain necessary before purchasing or assembling a device. The preparation-KL trial budgets above remain a separate second stage.
