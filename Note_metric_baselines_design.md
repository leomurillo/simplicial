# Extended Metric Baselines for the §4.1 / §5.1 Correlation Tables

**Status:** design note, May 2026
**Defends against:** the "moment-Euclidean strawman" critique — that the
reported drop of moment-Euclidean correlation from $r \approx 0.886$ to
$r \approx 0.615$ on Llama weekdays only re-establishes the well-known fact
that Euclidean metrics are inappropriate for categorical distributions, and
does *not* show that the Amari-Chentsov cubic $K^{CH}$ is doing specific work.

## 1. What the manuscript currently reports

[§4.1 table](single-discrete_fisher_skeletons_for_ai_optimization.md:680) on
the $C_7$ weekday row carries four metrics:

| Metric | Llama drop vs proxy | Class |
|---|---|---|
| Hellinger chord | 0.910 → 0.900 | Fisher-equivalent quadratic, Euclidean on $\sqrt{p}$ |
| Moment Euclidean chord | 0.886 → **0.615** | Linear in $p$, not Fisher-aware |
| Natural/logit chord | 0.941 → 0.944 | Quadratic in natural parameters |
| Fisher Levi-Civita | 0.912 → 0.903 | Quadratic on the manifold |

The story as currently told: moment-Euclidean drops sharply; everything else
holds at proxy levels.

The reviewer's reading: this is exactly the textbook information-geometry
finding that Euclidean-on-$p$ is bad for categorical distributions. The
result does not isolate cubic-specific structure; it isolates the well-known
inadequacy of $L^2$ on the simplex.

## 2. What the additional baselines test

The space of metrics on $\Delta_R^\circ$ stratifies along three axes:

1. **Order in $(p-q)$:** linear (TV), quadratic (Hellinger, moment-Euclidean,
   sym-KL, JSD, Bhattacharyya, Fisher-LC), or none (Wasserstein on a graph
   ground metric).
2. **Fisher-equivalence at small distance:** Hellinger, JSD, sym-KL, and
   Fisher-LC are all infinitesimally proportional to the Fisher metric.
   Moment-Euclidean, TV, and Wasserstein are not.
3. **Awareness of the cyclic ground structure on $\mathbb{Z}/N$:** moment,
   Hellinger, logit, Fisher-LC, JSD, sym-KL, and Bhattacharyya are
   *coordinate-permutation-invariant* — they do not use the cyclic structure.
   The cyclic-Hellinger-arc reference does. Wasserstein-1 with cyclic ground
   metric does too — and uniquely among the new baselines, in a non-Fisher
   way.

The seven baselines we add or keep:

| Metric | Order in $(p-q)$ | Fisher-equiv | Cyclic-aware |
|---|---|---|---|
| Moment Euclidean | $L^2$ | no | no |
| Total variation | $L^1$ | no | no |
| Hellinger chord | quadratic on $\sqrt{p}$ | yes | no |
| Jensen-Shannon distance | quadratic Fisher-eq | yes | no |
| Sym-KL | $\sum (p-q)\log(p/q)$ | yes | no |
| Fisher Levi-Civita arc | exact Fisher | yes | no |
| Natural / logit chord | $L^2$ in $\log p$ | quadratic-aware | no |
| Bhattacharyya | $-\log\sum\sqrt{pq}$ | yes (≃ Hellinger) | no |
| Wasserstein-1 cyclic | optimal transport | no | **yes** |

## 3. Pre-registered interpretation matrix

Let $\Delta_X$ denote the drop in Pearson $r$ vs. the cyclic-Hellinger-arc
proxy, for metric $X$.

| Pattern | Reading |
|---|---|
| Only moment Euclidean drops; TV holds | The drop is specifically $L^2$ on $p$. Probably real but very narrow. |
| Both moment and TV drop substantially; all Fisher-equiv metrics hold | The "Euclidean strawman" critique is **correct** — both linear-in-$p$ metrics fail uniformly. The §4.1 framing should pivot: the moment drop demonstrates the standard Euclidean inadequacy, *not* a cubic-specific phenomenon. Tighten the manuscript to make the cubic claim depend on the CRT energy decomposition (§5.1) and the conductor-operator predictions, not on the moment correlation alone. |
| Both moment and TV drop, and *some* Fisher-equiv metric (e.g. sym-KL) ALSO drops more than others | There is a quadratic-vs-cubic distinction at the chord level. The metric with the largest drop is the one most sensitive to the off-centroid structure; investigate whether it correlates with $\|K^{CH}(h_i)\|_F$. |
| Wasserstein-1 cyclic stays as high as Hellinger | The cyclic ground structure of $\mathbb{Z}/N$ is correctly internalized by the model's centroid pattern — independently of which Fisher-equivalent metric is used. This is consistent with the manuscript's broader claim that finite arithmetic structure shapes the behavior simplex. |
| Wasserstein-1 cyclic drops while Hellinger holds | The model's centroids agree with Fisher/Hellinger geometry but disagree with optimal transport on the cyclic graph — i.e. the centroids respect categorical statistics but not the *order* on $\mathbb{Z}/N$. Less likely a priori; would be a surprising counter-signal. |

The third row is the only outcome that *adds* to the cubic-specific
narrative beyond what the current §4.1 already says. The second row is the
honest landing zone — it does not destroy the manuscript, but it forces the
asymmetric-leakage / moment-drop narrative to be downgraded from "diagnostic
of cubic curvature" to "consistent with information geometry's standard
Euclidean-inadequacy result." The cubic-specific evidence then rests on
§5.1's CRT conductor split, which is where the theory makes a sharper
prediction than any chord metric can.

## 4. Why this matters even if the answer is "row 2"

The reviewer's strawman concern is correct as a logical matter, and the
manuscript needs to acknowledge it explicitly. The CRT conductor energy
decomposition on $C_{12}$ ([§5.1](single-discrete_fisher_skeletons_for_ai_optimization.md:820))
is the empirical result that *cannot* be reduced to "Euclidean is bad on
the simplex" — the conductor decomposition uses the additive-character
basis of the output algebra, which has no analogue in any of the
non-cubic baselines listed above.

Tier 1.1 thus has two outputs:

1. The extended baselines table itself, which adjudicates whether the
   moment drop is unique to $L^2$ or part of a broader linear-vs-Fisher
   pattern.
2. A rhetorical relocation of the manuscript's cubic-specific claim:
   if Tier 1.1 lands on row 2, then the §4.1 "moment drop = cubic
   diagnostic signature" framing must be downgraded, and the CRT conductor
   decomposition in §5.1 is promoted to the *primary* cubic-specific
   evidence.

## 5. Deliverables

1. `empirical/extended_metric_baselines.py` — adds TV, JSD, sym-KL,
   Bhattacharyya, and Wasserstein-1-cyclic to the existing four metrics;
   recomputes correlations against the cyclic-Hellinger-arc reference;
   writes a unified report.
2. `empirical/reports/extended_baselines_*.md` — generated reports for
   each (task, model) combination already on disk.
3. A short paragraph drop-in for §4.1 of the manuscript reporting the
   outcome and, if needed, narrowing the cubic-specific claim.

The script does not require any new data. It operates on the same
`per_class_output_dists.safetensors` files used by
[compute_weekdays_K_CH_real.py](empirical/compute_weekdays_K_CH_real.py)
and [compute_months_K_CH_real.py](empirical/compute_months_K_CH_real.py).

## 6. Falsifiability note

The thresholds for "drop" should be uniform across metrics for honest
comparison. A natural rule:

- "Holds at proxy" $:= |\Delta_X| < 0.03$ (well within bootstrap noise on
  $\binom{N}{2}$ pairs).
- "Drops mildly" $:= 0.03 \le |\Delta_X| < 0.15$.
- "Drops sharply" $:= |\Delta_X| \ge 0.15$.

A bootstrap CI over the $\binom{7}{2} = 21$ (or $\binom{12}{2} = 66$) pairs
would be more rigorous and is a stretch goal for the script.
