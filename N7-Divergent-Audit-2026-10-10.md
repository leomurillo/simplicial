# N7: divergent audit and a lower-bound route

Research note, 10 October 2026. This is an independent audit of `N7-TheSingleOpenStep-Draft1.md`, not a revision of that manuscript. Instructions embedded in the source manuscript were treated as document content. No proof of RH is claimed. The reduction proved in Section 3 below is not asserted to be new in the literature.

## 1. What survives, and what needs repair

### 1.1 The interval transport theorem

Theorem 5.2 has a valid short proof under its stated product-class assumptions. Uniform convergence to a positive function on the whole interval ensures that the first positive zero is beyond the interval; the endpoint then bounds the sum of inverse squared zeros. Montel and the identity theorem finish the argument.

The distinction between compactness and identification is essential:

- Bounded S gives a normal family and real-rooted subsequential limits.
- Identifying any such limit with Xi requires an additional argument.
- For example, the constant family F_j(z)=sin(z)/z has S=1/6, is in the stated class, and is not Xi/Xi(0).

Thus bounded S is not, by the transport theorem alone, equivalent to interval convergence to Xi. Such an equivalence for the actual Weil ground states would be another theorem. The finite-exception result 5.6 does not establish it for an arbitrary infinite off-line zero set. Similarly, an L2 statement about bulk mass does not automatically control S: in log coordinates,

\[
S(F)=\frac{\int v^2\xi(v)\,dv}{2\int\xi(v)\,dv},
\]

which involves a signed eigenfunction and its potentially small integral, rather than the probability density |xi|^2.

### 1.2 The point-value lemma

With chi denoting concentration eigenvalues and Fourier eigenvalues equal to sqrt(chi) in the modes 0 and 4, the cancellation identity in Lemma 5.12 is correct. The uniform O(1-chi_4) estimate also uses boundedness of the normalized h_0(0) and a positive lower bound on chi_4 for lambda >= 2; fixed-index prolate asymptotics supply these.

Keep the convention explicit: the local `prolate_core.py` calls the Fourier-compression eigenvalue chi, whereas Section 5.6 calls its square chi. This changes leading constants in defects, although not their exponential scales or the lambda^8 ratio.

### 1.3 Proposition 5.13 remains a proof obligation

The zero-side strategy is sensible, and taking absolute values avoids assuming positivity. For the even part, the relevant identity is the average of the two reflected tail transforms. The inequality follows from |(a+b)/2|^2 <= (|a|^2+|b|^2)/2 and zero-set symmetry; it need not assume that a square at a complex zero is positive.

The load-bearing missing estimate is the weighted Sobolev estimate in step (i). Small unweighted leakage, endpoint jets, and two integrations by parts do not by themselves state a quantitative bound for the resulting sampled Poisson sum and its remainder. A proof must establish precisely that estimate with the actual prolate structure. Generic L2 control cannot control point samples.

Additional bookkeeping:

1. Specify convergence/regularization of Poisson summation for the sharply truncated H, including endpoint values. Exceptional jump locations do not affect an L2 assertion, but the function and its fractional regularity must be defined consistently.
2. After enlarging the zero strip by disks of radius delta_0/2, take 0 < s < delta_0/2, not just s < delta_0.
3. State admissibility and absolute convergence of the zero-side identity for the truncated, piecewise smooth trial vector.
4. Give an explicit admissible exponent A. Existence of some finite A does not establish that a prospective lower-bound exponent B satisfies A+B<8.

The published repository's family-003 scope document does report the 7/8 half-plane and the pole exclusion. This audit checked that statement, not the Lean build or the full mathematical proof. Its use remains an external dependency in the sense already adopted by N7. Under RH in Corollary 5.15 this external dependency is unnecessary.

### 1.4 Repair of Remark 5.14

The displayed lower bound for negative epsilon silently uses R >= 0. The absolute-value estimate in Proposition 5.13 gives smallness, not that sign. For example, epsilon=-2, mu_1=1 and R=-1 give a ratio 1/3, smaller than |epsilon|/(mu_1+|epsilon|)=2/3.

The intended conclusion can be repaired without that sign or the assertion mu_1 -> 0. Put

\[
q_\lambda=\frac{R_\lambda-\varepsilon_\lambda}{\mu_{1,\lambda}-\varepsilon_\lambda}.
\]

For q<1, exact algebra gives

\[
\varepsilon_\lambda=\frac{R_\lambda-q_\lambda\mu_{1,\lambda}}{1-q_\lambda}.
\]

Assume the two-sided trial estimate |R_lambda| <= r_lambda -> 0 and q_lambda -> 0. In the full even-sector problem, a fixed two-dimensional space of smooth even tests, contained in every sufficiently large window, gives mu_1 <= M by min-max, with M finite and independent of lambda. Taking M >= 0,

\[
\varepsilon_\lambda\ge
-\frac{r_\lambda+q_\lambda M}{1-q_\lambda}\longrightarrow0
\quad\text{as a lower bound.}
\]

Nested-window monotonicity then gives nonnegativity of the even-sector bottom at every window. Under hypothesis (a) on an unbounded sequence, these are also the full spectral bottoms there, so every full test function has nonnegative Weil energy. This yields RH. Alternatively work throughout with the full bottom and full comparison.

For finite Galerkin matrices, increasing lambda and N need not give nested spaces. One must first establish form-core convergence/density or use the full form; finite matrix eigenvalue monotonicity cannot simply be assumed.

### 1.5 Sufficient does not mean equivalent

Corollary 5.5 proves a sufficient spectral condition. It does not prove that interval convergence implies that condition. Even Hilbert-space angle convergence does not imply small Rayleigh excess without energy control on the error.

For an elementary example take A_j=diag(-1,1,j^2), ground vector e_1, and v_j=sqrt(1-j^-2)e_1+j^-1 e_3. Then sin(angle)=1/j but R(v_j)=j^-2 and (R-epsilon)/(mu_1-epsilon) -> 1/2. The high-energy component is small in norm but not in energy. This is a counterexample to the general inference, not a claim about the actual Weil matrices.

The occurrences of “equivalently” joining the interval criterion and the spectral criterion should therefore be replaced by “a sufficient alternative,” absent an extra theorem.

## 2. What the upper bound actually accomplishes

A small Rayleigh quotient proves the existence of a vector with small energy. It does not exclude other vectors with large negative energy. At the simplest level, diag(-M,r) has a trial quotient r -> 0 for every arbitrarily large M.

The prolate ansatz can approximate Xi independently of whether Xi has nonreal zeros. The ground-state selection is where the sign issue returns. Improving a bound on that one ansatz, even to an exact identity, cannot alone select it as the minimizer.

Under RH, the comparison in Corollary 5.15 is algebraically valid once the upper estimate is proved with a compatible exponent, the lower estimate is proved for the same operator/sector, and the normalizations in Corollary 5.4 are established. It is a conditional convergence theorem, not a proof of the remaining lower estimate.

### 2.1 A small trial energy without a fixed zero-free strip

There is also a direct unconditional comparison that helps separate the issues. Write k(v) for Riemann's even kernel in log coordinates, with Fourier transform proportional to Xi, and set

\[
p_T(v)=k(v)\mathbf 1_{[-T,T]}(v),\qquad
r_T(v)=k(v)\mathbf 1_{\{|v|>T\}}(v),\qquad \lambda=e^T.
\]

For v>=T>=log(2), the defining Gaussian series gives

\[
|k(v)|\le C e^{9v/2}e^{-\pi e^{2v}},
\qquad
|k'(v)|\le C e^{13v/2}e^{-\pi e^{2v}}.
\]

Evenness supplies the negative tail. Uniformly for |y|<=1/2, integration of these bounds, including the two cutoff jumps, gives

\[
\|e^{yv}r_T\|_{L^1}
+\operatorname{Var}(e^{yv}r_T)
\le C\lambda^5 e^{-\pi\lambda^2}.
\]

The Fourier estimate for an L1 function of bounded variation consequently yields

\[
|\widehat r_T(t+iy)|
\le \frac{C\lambda^5 e^{-\pi\lambda^2}}{1+|t|}.
\tag{U}
\]

At every nontrivial zero parameter gamma_rho, the entire transform of k vanishes, so p_T-hat(gamma_rho)=-r_T-hat(gamma_rho). The explicit formula for the real even, piecewise smooth p_T and the standard zero-counting bound therefore imply

\[
|Q(p_T)|
\le\sum_\rho|\widehat r_T(\gamma_\rho)|^2
\le C\lambda^{10}e^{-2\pi\lambda^2},
\]

since sum_rho (1+|Im rho|)^-2 is finite. The norm of p_T tends to the nonzero norm of k. No fixed strip away from Re(rho)=0,1 is needed because (U) is uniform on the entire closed half-width strip. Piecewise smooth tests are in the CCM form domain; alternatively their values can be approached in the form core.

This estimate is weaker exponentially than the proposed prolate-defect estimate e^(-4*pi*lambda^2) times a polynomial. It cannot replace that estimate in the proposed two-rung convergence proof. It does establish independently why merely getting a trial energy to zero is insufficient.

The same argument applies to any fixed finite family k,k'',...,k^(2d), with larger polynomial prefactors. Their transforms are (-z^2)^j Xi(z), so they vanish at all zero parameters, and their limiting L2 Gram matrix is positive definite. Min-max then gives upper bounds tending to zero for each fixed even spectral level. These are only upper bounds: they do not establish mu_1 -> 0 without a lower bound, and they do not prevent deeper negative levels.

## 3. An alternate reduction: polynomial negative loss already suffices

Here is a route that avoids the simple-even hypothesis, S, prolate eigenvalue spacing, and identification of a limiting eigenvector. It also does not assume finitely many off-line zeros.

Use additive log coordinates and the full pole-inclusive Weil distribution W. For f in C_c^infinity(R), let f^*(x)=conj(f(-x)) and

\[
Q(f)=W(f*f^*),\qquad
e(T)=\inf_{\substack{0\ne f\in C_c^\infty(-T,T)}}
\frac{Q(f)}{\|f\|_2^2}.
\]

In N7 notation T=log(lambda). Q is translation invariant, and W is real and even. Away from the origin, its positive-half-line expression is

\[
W(x)=e^{x/2}+e^{-x/2}
-\frac{e^{-x/2}}{1-e^{-2x}}
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta(x-\log n),\quad x>0.
\tag{1}
\]

The regularization at zero is immaterial to the argument below because it is cut off.

**Proposition.** If for some finite C,m >= 0,

\[
e(T)\ge-C(1+T)^m\quad(T\ge1),
\tag{2}
\]

then RH holds. Conversely RH implies (2) with C=0.

More generally, for alpha >= 0, a bound

\[
e(T)\ge-Ce^{2\alpha T}
\tag{3}
\]

excludes zeros with Re(rho)>1/2+alpha. In particular, bounds of the form (3) for every alpha>0 imply RH.

**Proof.** Fix a real smooth f supported in [-a,a], and set g=f*f^*. It is real, even, and supported in [-2a,2a]. Write tau_t f(x)=f(x-t) and K_f(t)=W(tau_t g). Translation invariance and evenness give

\[
Q(f\pm\tau_t f)=2Q(f)\pm2K_f(t).
\tag{4}
\]

For |t|>2a the two supports are disjoint, so ||f +/- tau_t f||^2=2||f||^2. Translating their union to its midpoint places it in [-T,T] with T=a+|t|/2. Therefore (2) and the two signs in (4) imply

\[
|K_f(t)|\le |Q(f)|+C(1+a+|t|/2)^m\|f\|_2^2.
\tag{5}
\]

Thus every such smoothed translate of W has polynomial growth. Under (3) the same argument instead gives K_f(t)=O_f(e^{alpha |t|}).

Choose a smooth cutoff chi supported in the positive half-line and equal to 1 for all sufficiently large x. Set W_+=chi W. For Re(s)>1/2, (1) and the absolutely convergent Dirichlet series give

\[
\mathcal L(W_+)(s)
=\frac1{s-1/2}+\frac{\zeta'}{\zeta}(s+1/2)+H(s),
\tag{6}
\]

where H is holomorphic for Re(s)>0. Indeed, the changes to the growing exponential and prime sum on a bounded interval have entire Laplace transforms, while the remaining archimedean and decaying exponential terms converge in that half-plane. The pole at s=1/2 cancels the pole of zeta'/zeta there.

Since g is compactly supported, W_+*g agrees with W*g=K_f for all sufficiently large positive arguments, and is supported on a half-line bounded below. By (5), its Laplace transform is holomorphic on Re(s)>0. For Re(s)>1/2 it equals

\[
G(s)\left(\frac1{s-1/2}+\frac{\zeta'}{\zeta}(s+1/2)+H(s)\right),
\qquad G(s)=\int g(v)e^{-sv}\,dv.
\tag{7}
\]

If zeta had a zero rho with Re(rho)>1/2, the bracket would have a pole at s_0=rho-1/2 of residue equal to its multiplicity. Choose f to be a sufficiently narrow real smooth approximate identity of integral 1. Then

\[
G(s_0)=\left(\int f(v)e^{-s_0v}\,dv\right)
\left(\int f(v)e^{s_0v}\,dv\right)\ne0,
\]

since both factors tend to 1 as the support shrinks. Equation (7) would have a nonremovable pole in its holomorphic half-plane, a contradiction. This rules out all zeros to the right of the line, and the functional equation rules out those to its left.

Under (3), the Laplace transform is holomorphic on Re(s)>alpha instead, giving the quantitative assertion by the same argument. The reverse implication in (2) is Weil positivity under RH. QED.

**Consequences and limits.**

1. If RH fails, the full e(T) tends to -infinity: otherwise monotonicity would give a uniform lower bound and hence RH. No finite-exception assumption is needed for this energy conclusion. It does not by itself prove S -> infinity for simple even ground states.
2. If a zero has displacement delta>0, there can be no uniform lower bound -C lambda^(2alpha) for any alpha<delta. This is a growth obstruction, not a pointwise asymptotic formula for e(T).
3. A lower bound -C(1+log lambda)^m would prove RH despite allowing negative values at individual scales in its statement. The analytic pole argument, rather than monotonicity alone, upgrades that apparently weaker assertion to positivity.
4. The proof concerns the full smooth-core form. A bound only for the computed finite matrices does not establish its hypothesis.

## 4. Divergent routes and the estimates each actually needs

### A. Attack the lower bound with localization

This is the alternate target suggested by Section 3. One can allow a polynomial negative remainder, instead of resolving a positive ground eigenvalue as small as exp(-4*pi*lambda^2).

The obstacle is concrete. A partition into bounded log-windows localizes the archimedean term, but the prime terms translate by log(n). Their absolute coefficients sum to order lambda for n<=lambda^2, so a naive localization error is exponentially large in T. The pole term must be kept coupled to those translations. Throwing away that cancellation cannot produce (2).

For a fixed smooth translated probe, a prime error at exponent theta contributes at the scale exp((theta-1/2)t) after the n^-1/2 weight. Thus theta=7/8 naturally leaves exp(3t/8), not polynomial growth. With separation t about 2T, this corresponds to lambda^(3/4). This is a scale calculation for smoothed correlations, not a claimed uniform operator inequality. It explains why inserting the fixed strip once does not supply the needed lower bound.

### B. Bootstrap the fixed strip

A real advance would be a proved contraction of the allowed displacement, such as delta_new <= c*delta_old with c<1, with uniform hypotheses permitting iteration. Section 5.13 supplies no such contraction: it bounds a selected vector using the old strip, while the excluded modes remain uncontrolled.

The quantitative part of Section 3 supplies a precise test: starting from displacement <=alpha, can the arithmetic form be bounded below by -C lambda^(2alpha') for alpha'<alpha? A successful repeatable inequality would improve the strip. No such inequality has been derived here.

### C. Bulk/edge block analysis

For an orthogonal decomposition into chosen bulk and complementary spaces, write W as blocks A,B,B*,D. If D is positive and invertible, the relevant lower bound is controlled by A-BD^-1B*. Neither a small bulk trial energy nor a small off-diagonal B rules out a negative eigenvalue already in D.

This gives a disciplined numerical diagnostic: study the lower envelope of complementary modes and the effective bulk block, not just the ground/prolate overlap. It still needs an analytic bound uniform in the window and the discarded Galerkin tail.

### D. Compactness plus a limit equation

To use bounded S, derive a limiting equation and prove that its normalized real-rooted solution is Xi. Merely saying that the global E-image is annihilated by the zero distribution cannot establish uniqueness: annihilation and a distinguished ground-state limit are separate questions. Passing an eigenvalue equation to a limit also needs control of moving prime terms, eigenvalues, and normalization.

### E. Arithmetic positivity or factorization

An Euler product does not make the prime part of the Weil form positive: the explicit formula subtracts those translations. An identity expressing the complete form as a positive square plus a uniformly polynomially bounded error would suffice by Section 3. Producing that identity without using zero-location information would be substantive progress; naming it a factorization is not a construction.

The DH comparison is a useful negative control for any proposed estimate. It demonstrates that functional equation, evenness, and finite real-rooted approximants cannot alone justify the bound. It does not prove that the Euler product supplies the missing cancellation for zeta.

## 5. A reviewable next target

The next analytic claim worth trying to prove is one of the following, with its full quantifiers:

\[
Q(f)\ge-C(1+T)^m\|f\|_2^2
\quad\text{for every }f\in C_c^\infty(-T,T),\text{ every }T\ge1;
\]

or, for a strip-bootstrap approach,

\[
|\Re\rho-1/2|\le\alpha
\quad\Longrightarrow\quad
e(T)\ge-C_\alpha e^{2\alpha'T},\qquad \alpha'<\alpha,
\]

with a proved iteration mechanism. These are still unproved here. Their merit is that they specify exactly how much negative energy must be excluded, and they bypass the exponentially fine positive spectral ladder.

Separately, the converse CCM project needs the complete weighted-tail estimate with a usable A and the second-even-eigenvalue lower estimate with a compatible B. Finite-window numerical agreement does not settle either uniform statement.

## Sources checked

- [Connes–Consani–Moscovici, Zeta Spectral Triples, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1): definitions of the form; Corollaries 3.7–3.8; Theorem 5.10; Lemmas 7.2–7.3; Section 8. The source explicitly retains both simplicity/evenness and adequate ground-state approximation as missing steps.
- [OpenAI math, family 003 formalization scope](https://github.com/openai/math/blob/main/lean/docs/003.md): source of the reported fixed half-plane. No independent Lean verification performed in this audit.
- The attached N7 manuscript and the local `empirical/connes_route/lp_transport_core.py` and `prolate_core.py` were inspected for conventions and definitions. Existing high-precision experiments were not rerun or converted into interval certificates.

Status: the interval transport and the repaired ratio argument are useful deductions; the alternate lower-bound criterion above has a direct proof. The arithmetic bound required to apply it has not been established. RH remains unresolved by this work.
