# Audit kappa settlement record -- V/M layerwise packet propagation on Llama-3.1-8B and Mistral-7B-v0.3

**Scripts:**
- `empirical/layerwise_packet_spectroscopy.py` (Paper 36 §8 driver)
- `empirical/native_logit_lens_packet_score_layerwise.py` (Paper 36 §8 lens arm)
- `empirical/verify_audit_kappa_anchors.py` (anchor-gate verifier, settlement bookkeeping)

**Script versions:**
- driver: `audit_kappa_driver_v0.2_2026_06_12` (was `v0.1_2026_05_20`; see §1.2)
- lens scorer: `audit_kappa_lens_v0.1_2026_05_20` (UNCHANGED -- every measured quantity
  comes from this script, which was anchor-verified on 2026-05-20)

**Pre-registered protocol:** Paper 36 §3 (P1–P7), §3.A (P8–P10), §8 (script inventory).
**V/M binning:** v2insert-05 §1, inclusive convention per audit χ_12 (V = H_2+H_3+H_4; M = H_6+H_12).
**Three-outcome rule:** v2insert-04 §3.1.

---

## 1. Environment status (binding, per Paper 35 §3.6)

### 1.0 Deferral history (recorded fact, retained)

On 2026-05-20 the layerwise sweep was **DEFERRED for compute and environment
reasons** (Windows laptop, CPU-only, `transformers` not installed, no HF model
access provisioned; only final-layer native dists + layer-28 PCA-context
residuals saved locally). The deferral was recorded as an outcome, not a
silent skip. This section CLOSES that deferral.

### 1.1 Environment actually used (2026-06-12)

- GCP instance `audit-kappa-vm`, project `causalab-llama`, zone `us-central1-a`:
  `g2-standard-8` (8 vCPU, 32 GB) + 1× NVIDIA L4 (23 GB, driver 580.159.03),
  **on-demand** (spot/preemptible L4 was stocked out in all us-central1 G2 zones
  at run time), image family `pytorch-2-9-cu129-ubuntu-2404-nvidia-580`
  (deeplearning-platform-release).
- Python 3.12 venv (`--system-site-packages`): torch 2.9.1+cu129 (system),
  transformers 4.57.6, safetensors, accelerate, huggingface_hub + hf_transfer,
  sentencepiece, protobuf. (transformers 5.12.0 was initially installed and
  failed to import due to a broken system `torchaudio` ABI on the DLVM image;
  pinned `<5`. Environment fix only.)
- Models: `meta-llama/Llama-3.1-8B` and `mistralai/Mistral-7B-v0.3`, gated
  access granted, BF16.
- Forward passes: one per prompt, last-token residuals captured at every
  `hidden_states` row (33 rows = embedding row + 32 blocks; final row is
  post-final-RMSNorm, i.e. exactly what feeds W_U). Residuals stored BF16
  (matching Paper 26's "raw BF16" regime).
- Prompt sets: the **exact Paper 26 baseline prompt sets**
  `months/baseline/train_samples.json` (84) and
  `weekdays/baseline/train_samples.json` (49). (NOT
  `empirical/data/months_probe_manifest.json`, which is a different
  144-record template.)
- Wall clock on the instance ≈ 26 min; estimated cost ≈ $0.40 (on-demand
  g2-standard-8 ≈ $0.85/hr + 150 GB pd-balanced). Instance DELETED after
  artifact retrieval (E11 pattern).

### 1.2 Driver changes (recorded diff; no measured quantity touched)

The v0.1 driver's transformers code path was an unimplemented shell. v0.2
implements exactly the six capture steps of the v0.1 docstring (load BF16
model; load `train_samples.json` prompts; capture per-layer last-token
residuals; save safetensors + `W_U_VR` npz slice; invoke the lens scorer).
Two CLI args added (`--samples`, `--token-ids`), plus a single-token identity
assertion between supplied token ids and the tokenizer (capture-correctness
guard). One mechanical fix mid-run: `.detach()` on `lm_head.weight` before
`.numpy()` (first months attempt crashed at the W_U-save step; forwards were
otherwise complete; rerun from scratch). Full unified diff:
`empirical/reports/audit_kappa_driver_v0.1_to_v0.2.patch`.

**The lens scorer -- the only script that computes f_{d,ell} -- is byte-identical
to the version anchor-verified on 2026-05-20.** No prediction, threshold,
binning, or outcome rule was altered.

---

## 2. Anchor gate (Paper 36 §3 P2 / §7 F1; errand sanity gate) -- run BEFORE teardown

Verifier: `empirical/verify_audit_kappa_anchors.py`; output
`empirical/reports/audit_kappa_anchor_gate.json`.

### 2.1 Final-layer anchors: PASS

Llama-3.1-8B months, sweep final row (post-final-norm residual @ W_U_VR) vs the
2026-05-20 settlement anchors (themselves an exact 6-digit reproduction of
Paper 26):

| packet | sweep final | anchor | delta |
|---:|---:|---:|---:|
| f_2  | 0.051083 | 0.050608 | +0.000475 |
| f_3  | 0.066028 | 0.066390 | -0.000362 |
| f_4  | 0.059103 | 0.059082 | +0.000021 |
| f_6  | 0.166851 | 0.166506 | +0.000345 |
| f_12 | 0.656935 | 0.657415 | -0.000480 |

All five reproduce to ≤ 5e-4 (BF16 forward nondeterminism scale). P2's
final-layer band [0.62, 0.69] holds. Weekdays final f_7 = 1.0 exactly.
**The errand's STOP condition did not fire.**

### 2.2 Layer-28 anchor: RECONCILED -- instrument conflation found (P2 partially refuted)

Two findings, both pinned by exact-arithmetic cross-checks:

1. **Layer-index convention.** The causalab artifact "L28_last_token"
   corresponds to sweep row 29 (HF `hidden_states[k]` is the *input* to block
   k; block 28's output is row 29). Verified per-example on months/Llama:
   cosine(sweep row 29, saved `raw_features.safetensors`) = 0.9998 mean
   (row 28: 0.945; row 27: 0.899).
2. **Lens vs probe.** Scoring the **original Paper 26 saved layer-28
   residuals** with the model's own W_U slice gives
   f_12^(lens) = **0.638165**; the sweep's row 29 gives **0.638223**
   (agreement ~6e-5 -- the forward-pass reproduction is exact at the right
   index). Both are far outside P2's layer-28 band [0.30, 0.40]. The Paper 26
   number 0.355640 in that band is the **full-label trained-probe** quantity
   (Paper 36 §5 says so: "hidden-state shortcut audit, full-label probe");
   P2 pre-registered the probe number as a band for the *lens* quantity.
   The two instruments differ at this depth by ~0.28 in f_12 -- which is
   itself a P7-flavored lens/probe-gap datum.

**Verdict: P2 = final-layer half CONFIRMED; layer-28 half REFUTED as
pre-registered, with the discrepancy fully reconciled to an instrument
conflation (lens band written around a probe number), not a methodological
inconsistency with Paper 26.** F1 fired and was reconciled per its own
instruction before the rest of the table was interpreted.

**Designation: the *instrument-conflation exhibit*.** Same model, same layer,
same hidden states: trained-probe readout 0.356 vs frozen-unembedding lens
0.638. This is the live empirical instance of the survey item 4 thesis (the
readout quotient determines what you see) and is reserved under this name for
the consolidated interpretability-obstruction paper.

---

## 3. Layerwise spectra (model-side rows)

Full tables: `empirical/reports/layerwise_packet_spectroscopy_<task>_<model>.md`
(+ `.json`); capture manifests under `empirical/data/`.

Headline shape, months (f_12 vs row): both models show a **non-monotone**
profile -- noisy early/mid readouts, a single large crystallization jump
(Llama: rows 21→22, +0.454; Mistral: rows 17→18, +0.388), a high plateau with
**overshoot** above the final value (Llama peak 0.776 @ row 24 vs final 0.657;
Mistral peak 0.823 @ row 18 vs final 0.785), then a mild decline into the
readout. This is the third profile anticipated in Paper 36 §1.2 ("internal use
of a finer cyclic structure than the head exposes"), not the monotone-late-rise
of P1.

Weekdays: f_7 = 1.000000 at every row on both models -- structurally forced
(only one nontrivial packet exists on Z/7; the fraction normalizes to 1).

### 3.1 V/M saturation indices (σ_d = mean_ell[f_{d,ell}·ell/L]/f_{d,final}; rows 0..32, L = 32)

| | σ_2 (V) | σ_3 (V) | σ_4 (V) | σ_6 (M) | σ_12 (M) |
|---|---:|---:|---:|---:|---:|
| Llama-3.1-8B | 0.5642 | 0.9397 | 0.9215 | 0.4056 | 0.4369 |
| Mistral-7B-v0.3 | 1.8856 | 1.2749 | 1.6706 | 0.4522 | 0.4070 |

On BOTH models: every V-packet σ exceeds every M-packet σ (Llama min-V 0.564 >
max-M 0.437; Mistral min-V 1.275 > max-M 0.452), the M pair is tight, and the
ordering σ_6 > σ_12 replicates. Same separation direction on both models
(V carries relatively more depth-weighted mass; M concentrates late).
On Llama the V triple is loose: σ_2 = 0.564 sits closer to the M pair than to
{σ_3, σ_4} ≈ 0.93. On Mistral the V/M gap (0.82) exceeds the V-internal spread
(0.61).

---

## 4. Settlement of the pre-registered predictions (three-outcome rule)

| Prediction | Realized branch | Evidence |
|---|---|---|
| P1 (months f_12 late + monotone) | **REFUTED** (both models) | Second-half monotonicity violations: 11 (Llama), 9 (Mistral). Largest increment NOT in last six rows: Llama rows 21→22, Mistral rows 17→18. Profile = jump + overshoot + decline. |
| P2 (anchor row) | **Final half CONFIRMED; layer-28 half REFUTED-RECONCILED** | §2 above. Instrument conflation (probe number in lens band); apparatus fully reconciled at 6e-5. |
| P3 (coarse packets crystallize earlier; ell*_d non-decreasing in d) | **REFUTED as defined** (both models) | Llama ell* = (H_2:7, H_3:0, H_4:0, H_6:0, H_12:2); Mistral (1,0,0,0,0). F3 fires by the letter of the statistic. Apparatus caveat: ell* is dominated by noisy embedding-adjacent rows where lens readouts are near-arbitrary; the pre-registered statistic has no early-noise guard. |
| P4 (weekday H_7 ramp) | **AMBIGUOUS -- vacuous at the pre-registered metric** | f_7 ≡ 1 identically by fraction normalization on a prime modulus (both models, all 33 rows). The ramp lives in absolute nontrivial energy, which f_d cannot express. Final-layer consistency holds. |
| P5 (digits divisor split) | **DEFERRED** | No digits baseline prompt set exists in the tree (Paper 26 apparatus never produced one); generating a new prompt set would not be the pre-registered input. |
| P6 (predecessor-leakage asymmetry, layerwise) | **DEFERRED -- instrument not in driver set** | Requires class-conditional packet profiles; the lens arm outputs only E_x-averaged fractions. No analysis script exists; writing one was out of errand scope. |
| P7 (lens vs trained-probe gap) | **DEFERRED -- driver not finalized** | `quotient_probe_packet_score_layerwise.py` (Paper 36 §8) was never written; only the single-layer Paper 26 version exists. NOTE: §2.2's probe-vs-lens difference at causalab-L28 (0.356 vs 0.638) is a single-layer datum in P7's direction (gap >> 0.10 late in the network). |
| P8 (digits V/M σ asymmetry) -- primary | **DEFERRED** | With P5 (no digits data). |
| P9 (months V/M σ clustering) | **K-branch on BOTH models; propagation REAL and significant** (bootstrap 2026-06-13 supersedes the point-estimate "Llama joint-on-disjoint" reading) | §3.1 + bootstrap. Both models: full V/M order separation, same direction, σ_6 > σ_12 replicated. 2000-resample prompt bootstrap (`empirical/vm_bootstrap_significance.py`): min(σ_V)−max(σ_M) > 0 in 100% of resamples (Llama gap 0.13 CI [0.04,0.23]; Mistral 0.82 CI [0.65,1.05]). The H_2-defector reading is REFUTED — σ_2 exceeds all M in 100% of resamples (CI [0.49,0.67] vs σ_12 [0.42,0.45]). Real finding: Llama internal V three-level ladder M(≈0.42) < H_2(≈0.57) < {H_3,H_4}(≈0.93), non-overlapping bands; Mistral V uniformly high (~6× effect). Limitation: prompt-bands at one checkpoint/family; weight variance untested. |
| P10 (weekdays negative control) | **K-branch** (both models) | f_7 ≡ 1 at every row; no off-divisor/spurious structure can appear at the fraction level, and none did. P8/P9 remain interpretable (F6 does not fire). |

### Failure conditions fired

- **F1**: fired (layer-28 band) and reconciled (§2.2) before interpretation, per its own instruction.
- **F3**: fired by the letter of the ell* statistic (with the early-noise apparatus caveat recorded).
- **F2, F5, F6, F7, F8**: did NOT fire. (F2: weekday control is consistent at the only level the metric can express. F5: cross-model spectra qualitatively agree -- same jump/plateau/overshoot shape, same V/M direction. F7: V/M separation present on both models -- the empirical-propagation claim of Paper 47 (proposed) SURVIVES. F8: no cross-task sign test available without digits, but no sign reversal between models on months.)
- **F4**: not evaluable (probe arm deferred).

---

## 5. Available artefacts (all retrieved before teardown; instance deleted)

- `empirical/reports/layerwise_packet_spectroscopy_{months,weekdays}_{llama31_8b,mistral7b_v0_3}.{json,md}` -- the four spectra.
- `empirical/reports/run_log_{months,weekdays}_{llama31_8b,mistral7b_v0_3}.txt` -- full run logs.
- `empirical/data/residual_streams_{task}_{model}.safetensors` -- BF16 [n, 33, 4096] last-token residuals (4 files; months 22.7 MB, weekdays 13.2 MB each model). These make every downstream re-analysis (P6's class-conditional profiles, probe-arm fitting, CCSAE input) possible WITHOUT re-running the models.
- `empirical/data/W_U_VR_{task}_{model}.npz` -- unembedding slices [N, 4096] fp32.
- `empirical/data/capture_manifest_{task}_{model}.json` -- model id, token ids, versions, dtype.
- `empirical/reports/audit_kappa_anchor_gate.json` -- gate output (note: its `anchor_gate_pass=false` reflects the P2 layer-28 band check at row 28 pre-reconciliation; the errand's final-layer gate PASSED -- see §2).
- `empirical/reports/audit_kappa_driver_v0.1_to_v0.2.patch` -- exact driver diff.
- `empirical/reports/lens_finalonly_{months,weekdays}_llama31_8b.json` -- the 2026-05-20 final-only anchors (unchanged).

Mistral V_R token ids (tokenizer-derived on-VM, single-token asserted):
months `[5392, 6121, 4885, 4767, 3014, 4980, 5166, 4396, 4842, 5295, 5117, 5693]`,
weekdays `[10030, 11955, 12231, 11751, 8853, 9281, 8497]`.

---

## 6. What this audit now supports / does not support

Supports:
- The Paper 26 final-layer anchor chain end-to-end on fresh hardware (≤5e-4).
- Exact reconciliation of the Paper 26 layer-28 artifact (convention + instrument), removing the last methodological gap between Paper 26 and the sweep.
- A REAL, cross-model-replicated V/M depth-saturation separation on months (P9; direction V-earlier/M-late, identical on both models) -- the empirical-propagation claim survives its first two-model test.
- Cross-model replication of the months spectrum shape (jump + overshoot + decline), refuting P1's monotone-late narrative on both models simultaneously.

Does not support:
- Any digits-row claim (P5/P8 deferred -- no pre-registered digits prompt set exists).
- Any trained-probe-arm claim (P7 deferred -- layerwise probe driver not written).
- Layerwise class-conditional claims (P6 deferred -- analysis arm not written).
- Seed-noise-calibrated significance for P9 (single checkpoint per family; point estimates only).

Phases 3–4 of the errand (Paper 39 Γ-law, Paper 40 σ-audit extension): **drivers
not finalized, skipped** -- no `empirical/` scripts exist for either; writing new
experiment code was out of errand scope. Phase 5 (CCSAE, Paper 45): out of scope,
not started; note the captured residual streams above are exactly its input
activations for months/weekdays.

The companion audit lambda (training-side, small MLPs) was completed 2026-05-20;
see `empirical/reports/label_smoothing_substitution_VM_audit_lambda.md`.
