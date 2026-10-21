# Arithmetic Hodge-index attempt: the pole plane and section growth

11 October 2026. Based on the newly added Paper 53 §4.9. The goal of this pass is the sign theorem needed to turn its formal intersection dictionary into a proof, not another finite-window extrapolation.

**Outcome.** The formal intersection form and its inertia are determined exactly. A minimal conditional section-growth argument is given below. The required arithmetic section theory and its estimates have not been constructed, so this does not establish the all-clock inequality or RH.

## 1. The restored pole plane has an exact inertia formula

Let M be any finite Hermitian Weil Gram matrix on selected packets. Let J be the hyperbolic plane

\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Let B record two proposed degree/pole couplings of those packets. Define the formal intersection matrix

\[
\mathcal I=
\begin{pmatrix}BJB^*-M&B\\B^*&J\end{pmatrix}.
\tag{1}
\]

This construction makes sense regardless of the sign of M. With

\[
T=\begin{pmatrix}I&0\\-JB^*&I\end{pmatrix},
\]

direct multiplication gives

\[
T^*\mathcal I T=\begin{pmatrix}-M&0\\0&J\end{pmatrix}.
\tag{2}
\]

Consequently

\[
\boxed{n_+(\mathcal I)=1+n_-(M),\quad
n_-(\mathcal I)=1+n_+(M),\quad n_0(\mathcal I)=n_0(M).}
\tag{3}
\]

Here n_+, n_-, n_0 denote positive, negative, and zero inertia. Thus the statement that the formal arithmetic intersection form has only one positive direction is **exactly** M≥0. Formula (1) supplies the algebraic dictionary, not its sign theorem. Changing the chosen degree couplings B does not remove a negative direction of M.

For the actual pole term, write ell_±(f)=∫f(x)e^{±x/2}dx. The pole pairing is ell_+(f)conj(ell_−(g))+ell_−(f)conj(ell_+(g)), which has the form BJB*. A translation multiplies ell_± by e^{±t/2}, with the choice of translation orientation fixed consistently. This explains the hyperbolic-plane interpretation without assuming its orthogonal complement is negative.

## 2. Effective-looking entries are not the missing theorem

The exact rational matrix

\[
\mathcal I_{\rm test}=
\begin{pmatrix}
0&11&1&1\\11&0&1&4\\1&1&0&1\\1&4&1&0
\end{pmatrix}
\]

has nonnegative entries, zero self-intersections for its two formal graph classes, positive fibre degrees, and the correct hyperbolic fibre block. Its primitive block is

\[
\begin{pmatrix}-2&6\\6&-8\end{pmatrix},
\qquad\det=-20.
\]

It therefore has full inertia (2,2), by (2). It is a formal Hasse-violating control, not the intersection matrix of an actual curve product. Nonnegative intersection entries and graph-degree bookkeeping do not establish the geometric Hodge-index theorem.

The probe independently counted 105 points on y²=x³+x+1 over F_101, confirming the trace −3 used by the peer's certificate. That verifies its initial point-count input; it does not transplant the geometric positivity theorem to Q.

## 3. The weakest section-growth implication needed in this route

Here is a conditional lemma specifying the missing geometric input. It is not an assertion that the necessary arithmetic objects already exist.

**Section-growth lemma.** Suppose a real divisor class D in the primitive subspace has an independently defined self-intersection D². Suppose nonnegative section dimensions h(nD), h(K−nD) satisfy, for positive integers n,

\[
h(nD)+h(K-nD)\ge\frac12n^2D^2-O_D(n),
\tag{4}
\]

and independently

\[
h(nD)+h(K-nD)=o_D(n^2).
\tag{5}
\]

Then D²≤0. Indeed, divide (4) by n² and use (5).

Thus this proof route does not need a full Riemann–Roch equality, a strict negative margin, or uniformity in D. A one-sided quadratic lower bound and subquadratic growth along each fixed primitive ray suffice. The constant may depend on D, since each finite test is settled separately.

For the packet combination c, (2) identifies the primitive self-intersection with −c*Mc. If (4)–(5) are proved for every real rational coefficient combination of the two-clock packets, continuity extends the sign to all real coefficients, hence to complex coefficients for the real symmetric kernel. Every finite M is then semidefinite; the two-clock theorem gives RH.

The two inputs must be independent. Defining h using the positive spectral subspace of M and then asserting (5) merely inserts the desired sign into the construction. Likewise, an Euler-characteristic identity alone does not bound the two nonnegative section dimensions in (5).

## 4. Where existing arithmetic Riemann–Roch results enter

[Connes's account of the Riemann–Roch strategy](https://alainconnes.org/wp-content/uploads/EssayRH.pdf), §§2.3 and 4.3.2, explicitly separates arithmetic-curve Riemann–Roch from the proposed intersection theory and inequality on the square. It identifies a surface-type section inequality as the missing step in that framework. [Connes–Consani, *Riemann–Roch for the ring Z*](https://arxiv.org/abs/2306.00456), proves a formula for Arakelov divisors over an absolute base. Its abstract describes a degree/Euler-characteristic formula, not the needed sign theorem for every mixed packet correspondence.

These sources make the route mathematically grounded, but their statements do not by themselves identify section spaces satisfying (4)–(5) for the present two-clock form. This pass inspected the relevant strategy discussion and the later paper's abstract; it is not an exhaustive claim about all arithmetic geometry literature.

## 5. What the two clocks provide

The clocks give an injective homomorphism Z²→R, (m,n)↦m log2+n log3, with dense image. They organize every required correlation into one group algebra. They do not turn every other Euler factor into an integer monomial in those two generators: p=2^m3^n with integers m,n is impossible for primes p>3. Continuity recovers real zooms only after their arithmetic correlations have been controlled.

Accordingly, the group algebra and formal form already carry all zoom labels. What is absent is a positive arithmetic realization, or a section theory that forces the sign. This agrees with the earlier manuscript's distinction between scaling symmetry and polarization positivity.

A curve-level section formula for individual prime clocks does not automatically govern mixed clock correlations. A proposed extension must define the product/correspondence geometry and prove the subquadratic primitive-ray growth there, with the explicit-formula pairing as its intersection number.

## 6. Proof work completed and remaining

`empirical/connes_route/check_hodge_block.py` verifies (2) symbolically for arbitrary real symmetric two-packet M and arbitrary B, checks the formal indefinite control exactly, and counts the F_101 points independently. All checks passed; the corresponding JSON records them. No source manuscript was edited.

The formal pole-plane construction is now complete, and its exact relationship to every negative Weil direction is proved. To finish this route one must construct arithmetic section spaces for the packet correspondences, identify their quadratic Euler characteristic with (1), and prove the growth estimate (5). Neither a count of additional positive windows nor the existence of the formal matrix supplies those inputs.

The all-clock positivity theorem remains unproved in this work. The precise prospective advance is an independent section-growth theorem on the arithmetic square, strong enough to discharge (4)–(5).
