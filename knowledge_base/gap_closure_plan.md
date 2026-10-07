# Gap Closure Plan: Nonuniform Orthogonality And Finite-Row Proof Extraction

Created: 2026-05-14
Last updated: 2026-05-15

This file turns the two biggest current gaps into work packages.

## Executive Summary

The best coverage route is:

1. **Fisher-conductor bridge:** prove the full nonuniform orthogonality
   criterion in terms of the Fourier support of `m_p = 1/p`, then classify
   small cyclic and local rows as finite set problems.
2. **Quotient-character adjacency:** separate proof extraction from discovery
   computation. Each finite row should emit certificates that can be checked
   independently and cited as finite lemmas.
3. **Higher cohomology:** do not jump from support-level operadic boundaries to
   a cohomology theorem. First freeze the chain complex: objects, differential,
   signs, coefficient ring, `d^2 = 0`, normalizer action, and relation to the
   binary `Ext_CH` cocycle.

## Gap A: Full Nonuniform Fisher-Conductor Orthogonality Loci

### Theorem To Add

Let `R` be a finite additive output algebra, `hat R` its character group, and
`B_d` the set of nontrivial characters of conductor `d`. For `p in Delta_R^o`,
set `m_p(a) = 1/p_a`. In the additive-character basis,

```text
g_p(chi, psi) = hat(m_p)(psi chi^{-1}).
```

Therefore conductor packets `B_d` and `B_e` are Fisher-orthogonal at `p` iff

```text
hat(m_p)(eta) = 0
```

for every quotient `eta = psi chi^{-1}` with `chi in B_d`, `psi in B_e`, and
`d != e`.

Equivalently, the reciprocal density `m_p = 1/p` may have Fourier support only
in modes that do not translate a nontrivial character into a different
conductor packet.

### Why This Covers The Gap

The old statement was "generically destroyed, special symmetric cases remain."
The theorem above gives the exact special cases. The locus is the positive
part of a Fourier subspace, pushed through reciprocal normalization:

```text
choose positive m with supp(hat m) in Allowed,
p_x = (1/m_x) / sum_y (1/m_y).
```

This is nonlinear in `p`, but linear in the reciprocal density `m`.

### First Action Already Taken

Added and ran:

- `empirical/nonuniform_orthogonality_loci.py`
- `empirical/reports/nonuniform_orthogonality_loci_cyclic.md`
- `empirical/reports/nonuniform_orthogonality_loci_cyclic.json`

The cyclic atlas through `C_24` shows:

- prime `C_p`: one nontrivial packet, so conductor-block orthogonality is vacuous;
- prime powers `C_{p^a}`, `a >= 2`: nonconstant reciprocal modes survive in the top socle subgroup, e.g. `C_8` allows `0,4`, `C_9` allows `0,3,6`;
- mixed-prime cyclic rows like `C_6`, `C_10`, `C_12`, `C_15`, `C_24`: rigid, only constant reciprocal density preserves all conductor blocks.

### Second Action Already Taken

Added and ran:

- `empirical/local_nonuniform_orthogonality_loci.py`
- `empirical/reports/nonuniform_orthogonality_loci_local.md`
- `empirical/reports/nonuniform_orthogonality_loci_local.json`

The local atlas shows structured nonuniform reciprocal modes in the nilpotent
top layers: `F4[u]/(u^2)` allows the zero mode plus the conductor-`u` orbit,
`F4[u]/(u^3)` allows the zero mode plus the `u^2` orbit, `F2[u]/(u^4)` allows
`0,u^3`, `F2[u]/(u^5)` allows `0,u^4`, and `F8[u]/(u^2)` allows the zero mode
plus the conductor-`u` orbit.  The report now includes normalizer-orbit
compression and a `--check` mode that recomputes the JSON report.

### Next Mathematical Actions

1. Insert the theorem after `10.information_geometric_bridge.md` Proposition 6.1.
2. Add a corollary for cyclic `C_N`:
   - if `N` is prime, block orthogonality is vacuous;
   - if `N = p^a`, `a >= 2`, allowed reciprocal modes are multiples of `N/p`;
   - if `N` has at least two prime factors, allowed reciprocal modes are only `0`.
3. Generalize from cyclic groups to finite quotient rings by defining the
   conductor-preserving reciprocal mode set:

```text
A_R = {eta in hat R : cond(eta chi) = cond(chi)
       for all nontrivial chi with eta chi nontrivial}.
```

4. Compute `A_R` for the local rows already in Paper 11:
   `F4[u]/(u^2)`, `F2[u]/(u^4)`, `F16`, `F2[u]/(u^5)`, `F8[u]/(u^2)`.
5. Add a small "orthogonality loci" table to Paper 10 and cite the full
   machine report as an appendix artifact.

Status: item 1 is done in Paper 10 as Proposition 6.1A.  Items 2-5 remain
presentation work for the next manuscript pass.

### Falsifiers

- A nonuniform `p` whose reciprocal Fourier support intersects a forbidden
  quotient but whose blocks remain orthogonal would falsify the criterion.
- A cyclic classification counterexample would falsify the proposed cyclic
  corollary.
- Positivity can empty a formally allowed reciprocal subspace in some rows; this
  would narrow, not falsify, the Fourier-support theorem.

## Gap B: Proof Extraction For Finite Rows

### Current Situation

The finite arithmetic evidence is strong, but not all of it is in theorem-proof
form. The computation stack already contains the ingredients:

- `empirical/local_adjacency_constructor.py`
- `empirical/fisher_jet_functor.py`
- `empirical/hyper_adjacency_tower.py`
- `empirical/cocycle_reducer.py`
- `empirical/verify_local_adjacency_constructor.py`
- `empirical/verify_ext_ch_cocycle.py`
- `empirical/verify_next_local_row.py`
- reports under `empirical/reports/`

The extraction target is to turn each finite row into a certificate-backed
lemma, not just a report.

### Certificate Schema

Each finite row should emit a compact certificate:

```text
row_id
ring_presentation
coefficient_field
label_count
conductor_packets
normalizer_generators
quotient_shift_generators
closed_cell_counts_by_arity
orbit_counts_by_arity
raw_carry_atoms
raw_carry_pairs
pair_orbits
coboundary_model
coboundary_rank
residual_support
rational_or_modular_rank_certificate
script_version_or_hash
repro_command
```

Minimum certificate families:

- ring certificate: labels, addition table hash, conductor partition, normalizer
  generators/actions;
- shift certificate: each `(eta, source, target)` shift support, support
  distribution, composable-pair list;
- carry certificate: raw atom list, pair key, coefficient, path word, and
  direct-shift subtraction source;
- orbit certificate: representative, orbit size, stabilizer size, orbit
  coverage sum, missing entries;
- coboundary certificate: `C1/C2` basis definition, sparse coboundary columns,
  pivot rows, rank, residual normal form, and for modular rows a rank witness
  strong enough to justify the rational non-coboundary claim;
- ledger certificate: source report hashes plus full/support deficit ratios.

### Proof-Extraction Ladder

| Level | Claim type | Evidence needed | Output |
|---|---|---|---|
| L0 | Constructor correctness | ring presentation, label arithmetic, conductor packet partition | audited definitions and regression tests |
| L1 | Orbit enumeration | normalizer generators, orbit-stabilizer checks, canonical reps | finite orbit lemma |
| L2 | Carry cocycle | section definition, multiplication table, raw carry table | explicit 2-cocycle lemma |
| L3 | Non-coboundary | coboundary matrix, rank, residual normal form | finite cohomology/nontriviality lemma |
| L4 | Arity lift | contraction map, support lift, orbit image | support-level curvature/carry theorem |
| L5 | General theorem | family parameter proof independent of row enumeration | manuscript theorem |

### First Action Already Taken

Added and ran:

- `empirical/finite_row_certificates.py`
- `empirical/reports/finite_row_certificates.md`
- `empirical/reports/finite_row_certificates.json`

The certificate report currently compresses `F4[u]/(u^2)`, `F2[u]/(u^5)`, and
`F8[u]/(u^2)` into row counts, orbit counts, residual counts, and source
hashes.  It also has a `--check` mode that recomputes and compares the JSON
payload.  It is not yet a full pivot/residual proof checker, but it is now the
right citation target for finite-row proof extraction.

### Next Concrete Actions

1. Add a `--certificate` output mode to `verify_local_adjacency_constructor.py`
   and `verify_next_local_row.py`.
2. Make certificates small enough to review: hashes/counts/canonical reps, not
   giant orbit payloads.
3. Add an independent certificate checker script that recomputes only:
   arithmetic closure, orbit counts, coboundary rank, residual support.
4. For Paper 11, rewrite row claims as:
   - theorem if proved symbolically;
   - finite lemma if certified by exact enumeration;
   - computational evidence if only one script report exists;
   - conjecture if pattern extrapolates.
5. For `F8[u]/(u^2)`, keep the modular full-block rank certificate explicit:
   state which prime field was used and why the rank certifies the rational
   non-coboundary claim.

## Gap C: Higher Cohomology

### Status Update: FC2 Family Theorem Closed

FC2 no longer depends on finding a standalone cohomology of the closed
nontrivial hyper-adjacency tower.  The family theorem is solved by moving the
cohomological source back to the filtered quotient-character adjacency
extension class:

```text
[kappa] in the section-change/Hochschild 2-cohomology model
```

The hyper-adjacency boundary remains the Fisher-jet support shadow of that
class, modulo the Fisher-jet kernel.  See
`knowledge_base/fc2_family_theorem.md` and
`empirical/reports/fc2_family_certificate.md`.

### Do Not Overclaim Yet

The current support-level operadic boundary is useful, but higher
`Ext_CH^(n)` as a standalone hypercell cohomology is not publication-ready
until a separate augmented chain complex is fixed.  This is optional for FC2
rather than blocking FC2.

### Minimal Definition Freeze

Before proving higher cohomology, freeze:

1. coefficient ring: `Z`, `Q`, `F_p`, or row-native finite field;
2. oriented vs unordered cells;
3. adjacent-merge bar differential vs all-pair contraction differential;
4. sign convention;
5. closure rule after contraction;
6. normalizer equivariance;
7. exact relation between binary `kappa_s` and the degree-2 cochain.

Important correction: do not build higher cohomology on the current
nontrivial closed-cell contraction alone. If zero/trivial merges are discarded
before forming the differential, `d^2 = 0` can fail or become convention-bound.
The next complex should be an augmented closed-cell complex in which zero
labels and zero merges are retained through the differential, followed only
then by projection back to nontrivial hyper-adjacency support.

### Test Matrix

| Differential candidate | Pros | Risk | Next action |
|---|---|---|---|
| augmented adjacent bar differential | classical `d^2=0` proof available when zero merges remain | may not match Paper 11 all-pair support boundary | compare projected support image to H4 mixed orbit theorem |
| augmented all-pair contraction over `F_2` | matches unsigned support style in characteristic 2 | may be additive-group-only and miss ring/conductor filtration | use only as support diagnostic unless lifted |
| augmented signed all-pair contraction | closest to geometric alternating boundary | `d^2=0` must be checked, not assumed | compute small rows and find sign convention |
| filtered section-change complex | closest to binary `Ext_CH` | heavier and row-specific | build after certificate schema stabilizes |

### Next Concrete Actions

1. Create a note in Paper 11 saying higher `Ext_CH` is currently support-level
   unless/until this complex is frozen.
2. Run existing `compute_ext_ch_bar.py` and
   `compute_ext_ch_higher_arity_f2.py` only as exploratory diagnostics, not
   theorem evidence.
3. Create `empirical/cochain_complex_ext_ch.py` for the augmented-cell
   candidates, with an explicit `d^2` check before any cohomology dimensions
   are reported.
4. Build a small comparison report for `F4[u]/(u^2)`:
   - cells in arities 2-5;
   - rank of candidate differentials;
   - `d^2` status;
   - which H4 mixed support orbits are hit.
5. Select the smallest candidate complex whose degree-2 class recovers the
   existing binary cocycle representative.
6. Only then state `Ext_CH^(n)` as cohomology.

## Gap D: Critical-Leaf Tower Saturation

The critical-leaf problem is now distinct from support closure.  The current
finite audits show:

- neural cyclic proxies and selected local leaves can have zero support/K_CH
  leakage;
- exact full-block reductions on the tested local leaves still have residual
  deficit `1.0`;
- F2 suffix and F8 modular rows show decreasing orbit-normalized residual mass
  but not finite filtered closure.

Next actions:

1. repeat `streaming_modular_residual.py` over at least one additional odd
   prime;
2. extend the F2 suffix tower beyond `e=6`;
3. replace support-level H4-to-H3 cokernel with the full higher-current
   quotient once the complex is frozen;
4. decide whether the theorem target is normalized residual decay,
   quotient-level extinction, or exact filtered closure after a tower
   refinement.

Unsafe shortcut: treating zero support/K_CH leakage as full critical-leaf
closure.

## Work Order

1. **Now:** cite the reciprocal-density theorem and cyclic atlas as the first
   closure of the Fisher nonuniform-loci gap.
2. **Next:** add local-row orthogonality-loci computation using the existing
   local adjacency constructor.
3. **Then:** implement finite-row certificate output/checking.
4. **Then:** freeze the higher cohomology complex by comparing augmented
   bar/all-pair/filtered-section candidates on `F4[u]/(u^2)`.
5. **Finally:** revise Paper 10 and Paper 11 with theorem/lemma/conjecture
   labels that match the evidence level.

Status on 2026-05-15: steps 1 and 2 are done; step 3 has a first certificate
ledger with reproducibility checking, but still needs smaller proof objects and
independent pivot/residual certificates.  Gap D is now separated from support
closure and routed through the critical-leaf/tower audits.
