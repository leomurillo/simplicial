# Resolution of Paper 18 Open Problem O: the joint tensor metric is not forced to Bures

*Result note, 2026-06-23.* Develops and resolves **Open Problem O** (Paper 18 Rem 6.4):
*does closed-current/Noether positivity force the joint monotone metric on
$\mathcal D(\mathbb C^2\otimes\mathbb C^3)$, including tensor cross-coherences, to be the
minimal SLD/Bures member?* **Answer: no.** Companion to the D4 resolution
(`D4_resolution_bures_kubo_mori.md`); together they refute the Bures-everywhere assumption
of the quantum line. Cert: `empirical_leverage/C2/cert_openproblemO.py` (6/6 **GREEN**,
numpy, no torch). *Staging note — folds into Paper 18 §6, Paper 23, and Paper III D4 when
those are next touched; nothing here edits a live paper.*

## Why the question is delicate, and how it is resolved

Rem 6.3 already **withdrew** the closed-current route, noting it conflated two distinct
forcings — unitary invariance of a monotone metric (forces $\mathfrak{su}(n)$ per leg,
Thm 6.1) and norm-multiplicative closure (Hurwitz). Because the precise meaning of
"closed-current/Noether positivity" was thereby left ambiguous, we resolve O by a
**dichotomy over its natural readings**, and find that *every* reading fails to force the
minimal member. On $\mathcal D(\mathbb C^2\otimes\mathbb C^3)=\mathcal D(\mathbb C^6)$, with
the Petz family $g^f_\rho(A,A)=\sum_{ij}c^f(\lambda_i,\lambda_j)|A_{ij}|^2$:

**(H) The product structure cannot distinguish any member.** The Morozova–Chentsov weight is
homogeneous of degree $-1$, $c^f(tx,ty)=t^{-1}c^f(x,y)$, for *every* monotone $f$. A direct
consequence (certified): on product states with product-rule tangents
$X_A\otimes\rho_B+\rho_A\otimes X_B$, **every** monotone metric is additive,
$g^f_{\rho_A\otimes\rho_B}=g^f_{\rho_A}\oplus g^f_{\rho_B}$. So "additivity/extensivity of the
conserved charge across the factors" is **metric-agnostic** — it holds for the minimal,
maximal, and Kubo–Mori members alike, and forces nothing.

**(O1) Positivity does not select.** All three members (Bures minimal, Kubo–Mori, RLD maximal)
are strictly positive on genuine tensor cross-coherences (e.g. $|q{=}0,t{=}0\rangle\langle q{=}1,t{=}2|$):
$g^{\mathrm{SLD}}=10.53\le g^{\mathrm{KM}}=12.02\le g^{\mathrm{RLD}}=15.83$. Positivity is satisfied
by the whole Petz corridor; it cannot single out the minimal value.

**(O2) The one canonical selector is dual flatness — and it is Kubo–Mori, not Bures.** The only
property that uniquely pins a monotone metric is being the Hessian of a (additive) potential —
dual flatness. On $\mathcal D(\mathbb C^6)$, including on cross-coherences,
$$g^{\mathrm{KM}}=\textstyle\int_0^\infty\operatorname{Tr}\!\big(A(\rho+s)^{-1}A(\rho+s)^{-1}\big)ds=\operatorname{Hess}(\operatorname{Tr}\rho\log\rho),\qquad g^{\mathrm{Bures}}\neq\operatorname{Hess}$$
(certified on the cross-coherence: $g^{\mathrm{KM}}=12.0160=$ BKM integral, $g^{\mathrm{Bures}}=10.5263\neq$).
Kubo–Mori is the unique dually-flat monotone metric (Grasselli–Streater). So if any canonical
principle pins the joint metric, it pins **Kubo–Mori** — which is *not* minimal.

**(O3) Verdict.** The minimal (Bures) member is forced by **none** of the three —
{homogeneous additivity, positivity, dual flatness}. **Open Problem O resolves negative for its
conjectured Bures answer.**

## What this means for the program

- **The metrics agree on everything classical/separable** (diagonal states and product-rule
  tangents — by homogeneity) and **differ only on genuine entangled cross-coherences**; there,
  positivity is inert and dual flatness selects Kubo–Mori. So the Petz–Bures "crystallization
  layer" does *not* crystallize onto Bures.
- **The gauge recovery survives untouched.** The $\mathfrak{su}(2)\oplus\mathfrak{su}(3)$
  algebra of Thm 6.1 follows from unitary invariance alone, which is metric-agnostic — it holds
  for every monotone metric. So refuting the Bures forcing does **not** disturb the gauge content.
- **The necessity claim should be re-labelled.** Paper 18's Conclusion ("its necessity is
  Petz–Bures rigidity") is, for the *connection/cumulant* structure, **Petz–Kubo–Mori** rigidity
  (dual flatness); Bures retains the *estimation/QFI* role and the metric-agnostic Nambu dynamics.
  This is the tensor-product face of the D4 resolution: at single-factor and tensor-product level
  alike, the additive/dually-flat structure is Kubo–Mori, never the minimal Bures member.

## What remains genuinely open

A *specific*, fully-formalized "closed-current/Noether positivity" functional could in principle
impose a constraint not covered by the three readings above. But since that route was withdrawn
(Rem 6.3) and any monotone metric is positive, unitarily invariant, and product-additive, no such
functional built from positivity/extensivity/invariance can recover Bures. A forcing of the
minimal member would require a genuinely new principle (e.g. an estimation-optimality / QFI-saturation
condition) — which is the Bures *estimation* role, not a "positivity" one.

## Suggested manuscript updates (when touched)

- **Paper 18 Rem 6.4 / Conclusion**: record O as resolved-negative; relabel the connection-layer
  necessity Kubo–Mori (dual flatness), keep Bures for QFI/estimation; note the gauge algebra is
  metric-agnostic.
- **Paper III D4**: O is the tensor-product confirmation — single-factor and joint metric both
  pin to Kubo–Mori for the dual-flat structure.

## Files

- `empirical_leverage/C2/cert_openproblemO.py` (6/6 GREEN).
- Companion: `D4_resolution_bures_kubo_mori.md`. Source: Paper 18 Rem 6.3/6.4, T24 Thm 5.1.
