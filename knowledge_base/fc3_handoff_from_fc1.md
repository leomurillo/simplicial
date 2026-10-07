# FC3 Handoff From FC1

Created: 2026-05-15

## Purpose

FC1 is now closed at bounded finite-jet theorem scope with an exact finite
Noether-atlas certificate for `F4[u]/(u^2)`.  This note defines what FC3 may
import from FC1 and what it must still prove itself.

## Importable FC1 Data

FC3 may use these as established inputs:

| input | status | source |
|---|---|---|
| centroid packet-energy naturality | theorem | `knowledge_base/fc1_centroid_classification_theorem.md` |
| finite-sufficient differential module | theorem | `knowledge_base/fc1_exact_differential_module_theorem.md` |
| off-centroid first carry obstruction | theorem | `knowledge_base/fc1_off_centroid_closure_theorem.md` |
| bounded Noether atlas certificate | exact finite certificate | `empirical/reports/fc1_noether_atlas_certificate_f4_u2.md` |
| tuple residual ledger | exact finite certificate | `full/support/H4/H3/remaining = 1569/0/72/1470/27` |

## FC3 Theorem Candidate

The next theorem target should be a bounded information-investment theorem:

> For finite abelian rows and certified local rows with declared finite
> macrovariable skeletons, the information-investment functional
> \(\mathcal J_\infty\) decomposes into generated-subgroup descent,
> normalizer symmetry premium, and off-centroid carry costs.  The minimizer
> uses generated-subgroup closure by default, pays the normalizer premium
> exactly when the transfer gain exceeds resource cost, and charges filtered
> carry through the full/support/H4/H3/remaining residual ledger rather than
> through support closure alone.

This should be proved first for:

1. cyclic and finite abelian rows using B1/B2/B3/B4;
2. the certified local `F4[u]/(u^2)` bounded atlas using FC1/FC2 labels;
3. then the existing mixed local row verifier/A0 rows only after the cost
   terms are explicitly matched to their certificates.

This target is now launched as:

- `knowledge_base/fc3_bounded_information_investment_theorem.md`;
- `knowledge_base/fc3_local_split_ledger_theorem.md`;
- `knowledge_base/fc3_weighted_mixed_row_theorem.md`;
- `empirical/fc3_bounded_cost_ledger_f4_u2.py`;
- `empirical/reports/fc3_bounded_cost_ledger_f4_u2.md`;
- `empirical/reports/fc3_bounded_cost_ledger_f4_u2.json`;
- `empirical/fc3_local_split_ledger.py`;
- `empirical/reports/fc3_local_split_ledger.md`;
- `empirical/reports/fc3_local_split_ledger.json`.

The chosen first theorem is FC3-A: the cyclic/finite-abelian
generated-subgroup theorem plus the normalizer premium rule, extended only as
far as the certified `F4[u]/(u^2)` split-cost ledger.  The row-universal
mixed-row A0/J_infty unification remains deferred until the same separated
cost fields are available row by row.

The local projection-cost continuation is FC3-B: across the current exact FC2
row-classifier scope, the aggregate ledger is
`full/support/H4/H3/remaining = 180555/0/6648/173404/503`.  This extends the
support-underpricing rule beyond the first Noether-atlas row without claiming
that all rows have the full FC1 tuple atlas.

The weighted mixed-row continuation is FC3-C: task-dependent scalar weights may
now be attached to the split ledger and to the bounded mixed-row A0/J_infty
statement, provided the scalarization uses either the full-filtered audit mode
or the H4/H3/remaining visibility-partition mode and does not double-count
`full` against its partition.

## Cost Fields FC3 Must Keep Separate

FC3 must not collapse the following channels:

| cost field | meaning |
|---|---|
| generated-subgroup closure | minimal B2 support investment |
| normalizer premium | extra B3 resource paid for equivariance/transfer |
| support projection residual | support-level closure channel; currently `0` on the F4/u2 FC1 atlas |
| full filtered residual | true filtered section-change mass; `1569` on F4/u2 |
| H4-visible mass | Fisher-shadow incidence channel; `72` on F4/u2 |
| H3-contraction visible mass | weaker contraction-shadow channel; `1470` on F4/u2 |
| remaining hidden mass | still invisible to tested H4/H3 channels; `27` on F4/u2 |

## Proof Obligations For FC3

1. State \(\mathcal J_\infty\) with explicit resource weights for support,
   normalizer, full filtered residual, H4-visible mass, H3-contraction mass,
   and remaining hidden mass.  Done at bounded mixed-row scope in FC3-C, with
   full-filtered audit mode and visibility-partition mode kept separate.
2. Prove the cyclic/finite-abelian generated-subgroup minimizer remains the
   zero-carry baseline.
3. Prove the normalizer premium rule using the existing B3/B4 transfer
   criterion.
4. Add the local-row correction: a policy that pays only support closure is
   underpriced when full filtered residual survives.  Checked on the first
   local ledger by the gap `1569 - 0 = 1569`.
5. Instantiate the theorem on `F4[u]/(u^2)` using the FC1 atlas certificate
   without treating `K_CH` as an `Ext_CH` detector.  The current ledger records
   `72 + 1470 + 27 = 1569` as a visibility partition, not as a standalone
   detection theorem.

## Boundaries

FC3 may not claim:

- support residual `0` implies full filtered closure;
- `K_CH` detects `Ext_CH` by itself;
- quotient sufficiency is global rather than relative;
- arbitrary smooth invariants are classified by FC1;
- learned-model transfer is proved by the finite atlas alone.

The learned and optimizer branches remain FC4/FC5, downstream of the bounded
FC3 resource theorem.
