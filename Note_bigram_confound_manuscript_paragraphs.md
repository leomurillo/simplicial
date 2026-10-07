# Manuscript paragraph drafts — bigram-confound control

**Use:** after running `empirical/bigram_corpus_control.py` against C4 (or
another large public corpus), pick the paragraph that matches the outcome
and insert it into §4.1, immediately after the existing paragraph that ends
"… is a real off-centroid arithmetic feature, not a single-model artifact."

**Actual C4 outcome, May 14, 2026:** Variant B.  The completed
`allenai/c4` English run used 27,548 documents and exactly 10,000,000
whitespace tokens.  The headline transposed-alignment rows were:
Llama weekdays \(r=0.424\), sign agreement \(9/21\) at \(w=3\);
Mistral weekdays \(r=0.690\), sign agreement \(10/21\) at \(w=3\)
and \(r=0.739\), sign agreement \(10/21\) at \(w=5\); Llama months
\(r=0.359\), sign agreement \(35/60\) at \(w=3\).  This is the
pre-registered intermediate band: corpus bigrams partially explain the
transposed magnitude pattern, especially on Mistral, but do not fully
explain the sign pattern.

The two parametric numbers in each paragraph — `<R_VALUE>` and
`<SIGN_FRAC>` — should be filled from the corresponding row of the report's
**headline (max-|r| alignment)** table. Use the alignment label
(typically "transposed", reflecting the centroid-confusion vs.
corpus-sequence index convention).

A short shared preamble can introduce the control consistently in all
three variants:

> **Linguistic-bigram control.** A natural alternative explanation for the
> observed predecessor-bias asymmetry is that the model has internalized
> pretraining bigram frequencies — sequences such as "Sunday Monday" or
> "December January" being more frequent than their reverses. To test this,
> we computed co-occurrence statistics on a $10^7$-token sample of the C4
> English crawl (a published proxy for the web-text distribution used by
> both Llama-3.1 and Mistral-7B), at token-distance windows
> $w \in \{1, 3, 5, 10\}$. Letting $M_{\text{corp}}$ be the
> $7\times 7$ raw co-occurrence matrix, we compared the centroid asymmetry
> $A^{\text{emp}} = M_{\text{cent}} - M_{\text{cent}}^\top$ against both
> the same-alignment and transposed-alignment corpus asymmetries. (The
> transposed alignment is the one that corresponds to the reviewer's
> hypothesis: a pretraining bigram "$d_i$ followed by $d_j$" deposits mass
> at $M_{\text{corp}}[i, j]$, which would manifest in the model's
> confusion matrix at $M_{\text{cent}}[j, i]$ — true class $d_j$ leaking
> probability to label $d_i$.) Reported below is the headline Pearson
> $r$ between $A^{\text{emp}}$ and the alignment-appropriate corpus
> asymmetry, along with the sign-agreement rate on nonzero entries.

---

## Variant A — bigrams do NOT explain ($r \le 0.20$ AND sign-agree $\le 13/21$)

This is the outcome the manuscript currently assumes implicitly. Use this
paragraph if the empirical numbers fall into the pre-registered
"do not explain" band.

> The control gives headline transposed-alignment Pearson $r =$ **`<R_VALUE>`**
> with sign agreement **`<SIGN_FRAC>` / 21**. Both fall in the
> pre-registered "bigrams do not explain" band; corpus bigram statistics
> reproduce neither the magnitude nor the direction of the centroid
> asymmetry to within statistical reach. The asymmetric predecessor
> leakage is therefore a structural property of the model's representation,
> not a frequency-prior shadow of pretraining text. The "real off-centroid
> arithmetic feature" framing stands.

---

## Variant B — INTERMEDIATE (somewhere in the middle band)

This is the most likely outcome given the canned-corpus pilot
($r \approx 0.79$ with only 25 sentences) and is the honest scientific
landing zone.

> The control gives headline transposed-alignment Pearson $r =$ **`<R_VALUE>`**
> with sign agreement **`<SIGN_FRAC>` / 21**. This is consistent with
> both bigram and finite-arithmetic explanations of the asymmetry: the
> sequential "$d_i$ followed by $d_j$" co-occurrence pattern is correlated
> with the model's predecessor leakage, but does not fully determine
> it. We therefore weaken the qualitative claim: the asymmetric off-diagonal
> structure reflects *both* a learned pretraining-sequence prior and an
> off-centroid signal the cubic diagnostic registers. The orthogonal
> evidence — the moment-vs-Hellinger correlation drop (§4.1), the
> CRT conductor-energy spread on $C_{12}$ (§5.1), and the
> activation-pullback near-isometry (§7.2.1) — does not depend on the
> directional asymmetry and is unaffected by this finding.

---

## Variant C — bigrams FULLY explain ($r \ge 0.70$ AND sign-agree $\ge 18/21$)

This outcome would require retracting the strongest version of the
asymmetric-leakage claim. Use this paragraph if the empirical numbers
fall into the pre-registered "fully explain" band.

> The control gives headline transposed-alignment Pearson $r =$ **`<R_VALUE>`**
> with sign agreement **`<SIGN_FRAC>` / 21**, both above the
> pre-registered "bigrams fully explain" thresholds. The directional
> asymmetry observed in the centroid matrices is therefore predicted by
> ordinary pretraining-bigram statistics; we retract the framing of this
> asymmetry as a "real off-centroid arithmetic feature." The
> moment-vs-Hellinger correlation drop (§4.1), the CRT conductor-energy
> spread on $C_{12}$ (§5.1), and the activation-pullback near-isometry
> (§7.2.1) do not depend on the directional asymmetry and remain the
> primary empirical support for the cubic diagnostic; the asymmetry
> paragraph is now scoped as a *finding about pretraining text*, not as
> independent confirmation of the $K^{CH}$ thesis.

---

## Where else to update

If Variant C is the outcome, the matching language in **§11 ("The Launch
Pitch")** must also be edited. The current text on
[line 1334](single-discrete_fisher_skeletons_for_ai_optimization.md:1334):

> Both centroid matrices show asymmetric leakage: every weekday leaks more
> probability mass to its cyclic predecessor than to its successor,
> breaking the dihedral symmetry the proxy assumed.

should be reduced to a factual observation without the "breaking the
dihedral symmetry" framing being credited to the model — instead crediting
it to the pretraining distribution. Suggested replacement:

> Both centroid matrices show a consistent predecessor-direction asymmetry
> in their off-diagonal entries; this asymmetry tracks ordinary
> pretraining-bigram statistics and is reported here only to characterize
> the centroid surface. The diagnostic signal of interest is the
> moment-vs-Hellinger correlation drop and the conductor-energy spread,
> neither of which is bigram-explainable.

If Variant B is the outcome, no further edits are needed beyond the §4.1
paragraph replacement.

If Variant A is the outcome, the existing language stands and a one-line
footnote referencing the control is sufficient:

> *A pretraining-bigram control on a $10^7$-token C4 sample finds the
> centroid asymmetry uncorrelated with corpus co-occurrence asymmetry
> ($r =$ `<R_VALUE>`); see `Note_bigram_confound_design.md` and the
> generated report under `empirical/reports/`.*
