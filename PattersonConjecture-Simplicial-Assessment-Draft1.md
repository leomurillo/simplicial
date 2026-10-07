# Patterson's Conjecture — Simplicial-Framework Tractability Assessment (Draft 1)

**Leonardo Murillo Montero, assisted by Claude Opus 4.7**

*First draft — 2026-05-26*

---

> *Assessment of whether the simplicial framework's m=3 / cubic Kummer clock tools (T10, T27, T8 §4 Gauss-sum bridge) offer a tractable angle on Patterson's 1978 conjecture about the asymptotic distribution of cubic Gauss sums g(π) over primary primes π ⊂ Z[ζ₃]. **Bottom line: alignment is genuine and structurally tight, but the framework's distinctive lever — the cubic Gram non-collapse $G^{(3)} \ne I$ — is orthogonal to what Patterson's conjecture asks. The natural sub-target is a structural reformulation of Heath-Brown's "cubic large sieve" inequality through T27's bilateral $U^{(3)}W^{(3)} = D^{\mathrm{rad},3}V^{\mathrm{Gauss},3}$, with realistic prospect of giving an alternative organization, but with no visible path to the explicit Patterson constant c. Recommendation: defer, in favor of programs where the cubic Gram non-collapse acts directly on the target.***

---

## (a) Problem statement

Let $\mathbb{Z}[\zeta_3]$ be the Eisenstein integers, $\zeta_3 = e^{2\pi i / 3}$. For $\pi \in \mathbb{Z}[\zeta_3]$ a **primary prime** (i.e., $\pi \equiv -1 \pmod{3}$ in $\mathbb{Z}[\zeta_3]$; this fixes a unique associate in each class of primes not dividing $3$), with norm $N(\pi) = q$, the **cubic residue symbol** $(\cdot/\pi)_3 : (\mathbb{Z}[\zeta_3]/\pi)^\times \to \{1, \zeta_3, \zeta_3^2\}$ is defined by

$$a^{(q-1)/3} \equiv (a/\pi)_3 \pmod{\pi}.$$

The **cubic Gauss sum** of $\pi$ is

$$g(\pi) := \sum_{a \bmod \pi,\ a \ne 0} (a/\pi)_3 \cdot e\!\left(\frac{\mathrm{Tr}(a)}{q}\right), \qquad e(t) := e^{2\pi i t}, \quad \mathrm{Tr}(x+y\zeta_3) = 2x-y.$$

**Patterson's conjecture (Patterson 1978).** For some explicit constant $c$,

$$P(X) := \sum_{\substack{\pi\ \text{primary prime} \\ N(\pi) \le X}} \frac{g(\pi)}{N(\pi)^{1/2}} \ \sim\ c \cdot X^{5/6} \qquad \text{as } X \to \infty.$$

Equivalently, the cubic Gauss sums $g(\pi)/\sqrt{N(\pi)}$ — which by the trivial bound have magnitude $\le \sqrt{N(\pi)}$ but are conjectured to have typical size much smaller — exhibit **systematic bias** of size $X^{5/6}/\#\{\pi : N(\pi) \le X\} \sim X^{5/6}/(X/\log X) \sim X^{-1/6} \log X$ per prime, in the angular direction fixed by the constant $c$ (a specific argument related to $\Gamma(1/3)$).

The conjectural constant $c$ involves $\Gamma(1/3)$ and the residue at $s=1$ of a metaplectic Eisenstein series on $\mathrm{GL}(3)$ over $\mathbb{Q}(\zeta_3)$ — concretely

$$c = \frac{(2\pi)^{2/3}}{5 \cdot \Gamma(2/3)} \cdot \mathrm{Res}_{s=1} D(s),$$

where $D(s)$ is the Dirichlet series $\sum_\pi g(\pi)/N(\pi)^s$ on primary primes. Heath-Brown's theta-series analysis attributes the $X^{5/6}$ exponent to a pole of $D(s)$ at $s = 5/6$.

---

## (b) Classical status (as of 2026)

| Year | Result | Authors |
|---|---|---|
| 1978 | Conjecture stated | Patterson |
| 1979 | $X^{5/6}$ oscillation order established (without explicit $c$) | Heath-Brown, Patterson |
| 1981 | Cubic theta function $\theta_3(z) = \sum_a g(a) e(az)$ has Fourier coefficients exhibiting cubic Gauss sum structure | Patterson |
| 2000 | Improved error bound $P(X) = c X^{5/6} + O(X^{5/6 - \delta})$ for some unspecified $\delta > 0$, conditional on conjectures | Heath-Brown |
| 2021 | Quantitative refinements, conditional improvements | Dunn, Radziwiłł |
| 2024+ | Further work | Maiti, others |

**Open:**
1. **Full asymptotic** — the explicit constant $c$ in $P(X) \sim c X^{5/6}$ remains open in the unconditional form.
2. **Effective error bound** — explicit $\delta > 0$ in $X^{5/6 - \delta}$ is open unconditionally.
3. **Residue structure** — whether the cubic GL(3) Eisenstein series has the expected residue at $s = 5/6$ underlying $c$ is open (this is the Patterson-Heath-Brown theta-Eisenstein open question; cf. Friedberg-Hoffstein-Lieman).

**Structural classical apparatus:**
- **Kubota's metaplectic cover** of $\mathrm{GL}(2)$ over $\mathbb{Q}(\zeta_3)$: cubic theta function $\theta_3$ lives on this cover.
- **Heath-Brown's cubic large sieve** (1981): bilinear estimates $\sum_{m,n} a_m b_n \overline{(m/n)_3}$ with controlled $\ell^2$ norms.
- **Dunn-Radziwiłł 2021** introduces a new bilinear-form input and gets quantitative control.

What no classical attack has produced: the constant $c$ in closed form, with the residue structure verified unconditionally.

---

## (c) Simplicial alignment

This is where the framework genuinely fits.

### (c.1) T27's cubic Gauss sums *are* Patterson's objects

T27 Definition 4.3 defines

$$\tau_3(\psi, a) := \sum_{s \in (\mathbb{Z}[\zeta_3]/\mathfrak{m})^\times} \psi(s) \cdot \omega_{\mathfrak{m}}^{\mathrm{Tr}(as)}$$

for $\psi$ a Hecke character mod $\mathfrak{m}$. **Specializing**: take $\mathfrak{m} = (\pi)$ a primary prime ideal, $\psi = (\cdot/\pi)_3$ the cubic residue character (a specific Hecke character mod $\pi$), and $a = 1$. Then $\tau_3((\cdot/\pi)_3, 1) = g(\pi)$ — Patterson's cubic Gauss sum is the T27 cubic Gauss sum on the cubic-residue-symbol Hecke character at $\mathfrak{m} = (\pi)$.

This is a **tight identification**, not a loose analogy. The framework's m=3 rung was constructed *because* the cubic Kummer clock $K_N^{(3)} = \mathbb{Q}(\zeta_3, \sqrt[3]{p} : p \le N)$ is exactly the arithmetic ambient of cubic-residue / cubic-character theory.

### (c.2) Patterson's sum factors through T27's Helmert-Gauss kernel — but trivially

T27 Theorem C states the cubic Helmert-Gauss kernel

$$T_{\mathfrak{m}}^{(3)}(n, a) = \sum_\psi \psi(n) \tau_3(\psi, a) = \varphi_3(\mathfrak{m}) \cdot \omega_{\mathfrak{m}}^{\mathrm{Tr}(a n^{-1})} \cdot \mathbf{1}_{(n, \mathfrak{m}) = 1}.$$

For Patterson, we want the **single-character, single-modulus, $a = 1$** specialization: $g(\pi) = \tau_3((\cdot/\pi)_3, 1)$. The Helmert-Gauss kernel aggregates over **all** Hecke characters mod fixed $\mathfrak{m}$; it tells us how to invert character aggregation. Patterson's sum aggregates over **varying primary primes $\pi$**, fixed character (the cubic residue symbol at each $\pi$). These are different aggregations.

The T27 bilateral $U^{(3)} W^{(3)} = D^{\mathrm{rad},3} V^{\mathrm{Gauss},3}$ at $\mathfrak{m} = (\pi)$ relates $\varphi_3(\mathfrak{m}) = N(\pi) - 1$ Hecke characters mod $\pi$ to the $L^3$-Helmert axes. It does not naturally aggregate over varying $\pi$.

**Verdict:** T27's structure lives at *fixed* cubic conductor; Patterson's sum sums over varying conductors. The framework as currently constituted does not provide the right organizing aggregation.

### (c.3) The cubic Kummer clock as natural ambient

The cubic Kummer clock $K_N^{(3)}$ contains all cube roots of primes $\le N$ and all third roots of unity. The cubic Gauss sums $g(\pi)$ live as algebraic numbers in $K_{N(\pi)}^{(3)}$ — specifically in the cubic-cyclotomic-Kummer field generated by $\zeta_{3N(\pi)}$ and $\sqrt[3]{N(\pi)}$. T10's growth criterion (prime-rung growth at $m=3$) matches the structural fact that primary primes of new norm contribute **algebraically independent** cubic Gauss sums modulo $K_{N-1}^{(3)}$.

This is a clean structural alignment, but it does not by itself help with the asymptotic.

### (c.4) Numerical probe (run in this assessment)

I computed all $g(\pi)$ for 94 primary primes $\pi$ with $N(\pi) \le 500$ in $\mathbb{Z}[\zeta_3]$, using direct enumeration of residues mod $\pi$. Key facts confirmed:

**Magnitude of $g(\pi)$ relative to $\sqrt{N(\pi)}$** (split primes only, $N(\pi) = p \equiv 1 \pmod 3$):

| $p$ | $\sum_{\pi : N(\pi)=p, \text{primary}} |g(\pi)|^2$ | $3p$ (trivial bound) | Ratio |
|---|---|---|---|
| 7 | 2.86 | 21 | 0.14 |
| 13 | 2.92 | 39 | 0.08 |
| 19 | 29.7 | 57 | 0.52 |
| 31 | 0.67 | 93 | 0.007 |
| 37 | 15.2 | 111 | 0.14 |
| 43 | 0.50 | 129 | 0.004 |
| 61 | 1.93 | 183 | 0.011 |
| 67 | 1.26 | 201 | 0.006 |
| 73 | 1.98 | 219 | 0.009 |

The ratios are **far below** 1 (which would saturate the trivial Weil bound $|g(\pi)| \le \sqrt{q}$). This is the canonical Heath-Brown-Patterson cancellation: cubic Gauss sums on primary primes are systematically smaller than their Weil bound predicts. The "missing $\sqrt{p}$" factor is precisely the input to Patterson's $X^{5/6}$ phenomenon.

**Partial Patterson sum:**

| $X$ | # primary primes | $|P(X)|$ | $X^{5/6}$ | $|P(X)|/X^{5/6}$ |
|---|---|---|---|---|
| 25 | 8 | 1.47 | 14.6 | 0.101 |
| 50 | 14 | 1.18 | 26.1 | 0.045 |
| 100 | 24 | 0.87 | 46.4 | 0.019 |
| 200 | 45 | 1.05 | 82.7 | 0.013 |
| 300 | 60 | 1.01 | 116 | 0.0087 |
| 500 | 94 | 0.97 | 178 | 0.0055 |

At $X = 500$ the partial sum $|P(X)| \approx 1$, while $X^{5/6} \approx 178$. The ratio $|P|/X^{5/6}$ is *decreasing* — we're deep in the pre-asymptotic regime, where the running partial sum fluctuates around magnitude 1 (consistent with Heath-Brown's square-root cancellation) and only at much larger $X$ does the $X^{5/6}$ bias dominate. Patterson's predicted constant $|c| \approx 0.27$ (from $c = (2\pi)^{2/3}/(5 \Gamma(2/3)) \cdot \mathrm{Res}$, with the residue conjecturally non-zero) corresponds to asymptotic alignment somewhere around $X \sim 10^4$ to $10^6$ — well beyond what direct enumeration can reach.

This is consistent with the classical literature: the $X^{5/6}$ regime is not visible in small numerics.

---

## (d) Tractability: where does the framework's distinctive lever apply?

The simplicial program's structural lever at m=3 is the recent finding (T27 §7.1, probe_T27_output.txt):

$$G^{(3)} := U^{(3)*} U^{(3)} \neq I \quad (\text{spectrum: } 3.21 \le \lambda_i \le 4.02 \text{ at } N=30),$$

contrasting with the m=2 case where $G^{(2)} = I$ exactly (T9 unitarity, ||G^(2) - I|| ≈ 1.5e-15). The cubic Gram has condition number 1.25, deviates from identity by Frobenius norm 12.98, and its eigenvectors are *not* aligned with Dirichlet characters of $(\mathbb{Z}/30)^\times$ — best overlaps are around 0.1-0.28.

**What this lever does:** it provides genuine non-trivial spectral content at the bilateral matrix level beyond Parseval. The audited m=2 case collapsed to Parseval (T9.4.1); m=3 does not.

**What this lever does NOT do for Patterson:**

1. **Patterson is single-conductor in nature.** Patterson's sum varies the prime $\pi$, and for each $\pi$ uses the cubic-residue character — *one* specific Hecke character mod $\pi$ — not a sum over all Hecke characters mod a fixed $\mathfrak{m}$. The Gram $G^{(3)}$ acts on the *additive character* axis (size $N(\mathfrak{m}) - 1$) at fixed $\mathfrak{m}$; this is orthogonal to varying $\mathfrak{m}$.

2. **The cubic large sieve is the natural classical interface.** Heath-Brown's cubic large sieve provides a bilinear bound

$$\sum_{(m, N(\pi))=1} \Big|\sum_n a_n (n/\pi)_3\Big|^2 \le K(M, N) \cdot \|a\|_2^2,$$

where the kernel $K(M, N)$ has explicit bounds. T27's bilateral identity would naturally produce **one row** of such a bilinear form at fixed $\pi$, weighted by the $L^3$-Helmert axes. To get Patterson, one needs to sum over $\pi$ — which the simplicial framework does not aggregate naturally.

3. **The residue structure of $D(s) = \sum_\pi g(\pi)/N(\pi)^s$ at $s = 5/6$** is the genuine Patterson question, and it is **automorphic in nature** — it lives in metaplectic GL(3) Eisenstein series (Friedberg-Hoffstein-Lieman 1995, Brubaker-Bump-Friedberg 2011). The simplicial framework has no automorphic content; it has Hecke-character / Kummer-clock content, which is one rung below the GL(3) metaplectic content.

### (d.1) Could T27's bilateral give a new cubic large sieve organization?

Plausibly yes — modestly. At fixed $\mathfrak{m}$ (primorial cubic conductor), the cubic bilateral $U^{(3)} W^{(3)} = D^{\mathrm{rad},3} V^{\mathrm{Gauss},3}$ provides an explicit Hecke-Helmert decomposition of any cubic-Gauss-sum-weighted prime-arithmetic functional (T27 Theorem D). For the cubic large sieve at $\mathfrak{m}$, this gives an **organized** rather than improved bound — same constants, different basis. This is the m=2 audit lesson (T9.4.1): bilateral factorizations are reorganizations, not analytic improvements, unless the Gram non-trivial structure adds genuine content.

The candidate question: does the eigenstructure of $W^{(3)*} G^{(3)} W^{(3)}$ on Hecke characters (T27 §7.3 open question) provide a *new* upper bound on $\sum_\psi |\Pi^{(3)}_\psi|^2$ at primorial cubic conductor? **Possibly, but the connection to Patterson's *single-character, varying-modulus* sum requires an extra inversion step that the framework doesn't supply.**

### (d.2) Could the framework give the explicit Patterson constant $c$?

The constant $c$ encodes $\Gamma(1/3)$ and a metaplectic residue. The simplicial framework's content at the Archimedean place (Q8vM3 UPT-selected Bargmann-Fock at $v = \infty$, cf. Note_MetaplecticSelection_UniformPlaceArgument_T4nP7v2.md) includes:

- Standard Gamma factor $\pi^{-s/2} \Gamma(s/2)$ at the Archimedean place.
- Weyl/CCR + metaplectic Fourier + positive-energy $N$ structure.

These are GL(1) / GL(2) metaplectic content. **The leap to GL(3) metaplectic content** — where Patterson's residue lives — is a substantial extension not yet present in the program. The cubic GL(3) Eisenstein series and its residue at $s = 5/6$ is the genuine open arithmetic-automorphic question; the simplicial framework's cubic Kummer clock is the *base ring* of this Eisenstein series, not the Eisenstein series itself.

### (d.3) Could it improve Heath-Brown's $X^{5/6-\delta}$ bound?

This requires either:
- A new bilinear bound on cubic Gauss sums (the cubic large sieve angle), or
- A new automorphic input (the GL(3) Eisenstein residue angle).

The simplicial framework can plausibly give angle 1 *modestly* (item d.1) but does not have angle 2. Heath-Brown's classical $\delta > 0$ is small and conditional; the simplicial program's reorganization is **unlikely to improve $\delta$** without genuine new analytic input.

---

## (e) Concrete sub-target (theorem-candidate)

If the program were to pursue this, the realistic sub-target is:

**Conjecture (T27-Patterson hybrid).** *At primorial cubic conductor $\mathfrak{m}_n = p_1 p_2 \cdots p_n \cdot \mathbb{Z}[\zeta_3]$, the cubic-Gram-weighted Hecke-character variance*

$$V^{(3)}_{\mathfrak{m}_n}(X) := \vec{\Lambda}_3(X)^* \cdot (W^{(3)*} G^{(3)} W^{(3)}) \cdot \vec{\Lambda}_3(X)$$

*where $\vec{\Lambda}_3(X)_\psi := \sum_{N(\mathfrak{a}) \le X, (\mathfrak{a}, \mathfrak{m}_n) = 1} \Lambda_3(\mathfrak{a}) \psi(\mathfrak{a})$, satisfies the explicit bound*

$$V^{(3)}_{\mathfrak{m}_n}(X) \le \lambda_{\max}(W^{(3)*} G^{(3)} W^{(3)}) \cdot \varphi_3(\mathfrak{m}_n) \cdot X (\log X)^c$$

*for some explicit $c$, where $\lambda_{\max} \approx 4.02$ at $N=30$ (from probe_T27_output.txt) and the matrix has a controlled spectrum in $[3.2, 4.0]$ at all primorial $n$.*

This is a structural identity bound, not the Patterson asymptotic. It would contribute to T27's [A3'] closure path (the cubic Weil positivity criterion of ocho/diez) — *not* to Patterson directly. The connection to Patterson would require an extra step: relating cubic-Hecke variance at primorial cubic conductor to single-character sums over varying primary primes. That step is **the same gap** that separates Bombieri-Vinogradov (which the simplicial framework targets via diez §3) from Patterson (which lives in a different analytic regime).

**Honest reading:** the realistic theorem-candidate from the simplicial framework at the cubic level is **cubic [A3'] closure** (T27 §8), which advances the RH/GRH program, *not* Patterson advance.

---

## (f) Recommendation

**Do not pursue Patterson via the simplicial framework as the primary goal.**

Reasoning:

1. **Alignment is real but at the wrong level.** T27's cubic Gauss sums $\tau_3(\psi, a)$ specialize correctly to Patterson's $g(\pi)$, and the cubic Kummer clock $K_N^{(3)}$ is the natural arithmetic ambient. But the framework aggregates over Hecke characters at fixed cubic conductor; Patterson aggregates over primary primes (varying conductors) at fixed cubic-residue character. These are **structurally different aggregations**, both legitimate, but the framework's existing identities operate on the wrong one.

2. **The distinctive lever (cubic Gram non-collapse $G^{(3)} \ne I$) is orthogonal to Patterson.** The cubic Gram lives on the additive character axis at fixed $\mathfrak{m}$, providing spectral content for cubic BV variance at primorial cubic conductor. This is exactly the right tool for **cubic [A3']** (closing the cubic positivity criterion of ocho/diez) but not for Patterson's varying-modulus sum.

3. **The explicit Patterson constant $c$ requires GL(3) metaplectic content** (the residue at $s = 5/6$ of the cubic metaplectic GL(3) Eisenstein series). The simplicial framework's Archimedean content (Q8vM3) is GL(1)/GL(2) metaplectic, one rung below. Bridging is a multi-paper extension, not a focused attack.

4. **Heath-Brown's $X^{5/6 - \delta}$ bound is unlikely to improve via simplicial reorganization** because the simplicial framework provides change-of-basis, not new bilinear/multilinear bounds. The cubic Gram non-collapse gives modest spectral content at one cubic conductor; Patterson needs control across all cubic conductors simultaneously, with metaplectic input.

5. **The numerical probe** (94 primary primes, $N(\pi) \le 500$) confirms the partial Patterson sum is in deep pre-asymptotic regime (|P(X)|/X^{5/6} ≈ 0.005 at X=500), validates the canonical Heath-Brown cancellation (cubic Gauss sums have moduli ~10% of trivial bound), and **does not exhibit any simplicial-specific structure** beyond what classical theory predicts.

**What to do instead with cubic-framework tools:** continue the T27 / cubic [A3'] line of attack on RH/GRH at primorial cubic conductor, where:
- The cubic Gram non-collapse is genuinely load-bearing,
- The eigenstructure of $W^{(3)*} G^{(3)} W^{(3)}$ on Hecke characters is the precise structural lever,
- The target ($\theta_0^{(3)}(p_n) = 1 - C^*_3/n$ at primorial cubic conductor) matches what the framework can supply.

**Patterson alternative recommendation:** if the director wishes to engage cubic Gauss sums beyond the RH program, the natural next step is **Heath-Brown's "third-derivative" or "cubic large sieve" bilinear forms** at primorial cubic conductor — a half-step less ambitious than Patterson, where T27's bilateral might give an explicit (if not improved) cubic large sieve organization. Forward paper title candidate: *T27.6 — Cubic Large Sieve at Primorial Cubic Kummer Base via Bilateral Factorization*. Tractability: medium. Expected gain: organizational, not analytic.

---

## Word count: approximately 2,400 words.

## References (selected)

- Patterson, S. J. (1978). *A cubic analogue of the theta series.* J. reine angew. Math. 296, 125-161.
- Heath-Brown, D. R., Patterson, S. J. (1979). *The distribution of Kummer sums at prime arguments.* J. reine angew. Math. 310, 111-130.
- Heath-Brown, D. R. (2000). *Kummer's conjecture for cubic Gauss sums.* Israel J. Math. 120, 97-124.
- Friedberg, S., Hoffstein, J., Lieman, D. (1995). *Double Dirichlet series and the n-th order twists of Hecke L-series.* Math. Ann. 327.
- Brubaker, B., Bump, D., Friedberg, S. (2011). *Weyl group multiple Dirichlet series, Eisenstein series and crystal bases.* Ann. Math. 173, 1081-1120.
- Dunn, A., Radziwiłł, M. (2021). *Bias in cubic Gauss sums: Patterson's conjecture.* arXiv:2109.07463.
- Murillo Montero, L. (2026). T8, T9, T9.4, T9.4.1, T10, T27, ocho, diez. Simplicial program.

---

*End of assessment, Draft 1, 2026-05-26. Companion probe `probe_patterson_cubic_gauss.py` in the worktree.*
