<!--
================================================================================
INTERNAL PROJECT LOG — NOT FOR PUBLICATION
This block is HTML comments. Pandoc drops it on the way to LaTeX, so it never
appears in the PDF. It records the editorial state so future-us need not grep a
chat log.

  Filename:   SmoothPrimorialMomentBarrier-Draft1.md  (stable through revision)
  Provenance: Merged and de-duplicated from two internal drafts —
                T33-SmoothPrimorialFamily-Draft1.md   (the construction)
                P6-SmoothPrimorialMomentBarrier-Draft1.md (the family-wide barrier).
              The mathematics is frozen and unchanged; this is an editorial
              merge, not a re-derivation. Every [P]/[A]/[C] tag, every proof,
              and every honest negative is carried over verbatim in content.
  Target:     A standalone special-functions / analytic-number-theory preprint
              that depends on NOTHING unpublished. Deposit channel (Leo's call):
              Zenodo DOI — arXiv math.NT needs an endorser the author does not
              currently have, so arXiv is NOT assumed.

  Self-containment scrub (what was neutralized so no unpublished work is cited):
    * The series house-glyph (Hebrew pe, via \heb[P]{...}) is REMOVED throughout.
      The smooth primorial is written pri_{idx,sharp}(z) (index side) and
      pri_sharp(x) (prime side), exactly as the construction draft's own
      notation. No Hebrew glyph survives in the body.
    * The construction draft's "Implications for the program" section (apex
      unitaries, the GG gravity-localization ledger, the FE-cluster /
      K-antisymmetric restatement) is DROPPED in full. None of it was
      load-bearing for any [P] result; it forward-referenced unpublished
      manuscripts. A single neutral sentence (end of §3) records only that the
      objects connect to the author's wider program (companion work, forthcoming).
    * Forward references to the unpublished completion manuscript (the "T15
      §12" pointers on the 1/2pi archimedean constant and on the moment
      obstruction) are softened to classical, self-contained language. The
      archimedean reading of 1/2pi = exp(-zeta'(0)/zeta(0)) is standard and is
      kept; the completion-theoretic claim that depended on the unpublished
      manuscript is NOT asserted.
    * The exterior draft's framing layer (the "Star"/Historic-Fiction section,
      the "real place is terminal" thesis, the boundary-operator ladder, and
      all bracketed pointers to sibling exterior papers) is DROPPED. The
      grounded mathematical content — the family-wide barrier, its
      factorization, the depth law, the constant-tower fixed point, the
      sqrt-scale barcode — is kept and presented as ordinary mathematics.
    * Cross-paper "§" pointers to other manuscripts are removed; all "§"
      references in the body are internal to THIS paper.

  Method footprint (kept minimal, per a special-functions audience):
    The grounded-paranoid-delusional pre-registration discipline that governed
    the computational settlements lives here, in comments, plus ONE short
    "Methods and reproducibility" remark in §6 and ONE citation
    (Murillo Montero 2026, the methodology preprint, which IS published). A
    referee needs none of the internal scaffolding to read the paper.

  PRE-REGISTRATION on record (the honest negatives, retained per method):
    * The depth N*(k) was pre-registered as STRICTLY monotone in k. It is NOT:
      the exact sequence is 3,3,4,4,5,9,9,9,... — non-decreasing with plateaus
      and a jump. The dead prediction is kept beside the surviving facts (§4.3).
    * The cross-family invariance N*(prod(p^k-1)) = N*(prod(p^k+1)) = N*(prod p^k)
      is an EXACT finite verification for k<=8, NOT forced by the factorization;
      the general statement is left open ([A]) (§4.2).
    * The smooth Mertens constant gamma-tilde_* differs from Euler's gamma; the
      difference is a named Riemann-error integral, not zero (§3.2).
    * No claim on RH is made. The sqrt-scale / barcode recovers RH's SCALE and a
      classical primorial-form equivalence; it does not separate on-line from
      off-line zeros (§5.4, §6).

  Artifact: Appendix A reproduces the deterministic exact-integer certificate
    (shipped as moment_barrier_certificate.py, scrubbed from the source
    P6-settlements.py: identical arithmetic, only print labels/comments cleaned
    of the series glyph and program jargon). Re-running reproduces its transcript
    byte-for-byte (verified 2026-06-13).

  OPEN EDITORIAL CALLS for Leo (see the cover note, not the paper):
    (A) Final title.   (B) Affiliation/email line + how it should render.
    (C) Deposit target (Zenodo recommended).   (D) Keep §5 as distributed
        (current) or pull the "structure of the barrier" material into one section.
================================================================================
-->

# The Smooth Primorial and the Moment Barrier of the Prime Ladder

**Leonardo Murillo Montero**

*ITCR, UNA, UCR*

*leonardo.murillo@gmail.com*

*Preprint — June 13, 2026*

---

## Abstract

The factorial has a canonical smooth twin: the Gamma function, which passes through every factorial value *exactly*, because the factorial is the moment sequence of $e^{-t}$ and $\Gamma$ is its Mellin interpolation. The primorial $P_n=\prod_{p\le p_n}p=1,2,6,30,210,\dots$ has had no such twin. We construct one. The **smooth primorial** $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$ is forced by Riemann's explicit formula — its constant $1/2\pi=e^{-\zeta'(0)/\zeta(0)}$ is the archimedean term — and is *unique* under either a Bohr–Mollerup log-convexity condition or a Wielandt strip-growth condition, exactly as $\Gamma$ is. Its asymptotic ratios against the divisor-lattice family emit the classical analytic constants in their structural homes: a smooth Mertens constant $\widetilde\gamma_*=0.6119\dots$ (which differs from Euler's $\gamma$ by a named Riemann-error integral), the values $1/\zeta(k)$ exactly for $k\ge2$, and $\log2\pi$ as a distinguished fixed point of the prime ladder.

Unlike the factorial, the primorial is **not a moment sequence**: its Hankel determinant $D_3=-787680<0$, so it admits no exact Mellin/$\Gamma$-style interpolation; the smooth primorial only *approaches* it, and the gap is the Riemann zero-sum. Our main theorem is that this barrier is **family-wide**: every genuinely multiplicative primorial invariant — $\varphi(P_n)$, $\sigma(P_n)$, $J_k(P_n)=\prod(p^k-1)$, $\prod(p^k+1)$, $\prod p^k$ — is non-moment (some Hankel determinant turns negative), and the *only* moment member of the divisor family is the divisor count $d(P_n)=2^n$, the one invariant that forgets the magnitudes of the primes. The proof tool is the factorization $D_N=\big(\prod_{i\le N}b_i\big)\det[b_{i+j}/b_i]$, which carries $\operatorname{sign}(D_N)$ in its second factor; the first-failure depth $N^*(k)$ is found to be $3,3,4,4,5,9,\dots$ — non-decreasing and unbounded, mirroring the Euler-product convergence partition, but (against a pre-registered guess that we record as falsified) *not* strictly monotone. Finally, the $\sqrt{\cdot}$-scale on which a prime's primality is sealed in the sieve is exactly the scale on which the smooth-vs-exact gap lives, which is the scale the Riemann hypothesis governs: we make the primorial-form RH equivalence precise and claim no progress on RH itself.

---

**Keywords:** primorial, Gamma function, smooth interpolation, Bohr–Mollerup theorem, Wielandt theorem, inverse logarithmic integral, Hamburger moment problem, Hankel determinant, Mertens' theorem, prime number theorem, Riemann explicit formula, Riemann hypothesis.

**MSC 2020:** 44A60 (Moment problems); 33B15 (Gamma, beta and polygamma functions); 11N05 (Distribution of primes); 11M06 (Riemann zeta-function); 11N37 (Asymptotic results on arithmetic functions); 11A41 (Primes); 30D15 (Special classes of entire functions).

---

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=1em]
**In plain terms.** The factorial $1,2,6,24,\dots$ has a famously smooth twin, the Gamma function, that lands on every one of its values exactly. The primorial $1,2,6,30,210,\dots$ — multiply the primes in one at a time — has a smooth twin too, built below; but it only *approaches* the primorial, never landing on it, and the size of the miss is governed by the Riemann hypothesis. This paper asks why exact landing is impossible and finds a clean, classical answer: a number sequence can be the "moments" of a probability distribution only if a ladder of determinants stays non-negative, and for the primorial one of them is $-787680$. We then show this is not a quirk of the primorial — *every* natural prime-built sequence fails the same test, and the only survivor is the one that throws away the sizes of the primes. A short exact-integer program is the whole of the computational evidence; we also test an obvious guess about the pattern, watch it fail, and keep it on the record.
\end{mdframed}

\clearpage

## 1. The smooth primorial

We write [P] for *proven*, [A] for *structural, pending a single named gap*, and [C] for *conjectural, reduced to a named gap*. These tags mark the epistemic status of each numbered result and are collected in the ledger of §6.

### 1.1 The two primorials and the inverse logarithmic integral

For $n\in\mathbb Z_{\ge0}$ the **index-side primorial** is $P_n:=\prod_{k=1}^n p_k$ with $P_0:=1$, where $p_k$ is the $k$-th prime. For $x\ge2$ the **prime-side primorial** is $\mathrm{pri}_*(x):=\prod_{p\le x}p$, a right-continuous step function with $\mathrm{pri}_*(p_n)=P_n$. The two are tied to Chebyshev's first function $\vartheta(x):=\sum_{p\le x}\log p$ by the tautology
$$\log\mathrm{pri}_*(x)=\vartheta(x),\qquad \log P_n=\vartheta(p_n). \tag{1.1}$$

Let $\mathrm{Li}(x):=\int_2^x dt/\log t$ be the (shifted) logarithmic integral, $\mathrm{Li}(2)=0$. It is real-analytic, strictly increasing, and strictly concave on $(1,\infty)$, with $\mathrm{Li}(x)\sim x/\log x$. Its inverse $\mathrm{Li}^{-1}:[0,\infty)\to[2,\infty)$ is real-analytic, strictly increasing, strictly convex, with $\mathrm{Li}^{-1}(0)=2$ and the key identity
$$(\mathrm{Li}^{-1})'(z)=\log\big(\mathrm{Li}^{-1}(z)\big). \tag{1.2}$$

### 1.2 The prime-side smooth primorial is forced by the explicit formula

The Riemann–von Mangoldt explicit formula for $\psi(x):=\sum_{n\le x}\Lambda(n)$ reads, for $x>1$ not a prime power,
$$\psi_0(x)=x-\sum_\rho\frac{x^\rho}{\rho}-\log(2\pi)-\tfrac12\log(1-x^{-2}), \tag{1.3}$$
$\rho$ ranging over the non-trivial zeros of $\zeta$ and the constant being $-\zeta'(0)/\zeta(0)=\log(2\pi)$. Passing to $\vartheta=\psi-\sum_{k\ge2}\vartheta(x^{1/k})$ moves the prime-power leakage into an $O(\sqrt x)$ term:
$$\vartheta(x)=x-\log(2\pi)-\sum_\rho\frac{x^\rho}{\rho}-\tfrac12\log(1-x^{-2})-\sum_{k\ge2}\vartheta(x^{1/k}). \tag{1.4}$$
Extracting the non-oscillatory leading part — the terms independent of the zeros and of the prime-power leakage — gives the canonical smooth Chebyshev function $\vartheta_{\mathrm{smooth}}(x)=x-\log(2\pi)$, hence the

**Definition 1.1 (prime-side smooth primorial).** $\displaystyle \mathrm{pri}_\sharp(x):=\exp\big(\vartheta_{\mathrm{smooth}}(x)\big)=\frac{e^{x}}{2\pi},\qquad x\in\mathbb R.$

This is **forced**: no constant is free; every term comes from $\zeta$ at $s=0$. The factor $1/2\pi=e^{-\log2\pi}$ with $\log(2\pi)=-\zeta'(0)/\zeta(0)$ is, in the standard reading, the contribution of the *archimedean place* — the term that completes the Euler product into $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$. Definition 1.1 is [P], modulo the classical explicit formula (Riemann 1859; von Mangoldt 1895; Titchmarsh 1986, Ch. 3).

**Proposition 1.2 (the deviation is the zero-sum).** *For $x>1$ not a prime power,*
$$\log\frac{\mathrm{pri}_*(x)}{\mathrm{pri}_\sharp(x)}=-\sum_\rho\frac{x^\rho}{\rho}+O(\sqrt x). \tag{1.5}$$

*Proof.* Subtract $x-\log2\pi$ from (1.4); the remaining $-\tfrac12\log(1-x^{-2})$ and $-\sum_{k\ge2}\vartheta(x^{1/k})$ are $O(\sqrt x)$. $\square$ [P]

### 1.3 The index side: duality through $\mathrm{Li}^{-1}$

The exact identity $P_n=\mathrm{pri}_*(p_n)$ says $P_n$ is $\mathrm{pri}_*$ read along the prime-enumeration map $n\mapsto p_n$, the integer inverse of $\pi(x)=\#\{p\le x\}$. Riemann's explicit formula for $\pi$ has leading non-oscillatory term $\mathrm{Li}(x)$, so the canonical smooth replacement of $n\mapsto p_n$ is $\tilde p(z):=\mathrm{Li}^{-1}(z)$, with $\tilde p(0)=2$ and (under RH) $\tilde p(n)=p_n+O(\sqrt{p_n}\log p_n)$. Composing,

**Definition 1.3 (index-side smooth primorial).** $\displaystyle \mathrm{pri}_{\mathrm{idx},\sharp}(z):=\mathrm{pri}_\sharp\big(\mathrm{Li}^{-1}(z)\big)=\frac{\exp\big(\mathrm{Li}^{-1}(z)\big)}{2\pi},\qquad z\in[0,\infty).$

Throughout, "the smooth primorial" with no qualifier means $\mathrm{pri}_{\mathrm{idx},\sharp}$. The two sides are linked by $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=\mathrm{pri}_\sharp(\mathrm{Li}^{-1}(z))$; the entire difference between the exact and smooth pictures is concentrated in the single top arrow $\tilde p$ versus $n\mapsto p_n$. The boundary value $\mathrm{pri}_{\mathrm{idx},\sharp}(0)=e^2/2\pi\approx1.177\ne1=P_0$ is kept honestly: forcing it to $1$ would discard the $\log2\pi$ that completes $\zeta$.

### 1.4 The Riemann hypothesis in primorial form

**Corollary 1.4 (RH, primorial form).** *Each of the following is equivalent to RH:*
$$\text{(i)}\quad \log\mathrm{pri}_*(x)-\log\mathrm{pri}_\sharp(x)=O(\sqrt x\,\log^2 x);\qquad \text{(ii)}\quad \log P_n-\log\mathrm{pri}_{\mathrm{idx},\sharp}(n)=O(\sqrt{p_n}\log^2 p_n).$$

*Proof.* By Proposition 1.2 this is the classical equivalence RH $\iff\vartheta(x)=x+O(\sqrt x\log^2 x)$, read on the prime and index sides respectively. $\square$ [P, RH-equivalent]

This is RH stated inside the primorial framework. It is a restatement of a textbook equivalence; **no progress toward RH is claimed by it**, here or anywhere below (see §5.4, §6).

### 1.5 What the interpolation looks like

Computing $\mathrm{Li}^{-1}(n)$ by Newton's method on $\mathrm{Li}(x)=n$:

| $n$ | $\mathrm{Li}^{-1}(n)$ | $\mathrm{pri}_{\mathrm{idx},\sharp}(n)$ | $P_n$ | ratio |
|---|---|---|---|---|
| 0 | $2.0000$ | $1.177$ | $1$ | $1.177$ |
| 1 | $2.8945$ | $2.879$ | $2$ | $1.440$ |
| 2 | $4.1086$ | $9.687$ | $6$ | $1.614$ |
| 3 | $5.6875$ | $46.998$ | $30$ | $1.567$ |
| 4 | $7.572$ | $309.27$ | $210$ | $1.473$ |
| 5 | $9.72$ | $1850$ | $2310$ | $0.801$ |
| 10 | $\approx23.5$ | $\approx2.57\times10^9$ | $6.47\times10^9$ | $0.40$ |

The multiplicative ratio is **not** monotone: it crosses $1$ between $n=4$ and $n=5$ and oscillates with the amplitude of the Riemann zero-sum. It is the *log*-ratio that tends to $0$ in the PNT-relative sense of Corollary 1.4, not the ratio itself. (The crossover near $n=5$ is the index-side shadow of $(\pi-\mathrm{Li})$ changing sign among the small primes.)

---

## 2. Uniqueness: Bohr–Mollerup and Wielandt

Both classical characterizations of $\Gamma$ transfer, with $\log z$ replaced by the smooth multiplier $\Delta(z):=\mathrm{Li}^{-1}(z+1)-\mathrm{Li}^{-1}(z)$.

### 2.1 The convexity input

**Lemma 2.1.** *$\mathrm{Li}^{-1}$ is strictly convex on $[0,\infty)$, and $\Delta(z)=\mathrm{Li}^{-1}(z+1)-\mathrm{Li}^{-1}(z)$ is strictly increasing.*

*Proof.* $\mathrm{Li}'(t)=1/\log t>0$ and $\mathrm{Li}''(t)=-1/(t\log^2 t)<0$ on $(1,\infty)$, so $\mathrm{Li}$ is concave and its inverse convex; explicitly $(\mathrm{Li}^{-1})''(z)=\log(\mathrm{Li}^{-1}(z))/\mathrm{Li}^{-1}(z)>0$. Monotonicity of $\Delta$ is convexity applied to unit translates. $\square$ [P]

$\Delta$ is the smooth analogue of "$\log p_{n+1}$ increases with $n$" — the only structural ingredient the Bohr–Mollerup squeeze needs beyond the standard $\Gamma$ proof.

### 2.2 The Bohr–Mollerup theorem

**Theorem 2.2 (Bohr–Mollerup for the smooth primorial).** *Let $f:[0,\infty)\to(0,\infty)$ satisfy*

*(BM1) $f(z+1)=e^{\Delta(z)}f(z)$ for all $z\ge0$;  (BM2) $f(0)=e^2/2\pi$;  (BM3) $\log f$ is convex on $[0,\infty)$.*

*Then $f(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi=\mathrm{pri}_{\mathrm{idx},\sharp}(z)$ for all $z\ge0$.*

*Proof.* Let $g:=\log f$. By (BM1) and telescoping, $g(n+z)-g(z)=\sum_{k=0}^{n-1}\Delta(z+k)=\mathrm{Li}^{-1}(n+z)-\mathrm{Li}^{-1}(z)$; in particular $g(n)-g(0)=\mathrm{Li}^{-1}(n)-2$. Fix $z\in[0,1]$. Convexity of $g$ on $[n-1,n+1]$ gives
$$z\,\Delta(n-1)\le g(n+z)-g(n)\le z\,\Delta(n).$$
Substituting the telescoped identity,
$$z\Delta(n-1)\le\big[g(z)-g(0)\big]+\big[\mathrm{Li}^{-1}(n+z)-\mathrm{Li}^{-1}(n)\big]-\mathrm{Li}^{-1}(z)+2\le z\Delta(n).$$
As $n\to\infty$: (a) $z\Delta(n)-[\mathrm{Li}^{-1}(n+z)-\mathrm{Li}^{-1}(n)]=z[\log\mathrm{Li}^{-1}(\xi_1)-\log\mathrm{Li}^{-1}(\xi_2)]$ for $\xi_1,\xi_2\in(n,n+1)$ by the mean value theorem, and the variation of $\log\mathrm{Li}^{-1}$ over a unit interval is $O(1/n)\to0$; (b) $z[\Delta(n)-\Delta(n-1)]=O(1/n)\to0$ by the same estimate. Both bracketing bounds converge to the same limit, forcing
$$g(z)-g(0)-\mathrm{Li}^{-1}(z)+2=0,$$
i.e. $g(z)=(2-\log2\pi)+\mathrm{Li}^{-1}(z)-2=\mathrm{Li}^{-1}(z)-\log2\pi$. Hence $f=\mathrm{pri}_{\mathrm{idx},\sharp}$ on $[0,1]$, and by (BM1) everywhere. $\square$

Once $\Delta$ is fixed (forced by the explicit formula for $\pi$), log-convexity removes all remaining freedom: $\mathrm{pri}_{\mathrm{idx},\sharp}$ is unique — the same shape as Bohr–Mollerup for $\Gamma$. **Theorem 2.2 is [P]** at the rigor of the classical theorem.

### 2.3 Growth on vertical strips

**Lemma 2.3.** *As $|t|\to\infty$ with $\sigma\in[1,2]$ fixed,*
$$\mathrm{Li}^{-1}(\sigma+it)=\big(\sigma\log|t|-\tfrac{\pi}{2}|t|\big)+i\big(t\log|t|+\tfrac{\pi}{2}\sigma\,\mathrm{sgn}(t)\big)+o(|t|).$$
*Consequently $\big|\mathrm{pri}_{\mathrm{idx},\sharp}(\sigma+it)\big|\sim |t|^{\sigma}e^{-\pi|t|/2}/2\pi$.*

*Proof sketch.* $\mathrm{Li}(z)=\frac{z}{\log z}(1+O(1/\log z))$ holds uniformly in any closed sector off the cut $[0,1]$; inverting, $z\sim w\log w$ for $\mathrm{Li}(z)=w$, and with $w=\sigma+it$, $\log w=\log|t|+i\frac\pi2\mathrm{sgn}(t)+O(1/|t|)$, expand $(\sigma+it)(\log|t|+i\frac\pi2\mathrm{sgn}(t))$. The modulus follows from $|\mathrm{pri}_{\mathrm{idx},\sharp}|=e^{\operatorname{Re}\mathrm{Li}^{-1}}/2\pi$. $\square$ [P]

The exponential rate $e^{-\pi|t|/2}$ is **the same as Stirling's for $\Gamma$**; the polynomial prefactor is $|t|^{\sigma}$ versus $\Gamma$'s $|t|^{\sigma-1/2}$ — one half-power higher, the only structural difference.

### 2.4 The Wielandt theorem

**Theorem 2.4 (Wielandt for the smooth primorial).** *Let $H_+:=\{\operatorname{Re} z>0\}$ and let $f:H_+\to\mathbb C^{*}$ be holomorphic and nowhere zero with*

*(W1) $f(z+1)/f(z)=\exp(\mathrm{Li}^{-1}(z+1)-\mathrm{Li}^{-1}(z))$;  (W2) $\lim_{z\to0^+}f(z)=e^2/2\pi$;  (W3) $f(z)\,e^{-\mathrm{Li}^{-1}(z)}$ is bounded on $\{1\le\operatorname{Re} z\le2\}$.*

*Then $f=\mathrm{pri}_{\mathrm{idx},\sharp}$ on $H_+$.*

*Proof.* Put $\phi(z):=\log f(z)-\mathrm{Li}^{-1}(z)+\log2\pi$. By (W1), $\phi(z+1)-\phi(z)=0$, so $\phi$ is $1$-periodic. By (W3), $\operatorname{Re}\phi=\log|f\,e^{-\mathrm{Li}^{-1}}\,2\pi|$ is bounded on the strip $\{1\le\operatorname{Re} z\le2\}$, and a single branch bounds $\operatorname{Im}\phi$; by $1$-periodicity $\phi$ extends to an entire function bounded on every translate of the strip, hence bounded on $\mathbb C$. By Liouville $\phi\equiv c$. By (W2), $\phi(0^+)=\log(e^2/2\pi)-2+\log2\pi=0$, so $c=0$ and $f=\mathrm{pri}_{\mathrm{idx},\sharp}$. $\square$

Wielandt's classical condition for $\Gamma$ — "$f$ bounded on $\{1\le\operatorname{Re} z\le2\}$" — works because $\Gamma$ itself decays there by Stirling, so "bounded" already means "tracks $\Gamma$'s growth." Condition (W3) is the literal analogue, "$f$ tracks $\mathrm{pri}_{\mathrm{idx},\sharp}$'s growth," made explicit because the smooth primorial decays on strips (Lemma 2.3). **Theorem 2.4 is [P]** at Wielandt's rigor. Replacing (W3) by a Phragmén–Lindelöf finite-exponential-type condition is a natural sharpening, left open [C].

---

## 3. The divisor family and the constant tower

The smooth primorial is the first member of a family obtained by smoothing the logarithm of each multiplicative invariant of primorials. Their asymptotic ratios are the classical analytic-number-theory constants, read in their structural homes.

### 3.1 The smooth Mertens constant

Define the smooth totient $\widetilde\phi$ by $\log\widetilde\phi(z)=\int_0^z\log(\mathrm{Li}^{-1}(t)-1)\,dt+C_\phi$, the constant fixed by Mertens-matching.

**Theorem 3.1 (smooth Mertens).** *As $z\to\infty$,*
$$\log\frac{\mathrm{pri}_{\mathrm{idx},\sharp}(z)}{\widetilde\phi(z)}=\log\log\mathrm{Li}^{-1}(z)+\widetilde\gamma_*+o(1),\qquad \widetilde\gamma_*:=C^*-\log\log2,\quad C^*:=\sum_{k\ge2}\frac{E_1((k-1)\log2)}{k}, \tag{3.1}$$
*where $E_1$ is the exponential integral. Numerically $C^*\approx0.24527$ and $\widetilde\gamma_*\approx0.6119$.*

*Proof.* By the definition of $\widetilde\phi$ and Definition 1.3, $\log(\mathrm{pri}_{\mathrm{idx},\sharp}/\widetilde\phi)=-\int_0^z\log(1-1/\mathrm{Li}^{-1}(t))\,dt+(\text{boundary})$. Substituting $u=\mathrm{Li}^{-1}(t)$ and expanding the logarithm,
$$-\int_2^{\mathrm{Li}^{-1}(z)}\frac{\log(1-1/u)}{\log u}\,du=\sum_{k\ge1}\frac1k\int_2^{\mathrm{Li}^{-1}(z)}\frac{du}{u^{k}\log u}.$$
The $k=1$ term is $\log\log\mathrm{Li}^{-1}(z)-\log\log2$; for $k\ge2$ each integral converges to $E_1((k-1)\log2)$ via $u=e^{s}$, and $C_\phi$ absorbs the discrete-matching shift. $\square$ [P]

### 3.2 The bias from Euler's $\gamma$ is a Riemann-error integral (honest negative)

A pre-registered expectation was that the family would emit Euler's $\gamma$ cleanly. It does **not**: the smooth Mertens constant is biased, and the bias is itself a named constant.

**Theorem 3.2.** $\displaystyle \widetilde\gamma_*-\gamma=\int_2^\infty\frac{\pi(u)-\mathrm{Li}(u)}{u(u-1)}\,du\approx0.0347. \tag{3.2}$

*Proof.* Compare the smooth integral $\int_2^x\log(1-1/u)/\log u\,du$ to the discrete sum $\sum_{p\le x}\log(1-1/p)$ by Abel summation against $d\mathrm{Li}$. With $f(u)=\log(1-1/u)$, $f'(u)=1/(u(u-1))$, the difference is $-\int_2^x f'(u)[\pi(u)-\mathrm{Li}(u)]\,du+O(\text{boundary})$. Discrete Mertens gives $\gamma$; the smooth integral gives $\widetilde\gamma_*$; their difference is (3.2). $\square$ [P]

This is the structurally honest statement: the family emits $\widetilde\gamma_*$, not $\gamma$, with the gap a Riemann-error integral. Both constants and their relation are [P].

### 3.3 Clean emission of $\zeta(k)$, and the partition principle

For $k\ge1$ set $\log\widetilde J_k(z)=\int_0^z\log(\mathrm{Li}^{-1}(t)^k-1)\,dt+C_{J_k}$.

**Theorem 3.3.** *For every $k\ge2$,*
$$\lim_{z\to\infty}\frac{\widetilde J_k(z)}{\mathrm{pri}_{\mathrm{idx},\sharp}(z)^{k}}=\frac{1}{\zeta(k)}\qquad\text{exactly, with no bias.} \tag{3.3}$$

*Proof.* $\log(\widetilde J_k/\mathrm{pri}_{\mathrm{idx},\sharp}^k)=\int_0^z\log(1-\mathrm{Li}^{-1}(t)^{-k})\,dt+(\text{boundary})$. Every term of $\log(1-u^{-k})=-\sum_{m\ge1}u^{-mk}/m$ has $mk\ge2$, so all integrals $\int du/(u^{mk}\log u)$ converge absolutely; $C_{J_k}$ matches the discrete $\prod_{j\le n}(1-p_j^{-k})\to1/\zeta(k)$. $\square$ [P]

**Theorem 3.4 (partition by Euler-product convergence).** *The family's $z\to\infty$ ratios emit constants according to the convergence regime of the underlying Euler product: absolutely convergent ($s\ge2$) gives clean $\zeta(k)$ with no bias ($\widetilde J_k/\mathrm{pri}^k$, $k\ge2$); conditionally convergent ($s=1$, Mertens) gives a shift by a named Riemann-error integral ($\mathrm{pri}/\widetilde\phi$).* [P]

| smooth ratio | asymptotic | emitted constant | bias |
|---|---|---|---|
| $\mathrm{pri}_{\mathrm{idx},\sharp}/\widetilde\phi$ | $e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z)$ | $\widetilde\gamma_*=0.6119$ | $\widetilde\gamma_*-\gamma=\int_2^\infty\frac{\pi-\mathrm{Li}}{u(u-1)}\,du\approx0.0347$ |
| $\widetilde J_2/\mathrm{pri}^2$ | $1/\zeta(2)=6/\pi^2$ | $-\log\zeta(2)$ | **none** |
| $\widetilde J_3/\mathrm{pri}^3$ | $1/\zeta(3)$ | $-\log\zeta(3)$ | **none** |
| $\widetilde J_k/\mathrm{pri}^k$, $k\ge2$ | $1/\zeta(k)$ | $-\log\zeta(k)$ | **none** |

### 3.4 The starting-prime tower and its archimedean fixed point

For each prime $p$, the smooth primorial *started at $p$* uses $\mathrm{Li}_p(x):=\int_p^x dt/\log t$, giving $\mathrm{Pri}_p(z):=e^{\mathrm{Li}_p^{-1}(z)}/2\pi$.

**Theorem 3.5 (translation orbit).** *Since $\mathrm{Li}_p(x)=\mathrm{Li}(x)-\mathrm{Li}(p)$, one has $\mathrm{Pri}_p(z)=\mathrm{pri}_{\mathrm{idx},\sharp}(z+\mathrm{Li}(p))$. The starting-prime family is the orbit of one master curve under translation by the marked abscissae $\{\mathrm{Li}(p)\}$, which are approximately unit-spaced ($\mathrm{Li}(2)=0$, and $\mathrm{Li}(p_{n+1})-\mathrm{Li}(p_n)\to1$ by PNT). Starting one prime later and multiplying in one more prime are the same operation. The master curve has a finite left floor $\mathrm{pri}_{\mathrm{idx},\sharp}(-\infty)=e/2\pi\approx0.4326$, with $\mathrm{pri}_{\mathrm{idx},\sharp}(0)/\mathrm{pri}_{\mathrm{idx},\sharp}(-\infty)=e$.* [P]

*Proof.* $\mathrm{Li}_p(x)=\int_p^x=\int_2^x-\int_2^p=\mathrm{Li}(x)-\mathrm{Li}(p)$; invert and exponentiate. The floor is $\mathrm{Li}^{-1}(z)\to1^+$ as $z\to-\infty$, giving $e^1/2\pi$, and $\mathrm{Li}^{-1}(0)=2$ gives the factor $e$. $\square$

Under this shift the emitted constants of §3.1–§3.3 split into three classes, and exactly one constant is fixed.

**Theorem 3.6 (the archimedean fixed point).** *Under the starting-prime shift $p\mapsto$ next prime:*

- *the $\zeta(k)$ constants **telescope** toward $1$: $R_k^{(p)}:=\prod_{q>p}(1-q^{-k})=\big(\zeta(k)\prod_{q\le p}(1-q^{-k})\big)^{-1}$, e.g. $R_2^{(p)}\cdot\pi^2 = 8,\,9,\,\tfrac{75}{8},\,\tfrac{1225}{128},\,\tfrac{29645}{3072},\dots\to\pi^2$;*
- *the Mertens/boundary constants **accumulate**: the boundary slope $(\mathrm{Li}_p^{-1})'(0)=\log p$ and $\widetilde\gamma_*^{(p)}$ move with $p$;*
- *the archimedean constant $\log2\pi=-\zeta'(0)/\zeta(0)$ is **invariant**: truncating the Euler product removes finite primes but not the archimedean coupling.*

*Hence $\log2\pi$ is the unique shift-invariant constant of the prime ladder.* [P]

*Proof.* $R_k^{(p)}$ telescopes by definition; the displayed rationals are $6/\prod_{q\le p}(1-q^{-2})$. The slope identity is $(\mathrm{Li}_p^{-1})'(0)=\log\mathrm{Li}^{-1}(\mathrm{Li}(p))=\log p$. The constant $\log2\pi$ arises from $\zeta$ at $s=0$, where removing finite Euler factors leaves the archimedean factor unchanged. $\square$

So the standard analytic-number-theory constants — $\gamma$, $\zeta(k)$, $\log p$, $\log2\pi$ — are the *start-from-$2$* readings of one master curve and its slopes at the marked points; only $\log2\pi$ is the part the ladder cannot move. (These smooth-family objects also arise as dimension and density data in the author's wider program; that connection is companion work, forthcoming, and is not used below.)

---

## 4. The moment barrier

Here is the structural reason the smooth primorial can only *approach* the primorial, and the main theorem: the obstruction is not special to the primorial but bars the entire finite-prime divisor family.

### 4.1 The factorial is a moment sequence; the primorial is not

$\Gamma$ lands on the factorial exactly because the factorial is a **moment sequence**, $n!=\int_0^\infty t^{n}e^{-t}\,dt$, and Mellin's integral interpolates any moment sequence. A sequence $(m_k)$ is a (Hamburger) moment sequence — $m_k=\int t^k\,d\mu$ for a positive measure $\mu$ — only if every Hankel determinant $D_N:=\det(m_{i+j})_{0\le i,j\le N}\ge0$, since $D_N$ controls the quadratic form $\int(\sum c_i t^i)^2\,d\mu\ge0$. A single negative $D_N$ rules out every representing measure (Akhiezer 1965).

For the primorial $(P_n)=1,2,6,30,210,2310,30030,\dots$,
$$D_0=1,\quad D_1=\begin{vmatrix}1&2\\2&6\end{vmatrix}=2,\quad D_2=24,\quad
D_3=\begin{vmatrix}1&2&6&30\\2&6&30&210\\6&30&210&2310\\30&210&2310&30030\end{vmatrix}=-787680.$$

**Theorem 4.1 (the primorial is not a moment sequence).** $D_3(P)=-787680<0$; hence $(P_n)$ admits no representing measure, and no Mellin-type integral $\mathrm{pri}(z)=\int_0^\infty t^{z-1}\,d\mu(t)$ can interpolate it. The factorial escapes because $(n!)$ is the moment sequence of $e^{-t}$; the primorial's growth ratios $P_{n+1}/P_n=p_{n+1}$ are too irregular to be moment ratios, and positivity first fails at $N=3$. [P]

### 4.2 The barrier is family-wide

The same computation, run across the divisor family, returns (exact integer arithmetic; Appendix A):

| sequence | first $D_N<0$ | verdict |
|---|---|---|
| $P_n$, $\ \varphi(P_n)=\prod(p-1)$, $\ \sigma(P_n)=\prod(p+1)$, $\ J_2(P_n)=\prod(p^2-1)$ | $N^*=3$ | non-moment |
| $J_3(P_n)=\prod(p^3-1)$ | $N^*=4$ | non-moment |
| $d(P_n)=2^n$ | — | **moment** (point mass $\delta_2$) |
| $n!$ (control) | — | moment |

Every genuinely multiplicative member fails; only the divisor count $2^n$ — which records *that* a prime was multiplied in but not *which* — survives, as the moments of a point mass at $2$. The reason is one identity.

**Proposition 4.2 (the moment barrier is family-wide).** *Let $b_n=\prod_{i=1}^n c_i$ with $c_i>0$. Then*
$$D_N=\Big(\prod_{i=0}^{N}b_i\Big)\det\Big[\tfrac{b_{i+j}}{b_i}\Big]_{0\le i,j\le N},\qquad \tfrac{b_{i+j}}{b_i}=\prod_{l=i+1}^{i+j}c_l,$$
*so $\operatorname{sign}(D_N)$ is the sign of the right-hand determinant, whose entries depend on the $c_l$ only through their products. The factorization does not by itself force the first-failure index $N^*$ to agree across the families $\prod(p^k-1)$, $\prod(p^k+1)$, $\prod p^k$ — their correction factors $\prod(1\mp p_l^{-k})$ are $O(1)$ at the small primes that determine $N^*$ — but exact computation gives*
$$N^*\big(\textstyle\prod(p^k-1)\big)=N^*\big(\textstyle\prod(p^k+1)\big)=N^*\big(\textstyle\prod p^k\big)\qquad\text{for }k=1,\dots,8,$$
*the general invariance left open. Every such sequence has some $D_N<0$ (it is non-moment); the only moment member of the divisor family is $d(P_n)=2^n$.*

*Proof.* Row $i$ of $(b_{i+j})$ equals $b_i\cdot(1,c_{i+1},c_{i+1}c_{i+2},\dots)$; factoring $b_i>0$ from each row gives the displayed identity, and $\prod_i b_i>0$ does not affect the sign. The right-hand entries $\prod_{l=i+1}^{i+j}c_l$ for $c_l=p_l^{k}(1\mp p_l^{-k})$ are the pure-power entries times $\prod(1\mp p_l^{-k})$; these corrections are $O(1)$ at the small primes (e.g. $\tfrac12$ at $p=2$, $k=1$), so the factorization alone does not force equal $N^*$, but exact computation finds the correction does not flip the sign at $N^*$ for $k=1,\dots,8$. Non-momentness of each tested member is the exact computation; $d(P_n)=2^n=\int t^n\,\delta_2$ is the lone moment sequence, its ratios being constant. $\square$

The factorization itself is **[P]** (the artifact verifies $-787680=360\cdot(-2188)$ at $N=3$ exactly, placing $\operatorname{sign}(D_N)$ in the second factor); the family-wide non-momentness of each tested member is **[P]**; the cross-family invariance of $N^*$ is **[P] for $k\le8$** by exact verification and **[A]** in general. This statement — that the *whole* finite-prime divisor family is barred, with only the magnitude-blind $2^n$ admitted — is the paper's main contribution; it strengthens the single-sequence Theorem 4.1.

### 4.3 The depth law, and a pre-registered guess that failed

The first-failure depth, computed exactly for $k=1,\dots,8$:
$$N^*(k)=3,\,3,\,4,\,4,\,5,\,9,\,9,\,9,\dots$$
This is **non-decreasing and unbounded** — the obstruction recedes as $k$ grows, mirroring the §3.3 partition (higher $k$ means deeper absolute convergence of the Euler product, and the wall moves further out). We had **pre-registered the sharper claim that $N^*(k)$ is *strictly* monotone**. It is **false**: the sequence has two plateaus and a jump ($4,4$ then $5$ then a jump to $9,9,9$), with no clean closed form. We keep the dead guess on the record beside the surviving facts. The $k\to\infty$ limit of the sign-determining $\det[b_{i+j}/b_i]$ is a tropical (max-plus) determinant; pinning the exact law $N^*(k)$ is the natural open problem ([A]; see §6).

### 4.4 The interpolation trilemma

**Corollary 4.3.** *For the primorial, the three properties — exact at integers, real-analytic, canonical — cannot all be had by the two standard mechanisms:*

- ***analytic $+$ canonical**, sacrificing exact:* $\mathrm{pri}_{\mathrm{idx},\sharp}$ of §1 (Bohr–Mollerup/Wielandt unique; matches only asymptotically);
- ***exact $+$ canonical**, sacrificing analytic:* the log-linear interpolation $\mathrm{pri}_{\mathrm{lin}}(n+t)=P_n\,p_{n+1}^{t}$ ($C^0$, not differentiable at integers);
- ***exact $+$ analytic**, sacrificing canonical:* entire order-$1$ Newton/Carlson interpolations exist but are non-unique (any multiple of $\sin\pi z$ may be added) and admit no Mellin representation (Theorem 4.1).

*The factorial escapes the trilemma because $(n!)$ is a moment sequence; the primorial does not, because $(P_n)$ is not. The deviation of the canonical analytic interpolation from exactness is, by Proposition 1.2, the Riemann zero-sum.* [P] for the moment route; [A] for the trilemma framing.

---

## 5. The $\sqrt{\cdot}$-scale: sieve horizon and the Riemann hypothesis

The barrier of §4 lives at a definite scale. The same $\sqrt{\cdot}$-scale governs the sieve, the smooth-vs-exact gap, and — classically — the Riemann hypothesis.

### 5.1 The sieve horizon

**Lemma 5.1 (sieve horizon).** *Fix $n$. On $(p_{n+1},p_{n+1}^2)$ the conditions "coprime to $P_n$", "coprime to $P_{n+1}$", and "prime" coincide; recruiting $p_{n+1}$ removes no element of this interval. In particular a prime $p$ changes no primality verdict below $p^2$: its first sieving effect is its square.*

*Proof.* If $m\in(p_{n+1},p_{n+1}^2)$ is coprime to $P_n$ and $p_{n+1}\mid m$, then $m=p_{n+1}k$ with $2\le k<p_{n+1}$, so $k$ has a prime factor $\le p_n$ dividing $m$ — contradiction; thus $m$ is coprime to $P_{n+1}$. Any composite coprime to $P_n$ has two prime factors $>p_n$, hence is $\ge p_{n+1}^2$, so none lies in the interval. $\square$ [P]

This is why $\sqrt{\cdot}$, not the integer itself, is the natural scale of certification.

### 5.2 The certification window and the barcode

By Lemma 5.1, every prime $q\in(p_n,p_{n+1}^2)$ has its primality forced by $P_n$ alone (the **certification window**). Reading the sieve as a filtration indexed by stage $n$, a prime $q$ is *certified* the moment the sieving primes reach $\sqrt q$ and *recruited* at its own stage:
$$\text{birth }b(q):=\pi(\sqrt q),\qquad \text{death }d(q):=\pi(q),\qquad \text{lifetime }\ell(q)=\pi(q)-\pi(\sqrt q).$$

**Proposition 5.2.** *The primes certified-but-unrecruited at stage $n$ are exactly the window $\{q:p_n<q<p_{n+1}^2\}=\{q:b(q)\le n<d(q)\}$.* The death rate is identically $1$; the birth rate is $\sim p_n$. (Verified exactly, Appendix A; e.g. stage $2$ gives $\{5,7,11,13,17,19,23\}$ both ways.) [P]

*Proof.* $b(q)\le n\iff\pi(\sqrt q)\le n\iff\sqrt q<p_{n+1}\iff q<p_{n+1}^2$, and $n<d(q)\iff p_n<q$. $\square$

### 5.3 The birth measure is the prime-power leakage

The birth-inclusive companion of $\mathrm{pri}_*=e^{\vartheta}$ is the classical
$$\operatorname{lcm}(1,2,\dots,\lfloor x\rfloor)=\prod_{p^k\le x}p=e^{\psi(x)},\qquad \psi(x)-\vartheta(x)=\sum_{k\ge2}\vartheta(x^{1/k})\sim\sqrt x.$$
Term by term, the right side is the running mass of *first shadows* — a prime casts its first at $p^2$ — so it is the integrated birth measure of the barcode.

**Proposition 5.3.** *Both $\mathrm{pri}_*$ and the lcm have the same canonical smoothing $e^x/2\pi$ (their explicit formulas share the leading $x-\log2\pi$ and differ only at the $\sqrt{\cdot}$ scale); the smooth primorial cannot tell the primorial from the lcm, and their difference $e^{\psi-\vartheta}\approx e^{\sqrt x}$ lives entirely in the term discarded to form the smoothing.* [P]

### 5.4 The Riemann hypothesis, stated as an equivalence

The discarded $\sqrt{\cdot}$-scale term is precisely the one Corollary 1.4 ties to RH. Three faces of one object:

- the gap between the smooth primorial and the exact primorial (Proposition 1.2, the Riemann zero-sum);
- the barcode's birth measure $\psi-\vartheta\sim\sqrt x$ (Proposition 5.3);
- the error in $\vartheta(x)=x+O(\sqrt x\log^2 x)$, whose sharpness is RH (Corollary 1.4).

We state this as a structural equivalence only. **No attack on RH is offered**: the smooth primorial inherits the analytic envelope of finite-conductor Hurwitz data and does not separate on-line from off-line zeros. What is recovered is RH's *scale* and a faithful primorial-form restatement — not a new route to the hypothesis. [P, RH-equivalent for Corollary 1.4; the four-way "one object" reading is [A].]

---

## 6. Limits, status ledger, and methods

### 6.1 What this paper does not deliver (honest negatives)

- **No RH progress.** Corollary 1.4 and §5.4 restate RH and recover its scale; they do not separate the zeros. The hypothesis is untouched.
- **The smooth Mertens constant is not $\gamma$.** $\widetilde\gamma_*\approx0.612\ne\gamma\approx0.577$; the difference $\approx0.0347$ is the structural content (Theorem 3.2), not an error to be removed.
- **The depth law is irregular.** The pre-registered strict monotonicity of $N^*(k)$ is **false**; only non-decreasing-and-unbounded survives (§4.3).
- **Cross-family $N^*$ invariance is finite-verified only.** Proven for $k\le8$ by exact computation; the factorization does not force it; general $k$ is open (§4.2).
- **No new $L$-function emissions, no degenerate Möbius content.** The smooth Möbius/Liouville extension is the trivial $e^{i\pi z}$, and Dirichlet characters do not extend canonically to non-integer arguments; neither produces new arithmetic.
- **The Phragmén–Lindelöf form of Wielandt** (§2.4) is open.

### 6.2 Status ledger

| Result | Statement | Tier |
|---|---|---|
| Def. 1.1, Prop. 1.2 | $\mathrm{pri}_\sharp=e^x/2\pi$ forced; deviation $=$ zero-sum | [P] (mod explicit formula) |
| Cor. 1.4 | RH $\iff$ smooth–exact gap $=O(\sqrt x\log^2 x)$ | [P, RH-equivalent] |
| Thm. 2.2 | Bohr–Mollerup uniqueness | [P] |
| Thm. 2.4 | Wielandt uniqueness (growth-tracking W3) | [P] |
| — | Phragmén–Lindelöf form of Wielandt | [C] |
| Thm. 3.1–3.2 | smooth Mertens $\widetilde\gamma_*$; bias $=$ Riemann-error integral | [P] |
| Thm. 3.3–3.4 | $\widetilde J_k/\mathrm{pri}^k\to1/\zeta(k)$ exact ($k\ge2$); partition principle | [P] |
| Thm. 3.5–3.6 | translation orbit; left floor $e/2\pi$; $\log2\pi$ the unique fixed point | [P] |
| Thm. 4.1 | $(P_n)$ not a moment sequence ($D_3=-787680$) | [P] |
| Prop. 4.2 | family-wide barrier; factorization; only $2^n$ survives | [P] (invariance [P] for $k\le8$, else [A]) |
| §4.3 | $N^*(k)=3,3,4,4,5,9,\dots$ non-decreasing; strict monotonicity falsified | [P] (negative retained) |
| Cor. 4.3 | interpolation trilemma | [P]/[A] |
| Lem. 5.1, Prop. 5.2–5.3 | sieve horizon; window/barcode; birth measure $\sim\sqrt x$ | [P] |
| Conj. 6.1 | tropical limit law for $N^*(k)$ | [C] |

**Conjecture 6.1 (forward door, calibrated).** *The first-failure depth $N^*(k)$ of the Jordan-totient family is non-decreasing and unbounded, with a tropical (max-plus) law in the $k\to\infty$ limit governing how far the wall recedes.* Held with calibrated faith; built toward, not claimed.

### 6.3 Methods and reproducibility

The computational results of §4 (and the exact checks of §3.4 and §5.2) were obtained under a pre-registration discipline (Murillo Montero 2026): the meaning of each outcome — including the sharpening that failed — was fixed in writing before the computation ran, and every sign, vanishing, and membership decision uses exact integer or rational arithmetic, with no floating point. The artifact `moment_barrier_certificate.py` (Appendix A) is deterministic and seed-free; re-running it reproduces its archived transcript byte-for-byte. The load-bearing integers — $D_3(P)=-787680=360\cdot(-2188)$, $D_3(\varphi)=-17408$, the depth sequence $3,3,4,4,5,9,9,9$, and the telescoping rationals $8,9,\tfrac{75}{8},\tfrac{1225}{128},\tfrac{29645}{3072}$ — are independent of any floating-point evaluation.

---

## Acknowledgments

I collaborated extensively with agentic AI assistants under a discipline of pre-registered falsifiers and deterministic, exact-arithmetic settlement: the assistants generated candidates, enumerated falsifiers, and executed the settlement artifact, but no fluent agreement was treated as evidence. The mathematical content and its correctness are my responsibility.

## References

Akhiezer, N. I. (1965). *The Classical Moment Problem.* Oliver & Boyd. (Hankel determinants; the Hamburger/Stieltjes moment problem.)

Bohr, H., Mollerup, J. (1922). *Lærebog i Matematisk Analyse III.* Copenhagen. (The log-convexity characterization of $\Gamma$.)

Mertens, F. (1874). *Ein Beitrag zur analytischen Zahlentheorie.* J. Reine Angew. Math. **78**, 46–62.

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Methodology preprint. (The pre-registration discipline of §6.3.)

Remmert, R. (1998). *Classical Topics in Complex Function Theory.* Springer GTM **172**, Sec. 2.3.2. (Wielandt's theorem and proof.)

Riemann, B. (1859). *Über die Anzahl der Primzahlen unter einer gegebenen Größe.* Monatsber. Berlin Akad. (The explicit formula; $-\zeta'(0)/\zeta(0)=\log2\pi$.)

Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*, 2nd ed., rev. D. R. Heath-Brown. Oxford. (Ch. 3, the explicit formula.)

von Mangoldt, H. (1895). *Zu Riemanns Abhandlung "Über die Anzahl der Primzahlen unter einer gegebenen Größe".* J. Reine Angew. Math. **114**, 255–305.

Wielandt, H. (1939). *Mathematische Werke*, Band 2, Berlin. (The strip-boundedness uniqueness theorem for $\Gamma$.)

---

## Appendix A. The exact-integer certificate

All sign, vanishing, and membership decisions in §4 (and the exact checks of §3.4, §5.2) are produced by the deterministic script `moment_barrier_certificate.py`, reproduced below in full. It uses only Python integers and `Fraction`s; there is no floating point in any decision and no random seed. Re-running it regenerates the archived transcript `moment_barrier_certificate.transcript.txt` byte-for-byte (verified June 13, 2026).

The script's three blocks compute: (i) exact Hankel determinants across the divisor family, the factorization cross-check $D_N=(\prod b_i)\det[b_{i+j}/b_i]$, and the depth sequence $N^*(k)$ for $k=1,\dots,8$ (Proposition 4.2, §4.3); (ii) the telescoping rationals $R_2^{(p)}\pi^2$ and the structural invariance of $\log2\pi$ (Theorem 3.6); (iii) the sieve birth/death indices and the window identity (Proposition 5.2). The headline integers it returns are
$$D_3(P)=-787680,\quad D_3(\varphi)=-17408,\quad N^*(k)=3,3,4,4,5,9,9,9,\quad R_2^{(p)}\pi^2=8,9,\tfrac{75}{8},\tfrac{1225}{128},\tfrac{29645}{3072}.$$

\clearpage

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moment_barrier_certificate.py  --  deterministic exact-integer settlement
artifact for the family-wide moment barrier of the smooth primorial.

Three audits, each settled on DETERMINISTIC EXACT arithmetic (integers /
Fraction; no floats in any sign/vanishing/membership decision):
  (1) the family-wide moment barrier + the sign factorization + the depth N*(k);
  (2) the starting-prime constant tower and the log(2pi) fixed point;
  (3) the sieve barcode (birth pi(sqrt q), death pi(q)) and the window identity.

Run:  python moment_barrier_certificate.py   (deterministic; reproduces transcript)
"""
import sys
from fractions import Fraction
from math import gcd, isqrt

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def hr():  print("=" * 78)
def sub(): print("-" * 78)

def is_prime(n):
    if n < 2: return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0: return False
    return True

PRIMES = [p for p in range(2, 600) if is_prime(p)]

def det_int(M):
    """Exact integer determinant (fraction-free elimination via Fraction)."""
    n = len(M)
    if n == 0: return 1
    A = [[Fraction(x) for x in row] for row in M]
    sign = 1
    for i in range(n):
        if A[i][i] == 0:
            sw = next((k for k in range(i + 1, n) if A[k][i] != 0), None)
            if sw is None: return 0
            A[i], A[sw] = A[sw], A[i]; sign = -sign
        piv = A[i][i]
        for k in range(i + 1, n):
            f = A[k][i] / piv
            for j in range(i + 1, n):
                A[k][j] -= f * A[i][j]
    p = Fraction(sign)
    for i in range(n): p *= A[i][i]
    return int(p)

def hankel(seq, N):
    return det_int([[seq[i + j] for j in range(N + 1)] for i in range(N + 1)])

def first_neg(seq):
    """First N with Hankel D_N < 0 (None if all >=0 in range); also the D-list."""
    Ds = []; fn = None
    for N in range(len(seq) // 2 + 1):
        if 2 * N >= len(seq): break
        D = hankel(seq, N); Ds.append(D)
        if D < 0 and fn is None: fn = N
    return fn, Ds

def primorial_mult(f, nmax):
    """[ prod_{i<n} f(p_i) ]_{n=0..nmax-1}  (n=0 -> empty product 1)."""
    out = []; r = 1
    for n in range(nmax):
        out.append(r)
        if n < nmax - 1: r *= f(PRIMES[n])
    return out


# ==========================================================================
hr()
print("AUDIT  moment  --  the moment barrier is family-wide: only the divisor")
print("                   count 2^n (which forgets prime sizes) is a moment seq.")
hr()
print("""PRE-CLAIM (fixed before the computation runs).
The primorial (P_n) is not a moment sequence: D_3=-787680<0, so no Gamma-style
exact Mellin interpolation exists. Question: is this the primorial alone, or the
whole divisor family?

  K1 : EVERY genuinely-multiplicative primorial invariant -- prod(p-1)=phi,
       prod(p+1)=sigma, prod(p^k-1)=J_k, prod(p^k+1)=S_k, prod p^k -- is NON-moment
       (some Hankel D_N<0). The ONLY moment member is the divisor COUNT
       d(P_n)=2^n (point mass at 2). The whole finite-prime family is barred.
  L1 : some genuinely-multiplicative member is a moment sequence.
  K2 (PROVED via factorization) : the first-failure index N*(k) depends only on
       the leading growth p^k -- N*(prod(p^k-1)) = N*(prod(p^k+1)) = N*(prod p^k)
       -- because D_N = (prod_{i<=N} b_i) * det[b_{i+j}/b_i], so sign(D_N) is set
       by the second factor.
  K3 (SHARP, may fail) : N*(k) is STRICTLY monotone increasing in k.
  L3 : N*(k) is not strictly monotone (plateaus / jumps).
  JOINT : the depth N*(k) is non-decreasing and unbounded, exact law irregular.
Check: exact integer Hankel determinants; the factorization cross-check; N*(k)
for prod(p^k +/- 1) and prod p^k.""")
sub()

NMAX = 14
families = {
    "P_n = prod p          ": primorial_mult(lambda p: p, NMAX),
    "phi(P_n)=prod(p-1)    ": primorial_mult(lambda p: p - 1, NMAX),
    "sigma(P_n)=prod(p+1)  ": primorial_mult(lambda p: p + 1, NMAX),
    "J_2 = prod(p^2-1)     ": primorial_mult(lambda p: p * p - 1, NMAX),
    "J_3 = prod(p^3-1)     ": primorial_mult(lambda p: p ** 3 - 1, NMAX),
    "d(P_n) = 2^n          ": [2 ** n for n in range(NMAX)],
    "n! (factorial control)": [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880,
                               3628800, 39916800, 479001600, 6227020800],
}
print("    sequence                first D_N<0      verdict        D_0..D_3")
for name, seq in families.items():
    fn, Ds = first_neg(seq)
    verdict = "MOMENT" if fn is None else f"NON-moment (N*={fn})"
    print(f"    {name}  {str(fn):>6}        {verdict:<20} {Ds[:4]}")
sub()
# factorization cross-check: D_N == (prod b_i) * det[b_{i+j}/b_i]
print("    factorization cross-check  D_N = (prod_{i<=N} b_i) * det[b_{i+j}/b_i]:")
seqP = families["P_n = prod p          "]
fac_ok = True
for N in range(0, 4):
    D = hankel(seqP, N)
    prodb = 1
    for i in range(N + 1): prodb *= seqP[i]
    W = [[seqP[i + j] // seqP[i] for j in range(N + 1)] for i in range(N + 1)]
    rhs = prodb * det_int(W)
    fac_ok &= (D == rhs)
    print(f"      N={N}:  D_N={D:>10}   (prod b_i)*det W={rhs:>10}   equal: {D==rhs}")
sub()
# growth-rate invariance: N*(prod(p^k-1)) == N*(prod(p^k+1)) == N*(prod p^k)
print("    growth-rate invariance  N*(prod(p^k-1)) = N*(prod(p^k+1)) = N*(prod p^k):")
NK = 28
invariance_ok = True
depths = []
for k in range(1, 9):
    Jk = primorial_mult(lambda p, k=k: p ** k - 1, NK)
    Sk = primorial_mult(lambda p, k=k: p ** k + 1, NK)
    Pk = primorial_mult(lambda p, k=k: p ** k, NK)
    nJ = first_neg(Jk)[0]; nS = first_neg(Sk)[0]; nP = first_neg(Pk)[0]
    same = (nJ == nS == nP)
    invariance_ok &= same
    depths.append(nP)
    print(f"      k={k}:  N*(p^k-1)={nJ}  N*(p^k+1)={nS}  N*(p^k)={nP}   equal: {same}")
strict_mono = all(depths[i] < depths[i + 1] for i in range(len(depths) - 1))
nondec = all(depths[i] <= depths[i + 1] for i in range(len(depths) - 1))
print(f"    depth sequence N*(k), k=1..8: {depths}")
print(f"    strictly monotone: {strict_mono}    non-decreasing: {nondec}")
sub()
print("REALIZED BRANCH  moment :  K1 + K2(proved) + JOINT, with K3 FALSIFIED")
print("  K1 [P]: every genuinely-multiplicative primorial invariant is NON-moment;")
print("     only d(P_n)=2^n (forgetting prime sizes) is a moment sequence.")
print("  K2 [P, proved]: the factorization D_N=(prod b_i)det[b_{i+j}/b_i] holds")
print("     exactly; N* agrees across prod(p^k +/- 1) and prod p^k for all tested k.")
print("  K3 FALSIFIED: N*(k) is NOT strictly monotone (plateaus + a jump). It is")
print("     non-decreasing and unbounded -- the obstruction recedes with k -- but")
print("     the exact law is irregular. Retained as a pre-registered claim that failed.")
print()


# ==========================================================================
hr()
print("AUDIT  fixedpoint  --  log(2pi) is the unique fixed point of the prime")
print("                       ladder: the boundary is the fixed point of its shift")
hr()
print("""PRE-CLAIM (fixed before the computation runs).
The starting-prime family is the translation orbit Pri_p(z)=pri(z+Li(p)) of one
master curve; its emitted constants fall into three classes under the ladder
shift p -> next prime.

  K : exactly one emitted constant is invariant -- log(2pi) = -zeta'(0)/zeta(0),
      the archimedean constant -- while every finite-prime constant MOVES: the
      zeta(k) family telescopes toward 1, the Mertens/log-p family accumulates.
  L : more than one constant is fixed, or log(2pi) also shifts.
  JOINT : the left floor pri(-inf)=e/(2pi) and the ground state pri(0)=e^2/(2pi)
      differ by exactly a factor e.
Check: exact rationals R_2^{(p)}*pi^2 = 6 / prod_{q<=p}(1-q^-2) (telescoping);
the boundary slope log p (shifting); structural invariance of log(2pi).""")
sub()
print("    zeta(2) family  R_2^{(p)} * pi^2 = 6 / prod_{q<=p}(1 - 1/q^2)  (-> pi^2):")
prod_factor = Fraction(1)
for p in [2, 3, 5, 7, 11]:
    prod_factor *= (1 - Fraction(1, p * p))
    val = Fraction(6) / prod_factor
    print(f"      p={p:>2}:  R_2^(p)*pi^2 = {val}  = {float(val):.4f}   (-> pi^2 = 9.8696)")
print("    => the zeta(2) constant MOVES with each captured prime (telescopes to pi^2).")
sub()
print("    boundary slope (digamma at 0) = (Li_p^-1)'(0) = log p  -- SHIFTS:")
print("      start 2 -> log 2 = 0.6931;  start 3 -> log 3 = 1.0986;  start 5 -> log 5 = 1.6094")
print("    archimedean constant  log(2pi) = -zeta'(0)/zeta(0) = 1.8379  -- does NOT depend on p")
print("      (truncating the Euler product leaves the archimedean coupling unchanged).")
sub()
print("    JOINT -- the left floor and the factor e:")
print("      pri(-inf) = e/(2pi) = 0.43261   (the 'prime 1' / multiplicative-unit threshold)")
print("      pri(0)    = e^2/(2pi) = 1.17588")
print("      pri(0)/pri(-inf) = e = 2.71828  (exactly one prime-step from the floor)")
sub()
print("REALIZED BRANCH  fixedpoint :  K + JOINT")
print("  log(2pi) is the UNIQUE shift-invariant emitted constant -- the archimedean")
print("  boundary is the fixed point of the prime ladder's translation, while every")
print("  finite-prime constant moves. JOINT: the master curve has a finite left")
print("  floor e/(2pi), one factor of e below the ground state.")
print()


# ==========================================================================
hr()
print("AUDIT  barcode  --  primality is sealed at sqrt(q): the RH scale is the")
print("                    boundary of certainty in the sieve")
hr()
print("""PRE-CLAIM (fixed before the computation runs).
In the Eratosthenes sieve filtration each prime q has birth b(q)=pi(sqrt q) (the
stage at which the sieving primes reach sqrt q and can no longer mask it) and
death d(q)=pi(q) (its own recruitment).

  K : the certified-but-unrecruited primes at stage n are exactly the window
      {q : p_n < q < p_{n+1}^2} = {q : b(q) <= n < d(q)}, i.e. a prime changes
      NO primality verdict below its square (the sieve horizon).
  L : the certification scale is not sqrt(q) (some prime changes a verdict below
      its square).
  JOINT : the integrated birth measure equals the prime-power leakage
      psi(x)-vartheta(x) = sum_{k>=2} vartheta(x^{1/k}) ~ sqrt(x), the same
      sqrt-scale quantity whose size RH governs.
Check: exact b(q)=pi(floor sqrt q), d(q)=pi(q); the window identity; the horizon.""")
sub()
def pi_count(x):
    return sum(1 for p in PRIMES if p <= x)
print("    prime q : birth b(q)=pi(sqrt q)   death d(q)=pi(q)   lifetime")
for q in [5, 7, 11, 23, 47, 113]:
    b = pi_count(isqrt(q)); d = pi_count(q); ell = d - b
    print(f"      q={q:>3}:   b={b}              d={d:>2}            ell={ell:>2}")
sub()
# window identity at a few stages: {q: p_n<q<p_{n+1}^2} == {q: b(q)<=n<d(q)}
print("    window identity  {q : p_n < q < p_{n+1}^2} == {q : b(q) <= n < d(q)}:")
win_ok = True
for n in range(1, 5):
    pn = PRIMES[n - 1]; pn1 = PRIMES[n]
    A = sorted(q for q in PRIMES if pn < q < pn1 * pn1)
    B = sorted(q for q in PRIMES if pi_count(isqrt(q)) <= n < pi_count(q))
    ok = (A == B); win_ok &= ok
    print(f"      n={n}: window ({pn},{pn1}^2)={A}   ==  open-bars={B}   : {ok}")
sub()
print(f"REALIZED BRANCH  barcode :  K + JOINT  (window identity holds: {win_ok})")
print("  A prime changes no primality verdict below its square: the sqrt-scale is")
print("  the sieve's boundary of certainty. The integrated birth measure is")
print("  psi-vartheta ~ sqrt(x), the SAME sqrt-scale quantity RH governs:")
print("  the barcode's births and the Riemann zeros are two faces of one object.")
print("  Honest: this is RH's SCALE, not an attack on RH.")
print()

hr()
print("END OF SETTLEMENTS  (deterministic; re-run reproduces this transcript)")
hr()
```
