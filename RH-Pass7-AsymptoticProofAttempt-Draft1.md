# Pass-7 Asymptotic Identity: Proof Attempt and Honest Boundaries

**Leonardo Murillo Montero + Codex**

*Working draft - May 24, 2026*

## Honest opening

The previous validation note claimed the finite-$T$ deficit matches $1/T$ "within 0.06 percentage points." That match held at $T = 7$ specifically. **Looking at the T-scan from earlier sessions reveals the deficit DOES NOT follow $1/T$ uniformly**:

| $T$ | Trace at $N=30$ | Ratio to joint ($\approx 1.77$) | Naive $1/T$ prediction |
|---|---|---|---|
| 4 | 0.633 | 0.36 | 0.75 |
| 5 | 1.568 | 0.89 | 0.80 |
| 6 | 0.881 | 0.50 | 0.83 |
| 7 | 1.519 | 0.86 | 0.86 ✓ |
| 8 | 0.872 | 0.49 | 0.88 |
| 9 | 0.883 | 0.50 | 0.89 |
| 10 | 1.546 | 0.87 | 0.90 |
| 11 | 0.887 | 0.50 | 0.91 |
| 12 | 0.563 | 0.32 | 0.92 |

**The trace OSCILLATES wildly with $T$, with peaks near joint cumulant ($\sim 1.5$) and troughs near half ($\sim 0.6-0.9$).** The agreement at $T = 7$ was empirically striking but the simple $1/T$ scaling does not extend.

This forces a correction: the rigorous asymptotic identity is in a **Cesàro/time-averaged sense**, not pointwise at finite $T$. The Pass-7 framework's correctness needs to be restated accordingly.

## What is actually provable

### Setup

For each non-trivial Dirichlet character $\chi \pmod N$, define
\[
S_\chi(T) := \sum_{\substack{n \le e^T \\ \gcd(n, N) = 1}} \chi(n) \Lambda(n) / \sqrt{n}.
\]

The Pass-7 multiplicative apex trace at $(N, T)$ is
\[
\mathrm{trace}(N, T) = \frac{1}{\varphi(N)} \sum_{\chi \ne \chi_0} |S_\chi(T)|^2.
\]

### Explicit formula

By Perron's formula applied to the Dirichlet series $\sum \chi(n)\Lambda(n)/n^{s+1/2} = -L'/L(\chi, s+1/2)$, shifting the contour past the pole at $s = 0$ and the zeros at $s = \rho_\chi - 1/2$:

\[
\boxed{
S_\chi(T) = -\frac{L'}{L}(\chi, 1/2) + \sum_{\rho_\chi} \frac{e^{T(\rho_\chi - 1/2)}}{\rho_\chi - 1/2} + R_\chi(T),
}
\]

where $R_\chi(T)$ collects archimedean and contour-tail contributions, bounded by $O(e^{T(1/2 - \delta)}/T)$ for some $\delta > 0$ under standard zero-free region estimates.

### Conditional structure (under GRH for $L(\chi)$)

Assume GRH for the Dirichlet L-function $L(\chi, s)$: all non-trivial zeros are $\rho_\chi = 1/2 + i\gamma_\chi$ with $\gamma_\chi \in \mathbb R$. Then $\rho_\chi - 1/2 = i\gamma_\chi$ and:
\[
S_\chi(T) = -L'/L(\chi, 1/2) + \sum_{\gamma_\chi} \frac{e^{iT\gamma_\chi}}{i\gamma_\chi} + O(e^{-\delta T}).
\]

The second term oscillates: $|S_\chi(T)|^2$ is NOT monotone in $T$.

### The mean-square asymptotic

**Theorem (mean-square average, conditional on GRH).** Under GRH for all $L(\chi)$ with $\chi$ a primitive Dirichlet character of conductor dividing $N$:
\[
\lim_{T_0 \to \infty} \frac{1}{T_0} \int_0^{T_0} |S_\chi(T)|^2 \, dT = \sum_{\gamma_\chi} \frac{1}{\gamma_\chi^2} + \left|\frac{L'}{L}(\chi, 1/2)\right|^2 + \text{cross terms}.
\]

**Proof sketch.** Substituting the explicit formula:
\[
|S_\chi(T)|^2 = \left| -L'/L(\chi, 1/2) + \sum_\gamma e^{iT\gamma}/i\gamma \right|^2 + O(e^{-\delta T}).
\]
Expanding the square:
\[
|S_\chi(T)|^2 = |L'/L(\chi, 1/2)|^2 + 2\Re\!\left[-L'/L(\chi, 1/2) \overline{\sum_\gamma e^{iT\gamma}/i\gamma}\right] + \left|\sum_\gamma e^{iT\gamma}/i\gamma\right|^2 + \text{errors}.
\]

Averaging over $T \in [0, T_0]$:
- First term: constant, contributes $|L'/L(\chi, 1/2)|^2$.
- Cross terms: linear in $e^{iT\gamma}/(i\gamma)$, average to 0 as $T_0 \to \infty$.
- Quadratic term: $\sum_{\gamma_1, \gamma_2} e^{iT(\gamma_1 - \gamma_2)} / (i\gamma_1)(\overline{i\gamma_2}) = \sum_\gamma 1/\gamma^2$ on diagonal $\gamma_1 = \gamma_2$, off-diagonal averages to 0.
- Error terms: $O(e^{-\delta T})$ contributes 0 in the limit.

So the mean-square is $|L'/L(\chi, 1/2)|^2 + \sum_\gamma 1/\gamma^2$. $\square$

### Aggregating across characters

Summing over $\chi$ and dividing by $\varphi(N)$:
\[
\lim_{T_0 \to \infty} \frac{1}{T_0} \int_0^{T_0} \mathrm{trace}(N, T) \, dT
= \frac{1}{\varphi(N)} \sum_\chi \sum_{\gamma_\chi} \frac{1}{\gamma_\chi^2} + \frac{1}{\varphi(N)} \sum_\chi \left|\frac{L'}{L}(\chi, 1/2)\right|^2.
\]

The first term is $\ell_1^{\mathrm{joint}}(N) / \varphi(N)$. The second is an "asymptotic constant" determined by $|L'/L(\chi, 1/2)|^2$ values.

**Hmm — there's a $1/\varphi(N)$ factor.** This means:
\[
\lim_{T_0 \to \infty} \langle \mathrm{trace}(N, T) \rangle_T = \frac{\ell_1^{\mathrm{joint}}(N)}{\varphi(N)} + C(N).
\]

But empirically (LMFDB): trace ≈ $\ell_1^{\mathrm{joint}}(30) = 1.77$, NOT $\ell_1^{\mathrm{joint}}(30)/8 = 0.22$.

**There is a factor of $\varphi(N)$ discrepancy between my proof above and the empirical match.** Let me trace where this is wrong.

### Correction: normalization convention

In the session's computation:
\[
\widehat y_\chi = \frac{1}{\sqrt{\varphi(N)}} \sum_{r \in U} \overline{\chi(r)} \tilde y(r) = \frac{\overline{S_\chi(T)}}{\sqrt{\varphi(N)}}.
\]

So $|\widehat y_\chi|^2 = |S_\chi(T)|^2 / \varphi(N)$, and
\[
\mathrm{trace} = \sum_\chi |\widehat y_\chi|^2 = \frac{1}{\varphi(N)} \sum_\chi |S_\chi(T)|^2.
\]

Under Cesàro averaging:
\[
\langle \mathrm{trace} \rangle = \frac{1}{\varphi(N)} \sum_\chi \sum_{\gamma_\chi} \frac{1}{\gamma_\chi^2}.
\]

vs. joint cumulant:
\[
\ell_1^{\mathrm{joint}}(N) = \sum_\chi \sum_{\gamma_\chi} \frac{1}{\gamma_\chi^2}.
\]

These differ by factor $\varphi(N)$. At $N = 30, \varphi(N) = 8$. So predicted Cesàro-mean trace = 1.77/8 = 0.22, but observed trace = 1.52. **Off by factor 6.9** ≈ $\varphi(N) - 1$.

So either:
1. The normalization convention in the session's probe was different from my analytic setup (a $\sqrt{\varphi(N)}$ vs $\varphi(N)$ discrepancy), OR
2. The mean-square asymptotic above is wrong.

**This is a real gap in the "validation" claim.** The 0.86 ratio match was probably the result of a SPECIFIC normalization that happens to make $\mathrm{trace} \approx \ell_1^{\mathrm{joint}}$ at $T = 7$ for $N = 30$, but the underlying analytic relationship has a $\varphi(N)$ factor I missed.

### Re-examining the original validation

Looking again at the session's data:
- $N = 30$: trace 1.52, joint 1.77, ratio 0.86
- $N = 210$: trace 4.70, joint estimate ~5.0, ratio ~0.94

If the true relationship is $\langle \mathrm{trace} \rangle = \ell_1^{\mathrm{joint}}/\varphi(N) + C(N)$, then:
- $N = 30$: predicted 1.77/8 + C(30) = 0.22 + C(30); observed 1.52, so $C(30) \approx 1.3$
- $N = 210$: predicted 5.0/48 + C(210) = 0.10 + C(210); observed 4.70, so $C(210) \approx 4.6$

So $C(N)$ scales roughly with the trace itself, NOT a small correction. This suggests the dominant contribution to the trace is NOT the "$\ell_1^{\mathrm{joint}}/\varphi(N)$" piece but rather the "$|L'/L(\chi, 1/2)|^2$" pieces.

That is: at finite $T$, the trace is dominated by the *constant* term in $S_\chi(T)$, namely $L'/L(\chi, 1/2)$, NOT by the zero-sum oscillation.

This makes more physical sense: at small $T$ (like $T = 7$), the oscillating sum hasn't yet "filled in" its full mean-square content, so we mostly see the constant term.

### Revised understanding

The relationship trace $\to \ell_1^{\mathrm{joint}}(N)$ is **NOT** what the framework predicts. The actual relationship from the explicit formula is more subtle:

For each $\chi$:
\[
|S_\chi(T)|^2 = |L'/L(\chi, 1/2)|^2 + \text{oscillating}(T).
\]

The constant term $|L'/L(\chi, 1/2)|^2$ is what dominates at finite $T$, NOT $\sum_\rho 1/\gamma^2$.

So the session's "trace = 1.52" was approximately $\sum_\chi |L'/L(\chi, 1/2)|^2 / \varphi(N)$, NOT $\ell_1^{\mathrm{joint}}(30)$ rescaled.

The fact that LMFDB-computed $\ell_1^{\mathrm{joint}}(30) = 1.77$ ALSO equals (approximately) the observed trace is **a coincidence**, not a structural identity.

## Honest reassessment

### What Pass-7 actually shows

The session correctly identified:
1. The multiplicative apex is the right framework for finite-$N$ Dirichlet L-function structure.
2. The character coefficients $\widehat y_\chi$ encode partial-sum data for $L'/L(\chi)$.
3. The Born squares $|\widehat y_\chi|^2$ relate to L-function structure.

### What Pass-7 DOES NOT show

The session's "trace ≈ $\ell_1^{\mathrm{joint}}(N)$" appears to be a numerical near-coincidence at $T = 7$, not a structural identity provable from the explicit formula.

The actual structural relationship is:
\[
\mathrm{trace}(N, T) = \frac{1}{\varphi(N)}\sum_\chi |S_\chi(T)|^2
\]
and for $T$ "moderate":
\[
|S_\chi(T)|^2 \sim |L'/L(\chi, 1/2)|^2 + \text{oscillating in } T.
\]

The sum $\sum_\chi |L'/L(\chi, 1/2)|^2$ is a finite arithmetic quantity (computable from L-function central values), not a sum-over-zeros.

### What this means for Pass-7 framework

**The Pass-7 reframe needs significant restatement.** The multiplicative Dirichlet apex tracks **central L-function values** $L'/L(\chi, 1/2)$, not the **zero spectrum** $\sum_\rho 1/\gamma^2$.

Both quantities are connected via the explicit formula, but the Pass-5 Theorem 19.1 moment identity I was trying to validate involves the zero spectrum, while the multiplicative apex (at finite $T$) primarily encodes central values.

### What's still true

- The multiplicative apex captures **finite-arithmetic Dirichlet L-function content**.
- It is **the natural simplicial-program framework** for L-functions mod $N$.
- It provides explicit finite Born/Hankel structure connected to $L'/L(\chi, 1/2)$ values.
- It does NOT directly compute $\ell_n^{\mathrm{joint}}(N)$ at finite $T$ (the zero sum requires a different observable, like a properly Cesàro-averaged $|S_\chi(T)|^2$).

## Path forward

To make Pass-7 rigorous, the framework needs revision:

### Option 1: Compute $|L'/L(\chi, 1/2)|^2$ joint identity

If the multiplicative apex trace asymptotically equals $\sum_\chi |L'/L(\chi, 1/2)|^2 / \varphi(N) + o(1)$, then the rigorous Pass-7 identity is:
\[
\mathrm{trace}(N, T) = \frac{1}{\varphi(N)}\sum_\chi |L'/L(\chi, 1/2)|^2 + R(N, T)
\]
with $R(N, T) \to 0$ in some specific sense.

The connection to RH/GRH would then be via OTHER properties of $|L'/L(\chi, 1/2)|^2$, not directly the zero sum.

### Option 2: Define a different Born observable that targets zeros

Instead of single-T trace, use a Cesàro-averaged version:
\[
\widetilde{\mathrm{trace}}(N, T_0) := \frac{1}{T_0} \int_0^{T_0} \mathrm{trace}(N, T) \, dT
\]

Then:
\[
\lim_{T_0 \to \infty} \widetilde{\mathrm{trace}}(N, T_0) = \frac{1}{\varphi(N)} \sum_\chi \left[ |L'/L(\chi, 1/2)|^2 + \sum_\rho 1/\gamma^2 \right]
\]

The zero-sum part is then accessible, BUT it requires Cesàro averaging which the session's single-$T$ probe didn't do.

### Option 3: Reformulate the goal

Maybe the simplicial program should target $|L'/L(\chi, 1/2)|^2$ values directly, not zero sums. These are computable, finite, arithmetic — and may have their own positivity/RH-connection structure.

## Provisional theorem

What CAN be proved (with effort) under GRH:

**Theorem (Cesàro asymptotic moment identity).** Assume GRH for all primitive Dirichlet L-functions with conductor dividing $N$. Then
\[
\lim_{T_0 \to \infty} \frac{1}{T_0} \int_0^{T_0} \mathrm{trace}(N, T) \, dT = \frac{1}{\varphi(N)} \sum_{\chi \ne \chi_0} \left[ |L'/L(\chi, 1/2)|^2 + \sum_{\gamma_\chi} \gamma_\chi^{-2} \right].
\]

The proof follows the structure outlined above (explicit formula + mean-square of oscillating sum).

The cross term $|L'/L(\chi, 1/2)|^2$ is the central-value contribution; the sum-over-zeros is the spectral contribution. They're additive in the Cesàro mean.

## What this means for the RH program

The session's empirical validation was MISLEADING about Pass-7. The 0.86 ratio at $T = 7$ was a near-coincidence between trace and joint cumulant, not a structural identity.

The honest reframe:
- Pass-7 multiplicative apex is the **right framework** for finite-$N$ Dirichlet L-function arithmetic.
- The relationship to **zero spectra** requires Cesàro averaging and depends on GRH (not provable from it).
- The original Pass-5 Theorem 19.1 (Born squares match cumulants) is NOT directly witnessed by the multiplicative apex at single $T$.
- The session's validation showed the framework captures Dirichlet L-function content, but the specific moment identity claimed needs revision.

## Honest top-line

The previous "$0.86 = 1 - 1/7$" validation was **not the structural identity I claimed**. It was approximate agreement between two arithmetic quantities (trace at $T = 7$ and joint cumulant) that happens at that specific $T$.

The rigorous proof of Pass-7's claimed asymptotic identity requires:
1. **Cesàro averaging** (which the session probe didn't do)
2. **Conditional on GRH** for L-functions mod $N$
3. **Separation of central-value contribution from spectral contribution**

Pass-7 is still a useful framework, but its connection to RH is more indirect than the previous notes suggested. The simplicial program's Born-Helmert direct route via multiplicative apex doesn't immediately give the moment identity needed for Pass-5 Apex Lemma$_{HJ}$.

The honest top-line: **the simplicial framework provides finite Dirichlet L-function structure, but the bridge to RH/GRH zero positivity requires additional analytic work beyond what's been demonstrated**.

## What the team should know

1. The session's "0.06% match" was over-claimed. The deficit doesn't scale uniformly as $1/T$; the trace oscillates significantly.
2. The Cesàro-averaged identity is the actual structural target — and it has a $|L'/L(\chi, 1/2)|^2$ contribution that wasn't accounted for.
3. The Pass-7 framework needs to be re-examined: it captures L-function arithmetic but the precise link to $\ell_n^{\mathrm{joint}}(N)$ is more subtle.
4. The transfer matrix work, the LMFDB integration, and the broader framework remain valid — they just need to be deployed against a more carefully-stated target.

The research director should know: **the Pass-7 validation needs correction**. The structural reframing (GRH not RH) is still likely correct, but the specific empirical "validation" at $N = 30, T = 7$ doesn't prove the asymptotic identity I claimed.

## Recommended next step

Pause Pass-7 claims. Rerun the multiplicative apex computation with proper Cesàro averaging at varying $T$ ranges (e.g., compute $\langle \mathrm{trace}(N, T) \rangle$ over $T \in [T_0, T_1]$ for several windows) and see what the averaged trace converges to.

If averaged trace → $\sum_\chi |L'/L(\chi, 1/2)|^2 / \varphi(N) + \ell_1^{\mathrm{joint}}/\varphi(N)$, the rigorous Pass-7 theorem can be stated and proved.

If not, the framework needs more fundamental reconsideration.

The lesson: pre-committed criteria protect against false positives, but they can't catch a structural misidentification of what the observation is testing. The 0.06% match at $T = 7$ passed every pre-committed criterion AND was structurally misinterpreted. The criterion missed because it didn't compare against alternative structural hypotheses (constant $|L'/L|^2$ contribution).
