# FC3-B Local Split-Ledger Theorem

Created: 2026-05-15

## Status

This note continues FC3 after FC3-A.  FC3-A established the theorem shape:
generated-subgroup descent is the finite-abelian zero-structural baseline,
normalizer saturation is paid by the B4 premium rule, and certified local rows
must price full filtered carry separately from support projection.

FC3-B is the local projection-cost extension:

> On every currently certified FC2 local row with an atom-shadow and
> H4-to-H3 contraction certificate, the FC3 carry ledger decomposes as
> full/support/H4/H3/remaining, and support-only pricing underprices the row
> whenever the full filtered residual survives.

## Theorem Candidate

**FC3-B. Local split-ledger theorem at current certified-row scope.**  Let
\(R\) be a local conductor row for which the FC2 row classifier supplies:

1. a full-block filtered residual for the section class `[kappa_R]`;
2. the raw-support support-projection residual;
3. an atom-boundary H4 incidence map against the visible Fisher-shadow image;
4. an H4-to-H3 contraction-shadow refinement.

Then the local FC3 carry cost is the separated vector

```text
C_FC3(R) =
  full_filtered_residual
  + support_projection_residual
  + H4_visible_atoms
  + H3_contraction_visible_atoms
  + remaining_hidden_atoms.
```

The fields satisfy

```text
H4_visible_atoms
+ H3_contraction_visible_atoms
+ remaining_hidden_atoms
= full_filtered_residual.
```

If `support_projection_residual = 0` and `full_filtered_residual > 0`, any
scalarization that prices local carry only by support projection underprices
the local row by exactly

```text
full_filtered_residual - support_projection_residual.
```

## Certified Rows

The exact certificate is:

- `empirical/fc3_local_split_ledger.py`;
- `empirical/reports/fc3_local_split_ledger.md`;
- `empirical/reports/fc3_local_split_ledger.json`.

It covers:

| row | full | support | H4 | H3 | remaining |
|---|---:|---:|---:|---:|---:|
| `F4[u]/(u^2)` | 1569 | 0 | 72 | 1470 | 27 |
| `F2[u]/(u^5)` | 19140 | 0 | 5424 | 13618 | 98 |
| `F8[u]/(u^2)` | 158081 | 0 | 784 | 157178 | 119 |
| `F16` field control | 225 | 0 | 0 | 0 | 225 |
| `F2[u]/(u^4)` wild control | 1540 | 0 | 368 | 1138 | 34 |

Aggregate current-row ledger:

```text
full/support/H4/H3/remaining = 180555/0/6648/173404/503.
```

Thus the aggregate support-only underpricing gap is `180555` atoms.

## Proof

FC2 identifies the filtered section class `[kappa_R]` as the source of local
carry.  The full-block residual is the coefficient-level residual of that
class in the certified row classifier.  The support-projection residual is a
quotient/projection of this residual, not a proof of filtered triviality.

The atom-shadow map then partitions residual representatives by whether their
atom-boundary H4 orbit is incident to the tested visible Fisher-shadow image.
The H4-to-H3 contraction certificate refines the H4-invisible mass by asking
whether a pair contraction lands in the generated H3 shadow.  What remains is
the tested hidden residual.  By construction, the three visibility fields sum
to the full residual.

The underpricing claim is arithmetic: a support-only scalarization assigns
cost `support_projection_residual`; the filtered ledger assigns at least
`full_filtered_residual` to the aggregate full-filtered channel.  Their gap is
the stated difference.

## FC3 Reading

FC3-A, FC3-B, and FC3-C now solve the first bounded information-investment
layer:

1. generated-subgroup descent is the finite-abelian zero-carry baseline;
2. normalizer saturation is a resource-weighted transfer decision;
3. local filtered carry has an exact split ledger on the current certified
   rows;
4. support residual zero is never allowed to stand in for full filtered
   closure;
5. admissible task-dependent scalar weights are available in full-filtered
   audit mode or H4/H3/remaining visibility-partition mode.

The remaining FC3 work is not to redefine the theorem.  It is to extend the
same split ledger to more local rows and richer coefficient/higher-arity
hidden-residual observables without collapsing projection channels.

## Boundaries

FC3-B does not claim:

- the full FC1 Noether tuple atlas exists for every row in the table;
- H4 or H3 visibility detects `Ext_CH` by itself;
- support residual `0` is full filtered closure;
- the remaining hidden mass is zero outside the tested channels;
- learned-model behavior has paid these costs;
- downstream Bures, FEP, transformer, primorial, or RH material belongs in
  the core FC3 proof spine.
