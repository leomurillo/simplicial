# Critical Leaf Closure Theorem Candidate

Created: 2026-05-14

This note states the closure theorem suggested by the current finite evidence
stack.  It is not yet a theorem.  Its purpose is to pin down the exact limit
claim that would turn the critical-leaf census into a proof-grade result, and
to keep the measured finite obstruction visible.

## Empirical Status

The current executable stack has three layers.

| layer | script | measured object |
|---|---|---|
| neural cyclic proxy | `empirical/critical_leaf_projection.py` | K_CH cubic size, closure leakage, balanced leakage on cyclic conductor leaves |
| local support atlas | `empirical/local_row_balanced_leakage.py` | active carry-path leakage on saved Ext_CH rows |
| filtered leaf residual | `empirical/per_leaf_coboundary_audit.py` | leaf-restricted full-block coboundary residual |

The cross-mode summary is:

```text
empirical/reports/cross_mode_critical_leaf_summary.md
```

The sharp finite finding, after adding C2-volume and orbit-quotient
normalized columns, is:

| row | selected leaf | support/KCH balanced leakage | full-block deficit | nu_E residual | C2 orbit volume | residual orbit support | orbit residual mass | H3 orbits | H4 orbits | H4->H3 cokernel |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C7 Llama/Mistral proxy | full nontrivial | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| C12 Llama proxy | conductor_3, after excluding flat conductor_2 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| F_4[u]/(u^2) | u^2 | 0 | 1 | 0.015625 | 1552 | 26 | 0.016753 | 2 | 9 | 0 |
| F_2[u]/(u^2) | u+u^2 | 0 | 1 | 0.065574 | 31 | 2 | 0.064516 | 1 | 4 | 0 |
| F_2[u]/(u^3) | u^2+u^3 | 0 | 1 | 0.032787 | 136 | 6 | 0.044118 | 1 | 8 | 0 |
| F_2[u]/(u^4) | u^3+u^4 | 0 | 1 | 0.016393 | 612 | 20 | 0.032680 | 1 | 16 | 0 |
| F_2[u]/(u^5) | u^4+u^5 | 0 | 1 | 0.008197 | 2544 | 48 | 0.018868 | 1 | 28 | 0 |
| F_2[u]/(u^6) modular | u^5+u^6 | n/a | 1 | 0.004098 | 10496 | 116 | 0.011052 | n/a | n/a | n/a |
| F_8[u]/(u^2) modular | u^2 | 0 | 1 | 0.001953 | 76480 | 152 | 0.001987 | 4 | 53 | 0 |

Thus the minimizing leaves are support-closed, but the filtered full-block
residual does not vanish in the exact local leaf audits completed so far.
The C2-volume normalized residual mass and the orbit-quotient residual mass
both decay along the F2 suffix tower, but the relative `nu_lambda^E` deficit
remains `1.0`.  The support-level H4-to-H3 orbit cokernel is already zero on
the selected local rows.  The closure theorem must therefore identify whether
this quotient-level saturation promotes to full filtered Ext/hyper-adjacency
saturation in the tower, rather than treating finite support closure as enough.

The first suffix-leaf tower scan for `F_2[u]/(u^e)` on the top-two suffixes
keeps the active-atom-normalized and relative `nu_lambda^E` residual flat,
while the absolute C2-volume mass decays.  The `e=6` row is now reduced
modulo `1000003`, so its quotient-pressure datum has become modular
residual-orbit data.  The dedicated tower quotient report is:

```text
empirical/reports/tower_quotient_saturation.md
```

| row | suffix leaf | raw support | residual support | nu_E residual | C2 orbit volume | residual orbit support | orbit residual mass | H4 orbits |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| F_2[u]/(u^2) | u+u^2 | 4 | 4 | 0.065574 | 31 | 2 | 0.064516 | 4 |
| F_2[u]/(u^3) | u^2+u^3 | 32 | 32 | 0.032787 | 136 | 6 | 0.044118 | 8 |
| F_2[u]/(u^4) | u^3+u^4 | 256 | 256 | 0.016393 | 612 | 20 | 0.032680 | 16 |
| F_2[u]/(u^5) | u^4+u^5 | 2048 | 2048 | 0.008197 | 2544 | 48 | 0.018868 | 28 |

The first modular residual extension beyond the rational reduction frontier is:

| row | suffix leaf | field | residual support | nu_E residual | C2 orbit volume | residual orbit support | orbit residual mass | residual deficit |
|---|---|---|---:|---:|---:|---:|---:|---:|
| F_2[u]/(u^6) | u^5+u^6 | F_1000003 | 16384 | 0.004098 | 10496 | 116 | 0.011052 | 1 |

The same streaming modular reducer also gives:

| row | suffix leaf | field | residual support | nu_E residual | C2 orbit volume | residual orbit support | orbit residual mass | residual deficit |
|---|---|---|---:|---:|---:|---:|---:|---:|
| F_8[u]/(u^2) | u^2 | F_1000003 | 25088 | 0.001953 | 76480 | 152 | 0.001987 | 1 |

These modular rows are not rational closure proofs.  They do show that the
large-row quotient pressure is not merely raw support: after full modular
section-change reduction, the residual still equals the raw carry on these
selected leaves.

This does not prove closure: no tested row has killed the residual.  It does
narrow the theorem target to the difference between absolute normalized carry
mass decay, orbit-quotient saturation, and relative Ext/hyper-adjacency
saturation.

## Definitions

Let `(R_lambda, A_lambda)` be a cofinal arithmetic tower of finite
quotient-character atlases, compatible with CRT decomposition into local
factors.  Let `S_lambda` denote a conductor packet leaf, and write

```text
E_lambda(S)       = Ext_CH-generated residual on S,
H_A,lambda(S)     = full filtered residual on S,
H_hyp,lambda(S)   = higher hyper-adjacency quotient on S.
```

The finite exact sequence of Paper 13 is

```text
0 -> E_lambda(S) -> H_A,lambda(S) -> H_hyp,lambda(S) -> 0.
```

Let

```text
delta_lambda(S)
  = residual_support_lambda(S) / raw_support_lambda(S)
```

be the leaf-restricted full-block residual deficit computed by the
coboundary reducer when that finite audit is available.  Let

```text
L_lambda(S)
```

be the norm-valued balanced leakage budget: in cyclic neural proxy rows this
is the average `rho_frac * sqrt(closure_leakage_fraction)`, and in local
atlas rows it is the active carry leakage fraction weighted by full-block
residual survival.

Call a leaf `S_lambda` admissible if it is nonempty, regular in the atlas, and
does not owe zero leakage only to a quadratically flat K_CH response.

Define the finite critical leaf candidates by

```text
Crit_lambda
  = argmin { L_lambda(S) : S admissible }.
```

When several admissible leaves have zero balanced leakage, break ties by:

1. minimal full-block residual deficit, if measured;
2. maximal retained Fisher/carry mass;
3. conductor inclusion minimality inside the same CRT local factor.

## Candidate Theorem

**Critical Leaf Closure Theorem (candidate).**  Let
`{(R_lambda,A_lambda)}` be a CRT-compatible arithmetic tower whose finite
atlases satisfy the Mittag-Leffler hypotheses of Theorem 14.16 and whose
critical candidates `Crit_lambda` are eventually nested under conductor
projection.  Then the following are equivalent.

1. **Asymptotic filtered closure.**

   ```text
   lim_lambda delta_lambda(Crit_lambda) = 0
   ```

   after the canonical tower normalization by raw carry mass, orbit volume,
   or the normalized carry measure `nu_lambda^E`.

2. **Hyper-adjacency extinction on the critical leaf.**

   ```text
   lim H_hyp,lambda(Crit_lambda) = 0
   ```

   in the Mittag-Leffler inverse limit.

3. **Ext saturation.**

   ```text
   H_A,infty(Crit) = E_infty(Crit).
   ```

   Equivalently, every closed Fisher-current residual on the limiting
   critical leaf is generated by local `Ext_CH` carry classes.

4. **Zero long-time conductor leakage.**  For every interior periodic orbit
   and every heteroclinic arc supported on the limiting critical leaf, the
   Theorem 14.13 leakage budget vanishes in the tower limit:

   ```text
   lim_lambda \overline L_{Crit_lambda} = 0,
   lim_lambda \Lambda_{Crit_lambda} = 0.
   ```

Moreover, if `S_lambda` is an admissible leaf not eventually equal to
`Crit_lambda`, then at least one of the following persists along a cofinal
subtower:

```text
liminf L_lambda(S_lambda) > 0,
liminf delta_lambda(S_lambda) > 0,
lim H_hyp,lambda(S_lambda) != 0.
```

This is the precise form of "only the critical conductor leaf closes."

## RH Bridge Form

To use the theorem in the Riemann Hypothesis reduction, one needs the
additional analytic recovery hypothesis:

```text
closed currents on Crit  <->  explicit-formula Dirichlet/Euler data
```

under the additive-character convolution and CRT product limit.  With that
identification, off-leaf closed currents would be excluded by positive
leakage or nonzero hyper-adjacency obstruction, and the surviving closed
currents would lie on the critical conductor leaf.  This is the finite
arithmetic shadow of the critical line.

## What The Current Data Prove

The data do not prove the candidate theorem.  They prove the following finite
facts.

1. The executable cyclic proxy identifies zero balanced leakage leaves:
   `full_nontrivial` in C7 and `conductor_3` as the best non-flat leaf in C12.
2. The local atlas support metric identifies zero support-leakage leaves:
   `u^2`, the F2 suffix leaves, and `u^2` in the tested mixed rows.
3. The per-leaf full-block audits show residual deficit `1.0`,
   residual/active-atom mass `1.0`, and nonzero residual/orbit mass on all
   exact selected local leaves currently small enough to reduce.
4. The top-two suffix scan for `F_2[u]/(u^e)`, `e=2,3,4,5`, keeps
   residual/active-atom mass `1.0` and relative `nu_lambda^E` deficit `1.0`,
   while absolute C2-volume normalized residual mass halves at each step from
   `e=2` to `e=5`.
5. The same scan gives exact C2 orbit quotient volumes
   `31, 136, 612, 2544`, residual orbit supports `2, 6, 20, 48`, and
   orbit residual masses `0.064516, 0.044118, 0.032680, 0.018868`.
   The support-level H4-to-H3 orbit cokernel is `0` on every selected local
   row measured, including the size-gated `F_8[u]/(u^2)|u^2` row.
6. The streaming modular reducer over `F_1000003` completes the
   `F_2[u]/(u^6)` and `F_8[u]/(u^2)` selected leaves.  Both have modular
   residual deficit `1.0`, residual equal to raw support, and residual orbit
   masses `0.011052` and `0.001987`, respectively.

Therefore the theorem cannot be stated as finite exact closure on the
currently audited leaves.  It must be a tower statement or a statement with
an additional quotient-refinement mechanism that kills the surviving
full-block residual.

## Proof Obligations

The closure theorem reduces to five concrete obligations.

1. **Leaf nesting.**  Prove that the finite minimizers `Crit_lambda` are
   compatible under tower projection, after removing quadratically flat
   degeneracies.

2. **Normalized residual decay.**  Find the correct normalization
   `a_lambda` such that

   ```text
   a_lambda * dim H_hyp,lambda(Crit_lambda) -> 0
   ```

   or equivalently

   ```text
   delta_lambda(Crit_lambda) -> 0.
   ```

3. **Off-leaf separation.**  Prove that every other admissible leaf keeps
   positive leakage, positive residual deficit, or a nonzero limiting
   hyper-adjacency quotient.

4. **CRT additivity.**  Show that local critical leaves combine by CRT
   direct sum/tensor product without creating hidden mixed carry that can
   cancel the local obstruction off the critical leaf.

5. **Analytic recovery.**  Prove that the limiting closed-current generating
   function on the critical leaf recovers the zeta explicit formula: additive
   convolution gives the sum side, CRT tensor product gives the Euler product.

## Next Finite Certificates

The next finite tasks are ordered by payoff.

1. Repeat the streaming modular residual audit over at least one additional
   odd prime, so the large-row nonclosure signal is not tied to a single
   finite-field specialization.

2. Promote the current quotient-level observables into the theorem language:
   C2 orbit quotient volume, residual orbit support, orbit residual mass, H3/H4
   support orbit dimensions, and H4-to-H3 support orbit cokernel.  The current
   report also records raw support, residual support, residual deficit, active
   atom mass, orbit-normalized residual, packet-mass-normalized residual,
   C2-volume raw mass, C2-volume residual mass, and C2-volume deficit.

3. Extend `F_2[u]/(u^e)` for `e=7,8,...` on suffix leaves
   `{u^{e-1},u^e}` and `{u^m,...,u^e}`.  The deciding pattern is whether
   the full-block deficit remains `1.0`, decays after C2/orbit/hyper quotient
   normalization, or eventually drops exactly.  The first top-two suffix scan
   through `e=5` remains flat at `1.0` under active-atom and relative
   C2-volume normalization, but its absolute C2-volume residual mass decays;
   the modular `e=6` residual row continues the decay while retaining
   residual deficit `1.0`.

4. Replace the support-level H4-to-H3 orbit cokernel with the full higher
   current quotient rank once the finite complex presentation is in place.

5. Create certificate-backed lemmas for each finite row so the theorem can
   cite checkable finite facts rather than raw reports.

## Falsifiers

The candidate theorem should be rejected or revised if any of the following
occurs.

1. A deeper tower row has a noncritical admissible leaf with the same zero
   balanced leakage and lower normalized full-block residual.
2. The critical leaf residual deficit stays `1.0` under every natural
   normalization across increasing conductor depth.
3. The hyper-adjacency quotient stabilizes to a nonzero inverse-limit class
   on the critical leaf.
4. The analytic recovery map sends off-leaf residual classes to legitimate
   closed currents in the zeta explicit formula.

## Safe Public Statement

The safe current statement is:

> The finite census identifies conductor leaves with zero support/K_CH
> leakage, but exact leaf-restricted full-block audits show that the filtered
> residual still survives in the first tested local rows.  The remaining
> theorem is an asymptotic Ext-saturation statement: prove that the
> hyper-adjacency quotient vanishes in the tower limit exactly on the
> minimizing conductor leaf.

The unsafe current statement is:

> The finite rows already prove full critical-leaf closure.
