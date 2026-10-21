# Paper 60: focused novelty audit

*October 9, 2026. Primary-source comparison, not an exhaustive priority determination.*

## Finding that changes the positioning

Exponential chain-Gramian decay is established prior work. Klickstein and Sorrentino's *The controllability Gramian of lattice graphs*, Automatica 114 (2020), 108833, treats this directly. Its accessible preprint, *Optimal Input Placement in Lattice Graphs*, gives the diagonal decay factor in equations (20)–(21). [Published article](https://doi.org/10.1016/j.automatica.2020.108833); [preprint](https://arxiv.org/abs/1808.07750).

Their parameters map to ours as $p=-a$, $s=k$. Their $\alpha=a^2/(2k^2)-1$ is $\cosh(2\kappa)$, so
$$
\widetilde z=\alpha-\sqrt{\alpha^2-1}=e^{-2\kappa}.
$$
Thus even the exponent is shared. Paper 60's finite-chain uniform bounds transfer this spatial behavior to a different observable: full-record preparation KL with ongoing thermal noise. Do not advertise the exponent itself, or the factor-of-two decay length alone, as a new discovery.

## Closest comparisons

| Prior work and inspected evidence | Overlap | Candidate distinction of Paper 60 |
|---|---|---|
| Klickstein–Sorrentino, preprint §3 and published abstract, linked above | Lattice Gramians and exponential distance scaling | Thermal-noise information operator, finite-chain uniform bounds, and sharp contraction over a specified non-Gaussian deep-subspace preparation class |
| Harris et al., *Minimum requirements for feedback enhanced force sensing*, PRL 111 (2013), 103603; [paper](https://arxiv.org/abs/1303.1589) | Known feedback can be undone at the measurement-record level | An explicit residual transformation ties this established principle to the same preparation channel and spatial coefficient; not a new feedback-neutrality principle |
| Subaşı–Demirekler, *Quantitative Measure of Observability for Stochastic Systems*, IFAC 2011; [full conference paper](https://skoge.folk.ntnu.no/prost/proceedings/ifac11-proceedings/data/html/papers/0829.pdf); expanded Automatica 50 (2014), 1669–1674, [repository abstract](https://open.metu.edu.tr/handle/11511/58015) | Mutual-information observability for linear Gaussian state/measurement sequences | KL between two preparation-induced record laws, a fixed conditional thermal reference, and a worst-preparation contraction coefficient. Full conference paper inspected; journal full text not verified |
| Baram–Kailath, *Estimability and Regulability of Linear Systems*, IEEE TAC 33 (1988), 1116–1121; [NASA record](https://ntrs.nasa.gov/citations/19990111676), [technical report](https://ntrs.nasa.gov/api/citations/19870011357/downloads/19870011357.pdf) | Posterior improvement is distinct from deterministic observability | Do not claim that distinguishing observability from recoverability is new; our focus is a computable thermal KL ceiling |
| Powel–Morgansen, *Empirical Observability Gramian for Stochastic Observability of Nonlinear Systems*; [full preprint](https://arxiv.org/abs/2006.07451), introduction and references | Process noise changes the observability question; extensive earlier information-based notions | Exact linear thermal path experiment rather than an empirical nonlinear observability metric |
| Polyanskiy–Wu, *Strong data-processing inequalities for channels and Bayesian networks*; [paper](https://arxiv.org/abs/1508.06025) | Reference-dependent contraction, maximal correlation, and information contraction | The Gaussian contraction tool is standard. The network identification of its matrix is the application |
| Gross, *Logarithmic Sobolev Inequalities* (1975); [DOI](https://doi.org/10.2307/2373688) | Gaussian entropy contraction extends the ceiling beyond Gaussian input laws | Non-Gaussian validity should be presented as a consequence of a classical theorem, not an independent general SDPI discovery |
| *Informational Steady States and Conditional Entropy Production in Continuously Monitored Systems*, PRX Quantum 3 (2022), 010303; [paper](https://doi.org/10.1103/PRXQuantum.3.010303) | Information acquisition competes with environmental information loss | Our observable is initial-preparation distinguishability in the whole boundary record. A slogan about measurement competing with noise is insufficient novelty |
| Baiesi–Ciliberto–Falasco–Yolcu, *Thermal response of nonequilibrium RC-circuits*; [full preprint](https://arxiv.org/abs/1607.01531), §I | Experimentally measured thermal RC networks mapped to coupled overdamped harmonic coordinates | Establishes platform precedent, not our proposed chain experiment or validation of its assumed detector performance |

## Claim we can defend now

> For finite equal-temperature overdamped harmonic networks, we identify the exact Gaussian channel from hidden preparation to the entire boundary record. Its sharp Gaussian-reference KL contraction coefficient has a closed thermal form. In pinned chains this coefficient, restricted to an explicitly defined deep displacement preparation class, obeys finite-size-uniform bounds with the established lattice spatial exponent, and remains invariant under admissible boundary-only feedback.

This is a precise result to submit for expert comparison. The present search has not located the complete package in one earlier source, but that does not establish priority. The ingredients are strongly represented in existing control and information theory; reviewers may regard the combination as a useful specialization unless the physical prediction and validation are compelling.

## Statements to avoid

- “First spatial information screening law”: the deterministic Gramian exponent is already available by observability/controllability duality.
- “Feedback cannot improve measurement” without the ideal record and controller-information assumptions.
- “Cooling cannot help”: the ideal normalized coefficient is temperature independent; fixed physical preparations and detectors need not have temperature-independent KL.
- “Information loss is heat”: posterior KL slack has not been identified with a heat or entropy-production integral.
- “Every deep preparation is screened”: the complementary thermal modes and their independence are part of the preparation class.
- “The experiment confirms the theory”: there is no experimental data in this project yet.

## What would materially strengthen the paper

The proposed experiment should compare the exact finite-record likelihood with a calibrated alternative that omits ongoing hidden bath noise. Both can exhibit the same spatial exponential rate. A slope alone therefore cannot validate the thermal contribution. The discriminating evidence is the absolute visibility, its saturation with observation time, and its behavior under controlled changes to the observation channel.

The next literature pass should follow the references on stochastic reconstructibility (Liu–Bitmead), initial-state smoothing, and information-based observability, and inspect the published lattice article beyond the accessible preprint. The outcome should be a claim-by-claim comparison, not a tally of unmatched search terms. The experiment plan is in `60_visibility_experiment_protocol.md`.

## Search record and limits

Searches on October 9, 2026 covered lattice controllability/observability Gramians and exponential distance decay; Gaussian initial-state information and Riccati equations; stochastic observability and mutual information; feedback-neutrality in force sensing; and thermal RC experiments. Primary preprints, author-hosted papers, journal records, and institutional repositories were used. The published lattice article was accessible as a substantial preview; its preprint was read around the decay derivation. Negative search results are not evidence of absence. No claim is made about an exhaustive citation graph or unpublished work.
