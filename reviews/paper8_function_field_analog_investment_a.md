# Paper 8 Function-Field Analog: Investment A

## Strategic Recommendation

State the abstract finite Dedekind-quotient theorem in this paper.  Do not
leave it as a closing remark.

That choice makes the paper itself the structural unifier, provided the theorem
is stated with narrow hypotheses and the later stabilizer/polytope claims are
kept separate from the formal transfer:

\[
\mathbb Z/N\mathbb Z
\qquad\text{and}\qquad
\mathbb F_q[t]/(f)
\]

become two specializations of one theorem about conductor-block decompositions
of finite quotient rings.  Deferring the abstract theorem would keep the
function-field paper cleaner, but it would postpone the main punchline.  The
load-bearing investment is the punchline placement: this paper should say the
general theorem first, then let Paper 8 and the function-field theory appear
as corollaries.

The cost is that the paper must commit to honest minimum hypotheses.  The
right level is:

- finite commutative quotient \(R=A/I\) of a Dedekind domain, or more generally
  a finite commutative Frobenius ring with a chosen generating additive
  character;
- a self-dual additive character pairing identifying \(R\) with \(\widehat R\);
- a conductor lattice identified with the divisor or ideal lattice below \(I\);
- a Mobius inversion formula on that lattice.

These hypotheses hold for \(\mathbb Z/N\mathbb Z\), for
\(\mathbb F_q[t]/(f)\), and for finite quotients of Dedekind domains by
nonzero ideals.  They are narrow enough to prove with confidence and broad
enough to justify a general conductor-block theorem without pretending that
the integer-specific orbit-size, half-turn, or polytope arguments transfer for
free.

## Abstract Theorem Spine

Let \(R=A/I\) be a finite Dedekind quotient equipped with a nondegenerate
additive character pairing

\[
\langle a,b\rangle_\psi=\psi(ab),
\qquad a,b\in R,
\]

so that \(b\in R\) indexes the additive character \(\chi_b(a)=\psi(ab)\).
Let

\[
H_R=\{x\in\mathbb C^R:\sum_{a\in R}x_a=0\},
\qquad
v_a=e_a-|R|^{-1}{\bf 1}.
\]

Characters have conductors in the divisor lattice of \(I\).  For each
nontrivial conductor \(\mathfrak d\mid I\), define

\[
H_R^{[\mathfrak d]}
=
\operatorname{span}\{\chi_b:\operatorname{cond}(\chi_b)=\mathfrak d\}.
\]

Then

\[
H_R
=
\bigoplus_{\substack{\mathfrak d\mid I\\\mathfrak d\ne 1}}
H_R^{[\mathfrak d]}.
\]

The orthogonal projector \(P_{\mathfrak d}\) has translation-invariant kernel

\[
(P_{\mathfrak d})_{a,c}
=
|R|^{-1}C_{\mathfrak d}(a-c),
\]

where \(C_{\mathfrak d}\) is the generalized Ramanujan/Hayes conductor sum

\[
C_{\mathfrak d}(h)
=
\sum_{\operatorname{cond}(\chi)=\mathfrak d}\chi(h).
\]

For a block-sign vector \(\epsilon=(\epsilon_{\mathfrak d})\), set

\[
T_\epsilon
=
\sum_{\mathfrak d\mid I,\ \mathfrak d\ne 1}
\epsilon_{\mathfrak d}P_{\mathfrak d}.
\]

The resulting block signs form an elementary abelian operator group \(B_R\)
on \(H_R\).

Then the spectral compound

\[
X_R^{\mathrm{spec}}
=
\{T_\epsilon v_a:\epsilon_{\mathfrak d}\in\{\pm1\},\ a\in R\}
\]

is a union of regular simplex frames.  Let

\[
K_R=\{T\in B_R:T(V_R)=V_R\}
\]

be the finite kernel of block signs that act as relabelings of the original
simplex \(V_R=\{v_a:a\in R\}\), and remove duplicate simplex images.  If
\(M_R=|B_R/K_R|\), then after vertex normalization the resulting compound is a
unit-norm tight frame in \(H_R\) with frame bound

\[
A_R=\frac{|R|M_R}{|R|-1}.
\]

The unnormalized centered cross-Gram blocks are

\[
\langle T_\epsilon v_a,T_\eta v_b\rangle
=
|R|^{-1}
\sum_{\mathfrak d\mid I,\ \mathfrak d\ne 1}
\epsilon_{\mathfrak d}\eta_{\mathfrak d}
C_{\mathfrak d}(a-b).
\]

For unit-normalized vertices, this becomes

\[
\frac{1}{|R|-1}
\sum_{\mathfrak d\mid I,\ \mathfrak d\ne 1}
\epsilon_{\mathfrak d}\eta_{\mathfrak d}
C_{\mathfrak d}(a-b).
\]

As in Paper 8, the all-block sign is \(-I_{H_R}\), so the ordinary coherence
of the full compound is \(1\).  The useful packing statistic is the
non-antipodal/projective angle set obtained after deleting absolute value
\(1\).

Finally, coordinate-pair colors are fusions of the ideal-divisor association
scheme whenever that scheme is taken to be the Schurian scheme of the affine
unit action: unit multiplication preserves every conductor sum, so the colors
are constant on unit orbits of differences.

This is the abstract theorem behind the special case
\(R=\mathbb Z/N\mathbb Z\) treated in Paper 8.

## Status Discipline

The function-field paper should keep four layers visibly separate.

1. **Formal transfer.**  Character orthogonality, conductor projectors,
   generalized Ramanujan sums, block-sign tightness, and the normalized
   cross-Gram formula should be stated as the main theorem.
2. **Kernel and orbit census.**  The integer formula
   \(2^{\tau(N)-1}\) or \(2^{\tau(N)-2}\) should not be copied.  The new task
   is to classify \(K_R\), i.e. which conductor block signs act as translations
   or other simplex relabelings.
3. **Stabilizers.**  Prime, prime-power, and CRT stabilizer families are
   plausible theorem targets, but each needs a proof in the additive group of
   \(A/(f)\); the cyclic-generator and half-turn shortcuts are unavailable.
4. **Polytopes and refined normalizers.**  Convex-hull product/free-sum
   descriptions and Hayes-character monomial normalizers should be presented
   as new problems until small cases and structural proofs catch up.

## Two Specializations

### Integer Specialization

For \(A=\mathbb Z\), \(I=(N)\), and \(R=\mathbb Z/N\mathbb Z\), the conductor
blocks are the \(\Phi_d\) cyclotomic blocks, indexed by \(d\mid N\), and

\[
C_d(h)=c_d(h)
\]

is the ordinary Ramanujan sum.  The abstract theorem recovers the block-sign
spectral compound theorem of Paper 8, including the tight frame statement,
the Ramanujan cross-Gram formula, and the divisor-scheme fusion theorem.

The extra integer-specific features are not part of the abstract theorem:
the additive group is cyclic, the cyclic shift \(C_N\) has a canonical
generator, and the unique nonconstant one-dimensional cyclotomic block is
\(\Phi_2\) when \(2\mid N\).

### Function-Field Specialization

Let \(A=\mathbb F_q[t]\), let \(f\in A\) be monic, and set \(R=A/(f)\).  Write

\[
Q_f=|R|=q^{\deg f}.
\]

Use a fixed nontrivial additive character
\(\psi_0:\mathbb F_q\to\mathbb C^\times\) and the usual trace/residue pairing
to identify \(R\) with its character group.  For \(b\in R\),

\[
\chi_b(a)
=
\psi_0(\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}
(\operatorname{res}_f(ab))).
\]

Then

\[
\operatorname{cond}(\chi_b)=f/\gcd(f,b).
\]

For each monic \(d\mid f\), the Carlitz-Hayes conductor block is

\[
H_f^{[d]}
=
\operatorname{span}\{\chi_b:\operatorname{cond}(\chi_b)=d\},
\qquad
\dim H_f^{[d]}=|(A/(d))^\times|.
\]

The projector kernel is

\[
(P_d)_{a,c}=Q_f^{-1}C_d(a-c),
\]

where

\[
C_d(h)
=
\sum_{u\in(A/(d))^\times}\chi_u(h)
=
\sum_{e\mid \gcd(d,h)} |e|\,\mu(d/e).
\]

This is the exact function-field replacement for the Ramanujan-sum kernel in
Paper 8.

## Replacement Dictionary

| Integer Paper 8 object | Function-field analog |
| --- | --- |
| \(\mathbb Z/N\mathbb Z\) | \(A/(f)\), \(A=\mathbb F_q[t]\), \(f\) monic |
| \(N\) | \(Q_f=q^{\deg f}\) |
| coordinate labels \(i\in\mathbb Z/N\mathbb Z\) | coordinate labels \(a\in A/(f)\) |
| simplex vertices \(v_i=e_i-N^{-1}{\bf 1}\) | \(v_a=e_a-Q_f^{-1}{\bf 1}\) |
| cyclic shift \(C_N\) | full translation action of \((A/(f),+)\) |
| unit relabelings \(i\mapsto ui\) | \(a\mapsto ua\), \(u\in(A/(f))^\times\) |
| \(\operatorname{Aff}(\mathbb Z/N\mathbb Z)\) | \(R\rtimes R^\times\) |
| divisors \(d\mid N\) | monic divisors \(d\mid f\) |
| conductor of additive character | \(d=f/\gcd(f,b)\) |
| \(\Phi_d\) block | Carlitz-Hayes conductor-\(d\) block |
| \(\varphi(d)\) | \(\Phi_A(d)=|(A/(d))^\times|\) |
| Ramanujan sum \(c_d(h)\) | Hayes/Ramanujan polynomial sum \(C_d(h)\) |
| \(\gcd(N,h)\)-divisor scheme | ideal-gcd scheme \(g=\gcd(f,h)\) |
| CRT of integer quotients | CRT of polynomial local factors |

The critical warning is that \((\mathbb Z/N\mathbb Z,+)\) is cyclic, while
\((\mathbb F_q[t]/(f),+)\) is an \(\mathbb F_q\)-vector space, hence an
elementary abelian \(p\)-group.  Paper 8 arguments involving a single cyclic
generator, the half-turn \(C_N^{N/2}\), or the statement "a block sign acts as
a cyclic shift" must be rewritten in terms of the full translation group.

## Carlitz-Drinfeld Framing

The function-field paper should say explicitly that
\(\mathbb F_q[t]/(f)\) is the \(f\)-torsion model for the Carlitz module in
the same way that \(\mathbb Z/N\mathbb Z\) is the \(N\)-torsion model for
\(\mathbb G_m\).  Hayes sums and Carlitz cyclotomic extensions are therefore
not decorative replacements for Ramanujan sums; they are the natural conductor
sums attached to the unit action on torsion.

This paragraph does not need to develop Drinfeld module theory in detail.  Its
job is to place the frame theorem at the right altitude: both specializations
are spectral compounds of units acting on torsion of a one-dimensional
commutative arithmetic object.

## Paper 8 Survival Ledger

| Paper 8 result | Function-field status |
| --- | --- |
| Theorem 3.1, parity-dual simplex | Survives only after replacing "parity line" by a one-dimensional conductor block.  In \(A=\mathbb F_q[t]\), a linear conductor has dimension \(q-1\), so it is a Householder line only when \(q=2\). |
| Theorem 4.1, \(N=4\) stella-octangula | Mostly small-dimensional and \(\mathbb Z\)-specific.  Function-field quotients with \(Q_f=4\) split into different geometries depending on factorization type: irreducible quadratic, split squarefree, or nonreduced prime power. |
| Theorem 6.1, parity-class stabilizer | Generalizes as a residue-class stabilizer for a degree-one conductor.  For a linear divisor \(\ell\mid f\), the coordinate classes are fibers of \(R\to A/(\ell)\).  The stabilizer becomes a wreath product on \(q\) equal fibers, reducing to the parity \(S_m\wr S_2\) only when \(q=2\). |
| Theorem 6.2, parity convex-hull decomposition | Needs adjustment.  The prism/free-sum proof is tied to a one-dimensional parity axis and two coordinate fibers.  Higher-dimensional linear-conductor blocks should produce related fiber decompositions, but not the same two-class prism theorem. |
| Proposition 8.1, block-sign orbit size | Survives with a kernel \(K_R\), but the integer proof must be replaced.  Paper 8 uses cyclic shifts and the half-turn kernel; the function-field proof must classify which block signs act as translations of the additive group \(R\). |
| Theorem 8.2, Ramanujan few-angle tight frame | Survives after replacing \(c_d\) by \(C_d\) and keeping the normalization explicit: unnormalized cross-Grams carry \(|R|^{-1}\), while unit-vector angle sets carry \((|R|-1)^{-1}\).  This is the first core theorem of the new paper. |
| Theorem 8.3, prime spectral hull | Survives cleanly.  If \(f\) is irreducible, there is one nonconstant block, so \(X_f^{\mathrm{spec}}=V_f\cup(-V_f)\), with coordinate stabilizer \(S_{Q_f}\) and full stabilizer \(C_2\times S_{Q_f}\). |
| Theorem 8.4, \(N=6\) composite hull | Does not transfer verbatim.  It becomes a table of smallest composite function-field examples indexed by \((q,\) factorization type of \(f)\), not by \(Q_f\) alone. |
| Theorem 8.5, prime-power stabilizers | Expected to generalize strongly, but it needs a new proof.  For \(f=\pi^r\), the candidate stabilizer is governed by the \(\pi\)-adic congruence tree with branching \(|A/(\pi)|\).  The special top-layer fusion should be tested first in the binary residue case \(|A/(\pi)|=2\). |
| Theorem 8.6, divisor-scheme fusion | Survives in ideal language once the relevant ideal-gcd relations are formulated as the affine unit-action scheme.  This is the second core theorem. |
| Theorem 8.7, even semiprime parity collapse | Becomes a norm-two linear-factor theorem.  The integer statement uses the unique \(\Phi_2\) line; the function-field analog should assume a linear factor over \(\mathbb F_2\). |
| Theorem 8.8, odd squarefree two-prime CRT stabilizers | Generalizes with care.  For \(f=\pi\sigma\), CRT gives two residue-field factors.  If their norms differ, expect \(S_{|\pi|}\times S_{|\sigma|}\); if the norms coincide, a factor-swap symmetry may appear. |
| Theorems 8.9-8.11, Fourier-plane reflection obstructions | Need serious restatement.  The integer proofs use cyclic additive spectra and eigenvalues of order \(d\).  Over \(\mathbb F_q[t]\), translation eigenvalues have residue characteristic \(p\), while conductor structure is carried by Hayes characters.  The replacement object is the monomial normalizer of the Hayes character system. |
| Observation 8.12, layer separation | Survives conceptually but becomes richer.  The special meeting point is a one-dimensional nonconstant conductor block.  Linear factors over \(\mathbb F_2\) give \(\Phi_2\)-style meeting points, and split binary quotients can have several such points. |

## Small-Case Indexing

Function-field small cases must be indexed by

\[
(q,\text{factorization type of }f),
\]

not by \(Q_f\) alone.  The first warning is \(Q_f=4\) over \(\mathbb F_2\):

| \(f\) over \(\mathbb F_2\) | quotient type | expected role |
| --- | --- | --- |
| irreducible quadratic | field \(\mathbb F_4\) | prime/irreducible case, \(V\cup(-V)\) |
| \(t^2\) | nonreduced local ring | prime-power congruence-tree case |
| \(t(t+1)\) | split product \(\mathbb F_2\times\mathbb F_2\) | binary squarefree CRT case with several one-dimensional blocks |

The split case is the first place where the function-field theory is richer
than its integer parent.  There are two linear-conductor Householder lines,
one for each projection to \(\mathbb F_2\).  There is also a product-conductor
line, since \(\Phi_A(t(t+1))=1\).  Thus the paper should distinguish:

- the rank-two linear-factor skeleton, generated by the two coordinate
  projection characters;
- the full rank-three one-dimensional block-sign system on \(H_R\).

For a squarefree product of \(r\) distinct linear factors over \(\mathbb F_2\),
every nontrivial squarefree conductor has \(\Phi_A(d)=1\).  The linear factors
give \(r\) primitive coordinate-layer meeting points, while the full
one-dimensional block-sign group has rank \(2^r-1\).  This is not a defect of
the analogy; it is new structure exposed by the function-field side.

## Binary Meeting-Point Observation

The function-field analog of Paper 8's Observation 8.12 should be stated as a
labeled observation:

> Inside \(H_{A/(f)}\), one-dimensional nonconstant conductor blocks occur
> exactly for squarefree products of distinct linear factors over
> \(\mathbb F_2\).  The primitive coordinate/reflection meeting points are the
> individual linear factors.  Hence the integer \(\Phi_2\) uniqueness theorem
> is the special case where the divisor lattice contains only one norm-two
> residue-field direction.

If the paper wants the closest analog of "the \(\Phi_2\) line," it should focus
on individual linear factors over \(\mathbb F_2\).  If it wants the full
function-field enhancement, it should also record the additional product
conductor lines in split binary squarefree quotients.

## Refined Normalizers

The reflection-refinement theorems in Paper 8 do not formally transfer.
Theorems 8.9-8.11 rely on cyclic translation eigenvalues of order \(d\) and
on conjugate Fourier planes inside \(\Phi_d\)-blocks.  In the function-field
case, translation characters take values in \(p\)-th roots after choosing the
base additive character, while the conductor organization is Hayes/Carlitz
rather than cyclic-root-of-unity order.

The right replacement object is:

\[
\text{the monomial normalizer of the Hayes character system.}
\]

Even if the function-field paper does not classify this normalizer, naming it
is a structural contribution.  It cleanly marks the place where the analogy
stops being formal and new arithmetic geometry begins.

## Proposed Paper Structure

1. **Abstract finite Dedekind-quotient theorem.**  State the self-dual
   quotient-ring setup, conductor blocks, generalized Ramanujan sums,
   projector kernels, block-sign tightness, cross-Gram formula, and
   divisor-scheme fusion.

2. **Integer specialization.**  Explain that Paper 8 is the
   \(R=\mathbb Z/N\mathbb Z\) specialization, with ordinary Ramanujan sums and
   \(\Phi_d\)-blocks.

3. **Function-field specialization.**  Develop \(A=\mathbb F_q[t]\),
   \(R=A/(f)\), Carlitz-Hayes sums, conductor formula
   \(d=f/\gcd(f,b)\), and the explicit Mobius formula.

4. **Prime and prime-power quotients.**  Prove the irreducible case and the
   \(\pi\)-adic congruence-tree stabilizer theorem.

5. **Divisor schemes and CRT families.**  Prove the ideal-divisor fusion
   theorem, the squarefree two-prime CRT theorem, and the norm-two
   linear-factor parity-collapse analog.

6. **Small binary examples.**  Work out \(Q_f=4\), especially
   \(f=t(t+1)\), to show how multiple binary meeting points enrich the
   integer \(\Phi_2\) story.

7. **What changes from \(\mathbb Z\).**  Isolate the failed verbatim transfers:
   the cyclic generator, the half-turn kernel, the \(N=4\) stella boundary,
   the \(N=6\) hull, and the \(G(d,d,2)\) Fourier-plane normalizer story.

8. **Normalizers and next problems.**  State the monomial Hayes-normalizer
   problem as the function-field replacement for Paper 8's Fourier-plane
   reflection refinements.

## First Proof Targets

The proof route should be:

1. Prove the abstract projector kernel formula from conductor-character
   orthogonality.

2. Specialize it to
   \[
   (P_d)_{a,c}=Q_f^{-1}C_d(a-c)
   \]
   for \(A=\mathbb F_q[t]\).

3. Prove the Hayes Mobius identity
   \[
   C_d(h)=\sum_{e\mid \gcd(d,h)} |e|\,\mu(d/e).
   \]

4. Prove the block-sign cross-Gram formula
   \[
   \langle T_\epsilon v_a,T_\eta v_b\rangle
   =
   Q_f^{-1}\sum_{d\mid f,\ d>1}\epsilon_d\eta_d C_d(a-b).
   \]

5. Prove tightness of the duplicate-quotiented \(X_f^{\mathrm{spec}}\), with
   frame bound \(Q_fM_f/(Q_f-1)\), and record the projective angle set after
   removing antipodal pairs.

6. Prove divisor-scheme fusion from \(C_d(uh)=C_d(h)\).

7. Prove the irreducible, prime-power, and squarefree CRT stabilizer families.

Once these are done, the paper has already delivered the structural theorem.
The polytope and refined-normalizer sections can then be honestly labeled as
the places where the function-field analog stops being a formal transfer and
starts generating new problems.

## Publication Shape

This is a one-paper investment if the abstract theorem is the spine.  A
realistic length is about 30 pages:

- abstract theorem and two specializations;
- function-field proofs of the core projector, tight-frame, and divisor-fusion
  results;
- prime, prime-power, CRT, and binary small-case families;
- a final section marking the non-formal normalizer and polytope problems.

The natural specialty target is *Finite Fields and Their Applications*.
*Journal of Number Theory* becomes plausible if the abstract theorem is
foregrounded.  A higher target would require leaning harder into the
Carlitz/Drinfeld framing and proving a clean binary multi-meeting-point
theorem.
