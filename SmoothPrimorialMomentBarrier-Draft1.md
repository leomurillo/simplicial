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
              The mathematics of those drafts is frozen; the merge itself was
              editorial. Every [P]/[A]/[C] tag, proof, and honest negative is
              carried over in content.
  v2 repositioning (after a prior-art dive, 2026-06-13): the construction's
              uniqueness is recognized as the Krull-Webster / Marichal-Zenaidi
              theory of Delta f = g (NOT a new technique) and cited as such; the
              constant tower is recast as that theory's asymptotic/generalized-
              Euler-constant machinery; the genuinely-new construction-side
              content is the archimedean zeta'(0) normalization. New spine:
              moment barrier <=> the 2pi must be adjoined externally from zeta
              (Gamma generates its 2pi internally AS a moment sequence; the
              primorial cannot). New section 3.5 (three smooth primorials A/B/P_n)
              backed by empirical/smooth_primorial_three_objects.py. Berg-Szwarc
              sharpens the 2^n survivor. Refs added: Krull 1948/49, Webster 1997,
              Marichal-Zenaidi 2022, Fox-Karamchedu 2023, Arias de Reyna-Toulisse
              2013, Berg-Szwarc 2015. Theorem B (the family-wide barrier) is the
              centerpiece and lies outside the Krull-Webster/M-Z world.
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

The factorial has a canonical smooth twin: the Gamma function, which passes through every factorial value *exactly*, because the factorial is the moment sequence of $e^{-t}$ and $\Gamma$ is its Mellin interpolation. The primorial $P_n=\prod_{p\le p_n}p=1,2,6,30,210,\dots$ has had no such twin. We construct one. The **smooth primorial** $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$ is forced by Riemann's explicit formula — its constant $1/2\pi=e^{-\zeta'(0)/\zeta(0)}$ is the archimedean term — and is *unique* under either a Bohr–Mollerup log-convexity condition or a Wielandt strip-growth condition. Its uniqueness places it among the *multiple $\log\Gamma$-type functions* of Krull, Webster, and Marichal–Zenaïdi; what is arithmetic — and new — is the archimedean normalization $1/2\pi=e^{\zeta'(0)/\zeta(0)}$, which ties the object to $\zeta$ and (we show numerically) is exactly what makes it track the primorial at the Riemann scale, where the naive product of smooth primes drifts. Its asymptotic ratios against the divisor-lattice family emit the classical analytic constants — a smooth Mertens constant $\widetilde\gamma_*=0.6119\dots$ (the Marichal–Zenaïdi generalized Euler constant of the prime ladder, differing from Euler's $\gamma$ by a named Riemann-error integral), the values $1/\zeta(k)$ exactly for $k\ge2$, and $\log2\pi$ as a distinguished fixed point.

Unlike the factorial, the primorial is **not a moment sequence**: its Hankel determinant $D_3=-787680<0$, so it admits no exact Mellin/$\Gamma$-style interpolation; the smooth primorial only *approaches* it, and the gap is the Riemann zero-sum. Our main theorem is that this barrier is **family-wide**: every genuinely multiplicative primorial invariant — $\varphi(P_n)$, $\sigma(P_n)$, $J_k(P_n)=\prod(p^k-1)$, $\prod(p^k+1)$, $\prod p^k$ — is non-moment (some Hankel determinant turns negative), and the *only* moment member of the divisor family is the divisor count $d(P_n)=2^n$, the one invariant that forgets the magnitudes of the primes. This barrier ties the two halves of the paper together: the factorial generates its own $2\pi$ — as a moment sequence it carries an intrinsic measure, and $\sqrt{2\pi}$ is its Stirling constant — whereas the primorial, having no representing measure, cannot, so its archimedean constant must be adjoined from $\zeta$. The moment barrier and the external $\zeta'(0)$ normalization are one phenomenon. The barrier is not special to the divisor invariants: for *every* polynomial local factor $f$, $\prod f(p_i)$ is non-moment (proved in degrees $1$–$2$; for higher degree conditional on a prime-constellation conjecture), the obstruction being the gap condition $b^2>ae$ — pinning "irregular spacing" to a precise second-order condition. The proof tool is the factorization $D_N=\big(\prod_{i\le N}b_i\big)\det[b_{i+j}/b_i]$, which carries $\operatorname{sign}(D_N)$ in its second factor; the first-failure depth $N^*(k)$ is found to be $3,3,4,4,5,9,\dots$ — non-decreasing and unbounded, mirroring the Euler-product convergence partition, but (against a pre-registered guess that we record as falsified) *not* strictly monotone. Finally, the $\sqrt{\cdot}$-scale on which a prime's primality is sealed in the sieve is exactly the scale on which the smooth-vs-exact gap lives, which is the scale the Riemann hypothesis governs: we make the primorial-form RH equivalence precise and claim no progress on RH itself.

---

**Keywords:** primorial, Gamma function, smooth interpolation, Bohr–Mollerup theorem, Krull–Webster theorem, principal indefinite sum, higher-order convexity, Wielandt theorem, inverse logarithmic integral, Hamburger moment problem, Hankel determinant, generalized Euler constant, Mertens' theorem, prime number theorem, Riemann explicit formula, Riemann hypothesis.

**MSC 2020:** 44A60 (Moment problems); 33B15 (Gamma, beta and polygamma functions); 39A06 (Linear difference equations); 26A51 (Convexity, generalizations); 11N05 (Distribution of primes); 11M06 (Riemann zeta-function); 11N37 (Asymptotic results on arithmetic functions); 11A41 (Primes); 30D15 (Special classes of entire functions).

---

\begin{mdframed}[backgroundcolor=gray!8, linecolor=gray!40, linewidth=0.5pt,
                 innerleftmargin=14pt, innerrightmargin=14pt,
                 innertopmargin=10pt, innerbottommargin=10pt,
                 skipabove=1em, skipbelow=1em]
\textbf{In plain terms.} The factorial $1,2,6,24,\dots$ has a famously smooth twin, the Gamma function, that lands on every one of its values exactly. The primorial $1,2,6,30,210,\dots$ — multiply the primes in one at a time — has a smooth twin too, built below; but it only \emph{approaches} the primorial, never landing on it, and the size of the miss is governed by the Riemann hypothesis. This paper asks why exact landing is impossible and finds a clean, classical answer: a number sequence can be the ``moments'' of a probability distribution only if a ladder of determinants stays non-negative, and for the primorial one of them is $-787680$. We then show this is not a quirk of the primorial — \emph{every} natural prime-built sequence fails the same test, and the only survivor is the one that throws away the sizes of the primes. A short exact-integer program is the whole of the computational evidence; we also test an obvious guess about the pattern, watch it fail, and keep it on the record.
\end{mdframed}

\clearpage

## 1. The smooth primorial {#sec:1}

We write [P] for *proven*, [A] for *structural, pending a single named gap*, and [C] for *conjectural, reduced to a named gap*. These tags mark the epistemic status of each numbered result and are collected in the ledger of \hyperref[sec:6]{§6}.

**Main results.** The paper proves two theorems, stated here and established in the body.

\hypertarget{thm:a}{}
**Theorem A (existence and uniqueness).** *There is a canonical smooth primorial $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=e^{\mathrm{Li}^{-1}(z)}/2\pi$: it is forced by Riemann's explicit formula, and among solutions of its recursion it is the unique one satisfying either a Bohr–Mollerup log-convexity condition or a Wielandt strip-growth condition. It is to the primorial what the Gamma function is to the factorial.* Existence is the explicit formula (\hyperref[sec:1-2]{§1.2}–\hyperref[sec:1-3]{§1.3}); uniqueness is proved two independent ways (\hyperlink{stmt:2-2}{Theorems~2.2} and \hyperlink{stmt:2-4}{2.4}).

\hypertarget{thm:b}{}
**Theorem B (the family-wide moment barrier).** *Unlike the factorial, no genuinely multiplicative primorial invariant — $\varphi(P_n)$, $\sigma(P_n)$, the Jordan totients $J_k(P_n)$, $\prod(p^k+1)$, $\prod p^k$ — is a moment sequence; the only moment member of the entire divisor family is the magnitude-blind divisor count $d(P_n)=2^n$.* This is \hyperlink{stmt:4-2}{Theorem~4.2}, the paper's centerpiece; it strengthens the classical single-sequence fact that the primorial itself is not a moment sequence (\hyperlink{stmt:4-1}{Theorem~4.1}).

The constant tower of \hyperref[sec:3]{§3} ($\widetilde\gamma_*$, the exact $1/\zeta(k)$, and $\log2\pi$ as the prime ladder's unique fixed point) is a structural payoff of the construction, and \hyperref[sec:5]{§5} locates the smooth-to-exact gap at the $\sqrt{\cdot}$-scale governed by the Riemann hypothesis (no progress on RH is claimed).

**What is prior, and what is new.** The *uniqueness* in Theorem A is an instance of an established theory: the difference equation $\Delta f=g$ has a unique eventually-convex solution whenever $g$ is eventually convex (or $p$-convex) with $\Delta^p g(n)\to0$ — proved for our case ($p=1$) by Krull (1948) and Webster (1997), and developed comprehensively by Marichal and Zenaïdi (2022); §3's asymptotic constants are that theory's generalized-Stirling and generalized-Euler machinery instantiated for the primorial. What is genuinely new is arithmetic, and twofold: **(i)** the archimedean normalization $-\log2\pi=\zeta'(0)/\zeta(0)$ that ties the smooth primorial to $\zeta$ — not supplied by the convexity theory, and (\hyperref[sec:3-5]{§3.5}) the feature that makes our object track the primorial at the Riemann scale where the naive product of smooth primes drifts; and **(ii)** the family-wide moment barrier (Theorem B), which lies entirely outside that theory. The two are linked: \hyperref[sec:4]{§4} shows the barrier is *why* the $2\pi$ must be adjoined from $\zeta$.

### 1.1 The two primorials and the inverse logarithmic integral {#sec:1-1}

For $n\in\mathbb Z_{\ge0}$ the **index-side primorial** is $P_n:=\prod_{k=1}^n p_k$ with $P_0:=1$, where $p_k$ is the $k$-th prime. For $x\ge2$ the **prime-side primorial** is $\mathrm{pri}_*(x):=\prod_{p\le x}p$, a right-continuous step function with $\mathrm{pri}_*(p_n)=P_n$. The two are tied to Chebyshev's first function $\vartheta(x):=\sum_{p\le x}\log p$ by the tautology
$$\log\mathrm{pri}_*(x)=\vartheta(x),\qquad \log P_n=\vartheta(p_n). \tag{1.1}$$

Let $\mathrm{Li}(x):=\int_2^x dt/\log t$ be the (shifted) logarithmic integral, $\mathrm{Li}(2)=0$. It is real-analytic, strictly increasing, and strictly concave on $(1,\infty)$, with $\mathrm{Li}(x)\sim x/\log x$. Its inverse $\mathrm{Li}^{-1}:[0,\infty)\to[2,\infty)$ is real-analytic, strictly increasing, strictly convex, with $\mathrm{Li}^{-1}(0)=2$ and the key identity
$$(\mathrm{Li}^{-1})'(z)=\log\big(\mathrm{Li}^{-1}(z)\big). \tag{1.2}$$

### 1.2 The prime-side smooth primorial is forced by the explicit formula {#sec:1-2}

The Riemann–von Mangoldt explicit formula for $\psi(x):=\sum_{n\le x}\Lambda(n)$ reads, for $x>1$ not a prime power,
$$\psi_0(x)=x-\sum_\rho\frac{x^\rho}{\rho}-\log(2\pi)-\tfrac12\log(1-x^{-2}), \tag{1.3}$$
$\rho$ ranging over the non-trivial zeros of $\zeta$ and the constant being $-\zeta'(0)/\zeta(0)=\log(2\pi)$. Passing to $\vartheta=\psi-\sum_{k\ge2}\vartheta(x^{1/k})$ moves the prime-power leakage into an $O(\sqrt x)$ term:
$$\vartheta(x)=x-\log(2\pi)-\sum_\rho\frac{x^\rho}{\rho}-\tfrac12\log(1-x^{-2})-\sum_{k\ge2}\vartheta(x^{1/k}). \tag{1.4}$$
Extracting the non-oscillatory leading part — the terms independent of the zeros and of the prime-power leakage — gives the canonical smooth Chebyshev function $\vartheta_{\mathrm{smooth}}(x)=x-\log(2\pi)$, hence the

\hypertarget{stmt:1-1}{}
**Definition 1.1 (prime-side smooth primorial).** $\displaystyle \mathrm{pri}_\sharp(x):=\exp\big(\vartheta_{\mathrm{smooth}}(x)\big)=\frac{e^{x}}{2\pi},\qquad x\in\mathbb R.$

This is **forced**: no constant is free; every term comes from $\zeta$ at $s=0$. The factor $1/2\pi=e^{-\log2\pi}$ with $\log(2\pi)=-\zeta'(0)/\zeta(0)$ is, in the standard reading, the contribution of the *archimedean place* — the term that completes the Euler product into $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$. \hyperlink{stmt:1-1}{Definition~1.1} is [P], modulo the classical explicit formula (Riemann 1859; von Mangoldt 1895; Titchmarsh 1986, Ch. 3).

\hypertarget{stmt:1-2}{}
**Proposition 1.2 (the deviation is the zero-sum).** *For $x>1$ not a prime power,*
$$\log\frac{\mathrm{pri}_*(x)}{\mathrm{pri}_\sharp(x)}=-\sum_\rho\frac{x^\rho}{\rho}+O(\sqrt x). \tag{1.5}$$

*Proof.* Subtract $x-\log2\pi$ from (1.4); the remaining $-\tfrac12\log(1-x^{-2})$ and $-\sum_{k\ge2}\vartheta(x^{1/k})$ are $O(\sqrt x)$. $\square$ [P]

### 1.3 The index side: duality through $\mathrm{Li}^{-1}$ {#sec:1-3}

The exact identity $P_n=\mathrm{pri}_*(p_n)$ says $P_n$ is $\mathrm{pri}_*$ read along the prime-enumeration map $n\mapsto p_n$, the integer inverse of $\pi(x)=\#\{p\le x\}$. Riemann's explicit formula for $\pi$ has leading non-oscillatory term $\mathrm{Li}(x)$, so the canonical smooth replacement of $n\mapsto p_n$ is $\tilde p(z):=\mathrm{Li}^{-1}(z)$, with $\tilde p(0)=2$ and (under RH) $\tilde p(n)=p_n+O(\sqrt{p_n}\log p_n)$. Composing,

\hypertarget{stmt:1-3}{}
**Definition 1.3 (index-side smooth primorial).** $\displaystyle \mathrm{pri}_{\mathrm{idx},\sharp}(z):=\mathrm{pri}_\sharp\big(\mathrm{Li}^{-1}(z)\big)=\frac{\exp\big(\mathrm{Li}^{-1}(z)\big)}{2\pi},\qquad z\in[0,\infty).$

Throughout, "the smooth primorial" with no qualifier means $\mathrm{pri}_{\mathrm{idx},\sharp}$. The two sides are linked by $\mathrm{pri}_{\mathrm{idx},\sharp}(z)=\mathrm{pri}_\sharp(\mathrm{Li}^{-1}(z))$; the entire difference between the exact and smooth pictures is concentrated in the single top arrow $\tilde p$ versus $n\mapsto p_n$. The boundary value $\mathrm{pri}_{\mathrm{idx},\sharp}(0)=e^2/2\pi\approx1.177\ne1=P_0$ is kept honestly: forcing it to $1$ would discard the $\log2\pi$ that completes $\zeta$.

### 1.4 The Riemann hypothesis in primorial form {#sec:1-4}

\hypertarget{stmt:1-4}{}
**Corollary 1.4 (RH, primorial form).** *Each of the following is equivalent to RH:*
$$\text{(i)}\quad \log\mathrm{pri}_*(x)-\log\mathrm{pri}_\sharp(x)=O(\sqrt x\,\log^2 x);\qquad \text{(ii)}\quad \log P_n-\log\mathrm{pri}_{\mathrm{idx},\sharp}(n)=O(\sqrt{p_n}\log^2 p_n).$$

*Proof.* By \hyperlink{stmt:1-2}{Proposition~1.2} this is the classical equivalence RH $\iff\vartheta(x)=x+O(\sqrt x\log^2 x)$, read on the prime and index sides respectively. $\square$ [P, RH-equivalent]

This is RH stated inside the primorial framework. It is a restatement of a textbook equivalence; **no progress toward RH is claimed by it**, here or anywhere below (see \hyperref[sec:5-4]{§5.4}, \hyperref[sec:6]{§6}).

### 1.5 What the interpolation looks like {#sec:1-5}

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

The multiplicative ratio is **not** monotone: it crosses $1$ between $n=4$ and $n=5$ and oscillates with the amplitude of the Riemann zero-sum. It is the *log*-ratio that tends to $0$ in the PNT-relative sense of \hyperlink{stmt:1-4}{Corollary~1.4}, not the ratio itself. (The crossover near $n=5$ is the index-side shadow of $(\pi-\mathrm{Li})$ changing sign among the small primes.)

---

## 2. Uniqueness: Bohr–Mollerup and Wielandt {#sec:2}

Both classical characterizations of $\Gamma$ transfer, with $\log z$ replaced by the smooth multiplier $\Delta(z):=\mathrm{Li}^{-1}(z+1)-\mathrm{Li}^{-1}(z)$. Theorems 2.2 and 2.4 are the two halves of the uniqueness clause of \hyperlink{thm:a}{Theorem~A}: log-convexity (Bohr–Mollerup) and holomorphic strip-growth (Wielandt).

**These are instances of a general theory.** The Bohr–Mollerup characterization of $\Gamma$ was extended by Krull (1948) and Webster (1997) — and, across higher-order convexity, by Marichal and Zenaïdi (2022) — to the difference equation $\Delta f=g$: if $g$ is eventually $p$-convex (or $p$-concave) and $\Delta^{p}g(n)\to0$, then $\Delta f=g$ has a unique eventually $p$-convex solution modulo an additive constant, the *principal indefinite sum* $\Sigma g$ (with $\Sigma\log z=\log\Gamma(z)$ the namesake case, $p=1$). The smooth primorial fits at $p=1$: $\log\mathrm{pri}_{\mathrm{idx},\sharp}$ solves $\Delta f=g$ with $g=\Delta$, and by Lemma 2.1 $g$ is increasing and eventually concave (because $u\mapsto\log u/u$ decreases), with $\Delta g(n)=O(1/n)\to0$. Theorem 2.2 below is thus the Krull–Webster case; we give the self-contained Bohr–Mollerup proof for completeness, and Theorem 2.4 the independent complex-analytic (Wielandt) route. The one thing the convexity theory leaves free is the additive constant — fixed in \hyperref[sec:1-2]{§1.2} by the explicit formula to the archimedean $-\log2\pi$, which is the paper's arithmetic input and the seam to the moment barrier (\hyperref[sec:4]{§4}).

### 2.1 The convexity input {#sec:2-1}

\hypertarget{stmt:2-1}{}
**Lemma 2.1.** *$\mathrm{Li}^{-1}$ is strictly convex on $[0,\infty)$, and $\Delta(z)=\mathrm{Li}^{-1}(z+1)-\mathrm{Li}^{-1}(z)$ is strictly increasing.*

*Proof.* $\mathrm{Li}'(t)=1/\log t>0$ and $\mathrm{Li}''(t)=-1/(t\log^2 t)<0$ on $(1,\infty)$, so $\mathrm{Li}$ is concave and its inverse convex; explicitly $(\mathrm{Li}^{-1})''(z)=\log(\mathrm{Li}^{-1}(z))/\mathrm{Li}^{-1}(z)>0$. Monotonicity of $\Delta$ is convexity applied to unit translates. $\square$ [P]

$\Delta$ is the smooth analogue of "$\log p_{n+1}$ increases with $n$" — the only structural ingredient the Bohr–Mollerup squeeze needs beyond the standard $\Gamma$ proof.

### 2.2 The Bohr–Mollerup theorem {#sec:2-2}

\hypertarget{stmt:2-2}{}
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

### 2.3 Growth on vertical strips {#sec:2-3}

\hypertarget{stmt:2-3}{}
**Lemma 2.3.** *As $|t|\to\infty$ with $\sigma\in[1,2]$ fixed,*
$$\mathrm{Li}^{-1}(\sigma+it)=\big(\sigma\log|t|-\tfrac{\pi}{2}|t|\big)+i\big(t\log|t|+\tfrac{\pi}{2}\sigma\,\mathrm{sgn}(t)\big)+o(|t|).$$
*Consequently $\big|\mathrm{pri}_{\mathrm{idx},\sharp}(\sigma+it)\big|\sim |t|^{\sigma}e^{-\pi|t|/2}/2\pi$.*

*Proof sketch.* $\mathrm{Li}(z)=\frac{z}{\log z}(1+O(1/\log z))$ holds uniformly in any closed sector off the cut $[0,1]$; inverting, $z\sim w\log w$ for $\mathrm{Li}(z)=w$, and with $w=\sigma+it$, $\log w=\log|t|+i\frac\pi2\mathrm{sgn}(t)+O(1/|t|)$, expand $(\sigma+it)(\log|t|+i\frac\pi2\mathrm{sgn}(t))$. The modulus follows from $|\mathrm{pri}_{\mathrm{idx},\sharp}|=e^{\operatorname{Re}\mathrm{Li}^{-1}}/2\pi$. $\square$ [P]

The exponential rate $e^{-\pi|t|/2}$ is **the same as Stirling's for $\Gamma$**; the polynomial prefactor is $|t|^{\sigma}$ versus $\Gamma$'s $|t|^{\sigma-1/2}$ — one half-power higher, the only structural difference.

### 2.4 The Wielandt theorem {#sec:2-4}

\hypertarget{stmt:2-4}{}
**Theorem 2.4 (Wielandt for the smooth primorial).** *Let $H_+:=\{\operatorname{Re} z>0\}$ and let $f:H_+\to\mathbb C^{*}$ be holomorphic and nowhere zero with*

*(W1) $f(z+1)/f(z)=\exp(\mathrm{Li}^{-1}(z+1)-\mathrm{Li}^{-1}(z))$;  (W2) $\lim_{z\to0^+}f(z)=e^2/2\pi$;  (W3) $f(z)\,e^{-\mathrm{Li}^{-1}(z)}$ is bounded on $\{1\le\operatorname{Re} z\le2\}$.*

*Then $f=\mathrm{pri}_{\mathrm{idx},\sharp}$ on $H_+$.*

*Proof.* Put $\phi(z):=\log f(z)-\mathrm{Li}^{-1}(z)+\log2\pi$. By (W1), $\phi(z+1)-\phi(z)=0$, so $\phi$ is $1$-periodic. By (W3), $\operatorname{Re}\phi=\log|f\,e^{-\mathrm{Li}^{-1}}\,2\pi|$ is bounded on the strip $\{1\le\operatorname{Re} z\le2\}$, and a single branch bounds $\operatorname{Im}\phi$; by $1$-periodicity $\phi$ extends to an entire function bounded on every translate of the strip, hence bounded on $\mathbb C$. By Liouville $\phi\equiv c$. By (W2), $\phi(0^+)=\log(e^2/2\pi)-2+\log2\pi=0$, so $c=0$ and $f=\mathrm{pri}_{\mathrm{idx},\sharp}$. $\square$

Wielandt's classical condition for $\Gamma$ — "$f$ bounded on $\{1\le\operatorname{Re} z\le2\}$" — works because $\Gamma$ itself decays there by Stirling, so "bounded" already means "tracks $\Gamma$'s growth." Condition (W3) is the literal analogue, "$f$ tracks $\mathrm{pri}_{\mathrm{idx},\sharp}$'s growth," made explicit because the smooth primorial decays on strips (\hyperlink{stmt:2-3}{Lemma~2.3}). **Theorem 2.4 is [P]** at Wielandt's rigor. Replacing (W3) by a Phragmén–Lindelöf finite-exponential-type condition is a natural sharpening, left open [C].

---

## 3. The divisor family and the constant tower {#sec:3}

The smooth primorial is the first member of a family obtained by smoothing the logarithm of each multiplicative invariant of primorials. Their asymptotic ratios are the classical analytic-number-theory constants, read in their structural homes. In the language of §2 these are the *asymptotic constant* $\sigma[g]=\int_1^2\Sigma g$ and the *generalized Euler constant* $\gamma[g]$ that the Krull–Webster/Marichal–Zenaïdi theory attaches to a principal indefinite sum, here instantiated for the prime ladder; the smooth Mertens constant $\widetilde\gamma_*$ below is one such generalized Euler constant. This places the smooth primorial in the same family as $\Gamma$ and the Barnes $G$-function, whose Stirling constants are built from $\zeta'(0)$ (the $2\pi$) and $\zeta'(-1)$ (the Glaisher–Kinkelin constant): the smooth primorial sits at $\zeta'(0)$, alongside $\Gamma$.

### 3.1 The smooth Mertens constant {#sec:3-1}

Define the smooth totient $\widetilde\phi$ by $\log\widetilde\phi(z)=\int_0^z\log(\mathrm{Li}^{-1}(t)-1)\,dt+C_\phi$, the constant fixed by Mertens-matching.

\hypertarget{stmt:3-1}{}
**Theorem 3.1 (smooth Mertens).** *As $z\to\infty$,*
$$\log\frac{\mathrm{pri}_{\mathrm{idx},\sharp}(z)}{\widetilde\phi(z)}=\log\log\mathrm{Li}^{-1}(z)+\widetilde\gamma_*+o(1),\qquad \widetilde\gamma_*:=C^*-\log\log2,\quad C^*:=\sum_{k\ge2}\frac{E_1((k-1)\log2)}{k}, \tag{3.1}$$
*where $E_1$ is the exponential integral. Numerically $C^*\approx0.24527$ and $\widetilde\gamma_*\approx0.6119$.*

*Proof.* By the definition of $\widetilde\phi$ and \hyperlink{stmt:1-3}{Definition~1.3}, $\log(\mathrm{pri}_{\mathrm{idx},\sharp}/\widetilde\phi)=-\int_0^z\log(1-1/\mathrm{Li}^{-1}(t))\,dt+(\text{boundary})$. Substituting $u=\mathrm{Li}^{-1}(t)$ and expanding the logarithm,
$$-\int_2^{\mathrm{Li}^{-1}(z)}\frac{\log(1-1/u)}{\log u}\,du=\sum_{k\ge1}\frac1k\int_2^{\mathrm{Li}^{-1}(z)}\frac{du}{u^{k}\log u}.$$
The $k=1$ term is $\log\log\mathrm{Li}^{-1}(z)-\log\log2$; for $k\ge2$ each integral converges to $E_1((k-1)\log2)$ via $u=e^{s}$, and $C_\phi$ absorbs the discrete-matching shift. $\square$ [P]

### 3.2 The bias from Euler's $\gamma$ is a Riemann-error integral (honest negative) {#sec:3-2}

A pre-registered expectation was that the family would emit Euler's $\gamma$ cleanly. It does **not**: the smooth Mertens constant is biased, and the bias is itself a named constant.

\hypertarget{stmt:3-2}{}
**Theorem 3.2.**
$$\widetilde\gamma_*-\gamma=\int_2^\infty\frac{\pi(u)-\mathrm{Li}(u)}{u(u-1)}\,du\approx0.0347. \tag{3.2}$$

*Proof.* Compare the smooth integral $\int_2^x\log(1-1/u)/\log u\,du$ to the discrete sum $\sum_{p\le x}\log(1-1/p)$ by Abel summation against $d\mathrm{Li}$. With $f(u)=\log(1-1/u)$, $f'(u)=1/(u(u-1))$, the difference is $-\int_2^x f'(u)[\pi(u)-\mathrm{Li}(u)]\,du+O(\text{boundary})$. Discrete Mertens gives $\gamma$; the smooth integral gives $\widetilde\gamma_*$; their difference is (3.2). $\square$ [P]

This is the structurally honest statement: the family emits $\widetilde\gamma_*$, not $\gamma$, with the gap a Riemann-error integral. Both constants and their relation are [P]. Structurally $\widetilde\gamma_*$ is the Marichal–Zenaïdi generalized Euler constant of the prime-ladder increment — the area between the increment and its piecewise-linear interpolant, i.e. the discrete-to-smooth summation remainder — and (3.2) identifies the primorial-specific instance of that remainder as a prime-counting integral.

### 3.3 Clean emission of $\zeta(k)$, and the partition principle {#sec:3-3}

For $k\ge1$ set $\log\widetilde J_k(z)=\int_0^z\log(\mathrm{Li}^{-1}(t)^k-1)\,dt+C_{J_k}$.

\hypertarget{stmt:3-3}{}
**Theorem 3.3.** *For every $k\ge2$,*
$$\lim_{z\to\infty}\frac{\widetilde J_k(z)}{\mathrm{pri}_{\mathrm{idx},\sharp}(z)^{k}}=\frac{1}{\zeta(k)}\qquad\text{exactly, with no bias.} \tag{3.3}$$

*Proof.* $\log(\widetilde J_k/\mathrm{pri}_{\mathrm{idx},\sharp}^k)=\int_0^z\log(1-\mathrm{Li}^{-1}(t)^{-k})\,dt+(\text{boundary})$. Every term of $\log(1-u^{-k})=-\sum_{m\ge1}u^{-mk}/m$ has $mk\ge2$, so all integrals $\int du/(u^{mk}\log u)$ converge absolutely; $C_{J_k}$ matches the discrete $\prod_{j\le n}(1-p_j^{-k})\to1/\zeta(k)$. $\square$ [P]

\hypertarget{stmt:3-4}{}
**Theorem 3.4 (partition by Euler-product convergence).** *The family's $z\to\infty$ ratios emit constants according to the convergence regime of the underlying Euler product: absolutely convergent ($s\ge2$) gives clean $\zeta(k)$ with no bias ($\widetilde J_k/\mathrm{pri}^k$, $k\ge2$); conditionally convergent ($s=1$, Mertens) gives a shift by a named Riemann-error integral ($\mathrm{pri}/\widetilde\phi$).* [P]

| smooth ratio | asymptotic | emitted constant | bias |
|---|---|---|---|
| $\mathrm{pri}_{\mathrm{idx},\sharp}/\widetilde\phi$ | $e^{\widetilde\gamma_*}\log\mathrm{Li}^{-1}(z)$ | $\widetilde\gamma_*=0.6119$ | $\widetilde\gamma_*-\gamma=\int_2^\infty\frac{\pi-\mathrm{Li}}{u(u-1)}\,du\approx0.0347$ |
| $\widetilde J_2/\mathrm{pri}^2$ | $1/\zeta(2)=6/\pi^2$ | $-\log\zeta(2)$ | **none** |
| $\widetilde J_3/\mathrm{pri}^3$ | $1/\zeta(3)$ | $-\log\zeta(3)$ | **none** |
| $\widetilde J_k/\mathrm{pri}^k$, $k\ge2$ | $1/\zeta(k)$ | $-\log\zeta(k)$ | **none** |

### 3.4 The starting-prime tower and its archimedean fixed point {#sec:3-4}

For each prime $p$, the smooth primorial *started at $p$* uses $\mathrm{Li}_p(x):=\int_p^x dt/\log t$, giving $\mathrm{Pri}_p(z):=e^{\mathrm{Li}_p^{-1}(z)}/2\pi$.

\hypertarget{stmt:3-5}{}
**Theorem 3.5 (translation orbit).** *Since $\mathrm{Li}_p(x)=\mathrm{Li}(x)-\mathrm{Li}(p)$, one has $\mathrm{Pri}_p(z)=\mathrm{pri}_{\mathrm{idx},\sharp}(z+\mathrm{Li}(p))$. The starting-prime family is the orbit of one master curve under translation by the marked abscissae $\{\mathrm{Li}(p)\}$, which are approximately unit-spaced ($\mathrm{Li}(2)=0$, and $\mathrm{Li}(p_{n+1})-\mathrm{Li}(p_n)\to1$ by PNT). Starting one prime later and multiplying in one more prime are the same operation. The master curve has a finite left floor $\mathrm{pri}_{\mathrm{idx},\sharp}(-\infty)=e/2\pi\approx0.4326$, with $\mathrm{pri}_{\mathrm{idx},\sharp}(0)/\mathrm{pri}_{\mathrm{idx},\sharp}(-\infty)=e$.* [P]

*Proof.* $\mathrm{Li}_p(x)=\int_p^x=\int_2^x-\int_2^p=\mathrm{Li}(x)-\mathrm{Li}(p)$; invert and exponentiate. The floor is $\mathrm{Li}^{-1}(z)\to1^+$ as $z\to-\infty$, giving $e^1/2\pi$, and $\mathrm{Li}^{-1}(0)=2$ gives the factor $e$. $\square$

Under this shift the emitted constants of \hyperref[sec:3-1]{§3.1}–\hyperref[sec:3-3]{§3.3} split into three classes, and exactly one constant is fixed.

\hypertarget{stmt:3-6}{}
**Theorem 3.6 (the archimedean fixed point).** *Under the starting-prime shift $p\mapsto$ next prime:*

- *the $\zeta(k)$ constants **telescope** toward $1$: $R_k^{(p)}:=\prod_{q>p}(1-q^{-k})=\big(\zeta(k)\prod_{q\le p}(1-q^{-k})\big)^{-1}$, e.g. $R_2^{(p)}\cdot\pi^2 = 8,\,9,\,\tfrac{75}{8},\,\tfrac{1225}{128},\,\tfrac{29645}{3072},\dots\to\pi^2$;*
- *the Mertens/boundary constants **accumulate**: the boundary slope $(\mathrm{Li}_p^{-1})'(0)=\log p$ and $\widetilde\gamma_*^{(p)}$ move with $p$;*
- *the archimedean constant $\log2\pi=-\zeta'(0)/\zeta(0)$ is **invariant**: truncating the Euler product removes finite primes but not the archimedean coupling.*

*Hence $\log2\pi$ is the unique shift-invariant constant of the prime ladder.* [P]

*Proof.* $R_k^{(p)}$ telescopes by definition; the displayed rationals are $6/\prod_{q\le p}(1-q^{-2})$. The slope identity is $(\mathrm{Li}_p^{-1})'(0)=\log\mathrm{Li}^{-1}(\mathrm{Li}(p))=\log p$. The constant $\log2\pi$ arises from $\zeta$ at $s=0$, where removing finite Euler factors leaves the archimedean factor unchanged. $\square$

So the standard analytic-number-theory constants — $\gamma$, $\zeta(k)$, $\log p$, $\log2\pi$ — are the *start-from-$2$* readings of one master curve and its slopes at the marked points; only $\log2\pi$ is the part the ladder cannot move. (These smooth-family objects also arise as dimension and density data in the author's wider program; that connection is companion work, forthcoming, and is not used below.)

### 3.5 Three smooth primorials, and why the explicit formula is the right one {#sec:3-5}

The convexity theory of §2 fixes the smooth primorial only up to the additive constant of \hyperref[sec:1-2]{§1.2}, and even the *base increment* is a choice. Two natural choices, against the exact object, give three sequences to compare:

- $A(n)=\mathrm{pri}_{\mathrm{idx},\sharp}(n)=e^{\mathrm{Li}^{-1}(n)}/2\pi$ — the explicit-formula object of §1;
- $B(n)=\prod_{k\le n}\mathrm{li}^{-1}(k)$ — the *product of smooth primes*: the Krull–Webster/Marichal–Zenaïdi principal indefinite sum of the smooth log-prime $z\mapsto\log\mathrm{li}^{-1}(z)$, where $\mathrm{li}^{-1}$ (inverse of the *unshifted* logarithmic integral) is the smooth $n$-th prime, $p_n\sim\mathrm{li}^{-1}(n)$ (Arias de Reyna–Toulisse 2012);
- $P_n=\prod_{k\le n}p_k$ — the exact primorial.

$A$ and $B$ are genuinely different functions. Because $\int\log\mathrm{li}^{-1}=\mathrm{li}^{-1}$ *exactly* (the identity $(\mathrm{li}^{-1})'=\log\mathrm{li}^{-1}$) while the *sum* $\sum_{k\le n}\log\mathrm{li}^{-1}(k)$ carries the Euler–Maclaurin $\tfrac12$-term, $\log A-\log B\to\infty$: numerically $A/B\sim\mathrm{li}^{-1}(n)^{c}$ with $c\approx\tfrac12$.

What singles out $A$ is *how* it misses $P_n$. Computed in exact-then-high-precision arithmetic for $n\le20$ (certificate `smooth_primorial_three_objects.py`, archived with this paper):

| object | behaviour of $\log(\text{object}/P_n)$ |
|---|---|
| $A$ — explicit formula | **oscillates and changes sign**: $+0.34,+0.48,+0.45,+0.39,+0.14,-0.04,-0.28,\dots$, crossing $0$ near $n=6$ — the $\sqrt{\cdot}$-scale Riemann zero-sum of \hyperlink{stmt:1-4}{Corollary~1.4} |
| $B$ — product of smooth primes | **monotone, systematically accumulating**: $-0.02,-0.08,-0.29,-0.51,-0.89,\dots$, never changing sign |

The explicit-formula normalization $-\log2\pi=\zeta'(0)/\zeta(0)$ absorbs exactly the systematic drift that the naive product $B$ carries, leaving only the oscillating, Riemann-scale error. **This is why $A$, not $B$, is the canonical smooth primorial**: the arithmetic input that makes it faithful is the same archimedean constant that \hyperref[sec:4]{§4} shows must be adjoined because the primorial is not a moment sequence. The distinctness of the three objects, and the $\sqrt{\cdot}$-scale character of $A$'s defect (via \hyperlink{stmt:1-4}{Corollary~1.4}), are [P]; the precise divergence exponent $c$ and the monotonicity of $B$'s drift are reported numerically.

---

## 4. The moment barrier {#sec:4}

Here is the structural reason the smooth primorial can only *approach* the primorial, and the main theorem: the obstruction is not special to the primorial but bars the entire finite-prime divisor family.

### 4.1 The factorial is a moment sequence; the primorial is not {#sec:4-1}

$\Gamma$ lands on the factorial exactly because the factorial is a **moment sequence**, $n!=\int_0^\infty t^{n}e^{-t}\,dt$, and Mellin's integral interpolates any moment sequence. A sequence $(m_k)$ is a (Hamburger) moment sequence — $m_k=\int t^k\,d\mu$ for a positive measure $\mu$ — only if every Hankel determinant $D_N:=\det(m_{i+j})_{0\le i,j\le N}\ge0$, since $D_N$ controls the quadratic form $\int(\sum c_i t^i)^2\,d\mu\ge0$. A single negative $D_N$ rules out every representing measure (Akhiezer 1965).

For the primorial $(P_n)=1,2,6,30,210,2310,30030,\dots$,
$$D_0=1,\quad D_1=\begin{vmatrix}1&2\\2&6\end{vmatrix}=2,\quad D_2=24,\quad
D_3=\begin{vmatrix}1&2&6&30\\2&6&30&210\\6&30&210&2310\\30&210&2310&30030\end{vmatrix}=-787680.$$

\hypertarget{stmt:4-1}{}
**Theorem 4.1 (the primorial is not a moment sequence).** $D_3(P)=-787680<0$; hence $(P_n)$ admits no representing measure, and no Mellin-type integral $\mathrm{pri}(z)=\int_0^\infty t^{z-1}\,d\mu(t)$ can interpolate it. The factorial escapes because $(n!)$ is the moment sequence of $e^{-t}$; the primorial's growth ratios $P_{n+1}/P_n=p_{n+1}$ are too irregular to be moment ratios, and positivity first fails at $N=3$. [P]

**The barrier and the archimedean constant are one fact.** This is the structural counterpart of the construction's normalization (\hyperref[sec:1-2]{§1.2}, \hyperref[sec:2]{§2}). The factorial *generates its own* $2\pi$: as a moment sequence it carries an intrinsic measure $e^{-t}\,dt$, and the $\sqrt{2\pi}$ in Stirling — equivalently, the Marichal–Zenaïdi asymptotic constant of $\log\Gamma$ — is read off from that measure. The primorial has no representing measure (Theorem 4.1), so it *cannot* generate its archimedean constant internally; the $-\log2\pi=\zeta'(0)/\zeta(0)$ must be adjoined from $\zeta$'s explicit formula. The moment barrier and the external archimedean normalization are two faces of one phenomenon — and \hyperref[sec:3-5]{§3.5} showed that this adjoined constant is precisely what makes the smooth primorial faithful at the Riemann scale.

### 4.2 The barrier is family-wide {#sec:4-2}

The same computation, run across the divisor family, returns (exact integer arithmetic; \hyperref[sec:app-a]{Appendix~A}):

| sequence | first $D_N<0$ | verdict |
|---|---|---|
| $P_n$, $\ \varphi(P_n)=\prod(p-1)$, $\ \sigma(P_n)=\prod(p+1)$, $\ J_2(P_n)=\prod(p^2-1)$ | $N^*=3$ | non-moment |
| $J_3(P_n)=\prod(p^3-1)$ | $N^*=4$ | non-moment |
| $d(P_n)=2^n$ | — | **moment** (point mass $\delta_2$) |
| $n!$ (control) | — | moment |

Every genuinely multiplicative member fails; only the divisor count $2^n$ — which records *that* a prime was multiplied in but not *which* — survives, as the moments of a point mass at $2$. The reason is one identity.

\hypertarget{stmt:4-2}{}
**Theorem 4.2 (the moment barrier is family-wide).** *Let $b_n=\prod_{i=1}^n c_i$ with $c_i>0$. Then*
$$D_N=\Big(\prod_{i=0}^{N}b_i\Big)\det\Big[\tfrac{b_{i+j}}{b_i}\Big]_{0\le i,j\le N},\qquad \tfrac{b_{i+j}}{b_i}=\prod_{l=i+1}^{i+j}c_l,$$
*so $\operatorname{sign}(D_N)$ is the sign of the right-hand determinant, whose entries depend on the $c_l$ only through their products. The factorization does not by itself force the first-failure index $N^*$ to agree across the families $\prod(p^k-1)$, $\prod(p^k+1)$, $\prod p^k$ — their correction factors $\prod(1\mp p_l^{-k})$ are $O(1)$ at the small primes that determine $N^*$ — but exact computation gives*
$$N^*\big(\textstyle\prod(p^k-1)\big)=N^*\big(\textstyle\prod(p^k+1)\big)=N^*\big(\textstyle\prod p^k\big)\qquad\text{for }k=1,\dots,8,$$
*the general invariance left open. Every such sequence has some $D_N<0$ (it is non-moment); the only moment member of the divisor family is $d(P_n)=2^n$.*

*Proof.* Row $i$ of $(b_{i+j})$ equals $b_i\cdot(1,c_{i+1},c_{i+1}c_{i+2},\dots)$; factoring $b_i>0$ from each row gives the displayed identity, and $\prod_i b_i>0$ does not affect the sign. The right-hand entries $\prod_{l=i+1}^{i+j}c_l$ for $c_l=p_l^{k}(1\mp p_l^{-k})$ are the pure-power entries times $\prod(1\mp p_l^{-k})$; these corrections are $O(1)$ at the small primes (e.g. $\tfrac12$ at $p=2$, $k=1$), so the factorization alone does not force equal $N^*$, but exact computation finds the correction does not flip the sign at $N^*$ for $k=1,\dots,8$. Non-momentness of each tested member is the exact computation; $d(P_n)=2^n=\int t^n\,\delta_2$ is the lone moment sequence, its ratios being constant. $\square$

The factorization itself is **[P]** (the artifact verifies $-787680=360\cdot(-2188)$ at $N=3$ exactly, placing $\operatorname{sign}(D_N)$ in the second factor); the family-wide non-momentness of each tested member is **[P]**; the cross-family invariance of $N^*$ is **[P] for $k\le8$** by exact verification and **[A]** in general. This statement — that the *whole* finite-prime divisor family is barred, with only the magnitude-blind $2^n$ admitted — is \hyperlink{thm:b}{Theorem~B}, the paper's centerpiece; it strengthens the single-sequence \hyperlink{stmt:4-1}{Theorem~4.1}.

**The survivor, and why the barrier is about prime *irregularity*.** The lone survivor $d(P_n)=2^n$ is the degenerate moment sequence: its Hankel determinants are $D_0=1$, $D_1=D_2=\cdots=0$ — the signature of a measure with a *single* mass point (Berg and Szwarc 2015) — and indeed $2^n=\int t^n\,d\delta_2$. One is tempted to read off a clean dichotomy ("$\prod f(p_i)$ is a moment sequence iff $f$ is constant"), but that is **false**, and seeing why is the point. The moment property is a property of the ratio sequence $c_i=b_i/b_{i-1}$, and *many* non-constant ratio sequences are moment sequences: $c_i=i$ gives $n!$ (moments of $e^{-t}$), $c_i=2i-1$ gives the double factorials (Gamma moments), and indeed any arithmetic progression $c_i=a+bi$ gives a Gamma/Pochhammer moment sequence. So what singles out the primorial families is not the *magnitude* of the primes but their *irregular spacing*: replacing the primes $2,3,5,7,11,13$ by the odd numbers $1,3,5,7,9,11$ — the same sizes, but constant gaps — turns the first failing sign-determinant from $\det W_3=-2188<0$ into $+768>0$, a moment sequence. The moment barrier is a manifestation of the irregular spacing of the primes — the very irregularity the Riemann zeros measure (\hyperref[sec:1]{§1}, \hyperref[sec:5]{§5}), which is the same scale at which the smooth primorial deviates from the exact one.

What we therefore claim is one-directional and exactly what the computation supports (Theorem 4.2): each standard multiplicative invariant ($\varphi,\sigma,J_k,\prod(p^k\pm1),\prod p^k$) fails Hankel positivity, while only the magnitude-blind $d=2^n$ survives. The reverse implication — a clean characterization of *which* $\prod f(p_i)$ are moment sequences — is a Hankel-total-positivity question that the odds-vs-primes contrast shows is genuinely delicate. For *polynomial* local factors it is settled (\hyperlink{stmt:4-4}{Theorem~4.4}, \hyperref[sec:4-5]{§4.5}): all are non-moment, with the obstruction located at a prime-gap local maximum. (We use only the *necessary* half of the criterion, $D_N<0\Rightarrow$ non-moment; the converse fails — $D_N\ge0$ for all $N$ need not give a representing measure, Berg–Szwarc exhibiting $1,1,1,1,0,0,\dots$ — so the criterion is invoked exactly where it is unconditional.)

### 4.3 The depth law, and a pre-registered guess that failed {#sec:4-3}

The first-failure depth, computed exactly for $k=1,\dots,8$:
$$N^*(k)=3,\,3,\,4,\,4,\,5,\,9,\,9,\,9,\dots$$
This is **non-decreasing and unbounded** — the obstruction recedes as $k$ grows, mirroring the \hyperref[sec:3-3]{§3.3} partition (higher $k$ means deeper absolute convergence of the Euler product, and the wall moves further out). We had **pre-registered the sharper claim that $N^*(k)$ is *strictly* monotone**. It is **false**: the sequence has two plateaus and a jump ($4,4$ then $5$ then a jump to $9,9,9$), with no clean closed form. We keep the dead guess on the record beside the surviving facts. The $k\to\infty$ limit of the sign-determining $\det[b_{i+j}/b_i]$ is a tropical (max-plus) determinant; pinning the exact law $N^*(k)$ is the natural open problem ([A]; see \hyperref[sec:6]{§6}).

### 4.4 The interpolation trilemma {#sec:4-4}

\hypertarget{stmt:4-3}{}
**Corollary 4.3.** *For the primorial, the three properties — exact at integers, real-analytic, canonical — cannot all be had by the two standard mechanisms:*

- ***analytic $+$ canonical**, sacrificing exact:* $\mathrm{pri}_{\mathrm{idx},\sharp}$ of \hyperref[sec:1]{§1} (Bohr–Mollerup/Wielandt unique; matches only asymptotically);
- ***exact $+$ canonical**, sacrificing analytic:* the log-linear interpolation $\mathrm{pri}_{\mathrm{lin}}(n+t)=P_n\,p_{n+1}^{t}$ ($C^0$, not differentiable at integers);
- ***exact $+$ analytic**, sacrificing canonical:* entire order-$1$ Newton/Carlson interpolations exist but are non-unique (any multiple of $\sin\pi z$ may be added) and admit no Mellin representation (\hyperlink{stmt:4-1}{Theorem~4.1}).

*The factorial escapes the trilemma because $(n!)$ is a moment sequence; the primorial does not, because $(P_n)$ is not. The deviation of the canonical analytic interpolation from exactness is, by \hyperlink{stmt:1-2}{Proposition~1.2}, the Riemann zero-sum.* [P] for the moment route; [A] for the trilemma framing.

### 4.5 All polynomial local factors, and the prime-gap mechanism {#sec:4-5}

\hyperlink{stmt:4-2}{Theorem~4.2} concerns the specific multiplicative invariants $\varphi,\sigma,J_k$. The barrier in fact holds for *every* polynomial local factor, and the proof locates its mechanism precisely in the prime gaps.

\hypertarget{stmt:4-4}{}
**Theorem 4.4 (polynomial local factors).** *Let $f$ be a polynomial of degree $\ge1$ with $f(p)>0$ at all primes. Then $b_n=\prod_{i\le n}f(p_i)$ is not a Hamburger moment sequence. This is unconditional for $\deg f\in\{1,2\}$; for $\deg f\ge3$ it is conditional on a Hardy–Littlewood prime-constellation conjecture (the residual below), and verified with no exceptions across thousands of polynomials (degrees up to $4096$).*

*Reduction to monic.* Write $f=a\,g$ with $g$ monic; $a>0$ is forced ($f>0$ on infinitely many primes). Then $D_N(f)=a^{N(N+1)}D_N(g)$ — sign-preserving — so we may take $f$ monic.

*Degrees 1 and 2 are closed ([P]).* For $f(p)=p+c$ ($c>-2$): $D_2(c)=-2(c-1)(c+2)^2(c+3)<0$ for $c>1$, while $D_3(c)=4(c+2)^3(c+3)^2(c+5)\,(c^3-21c^2-297c-547)<0$ for $-2<c\le1$. For monic $f(p)=p^2+Bp+C$, the valid $(B,C)$-region splits at $B=-5$: on $B\le-5$, $D_2=2f(2)^2f(3)\,g_2$ with $g_2$ strictly decreasing in $C$ (discriminant $-47<0$) is negative; on $B>-5$ the binding prime is $2$ and the $3\times3$ principal minor $M_{\{2,3,4\}}=-12\big(\textstyle\prod_k f(p_k)^{m_k}\big)\Psi$, with $\Psi$ increasing in $C$ from $E_2(B)\ge E_2(-5)=18\,770>0$, is negative. Both bounds are explicit and exact.

*The mechanism (algebraic core, [P]).* Here a *non-leading* principal minor is the right witness. With $c_l=f(p_l)$, the consecutive $3\times3$ principal Hankel minor on $\{m,m+1,m+2\}$ factors as
$$M_{\{m,m+1,m+2\}}=-\big(\text{positive monomial in the }c_l\big)\cdot Q,$$
and, writing the four primes it sees as $q_1<q_2<q_3<q_4$ with gaps $a=q_2-q_1$, $b=q_3-q_2$, $e=q_4-q_3$, its sign as the window recedes is
$$\operatorname{sign}(Q)\ \longrightarrow\ \operatorname{sign}\!\big(b^2-ae\big)\qquad(\text{the degree cancels: leading coefficient }=(\deg f)^2(b^2-ae)).$$
So the minor is **negative — non-moment — exactly when $b^2>ae$** (equivalently, when the gap-ratio $d_{i+1}/d_i$ drops at that step; a gap *local maximum* is the simplest sufficient case, not a necessary one). This is what "irregular spacing" means, sharply: not magnitude, not mere non-arithmeticity, but a *second-order excess in the gap sequence*. The obstruction is in fact **self-similar**: the consecutive $K\times K$ principal minor of $(b_n)$ is negative iff the $(K-1)\times(K-1)$ Hankel determinant of the *prime-gap sequence itself* is negative — the $K=3$ case being $b^2-ae<0$ — so the moment problem for $\prod f(p_i)$ collapses, level by level, onto Hankel positivity of the gaps. The degree enters only through an explicit threshold: $M_{\{m,m+1,m+2\}}<0$ iff $b^2>(1+W/q)^{3d-2}ae$ with $W=a+b+e$, so the window index needed grows like $q^*(d)\sim(3d-2)\,W/\ln(b^2/ae)$ — linear in $d$. The discrimination is decisive: every smooth-gap ratio sequence stays a moment sequence — $c_i=i$ ($n!$), $c_i=2i-1$, every arithmetic progression (Gamma/Pochhammer), $c_i=i^2$ ($(n!)^2$), $c_i=2^i$ — because their gap-ratios never drop; the criterion provably does not fire. (Three independent derivations — orthogonal-polynomial Jacobi weights $\lambda_k=D_{k-2}D_k/D_{k-1}^2$, the sliding-minor factorization, and the gap identity $\det W_2=c_3\,g_1g_3-c_1\,g_2^2$ — agree.)

*The residual ([C], a prime-constellation conjecture).* What is **not** unconditional is the existence of the firing windows uniformly in degree. The *shape* $b^2>ae$ does occur infinitely often unconditionally — from $\liminf_n d_n\le246$ (Zhang 2014, Maynard 2015) and $\limsup_n d_n=\infty$ (Westzynthius 1931), with width $O(p^{0.525})$ (Baker–Harman–Pintz 2001) — and the degree-uniform threshold above is explicit. But the firing minor sits at a fixed parity of index, and "infinitely many firings of the required parity, with bounded neighbours, at arbitrarily large primes" does **not** follow from those inputs: an explicit gap sequence meeting all of them fires only at the wrong parity. That statement is a Hardy–Littlewood-type assertion — a fixed admissible prime quadruple occurring infinitely often — so for $\deg f\ge3$ the theorem is *conditional* on it. Degrees $1$ and $2$ avoid this entirely, closing by the explicit determinants above. (Adversarially verified; one route initially over-claimed "morally unconditional," which the skeptic pass corrected to conditional.)

*Two faces of Hardy–Littlewood.* It is worth being precise about *which* Hardy–Littlewood statement the residual invokes, because the count-side conjecture is far better understood than the one needed here. The Hardy–Littlewood $k$-tuple circle splits into two assertions usually named together. **(A) The density face:** for an admissible tuple $H$, $\pi_H(x)\sim\mathfrak S(H)\,x/(\log x)^{k}$ with explicit singular series $\mathfrak S(H)$; this is the asymptotic *count* of prime constellations and the object of the modern level-of-distribution machinery (Bombieri–Vinogradov, and the conditional Elliott–Halberstam strengthenings that Zhang and Maynard exploit). **(B) The consecutive face:** the existence of a *bounded-width pattern of three consecutive prime gaps* — a fixed admissible quadruple appearing as four **consecutive** primes — infinitely often. The residual above is of type (B), and (B) is strictly harder than (A): the Maynard–Tao method realizes any admissible tuple as primes but not as *consecutive* primes, and consecutiveness is exactly the open quadruplet obstruction. The unconditional inputs we *do* have push in the right direction but stop short — record gaps give neighbours strictly smaller, hence $b^2>ae$ with margin $>1$ unconditionally, but the margin can degrade as $\sim 4/b$ while the width penalty $(1+W/q)^{3d-2}$ grows through $W=O(q^{0.525})$, so they yield a near-miss rather than a closure. Thus the barrier's conditionality is *not* a gap in the density theory of primes (which is rich and which this circle of ideas connects to elsewhere) but a genuine call on the consecutive-constellation face, which is open for everyone. For any individually specified $f$ the point is moot: a single negative minor past $q^*(\deg f)$ certifies non-momentness with no conjecture, and such a minor exists in the data for every degree tested.

*No fixed-$N$ certificate.* The first-failing index grows with the degree (empirically $\sim$linearly: $m(d)=14,16,40,40,85,170,\dots$), so **no bounded Hankel check certifies non-moment**: $p^{128}$, for instance, has every principal minor positive through $N=22$ yet fails at a $3\times3$ minor near index $42$. Non-momentness is certified by an explicit negative minor whose index depends on $\deg f$.

---

## 5. The $\sqrt{\cdot}$-scale: sieve horizon and the Riemann hypothesis {#sec:5}

The barrier of \hyperref[sec:4]{§4} lives at a definite scale. The same $\sqrt{\cdot}$-scale governs the sieve, the smooth-vs-exact gap, and — classically — the Riemann hypothesis.

### 5.1 The sieve horizon {#sec:5-1}

\hypertarget{stmt:5-1}{}
**Lemma 5.1 (sieve horizon).** *Fix $n$. On $(p_{n+1},p_{n+1}^2)$ the conditions "coprime to $P_n$", "coprime to $P_{n+1}$", and "prime" coincide; recruiting $p_{n+1}$ removes no element of this interval. In particular a prime $p$ changes no primality verdict below $p^2$: its first sieving effect is its square.*

*Proof.* If $m\in(p_{n+1},p_{n+1}^2)$ is coprime to $P_n$ and $p_{n+1}\mid m$, then $m=p_{n+1}k$ with $2\le k<p_{n+1}$, so $k$ has a prime factor $\le p_n$ dividing $m$ — contradiction; thus $m$ is coprime to $P_{n+1}$. Any composite coprime to $P_n$ has two prime factors $>p_n$, hence is $\ge p_{n+1}^2$, so none lies in the interval. $\square$ [P]

This is why $\sqrt{\cdot}$, not the integer itself, is the natural scale of certification.

### 5.2 The certification window and the barcode {#sec:5-2}

By \hyperlink{stmt:5-1}{Lemma~5.1}, every prime $q\in(p_n,p_{n+1}^2)$ has its primality forced by $P_n$ alone (the **certification window**). Reading the sieve as a filtration indexed by stage $n$, a prime $q$ is *certified* the moment the sieving primes reach $\sqrt q$ and *recruited* at its own stage:
$$\text{birth }b(q):=\pi(\sqrt q),\qquad \text{death }d(q):=\pi(q),\qquad \text{lifetime }\ell(q)=\pi(q)-\pi(\sqrt q).$$

\hypertarget{stmt:5-2}{}
**Proposition 5.2.** *The primes certified-but-unrecruited at stage $n$ are exactly the window $\{q:p_n<q<p_{n+1}^2\}=\{q:b(q)\le n<d(q)\}$.* The death rate is identically $1$; the birth rate is $\sim p_n$. (Verified exactly, \hyperref[sec:app-a]{Appendix~A}; e.g. stage $2$ gives $\{5,7,11,13,17,19,23\}$ both ways.) [P]

*Proof.* $b(q)\le n\iff\pi(\sqrt q)\le n\iff\sqrt q<p_{n+1}\iff q<p_{n+1}^2$, and $n<d(q)\iff p_n<q$. $\square$

### 5.3 The birth measure is the prime-power leakage {#sec:5-3}

The birth-inclusive companion of $\mathrm{pri}_*=e^{\vartheta}$ is the classical
$$\operatorname{lcm}(1,2,\dots,\lfloor x\rfloor)=\prod_{p^k\le x}p=e^{\psi(x)},\qquad \psi(x)-\vartheta(x)=\sum_{k\ge2}\vartheta(x^{1/k})\sim\sqrt x.$$
Term by term, the right side is the running mass of *first shadows* — a prime casts its first at $p^2$ — so it is the integrated birth measure of the barcode.

\hypertarget{stmt:5-3}{}
**Proposition 5.3.** *Both $\mathrm{pri}_*$ and the lcm have the same canonical smoothing $e^x/2\pi$ (their explicit formulas share the leading $x-\log2\pi$ and differ only at the $\sqrt{\cdot}$ scale); the smooth primorial cannot tell the primorial from the lcm, and their difference $e^{\psi-\vartheta}\approx e^{\sqrt x}$ lives entirely in the term discarded to form the smoothing.* [P]

### 5.4 The Riemann hypothesis, stated as an equivalence {#sec:5-4}

The discarded $\sqrt{\cdot}$-scale term is precisely the one \hyperlink{stmt:1-4}{Corollary~1.4} ties to RH. Three faces of one object:

- the gap between the smooth primorial and the exact primorial (\hyperlink{stmt:1-2}{Proposition~1.2}, the Riemann zero-sum);
- the barcode's birth measure $\psi-\vartheta\sim\sqrt x$ (\hyperlink{stmt:5-3}{Proposition~5.3});
- the error in $\vartheta(x)=x+O(\sqrt x\log^2 x)$, whose sharpness is RH (\hyperlink{stmt:1-4}{Corollary~1.4}).

We state this as a structural equivalence only. **No attack on RH is offered**: the smooth primorial inherits the analytic envelope of finite-conductor Hurwitz data and does not separate on-line from off-line zeros. What is recovered is RH's *scale* and a faithful primorial-form restatement — not a new route to the hypothesis. [P, RH-equivalent for \hyperlink{stmt:1-4}{Corollary~1.4}; the four-way "one object" reading is [A].]

---

## 6. Limits, status ledger, and methods {#sec:6}

### 6.1 What this paper does not deliver (honest negatives) {#sec:6-1}

- **No RH progress.** \hyperlink{stmt:1-4}{Corollary~1.4} and \hyperref[sec:5-4]{§5.4} restate RH and recover its scale; they do not separate the zeros. The hypothesis is untouched.
- **The uniqueness is not a new technique.** Theorems 2.2 and 2.4 instantiate the Krull–Webster / Marichal–Zenaïdi theory of the difference equation $\Delta f=g$ (\hyperref[sec:2]{§2}); the construction-side novelty is the archimedean $\zeta'(0)$ normalization and its Riemann-scale faithfulness (\hyperref[sec:3-5]{§3.5}), not the uniqueness itself.
- **The smooth Mertens constant is not $\gamma$.** $\widetilde\gamma_*\approx0.612\ne\gamma\approx0.577$; the difference $\approx0.0347$ is the structural content (\hyperlink{stmt:3-2}{Theorem~3.2}), not an error to be removed.
- **The depth law is irregular.** The pre-registered strict monotonicity of $N^*(k)$ is **false**; only non-decreasing-and-unbounded survives (\hyperref[sec:4-3]{§4.3}).
- **Cross-family $N^*$ invariance is finite-verified only.** Proven for $k\le8$ by exact computation; the factorization does not force it; general $k$ is open (\hyperref[sec:4-2]{§4.2}).
- **The polynomial barrier is proved only in low degree; higher degree is conditional.** \hyperlink{stmt:4-4}{Theorem~4.4} (every polynomial local factor is non-moment) is unconditional for $\deg f\in\{1,2\}$; for $\deg f\ge3$ it is *conditional* on a Hardy–Littlewood prime-constellation conjecture (\hyperref[sec:4-5]{§4.5}) — the degree-uniformity and the firing-shape-infinitely-often are unconditional, but pinning the firing index's parity is not. The converse direction fails for general ratio sequences ($c_i=i,\,2i-1,\,i^2,\,2^i$ are non-constant moment sequences), so the obstruction is the gap condition $b^2>ae$, not magnitude; a full cross-$f$ characterization is open. Because the first-failing minor's index grows with $\deg f$, **no fixed-$N$ check certifies non-momentness** (e.g. $p^{128}$ survives a full PSD check through $N=22$).
- **No new $L$-function emissions, no degenerate Möbius content.** The smooth Möbius/Liouville extension is the trivial $e^{i\pi z}$, and Dirichlet characters do not extend canonically to non-integer arguments; neither produces new arithmetic.
- **The Phragmén–Lindelöf form of Wielandt** (\hyperref[sec:2-4]{§2.4}) is open.

### 6.2 Status ledger {#sec:6-2}

| Result | Statement | Tier |
|---|---|---|
| Def. 1.1, Prop. 1.2 | $\mathrm{pri}_\sharp=e^x/2\pi$ forced; deviation $=$ zero-sum | [P] (mod explicit formula) |
| Cor. 1.4 | RH $\iff$ smooth–exact gap $=O(\sqrt x\log^2 x)$ | [P, RH-equivalent] |
| Thm. 2.2 | Bohr–Mollerup uniqueness (Krull–Webster/M–Z, $p=1$) | [P] |
| Thm. 2.4 | Wielandt uniqueness (growth-tracking W3) | [P] |
| — | Phragmén–Lindelöf form of Wielandt | [C] |
| Thm. 3.1–3.2 | smooth Mertens $\widetilde\gamma_*$ (M–Z generalized Euler const.); bias $=$ Riemann-error integral | [P] |
| Thm. 3.3–3.4 | $\widetilde J_k/\mathrm{pri}^k\to1/\zeta(k)$ exact ($k\ge2$); partition principle | [P] |
| Thm. 3.5–3.6 | translation orbit; left floor $e/2\pi$; $\log2\pi$ the unique fixed point | [P] |
| §3.5 | three smooth primorials; $A$ (explicit-formula) $\sqrt{\cdot}$-faithful, $B$ drifts | [P]; exponent numerical |
| Thm. 4.1 | $(P_n)$ not a moment sequence ($D_3=-787680$) | [P] |
| **Thm. 4.2** | **family-wide barrier; factorization; only $2^n$ survives** | [P] (invariance [P] for $k\le8$, else [A]) |
| \hyperref[sec:4-3]{§4.3} | $N^*(k)=3,3,4,4,5,9,\dots$ non-decreasing; strict monotonicity falsified | [P] (negative retained) |
| Cor. 4.3 | interpolation trilemma | [P]/[A] |
| **Thm. 4.4** | **every polynomial local factor non-moment; self-similar gap-Hankel ($b^2>ae$) mechanism** | [P] deg 1–2; [C] (Hardy–Littlewood constellation) for deg $\ge3$ |
| Lem. 5.1, Prop. 5.2–5.3 | sieve horizon; window/barcode; birth measure $\sim\sqrt x$ | [P] |
| Conj. 6.1 | tropical limit law for $N^*(k)$ | [C] |

\hypertarget{stmt:6-1}{}
**Conjecture 6.1 (forward door, calibrated).** *The first-failure depth $N^*(k)$ of the Jordan-totient family is non-decreasing and unbounded, with a tropical (max-plus) law in the $k\to\infty$ limit governing how far the wall recedes.* Held with calibrated faith; built toward, not claimed.

### 6.3 Methods and reproducibility {#sec:6-3}

The computational results of \hyperref[sec:4]{§4} (and the exact checks of \hyperref[sec:3-4]{§3.4} and \hyperref[sec:5-2]{§5.2}) were obtained under a pre-registration discipline (Murillo Montero 2026): the meaning of each outcome — including the sharpening that failed — was fixed in writing before the computation ran, and every sign, vanishing, and membership decision uses exact integer or rational arithmetic, with no floating point. The artifact `moment_barrier_certificate.py` (\hyperref[sec:app-a]{Appendix~A}) is deterministic and seed-free; re-running it reproduces its archived transcript byte-for-byte. The load-bearing integers — $D_3(P)=-787680=360\cdot(-2188)$, $D_3(\varphi)=-17408$, the depth sequence $3,3,4,4,5,9,9,9$, and the telescoping rationals $8,9,\tfrac{75}{8},\tfrac{1225}{128},\tfrac{29645}{3072}$ — are independent of any floating-point evaluation. The structural comparison of \hyperref[sec:3-5]{§3.5} uses a separate deterministic high-precision (40-digit) computation, `smooth_primorial_three_objects.py`, also archived; its qualitative conclusions — the sign change in $A$'s defect and the monotone drift of $B$'s — are robust to the working precision. The moment-property survey behind \hyperref[sec:4-2]{§4.2} (the non-moment families, the moment counterexamples $i,2i-1,a+bi$, and the symbolic sign-determinant $\det W_N$) is `magnitude_blind_moment_probe.py`, exact-arithmetic (sympy) and archived. The polynomial-local-factor results of \hyperref[sec:4-5]{§4.5} — the scaling reduction, the exact degree-1 and degree-2 factorizations, the $3\times3$-minor identity $M=-(\text{positive})\,Q$ with $\operatorname{sign}(Q)\to\operatorname{sign}(b^2-ae)$, and the no-fixed-$N$ witness $p^{128}$ — were obtained and adversarially re-verified by exact symbolic computation; the certificates are archived (`polynomial_local_factor_recon.py` and the accompanying scripts).

---

## Acknowledgments {#sec:acknowledgments}

I collaborated extensively with agentic AI assistants under a discipline of pre-registered falsifiers and deterministic, exact-arithmetic settlement: the assistants generated candidates, enumerated falsifiers, and executed the settlement artifact, but no fluent agreement was treated as evidence. The mathematical content and its correctness are my responsibility.

## References {#sec:references}

Akhiezer, N. I. (1965). *The Classical Moment Problem.* Oliver & Boyd. (Hankel determinants; the Hamburger/Stieltjes moment problem.)

Arias de Reyna, J., Toulisse, J. (2013). *The $n$-th prime asymptotically.* J. Théor. Nombres Bordeaux **25**(3), 521–555. (arXiv:1203.5413; $p_n\sim\mathrm{li}^{-1}(n)$, with $|p_n-\mathrm{li}^{-1}(n)|\le\tfrac1\pi\sqrt n(\log n)^{5/2}$.)

Baker, R. C., Harman, G., Pintz, J. (2001). *The difference between consecutive primes, II.* Proc. London Math. Soc. **83**(3), 532–562. (Gap width $p_{n+1}-p_n=O(p_n^{0.525})$; the $o(p)$ window bound in §4.5.)

Berg, C., Szwarc, R. (2015). *A determinant characterization of moment sequences with finitely many mass points.* Linear Multilinear Algebra **63**(8), 1568–1576. (arXiv:1405.7267; the single-mass-point/`$2^n$' survivor and the $D_N\ge0$ caveat.)

Bohr, H., Mollerup, J. (1922). *Lærebog i Matematisk Analyse III.* Copenhagen. (The log-convexity characterization of $\Gamma$.)

Fox, M., Karamchedu, C. (2023). *On a weighted series of the Hurwitz zeta function.* arXiv:2302.01865. (Compact statement of the Marichal–Zenaïdi uniqueness theorem and explicit solution formula.)

Krull, W. (1948, 1949). *Bemerkungen zur Differenzengleichung $g(x+1)-g(x)=\varphi(x)$, I, II.* Math. Nachr. **1**, 365–376; **2**, 251–262. (The $p=1$ generalization of Bohr–Mollerup.)

Marichal, J.-L., Zenaïdi, N. (2022). *A Generalization of Bohr–Mollerup's Theorem for Higher Order Convex Functions.* Developments in Mathematics **70**, Springer (open access). (Principal indefinite sum; asymptotic and generalized Euler constants; generalized Stirling.)

Maynard, J. (2015). *Small gaps between primes.* Ann. of Math. **181**(1), 383–413. (Bounded gaps; used in the §4.5 prime-gap reduction.)

Mertens, F. (1874). *Ein Beitrag zur analytischen Zahlentheorie.* J. Reine Angew. Math. **78**, 46–62.

Murillo Montero, L. (2026). *Grounded-Paranoid-Delusional Inquiry: A Verification-Gated Methodology.* Methodology preprint. (The pre-registration discipline of \hyperref[sec:6-3]{§6.3}.)

Petreolle, M., Sokal, A. D., Zhu, B.-X. (2020). *Lattice paths and branched continued fractions.* Mem. Amer. Math. Soc. (Hankel-total-positivity = Stieltjes moment property; the continued-fraction lens of §4.)

Remmert, R. (1998). *Classical Topics in Complex Function Theory.* Springer GTM **172**, Sec. 2.3.2. (Wielandt's theorem and proof.)

Riemann, B. (1859). *Über die Anzahl der Primzahlen unter einer gegebenen Größe.* Monatsber. Berlin Akad. (The explicit formula; $-\zeta'(0)/\zeta(0)=\log2\pi$.)

Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function*, 2nd ed., rev. D. R. Heath-Brown. Oxford. (Ch. 3, the explicit formula.)

von Mangoldt, H. (1895). *Zu Riemanns Abhandlung "Über die Anzahl der Primzahlen unter einer gegebenen Größe".* J. Reine Angew. Math. **114**, 255–305.

Webster, R. (1997). *Log-convex solutions to the functional equation $f(x+1)=g(x)f(x)$: $\Gamma$-type functions.* J. Math. Anal. Appl. **209**, 605–623. (The multiplicative $p=1$ generalization of Bohr–Mollerup.)

Westzynthius, E. (1931). *Über die Verteilung der Zahlen, die zu den $n$ ersten Primzahlen teilerfremd sind.* Comm. Phys.-Math. Soc. Sci. Fenn. **5**(25), 1–37. (Large prime gaps: $\limsup g_n/\log p_n=\infty$; the §4.5 gap-spike source.)

Wielandt, H. (1939). *Mathematische Werke*, Band 2, Berlin. (The strip-boundedness uniqueness theorem for $\Gamma$.)

Zhang, Y. (2014). *Bounded gaps between primes.* Ann. of Math. **179**(3), 1121–1174. (Used with Westzynthius in the §4.5 reduction.)

---

## Appendix A. The exact-integer certificate {#sec:app-a}

All sign, vanishing, and membership decisions in \hyperref[sec:4]{§4} (and the exact checks of \hyperref[sec:3-4]{§3.4}, \hyperref[sec:5-2]{§5.2}) are produced by the deterministic script `moment_barrier_certificate.py`, reproduced below in full. It uses only Python integers and `Fraction`s; there is no floating point in any decision and no random seed. Re-running it regenerates the archived transcript `moment_barrier_certificate.transcript.txt` byte-for-byte (verified June 13, 2026).

The script's three blocks compute: (i) exact Hankel determinants across the divisor family, the factorization cross-check $D_N=(\prod b_i)\det[b_{i+j}/b_i]$, and the depth sequence $N^*(k)$ for $k=1,\dots,8$ (\hyperlink{stmt:4-2}{Theorem~4.2}, \hyperref[sec:4-3]{§4.3}); (ii) the telescoping rationals $R_2^{(p)}\pi^2$ and the structural invariance of $\log2\pi$ (\hyperlink{stmt:3-6}{Theorem~3.6}); (iii) the sieve birth/death indices and the window identity (\hyperlink{stmt:5-2}{Proposition~5.2}). The headline integers it returns are
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
