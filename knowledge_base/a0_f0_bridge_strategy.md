# A0-F0 Bridge Strategy

Created: 2026-05-14

Goal: close the gap between the exact finite Fisher skeleton at F0 and the
program attractor A0, universal information-investment modeling for prediction
and generative engines.

## Central Move

Insert one explicit bridge node:

> **B0: Information-investment functional.**  Given a categorical behavior
> space, a candidate finite discretization, and a resource budget, define the
> cost of a prediction engine as Fisher distortion plus closure leakage plus
> pullback defect plus resource expenditure.

Then the route is:

```text
F0 exact coordinates
  -> B0 information-investment functional
  -> A0 optimal discretization principle
```

F0 tells us which coordinates are not arbitrary.  B0 tells us what counts as
spending information well.  A0 is allowed to become theorem-facing only after
B0 has mathematical and empirical teeth.

## Balance-Transfer Descent Principle

The nested zero-sum hyperplanes

```text
H_N -> H_{N-1} -> ... -> H_2 -> ray
```

should be treated as an information-transfer ladder, not merely as a sequence
of linear subspaces.  Passing down one degree spends or releases a conserved
balance currency: the zero-sum condition is the rule that keeps the discarded
degree from becoming an untracked force.

In finite arithmetic language, this means a candidate discretization should
not only approximate the active translation spectrum.  It should also pay for
the lower conductor/divisor levels needed to make that spectrum stable under
Taylor multiplication, quotient shifts, and reciprocal-density coupling.

This gives B0 its first extra term:

```text
DescentBalanceCost(D)
```

A support that uses a higher conductor level while skipping lower
balance-transfer levels is cheap in dimension but expensive in closure.  A
support that descends through the needed conductor divisors is allowed to be
small without being brittle.  This is the finite version of harmonizing
discretized translation with discretized stretching.

## Two-Axis Descent: NZSBTL × PSL

The balance-transfer descent of the previous section is the *additive* (linear-
scale, simplicial-coordinate) descent.  It has a multiplicative (prime-power,
conductor) dual.  The two descents together carry the A0 program from a
single-axis lcm-conductor closure principle (B1-B4) to a joint two-axis
optimization principle.  This section formalizes the two axes and the
duality that connects them.

### NZSBTL (translation discretization)

Paper 10 Section 12 (Definition 12.1) defines the **Nested Zero-Sum Balance-
Transfer Ladder** of the simplicial frame on \(R\) as a maximal Fisher-
orthogonal flag

```text
H_R = H^(0) ⊃ H^(1) ⊃ ... ⊃ H^(N-2) = line
```

with each \(H^(k)\) a zero-sum subhyperplane of dimension \(N-1-k\).  The
balance currency at each step is one zero-mean Fisher coordinate (Paper 10
Proposition 12.2); the total budget is \(N-1\) Fisher-variance units.

NZSBTL is *conductor-respecting* (Paper 10 Definition 12.3) when each
one-dimensional summand \(L_k\) lies inside a single conductor packet
\(H_R^{[d_k]}\).  Conductor-respecting NZSBTLs are parameterized by
Proposition 12.4: choose a cross-packet ordering (a maximal PSL flag, see
below) and a Fisher-orthogonal flag inside each packet.

### PSL (stretching discretization)

Paper 11 §9.6 (Definition 9.6.1) defines the **Prime Spectral Ladder** as the
totally ordered set of nontrivial conductor levels

```text
PSL(R) = { (p, k) : p | |R|,  1 ≤ k ≤ d_p }
```

shuffled across primes, with within-prime depth giving the order.  The
prime-conductor depth of \(R\) is \(d(R) = sum_p d_p\); maximal PSL flags are
exactly the shuffles of the within-prime chains.

PSL lifts arity-by-arity to the hyper-adjacency suboperads of Paper 11
Proposition 9.6.2: each PSL step embeds the local hyper-adjacency operad at
one depth into the next, and across primes embeds the tensor product of
local operads into the CRT-glued global operad.

### Centroid duality (Paper 10 Theorem 12.7)

At \(p_*\), conductor-respecting NZSBTLs of \(H_R\) are in canonical
bijection with pairs (maximal PSL flag of \(R\), Fisher-orthogonal flag
inside each conductor packet).  The balance currency splits as

```text
sum over PSL levels  +  sum over within-packet flags
```

with cross-prime and within-prime contributions independent.  Pontryagin
duality identifies NZSBTL flags of \(H_R\) with subgroup flags of
\(\widehat R \setminus \{1\}\), and the centroid Fisher metric matches the
Plancherel inner product up to scale.  In short: at the centroid,
*translation discretization on \(H_R\)* and *stretching discretization on
\(\widehat R\)* are conjugate descents through the same finite Fisher
skeleton.

### Off-centroid carry obstruction (Paper 11 Theorem 9.6)

Along an \(m\)-flat ray \(p_* + th\), the failure of consecutive NZSBTL
levels to remain Fisher-orthogonal at order \(n\) decomposes as

```text
Carry_n = sum over PSL boundaries (d, d')  of   sum_{η ≠ 0} ĥⁿ(η) A_η^{d', d}
```

where \(A_\eta^{d',d}\) are the quotient-character adjacency operators of
Paper 11 Definition 2.1.  By Corollary 9.6.3, the carry is concentrated at
PSL boundaries; it vanishes inside any single conductor packet.  The binary-
floor case (n=1) is the conductor selection rule of Paper 10 Theorem 3.1;
higher arities are operadic composites generated by the binary floor
(Paper 11 Proposition 9.5.8 + Theorem 9.5).

### The unified two-axis functional \(\mathcal J_\infty\)

Combine the centroid duality with the off-centroid carry into a single cost:

```text
J∞(D; μ, Res)
  =  Σ_{n≥0} ‖Carry_n^{[L, M]}(h_μ)‖²
  +  λ_NZSBTL · depth_NZSBTL(L)
  +  λ_PSL    · depth_PSL(M)
  +  λ_Res    · Res(D).
```

The within-packet contributions to \(\mathrm{Carry}_n\) vanish at every
order (Corollary 9.6.3); convergence of the carry-sum is controlled by the
prime-conductor depth filtration of \(\widehat{h_\mu^n}\).  The two-axis A0
target reads:

> A0 (joint NZSBTL × PSL, bounded theorem on the current verified atlas).  Within a fixed finite categorical
> behavior class \(\mu\) and a fixed resource proxy, the minimum of
> \(\mathcal J_\infty\) over symmetry-compatible \((L, M)\) is attained on a
> joint NZSBTL × PSL refinement of the behavior algebra.  The minimizing
> depths are determined by the Fisher-energy rank of \(h_\mu\) on \(H_R\)
> (NZSBTL axis) and the prime-conductor depth of the subgroup generated by
> the reciprocal-density support of \(h_\mu\) in \(\widehat R\) (PSL axis).

### FC3 weighted split ledger

FC3-C adds the task-dependent scalarization needed to use
\(\mathcal J_\infty\) without erasing the local filtered-carry fields.  The
mixed-row scalar objective is admissible only if its local term uses either
the full-filtered audit mode

```text
lambda_full * full + lambda_support * support
```

or the visibility-partition mode

```text
lambda_support * support
+ lambda_H4 * H4
+ lambda_H3 * H3
+ lambda_hidden * remaining.
```

The convention is that `H4 + H3 + remaining = full`.  Therefore the aggregate
full term and the visibility partition are not independent carry masses unless
the full term is explicitly an external audit penalty.  At current certified
scope the local row-family ledger is

```text
full/support/H4/H3/remaining = 180555/0/6648/173404/503.
```

This is the bridge from the A0 functional to FC3 pricing: generated-subgroup
descent, normalizer premium, PSL boundary carry, local filtered carry, and
resource cost stay separate until a declared task weight vector prices them.

### Status by axis

- NZSBTL axis (single-axis closure): proved for cyclic \(R\) in B1; extended
  to finite abelian \(R\) in B2.
- PSL axis (single-axis closure): the conductor-lattice / hyper-adjacency
  embedding is proved in Paper 11 Proposition 9.6.2.
- Centroid joint duality: proved in Paper 10 Theorem 12.7.
- Off-centroid joint carry obstruction: proved in Paper 11 Theorem 9.6.
- Two-axis optimization (B6, the joint A0 statement): proved on cyclic and
  finite-abelian rows and on the currently verified mixed atlas by Paper 12
  Theorem 9.2.1 plus the per-row carry-vs-depth certificate.
- FC3 scalar pricing: bounded mixed-row scalarization is recorded in
  `knowledge_base/fc3_weighted_mixed_row_theorem.md`; it preserves the
  full/support/H4/H3/remaining carry split and keeps support-only pricing
  visibly insufficient for filtered-closure-sensitive tasks.

### N=4 / Cayley-Dickson as the prime-2 / depth-2 row

For \(R\) of order 4 (PSL has depth 2 over the single prime 2) and
\(\dim H_4 = 3\) (NZSBTL has length 3), the *additional* Hodge identification
\(H_4 \cong \Lambda^2 H_4^*\) (Paper 13 §2) makes a single axis vector
double as a 2-form, producing the simplicial cross product and the imaginary
quaternions.  At any other \((|R|, \dim H_R)\) the Hodge degree and the
prime-tower depth do not both match, and the analogue of the quaternionic
edge-frame algebra is not generally a division algebra.  The Cayley-Dickson
tower \(\mathbb R \to \mathbb C \to \mathbb H \to \mathbb O\) is one prime
family (the 2-tower) of A0's two-axis classification; cyclotomic and
Carlitz-Hayes function-field towers are analogous structures at other
primes.  See Paper 13 Remark 2.1.

## Why This Closes The Gap

F0 is a coordinate theorem: at maximum entropy the zero-sum simplicial gauge
slice, categorical Fisher tangent space, and additive-character conductor
resolution coincide; off-centroid coupling is governed by quotient characters.

A0 is an optimization claim: prediction engines should invest finite resources
in discretizations that linearize curvature and preserve useful structure.

The missing ingredient is a variational objective that turns "these are the
right coordinates" into "these are the efficient coordinates under a budget."

## Candidate Functional

For a task distribution \(\mu\), model family \(q_\theta(y\mid x)\), finite
output algebra \(R\), and candidate discretization \(\mathcal D\), define

```text
J(D) =
  FisherLinearizationError(D)
+ lambda_1 * ForbiddenReciprocalEnergy(D)
+ lambda_2 * ClosureLeakage(D)
+ lambda_3 * DescentBalanceCost(D)
+ lambda_4 * PullbackDefect(D)
+ lambda_5 * ResourceCost(D).
```

Interpretation:

- `FisherLinearizationError`: residual curvature/cubic error after projecting
  behavior onto the candidate finite skeleton.
- `ForbiddenReciprocalEnergy`: nonuniform block-orthogonality failure from the
  reciprocal-density theorem in Paper 10.
- `ClosureLeakage`: support leakage and full filtered leakage, tracked
  separately.
- `DescentBalanceCost`: missing lower conductor/divisor levels required by the
  nested zero-sum balance-transfer ladder.
- `PullbackDefect`: activation/parameter-map distortion relative to the
  behavior-side Fisher skeleton.
- `ResourceCost`: rank, parameter count, FLOPs, latency, energy, memory, or
  sample complexity, depending on the experiment.

The first theorem target is not "this is the universal objective."  The first
target is:

> Within a fixed finite behavior class and fixed resource proxy,
> conductor/quotient-character discretizations minimize \(J\) among
> symmetry-compatible discretizations whenever the task distribution is
> generated by the corresponding finite skeleton.

That is a reachable theorem.  Universality comes later by approximation and
transfer, not by proclamation.

## Theorem Ladder

| Step | Rank | Statement | Current status |
|---|---|---|---|
| B0.1 | definition | Define \(J(\mathcal D)\) with separate Fisher, leakage, pullback, and resource terms. | open |
| B0.2 | theorem | At \(p_*\), the conductor resolution is the minimal translation/Galois-invariant Fisher diagonalization. | mostly F0/T6 |
| B0.3 | theorem | Off-centroid forbidden reciprocal energy exactly measures fixed-block orthogonality failure. | Paper 10 Proposition 6.1A |
| B0.4 | finite lemma | Quotient-character adjacency is the minimal closure object for Fisher Taylor couplings up to a fixed arity. | strong, needs proof extraction |
| B0.5 | definition/theorem target | Descent-balance cost is the missing conductor/divisor closure required by nested zero-sum transfer. | prototype landed |
| B0.6 | theorem/protocol | If pullback defect is bounded, behavior-side closure/leakage bounds transfer to the learned representation. | open |
| B0.7 | empirical theorem-candidate | Lower \(J\) predicts better resource-performance tradeoffs than random, PCA, or generic Fourier bases. | open |
| B0.8 | definition | NZSBTL: maximal Fisher-orthogonal flag of zero-sum subhyperplanes of \(H_R\) terminating in a line, with one zero-sum balance-currency unit per descent step. | Paper 10 Definition 12.1, Proposition 12.2 |
| B0.9 | definition | PSL: totally ordered shuffle of within-prime conductor depth chains, with prime-conductor depth \(d(R)=\sum_p d_p\). | Paper 11 Definition 9.6.1; PSL embeds in hyper-adjacency by Proposition 9.6.2 |
| B0.10 | theorem | Centroid Pontryagin duality: conductor-respecting NZSBTLs of \(H_R\) biject with (maximal PSL flag, within-packet Fisher-orthogonal flag) pairs; cross-prime and within-prime currencies are independent. | Paper 10 Theorem 12.7 |
| B0.11 | theorem | Off-centroid carry obstruction: the failure of NZSBTL Fisher-orthogonality at order \(n\) is concentrated at PSL boundaries and is an operadic composite of binary-floor quotient-shift operators. | Paper 11 Theorem 9.6; Corollary 9.6.3 (conductor-pure rays carry no obstruction at \(n=1\)) |
| B0.12 | theorem on cyclic/abelian + verified mixed atlas | Joint two-axis A0 (Paper 12 Theorem 9.2.1): the unique minimizer of \(\mathcal J_\infty\) is the joint NZSBTL\(\times\)PSL refinement with NZSBTL depth = \(\sum_{p,\mathfrak d}k_{\mathfrak d}^*\) and PSL depth = \(\sum_p d_{\mathrm{PSL}}^*(p)\), up to within-packet orthogonal freedom.  The per-row hypothesis \((\dagger_p)\) holds on every cyclic and finite-abelian row (B1/B2) and on every mixed local atlas row computed so far: F_4[u]/(u^2) at λ_PSL_crit = 55.4, F_2[u]/(u^4) at 2.00, F_2[u]/(u^5) at 2.00, F_8[u]/(u^2) at 924.  Joint A0 holds unconditionally on the Paper 11 atlas at every λ_PSL < 2.00 (the binding row). | Theorem; full 6-step proof in Paper 12 §9.2 + direct finite verification in `empirical/verify_per_row_carry_vs_depth.py`; `empirical/reports/per_row_carry_vs_depth.md` |

## First Prototype

Implemented:

- `empirical/information_investment_functional.py`
- `empirical/reports/information_investment_functional.md`
- `empirical/reports/information_investment_functional.json`
- `empirical/information_investment_frontier.py`
- `empirical/reports/information_investment_frontier.md`
- `empirical/reports/information_investment_frontier.json`

The prototype scores exact finite rows by

```text
J(D) =
  fisher_projection_error
+ reciprocal_projection_error
+ closure_leakage
+ descent_balance_cost
+ resource_weight * resource_cost.
```

First readings:

- `C7`: prime rows force the whole prime spectral family if closure and
  descent-balance are required.  This is a control, not a compression win.
- `C8`: the top-socle mode is already closed; the one-mode conductor support
  wins.
- `C12`: raw active support `{3,9}` is not enough; B0 selects the descent
  closure `{3,6,9}`, paying for the missing balance-transfer mode without
  buying the full space.
- `F4[u]/(u^2)`: the conductor-`u` packet is already closed and wins against
  low-index/random supports.

## First Frontier Audit

The frontier audit samples train and held-out finite tasks.  It compares
descent/conductor supports against learned aggregate top-Fisher-energy supports
under the same support budget.

First readings:

- `C7`: prime rows remain controls; closure collapses to the whole nontrivial
  prime family.
- `C8`: descent closure and learned same-budget support agree on average,
  because the train energy ranking discovers the same top-socle closures.
- `C12`: descent closure wins clearly on held-out tasks.  The learned
  same-budget energy support misses balance-transfer modes, so it has nonzero
  projection, reciprocal, closure, and balance cost.
- `F4[u]/(u^2)`: descent closure wins on mixed local tasks, with the
  allowed-reciprocal packet winning only when the held-out task lies inside the
  conductor-`u` closed locus.

This is the first A0-facing evidence that B0 is not merely repackaging energy
ranking: the structural closure policy can beat a learned low-rank support with
the same dimensional budget.

## First Theorem Family

The cyclic family is now theorem-facing.  For \(C_N\) and reciprocal Fourier
support \(S\), B0 descent closure is

```text
D_N(S) = { k != 0 : cond(k) divides lcm(cond(S)) }.
```

Equivalently, \(D_N(S)\cup\{0\}\) is the unique subgroup generated by \(S\).
It is the unique minimum-resource support with zero reciprocal projection,
zero Fisher projection, zero closure leakage, and zero descent-balance cost.
See `knowledge_base/b0_cyclic_descent_theorem.md` and
`empirical/reports/cyclic_b0_descent_theorem.md`.

## Second Theorem Family

The finite-abelian family sharpens the cyclic theorem.  For a finite abelian
character group \(G\), B0 descent closure is simply

```text
D_G(S) = <S> \ {0}.
```

This is the unique minimum-resource zero-structural-cost support.  In cyclic
groups it reduces to the lcm-conductor formula.  In noncyclic products and
local additive rows, lcm/order saturation and conductor-rank saturation can
overbuy.  This separates minimal information investment from optional
symmetry-complete modeling.  See
`knowledge_base/b0_abelian_descent_theorem.md` and
`empirical/reports/abelian_b0_descent_theorem.md`.

## Third Theorem Family

The normalizer-saturated policy adds symmetry completion as a separately priced
investment.  For a normalizer action \(\Gamma\),

```text
D_G^Gamma(S) = < Gamma . S > \ {0}.
```

This is the unique minimum-resource support that contains the active support,
is additively closed, and is \(\Gamma\)-invariant.  The difference
\(|D_G^\Gamma(S)|-|D_G(S)|\) is the symmetry premium.

First readings:

- cyclic rows have zero premium: generated subgroups are already
  unit-normalizer invariant;
- local rows have positive premium: normalizer completion can buy conductor
  orbits or even full local additive rows;
- frontier audits now show `normalizer_saturation` separately from
  `descent_closure`, so B0 can ask whether symmetry is worth its resource cost.

See `knowledge_base/b0_normalizer_investment.md` and
`empirical/reports/normalizer_b0_investment.md`.

## First Transfer Policy

The transfer audit turns the B3 premium into a decision rule.  If held-out tasks
range over normalizer transforms of a source task, pay for B3 exactly when

```text
expected structural transfer gain > resource-weighted symmetry premium.
```

Implemented:

- `empirical/normalizer_transfer_audit.py`
- `empirical/reports/normalizer_transfer_audit.md`
- `empirical/reports/normalizer_transfer_audit.json`

First local-row results:

- `F4[u]/(u^2)`: B3 beats B2 on `0.812` of transfer cases; mean net gain
  `1.330668`.
- `F2[u]/(u^4)`: B3 beats B2 on `0.799` of transfer cases; mean net gain
  `1.230162`.

See `knowledge_base/b0_symmetry_transfer_audit.md`.

## Learned Behavior/Update Audit

Implemented:

- `empirical/learned_behavior_b0_b4_audit.py`
- `empirical/reports/learned_behavior_b0_b4_audit.md`
- `empirical/reports/learned_behavior_b0_b4_audit.json`

This is B5: an empirical protocol, not a theorem.  It consumes the saved
weekday/month learned behavior tables, the activation-pullback reports, the
calendar transformer update reports, and the `F4[u]/(u^2)` optimizer reports.
For each learned artifact it keeps three quantities separate:

- behavior-side active support inferred from probability/reciprocal Fourier
  energy;
- B2 minimal subgroup descent;
- B3 normalizer saturation and full conductor/filter saturation.

First readings:

- Llama weekday and month behavior tables have broad reciprocal support at the
  default `0.01` energy threshold.  Their B2 cyclic closure is already the full
  nontrivial row, so B3 adds no symmetry premium and there is no compression
  win in these final behavior tables.
- C12 calendar update filters can suppress leakage relative to the declared
  filter and sometimes improve held-out metrics, but the non-full filters are
  generally not B2 subgroup-closed.  They are update-side filter evidence, not
  exact-support descent evidence.
- The `F4[u]/(u^2)` optimizer support is genuinely B2 closed: `7` nontrivial
  modes out of `15`, with near-zero final leakage and better KL than Adam in
  the saved run.  B3 normalizer saturation would buy the full local row; the
  transfer gain is currently a support-level estimate, not a direct learned
  deployment measurement.

B5 therefore advances item 9 below but does not solve A0.  It mainly clarifies
which learned artifacts are behavior-side full-support evidence and which are
update-side projection evidence.

## Direct Learned B4 Pressure Test

Implemented:

- `empirical/learned_normalizer_transfer_experiment.py`
- `empirical/reports/learned_normalizer_transfer_f4_u2.md`
- `empirical/reports/learned_normalizer_transfer_f4_u2.json`

This is the first direct learned version of the B4 transfer criterion.  It
uses `F4[u]/(u^2)` context-logit tables because that row has a real B2/B3
resource split.  For each source support, the experiment samples held-out
normalizer-transformed target distributions, trains stochastic Adam updates
under source-declared support policies, and compares measured target KL against
the resource premium.

First reading at resource weight `0.25`:

- source B3 covers the target support in the sampled transfer cases and lowers
  KL relative to source B2;
- the mean measured KL gain is only `0.072084`, while the mean
  resource-weighted B3 premium is `0.212500`;
- the mean net gain is therefore `-0.140416`, and B3 beats B2 by measured
  `J = KL + resource_weight * resource` on `0.000` of cases;
- the implied break-even resource weight is about `0.084805`;
- oracle target B2 wins all cases, which supports the B2 "minimal prediction
  investment" reading when the target transform is known.

This is an important negative result.  It does not refute B4; it applies B4:
at the current learned-update scale and resource price, the symmetry premium is
not paid back.  B3 is representationally correct but over-expensive.  The next
A0 step is a resource-weight/signal/sample frontier, followed by a shared
parameterization or checkpoint experiment where symmetry can transfer more
than support coverage.

## Best Route

1. **Define the functional before broadening claims.**  \(\mathcal J_\infty\) is
   now precise on finite categorical \(\mu\) (Paper 12 §9.2); the carry-sum is
   concentrated on PSL boundaries by Corollary 9.6.3, and FC3-C supplies the
   admissible weighted split ledger for current certified local rows.
2. **Prove the clean finite case.**  B1-B2 prove the cyclic/abelian one-axis
   minimizer; the joint two-axis statement (B6) reduces to bounding the
   carry-sum against the resource-weighted PSL depth on each local atlas row.
3. **Add adversarial controls.**  Scramble labels, use random bases, use PCA
   bases, use generic Fourier bases that ignore the conductor lattice, and use
   *NZSBTLs that violate conductor-respect* (i.e., mix packets inside a single
   descent line) as a structural baseline — Theorem 12.8 predicts a strictly
   larger carry-sum for such NZSBTLs.
4. **Attach resource metrics.**  The two-axis depths \((d_{NZSBTL}, d_{PSL})\)
   are the structural resources; rank, memory, latency, sample count, energy
   are the engineering resources.  The frontier is on the joint pair
   \((\lambda_{NZSBTL}, \lambda_{PSL}, \lambda_{Res})\).
5. **Then pull back through models.**  Measure how much of the behavior-side
   two-axis efficiency survives activation maps, parameter maps, and
   stochastic optimization.  GFWSVD (Paper 12 Theorem 1.1.6) already supplies
   PSL-axis efficiency automatically at Hayes-equivariant population-loss
   optima; the within-packet NZSBTL flag is the new measurable quantity for
   the learned/representation side.

## Minimal Experiments

| Experiment | Purpose | Win condition | Falsifier |
|---|---|---|---|
| finite synthetic rows | isolate F0 -> B0 without neural confounds | conductor/quotient basis minimizes \(J\) and resource cost | random/PCA basis wins |
| C7 prime control | test curvature without mixed carry | finite basis predicts Fisher/Hellinger behavior but no Ext leakage | Ext-like leakage appears after controls |
| C12/months mixed row | test CRT/conductor investment | closed packets improve leakage-resource frontier | projection hides loss or no resource gain |
| F4[u]/u2 optimizer | test tame/wild carry closure | update projection improves leakage and loss/resource Pareto | leakage falls but loss/resource worsens |
| activation pullback audit | test transfer from behavior to model | bounded pullback defect predicts where projection helps | pullback defect swamps finite skeleton |

## Publication Consequence

The first A0-facing paper should not claim universal generative-engine
optimality.  It should claim:

> A finite information-investment functional can be defined on structured
> categorical behavior spaces.  In exact finite rows, its minimizers are the
> quotient-character/conductor discretizations forced by Fisher geometry.

That is the bridge paper.  It is modest enough to be true and strong enough to
make A0 visible.

## Disconfirmation Questions

1. Does \(J\) merely repackage conductor assumptions, or does it choose the
   conductor basis from observable data?
2. Do generic low-rank bases beat quotient-character bases under the same
   resource budget?
3. Does nonuniform reciprocal energy predict real leakage outside exact rows?
4. Does closure leakage correlate with energy, latency, rank, or sample
   complexity?
5. Does learned pullback distortion destroy the exact finite advantage?

## Immediate Work Items

1. Add B0 to the claim graph between F0 and A0.
2. Done: create `empirical/information_investment_functional.py` for finite
   behavior tables with pluggable basis/discretization choices.
3. Done: run the first finite synthetic benchmark on `C7`, `C8`, `C12`, and
   `F4[u]/(u^2)`.
4. Done: add learned low-rank multi-sample baselines via the frontier audit.
5. Done: turn the frontier observations into the cyclic B0 descent theorem.
6. Done: generalize the theorem shape from cyclic rows to finite abelian
   groups and local additive rows.
7. Done: add normalizer-saturated variants so we can choose between minimal
   investment and symmetry-complete investment.
8. Done: connect the symmetry premium to finite transfer.  B3 wins when
   transfer gain exceeds resource-weighted premium.
9. Done: move the same policy into a learned behavior/update audit, with exact
   support evidence and learned artifacts kept separate.
10. Done: run a direct learned normalizer-transfer deployment experiment.  At
   resource weight `0.25`, B3 does not pay for itself in the `F4[u]/(u^2)`
   context-logit table.
11. Next: sweep resource weight, signal scale, sample count, and shared
   parameterization to locate the B2/B3 break-even frontier.
12. Promote only the finite-row result to manuscript language; keep learned
   model transfer as protocol until the pullback audit stabilizes.
13. Done: formalize the NZSBTL (Paper 10 §12) as the additive descent axis of
   the A0 functional.
14. Done: formalize the PSL (Paper 11 §9.6) as the multiplicative descent axis
   and lift it arity-by-arity to the hyper-adjacency operad.
15. Done: prove the centroid Pontryagin duality between NZSBTL and PSL
   (Paper 10 Theorem 12.7) and the off-centroid carry obstruction
   (Paper 11 Theorem 9.6).
16. Done: write the joint two-axis information-investment functional
   \(\mathcal J_\infty\) explicitly (Paper 12 §9.2) and state the joint A0
   theorem-target with depth formulas in both axes.
17. Done: identify the \(N=4\) Cayley-Dickson row as the prime-2/depth-2
   instance of the general two-axis classification (Paper 13 Remark 2.1).
18. Done: prove the joint A0 minimum analytically.  Paper 12 Theorem 9.2.1
   reduces the joint statement to a per-row carry-vs-depth inequality
   \((\dagger_p)\) via a 6-step proof (currency split → carry concentration
   → within-packet SVD → generated-subgroup PSL → CRT separation → resource
   monotonicity).  On cyclic and finite-abelian rows \((\dagger_p)\) holds
   unconditionally by B1/B2.
19. Done: verify \((\dagger_p)\) on each mixed local atlas row.  The verifier
   `empirical/verify_per_row_carry_vs_depth.py` evaluates
   \(\sum_n\|\mathrm{Carry}_n\|_F^2\) for every Fourier-pure test
   displacement and every shallow PSL flag, and reports the per-row
   break-even \(\lambda_{\mathrm{PSL}}^{\mathrm{crit}}(R)\).  Output:
   `empirical/reports/per_row_carry_vs_depth.md/json`.  Eight rows
   sweeping residue degree \(\deg(\kappa)\in\{1,2,3,4\}\) and wild depth
   \(d_{\max}\in\{2,3,4,5\}\) (residue-1 axis only):
   F_2[u]/(u^2) = 2.125, F_2[u]/(u^3) = 2.0078, F_2[u]/(u^4) = 2.00049,
   F_2[u]/(u^5) = 2.0000305, F_4[u]/(u^2) = 55.41, F_4[u]/(u^3) = 36.59,
   F_8[u]/(u^2) = 924.04, F_16[u]/(u^2) = 10950.  All strictly positive:
   (†_p) holds on every mixed row of the verified atlas, and joint A0
   holds unconditionally at every λ_PSL < 2.0000305 (the binding
   F_2[u]/(u^5) row).
20. Done: characterize the resource-weight phase boundary.  Two
   monotonicities cooperate.  At fixed wild depth 2, λ_PSL_crit is
   strictly monotone *increasing* in residue degree
   (2.125 < 55.41 < 924.04 < 10950), so larger residue fields afford
   strictly greater tolerance.  At fixed residue field, λ_PSL_crit is
   strictly monotone *decreasing* in wild depth — the F_2[u]/(u^n)
   sequence sweeps 2.125, 2.0078, 2.00049, 2.0000305 from n=2 to 5
   (asymptoting to 2 from above on the verified slice), and the F_4 row
   drops from 55.41 to 36.59 between u^2 and u^3.  Operational A0
   trust frontier: λ_PSL < 2.0000305 is unconditional on the verified
   atlas; above the depth-matched F_2[u]/(u^n) break-even, shallower PSL
   begins to pay on residue-1 wild-stress rows first.
21. Done: the previously-flagged deeper mixed rows F_4[u]/(u^3) and
   F_16[u]/(u^2) are included in item 19; both satisfy (†_p)
   (36.59 and 10950).  Residue degree pushes λ_PSL_crit *up*, wild depth
   pulls it *down*; the trust frontier is set by the residue-1
   wild-stress sequence, not by large-residue rows.  Open follow-up:
   prove inf_{n} λ_PSL_crit(F_2[u]/(u^n)) = 2 (currently a 4-point
   empirical pattern with the closed form 2 + 2^{5-4n} matching the
   n_max=4 truncation exactly), and converge the carry-series
   truncation past n_max=4 for the shallow-depth-large-residue rows
   (where higher n_max raises the values, e.g. F_16[u]/(u^2) from 10950
   to ≈23229 at n_max=16; the monotonicities and binding sequence
   are stable).
22. Done: add FC3-C weighted mixed-row scalarization.  The admissible scalar
   ledger keeps generated-subgroup descent, normalizer premium, PSL carry,
   full filtered carry, support projection, H4-visible mass,
   H3-contraction-visible mass, remaining hidden mass, and resource cost as
   distinct fields.  It imports the current exact local ledger
   `180555/0/6648/173404/503` and forbids support-only pricing from being read
   as filtered closure.
