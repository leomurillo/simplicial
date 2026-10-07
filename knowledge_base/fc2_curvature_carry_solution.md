# FC2 Solution: Filtered Curvature-Carry Duality

Created: 2026-05-14

This note records the theorem-facing resolution of FC2 for the first mixed
local row:

```text
R = F_4[u]/(u^2)
```

The key correction is that the cohomology object is **not** the signed boundary
on closed nontrivial hyper-adjacency cells.  That boundary is the right
support selector for Fisher jets, but it fails \(d^2=0\) over \(\mathbb Z\) on
closed nontrivial cells.  The cohomology object is instead the filtered
quotient-character adjacency extension class.

## Theorem

**FC2-A. Filtered curvature-carry duality for \(F_4[u]/(u^2)\).**  Let
\(\mathcal A_R\) be the local quotient-character adjacency algebra with its
tame/wild conductor filtration, and let

```text
s : gr A_R -> A_R
```

be the normalized quotient-shift section used by the local adjacency
constructor.  The carry

```text
kappa(x,y) = s(x)s(y) - s(xy)
```

is a Hayes-equivariant filtered 2-cocycle.  Its cohomology class is nonzero
under full-block section changes.  Under the Fisher-jet functor, the same
class has two visible shadows:

1. the cubic metric shadow \(K^{CH}\), through the antisymmetric commutator
   part of the mixed \(srt^2\) Fisher coefficient;
2. the arity-4 curvature shadow, through the input-side Fisher-jet lift of the
   \(592\) commutator orbits onto exactly the seven mixed TTWW/TWWW
   hyper-adjacency orbits.

Thus the binary \(\operatorname{Ext}_{CH}\) carry and the arity-4
Amari-Chentsov curvature support are not separate coincidences.  They are two
functorial images of the same filtered extension class.

## Proof Skeleton

1. **Cocycle.**  Associativity of multiplication in \(\mathcal A_R\) gives
   the usual section-extension identity
   \(\delta\kappa=0\).  Replacing the section \(s\) by \(s+\phi\) changes
   \(\kappa\) by the finite coboundary \(\delta\phi\), so the class
   \([\kappa]\) is section invariant.
2. **Nontriviality.**  The exact finite reducer finds \(1569\) raw carry atoms
   on \(369\) carry pairs, reduced by the Hayes normalizer to \(71\) atom
   orbits and \(20\) pair orbits.  In the full-block section-change model,
   \(\dim C^1=3204\), \(\dim C^2=76320\), \(\operatorname{rank}B^2=3204\),
   and the residual support is still \(1569\).  Hence the carry is not a
   coboundary.
3. **Cubic shadow.**  The Fisher-jet functor sends the filtered product
   defect to the mixed \(srt^2\) coefficient.  Its antisymmetric commutator
   support is the \(592\)-orbit curvature-carry row isolated in Paper 11
   Section 9.1.
4. **Arity-4 shadow.**  The input-side lift sends each arity-2 commutator
   orbit to exactly one arity-4 orbit.  It hits all \(7/7\) mixed TTWW/TWWW
   orbits and \(0/11\) pure TTTT/WWWW orbits in the \(3165\)-cell,
   \(18\)-orbit arity-4 atlas.
5. **Wrong complex excluded.**  The signed all-pair boundary on closed
   nontrivial hypercells fails \(d^2=0\) over \(\mathbb Z\).  A tiny witness
   on \((\mathbb Z/2)^2\) gives
   \(d_3d_4(1,2,1,2)=4(3,3)-2(2,2)+2(1,1)\).  Therefore the hypercell
   boundary is a support/jet shadow, not the cohomology source.

## Certificate

The reproducible certificate is:

- `empirical/fc2_curvature_carry_certificate.py`
- `empirical/reports/fc2_curvature_carry_certificate.md`
- `empirical/reports/fc2_curvature_carry_certificate.json`

The certificate reuses the existing exact reducers and records the three
decisive facts: nonzero binary filtered class, exact arity-4 mixed curvature
shadow, and failure of the naive hypercell complex.

## What Is Solved

FC2 is solved for the first mixed local row in the theorem-facing sense:

```text
Ext_CH filtered class -> K_CH cubic shadow -> arity-4 curvature support
```

The phrase "curvature-carry cohomology" should now mean this filtered
extension class plus its Fisher-jet images, not a standalone cohomology of
closed nontrivial hypercells.

## What Remains

1. Classify which deeper tame/wild rows have nonzero \([\kappa_R]\).
2. Compute Fisher-jet kernels and visible support quotients beyond arity 4.
3. Turn the Fisher-jet shadow map into a named functor in Paper 11.
4. Decide whether an augmented hypercell complex is still useful as a
   secondary object; it is no longer needed as the source of FC2.
5. Extract coefficient-level arity-4 curvature values into the same
   certificate format, beyond support.
