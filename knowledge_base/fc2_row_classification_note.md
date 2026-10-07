# FC2 Row Classification Note

Created: 2026-05-14

This note starts the FC2 classification phase after the source theorem.  It
does not reopen FC2: the cohomological source remains the filtered section
class \([\kappa_R]\).  The new object of study is the row-by-row visibility of
that class under exact projections and Fisher-jet shadows.

## Classification Problem

For each finite local row \(R\), record:

1. whether \([\kappa_R]\ne 0\), measured by the full-block section-change
   residual;
2. which projection kernels erase it, beginning with the raw-support
   support-gauge quotient;
3. which part is visible in the cubic \(K^{CH}\) commutator and higher
   hyper-adjacency Fisher shadows, only where an exact lift certificate has
   been computed;
4. the Hayes/Galois normalizer orbit decomposition of raw atoms, carry pairs,
   and closed H3/H4 families.

The reproducible classifier is:

- `empirical/fc2_row_classifier.py`
- `empirical/reports/fc2_row_classification.md`
- `empirical/reports/fc2_row_classification.json`
- `empirical/fc2_visible_fisher_kernel.py`
- `empirical/reports/fc2_visible_fisher_kernel.md`
- `empirical/reports/fc2_visible_fisher_kernel.json`
- `empirical/fc2_atom_shadow_map.py`
- `empirical/reports/fc2_atom_shadow_map.md`
- `empirical/reports/fc2_atom_shadow_map.json`
- `empirical/fc2_h4_contraction_shadow.py`
- `empirical/reports/fc2_h4_contraction_shadow.md`
- `empirical/reports/fc2_h4_contraction_shadow.json`

## Finite-Atlas Support-Kernel Proposition

In the current exact classifier run, every measured row has a nonzero
full-block filtered residual, while the raw-support support projection has
residual `0`.

| row | full residual | support residual | support erasure | K_CH / higher shadow status |
|---|---:|---:|---:|---|
| `F4[u]/(u^2)` | `1569` | `0` | `1569` | complete: `592/592` commutator orbits lift to `7/7` mixed H4 and `0/11` pure H4 orbits |
| `F2[u]/(u^5)` | `19140` | `0` | `19140` | exact visible shadow after streaming extraction: `6656/6656` commutator orbits lift to `43/43` mixed H4 and `0/29` pure H4 orbits |
| `F8[u]/(u^2)` | `158081` | `0` | `158081` | exact visible shadow after sparse extraction: `17944/17944` commutator orbits lift to `30/30` mixed H4 and `0/56` pure H4 orbits |
| `F16` field control | `225` | `0` | `225` | no conductor-mixed mode pairs, so mixed-conductor K_CH is empty |
| `F2[u]/(u^4)` wild control | `1540` | `0` | `1540` | exact visible shadow: `1148/1148` commutator orbits lift to `17/17` mixed H4 and `0/15` pure H4 orbits |

Thus raw-support closure is not a filtered-closure certificate.  More sharply:
`F4[u]/(u^2)` has support residual `0` under this quotient but has a certified
nonzero cubic/arity-4 Fisher shadow.  The support quotient is therefore a
properly lossy projection, not \(K^{CH}\) itself.

## Visible Fisher-Jet Kernel Layer

The second classifier layer tests the conductor-mixed \(K^{CH}\) commutator
support under the `FisherJet` functor and the input-side H4 lift.  It records
exact orbit tables where feasible and deterministic gated profiles where the
current extractor is too expensive.

| row | mixed mode pairs | K_CH entries | K_CH orbits | input-side H4 lift | status |
|---|---:|---:|---:|---|---|
| `F4[u]/(u^2)` | `36` | `14112` | `592` | `592/592` H2; mixed `7/7`, pure `0/11` | exact regression |
| `F2[u]/(u^5)` | `310` | `558000` | `6656` | `6656/6656` H2; mixed `43/43`, pure `0/29` | exact stress row |
| `F8[u]/(u^2)` | `392` | `3013696` | `17944` | `17944/17944` H2; mixed `30/30`, pure `0/56` | exact stress row |
| `F2[u]/(u^4)` | `70` | `27440` | `1148` | `1148/1148` H2; mixed `17/17`, pure `0/15` | exact control |
| `F16` | `0` | `0` | `0` | empty mixed channel | exact empty control |

This layer does not by itself assign individual full filtered residual atoms
to an `Ext_CH` detection class.  \(K^{CH}\) remains a Fisher-jet shadow of
\([\kappa]\), not a standalone `Ext_CH` atom detector.

## Coefficient-Level Atom Shadow Map

The third classifier layer maps each full filtered residual atom to its closed
H4 atom-boundary support cell
\[
(\eta_L,\eta_R,\mathrm{input},\mathrm{output}).
\]
Because the current atlas has `full_block_residual_equal_raw=true`, raw carry
atoms are valid coefficient-level residual representatives.  The map then
checks whether the atom-boundary H4 orbit is incident to the already certified
input-side H4 image of the \(K^{CH}\) Fisher shadow.  This is an H4-support
incidence flag, not an `Ext_CH` detector claim for \(K^{CH}\).

| row | support-erased atoms | K_CH H4 image orbits | atom-boundary H4 image orbits | visible H4-incident atoms | H4-invisible atoms |
|---|---:|---:|---:|---:|---:|
| `F4[u]/(u^2)` | `1569` | `7` | `2` | `72` | `1497` |
| `F2[u]/(u^5)` | `19140` | `43` | `21` | `5424` | `13716` |
| `F8[u]/(u^2)` | `158081` | `30` | `3` | `784` | `157297` |
| `F16` field control | `225` | `0` | `0` | `0` | `225` |
| `F2[u]/(u^4)` wild control | `1540` | `17` | `7` | `368` | `1172` |

Family-level pattern:

- `F4[u]/(u^2)`: only `TTWW` atom-boundary atoms are H4-incident
  (`72/72`); `TTTT` and `WWWW` remain invisible to this channel.
- `F8[u]/(u^2)`: only `1122` atom-boundary atoms are H4-incident
  (`784/784`); `1111` and `2222` remain invisible.
- `F2[u]/(u^5)`: mixed adjacent-depth families `2233`, `2244`, `2255`,
  `3344`, `3355`, and `4455` are H4-incident; pure-depth families `2222`,
  `3333`, `4444`, and `5555` remain invisible.
- `F2[u]/(u^4)`: mixed adjacent-depth families `2233`, `2244`, and `3344`
  are H4-incident; pure-depth families `2222`, `3333`, and `4444` remain
  invisible.
- `F16`: the mixed-conductor \(K^{CH}\) channel is empty, so all field-control
  atoms remain H4-invisible under this tested channel.

## H4-Invisible Contraction Shadow

The fourth classifier layer takes the H4-invisible atom-boundary mass and
contracts both sides to H3.  First it contracts the exact input-side H4 image
of the \(K^{CH}\) Fisher shadow to a generated H3 support shadow.  Then it
asks whether an H4-invisible atom-boundary cell has at least one H4-to-H3
pair contraction landing in that generated H3 shadow.

This is a weaker support projection than H4 incidence.  It is useful for
separating "invisible at H4 but visible after contraction" from "still
invisible to the tested contraction channel"; it is not filtered closure and
not an `Ext_CH` detector claim for \(K^{CH}\).

| row | raw atoms | H4-visible atoms | H4-invisible atoms | H3-contraction visible from H4-invisible | remaining invisible |
|---|---:|---:|---:|---:|---:|
| `F4[u]/(u^2)` | `1569` | `72` | `1497` | `1470` | `27` |
| `F2[u]/(u^5)` | `19140` | `5424` | `13716` | `13618` | `98` |
| `F8[u]/(u^2)` | `158081` | `784` | `157297` | `157178` | `119` |
| `F16` field control | `225` | `0` | `225` | `0` | `225` |
| `F2[u]/(u^4)` wild control | `1540` | `368` | `1172` | `1138` | `34` |

For `F8[u]/(u^2)`, the H4-level atom map saw only the `1122` mixed family.
After H4-to-H3 contraction, `42/49` of the `1111` atoms and `157136/157248`
of the `2222` atoms become incident to the generated H3 shadow.  The exact
remaining invisible residue is `119` atoms.

## Immediate Handoff

For FC1, the natural macrovariable census should include conductor packet
sizes, carry path distributions, normalizer pair orbits, H3/H4 family orbits,
visible Fisher-shadow support, and atom-boundary H4 incidence mass.  Rows with
the same support residual can still have different filtered carry mass, orbit
structure, visible/invisible atom-boundary splits, and H3 contraction-shadow
residues.

For FC3, the information-investment functional should charge full filtered
residual separately from support-visible residual and separately again from
the atom-boundary H4-visible component.  Projection kernels mark carry mass
invisible to a chosen cost channel unless the model pays for a richer
\(K^{CH}\), higher-arity Fisher-jet, contraction-shadow, or coefficient-shadow
observable.

Next exact task: refine the remaining contraction-invisible residue by signed
coefficient shadows or higher arity channels beyond the tested input-side H4
and H4-to-H3 images, while preserving the full/support/Fisher-shadow
distinctions.
