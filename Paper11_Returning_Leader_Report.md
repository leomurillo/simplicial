# Paper 11 Returning Leader Report

**Date:** May 11, 2026
**Prepared for:** returning project lead
**Primary artifact:** `11.quotient_character_adjacency_algebras.md`
**Status:** no Heaven escalation is indicated.

## May 12 Addendum

The manuscript now records the algebra-first interpretation explicitly:
\(\operatorname{Ext}_{CH}\) is represented by the carry \(2\)-cocycle of the
local filtered multiplication law over the tame/wild associated graded.  The
existing finite rows are therefore regression evidence for the next
constructor, not the intended long-term discovery mechanism.

The first constructor pass has landed:
`empirical/local_adjacency_constructor.py` builds the finite local packets,
quotient-shift generators, normalizer action, and carry table; and
`empirical/fisher_jet_functor.py` supplies the analytic \(M,B^\tau,B^\omega,C\)
pieces over that constructor.  The next layer,
`empirical/hyper_adjacency_tower.py`, packages the arity cells, orbits, and
pair contractions.  `empirical/cocycle_reducer.py` now exports the canonical
\(\operatorname{Ext}_{CH}\) cocycle representative: \(1569\) raw atoms,
\(369\) carry pairs, \(71\) atom orbits, and \(20\) pair orbits for the F4
row.  `empirical/verify_local_adjacency_constructor.py` verifies the F4 row
plus the two \(Q_f=16\) controls.  The generated reports are
`empirical/reports/local_adjacency_constructor_f4_u2.md` and
`empirical/reports/ext_ch_cocycle_f4_u2.md`.

## What Changed

Paper 11 has moved from a framework draft to a measured local row for

$$
R={\mathbb F}_4[u]/(u^2).
$$

The manuscript now records:

1. the quotient-character adjacency algebra and CRT/local-normalizer setup;
2. the centroid normalization \(c=1\);
3. the first mixed \(srt^2\) representative of \(\operatorname{Ext}_{CH}\);
4. the arity-2 normalizer census: \(4438\) full-defect orbits, \(592\)
   commutator orbits, and collision-free local signatures;
5. the arity-3 atlas: \(210\) closed cells and five
   \(\Gamma_R\times S_3\)-orbits;
6. the arity-4 skeleton: \(3165\) closed cells and \(18\)
   \(\Gamma_R\times S_4\)-orbits;
7. the support-level arity-4 curvature theorem: the \(592\) arity-2
   commutator orbits lift exactly onto the seven mixed TTWW/TWWW arity-4
   orbits and onto no pure TTTT/WWWW orbit;
8. the paired-slot coefficient rule on the full mixed lift:
   \[
   R^{(4)}=-1:44,\qquad R^{(4)}=1:504,\qquad R^{(4)}=2:44.
   \]
9. the H4-to-H3 contraction audit: \(18990\) candidate pair contractions,
   \(17640\) valid, all \(5\) H3 orbits hit, and \(16/18\) H4 orbits valid;
10. the two \(Q_f=16\) control atlases: \({\mathbb F}_2[u]/(u^4)\) has
    arity \(3:210/7\), arity \(4:3165/32\); \({\mathbb F}_{16}\) has arity
    \(3:210/2\), arity \(4:3165/7\).

## Attention Point

The old ambiguity was coefficient scope.  The inherited arity-2 commutator
sign is now used only as a support selector.  Signed arity-4 coefficients are
computed independently by the paired-slot Bianchi projection, equivalently the
\(NC_4\) contraction that remains after the unrestricted \(\Pi_4\) Leibniz
expansion.

The sealed target cell returns

$$
R^{(4)}(u,1,1,u)_{u\leftarrow u}=-1,
$$

and the full mixed-lift table scans all \(592\) support records.

## Boundary

Do not claim a full cohomological construction of
\(\operatorname{Ext}_{CH}^{(4)}\) or an operadic composition law.  Those are
future research targets, not blockers for Draft 0.3.1.

## Leader Packet

The packet is intentionally small but now includes the measured finite row:

1. `11.quotient_character_adjacency_algebras.md`;
2. `empirical/local_adjacency_constructor.py`;
3. `empirical/fisher_jet_functor.py`;
4. `empirical/hyper_adjacency_tower.py`;
5. `empirical/cocycle_reducer.py`;
6. `empirical/verify_local_adjacency_constructor.py`;
7. `empirical/verify_ext_ch_cocycle.py`;
8. `empirical/reports/local_adjacency_constructor_f4_u2.md`;
9. `empirical/reports/ext_ch_cocycle_f4_u2.md`;
10. `empirical/reports/f4_u2_ext_ch.md`;
11. `empirical/reports/f4_u2_ext_orbits.json`;
12. `empirical/reports/h3_f4_u2.md`;
13. `empirical/reports/h4_f4_u2_audit.md`;
14. `empirical/reports/h4_f4_u2_curvature_lift.md`;
15. `empirical/reports/h4_R4_covariant_target_cell.md`;
16. `empirical/reports/h4_R4_covariant_full_mixed_lift_table.md`;
17. `empirical/reports/h4_to_h3_contractions.json`;
18. `empirical/reports/f2_u4_atlas.json`;
19. `empirical/reports/f16_atlas.json`.

Everything else is provenance or team diagnostics unless the lead asks to
audit the computation.
