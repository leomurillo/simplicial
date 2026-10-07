# Audit of Pass-5 §17: The Apex No-Isolator Argument

**Leonardo Murillo Montero + Codex**

*Draft 1 — May 25, 2026*

## Verdict in one line

**§16.7 Lemma 16.4 (off-axis spectral isolator) is rigorous.** **§17.3 "True No-Isolator Theorem" is NOT a theorem** — it is a restated goal, logically equivalent to RH itself. The simplicial program's contribution at §17 is a sharp *reformulation* of the GRH target, not a proof.

## 1. What §17 actually says

Pass-5 §16–17 builds the chain:

1. **§16.3 Theorem 16.2 (Operational native gate equivalence).** RH ⟺ $H_n, J_n \succeq 0$ for all $n$ on the folded cumulants $\mu_n = \ell_{n+1}$. Both directions proven rigorously (Stieltjes forward; Hamburger/Stieltjes moment problem + Hadamard atomization reverse).

2. **§16.7 Lemma 16.4 (off-axis spectral isolator).** If the folded zero ledger contains a point $\lambda_0 \notin [0, \infty)$, then there is a real polynomial $p$ with $\mathcal{Q}[p] < 0$. (Proven; see §3 below for the audit.)

3. **§17.1 Differential-functional reformulation.** Hankel positivity $\Leftrightarrow$ for every real polynomial $p$:
$$\mathfrak{D}_{p^2}[F] \ge 0 \quad\text{and}\quad \mathfrak{D}_{sp^2}[F] \ge 0,$$
where $F(x) = (\xi'/\xi)(1/2 + \sqrt{x}) / (2\sqrt{x})$ and $\mathfrak{D}_g[F] := \sum_n g_n (-1)^n F^{(n)}(0)/n!$.

4. **§17.2 Prime/gamma split.** $F = F_{\mathrm{arch}} + F_{\mathrm{prime}}$ with explicit closed forms, where $F_{\mathrm{arch}}$ comes from $1/s + 1/(s-1) - (\log\pi)/2 + \psi(s/2)/2$ and $F_{\mathrm{prime}}$ from $\zeta'/\zeta(s)$.

5. **§17.3 "True No-Isolator Theorem".** For every real polynomial $p$, $\mathfrak{D}_{p^2}[F] \ge 0$ and $\mathfrak{D}_{sp^2}[F] \ge 0$.

The Pass-5 text after §17.3 says: *"The advantage is tactical. Instead of searching for zeros, we search for a positive-cone proof of these finite jets. ... The explicit-formula route must prove that no such finite prime/gamma jet witness exists."*

This is honest: §17.3 is presented as the **next target**, not as a theorem already proven.

## 2. What's rigorous

### 2.1 Theorem 16.2 (the equivalence)

Both directions are classical:

- **Forward (RH ⟹ Hankel positivity).** Hadamard product gives $B(x) = \prod_k (1 + x \gamma_k^{-2})$, so $B'/B$ is a positive trace-weighted Stieltjes transform of the atomic measure $\sum_k \gamma_k^{-2} \delta_{\gamma_k^{-2}}$. Stieltjes positivity (Lemma 3.1 of the GRH note) gives $H_n, J_n \succeq 0$.

- **Reverse (Hankel positivity ⟹ RH).** Hamburger moment problem (positive Hankel ⟺ positive measure on $\mathbb{R}$) + Stieltjes refinement (with $J$ positive ⟹ measure on $[0, \infty)$) + uniqueness of Taylor expansion at $0$ ⟹ the recovered measure coincides with $B'/B$ on its domain. Since $B'/B$ is meromorphic with simple poles at $-\gamma_k^{-2}$, the measure is atomic on $(0, \infty)$, forcing all $\gamma_k^2 > 0$, hence $\gamma_k \in \mathbb{R}$, hence all zeros of $\xi$ on the critical line. ✓

This is the unconditional analytic skeleton — both directions rigorous classical moment theory.

### 2.2 Lemma 16.4 (sensitivity)

**Statement.** If the folded zero ledger contains $\lambda_0 \notin [0, \infty)$, then $\exists$ real polynomial $p$ with $\mathcal{Q}[p] = \sum_\alpha m_\alpha \lambda_\alpha p(\lambda_\alpha)^2 < 0$.

**Proof structure:**

1. The set $K := \{\lambda_\alpha\} \cup \{0\}$ is compact in $\mathbb{C}$ with $0$ as only accumulation point (because $\lambda_\alpha = -\alpha^{-1} \to 0$ as $|\alpha| \to \infty$, and $\xi$ has only finitely many zeros in any bounded set).
2. Trace summability: $\sum_\alpha m_\alpha |\lambda_\alpha| < \infty$. This follows from $\sum_\rho |\rho - 1/2|^{-2} < \infty$ (classical zero-density bound; works for any horizontal strip configuration of zeros, not just RH).
3. **Real $\lambda_0 < 0$ case.** Apply Mergelyan to find polynomial $p \approx 1$ at $\lambda_0$, $\approx 0$ elsewhere on $K$. Then $\mathcal{Q}[p] \approx m_{\lambda_0} \lambda_0 + \epsilon \cdot O(1) < 0$.
4. **Nonreal $\lambda_0$ case.** Pick $w \in \mathbb{C}$ with $2 \mathrm{Re}(m_{\lambda_0} \lambda_0 w^2) < 0$. Use conjugation-symmetric Mergelyan to build real polynomial $p$ with $p(\lambda_0) \approx w$, $p(\overline{\lambda_0}) \approx \bar{w}$, $p$ small elsewhere on $K$. Paired contribution $2 \mathrm{Re}(m_{\lambda_0} \lambda_0 w^2) < 0$ dominates the trace-summable remainder. ✓

**Audit verdict:** The proof is rigorous.

Two technical points worth flagging:

- **Continuity of the prescribed function at 0.** The Mergelyan approximation needs $f$ continuous on $K$ with $f(\lambda_0) = w$, $f(\bar\lambda_0) = \bar w$, $f = 0$ elsewhere. Continuity at $0$ requires $f \to 0$ along $K \setminus \{\lambda_0, \bar\lambda_0\}$. This holds because all other $\lambda_\alpha$ accumulate to $0$ and $f$ is $0$ on those. ✓
- **Polynomial conjugation symmetry.** Mergelyan gives a complex polynomial; replacing it by $(p + \bar p)/2$ (real-coefficient version, where $\bar p$ means conjugate coefficients) preserves uniform-on-$K$ approximation because $K$ is conjugation-symmetric. ✓

So Lemma 16.4 stands.

**What it proves:**
$$\text{some folded zero } \lambda_0 \notin [0, \infty) \;\Longrightarrow\; \exists n,\, H_n \not\succeq 0.$$

Equivalently (contrapositive):
$$\forall n,\, H_n \succeq 0 \;\Longrightarrow\; \text{all folded zeros in } [0, \infty) \;\Longleftrightarrow\; \mathrm{RH}.$$

This is the **same** direction as Theorem 16.2 reverse, but proved **constructively**: not by abstract moment theory but by exhibiting an explicit isolator polynomial.

### 2.3 §17.1–§17.2 (Bures pullback + prime/gamma split)

The identities

$$F(x) = \frac{1}{2\sqrt{x}} \frac{\xi'}{\xi}\!\left(\tfrac12 + \sqrt{x}\right), \qquad F = F_{\mathrm{arch}} + F_{\mathrm{prime}}$$

with $F_{\mathrm{arch}}$ and $F_{\mathrm{prime}}$ defined as the odd-in-$t$ parts of $A(1/2 \pm t)/2t$ and $P(1/2 \pm t)/2t$ respectively, are **exact analytical identities**. They are computations from the Hadamard / functional-equation forms of $\xi$. ✓

The Bures/Herglotz pullback $m_B(z) = 2z F(-z^2)$ in §17 is also a rigorous identity once $F$ is defined.

So everything in §17 *up to and including* §17.2 is rigorous machinery: it gives an explicit closed form of the object we want to prove positive on quadratic test polynomials.

## 3. What is NOT a theorem (the actual gap)

### 3.1 §17.3 "True No-Isolator Theorem"

**Stated:** For every real polynomial $p$, $\mathfrak{D}_{p^2}[F] \ge 0$ and $\mathfrak{D}_{sp^2}[F] \ge 0$.

**Logical content:** By Theorem 16.2, this is equivalent to RH.

**Status:** Stated, not proven. The Pass-5 text explicitly notes this: *"The explicit-formula route must prove that no such finite prime/gamma jet witness exists."*

So §17.3 is **a target, not a theorem**. The "no-isolator" terminology is honest if read carefully — the lemma that's proven (Lemma 16.4) is the *converse* direction: "if an isolator polynomial existed, we could find it constructively." The forward "no isolator can exist" direction is exactly RH.

### 3.2 What the §17 chain delivers vs. claims

| Statement | Status |
|---|---|
| Theorem 16.2 (RH ⟺ Hankel positivity) | **Rigorous** |
| Lemma 16.4 (off-line zero ⟹ finite negative witness) | **Rigorous, constructive** |
| §17.1 (Bures pullback identity) | **Rigorous** |
| §17.2 (prime/gamma split, explicit closed form) | **Rigorous** |
| §17.3 (no negative witness exists for every $p$) | **Stated, equivalent to RH, NOT proven** |

## 4. What this means for A1 in the GRH-pending list

The audit refines the A1 item. There is no hidden GRH proof inside §17. What §17 gives is:

**A clean analytical target.** Prove $\mathfrak{D}_{p^2}[F_{\mathrm{arch}} + F_{\mathrm{prime}}] \ge 0$ and $\mathfrak{D}_{sp^2}[F_{\mathrm{arch}} + F_{\mathrm{prime}}] \ge 0$ for every real polynomial $p$, where $F_{\mathrm{arch}}, F_{\mathrm{prime}}$ are explicit closed-form functions.

**Concretely:** the Taylor jets of $F$ at $0$ are the cumulants $\mu_n = \ell_{n+1}$. So the inequalities amount to
$$\sum_{a,b=0}^n c_a c_b \mu_{a+b} \ge 0, \qquad \sum_{a,b=0}^n c_a c_b \mu_{a+b+1} \ge 0$$
for every $(c_0, \ldots, c_n) \in \mathbb{R}^{n+1}$ and every $n \ge 0$. With $F$ split as arch + prime, each cumulant decomposes as $\mu_n = \mu_n^{\mathrm{arch}} + \mu_n^{\mathrm{prime}}$.

The analytical question becomes: **can the archimedean cone dominate the prime cone?** That is:
$$c^T H_n^{\mathrm{arch}} c + c^T H_n^{\mathrm{prime}} c \ge 0 \quad ?$$

This is exactly an explicit-formula problem. It is morally the same task that Bombieri–Lagarias and Connes attacked for Li's coefficients. Our reformulation has more structure (the prime/gamma split at every $n$, not just for the integrated $\lambda_n$), but the fundamental difficulty is unchanged.

## 5. Refined A1 prognosis

- **Settled by this audit:** §17.3 is a goal, not a free theorem. The Apex No-Isolator name in the program covers two distinct objects; only the sensitivity half (Lemma 16.4) is proven.
- **Still open:** the specificity half — finding a positive-cone proof of $\mathfrak{D}_{p^2}[F] \ge 0$ from the explicit closed-form expressions for $F_{\mathrm{arch}}, F_{\mathrm{prime}}$.
- **Cheap next test:** numerically compute $\mu_n^{\mathrm{arch}}$ and $\mu_n^{\mathrm{prime}}$ for small $n$, evaluate $\mathfrak{D}_{p^2}[F_{\mathrm{arch}}]$ and $\mathfrak{D}_{p^2}[F_{\mathrm{prime}}]$ on a basis of small polynomials, and see whether the archimedean piece has a clean positive margin over the prime piece. If yes, that suggests a Bombieri-Lagarias-style bound is achievable; if no, the problem is structurally harder.

## 6. What the simplicial program still might contribute uniquely

The §17 reformulation puts us on the same footing as classical Li-criterion attacks. The simplicial program's distinctive assets that have NOT yet been brought to bear on this specific target:

1. **Helmert decomposition of the prime contribution.** $\zeta'/\zeta(s)$ at primorial scale decomposes through the radical clock $K_N = \mathbb{Q}(\sqrt{p} : p \le N)$. This might give a *new* prime-side bound not available in the classical attack.

2. **Subagent A's equidistribution theorem at N=6 (closed form).** At the primorial equidistribution limit, the Helmert decomposition forces specific structural cancellations. Extending this to general primorial N could give the missing prime-side cone bound.

3. **The joint-cumulant version.** Going from $\xi$ (Riemann's) to $\Xi_N$ (joint primorial) replaces the prime/gamma split with a *48-fold* (at N=210) split with character orthogonality. Cross-character cancellations might give bounds unavailable in the single-$\xi$ case.

These remain Tier-A pending items (A2, A3). A1 itself, as a "free win," is settled: it isn't one.

## 7. Recommendation

1. **Mark A1 as audited and closed.** §17 contains no hidden GRH proof. The "no-isolator" name covers a rigorous sensitivity lemma plus a stated-but-unproven specificity goal.

2. **Run the numerical probe (item 5 above).** Compute $\mu_n^{\mathrm{arch}}$ and $\mu_n^{\mathrm{prime}}$ explicitly for $n \le 30$ at mpmath dps=100 using the closed-form $\xi'/\xi$ expansion. Check whether $H_n^{\mathrm{arch}} + H_n^{\mathrm{prime}} \succeq 0$ holds with positive margin from $H_n^{\mathrm{arch}}$ alone. This will tell us whether a Bombieri-Lagarias-style proof is even structurally possible.

3. **Move to A2 (extend subagent A's N=6 theorem) and A3 (Pass-8 Cesàro at all rungs).** These are the genuine simplicial-native assets that have not yet been brought to bear on §17's target.

---

*Audit performed by reading Pass-5 §15–§17 line-by-line on May 25, 2026. The conclusion is honest: §17 is a sharp reformulation, not a hidden proof. The remaining analytical work lives at items A2, A3 and the numerical probe described above.*
