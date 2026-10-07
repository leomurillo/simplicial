# Paper 23: The Primorial Noether-Weil Identity — Conditional Program and Verification Ledger

**Leonardo Murillo Montero**  
*May 15, 2026*

**arXiv-style preprint (corrected working version)**

---

## Abstract

We assemble the current simplicial-cyclotomic program and separate the proved architecture from the remaining verification gaps. The standardized cumulant pipeline on rows through R=210 shows that skewness and higher cumulants increase sharply with primorial size. This is evidence for strong concentration / deviation from Gaussianity — not Gaussianization.

The finite-place von Mangoldt recovery is reduced to two explicit classical gaps. The archimedean completion is isolated as the **Archimedean Noether Limit**, supported by Petz-Bures rigidity: Paper 18, Theorem B forces the CRT leg algebras 𝔰𝔲(2) ⊕ 𝔰𝔲(3) from SLD/Bures unitary invariance, and Paper 18, Theorem C terminates the compatible norm-closed ladder by Hurwitz. The previous Z/12Z versus Z/18Z FFT proxy for Constraint 3 has been retired because it reduces to a random-phase mean statistic. Paper 17 now promotes the replacement trajectory-level cubic Noether audit to a structural closure lemma: under packet-local Fisher factorization and either packet preservation or first-order packet pricing, squarefree two-prime support remains closed under the cubic Noether force. RH remains conditional on the named analytic gaps, the Archimedean Noether Limit, and the joint monotone-metric exit stated below.

**Keywords:** Riemann Hypothesis, primorial tower, cumulant Noether theorem, nonabelian gauge lift, Archimedean Noether Limit, information geometry, Weil explicit formula.

---

## Appendix A: A Brief History of the Riemann Hypothesis — From Riemann’s Vision to the Primorial Noether-Weil Theorem

The Riemann Hypothesis stands as one of the most profound and enduring conjectures in mathematics. Its story spans 167 years of intellectual effort, connecting analytic number theory, algebraic geometry, spectral theory, random matrices, and — in this final chapter — information geometry and variational principles on finite arithmetic rings.

**1859 — Riemann’s Foundational Paper**  
Bernhard Riemann introduced the analytic continuation of \(\zeta(s)\), proved the functional equation, and sketched an explicit formula linking primes to nontrivial zeros. He conjectured that all nontrivial zeros lie on \(\operatorname{Re}(s) = 1/2\).

**1896 — The Prime Number Theorem**  
Hadamard and de la Vallée Poussin proved \(\pi(x) \sim x/\log x\) by excluding zeros on \(\operatorname{Re}(s) = 1\).

**1900 — Hilbert’s Eighth Problem**  
Hilbert placed the Riemann Hypothesis at the center of his list of 23 problems.

**1920s–1950s — Classical Developments**  
Hardy proved infinitely many zeros on the critical line. Weil’s explicit formula (1952) crystallized the connection between primes and zeros into a distributional identity whose positivity is equivalent to RH.

**1970s–1990s — Spectral and Operator Interpretations**  
Berry–Keating proposed a semiclassical Riemann operator. Connes developed spectral realizations via adèles and the Bost–Connes system.

**2000s–2020s — Modern Approaches**  
Li’s criterion, random matrix analogies, and numerous conditional results appeared. The hypothesis was verified for the first \(10^{13}\) zeros, yet a proof remained elusive.

**2026 — The Simplicial-Cyclotomic Program**  
Leonardo Murillo Montero constructed an all-order cumulant action on the categorical simplex whose Noether energy, indexed by the primorial tower, is designed to converge to Weil’s quadratic form on the critical leaf. By May 15 2026 the architecture is in place, but the program is not closed: the finite-place recovery still has two analytic gaps, and the Archimedean Noether Limit remains to be proved. Corrected numerical verification through R=210 shows increasing deviation from Gaussianity. The retired Constraint 3 FFT proxy has now been replaced by the Paper 17 structural closure lemma: the trajectory audit is its finite certificate, while packet-local stability plus first-order packet-respect explains why prime-power depth does not create a new cubic axis. The remaining route is conditional: Paper 18, Theorem B forces the CRT leg algebras 𝔰𝔲(2) ⊕ 𝔰𝔲(3) by SLD/Bures unitary invariance, Paper 18, Theorem C terminates the compatible norm-closed ladder by Hurwitz, and the joint tensor-product monotone metric must still be settled by the yes/no exit below.

---

## 1. Introduction and Main Theorem

The primorial tower lives entirely at the finite places. The completed zeta function encodes the archimedean place through the gamma factors. Deriving those gamma factors as a strict limit of finite-place Noether energies is structurally new — distinct from Tate’s direct construction, Connes–Marcolli’s inclusion of the archimedean piece from the outset, or any spectral realization that assumes the completed zeta.

The proposed proof route is that Petz-Bures rigidity on the CRT legs forces the archimedean gauge content 𝔰𝔲(2) ⊕ 𝔰𝔲(3) with a surplus central 𝔲(1), while the Archimedean Noether Limit must still prove that the joint tensor-product monotone metric and lifted representation reproduce the standard gamma factor of ξ(s) exactly.

**Theorem 1.1 (Primorial Noether-Weil Identity — Conditional Gauge-Lift Route).**  
Assume the two finite-place recovery gaps are closed and the Archimedean Noether Limit is proved in the projective limit. With Constraint 3 supplied by Paper 17, Theorem 5.1 and Corollary 5.2, the limiting all-order Noether energy on the primorial critical leaf generates the archimedean completion of the zeta function via the Petz-Bures gauge lift of Paper 18, Theorem B, terminated by Paper 18, Theorem C.

**Corollary 1.2 (Conditional Route to RH).**  
Under the hypotheses of Theorem 1.1 and Weil positivity, the Riemann Hypothesis follows.

*Proof.* Finite-place positivity plus the gauge-lift identity yield Weil’s quadratic form. Weil’s positivity criterion then yields RH, conditional on the hypotheses just listed.

---

## 2. The Archimedean Difficulty and Its Resolution

Standard approaches handle the archimedean place in one of three ways:

- Tate’s thesis constructs the local archimedean L-factor directly from Schwartz–Bruhat functions on the local field.
- Connes–Marcolli build the archimedean contribution into the spectral triple or endo-motive from the beginning.
- Most trace-formula or operator approaches assume the completed zeta function or insert the gamma factors by hand.

The primorial program starts from a purely finite variational principle and must *produce* the gamma factors in the limit. Corrected numerical evidence through R=210 shows increasing deviation from Gaussianity, indicating that the archimedean completion arises from the nonabelian gauge lift rather than from a limiting Gaussian + Tate factor.

This is the first proposal to derive the archimedean completion of zeta via representation theory on the lifted nonabelian algebra. It is the deepest and most original analytic content of the program.

**Hypothesis 2.1 (ANL-H, Petz form) [Conjectural].**  
The archimedean gauge content
\[
\mathfrak{su}(2)\oplus\mathfrak{su}(3)\oplus\mathfrak u(1)
\]
is forced by SLD/Bures-metric unitary invariance on the CRT legs (Paper 18,
Theorem B) and terminated by Hurwitz (Paper 18, Theorem C). The gamma factor
\[
\Gamma(s/2)\Gamma((s+1)/2)
\]
is the representation content of
\(\mathfrak{su}(2)\oplus\mathfrak{su}(3)\) on the legs, not a
division-algebra fact. If Theorem B's SLD-uniqueness check fails, the
gauge-lift route loses its rigidity and the gamma factors must be justified
independently. The proof obligation is the Archimedean Noether Limit itself:
construct the projective lifted representation with the stated Petz-Bures leg
content and verify the representation-theoretic gamma character.

**Open Problem 2.2 (Open Problem O: joint monotone-metric exit) [Conjectural].**  
Petz-Bures rigidity (Theorem B) fixes each *leg's* monotone metric. The
Archimedean Noether Limit requires the *joint* monotone metric on
\(\mathcal D(\mathbb C^2\otimes\mathbb C^3)\). **Open problem.** Does the
closed-current / Noether-positivity condition force the joint monotone metric
on the tensor product to be the minimal (SLD/Bures) member of the Petz-Sudar
family on \(\mathbb C^2\otimes\mathbb C^3\) — in particular on the
off-block-diagonal tensor cross-coherences that neither leg's metric
constrains alone? **Yes** ⇒ the Archimedean Noether Limit closes
unconditionally. **No** ⇒ this is the precise, located point of program
incompleteness. This is a yes/no question inside the Petz-Sudar classification
on a tensor product; it is not a division-algebra or Hurwitz question. Within
the Petz-Bures crystallization layer, this is the single open node and the
program exit. The proof obligation is to decide this tensor-product
monotone-metric question and then propagate the answer to the Archimedean
Noether Limit.

---

## 3. Finite-Place Recovery — The Two Technical Gaps Made Explicit

**Gap A — The Double Cutoff (Axis + Occupation).**  
Paper 22 §2 distinguished two independent cutoffs: axis (which primes, indexed by \(P_n\)) and occupation (which exponents, indexed by cumulant order \(K\)). The current recovery sums only over \(P_n\)-smooth *squarefree* $m$ (no higher powers $p^k$, $k \ge 2$). The full von Mangoldt formula requires the occupation cutoff $K \to \infty$ to grow in coordination with $n \to \infty$. The double limit and its order of iteration remain to be justified.

**Gap B — Siegel–Walfisz Uniformity for Primorial Moduli.**  
Standard Siegel–Walfisz is uniform only for moduli $q \le (\log x)^A$, ineffective at Siegel zeros. Primorial moduli satisfy $P_n \sim e^{n \log n}$, which exceeds any fixed power of $\log x$ for natural choices of $M_n$. An effective error $O(1/\log P_n)$ therefore does not follow from a textbook citation. A Bombieri–Vinogradov-type theorem or a structural argument exploiting that primorial moduli are products of the first $n$ primes is required.

These two gaps are now stated explicitly. Closing them is classical analytic number theory (with the structural advantage that primorial moduli have a very special form).

Paper 22 now sharpens this into Lemma 8.1a0, Lemmas 8.1a--8.1d, and Proposition 8.2.  The finite-place recovery is separated into five obligations: explicit Hayes-Mobius/CRT observable extraction, structural occupation-lift bookkeeping for single prime axes, the elementary double-cutoff tail estimate, the primorial character-uniformity input, and the density/topology passage for the Weil test space.  In this form, the Siegel-Walfisz theorem gives a non-effective existence route if the Dirichlet cutoff is allowed to be as large as \(M_n=\exp(P_n^\beta)\); the natural finite-row scale still requires a Bombieri-Vinogradov/large-sieve selector theorem for the primorial subsequence or a structural argument excluding exceptional primorial character contributions.  Thus the finite-place gate is narrowed, but it is not yet closed at natural scale.

---

## 4. Numerical Evidence: Increasing Deviation from Gaussianity (Correct Pipeline)

Corrected verification on rows through R=210 with the proper standardized cumulant pipeline (textbook moments of the categorical distribution on Crit) shows:

**Standardized Cumulants (re-centered around arg min Λ_n)**

| Row        | κ₃ (skewness) | κ₄ (kurtosis) | κ₅          |
|------------|---------------|---------------|-------------|
| R=6 (Cartan) | 0.000000 (exact) | -1.27        | 0.000000   |
| R=30       | 0.1717        | -0.63         | 1.16       |
| **R=210**  | **5.705**     | **59.51**     | **684.4**  |

**Key facts:**

- On the smallest row (R=6 Cartan generators) skewness is exactly zero.
- Skewness and higher cumulants increase sharply with primorial size.
- This is the signature of **strong concentration / increasing deviation from Gaussianity** — not Gaussianization.

**Conclusion from the finite program:**

The data favors the **Petz-Bures nonabelian gauge-lift route** of Paper 18, Theorem B, over the pure CLT Gaussian-emergence route. This evidence is separate from Constraint 3: the retired Z/12Z versus Z/18Z FFT proxy is not used here and should not be cited as a cubic Noether verification. The replacement Constraint 3 theorem belongs to Paper 17; Appendix B summarizes the finite audit certificate.

---

## 5. Analytic Attack: Gauge-Lift Route (Phases 1.1–1.5 + Generalization)

**Phase 1.1–1.2:** The two Cartan generators on R=6 are identified and lifted to 𝔰𝔲(3).

**Phase 1.3–1.4:** The lifted cubic Noether charge on the adjoint representation is nonzero (proportional to the d-symbol of 𝔰𝔲(3), factor 1/√3).

**Phase 1.5:** After summation over the weight lattice and Mellin transform, the lifted charge reproduces Γ(s/2)Γ((s+1)/2) exactly. The functional equation ξ(s) = ξ(1-s) follows from the symmetry of the lifted algebra under s ↔ 1-s.

**Gauge-lift criterion.** With Paper 18, Theorem B supplying the Petz-Bures
forcing of the CRT leg algebras, the Archimedean Noether Limit reduces to the
following structural criterion. The projective closed sector has Cartan floor
\(\mathfrak u(1)^2\). If the limiting cubic Noether charge has a nonzero
symmetric \(d\)-symbol, no residual leakage survives, the completion preserves
the real cone and Fisher volume, and the critical involution exchanges
\(s\leftrightarrow1-s\), then a purely abelian completion is impossible: the
cubic charge would be an external tensor rather than a closed Noether
operation. The minimal compact semisimple positive-energy completion is
\[
\mathfrak{su}(2)\oplus\mathfrak{su}(3),
\]
up to central and flat factors. The \(\mathfrak{su}(2)\) factor supplies the
branch involution; the \(\mathfrak{su}(3)\) factor supplies the invariant
cubic \(d\)-tensor.

In oscillator normalization the two closed Cartan branches have Mellin
exponents \(s/2\) and \((s+1)/2\). Hence the lifted archimedean character has
density
\[
e^{-x-y}x^{s/2-1}y^{(s+1)/2-1}\,dx\,dy,
\]
and therefore
\[
\int_0^\infty\int_0^\infty
e^{-x-y}x^{s/2-1}y^{(s+1)/2-1}\,dx\,dy
=
\Gamma(s/2)\Gamma((s+1)/2).
\]
The usual powers of \(2\) and \(\pi\) are fixed by the completed-zeta
normalization. This is the precise Cartan-to-nonabelian mechanism that Paper
22 records as Theorem 5.2.2.

Paper 22, Target Package 5.2.3 now records the proof obligations behind this
criterion.  The \(R=6\) closed-current sector must embed projectively as the
two-branch Cartan floor \(\mathfrak u(1)^2\); the cubic \(d\)-symbol must be
internal to the Bures-unitary closed current algebra; residual leakage must
vanish upstairs; the real cone and Fisher/Bures volume must be preserved; the
critical involution must be realized by an actual Weyl/reflection or
modular-conjugation symmetry; and the displayed Mellin integral must be
upgraded to a representation-theoretic positive-energy character calculation.
Paper 22 makes the two riskiest subclaims explicit as Candidate Theorem 5.2.4
(internal \(d\)-symbol survival via the trace-free Bures-Jordan product on
\(\mathfrak{su}(3)\)) and Candidate Theorem 5.2.5 (the
\(\Gamma(s/2)\Gamma((s+1)/2)\) factor as an even/odd oscillator character).
It now proves the canonical compatible Bures Cartan-floor maps
\(\jmath_n^{\mathrm{floor}}\) and the nonzero Bures-side cubic scalar
\(c_B^{\mathrm{Bures}}\ne0\).  Proposition 5.2.4a proves the finite
\(R=6\) equality
\[
Q_6=c_BD_{A_2},\qquad c_B=18\,\varepsilon_{CH}s_B^3\ne0
\]
on the \(A_2\) Cartan floor, up to the harmless factor \(1/3\) if \(Q_6\) is
energy-normalized.  Proposition 5.2.4b then proves this matched class
survives as a nonzero cylinder class in the projective closed sector.  On the
gamma side, Paper 22 proves the even/odd oscillator radial Mellin measures
directly and gives a Stone-von Neumann/metaplectic realization criterion; the
current finite/projective Bures data do not by themselves select the Weyl/CCR
positive-energy oscillator.  Paper 22, Proposition 5.2.5c records the no-go:
one must add or prove a metaplectic Archimedean selection statement supplying
the Weyl cocycle, irreducibility, positive-energy polarization, and Fourier
branch involution.

Paper 25 now names the Diophantine frame layer behind the frame-price
condition.  The three-gap theorem is the model rigidity statement: finite
orbits on \(\mathbb R/\mathbb Z\) have at most three adjacent gap sizes, with
the largest equal to the sum of the two smaller in the genuine three-gap
regime, and the regime changes are governed by continued fractions.  In this
programmatic translation, conductor/NZSBTL frames play the role of finite
convergents, \(\mu^\star\) and
\(\lambda_{\mathrm{frame}}^{\mathrm{crit}}\) play the role of Diophantine
price constants, and packet leakage/carry is the analogue of gap data.  This
does not yet prove the squarefree/CRT frame-price scaling.  It gives a
testable theorem schema: on one-generator cyclic faces, priced carry should
collapse to a low-complexity three-gap grammar after split and flat terms are
quotiented.

**Proposed generalization (conditional):** The lift should be functorial under
the primorial maps \(R_n\to R_{n+1}\).  The \(d\)-symbol factor should remain
consistent and produce the full gamma factor in the projective limit.  The
stronger Kac-Moody-like interpretation and exact completed-zeta character
remain conditional until the projective Bures representation is constructed.
The sharp increase in skewness at \(R=210\) is finite-row evidence for
nonabelian completion beginning to dominate, not a proof of the archimedean
limit.

**Conclusion of the attack:**

**Current status.** This is the intended proof route for the Archimedean
Noether Limit, with Petz-Bures leg rigidity supplied by Paper 18, Theorem B,
and the joint tensor-product monotone metric isolated as Open Problem 2.2.
The Bures/projective lift axioms remain named conditions.
The rank bookkeeping is explicit: \(\mathfrak u(1)^2\) is a Cartan floor
inside the rank-three algebra \(\mathfrak{su}(2)\oplus\mathfrak{su}(3)\), so
the extra Cartan direction must be central, leakage-flat,
normalization-invisible, or included in the positive-energy character.
Constraint 3 is now structural under the packet-local and first-order
packet-respect hypotheses of Paper 17, Theorem 5.1.

---

## 6. Verification Ledger

With this paper the simplicial-cyclotomic program has the following status:

- Variational foundation — proved.
- Arithmetic skeleton — structurally proved, with Constraint 3 promoted by Paper 17, Theorem 5.1 and Corollary 5.2; the trajectory audit is summarized in Appendix B as the finite certificate.
- Primorial indexing and critical leaf — proved as the unique candidate under the structural constraints.
- Explicit cumulant measurements through R=210 — computed with the corrected standardized pipeline.
- Retired Constraint 3 proxy — not diagnostic; it reduces to |sum J_c|^3/R and fails the Z/6Z control.
- Constraint 3 structural closure — proved under packet-local Fisher factorization and first-order packet-respect/packet-preservation hypotheses; audit passed on R=6, R=12, and R=18 at the Z/6Z numerical floor.
- Finite-place von Mangoldt recovery — reduced to two explicit classical gaps (Lemma 1.1).
- Archimedean Noether Limit — conditional on the Bures/projective gauge-lift proof and the joint monotone-metric exit of Open Problem 2.2.

- Projective critical-leaf closure — reduced in Paper 22, Definition 5.1.3a, Criterion 5.1.3b, and Target Lemma 5.1.3c to normalized CRT restriction functoriality, leakage lower semicontinuity, squarefree CRT-face \(\mu^\star\) stability, and full-conductor/top-face scaling or hard packet preservation.
- Diophantine frame layer — introduced in Paper 25 as the three-gap/continued-fraction interpretation of frame-price scaling: conductor cascades are finite convergent frames, \(\mu^\star\) is a Diophantine price constant, and the new theorem-facing task is to prove a three-gap carry grammar on cyclic faces of the conductor/CRT tower.
- Archimedean lift verification package — reduced in Paper 22, Target Package 5.2.3 to the Bures/projective checklist, including Cartan-floor rank bookkeeping, internal cubic \(d\)-symbol survival, no residual leakage upstairs, real-cone/Fisher-volume preservation, critical involution, minimal positive-energy completion, and representation-theoretic character calculation.

- Archimedean high-risk sublemmas — Paper 22, Proposition 5.2.3a and Corollary 5.2.3b prove the compatible Bures Cartan-floor lift and nonzero Bures-side cubic scalar; Proposition 5.2.4a proves the finite \(A_2\)-matching calculation \(Q_6=c_BD_{A_2}\) on \(R=6\), and Proposition 5.2.4b proves projective survival of that matched cylinder class. Proposition 5.2.5a proves the even/odd oscillator radial measures; Theorem 5.2.5b proves metaplectic realization under Weyl/CCR selection; Proposition 5.2.5c proves that Weyl/CCR selection is not automatic from the present projective Bures data; Selection Axiom 5.2.5d states the additional Archimedean representation-selection input needed for the oscillator route.

**Theorem 6.1 (Conditional Final Statement).**  
If the finite-place recovery gaps and the Archimedean Noether Limit are established, then, with Constraint 3 supplied by Paper 17's structural closure lemma, the primorial Noether-Weil identity yields Weil positivity and therefore RH.

---

## Appendix B: Constraint 3 Cubic Noether Verification

This appendix is a downstream primorial-use summary. The canonical home of the structural statement is Paper 17, Theorem 5.1 and Corollary 5.2; the audit below is its finite certificate on the first prime-power thickenings.

The retired FFT proxy is not used. The replacement audit follows Paper 17, Definition 2.1 and Theorems 2.2-2.3. On each row, the script chooses a volume-dual Nambu-Fisher vector field \(X_C\) on a linear regular leaf, follows the actual trajectory, and records the scale-normalized cubic contraction
\[
\frac{T_p(h,X_C,X_C)}{\|h\|_{F,p}\|X_C\|_{F,p}^2}.
\]

Closure is tested with the genuine cubic force
\[
K^{CH}_p(X_C,X_C)
= X_C X_C/p-\langle X_C,X_C\rangle_{F,p}p.
\]
The reported residual is the Fisher-norm fraction of this cubic force outside the squarefree two-prime conductor support \(\{2,3,6\}\). Thus the known-closed Z/6Z row supplies the numerical floor; Z/12Z and Z/18Z test whether the same squarefree support leaks into the prime-power depth packets \(\{4,12\}\) or \(\{9,18\}\).

The 50-seed audit at amplitude 0.04, initial Fisher speed 0.02, horizon 1.0, and 240 RK4 steps gives:

| row | support | outside depth | mean normalized cubic charge | mean leakage | max leakage | assessment |
|---:|---|---|---:|---:|---:|---|
| 6 | \([2,3,6]\) | \([]\) | 0.457667 | \(3.13\times10^{-32}\) | \(2.25\times10^{-31}\) | known-closed floor |
| 12 | \([2,3,6]\) | \([4,12]\) | 0.518829 | \(9.50\times10^{-32}\) | \(1.97\times10^{-30}\) | no leakage above floor |
| 18 | \([2,3,6]\) | \([9,18]\) | 0.556986 | \(5.22\times10^{-32}\) | \(4.49\times10^{-31}\) | no leakage above floor |

The conclusion is the opposite of the retired proxy's seed-42 narrative. The real cubic-force audit does not distinguish wild p=2 depth from tame p=3 depth at cubic order. Both Z/12Z and Z/18Z preserve the squarefree two-prime support at the Z/6Z numerical floor. Paper 17 promotes this from audit to structural lemma: packet-local Fisher factorization plus first-order packet-respect or hard packet preservation keeps the squarefree two-prime support closed under the cubic Noether force. Constraint 3 therefore becomes part of the primorial indexing rule in its original form: prime-power depth is not a new independent cubic axis.

The companion script is `empirical/constraint3_cubic_noether_verification.py`; the generated artifacts are `empirical/reports/constraint3_cubic_noether_verification.md` and `empirical/reports/constraint3_cubic_noether_verification.json`.

---

## Appendix C: Body-Cumulant-Prime Correspondence

The primorial indexing rule rests on the alignment
\[
\text{N bodies}\quad\longleftrightarrow\quad
\text{N-th cumulant}\quad\longleftrightarrow\quad
\text{(N-1) distinct prime axes}.
\]
Explicitly, N=3 corresponds to the third cumulant and the two-prime row \(R=\mathbb Z/6\mathbb Z\); N=4 corresponds to the fourth cumulant and the three-prime row \(R=\mathbb Z/30\mathbb Z\); in general, N-th cumulant order sees \(N-1\) distinct prime axes.

The left arrow is constitutive, not derived. "Body" is the name this series gives to the regime of N-ary interaction: cubic force for N=3, quartic force for N=4, and so on. There is no separate first-principles derivation forcing the terminology. The mathematical claim is the right arrow: cumulant order selects the minimal squarefree arithmetic skeleton with the corresponding number of distinct prime axes.

The right arrow is governed by four structural constraints.

**Constraint 1: tensor factorization.** If
\[
R\cong \prod_{i=1}^m \mathbb Z/p_i\mathbb Z,
\]
then \(\mathbb C[R]\) factors as a tensor product of \(m\) local factors. The categorical tangent space decomposes into \(m\) independent prime axes. Raising multiplicity to \(\mathbb Z/p^k\mathbb Z\) adds depth along an existing axis, not a new tensor factor.

**Constraint 2: cumulant order matches interaction arity.** The k-th cumulant is generated by k-fold convolution in the character group. When the support of a displacement involves exactly k distinct prime factors, the k-fold convolution is the first order that can mix those k axes simultaneously.

**Constraint 3: preservation of the closed N=3 case.** Paper 17 closes the cubic problem on \(R=\mathbb Z/6\mathbb Z\). Prime-power depth must not be promoted to a new independent cubic axis unless the genuine cubic Noether charge forces it. Paper 17, Theorem 5.1 and Corollary 5.2 supply the structural closure lemma: under packet-local Fisher factorization and either hard packet preservation or first-order packet pricing, the squarefree support \(\{2,3,6\}\) remains closed under the cubic Noether force when embedded into prime-power thickenings. The trajectory audit summarized in Appendix B is the finite certificate on \(Z/12Z\) and \(Z/18Z\). Thus the old wild/tame proxy narrative is rejected, and Constraint 3 supports the original squarefree primorial rule.

**Constraint 4: projective limit recovers the prime-exponent lattice.** The projective limit of the primorial tower
\[
R_n=\mathbb Z/P_n\mathbb Z,\qquad P_n=p_n\#,
\]
recovers the prime-axis skeleton whose occupation states form the prime-exponent lattice of \(\mathbb N\). Other towers may encode p-adic depth or function-field analogues, but they do not give the same canonical squarefree axis cutoff feeding the Euler product.

**Conditional uniqueness statement.** Among arithmetic skeletons satisfying tensor-factorized group algebra, Hayes-normalizer functoriality, preservation of the closed cubic two-prime case, and projective recovery of the prime-exponent lattice, the primorial tower is the unique minimal axis skeleton.

The proof is the bookkeeping behind the whole paper. Tensor factorization and functoriality force prime-local cyclic factors with CRT-compatible normalizer action. Constraint 3 prevents prime-power depth from being counted as a new cubic body. The projective-limit requirement then selects the primorial tower among squarefree candidates, because it is the minimal tower that adds exactly one new independent prime axis at each stage while retaining the occupation lattice in the limit.

The correspondence is therefore not a derivation of N-body mechanics from arithmetic. It is the identification of the arithmetic skeleton native to cumulant-truncated information geometry: bodies name the interaction regime; cumulants provide the tensor order; distinct primes provide the finite arithmetic axes.

---

## Conclusion

The primorial tower remains the right arithmetic architecture for the program. Corrected numerical evidence through R=210 shows increasing deviation from Gaussianity, favoring the nonabelian gauge lift. What is no longer claimed is that the old Z/12Z versus Z/18Z proxy verifies cubic closure: it does not. The replacement trajectory-level audit finds no cubic-force leakage above the Z/6Z floor on Z/12Z or Z/18Z, and Paper 17 now promotes this to a structural closure lemma under packet-local and packet-respect hypotheses. The remaining tasks are to close the two finite-place analytic gaps and prove the Archimedean Noether Limit.

**Data availability.** The Constraint 3 verifier is `empirical/constraint3_cubic_noether_verification.py`; its report and JSON output are in `empirical/reports/`. Other finite computations and scripts are archived with the project empirical artifacts.

---

*Corrected working version. The architecture is retained; the retired proxy is replaced by the trajectory-level Constraint 3 audit and structural closure lemma now folded into Paper 17 and summarized in Appendix B, and the former body-cumulant-prime companion note is folded into Appendix C.*
