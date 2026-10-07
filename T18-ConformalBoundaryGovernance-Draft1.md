# T18 - Conformal Boundary Governance

**Distribution-Free Validity for Representation Closure, Belief Updating, and Action**

**Leonardo Murillo Montero**

*First draft - May 26, 2026*

---

> *Closure should not merely be discovered. Closure should be governed.*

---

## Abstract

**Situation.** T0-T17 developed a finite mathematical architecture for
projection, boundary, closure, renormalization, curvature, continuum
completion, learned representation, active inference, and governed action. The
central repeated mechanism is now visible. A finite system chooses a retained
sector \(S\). If \(S\) is not closed under the relevant interactions, the
missing terms return as boundary residuals. T11-T13 showed that the boundary
can be completed by finite conductor fusion. T14 showed that curvature and
Noether defect are projection-boundary obstructions. T15 showed that open
systems require terminal boundary completion. T16 showed that learned
intelligence is representation closure under capacity and governance. T17
showed that belief updating should follow packet-resolved boundary surprise,
not scalar surprise alone.

**Gap.** Discovery is not enough. If every surprising residual is allowed to
change the representation, the system overfits noise, admits shortcuts, routes
unsafe completions, and acts on unstable evidence. If surprise is suppressed
globally, the system misses real structure. The missing principle is not another
closure operator. The missing principle is a finite-sample law deciding when a
closure move is allowed.

**Action.** We introduce **Conformal Boundary Governance**. A boundary score is
turned into a calibration ledger. The ledger produces finite-rank p-values and
boundary belief sets. Closure updates, packet admissions, external actions,
tool calls, memory writes, and policy changes are allowed only when the relevant
boundary completion is conformally admitted. The central rule is
\[
\boxed{
\text{do not govern raw surprise;}
\qquad
\text{govern boundary completion.}
}
\]

**Result.** We prove nine structure theorems. First, the **Boundary Scores Are
Conformal Scores Theorem**. Second, the **Boundary Calibration Ledger
Theorem**. Third, the **Conformal Boundary Set Theorem**. Fourth, the
**Conformal Update Gate Theorem**. Fifth, the **Mondrian / Conductor-Conditional
Boundary Theorem**. Sixth, the **Boundary Efficiency Theorem**. Seventh, the
**Conformal Active-Inference Policy Theorem**. Eighth, the **Adaptive
Exchangeability / Martingale Boundary Theorem**. Ninth, the **Conformal Closure
Governance Theorem**.

**Top claim.** Under exchangeability of calibration and deployment episodes
within the declared boundary ledger cell, every conformally governed closure
move has finite-sample error control. Under boundary-score separation, the
governed system converges from valid ambiguity to valid action. Thus T18 turns
the T-series from a theory of closure into a theory of lawful closure:
\[
\boxed{
\text{valid finite intelligence}
=
\text{representation closure}
+
\text{boundary calibration}
+
\text{conformal governance}.
}
\]

**Keywords:** conformal boundary governance, representation closure, finite
sample validity, boundary score, conformal set, update gate, conductor-conditional
calibration, active inference, policy governance, exchangeability, martingale,
adaptive architecture, alignment.

---

## Cross-references from prior papers

| Cited result | Used for |
|---|---|
| T0 gauge selection and apex generator | Scores depend on the chosen gauge/observable sector |
| T1 native simplicial chart | Finite state spaces and probability ledgers |
| T2 cumulant tower | Connected residuals and interaction order |
| T3 character orthogonality | Packet decompositions and conductor channels |
| T11 apex vertex calculus | Boundary packets and fusion completion |
| T12 finite apex determinacy | Finite spectral support of observable towers |
| T13 exact simplicial renormalization | Boundary integration and closure flow |
| T14 projected flatness | Curvature, beta source, and Noether defect as boundary obstructions |
| T15 finite-to-archimedean completion | Open boundary completion and terminal correction |
| T16 representation closure | AI systems as projection-completion architectures |
| T17 active boundary inference | Packet-resolved free energy and policy selection |

---

## 0. The Steelthread

The paper has one thread:

\[
\boxed{
\text{boundary detection tells us what could be completed;}
\quad
\text{conformal governance tells us when completion is allowed.}
}
\]

The nine milestones are:

1. Boundary scores are conformal scores.
2. Boundary scores live in calibration ledgers.
3. Calibration ledgers produce conformal boundary sets.
4. One-sided null ledgers produce update gates.
5. Conductor/Mondrian ledgers give sector-conditional validity.
6. Boundary scores improve efficiency when they separate structure from noise.
7. Active policies can be governed by conformal boundary sets.
8. Persistent violation of exchangeability is a boundary signal.
9. Closure, calibration, and governance form the final finite architecture.

The paper is deliberately finite. There is no asymptotic promise hidden in the
main theorems. The main validity statements are rank statements in finite
ledgers.

---

## 1. Basic Setting

Let \(\Omega\) be a finite state or data space. Let
\[
H=\mathbb R^\Omega
\]
be the full observable space. A finite system retains a sector
\[
H_S\subseteq H.
\]
The retained sector supplies the system's current representation, model, or
belief state. A task interaction, loss, or observation functional is denoted
\[
V.
\]

The T-series boundary principle says that the retained sector is incomplete
when
\[
V(H_S)\not\subseteq H_S.
\]
The missing part is a boundary:
\[
\partial S
=
\operatorname{supp}\big((I-\Pi_S)V(H_S)\big),
\]
where \(\Pi_S\) is the projection onto the retained sector. In packet language,
\[
\partial S\subseteq \{\beta_1,\ldots,\beta_m\}.
\]

A **boundary completion** is a move
\[
S\longmapsto S+\beta
\]
or more generally
\[
S\longmapsto \operatorname{Cl}_{\mathcal B}(S),
\]
where \(\mathcal B\subseteq\partial S\) is a packet set.

T18 asks:

\[
\boxed{
\text{When is the system allowed to make this move?}
}
\]

The answer is not "whenever surprise is high." The answer is:

\[
\boxed{
\text{when the boundary completion is conformally admitted by a calibration
ledger.}
}
\]

---

## 2. Episodes, Regimes, and Scores

An **episode** is a finite object
\[
Z=(X,Y,E)
\]
containing whatever the task makes available: observations \(X\), labels or
outcomes \(Y\), and evidence windows \(E\). Examples include:

- a prediction instance;
- a block of residuals;
- a belief-update episode;
- a policy-evaluation episode;
- an interaction with a tool or memory system;
- a boundary verification window.

The episode has an associated regime
\[
h(Z)\in\mathcal H.
\]
The regime space \(\mathcal H\) may contain labels such as:

\[
\mathcal H
=
\{\mathrm{noise},\mathrm{structural}\},
\]
or packet completions:
\[
\mathcal H
=
\{\varnothing,\beta_1,\ldots,\beta_m\},
\]
or policy regimes:
\[
\mathcal H
=
\{\mathrm{skip},\mathrm{inspect},\mathrm{update},\mathrm{defer}\}.
\]

A **boundary score** is a measurable map
\[
s:Z\mapsto\mathbb R
\]
whose direction is fixed in advance. Throughout the main text, larger scores
mean stronger evidence for a boundary completion. If a score is naturally a
nonconformity score where smaller is better, reverse the inequalities. Nothing
depends on this convention.

Important scores from T17 are:

### Scalar Surprise

\[
s_{\mathrm{scalar}}(Z)
=
\mathcal S_S(Z).
\]

This is the retained model's total surprise. It is generally not a good
boundary score because noise and structure may have the same scalar surprise.

### Boundary Residual Score

\[
s_{\partial}(Z)
=
\max_{\beta\in\partial S}
\left|
\left\langle
R_S(Z),\beta
\right\rangle
\right|,
\]
where \(R_S\) is the retained residual.

### Boundary Gain Score

Let \(\hat\beta(Z)\) be the packet selected by evidence data. Let \(V\) be a
verification window. Define
\[
s_{\Delta A}(Z)
=
\mathcal L_S(V)
-
\mathcal L_{S+\hat\beta}(V).
\]

This is the operational score used by the T17 experiments: not merely "which
packet correlates with residuals," but "which packet improves held-out
accuracy after paying for closure."

### Policy Gain Score

For a policy \(\pi\), define
\[
s_{\pi}(Z)
=
U(\pi_{S+\hat\beta};Z)-U(\pi_S;Z),
\]
where \(U\) is utility, reward, negative expected free energy, or governed task
value.

These scores are not assumed correct. They are candidates. Conformal governance
does not certify that a bad score is semantically good. It certifies validity
relative to the score and ledger supplied. This distinction is the main
discipline of T18.

---

## 3. The Finite Rank Lemma

The following lemma is the only probabilistic engine needed in the paper.

### Lemma 3.1. Finite Rank Superuniformity

Let
\[
S_1,\ldots,S_n,S_{n+1}
\]
be exchangeable real random variables. Define the one-sided rank p-value
\[
p(S_{n+1})
=
\frac{
1+\#\{i\le n:S_i\ge S_{n+1}\}
}{
n+1
}.
\]
Then for every \(\alpha\in[0,1]\),
\[
\mathbb P\{p(S_{n+1})\le \alpha\}
\le
\alpha.
\]

If ties are broken uniformly at random, equality holds at the attainable grid
levels.

#### Proof

Exchangeability implies that the rank of \(S_{n+1}\) among
\[
S_1,\ldots,S_n,S_{n+1}
\]
is uniformly distributed after random tie-breaking. The event
\[
p(S_{n+1})\le\alpha
\]
is the event that \(S_{n+1}\) lies among the largest
\[
\lfloor \alpha(n+1)\rfloor
\]
rank positions. The probability is therefore at most
\[
\frac{\lfloor \alpha(n+1)\rfloor}{n+1}
\le
\alpha.
\]
Without random tie-breaking, the same inequality follows by conservative rank
counting. \(\square\)

This lemma is elementary, but it is the hinge of T18. The T-series supplies the
right scores. The finite rank lemma supplies lawful admission.

---

## 4. Milestone 1: Boundary Scores Are Conformal Scores

### Theorem 1. Boundary Scores Are Conformal Scores

Let \(S\) be a retained sector and let \(s_\partial\) be any boundary score
constructed from:

1. retained residuals;
2. candidate packets;
3. held-out boundary gain;
4. policy gain;
5. governance cost.

If \(s_\partial\) is computed by the same deterministic rule on calibration and
test episodes, then \(s_\partial\) is a valid conformal score for rank
calibration.

#### Proof

A conformal score is not required to be correct, sufficient, optimal, or
probabilistic. It must be a measurable rule applied symmetrically to calibration
and test episodes. By assumption, \(s_\partial\) is computed from the episode
and the fixed retained sector \(S\) by a deterministic rule. Therefore, under
exchangeability of the episodes, the sequence of scores is exchangeable. The
finite rank lemma applies. \(\square\)

### Interpretation

This theorem is deliberately modest. It says:

\[
\text{T-boundary scores can be calibrated without distributional assumptions.}
\]

It does not say:

\[
\text{every boundary score is a good score.}
\]

The semantic power comes from T11-T17. The validity power comes from rank
calibration.

---

## 5. Milestone 2: Boundary Calibration Ledger

T1 introduced probability ledgers. T3 introduced packet ledgers. T13 introduced
renormalization ledgers. T18 introduces calibration ledgers.

### Definition 5.1. Boundary Calibration Ledger

A **boundary calibration ledger** at sector \(S\) is a finite table
\[
\mathcal L_S
=
\{(Z_i,s_i,h_i,\kappa_i)\}_{i=1}^n,
\]
where:

- \(Z_i\) is an episode;
- \(s_i=s(Z_i)\) is a boundary score;
- \(h_i\in\mathcal H\) is a regime label or completion label;
- \(\kappa_i\in\mathcal K\) is a conductor, sector, task, policy, or governance
  cell.

The ledger is **cell-exchangeable** when, for each fixed
\[
(h,\kappa),
\]
the calibration episodes in that cell are exchangeable with a future test
episode from the same cell.

### Theorem 2. Boundary Calibration Ledger Theorem

Every finite retained sector \(S\), finite candidate boundary family
\[
\mathcal B=\{\beta_1,\ldots,\beta_m\},
\]
and finite episode protocol determines a boundary calibration ledger for any
chosen boundary score \(s\). If the ledger is cell-exchangeable, then conformal
p-values computed inside each cell are finite-sample valid in that cell.

#### Proof

The finite protocol makes \(Z_i\), \(s_i\), \(h_i\), and \(\kappa_i\) finite
data. Restrict the ledger to any cell
\[
(h,\kappa).
\]
By cell-exchangeability, the calibration scores in that cell and the future
test score from the same cell are exchangeable. Apply Lemma 3.1 inside the
cell. \(\square\)

### Interpretation

The ledger is the bridge between the T-series and finite-sample uncertainty.
It says:

\[
\boxed{
\text{validity is local to the declared calibration cell.}
}
\]

This is why the conductor language matters. The more faithfully the ledger
names the relevant packet/channel/sector, the less it hides boundary leakage in
a marginal average.

---

## 6. Milestone 3: Conformal Boundary Sets

We now make boundary completion set-valued.

Let
\[
\mathcal H=\{\varnothing,\beta_1,\ldots,\beta_m\}
\]
be the candidate completion space. The symbol \(\varnothing\) means "no
structural boundary completion admitted."

For each candidate \(h\in\mathcal H\), suppose we have a calibration ledger
\[
\mathcal L_h=\{s_{h,1},\ldots,s_{h,n_h}\}
\]
containing scores from episodes whose correct completion is \(h\). Define the
label-conditional p-value
\[
p_h(Z)
=
\frac{
1+\#\{i\le n_h:s_{h,i}\le s_h(Z)\}
}{
n_h+1
}
\]
when larger scores are more compatible with \(h\). Equivalently, use the upper
tail if larger scores are less compatible. The direction is part of the score
definition.

### Definition 6.1. Conformal Boundary Set

The conformal boundary set at level \(\alpha\) is
\[
C_\alpha(Z)
=
\{h\in\mathcal H:p_h(Z)>\alpha\}.
\]

### Theorem 3. Conformal Boundary Set Theorem

Assume that, for the true completion \(h^\star\), the calibration ledger
\[
\mathcal L_{h^\star}
\]
is exchangeable with the test episode. Then
\[
\mathbb P\{h^\star\in C_\alpha(Z)\}\ge 1-\alpha.
\]

#### Proof

The event \(h^\star\notin C_\alpha(Z)\) is
\[
p_{h^\star}(Z)\le\alpha.
\]
By Lemma 3.1, this event has probability at most \(\alpha\). Hence
\[
\mathbb P\{h^\star\in C_\alpha(Z)\}
=
1-\mathbb P\{p_{h^\star}(Z)\le\alpha\}
\ge
1-\alpha.
\]
\(\square\)

### Interpretation

The theorem gives a lawful boundary belief set:

\[
C_\alpha(Z)\subseteq\{\varnothing,\beta_1,\ldots,\beta_m\}.
\]

It may be:

- a singleton \(\{\beta_j\}\): admit packet \(\beta_j\);
- a singleton \(\{\varnothing\}\): do not update;
- a multi-set of candidates: defer or gather evidence;
- empty: the episode is incompatible with the declared ledger.

Ambiguity is not failure. Ambiguity is the valid output when the available
evidence does not justify a unique closure move.

---

## 7. Milestone 4: Conformal Update Gate

In many systems we do not need to name the exact packet immediately. We first
need to ask whether any structural update is justified.

Let \(h=0\) denote the null regime:

\[
h=0
\quad\Longleftrightarrow\quad
\text{noise, precision error, or no admissible structural boundary.}
\]

Let \(s(Z)\) be a boundary evidence score where larger values favor structural
completion. Let
\[
\mathcal L_0=\{s_1^0,\ldots,s_n^0\}
\]
be a null calibration ledger. Define
\[
p_0(Z)
=
\frac{
1+\#\{i:s_i^0\ge s(Z)\}
}{
n+1
}.
\]

### Definition 7.1. Conformal Update Gate

The level-\(\alpha\) conformal update gate is
\[
G_\alpha(Z)
=
\mathbf 1\{p_0(Z)\le\alpha\}.
\]

When \(G_\alpha(Z)=1\), the system is allowed to open a closure procedure. When
\[
G_\alpha(Z)=0,
\]
the system must treat the event as noise, ambiguity, or insufficient evidence.

### Theorem 4. Conformal Update Gate Theorem

If null calibration episodes are exchangeable with a future null episode, then
\[
\mathbb P_0\{G_\alpha(Z)=1\}\le\alpha.
\]

That is, the false structural update rate is controlled at level \(\alpha\).

#### Proof

Under the null, the calibration scores
\[
s_1^0,\ldots,s_n^0
\]
and the test score \(s(Z)\) are exchangeable. The update event is
\[
p_0(Z)\le\alpha.
\]
Apply Lemma 3.1. \(\square\)

### Corollary 4.1. Governed Closure Error

Suppose every unsafe closure move under the null is made only after
\[
G_\alpha(Z)=1.
\]
Then the probability of an unsafe null closure move is at most \(\alpha\).

#### Proof

The unsafe closure event is a subset of \(\{G_\alpha=1\}\). Use Theorem 4.
\(\square\)

### Interpretation

This theorem is the first sharp governance statement:

\[
\boxed{
\text{false boundary birth can be finite-sample controlled.}
}
\]

This is the mathematical version of the architectural rule:

\[
\text{do not create new structure merely because the model is surprised.}
\]

---

## 8. Milestone 5: Mondrian / Conductor-Conditional Boundary

Marginal validity may hide sector leakage. T3 and T11 already taught us that
packets live in conductor channels. T18 therefore calibrates by cells.

Let
\[
\kappa:Z\to\mathcal K
\]
be a finite taxonomy. Examples:

- conductor;
- packet order;
- sector \(S\);
- context class;
- task family;
- policy regime;
- source/user/environment class;
- safety governance channel.

For each cell \(k\in\mathcal K\), define a cell ledger
\[
\mathcal L_{0,k}=\{s_i^0:\kappa_i=k\}.
\]

### Theorem 5. Mondrian / Conductor-Conditional Boundary Theorem

Fix a cell \(k\). If null calibration episodes with \(\kappa=k\) are
exchangeable with a future null test episode satisfying \(\kappa(Z)=k\), then
the cellwise update gate
\[
G_{\alpha,k}(Z)
=
\mathbf 1\{p_{0,k}(Z)\le\alpha\}
\]
satisfies
\[
\mathbb P_0\{G_{\alpha,k}(Z)=1\mid \kappa(Z)=k\}\le\alpha.
\]

The same statement holds for conformal boundary sets computed inside the cell.

#### Proof

Condition on \(\kappa(Z)=k\). By assumption, calibration and test scores inside
the cell are exchangeable. Apply Lemma 3.1 inside that cell. \(\square\)

### Interpretation

This theorem explains the empirical lesson of the conformal boundary
experiments:

\[
\text{marginal coverage can be valid while a boundary sector leaks.}
\]

Conductor-conditional calibration prevents this by refusing to average away the
packet channel.

It also explains the limitation: if a cell has too little calibration data, the
valid set may become large. There is no free theorem that creates information.
There is only a theorem that refuses to counterfeit certainty.

---

## 9. Milestone 6: Boundary Efficiency

Validity alone is not enough. A valid set that always returns every hypothesis
is lawful but useless. Efficiency asks for small sets and decisive gates.

Let \(s\) be a structural score. Let \(F_0\) be its null score distribution and
\(F_1\) its structural score distribution. Larger scores favor structure.

Define the null conformal threshold
\[
q_{0,\alpha}
=
\inf\{t:\mathbb P_0(s\le t)\ge 1-\alpha\}.
\]

The population update rule is:
\[
\text{update when }s>q_{0,\alpha}.
\]

### Definition 9.1. Boundary Separation

A boundary score \(s_\partial\) separates structure from noise at level
\((\alpha,\delta)\) if
\[
\mathbb P_1\{s_\partial>q_{0,\alpha}\}\ge 1-\delta.
\]

It is **more efficient** than scalar surprise \(s_{\mathrm{scalar}}\) at
\((\alpha,\delta)\) if
\[
\mathbb P_1\{s_\partial>q_{0,\alpha}^{\partial}\}
>
\mathbb P_1\{s_{\mathrm{scalar}}>q_{0,\alpha}^{\mathrm{scalar}}\}
\]
while both use null gates with false update control \(\alpha\).

### Theorem 6. Boundary Efficiency Theorem

Assume two scores \(s_a\) and \(s_b\) are both governed by valid null conformal
update gates at level \(\alpha\). If
\[
\mathbb P_1\{s_b>q_{0,\alpha}^{b}\}
>
\mathbb P_1\{s_a>q_{0,\alpha}^{a}\},
\]
then \(s_b\) has strictly higher structural update power at the same false
update level. If additionally \(s_b\) yields a singleton boundary set whenever
it updates, while \(s_a\) yields a multi-hypothesis set with positive
probability, then \(s_b\) is strictly more efficient in expected set size.

#### Proof

Both gates have false update rate at most \(\alpha\) by Theorem 4. The true
update rate under the structural regime is exactly the probability of exceeding
the corresponding null threshold. The assumed inequality gives strictly greater
power for \(s_b\). Expected set-size efficiency follows by comparing the
probability mass assigned to singleton versus multi-hypothesis outputs.
\(\square\)

### Corollary 6.1. Scalar Surprise Can Be Valid but Inefficient

If noise and structure have the same scalar surprise distribution, then any
scalar-surprise update gate with false update control \(\alpha\) has structural
update power at most \(\alpha\). A boundary score with separation can have power
near one at the same false update level.

#### Proof

If the null and structural scalar-score distributions coincide, the probability
of crossing a null \(\alpha\)-tail threshold is the same under both regimes,
hence at most \(\alpha\). The separated boundary score satisfies Definition
9.1 with small \(\delta\). \(\square\)

### Interpretation

This is the formal version of:

\[
\boxed{
\text{scalar CP gives valid ambiguity;}
\qquad
\text{boundary CP gives valid action.}
}
\]

It is also the correct limitation. Conformal calibration does not make a bad
score good. It makes the score honest. T17 provides better scores; T18 governs
them.

---

## 10. Milestone 7: Conformal Active-Inference Policy

T17 decomposed expected free energy into boundary packets. T18 governs policy
admission.

Let \(\mathcal A\) be a finite action set. Examples:

\[
\mathcal A
=
\{\mathrm{skip},\mathrm{inspect},\mathrm{update},\mathrm{call\ tool},
\mathrm{write\ memory},\mathrm{defer}\}.
\]

Let each action \(a\in\mathcal A\) require a boundary hypothesis
\[
h(a)\in\mathcal H.
\]

For example:

- "skip" requires \(\varnothing\);
- "inspect gated cue" requires \(\beta_j\);
- "write memory" requires a stable boundary completion;
- "call external tool" requires an open-world boundary route;
- "change representation" requires a closure update.

### Definition 10.1. Conformal Policy

A policy \(\pi_\alpha\) is **conformal** if it chooses action \(a\) only when
\[
h(a)\in C_\alpha(Z).
\]

If no high-value action is conformally admitted, the policy must choose a safe
default such as skip, defer, ask for evidence, or route to a governed external
channel.

### Theorem 7. Conformal Active-Inference Policy Theorem

Assume:

1. \(C_\alpha(Z)\) is a conformal boundary set satisfying Theorem 3.
2. An unsafe action under true regime \(h^\star\) can occur only if
   \[
   h^\star\notin C_\alpha(Z)
   \]
   or if the policy violates its admissibility rule.
3. The policy is conformal.

Then
\[
\mathbb P\{\text{unsafe action caused by boundary misclassification}\}
\le
\alpha.
\]

If losses are bounded by \(L_{\max}\), then
\[
\mathbb E[\text{boundary misclassification loss}]
\le
\alpha L_{\max}.
\]

#### Proof

By conformality, the policy acts only through hypotheses in \(C_\alpha(Z)\). A
boundary misclassification unsafe action requires exclusion of the true
hypothesis \(h^\star\). By Theorem 3, this event has probability at most
\(\alpha\). The expected loss bound follows from boundedness. \(\square\)

### Interpretation

This theorem does not say that every conformal action is optimal. It says that
the policy can be forced to act only through statistically admitted boundary
hypotheses.

In T17 terms:

\[
\text{expected free energy chooses value;}
\qquad
\text{conformal boundary governance permits action.}
\]

The system may still choose a conservative safe action when the set is large.
This is not a defect. In open systems, lawful uncertainty should sometimes
become delay.

---

## 11. Milestone 8: Adaptive Exchangeability / Martingale Boundary

The previous theorems assume exchangeability inside ledger cells. Real agents
operate in streams. Environments shift. New boundary regimes appear. Calibration
ledgers age.

T18 treats exchangeability failure itself as a boundary signal.

Let
\[
p_1,p_2,\ldots
\]
be conformal p-values produced by a fixed ledger protocol under a declared null
or cell model.

Under stable exchangeability, the p-values are superuniform:
\[
\mathbb P(p_t\le u\mid \mathcal F_{t-1})\le u.
\]

Let \(b_t:[0,1]\to[0,\infty)\) be predictable betting functions satisfying
\[
\int_0^1 b_t(u)\,du\le 1.
\]

Define
\[
M_0=1,
\qquad
M_t=M_{t-1}b_t(p_t).
\]

### Theorem 8. Adaptive Exchangeability / Martingale Boundary Theorem

Under the stable exchangeability model, \(M_t\) is a nonnegative
supermartingale. Therefore, for any \(\lambda>0\),
\[
\mathbb P\left\{\sup_{t\ge0}M_t\ge\lambda\right\}
\le
\frac1\lambda.
\]

If \(M_t\) crosses a governance threshold \(\lambda\), the agent has
finite-sample evidence that its ledger cell is no longer stable. Such a crossing
is a valid trigger for:

- forming a new boundary cell;
- collecting new calibration episodes;
- opening a neurogenesis step;
- suspending a policy;
- pruning a stale boundary route after sufficient contrary evidence.

#### Proof

The superuniform property gives
\[
\mathbb E[b_t(p_t)\mid\mathcal F_{t-1}]\le \int_0^1 b_t(u)\,du\le1.
\]
Thus
\[
\mathbb E[M_t\mid\mathcal F_{t-1}]
=
M_{t-1}\mathbb E[b_t(p_t)\mid\mathcal F_{t-1}]
\le
M_{t-1}.
\]
So \(M_t\) is a nonnegative supermartingale. The maximal inequality follows
from Ville's inequality. \(\square\)

### Interpretation

This is the mathematical form of adaptive architecture:

\[
\boxed{
\text{diverge when calibration breaks;}
\qquad
\text{converge when new ledgers stabilize.}
}
\]

Neurogenesis is not arbitrary expansion. It is triggered by persistent
calibration failure. Pruning is not arbitrary compression. It is justified when
a boundary route no longer receives conformally admitted evidence.

Thus the architecture breathes:

\[
\text{detect}
\to
\text{diverge}
\to
\text{calibrate}
\to
\text{close}
\to
\text{prune}.
\]

---

## 12. Milestone 9: Conformal Closure Governance

We now state the master theorem.

### Definition 12.1. Governed Closure Architecture

A finite system is a **governed closure architecture** when it consists of:

1. a retained sector \(S\);
2. a finite boundary candidate family \(\mathcal B\);
3. a score family \(\mathcal S_\partial\);
4. a calibration ledger \(\mathcal L_S\);
5. a taxonomy \(\kappa\);
6. conformal boundary sets \(C_\alpha\);
7. update gates \(G_\alpha\);
8. an action policy \(\pi_\alpha\);
9. an adaptive exchangeability monitor \(M_t\);
10. governance constraints \(\mathcal G\) specifying which completions are
    permitted.

The policy is **lawful** if it never:

- admits a packet outside \(C_\alpha\);
- updates when \(G_\alpha=0\);
- acts through a completion forbidden by \(\mathcal G\);
- continues using a ledger after its exchangeability monitor has crossed the
  suspension threshold.

### Theorem 9. Conformal Closure Governance Theorem

Let a governed closure architecture operate on finite episodes. Assume:

1. Within each declared ledger cell \((h,\kappa)\), calibration and deployment
   episodes are exchangeable until the martingale monitor signals otherwise.
2. Boundary sets and update gates are computed by the finite-rank rules above.
3. The policy is lawful.
4. Boundary misclassification losses are bounded by \(L_{\max}\).

Then, for each active ledger cell:

\[
\mathbb P\{\text{false structural update in the cell}\}\le\alpha,
\]

\[
\mathbb P\{\text{true boundary hypothesis excluded from }C_\alpha\}\le\alpha,
\]

and

\[
\mathbb E[\text{boundary-governance loss in the cell}]
\le
\alpha L_{\max}.
\]

If, in addition, the boundary gain score separates structural from null regimes
with miss probability \(\delta\), then the governed architecture admits the
correct closure with probability at least \(1-\delta\) while retaining false
update control \(\alpha\). If the separation improves along refinement,
calibration, or evidence growth, the architecture converges from valid
ambiguity to valid action.

#### Proof

False structural update control follows from Theorem 4 in each active cell.
True boundary inclusion follows from Theorem 3 in each active cell. Loss control
follows from Theorem 7. The martingale monitor ensures that these statements are
claimed only while the active cell has not been statistically rejected by the
declared exchangeability test. The final efficiency statement is Theorem 6
applied to the boundary gain score. \(\square\)

### Final Compression

T18 proves the finite law of governed completion:

\[
\boxed{
\begin{aligned}
\text{closure} &\text{ supplies possible completions,}\\
\text{calibration} &\text{ supplies finite-sample validity,}\\
\text{governance} &\text{ supplies lawful admission.}
\end{aligned}
}
\]

The resulting architecture is:

\[
\boxed{
\text{valid finite intelligence}
=
\text{representation closure}
+
\text{boundary calibration}
+
\text{conformal governance}.
}
\]

---

## 13. Why This Is the Last Paper of the Deck

T0-T17 repeatedly discover the same shape:

\[
\text{project}
\to
\text{boundary}
\to
\text{complete}
\to
\text{project again}.
\]

That cycle explains:

- finite gauges;
- cumulant interactions;
- conductor packets;
- apex vertices;
- renormalization;
- curvature;
- continuum completion;
- residual streams;
- attention;
- active inference;
- external tools and memory;
- alignment as boundary governance.

But the cycle is incomplete unless the system knows when completion is allowed.
T18 supplies that missing law.

The final deck is therefore not:

\[
\text{everything is closure.}
\]

The final deck is:

\[
\boxed{
\text{everything finite that learns must close boundaries,}
\qquad
\text{and every closure must be governed.}
}
\]

This is the power-complete form:

\[
\text{Diverge: detect unresolved boundary.}
\]

\[
\text{Converge: admit only calibrated completion.}
\]

\[
\text{Repeat: monitor exchangeability and rebuild ledgers when the world moves.}
\]

---

## 14. Consequences

### 14.1 Mathematics

T18 makes uncertainty a structural object. The conformal set is not merely a
statistical wrapper around a prediction. It is a finite set of admissible
boundary completions.

This means that projection theory, closure theory, and finite-sample inference
share a common object:

\[
C_\alpha(Z)\subseteq\operatorname{Cl}(S)\setminus S.
\]

### 14.2 Physics

T13 and T14 identified renormalization sources, curvature, and Noether defects
as boundary obstructions. T18 adds the finite observer's rule:

\[
\text{do not renormalize on every fluctuation;}
\quad
\text{renormalize on calibrated boundary evidence.}
\]

This gives a discrete statistical analogue of lawful effective theory
selection.

### 14.3 Artificial Intelligence

T16 gave the architecture:

\[
\text{features, residuals, attention, memory, tools, alignment}.
\]

T17 gave the active inference rule:

\[
\text{update on boundary-structured surprise}.
\]

T18 gives the deployment rule:

\[
\text{act only through conformally admitted boundary completions.}
\]

This reframes safety:

\[
\boxed{
\text{alignment is governed boundary routing with calibrated admission.}
}
\]

### 14.4 Scientific Method

T18 also describes the research process itself. A theory expands when residuals
persist. It contracts when a boundary closes. It remains honest when every
claimed closure is calibrated against what would have happened under noise.

The method is:

\[
\text{diverge without fantasy;}
\qquad
\text{converge without denial.}
\]

---

## 15. Limitations

T18 is finite and explicit about its assumptions.

### 15.1 Exchangeability Is a Condition, Not a Miracle

The validity theorem requires exchangeability inside the declared ledger cell.
If the world shifts, the ledger must be suspended, refreshed, or split. The
martingale theorem is included precisely because real systems drift.

### 15.2 Scores Are Not Automatically Semantically Good

Conformal validity applies to the score supplied. If scalar surprise is the
wrong score, conformal prediction will honestly return ambiguity or bad
efficiency. T17 supplies boundary scores; T18 governs them.

### 15.3 Conditional Validity Requires Cells

No finite method can give exact validity for every infinitely refined condition
without paying in set size or assumptions. T18 therefore uses finite conductor
or sector cells. This is not a weakness. It is the finite honesty of the method.

### 15.4 Governance Can Defer

A lawful system may refuse to act. In high-stakes settings, this is a feature.
The safe default is part of the architecture, not an afterthought.

---

## 16. Appendix A: The Calibration Algorithms

This appendix states the algorithms in executable mathematical form.

### Algorithm A.1. Boundary Prediction Set

Input:

- candidate hypotheses \(\mathcal H\);
- calibration ledgers \(\mathcal L_h\) for \(h\in\mathcal H\);
- score functions \(s_h\);
- test episode \(Z\);
- level \(\alpha\).

For each \(h\in\mathcal H\):

1. Compute \(s_h(Z)\).
2. Compute
   \[
   p_h(Z)
   =
   \frac{1+\#\{i:s_{h,i}\le s_h(Z)\}}{n_h+1}
   \]
   when larger scores are more compatible with \(h\).

Return:

\[
C_\alpha(Z)=\{h:p_h(Z)>\alpha\}.
\]

### Algorithm A.2. Null Update Gate

Input:

- null ledger \(\mathcal L_0=\{s_i^0\}_{i=1}^n\);
- test boundary score \(s(Z)\);
- level \(\alpha\).

Compute:

\[
p_0(Z)=
\frac{1+\#\{i:s_i^0\ge s(Z)\}}{n+1}.
\]

Return:

\[
G_\alpha(Z)=\mathbf 1\{p_0(Z)\le\alpha\}.
\]

### Algorithm A.3. Conductor-Conditional Gate

Input:

- taxonomy \(\kappa\);
- cell \(k=\kappa(Z)\);
- null ledger restricted to \(k\);
- score \(s(Z)\);
- level \(\alpha\).

Compute the same null p-value inside cell \(k\). If the cell has too few
calibration points, return "defer" or merge only into a predeclared coarser
cell. Never create a cell after seeing the test score unless the selection rule
is itself included in the calibration protocol.

### Algorithm A.4. Governed Action

Input:

- conformal boundary set \(C_\alpha(Z)\);
- allowed completions \(\mathcal G\);
- action map \(a\mapsto h(a)\);
- utility \(U(a;Z)\).

Return:

\[
\pi_\alpha(Z)
\in
\arg\max
\{U(a;Z):h(a)\in C_\alpha(Z),\ h(a)\in\mathcal G\}.
\]

If the admissible set is empty, return the safe default action.

---

## 17. Appendix B: The Empirical Signatures

The following empirical signatures are predicted by T18.

### E4 Signature: Boundary-Resolved Prediction Sets

In a shortcut task, marginal conformal prediction may achieve coverage while
using large sets or leaking in boundary sectors. Boundary/Mondrian calibration
should preserve coverage in the forced boundary sector with smaller sets.

### E5 Signature: Matched Surprise

When structural and noise episodes have matched scalar surprise:

\[
\mathrm{AUC}(s_{\mathrm{scalar}})\approx 0.5.
\]

If boundary gain identifies stable closure:

\[
\mathrm{AUC}(s_{\Delta A})\to 1.
\]

Conformal scalar surprise should yield valid ambiguity. Conformal boundary gain
should yield valid update.

### E6 Signature: Policy Governance

In an active cue task, scalar surprise should not justify cue use. Boundary gain
should conformally admit the transformed cue only when the structural packet is
stable.

The expected pattern is:

\[
\text{false gated-cue action}\le\alpha,
\qquad
\text{structural reward}\approx\text{oracle reward}
\]
when boundary separation is strong.

---

## 18. Appendix C: Relationship to Classical Conformal Prediction

The main text is self-contained. It uses only the finite rank lemma. In standard
statistical language, the constructions correspond to:

- split conformal prediction;
- label-conditional conformal prediction;
- Mondrian or group-conditional conformal prediction;
- one-sided conformal testing;
- conformal risk control;
- conformal martingales for monitoring exchangeability.

T18 does not depend on naming these traditions. It depends on the finite rank
fact and the T-series boundary scores. The classical literature is therefore a
supporting historical and technical context, while the T18 claim is internal:

\[
\boxed{
\text{the right conformal score for intelligence is a boundary score.}
}
\]

---

## 19. References to the Lamed Series

1. T0 - Gauge Selection, Fourier-Mellin Simplex, and Apex Generator.
2. T1 - Native Simplicial Chart.
3. T2 - Cumulant Tower and Effective Action.
4. T3 - Character Orthogonality and Conductor Lattice.
5. T4 - Helmert Simplicial Residue Ladder.
6. T5 - Harmonic Simplicial Dual Gauge.
7. T6 - RMS Simplicial Quadratic Gauge.
8. T7 - Complex Amplitudes and Quantum Sector.
9. T8 - Multiplicative Apex and Dirichlet Polynomials.
10. T9 - Helmert-Fourier Transfer Matrix.
11. T10 - Kummer Clock and \(M\)-Power Gauge Hierarchy.
12. T11 - Apex Vertex Calculus.
13. T12 - Finite Apex Determinacy.
14. T13 - Exact Simplicial Renormalization.
15. T14 - Projected Flatness, Curvature, and Linearization.
16. T15 - Finite-to-Archimedean Completion.
17. T16 - Representation Closure and Open Intelligence.
18. T17 - Active Boundary Inference.

---

## 20. Closing

The T-series began with a finite simplex and a gauge question. It ends with a
finite law of admission.

The final object is not merely a model, a geometry, a renormalization group, an
agent, or a prediction set. It is a governed closure system:

\[
\boxed{
(S,\partial S,\operatorname{Cl},\mathcal L,C_\alpha,\mathcal G,\pi_\alpha).
}
\]

It detects what is missing, calibrates whether the missing thing is real enough
to act on, and routes completion only through lawful channels.

That is the final compression:

\[
\boxed{
\text{Diverge to see the boundary.}
}
\]

\[
\boxed{
\text{Converge only through calibrated closure.}
}
\]

\[
\boxed{
\text{Govern every completion that changes the world.}
}
\]
