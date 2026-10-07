# Problem 10.1 Flagship Brief

**Purpose.**  Make the Fisher-Conductor Coupling Tensor the central research
object connecting Papers 8, 9, and 10.  The centroid theorem gives the exact
arithmetic spectral resolution of the categorical Fisher tangent geometry.
Problem 10.1 asks for the arithmetic calculus of how that resolution breaks
away from the centroid.

This is the right flagship because it is narrow enough to compute, broad
enough to organize the program, and honest about the current mathematics:
Papers 8 and 9 prove the conductor decomposition at maximum entropy; Paper 10
identifies the off-centroid tensor whose Taylor coefficients should carry the
next arithmetic structure.

---

## 1. Flagship Statement

Let \(R=A/I\) be a finite quotient ring, let \(p\in\Delta_R^\circ\), and let

$$
g^F_p(u,w)=\sum_{a\in R}\frac{u_aw_a}{p_a}
$$

be the categorical Fisher metric.  Express \(g^F_p\) in the additive-character
basis of \(H_R\), grouped by primitive conductor blocks
\(H_R^{[\mathfrak d]}\).  Determine the selection rules, coefficient formulas,
normalizers, and geometric consequences of the block couplings

$$
g^F_p\left(H_R^{[\mathfrak d]},H_R^{[\mathfrak e]}\right).
$$

The centroid \(p_*\) is the zeroth-order theorem: the conductor blocks are
Fisher-orthogonal.  The flagship problem is the full arithmetic Taylor
expansion of the Fisher metric around \(p_*\).

---

## 2. Terminology Discipline

The theorem-level object is a character line, a primitive conductor block, or
a conductor-indexed coupling between such blocks.  Use "prime" only when the
statement has passed through a factorization theorem that identifies how
prime powers, CRT factors, norm-two factors, or mixed-composite conductor data
produce the observed geometry.

Recommended language:

1. Say **primitive conductor block** in statements of decomposition,
   orthogonality, coupling, and tensor formulas.
2. Say **quotient-conductor relation** for first-order couplings
   \(\psi\chi^{-1}\), not "prime interaction."
3. Say **conductor-depth filtration** or **product support in the dual
   character group** for all-order expansions, not "prime cascade."
4. Say **factorization-sensitive geometry** when interpreting polyhedral
   behavior before a full classification is proved.
5. Reserve **prime geometry** for proved specializations: prime \(N\),
   prime-power congruence trees, CRT products of distinct primes, and
   norm-two one-dimensional conductor blocks.

The slogan is: conductors are the rigorous coordinates; primes are the earned
interpretation.  The flagship should first prove the conductor calculus, then
translate it into prime-factorization language case by case.

---

## 3. What We Already Own

1. **Centroid resolution.**  At \(p_*\), the centered simplex score frame is
   the Fisher score frame, and the additive-character conductor decomposition
   diagonalizes the tangent Fisher geometry.

2. **First-order selection rule.**  If \(p=p_*+h\), the first-order coupling
   between character lines \(\chi\) and \(\psi\) is governed by
   \(\widehat h(\psi\chi^{-1})\).  Thus conductor support of \(h\) controls
   which block couplings can appear.

3. **All-order support filtration.**  Along conductor-flat \(m\)- and
   \(e\)-rays, the \(n\)-th Taylor coefficient is controlled by product
   support in the dual character group.  Support is not the final formula, but
   it is the skeleton.

4. **Second-order target.**  The \(n=2\) coefficient is the first genuinely
   nonlinear arithmetic object: a bilinear Hayes-Mobius convolution tensor
   coming from \(\widehat{h^2}=\widehat h*\widehat h\).

5. **Binary atlas.**  The split \(Q_f=4\) case already gives a fully visible
   first model where off-centroid Fisher coupling appears in a small
   Dedekind/function-field quotient.

---

## 4. Workstreams

### A. Coefficient Formulas

Deliver the explicit first- and second-order tensor formulas in conductor
coordinates.

Immediate tasks:

1. Fix Fourier normalization conventions once, and use them across Papers 9
   and 10.
2. Write the first-order coefficient as a block matrix indexed by conductor
   pairs.
3. Compute the second-order Hayes-Mobius tensor for integer \(N\), then for
   Dedekind quotients.
4. Identify cancellations: support rules say where coefficients may live, but
   the flagship needs to know when they vanish.

First cases:

- \(N=4,6,8,9,12\)
- \(R=\mathbb F_2[t]/(t(t+1))\)
- \(R=\mathbb F_2[t]/(t^2)\)
- \(R=\mathbb F_4\)

Sequencing rule:

1. Close the \(N=4\) scout first: compute the second-order coefficients for
   \(\mathbb F_2[t]/(t^2)\), transfer them to \(\mathbb Z/4\mathbb Z\), and
   verify the transfer mechanism.
2. Only after that unit test should the prime-power scouts \(N=8\) via
   \(\mathbb F_2[t]/(t^3)\) and \(N=9\) via
   \(\mathbb F_3[t]/(t^2)\) be treated as family evidence.
3. Run the integer mixed-composite tracks in parallel when bandwidth permits:
   the full \(\mathbb Z/6\mathbb Z\) tensor and restricted subtensors inside
   \(\mathbb Z/12\mathbb Z\) are independent of the prime-power scout.

Do not substitute \(\mathbb Z/6\mathbb Z\) for a restricted
\(\mathbb Z/12\mathbb Z\) computation.  The former has conductor blocks
\(\{2,3,6\}\) and dimension \(5\).  The latter lives inside the divisor
lattice of \(12\); restricting to selected \(\varphi(d)=2\) blocks such as
\(H^{[3]},H^{[4]},H^{[6]}\) is a range restriction on the off-centroid tensor,
not a change of ambient ring.

### B. Orthogonality Locus

Classify nonuniform \(p\) for which conductor blocks remain mutually
Fisher-orthogonal.

This is the cleanest way to test how special the centroid really is.  The
expected answer is that exact block orthogonality is rare, but the exceptions
may reveal arithmetic submanifolds: binary lines, CRT fibers, or distributions
constant on conductor-visible partitions.

### C. Conductor-Flat Geodesics

Compare \(m\)-flat and \(e\)-flat rays initialized in a single conductor block.

Questions:

1. When does the support filtration close after one or two steps?
2. When do higher product sets force new conductor couplings?
3. Which cases admit closed Ramanujan/Hayes coefficient formulas rather than
   only support descriptions?

### D. Carlitz-Hayes Equivariance

Make Problem 9.6 operational by asking how the Carlitz-Hayes normalizer acts
on the off-centroid coupling tensor.

This turns the function-field side from analogy into machinery.  The target is
not merely a spectral compound at the centroid, but an equivariant calculus for
the Taylor coefficients away from the centroid.

### E. Polyhedral Consequences

Feed the tensor data back into the spectral-compound program.

The tensor should explain which divisor/conductor interactions appear as
polyhedral shattering: p-adic congruence trees, CRT products, binary parity
fibers, and mixed-composite rigidity.  This workstream should stay
conjecture-aware: use the tensor to generate structural predictions, then test
them by exact enumeration.

Polytope tests should follow the cautious ladder in
`reviews/polytope_program_cautious_plan.md`: vertex/block census, pair-color
schemes, generator lower bounds, pair-color upper bounds, exact facet
reconstruction, and only then structural theorems.  The immediate frontier
rows are \(N=18,20,24\).  Their role is to probe mixed-composite behavior, not
to claim a solved face-lattice classification.

---

## 5. Explorer Assignments

**Explorer 1: Formula Keeper.**  Own the normalization, first-order block
formula, and second-order tensor statement.  Output should be theorem-ready
lemmas with hypotheses and proof sketches.

**Explorer 2: Atlas Builder.**  Compute exact small examples.  Start with
\(Q_f=4\), then integer \(N=6,8,9,12\).  Output should be tables of conductor
supports, nonzero block couplings, and cancellation patterns.

**Explorer 3: Orthogonality Cartographer.**  Search for nonuniform
orthogonality loci.  Distinguish genuine conductor-orthogonal families from
coordinate artifacts.

**Explorer 4: Carlitz-Hayes Scout.**  Translate the first two tensor levels
into function-field language and identify candidate normalizer actions.

**Explorer 5: Polytope Liaison.**  Compare tensor predictions to spectral hull
data from Paper 8.  The goal is a dictionary from coupling patterns to
polyhedral decomposition patterns.  Own the \(N=18,20,24\) frontier ladder:
keep vertex/block data, coordinate-pair colors, and stabilizer evidence
separate from full face-lattice claims.

---

## 6. Success Criteria

The flagship is working if, after one exploration cycle, we have:

1. A theorem-ready first-order coupling formula.
2. A second-order Hayes-Mobius formula in at least the integer cyclic case.
3. Exact \(Q_f=4\) atlases for split, nilpotent, and irreducible quotients.
4. A short list of candidate nonuniform orthogonality loci.
5. A revised Problem 9.6 that explicitly acts on the coupling tensor.
6. A table linking small \(N\) tensor supports to known Paper 8 polyhedral
   behavior.
7. Frontier polytope rows for \(N=18,20,24\), explicitly labeled by evidence
   level: safe census, exact stabilizer test, seeded facet computation, or
   theorem.

---

## 7. Presentation Line

The centroid is the crystal: conductor blocks are perfectly orthogonal there.
Off the centroid, the crystal does not vanish; it diffracts.  Problem 10.1 is
the diffraction calculus.  First support, then coefficients, then symmetry,
then geometry.

That is the call to action: do not ask whether the centroid theorem survives
unchanged.  It does not.  Ask how it fails, and compute the arithmetic of that
failure.
