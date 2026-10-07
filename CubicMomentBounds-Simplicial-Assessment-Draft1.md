# Cubic Moment Bounds for Dirichlet L-functions at Primorial Moduli — Simplicial Assessment

**Leonardo Murillo Montero (audit by Claude Opus 4.7)**

*First draft — May 26, 2026*

---

> *Tractability assessment for unconditional bounds on $M_3(T, q) := \sum_{\chi^* \bmod q} \int_0^T |L(1/2 + it, \chi)|^3\,dt$ at primorial $q = P_n$ via T27's cubic Helmert–Gauss bilateral. Diagnostic verdict: the simplicial cubic tools align suggestively with the cubic-moment object, but the recent T27 / universal-W probes locate the simplicial cubic content at a different structural address than the L-function content — and the residual structural gap is the same one that obstructs RH itself. **Recommend defer.***

---

## (a) Problem statement

The **third (cubic) moment** of Dirichlet L-functions at modulus $q$ is
$$M_3(T, q) \;:=\; \sum_{\substack{\chi \bmod q \\ \chi \text{ primitive}}}\;\int_0^T \big|L(\tfrac12 + it, \chi)\big|^3 \,dt.$$

At **primorial** $q = P_n = \prod_{i \le n} p_i$, **no unconditional bound is known**. The cubic moment is structurally distinguished from the second and fourth moments because:

1. **Not Plancherel-accessible:** $|L|^3 = |L|^2 \cdot |L|$ is not the modulus of an inner product, so the standard $L^2$ Parseval / large-sieve / approximate-functional-equation chain that handles the second and fourth moments does not apply directly.
2. **Not a Dirichlet polynomial squared:** the fourth moment $|L|^4 = |L^2|^2$ reduces (via the approximate functional equation) to a Dirichlet polynomial squared, so Heath-Brown 1980's mean-value theorem closes it. $|L|^3$ admits no such reduction.
3. **Genuine 3rd-cumulant content:** $|L|^3$ probes the third absolute moment of values of $L$ on the critical line — the Fisher-level statistic of a single L-function over a height window. By GUE conjecture, the moments should follow the random-matrix-theory predictions of Keating-Snaith 2000:
   $$M_k(T) \;\sim\; g_k \,a_k\, T (\log T)^{k^2},$$
   so $M_3$ should be of order $q\, T (\log qT)^9 \cdot \varphi(q)^{-2}$ (after primitive-character normalisation). No proof of the exact moment asymptotic at $k=3$ is known for $\zeta$, let alone for families of Dirichlet L-functions at primorial moduli.

The simplicial program's relevance: the cubic Weil moment $\mathcal{C}_\zeta(g; \eta)$ of *ocho* §2 is structurally a third-cumulant object on $\zeta$-zeros; the cubic A–C tensor of *siete* §5 is the third-order tensor of log-zeta residues; T27 builds the cubic Helmert–Gauss bilateral at $m=3$. These are the program's natural cubic tools.

---

## (b) Classical status

| Moment | Modulus regime | Status |
|---|---|---|
| $M_2(T, q)$ | All $q$ | **Solved** (Plancherel + zero-density). $M_2(T, q) \sim qT \log(qT)/\varphi(q)$ uniformly. |
| $M_4(T, q)$ | $q$ prime | **Heath-Brown 1980**. $M_4(T, q) \ll qT(\log qT)^4$ unconditionally. |
| $M_4(T, q)$ | $q$ primorial / composite | **Conrey–Iwaniec; Soundararajan–Young 2010+**. Bounds in many cases, sharp asymptotic in fewer. |
| $M_3(T, q)$ | $q = 1$ ($\zeta$) | **Ingham 1926** for $M_3$ with extra log factor; sharp asymptotic still **open**. |
| $M_3(T, q)$ | $q$ prime | Conditional bounds via subconvexity; sharp asymptotic **open**. |
| $M_3(T, q)$ | $q$ primorial | **Open**, with no specific structural obstacle beyond the general cubic difficulty. |

The closest classical anchor for $M_3$ is the **shifted cubic moment**
$$\int_0^T |L(\tfrac12 + it + \alpha, \chi)|^2 \, L(\tfrac12 + it + \beta, \chi)\,dt,$$
which is bilinear (one factor and its modulus squared) and amenable to large-sieve techniques. Heath-Brown's 12th-moment bound for $\zeta$ + Hölder gives convexity-style upper bounds on $M_3$ but never the sharp $(\log T)^9$ rate. **Conditional on GRH**, sharp bounds follow from the Soundararajan–Harper machinery (Soundararajan 2009; Harper 2013).

What classical methods **do not** provide:
- Any algebraic identity for $M_3$ analogous to Parseval for $M_2$.
- Any approximate-functional-equation reduction analogous to the AFE for $M_4$.
- Any "natural basis" in which the cubic moment factorises or telescopes.

---

## (c) Simplicial alignment

The simplicial program's cubic-order objects, surveyed for relevance to $M_3$:

**Cubic Weil moment $\mathcal{C}_\zeta(g; \eta)$ (*ocho* §2).** Defined as
$$\mathcal{C}_\zeta(g; \eta) := \sum_{\rho_1, \rho_2, \rho_3} \widetilde g(\rho_1)\widetilde g(\rho_2)\widetilde g(\rho_3)\,K_3(\rho_1, \rho_2, \rho_3),$$
$K_3$ the cubic surface kernel supported near $\rho_1 + \rho_2 + \rho_3 = 3/2$. Under RH this equals $\int \mathcal{S}_g(x)^3 \eta(x)\,dx$ where $\mathcal{S}_g$ is the zero-spectrum Fourier sum. **This is not the third moment of $|L|$ on the critical line; it is the third cumulant of zeros of a single L-function**, and lives on the zero spectrum, not on the value spectrum. Different object.

**Cubic A–C tensor (*siete* §5).** $T^\zeta(\chi_a, \chi_b, \chi_c; s, N) = \widehat Q^{(N)}_{a+b+c} - \sum_{\text{pairs}} \widehat Q_{a+b} \widehat Q_c + 2 \widehat Q_a \widehat Q_b \widehat Q_c$, the third-cumulant tensor of log $\zeta$ over $\mathbb{Z}/N$ residues. Lives at fixed $s$ as a finite-N tensor; **not directly a moment of $|L|$**.

**T27 cubic bilateral factorization.** $U^{(3)} W^{(3)} = D^{\mathrm{rad},3} V^{\mathrm{Gauss},3}$ over the cubic Kummer base $\mathbb{Z}[\zeta_3]/\mathfrak{m}$, with Hecke characters of $\mathbb{Z}[\zeta_3]$ replacing Dirichlet characters of $\mathbb{Z}$. **At face value, T27 is about Hecke L-functions of $\mathbb{Q}(\zeta_3)$, not about Dirichlet L-functions of $\mathbb{Z}$.** Via $\zeta_{\mathbb{Q}(\zeta_3)}(s) = \zeta(s) L(s, \chi_3)$, the Dedekind-factored case gives a 2-dimensional Dirichlet block — the cubic-quadratic character $\chi_3$ — but the rest of $W^{(3)}$ is genuinely Hecke content.

**Cubic Fejér class $\mathcal{G}^{(3)}$ + cubic-shift bypass.** The path *ocho* / *diez* set up was: cubic positivity $\equiv$ RH, with [A3'] (primorial-indexed BV at rate $1 - C^*/n$) as the unconditional residual. The cubic-shift moment object is the third cumulant of the **explicit formula**, not the third moment of $|L|$ values.

**Net alignment.** The simplicial program has well-developed cubic-order tools, but **all of them live on the zero side or the explicit-formula side**, not on the $|L|$-value side. The cubic moment $M_3(T, q)$ is a value-spectrum object. The two sides are connected by the explicit formula but they are not the same object.

This is the first honest gap to note: **the simplicial program's "cubic" content is not aimed at $M_3(T, q)$**. It is aimed at the cubic Weil-positivity criterion. These are related (both at cubic order) but they are different theorems.

---

## (d) Tractability — does T27's near-scalar $G^{(3)}$ help?

The recent T27 probe (`probe_T27_output.txt`) found that the cubic Gram operator $G^{(3)} = U^{(3)*}U^{(3)}$ at $N=30$ has spectrum tightly clustered in $[3.21, 4.02]$ with condition number $\kappa \approx 1.25$. That is, $G^{(3)}$ is **nearly a scalar multiple of the identity** ($G^{(3)} \approx 3.4\,I$, with 6% multiplicative spread).

T27 §7.1 had hoped that the *non-trivial* Gram structure of $G^{(3)}$ would supply analytic content beyond the $m=2$ case (where $G^{(2)} = I$ gave exact Parseval, with no new analytic content per T9.4.1 §5.3). The probe answers this hope: **the Gram is technically not the identity, but it is so close to scalar that the cubic Parseval-with-scalar form is, structurally, the same as the $m=2$ Parseval up to a constant.**

Concretely, the cubic identity (T27 Theorem D) is
$$\vec a^* W^{(3)*} G^{(3)} W^{(3)} \vec a \;=\; \sum_{k=1}^{N-1} \frac{|(\,V^{\mathrm{Gauss},3} \vec a)_k|^2}{(Nk(1+k^2))^{2/3}}.$$

With $G^{(3)} \approx \bar\lambda \, I + E$ where $\bar\lambda \approx 3.4$ and $\|E\|/\bar\lambda \approx 6\%$:
$$\vec a^* W^{(3)*} G^{(3)} W^{(3)} \vec a \;=\; \bar\lambda\,\varphi_3(\mathfrak{m})\|\vec a\|^2 \;+\; O(0.06 \bar\lambda \varphi_3(\mathfrak m)\|\vec a\|^2).$$

So the cubic bilateral identity reads
$$(1 \pm 0.06) \cdot \bar\lambda\,\varphi_3(\mathfrak m)\,\|\vec a\|^2 \;=\; \sum_k (R_k^{(3)})^2 \big|(V^{\mathrm{Gauss},3} \vec a)_k\big|^2.$$

**This is a Parseval-with-scalar identity, structurally identical to the $m=2$ case.** The "cubic-Galois richness" hope of T27 (the eigenstructure of $W^{(3)*} G^{(3)} W^{(3)}$ encoding new analytic content) is **largely empty**: the eigenstructure is "approximately $\bar\lambda$ times the identity" with a 6% perturbation that is *not the cubic-Galois content of $K_N^{(3)}$* but rather the residual non-orthogonality of $L^3$-normalized vectors in $L^2$.

**Consequence for $M_3$:** even if one wanted to push the cubic bilateral onto $M_3(T, q)$ via some analog of the T9.4.1 BV-variance identity, the bilateral identity is fundamentally an $L^2$ (Parseval-style) identity over Hecke characters. It cannot accommodate $|L|^3$ which is not a squared norm. **The bilateral output is intrinsically $L^2$.**

What the bilateral CAN do for $M_3$:
1. **Bound $M_3$ via Hölder** $M_3 \le M_2^{1/2} M_4^{1/2}$ (Cauchy-Schwarz on the integrand). The bilateral controls $M_2$; classical methods control $M_4$. Combined: $M_3 \ll \sqrt{M_2 \cdot M_4}$. This is the **convexity** bound, not better than classical Hölder.
2. **Reorganise the second-moment part** of $M_3 = \int |L|^2 \cdot |L|\,dt$ via the bilateral, then push a pointwise bound for $|L|$ through. But the pointwise bound for $|L|$ on the critical line is the **subconvexity problem**, itself open at primorial $q$ at the required Burgess strength.

Numerical sanity check (this worktree's `probe_cubic_moment_simplicial.py`):
- $q = 6$, $T = 30$: $M_2 = 96.86$, $M_3 = 153.08$, $M_4 = 266.29$.
  Cauchy–Schwarz $\sqrt{M_2 M_4} = 160.60$, only **4.9% larger** than $M_3$.
- $q = 30$, $T = 30$: $M_2 = 431.60$, $M_3 = 727.12$, $M_4 = 1342.51$.
  $\sqrt{M_2 M_4} = 761.20$, only **4.7% larger** than $M_3$.

**Cauchy–Schwarz is essentially tight on $M_3$** at small primorial scales. The simplicial bilateral's contribution to $M_3$ via $M_2$-bounds plus C–S would reproduce the classical convexity rate up to constants, with no new content.

(These are sums over **all** characters mod $q$, including non-primitive — there are no primitive characters mod 6 or mod 30 in the strict sense, because each prime $p \le n$ in the primorial contributes only $\varphi(p) = p-1$ characters, all of conductor $p$, never of conductor $P_n$. This is a feature of primorial $q$ that classical $M_3$ asymptotics handle by working with `chi^*` the unique primitive character inducing $\chi$.)

---

## (e) Concrete sub-target

Given the structural analysis, what could the simplicial framework still attempt? Three honest sub-targets, in increasing order of ambition and decreasing order of plausibility:

### (e.1) **Modest target: convexity-rate $M_3$ at primorial via bilateral $M_2$ + Heath-Brown $M_4$.**

**Theorem-candidate.** *For primorial $q = P_n$ and $T \ge q$:*
$$M_3(T, P_n) \;\ll\; q\, T \,(\log qT)^{5/2} \cdot \frac{\varphi(q)^{1/2}}{q^{1/2}},$$
*via Hölder + classical $M_2$ + Heath-Brown $M_4$.*

This is **achievable** and within reach of a paper-scale write-up, but it is **not new** — it follows by Hölder from known $M_2$ and $M_4$ bounds. The simplicial bilateral contributes only the *reorganization* of $M_2$ via the Helmert basis, which (per the T9.4.1 audit and the recent G^{(3)} ≈ scalar finding) is a Parseval-equivalent reorganization. **No structural advance**.

### (e.2) **Aspirational target: log-power-saving $M_3$ via cubic Helmert telescoping.**

The classical conjectural asymptotic is $M_3 \sim c\, q T (\log qT)^9 \varphi(q)^{-2}$. The convexity rate above is $(\log qT)^{5/2}$. The gap is $(\log qT)^{6.5}$.

**Question:** does the cubic-Helmert-axis decomposition give telescoping cancellation across rungs $k = 1, \ldots, N-1$ that saves log-powers in $M_3$?

For $M_2$, T9.4.1 §5.3 showed: cross-rung orthogonality collapses to Parseval. **No telescoping**. For $M_3$ structurally similar: the cubic bilateral lives in $L^2$, not in $L^3$ or any direct cubic norm. A cubic-Hölder Plancherel does not exist as an algebraic identity.

**Verdict on (e.2):** *not tractable* by direct extension of the bilateral. Would require a genuinely new structural tool (e.g., a triple-Helmert kernel with three independent axis-indices satisfying a triple-Parseval identity — no such object is known in any literature, and the simplicial program does not construct one).

### (e.3) **Speculative target: shifted cubic moment via universal-W cross-projection.**

The universal-W probe (`probe_universal_W_output.txt`) finds that $W$'s eigenbasis has DFT-like spectrum and that the von Mangoldt vector $\mathrm{vec}(\Lambda)$ decomposes cleanly in the W-eigenbasis (largest coefficient 18.5 at $\arg/\pi = -0.764$).

**Question:** if one expresses the shifted moment $\int |L(\frac12 + it + \alpha, \chi)|^2 L(\frac12 + it + \beta, \chi)\,dt$ via its Dirichlet-series approximation $\sum (n)\,n^{-1/2-it}$, can the universal-W eigenbasis diagonalize the resulting tensor (a 3-index object with multiplicative structure)?

This is **technically open**, but the answer is informed by the *cross-projection structure* of the W eigenbasis: $\mathrm{vec}(\Lambda)$ has 10 dominant components in the W basis, spread across eigenvalues with arguments $\{-0.99, -0.76, -0.52, -0.48, -0.02, +0.48, +0.49, +0.52, +0.98\}\pi$. The dominant component at $\arg/\pi = -0.764$ is the **outlier eigenvalue** — not at any natural root of unity. This outlier is the dominant $\zeta$-content of $W$. Whether the shifted cubic moment lives on cross-projections involving this outlier is **not known**.

**Verdict on (e.3):** would need a dedicated probe to test if shifted-cubic-moment Dirichlet polynomials project cleanly onto the W-eigenbasis. Even if they do, translating that into an unconditional cubic moment bound requires further structural input that is currently absent. **Long-shot, but worth a 30-min focused probe.**

---

## (f) Recommendation

### Verdict: defer.

The simplicial cubic tools (T27, *ocho*, *siete*) align with cubic-order objects in analytic NT — but **not** with $M_3(T, q)$ as a value-spectrum statistic. The cubic Weil moment of *ocho* is a third-cumulant on zeros, not on values. The cubic A–C tensor of *siete* is a third-cumulant on log-zeta residues, not on $|L|$ moments. The T27 bilateral is intrinsically $L^2$ over Hecke characters of $\mathbb{Z}[\zeta_3]$, not Dirichlet characters of $\mathbb{Z}$.

The recent diagnostic probes sharpen this further:
1. **$G^{(3)}$ near-scalar:** the bilateral's "cubic-Galois richness" hope was largely empty. The bilateral identity at $m=3$ is Parseval-with-scalar, structurally the same as $m=2$.
2. **Universal W:** the L-function content lives at *cross-projections* of $\mathrm{vec}(\Lambda)$ onto W-eigenvectors, with a single dominant outlier eigenvector at $\arg/\pi \approx -0.764$. This is a specific computational handle, but it is not the natural object for $M_3$ either.
3. **Cauchy-Schwarz is tight on $M_3$:** numerical probe shows $\sqrt{M_2 M_4} / M_3 \approx 1.05$ at small primorial. Any bound on $M_3$ via $M_2 \cdot M_4$ + Hölder reproduces the classical convexity rate; the simplicial bilateral does not improve over Hölder.

### What the simplicial program SHOULD pursue (in order of structural fit):

1. **[A3'] residual at the cubic Kummer base (T27 §8 path).** This is the program's *natural* cubic target — primorial-indexed Bombieri-Vinogradov rate for Hecke L-functions of $\mathbb{Q}(\zeta_3)$, which closes the cubic positivity criterion via *ocho* / *diez*. Same level of difficulty as classical [A3'] (Polymath-8-scale analytic NT), but at the cubic Kummer base where the program's tools (cubic bilateral, $L^3$-Helmert) are designed to live. **This is the right cubic target. $M_3(T, q)$ is not.**

2. **Universal-W probe of the von Mangoldt cross-projection structure.** The dominant eigenvector at $\arg/\pi = -0.764$ is the "$\zeta$-axis" of the W spectrum, and identifying its $L^2$ projection onto $\mathrm{vec}(\Lambda)$ exactly may yield structural identities for $L'/L$ or related zeta-density objects. This is forward-door work (not aimed at RH-closure) but it is the natural next probe of the universal-W finding. **Recommend as a 1-2 day focused exploration.**

3. **Avoid $M_3(T, q)$.** It is a hard analytic-NT problem in its own right, but the simplicial framework does not provide distinctive tools for it. Pushing on $M_3$ via the bilateral would reproduce convexity rates already accessible via classical Hölder + Heath-Brown. The opportunity cost (months of work for no structural advance) is not justified.

### Concrete next probe (if the director wants to test (e.3)):

`probe_shifted_cubic_W_projection.py` — at $N = 30$, compute the Dirichlet-polynomial approximation to $\sum_\chi \int |L(1/2+it+\alpha, \chi)|^2 L(1/2+it+\beta, \chi)\,dt$ and project the resulting 3-index tensor (in the $(\alpha, \beta, t)$ slice) onto the universal-W eigenbasis. If the projection concentrates on a single W-eigenvector (analogously to $\mathrm{vec}(\Lambda)$'s 60% concentration at $\arg/\pi = -0.764$), there is a candidate structural identity worth pursuing. If the projection is spread, the shifted cubic moment is not naturally W-diagonal and (e.3) closes negatively. **30-60 min compute, decisive test.**

---

## Summary table

| Question | Verdict |
|---|---|
| Natural simplicial form of $M_3(T, P_n)$? | None — $M_3$ is a value-spectrum statistic; simplicial cubic tools live on zero-side and explicit-formula side. |
| Does $M_3$ factor through T27's cubic bilateral? | No — T27 is intrinsically $L^2$ over Hecke characters; $M_3$ is not an $L^2$ inner product. |
| Given $G^{(3)}$ near-scalar, what does the cubic bilateral say about $M_3$? | Parseval-with-scalar, same content as $m=2$. No new analytic content for cubic moments. |
| Can universal-W's DFT-like spectrum be exploited for $M_3$? | Speculative — would need shifted-cubic-moment cross-projection probe (item (e.3)). Long-shot but cheap to test. |
| Is the natural simplicial output $M_3 \ll q T \log^A$ with explicit $A$? | $A = 5/2$ via Hölder + Heath-Brown $M_4$, but this is the classical convexity bound; no advance. |
| Recommend pursuit? | **No** — defer to [A3'] at the cubic Kummer base (T27 §8), which is the program's natural cubic target. |

---

## Concrete probe data appendix (this assessment)

**`probe_cubic_moment_simplicial.py` output, $T = 30$, summed over all chars mod $q$:**

```
q=6:     M_2 =  96.86,  M_3 = 153.08,  M_4 = 266.29
         sqrt(M_2 M_4) = 160.60   M_3 / sqrt(M_2 M_4) = 0.953

q=30:    M_2 = 431.60,  M_3 = 727.12,  M_4 = 1342.51
         sqrt(M_2 M_4) = 761.20   M_3 / sqrt(M_2 M_4) = 0.955
```

Cauchy-Schwarz $M_3^2 \le M_2 M_4$ is tight to 4.7% at both moduli, consistent with the heuristic that the cubic moment is dominated by the "typical-value" diagonal where $|L|$ is concentrated near $\sqrt{\log T}$ — which is exactly the Hölder-equality regime.

The Helmert-Kloosterman prime sum $\Pi_k(X; N)$ structure of T9.4.1 enters the second-moment factorization $M_2$ but does not extend to $M_3$ algebraically. The bilateral identity is fundamentally $L^2$.

---

## References (program-internal)

- T9.4 — `T9.4-GaussSumDecompositionConductorBlocks-Draft1.md`.
- T9.4.1 — `T9.4.1-BV-Variance-Helmert-Identity-Draft1.md`. Audit conclusion: $m=2$ bilateral reduces to Parseval on units.
- T27 — `T27-CubicBilateralFactorization-Draft1.md`. Cubic Kummer bilateral; G^{(3)} ≠ I structurally but probe finds ≈ scalar.
- *ocho* — cubic Weil positivity criterion (zero-side third cumulant, not value-side).
- *siete* — cubic A–C tensor of log-zeta.
- *diez* — [A1'], [A2'] closures + [A3'] outline.
- `probe_T27_output.txt` — G^{(3)} eigenstructure, $\kappa = 1.25$ at $N=30$.
- `probe_universal_W_output.txt` — W ≈ DFT-like, vec(Lambda) dominant at $\arg/\pi = -0.764$.
- `probe_cubic_moment_simplicial.py` — this assessment's M_3 sanity data.

## References (classical)

- Heath-Brown, D. R. (1980). The fourth power moment of the Riemann zeta function. *Proc. London Math. Soc.* (3) 38, 385–422.
- Ingham, A. E. (1926). Mean-value theorems in the theory of the Riemann zeta function. *Proc. London Math. Soc.* (2) 27, 273–300.
- Keating, J. P. and Snaith, N. C. (2000). Random matrix theory and L-functions at $s = 1/2$. *Comm. Math. Phys.* 214, 91–110.
- Soundararajan, K. (2009). Moments of the Riemann zeta function. *Ann. of Math.* (2) 170, 981–993.
- Harper, A. J. (2013). Sharp conditional bounds for moments of the Riemann zeta function. arXiv:1305.4618.
- Conrey, J. B. and Iwaniec, H. (2000). The cubic moment of central values of automorphic L-functions. *Ann. of Math.* (2) 151, 1175–1216.
- Watt, N. (1995). A note on the mean fourth power of Dirichlet L-functions. *Acta Arithmetica* 71, 387–404.
- Young, M. P. (2011). The fourth moment of Dirichlet L-functions. *Ann. of Math.* (2) 173, 1–50.

---

*The director's instinct that the simplicial cubic tools should align with the cubic moment problem was structurally reasonable; the recent T27 + universal-W probes refine that picture. The cubic tools align with cubic-order objects, but $M_3(T, q)$ is the wrong cubic-order object — it is on the value spectrum, while the simplicial cubic content is on the zero spectrum / explicit formula. The natural cubic target remains [A3'] at the cubic Kummer base.*

— Director-audit dialogue, May 26, 2026
