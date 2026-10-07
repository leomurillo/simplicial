# Prompt: Three-Way Coherence Audit (audits κ and λ) — fresh-session brief

You are picking up a research-program task cold. The team workspace is
`C:\Projects\simplicial\`. You have no conversational context from prior
sessions; everything you need is in the files referenced below, plus the
existing `empirical/` audit-code corpus as templates.

## Mission, in one paragraph

The program's proposed Paper 47 (Arithmetic Decoupling Theorem; opened in
`v2insert-02.md`) claims that the kinematic (V) and gravity-adjacent (M)
sectors of the Bures lift's tangent space are HS-orthogonal at every
verified order, forced by Pontryagin character orthogonality on the
conductor lattice of `ℤ/6`. The claim is currently [P] at 2nd/4th order
(audited in `32_one_functional_four_forces_v0.2 (2).md` §13.2A and §13.2B)
and conjectured at all orders. Two empirical bridges have been pre-registered
to test whether the V/M decoupling *propagates* through training to leave a
measurable signature in real networks: **audit κ** (inference-side, on
Llama-3.1-8B / Mistral-7B-v0.3 via Paper 36's layerwise packet spectroscopy,
specified in `v2insert-05.md`) and **audit λ** (training-side, on small
MLPs via Paper 37's `(α, ε)` sweep, specified in `v2insert-06.md`). Both
ride on already-pre-registered sweeps in existing manuscripts (Paper 36 and
Paper 37 are draft v0.1 papers with full pre-registered protocols), but the
sweeps have *not yet been run* — Paper 36 v0.1 and Paper 37 v0.1 are
protocols, not measurements. Your task is to **code and run** the
underlying sweeps, then apply the V/M binning step to settle audits κ and λ
under three-outcome matched-pair pre-claim discipline. Your output is
deterministic scripts under `empirical/`, deterministic transcripts beside
them, and a settlement record in `v2insert-07.md` (creating it new) that
states which branch each audit realized.

## Read these files first, in this order

These are anchored objects (per Paper 35 §3.3) — read them as the source's
own statements, do not paraphrase or reconstruct. Sizes are listed so you
can plan your context budget.

1. **`v2insert-06.md`** (~25 KB) — the most recent insert, specifies the
   composition (audit λ on Paper 37's sweep, audit κ on Paper 36's sweep).
   Contains the pre-registered prediction P11 and the V/M analog tables.
2. **`v2insert-05.md`** (~31 KB) — specifies audit κ in detail; contains
   pre-registered predictions P8 (digits), P9 (months), P10 (weekdays
   control). Contains the V/M analog on `ℤ/10`, `ℤ/12`, `ℤ/7`.
3. **`v2insert-02.md`** (~27 KB) — the structural anchor for Paper 47 V/M
   Arithmetic Decoupling. Read to understand what V/M means.
4. **`32_one_functional_four_forces_v0.2 (2).md`** §6.1, §6.2, §13.2A,
   §13.2B (large file; read only those sections) — the Pontryagin
   character orthogonality (§6.2 Lemma 6.1a–c, the load-bearing [P]) and
   the §13.2B 4th-order audit that established the V/M sub-bundle
   structure. The audit scripts in `empirical/paper32_13_2_*.py` are your
   anchored templates for deterministic exact-arithmetic audits.
5. **`36_layerwise_packet_spectroscopy.md`** (~30 KB) — the pre-registered
   protocol for inference-side layerwise packet measurement. §1–§4
   (apparatus), §3 (P1–P7), §8 (script inventory, run-command schema),
   §9 (result templates).
6. **`37_label_smoothing_in_the_conductor_blind_spot.md`** (~30 KB) — the
   pre-registered protocol for training-side `(α, ε)` sweep on the months
   task. §2 (setup, Pareto rule, support `S`), §4 (sweep grid, splits,
   outcomes), §5 (P1–P7), §8 (script inventory), §9 (result templates).
7. **`35_grounded_paranoid_delusional_methodology.md`** (~28 KB) — the
   methodology paper. Read §3 (tenets, especially §3.3 anchored-objects
   and §3.4 deterministic-exact-reproducible) and §6.1 (the
   permanent-deferral failure mode). §3.1 carries the *binary* form of
   matched-pair pre-claiming; v2insert-04 extends it to three-outcome.
8. **`v2insert-04.md`** (~22 KB) — the methodology update specifying the
   three-outcome matched-pair rule. Read §2 (the rule) and §3.1 (the new
   tenet text). Binding from your work forward.

If a file you need is missing or you cannot read it, **stop and report**
rather than reconstructing — the anchored-objects rule (Paper 35 §3.3)
forbids substituting a paraphrase for the source.

## Existing code templates (read these for style conventions)

All in `C:\Projects\simplicial\empirical\`:

- `paper32_13_2_bures_dispersion_audit.py` — deterministic audit template
  (no model freedom, exact arithmetic where possible, transcript-friendly
  prints). Use this as the structural template for your audit scripts.
- `paper32_13_2B_fourth_order_casimir_audit.py` — second audit template,
  more complex (includes Hessian computations).
- `insert16_conductor_misspecification_certificate.py` — character-basis
  arithmetic on multiple primorial rows; the conductor-lattice machinery
  you will reuse for V/M binning.
- `activation_pullback_audit.py`, `bigram_corpus_control.py` — examples of
  audits on real transformer activations (Llama-3.1-8B and Mistral-7B-v0.3
  are loaded via HuggingFace `transformers`). Use these for Llama/Mistral
  forward-pass plumbing if you tackle audit κ.

The corpus convention: deterministic (no seeds in decisive paths, or
seeds explicit and recorded), exact (integer / rational arithmetic in any
vanishing or membership decision; floating point only for reporting),
reproducible (full script + run transcript archived together). Transcripts
are plain text, named `*_run_output.txt`, generated by piping the script's
stdout to file.

## What to compute — two audits in priority order

### Audit λ — Paper 37 (α, ε) sweep with V/M binning (lower compute, do first)

The pre-registered protocol is `37_label_smoothing_in_the_conductor_blind_spot.md`
§4 (sweep grid: `α ∈ {0, 0.25, 0.5, 0.75, 1.0}`, `ε ∈ {0, 0.03, 0.06, 0.1, 0.15, 0.2}`,
widths `W ∈ {16, 32, 64}`, three seeds, months task `ℤ/12`, support `S = {12}`).
The script inventory is §8 of that file (`empirical/label_smoothing_substitution_sweep.py`).

**Step 1.** Implement `empirical/label_smoothing_substitution_sweep.py`
following Paper 37 §4 verbatim. Paper 12 anchor for sanity: width 32,
`α = 1, ε = 0` should reproduce test loss `≈ 4.0514` on the months task
(Paper 37 §7); width 32, `α = 0, ε = 0` should reproduce `≈ 9.0838`
(Paper 37 §7, baseline). **If those two corners are outside `[3.5, 4.5]`
and `[8.0, 10.0]` respectively, your implementation does not reproduce
Paper 12 and you must reconcile before continuing** (Paper 37 §6 F2 says
the sweep is uninterpretable until you do).

**Step 2.** Add the V/M binning post-hoc. Per `v2insert-06.md` §2:

```
V on ℤ/12 (single-prime / prime-power axes): H_2 + H_3 + H_4
M on ℤ/12 (cross-prime carry):                H_6 + H_12

For each trained MLP at (α, ε, W, seed):
  σ_V := f_2^(final) + f_3^(final) + f_4^(final)
  σ_M := f_6^(final) + f_12^(final)
  ρ_{V/M} := σ_V / σ_M

Aggregate over seeds. Report per (α, ε, W) the mean and SD of ρ_{V/M}.
```

The packet-fraction definition is in Paper 36 §2.3 (the `f_{d,ℓ}` formula)
and in Paper 12 (the months centroid construction). Both are anchored
objects — use the formulae from those files verbatim.

**Step 3.** Settle pre-registered prediction P11 (`v2insert-06.md` §2).
Three pre-claimed branches:

- **K-branch:** `ρ_{V/M}` varies *monotonically* with `α` along iso-loss
  contours `G_IID(α, ε, W) = const`. Concretely: at the `α=1, ε=0` corner
  and the iso-loss-equivalent `α=0, ε=ε^\star` corner, `ρ_{V/M}` differs
  by more than the seed-noise scale.
- **L-branch:** `ρ_{V/M}` is statistically indistinguishable along iso-loss
  contours. Mechanisms A (ε) and B (α) are fully substitutive at the
  packet-signature level.
- **Joint-on-disjoint branch (per v2insert-04 §3.1 extension):** non-monotone
  along the ridge — saddle, sign reversal, or some other pattern.

All three are publishable. Do **not** select a branch in advance; report
what the data show.

**Step 4.** Output:
- `empirical/label_smoothing_substitution_sweep.py` (the driver)
- `empirical/label_smoothing_substitution_sweep_VM_binning.py` (the post-hoc V/M aggregation)
- `empirical/reports/label_smoothing_substitution_months_width{16,32,64}.md`
  (one per width — these are pre-registered in Paper 37 §8 script inventory)
- `empirical/reports/label_smoothing_substitution_VM_audit_lambda.md`
  (the settlement record — your write-up of what each pre-claimed branch
  realized)
- Run transcripts: `*_run_output.txt` beside each script.

### Audit κ — Paper 36 sweep with V/M binning (higher compute, do if feasible)

Requires GPU access and HuggingFace model downloads (Llama-3.1-8B is
~16 GB; Mistral-7B-v0.3 is ~14 GB). If your environment lacks GPU or
can't download those models, **stop here, document what you did for
audit λ, and report that audit κ is deferred for compute reasons** —
this is itself a legitimate outcome under Paper 35 §3.6 (the deferred
state is a recorded fact, not a silent skip).

If you can run it:

**Step 1.** Implement `empirical/layerwise_packet_spectroscopy.py` per
Paper 36 §8 (driver) and `empirical/native_logit_lens_packet_score_layerwise.py`
per Paper 36 §8 (the lens arm). The script inventory in Paper 36 §8 is
your exact pre-registered specification — follow it verbatim.

**Step 2.** Run the sweep on months (`ℤ/12`), digits (`ℤ/10`), and
weekdays (`ℤ/7`) on Llama-3.1-8B (and Mistral-7B-v0.3 if time permits;
single-model run is acceptable). Paper 36 §1.2 / §5 anchor: at layer 28
on Llama-3.1-8B months, the raw BF16 hidden-probe should give
`f_{12,28}^{(lens)} ≈ 0.356`; the final-layer (native logit) lens should
give `f_{12,final}^{(lens)} ≈ 0.657`. **If those numbers are outside the
bands `[0.30, 0.40]` and `[0.62, 0.69]` respectively (Paper 36 §3 P2),
your sweep does not reconcile with Paper 26's anchor and you must
reconcile before reporting the other layers** (Paper 36 §7 F1).

**Step 3.** Add V/M binning per task. Per `v2insert-05.md` §1:

```
ℤ/12 (months):   V = H_2 + H_3 + H_4;  M = H_6 + H_12
ℤ/10 (digits):   V = H_2 + H_5;        M = H_10
ℤ/7  (weekdays): only H_7; no V/M split (negative control)

For each task and each layer ℓ:
  σ_V(ℓ) := sum of f_{d,ℓ}^(lens) over d in V
  σ_M(ℓ) := sum of f_{d,ℓ}^(lens) over d in M

Depth-normalized saturation index per packet:
  σ_d := mean_ℓ [ (f_{d,ℓ} / f_{d,final}) * (ℓ / L_model) ]
```

**Step 4.** Settle pre-registered predictions P8 (digits), P9 (months),
P10 (weekdays control), per `v2insert-05.md` §2. Each is three-outcome
pre-claimed; report which branch each realized.

**Step 5.** Output:
- `empirical/layerwise_packet_spectroscopy.py`
- `empirical/native_logit_lens_packet_score_layerwise.py`
- `empirical/reports/layerwise_packet_spectroscopy_{months,weekdays,digits}_llama31_8b.{md,json}`
  (and `_mistral7b_v0_3.*` if you also run that model)
- `empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md`
  (the settlement record)
- Run transcripts beside scripts.

## Pre-registered predictions (already committed; do not modify)

These were pre-registered before this fresh session started. You report
the realized branch; you do not adjudicate which branch you would have
preferred.

### From `v2insert-05.md` (audit κ):

- **P8 (digits, ℤ/10):** depth-normalized saturation indices σ_2, σ_5 (V)
  vs σ_{10} (M) differ by more than seed noise (K-branch) /
  indistinguishable (L-branch) / separate with sign opposite to the
  Paper 47 naive prediction (joint-on-disjoint).
- **P9 (months, ℤ/12):** V cluster (`H_2, H_3, H_4`) and M cluster
  (`H_6, H_12`) separate (K) / don't separate (L) / `H_4` clusters with M
  rather than V (joint-on-disjoint, would trigger a V/W/M trichotomy
  update to Paper 47).
- **P10 (weekdays, ℤ/7) — negative control:** no V/M signal (control
  passes, K-branch) / spurious signal (control fails, P8/P9
  uninterpretable, L-branch) / structural separation on a different axis
  (joint-on-disjoint).

### From `v2insert-06.md` (audit λ):

- **P11 (months, ℤ/12):** `ρ_{V/M}(α, ε, W)` varies monotonically with `α`
  along iso-loss contours (K-branch) / is iso-loss-invariant (L-branch) /
  varies non-monotonically along ridge (joint-on-disjoint).

## Discipline (binding)

These are not suggestions; they are tenets of Paper 35.

1. **Anchored objects (Paper 35 §3.3).** Use the formulae in the cited
   manuscripts (Paper 12 for the months centroid, Paper 26 for the lens
   arm, Paper 36 for f_{d,ℓ} definition, Paper 37 for the (α, ε) Pareto
   rule). Do not paraphrase or reconstruct unless the reconstruction is
   itself verified against the source's own artifact. If you reconstruct,
   verify against an existing anchor (e.g., Paper 12's
   width-32 `α=1, ε=0` test loss is your sanity check).
2. **Deterministic, exact, reproducible (Paper 35 §3.4).** Seeds explicit
   and recorded. Floating point only in continuous-valued reporting; integer
   /rational arithmetic in any discrete vanishing decision. Full transcripts
   archived. Reports include the source-script version.
3. **Three-outcome matched-pair (Paper 35 §3.1 as extended by v2insert-04).**
   Pre-claimed branches for P8, P9, P10, P11 are listed above. Realize
   whichever branch the data shows; report it; do not silently absorb a
   third-outcome branch into one of the binary K/L.
4. **No upward tier-crossing (Paper 35 §3.5 firewall).** Report your audits
   as [P] for the deterministic computations, [A] for any structural
   identification you make, [C] for anything you conjecture beyond what
   the audit measured. Do not promote [A] to [P] without a named further
   audit; do not promote [C] to [A] without a named further structural
   argument.
5. **Failures are first-class (Paper 35 §3.6).** If your script returns an
   unexpected value (e.g., Paper 12 anchor not reproduced; Paper 26 anchor
   not reproduced), record the failure with full transcript, diagnose,
   and re-run with the correction. Do *not* delete failed transcripts; the
   record is append-only.
6. **Dimensional firewall (Paper 32 §11.2; see also v2insert-02 §3.7).**
   No physical units, no dimensionful constants, no Planck scale, no
   horizon area, no Newton constant, no Bekenstein–Hawking entropy values,
   no graviton mass. Only structural dimensionless quantities (`σ_V`,
   `σ_M`, `ρ_{V/M}`, packet fractions, depth-normalized indices).

## Output expectations

All scripts under `C:\Projects\simplicial\empirical\`. All reports under
`C:\Projects\simplicial\empirical\reports\`. Naming follows the conventions
in Paper 36 §8 and Paper 37 §8.

The settlement records are the headline deliverables:

- `empirical/reports/label_smoothing_substitution_VM_audit_lambda.md` —
  audit λ result. Reports which P11 branch realized (K / L /
  joint-on-disjoint) with effect sizes, error bars, and seed-noise
  estimates.
- `empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md` —
  audit κ result. Reports P8 (digits) / P9 (months) / P10 (weekdays
  control) jointly, each with its realized branch.

Finally, create `v2insert-07.md` at the top level of `C:\Projects\simplicial\`,
in the same format as `v2insert-05.md` and `v2insert-06.md`, recording the
audit settlement. Its content should include:

- The realized branches of P8, P9, P10, P11.
- The (κ, λ) joint outcome from the four-cell matrix in `v2insert-06.md`
  §4: (K,K) / (K,L) / (L,K) / (L,L) plus joint-on-disjoint products.
- Implications for Paper 47 (proposed) — does the V/M Arithmetic
  Decoupling Theorem have empirical support at the propagation level?
- Implications for Papers 36 and 37 themselves — does the V/M signal
  match or refine their pre-registered P1–P7 / P1–P10 patterns?
- Carry-forward for future audits (e.g., `ℤ/30` extension).

If you can only complete audit λ, `v2insert-07.md` records that
realization and explicitly defers audit κ with a named reason. That is a
legitimate outcome.

## Success criteria

1. `empirical/label_smoothing_substitution_sweep.py` runs deterministically
   end-to-end and reproduces Paper 12 anchor at `(α=1, ε=0, W=32)` within
   `[3.5, 4.5]` test loss. (Paper 37 §7 anchor; Paper 37 §6 F2 falsifier.)
2. The settlement record for audit λ states *one* of the three P11
   branches as realized, with effect sizes.
3. (If you ran audit κ) Paper 26 anchor reproduced at layer-28 Llama-3.1-8B
   months: `f_{12,28}^{(lens)} ∈ [0.30, 0.40]` and
   `f_{12,final}^{(lens)} ∈ [0.62, 0.69]`. (Paper 36 §3 P2; Paper 36 §7 F1.)
4. The settlement record for audit κ states realized branches for P8, P9,
   P10.
5. `v2insert-07.md` exists at the top level and follows the format of
   `v2insert-05.md` / `v2insert-06.md`.
6. All artifacts (scripts, transcripts, reports) are under `empirical/`
   per the file-hygiene rule.

## What NOT to do

1. Do *not* propose new theory or new structural claims. Your task is to
   *measure* against pre-registered predictions, not to interpret beyond
   what the audit returns.
2. Do *not* assert any of the [C] conjectures of Paper 47 as confirmed by
   audits κ or λ. These audits test *propagation* of the V/M decoupling
   to network internals; even a clean K-branch outcome is a *structural
   correspondence* and not a derivation. Use correspondence language per
   `v2insert-02.md` §3.7 and `v2insert-06.md` §7.
3. Do *not* delete or overwrite the existing files at the top level of
   `C:\Projects\simplicial\` (the Paper 32/35/36/37 manuscripts, the
   v2insert-01..06 files). These are part of the corpus and append-only.
4. Do *not* modify the pre-registered predictions P8, P9, P10, P11. They
   were committed before your session began.
5. Do *not* claim significance, importance, or field-defining status for
   the audit results. Paper 35 §7 final unsafe statement forbids this; the
   methodology operates on its own outputs.

## If you get stuck

- **Compute too large?** Run audit λ only; note audit κ as deferred.
  Audit λ alone is a complete settlement record for P11; deferring κ is
  legitimate per Paper 35 §3.6.
- **Paper 12 anchor not reproducing?** Stop and diagnose. The sweep is
  uninterpretable until reconciled (Paper 37 §6 F2). Document the
  discrepancy in the run transcript and report it as a method-discrepancy
  event under Paper 35 §3.6.
- **HuggingFace model download failing?** Note the failure, document the
  environment, mark audit κ as deferred, and complete audit λ. The
  deferral is a stated result.
- **Ambiguous prediction outcome (effect size between bands, or
  branch-classification unclear)?** Report it as such. Paper 35 §3.6
  permits "the audit was inconclusive at the current statistical power"
  as a stated outcome; it does not permit silently picking the nearest
  branch.

You have everything you need to start. Read the eight anchor files in
order, study the existing audit templates in `empirical/`, then implement,
run, and settle. Honor the tenets of Paper 35; your settlement record is
the only thing that travels back to the team.
