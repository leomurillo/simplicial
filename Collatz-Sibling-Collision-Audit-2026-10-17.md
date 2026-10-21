# Audit of the twin–sibling collision argument

17 October 2026. Review of the pasted progress report and Section 12.12 of 01g.

**Assessment.** The exact collision identity and the no-L2 proof withstand this audit. Novelty has not been established by an exhaustive literature review. The remaining sibling problem concerns collision-weighted regularity; it is not a prerequisite for ordinary total-variation regularity, which follows from Tao's Proposition 1.14. The minimum-operator transfer remains separate.

The affine-walk attack below proves that nonzero sibling states cannot reach the identity exactly. It also gives an explicit obstruction to the simplest distance-based bound. No uniform sibling-correlation bound is proved.

## 1. The no-L2 argument is sound

Use the manuscript's notation K_n=sum mu_n^2, f_n=(2/3)3^n K_n, c_m(k)=(2/3)3^m P(Y=A^kY' mod 3^m), and F_n=sum_(k>=1)4^(-k)c_(n-1)(k), where A(x)=4x+1.

Conditioning on the first geometric exponents gives the exact identity

\[
f_n-f_{n-1}=2F_n.
\]

There is a short version of the manuscript's contradiction proof. Suppose the law has density g in L2 with respect to normalized Haar measure. Then f_n tends to (2/3)||g||_2^2. Since A^(3^j) tends uniformly to the identity and composition is strongly continuous on L2, choose one fixed k=3^j with

\[
I_k=\langle g,g\circ A^{-k}\rangle>0.
\]

The cylinder conditional expectations of g converge in L2, so c_m(k) tends to (2/3)I_k. Hence, for all sufficiently large n,

\[
f_n-f_{n-1}\ge2\,4^{-k}c_{n-1}(k)\ge\varepsilon_k>0.
\]

This contradicts convergence of f_n. It uses just one positive sibling term and does not require interchanging the whole infinite sum with a limit.

Combining this with [Tao's fine-scale mixing theorem, Proposition 1.14](https://arxiv.org/html/1909.03562v5#S1.SS4), as detailed in our earlier mixing audit, gives the consistent conclusion: the law has a Haar density g in L1, but g is not in L2. The statement in Section 12.12 that absolute continuity is unsettled in that source needs correction.

## 2. An unconditional lower growth bound

The same reasoning can be adapted to the known L1 density without assuming it is in L2. Choose epsilon>0 such that E={g>=epsilon} has positive Haar measure. Translations by A^(3^j) are continuous on L1 for the indicator of E, so for some fixed k=3^j,

\[
\mathrm{Haar}(E\cap A^k E)>0.
\]

Write g_m=E[g | residues modulo 3^m]. Martingale convergence gives g_m->g almost everywhere; the same holds after composition with the fixed Haar-preserving map A^(-k). Fatou's lemma implies

\[
\liminf_m\langle g_m,g_m\circ A^{-k}\rangle
\ge\epsilon^2\mathrm{Haar}(E\cap A^kE)>0.
\]

Thus **F_n is bounded below by a positive constant eventually, and f_n>=c n eventually**, for some non-explicit c>0. This is a lower bound, not the upper bound needed for sibling transversality. The constant can be extremely small because the selected k may be large.

## 3. What the measurements do and do not show

If c_m(1) grows like a log m with a>0, positivity gives F_(m+1)>=c_m(1)/4, so sup F_n is infinite. Such growth is compatible with the weaker target F_n=o(f_(n-1)).

For example, if F_n~b log n with b>0, then f_n~2b n log n, and still nW_n->1/2. If F_n tends to a positive constant, the same limit holds. Thus observing nW_n near 1/2 cannot distinguish bounded sibling factors from logarithmically growing ones.

Likewise, small measured sibling coherence does not establish zero coherence. The exact formula in Proposition 12.34 expresses it through the relative increment of c_m(k). The phrase “siblings forget” should describe an asymptotic conjecture or finite numerical observation, not an exact identity asserting independence.

Uniform boundedness of F_n implies boundedness of c_m(k) for every fixed k. The converse needs summable control in k; separately bounded sequences for each k do not alone bound their weighted sum uniformly in m.

## 4. The affine collision walk

Put B_a(x)=(1+3x)/2^a. For an affine state h(x)=u x+v, with u a power of two and v a dyadic rational in Z_3, define

\[
H_m(h)=3^mP(Y\equiv h(Y')\pmod{3^m}).
\]

Conditioning on first steps a,b gives a transition to

\[
h_{a,b}=B_a^{-1}\circ h\circ B_b,
\quad
u'=2^{a-b}u,\qquad
v'=\frac{2^{a-b}u+2^a v-1}{3}. \tag{1}
\]

The branch is admissible precisely when v' belongs to Z_3; otherwise the collision is already impossible modulo 3. The recurrence is

\[
H_m(h)=3\sum_{a,b\ge1}2^{-a-b}
\mathbf1_{v'\in\mathbb Z_3}H_{m-1}(h_{a,b}),
\qquad H_0(h)=1. \tag{2}
\]

These are positive transfer weights, not probabilities: their row sum need not be one.

For a self-loop, equality of slopes forces a=b, and equality of offsets becomes

\[
(3-2^a)v=u-1.
\]

At the identity this holds for every a, giving total self-loop weight 3 sum_(a>=1)4^(-a)=1. For any other state, at most one a can work, so its self-loop weight is at most 3/4. This confirms the stated one-step observation. It does not control longer cycles or weighted paths escaping through infinitely many states.

## 5. No finite path from a nonzero sibling to the identity

**Proposition.** For every nonzero integer k, the state A^k cannot reach the identity through any finite sequence of the paired transitions (1).

**Proof.** Such a path of length l would imply B_w=A^k B_v for two words of equal length l. Conjugate by z=3x+1. The maps B_a become

\[
G_a(z)=1+3\,2^{-a}z,
\]

and A^k becomes multiplication by 4^k. Thus G_w=4^k G_v. For l>=1, the constant coefficient of G_w is

\[
C_w=1+\frac3{2^{a_1}}+\cdots+
\frac{3^{l-1}}{2^{a_1+\cdots+a_{l-1}}}.
\]

It has reduced odd numerator N_w and power-of-two denominator. For l>=2,

\[
N_w=2^{a_{l-1}}N_{\mathrm{prefix}}+3^{l-1},
\]

where N_prefix is odd. Thus a_(l-1)=v_2(N_w-3^(l-1)), and recursively the numerator determines all a_1,...,a_(l-1), and hence the denominator. If C_w=4^k C_v, their odd numerators agree, so their denominators also agree, and 4^k=1. For l=1 both constants are 1, giving the same contradiction. A path of length zero is excluded by k!=0. This proves the claim. The last exponent need not be recovered: it affects the slope but not the constant coefficient. Square.

The proposition removes exact access to the critical identity state. It does not remove arbitrarily close approaches or give a bound on their total weights.

## 6. A failed simple bound and the precise certificate target

Let depth(h)=max(0,min(v_3(u-1),v_3(v))) for a nonidentity state. The natural candidate B(h)=1+depth(h) fails.

Indeed A goes to h(x)=2x+1 when a=1,b=2, with transfer weight 3/8. For this h, admissible pairs are exactly odd a and odd b, with total transfer weight 3(2/3)^2=4/3. Every successor has B>=1, while B(h)=1. Thus the transfer of B at h exceeds B(h). Already the finite positive sum over a,b<=8 is 21675/16384>1. The state h also has a self-loop of weight 3/4 at a=b=1.

This demonstrates why “only the identity has a critical self-loop” is insufficient.

A useful sufficient certificate would be a finite-valued function B>=1 on all states reachable from the A^k, k>=1, satisfying

\[
B(h)\ge3\sum_{a,b\ge1}2^{-a-b}
\mathbf1_{v'\in\mathbb Z_3}B(h_{a,b}),
\qquad
\sum_{k\ge1}4^{-k}B(A^k)<\infty. \tag{3}
\]

Induction in (2) would give H_m(h)<=B(h), and consequently

\[
F_n\le\tfrac23\sum_{k\ge1}4^{-k}B(A^k).
\]

**No such certificate has been constructed here.** Any successful one needs more than the single depth coordinate tested above. Alternatively, a level-dependent bound could establish the weaker target without forcing F_n to remain bounded.

## 7. What a sibling upper bound would add

Let g_n(x)=3^n mu_n(x modulo 3^n). Orthogonality of martingale differences and the collision identity give

\[
\|g_n-g_{n-1}\|_2^2=3F_n.
\]

Tao's theorem gives ||g_n-g_(n-1)||_1=O_A(n^(-A)) for every A>0. If one proves even a polynomial bound F_n=O(n^B), interpolation gives, for 1<p<2 and theta=2/p-1,

\[
\|g_n-g_{n-1}\|_p
\le\|g_n-g_{n-1}\|_1^\theta
\|g_n-g_{n-1}\|_2^{1-\theta}.
\]

Choose A sufficiently large; the right side becomes summable in n. Hence **a polynomial sibling bound would prove g in Lp for every p<2**, while the audited theorem excludes L2. This is a substantive possible payoff of the sibling attack beyond already-known total-variation regularity. A polynomial bound alone does not force W_n->0 without further control of the increments.

It still would not supply a bound on endpoint-minimizing left Perron vectors or prevent active-policy entropy collapse. Those remain the two issues identified in the policy-concentration note. The no-L2 result is a reason to avoid a transfer argument that assumes a square-integrable Syracuse density.

## 8. Verification and document status

The independent checker `empirical_01g/kl/sibling_affine_audit.py` verifies the full geometrically summed collision identity in exact rational arithmetic through n=6, checks odd-numerator uniqueness on 341 finite prefixes, and verifies the explicit failure of the depth-only bound. All checks pass. The proofs above cover the infinite statements; finite checks do not establish limits or priority.

Keep `Collatz-Strict-Level-Improvement-Draft1.md` as an audit copy for now. It concerns the minimum operator and is not superseded by the collision argument. Archiving it is reasonable after the main manuscript incorporates the corrections and its proof and certificate coverage have been compared. No file was deleted or moved in this pass.
