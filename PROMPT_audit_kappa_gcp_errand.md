# ERRAND PROMPT — Close the deferred LLM validation block (audit κ) on GCP

Paste this into a fresh Claude Code session in `C:\Projects\simplicial`.

---

This is an EXECUTION ERRAND, not research. The science is pre-registered and frozen;
your job is provisioning, faithful execution, artifact retrieval, and settlement
bookkeeping. Estimated wall clock: half a working day; GPU cost: single-digit dollars.

## Read first, in this order

1. `empirical/audit_kappa_gcp_runbook.md` — the full recipe (VM type, staging list,
   run order, teardown). Follow it.
2. `empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md` — the recorded
   deferral (§1) and what was already measured from saved artifacts (§2). Your output
   REPLACES the deferral with outcomes.
3. `36_layerwise_packet_spectroscopy.md` — §3 pre-registered predictions, §8 script
   inventory, plus the V/M binning (v2insert-05 §1) and three-outcome rule
   (v2insert-04 §3.1) it cites.
4. The two drivers (READ ONLY — never execute locally):
   `empirical/layerwise_packet_spectroscopy.py` and
   `empirical/native_logit_lens_packet_score_layerwise.py`. Learn their CLI and input
   manifests; note which `months/` / `weekdays/` assets they expect.

## Hard rules

- **NEVER run or import `torch`/`transformers` locally.** A prior local torch run
  physically destroyed this laptop's drive. `importlib.util.find_spec` probing is
  allowed; execution happens ONLY on the GCP instance. Check HF access with plain
  HTTP (e.g. `curl -H "Authorization: Bearer $env:HF_TOKEN"
  https://huggingface.co/api/models/meta-llama/Llama-3.1-8B`), not a python import.
- **Pre-registration is frozen.** Do not alter predictions, thresholds, packet
  binning, or the three-outcome rule. If a driver needs a code fix merely to RUN
  (path, API drift, dtype, tokenizer kwarg), make the minimal fix, record the exact
  diff in the settlement report, and state explicitly that it does not touch any
  measured quantity. If a fix WOULD touch a measured quantity: STOP and report.
- **GPD settlement discipline** (Paper 35 §3.6): outcomes are recorded whichever way
  they fall. A failed prediction is a result, not a bug to iterate on. No re-runs to
  get a better answer; re-run only for crashes/incomplete artifacts.
- **Spot instances:** persist artifacts as they are produced (scp or GCS bucket after
  each task), so preemption loses minutes, not the run.

## Phase 0 — Preflight (local, no model execution)

Verify and report each item; if ANY fails, STOP and tell the user exactly what to do:
1. `gcloud auth list` + active project set; permission to create instances.
2. GPU quota for 1× NVIDIA L4 in the chosen region (`gcloud compute regions describe`
   or attempt a dry-run create). Fallback if no GPU quota: high-mem CPU per runbook.
3. `HF_TOKEN` available and gated access GRANTED for `meta-llama/Llama-3.1-8B`
   (HTTP 200 on the API check above; 403 = user must accept the license on the HF
   site). Same check for `mistralai/Mistral-7B-v0.3` (Phase 2; non-blocking).
4. Confirm the driver input assets exist locally (the `months/` and `weekdays/`
   subdirectories the drivers reference — e.g. `months/baseline/`,
   `weekdays/baseline/`) and assemble the exact scp staging list.

## Phase 1 — Audit κ proper (the deliverable)

Per the runbook: create the transient VM (`g2-standard-8` + L4, spot, Deep Learning
VM image or Debian 12 + venv), stage scripts and assets, download Llama-3.1-8B, run
the layerwise sweep for BOTH tasks (months, weekdays), both arms (driver + lens).
Retrieve all JSONs, reports, and run logs into `empirical/reports/` locally.
Sanity gate before teardown: the final-layer values reproduced by the sweep must
match the already-measured anchors in the settlement record §2 (e.g. months
f₂ = 0.050608, f₃ = 0.066390, f₄ = 0.059082) — if they don't, capture environment
details and STOP for handoff (do not tune until they match).

## Phase 2 — Mistral-7B-v0.3 arm

Same sweep, if gated access is granted. If not granted: record the deferral with
reason and move on.

## Phases 3–4 — Conditional

Paper 39 (attention-sink Γ-law) and Paper 40 (σ-audit taxonomy extension) ONLY if
their driver scripts exist in `empirical/` and run as-is (check the manuscripts'
script inventories). If a driver is not finalized: record "driver not finalized,
skipped" — do NOT write new experiment code in this errand.

## Phase 5 — CCSAE (Paper 45)

OUT OF SCOPE. Do not start; it is a separately budgeted multi-hour training job.

## Teardown + settlement (required, even on partial failure)

1. Verify retrieved artifacts (file counts, JSON parse, row counts), then DELETE the
   instance. Record instance type, region, hours, and estimated cost.
2. Update `empirical/reports/layerwise_packet_spectroscopy_VM_audit_kappa.md`:
   replace the §1 deferral with the environment actually used and point to the new
   per-phase reports.
3. Land the measured outcomes in Paper 36 against the pre-registered predictions,
   each marked by the three-outcome rule (confirmed / refuted / ambiguous), per the
   papers-lead convention (results go in the manuscript, not standalone notes).
4. Final message: a P-by-P outcome table, anchors-reproduction check result, any
   driver diffs applied, cost, and what was deferred/skipped with reasons.
