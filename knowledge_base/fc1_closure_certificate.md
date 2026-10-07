# FC1 Closure Certificate

Created: 2026-05-15

## Status

FC1 is closed at the bounded finite-jet theorem scope.

The analytic theorem is not waiting on another census.  The theorem pieces are:

1. **FC1-A:** centroid finite-sufficient normalizer-equivariant quadratic
   macrovariable jets are conductor packet energies plus packetwise
   orthogonal refinements.
2. **FC1-B1:** at fixed finite adjacency/Fisher-jet order, finite-sufficient
   Hamiltonian differentials pull back through a finite observation map
   \(\Phi_{R,k}\), and exact decomposable Fisher-volume currents live in the
   exterior power of that finite module.
3. **FC1-C:** at fixed finite-jet order, off-centroid closure fails first by
   quotient-character adjacency carry; the filtered source is FC2's
   \([\kappa]\), with `K_CH`, H4, contraction shadows, and higher Fisher jets
   only visible projections modulo their kernels.

The finite atlas layer is now delivered as an exact bounded certificate for
the first mixed row `F4[u]/(u^2)`.

## Delivered Atlas Scope

The closure certificate is:

- `empirical/fc1_noether_atlas_final_certificate_f4_u2.py`;
- `empirical/reports/fc1_noether_atlas_certificate_f4_u2.json`;
- `empirical/reports/fc1_noether_atlas_certificate_f4_u2.md`.

It gathers the following exact finite layers:

| layer | artifact | delivered datum |
|---|---|---|
| base orbit skeleton | `empirical/reports/fc1_noether_atlas_census_f4_u2.md` | `637` seed coordinates, `592` `K_CH` commutator orbits, `20` carry-pair orbits |
| aggregate tuple baseline | `empirical/reports/fc1_noether_tuple_census_f4_u2_small.md` | \(C(24,14)=1,961,256\) supports; full stabilizer; trivial determinant baseline |
| selected size-12 chart | `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_selected.md` | `120` supports -> `15` normalizer orbits; `12` sign-nontrivial determinant orbit types |
| full size-24 chart | `empirical/reports/fc1_noether_moving_tuple_census_f4_u2_size24.md` | `40,116,600` supports -> `1,674,272` normalizer orbits; `1,248` sign-nontrivial determinant orbit types |
| carry-pair one-split atlas | `empirical/reports/fc1_noether_carry_pair_atlas_f4_u2.md` | all `20` carry-pair orbits assessed; `18` tuple-capable charts; `2` companion-coordinate charts |

Across the separate carry-pair one-split charts, not as a simultaneous atlas,
the certificate records `20,091,354` normalizer orbit types and `15,048`
sign-nontrivial determinant-character chart orbit types.

Every enumerated tuple chart inherits the residual label

```text
full/support/H4/H3/remaining = 1569/0/72/1470/27.
```

This keeps full filtered residual, support projection, H4 incidence,
H3-contraction visibility, and remaining hidden mass separate.

## Closure Verdict

FC1 is complete enough to stop being the active core dependency.  The next
core theorem target is FC3.

The exact finite atlas is a computer-assisted certificate, not empirical
neural evidence.  It complements the analytic proof by demonstrating the
Noether orbit/stabilizer/determinant/residual ledger on the first mixed row.

## Non-Claims

This closure does not claim:

- simultaneous enumeration of all \(C(637,14)\) tuple supports;
- all `K_CH` commutator coordinates split into individual moving charts;
- arbitrary smooth invariant functions inside a packet;
- all Fisher-volume-preserving currents;
- full filtered closure from support residual `0`;
- `K_CH` as an `Ext_CH` detector by itself;
- global sufficiency beyond the declared finite skeleton.

Those are not blockers for FC1 as bounded finite-jet theorem plus exact finite
atlas certificate.  They remain optional extensions or FC3/FC6-facing cost
refinements.

## FC3 Inputs Now Available

FC3 may now use the following FC1 outputs:

1. finite-sufficient macrovariable module \(\Omega^1_{R,k,\mathrm{nat}}\);
2. exact decomposable current convention for Hamiltonian tuples;
3. normalizer orbit/stabilizer/determinant atlas fields on the declared
   `F4[u]/(u^2)` skeleton;
4. tuple-level residual ledger
   `full/support/H4/H3/remaining = 1569/0/72/1470/27`;
5. explicit non-claim boundaries separating support closure, Fisher-shadow
   visibility, and full filtered closure.
