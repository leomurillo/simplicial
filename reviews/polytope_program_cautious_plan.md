# Cautious Polytope Program

**Purpose.**  Continue the spectral hull/factorization classification without
turning computational frontier data into premature structure theorems.  The
program should compare prime, prime-power, squarefree, and mixed-composite
families, while keeping the status of each claim visible: theorem, exact
enumeration, seeded computation, invariant probe, or conjectural pattern.

---

## 1. Classification Lanes

### A. Prime Lane

Status: theorem.

For odd prime \(p\), the full spectral compound is

$$
X_p^{\mathrm{spec}}=V_p\cup(-V_p),
$$

with antipodal-simplex hull, central cube-slice polar, coordinate stabilizer
\(S_p\), and full orthogonal stabilizer \(C_2\times S_p\).

Role in the program: baseline.  This is the one-block case where the
factorization language is already earned.

### B. Prime-Power Lane

Status: coordinate-stabilizer theorem; full face-lattice program remains open
beyond the computed small rows.

Odd prime powers exhibit p-adic congruence-tree wreath products.  Powers of
two exhibit a special top-layer fusion into four-point fibers.  These are
factorization-sensitive coordinate symmetries, not yet full spectral-hull
stabilizer classifications.

Test cases:

- \(N=8\): Qhull-seeded exact facet reconstruction; binary top-layer fusion.
- \(N=9\): Qhull-seeded exact facet reconstruction; odd p-adic tree.
- Higher targets: separate coordinate-pair stabilizers from full
  Gram/orthogonal stabilizers.

### C. Squarefree Product Lane

Status: partial theorem for two-prime CRT coordinate stabilizers; face-lattice
classification open.

Odd squarefree \(N=pq\) separates by CRT coordinates at the coordinate layer.
Even semiprimes \(N=2p\) are dominated by parity fibers and collapse to
\(S_p\wr S_2\).

Test cases:

- \(N=6,10\): even semiprime parity collapse.
- \(N=15\): odd CRT product \(S_3\times S_5\).
- Future: higher squarefree products with three or more factors.

### D. Mixed-Composite Lane

Status: exact coordinate-pair stabilizer tests for selected rows; full
face-lattice and full orthogonal stabilizer classification open.

This is the caution lane.  Mixed composites can be rigid, blown up, CRT-split,
or parity-dominated depending on how prime-power and squarefree layers fuse.

Current anchor cases:

- \(N=12\): divisor-lattice rigidity; coordinate stabilizer
  \(\operatorname{Aff}(\mathbb Z/12\mathbb Z)\).  The refined reading is
  \(\operatorname{Aff}(\mathbb Z/4)\times S_3\), with no extra freedom because
  \(S_3=\operatorname{Aff}(\mathbb Z/3)\).
- \(N=18\): three-fold blow-up of the divisor scheme on \(\mathbb Z/6\).
- \(N=20\): \(\operatorname{Aff}(\mathbb Z/4)\times S_5\) CRT-style product.
- \(N=24\): full nonzero gcd-distance pair-color scheme with an exact
  order-\(768\) coordinate stabilizer test; face-lattice work not yet done.

---

## 2. Frontier Rows

The polytope census now includes safe frontier rows for \(N=18,20,24\).  These
are not face-lattice claims.

| \(N\) | dim | conductor/cyclotomic blocks | simplices | vertices | coordinate evidence | spectral-affine orthogonal lower |
|---:|---:|---|---:|---:|---|---:|
| 18 | 17 | \(2,3,6,9,18\) | 16 | 288 | exact pair-color stabilizer \(559872\) | 1728 |
| 20 | 19 | \(2,4,5,10,20\) | 16 | 320 | exact pair-color stabilizer \(960\) | 2560 |
| 24 | 23 | \(2,3,4,6,8,12,24\) | 64 | 1536 | exact pair-color stabilizer \(768\) | 12288 |

Interpretation:

1. \(N=18\), \(N=20\), and \(N=24\) are already useful stabilizer probes
   because their coordinate-pair invariants are exact in the mixed-composite
   verifier.
2. \(N=24\) is the first serious face-lattice stress test in this trio: many
   blocks, dimension \(23\), and \(1536\) vertices.  Treat it as a staged
   problem, not a one-shot facet enumeration.
3. The polar-intersection formula remains the safe convex-hull handle for all
   three rows.

---

## 3. Rigidity Frontier

The first proposed generalization of the \(N=12\) row was:

> Are higher \(4p\) or \(4pq\) rows affine-rigid for the same reason as
> \(N=12\)?

The coordinate-layer answer is no.  The frontier verifier
`empirical/verify_mixed_rigidity_frontier.py` gives:

| \(N\) | factor form | coordinate stabilizer | affine order | affine-rigid? |
|---:|---|---|---:|---|
| 12 | \(4\cdot3\) | \(\operatorname{Aff}(\mathbb Z/4)\times S_3\) | 48 | yes |
| 20 | \(4\cdot5\) | \(\operatorname{Aff}(\mathbb Z/4)\times S_5\) | 160 | no |
| 28 | \(4\cdot7\) | \(\operatorname{Aff}(\mathbb Z/4)\times S_7\) | 336 | no |
| 60 | \(4\cdot3\cdot5\) | \(\operatorname{Aff}(\mathbb Z/4)\times S_3\times S_5\) | 960 | no |

Thus \(N=12\) is special partly because \(3\) is the only odd prime for which
the full symmetric group on that CRT side is already affine.  The refined
question is not whether \(4p\) or \(4pq\) are rigid.  They are not, once an
odd prime \(p>3\) contributes a full \(S_p\) factor.  The better question is:

> Which conductor/CRT factors contribute only their affine subgroup, and which
> enlarge to full symmetric or wreath-product factors?

That formulation matches the evidence from \(N=15,18,20,24,28,60\) without
turning the \(N=12\) accident into a false family law.

---

## 4. Testing Ladder

Use this order for each new \(N\):

1. **Vertex/block census.**  Record blocks, distinct simplex images, vertices,
   antipodal pairs, dimension, and the spectral-affine lower subgroup.
2. **Coordinate-pair colors.**  Compute exact pair-color classes and compare
   with expected divisor/conductor schemes.
3. **Generator lower bounds.**  Verify explicit affine, CRT, wreath, or
   blow-up generators preserve the vertex set.
4. **Pair-color upper bounds.**  When feasible, prove the coordinate
   stabilizer by matching the generator lower bound to the exact pair-color
   automorphism count.
5. **Facet probes.**  Use Qhull only as a seed source, then reconstruct
   exposed faces exactly over rationals.
6. **Structural theorem.**  Promote only after a proof explains the observed
   product, free-sum, prism, CRT, p-adic, or rigidity pattern.

No row should jump from step 1 or 2 directly to a face-lattice theorem.

---

## 5. Next Actions

1. Isolate a compact structural description of the order-\(768\) coordinate
   stabilizer for \(N=24\), beyond exhaustive pair-color witnesses.
2. Determine whether \(N=24\)'s exact gcd-distance scheme predicts a product,
   prism, free-sum, or rigidity pattern at the face-lattice level.
3. Add a separate frontier report for \(N=18,20,24\) if the main census report
   becomes too slow.
4. Compare \(N=18,20,24\) tensor-support predictions from Problem 10.1 against
   their coordinate-pair color schemes.
5. Keep the Paper 8 wording conservative: \(N=18,20,24\) are higher
   mixed-composite tests, not solved hull families.
6. Use `empirical/reports/mixed_rigidity_frontier.md` as the reference for
   the failed \(4p\)/\(4pq\) affine-rigidity generalization.

---

## 6. Explorer Call

The polytope program should now move like a cautious climber: one exact
foothold at a time.  Prime and prime-power cases give reference terrain;
squarefree products test CRT separation; mixed composites test whether the
divisor lattice fuses, blows up, or rigidifies.  For \(N=18,20,24\), the first
victory is not a full face lattice.  The first victory is an exact invariant
profile that tells us which theorem is worth trying to prove.
