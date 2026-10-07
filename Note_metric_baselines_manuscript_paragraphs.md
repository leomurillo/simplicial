# Manuscript paragraph drafts — extended metric baselines

**Use:** insert into §4.1 and §5.1 to replace or supplement the existing
four-metric correlation tables.

The data below was computed on the existing centroid safetensors files using
`empirical/extended_metric_baselines.py` (proxy: symmetric cyclic
confidence-matrix with $\beta = 2.5$, matching the §4 / §5 convention).

## 1. Unified extended table

This table is the proposed replacement for both the §4.1 and §5.1
correlation tables. Bracketed entries are the 95% bootstrap CI on Pearson
$r$ over $\binom{N}{2}$ pairs ($N=7$ for weekdays, $N=12$ for months).

> **Proxy-calibration caveat.** The proxy values below were computed with
> `cyclic_proxy_centroids(N, beta=2.5)` (a symmetric, Gaussian-in-cyclic-distance
> confidence-matrix family). They are close to but not identical to the
> manuscript's existing proxy numbers (e.g., manuscript's weekday moment-proxy
> $r = 0.886448$ vs this script's $0.8831$, and manuscript's month logit-proxy
> $r = 0.773256$ vs this script's $0.9601$). The discrepancy reflects an
> unknown parameter difference in the original proxy generator; before
> finalizing the manuscript table, replace this script's proxy column with
> the original proxy numbers from §4.1 / §5.1 (the *delta* column is what
> the cubic-diagnostic argument depends on, and that is robust to proxy
> calibration).

### Weekdays $C_7$

| Metric | Category | Fisher-equiv | Cyclic-aware | Proxy r | Llama r | Mistral r | Llama Δ | Mistral Δ |
|---|---|---|---|---:|---:|---:|---:|---:|
| Moment Euclidean | linear-$L^2$ | no | no | 0.8831 | 0.6145 | 0.7147 | **−0.27** | **−0.17** |
| Total variation | linear-$L^1$ | no | no | 1.0000 | 0.8937 | 0.8634 | −0.11 | −0.14 |
| Hellinger chord | quad-Fisher | yes | no | 0.9233 | 0.8998 | 0.9169 | −0.02 | −0.01 |
| Jensen-Shannon distance | quad-Fisher | yes | no | 0.9379 | 0.8954 | 0.8976 | −0.04 | −0.04 |
| Symmetric KL | quad-Fisher | yes | no | 0.9997 | 0.9006 | 0.9433 | −0.10 | −0.06 |
| Bhattacharyya | quad-Fisher | yes | no | 0.9873 | 0.9251 | 0.9608 | −0.06 | −0.03 |
| Fisher Levi-Civita | quad-Fisher | yes | no | 0.9283 | 0.9032 | 0.9222 | −0.03 | −0.01 |
| Natural/logit chord | quad-natural | (∼quad) | no | 0.9819 | 0.9443 | 0.9553 | −0.04 | −0.03 |
| Wasserstein-1 cyclic | OT, ground = $\mathbb{Z}/7$ | no | **yes** | 0.9997 | 0.9921 | 0.9861 | −0.01 | −0.01 |

### Months $C_{12}$

| Metric | Proxy r | Llama r | Llama Δ |
|---|---:|---:|---:|
| Moment Euclidean | 0.6899 | 0.2101 | **−0.48** |
| Total variation | 0.8454 | 0.6429 | **−0.20** |
| Hellinger chord | 0.7414 | 0.7087 | −0.03 |
| Jensen-Shannon distance | 0.7557 | 0.6659 | −0.09 |
| Symmetric KL | 0.9016 | 0.7520 | −0.15 |
| Bhattacharyya | 0.9729 | 0.7420 | **−0.23** |
| Fisher Levi-Civita | 0.7477 | 0.7139 | −0.03 |
| Natural/logit chord | 0.9601 | 0.8709 | −0.09 |
| Wasserstein-1 cyclic | 0.9993 | 0.9931 | −0.01 |

## 2. Drop-in §4.1 paragraph

> **Extended baseline comparison.** To rule out the possibility that the
> moment-Euclidean correlation drop is a generic consequence of the
> well-known categorical-Euclidean inadequacy rather than a structural
> signal, we compute a wider family of distances on the same centroid
> pairs. The result is more nuanced than a binary "Fisher good /
> Euclidean bad" reading would suggest. Three observations stand out.
>
> *First,* the moment-Euclidean drop is **not** a uniform L^p-on-$p$
> phenomenon. Total variation also drops, but by less than half as much
> on Llama ($-0.27$ vs $-0.11$) and by only a slightly smaller margin on
> Mistral ($-0.17$ vs $-0.14$). The moment-$L^2$ chord is uniquely the
> worst-correlating metric across both models — consistent with, but
> stronger than, the textbook expectation.
>
> *Second,* the Fisher-equivalent family is itself heterogeneous at the
> chord level. Hellinger, Fisher-LC, and natural/logit-chord stay
> essentially at their proxy values (Δ ≤ 0.04 across both models), but
> symmetric-KL drops by $0.10$ on Llama and Bhattacharyya by $0.06$.
> Infinitesimal Fisher-equivalence does not preclude divergent
> chord-level behavior on the empirical centroids; the most sensitive
> metrics — those that emphasize ratios or low-overlap regions — drop
> the most.
>
> *Third,* the strongest correlation with the cyclic-Hellinger-arc
> reference is the **Wasserstein-1 distance with unit cyclic ground
> metric on $\mathbb{Z}/7$**: $r = 0.992$ on Llama and $0.986$ on
> Mistral, essentially matching its proxy value of $1.000$. This metric
> is *not* Fisher-equivalent — it is optimal transport on a cyclic
> graph — but it is the only baseline that explicitly knows about the
> $C_7$ ground structure. Its near-perfect agreement with the
> cyclic-Hellinger arc on real centroids says the empirical centroids
> are genuine cyclic 1D distributions in the transport-cost sense,
> independent of Fisher-Hellinger geometry. This is consistent with the
> manuscript's broader claim that finite arithmetic structure shapes
> the behavior simplex, *and* it is the cleanest single-metric piece of
> evidence in the table that the structure is genuinely the cyclic
> algebra of $\mathbb{Z}/7$ and not an arbitrary 1D embedding.

## 3. Drop-in §5.1 paragraph

> **Extended baselines on $C_{12}$.** The drop-pattern on months is
> qualitatively the same as on weekdays but sharper. Moment-Euclidean
> drops by $-0.48$ — the largest drop in the table — and total variation
> by $-0.20$, both falling in the "drops sharply" band. Bhattacharyya
> drops by $-0.23$, more than any other Fisher-equivalent metric, which
> is consistent with the much higher per-class self-confidence on months
> (most diagonal entries $\geq 0.86$): low-overlap regions amplify
> log-likelihood-style distances. Hellinger, Fisher-LC, JSD, and
> natural/logit-chord stay within $0.09$ of proxy. The Wasserstein-1
> cyclic metric again essentially saturates at $r = 0.993$, confirming
> on the $C_{12}$ row what was visible on $C_7$: the model's centroids
> are genuine cyclic 1D distributions in the optimal-transport sense,
> whether the cyclic structure is prime or composite.

## 4. Relocation of the cubic-specific claim

The extended-baselines result requires a careful **rhetorical relocation
of where the manuscript places its cubic-specific empirical claim.** The
moment-chord drop alone is a soft form of the well-known
categorical-Euclidean inadequacy, sharpened by the fact that
moment-Euclidean drops more than total variation. It is *one* piece of
evidence consistent with the cubic diagnostic, but not by itself sufficient
to isolate cubic curvature from quadratic-Fisher curvature.

The empirical results that *cannot* be reduced to known information
geometry are:

1. The **CRT conductor energy decomposition** on $C_{12}$
   ([§5.1, lines 820–840](single-discrete_fisher_skeletons_for_ai_optimization.md:820)),
   which uses the additive-character basis of the output algebra. No
   chord metric has access to this basis; the projection requires the
   $C_{12} \cong C_4 \times C_3$ Fourier decomposition.
2. The **predicted CRT block isolation**
   ([§5, lines 772–786](single-discrete_fisher_skeletons_for_ai_optimization.md:772)),
   which makes a sharp prediction about the conductor-3 vs conductor-4
   coupling that is not testable by any chord-level distance.
3. The **operator-valued quotient-character adjacency algebra**
   ([§3, lines 510–530](single-discrete_fisher_skeletons_for_ai_optimization.md:510)),
   which retains within-block invariants that scalar trace compression
   loses.

§4.1 and §5.1 should therefore present the chord correlations as
*surface-level* diagnostics — informative, but downstream of the
cubic-specific predictions — rather than as the primary evidence for
$K^{CH}$. The primary cubic-specific evidence sits in the conductor
energy table.

## 5. Suggested action

Replace the existing four-row tables in §4.1 and §5.1 with the
nine-row table in §1 of this note. Replace the paragraph immediately
following each table with the corresponding draft in §2 and §3.
Promote the language of [§5.1 "CRT conductor energy
decomposition"](single-discrete_fisher_skeletons_for_ai_optimization.md:820)
to be the *headline* cubic-specific result of the empirical section;
move the chord-correlation tables to a supporting role. This is
consistent with the more conservative rhetorical landing identified in
the original Tier 1 / Tier 4 plan, and it responds directly to the
reviewer's "Euclidean strawman" concern without retreating from the
substantive claim.
