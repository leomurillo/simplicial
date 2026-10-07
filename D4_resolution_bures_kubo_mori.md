# Resolution of Paper III Open Problem D4: the quantum moving cubic is Kubo–Mori, not Bures

*Result note, 2026-06-23.* Follow-up to leverage item C2 (finding F2). Resolves Paper III's
open problem **D4** (the quantum continuation of the moving Amari–Chentsov cubic) and the
apparent Bures-vs-Kubo–Mori inconsistency in the program's quantum line (Papers 15/18/44 vs
T24). Cert: `empirical_leverage/C2/cert_bures_km_resolution.py` (qubit, 6/6 **GREEN**, numpy,
no torch). *Staging note — substance folds into Paper III (D4 entry), Paper 18 §6, and T24 §6
when those manuscripts are next touched; nothing here edits a live paper.*

## The fork

- The cubic-**mechanics** line (Papers 15/18/44) takes the metric to be **Bures**, selected by
  "the monotone metric whose Nambu flow is the von Neumann flow $\dot\rho=-i[H,\rho]$"
  (Paper 15 Thm 3.2; Paper 18 §4).
- Paper III's **information geometry** — Fisher $=\operatorname{Hess}$(negative entropy), the
  $\alpha$-collapse $\Gamma^{(\alpha)}=-\tfrac{1+\alpha}{2}T$, dual flatness, the cumulant tower —
  is a *dually-flat* structure, and the **unique** dually-flat monotone metric is **Kubo–Mori**
  (Grasselli–Streater; T24 Thm 5.1). T24 §6 already flagged that Paper 18/T7 silently wrote
  "Bures" where additivity wants Kubo–Mori.

## The resolution (three certified facts → role separation)

**1. The von-Neumann criterion is metric-agnostic; the Bures selection is under-determined.**
Paper 15 Thm 3.2's proof (lines 120–127) uses *only* "the Bures metric is invariant under
unitary conjugation $\Rightarrow$ its volume form is invariant $\Rightarrow$ $Y_H=-i[H,\rho]$ is
divergence-free." Nothing Bures-specific enters. **Every** monotone metric is unitarily
invariant, so the identical theorem holds for the volume form of every $g^f$ — Kubo–Mori, RLD,
all of them. Hence "the metric whose Nambu flow is von Neumann" does *not* single out Bures.
*Certified (M1): $g^f$ is unitary-invariant for $f\in\{$SLD/Bures, Kubo–Mori, RLD$\}$ to
$1.3\times10^{-13}$.*

**2. Kubo–Mori is the dual-flat / entropy-Hessian metric — the quantum continuation of Paper III.**
Paper III's foundational identity is "Fisher $=\operatorname{Hess}(\sum_i p_i\log p_i)$, hence
dually flat" (§3). Its quantum continuation is **Kubo–Mori $=\operatorname{Hess}(\operatorname{Tr}\rho\log\rho)$**
(the BKM metric), *not* Bures:
$$g^{\mathrm{KM}}_\rho=\int_0^\infty \operatorname{Tr}\!\big(A(\rho+s)^{-1}A(\rho+s)^{-1}\big)\,ds=\operatorname{Hess}(\operatorname{Tr}\rho\log\rho),\qquad g^{\mathrm{Bures}}\neq\operatorname{Hess}.$$
*Certified (M2), qubit coherence direction: $g^{\mathrm{KM}}=$ BKM integral $=\operatorname{Hess}(\operatorname{Tr}\rho\log\rho)$ to $10^{-4}$ at $r\in\{0.2,0.5,0.8\}$ (e.g. $4.05465$ all three), while $g^{\mathrm{Bures}}=4.000\neq$.* So Paper III's $\alpha$-collapse / dual-flat / cumulant structure continues on Kubo–Mori; Bures is the minimal/estimation member ($4g^{\mathrm{SLD}}=$ QFI) and is not dually flat.

**3. They agree where Paper III lives — so there is no contradiction, only role separation.**
On the decoherent face (diagonal $\rho$ = the classical submanifold Paper III actually parametrizes)
and at the maximally-mixed center, *all* monotone metrics coincide ($c^f(\lambda,\lambda)=1/\lambda$).
*Certified (M3): all three metrics agree on the diagonal tangent (= classical Fisher) to $10^{-9}$,
and Bures$=$Kubo–Mori at the center.* The fork opens only on coherences.

## What this means for the corpus

- **Paper III D4 is answered:** the quantum moving cubic's *connection / dual-flat / cumulant*
  structure is carried by **Kubo–Mori**. The diagonal AC-tensor *value* is metric-independent
  (so Paper 15 Thm 2.2 and Paper 44 Lemma 4.1's classical recovery are correct as stated — they
  live on the decoherent face); the metric choice bites only on the off-diagonal connection data,
  and there the dually-flat structure forces Kubo–Mori.
- **Paper 18 Thm 6.1's Bures selection is under-determined** by its stated von-Neumann criterion
  (fact 1). This is not a defect in the *classical-recovery* results; it means the "Bures" label on
  the **connection/additivity** structure should be **Kubo–Mori**, confirming T24 §6's audit.
- **Role separation (the clean statement):** **Bures** = estimation/QFI geometry + the (metric-
  agnostic) Nambu dynamics; **Kubo–Mori** = the dual-flat connection that carries the $\alpha$-family,
  the cumulant tower, and the relative-entropy/Bregman structure. They agree on the classical
  submanifold and at the center; they are not competitors for one role.

## What this does *not* resolve

Paper 18 Rem 6.4 (Open Problem O — does closed-current positivity force the *joint* monotone metric
on $D(\mathbb{C}^2\otimes\mathbb{C}^3)$ to be minimal/Bures?) is a **distinct** node: it concerns
the tensor-product positivity selection, not the single-factor dual-flat selection settled here.
O remains open.

## Suggested manuscript updates (when touched)

- **Paper III**, D4 entry: "the quantum continuation is Kubo–Mori $=\operatorname{Hess}(\operatorname{Tr}\rho\log\rho)$, the unique dually-flat monotone metric; Bures agrees on the diagonal and carries the estimation/QFI role."
- **Paper 18 §6 / Paper 44 §1.3**: relabel the *connection/additivity* structure Kubo–Mori (keep Bures for QFI/estimation and the diagonal recovery); cite T24 §6 and this resolution; note Thm 3.2 selects no metric.
- **T24 §6**: this is the explicit qubit confirmation of the §6 recommendation.

## Files

- `empirical_leverage/C2/cert_bures_km_resolution.py` (6/6 GREEN).
- Source criteria verified: `15.information_geometric_mechanics_on_the_density_matrix_manifold.md` Thm 3.2 (proof lines 120–127); `T24-ChentsovPetzMonotoneMetricFork-Draft1.md` Thm 5.1 / §6.
