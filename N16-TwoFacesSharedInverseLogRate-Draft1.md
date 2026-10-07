# N16 — The Two Faces of RH Converge at One Inverse-Log Rate

## A Cross-Face Structural Note on the Nyman–Beurling and Connes–Consani Approaches

**Leonardo Murillo Montero**

*Independent researcher — leonardo.murillo@gmail.com*

*First draft — June 9, 2026*

<!--
Program record (not part of the paper). Sixteenth note of the Numbers (N-) series. STRUCTURAL/EXPOSITORY
note, NOT a research contribution toward a proof; does NOT prove RH. Honest scope: the per-face inverse-log
results are KNOWN (BDBLS 2000 for Nyman–Beurling–Báez-Duarte; Śliwiński arXiv:2601.12133 / Heisenberg for
the CCM scaling operators). The NEW content here is only the cross-face OBSERVATION: the two most
structurally opposite equivalent forms of RH — an L^2 approximation distance and a spectral approximation
error — share the same 1/log convergence rate, governed by the same archimedean log-window (log-conductor)
scale, and RH is in both "the inverse-log-limited sequence reaches its floor." This upgrades the program's
'conservation of difficulty' (N11) from QUALITATIVE (all routes reduce to one step) to QUANTITATIVE (all
routes approach it at the same RATE). It is a unification of intuition, not a lever: both faces still
bottleneck on the limit→0, which is RH, left open. Tiering: the two per-face statements = [P] (cited);
the cross-face shared-rate reading = [A] (structural analogy, this note). Certificate:
empirical/p_infinity/probe_baezduarte_inverselog.py — GREEN (25 dps): the bridge invariant
Sum_rho 1/|rho|^2 = 2 + gamma - log(4 pi) = 0.0461914 confirmed against the zero-sum (200 zeros + tail) to 1e-5.
Anchors: N11 (conservation of difficulty / the one wall), N14–N15 (the archimedean potential), the CCM
prolate convergence (arXiv:2511.22755) and its spectral analysis (Śliwiński, arXiv:2601.12133).
-->

---

> **Status (read first).** This is a *structural note*, not a step toward a proof, and it does not prove
> the Riemann Hypothesis. Both per-face convergence results quoted below are established in the literature.
> The only thing offered here is the observation that they are the *same* rate, governed by the *same*
> scale — a quantitative sharpening of the heuristic that every route to RH meets the same obstruction.

---

## 1. Two opposite faces

The Riemann Hypothesis has many equivalent formulations; two of them sit at opposite ends of the subject.

**The approximation face (Nyman–Beurling–Báez-Duarte).** RH holds **iff** $d_N \to 0$, where
$$
d_N^2 \;=\; \inf_{D_N}\;\frac{1}{2\pi}\int_{-\infty}^{\infty}\Bigl|\,1-\zeta\!\left(\tfrac12+it\right)D_N\!\left(\tfrac12+it\right)\Bigr|^2\,\frac{dt}{\tfrac14+t^2},
$$
the infimum over Dirichlet polynomials $D_N(s)=\sum_{n\le N}a_n n^{-s}$. This measures how well the constant
function $1$ is approximated by dilates of $\zeta$ truncated to $N$ terms. Báez-Duarte–Balazard–Landreau–Saias
(2000) showed the decay is **inverse-logarithmic**, with
$$
\liminf_{N\to\infty}(\log N)\,d_N^2 \;\ge\; \sum_{\rho}\frac{1}{|\rho|^2},
\qquad\text{and conjecturally}\qquad d_N^2 \sim \frac{\sum_\rho |\rho|^{-2}}{\log N}.
$$

**The spectral face (Connes–Consani–Moscovici).** The finite-prime scaling operators $D_{\log}^{(\lambda,N)}$
(the compression of the scaling generator $\hat D=-i\,d/du$, $[\hat u,\hat D]=iI$, onto a log-window of
length $2\ln\lambda$, with the rank-one Weil constraint) are self-adjoint, so their eigenvalues
$\{\nu_k\}$ are **real**; they approximate the zeros $\{\zeta_k\}$. RH holds **iff** the uniform error
$\mathcal E(\lambda,N)=\max_k|\nu_k-\zeta_k|\to 0$. Śliwiński (arXiv:2601.12133) proves the mean error is
**inverse-logarithmic from below**,
$$
\varepsilon(\lambda,N)\;\ge\;\frac{1}{4\ln\lambda},
$$
directly from the Heisenberg–Pauli–Weyl uncertainty $\sigma_u\sigma_\zeta\ge\tfrac12$ on the log-window
$\sigma_u\le 2\ln\lambda$.

## 2. One rate, one scale, one bridge invariant

The two faces could hardly be more different — one is a least-squares approximation of $1$ by dilated
fractional parts, the other is the spectrum of an explicit self-adjoint operator built from the primes.
Yet **both converge at the inverse-logarithmic rate $1/\log$**, and for the same reason: a budget of $N$
terms (or a window $\lambda$) resolves only $\sim\log N$ (resp. $\sim\ln\lambda$) *independent
logarithmic scales* — the primes up to $N$ span $\log N$ in $\log$-scale; the CCM window spans $2\ln\lambda$.
The convergence is throttled by the number of resolved scales of the **archimedean log-window
(the log-conductor)**, identical on both sides.

The **bridge invariant** is the zero-sum
$$
\boxed{\;\sum_{\rho}\frac{1}{|\rho|^{2}} \;=\; \sum_{\rho}\frac{1}{\rho(1-\rho)} \;=\; 2+\gamma-\log(4\pi)\;=\;0.0461914\ldots\;}
$$
(the second equality is the unconditional Hadamard identity; on the critical line
$|\rho|^2=\rho(1-\rho)$). It sets the floor of the approximation face exactly, and is confirmed
numerically against the zero-sum to $10^{-5}$ (certificate). The spectral face's floor $1/(4\ln\lambda)$
is the uncertainty constant rather than this invariant — the two constants differ — but the *rate* and the
*mechanism* (the log-window resolution) are shared.

## 3. Quantitative conservation of difficulty

N11 records the heuristic that every independent route to RH terminates at the same obstruction (the
archimedean spectral realization / the domination $A\ge P$). This note sharpens that statement: the routes
do not merely reduce to the same step — **they approach it at the same rate.** Both faces are
inverse-log-limited sequences, and in each,
$$
\text{RH} \iff \text{the inverse-log-limited sequence actually reaches its floor.}
$$
This explains, in one stroke, why *finite* witnesses fail **uniformly** on every face: the convergence is
intrinsically logarithmic, so the entire arithmetic content lives in the slow tail — precisely the
sensitivity to an off-critical zero (which, on the approximation face, would lift $\sum_\rho|\rho|^{-2}$
above its on-line value, and on the spectral face would prevent a real eigenvalue from tracking a complex
zero). The shared $1/\log$ rate is the quantitative signature of the program's single wall.

## 4. Honest scope

This is a unification of *intuition*, not a *lever*. Neither face is advanced toward closure here; both
still bottleneck on the limit reaching its floor, which is RH. The value of the observation is diagnostic:
it identifies the inverse-log rate, set by the archimedean log-window, as the invariant difficulty shared
by the two most distant formulations — and thereby tells any would-be prover that a successful argument
must control a *logarithmically slow tail*, on whichever face it operates. It claims nothing more.

---

*Certificate.* `empirical/p_infinity/probe_baezduarte_inverselog.py` (GREEN, 25 dps): confirms
$\sum_\rho |\rho|^{-2}=2+\gamma-\log(4\pi)$ to $10^{-5}$ and tabulates the two per-face inverse-log laws.
