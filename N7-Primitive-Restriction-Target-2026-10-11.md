# Primitive restriction: a sufficient arithmetic growth mechanism

11 October 2026. Companion to `N7-Arithmetic-Hodge-Index-Attempt-2026-10-11.md`. Source manuscripts are unchanged.

**Status.** This note proves a classical restriction estimate, an elementary lattice-counting estimate, and conditional implications specifying how they would apply to the packet pairing. It also proves an obstruction to realizing all packet intersections on one ordinary smooth projective surface. It does not construct the necessary arithmetic section theory or prove RH.

## 1. Only the packet-difference rays are needed

Keep the fixed packet and kernel from the two-clock note:

\[
a=\log2,\qquad G(z)=\frac{5-4\cosh(az)}{1-z^2},\qquad
K(t)=\sum_\rho G(\rho-\tfrac12)e^{(\rho-1/2)t},\qquad q=K(0)>0.
\]

The removable values of G are understood. The zero sum, with multiplicities, converges absolutely and locally uniformly. G has no zeros on the critical strip translated by -1/2. Let \(\mathcal T=\mathbb Z\log2+\mathbb Z\log3\).

The pole-plane construction supplies formal primitive packet classes P_t with

\[
P_s\cdot P_t=-K(s-t).
\]

For \(D_t=P_t-P_0\), bilinearity gives the exact identity

\[
\boxed{D_t^2=2(K(t)-q).}                                      \tag{1}
\]

Consequently it suffices to construct section sizes, independently of the desired sign, satisfying for each fixed \(t\in\mathcal T\)

\[
h(nD_t)+h(\kappa-nD_t)
\ge n^2(K(t)-q)-O_t(n),                                      \tag{2}
\]
\[
h(nD_t)+h(\kappa-nD_t)=o_t(n^2).                              \tag{3}
\]

Here κ denotes the proposed canonical class, avoiding confusion with the kernel K. Dividing by n² yields K(t)≤q. Density and continuity extend this to all real t. The earlier one-sided Laplace argument then gives RH. Neither constants uniform in t nor estimates for all finite packet combinations are required for this particular reduction.

For completeness, that last implication is specific to the zeta kernel. If K≤q, the function q−K is nonnegative on [0,∞), with a Laplace transform initially defined for Re s>1/2:

\[
L(s)=\frac q s-\sum_\rho\frac{G(\rho-1/2)}{s-(\rho-1/2)}.
\]

The sum continues meromorphically, with a nonzero residue at every shifted zero and no singularity at any positive real s. An off-line zero in Re s>0 would force the abscissa of convergence of the nonnegative Laplace integral to be positive: otherwise the integral would be holomorphic at that pole. Landau's theorem forces a singularity at this positive real abscissa, a contradiction. Functional-equation symmetry excludes the other half. This is the same nonnegative-transform mechanism used in [Suzuki's screw-function work, §7.2](https://arxiv.org/html/2206.03682); the displayed transform here is for our packet.

Thus (2)–(3) on the single family D_t suffice. This is a reduction of the required input, not a proof of either arithmetic hypothesis.

## 2. The classical restriction calculation gives O(1)

Let S be a smooth projective integral surface over an algebraically closed field. Choose a smooth integral very ample curve H and set r=H²>0. For an integral divisor E write d=E·H.

If d<0 then h⁰(S,O(E))=0: a nonzero section would give an effective divisor, whose intersection with H is nonnegative.

On the smooth projective curve H, a line bundle of degree d has at most max(0,d+1) independent sections. For d≥0, successively subtracting d+1 points proves this using the one-dimensional evaluation quotient and the vanishing at negative degree.

The restriction sequence

\[
0\longrightarrow O_S(E-H)\longrightarrow O_S(E)
\longrightarrow O_H(E)\longrightarrow0
\]

therefore gives

\[
h^0(E)\le h^0(E-H)+\max(0,d+1).
\]

Iterate until the degree is negative. With J=⌊d/r⌋ for d≥0,

\[
h^0(E)\le C_r(d):=
\begin{cases}
0,&d<0,\\
(J+1)(d+1)-\dfrac{rJ(J+1)}2,&d\ge0.
\end{cases}                                                   \tag{4}
\]

If D·H=0, this gives

\[
h^0(nD)\le1,\qquad h^0(\kappa-nD)\le C_r(\kappa\cdot H),       \tag{5}
\]

independently of n. Combining this with surface Riemann–Roch and Serre duality,

\[
h^0(nD)+h^0(\kappa-nD)
\ge\tfrac12n^2D^2-\tfrac12nD\cdot\kappa+\chi(O_S),
\]

proves D²≤0. This is the classical Hodge-index mechanism; the [surface notes, §6](https://people.math.harvard.edu/~landesman/assets/surfaces-notes.pdf) give the related Riemann–Roch argument. The explicit bound (4) is derived above to expose the needed restriction input.

The useful feature is that the number of restrictions is independent of n. Primitivity keeps the degree constant while n grows. A positive-square direction would demand quadratic sections through Riemann–Roch, while restriction allows only boundedly many.

## 3. Arithmetic restriction can be weaker and still suffice

Ordinary vector-space dimension is not automatically the right arithmetic section size. For small sections in normed lattices, one typically counts logarithmically, and changing metrics can change that count even when an underlying algebraic degree is fixed. Accordingly, transplanting the O(1) assertion in (5) is unnecessary.

Here is a sufficient abstract replacement. Suppose there is a degree functional d(E)=E·H with r=H²>0, and a nonnegative section size h. Fix D with d(D)=0. For each of the two families E_n=nD and E_n=κ−nD, require:

1. A fixed integer J, independent of n, such that d(E_n−JH)<0.
2. Restriction inequalities, for 0≤j<J,
   \[
   h(E_n-jH)\le h(E_n-(j+1)H)+b_j(n).
   \]
3. A terminal estimate h(E_n−JH)=o(n²), and b_j(n)=o(n²) for each of these finitely many j.

Telescoping proves h(E_n)=o(n²). If the terminal term and every b_j are O_D(n+1), the result is O_D(n+1), which is already stronger than (3). Exact negative-degree vanishing is one possible terminal estimate, not a necessary axiom.

These are statements to establish for actual arithmetic objects. The inequalities are not consequences of writing a formal intersection matrix.

### A concrete source of O(n) restriction terms

Let Λ be a fixed lattice of rank r in a finite-dimensional real normed vector space. For a fixed norm ||·||₀, lattice discreteness and a fundamental-domain counting argument give

\[
\#\{v\in\Lambda:\|v\|_0\le R\}\le C_\Lambda(1+R)^r.
\]

Suppose the norms used at stage n satisfy

\[
\|v\|_n\ge e^{-cn-c_0}\|v\|_0.
\]

Then

\[
\log\#\{v\in\Lambda:\|v\|_n\le1\}
\le\log C_\Lambda+r\log(1+e^{cn+c_0})=O(n+1).                 \tag{6}
\]

The constants may depend on the fixed direction D and the restriction step. No zero-location statement enters this counting proof.

Thus an arithmetic construction would discharge (3) if its finitely many restriction contributions were bounded by counts of the form (6), and its terminal contribution had the same bound. This requires fixed lattice ranks along n, controlled norm distortion, and justified restriction/counting inequalities. For logarithmic counts, ordinary exactness of vector spaces alone does not prove the required inequalities: bounds on fibers and norms must also be supplied.

**Concrete construction target:** restriction spaces of fixed rank along each D_t, norms varying at most exponentially in n, and a subquadratic terminal term, coupled to the quadratic lower estimate (2). The full section spaces need not have bounded rank, and no uniformity across t is demanded.

## 4. A fixed ordinary surface cannot carry every exact packet intersection

There is an unconditional constraint on what such a construction can be.

**Proposition.** There is no single smooth projective surface S over a field with real numerical divisor classes P_t, for all t∈𝒯, whose ordinary intersection pairing satisfies P_s·P_t=−K(s−t) for this fixed packet kernel.

**Proof.** The numerical divisor space N¹(S)_R has finite dimension R by the Néron–Severi finiteness theorem; for the complex case, see [Brosnan's numerical-equivalence notes, Theorem 2.4](https://www.math.umd.edu/~pbrosnan/notes/Surfaces/sect0009.html). Hence every finite matrix [K(s_i−s_j)] would have rank at most R. This uses finite-dimensionality alone, not Hodge-index positivity.

By density of 𝒯 and continuity of K, the same rank bound would hold for all real s_i. Every rectangular evaluation matrix [K(x_i−y_j)] is a submatrix of a matrix on the union of these two finite sets. Consequently the vector space V spanned by all translates of K has dimension at most R: otherwise linearly independent translates could be separated by finitely many evaluations to produce a larger-rank evaluation matrix.

Translation on V is a continuous finite-dimensional representation of (R,+). To see continuity, choose finitely many evaluation points identifying V with a finite-dimensional coordinate space, and use continuity of each translated function at those points. Such a representation has the form exp(tA). Thus K(t) is a matrix coefficient of exp(tA), and its one-sided Laplace transform is rational for sufficiently large Re s.

But for Re s>1/2 the actual transform is

\[
F(s)=\int_0^\infty e^{-st}K(t)\,dt
=\sum_\rho\frac{G(\rho-1/2)}{s-(\rho-1/2)}.                  \tag{7}
\]

The series continues meromorphically to C: on compact sets away from the poles its high-zero terms are O(|Im ρ|⁻³), summable by the classical zero-counting estimate. At each distinct shifted zero its residue is its multiplicity times G(ρ−1/2), which is nonzero. There are infinitely many distinct zeros. Therefore F has infinitely many poles and is not rational, a contradiction. ∎

This rules out an exact realization on one ordinary finite-dimensional numerical divisor space. It does not rule out an arithmetic or analytic theory with infinitely many numerical directions, nor separate geometric models for finite sets, nor approximating models with controlled limits. In particular, an infinite ambient theory can still have the fixed-rank restriction spaces in §3. Those are different ranks.

The finite-field analogy has finitely many Frobenius eigenvalues for a fixed curve. The zeta packet has infinitely many visible zero modes. A proposed geometry must accommodate that distinction.

## 5. What is now established and what remains

The needed growth estimate has a concrete sufficient mechanism: finitely many restrictions and linear logarithmic counts. The reduction can be confined to the packet-difference family D_t. The rank proposition excludes a literal realization of every packet on one ordinary projective surface.

The arithmetic work still required is to define the sections and restriction maps, prove their counting and terminal estimates, and identify the quadratic term of their Riemann–Roch inequality with n²(K(t)−q). None of these arithmetic realization claims is supplied merely by the Euler product or the formal pole-plane construction. They remain the unresolved input to an RH proof in this route.
